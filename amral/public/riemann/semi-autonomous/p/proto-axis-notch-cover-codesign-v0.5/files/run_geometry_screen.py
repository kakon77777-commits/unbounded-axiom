from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np

from notch.context import FrontierContext
from notch.cover import Patch
from notch.dual import optimize_core_measure, uniform_core_threshold


ROOT = Path(__file__).resolve().parent


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    parent = read_json(
        ROOT
        / "data"
        / "parent_witnesses"
        / "R16_0__x4_Y3__r3_3.witness.json"
    )
    patch = Patch(**parent["patch"])
    densities = (10.0, 12.0, 14.0)
    width_factors = (1.2, 1.5, 2.0)
    bump_powers = (3, 4, 5)
    rows = []
    for density in densities:
        for width_factor in width_factors:
            for bump_power in bump_powers:
                context = FrontierContext(
                    radius=16.0,
                    density=density,
                    width_factor=width_factor,
                    bump_power=bump_power,
                )
                base, _ = context.base_matrix(
                    (0, 1, 2, 3, 4),
                    axis_step=0.05,
                )
                points = patch.points(3, 3)
                optimized = optimize_core_measure(
                    context.core_matrices(points),
                    base,
                    maxiter=120,
                )
                rows.append(
                    {
                        "density": density,
                        "width_factor": width_factor,
                        "bump_power": bump_power,
                        "basis_count": context.count,
                        "dimension": context.dimension,
                        "bump_width": float(
                            context.model["width"]
                        ),
                        "quadrature_points_per_width": float(
                            context.model["width"] / context.step
                        ),
                        "uniform_axis_uniform_core_threshold": float(
                            uniform_core_threshold(
                                context,
                                patch,
                                base,
                                nx=3,
                                ny=3,
                            )
                        ),
                        "optimized_core_uniform_axis_threshold": float(
                            optimized["threshold"]
                        ),
                        "tail_minimum_eigenvalue": float(
                            np.linalg.eigvalsh(
                                context.tail_matrix
                            )[0]
                        ),
                        "core_optimizer_success": bool(
                            optimized["optimizer_success"]
                        ),
                    }
                )
    ranked = sorted(
        rows,
        key=lambda row: row[
            "optimized_core_uniform_axis_threshold"
        ],
    )
    output = {
        "schema": "RH.AxisNotch.GeometryScreen.v0.5",
        "configuration": {
            "radius": 16.0,
            "patch": patch.to_dict(),
            "axis_step": 0.05,
            "core_grid": [3, 3],
            "densities": list(densities),
            "width_factors": list(width_factors),
            "bump_powers": list(bump_powers),
        },
        "row_count": len(rows),
        "rows": rows,
        "top_five": ranked[:5],
        "interpretation": (
            "These dictionaries are not nested. Lower uniform/core "
            "thresholds only nominate configurations for joint dual; "
            "they do not pass the gate."
        ),
        "global_rh_certificate": False,
    }
    (ROOT / "outputs" / "geometry_screen.json").write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
