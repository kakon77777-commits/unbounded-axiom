from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
from scipy.integrate import quad

from .axis import (
    AxisBand,
    default_axis_bands,
    downward_count_majorant,
    s_bound,
)
from .model import (
    constrained_whitener,
    fourier_matrix,
    fourier_vector,
    paired_bump_basis,
    paired_bump_second_derivative,
    trapezoid_weights,
)


def source_aligned_tail_multiplier(
    start: float = 145.0,
    split: int = 500,
) -> float:
    """Floating tail prototype using the published Trudgian S(t) profile."""

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


def core_matrix_from_transform(transform: np.ndarray) -> np.ndarray:
    transform = np.asarray(transform, dtype=complex)
    return 2.0 * np.real(np.outer(transform, transform))


@dataclass
class FrontierContext:
    radius: float
    density: float = 10.0
    width_factor: float = 1.5
    step: float = 0.01

    def __post_init__(self) -> None:
        self.count = int(round(self.density * self.radius))
        if self.count < 3:
            raise ValueError("basis count is too small")
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
        self.tail_multiplier = source_aligned_tail_multiplier()
        self.tail_matrix = (
            self.tail_multiplier
            * 2.0
            * self.radius
            * 0.5
            * (d2 + d2.T)
        )
        self.bands: list[AxisBand] = default_axis_bands()
        self.count_coefficients = np.asarray(
            [downward_count_majorant(band) for band in self.bands]
        )

    @property
    def dimension(self) -> int:
        return int(self.coordinate_map.shape[1])

    def transform(self, points: np.ndarray) -> np.ndarray:
        return fourier_matrix(points, self.model) @ self.coordinate_map

    def core_transforms(self, points: np.ndarray) -> np.ndarray:
        return self.transform(np.asarray(points, dtype=complex))

    def core_matrices(self, points: np.ndarray) -> np.ndarray:
        transforms = self.core_transforms(points)
        return np.asarray(
            [core_matrix_from_transform(row) for row in transforms]
        )

    def axis_transforms(self, grid: np.ndarray) -> np.ndarray:
        return self.transform(np.asarray(grid, dtype=complex)).real

    def axis_outer_matrices(self, grid: np.ndarray) -> np.ndarray:
        transforms = self.axis_transforms(grid)
        return np.einsum("ki,kj->kij", transforms, transforms)

    def uniform_axis_matrix(
        self,
        band_index: int,
        step: float,
    ) -> tuple[np.ndarray, np.ndarray]:
        band = self.bands[band_index]
        count = int(round((band.stop - band.start) / step)) + 1
        grid = np.linspace(band.start, band.stop, count)
        matrices = self.axis_outer_matrices(grid)
        return (
            self.count_coefficients[band_index]
            * np.mean(matrices, axis=0),
            grid,
        )

    def base_matrix(
        self,
        band_indices: tuple[int, ...],
        axis_step: float = 0.25,
        tail_fraction: float = 1.0,
    ) -> tuple[np.ndarray, dict[str, object]]:
        matrix = tail_fraction * self.tail_matrix
        rows = []
        for index in band_indices:
            piece, grid = self.uniform_axis_matrix(index, axis_step)
            matrix = matrix + piece
            rows.append(
                {
                    "band_id": self.bands[index].band_id,
                    "grid_count": len(grid),
                    "step": axis_step,
                    "count_downward": self.count_coefficients[index],
                }
            )
        return 0.5 * (matrix + matrix.T), {
            "tail_fraction": tail_fraction,
            "bands": rows,
        }
