from __future__ import annotations

import json
import math
from pathlib import Path

from frontier.axis import PUBLISHED_S_BOUND, default_axis_bands
from frontier.context import source_aligned_tail_multiplier


ROOT = Path(__file__).resolve().parent


def legacy_s_bound(t: float) -> float:
    return (
        0.111 * math.log(t)
        + 0.275 * math.log(math.log(t))
        + 2.450
    )


def legacy_theta(t: float) -> float:
    from scipy.special import loggamma

    z = 0.25 + 0.5j * t
    return float(loggamma(z).imag - t * math.log(math.pi) / 2.0)


def legacy_count(start: float, stop: float) -> float:
    return max(
        0.0,
        (legacy_theta(stop) - legacy_theta(start)) / math.pi
        + legacy_s_bound(start)
        + legacy_s_bound(stop),
    )


def main() -> None:
    bands = default_axis_bands()
    rows = []
    for band in bands:
        legacy = legacy_count(band.start, band.stop)
        rows.append(
            {
                "band_id": band.band_id,
                "interval": [band.start, band.stop],
                "legacy_preprint_profile": legacy,
                "published_profile": band.count_majorant,
                "increase": band.count_majorant - legacy,
            }
        )
    output = {
        "schema": "RH.SupportPrime.SourceProfile.v0.4",
        "published_s_bound": PUBLISHED_S_BOUND,
        "primary_source": {
            "author": "Timothy S. Trudgian",
            "title": (
                "An improved upper bound for the argument of the "
                "Riemann zeta-function on the critical line II"
            ),
            "journal": "Journal of Number Theory 134 (2014), 280-292",
            "doi_url": (
                "https://doi.org/10.1016/j.jnt.2013.07.017"
            ),
            "arxiv_url": "https://arxiv.org/abs/1208.5846",
            "note": (
                "The arXiv abstract reports 0.111, 0.275, 2.450; "
                "the published abstract reports the conservative "
                "0.112, 0.278, 2.510 constants used here."
            ),
        },
        "band_rows": rows,
        "source_aligned_tail_multiplier": (
            source_aligned_tail_multiplier()
        ),
        "certification_status": (
            "Source-aligned floating implementation; directed-rounding "
            "and interval transfer remain open."
        ),
        "global_rh_certificate": False,
    }
    (ROOT / "outputs" / "source_profile.json").write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
