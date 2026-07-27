from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, localcontext
from fractions import Fraction

from .decimal_interval import (
    CInterval,
    DInterval,
    HIGH_CONTEXT,
    complex_interval_sum,
    interval_sum,
)
from .rational_complex import QComplex, scale_interval
from .transcendental import complex_exp_interval, exp_interval


MOMENT_SERIES_TERMS = 28


@dataclass(frozen=True)
class BoxExponentialDensity:
    name: str
    terms: tuple[tuple[QComplex, "AffineExponent"], ...]


@dataclass(frozen=True)
class AffineExponent:
    """Complex exponent with named, shared real perturbation variables."""

    center: QComplex
    perturbations: tuple[
        tuple[str, QComplex, Fraction],
        ...,
    ] = ()

    @staticmethod
    def point(value: QComplex) -> "AffineExponent":
        return AffineExponent(value)

    def __neg__(self) -> "AffineExponent":
        return AffineExponent(
            -self.center,
            tuple(
                (name, -coefficient, half_width)
                for name, coefficient, half_width
                in self.perturbations
            ),
        )

    def __add__(
        self,
        other: "AffineExponent",
    ) -> "AffineExponent":
        merged: dict[str, tuple[QComplex, Fraction]] = {}
        for name, coefficient, half_width in (
            self.perturbations + other.perturbations
        ):
            if name in merged:
                previous, previous_width = merged[name]
                if previous_width != half_width:
                    raise ValueError(
                        f"inconsistent width for variable {name}"
                    )
                coefficient = previous + coefficient
            if coefficient.is_zero():
                merged.pop(name, None)
            else:
                merged[name] = (coefficient, half_width)
        return AffineExponent(
            self.center + other.center,
            tuple(
                (
                    name,
                    coefficient,
                    half_width,
                )
                for name, (coefficient, half_width)
                in sorted(merged.items())
            ),
        )

    def enclosure(self) -> CInterval:
        result = self.center.to_interval()
        for _, coefficient, half_width in self.perturbations:
            delta = DInterval.from_fraction(half_width)
            signed_delta = DInterval(-delta.hi, delta.hi)
            result = result + (
                coefficient.to_interval()
                * CInterval(signed_delta, DInterval.zero())
            )
        return result


@dataclass
class BoxProjectedGramResult:
    positive_functions: list[BoxExponentialDensity]
    negative_functions: list[BoxExponentialDensity]
    positive_weights: list[Fraction]
    negative_weights: list[Fraction]
    projected_gram: list[list[DInterval]]
    structural_gram: list[list[DInterval]]
    structural_determinant: DInterval
    maximum_unprojected_imaginary_width: Decimal
    maximum_projected_width: Decimal
    moment_series_terms: int


def _fraction(row: dict[str, int]) -> Fraction:
    return Fraction(int(row["numerator"]), int(row["denominator"]))


def _complex_point(value: QComplex) -> CInterval:
    return value.to_interval()


def _complex_pow(value: CInterval, exponent: int) -> CInterval:
    if exponent < 0:
        return _complex_pow(value, -exponent).reciprocal()
    result = CInterval.one()
    base = value
    power = exponent
    while power:
        if power & 1:
            result = result * base
        power >>= 1
        if power:
            base = base * base
    return result


def _is_exact_zero(value: CInterval) -> bool:
    return (
        value.re.lo == 0
        and value.re.hi == 0
        and value.im.lo == 0
        and value.im.hi == 0
    )


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


def structural_constant() -> BoxExponentialDensity:
    return BoxExponentialDensity(
        "constraint_G0",
        ((QComplex.one(), AffineExponent.point(QComplex.zero())),),
    )


def structural_cosh_half() -> BoxExponentialDensity:
    half = Fraction(1, 2)
    coefficient = QComplex(half)
    return BoxExponentialDensity(
        "constraint_Gi2",
        (
            (coefficient, AffineExponent.point(QComplex(half))),
            (coefficient, AffineExponent.point(QComplex(-half))),
        ),
    )


def axis_box_density(
    name: str,
    center: Fraction,
    half_width: Fraction,
) -> BoxExponentialDensity:
    coefficient = QComplex(Fraction(1, 2))
    positive = AffineExponent(
        QComplex(Fraction(0), center),
        (
            (
                name,
                QComplex(Fraction(0), Fraction(1)),
                half_width,
            ),
        ),
    )
    return BoxExponentialDensity(
        name,
        (
            (coefficient, positive),
            (coefficient, -positive),
        ),
    )


