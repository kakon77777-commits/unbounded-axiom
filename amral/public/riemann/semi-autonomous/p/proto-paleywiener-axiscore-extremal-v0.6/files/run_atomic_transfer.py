from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from pwext.dual import reconstruct_atomic_witness
from pwext.green import continuous_atomic_threshold
from pwext.model import PWGalerkinContext


ROOT = Path(__file__).resolve().parent


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    convergence = read_json(
        ROOT / "outputs" / "galerkin_joint_convergence.json"
    )
    source = convergence["rows"][-1]
    joint = source["joint_dual"]
    galerkin_rows = []
    for raw_dimension in (192, 208, 224, 256, 288):
        context = PWGalerkinContext(
            16.0,
            raw_dimension,
            quadrature_order=2560,
        )
        reconstruction = reconstruct_atomic_witness(
            context,
            joint,
        )
        reconstruction["raw_dimension"] = raw_dimension
        reconstruction[
            "maximum_structural_residual"
        ] = max(context.structural_residuals.values())
        galerkin_rows.append(reconstruction)
        print(
            json.dumps(reconstruction, ensure_ascii=False),
            flush=True,
        )
    direct_green_rows = []
    for step in (0.02, 0.01, 0.005, 0.0025):
        row = continuous_atomic_threshold(
            radius=16.0,
            time_step=step,
            count_coefficients=PWGalerkinContext(
                16.0,
                8,
                quadrature_order=512,
            ).count_coefficients,
            axis_supports=joint["axis_supports"],
            core_support=joint["core_support"],
            safe_alpha=joint["safe_alpha"],
        )
        direct_green_rows.append(row)
        print(json.dumps(row, ensure_ascii=False), flush=True)
    finest = direct_green_rows[-1]
    output = {
        "schema": "RH.PaleyWiener.AtomicTransfer.v0.6",
        "source_raw_dimension": source["raw_dimension"],
        "source_effective_dimension": source[
            "effective_dimension"
        ],
        "source_joint_alpha": joint["alpha"],
        "source_safe_alpha": joint["safe_alpha"],
        "galerkin_transfer_rows": galerkin_rows,
        "direct_green_transfer_rows": direct_green_rows,
        "direct_green_finest_raw_threshold_above_one": bool(
            finest["raw_threshold_for_fixed_measures"] > 1.0
        ),
        "direct_green_finest_safe_psd": bool(
            finest["tested_safe_psd"]
        ),
        "continuous_kernel_floating_obstruction": bool(
            finest["raw_threshold_for_fixed_measures"] > 1.0
            and finest["tested_safe_psd"]
        ),
        "interval_certified": False,
        "interpretation": (
            "The final Galerkin atomic measures are evaluated in "
            "an independent direct Green-kernel solver. Passing "
            "supports a continuous-kernel floating obstruction but "
            "does not replace interval enclosure of elementary "
            "kernel integrals."
        ),
        "global_rh_certificate": False,
    }
    (
        ROOT / "outputs" / "atomic_transfer.json"
    ).write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
