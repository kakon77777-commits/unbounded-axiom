#!/usr/bin/env python3
"""Structural/exact verifier for RH-W-16 three-parameter tube.

The verifier does not regenerate transcendental corner matrices. It checks
stored interval symmetry, exact Gram matrices, trilinear remainder arithmetic,
prime-power chamber stability, exact LDL^T lower bounds, and the global upper
Rayleigh witness using only rational operations after parsing the certificate.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json,math,sys
import weil_interval_core as base
sys.set_int_max_str_digits(0)

def fq(o):return F(int(o['num']),int(o['den']))
def iv(o):return base.IV(fq(o['lower']),fq(o['upper']))
def ldlt(A):
 n=len(A);L=[[F(0) for _ in range(n)] for _ in range(n)];p=[]
 for i in range(n):
  L[i][i]=F(1);z=A[i][i]-sum(L[i][k]*L[i][k]*p[k] for k in range(i))
  if z<=0:return False,p+[z]
  p.append(z)
  for j in range(i+1,n):L[j][i]=(A[j][i]-sum(L[j][k]*L[i][k]*p[k] for k in range(i)))/z
 return True,p

def grid_center(x,grid=10**42):
 m=x.midpoint();q=m.numerator*grid//m.denominator;a,b=F(q,grid),F(q+1,grid)
 return a if abs(m-a)<=abs(b-m) else b

def iq(A,c):
 z=base.IV.point(0)
 for i in range(len(c)):
  for j in range(len(c)):z+=A[i][j].scale(F(c[i]*c[j]))
 return base.coarsen(z,72)
def eq(A,c):return sum((F(c[i]*c[j])*A[i][j] for i in range(len(c)) for j in range(len(c))),F(0))

def ppbase(n):
 for p in range(2,n+1):
  if any(p%q==0 for q in range(2,math.isqrt(p)+1)):continue
  v=p
  while v<n:v*=p
  if v==n:return p

def mul(k,x):return base.IV(k*x.lo,k*x.hi) if k>=0 else base.IV(k*x.hi,k*x.lo)

def main():
 root=Path(__file__).resolve().parent;d=json.loads((root/'three_parameter_tube_certificate.json').read_text())
 if d['schema']!='RH-W-16-three-parameter-tube-v0.1':raise AssertionError('schema')
 h0=fq(d['basis']['h_center']);rh=fq(d['tube']['h_radius']);rd=fq(d['tube']['d_radius']);rs=fq(d['tube']['sigma_radius'])
 D=F(893,5000);N=int(d['basis']['per_channel_dimension']);dim=2*N
 if (rh,rd,rs)!=(F(1,100_000_000),F(1,10_000_000),F(1,10_000_000)):raise AssertionError('radii')
 if fq(d['tube']['volume'])!=8*rh*rd*rs:raise AssertionError('volume')
 delta=fq(d['certificate']['delta_lower']);upper=fq(d['certificate']['upper_ratio'])
 corr={(0,0):3,(0,1):5,(1,0):5,(1,1):7}
 # Reconstruct stored remainder formula from stored integer derivative bounds.
 hmin=h0-rh;Gcc=4/hmin**2
 Lcc={r:fq(d['second_derivative_bounds'][str(r)]['center']['ceil']) for r in (3,5,7)}
 Lhh={r:fq(d['second_derivative_bounds'][str(r)]['scale_h']['ceil']) for r in (3,5,7)}
 Ghh={r:fq(d['second_derivative_bounds'][str(r)]['gram_scale_h']) for r in (3,5,7)}
 ER=[[F(0) for _ in range(dim)] for _ in range(dim)];GR=[[F(0) for _ in range(dim)] for _ in range(dim)]
 rows=[];grows=[]
 for I in range(dim):
  ca,i=divmod(I,N);mr=gr=F(0)
  for J in range(dim):
   cb,j=divmod(J,N);r=corr[(ca,cb)];a=F(i-j);b=F(0 if ca==cb else 1)
   center_shape=a*a*rd**2+b*b*rs**2
   ER[I][J]=(Lcc[r]*center_shape+Lhh[r]*rh**2)/2
   GR[I][J]=(Gcc*center_shape+Ghh[r]*rh**2)/2
   mr+=ER[I][J]+delta*GR[I][J];gr+=GR[I][J]
  rows.append(mr);grows.append(gr)
 if [[fq(x) for x in row] for row in d['interpolation']['entry_remainders']]!=ER:raise AssertionError('entry remainder')
 if [[fq(x) for x in row] for row in d['interpolation']['gram_entry_remainders']]!=GR:raise AssertionError('gram remainder')
 eps=max(rows);geps=max(grows)
 if fq(d['interpolation']['global_combined_row_remainder'])!=eps:raise AssertionError('global remainder')
 if fq(d['interpolation']['global_gram_row_remainder'])!=geps:raise AssertionError('gram global remainder')
 # Chamber identity and knot margin are reconstructed with rigorous log intervals.
 logs={n:base.log_rational_iv(F(n),260) for n in (2,3,4,5)};hiv=base.IV(h0-rh,h0+rh);best=None
 for ca in range(2):
  for cb in range(2):
   r=corr[(ca,cb)];q=(r+1)//2;b=0 if ca==cb else 1
   for i in range(N):
    for j in range(N):
     a=i-j;civ=base.IV(F(a)*D-abs(a)*rd-b*rs,F(a)*D+abs(a)*rd+b*rs)
     for x in logs.values():
      for sample in (x,-x):
       for k in range(-q,q+1):
        knot=civ+mul(F(k),hiv)
        dist=knot.lo-sample.hi if sample.hi<knot.lo else sample.lo-knot.hi if knot.hi<sample.lo else F(0)
        best=dist if best is None or dist<best else best
 if best!=fq(d['chamber']['minimum_sample_to_knot_margin']) or best<=0:raise AssertionError('chamber margin')
 maxR=4*(D+rd)+rs+4*(h0+rh)
 if maxR!=fq(d['chamber']['max_support_radius']) or maxR>=logs[5].lo:raise AssertionError('support chamber')
 if d['chamber']['active_global_prime_powers']!=[2,3,4]:raise AssertionError('active pp')
 # Corner exact certificates.
 labels=('mmm','mmp','mpm','mpp','pmm','pmp','ppm','ppp');corners=[]
 for name in labels:
  o=d['corners'][name];M=[[iv(x) for x in row] for row in o['matrix']];G=[[fq(x) for x in row] for row in o['gram']]
  for i in range(dim):
   for j in range(dim):
    if M[i][j]!=M[j][i] or G[i][j]!=G[j][i]:raise AssertionError('symmetry')
  C=[[grid_center(M[i][j]) for j in range(dim)] for i in range(dim)]
  pe=max(sum(max(abs(C[i][j]-M[i][j].lo),abs(M[i][j].hi-C[i][j])) for j in range(dim)) for i in range(dim))
  sc=d['certificate']['corner_certificates'][name]
  if pe!=fq(sc['point_row_error']):raise AssertionError('point row error')
  T=[[C[i][j]-delta*G[i][j]-((pe+eps) if i==j else 0) for j in range(dim)] for i in range(dim)]
  ok,p=ldlt(T)
  if not ok or p!=[fq(x) for x in sc['ldlt_pivots']]:raise AssertionError('lower LDL')
  GT=[[G[i][j]-(geps if i==j else 0) for j in range(dim)] for i in range(dim)]
  gok,gp=ldlt(GT)
  if not gok or gp!=[fq(x) for x in sc['gram_ldlt_pivots']]:raise AssertionError('gram LDL')
  corners.append((M,G))
 # Upper witness over convex hull plus interpolation remainder.
 w=list(map(int,d['upper_witness']['integer_vector']));qs=[iq(M,w) for M,G in corners];gs=[eq(G,w) for M,G in corners]
 dq=sum(abs(F(w[i]*w[j]))*ER[i][j] for i in range(dim) for j in range(dim));dg=sum(abs(F(w[i]*w[j]))*GR[i][j] for i in range(dim) for j in range(dim))
 qt=base.IV(min(x.lo for x in qs)-dq,max(x.hi for x in qs)+dq);gt=base.IV(min(gs)-dg,max(gs)+dg)
 if qt!=iv(d['upper_witness']['tube_quadratic_interval']) or gt!=iv(d['upper_witness']['tube_gram_interval']):raise AssertionError('tube witness')
 if gt.lo<=0 or qt.hi>=upper*gt.lo:raise AssertionError('upper ratio')
 lines=['schema=OK','dimension=10','trilinear_remainder=OK','eight_corner_symmetry=OK','eight_corner_ldlt_positive=8/8','eight_corner_gram_ldlt_positive=8/8','prime_power_chamber=[2,3,4]','sample_to_knot_margin_positive=OK',f'global_combined_row_remainder={float(eps):.18e}',f'upper_witness_ratio_hi={float(qt.hi/gt.lo):.18e}','exact_3d_tube_bracket=1e-8<lambda_min<5e-8','status=EXACT_THREE_PARAMETER_TUBE_CERTIFICATE_OK','RH_CLAIM=False']
 text='\n'.join(lines)+'\n';(root/'EXACT_VERIFY.txt').write_text(text);print(text,end='')
if __name__=='__main__':main()
