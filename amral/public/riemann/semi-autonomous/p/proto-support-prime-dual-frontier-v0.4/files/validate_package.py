from __future__ import annotations

import compileall
import io
import json
import re
import unittest
from pathlib import Path
from typing import Any

from verify_saved_witnesses import verify_all_saved_witnesses


ROOT = Path(__file__).resolve().parent


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def true_global_flags(value: object, path: str = "$") -> list[str]:
    found: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            if key in {
                "global_certificate_pass",
                "global_rh_certificate",
            } and child is True:
                found.append(child_path)
            found.extend(true_global_flags(child, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(
                true_global_flags(child, f"{path}[{index}]")
            )
    return found


def main() -> None:
    metadata = ROOT / "metadata"
    metadata.mkdir(parents=True, exist_ok=True)
    json_paths = sorted(
        path
        for parent in ("data", "outputs", "metadata")
        for path in (ROOT / parent).rglob("*.json")
        if path.name != "validation_report.json"
    )
    parsed = {
        str(path.relative_to(ROOT)): read_json(path)
        for path in json_paths
    }

    suite = unittest.defaultTestLoader.discover(
        str(ROOT / "tests"),
        pattern="test_*.py",
        top_level_dir=str(ROOT),
    )
    test_stream = io.StringIO()
    test_result = unittest.TextTestRunner(
        stream=test_stream,
        verbosity=2,
    ).run(suite)

    scripts = (
        "run_source_profile.py",
        "run_cover_audit.py",
        "run_frontier_sweep.py",
        "run_axis_refinement.py",
        "run_joint_dual.py",
        "run_prime_cost.py",
        "run_summary.py",
        "verify_saved_witnesses.py",
        "validate_package.py",
        "build_release.py",
    )
    syntax_pass = compileall.compile_dir(
        str(ROOT / "frontier"),
        quiet=1,
    ) and all(
        compileall.compile_file(str(ROOT / name), quiet=1)
        for name in scripts
    )

    summary = parsed["outputs/experiment_summary.json"]
    uniform = parsed["outputs/uniform_frontier.json"]
    joint = parsed["outputs/joint_dual_summary.json"]
    refinement = parsed["outputs/axis_refinement.json"]
    prime = parsed["outputs/prime_cost.json"]
    source = parsed["outputs/source_profile.json"]
    cover = parsed["outputs/cover_audit.json"]
    stored_witness_verification = parsed[
        "outputs/witness_verification.json"
    ]
    recomputed_witness_verification = verify_all_saved_witnesses()

    global_true_paths: list[str] = []
    for name, value in parsed.items():
        global_true_paths.extend(
            f"{name}:{path}"
            for path in true_global_flags(value)
        )

    markdown_paths = sorted(ROOT.glob("*.md"))
    bad_math_delimiters = []
    for path in markdown_paths:
        text = path.read_text(encoding="utf-8")
        if re.search(r"\\\(|\\\)|\\\[|\\\]", text):
            bad_math_delimiters.append(path.name)

    witness_paths = sorted(
        (ROOT / "outputs" / "witnesses").glob("*.witness.json")
    )
    required_docs = {
        "README.md",
        "METHOD.md",
        "RESULTS.md",
        "TRUST_BOUNDARY.md",
        "REPLAY.md",
        "RESEARCH_LOG.md",
        "NEXT_NODE_AXIS_NOTCH_CODESIGN.md",
        "SOURCES.md",
        "RH支撐質數對偶前沿_軸網格假逃逸與頻譜缺口轉向_v0.4_半AI自主研究稿.md",
    }
    r10 = next(
        row
        for row in prime["benchmark_rows"]
        if row["radius"] == 10.25
    )
    checks = {
        "all_json_parse": True,
        "python_syntax_pass": bool(syntax_pass),
        "unit_tests_pass": bool(test_result.wasSuccessful()),
        "required_docs_present": required_docs.issubset(
            {path.name for path in markdown_paths}
        ),
        "dollar_math_delimiter_policy_pass": not bad_math_delimiters,
        "original_cover_pass": bool(
            cover["original_cover"]["cover_pass"]
        ),
        "refined_cover_pass": bool(
            cover["refined_cover"]["cover_pass"]
        ),
        "uniform_configuration_count_is_126": (
            uniform["row_count"] == 126
        ),
        "joint_radius_count_is_4": (
            len(joint["radius_rows"]) == 4
        ),
        "all_sampled_radii_have_a_dual_block": bool(
            summary[
                "all_sampled_support_only_radii_have_a_dual_block"
            ]
        ),
        "coarse_axis_false_escape_reproduced": bool(
            refinement["coarse_grid_false_escape"]
        ),
        "witness_file_count_is_12": len(witness_paths) == 12,
        "witness_path_sets_match": bool(
            recomputed_witness_verification["path_sets_match"]
        ),
        "all_witnesses_reconstruct_psd": bool(
            recomputed_witness_verification[
                "all_serialized_sparse_witnesses_psd"
            ]
        ),
        "all_witnesses_block_budget": bool(
            recomputed_witness_verification[
                "all_serialized_measures_block_budget"
            ]
        ),
        "stored_and_recomputed_witness_counts_match": (
            stored_witness_verification["actual_witness_count"]
            == recomputed_witness_verification[
                "actual_witness_count"
            ]
            == 12
        ),
        "r10_25_actual_prime_count_matches": (
            r10["prime_count"] == 41141456
            and r10["prime_power_term_count"] == 41144807
        ),
        "published_source_constants_match": (
            source["published_s_bound"]["log_coefficient"]
            == 0.112
            and source["published_s_bound"][
                "loglog_coefficient"
            ]
            == 0.278
            and source["published_s_bound"]["constant"] == 2.51
        ),
        "full_cover_exhaustion_flag_remains_false": not joint[
            "full_refined_cover_joint_gate_exhausted"
        ],
        "known_zero_use_is_false": not summary[
            "known_zero_ordinates_used"
        ],
        "no_true_global_certificate_flag": not global_true_paths,
    }
    report = {
        "schema": "EveMissLab.RH.ValidationReport.v0.4",
        "validated_at": "2026-07-24T00:00:00+08:00",
        "json_file_count": len(json_paths),
        "markdown_file_count": len(markdown_paths),
        "unit_test_count": test_result.testsRun,
        "unit_test_failures": len(test_result.failures),
        "unit_test_errors": len(test_result.errors),
        "witness_file_count": len(witness_paths),
        "bad_math_delimiter_files": bad_math_delimiters,
        "true_global_certificate_paths": global_true_paths,
        "recomputed_witness_maximum_minimum_eigenvalue_abs_difference": (
            recomputed_witness_verification[
                "maximum_minimum_eigenvalue_abs_difference"
            ]
        ),
        "checks": checks,
        "validation_pass": all(checks.values()),
        "test_log": test_stream.getvalue().splitlines(),
        "trust_level": (
            "E0 finite conic/support algebra plus E1 structure and "
            "E2 floating research validation; no E3 analytic transfer"
        ),
    }
    write_json(metadata / "validation_report.json", report)
    if not report["validation_pass"]:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
