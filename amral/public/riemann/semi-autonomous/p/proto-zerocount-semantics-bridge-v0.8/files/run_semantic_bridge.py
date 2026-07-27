from __future__ import annotations

import json
from pathlib import Path

from bridge.semantics import semantic_audit


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "outputs" / "semantic_bridge.json"


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    output = semantic_audit()
    OUTPUT.write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    if not output["all_invalid_rules_refuted"]:
        raise SystemExit("semantic countermodel audit failed")
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
