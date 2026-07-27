from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parent
REPORT = ROOT / "metadata" / "validation_report.json"
PAPER = (
    "占用算子族與覆蓋式Green證書_RH位置量詞語義橋精確合成模型與"
    "微半徑轉移_v0.9_半AI自主研究稿.md"
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
    "NEXT_NODE_LOCAL_INTERVAL_GREEN.md",
    "LICENSE",
    PAPER,
    "requirements.txt",
    "run_all.py",
    "run_tests.py",
    "run_semantic_bridge.py",
    "generate_cover_certificate.py",
    "verify_cover_certificate.py",
    "run_clamped_radius_certificate.py",
    "verify_clamped_radius_certificate.py",
    "run_floating_clamped_study.py",
    "run_summary.py",
    "verify_outputs.py",
    "validate_package.py",
    "build_release.py",
    "occupancy_cert/__init__.py",
    "occupancy_cert/rational_interval.py",
    "occupancy_cert/dirichlet_green.py",
    "occupancy_cert/cover.py",
    "occupancy_cert/semantics.py",
    "occupancy_cert/clamped_budget.py",
    "occupancy_cert/floating_clamped.py",
    "data/synthetic_occupancy_model.json",
    "data/parent_v0.7_rational_atomic_witness.json",
    "data/parent_v0.7_interval_atomic_certificate.json",
    "outputs/occupancy_semantic_bridge.json",
    "outputs/dirichlet_green_cover_certificate.json",
    "outputs/dirichlet_green_cover_verification.json",
    "outputs/clamped_58cell_radius_certificate.json",
    "outputs/clamped_58cell_radius_verification.json",
    "outputs/floating_clamped_location_study.json",
    "outputs/experiment_summary.json",
    "outputs/output_verification.json",
    "metadata/research_node.json",
    "metadata/claim_register.json",
    "metadata/gap_ledger.json",
    "metadata/dependency_graph.json",
    "metadata/handoff.json",
    "metadata/source_lineage.json",
    "tests/__init__.py",
    "tests/test_rational_interval.py",
    "tests/test_occupancy_cover.py",
    "tests/test_clamped_budget.py",
)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def walk_key(value: Any, key: str) -> Iterable[Any]:
    if isinstance(value, dict):
        for name, item in value.items():
            if name == key:
                yield item
            yield from walk_key(item, key)
    elif isinstance(value, list):
        for item in value:
            yield from walk_key(item, key)


def math_delimiter_audit() -> list[str]:
    failures: list[str] = []
    forbidden = ("\\(", "\\)", "\\[", "\\]")
    for path in sorted(ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for token in forbidden:
            if token in text:
                failures.append(
                    f"{path.relative_to(ROOT)} contains {token}"
                )
        in_fence = False
        prose_lines = []
        for line in text.splitlines():
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if not in_fence:
                prose_lines.append(line)
        if "\n".join(prose_lines).count("$") % 2:
            failures.append(
                f"{path.relative_to(ROOT)} has an odd dollar count"
            )
    return failures


def main() -> None:
    missing = [name for name in REQUIRED if not (ROOT / name).is_file()]
    json_paths = sorted(ROOT.rglob("*.json"))
    json_failures = []
    parsed: dict[Path, Any] = {}
    for path in json_paths:
        try:
            parsed[path] = read_json(path)
        except Exception as exc:
            json_failures.append(
                f"{path.relative_to(ROOT)}: "
                f"{type(exc).__name__}: {exc}"
            )
    verification = read_json(
        ROOT / "outputs" / "output_verification.json"
    )
    summary = read_json(ROOT / "outputs" / "experiment_summary.json")
    cover = read_json(
        ROOT / "outputs" / "dirichlet_green_cover_certificate.json"
    )
    clamped = read_json(
        ROOT / "outputs" / "clamped_58cell_radius_certificate.json"
    )
    floating = read_json(
        ROOT / "outputs" / "floating_clamped_location_study.json"
    )
    claims = read_json(ROOT / "metadata" / "claim_register.json")
    gaps = read_json(ROOT / "metadata" / "gap_ledger.json")
    graph = read_json(ROOT / "metadata" / "dependency_graph.json")
    global_values = [
        item
        for value in parsed.values()
        for item in walk_key(value, "global_rh_certificate")
    ]
    math_failures = math_delimiter_audit()
    checks = {
        "required_files_present": not missing,
        "all_json_parse": not json_failures,
        "math_delimiters_compliant": not math_failures,
        "output_verification_pass": verification[
            "verification_pass"
        ],
        "summary_pass": summary["summary_pass"],
        "exact_cover_true": cover["classification"][
            "exact_rational_cover_certificate"
        ],
        "cover_not_zeta": (
            cover["classification"][
                "zeta_facing_occupancy_certificate"
            ]
            is False
        ),
        "conditional_clamped_true": clamped["classification"][
            "conditional_abstract_operator_family_certificate"
        ],
        "clamped_not_actual_zero": (
            clamped["classification"][
                "actual_zero_occupancy_certificate"
            ]
            is False
        ),
        "floating_not_universal": (
            floating["classification"][
                "universal_location_quantifier_certified"
            ]
            is False
        ),
        "claim_register_global_false": (
            claims["global_rh_certificate"] is False
        ),
        "gap_ledger_global_false": (
            gaps["global_rh_certificate"] is False
        ),
        "dependency_graph_global_false": (
            graph["global_rh_certificate"] is False
        ),
        "all_discovered_global_flags_false": (
            bool(global_values)
            and all(value is False for value in global_values)
        ),
    }
    result = {
        "schema": "RH.Occupancy.OperatorFamilyValidation.v0.9",
        "required_file_count": len(REQUIRED),
        "json_file_count_excluding_validation_report": len(
            [
                path
                for path in json_paths
                if path != REPORT
            ]
        ),
        "missing_files": missing,
        "json_failures": json_failures,
        "math_delimiter_failures": math_failures,
        "checks": checks,
        "validation_pass": all(checks.values()),
        "global_rh_certificate": False,
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    if not result["validation_pass"]:
        raise SystemExit(json.dumps(result, indent=2, ensure_ascii=False))
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
