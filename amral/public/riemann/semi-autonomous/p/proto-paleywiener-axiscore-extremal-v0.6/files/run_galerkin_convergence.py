from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

from pwext.cover import Patch
from pwext.dual import cutting_plane_joint_dual
from pwext.model import PWGalerkinContext


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "outputs" / "galerkin_joint_convergence.json"


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_output(rows: list[dict[str, Any]]) -> None:
    output = {
        "schema": "RH.PaleyWiener.GalerkinJointConvergence.v0.6",
        "configuration": {
            "radius": 16.0,
            "raw_dimensions": [
                24, 40, 64, 80, 96, 120, 144, 160, 176, 192
            ],
            "quadrature_order": 2048,
            "axis_step": 0.1,
            "core_grid": [3, 3],
            "tail_inner_product": (
                "2*R*tail_multiplier*integral(psi''*phi'')"
            ),
            "basis_family": (
                "(1-u^2)^2*T_{2n}(u), with structural-zero "
                "projection and tail whitening"
            ),
        },
        "rows": rows,
        "all_safe_bounds_above_one": bool(
            rows
            and all(
                row["joint_dual"]["safe_alpha"] > 1.0
                for row in rows
            )
        ),
        "monotone_raw_alpha_nonincreasing": bool(
            all(
                right["joint_dual"]["alpha"]
                <= left["joint_dual"]["alpha"] + 2e-6
                for left, right in zip(rows[:-1], rows[1:])
            )
        ),
        "interpretation": (
            "Each row is a finite nested Galerkin obstruction. "
            "Only transfer of one atomic witness to the direct "
            "clamped Green kernel can support a continuous-space "
            "floating claim."
        ),
        "global_rh_certificate": False,
    }
    OUTPUT.write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parent = read_json(
        ROOT / "data" / "parent_geometry_joint.json"
    )
    patch = Patch(**parent["configuration"]["patch"])
    dimensions = [24, 40, 64, 80, 96, 120, 144, 160, 176, 192]
    rows: list[dict[str, Any]] = []
    for raw_dimension in dimensions:
        started = time.perf_counter()
        context = PWGalerkinContext(
            radius=16.0,
            raw_dimension=raw_dimension,
            quadrature_order=2048,
        )
        joint = cutting_plane_joint_dual(
            context,
            patch.points(3, 3),
            axis_step=0.1,
            max_outer=24,
            maxiter=260,
        )
        row = {
            "raw_dimension": raw_dimension,
            "effective_dimension": context.dimension,
            "structural_residuals": context.structural_residuals,
            "joint_dual": joint.to_summary(),
            "elapsed_seconds": float(
                time.perf_counter() - started
            ),
            "safe_budget_block": bool(
                joint.safe_alpha > 1.0
                and joint.safe_min_eigenvalue >= -1e-9
            ),
        }
        rows.append(row)
        write_output(rows)
        print(
            json.dumps(
                {
                    "raw_dimension": raw_dimension,
                    "effective_dimension": context.dimension,
                    "alpha": joint.alpha,
                    "safe_alpha": joint.safe_alpha,
                    "safe_min_eigenvalue": (
                        joint.safe_min_eigenvalue
                    ),
                    "outer_iterations": joint.outer_iterations,
                    "elapsed_seconds": row["elapsed_seconds"],
                },
                ensure_ascii=False,
            ),
            flush=True,
        )


if __name__ == "__main__":
    main()
