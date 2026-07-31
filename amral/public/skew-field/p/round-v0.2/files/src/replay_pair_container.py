"""Replay the Round 2 fixed pair-container area."""
from pathlib import Path
import json
import math
import numpy as np
from scipy.spatial import ConvexHull

ROOT = Path(__file__).resolve().parents[1]
summary = json.loads((ROOT / "data" / "round02_summary.json").read_text())
rho = summary["parameters"]["rho"]

constant = np.loadtxt(
    ROOT / "data" / "constant_placed.csv",
    delimiter=",",
    skiprows=1,
)
candidate = np.loadtxt(
    ROOT / "data" / "candidate_mirror_placed.csv",
    delimiter=",",
    skiprows=1,
)

points = np.vstack([constant, candidate])
hull = ConvexHull(points)
poly = points[hull.vertices]
x = poly[:, 0]
y = poly[:, 1]
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
saved = summary["final_pair_container"]["convex_thick_area"]

print("center hull area:", area)
print("center hull perimeter:", perimeter)
print("thick area:", thick_area)
print("saved:", saved)
print("difference:", thick_area - saved)
