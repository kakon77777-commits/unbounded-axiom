from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.linalg import eigh

from .model import (
    rank_two_threshold_from_gram,
    source_aligned_tail_multiplier,
)


def trapezoid_weights(size: int, step: float) -> np.ndarray:
    weights = np.full(size, step, dtype=float)
    weights[0] = weights[-1] = step / 2.0
    return weights


def even_evaluation_densities(
    t: np.ndarray,
    point: complex,
) -> tuple[np.ndarray, np.ndarray]:
    x = float(complex(point).real)
    y = float(complex(point).imag)
    real = np.cos(x * t) * np.cosh(y * t)
    imag = -np.sin(x * t) * np.sinh(y * t)
    return real, imag


def clamped_green_kernel(
    s: np.ndarray | float,
    t: np.ndarray | float,
    radius: float,
    tail_scale: float,
) -> np.ndarray:
    """Explicit inverse kernel of tail_scale*D^4 on a clamped interval."""
    s_array, t_array = np.broadcast_arrays(
        np.asarray(s, dtype=float),
        np.asarray(t, dtype=float),
    )
    length = 2.0 * radius
    xi = s_array + radius
    eta = t_array + radius
    lower = np.minimum(xi, eta)
    upper = np.maximum(xi, eta)
    return (
        lower
        * lower
        * (length - upper) ** 2
        * (
            3.0 * upper * length
            - (length + 2.0 * upper) * lower
        )
        / (6.0 * length**3 * tail_scale)
    )


def clamped_representer(
    density: np.ndarray,
    t: np.ndarray,
    tail_scale: float,
) -> np.ndarray:
    """Solve tail_scale*k''''=density with clamped end conditions."""
    t = np.asarray(t, dtype=float)
    density = np.asarray(density, dtype=float)
    if density.ndim == 1:
        density = density[:, None]
        squeeze = True
    else:
        squeeze = False
    moments = []
    for power in range(4):
        moments.append(
            cumulative_trapezoid(
                (t**power)[:, None] * density,
                t,
                axis=0,
                initial=0.0,
            )
        )
    f0, f1, f2, f3 = moments
    particular = (
        (t**3)[:, None] * f0
        - 3.0 * (t**2)[:, None] * f1
        + 3.0 * t[:, None] * f2
        - f3
    ) / (6.0 * tail_scale)
    right = float(t[-1])
    left = float(t[0])
    length = right - left
    value_right = particular[-1]
    slope_right = (
        right * right * f0[-1]
        - 2.0 * right * f1[-1]
        + f2[-1]
    ) / (2.0 * tail_scale)
    cubic = (
        2.0 * value_right - length * slope_right
    ) / (length**3)
    quadratic = (
        length * slope_right - 3.0 * value_right
    ) / (length**2)
    shifted = (t - left)[:, None]
    result = (
        particular
        + quadratic[None, :] * shifted * shifted
        + cubic[None, :] * shifted * shifted * shifted
    )
    return result[:, 0] if squeeze else result


def inner_products(
    densities: np.ndarray,
    representers: np.ndarray,
    weights: np.ndarray,
) -> np.ndarray:
    densities = np.asarray(densities, dtype=float)
    representers = np.asarray(representers, dtype=float)
    if densities.ndim == 1:
        densities = densities[:, None]
    if representers.ndim == 1:
        representers = representers[:, None]
    return densities.T @ (weights[:, None] * representers)


