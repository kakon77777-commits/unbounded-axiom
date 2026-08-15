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

Record shape and constraints follow Cloudflare's current documented
Vectorize limits (id <=64 UTF-8 bytes; metadata <=10KiB/vector; metadata
keys must not contain "." or '"' or start with "$"; Cloudflare recommends
<=5000 vectors per NDJSON upload file to avoid its API's global rate
limit; max 100MB per upload) -- all checked per record/shard, not assumed.
Doc and chunk vectors are written to separate Vectorize `namespace`s
(document/chunk): namespace filtering is applied BEFORE the ANN search,
so this preserves the same doc/chunk-are-separate-candidate-pools
structure the browser's DSRS already uses (index_profile.doc_chunk_
aggregation), rather than letting the far more numerous chunk vectors
dominate top-K in one flat pool. The id scheme follows the Logic Matrix
MCP x DSRS architecture decision doc §9 (document id = lm-XXXXXX, chunk
id = "{doc_id}#chunk-{index}"), matched against the real, already-
generated chunk-embeddings-manifest.json key format (unpadded index)
rather than that doc's zero-padded illustrative example.

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

MAX_PER_FILE = 5000  # Cloudflare-recommended max vectors per NDJSON upload file
                      # (not a hard limit; stated purpose is avoiding the Cloudflare
                      # API's global rate limit during `wrangler vectorize insert`)
MAX_ID_BYTES = 64        # Vectorize platform limit, vector id (UTF-8 bytes)
MAX_METADATA_BYTES = 10 * 1024  # Vectorize platform limit, metadata per vector
MAX_SHARD_BYTES = 100 * 1024 * 1024  # Vectorize platform limit, max upload size
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


def _check_id_length(vector_id):
    n = len(vector_id.encode("utf-8"))
    if n > MAX_ID_BYTES:
        raise SystemExit(f"vector id exceeds {MAX_ID_BYTES} bytes ({n}): {vector_id!r}")


def _check_metadata_size(md, vector_id):
    n = len(json.dumps(md, ensure_ascii=False).encode("utf-8"))
    if n > MAX_METADATA_BYTES:
        raise SystemExit(f"metadata for {vector_id!r} exceeds {MAX_METADATA_BYTES} bytes ({n})")


