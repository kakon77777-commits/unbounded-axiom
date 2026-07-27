from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
from scipy.special import loggamma


PUBLISHED_S_BOUND = {
    "log_coefficient": 0.112,
    "loglog_coefficient": 0.278,
    "constant": 2.510,
    "valid_from": math.e,
    "doi": "10.1016/j.jnt.2013.07.017",
}


@dataclass(frozen=True)
class AxisBand:
    band_id: str
    start: float
    stop: float
    count_majorant: float


def s_bound(t: float) -> float:
    return (
        PUBLISHED_S_BOUND["log_coefficient"] * math.log(t)
        + PUBLISHED_S_BOUND["loglog_coefficient"]
        * math.log(math.log(t))
        + PUBLISHED_S_BOUND["constant"]
    )


def riemann_siegel_theta(t: float) -> float:
    z = 0.25 + 0.5j * t
    return float(
        loggamma(z).imag - t * math.log(math.pi) / 2.0
    )


def interval_zero_count_majorant(
    start: float,
    stop: float,
) -> float:
    delta_theta = (
        riemann_siegel_theta(stop) - riemann_siegel_theta(start)
    ) / math.pi
    return max(
        0.0,
        delta_theta + s_bound(start) + s_bound(stop),
    )


def downward_count_majorant(
    band: AxisBand,
    decimals: int = 12,
) -> float:
    scale = 10**decimals
    return math.floor(band.count_majorant * scale) / scale


def default_axis_bands() -> list[AxisBand]:
    endpoints = (14.0, 18.0, 23.0, 35.0, 70.0, 145.0)
    return [
        AxisBand(
            band_id=f"A{index}",
            start=start,
            stop=stop,
            count_majorant=interval_zero_count_majorant(
                start,
                stop,
            ),
        )
        for index, (start, stop) in enumerate(
            zip(endpoints[:-1], endpoints[1:])
        )
    ]


def band_grid(band: AxisBand, step: float) -> np.ndarray:
    count = int(round((band.stop - band.start) / step)) + 1
    return np.linspace(band.start, band.stop, count)
