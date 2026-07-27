from __future__ import annotations

import hashlib
import json
from decimal import Decimal
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def exact_decimal(value: str) -> Fraction:
    return Fraction(Decimal(value))


def main() -> None:
    certificate_path = (
        ROOT / "outputs" / "interval_atomic_certificate.json"
    )
    certificate = json.loads(
        certificate_path.read_text(encoding="utf-8")
    )
    verification = json.loads(
        (
            ROOT / "outputs" / "certificate_verification.json"
        ).read_text(encoding="utf-8")
    )
    witness = json.loads(
        (
            ROOT
            / "data"
            / "rational_atomic_witness_v0.6.json"
        ).read_text(encoding="utf-8")
    )
    proof = certificate["proof"]
    first_minor = exact_decimal(
        proof["first_leading_minor_lower"]
    )
    determinant = exact_decimal(proof["determinant_lower"])
    neumann_defect = exact_decimal(
        proof["neumann_defect_infinity_norm_upper"]
    )
    axis_sums = [
        sum(
            (
                Fraction(
                    atom["weight"]["numerator"],
                    atom["weight"]["denominator"],
                )
                for atom in support
            ),
            Fraction(0),
        )
        for support in witness["axis_supports"]
    ]
    core_sum = sum(
        (
            Fraction(
                atom["weight"]["numerator"],
                atom["weight"]["denominator"],
            )
            for atom in witness["core_support"]
        ),
        Fraction(0),
    )
    checks = {
        "serialized_neumann_defect_below_one": (
            0 <= neumann_defect < 1
        ),
        "serialized_first_minor_strictly_positive": (
            first_minor > 0
        ),
        "serialized_determinant_strictly_positive": (
            determinant > 0
        ),
        "all_axis_probabilities_exactly_one": all(
            value == 1 for value in axis_sums
        ),
        "core_probability_exactly_one": core_sum == 1,
        "full_recomputation_passed": bool(
            verification["verification_pass"]
        ),
        "abstract_interval_flag_true": (
            certificate["classification"][
                "abstract_continuous_interval_certificate"
            ]
            is True
        ),
        "layer_b_flags_false": all(
            certificate["classification"][key] is False
            for key in (
                "zeta_facing_tail_theorem_certified",
                "zeta_facing_count_coefficients_certified",
                "explicit_formula_admissibility_certified",
            )
        ),
        "global_flag_false": (
            certificate["classification"]["global_rh_certificate"]
            is False
        ),
    }
    output = {
        "schema": "RH.IntervalGreenKernel.ExactSerializationAudit.v0.7",
        "certificate_sha256": hashlib.sha256(
            certificate_path.read_bytes()
        ).hexdigest(),
        "checks": checks,
        "audit_pass": all(checks.values()),
        "interpretation": (
            "Exact Fraction arithmetic validates the serialized proof "
            "inequalities and trust flags after full interval replay."
        ),
        "global_rh_certificate": False,
    }
    (
        ROOT / "outputs" / "exact_serialization_audit.json"
    ).write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, indent=2, ensure_ascii=False))
    if not output["audit_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

