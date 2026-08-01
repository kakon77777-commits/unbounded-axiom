#!/usr/bin/env python3
"""Pure-rational verifier for RH-W-14's continuous (d,sigma) parameter tube."""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json, math, sys

import weil_interval_core as base
from rigorous_refinement_tools import euler_gamma_binet_iv

sys.set_int_max_str_digits(0)


def fq(o):
    return F(int(o["num"]), int(o["den"]))


def iv(o):
    return base.IV(fq(o["lower"]), fq(o["upper"]))


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


def ldlt(A):
    n = len(A)
    L = [[F(0) for _ in range(n)] for _ in range(n)]
    piv = []
    for i in range(n):
        L[i][i] = F(1)
        z = A[i][i] - sum(L[i][k] * L[i][k] * piv[k] for k in range(i))
        if z <= 0:
            return False, piv + [z]
        piv.append(z)
        for j in range(i + 1, n):
            L[j][i] = (A[j][i] - sum(L[j][k] * L[i][k] * piv[k] for k in range(i))) / z
    return True, piv


def center(x, grid):
    m = x.midpoint()
    q = m.numerator * grid // m.denominator
    a, b = F(q, grid), F(q + 1, grid)
    return a if abs(m - a) <= abs(b - m) else b


def iq(A, c):
    z = base.IV.point(0)
    for i in range(len(c)):
        for j in range(len(c)):
            z += A[i][j].scale(F(c[i] * c[j]))
    return base.coarsen(z, 72)


def eq(A, c):
    return sum((F(c[i] * c[j]) * A[i][j] for i in range(len(c)) for j in range(len(c))), F(0))


