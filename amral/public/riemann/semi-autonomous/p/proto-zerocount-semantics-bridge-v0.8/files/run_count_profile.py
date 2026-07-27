from __future__ import annotations

import json
from pathlib import Path

from bridge.axis import (
    INHERITED_S_PROFILE,
    count_profile_rows,
    lower_profile_downward,
    upper_profile_upward,
)


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "outputs" / "typed_count_profile.json"


def main() -> None:
    rows = count_profile_rows()
    lower = lower_profile_downward()
    upper = upper_profile_upward()
    output = {
        "schema": "RH.ZeroCount.TypedBandProfile.v0.8",
        "source_profile": INHERITED_S_PROFILE,
        "difference_identity": (
            "N(b)-N(a)=(theta(b)-theta(a))/pi+S(b)-S(a), "
            "subject to the adopted endpoint convention"
        ),
        "rows": rows,
        "downward_floating_lower_profile": lower,
        "upward_floating_upper_profile": upper,
        "semantic_roles": {
            "upper": (
                "may weight a supremum leakage majorant after source "
                "and endpoint certification"
            ),
            "lower": (
                "may weight an infimum minorant, but not an arbitrary "
                "probability measure or atomic operator"
            ),
        },
        "endpoint_conventions_certified": False,
        "directed_theta_and_log_enclosures_certified": False,
        "zeta_facing_profile_certified": False,
        "known_zero_ordinate_table_used": False,
        "global_rh_certificate": False,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
