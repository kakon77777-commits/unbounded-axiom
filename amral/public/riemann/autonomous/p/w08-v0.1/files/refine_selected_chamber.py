#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json, math, sys
import numpy as np
from scipy.linalg import eigh
import weil_interval_core as core
from arch_tail_refinement import arch_series_iv_precise
sys.set_int_max_str_digits(0)
H=F(3,20);D=F(9,40);N=13;SHIFTS=tuple(F(j-N//2)*D for j in range(N));NMAX=27
core.H=H
LOG4PI=core.log4pi_iv(); GAMMA=core.euler_gamma_iv(10000); CONST=LOG4PI+GAMMA

def ppbase(n):
 for p in range(2,n+1):
  if any(p%d==0 for d in range(2,math.isqrt(p)+1)): continue
  q=p
  while q<n:q*=p
  if q==n:return p
 return None
PP={n:p for n in range(2,NMAX+1) if (p:=ppbase(n))}
LOGS={n:core.log_rational_iv(F(n),170) for n in range(2,NMAX+2)}
SQRTS={n:core.sqrt_rational_iv(F(n),110) for n in PP}

def entry(center,K):
 f0=core.f_value(center,F(0)); endpoint=core.coarsen(core.integrate_f_exp(center,F(1,2))+core.integrate_f_exp(center,F(-1,2)),60); constant=core.coarsen(-CONST.scale(f0),60); arch,aa=arch_series_iv_precise(center,K)
 left,right=core.support(center);radius=max(abs(left),abs(right));assert LOGS[NMAX+1].lo>radius
 blocks={};pt=core.IV.point(0);active=[]
 for n,p in PP.items():
  coeff=LOGS[p]/SQRTS[n];fp=core.f_interval(center,LOGS[n]);fm=core.f_interval(center,-LOGS[n]);term=core.coarsen(-(coeff*(fp+fm)),65);blocks[n]=term;pt=core.coarsen(pt+term,60)
  if not(fp.lo==fp.hi==0 and fm.lo==fm.hi==0):active.append(n)
 pf=core.coarsen(endpoint+constant+arch,55);total=core.coarsen(pf+pt,55)
 return total,{'center':core.frac_json(center),'support':[core.frac_json(left),core.frac_json(right)],'f0':core.frac_json(f0),'endpoint':core.iv_json(endpoint),'constant':core.iv_json(constant),'arch':core.iv_json(arch),'prime_free':core.iv_json(pf),'prime_total':core.iv_json(pt),'prime_blocks':{str(n):core.iv_json(v)for n,v in blocks.items()},'active':active,'arch_audit':aa,'total':core.iv_json(total)}

def ldlt(A):
 n=len(A);L=[[F(0)for _ in range(n)]for _ in range(n)];Ds=[]
 for i in range(n):
  L[i][i]=F(1);q=A[i][i]-sum(L[i][k]*L[i][k]*Ds[k]for k in range(i))
  if q<=0:return False,Ds+[q]
  Ds.append(q)
  for j in range(i+1,n):L[j][i]=(A[j][i]-sum(L[j][k]*L[i][k]*Ds[k]for k in range(i)))/q
 return True,Ds

def gc(x,grid=10**26):
 m=x.midpoint();q=m.numerator*grid//m.denominator;a=F(q,grid);b=F(q+1,grid);return a if abs(m-a)<=abs(b-m)else b

def main():
 out=Path(__file__).parent;lags=[];aud=[]
 for lag in range(N):
  K=500 if lag<=2 else 180
  print('lag',lag,'K',K,flush=True);v,a=entry(-F(lag)*D,K);lags.append(v);aud.append(a);print(v.decimal(15),'width',float(v.width()),'active',a['active'],flush=True)
 M=[[lags[abs(i-j)]for j in range(N)]for i in range(N)];G=[[core.f_value(F(i-j)*D,F(0))for j in range(N)]for i in range(N)]
 Mf=np.array([[float(x.midpoint())for x in row]for row in M]);Gf=np.array([[float(x)for x in row]for row in G]);ev=eigh(Mf,Gf,eigvals_only=True);print('gen min',ev[0])
 C=[[gc(x)for x in row]for row in M];eps=max(sum(max(abs(C[i][j]-M[i][j].lo),abs(M[i][j].hi-C[i][j]))for j in range(N))for i in range(N));print('eps',float(eps))
 cert=None
 for delta in [F(1,100000),F(1,200000),F(1,500000),F(1,1000000),F(1,2000000),F(1,5000000),F(0)]:
  A=[[C[i][j]-delta*G[i][j]-(eps if i==j else F(0))for j in range(N)]for i in range(N)];ok,p=ldlt(A);print('delta',delta,ok,float(p[-1]));
  if ok:cert=(delta,p);break
 res={'schema':'RH-W-08-refined-chamber-v0.1','date':'2026-07-23','status':'CERTIFIED_POSITIVE_GENERALIZED_MARGIN' if cert and cert[0]>0 else ('CERTIFIED_POSITIVE' if cert else 'INCONCLUSIVE'),'basis':{'family':'translated normalized cubic B-splines','h':core.frac_json(H),'spacing':core.frac_json(D),'dimension':N,'shifts':[core.frac_json(x)for x in SHIFTS]},'support':{'max_radius':core.frac_json(F(N-1)*D+4*H),'n_ge_28_excluded':True},'prime_powers':PP,'lag_entries':{str(k):core.iv_json(v)for k,v in enumerate(lags)},'lag_audits':{str(k):a for k,a in enumerate(aud)},'matrix':[[core.iv_json(x)for x in row]for row in M],'gram':[[core.frac_json(x)for x in row]for row in G],'exploration':{'midpoint_generalized_min_eigenvalue_display_only':float(ev[0])},'certificate':None if not cert else {'delta':core.frac_json(cert[0]),'row_radius':core.frac_json(eps),'pivots':[core.frac_json(x)for x in cert[1]],'method':'exact LDL on C-delta*G-epsilon*I','meaning':'for every matrix in the interval family, c^T M c > delta c^T G c for all nonzero c'},'rigor_contract':{'floating_point_in_proof_path':False,'arch_tail':'7 integrations by parts; signed p=3,5,7 tail intervals; p=8 remainder','euler_gamma':'harmonic/log enclosure at n=10000','transcendentals':'rational series plus documented outward Decimal.exp enclosure'},'scope_warning':'Finite-dimensional positivity does not imply RH.'}
 (out/'refined_13x13_interval.json').write_text(json.dumps(res,indent=2),encoding='utf-8')
 (out/'REFINEMENT_VALIDATION.txt').write_text(f"status={res['status']}\nmidpoint_generalized_min_display={ev[0]:.18e}\nrow_radius={float(eps):.18e}\ndelta={cert[0] if cert else 'NONE'}\nRH_CLAIM=False\n")
if __name__=='__main__':main()
