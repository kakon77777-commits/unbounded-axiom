"""Replay connected exposure components for the Round 7 attack."""
from pathlib import Path
import json
import numpy as np
from shapely.geometry import LineString, Polygon

ROOT = Path(__file__).resolve().parents[1]
summary = json.loads((ROOT / "data/round07_summary.json").read_text())
rho = summary["parameters"]["rho"]

boundary = np.loadtxt(
    ROOT / "data/containers/round6_filled_exterior.csv",
    delimiter=",",
    skiprows=1,
)
curve = np.loadtxt(
    ROOT / "data/curves/round7_attack_best_against_round6.csv",
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

if outside.geom_type == "Polygon":
    components = [outside]
else:
    components = list(outside.geoms)

areas = sorted([component.area for component in components], reverse=True)
print("outside area:", outside.area)
print("component count:", len(components))
print("component areas:", areas)
