from __future__ import annotations

import functools
import math
from dataclasses import dataclass

import numpy as np
from numpy.polynomial import Chebyshev
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
from scipy.linalg import eigh, null_space

from .axis import (
    AxisBand,
    default_axis_bands,
    downward_count_majorant,
    s_bound,
)


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
    """Return even polynomials with value and slope zero at both ends."""
    normalized_t = np.asarray(normalized_t, dtype=float)
    window = Chebyshev([3.0 / 8.0, 0.0, -0.5, 0.0, 1.0 / 8.0])
    values = []
    seconds = []
    for index in range(raw_dimension):
        polynomial = window * Chebyshev.basis(2 * index)
        values.append(polynomial(normalized_t))
        seconds.append(
            polynomial.deriv(2)(normalized_t) / (radius * radius)
        )
    return (
        np.stack(values, axis=1),
        np.stack(seconds, axis=1),
    )


def rank_two_threshold_from_gram(
    p_norm: np.ndarray | float,
    u_norm: np.ndarray | float,
    v_norm: np.ndarray | float,
    uv_inner: np.ndarray | float,
    pu_inner: np.ndarray | float,
    pv_inner: np.ndarray | float,
    axis_coefficient: float,
) -> np.ndarray:
    """Closed one-axis/one-core extremal from six kernel inner products."""
    p_norm = np.asarray(p_norm, dtype=float)
    u_norm = np.asarray(u_norm, dtype=float)
    v_norm = np.asarray(v_norm, dtype=float)
    uv_inner = np.asarray(uv_inner, dtype=float)
    pu_inner = np.asarray(pu_inner, dtype=float)
    pv_inner = np.asarray(pv_inner, dtype=float)
    denominator = 1.0 + axis_coefficient * p_norm
    a = u_norm - axis_coefficient * pu_inner * pu_inner / denominator
    b = v_norm - axis_coefficient * pv_inner * pv_inner / denominator
    c = uv_inner - axis_coefficient * pu_inner * pv_inner / denominator
    discriminant = np.maximum(
        0.0,
        (a + b) ** 2 - 4.0 * c * c,
    )
    negative_magnitude = (
        np.sqrt(discriminant) - (a - b)
    )
    return np.where(
        negative_magnitude > 1e-14,
        1.0 / negative_magnitude,
        np.inf,
    )


@dataclass
class PWGalerkinContext:
    radius: float
    raw_dimension: int
    quadrature_order: int = 2048
    whitening_rcond: float = 1e-12

    def __post_init__(self) -> None:
        if self.raw_dimension < 5:
            raise ValueError("raw_dimension must be at least 5")
        nodes, base_weights = gauss_rule(self.quadrature_order)
        self.t = self.radius * nodes
        self.weights = self.radius * base_weights
        basis, second = clamped_even_chebyshev(
            nodes,
            self.raw_dimension,
            self.radius,
        )
        tail_scale = (
            2.0
            * self.radius
            * source_aligned_tail_multiplier()
        )
        tail_gram = (
            tail_scale
            * second.T
            @ (self.weights[:, None] * second)
        )
        structural_rows = np.vstack(
            (
                basis.T @ self.weights,
                basis.T @ (
                    self.weights * np.cosh(0.5 * self.t)
                ),
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
        self.basis = basis
        self.second = second
        self.weighted_coordinate_basis = (
            self.weights[:, None]
            * basis
            @ self.coordinate_map
        )
        self.tail_matrix = np.eye(self.coordinate_map.shape[1])
        self.tail_scale = tail_scale
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
        self.bands: list[AxisBand] = default_axis_bands()
        self.count_coefficients = np.asarray(
            [
                downward_count_majorant(band)
                for band in self.bands
            ]
        )

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
                    1j * np.outer(points[start:stop], self.t)
                )
                @ self.weighted_coordinate_basis
            )
        return output

    def axis_transforms(self, points: np.ndarray) -> np.ndarray:
        values = self.transform(np.asarray(points, dtype=float))
        return values.real

    def core_matrices(self, points: np.ndarray) -> np.ndarray:
        transform = self.transform(points)
        return np.asarray(
            [
                2.0 * np.real(np.outer(row, row))
                for row in transform
            ]
        )

    def kernel_gram(
        self,
        axis_x: float,
        core_z: complex,
    ) -> dict[str, float]:
        p = self.transform(np.asarray([axis_x]))[0].real
        core = self.transform(np.asarray([core_z]))[0]
        u = core.real
        v = core.imag
        return {
            "p_norm": float(p @ p),
            "u_norm": float(u @ u),
            "v_norm": float(v @ v),
            "uv_inner": float(u @ v),
            "pu_inner": float(p @ u),
            "pv_inner": float(p @ v),
        }

    def point_extremal(
        self,
        axis_x: float,
        core_z: complex,
        axis_coefficient: float,
    ) -> float:
        gram = self.kernel_gram(axis_x, core_z)
        return float(
            rank_two_threshold_from_gram(
                axis_coefficient=axis_coefficient,
                **gram,
            )
        )
