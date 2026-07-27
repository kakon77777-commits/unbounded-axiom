#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dynamic Semantic Revealing search index — Phase 0 + Phase 1 + Phase 4 relations.

Spec: content/papers/2026/2026-07/02_動態語義顯影_本地端實作技術白皮書_v0.1.md
(lm-001862). This module implements Phase 0 (data inventory ->
documents.raw.jsonl), the data side of Phase 1 (compressed static index for
the pure-frontend exact+lexical search in shell/public/semantic/), and §19's
relation index (Phase 4).

Every derived field is source-tagged per §5 of the spec:
    author_declared   — came from the paper's own YAML frontmatter
    system_inferred    — deterministic heuristic extraction (no model call)

§19.1 asks for 5 relation types. None are guessed — each comes from data
this codebase already independently verifies elsewhere:
    same_series           registry/programs/*.json iteration membership
                           (curated by a human/agent research-lineage review)
    previous_version /
    next_version           adjacent `sequence` numbers within the SAME
                           program's `iterations` array (already sorted,
                           gaps are self-declared in `integrity.missing_sequences`)
    explicit_link          registry/tcf/*.json edges that passed graph_layer.py's
                           adversarial-audit gate AND carry a verbatim
                           `external_ref` quote (one paper's own text citing
                           another) — reuses graph_layer's edge-building
                           functions directly rather than duplicating that
                           (non-trivial) verification logic. Coverage is
                           narrow (only the ~46 papers with a TCF extraction)
                           and stays honestly absent elsewhere, same as
                           same_series being absent outside a Program.
    same_primary_keyword   documents sharing the same keywords[0]. For the
                           ~98% of docs without author-declared keywords this
                           is really "first surviving title-chunk", not a
                           curated topic tag — so clusters above a sanity cap
                           are dropped rather than risk a mega-cluster from
                           an overly generic fragment (empirically the corpus
                           tops out at 12; see build note below).

Tier D is honest: every relation type is absent (never faked) for documents
it doesn't apply to.

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
from scripts.graph_layer import (
    _load_tcf_files, _concept_index, _build_edges, _load_verdicts, _gate_edges,
)

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


# Type codes used in the compact "r" list — single letters purely to keep
# dist/ai/semantic-index.min.json small; they're nested inside per-relation
# pairs (["lm-000123", "s"]) so they never collide with the compact record's
# own top-level single-letter keys (i,t,u,d,s,h,k,r,p).
REL_SAME_SERIES = "s"
REL_PREVIOUS_VERSION = "p"
REL_NEXT_VERSION = "n"
REL_EXPLICIT_LINK = "e"
REL_SAME_KEYWORD = "k"

# §19.1 priority when the SAME target doc arises from more than one relation
# source (e.g. two Program siblings that also happen to share a title-chunk
# keyword) — keep only the most-specific explanation per (doc, target) pair
# rather than listing the same target twice under different types.
# previous/next_version MUST outrank same_series: every version-adjacent pair
# is, by construction, ALSO a same_series pair (both come from the same
# Program's iterations list) — same_series covers every pair in a program,
# version-adjacency only the consecutive ones. Priority-ordering same_series
# first would let the generic relation win on literally every pair the
# specific one was meant to cover, silently discarding it every time (caught
# by inspecting real build output: zero "p"/"n" entries appeared anywhere in
# the corpus until this order was fixed).
_REL_PRIORITY = [REL_PREVIOUS_VERSION, REL_NEXT_VERSION, REL_SAME_SERIES, REL_EXPLICIT_LINK, REL_SAME_KEYWORD]

# same_primary_keyword clusters above this size almost certainly indicate an
# overly generic title-chunk (an artifact of _extract_keywords' blind regex
# chunker, not real topical similarity) rather than a real cluster — drop
# them rather than risk a mega-cluster polluting Tier D. The corpus's real
# clusters top out at 12 as of this writing, so this only ever fires on a
# genuinely degenerate fragment.
_KEYWORD_CLUSTER_MAX = 15
# Cap how many same_primary_keyword partners get RECORDED per doc even within
# an allowed cluster, so one very large-but-still-under-cap cluster doesn't
# give every member a dozen redundant relation entries.
_KEYWORD_PARTNERS_MAX = 8


def _build_version_relations() -> dict[str, list[tuple[str, str]]]:
    """previous_version/next_version — adjacent `sequence` entries within the
    SAME program's `iterations` array. Sorted defensively even though the
    2026-07-27 audit found every program file already sorted ascending with
    no duplicate sequence numbers — this must not silently misorder if a
    future program file violates that."""
    out: dict[str, list[tuple[str, str]]] = {}
    for seed in load_program_seeds():
        iters = [a for a in (seed.get("iterations") or []) if a.get("id") and a.get("sequence") is not None]
        iters.sort(key=lambda a: a["sequence"])
        for i in range(len(iters) - 1):
            prev_id, next_id = iters[i]["id"], iters[i + 1]["id"]
            if prev_id == next_id:
                continue
            out.setdefault(next_id, []).append((prev_id, REL_PREVIOUS_VERSION))
            out.setdefault(prev_id, []).append((next_id, REL_NEXT_VERSION))
    return out


def _build_explicit_link_relations(registry) -> dict[str, list[tuple[str, str]]]:
    """explicit_link — reuses graph_layer.py's own edge-building + adversarial-
    audit gate directly (rather than re-deriving "which cross-references are
    real" with separate, potentially-inconsistent logic) and keeps only edges
    carrying a verbatim `external_ref` quote — one paper's own text citing
    another — which is what "explicit" means in the relation's name; a
    `shared_concept`-only edge (co-occurrence, no direct citation) is a
    weaker signal that graph_layer.py itself already tags separately and
    isn't claimed here. Bidirectional for search purposes: if a user's query
    strongly matches either side of a citation, the other side is still a
    relevant Tier D neighbour regardless of citation direction."""
    tcfs, _errors = _load_tcf_files()
    out: dict[str, list[tuple[str, str]]] = {}
    if not tcfs:
        return out
    registry_ids = {it["id"] for it in registry["items"]}
    index = _concept_index(tcfs)
    candidates, _unresolved, _dropped = _build_edges(tcfs, index, registry_ids)
    published, _rejected, _pending = _gate_edges(candidates, _load_verdicts())
    for e in published:
        if not any(ev.get("kind") == "external_ref" for ev in (e.get("evidence") or [])):
            continue
        src, dst = e["from"], e["to"]
        if src == dst:
            continue
        out.setdefault(src, []).append((dst, REL_EXPLICIT_LINK))
        out.setdefault(dst, []).append((src, REL_EXPLICIT_LINK))
    return out


def _build_keyword_cluster_relations(keyword_by_id: dict) -> dict[str, list[tuple[str, str]]]:
    """same_primary_keyword — group by keywords[0] (see module docstring for
    why "primary" is aspirational for system_inferred keywords), skip
    clusters too large to be a real topical signal, cap partners per doc."""
    clusters: dict[str, list[str]] = {}
    for doc_id, kw in keyword_by_id.items():
        if not kw:
            continue
        clusters.setdefault(kw, []).append(doc_id)

    out: dict[str, list[tuple[str, str]]] = {}
    for kw, ids in clusters.items():
        if len(ids) < 2 or len(ids) > _KEYWORD_CLUSTER_MAX:
            continue
        ids = sorted(ids)
        for did in ids:
            partners = [x for x in ids if x != did][:_KEYWORD_PARTNERS_MAX]
            out.setdefault(did, []).extend((p, REL_SAME_KEYWORD) for p in partners)
    return out


def _merge_relations(*relation_maps: dict) -> dict[str, list[tuple[str, str]]]:
    """Combine several doc_id -> [(target, type)] maps, keeping at most one
    entry per (doc, target) pair — decided by _REL_PRIORITY, NOT by which
    map was passed first (an earlier version used "first map wins" insertion
    order, which made _REL_PRIORITY dead code: same_series was always passed
    first, so it always won regardless of the priority list's own order,
    silently discarding every previous_version/next_version entry — caught
    by inspecting real build output showing zero "p"/"n" relations anywhere
    in the corpus). Collects every candidate type per (doc, target) pair
    first, THEN picks the lowest-_REL_PRIORITY-index one, so the result is
    identical no matter what order callers pass the maps in."""
    candidates: dict[str, dict[str, list[str]]] = {}
    for rel_map in relation_maps:
        for doc_id, pairs in rel_map.items():
            bucket = candidates.setdefault(doc_id, {})
            for target, rtype in pairs:
                if target == doc_id:
                    continue
                bucket.setdefault(target, []).append(rtype)
    return {
        doc_id: sorted(
            ((target, min(types, key=_REL_PRIORITY.index)) for target, types in bucket.items()),
            key=lambda kv: (_REL_PRIORITY.index(kv[1]), kv[0]),
        )
        for doc_id, bucket in candidates.items()
    }


def build_documents(registry) -> list:
    """Phase 0: one full record (§4.1) per registry item.

    Two passes: relations can't all be built until every document's keywords
    are known (same_primary_keyword needs the full corpus's keywords[0] to
    form clusters), so pass 1 extracts everything EXCEPT relations, and pass
    2 builds the relation map (now that keywords exist) and attaches it."""
    series_map = _build_program_relations()[1]
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
            "related_ids": [],  # filled in pass 2 below
            "metadata": {
                "title_source": "author_declared",
                "summary_source": "system_inferred" if summary else "unavailable",
                "keywords_source": kw_source,
                "relation_source": None,  # filled in pass 2 below
                "confidence": round(0.6 if summary else 0.3, 2),
                "schema_version": "0.1",
                "generated_at": generated_at,
            },
        })

    keyword_by_id = {d["id"]: (d["keywords"][0] if d["keywords"] else None) for d in docs}
    relations = _merge_relations(
        {k: [(x, REL_SAME_SERIES) for x in v] for k, v in _build_program_relations()[0].items()},
        _build_version_relations(),
        _build_explicit_link_relations(registry),
        _build_keyword_cluster_relations(keyword_by_id),
    )
    for d in docs:
        pairs = relations.get(d["id"], [])
        d["related_ids"] = [{"id": target, "type": rtype} for target, rtype in pairs]
        if pairs:
            d["metadata"]["relation_source"] = "system_inferred"
    return docs


def _compact(doc: dict) -> dict:
    """§4.2 search-time compressed record — short keys, no body_text.
    "r" is now a list of [target_id, type_code] pairs (§19's 5 relation
    types — see module docstring), not a flat id list; type_code is one of
    REL_SAME_SERIES/REL_PREVIOUS_VERSION/REL_NEXT_VERSION/REL_EXPLICIT_LINK/
    REL_SAME_KEYWORD. "p" (Program label) is real curated membership from
    registry/programs/*.json — used by §20 diversity reranking's
    max_per_series_top_10 quota, null for docs outside any Program."""
    return {
        "i": doc["id"], "t": doc["title"], "u": doc["url"], "d": doc["date"],
        "s": doc["summary"], "h": doc["headings"], "k": doc["keywords"],
        "r": [[rel["id"], rel["type"]] for rel in doc["related_ids"]],
        "p": (doc["series"][0] if doc["series"] else None),
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
        "note": "Dynamic Semantic Revealing search index (Phase 0+1+2+3+4: "
                "exact/lexical retrieval, concept-dictionary query expansion, "
                "local vector search, and §19's 5-type relation index + §20 "
                "diversity reranking all live). channels.relations stays "
                "honestly partial by design — same_series/previous_version/"
                "next_version from real curated Program membership, "
                "explicit_link from graph_layer.py's adversarially-audited "
                "citation edges, same_primary_keyword from shared title-chunk "
                "clustering — never guessed, and absent (not faked) for any "
                "document none of these five apply to. See /timeline/ search "
                "box. Spec: lm-001862 (動態語義顯影本地端實作白皮書).",
        "channels": {"exact": True, "lexical": True, "dictionary": True, "semantic": True, "relations": True},
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
