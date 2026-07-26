from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
from scipy.special import loggamma

from .model import fourier_matrix


@dataclass(frozen=True)
class AxisBand:
    band_id: str
    start: float
    stop: float
    count_majorant: float


def s_bound(t: float) -> float:
    """Inherited explicit profile used as a floating zero-count majorant."""
    return 0.111 * math.log(t) + 0.275 * math.log(math.log(t)) + 2.450


def riemann_siegel_theta(t: float) -> float:
    z = 0.25 + 0.5j * t
    return float(loggamma(z).imag - t * math.log(math.pi) / 2.0)


def interval_zero_count_majorant(start: float, stop: float) -> float:
    delta_theta = (
        riemann_siegel_theta(stop) - riemann_siegel_theta(start)
    ) / math.pi
    return max(0.0, delta_theta + s_bound(start) + s_bound(stop))


def default_axis_bands() -> list[AxisBand]:
    endpoints = (14.0, 18.0, 23.0, 35.0, 70.0, 145.0)
    return [
        AxisBand(
            band_id=f"A{index}",
            start=start,
            stop=stop,
            count_majorant=interval_zero_count_majorant(start, stop),
        )
        for index, (start, stop) in enumerate(
            zip(endpoints[:-1], endpoints[1:])
        )
    ]


def band_grids(
    bands: list[AxisBand],
    step: float,
) -> list[np.ndarray]:
    return [
        np.linspace(
            band.start,
            band.stop,
            int(round((band.stop - band.start) / step)) + 1,
        )
        for band in bands
    ]


def axis_gram_matrices(
    grids: list[np.ndarray],
    model: dict[str, object],
    basis_coefficients: np.ndarray,
) -> list[np.ndarray]:
    output = []
    for grid in grids:
        transform = (
            fourier_matrix(grid.astype(complex), model)
            @ basis_coefficients
        ).real
        output.append(
            np.asarray([np.outer(row, row) for row in transform])
        )
    return output
