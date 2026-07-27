from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np

from notch.codes import resolve_codes
from notch.context import FrontierContext
from notch.dual import (
    optimize_core_measure,
    rank_two_point_thresholds,
    uniform_core_threshold,
)
from notch.cover import Patch


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


def main() -> None:
    atlas = read_json(ROOT / "outputs" / "peak_atlas.json")
    rows = []
    for witness_path in selected_parent_witnesses():
        parent = read_json(witness_path)
        patch = Patch(**parent["patch"])
        patch_center = 0.5 * (patch.x_min + patch.x_max)
        points = patch.points(3, 3)
        for code in resolve_codes(
            patch_center,
            patch.x_min,
            patch.x_max,
            atlas,
        ):
            context = FrontierContext(
                radius=float(parent["configuration"]["radius"]),
                density=float(parent["configuration"]["density"]),
                width_factor=float(
                    parent["configuration"]["width_factor"]
                ),
                notch_points=code.value_points,
                derivative_notch_points=code.derivative_points,
            )
            base, base_metadata = context.base_matrix(
                (0, 1, 2, 3, 4),
                axis_step=0.05,
            )
            uniform_threshold = uniform_core_threshold(
                context,
                patch,
                base,
                nx=3,
                ny=3,
            )
            core_matrices = context.core_matrices(points)
            optimized_core = optimize_core_measure(
                core_matrices,
                base,
                maxiter=120,
            )
            center_transform = context.transform(
                np.asarray(
                    [
                        complex(
                            patch_center,
                            0.5 * (patch.y_min + patch.y_max),
                        )
                    ]
                )
            )
            center_threshold = float(
                rank_two_point_thresholds(
                    center_transform,
                    base,
                )[0]
            )
            value_residuals = (
                np.max(
                    np.abs(
                        context.transform(
                            np.asarray(
                                code.value_points,
                                dtype=complex,
                            )
                        )
                    )
                )
                if code.value_points
                else 0.0
            )
            derivative_residuals = (
                np.max(
                    np.abs(
                        context.derivative_transform(
                            np.asarray(
                                code.derivative_points,
                                dtype=complex,
                            )
                        )
                    )
                )
                if code.derivative_points
                else 0.0
            )
            derivative_at_anchor = context.derivative_transform(
                np.asarray([complex(patch_center)])
            )
            midpoint_y = 0.5 * (
                patch.y_min + patch.y_max
            )
            actual = context.transform(
                np.asarray(
                    [complex(patch_center, midpoint_y)]
                )
            )[0]
            taylor_leading = (
                1j
                * midpoint_y
                * derivative_at_anchor[0]
            )
            taylor_relative_error = float(
                np.linalg.norm(actual - taylor_leading)
                / max(np.linalg.norm(actual), 1e-15)
            )
            center_core_eigenvalues = np.linalg.eigvalsh(
                context.core_matrices(
                    np.asarray(
                        [complex(patch_center, midpoint_y)]
                    )
                )[0]
            )
            rows.append(
                {
                    "radius": context.radius,
                    "patch_id": patch.patch_id,
                    "code_id": code.code_id,
                    "interpretation": code.interpretation,
                    "value_notches": list(code.value_points),
                    "derivative_notches": list(
                        code.derivative_points
                    ),
                    "basis_count": context.count,
                    "dimension": context.dimension,
                    "constraint_metadata": (
                        context.constraint_metadata
                    ),
                    "value_notch_max_residual": float(
                        value_residuals
                    ),
                    "derivative_notch_max_residual": float(
                        derivative_residuals
                    ),
                    "anchor_derivative_frobenius_norm": float(
                        np.linalg.norm(derivative_at_anchor)
                    ),
                    "anchor_taylor_leading_relative_error": (
                        taylor_relative_error
                    ),
                    "center_core_minimum_eigenvalue": float(
                        center_core_eigenvalues[0]
                    ),
                    "center_core_negative_eigenvalue_count": int(
                        np.sum(center_core_eigenvalues < -1e-10)
                    ),
                    "center_point_threshold": center_threshold,
                    "uniform_axis_uniform_core_threshold": float(
                        uniform_threshold
                    ),
                    "optimized_core_uniform_axis_threshold": float(
                        optimized_core["threshold"]
                    ),
                    "core_optimizer_success": bool(
                        optimized_core["optimizer_success"]
                    ),
                    "base_metadata": base_metadata,
                }
            )

    ranked = {}
    for radius in sorted({row["radius"] for row in rows}):
        candidates = [
            row for row in rows if row["radius"] == radius
        ]
        ranked[str(radius)] = [
            row["code_id"]
            for row in sorted(
                candidates,
                key=lambda row: row[
                    "optimized_core_uniform_axis_threshold"
                ],
            )
        ]
    output = {
        "schema": "RH.AxisNotch.NotchScreen.v0.5",
        "axis_step": 0.05,
        "core_grid": [3, 3],
        "rows": rows,
        "ranked_code_ids_low_threshold_first": ranked,
        "interpretation": (
            "A lower searched dual threshold is favorable but is "
            "only a screen. Joint axis/core optimization and dense "
            "axis audit remain mandatory."
        ),
        "global_rh_certificate": False,
    }
    (ROOT / "outputs" / "notch_screen.json").write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
