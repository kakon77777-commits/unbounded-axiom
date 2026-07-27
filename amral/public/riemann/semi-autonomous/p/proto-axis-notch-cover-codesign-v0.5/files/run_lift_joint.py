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


def frequency_grid(center: float, half_width: float) -> tuple[float, ...]:
    count = int(round(2.0 * half_width / 0.1)) + 1
    return tuple(
        float(value)
        for value in np.linspace(
            center - half_width,
            center + half_width,
            count,
        )
    )


def main() -> None:
    parent = read_json(
        ROOT
        / "data"
        / "parent_witnesses"
        / "R16_0__x4_Y3__r3_3.witness.json"
    )
    patch = Patch(**parent["patch"])
    center = 0.5 * (patch.x_min + patch.x_max)
    configurations = [
        ("baseline", (), (4,)),
        ("grid21_p4", frequency_grid(center, 1.0), (4,)),
    ]
    rows = []
    for lift_id, frequencies, powers in configurations:
        context = FrontierContext(
            radius=16.0,
            density=10.0,
            width_factor=1.5,
            spectral_lift_frequencies=frequencies,
            spectral_lift_powers=powers,
        )
        points = patch.points(3, 3)
        joint = cutting_plane_joint_dual(
            context,
            points,
            band_indices=(0, 1, 2, 3, 4),
            axis_step=0.05,
            max_outer=20,
            maxiter=200,
        )
        rank_one = audit_rank_one_direction(
            context,
            joint.minimum_generalized_vector,
            points,
            axis_step=0.025,
        )
        row: dict[str, Any] = {
            "lift_id": lift_id,
            "frequencies": list(frequencies),
            "powers": list(powers),
            "dimension": context.dimension,
            "effective_added_dimension": context.lift_metadata[
                "effective_added_dimension"
            ],
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
                random_count=48,
                bottom_count=16,
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

    baseline_alpha = rows[0]["joint_dual"]["alpha"]
    lifted_alpha = rows[1]["joint_dual"]["alpha"]
    output = {
        "schema": "RH.AxisNotch.LiftJoint.v0.5",
        "configuration": {
            "radius": 16.0,
            "patch": patch.to_dict(),
            "axis_step": 0.05,
            "dense_axis_audit_step": 0.025,
            "core_grid": [3, 3],
        },
        "rows": rows,
        "raw_alpha_relative_improvement": float(
            1.0 - lifted_alpha / baseline_alpha
        ),
        "lift_family_crosses_dual_gate": bool(
            rows[0]["joint_dual"]["safe_alpha"] > 1.0
            and rows[1]["joint_dual"]["safe_alpha"] < 1.0
        ),
        "interpretation": (
            "A reconstructed safe alpha above 1 blocks the finite "
            "primal branch. Alpha below 1 would only authorize a "
            "primal search; it would not prove feasibility."
        ),
        "global_rh_certificate": False,
    }
    (ROOT / "outputs" / "lift_joint.json").write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
