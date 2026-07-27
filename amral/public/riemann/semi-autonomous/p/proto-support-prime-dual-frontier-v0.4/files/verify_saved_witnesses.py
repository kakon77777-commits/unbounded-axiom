from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

import numpy as np

from frontier.context import FrontierContext


ROOT = Path(__file__).resolve().parent


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def reconstruct_sparse_witness(
    payload: dict[str, Any],
    context: FrontierContext,
) -> dict[str, Any]:
    joint = payload["joint_dual"]
    base = context.tail_matrix.copy()
    raw_axis_weight_sums = []
    for band_index, support in enumerate(joint["axis_supports"]):
        raw_weights = np.asarray(
            [row["weight"] for row in support],
            dtype=float,
        )
        raw_sum = float(np.sum(raw_weights))
        weights = raw_weights / raw_sum
        points = np.asarray(
            [row["x"] for row in support],
            dtype=float,
        )
        transforms = context.axis_transforms(points)
        matrices = np.einsum(
            "ki,kj->kij",
            transforms,
            transforms,
        )
        base += (
            context.count_coefficients[band_index]
            * np.tensordot(weights, matrices, axes=1)
        )
        raw_axis_weight_sums.append(raw_sum)

    core_support = joint["core_support"]
    raw_core_weights = np.asarray(
        [row["weight"] for row in core_support],
        dtype=float,
    )
    raw_core_weight_sum = float(np.sum(raw_core_weights))
    core_weights = raw_core_weights / raw_core_weight_sum
    core_points = np.asarray(
        [
            complex(row["x"], row["y"])
            for row in core_support
        ],
        dtype=complex,
    )
    core_matrices = context.core_matrices(core_points)
    core = np.tensordot(core_weights, core_matrices, axes=1)
    safe_alpha = float(joint["safe_alpha"])
    witness = base + safe_alpha * core
    witness = 0.5 * (witness + witness.T)
    minimum = float(np.linalg.eigvalsh(witness)[0])
    return {
        "minimum_eigenvalue": minimum,
        "normalization_convention": (
            "Every serialized nonnegative support group is divided "
            "by its serialized weight sum before reconstruction."
        ),
        "raw_axis_weight_sums": raw_axis_weight_sums,
        "raw_core_weight_sum": raw_core_weight_sum,
        "normalized_axis_weight_sums": [
            1.0 for _ in raw_axis_weight_sums
        ],
        "normalized_core_weight_sum": 1.0,
        "effective_lower_bound": safe_alpha,
        "serialized_sparse_witness_psd": minimum >= -1e-10,
        "serialized_measure_budget_block": (
            minimum >= -1e-10
            and np.min(raw_core_weights) >= -1e-12
            and all(
                np.min(
                    np.asarray(
                        [row["weight"] for row in support],
                        dtype=float,
                    )
                )
                >= -1e-12
                for support in joint["axis_supports"]
            )
            and safe_alpha > 1.0
        ),
    }


def verify_all_saved_witnesses() -> dict[str, Any]:
    summary = read_json(ROOT / "outputs" / "joint_dual_summary.json")
    expected_paths = sorted(
        ROOT / row["witness_file"]
        for radius_row in summary["radius_rows"]
        for row in radius_row["candidate_rows"]
    )
    actual_paths = sorted(
        (ROOT / "outputs" / "witnesses").glob("*.witness.json")
    )
    contexts: dict[tuple[float, float, float], FrontierContext] = {}
    rows = []
    for path in expected_paths:
        payload = read_json(path)
        configuration = payload["configuration"]
        key = (
            float(configuration["radius"]),
            float(configuration["density"]),
            float(configuration["width_factor"]),
        )
        if key not in contexts:
            contexts[key] = FrontierContext(
                radius=key[0],
                density=key[1],
                width_factor=key[2],
            )
        reconstructed = reconstruct_sparse_witness(
            payload,
            contexts[key],
        )
        stored_minimum = float(
            payload["joint_dual"]["safe_min_eigenvalue"]
        )
        rows.append(
            {
                "witness_file": str(path.relative_to(ROOT)),
                "sha256": sha256(path),
                "radius": key[0],
                "patch_id": payload["patch"]["patch_id"],
                "stored_safe_min_eigenvalue": stored_minimum,
                "reconstructed": reconstructed,
                "minimum_eigenvalue_abs_difference": abs(
                    reconstructed["minimum_eigenvalue"]
                    - stored_minimum
                ),
            }
        )
    return {
        "schema": "RH.SupportPrime.WitnessVerification.v0.4",
        "expected_witness_count": len(expected_paths),
        "actual_witness_count": len(actual_paths),
        "path_sets_match": (
            {path.resolve() for path in expected_paths}
            == {path.resolve() for path in actual_paths}
        ),
        "rows": rows,
        "all_serialized_sparse_witnesses_psd": all(
            row["reconstructed"]["serialized_sparse_witness_psd"]
            for row in rows
        ),
        "all_serialized_measures_block_budget": all(
            row["reconstructed"]["serialized_measure_budget_block"]
            for row in rows
        ),
        "maximum_minimum_eigenvalue_abs_difference": max(
            (
                row["minimum_eigenvalue_abs_difference"]
                for row in rows
            ),
            default=0.0,
        ),
        "verification_level": (
            "E2 floating reconstruction of serialized finite-model "
            "measures; no interval or analytic transfer"
        ),
        "global_rh_certificate": False,
    }


def main() -> None:
    output = verify_all_saved_witnesses()
    (ROOT / "outputs" / "witness_verification.json").write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, indent=2, ensure_ascii=False))
    if not (
        output["path_sets_match"]
        and output["all_serialized_sparse_witnesses_psd"]
        and output["all_serialized_measures_block_budget"]
    ):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
