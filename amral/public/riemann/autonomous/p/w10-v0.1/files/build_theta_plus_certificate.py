#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json, math, sys
import numpy as np
from scipy.linalg import eigh

import weil_interval_core as core
from rigorous_refinement_tools import euler_gamma_binet_iv, arch_series_high_resolution

sys.set_int_max_str_digits(0)
H = F(87, 400)
D = F(117, 512) + F(1, 5000)
N = 15
SHIFTS = tuple(F(j - N // 2) * D for j in range(N))
GRID = 10**32
DELTA = F(1, 10**9)
core.H = H


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


def grid_center(x: core.IV) -> F:
    midpoint = x.midpoint()
    q = midpoint.numerator * GRID // midpoint.denominator
    left = F(q, GRID)
    right = F(q + 1, GRID)
    return left if abs(midpoint - left) <= abs(right - midpoint) else right


def main() -> None:
    out = Path(__file__).resolve().parent
    radius = F(N - 1) * D + 4 * H
    exclusion_n = math.ceil(math.exp(float(radius)))
    while core.log_rational_iv(F(exclusion_n), 180).lo <= radius:
        exclusion_n += 1
    nmax = exclusion_n - 1
    prime_powers = {
        n: p for n in range(2, nmax + 1) if (p := prime_power_base(n)) is not None
    }
    logs = {n: core.log_rational_iv(F(n), 200) for n in range(2, exclusion_n + 1)}
    sqrts = {n: core.sqrt_rational_iv(F(n), 130) for n in prime_powers}

    gamma = euler_gamma_binet_iv(100, 4)
    constant_total = core.log4pi_iv() + gamma

    def entry(center: F, K: int):
        f0 = core.f_value(center, F(0))
        endpoint = core.coarsen(
            core.integrate_f_exp(center, F(1, 2))
            + core.integrate_f_exp(center, F(-1, 2)),
            78,
        )
        constant = core.coarsen(-constant_total.scale(f0), 78)
        arch, arch_audit = arch_series_high_resolution(center, K)
        prime_total = core.IV.point(0)
        prime_blocks = {}
        active = []
        for n, p in prime_powers.items():
            coefficient = logs[p] / sqrts[n]
            plus = core.f_interval(center, logs[n])
            minus = core.f_interval(center, -logs[n])
            term = core.coarsen(-(coefficient * (plus + minus)), 78)
            prime_blocks[str(n)] = core.iv_json(term)
            prime_total = core.coarsen(prime_total + term, 78)
            if not (plus.lo == plus.hi == 0 and minus.lo == minus.hi == 0):
                active.append(n)
        prime_free = core.coarsen(endpoint + constant + arch, 75)
        total = core.coarsen(prime_free + prime_total, 75)
        left, right = core.support(center)
        return total, {
            "center": core.frac_json(center),
            "support": [core.frac_json(left), core.frac_json(right)],
            "f0": core.frac_json(f0),
            "endpoint": core.iv_json(endpoint),
            "constant": core.iv_json(constant),
            "arch": core.iv_json(arch),
            "prime_free": core.iv_json(prime_free),
            "prime_total": core.iv_json(prime_total),
            "prime_blocks": prime_blocks,
            "active": active,
            "arch_audit": arch_audit,
            "total": core.iv_json(total),
        }

    lags = []
    audits = []
    for lag in range(N):
        K = 500 if lag <= 2 else 180
        value, audit = entry(-F(lag) * D, K)
        lags.append(value)
        audits.append(audit)
        print(f"lag={lag} width={float(value.width()):.18e} active={audit['active']}")

    matrix = [[lags[abs(i - j)] for j in range(N)] for i in range(N)]
    gram = [[core.f_value(F(i - j) * D, F(0)) for j in range(N)] for i in range(N)]
    midpoint_matrix = np.array([[float(x.midpoint()) for x in row] for row in matrix])
    gram_float = np.array([[float(x) for x in row] for row in gram])
    exploratory_eigs = eigh(midpoint_matrix, gram_float, eigvals_only=True)

    center = [[grid_center(x) for x in row] for row in matrix]
    row_radius = max(
        sum(
            max(abs(center[i][j] - matrix[i][j].lo), abs(matrix[i][j].hi - center[i][j]))
            for j in range(N)
        )
        for i in range(N)
    )
    test_matrix = [
        [
            center[i][j] - DELTA * gram[i][j] - (row_radius if i == j else F(0))
            for j in range(N)
        ]
        for i in range(N)
    ]
    ok, pivots = ldlt(test_matrix)
    if not ok:
        raise ArithmeticError("failed to certify selected delta")

    log3 = logs[3]
    boundary_location = D + 4 * H
    boundary_gap = core.IV.point(boundary_location) - log3
    if boundary_gap.lo <= 0:
        raise ArithmeticError("expected lag-1 n=3 sample to be inside support")

    result = {
        "schema": "RH-W-10-theta-plus-certificate-v0.1",
        "date": "2026-07-23",
        "status": "CERTIFIED_POSITIVE_GENERALIZED_MARGIN",
        "basis": {
            "family": "translated normalized cubic B-splines",
            "h": core.frac_json(H),
            "spacing": core.frac_json(D),
            "dimension": N,
            "shifts": [core.frac_json(x) for x in SHIFTS],
        },
        "support": {
            "max_radius": core.frac_json(radius),
            "exclusion_n": exclusion_n,
            "log_exclusion_n": core.iv_json(logs[exclusion_n]),
            "all_n_ge_exclusion_n_excluded": True,
        },
        "prime_powers": {str(n): p for n, p in prime_powers.items()},
        "activation_boundary": {
            "lag": 1,
            "prime_power": 3,
            "boundary_equation": "log(3)=d+4h",
            "d_plus_4h": core.frac_json(boundary_location),
            "log3": core.iv_json(log3),
            "positive_gap_boundary_minus_log3": core.iv_json(boundary_gap),
            "n3_at_negative_sample_is_active": True,
        },
        "constants": {
            "euler_gamma": core.iv_json(gamma),
            "gamma_method": "digamma Binet expansion through B8 with signed first-omitted-term bound",
        },
        "lag_entries": {str(k): core.iv_json(v) for k, v in enumerate(lags)},
        "lag_audits": {str(k): audit for k, audit in enumerate(audits)},
        "matrix": [[core.iv_json(x) for x in row] for row in matrix],
        "gram": [[core.frac_json(x) for x in row] for row in gram],
        "exploration": {
            "midpoint_generalized_min_eigenvalue_display_only": float(exploratory_eigs[0]),
            "midpoint_generalized_max_eigenvalue_display_only": float(exploratory_eigs[-1]),
        },
        "certificate": {
            "delta": core.frac_json(DELTA),
            "grid_denominator": str(GRID),
            "row_radius": core.frac_json(row_radius),
            "pivots": [core.frac_json(x) for x in pivots],
            "method": "exact rational LDL^T on C-delta*G-row_radius*I",
            "meaning": "for every matrix in the interval family, c^T M c > delta c^T G c for all nonzero c",
        },
        "rigor_contract": {
            "floating_point_in_proof_path": False,
            "adaptive_search_role": "candidate generation only",
            "arch_tail": "signed derivative terms with rational power-tail continuation to cutoff 20000",
            "euler_gamma": "Binet/digamma signed remainder",
            "transcendentals": "rational series plus documented outward Decimal.exp enclosure",
        },
        "scope_warning": "Finite-dimensional positivity, even at 1e-9 generalized margin, does not imply RH.",
    }
    (out / "theta_plus_15x15_interval.json").write_text(
        json.dumps(result, indent=2), encoding="utf-8"
    )
    (out / "THETA_PLUS_BUILD_VALIDATION.txt").write_text(
        "\n".join([
            f"status={result['status']}",
            f"dimension={N}",
            f"prime_powers={len(prime_powers)}",
            f"midpoint_generalized_min_display={exploratory_eigs[0]:.18e}",
            f"row_radius={float(row_radius):.18e}",
            f"delta={DELTA}",
            f"boundary_inside_gap_lower={float(boundary_gap.lo):.18e}",
            "RH_CLAIM=False",
        ]) + "\n",
        encoding="utf-8",
    )
    print((out / "theta_plus_15x15_interval.json"))


if __name__ == "__main__":
    main()
