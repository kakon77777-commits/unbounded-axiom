from __future__ import annotations

from fractions import Fraction
from typing import Any

from .rational_interval import (
    QInterval,
    as_fraction,
    fraction_text,
    interval_sum,
)


def green_point(x: Fraction, y: Fraction) -> Fraction:
    """Dirichlet Laplacian Green kernel on the unit interval."""

    x = as_fraction(x)
    y = as_fraction(y)
    return min(x, y) - x * y


def green_diagonal_interval(x: QInterval) -> QInterval:
    endpoint_values = (
        x.lo * (1 - x.lo),
        x.hi * (1 - x.hi),
    )
    upper = max(endpoint_values)
    if x.lo <= Fraction(1, 2) <= x.hi:
        upper = Fraction(1, 4)
    return QInterval(min(endpoint_values), upper)


def green_interval(x: QInterval, y: QInterval) -> QInterval:
    """Enclose K(x,y), preserving exact ordering whenever available."""

    if x.lo == x.hi and y.lo != y.hi:
        return green_interval(y, x)
    if y.lo == y.hi:
        point = y.lo
        pieces: list[QInterval] = []
        left_hi = min(x.hi, point)
        if x.lo <= left_hi:
            pieces.append(QInterval(x.lo, left_hi) * (1 - point))
        right_lo = max(x.lo, point)
        if right_lo <= x.hi:
            pieces.append(
                QInterval.point(point)
                * (1 - QInterval(right_lo, x.hi))
            )
        if not pieces:
            raise ArithmeticError("point split produced no Green pieces")
        output = pieces[0]
        for piece in pieces[1:]:
            output = output.hull(piece)
        return output
    if x.hi <= y.lo:
        return x * (1 - y)
    if y.hi <= x.lo:
        return y * (1 - x)

    # Conservative independent-variable enclosure for overlapping cells.
    minimum = QInterval(
        min(x.lo, y.lo),
        min(x.hi, y.hi),
    )
    return minimum - x * y


def _point_inverse_two(
    matrix: list[list[Fraction]],
) -> list[list[Fraction]]:
    determinant = (
        matrix[0][0] * matrix[1][1]
        - matrix[0][1] * matrix[1][0]
    )
    if determinant == 0:
        raise ArithmeticError("singular point matrix")
    return [
        [matrix[1][1] / determinant, -matrix[0][1] / determinant],
        [-matrix[1][0] / determinant, matrix[0][0] / determinant],
    ]


def _interval_inverse_two(
    matrix: list[list[QInterval]],
) -> tuple[list[list[QInterval]], QInterval]:
    off_diagonal = matrix[0][1].hull(matrix[1][0])
    determinant = (
        matrix[0][0] * matrix[1][1]
        - off_diagonal.square()
    )
    if determinant.lo <= 0:
        raise ArithmeticError(
            "positive-system interval determinant is not positive"
        )
    return (
        [
            [
                matrix[1][1] / determinant,
                -off_diagonal / determinant,
            ],
            [
                -off_diagonal / determinant,
                matrix[0][0] / determinant,
            ],
        ],
        determinant,
    )


