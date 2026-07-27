from __future__ import annotations

import json
from pathlib import Path

from interval_cert.certificate import verify_certificate


ROOT = Path(__file__).resolve().parent


def main() -> None:
    witness = json.loads(
        (
            ROOT
            / "data"
            / "rational_atomic_witness_v0.6.json"
        ).read_text(encoding="utf-8")
    )
    certificate = json.loads(
        (
            ROOT
            / "outputs"
            / "interval_atomic_certificate.json"
        ).read_text(encoding="utf-8")
    )
    verification = verify_certificate(witness, certificate)
    output = ROOT / "outputs" / "certificate_verification.json"
    output.write_text(
        json.dumps(
            verification,
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    print(json.dumps(verification, indent=2, ensure_ascii=False))
    if not verification["verification_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

