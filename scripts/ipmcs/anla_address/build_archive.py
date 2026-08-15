"""IPMCS Phase IP-4 -- build step.

Packs the real Logic Matrix corpus (content/papers/) through ANLA's real
anla1.snapshot pipeline (BLAKE3 content-addressing, content-defined chunking,
per-chunk + per-file hash verification on every future read) -- not a
reimplemented hash scheme. Emits two things:

  1. logic-matrix-corpus.anla -- the real archive (gitignored, regenerable,
     ~90MB; nothing here is precision-sensitive the way the embedding NDJSON
     exports were, so no manifest/bit-pattern round-trip proof is needed
     beyond ANLA's own verify_archive(), run below).
  2. paper-addresses-<date>.json -- a small, committed sidecar mapping each
     Logic Matrix paper_id to its ANLA object_id + content_hash (both
     hex-encoded) + source path, cross-referenced against registry/papers.json
     (the SAME id namespace ipmcsSearch() already returns). Node-side code
     reads this directly for O(1) address lookup without needing Python;
     resolve_address.py (this directory) is what actually re-verifies against
     the archive at query time.

Usage: python build_archive.py
(reads ../../../registry/papers.json and ../../../content/papers/,
writes into this directory)
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent.parent
ANLA_PYTHON = Path(r"D:\Ai\work together\ANLA\python")
sys.path.insert(0, str(ANLA_PYTHON))

from anla1.fs import scan_tree  # noqa: E402
from anla1.snapshot import cdc_chunker, list_snapshots, verify_archive, write_snapshot  # noqa: E402

CONTENT_PAPERS = REPO_ROOT / "content" / "papers"
PAPERS_JSON = REPO_ROOT / "registry" / "papers.json"
ARCHIVE_PATH = HERE / "logic-matrix-corpus.anla"
SIDECAR_PATH = HERE / "paper-addresses-2026-08-15.json"

#: Fixed so the archive is reproducible across rebuilds -- there is no lineage
#: to preserve yet (this is the first pack), and a random id would make two
#: builds of the identical corpus look like different archives for no reason.
ARCHIVE_ID = bytes(range(16))


def main() -> int:
    if not CONTENT_PAPERS.is_dir():
        raise SystemExit(f"corpus dir not found: {CONTENT_PAPERS}")
    papers = json.loads(PAPERS_JSON.read_text(encoding="utf-8"))["items"]
    print(f"papers.json: {len(papers)} items")

    print(f"scanning {CONTENT_PAPERS} ...")
    tree = scan_tree(CONTENT_PAPERS)
    print(f"  {len(tree.files)} files, {tree.total_bytes:,} bytes")

    print(f"packing -> {ARCHIVE_PATH} ...")
    t0 = time.perf_counter()
    archive_bytes = write_snapshot(
        ARCHIVE_PATH, **tree.as_source(),
        created_unix_ns=time.time_ns(),
        chunker=cdc_chunker(),
        archive_id=ARCHIVE_ID,
    )
    print(f"  {archive_bytes:,} archive bytes in {time.perf_counter() - t0:.1f}s")

    print("verify_archive() ...")
    data = ARCHIVE_PATH.read_bytes()
    report = verify_archive(data)
    print(f"  {report.unique_chunks} unique chunks, {report.logical_bytes:,} logical bytes -- OK")

    snapshot = list_snapshots(data)[-1]
    by_path = {}
    for entry in snapshot.manifest["objects"]:
        if entry["kind"] != "regular-file":
            continue
        by_path[entry["path"]] = {
            "object_id": entry["object_id"].hex(),
            "content_hash": entry["content_hash"].hex(),
            "size": entry["size"],
        }
    print(f"  {len(by_path)} regular-file entries in manifest")

    # content/papers/ -relative path, POSIX separators, matching scan_tree's
    # own path convention -- cross-referenced against source_file which is
    # repo-root-relative ("content/papers/...").
    prefix = "content/papers/"
    sidecar = {}
    missing = []       # papers.json entry -> no matching ANLA manifest path
    id_collisions = []  # two+ papers.json entries claim the same id (registry bug,
                        # not an ANLA/archiving problem -- both files are archived and
                        # addressable, but only one can occupy the sidecar's per-id slot)
    for item in papers:
        rel = item["source_file"]
        if not rel.startswith(prefix):
            continue
        anla_path = rel[len(prefix):]
        hit = by_path.get(anla_path)
        if hit is None:
            missing.append(item["id"])
            continue
        if item["id"] in sidecar and sidecar[item["id"]]["path"] != anla_path:
            id_collisions.append({
                "id": item["id"],
                "kept_path": sidecar[item["id"]]["path"],
                "dropped_path": anla_path,
                "dropped_object_id": hit["object_id"],
            })
            continue  # first-seen wins; both are still in the .anla archive itself
        sidecar[item["id"]] = {"path": anla_path, **hit}

    if missing:
        print(f"  WARNING: {len(missing)} papers.json entries had no ANLA manifest match "
              f"(first 5: {missing[:5]})")
    if id_collisions:
        print(f"  WARNING: {len(id_collisions)} paper_id(s) claimed by 2+ source files "
              f"(registry bug, pre-existing -- not introduced by this script): "
              f"{[c['id'] for c in id_collisions]}")

    SIDECAR_PATH.write_text(
        json.dumps({
            "archive": ARCHIVE_PATH.name,
            "archive_id": ARCHIVE_ID.hex(),
            "hash_algorithm": snapshot.hash_algorithm,
            "built_unix_ns": snapshot.manifest.get("created_unix_ns"),
            "paper_count": len(sidecar),
            "unmatched_papers": missing,
            "id_collisions": id_collisions,
            "addresses": sidecar,
        }, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    print(f"wrote {SIDECAR_PATH} ({len(sidecar)} addresses, "
          f"{len(missing)} unmatched, {len(id_collisions)} id collisions)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
