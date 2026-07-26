from __future__ import annotations

import csv
import json
from fractions import Fraction
from pathlib import Path

import numpy as np

from dualcert.context import TailDualContext, rational_patch_center
from dualcert.cover import coverage_audit, default_cover
from dualcert.witness import (
    generalized_negative_threshold,
    make_rational_payload,
    verify_rational_payload,
    witness_matrix,
)


ROOT = Path(__file__).resolve().parent


def write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    outputs = ROOT / "outputs"
    witness_directory = outputs / "witnesses"
    outputs.mkdir(parents=True, exist_ok=True)
    witness_directory.mkdir(parents=True, exist_ok=True)

    context = TailDualContext()
    patches = default_cover()
    write_json(outputs / "cover_audit.json", coverage_audit(patches))
    axis_grid = np.linspace(18.0, 23.0, 26)
    band = context.bands[1]
    count_floor = np.floor(band.count_majorant * 1e12) / 1e12
    axis_average = context.uniform_axis_average(
        1,
        axis_grid,
        count_coefficient=count_floor,
    )
    alpha = 2.0
    tail_fraction = 1e-3
    stress_tail_fraction = 1e-6
    parent_results = {
        item["patch_id"]: item
        for item in json.loads(
            (ROOT / "data" / "parent_gram_results.json").read_text(
                encoding="utf-8"
            )
        )
    }

    tail_eigenvalues = np.linalg.eigvalsh(context.tail_matrix)
    rows = []
    for patch in patches:
        x, y = rational_patch_center(patch)
        point = complex(float(x), float(y))
        core = context.core_matrix(point)
        tail_threshold = generalized_negative_threshold(
            core, context.tail_matrix
        )
        hybrid_base = axis_average + tail_fraction * context.tail_matrix
        hybrid_threshold = generalized_negative_threshold(
            core, hybrid_base
        )
        tail_witness = witness_matrix(
            context.tail_matrix,
            np.zeros_like(axis_average),
            core,
            alpha=alpha,
            tail_fraction=1.0,
        )
        primary_witness = witness_matrix(
            context.tail_matrix,
            axis_average,
            core,
            alpha=alpha,
            tail_fraction=tail_fraction,
        )
        stress_witness = witness_matrix(
            context.tail_matrix,
            axis_average,
            core,
            alpha=alpha,
            tail_fraction=stress_tail_fraction,
        )
        axis_only = witness_matrix(
            context.tail_matrix,
            axis_average,
            core,
            alpha=alpha,
            tail_fraction=0.0,
        )
        parent_gram = np.asarray(
            parent_results[patch.patch_id]["gram"],
            dtype=float,
        )
        parent_center_value = float(np.sum(core * parent_gram))
        parent_dual_subobjective = float(
            np.sum(
                (
                    tail_fraction * context.tail_matrix
                    + axis_average
                )
                * parent_gram
            )
        )
        parent_witness_pairing = float(
            np.sum(primary_witness * parent_gram)
        )
        row = {
            "patch_id": patch.patch_id,
            "center": {"x": str(x), "y": str(y)},
            "alpha": alpha,
            "tail_fraction": tail_fraction,
            "axis_band_id": band.band_id,
            "axis_interval": [18.0, 23.0],
            "axis_grid_count": len(axis_grid),
            "axis_count_original": band.count_majorant,
            "axis_count_downward": count_floor,
            "tail_only_optimal_single_point_alpha": tail_threshold,
            "hybrid_optimal_single_point_alpha": hybrid_threshold,
            "tail_only_alpha_2_min_eigenvalue": float(
                np.linalg.eigvalsh(tail_witness)[0]
            ),
            "primary_alpha_2_min_eigenvalue": float(
                np.linalg.eigvalsh(primary_witness)[0]
            ),
            "stress_rho_1e_6_alpha_2_min_eigenvalue": float(
                np.linalg.eigvalsh(stress_witness)[0]
            ),
            "axis_only_alpha_2_min_eigenvalue": float(
                np.linalg.eigvalsh(axis_only)[0]
            ),
            "dual_lower_bound": alpha,
            "target_budget": 1.0,
            "finite_floating_dual_pass": bool(
                np.linalg.eigvalsh(primary_witness)[0] > 0.0
            ),
            "parent_primal_crosscheck": {
                "center_core_value": parent_center_value,
                "dual_subobjective_value": parent_dual_subobjective,
                "witness_pairing": parent_witness_pairing,
                "identity_residual": (
                    parent_dual_subobjective
                    + alpha * parent_center_value
                    - parent_witness_pairing
                ),
                "pairing_nonnegative": parent_witness_pairing >= -1e-10,
                "subobjective_at_least_2": (
                    parent_dual_subobjective >= 2.0 - 1e-10
                ),
            },
            "global_rh_certificate": False,
        }
        rows.append(row)
        write_json(
            witness_directory / f"{patch.patch_id}.witness.json",
            row,
        )

    rational_payload = make_rational_payload(
        context,
        patches,
        axis_grid,
        alpha=2,
        tail_fraction=Fraction(1, 1000),
        decimals=12,
    )
    rational_verification = verify_rational_payload(rational_payload)
    write_json(outputs / "rational_model.json", rational_payload)
    write_json(
        outputs / "rational_verification.json",
        rational_verification,
    )

    with (outputs / "witness_summary.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        fields = [
            "patch_id",
            "tail_only_optimal_single_point_alpha",
            "hybrid_optimal_single_point_alpha",
            "tail_only_alpha_2_min_eigenvalue",
            "primary_alpha_2_min_eigenvalue",
            "stress_rho_1e_6_alpha_2_min_eigenvalue",
            "axis_only_alpha_2_min_eigenvalue",
            "dual_lower_bound",
            "finite_floating_dual_pass",
        ]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(
            {field: row[field] for field in fields} for row in rows
        )

    summary = {
        "schema": "RH.AxisTarget.DualExperimentSummary.v0.3",
        "research_mode": "semi-autonomous AI mathematical research",
        "provenance": {
            "technical_research_lead": (
                "OpenAI Codex (AI research collaborator)"
            ),
            "research_field_and_authorization": "Neo.K / EveMissLab",
            "technical_judgments_attributed_to_ai": True,
        },
        "parent_node": "RH-PSDGRAM-20260724-v0.2",
        "patch_count": len(patches),
        "dimension": context.dimension,
        "known_zero_ordinates_used": False,
        "primary_witness": {
            "alpha": alpha,
            "tail_fraction": tail_fraction,
            "axis_band": "A1",
            "axis_interval": [18.0, 23.0],
            "axis_grid_count": len(axis_grid),
            "axis_measure": "uniform probability measure",
            "count_coefficient_downward": count_floor,
        },
        "finite_floating_pass_count": sum(
            row["finite_floating_dual_pass"] for row in rows
        ),
        "primary_min_eigenvalue_range": [
            min(row["primary_alpha_2_min_eigenvalue"] for row in rows),
            max(row["primary_alpha_2_min_eigenvalue"] for row in rows),
        ],
        "stress_rho_1e_6_min_eigenvalue_range": [
            min(
                row["stress_rho_1e_6_alpha_2_min_eigenvalue"]
                for row in rows
            ),
            max(
                row["stress_rho_1e_6_alpha_2_min_eigenvalue"]
                for row in rows
            ),
        ],
        "tail_only_optimal_alpha_range": [
            min(
                row["tail_only_optimal_single_point_alpha"]
                for row in rows
            ),
            max(
                row["tail_only_optimal_single_point_alpha"]
                for row in rows
            ),
        ],
        "hybrid_optimal_alpha_range": [
            min(
                row["hybrid_optimal_single_point_alpha"]
                for row in rows
            ),
            max(
                row["hybrid_optimal_single_point_alpha"]
                for row in rows
            ),
        ],
        "axis_only_min_eigenvalue_range": [
            min(
                row["axis_only_alpha_2_min_eigenvalue"]
                for row in rows
            ),
            max(
                row["axis_only_alpha_2_min_eigenvalue"]
                for row in rows
            ),
        ],
        "tail_matrix_min_eigenvalue": float(tail_eigenvalues[0]),
        "tail_matrix_positive_definite": bool(
            tail_eigenvalues[0] > 0.0
        ),
        "rational_surrogate_all_exact_ldl_positive": (
            rational_verification["all_exact_ldl_positive"]
        ),
        "parent_primal_crosscheck": {
            "all_pairings_nonnegative": all(
                row["parent_primal_crosscheck"][
                    "pairing_nonnegative"
                ]
                for row in rows
            ),
            "all_subobjectives_at_least_2": all(
                row["parent_primal_crosscheck"][
                    "subobjective_at_least_2"
                ]
                for row in rows
            ),
            "witness_pairing_range": [
                min(
                    row["parent_primal_crosscheck"][
                        "witness_pairing"
                    ]
                    for row in rows
                ),
                max(
                    row["parent_primal_crosscheck"][
                        "witness_pairing"
                    ]
                    for row in rows
                ),
            ],
            "identity_residual_abs_max": max(
                abs(
                    row["parent_primal_crosscheck"][
                        "identity_residual"
                    ]
                )
                for row in rows
            ),
        },
        "dual_lower_bound": alpha,
        "target_budget": 1.0,
        "current_r3_patchwise_function_class_rejected": True,
        "global_rh_certificate": False,
        "interpretation": (
            "For every patch, the finite-model objective is at least 2 "
            "whenever the block is at most -1 at the rational patch "
            "center. The target budget below 1 is therefore impossible "
            "for the current R=3 patchwise function class."
        ),
        "trust_boundary": (
            "Exact LDL positivity applies to the exported decimal-rational "
            "surrogate. Transfer to the Fourier integrals, count bound, "
            "and tail theorem remains E2 floating and is not an RH proof."
        ),
        "patch_rows": rows,
    }
    write_json(outputs / "experiment_summary.json", summary)
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
