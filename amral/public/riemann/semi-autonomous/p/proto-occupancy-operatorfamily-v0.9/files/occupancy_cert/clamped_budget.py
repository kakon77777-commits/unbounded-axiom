from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from typing import Any

from .cover import canonical_json_hash
from .rational_interval import as_fraction, fraction_text


def file_sha256(path: Any) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _effective_axis_atoms(
    witness: dict[str, Any],
) -> list[dict[str, Any]]:
    coefficients = [
        as_fraction(value)
        for value in witness["model"]["count_coefficients"]
    ]
    atoms: list[dict[str, Any]] = []
    for band_index, (coefficient, support) in enumerate(
        zip(coefficients, witness["axis_supports"])
    ):
        for atom_index, atom in enumerate(support):
            probability = as_fraction(atom["weight"])
            atoms.append(
                {
                    "atom_id": f"b{band_index}_a{atom_index}",
                    "band_index": band_index,
                    "center": as_fraction(atom["x"]),
                    "probability_weight": probability,
                    "operator_weight": coefficient * probability,
                }
            )
    return atoms


def build_clamped_radius_certificate(
    witness: dict[str, Any],
    parent_certificate: dict[str, Any],
    witness_file_hash: str,
    certificate_file_hash: str,
    uniform_radius: Fraction = Fraction(
        1, 500_000_000_000_000
    ),
    failed_budget_probe: Fraction = Fraction(
        1, 400_000_000_000_000
    ),
) -> dict[str, Any]:
    witness_hash = canonical_json_hash(witness)
    parent_checks = {
        "witness_canonical_hash_matches_parent": (
            parent_certificate["input"]["canonical_witness_sha256"]
            == witness_hash
        ),
        "parent_abstract_interval_certificate": (
            parent_certificate["classification"][
                "abstract_continuous_interval_certificate"
            ]
            is True
        ),
        "parent_operator_strictly_positive": (
            parent_certificate["classification"][
                "abstract_operator_strictly_positive"
            ]
            is True
        ),
        "parent_global_flag_false": (
            parent_certificate["classification"][
                "global_rh_certificate"
            ]
            is False
        ),
    }
    if not all(parent_checks.values()):
        raise ArithmeticError(f"parent dependency failed: {parent_checks}")

    model = witness["model"]
    radius = as_fraction(model["radius"])
    tail_scale = as_fraction(
        model["tail_scale_lower_decimal_rational"]
    )
    parent_alpha = as_fraction(model["target_alpha"])
    child_alpha = Fraction(1)
    if not 0 < child_alpha < parent_alpha:
        raise ArithmeticError("child alpha must be inside parent margin")
    ratio = child_alpha / parent_alpha
    convex_margin = 1 - ratio

    atoms = _effective_axis_atoms(witness)
    band_sums = []
    for support in witness["axis_supports"]:
        band_sums.append(
            sum(
                (as_fraction(atom["weight"]) for atom in support),
                Fraction(0),
            )
        )
    if any(value != 1 for value in band_sums):
        raise ArithmeticError("axis probabilities do not sum to one")

    total_operator_weight = sum(
        (atom["operator_weight"] for atom in atoms),
        Fraction(0),
    )
    interval_length = 2 * radius
    pi_lower = Fraction(3)
    sqrt_three_lower = Fraction(5, 3)
    green_l2_norm_upper = (
        interval_length**4
        / (pi_lower**4 * tail_scale)
    )
    # sqrt((2R)(2R^3/3)) = 2R^2/sqrt(3) < 6R^2/5.
    representer_product_upper = (
        Fraction(6, 5)
        * radius**2
        * green_l2_norm_upper
    )
    rank_one_location_coefficient = (
        2 * representer_product_upper
    )
    weighted_radius_sum = total_operator_weight * uniform_radius
    perturbation_upper = (
        rank_one_location_coefficient * weighted_radius_sum
    )
    coercivity_lower = convex_margin - perturbation_upper
    critical_uniform_radius = (
        convex_margin
        / (
            rank_one_location_coefficient
            * total_operator_weight
        )
    )
    failed_probe_upper = (
        rank_one_location_coefficient
        * total_operator_weight
        * failed_budget_probe
    )
    if coercivity_lower <= 0:
        raise ArithmeticError("uniform radius did not fit convex margin")
    if failed_probe_upper < convex_margin:
        raise ArithmeticError("failed-budget probe unexpectedly passes")

    cell_rows = []
    for atom in atoms:
        center = atom["center"]
        cell_rows.append(
            {
                "atom_id": atom["atom_id"],
                "band_index": atom["band_index"],
                "center": fraction_text(center),
                "operator_weight": fraction_text(
                    atom["operator_weight"]
                ),
                "closed_location_cell": {
                    "lo": fraction_text(center - uniform_radius),
                    "hi": fraction_text(center + uniform_radius),
                },
            }
        )

    return {
        "schema": "RH.Occupancy.ClampedGreenRadiusCertificate.v0.9",
        "node": "RH-Occupancy-OperatorFamily-20260725-v0.9",
        "parent_dependency": {
            "package": "RH_IntervalGreenKernel_AtomicCertificate_v0.7",
            "witness_file_sha256": witness_file_hash,
            "certificate_file_sha256": certificate_file_hash,
            "witness_canonical_sha256": witness_hash,
            "checks": parent_checks,
            "dependency_mode": (
                "conditional theorem reuse; parent v0.7 owns the full "
                "directed-decimal replay"
            ),
        },
        "parameters": {
            "clamped_radius": fraction_text(radius),
            "tail_scale": fraction_text(tail_scale),
            "parent_alpha": fraction_text(parent_alpha),
            "child_alpha": fraction_text(child_alpha),
            "convex_ratio": fraction_text(ratio),
            "convex_coercivity_margin": fraction_text(convex_margin),
            "axis_atom_count": len(atoms),
            "total_axis_operator_weight": fraction_text(
                total_operator_weight
            ),
            "uniform_location_radius": fraction_text(uniform_radius),
        },
        "proof_budget": {
            "pi_lower": fraction_text(pi_lower),
            "sqrt_three_lower": fraction_text(sqrt_three_lower),
            "green_l2_operator_norm_upper": fraction_text(
                green_l2_norm_upper
            ),
            "representer_norm_product_upper": fraction_text(
                representer_product_upper
            ),
            "rank_one_location_coefficient": fraction_text(
                rank_one_location_coefficient
            ),
            "weighted_radius_sum": fraction_text(weighted_radius_sum),
            "perturbation_operator_norm_upper": fraction_text(
                perturbation_upper
            ),
            "coercivity_lower_bound": fraction_text(coercivity_lower),
            "critical_uniform_radius_for_this_budget": fraction_text(
                critical_uniform_radius
            ),
            "failed_budget_probe_radius": fraction_text(
                failed_budget_probe
            ),
            "failed_budget_probe_perturbation_upper": fraction_text(
                failed_probe_upper
            ),
            "failed_probe_is_operator_counterexample": False,
        },
        "location_cells": cell_rows,
        "statement": {
            "quantifier": (
                "for all 58 independent locations in the listed cells"
            ),
            "operator_claim": (
                "the inherited abstract clamped Green operator at "
                "alpha=1 is bounded below by the listed positive "
                "coercivity rational"
            ),
            "argument": (
                "convex margin from alpha 21/20 to 1, followed by a "
                "rank-one perturbation bound and two Poincare bounds"
            ),
        },
        "classification": {
            "exact_rational_perturbation_budget": True,
            "conditional_abstract_operator_family_certificate": True,
            "coordinate_dependent_parent_atom_calibration": True,
            "actual_zero_occupancy_certificate": False,
            "zeta_facing_count_or_presence_theorem": False,
            "global_rh_certificate": False,
        },
    }


