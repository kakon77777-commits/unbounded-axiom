from __future__ import annotations

import compileall
import io
import json
import re
import unittest
from pathlib import Path
from typing import Any

from verify_outputs import verify


ROOT = Path(__file__).resolve().parent


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def true_forbidden_flags(
    value: object,
    path: str = "$",
) -> list[str]:
    found: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            if key in {
                "global_certificate_pass",
                "global_rh_certificate",
                "interval_certified",
            } and child is True:
                found.append(child_path)
            found.extend(
                true_forbidden_flags(child, child_path)
            )
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(
                true_forbidden_flags(
                    child,
                    f"{path}[{index}]",
                )
            )
    return found


def main() -> None:
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
    stream = io.StringIO()
    test_result = unittest.TextTestRunner(
        stream=stream,
        verbosity=2,
    ).run(suite)
    scripts = (
        "run_green_rank_two.py",
        "run_quadrature_audit.py",
        "run_galerkin_convergence.py",
        "run_atomic_transfer.py",
        "run_certificate_budget.py",
        "run_rational_witness.py",
        "run_summary.py",
        "verify_outputs.py",
        "validate_package.py",
        "build_release.py",
    )
    syntax_pass = compileall.compile_dir(
        str(ROOT / "pwext"),
        quiet=1,
    ) and all(
        compileall.compile_file(str(ROOT / name), quiet=1)
        for name in scripts
    )
    markdown_paths = sorted(ROOT.glob("*.md"))
    bad_math_delimiters = []
    for path in markdown_paths:
        text = path.read_text(encoding="utf-8")
        if re.search(r"\\\(|\\\)|\\\[|\\\]", text):
            bad_math_delimiters.append(path.name)
    required_docs = {
        "README.md",
        "THEORY.md",
        "METHOD.md",
        "RESULTS.md",
        "TRUST_BOUNDARY.md",
        "REPLAY.md",
        "RESEARCH_LOG.md",
        "NEXT_NODE_INTERVAL_GREEN.md",
        "SOURCES.md",
        "PaleyWiener軸核極值_RH連續核對偶原子障礙與二階Schur證書化_v0.6_半AI自主研究稿.md",
    }
    required_metadata = {
        "research_node.json",
        "claim_register.json",
        "gap_ledger.json",
        "handoff.json",
        "source_lineage.json",
    }
    forbidden_true_paths: list[str] = []
    for name, value in parsed.items():
        forbidden_true_paths.extend(
            f"{name}:{path}"
            for path in true_forbidden_flags(value)
        )
    convergence = parsed[
        "outputs/galerkin_joint_convergence.json"
    ]
    transfer = parsed["outputs/atomic_transfer.json"]
    rational = parsed[
        "outputs/rational_atomic_witness.json"
    ]
    summary = parsed["outputs/experiment_summary.json"]
    recomputed = verify()
    checks = {
        "all_json_parse": True,
        "python_syntax_pass": bool(syntax_pass),
        "unit_tests_pass": bool(test_result.wasSuccessful()),
        "required_docs_present": required_docs.issubset(
            {path.name for path in markdown_paths}
        ),
        "required_metadata_present": required_metadata.issubset(
            {
                path.name
                for path in (ROOT / "metadata").glob("*.json")
            }
        ),
        "dollar_math_delimiter_policy_pass": not bad_math_delimiters,
        "galerkin_level_count_is_10": (
            len(convergence["rows"]) == 10
        ),
        "galerkin_sequence_monotone": bool(
            convergence["monotone_raw_alpha_nonincreasing"]
        ),
        "continuous_kernel_floating_obstruction_pass": bool(
            transfer["continuous_kernel_floating_obstruction"]
        ),
        "rational_atom_counts_match": (
            sum(
                len(group)
                for group in rational["axis_supports"]
            )
            == 58
            and len(rational["core_support"]) == 2
        ),
        "rational_floating_pass": bool(
            rational["rationalized_floating_pass"]
        ),
        "recomputed_output_verification_pass": bool(
            recomputed["verification_pass"]
        ),
        "next_node_matches": (
            summary["next_node"]
            == "RH-IntervalGreenKernel-AtomicCertificate-20260725-v0.7"
        ),
        "known_zero_use_is_false": not summary[
            "known_zero_ordinates_used"
        ],
        "no_true_global_or_interval_flags": (
            not forbidden_true_paths
        ),
    }
    report = {
        "schema": "EveMissLab.RH.ValidationReport.v0.6",
        "validated_at": "2026-07-25T00:00:00+08:00",
        "json_file_count": len(json_paths),
        "markdown_file_count": len(markdown_paths),
        "unit_test_count": test_result.testsRun,
        "unit_test_failures": len(test_result.failures),
        "unit_test_errors": len(test_result.errors),
        "bad_math_delimiter_files": bad_math_delimiters,
        "forbidden_true_flag_paths": forbidden_true_paths,
        "checks": checks,
        "validation_pass": all(checks.values()),
        "test_log": stream.getvalue().splitlines(),
        "trust_level": (
            "E0 continuous Hilbert/operator reductions, E1 "
            "rational serialization, and E2 floating Green-kernel "
            "validation; no E3 interval or zeta transfer"
        ),
    }
    write_json(
        ROOT / "metadata" / "validation_report.json",
        report,
    )
    if not report["validation_pass"]:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
