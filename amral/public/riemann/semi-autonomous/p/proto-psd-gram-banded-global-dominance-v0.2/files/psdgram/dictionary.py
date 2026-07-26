from __future__ import annotations

import csv
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
from scipy.integrate import quad

from .cover import Patch
from .model import (
    block_values,
    constrained_whitener,
    fourier_matrix,
    spectral_energy_matrix,
)


@dataclass
class LocalDictionary:
    patch: Patch
    selected_candidate_ids: list[str]
    selected_candidate_indices: list[int]
    raw_reduced: np.ndarray
    raw_coefficients: np.ndarray
    basis_reduced: np.ndarray
    basis_coefficients: np.ndarray
    raw_coordinates: np.ndarray
    parent_gram: np.ndarray
    matrices: dict[str, np.ndarray]
    selection_audit: dict[str, Any]


def load_parent_candidates(path: Path) -> list[dict[str, Any]]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_ordinates(path: Path) -> np.ndarray:
    with path.open(encoding="utf-8") as handle:
        return np.asarray(
            [float(row["ordinate"]) for row in csv.DictReader(handle)]
        )


def _s_bound(t: float) -> float:
    return 0.111 * math.log(t) + 0.275 * math.log(math.log(t)) + 2.450


def tail_multiplier(start: float = 145.0, split: int = 500) -> float:
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


def build_global_matrices(
    model: dict[str, object],
    ordinates: np.ndarray,
) -> tuple[np.ndarray, dict[str, np.ndarray], dict[str, Any]]:
    coordinate_map = constrained_whitener(model)
    arithmetic = (
        coordinate_map.T @ np.asarray(model["q_arithmetic"]) @ coordinate_map
    )
    arithmetic = 0.5 * (arithmetic + arithmetic.T)
    energy, energy_bands = spectral_energy_matrix(model, coordinate_map)

    second = np.asarray(model["basis_second_derivative"])
    weights = np.asarray(model["weights"])
    d2_full = second.T @ (weights[:, None] * second)
    d2 = coordinate_map.T @ d2_full @ coordinate_map
    d2 = 0.5 * (d2 + d2.T)
    tail = (
        tail_multiplier()
        * 2.0
        * float(model["radius"])
        * d2
    )

    zero_transform = (
        fourier_matrix(ordinates.astype(complex), model) @ coordinate_map
    ).real
    known_zero = zero_transform.T @ zero_transform
    first_zero = np.outer(zero_transform[0], zero_transform[0])

    matrices = {
        "arithmetic": arithmetic,
        "axis_energy": 0.5 * (energy + energy.T),
        "d2": d2,
        "tail": 0.5 * (tail + tail.T),
        "proxy": 0.5 * (energy + energy.T + tail + tail.T),
        "known_zero": 0.5 * (known_zero + known_zero.T),
        "first_zero": 0.5 * (first_zero + first_zero.T),
    }
    metadata = {
        "coordinate_dimension": int(coordinate_map.shape[1]),
        "axis_energy_bands": energy_bands,
        "tail_multiplier": tail_multiplier(),
        "tail_model": (
            "2R * integral |psi''|^2 times a conservative t^-4 "
            "zero-density profile"
        ),
    }
    return coordinate_map, matrices, metadata


def gram_block_matrices(
    points: np.ndarray,
    model: dict[str, object],
    basis_coefficients: np.ndarray,
) -> np.ndarray:
    transform = fourier_matrix(points, model) @ basis_coefficients
    return np.asarray(
        [2.0 * np.real(np.outer(row, row)) for row in transform]
    )


def _candidate_core_metrics(
    patch: Patch,
    candidates: list[dict[str, Any]],
    model: dict[str, object],
) -> tuple[np.ndarray, np.ndarray]:
    points = patch.points(9, 7)
    coefficient_matrix = np.column_stack(
        [np.asarray(item["coefficients"], dtype=float) for item in candidates]
    )
    transform = fourier_matrix(points, model) @ coefficient_matrix
    blocks = 2.0 * np.real(transform * transform)
    worst = np.max(blocks, axis=0)
    energy = np.asarray(
        [float(item["axis_band_energy"]) for item in candidates]
    )
    ratio = np.full(len(candidates), np.inf)
    negative = worst < -1e-14
    ratio[negative] = energy[negative] / (-worst[negative])
    return worst, ratio


def _mandatory_candidate_ids(parent_certificate: dict[str, Any]) -> list[str]:
    ids = [
        item["candidate_id"]
        for item in parent_certificate["active_candidates"]
    ]
    baseline = parent_certificate.get("single_candidate_baseline")
    if baseline:
        ids.append(baseline["candidate_id"])
    return list(dict.fromkeys(ids))


