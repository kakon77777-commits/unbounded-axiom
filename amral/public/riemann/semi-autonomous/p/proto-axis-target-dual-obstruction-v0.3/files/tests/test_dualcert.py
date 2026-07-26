from __future__ import annotations

import json
import unittest
from fractions import Fraction
from pathlib import Path

import numpy as np

from dualcert.context import TailDualContext, rational_patch_center
from dualcert.cover import default_cover
from dualcert.witness import (
    exact_ldl_positive,
    verify_rational_payload,
    witness_matrix,
)


ROOT = Path(__file__).resolve().parents[1]


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


class DualCertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.context = TailDualContext()
        cls.summary = read_json(
            ROOT / "outputs" / "experiment_summary.json"
        )
        cls.sensitivity = read_json(
            ROOT / "outputs" / "sensitivity.json"
        )
        cls.rational_payload = read_json(
            ROOT / "outputs" / "rational_model.json"
        )

    def test_context_dimension_and_tail_positivity(self) -> None:
        self.assertEqual(self.context.dimension, 22)
        self.assertGreater(
            np.linalg.eigvalsh(self.context.tail_matrix)[0],
            0.03,
        )

    def test_patch_centers_are_exact_rationals_inside_patches(self) -> None:
        for patch in default_cover():
            x, y = rational_patch_center(patch)
            self.assertIsInstance(x, Fraction)
            self.assertIsInstance(y, Fraction)
            self.assertLessEqual(patch.x_min, float(x))
            self.assertGreaterEqual(patch.x_max, float(x))
            self.assertLessEqual(patch.y_min, float(y))
            self.assertGreaterEqual(patch.y_max, float(y))

    def test_primary_float_witnesses_pass_all_patches(self) -> None:
        self.assertEqual(
            self.summary["finite_floating_pass_count"],
            18,
        )
        self.assertGreater(
            self.summary["primary_min_eigenvalue_range"][0],
            3e-5,
        )
        self.assertEqual(self.summary["dual_lower_bound"], 2.0)
        self.assertEqual(self.summary["target_budget"], 1.0)

    def test_primary_witness_recomputes_for_first_patch(self) -> None:
        patch = default_cover()[0]
        x, y = rational_patch_center(patch)
        core = self.context.core_matrix(
            complex(float(x), float(y))
        )
        grid = np.linspace(18.0, 23.0, 26)
        count_floor = (
            np.floor(
                self.context.bands[1].count_majorant * 1e12
            )
            / 1e12
        )
        axis_average = self.context.uniform_axis_average(
            1,
            grid,
            count_coefficient=count_floor,
        )
        witness = witness_matrix(
            self.context.tail_matrix,
            axis_average,
            core,
            alpha=2.0,
            tail_fraction=1e-3,
        )
        self.assertGreater(np.linalg.eigvalsh(witness)[0], 3e-5)

    def test_count_coefficient_is_rounded_down(self) -> None:
        exported = float(
            self.rational_payload["axis_band"][
                "count_coefficient_downward"
            ]
        )
        original = self.rational_payload["axis_band"][
            "original_floating_count_coefficient"
        ]
        self.assertLessEqual(exported, original)
        self.assertGreater(original - exported, 0.0)
        self.assertLess(original - exported, 1e-12)

    def test_exact_rational_ldl_passes(self) -> None:
        result = verify_rational_payload(self.rational_payload)
        self.assertTrue(result["tail_exact_ldl_positive"])
        self.assertTrue(result["all_exact_ldl_positive"])
        self.assertEqual(len(result["patch_rows"]), 18)
        self.assertTrue(
            all(
                row["pivot_count"] == 22
                for row in result["patch_rows"]
            )
        )

    def test_exact_ldl_rejects_indefinite_toy_matrix(self) -> None:
        positive, pivots = exact_ldl_positive(
            [
                [Fraction(1), Fraction(0)],
                [Fraction(0), Fraction(-1)],
            ]
        )
        self.assertFalse(positive)
        self.assertLess(pivots[-1], 0)

    def test_parent_primal_crosscheck_closes_identity(self) -> None:
        crosscheck = self.summary["parent_primal_crosscheck"]
        self.assertTrue(crosscheck["all_pairings_nonnegative"])
        self.assertTrue(crosscheck["all_subobjectives_at_least_2"])
        self.assertLess(
            crosscheck["identity_residual_abs_max"],
            2e-14,
        )

    def test_sensitivity_and_support_transition(self) -> None:
        self.assertTrue(self.sensitivity["primary_witness_stable"])
        self.assertEqual(
            self.sensitivity[
                "first_sampled_radius_with_any_patch_escape"
            ],
            5.1,
        )
        self.assertEqual(
            self.sensitivity[
                "first_sampled_radius_with_stable_all_patch_escape"
            ],
            8.5,
        )
        self.assertTrue(
            all(
                row["pass_count"] == 18
                for row in self.sensitivity[
                    "quadrature_step_rows"
                ]
            )
        )

    def test_claim_boundary_remains_false(self) -> None:
        self.assertFalse(self.summary["known_zero_ordinates_used"])
        self.assertFalse(self.summary["global_rh_certificate"])
        self.assertTrue(
            self.summary[
                "current_r3_patchwise_function_class_rejected"
            ]
        )


if __name__ == "__main__":
    unittest.main()
