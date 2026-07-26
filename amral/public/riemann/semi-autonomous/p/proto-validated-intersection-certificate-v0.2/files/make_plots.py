from __future__ import annotations

import csv
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"

# Piecewise-linear function nodes (base plus reported central correction midpoint).
rows = list(csv.DictReader((ROOT / "data/base_nodes.csv").open(encoding="utf-8")))
t = np.array([float(row["t"]) for row in rows])
y = np.array([float(row["base_value"]) for row in rows])
cert = json.loads((OUT / "certificate.json").read_text(encoding="utf-8"))
a = sum(cert["arithmetic"]["endpoint_correction_interval"]) / 2
y[len(y) // 2] += a
plt.figure(figsize=(9, 4.8))
plt.plot(t, y)
plt.axhline(0, linewidth=0.8)
plt.xlabel("t")
plt.ylabel("psi(t)")
plt.title("Validated piecewise-linear test function")
plt.tight_layout()
plt.savefig(OUT / "validated_test_function.png", dpi=180)
plt.close()

# Certified adaptive cover.
cells = list(csv.DictReader((OUT / "certified_region_cells.csv").open(encoding="utf-8")))
plt.figure(figsize=(9, 4.8))
ax = plt.gca()
values = np.array([float(cell["block_upper"]) for cell in cells])
normalized = np.log10(np.maximum(-values, 1e-16))
for cell, value in zip(cells, normalized):
    x0, x1 = float(cell["x_lo"]), float(cell["x_hi"])
    y0, y1 = float(cell["y_lo"]), float(cell["y_hi"])
    rectangle = plt.Rectangle((x0, y0), x1 - x0, y1 - y0, fill=True, alpha=0.5)
    rectangle.set_facecolor(plt.cm.viridis((value - normalized.min()) / max(np.ptp(normalized), 1e-12)))
    rectangle.set_edgecolor("none")
    ax.add_patch(rectangle)
ax.set_xlim(8, 8.5)
ax.set_ylim(-0.2, -0.1)
ax.set_xlabel("Re(w)")
ax.set_ylabel("Im(w)")
ax.set_title("Adaptive continuous-region certificate cover")
plt.tight_layout()
plt.savefig(OUT / "certified_region_cover.png", dpi=180)
plt.close()

# Arithmetic intervals.
labels = ["Finite", "Archimedean", "Total"]
intervals = [
    cert["arithmetic"]["finite_interval"],
    cert["arithmetic"]["archimedean_interval"],
    cert["arithmetic"]["arithmetic_total_interval"],
]
centers = np.array([(a + b) / 2 for a, b in intervals])
errors = np.array([(b - a) / 2 for a, b in intervals])
positions = np.arange(len(labels))
plt.figure(figsize=(8, 4.8))
plt.errorbar(centers, positions, xerr=errors, fmt="o", capsize=5)
plt.axvline(0, linewidth=0.8)
plt.yticks(positions, labels)
plt.xlabel("Certified interval")
plt.title("Arithmetic certificate intervals")
plt.tight_layout()
plt.savefig(OUT / "arithmetic_intervals.png", dpi=180)
plt.close()
