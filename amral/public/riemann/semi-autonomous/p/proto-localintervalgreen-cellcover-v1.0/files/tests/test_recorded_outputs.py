from __future__ import annotations

import json
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_json(name: str) -> dict:
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


class RecordedOutputTests(unittest.TestCase):
    def test_maximum_certificate_passes_with_safe_flags(self) -> None:
        certificate = read_json(
            "outputs/local_green_cell_certificate_h178e-8.json"
        )
        self.assertTrue(certificate["proof"]["certificate_pass"])
        self.assertGreater(
            Fraction(
                certificate["proof"]["determinant_lower"]
            ),
            0,
        )
        self.assertFalse(
            certificate["classification"][
                "actual_zeta_occupancy_family"
            ]
        )
        self.assertFalse(
            certificate["classification"]["global_rh_certificate"]
        )

    def test_radius_ladder_boundary_classification(self) -> None:
        ladder = read_json(
            "outputs/local_green_radius_ladder.json"
        )
        rows = {row["label"]: row for row in ladder["rows"]}
        self.assertTrue(rows["strongest_tested_pass"]["certificate_pass"])
        self.assertFalse(
            rows["first_tested_boundary_failure"]["certificate_pass"]
        )
        self.assertEqual(
            rows["first_tested_boundary_failure"]["failure_class"],
            "sylvester_lower_bound_failure",
        )
        self.assertEqual(
            Fraction(ladder["certified_uniform_half_width"]),
            Fraction(89, 50_000_000),
        )

    def test_combined_verification_passes(self) -> None:
        verification = read_json("outputs/output_verification.json")
        self.assertTrue(verification["verification_pass"])
        self.assertTrue(all(verification["checks"].values()))
        self.assertFalse(verification["global_rh_certificate"])


if __name__ == "__main__":
    unittest.main()

