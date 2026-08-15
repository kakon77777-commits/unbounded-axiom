#!/usr/bin/env python3
"""
Phase C1.2: Exact Retrieval Drift Isolation.

retrieval_drift.py's 29/30 chunk-namespace result went through Vectorize's
DEFAULT (approximate) scoring -- it answers "how much does the real
production path differ end to end," but conflates two variables: encoder
drift (browser-q8 vs node-q8) and Vectorize's ANN approximation. This script
removes the second variable entirely: exact cosine, computed locally against
the full corpus (registry/generated/*.f32.bin), zero Cloudflare involvement.
"""
import json
import math
import struct
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent
GENERATED = REPO_ROOT / "registry" / "generated"
TESTVEC_PATH = HERE / "test-vectors-2026-08-15.ndjson"
OUT_PATH = HERE / "c1_2-exact-drift-2026-08-15.json"

TOP_K = 10


def load_corpus_vectors(bin_path, manifest_path, id_key):
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    dim = manifest["dim"]
    items = manifest[id_key]
    ids_by_index = [None] * len(items)
    for k, info in items.items():
        ids_by_index[info["index"]] = k
    raw = bin_path.read_bytes()
    n = len(ids_by_index)
    matrix = np.frombuffer(raw, dtype="<f4", count=n * dim).reshape(n, dim).astype(np.float64)
    return ids_by_index, matrix, dim


def top_k_exact(query_vec, ids_by_index, matrix, k):
    q = np.asarray(query_vec, dtype=np.float64)
    qn = np.linalg.norm(q)
    mn = np.linalg.norm(matrix, axis=1)
    denom = qn * mn
    denom[denom == 0] = 1.0  # avoid div-by-zero; those rows' dot product is 0 anyway
    scores = (matrix @ q) / denom
    top_idx = np.argsort(-scores)[:k]
    return [(ids_by_index[i], round(float(scores[i]), 8)) for i in top_idx]


def rank_correlation(a_ids, b_ids):
    common = [i for i in a_ids if i in b_ids]
    if len(common) < 2:
        return None
    a_ranks = {v: i for i, v in enumerate(a_ids)}
    b_ranks = {v: i for i, v in enumerate(b_ids)}
    n = len(common)
    d2 = sum((a_ranks[c] - b_ranks[c]) ** 2 for c in common)
    return 1 - (6 * d2) / (n * (n ** 2 - 1))


def main():
    doc_ids, doc_vecs, doc_dim = load_corpus_vectors(
        GENERATED / "embeddings.f32.bin", GENERATED / "embeddings-manifest.json", "docs")
    chunk_ids, chunk_vecs, chunk_dim = load_corpus_vectors(
        GENERATED / "chunk-embeddings.f32.bin", GENERATED / "chunk-embeddings-manifest.json", "chunks")
    print(f"loaded {len(doc_ids)} doc vectors (dim={doc_dim}), {len(chunk_ids)} chunk vectors (dim={chunk_dim})")

    test_vectors = {}
    for line in TESTVEC_PATH.read_text(encoding="utf-8").splitlines():
        rec = json.loads(line)
        test_vectors[rec["id"]] = rec

    n_queries = len([k for k in test_vectors if k.startswith("test-browser-")])
    results = []
    for i in range(n_queries):
        browser_rec = test_vectors[f"test-browser-{i}"]
        node_rec = test_vectors[f"test-nodeq8-{i}"]
        query = browser_rec["metadata"]["query"]
        browser_vec = browser_rec["values"]
        node_vec = node_rec["values"]

        row = {"query": query}
        for label, ids_by_index, vecs in (("document", doc_ids, doc_vecs), ("chunk", chunk_ids, chunk_vecs)):
            browser_top = top_k_exact(browser_vec, ids_by_index, vecs, TOP_K)
            node_top = top_k_exact(node_vec, ids_by_index, vecs, TOP_K)
            browser_top_ids = [t[0] for t in browser_top]
            node_top_ids = [t[0] for t in node_top]
            overlap = len(set(browser_top_ids) & set(node_top_ids))
            row[label] = {
                "browser_top10": browser_top,
                "node_q8_top10": node_top,
                "overlap_count": overlap,
                "top1_match": browser_top_ids[0] == node_top_ids[0] if browser_top_ids and node_top_ids else None,
                "rank_correlation_on_common": rank_correlation(browser_top_ids, node_top_ids),
            }
        results.append(row)
        print(f"[{i+1}/{n_queries}] {query!r} doc_overlap={row['document']['overlap_count']}/10 "
              f"doc_top1={row['document']['top1_match']} chunk_overlap={row['chunk']['overlap_count']}/10 "
              f"chunk_top1={row['chunk']['top1_match']}")

    doc_top1 = sum(1 for r in results if r["document"]["top1_match"])
    chunk_top1 = sum(1 for r in results if r["chunk"]["top1_match"])
    doc_overlaps = [r["document"]["overlap_count"] for r in results]
    chunk_overlaps = [r["chunk"]["overlap_count"] for r in results]

    report = {
        "purpose": "Phase C1.2: exact (non-ANN) cosine sweep against the full local corpus, isolating encoder drift (browser-q8 vs node-q8) from Vectorize's approximate ANN scoring. Zero Cloudflare calls.",
        "corpus_size": {"documents": len(doc_ids), "chunks": len(chunk_ids)},
        "top_k": TOP_K,
        "query_count": n_queries,
        "summary": {
            "document_top1_match_rate": f"{doc_top1}/{n_queries}",
            "chunk_top1_match_rate": f"{chunk_top1}/{n_queries}",
            "document_mean_overlap_of_10": sum(doc_overlaps) / len(doc_overlaps),
            "chunk_mean_overlap_of_10": sum(chunk_overlaps) / len(chunk_overlaps),
        },
        "per_query": results,
    }
    OUT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nwrote {OUT_PATH}")
    print(f"document top1 match rate (exact): {doc_top1}/{n_queries}")
    print(f"chunk    top1 match rate (exact): {chunk_top1}/{n_queries}")


if __name__ == "__main__":
    main()
