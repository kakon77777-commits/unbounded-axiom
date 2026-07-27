from __future__ import annotations

import json
from pathlib import Path

from frontier.cover import (
    coverage_audit,
    default_cover,
    refined_cover,
)


ROOT = Path(__file__).resolve().parent


def main() -> None:
    original = default_cover()
    refined = refined_cover(original, 4, 4)
    output = {
        "schema": "RH.SupportPrime.CoverAudit.v0.4",
        "target_window": {
            "x": [20.0, 20.5],
            "y": [-0.2, -0.1],
        },
        "original_patch_count": len(original),
        "refined_patch_count": len(refined),
        "refinement": {"split_x": 4, "split_y": 4},
        "original_cover": coverage_audit(original),
        "refined_cover": coverage_audit(refined),
        "global_rh_certificate": False,
    }
    (ROOT / "outputs" / "cover_audit.json").write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
