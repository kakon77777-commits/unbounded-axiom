from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent


def read_json(name: str) -> Any:
    return json.loads(
        (ROOT / "outputs" / name).read_text(encoding="utf-8")
    )


def main() -> None:
    uniform = read_json("uniform_frontier.json")
    joint = read_json("joint_dual_summary.json")
    refinement = read_json("axis_refinement.json")
    prime = read_json("prime_cost.json")
    witness = read_json("witness_verification.json")
    cover = read_json("cover_audit.json")
    source = read_json("source_profile.json")
    prime_benchmarks = {
        row["radius"]: row for row in prime["benchmark_rows"]
    }
    output = {
        "schema": "RH.SupportPrime.ExperimentSummary.v0.4",
        "date": "2026-07-24",
        "research_mode": "semi-autonomous AI mathematical research",
        "target_window": cover["target_window"],
        "original_patch_count": cover["original_patch_count"],
        "refined_patch_count": cover["refined_patch_count"],
        "uniform_configuration_count": uniform["row_count"],
        "uniform_first_center_escape": uniform[
            "first_sampled_any_geometry_center_escape"
        ],
        "uniform_first_patch_measure_escape": uniform[
            "first_sampled_any_geometry_uniform_patch_escape"
        ],
        "joint_radius_rows": [
            {
                "radius": row["radius"],
                "dimension": row["dimension"],
                "searched_candidate_count": row[
                    "searched_candidate_count"
                ],
                "strongest_safe_alpha": row[
                    "strongest_searched_safe_alpha"
                ],
                "at_least_one_searched_patch_blocked": row[
                    "at_least_one_searched_patch_blocked"
                ],
            }
            for row in joint["radius_rows"]
        ],
        "all_sampled_support_only_radii_have_a_dual_block": all(
            row["at_least_one_searched_patch_blocked"]
            for row in joint["radius_rows"]
        ),
        "axis_coarse_grid_false_escape": refinement[
            "coarse_grid_false_escape"
        ],
        "axis_refinement_alpha_path": [
            {
                "step": row["axis_step"],
                "alpha": row["alpha"],
                "safe_alpha": row["safe_alpha"],
            }
            for row in refinement["rows"]
        ],
        "serialized_witness_count": witness[
            "actual_witness_count"
        ],
        "all_serialized_witnesses_reconstruct_psd": witness[
            "all_serialized_sparse_witnesses_psd"
        ],
        "all_serialized_measures_block_budget": witness[
            "all_serialized_measures_block_budget"
        ],
        "r10_25_prime_benchmark": prime_benchmarks[10.25],
        "r16_prime_cost_projection": next(
            row
            for row in prime["projection_rows"]
            if row["radius"] == 16.0
        ),
        "published_s_bound": source["published_s_bound"],
        "primal_high_cost_search_started": False,
        "primal_gate_reason": (
            "Every sampled radius has at least one searched patch "
            "blocked by a reconstructed safe dual witness."
        ),
        "research_decision": (
            "Stop support-only expansion and proceed to "
            "RH_Axis_Notch_Cover_Codesign_v0.5."
        ),
        "full_refined_cover_joint_gate_exhausted": joint[
            "full_refined_cover_joint_gate_exhausted"
        ],
        "known_zero_ordinates_used": False,
        "global_rh_certificate": False,
    }
    (ROOT / "outputs" / "experiment_summary.json").write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
