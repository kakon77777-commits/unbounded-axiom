from __future__ import annotations

import json
import unittest
from fractions import Fraction
from pathlib import Path

from occupancy_cert.clamped_budget import (
    build_clamped_radius_certificate,
    file_sha256,
    verify_clamped_radius_certificate,
)
from occupancy_cert.rational_interval import as_fraction


ROOT = Path(__file__).resolve().parents[1]


class ClampedBudgetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.witness_path = (
            ROOT / "data" / "parent_v0.7_rational_atomic_witness.json"
        )
        cls.parent_path = (
            ROOT / "data" / "parent_v0.7_interval_atomic_certificate.json"
        )
        cls.witness = json.loads(
            cls.witness_path.read_text(encoding="utf-8")
        )
        cls.parent = json.loads(
            cls.parent_path.read_text(encoding="utf-8")
        )
        cls.witness_hash = file_sha256(cls.witness_path)
        cls.parent_hash = file_sha256(cls.parent_path)

    def test_uniform_radius_certificate(self) -> None:
        result = build_clamped_radius_certificate(
            self.witness,
            self.parent,
            self.witness_hash,
            self.parent_hash,
        )
        self.assertEqual(len(result["location_cells"]), 58)
        self.assertGreater(
            as_fraction(
                result["proof_budget"]["coercivity_lower_bound"]
            ),
            0,
        )
        self.assertTrue(
            verify_clamped_radius_certificate(
                self.witness,
                self.parent,
                result,
                self.witness_hash,
                self.parent_hash,
            )["verification_pass"]
        )

    def test_budget_probe_has_correct_orientation(self) -> None:
        result = build_clamped_radius_certificate(
            self.witness,
            self.parent,
            self.witness_hash,
            self.parent_hash,
        )
        margin = as_fraction(
            result["parameters"]["convex_coercivity_margin"]
        )
        probe = as_fraction(
            result["proof_budget"][
                "failed_budget_probe_perturbation_upper"
            ]
        )
        self.assertGreater(probe, margin)
        self.assertFalse(
            result["proof_budget"][
                "failed_probe_is_operator_counterexample"
            ]
        )
        self.assertEqual(
            as_fraction(
                result["parameters"]["uniform_location_radius"]
            ),
            Fraction(1, 500_000_000_000_000),
        )


if __name__ == "__main__":
    unittest.main()

