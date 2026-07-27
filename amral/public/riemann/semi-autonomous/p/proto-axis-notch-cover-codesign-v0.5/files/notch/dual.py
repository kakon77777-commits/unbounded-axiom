from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any

import numpy as np
from scipy.linalg import eigh, solve_triangular
from scipy.optimize import minimize

from .context import FrontierContext
from .cover import Patch


def generalized_negative_threshold(
    core_matrix: np.ndarray,
    positive_matrix: np.ndarray,
) -> float:
    value = float(
        eigh(
            0.5 * (core_matrix + core_matrix.T),
            0.5 * (positive_matrix + positive_matrix.T),
            eigvals_only=True,
            subset_by_index=[0, 0],
            check_finite=False,
        )[0]
    )
    if value >= -1e-13:
        return math.inf
    return -1.0 / value


def rank_two_point_thresholds(
    transforms: np.ndarray,
    positive_matrix: np.ndarray,
) -> np.ndarray:
    """Compute point-core thresholds using the rank-two core identity."""
    transform = np.asarray(transforms, dtype=complex)
    lower = np.linalg.cholesky(
        0.5 * (positive_matrix + positive_matrix.T)
    )
    real = solve_triangular(
        lower,
        transform.real.T,
        lower=True,
        check_finite=False,
    ).T
    imag = solve_triangular(
        lower,
        transform.imag.T,
        lower=True,
        check_finite=False,
    ).T
    a = 2.0 * np.sum(real * real, axis=1)
    b = 2.0 * np.sum(imag * imag, axis=1)
    c = 2.0 * np.sum(real * imag, axis=1)
    discriminant = np.maximum(0.0, (a + b) ** 2 - 4.0 * c * c)
    negative = 0.5 * ((a - b) - np.sqrt(discriminant))
    return np.where(negative < -1e-13, -1.0 / negative, np.inf)


def uniform_core_threshold(
    context: FrontierContext,
    patch: Patch,
    positive_matrix: np.ndarray,
    nx: int = 3,
    ny: int = 3,
) -> float:
    matrices = context.core_matrices(patch.points(nx, ny))
    return generalized_negative_threshold(
        np.mean(matrices, axis=0),
        positive_matrix,
    )


def optimize_core_measure(
    core_matrices: np.ndarray,
    positive_matrix: np.ndarray,
    maxiter: int = 160,
) -> dict[str, Any]:
    core_matrices = np.asarray(core_matrices, dtype=float)
    count = len(core_matrices)

    def value_gradient(weights: np.ndarray) -> tuple[float, np.ndarray]:
        core = np.tensordot(weights, core_matrices, axes=1)
        values, vectors = eigh(
            0.5 * (core + core.T),
            0.5 * (positive_matrix + positive_matrix.T),
            subset_by_index=[0, 0],
            check_finite=False,
        )
        eigenvalue = float(values[0])
        vector = vectors[:, 0]
        derivative = np.einsum(
            "i,kij,j->k",
            vector,
            core_matrices,
            vector,
        )
        return math.log(-eigenvalue), derivative / eigenvalue

    starts = [np.full(count, 1.0 / count)]
    starts.extend(np.eye(count))
    best: tuple[float, Any] | None = None
    for start in starts:
        result = minimize(
            lambda weights: value_gradient(weights)[0],
            start,
            jac=lambda weights: value_gradient(weights)[1],
            method="SLSQP",
            bounds=[(0.0, 1.0)] * count,
            constraints={
                "type": "eq",
                "fun": lambda weights: float(np.sum(weights) - 1.0),
                "jac": lambda weights: np.ones(count),
            },
            options={"ftol": 1e-10, "maxiter": maxiter},
        )
        threshold = float(math.exp(-result.fun))
        if best is None or threshold > best[0]:
            best = (threshold, result)
    assert best is not None
    threshold, result = best
    return {
        "threshold": threshold,
        "weights": np.asarray(result.x),
        "optimizer_success": bool(result.success),
        "optimizer_message": str(result.message),
        "iterations": int(result.nit),
    }