def _select_diverse_indices(
    candidates: list[dict[str, Any]],
    ratio: np.ndarray,
    mandatory_ids: list[str],
    maximum_size: int,
) -> tuple[list[int], dict[str, Any]]:
    by_id = {
        item["candidate_id"]: index
        for index, item in enumerate(candidates)
    }
    ranked = [
        int(index)
        for index in np.argsort(ratio)
        if np.isfinite(ratio[index])
    ]
    pool = list(dict.fromkeys(
        [by_id[item] for item in mandatory_ids if item in by_id]
        + ranked[:32]
    ))
    selected: list[int] = []
    orthonormal: list[np.ndarray] = []

    def add(index: int, force: bool = False) -> bool:
        vector = np.asarray(
            candidates[index]["reduced_coefficients"], dtype=float
        )
        residual = vector.copy()
        for direction in orthonormal:
            residual -= direction * float(direction @ residual)
        norm = float(np.linalg.norm(residual))
        if norm < 1e-7 and not force:
            return False
        selected.append(index)
        if norm >= 1e-7:
            orthonormal.append(residual / norm)
        return True

    for candidate_id in mandatory_ids:
        if candidate_id in by_id and len(selected) < maximum_size:
            add(by_id[candidate_id])

    while len(selected) < maximum_size:
        best = None
        for pool_rank, index in enumerate(pool):
            if index in selected:
                continue
            vector = np.asarray(
                candidates[index]["reduced_coefficients"], dtype=float
            )
            residual = vector.copy()
            for direction in orthonormal:
                residual -= direction * float(direction @ residual)
            residual_norm = float(np.linalg.norm(residual))
            score = residual_norm / (1.0 + 0.08 * pool_rank)
            if best is None or score > best[0]:
                best = (score, index, residual_norm)
        if best is None or best[2] < 1e-5:
            break
        add(best[1])

    audit = {
        "mandatory_candidate_ids": mandatory_ids,
        "pool_size": len(pool),
        "requested_dictionary_size": maximum_size,
        "selected_raw_count": len(selected),
        "selected_ids": [
            candidates[index]["candidate_id"] for index in selected
        ],
        "selected_core_energy_ratios": [
            float(ratio[index]) for index in selected
        ],
    }
    return selected, audit


def _orthonormal_span(raw_reduced: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    gram = raw_reduced.T @ raw_reduced
    values, vectors = np.linalg.eigh(0.5 * (gram + gram.T))
    threshold = max(1e-11, 1e-9 * float(np.max(values)))
    keep = values > threshold
    basis = (
        raw_reduced
        @ vectors[:, keep]
        @ np.diag(1.0 / np.sqrt(values[keep]))
    )
    coordinates = basis.T @ raw_reduced
    return basis, coordinates


def build_local_dictionary(
    patch: Patch,
    candidates: list[dict[str, Any]],
    parent_certificate: dict[str, Any],
    model: dict[str, object],
    coordinate_map: np.ndarray,
    global_matrices: dict[str, np.ndarray],
    maximum_size: int = 8,
) -> LocalDictionary:
    worst, ratio = _candidate_core_metrics(patch, candidates, model)
    mandatory_ids = _mandatory_candidate_ids(parent_certificate)
    indices, audit = _select_diverse_indices(
        candidates, ratio, mandatory_ids, maximum_size
    )
    raw_reduced = np.column_stack(
        [
            np.asarray(candidates[index]["reduced_coefficients"], dtype=float)
            for index in indices
        ]
    )
    raw_coefficients = np.column_stack(
        [
            np.asarray(candidates[index]["coefficients"], dtype=float)
            for index in indices
        ]
    )
    basis_reduced, coordinates = _orthonormal_span(raw_reduced)
    basis_coefficients = coordinate_map @ basis_reduced
    local_matrices = {
        name: basis_reduced.T @ matrix @ basis_reduced
        for name, matrix in global_matrices.items()
    }
    local_matrices = {
        name: 0.5 * (matrix + matrix.T)
        for name, matrix in local_matrices.items()
    }

    coordinate_by_id = {
        candidates[index]["candidate_id"]: coordinates[:, position]
        for position, index in enumerate(indices)
    }
    parent_gram = np.zeros(
        (basis_reduced.shape[1], basis_reduced.shape[1])
    )
    omitted_parent_ids = []
    for item in parent_certificate["active_candidates"]:
        candidate_id = item["candidate_id"]
        if candidate_id not in coordinate_by_id:
            omitted_parent_ids.append(candidate_id)
            continue
        vector = coordinate_by_id[candidate_id]
        parent_gram += float(item["weight"]) * np.outer(vector, vector)
    audit.update(
        {
            "span_dimension": int(basis_reduced.shape[1]),
            "raw_gram_condition_nonzero": float(
                np.max(np.linalg.eigvalsh(raw_reduced.T @ raw_reduced))
                / max(
                    1e-16,
                    np.min(
                        np.linalg.eigvalsh(raw_reduced.T @ raw_reduced)[
                            np.linalg.eigvalsh(raw_reduced.T @ raw_reduced)
                            > 1e-11
                        ]
                    ),
                )
            ),
            "omitted_parent_active_ids": omitted_parent_ids,
            "fit_core_worst_by_selected_id": {
                candidates[index]["candidate_id"]: float(worst[index])
                for index in indices
            },
        }
    )
    return LocalDictionary(
        patch=patch,
        selected_candidate_ids=[
            candidates[index]["candidate_id"] for index in indices
        ],
        selected_candidate_indices=indices,
        raw_reduced=raw_reduced,
        raw_coefficients=raw_coefficients,
        basis_reduced=basis_reduced,
        basis_coefficients=basis_coefficients,
        raw_coordinates=coordinates,
        parent_gram=parent_gram,
        matrices=local_matrices,
        selection_audit=audit,
    )


def matrix_value(matrix: np.ndarray, gram: np.ndarray) -> float:
    return float(np.sum(matrix * gram))


def evaluate_gram_blocks(
    points: np.ndarray,
    gram: np.ndarray,
    model: dict[str, object],
    basis_coefficients: np.ndarray,
) -> np.ndarray:
    matrices = gram_block_matrices(points, model, basis_coefficients)
    return np.einsum("kij,ij->k", matrices, gram)


def raw_diagonal_tables(
    points: np.ndarray,
    dictionary: LocalDictionary,
    model: dict[str, object],
) -> np.ndarray:
    return np.column_stack(
        [
            block_values(
                points,
                dictionary.raw_coefficients[:, index],
                model,
            )
            for index in range(dictionary.raw_coefficients.shape[1])
        ]
    )
