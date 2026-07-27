from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any

from occupancy_cert.rational_interval import as_fraction


ROOT = Path(__file__).resolve().parent
OUTPUTS = ROOT / "outputs"
OUTPUT = OUTPUTS / "experiment_summary.json"


def read_json(name: str) -> Any:
    return json.loads((OUTPUTS / name).read_text(encoding="utf-8"))


def main() -> None:
    semantic = read_json("occupancy_semantic_bridge.json")
    cover = read_json("dirichlet_green_cover_certificate.json")
    cover_verification = read_json(
        "dirichlet_green_cover_verification.json"
    )
    clamped = read_json("clamped_58cell_radius_certificate.json")
    clamped_verification = read_json(
        "clamped_58cell_radius_verification.json"
    )
    floating = read_json("floating_clamped_location_study.json")
    rows = {
        row["cell_half_width"]: row
        for row in floating["adversarial_corner_rows"]
    }
    certified_radius = as_fraction(
        clamped["parameters"]["uniform_location_radius"]
    )
    diagnostic_above_width = Fraction(16, 1000)
    scale_gap = float(diagnostic_above_width / certified_radius)
    checks = {
        "exact_semantic_bridge": semantic["classification"][
            "exact_semantic_theorem"
        ],
        "count_only_failure_exact": (
            as_fraction(
                semantic["count_only_counterexample"][
                    "exact_point_proof"
                ]["schur_determinant"]
            )
            < 0
        ),
        "cover_verification": cover_verification["verification_pass"],
        "adaptive_cover_complete": (
            cover["statistics"]["certified_leaf_count"] == 8
            and cover["statistics"]["unresolved_leaf_count"] == 0
        ),
        "clamped_verification": clamped_verification[
            "verification_pass"
        ],
        "clamped_coercivity_positive": (
            as_fraction(
                clamped["proof_budget"]["coercivity_lower_bound"]
            )
            > 0
        ),
        "floating_transition_seen": (
            rows[0.016]["adversarial_corner_threshold"] > 1.0
            and rows[0.017]["adversarial_corner_threshold"] < 1.0
        ),
        "global_flags_false": all(
            value is False
            for value in (
                semantic["classification"]["global_rh_certificate"],
                cover["classification"]["global_rh_certificate"],
                cover_verification["global_rh_certificate"],
                clamped["classification"]["global_rh_certificate"],
                clamped_verification["global_rh_certificate"],
                floating["classification"]["global_rh_certificate"],
            )
        ),
    }
    result = {
        "schema": "RH.Occupancy.OperatorFamilySummary.v0.9",
        "node": "RH-Occupancy-OperatorFamily-20260725-v0.9",
        "summary_pass": all(checks.values()),
        "checks": checks,
        "exact_results": {
            "count_only_counterexample_determinant": semantic[
                "count_only_counterexample"
            ]["exact_point_proof"]["schur_determinant"],
            "count_only_negative_quadratic": semantic[
                "count_only_counterexample"
            ]["negative_quadratic_value"],
            "synthetic_cover_leaf_count": cover["statistics"][
                "certified_leaf_count"
            ],
            "synthetic_cover_maximum_depth": cover["statistics"][
                "maximum_leaf_depth"
            ],
            "synthetic_cover_minimum_determinant_lower": cover[
                "statistics"
            ]["minimum_determinant_lower"],
            "clamped_certified_uniform_radius": clamped["parameters"][
                "uniform_location_radius"
            ],
            "clamped_budget_critical_radius": clamped["proof_budget"][
                "critical_uniform_radius_for_this_budget"
            ],
            "clamped_coercivity_lower_bound": clamped["proof_budget"][
                "coercivity_lower_bound"
            ],
        },
        "floating_diagnostic": {
            "fixed_location_threshold": floating[
                "base_fixed_location_threshold"
            ],
            "observed_transition_bracket": floating[
                "observed_transition_bracket"
            ],
            "tested_width_0_016_threshold": rows[0.016][
                "adversarial_corner_threshold"
            ],
            "tested_width_0_017_threshold": rows[0.017][
                "adversarial_corner_threshold"
            ],
            "diagnostic_to_certified_radius_ratio": scale_gap,
            "interpretation": (
                "The roughly 8e12 scale gap is a proof-budget gap, "
                "not a certified operator-family gap."
            ),
        },
        "decision": {
            "occupancy_quantifier_architecture": "retained",
            "scalar_count_operator_substitution": "rejected",
            "next_primary_bottleneck": (
                "local interval Green derivatives and adaptive "
                "location-cell Schur covers"
            ),
            "zeta_presence_cells": "open",
            "upper_envelope_no_go_track": "separate",
        },
        "classification": {
            "exact_synthetic_occupancy_family": True,
            "conditional_abstract_clamped_family": True,
            "actual_zeta_occupancy_family": False,
            "explicit_formula_global_transfer": False,
            "global_rh_certificate": False,
        },
    }
    OUTPUT.write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    if not result["summary_pass"]:
        failed = [key for key, value in checks.items() if not value]
        raise SystemExit(f"summary checks failed: {failed}")
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

