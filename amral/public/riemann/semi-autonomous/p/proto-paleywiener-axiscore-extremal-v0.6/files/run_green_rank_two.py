from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np

from pwext.axis import band_grid, default_axis_bands, downward_count_majorant
from pwext.cover import Patch
from pwext.green import GreenRankTwoScanner


ROOT = Path(__file__).resolve().parent


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    parent = read_json(
        ROOT / "data" / "parent_geometry_joint.json"
    )
    patch = Patch(**parent["configuration"]["patch"])
    core_point = complex(
        0.5 * (patch.x_min + patch.x_max),
        0.5 * (patch.y_min + patch.y_max),
    )
    bands = default_axis_bands()
    rows = []
    for time_step in (0.02, 0.01, 0.005):
        scanner = GreenRankTwoScanner(
            radius=16.0,
            time_step=time_step,
        )
        band_rows = []
        for band in bands:
            grid = band_grid(band, 0.05)
            scan = scanner.scan(
                grid,
                core_point,
                downward_count_majorant(band),
            )
            thresholds = np.asarray(scan["thresholds"])
            maximum_index = int(np.argmax(thresholds))
            minimum_index = int(np.argmin(thresholds))
            band_rows.append(
                {
                    "band_id": band.band_id,
                    "count_coefficient": downward_count_majorant(
                        band
                    ),
                    "maximum_point_lower_bound": float(
                        thresholds[maximum_index]
                    ),
                    "maximum_point_x": float(
                        grid[maximum_index]
                    ),
                    "minimum_point_extremal": float(
                        thresholds[minimum_index]
                    ),
                    "minimum_point_x": float(
                        grid[minimum_index]
                    ),
                }
            )
        rows.append(
            {
                "time_step": scanner.actual_step,
                "time_grid_count": len(scanner.t),
                "core_point": {
                    "x": core_point.real,
                    "y": core_point.imag,
                },
                "axis_step": 0.05,
                "structural_gram_condition": float(
                    np.linalg.cond(scanner.structural_gram)
                ),
                "band_rows": band_rows,
            }
        )
        print(
            json.dumps(rows[-1], ensure_ascii=False),
            flush=True,
        )
    finest = rows[-1]["band_rows"]
    output = {
        "schema": "RH.PaleyWiener.GreenRankTwo.v0.6",
        "continuous_problem": (
            "One real-axis evaluation penalty and one fixed "
            "off-axis core evaluation in the clamped even H_0^2 "
            "tail Hilbert space."
        ),
        "closed_form": (
            "Lambda=1/(sqrt((a+b)^2-4c^2)-(a-b)), after "
            "rank-one axis Sherman-Morrison correction."
        ),
        "rows": rows,
        "finest_step_all_single_band_lower_bounds_below_one": all(
            row["maximum_point_lower_bound"] < 1.0
            for row in finest
        ),
        "interpretation": (
            "No single band and single atom certifies the observed "
            "full obstruction. The five-band measure interaction "
            "is essential."
        ),
        "interval_certified": False,
        "global_rh_certificate": False,
    }
    (
        ROOT / "outputs" / "green_rank_two_scan.json"
    ).write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
