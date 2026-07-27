from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.linalg import eigh


def trapezoid_weights(size: int, step: float) -> np.ndarray:
    weights = np.full(size, step, dtype=float)
    weights[0] = weights[-1] = step / 2.0
    return weights


def clamped_representer(
    density: np.ndarray,
    t: np.ndarray,
    tail_scale: float,
) -> np.ndarray:
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
    left = float(t[0])
    right = float(t[-1])
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
    return densities.T @ (weights[:, None] * representers)


@dataclass
class FloatingClampedContext:
    radius: float
    time_step: float
    tail_scale: float
    count_coefficients: np.ndarray
    band_indices: np.ndarray
    atom_probabilities: np.ndarray
    core_support: list[dict[str, float]]

    def __post_init__(self) -> None:
        count = int(round(2.0 * self.radius / self.time_step)) + 1
        self.t = np.linspace(-self.radius, self.radius, count)
        self.actual_step = float(self.t[1] - self.t[0])
        self.weights = trapezoid_weights(len(self.t), self.actual_step)
        structural = np.column_stack(
            (np.ones_like(self.t), np.cosh(0.5 * self.t))
        )
        structural_rep = clamped_representer(
            structural,
            self.t,
            self.tail_scale,
        )
        structural_gram = inner_products(
            structural,
            structural_rep,
            self.weights,
        )
        self.structural = structural
        self.structural_inverse = np.linalg.inv(
            0.5 * (structural_gram + structural_gram.T)
        )

    def threshold(self, axis_locations: np.ndarray) -> float:
        densities = [
            np.cos(float(location) * self.t)
            for location in axis_locations
        ]
        core_u_indices: list[int] = []
        core_v_indices: list[int] = []
        for row in self.core_support:
            x = float(row["x"])
            y = float(row["y"])
            core_u_indices.append(len(densities))
            densities.append(
                np.cos(x * self.t) * np.cosh(y * self.t)
            )
            core_v_indices.append(len(densities))
            densities.append(
                -np.sin(x * self.t) * np.sinh(y * self.t)
            )
        density_matrix = np.column_stack(densities)
        representers = clamped_representer(
            density_matrix,
            self.t,
            self.tail_scale,
        )
        full = inner_products(
            density_matrix,
            representers,
            self.weights,
        )
        structural_cross = inner_products(
            self.structural,
            representers,
            self.weights,
        )
        gram = (
            full
            - structural_cross.T
            @ self.structural_inverse
            @ structural_cross
        )
        gram = 0.5 * (gram + gram.T)
        values, vectors = np.linalg.eigh(gram)
        keep = values > 1e-11 * float(values[-1])
        coordinates = (
            np.sqrt(values[keep])[:, None]
            * vectors[:, keep].T
        )
        dimension = int(np.sum(keep))
        base = np.eye(dimension)
        for index, (band, probability) in enumerate(
            zip(self.band_indices, self.atom_probabilities)
        ):
            vector = coordinates[:, index]
            weight = (
                float(self.count_coefficients[int(band)])
                * float(probability)
            )
            base += weight * np.outer(vector, vector)
        raw_core_weights = np.asarray(
            [row["weight"] for row in self.core_support],
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
        minimum = float(
            eigh(
                core,
                base,
                eigvals_only=True,
                subset_by_index=[0, 0],
                check_finite=False,
            )[0]
        )
        if minimum >= -1e-14:
            return float("inf")
        return -1.0 / minimum


def adversarial_corner(
    context: FloatingClampedContext,
    centers: np.ndarray,
    gradient: np.ndarray,
    half_width: float,
    sweeps: int = 4,
) -> tuple[float, np.ndarray, int]:
    signs = -np.sign(gradient)
    signs[signs == 0] = -1.0
    points = centers + half_width * signs
    value = context.threshold(points)
    flips = 0
    for _ in range(sweeps):
        improved = False
        for index in range(len(points)):
            candidate = points.copy()
            candidate[index] = (
                centers[index] - half_width
                if points[index] > centers[index]
                else centers[index] + half_width
            )
            candidate_value = context.threshold(candidate)
            if candidate_value < value - 1e-11:
                points = candidate
                value = candidate_value
                flips += 1
                improved = True
        if not improved:
            break
    return value, points, flips


def floating_location_study(
    count_coefficients: np.ndarray,
    centers: np.ndarray,
    band_indices: np.ndarray,
    atom_probabilities: np.ndarray,
    core_support: list[dict[str, float]],
    tail_scale: float,
) -> dict[str, Any]:
    base_context = FloatingClampedContext(
        radius=16.0,
        time_step=0.02,
        tail_scale=tail_scale,
        count_coefficients=count_coefficients,
        band_indices=band_indices,
        atom_probabilities=atom_probabilities,
        core_support=core_support,
    )
    base_threshold = base_context.threshold(centers)
    finite_difference_step = 1e-4
    gradient = np.empty(len(centers))
    for index in range(len(centers)):
        plus = centers.copy()
        minus = centers.copy()
        plus[index] += finite_difference_step
        minus[index] -= finite_difference_step
        gradient[index] = (
            base_context.threshold(plus)
            - base_context.threshold(minus)
        ) / (2.0 * finite_difference_step)

    half_widths = (0.012, 0.014, 0.015, 0.016, 0.017, 0.018, 0.020)
    rows: list[dict[str, Any]] = []
    selected_points: dict[float, np.ndarray] = {}
    for half_width in half_widths:
        threshold, points, flips = adversarial_corner(
            base_context,
            centers,
            gradient,
            half_width,
        )
        selected_points[half_width] = points
        rows.append(
            {
                "cell_half_width": half_width,
                "time_step": base_context.actual_step,
                "adversarial_corner_threshold": threshold,
                "coordinate_flips_after_gradient_corner": flips,
                "threshold_above_one": bool(threshold > 1.0),
                "corner_signs": [
                    int(np.sign(point - center))
                    for point, center in zip(points, centers)
                ],
            }
        )

    refinements = []
    for half_width in (0.015, 0.016, 0.017):
        points = selected_points[half_width]
        step_rows = []
        for time_step in (0.02, 0.01, 0.005):
            context = FloatingClampedContext(
                radius=16.0,
                time_step=time_step,
                tail_scale=tail_scale,
                count_coefficients=count_coefficients,
                band_indices=band_indices,
                atom_probabilities=atom_probabilities,
                core_support=core_support,
            )
            step_rows.append(
                {
                    "time_step": context.actual_step,
                    "threshold": context.threshold(points),
                }
            )
        refinements.append(
            {
                "cell_half_width": half_width,
                "fixed_corner_time_refinement": step_rows,
            }
        )

    return {
        "schema": "RH.Occupancy.FloatingClampedLocationStudy.v0.9",
        "configuration": {
            "axis_atom_count": len(centers),
            "base_time_step": base_context.actual_step,
            "finite_difference_step": finite_difference_step,
            "corner_search": (
                "central gradient sign followed by up to four "
                "deterministic coordinate-flip sweeps"
            ),
        },
        "base_fixed_location_threshold": base_threshold,
        "gradient_summary": {
            "minimum": float(np.min(gradient)),
            "maximum": float(np.max(gradient)),
            "l2_norm": float(np.linalg.norm(gradient)),
            "l1_norm": float(np.sum(np.abs(gradient))),
        },
        "adversarial_corner_rows": rows,
        "time_refinements": refinements,
        "observed_transition_bracket": {
            "last_tested_width_above_one": 0.016,
            "first_tested_width_below_one": 0.017,
        },
        "classification": {
            "floating_diagnostic": True,
            "universal_location_quantifier_certified": False,
            "operator_counterexample_certified": False,
            "actual_zero_occupancy_certificate": False,
            "global_rh_certificate": False,
        },
    }

