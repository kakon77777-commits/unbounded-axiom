from __future__ import annotations

import json
import unittest
from pathlib import Path

import numpy as np

from notch.codes import resolve_codes
from notch.context import FrontierContext
from notch.model import spectral_slope_basis


ROOT = Path(__file__).resolve().parents[1]


def read_output(name: str) -> dict[str, object]:
    return json.loads(
        (ROOT / "outputs" / name).read_text(encoding="utf-8")
    )


class AxisNotchPackageTests(unittest.TestCase):
    def test_peak_atlas_uses_all_parent_witnesses(self) -> None:
        atlas = read_output("peak_atlas.json")
        self.assertEqual(atlas["parent_witness_count"], 12)
        rows = atlas["band_rows"]
        self.assertEqual([row["band_id"] for row in rows], [
            "A0", "A1", "A2", "A3", "A4"
        ])
        peaks = [row["primary_peak"]["x"] for row in rows]
        expected = [17.83, 20.38, 23.24, 42.18, 83.05]
        np.testing.assert_allclose(peaks, expected, atol=0.011)

    def test_peak_atlas_target_overlap(self) -> None:
        atlas = read_output("peak_atlas.json")
        observation = atlas["structural_observation"]
        self.assertTrue(
            observation["A1_overlaps_target_real_interval"]
        )
        self.assertGreater(
            observation["harmonic_ratios_relative_to_A1"][
                "A3_over_A1"
            ],
            2.0,
        )

    def test_notch_codes_are_unique_and_complete(self) -> None:
        atlas = read_output("peak_atlas.json")
        codes = resolve_codes(
            patch_center=20.4075,
            patch_x_min=20.395,
            patch_x_max=20.42,
            atlas=atlas,
        )
        identifiers = [code.code_id for code in codes]
        self.assertEqual(len(identifiers), 10)
        self.assertEqual(len(set(identifiers)), 10)
        self.assertIn("anchor_flat", identifiers)

    def test_anchor_flat_suppresses_derivative(self) -> None:
        screen = read_output("notch_screen.json")
        self.assertEqual(len(screen["rows"]), 20)
        row = next(
            row
            for row in screen["rows"]
            if row["radius"] == 16.0
            and row["code_id"] == "anchor_flat"
        )
        self.assertLess(
            row["anchor_derivative_frobenius_norm"],
            2e-12,
        )
        self.assertGreater(
            row["optimized_core_uniform_axis_threshold"],
            30.0,
        )

    def test_spectral_slope_atom_is_even(self) -> None:
        t = np.linspace(-0.8, 0.8, 101)
        atoms, _, metadata = spectral_slope_basis(
            t,
            radius=1.0,
            frequencies=(2.3,),
            powers=(4,),
        )
        self.assertEqual(metadata, [{"frequency": 2.3, "power": 4}])
        np.testing.assert_allclose(
            atoms[:, 0],
            atoms[::-1, 0],
            atol=2e-15,
        )

    def test_spectral_slope_analytic_second_derivative(self) -> None:
        points = np.asarray([-0.63, -0.21, 0.0, 0.37, 0.71])
        h = 1e-5
        center, analytic, _ = spectral_slope_basis(
            points, 1.0, (2.3,), (4,)
        )
        left, _, _ = spectral_slope_basis(
            points - h, 1.0, (2.3,), (4,)
        )
        right, _, _ = spectral_slope_basis(
            points + h, 1.0, (2.3,), (4,)
        )
        finite = (right - 2.0 * center + left) / (h * h)
        np.testing.assert_allclose(
            analytic,
            finite,
            rtol=4e-6,
            atol=2e-6,
        )

    def test_uniform_axis_matrix_matches_outer_mean(self) -> None:
        context = FrontierContext(
            radius=1.0,
            density=6.0,
            width_factor=1.5,
            bump_power=3,
            step=0.04,
        )
        matrix, grid = context.uniform_axis_matrix(0, step=1.0)
        transforms = context.axis_transforms(grid)
        expected = (
            context.count_coefficients[0]
            * np.mean(
                np.einsum(
                    "ki,kj->kij",
                    transforms,
                    transforms,
                ),
                axis=0,
            )
        )
        np.testing.assert_allclose(matrix, expected, atol=2e-14)

    def test_lift_scaling_improves_but_saturates(self) -> None:
        scaling = read_output("lift_scaling.json")
        rows = scaling["rows"]
        self.assertEqual(len(rows), 8)
        baseline = next(row for row in rows if row["lift_id"] == "baseline")
        grid21 = next(row for row in rows if row["lift_id"] == "grid21_p4")
        self.assertEqual(grid21["effective_added_dimension"], 15)
        self.assertLess(
            grid21["optimized_core_uniform_axis_threshold"],
            baseline["optimized_core_uniform_axis_threshold"],
        )
        self.assertGreater(
            grid21["relative_improvement_vs_baseline"],
            0.03,
        )
        self.assertLess(
            max(
                row["relative_improvement_vs_baseline"]
                for row in rows
            ),
            0.04,
        )

    def test_lift_joint_remains_dual_blocked(self) -> None:
        joint = read_output("lift_joint.json")
        self.assertFalse(joint["lift_family_crosses_dual_gate"])
        self.assertEqual(len(joint["rows"]), 2)
        for row in joint["rows"]:
            self.assertTrue(row["safe_budget_block"])
            self.assertFalse(row["primal_search_started"])
            self.assertGreater(row["joint_dual"]["safe_alpha"], 1.0)
            self.assertGreater(
                row["rank_one_complementary_audit"][
                    "scaled_objective"
                ],
                1.0,
            )

    def test_geometry_screen_and_joint_result(self) -> None:
        screen = read_output("geometry_screen.json")
        self.assertEqual(screen["row_count"], 27)
        self.assertEqual(
            screen["top_five"][0]["dimension"],
            190,
        )
        joint = read_output("geometry_joint.json")
        self.assertFalse(joint["any_geometry_crosses_dual_gate"])
        best = min(
            joint["rows"],
            key=lambda row: row["joint_dual"]["alpha"],
        )
        self.assertEqual(best["geometry_id"], "d12_w2_p5")
        self.assertAlmostEqual(
            best["joint_dual"]["safe_alpha"],
            1.071761172347693,
            places=12,
        )
        self.assertFalse(best["primal_search_started"])

    def test_joint_reconstruction_report_passes(self) -> None:
        verification = read_output("joint_verification.json")
        self.assertEqual(verification["row_count"], 4)
        self.assertTrue(
            verification[
                "all_reconstructed_psd_and_block_budget"
            ]
        )
        self.assertLess(
            verification[
                "maximum_minimum_eigenvalue_abs_difference"
            ],
            1e-12,
        )

    def test_summary_keeps_global_claim_false(self) -> None:
        summary = read_output("experiment_summary.json")
        self.assertFalse(summary["global_rh_certificate"])
        self.assertFalse(summary["known_zero_ordinates_used"])
        self.assertFalse(summary["primal_search_started"])
        self.assertEqual(
            summary["next_node"],
            "RH-PaleyWiener-AxisCoreExtremal-20260724-v0.6",
        )


if __name__ == "__main__":
    unittest.main()
