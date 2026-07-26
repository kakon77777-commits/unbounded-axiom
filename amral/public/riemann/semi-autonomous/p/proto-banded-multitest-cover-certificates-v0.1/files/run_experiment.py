from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import numpy as np

from bmcc.cover import coverage_audit, default_cover
from bmcc.model import (
    build_model,
    constrained_whitener,
    spectral_energy_matrix,
)
from bmcc.optimizer import build_patch_certificate, generate_candidates


ROOT = Path(__file__).resolve().parent


def _load_ordinates() -> np.ndarray:
    with (ROOT / "data" / "first_50_ordinates.csv").open(
        encoding="utf-8"
    ) as handle:
        return np.asarray(
            [float(row["ordinate"]) for row in csv.DictReader(handle)]
        )


def _write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    fields = sorted(set().union(*(row.keys() for row in rows)))
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    outputs = ROOT / "outputs"
    outputs.mkdir(parents=True, exist_ok=True)
    certificate_dir = outputs / "certificates"
    certificate_dir.mkdir(parents=True, exist_ok=True)

    model = build_model()
    coordinate_map = constrained_whitener(model)
    ordinates = _load_ordinates()
    energy, energy_bands = spectral_energy_matrix(model, coordinate_map)
    patches = default_cover()
    penalties = (0.0, 1.5e-4, 2e-4, 2.5e-4)
    candidates = generate_candidates(
        patches=patches,
        model=model,
        coordinate_map=coordinate_map,
        energy=energy,
        ordinates=ordinates,
        penalties=penalties,
        arithmetic_floor=5e-5,
        random_seed=20260724,
    )
    candidate_rows = [candidate.summary() for candidate in candidates]
    _write_json(outputs / "candidate_library.json", candidate_rows)
    _write_csv(
        outputs / "candidate_summary.csv",
        [
            {
                key: value
                for key, value in row.items()
                if key not in {"coefficients", "reduced_coefficients"}
            }
            for row in candidate_rows
        ],
    )

    certificates = []
    for patch in patches:
        certificate = build_patch_certificate(
            patch=patch,
            candidates=candidates,
            model=model,
        )
        certificates.append(certificate)
        _write_json(
            certificate_dir / f"{patch.patch_id}.certificate.json",
            certificate,
        )

    audit = coverage_audit(patches)
    certificate_rows = [
        {
            "patch_id": item["patch"]["patch_id"],
            "active_candidate_count": item["active_candidate_count"],
            "arithmetic_value": item["arithmetic_value"],
            "axis_band_energy": item["axis_band_energy"],
            "stage_one_axis_energy_optimum": item[
                "stage_one_axis_energy_optimum"
            ],
            "known_first_50_zero_mass_holdout": item[
                "known_first_50_zero_mass_holdout"
            ],
            "tail_majorant_from_145_prototype": item[
                "tail_majorant_from_145_prototype"
            ],
            "guard_positive_max": item["guard_positive_max"],
            "partial_gap": item[
                "partial_gap_excluding_other_off_axis_bands"
            ],
            "dense_core_max": item["dense_core_max"],
            "crude_continuous_upper_bound": item[
                "crude_continuous_upper_bound"
            ],
            "single_axis_energy": (
                item["single_candidate_baseline"]["axis_band_energy"]
                if item["single_candidate_baseline"]
                else None
            ),
            "stage_one_energy_improvement_vs_single_fraction": item[
                "stage_one_axis_energy_improvement_vs_single_fraction"
            ],
            "selected_energy_overhead_vs_single_fraction": item[
                "selected_axis_energy_overhead_vs_single_fraction"
            ],
            "selected_guard_improvement_vs_single_fraction": item[
                "selected_guard_improvement_vs_single_fraction"
            ],
            "sampled_core_pass": item["sampled_core_pass"],
            "crude_continuous_sign_pass": item[
                "crude_continuous_sign_pass"
            ],
            "global_certificate_pass": item["global_certificate_pass"],
        }
        for item in certificates
    ]
    _write_csv(outputs / "certificate_summary.csv", certificate_rows)

    summary = {
        "schema": "RH.BMCC.ExperimentSummary.v0.1",
        "research_mode": "semi-autonomous AI mathematical research",
        "provenance": {
            "technical_research_lead": "OpenAI Codex (AI research collaborator)",
            "research_field_and_authorization": "Neo.K / EveMissLab",
            "attribution_rule": (
                "Mathematical architecture, experiment choices, numerical "
                "interpretation, and next-node decisions in this package are "
                "AI research judgments unless explicitly marked otherwise."
            ),
        },
        "target_window": {
            "x": [20.0, 20.5],
            "y": [-0.2, -0.1],
        },
        "adaptive_cover_rule": (
            "Use height width 0.20 on the two farther distance strata and "
            "height width 0.10 on the two strata nearest the symmetry axis."
        ),
        "cover_audit": audit,
        "patch_count": len(patches),
        "candidate_count": len(candidates),
        "candidate_penalties": list(penalties),
        "known_zero_ordinates_used_in_optimization": False,
        "known_zero_ordinates_used_as_holdout_only": True,
        "axis_energy_bands": energy_bands,
        "structural_constraints": [
            "G(0)=0",
            "G(i/2)=0",
            "C0 norm = 1 for each rank-one candidate",
            "arithmetic scalar >= 5e-5 for each candidate",
            "nonnegative conic aggregation",
        ],
        "candidate_arithmetic_minimum": min(
            candidate.arithmetic_value for candidate in candidates
        ),
        "all_candidate_arithmetic_floor_pass": all(
            candidate.arithmetic_value >= 5e-5 - 2e-7
            for candidate in candidates
        ),
        "certificate_rows": certificate_rows,
        "all_sampled_core_pass": all(
            item["sampled_core_pass"] for item in certificates
        ),
        "all_crude_continuous_sign_pass": all(
            item["crude_continuous_sign_pass"] for item in certificates
        ),
        "crude_continuous_sign_pass_count": sum(
            item["crude_continuous_sign_pass"] for item in certificates
        ),
        "any_partial_budget_pass": any(
            item["partial_budget_pass"] for item in certificates
        ),
        "partial_budget_pass_count": sum(
            item["partial_budget_pass"] for item in certificates
        ),
        "partial_gap_range": [
            min(
                item["partial_gap_excluding_other_off_axis_bands"]
                for item in certificates
            ),
            max(
                item["partial_gap_excluding_other_off_axis_bands"]
                for item in certificates
            ),
        ],
        "global_certificate_pass": False,
        "global_failure_reasons": [
            "No interval arithmetic enclosure of the core or arithmetic form.",
            "The crude continuous sign audit may fail even when dense grids pass.",
            "Other off-axis bands do not yet have a signed global budget.",
            "The zero tail majorant is a floating prototype, not a formal bound object.",
        ],
        "next_node_decision": (
            "Keep the adaptive cover and upgrade the diagonal nonnegative "
            "cone to a full PSD Gram cone with off-diagonal cross terms."
        ),
        "related_ablation_output": "outputs/ablation_summary.json",
    }
    _write_json(outputs / "experiment_summary.json", summary)

    coefficient_bytes = json.dumps(
        [candidate.coefficients.tolist() for candidate in candidates],
        separators=(",", ":"),
    ).encode("utf-8")
    replay = {
        "schema": "RH.BMCC.Replay.v0.1",
        "command": "python run_experiment.py",
        "numpy_seed": 20260724,
        "candidate_coefficient_sha256": hashlib.sha256(
            coefficient_bytes
        ).hexdigest(),
        "output_files": [
            "outputs/experiment_summary.json",
            "outputs/candidate_library.json",
            "outputs/candidate_summary.csv",
            "outputs/certificate_summary.csv",
            "outputs/certificates/*.certificate.json",
        ],
    }
    _write_json(outputs / "replay.json", replay)
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
