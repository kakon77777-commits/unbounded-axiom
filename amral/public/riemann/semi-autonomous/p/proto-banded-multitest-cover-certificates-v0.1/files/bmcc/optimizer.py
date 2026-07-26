from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any

import numpy as np
from scipy.integrate import quad
from scipy.optimize import linprog, minimize

from .cover import Patch
from .model import (
    block_matrices,
    block_values,
    fourier_matrix,
    function_diagnostics,
)


@dataclass
class Candidate:
    candidate_id: str
    seed_patch: str
    penalty: float
    optimizer_success: bool
    optimizer_message: str
    reduced_coefficients: np.ndarray
    coefficients: np.ndarray
    seed_grid_max_block: float
    arithmetic_value: float
    axis_band_energy: float
    known_zero_mass: float
    first_zero_mass: float
    l1: float
    first_moment_l1: float
    derivative_variation: float

    def summary(self) -> dict[str, Any]:
        return {
            "candidate_id": self.candidate_id,
            "seed_patch": self.seed_patch,
            "penalty": self.penalty,
            "optimizer_success": self.optimizer_success,
            "optimizer_message": self.optimizer_message,
            "seed_grid_max_block": self.seed_grid_max_block,
            "arithmetic_value": self.arithmetic_value,
            "axis_band_energy": self.axis_band_energy,
            "known_zero_mass": self.known_zero_mass,
            "first_zero_mass": self.first_zero_mass,
            "l1": self.l1,
            "first_moment_l1": self.first_moment_l1,
            "derivative_variation": self.derivative_variation,
            "reduced_coefficients": self.reduced_coefficients.tolist(),
            "coefficients": self.coefficients.tolist(),
        }


def quadratic_values(matrices: np.ndarray, vector: np.ndarray) -> np.ndarray:
    return np.einsum("i,kij,j->k", vector, matrices, vector)


def _solve_penalized_minimax(
    matrices: np.ndarray,
    arithmetic: np.ndarray,
    energy_normalized: np.ndarray,
    arithmetic_floor: float,
    penalty: float,
    starts: list[np.ndarray],
) -> Any:
    dimension = arithmetic.shape[0]

    def target_constraint(z: np.ndarray) -> np.ndarray:
        return z[-1] - quadratic_values(matrices, z[:-1])

    def target_jacobian(z: np.ndarray) -> np.ndarray:
        return np.column_stack(
            (
                -2.0 * np.einsum("kij,j->ki", matrices, z[:-1]),
                np.ones(len(matrices)),
            )
        )

    constraints = [
        {
            "type": "eq",
            "fun": lambda z: z[:-1] @ z[:-1] - 1.0,
            "jac": lambda z: np.concatenate((2.0 * z[:-1], [0.0])),
        },
        {
            "type": "ineq",
            "fun": lambda z: z[:-1] @ arithmetic @ z[:-1]
            - arithmetic_floor,
            "jac": lambda z: np.concatenate(
                (2.0 * arithmetic @ z[:-1], [0.0])
            ),
        },
        {
            "type": "ineq",
            "fun": target_constraint,
            "jac": target_jacobian,
        },
    ]

    best = None
    for start in starts:
        start = np.asarray(start, dtype=float)
        start /= np.linalg.norm(start)
        t0 = float(np.max(quadratic_values(matrices, start)) + 1e-7)
        result = minimize(
            lambda z: float(
                z[-1] + penalty * (z[:-1] @ energy_normalized @ z[:-1])
            ),
            np.concatenate((start, [t0])),
            jac=lambda z: np.concatenate(
                (2.0 * penalty * energy_normalized @ z[:-1], [1.0])
            ),
            constraints=constraints,
            method="SLSQP",
            options={"maxiter": 1400, "ftol": 1e-12, "disp": False},
        )
        y = result.x[:-1]
        norm = np.linalg.norm(y)
        if norm == 0.0:
            continue
        y = y / norm
        feasible = (
            y @ arithmetic @ y >= arithmetic_floor - 2e-7
            and np.max(quadratic_values(matrices, y)) <= result.x[-1] + 2e-7
        )
        score = float(
            np.max(quadratic_values(matrices, y))
            + penalty * (y @ energy_normalized @ y)
        )
        if feasible and (best is None or score < best[0]):
            best = (score, result, y)
    if best is None:
        raise RuntimeError("All penalized minimax starts failed feasibility checks")
    return best[1], best[2]


