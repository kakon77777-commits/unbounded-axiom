from __future__ import annotations

import hashlib
import json
from decimal import Decimal
from fractions import Fraction
from typing import Any

from .box_green import (
    BoxProjectedGramResult,
    build_box_projected_gram,
)
from .decimal_interval import (
    DInterval,
    decimal_add_upper,
    decimal_div_upper,
    decimal_sub_lower,
    interval_sum,
)
from .transcendental import transcendental_audit


def canonical_json_hash(value: Any) -> str:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _point(value: Fraction) -> DInterval:
    return DInterval.from_fraction(value)


def _identity(size: int) -> list[list[DInterval]]:
    return [
        [
            DInterval.from_int(int(row == column))
            for column in range(size)
        ]
        for row in range(size)
    ]


def _matmul(
    left: list[list[DInterval]],
    right: list[list[DInterval]],
) -> list[list[DInterval]]:
    rows = len(left)
    shared = len(right)
    columns = len(right[0])
    if len(left[0]) != shared:
        raise ValueError("matrix dimension mismatch")
    return [
        [
            interval_sum(
                left[row][index] * right[index][column]
                for index in range(shared)
            )
            for column in range(columns)
        ]
        for row in range(rows)
    ]


def _subtract(
    left: list[list[DInterval]],
    right: list[list[DInterval]],
) -> list[list[DInterval]]:
    return [
        [
            left[row][column] - right[row][column]
            for column in range(len(left[0]))
        ]
        for row in range(len(left))
    ]


def _infinity_norm_upper(
    matrix: list[list[DInterval]],
) -> Decimal:
    maximum = Decimal(0)
    for row in matrix:
        total = Decimal(0)
        for value in row:
            total = decimal_add_upper(total, value.abs_upper())
        maximum = max(maximum, total)
    return maximum


def _matrix_to_json(
    matrix: list[list[DInterval]],
) -> list[list[dict[str, str]]]:
    return [
        [value.to_json() for value in row]
        for row in matrix
    ]


def _matrix_from_decimal_strings(
    matrix: list[list[str]],
) -> list[list[DInterval]]:
    return [
        [DInterval.from_decimal(value) for value in row]
        for row in matrix
    ]


def _decimal_candidate(value: float) -> str:
    return format(float(value), ".17e")


def _candidate_matrices(
    system: list[list[DInterval]],
    cross: list[list[DInterval]],
) -> tuple[list[list[str]], list[list[str]]]:
    import numpy as np

    system_midpoint = np.asarray(
        [
            [float(value.midpoint()) for value in row]
            for row in system
        ],
        dtype=float,
    )
    cross_midpoint = np.asarray(
        [
            [float(value.midpoint()) for value in row]
            for row in cross
        ],
        dtype=float,
    )
    inverse = np.linalg.inv(system_midpoint)
    solution = np.linalg.solve(system_midpoint, cross_midpoint)
    return (
        [
            [_decimal_candidate(value) for value in row]
            for row in inverse
        ],
        [
            [_decimal_candidate(value) for value in row]
            for row in solution
        ],
    )


def _projected_hash(gram: list[list[DInterval]]) -> str:
    serialized = [
        [
            [str(value.lo), str(value.hi)]
            for value in row
        ]
        for row in gram
    ]
    return canonical_json_hash(serialized)


def _system_from_gram(
    gram_result: BoxProjectedGramResult,
) -> tuple[
    list[list[DInterval]],
    list[list[DInterval]],
    list[list[DInterval]],
]:
    positive_count = len(gram_result.positive_functions)
    negative_count = len(gram_result.negative_functions)
    gram = gram_result.projected_gram
    weights = [_point(value) for value in gram_result.positive_weights]
    system = [
        [
            DInterval.from_int(int(row == column))
            + gram[row][column] * weights[column]
            for column in range(positive_count)
        ]
        for row in range(positive_count)
    ]
    cross = [
        [
            gram[row][positive_count + column]
            for column in range(negative_count)
        ]
        for row in range(positive_count)
    ]
    negative = [
        [
            gram[
                positive_count + row
            ][
                positive_count + column
            ]
            for column in range(negative_count)
        ]
        for row in range(negative_count)
    ]
    return system, cross, negative


