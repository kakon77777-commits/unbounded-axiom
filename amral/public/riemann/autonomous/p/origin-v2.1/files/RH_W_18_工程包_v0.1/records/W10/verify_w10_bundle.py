#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
from math import factorial
import json, sys, math
import weil_interval_core as core
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent
GRID=10**32

def fq(o): return F(int(o['num']),int(o['den']))
def iv(o): return core.IV(fq(o['lower']),fq(o['upper']))
def center(x):
 m=x.midpoint();q=m.numerator*GRID//m.denominator;a,b=F(q,GRID),F(q+1,GRID)
 return a if abs(m-a)<=abs(b-m) else b
def ldlt(A):
 n=len(A);L=[[F(0) for _ in range(n)] for _ in range(n)];p=[]
 for i in range(n):
  L[i][i]=F(1);z=A[i][i]-sum(L[i][k]*L[i][k]*p[k] for k in range(i))
  if z<=0:return False,p+[z]
  p.append(z)
  for j in range(i+1,n):L[j][i]=(A[j][i]-sum(L[j][k]*L[i][k]*p[k] for k in range(i)))/z
 return True,p

def ppbase(n):
 for p in range(2,n+1):
  if any(p%q==0 for q in range(2,math.isqrt(p)+1)):continue
  v=p
  while v<n:v*=p
  if v==n:return p
 return None

def main():
 t=json.loads((ROOT/'theta_plus_15x15_interval.json').read_text())
 assert t['schema']=='RH-W-10-theta-plus-certificate-v0.1'
 assert t['status']=='CERTIFIED_POSITIVE_GENERALIZED_MARGIN'
 assert t['rigor_contract']['floating_point_in_proof_path'] is False
 h=fq(t['basis']['h']);d=fq(t['basis']['spacing']);n=int(t['basis']['dimension'])
 assert h==F(87,400) and d==F(73189,320000) and n==15
 pp={k:ppbase(k) for k in range(2,int(t['support']['exclusion_n']))};pp={k:v for k,v in pp.items() if v}
 assert pp=={int(k):int(v) for k,v in t['prime_powers'].items()}
 gap=iv(t['activation_boundary']['positive_gap_boundary_minus_log3']);assert gap.lo>0
 assert t['activation_boundary']['n3_at_negative_sample_is_active'] is True
 M=[[iv(x) for x in row] for row in t['matrix']];G=[[fq(x) for x in row] for row in t['gram']]
 C=[[center(M[i][j]) for j in range(n)] for i in range(n)]
 e=max(sum(max(abs(C[i][j]-M[i][j].lo),abs(M[i][j].hi-C[i][j])) for j in range(n)) for i in range(n))
 cert=t['certificate'];assert e==fq(cert['row_radius']);delta=fq(cert['delta']);assert delta==F(1,10**9)
 A=[[C[i][j]-delta*G[i][j]-(e if i==j else F(0)) for j in range(n)] for i in range(n)]
 ok,p=ldlt(A);assert ok and p==[fq(x) for x in cert['pivots']]
 s=json.loads((ROOT/'prime3_soft_activation_certificate.json').read_text())
 assert s['schema']=='RH-W-10-prime3-soft-activation-v0.1'
 log3=core.log_rational_iv(F(3),220);sqrt3=core.sqrt_rational_iv(F(3),140)
 mu_minus=core.IV.point(fq(s['theta_minus']['d'])+4*h)-log3
 mu_plus=core.IV.point(fq(s['theta_plus']['d'])+4*h)-log3
 assert mu_minus.hi<0<mu_plus.lo
 eps=core.coarsen(mu_plus/core.IV.point(h),100)
 mag=core.coarsen((log3/sqrt3),100)
 for _ in range(7): mag=core.coarsen(mag*eps,100)
 predicted=-mag.scale(F(1,factorial(7)))
 stored=iv(s['theta_plus']['prime3_lag1_entry'])
 assert stored.lo<=predicted.lo and predicted.hi<=stored.hi or predicted.lo<=stored.lo and stored.hi<=predicted.hi
 assert s['boundary']['regularity']=='C^6 but not C^7 at mu=0'
 print('theta_plus_15d_ldlt=OK')
 print('prime3_mu_minus_inactive=OK')
 print('prime3_mu_plus_active=OK')
 print('seventh_order_soft_activation=OK')
 print('status=EXACT_W10_BUNDLE_CERTIFICATE_OK')
 print('RH_CLAIM=False')
if __name__=='__main__':main()
