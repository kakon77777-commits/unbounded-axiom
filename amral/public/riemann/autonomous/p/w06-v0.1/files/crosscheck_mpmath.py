#!/usr/bin/env python3
"""Independent high-precision cross-check; never part of the proof path."""
from __future__ import annotations
import json
from math import comb
from pathlib import Path
import mpmath as mp

mp.mp.dps=80
H=mp.mpf(1)/10
SHIFTS=(-mp.mpf(3)/10,-mp.mpf(3)/20,mp.mpf(0),mp.mpf(3)/20,mp.mpf(3)/10)


def beta(m,x):
    s=mp.mpf(0)
    for k in range(m+2):
        y=x+mp.mpf(m+1)/2-k
        if y>0:
            s+=(-1)**k*comb(m+1,k)*y**m
    return s/mp.factorial(m)


def corr_lag(lag,x):
    center=SHIFTS[0]-SHIFTS[lag]
    return beta(7,(x-center)/H)


def entry(lag):
    center=SHIFTS[0]-SHIFTS[lag]
    left,right=center-4*H,center+4*H
    radius=max(abs(left),abs(right))
    f0=corr_lag(lag,0)
    endpoint=mp.quad(lambda x:corr_lag(lag,x)*(mp.exp(x/2)+mp.exp(-x/2)),[left,right])
    constant=-(mp.log(4*mp.pi)+mp.euler)*f0
    points={mp.mpf(0),radius}
    for k in range(-4,5):
        for q in (center+H*k,-center-H*k):
            if 0<q<radius: points.add(q)
    points=sorted(points)
    def integrand(x):
        if abs(x)<mp.mpf('1e-35'): return f0/2
        num=mp.exp(x/2)*(corr_lag(lag,x)+corr_lag(lag,-x))-2*f0
        return num/(mp.exp(x)-mp.exp(-x))
    local=mp.quad(integrand,points)
    tail=-f0*mp.log(mp.tanh(radius/2))
    arch=-local+tail
    prime=mp.mpf(0)
    if radius>=mp.log(2):
        prime=-(mp.log(2)/mp.sqrt(2))*(corr_lag(lag,mp.log(2))+corr_lag(lag,-mp.log(2)))
    return endpoint+constant+arch+prime


def q(o): return mp.mpf(o['num'])/mp.mpf(o['den'])


def main():
    base=Path(__file__).resolve().parent
    d=json.loads((base/'weil_matrix_prime2_5x5_interval.json').read_text(encoding='utf-8'))
    lines=['INDEPENDENT_FLOATING_CROSSCHECK_ONLY']
    for lag in range(5):
        x=entry(lag); o=d['lag_entries'][f'T{lag}']; lo=q(o['lower']);hi=q(o['upper']);ok=lo<=x<=hi
        lines += [f'T{lag}={mp.nstr(x,55)}',f'T{lag}_inside_interval={ok}']
        if not ok: raise SystemExit(f'T{lag} escaped interval')
    lines+=['CROSSCHECK_OK','RH_CLAIM=False']
    (base/'CROSSCHECK.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print('\n'.join(lines))

if __name__=='__main__':main()
