from __future__ import annotations

from dataclasses import dataclass
from decimal import (
    Context,
    Decimal,
    ROUND_CEILING,
    ROUND_FLOOR,
    ROUND_HALF_EVEN,
    localcontext,
)
from fractions import Fraction
from typing import Iterable


PRECISION = 90
LOW_CONTEXT = Context(
    prec=PRECISION,
    rounding=ROUND_FLOOR,
    Emin=-999999,
    Emax=999999,
)
HIGH_CONTEXT = Context(
    prec=PRECISION,
    rounding=ROUND_CEILING,
    Emin=-999999,
    Emax=999999,
)
MID_CONTEXT = Context(
    prec=PRECISION,
    rounding=ROUND_HALF_EVEN,
    Emin=-999999,
    Emax=999999,
)


def _low_div(numerator: Decimal, denominator: Decimal) -> Decimal:
    with localcontext(LOW_CONTEXT):
        return numerator / denominator


def _high_div(numerator: Decimal, denominator: Decimal) -> Decimal:
    with localcontext(HIGH_CONTEXT):
        return numerator / denominator


@dataclass(frozen=True)
class DInterval:
    lo: Decimal
    hi: Decimal

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError(f"invalid interval [{self.lo}, {self.hi}]")

    @staticmethod
    def zero() -> "DInterval":
        return DInterval(Decimal(0), Decimal(0))

    @staticmethod
    def one() -> "DInterval":
        return DInterval(Decimal(1), Decimal(1))

    @staticmethod
    def from_int(value: int) -> "DInterval":
        point = Decimal(value)
        return DInterval(point, point)

    @staticmethod
    def from_decimal(value: Decimal | str | int) -> "DInterval":
        point = value if isinstance(value, Decimal) else Decimal(value)
        return DInterval(point, point)

    @staticmethod
    def from_fraction(value: Fraction) -> "DInterval":
        numerator = Decimal(value.numerator)
        denominator = Decimal(value.denominator)
        return DInterval(
            _low_div(numerator, denominator),
            _high_div(numerator, denominator),
        )

    @staticmethod
    def from_json(row: dict[str, str]) -> "DInterval":
        return DInterval(Decimal(row["lo"]), Decimal(row["hi"]))

    def to_json(self) -> dict[str, str]:
        return {"lo": str(self.lo), "hi": str(self.hi)}

    def midpoint(self) -> Decimal:
        with localcontext(MID_CONTEXT):
            return (self.lo + self.hi) / Decimal(2)

    def width(self) -> Decimal:
        with localcontext(HIGH_CONTEXT):
            return self.hi - self.lo

    def radius_upper(self) -> Decimal:
        with localcontext(HIGH_CONTEXT):
            return (self.hi - self.lo) / Decimal(2)

    def abs_upper(self) -> Decimal:
        return max(self.lo.copy_abs(), self.hi.copy_abs())

    def contains_zero(self) -> bool:
        return self.lo <= 0 <= self.hi

    def intersect(self, other: "DInterval") -> "DInterval":
        lower = max(self.lo, other.lo)
        upper = min(self.hi, other.hi)
        if lower > upper:
            raise ArithmeticError(
                f"disjoint rigorous intervals: {self} and {other}"
            )
        return DInterval(lower, upper)

    def widen(self, radius: Decimal) -> "DInterval":
        if radius < 0:
            raise ValueError("radius must be nonnegative")
        with localcontext(LOW_CONTEXT):
            lower = self.lo - radius
        with localcontext(HIGH_CONTEXT):
            upper = self.hi + radius
        return DInterval(lower, upper)

    def __neg__(self) -> "DInterval":
        return DInterval(
            self.hi.copy_negate(),
            self.lo.copy_negate(),
        )

    def __add__(self, other: "DInterval") -> "DInterval":
        with localcontext(LOW_CONTEXT):
            lower = self.lo + other.lo
        with localcontext(HIGH_CONTEXT):
            upper = self.hi + other.hi
        return DInterval(lower, upper)

    def __sub__(self, other: "DInterval") -> "DInterval":
        return self + (-other)

    def __mul__(self, other: "DInterval") -> "DInterval":
        with localcontext(LOW_CONTEXT):
            lower_candidates = (
                self.lo * other.lo,
                self.lo * other.hi,
                self.hi * other.lo,
                self.hi * other.hi,
            )
            lower = min(lower_candidates)
        with localcontext(HIGH_CONTEXT):
            upper_candidates = (
                self.lo * other.lo,
                self.lo * other.hi,
                self.hi * other.lo,
                self.hi * other.hi,
            )
            upper = max(upper_candidates)
        return DInterval(lower, upper)

    def square(self) -> "DInterval":
        with localcontext(HIGH_CONTEXT):
            upper = max(self.lo * self.lo, self.hi * self.hi)
        if self.contains_zero():
            lower = Decimal(0)
        else:
            with localcontext(LOW_CONTEXT):
                lower = min(self.lo * self.lo, self.hi * self.hi)
        return DInterval(lower, upper)

    def reciprocal(self) -> "DInterval":
        if self.contains_zero():
            raise ZeroDivisionError(f"interval contains zero: {self}")
        with localcontext(LOW_CONTEXT):
            lower = Decimal(1) / self.hi
        with localcontext(HIGH_CONTEXT):
            upper = Decimal(1) / self.lo
        return DInterval(lower, upper)

    def __truediv__(self, other: "DInterval") -> "DInterval":
        return self * other.reciprocal()

    def pow_int(self, exponent: int) -> "DInterval":
        if exponent < 0:
            return self.pow_int(-exponent).reciprocal()
        result = DInterval.one()
        base = self
        power = exponent
        while power:
            if power & 1:
                result = result * base
            power >>= 1
            if power:
                base = base.square()
        return result


