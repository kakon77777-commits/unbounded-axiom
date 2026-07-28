#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dynamic Semantic Revealing search index — Phase 5 chunk-level vectors.

Spec: content/papers/2026/2026-07/02_動態語義顯影_本地端實作技術白皮書_v0.1.md
(lm-001862), §17.2 ("若後續加入全文，再建立 chunk 向量") / §17.3 (aggregation:
MVP uses max_j M(chunk_j, query)) / §26 Phase 5 ("建立 chunk").

Phase 3's document-level vector (title + summary + headings, see
build_embeddings.py) captures what a paper is ABOUT; it can't tell you WHICH
passage matches a specific query in a 15,000-character paper. This adds a
second, complementary vector set — one per section — so the client can also
surface "this specific paragraph is the match" precision, aggregated back to
a per-document score via a simple max (the spec's own stated MVP choice over
weighted top-K, to avoid one accidental over-broad section dominating).

Chunking: a corpus-wide sample found headings wildly uneven -- 44% of docs
have ZERO markdown headings at all, while others range up to 117 -- so this
can't just be "one chunk per ## heading". Instead: extract natural text
units (heading-delimited sections where headings exist, paragraph breaks
otherwise), then greedily bucket them by cumulative length into AT MOST
MAX_CHUNKS_PER_DOC buckets, preserving document order. This bounds the
corpus-wide chunk count (a 117-heading paper still produces at most 6 chunks,
not 117) while a normal 3-8-section paper gets close to one chunk per
section. Each chunk's embedded text is capped at MAX_CHUNK_CHARS so the
embedding input stays a reasonable, consistent size regardless of how much
raw text a bucket accumulated.