@dataclass
class JointDualResult:
    alpha: float
    safe_alpha: float
    safe_min_eigenvalue: float
    axis_supports: list[list[dict[str, float]]]
    core_support: list[dict[str, float]]
    outer_iterations: int
    optimizer_success: bool
    optimizer_message: str
    active_axis_counts: list[int]
    witness_matrix: np.ndarray
    base_matrix: np.ndarray
    core_matrix: np.ndarray
    minimum_generalized_vector: np.ndarray
    axis_gradient_gaps: list[float]

    def to_summary(self) -> dict[str, Any]:
        return {
            "alpha": self.alpha,
            "safe_alpha": self.safe_alpha,
            "safe_min_eigenvalue": self.safe_min_eigenvalue,
            "axis_supports": self.axis_supports,
            "core_support": self.core_support,
            "outer_iterations": self.outer_iterations,
            "optimizer_success": self.optimizer_success,
            "optimizer_message": self.optimizer_message,
            "active_axis_counts": self.active_axis_counts,
            "axis_gradient_gaps": self.axis_gradient_gaps,
        }


def cutting_plane_joint_dual(
    context: FrontierContext,
    core_points: np.ndarray,
    band_indices: tuple[int, ...] = (0, 1, 2, 3, 4),
    axis_step: float = 0.25,
    initial_axis_nodes: int = 7,
    max_outer: int = 14,
    maxiter: int = 180,
) -> JointDualResult:
    core_points = np.asarray(core_points, dtype=complex).reshape(-1)
    core_matrices = context.core_matrices(core_points)
    grids: list[np.ndarray] = []
    full_axis_transforms: list[np.ndarray] = []
    coefficients: list[float] = []
    for index in band_indices:
        band = context.bands[index]
        size = int(round((band.stop - band.start) / axis_step)) + 1
        grid = np.linspace(band.start, band.stop, size)
        grids.append(grid)
        full_axis_transforms.append(context.axis_transforms(grid))
        coefficients.append(float(context.count_coefficients[index]))

    active = [
        sorted(
            set(
                np.linspace(0, len(grid) - 1, initial_axis_nodes)
                .round()
                .astype(int)
                .tolist()
            )
        )
        for grid in grids
    ]
    previous_weights: list[np.ndarray] | None = None
    previous_active: list[list[int]] | None = None
    final: tuple[Any, ...] | None = None

    for outer in range(max_outer):
        active_matrices = [
            np.einsum(
                "ki,kj->kij",
                transforms[indices],
                transforms[indices],
            )
            for transforms, indices in zip(
                full_axis_transforms,
                active,
            )
        ]
        sizes = [len(item) for item in active_matrices]
        sizes.append(len(core_matrices))
        offsets = np.cumsum([0] + sizes)
        variable_count = int(offsets[-1])
        group_count = len(band_indices) + 1

        def unpack(vector: np.ndarray) -> list[np.ndarray]:
            return [
                vector[offsets[k] : offsets[k + 1]]
                for k in range(group_count)
            ]

        def value_gradient(
            vector: np.ndarray,
        ) -> tuple[
            float,
            np.ndarray,
            float,
            np.ndarray,
            np.ndarray,
            np.ndarray,
        ]:
            weights = unpack(vector)
            base = context.tail_matrix.copy()
            for group, (coefficient, matrices) in enumerate(
                zip(coefficients, active_matrices)
            ):
                base += coefficient * np.tensordot(
                    weights[group],
                    matrices,
                    axes=1,
                )
            core = np.tensordot(
                weights[-1],
                core_matrices,
                axes=1,
            )
            values, vectors = eigh(
                0.5 * (core + core.T),
                0.5 * (base + base.T),
                subset_by_index=[0, 0],
                check_finite=False,
            )
            eigenvalue = float(values[0])
            eigenvector = vectors[:, 0]
            gradient = np.empty_like(vector)
            for group, (coefficient, matrices) in enumerate(
                zip(coefficients, active_matrices)
            ):
                gradient[
                    offsets[group] : offsets[group + 1]
                ] = -coefficient * np.einsum(
                    "i,kij,j->k",
                    eigenvector,
                    matrices,
                    eigenvector,
                )
            gradient[offsets[-2] : offsets[-1]] = (
                np.einsum(
                    "i,kij,j->k",
                    eigenvector,
                    core_matrices,
                    eigenvector,
                )
                / eigenvalue
            )
            return (
                math.log(-eigenvalue),
                gradient,
                eigenvalue,
                eigenvector,
                0.5 * (base + base.T),
                0.5 * (core + core.T),
            )

        if previous_weights is None:
            initial = np.concatenate(
                [np.full(size, 1.0 / size) for size in sizes]
            )
        else:
            assert previous_active is not None
            groups = []
            for group in range(len(band_indices)):
                old = {
                    index: previous_weights[group][position]
                    for position, index in enumerate(
                        previous_active[group]
                    )
                }
                values = np.asarray(
                    [old.get(index, 1e-4) for index in active[group]]
                )
                groups.append(values / np.sum(values))
            groups.append(previous_weights[-1])
            initial = np.concatenate(groups)

        constraints = []
        for group in range(group_count):
            left = int(offsets[group])
            right = int(offsets[group + 1])
            jacobian = np.zeros(variable_count)
            jacobian[left:right] = 1.0
            constraints.append(
                {
                    "type": "eq",
                    "fun": (
                        lambda vector, left=left, right=right:
                        float(np.sum(vector[left:right]) - 1.0)
                    ),
                    "jac": (
                        lambda vector, jacobian=jacobian: jacobian
                    ),
                }
            )

        result = minimize(
            lambda vector: value_gradient(vector)[0],
            initial,
            jac=lambda vector: value_gradient(vector)[1],
            method="SLSQP",
            bounds=[(0.0, 1.0)] * variable_count,
            constraints=constraints,
            options={
                "ftol": 1e-9,
                "maxiter": maxiter,
                "disp": False,
            },
        )
        (
            _,
            _,
            eigenvalue,
            eigenvector,
            base,
            core,
        ) = value_gradient(result.x)
        weights = unpack(result.x)
        old_active = [indices.copy() for indices in active]
        additions = []
        gaps = []
        for group, transforms in enumerate(full_axis_transforms):
            scores = (transforms @ eigenvector) ** 2
            best_index = int(np.argmax(scores))
            active_maximum = float(np.max(scores[active[group]]))
            gaps.append(float(scores[best_index] - active_maximum))
            if best_index not in active[group]:
                active[group].append(best_index)
                active[group].sort()
                additions.append((group, best_index))
        previous_weights = [item.copy() for item in weights]
        previous_active = old_active
        final = (
            outer,
            result,
            eigenvalue,
            eigenvector,
            base,
            core,
            weights,
            old_active,
            gaps,
        )
        if not additions:
            break

    assert final is not None
    (
        outer,
        result,
        eigenvalue,
        eigenvector,
        base,
        core,
        weights,
        final_active,
        gaps,
    ) = final
    alpha = -1.0 / float(eigenvalue)
    safe_alpha = (
        1.0 + 0.5 * (alpha - 1.0)
        if alpha > 1.0
        else 0.995 * alpha
    )
    witness = base + safe_alpha * core
    safe_minimum = float(
        np.linalg.eigvalsh(0.5 * (witness + witness.T))[0]
    )

    axis_supports = []
    for group, (indices, group_weights, grid) in enumerate(
        zip(final_active, weights[:-1], grids)
    ):
        axis_supports.append(
            [
                {
                    "x": float(grid[index]),
                    "weight": float(group_weights[position]),
                }
                for position, index in enumerate(indices)
                if group_weights[position] > 1e-7
            ]
        )
    core_support = [
        {
            "point_index": int(index),
            "x": float(core_points[index].real),
            "y": float(core_points[index].imag),
            "weight": float(weights[-1][index]),
        }
        for index in np.flatnonzero(weights[-1] > 1e-7)
    ]
    return JointDualResult(
        alpha=float(alpha),
        safe_alpha=float(safe_alpha),
        safe_min_eigenvalue=safe_minimum,
        axis_supports=axis_supports,
        core_support=core_support,
        outer_iterations=int(outer + 1),
        optimizer_success=bool(result.success),
        optimizer_message=str(result.message),
        active_axis_counts=[len(item) for item in final_active],
        witness_matrix=0.5 * (witness + witness.T),
        base_matrix=base,
        core_matrix=core,
        minimum_generalized_vector=eigenvector,
        axis_gradient_gaps=gaps,
    )
