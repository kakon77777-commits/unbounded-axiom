"""Replay the Round 9 twelve-family nonconvex container."""
from pathlib import Path
import json
import numpy as np
from shapely.geometry import LineString, Polygon
from shapely.ops import unary_union

ROOT = Path(__file__).resolve().parents[1]
summary = json.loads((ROOT / "data/round09_summary.json").read_text())
rho = summary["parameters"]["rho"]

tubes = []
for path in sorted((ROOT / "data" / "curves").glob("placed_*.csv")):
    points = np.loadtxt(path, delimiter=",", skiprows=1)
    tubes.append(
        LineString(points).buffer(
            rho,
            quad_segs=192,
            cap_style=1,
            join_style=1,
        )
    )

union = unary_union(tubes)
if union.geom_type != "Polygon":
    raise RuntimeError(f"Unexpected geometry: {union.geom_type}")

filled = Polygon(union.exterior)
saved = summary["container_response"]["final_simply_connected_area"]

print("raw union:", union.area)
print("filled:", filled.area)
print("saved:", saved)
print("difference:", filled.area - saved)
