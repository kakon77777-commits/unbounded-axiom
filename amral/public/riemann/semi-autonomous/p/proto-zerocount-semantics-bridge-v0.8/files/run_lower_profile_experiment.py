from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np

from bridge.axis import lower_profile_downward
from bridge.cover import Patch
from bridge.galerkin import (
    PWGalerkinContext,
    cutting_plane_joint_dual,
    dense_primal_escape_diagnostic,
)
from bridge.green import continuous_atomic_threshold


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "outputs" / "lower_profile_experiment.json"
PATCH = Patch(
    patch_id="x4_Y3__r3_3",
    x_min=20.395,
    x_max=20.42,
    y_min=-0.10625,
    y_max=-0.1,
    guard_dx=0.00375,
    guard_dy=0.0015,
)
RAW_DIMENSIONS = (24, 40, 64, 80, 96, 120, 144, 160, 176, 192)


def main() -> None:
    profile = tuple(lower_profile_downward())
    rows: list[dict[str, Any]] = []
    final_context: PWGalerkinContext | None = None
    final_result = None
    for raw_dimension in RAW_DIMENSIONS:
        context = PWGalerkinContext(
            radius=16.0,
            raw_dimension=raw_dimension,
            count_coefficients_input=profile,
            quadrature_order=2048,
        )
        result = cutting_plane_joint_dual(
            context,
            PATCH.points(3, 3),
            axis_step=0.05,
            initial_axis_nodes=7,
            max_outer=28,
            maxiter=320,
        )
        rows.append(
            {
                "raw_dimension": raw_dimension,
                "effective_dimension": context.dimension,
                "alpha": result.alpha,
                "safe_alpha": result.safe_alpha,
                "safe_minimum_eigenvalue": (
                    result.safe_min_eigenvalue
                ),
                "outer_iterations": result.outer_iterations,
                "optimizer_success": result.optimizer_success,
            }
        )
        final_context = context
        final_result = result
    assert final_context is not None
    assert final_result is not None

    direct_green = []
    for step in (0.02, 0.01, 0.005):
        direct_green.append(
            continuous_atomic_threshold(
                radius=16.0,
                time_step=step,
                count_coefficients=np.asarray(profile),
                axis_supports=final_result.axis_supports,
                core_support=final_result.core_support,
                tail_scale_override=final_context.tail_scale,
            )
        )
    primal = dense_primal_escape_diagnostic(
        final_context,
        final_result.minimum_generalized_vector,
        PATCH,
        core_grid_size=101,
        axis_step=0.01,
    )
    output = {
        "schema": "RH.LowerProfile.RobustSearch.v0.8",
        "configuration": {
            "radius": 16.0,
            "patch": PATCH.__dict__,
            "count_profile": list(profile),
            "profile_status": (
                "floating downward-rounded lower candidate; not a "
                "zeta-facing operator lower certificate"
            ),
            "raw_dimensions": list(RAW_DIMENSIONS),
            "quadrature_order": 2048,
            "axis_step": 0.05,
            "core_measure_grid": [3, 3],
        },
        "galerkin_rows": rows,
        "final_atomic_measures": {
            "axis_supports": final_result.axis_supports,
            "core_support": final_result.core_support,
        },
        "direct_green_transfer": direct_green,
        "primal_escape_diagnostic": primal,
        "first_dimension_below_one": next(
            row["raw_dimension"]
            for row in rows
            if row["alpha"] < 1.0
        ),
        "high_dimension_obstruction_above_one": bool(
            rows[-1]["alpha"] > 1.0
        ),
        "fixed_measure_direct_threshold_last": direct_green[-1][
            "raw_threshold_for_fixed_measures"
        ],
        "interpretation": (
            "Under the lower candidate profile the high-dimensional "
            "abstract envelope obstruction disappears. This does not "
            "repair the actual-zero operator bridge, because count "
            "lower bounds do not locate the zeros."
        ),
        "interval_certified": False,
        "actual_zero_side_theorem": False,
        "global_rh_certificate": False,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
