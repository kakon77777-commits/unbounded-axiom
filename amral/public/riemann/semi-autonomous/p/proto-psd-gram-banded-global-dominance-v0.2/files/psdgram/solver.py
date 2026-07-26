from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np
from scipy.optimize import linprog, minimize


@dataclass
class FactorizedResult:
    rank: int
    factor: np.ndarray
    gram: np.ndarray
    optimizer_success: bool
    optimizer_message: str
    objective_value: float
    core_max: float
    arithmetic_value: float
    iterations: int
    constraint_violation: float


@dataclass
class BandedFactorizedResult:
    factor_result: FactorizedResult
    band_bounds: np.ndarray
    band_charges: np.ndarray
    tail_value: float
    majorant_value: float
    guard_bound: float | None = None


def matrix_value(matrix: np.ndarray, factor: np.ndarray) -> float:
    return float(np.einsum("ir,ij,jr->", factor, matrix, factor))


def matrix_values(matrices: np.ndarray, factor: np.ndarray) -> np.ndarray:
    return np.einsum("ir,kij,jr->k", factor, matrices, factor)


def matrix_grad(matrix: np.ndarray, factor: np.ndarray) -> np.ndarray:
    return 2.0 * matrix @ factor


def matrix_grads(matrices: np.ndarray, factor: np.ndarray) -> np.ndarray:
    return 2.0 * np.einsum("kij,jr->kir", matrices, factor)


def factor_from_gram(
    gram: np.ndarray,
    rank: int,
    core_matrices: np.ndarray,
    safety: float = 1.002,
) -> np.ndarray:
    values, vectors = np.linalg.eigh(0.5 * (gram + gram.T))
    order = np.argsort(values)[::-1]
    values = np.maximum(values[order], 0.0)
    vectors = vectors[:, order]
    factor = np.zeros((len(gram), rank))
    keep = min(rank, int(np.sum(values > 1e-12)))
    if keep:
        factor[:, :keep] = (
            vectors[:, :keep] * np.sqrt(values[:keep])[None, :]
        )
    core = matrix_values(core_matrices, factor)
    worst = float(np.max(core))
    if worst >= 0.0:
        raise ValueError("Truncated Gram factor is not negative on the core")
    factor *= np.sqrt(safety / (-worst))
    return factor


def rank_one_start(
    direction: np.ndarray,
    rank: int,
    core_matrices: np.ndarray,
    arithmetic: np.ndarray,
    arithmetic_floor: float,
) -> np.ndarray:
    direction = np.asarray(direction, dtype=float)
    direction /= np.linalg.norm(direction)
    values = np.einsum("i,kij,j->k", direction, core_matrices, direction)
    worst = float(np.max(values))
    if worst >= 0.0:
        raise ValueError("Rank-one direction is not negative across the core")
    scale = 1.005 / (-worst)
    arithmetic_value = float(direction @ arithmetic @ direction) * scale
    if arithmetic_value <= 0.0:
        raise ValueError("Rank-one direction has nonpositive arithmetic value")
    scale = max(scale, 1.005 * arithmetic_floor / arithmetic_value * scale)
    factor = np.zeros((len(direction), rank))
    factor[:, 0] = np.sqrt(scale) * direction
    return factor


def _constraint_violation(
    core_matrices: np.ndarray,
    arithmetic: np.ndarray,
    arithmetic_floor: float,
    factor: np.ndarray,
) -> float:
    core_violation = max(
        0.0, float(np.max(matrix_values(core_matrices, factor)) + 1.0)
    )
    arithmetic_violation = max(
        0.0, arithmetic_floor - matrix_value(arithmetic, factor)
    )
    return max(core_violation, arithmetic_violation)