def generate_candidates(
    patches: list[Patch],
    model: dict[str, object],
    coordinate_map: np.ndarray,
    energy: np.ndarray,
    ordinates: np.ndarray,
    penalties: tuple[float, ...],
    arithmetic_floor: float,
    random_seed: int,
) -> list[Candidate]:
    arithmetic = coordinate_map.T @ np.asarray(model["q_arithmetic"]) @ coordinate_map
    arithmetic = 0.5 * (arithmetic + arithmetic.T)
    energy_scale = float(np.trace(energy) / len(energy))
    energy_normalized = energy / energy_scale
    q_vectors = np.linalg.eigh(arithmetic)[1]
    e_vectors = np.linalg.eigh(energy_normalized)[1]
    zero_transform = fourier_matrix(ordinates.astype(complex), model)
    rng = np.random.default_rng(random_seed)
    candidates: list[Candidate] = []

    for patch in patches:
        seed_points = patch.points(9, 7)
        matrices = block_matrices(seed_points, model, coordinate_map)
        mean_vector = np.linalg.eigh(np.mean(matrices, axis=0))[1][:, 0]
        continuation = mean_vector
        for index, penalty in enumerate(penalties):
            random_start = rng.normal(size=arithmetic.shape[0])
            starts = [
                continuation,
                mean_vector,
                q_vectors[:, -1],
                e_vectors[:, 0],
                random_start,
            ]
            result, reduced = _solve_penalized_minimax(
                matrices,
                arithmetic,
                energy_normalized,
                arithmetic_floor,
                penalty,
                starts,
            )
            continuation = reduced
            coefficients = coordinate_map @ reduced
            zero_values = zero_transform @ coefficients
            diagnostics = function_diagnostics(coefficients, model)
            candidate_id = f"{patch.patch_id}_P{index:02d}"
            candidates.append(
                Candidate(
                    candidate_id=candidate_id,
                    seed_patch=patch.patch_id,
                    penalty=float(penalty),
                    optimizer_success=bool(result.success),
                    optimizer_message=str(result.message),
                    reduced_coefficients=reduced,
                    coefficients=coefficients,
                    seed_grid_max_block=float(
                        np.max(quadratic_values(matrices, reduced))
                    ),
                    arithmetic_value=float(reduced @ arithmetic @ reduced),
                    axis_band_energy=float(reduced @ energy @ reduced),
                    known_zero_mass=float(np.sum(np.abs(zero_values) ** 2)),
                    first_zero_mass=float(abs(zero_values[0]) ** 2),
                    l1=diagnostics["l1"],
                    first_moment_l1=diagnostics["first_moment_l1"],
                    derivative_variation=diagnostics[
                        "derivative_total_variation_proxy"
                    ],
                )
            )
    return candidates


def _block_table(
    points: np.ndarray,
    candidates: list[Candidate],
    model: dict[str, object],
) -> np.ndarray:
    transform = fourier_matrix(points, model)
    coefficients = np.column_stack([c.coefficients for c in candidates])
    values = transform @ coefficients
    return 2.0 * np.real(values * values)


def _stage_one(
    active_core: np.ndarray,
    arithmetic: np.ndarray,
    energy: np.ndarray,
    arithmetic_floor: float,
) -> Any:
    a_ub = np.vstack((active_core, -arithmetic[None, :]))
    b_ub = np.concatenate(
        (-np.ones(len(active_core)), [-arithmetic_floor])
    )
    return linprog(
        energy,
        A_ub=a_ub,
        b_ub=b_ub,
        bounds=[(0.0, None)] * len(energy),
        method="highs",
    )


def _stage_two(
    active_core: np.ndarray,
    guard: np.ndarray,
    arithmetic: np.ndarray,
    energy: np.ndarray,
    arithmetic_floor: float,
    energy_limit: float,
) -> Any:
    count = len(energy)
    core_rows = np.column_stack((active_core, np.zeros(len(active_core))))
    guard_rows = np.column_stack((guard, -np.ones(len(guard))))
    arithmetic_row = np.concatenate((-arithmetic, [0.0]))[None, :]
    energy_row = np.concatenate((energy, [0.0]))[None, :]
    a_ub = np.vstack((core_rows, guard_rows, arithmetic_row, energy_row))
    b_ub = np.concatenate(
        (
            -np.ones(len(active_core)),
            np.zeros(len(guard)),
            [-arithmetic_floor, energy_limit],
        )
    )
    objective = np.concatenate((np.full(count, 1e-10), [1.0]))
    return linprog(
        objective,
        A_ub=a_ub,
        b_ub=b_ub,
        bounds=[(0.0, None)] * count + [(0.0, None)],
        method="highs",
    )


