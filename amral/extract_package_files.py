#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract one package's human-legible files for its detail page.

Pulls the small, readable members out of a packages/*.zip — markdown docs,
CSVs, text logs, small JSON, small source files — into
public/p/<id>/files/<relative-path>, and writes a files.json index next to
them. Large data blobs (certificates, point-cloud JSON) and __pycache__ stay
zip-only; the detail page links to the full zip for those. Re-run after
re-copying an updated package, then rebuild whichever detail page uses it.

Usage: python extract_package_files.py <package-id>   (id from manifest.json,
       e.g. w17-v0.1)  — or with no args, extracts every package in the
       manifest (safe to re-run; idempotent).
"""
import json
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ziputil import decoded_infolist

ROOT = Path(__file__).resolve().parent
CASE_DIR = ROOT / "public" / "riemann"
PACKAGES = CASE_DIR / "packages"
MANIFEST = CASE_DIR / "manifest.json"
P_DIR = CASE_DIR / "p"

# extension -> max size (bytes) to treat as "legible enough to extract"
LEGIBLE = {"md": 1 << 20, "csv": 1 << 20, "txt": 1 << 20, "json": 30_000, "py": 30_000}


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
        # strip the single top-level "<PackageName>/" wrapper folder, if present
        roots = {n.split("/", 1)[0] for n, i in pairs if "/" in n}
        prefix = (list(roots)[0] + "/") if len(roots) == 1 else ""
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
    by_id = {e["id"]: e for e in manifest["origin"] + manifest["engineering"] + manifest["other"]}

    targets = sys.argv[1:] or list(by_id.keys())
    for pid in targets:
        pkg = by_id.get(pid)
        if not pkg:
            print(f"  ! unknown package id: {pid}", file=sys.stderr)
            continue
        extract_one(pkg)


if __name__ == "__main__":
    main()
