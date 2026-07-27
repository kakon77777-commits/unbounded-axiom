from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from fractions import Fraction
from typing import Iterable

from .decimal_interval import (
    CInterval,
    DInterval,
    complex_interval_sum,
    interval_sum,
)
from .rational_complex import QComplex, scale_interval
from .transcendental import complex_exp_rational


@dataclass(frozen=True)
class ExponentialDensity:
    name: str
    terms: tuple[tuple[QComplex, QComplex], ...]


@dataclass
class ProjectedGramResult:
    positive_functions: list[ExponentialDensity]
    negative_functions: list[ExponentialDensity]
    positive_weights: list[Fraction]
    negative_weights: list[Fraction]
    projected_gram: list[list[DInterval]]
    structural_gram: list[list[DInterval]]
    structural_determinant: DInterval
    maximum_unprojected_imaginary_width: Decimal
    maximum_projected_width: Decimal


def _fraction(row: dict[str, int]) -> Fraction:
    return Fraction(int(row["numerator"]), int(row["denominator"]))


def _fraction_matrix_inverse(
    matrix: list[list[Fraction]],
) -> list[list[Fraction]]:
    size = len(matrix)
    augmented = [
        row[:]
        + [
            Fraction(int(column == index))
            for column in range(size)
        ]
        for index, row in enumerate(matrix)
    ]
    for column in range(size):
        pivot = next(
            (
                row
                for row in range(column, size)
                if augmented[row][column] != 0
            ),
            None,
        )
        if pivot is None:
            raise ArithmeticError("singular rational boundary matrix")
        if pivot != column:
            augmented[column], augmented[pivot] = (
                augmented[pivot],
                augmented[column],
            )
        pivot_value = augmented[column][column]
        augmented[column] = [
            value / pivot_value
            for value in augmented[column]
        ]
        for row in range(size):
            if row == column:
                continue
            multiplier = augmented[row][column]
            if multiplier == 0:
                continue
            augmented[row] = [
                left - multiplier * right
                for left, right in zip(
                    augmented[row],
                    augmented[column],
                )
            ]
    return [row[size:] for row in augmented]


def structural_constant() -> ExponentialDensity:
    return ExponentialDensity(
        "constraint_G0",
        ((QComplex.one(), QComplex.zero()),),
    )


def structural_cosh_half() -> ExponentialDensity:
    half = Fraction(1, 2)
    coefficient = QComplex(half)
    return ExponentialDensity(
        "constraint_Gi2",
        (
            (coefficient, QComplex(half)),
            (coefficient, QComplex(-half)),
        ),
    )


def axis_density(name: str, x: Fraction) -> ExponentialDensity:
    coefficient = QComplex(Fraction(1, 2))
    return ExponentialDensity(
        name,
        (
            (coefficient, QComplex(Fraction(0), x)),
            (coefficient, QComplex(Fraction(0), -x)),
        ),
    )


def core_real_density(
    name: str,
    x: Fraction,
    y: Fraction,
) -> ExponentialDensity:
    quarter = QComplex(Fraction(1, 4))
    return ExponentialDensity(
        name,
        tuple(
            (
                quarter,
                QComplex(real_part, imag_part),
            )
            for real_part in (y, -y)
            for imag_part in (x, -x)
        ),
    )


def core_imag_density(
    name: str,
    x: Fraction,
    y: Fraction,
) -> ExponentialDensity:
    positive_i = QComplex(Fraction(0), Fraction(1, 4))
    negative_i = -positive_i
    return ExponentialDensity(
        name,
        (
            (positive_i, QComplex(y, x)),
            (negative_i, QComplex(-y, x)),
            (negative_i, QComplex(y, -x)),
            (positive_i, QComplex(-y, -x)),
        ),
    )


