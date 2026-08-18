# -*- coding: utf-8 -*-
"""One round of the "3 series at a time" attachments-pending processing Neo
asked for (2026-08-17): for each named series, extract any zips, copy every
real paper .md into ingest/01-before/ renamed to its own in-doc H1 title
(matching the established "rename file -> in-doc H1" convention), and record
non-.md files as companion candidates (to be wired to their parent paper's
lm-id AFTER Stage 1 assigns one, same as every prior companion batch --
never published as their own paper). Copies, does not move: the originals in
attachments-pending/ stay put until a human/agent confirms the batch
published cleanly, matching this pipeline's established
archive-after-not-before discipline.

Usage: python scripts/stage_attachments_batch.py "series name 1" "series name 2" ...
"""
import json
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "ingest" / "attachments-pending"
DEST = ROOT / "ingest" / "01-before"
SCRATCH_ZIP = ROOT / "ingest" / "_zip-extract-scratch"

ILLEGAL_WIN = re.compile(r'[<>"/\\|?*\x00-\x1f]')


def safe_title(title, fallback):
    t = title.strip()
    t = ILLEGAL_WIN.sub("_", t)
    t = t.rstrip(". ")
    return t if t else fallback


def extract_title(md_path):
    text = md_path.read_text(encoding="utf-8", errors="replace")
    for line in text.splitlines()[:40]:
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return None


def main(series_names):
    DEST.mkdir(parents=True, exist_ok=True)
    manifest = {"staged_papers": [], "companion_candidates": [], "skipped": []}

    for series in series_names:
        series_dir = SRC / series
        if not series_dir.is_dir():
            print(f"SKIP (not found): {series}")
            continue

        # Extract any zips into a per-series scratch dir first.
        extract_root = SCRATCH_ZIP / series
        if extract_root.exists():
            shutil.rmtree(extract_root)
        extract_root.mkdir(parents=True)

        all_files = []
        for f in series_dir.rglob("*"):
            if not f.is_file():
                continue
            if f.suffix.lower() == ".zip":
                with zipfile.ZipFile(f) as zf:
                    target = extract_root / f.stem
                    zf.extractall(target)
                    all_files.extend(p for p in target.rglob("*") if p.is_file())
            else:
                all_files.append(f)

        md_files = [f for f in all_files if f.suffix.lower() == ".md"]
        other_files = [f for f in all_files if f.suffix.lower() != ".md"]

        for md in md_files:
            title = extract_title(md)
            if not title:
                manifest["skipped"].append({"series": series, "file": md.name, "reason": "no H1 title found"})
                continue
            dest_name = safe_title(title, md.stem) + ".md"
            dest_path = DEST / dest_name
            n = 1
            while dest_path.exists():
                dest_path = DEST / f"{safe_title(title, md.stem)}-{n}.md"
                n += 1
            shutil.copy2(md, dest_path)
            manifest["staged_papers"].append({
                "series": series, "original_filename": md.name,
                "staged_as": dest_path.name, "title": title,
            })

        for other in other_files:
            manifest["companion_candidates"].append({
                "series": series, "file": other.name,
                "source_path": str(other.relative_to(extract_root)) if extract_root in other.parents else other.name,
                "likely_parent_prefix": re.match(r"^[A-Za-z0-9_]+", other.stem).group(0) if re.match(r"^[A-Za-z0-9_]+", other.stem) else None,
            })

    out = ROOT / "ingest" / "reports" / "attachments-batch-manifest.json"
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"staged {len(manifest['staged_papers'])} papers, "
          f"{len(manifest['companion_candidates'])} companion candidates, "
          f"{len(manifest['skipped'])} skipped -> {out}")


if __name__ == "__main__":
    main(sys.argv[1:])
