from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from typing import Any

import numpy as np
from scipy.linalg import eigh

from .context import TailDualContext, rational_patch_center
from .cover import Patch


def generalized_negative_threshold(
    core_matrix: np.ndarray,
    positive_matrix: np.ndarray,
) -> float:
    eigenvalues = eigh(
        0.5 * (core_matrix + core_matrix.T),
        0.5 * (positive_matrix + positive_matrix.T),
        eigvals_only=True,
    )
    negative = eigenvalues[eigenvalues < -1e-12]
    if not len(negative):
        return math.inf
    return float(np.min(-1.0 / negative))


def witness_matrix(
    tail_matrix: np.ndarray,
    axis_average: np.ndarray,
    core_matrix: np.ndarray,
    alpha: float,
    tail_fraction: float,
) -> np.ndarray:
    matrix = (
        tail_fraction * tail_matrix
        + axis_average
        + alpha * core_matrix
    )
    return 0.5 * (matrix + matrix.T)


def decimal_string(value: float, decimals: int) -> str:
    return f"{float(value):.{decimals}f}"


def downward_decimal_string(value: float, decimals: int) -> str:
    scale = 10**decimals
    lowered = math.floor(float(value) * scale) / scale
    return f"{lowered:.{decimals}f}"


def matrix_strings(
    matrix: np.ndarray,
    decimals: int,
) -> list[list[str]]:
    return [
        [decimal_string(value, decimals) for value in row]
        for row in np.asarray(matrix)
    ]


def vector_strings(
    vector: np.ndarray,
    decimals: int,
) -> list[str]:
    return [
        decimal_string(value, decimals)
        for value in np.asarray(vector)
    ]


def make_rational_payload(
    context: TailDualContext,
    patches: list[Patch],
    axis_grid: np.ndarray,
    alpha: int = 2,
    tail_fraction: Fraction = Fraction(1, 1000),
    decimals: int = 12,
) -> dict[str, Any]:
    band = context.bands[1]
    axis_transforms = context.axis_transforms(axis_grid)
    patch_rows = []
    for patch in patches:
        x, y = rational_patch_center(patch)
        transform = context.core_transform(
            complex(float(x), float(y))
        )
        patch_rows.append(
            {
                "patch_id": patch.patch_id,
                "center_x": str(x),
                "center_y": str(y),
                "core_transform_real": vector_strings(
                    transform.real, decimals
                ),
                "core_transform_imag": vector_strings(
                    transform.imag, decimals
                ),
            }
        )
    return {
        "schema": "RH.AxisTarget.RationalDualModel.v0.3",
        "decimal_places": decimals,
        "dimension": context.dimension,
        "alpha": str(alpha),
        "tail_fraction": (
            f"{tail_fraction.numerator}/{tail_fraction.denominator}"
        ),
        "axis_band": {
            "band_id": band.band_id,
            "start": str(band.start),
            "stop": str(band.stop),
            "count_coefficient_downward": downward_decimal_string(
                band.count_majorant, decimals
            ),
            "original_floating_count_coefficient": band.count_majorant,
        },
        "axis_grid": [
            decimal_string(value, decimals) for value in axis_grid
        ],
        "axis_transform_vectors": [
            vector_strings(row, decimals) for row in axis_transforms
        ],
        "tail_matrix": matrix_strings(
            context.tail_matrix, decimals
        ),
        "patches": patch_rows,
        "construction": (
            "P(x)=g(x)g(x)^T; "
            "C(z)=2(Re(g)Re(g)^T-Im(g)Im(g)^T); "
            "W=rho*T+N1*mean(P)+alpha*C."
        ),
    }


def parse_fraction_matrix(rows: list[list[str]]) -> list[list[Fraction]]:
    return [[Fraction(value) for value in row] for row in rows]


def exact_ldl_positive(
    matrix: list[list[Fraction]],
) -> tuple[bool, list[Fraction]]:
    dimension = len(matrix)
    lower = [
        [Fraction(0) for _ in range(dimension)]
        for _ in range(dimension)
    ]
    diagonal: list[Fraction] = []
    for i in range(dimension):
        lower[i][i] = Fraction(1)
        pivot = matrix[i][i] - sum(
            lower[i][k] * lower[i][k] * diagonal[k]
            for k in range(i)
        )
        diagonal.append(pivot)
        if pivot <= 0:
            return False, diagonal
        for j in range(i + 1, dimension):
            lower[j][i] = (
                matrix[j][i]
                - sum(
                    lower[j][k]
                    * lower[i][k]
                    * diagonal[k]
                    for k in range(i)
                )
            ) / pivot
    return True, diagonal


def _outer(
    left: list[Fraction],
    right: list[Fraction],
) -> list[list[Fraction]]:
    return [
        [left[i] * right[j] for j in range(len(right))]
        for i in range(len(left))
    ]


def verify_rational_payload(
    payload: dict[str, Any],
) -> dict[str, Any]:
    dimension = int(payload["dimension"])
    alpha = Fraction(payload["alpha"])
    tail_fraction = Fraction(payload["tail_fraction"])
    count_coefficient = Fraction(
        payload["axis_band"]["count_coefficient_downward"]
    )
    tail = parse_fraction_matrix(payload["tail_matrix"])
    axis_vectors = [
        [Fraction(value) for value in row]
        for row in payload["axis_transform_vectors"]
    ]
    axis_average = [
        [
            count_coefficient
            * sum(vector[i] * vector[j] for vector in axis_vectors)
            / len(axis_vectors)
            for j in range(dimension)
        ]
        for i in range(dimension)
    ]

    tail_positive, tail_pivots = exact_ldl_positive(tail)
    rows = []
    all_positive = tail_positive
    for patch in payload["patches"]:
        real = [
            Fraction(value)
            for value in patch["core_transform_real"]
        ]
        imag = [
            Fraction(value)
            for value in patch["core_transform_imag"]
        ]
        real_outer = _outer(real, real)
        imag_outer = _outer(imag, imag)
        core = [
            [
                2 * (real_outer[i][j] - imag_outer[i][j])
                for j in range(dimension)
            ]
            for i in range(dimension)
        ]
        witness = [
            [
                tail_fraction * tail[i][j]
                + axis_average[i][j]
                + alpha * core[i][j]
                for j in range(dimension)
            ]
            for i in range(dimension)
        ]
        positive, pivots = exact_ldl_positive(witness)
        all_positive = all_positive and positive
        rows.append(
            {
                "patch_id": patch["patch_id"],
                "exact_ldl_positive": positive,
                "pivot_count": len(pivots),
                "minimum_pivot_float": float(min(pivots)),
                "maximum_pivot_bit_length": max(
                    value.numerator.bit_length()
                    + value.denominator.bit_length()
                    for value in pivots
                ),
            }
        )

    canonical = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return {
        "schema": "RH.AxisTarget.RationalVerification.v0.3",
        "payload_sha256": hashlib.sha256(canonical).hexdigest(),
        "tail_exact_ldl_positive": tail_positive,
        "tail_minimum_pivot_float": float(min(tail_pivots)),
        "patch_rows": rows,
        "all_exact_ldl_positive": all_positive,
        "logical_lower_bound": int(alpha),
        "global_rh_certificate": False,
        "scope": (
            "Exact positivity for the exported decimal-rational "
            "finite surrogate only."
        ),
    }
