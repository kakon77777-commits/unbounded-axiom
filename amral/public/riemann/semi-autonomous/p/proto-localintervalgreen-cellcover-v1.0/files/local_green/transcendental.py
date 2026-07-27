from __future__ import annotations

import functools
import math
from decimal import Decimal, ROUND_HALF_EVEN, localcontext
from fractions import Fraction

from .decimal_interval import (
    CInterval,
    DInterval,
    HIGH_CONTEXT,
    MID_CONTEXT,
)
from .rational_complex import QComplex


ATAN5_TERMS = 96
ATAN239_TERMS = 40
TRIG_TERMS = 44
EXP_TERMS = 48


def _atan_unit_fraction_bounds(
    denominator: int,
    terms: int,
) -> tuple[Fraction, Fraction]:
    partial = Fraction(0)
    for index in range(terms):
        term = Fraction(
            1,
            (2 * index + 1) * denominator ** (2 * index + 1),
        )
        partial += term if index % 2 == 0 else -term
    next_term = Fraction(
        1,
        (2 * terms + 1) * denominator ** (2 * terms + 1),
    )
    if terms % 2 == 0:
        return partial, partial + next_term
    return partial - next_term, partial


@functools.lru_cache(maxsize=1)
def pi_fraction_bounds() -> tuple[Fraction, Fraction]:
    atan5_lo, atan5_hi = _atan_unit_fraction_bounds(
        5,
        ATAN5_TERMS,
    )
    atan239_lo, atan239_hi = _atan_unit_fraction_bounds(
        239,
        ATAN239_TERMS,
    )
    lower = 16 * atan5_lo - 4 * atan239_hi
    upper = 16 * atan5_hi - 4 * atan239_lo
    return lower, upper


@functools.lru_cache(maxsize=1)
def pi_interval() -> DInterval:
    lower, upper = pi_fraction_bounds()
    lower_decimal = DInterval.from_fraction(lower).lo
    upper_decimal = DInterval.from_fraction(upper).hi
    return DInterval(lower_decimal, upper_decimal)


def _taylor_sin_cos(reduced: DInterval) -> tuple[DInterval, DInterval]:
    square = reduced * reduced
    sin_sum = DInterval.zero()
    cos_sum = DInterval.zero()
    sin_power = reduced
    cos_power = DInterval.one()
    sin_factorial = 1
    cos_factorial = 1
    for index in range(TRIG_TERMS):
        sin_term = sin_power / DInterval.from_int(sin_factorial)
        cos_term = cos_power / DInterval.from_int(cos_factorial)
        if index % 2:
            sin_sum = sin_sum - sin_term
            cos_sum = cos_sum - cos_term
        else:
            sin_sum = sin_sum + sin_term
            cos_sum = cos_sum + cos_term
        sin_power = sin_power * square
        cos_power = cos_power * square
        sin_factorial *= (2 * index + 2) * (2 * index + 3)
        cos_factorial *= (2 * index + 1) * (2 * index + 2)

    magnitude = reduced.abs_upper()
    with localcontext(HIGH_CONTEXT):
        sin_error = (
            magnitude ** (2 * TRIG_TERMS + 1)
            / Decimal(math.factorial(2 * TRIG_TERMS + 1))
        )
        cos_error = (
            magnitude ** (2 * TRIG_TERMS)
            / Decimal(math.factorial(2 * TRIG_TERMS))
        )
    return sin_sum.widen(sin_error), cos_sum.widen(cos_error)


@functools.lru_cache(maxsize=None)
def sin_cos_rational(angle: Fraction) -> tuple[DInterval, DInterval]:
    return sin_cos_interval(DInterval.from_fraction(angle))


@functools.lru_cache(maxsize=None)
def sin_cos_interval(
    angle_interval: DInterval,
) -> tuple[DInterval, DInterval]:
    """Directed enclosure of sine and cosine on a narrow real interval.

    The range-reduction quadrant is selected from the interval midpoint, but
    the subtraction itself uses the rigorous Machin enclosure of pi.  A cell
    that straddles a range-reduction boundary is therefore harmless as long
    as the resulting reduced interval remains inside the Taylor guard.
    """
    pi = pi_interval()
    half_pi = pi * DInterval.from_fraction(Fraction(1, 2))
    with localcontext(MID_CONTEXT):
        quotient = angle_interval.midpoint() / half_pi.midpoint()
        quadrant = int(
            quotient.to_integral_value(rounding=ROUND_HALF_EVEN)
        )
    reduced = (
        angle_interval
        - half_pi * DInterval.from_int(quadrant)
    )
    if reduced.abs_upper() >= Decimal("0.85"):
        raise ArithmeticError(
            f"unstable trigonometric range reduction: {reduced}"
        )
    sin_reduced, cos_reduced = _taylor_sin_cos(reduced)
    residue = quadrant % 4
    if residue == 0:
        return sin_reduced, cos_reduced
    if residue == 1:
        return cos_reduced, -sin_reduced
    if residue == 2:
        return -sin_reduced, -cos_reduced
    return -cos_reduced, sin_reduced


@functools.lru_cache(maxsize=None)
def exp_rational(value: Fraction) -> DInterval:
    return exp_interval(DInterval.from_fraction(value))


@functools.lru_cache(maxsize=None)
def exp_interval(source: DInterval) -> DInterval:
    """Directed enclosure of exp on a real interval."""
    magnitude = source.abs_upper()
    scale_power = 0
    threshold = Decimal(1) / Decimal(16)
    while magnitude > threshold:
        scale_power += 1
        magnitude /= Decimal(2)
    divisor = 2**scale_power
    reduced = source / DInterval.from_int(divisor)
    total = DInterval.one()
    term = DInterval.one()
    for index in range(1, EXP_TERMS + 1):
        term = (
            term
            * reduced
            / DInterval.from_int(index)
        )
        total = total + term
    reduced_magnitude = reduced.abs_upper()
    with localcontext(HIGH_CONTEXT):
        error = (
            Decimal(2)
            * reduced_magnitude ** (EXP_TERMS + 1)
            / Decimal(math.factorial(EXP_TERMS + 1))
        )
    result = total.widen(error)
    for _ in range(scale_power):
        result = result.square()
    if result.lo <= 0:
        raise ArithmeticError("exponential enclosure lost positivity")
    return result


@functools.lru_cache(maxsize=None)
def complex_exp_rational(value: QComplex) -> CInterval:
    magnitude = exp_rational(value.re)
    sine, cosine = sin_cos_rational(value.im)
    return CInterval(magnitude * cosine, magnitude * sine)


@functools.lru_cache(maxsize=None)
def complex_exp_interval(value: CInterval) -> CInterval:
    """Rectangular directed enclosure of the complex exponential."""
    magnitude = exp_interval(value.re)
    sine, cosine = sin_cos_interval(value.im)
    return CInterval(magnitude * cosine, magnitude * sine)


def transcendental_audit() -> dict[str, object]:
    pi = pi_interval()
    return {
        "decimal_precision": 90,
        "pi_interval": pi.to_json(),
        "pi_interval_width": str(pi.width()),
        "machin_formula": "pi = 16*atan(1/5) - 4*atan(1/239)",
        "atan_1_over_5_terms": ATAN5_TERMS,
        "atan_1_over_239_terms": ATAN239_TERMS,
        "trigonometric_taylor_terms": TRIG_TERMS,
        "exponential_taylor_terms": EXP_TERMS,
        "directed_rounding": "decimal ROUND_FLOOR / ROUND_CEILING",
    }
