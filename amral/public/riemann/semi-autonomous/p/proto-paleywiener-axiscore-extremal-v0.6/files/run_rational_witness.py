from __future__ import annotations

import json
import math
from decimal import Decimal
from pathlib import Path
from typing import Any

import numpy as np

from pwext.green import continuous_atomic_threshold
from pwext.model import PWGalerkinContext


ROOT = Path(__file__).resolve().parent
WEIGHT_DENOMINATOR = 10**12
TAIL_DENOMINATOR = 10**18


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def decimal_fraction(value: float) -> dict[str, int]:
    decimal = Decimal(str(round(float(value), 12)))
    numerator, denominator = decimal.as_integer_ratio()
    return {
        "numerator": int(numerator),
        "denominator": int(denominator),
    }


def rationalize_probability(
    values: list[float],
) -> list[int]:
    weights = np.asarray(values, dtype=float)
    weights = weights / np.sum(weights)
    scaled = weights * WEIGHT_DENOMINATOR
    numerators = np.floor(scaled).astype(np.int64)
    remainder = int(
        WEIGHT_DENOMINATOR - np.sum(numerators)
    )
    order = np.argsort(-(scaled - numerators))
    numerators[order[:remainder]] += 1
    if int(np.sum(numerators)) != WEIGHT_DENOMINATOR:
        raise RuntimeError("probability rationalization failed")
    return numerators.astype(int).tolist()


def main() -> None:
    convergence = read_json(
        ROOT / "outputs" / "galerkin_joint_convergence.json"
    )
    source = convergence["rows"][-1]
    joint = source["joint_dual"]
    rational_axis_supports = []
    floating_axis_supports = []
    for support in joint["axis_supports"]:
        numerators = rationalize_probability(
            [float(row["weight"]) for row in support]
        )
        rational_group = []
        floating_group = []
        for row, numerator in zip(support, numerators):
            x_fraction = decimal_fraction(float(row["x"]))
            rational_group.append(
                {
                    "x": x_fraction,
                    "weight": {
                        "numerator": numerator,
                        "denominator": WEIGHT_DENOMINATOR,
                    },
                }
            )
            floating_group.append(
                {
                    "x": (
                        x_fraction["numerator"]
                        / x_fraction["denominator"]
                    ),
                    "weight": (
                        numerator / WEIGHT_DENOMINATOR
                    ),
                }
            )
        rational_axis_supports.append(rational_group)
        floating_axis_supports.append(floating_group)
    core_numerators = rationalize_probability(
        [float(row["weight"]) for row in joint["core_support"]]
    )
    rational_core_support = []
    floating_core_support = []
    for row, numerator in zip(
        joint["core_support"],
        core_numerators,
    ):
        x_fraction = decimal_fraction(float(row["x"]))
        y_fraction = decimal_fraction(float(row["y"]))
        rational_core_support.append(
            {
                "x": x_fraction,
                "y": y_fraction,
                "weight": {
                    "numerator": numerator,
                    "denominator": WEIGHT_DENOMINATOR,
                },
            }
        )
        floating_core_support.append(
            {
                "x": (
                    x_fraction["numerator"]
                    / x_fraction["denominator"]
                ),
                "y": (
                    y_fraction["numerator"]
                    / y_fraction["denominator"]
                ),
                "weight": numerator / WEIGHT_DENOMINATOR,
            }
        )
    context = PWGalerkinContext(
        16.0,
        8,
        quadrature_order=512,
    )
    coefficient_fractions = [
        decimal_fraction(float(value))
        for value in context.count_coefficients
    ]
    rational_coefficients = np.asarray(
        [
            row["numerator"] / row["denominator"]
            for row in coefficient_fractions
        ]
    )
    tail_value = context.tail_scale
    tail_numerator = math.floor(
        tail_value * TAIL_DENOMINATOR
    )
    rational_tail_scale = (
        tail_numerator / TAIL_DENOMINATOR
    )
    audit_rows = []
    for step in (0.01, 0.005, 0.0025):
        audit_rows.append(
            continuous_atomic_threshold(
                radius=16.0,
                time_step=step,
                count_coefficients=rational_coefficients,
                axis_supports=floating_axis_supports,
                core_support=floating_core_support,
                safe_alpha=1.05,
                tail_scale_override=rational_tail_scale,
            )
        )
    output = {
        "schema": "RH.PaleyWiener.RationalAtomicWitness.v0.6",
        "model": {
            "radius": {"numerator": 16, "denominator": 1},
            "target_alpha": {
                "numerator": 21,
                "denominator": 20
            },
            "tail_scale_lower_decimal_rational": {
                "numerator": tail_numerator,
                "denominator": TAIL_DENOMINATOR
            },
            "count_coefficients": coefficient_fractions,
            "structural_constraints": [
                "integral psi(t) dt = 0",
                "integral psi(t) cosh(t/2) dt = 0"
            ]
        },
        "axis_supports": rational_axis_supports,
        "core_support": rational_core_support,
        "weight_denominator": WEIGHT_DENOMINATOR,
        "source": {
            "raw_dimension": source["raw_dimension"],
            "source_alpha": joint["alpha"],
            "source_safe_alpha": joint["safe_alpha"]
        },
        "floating_green_audit_rows": audit_rows,
        "finest_schur_minimum_eigenvalue": audit_rows[-1][
            "schur_certificate_minimum_eigenvalue"
        ],
        "finest_full_witness_minimum_eigenvalue": audit_rows[-1][
            "tested_safe_minimum_eigenvalue"
        ],
        "rationalized_floating_pass": bool(
            audit_rows[-1]["tested_safe_psd"]
            and audit_rows[-1][
                "schur_certificate_minimum_eigenvalue"
            ]
            > 0.0
        ),
        "interval_certified": False,
        "required_next_step": (
            "Interval-enclose the tail coefficient theorem, every "
            "projected Green-kernel inner product, the positive "
            "60-by-60 solve, and the final 2-by-2 Schur matrix."
        ),
        "global_rh_certificate": False,
    }
    (
        ROOT / "outputs" / "rational_atomic_witness.json"
    ).write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "axis_atom_count": sum(
                    len(group)
                    for group in rational_axis_supports
                ),
                "core_atom_count": len(rational_core_support),
                "target_alpha": 1.05,
                "finest_schur_minimum_eigenvalue": output[
                    "finest_schur_minimum_eigenvalue"
                ],
                "rationalized_floating_pass": output[
                    "rationalized_floating_pass"
                ],
            },
            indent=2,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
