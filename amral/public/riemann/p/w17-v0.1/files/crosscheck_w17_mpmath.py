#!/usr/bin/env python3
"""80-digit floating crosscheck of event-sensitive RH-W-17 entries."""
from pathlib import Path
import json,math
import mpmath as mp
mp.mp.dps=80
ROOT=Path(__file__).resolve().parent

def q(o):return mp.mpf(o['num'])/mp.mpf(o['den'])
def beta(deg,z):
 h=mp.mpf(deg+1)/2;s=mp.mpf('0')
 for k in range(deg+2):
  y=z+h-k
  if y>0:s+=(-1)**k*math.comb(deg+1,k)*y**deg
 return s/math.factorial(deg)
def ppbase(n):
 for p in range(2,n+1):
  if any(p%r==0 for r in range(2,math.isqrt(p)+1)):continue
  v=p
  while v<n:v*=p
  if v==n:return p

def calc(deg,h,c):
 rad=mp.mpf(deg+1)/2*h;l,r=c-rad,c+rad;f=lambda x:beta(deg,(x-c)/h);f0=f(0);pts=[l+k*h for k in range(deg+2)]
 endpoint=mp.fsum(mp.quad(lambda x:f(x)*(mp.e**(x/2)+mp.e**(-x/2)),[a,b]) for a,b in zip(pts[:-1],pts[1:]))
 const=-(mp.log(4*mp.pi)+mp.euler)*f0;R=max(abs(l),abs(r));sp={mp.mpf('0'),R}
 for z in pts:
  if 0<z<R:sp.add(z)
  if 0<-z<R:sp.add(-z)
 sp=sorted(sp)
 def integrand(x):
  if abs(x)<mp.mpf('1e-35'):return f0/2
  return (mp.e**(x/2)*(f(x)+f(-x))-2*f0)/(mp.e**x-mp.e**(-x))
 local=mp.fsum(mp.quad(integrand,[a,b]) for a,b in zip(sp[:-1],sp[1:]))
 arch=-local+2*f0*mp.atanh(mp.e**(-R));prime=mp.mpf('0')
 for n in (2,3,4):
  p=ppbase(n);prime-=mp.log(p)/mp.sqrt(n)*(f(mp.log(n))+f(-mp.log(n)))
 return endpoint+const+arch+prime

def main():
 o=json.loads((ROOT/'chamber_subdivision_certificate.json').read_text());h=q(o['basis']['h']);lines=[];mx=mp.mpf('0')
 tests=[(0,4,3),(0,9,5),(5,9,7)]
 for key,p in sorted(o['points'].items(),key=lambda kv:q(kv[1]['d'])):
  d=q(p['d']);sh=[[(i-2)*d for i in range(5)],[(i-2)*d for i in range(5)]]
  for I,J,deg in tests:
   ca,i=divmod(I,5);cb,j=divmod(J,5);center=sh[ca][i]-sh[cb][j];val=calc(deg,h,center);z=p['matrix'][I][J];lo=q(z['lower']);hi=q(z['upper'])
   if not lo<=val<=hi:raise AssertionError((key,I,J,mp.nstr(val,30),mp.nstr(lo,30),mp.nstr(hi,30)))
   mx=max(mx,abs(val-(lo+hi)/2));lines.append(f'd={mp.nstr(d,12)} entry=({I},{J}) degree={deg} value={mp.nstr(val,28)} width={mp.nstr(hi-lo,6)}')
 lines += [f'max_midpoint_difference={mp.nstr(mx,12)}','status=CROSSCHECK_OK','rigor=HIGH_PRECISION_FLOATING_ONLY','RH_CLAIM=False']
 text='\n'.join(lines)+'\n';(ROOT/'CROSSCHECK.txt').write_text(text);print(text,end='')
if __name__=='__main__':main()
