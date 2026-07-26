from __future__ import annotations

import json
import unittest
from pathlib import Path

import numpy as np

from psdgram.axis import default_axis_bands
from psdgram.cover import coverage_audit, default_cover
from psdgram.solver import (
    factor_from_gram,
    matrix_grad,
    matrix_value,
    matrix_values,
    solve_diagonal_stage_one,
)


ROOT = Path(__file__).resolve().parents[1]


def load_output(name: str) -> object:
    return json.loads(
        (ROOT / "outputs" / name).read_text(encoding="utf-8")
    )


class PSDGramTests(unittest.TestCase):
    def test_adaptive_cover_is_exact_on_rational_cells(self) -> None:
        patches = default_cover()
        audit = coverage_audit(patches)
        self.assertEqual(len(patches), 18)
        self.assertTrue(audit["cover_pass"])
        self.assertEqual(audit["rational_uncovered_probes"], [])
        self.assertEqual(audit["dense_grid_uncovered_count"], 0)

    def test_axis_bands_partition_prefix_and_have_positive_counts(
        self,
    ) -> None:
        bands = default_axis_bands()
        self.assertEqual(
            [band.start for band in bands],
            [14.0, 18.0, 23.0, 35.0, 70.0],
        )
        self.assertEqual(
            [band.stop for band in bands],
            [18.0, 23.0, 35.0, 70.0, 145.0],
        )
        self.assertTrue(
            all(band.count_majorant > 0.0 for band in bands)
        )
        self.assertTrue(
            all(
                left.stop == right.start
                for left, right in zip(bands[:-1], bands[1:])
            )
        )

    def test_matrix_gradient_matches_centered_difference(self) -> None:
        rng = np.random.default_rng(20260724)
        raw = rng.normal(size=(4, 4))
        matrix = 0.5 * (raw + raw.T)
        factor = rng.normal(size=(4, 3))
        direction = rng.normal(size=(4, 3))
        epsilon = 1e-6
        finite_difference = (
            matrix_value(matrix, factor + epsilon * direction)
            - matrix_value(matrix, factor - epsilon * direction)
        ) / (2.0 * epsilon)
        analytic = float(
            np.sum(matrix_grad(matrix, factor) * direction)
        )
        self.assertTrue(
            np.isclose(
                finite_difference,
                analytic,
                rtol=2e-8,
                atol=2e-8,
            )
        )

    def test_factor_from_gram_is_psd_and_normalized(self) -> None:
        gram = np.diag([4.0, 1.0, 0.0])
        core_matrices = np.asarray(
            [-np.eye(3), -0.5 * np.eye(3)]
        )
        factor = factor_from_gram(
            gram,
            rank=2,
            core_matrices=core_matrices,
        )
        reconstructed = factor @ factor.T
        self.assertGreaterEqual(
            np.linalg.eigvalsh(reconstructed).min(),
            -1e-13,
        )
        self.assertEqual(factor.shape, (3, 2))
        self.assertLessEqual(
            np.max(matrix_values(core_matrices, factor)),
            -1.001,
        )

    def test_diagonal_lp_satisfies_toy_constraints(self) -> None:
        core = np.asarray([[-2.0, -1.0], [-1.0, -3.0]])
        arithmetic = np.asarray([1.0, 1.0])
        objective = np.asarray([2.0, 1.0])
        result = solve_diagonal_stage_one(
            core,
            arithmetic,
            objective,
            arithmetic_floor=0.5,
        )
        self.assertTrue(result.success)
        self.assertGreaterEqual(np.min(result.x), -1e-12)
        self.assertLessEqual(np.max(core @ result.x), -1.0 + 1e-9)
        self.assertGreaterEqual(
            arithmetic @ result.x,
            0.5 - 1e-9,
        )

    def test_full_gram_outputs_are_psd_and_core_negative(self) -> None:
        results = load_output("gram_results.json")
        self.assertEqual(len(results), 18)
        for result in results:
            gram = np.asarray(result["gram"], dtype=float)
            self.assertGreaterEqual(
                np.linalg.eigvalsh(0.5 * (gram + gram.T)).min(),
                -2e-12,
            )
            self.assertLess(result["dense_core_max"], 0.0)
            self.assertTrue(
                result["lipschitz_audit"][
                    "core_refined_continuous_sign_pass"
                ]
            )
            self.assertFalse(result["global_certificate_pass"])

    def test_axis_charges_and_majorants_recompute(self) -> None:
        results = load_output("gram_results.json")
        for result in results:
            charges = []
            for band in result["axis_bands"]:
                charge = (
                    band["count_majorant"]
                    * band["sampled_supremum"]
                )
                self.assertTrue(
                    np.isclose(
                        charge,
                        band["sampled_charge"],
                        rtol=2e-13,
                        atol=2e-13,
                    )
                )
                charges.append(charge)
            recomputed = result["tail_majorant"] + sum(charges)
            self.assertTrue(
                np.isclose(
                    recomputed,
                    result["sampled_axis_plus_tail_majorant"],
                    rtol=2e-13,
                    atol=2e-13,
                )
            )

    def test_rank_sweeps_collapse_to_rank_one(self) -> None:
        results = load_output("rank_study.json")
        self.assertEqual(len(results), 16)
        self.assertEqual(
            {result["requested_rank"] for result in results},
            {1, 2, 4, 8},
        )
        self.assertEqual(
            {result["numerical_rank"] for result in results},
            {1},
        )

    def test_summary_keeps_claim_boundary_explicit(self) -> None:
        summary = load_output("experiment_summary.json")
        self.assertFalse(
            summary["known_zero_ordinates_used_in_optimization"]
        )
        self.assertTrue(
            summary["known_zero_ordinates_used_as_holdout_only"]
        )
        self.assertFalse(summary["global_certificate_pass"])
        self.assertTrue(
            summary["all_core_refined_continuous_sign_pass"]
        )
        self.assertFalse(
            summary["all_core_crude_continuous_sign_pass"]
        )
        self.assertIn("No convex SDP solver", summary["solver_boundary"])


if __name__ == "__main__":
    unittest.main()
