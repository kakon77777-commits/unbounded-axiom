import numpy as np

from bmcc.optimizer import _stage_one, _stage_two, tail_multiplier


def test_two_stage_conic_lp() -> None:
    core = np.asarray(
        [
            [-2.0, -0.5],
            [-0.5, -2.0],
        ]
    )
    guard = np.asarray([[1.0, -0.2], [-0.2, 1.0]])
    arithmetic = np.asarray([1.0, 1.0])
    energy = np.asarray([1.0, 1.0])
    first = _stage_one(core, arithmetic, energy, 0.1)
    assert first.success
    second = _stage_two(
        core,
        guard,
        arithmetic,
        energy,
        0.1,
        1.05 * first.fun,
    )
    assert second.success
    weights = second.x[:-1]
    assert np.max(core @ weights) <= -1.0 + 1e-8
    assert arithmetic @ weights >= 0.1 - 1e-8
    assert energy @ weights <= 1.05 * first.fun + 1e-8


def test_tail_multiplier_is_positive_and_small() -> None:
    value = tail_multiplier(145.0, 500)
    assert 0.0 < value < 1e-4
