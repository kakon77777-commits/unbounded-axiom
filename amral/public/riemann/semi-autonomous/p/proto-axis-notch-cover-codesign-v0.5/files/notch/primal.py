from __future__ import annotations

from typing import Any

import numpy as np
from scipy.linalg import eigh
from scipy.optimize import linprog

from .context import FrontierContext
from .dual import JointDualResult


def audit_rank_one_direction(
    context: FrontierContext,
    direction: np.ndarray,
    core_points: np.ndarray,
    core_nx: int = 81,
    core_ny: int = 61,
    axis_step: float = 0.025,
) -> dict[str, Any]:
    direction = np.asarray(direction, dtype=float)
    xs = np.linspace(
        float(np.min(core_points.real)),
        float(np.max(core_points.real)),
        core_nx,
    )
    ys = np.linspace(
        float(np.min(core_points.imag)),
        float(np.max(core_points.imag)),
        core_ny,
    )
    dense_core_points = (
        xs[:, None] + 1j * ys[None, :]
    ).reshape(-1)
    core_transform = context.transform(dense_core_points)
    core_values = 2.0 * np.real(
        (core_transform @ direction) ** 2
    )
    core_maximum = float(np.max(core_values))
    scale_squared = (
        -1.0 / core_maximum
        if core_maximum < 0.0
        else float("inf")
    )
    band_rows = []
    for index, band in enumerate(context.bands):
        size = int(round((band.stop - band.start) / axis_step)) + 1
        grid = np.linspace(band.start, band.stop, size)
        values = (context.axis_transforms(grid) @ direction) ** 2
        maximum_index = int(np.argmax(values))
        maximum = float(values[maximum_index])
        band_rows.append(
            {
                "band_id": band.band_id,
                "maximum": maximum,
                "maximum_x": float(grid[maximum_index]),
                "charge": float(
                    context.count_coefficients[index] * maximum
                ),
            }
        )
    tail = float(direction @ context.tail_matrix @ direction)
    objective = scale_squared * (
        tail + sum(row["charge"] for row in band_rows)
    )
    return {
        "dense_core_point_count": len(dense_core_points),
        "dense_core_range": [
            float(np.min(core_values)),
            core_maximum,
        ],
        "scale_squared": scale_squared,
        "tail_unscaled": tail,
        "band_rows": band_rows,
        "scaled_objective": objective,
        "finite_rank_one_pass": bool(
            core_maximum < 0.0 and objective < 1.0
        ),
    }


def candidate_rays_from_dual(
    context: FrontierContext,
    core_points: np.ndarray,
    dual: JointDualResult,
    random_count: int = 32,
    bottom_count: int = 12,
    seed: int = 20260724,
) -> np.ndarray:
    core_matrices = context.core_matrices(core_points)
    rays = []
    for matrix in core_matrices:
        _, vectors = eigh(
            0.5 * (matrix + matrix.T),
            dual.base_matrix,
            subset_by_index=[0, 0],
            check_finite=False,
        )
        rays.append(vectors[:, 0])
    rng = np.random.default_rng(seed)
    for _ in range(random_count):
        weights = rng.dirichlet(np.ones(len(core_matrices)))
        matrix = np.tensordot(weights, core_matrices, axes=1)
        _, vectors = eigh(
            0.5 * (matrix + matrix.T),
            dual.base_matrix,
            subset_by_index=[0, 0],
            check_finite=False,
        )
        rays.append(vectors[:, 0])
    critical = (
        dual.base_matrix + dual.alpha * dual.core_matrix
    )
    _, vectors = np.linalg.eigh(0.5 * (critical + critical.T))
    rays.extend(vectors[:, : min(bottom_count, len(vectors))].T)
    rays.append(dual.minimum_generalized_vector)
    normalized = []
    for ray in rays:
        norm = float(np.linalg.norm(ray))
        if norm <= 1e-14:
            continue
        candidate = np.asarray(ray, dtype=float) / norm
        if not any(
            abs(float(candidate @ prior)) > 1.0 - 1e-9
            for prior in normalized
        ):
            normalized.append(candidate)
    return np.column_stack(normalized)


