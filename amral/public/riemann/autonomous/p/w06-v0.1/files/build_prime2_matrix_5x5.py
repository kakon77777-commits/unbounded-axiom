#!/usr/bin/env python3
"""Build a rigorous 5x5 prime-2-active Toeplitz Weil matrix.

This imports the exact interval machinery from build_prime_active_matrix.py.
The basis consists of five translated cubic B-splines.  The total correlation
support is below log(3), so n=2 is the only possible von Mangoldt sample.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json
import hashlib

import build_prime_active_matrix as core

SHIFTS5 = (F(-3,10), F(-3,20), F(0), F(3,20), F(3,10))
core.SHIFTS = SHIFTS5


def absmax(x: core.IV) -> F:
    return max(abs(x.lo), abs(x.hi))


def interval_ldlt(A: list[list[core.IV]]) -> tuple[bool, list[core.IV], list[list[core.IV]]]:
    n = len(A)
    L = [[core.IV.point(0) for _ in range(n)] for _ in range(n)]
    D: list[core.IV] = []
    for i in range(n):
        L[i][i] = core.IV.point(1)
        d = A[i][i]
        for k in range(i):
            d = d - L[i][k] * L[i][k] * D[k]
        d = core.coarsen(d, 35)
        D.append(d)
        if d.lo <= 0:
            return False, D, L
        for j in range(i+1, n):
            num = A[j][i]
            for k in range(i):
                num = num - L[j][k] * L[i][k] * D[k]
            L[j][i] = core.coarsen(num / d, 35)
    return True, D, L


def main() -> None:
    outdir = Path(__file__).resolve().parent
    n = len(SHIFTS5)

    # Translation invariance: compute one entry per lag.
    lag_values: dict[int, core.IV] = {}
    lag_audits: dict[int, dict] = {}
    for lag in range(n):
        val, audit = core.matrix_entry(0, lag, 240)
        lag_values[lag] = val
        lag_audits[lag] = audit

    A = [[lag_values[abs(i-j)] for j in range(n)] for i in range(n)]
    pd, pivots, L = interval_ldlt(A)

    # Gram matrix is also Toeplitz with exact rational entries.
    gram_lags = [core.f_value(SHIFTS5[0]-SHIFTS5[lag], F(0)) for lag in range(n)]
    G = [[gram_lags[abs(i-j)] for j in range(n)] for i in range(n)]

    # Prime block by lag, to make the support chamber visible.
    prime_lags = []
    prime_free_lags = []
    for lag in range(n):
        pa = lag_audits[lag]
        def parse_iv(obj: dict) -> core.IV:
            return core.IV(F(int(obj['lower']['num']), int(obj['lower']['den'])),
                           F(int(obj['upper']['num']), int(obj['upper']['den'])))
        prime_lags.append(parse_iv(pa['prime_term']))
        prime_free_lags.append(parse_iv(pa['prime_free_total']))

    result = {
        'schema': 'RH-W-06-prime2-toeplitz-5x5-v0.1',
        'date': '2026-07-23',
        'status': 'RAW_INTERVAL_BUILT_NATURAL_LDL_POSITIVE' if pd else 'RAW_INTERVAL_BUILT_NATURAL_LDL_INCONCLUSIVE',
        'scope_warning': 'Finite-dimensional positivity does not imply RH.',
        'basis': {
            'h': core.frac_json(core.H),
            'shifts': [core.frac_json(x) for x in SHIFTS5],
            'individual_support_radius': core.frac_json(2*core.H),
            'max_correlation_radius': core.frac_json(max(SHIFTS5)-min(SHIFTS5)+4*core.H),
            'toeplitz': True,
        },
        'support_chamber': {
            'active_von_mangoldt_indices': [2],
            'n_ge_3_excluded': True,
            'threshold_statement': 'max correlation support < log(3), while lags 2,3,4 cross log(2)',
        },
        'lag_entries': {f'T{lag}': core.iv_json(lag_values[lag]) for lag in range(n)},
        'prime_lag_blocks': {f'P{lag}': core.iv_json(prime_lags[lag]) for lag in range(n)},
        'prime_free_lag_entries': {f'A{lag}': core.iv_json(prime_free_lags[lag]) for lag in range(n)},
        'matrix': [[core.iv_json(A[i][j]) for j in range(n)] for i in range(n)],
        'interval_ldlt': {
            'positive_definite': pd,
            'pivots': [core.iv_json(x) for x in pivots],
            'method': 'natural interval LDL^T with exact rational endpoints',
        },
        'gram_exact': {
            'lags': [core.frac_json(x) for x in gram_lags],
            'matrix': [[core.frac_json(G[i][j]) for j in range(n)] for i in range(n)],
        },
        'lag_audits': {str(k): v for k,v in lag_audits.items()},
        'rigor_contract': {
            'floating_point_in_proof_path': False,
            'prime_completeness': 'support<log(3); n=2 evaluated by interval polynomial arithmetic',
            'transcendentals': 'rational series / integer sqrt / documented Decimal.exp enclosure',
            'claim': 'local 5D positivity only; no RH implication',
        },
    }

    path = outdir / 'weil_matrix_prime2_5x5_interval.json'
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')

    lines = [
        'RH-W-06 5x5 prime-2 Toeplitz build',
        f'status={result["status"]}',
        'lag_intervals=' + ', '.join(f'T{k}={lag_values[k].decimal(14)}' for k in range(n)),
        'prime_lags=' + ', '.join(f'P{k}={prime_lags[k].decimal(14)}' for k in range(n)),
        'ldlt_pivots=' + ', '.join(str(x.decimal(14)) for x in pivots),
        'FLOATING_POINT_IN_PROOF_PATH=False',
        'RH_CLAIM=False',
    ]
    (outdir / 'VALIDATION_5x5.txt').write_text('\n'.join(lines)+'\n', encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
