from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from interval_cert.green import build_projected_gram


ROOT = Path(__file__).resolve().parent


def main() -> None:
    witness = json.loads(
        (
            ROOT
            / "data"
            / "rational_atomic_witness_v0.6.json"
        ).read_text(encoding="utf-8")
    )
    orientation = json.loads(
        (
            ROOT
            / "outputs"
            / "coefficient_orientation_audit.json"
        ).read_text(encoding="utf-8")
    )
    gram_result = build_projected_gram(witness)
    gram = np.asarray(
        [
            [float(value.midpoint()) for value in row]
            for row in gram_result.projected_gram
        ]
    )
    positive_count = len(gram_result.positive_functions)
    positive_gram = gram[:positive_count, :positive_count]
    cross = gram[:positive_count, positive_count:]
    negative_gram = gram[positive_count:, positive_count:]
    lower_counts = [
        row["lower_count_from_absolute_S_only"]
        for row in orientation["rows"]
    ]
    positive_weights = []
    for band_index, support in enumerate(witness["axis_supports"]):
        for atom in support:
            positive_weights.append(
                lower_counts[band_index]
                * atom["weight"]["numerator"]
                / atom["weight"]["denominator"]
            )
    alpha = (
        witness["model"]["target_alpha"]["numerator"]
        / witness["model"]["target_alpha"]["denominator"]
    )
    negative_weights = []
    for atom in witness["core_support"]:
        signed_weight = (
            2
            * alpha
            * atom["weight"]["numerator"]
            / atom["weight"]["denominator"]
        )
        positive_weights.append(signed_weight)
        negative_weights.append(signed_weight)
    diagonal = np.asarray(positive_weights)
    system = (
        np.eye(positive_count)
        + positive_gram * diagonal[None, :]
    )
    solution = np.linalg.solve(system, cross)
    effective_negative = (
        negative_gram
        - cross.T @ (diagonal[:, None] * solution)
    )
    negative_diagonal = np.asarray(negative_weights)
    test_matrix = (
        np.diag(1.0 / negative_diagonal)
        - effective_negative
    )
    schur = (
        np.sqrt(negative_diagonal)[:, None]
        * test_matrix
        * np.sqrt(negative_diagonal)[None, :]
    )
    eigenvalues = np.linalg.eigvalsh(
        0.5 * (schur + schur.T)
    )
    output = {
        "schema": "RH.CoefficientOrientationStressTest.v0.7",
        "substitution": (
            "Replace each stored upper-profile band coefficient by "
            "max(0, Delta theta/pi - B(a) - B(b)); keep atoms, "
            "probability weights, core measure, alpha, and kernel fixed."
        ),
        "lower_profile": lower_counts,
        "floating_two_by_two_test_matrix": test_matrix.tolist(),
        "floating_schur_matrix": schur.tolist(),
        "floating_schur_eigenvalues": eigenvalues.tolist(),
        "fixed_witness_survives_lower_profile": bool(
            eigenvalues[0] >= 0
        ),
        "role": (
            "Diagnostic counterstress only; it is not an interval "
            "nonexistence theorem for all possible witnesses."
        ),
        "required_response": (
            "Re-derive coefficient orientation, add validated lower "
            "zero counts/presence, or redesign the dual. Do not merely "
            "reuse the current upper-profile coefficients."
        ),
        "global_rh_certificate": False,
    }
    (
        ROOT / "outputs" / "orientation_stress_test.json"
    ).write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

