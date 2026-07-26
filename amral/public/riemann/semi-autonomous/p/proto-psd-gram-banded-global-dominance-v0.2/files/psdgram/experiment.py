from __future__ import annotations

import json
import math
from dataclasses import asdict
from pathlib import Path
from typing import Any

import numpy as np

from .axis import (
    AxisBand,
    axis_gram_matrices,
    band_grids,
    default_axis_bands,
)
from .cover import Patch
from .dictionary import (
    build_global_matrices,
    gram_block_matrices,
    load_ordinates,
    load_parent_candidates,
    matrix_value as gram_matrix_value,
)
from .model import build_model, fourier_matrix
from .solver import (
    BandedFactorizedResult,
    factor_from_gram,
    matrix_value,
    matrix_values,
    solve_banded_diagonal_stage_one,
    solve_banded_diagonal_stage_two,
    solve_banded_factorized_stage_one,
    solve_banded_factorized_stage_two,
)


class ExperimentContext:
    def __init__(self, root: Path):
        self.root = root
        self.model = build_model()
        self.ordinates = load_ordinates(
            root / "data" / "first_50_ordinates.csv"
        )
        (
            self.coordinate_map,
            self.global_matrices,
            self.global_metadata,
        ) = build_global_matrices(self.model, self.ordinates)
        self.candidates = load_parent_candidates(
            root / "data" / "parent_candidate_library.json"
        )
        self.candidate_by_id = {
            item["candidate_id"]: item for item in self.candidates
        }
        self.reduced_candidates = np.column_stack(
            [
                np.asarray(item["reduced_coefficients"], dtype=float)
                for item in self.candidates
            ]
        )
        self.full_candidates = (
            self.coordinate_map @ self.reduced_candidates
        )
        self.candidate_arithmetic = np.einsum(
            "ik,ij,jk->k",
            self.reduced_candidates,
            self.global_matrices["arithmetic"],
            self.reduced_candidates,
        )
        self.candidate_tail = np.einsum(
            "ik,ij,jk->k",
            self.reduced_candidates,
            self.global_matrices["tail"],
            self.reduced_candidates,
        )
        self.bands = default_axis_bands()
        self.band_counts = np.asarray(
            [band.count_majorant for band in self.bands]
        )
        self.axis_active_grids = band_grids(self.bands, 0.5)
        self.axis_dense_grids = band_grids(self.bands, 0.05)
        self.axis_dense_step = 0.05

    def parent_certificate(self, patch_id: str) -> dict[str, Any]:
        return json.loads(
            (
                self.root
                / "data"
                / "parent_certificates"
                / f"{patch_id}.certificate.json"
            ).read_text(encoding="utf-8")
        )

    def parent_gram(self, patch_id: str) -> np.ndarray:
        certificate = self.parent_certificate(patch_id)
        gram = np.zeros(
            (
                self.coordinate_map.shape[1],
                self.coordinate_map.shape[1],
            )
        )
        for item in certificate["active_candidates"]:
            vector = np.asarray(
                self.candidate_by_id[item["candidate_id"]][
                    "reduced_coefficients"
                ],
                dtype=float,
            )
            gram += float(item["weight"]) * np.outer(vector, vector)
        return gram


def _candidate_table(
    points: np.ndarray,
    context: ExperimentContext,
    orbit_block: bool,
) -> np.ndarray:
    transform = fourier_matrix(points, context.model) @ context.full_candidates
    if orbit_block:
        return 2.0 * np.real(transform * transform)
    return np.real(transform) ** 2


def _gram_transform(
    points: np.ndarray,
    context: ExperimentContext,
) -> np.ndarray:
    return fourier_matrix(points, context.model) @ context.coordinate_map


def _gram_values(
    transform: np.ndarray,
    gram: np.ndarray,
    orbit_block: bool,
) -> np.ndarray:
    values = np.einsum("ki,ij,kj->k", transform, gram, transform)
    return 2.0 * np.real(values) if orbit_block else np.real(values)


def _matrix_from_transform(
    vector: np.ndarray,
    orbit_block: bool,
) -> np.ndarray:
    matrix = np.outer(vector, vector)
    return 2.0 * np.real(matrix) if orbit_block else np.real(matrix)


