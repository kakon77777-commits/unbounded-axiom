from __future__ import annotations

import csv
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from .core import PhaseShapingResult


def save_result(result: PhaseShapingResult, output_dir: str | Path) -> None:
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)

    (output / "phase_shaping_result.json").write_text(
        json.dumps(result.summary_dict(), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    with (output / "psi_samples.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["t", "psi"])
        writer.writerows(zip(result.t, result.psi, strict=True))

    with (output / "region_block.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["x", "y", "G_real", "G_imag", "block"])
        for ix, x in enumerate(result.check_x):
            for iy, y in enumerate(result.check_y):
                value = result.G_grid[ix, iy]
                writer.writerow(
                    [x, y, value.real, value.imag, result.block_grid[ix, iy]]
                )

    _save_plot(result, output / "phase_shaping.png")


def _save_plot(result: PhaseShapingResult, path: Path) -> None:
    x_mesh, y_mesh = np.meshgrid(result.check_x, result.check_y, indexing="ij")

    figure = plt.figure(figsize=(8, 11))
    axes = figure.subplots(3, 1)

    contour = axes[0].contourf(x_mesh, y_mesh, result.block_grid, levels=30)
    figure.colorbar(contour, ax=axes[0], label=r"$2\operatorname{Re}(G(w)^2)$")
    axes[0].set_title("Regional orbit block")
    axes[0].set_xlabel("Re(w)")
    axes[0].set_ylabel("Im(w)")

    real_contour = axes[1].contourf(x_mesh, y_mesh, result.G_grid.real, levels=30)
    figure.colorbar(real_contour, ax=axes[1], label="Re G")
    axes[1].set_title("Real part of G")
    axes[1].set_xlabel("Re(w)")
    axes[1].set_ylabel("Im(w)")

    imag_contour = axes[2].contourf(x_mesh, y_mesh, result.G_grid.imag, levels=30)
    figure.colorbar(imag_contour, ax=axes[2], label="Im G")
    axes[2].set_title("Imaginary part of G")
    axes[2].set_xlabel("Re(w)")
    axes[2].set_ylabel("Im(w)")

    figure.tight_layout()
    figure.savefig(path, dpi=160)
    plt.close(figure)