Storage mirrors build_embeddings.py exactly (see that file's docstring for
the two-tier persisted-vs-deployed reasoning): registry/generated/ holds the
canonical, git-tracked, incrementally-updated (content-hash per CHUNK, not
per document -- editing one section shouldn't force re-embedding a whole
15,000-character paper's other five chunks) vectors; dist/ai/ holds the
per-build re-emitted deploy asset, plus a parallel doc-id-per-chunk array so
the client can aggregate chunk hits back to a document without a separate
lookup table.
"""
import hashlib
import json
import os
import re
import struct
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.config import ROOT, PAPERS_DIR, DIST_DIR
from scripts.render import extract_raw_text
from scripts.semantic_layer import _parse_frontmatter, MD_STRIP_RE

GENERATED_DIR = ROOT / "registry" / "generated"
MANIFEST_PATH = GENERATED_DIR / "chunk-embeddings-manifest.json"
BINARY_PATH = GENERATED_DIR / "chunk-embeddings.f32.bin"

MODEL_NAME = "BAAI/bge-small-zh-v1.5"
ONNX_MODEL_NAME = "Xenova/bge-small-zh-v1.5"
DIM = 512
QUERY_INSTRUCTION = "为这个句子生成表示以用于检索相关文章："

MAX_CHUNKS_PER_DOC = 6
MAX_CHUNK_CHARS = 800
MIN_CHUNK_CHARS = 30  # shorter than this isn't worth its own embedding call

SECTION_HEADING_RE = re.compile(r"^(#{2,3})\s+(.+?)\s*$", re.MULTILINE)
PARA_SPLIT_RE = re.compile(r"\n\s*\n")


def _now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _clean(text: str) -> str:
    text = MD_STRIP_RE.sub("", text)
    return re.sub(r"\s+", " ", text).strip()


def _extract_units(body: str) -> list:
    """(heading_or_None, text) per natural unit -- heading-delimited section
    if the doc has any ##/### headings, else paragraph-delimited."""
    headings = list(SECTION_HEADING_RE.finditer(body))
    units = []
    if headings:
        # content before the first heading, if any, is still real text
        if headings[0].start() > 0:
            pre = _clean(body[: headings[0].start()])
            if len(pre) >= MIN_CHUNK_CHARS:
                units.append((None, pre))
        for i, hm in enumerate(headings):
            start = hm.end()
            end = headings[i + 1].start() if i + 1 < len(headings) else len(body)
            heading_text = _clean(hm.group(2))
            content = _clean(body[start:end])
            if content or heading_text:
                units.append((heading_text or None, content))
    else:
        for para in PARA_SPLIT_RE.split(body):
            cleaned = _clean(para)
            if len(cleaned) >= MIN_CHUNK_CHARS:
                units.append((None, cleaned))
    return units


def _bucket_units(units: list) -> list:
    """Greedy length-balanced grouping into <= MAX_CHUNKS_PER_DOC buckets,
    preserving order. Returns [(heading_or_None, joined_text), ...].

    A bucket's heading is whichever unit's heading was the FIRST one actually
    placed into THAT bucket -- decided only once the flush decision for the
    incoming unit has already been made, not "peeked" from the incoming unit
    before deciding whether it even joins the current bucket. Getting this
    order backwards (checking the incoming unit's heading before the flush
    check) silently mislabels the case that matters most: a document that
    opens with real pre-heading content (an intro/abstract paragraph before
    its first `##`) gets that intro merged into the SAME decision step as
    the first real heading, so the intro's bucket inherits that heading's
    name instead of staying `None` (see build/chunk.py in the DRVS package,
    where this exact bug was caught by a test)."""
    if not units:
        return []
    total_len = sum(len(t) for _, t in units)
    target = max(1, total_len // MAX_CHUNKS_PER_DOC)

    buckets = []
    cur_heading = None
    cur_heading_set = False
    cur_parts = []
    cur_len = 0
    for heading, text in units:
        if cur_parts and cur_len + len(text) > target and len(buckets) < MAX_CHUNKS_PER_DOC - 1:
            buckets.append((cur_heading, " ".join(cur_parts)))
            cur_heading, cur_heading_set, cur_parts, cur_len = None, False, [], 0
        if not cur_heading_set and heading:
            cur_heading = heading
            cur_heading_set = True
        cur_parts.append(text)
        cur_len += len(text)
    if cur_parts:
        buckets.append((cur_heading, " ".join(cur_parts)))
    return buckets[:MAX_CHUNKS_PER_DOC]


def _chunk_text(doc_title: str, heading, body_text: str) -> str:
    """What actually gets embedded -- title context + section heading (if
    any) + the section's own text, so a chunk embedded in isolation still
    carries which paper/section it's from (matters for short chunks whose
    own text alone is ambiguous)."""
    prefix = doc_title if not heading else f"{doc_title} — {heading}"
    text = f"{prefix}\n{body_text}"
    return text[:MAX_CHUNK_CHARS]


def _content_hash(text: str) -> str:
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def build_chunks_for_doc(doc_id: str, title: str, source_file: str, ext: str) -> list:
    """Returns [{"chunk_id", "heading", "text"}] for one document."""
    src = ROOT / source_file
    if not src.exists():
        return []
    try:
        raw_text = extract_raw_text(src, ext).lstrip("﻿")
    except Exception:
        return []
    _fm, body = _parse_frontmatter(raw_text)
    if not body:
        return []
    units = _extract_units(body)
    buckets = _bucket_units(units)
    chunks = []
    for i, (heading, text) in enumerate(buckets):
        if len(text) < MIN_CHUNK_CHARS:
            continue
        chunks.append({
            "chunk_id": f"{doc_id}#chunk-{i}",
            "heading": heading,
            "text": _chunk_text(title, heading, text),
        })
    return chunks


def _load_manifest() -> dict:
    if MANIFEST_PATH.exists():
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    return {"model": MODEL_NAME, "dim": DIM, "chunks": {}}


def _load_persisted_vectors(manifest: dict) -> dict:
    if not BINARY_PATH.exists():
        return {}
    raw = BINARY_PATH.read_bytes()
    vectors = {}
    for chunk_id, info in manifest.get("chunks", {}).items():
        off = info["index"] * DIM * 4
        if off + DIM * 4 > len(raw):
            continue
        vectors[chunk_id] = struct.unpack_from(f"<{DIM}f", raw, off)
    return vectors


def build_chunk_embeddings(registry, build_id=None, force: bool = False) -> dict:
    manifest = _load_manifest()
    old_meta = manifest.get("chunks", {})
    old_vectors = _load_persisted_vectors(manifest)

    all_chunks = {}  # chunk_id -> {heading, text, doc_id}
    for it in registry["items"]:
        doc_chunks = build_chunks_for_doc(it["id"], it["title"], it["source_file"], it.get("ext", "md"))
        for c in doc_chunks:
            all_chunks[c["chunk_id"]] = {"heading": c["heading"], "text": c["text"], "doc_id": it["id"]}

    hashes_by_id = {cid: _content_hash(c["text"]) for cid, c in all_chunks.items()}
    to_embed = [
        cid for cid in all_chunks
        if force or cid not in old_vectors or old_meta.get(cid, {}).get("hash") != hashes_by_id[cid]
    ]

    vectors = dict(old_vectors)
    if to_embed:
        print(f"[semantic] embedding {len(to_embed)} new/changed chunk(s) with {MODEL_NAME} ...")
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer(MODEL_NAME)
        batch_texts = [all_chunks[cid]["text"] for cid in to_embed]
        encoded = model.encode(batch_texts, normalize_embeddings=True, show_progress_bar=False, batch_size=32)
        for cid, vec in zip(to_embed, encoded):
            vectors[cid] = tuple(float(x) for x in vec)

    final_ids = sorted(cid for cid in all_chunks if cid in vectors)
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    packed = bytearray()
    manifest_chunks = {}
    for idx, cid in enumerate(final_ids):
        packed += struct.pack(f"<{DIM}f", *vectors[cid])
        manifest_chunks[cid] = {
            "hash": hashes_by_id[cid], "index": idx,
            "doc_id": all_chunks[cid]["doc_id"], "heading": all_chunks[cid]["heading"],
        }
    BINARY_PATH.write_bytes(bytes(packed))
    MANIFEST_PATH.write_text(json.dumps({
        "model": MODEL_NAME, "onnx_model": ONNX_MODEL_NAME, "dim": DIM,
        "query_instruction": QUERY_INSTRUCTION, "generated_at": _now(),
        "max_chunks_per_doc": MAX_CHUNKS_PER_DOC,
        "chunks": manifest_chunks,
    }, ensure_ascii=False, indent=1), encoding="utf-8")

    # Deploy asset: vectors + parallel doc_id/heading arrays (same order) so
    # the client can aggregate max-per-document without a separate id lookup,
    # AND can tell the user WHICH section matched (§15 hit-reason UI must
    # name a real field, never just say "AI thinks so" — showing "chunk N of
    # doc X matched" without naming what chunk N actually IS would be exactly
    # that opaque non-answer).
    dist_packed = bytearray()
    doc_ids = []
    headings = []
    for cid in final_ids:
        dist_packed += struct.pack(f"<{DIM}f", *vectors[cid])
        doc_ids.append(all_chunks[cid]["doc_id"])
        headings.append(all_chunks[cid]["heading"])
    ai_dir = DIST_DIR / "ai"
    ai_dir.mkdir(parents=True, exist_ok=True)
    (ai_dir / "semantic-chunks.bin").write_bytes(bytes(dist_packed))
    (ai_dir / "semantic-chunks-meta.json").write_text(json.dumps({
        "schema_version": "0.1", "generated_at": _now(), "build_id": build_id,
        "model": ONNX_MODEL_NAME, "dim": DIM, "query_instruction": QUERY_INSTRUCTION,
        "count": len(final_ids), "docs_covered": len(set(doc_ids)),
        "max_chunks_per_doc": MAX_CHUNKS_PER_DOC,
        "doc_ids": doc_ids,
        "headings": headings,
        "note": "Phase 5 chunk-level vectors (§17.2/§17.3). doc_ids[i]/"
                "headings[i] describe the document/section chunk vector i "
                "belongs to (headings[i] is null for a paragraph-fallback "
                "chunk with no markdown heading) -- aggregate to a "
                "per-document score via max(chunk similarities) per §17.3's "
                "MVP formula. Complementary to semantic-vectors.bin (whole-"
                "document title+summary+headings): this set captures WHICH "
                "passage matched, not just that some part of the doc did.",
    }, ensure_ascii=False), encoding="utf-8")

    return {
        "total_docs": len(registry["items"]),
        "docs_with_chunks": len(set(all_chunks[cid]["doc_id"] for cid in all_chunks)),
        "total_chunks": len(final_ids),
        "embedded_now": len(to_embed),
        "bytes": len(dist_packed),
    }


if __name__ == "__main__":
    reg = json.loads((ROOT / "registry" / "papers.json").read_text(encoding="utf-8"))
    stats = build_chunk_embeddings(reg, build_id="manual-run", force="--force" in sys.argv)
    print(json.dumps(stats, ensure_ascii=False, indent=2))
