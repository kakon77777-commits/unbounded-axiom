import numpy as np

from bmcc.model import (
    block_values,
    build_model,
    constrained_whitener,
    spectral_energy_matrix,
)


def test_whitener_and_structural_constraints() -> None:
    model = build_model()
    coordinate_map = constrained_whitener(model)
    gram = coordinate_map.T @ model["c0"] @ coordinate_map
    assert coordinate_map.shape == (24, 22)
    assert np.max(np.abs(gram - np.eye(22))) < 2e-8
    assert np.max(np.abs(model["g0_constraint"] @ coordinate_map)) < 1e-8
    assert np.max(np.abs(model["endpoint_constraint"] @ coordinate_map)) < 1e-8


def test_axis_energy_is_psd_and_independent_of_zero_list() -> None:
    model = build_model()
    coordinate_map = constrained_whitener(model)
    energy, bands = spectral_energy_matrix(
        model, coordinate_map, start=14.0, stop=35.0, step=0.2
    )
    assert bands == [{"start": 14.0, "stop": 35.0, "step": 0.2}]
    assert np.linalg.eigvalsh(energy)[0] > -1e-10


def test_rank_one_cone_is_nonnegative_on_real_axis() -> None:
    model = build_model()
    coordinate_map = constrained_whitener(model)
    rng = np.random.default_rng(7)
    points = np.linspace(14.0, 35.0, 71).astype(complex)
    total = np.zeros(len(points))
    for weight in (0.3, 0.7, 1.1):
        reduced = rng.normal(size=coordinate_map.shape[1])
        reduced /= np.linalg.norm(reduced)
        total += weight * block_values(
            points, coordinate_map @ reduced, model
        )
    assert np.min(total) > -1e-11