def solve_ray_cone_primal(
    context: FrontierContext,
    core_points: np.ndarray,
    rays: np.ndarray,
    axis_step: float = 0.25,
) -> dict[str, Any]:
    rays = np.asarray(rays, dtype=float)
    core_matrices = context.core_matrices(core_points)
    core_table = np.einsum(
        "ik,qij,jk->qk",
        rays,
        core_matrices,
        rays,
    )
    ray_count = rays.shape[1]
    band_count = len(context.bands)
    tail = np.einsum(
        "ik,ij,jk->k",
        rays,
        context.tail_matrix,
        rays,
    )
    rows = [
        np.column_stack(
            (core_table, np.zeros((len(core_table), band_count)))
        )
    ]
    bounds_rows = [-np.ones(len(core_table))]
    axis_tables = []
    for band_index, band in enumerate(context.bands):
        size = int(round((band.stop - band.start) / axis_step)) + 1
        grid = np.linspace(band.start, band.stop, size)
        transform = context.axis_transforms(grid) @ rays
        table = transform * transform
        axis_tables.append((grid, table))
        band_part = np.zeros((len(grid), band_count))
        band_part[:, band_index] = -1.0
        rows.append(np.column_stack((table, band_part)))
        bounds_rows.append(np.zeros(len(grid)))
    objective = np.concatenate(
        (tail, context.count_coefficients)
    )
    result = linprog(
        objective,
        A_ub=np.vstack(rows),
        b_ub=np.concatenate(bounds_rows),
        bounds=[(0.0, None)] * (ray_count + band_count),
        method="highs",
    )
    output: dict[str, Any] = {
        "solver_success": bool(result.success),
        "solver_message": str(result.message),
        "ray_count": ray_count,
        "axis_step": axis_step,
    }
    if not result.success:
        return output
    weights = np.asarray(result.x[:ray_count])
    band_bounds = np.asarray(result.x[ray_count:])
    gram = (rays * weights[None, :]) @ rays.T
    output.update(
        {
            "objective": float(result.fun),
            "active_ray_count": int(np.sum(weights > 1e-9)),
            "weights": weights.tolist(),
            "band_bounds": band_bounds.tolist(),
            "gram": gram.tolist(),
            "sampled_core_max": float(
                np.max(
                    np.einsum(
                        "qij,ij->q",
                        core_matrices,
                        gram,
                    )
                )
            ),
            "gram_numerical_rank": int(
                np.sum(np.linalg.eigvalsh(gram) > 1e-9)
            ),
        }
    )
    return output


def audit_gram_candidate(
    context: FrontierContext,
    gram: np.ndarray,
    core_points: np.ndarray,
    core_nx: int = 81,
    core_ny: int = 61,
    axis_step: float = 0.025,
) -> dict[str, Any]:
    gram = np.asarray(gram, dtype=float)
    xs = np.linspace(
        float(np.min(core_points.real)),
        float(np.max(core_points.real)),
        core_nx,
    )
    ys = np.linspace(
        float(np.min(core_points.imag)),
        float(np.max(core_points.imag)),
        core_ny,
    )
    points = (xs[:, None] + 1j * ys[None, :]).reshape(-1)
    transform = context.transform(points)
    core_values = 2.0 * np.real(
        np.einsum("ki,ij,kj->k", transform, gram, transform)
    )
    band_rows = []
    for index, band in enumerate(context.bands):
        size = int(round((band.stop - band.start) / axis_step)) + 1
        grid = np.linspace(band.start, band.stop, size)
        axis = context.axis_transforms(grid)
        values = np.einsum("ki,ij,kj->k", axis, gram, axis)
        maximum_index = int(np.argmax(values))
        band_rows.append(
            {
                "band_id": band.band_id,
                "maximum": float(values[maximum_index]),
                "maximum_x": float(grid[maximum_index]),
                "charge": float(
                    context.count_coefficients[index]
                    * values[maximum_index]
                ),
            }
        )
    tail = float(np.sum(context.tail_matrix * gram))
    objective = tail + sum(row["charge"] for row in band_rows)
    eigenvalues = np.linalg.eigvalsh(0.5 * (gram + gram.T))
    return {
        "dense_core_point_count": len(points),
        "dense_core_range": [
            float(np.min(core_values)),
            float(np.max(core_values)),
        ],
        "tail": tail,
        "band_rows": band_rows,
        "dense_objective": objective,
        "minimum_gram_eigenvalue": float(eigenvalues[0]),
        "gram_numerical_rank": int(np.sum(eigenvalues > 1e-9)),
        "finite_dense_pass": bool(
            np.max(core_values) <= -1.0 and objective < 1.0
        ),
    }
