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
import re
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


def _ai_authored_set() -> set:
    """Ids/basenames marked AI-autonomous (the Research Ecology output). The default is
    'collaborative' (human-led, AI-assisted — the whole current corpus). A paper is
    'ai_autonomous' only if its id starts with 'lm-ai-' OR it is listed in the optional
    registry/ai-authored.json override. Absent file -> empty set -> all collaborative."""
    p = REGISTRY_DIR / "ai-authored.json"
    if p.exists():
        try:
            return set(json.loads(p.read_text(encoding="utf-8")).get("ai_autonomous", []))
        except Exception:
            pass
    return set()


def _authorship(eid: str, base: str, ai_set: set) -> str:
    return ("ai_autonomous" if (eid.startswith("lm-ai-") or eid in ai_set or base in ai_set)
            else "collaborative")


def _reserved_companion_ids() -> set:
    """Retired ids (papers demoted to companion attachments) that must NEVER be
    reassigned — else a future paper would silently steal a URL that 301s elsewhere.
    Read inline from registry/companions.json (mirrors _ai_authored_set)."""
    p = REGISTRY_DIR / "companions.json"
    if p.exists():
        try:
            comp = json.loads(p.read_text(encoding="utf-8")).get("companions", {}) or {}
            return {a["retired_id"] for atts in comp.values() for a in (atts or [])
                    if a.get("retired_id")}
        except Exception:
            pass
    return set()


def build_registry(entries) -> dict:
    """entries: list of (slug, display, ext, src Path). Returns a registry dict with
    stable ids. Existing ids are preserved (keyed by source_file); new files are
    assigned the next free lm-NNNNNN in sorted source order for determinism."""
    prev = load_registry()
    # Key identity by BASENAME so ids survive the chronological folder move
    # (papers/ -> content/papers/YYYY/YYYY-MM/): the path changes, the name does not.
    by_base = {Path(it["source_file"]).name: it for it in prev.get("items", [])}
    used_ids = {it["id"] for it in prev.get("items", [])}
    used_ids |= _reserved_companion_ids()  # retired (demoted) ids stay reserved forever

    def next_id():
        n = 1
        while f"lm-{n:06d}" in used_ids:
            n += 1
        return f"lm-{n:06d}"

    dates = _git_first_add_dates()  # basename -> 'YYYY-MM-DD'
    ai_set = _ai_authored_set()     # ids/basenames that are AI-autonomous (default: none)

    cur = []
    for slug, display, ext, src in entries:
        rel = src.relative_to(ROOT).as_posix()
        cur.append((src.name, rel, slug, display, ext, src))

    # New files (by basename) get the next free id, in deterministic basename order.
    for base in sorted(b for (b, *_) in cur if b not in by_base):
        nid = next_id()
        used_ids.add(nid)
        by_base[base] = {"id": nid}

    def _month_from_path(relp):
        m = re.search(r"papers/(\d{4})/(\d{4}-\d{2})/", relp)
        return m.group(2) if m else None

    items = []
    for base, rel, slug, display, ext, src in cur:
        eid = by_base[base]["id"]
        d = dates.get(base)                    # git first-add 'YYYY-MM-DD' or None
        mp = _month_from_path(rel)             # folder-path month 'YYYY-MM' (authoritative §5)
        if mp:
            year, month, conf = int(mp[:4]), mp, "explicit"
        elif d:
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
            "authorship": _authorship(eid, base, ai_set),
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
