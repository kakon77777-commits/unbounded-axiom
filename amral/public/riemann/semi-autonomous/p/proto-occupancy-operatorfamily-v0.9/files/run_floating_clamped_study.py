from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from occupancy_cert.floating_clamped import floating_location_study
from occupancy_cert.rational_interval import as_fraction


ROOT = Path(__file__).resolve().parent
WITNESS_PATH = ROOT / "data" / "parent_v0.7_rational_atomic_witness.json"
OUTPUT = ROOT / "outputs" / "floating_clamped_location_study.json"


def main() -> None:
    witness = json.loads(WITNESS_PATH.read_text(encoding="utf-8"))
    model = witness["model"]
    count_coefficients = np.asarray(
        [
            float(as_fraction(value))
            for value in model["count_coefficients"]
        ]
    )
    centers = []
    band_indices = []
    probabilities = []
    for band_index, support in enumerate(witness["axis_supports"]):
        for atom in support:
            centers.append(float(as_fraction(atom["x"])))
            band_indices.append(band_index)
            probabilities.append(float(as_fraction(atom["weight"])))
    core_support = [
        {
            "x": float(as_fraction(atom["x"])),
            "y": float(as_fraction(atom["y"])),
            "weight": float(as_fraction(atom["weight"])),
        }
        for atom in witness["core_support"]
    ]
    result = floating_location_study(
        count_coefficients,
        np.asarray(centers),
        np.asarray(band_indices, dtype=int),
        np.asarray(probabilities),
        core_support,
        float(
            as_fraction(
                model["tail_scale_lower_decimal_rational"]
            )
        ),
    )
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "base": result["base_fixed_location_threshold"],
                "rows": [
                    {
                        "h": row["cell_half_width"],
                        "alpha": row[
                            "adversarial_corner_threshold"
                        ],
                    }
                    for row in result["adversarial_corner_rows"]
                ],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
