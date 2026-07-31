"""Replay the Round 4 seven-family nonconvex container."""
from pathlib import Path
import json
import numpy as np
from shapely.geometry import LineString, Polygon
from shapely.ops import unary_union

ROOT = Path(__file__).resolve().parents[1]
summary = json.loads((ROOT / "data/round04_summary.json").read_text())
rho = summary["parameters"]["rho"]

geometries = []
for path in sorted((ROOT / "data/curves").glob("placed_*.csv")):
    points = np.loadtxt(path, delimiter=",", skiprows=1)
    geometries.append(
        LineString(points).buffer(
            rho,
            quad_segs=96,
            cap_style=1,
            join_style=1,
        )
    )

union = unary_union(geometries)
filled = Polygon(union.exterior)

saved_raw = summary["nonconvex_finite_family"]["raw_union_area_high"]
saved_filled = summary["nonconvex_finite_family"]["filled_simply_connected_area_high"]

print("raw union area:", union.area)
print("saved raw:", saved_raw)
print("raw difference:", union.area - saved_raw)
print("filled area:", filled.area)
print("saved filled:", saved_filled)
print("filled difference:", filled.area - saved_filled)