@dataclass
class GreenRankTwoScanner:
    radius: float
    time_step: float
    tail_scale_override: float | None = None

    def __post_init__(self) -> None:
        count = int(round(2.0 * self.radius / self.time_step)) + 1
        self.t = np.linspace(-self.radius, self.radius, count)
        self.actual_step = float(self.t[1] - self.t[0])
        self.weights = trapezoid_weights(
            len(self.t),
            self.actual_step,
        )
        self.tail_scale = (
            float(self.tail_scale_override)
            if self.tail_scale_override is not None
            else (
                2.0
                * self.radius
                * source_aligned_tail_multiplier()
            )
        )
        self.structural_densities = np.column_stack(
            (
                np.ones_like(self.t),
                np.cosh(0.5 * self.t),
            )
        )
        self.structural_representers = clamped_representer(
            self.structural_densities,
            self.t,
            self.tail_scale,
        )
        self.structural_gram = inner_products(
            self.structural_densities,
            self.structural_representers,
            self.weights,
        )
        self.structural_inverse = np.linalg.inv(
            0.5
            * (
                self.structural_gram
                + self.structural_gram.T
            )
        )

    def projected_fixed_gram(
        self,
        densities: np.ndarray,
        representers: np.ndarray,
    ) -> np.ndarray:
        full = inner_products(
            densities,
            representers,
            self.weights,
        )
        structural_cross = inner_products(
            self.structural_densities,
            representers,
            self.weights,
        )
        return (
            full
            - structural_cross.T
            @ self.structural_inverse
            @ structural_cross
        )

    def scan(
        self,
        axis_grid: np.ndarray,
        core_point: complex,
        axis_coefficient: float,
        batch_size: int = 96,
    ) -> dict[str, np.ndarray | float]:
        axis_grid = np.asarray(axis_grid, dtype=float)
        core_real, core_imag = even_evaluation_densities(
            self.t,
            core_point,
        )
        fixed_densities = np.column_stack(
            (core_real, core_imag)
        )
        fixed_representers = clamped_representer(
            fixed_densities,
            self.t,
            self.tail_scale,
        )
        fixed_gram = self.projected_fixed_gram(
            fixed_densities,
            fixed_representers,
        )
        fixed_structural_cross = inner_products(
            self.structural_densities,
            fixed_representers,
            self.weights,
        )
        thresholds = np.empty(len(axis_grid))
        p_norms = np.empty(len(axis_grid))
        pu_values = np.empty(len(axis_grid))
        pv_values = np.empty(len(axis_grid))

        for start in range(0, len(axis_grid), batch_size):
            stop = min(start + batch_size, len(axis_grid))
            densities = np.cos(
                np.outer(self.t, axis_grid[start:stop])
            )
            representers = clamped_representer(
                densities,
                self.t,
                self.tail_scale,
            )
            full_norm = np.sum(
                self.weights[:, None]
                * densities
                * representers,
                axis=0,
            )
            structural_cross = inner_products(
                self.structural_densities,
                representers,
                self.weights,
            )
            projected_norm = full_norm - np.einsum(
                "ik,ij,jk->k",
                structural_cross,
                self.structural_inverse,
                structural_cross,
            )
            full_fixed_cross = densities.T @ (
                self.weights[:, None] * fixed_representers
            )
            projected_fixed_cross = (
                full_fixed_cross
                - structural_cross.T
                @ self.structural_inverse
                @ fixed_structural_cross
            )
            threshold = rank_two_threshold_from_gram(
                p_norm=projected_norm,
                u_norm=fixed_gram[0, 0],
                v_norm=fixed_gram[1, 1],
                uv_inner=fixed_gram[0, 1],
                pu_inner=projected_fixed_cross[:, 0],
                pv_inner=projected_fixed_cross[:, 1],
                axis_coefficient=axis_coefficient,
            )
            thresholds[start:stop] = threshold
            p_norms[start:stop] = projected_norm
            pu_values[start:stop] = projected_fixed_cross[:, 0]
            pv_values[start:stop] = projected_fixed_cross[:, 1]

        return {
            "axis_grid": axis_grid,
            "thresholds": thresholds,
            "p_norms": p_norms,
            "pu_inner": pu_values,
            "pv_inner": pv_values,
            "u_norm": float(fixed_gram[0, 0]),
            "v_norm": float(fixed_gram[1, 1]),
            "uv_inner": float(fixed_gram[0, 1]),
            "time_step": self.actual_step,
            "structural_gram_condition": float(
                np.linalg.cond(self.structural_gram)
            ),
        }


