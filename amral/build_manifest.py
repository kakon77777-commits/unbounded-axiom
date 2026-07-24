#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AMRAL package manifest builder — Riemann Hypothesis case study.

Scans amral/public/riemann/packages/*.zip (raw research packages, dropped in
unmodified) and writes amral/public/riemann/manifest.json for the grid page.
Never touches the zip bytes: sha256 is computed over the untouched file so it
always matches whatever the package's own internal SHA256SUMS.txt (if any)
already certifies. Re-run after adding new packages, then redeploy.

One case study per public/<slug>/ subtree (currently just "riemann"); when a
second case study arrives, parameterize CASE instead of hardcoding it.
"""
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ziputil import decoded_names

ROOT = Path(__file__).resolve().parent
CASE_DIR = ROOT / "public" / "riemann"
PACKAGES = CASE_DIR / "packages"
MANIFEST = CASE_DIR / "manifest.json"
P_DIR = CASE_DIR / "p"

ORIGIN_RE = re.compile(r"^RH_AI_研究起點_v([\d.]+)(?:_(.+?))?_完整包\.zip$")
W_RE = re.compile(r"^RH_W_(\d+)_工程包_v([\d.]+)_完整包\.zip$")
CASE_RE = re.compile(r"^RH_CASE_(\d+)_(.+?)_v([\d.]+)\.zip$")
# standalone side-experiments outside the W-01..20 batch, e.g. "RH_Regional_Phase_Shaping_v0.1.zip"
PROTOTYPE_RE = re.compile(r"^RH_([A-Za-z][A-Za-z0-9]*(?:_[A-Za-z0-9]+)*)_v([\d.]+)\.zip$")
# primary doc inside a package, e.g. "01_RH-W-17_腔室感知切分與事件薄層_v0.1.md"
# or (older, simpler packages) "RH-W-01_測試函數空間固定_v0.1.md" with no "01_" prefix.
W_TITLE_RE_PREFIXED = re.compile(r"^01_RH-W-\d+_(.+?)_v[\d.]+\.md$")
W_TITLE_RE_BARE = re.compile(r"^RH-W-\d+_(.+?)_v[\d.]+\.md$")

# Lexical stamp: tag a card with whichever keyword its own title uses first.
# This quotes the package's own vocabulary rather than asserting a verdict.
STAMP_KEYWORDS = [
    ("閉合", "closed"), ("證書", "closed"),
    ("GAP", "open"), ("軟啟動", "open"), ("活化", "open"), ("切分", "open"),
]


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def latest_zip_timestamp(zf):
    """When the package was sealed: the latest internal file timestamp
    (the last file written, typically SHA256SUMS.txt or a final report)."""
    times = [i.date_time for i in zf.infolist() if i.date_time > (1980, 1, 1, 0, 0, 0)]
    if not times:
        return None
    y, mo, d, h, mi, s = max(times)
    # DOS timestamps carry no zone; cross-checked against filesystem mtime on
    # these packages, the packaging tool wrote UTC (~8h behind local Taipei time).
    return f"{y:04d}-{mo:02d}-{d:02d}T{h:02d}:{mi:02d}:{s:02d}Z"


def stamp_for(title):
    for kw, kind in STAMP_KEYWORDS:
        if kw in title:
            return {"label": kw, "kind": kind}
    return None


def find_w_title(names):
    basenames = [n.rsplit("/", 1)[-1] for n in names]
    for pattern in (W_TITLE_RE_PREFIXED, W_TITLE_RE_BARE):
        for base in basenames:
            m = pattern.match(base)
            if m:
                return m.group(1)
    return None


def build_entry(path):
    name = path.name
    size = path.stat().st_size
    sha256 = sha256_of(path)
    with zipfile.ZipFile(path) as zf:
        names = decoded_names(zf)
        file_count = sum(1 for n in names if not n.endswith("/"))
        generated_at = latest_zip_timestamp(zf)
        w_title = find_w_title(names)

    m = ORIGIN_RE.match(name)
    if m:
        version, desc = m.group(1), m.group(2)
        title = (desc or "研究起點").replace("_", " ").strip()
        entry = {
            "series": "origin", "series_label": "研究起點",
            "id": f"origin-v{version}", "number": None, "version": version,
            "title": title, "filename": name, "size": size,
            "file_count": file_count, "sha256": sha256,
            "generated_at": generated_at, "stamp": stamp_for(title),
        }
        entry["has_detail_page"] = (P_DIR / entry["id"] / "index.html").exists()
        return entry

    m = W_RE.match(name)
    if m:
        number, version = m.group(1), m.group(2)
        title = (w_title or f"W-{number}").replace("_", " ").strip()
        entry = {
            "series": "engineering", "series_label": "W 工程包",
            "id": f"w{number}-v{version}", "number": int(number), "version": version,
            "title": title, "filename": name, "size": size,
            "file_count": file_count, "sha256": sha256,
            "generated_at": generated_at, "stamp": stamp_for(title),
        }
        entry["has_detail_page"] = (P_DIR / entry["id"] / "index.html").exists()
        return entry

    m = CASE_RE.match(name)
    if m:
        case_num, desc, version = m.group(1), m.group(2), m.group(3)
        title = desc.replace("_", " ").strip()
        entry = {
            "series": "platform", "series_label": "平台匯入包",
            "id": f"case{case_num}-v{version}", "number": int(case_num), "version": version,
            "title": title, "filename": name, "size": size,
            "file_count": file_count, "sha256": sha256,
            "generated_at": generated_at, "stamp": None,
        }
        entry["has_detail_page"] = (P_DIR / entry["id"] / "index.html").exists()
        return entry

    m = PROTOTYPE_RE.match(name)
    if m:
        desc, version = m.group(1), m.group(2)
        title = desc.replace("_", " ").strip()
        entry = {
            "series": "prototype", "series_label": "側支原型",
            "id": f"proto-{desc.lower().replace('_', '-')}-v{version}", "number": None, "version": version,
            "title": title, "filename": name, "size": size,
            "file_count": file_count, "sha256": sha256,
            "generated_at": generated_at, "stamp": None,
        }
        entry["has_detail_page"] = (P_DIR / entry["id"] / "index.html").exists()
        return entry

    return {
        "series": "other", "series_label": "其他",
        "id": name, "number": None, "version": None, "title": name,
        "filename": name, "size": size, "file_count": file_count,
        "sha256": sha256, "generated_at": generated_at, "stamp": None,
        "has_detail_page": False,
    }


def main():
    entries = [build_entry(p) for p in sorted(PACKAGES.glob("*.zip"))]

    origin = sorted(
        (e for e in entries if e["series"] == "origin"),
        key=lambda e: tuple(int(x) for x in e["version"].split(".")),
    )
    engineering = sorted(
        (e for e in entries if e["series"] == "engineering"),
        key=lambda e: (e["number"], tuple(int(x) for x in e["version"].split("."))),
    )
    platform = sorted((e for e in entries if e["series"] == "platform"), key=lambda e: e["title"])
    prototype = sorted((e for e in entries if e["series"] == "prototype"), key=lambda e: e["title"])
    other = [e for e in entries if e["series"] == "other"]
    if other:
        print(f"NOTE: {len(other)} package(s) did not match a known naming pattern: "
              + ", ".join(e['filename'] for e in other))

    manifest = {
        "generated_by": "amral/build_manifest.py",
        "counts": {
            "total": len(entries), "origin": len(origin), "engineering": len(engineering),
            "platform": len(platform), "prototype": len(prototype),
        },
        "total_size": sum(e["size"] for e in entries),
        "origin": origin,
        "engineering": engineering,
        "platform": platform,
        "prototype": prototype,
        "other": other,
    }
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {MANIFEST.relative_to(ROOT.parent)} — {len(entries)} packages, "
          f"{sum(e['size'] for e in entries) / 1024:.0f} KiB")


if __name__ == "__main__":
    main()
