#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AMRAL package manifest builder — PROGRAM-UNIVERSAL-COVERING case studies.

Scans amral/public/<case>/packages/*.zip and writes .../manifest.json for
that case study's grid page. Never touches the zip bytes: sha256 is computed
over the untouched file. Re-run after adding new packages, then redeploy.

Unlike the Riemann case study, each of these case studies is a single flat
version sequence ("rounds") with no origin/engineering/platform split, so
the manifest has one list instead of four. The round title is not encoded
in any internal filename — every package's README.md carries a one-line
round summary as the first paragraph after its H1, so that's what's used
verbatim (quoting the package's own vocabulary, same principle as the
Riemann builder's stamp_for()).

Usage: python build_manifest_covering.py --case moser|skew-field
"""
import argparse
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ziputil import decoded_infolist

ROOT = Path(__file__).resolve().parent

CASES = {
    "moser": {
        "dir": "moser",
        "re": re.compile(r"^Moser_Skew_Lab_v([\d.]+)\.zip$"),
    },
    "skew-field": {
        "dir": "skew-field",
        "re": re.compile(r"^CenterGenerated_Bridge_Experiment_v([\d.]+)\.zip$"),
    },
}

_parser = argparse.ArgumentParser()
_parser.add_argument("--case", required=True, choices=list(CASES))
_cli = _parser.parse_args()
CASE = CASES[_cli.case]

CASE_DIR = ROOT / "public" / CASE["dir"]
PACKAGES = CASE_DIR / "packages"
MANIFEST = CASE_DIR / "manifest.json"
P_DIR = CASE_DIR / "p"

H1_RE = re.compile(r"^#\s+.+$")


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def latest_zip_timestamp(zf):
    times = [i.date_time for i in zf.infolist() if i.date_time > (1980, 1, 1, 0, 0, 0)]
    if not times:
        return None
    y, mo, d, h, mi, s = max(times)
    return f"{y:04d}-{mo:02d}-{d:02d}T{h:02d}:{mi:02d}:{s:02d}Z"


def find_round_title(zf, pairs):
    """First non-blank line(s) after the README.md's H1 heading, trimmed to
    something card-sized. Prefers the shallowest README.md (the package's
    own, not a nested/archived copy).

    Two README shapes show up across these packages: a self-contained
    one-line round summary ("半自主研究第 1 輪封裝。"), or a short colon-
    terminated heading introducing a bullet list ("第 2 輪核心結果：" then
    "- 術語更正：..."). The heading alone isn't descriptive, so when it's
    short and colon-terminated, the first bullet is used instead."""
    top = [(n, i) for n, i in pairs if n.rsplit("/", 1)[-1] == "README.md"]
    top.sort(key=lambda ni: ni[0].count("/"))
    if not top:
        return None
    name, info = top[0]
    text = zf.read(info).decode("utf-8", errors="replace")
    lines = [ln.strip() for ln in text.splitlines()]
    saw_h1 = False
    candidates = []
    for ln in lines:
        if not saw_h1:
            if H1_RE.match(ln):
                saw_h1 = True
            continue
        if ln:
            candidates.append(ln)
        if len(candidates) >= 2:
            break
    if not candidates:
        return None
    line = candidates[0]
    if (line.endswith(("：", ":")) and len(line) <= 20 and len(candidates) > 1):
        line = candidates[1]
    line = re.sub(r"^[-*]\s*", "", line)
    line = line.strip("。：:；;")
    if len(line) > 40:
        m = re.search(r"[。；;,，]", line[10:])
        line = line[:10 + m.start()] if m else line[:40].rstrip() + "…"
    return line


def build_entry(path):
    name = path.name
    size = path.stat().st_size
    sha256 = sha256_of(path)
    m = CASE["re"].match(name)
    if not m:
        return {
            "id": name, "version": None, "title": name, "filename": name,
            "size": size, "file_count": 0, "sha256": sha256,
            "generated_at": None, "has_detail_page": False, "unmatched": True,
        }
    version = m.group(1)
    with zipfile.ZipFile(path) as zf:
        pairs = decoded_infolist(zf)
        file_count = sum(1 for n, i in pairs if not i.is_dir())
        generated_at = latest_zip_timestamp(zf)
        title = find_round_title(zf, pairs) or f"v{version}"
    entry = {
        "id": f"round-v{version}", "version": version, "title": title,
        "filename": name, "size": size, "file_count": file_count,
        "sha256": sha256, "generated_at": generated_at,
    }
    entry["has_detail_page"] = (P_DIR / entry["id"] / "index.html").exists()
    return entry


def main():
    entries = [build_entry(p) for p in sorted(PACKAGES.glob("*.zip"))]
    unmatched = [e for e in entries if e.get("unmatched")]
    if unmatched:
        print(f"NOTE: {len(unmatched)} package(s) did not match the expected naming pattern: "
              + ", ".join(e["filename"] for e in unmatched))
    rounds = sorted(
        (e for e in entries if not e.get("unmatched")),
        key=lambda e: tuple(int(x) for x in e["version"].split(".")),
    )

    manifest = {
        "generated_by": "amral/build_manifest_covering.py",
        "case": _cli.case,
        "counts": {"total": len(rounds)},
        "total_size": sum(e["size"] for e in rounds),
        "rounds": rounds,
        "other": unmatched,
    }
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {MANIFEST.relative_to(ROOT.parent)} — {len(rounds)} packages, "
          f"{sum(e['size'] for e in rounds) / 1024:.0f} KiB")


if __name__ == "__main__":
    main()
