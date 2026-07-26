from __future__ import annotations

import csv
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from .core import IntersectionConfig, RadiusIntersectionResult


def _selected_result(
    config: IntersectionConfig, results: list[RadiusIntersectionResult]
) -> RadiusIntersectionResult:
    return min(results, key=lambda item: abs(item.support_radius - config.selected_radius))


def save_outputs(
    config: IntersectionConfig,
    results: list[RadiusIntersectionResult],
    output_dir: str | Path,
) -> None:
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)

    payload = {
        "config": {
            **config.__dict__,
            "support_radii": list(config.support_radii),
        },
        "results": [item.summary_dict() for item in results],
    }
    (output / "intersection_scan_result.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    with (output / "intersection_scan.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "support_radius",
                "activated_count",
                "constrained_dimension",
                "arithmetic_min_eigenvalue",
                "required_arithmetic_margin",
                "arithmetic_value",
                "fit_grid_max_block",
                "check_grid_max_block",
                "check_grid_min_block",
                "intersection_found_on_grid",
                "optimizer_success",
            ]
        )
        for item in results:
            writer.writerow(
                [
                    item.support_radius,
                    len(item.activated_prime_powers),
                    item.constrained_dimension,
                    item.arithmetic_min_eigenvalue,
                    item.required_arithmetic_margin,
                    item.arithmetic_value,
                    item.fit_grid_max_block,
                    item.check_grid_max_block,
                    item.check_grid_min_block,
                    item.intersection_found_on_grid,
                    item.optimizer_success,
                ]
            )

    radii = np.asarray([item.support_radius for item in results])
    max_blocks = np.asarray([item.check_grid_max_block for item in results])
    plt.figure(figsize=(8, 5))
    plt.plot(radii, max_blocks, marker="o")
    plt.axhline(0.0, linewidth=1.0)
    plt.xlabel("Support radius R")
    plt.ylabel("Dense-grid max of 2 Re(G(w)^2)")
    plt.title("Regional separation margin")
    plt.tight_layout()
    plt.savefig(output / "separation_margin.png", dpi=180)
    plt.close()

    arithmetic_values = np.asarray([item.arithmetic_value for item in results])
    required = np.asarray([item.required_arithmetic_margin for item in results])
    plt.figure(figsize=(8, 5))
    plt.plot(radii, arithmetic_values, marker="o", label="candidate value")
    plt.plot(radii, required, marker="s", label="required margin")
    plt.yscale("log")
    plt.xlabel("Support radius R")
    plt.ylabel("Arithmetic quadratic value (log scale)")
    plt.title("Arithmetic safety margin for the same coefficient vector")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output / "arithmetic_margin.png", dpi=180)
    plt.close()

    selected = _selected_result(config, results)
    plt.figure(figsize=(8, 5))
    extent = [
        selected.check_y[0],
        selected.check_y[-1],
        selected.check_x[0],
        selected.check_x[-1],
    ]
    plt.imshow(selected.check_block, origin="lower", aspect="auto", extent=extent)
    plt.colorbar(label="2 Re(G(w)^2)")
    plt.xlabel("Im(w)")
    plt.ylabel("Re(w)")
    plt.title(f"Selected regional block, R={selected.support_radius:g}")
    plt.tight_layout()
    plt.savefig(output / "selected_region_block.png", dpi=180)
    plt.close()

    np.savetxt(
        output / "selected_coefficients.csv",
        np.column_stack((np.arange(len(selected.coefficients)), selected.coefficients)),
        delimiter=",",
        header="basis_index,coefficient",
        comments="",
    )
    np.savetxt(
        output / "selected_psi.csv",
        np.column_stack((selected.t, selected.psi)),
        delimiter=",",
        header="t,psi",
        comments="",
    )

    with (output / "selected_region_block.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["real_w", "imag_w", "G_real", "G_imag", "orbit_block"])
        for ix, real_w in enumerate(selected.check_x):
            for iy, imag_w in enumerate(selected.check_y):
                value = selected.check_G[ix, iy]
                writer.writerow(
                    [real_w, imag_w, value.real, value.imag, selected.check_block[ix, iy]]
                )

    audit = {
        "selected_radius": selected.support_radius,
        "direct_audit": selected.direct_audit,
        "matrix_audit": selected.matrix_audit,
        "endpoint_residual": selected.endpoint_residual,
        "central_residual": selected.central_residual,
        "c0_norm": selected.c0_norm,
    }
    (output / "normalization_audit.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2), encoding="utf-8"
    )
