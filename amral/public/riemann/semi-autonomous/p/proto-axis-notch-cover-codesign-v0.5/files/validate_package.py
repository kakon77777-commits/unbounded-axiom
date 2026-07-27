from __future__ import annotations

import compileall
import io
import json
import re
import unittest
from pathlib import Path
from typing import Any

from verify_joint_results import verify_all


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
                "continuous_function_space_obstruction_proved",
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
        "run_peak_atlas.py",
        "run_notch_screen.py",
        "run_lift_screen.py",
        "run_lift_scaling.py",
        "run_lift_joint.py",
        "run_geometry_screen.py",
        "run_geometry_joint.py",
        "verify_joint_results.py",
        "run_summary.py",
        "validate_package.py",
        "build_release.py",
    )
    syntax_pass = compileall.compile_dir(
        str(ROOT / "notch"),
        quiet=1,
    ) and all(
        compileall.compile_file(str(ROOT / name), quiet=1)
        for name in scripts
    )

    atlas = parsed["outputs/peak_atlas.json"]
    notch = parsed["outputs/notch_screen.json"]
    lift_scaling = parsed["outputs/lift_scaling.json"]
    lift_joint = parsed["outputs/lift_joint.json"]
    geometry_screen = parsed["outputs/geometry_screen.json"]
    geometry_joint = parsed["outputs/geometry_joint.json"]
    summary = parsed["outputs/experiment_summary.json"]
    stored_verification = parsed[
        "outputs/joint_verification.json"
    ]
    recomputed_verification = verify_all()

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

    required_docs = {
        "README.md",
        "METHOD.md",
        "RESULTS.md",
        "TRUST_BOUNDARY.md",
        "REPLAY.md",
        "RESEARCH_LOG.md",
        "NEXT_NODE_PALEY_WIENER.md",
        "SOURCES.md",
        "RH軸缺口共設計的單調性障礙_子空間失效外部升維飽和與PaleyWiener轉向_v0.5_半AI自主研究稿.md",
    }
    required_metadata = {
        "research_node.json",
        "claim_register.json",
        "gap_ledger.json",
        "handoff.json",
        "source_lineage.json",
    }
    grid21 = next(
        row
        for row in lift_scaling["rows"]
        if row["lift_id"] == "grid21_p4"
    )
    best_geometry = min(
        geometry_joint["rows"],
        key=lambda row: row["joint_dual"]["alpha"],
    )
    checks = {
        "all_json_parse": True,
        "python_syntax_pass": bool(syntax_pass),
        "unit_tests_pass": bool(test_result.wasSuccessful()),
        "required_docs_present": required_docs.issubset(
            {path.name for path in markdown_paths}
        ),
        "required_metadata_present": required_metadata.issubset(
            {path.name for path in metadata.glob("*.json")}
        ),
        "dollar_math_delimiter_policy_pass": not bad_math_delimiters,
        "parent_witness_count_is_12": (
            atlas["parent_witness_count"] == 12
        ),
        "five_peak_atlas_rows": len(atlas["band_rows"]) == 5,
        "notch_row_count_is_20": len(notch["rows"]) == 20,
        "lift_scaling_row_count_is_8": (
            len(lift_scaling["rows"]) == 8
        ),
        "grid21_effective_added_dimension_is_15": (
            grid21["effective_added_dimension"] == 15
        ),
        "lift_joint_gate_remains_blocked": (
            not lift_joint["lift_family_crosses_dual_gate"]
            and all(
                row["joint_dual"]["safe_alpha"] > 1.0
                for row in lift_joint["rows"]
            )
        ),
        "geometry_configuration_count_is_27": (
            geometry_screen["row_count"] == 27
        ),
        "best_geometry_id_matches": (
            best_geometry["geometry_id"] == "d12_w2_p5"
        ),
        "geometry_joint_gate_remains_blocked": (
            not geometry_joint["any_geometry_crosses_dual_gate"]
            and best_geometry["joint_dual"]["safe_alpha"] > 1.0
        ),
        "stored_joint_reconstruction_passes": bool(
            stored_verification[
                "all_reconstructed_psd_and_block_budget"
            ]
        ),
        "recomputed_joint_reconstruction_passes": bool(
            recomputed_verification[
                "all_reconstructed_psd_and_block_budget"
            ]
        ),
        "stored_and_recomputed_joint_row_counts_match": (
            stored_verification["row_count"]
            == recomputed_verification["row_count"]
            == 4
        ),
        "joint_reconstruction_difference_below_1e_12": (
            recomputed_verification[
                "maximum_minimum_eigenvalue_abs_difference"
            ]
            < 1e-12
        ),
        "primal_search_not_started": (
            not summary["primal_search_started"]
            and all(
                not row["primal_search_started"]
                for row in lift_joint["rows"]
                + geometry_joint["rows"]
            )
        ),
        "known_zero_use_is_false": not summary[
            "known_zero_ordinates_used"
        ],
        "no_true_global_or_continuous_certificate_flag": (
            not global_true_paths
        ),
    }
    report = {
        "schema": "EveMissLab.RH.ValidationReport.v0.5",
        "validated_at": "2026-07-24T00:00:00+08:00",
        "json_file_count": len(json_paths),
        "markdown_file_count": len(markdown_paths),
        "unit_test_count": test_result.testsRun,
        "unit_test_failures": len(test_result.failures),
        "unit_test_errors": len(test_result.errors),
        "bad_math_delimiter_files": bad_math_delimiters,
        "true_global_certificate_paths": global_true_paths,
        "recomputed_joint_maximum_minimum_eigenvalue_abs_difference": (
            recomputed_verification[
                "maximum_minimum_eigenvalue_abs_difference"
            ]
        ),
        "checks": checks,
        "validation_pass": all(checks.values()),
        "test_log": test_stream.getvalue().splitlines(),
        "trust_level": (
            "E0 finite-space monotonicity and conic algebra plus E1 "
            "structure and E2 floating research validation; no E3 "
            "continuous or analytic transfer"
        ),
    }
    write_json(metadata / "validation_report.json", report)
    if not report["validation_pass"]:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
