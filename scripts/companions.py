#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Companion attachments — the C-model sub-coordinate layer.

A companion is a file that belongs to a paper (accompanying code, a Lean proof, a
witness dataset, a worked-example set) but is NOT itself a standalone paper: it has
no own lm-id, and is absent from the timeline and the corpus count. Companions live
in content/attachments/{parent-id}/ and are served under the PARENT's coordinate at
/raw/{parent-id}/{file} — literally a sub-link under the paper's id.

Declared in registry/companions.json (overlay, keyed by parent lm-id), mirroring the
media.json / ai-authored.json overlay pattern. Two provenance modes:

    born-C    the file was always an attachment (no retired_id).
    migrate-C the file used to be a mis-filed standalone paper; `retired_id` records
              the lm-id it held. The build reserves that id forever (registry never
              reassigns it — see registry._reserved_companion_ids) and 301s
              /p/{retired_id}/ + /raw/{retired_id}.{ext} to the parent, honouring the
              canonical-URL iron rule.

Outputs:
    dist/raw/{parent}/{file}          the attachment bytes (served, citable, re-verifiable)
    dist/ai/companions.json           machine declaration (parent -> [attachments])
    dist/companions-redirect-map.json retired path -> target, for the Worker's 301s

Returns redirect + legacy-slug extras that idroutes folds into redirects.json and
papers-legacy-map.json.
"""
import hashlib
import json
import shutil
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

from scripts.config import *
from scripts.helpers import *

REGISTRY_DIR = ROOT / "registry"
COMPANIONS_JSON = REGISTRY_DIR / "companions.json"
ATTACH_DIR = ROOT / "content" / "attachments"


def _sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _zip_file_count(path: Path):
    """Number of non-directory entries inside a zip, without extracting. None if unreadable."""
    try:
        with zipfile.ZipFile(path) as zf:
            return sum(1 for info in zf.infolist() if not info.is_dir())
    except (zipfile.BadZipFile, OSError):
        return None


def load_companions() -> dict:
    """{parent_id: [attachment, ...]} from registry/companions.json, or {}."""
    if COMPANIONS_JSON.exists():
        try:
            return json.loads(COMPANIONS_JSON.read_text(encoding="utf-8")).get("companions", {}) or {}
        except Exception:
            return {}
    return {}


def reserved_ids() -> set:
    """Retired lm-ids (papers demoted to companions) that must never be reassigned."""
    ids = set()
    for atts in load_companions().values():
        for a in atts or []:
            rid = a.get("retired_id")
            if rid:
                ids.add(rid)
    return ids


def _now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def write_companions(registry) -> dict:
    """Copy attachments into dist/raw/{parent}/, emit /ai/companions.json + the
    retired-id redirect map, and return extras for redirects.json / the legacy map:

        {"redirects": [{from,to,status}], "legacy": {slug: {id, ext}},
         "attachments": int, "parents": int, "retired": [ids], "missing": [..]}
    """
    companions = load_companions()
    known = {it["id"] for it in registry["items"]}
    by_id = {it["id"]: it for it in registry["items"]}

    emitted = {}      # parent -> [resolved attachment]
    redirects = []    # for redirects.json
    legacy = {}       # slug -> {id, ext} for papers-legacy-map.json
    redir_map = {}    # /p|/raw path -> target, for the Worker
    missing, retired = [], []
    n_att = 0

    for parent, atts in sorted(companions.items()):
        if parent not in known:
            print(f"[warn] companions: parent {parent} not in registry — skipped")
            continue
        resolved = []
        for a in atts or []:
            fname = a.get("file")
            if not fname:
                continue
            src = ATTACH_DIR / parent / fname
            if not src.exists():
                print(f"[warn] companions: missing file {src} — skipped")
                missing.append(f"{parent}/{fname}")
                continue
            ext = Path(fname).suffix.lower().lstrip(".")
            dst = DIST_DIR / "raw" / parent / fname
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            raw_url = f"/raw/{parent}/{quote(fname)}"
            entry = {
                "file": fname,
                "orig": a.get("orig", fname),
                "label": a.get("label", fname),
                "kind": a.get("kind", "file"),
                "ext": ext,
                "bytes": src.stat().st_size,
                "raw_url": raw_url,
                "mime": mime_for(ext),
                "sha256": _sha256_of(src),
            }
            if ext == "zip":
                fc = _zip_file_count(src)
                if fc is not None:
                    entry["file_count"] = fc
            rid = a.get("retired_id")
            if rid:
                entry["retired_id"] = rid
                retired.append(rid)
                # true 301s for the id + raw route this file used to occupy
                redirects.append({"from": f"/p/{rid}/", "to": f"/p/{parent}/", "status": 301})
                redirects.append({"from": f"/raw/{rid}.{ext}", "to": raw_url, "status": 301})
                redir_map[f"/p/{rid}/"] = f"/p/{parent}/"
                redir_map[f"/raw/{rid}.{ext}"] = raw_url
                # legacy /papers/<slug> surface the retired paper had -> parent
                rslug = a.get("retired_slug")
                if rslug:
                    legacy[rslug] = {"id": parent, "ext": by_id[parent]["ext"]}
            resolved.append(entry)
            n_att += 1
        if resolved:
            emitted[parent] = resolved

    # machine declaration (sibling of /ai/media.json)
    ai = DIST_DIR / "ai"
    ai.mkdir(parents=True, exist_ok=True)
    (ai / "companions.json").write_text(json.dumps({
        "version": "0.2", "generated_at": _now(),
        "parents": len(emitted), "attachments": n_att,
        "note": "parent lm-id -> [attachments]. Each attachment is a sub-coordinate file "
                "(/raw/{parent}/{file}) that belongs to the paper but is not itself a "
                "standalone paper (no own id, absent from the timeline/count). retired_id "
                "(if present) = the id this file held when mis-filed as a paper; it 301s to "
                "the parent. sha256 = hash of the exact bytes served at raw_url — verify "
                "integrity before or after download, same guarantee as AMRAL's package "
                "manifests (raw bytes, never repackaged). file_count (zip only) = number of "
                "files inside the archive, so a crawler can judge it before downloading.",
        "companions": emitted,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # compact retired-path -> target map for the Worker's 301s
    (DIST_DIR / "companions-redirect-map.json").write_text(
        json.dumps(redir_map, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    return {"redirects": redirects, "legacy": legacy, "attachments": n_att,
            "parents": len(emitted), "retired": retired, "missing": missing}
