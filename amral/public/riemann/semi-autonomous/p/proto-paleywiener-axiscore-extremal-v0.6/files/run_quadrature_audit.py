from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np

from pwext.axis import default_axis_bands, downward_count_majorant
from pwext.cover import Patch
from pwext.green import GreenRankTwoScanner
from pwext.model import PWGalerkinContext


ROOT = Path(__file__).resolve().parent


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    parent = read_json(
        ROOT / "data" / "parent_geometry_joint.json"
    )
    patch = Patch(**parent["configuration"]["patch"])
    point = complex(
        0.5 * (patch.x_min + patch.x_max),
        0.5 * (patch.y_min + patch.y_max),
    )
    axis_x = 20.4
    coefficient = downward_count_majorant(
        default_axis_bands()[1]
    )
    galerkin_rows = []
    for raw_dimension in (
        40, 64, 80, 96, 112, 128, 144, 160, 176, 192
    ):
        context = PWGalerkinContext(
            16.0,
            raw_dimension,
            quadrature_order=2048,
        )
        galerkin_rows.append(
            {
                "raw_dimension": raw_dimension,
                "effective_dimension": context.dimension,
                "point_extremal": context.point_extremal(
                    axis_x,
                    point,
                    coefficient,
                ),
                "maximum_structural_residual": max(
                    context.structural_residuals.values()
                ),
            }
        )
    quadrature_rows = []
    for order in (1024, 1536, 2048, 2560):
        context = PWGalerkinContext(
            16.0,
            192,
            quadrature_order=order,
        )
        quadrature_rows.append(
            {
                "quadrature_order": order,
                "effective_dimension": context.dimension,
                "point_extremal": context.point_extremal(
                    axis_x,
                    point,
                    coefficient,
                ),
            }
        )
    green_rows = []
    for step in (0.02, 0.01, 0.005, 0.0025):
        scanner = GreenRankTwoScanner(16.0, step)
        scan = scanner.scan(
            np.asarray([axis_x]),
            point,
            coefficient,
        )
        green_rows.append(
            {
                "time_step": scanner.actual_step,
                "time_grid_count": len(scanner.t),
                "point_extremal": float(
                    np.asarray(scan["thresholds"])[0]
                ),
            }
        )
    output = {
        "schema": "RH.PaleyWiener.QuadratureAudit.v0.6",
        "configuration": {
            "radius": 16.0,
            "axis_x": axis_x,
            "core_point": {
                "x": point.real,
                "y": point.imag,
            },
            "band": "A1",
            "count_coefficient": coefficient,
        },
        "galerkin_dimension_rows": galerkin_rows,
        "galerkin_quadrature_rows_at_raw_dimension_192": (
            quadrature_rows
        ),
        "direct_green_rows": green_rows,
        "galerkin_approaches_direct_green_from_above": bool(
            galerkin_rows[-1]["point_extremal"]
            > green_rows[-1]["point_extremal"]
            and all(
                right["point_extremal"]
                <= left["point_extremal"] + 2e-6
                for left, right in zip(
                    galerkin_rows[:-1],
                    galerkin_rows[1:],
                )
            )
        ),
        "interval_certified": False,
        "global_rh_certificate": False,
    }
    (
        ROOT / "outputs" / "quadrature_audit.json"
    ).write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
