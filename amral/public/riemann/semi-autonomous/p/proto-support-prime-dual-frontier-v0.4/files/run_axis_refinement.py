from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from frontier.context import FrontierContext
from frontier.cover import default_cover, refined_cover
from frontier.dual import cutting_plane_joint_dual


ROOT = Path(__file__).resolve().parent


def main() -> None:
    context = FrontierContext(
        radius=16.0,
        density=10.0,
        width_factor=1.5,
    )
    refined = refined_cover(default_cover(), 4, 4)
    patch = next(
        item
        for item in refined
        if item.patch_id == "x4_Y3__r2_3"
    )
    points = patch.points(3, 3)
    rows = []
    for step in (0.25, 0.1, 0.05, 0.025):
        result = cutting_plane_joint_dual(
            context,
            points,
            band_indices=(0, 1, 2, 3, 4),
            axis_step=step,
            max_outer=20,
        )
        rows.append(
            {
                "axis_step": step,
                "alpha": result.alpha,
                "safe_alpha": result.safe_alpha,
                "safe_min_eigenvalue": (
                    result.safe_min_eigenvalue
                ),
                "outer_iterations": result.outer_iterations,
                "active_axis_counts": (
                    result.active_axis_counts
                ),
                "axis_gradient_gaps": (
                    result.axis_gradient_gaps
                ),
            }
        )
    output = {
        "schema": "RH.SupportPrime.AxisRefinement.v0.4",
        "configuration": {
            "radius": 16.0,
            "density": 10.0,
            "width_factor": 1.5,
            "basis_count": context.count,
            "dimension": context.dimension,
            "patch": patch.to_dict(),
            "core_points": [
                {"x": float(point.real), "y": float(point.imag)}
                for point in points
            ],
        },
        "rows": rows,
        "coarse_grid_false_escape": bool(
            rows[0]["alpha"] < 1.0
            and rows[-1]["safe_alpha"] > 1.0
        ),
        "interpretation": (
            "Each discrete axis measure is a valid lower bound. "
            "Refinement expands the searched measure support and "
            "reveals peaks missed by the coarse grid; it is not an "
            "interval certificate of the continuous supremum."
        ),
        "global_rh_certificate": False,
    }
    (ROOT / "outputs" / "axis_refinement.json").write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
