#!/usr/bin/env python3
"""Independent high-precision floating crosscheck; not part of proof path."""
from __future__ import annotations
from pathlib import Path
import json, math
import mpmath as mp

mp.mp.dps = 80


def beta(deg, z):
    half = mp.mpf(deg + 1) / 2
    total = mp.mpf('0')
    for k in range(deg + 2):
        y = z + half - k
        if y > 0:
            total += (-1)**k * math.comb(deg+1,k) * y**deg
    return total / math.factorial(deg)


def pp_base(n):
    for p in range(2,n+1):
        if any(p%q==0 for q in range(2,math.isqrt(p)+1)):
            continue
        v=p
        while v<n:v*=p
        if v==n:return p
    return None


def calc(deg,h,center,exclusion):
    radius=mp.mpf(deg+1)/2*h
    left,right=center-radius,center+radius
    f=lambda x: beta(deg,(x-center)/h)
    f0=f(mp.mpf('0'))
    pts=[left + k*h for k in range(deg+2)]
    endpoint=mp.fsum(mp.quad(lambda x:f(x)*(mp.e**(x/2)+mp.e**(-x/2)),[a,b]) for a,b in zip(pts[:-1],pts[1:]))
    const=-(mp.log(4*mp.pi)+mp.euler)*f0
    maxr=max(abs(left),abs(right))
    split={mp.mpf('0'),maxr}
    for q in pts:
        if 0<q<maxr:split.add(q)
        if 0<-q<maxr:split.add(-q)
    sp=sorted(split)
    def integrand(x):
        if abs(x) < mp.mpf('1e-50'): return f0/2
        return (mp.e**(x/2)*(f(x)+f(-x))-2*f0)/(mp.e**x-mp.e**(-x))
    local=mp.fsum(mp.quad(integrand,[a,b]) for a,b in zip(sp[:-1],sp[1:]))
    tail=mp.quad(lambda x:2*f0/(mp.e**x-mp.e**(-x)),[maxr,mp.inf])
    arch=-local+tail
    prime=mp.mpf('0')
    active=[]
    for n in range(2,exclusion):
        p=pp_base(n)
        if p is None:continue
        x=mp.log(n)
        val=f(x)+f(-x)
        if abs(val)>mp.mpf('1e-70'):
            active.append(n)
        prime-=mp.log(p)/mp.sqrt(n)*val
    return endpoint+const+arch+prime,active


def main():
    root=Path(__file__).resolve().parent
    obj=json.loads((root/'mixed_10x10_interval.json').read_text())
    h=mp.mpf(3)/20;d=mp.mpf(9)/40;ex=int(obj['support']['exclusion_n'])
    mapping={'1x1':3,'1x3':5,'3x3':7}
    lines=[]
    max_center_error=mp.mpf('0')
    for key,deg in mapping.items():
        for lag in range(5):
            val,active=calc(deg,h,lag*d,ex)
            I=obj['lag_entries'][key][str(lag)]
            lo=mp.mpf(I['lower']['num'])/mp.mpf(I['lower']['den'])
            hi=mp.mpf(I['upper']['num'])/mp.mpf(I['upper']['den'])
            if not (lo <= val <= hi):
                raise AssertionError(f'{key} lag {lag} crosscheck outside interval: {val} not in [{lo},{hi}]')
            center=(lo+hi)/2
            err=abs(val-center)
            max_center_error=max(max_center_error,err)
            if active != obj['activation_graph'][key][str(lag)]:
                raise AssertionError('active set mismatch')
            lines.append(f'{key} lag={lag} value={mp.nstr(val,25)} interval_width={mp.nstr(hi-lo,8)} active={active}')
    lines += [
        f'max_center_error={mp.nstr(max_center_error,12)}',
        'status=CROSSCHECK_OK',
        'rigor=HIGH_PRECISION_FLOATING_ONLY',
        'RH_CLAIM=False',
    ]
    text='\n'.join(lines)+'\n'
    (root/'CROSSCHECK.txt').write_text(text,encoding='utf-8')
    print(text,end='')

if __name__=='__main__':main()
