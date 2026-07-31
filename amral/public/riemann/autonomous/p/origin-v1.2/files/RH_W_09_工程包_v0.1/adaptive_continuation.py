#!/usr/bin/env python3
"""Local adaptive continuation for translated cubic B-spline Weil chambers.

This is an exploratory layer.  It uses floating-point quadrature and generalized
eigenvalue routines only to rank candidates.  It never emits a proof status.
"""
from __future__ import annotations
import csv, json, math, time
from functools import lru_cache
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh
from scipy.special import comb

DEG = 7
FACT = math.factorial(DEG)


def beta7(z: float) -> float:
    if z <= -4.0 or z >= 4.0:
        return 0.0
    total = 0.0
    for k in range(9):
        y = z + 4.0 - k
        if y > 0.0:
            total += ((-1) ** k) * comb(8, k, exact=True) * y**7 / FACT
    return total


def prime_power_base(n: int) -> int | None:
    for p in range(2, n + 1):
        if any(p % d == 0 for d in range(2, math.isqrt(p) + 1)):
            continue
        q = p
        while q < n:
            q *= p
        if q == n:
            return p
    return None


VM = {n: (math.log(p) if (p := prime_power_base(n)) else 0.0) for n in range(2, 1000)}


@lru_cache(maxsize=20000)
def entry(center: float, h: float) -> float:
    def f(x: float) -> float:
        return beta7((x - center) / h)

    left = center - 4 * h
    right = center + 4 * h
    radius = max(abs(left), abs(right))
    knots = [center + h * k for k in range(-4, 5)]

    endpoint = sum(
        quad(
            lambda x: f(x) * (math.exp(x / 2) + math.exp(-x / 2)),
            a,
            b,
            epsabs=5e-9,
            epsrel=5e-9,
            limit=80,
        )[0]
        for a, b in zip(knots[:-1], knots[1:])
    )

    f0 = f(0.0)
    F0 = 2 * f0
    constant = -(math.log(4 * math.pi) + 0.5772156649015329) * f0

    def even_f(x: float) -> float:
        return f(x) + f(-x)

    def integrand(x: float) -> float:
        if abs(x) < 1e-10:
            return F0 / 4
        return (
            even_f(x) * math.exp(-x / 2) - F0 * math.exp(-x)
        ) / (-math.expm1(-2 * x))

    points = sorted(
        {0.0, radius}
        | {q for q in knots if 0 < q < radius}
        | {-q for q in knots if 0 < -q < radius}
    )
    integral = sum(
        quad(integrand, a, b, epsabs=5e-9, epsrel=5e-9, limit=80)[0]
        for a, b in zip(points[:-1], points[1:])
    )
    arch = -(integral - F0 * math.atanh(math.exp(-radius)))

    prime = 0.0
    nmax = min(999, int(math.exp(radius)) + 1)
    for n in range(2, nmax + 1):
        lam = VM[n]
        if lam:
            x = math.log(n)
            prime -= lam / math.sqrt(n) * (f(x) + f(-x))
    return endpoint + constant + arch + prime


def chamber(h: float, d: float, dimension: int) -> tuple[float, float, float] | None:
    lags = [entry(round(-k * d, 13), round(h, 13)) for k in range(dimension)]
    M = np.array([[lags[abs(i - j)] for j in range(dimension)] for i in range(dimension)])
    glags = [beta7(k * d / h) for k in range(dimension)]
    G = np.array([[glags[abs(i - j)] for j in range(dimension)] for i in range(dimension)])
    gram_eigs = np.linalg.eigvalsh(G)
    if gram_eigs[0] < 1e-9:
        return None
    vals = eigh(M, G, eigvals_only=True)
    return float(vals[0]), float(vals[-1]), float(gram_eigs[0])