def solve_factorized_stage_one(
    core_matrices: np.ndarray,
    arithmetic: np.ndarray,
    objective_matrix: np.ndarray,
    arithmetic_floor: float,
    initial_factors: list[np.ndarray],
    maxiter: int = 1600,
) -> FactorizedResult:
    dimension, rank = initial_factors[0].shape

    def unpack(x: np.ndarray) -> np.ndarray:
        return x.reshape(dimension, rank)

    def objective(x: np.ndarray) -> float:
        return matrix_value(objective_matrix, unpack(x))

    def objective_jac(x: np.ndarray) -> np.ndarray:
        return matrix_grad(objective_matrix, unpack(x)).reshape(-1)

    def core_fun(x: np.ndarray) -> np.ndarray:
        return -1.0 - matrix_values(core_matrices, unpack(x))

    def core_jac(x: np.ndarray) -> np.ndarray:
        return -matrix_grads(core_matrices, unpack(x)).reshape(
            len(core_matrices), -1
        )

    def arithmetic_fun(x: np.ndarray) -> float:
        return matrix_value(arithmetic, unpack(x)) - arithmetic_floor

    def arithmetic_jac(x: np.ndarray) -> np.ndarray:
        return matrix_grad(arithmetic, unpack(x)).reshape(-1)

    constraints = [
        {"type": "ineq", "fun": core_fun, "jac": core_jac},
        {
            "type": "ineq",
            "fun": arithmetic_fun,
            "jac": arithmetic_jac,
        },
    ]
    best = None
    for initial in initial_factors:
        result = minimize(
            objective,
            initial.reshape(-1),
            jac=objective_jac,
            constraints=constraints,
            method="SLSQP",
            options={
                "maxiter": maxiter,
                "ftol": 1e-11,
                "disp": False,
            },
        )
        factor = unpack(result.x)
        violation = _constraint_violation(
            core_matrices,
            arithmetic,
            arithmetic_floor,
            factor,
        )
        score = objective(result.x)
        if violation <= 5e-6 and (
            best is None or score < best[0]
        ):
            best = (score, result, factor, violation)
    if best is None:
        raise RuntimeError("No feasible factorized stage-one result")
    score, result, factor, violation = best
    gram = factor @ factor.T
    return FactorizedResult(
        rank=rank,
        factor=factor,
        gram=gram,
        optimizer_success=bool(result.success),
        optimizer_message=str(result.message),
        objective_value=float(score),
        core_max=float(np.max(matrix_values(core_matrices, factor))),
        arithmetic_value=matrix_value(arithmetic, factor),
        iterations=int(result.nit),
        constraint_violation=float(violation),
    )


