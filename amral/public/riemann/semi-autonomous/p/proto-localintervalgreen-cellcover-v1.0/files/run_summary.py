from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "outputs"


def read_json(name: str) -> Any:
    return json.loads((OUTPUT / name).read_text(encoding="utf-8"))


def main() -> None:
    certificate = read_json(
        "local_green_cell_certificate_h178e-8.json"
    )
    ladder = read_json("local_green_radius_ladder.json")
    family = read_json("local_green_cover_family.json")
    corner = read_json(
        "adversarial_corner_point_certificate_h1e-3.json"
    )
    verification = read_json("output_verification.json")
    rows = {row["label"]: row for row in ladder["rows"]}
    checks = {
        "maximum_box_pass": certificate["proof"]["certificate_pass"],
        "maximum_box_verifies": verification["checks"][
            "maximum_certificate_verifies"
        ],
        "cover_family_verifies": verification["checks"][
            "cover_family_verifies"
        ],
        "boundary_failure_not_counterexample": (
            rows["first_tested_boundary_failure"][
                "failure_is_point_counterexample"
            ]
            is False
        ),
        "exact_corner_point_pass": corner["proof"][
            "certificate_pass"
        ],
        "actual_zeta_flag_false": (
            certificate["classification"][
                "actual_zeta_occupancy_family"
            ]
            is False
        ),
        "global_flag_false": (
            certificate["classification"][
                "global_rh_certificate"
            ]
            is False
        ),
    }
    result = {
        "schema": "RH.LocalIntervalGreen.ExperimentSummary.v1.0",
        "node": "RH-LocalIntervalGreen-CellCover-20260725-v1.0",
        "technical_cap_status": "complete",
        "main_result": {
            "axis_location_dimension": 58,
            "band_count": family["band_count"],
            "band_atom_counts": family["band_atom_counts"],
            "child_alpha": "1/1",
            "certified_uniform_half_width": ladder[
                "certified_uniform_half_width"
            ],
            "first_tested_failure_above": ladder[
                "first_tested_failure_above_certified_width"
            ],
            "exact_improvement_over_v0.9": ladder[
                "exact_radius_improvement_factor"
            ],
            "neumann_defect_upper": certificate["proof"][
                "neumann_defect_infinity_norm_upper"
            ],
            "first_minor_lower": certificate["proof"][
                "first_leading_minor_lower"
            ],
            "determinant_lower": certificate["proof"][
                "determinant_lower"
            ],
        },
        "failure_audit": {
            "at_1.8e-6": rows[
                "first_tested_boundary_failure"
            ]["failure_class"],
            "at_1e-4": rows["requested_1e-4"]["failure_class"],
            "at_1e-3": rows["requested_1e-3"]["failure_class"],
            "exact_h1e-3_corner_point_passes": corner["proof"][
                "certificate_pass"
            ],
            "interpretation": (
                "Failed universal-box enclosures are inconclusive "
                "proof-system outcomes, not certified operator "
                "counterexamples."
            ),
        },
        "checks": checks,
        "summary_pass": all(checks.values()),
        "next_round": (
            "integrated research report and downstream AI handoff"
        ),
        "actual_zeta_occupancy_family": False,
        "explicit_formula_transfer_certified": False,
        "global_rh_certificate": False,
    }
    path = OUTPUT / "experiment_summary.json"
    path.write_text(
        json.dumps(
            result,
            indent=2,
            ensure_ascii=False,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    if not result["summary_pass"]:
        raise SystemExit(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

