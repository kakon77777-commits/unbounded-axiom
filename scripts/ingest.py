#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""§25 three-stage ingest — STAGE 1.

Analyze ingest/01-before (or --source) into ingest/02-agent-staging and copy
non-blocked files to ingest/03-after (organized by inferred YYYY/YYYY-MM). NEVER
writes to content/papers/ or the registry — only publish_ingested.py may promote
to canon.

Run: python scripts/ingest.py [--source "Human&Ai/01-before"]

--source takes a path relative to ingest/ (or an absolute path) so alternate
intake folders (e.g. authorship-split Human&Ai/ vs AI/) can be staged without
moving files into the default ingest/01-before/. Run each source's full 3-stage
flow (stage1 -> review -> publish) to completion before starting the next one —
id_candidate assignment reads the registry fresh each run, so two un-published
sources staged back-to-back would propose colliding candidate ids.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from datetime import datetime, timezone
from pathlib import Path

from scripts.config import ROOT, SUPPORTED_EXTS
from scripts.helpers import lang_tag
from scripts.registry import load_registry
from scripts.normalize_math import normalize as normalize_math

INGEST = ROOT / "ingest"
STAGING, AFTER, REPORTS = INGEST / "02-agent-staging", INGEST / "03-after", INGEST / "reports"
FIRST_STAGE_EXTS = {".md", ".py", ".lean", ".ts", ".jsx"}


def _resolve_source(source: str | None) -> Path:
    if not source:
        return INGEST / "01-before"
    p = Path(source)
    return p if p.is_absolute() else INGEST / p


def _hash(p):
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return "sha256:" + h.hexdigest()


def _infer_date(name):
    m = re.search(r"(20\d{2})[-_]?(0[1-9]|1[0-2])(?:[-_]?(\d{2}))?", name)
    if m:
        return f"{m.group(1)}-{m.group(2)}", ("explicit" if m.group(3) else "inferred")
    # No date in filename: a freshly ingested paper's publication date is NOW
    # (upload = the objective public date, per project policy) — not "undated".
    return datetime.now(timezone.utc).strftime("%Y-%m"), "publication-now"


def _sub(month):
    return f"{month.split('-')[0]}/{month}" if month else "undated"


def main(source: str | None = None):
    BEFORE = _resolve_source(source)
    for d in (BEFORE, STAGING, AFTER, REPORTS):
        d.mkdir(parents=True, exist_ok=True)
    reg = load_registry()
    known_hashes = {it.get("hash") for it in reg.get("items", [])}
    known_titles = {it.get("title") for it in reg.get("items", [])}
    used_ids = {it["id"] for it in reg.get("items", [])}

    def next_candidate():
        n = 1
        while f"lm-{n:06d}" in used_ids:
            n += 1
        cid = f"lm-{n:06d}"
        used_ids.add(cid)
        return cid

    files = sorted(p for p in BEFORE.rglob("*")
                   if p.is_file() and p.suffix.lower() in FIRST_STAGE_EXTS
                   and p.suffix.lower() in SUPPORTED_EXTS)
    ready, review = [], []
    for f in files:
        title, ext = f.stem, f.suffix.lower().lstrip(".")
        h = _hash(f)
        dup = (h in known_hashes) or (title in known_titles)
        month, conf = _infer_date(f.name)
        needs_review = dup or conf == "unknown"
        cand = next_candidate()
        unit = STAGING / cand
        unit.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, unit / ("source." + ext))
        meta = {"id_candidate": cand, "title": title, "ext": ext,
                "language": lang_tag(title), "hash": h, "month": month,
                "date_confidence": conf,
                "date_basis": "filename-inferred (publication date; confirm before publish)",
                "duplicate_candidate": dup, "needs_review": needs_review,
                "proposed_path": f"content/papers/{_sub(month)}/{f.name}",
                "source_name": f.name}
        (unit / "metadata.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2),
                                            encoding="utf-8")
        (unit / "proposed-frontmatter.yaml").write_text(
            f"---\ntitle: {json.dumps(title, ensure_ascii=False)}\n"
            f"language: {meta['language']}\nmonth: {month or 'unknown'}\n"
            f"date_confidence: {conf}\nstatus: staged\n---\n", encoding="utf-8")
        notes = []
        if dup:
            notes.append("Possible duplicate (hash or title already in registry) — do NOT publish without review.")
        if conf == "unknown":
            notes.append("Date not inferable from filename; would go to content/papers/undated/ unless corrected.")
        (unit / "notes.md").write_text(
            "# Staging notes\n\n" + ("\n".join(f"- {n}" for n in notes) or "- OK: no blockers."),
            encoding="utf-8")
        if needs_review:
            review.append(meta)
        else:
            dest = AFTER / _sub(month)
            dest.mkdir(parents=True, exist_ok=True)
            # Auto-repair Canvas copy-paste math corruption on .md (no-op on a clean
            # \[…\] download — see scripts/normalize_math.py). What lands in 03-after
            # is exactly what gets reviewed and published.
            if ext == "md":
                raw = f.read_text(encoding="utf-8", newline="")  # preserve EOL
                fixed = normalize_math(raw)
                (dest / f.name).write_text(fixed, encoding="utf-8", newline="")
            else:
                shutil.copy2(f, dest / f.name)
            ready.append(meta)

    now = datetime.now(timezone.utc)
    ts = now.strftime("%Y-%m-%dT%H%M%SZ")
    iso = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    (REPORTS / f"ingest-{ts}.json").write_text(json.dumps(
        {"generated_at": iso, "input_files": len(files), "ready": len(ready),
         "needs_review": len(review), "ready_items": ready,
         "needs_review_items": review}, ensure_ascii=False, indent=2), encoding="utf-8")
    md = ["# Ingest Report", f"Generated at: {iso}", "",
          f"- Input files: {len(files)}", f"- Ready: {len(ready)}",
          f"- Needs review: {len(review)}", ""]
    for label, lst in (("Ready", ready), ("Needs review", review)):
        if lst:
            md.append(f"## {label}")
            for m in lst:
                md += [f"### {m['id_candidate']} — {m['title']}",
                       f"- proposed_path: {m['proposed_path']}",
                       f"- date_confidence: {m['date_confidence']} | duplicate: {m['duplicate_candidate']}", ""]
    (REPORTS / f"ingest-{ts}.md").write_text("\n".join(md), encoding="utf-8")
    print(f"[ingest] input={len(files)} ready={len(ready)} needs_review={len(review)} "
          f"-> ingest/03-after + reports/ingest-{ts}.md (canonical corpus untouched)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default=None,
                         help='Path relative to ingest/ (or absolute) to stage instead of 01-before/.')
    main(parser.parse_args().source)
