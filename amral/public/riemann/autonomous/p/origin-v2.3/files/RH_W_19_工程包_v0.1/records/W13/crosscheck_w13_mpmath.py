#!/usr/bin/env python3
"""80-digit independent floating crosscheck; not part of the proof path."""
from __future__ import annotations
from pathlib import Path
import json,math
import mpmath as mp
mp.mp.dps=80

def beta(deg,z):
 h=mp.mpf(deg+1)/2;s=mp.mpf('0')
 for k in range(deg+2):
  y=z+h-k
  if y>0:s+=(-1)**k*math.comb(deg+1,k)*y**deg
 return s/math.factorial(deg)

def ppbase(n):
 for p in range(2,n+1):
  if any(p%q==0 for q in range(2,math.isqrt(p)+1)):continue
  v=p
  while v<n:v*=p
  if v==n:return p
 return None

def calc(deg,h,c,ex):
 rad=mp.mpf(deg+1)/2*h;l,r=c-rad,c+rad;f=lambda x:beta(deg,(x-c)/h);f0=f(0);pts=[l+k*h for k in range(deg+2)]
 endpoint=mp.fsum(mp.quad(lambda x:f(x)*(mp.e**(x/2)+mp.e**(-x/2)),[a,b]) for a,b in zip(pts[:-1],pts[1:]))
 const=-(mp.log(4*mp.pi)+mp.euler)*f0;R=max(abs(l),abs(r));sp={mp.mpf('0'),R}
 for q in pts:
  if 0<q<R:sp.add(q)
  if 0<-q<R:sp.add(-q)
 sp=sorted(sp)
 def integrand(x):
  if abs(x)<mp.mpf('1e-45'):return f0/2
  return (mp.e**(x/2)*(f(x)+f(-x))-2*f0)/(mp.e**x-mp.e**(-x))
 local=mp.fsum(mp.quad(integrand,[a,b]) for a,b in zip(sp[:-1],sp[1:]));arch=-local+2*f0*mp.atanh(mp.e**(-R))
 prime=mp.mpf('0');active=[]
 for n in range(2,ex):
  p=ppbase(n)
  if p is None:continue
  x=mp.log(n);v=f(x)+f(-x)
  if abs(v)>mp.mpf('1e-65'):active.append(n)
  prime-=mp.log(p)/mp.sqrt(n)*v
 return endpoint+const+arch+prime,active

def main():
 root=Path(__file__).resolve().parent;o=json.loads((root/'mixed_10x10_nearzero_interval.json').read_text())
 h=mp.mpf(o['basis']['h']['num'])/mp.mpf(o['basis']['h']['den']);d=mp.mpf(o['basis']['spacing']['num'])/mp.mpf(o['basis']['spacing']['den']);ex=int(o['support']['exclusion_n'])
 mapping={'1x1':3,'1x3':5,'3x3':7};lines=[];mx=mp.mpf('0')
 for key,deg in mapping.items():
  for lag in range(5):
   val,active=calc(deg,h,lag*d,ex);I=o['lag_entries'][key][str(lag)];lo=mp.mpf(I['lower']['num'])/mp.mpf(I['lower']['den']);hi=mp.mpf(I['upper']['num'])/mp.mpf(I['upper']['den'])
   if not(lo<=val<=hi):raise AssertionError(f'{key} lag {lag} outside interval')
   if active!=o['activation_graph'][key][str(lag)]:raise AssertionError('activation')
   mx=max(mx,abs(val-(lo+hi)/2));lines.append(f'{key} lag={lag} value={mp.nstr(val,30)} width={mp.nstr(hi-lo,8)} active={active}')
 lines += [f'max_center_error={mp.nstr(mx,14)}','status=CROSSCHECK_OK','rigor=HIGH_PRECISION_FLOATING_ONLY','RH_CLAIM=False']
 text='\n'.join(lines)+'\n';(root/'CROSSCHECK.txt').write_text(text);print(text,end='')
if __name__=='__main__':main()
