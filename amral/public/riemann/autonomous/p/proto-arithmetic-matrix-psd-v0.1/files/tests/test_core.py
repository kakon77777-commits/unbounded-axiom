from __future__ import annotations

import numpy as np

from arithmetic_psd.core import (
    ArithmeticScanConfig,
    activated_prime_powers,
    archimedean_multiplier,
    build_radius_result,
)


def small_config(radius: float) -> ArithmeticScanConfig:
    return ArithmeticScanConfig(
        support_radii=(radius,),
        basis_size=8,
        quadrature_points=1201,
        frequency_max=35.0,
        frequency_points=4001,
        selected_radius=radius,
    )


def test_no_prime_activation_below_threshold() -> None:
    assert activated_prime_powers(np.log(2.0) - 1e-4, 1000) == []


def test_prime_two_activates_above_threshold() -> None:
    items = activated_prime_powers(np.log(2.0) + 1e-3, 1000)
    assert any(item.prime == 2 and item.exponent == 1 for item in items)


def test_archimedean_multiplier_is_even() -> None:
    points = np.asarray([0.0, 1.0, 3.5, 9.0])
    assert np.allclose(archimedean_multiplier(points), archimedean_multiplier(-points))


def test_constraints_are_satisfied_numerically() -> None:
    result = build_radius_result(small_config(0.3), 0.3)
    assert result.endpoint_constraint_residual < 1e-8
    assert result.central_constraint_residual < 1e-8


def test_matrices_are_symmetric() -> None:
    result = build_radius_result(small_config(0.4), 0.4)
    assert np.allclose(result.matrix_archimedean, result.matrix_archimedean.T)
    assert np.allclose(result.matrix_finite, result.matrix_finite.T)
    assert np.allclose(result.matrix_total, result.matrix_total.T)
