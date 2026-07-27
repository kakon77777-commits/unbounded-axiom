from __future__ import annotations

import json
from pathlib import Path

from occupancy_cert.semantics import occupancy_semantic_audit


ROOT = Path(__file__).resolve().parent
MODEL_PATH = ROOT / "data" / "synthetic_occupancy_model.json"
OUTPUT = ROOT / "outputs" / "occupancy_semantic_bridge.json"


def main() -> None:
    model = json.loads(MODEL_PATH.read_text(encoding="utf-8"))
    result = occupancy_semantic_audit(model)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

