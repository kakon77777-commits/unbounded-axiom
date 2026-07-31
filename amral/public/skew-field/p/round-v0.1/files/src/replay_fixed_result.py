"""Replay the fixed all-four convex-container metrics.

This script uses the exact curve grids used by the optimizer. It does not
rerun the global optimization; it verifies the saved fixed placement.
"""
from pathlib import Path
import json
import math
import numpy as np
from scipy.spatial import ConvexHull

ROOT = Path(__file__).resolve().parents[1]
summary = json.loads((ROOT / "data" / "summary.json").read_text(encoding="utf-8"))
rho = summary["parameters"]["rho"]

def transform(points, phi, translation):
    c, s = math.cos(phi), math.sin(phi)
    rotation = np.array([[c, -s], [s, c]])
    return points @ rotation.T + np.asarray(translation)

names = [
    "constant_curvature",
    "archimedean",
    "contact_saturated",
    "finite_width_layer",
]
placed = []
for name in names:
    points = np.loadtxt(
        ROOT / "data" / "curves_optimization" / f"{name}.csv",
        delimiter=",",
        skiprows=1,
    )
    phi, translation = summary["all_four"]["placements"][name]
    placed.append(transform(points, phi, translation))

points = np.vstack(placed)
hull = ConvexHull(points)
poly = points[hull.vertices]
x, y = poly[:, 0], poly[:, 1]
area = 0.5 * abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1)))
perimeter = np.sum(
    np.hypot(
        np.diff(np.r_[x, x[0]]),
        np.diff(np.r_[y, y[0]]),
    )
)
thick_area = area + rho * perimeter + math.pi * rho**2

print("center hull area:", area)
print("center hull perimeter:", perimeter)
print("thick convex container area:", thick_area)
print("saved area:", summary["all_four"]["optimized_proxy_area"])
print("difference:", thick_area - summary["all_four"]["optimized_proxy_area"])
