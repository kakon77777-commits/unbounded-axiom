from __future__ import annotations

import json
import math
from decimal import Decimal
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def midpoint(row: dict[str, str]) -> float:
    return float(
        (Decimal(row["lo"]) + Decimal(row["hi"])) / Decimal(2)
    )


def fraction(row: dict[str, int]) -> Fraction:
    return Fraction(row["numerator"], row["denominator"])


def main() -> None:
    witness = json.loads(
        (
            ROOT
            / "data"
            / "rational_atomic_witness_v0.6.json"
        ).read_text(encoding="utf-8")
    )
    certificate = json.loads(
        (
            ROOT / "outputs" / "interval_atomic_certificate.json"
        ).read_text(encoding="utf-8")
    )
    matrix = certificate["proof"]["final_two_by_two_matrix"]
    t00 = midpoint(matrix[0][0])
    t01 = midpoint(matrix[0][1])
    t11 = midpoint(matrix[1][1])
    alpha = fraction(witness["model"]["target_alpha"])
    core_weights = [
        fraction(atom["weight"])
        for atom in witness["core_support"]
    ]
    b0 = float(2 * alpha * core_weights[0])
    b1 = float(2 * alpha * core_weights[1])
    s00 = b0 * t00
    s01 = math.sqrt(b0 * b1) * t01
    s11 = b1 * t11
    minimum = (
        s00
        + s11
        - math.sqrt((s00 - s11) ** 2 + 4 * s01 * s01)
    ) / 2
    parent = float(
        witness["finest_schur_minimum_eigenvalue"]
    )
    output = {
        "schema": "RH.IntervalGreenKernel.FloatingCrosscheck.v0.7",
        "interval_midpoint_schur_matrix": [
            [s00, s01],
            [s01, s11],
        ],
        "interval_midpoint_minimum_eigenvalue": minimum,
        "parent_grid_minimum_eigenvalue": parent,
        "absolute_difference": abs(minimum - parent),
        "crosscheck_below_1e_7": abs(minimum - parent) < 1e-7,
        "role": (
            "diagnostic agreement only; the proof uses interval "
            "Neumann and Sylvester inequalities."
        ),
        "global_rh_certificate": False,
    }
    (
        ROOT / "outputs" / "floating_crosscheck.json"
    ).write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, indent=2, ensure_ascii=False))
    if not output["crosscheck_below_1e_7"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

