from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

from frontier.context import FrontierContext
from frontier.cover import default_cover
from frontier.dual import (
    rank_two_point_thresholds,
    uniform_core_threshold,
)
from frontier.primecost import cost_projection


ROOT = Path(__file__).resolve().parent


def write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    radii = (
        4.5,
        5.0,
        5.5,
        6.0,
        7.0,
        8.0,
        9.0,
        10.0,
        10.25,
        10.5,
        11.0,
        12.0,
        14.0,
        16.0,
    )
    densities = (6.0, 8.0, 10.0)
    width_factors = (0.9, 1.2, 1.5)
    band_sets = {
        "tail_only": (),
        "single_A1": (1,),
        "three_A0_A2": (0, 1, 2),
        "five_A0_A4": (0, 1, 2, 3, 4),
    }
    patches = default_cover()
    centers = np.asarray(
        [
            complex(
                (patch.x_min + patch.x_max) / 2.0,
                (patch.y_min + patch.y_max) / 2.0,
            )
            for patch in patches
        ]
    )
    rows = []
    for radius in radii:
        for density in densities:
            for width_factor in width_factors:
                context = FrontierContext(
                    radius=radius,
                    density=density,
                    width_factor=width_factor,
                )
                transforms = context.transform(centers)
                threshold_rows = {}
                full_base = None
                for name, indices in band_sets.items():
                    base, _ = context.base_matrix(
                        indices,
                        axis_step=0.25,
                    )
                    thresholds = rank_two_point_thresholds(
                        transforms,
                        base,
                    )
                    threshold_rows[name] = {
                        "minimum": float(np.min(thresholds)),
                        "maximum": float(np.max(thresholds)),
                        "all_18_centers_below_1": bool(
                            np.max(thresholds) < 1.0
                        ),
                    }
                    if name == "five_A0_A4":
                        full_base = base
                assert full_base is not None
                patch_thresholds = [
                    uniform_core_threshold(
                        context,
                        patch,
                        full_base,
                        nx=3,
                        ny=3,
                    )
                    for patch in patches
                ]
                rows.append(
                    {
                        "radius": radius,
                        "density": density,
                        "width_factor": width_factor,
                        "basis_count": context.count,
                        "dimension": context.dimension,
                        "model_step": context.step,
                        "axis_measure_step": 0.25,
                        "center_thresholds": threshold_rows,
                        "full5_original_patch_uniform_3x3": {
                            "minimum": min(patch_thresholds),
                            "maximum": max(patch_thresholds),
                            "all_18_patches_below_1": (
                                max(patch_thresholds) < 1.0
                            ),
                        },
                        "prime_cost_projection": cost_projection(
                            radius,
                            context.dimension,
                        ),
                    }
                )

    best_by_radius = []
    for radius in radii:
        candidates = [
            row for row in rows if row["radius"] == radius
        ]
        best = min(
            candidates,
            key=lambda row: row[
                "full5_original_patch_uniform_3x3"
            ]["maximum"],
        )
        best_by_radius.append(
            {
                "radius": radius,
                "density": best["density"],
                "width_factor": best["width_factor"],
                "basis_count": best["basis_count"],
                "dimension": best["dimension"],
                "best_uniform_patch_maximum": best[
                    "full5_original_patch_uniform_3x3"
                ]["maximum"],
                "full5_center_maximum": best[
                    "center_thresholds"
                ]["five_A0_A4"]["maximum"],
                "cutoff_float": math.exp(2.0 * radius),
            }
        )

    first_center_escape = next(
        (
            row
            for row in rows
            if row["center_thresholds"]["five_A0_A4"][
                "all_18_centers_below_1"
            ]
        ),
        None,
    )
    first_uniform_patch_escape = next(
        (
            row
            for row in rows
            if row["full5_original_patch_uniform_3x3"][
                "all_18_patches_below_1"
            ]
        ),
        None,
    )
    output = {
        "schema": "RH.SupportPrime.UniformFrontier.v0.4",
        "research_mode": "semi-autonomous AI mathematical research",
        "profile": "published Trudgian constants, floating evaluation",
        "row_count": len(rows),
        "radii": list(radii),
        "densities": list(densities),
        "width_factors": list(width_factors),
        "band_sets": {
            name: list(indices)
            for name, indices in band_sets.items()
        },
        "rows": rows,
        "best_by_radius": best_by_radius,
        "first_sampled_any_geometry_center_escape": (
            {
                key: first_center_escape[key]
                for key in (
                    "radius",
                    "density",
                    "width_factor",
                    "basis_count",
                    "dimension",
                )
            }
            if first_center_escape is not None
            else None
        ),
        "first_sampled_any_geometry_uniform_patch_escape": (
            {
                key: first_uniform_patch_escape[key]
                for key in (
                    "radius",
                    "density",
                    "width_factor",
                    "basis_count",
                    "dimension",
                )
            }
            if first_uniform_patch_escape is not None
            else None
        ),
        "interpretation": (
            "Uniform axis and core measures are valid lower-bound "
            "witnesses but are not optimized dual gates. Joint "
            "axis/core measure optimization is reported separately."
        ),
        "global_rh_certificate": False,
    }
    write_json(ROOT / "outputs" / "uniform_frontier.json", output)
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
