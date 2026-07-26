from __future__ import annotations

import math
from dataclasses import dataclass
from fractions import Fraction

import numpy as np
from scipy.integrate import quad

from .axis import AxisBand, default_axis_bands
from .cover import Patch
from .model import (
    constrained_whitener,
    fourier_matrix,
    fourier_vector,
    paired_bump_basis,
    paired_bump_second_derivative,
    trapezoid_weights,
)


def s_bound(t: float) -> float:
    return 0.111 * math.log(t) + 0.275 * math.log(math.log(t)) + 2.450


def tail_multiplier(start: float = 145.0, split: int = 500) -> float:
    def density(t: float) -> float:
        return 1.0 + math.log(t) / (2.0 * math.pi) + 2.0 * s_bound(
            t + 1.0
        )

    first_shell = int(math.ceil(start))
    finite = sum(
        density(n + 1.0) / (n**4)
        for n in range(first_shell, split)
    )
    continuation = quad(
        lambda value: density(value + 1.0) / value**4,
        float(split),
        np.inf,
        epsabs=1e-14,
        epsrel=1e-11,
    )[0]
    return float(finite + 1.05 * continuation)


def rational_patch_center(patch: Patch) -> tuple[Fraction, Fraction]:
    x = (
        Fraction(str(patch.x_min)) + Fraction(str(patch.x_max))
    ) / 2
    y = (
        Fraction(str(patch.y_min)) + Fraction(str(patch.y_max))
    ) / 2
    return x, y


def core_matrix_from_transform(transform: np.ndarray) -> np.ndarray:
    transform = np.asarray(transform, dtype=complex)
    return 2.0 * np.real(np.outer(transform, transform))


def axis_matrix_from_transform(transform: np.ndarray) -> np.ndarray:
    transform = np.asarray(transform, dtype=float)
    return np.outer(transform, transform)


@dataclass
class TailDualContext:
    radius: float = 3.0
    count: int = 24
    step: float = 0.01
    width_factor: float = 1.2

    def __post_init__(self) -> None:
        t = np.arange(
            -self.radius,
            self.radius + self.step / 2.0,
            self.step,
        )
        basis, centers, width = paired_bump_basis(
            t,
            radius=self.radius,
            count=self.count,
            width_factor=self.width_factor,
        )
        second = paired_bump_second_derivative(
            t,
            radius=self.radius,
            count=self.count,
            width_factor=self.width_factor,
        )
        weights = trapezoid_weights(len(t), self.step)
        c0 = basis.T @ (weights[:, None] * basis)
        g0 = fourier_vector(0.0, t, basis, weights).real
        endpoint = fourier_vector(0.5j, t, basis, weights).real
        self.model = {
            "radius": self.radius,
            "count": self.count,
            "step": self.step,
            "t": t,
            "basis": basis,
            "basis_second_derivative": second,
            "weights": weights,
            "c0": c0,
            "g0_constraint": g0,
            "endpoint_constraint": endpoint,
            "centers": centers,
            "width": width,
        }
        self.coordinate_map = constrained_whitener(self.model)
        d2_full = second.T @ (weights[:, None] * second)
        d2 = self.coordinate_map.T @ d2_full @ self.coordinate_map
        self.tail_matrix = (
            tail_multiplier()
            * 2.0
            * self.radius
            * 0.5
            * (d2 + d2.T)
        )
        self.bands: list[AxisBand] = default_axis_bands()

    @property
    def dimension(self) -> int:
        return int(self.coordinate_map.shape[1])

    def transform(self, points: np.ndarray) -> np.ndarray:
        return fourier_matrix(points, self.model) @ self.coordinate_map

    def core_transform(self, point: complex) -> np.ndarray:
        return self.transform(np.asarray([point], dtype=complex))[0]

    def core_matrix(self, point: complex) -> np.ndarray:
        return core_matrix_from_transform(self.core_transform(point))

    def axis_transforms(self, grid: np.ndarray) -> np.ndarray:
        return self.transform(np.asarray(grid, dtype=complex)).real

    def uniform_axis_average(
        self,
        band_index: int,
        grid: np.ndarray,
        count_coefficient: float | None = None,
    ) -> np.ndarray:
        transforms = self.axis_transforms(grid)
        coefficient = (
            self.bands[band_index].count_majorant
            if count_coefficient is None
            else float(count_coefficient)
        )
        return (
            coefficient
            * transforms.T
            @ transforms
            / len(transforms)
        )
