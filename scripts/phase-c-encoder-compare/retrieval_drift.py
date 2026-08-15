#!/usr/bin/env python3
"""
Phase C1 retrieval-drift step: for each oracle query, compare document- and
chunk-namespace top-k retrieval using the browser-q8 vector vs the node-q8
vector (both already upserted as temp test vectors, namespace=phase-c-test,
ids test-browser-{i}/test-nodeq8-{i} -- see compare_encoders.mjs).

"encoder drift -> retrieval drift" is what actually matters per the Phase C
handoff, not vector cosine alone -- this measures the thing that actually
matters for hybrid retrieval quality.
"""
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent
INDEX_NAME = "logic-matrix-dsrs-v1-index-v1"
COMPARISON_PATH = HERE / "comparison-2026-08-15.json"
OUT_PATH = HERE / "retrieval-drift-2026-08-15.json"

TOP_K = 10


def wrangler_query(vector_id, namespace, top_k=TOP_K):
    proc = subprocess.run(
        ["npx", "wrangler", "vectorize", "query", INDEX_NAME,
         "--vector-id", vector_id, "--namespace", namespace, "--top-k", str(top_k)],
        cwd=str(REPO_ROOT), capture_output=True, encoding="utf-8", errors="replace",
        timeout=60, shell=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"wrangler query failed for {vector_id}/{namespace}: {proc.stderr[-500:]}")
    out = proc.stdout
    start = out.index("{")
    parsed = json.loads(out[start:])
    return [m["id"] for m in parsed["matches"]]


def rank_correlation(a_ids, b_ids):
    common = [i for i in a_ids if i in b_ids]
    if len(common) < 2:
        return None
    a_ranks = {v: i for i, v in enumerate(a_ids)}
    b_ranks = {v: i for i, v in enumerate(b_ids)}
    n = len(common)
    d2 = sum((a_ranks[c] - b_ranks[c]) ** 2 for c in common)
    return 1 - (6 * d2) / (n * (n ** 2 - 1)) if n > 1 else None


def main():
    comparison = json.loads(COMPARISON_PATH.read_text(encoding="utf-8"))
    queries = [c["query"] for c in comparison["comparisons"]]

    drift = []
    for i, q in enumerate(queries):
        row = {"query": q}
        for ns in ("document", "chunk"):
            browser_ids = wrangler_query(f"test-browser-{i}", ns)
            node_ids = wrangler_query(f"test-nodeq8-{i}", ns)
            overlap = len(set(browser_ids) & set(node_ids))
            row[ns] = {
                "browser_top10": browser_ids,
                "node_q8_top10": node_ids,
                "overlap_count": overlap,
                "overlap_of_10": overlap,
                "top1_match": (browser_ids[0] if browser_ids else None) == (node_ids[0] if node_ids else None),
                "rank_correlation_on_common": rank_correlation(browser_ids, node_ids),
            }
        drift.append(row)
        print(f"[{i+1}/{len(queries)}] {q!r} doc_overlap={row['document']['overlap_count']}/10 "
              f"doc_top1_match={row['document']['top1_match']} "
              f"chunk_overlap={row['chunk']['overlap_count']}/10 "
              f"chunk_top1_match={row['chunk']['top1_match']}", file=sys.stderr)

    doc_top1_matches = sum(1 for r in drift if r["document"]["top1_match"])
    chunk_top1_matches = sum(1 for r in drift if r["chunk"]["top1_match"])
    doc_overlaps = [r["document"]["overlap_count"] for r in drift]
    chunk_overlaps = [r["chunk"]["overlap_count"] for r in drift]

    report = {
        "generated_at_note": "Phase C1 retrieval-drift, 2026-08-15",
        "index": INDEX_NAME,
        "top_k": TOP_K,
        "query_count": len(queries),
        "summary": {
            "document_top1_match_rate": f"{doc_top1_matches}/{len(queries)}",
            "chunk_top1_match_rate": f"{chunk_top1_matches}/{len(queries)}",
            "document_mean_overlap_of_10": sum(doc_overlaps) / len(doc_overlaps),
            "chunk_mean_overlap_of_10": sum(chunk_overlaps) / len(chunk_overlaps),
        },
        "per_query": drift,
    }
    OUT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nwrote {OUT_PATH}", file=sys.stderr)
    print(f"document top1 match rate: {doc_top1_matches}/{len(queries)}", file=sys.stderr)
    print(f"chunk    top1 match rate: {chunk_top1_matches}/{len(queries)}", file=sys.stderr)


if __name__ == "__main__":
    main()
