from __future__ import annotations

import json
from pathlib import Path

from occupancy_cert.clamped_budget import (
    build_clamped_radius_certificate,
    file_sha256,
)


ROOT = Path(__file__).resolve().parent
WITNESS_PATH = ROOT / "data" / "parent_v0.7_rational_atomic_witness.json"
PARENT_CERTIFICATE_PATH = (
    ROOT / "data" / "parent_v0.7_interval_atomic_certificate.json"
)
OUTPUT = ROOT / "outputs" / "clamped_58cell_radius_certificate.json"


def main() -> None:
    witness = json.loads(WITNESS_PATH.read_text(encoding="utf-8"))
    parent = json.loads(
        PARENT_CERTIFICATE_PATH.read_text(encoding="utf-8")
    )
    result = build_clamped_radius_certificate(
        witness,
        parent,
        file_sha256(WITNESS_PATH),
        file_sha256(PARENT_CERTIFICATE_PATH),
    )
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result["proof_budget"], indent=2))


if __name__ == "__main__":
    main()

