import numpy as np

from phase_shaping.core import PhaseShapingConfig, fit_phase_shaper


def small_config() -> PhaseShapingConfig:
    return PhaseShapingConfig(
        x_min=3.0,
        x_max=3.2,
        y_min=-0.2,
        y_max=-0.1,
        support_radius=5.0,
        basis_size=12,
        bump_width=0.2,
        quadrature_points=1501,
        fit_nx=5,
        fit_ny=4,
        check_nx=7,
        check_ny=5,
        ridge=1e-4,
    )


def test_endpoint_constraint() -> None:
    result = fit_phase_shaper(small_config())
    assert result.endpoint_residual < 1e-6


def test_symmetry() -> None:
    result = fit_phase_shaper(small_config())
    assert result.symmetry_even_residual < 1e-6
    assert result.symmetry_real_residual < 1e-6


def test_shapes() -> None:
    result = fit_phase_shaper(small_config())
    assert result.G_grid.shape == (7, 5)
    assert result.block_grid.shape == (7, 5)
    assert np.isfinite(result.block_grid).all()
