#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Stable-identity layer for the Corpus Engine.

Assigns a permanent `lm-NNNNNN` id to every paper and persists it in
registry/papers.json. Ids are keyed by the source file path so they survive
title/slug changes and rebuilds; new files get the next free id.

Dates use the git first-add month as the *publication / upload date* (an
objective public date), which per project policy is distinct from the author's
in-text writing date. Untracked files (no git history) get date_confidence
'unknown'.
"""
import hashlib
import json
import subprocess

from scripts.config import *
from scripts.helpers import *

REGISTRY_DIR = ROOT / "registry"
GEN_DIR = REGISTRY_DIR / "generated"
PAPERS_JSON = REGISTRY_DIR / "papers.json"


def _git_first_add_dates():
    """relpath (posix, e.g. 'papers/AGI.md') -> 'YYYY-MM-DD' of first git add. {} if git unavailable."""
    try:
        out = subprocess.run(
            ["git", "-C", str(ROOT), "-c", "core.quotepath=off", "log",
             "--diff-filter=A", "--reverse", "--format=C %ad",
             "--date=format:%Y-%m-%d", "--name-only"],
            capture_output=True,
        ).stdout.decode("utf-8", "replace")
    except Exception:
        return {}
    cur = None
    seen = {}
    for line in out.splitlines():
        if line.startswith("C "):
            cur = line[2:].strip()
        elif line.strip():
            base = line.strip().rsplit("/", 1)[-1]  # basename: move-stable key
            if base not in seen:
                seen[base] = cur
    return seen


def _hash_file(p) -> str:
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return "sha256:" + h.hexdigest()


def load_registry() -> dict:
    if PAPERS_JSON.exists():
        try:
            return json.loads(PAPERS_JSON.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"version": "0.2", "items": []}


def build_registry(entries) -> dict:
    """entries: list of (slug, display, ext, src Path). Returns a registry dict with
    stable ids. Existing ids are preserved (keyed by source_file); new files are
    assigned the next free lm-NNNNNN in sorted source order for determinism."""
    prev = load_registry()
    # Key identity by BASENAME so ids survive the chronological folder move
    # (papers/ -> content/papers/YYYY/YYYY-MM/): the path changes, the name does not.
    by_base = {Path(it["source_file"]).name: it for it in prev.get("items", [])}
    used_ids = {it["id"] for it in prev.get("items", [])}

    def next_id():
        n = 1
        while f"lm-{n:06d}" in used_ids:
            n += 1
        return f"lm-{n:06d}"

    dates = _git_first_add_dates()  # basename -> 'YYYY-MM-DD'

    cur = []
    for slug, display, ext, src in entries:
        rel = src.relative_to(ROOT).as_posix()
        cur.append((src.name, rel, slug, display, ext, src))

    # New files (by basename) get the next free id, in deterministic basename order.
    for base in sorted(b for (b, *_) in cur if b not in by_base):
        nid = next_id()
        used_ids.add(nid)
        by_base[base] = {"id": nid}

    items = []
    for base, rel, slug, display, ext, src in cur:
        eid = by_base[base]["id"]
        d = dates.get(base)
        if d:
            year, month, conf = int(d[:4]), d[:7], "explicit"
        else:
            year, month, conf = None, None, "unknown"
        items.append({
            "id": eid,
            "title": display,
            "source_file": rel,
            "legacy_slug": slug,
            "ext": ext,
            "language": lang_tag(display),
            "created": d,
            "year": year,
            "month": month,
            "date_confidence": conf,
            "date_basis": "git-first-add (publication/upload date; not the author's in-text writing date)",
            "canonical_url": f"/p/{eid}/",
            "raw_url": f"/raw/{eid}.{ext}",
            "api_url": f"/api/papers/{eid}.json",
            "legacy_page_url": f"/papers/{slug}.html",
            "legacy_raw_url": f"/papers/{slug}",
            "hash": _hash_file(src),
        })

    items.sort(key=lambda x: x["id"])
    return {"version": "0.2", "count": len(items), "items": items}


def save_registry(reg) -> None:
    REGISTRY_DIR.mkdir(exist_ok=True)
    GEN_DIR.mkdir(parents=True, exist_ok=True)
    # Persist WITHOUT a timestamp so the file only changes when papers change.
    PAPERS_JSON.write_text(
        json.dumps(reg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