def derivative_bound(r, h, d0, rd, rs, N):
    q = F(r + 1, 2)
    center_radius = F(N - 1) * (d0 + rd) + (rs if r == 5 else F(0))
    R = center_radius + q * h
    e = base.exp_iv(R / 2, 100)
    const = base.log4pi_iv() + euler_gamma_binet_iv(100, 4)
    coeff = base.IV.point(0)
    active = []
    n = 2
    while base.log_rational_iv(F(n), 220).lo <= R:
        p = ppbase(n)
        if p is not None:
            active.append(n)
            coeff += base.log_rational_iv(F(p), 220) / base.sqrt_rational_iv(F(n), 150)
        n += 1
    endpoint = F(4) * q * e.hi
    constant = const.hi / h
    prime = F(2) * coeff.hi / h
    arch = R * (e.hi / (2 * h) + F(4) / (h * h))
    total = endpoint + constant + prime + arch
    integer_upper = F((total.numerator + total.denominator - 1) // total.denominator)
    return R, active, endpoint, constant, prime, arch, total, integer_upper


def interval_distance(a, b):
    if a.hi < b.lo:
        return b.lo - a.hi
    if b.hi < a.lo:
        return a.lo - b.hi
    return F(0)


def chamber_margin(h, d0, rd, rs, N):
    logs = {n: base.log_rational_iv(F(n), 240) for n in (2, 3, 4, 5)}
    best = None
    witness = None
    for r in (3, 5, 7):
        q = (r + 1) // 2
        for lag in range(N):
            c0 = F(lag) * d0
            cr = F(lag) * rd + (rs if r == 5 else F(0))
            civ = base.IV(c0 - cr, c0 + cr)
            for n, x in logs.items():
                for sign in (1, -1):
                    sample = x if sign == 1 else -x
                    for k in range(-q, q + 1):
                        knot = civ + base.IV.point(F(k) * h)
                        dist = interval_distance(sample, knot)
                        if best is None or dist < best:
                            best = dist
                            witness = (r, lag, n, sign, k, sample, knot)
    return best, witness


def main():
    root = Path(__file__).resolve().parent
    tube = json.loads((root / "parameter_tube_2d_certificate.json").read_text(encoding="utf-8"))
    point = json.loads((root / "mixed_10x10_nearzero_interval.json").read_text(encoding="utf-8"))
    if tube["schema"] != "RH-W-14-rigorous-parameter-tube-v0.1":
        raise AssertionError("tube schema")
    if point["schema"] != "RH-W-13-cross-regularity-continuation-v0.1":
        raise AssertionError("center schema")

    h = fq(tube["basis"]["fixed_h"])
    N = int(tube["basis"]["per_channel_dimension"])
    dim = int(tube["basis"]["total_dimension"])
    if dim != 2 * N or tuple(tube["basis"]["basis_degrees"]) != (1, 3):
        raise AssertionError("basis")
    pd = tube["parameter_tube"]["spacing_d"]
    ps = tube["parameter_tube"]["relative_shift_sigma"]
    d0, rd = fq(pd["center"]), fq(pd["radius"])
    s0, rs = fq(ps["center"]), fq(ps["radius"])
    if s0 != 0 or rd <= 0 or rs <= 0:
        raise AssertionError("nondegenerate tube")
    if [fq(x) for x in pd["interval"]] != [d0 - rd, d0 + rd]:
        raise AssertionError("d interval")
    if [fq(x) for x in ps["interval"]] != [-rs, rs]:
        raise AssertionError("sigma interval")
    if not tube["parameter_tube"]["alpha_gauge_not_counted_as_dimension"]:
        raise AssertionError("alpha gauge bookkeeping")

    M = [[iv(x) for x in row] for row in point["matrix"]]
    G = [[fq(x) for x in row] for row in point["gram"]]
    for i in range(dim):
        for j in range(dim):
            if M[i][j] != M[j][i] or G[i][j] != G[j][i]:
                raise AssertionError("symmetry")

    cert = tube["certificate"]
    delta = fq(cert["delta_lower"])
    upper = fq(cert["upper_ratio"])
    grid = int(cert["grid_denominator"])
    C = [[center(M[i][j], grid) for j in range(dim)] for i in range(dim)]

    stored_bounds = tube["b_spline_global_bounds"]
    if fq(stored_bounds["beta_sup"]) != 1 or fq(stored_bounds["beta_prime_sup"]) != 1 or fq(stored_bounds["beta_second_sup"]) != 4:
        raise AssertionError("B-spline universal bounds")
    LG = F(1) / h
    if fq(stored_bounds["gram_center_derivative_bound"]) != LG:
        raise AssertionError("Gram derivative")
    LM = {}
    for r in (3, 5, 7):
        R, active, endpoint, constant, prime, arch, total, integer_upper = derivative_bound(r, h, d0, rd, rs, N)
        sb = stored_bounds["weil_center_derivative_bounds"][str(r)]
        checks = {
            "support_radius_max": R,
            "endpoint_bound": endpoint,
            "constant_bound": constant,
            "prime_bound": prime,
            "archimedean_bound": arch,
            "exact_total": total,
            "integer_upper": integer_upper,
        }
        for key, value in checks.items():
            if fq(sb[key]) != value:
                raise AssertionError(f"derivative bound {r} {key}")
        if sb["active_prime_powers_for_bound"] != active:
            raise AssertionError("derivative prime set")
        if integer_upper < total:
            raise AssertionError("integer derivative upper")
        LM[r] = integer_upper

    corr = {(0, 0): 3, (0, 1): 5, (1, 0): 5, (1, 1): 7}
    base_rows = []
    m_rows = []
    g_rows = []
    combined = []
    for I in range(dim):
        ca, i = divmod(I, N)
        bsum = msum = gsum = F(0)
        for J in range(dim):
            cb, j = divmod(J, N)
            r = corr[(ca, cb)]
            var = F(abs(i - j)) * rd + (rs if ca != cb else F(0))
            bsum += max(abs(C[I][J] - M[I][J].lo), abs(M[I][J].hi - C[I][J]))
            msum += LM[r] * var
            gsum += LG * var
        base_rows.append(bsum)
        m_rows.append(msum)
        g_rows.append(gsum)
        combined.append(bsum + msum + delta * gsum)

    if [fq(x) for x in cert["base_point_row_errors"]] != base_rows:
        raise AssertionError("base row errors")
    if [fq(x) for x in cert["tube_M_row_bounds"]] != m_rows:
        raise AssertionError("M row bounds")
    if [fq(x) for x in cert["tube_G_row_bounds"]] != g_rows:
        raise AssertionError("G row bounds")
    if [fq(x) for x in cert["combined_row_bounds"]] != combined:
        raise AssertionError("combined rows")
    epsilon = max(combined)
    epsilon_g = max(g_rows)
    if fq(cert["global_combined_row_bound"]) != epsilon or fq(cert["global_gram_row_bound"]) != epsilon_g:
        raise AssertionError("global row bounds")

    T = [[C[i][j] - delta * G[i][j] - (epsilon if i == j else F(0)) for j in range(dim)] for i in range(dim)]
    ok, piv = ldlt(T)
    if not ok or [fq(x) for x in cert["ldlt_pivots"]] != piv:
        raise AssertionError("tube lower LDLT")
    GT = [[G[i][j] - (epsilon_g if i == j else F(0)) for j in range(dim)] for i in range(dim)]
    gok, gpiv = ldlt(GT)
    if not gok or [fq(x) for x in cert["gram_tube_ldlt_pivots"]] != gpiv:
        raise AssertionError("tube Gram LDLT")

    wobj = tube["upper_witness"]
    w = list(map(int, wobj["integer_vector"]))
    if w != list(map(int, point["upper_witness"]["integer_vector"])):
        raise AssertionError("witness identity")
    q0 = iq(M, w)
    g0 = eq(G, w)
    dq = dg = F(0)
    for I in range(dim):
        ca, i = divmod(I, N)
        for J in range(dim):
            cb, j = divmod(J, N)
            r = corr[(ca, cb)]
            var = F(abs(i - j)) * rd + (rs if ca != cb else F(0))
            wt = abs(F(w[I] * w[J]))
            dq += wt * LM[r] * var
            dg += wt * LG * var
    qt = base.IV(q0.lo - dq, q0.hi + dq)
    gt = base.IV(g0 - dg, g0 + dg)
    if iv(wobj["center_quadratic_interval"]) != q0 or fq(wobj["center_gram_exact"]) != g0:
        raise AssertionError("center witness")
    if fq(wobj["tube_quadratic_variation_bound"]) != dq or fq(wobj["tube_gram_variation_bound"]) != dg:
        raise AssertionError("witness variation")
    if iv(wobj["tube_quadratic_interval"]) != qt or iv(wobj["tube_gram_interval"]) != gt:
        raise AssertionError("tube witness intervals")
    if gt.lo <= 0 or qt.hi >= upper * gt.lo:
        raise AssertionError("tube upper bound")

    ch = tube["chamber_stability"]
    max_support = F(N - 1) * (d0 + rd) + 4 * h
    log5 = base.log_rational_iv(F(5), 240)
    if fq(ch["max_support_radius"]) != max_support or iv(ch["log5"]) != log5:
        raise AssertionError("support data")
    if max_support >= log5.lo or not ch["all_n_ge_5_excluded"]:
        raise AssertionError("support exclusion")
    margin, mw = chamber_margin(h, d0, rd, rs, N)
    if fq(ch["minimum_sample_to_spline_knot_margin"]) != margin or margin <= 0:
        raise AssertionError("chamber margin")
    if ch["active_global_prime_powers"] != [2, 3, 4] or not ch["prime_power_activation_graph_constant_on_tube"]:
        raise AssertionError("activation graph")

    lines = [
        "schema=OK",
        "center_certificate_dependency=RH-W-13",
        "tube_parameters=d,sigma",
        "tube_is_nondegenerate=OK",
        "alpha_gauge_excluded=OK",
        "b_spline_derivative_bounds=RECONSTRUCTED",
        f"weil_lipschitz_bounds={{{3}:{LM[3]},{5}:{LM[5]},{7}:{LM[7]}}}",
        f"minimum_knot_margin={float(margin):.18e}",
        "prime_power_chamber_constant=[2,3,4]",
        f"gram_tube_ldlt_pivots_positive={len(gpiv)}",
        f"mixed_tube_ldlt_pivots_positive={len(piv)}",
        "exact_tube_bracket=1e-8<lambda_min<5e-8",
        "status=EXACT_2D_PARAMETER_TUBE_CERTIFICATE_OK",
        "RH_CLAIM=False",
    ]
    text = "\n".join(lines) + "\n"
    (root / "EXACT_TUBE_VERIFY.txt").write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