def solve_factorized_stage_two(
    core_matrices: np.ndarray,
    guard_matrices: np.ndarray,
    arithmetic: np.ndarray,
    objective_matrix: np.ndarray,
    arithmetic_floor: float,
    objective_limit: float,
    initial_factor: np.ndarray,
    maxiter: int = 1800,
) -> tuple[FactorizedResult, float]:
    dimension, rank = initial_factor.shape

    def unpack(x: np.ndarray) -> tuple[np.ndarray, float]:
        return x[:-1].reshape(dimension, rank), float(x[-1])

    def objective(x: np.ndarray) -> float:
        factor, guard_bound = unpack(x)
        return guard_bound + 1e-10 * matrix_value(
            objective_matrix, factor
        )

    def objective_jac(x: np.ndarray) -> np.ndarray:
        factor, _ = unpack(x)
        return np.concatenate(
            (
                1e-10
                * matrix_grad(objective_matrix, factor).reshape(-1),
                [1.0],
            )
        )

    def core_fun(x: np.ndarray) -> np.ndarray:
        factor, _ = unpack(x)
        return -1.0 - matrix_values(core_matrices, factor)

    def core_jac(x: np.ndarray) -> np.ndarray:
        factor, _ = unpack(x)
        gradients = -matrix_grads(core_matrices, factor).reshape(
            len(core_matrices), -1
        )
        return np.column_stack((gradients, np.zeros(len(gradients))))

    def guard_fun(x: np.ndarray) -> np.ndarray:
        factor, guard_bound = unpack(x)
        return guard_bound - matrix_values(guard_matrices, factor)

    def guard_jac(x: np.ndarray) -> np.ndarray:
        factor, _ = unpack(x)
        gradients = -matrix_grads(guard_matrices, factor).reshape(
            len(guard_matrices), -1
        )
        return np.column_stack((gradients, np.ones(len(gradients))))

    def arithmetic_fun(x: np.ndarray) -> float:
        factor, _ = unpack(x)
        return matrix_value(arithmetic, factor) - arithmetic_floor

    def arithmetic_jac(x: np.ndarray) -> np.ndarray:
        factor, _ = unpack(x)
        return np.concatenate(
            (matrix_grad(arithmetic, factor).reshape(-1), [0.0])
        )

    def leakage_fun(x: np.ndarray) -> float:
        factor, _ = unpack(x)
        return objective_limit - matrix_value(objective_matrix, factor)

    def leakage_jac(x: np.ndarray) -> np.ndarray:
        factor, _ = unpack(x)
        return np.concatenate(
            (-matrix_grad(objective_matrix, factor).reshape(-1), [0.0])
        )

    constraints = [
        {"type": "ineq", "fun": core_fun, "jac": core_jac},
        {"type": "ineq", "fun": guard_fun, "jac": guard_jac},
        {
            "type": "ineq",
            "fun": arithmetic_fun,
            "jac": arithmetic_jac,
        },
        {"type": "ineq", "fun": leakage_fun, "jac": leakage_jac},
        {
            "type": "ineq",
            "fun": lambda x: x[-1],
            "jac": lambda x: np.concatenate(
                (np.zeros(len(x) - 1), [1.0])
            ),
        },
    ]
    initial_guard = max(
        0.0,
        float(np.max(matrix_values(guard_matrices, initial_factor))),
    ) + 1e-6
    result = minimize(
        objective,
        np.concatenate((initial_factor.reshape(-1), [initial_guard])),
        jac=objective_jac,
        constraints=constraints,
        method="SLSQP",
        options={"maxiter": maxiter, "ftol": 1e-11, "disp": False},
    )
    factor, guard_bound = unpack(result.x)
    violation = max(
        _constraint_violation(
            core_matrices,
            arithmetic,
            arithmetic_floor,
            factor,
        ),
        max(
            0.0,
            matrix_value(objective_matrix, factor) - objective_limit,
        ),
        max(
            0.0,
            float(np.max(matrix_values(guard_matrices, factor)))
            - guard_bound,
        ),
        max(0.0, -guard_bound),
    )
    if violation > 1e-5:
        raise RuntimeError(
            f"Stage-two factorized result violates constraints by {violation}"
        )
    gram = factor @ factor.T
    return (
        FactorizedResult(
            rank=rank,
            factor=factor,
            gram=gram,
            optimizer_success=bool(result.success),
            optimizer_message=str(result.message),
            objective_value=matrix_value(objective_matrix, factor),
            core_max=float(np.max(matrix_values(core_matrices, factor))),
            arithmetic_value=matrix_value(arithmetic, factor),
            iterations=int(result.nit),
            constraint_violation=float(violation),
        ),
        float(guard_bound),
    )


def solve_diagonal_stage_one(
    core_table: np.ndarray,
    arithmetic: np.ndarray,
    objective: np.ndarray,
    arithmetic_floor: float,
) -> Any:
    a_ub = np.vstack((core_table, -arithmetic[None, :]))
    b_ub = np.concatenate(
        (-np.ones(len(core_table)), [-arithmetic_floor])
    )
    return linprog(
        objective,
        A_ub=a_ub,
        b_ub=b_ub,
        bounds=[(0.0, None)] * len(objective),
        method="highs",
    )


def solve_diagonal_stage_two(
    core_table: np.ndarray,
    guard_table: np.ndarray,
    arithmetic: np.ndarray,
    objective: np.ndarray,
    arithmetic_floor: float,
    objective_limit: float,
) -> Any:
    count = len(objective)
    a_ub = np.vstack(
        (
            np.column_stack((core_table, np.zeros(len(core_table)))),
            np.column_stack((guard_table, -np.ones(len(guard_table)))),
            np.concatenate((-arithmetic, [0.0]))[None, :],
            np.concatenate((objective, [0.0]))[None, :],
        )
    )
    b_ub = np.concatenate(
        (
            -np.ones(len(core_table)),
            np.zeros(len(guard_table)),
            [-arithmetic_floor, objective_limit],
        )
    )
    return linprog(
        np.concatenate((np.full(count, 1e-10), [1.0])),
        A_ub=a_ub,
        b_ub=b_ub,
        bounds=[(0.0, None)] * count + [(0.0, None)],
        method="highs",
    )