def core_real_density(
    name: str,
    x: Fraction,
    y: Fraction,
) -> BoxExponentialDensity:
    quarter = QComplex(Fraction(1, 4))
    return BoxExponentialDensity(
        name,
        tuple(
            (
                quarter,
                AffineExponent.point(
                    QComplex(real_part, imag_part)
                ),
            )
            for real_part in (y, -y)
            for imag_part in (x, -x)
        ),
    )


def core_imag_density(
    name: str,
    x: Fraction,
    y: Fraction,
) -> BoxExponentialDensity:
    positive_i = QComplex(Fraction(0), Fraction(1, 4))
    negative_i = -positive_i
    return BoxExponentialDensity(
        name,
        (
            (
                positive_i,
                AffineExponent.point(QComplex(y, x)),
            ),
            (
                negative_i,
                AffineExponent.point(QComplex(-y, x)),
            ),
            (
                negative_i,
                AffineExponent.point(QComplex(y, -x)),
            ),
            (
                positive_i,
                AffineExponent.point(QComplex(-y, -x)),
            ),
        ),
    )


class BoxIntervalClampedGreen:
    """Directed Green pairing for rectangular complex-exponent cells."""

    def __init__(self, radius: Fraction, tail_scale: Fraction):
        self.radius = radius
        self.tail_scale = tail_scale
        self._moment_cache: dict[
            tuple[CInterval, int],
            CInterval,
        ] = {}
        self._raw_pair_cache: dict[
            tuple[AffineExponent, AffineExponent],
            CInterval,
        ] = {}
        self._pair_cache: dict[
            tuple[AffineExponent, AffineExponent],
            CInterval,
        ] = {}
        self.maximum_imaginary_width = Decimal(0)
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
        exponent: CInterval,
        sign: int,
    ) -> CInterval:
        multiplier = QComplex(self.radius * sign)
        return complex_exp_interval(
            scale_interval(exponent, multiplier)
        )

    def _polynomial_moment(self, power: int) -> CInterval:
        if power % 2:
            value = Fraction(0)
        else:
            value = (
                2
                * self.radius ** (power + 1)
                / Fraction(power + 1)
            )
        return _complex_point(QComplex(value))

    def _series_moment(
        self,
        exponent: CInterval,
        power: int,
    ) -> CInterval:
        """Analytic enclosure that remains regular when the box contains 0."""
        total = CInterval.zero()
        exponent_power = CInterval.one()
        factorial = 1
        for index in range(MOMENT_SERIES_TERMS + 1):
            polynomial = self._polynomial_moment(power + index)
            coefficient = QComplex(Fraction(1, factorial))
            total = total + scale_interval(
                exponent_power * polynomial,
                coefficient,
            )
            exponent_power = exponent_power * exponent
            factorial *= index + 1

        norm_upper = (
            exponent.re.abs_upper() + exponent.im.abs_upper()
        )
        with localcontext(HIGH_CONTEXT):
            scaled_norm = norm_upper * (
                Decimal(self.radius.numerator)
                / Decimal(self.radius.denominator)
            )
        exponential_upper = exp_interval(
            DInterval(Decimal(0), scaled_norm)
        ).hi
        absolute_integral = DInterval.from_fraction(
            2
            * self.radius ** (power + 1)
            / Fraction(power + 1)
        ).hi
        with localcontext(HIGH_CONTEXT):
            remainder = (
                absolute_integral
                * exponential_upper
                * scaled_norm ** (MOMENT_SERIES_TERMS + 1)
                / Decimal(
                    _factorial(MOMENT_SERIES_TERMS + 1)
                )
            )
        return CInterval(
            total.re.widen(remainder),
            total.im.widen(remainder),
        )

    def moment(
        self,
        exponent: CInterval,
        power: int,
    ) -> CInterval:
        key = (exponent, power)
        if key in self._moment_cache:
            return self._moment_cache[key]
        if _is_exact_zero(exponent):
            result = self._polynomial_moment(power)
            self._moment_cache[key] = result
            return result
        if (
            exponent.re.contains_zero()
            and exponent.im.contains_zero()
        ):
            result = self._series_moment(exponent, power)
            self._moment_cache[key] = result
            return result

        inverse = exponent.reciprocal()
        plus = self._exp_at_radius(exponent, 1)
        minus = self._exp_at_radius(exponent, -1)
        upper_coefficient = QComplex(self.radius**power)
        lower_coefficient = QComplex((-self.radius) ** power)
        boundary = (
            scale_interval(plus, upper_coefficient)
            - scale_interval(minus, lower_coefficient)
        )
        first = boundary * inverse
        if power == 0:
            result = first
        else:
            recurrence = scale_interval(
                inverse,
                QComplex(Fraction(power)),
            )
            result = (
                first
                - recurrence * self.moment(exponent, power - 1)
            )
        self._moment_cache[key] = result
        return result

    def _raw_exponential_pair(
        self,
        left: AffineExponent,
        right: AffineExponent,
    ) -> CInterval:
        key = (left, right)
        if key in self._raw_pair_cache:
            return self._raw_pair_cache[key]
        left_box = left.enclosure()
        right_box = right.enclosure()
        if _is_exact_zero(right_box):
            prefactor = QComplex(
                Fraction(1, 24) / self.tail_scale
            )
            polynomial_integral = (
                self.moment(left_box, 4)
                - scale_interval(
                    self.moment(left_box, 2),
                    QComplex(2 * self.radius * self.radius),
                )
                + scale_interval(
                    self.moment(left_box, 0),
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
            scale_interval(
                _complex_pow(right_box, 4),
                QComplex(self.tail_scale),
            )
        ).reciprocal()
        minus_boundary = self._exp_at_radius(right_box, -1)
        plus_boundary = self._exp_at_radius(right_box, 1)
        right_times_prefactor = right_box * prefactor
        boundary_rhs = [
            -prefactor * minus_boundary,
            -right_times_prefactor * minus_boundary,
            -prefactor * plus_boundary,
            -right_times_prefactor * plus_boundary,
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
        result = (
            prefactor * self.moment(
                (left + right).enclosure(),
                0,
            )
        )
        for polynomial_power, coefficient in enumerate(
            polynomial_coefficients
        ):
            result = result + coefficient * self.moment(
                left_box,
                polynomial_power,
            )
        self._raw_pair_cache[key] = result
        return result

    def exponential_pair(
        self,
        left: AffineExponent,
        right: AffineExponent,
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
        left: BoxExponentialDensity,
        right: BoxExponentialDensity,
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


def _factorial(value: int) -> int:
    result = 1
    for factor in range(2, value + 1):
        result *= factor
    return result


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
    axis_half_width: Fraction,
    child_alpha: Fraction = Fraction(1),
) -> tuple[
    list[BoxExponentialDensity],
    list[BoxExponentialDensity],
    list[Fraction],
    list[Fraction],
]:
    model = witness["model"]
    count_coefficients = [
        _fraction(row)
        for row in model["count_coefficients"]
    ]
    positive_functions: list[BoxExponentialDensity] = []
    negative_functions: list[BoxExponentialDensity] = []
    positive_weights: list[Fraction] = []
    negative_weights: list[Fraction] = []
    for band_index, (coefficient, support) in enumerate(
        zip(count_coefficients, witness["axis_supports"])
    ):
        for atom_index, atom in enumerate(support):
            x = _fraction(atom["x"])
            weight = _fraction(atom["weight"])
            positive_functions.append(
                axis_box_density(
                    f"axis_b{band_index}_a{atom_index}",
                    x,
                    axis_half_width,
                )
            )
            positive_weights.append(coefficient * weight)
    for atom_index, atom in enumerate(witness["core_support"]):
        x = _fraction(atom["x"])
        y = _fraction(atom["y"])
        weight = _fraction(atom["weight"])
        signed_weight = 2 * child_alpha * weight
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


def build_box_projected_gram(
    witness: dict[str, object],
    axis_half_width: Fraction,
    child_alpha: Fraction = Fraction(1),
) -> BoxProjectedGramResult:
    model = witness["model"]
    radius = _fraction(model["radius"])
    tail_scale = _fraction(
        model["tail_scale_lower_decimal_rational"]
    )
    evaluator = BoxIntervalClampedGreen(radius, tail_scale)
    structural = [structural_constant(), structural_cosh_half()]
    (
        positive_functions,
        negative_functions,
        positive_weights,
        negative_weights,
    ) = functions_from_witness(
        witness,
        axis_half_width,
        child_alpha,
    )
    evaluation_functions = positive_functions + negative_functions

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
    return BoxProjectedGramResult(
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
        moment_series_terms=MOMENT_SERIES_TERMS,
    )
