"""Replay Fourier-20 and B-spline residual exposures."""
from pathlib import Path
import json
import numpy as np
from shapely.geometry import LineString, Polygon

ROOT = Path(__file__).resolve().parents[1]
summary = json.loads((ROOT / "data/round09_summary.json").read_text())
rho = summary["parameters"]["rho"]

boundary = np.loadtxt(
    ROOT / "data/containers/round9_filled_exterior.csv",
    delimiter=",",
    skiprows=1,
)
container = Polygon(boundary)

for filename, key in [
    ("round10_seed_best_against_round9.csv", "round10_seed"),
    ("bspline_holdout_best.csv", "non_fourier_holdout"),
]:
    curve = np.loadtxt(
        ROOT / "data" / "curves" / filename,
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
    saved = summary[key]["outside_area_high"]
    print(filename, outside, saved, outside - saved)
