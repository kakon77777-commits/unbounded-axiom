from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPORT = ROOT / "metadata" / "validation_report.json"
PAPER = (
    "零點計數係數語義橋_RH上包絡無效定理組態下界與連續逃逸_"
    "v0.8_半AI自主研究稿.md"
)
REQUIRED = (
    "README.md",
    "THEORY.md",
    "METHOD.md",
    "RESULTS.md",
    "TRUST_BOUNDARY.md",
    "REPLAY.md",
    "RESEARCH_LOG.md",
    "SOURCES.md",
    "CHANGELOG.md",
    "NEXT_NODE_OCCUPANCY_OPERATOR_FAMILY.md",
    "LICENSE",
    PAPER,
    "requirements.txt",
    "run_all.py",
    "run_tests.py",
    "run_semantic_bridge.py",
    "run_count_profile.py",
    "run_lineage_audit.py",
    "run_lower_profile_experiment.py",
    "run_summary.py",
    "verify_outputs.py",
    "bridge/__init__.py",
    "bridge/semantics.py",
    "bridge/axis.py",
    "bridge/cover.py",
    "bridge/galerkin.py",
    "bridge/green.py",
    "outputs/semantic_bridge.json",
    "outputs/typed_count_profile.json",
    "outputs/lineage_semantic_audit.json",
    "outputs/lower_profile_experiment.json",
    "outputs/experiment_summary.json",
    "outputs/output_verification.json",
    "metadata/research_node.json",
    "metadata/claim_register.json",
    "metadata/gap_ledger.json",
    "metadata/handoff.json",
    "metadata/source_lineage.json",
)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def math_delimiter_audit() -> list[str]:
    failures = []
    forbidden = ("\\(", "\\)", "\\[", "\\]")
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for token in forbidden:
            if token in text:
                failures.append(
                    f"{path.relative_to(ROOT)} contains {token}"
                )
    return failures


def main() -> None:
    missing = [name for name in REQUIRED if not (ROOT / name).is_file()]
    json_paths = sorted(ROOT.rglob("*.json"))
    json_failures = []
    for path in json_paths:
        try:
            read_json(path)
        except Exception as exc:
            json_failures.append(
                f"{path.relative_to(ROOT)}: {type(exc).__name__}: {exc}"
            )
    verification = read_json(
        ROOT / "outputs" / "output_verification.json"
    )
    summary = read_json(ROOT / "outputs" / "experiment_summary.json")
    lineage = read_json(
        ROOT / "outputs" / "lineage_semantic_audit.json"
    )
    claims = read_json(ROOT / "metadata" / "claim_register.json")
    checks = {
        "required_files_present": not missing,
        "all_json_parse": not json_failures,
        "math_delimiters_compliant": not math_delimiter_audit(),
        "output_verification_pass": verification[
            "verification_pass"
        ],
        "summary_pass": summary["summary_pass"],
        "semantic_theorems_exact": summary["classification"][
            "exact_semantic_theorems"
        ],
        "actual_operator_bridge_false": not summary[
            "classification"
        ]["actual_zero_side_operator_bridge"],
        "prototype_not_unresolved": not lineage[
            "target_patch_relevance"
        ]["actual_unresolved_zeta_target"],
        "claim_register_global_false": not claims[
            "global_rh_certificate"
        ],
        "all_global_flags_false": all(
            value is False
            for value in (
                verification["global_rh_certificate"],
                summary["classification"]["global_rh_certificate"],
                lineage["global_rh_certificate"],
            )
        ),
    }
    report = {
        "schema": "RH.ZeroCountSemanticsBridge.Validation.v0.8",
        "required_file_count": len(REQUIRED),
        "json_file_count": len(json_paths),
        "markdown_file_count": len(list(ROOT.rglob("*.md"))),
        "missing_files": missing,
        "json_failures": json_failures,
        "math_delimiter_failures": math_delimiter_audit(),
        "checks": checks,
        "validation_pass": all(checks.values()),
        "global_rh_certificate": False,
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    if not report["validation_pass"]:
        raise SystemExit(
            json.dumps(report, indent=2, ensure_ascii=False)
        )
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
