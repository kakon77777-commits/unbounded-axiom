#!/usr/bin/env python3
"""Create a deterministic final ZIP and standalone handoff artifacts."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import zipfile


PACKAGE = Path(__file__).resolve().parent
WORKSPACE = PACKAGE.parent
ZIP_PATH = WORKSPACE / f"{PACKAGE.name}.zip"
REPORT_NAME = "RH半AI自主研究完整報告_v0.1-v1.0_與後續AI交接_v1.0.md"
HANDOFF_MD_NAME = "RH_v0.1-v1.0_AI_HANDOFF_v1.0.md"
HANDOFF_JSON_NAME = "RH_v0.1-v1.0_AI_HANDOFF_v1.0.json"
CHECKSUM_NAME = f"{PACKAGE.name}_SHA256SUMS.txt"
FIXED_ZIP_TIME = (2026, 7, 25, 12, 0, 0)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def package_files() -> list[Path]:
    files = []
    for path in PACKAGE.rglob("*"):
        if not path.is_file():
            continue
        if "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        files.append(path)
    return sorted(files, key=lambda item: item.relative_to(PACKAGE).as_posix())


def build_zip() -> None:
    temporary = ZIP_PATH.with_suffix(".zip.tmp")
    if temporary.exists():
        temporary.unlink()
    with zipfile.ZipFile(
        temporary,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as zf:
        for path in package_files():
            relative = Path(PACKAGE.name) / path.relative_to(PACKAGE)
            info = zipfile.ZipInfo(relative.as_posix(), date_time=FIXED_ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o100644 & 0xFFFF) << 16
            info.create_system = 3
            zf.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED)
    temporary.replace(ZIP_PATH)


def main() -> None:
    subprocess.run(
        ["python3", "validate_release.py", "--require-sources"],
        cwd=PACKAGE,
        check=True,
    )
    build_zip()

    standalone_report = WORKSPACE / REPORT_NAME
    standalone_handoff_md = WORKSPACE / HANDOFF_MD_NAME
    standalone_handoff = WORKSPACE / HANDOFF_JSON_NAME
    shutil.copy2(PACKAGE / REPORT_NAME, standalone_report)
    shutil.copy2(PACKAGE / "AI_HANDOFF.md", standalone_handoff_md)
    shutil.copy2(PACKAGE / "metadata" / "ai-handoff.json", standalone_handoff)

    outputs = [
        ZIP_PATH,
        standalone_report,
        standalone_handoff_md,
        standalone_handoff,
    ]
    checksum_path = WORKSPACE / CHECKSUM_NAME
    checksum_path.write_text(
        "".join(f"{sha256_file(path)}  {path.name}\n" for path in outputs),
        encoding="utf-8",
    )

    print(
        json.dumps(
            {
                "status": "ok",
                "zip": ZIP_PATH.name,
                "zip_sha256": sha256_file(ZIP_PATH),
                "standalone_report": standalone_report.name,
                "standalone_handoff_md": standalone_handoff_md.name,
                "standalone_handoff_json": standalone_handoff.name,
                "checksums": checksum_path.name,
                "zip_files": len(package_files()),
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
