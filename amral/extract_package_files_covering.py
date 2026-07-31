#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract one package's human-legible files for its detail page.

PROGRAM-UNIVERSAL-COVERING counterpart of extract_package_files.py — same
extraction rules and wrapper-folder-stripping fix, pointed at
public/<case>/packages/ instead of public/riemann/<track>/packages/, and
reading the single-list "rounds" manifest schema instead of the four-bucket
Riemann one.

Usage: python extract_package_files_covering.py --case moser|skew-field [round-id ...]
       (id from manifest.json, e.g. round-v0.15) — omit ids to extract every
       package for that case's manifest (safe to re-run; idempotent).
"""
import argparse
import json
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ziputil import decoded_infolist

ROOT = Path(__file__).resolve().parent

CASE_DIRS = {"moser": "moser", "skew-field": "skew-field"}

_parser = argparse.ArgumentParser()
_parser.add_argument("--case", required=True, choices=list(CASE_DIRS))
_parser.add_argument("package_ids", nargs="*")
_cli = _parser.parse_args()

CASE_DIR = ROOT / "public" / CASE_DIRS[_cli.case]
PACKAGES = CASE_DIR / "packages"
MANIFEST = CASE_DIR / "manifest.json"
P_DIR = CASE_DIR / "p"

LEGIBLE = {"md": 1 << 20, "csv": 1 << 20, "txt": 1 << 20, "json": 30_000, "py": 30_000,
           "png": 1 << 20, "jpg": 1 << 20, "jpeg": 1 << 20, "svg": 1 << 20}


def should_extract(name, size):
    if "__pycache__" in name or name.endswith("/"):
        return False
    ext = name.rsplit(".", 1)[-1].lower() if "." in name else ""
    limit = LEGIBLE.get(ext)
    return limit is not None and size <= limit


def extract_one(pkg):
    zpath = PACKAGES / pkg["filename"]
    out_dir = P_DIR / pkg["id"] / "files"
    out_dir.mkdir(parents=True, exist_ok=True)
    index = []
    with zipfile.ZipFile(zpath) as zf:
        pairs = decoded_infolist(zf)
        has_unnested = any("/" not in n for n, i in pairs if not i.is_dir())
        roots = {n.split("/", 1)[0] for n, i in pairs if "/" in n}
        prefix = (list(roots)[0] + "/") if len(roots) == 1 and not has_unnested else ""
        for name, info in pairs:
            if info.is_dir():
                continue
            rel = name[len(prefix):] if name.startswith(prefix) else name
            if not rel or not should_extract(rel, info.file_size):
                continue
            dest = out_dir / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(zf.read(info))
            index.append({"path": rel, "size": info.file_size})
    index.sort(key=lambda e: e["path"])
    (P_DIR / pkg["id"] / "files.json").write_text(
        json.dumps({"package_id": pkg["id"], "filename": pkg["filename"], "files": index},
                    ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"  {pkg['id']}: extracted {len(index)} files")


def main():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    by_id = {e["id"]: e for e in manifest.get("rounds", [])}

    targets = _cli.package_ids or list(by_id.keys())
    for pid in targets:
        pkg = by_id.get(pid)
        if not pkg:
            print(f"  ! unknown package id: {pid}", file=sys.stderr)
            continue
        extract_one(pkg)


if __name__ == "__main__":
    main()
