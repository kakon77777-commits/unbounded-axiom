from __future__ import annotations

import json
import statistics
from collections import Counter
from pathlib import Path

import numpy as np

from psdgram.cover import coverage_audit, default_cover


ROOT = Path(__file__).resolve().parent


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def range_mean(values: list[float]) -> dict[str, float]:
    return {
        "minimum": min(values),
        "mean": statistics.mean(values),
        "maximum": max(values),
    }


def main() -> None:
    outputs = ROOT / "outputs"
    gram_results = list(read_json(outputs / "gram_results.json"))
    diagonal_results = list(
        read_json(outputs / "diagonal_results.json")
    )
    rank_study = list(read_json(outputs / "rank_study.json"))
    candidates = list(
        read_json(ROOT / "data" / "parent_candidate_library.json")
    )

    candidate_vectors = np.column_stack(
        [
            np.asarray(item["reduced_coefficients"], dtype=float)
            for item in candidates
        ]
    )
    candidate_vectors /= np.linalg.norm(
        candidate_vectors, axis=0
    )[None, :]

    direction_distances = []
    for result in gram_results:
        gram = np.asarray(result["gram"], dtype=float)
        values, vectors = np.linalg.eigh(0.5 * (gram + gram.T))
        direction = vectors[:, int(np.argmax(values))]
        cosines = np.abs(direction @ candidate_vectors)
        closest = int(np.argmax(cosines))
        cosine = float(cosines[closest])
        direction_distances.append(
            {
                "patch_id": result["patch_id"],
                "closest_parent_candidate_id": candidates[closest][
                    "candidate_id"
                ],
                "absolute_c0_cosine": cosine,
                "c0_angle_degrees": float(
                    np.degrees(np.arccos(min(1.0, cosine)))
                ),
            }
        )

    band_statistics = []
    dominant_bands = []
    for band_index in range(len(gram_results[0]["axis_bands"])):
        charges = [
            result["axis_bands"][band_index]["sampled_charge"]
            for result in gram_results
        ]
        shares = [
            result["axis_bands"][band_index]["sampled_charge"]
            / result["sampled_axis_plus_tail_majorant"]
            for result in gram_results
        ]
        band_statistics.append(
            {
                "band_id": gram_results[0]["axis_bands"][band_index][
                    "band_id"
                ],
                "start": gram_results[0]["axis_bands"][band_index][
                    "start"
                ],
                "stop": gram_results[0]["axis_bands"][band_index][
                    "stop"
                ],
                "sampled_charge": range_mean(charges),
                "sampled_objective_share": range_mean(shares),
            }
        )
    for result in gram_results:
        dominant_bands.append(
            max(
                result["axis_bands"],
                key=lambda band: band["sampled_charge"],
            )["band_id"]
        )

    paired_reductions = []
    for diagonal, gram in zip(diagonal_results, gram_results):
        paired_reductions.append(
            {
                "patch_id": gram["patch_id"],
                "sampled_majorant_reduction_fraction": (
                    diagonal["sampled_axis_plus_tail_majorant"]
                    - gram["sampled_axis_plus_tail_majorant"]
                )
                / diagonal["sampled_axis_plus_tail_majorant"],
                "known_zero_holdout_reduction_fraction": (
                    diagonal["known_first_50_holdout_mass"]
                    - gram["known_first_50_holdout_mass"]
                )
                / diagonal["known_first_50_holdout_mass"],
            }
        )

    rank_rows = []
    for patch_id in dict.fromkeys(
        item["patch_id"] for item in rank_study
    ):
        members = [
            item for item in rank_study if item["patch_id"] == patch_id
        ]
        rank_rows.append(
            {
                "patch_id": patch_id,
                "sweeps": [
                    {
                        "requested_rank": item["requested_rank"],
                        "numerical_rank": item["numerical_rank"],
                        "sampled_majorant": item[
                            "sampled_axis_plus_tail_majorant"
                        ],
                    }
                    for item in members
                ],
                "sampled_majorant_range": [
                    min(
                        item["sampled_axis_plus_tail_majorant"]
                        for item in members
                    ),
                    max(
                        item["sampled_axis_plus_tail_majorant"]
                        for item in members
                    ),
                ],
            }
        )

    sampled_majorants = [
        item["sampled_axis_plus_tail_majorant"]
        for item in gram_results
    ]
    corrected_majorants = [
        item["lipschitz_corrected_axis_plus_tail_majorant"]
        for item in gram_results
    ]
    angles = [
        item["c0_angle_degrees"] for item in direction_distances
    ]
    diagnostic = {
        "schema": "RH.PSDGram.Diagnostics.v0.2",
        "sampled_majorant": range_mean(sampled_majorants),
        "lipschitz_corrected_majorant": range_mean(
            corrected_majorants
        ),
        "target_budget": 1.0,
        "best_sampled_budget_multiple": min(sampled_majorants),
        "best_lipschitz_corrected_budget_multiple": min(
            corrected_majorants
        ),
        "band_statistics": band_statistics,
        "dominant_band_counts": dict(Counter(dominant_bands)),
        "tail_objective_share": range_mean(
            [
                item["tail_majorant"]
                / item["sampled_axis_plus_tail_majorant"]
                for item in gram_results
            ]
        ),
        "paired_reductions": paired_reductions,
        "full_gram_direction_distance_from_parent_library": {
            "metric": (
                "Principal angle in the C0-whitened constrained "
                "coordinate space."
            ),
            "angle_degrees": range_mean(angles),
            "rows": direction_distances,
        },
        "rank_study": rank_rows,
        "continuity": {
            "refined_core_pass_count": sum(
                item["lipschitz_audit"][
                    "core_refined_continuous_sign_pass"
                ]
                for item in gram_results
            ),
            "patch_count": len(gram_results),
            "refined_core_upper_range": [
                min(
                    item["lipschitz_audit"][
                        "core_refined_continuous_upper"
                    ]
                    for item in gram_results
                ),
                max(
                    item["lipschitz_audit"][
                        "core_refined_continuous_upper"
                    ]
                    for item in gram_results
                ),
            ],
        },
        "decision": (
            "Stop expanding the same primal rank family. Construct a "
            "dual axis-target transfer lower-bound certificate focused "
            "on the [18,23] band before any further global optimization."
        ),
    }
    write_json(outputs / "diagnostics.json", diagnostic)
    write_json(
        outputs / "cover_audit.json",
        coverage_audit(default_cover()),
    )
    summary = dict(read_json(outputs / "experiment_summary.json"))
    summary.update(
        {
            "gram_sampled_majorant_range": [
                min(sampled_majorants),
                max(sampled_majorants),
            ],
            "gram_lipschitz_corrected_majorant_range": [
                min(corrected_majorants),
                max(corrected_majorants),
            ],
            "dominant_sampled_axis_band": {
                "band_id": "A1",
                "interval": [18.0, 23.0],
                "dominant_patch_count": dominant_bands.count("A1"),
            },
            "next_node_decision": (
                "Construct a dual axis-target transfer lower-bound "
                "certificate focused on [18,23] before any further "
                "primal rank expansion."
            ),
        }
    )
    write_json(outputs / "experiment_summary.json", summary)


if __name__ == "__main__":
    main()
