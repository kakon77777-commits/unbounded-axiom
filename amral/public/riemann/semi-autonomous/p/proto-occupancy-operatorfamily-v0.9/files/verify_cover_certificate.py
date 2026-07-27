from __future__ import annotations

import json
from pathlib import Path

from occupancy_cert.cover import verify_cover


ROOT = Path(__file__).resolve().parent
MODEL_PATH = ROOT / "data" / "synthetic_occupancy_model.json"
CERTIFICATE_PATH = (
    ROOT / "outputs" / "dirichlet_green_cover_certificate.json"
)
OUTPUT = ROOT / "outputs" / "dirichlet_green_cover_verification.json"


def main() -> None:
    model = json.loads(MODEL_PATH.read_text(encoding="utf-8"))
    certificate = json.loads(
        CERTIFICATE_PATH.read_text(encoding="utf-8")
    )
    result = verify_cover(model, certificate)
    OUTPUT.write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    if not result["verification_pass"]:
        failed = [
            key for key, value in result["checks"].items() if not value
        ]
        raise SystemExit(f"cover verification failed: {failed}")
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

