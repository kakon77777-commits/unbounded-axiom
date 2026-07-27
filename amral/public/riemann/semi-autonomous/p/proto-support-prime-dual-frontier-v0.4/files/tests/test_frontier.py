from __future__ import annotations

import json
import math
import unittest
from pathlib import Path

import numpy as np

from frontier.axis import PUBLISHED_S_BOUND, default_axis_bands
from frontier.context import FrontierContext
from frontier.cover import coverage_audit, default_cover, refined_cover
from frontier.dual import (
    generalized_negative_threshold,
    rank_two_point_thresholds,
)
from frontier.primecost import (
    segmented_prime_log_histogram,
    strict_prime_power_cutoff,
)
from verify_saved_witnesses import verify_all_saved_witnesses


ROOT = Path(__file__).resolve().parents[1]


def read_json(relative: str) -> object:
    return json.loads(
        (ROOT / relative).read_text(encoding="utf-8")
    )


class FrontierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.uniform = read_json("outputs/uniform_frontier.json")
        cls.joint = read_json("outputs/joint_dual_summary.json")
        cls.refinement = read_json("outputs/axis_refinement.json")
        cls.prime = read_json("outputs/prime_cost.json")
        cls.source = read_json("outputs/source_profile.json")

    def test_published_source_constants_are_used(self) -> None:
        self.assertEqual(PUBLISHED_S_BOUND["log_coefficient"], 0.112)
        self.assertEqual(PUBLISHED_S_BOUND["loglog_coefficient"], 0.278)
        self.assertEqual(PUBLISHED_S_BOUND["constant"], 2.510)
        counts = [band.count_majorant for band in default_axis_bands()]
        stored = [
            row["published_profile"]
            for row in self.source["band_rows"]
        ]
        np.testing.assert_allclose(counts, stored, rtol=0.0, atol=1e-12)

    def test_cover_and_refinement_are_complete(self) -> None:
        original = default_cover()
        refined = refined_cover(original, 4, 4)
        self.assertEqual(len(original), 18)
        self.assertEqual(len(refined), 288)
        self.assertTrue(coverage_audit(original)["cover_pass"])
        self.assertTrue(coverage_audit(refined)["cover_pass"])

    def test_context_dimension_tracks_two_structural_constraints(self) -> None:
        context = FrontierContext(radius=3.0)
        self.assertEqual(context.count, 30)
        self.assertEqual(context.dimension, 28)
        self.assertGreater(
            np.linalg.eigvalsh(context.tail_matrix)[0],
            0.0,
        )

    def test_rank_two_threshold_matches_generalized_eigensolve(self) -> None:
        context = FrontierContext(radius=3.0)
        base, _ = context.base_matrix((0, 1, 2, 3, 4), 0.25)
        points = np.asarray(
            [20.1 - 0.18j, 20.25 - 0.15j, 20.4 - 0.11j]
        )
        transforms = context.transform(points)
        fast = rank_two_point_thresholds(transforms, base)
        direct = np.asarray(
            [
                generalized_negative_threshold(matrix, base)
                for matrix in context.core_matrices(points)
            ]
        )
        np.testing.assert_allclose(fast, direct, rtol=2e-10, atol=1e-10)

    def test_uniform_frontier_has_all_126_configurations(self) -> None:
        self.assertEqual(self.uniform["row_count"], 126)
        self.assertEqual(
            self.uniform[
                "first_sampled_any_geometry_center_escape"
            ]["radius"],
            10.0,
        )
        self.assertEqual(
            self.uniform[
                "first_sampled_any_geometry_uniform_patch_escape"
            ]["radius"],
            14.0,
        )

    def test_axis_refinement_exposes_coarse_false_escape(self) -> None:
        rows = self.refinement["rows"]
        self.assertTrue(self.refinement["coarse_grid_false_escape"])
        self.assertLess(rows[0]["alpha"], 1.0)
        self.assertGreater(rows[-1]["safe_alpha"], 1.09)
        self.assertGreater(rows[-1]["safe_min_eigenvalue"], 0.11)

    def test_each_sampled_radius_has_a_safe_dual_block(self) -> None:
        self.assertEqual(
            [row["radius"] for row in self.joint["radius_rows"]],
            [10.25, 12.0, 14.0, 16.0],
        )
        for row in self.joint["radius_rows"]:
            self.assertTrue(row["at_least_one_searched_patch_blocked"])
            self.assertGreater(
                row["strongest_searched_safe_alpha"],
                1.0,
            )
        self.assertFalse(
            self.joint["full_refined_cover_joint_gate_pass"]
        )

    def test_serialized_witnesses_reconstruct_and_block(self) -> None:
        verification = verify_all_saved_witnesses()
        self.assertTrue(verification["path_sets_match"])
        self.assertEqual(verification["expected_witness_count"], 12)
        self.assertTrue(
            verification["all_serialized_sparse_witnesses_psd"]
        )
        self.assertTrue(
            verification["all_serialized_measures_block_budget"]
        )
        self.assertLess(
            verification[
                "maximum_minimum_eigenvalue_abs_difference"
            ],
            1e-8,
        )

    def test_prime_support_cutoff_and_small_exact_count(self) -> None:
        self.assertEqual(strict_prime_power_cutoff(3.0), 403)
        result = segmented_prime_log_histogram(
            3.0,
            bin_width=0.01,
            segment_size=200,
        )
        self.assertEqual(result.prime_count, 79)
        self.assertEqual(result.prime_power_term_count, 98)
        benchmark = {
            row["radius"]: row
            for row in self.prime["benchmark_rows"]
        }
        self.assertEqual(benchmark[10.25]["cutoff"], 799902177)
        self.assertEqual(benchmark[10.25]["prime_count"], 41141456)

    def test_no_global_rh_claim(self) -> None:
        for payload in (
            self.uniform,
            self.joint,
            self.refinement,
            self.prime,
            self.source,
        ):
            self.assertFalse(payload["global_rh_certificate"])
        self.assertTrue(
            math.isclose(
                self.source["source_aligned_tail_multiplier"],
                9.935682232184019e-7,
                rel_tol=1e-12,
            )
        )


if __name__ == "__main__":
    unittest.main()
