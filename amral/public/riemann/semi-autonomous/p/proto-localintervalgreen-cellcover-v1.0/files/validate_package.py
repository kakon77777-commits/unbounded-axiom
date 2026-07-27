from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parent
REPORT = ROOT / "metadata" / "validation_report.json"
PAPER = (
    "局部區間Green位置覆蓋_RH五十八胞算子族證書尺度提升與"
    "技術收束_v1.0_半AI自主研究稿.md"
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
    "NEXT_ROUND_FINAL_SYNTHESIS.md",
    "LICENSE",
    PAPER,
    "requirements.txt",
    "generate_cell_cover.py",
    "verify_cell_cover.py",
    "run_summary.py",
    "run_tests.py",
    "run_all.py",
    "validate_package.py",
    "build_release.py",
    "local_green/__init__.py",
    "local_green/decimal_interval.py",
    "local_green/rational_complex.py",
    "local_green/transcendental.py",
    "local_green/box_green.py",
    "local_green/box_certificate.py",
    "data/parent_v0.7_rational_atomic_witness.json",
    "data/parent_v0.7_interval_atomic_certificate.json",
    "data/parent_v0.9_clamped_radius_certificate.json",
    "data/parent_v0.9_floating_location_study.json",
    "data/adversarial_corner_witness_h1e-3.json",
    "outputs/local_green_cell_certificate_h178e-8.json",
    "outputs/local_green_cell_verification_h178e-8.json",
    "outputs/local_green_radius_ladder.json",
    "outputs/local_green_cover_family.json",
    "outputs/local_green_cover_family_verification.json",
    "outputs/adversarial_corner_point_certificate_h1e-3.json",
    "outputs/adversarial_corner_point_verification_h1e-3.json",
    "outputs/output_verification.json",
    "outputs/experiment_summary.json",
    "metadata/research_node.json",
    "metadata/claim_register.json",
    "metadata/gap_ledger.json",
    "metadata/dependency_graph.json",
    "metadata/handoff.json",
    "metadata/source_lineage.json",
    "tests/__init__.py",
    "tests/test_interval_engine.py",
    "tests/test_recorded_outputs.py",
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

    verification = read_json(OUTPUT_PATH("output_verification.json"))
    summary = read_json(OUTPUT_PATH("experiment_summary.json"))
    certificate = read_json(
        OUTPUT_PATH("local_green_cell_certificate_h178e-8.json")
    )
    ladder = read_json(
        OUTPUT_PATH("local_green_radius_ladder.json")
    )
    family = read_json(
        OUTPUT_PATH("local_green_cover_family.json")
    )
    corner = read_json(
        OUTPUT_PATH(
            "adversarial_corner_point_certificate_h1e-3.json"
        )
    )
    claims = read_json(ROOT / "metadata" / "claim_register.json")
    gaps = read_json(ROOT / "metadata" / "gap_ledger.json")
    handoff = read_json(ROOT / "metadata" / "handoff.json")
    global_values = [
        item
        for value in parsed.values()
        for item in walk_key(value, "global_rh_certificate")
    ]
    actual_zeta_values = [
        item
        for value in parsed.values()
        for item in walk_key(value, "actual_zeta_occupancy_family")
    ]
    nondeterministic_keys = [
        str(path.relative_to(ROOT))
        for path, value in parsed.items()
        if list(walk_key(value, "wall_seconds_diagnostic"))
    ]
    math_failures = math_delimiter_audit()
    rows = {row["label"]: row for row in ladder["rows"]}
    gap_map = {row["gap_id"]: row for row in gaps["gaps"]}
    checks = {
        "required_files_present": not missing,
        "all_json_parse": not json_failures,
        "math_delimiters_compliant": not math_failures,
        "deterministic_outputs": not nondeterministic_keys,
        "output_verification_pass": verification[
            "verification_pass"
        ],
        "summary_pass": summary["summary_pass"],
        "maximum_certificate_true": certificate["classification"][
            "local_58cell_interval_certificate"
        ],
        "maximum_radius_exact": (
            certificate["statement"]["axis_cell_half_width"]
            == "89/50000000"
        ),
        "maximum_determinant_positive": (
            float(certificate["proof"]["determinant_lower"]) > 0
        ),
        "cover_family_true": family["classification"][
            "abstract_local_location_cover_family"
        ],
        "boundary_failure_classified": (
            rows["first_tested_boundary_failure"]["failure_class"]
            == "sylvester_lower_bound_failure"
        ),
        "corner_point_true": corner["proof"]["certificate_pass"],
        "claim_register_global_false": (
            claims["global_rh_certificate"] is False
        ),
        "gap_ledger_global_false": (
            gaps["global_rh_certificate"] is False
        ),
        "zeta_occupancy_gap_open": (
            gap_map["G09-ZETA-OCC"]["status"] == "open"
        ),
        "explicit_formula_gap_open": (
            gap_map["G09-EF-TRANSFER"]["status"] == "open"
        ),
        "next_round_is_final_synthesis": (
            handoff["next_round"]["status"] == "scheduled"
            and "integrated" in handoff["next_round"]["deliverable"]
        ),
        "all_discovered_global_flags_false": (
            bool(global_values)
            and all(value is False for value in global_values)
        ),
        "all_discovered_actual_zeta_flags_false": (
            bool(actual_zeta_values)
            and all(value is False for value in actual_zeta_values)
        ),
    }
    result = {
        "schema": "RH.LocalIntervalGreen.PackageValidation.v1.0",
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
        "nondeterministic_json_files": nondeterministic_keys,
        "checks": checks,
        "validation_pass": all(checks.values()),
        "actual_zeta_occupancy_family": False,
        "global_rh_certificate": False,
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(
        json.dumps(
            result,
            indent=2,
            ensure_ascii=False,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    if not result["validation_pass"]:
        raise SystemExit(json.dumps(result, indent=2, ensure_ascii=False))
    print(json.dumps(result, indent=2, ensure_ascii=False))


def OUTPUT_PATH(name: str) -> Path:
    return ROOT / "outputs" / name


if __name__ == "__main__":
    main()