def verify_clamped_radius_certificate(
    witness: dict[str, Any],
    parent_certificate: dict[str, Any],
    certificate: dict[str, Any],
    witness_file_hash: str,
    certificate_file_hash: str,
) -> dict[str, Any]:
    regenerated = build_clamped_radius_certificate(
        witness,
        parent_certificate,
        witness_file_hash,
        certificate_file_hash,
        uniform_radius=as_fraction(
            certificate["parameters"]["uniform_location_radius"]
        ),
        failed_budget_probe=as_fraction(
            certificate["proof_budget"]["failed_budget_probe_radius"]
        ),
    )
    checks = {
        "exact_regeneration": regenerated == certificate,
        "parent_hash_lock": (
            certificate["parent_dependency"]["witness_file_sha256"]
            == witness_file_hash
            and certificate["parent_dependency"][
                "certificate_file_sha256"
            ]
            == certificate_file_hash
        ),
        "positive_coercivity": (
            as_fraction(
                certificate["proof_budget"]["coercivity_lower_bound"]
            )
            > 0
        ),
        "all_58_cells_present": (
            len(certificate["location_cells"]) == 58
        ),
        "failed_probe_only_budget_failure": (
            certificate["proof_budget"][
                "failed_probe_is_operator_counterexample"
            ]
            is False
        ),
        "actual_zero_flag_false": (
            certificate["classification"][
                "actual_zero_occupancy_certificate"
            ]
            is False
        ),
        "global_flag_false": (
            certificate["classification"]["global_rh_certificate"]
            is False
        ),
    }
    return {
        "schema": "RH.Occupancy.ClampedGreenRadiusVerification.v0.9",
        "checks": checks,
        "verification_pass": all(checks.values()),
        "recomputed_coercivity_lower_bound": regenerated[
            "proof_budget"
        ]["coercivity_lower_bound"],
        "recomputed_critical_uniform_radius": regenerated[
            "proof_budget"
        ]["critical_uniform_radius_for_this_budget"],
        "global_rh_certificate": False,
    }

