#!/usr/bin/env python3
"""Pure-rational verifier for RH-W-08 refined 13x13 chamber.

It verifies the supplied interval matrix, exact Gram matrix, fixed-grid center,
row-radius perturbation, and exact LDL^T certificate for
C - delta G - epsilon I > 0.  It intentionally does not recompute
transcendental enclosures; that belongs to the interval-generation layer.
"""
from fractions import Fraction as F
from pathlib import Path
import json

GRID=10**26

def frac(o): return F(int(o['num']),int(o['den']))
def iv(o): return frac(o['lower']),frac(o['upper'])

def grid_center(lo,hi):
    m=(lo+hi)/2
    q=m.numerator*GRID//m.denominator
    a=F(q,GRID);b=F(q+1,GRID)
    return a if abs(m-a)<=abs(b-m) else b

def ldlt(A):
    n=len(A);L=[[F(0) for _ in range(n)] for _ in range(n)];D=[]
    for i in range(n):
        L[i][i]=F(1)
        d=A[i][i]-sum(L[i][k]*L[i][k]*D[k] for k in range(i))
        if d<=0:return False,D+[d]
        D.append(d)
        for j in range(i+1,n):
            L[j][i]=(A[j][i]-sum(L[j][k]*L[i][k]*D[k] for k in range(i)))/d
    return True,D

def main():
    p=Path(__file__).with_name('refined_13x13_interval.json')
    j=json.loads(p.read_text(encoding='utf-8'))
    assert j['schema']=='RH-W-08-refined-chamber-v0.1'
    assert j['status']=='CERTIFIED_POSITIVE_GENERALIZED_MARGIN'
    assert j['rigor_contract']['floating_point_in_proof_path'] is False
    assert j['basis']['dimension']==13
    assert sorted(map(int,j['prime_powers'].keys()))==[2,3,4,5,7,8,9,11,13,16,17,19,23,25,27]
    M=[[iv(x) for x in row] for row in j['matrix']]
    G=[[frac(x) for x in row] for row in j['gram']]
    n=len(M);assert n==13 and all(len(r)==n for r in M)
    C=[[grid_center(*M[i][k]) for k in range(n)] for i in range(n)]
    eps=max(sum(max(abs(C[i][k]-M[i][k][0]),abs(M[i][k][1]-C[i][k])) for k in range(n)) for i in range(n))
    cert=j['certificate'];delta=frac(cert['delta']);stated=frac(cert['row_radius'])
    assert eps==stated and delta==F(1,100000)
    A=[[C[i][k]-delta*G[i][k]-(eps if i==k else F(0)) for k in range(n)] for i in range(n)]
    ok,piv=ldlt(A);assert ok and all(x>0 for x in piv)
    stated_piv=[frac(x) for x in cert['pivots']]
    assert piv==stated_piv
    print('schema=OK')
    print('dimension=13')
    print('prime_power_enumeration=OK')
    print(f'row_radius={eps}')
    print(f'generalized_margin_delta={delta}')
    print(f'ldlt_pivots_positive={len(piv)}')
    print('status=CERTIFIED_POSITIVE_GENERALIZED_MARGIN')
    print('RH_CLAIM=False')
if __name__=='__main__':main()
