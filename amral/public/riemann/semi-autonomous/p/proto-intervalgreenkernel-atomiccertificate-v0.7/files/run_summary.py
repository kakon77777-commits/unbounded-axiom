from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def read(name: str) -> dict:
    return json.loads(
        (ROOT / "outputs" / name).read_text(encoding="utf-8")
    )


def main() -> None:
    certificate = read("interval_atomic_certificate.json")
    verification = read("certificate_verification.json")
    exact_audit = read("exact_serialization_audit.json")
    crosscheck = read("floating_crosscheck.json")
    orientation = read("coefficient_orientation_audit.json")
    stress = read("orientation_stress_test.json")
    summary = {
        "schema": "RH.IntervalGreenKernel.ExperimentSummary.v0.7",
        "node": certificate["node"],
        "abstract_interval_result": {
            "target_alpha": certificate["statement"]["target_alpha"],
            "positive_rank": certificate["input"]["positive_rank"],
            "negative_rank": certificate["input"]["negative_rank"],
            "neumann_defect_upper": certificate["proof"][
                "neumann_defect_infinity_norm_upper"
            ],
            "first_minor_lower": certificate["proof"][
                "first_leading_minor_lower"
            ],
            "determinant_lower": certificate["proof"][
                "determinant_lower"
            ],
            "abstract_continuous_interval_certificate": True,
        },
        "replay": {
            "full_verification_pass": verification[
                "verification_pass"
            ],
            "exact_serialization_audit_pass": exact_audit[
                "audit_pass"
            ],
            "floating_crosscheck_difference": crosscheck[
                "absolute_difference"
            ],
        },
        "coefficient_bridge": {
            "orientation_blocker_confirmed": orientation[
                "orientation_blocker_confirmed"
            ],
            "all_stored_coefficients_are_lower_certificates": (
                orientation[
                    "all_stored_coefficients_are_lower_certificates"
                ]
            ),
            "lower_profile_stress_minimum_eigenvalue": stress[
                "floating_schur_eigenvalues"
            ][0],
            "fixed_witness_survives_lower_profile": stress[
                "fixed_witness_survives_lower_profile"
            ],
        },
        "next_node": "RH-RobustBandCounts-ZetaBridge-20260725-v0.8",
        "zeta_facing_tail_theorem_certified": False,
        "zeta_facing_count_coefficients_certified": False,
        "explicit_formula_admissibility_certified": False,
        "global_rh_certificate": False,
    }
    (
        ROOT / "outputs" / "experiment_summary.json"
    ).write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

