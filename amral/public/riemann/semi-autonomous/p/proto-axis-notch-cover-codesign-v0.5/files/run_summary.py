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
    atlas = read_json("peak_atlas.json")
    notch = read_json("notch_screen.json")
    lift = read_json("lift_joint.json")
    geometry = read_json("geometry_joint.json")
    verification = read_json("joint_verification.json")
    best_geometry = min(
        geometry["rows"],
        key=lambda row: row["joint_dual"]["alpha"],
    )
    anchor_flat = next(
        row
        for row in notch["rows"]
        if row["radius"] == 16.0
        and row["code_id"] == "anchor_flat"
    )
    output = {
        "schema": "RH.AxisNotch.ExperimentSummary.v0.5",
        "date": "2026-07-24",
        "research_mode": "semi-autonomous AI mathematical research",
        "parent_node": "RH-SupportPrime-DualFrontier-20260724-v0.4",
        "target_window": {
            "x": [20.0, 20.5],
            "y": [-0.2, -0.1],
        },
        "parent_witness_count_in_peak_atlas": atlas[
            "parent_witness_count"
        ],
        "axis_peak_atlas": atlas["structural_observation"],
        "subspace_notch_result": {
            "theorem": (
                "Adding homogeneous notch constraints creates a "
                "subspace of the already searched parent function "
                "space and cannot improve primal feasibility."
            ),
            "anchor_flat_optimized_core_uniform_threshold": (
                anchor_flat[
                    "optimized_core_uniform_axis_threshold"
                ]
            ),
            "anchor_flat_derivative_norm": anchor_flat[
                "anchor_derivative_frobenius_norm"
            ],
        },
        "external_lift_result": {
            "family": "t*q_R(t)*sin(omega*t)",
            "baseline_alpha": lift["rows"][0]["joint_dual"][
                "alpha"
            ],
            "grid21_alpha": lift["rows"][1]["joint_dual"][
                "alpha"
            ],
            "relative_improvement": lift[
                "raw_alpha_relative_improvement"
            ],
            "crosses_dual_gate": lift[
                "lift_family_crosses_dual_gate"
            ],
        },
        "best_geometry_result": {
            "geometry_id": best_geometry["geometry_id"],
            "dimension": best_geometry["dimension"],
            "alpha": best_geometry["joint_dual"]["alpha"],
            "safe_alpha": best_geometry["joint_dual"][
                "safe_alpha"
            ],
            "safe_min_eigenvalue": best_geometry[
                "joint_dual"
            ]["safe_min_eigenvalue"],
            "relative_improvement_vs_baseline": best_geometry[
                "raw_alpha_relative_improvement_vs_baseline"
            ],
            "crosses_dual_gate": not best_geometry[
                "safe_budget_block"
            ],
        },
        "primal_search_started": False,
        "primal_gate_reason": (
            "Every joint candidate retains a reconstructed safe "
            "dual lower bound above 1."
        ),
        "research_decision": (
            "Stop homogeneous subspace notches, stop the tested "
            "spectral-slope lift family, and stop further polynomial "
            "bump scaling. Formulate the next node as a continuous "
            "Paley-Wiener axis-core extremal problem."
        ),
        "next_node": "RH-PaleyWiener-AxisCoreExtremal-20260724-v0.6",
        "joint_verification_pass": verification[
            "all_reconstructed_psd_and_block_budget"
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