def solve_banded_factorized_stage_one(
    core_matrices: np.ndarray,
    axis_matrices: list[np.ndarray],
    band_counts: np.ndarray,
    arithmetic: np.ndarray,
    tail_matrix: np.ndarray,
    arithmetic_floor: float,
    initial_factors: list[np.ndarray],
    maxiter: int = 2200,
) -> BandedFactorizedResult:
    dimension, rank = initial_factors[0].shape
    band_count = len(axis_matrices)

    def unpack(x: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        return (
            x[: dimension * rank].reshape(dimension, rank),
            x[dimension * rank :],
        )

    def objective(x: np.ndarray) -> float:
        factor, bounds = unpack(x)
        return matrix_value(tail_matrix, factor) + float(
            band_counts @ bounds
        )

    def objective_jac(x: np.ndarray) -> np.ndarray:
        factor, _ = unpack(x)
        return np.concatenate(
            (matrix_grad(tail_matrix, factor).reshape(-1), band_counts)
        )

    def core_fun(x: np.ndarray) -> np.ndarray:
        factor, _ = unpack(x)
        return -1.0 - matrix_values(core_matrices, factor)

    def core_jac(x: np.ndarray) -> np.ndarray:
        factor, _ = unpack(x)
        gradients = -matrix_grads(core_matrices, factor).reshape(
            len(core_matrices), -1
        )
        return np.column_stack(
            (gradients, np.zeros((len(gradients), band_count)))
        )

    def arithmetic_fun(x: np.ndarray) -> float:
        factor, _ = unpack(x)
        return matrix_value(arithmetic, factor) - arithmetic_floor

    def arithmetic_jac(x: np.ndarray) -> np.ndarray:
        factor, _ = unpack(x)
        return np.concatenate(
            (
                matrix_grad(arithmetic, factor).reshape(-1),
                np.zeros(band_count),
            )
        )

    constraints: list[dict[str, Any]] = [
        {"type": "ineq", "fun": core_fun, "jac": core_jac},
        {
            "type": "ineq",
            "fun": arithmetic_fun,
            "jac": arithmetic_jac,
        },
        {
            "type": "ineq",
            "fun": lambda x: unpack(x)[1],
            "jac": lambda x: np.column_stack(
                (
                    np.zeros((band_count, dimension * rank)),
                    np.eye(band_count),
                )
            ),
        },
    ]

    for band_index, matrices in enumerate(axis_matrices):
        def band_fun(
            x: np.ndarray,
            band_index: int = band_index,
            matrices: np.ndarray = matrices,
        ) -> np.ndarray:
            factor, bounds = unpack(x)
            return bounds[band_index] - matrix_values(matrices, factor)

        def band_jac(
            x: np.ndarray,
            band_index: int = band_index,
            matrices: np.ndarray = matrices,
        ) -> np.ndarray:
            factor, _ = unpack(x)
            factor_part = -matrix_grads(matrices, factor).reshape(
                len(matrices), -1
            )
            bound_part = np.zeros((len(matrices), band_count))
            bound_part[:, band_index] = 1.0
            return np.column_stack((factor_part, bound_part))

        constraints.append(
            {"type": "ineq", "fun": band_fun, "jac": band_jac}
        )

    best = None
    for initial_factor in initial_factors:
        initial_bounds = np.asarray(
            [
                max(
                    1e-10,
                    1.002
                    * float(np.max(matrix_values(matrices, initial_factor))),
                )
                for matrices in axis_matrices
            ]
        )
        initial = np.concatenate(
            (initial_factor.reshape(-1), initial_bounds)
        )
        result = minimize(
            objective,
            initial,
            jac=objective_jac,
            constraints=constraints,
            method="SLSQP",
            options={"maxiter": maxiter, "ftol": 1e-10, "disp": False},
        )
        factor, bounds = unpack(result.x)
        base_violation = _constraint_violation(
            core_matrices,
            arithmetic,
            arithmetic_floor,
            factor,
        )
        axis_violation = max(
            [
                max(
                    0.0,
                    float(np.max(matrix_values(matrices, factor)))
                    - bounds[index],
                )
                for index, matrices in enumerate(axis_matrices)
            ]
            + [max(0.0, float(-np.min(bounds)))]
        )
        violation = max(base_violation, axis_violation)
        score = objective(result.x)
        if violation <= 2e-5 and (
            best is None or score < best[0]
        ):
            best = (score, result, factor, bounds, violation)
    if best is None:
        raise RuntimeError("No feasible banded factorized stage-one result")

    score, result, factor, bounds, violation = best
    factor_result = FactorizedResult(
        rank=rank,
        factor=factor,
        gram=factor @ factor.T,
        optimizer_success=bool(result.success),
        optimizer_message=str(result.message),
        objective_value=float(score),
        core_max=float(np.max(matrix_values(core_matrices, factor))),
        arithmetic_value=matrix_value(arithmetic, factor),
        iterations=int(result.nit),
        constraint_violation=float(violation),
    )
    tail_value = matrix_value(tail_matrix, factor)
    charges = band_counts * bounds
    return BandedFactorizedResult(
        factor_result=factor_result,
        band_bounds=bounds,
        band_charges=charges,
        tail_value=tail_value,
        majorant_value=float(tail_value + np.sum(charges)),
    )


def solve_banded_factorized_stage_two(
    core_matrices: np.ndarray,
    guard_matrices: np.ndarray,
    axis_matrices: list[np.ndarray],
    band_counts: np.ndarray,
    arithmetic: np.ndarray,
    tail_matrix: np.ndarray,
    arithmetic_floor: float,
    majorant_limit: float,
    initial: BandedFactorizedResult,
    maxiter: int = 2400,
) -> BandedFactorizedResult:
    initial_factor = initial.factor_result.factor
    dimension, rank = initial_factor.shape
    band_count = len(axis_matrices)
    factor_size = dimension * rank

    def unpack(x: np.ndarray) -> tuple[np.ndarray, np.ndarray, float]:
        return (
            x[:factor_size].reshape(dimension, rank),
            x[factor_size : factor_size + band_count],
            float(x[-1]),
        )

    def majorant(factor: np.ndarray, bounds: np.ndarray) -> float:
        return matrix_value(tail_matrix, factor) + float(
            band_counts @ bounds
        )

    def objective(x: np.ndarray) -> float:
        factor, bounds, guard_bound = unpack(x)
        return guard_bound + 1e-10 * majorant(factor, bounds)

    def objective_jac(x: np.ndarray) -> np.ndarray:
        factor, _, _ = unpack(x)
        return np.concatenate(
            (
                1e-10
                * matrix_grad(tail_matrix, factor).reshape(-1),
                1e-10 * band_counts,
                [1.0],
            )
        )

    def append_tail(
        factor_part: np.ndarray,
        band_part: np.ndarray,
        guard_part: np.ndarray,
    ) -> np.ndarray:
        return np.column_stack((factor_part, band_part, guard_part))

    def core_fun(x: np.ndarray) -> np.ndarray:
        factor, _, _ = unpack(x)
        return -1.0 - matrix_values(core_matrices, factor)

    def core_jac(x: np.ndarray) -> np.ndarray:
        factor, _, _ = unpack(x)
        return append_tail(
            -matrix_grads(core_matrices, factor).reshape(
                len(core_matrices), -1
            ),
            np.zeros((len(core_matrices), band_count)),
            np.zeros(len(core_matrices)),
        )

    def guard_fun(x: np.ndarray) -> np.ndarray:
        factor, _, guard_bound = unpack(x)
        return guard_bound - matrix_values(guard_matrices, factor)

    def guard_jac(x: np.ndarray) -> np.ndarray:
        factor, _, _ = unpack(x)
        return append_tail(
            -matrix_grads(guard_matrices, factor).reshape(
                len(guard_matrices), -1
            ),
            np.zeros((len(guard_matrices), band_count)),
            np.ones(len(guard_matrices)),
        )

    def arithmetic_fun(x: np.ndarray) -> float:
        factor, _, _ = unpack(x)
        return matrix_value(arithmetic, factor) - arithmetic_floor

    def arithmetic_jac(x: np.ndarray) -> np.ndarray:
        factor, _, _ = unpack(x)
        return np.concatenate(
            (
                matrix_grad(arithmetic, factor).reshape(-1),
                np.zeros(band_count + 1),
            )
        )

    def majorant_fun(x: np.ndarray) -> float:
        factor, bounds, _ = unpack(x)
        return majorant_limit - majorant(factor, bounds)

    def majorant_jac(x: np.ndarray) -> np.ndarray:
        factor, _, _ = unpack(x)
        return np.concatenate(
            (
                -matrix_grad(tail_matrix, factor).reshape(-1),
                -band_counts,
                [0.0],
            )
        )

    constraints: list[dict[str, Any]] = [
        {"type": "ineq", "fun": core_fun, "jac": core_jac},
        {"type": "ineq", "fun": guard_fun, "jac": guard_jac},
        {
            "type": "ineq",
            "fun": arithmetic_fun,
            "jac": arithmetic_jac,
        },
        {"type": "ineq", "fun": majorant_fun, "jac": majorant_jac},
        {
            "type": "ineq",
            "fun": lambda x: unpack(x)[1],
            "jac": lambda x: append_tail(
                np.zeros((band_count, factor_size)),
                np.eye(band_count),
                np.zeros(band_count),
            ),
        },
        {
            "type": "ineq",
            "fun": lambda x: x[-1],
            "jac": lambda x: np.concatenate(
                (np.zeros(len(x) - 1), [1.0])
            ),
        },
    ]

    for band_index, matrices in enumerate(axis_matrices):
        def band_fun(
            x: np.ndarray,
            band_index: int = band_index,
            matrices: np.ndarray = matrices,
        ) -> np.ndarray:
            factor, bounds, _ = unpack(x)
            return bounds[band_index] - matrix_values(matrices, factor)

        def band_jac(
            x: np.ndarray,
            band_index: int = band_index,
            matrices: np.ndarray = matrices,
        ) -> np.ndarray:
            factor, _, _ = unpack(x)
            band_part = np.zeros((len(matrices), band_count))
            band_part[:, band_index] = 1.0
            return append_tail(
                -matrix_grads(matrices, factor).reshape(
                    len(matrices), -1
                ),
                band_part,
                np.zeros(len(matrices)),
            )

        constraints.append(
            {"type": "ineq", "fun": band_fun, "jac": band_jac}
        )

    initial_guard = max(
        0.0,
        float(
            np.max(
                matrix_values(
                    guard_matrices, initial.factor_result.factor
                )
            )
        ),
    ) + 1e-6
    x0 = np.concatenate(
        (
            initial.factor_result.factor.reshape(-1),
            1.0005 * initial.band_bounds,
            [initial_guard],
        )
    )
    result = minimize(
        objective,
        x0,
        jac=objective_jac,
        constraints=constraints,
        method="SLSQP",
        options={"maxiter": maxiter, "ftol": 1e-10, "disp": False},
    )
    factor, bounds, guard_bound = unpack(result.x)
    base_violation = _constraint_violation(
        core_matrices,
        arithmetic,
        arithmetic_floor,
        factor,
    )
    axis_violation = max(
        [
            max(
                0.0,
                float(np.max(matrix_values(matrices, factor)))
                - bounds[index],
            )
            for index, matrices in enumerate(axis_matrices)
        ]
        + [max(0.0, float(-np.min(bounds)))]
    )
    violation = max(
        base_violation,
        axis_violation,
        max(0.0, majorant(factor, bounds) - majorant_limit),
        max(
            0.0,
            float(np.max(matrix_values(guard_matrices, factor)))
            - guard_bound,
        ),
        max(0.0, -guard_bound),
    )
    if violation > 3e-5:
        raise RuntimeError(
            f"Banded stage-two result violates constraints by {violation}"
        )
    factor_result = FactorizedResult(
        rank=rank,
        factor=factor,
        gram=factor @ factor.T,
        optimizer_success=bool(result.success),
        optimizer_message=str(result.message),
        objective_value=majorant(factor, bounds),
        core_max=float(np.max(matrix_values(core_matrices, factor))),
        arithmetic_value=matrix_value(arithmetic, factor),
        iterations=int(result.nit),
        constraint_violation=float(violation),
    )
    tail_value = matrix_value(tail_matrix, factor)
    charges = band_counts * bounds
    return BandedFactorizedResult(
        factor_result=factor_result,
        band_bounds=bounds,
        band_charges=charges,
        tail_value=tail_value,
        majorant_value=float(tail_value + np.sum(charges)),
        guard_bound=float(guard_bound),
    )


def solve_banded_diagonal_stage_one(
    core_table: np.ndarray,
    axis_tables: list[np.ndarray],
    band_counts: np.ndarray,
    arithmetic: np.ndarray,
    tail: np.ndarray,
    arithmetic_floor: float,
) -> Any:
    candidate_count = len(arithmetic)
    band_count = len(axis_tables)
    rows = [
        np.column_stack((core_table, np.zeros((len(core_table), band_count))))
    ]
    bounds_rhs = [-np.ones(len(core_table))]
    for band_index, table in enumerate(axis_tables):
        band_columns = np.zeros((len(table), band_count))
        band_columns[:, band_index] = -1.0
        rows.append(np.column_stack((table, band_columns)))
        bounds_rhs.append(np.zeros(len(table)))
    rows.append(
        np.concatenate((-arithmetic, np.zeros(band_count)))[None, :]
    )
    bounds_rhs.append(np.asarray([-arithmetic_floor]))
    objective = np.concatenate((tail, band_counts))
    return linprog(
        objective,
        A_ub=np.vstack(rows),
        b_ub=np.concatenate(bounds_rhs),
        bounds=[(0.0, None)] * (candidate_count + band_count),
        method="highs",
    )


def solve_banded_diagonal_stage_two(
    core_table: np.ndarray,
    guard_table: np.ndarray,
    axis_tables: list[np.ndarray],
    band_counts: np.ndarray,
    arithmetic: np.ndarray,
    tail: np.ndarray,
    arithmetic_floor: float,
    majorant_limit: float,
) -> Any:
    candidate_count = len(arithmetic)
    band_count = len(axis_tables)
    total = candidate_count + band_count + 1
    rows = []
    rhs = []

    core_rows = np.zeros((len(core_table), total))
    core_rows[:, :candidate_count] = core_table
    rows.append(core_rows)
    rhs.append(-np.ones(len(core_table)))

    guard_rows = np.zeros((len(guard_table), total))
    guard_rows[:, :candidate_count] = guard_table
    guard_rows[:, -1] = -1.0
    rows.append(guard_rows)
    rhs.append(np.zeros(len(guard_table)))

    for band_index, table in enumerate(axis_tables):
        axis_rows = np.zeros((len(table), total))
        axis_rows[:, :candidate_count] = table
        axis_rows[:, candidate_count + band_index] = -1.0
        rows.append(axis_rows)
        rhs.append(np.zeros(len(table)))

    arithmetic_row = np.zeros(total)
    arithmetic_row[:candidate_count] = -arithmetic
    rows.append(arithmetic_row[None, :])
    rhs.append(np.asarray([-arithmetic_floor]))

    majorant_row = np.zeros(total)
    majorant_row[:candidate_count] = tail
    majorant_row[
        candidate_count : candidate_count + band_count
    ] = band_counts
    rows.append(majorant_row[None, :])
    rhs.append(np.asarray([majorant_limit]))

    objective = np.zeros(total)
    objective[:candidate_count] = 1e-10 * tail
    objective[
        candidate_count : candidate_count + band_count
    ] = 1e-10 * band_counts
    objective[-1] = 1.0
    return linprog(
        objective,
        A_ub=np.vstack(rows),
        b_ub=np.concatenate(rhs),
        bounds=[(0.0, None)] * total,
        method="highs",
    )
