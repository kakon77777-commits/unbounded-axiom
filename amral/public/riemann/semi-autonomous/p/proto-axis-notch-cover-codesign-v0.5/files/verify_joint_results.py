from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np

from notch.context import FrontierContext


ROOT = Path(__file__).resolve().parent


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def reconstruct(
    context: FrontierContext,
    joint: dict[str, Any],
) -> dict[str, Any]:
    base = context.tail_matrix.copy()
    raw_axis_sums = []
    for band_index, support in enumerate(joint["axis_supports"]):
        raw_weights = np.asarray(
            [row["weight"] for row in support],
            dtype=float,
        )
        raw_sum = float(np.sum(raw_weights))
        weights = raw_weights / raw_sum
        points = np.asarray(
            [row["x"] for row in support],
            dtype=float,
        )
        transforms = context.axis_transforms(points)
        base += (
            context.count_coefficients[band_index]
            * np.tensordot(
                weights,
                np.einsum(
                    "ki,kj->kij",
                    transforms,
                    transforms,
                ),
                axes=1,
            )
        )
        raw_axis_sums.append(raw_sum)
    core_support = joint["core_support"]
    raw_core_weights = np.asarray(
        [row["weight"] for row in core_support],
        dtype=float,
    )
    raw_core_sum = float(np.sum(raw_core_weights))
    core_weights = raw_core_weights / raw_core_sum
    core_points = np.asarray(
        [
            complex(row["x"], row["y"])
            for row in core_support
        ]
    )
    core = np.tensordot(
        core_weights,
        context.core_matrices(core_points),
        axes=1,
    )
    witness = (
        base + float(joint["safe_alpha"]) * core
    )
    minimum = float(
        np.linalg.eigvalsh(
            0.5 * (witness + witness.T)
        )[0]
    )
    return {
        "minimum_eigenvalue": minimum,
        "stored_minimum_eigenvalue": float(
            joint["safe_min_eigenvalue"]
        ),
        "minimum_eigenvalue_abs_difference": abs(
            minimum - float(joint["safe_min_eigenvalue"])
        ),
        "raw_axis_weight_sums": raw_axis_sums,
        "raw_core_weight_sum": raw_core_sum,
        "normalized_measure_convention": True,
        "safe_budget_block": bool(
            minimum >= -1e-9
            and float(joint["safe_alpha"]) > 1.0
        ),
    }


def verify_all() -> dict[str, Any]:
    lift = read_json(ROOT / "outputs" / "lift_joint.json")
    geometry = read_json(ROOT / "outputs" / "geometry_joint.json")
    rows = []
    for row in lift["rows"]:
        context = FrontierContext(
            radius=16.0,
            density=10.0,
            width_factor=1.5,
            bump_power=3,
            spectral_lift_frequencies=tuple(
                row["frequencies"]
            ),
            spectral_lift_powers=tuple(row["powers"]),
        )
        rows.append(
            {
                "family": "lift",
                "configuration_id": row["lift_id"],
                "dimension": context.dimension,
                "reconstruction": reconstruct(
                    context,
                    row["joint_dual"],
                ),
            }
        )
    for row in geometry["rows"]:
        context = FrontierContext(
            radius=16.0,
            density=float(row["density"]),
            width_factor=float(row["width_factor"]),
            bump_power=int(row["bump_power"]),
        )
        rows.append(
            {
                "family": "geometry",
                "configuration_id": row["geometry_id"],
                "dimension": context.dimension,
                "reconstruction": reconstruct(
                    context,
                    row["joint_dual"],
                ),
            }
        )
    return {
        "schema": "RH.AxisNotch.JointVerification.v0.5",
        "row_count": len(rows),
        "rows": rows,
        "all_reconstructed_psd_and_block_budget": all(
            row["reconstruction"]["safe_budget_block"]
            for row in rows
        ),
        "maximum_minimum_eigenvalue_abs_difference": max(
            row["reconstruction"][
                "minimum_eigenvalue_abs_difference"
            ]
            for row in rows
        ),
        "verification_level": (
            "E2 floating reconstruction with normalized serialized "
            "measures; no interval analytic transfer"
        ),
        "global_rh_certificate": False,
    }


def main() -> None:
    output = verify_all()
    (ROOT / "outputs" / "joint_verification.json").write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, indent=2, ensure_ascii=False))
    if not output["all_reconstructed_psd_and_block_budget"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
