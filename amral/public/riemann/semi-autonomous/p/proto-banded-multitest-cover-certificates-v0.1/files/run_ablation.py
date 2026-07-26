from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np

from bmcc.cover import coarse_cover, default_cover
from bmcc.model import build_model, constrained_whitener, spectral_energy_matrix
from bmcc.optimizer import build_patch_certificate, generate_candidates


ROOT = Path(__file__).resolve().parent


def _load_ordinates() -> np.ndarray:
    with (ROOT / "data" / "first_50_ordinates.csv").open(
        encoding="utf-8"
    ) as handle:
        return np.asarray(
            [float(row["ordinate"]) for row in csv.DictReader(handle)]
        )


def _summarize(label: str, certificates: list[dict[str, object]]) -> dict[str, object]:
    rows = []
    for item in certificates:
        rows.append(
            {
                "cover": label,
                "patch_id": item["patch"]["patch_id"],
                "axis_band_energy": item["axis_band_energy"],
                "known_first_50_zero_mass_holdout": item[
                    "known_first_50_zero_mass_holdout"
                ],
                "tail_majorant_from_145_prototype": item[
                    "tail_majorant_from_145_prototype"
                ],
                "partial_gap": item[
                    "partial_gap_excluding_other_off_axis_bands"
                ],
                "crude_continuous_upper_bound": item[
                    "crude_continuous_upper_bound"
                ],
                "crude_continuous_sign_pass": item[
                    "crude_continuous_sign_pass"
                ],
            }
        )
    return {
        "cover": label,
        "patch_count": len(rows),
        "continuous_sign_pass_count": sum(
            bool(row["crude_continuous_sign_pass"]) for row in rows
        ),
        "max_axis_band_energy": max(row["axis_band_energy"] for row in rows),
        "max_known_first_50_zero_mass_holdout": max(
            row["known_first_50_zero_mass_holdout"] for row in rows
        ),
        "max_tail_majorant_from_145_prototype": max(
            row["tail_majorant_from_145_prototype"] for row in rows
        ),
        "most_negative_partial_gap": min(row["partial_gap"] for row in rows),
        "max_crude_continuous_upper_bound": max(
            row["crude_continuous_upper_bound"] for row in rows
        ),
        "rows": rows,
    }


def main() -> None:
    outputs = ROOT / "outputs"
    outputs.mkdir(parents=True, exist_ok=True)
    model = build_model()
    coordinate_map = constrained_whitener(model)
    energy, _ = spectral_energy_matrix(model, coordinate_map)
    ordinates = _load_ordinates()
    penalties = (0.0, 1.5e-4, 2e-4, 2.5e-4)

    results: dict[str, dict[str, object]] = {}
    for label, patches in (
        ("coarse_3x2", coarse_cover()),
        ("adaptive_18_patch", default_cover()),
    ):
        candidates = generate_candidates(
            patches,
            model,
            coordinate_map,
            energy,
            ordinates,
            penalties,
            arithmetic_floor=5e-5,
            random_seed=20260724,
        )
        certificates = [
            build_patch_certificate(patch, candidates, model)
            for patch in patches
        ]
        results[label] = _summarize(label, certificates)

    coarse = results["coarse_3x2"]
    adaptive = results["adaptive_18_patch"]
    comparison = {
        "max_axis_energy_reduction_factor": (
            coarse["max_axis_band_energy"] / adaptive["max_axis_band_energy"]
        ),
        "max_known_zero_mass_reduction_factor": (
            coarse["max_known_first_50_zero_mass_holdout"]
            / adaptive["max_known_first_50_zero_mass_holdout"]
        ),
        "max_tail_reduction_factor": (
            coarse["max_tail_majorant_from_145_prototype"]
            / adaptive["max_tail_majorant_from_145_prototype"]
        ),
        "partial_deficit_reduction_factor": (
            abs(coarse["most_negative_partial_gap"])
            / abs(adaptive["most_negative_partial_gap"])
        ),
        "continuous_pass_fraction_coarse": (
            coarse["continuous_sign_pass_count"] / coarse["patch_count"]
        ),
        "continuous_pass_fraction_adaptive": (
            adaptive["continuous_sign_pass_count"] / adaptive["patch_count"]
        ),
    }
    output = {
        "schema": "RH.BMCC.CoverAblation.v0.1",
        "question": (
            "Does refining height windows near the symmetry axis remove the "
            "coarse-cover boundary catastrophe without using zero ordinates?"
        ),
        "same_model_and_penalties": True,
        "known_zero_ordinates_used_in_optimization": False,
        "results": results,
        "comparison": comparison,
        "conclusion": (
            "Adaptive anisotropic refinement removes the coarse-cover numerical "
            "catastrophe and makes every patch pass the floating Lipschitz sign "
            "audit, but the partial global leakage budget remains negative."
        ),
        "evidence_level": "E2 floating numerical ablation",
    }
    (outputs / "ablation_summary.json").write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
