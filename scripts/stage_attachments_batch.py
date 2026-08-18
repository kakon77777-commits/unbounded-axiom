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

ILLEGAL_WIN = re.compile(r'[<>"/|?*\x00-\x1f]')


def safe_title(title, fallback):
    """Titles sometimes carry inline LaTeX (e.g. "$O\\sim\\Omega$") -- drop
    backslashes outright rather than replacing them with the generic
    illegal-character underscore, or "$O\\sim\\Omega$" becomes the
    confusing "$O_sim_Omega$" instead of the intended "$OsimΩ$"-ish
    plain-text rendering. Backslash carries no meaning of its own in a
    plain filename, unlike the other illegal characters below."""
    t = title.strip()
    t = t.replace("\\", "")
    t = ILLEGAL_WIN.sub("_", t)
    t = t.rstrip(". ")
    return t if t else fallback


def _strip_frontmatter(lines):
    """Some source packages carry a long YAML frontmatter block (dozens of
    lines of internal_artifacts/canonical_keywords/etc.) before the real H1
    -- a fixed line-count scan window can run out before ever reaching it.
    Skip a leading '---' ... '---' block entirely so the H1 scan always
    starts counting from the real body."""
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return lines[i + 1:]
    return lines


def extract_title(md_path):
    """Some source packages open with a generic "<series> Paper NN"-style H1
    immediately followed by the paper's real descriptive H1 (blank lines
    allowed between them, no other content) -- e.g. "# XYZ Series Paper 01"
    then "# 造物之後：為什麼要創造一個世界？". Prefer the LAST H1 in that
    leading run, since it's consistently the real title; a normal single-H1
    file is unaffected (falls through to the same H1 either way)."""
    text = md_path.read_text(encoding="utf-8", errors="replace")
    body_lines = _strip_frontmatter(text.splitlines())
    last_leading_h1 = None
    for line in body_lines[:40]:
        line = line.strip()
        if line.startswith("# "):
            last_leading_h1 = line[2:].strip()
            continue
        if line == "":
            continue
        break  # first non-blank, non-H1 line ends the leading run
    if last_leading_h1:
        return last_leading_h1
    # Fallback: no leading run (H1 appears deeper in the file) -- first H1 anywhere.
    for line in body_lines[:40]:
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
            # A same-named file already staged with byte-identical content is
            # this exact source being re-copied (e.g. the script re-run after
            # an earlier partial batch) -- overwrite in place rather than
            # minting a "-1" duplicate. Only genuinely different content
            # collides and gets a numbered suffix.
            if dest_path.exists() and dest_path.read_bytes() == md.read_bytes():
                shutil.copy2(md, dest_path)
                manifest["staged_papers"].append({
                    "series": series, "original_filename": md.name,
                    "staged_as": dest_path.name, "title": title,
                })
                continue
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
