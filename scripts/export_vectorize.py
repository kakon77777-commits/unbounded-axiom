#!/usr/bin/env python3
"""
Logic Matrix MCP -- Phase B step 1: deterministic export of the existing
DSRS-v1 corpus vectors into Cloudflare Vectorize-compatible NDJSON, plus a
validation + dry-run report.

Creates ZERO Cloudflare resources. Reads only local, already-committed
artifacts (registry/generated/*.f32.bin + manifests, registry/papers.json)
and writes local files under registry/generated/vectorize-export/. The
actual `wrangler vectorize create` / `wrangler vectorize insert` step is
deliberately NOT run here -- that is the real infrastructure-creation
checkpoint and belongs in a separate, explicitly-confirmed step.

Record shape and metadata-key constraints follow Cloudflare's documented
NDJSON import format (id, values, metadata; metadata keys must not contain
"." or '"' or start with "$"; max 5000 vectors per --file= import), and the
id scheme follows the Logic Matrix MCP x DSRS architecture decision doc §9
(document id = lm-XXXXXX, chunk id = "{doc_id}#chunk-{index}"), matched
against the real, already-generated chunk-embeddings-manifest.json key
format (unpadded index) rather than that doc's zero-padded illustrative
example.

See registry/embedding-profiles/dsrs-v1.json for the frozen profile this
export is derived from (embedding_space=dsrs-v1, index_profile=dsrs-index-v1).
"""
import json
import math
import struct
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GENERATED = ROOT / "registry" / "generated"
OUT_DIR = GENERATED / "vectorize-export"
PROFILE_PATH = ROOT / "registry" / "embedding-profiles" / "dsrs-v1.json"
PAPERS_PATH = ROOT / "registry" / "papers.json"

MAX_PER_FILE = 5000  # wrangler vectorize insert --file= hard limit
INVALID_KEY_CHARS = (".", '"')
PROFILE_ID = "dsrs-v1"
INDEX_PROFILE_ID = "dsrs-index-v1"


def _load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def _l2norm(vec):
    return math.sqrt(sum(x * x for x in vec))


def _check_metadata_keys(md):
    for k in md:
        if not k or k.startswith("$") or any(c in k for c in INVALID_KEY_CHARS):
            raise SystemExit(f"invalid Vectorize metadata key: {k!r}")


def _read_vectors(bin_path, dim, n):
    raw = bin_path.read_bytes()
    expect = dim * 4 * n
    if len(raw) != expect:
        raise SystemExit(f"{bin_path.name}: size {len(raw)} bytes != expected {expect} (dim={dim}, n={n})")
    for i in range(n):
        off = i * dim * 4
        yield struct.unpack_from(f"<{dim}f", raw, off)


def _write_shards(records, prefix, out_dir):
    shard_files = []
    shard = []
    shard_idx = 0

    def flush():
        nonlocal shard, shard_idx
        if not shard:
            return
        path = out_dir / f"{prefix}-{shard_idx:03d}.ndjson"
        with path.open("w", encoding="utf-8", newline="\n") as f:
            for rec in shard:
                f.write(json.dumps(rec, ensure_ascii=False, separators=(",", ":")))
                f.write("\n")
        shard_files.append({"file": path.name, "records": len(shard)})
        shard_idx += 1
        shard = []

    for rec in records:
        shard.append(rec)
        if len(shard) >= MAX_PER_FILE:
            flush()
    flush()
    return shard_files


