from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
OUTPUTS = ROOT / "outputs"


def read_json(name: str) -> Any:
    return json.loads((OUTPUTS / name).read_text(encoding="utf-8"))


def main() -> None:
    semantic = read_json("semantic_bridge.json")
    profile = read_json("typed_count_profile.json")
    lineage = read_json("lineage_semantic_audit.json")
    experiment = read_json("lower_profile_experiment.json")
    output = {
        "schema": "RH.ZeroCountSemanticsBridge.Summary.v0.8",
        "node": "RH-ZeroCount-SemanticsBridge-20260725-v0.8",
        "main_results": {
            "upper_count_supremum_envelope_valid": True,
            "lower_count_infimum_minorant_valid": True,
            "lower_count_arbitrary_measure_transfer_valid": False,
            "v0_7_abstract_interval_certificate_retained": (
                lineage["abstract_v0_7_certificate_retained"]
            ),
            "v0_7_actual_zero_side_obstruction_proved": False,
            "lower_profile_high_dimension_alpha": (
                experiment["galerkin_rows"][-1]["alpha"]
            ),
            "lower_profile_direct_green_threshold": (
                experiment[
                    "fixed_measure_direct_threshold_last"
                ]
            ),
            "sampled_primal_escape_objective": (
                experiment["primal_escape_diagnostic"][
                    "normalized_objective"
                ]
            ),
        },
        "decision": (
            "Stop treating scalar count intervals as operator mass. "
            "Retain v0.7 as an abstract certificate and pursue two "
            "separate theorem tracks: certify the upper-envelope no-go "
            "statement, or add location/occupancy certificates that "
            "really dominate zero-side evaluation operators."
        ),
        "required_next_object": (
            "A band occupancy certificate carrying locations or cells, "
            "multiplicities, endpoint conventions, and an operator-"
            "dominance statement; scalar counts alone are insufficient."
        ),
        "prototype_status": lineage["target_patch_relevance"],
        "checks": {
            "semantic_counterexample_pass": semantic[
                "all_invalid_rules_refuted"
            ],
            "profile_remains_uncertified": not profile[
                "zeta_facing_profile_certified"
            ],
            "lower_profile_escape_observed": not experiment[
                "high_dimension_obstruction_above_one"
            ],
            "global_flag_false": not experiment[
                "global_rh_certificate"
            ],
        },
        "classification": {
            "exact_semantic_theorems": True,
            "floating_lower_profile_diagnostic": True,
            "upper_envelope_method_nogo_fully_certified": False,
            "actual_zero_side_operator_bridge": False,
            "explicit_formula_transfer": False,
            "global_rh_certificate": False,
        },
    }
    output["summary_pass"] = all(output["checks"].values())
    (OUTPUTS / "experiment_summary.json").write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    if not output["summary_pass"]:
        raise SystemExit("summary checks failed")
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
