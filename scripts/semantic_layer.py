#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dynamic Semantic Revealing search index — Phase 0 + Phase 1.

Spec: content/papers/2026/2026-07/02_動態語義顯影_本地端實作技術白皮書_v0.1.md
(lm-001862). This module implements Phase 0 (data inventory ->
documents.raw.jsonl) and the data side of Phase 1 (compressed static index
for the pure-frontend exact+lexical search in shell/public/semantic/).

Every derived field is source-tagged per §5 of the spec:
    author_declared   — came from the paper's own YAML frontmatter
    system_inferred    — deterministic heuristic extraction (no model call)
Phase 2 (dictionary/aliases), Phase 3 (vector/semantic), and Phase 4
(full relation graph + diversity rerank) are NOT implemented here — the
compressed index's "channels" block honestly reports semantic=False,
relations=partial so the frontend never claims capability this layer
doesn't have.

Relations (`related_ids`) are NOT guessed. The only relation source is
registry/programs/*.json — real, already-curated Program membership — so
Tier D ("same series") is honest for the ~50 papers in a Program and
simply absent (not faked) for everything else.

Outputs:
    registry/generated/semantic-documents.raw.jsonl   Phase 0 full record (§4.1)
    dist/ai/semantic-index.min.json                    Phase 1 compressed record (§4.2)
"""
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from scripts.config import *
from scripts.render import extract_raw_text
from scripts.programs import load_program_seeds

GENERATED_DIR = ROOT / "registry" / "generated"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?\n)---\s*\n", re.DOTALL)
FM_KV_RE = re.compile(r'^([A-Za-z_]+):\s*(.*)$')
FM_LIST_ITEM_RE = re.compile(r'^\s*-\s+(.*)$')
HEADING_RE = re.compile(r"^#{2,3}\s+(.+?)\s*$", re.MULTILINE)
MD_STRIP_RE = re.compile(r"[*_`#>]")
LATEX_INLINE_RE = re.compile(r"\$[^$\n]{1,80}\$")
LABEL_LINE_RE = re.compile(r'^[A-Za-z一-鿿 ]{1,14}[:：]\s*\S')
CJK_RUN_RE = re.compile(r"[一-鿿]{2,6}")
# Word/HTML-export leftovers seen across the corpus: stray MSO conditional-comment
# fragments (<!--[if ...]>, <![endif]-->), stray tags, and a leading UTF-8 BOM that
# `str.strip()` does not remove (U+FEFF is not whitespace in Python's unicode tables).
HTML_LINE_RE = re.compile(r'^</?[a-zA-Z!]|^<!--|^<!\[|-->$|^-->')
ABSTRACT_LABEL_RE = re.compile(r'^(摘要|abstract)[:：]?$', re.IGNORECASE)
_COMPARE_STRIP_RE = re.compile(r'[\s*_`「」『』《》〈〉“”‘’．。，、：:；;\-—－()（）\[\]]+')
# Same MSO/HTML leftovers as HTML_LINE_RE, but occurring mid-line (e.g. an inline
# "<![if !msEquation]...<![endif]" placeholder, or a Word equation exported as an
# embedded base64 PNG) rather than as a whole line — must be cut out, not skipped.
INLINE_HTML_RE = re.compile(r'<!--.*?-->|<!\[if[^\]]*\]>?|<!\[endif\]>?|<!\[vml\]>?')
INLINE_DATA_IMAGE_RE = re.compile(r'!\[[^\]]*\]\(data:image[^)]*\)')
# A short line ending in a colon/question mark with nothing after it is a section
# introducer ("其中：", "本文提出：") pointing at a list/equation/quote that follows,
# not summary-worthy prose — skip it while we're still looking for the real paragraph.
INTRODUCER_LINE_RE = re.compile(r'[:：?？]$')
LATIN_TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9+.\-]{1,}")
TITLE_STOPWORDS = {
    "一種", "研究", "初步", "框架", "模型", "理論", "系統", "分析", "方法",
    "白皮書", "技術", "本地", "文件", "論文", "草稿", "報告", "綱領", "系列",
}


def _now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _parse_frontmatter(text: str):
    """Tiny hand-rolled subset of YAML: `key: value` and `key:\\n  - item` lists.
    Good enough for this corpus's frontmatter; not a general YAML parser."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    body = text[m.end():]
    fm: dict = {}
    lines = m.group(1).split("\n")
    i = 0
    while i < len(lines):
        km = FM_KV_RE.match(lines[i])
        if km:
            key, val = km.group(1), km.group(2).strip()
            if val == "":
                items, j = [], i + 1
                while j < len(lines):
                    im = FM_LIST_ITEM_RE.match(lines[j])
                    if not im:
                        break
                    items.append(im.group(1).strip().strip('"'))
                    j += 1
                if items:
                    fm[key] = items
                    i = j
                    continue
            else:
                fm[key] = val.strip('"')
        i += 1
    return fm, body


def _extract_headings(body: str, limit: int = 6) -> list:
    heads = []
    for hm in HEADING_RE.finditer(body):
        h = MD_STRIP_RE.sub("", hm.group(1).strip())
        if h and h not in heads:
            heads.append(h[:60])
        if len(heads) >= limit:
            break
    return heads


def _compare_key(s: str) -> str:
    return _COMPARE_STRIP_RE.sub("", s).lower()


def _extract_summary(body: str, title: str = "", limit: int = 180) -> str:
    title_key = _compare_key(title)
    para, in_fence = [], False
    for raw_line in body.split("\n"):
        s = raw_line.strip()
        if s.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if not s:
            if para:
                break
            continue
        if HTML_LINE_RE.search(s):
            continue
        if s.startswith(("#", "|", "$$", ">", "-", "*", "![")) or re.match(r"^\d+\.", s):
            continue
        if ABSTRACT_LABEL_RE.match(s):
            continue
        s = INLINE_DATA_IMAGE_RE.sub("", s)
        s = INLINE_HTML_RE.sub("", s)
        candidate = MD_STRIP_RE.sub("", s).strip()
        if not candidate:
            continue
        if len(candidate) < 40 and LABEL_LINE_RE.match(candidate):
            continue
        if not para and len(candidate) < 16 and INTRODUCER_LINE_RE.search(candidate):
            continue
        # Skip lines that just restate the title/subtitle (bold-title echo without
        # markdown bold markers, so the "*" prefix check above didn't already catch it).
        ck = _compare_key(candidate)
        if title_key and ck and len(ck) < len(title_key) + 12 and (ck in title_key or title_key in ck):
            continue
        para.append(candidate)
        if len(" ".join(para)) > limit * 2:
            break
    text = " ".join(para)
    text = LATEX_INLINE_RE.sub("", text)
    text = re.sub(r"\s+", " ", text).strip().lstrip("﻿")
    if len(text) > limit:
        text = text[:limit].rstrip() + "…"
    return text


def _extract_keywords(title: str, fm_keywords, limit: int = 6):
    if fm_keywords:
        return [k[:24] for k in fm_keywords[:limit] if k], "author_declared"
    toks = [t for t in CJK_RUN_RE.findall(title) if t not in TITLE_STOPWORDS]
    toks += LATIN_TOKEN_RE.findall(title)
    seen: list = []
    for t in toks:
        if t not in seen:
            seen.append(t)
    return seen[:limit], "system_inferred"


def _build_program_relations():
    """doc_id -> (sorted related doc_ids, program short label). Real, curated
    membership only — never a guessed/heuristic relation."""
    related_map: dict[str, set] = {}
    series_map: dict[str, str] = {}
    for seed in load_program_seeds():
        ids = []
        for a in (seed.get("foundation_artifacts") or []):
            if a.get("id"):
                ids.append(a["id"])
        for a in (seed.get("iterations") or []):
            if a.get("id"):
                ids.append(a["id"])
        ids = list(dict.fromkeys(ids))
        if len(ids) < 2:
            continue
        label = seed.get("short_title") or seed.get("title") or seed.get("id")
        for did in ids:
            related_map.setdefault(did, set()).update(x for x in ids if x != did)
            series_map[did] = label
    return related_map, series_map


def build_documents(registry) -> list:
    """Phase 0: one full record (§4.1) per registry item."""
    related_map, series_map = _build_program_relations()
    generated_at = _now()
    docs = []
    for it in registry["items"]:
        doc_id = it["id"]
        src = ROOT / it["source_file"]
        ext = it.get("ext", "md")
        raw_text = ""
        if src.exists():
            try:
                raw_text = extract_raw_text(src, ext).lstrip("﻿")
            except Exception as e:
                print(f"[warn] semantic_layer: could not read {src} — {e}")
        fm, body = _parse_frontmatter(raw_text) if raw_text else ({}, "")
        headings = _extract_headings(body) if body else []
        summary = _extract_summary(body, it["title"]) if body else ""
        fm_kw = fm.get("keywords") if isinstance(fm.get("keywords"), list) else None
        keywords, kw_source = _extract_keywords(it["title"], fm_kw)
        related = sorted(related_map.get(doc_id, []))
        series = [series_map[doc_id]] if doc_id in series_map else []

        docs.append({
            "id": doc_id,
            "title": it["title"],
            "url": it["canonical_url"],
            "date": it.get("month") or it.get("created") or "",
            "language": it.get("language", ""),
            "summary": summary,
            "headings": headings,
            "body_text": "",
            "series": series,
            "keywords": keywords,
            "aliases": [],
            "related_ids": related,
            "metadata": {
                "title_source": "author_declared",
                "summary_source": "system_inferred" if summary else "unavailable",
                "keywords_source": kw_source,
                "relation_source": "system_inferred" if related else None,
                "confidence": round(0.6 if summary else 0.3, 2),
                "schema_version": "0.1",
                "generated_at": generated_at,
            },
        })
    return docs


def _compact(doc: dict) -> dict:
    """§4.2 search-time compressed record — short keys, no body_text."""
    return {
        "i": doc["id"], "t": doc["title"], "u": doc["url"], "d": doc["date"],
        "s": doc["summary"], "h": doc["headings"], "k": doc["keywords"],
        "r": doc["related_ids"],
    }


def write_semantic_index(registry, build_id=None) -> dict:
    """Write both Phase 0 (raw jsonl) and Phase 1 (compressed static index).
    Returns {"count", "with_summary", "with_headings", "with_related", "bytes"}."""
    docs = build_documents(registry)

    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    raw_path = GENERATED_DIR / "semantic-documents.raw.jsonl"
    with raw_path.open("w", encoding="utf-8") as f:
        for d in docs:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")

    compact = [_compact(d) for d in docs]
    payload = {
        "schema_version": "0.1",
        "generated_at": _now(),
        "build_id": build_id,
        "count": len(compact),
        "note": "Dynamic Semantic Revealing search index (Phase 0+1). "
                "channels.semantic and full channels.relations are honestly "
                "False/partial — this MVP ships exact+lexical retrieval only; "
                "see /timeline/ search box. Spec: lm-001862 (動態語"
                "義顯影本地端實作白皮書).",
        "channels": {"exact": True, "lexical": True, "semantic": False, "relations": True},
        "documents": compact,
    }
    ai_dir = DIST_DIR / "ai"
    ai_dir.mkdir(parents=True, exist_ok=True)
    out_path = ai_dir / "semantic-index.min.json"
    out_text = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    out_path.write_text(out_text, encoding="utf-8")

    return {
        "count": len(docs),
        "with_summary": sum(1 for d in docs if d["summary"]),
        "with_headings": sum(1 for d in docs if d["headings"]),
        "with_related": sum(1 for d in docs if d["related_ids"]),
        "bytes": len(out_text.encode("utf-8")),
    }
