"""IPMCS Phase IP-4 -- runtime address resolution.

Given one or more Logic Matrix paper_ids, re-extracts each from the real
logic-matrix-corpus.anla archive via anla1.snapshot.extract_snapshot() --
which independently re-verifies, per anla1/snapshot.py: each chunk's stored
bytes against its payload_hash, each chunk's decoded content against its own
chunk_id, and the whole file against its content_hash (raises IntegrityFailure
on any mismatch, does not silently return wrong bytes). This is the same
verification path ANLA's own test harness (test_demo/run.py) trusts, deliberately
not a lighter-weight shortcut -- see that file's docstring for why a check that
never re-reads the archive would be non-falsifiable.

`digest_verified` is only ever true when that full chain actually ran and
matched; on IntegrityFailure/ManifestInvalid/missing-id it reports false with
the reason, never fabricates confirmation.

Usage: python resolve_address.py <paper_id> [<paper_id> ...]
Output: one JSON object on stdout, {paper_id: {digest_verified, object_id,
content_hash, size, path, ...}}
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ANLA_PYTHON = Path(r"D:\Ai\work together\ANLA\python")
sys.path.insert(0, str(ANLA_PYTHON))

from anla.errors import AnlaError  # noqa: E402
from anla1.snapshot import extract_snapshot, list_snapshots  # noqa: E402

ARCHIVE_PATH = HERE / "logic-matrix-corpus.anla"
SIDECAR_PATH = HERE / "paper-addresses-2026-08-15.json"


def resolve(paper_ids: list[str]) -> dict:
    sidecar = json.loads(SIDECAR_PATH.read_text(encoding="utf-8"))
    addresses = sidecar["addresses"]
    data = ARCHIVE_PATH.read_bytes()
    snapshot = list_snapshots(data)[-1]

    result = {}
    try:
        # One extract_snapshot() call verifies every object's full hash chain;
        # reused across all requested ids rather than re-parsing the archive
        # per id.
        verified = extract_snapshot(data, snapshot)
        extract_error = None
    except AnlaError as e:
        verified = {}
        extract_error = f"{type(e).__name__}: {e}"

    for pid in paper_ids:
        addr = addresses.get(pid)
        if addr is None:
            result[pid] = {"digest_verified": False, "reason": "no ANLA address for this paper_id"}
            continue
        if extract_error is not None:
            result[pid] = {"digest_verified": False, "reason": extract_error,
                            "object_id": addr["object_id"], "path": addr["path"]}
            continue
        content = verified.get(addr["path"])
        result[pid] = {
            "digest_verified": content is not None,
            "object_id": addr["object_id"],
            "content_hash": addr["content_hash"],
            "size": addr["size"],
            "path": addr["path"],
            "archive": sidecar["archive"],
            "hash_algorithm": sidecar["hash_algorithm"],
        }
        if content is None:
            result[pid]["reason"] = "path present in sidecar but absent from latest snapshot manifest"
    return result


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: python resolve_address.py <paper_id> [<paper_id> ...]", file=sys.stderr)
        return 1
    print(json.dumps(resolve(sys.argv[1:]), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
