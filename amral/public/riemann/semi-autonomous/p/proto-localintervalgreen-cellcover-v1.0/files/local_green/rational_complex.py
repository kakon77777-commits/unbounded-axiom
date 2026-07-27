from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .decimal_interval import CInterval, DInterval


@dataclass(frozen=True)
class QComplex:
    re: Fraction
    im: Fraction = Fraction(0)

    @staticmethod
    def zero() -> "QComplex":
        return QComplex(Fraction(0), Fraction(0))

    @staticmethod
    def one() -> "QComplex":
        return QComplex(Fraction(1), Fraction(0))

    def is_zero(self) -> bool:
        return self.re == 0 and self.im == 0

    def conjugate(self) -> "QComplex":
        return QComplex(self.re, -self.im)

    def inverse(self) -> "QComplex":
        denominator = self.re * self.re + self.im * self.im
        if denominator == 0:
            raise ZeroDivisionError("zero rational complex")
        return QComplex(
            self.re / denominator,
            -self.im / denominator,
        )

    def __neg__(self) -> "QComplex":
        return QComplex(-self.re, -self.im)

    def __add__(self, other: "QComplex") -> "QComplex":
        return QComplex(self.re + other.re, self.im + other.im)

    def __sub__(self, other: "QComplex") -> "QComplex":
        return self + (-other)

    def __mul__(self, other: "QComplex") -> "QComplex":
        return QComplex(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    def __truediv__(self, other: "QComplex") -> "QComplex":
        return self * other.inverse()

    def pow_int(self, exponent: int) -> "QComplex":
        if exponent < 0:
            return self.pow_int(-exponent).inverse()
        result = QComplex.one()
        base = self
        power = exponent
        while power:
            if power & 1:
                result = result * base
            power >>= 1
            if power:
                base = base * base
        return result

    def to_interval(self) -> CInterval:
        return CInterval(
            DInterval.from_fraction(self.re),
            DInterval.from_fraction(self.im),
        )


def scale_interval(value: CInterval, scalar: QComplex) -> CInterval:
    return value * scalar.to_interval()

