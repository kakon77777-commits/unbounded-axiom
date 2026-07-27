from __future__ import annotations

from fractions import Fraction
from typing import Any

from .dirichlet_green import point_proof_json, schur_point
from .rational_interval import as_fraction, fraction_text


def occupancy_semantic_audit(model: dict[str, Any]) -> dict[str, Any]:
    cells = model["occupancy_cells"]
    left_endpoint = as_fraction(cells[0]["interval"]["lo"])
    count_only_points = [left_endpoint, left_endpoint]
    counterexample = schur_point(count_only_points, model)
    schur = counterexample["schur_matrix"]
    witness = [schur[0][1], -schur[0][0]]
    quadratic = sum(
        witness[row]
        * schur[row][column]
        * witness[column]
        for row in range(2)
        for column in range(2)
    )
    if counterexample["schur_determinant"] >= 0 or quadratic >= 0:
        raise ArithmeticError("count-only counterexample did not fail")

    return {
        "schema": "RH.Occupancy.SemanticBridge.v0.9",
        "exact_transfer_theorem": {
            "name": "OccupancySelectionOperatorTransfer",
            "premises": [
                (
                    "Each certified cell I_r contains at least ell_r "
                    "actual points, with endpoint and multiplicity "
                    "conventions fixed."
                ),
                (
                    "For every selection x_rk in I_r of ell_r points, "
                    "the selected finite-rank operator W(x) is PSD."
                ),
                (
                    "Every unselected actual point contributes a PSD "
                    "rank-one operator with the same nonnegative sign."
                ),
            ],
            "conclusion": (
                "The operator containing all actual points is PSD; "
                "the surplus over a selected configuration is PSD."
            ),
            "quantifier_preserved": True,
            "definition_substitution_forbidden": (
                "A scalar count lower bound may not be replaced by an "
                "arbitrary probability measure or fixed operator floor."
            ),
        },
        "count_only_counterexample": {
            "description": (
                "The same total count two in the broad union permits "
                "both points at 1/5; the Schur determinant is negative."
            ),
            "configuration": [
                fraction_text(value) for value in count_only_points
            ],
            "exact_point_proof": point_proof_json(counterexample),
            "negative_direction": [
                fraction_text(value) for value in witness
            ],
            "negative_quadratic_value": fraction_text(quadratic),
            "count_two_suffices_for_operator_positivity": False,
        },
        "type_rules": {
            "cell_occupancy_plus_universal_family": (
                "valid actual-configuration transfer"
            ),
            "scalar_count_lower_plus_arbitrary_measure": "invalid",
            "scalar_count_lower_plus_fixed_nonzero_psd_floor": (
                "generally invalid"
            ),
        },
        "classification": {
            "exact_semantic_theorem": True,
            "exact_count_only_counterexample": True,
            "synthetic_operator_model": True,
            "zeta_facing_presence_theorem": False,
            "global_rh_certificate": False,
        },
    }

