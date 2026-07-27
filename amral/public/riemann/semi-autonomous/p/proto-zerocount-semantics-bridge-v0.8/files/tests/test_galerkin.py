from __future__ import annotations

import unittest

from bridge.axis import lower_profile_downward
from bridge.cover import Patch
from bridge.galerkin import (
    PWGalerkinContext,
    cutting_plane_joint_dual,
)


class GalerkinTests(unittest.TestCase):
    def test_small_galerkin_problem_replays(self) -> None:
        patch = Patch(
            "test",
            20.395,
            20.42,
            -0.10625,
            -0.1,
        )
        context = PWGalerkinContext(
            radius=16.0,
            raw_dimension=24,
            count_coefficients_input=tuple(lower_profile_downward()),
            quadrature_order=512,
        )
        result = cutting_plane_joint_dual(
            context,
            patch.points(3, 3),
            axis_step=0.25,
            max_outer=8,
            maxiter=120,
        )
        self.assertTrue(result.optimizer_success)
        self.assertGreater(result.alpha, 1.0)
        self.assertGreater(result.safe_min_eigenvalue, 0.0)
        self.assertFalse(result.axis_supports[0])
        self.assertFalse(result.axis_supports[1])
        self.assertFalse(result.axis_supports[2])
