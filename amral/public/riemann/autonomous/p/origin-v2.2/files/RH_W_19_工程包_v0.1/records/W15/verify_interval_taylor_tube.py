#!/usr/bin/env python3
"""Pure-rational structural verifier for RH-W-15.

It does not regenerate transcendental corner enclosures.  It verifies their
symmetry, rational interval radii, chamber identity, tensor-interpolation
remainder, exact LDL^T lower bounds, the upper Rayleigh witness, and the
corrected RH-W-14 Lipschitz re-audit.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json,math,sys
import weil_interval_core as base
from rigorous_refinement_tools import euler_gamma_binet_iv
sys.set_int_max_str_digits(0)

def fq(o):return F(int(o['num']),int(o['den']))
def iv(o):return base.IV(fq(o['lower']),fq(o['upper']))
def fj(q):return base.frac_json(q)

def ldlt(A):
 n=len(A);L=[[F(0) for _ in range(n)] for _ in range(n)];p=[]
 for i in range(n):
  L[i][i]=F(1);z=A[i][i]-sum(L[i][k]*L[i][k]*p[k] for k in range(i))
  if z<=0:return False,p+[z]
  p.append(z)
  for j in range(i+1,n):L[j][i]=(A[j][i]-sum(L[j][k]*L[i][k]*p[k] for k in range(i)))/z
 return True,p

def grid_center(x,grid):
 m=x.midpoint();q=m.numerator*grid//m.denominator;a,b=F(q,grid),F(q+1,grid)
 return a if abs(m-a)<=abs(b-m) else b

def ppbase(n):
 for p in range(2,n+1):
  if any(p%q==0 for q in range(2,math.isqrt(p)+1)):continue
  v=p
  while v<n:v*=p
  if v==n:return p

def atanh_exp_minus_iv(R):
 e=base.exp_iv(-R,115)
 lr=(F(1)+e.lo)/(F(1)-e.lo);hr=(F(1)+e.hi)/(F(1)-e.hi)
 return base.coarsen(base.IV(base.log_rational_iv(lr,220).lo/2,base.log_rational_iv(hr,220).hi/2),70)

def coeff_sum(R):
 z=base.IV.point(0);act=[];n=2
 while base.log_rational_iv(F(n),220).lo<=R:
  p=ppbase(n)
  if p is not None:
   act.append(n);z+=base.log_rational_iv(F(p),220)/base.sqrt_rational_iv(F(n),160)
  n+=1
 return act,z

def first_bound(r,h,d0,rd,rs,N):
 q=F(r+1,2);R=F(N-1)*(d0+rd)+(rs if r==5 else 0)+q*h;e=base.exp_iv(R/2,110).hi
 const=(base.log4pi_iv()+euler_gamma_binet_iv(100,4)).hi;act,cs=coeff_sum(R)
 vals={'R':R,'active':act,'endpoint':4*q*e,'constant':const/h,'prime':2*cs.hi/h,
       'arch_inside':R*(e/(2*h)+4/h**2),'arch_outside':2*atanh_exp_minus_iv(R).hi/h}
 vals['total']=vals['endpoint']+vals['constant']+vals['prime']+vals['arch_inside']+vals['arch_outside']
 vals['ceil']=F((vals['total'].numerator+vals['total'].denominator-1)//vals['total'].denominator)
 return vals

def second_bound(r,h,d0,rd,rs,N):
 q=F(r+1,2);R=F(N-1)*(d0+rd)+(rs if r==5 else 0)+q*h;e=base.exp_iv(R/2,110).hi
 const=(base.log4pi_iv()+euler_gamma_binet_iv(100,4)).hi;act,cs=coeff_sum(R)
 vals={'R':R,'active':act,'endpoint':16*q*e/h,'constant':4*const/h**2,'prime':8*cs.hi/h**2,
       'arch_inside':R*(2*e/h**2+8/h**3),'arch_outside':8*atanh_exp_minus_iv(R).hi/h**2}
 vals['total']=vals['endpoint']+vals['constant']+vals['prime']+vals['arch_inside']+vals['arch_outside']
 vals['ceil']=F((vals['total'].numerator+vals['total'].denominator-1)//vals['total'].denominator)
 return vals

def iq(A,c):
 z=base.IV.point(0)
 for i in range(len(c)):
  for j in range(len(c)):z+=A[i][j].scale(F(c[i]*c[j]))
 return base.coarsen(z,72)
def eq(A,c):return sum((F(c[i]*c[j])*A[i][j] for i in range(len(c)) for j in range(len(c))),F(0))

def main():
 root=Path(__file__).resolve().parent
 d=json.loads((root/'interval_taylor_tube_2d_certificate.json').read_text())
 if d['schema']!='RH-W-15-interval-taylor-tube-v0.1':raise AssertionError('schema')
 h=fq(d['basis']['h']);N=int(d['basis']['per_channel_dimension']);dim=2*N
 D=fq(d['tube']['d_center']);rd=fq(d['tube']['d_radius']);rs=fq(d['tube']['sigma_radius'])
 if rd!=F(1,10_000_000) or rs!=rd:raise AssertionError('radii')
 if fq(d['tube']['radius_expansion_over_RH_W_14'])!=25000:raise AssertionError('expansion')
 corr={(0,0):3,(0,1):5,(1,0):5,(1,1):7};delta=fq(d['certificate']['delta_lower']);upper=fq(d['certificate']['upper_ratio']);grid=10**42
 # Bounds.
 L2={}
 for r in (3,5,7):
  got=second_bound(r,h,D,rd,rs,N);st=d['second_derivative_bounds'][str(r)]
  for k in ('R','endpoint','constant','prime','arch_inside','arch_outside','total','ceil'):
   if fq(st[k])!=got[k]:raise AssertionError(f'second {r} {k}')
  if st['active']!=got['active']:raise AssertionError('second active')
  L2[r]=got['ceil']
 # Remainders.
 LG2=F(4,h**2);ER=[[F(0) for _ in range(dim)] for _ in range(dim)];GR=[[F(0) for _ in range(dim)] for _ in range(dim)]
 rows=[];grows=[]
 for I in range(dim):
  ca,i=divmod(I,N);mr=gr=F(0)
  for J in range(dim):
   cb,j=divmod(J,N);shape=(F((i-j)**2)*rd**2+(F(1)*rs**2 if ca!=cb else 0))/2
   ER[I][J]=L2[corr[(ca,cb)]]*shape;GR[I][J]=LG2*shape;mr+=ER[I][J]+delta*GR[I][J];gr+=GR[I][J]
  rows.append(mr);grows.append(gr)
 if [[fq(x) for x in row] for row in d['interpolation']['entry_remainders']]!=ER:raise AssertionError('entry remainder')
 if [[fq(x) for x in row] for row in d['interpolation']['gram_entry_remainders']]!=GR:raise AssertionError('gram remainder')
 eps=max(rows);geps=max(grows)
 if fq(d['interpolation']['global_combined_row_remainder'])!=eps:raise AssertionError('eps')
 # Corners and exact LDL.
 corners=[]
 for name in ('mm','mp','pm','pp'):
  o=d['corners'][name];M=[[iv(x) for x in row] for row in o['matrix']];G=[[fq(x) for x in row] for row in o['gram']]
  for i in range(dim):
   for j in range(dim):
    if M[i][j]!=M[j][i] or G[i][j]!=G[j][i]:raise AssertionError('symmetry')
  C=[[grid_center(M[i][j],grid) for j in range(dim)] for i in range(dim)]
  pe=max(sum(max(abs(C[i][j]-M[i][j].lo),abs(M[i][j].hi-C[i][j])) for j in range(dim)) for i in range(dim))
  sc=d['certificate']['corner_certificates'][name]
  if fq(sc['point_row_error'])!=pe or fq(sc['combined_remainder'])!=eps:raise AssertionError('corner error')
  T=[[C[i][j]-delta*G[i][j]-((pe+eps) if i==j else 0) for j in range(dim)] for i in range(dim)]
  ok,p=ldlt(T)
  if not ok or [fq(x) for x in sc['ldlt_pivots']]!=p:raise AssertionError('corner LDL')
  GT=[[G[i][j]-(geps if i==j else 0) for j in range(dim)] for i in range(dim)]
  gok,gp=ldlt(GT)
  if not gok or [fq(x) for x in sc['gram_ldlt_pivots']]!=gp:raise AssertionError('gram LDL')
  corners.append((M,G))
 # Upper witness.
 w=list(map(int,d['upper_witness']['integer_vector']));qs=[iq(M,w) for M,G in corners];gs=[eq(G,w) for M,G in corners]
 dq=sum(abs(F(w[i]*w[j]))*ER[i][j] for i in range(dim) for j in range(dim));dg=sum(abs(F(w[i]*w[j]))*GR[i][j] for i in range(dim) for j in range(dim))
 qt=base.IV(min(x.lo for x in qs)-dq,max(x.hi for x in qs)+dq);gt=base.IV(min(gs)-dg,max(gs)+dg)
 if iv(d['upper_witness']['tube_quadratic_interval'])!=qt or iv(d['upper_witness']['tube_gram_interval'])!=gt:raise AssertionError('witness tube')
 if qt.hi>=upper*gt.lo:raise AssertionError('upper ratio')
 # Corrected W-14 re-audit.
 center=json.loads((root/'mixed_10x10_nearzero_interval.json').read_text());M0=[[iv(x) for x in row] for row in center['matrix']];G0=[[fq(x) for x in row] for row in center['gram']];C0=[[grid_center(M0[i][j],grid) for j in range(dim)] for i in range(dim)]
 oldr=F(4,10**12);L1={r:first_bound(r,h,D,oldr,oldr,N)['ceil'] for r in (3,5,7)}
 oldrows=[]
 for I in range(dim):
  ca,i=divmod(I,N);z=F(0)
  for J in range(dim):
   cb,j=divmod(J,N);var=F(abs(i-j))*oldr+(oldr if ca!=cb else 0);be=max(abs(C0[I][J]-M0[I][J].lo),abs(M0[I][J].hi-C0[I][J]))
   z+=be+L1[corr[(ca,cb)]]*var+delta*(F(1,h)*var)
  oldrows.append(z)
 oldeps=max(oldrows);T0=[[C0[i][j]-delta*G0[i][j]-(oldeps if i==j else 0) for j in range(dim)] for i in range(dim)];ook,op=ldlt(T0)
 if not ook:raise AssertionError('W14 corrected re-audit')
 rea={'schema':'RH-W-14-corrected-arch-tail-reaudit-v0.1','corrected_first_derivative_integer_bounds':{str(r):fj(L1[r]) for r in L1},'corrected_global_combined_row_bound':fj(oldeps),'ldlt_pivots':[fj(x) for x in op],'status':'RH-W-14_RECERTIFIED_WITH_SUPPORT_EXTERIOR_ARCHIMEDEAN_TAIL','original_conclusion_preserved':True,'RH_CLAIM':False}
 (root/'RH-W-14_corrected_lipschitz_reaudit.json').write_text(json.dumps(rea,indent=2))
 lines=['schema=OK','four_corner_matrices=OK','tensor_interpolation_remainder=OK',f'second_derivative_bounds={{{3}:{L2[3]},{5}:{L2[5]},{7}:{L2[7]}}}',f'global_second_order_row_remainder={float(eps):.18e}','corner_ldlt_positive=4/4','gram_corner_ldlt_positive=4/4','exact_tube_bracket=1e-8<lambda_min<5e-8','RH-W-14_corrected_tail_reaudit=PASS',f'RH-W-14_corrected_L={{{3}:{L1[3]},{5}:{L1[5]},{7}:{L1[7]}}}','status=EXACT_INTERVAL_TAYLOR_TUBE_CERTIFICATE_OK','RH_CLAIM=False']
 text='\n'.join(lines)+'\n';(root/'EXACT_VERIFY.txt').write_text(text);print(text,end='')
if __name__=='__main__':main()
