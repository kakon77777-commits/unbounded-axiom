from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np

from notch.context import FrontierContext
from notch.cover import Patch
from notch.dual import optimize_core_measure, uniform_core_threshold


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
    families = [
        ("baseline", (), (4,)),
        ("grid5_p4", frequency_grid(center, 0.2), (4,)),
        ("grid9_p4", frequency_grid(center, 0.4), (4,)),
        ("grid13_p4", frequency_grid(center, 0.6), (4,)),
        ("grid21_p4", frequency_grid(center, 1.0), (4,)),
        ("grid9_p46", frequency_grid(center, 0.4), (4, 6)),
        ("grid13_p46", frequency_grid(center, 0.6), (4, 6)),
        ("grid9_p468", frequency_grid(center, 0.4), (4, 6, 8)),
    ]
    rows = []
    for lift_id, frequencies, powers in families:
        context = FrontierContext(
            radius=16.0,
            density=10.0,
            width_factor=1.5,
            spectral_lift_frequencies=frequencies,
            spectral_lift_powers=powers,
        )
        base, _ = context.base_matrix(
            (0, 1, 2, 3, 4),
            axis_step=0.05,
        )
        points = patch.points(3, 3)
        optimized = optimize_core_measure(
            context.core_matrices(points),
            base,
            maxiter=120,
        )
        rows.append(
            {
                "lift_id": lift_id,
                "frequency_count": len(frequencies),
                "powers": list(powers),
                "requested_atom_count": (
                    len(frequencies) * len(powers)
                ),
                "total_basis_count": context.count,
                "dimension": context.dimension,
                "effective_added_dimension": context.lift_metadata[
                    "effective_added_dimension"
                ],
                "uniform_axis_uniform_core_threshold": float(
                    uniform_core_threshold(
                        context,
                        patch,
                        base,
                        nx=3,
                        ny=3,
                    )
                ),
                "optimized_core_uniform_axis_threshold": float(
                    optimized["threshold"]
                ),
                "tail_minimum_eigenvalue": float(
                    np.linalg.eigvalsh(context.tail_matrix)[0]
                ),
            }
        )
    baseline = rows[0][
        "optimized_core_uniform_axis_threshold"
    ]
    for row in rows:
        row["relative_improvement_vs_baseline"] = float(
            1.0
            - row["optimized_core_uniform_axis_threshold"]
            / baseline
        )
    output = {
        "schema": "RH.AxisNotch.LiftScaling.v0.5",
        "configuration": {
            "radius": 16.0,
            "patch": patch.to_dict(),
            "frequency_step": 0.1,
        },
        "rows": rows,
        "interpretation": (
            "This is a uniform-axis/core screen, not the joint dual "
            "gate. It tests whether added external directions show a "
            "meaningful scaling trend before expensive optimization."
        ),
        "global_rh_certificate": False,
    }
    (ROOT / "outputs" / "lift_scaling.json").write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