class IntervalClampedGreen:
    def __init__(self, radius: Fraction, tail_scale: Fraction):
        self.radius = radius
        self.tail_scale = tail_scale
        self._moment_cache: dict[
            tuple[QComplex, int],
            CInterval,
        ] = {}
        self._raw_pair_cache: dict[
            tuple[QComplex, QComplex],
            CInterval,
        ] = {}
        self._pair_cache: dict[
            tuple[QComplex, QComplex],
            CInterval,
        ] = {}
        self.maximum_imaginary_width = Decimal(0)
        radius_q = QComplex(radius)
        self._radius_q = radius_q
        r = radius
        boundary_matrix = [
            [Fraction(1), -r, r * r, -(r**3)],
            [Fraction(0), Fraction(1), -2 * r, 3 * r * r],
            [Fraction(1), r, r * r, r**3],
            [Fraction(0), Fraction(1), 2 * r, 3 * r * r],
        ]
        self.boundary_inverse = _fraction_matrix_inverse(
            boundary_matrix
        )

    def _exp_at_radius(
        self,
        exponent: QComplex,
        sign: int,
    ) -> CInterval:
        multiplier = QComplex(self.radius * sign)
        return complex_exp_rational(exponent * multiplier)

    def moment(self, exponent: QComplex, power: int) -> CInterval:
        key = (exponent, power)
        if key in self._moment_cache:
            return self._moment_cache[key]
        if exponent.is_zero():
            if power % 2:
                value = Fraction(0)
            else:
                value = (
                    2
                    * self.radius ** (power + 1)
                    / Fraction(power + 1)
                )
            result = QComplex(value).to_interval()
            self._moment_cache[key] = result
            return result

        inverse = exponent.inverse()
        plus = self._exp_at_radius(exponent, 1)
        minus = self._exp_at_radius(exponent, -1)
        upper_coefficient = QComplex(self.radius**power)
        lower_coefficient = QComplex((-self.radius) ** power)
        boundary = (
            scale_interval(plus, upper_coefficient)
            - scale_interval(minus, lower_coefficient)
        )
        first = scale_interval(boundary, inverse)
        if power == 0:
            result = first
        else:
            recurrence = QComplex(Fraction(power)) * inverse
            result = (
                first
                - scale_interval(
                    self.moment(exponent, power - 1),
                    recurrence,
                )
            )
        self._moment_cache[key] = result
        return result

    def _raw_exponential_pair(
        self,
        left: QComplex,
        right: QComplex,
    ) -> CInterval:
        key = (left, right)
        if key in self._raw_pair_cache:
            return self._raw_pair_cache[key]
        if right.is_zero():
            prefactor = QComplex(
                Fraction(1, 24) / self.tail_scale
            )
            polynomial_integral = (
                self.moment(left, 4)
                - scale_interval(
                    self.moment(left, 2),
                    QComplex(2 * self.radius * self.radius),
                )
                + scale_interval(
                    self.moment(left, 0),
                    QComplex(self.radius**4),
                )
            )
            result = scale_interval(
                polynomial_integral,
                prefactor,
            )
            self._raw_pair_cache[key] = result
            return result

        prefactor = (
            QComplex(self.tail_scale)
            * right.pow_int(4)
        ).inverse()
        minus_boundary = self._exp_at_radius(right, -1)
        plus_boundary = self._exp_at_radius(right, 1)
        right_times_prefactor = right * prefactor
        boundary_rhs = [
            scale_interval(minus_boundary, -prefactor),
            scale_interval(
                minus_boundary,
                -right_times_prefactor,
            ),
            scale_interval(plus_boundary, -prefactor),
            scale_interval(
                plus_boundary,
                -right_times_prefactor,
            ),
        ]
        polynomial_coefficients = [
            complex_interval_sum(
                scale_interval(value, QComplex(coefficient))
                for coefficient, value in zip(
                    inverse_row,
                    boundary_rhs,
                )
            )
            for inverse_row in self.boundary_inverse
        ]
        result = scale_interval(
            self.moment(left + right, 0),
            prefactor,
        )
        for power, coefficient in enumerate(
            polynomial_coefficients
        ):
            result = result + coefficient * self.moment(
                left,
                power,
            )
        self._raw_pair_cache[key] = result
        return result

    def exponential_pair(
        self,
        left: QComplex,
        right: QComplex,
    ) -> CInterval:
        key = (left, right)
        if key in self._pair_cache:
            return self._pair_cache[key]
        direct = self._raw_exponential_pair(left, right)
        if left == right:
            result = direct
        else:
            reverse = self._raw_exponential_pair(right, left)
            result = direct.intersect(reverse)
        self._pair_cache[(left, right)] = result
        self._pair_cache[(right, left)] = result
        return result

    def density_pair(
        self,
        left: ExponentialDensity,
        right: ExponentialDensity,
    ) -> DInterval:
        result = CInterval.zero()
        for left_coefficient, left_exponent in left.terms:
            for right_coefficient, right_exponent in right.terms:
                coefficient = (
                    left_coefficient * right_coefficient
                )
                result = result + scale_interval(
                    self.exponential_pair(
                        left_exponent,
                        right_exponent,
                    ),
                    coefficient,
                )
        if not result.im.contains_zero():
            raise ArithmeticError(
                f"real density pairing lost reality: "
                f"{left.name}, {right.name}, {result.im}"
            )
        self.maximum_imaginary_width = max(
            self.maximum_imaginary_width,
            result.im.width(),
        )
        return result.re


