from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any

from occupancy_cert.clamped_budget import (
    file_sha256,
    verify_clamped_radius_certificate,
)
from occupancy_cert.cover import verify_cover
from occupancy_cert.rational_interval import as_fraction
from occupancy_cert.semantics import occupancy_semantic_audit


ROOT = Path(__file__).resolve().parent
OUTPUTS = ROOT / "outputs"
DATA = ROOT / "data"
OUTPUT = OUTPUTS / "output_verification.json"


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    model = read_json(DATA / "synthetic_occupancy_model.json")
    witness_path = DATA / "parent_v0.7_rational_atomic_witness.json"
    parent_path = DATA / "parent_v0.7_interval_atomic_certificate.json"
    witness = read_json(witness_path)
    parent = read_json(parent_path)
    semantic = read_json(OUTPUTS / "occupancy_semantic_bridge.json")
    cover = read_json(
        OUTPUTS / "dirichlet_green_cover_certificate.json"
    )
    cover_stored_verification = read_json(
        OUTPUTS / "dirichlet_green_cover_verification.json"
    )
    clamped = read_json(
        OUTPUTS / "clamped_58cell_radius_certificate.json"
    )
    clamped_stored_verification = read_json(
        OUTPUTS / "clamped_58cell_radius_verification.json"
    )
    floating = read_json(
        OUTPUTS / "floating_clamped_location_study.json"
    )
    summary = read_json(OUTPUTS / "experiment_summary.json")

    cover_recomputed = verify_cover(model, cover)
    clamped_recomputed = verify_clamped_radius_certificate(
        witness,
        parent,
        clamped,
        file_sha256(witness_path),
        file_sha256(parent_path),
    )
    floating_rows = {
        row["cell_half_width"]: row
        for row in floating["adversarial_corner_rows"]
    }
    refinement_map = {
        row["cell_half_width"]: row["fixed_corner_time_refinement"]
        for row in floating["time_refinements"]
    }
    checks = {
        "semantic_exact_regeneration": (
            semantic == occupancy_semantic_audit(model)
        ),
        "counterexample_determinant_exact": (
            semantic["count_only_counterexample"][
                "exact_point_proof"
            ]["schur_determinant"]
            == "-254/558009"
        ),
        "counterexample_direction_exact": (
            semantic["count_only_counterexample"][
                "negative_quadratic_value"
            ]
            == "-663194/13755479859"
        ),
        "cover_reverification": cover_recomputed["verification_pass"],
        "cover_verification_reproduced": (
            cover_recomputed == cover_stored_verification
        ),
        "cover_shape": (
            cover["statistics"]["node_count"] == 15
            and cover["statistics"]["certified_leaf_count"] == 8
            and cover["statistics"]["maximum_leaf_depth"] == 7
        ),
        "cover_minimum_strict": (
            as_fraction(
                cover["statistics"]["minimum_determinant_lower"]
            )
            > 0
        ),
        "clamped_reverification": clamped_recomputed[
            "verification_pass"
        ],
        "clamped_verification_reproduced": (
            clamped_recomputed == clamped_stored_verification
        ),
        "clamped_radius_exact": (
            as_fraction(
                clamped["parameters"]["uniform_location_radius"]
            )
            == Fraction(1, 500_000_000_000_000)
        ),
        "clamped_positive_margin": (
            as_fraction(
                clamped["proof_budget"]["coercivity_lower_bound"]
            )
            > 0
        ),
        "floating_base_calibration": (
            1.13 < floating["base_fixed_location_threshold"] < 1.14
        ),
        "floating_transition": (
            floating_rows[0.016]["adversarial_corner_threshold"] > 1
            and floating_rows[0.017][
                "adversarial_corner_threshold"
            ]
            < 1
        ),
        "floating_time_refinement_stable": all(
            max(row["threshold"] for row in values)
            - min(row["threshold"] for row in values)
            < 2e-5
            for values in refinement_map.values()
        ),
        "floating_not_universal": (
            floating["classification"][
                "universal_location_quantifier_certified"
            ]
            is False
        ),
        "summary_pass": summary["summary_pass"],
        "all_global_flags_false": all(
            value is False
            for value in (
                semantic["classification"]["global_rh_certificate"],
                cover["classification"]["global_rh_certificate"],
                cover_stored_verification["global_rh_certificate"],
                clamped["classification"]["global_rh_certificate"],
                clamped_stored_verification["global_rh_certificate"],
                floating["classification"]["global_rh_certificate"],
                summary["classification"]["global_rh_certificate"],
            )
        ),
    }
    result = {
        "schema": "RH.Occupancy.OperatorFamilyVerification.v0.9",
        "checks": checks,
        "verification_pass": all(checks.values()),
        "exact_cover_leaf_count": cover["statistics"][
            "certified_leaf_count"
        ],
        "exact_clamped_coercivity_lower": clamped["proof_budget"][
            "coercivity_lower_bound"
        ],
        "floating_transition_bracket": floating[
            "observed_transition_bracket"
        ],
        "global_rh_certificate": False,
    }
    OUTPUT.write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    if not result["verification_pass"]:
        failed = [key for key, value in checks.items() if not value]
        raise SystemExit(f"output verification failed: {failed}")
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