def prove_with_candidates(
    gram_result: BoxProjectedGramResult,
    inverse_strings: list[list[str]],
    solution_strings: list[list[str]],
) -> dict[str, Any]:
    system, cross, negative = _system_from_gram(gram_result)
    positive_count = len(gram_result.positive_functions)
    inverse = _matrix_from_decimal_strings(inverse_strings)
    solution_point = _matrix_from_decimal_strings(solution_strings)
    identity = _identity(positive_count)

    defect = _subtract(identity, _matmul(inverse, system))
    defect_norm = _infinity_norm_upper(defect)
    proof: dict[str, Any] = {
        "neumann_defect_infinity_norm_upper": str(defect_norm),
        "neumann_regular": bool(defect_norm < 1),
    }
    if defect_norm >= 1:
        proof.update(
            {
                "certificate_pass": False,
                "failure_class": "neumann_inverse_failure",
            }
        )
        return proof

    raw_residual = _subtract(
        cross,
        _matmul(system, solution_point),
    )
    transformed_residual = _matmul(inverse, raw_residual)
    denominator_lower = decimal_sub_lower(
        Decimal(1),
        defect_norm,
    )
    radii: list[Decimal] = []
    for column in range(len(cross[0])):
        residual_norm = max(
            transformed_residual[row][column].abs_upper()
            for row in range(positive_count)
        )
        radii.append(
            decimal_div_upper(
                residual_norm,
                denominator_lower,
            )
        )
    solution = [
        [
            solution_point[row][column].widen(radii[column])
            for column in range(len(cross[0]))
        ]
        for row in range(positive_count)
    ]

    correction = [
        [
            interval_sum(
                cross[index][row]
                * _point(gram_result.positive_weights[index])
                * solution[index][column]
                for index in range(positive_count)
            )
            for column in range(len(cross[0]))
        ]
        for row in range(len(cross[0]))
    ]
    effective_negative = _subtract(negative, correction)
    negative_inverse_diagonal = [
        _point(Fraction(1, 1) / weight)
        for weight in gram_result.negative_weights
    ]
    raw_test = [
        [
            (
                negative_inverse_diagonal[row]
                if row == column
                else DInterval.zero()
            )
            - effective_negative[row][column]
            for column in range(len(negative))
        ]
        for row in range(len(negative))
    ]
    off_diagonal = raw_test[0][1].intersect(raw_test[1][0])
    test_matrix = [
        [raw_test[0][0], off_diagonal],
        [off_diagonal, raw_test[1][1]],
    ]
    determinant = (
        test_matrix[0][0] * test_matrix[1][1]
        - off_diagonal.square()
    )
    sylvester_pass = (
        test_matrix[0][0].lo > 0
        and determinant.lo > 0
    )
    proof.update(
        {
            "transformed_residual_infinity_norm_upper": [
                str(
                    max(
                        transformed_residual[row][column].abs_upper()
                        for row in range(positive_count)
                    )
                )
                for column in range(len(cross[0]))
            ],
            "solution_component_radius_upper": [
                str(value)
                for value in radii
            ],
            "verified_solution_enclosure": True,
            "final_two_by_two_matrix": _matrix_to_json(test_matrix),
            "first_leading_minor_lower": str(test_matrix[0][0].lo),
            "determinant_interval": determinant.to_json(),
            "determinant_lower": str(determinant.lo),
            "sylvester_positive_definite": bool(sylvester_pass),
            "certificate_pass": bool(sylvester_pass),
            "failure_class": (
                None
                if sylvester_pass
                else "sylvester_lower_bound_failure"
            ),
        }
    )
    return proof


