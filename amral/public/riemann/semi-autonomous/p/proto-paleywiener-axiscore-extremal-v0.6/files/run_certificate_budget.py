from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from pwext.green import continuous_atomic_threshold
from pwext.model import PWGalerkinContext


ROOT = Path(__file__).resolve().parent


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    convergence = read_json(
        ROOT / "outputs" / "galerkin_joint_convergence.json"
    )
    joint = convergence["rows"][-1]["joint_dual"]
    coefficients = PWGalerkinContext(
        16.0,
        8,
        quadrature_order=512,
    ).count_coefficients
    rows = []
    alphas = (
        1.01,
        1.03,
        1.05,
        1.06,
        float(joint["safe_alpha"]),
    )
    for step in (0.01, 0.005, 0.0025):
        alpha_rows = []
        for alpha in alphas:
            result = continuous_atomic_threshold(
                radius=16.0,
                time_step=step,
                count_coefficients=coefficients,
                axis_supports=joint["axis_supports"],
                core_support=joint["core_support"],
                safe_alpha=alpha,
            )
            alpha_rows.append(
                {
                    "alpha": alpha,
                    "full_witness_minimum_eigenvalue": result[
                        "tested_safe_minimum_eigenvalue"
                    ],
                    "schur_minimum_eigenvalue": result[
                        "schur_certificate_minimum_eigenvalue"
                    ],
                    "positive_system_condition": result[
                        "positive_system_condition"
                    ],
                    "schur_matrix": result[
                        "schur_certificate_matrix"
                    ],
                }
            )
        rows.append(
            {
                "time_step": step,
                "alpha_rows": alpha_rows,
            }
        )
        print(json.dumps(rows[-1], ensure_ascii=False), flush=True)
    target = next(
        row
        for row in rows[-1]["alpha_rows"]
        if row["alpha"] == 1.05
    )
    previous_target = next(
        row
        for row in rows[-2]["alpha_rows"]
        if row["alpha"] == 1.05
    )
    output = {
        "schema": "RH.PaleyWiener.CertificateBudget.v0.6",
        "atomic_axis_support_count": sum(
            len(group) for group in joint["axis_supports"]
        ),
        "atomic_core_support_count": len(
            joint["core_support"]
        ),
        "positive_rank": 60,
        "negative_rank": 2,
        "rows": rows,
        "recommended_interval_target_alpha": 1.05,
        "recommended_target_alpha_margin_above_one": 0.05,
        "finest_target_full_witness_minimum_eigenvalue": target[
            "full_witness_minimum_eigenvalue"
        ],
        "finest_target_schur_minimum_eigenvalue": target[
            "schur_minimum_eigenvalue"
        ],
        "last_step_schur_drift": abs(
            target["schur_minimum_eigenvalue"]
            - previous_target["schur_minimum_eigenvalue"]
        ),
        "certification_reduction": (
            "After positive-axis and positive-core Woodbury "
            "reduction, continuous PSD is equivalent to a 2-by-2 "
            "Schur matrix being PSD."
        ),
        "interval_certified": False,
        "global_rh_certificate": False,
    }
    (
        ROOT / "outputs" / "certificate_budget.json"
    ).write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
