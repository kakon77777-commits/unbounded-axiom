#!/usr/bin/env python3
"""Numerical regression for centered cardinal B-spline convolution identities.

This is an independent floating-point regression, not a proof artifact.
"""
from __future__ import annotations
from math import comb, factorial
import json
from pathlib import Path
import numpy as np
from scipy.integrate import quad

OUT = Path(__file__).resolve().parent


def beta(m: int, x: float) -> float:
    if m == 0:
        if -0.5 < x < 0.5:
            return 1.0
        if x == -0.5 or x == 0.5:
            return 0.5
        return 0.0
    s = 0.0
    a = (m + 1) / 2.0
    for k in range(m + 2):
        y = x + a - k
        if y > 0:
            s += ((-1) ** k) * comb(m + 1, k) * y**m
    return s / factorial(m)


def conv(m: int, n: int, x: float) -> float:
    lm, rm = -(m + 1)/2, (m + 1)/2
    ln, rn = x-(n + 1)/2, x+(n + 1)/2
    left, right = max(lm, ln), min(rm, rn)
    if left >= right:
        return 0.0
    points = []
    # knots of beta_m(y)
    points.extend([-(m+1)/2 + k for k in range(m+2)])
    # knots of beta_n(y-x)
    points.extend([x-(n+1)/2 + k for k in range(n+2)])
    points = sorted(p for p in points if left < p < right)
    val, err = quad(lambda y: beta(m, y) * beta(n, y-x), left, right,
                    points=points, epsabs=2e-13, epsrel=2e-13, limit=200)
    return val


def main() -> None:
    max_conv_err = 0.0
    max_edge_err = 0.0
    records = []
    for m in range(5):
        for n in range(5):
            r = m+n+1
            rad = (r+1)/2
            xs = np.linspace(-rad+0.037, rad-0.037, 11)
            for x in xs:
                got = conv(m,n,float(x))
                expected = beta(r,float(x))
                e = abs(got-expected)
                max_conv_err=max(max_conv_err,e)
            for eps in (1e-2, 3e-3, 1e-3):
                x=-rad+eps
                got=beta(r,x)
                expected=eps**r/factorial(r)
                max_edge_err=max(max_edge_err,abs(got-expected))
            records.append({"m":m,"n":n,"r":r})
    status = max_conv_err < 2e-9 and max_edge_err < 2e-9
    text=(
        f"pairs={len(records)}\n"
        f"max_convolution_error={max_conv_err:.16e}\n"
        f"max_first_piece_error={max_edge_err:.16e}\n"
        f"status={'ALL_CHECKS_OK' if status else 'FAILED'}\n"
        "rigor=FLOATING_POINT_REGRESSION_ONLY\n"
    )
    (OUT/'VALIDATION.txt').write_text(text,encoding='utf-8')
    print(text,end='')
    if not status:
        raise SystemExit(1)

if __name__=='__main__':
    main()
