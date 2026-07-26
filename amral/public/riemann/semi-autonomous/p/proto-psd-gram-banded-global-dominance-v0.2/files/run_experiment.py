from __future__ import annotations

import csv
import json
from pathlib import Path

from psdgram.cover import default_cover
from psdgram.experiment import (
    ExperimentContext,
    run_diagonal_patch,
    run_factorized_patch,
)


ROOT = Path(__file__).resolve().parent


def write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    fields = sorted(set().union(*(row.keys() for row in rows)))
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def compact_row(result: dict[str, object]) -> dict[str, object]:
    return {
        "patch_id": result["patch_id"],
        "method": result["method"],
        "requested_rank": result["requested_rank"],
        "numerical_rank": result["numerical_rank"],
        "arithmetic_value": result["arithmetic_value"],
        "dense_core_max": result["dense_core_max"],
        "guard_positive_max": result["guard_positive_max"],
        "sampled_axis_prefix_majorant": result[
            "sampled_axis_prefix_majorant"
        ],
        "tail_majorant": result["tail_majorant"],
        "sampled_axis_plus_tail_majorant": result[
            "sampled_axis_plus_tail_majorant"
        ],
        "lipschitz_corrected_axis_plus_tail_majorant": result[
            "lipschitz_corrected_axis_plus_tail_majorant"
        ],
        "known_first_50_holdout_mass": result[
            "known_first_50_holdout_mass"
        ],
        "sampled_partial_gap": result[
            "sampled_partial_gap_excluding_unknown_off_axis"
        ],
        "lipschitz_corrected_partial_gap": result[
            "lipschitz_corrected_partial_gap_excluding_unknown_off_axis"
        ],
        "core_continuous_sign_pass": result["lipschitz_audit"][
            "core_refined_continuous_sign_pass"
        ],
        "global_certificate_pass": result["global_certificate_pass"],
    }


