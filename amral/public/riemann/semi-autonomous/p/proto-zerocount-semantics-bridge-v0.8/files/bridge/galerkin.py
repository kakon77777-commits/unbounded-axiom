from __future__ import annotations

import functools
import math
from dataclasses import dataclass
from typing import Any

import numpy as np
from numpy.polynomial import Chebyshev
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
from scipy.linalg import eigh, null_space
from scipy.optimize import minimize

from .axis import AxisBand, default_axis_bands, s_bound


@functools.lru_cache(maxsize=None)
def source_aligned_tail_multiplier(
    start: float = 145.0,
    split: int = 500,
) -> float:
    def density(t: float) -> float:
        return (
            1.0
            + math.log(t + 1.0) / (2.0 * math.pi)
            + 2.0 * s_bound(t + 1.0)
        )

    first_shell = int(math.ceil(start))
    finite = sum(
        density(float(n)) / (n**4)
        for n in range(first_shell, split)
    )
    continuation = quad(
        lambda value: density(value) / value**4,
        float(split),
        np.inf,
        epsabs=1e-14,
        epsrel=1e-11,
    )[0]
    return float(finite + 1.05 * continuation)


@functools.lru_cache(maxsize=8)
def gauss_rule(order: int) -> tuple[np.ndarray, np.ndarray]:
    nodes, weights = leggauss(order)
    nodes.setflags(write=False)
    weights.setflags(write=False)
    return nodes, weights


def clamped_even_chebyshev(
    normalized_t: np.ndarray,
    raw_dimension: int,
    radius: float,
) -> tuple[np.ndarray, np.ndarray]:
    window = Chebyshev(
        [3.0 / 8.0, 0.0, -0.5, 0.0, 1.0 / 8.0]
    )
    values = []
    seconds = []
    for index in range(raw_dimension):
        polynomial = window * Chebyshev.basis(2 * index)
        values.append(polynomial(normalized_t))
        seconds.append(
            polynomial.deriv(2)(normalized_t) / (radius * radius)
        )
    return np.stack(values, axis=1), np.stack(seconds, axis=1)


def band_grid(band: AxisBand, step: float) -> np.ndarray:
    return np.linspace(
        band.start,
        band.stop,
        int(round((band.stop - band.start) / step)) + 1,
    )