def _inverse_symmetric_two_by_two(
    matrix: list[list[DInterval]],
) -> tuple[list[list[DInterval]], DInterval]:
    determinant = (
        matrix[0][0] * matrix[1][1]
        - matrix[0][1].square()
    )
    if determinant.lo <= 0:
        raise ArithmeticError(
            f"structural Gram determinant not positive: {determinant}"
        )
    inverse_determinant = determinant.reciprocal()
    inverse = [
        [
            matrix[1][1] * inverse_determinant,
            -matrix[0][1] * inverse_determinant,
        ],
        [
            -matrix[0][1] * inverse_determinant,
            matrix[0][0] * inverse_determinant,
        ],
    ]
    return inverse, determinant


def _bilinear_two(
    left: list[DInterval],
    matrix: list[list[DInterval]],
    right: list[DInterval],
) -> DInterval:
    return interval_sum(
        left[row] * matrix[row][column] * right[column]
        for row in range(2)
        for column in range(2)
    )


def functions_from_witness(
    witness: dict[str, object],
) -> tuple[
    list[ExponentialDensity],
    list[ExponentialDensity],
    list[Fraction],
    list[Fraction],
]:
    model = witness["model"]
    alpha = _fraction(model["target_alpha"])
    count_coefficients = [
        _fraction(row)
        for row in model["count_coefficients"]
    ]
    positive_functions: list[ExponentialDensity] = []
    negative_functions: list[ExponentialDensity] = []
    positive_weights: list[Fraction] = []
    negative_weights: list[Fraction] = []
    for band_index, (coefficient, support) in enumerate(
        zip(count_coefficients, witness["axis_supports"])
    ):
        for atom_index, atom in enumerate(support):
            x = _fraction(atom["x"])
            weight = _fraction(atom["weight"])
            positive_functions.append(
                axis_density(
                    f"axis_b{band_index}_a{atom_index}",
                    x,
                )
            )
            positive_weights.append(coefficient * weight)
    for atom_index, atom in enumerate(witness["core_support"]):
        x = _fraction(atom["x"])
        y = _fraction(atom["y"])
        weight = _fraction(atom["weight"])
        signed_weight = 2 * alpha * weight
        positive_functions.append(
            core_real_density(f"core_u_{atom_index}", x, y)
        )
        positive_weights.append(signed_weight)
        negative_functions.append(
            core_imag_density(f"core_v_{atom_index}", x, y)
        )
        negative_weights.append(signed_weight)
    return (
        positive_functions,
        negative_functions,
        positive_weights,
        negative_weights,
    )


def build_projected_gram(
    witness: dict[str, object],
) -> ProjectedGramResult:
    model = witness["model"]
    radius = _fraction(model["radius"])
    tail_scale = _fraction(
        model["tail_scale_lower_decimal_rational"]
    )
    evaluator = IntervalClampedGreen(radius, tail_scale)
    structural = [structural_constant(), structural_cosh_half()]
    (
        positive_functions,
        negative_functions,
        positive_weights,
        negative_weights,
    ) = functions_from_witness(witness)
    evaluation_functions = (
        positive_functions + negative_functions
    )

    structural_gram = [
        [DInterval.zero() for _ in range(2)]
        for _ in range(2)
    ]
    for row in range(2):
        for column in range(row, 2):
            value = evaluator.density_pair(
                structural[row],
                structural[column],
            )
            structural_gram[row][column] = value
            structural_gram[column][row] = value
    structural_inverse, structural_determinant = (
        _inverse_symmetric_two_by_two(structural_gram)
    )
    cross = [
        [
            evaluator.density_pair(
                structural[row],
                function,
            )
            for function in evaluation_functions
        ]
        for row in range(2)
    ]
    count = len(evaluation_functions)
    projected = [
        [DInterval.zero() for _ in range(count)]
        for _ in range(count)
    ]
    maximum_width = Decimal(0)
    for row in range(count):
        left_cross = [cross[0][row], cross[1][row]]
        for column in range(row, count):
            right_cross = [
                cross[0][column],
                cross[1][column],
            ]
            raw = evaluator.density_pair(
                evaluation_functions[row],
                evaluation_functions[column],
            )
            correction = _bilinear_two(
                left_cross,
                structural_inverse,
                right_cross,
            )
            value = raw - correction
            projected[row][column] = value
            projected[column][row] = value
            maximum_width = max(maximum_width, value.width())
    return ProjectedGramResult(
        positive_functions=positive_functions,
        negative_functions=negative_functions,
        positive_weights=positive_weights,
        negative_weights=negative_weights,
        projected_gram=projected,
        structural_gram=structural_gram,
        structural_determinant=structural_determinant,
        maximum_unprojected_imaginary_width=(
            evaluator.maximum_imaginary_width
        ),
        maximum_projected_width=maximum_width,
    )

