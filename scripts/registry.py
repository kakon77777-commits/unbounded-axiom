#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Stable-identity layer for the Corpus Engine.

Assigns a permanent `lm-NNNNNN` id to every paper and persists it in
registry/papers.json. Ids are keyed by the source file path so they survive
title/slug changes and rebuilds; new files get the next free id.

Dates use the git first-add month as the *publication / upload date* (an
objective public date), which per project policy is distinct from the author's
in-text writing date. Untracked files (no git history) get date_confidence
'unknown'. Papers ingested from 2026-08-07 onward (Neo's CTCL-as-base-timestamp
policy) get a verified CTCL instant instead, via registry/ctcl-dates.json —
see _ctcl_dates(). Everything published before that date keeps git-first-add
forever; the two sources never mix for the same paper.
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


def _ctcl_dates():
    """basename -> {'instant_id', 'rfc3339', 'source', 'signature_alg', 'date'}, from
    registry/ctcl-dates.json. Populated by ingest.py when run with --ctcl-instant-file
    (Neo's 2026-08-07 policy: every paper ingested from that date on is dated by a
    verified, Ed25519-signed CTCL instant instead of git-first-add). Absent entirely for
    any paper published before that switch — those keep git-first-add, forever, by
    design (mirrors _ai_authored_set() / _reserved_companion_ids(): an optional sidecar,
    {} if missing, never required)."""
    p = REGISTRY_DIR / "ctcl-dates.json"
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}


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
    prev_items = prev.get("items", [])
    # Identity is keyed by exact path first (unambiguous: two files can never
    # share a path). Basename is only a FALLBACK, for the case ids need to
    # survive the chronological folder move (papers/ -> content/papers/
    # YYYY/YYYY-MM/) -- same file, same content, new path, old path gone.
    #
    # An earlier version of this function keyed by basename ALONE, via a
    # single `{basename: item}` dict built from prev_items. That silently
    # broke the moment two DIFFERENT files ever shared a basename (e.g. a
    # revised draft of 《貨幣的時間本質...》 re-ingested into a later month
    # folder without renaming -- found as a real defect, both files resolving
    # to lm-000199, different content_hash). Worse: once that collision was
    # baked into a saved registry, the basename dict comprehension collapsed
    # the two prior entries into whichever iterated last, so a naive
    # path-independent fix made ids CHURN on every rebuild instead of
    # settling -- caught by re-running the pipeline twice and diffing, not by
    # reasoning about the code alone.
    prev_by_path = {it["source_file"]: it["id"] for it in prev_items}
    prev_by_base = {}
    for it in prev_items:
        prev_by_base.setdefault(Path(it["source_file"]).name, []).append((it["source_file"], it["id"]))

    used_ids = {it["id"] for it in prev_items}
    used_ids |= _reserved_companion_ids()  # retired (demoted) ids stay reserved forever

    def next_id():
        n = 1
        while f"lm-{n:06d}" in used_ids:
            n += 1
        return f"lm-{n:06d}"

    dates = _git_first_add_dates()  # basename -> 'YYYY-MM-DD'
    ctcl_dates = _ctcl_dates()      # basename -> CTCL instant record (CTCL-era papers only)
    ai_set = _ai_authored_set()     # ids/basenames that are AI-autonomous (default: none)

    cur = []
    for slug, display, ext, src in entries:
        rel = src.relative_to(ROOT).as_posix()
        cur.append((src.name, rel, slug, display, ext, src))
    cur_paths = {rel for _, rel, *_ in cur}

    path_to_id = {}
    for base, rel, *_ in cur:
        if rel in prev_by_path:
            path_to_id[rel] = prev_by_path[rel]  # unambiguous: this exact path already has an id
            continue
        candidates = prev_by_base.get(base, [])
        # A real move/rename: exactly one prior entry had this basename, and
        # its old exact path is gone now (not still present under some OTHER
        # current path -- that would mean two files sharing a name, not one
        # file moving).
        if len(candidates) == 1 and candidates[0][0] not in cur_paths:
            path_to_id[rel] = candidates[0][1]

    # New files (including "moved" candidates that didn't resolve above) get
    # the next free id, in deterministic path order.
    for base, rel, *_ in sorted(cur, key=lambda t: t[1]):
        if rel not in path_to_id:
            nid = next_id()
            used_ids.add(nid)
            path_to_id[rel] = nid

    # Safety net: an id must resolve to exactly one path. Catches a collision
    # already baked into a PRIOR registry (the lm-000199 class) -- without
    # this, the exact-path lookup above would silently perpetuate it forever
    # instead of ever repairing it. Keeps the first path (sorted,
    # deterministic); every other path claiming the same id gets a fresh one.
    id_to_paths = {}
    for rel, eid in path_to_id.items():
        id_to_paths.setdefault(eid, []).append(rel)
    for eid, paths in id_to_paths.items():
        if len(paths) < 2:
            continue
        for rel in sorted(paths)[1:]:
            nid = next_id()
            used_ids.add(nid)
            path_to_id[rel] = nid

    def _month_from_path(relp):
        m = re.search(r"papers/(\d{4})/(\d{4}-\d{2})/", relp)
        return m.group(2) if m else None

    items = []
    for base, rel, slug, display, ext, src in cur:
        eid = path_to_id[rel]
        ctcl = ctcl_dates.get(base)             # CTCL instant record, if this paper is CTCL-era
        d = ctcl["date"] if ctcl else dates.get(base)  # 'YYYY-MM-DD' or None
        mp = _month_from_path(rel)             # folder-path month 'YYYY-MM' (authoritative §5)
        if mp:
            year, month, conf = int(mp[:4]), mp, "explicit"
        elif d:
            year, month, conf = int(d[:4]), d[:7], "explicit"
        else:
            year, month, conf = None, None, "unknown"
        basis = (f"ctcl-verified-instant ({ctcl['instant_id']}, {ctcl['signature_alg']}-signed, "
                  f"{ctcl['rfc3339']})" if ctcl else
                 "git-first-add (publication/upload date; not the author's in-text writing date)")
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
            "date_basis": basis,
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
