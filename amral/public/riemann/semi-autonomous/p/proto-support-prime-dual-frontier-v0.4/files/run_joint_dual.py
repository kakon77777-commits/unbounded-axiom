from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from frontier.context import FrontierContext
from frontier.cover import default_cover, refined_cover
from frontier.dual import (
    cutting_plane_joint_dual,
    optimize_core_measure,
    uniform_core_threshold,
)
from frontier.primal import (
    audit_gram_candidate,
    audit_rank_one_direction,
    candidate_rays_from_dual,
    solve_ray_cone_primal,
)
from frontier.primecost import cost_projection


ROOT = Path(__file__).resolve().parent


def write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def point_rows(points: np.ndarray) -> list[dict[str, float]]:
    return [
        {"x": float(point.real), "y": float(point.imag)}
        for point in points
    ]


def main() -> None:
    outputs = ROOT / "outputs"
    witnesses = outputs / "witnesses"
    outputs.mkdir(parents=True, exist_ok=True)
    witnesses.mkdir(parents=True, exist_ok=True)
    selected_geometry = {
        "density": 10.0,
        "width_factor": 1.5,
        "cover_split_x": 4,
        "cover_split_y": 4,
        "axis_grid_step": 0.05,
        "core_grid": [3, 3],
    }
    radii_and_search_counts = (
        (10.25, 2),
        (12.0, 2),
        (14.0, 3),
        (16.0, 5),
    )
    refined = refined_cover(default_cover(), 4, 4)
    radius_rows = []
    primal_rows = []
    for radius, search_count in radii_and_search_counts:
        context = FrontierContext(
            radius=radius,
            density=selected_geometry["density"],
            width_factor=selected_geometry["width_factor"],
        )
        uniform_base, base_metadata = context.base_matrix(
            (0, 1, 2, 3, 4),
                axis_step=selected_geometry["axis_grid_step"],
        )
        ranked = sorted(
            (
                (
                    uniform_core_threshold(
                        context,
                        patch,
                        uniform_base,
                        nx=3,
                        ny=3,
                    ),
                    patch,
                )
                for patch in refined
            ),
            key=lambda item: item[0],
            reverse=True,
        )
        candidate_rows = []
        candidate_objects = []
        for uniform_threshold, patch in ranked[:search_count]:
            points = patch.points(3, 3)
            core_matrices = context.core_matrices(points)
            core_only = optimize_core_measure(
                core_matrices,
                uniform_base,
            )
            joint = cutting_plane_joint_dual(
                context,
                points,
                band_indices=(0, 1, 2, 3, 4),
                axis_step=selected_geometry["axis_grid_step"],
                max_outer=16,
            )
            witness_payload = {
                "schema": "RH.SupportPrime.JointDualWitness.v0.4",
                "configuration": {
                    "radius": radius,
                    "density": context.density,
                    "width_factor": context.width_factor,
                    "basis_count": context.count,
                    "dimension": context.dimension,
                    "model_step": context.step,
                    "band_indices": [0, 1, 2, 3, 4],
                    "count_coefficients_downward": (
                        context.count_coefficients.tolist()
                    ),
                    "base_metadata": base_metadata,
                },
                "patch": patch.to_dict(),
                "core_points": point_rows(points),
                "uniform_axis_uniform_core_threshold": (
                    uniform_threshold
                ),
                "optimized_core_uniform_axis_threshold": (
                    core_only["threshold"]
                ),
                "joint_dual": joint.to_summary(),
                "dual_budget_block": bool(joint.safe_alpha > 1.0),
                "global_rh_certificate": False,
            }
            witness_path = (
                witnesses
                / f"R{str(radius).replace('.', '_')}"
                f"__{patch.patch_id}.witness.json"
            )
            write_json(witness_path, witness_payload)
            row = {
                "patch_id": patch.patch_id,
                "uniform_axis_uniform_core_threshold": (
                    uniform_threshold
                ),
                "optimized_core_uniform_axis_threshold": (
                    core_only["threshold"]
                ),
                "joint_alpha": joint.alpha,
                "safe_alpha": joint.safe_alpha,
                "safe_min_eigenvalue": (
                    joint.safe_min_eigenvalue
                ),
                "dual_budget_block": joint.safe_alpha > 1.0,
                "witness_file": str(
                    witness_path.relative_to(ROOT)
                ),
            }
            candidate_rows.append(row)
            candidate_objects.append((row, patch, points, joint))

        strongest = max(
            candidate_objects,
            key=lambda item: item[0]["joint_alpha"],
        )
        strongest_row, strongest_patch, points, strongest_joint = (
            strongest
        )
        rank_one = audit_rank_one_direction(
            context,
            strongest_joint.minimum_generalized_vector,
            points,
        )
        primal_row: dict[str, object] = {
            "radius": radius,
            "patch_id": strongest_patch.patch_id,
            "joint_alpha": strongest_joint.alpha,
            "rank_one_complementary_direction": rank_one,
        }
        if strongest_joint.alpha < 1.0:
            rays = candidate_rays_from_dual(
                context,
                points,
                strongest_joint,
            )
            ray_cone = solve_ray_cone_primal(
                context,
                points,
                rays,
                axis_step=0.25,
            )
            primal_row["ray_cone"] = ray_cone
            if ray_cone.get("solver_success"):
                primal_row["ray_cone_dense_audit"] = (
                    audit_gram_candidate(
                        context,
                        np.asarray(ray_cone["gram"]),
                        points,
                    )
                )
        primal_rows.append(primal_row)
        radius_rows.append(
            {
                "radius": radius,
                "basis_count": context.count,
                "dimension": context.dimension,
                "refined_patch_count": len(refined),
                "searched_candidate_count": search_count,
                "top_uniform_threshold": ranked[0][0],
                "strongest_searched_joint_alpha": (
                    strongest_row["joint_alpha"]
                ),
                "strongest_searched_safe_alpha": (
                    strongest_row["safe_alpha"]
                ),
                "at_least_one_searched_patch_blocked": any(
                    row["dual_budget_block"]
                    for row in candidate_rows
                ),
                "all_searched_patches_below_1": all(
                    row["joint_alpha"] < 1.0
                    for row in candidate_rows
                ),
                "candidate_rows": candidate_rows,
                "prime_cost_projection": cost_projection(
                    radius,
                    context.dimension,
                ),
            }
        )

    first_searched_escape = next(
        (
            row
            for row in radius_rows
            if row["all_searched_patches_below_1"]
        ),
        None,
    )
    output = {
        "schema": "RH.SupportPrime.JointDualSummary.v0.4",
        "selected_geometry": selected_geometry,
        "original_patch_count": len(default_cover()),
        "refined_patch_count": len(refined),
        "radius_rows": radius_rows,
        "first_sampled_radius_with_all_searched_patches_below_1": (
            first_searched_escape["radius"]
            if first_searched_escape is not None
            else None
        ),
        "full_refined_cover_joint_gate_exhausted": False,
        "full_refined_cover_joint_gate_pass": False,
        "interpretation": (
            "Every alpha above 1 is an explicit finite-model block. "
            "Alpha below 1 only records failure of the searched witness "
            "family; it is not proof that the full dual optimum is below 1."
        ),
        "global_rh_certificate": False,
    }
    write_json(outputs / "joint_dual_summary.json", output)
    write_json(
        outputs / "primal_diagnostics.json",
        {
            "schema": "RH.SupportPrime.PrimalDiagnostics.v0.4",
            "rows": primal_rows,
            "global_rh_certificate": False,
        },
    )
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
