from __future__ import annotations

import numpy as np

from intersection_solver import IntersectionConfig, solve_radius
from intersection_solver.arithmetic import activated_prime_powers


def tiny_config() -> IntersectionConfig:
    return IntersectionConfig(
        x_min=8.0,
        x_max=8.2,
        y_min=-0.2,
        y_max=-0.1,
        support_radii=(2.5,),
        basis_size=12,
        quadrature_points=1001,
        fit_nx=5,
        fit_ny=4,
        check_nx=9,
        check_ny=7,
        optimizer_starts=2,
        optimizer_maxiter=120,
        selected_radius=2.5,
    )


def test_prime_activation_threshold() -> None:
    assert activated_prime_powers(0.69, 1000) == []
    assert len(activated_prime_powers(0.70, 1000)) == 1


def test_shared_normalization_and_constraints() -> None:
    result = solve_radius(tiny_config(), 2.5)
    assert abs(result.c0_norm - 1.0) < 5e-5
    assert result.endpoint_residual < 1e-8
    assert result.central_residual < 1e-8


def test_matrix_direct_audit() -> None:
    result = solve_radius(tiny_config(), 2.5)
    assert result.matrix_audit["c0_abs_difference"] < 5e-3
    assert result.matrix_audit["finite_abs_difference"] < 5e-3
    assert result.matrix_audit["archimedean_abs_difference"] < 5e-3
    assert result.matrix_audit["total_abs_difference"] < 5e-3


def test_outputs_are_finite() -> None:
    result = solve_radius(tiny_config(), 2.5)
    values = [
        result.arithmetic_value,
        result.check_grid_max_block,
        result.check_grid_min_block,
        result.arithmetic_min_eigenvalue,
    ]
    assert np.all(np.isfinite(values))
