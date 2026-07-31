"""Replay the Round 11 seed exposure."""
from pathlib import Path
import json
import numpy as np
from shapely.geometry import LineString, Polygon

ROOT = Path(__file__).resolve().parents[1]
summary = json.loads((ROOT / "data" / "round10_summary.json").read_text())
rho = summary["parameters"]["rho"]

container = Polygon(
    np.loadtxt(
        ROOT / "data" / "containers" / "round10_filled_exterior.csv",
        delimiter=",",
        skiprows=1,
    )
)
curve = np.loadtxt(
    ROOT / "data" / "curves" / "round11_seed_best_against_round10.csv",
    delimiter=",",
    skiprows=1,
)
tube = LineString(curve).buffer(
    rho,
    quad_segs=192,
    cap_style=1,
    join_style=1,
)
outside = tube.difference(container).area
saved = summary["round11_seed"]["outside_area_high"]

print("outside:", outside)
print("saved:", saved)
print("difference:", outside - saved)
