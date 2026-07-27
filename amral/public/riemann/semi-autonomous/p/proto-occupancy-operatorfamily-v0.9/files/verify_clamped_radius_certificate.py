from __future__ import annotations

import json
from pathlib import Path

from occupancy_cert.clamped_budget import (
    file_sha256,
    verify_clamped_radius_certificate,
)


ROOT = Path(__file__).resolve().parent
WITNESS_PATH = ROOT / "data" / "parent_v0.7_rational_atomic_witness.json"
PARENT_CERTIFICATE_PATH = (
    ROOT / "data" / "parent_v0.7_interval_atomic_certificate.json"
)
CERTIFICATE_PATH = (
    ROOT / "outputs" / "clamped_58cell_radius_certificate.json"
)
OUTPUT = ROOT / "outputs" / "clamped_58cell_radius_verification.json"


def main() -> None:
    witness = json.loads(WITNESS_PATH.read_text(encoding="utf-8"))
    parent = json.loads(
        PARENT_CERTIFICATE_PATH.read_text(encoding="utf-8")
    )
    certificate = json.loads(
        CERTIFICATE_PATH.read_text(encoding="utf-8")
    )
    result = verify_clamped_radius_certificate(
        witness,
        parent,
        certificate,
        file_sha256(WITNESS_PATH),
        file_sha256(PARENT_CERTIFICATE_PATH),
    )
    OUTPUT.write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    if not result["verification_pass"]:
        failed = [
            key for key, value in result["checks"].items() if not value
        ]
        raise SystemExit(f"clamped verification failed: {failed}")
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
