#!/usr/bin/env python3
"""Exploratory local continuation across the lag-1 prime-3 support boundary.

Floating point is used only to describe the local mode.  It is not a proof path.
"""
from __future__ import annotations
import csv, json, math, sys
from pathlib import Path
import numpy as np
from scipy.linalg import eigh

SOURCE = Path('/mnt/data/RH_W_09_工程包_v0.1')
sys.path.insert(0, str(SOURCE))
import adaptive_continuation as ac

H = 87 / 400
N = 15
BOUNDARY_D = math.log(3.0) - 4.0 * H
MUS = [-8e-4,-4e-4,-2e-4,-1e-4,-5e-5,-1e-5,0.0,1e-5,5e-5,1e-4,2e-4,4e-4,8e-4]


def matrix_and_gram(d: float):
    lags = [ac.entry(round(-k*d, 13), round(H, 13)) for k in range(N)]
    M = np.array([[lags[abs(i-j)] for j in range(N)] for i in range(N)])
    glags = [ac.beta7(k*d/H) for k in range(N)]
    G = np.array([[glags[abs(i-j)] for j in range(N)] for i in range(N)])
    return M, G


def main():
    rows=[]
    previous=None
    for mu in MUS:
        d=BOUNDARY_D+mu
        M,G=matrix_and_gram(d)
        vals,vecs=eigh(M,G)
        v=vecs[:,0]
        if v.sum()>0: v=-v
        eu=v/np.linalg.norm(v)
        s1=float(sum(v[i]*v[i+1] for i in range(N-1)))
        parity=float(np.dot(eu,eu[::-1]))
        overlap=None if previous is None else float(abs(np.dot(eu,previous)))
        previous=eu
        rows.append({
            'mu':mu,'d':d,'lambda1':float(vals[0]),'lambda2':float(vals[1]),
            'gap12':float(vals[1]-vals[0]),'adjacent_correlation_S1':s1,
            'parity_reverse_overlap':parity,'successive_mode_overlap':overlap,
            'status':'FLOATING_EXPLORATION_ONLY'
        })
    out=Path(__file__).resolve().parent
    (out/'local_boundary_exploration.json').write_text(json.dumps({
        'schema':'RH-W-10-local-boundary-exploration-v0.1',
        'h':H,'dimension':N,'boundary_d':BOUNDARY_D,'rows':rows,
        'scope_warning':'Floating-point local mode study only; no proof status.'
    },indent=2),encoding='utf-8')
    with (out/'local_boundary_exploration.csv').open('w',newline='',encoding='utf-8-sig') as fh:
        w=csv.DictWriter(fh,fieldnames=list(rows[0].keys()));w.writeheader();w.writerows(rows)
    for r in rows:
        print(f"mu={r['mu']:+.1e} lambda1={r['lambda1']:.16e} gap12={r['gap12']:.16e} S1={r['adjacent_correlation_S1']:.9f}")

if __name__=='__main__': main()
