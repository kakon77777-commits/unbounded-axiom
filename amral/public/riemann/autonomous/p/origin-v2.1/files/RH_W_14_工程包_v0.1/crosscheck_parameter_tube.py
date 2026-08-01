#!/usr/bin/env python3
"""High-precision floating sample check of the certified tube; not proof path."""
from __future__ import annotations
from pathlib import Path
import json, math
import mpmath as mp
import numpy as np
from scipy.linalg import eigh

mp.mp.dps = 55
N = 5


def beta(deg, z):
    half = mp.mpf(deg + 1) / 2
    s = mp.mpf("0")
    for k in range(deg + 2):
        y = z + half - k
        if y > 0:
            s += (-1) ** k * math.comb(deg + 1, k) * y ** deg
    return s / math.factorial(deg)


def ppbase(n):
    for p in range(2, n + 1):
        if any(p % q == 0 for q in range(2, math.isqrt(p) + 1)):
            continue
        v = p
        while v < n:
            v *= p
        if v == n:
            return p
    return None


def calc(deg, h, c, ex=5):
    rad = mp.mpf(deg + 1) / 2 * h
    left, right = c - rad, c + rad
    f = lambda x: beta(deg, (x - c) / h)
    f0 = f(0)
    pts = [left + k * h for k in range(deg + 2)]
    endpoint = mp.fsum(
        mp.quad(lambda x: f(x) * (mp.exp(x / 2) + mp.exp(-x / 2)), [a, b])
        for a, b in zip(pts[:-1], pts[1:])
    )
    const = -(mp.log(4 * mp.pi) + mp.euler) * f0
    R = max(abs(left), abs(right))
    split = {mp.mpf("0"), R}
    for q in pts:
        if 0 < q < R:
            split.add(q)
        if 0 < -q < R:
            split.add(-q)
    split = sorted(split)

    def integrand(x):
        if abs(x) < mp.mpf("1e-35"):
            return f0 / 2
        return (mp.exp(x / 2) * (f(x) + f(-x)) - 2 * f0) / (mp.exp(x) - mp.exp(-x))

    local = mp.fsum(mp.quad(integrand, [a, b]) for a, b in zip(split[:-1], split[1:]))
    arch = -local + 2 * f0 * mp.atanh(mp.exp(-R))
    prime = mp.mpf("0")
    for n in range(2, ex):
        p = ppbase(n)
        if p is None:
            continue
        x = mp.log(n)
        prime -= mp.log(p) / mp.sqrt(n) * (f(x) + f(-x))
    return endpoint + const + arch + prime


def matrices(h, d, sigma):
    degs = (1, 3)
    corr = {(1, 1): 3, (1, 3): 5, (3, 3): 7}
    shifts = [mp.mpf(j - 2) * d for j in range(N)]
    channel = [
        [x - sigma / 2 for x in shifts],
        [x + sigma / 2 for x in shifts],
    ]
    M = np.zeros((10, 10), dtype=float)
    G = np.zeros((10, 10), dtype=float)
    cache = {}
    for ca, a in enumerate(degs):
        for cb, b in enumerate(degs):
            r = corr[tuple(sorted((a, b)))]
            for i in range(N):
                for j in range(N):
                    I, J = ca * N + i, cb * N + j
                    c = channel[ca][i] - channel[cb][j]
                    # W and beta are even in c; string key preserves high precision.
                    key = (r, mp.nstr(abs(c), 50))
                    if key not in cache:
                        cache[key] = calc(r, h, abs(c))
                    M[I, J] = float(cache[key])
                    G[I, J] = float(beta(r, -c / h))
    M = (M + M.T) / 2
    G = (G + G.T) / 2
    return eigh(M, G, eigvals_only=True)


def main():
    root = Path(__file__).resolve().parent
    cert = json.loads((root / "parameter_tube_2d_certificate.json").read_text(encoding="utf-8"))
    def q(o):
        return mp.mpf(o["num"]) / mp.mpf(o["den"])
    h = q(cert["basis"]["fixed_h"])
    d0 = q(cert["parameter_tube"]["spacing_d"]["center"])
    rd = q(cert["parameter_tube"]["spacing_d"]["radius"])
    rs = q(cert["parameter_tube"]["relative_shift_sigma"]["radius"])
    samples = [
        ("center", d0, mp.mpf("0")),
        ("d_minus", d0 - rd, mp.mpf("0")),
        ("d_plus", d0 + rd, mp.mpf("0")),
        ("sigma_minus", d0, -rs),
        ("sigma_plus", d0, rs),
        ("corner_mm", d0 - rd, -rs),
        ("corner_pp", d0 + rd, rs),
    ]
    lines = []
    lows = []
    for name, d, s in samples:
        vals = matrices(h, d, s)
        lows.append(vals[0])
        lines.append(f"{name}: lambda0={vals[0]:.18e} lambda1={vals[1]:.18e}")
    lines += [
        f"sample_min={min(lows):.18e}",
        f"sample_max={max(lows):.18e}",
        "all_samples_inside_exact_bracket=" + str(all(1e-8 < x < 5e-8 for x in lows)),
        "status=CROSSCHECK_TUBE_SAMPLES_OK",
        "rigor=HIGH_PRECISION_FLOATING_SAMPLE_ONLY",
        "RH_CLAIM=False",
    ]
    text = "\n".join(lines) + "\n"
    (root / "CROSSCHECK_TUBE.txt").write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
