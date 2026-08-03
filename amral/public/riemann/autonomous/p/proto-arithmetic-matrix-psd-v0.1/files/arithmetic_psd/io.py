from __future__ import annotations

import csv
import json
from dataclasses import asdict
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from .core import ArithmeticScanConfig, RadiusResult


def _closest_result(results: list[RadiusResult], radius: float) -> RadiusResult:
    return min(results, key=lambda item: abs(item.support_radius - radius))


def save_scan(
    config: ArithmeticScanConfig,
    results: list[RadiusResult],
    output_dir: str | Path,
) -> None:
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    summary = {
        "config": asdict(config),
        "no_prime_support_threshold": float(np.log(2.0) / 2.0),
        "results": [result.summary_dict() for result in results],
        "warning": (
            "Research prototype only. The local formulas are implemented in a fixed unitary convention, "
            "but numerical PSD and frequency truncation are not rigorous interval certificates."
        ),
    }
    (out / "arithmetic_scan_result.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    with (out / "support_scan.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "support_radius",
                "convolution_log_radius",
                "activated_count",
                "min_eigen_archimedean",
                "min_eigen_finite",
                "min_eigen_total",
                "max_eigen_total",
                "numerical_psd",
                "archimedean_spectral_crosscheck_norm",
            ]
        )
        for result in results:
            writer.writerow(
                [
                    result.support_radius,
                    result.convolution_log_radius,
                    len(result.activated_prime_powers),
                    result.min_eigen_archimedean,
                    result.min_eigen_finite,
                    result.min_eigen_total,
                    result.max_eigen_total,
                    result.numerical_psd,
                    result.archimedean_spectral_crosscheck_norm,
                ]
            )

    with (out / "activated_prime_powers.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.writer(handle)
        writer.writerow(["support_radius", "prime", "exponent", "m_log_p", "coefficient"])
        for result in results:
            for item in result.activated_prime_powers:
                writer.writerow(
                    [
                        result.support_radius,
                        item.prime,
                        item.exponent,
                        item.log_value,
                        item.coefficient,
                    ]
                )

    radii = np.asarray([item.support_radius for item in results])
    min_arch = np.asarray([item.min_eigen_archimedean for item in results])
    min_fin = np.asarray([item.min_eigen_finite for item in results])
    min_total = np.asarray([item.min_eigen_total for item in results])

    fig, ax = plt.subplots(figsize=(9, 5.4))
    ax.plot(radii, min_arch, marker="o", label="archimedean")
    ax.plot(radii, min_fin, marker="o", label="finite places")
    ax.plot(radii, min_total, marker="o", label="total")
    ax.axhline(0.0, linewidth=1)
    ax.axvline(np.log(2.0) / 2.0, linewidth=1, linestyle="--", label="no-prime threshold")
    ax.set_xlabel("support radius R of ψ")
    ax.set_ylabel("minimum constrained eigenvalue")
    ax.set_title("Arithmetic matrix support scan")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out / "support_scan.png", dpi=170)
    plt.close(fig)

    selected = _closest_result(results, config.selected_radius)
    np.savetxt(out / "selected_matrix_archimedean.csv", selected.matrix_archimedean, delimiter=",")
    np.savetxt(out / "selected_matrix_finite.csv", selected.matrix_finite, delimiter=",")
    np.savetxt(out / "selected_matrix_total.csv", selected.matrix_total, delimiter=",")
    np.savetxt(out / "selected_matrix_total_reduced.csv", selected.matrix_total_reduced, delimiter=",")

    fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.2))
    for ax, matrix, title in zip(
        axes,
        [selected.matrix_archimedean, selected.matrix_finite, selected.matrix_total],
        ["Archimedean", "Finite places", "Total"],
        strict=True,
    ):
        image = ax.imshow(matrix, aspect="auto")
        ax.set_title(f"{title} matrix, R={selected.support_radius:g}")
        fig.colorbar(image, ax=ax, fraction=0.046, pad=0.04)
    fig.tight_layout()
    fig.savefig(out / "selected_matrices.png", dpi=170)
    plt.close(fig)