def main() -> None:
    outputs = ROOT / "outputs"
    outputs.mkdir(parents=True, exist_ok=True)
    patch_outputs = outputs / "patches"
    patch_outputs.mkdir(parents=True, exist_ok=True)
    context = ExperimentContext(ROOT)
    patches = default_cover()

    rank_study_ids = ["X1_Y0", "X1_Y1", "x2_Y2", "x2_Y3"]
    rank_study = []
    for patch_id in rank_study_ids:
        patch = next(item for item in patches if item.patch_id == patch_id)
        for rank in (1, 2, 4, 8):
            print(f"rank-study {patch_id} rank={rank}", flush=True)
            result = run_factorized_patch(patch, rank, context)
            rank_study.append(result)
    write_json(outputs / "rank_study.json", rank_study)

    # Representative rank sweeps test whether higher-rank factors survive.
    # The full 18-patch pass uses rank one because the sweep is designed to
    # detect the observed collapse before paying the all-patch cost.
    selected_rank = 1
    diagonal_results = []
    gram_results = []
    for patch in patches:
        print(f"diagonal {patch.patch_id}", flush=True)
        diagonal = run_diagonal_patch(patch, context)
        diagonal_results.append(diagonal)
        write_json(
            patch_outputs / f"{patch.patch_id}.diagonal.json",
            diagonal,
        )

        print(
            f"full-gram {patch.patch_id} rank={selected_rank}",
            flush=True,
        )
        gram = run_factorized_patch(
            patch, selected_rank, context
        )
        gram_results.append(gram)
        write_json(
            patch_outputs / f"{patch.patch_id}.gram.json",
            gram,
        )

    rows = [
        compact_row(item)
        for item in diagonal_results + gram_results
    ]
    write_csv(outputs / "comparison.csv", rows)
    write_json(outputs / "diagonal_results.json", diagonal_results)
    write_json(outputs / "gram_results.json", gram_results)

    paired = []
    for diagonal, gram in zip(diagonal_results, gram_results):
        diagonal_majorant = diagonal[
            "sampled_axis_plus_tail_majorant"
        ]
        gram_majorant = gram["sampled_axis_plus_tail_majorant"]
        paired.append(
            {
                "patch_id": diagonal["patch_id"],
                "diagonal_sampled_majorant": diagonal_majorant,
                "gram_sampled_majorant": gram_majorant,
                "sampled_majorant_reduction_fraction": (
                    diagonal_majorant - gram_majorant
                )
                / diagonal_majorant,
                "diagonal_holdout": diagonal[
                    "known_first_50_holdout_mass"
                ],
                "gram_holdout": gram[
                    "known_first_50_holdout_mass"
                ],
                "holdout_reduction_fraction": (
                    diagonal["known_first_50_holdout_mass"]
                    - gram["known_first_50_holdout_mass"]
                )
                / diagonal["known_first_50_holdout_mass"],
                "gram_numerical_rank": gram["numerical_rank"],
                "gram_partial_gap": gram[
                    "sampled_partial_gap_excluding_unknown_off_axis"
                ],
            }
        )

    summary = {
        "schema": "RH.PSDGram.ExperimentSummary.v0.2",
        "research_mode": "semi-autonomous AI mathematical research",
        "provenance": {
            "technical_research_lead": (
                "OpenAI Codex (AI research collaborator)"
            ),
            "research_field_and_authorization": "Neo.K / EveMissLab",
            "technical_judgments_attributed_to_ai": True,
        },
        "parent_node": "RH-BMCC-20260724-v0.1",
        "patch_count": len(patches),
        "candidate_ray_count": len(context.candidates),
        "full_gram_coordinate_dimension": int(
            context.coordinate_map.shape[1]
        ),
        "selected_factor_rank": selected_rank,
        "rank_study_patch_ids": rank_study_ids,
        "axis_bands": [
            {
                "band_id": band.band_id,
                "start": band.start,
                "stop": band.stop,
                "count_majorant": band.count_majorant,
            }
            for band in context.bands
        ],
        "known_zero_ordinates_used_in_optimization": False,
        "known_zero_ordinates_used_as_holdout_only": True,
        "solver_boundary": (
            "No convex SDP solver was available. A=L L^T was optimized "
            "with multi-start SLSQP; PSD is constructive, global SDP "
            "optimality is not claimed."
        ),
        "paired_results": paired,
        "gram_numerical_ranks": [
            item["numerical_rank"] for item in gram_results
        ],
        "mean_sampled_majorant_reduction_fraction": sum(
            item["sampled_majorant_reduction_fraction"]
            for item in paired
        )
        / len(paired),
        "min_sampled_majorant_reduction_fraction": min(
            item["sampled_majorant_reduction_fraction"]
            for item in paired
        ),
        "max_sampled_majorant_reduction_fraction": max(
            item["sampled_majorant_reduction_fraction"]
            for item in paired
        ),
        "gram_sampled_partial_gap_range": [
            min(
                item[
                    "sampled_partial_gap_excluding_unknown_off_axis"
                ]
                for item in gram_results
            ),
            max(
                item[
                    "sampled_partial_gap_excluding_unknown_off_axis"
                ]
                for item in gram_results
            ),
        ],
        "gram_sampled_majorant_range": [
            min(
                item["sampled_axis_plus_tail_majorant"]
                for item in gram_results
            ),
            max(
                item["sampled_axis_plus_tail_majorant"]
                for item in gram_results
            ),
        ],
        "gram_lipschitz_corrected_majorant_range": [
            min(
                item[
                    "lipschitz_corrected_axis_plus_tail_majorant"
                ]
                for item in gram_results
            ),
            max(
                item[
                    "lipschitz_corrected_axis_plus_tail_majorant"
                ]
                for item in gram_results
            ),
        ],
        "gram_lipschitz_corrected_partial_gap_range": [
            min(
                item[
                    "lipschitz_corrected_partial_gap_excluding_unknown_off_axis"
                ]
                for item in gram_results
            ),
            max(
                item[
                    "lipschitz_corrected_partial_gap_excluding_unknown_off_axis"
                ]
                for item in gram_results
            ),
        ],
        "any_sampled_partial_budget_pass": any(
            item["sampled_partial_budget_pass"]
            for item in gram_results
        ),
        "any_lipschitz_corrected_partial_budget_pass": any(
            item["lipschitz_corrected_partial_budget_pass"]
            for item in gram_results
        ),
        "all_core_crude_continuous_sign_pass": all(
            item["lipschitz_audit"][
                "core_crude_continuous_sign_pass"
            ]
            for item in gram_results
        ),
        "all_core_refined_continuous_sign_pass": all(
            item["lipschitz_audit"][
                "core_refined_continuous_sign_pass"
            ]
            for item in gram_results
        ),
        "core_crude_continuity_failures": [
            item["patch_id"]
            for item in gram_results
            if not item["lipschitz_audit"][
                "core_crude_continuous_sign_pass"
            ]
        ],
        "core_refined_continuity_failures": [
            item["patch_id"]
            for item in gram_results
            if not item["lipschitz_audit"][
                "core_refined_continuous_sign_pass"
            ]
        ],
        "continuity_audit": (
            "Floating sampled first derivatives plus global "
            "second-derivative envelopes on every core cell and "
            "axis-band interval."
        ),
        "dominant_sampled_axis_band": {
            "band_id": "A1",
            "interval": [18.0, 23.0],
            "dominant_patch_count": sum(
                max(
                    item["axis_bands"],
                    key=lambda band: band["sampled_charge"],
                )["band_id"]
                == "A1"
                for item in gram_results
            ),
        },
        "next_node_decision": (
            "Construct a dual axis-target transfer lower-bound "
            "certificate focused on [18,23] before any further "
            "primal rank expansion."
        ),
        "global_certificate_pass": False,
        "global_failure_reasons": [
            "Every sampled zero-position-free partial majorant remains above the unit target margin.",
            "Axis suprema and count majorants are floating, not interval-certified.",
            "Unknown off-axis bands are not yet charged.",
            "The target patches do not carry positive winding or zero-presence certificates.",
            "Factorized SLSQP does not certify the convex SDP optimum."
        ],
    }
    write_json(outputs / "experiment_summary.json", summary)
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
