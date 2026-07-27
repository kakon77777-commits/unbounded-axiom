from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.linalg import eigh

from .galerkin import source_aligned_tail_multiplier


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


def clamped_representer(
    density: np.ndarray,
    t: np.ndarray,
    tail_scale: float,
) -> np.ndarray:
    """Solve tail_scale times r'''' = density with clamped endpoints."""

    t = np.asarray(t, dtype=float)
    density = np.asarray(density, dtype=float)
    if density.ndim == 1:
        density = density[:, None]
        squeeze = True
    else:
        squeeze = False
    moments = [
        cumulative_trapezoid(
            (t**power)[:, None] * density,
            t,
            axis=0,
            initial=0.0,
        )
        for power in range(4)
    ]
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
class GreenContext:
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

    def projected_gram(
        self,
        densities: np.ndarray,
        representers: np.ndarray,
    ) -> np.ndarray:
        full = inner_products(
            densities,
            representers,
            self.weights,
        )
        cross = inner_products(
            self.structural_densities,
            representers,
            self.weights,
        )
        output = (
            full
            - cross.T @ self.structural_inverse @ cross
        )
        return 0.5 * (output + output.T)


def continuous_atomic_threshold(
    radius: float,
    time_step: float,
    count_coefficients: np.ndarray,
    axis_supports: list[list[dict[str, float]]],
    core_support: list[dict[str, float]],
    tail_scale_override: float | None = None,
    gram_rcond: float = 1e-11,
) -> dict[str, Any]:
    context = GreenContext(
        radius,
        time_step,
        tail_scale_override=tail_scale_override,
    )
    densities = []
    axis_slices = []
    for support in axis_supports:
        start = len(densities)
        densities.extend(
            np.cos(float(row["x"]) * context.t)
            for row in support
        )
        axis_slices.append(slice(start, len(densities)))
    core_u_indices = []
    core_v_indices = []
    for row in core_support:
        real, imag = even_evaluation_densities(
            context.t,
            complex(float(row["x"]), float(row["y"])),
        )
        core_u_indices.append(len(densities))
        densities.append(real)
        core_v_indices.append(len(densities))
        densities.append(imag)
    density_matrix = np.column_stack(densities)
    representers = clamped_representer(
        density_matrix,
        context.t,
        context.tail_scale,
    )
    gram = context.projected_gram(
        density_matrix,
        representers,
    )
    values, vectors = np.linalg.eigh(gram)
    cutoff = gram_rcond * float(values[-1])
    keep = values > cutoff
    coordinates = (
        np.sqrt(values[keep])[:, None]
        * vectors[:, keep].T
    )
    dimension = int(np.sum(keep))
    base = np.eye(dimension)
    for coefficient, support, support_slice in zip(
        count_coefficients,
        axis_supports,
        axis_slices,
    ):
        if not support or float(coefficient) == 0.0:
            continue
        raw_weights = np.asarray(
            [row["weight"] for row in support],
            dtype=float,
        )
        weights = raw_weights / np.sum(raw_weights)
        group = coordinates[:, support_slice]
        base += (
            float(coefficient)
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
    return {
        "time_step": context.actual_step,
        "time_grid_count": len(context.t),
        "evaluation_function_count": len(densities),
        "effective_kernel_rank": dimension,
        "projected_gram_minimum_retained_eigenvalue": float(
            values[keep][0]
        ),
        "projected_gram_maximum_eigenvalue": float(values[-1]),
        "minimum_generalized_eigenvalue": minimum_generalized,
        "raw_threshold_for_fixed_measures": float(threshold),
        "structural_gram_condition": float(
            np.linalg.cond(context.structural_gram)
        ),
        "interval_certified": False,
        "global_rh_certificate": False,
    }
