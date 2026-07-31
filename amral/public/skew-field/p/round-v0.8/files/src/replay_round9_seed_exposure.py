"""Replay the Round 9 seed exposure against the Round 8 container."""
from pathlib import Path
import json
import numpy as np
from shapely.geometry import LineString, Polygon

ROOT = Path(__file__).resolve().parents[1]
summary = json.loads((ROOT / "data/round08_summary.json").read_text())
rho = summary["parameters"]["rho"]

boundary = np.loadtxt(
    ROOT / "data/containers/round8_filled_exterior.csv",
    delimiter=",",
    skiprows=1,
)
curve = np.loadtxt(
    ROOT / "data/curves/round9_seed_best_against_round8.csv",
    delimiter=",",
    skiprows=1,
)

container = Polygon(boundary)
tube = LineString(curve).buffer(
    rho,
    quad_segs=192,
    cap_style=1,
    join_style=1,
)
outside = tube.difference(container)

print("outside area:", outside.area)
print("saved:", summary["round9_seed"]["outside_area_high"])
print("difference:", outside.area - summary["round9_seed"]["outside_area_high"])
