from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

from scipy.special import loggamma


ROOT = Path(__file__).resolve().parent
ENDPOINTS = (14.0, 18.0, 23.0, 35.0, 70.0, 145.0)


def fraction(row: dict[str, int]) -> Fraction:
    return Fraction(row["numerator"], row["denominator"])


def s_bound(value: float) -> float:
    return (
        0.112 * math.log(value)
        + 0.278 * math.log(math.log(value))
        + 2.510
    )


def theta(value: float) -> float:
    z = 0.25 + 0.5j * value
    return float(
        loggamma(z).imag - value * math.log(math.pi) / 2
    )


def main() -> None:
    witness = json.loads(
        (
            ROOT
            / "data"
            / "rational_atomic_witness_v0.6.json"
        ).read_text(encoding="utf-8")
    )
    stored = [
        float(fraction(row))
        for row in witness["model"]["count_coefficients"]
    ]
    rows = []
    for index, (start, stop, coefficient) in enumerate(
        zip(ENDPOINTS[:-1], ENDPOINTS[1:], stored)
    ):
        theta_increment = (theta(stop) - theta(start)) / math.pi
        argument_budget = s_bound(start) + s_bound(stop)
        lower = max(0.0, theta_increment - argument_budget)
        upper = max(0.0, theta_increment + argument_budget)
        rows.append(
            {
                "band": f"A{index}",
                "interval": [start, stop],
                "theta_increment": theta_increment,
                "absolute_S_endpoint_budget": argument_budget,
                "lower_count_from_absolute_S_only": lower,
                "upper_count_from_absolute_S_only": upper,
                "stored_positive_coefficient": coefficient,
                "stored_matches_downward_rounded_upper": bool(
                    coefficient <= upper
                    and upper - coefficient < 2e-12
                ),
                "stored_is_justified_positive_lower_coefficient": bool(
                    coefficient <= lower
                ),
            }
        )
    all_upper = all(
        row["stored_matches_downward_rounded_upper"]
        for row in rows
    )
    all_lower = all(
        row["stored_is_justified_positive_lower_coefficient"]
        for row in rows
    )
    output = {
        "schema": "RH.CoefficientOrientationAudit.v0.7",
        "source_bound": {
            "statement": (
                "|S(T)| <= 0.112 log(T) + 0.278 log log(T) "
                "+ 2.510 for T >= e"
            ),
            "doi": "10.1016/j.jnt.2013.07.017",
        },
        "zero_count_difference_identity": (
            "N(b)-N(a) = (theta(b)-theta(a))/pi + S(b)-S(a), "
            "away from endpoint zeros under the standard convention"
        ),
        "rows": rows,
        "all_stored_coefficients_match_upper_profile": all_upper,
        "all_stored_coefficients_are_lower_certificates": all_lower,
        "orientation_blocker_confirmed": bool(all_upper and not all_lower),
        "consequence": (
            "The Layer A interval theorem remains valid for its exact "
            "abstract coefficients. A zeta-facing positive-axis transfer "
            "cannot use these stored majorants as lower counts without "
            "a separate inequality-direction derivation or validated "
            "zero-count/presence certificates."
        ),
        "known_zero_ordinate_table_used": False,
        "global_rh_certificate": False,
    }
    (
        ROOT / "outputs" / "coefficient_orientation_audit.json"
    ).write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, indent=2, ensure_ascii=False))
    if not output["orientation_blocker_confirmed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

