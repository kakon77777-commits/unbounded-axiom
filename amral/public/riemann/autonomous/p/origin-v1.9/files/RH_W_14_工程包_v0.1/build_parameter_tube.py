#!/usr/bin/env python3
"""Build a rigorous two-parameter tube around the RH-W-13 mixed dictionary.

The scale h is fixed.  The genuine subspace parameters spacing d and relative
channel shift sigma vary in a rational rectangle.  A global Lipschitz envelope
for every Weil and Gram entry converts the certified point interval into a
continuous parameter-tube certificate.

This is a finite-dimensional result and makes no RH claim.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json, math, sys

import weil_interval_core as base
from rigorous_refinement_tools import euler_gamma_binet_iv

sys.set_int_max_str_digits(0)

H = F(1797, 10000)
D0 = F(893, 5000)
SIGMA0 = F(0)
RHO_D = F(4, 10**12)
RHO_SIGMA = F(4, 10**12)
N = 5
DEGREES = (1, 3)
CORR = {(0, 0): 3, (0, 1): 5, (1, 0): 5, (1, 1): 7}
DELTA = F(1, 100_000_000)
UPPER = F(1, 20_000_000)
GRID = 10**42


def fq(obj):
    return F(int(obj["num"]), int(obj["den"]))


def iv(obj):
    return base.IV(fq(obj["lower"]), fq(obj["upper"]))


def prime_power_base(n: int) -> int | None:
    for p in range(2, n + 1):
        if any(p % q == 0 for q in range(2, math.isqrt(p) + 1)):
            continue
        v = p
        while v < n:
            v *= p
        if v == n:
            return p
    return None


def ldlt(A):
    n = len(A)
    L = [[F(0) for _ in range(n)] for _ in range(n)]
    pivots = []
    for i in range(n):
        L[i][i] = F(1)
        p = A[i][i] - sum(L[i][k] * L[i][k] * pivots[k] for k in range(i))
        if p <= 0:
            return False, pivots + [p]
        pivots.append(p)
        for j in range(i + 1, n):
            L[j][i] = (
                A[j][i]
                - sum(L[j][k] * L[i][k] * pivots[k] for k in range(i))
            ) / p
    return True, pivots


def grid_center(x: base.IV) -> F:
    m = x.midpoint()
    q = m.numerator * GRID // m.denominator
    a, b = F(q, GRID), F(q + 1, GRID)
    return a if abs(m - a) <= abs(b - m) else b


def interval_quadratic(A, c):
    out = base.IV.point(0)
    for i in range(len(c)):
        for j in range(len(c)):
            out += A[i][j].scale(F(c[i] * c[j]))
    return base.coarsen(out, 72)


def exact_quadratic(A, c):
    return sum(
        (F(c[i] * c[j]) * A[i][j] for i in range(len(c)) for j in range(len(c))),
        F(0),
    )


def derivative_bound(correlation_degree: int):
    """Rigorous global |dW/dcenter| bound over the whole tube.

    Uses 0<=beta<=1, ||beta'||_inf<=1, ||beta''||_inf<=4.
    The archimedean integrand is bounded after preserving its x=0 cancellation.
    """
    q = F(correlation_degree + 1, 2)
    center_radius = F(N - 1) * (D0 + RHO_D)
    if correlation_degree == 5:
        center_radius += RHO_SIGMA
    support_radius = center_radius + q * H
    exp_half = base.exp_iv(support_radius / 2, 100)
    const = base.log4pi_iv() + euler_gamma_binet_iv(100, 4)

    coeff_sum = base.IV.point(0)
    active = []
    n = 2
    while base.log_rational_iv(F(n), 220).lo <= support_radius:
        p = prime_power_base(n)
        if p is not None:
            active.append(n)
            coeff_sum += base.log_rational_iv(F(p), 220) / base.sqrt_rational_iv(F(n), 150)
        n += 1

    endpoint = F(4) * q * exp_half.hi
    constant = const.hi / H
    prime = F(2) * coeff_sum.hi / H
    arch = support_radius * (exp_half.hi / (2 * H) + F(4) / (H * H))
    total = endpoint + constant + prime + arch
    integer_upper = F((total.numerator + total.denominator - 1) // total.denominator)
    return {
        "correlation_degree": correlation_degree,
        "support_radius_max": support_radius,
        "active_prime_powers_for_bound": active,
        "endpoint_bound": endpoint,
        "constant_bound": constant,
        "prime_bound": prime,
        "archimedean_bound": arch,
        "exact_total": total,
        "integer_upper": integer_upper,
    }


def interval_distance(a: base.IV, b: base.IV) -> F:
    if a.hi < b.lo:
        return b.lo - a.hi
    if b.hi < a.lo:
        return a.lo - b.hi
    return F(0)


def chamber_margin():
    logs = {n: base.log_rational_iv(F(n), 240) for n in (2, 3, 4, 5)}
    best = None
    witness = None
    for r in (3, 5, 7):
        q = (r + 1) // 2
        for lag in range(N):
            c0 = F(lag) * D0
            cr = F(lag) * RHO_D + (RHO_SIGMA if r == 5 else F(0))
            c_iv = base.IV(c0 - cr, c0 + cr)
            for n, x in logs.items():
                for sign in (1, -1):
                    sample = x if sign == 1 else -x
                    for k in range(-q, q + 1):
                        knot = c_iv + base.IV.point(F(k) * H)
                        dist = interval_distance(sample, knot)
                        if best is None or dist < best:
                            best = dist
                            witness = {
                                "correlation_degree": r,
                                "lag": lag,
                                "n": n,
                                "sample_sign": sign,
                                "knot_index": k,
                                "sample": base.iv_json(sample),
                                "knot_interval": base.iv_json(knot),
                            }
    if best is None:
        raise AssertionError("empty chamber margin search")
    return best, witness


def main():
    root = Path(__file__).resolve().parent
    point = json.loads((root / "mixed_10x10_nearzero_interval.json").read_text(encoding="utf-8"))
    if point["schema"] != "RH-W-13-cross-regularity-continuation-v0.1":
        raise AssertionError("unexpected center schema")

    M = [[iv(x) for x in row] for row in point["matrix"]]
    G = [[fq(x) for x in row] for row in point["gram"]]
    dim = 2 * N
    C = [[grid_center(M[i][j]) for j in range(dim)] for i in range(dim)]

    bounds = {r: derivative_bound(r) for r in (3, 5, 7)}
    LM = {r: bounds[r]["integer_upper"] for r in bounds}
    LG = F(1, 1) / H

    base_rows = []
    tube_M_rows = []
    tube_G_rows = []
    combined_rows = []
    for I in range(dim):
        ca, i = divmod(I, N)
        bsum = F(0)
        msum = F(0)
        gsum = F(0)
        for J in range(dim):
            cb, j = divmod(J, N)
            r = CORR[(ca, cb)]
            variation = F(abs(i - j)) * RHO_D
            if ca != cb:
                variation += RHO_SIGMA
            base_error = max(abs(C[I][J] - M[I][J].lo), abs(M[I][J].hi - C[I][J]))
            bsum += base_error
            msum += LM[r] * variation
            gsum += LG * variation
        base_rows.append(bsum)
        tube_M_rows.append(msum)
        tube_G_rows.append(gsum)
        combined_rows.append(bsum + msum + DELTA * gsum)

    epsilon = max(combined_rows)
    epsilon_g = max(tube_G_rows)
    T = [
        [C[i][j] - DELTA * G[i][j] - (epsilon if i == j else F(0)) for j in range(dim)]
        for i in range(dim)
    ]
    ok, pivots = ldlt(T)
    if not ok:
        raise ArithmeticError("tube lower certificate failed")

    GT = [[G[i][j] - (epsilon_g if i == j else F(0)) for j in range(dim)] for i in range(dim)]
    gok, gpivots = ldlt(GT)
    if not gok:
        raise ArithmeticError("Gram tube positivity failed")

    witness = list(map(int, point["upper_witness"]["integer_vector"]))
    q0 = interval_quadratic(M, witness)
    g0 = exact_quadratic(G, witness)
    delta_q = F(0)
    delta_g = F(0)
    for I in range(dim):
        ca, i = divmod(I, N)
        for J in range(dim):
            cb, j = divmod(J, N)
            r = CORR[(ca, cb)]
            variation = F(abs(i - j)) * RHO_D
            if ca != cb:
                variation += RHO_SIGMA
            weight = abs(F(witness[I] * witness[J]))
            delta_q += weight * LM[r] * variation
            delta_g += weight * LG * variation
    q_tube = base.IV(q0.lo - delta_q, q0.hi + delta_q)
    g_tube = base.IV(g0 - delta_g, g0 + delta_g)
    if g_tube.lo <= 0 or q_tube.hi >= UPPER * g_tube.lo:
        raise ArithmeticError("tube upper witness failed")

    max_support = F(N - 1) * (D0 + RHO_D) + 4 * H
    log5 = base.log_rational_iv(F(5), 240)
    if max_support >= log5.lo:
        raise ArithmeticError("n>=5 support exclusion failed")
    knot_margin, knot_witness = chamber_margin()
    if knot_margin <= 0:
        raise ArithmeticError("spline chamber is not stable")

    result = {
        "schema": "RH-W-14-rigorous-parameter-tube-v0.1",
        "date": "2026-07-23",
        "status": "CERTIFIED_2D_NEAR_ZERO_PARAMETER_TUBE",
        "center_artifact": "mixed_10x10_nearzero_interval.json",
        "basis": {
            "fixed_h": base.frac_json(H),
            "basis_degrees": [1, 3],
            "per_channel_dimension": N,
            "total_dimension": dim,
        },
        "parameter_tube": {
            "dimension": 2,
            "spacing_d": {
                "center": base.frac_json(D0),
                "radius": base.frac_json(RHO_D),
                "interval": [base.frac_json(D0 - RHO_D), base.frac_json(D0 + RHO_D)],
            },
            "relative_shift_sigma": {
                "center": base.frac_json(SIGMA0),
                "radius": base.frac_json(RHO_SIGMA),
                "interval": [base.frac_json(-RHO_SIGMA), base.frac_json(RHO_SIGMA)],
            },
            "h_is_fixed_this_round": True,
            "alpha_gauge_not_counted_as_dimension": True,
        },
        "b_spline_global_bounds": {
            "beta_sup": base.frac_json(F(1)),
            "beta_prime_sup": base.frac_json(F(1)),
            "beta_second_sup": base.frac_json(F(4)),
            "derivation": "cardinal B-spline convolution and finite-difference derivative identities",
            "gram_center_derivative_bound": base.frac_json(LG),
            "weil_center_derivative_bounds": {
                str(r): {
                    k: (base.frac_json(v) if isinstance(v, F) else v)
                    for k, v in bounds[r].items()
                }
                for r in bounds
            },
        },
        "chamber_stability": {
            "max_support_radius": base.frac_json(max_support),
            "log5": base.iv_json(log5),
            "all_n_ge_5_excluded": True,
            "minimum_sample_to_spline_knot_margin": base.frac_json(knot_margin),
            "margin_witness": knot_witness,
            "prime_power_activation_graph_constant_on_tube": True,
            "active_global_prime_powers": [2, 3, 4],
        },
        "certificate": {
            "delta_lower": base.frac_json(DELTA),
            "upper_ratio": base.frac_json(UPPER),
            "exact_bracket_on_entire_tube": "1e-8 < lambda_min(M(d,sigma),G(d,sigma)) < 5e-8",
            "grid_denominator": str(GRID),
            "base_point_row_errors": [base.frac_json(x) for x in base_rows],
            "tube_M_row_bounds": [base.frac_json(x) for x in tube_M_rows],
            "tube_G_row_bounds": [base.frac_json(x) for x in tube_G_rows],
            "combined_row_bounds": [base.frac_json(x) for x in combined_rows],
            "global_combined_row_bound": base.frac_json(epsilon),
            "global_gram_row_bound": base.frac_json(epsilon_g),
            "ldlt_pivots": [base.frac_json(x) for x in pivots],
            "gram_tube_ldlt_pivots": [base.frac_json(x) for x in gpivots],
            "method": "point interval plus rigorous center-Lipschitz envelope and exact rational LDL^T",
        },
        "upper_witness": {
            "integer_vector": witness,
            "center_quadratic_interval": base.iv_json(q0),
            "center_gram_exact": base.frac_json(g0),
            "tube_quadratic_variation_bound": base.frac_json(delta_q),
            "tube_gram_variation_bound": base.frac_json(delta_g),
            "tube_quadratic_interval": base.iv_json(q_tube),
            "tube_gram_interval": base.iv_json(g_tube),
        },
        "scope_warning": "This is a continuous two-parameter finite-dimensional spectral tube. It neither proves nor disproves RH.",
    }

    (root / "parameter_tube_2d_certificate.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    summary = "\n".join(
        [
            f"status={result['status']}",
            "tube_dimensions=d,sigma",
            f"d_radius={float(RHO_D):.18e}",
            f"sigma_radius={float(RHO_SIGMA):.18e}",
            f"combined_row_bound={float(epsilon):.18e}",
            f"gram_row_bound={float(epsilon_g):.18e}",
            f"minimum_knot_margin={float(knot_margin):.18e}",
            "exact_lower=lambda_min>1e-8_on_entire_tube",
            "exact_upper=lambda_min<5e-8_on_entire_tube",
            "RH_CLAIM=False",
        ]
    ) + "\n"
    (root / "BUILD_SUMMARY.txt").write_text(summary, encoding="utf-8")
    print(summary, end="")


if __name__ == "__main__":
    main()