def _matmul_point(
    left: list[list[Fraction]],
    right: list[list[Fraction]],
) -> list[list[Fraction]]:
    return [
        [
            sum(
                left[row][index] * right[index][column]
                for index in range(len(right))
            )
            for column in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def _transpose_point(
    matrix: list[list[Fraction]],
) -> list[list[Fraction]]:
    return [list(row) for row in zip(*matrix)]


def model_parameters(model: dict[str, Any]) -> dict[str, Any]:
    cells = model["occupancy_cells"]
    negative = model["negative_targets"]
    if len(cells) != 2 or len(negative) != 2:
        raise ValueError("v0.9 exact prototype requires two-by-two ranks")
    return {
        "positive_weights": [
            as_fraction(row["operator_weight"]) for row in cells
        ],
        "negative_weights": [
            as_fraction(row["operator_weight"]) for row in negative
        ],
        "negative_points": [
            as_fraction(row["point"]) for row in negative
        ],
    }


def schur_point(
    points: list[Fraction],
    model: dict[str, Any],
) -> dict[str, Any]:
    parameters = model_parameters(model)
    positive_weights = parameters["positive_weights"]
    negative_weights = parameters["negative_weights"]
    targets = parameters["negative_points"]
    points = [as_fraction(value) for value in points]

    k_xx = [
        [green_point(left, right) for right in points]
        for left in points
    ]
    system = [
        [
            (
                Fraction(1, 1) / positive_weights[row]
                if row == column
                else Fraction(0)
            )
            + k_xx[row][column]
            for column in range(2)
        ]
        for row in range(2)
    ]
    inverse = _point_inverse_two(system)
    k_yx = [
        [green_point(target, point) for point in points]
        for target in targets
    ]
    correction = _matmul_point(
        _matmul_point(k_yx, inverse),
        _transpose_point(k_yx),
    )
    k_yy = [
        [green_point(left, right) for right in targets]
        for left in targets
    ]
    schur = [
        [
            (
                Fraction(1, 1) / negative_weights[row]
                if row == column
                else Fraction(0)
            )
            - k_yy[row][column]
            + correction[row][column]
            for column in range(2)
        ]
        for row in range(2)
    ]
    determinant = (
        schur[0][0] * schur[1][1]
        - schur[0][1] * schur[1][0]
    )
    return {
        "positive_system": system,
        "schur_matrix": schur,
        "schur_determinant": determinant,
    }


def schur_interval(
    box: list[QInterval],
    model: dict[str, Any],
) -> dict[str, Any]:
    parameters = model_parameters(model)
    positive_weights = parameters["positive_weights"]
    negative_weights = parameters["negative_weights"]
    target_intervals = [
        QInterval.point(value)
        for value in parameters["negative_points"]
    ]

    k_xx = [
        [
            (
                green_diagonal_interval(box[row])
                if row == column
                else green_interval(box[row], box[column])
            )
            for column in range(2)
        ]
        for row in range(2)
    ]
    system = [
        [
            (
                QInterval.point(1 / positive_weights[row])
                if row == column
                else QInterval.point(0)
            )
            + k_xx[row][column]
            for column in range(2)
        ]
        for row in range(2)
    ]
    inverse, system_determinant = _interval_inverse_two(system)
    k_yx = [
        [
            green_interval(target, point)
            for point in box
        ]
        for target in target_intervals
    ]
    correction = [
        [
            interval_sum(
                k_yx[row][left]
                * inverse[left][right]
                * k_yx[column][right]
                for left in range(2)
                for right in range(2)
            )
            for column in range(2)
        ]
        for row in range(2)
    ]
    k_yy = [
        [
            (
                green_diagonal_interval(target_intervals[row])
                if row == column
                else green_interval(
                    target_intervals[row],
                    target_intervals[column],
                )
            )
            for column in range(2)
        ]
        for row in range(2)
    ]
    raw_schur = [
        [
            (
                QInterval.point(1 / negative_weights[row])
                if row == column
                else QInterval.point(0)
            )
            - k_yy[row][column]
            + correction[row][column]
            for column in range(2)
        ]
        for row in range(2)
    ]
    off_diagonal = raw_schur[0][1].hull(raw_schur[1][0])
    schur = [
        [raw_schur[0][0], off_diagonal],
        [off_diagonal, raw_schur[1][1]],
    ]
    determinant = (
        schur[0][0] * schur[1][1]
        - off_diagonal.square()
    )
    passes = schur[0][0].lo > 0 and determinant.lo > 0
    return {
        "positive_system_determinant": system_determinant,
        "schur_matrix": schur,
        "first_leading_minor": schur[0][0],
        "schur_determinant": determinant,
        "sylvester_positive": passes,
    }


def interval_proof_json(proof: dict[str, Any]) -> dict[str, Any]:
    return {
        "positive_system_determinant": proof[
            "positive_system_determinant"
        ].to_json(),
        "schur_matrix": [
            [value.to_json() for value in row]
            for row in proof["schur_matrix"]
        ],
        "first_leading_minor": proof[
            "first_leading_minor"
        ].to_json(),
        "schur_determinant": proof["schur_determinant"].to_json(),
        "sylvester_positive": proof["sylvester_positive"],
    }


def point_proof_json(proof: dict[str, Any]) -> dict[str, Any]:
    return {
        "positive_system": [
            [fraction_text(value) for value in row]
            for row in proof["positive_system"]
        ],
        "schur_matrix": [
            [fraction_text(value) for value in row]
            for row in proof["schur_matrix"]
        ],
        "schur_determinant": fraction_text(
            proof["schur_determinant"]
        ),
    }

