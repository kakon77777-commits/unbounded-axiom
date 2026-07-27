from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np

from notch.context import FrontierContext
from notch.cover import Patch
from notch.dual import (
    optimize_core_measure,
    rank_two_point_thresholds,
    uniform_core_threshold,
)


ROOT = Path(__file__).resolve().parent


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def selected_parent_witnesses() -> list[Path]:
    return [
        ROOT
        / "data"
        / "parent_witnesses"
        / "R10_25__x5_Y3__r3_3.witness.json",
        ROOT
        / "data"
        / "parent_witnesses"
        / "R16_0__x4_Y3__r3_3.witness.json",
    ]


def lift_families(
    center: float,
    atlas_a1: float,
    atlas_a3: float,
    atlas_a4: float,
) -> list[dict[str, object]]:
    return [
        {
            "lift_id": "baseline",
            "frequencies": (),
            "powers": (4,),
        },
        {
            "lift_id": "slope1",
            "frequencies": (center,),
            "powers": (4,),
        },
        {
            "lift_id": "slope3",
            "frequencies": (
                center - 0.1,
                center,
                center + 0.1,
            ),
            "powers": (4,),
        },
        {
            "lift_id": "slope5",
            "frequencies": (
                center - 0.2,
                center - 0.1,
                center,
                center + 0.1,
                center + 0.2,
            ),
            "powers": (4,),
        },
        {
            "lift_id": "slope_powers3",
            "frequencies": (center,),
            "powers": (4, 6, 8),
        },
        {
            "lift_id": "slope_grid6",
            "frequencies": (
                center - 0.15,
                center,
                center + 0.15,
            ),
            "powers": (4, 6),
        },
        {
            "lift_id": "atlas_A1_powers",
            "frequencies": (atlas_a1,),
            "powers": (4, 6, 8),
        },
        {
            "lift_id": "center_A3_A4",
            "frequencies": (center, atlas_a3, atlas_a4),
            "powers": (4,),
        },
    ]


def main() -> None:
    atlas = read_json(ROOT / "outputs" / "peak_atlas.json")
    peaks = {
        row["band_id"]: round(
            float(row["primary_peak"]["x"]),
            2,
        )
        for row in atlas["band_rows"]
    }
    rows = []
    for witness_path in selected_parent_witnesses():
        parent = read_json(witness_path)
        patch = Patch(**parent["patch"])
        center_x = 0.5 * (patch.x_min + patch.x_max)
        center_y = 0.5 * (patch.y_min + patch.y_max)
        core_points = patch.points(3, 3)
        for family in lift_families(
            center_x,
            peaks["A1"],
            peaks["A3"],
            peaks["A4"],
        ):
            frequencies = tuple(
                float(value)
                for value in family["frequencies"]
            )
            powers = tuple(
                int(value) for value in family["powers"]
            )
            context = FrontierContext(
                radius=float(parent["configuration"]["radius"]),
                density=float(parent["configuration"]["density"]),
                width_factor=float(
                    parent["configuration"]["width_factor"]
                ),
                spectral_lift_frequencies=frequencies,
                spectral_lift_powers=powers,
            )
            base, _ = context.base_matrix(
                (0, 1, 2, 3, 4),
                axis_step=0.05,
            )
            core_matrices = context.core_matrices(core_points)
            optimized_core = optimize_core_measure(
                core_matrices,
                base,
                maxiter=120,
            )
            center_transform = context.transform(
                np.asarray([complex(center_x, center_y)])
            )
            center_threshold = float(
                rank_two_point_thresholds(
                    center_transform,
                    base,
                )[0]
            )
            uniform_threshold = float(
                uniform_core_threshold(
                    context,
                    patch,
                    base,
                    nx=3,
                    ny=3,
                )
            )
            derivative = context.derivative_transform(
                np.asarray([complex(center_x)])
            )
            center_core_eigenvalues = np.linalg.eigvalsh(
                context.core_matrices(
                    np.asarray([complex(center_x, center_y)])
                )[0]
            )
            rows.append(
                {
                    "radius": context.radius,
                    "patch_id": patch.patch_id,
                    "lift_id": family["lift_id"],
                    "frequencies": list(frequencies),
                    "powers": list(powers),
                    "local_basis_count": context.local_count,
                    "total_basis_count": context.count,
                    "dimension": context.dimension,
                    "lift_metadata": context.lift_metadata,
                    "center_point_threshold": center_threshold,
                    "uniform_axis_uniform_core_threshold": (
                        uniform_threshold
                    ),
                    "optimized_core_uniform_axis_threshold": float(
                        optimized_core["threshold"]
                    ),
                    "anchor_derivative_frobenius_norm": float(
                        np.linalg.norm(derivative)
                    ),
                    "center_core_minimum_eigenvalue": float(
                        center_core_eigenvalues[0]
                    ),
                    "tail_minimum_eigenvalue": float(
                        np.linalg.eigvalsh(
                            context.tail_matrix
                        )[0]
                    ),
                    "core_optimizer_success": bool(
                        optimized_core["optimizer_success"]
                    ),
                }
            )

    ranked = {}
    for radius in sorted({row["radius"] for row in rows}):
        candidates = [
            row for row in rows if row["radius"] == radius
        ]
        ranked[str(radius)] = [
            row["lift_id"]
            for row in sorted(
                candidates,
                key=lambda row: row[
                    "optimized_core_uniform_axis_threshold"
                ],
            )
        ]
    output = {
        "schema": "RH.AxisNotch.LiftScreen.v0.5",
        "atom_family": "t*q_R(t)*sin(omega*t)",
        "axis_step": 0.05,
        "core_grid": [3, 3],
        "rows": rows,
        "ranked_lift_ids_low_threshold_first": ranked,
        "subspace_monotonicity_note": (
            "Linear notch constraints alone restrict the parent "
            "space and cannot improve primal feasibility. These "
            "spectral atoms instead enlarge the dictionary."
        ),
        "global_rh_certificate": False,
    }
    (ROOT / "outputs" / "lift_screen.json").write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
