from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import numpy as np

from notch.axis import default_axis_bands


ROOT = Path(__file__).resolve().parent


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def local_maxima(
    grid: np.ndarray,
    density: np.ndarray,
    separation: float,
    count: int = 4,
) -> list[dict[str, float]]:
    candidates = [
        index
        for index in range(1, len(grid) - 1)
        if density[index] >= density[index - 1]
        and density[index] >= density[index + 1]
        and density[index] > float(np.max(density)) * 1e-6
    ]
    candidates.sort(key=lambda index: density[index], reverse=True)
    selected = []
    for index in candidates:
        if any(
            abs(float(grid[index] - grid[prior])) < separation
            for prior in selected
        ):
            continue
        selected.append(index)
        if len(selected) == count:
            break
    maximum = float(np.max(density))
    return [
        {
            "x": float(grid[index]),
            "relative_score": float(density[index] / maximum),
            "raw_kde_score": float(density[index]),
        }
        for index in selected
    ]


def main() -> None:
    witness_paths = sorted(
        (ROOT / "data" / "parent_witnesses").glob(
            "*.witness.json"
        )
    )
    bands = default_axis_bands()
    bandwidths = (0.18, 0.12, 0.16, 0.20, 0.30)
    records: list[list[dict[str, float | str]]] = [
        [] for _ in bands
    ]
    per_witness = []
    for path in witness_paths:
        payload = read_json(path)
        witness_row = {
            "file": str(path.relative_to(ROOT)),
            "radius": float(payload["configuration"]["radius"]),
            "patch_id": payload["patch"]["patch_id"],
            "bands": [],
        }
        for band_index, support in enumerate(
            payload["joint_dual"]["axis_supports"]
        ):
            raw_weights = np.asarray(
                [row["weight"] for row in support],
                dtype=float,
            )
            weights = raw_weights / np.sum(raw_weights)
            points = np.asarray(
                [row["x"] for row in support],
                dtype=float,
            )
            for point, weight in zip(points, weights):
                records[band_index].append(
                    {
                        "x": float(point),
                        "weight": float(weight),
                        "radius": float(
                            payload["configuration"]["radius"]
                        ),
                        "patch_id": payload["patch"]["patch_id"],
                    }
                )
            mean = float(np.sum(points * weights))
            entropy = float(
                -np.sum(
                    weights
                    * np.log(np.maximum(weights, 1e-300))
                )
            )
            order = np.argsort(weights)[::-1][:3]
            witness_row["bands"].append(
                {
                    "band_id": bands[band_index].band_id,
                    "weighted_mean": mean,
                    "weighted_standard_deviation": float(
                        np.sqrt(
                            np.sum(weights * (points - mean) ** 2)
                        )
                    ),
                    "effective_support_size": float(
                        math.exp(entropy)
                    ),
                    "top_supports": [
                        {
                            "x": float(points[index]),
                            "weight": float(weights[index]),
                        }
                        for index in order
                    ],
                }
            )
        per_witness.append(witness_row)

    band_rows = []
    for band_index, band in enumerate(bands):
        grid = np.arange(
            band.start,
            band.stop + 0.005,
            0.01,
        )
        bandwidth = bandwidths[band_index]
        density = np.zeros_like(grid)
        for record in records[band_index]:
            density += float(record["weight"]) * np.exp(
                -0.5
                * (
                    (grid - float(record["x"]))
                    / bandwidth
                )
                ** 2
            )
        peaks = local_maxima(
            grid,
            density,
            separation=2.0 * bandwidth,
        )
        points = np.asarray(
            [float(record["x"]) for record in records[band_index]]
        )
        weights = np.asarray(
            [
                float(record["weight"])
                for record in records[band_index]
            ]
        )
        weights /= np.sum(weights)
        mean = float(np.sum(points * weights))
        band_rows.append(
            {
                "band_id": band.band_id,
                "interval": [band.start, band.stop],
                "bandwidth": bandwidth,
                "aggregate_weighted_mean": mean,
                "aggregate_weighted_standard_deviation": float(
                    np.sqrt(
                        np.sum(weights * (points - mean) ** 2)
                    )
                ),
                "kde_peaks": peaks,
                "primary_peak": peaks[0],
                "support_record_count": len(records[band_index]),
            }
        )

    peak = {
        row["band_id"]: row["primary_peak"]["x"]
        for row in band_rows
    }
    output = {
        "schema": "RH.AxisNotch.PeakAtlas.v0.5",
        "parent_witness_count": len(witness_paths),
        "aggregation_rule": (
            "Normalize each band measure within each witness, give "
            "each witness equal total mass per band, and form a "
            "Gaussian KDE over serialized support locations."
        ),
        "band_rows": band_rows,
        "per_witness": per_witness,
        "structural_observation": {
            "target_real_interval": [20.0, 20.5],
            "A1_primary_peak": peak["A1"],
            "A3_primary_peak": peak["A3"],
            "A4_primary_peak": peak["A4"],
            "A1_overlaps_target_real_interval": bool(
                20.0 <= peak["A1"] <= 20.5
            ),
            "harmonic_ratios_relative_to_A1": {
                "A3_over_A1": peak["A3"] / peak["A1"],
                "A4_over_A1": peak["A4"] / peak["A1"],
            },
        },
        "recommended_code_templates": [
            {
                "code_id": "baseline",
                "value_notches": [],
                "derivative_notches": [],
            },
            {
                "code_id": "anchor1",
                "value_notches": ["patch_center"],
                "derivative_notches": [],
            },
            {
                "code_id": "harmonic3",
                "value_notches": [
                    "patch_center",
                    "2*patch_center",
                    "4*patch_center",
                ],
                "derivative_notches": [],
            },
            {
                "code_id": "atlas3",
                "value_notches": [
                    "patch_center",
                    peak["A3"],
                    peak["A4"],
                ],
                "derivative_notches": [],
            },
            {
                "code_id": "five_band",
                "value_notches": [
                    peak["A0"],
                    "patch_center",
                    peak["A2"],
                    peak["A3"],
                    peak["A4"],
                ],
                "derivative_notches": [],
            },
            {
                "code_id": "anchor_flat",
                "value_notches": ["patch_center"],
                "derivative_notches": ["patch_center"],
                "role": (
                    "Taylor-sign ablation expected to suppress "
                    "the useful first derivative."
                ),
            },
        ],
        "global_rh_certificate": False,
    }
    (ROOT / "outputs" / "peak_atlas.json").write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