def _best_single(
    dense_core: np.ndarray,
    guard: np.ndarray,
    candidates: list[Candidate],
    arithmetic_floor: float,
) -> dict[str, Any] | None:
    best = None
    for index, candidate in enumerate(candidates):
        worst = float(np.max(dense_core[:, index]))
        if worst >= 0.0:
            continue
        scale = 1.0 / (-worst)
        if scale * candidate.arithmetic_value < arithmetic_floor:
            continue
        row = {
            "candidate_id": candidate.candidate_id,
            "scale": scale,
            "axis_band_energy": scale * candidate.axis_band_energy,
            "known_zero_mass": scale * candidate.known_zero_mass,
            "first_zero_mass": scale * candidate.first_zero_mass,
            "arithmetic_value": scale * candidate.arithmetic_value,
            "guard_positive_max": max(
                0.0, float(np.max(scale * guard[:, index]))
            ),
        }
        if best is None or row["axis_band_energy"] < best["axis_band_energy"]:
            best = row
    return best


def _s_bound(t: float) -> float:
    return 0.111 * math.log(t) + 0.275 * math.log(math.log(t)) + 2.450


def tail_multiplier(start: float = 145.0, split: int = 500) -> float:
    """Prototype coefficient multiplying TV(psi')^2 in a t^-4 tail."""

    def density(t: float) -> float:
        return 1.0 + math.log(t) / (2.0 * math.pi) + 2.0 * _s_bound(t + 1.0)

    first_shell = int(math.ceil(start))
    finite = sum(
        density(n + 1.0) / (n**4) for n in range(first_shell, split)
    )
    continuation = quad(
        lambda value: density(value + 1.0) / value**4,
        float(split),
        np.inf,
        epsabs=1e-14,
        epsrel=1e-11,
    )[0]
    return float(finite + 1.05 * continuation)


