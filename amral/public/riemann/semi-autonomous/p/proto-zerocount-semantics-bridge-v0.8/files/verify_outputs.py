from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from bridge.axis import lower_profile_downward
from bridge.semantics import semantic_audit


ROOT = Path(__file__).resolve().parent
OUTPUTS = ROOT / "outputs"
OUTPUT = OUTPUTS / "output_verification.json"


def read_json(name: str) -> Any:
    return json.loads((OUTPUTS / name).read_text(encoding="utf-8"))


def probability_sum(support: list[dict[str, float]]) -> float:
    return sum(float(row["weight"]) for row in support)


def main() -> None:
    semantic = read_json("semantic_bridge.json")
    profile = read_json("typed_count_profile.json")
    lineage = read_json("lineage_semantic_audit.json")
    experiment = read_json("lower_profile_experiment.json")
    summary = read_json("experiment_summary.json")
    rows = experiment["galerkin_rows"]
    direct = experiment["direct_green_transfer"]
    supports = experiment["final_atomic_measures"]["axis_supports"]
    active_sums = [
        probability_sum(support)
        for coefficient, support in zip(
            experiment["configuration"]["count_profile"],
            supports,
        )
        if coefficient > 0
    ]
    checks = {
        "semantic_recomputed": semantic == semantic_audit(),
        "lower_profile_recomputed": (
            profile["downward_floating_lower_profile"]
            == lower_profile_downward()
        ),
        "lineage_retains_v07": lineage[
            "abstract_v0_7_certificate_retained"
        ],
        "dimensions_strictly_increase": all(
            right["effective_dimension"]
            > left["effective_dimension"]
            for left, right in zip(rows[:-1], rows[1:])
        ),
        "low_dimension_obstruction_seen": (
            rows[0]["alpha"] > 1.0
            and rows[1]["alpha"] > 1.0
        ),
        "high_dimension_escape_seen": (
            rows[2]["alpha"] < 1.0
            and rows[-1]["alpha"] < 0.14
        ),
        "direct_green_steps_refine": (
            [row["time_grid_count"] for row in direct]
            == [1601, 3201, 6401]
        ),
        "direct_green_matches_galerkin": abs(
            direct[-1]["raw_threshold_for_fixed_measures"]
            - rows[-1]["alpha"]
        )
        < 5e-6,
        "sampled_primal_escape": (
            experiment["primal_escape_diagnostic"][
                "normalized_objective"
            ]
            < 0.14
        ),
        "sampled_core_normalization": (
            experiment["primal_escape_diagnostic"][
                "normalized_core_maximum"
            ]
            == -1.0
        ),
        "active_probability_sums": all(
            abs(value - 1.0) < 2e-10
            for value in active_sums
        ),
        "summary_pass": summary["summary_pass"],
        "all_global_flags_false": all(
            value is False
            for value in (
                semantic["global_rh_certificate"],
                profile["global_rh_certificate"],
                lineage["global_rh_certificate"],
                experiment["global_rh_certificate"],
                summary["classification"]["global_rh_certificate"],
            )
        ),
    }
    output = {
        "schema": "RH.ZeroCountSemanticsBridge.Verification.v0.8",
        "checks": checks,
        "verification_pass": all(checks.values()),
        "recomputed_final_galerkin_alpha": rows[-1]["alpha"],
        "recomputed_final_direct_green_threshold": direct[-1][
            "raw_threshold_for_fixed_measures"
        ],
        "recomputed_sampled_primal_objective": experiment[
            "primal_escape_diagnostic"
        ]["normalized_objective"],
        "global_rh_certificate": False,
    }
    OUTPUT.write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    if not output["verification_pass"]:
        failed = [key for key, value in checks.items() if not value]
        raise SystemExit(f"output verification failed: {failed}")
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