def nearest_prime_power_boundary(h: float, d: float, dimension: int) -> dict:
    radius = (dimension - 1) * d + 4 * h
    best: tuple[float, tuple[int, int, int, float]] | None = None
    for lag in range(dimension):
        for n, lam in VM.items():
            if not lam or math.log(n) > radius + 1:
                continue
            x = math.log(n)
            for sign in (-1, 1):
                signed = abs(sign * x + lag * d) - 4 * h
                candidate = (abs(signed), (lag, n, sign, signed))
                if best is None or candidate[0] < best[0]:
                    best = candidate
    assert best is not None
    lag, n, sign, signed = best[1]
    return {
        "absolute_distance": best[0],
        "lag": lag,
        "n": n,
        "sample_sign": sign,
        "signed_distance": signed,
        "meaning": "zero marks a correlation-support activation boundary",
    }


def main() -> None:
    out = Path(__file__).resolve().parent
    dimension = 15
    h = 0.15
    d = 0.225
    step_h = 0.015
    step_d = 0.015
    best = chamber(h, d, dimension)
    if best is None:
        raise RuntimeError("invalid starting chamber")

    records: list[dict] = []
    for iteration in range(20):
        candidates: list[tuple[float, float, float, tuple[float, float, float]]] = []
        for dh, dd in (
            (0, 0), (step_h, 0), (-step_h, 0), (0, step_d), (0, -step_d),
            (step_h, step_d), (step_h, -step_d), (-step_h, step_d), (-step_h, -step_d),
        ):
            hh = h + dh
            ddd = d + dd
            if hh <= 0.03 or ddd <= 0.05 or not (1.05 <= ddd / hh <= 4.5):
                continue
            if (dimension - 1) * ddd + 4 * hh > 5.0:
                continue
            result = chamber(hh, ddd, dimension)
            if result is not None:
                candidates.append((result[0], hh, ddd, result))
        candidates.sort(key=lambda row: row[0])
        improved = bool(candidates) and candidates[0][0] < best[0] - max(1e-10, abs(best[0]) * 1e-5)
        if improved:
            _, h, d, best = candidates[0]
        else:
            step_h /= 2
            step_d /= 2

        boundary = nearest_prime_power_boundary(h, d, dimension)
        records.append({
            "iteration": iteration,
            "h": h,
            "d": d,
            "dimension": dimension,
            "lambda_min_exploratory": best[0],
            "lambda_max_exploratory": best[1],
            "gram_min_exploratory": best[2],
            "step_h": step_h,
            "step_d": step_d,
            "improved": improved,
            "max_radius": (dimension - 1) * d + 4 * h,
            "nearest_boundary": boundary,
            "status": "NUMERICAL_CANDIDATE_ONLY",
        })
        if max(step_h, step_d) < 2e-4:
            break

    final = records[-1]
    payload = {
        "schema": "RH-W-09-adaptive-continuation-v0.1",
        "date": "2026-07-23",
        "start": {"h": 0.15, "d": 0.225, "dimension": dimension},
        "policy": "coordinate neighborhood with step halving; floating exploration only",
        "records": records,
        "selected_candidate": final,
        "scope_warning": "The continuation output is not a proof or certificate.",
    }
    (out / "adaptive_continuation_path.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    with (out / "adaptive_continuation_path.csv").open("w", newline="", encoding="utf-8-sig") as fh:
        fields = [
            "iteration", "h", "d", "dimension", "lambda_min_exploratory",
            "lambda_max_exploratory", "gram_min_exploratory", "step_h", "step_d",
            "improved", "max_radius", "nearest_boundary_n", "nearest_boundary_lag",
            "nearest_boundary_distance", "status",
        ]
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for row in records:
            writer.writerow({
                "iteration": row["iteration"], "h": row["h"], "d": row["d"],
                "dimension": row["dimension"],
                "lambda_min_exploratory": row["lambda_min_exploratory"],
                "lambda_max_exploratory": row["lambda_max_exploratory"],
                "gram_min_exploratory": row["gram_min_exploratory"],
                "step_h": row["step_h"], "step_d": row["step_d"],
                "improved": row["improved"], "max_radius": row["max_radius"],
                "nearest_boundary_n": row["nearest_boundary"]["n"],
                "nearest_boundary_lag": row["nearest_boundary"]["lag"],
                "nearest_boundary_distance": row["nearest_boundary"]["absolute_distance"],
                "status": row["status"],
            })
    print(json.dumps(final, indent=2))


if __name__ == "__main__":
    main()
