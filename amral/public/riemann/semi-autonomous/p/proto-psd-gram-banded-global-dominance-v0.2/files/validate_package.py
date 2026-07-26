from __future__ import annotations

import compileall
import io
import json
import unittest
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parent


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def true_global_flags(value: object, path: str = "$") -> list[str]:
    found = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            if key == "global_certificate_pass" and child is True:
                found.append(child_path)
            found.extend(true_global_flags(child, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(
                true_global_flags(child, f"{path}[{index}]")
            )
    return found


def main() -> None:
    json_paths = sorted(
        path
        for parent in ("data", "outputs", "metadata")
        for path in (ROOT / parent).rglob("*.json")
    )
    parsed = {str(path.relative_to(ROOT)): read_json(path) for path in json_paths}

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

    syntax_pass = compileall.compile_dir(
        str(ROOT / "psdgram"),
        quiet=1,
    ) and all(
        compileall.compile_file(str(ROOT / name), quiet=1)
        for name in (
            "run_experiment.py",
            "refresh_audits.py",
            "build_diagnostics.py",
            "build_release.py",
            "validate_package.py",
        )
    )

    gram_results = parsed["outputs/gram_results.json"]
    diagonal_results = parsed["outputs/diagonal_results.json"]
    rank_study = parsed["outputs/rank_study.json"]
    summary = parsed["outputs/experiment_summary.json"]
    minimum_eigenvalue = min(
        float(
            np.linalg.eigvalsh(
                0.5
                * (
                    np.asarray(item["gram"], dtype=float)
                    + np.asarray(item["gram"], dtype=float).T
                )
            ).min()
        )
        for item in gram_results
    )
    global_true_paths = []
    for name, value in parsed.items():
        if name.startswith("outputs/"):
            global_true_paths.extend(
                f"{name}:{path}"
                for path in true_global_flags(value)
            )

    checks = {
        "all_json_parse": True,
        "python_syntax_pass": bool(syntax_pass),
        "unit_tests_pass": bool(test_result.wasSuccessful()),
        "gram_patch_count_is_18": len(gram_results) == 18,
        "diagonal_patch_count_is_18": len(diagonal_results) == 18,
        "rank_study_count_is_16": len(rank_study) == 16,
        "saved_grams_psd_to_tolerance": minimum_eigenvalue >= -2e-12,
        "all_refined_core_sign_pass": all(
            item["lipschitz_audit"][
                "core_refined_continuous_sign_pass"
            ]
            for item in gram_results
        ),
        "known_zero_optimization_is_false": not summary[
            "known_zero_ordinates_used_in_optimization"
        ],
        "known_zero_holdout_is_true": summary[
            "known_zero_ordinates_used_as_holdout_only"
        ],
        "no_true_global_certificate_flag_in_outputs": not global_true_paths,
    }
    report = {
        "schema": "EveMissLab.RH.ValidationReport.v0.2",
        "validated_at": "2026-07-24T00:00:00+08:00",
        "json_file_count": len(json_paths),
        "unit_test_count": test_result.testsRun,
        "unit_test_failures": len(test_result.failures),
        "unit_test_errors": len(test_result.errors),
        "minimum_saved_gram_eigenvalue": minimum_eigenvalue,
        "true_global_certificate_paths": global_true_paths,
        "checks": checks,
        "validation_pass": all(checks.values()),
        "test_log": test_stream.getvalue().splitlines(),
        "trust_level": "E2 floating numerical package validation"
    }
    write_json(ROOT / "metadata" / "validation_report.json", report)
    if not report["validation_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