@dataclass
class PWGalerkinContext:
    radius: float
    raw_dimension: int
    count_coefficients_input: tuple[float, ...]
    quadrature_order: int = 2048
    whitening_rcond: float = 1e-12

    def __post_init__(self) -> None:
        if self.raw_dimension < 5:
            raise ValueError("raw_dimension must be at least five")
        self.bands = default_axis_bands()
        if len(self.count_coefficients_input) != len(self.bands):
            raise ValueError("one count coefficient is required per band")
        self.count_coefficients = np.asarray(
            self.count_coefficients_input,
            dtype=float,
        )
        nodes, base_weights = gauss_rule(self.quadrature_order)
        self.t = self.radius * nodes
        self.weights = self.radius * base_weights
        basis, second = clamped_even_chebyshev(
            nodes,
            self.raw_dimension,
            self.radius,
        )
        self.tail_scale = (
            2.0
            * self.radius
            * source_aligned_tail_multiplier()
        )
        tail_gram = (
            self.tail_scale
            * second.T
            @ (self.weights[:, None] * second)
        )
        structural_rows = np.vstack(
            (
                basis.T @ self.weights,
                basis.T
                @ (self.weights * np.cosh(0.5 * self.t)),
            )
        )
        kernel = null_space(
            structural_rows,
            rcond=self.whitening_rcond,
        )
        reduced_tail = kernel.T @ tail_gram @ kernel
        values, vectors = eigh(
            0.5 * (reduced_tail + reduced_tail.T)
        )
        cutoff = self.whitening_rcond * float(values[-1])
        keep = values > cutoff
        self.coordinate_map = (
            kernel
            @ vectors[:, keep]
            @ np.diag(1.0 / np.sqrt(values[keep]))
        )
        self.weighted_coordinate_basis = (
            self.weights[:, None]
            * basis
            @ self.coordinate_map
        )
        self.tail_matrix = np.eye(self.coordinate_map.shape[1])
        self.structural_residuals = {
            "G0": float(
                np.max(
                    np.abs(
                        structural_rows[0] @ self.coordinate_map
                    )
                )
            ),
            "Gi2": float(
                np.max(
                    np.abs(
                        structural_rows[1] @ self.coordinate_map
                    )
                )
            ),
        }

    @property
    def dimension(self) -> int:
        return int(self.coordinate_map.shape[1])

    def transform(
        self,
        points: np.ndarray,
        batch_size: int = 128,
    ) -> np.ndarray:
        points = np.asarray(points, dtype=complex).reshape(-1)
        output = np.empty(
            (len(points), self.dimension),
            dtype=complex,
        )
        for start in range(0, len(points), batch_size):
            stop = min(start + batch_size, len(points))
            output[start:stop] = (
                np.exp(
                    1j
                    * np.outer(points[start:stop], self.t)
                )
                @ self.weighted_coordinate_basis
            )
        return output

    def axis_transforms(self, points: np.ndarray) -> np.ndarray:
        return self.transform(np.asarray(points, dtype=float)).real

    def core_values(
        self,
        points: np.ndarray,
        vector: np.ndarray,
    ) -> np.ndarray:
        values = self.transform(points) @ vector
        return 2.0 * np.real(values * values)

    def core_matrices(self, points: np.ndarray) -> np.ndarray:
        transform = self.transform(points)
        return np.asarray(
            [
                2.0 * np.real(np.outer(row, row))
                for row in transform
            ]
        )


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
    axis_step: float = 0.05,
    initial_axis_nodes: int = 7,
    max_outer: int = 28,
    maxiter: int = 320,
) -> JointDualResult:
    """Optimize atomic measures for the nonzero coefficient bands."""

    core_points = np.asarray(core_points, dtype=complex).reshape(-1)
    core_matrices = context.core_matrices(core_points)
    active_band_indices = [
        index
        for index, coefficient in enumerate(
            context.count_coefficients
        )
        if coefficient > 0
    ]
    grids = [
        band_grid(context.bands[index], axis_step)
        for index in active_band_indices
    ]
    axis_transforms = [
        context.axis_transforms(grid)
        for grid in grids
    ]
    coefficients = np.asarray(
        [
            context.count_coefficients[index]
            for index in active_band_indices
        ],
        dtype=float,
    )
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
        np.linalg.eigvalsh(0.5 * (witness + witness.T))[0]
    )
    axis_supports: list[list[dict[str, float]]] = [
        [] for _ in context.bands
    ]
    for band_index, indices, group_weights, grid in zip(
        active_band_indices,
        final_active,
        weights[:-1],
        grids,
    ):
        axis_supports[band_index] = [
            {
                "x": float(grid[index]),
                "weight": float(group_weights[position]),
            }
            for position, index in enumerate(indices)
            if group_weights[position] > 1e-8
        ]
    core_support = [
        {
            "point_index": int(index),
            "x": float(core_points[index].real),
            "y": float(core_points[index].imag),
            "weight": float(weights[-1][index]),
        }
        for index in np.flatnonzero(weights[-1] > 1e-8)
    ]
    active_counts = [0 for _ in context.bands]
    gradient_gaps = [0.0 for _ in context.bands]
    for band_index, count, gap in zip(
        active_band_indices,
        [len(item) for item in final_active],
        gaps,
    ):
        active_counts[band_index] = count
        gradient_gaps[band_index] = gap
    return JointDualResult(
        alpha=float(alpha),
        safe_alpha=float(safe_alpha),
        safe_min_eigenvalue=safe_minimum,
        axis_supports=axis_supports,
        core_support=core_support,
        outer_iterations=int(outer + 1),
        optimizer_success=bool(result.success),
        optimizer_message=str(result.message),
        active_axis_counts=active_counts,
        axis_gradient_gaps=gradient_gaps,
        minimum_generalized_vector=eigenvector,
        base_matrix=base,
        core_matrix=core,
    )


def dense_primal_escape_diagnostic(
    context: PWGalerkinContext,
    vector: np.ndarray,
    patch: Any,
    core_grid_size: int = 101,
    axis_step: float = 0.01,
) -> dict[str, Any]:
    points = patch.points(core_grid_size, core_grid_size)
    core_values = context.core_values(points, vector)
    core_maximum = float(np.max(core_values))
    if core_maximum >= 0:
        raise ArithmeticError("candidate has no uniform grid negativity")
    scale = -1.0 / core_maximum
    axis_rows = []
    objective_raw = float(vector @ vector)
    for band, coefficient in zip(
        context.bands,
        context.count_coefficients,
    ):
        grid = band_grid(band, axis_step)
        values = (context.axis_transforms(grid) @ vector) ** 2
        maximum_index = int(np.argmax(values))
        maximum = float(values[maximum_index])
        objective_raw += float(coefficient) * maximum
        axis_rows.append(
            {
                "band_id": band.band_id,
                "coefficient": float(coefficient),
                "sampled_maximum": maximum,
                "sampled_argmax": float(grid[maximum_index]),
                "sampled_charge": float(coefficient) * maximum,
            }
        )
    return {
        "core_grid": [core_grid_size, core_grid_size],
        "axis_step": axis_step,
        "raw_core_minimum": float(np.min(core_values)),
        "raw_core_maximum": core_maximum,
        "normalization_scale": scale,
        "normalized_core_minimum": float(
            scale * np.min(core_values)
        ),
        "normalized_core_maximum": -1.0,
        "tail_raw": float(vector @ vector),
        "axis_rows": axis_rows,
        "normalized_objective": float(scale * objective_raw),
        "below_one_on_sampled_problem": bool(
            scale * objective_raw < 1.0
        ),
        "continuous_patch_certified": False,
        "evidence_level": "E2 dense-grid Galerkin diagnostic",
    }
