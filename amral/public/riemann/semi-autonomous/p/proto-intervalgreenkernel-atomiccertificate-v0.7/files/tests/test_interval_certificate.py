from __future__ import annotations

import copy
import json
import unittest
from decimal import Decimal
from fractions import Fraction
from pathlib import Path

from interval_cert.certificate import (
    _neumann_and_sylvester,
    _projected_hash,
    canonical_json_hash,
)
from interval_cert.green import (
    IntervalClampedGreen,
    build_projected_gram,
    structural_constant,
)
from interval_cert.transcendental import (
    exp_rational,
    pi_interval,
    sin_cos_rational,
)


ROOT = Path(__file__).resolve().parents[1]


class ElementaryIntervalTests(unittest.TestCase):
    def test_pi_encloses_reference_decimal(self) -> None:
        pi = pi_interval()
        reference = Decimal(
            "3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825"
        )
        self.assertLessEqual(pi.lo, reference)
        self.assertGreaterEqual(pi.hi, reference)

    def test_trigonometric_identity_contains_one(self) -> None:
        sine, cosine = sin_cos_rational(Fraction(1624, 5))
        identity = sine.square() + cosine.square()
        self.assertLessEqual(identity.lo, Decimal(1))
        self.assertGreaterEqual(identity.hi, Decimal(1))

    def test_exponential_reciprocity_contains_one(self) -> None:
        positive = exp_rational(Fraction(8, 5))
        negative = exp_rational(Fraction(-8, 5))
        product = positive * negative
        self.assertLessEqual(product.lo, Decimal(1))
        self.assertGreaterEqual(product.hi, Decimal(1))

    def test_constant_green_pair_contains_closed_form(self) -> None:
        radius = Fraction(16)
        tail_scale = Fraction(31794183142988, 10**18)
        evaluator = IntervalClampedGreen(radius, tail_scale)
        value = evaluator.density_pair(
            structural_constant(),
            structural_constant(),
        )
        exact = Fraction(2, 45) * radius**5 / tail_scale
        enclosure = type(value).from_fraction(exact)
        self.assertLessEqual(value.lo, enclosure.hi)
        self.assertGreaterEqual(value.hi, enclosure.lo)


class FullCertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.witness = json.loads(
            (
                ROOT
                / "data"
                / "rational_atomic_witness_v0.6.json"
            ).read_text(encoding="utf-8")
        )
        cls.certificate = json.loads(
            (
                ROOT
                / "outputs"
                / "interval_atomic_certificate.json"
            ).read_text(encoding="utf-8")
        )
        cls.gram = build_projected_gram(cls.witness)

    def test_witness_hash_matches(self) -> None:
        self.assertEqual(
            self.certificate["input"][
                "canonical_witness_sha256"
            ],
            canonical_json_hash(self.witness),
        )

    def test_projected_gram_hash_matches(self) -> None:
        self.assertEqual(
            self.certificate["green_kernel"][
                "projected_gram_sha256"
            ],
            _projected_hash(self.gram.projected_gram),
        )

    def test_full_neumann_sylvester_reproduction(self) -> None:
        candidate = self.certificate["neumann_candidate"]
        proof = _neumann_and_sylvester(
            self.gram,
            candidate["inverse_decimal_rational"],
            candidate["solution_decimal_rational"],
        )
        self.assertEqual(proof, self.certificate["proof"])
        self.assertTrue(proof["sylvester_positive_definite"])

    def test_zero_inverse_failure_injection_is_rejected(self) -> None:
        candidate = copy.deepcopy(
            self.certificate["neumann_candidate"]
        )
        size = len(candidate["inverse_decimal_rational"])
        candidate["inverse_decimal_rational"] = [
            ["0" for _ in range(size)]
            for _ in range(size)
        ]
        with self.assertRaises(ArithmeticError):
            _neumann_and_sylvester(
                self.gram,
                candidate["inverse_decimal_rational"],
                candidate["solution_decimal_rational"],
            )

    def test_trust_boundary_flags(self) -> None:
        classification = self.certificate["classification"]
        self.assertTrue(
            classification[
                "abstract_continuous_interval_certificate"
            ]
        )
        self.assertFalse(
            classification[
                "zeta_facing_tail_theorem_certified"
            ]
        )
        self.assertFalse(
            classification[
                "zeta_facing_count_coefficients_certified"
            ]
        )
        self.assertFalse(
            classification[
                "explicit_formula_admissibility_certified"
            ]
        )
        self.assertFalse(classification["global_rh_certificate"])

    def test_coefficient_orientation_blocker_is_preserved(self) -> None:
        audit = json.loads(
            (
                ROOT
                / "outputs"
                / "coefficient_orientation_audit.json"
            ).read_text(encoding="utf-8")
        )
        self.assertTrue(audit["orientation_blocker_confirmed"])
        self.assertFalse(
            audit["all_stored_coefficients_are_lower_certificates"]
        )
        self.assertFalse(audit["global_rh_certificate"])


if __name__ == "__main__":
    unittest.main()
