from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from psdgram.cover import default_cover
from psdgram.experiment import ExperimentContext, evaluate_gram_candidate
from run_experiment import compact_row, write_csv, write_json


ROOT = Path(__file__).resolve().parent


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def refresh_results(
    results: list[dict[str, object]],
    context: ExperimentContext,
) -> list[dict[str, object]]:
    patches = {patch.patch_id: patch for patch in default_cover()}
    refreshed = []
    for result in results:
        print(
            f"refresh {result['method']} {result['patch_id']}",
            flush=True,
        )
        refreshed.append(
            evaluate_gram_candidate(
                patches[str(result["patch_id"])],
                np.asarray(result["gram"], dtype=float),
                context,
                method=str(result["method"]),
                requested_rank=(
                    None
                    if result["requested_rank"] is None
                    else int(result["requested_rank"])
                ),
                optimizer=dict(result["optimizer"]),
            )
        )
    return refreshed


def main() -> None:
    outputs = ROOT / "outputs"
    context = ExperimentContext(ROOT)
    diagonal_results = refresh_results(
        list(load_json(outputs / "diagonal_results.json")),
        context,
    )
    gram_results = refresh_results(
        list(load_json(outputs / "gram_results.json")),
        context,
    )
    rank_study = refresh_results(
        list(load_json(outputs / "rank_study.json")),
        context,
    )

    write_json(outputs / "diagonal_results.json", diagonal_results)
    write_json(outputs / "gram_results.json", gram_results)
    write_json(outputs / "rank_study.json", rank_study)
    write_csv(
        outputs / "comparison.csv",
        [
            compact_row(item)
            for item in diagonal_results + gram_results
        ],
    )

    patch_outputs = outputs / "patches"
    for result in diagonal_results:
        write_json(
            patch_outputs
            / f"{result['patch_id']}.diagonal.json",
            result,
        )
    for result in gram_results:
        write_json(
            patch_outputs / f"{result['patch_id']}.gram.json",
            result,
        )

    summary = dict(load_json(outputs / "experiment_summary.json"))
    summary.update(
        {
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
            "continuity_audit": (
                "Floating sampled first derivatives plus global "
                "second-derivative envelopes on every core cell and "
                "axis-band interval."
            ),
        }
    )
    write_json(outputs / "experiment_summary.json", summary)


if __name__ == "__main__":
    main()
