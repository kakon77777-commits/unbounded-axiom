from __future__ import annotations

import unittest

from bridge.axis import (
    count_profile_rows,
    lower_profile_downward,
    upper_profile_upward,
)
from bridge.semantics import (
    exact_rank_one_operator_counterexample,
    exact_two_point_counterexample,
    semantic_audit,
)


class SemanticTests(unittest.TestCase):
    def test_exact_two_point_counterexample(self) -> None:
        result = exact_two_point_counterexample()
        self.assertTrue(result["upper_envelope_valid"])
        self.assertTrue(result["infimum_minorant_valid"])
        self.assertTrue(result["arbitrary_measure_minorant_false"])

    def test_rank_one_common_floor_is_zero(self) -> None:
        result = exact_rank_one_operator_counterexample()
        self.assertFalse(result["common_nonzero_psd_floor_exists"])

    def test_semantic_audit(self) -> None:
        result = semantic_audit()
        self.assertTrue(result["all_valid_rules_marked_valid"])
        self.assertTrue(result["all_invalid_rules_refuted"])
        self.assertFalse(result["global_rh_certificate"])

    def test_typed_profiles_have_correct_order(self) -> None:
        rows = count_profile_rows()
        lower = lower_profile_downward()
        upper = upper_profile_upward()
        self.assertEqual(len(rows), 5)
        self.assertEqual(len(lower), 5)
        self.assertEqual(len(upper), 5)
        self.assertTrue(
            all(left <= right for left, right in zip(lower, upper))
        )
        self.assertEqual(lower[:3], [0.0, 0.0, 0.0])
        self.assertGreater(lower[3], 5.0)
        self.assertGreater(lower[4], 26.0)
