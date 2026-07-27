from __future__ import annotations

import unittest
from fractions import Fraction

from occupancy_cert.rational_interval import QInterval


class RationalIntervalTests(unittest.TestCase):
    def test_arithmetic_encloses_all_corners(self) -> None:
        left = QInterval(Fraction(-1, 3), Fraction(2, 5))
        right = QInterval(Fraction(1, 7), Fraction(3, 4))
        product = left * right
        corners = [
            x * y
            for x in (left.lo, left.hi)
            for y in (right.lo, right.hi)
        ]
        self.assertEqual(product.lo, min(corners))
        self.assertEqual(product.hi, max(corners))

    def test_square_crossing_zero(self) -> None:
        value = QInterval(Fraction(-2, 3), Fraction(1, 4)).square()
        self.assertEqual(value.lo, 0)
        self.assertEqual(value.hi, Fraction(4, 9))


if __name__ == "__main__":
    unittest.main()

