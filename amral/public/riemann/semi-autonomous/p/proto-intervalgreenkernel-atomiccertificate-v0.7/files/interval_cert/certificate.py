from __future__ import annotations

import hashlib
import json
from decimal import Decimal
from fractions import Fraction
from typing import Any

from .decimal_interval import (
    DInterval,
    decimal_add_upper,
    decimal_div_upper,
    decimal_sub_lower,
    interval_sum,
)
from .green import ProjectedGramResult, build_projected_gram
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
    gram_result: ProjectedGramResult,
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


def _neumann_and_sylvester(
    gram_result: ProjectedGramResult,
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
    if defect_norm >= 1:
        raise ArithmeticError(
            f"Neumann defect does not prove regularity: {defect_norm}"
        )

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
    if not sylvester_pass:
        raise ArithmeticError(
            "final two-by-two interval Sylvester test failed"
        )
    return {
        "neumann_defect_infinity_norm_upper": str(defect_norm),
        "neumann_regular": True,
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
        "sylvester_positive_definite": True,
    }


def _probability_checks(witness: dict[str, Any]) -> dict[str, Any]:
    axis_sums = [
        sum(
            (
                Fraction(
                    atom["weight"]["numerator"],
                    atom["weight"]["denominator"],
                )
                for atom in support
            ),
            Fraction(0),
        )
        for support in witness["axis_supports"]
    ]
    core_sum = sum(
        (
            Fraction(
                atom["weight"]["numerator"],
                atom["weight"]["denominator"],
            )
            for atom in witness["core_support"]
        ),
        Fraction(0),
    )
    return {
        "axis_probability_sums": [
            f"{value.numerator}/{value.denominator}"
            for value in axis_sums
        ],
        "core_probability_sum": (
            f"{core_sum.numerator}/{core_sum.denominator}"
        ),
        "all_probability_sums_exactly_one": bool(
            all(value == 1 for value in axis_sums)
            and core_sum == 1
        ),
    }


def build_certificate(witness: dict[str, Any]) -> dict[str, Any]:
    gram_result = build_projected_gram(witness)
    system, cross, _ = _system_from_gram(gram_result)
    inverse_strings, solution_strings = _candidate_matrices(
        system,
        cross,
    )
    proof = _neumann_and_sylvester(
        gram_result,
        inverse_strings,
        solution_strings,
    )
    probability = _probability_checks(witness)
    if not probability["all_probability_sums_exactly_one"]:
        raise ArithmeticError("witness probability normalization failed")
    if not all(weight > 0 for weight in gram_result.positive_weights):
        raise ArithmeticError("positive factor contains nonpositive weight")
    if not all(weight > 0 for weight in gram_result.negative_weights):
        raise ArithmeticError("negative factor contains nonpositive weight")

    return {
        "schema": "RH.IntervalGreenKernel.AtomicCertificate.v0.7",
        "node": "RH-IntervalGreenKernel-AtomicCertificate-20260725-v0.7",
        "statement": {
            "domain": (
                "even clamped H_0^2(-16,16) with G(0)=G(i/2)=0"
            ),
            "tail_scale": witness["model"][
                "tail_scale_lower_decimal_rational"
            ],
            "target_alpha": witness["model"]["target_alpha"],
            "claim": (
                "The fixed rational atomic dual witness defines a "
                "strictly positive operator in the abstract continuous "
                "Green-kernel model."
            ),
        },
        "input": {
            "canonical_witness_sha256": canonical_json_hash(witness),
            "axis_atom_count": sum(
                len(support)
                for support in witness["axis_supports"]
            ),
            "positive_rank": len(gram_result.positive_functions),
            "negative_rank": len(gram_result.negative_functions),
            **probability,
        },
        "arithmetic": transcendental_audit(),
        "green_kernel": {
            "method": (
                "closed clamped D^4 inverse; exponential moments; "
                "two-sided orientation intersection"
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
            "abstract_continuous_interval_certificate": True,
            "abstract_operator_strictly_positive": True,
            "zeta_facing_tail_theorem_certified": False,
            "zeta_facing_count_coefficients_certified": False,
            "explicit_formula_admissibility_certified": False,
            "global_rh_certificate": False,
        },
        "trust_boundary": (
            "This certifies Layer A only. It does not certify that the "
            "rational coefficients are valid zeta-facing lower bounds, "
            "nor the global explicit-formula transfer."
        ),
    }


def verify_certificate(
    witness: dict[str, Any],
    certificate: dict[str, Any],
) -> dict[str, Any]:
    checks: dict[str, bool] = {
        "schema": (
            certificate.get("schema")
            == "RH.IntervalGreenKernel.AtomicCertificate.v0.7"
        ),
        "witness_hash": (
            certificate["input"]["canonical_witness_sha256"]
            == canonical_json_hash(witness)
        ),
        "global_flag_false": (
            certificate["classification"]["global_rh_certificate"]
            is False
        ),
        "layer_b_flags_false": all(
            certificate["classification"][key] is False
            for key in (
                "zeta_facing_tail_theorem_certified",
                "zeta_facing_count_coefficients_certified",
                "explicit_formula_admissibility_certified",
            )
        ),
    }
    gram_result = build_projected_gram(witness)
    checks["projected_gram_hash"] = (
        certificate["green_kernel"]["projected_gram_sha256"]
        == _projected_hash(gram_result.projected_gram)
    )
    checks["structural_determinant_positive"] = (
        gram_result.structural_determinant.lo > 0
    )
    candidate = certificate["neumann_candidate"]
    recomputed_proof = _neumann_and_sylvester(
        gram_result,
        candidate["inverse_decimal_rational"],
        candidate["solution_decimal_rational"],
    )
    checks["proof_reproduction"] = (
        recomputed_proof == certificate["proof"]
    )
    checks["neumann_regular"] = bool(
        recomputed_proof["neumann_regular"]
    )
    checks["sylvester_positive"] = bool(
        recomputed_proof["sylvester_positive_definite"]
    )
    checks["abstract_flag_true"] = (
        certificate["classification"][
            "abstract_continuous_interval_certificate"
        ]
        is True
    )
    return {
        "schema": "RH.IntervalGreenKernel.Verification.v0.7",
        "checks": checks,
        "verification_pass": all(checks.values()),
        "recomputed_neumann_defect_upper": recomputed_proof[
            "neumann_defect_infinity_norm_upper"
        ],
        "recomputed_first_minor_lower": recomputed_proof[
            "first_leading_minor_lower"
        ],
        "recomputed_determinant_lower": recomputed_proof[
            "determinant_lower"
        ],
        "abstract_continuous_interval_certificate": bool(
            all(checks.values())
        ),
        "global_rh_certificate": False,
    }

