#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""§25 three-stage ingest — STAGE 2.

Promote ingest/03-after/** into the canonical corpus at content/papers/ (keeping
the YYYY/YYYY-MM structure), then rebuild so the new papers receive real stable
ids and all canonical routes. This is the ONLY writer into content/papers/.

Run: python scripts/publish_ingested.py
"""
import json
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from datetime import datetime, timezone

from scripts.config import ROOT, PAPERS_DIR

INGEST = ROOT / "ingest"
AFTER = INGEST / "03-after"
REPORTS = INGEST / "reports"


def main():
    AFTER.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)
    moved = []
    for f in sorted(p for p in AFTER.rglob("*") if p.is_file() and p.name != ".gitkeep"):
        rel = f.relative_to(AFTER)                 # e.g. 2026/2026-05/name.md
        dest = PAPERS_DIR / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(f), str(dest))
        moved.append(str(rel).replace("\\", "/"))

    if moved:
        from scripts.build import main as build_main
        build_main()

    now = datetime.now(timezone.utc)
    ts = now.strftime("%Y-%m-%dT%H%M%SZ")
    (REPORTS / f"publish-{ts}.json").write_text(json.dumps(
        {"generated_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "promoted": len(moved),
         "rebuilt": bool(moved), "files": moved}, ensure_ascii=False, indent=2),
        encoding="utf-8")
    print(f"[publish] promoted {len(moved)} file(s) into {PAPERS_DIR}; "
          f"{'rebuilt' if moved else 'nothing to rebuild'} -> reports/publish-{ts}.json")


if __name__ == "__main__":
    main()