def build_patch_certificate(
    patch: Patch,
    candidates: list[Candidate],
    model: dict[str, object],
    arithmetic_floor: float = 1e-3,
    energy_slack: float = 0.05,
    max_exchange_rounds: int = 16,
) -> dict[str, Any]:
    fit_points = patch.points(9, 7)
    dense_nx = 161
    dense_ny = 121
    dense_points = patch.points(dense_nx, dense_ny)
    guard_points = patch.guard_ring(49, 37)
    fit_table = _block_table(fit_points, candidates, model)
    dense_table = _block_table(dense_points, candidates, model)
    guard_table = _block_table(guard_points, candidates, model)

    arithmetic = np.asarray([c.arithmetic_value for c in candidates])
    energy = np.asarray([c.axis_band_energy for c in candidates])
    active = fit_table.copy()
    history: list[dict[str, Any]] = []
    result_two = None

    for round_index in range(max_exchange_rounds):
        result_one = _stage_one(active, arithmetic, energy, arithmetic_floor)
        if not result_one.success:
            raise RuntimeError(
                f"{patch.patch_id}: stage-one LP failed: {result_one.message}"
            )
        energy_optimum = float(result_one.fun)
        result_two = _stage_two(
            active,
            guard_table,
            arithmetic,
            energy,
            arithmetic_floor,
            (1.0 + energy_slack) * energy_optimum,
        )
        if not result_two.success:
            raise RuntimeError(
                f"{patch.patch_id}: stage-two LP failed: {result_two.message}"
            )
        weights = result_two.x[:-1]
        dense_values = dense_table @ weights
        worst_index = int(np.argmax(dense_values))
        dense_maximum = float(dense_values[worst_index])
        history.append(
            {
                "round": round_index,
                "active_core_constraints": int(len(active)),
                "stage_one_energy": energy_optimum,
                "stage_two_energy": float(energy @ weights),
                "dense_core_max": dense_maximum,
            }
        )
        if dense_maximum <= -1.0 + 2e-7:
            break
        active = np.vstack((active, dense_table[worst_index]))

    if result_two is None:
        raise RuntimeError("Internal error: no conic solution")
    weights = result_two.x[:-1]
    dense_values = dense_table @ weights
    guard_values = guard_table @ weights
    nonzero = np.flatnonzero(weights > max(1e-10, 1e-8 * np.max(weights)))
    known_mass = float(
        np.dot(weights, [candidate.known_zero_mass for candidate in candidates])
    )
    first_mass = float(
        np.dot(weights, [candidate.first_zero_mass for candidate in candidates])
    )
    arithmetic_value = float(arithmetic @ weights)
    axis_energy = float(energy @ weights)
    tv_square_sum = float(
        np.dot(
            weights,
            [candidate.derivative_variation**2 for candidate in candidates],
        )
    )
    tail_bound = tail_multiplier() * tv_square_sum
    l1_lipschitz = float(
        np.dot(
            weights,
            [
                4.0
                * math.exp(2.0 * abs(patch.y_min) * float(model["radius"]))
                * candidate.l1
                * candidate.first_moment_l1
                for candidate in candidates
            ],
        )
    )
    dx = (patch.x_max - patch.x_min) / (dense_nx - 1)
    dy = (patch.y_max - patch.y_min) / (dense_ny - 1)
    crude_continuous_upper = float(
        np.max(dense_values) + l1_lipschitz * (dx + dy) / 2.0
    )
    guard_positive = max(0.0, float(np.max(guard_values)))
    partial_gap = 1.0 - known_mass - tail_bound - guard_positive
    baseline = _best_single(
        dense_table, guard_table, candidates, arithmetic_floor
    )
    stage_one_energy = float(history[-1]["stage_one_energy"])
    stage_one_improvement = None
    selected_energy_overhead = None
    guard_improvement = None
    if baseline is not None:
        stage_one_improvement = (
            baseline["axis_band_energy"] - stage_one_energy
        ) / baseline["axis_band_energy"]
        selected_energy_overhead = (
            axis_energy - baseline["axis_band_energy"]
        ) / baseline["axis_band_energy"]
        if baseline["guard_positive_max"] > 0.0:
            guard_improvement = (
                baseline["guard_positive_max"] - guard_positive
            ) / baseline["guard_positive_max"]

    pareto_profile = []
    for slack in (0.0, 0.01, 0.025, 0.05, 0.10):
        pareto_result = _stage_two(
            active,
            guard_table,
            arithmetic,
            energy,
            arithmetic_floor,
            (1.0 + slack) * stage_one_energy,
        )
        if not pareto_result.success:
            pareto_profile.append(
                {
                    "axis_energy_slack": slack,
                    "solver_success": False,
                    "message": pareto_result.message,
                }
            )
            continue
        pareto_weights = pareto_result.x[:-1]
        pareto_profile.append(
            {
                "axis_energy_slack": slack,
                "solver_success": True,
                "axis_band_energy": float(energy @ pareto_weights),
                "guard_positive_max": max(
                    0.0, float(np.max(guard_table @ pareto_weights))
                ),
                "dense_core_max": float(
                    np.max(dense_table @ pareto_weights)
                ),
                "active_candidate_count": int(
                    np.sum(
                        pareto_weights
                        > max(1e-10, 1e-8 * np.max(pareto_weights))
                    )
                ),
            }
        )

    return {
        "patch": patch.to_dict(),
        "normalization": "aggregate dense-core maximum constrained to <= -1",
        "candidate_count": len(candidates),
        "active_candidate_count": int(len(nonzero)),
        "active_candidates": [
            {
                "candidate_id": candidates[index].candidate_id,
                "weight": float(weights[index]),
            }
            for index in nonzero
        ],
        "arithmetic_floor": arithmetic_floor,
        "arithmetic_value": arithmetic_value,
        "stage_one_axis_energy_optimum": stage_one_energy,
        "axis_band_energy": axis_energy,
        "known_first_50_zero_mass_holdout": known_mass,
        "first_zero_mass_holdout": first_mass,
        "tail_majorant_from_145_prototype": tail_bound,
        "guard_positive_max": guard_positive,
        "partial_gap_excluding_other_off_axis_bands": partial_gap,
        "dense_core_max": float(np.max(dense_values)),
        "dense_core_min": float(np.min(dense_values)),
        "dense_core_grid": {"nx": dense_nx, "ny": dense_ny},
        "guard_grid_count": int(len(guard_points)),
        "crude_l1_lipschitz_constant": l1_lipschitz,
        "crude_continuous_upper_bound": crude_continuous_upper,
        "sampled_core_pass": bool(np.max(dense_values) < 0.0),
        "crude_continuous_sign_pass": bool(crude_continuous_upper < 0.0),
        "partial_budget_pass": bool(partial_gap > 0.0),
        "other_off_axis_bands_certified": False,
        "global_certificate_pass": False,
        "single_candidate_baseline": baseline,
        "stage_one_axis_energy_improvement_vs_single_fraction": stage_one_improvement,
        "selected_axis_energy_overhead_vs_single_fraction": selected_energy_overhead,
        "selected_guard_improvement_vs_single_fraction": guard_improvement,
        "guard_axis_energy_pareto": pareto_profile,
        "exchange_history": history,
        "status": (
            "E2 floating sampled certificate"
            if np.max(dense_values) < 0.0
            else "failed sampled certificate"
        ),
        "warning": (
            "The holdout zero values, derivative-variation tail, quadrature, "
            "LP, and Lipschitz audit are floating prototype computations. "
            "No interval enclosure or global off-axis budget is asserted."
        ),
    }
