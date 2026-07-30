#!/usr/bin/env python3
"""Exact rational verifier for RH-W-06 prime-active certificates.

No floating-point operation participates in the checks.  The verifier proves:
1. the 2x2 matrix is positive on its stated subspace;
2. the 5x5 interval family is uniformly positive definite via a midpoint
   spectral margin and an exact row-sum perturbation bound;
3. c=(1,1,0,-1,-1) is negative for the artificial prime-free block but
   positive after the genuine n=2 von Mangoldt block is restored.

These are finite-dimensional local statements and do not imply RH.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent


class IV:
    def __init__(self, lo: F, hi: F):
        if lo > hi:
            raise ValueError('reversed interval')
        self.lo, self.hi = lo, hi

    def __add__(self, other: 'IV') -> 'IV':
        return IV(self.lo + other.lo, self.hi + other.hi)

    def __sub__(self, other: 'IV') -> 'IV':
        return IV(self.lo - other.hi, self.hi - other.lo)

    def scale(self, q: F) -> 'IV':
        return IV(self.lo*q, self.hi*q) if q >= 0 else IV(self.hi*q, self.lo*q)

    def midpoint(self) -> F:
        return (self.lo+self.hi)/2

    def radius(self) -> F:
        return (self.hi-self.lo)/2


def q(o: dict) -> F:
    return F(int(o['num']), int(o['den']))


def iv(o: dict) -> IV:
    return IV(q(o['lower']), q(o['upper']))


def exact_ldlt_positive(A: list[list[F]]) -> list[F]:
    n = len(A)
    L = [[F(0) for _ in range(n)] for _ in range(n)]
    D: list[F] = []
    for i in range(n):
        L[i][i] = F(1)
        di = A[i][i] - sum(L[i][k]*L[i][k]*D[k] for k in range(i))
        if di <= 0:
            raise ValueError(f'nonpositive exact pivot at {i}: {di}')
        D.append(di)
        for j in range(i+1,n):
            num = A[j][i] - sum(L[j][k]*L[i][k]*D[k] for k in range(i))
            L[j][i] = num/di
    return D


def quad_from_lags(lags: list[IV], c: list[int]) -> IV:
    out = IV(F(0),F(0))
    for i,ci in enumerate(c):
        for j,cj in enumerate(c):
            out = out + lags[abs(i-j)].scale(F(ci*cj))
    return out


def verify_2x2() -> list[str]:
    data=json.loads((BASE/'weil_matrix_prime2_2x2_interval.json').read_text(encoding='utf-8'))
    if data['scope_warning'] != 'Finite-dimensional positivity does not imply RH.':
        raise ValueError('2x2 scope warning missing')
    m11=iv(data['matrix']['M11']); m12=iv(data['matrix']['M12']); m22=iv(data['matrix']['M22'])
    if (m11.lo,m11.hi)!=(m22.lo,m22.hi):
        raise ValueError('2x2 translation symmetry failed')
    even=m11+m12; odd=m11-m12
    if even.lo<=0 or odd.lo<=0:
        raise ValueError('2x2 positivity not proved')
    p=iv(data['prime2_coupling_effect']['M12_prime_term'])
    if p.hi >= 0:
        raise ValueError('n=2 off-diagonal coupling is not strictly negative')
    return [
        '2x2=CERTIFIED_POSITIVE',
        f'2x2_even_lower={even.lo}',
        f'2x2_odd_lower={odd.lo}',
        f'2x2_prime_coupling_upper={p.hi}',
    ]


def verify_5x5() -> list[str]:
    data=json.loads((BASE/'weil_matrix_prime2_5x5_interval.json').read_text(encoding='utf-8'))
    if data['scope_warning'] != 'Finite-dimensional positivity does not imply RH.':
        raise ValueError('5x5 scope warning missing')
    lags=[iv(data['lag_entries'][f'T{k}']) for k in range(5)]
    prime=[iv(data['prime_lag_blocks'][f'P{k}']) for k in range(5)]
    free=[iv(data['prime_free_lag_entries'][f'A{k}']) for k in range(5)]

    # Exact midpoint spectral margin: C - delta I is positive definite.
    C=[[lags[abs(i-j)].midpoint() for j in range(5)] for i in range(5)]
    delta=F(1,200)  # 0.005
    B=[[C[i][j]-(delta if i==j else F(0)) for j in range(5)] for i in range(5)]
    pivots=exact_ldlt_positive(B)

    # Every admissible interval matrix A=C+E has ||E||_2 <= ||E||_infty.
    row_radii=[]
    for i in range(5):
        row_radii.append(sum(lags[abs(i-j)].radius() for j in range(5)))
    eps=max(row_radii)
    if eps >= delta:
        raise ValueError('interval perturbation exceeds spectral margin')
    uniform_lower=delta-eps

    # A single small integer witness displays the sign flip caused by prime 2.
    c=[1,1,0,-1,-1]
    q_free=quad_from_lags(free,c)
    q_prime=quad_from_lags(prime,c)
    q_full=quad_from_lags(lags,c)
    if q_free.hi >= 0:
        raise ValueError('prime-free negative witness not certified')
    if q_prime.lo <= 0:
        raise ValueError('prime-2 corrective contribution not positive on witness')
    if q_full.lo <= 0:
        raise ValueError('full witness positivity not certified')

    # Structural checks on which lags activate n=2.
    active=[data['lag_audits'][str(k)]['prime_audit']['n2_active'] for k in range(5)]
    if active != [False,False,True,True,True]:
        raise ValueError(f'unexpected activation pattern: {active}')
    if not all(data['lag_audits'][str(k)]['prime_audit']['n_ge_3_excluded'] for k in range(5)):
        raise ValueError('n>=3 exclusion missing')

    return [
        '5x5=CERTIFIED_POSITIVE',
        f'midpoint_margin_delta={delta}',
        f'max_interval_row_radius={eps}',
        f'uniform_eigenvalue_lower_bound={uniform_lower}',
        'exact_shifted_midpoint_ldlt_pivots=' + ','.join(str(x) for x in pivots),
        f'prime_free_witness_upper={q_free.hi}',
        f'prime2_witness_lower={q_prime.lo}',
        f'full_witness_lower={q_full.lo}',
        'activation_pattern=[False,False,True,True,True]',
    ]


def main() -> None:
    lines=['RH-W-06 EXACT RATIONAL VERIFIER']+verify_2x2()+verify_5x5()+[
        'FLOATING_POINT_USED=False',
        'RH_CLAIM=False',
        'ALL_CERTIFICATES_OK',
    ]
    (BASE/'EXACT_VERIFY.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print('\n'.join(lines))


if __name__=='__main__':
    main()
