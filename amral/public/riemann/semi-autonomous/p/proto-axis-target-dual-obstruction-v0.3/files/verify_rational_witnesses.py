from __future__ import annotations

import json
from pathlib import Path

from dualcert.witness import verify_rational_payload


ROOT = Path(__file__).resolve().parent


def main() -> None:
    payload = json.loads(
        (ROOT / "outputs" / "rational_model.json").read_text(
            encoding="utf-8"
        )
    )
    result = verify_rational_payload(payload)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    if not result["all_exact_ldl_positive"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