def build_box_certificate(
    witness: dict[str, Any],
    axis_half_width: Fraction,
    child_alpha: Fraction = Fraction(1),
) -> dict[str, Any]:
    gram_result = build_box_projected_gram(
        witness,
        axis_half_width,
        child_alpha,
    )
    system, cross, _ = _system_from_gram(gram_result)
    inverse_strings, solution_strings = _candidate_matrices(
        system,
        cross,
    )
    proof = prove_with_candidates(
        gram_result,
        inverse_strings,
        solution_strings,
    )
    width_string = (
        f"{axis_half_width.numerator}/"
        f"{axis_half_width.denominator}"
    )
    alpha_string = (
        f"{child_alpha.numerator}/{child_alpha.denominator}"
    )
    return {
        "schema": "RH.LocalIntervalGreen.CellCertificate.v1.0",
        "node": "RH-LocalIntervalGreen-CellCover-20260725-v1.0",
        "statement": {
            "domain": (
                "even clamped H_0^2(-16,16) with G(0)=G(i/2)=0"
            ),
            "axis_cell_half_width": width_string,
            "child_alpha": alpha_string,
            "quantifier": (
                "for every independent choice of the 58 axis "
                "locations in their closed centered cells"
            ),
            "claim": (
                "The resulting abstract continuous Green-kernel "
                "operator is strictly positive."
            ),
        },
        "input": {
            "canonical_witness_sha256": canonical_json_hash(witness),
            "axis_location_dimension": 58,
            "positive_rank": len(gram_result.positive_functions),
            "negative_rank": len(gram_result.negative_functions),
        },
        "arithmetic": {
            **transcendental_audit(),
            "zero_crossing_moment_method": (
                "complex power series with explicit exponential tail"
            ),
            "moment_series_terms": gram_result.moment_series_terms,
            "shared_variable_cancellation": True,
        },
        "green_kernel": {
            "method": (
                "cell-valued clamped D^4 inverse; affine-tagged "
                "exponents; two-sided orientation intersection"
            ),
            "structural_gram": _matrix_to_json(
                gram_result.structural_gram
            ),
            "structural_determinant": (
                gram_result.structural_determinant.to_json()
            ),
            "structural_projection_invertible": True,
            "projected_gram_sha256": _projected_hash(
                gram_result.projected_gram
            ),
            "maximum_unprojected_imaginary_width": str(
                gram_result.maximum_unprojected_imaginary_width
            ),
            "maximum_projected_interval_width": str(
                gram_result.maximum_projected_width
            ),
        },
        "neumann_candidate": {
            "inverse_decimal_rational": inverse_strings,
            "solution_decimal_rational": solution_strings,
        },
        "proof": proof,
        "classification": {
            "local_58cell_interval_certificate": bool(
                proof["certificate_pass"]
            ),
            "abstract_operator_strictly_positive": bool(
                proof["certificate_pass"]
            ),
            "actual_zeta_occupancy_family": False,
            "zeta_facing_tail_theorem_certified": False,
            "explicit_formula_transfer_certified": False,
            "global_rh_certificate": False,
        },
        "trust_boundary": (
            "This is a universal local-location certificate only in "
            "the inherited abstract Green model. It does not identify "
            "the 58 locations with actual zeta ordinates and does not "
            "complete the explicit-formula transfer."
        ),
    }


def verify_box_certificate(
    witness: dict[str, Any],
    certificate: dict[str, Any],
) -> dict[str, Any]:
    numerator, denominator = certificate["statement"][
        "axis_cell_half_width"
    ].split("/")
    axis_half_width = Fraction(int(numerator), int(denominator))
    alpha_numerator, alpha_denominator = certificate["statement"][
        "child_alpha"
    ].split("/")
    child_alpha = Fraction(
        int(alpha_numerator),
        int(alpha_denominator),
    )
    gram_result = build_box_projected_gram(
        witness,
        axis_half_width,
        child_alpha,
    )
    candidates = certificate["neumann_candidate"]
    proof = prove_with_candidates(
        gram_result,
        candidates["inverse_decimal_rational"],
        candidates["solution_decimal_rational"],
    )
    checks = {
        "schema": (
            certificate.get("schema")
            == "RH.LocalIntervalGreen.CellCertificate.v1.0"
        ),
        "witness_hash": (
            certificate["input"]["canonical_witness_sha256"]
            == canonical_json_hash(witness)
        ),
        "projected_gram_hash": (
            certificate["green_kernel"]["projected_gram_sha256"]
            == _projected_hash(gram_result.projected_gram)
        ),
        "proof_reproduction": proof == certificate["proof"],
        "actual_zeta_flag_false": (
            certificate["classification"][
                "actual_zeta_occupancy_family"
            ]
            is False
        ),
        "global_flag_false": (
            certificate["classification"]["global_rh_certificate"]
            is False
        ),
    }
    expected_pass = bool(certificate["proof"]["certificate_pass"])
    checks["classification_matches_proof"] = (
        certificate["classification"][
            "local_58cell_interval_certificate"
        ]
        is expected_pass
    )
    return {
        "schema": "RH.LocalIntervalGreen.CellVerification.v1.0",
        "checks": checks,
        "verification_pass": all(checks.values()),
        "certificate_pass": bool(proof["certificate_pass"]),
        "failure_class": proof["failure_class"],
        "recomputed_neumann_defect_upper": proof[
            "neumann_defect_infinity_norm_upper"
        ],
        "recomputed_first_minor_lower": proof.get(
            "first_leading_minor_lower"
        ),
        "recomputed_determinant_lower": proof.get(
            "determinant_lower"
        ),
        "actual_zeta_occupancy_family": False,
        "global_rh_certificate": False,
    }