def continuous_atomic_threshold(
    radius: float,
    time_step: float,
    count_coefficients: np.ndarray,
    axis_supports: list[list[dict[str, float]]],
    core_support: list[dict[str, float]],
    safe_alpha: float | None = None,
    gram_rcond: float = 1e-11,
    tail_scale_override: float | None = None,
) -> dict[str, object]:
    """Evaluate an atomic dual directly in the clamped Green RKHS.

    This bypasses a chosen Galerkin dictionary.  It remains a floating
    quadrature object until the elementary kernel integrals are
    interval-enclosed.
    """
    scanner = GreenRankTwoScanner(
        radius,
        time_step,
        tail_scale_override=tail_scale_override,
    )
    densities = []
    axis_slices = []
    for support in axis_supports:
        start = len(densities)
        densities.extend(
            np.cos(float(row["x"]) * scanner.t)
            for row in support
        )
        axis_slices.append(slice(start, len(densities)))
    core_u_indices = []
    core_v_indices = []
    for row in core_support:
        real, imag = even_evaluation_densities(
            scanner.t,
            complex(float(row["x"]), float(row["y"])),
        )
        core_u_indices.append(len(densities))
        densities.append(real)
        core_v_indices.append(len(densities))
        densities.append(imag)
    density_matrix = np.column_stack(densities)
    representers = clamped_representer(
        density_matrix,
        scanner.t,
        scanner.tail_scale,
    )
    gram = scanner.projected_fixed_gram(
        density_matrix,
        representers,
    )
    gram = 0.5 * (gram + gram.T)
    values, vectors = np.linalg.eigh(gram)
    cutoff = gram_rcond * float(values[-1])
    keep = values > cutoff
    coordinates = (
        np.sqrt(values[keep])[:, None]
        * vectors[:, keep].T
    )
    dimension = int(np.sum(keep))
    base = np.eye(dimension)
    for band_index, (support, support_slice) in enumerate(
        zip(axis_supports, axis_slices)
    ):
        raw_weights = np.asarray(
            [row["weight"] for row in support],
            dtype=float,
        )
        weights = raw_weights / np.sum(raw_weights)
        group = coordinates[:, support_slice]
        base += (
            float(count_coefficients[band_index])
            * (group * weights[None, :])
            @ group.T
        )
    raw_core_weights = np.asarray(
        [row["weight"] for row in core_support],
        dtype=float,
    )
    core_weights = raw_core_weights / np.sum(raw_core_weights)
    core = np.zeros_like(base)
    for weight, u_index, v_index in zip(
        core_weights,
        core_u_indices,
        core_v_indices,
    ):
        u = coordinates[:, u_index]
        v = coordinates[:, v_index]
        core += 2.0 * float(weight) * (
            np.outer(u, u) - np.outer(v, v)
        )
    minimum_generalized = float(
        eigh(
            core,
            base,
            eigvals_only=True,
            subset_by_index=[0, 0],
            check_finite=False,
        )[0]
    )
    threshold = (
        -1.0 / minimum_generalized
        if minimum_generalized < -1e-14
        else float("inf")
    )
    output: dict[str, object] = {
        "time_step": scanner.actual_step,
        "time_grid_count": len(scanner.t),
        "evaluation_function_count": len(densities),
        "effective_kernel_rank": dimension,
        "projected_gram_minimum_retained_eigenvalue": float(
            values[keep][0]
        ),
        "projected_gram_maximum_eigenvalue": float(values[-1]),
        "minimum_generalized_eigenvalue": minimum_generalized,
        "raw_threshold_for_fixed_measures": float(threshold),
        "structural_gram_condition": float(
            np.linalg.cond(scanner.structural_gram)
        ),
    }
    if safe_alpha is not None:
        witness = base + float(safe_alpha) * core
        positive_indices: list[int] = []
        positive_scales: list[float] = []
        for band_index, (support, support_slice) in enumerate(
            zip(axis_supports, axis_slices)
        ):
            raw_weights = np.asarray(
                [row["weight"] for row in support],
                dtype=float,
            )
            weights = raw_weights / np.sum(raw_weights)
            for local_index, weight in enumerate(weights):
                positive_indices.append(
                    int(support_slice.start + local_index)
                )
                positive_scales.append(
                    float(
                        np.sqrt(
                            count_coefficients[band_index]
                            * weight
                        )
                    )
                )
        negative_indices: list[int] = []
        negative_scales: list[float] = []
        for weight, u_index, v_index in zip(
            core_weights,
            core_u_indices,
            core_v_indices,
        ):
            scale = float(
                np.sqrt(2.0 * float(safe_alpha) * weight)
            )
            positive_indices.append(u_index)
            positive_scales.append(scale)
            negative_indices.append(v_index)
            negative_scales.append(scale)
        positive_scales_array = np.asarray(positive_scales)
        negative_scales_array = np.asarray(negative_scales)
        positive_gram = gram[
            np.ix_(positive_indices, positive_indices)
        ] * (
            positive_scales_array[:, None]
            * positive_scales_array[None, :]
        )
        negative_gram = gram[
            np.ix_(negative_indices, negative_indices)
        ] * (
            negative_scales_array[:, None]
            * negative_scales_array[None, :]
        )
        cross_gram = gram[
            np.ix_(positive_indices, negative_indices)
        ] * (
            positive_scales_array[:, None]
            * negative_scales_array[None, :]
        )
        positive_system = (
            np.eye(len(positive_indices)) + positive_gram
        )
        schur = np.eye(len(negative_indices)) - (
            negative_gram
            - cross_gram.T
            @ np.linalg.solve(positive_system, cross_gram)
        )
        schur = 0.5 * (schur + schur.T)
        output.update(
            {
                "tested_safe_alpha": float(safe_alpha),
                "tested_safe_minimum_eigenvalue": float(
                    np.linalg.eigvalsh(
                        0.5 * (witness + witness.T)
                    )[0]
                ),
                "tested_safe_psd": bool(
                    np.linalg.eigvalsh(
                        0.5 * (witness + witness.T)
                    )[0]
                    >= -1e-9
                ),
                "positive_rank_for_schur_test": len(
                    positive_indices
                ),
                "negative_rank_for_schur_test": len(
                    negative_indices
                ),
                "positive_system_condition": float(
                    np.linalg.cond(positive_system)
                ),
                "schur_certificate_minimum_eigenvalue": float(
                    np.linalg.eigvalsh(schur)[0]
                ),
                "schur_certificate_matrix": schur.tolist(),
            }
        )
    return output
