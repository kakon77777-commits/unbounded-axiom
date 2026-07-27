from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np

from pwext.green import continuous_atomic_threshold


ROOT = Path(__file__).resolve().parent


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def fraction_value(value: dict[str, int]) -> float:
    return value["numerator"] / value["denominator"]


def verify() -> dict[str, Any]:
    witness = read_json(
        ROOT / "outputs" / "rational_atomic_witness.json"
    )
    denominator = int(witness["weight_denominator"])
    rational_probability_sums_pass = all(
        sum(
            int(row["weight"]["numerator"])
            for row in group
        )
        == denominator
        for group in witness["axis_supports"]
    ) and (
        sum(
            int(row["weight"]["numerator"])
            for row in witness["core_support"]
        )
        == denominator
    )
    axis_supports = [
        [
            {
                "x": fraction_value(row["x"]),
                "weight": fraction_value(row["weight"]),
            }
            for row in group
        ]
        for group in witness["axis_supports"]
    ]
    core_support = [
        {
            "x": fraction_value(row["x"]),
            "y": fraction_value(row["y"]),
            "weight": fraction_value(row["weight"]),
        }
        for row in witness["core_support"]
    ]
    coefficients = np.asarray(
        [
            fraction_value(row)
            for row in witness["model"]["count_coefficients"]
        ]
    )
    tail_scale = fraction_value(
        witness["model"]["tail_scale_lower_decimal_rational"]
    )
    alpha = fraction_value(
        witness["model"]["target_alpha"]
    )
    recomputed = continuous_atomic_threshold(
        radius=fraction_value(
            witness["model"]["radius"]
        ),
        time_step=0.01,
        count_coefficients=coefficients,
        axis_supports=axis_supports,
        core_support=core_support,
        safe_alpha=alpha,
        tail_scale_override=tail_scale,
    )
    stored = next(
        row
        for row in witness["floating_green_audit_rows"]
        if abs(row["time_step"] - 0.01) < 1e-12
    )
    schur_difference = abs(
        recomputed["schur_certificate_minimum_eigenvalue"]
        - stored["schur_certificate_minimum_eigenvalue"]
    )
    full_difference = abs(
        recomputed["tested_safe_minimum_eigenvalue"]
        - stored["tested_safe_minimum_eigenvalue"]
    )
    checks = {
        "rational_probability_sums_pass": (
            rational_probability_sums_pass
        ),
        "axis_atom_count_is_58": (
            sum(len(group) for group in axis_supports) == 58
        ),
        "core_atom_count_is_2": len(core_support) == 2,
        "target_alpha_is_21_over_20": alpha == 1.05,
        "recomputed_safe_psd": bool(
            recomputed["tested_safe_psd"]
        ),
        "recomputed_schur_positive": (
            recomputed[
                "schur_certificate_minimum_eigenvalue"
            ]
            > 0.06
        ),
        "schur_reconstruction_difference_below_1e_11": (
            schur_difference < 1e-11
        ),
        "full_reconstruction_difference_below_1e_10": (
            full_difference < 1e-10
        ),
        "interval_flag_remains_false": not witness[
            "interval_certified"
        ],
        "global_flag_remains_false": not witness[
            "global_rh_certificate"
        ],
    }
    return {
        "schema": "RH.PaleyWiener.OutputVerification.v0.6",
        "recomputed_time_step": 0.01,
        "recomputed_schur_minimum_eigenvalue": recomputed[
            "schur_certificate_minimum_eigenvalue"
        ],
        "stored_schur_minimum_eigenvalue": stored[
            "schur_certificate_minimum_eigenvalue"
        ],
        "schur_minimum_abs_difference": schur_difference,
        "full_minimum_abs_difference": full_difference,
        "checks": checks,
        "verification_pass": all(checks.values()),
        "verification_level": (
            "E1 rational serialization and E2 floating direct "
            "Green reconstruction; no interval certification"
        ),
        "interval_certified": False,
        "global_rh_certificate": False,
    }


def main() -> None:
    output = verify()
    (
        ROOT / "outputs" / "output_verification.json"
    ).write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, indent=2, ensure_ascii=False))
    if not output["verification_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
