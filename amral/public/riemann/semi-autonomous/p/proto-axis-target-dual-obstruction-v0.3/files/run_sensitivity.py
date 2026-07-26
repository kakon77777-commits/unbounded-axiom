from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

import numpy as np

from dualcert.context import TailDualContext, rational_patch_center
from dualcert.cover import default_cover
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


def patch_points() -> tuple[list[object], np.ndarray]:
    patches = default_cover()
    points = []
    for patch in patches:
        x, y = rational_patch_center(patch)
        points.append(complex(float(x), float(y)))
    return patches, np.asarray(points)


def witness_margin_rows(
    context: TailDualContext,
    axis_step: float,
    tail_fraction: float,
) -> list[float]:
    patches, points = patch_points()
    grid = np.linspace(
        18.0,
        23.0,
        int(round(5.0 / axis_step)) + 1,
    )
    count_floor = (
        np.floor(context.bands[1].count_majorant * 1e12) / 1e12
    )
    axis_average = context.uniform_axis_average(
        1, grid, count_coefficient=count_floor
    )
    transforms = context.transform(points)
    margins = []
    for transform in transforms:
        core = 2.0 * np.real(np.outer(transform, transform))
        witness = witness_matrix(
            context.tail_matrix,
            axis_average,
            core,
            alpha=2.0,
            tail_fraction=tail_fraction,
        )
        margins.append(float(np.linalg.eigvalsh(witness)[0]))
    assert len(margins) == len(patches)
    return margins


def main() -> None:
    outputs = ROOT / "outputs"
    outputs.mkdir(parents=True, exist_ok=True)
    patches, points = patch_points()
    baseline = TailDualContext()

    quadrature_rows = []
    for step in (0.02, 0.015, 0.01, 0.0075):
        context = TailDualContext(step=step)
        margins = witness_margin_rows(
            context,
            axis_step=0.2,
            tail_fraction=1e-3,
        )
        quadrature_rows.append(
            {
                "model_step": step,
                "minimum_margin": min(margins),
                "maximum_margin": max(margins),
                "pass_count": sum(value > 0.0 for value in margins),
            }
        )

    axis_grid_rows = []
    for axis_step in (0.2, 0.1, 0.05, 0.025, 0.0125):
        margins = witness_margin_rows(
            baseline,
            axis_step=axis_step,
            tail_fraction=1e-3,
        )
        axis_grid_rows.append(
            {
                "axis_step": axis_step,
                "axis_point_count": int(round(5.0 / axis_step)) + 1,
                "minimum_margin": min(margins),
                "maximum_margin": max(margins),
                "pass_count": sum(value > 0.0 for value in margins),
            }
        )

    tail_fraction_rows = []
    for tail_fraction in (
        0.0,
        1e-8,
        1e-7,
        1e-6,
        1e-5,
        1e-4,
        1e-3,
    ):
        margins = witness_margin_rows(
            baseline,
            axis_step=0.2,
            tail_fraction=tail_fraction,
        )
        tail_fraction_rows.append(
            {
                "tail_fraction": tail_fraction,
                "minimum_margin": min(margins),
                "maximum_margin": max(margins),
                "pass_count": sum(value > 0.0 for value in margins),
            }
        )

    radii = sorted(
        {
            *np.arange(2.0, 8.01, 0.5).round(10).tolist(),
            *np.arange(5.0, 5.51, 0.1).round(10).tolist(),
            *np.arange(8.2, 8.61, 0.05).round(10).tolist(),
            9.0,
            10.0,
        }
    )
    radius_rows = []
    for radius in radii:
        count = int(round(8.0 * radius))
        context = TailDualContext(radius=radius, count=count)
        transforms = context.transform(points)
        thresholds = []
        for transform in transforms:
            core = 2.0 * np.real(np.outer(transform, transform))
            thresholds.append(
                generalized_negative_threshold(
                    core,
                    context.tail_matrix,
                )
            )
        radius_rows.append(
            {
                "radius": radius,
                "basis_count": count,
                "dimension": context.dimension,
                "minimum_tail_only_alpha": min(thresholds),
                "maximum_tail_only_alpha": max(thresholds),
                "all_18_patches_tail_killed": min(thresholds) > 1.0,
                "all_18_patches_escape_center_tail_bound": (
                    max(thresholds) < 1.0
                ),
                "explicit_prime_cutoff_proxy": math.exp(2.0 * radius),
                "cutoff_ratio_vs_radius_3": math.exp(
                    2.0 * (radius - 3.0)
                ),
            }
        )

    decimal_rows = []
    axis_grid = np.linspace(18.0, 23.0, 26)
    for decimals in (6, 8, 10, 12):
        payload = make_rational_payload(
            baseline,
            patches,
            axis_grid,
            alpha=2,
            tail_fraction=Fraction(1, 1000),
            decimals=decimals,
        )
        verification = verify_rational_payload(payload)
        decimal_rows.append(
            {
                "decimal_places": decimals,
                "all_exact_ldl_positive": verification[
                    "all_exact_ldl_positive"
                ],
                "minimum_exact_ldl_pivot_float": min(
                    item["minimum_pivot_float"]
                    for item in verification["patch_rows"]
                ),
            }
        )

    first_any_escape = next(
        (
            row["radius"]
            for row in radius_rows
            if not row["all_18_patches_tail_killed"]
        ),
        None,
    )
    stable_all_escape = None
    for index, row in enumerate(radius_rows):
        if all(
            later["all_18_patches_escape_center_tail_bound"]
            for later in radius_rows[index:]
        ):
            stable_all_escape = row["radius"]
            break

    summary = {
        "schema": "RH.AxisTarget.DualSensitivity.v0.3",
        "quadrature_step_rows": quadrature_rows,
        "axis_grid_rows": axis_grid_rows,
        "tail_fraction_rows": tail_fraction_rows,
        "support_radius_rows": radius_rows,
        "decimal_rationalization_rows": decimal_rows,
        "first_sampled_radius_with_any_patch_escape": first_any_escape,
        "first_sampled_radius_with_stable_all_patch_escape": (
            stable_all_escape
        ),
        "primary_witness_stable": bool(
            all(
                row["pass_count"] == 18
                for row in quadrature_rows + axis_grid_rows
            )
            and decimal_rows[-1]["all_exact_ldl_positive"]
        ),
        "interpretation": (
            "The R=3 rejection is insensitive to the tested model and "
            "axis grids. Enlarging support while keeping roughly eight "
            "bumps per unit first lets some patches escape near R=5.1; "
            "all sampled patch centers remain below the tail-only unit "
            "bound only from the sampled R=8.5 suffix onward. This "
            "raises the prime-side cutoff proxy by about exp(11)."
        ),
        "global_rh_certificate": False,
    }
    write_json(outputs / "sensitivity.json", summary)
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
