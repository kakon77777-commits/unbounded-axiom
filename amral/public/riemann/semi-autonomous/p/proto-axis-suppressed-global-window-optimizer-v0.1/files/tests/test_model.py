import numpy as np
from prototype import build_model

def test_model_matrices_are_symmetric():
    model = build_model(step=0.02)
    assert np.max(np.abs(model["c0"]-model["c0"].T)) < 1e-10
    assert np.max(
        np.abs(model["q_arithmetic"]-model["q_arithmetic"].T)
    ) < 1e-10

def test_prime_power_filter_is_finite():
    model = build_model(step=0.02)
    assert 0 < len(model["prime_powers"]) < 1000
