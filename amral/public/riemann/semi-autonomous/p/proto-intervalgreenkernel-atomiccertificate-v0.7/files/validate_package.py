from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MAIN_PAPER = (
    "區間Green核原子證書_RH抽象連續障礙的有理包絡與二階"
    "Sylvester判定_v0.7_半AI自主研究稿.md"
)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    required = [
        "README.md",
        "THEORY.md",
        "METHOD.md",
        "RESULTS.md",
        "TRUST_BOUNDARY.md",
        "REPLAY.md",
        "RESEARCH_LOG.md",
        "NEXT_NODE_ROBUST_COUNTS.md",
        "SOURCES.md",
        "CHANGELOG.md",
        "LICENSE",
        MAIN_PAPER,
        "data/rational_atomic_witness_v0.6.json",
        "outputs/interval_atomic_certificate.json",
        "outputs/certificate_verification.json",
        "outputs/exact_serialization_audit.json",
        "outputs/floating_crosscheck.json",
        "outputs/coefficient_orientation_audit.json",
        "outputs/orientation_stress_test.json",
        "outputs/experiment_summary.json",
        "metadata/research_node.json",
        "metadata/claim_register.json",
        "metadata/gap_ledger.json",
        "metadata/handoff.json",
        "metadata/source_lineage.json",
        "generate_certificate.py",
        "verify_certificate.py",
        "audit_certificate.py",
        "run_coefficient_orientation_audit.py",
        "run_orientation_stress_test.py",
        "run_floating_crosscheck.py",
        "run_summary.py",
        "tests/test_interval_certificate.py",
    ]
    missing = [
        relative
        for relative in required
        if not (ROOT / relative).is_file()
    ]

    json_files = sorted(ROOT.rglob("*.json"))
    json_errors = []
    for path in json_files:
        try:
            load_json(path)
        except Exception as error:
            json_errors.append(
                f"{path.relative_to(ROOT)}: {error}"
            )

    markdown_files = sorted(ROOT.glob("*.md"))
    math_errors = []
    forbidden = re.compile(r"\\\(|\\\)|\\\[|\\\]")
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        if forbidden.search(text):
            math_errors.append(
                f"{path.name}: forbidden non-dollar math delimiter"
            )
        if text.count("$") % 2:
            math_errors.append(
                f"{path.name}: odd dollar delimiter count"
            )

    certificate = load_json(
        ROOT / "outputs" / "interval_atomic_certificate.json"
    )
    verification = load_json(
        ROOT / "outputs" / "certificate_verification.json"
    )
    audit = load_json(
        ROOT / "outputs" / "exact_serialization_audit.json"
    )
    orientation = load_json(
        ROOT / "outputs" / "coefficient_orientation_audit.json"
    )
    stress = load_json(
        ROOT / "outputs" / "orientation_stress_test.json"
    )
    summary = load_json(
        ROOT / "outputs" / "experiment_summary.json"
    )
    semantic_checks = {
        "abstract_interval_true": certificate[
            "classification"
        ]["abstract_continuous_interval_certificate"]
        is True,
        "verification_pass": verification["verification_pass"] is True,
        "exact_audit_pass": audit["audit_pass"] is True,
        "orientation_blocker_true": orientation[
            "orientation_blocker_confirmed"
        ]
        is True,
        "stored_coefficients_not_lower_certificates": orientation[
            "all_stored_coefficients_are_lower_certificates"
        ]
        is False,
        "stress_does_not_survive": stress[
            "fixed_witness_survives_lower_profile"
        ]
        is False,
        "all_global_flags_false": all(
            item.get("global_rh_certificate") is False
            for item in (
                certificate["classification"],
                verification,
                audit,
                orientation,
                stress,
                summary,
            )
        ),
        "all_layer_b_flags_false": all(
            certificate["classification"][key] is False
            for key in (
                "zeta_facing_tail_theorem_certified",
                "zeta_facing_count_coefficients_certified",
                "explicit_formula_admissibility_certified",
            )
        ),
    }
    validation_pass = bool(
        not missing
        and not json_errors
        and not math_errors
        and all(semantic_checks.values())
    )
    report = {
        "schema": "EveMissLab.RH.ValidationReport.v0.7",
        "required_file_count": len(required),
        "json_file_count": len(json_files),
        "markdown_file_count": len(markdown_files),
        "missing_files": missing,
        "json_errors": json_errors,
        "math_delimiter_errors": math_errors,
        "semantic_checks": semantic_checks,
        "validation_pass": validation_pass,
        "abstract_continuous_interval_certificate": True,
        "global_rh_certificate": False,
    }
    (
        ROOT / "metadata" / "validation_report.json"
    ).write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, indent=2, ensure_ascii=False))
    if not validation_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