@dataclass(frozen=True)
class CInterval:
    re: DInterval
    im: DInterval

    @staticmethod
    def zero() -> "CInterval":
        return CInterval(DInterval.zero(), DInterval.zero())

    @staticmethod
    def one() -> "CInterval":
        return CInterval(DInterval.one(), DInterval.zero())

    def intersect(self, other: "CInterval") -> "CInterval":
        return CInterval(
            self.re.intersect(other.re),
            self.im.intersect(other.im),
        )

    def conjugate(self) -> "CInterval":
        return CInterval(self.re, -self.im)

    def __neg__(self) -> "CInterval":
        return CInterval(-self.re, -self.im)

    def __add__(self, other: "CInterval") -> "CInterval":
        return CInterval(self.re + other.re, self.im + other.im)

    def __sub__(self, other: "CInterval") -> "CInterval":
        return self + (-other)

    def __mul__(self, other: "CInterval") -> "CInterval":
        return CInterval(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    def reciprocal(self) -> "CInterval":
        denominator = self.re.square() + self.im.square()
        inverse = denominator.reciprocal()
        conjugate = self.conjugate()
        return CInterval(
            conjugate.re * inverse,
            conjugate.im * inverse,
        )

    def __truediv__(self, other: "CInterval") -> "CInterval":
        return self * other.reciprocal()


def interval_sum(values: Iterable[DInterval]) -> DInterval:
    total = DInterval.zero()
    for value in values:
        total = total + value
    return total


def complex_interval_sum(values: Iterable[CInterval]) -> CInterval:
    total = CInterval.zero()
    for value in values:
        total = total + value
    return total


def decimal_add_upper(left: Decimal, right: Decimal) -> Decimal:
    with localcontext(HIGH_CONTEXT):
        return left + right


def decimal_div_upper(left: Decimal, right: Decimal) -> Decimal:
    with localcontext(HIGH_CONTEXT):
        return left / right


def decimal_mul_upper(left: Decimal, right: Decimal) -> Decimal:
    with localcontext(HIGH_CONTEXT):
        return left * right


def decimal_sub_lower(left: Decimal, right: Decimal) -> Decimal:
    with localcontext(LOW_CONTEXT):
        return left - right
