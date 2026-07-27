from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any

import numpy as np
from scipy.linalg import eigh
from scipy.optimize import minimize

from .axis import band_grid
from .model import PWGalerkinContext


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
    axis_gradient_gaps: list[float]
    minimum_generalized_vector: np.ndarray
    base_matrix: np.ndarray
    core_matrix: np.ndarray

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
    context: PWGalerkinContext,
    core_points: np.ndarray,
    axis_step: float = 0.1,
    initial_axis_nodes: int = 7,
    max_outer: int = 18,
    maxiter: int = 220,
) -> JointDualResult:
    core_points = np.asarray(core_points, dtype=complex).reshape(-1)
    core_matrices = context.core_matrices(core_points)
    grids = [
        band_grid(band, axis_step)
        for band in context.bands
    ]
    axis_transforms = [
        context.axis_transforms(grid)
        for grid in grids
    ]
    coefficients = context.count_coefficients
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
                axis_transforms,
                active,
            )
        ]
        sizes = [len(matrices) for matrices in active_matrices]
        sizes.append(len(core_matrices))
        offsets = np.cumsum([0] + sizes)
        variable_count = int(offsets[-1])

        def unpack(vector: np.ndarray) -> list[np.ndarray]:
            return [
                vector[offsets[index] : offsets[index + 1]]
                for index in range(len(sizes))
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
            eigenvalues, eigenvectors = eigh(
                0.5 * (core + core.T),
                0.5 * (base + base.T),
                subset_by_index=[0, 0],
                check_finite=False,
            )
            eigenvalue = float(eigenvalues[0])
            eigenvector = eigenvectors[:, 0]
            if eigenvalue >= -1e-15:
                return (
                    100.0,
                    np.zeros_like(vector),
                    eigenvalue,
                    eigenvector,
                    base,
                    core,
                )
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
            for group in range(len(grids)):
                old = {
                    index: previous_weights[group][position]
                    for position, index in enumerate(
                        previous_active[group]
                    )
                }
                values = np.asarray(
                    [old.get(index, 1e-5) for index in active[group]]
                )
                groups.append(values / np.sum(values))
            groups.append(previous_weights[-1])
            initial = np.concatenate(groups)

        constraints = []
        for group in range(len(sizes)):
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
                "ftol": 2e-10,
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
        additions: list[tuple[int, int]] = []
        gaps = []
        for group, transforms in enumerate(axis_transforms):
            scores = (transforms @ eigenvector) ** 2
            best_index = int(np.argmax(scores))
            active_maximum = float(
                np.max(scores[active[group]])
            )
            gaps.append(
                float(scores[best_index] - active_maximum)
            )
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

    if final is None:
        raise RuntimeError("joint optimization produced no iterate")
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
        np.linalg.eigvalsh(
            0.5 * (witness + witness.T)
        )[0]
    )
    axis_supports = []
    for indices, group_weights, grid in zip(
        final_active,
        weights[:-1],
        grids,
    ):
        axis_supports.append(
            [
                {
                    "x": float(grid[index]),
                    "weight": float(group_weights[position]),
                }
                for position, index in enumerate(indices)
                if group_weights[position] > 1e-8
            ]
        )
    core_support = [
        {
            "point_index": int(index),
            "x": float(core_points[index].real),
            "y": float(core_points[index].imag),
            "weight": float(weights[-1][index]),
        }
        for index in np.flatnonzero(weights[-1] > 1e-8)
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
        axis_gradient_gaps=gaps,
        minimum_generalized_vector=eigenvector,
        base_matrix=base,
        core_matrix=core,
    )


def reconstruct_atomic_witness(
    context: PWGalerkinContext,
    joint: dict[str, Any],
) -> dict[str, float | bool]:
    base = context.tail_matrix.copy()
    for band_index, support in enumerate(joint["axis_supports"]):
        raw_weights = np.asarray(
            [row["weight"] for row in support],
            dtype=float,
        )
        weights = raw_weights / np.sum(raw_weights)
        points = np.asarray(
            [row["x"] for row in support],
            dtype=float,
        )
        transforms = context.axis_transforms(points)
        base += (
            context.count_coefficients[band_index]
            * np.tensordot(
                weights,
                np.einsum(
                    "ki,kj->kij",
                    transforms,
                    transforms,
                ),
                axes=1,
            )
        )
    core_support = joint["core_support"]
    raw_core_weights = np.asarray(
        [row["weight"] for row in core_support],
        dtype=float,
    )
    core_weights = raw_core_weights / np.sum(raw_core_weights)
    core_points = np.asarray(
        [
            complex(row["x"], row["y"])
            for row in core_support
        ]
    )
    core = np.tensordot(
        core_weights,
        context.core_matrices(core_points),
        axes=1,
    )
    safe = base + float(joint["safe_alpha"]) * core
    raw = base + float(joint["alpha"]) * core
    raw_generalized = float(
        eigh(
            core,
            base,
            eigvals_only=True,
            subset_by_index=[0, 0],
            check_finite=False,
        )[0]
    )
    threshold = (
        -1.0 / raw_generalized
        if raw_generalized < -1e-14
        else float("inf")
    )
    return {
        "dimension": context.dimension,
        "raw_threshold_for_fixed_measures": float(threshold),
        "safe_minimum_eigenvalue": float(
            np.linalg.eigvalsh(
                0.5 * (safe + safe.T)
            )[0]
        ),
        "raw_minimum_eigenvalue": float(
            np.linalg.eigvalsh(
                0.5 * (raw + raw.T)
            )[0]
        ),
        "safe_psd": bool(
            np.linalg.eigvalsh(
                0.5 * (safe + safe.T)
            )[0]
            >= -1e-9
        ),
    }
