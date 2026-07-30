"""Numerical regression checks for RH-W-02.

These checks do not prove any RH statement. They test the explicit inverse
formula, moment constraints, and the raw-L2 point-evaluation failure witness.
"""
from __future__ import annotations

import math
from pathlib import Path

import numpy as np


def bump(q: np.ndarray) -> np.ndarray:
    out = np.zeros_like(q, dtype=float)
    mask = np.abs(q) < 1.0
    z = q[mask]
    out[mask] = np.exp(-1.0 / (1.0 - z * z))
    return out


def cumtrapz(y: np.ndarray, x: np.ndarray) -> np.ndarray:
    out = np.zeros_like(y, dtype=float)
    out[1:] = np.cumsum(0.5 * (y[1:] + y[:-1]) * np.diff(x))
    return out


def main() -> None:
    # A smooth compact seed in log coordinates.
    u = np.linspace(-3.0, 3.0, 60001)
    du = u[1] - u[0]
    h = bump(u / 1.25) * (1.0 + 0.2 * np.cos(3.0 * u))

    # Numerical P h = h'' + h'.
    hp = np.gradient(h, du, edge_order=2)
    hpp = np.gradient(hp, du, edge_order=2)
    g = hpp + hp

    moment0 = np.trapezoid(g, u)
    moment1 = np.trapezoid(np.exp(u) * g, u)

    # Explicit inverse: Y=e^{-u} int_{-inf}^u e^v G(v)dv, H=int Y.
    y = np.exp(-u) * cumtrapz(np.exp(u) * g, u)
    h_rec = cumtrapz(y, u)

    # Numerical integration constants drift slightly; align on the central support.
    mask = np.abs(u) < 1.15
    offset = float(np.mean(h_rec[mask] - h[mask]))
    h_rec -= offset
    inverse_error = float(np.max(np.abs(h_rec[mask] - h[mask])))

    # L2 failure witness: psi_n(t0)=1 while norm tends to zero.
    t = np.linspace(-2.0, 2.0, 200001)
    t0 = 0.3
    l2_rows = []
    for n in (2, 4, 8, 16, 32, 64):
        psi = np.exp(-(n * (t - t0)) ** 2)
        l2 = math.sqrt(float(np.trapezoid(psi * psi, t)))
        value = float(np.exp(-(n * (t0 - t0)) ** 2))
        l2_rows.append((n, value, l2))

    checks = {
        "moment0_abs": abs(float(moment0)),
        "moment1_abs": abs(float(moment1)),
        "inverse_max_error_on_core": inverse_error,
        "l2_norm_strictly_decreasing": all(
            l2_rows[i + 1][2] < l2_rows[i][2] for i in range(len(l2_rows) - 1)
        ),
        "point_values_all_one": all(abs(row[1] - 1.0) < 1e-15 for row in l2_rows),
    }

    # Tolerances account for finite-difference differentiation of a C-infinity bump.
    assert checks["moment0_abs"] < 2e-5, checks
    assert checks["moment1_abs"] < 2e-5, checks
    assert checks["inverse_max_error_on_core"] < 2e-3, checks
    assert checks["l2_norm_strictly_decreasing"], checks
    assert checks["point_values_all_one"], checks

    lines = [
        "RH-W-02 numerical regression",
        f"moment0_abs={checks['moment0_abs']:.6e}",
        f"moment1_abs={checks['moment1_abs']:.6e}",
        f"inverse_max_error_on_core={checks['inverse_max_error_on_core']:.6e}",
        "L2 point-evaluation witness:",
    ]
    lines.extend(f"n={n:>2d} value_at_t0={v:.1f} L2={norm:.6e}" for n, v, norm in l2_rows)
    lines.append("ALL_CHECKS_OK")
    text = "\n".join(lines) + "\n"
    print(text, end="")
    Path(__file__).with_name("VALIDATION.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
