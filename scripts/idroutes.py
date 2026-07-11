#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Stable-id output routes (additive; non-breaking).

Generates the canonical machine/human surface keyed by stable id:

    /p/{id}/index.html      canonical paper page (self-canonical)
    /raw/{id}.{ext}         raw source copy
    /api/papers/{id}.json   per-paper metadata
    /api/papers/index.json  registry index
    /_redirects             header-only (0 rules; /papers/* handled by a Function)
    /redirects.json         machine-readable redirect map (page + raw)
    /papers-legacy-map.json { legacy_slug: {id, ext} } for the catch-all Function

The legacy /papers/<slug>(.html) surface is retired: it is no longer generated as
files and is served by the catch-all Pages Function functions/papers/[[path]].js,
which 301s to /p/{id}/ or /raw/{id}.{ext}. The /p/ pages carry a log-crawler
prefetch keyed by the *stable id* so the Triadic-Logic graph node identity is
id-native end to end.
"""
import json
import shutil
from datetime import datetime, timezone

from scripts.config import *
from scripts.helpers import *
from scripts.render import *
from scripts.geo_layer import geo_jsonld_blocks, jsonld_script_tags

REGISTRY_DIR = ROOT / "registry"


def _paper_doc(item, body, mode, geo_signals=None) -> str:
    """Render /p/{id}/index.html. Mirrors the legacy paper page but with absolute
    paths, an id-based self-canonical, and /raw/{id}.{ext} as the source.

    geo_signals (optional): {"qa": [...], "definitions": [...]} detected in the raw
    source (scripts/geo_layer.py) — emits extra FAQPage/DefinedTermSet JSON-LD when
    present. Not used by the production build (the Astro shell overlay regenerates
    /p/{id}/ independently, see shell/src/lib/geo.ts) but keeps a plain `python
    build.py` run consistent for local preview."""
    display = item["title"]
    ext = item["ext"]
    lang = lang_tag(display)
    canonical = f"{SITE_URL}{item['canonical_url']}"        # https://.../p/{id}/
    raw_href = item["raw_url"]                              # /raw/{id}.{ext}
    page_description = f"{display} | {SITE_TITLE} {SITE_VERSION}"

    if mode in ("full", "source") and body:
        note = "" if mode == "full" else '<p style="opacity:0.6">[原始碼檢視 / source view]</p>'
        content = note + body
    else:
        if ext == "pdf":
            content = (
                f'<p>PDF 文件。<a href="{raw_href}" target="_blank" rel="noopener">開啟 / 下載原檔</a></p>'
                f'<iframe src="{raw_href}" style="width:100%;height:80vh;border:1px solid #0f0;margin-top:12px"></iframe>'
            )
        else:
            content = f'<p>原檔：<a href="{raw_href}" target="_blank" rel="noopener">下載 {esc(ext)}</a></p>'

    jsonld = (
        "{\n"
        '  "@context": "https://schema.org",\n'
        '  "@type": "ScholarlyArticle",\n'
        f'  "name": {json_safe(display)},\n'
        f'  "url": "{canonical}",\n'
        f'  "identifier": {json_safe(item["id"])},\n'
        f'  "inLanguage": "{lang}",\n'
        f'  "author": {{"@type": "Person", "name": {json_safe(SITE_AUTHOR)}}},\n'
        f'  "publisher": {{"@type": "Organization", "name": {json_safe(SITE_ORG)}}},\n'
        f'  "isPartOf": {{"@type": "Collection", "name": {json_safe(SITE_TITLE)}, "url": "{SITE_URL}"}},\n'
        '  "encodingFormat": "text/html"\n'
        "}"
    )
    extra_jsonld = jsonld_script_tags(geo_jsonld_blocks(geo_signals, canonical)) if geo_signals else ""

    return (
        "<!DOCTYPE html>\n"
        f'<html lang="{lang}">\n<head>\n'
        '<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        f"<title>{esc(display)} · {esc(SITE_TITLE)}</title>\n"
        f'<meta name="description" content="{esc(page_description)}">\n'
        f'<meta name="author" content="{esc(SITE_AUTHOR)}">\n'
        '<meta name="robots" content="index, follow">\n'
        '<meta name="ai-content-policy" content="indexable, citable, training-allowed">\n'
        f'<meta name="lm-paper-id" content="{esc(item["id"])}">\n'
        f'<link rel="alternate" type="{mime_for(ext)}" href="{raw_href}" title="原始檔 / source ({esc(ext)})">\n'
        f'<link rel="canonical" href="{canonical}">\n'
        f'<script type="application/ld+json">\n{jsonld}\n</script>\n'
        f'{extra_jsonld}'
        f'<link rel="prefetch" href="/api/log-crawler?id={item["id"]}">\n'
        f"<style>{PAGE_CSS}</style>\n</head>\n<body>\n"
        '<div class="nav">'
        '<a href="/index.html">&larr; 回 Logic Matrix 索引</a>'
        '<div>'
        '<a href="/cosmomind.html" style="margin-right:15px;">→ 星環式認知展開圖</a>'
        '<a href="/base-space.html">🧬 拓撲底空間</a>'
        '</div>'
        '</div>\n'
        f'<header class="header"><h1>{esc(display)}</h1>'
        f'<p>{esc(SITE_TITLE)} · {esc(SITE_ORG)}</p></header>\n'
        f"{disclaimer_html()}\n"
        f"<article>\n{content}\n"
        f'<div class="altbar">原始檔（供 RAG/下載）：'
        f'<a href="{raw_href}" rel="noopener">{esc(raw_href)}</a> [{esc(ext)}] · id: {esc(item["id"])}</div>\n'
        "</article>\n"
        f"<footer><p>{esc(SITE_AUTHOR)} · Cl + ε</p></footer>\n"
        "</body>\n</html>\n"
    )


def _src_map(entries):
    return {src.relative_to(ROOT).as_posix(): (slug, display, ext, src)
            for slug, display, ext, src in entries}


def write_id_pages(registry, entries, geo_per_id=None) -> int:
    smap = _src_map(entries)
    geo_per_id = geo_per_id or {}
    n = 0
    for item in registry["items"]:
        slug, display, ext, src = smap[item["source_file"]]
        body, mode = extract_body(src, ext)
        d = DIST_DIR / "p" / item["id"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(
            _paper_doc(item, body, mode, geo_per_id.get(item["id"])), encoding="utf-8")
        n += 1
    return n


def write_raw_files(registry, entries) -> int:
    smap = _src_map(entries)
    rawdir = DIST_DIR / "raw"
    rawdir.mkdir(parents=True, exist_ok=True)
    n = 0
    for item in registry["items"]:
        _, _, _, src = smap[item["source_file"]]
        shutil.copy2(src, rawdir / f"{item['id']}.{item['ext']}")
        n += 1
    return n


def write_api(registry) -> None:
    apidir = DIST_DIR / "api" / "papers"
    apidir.mkdir(parents=True, exist_ok=True)
    for item in registry["items"]:
        (apidir / f"{item['id']}.json").write_text(
            json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    idx_fields = ("id", "title", "language", "authorship", "month", "canonical_url", "raw_url", "api_url")
    index = {
        "version": "0.2",
        "count": len(registry["items"]),
        "items": [{k: it[k] for k in idx_fields} for it in registry["items"]],
    }
    (apidir / "index.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_redirects(registry, companions=None) -> None:
    """Full machine-readable redirects.json (page+raw). NO static _redirects rules.

    The legacy /papers/* surface is retired: every /papers/<slug>(.html) request is
    handled dynamically by the catch-all Pages Function functions/papers/[[path]].js,
    which 301s to /p/{id}/ (page) or /raw/{id}.{ext} (raw). We therefore emit ZERO
    per-paper rules into dist/_redirects — a static rule and a Function on the same
    /papers/* path both claim the route (Functions win, so static rules would be dead
    weight yet still count against Cloudflare's 2000-rule cap and drift out of sync).
    The complete page+raw map is still published for agents in /redirects.json and
    registry/redirects.json."""
    data = []
    for it in registry["items"]:
        slug = it["legacy_slug"]
        page_from = f"/papers/{slug}.html"
        raw_from = f"/papers/{slug}"
        data.append({"from": page_from, "to": it["canonical_url"], "status": 301})
        data.append({"from": raw_from, "to": it["raw_url"], "status": 301})
    # Companion demotions: retired /p/{id}/ + /raw/{id}.{ext} -> parent (301).
    if companions:
        data.extend(companions.get("redirects", []))
    # _redirects carries NO per-paper rules (the [[path]].js Function handles /papers/*).
    (DIST_DIR / "_redirects").write_text(
        "# /papers/* is handled dynamically by functions/papers/[[path]].js (0 static rules)\n",
        encoding="utf-8")
    payload = json.dumps({"version": "0.2", "redirects": data}, ensure_ascii=False, indent=2) + "\n"
    (DIST_DIR / "redirects.json").write_text(payload, encoding="utf-8")
    REGISTRY_DIR.mkdir(exist_ok=True)
    (REGISTRY_DIR / "redirects.json").write_text(payload, encoding="utf-8")


def write_legacy_map(registry, companions=None) -> None:
    """dist/papers-legacy-map.json — flat { legacy_slug: {id, ext} } for the
    catch-all Function functions/papers/[[path]].js to resolve legacy /papers/<slug>
    URLs to their id-native targets (/p/{id}/ page or /raw/{id}.{ext} raw)."""
    legacy_map = {
        it["legacy_slug"]: {"id": it["id"], "ext": it["ext"]}
        for it in registry["items"]
    }
    # A retired paper's legacy /papers/<slug> now points at its parent paper.
    if companions:
        legacy_map.update(companions.get("legacy", {}))
    (DIST_DIR / "papers-legacy-map.json").write_text(
        json.dumps(legacy_map, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_sitemap_canonical(registry) -> None:
    """Canonical-only sitemap (§26.6.6): stable-id /p/{id}/ routes + fixed hub pages.
    Legacy /papers/ URLs are intentionally NOT listed — they 301 to canonical, so
    crawlers converge on one stable route per paper instead of guessing."""
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    fixed = ["/", "/cosmomind.html", "/base-space.html", "/deconstruction.html",
             "/llms.txt", "/llms-full.txt"]
    urls = [f"  <url><loc>{SITE_URL}{u}</loc><lastmod>{now_iso}</lastmod></url>" for u in fixed]
    for it in registry["items"]:
        urls.append(
            f"  <url><loc>{SITE_URL}{it['canonical_url']}</loc><lastmod>{now_iso}</lastmod></url>"
        )
    body = ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "\n".join(urls) + "\n</urlset>\n")
    (DIST_DIR / "sitemap.xml").write_text(body, encoding="utf-8")
