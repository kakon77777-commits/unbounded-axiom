"""Generate the moving-knot B-spline holdout curve."""
from pathlib import Path
import json
import math
import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.interpolate import CubicSpline

ROOT = Path(__file__).resolve().parents[1]
summary = json.loads((ROOT / "data/round09_summary.json").read_text())
info = summary["non_fourier_holdout"]

knots = np.asarray(info["knots"], dtype=float)
values = np.asarray(info["values"], dtype=float)
s = np.linspace(0.0, 1.0, 8001)
g = CubicSpline(knots, values, bc_type="natural")(s)
raw = np.exp(g - np.max(g))
kappa = math.pi * raw / np.trapezoid(raw, s)
theta = np.concatenate([[0.0], cumulative_trapezoid(kappa, s)])
theta *= math.pi / theta[-1]
x = np.concatenate([[0.0], cumulative_trapezoid(np.cos(theta), s)])
y = np.concatenate([[0.0], cumulative_trapezoid(np.sin(theta), s)])
radial_dot = x * np.cos(theta) + y * np.sin(theta)

output = ROOT / "data" / "curves" / "bspline_holdout_replayed.csv"
np.savetxt(
    output,
    np.column_stack([s, x, y, kappa, theta, radial_dot]),
    delimiter=",",
    header="s,x,y,kappa,theta,radial_dot",
    comments="",
)
print(output)
