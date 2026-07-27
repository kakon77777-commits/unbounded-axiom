#!/usr/bin/env python3
"""Validate the final synthesis package without rerunning costly optimizers."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
import zipfile

import build_release


PACKAGE = Path(__file__).resolve().parent
WORKSPACE = PACKAGE.parent
MANIFEST = PACKAGE / "MANIFEST.sha256"
VALIDATION_REPORT = PACKAGE / "validation" / "final-validation.json"

MANIFEST_EXCLUSIONS = {
    "MANIFEST.sha256",
    "validation/final-validation.json",
}

REQUIRED_FILES = [
    "README.md",
    "RH半AI自主研究完整報告_v0.1-v1.0_與後續AI交接_v1.0.md",
    "AI_HANDOFF.md",
    "TRUST_BOUNDARY.md",
    "REPLAY.md",
    "build_release.py",
    "validate_release.py",
    "metadata/case-manifest.json",
    "metadata/timeline.json",
    "metadata/dependency-graph.json",
    "metadata/claim-register.json",
    "metadata/gap-ledger.json",
    "metadata/failure-correction-map.json",
    "metadata/artifact-index.json",
    "metadata/source-corpus.json",
    "metadata/ai-handoff.json",
    "validation/source-archive-audit.json",
    "validation/evidence-snapshot-index.json",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_json(relative: str) -> object:
    with (PACKAGE / relative).open("r", encoding="utf-8") as fh:
        return json.load(fh)


def release_files() -> list[Path]:
    files = []
    for path in PACKAGE.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(PACKAGE).as_posix()
        if relative in MANIFEST_EXCLUSIONS:
            continue
        if "__pycache__" in path.parts or relative.endswith(".pyc"):
            continue
        files.append(path)
    return sorted(files, key=lambda item: item.relative_to(PACKAGE).as_posix())


def write_manifest() -> None:
    lines = [
        f"{sha256_file(path)}  {path.relative_to(PACKAGE).as_posix()}"
        for path in release_files()
    ]
    MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")


def read_manifest() -> dict[str, str]:
    records: dict[str, str] = {}
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, relative = line.split(maxsplit=1)
        records[relative.lstrip(" *")] = digest
    return records


def check_markdown_math(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    failures = []
    if "\\(" in text or "\\)" in text or "\\[" in text or "\\]" in text:
        failures.append("uses non-dollar LaTeX delimiters")
    if text.count("$") % 2:
        failures.append("has an odd total dollar-delimiter count")
    return failures


def validate(require_sources: bool = False) -> dict:
    checks = []

    def record(check_id: str, passed: bool, detail: object) -> None:
        checks.append({"check_id": check_id, "passed": bool(passed), "detail": detail})

    missing = [name for name in REQUIRED_FILES if not (PACKAGE / name).is_file()]
    record("required_files", not missing, {"missing": missing})

    json_failures = []
    for path in sorted(PACKAGE.rglob("*.json")):
        if path == VALIDATION_REPORT:
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:  # pragma: no cover - diagnostic path
            json_failures.append(
                {
                    "path": path.relative_to(PACKAGE).as_posix(),
                    "error": str(exc),
                }
            )
    record("json_parse", not json_failures, {"failures": json_failures})

    artifact_index = load_json("metadata/artifact-index.json")
    archive_failures = []
    archive_sources_present = 0
    recorded_archive_audit = load_json("validation/source-archive-audit.json")
    for expected in artifact_index["canonical_source_archives"]:
        archive = WORKSPACE / expected["filename"]
        if not archive.is_file():
            if require_sources:
                archive_failures.append(
                    {"archive": expected["filename"], "error": "missing"}
                )
            continue
        archive_sources_present += 1
        actual_hash = sha256_file(archive)
        audit = build_release.audit_archive(archive)
        if actual_hash != expected["sha256"]:
            archive_failures.append(
                {
                    "archive": archive.name,
                    "error": "sha256_mismatch",
                    "expected": expected["sha256"],
                    "actual": actual_hash,
                }
            )
        if not audit["zip_crc_test"] or not audit["manifest_pass"]:
            archive_failures.append(
                {
                    "archive": archive.name,
                    "error": "archive_audit_failed",
                    "audit": audit,
                }
            )
    record(
        "canonical_archives",
        not archive_failures
        and len(artifact_index["canonical_source_archives"]) == 10
        and (
            archive_sources_present == 10
            or (
                not require_sources
                and recorded_archive_audit["all_zip_crc_pass"] is True
                and recorded_archive_audit["all_internal_manifests_pass"] is True
                and recorded_archive_audit["archive_count"] == 10
            )
        ),
        {
            "mode": (
                "live_source_reaudit"
                if archive_sources_present == 10
                else "recorded_canonical_audit"
            ),
            "require_sources": require_sources,
            "sources_present": archive_sources_present,
            "archive_count": len(artifact_index["canonical_source_archives"]),
            "failures": archive_failures,
        },
    )

    snapshot_index = load_json("validation/evidence-snapshot-index.json")
    snapshot_failures = []
    archive_handles: dict[str, zipfile.ZipFile] = {}
    try:
        for item in snapshot_index["records"]:
            snapshot = PACKAGE / item["snapshot_path"]
            if not snapshot.is_file():
                snapshot_failures.append(
                    {"path": item["snapshot_path"], "error": "missing"}
                )
                continue
            snapshot_hash = sha256_file(snapshot)
            if snapshot_hash != item["sha256"]:
                snapshot_failures.append(
                    {
                        "path": item["snapshot_path"],
                        "error": "snapshot_hash_mismatch",
                    }
                )
                continue
            archive_name = item["source_archive"]
            archive_path = WORKSPACE / archive_name
            if archive_path.is_file():
                if archive_name not in archive_handles:
                    archive_handles[archive_name] = zipfile.ZipFile(archive_path)
                source_bytes = archive_handles[archive_name].read(
                    item["source_member"]
                )
                if hashlib.sha256(source_bytes).hexdigest() != item["sha256"]:
                    snapshot_failures.append(
                        {
                            "path": item["snapshot_path"],
                            "error": "canonical_member_hash_mismatch",
                        }
                    )
            elif require_sources:
                snapshot_failures.append(
                    {
                        "path": item["snapshot_path"],
                        "error": "canonical_source_archive_missing",
                    }
                )
    finally:
        for handle in archive_handles.values():
            handle.close()
    record(
        "canonical_snapshots",
        not snapshot_failures and len(snapshot_index["records"]) == 82,
        {
            "snapshot_count": len(snapshot_index["records"]),
            "failures": snapshot_failures,
        },
    )

    source_corpus = load_json("metadata/source-corpus.json")
    source_failures = []
    source_files_present = 0
    for item in source_corpus["items"]:
        path = WORKSPACE / item["path"]
        if not path.is_file():
            if require_sources:
                source_failures.append({"path": item["path"], "error": "missing"})
        else:
            source_files_present += 1
        if path.is_file() and sha256_file(path) != item["sha256"]:
            source_failures.append(
                {"path": item["path"], "error": "sha256_mismatch"}
            )
    record(
        "prehistory_sources",
        not source_failures
        and len(source_corpus["items"]) == 13
        and (source_files_present == 13 or not require_sources),
        {
            "mode": (
                "live_source_reaudit"
                if source_files_present == 13
                else "indexed_source_hashes"
            ),
            "require_sources": require_sources,
            "sources_present": source_files_present,
            "source_count": len(source_corpus["items"]),
            "failures": source_failures,
        },
    )

    handoff = load_json("metadata/ai-handoff.json")
    case_manifest = load_json("metadata/case-manifest.json")
    expected_flags = {
        "rh_proved": False,
        "rh_disproved": False,
        "actual_zeta_occupancy_family": False,
        "zeta_facing_count_and_tail_coefficients_certified": False,
        "explicit_formula_transfer_certified": False,
        "global_rh_certificate": False,
        "v0_7_abstract_continuous_interval_certificate": True,
        "v1_0_abstract_58_location_cover_certificate": True,
    }
    flag_failures = []
    for key, value in expected_flags.items():
        if handoff["hard_flags"].get(key) is not value:
            flag_failures.append(
                {
                    "source": "metadata/ai-handoff.json",
                    "flag": key,
                    "expected": value,
                    "actual": handoff["hard_flags"].get(key),
                }
            )
        if case_manifest["hard_flags"].get(key) is not value:
            flag_failures.append(
                {
                    "source": "metadata/case-manifest.json",
                    "flag": key,
                    "expected": value,
                    "actual": case_manifest["hard_flags"].get(key),
                }
            )
    record("hard_flags", not flag_failures, {"failures": flag_failures})

    timeline = load_json("metadata/timeline.json")
    sequence = [node["sequence"] for node in timeline["nodes"]]
    versions = [node["version"] for node in timeline["nodes"]]
    timeline_ok = (
        sequence == list(range(1, 11))
        and versions
        == ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0"]
        and all(node["global_rh_certificate"] is False for node in timeline["nodes"])
    )
    record(
        "timeline",
        timeline_ok,
        {"sequences": sequence, "versions": versions},
    )

    claim_register = load_json("metadata/claim-register.json")
    gap_ledger = load_json("metadata/gap-ledger.json")
    semantic_ok = (
        claim_register["global_rh_certificate"] is False
        and gap_ledger["actual_zeta_occupancy_family"] is False
        and gap_ledger["explicit_formula_transfer_certified"] is False
        and gap_ledger["global_rh_certificate"] is False
        and any(
            claim["claim_id"] == "SYN-C18"
            and claim["status"] == "explicit_nonclaim"
            for claim in claim_register["claims"]
        )
    )
    record(
        "claim_gap_semantics",
        semantic_ok,
        {
            "claim_count": len(claim_register["claims"]),
            "open_blocking_gap_count": len(gap_ledger["open_blocking"]),
        },
    )

    markdown_failures = []
    for path in sorted(PACKAGE.glob("*.md")):
        failures = check_markdown_math(path)
        if failures:
            markdown_failures.append(
                {
                    "path": path.relative_to(PACKAGE).as_posix(),
                    "failures": failures,
                }
            )
    record("markdown_math_delimiters", not markdown_failures, markdown_failures)

    report_text = (
        PACKAGE
        / "RH半AI自主研究完整報告_v0.1-v1.0_與後續AI交接_v1.0.md"
    ).read_text(encoding="utf-8")
    required_phrases = [
        "本研究沒有證明或反證黎曼猜想",
        "`actual_zeta_occupancy_family` | `false`",
        "`explicit_formula_transfer_certified` | `false`",
        "`global_rh_certificate` | `false`",
        "1.78\\times10^{-6}",
        "RH-ConditionalOffAxisCell-ZetaTransfer-2026Q3-v1.1",
    ]
    missing_phrases = [
        phrase for phrase in required_phrases if phrase not in report_text
    ]
    record("report_trust_markers", not missing_phrases, {"missing": missing_phrases})

    if not MANIFEST.is_file():
        record("release_manifest", False, {"error": "MANIFEST.sha256 missing"})
    else:
        expected_manifest = read_manifest()
        current_files = {
            path.relative_to(PACKAGE).as_posix(): sha256_file(path)
            for path in release_files()
        }
        missing_entries = sorted(set(current_files) - set(expected_manifest))
        extra_entries = sorted(set(expected_manifest) - set(current_files))
        mismatches = sorted(
            relative
            for relative in set(current_files) & set(expected_manifest)
            if current_files[relative] != expected_manifest[relative]
        )
        record(
            "release_manifest",
            not missing_entries and not extra_entries and not mismatches,
            {
                "entry_count": len(expected_manifest),
                "missing_entries": missing_entries,
                "extra_entries": extra_entries,
                "hash_mismatches": mismatches,
            },
        )

    passed = all(check["passed"] for check in checks)
    return {
        "schema": "RH.FinalSynthesisValidation.v1.0",
        "status": "PASS" if passed else "FAIL",
        "check_count": len(checks),
        "passed_count": sum(1 for check in checks if check["passed"]),
        "failed_count": sum(1 for check in checks if not check["passed"]),
        "checks": checks,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write-manifest",
        action="store_true",
        help="Regenerate MANIFEST.sha256 before validating.",
    )
    parser.add_argument(
        "--require-sources",
        action="store_true",
        help="Require all ten canonical ZIPs and thirteen prehistory sources beside the package.",
    )
    args = parser.parse_args()
    if args.write_manifest:
        write_manifest()
    report = validate(require_sources=args.require_sources)
    VALIDATION_REPORT.parent.mkdir(parents=True, exist_ok=True)
    VALIDATION_REPORT.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "status": report["status"],
                "checks": report["check_count"],
                "passed": report["passed_count"],
                "failed": report["failed_count"],
            },
            ensure_ascii=False,
        )
    )
    if report["status"] != "PASS":
        for check in report["checks"]:
            if not check["passed"]:
                print(
                    json.dumps(check, ensure_ascii=False, sort_keys=True),
                    file=sys.stderr,
                )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
