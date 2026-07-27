from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Any, Iterable


def as_fraction(value: Any) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    if isinstance(value, dict):
        return Fraction(
            int(value["numerator"]),
            int(value["denominator"]),
        )
    raise TypeError(f"cannot convert {type(value).__name__} to Fraction")


def fraction_text(value: Fraction) -> str:
    value = as_fraction(value)
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def fraction_json(value: Fraction) -> dict[str, int]:
    value = as_fraction(value)
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
    }


@dataclass(frozen=True)
class QInterval:
    lo: Fraction
    hi: Fraction

    def __post_init__(self) -> None:
        object.__setattr__(self, "lo", as_fraction(self.lo))
        object.__setattr__(self, "hi", as_fraction(self.hi))
        if self.lo > self.hi:
            raise ValueError(f"invalid interval [{self.lo}, {self.hi}]")

    @classmethod
    def point(cls, value: Any) -> "QInterval":
        value = as_fraction(value)
        return cls(value, value)

    @classmethod
    def from_json(cls, value: dict[str, str]) -> "QInterval":
        return cls(as_fraction(value["lo"]), as_fraction(value["hi"]))

    def to_json(self) -> dict[str, str]:
        return {
            "lo": fraction_text(self.lo),
            "hi": fraction_text(self.hi),
        }

    @property
    def width(self) -> Fraction:
        return self.hi - self.lo

    @property
    def midpoint(self) -> Fraction:
        return (self.lo + self.hi) / 2

    def __add__(self, other: Any) -> "QInterval":
        other = interval(other)
        return QInterval(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self) -> "QInterval":
        return QInterval(-self.hi, -self.lo)

    def __sub__(self, other: Any) -> "QInterval":
        return self + (-interval(other))

    def __rsub__(self, other: Any) -> "QInterval":
        return interval(other) - self

    def __mul__(self, other: Any) -> "QInterval":
        other = interval(other)
        products = (
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        )
        return QInterval(min(products), max(products))

    __rmul__ = __mul__

    def reciprocal(self) -> "QInterval":
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError(
                f"interval contains zero: [{self.lo}, {self.hi}]"
            )
        return QInterval(1 / self.hi, 1 / self.lo)

    def __truediv__(self, other: Any) -> "QInterval":
        return self * interval(other).reciprocal()

    def square(self) -> "QInterval":
        if self.lo <= 0 <= self.hi:
            return QInterval(0, max(self.lo * self.lo, self.hi * self.hi))
        values = (self.lo * self.lo, self.hi * self.hi)
        return QInterval(min(values), max(values))

    def hull(self, other: Any) -> "QInterval":
        other = interval(other)
        return QInterval(min(self.lo, other.lo), max(self.hi, other.hi))

    def contains(self, value: Any) -> bool:
        value = as_fraction(value)
        return self.lo <= value <= self.hi


def interval(value: Any) -> QInterval:
    if isinstance(value, QInterval):
        return value
    return QInterval.point(value)


def interval_sum(values: Iterable[QInterval]) -> QInterval:
    total = QInterval.point(0)
    for value in values:
        total = total + value
    return total

