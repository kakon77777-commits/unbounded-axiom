from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np

from notch.context import FrontierContext
from notch.cover import Patch
from notch.dual import cutting_plane_joint_dual
from notch.primal import (
    audit_gram_candidate,
    audit_rank_one_direction,
    candidate_rays_from_dual,
    solve_ray_cone_primal,
)


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
    prior_joint = read_json(ROOT / "outputs" / "lift_joint.json")
    baseline = next(
        row
        for row in prior_joint["rows"]
        if row["lift_id"] == "baseline"
    )
    patch = Patch(**parent["patch"])
    configurations = [
        {
            "geometry_id": "d10_w2_p4",
            "density": 10.0,
            "width_factor": 2.0,
            "bump_power": 4,
        },
        {
            "geometry_id": "d12_w2_p5",
            "density": 12.0,
            "width_factor": 2.0,
            "bump_power": 5,
        },
    ]
    rows = []
    for configuration in configurations:
        context = FrontierContext(
            radius=16.0,
            density=configuration["density"],
            width_factor=configuration["width_factor"],
            bump_power=configuration["bump_power"],
        )
        points = patch.points(3, 3)
        joint = cutting_plane_joint_dual(
            context,
            points,
            band_indices=(0, 1, 2, 3, 4),
            axis_step=0.05,
            max_outer=20,
            maxiter=220,
        )
        rank_one = audit_rank_one_direction(
            context,
            joint.minimum_generalized_vector,
            points,
            axis_step=0.025,
        )
        row: dict[str, Any] = {
            **configuration,
            "basis_count": context.count,
            "dimension": context.dimension,
            "bump_width": float(context.model["width"]),
            "joint_dual": joint.to_summary(),
            "safe_budget_block": bool(joint.safe_alpha > 1.0),
            "rank_one_complementary_audit": rank_one,
            "primal_search_started": False,
        }
        if joint.safe_alpha < 1.0:
            row["primal_search_started"] = True
            rays = candidate_rays_from_dual(
                context,
                points,
                joint,
                random_count=64,
                bottom_count=20,
            )
            ray_cone = solve_ray_cone_primal(
                context,
                points,
                rays,
                axis_step=0.05,
            )
            row["ray_cone"] = ray_cone
            if ray_cone.get("solver_success"):
                row["ray_cone_dense_audit"] = (
                    audit_gram_candidate(
                        context,
                        np.asarray(ray_cone["gram"]),
                        points,
                        axis_step=0.025,
                    )
                )
        rows.append(row)

    baseline_alpha = float(baseline["joint_dual"]["alpha"])
    for row in rows:
        row["raw_alpha_relative_improvement_vs_baseline"] = float(
            1.0 - row["joint_dual"]["alpha"] / baseline_alpha
        )
    output = {
        "schema": "RH.AxisNotch.GeometryJoint.v0.5",
        "configuration": {
            "radius": 16.0,
            "patch": patch.to_dict(),
            "axis_step": 0.05,
            "dense_axis_audit_step": 0.025,
            "core_grid": [3, 3],
        },
        "baseline": {
            "geometry_id": "d10_w1_5_p3",
            "dimension": baseline["dimension"],
            "joint_dual": baseline["joint_dual"],
        },
        "rows": rows,
        "any_geometry_crosses_dual_gate": any(
            not row["safe_budget_block"] for row in rows
        ),
        "interpretation": (
            "The geometry screen nominates nonnested dictionaries. "
            "Only a safe alpha below 1 authorizes primal search."
        ),
        "global_rh_certificate": False,
    }
    (ROOT / "outputs" / "geometry_joint.json").write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
