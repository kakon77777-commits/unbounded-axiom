#!/usr/bin/env python3
"""RH-W-16: rigorous three-parameter (h,d,sigma) tube.

Eight rigorous corner matrices are combined by tensor-product trilinear
interpolation. Pure second-derivative bounds in the center coordinate and in
scale h control the interpolation remainder. All final matrix certificates are
exact rational LDL^T checks. Finite-dimensional only; no RH claim.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json, math, sys

import weil_interval_core as base
import mixed_order_core as mixed
import build_interval_taylor_tube as w15
from rigorous_refinement_tools import euler_gamma_binet_iv

sys.set_int_max_str_digits(0)
H0=F(1797,10000)
D0=F(893,5000)
S0=F(0)
RHO_H=F(1,100_000_000)   # 1e-8
RHO_D=F(1,10_000_000)    # 1e-7
RHO_S=F(1,10_000_000)    # 1e-7
N=5
CORR={(0,0):3,(0,1):5,(1,0):5,(1,1):7}
DELTA=F(1,100_000_000)
UPPER=F(1,20_000_000)
GRID=10**42


def frac(q):return base.frac_json(q)
def ivj(x):return base.iv_json(x)
def fq(o):return F(int(o['num']),int(o['den']))

def ldlt(A):
 n=len(A);L=[[F(0) for _ in range(n)] for _ in range(n)];p=[]
 for i in range(n):
  L[i][i]=F(1);z=A[i][i]-sum(L[i][k]*L[i][k]*p[k] for k in range(i))
  if z<=0:return False,p+[z]
  p.append(z)
  for j in range(i+1,n):L[j][i]=(A[j][i]-sum(L[j][k]*L[i][k]*p[k] for k in range(i)))/z
 return True,p

def grid_center(x):
 m=x.midpoint();q=m.numerator*GRID//m.denominator;a,b=F(q,GRID),F(q+1,GRID)
 return a if abs(m-a)<=abs(b-m) else b

def iq(A,c):
 z=base.IV.point(0)
 for i in range(len(c)):
  for j in range(len(c)):z+=A[i][j].scale(F(c[i]*c[j]))
 return base.coarsen(z,72)
def eq(A,c):return sum((F(c[i]*c[j])*A[i][j] for i in range(len(c)) for j in range(len(c))),F(0))

def generic_weil_bound(r,hmin,hmax,R,A,B):
 """Absolute bound for W(g), with |g|<=A, |g'|<=B, support halfwidth q*hmax."""
 q=F(r+1,2);e=base.exp_iv(R/2,110).hi
 const=(base.log4pi_iv()+euler_gamma_binet_iv(100,4)).hi
 active,coeff=w15.active_coeff_sum(R)
 endpoint=4*q*hmax*A*e
 constant=const*A
 prime=2*coeff.hi*A
 inside=R*(A*e/2+B)
 outside=2*A*w15.atanh_exp_minus_iv(R).hi
 total=endpoint+constant+prime+inside+outside
 ceil=F((total.numerator+total.denominator-1)//total.denominator)
 return {'R':R,'active':active,'amplitude':A,'x_derivative':B,'endpoint':endpoint,'constant':constant,'prime':prime,'arch_inside':inside,'arch_outside':outside,'total':total,'ceil':ceil}

def second_bounds(r):
 hmin=H0-RHO_H;hmax=H0+RHO_H;q=F(r+1,2)
 R=F(N-1)*(D0+RHO_D)+(RHO_S if r==5 else 0)+q*hmax
 Ac=4/hmin**2;Bc=8/hmin**3
 Ah=(2*q+4*q*q)/hmin**2
 Bh=(2+16*q+8*q*q)/hmin**3
 return generic_weil_bound(r,hmin,hmax,R,Ac,Bc),generic_weil_bound(r,hmin,hmax,R,Ah,Bh)

def mul_iv_scalar(k,x):
 return base.IV(k*x.lo,k*x.hi) if k>=0 else base.IV(k*x.hi,k*x.lo)

def chamber_margin():
 logs={n:base.log_rational_iv(F(n),260) for n in (2,3,4,5)}
 hiv=base.IV(H0-RHO_H,H0+RHO_H)
 best=None;wit=None
 for ca in range(2):
  for cb in range(2):
   r=CORR[(ca,cb)];q=(r+1)//2;b=0 if ca==cb else 1
   for i in range(N):
    for j in range(N):
     a=i-j;c0=F(a)*D0;cr=abs(a)*RHO_D+b*RHO_S;civ=base.IV(c0-cr,c0+cr)
     for n,x in logs.items():
      for sign in (1,-1):
       sample=x if sign==1 else -x
       for k in range(-q,q+1):
        knot=civ+mul_iv_scalar(F(k),hiv)
        if sample.hi<knot.lo:dist=knot.lo-sample.hi
        elif knot.hi<sample.lo:dist=sample.lo-knot.hi
        else:dist=F(0)
        if best is None or dist<best:
         best=dist;wit={'channels':[ca,cb],'indices':[i,j],'r':r,'n':n,'sign':sign,'k':k,'center_interval':ivj(civ),'h_interval':ivj(hiv),'knot_interval':ivj(knot),'sample':ivj(sample)}
 return best,wit

def main():
 root=Path(__file__).resolve().parent
 gamma=euler_gamma_binet_iv(100,4);const_total=base.log4pi_iv()+gamma
 hmin,hmax=H0-RHO_H,H0+RHO_H
 maxR=F(N-1)*(D0+RHO_D)+RHO_S+4*hmax
 log5=base.log_rational_iv(F(5),260)
 if maxR>=log5.lo:raise ArithmeticError('n>=5 not excluded')
 pp={n:p for n in range(2,5) if (p:=w15.prime_power_base(n)) is not None}
 logs={n:base.log_rational_iv(F(n),260) for n in range(2,6)}
 sqrts={n:base.sqrt_rational_iv(F(n),180) for n in pp}
 sec={r:second_bounds(r) for r in (3,5,7)}

 labels=[];corners={}
 for hs,h in (('m',hmin),('p',hmax)):
  for ds,d in (('m',D0-RHO_D),('p',D0+RHO_D)):
   for ss,s in (('m',-RHO_S),('p',RHO_S)):
    name=hs+ds+ss;labels.append((name,h,d,s));print(f'building corner {name} h={h} d={d} sigma={s}',flush=True)
    w15.H=h
    M,G,act,ncache=w15.build_point(d,s,const_total,pp,logs,sqrts)
    corners[name]={'h':h,'d':d,'sigma':s,'M':M,'G':G,'activation':act,'cache_entries':ncache}
 w15.H=H0

 dim=2*N;Lcc={r:sec[r][0]['ceil'] for r in sec};Lhh={r:sec[r][1]['ceil'] for r in sec}
 hmin=H0-RHO_H
 Gcc=4/hmin**2
 Ghh={r:(2*F(r+1,2)+4*F(r+1,2)**2)/hmin**2 for r in (3,5,7)}
 ER=[[F(0) for _ in range(dim)] for _ in range(dim)];GR=[[F(0) for _ in range(dim)] for _ in range(dim)]
 rows=[];grows=[]
 for I in range(dim):
  ca,i=divmod(I,N);mr=gr=F(0)
  for J in range(dim):
   cb,j=divmod(J,N);r=CORR[(ca,cb)];a=F(i-j);b=F(0 if ca==cb else 1)
   center_shape=a*a*RHO_D**2+b*b*RHO_S**2
   ER[I][J]=(Lcc[r]*center_shape+Lhh[r]*RHO_H**2)/2
   GR[I][J]=(Gcc*center_shape+Ghh[r]*RHO_H**2)/2
   mr+=ER[I][J]+DELTA*GR[I][J];gr+=GR[I][J]
  rows.append(mr);grows.append(gr)
 eps=max(rows);geps=max(grows)

 center=json.loads((root/'mixed_10x10_nearzero_interval.json').read_text());w=list(map(int,center['upper_witness']['integer_vector']))
 qcorn=[];gcorn=[];ccert={}
 for name,_,_,_ in labels:
  M=corners[name]['M'];G=corners[name]['G'];C=[[grid_center(M[i][j]) for j in range(dim)] for i in range(dim)]
  pe=max(sum(max(abs(C[i][j]-M[i][j].lo),abs(M[i][j].hi-C[i][j])) for j in range(dim)) for i in range(dim))
  T=[[C[i][j]-DELTA*G[i][j]-((pe+eps) if i==j else 0) for j in range(dim)] for i in range(dim)]
  ok,p=ldlt(T)
  if not ok:raise ArithmeticError(f'lower failed {name}: {float(p[-1]):.4e}')
  GT=[[G[i][j]-(geps if i==j else 0) for j in range(dim)] for i in range(dim)]
  gok,gp=ldlt(GT)
  if not gok:raise ArithmeticError(f'gram failed {name}')
  q=iq(M,w);g=eq(G,w);qcorn.append(q);gcorn.append(g)
  ccert[name]={'point_row_error':pe,'ldlt_pivots':p,'gram_ldlt_pivots':gp,'q':q,'g':g}
 dq=sum(abs(F(w[i]*w[j]))*ER[i][j] for i in range(dim) for j in range(dim))
 dg=sum(abs(F(w[i]*w[j]))*GR[i][j] for i in range(dim) for j in range(dim))
 qt=base.IV(min(x.lo for x in qcorn)-dq,max(x.hi for x in qcorn)+dq);gt=base.IV(min(gcorn)-dg,max(gcorn)+dg)
 if gt.lo<=0 or qt.hi>=UPPER*gt.lo:raise ArithmeticError(f'upper failed ratio={float(qt.hi/gt.lo):.4e}')
 margin,mwit=chamber_margin()
 if margin<=0:raise ArithmeticError('chamber unstable')

 def obj(c):return {'h':frac(c['h']),'d':frac(c['d']),'sigma':frac(c['sigma']),'cache_entries':c['cache_entries'],'matrix':[[ivj(x) for x in row] for row in c['M']],'gram':[[frac(x) for x in row] for row in c['G']],'activation':c['activation']}
 result={
  'schema':'RH-W-16-three-parameter-tube-v0.1','date':'2026-07-24','status':'CERTIFIED_TRILINEAR_INTERVAL_TAYLOR_TUBE',
  'basis':{'h_center':frac(H0),'degrees':[1,3],'per_channel_dimension':N,'total_dimension':dim},
  'tube':{'h_radius':frac(RHO_H),'d_radius':frac(RHO_D),'sigma_radius':frac(RHO_S),'h_interval':[frac(hmin),frac(hmax)],'d_interval':[frac(D0-RHO_D),frac(D0+RHO_D)],'sigma_interval':[frac(-RHO_S),frac(RHO_S)],'volume':frac(8*RHO_H*RHO_D*RHO_S)},
  'second_derivative_bounds':{str(r):{'center':{k:(frac(v) if isinstance(v,F) else v) for k,v in sec[r][0].items()},'scale_h':{k:(frac(v) if isinstance(v,F) else v) for k,v in sec[r][1].items()},'gram_center':frac(Gcc),'gram_scale_h':frac(Ghh[r])} for r in sec},
  'chamber':{'max_support_radius':frac(maxR),'log5':ivj(log5),'active_global_prime_powers':[2,3,4],'minimum_sample_to_knot_margin':frac(margin),'margin_witness':mwit,'constant_on_tube':True},
  'interpolation':{'method':'tensor-product trilinear interpolation of eight rigorous corner matrices plus pure second-derivative remainders in center and h','entry_remainders':[[frac(x) for x in row] for row in ER],'gram_entry_remainders':[[frac(x) for x in row] for row in GR],'global_combined_row_remainder':frac(eps),'global_gram_row_remainder':frac(geps)},
  'corners':{name:obj(corners[name]) for name,_,_,_ in labels},
  'certificate':{'delta_lower':frac(DELTA),'upper_ratio':frac(UPPER),'corner_certificates':{name:{'point_row_error':frac(v['point_row_error']),'ldlt_pivots':[frac(x) for x in v['ldlt_pivots']],'gram_ldlt_pivots':[frac(x) for x in v['gram_ldlt_pivots']]} for name,v in ccert.items()},'exact_bracket':'1e-8 < lambda_min(M(h,d,sigma),G(h,d,sigma)) < 5e-8 for every point in the 3D box'},
  'upper_witness':{'integer_vector':w,'corner_quadratic_intervals':[ivj(x) for x in qcorn],'corner_gram_exact':[frac(x) for x in gcorn],'quadratic_remainder_bound':frac(dq),'gram_remainder_bound':frac(dg),'tube_quadratic_interval':ivj(qt),'tube_gram_interval':ivj(gt)},
  'scope_warning':'A continuous finite-dimensional three-parameter near-zero positive tube neither proves nor disproves RH.'}
 (root/'three_parameter_tube_certificate.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
 text='\n'.join([f'status={result["status"]}',f'dimension={dim}',f'h_radius={float(RHO_H):.3e}',f'd_radius={float(RHO_D):.3e}',f'sigma_radius={float(RHO_S):.3e}',f'combined_second_order_row_remainder={float(eps):.18e}',f'minimum_knot_margin={float(margin):.18e}',f'upper_witness_ratio_hi={float(qt.hi/gt.lo):.18e}','exact_tube_bracket=1e-8<lambda_min<5e-8','RH_CLAIM=False'])+'\n'
 (root/'BUILD_SUMMARY.txt').write_text(text);print(text,end='')
if __name__=='__main__':main()
