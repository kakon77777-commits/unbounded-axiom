from __future__ import annotations

import math
from dataclasses import asdict, dataclass

from scipy.special import loggamma


@dataclass(frozen=True)
class AxisBand:
    band_id: str
    start: float
    stop: float


INHERITED_S_PROFILE = {
    "log_coefficient": 0.112,
    "loglog_coefficient": 0.278,
    "constant": 2.510,
    "valid_from": math.e,
    "source_doi": "10.1016/j.jnt.2013.07.017",
    "source_arxiv": "1208.5846",
    "status": (
        "conservative floating profile inherited from v0.4-v0.7; "
        "not interval-enclosed in this node"
    ),
}


def default_axis_bands() -> list[AxisBand]:
    endpoints = (14.0, 18.0, 23.0, 35.0, 70.0, 145.0)
    return [
        AxisBand(f"A{index}", start, stop)
        for index, (start, stop) in enumerate(
            zip(endpoints[:-1], endpoints[1:])
        )
    ]


def s_bound(t: float) -> float:
    return (
        INHERITED_S_PROFILE["log_coefficient"] * math.log(t)
        + INHERITED_S_PROFILE["loglog_coefficient"]
        * math.log(math.log(t))
        + INHERITED_S_PROFILE["constant"]
    )


def riemann_siegel_theta(t: float) -> float:
    z = 0.25 + 0.5j * t
    return float(loggamma(z).imag - 0.5 * t * math.log(math.pi))


def count_profile_rows() -> list[dict[str, object]]:
    rows = []
    for band in default_axis_bands():
        theta_increment = (
            riemann_siegel_theta(band.stop)
            - riemann_siegel_theta(band.start)
        ) / math.pi
        endpoint_budget = s_bound(band.start) + s_bound(band.stop)
        lower = max(0.0, theta_increment - endpoint_budget)
        upper = max(0.0, theta_increment + endpoint_budget)
        rows.append(
            {
                **asdict(band),
                "theta_increment": theta_increment,
                "absolute_S_endpoint_budget": endpoint_budget,
                "floating_count_lower": lower,
                "floating_count_upper": upper,
                "lower_role": "count_lower_candidate",
                "upper_role": "count_upper_candidate",
                "endpoint_theorem_certified": False,
                "directed_transcendental_enclosure": False,
            }
        )
    return rows


def lower_profile_downward(decimals: int = 12) -> list[float]:
    scale = 10**decimals
    return [
        math.floor(float(row["floating_count_lower"]) * scale) / scale
        for row in count_profile_rows()
    ]


def upper_profile_upward(decimals: int = 12) -> list[float]:
    scale = 10**decimals
    return [
        math.ceil(float(row["floating_count_upper"]) * scale) / scale
        for row in count_profile_rows()
    ]