def main():
    profile = _load_json(PROFILE_PATH)
    papers_raw = _load_json(PAPERS_PATH)
    papers_list = papers_raw["items"] if isinstance(papers_raw, dict) and "items" in papers_raw else papers_raw
    papers_by_id = {p["id"]: p for p in papers_list}

    doc_manifest = _load_json(GENERATED / "embeddings-manifest.json")
    doc_dim = doc_manifest["dim"]
    doc_ids_by_index = [None] * len(doc_manifest["docs"])
    for doc_id, info in doc_manifest["docs"].items():
        doc_ids_by_index[info["index"]] = doc_id
    if None in doc_ids_by_index:
        raise SystemExit("embeddings-manifest.json: gap in doc index assignment")

    chunk_manifest = _load_json(GENERATED / "chunk-embeddings-manifest.json")
    chunk_dim = chunk_manifest["dim"]
    chunk_keys_by_index = [None] * len(chunk_manifest["chunks"])
    for key, info in chunk_manifest["chunks"].items():
        chunk_keys_by_index[info["index"]] = key
    if None in chunk_keys_by_index:
        raise SystemExit("chunk-embeddings-manifest.json: gap in chunk index assignment")

    if doc_dim != chunk_dim:
        raise SystemExit(f"dimension mismatch: doc={doc_dim} chunk={chunk_dim}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # ---- documents ----
    doc_records = []
    zero_doc_count = 0
    doc_norm_samples = []
    for i, vec in enumerate(_read_vectors(GENERATED / "embeddings.f32.bin", doc_dim, len(doc_ids_by_index))):
        doc_id = doc_ids_by_index[i]
        norm = _l2norm(vec)
        if norm < 1e-9:
            zero_doc_count += 1
        if i % 400 == 0:
            doc_norm_samples.append(round(norm, 6))
        paper = papers_by_id.get(doc_id, {})
        md = {"paper_id": doc_id, "type": "document", "profile_id": PROFILE_ID}
        if paper.get("title"):
            md["title"] = paper["title"][:500]
        if paper.get("canonical_url"):
            md["url"] = paper["canonical_url"]
        if paper.get("language"):
            md["language"] = paper["language"]
        if paper.get("year"):
            md["year"] = paper["year"]
        _check_metadata_keys(md)
        # Values rounded to 8 decimal places: a normalized (L2=1) component
        # lies in [-1, 1], so 8 decimals preserves float32's ~7 significant
        # digits in full while keeping the NDJSON text compact -- a
        # documented, deliberate choice, not silent lossy truncation.
        doc_records.append({"id": doc_id, "values": [round(x, 8) for x in vec], "metadata": md})

    # ---- chunks ----
    chunk_records = []
    zero_chunk_count = 0
    chunk_norm_samples = []
    for i, vec in enumerate(_read_vectors(GENERATED / "chunk-embeddings.f32.bin", chunk_dim, len(chunk_keys_by_index))):
        key = chunk_keys_by_index[i]  # e.g. "lm-000001#chunk-0"
        info = chunk_manifest["chunks"][key]
        doc_id = info["doc_id"]
        norm = _l2norm(vec)
        if norm < 1e-9:
            zero_chunk_count += 1
        if i % 2000 == 0:
            chunk_norm_samples.append(round(norm, 6))
        md = {
            "paper_id": doc_id,
            "chunk_id": key.split("#", 1)[1],
            "type": "chunk",
            "profile_id": PROFILE_ID,
        }
        if info.get("heading"):
            md["heading"] = info["heading"][:200]
        paper = papers_by_id.get(doc_id, {})
        if paper.get("language"):
            md["language"] = paper["language"]
        if paper.get("year"):
            md["year"] = paper["year"]
        _check_metadata_keys(md)
        chunk_records.append({"id": key, "values": [round(x, 8) for x in vec], "metadata": md})

    all_ids = [r["id"] for r in doc_records] + [r["id"] for r in chunk_records]
    dup_count = len(all_ids) - len(set(all_ids))

    doc_shards = _write_shards(doc_records, "docs", OUT_DIR)
    chunk_shards = _write_shards(chunk_records, "chunks", OUT_DIR)

    idx_profile = profile.get("index_profile", {})
    profile_consistency = {
        "document_vectors_profile_says": idx_profile.get("document_vectors"),
        "document_vectors_actual": len(doc_records),
        "chunk_vectors_profile_says": idx_profile.get("chunk_vectors"),
        "chunk_vectors_actual": len(chunk_records),
        "matches": (
            idx_profile.get("document_vectors") == len(doc_records)
            and idx_profile.get("chunk_vectors") == len(chunk_records)
        ),
    }

    report = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "purpose": "Phase B step 1 (deterministic export) for Logic Matrix MCP x DSRS. Zero Cloudflare resources created -- local NDJSON only.",
        "source_profile": {"embedding_space": PROFILE_ID, "index_profile": INDEX_PROFILE_ID},
        "profile_consistency": profile_consistency,
        "counts": {
            "documents_exported": len(doc_records),
            "documents_expected_from_manifest": len(doc_manifest["docs"]),
            "chunks_exported": len(chunk_records),
            "chunks_expected_from_manifest": len(chunk_manifest["chunks"]),
        },
        "validation": {
            "dimension": doc_dim,
            "documents_count_matches_manifest": len(doc_records) == len(doc_manifest["docs"]),
            "chunks_count_matches_manifest": len(chunk_records) == len(chunk_manifest["chunks"]),
            "zero_norm_documents": zero_doc_count,
            "zero_norm_chunks": zero_chunk_count,
            "zero_norm_expected": 0,
            "zero_norm_note": "0 expected -- registry/generated/*.f32.bin never contains the dist/-only zero-padding vector (see dsrs-v1.json index_profile.zero_vector_policy). A nonzero count here means the wrong source file was read.",
            "duplicate_id_count_across_doc_and_chunk_namespace": dup_count,
            "document_l2_norm_samples": doc_norm_samples,
            "chunk_l2_norm_samples": chunk_norm_samples,
            "metadata_keys_validated": "no '.', no '\"', no leading '$' (Vectorize constraint) -- checked per record during export, script aborts on violation",
        },
        "output": {
            "max_records_per_ndjson_file": MAX_PER_FILE,
            "document_shards": doc_shards,
            "chunk_shards": chunk_shards,
            "not_committed_to_git": "*.ndjson under this directory is gitignored (regenerable, ~tens of MB of JSON text); this report (dry_run_manifest.json) is committed as the durable evidence this step ran.",
        },
        "next_step_not_taken": "wrangler vectorize create / wrangler vectorize insert -- deliberately not run by this script. Requires an explicit go-ahead (creates persistent, billable Cloudflare infrastructure).",
    }
    (OUT_DIR / "dry_run_manifest.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    summary = [
        f"documents: {len(doc_records)}/{len(doc_manifest['docs'])} exported, {zero_doc_count} zero-norm, {len(doc_shards)} shard(s)",
        f"chunks: {len(chunk_records)}/{len(chunk_manifest['chunks'])} exported, {zero_chunk_count} zero-norm, {len(chunk_shards)} shard(s)",
        f"duplicate ids across doc+chunk id space: {dup_count}",
        f"profile_consistency.matches: {profile_consistency['matches']}",
        f"output dir: {OUT_DIR}",
    ]
    print("\n".join(summary))
    if zero_doc_count or zero_chunk_count or dup_count or not profile_consistency["matches"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
