#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Stable-id output routes (additive; non-breaking).

Generates the canonical machine/human surface keyed by stable id:

    /p/{id}/index.html      canonical paper page (self-canonical)
    /raw/{id}.{ext}         raw source copy
    /api/papers/{id}.json   per-paper metadata
    /api/papers/index.json  registry index
    /_redirects             Cloudflare legacy -> canonical 301 map (blueprint)
    /redirects.json         machine-readable redirect map

Legacy /papers/<slug>.md(.html) output is left untouched by this module, so
existing URLs, functions, and base-space keep working. The /p/ pages carry a
log-crawler prefetch keyed by the *legacy slug* so the Triadic-Logic graph node
identity stays unified with the legacy pages.
"""
import json
import shutil
from datetime import datetime, timezone

from scripts.config import *
from scripts.helpers import *
from scripts.render import *

REGISTRY_DIR = ROOT / "registry"


def _paper_doc(item, body, mode) -> str:
    """Render /p/{id}/index.html. Mirrors the legacy paper page but with absolute
    paths, an id-based self-canonical, and /raw/{id}.{ext} as the source."""
    display = item["title"]
    ext = item["ext"]
    slug = item["legacy_slug"]
    lang = lang_tag(display)
    canonical = f"{SITE_URL}{item['canonical_url']}"        # https://.../p/{id}/
    raw_href = item["raw_url"]                              # /raw/{id}.{ext}
    log_slug = quote(slug)                                  # graph node key (legacy)
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
        f'<link rel="prefetch" href="/api/log-crawler?slug={log_slug}">\n'
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


def write_id_pages(registry, entries) -> int:
    smap = _src_map(entries)
    n = 0
    for item in registry["items"]:
        slug, display, ext, src = smap[item["source_file"]]
        body, mode = extract_body(src, ext)
        d = DIST_DIR / "p" / item["id"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(_paper_doc(item, body, mode), encoding="utf-8")
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
    idx_fields = ("id", "title", "language", "month", "canonical_url", "raw_url", "api_url")
    index = {
        "version": "0.2",
        "count": len(registry["items"]),
        "items": [{k: it[k] for k in idx_fields} for it in registry["items"]],
    }
    (apidir / "index.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_redirects(registry) -> None:
    """Cloudflare _redirects + machine-readable redirects.json mapping legacy
    /papers/ URLs to the stable-id canonical/raw routes."""
    lines = ["# Legacy paper URLs -> stable-id canonical routes (Corpus Engine v0.2)"]
    data = []
    for it in registry["items"]:
        slug = it["legacy_slug"]
        page_from = f"/papers/{slug}.html"
        raw_from = f"/papers/{slug}"
        lines.append(f"{page_from} {it['canonical_url']} 301")
        lines.append(f"{raw_from} {it['raw_url']} 301")
        data.append({"from": page_from, "to": it["canonical_url"], "status": 301})
        data.append({"from": raw_from, "to": it["raw_url"], "status": 301})
    (DIST_DIR / "_redirects").write_text("\n".join(lines) + "\n", encoding="utf-8")
    payload = json.dumps({"version": "0.2", "redirects": data}, ensure_ascii=False, indent=2) + "\n"
    (DIST_DIR / "redirects.json").write_text(payload, encoding="utf-8")
    REGISTRY_DIR.mkdir(exist_ok=True)
    (REGISTRY_DIR / "redirects.json").write_text(payload, encoding="utf-8")


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
