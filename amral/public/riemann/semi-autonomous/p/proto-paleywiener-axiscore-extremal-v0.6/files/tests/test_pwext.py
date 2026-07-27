from __future__ import annotations

import json
import unittest
from pathlib import Path

import numpy as np
from scipy.linalg import eigh

from pwext.green import (
    GreenRankTwoScanner,
    clamped_green_kernel,
    clamped_representer,
)
from pwext.model import (
    PWGalerkinContext,
    clamped_even_chebyshev,
    rank_two_threshold_from_gram,
)


ROOT = Path(__file__).resolve().parents[1]


def read_output(name: str) -> dict[str, object]:
    return json.loads(
        (ROOT / "outputs" / name).read_text(encoding="utf-8")
    )


class PaleyWienerExtremalTests(unittest.TestCase):
    def test_clamped_basis_value_and_slope_vanish(self) -> None:
        points = np.asarray([-1.0, 1.0])
        values, _ = clamped_even_chebyshev(
            points,
            raw_dimension=8,
            radius=2.0,
        )
        np.testing.assert_allclose(values, 0.0, atol=2e-14)
        h = 1e-6
        left, _ = clamped_even_chebyshev(
            np.asarray([-1.0 + h, 1.0 - h]),
            raw_dimension=8,
            radius=2.0,
        )
        self.assertLess(float(np.max(np.abs(left))) / h, 2e-3)

    def test_galerkin_structural_constraints(self) -> None:
        context = PWGalerkinContext(
            4.0,
            20,
            quadrature_order=512,
        )
        self.assertEqual(context.dimension, 18)
        self.assertLess(
            max(context.structural_residuals.values()),
            1e-8,
        )
        np.testing.assert_allclose(
            context.tail_matrix,
            np.eye(context.dimension),
            atol=0.0,
        )

    def test_green_representer_clamped_boundaries(self) -> None:
        scanner = GreenRankTwoScanner(2.0, 0.002)
        density = np.cos(2.3 * scanner.t)
        representer = clamped_representer(
            density,
            scanner.t,
            scanner.tail_scale,
        )
        self.assertLess(abs(float(representer[0])), 1e-8)
        self.assertLess(abs(float(representer[-1])), 1e-7)
        for xs, ys in (
            (
                scanner.t[:8] - scanner.t[0],
                representer[:8],
            ),
            (
                scanner.t[-8:] - scanner.t[-1],
                representer[-8:],
            ),
        ):
            coefficients = np.polynomial.polynomial.polyfit(
                xs,
                ys,
                4,
            )
            self.assertLess(abs(float(coefficients[1])), 2e-5)

    def test_explicit_green_kernel_matches_ode_solver(self) -> None:
        scanner = GreenRankTwoScanner(1.0, 0.01)
        density = np.cos(2.3 * scanner.t)
        ode = clamped_representer(
            density,
            scanner.t,
            scanner.tail_scale,
        )
        kernel = clamped_green_kernel(
            scanner.t[:, None],
            scanner.t[None, :],
            radius=1.0,
            tail_scale=scanner.tail_scale,
        )
        integral = kernel @ (scanner.weights * density)
        np.testing.assert_allclose(
            integral,
            ode,
            rtol=2e-12,
            atol=2e-8,
        )
        np.testing.assert_allclose(kernel, kernel.T, atol=0.0)

    def test_rank_two_formula_matches_generalized_eigenvalue(
        self,
    ) -> None:
        rng = np.random.default_rng(20260725)
        p = rng.normal(size=7)
        u = rng.normal(size=7)
        v = rng.normal(size=7)
        coefficient = 3.7
        base = np.eye(7) + coefficient * np.outer(p, p)
        core = 2.0 * (
            np.outer(u, u) - np.outer(v, v)
        )
        minimum = float(
            eigh(
                core,
                base,
                eigvals_only=True,
                subset_by_index=[0, 0],
            )[0]
        )
        expected = -1.0 / minimum
        actual = float(
            rank_two_threshold_from_gram(
                p_norm=p @ p,
                u_norm=u @ u,
                v_norm=v @ v,
                uv_inner=u @ v,
                pu_inner=p @ u,
                pv_inner=p @ v,
                axis_coefficient=coefficient,
            )
        )
        self.assertAlmostEqual(actual, expected, places=12)

    def test_single_band_scan_does_not_cross_one(self) -> None:
        output = read_output("green_rank_two_scan.json")
        self.assertTrue(
            output[
                "finest_step_all_single_band_lower_bounds_below_one"
            ]
        )
        a1 = output["rows"][-1]["band_rows"][1]
        self.assertAlmostEqual(
            a1["maximum_point_lower_bound"],
            0.26125331168208926,
            places=11,
        )

    def test_galerkin_joint_sequence_is_monotone(self) -> None:
        output = read_output(
            "galerkin_joint_convergence.json"
        )
        self.assertEqual(len(output["rows"]), 10)
        self.assertTrue(
            output["monotone_raw_alpha_nonincreasing"]
        )
        self.assertTrue(output["all_safe_bounds_above_one"])
        self.assertAlmostEqual(
            output["rows"][-1]["joint_dual"]["alpha"],
            1.1324752108835305,
            places=11,
        )

    def test_independent_green_and_galerkin_agree(self) -> None:
        output = read_output("quadrature_audit.json")
        self.assertTrue(
            output["galerkin_approaches_direct_green_from_above"]
        )
        galerkin = output["galerkin_dimension_rows"][-1][
            "point_extremal"
        ]
        direct = output["direct_green_rows"][-1][
            "point_extremal"
        ]
        self.assertLess(abs(galerkin - direct), 2e-9)

    def test_atomic_transfer_passes_direct_green(self) -> None:
        output = read_output("atomic_transfer.json")
        self.assertTrue(
            output["continuous_kernel_floating_obstruction"]
        )
        finest = output["direct_green_transfer_rows"][-1]
        self.assertGreater(
            finest["raw_threshold_for_fixed_measures"],
            1.13,
        )
        self.assertGreater(
            finest["schur_certificate_minimum_eigenvalue"],
            0.05,
        )
        self.assertEqual(
            finest["negative_rank_for_schur_test"],
            2,
        )

    def test_rational_probability_sums(self) -> None:
        output = read_output("rational_atomic_witness.json")
        denominator = output["weight_denominator"]
        for group in output["axis_supports"]:
            self.assertEqual(
                sum(
                    row["weight"]["numerator"]
                    for row in group
                ),
                denominator,
            )
        self.assertEqual(
            sum(
                row["weight"]["numerator"]
                for row in output["core_support"]
            ),
            denominator,
        )

    def test_rational_candidate_has_expected_scope(self) -> None:
        output = read_output("rational_atomic_witness.json")
        self.assertEqual(
            sum(len(group) for group in output["axis_supports"]),
            58,
        )
        self.assertEqual(len(output["core_support"]), 2)
        self.assertEqual(
            output["model"]["target_alpha"],
            {"numerator": 21, "denominator": 20},
        )
        self.assertTrue(output["rationalized_floating_pass"])
        self.assertFalse(output["interval_certified"])

    def test_certificate_budget_has_margin(self) -> None:
        output = read_output("certificate_budget.json")
        self.assertEqual(
            output["recommended_interval_target_alpha"],
            1.05,
        )
        self.assertGreater(
            output["finest_target_schur_minimum_eigenvalue"],
            0.069,
        )
        self.assertLess(
            output["last_step_schur_drift"],
            3e-8,
        )

    def test_summary_keeps_global_flags_false(self) -> None:
        output = read_output("experiment_summary.json")
        self.assertTrue(
            output["continuous_kernel_atomic_result"][
                "floating_obstruction_pass"
            ]
        )
        self.assertFalse(output["interval_certified"])
        self.assertFalse(output["global_rh_certificate"])
        self.assertFalse(output["known_zero_ordinates_used"])
        self.assertEqual(
            output["next_node"],
            "RH-IntervalGreenKernel-AtomicCertificate-20260725-v0.7",
        )


if __name__ == "__main__":
    unittest.main()
