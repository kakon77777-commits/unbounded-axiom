from __future__ import annotations

import json
from pathlib import Path

from occupancy_cert.cover import generate_cover


ROOT = Path(__file__).resolve().parent
MODEL_PATH = ROOT / "data" / "synthetic_occupancy_model.json"
OUTPUT = ROOT / "outputs" / "dirichlet_green_cover_certificate.json"


def main() -> None:
    model = json.loads(MODEL_PATH.read_text(encoding="utf-8"))
    certificate = generate_cover(model, max_depth=12)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(certificate, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(certificate["statistics"], indent=2))


if __name__ == "__main__":
    main()

