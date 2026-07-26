from __future__ import annotations

import compileall
import io
import json
import unittest
from pathlib import Path

from dualcert.witness import verify_rational_payload


ROOT = Path(__file__).resolve().parent


def read_json(path: Path) -> object:
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
        "run_dual_experiment.py",
        "run_sensitivity.py",
        "verify_rational_witnesses.py",
        "validate_package.py",
        "build_release.py",
    )
    syntax_pass = compileall.compile_dir(
        str(ROOT / "dualcert"),
        quiet=1,
    ) and all(
        compileall.compile_file(str(ROOT / name), quiet=1)
        for name in scripts
    )

    summary = parsed["outputs/experiment_summary.json"]
    sensitivity = parsed["outputs/sensitivity.json"]
    rational_payload = parsed["outputs/rational_model.json"]
    stored_verification = parsed[
        "outputs/rational_verification.json"
    ]
    recomputed_verification = verify_rational_payload(
        rational_payload
    )
    cover = parsed["outputs/cover_audit.json"]
    witness_paths = sorted(
        (ROOT / "outputs" / "witnesses").glob("*.witness.json")
    )

    global_true_paths: list[str] = []
    for name, value in parsed.items():
        global_true_paths.extend(
            f"{name}:{path}"
            for path in true_global_flags(value)
        )

    checks = {
        "all_json_parse": True,
        "python_syntax_pass": bool(syntax_pass),
        "unit_tests_pass": bool(test_result.wasSuccessful()),
        "cover_pass": bool(cover["cover_pass"]),
        "witness_file_count_is_18": len(witness_paths) == 18,
        "floating_witness_pass_count_is_18": (
            summary["finite_floating_pass_count"] == 18
        ),
        "dual_lower_bound_exceeds_target": (
            summary["dual_lower_bound"]
            > summary["target_budget"]
        ),
        "r3_rejection_flag_is_true": bool(
            summary[
                "current_r3_patchwise_function_class_rejected"
            ]
        ),
        "known_zero_use_is_false": not summary[
            "known_zero_ordinates_used"
        ],
        "rational_verification_recomputes_identically": (
            recomputed_verification == stored_verification
        ),
        "all_rational_witnesses_exact_positive": bool(
            recomputed_verification["all_exact_ldl_positive"]
        ),
        "primary_sensitivity_is_stable": bool(
            sensitivity["primary_witness_stable"]
        ),
        "no_true_global_certificate_flag": not global_true_paths,
    }
    report = {
        "schema": "EveMissLab.RH.ValidationReport.v0.3",
        "validated_at": "2026-07-24T00:00:00+08:00",
        "json_file_count": len(json_paths),
        "unit_test_count": test_result.testsRun,
        "unit_test_failures": len(test_result.failures),
        "unit_test_errors": len(test_result.errors),
        "witness_file_count": len(witness_paths),
        "rational_payload_sha256": recomputed_verification[
            "payload_sha256"
        ],
        "true_global_certificate_paths": global_true_paths,
        "checks": checks,
        "validation_pass": all(checks.values()),
        "test_log": test_stream.getvalue().splitlines(),
        "trust_level": (
            "E0 exact finite rational surrogate plus E2 floating "
            "research validation; no E3 analytic transfer"
        ),
    }
    write_json(metadata / "validation_report.json", report)
    if not report["validation_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
