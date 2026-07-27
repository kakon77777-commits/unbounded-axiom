from __future__ import annotations

import unittest
from decimal import Decimal
from fractions import Fraction

from local_green.box_green import (
    AffineExponent,
    BoxIntervalClampedGreen,
)
from local_green.decimal_interval import CInterval, DInterval
from local_green.rational_complex import QComplex
from local_green.transcendental import (
    exp_interval,
    exp_rational,
    sin_cos_interval,
)


class IntervalEngineTests(unittest.TestCase):
    def test_trigonometric_origin(self) -> None:
        sine, cosine = sin_cos_interval(DInterval.zero())
        self.assertLessEqual(sine.lo, 0)
        self.assertGreaterEqual(sine.hi, 0)
        self.assertLessEqual(cosine.lo, 1)
        self.assertGreaterEqual(cosine.hi, 1)

    def test_exponential_box_contains_endpoint_enclosures(self) -> None:
        box = DInterval(Decimal("-0.01"), Decimal("0.02"))
        enclosure = exp_interval(box)
        lower = exp_rational(Fraction(-1, 100))
        upper = exp_rational(Fraction(1, 50))
        self.assertLessEqual(enclosure.lo, lower.lo)
        self.assertGreaterEqual(enclosure.hi, upper.hi)

    def test_shared_affine_variable_cancels_exactly(self) -> None:
        positive = AffineExponent(
            QComplex(Fraction(0), Fraction(14)),
            (
                (
                    "x",
                    QComplex(Fraction(0), Fraction(1)),
                    Fraction(1, 1000),
                ),
            ),
        )
        total = positive + (-positive)
        self.assertEqual(total, AffineExponent.point(QComplex.zero()))
        self.assertEqual(total.enclosure(), CInterval.zero())

    def test_zero_crossing_moment_contains_exact_zero_value(self) -> None:
        evaluator = BoxIntervalClampedGreen(
            Fraction(16),
            Fraction(31794183142988, 10**18),
        )
        epsilon = DInterval(
            Decimal("-0.000001"),
            Decimal("0.000001"),
        )
        value = evaluator.moment(
            CInterval(DInterval.zero(), epsilon),
            0,
        )
        self.assertLessEqual(value.re.lo, 32)
        self.assertGreaterEqual(value.re.hi, 32)
        self.assertTrue(value.im.contains_zero())


if __name__ == "__main__":
    unittest.main()

