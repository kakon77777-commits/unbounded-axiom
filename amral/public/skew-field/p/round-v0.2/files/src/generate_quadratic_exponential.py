"""Replay the Round 2 quadratic-exponential candidate.

This intentionally uses the same endpoint quadrature convention as the
search ledger. It replays the numerical candidate, not a separately
re-optimized continuous-limit curve.
"""
from pathlib import Path
import math
import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import brentq

Q = 1.0900735478479215
C = 0.9538448569085957
N_THETA = 14001
N_ENDPOINT = 2001

def fp(theta):
    return np.exp(Q * (theta - C) ** 2)

def endpoint_equation(theta):
    grid = np.linspace(0.0, theta, N_ENDPOINT)
    values = fp(grid)
    f_end = np.trapezoid(values, grid)
    return theta + math.atan2(f_end, fp(theta)) - math.pi

theta_end = brentq(
    endpoint_equation,
    1e-8,
    math.pi - 1e-8,
    xtol=1e-13,
)
theta = np.linspace(0.0, theta_end, N_THETA)
fp_values = fp(theta)
f = np.concatenate([[0.0], cumulative_trapezoid(fp_values, theta)])

speed0 = np.sqrt(f * f + fp_values * fp_values)
b = 1.0 / np.trapezoid(speed0, theta)
r = b * f
x = r * np.cos(theta)
y = r * np.sin(theta)

speed = b * speed0
s = np.concatenate([[0.0], cumulative_trapezoid(speed, theta)])
s = s / s[-1]

fpp = fp_values * (2.0 * Q * (theta - C))
curvature = (
    (f * f + 2.0 * fp_values * fp_values - f * fpp)
    / (f * f + fp_values * fp_values) ** 1.5
) / b

out = np.column_stack([s, x, y, curvature])
path = Path(__file__).resolve().parents[1] / "data" / "candidate_curve_replayed.csv"
np.savetxt(path, out, delimiter=",", header="s,x,y,kappa", comments="")

print(path)
print("theta_end =", theta_end)
print("b =", b)
print("max curvature =", curvature.max())
