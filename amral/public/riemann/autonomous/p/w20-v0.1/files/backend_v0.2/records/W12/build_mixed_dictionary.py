#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json, math, sys
import numpy as np
from scipy.linalg import eigh

import weil_interval_core as base
import mixed_order_core as mixed
from rigorous_refinement_tools import euler_gamma_binet_iv

sys.set_int_max_str_digits(0)

H = F(3, 20)
D = F(9, 40)
N = 5
BASIS_DEGREES = (1, 3)
CORR_DEGREES = {(1, 1): 3, (1, 3): 5, (3, 3): 7}
K_BY_CORR_DEGREE = {3: 900, 5: 320, 7: 180}
GRID = 10**30
DELTA = F(1, 2000)
SHIFTS = tuple(F(j - N // 2) * D for j in range(N))


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
        pivot = A[i][i] - sum(L[i][k] * L[i][k] * pivots[k] for k in range(i))
        if pivot <= 0:
            return False, pivots + [pivot]
        pivots.append(pivot)
        for j in range(i + 1, n):
            L[j][i] = (
                A[j][i] - sum(L[j][k] * L[i][k] * pivots[k] for k in range(i))
            ) / pivot
    return True, pivots


def grid_center(x: base.IV) -> F:
    m = x.midpoint()
    q = m.numerator * GRID // m.denominator
    left = F(q, GRID)
    right = F(q + 1, GRID)
    return left if abs(m - left) <= abs(right - m) else right


def parse_iv(obj: dict) -> base.IV:
    return base.IV(
        F(int(obj["lower"]["num"]), int(obj["lower"]["den"])),
        F(int(obj["upper"]["num"]), int(obj["upper"]["den"])),
    )


def interval_quadratic(A, c):
    total = base.IV.point(0)
    for i in range(len(c)):
        for j in range(len(c)):
            total += A[i][j].scale(F(c[i] * c[j]))
    return base.coarsen(total, 60)


def exact_quadratic(A, c):
    return sum((F(c[i] * c[j]) * A[i][j] for i in range(len(c)) for j in range(len(c))), F(0))


def block_interval(A, start, size):
    return [[A[start+i][start+j] for j in range(size)] for i in range(size)]


def block_exact(A, start, size):
    return [[A[start+i][start+j] for j in range(size)] for i in range(size)]


def certify_block(Aiv, Gex, delta):
    size = len(Aiv)
    C = [[grid_center(Aiv[i][j]) for j in range(size)] for i in range(size)]
    eps = max(
        sum(max(abs(C[i][j]-Aiv[i][j].lo), abs(Aiv[i][j].hi-C[i][j])) for j in range(size))
        for i in range(size)
    )
    test = [[C[i][j]-delta*Gex[i][j]-(eps if i==j else F(0)) for j in range(size)] for i in range(size)]
    ok,piv=ldlt(test)
    if not ok:
        raise ArithmeticError(f"isolated block certificate failed at delta={delta}")
    return eps,piv


def main() -> None:
    out = Path(__file__).resolve().parent
    max_corr_degree = max(CORR_DEGREES.values())
    max_radius = F(N - 1) * D + F(mixed.halfwidth_units(max_corr_degree)) * H
    exclusion_n = math.ceil(math.exp(float(max_radius)))
    while base.log_rational_iv(F(exclusion_n), 180).lo <= max_radius:
        exclusion_n += 1
    prime_powers = {
        n: p for n in range(2, exclusion_n) if (p := prime_power_base(n)) is not None
    }
    logs = {n: base.log_rational_iv(F(n), 210) for n in range(2, exclusion_n + 1)}
    sqrts = {n: base.sqrt_rational_iv(F(n), 140) for n in prime_powers}
    gamma = euler_gamma_binet_iv(100, 4)
    constant_total = base.log4pi_iv() + gamma

    def entry(corr_degree: int, center: F):
        f0 = mixed.f_value(corr_degree, H, center, F(0))
        endpoint = base.coarsen(
            mixed.integrate_f_exp(corr_degree, H, center, F(1, 2))
            + mixed.integrate_f_exp(corr_degree, H, center, F(-1, 2)),
            72,
        )
        constant = base.coarsen(-constant_total.scale(f0), 72)
        K = K_BY_CORR_DEGREE[corr_degree]
        arch, arch_audit = mixed.arch_series_generic(corr_degree, H, center, K)
        prime_total = base.IV.point(0)
        blocks = {}
        active = []
        for n, p in prime_powers.items():
            coeff = logs[p] / sqrts[n]
            plus = mixed.f_interval(corr_degree, H, center, logs[n])
            minus = mixed.f_interval(corr_degree, H, center, -logs[n])
            term = base.coarsen(-(coeff * (plus + minus)), 70)
            blocks[str(n)] = base.iv_json(term)
            prime_total = base.coarsen(prime_total + term, 70)
            if not (plus.lo == plus.hi == 0 and minus.lo == minus.hi == 0):
                active.append(n)
        prime_free = base.coarsen(endpoint + constant + arch, 68)
        total = base.coarsen(prime_free + prime_total, 68)
        left, right = mixed.support(corr_degree, H, center)
        return total, {
            "correlation_degree": corr_degree,
            "center": base.frac_json(center),
            "support": [base.frac_json(left), base.frac_json(right)],
            "f0": base.frac_json(f0),
            "endpoint": base.iv_json(endpoint),
            "constant": base.iv_json(constant),
            "arch": base.iv_json(arch),
            "prime_free": base.iv_json(prime_free),
            "prime_total": base.iv_json(prime_total),
            "prime_blocks": blocks,
            "active": active,
            "arch_audit": arch_audit,
            "total": base.iv_json(total),
        }

    lag_values = {}
    lag_audits = {}
    for pair, corr_degree in CORR_DEGREES.items():
        key = f"{pair[0]}x{pair[1]}"
        lag_values[key] = []
        lag_audits[key] = []
        for lag in range(N):
            value, audit = entry(corr_degree, F(lag) * D)
            lag_values[key].append(value)
            lag_audits[key].append(audit)
            print(
                f"block={key} lag={lag} degree={corr_degree} "
                f"width={float(value.width()):.3e} active={audit['active']}"
            )

    dim = len(BASIS_DEGREES) * N
    matrix = [[base.IV.point(0) for _ in range(dim)] for _ in range(dim)]
    gram = [[F(0) for _ in range(dim)] for _ in range(dim)]
    prime_matrices = {
        n: [[base.IV.point(0) for _ in range(dim)] for _ in range(dim)]
        for n in prime_powers
    }

    for ca, a in enumerate(BASIS_DEGREES):
        for cb, b in enumerate(BASIS_DEGREES):
            pair = (min(a, b), max(a, b))
            key = f"{pair[0]}x{pair[1]}"
            corr_degree = CORR_DEGREES[pair]
            for i in range(N):
                for j in range(N):
                    lag = abs(i - j)
                    I = ca * N + i
                    J = cb * N + j
                    matrix[I][J] = lag_values[key][lag]
                    gram[I][J] = mixed.f_value(corr_degree, H, F(i - j) * D, F(0))
                    for n in prime_powers:
                        prime_matrices[n][I][J] = parse_iv(
                            lag_audits[key][lag]["prime_blocks"][str(n)]
                        )

    # exact Gram positivity
    gram_ok, gram_pivots = ldlt(gram)
    if not gram_ok:
        raise ArithmeticError("mixed Gram matrix is not positive definite")

    Mfloat = np.array([[float(x.midpoint()) for x in row] for row in matrix])
    Gfloat = np.array([[float(x) for x in row] for row in gram])
    eigvals, eigvecs = eigh(Mfloat, Gfloat)
    v = eigvecs[:, 0]
    v1, v3 = v[:N], v[N:]

    center = [[grid_center(x) for x in row] for row in matrix]
    row_radii = [
        sum(
            max(abs(center[i][j] - matrix[i][j].lo), abs(matrix[i][j].hi - center[i][j]))
            for j in range(dim)
        )
        for i in range(dim)
    ]
    row_radius = max(row_radii)
    cert_matrix = [
        [
            center[i][j] - DELTA * gram[i][j] - (row_radius if i == j else F(0))
            for j in range(dim)
        ]
        for i in range(dim)
    ]
    cert_ok, cert_pivots = ldlt(cert_matrix)
    if not cert_ok:
        raise ArithmeticError(
            f"mixed certificate failed at delta={DELTA}; row_radius={float(row_radius):.3e}"
        )

    # Display-only channel and arithmetic attribution at the midpoint eigenvector.
    def quad(A, x, y=None):
        y = x if y is None else y
        return float(x @ A @ y)

    G11 = Gfloat[:N, :N]
    G13 = Gfloat[:N, N:]
    G33 = Gfloat[N:, N:]
    M11 = Mfloat[:N, :N]
    M13 = Mfloat[:N, N:]
    M33 = Mfloat[N:, N:]
    channel = {
        "coefficient_l2_fraction_m1": float(np.dot(v1, v1) / np.dot(v, v)),
        "coefficient_l2_fraction_m3": float(np.dot(v3, v3) / np.dot(v, v)),
        "gram_m1_self": quad(G11, v1),
        "gram_cross_twice": 2 * quad(G13, v1, v3),
        "gram_m3_self": quad(G33, v3),
        "weil_m1_self": quad(M11, v1),
        "weil_cross_twice": 2 * quad(M13, v1, v3),
        "weil_m3_self": quad(M33, v3),
    }
    prime_attribution = {}
    for n, Piv in prime_matrices.items():
        Pf = np.array([[float(x.midpoint()) for x in row] for row in Piv])
        prime_attribution[str(n)] = {
            "quadratic_contribution_on_lowest_midpoint_mode": quad(Pf, v),
            "m1_self": quad(Pf[:N, :N], v1),
            "cross_twice": 2 * quad(Pf[:N, N:], v1, v3),
            "m3_self": quad(Pf[N:, N:], v3),
        }

    # Single-channel comparison.
    eig11 = eigh(M11, G11, eigvals_only=True)
    eig33 = eigh(M33, G33, eigvals_only=True)

    # Exact isolated-channel lower bounds and a rational mixed upper witness.
    M11iv = block_interval(matrix, 0, N)
    M33iv = block_interval(matrix, N, N)
    G11ex = block_exact(gram, 0, N)
    G33ex = block_exact(gram, N, N)
    delta11 = F(1, 20)
    delta33 = F(1, 250)
    eps11, piv11 = certify_block(M11iv, G11ex, delta11)
    eps33, piv33 = certify_block(M33iv, G33ex, delta33)

    witness_scale = 10**7
    vmax = float(np.max(np.abs(v)))
    witness = [int(round(float(x) / vmax * witness_scale)) for x in v]
    if all(x == 0 for x in witness):
        raise ArithmeticError("zero rational witness")
    witness_q = interval_quadratic(matrix, witness)
    witness_g = exact_quadratic(gram, witness)
    witness_upper = F(1, 1000)
    if witness_q.hi >= witness_upper * witness_g:
        raise ArithmeticError("failed to certify mixed upper witness")
    w1, w3 = witness[:N], witness[N:]
    q11 = interval_quadratic(M11iv, w1)
    q33 = interval_quadratic(M33iv, w3)
    q13 = base.IV.point(0)
    for i in range(N):
        for j in range(N):
            q13 += matrix[i][N+j].scale(F(2*w1[i]*w3[j]))
    q13 = base.coarsen(q13, 60)
    witness_prime = {str(n): base.iv_json(interval_quadratic(Piv, witness)) for n, Piv in prime_matrices.items()}

    result = {
        "schema": "RH-W-12-mixed-order-dictionary-v0.1",
        "date": "2026-07-23",
        "status": "CERTIFIED_POSITIVE_ON_THIS_MIXED_SUBSPACE",
        "scope_warning": "Finite-dimensional positivity on this mixed dictionary does not imply RH.",
        "basis": {
            "basis_degrees": list(BASIS_DEGREES),
            "correlation_degrees": {f"{a}x{b}": r for (a, b), r in CORR_DEGREES.items()},
            "h": base.frac_json(H),
            "spacing": base.frac_json(D),
            "per_channel_dimension": N,
            "total_dimension": dim,
            "shifts": [base.frac_json(x) for x in SHIFTS],
            "definition": "v_{m,j}(x)=h^(-1/2) beta_m((x-t_j)/h), m in {1,3}",
        },
        "support": {
            "max_correlation_radius": base.frac_json(max_radius),
            "exclusion_n": exclusion_n,
            "log_exclusion_n": base.iv_json(logs[exclusion_n]),
            "all_n_ge_exclusion_n_excluded": True,
        },
        "prime_powers": {str(n): p for n, p in prime_powers.items()},
        "activation_graph": {
            key: {str(lag): audit[lag]["active"] for lag in range(N)}
            for key, audit in lag_audits.items()
        },
        "lag_entries": {
            key: {str(lag): base.iv_json(value) for lag, value in enumerate(values)}
            for key, values in lag_values.items()
        },
        "lag_audits": {
            key: {str(lag): audit for lag, audit in enumerate(audits)}
            for key, audits in lag_audits.items()
        },
        "matrix": [[base.iv_json(x) for x in row] for row in matrix],
        "gram": [[base.frac_json(x) for x in row] for row in gram],
        "gram_certificate": {
            "positive_definite": True,
            "ldlt_pivots": [base.frac_json(x) for x in gram_pivots],
        },
        "exploration_display_only": {
            "mixed_generalized_eigenvalues": [float(x) for x in eigvals],
            "m1_only_min": float(eig11[0]),
            "m3_only_min": float(eig33[0]),
            "lowest_mode_channel_attribution": channel,
            "prime_power_attribution": prime_attribution,
        },
        "certificate": {
            "delta": base.frac_json(DELTA),
            "grid_denominator": str(GRID),
            "row_radius": base.frac_json(row_radius),
            "row_radii": [base.frac_json(x) for x in row_radii],
            "ldlt_pivots": [base.frac_json(x) for x in cert_pivots],
            "method": "exact rational LDL^T on C-delta*G-row_radius*I",
            "meaning": "for every matrix in the interval family, c^T M c > delta c^T G c for every nonzero c",
        },
        "isolated_channel_certificates": {
            "m1_only": {
                "delta": base.frac_json(delta11),
                "row_radius": base.frac_json(eps11),
                "ldlt_pivots": [base.frac_json(x) for x in piv11],
                "meaning": "lambda_min(M11,G11)>1/20",
            },
            "m3_only": {
                "delta": base.frac_json(delta33),
                "row_radius": base.frac_json(eps33),
                "ldlt_pivots": [base.frac_json(x) for x in piv33],
                "meaning": "lambda_min(M33,G33)>1/250",
            },
        },
        "mixed_upper_witness": {
            "integer_vector": witness,
            "quadratic_interval": base.iv_json(witness_q),
            "gram_exact": base.frac_json(witness_g),
            "upper_ratio": base.frac_json(witness_upper),
            "certified_relation": "c^T M c < (1/1000) c^T G c",
            "channel_components": {
                "m1_self": base.iv_json(q11),
                "cross_twice": base.iv_json(q13),
                "m3_self": base.iv_json(q33),
            },
            "prime_power_components": witness_prime,
            "consequence": "1/2000 < lambda_min(mixed) < 1/1000, while isolated m3 > 1/250 and isolated m1 > 1/20",
        },
        "rigor_contract": {
            "floating_point_in_proof_path": False,
            "floating_point_role": "display-only generalized eigenspectrum and mode attribution",
            "prime_power_completeness": "all von Mangoldt nonzero n below the rigorously excluded threshold are enumerated",
            "archimedean_tail": "degree-specific signed derivative expansion for correlation degrees 3,5,7",
            "transcendentals": "rational log/arctan/sqrt enclosures plus documented outward Decimal.exp enclosure",
        },
    }
    path = out / "mixed_10x10_interval.json"
    path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    summary = [
        f"status={result['status']}",
        f"dimension={dim}",
        f"prime_powers={list(prime_powers)}",
        f"mixed_midpoint_generalized_min_display={eigvals[0]:.18e}",
        f"m1_only_min_display={eig11[0]:.18e}",
        f"m3_only_min_display={eig33[0]:.18e}",
        f"row_radius={float(row_radius):.18e}",
        f"delta={DELTA}",
        "RH_CLAIM=False",
    ]
    (out / "BUILD_SUMMARY.txt").write_text("\n".join(summary) + "\n", encoding="utf-8")
    print("\n".join(summary))
    print(path)


if __name__ == "__main__":
    main()
