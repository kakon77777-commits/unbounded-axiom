#!/usr/bin/env python3
"""Exact verifier for RH-W-07 multiprime chamber certificate.

Uses only Python integers and fractions.Fraction. It does not recompute
transcendental enclosures; it verifies the supplied interval matrix, support
audit consistency, midpoint-margin positive-definiteness certificate, and
strict witness sign flips.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json

GRID=10**20


def frac(o): return F(int(o['num']),int(o['den']))
def iv(o): return (frac(o['lower']),frac(o['upper']))

def grid_center(lo:F,hi:F)->F:
    m=(lo+hi)/2
    q=m.numerator*GRID//m.denominator
    a=F(q,GRID); b=F(q+1,GRID)
    return a if abs(m-a)<=abs(b-m) else b

def exact_ldlt(A):
    n=len(A); L=[[F(0) for _ in range(n)] for _ in range(n)]; D=[]
    for i in range(n):
        L[i][i]=F(1)
        d=A[i][i]-sum(L[i][k]*L[i][k]*D[k] for k in range(i))
        if d<=0: return False,D+[d]
        D.append(d)
        for j in range(i+1,n):
            num=A[j][i]-sum(L[j][k]*L[i][k]*D[k] for k in range(i))
            L[j][i]=num/d
    return True,D

def q_interval(M,c):
    lo=F(0); hi=F(0)
    for i,ci in enumerate(c):
        for j,cj in enumerate(c):
            a,b=M[i][j]; q=F(ci*cj)
            if q>=0: lo+=q*a; hi+=q*b
            else: lo+=q*b; hi+=q*a
    return lo,hi

def parse_audit_iv(o): return iv(o)

def main():
    path=Path(__file__).with_name('multiprime_9x9_interval.json')
    j=json.loads(path.read_text(encoding='utf-8'))
    assert j['schema']=='RH-W-07-multiprime-chamber-v0.1'
    assert j['rigor_contract']['floating_point_in_proof_path'] is False
    assert j['support_compiler']['all_nonzero_von_mangoldt_indices_below_8']==[2,3,4,5,7]
    expected=[[],[],[2],[2],[2,3],[2,3,4],[3,4],[3,4,5],[4,5,7]]
    got=[x['active_prime_powers'] for x in j['support_compiler']['active_by_lag']]
    assert got==expected,(got,expected)

    M=[[iv(x) for x in row] for row in j['matrix']]
    n=len(M)
    C=[[grid_center(*M[i][k]) for k in range(n)] for i in range(n)]
    eps=max(sum(max(abs(C[i][k]-M[i][k][0]),abs(M[i][k][1]-C[i][k])) for k in range(n)) for i in range(n))
    cert=j['positive_certificate']; assert cert is not None
    delta=frac(cert['delta']); stated_eps=frac(cert['interval_row_radius'])
    assert eps==stated_eps
    A=[[C[i][k]-(delta if i==k else F(0)) for k in range(n)] for i in range(n)]
    ok,pivots=exact_ldlt(A); assert ok and all(x>0 for x in pivots)
    assert delta-eps==frac(cert['certified_lower_margin']) and delta-eps>0

    # Reconstruct cumulative matrices from lag audits.
    audits=[j['lag_audits'][str(k)] for k in range(n)]
    stages=[set(),{2},{2,3},{2,3,4},{2,3,4,5},{2,3,4,5,7}]
    mats=[]
    for S in stages:
        lags=[]
        for a in audits:
            lo,hi=parse_audit_iv(a['prime_free'])
            for q in S:
                if str(q) in a['prime_blocks']:
                    x,y=parse_audit_iv(a['prime_blocks'][str(q)])
                    lo+=x; hi+=y
            lags.append((lo,hi))
        mats.append([[lags[abs(i-k)] for k in range(n)] for i in range(n)])

    for event in j['strict_witness_sign_flips']:
        added=set(event['added_prime_powers'])
        idx=next(i for i in range(1,len(stages)) if stages[i]-stages[i-1]==added)
        before=q_interval(mats[idx-1],event['vector'])
        after=q_interval(mats[idx],event['vector'])
        if event['direction']=='negative_to_positive':
            assert before[1]<0 and after[0]>0
        else:
            assert before[0]>0 and after[1]<0

    print('schema=OK')
    print('activation_graph=OK')
    print(f'dimension={n}')
    print(f'delta={delta}')
    print(f'interval_row_radius={eps}')
    print(f'certified_lower_margin={delta-eps}')
    print(f'ldlt_pivots_positive={len(pivots)}')
    print(f'strict_sign_flips={len(j["strict_witness_sign_flips"])}')
    print('status=CERTIFIED_POSITIVE_ON_THIS_9D_SUBSPACE')
    print('RH_CLAIM=False')

if __name__=='__main__': main()
