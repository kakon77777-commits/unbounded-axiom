#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dynamic Semantic Revealing search index — Phase 3 (local vector search).

Spec: content/papers/2026/2026-07/02_動態語義顯影_本地端實作技術白皮書_v0.1.md
(lm-001862), §16.2 API-enhanced mode / §17 vector index scheme / §18.3
incremental update. Phase 3 goal per §26: "建立文件級嵌入；API 回傳語義結果；
加入 C 級顯示" (build document-level embeddings; an API returns semantic
results; add Tier-C display).

This site is 100% static (Cloudflare Workers Static Assets, dist/ rebuilt
from scratch every run — see build.py's shutil.rmtree(DIST_DIR)), and §16.1
already establishes a strong "pure frontend, no server" precedent that every
prior phase followed. Rather than stand up a real networked API (§16.2's
literal framing) or add a Cloudflare Workers AI binding (a new account-level
infra dependency), Phase 3 keeps the same shape everything else uses: the
"API" becomes in-browser WASM inference (@huggingface/transformers, ONNX
runtime) running in the existing lexical-search-worker.js, comparing the
query vector against these PRE-COMPUTED document vectors. Same effect —
exact search never depends on it, and it degrades to exact+lexical+dictionary
results if the model fails to load — without a new server component.

Model: BAAI/bge-small-zh-v1.5 — a Chinese-specific (not diluted-multilingual)
BGE embedding model, chosen after sampling actual corpus retrieval quality
(strong topical clustering with zero lexical overlap, e.g. "人工智慧的自我
意識問題" correctly surfaces AI-consciousness papers that share no keywords
with the query). Its ONNX int8 export (Xenova/bge-small-zh-v1.5) is ~23MB,
versus ~113MB for the smallest viable multilingual alternative — the
Python (this script) and JS (lexical-search-worker.js) sides MUST use the
same underlying model or their vectors live in incompatible spaces.
BGE's own convention (confirmed against the model card): documents are
encoded with NO instruction prefix; only the QUERY gets one at search time
("为这个句子生成表示以用于检索相关文章："). Raw cosine values are not
comparable to a fixed absolute threshold — BGE's own docs note ">0.5" does
NOT mean "similar"; only relative ranking is meaningful, so scoreCorpus
must rank/normalize this channel rather than gate it on an absolute cutoff.

Embedding input follows §17.2 exactly: title + "\n" + summary + "\n" +
headings (reusing semantic_layer.build_documents' already-extracted fields,
rather than re-deriving them, so the embedded text always matches what
Phase 0/1 already show as the document's summary/headings).

Storage (two-tier, matching every other generator in this codebase):
    registry/generated/embeddings-manifest.json   doc_id -> {hash, index}
    registry/generated/embeddings.f32.bin          packed float32 vectors,
                                                     canonical sorted-by-id
                                                     order, persisted/git-
                                                     tracked so re-running a
                                                     build never re-embeds
                                                     unchanged documents
                                                     (§18.3)
    dist/ai/semantic-vectors.bin                    same vectors, RE-ORDERED
                                                     to match registry["items"]
                                                     iteration order (i.e.
                                                     semantic-index.min.json's
                                                     "documents" array) so the
                                                     frontend needs no extra
                                                     id->offset lookup — vector
                                                     i belongs to documents[i].
                                                     Rebuilt every run (dist/
                                                     is wiped each build) but
                                                     cheap: no model load
                                                     unless embeddings-manifest
                                                     actually changed.
    dist/ai/semantic-vectors-meta.json              model name, dim, query
                                                     instruction, build_id.

A document with no summary/headings/title text to embed gets an all-zero
vector in the dist/ output (never a crash) — the JS scorer must treat a
zero-norm vector as similarity 0, not divide-by-zero.
"""
import hashlib
import json
import os
import struct
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.config import ROOT, DIST_DIR
from scripts.semantic_layer import build_documents

GENERATED_DIR = ROOT / "registry" / "generated"
MANIFEST_PATH = GENERATED_DIR / "embeddings-manifest.json"
BINARY_PATH = GENERATED_DIR / "embeddings.f32.bin"

MODEL_NAME = "BAAI/bge-small-zh-v1.5"
ONNX_MODEL_NAME = "Xenova/bge-small-zh-v1.5"
DIM = 512
QUERY_INSTRUCTION = "为这个句子生成表示以用于检索相关文章："


def _now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _embed_text(doc: dict) -> str:
    parts = [doc["title"], doc["summary"]] + doc["headings"]
    return "\n".join(p for p in parts if p)


def _content_hash(text: str) -> str:
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def _load_manifest() -> dict:
    if MANIFEST_PATH.exists():
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    return {"model": MODEL_NAME, "dim": DIM, "docs": {}}


def _load_persisted_vectors(manifest: dict) -> dict:
    if not BINARY_PATH.exists():
        return {}
    raw = BINARY_PATH.read_bytes()
    vectors = {}
    for doc_id, info in manifest.get("docs", {}).items():
        off = info["index"] * DIM * 4
        if off + DIM * 4 > len(raw):
            continue  # stale manifest/binary mismatch -> treat as missing, will re-embed
        vectors[doc_id] = struct.unpack_from(f"<{DIM}f", raw, off)
    return vectors


def build_embeddings(registry, build_id=None, force: bool = False) -> dict:
    docs = build_documents(registry)
    manifest = _load_manifest()
    old_docs_meta = manifest.get("docs", {})
    old_vectors = _load_persisted_vectors(manifest)

    texts_by_id, hashes_by_id = {}, {}
    for d in docs:
        text = _embed_text(d)
        if not text.strip():
            continue
        texts_by_id[d["id"]] = text
        hashes_by_id[d["id"]] = _content_hash(text)

    to_embed = [
        doc_id for doc_id, h in hashes_by_id.items()
        if force or doc_id not in old_vectors or old_docs_meta.get(doc_id, {}).get("hash") != h
    ]

    vectors = dict(old_vectors)
    if to_embed:
        print(f"[semantic] embedding {len(to_embed)} new/changed document(s) with {MODEL_NAME} ...")
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer(MODEL_NAME)
        batch_texts = [texts_by_id[i] for i in to_embed]
        encoded = model.encode(batch_texts, normalize_embeddings=True, show_progress_bar=False, batch_size=32)
        for doc_id, vec in zip(to_embed, encoded):
            vectors[doc_id] = tuple(float(x) for x in vec)

    # Canonical persisted storage: sorted doc_id order, only docs that still
    # have embeddable text AND a vector (covers both "newly embedded" and
    # "reused from before" — never re-derives what didn't change).
    final_ids = sorted(i for i in texts_by_id if i in vectors)
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    packed = bytearray()
    manifest_docs = {}
    for idx, doc_id in enumerate(final_ids):
        packed += struct.pack(f"<{DIM}f", *vectors[doc_id])
        manifest_docs[doc_id] = {"hash": hashes_by_id[doc_id], "index": idx}
    BINARY_PATH.write_bytes(bytes(packed))
    MANIFEST_PATH.write_text(json.dumps({
        "model": MODEL_NAME,
        "onnx_model": ONNX_MODEL_NAME,
        "dim": DIM,
        "query_instruction": QUERY_INSTRUCTION,
        "generated_at": _now(),
        "docs": manifest_docs,
    }, ensure_ascii=False, indent=1), encoding="utf-8")

    # dist/ output: same vectors, re-ordered to match registry["items"] (the
    # same iteration order semantic_layer.py uses for semantic-index.min.json's
    # "documents" array) so the frontend can use one shared index, no id map.
    dist_packed = bytearray()
    covered = 0
    for it in registry["items"]:
        vec = vectors.get(it["id"])
        if vec is None:
            vec = (0.0,) * DIM
        else:
            covered += 1
        dist_packed += struct.pack(f"<{DIM}f", *vec)
    ai_dir = DIST_DIR / "ai"
    ai_dir.mkdir(parents=True, exist_ok=True)
    (ai_dir / "semantic-vectors.bin").write_bytes(bytes(dist_packed))
    meta_text = json.dumps({
        "schema_version": "0.1",
        "generated_at": _now(),
        "build_id": build_id,
        "model": ONNX_MODEL_NAME,
        "dim": DIM,
        "query_instruction": QUERY_INSTRUCTION,
        "count": len(registry["items"]),
        "covered": covered,
        "note": "Phase 3 document-level vectors (BAAI/bge-small-zh-v1.5, "
                "512-dim, L2-normalized). Vector i corresponds to "
                "semantic-index.min.json's documents[i] -- same iteration "
                "order, no separate id map needed. A document with no "
                "summary/headings/title text has an all-zero vector; treat "
                "zero-norm as similarity 0, never divide by its norm.",
    }, ensure_ascii=False)
    (ai_dir / "semantic-vectors-meta.json").write_text(meta_text, encoding="utf-8")

    return {
        "total": len(registry["items"]),
        "embeddable": len(texts_by_id),
        "embedded_now": len(to_embed),
        "covered": covered,
        "bytes": len(dist_packed),
    }


if __name__ == "__main__":
    # Standalone/manual run: reuse the already-built registry.json rather than
    # re-scanning the corpus (build.py passes the in-memory registry directly
    # when calling build_embeddings() as part of the normal build).
    reg = json.loads((ROOT / "registry" / "papers.json").read_text(encoding="utf-8"))
    stats = build_embeddings(reg, build_id="manual-run", force="--force" in sys.argv)
    print(json.dumps(stats, ensure_ascii=False, indent=2))
