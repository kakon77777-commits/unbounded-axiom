#!/usr/bin/env python3
"""Fast exact-rational adapter for RH-W-15.

It trusts the stored outward transcendental enclosures under the round's documented
software contract, then independently checks symmetry, stored integer derivative
ceilings, tensor remainder arithmetic, exact LDL^T, upper witness, chamber metadata,
and the corrected W-14 audit. It intentionally does not recompute Binet/log/exp
series; the slower native verifier remains shipped beside it.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json,sys
import weil_interval_core as base
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent

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
def center(x,grid=10**42):
 m=x.midpoint();q=m.numerator*grid//m.denominator;a,b=F(q,grid),F(q+1,grid)
 return a if abs(m-a)<=abs(b-m) else b
def iq(A,c):
 z=base.IV.point(0)
 for i in range(len(c)):
  for j in range(len(c)):z+=A[i][j].scale(F(c[i]*c[j]))
 return base.coarsen(z,72)
def eq(A,c):return sum((F(c[i]*c[j])*A[i][j] for i in range(len(c)) for j in range(len(c))),F(0))

def main():
 d=json.loads((ROOT/'interval_taylor_tube_2d_certificate.json').read_text())
 assert d['schema']=='RH-W-15-interval-taylor-tube-v0.1'
 h=fq(d['basis']['h']);N=int(d['basis']['per_channel_dimension']);dim=2*N
 rd=fq(d['tube']['d_radius']);rs=fq(d['tube']['sigma_radius']);assert rd==rs==F(1,10_000_000)
 assert fq(d['tube']['radius_expansion_over_RH_W_14'])==25000
 delta=fq(d['certificate']['delta_lower']);upper=fq(d['certificate']['upper_ratio'])
 corr={(0,0):3,(0,1):5,(1,0):5,(1,1):7}
 L2={r:fq(d['second_derivative_bounds'][str(r)]['ceil']) for r in (3,5,7)}
 assert L2=={3:F(2494),5:F(3110),7:F(3697)}
 LG2=F(4,h**2);ER=[[F(0) for _ in range(dim)] for _ in range(dim)];GR=[[F(0) for _ in range(dim)] for _ in range(dim)]
 rows=[];grows=[]
 for I in range(dim):
  ca,i=divmod(I,N);mr=gr=F(0)
  for J in range(dim):
   cb,j=divmod(J,N);shape=(F((i-j)**2)*rd**2+(rs**2 if ca!=cb else 0))/2
   ER[I][J]=L2[corr[(ca,cb)]]*shape;GR[I][J]=LG2*shape;mr+=ER[I][J]+delta*GR[I][J];gr+=GR[I][J]
  rows.append(mr);grows.append(gr)
 assert [[fq(x) for x in row] for row in d['interpolation']['entry_remainders']]==ER
 assert [[fq(x) for x in row] for row in d['interpolation']['gram_entry_remainders']]==GR
 eps=max(rows);geps=max(grows);assert fq(d['interpolation']['global_combined_row_remainder'])==eps
 corners=[]
 for name in ('mm','mp','pm','pp'):
  o=d['corners'][name];M=[[iv(x) for x in row] for row in o['matrix']];G=[[fq(x) for x in row] for row in o['gram']]
  for i in range(dim):
   for j in range(dim):assert M[i][j]==M[j][i] and G[i][j]==G[j][i]
  C=[[center(M[i][j]) for j in range(dim)] for i in range(dim)]
  pe=max(sum(max(abs(C[i][j]-M[i][j].lo),abs(M[i][j].hi-C[i][j])) for j in range(dim)) for i in range(dim))
  sc=d['certificate']['corner_certificates'][name];assert fq(sc['point_row_error'])==pe and fq(sc['combined_remainder'])==eps
  T=[[C[i][j]-delta*G[i][j]-((pe+eps) if i==j else F(0)) for j in range(dim)] for i in range(dim)]
  ok,p=ldlt(T);assert ok and p==[fq(x) for x in sc['ldlt_pivots']]
  GT=[[G[i][j]-(geps if i==j else F(0)) for j in range(dim)] for i in range(dim)]
  gok,gp=ldlt(GT);assert gok and gp==[fq(x) for x in sc['gram_ldlt_pivots']]
  corners.append((M,G))
 w=list(map(int,d['upper_witness']['integer_vector']));qs=[iq(M,w) for M,G in corners];gs=[eq(G,w) for M,G in corners]
 dq=sum(abs(F(w[i]*w[j]))*ER[i][j] for i in range(dim) for j in range(dim));dg=sum(abs(F(w[i]*w[j]))*GR[i][j] for i in range(dim) for j in range(dim))
 qt=base.IV(min(x.lo for x in qs)-dq,max(x.hi for x in qs)+dq);gt=base.IV(min(gs)-dg,max(gs)+dg)
 assert qt==iv(d['upper_witness']['tube_quadratic_interval']) and gt==iv(d['upper_witness']['tube_gram_interval'])
 assert gt.lo>0 and qt.hi<upper*gt.lo
 rea=json.loads((ROOT/'RH-W-14_corrected_lipschitz_reaudit.json').read_text())
 assert rea['schema']=='RH-W-14-corrected-arch-tail-reaudit-v0.1'
 assert {k:fq(v) for k,v in rea['corrected_first_derivative_integer_bounds'].items()}=={'3':F(179),'5':F(218),'7':F(255)}
 assert all(fq(x)>0 for x in rea['ldlt_pivots']) and rea['original_conclusion_preserved'] is True
 assert d['chamber']['active_global_prime_powers']==[2,3,4]
 print('stored_transcendental_enclosures=TRUSTED_UNDER_DOCUMENTED_CONTRACT')
 print('tensor_interpolation_remainder=OK')
 print('corner_ldlt_positive=4/4')
 print('gram_corner_ldlt_positive=4/4')
 print('upper_witness=OK')
 print('RH-W-14_corrected_tail_reaudit=PASS')
 print('status=EXACT_INTERVAL_TAYLOR_TUBE_CERTIFICATE_OK')
 print('RH_CLAIM=False')
if __name__=='__main__':main()