def _roundtrip_check(vec, values_json_str):
    """True bitwise float32 round-trip: source float32 vs NDJSON-serialize/parse/
    cast float32, for every component, compared as raw bytes -- not value equality.
    Value equality (`==`/`!=` on the unpacked floats) is NOT the same check: it
    silently misses a +0.0-vs--0.0 bit-pattern flip (0.0 == -0.0 is True) and
    false-positives on an identical-bit-pattern NaN (nan != nan is True even for
    the same bits). Comparing struct.pack(...) output directly avoids both."""
    parsed = json.loads(values_json_str)
    mismatches = 0
    for x, p in zip(vec, parsed):
        if struct.pack("<f", x) != struct.pack("<f", p):
            mismatches += 1
    return mismatches


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
        size = path.stat().st_size
        if size > MAX_SHARD_BYTES:
            raise SystemExit(f"{path.name}: {size} bytes exceeds Vectorize's {MAX_SHARD_BYTES}-byte upload limit")
        shard_files.append({"file": path.name, "records": len(shard), "bytes": size})
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
    doc_roundtrip_mismatches = 0
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
        _check_id_length(doc_id)
        _check_metadata_size(md, doc_id)
        # Full precision, no rounding: round(x, 8) rounds to a FIXED decimal
        # PLACE, not a fixed number of significant digits -- for a
        # small-magnitude component (routinely present in these 512-dim
        # vectors) that throws away real float32 precision. Python's default
        # float repr (used by json.dumps) is a shortest-string round-trip
        # encoding for the float64 that exactly holds this float32 value, so
        # parsing it back and casting to float32 reproduces the identical
        # bit pattern -- verified below by _roundtrip_check on every vector,
        # not assumed.
        values = list(vec)
        doc_roundtrip_mismatches += _roundtrip_check(vec, json.dumps(values))
        doc_records.append({"id": doc_id, "values": values, "namespace": "document", "metadata": md})

    # ---- chunks ----
    chunk_records = []
    zero_chunk_count = 0
    chunk_norm_samples = []
    chunk_roundtrip_mismatches = 0
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
        _check_id_length(key)
        _check_metadata_size(md, key)
        values = list(vec)
        chunk_roundtrip_mismatches += _roundtrip_check(vec, json.dumps(values))
        chunk_records.append({"id": key, "values": values, "namespace": "chunk", "metadata": md})

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
            "id_length_validated": f"every id checked against the {MAX_ID_BYTES}-byte Vectorize limit, script aborts on violation",
            "metadata_size_validated": f"every metadata object checked against the {MAX_METADATA_BYTES}-byte ({MAX_METADATA_BYTES // 1024}KiB) Vectorize limit, script aborts on violation",
            "float32_roundtrip_check": {
                "method": "for every vector, every component: source float32 vs (json.dumps -> json.loads -> struct-cast float32), compared as raw struct.pack(...) bytes -- not `==`/`!=` on the unpacked float values. Value equality would silently miss a +0.0/-0.0 bit-pattern flip (0.0 == -0.0 is True) and false-positive on an identical-bit-pattern NaN (nan != nan is True even for the same bits); this dataset has neither in practice, but the check now genuinely tests what it claims to test.",
                "documents_mismatches": doc_roundtrip_mismatches,
                "chunks_mismatches": chunk_roundtrip_mismatches,
                "expected": 0,
                "regression_note": "two fixes landed here. (1) An earlier version used round(x, 8), which measurably broke round-trip (72% of sampled float32 components failed -- 8 decimal PLACES is not the same as float32's ~9 significant-digit requirement). Fixed by exporting full, unrounded values. (2) The validator itself then compared unpacked float VALUES (`!=`), not bit patterns -- caught in a later review round; fixed to compare struct.pack(...) bytes directly (Step 1.1.1).",
            },
        },
        "output": {
            "max_records_per_ndjson_file": MAX_PER_FILE,
            "document_shards": doc_shards,
            "chunk_shards": chunk_shards,
            "max_shard_bytes": MAX_SHARD_BYTES,
            "namespaces": {
                "document": len(doc_records),
                "chunk": len(chunk_records),
                "why": "Vectorize applies namespace filtering BEFORE the ANN search, not as a post-filter (confirmed against current Cloudflare docs). Without this, a flat pool of 2675 docs + 15616 chunks would let chunk vectors (5.8x more numerous) dominate topK and truncate document-level candidates before scoring -- the browser's current behavior keeps doc and chunk as separate candidate pools and folds via max() only at the end (index_profile.doc_chunk_aggregation); namespace segmentation is the Vectorize-native way to preserve that same structure.",
            },
            "metadata_indexes_created": [],
            "metadata_indexes_note": "Deliberately zero for v1. Cloudflare requires a metadata index to exist BEFORE inserting vectors that need to be filtered by that property (vectors upserted earlier are not backfilled into an index created later -- would require re-upserting all 18291 vectors). Filtering by type is already covered by namespace at no cost. language/year/paper_id filters are deferred until an actual query need is confirmed, rather than speculatively indexed now.",
            "not_committed_to_git": "*.ndjson under this directory is gitignored (regenerable, ~tens of MB of JSON text); this report (dry_run_manifest.json) is committed as the durable evidence this step ran.",
        },
        "next_step_not_taken": "wrangler vectorize create / wrangler vectorize insert -- deliberately not run by this script. Requires an explicit go-ahead (creates persistent, billable Cloudflare infrastructure).",
    }
    (OUT_DIR / "dry_run_manifest.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    summary = [
        f"documents: {len(doc_records)}/{len(doc_manifest['docs'])} exported, {zero_doc_count} zero-norm, {doc_roundtrip_mismatches} roundtrip mismatches, {len(doc_shards)} shard(s)",
        f"chunks: {len(chunk_records)}/{len(chunk_manifest['chunks'])} exported, {zero_chunk_count} zero-norm, {chunk_roundtrip_mismatches} roundtrip mismatches, {len(chunk_shards)} shard(s)",
        f"duplicate ids across doc+chunk id space: {dup_count}",
        f"profile_consistency.matches: {profile_consistency['matches']}",
        f"output dir: {OUT_DIR}",
    ]
    print("\n".join(summary))
    if (
        zero_doc_count or zero_chunk_count or dup_count
        or doc_roundtrip_mismatches or chunk_roundtrip_mismatches
        or not profile_consistency["matches"]
    ):
        sys.exit(1)


if __name__ == "__main__":
    main()