def _parent_factor_starts(
    parent_gram: np.ndarray,
    rank: int,
    core_matrices: np.ndarray,
    random_seed: int,
) -> list[np.ndarray]:
    base = factor_from_gram(parent_gram, rank, core_matrices)
    starts = [base]
    rng = np.random.default_rng(random_seed)
    for epsilon in (0.002, 0.008, 0.025, 0.06):
        trial = base.copy()
        trial += (
            epsilon
            * np.linalg.norm(base)
            * rng.normal(size=trial.shape)
            / np.sqrt(trial.size)
        )
        worst = float(np.max(matrix_values(core_matrices, trial)))
        if worst < 0.0:
            trial *= np.sqrt(1.005 / (-worst))
            starts.append(trial)
    return starts


def _canonical_factor(gram: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(0.5 * (gram + gram.T))
    keep = values > max(1e-12, 1e-9 * float(np.max(values)))
    return vectors[:, keep] * np.sqrt(values[keep])[None, :]


def _lipschitz_audits(
    patch: Patch,
    gram: np.ndarray,
    dense_core_max: float,
    axis_sampled_maxima: np.ndarray,
    context: ExperimentContext,
) -> dict[str, Any]:
    factor = _canonical_factor(gram)
    coefficients = context.coordinate_map @ factor
    t = np.asarray(context.model["t"])
    weights = np.asarray(context.model["weights"])
    basis = np.asarray(context.model["basis"])
    core_lipschitz = 0.0
    core_hessian_bound = 0.0
    axis_lipschitz = 0.0
    axis_second_derivative_bound = 0.0
    for column in range(coefficients.shape[1]):
        psi = basis @ coefficients[:, column]
        l1 = float(np.sum(weights * np.abs(psi)))
        first = float(np.sum(weights * np.abs(t * psi)))
        second = float(np.sum(weights * np.abs(t * t * psi)))
        axis_lipschitz += 2.0 * l1 * first
        axis_second_derivative_bound += 2.0 * (
            first * first + l1 * second
        )
        core_lipschitz += (
            4.0
            * math.exp(
                2.0
                * float(context.model["radius"])
                * abs(patch.y_min)
            )
            * l1
            * first
        )
        core_hessian_bound += (
            4.0
            * math.exp(
                2.0
                * float(context.model["radius"])
                * abs(patch.y_min)
            )
            * (first * first + l1 * second)
        )

    weighted_psi = (
        weights[:, None] * (basis @ coefficients)
    )
    weighted_psi_prime = 1j * t[:, None] * weighted_psi

    def transforms(points: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        points = np.asarray(points, dtype=complex).reshape(-1)
        values = np.empty(
            (len(points), coefficients.shape[1]), dtype=complex
        )
        derivatives = np.empty_like(values)
        for start in range(0, len(points), 256):
            stop = min(start + 256, len(points))
            exponential = np.exp(
                1j * np.outer(points[start:stop], t)
            )
            values[start:stop] = exponential @ weighted_psi
            derivatives[start:stop] = (
                exponential @ weighted_psi_prime
            )
        return values, derivatives

    core_dx = (patch.x_max - patch.x_min) / 160.0
    core_dy = (patch.y_max - patch.y_min) / 120.0
    core_crude_upper = dense_core_max + core_lipschitz * (
        core_dx + core_dy
    ) / 2.0

    core_values, core_derivatives = transforms(
        patch.points(161, 121)
    )
    sampled_dx = 4.0 * np.real(
        np.sum(core_values * core_derivatives, axis=1)
    )
    sampled_dy = 4.0 * np.real(
        np.sum(core_values * (1j * core_derivatives), axis=1)
    )
    core_cell_l1_radius = (core_dx + core_dy) / 2.0
    refined_dx_bound = (
        float(np.max(np.abs(sampled_dx)))
        + core_hessian_bound * core_cell_l1_radius
    )
    refined_dy_bound = (
        float(np.max(np.abs(sampled_dy)))
        + core_hessian_bound * core_cell_l1_radius
    )
    core_refined_upper = (
        dense_core_max
        + refined_dx_bound * core_dx / 2.0
        + refined_dy_bound * core_dy / 2.0
    )

    axis_crude_corrected = (
        axis_sampled_maxima
        + axis_lipschitz * context.axis_dense_step / 2.0
    )
    axis_sampled_derivative_maxima = []
    axis_refined_corrected = []
    for sampled_maximum, grid in zip(
        axis_sampled_maxima, context.axis_dense_grids
    ):
        axis_values, axis_derivatives = transforms(
            grid.astype(complex)
        )
        sampled_derivative = 2.0 * np.real(
            np.sum(
                np.conjugate(axis_values) * axis_derivatives,
                axis=1,
            )
        )
        derivative_maximum = float(
            np.max(np.abs(sampled_derivative))
        )
        half_step = (
            float(np.max(np.diff(grid))) / 2.0
            if len(grid) > 1
            else 0.0
        )
        local_derivative_bound = (
            derivative_maximum
            + axis_second_derivative_bound * half_step
        )
        axis_sampled_derivative_maxima.append(derivative_maximum)
        axis_refined_corrected.append(
            float(sampled_maximum + local_derivative_bound * half_step)
        )

    return {
        "canonical_factor_rank": int(factor.shape[1]),
        "core_lipschitz": core_lipschitz,
        "core_crude_continuous_upper": float(core_crude_upper),
        "core_crude_continuous_sign_pass": bool(
            core_crude_upper < 0.0
        ),
        "core_hessian_bound": core_hessian_bound,
        "core_sampled_dx_max": float(np.max(np.abs(sampled_dx))),
        "core_sampled_dy_max": float(np.max(np.abs(sampled_dy))),
        "core_refined_dx_bound": refined_dx_bound,
        "core_refined_dy_bound": refined_dy_bound,
        "core_refined_continuous_upper": float(
            core_refined_upper
        ),
        "core_refined_continuous_sign_pass": bool(
            core_refined_upper < 0.0
        ),
        "axis_lipschitz": axis_lipschitz,
        "axis_second_derivative_bound": axis_second_derivative_bound,
        "axis_sampled_derivative_maxima": (
            axis_sampled_derivative_maxima
        ),
        "axis_crude_corrected_suprema": (
            axis_crude_corrected.tolist()
        ),
        "axis_corrected_suprema": axis_refined_corrected,
        "axis_lipschitz_correction_per_band": float(
            axis_lipschitz * context.axis_dense_step / 2.0
        ),
    }


def evaluate_gram_candidate(
    patch: Patch,
    gram: np.ndarray,
    context: ExperimentContext,
    method: str,
    requested_rank: int | None,
    optimizer: dict[str, Any],
) -> dict[str, Any]:
    dense_core_points = patch.points(161, 121)
    dense_core_transform = _gram_transform(dense_core_points, context)
    dense_core = _gram_values(
        dense_core_transform, gram, orbit_block=True
    )
    guard_points = patch.guard_ring(49, 37)
    guard_transform = _gram_transform(guard_points, context)
    guard = _gram_values(guard_transform, gram, orbit_block=True)

    axis_maxima = []
    axis_argmax = []
    for band, grid in zip(context.bands, context.axis_dense_grids):
        transform = _gram_transform(grid.astype(complex), context).real
        values = _gram_values(transform, gram, orbit_block=False)
        index = int(np.argmax(values))
        axis_maxima.append(float(values[index]))
        axis_argmax.append(float(grid[index]))
    axis_maxima_array = np.asarray(axis_maxima)
    axis_charges = context.band_counts * axis_maxima_array

    arithmetic = gram_matrix_value(
        context.global_matrices["arithmetic"], gram
    )
    tail = gram_matrix_value(context.global_matrices["tail"], gram)
    known = gram_matrix_value(
        context.global_matrices["known_zero"], gram
    )
    first = gram_matrix_value(
        context.global_matrices["first_zero"], gram
    )
    axis_energy = gram_matrix_value(
        context.global_matrices["axis_energy"], gram
    )
    sampled_majorant = float(tail + np.sum(axis_charges))
    guard_positive = max(0.0, float(np.max(guard)))
    partial_gap = 1.0 - sampled_majorant - guard_positive
    eigenvalues = np.linalg.eigvalsh(0.5 * (gram + gram.T))
    max_eigenvalue = float(np.max(eigenvalues))
    numerical_rank = int(
        np.sum(eigenvalues > max(1e-10, 1e-7 * max_eigenvalue))
    )
    off_diagonal = gram - np.diag(np.diag(gram))
    off_diagonal_fraction = float(
        np.linalg.norm(off_diagonal)
        / max(1e-16, np.linalg.norm(gram))
    )
    lipschitz = _lipschitz_audits(
        patch,
        gram,
        float(np.max(dense_core)),
        axis_maxima_array,
        context,
    )
    corrected_axis_charges = (
        context.band_counts
        * np.asarray(lipschitz["axis_corrected_suprema"])
    )
    corrected_majorant = float(tail + np.sum(corrected_axis_charges))
    corrected_gap = 1.0 - corrected_majorant - guard_positive

    return {
        "patch_id": patch.patch_id,
        "method": method,
        "requested_rank": requested_rank,
        "numerical_rank": numerical_rank,
        "gram_min_eigenvalue": float(np.min(eigenvalues)),
        "gram_max_eigenvalue": max_eigenvalue,
        "off_diagonal_frobenius_fraction": off_diagonal_fraction,
        "arithmetic_value": arithmetic,
        "dense_core_max": float(np.max(dense_core)),
        "dense_core_min": float(np.min(dense_core)),
        "guard_positive_max": guard_positive,
        "axis_band_energy_integral_proxy": axis_energy,
        "axis_bands": [
            {
                **asdict(band),
                "sampled_supremum": axis_maxima[index],
                "sampled_argmax": axis_argmax[index],
                "sampled_charge": float(axis_charges[index]),
                "lipschitz_corrected_supremum": lipschitz[
                    "axis_corrected_suprema"
                ][index],
                "lipschitz_corrected_charge": float(
                    corrected_axis_charges[index]
                ),
            }
            for index, band in enumerate(context.bands)
        ],
        "sampled_axis_prefix_majorant": float(np.sum(axis_charges)),
        "tail_majorant": tail,
        "sampled_axis_plus_tail_majorant": sampled_majorant,
        "lipschitz_corrected_axis_plus_tail_majorant": corrected_majorant,
        "known_first_50_holdout_mass": known,
        "first_zero_holdout_mass": first,
        "sampled_partial_gap_excluding_unknown_off_axis": partial_gap,
        "lipschitz_corrected_partial_gap_excluding_unknown_off_axis": corrected_gap,
        "sampled_partial_budget_pass": bool(partial_gap > 0.0),
        "lipschitz_corrected_partial_budget_pass": bool(
            corrected_gap > 0.0
        ),
        "global_certificate_pass": False,
        "lipschitz_audit": lipschitz,
        "optimizer": optimizer,
        "gram": gram.tolist(),
        "trust_boundary": (
            "E2 floating factorized search and sampled band majorant. "
            "No convex-global optimality, interval enclosure, zero-presence "
            "certificate, or unknown off-axis budget is asserted."
        ),
    }


def run_diagonal_patch(
    patch: Patch,
    context: ExperimentContext,
    objective_slack: float = 0.05,
    max_rounds: int = 10,
) -> dict[str, Any]:
    core_active = _candidate_table(
        patch.points(9, 7), context, orbit_block=True
    )
    dense_core = _candidate_table(
        patch.points(161, 121), context, orbit_block=True
    )
    axis_active = [
        _candidate_table(grid.astype(complex), context, orbit_block=False)
        for grid in context.axis_active_grids
    ]
    axis_dense = [
        _candidate_table(grid.astype(complex), context, orbit_block=False)
        for grid in context.axis_dense_grids
    ]
    guard = _candidate_table(
        patch.guard_ring(49, 37), context, orbit_block=True
    )
    history = []
    stage_two = None
    stage_one = None

    for round_index in range(max_rounds):
        stage_one = solve_banded_diagonal_stage_one(
            core_active,
            axis_active,
            context.band_counts,
            context.candidate_arithmetic,
            context.candidate_tail,
            1e-3,
        )
        if not stage_one.success:
            raise RuntimeError(
                f"{patch.patch_id}: diagonal stage one failed"
            )
        stage_two = solve_banded_diagonal_stage_two(
            core_active,
            guard,
            axis_active,
            context.band_counts,
            context.candidate_arithmetic,
            context.candidate_tail,
            1e-3,
            (1.0 + objective_slack) * float(stage_one.fun),
        )
        if not stage_two.success:
            raise RuntimeError(
                f"{patch.patch_id}: diagonal stage two failed"
            )
        weights = stage_two.x[: len(context.candidates)]
        bounds = stage_two.x[
            len(context.candidates) : len(context.candidates)
            + len(context.bands)
        ]
        core_values = dense_core @ weights
        worst_core_index = int(np.argmax(core_values))
        core_violation = float(core_values[worst_core_index] + 1.0)
        axis_violations = []
        for band_index, table in enumerate(axis_dense):
            values = table @ weights
            worst_index = int(np.argmax(values))
            axis_violations.append(
                (
                    float(values[worst_index] - bounds[band_index]),
                    band_index,
                    worst_index,
                )
            )
        worst_axis = max(axis_violations)
        history.append(
            {
                "round": round_index,
                "stage_one_majorant": float(stage_one.fun),
                "stage_two_guard_bound": float(stage_two.x[-1]),
                "dense_core_violation": core_violation,
                "dense_axis_violation": worst_axis[0],
            }
        )
        if core_violation <= 2e-7 and worst_axis[0] <= 2e-7:
            break
        if core_violation > 2e-7:
            core_active = np.vstack(
                (core_active, dense_core[worst_core_index])
            )
        for violation, band_index, worst_index in axis_violations:
            if violation > 2e-7:
                axis_active[band_index] = np.vstack(
                    (
                        axis_active[band_index],
                        axis_dense[band_index][worst_index],
                    )
                )

    if stage_two is None or stage_one is None:
        raise RuntimeError("No diagonal result")
    weights = stage_two.x[: len(context.candidates)]
    gram = (
        context.reduced_candidates
        @ np.diag(weights)
        @ context.reduced_candidates.T
    )
    active = np.flatnonzero(
        weights > max(1e-10, 1e-8 * float(np.max(weights)))
    )
    return evaluate_gram_candidate(
        patch,
        gram,
        context,
        method="diagonal_72_ray_cone",
        requested_rank=None,
        optimizer={
            "stage_one_lp_success": bool(stage_one.success),
            "stage_one_sampled_majorant": float(stage_one.fun),
            "stage_two_lp_success": bool(stage_two.success),
            "stage_two_guard_bound": float(stage_two.x[-1]),
            "objective_slack": objective_slack,
            "active_candidate_count": int(len(active)),
            "active_candidates": [
                {
                    "candidate_id": context.candidates[index][
                        "candidate_id"
                    ],
                    "weight": float(weights[index]),
                }
                for index in active
            ],
            "exchange_history": history,
        },
    )


def run_factorized_patch(
    patch: Patch,
    rank: int,
    context: ExperimentContext,
    objective_slack: float = 0.05,
    max_rounds: int = 10,
    random_seed: int = 20260724,
) -> dict[str, Any]:
    fit_transform = _gram_transform(patch.points(9, 7), context)
    core_active = np.asarray(
        [
            _matrix_from_transform(row, orbit_block=True)
            for row in fit_transform
        ]
    )
    dense_core_transform = _gram_transform(
        patch.points(161, 121), context
    )
    guard_transform = _gram_transform(
        patch.guard_ring(49, 37), context
    )
    guard_matrices = np.asarray(
        [
            _matrix_from_transform(row, orbit_block=True)
            for row in guard_transform
        ]
    )
    axis_active = axis_gram_matrices(
        context.axis_active_grids,
        context.model,
        context.coordinate_map,
    )
    axis_dense_transform = [
        _gram_transform(grid.astype(complex), context).real
        for grid in context.axis_dense_grids
    ]
    parent_gram = context.parent_gram(patch.patch_id)
    starts = _parent_factor_starts(
        parent_gram,
        rank,
        core_active,
        random_seed + sum(ord(ch) for ch in patch.patch_id) + rank,
    )
    history = []
    stage_one = None
    stage_two = None

    for round_index in range(max_rounds):
        stage_one = solve_banded_factorized_stage_one(
            core_active,
            axis_active,
            context.band_counts,
            context.global_matrices["arithmetic"],
            context.global_matrices["tail"],
            1e-3,
            starts,
        )
        stage_two = solve_banded_factorized_stage_two(
            core_active,
            guard_matrices,
            axis_active,
            context.band_counts,
            context.global_matrices["arithmetic"],
            context.global_matrices["tail"],
            1e-3,
            (1.0 + objective_slack) * stage_one.majorant_value,
            stage_one,
        )
        selected_gram = stage_two.factor_result.gram
        core_values = _gram_values(
            dense_core_transform,
            selected_gram,
            orbit_block=True,
        )
        worst_core_index = int(np.argmax(core_values))
        core_violation = float(core_values[worst_core_index] + 1.0)
        axis_violations = []
        for band_index, transform in enumerate(axis_dense_transform):
            values = _gram_values(
                transform, selected_gram, orbit_block=False
            )
            worst_index = int(np.argmax(values))
            axis_violations.append(
                (
                    float(
                        values[worst_index]
                        - stage_two.band_bounds[band_index]
                    ),
                    band_index,
                    worst_index,
                )
            )
        worst_axis = max(axis_violations)
        history.append(
            {
                "round": round_index,
                "stage_one_majorant": stage_one.majorant_value,
                "stage_two_majorant": stage_two.majorant_value,
                "stage_two_guard_bound": stage_two.guard_bound,
                "dense_core_violation": core_violation,
                "dense_axis_violation": worst_axis[0],
                "stage_one_success": stage_one.factor_result.optimizer_success,
                "stage_two_success": stage_two.factor_result.optimizer_success,
            }
        )
        if core_violation <= 3e-7 and worst_axis[0] <= 3e-7:
            break
        if core_violation > 3e-7:
            core_active = np.concatenate(
                (
                    core_active,
                    _matrix_from_transform(
                        dense_core_transform[worst_core_index],
                        orbit_block=True,
                    )[None, :, :],
                )
            )
        for violation, band_index, worst_index in axis_violations:
            if violation > 3e-7:
                axis_active[band_index] = np.concatenate(
                    (
                        axis_active[band_index],
                        _matrix_from_transform(
                            axis_dense_transform[band_index][worst_index],
                            orbit_block=False,
                        )[None, :, :],
                    )
                )
        starts = [stage_two.factor_result.factor]
        rng = np.random.default_rng(
            random_seed + round_index + rank * 101
        )
        for epsilon in (0.002, 0.01):
            trial = stage_two.factor_result.factor.copy()
            trial += (
                epsilon
                * np.linalg.norm(trial)
                * rng.normal(size=trial.shape)
                / np.sqrt(trial.size)
            )
            worst = float(np.max(matrix_values(core_active, trial)))
            if worst < 0.0:
                trial *= np.sqrt(1.003 / (-worst))
                starts.append(trial)

    if stage_two is None or stage_one is None:
        raise RuntimeError("No factorized result")
    return evaluate_gram_candidate(
        patch,
        stage_two.factor_result.gram,
        context,
        method="factorized_full_22d_psd_gram",
        requested_rank=rank,
        optimizer={
            "solver": "SciPy SLSQP on A=L L^T",
            "convex_global_optimality_claimed": False,
            "stage_one_success": stage_one.factor_result.optimizer_success,
            "stage_one_message": stage_one.factor_result.optimizer_message,
            "stage_one_sampled_majorant": stage_one.majorant_value,
            "stage_two_success": stage_two.factor_result.optimizer_success,
            "stage_two_message": stage_two.factor_result.optimizer_message,
            "stage_two_sampled_majorant": stage_two.majorant_value,
            "stage_two_guard_bound": stage_two.guard_bound,
            "objective_slack": objective_slack,
            "exchange_history": history,
        },
    )
