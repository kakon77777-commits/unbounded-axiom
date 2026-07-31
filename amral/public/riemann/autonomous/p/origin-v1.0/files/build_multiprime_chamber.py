#!/usr/bin/env python3
"""Compile a rigorous multi-prime-power support chamber for the Weil form.

Basis: nine translated normalized cubic B-splines with h=1/10 and shifts
-4/5,-3/5,...,4/5. Correlations are beta_7 splines. The maximum support
radius is 2, so all n>=8 are excluded by 2 < log(8). The nonzero von Mangoldt
indices that can occur are exactly 2,3,4,5,7.

The proof path uses integer/Fraction interval arithmetic plus the documented
Decimal.exp enclosure inherited from weil_interval_core.py. This is a local
finite-dimensional certificate only and makes no RH claim.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json
import math
import numpy as np

import weil_interval_core as core

H = F(1,10)
SHIFTS = tuple(F(k,5) for k in range(-4,5))
NMAX = 7
PRIME_POWERS = {2:2,3:3,4:2,5:5,7:7}  # n -> prime base, Lambda(n)=log(p)


def parse_iv(obj: dict) -> core.IV:
    return core.IV(F(int(obj['lower']['num']), int(obj['lower']['den'])),
                   F(int(obj['upper']['num']), int(obj['upper']['den'])))


def prime_power_base(n: int) -> int | None:
    return PRIME_POWERS.get(n)


def matrix_entry_center(center: F, K: int = 220) -> tuple[core.IV, dict]:
    f0 = core.f_value(center, F(0))
    endpoint = core.coarsen(core.integrate_f_exp(center, F(1,2)) + core.integrate_f_exp(center, F(-1,2)), 45)
    constant = core.coarsen(-(core.log4pi_iv() + core.euler_gamma_iv(100)).scale(f0), 45)
    arch, arch_audit = core.arch_series_iv(center, K)
    left, right = core.support(center)
    radius = max(abs(left), abs(right))

    log8 = core.log_rational_iv(F(8), 140)
    if not log8.lo > radius:
        raise AssertionError(f'n>=8 exclusion failed: radius={radius}')

    prime_blocks: dict[int, core.IV] = {}
    prime_audits: list[dict] = []
    prime_total = core.IV.point(0)
    for n in range(2, NMAX+1):
        p = prime_power_base(n)
        if p is None:
            prime_audits.append({
                'n': n, 'lambda_nonzero': False, 'reason': 'not a prime power',
                'term': core.iv_json(core.IV.point(0)),
            })
            continue
        logn = core.log_rational_iv(F(n), 140)
        logp = core.log_rational_iv(F(p), 140)
        sqrtn = core.sqrt_rational_iv(F(n), 100)
        coeff = logp / sqrtn
        # Evaluate each orientation; interval evaluation itself proves zero if outside support.
        fplus = core.f_interval(center, logn)
        fminus = core.f_interval(center, -logn)
        term = core.coarsen(-(coeff * (fplus + fminus)), 50)
        prime_blocks[n] = term
        prime_total = core.coarsen(prime_total + term, 45)
        prime_audits.append({
            'n': n,
            'prime_base': p,
            'lambda_nonzero': True,
            'log_n': core.iv_json(logn),
            'log_p': core.iv_json(logp),
            'sqrt_n': core.iv_json(sqrtn),
            'coefficient_lambda_over_sqrt_n': core.iv_json(coeff),
            'f_plus': core.iv_json(fplus),
            'f_minus': core.iv_json(fminus),
            'active': not (fplus.lo == fplus.hi == 0 and fminus.lo == fminus.hi == 0),
            'term': core.iv_json(term),
        })

    prime_free = core.coarsen(endpoint + constant + arch, 40)
    total = core.coarsen(prime_free + prime_total, 40)
    audit = {
        'center': core.frac_json(center),
        'support': [core.frac_json(left), core.frac_json(right)],
        'radius': core.frac_json(radius),
        'f0': core.frac_json(f0),
        'endpoint': core.iv_json(endpoint),
        'constant': core.iv_json(constant),
        'arch': core.iv_json(arch),
        'prime_free': core.iv_json(prime_free),
        'prime_total': core.iv_json(prime_total),
        'prime_blocks': {str(n): core.iv_json(v) for n,v in prime_blocks.items()},
        'prime_audits': prime_audits,
        'arch_audit': arch_audit,
        'total': core.iv_json(total),
        'n_ge_8_excluded': True,
        'log8': core.iv_json(log8),
    }
    return total, audit


def exact_ldlt_positive(A: list[list[F]]) -> tuple[bool, list[F]]:
    n=len(A)
    L=[[F(0) for _ in range(n)] for _ in range(n)]
    D=[]
    for i in range(n):
        L[i][i]=F(1)
        d=A[i][i]-sum(L[i][k]*L[i][k]*D[k] for k in range(i))
        D.append(d)
        if d <= 0:
            return False,D
        for j in range(i+1,n):
            num=A[j][i]-sum(L[j][k]*L[i][k]*D[k] for k in range(i))
            L[j][i]=num/d
    return True,D


def matrix_from_lags(lags: list[core.IV]) -> list[list[core.IV]]:
    n=len(SHIFTS)
    return [[lags[abs(i-j)] for j in range(n)] for i in range(n)]


def midpoint_float(A: list[list[core.IV]]) -> np.ndarray:
    return np.array([[float(x.midpoint()) for x in row] for row in A],dtype=float)


def interval_radius_row_bound(A: list[list[core.IV]]) -> F:
    return max(sum((x.width()/2 for x in row),F(0)) for row in A)


def rational_witness_interval(A: list[list[core.IV]], c: list[int]) -> core.IV:
    out=core.IV.point(0)
    for i,ci in enumerate(c):
        for j,cj in enumerate(c):
            out=out + A[i][j].scale(F(ci*cj))
    return out


def cumulative_lags(audits: list[dict], active_set: set[int]) -> list[core.IV]:
    out=[]
    for aud in audits:
        val=parse_iv(aud['prime_free'])
        for n in active_set:
            block=aud['prime_blocks'].get(str(n))
            if block:
                val=core.coarsen(val+parse_iv(block),40)
        out.append(val)
    return out


def main() -> None:
    outdir=Path(__file__).resolve().parent
    lags=[]; audits=[]
    for lag in range(len(SHIFTS)):
        center=SHIFTS[0]-SHIFTS[lag]
        val,aud=matrix_entry_center(center,1000 if lag <= 1 else 100)
        lags.append(val); audits.append(aud)

    A=matrix_from_lags(lags)
    # Use a fixed decimal rational center to keep exact LDL arithmetic bounded.
    # The displacement from the true interval midpoint is added to the radius.
    GRID=10**20
    def grid_center(x: core.IV) -> F:
        m=x.midpoint()
        q=m.numerator*GRID//m.denominator
        lo=F(q,GRID); hi=F(q+1,GRID)
        return lo if abs(m-lo)<=abs(hi-m) else hi
    C=[[grid_center(x) for x in row] for row in A]
    eps=max(sum((max(abs(C[i][j]-A[i][j].lo),abs(A[i][j].hi-C[i][j])) for j in range(len(A))),F(0)) for i in range(len(A)))
    evals=np.linalg.eigvalsh(midpoint_float(A))
    min_eval=float(evals[0])

    # Find a simple rational spectral margin below the numerical minimum and above epsilon.
    candidates=[F(1,200),F(1,500),F(1,1000),F(1,2000),F(1,5000),F(1,10000)]
    delta=None; pivots=[]
    for d in candidates:
        shifted=[[C[i][j]-(d if i==j else F(0)) for j in range(len(C))] for i in range(len(C))]
        ok,p=exact_ldlt_positive(shifted)
        if ok and d>eps:
            delta=d; pivots=p; break

    stages=[set(),{2},{2,3},{2,3,4},{2,3,4,5},{2,3,4,5,7}]
    stage_data=[]
    stage_mats=[]
    for s in stages:
        sl=cumulative_lags(audits,s)
        M=matrix_from_lags(sl)
        stage_mats.append(M)
        ev=np.linalg.eigvalsh(midpoint_float(M))
        stage_data.append({
            'active_prime_powers': sorted(s),
            'midpoint_min_eigenvalue_display_only': float(ev[0]),
            'midpoint_inertia_display_only': {
                'negative': int(np.sum(ev < -1e-10)),
                'near_zero': int(np.sum(np.abs(ev)<=1e-10)),
                'positive': int(np.sum(ev > 1e-10)),
            },
        })

    # Recheck a small fixed set of candidate sign-flip witnesses discovered
    # in the exploratory pass. Only interval-certified flips are emitted.
    witness_events=[]
    fixed_candidates={
        1:[3,-3,-8,-6,0,6,8,3,-3],
        2:[12,2,-16,-16,-9,-16,-16,2,12],
        3:[2,1,-2,-2,0,2,2,-1,-2],
        4:[16,9,2,2,0,-2,-2,-9,-16],
        5:[1,1,1,1,1,1,1,1,1],
    }
    for k in range(1,len(stage_mats)):
        c=fixed_candidates[k]
        qb=rational_witness_interval(stage_mats[k-1],c)
        qa=rational_witness_interval(stage_mats[k],c)
        if (qb.hi<0 and qa.lo>0) or (qb.lo>0 and qa.hi<0):
            witness_events.append({
                'added_prime_powers':sorted(stages[k]-stages[k-1]),
                'vector':c,
                'before':core.iv_json(qb),
                'after':core.iv_json(qa),
                'direction':'negative_to_positive' if qb.hi<0 else 'positive_to_negative',
            })
    active_by_lag=[]
    for lag,aud in enumerate(audits):
        active=[]
        for pa in aud['prime_audits']:
            if pa.get('active'): active.append(pa['n'])
        active_by_lag.append({'lag':lag,'center_abs':core.frac_json(abs(SHIFTS[0]-SHIFTS[lag])),'radius':aud['radius'],'active_prime_powers':active})

    result={
        'schema':'RH-W-07-multiprime-chamber-v0.1',
        'date':'2026-07-23',
        'status':'CERTIFIED_POSITIVE_ON_THIS_9D_SUBSPACE' if delta is not None else 'RAW_INTERVAL_BUILT_CERTIFICATE_INCONCLUSIVE',
        'scope_warning':'Finite-dimensional positivity does not imply RH.',
        'basis':{
            'family':'translated normalized cubic B-splines; correlations beta_7',
            'h':core.frac_json(H),
            'shifts':[core.frac_json(x) for x in SHIFTS],
            'dimension':len(SHIFTS),
            'max_correlation_radius':core.frac_json(F(2)),
            'toeplitz':True,
        },
        'support_compiler':{
            'all_nonzero_von_mangoldt_indices_below_8':[2,3,4,5,7],
            'n_ge_8_excluded_by':'2 < log(8)',
            'active_by_lag':active_by_lag,
        },
        'lag_entries':{f'T{k}':core.iv_json(v) for k,v in enumerate(lags)},
        'lag_audits':{str(k):v for k,v in enumerate(audits)},
        'matrix':[[core.iv_json(x) for x in row] for row in A],
        'positive_certificate':None if delta is None else {
            'method':'exact rational LDL^T on midpoint-delta*I plus interval row-radius perturbation',
            'delta':core.frac_json(delta),
            'interval_row_radius':core.frac_json(eps),
            'certified_lower_margin':core.frac_json(delta-eps),
            'midpoint_shifted_ldlt_pivots':[core.frac_json(x) for x in pivots],
        },
        'cumulative_prime_power_stages':stage_data,
        'strict_witness_sign_flips':witness_events,
        'display_only_midpoint_spectrum':evals.tolist(),
        'rigor_contract':{
            'floating_point_in_proof_path':False,
            'display_only_numpy_used_for':'exploration and reporting only; not certificate',
            'prime_completeness':'all n=2,...,7 audited; only prime powers have Lambda(n)!=0; n>=8 excluded by support<log(8)',
            'transcendentals':'rational series / integer sqrt / documented Decimal.exp outward enclosure',
            'claim':'local 9D positivity only; no RH implication',
        },
    }
    (outdir/'multiprime_9x9_interval.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    lines=[
        'RH-W-07 multiprime chamber build',
        f'status={result["status"]}',
        'active_by_lag='+str([x['active_prime_powers'] for x in active_by_lag]),
        'lag_intervals='+', '.join(f'T{k}={lags[k].decimal(12)}' for k in range(len(lags))),
        f'midpoint_min_eigenvalue_display_only={min_eval:.16e}',
        f'interval_row_radius={float(eps):.16e}',
        'delta='+('NONE' if delta is None else str(delta)),
        'certified_margin='+('NONE' if delta is None else f'{float(delta-eps):.16e}'),
        f'witness_sign_flips={len(witness_events)}',
        'FLOATING_POINT_IN_PROOF_PATH=False',
        'RH_CLAIM=False',
    ]
    (outdir/'VALIDATION.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print('\n'.join(lines))

if __name__=='__main__':
    main()
