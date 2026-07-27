from __future__ import annotations

import json
import unittest
from fractions import Fraction
from pathlib import Path

from occupancy_cert.cover import generate_cover, verify_cover
from occupancy_cert.dirichlet_green import (
    green_point,
    schur_point,
)
from occupancy_cert.semantics import occupancy_semantic_audit


ROOT = Path(__file__).resolve().parents[1]


class OccupancyCoverTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.model = json.loads(
            (
                ROOT / "data" / "synthetic_occupancy_model.json"
            ).read_text(encoding="utf-8")
        )

    def test_green_kernel_values(self) -> None:
        self.assertEqual(
            green_point(Fraction(1, 3), Fraction(2, 3)),
            Fraction(1, 9),
        )
        self.assertEqual(
            green_point(Fraction(1, 5), Fraction(1, 5)),
            Fraction(4, 25),
        )

    def test_count_only_counterexample_is_exact(self) -> None:
        audit = occupancy_semantic_audit(self.model)
        counterexample = audit["count_only_counterexample"]
        self.assertEqual(
            counterexample["exact_point_proof"]["schur_determinant"],
            "-254/558009",
        )
        self.assertEqual(
            counterexample["negative_quadratic_value"],
            "-663194/13755479859",
        )

    def test_adaptive_cover_shape_and_verification(self) -> None:
        certificate = generate_cover(self.model, max_depth=12)
        self.assertFalse(
            certificate["statistics"]["root_box_directly_certified"]
        )
        self.assertEqual(
            certificate["statistics"]["certified_leaf_count"], 8
        )
        self.assertEqual(
            certificate["statistics"]["maximum_leaf_depth"], 7
        )
        self.assertEqual(
            certificate["statistics"]["unresolved_leaf_count"], 0
        )
        self.assertTrue(
            verify_cover(self.model, certificate)["verification_pass"]
        )

    def test_rational_grid_points_are_positive(self) -> None:
        left = [
            Fraction(1, 5)
            + Fraction(index, 10) * Fraction(1, 5)
            for index in range(11)
        ]
        right = [
            Fraction(3, 5)
            + Fraction(index, 10) * Fraction(1, 5)
            for index in range(11)
        ]
        determinants = [
            schur_point([x, y], self.model)["schur_determinant"]
            for x in left
            for y in right
        ]
        self.assertGreater(min(determinants), 0)


if __name__ == "__main__":
    unittest.main()

