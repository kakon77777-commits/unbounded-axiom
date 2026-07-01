#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deterministic-ingestion validators (whitepaper §26).

- validate_routes: every registry item's canonical/raw/api route must exist in
  dist (§26.7.2-4). Writes registry/generated/route-consistency.json.
- validate_links: scan the CANONICAL HTML surface (/p/, hubs, index) for unknown
  internal relative links — the "[t] / [x_0] / /papers/λ fake page" problem
  (§26.5.7). Warn-only in phase 1. Writes registry/generated/broken-links.json.

Turning lottery-like ingestion into deterministic ingestion means: no route the
manifest promises is missing, and no rendered link invents a page that isn't there.
"""
import json
import os
import re

from scripts.config import *

REGISTRY_DIR = ROOT / "registry"
GEN_DIR = REGISTRY_DIR / "generated"
IGNORED = REGISTRY_DIR / "ignored-links.json"

# Cloudflare Pages Functions (dynamic routes, not static files) — always valid targets.
KNOWN_DYNAMIC = ("api/log-crawler", "api/base-space")

# hrefs; skip pure in-page anchors (href="#...").
_HREF = re.compile(r'href="([^"#][^"]*)"')


def _load_ignored():
    if IGNORED.exists():
        try:
            d = json.loads(IGNORED.read_text(encoding="utf-8"))
            return ([re.compile(p) for p in d.get("ignore_patterns", [])],
                    set(d.get("ignore_exact", [])))
        except Exception:
            pass
    return [], set()


def validate_routes(registry) -> list:
    """§26.7.2-4: assert canonical_url / raw_url / api_url all exist in dist."""
    issues = []
    for it in registry["items"]:
        for path, url in (
            (DIST_DIR / "p" / it["id"] / "index.html", it["canonical_url"]),
            (DIST_DIR / "raw" / f"{it['id']}.{it['ext']}", it["raw_url"]),
            (DIST_DIR / "api" / "papers" / f"{it['id']}.json", it["api_url"]),
        ):
            if not path.exists():
                issues.append({"id": it["id"], "missing": url})
    GEN_DIR.mkdir(parents=True, exist_ok=True)
    (GEN_DIR / "route-consistency.json").write_text(json.dumps({
        "version": "0.2",
        "total_papers": len(registry["items"]),
        "routes_checked": len(registry["items"]) * 3,
        "missing": len(issues),
        "ok": len(issues) == 0,
        "issues": issues[:200],
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return issues


def _existing_paths() -> set:
    ex = set()
    for dp, _, fns in os.walk(DIST_DIR):
        for fn in fns:
            ex.add(os.path.relpath(os.path.join(dp, fn), DIST_DIR).replace("\\", "/"))
    return ex


def _resolves(href, page_rel, existing, ign_pat, ign_exact) -> bool:
    h = href.split("#", 1)[0].split("?", 1)[0]
    if not h:
        return True
    if re.match(r'^[a-zA-Z][a-zA-Z0-9+.\-]*://', h) or h.startswith("//"):
        return True
    if h.startswith(("mailto:", "tel:", "javascript:", "data:")):
        return True
    if h in ign_exact or any(p.search(h) for p in ign_pat):
        return True
    if h.startswith("/"):
        target = h.lstrip("/")
    else:
        target = os.path.normpath(os.path.join(os.path.dirname(page_rel), h)).replace("\\", "/")
    target = target.rstrip("/")
    if not target:
        return True  # site root
    if target.startswith(KNOWN_DYNAMIC):
        return True
    return (target in existing
            or f"{target}/index.html" in existing
            or f"{target}.html" in existing)


def validate_links(registry) -> list:
    """§26.5.7: report unknown internal relative links on the canonical surface."""
    ign_pat, ign_exact = _load_ignored()
    existing = _existing_paths()
    broken = []
    scanned = 0
    for dp, _, fns in os.walk(DIST_DIR):
        for fn in fns:
            if not fn.endswith(".html"):
                continue
            page_rel = os.path.relpath(os.path.join(dp, fn), DIST_DIR).replace("\\", "/")
            if page_rel.startswith("papers/"):
                continue  # legacy surface (being retired) — validate the canonical surface
            scanned += 1
            try:
                html = open(os.path.join(dp, fn), encoding="utf-8").read()
            except Exception:
                continue
            for m in _HREF.finditer(html):
                href = m.group(1)
                if not _resolves(href, page_rel, existing, ign_pat, ign_exact):
                    broken.append({"source": "/" + page_rel, "href": href,
                                   "reason": "unknown_relative_link"})
    GEN_DIR.mkdir(parents=True, exist_ok=True)
    (GEN_DIR / "broken-links.json").write_text(json.dumps({
        "version": "0.2",
        "phase": "warn-only",
        "html_scanned": scanned,
        "broken_count": len(broken),
        "broken_links": broken[:500],
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return broken
