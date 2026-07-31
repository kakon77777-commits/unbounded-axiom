"""Replay the Round 4 convex pair-container area."""
from pathlib import Path
import json
import math
import numpy as np
from scipy.spatial import ConvexHull

ROOT = Path(__file__).resolve().parents[1]
summary = json.loads((ROOT / "data/round04_summary.json").read_text())
rho = summary["parameters"]["rho"]

curve_a = np.loadtxt(
    ROOT / "data/containers/convex_pair_round3.csv",
    delimiter=",",
    skiprows=1,
)
curve_b = np.loadtxt(
    ROOT / "data/containers/convex_pair_M10_placed.csv",
    delimiter=",",
    skiprows=1,
)

points = np.vstack([curve_a, curve_b])
hull = ConvexHull(points)
polygon = points[hull.vertices]
x = polygon[:, 0]
y = polygon[:, 1]

area = 0.5 * abs(
    np.dot(x, np.roll(y, -1))
    - np.dot(y, np.roll(x, -1))
)
perimeter = np.sum(
    np.hypot(
        np.diff(np.r_[x, x[0]]),
        np.diff(np.r_[y, y[0]]),
    )
)
thick_area = area + rho * perimeter + math.pi * rho**2
saved = summary["convex_finite_family"]["thick_area"]

print("center area:", area)
print("center perimeter:", perimeter)
print("thick area:", thick_area)
print("saved:", saved)
print("difference:", thick_area - saved)
