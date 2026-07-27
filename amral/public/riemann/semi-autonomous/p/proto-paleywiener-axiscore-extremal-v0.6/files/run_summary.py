from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent


def read_output(name: str) -> Any:
    return json.loads(
        (ROOT / "outputs" / name).read_text(encoding="utf-8")
    )


def main() -> None:
    rank_two = read_output("green_rank_two_scan.json")
    quadrature = read_output("quadrature_audit.json")
    convergence = read_output(
        "galerkin_joint_convergence.json"
    )
    transfer = read_output("atomic_transfer.json")
    budget = read_output("certificate_budget.json")
    rational = read_output("rational_atomic_witness.json")
    final_galerkin = convergence["rows"][-1]
    finest_green = transfer["direct_green_transfer_rows"][-1]
    output = {
        "schema": "RH.PaleyWiener.ExperimentSummary.v0.6",
        "date": "2026-07-25",
        "research_mode": (
            "semi-autonomous AI mathematical research"
        ),
        "parent_node": (
            "RH-AxisNotch-CoverCodesign-20260724-v0.5"
        ),
        "continuous_domain": (
            "real-even clamped H_0^2(-R,R), structural zeros "
            "G(0)=G(i/2)=0, tail inner product"
        ),
        "exact_results": {
            "trace_class_primal_measure_dual_weak_duality": True,
            "one_axis_one_core_rank_two_closed_form": True,
            "explicit_clamped_green_kernel": True,
            "finite_atomic_psd_reduces_to_core_negative_rank": True,
            "final_negative_schur_rank": 2
        },
        "single_band_result": {
            "all_best_single_point_lower_bounds_below_one": (
                rank_two[
                    "finest_step_all_single_band_lower_bounds_below_one"
                ]
            ),
            "A1_best_single_point_lower_bound": (
                rank_two["rows"][-1]["band_rows"][1][
                    "maximum_point_lower_bound"
                ]
            ),
            "A1_best_x": (
                rank_two["rows"][-1]["band_rows"][1][
                    "maximum_point_x"
                ]
            )
        },
        "galerkin_result": {
            "raw_dimension": final_galerkin["raw_dimension"],
            "effective_dimension": final_galerkin[
                "effective_dimension"
            ],
            "joint_alpha": final_galerkin["joint_dual"]["alpha"],
            "safe_alpha": final_galerkin["joint_dual"][
                "safe_alpha"
            ],
            "safe_minimum_eigenvalue": final_galerkin[
                "joint_dual"
            ]["safe_min_eigenvalue"],
            "monotone_raw_alpha_nonincreasing": convergence[
                "monotone_raw_alpha_nonincreasing"
            ]
        },
        "independent_kernel_agreement": {
            "galerkin_point_extremal_raw_dimension_192": (
                quadrature["galerkin_dimension_rows"][-1][
                    "point_extremal"
                ]
            ),
            "direct_green_point_extremal_finest": (
                quadrature["direct_green_rows"][-1][
                    "point_extremal"
                ]
            ),
            "absolute_difference": abs(
                quadrature["galerkin_dimension_rows"][-1][
                    "point_extremal"
                ]
                - quadrature["direct_green_rows"][-1][
                    "point_extremal"
                ]
            )
        },
        "continuous_kernel_atomic_result": {
            "axis_atom_count": budget[
                "atomic_axis_support_count"
            ],
            "core_atom_count": budget[
                "atomic_core_support_count"
            ],
            "raw_threshold_for_fixed_measures": finest_green[
                "raw_threshold_for_fixed_measures"
            ],
            "safe_alpha": finest_green["tested_safe_alpha"],
            "safe_full_minimum_eigenvalue": finest_green[
                "tested_safe_minimum_eigenvalue"
            ],
            "safe_schur_minimum_eigenvalue": finest_green[
                "schur_certificate_minimum_eigenvalue"
            ],
            "floating_obstruction_pass": transfer[
                "continuous_kernel_floating_obstruction"
            ]
        },
        "rational_certificate_candidate": {
            "target_alpha": 1.05,
            "weight_denominator": rational[
                "weight_denominator"
            ],
            "full_minimum_eigenvalue": rational[
                "finest_full_witness_minimum_eigenvalue"
            ],
            "schur_minimum_eigenvalue": rational[
                "finest_schur_minimum_eigenvalue"
            ],
            "floating_pass": rational[
                "rationalized_floating_pass"
            ],
            "interval_certified": rational[
                "interval_certified"
            ]
        },
        "research_decision": (
            "Stop dictionary and Galerkin expansion. Preserve the "
            "rational 58-axis-plus-2-core atomic witness and next "
            "interval-certify the explicit Green-kernel 2-by-2 "
            "Schur certificate at alpha=21/20."
        ),
        "next_node": (
            "RH-IntervalGreenKernel-AtomicCertificate-"
            "20260725-v0.7"
        ),
        "known_zero_ordinates_used": False,
        "interval_certified": False,
        "global_rh_certificate": False
    }
    (
        ROOT / "outputs" / "experiment_summary.json"
    ).write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
