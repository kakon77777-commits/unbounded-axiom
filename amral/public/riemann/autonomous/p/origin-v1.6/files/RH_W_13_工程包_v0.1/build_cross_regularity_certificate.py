#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json, math, sys
import numpy as np
from scipy.linalg import eigh

import weil_interval_core as base
import mixed_order_core as mixed
from mixed_order_jump_tail import arch_series_jump_resolved
from rigorous_refinement_tools import euler_gamma_binet_iv

sys.set_int_max_str_digits(0)
H=F(1797,10000)
D=F(893,5000)
SIGMA=F(0)
N=5
BASIS_DEGREES=(1,3)
CORR_DEGREES={(1,1):3,(1,3):5,(3,3):7}
K_BY_CORR_DEGREE={3:4000,5:1500,7:700}
GRID=10**42
DELTA=F(1,100_000_000)
UPPER=F(1,20_000_000)
DELTA_M1=F(1,2500)
DELTA_M3=F(1,10_000_000)
SHIFTS=tuple(F(j-N//2)*D for j in range(N))


def prime_power_base(n:int)->int|None:
    for p in range(2,n+1):
        if any(p%q==0 for q in range(2,math.isqrt(p)+1)):continue
        v=p
        while v<n:v*=p
        if v==n:return p
    return None


def ldlt(A):
    n=len(A);L=[[F(0) for _ in range(n)] for _ in range(n)];p=[]
    for i in range(n):
        L[i][i]=F(1)
        piv=A[i][i]-sum(L[i][k]*L[i][k]*p[k] for k in range(i))
        if piv<=0:return False,p+[piv]
        p.append(piv)
        for j in range(i+1,n):
            L[j][i]=(A[j][i]-sum(L[j][k]*L[i][k]*p[k] for k in range(i)))/piv
    return True,p


def grid_center(x:base.IV)->F:
    m=x.midpoint();q=m.numerator*GRID//m.denominator
    a,b=F(q,GRID),F(q+1,GRID)
    return a if abs(m-a)<=abs(b-m) else b


def parse_iv(obj):
    return base.IV(F(int(obj['lower']['num']),int(obj['lower']['den'])),F(int(obj['upper']['num']),int(obj['upper']['den'])))


def interval_quadratic(A,c):
    out=base.IV.point(0)
    for i in range(len(c)):
        for j in range(len(c)):
            out += A[i][j].scale(F(c[i]*c[j]))
    return base.coarsen(out,72)


def exact_quadratic(A,c):
    return sum((F(c[i]*c[j])*A[i][j] for i in range(len(c)) for j in range(len(c))),F(0))


def certify(Aiv,G,delta):
    n=len(Aiv);C=[[grid_center(Aiv[i][j]) for j in range(n)] for i in range(n)]
    eps=max(sum(max(abs(C[i][j]-Aiv[i][j].lo),abs(Aiv[i][j].hi-C[i][j])) for j in range(n)) for i in range(n))
    T=[[C[i][j]-delta*G[i][j]-(eps if i==j else F(0)) for j in range(n)] for i in range(n)]
    ok,p=ldlt(T)
    return ok,eps,p,C


def main():
    out=Path(__file__).resolve().parent
    max_radius=F(N-1)*D+4*H
    exclusion=math.ceil(math.exp(float(max_radius)))
    while base.log_rational_iv(F(exclusion),220).lo<=max_radius:exclusion+=1
    pp={n:p for n in range(2,exclusion) if (p:=prime_power_base(n)) is not None}
    logs={n:base.log_rational_iv(F(n),240) for n in range(2,exclusion+1)}
    sqrts={n:base.sqrt_rational_iv(F(n),170) for n in pp}
    gamma=euler_gamma_binet_iv(100,4)
    const_total=base.log4pi_iv()+gamma

    def entry(r,center):
        f0=mixed.f_value(r,H,center,F(0))
        endpoint=base.coarsen(mixed.integrate_f_exp(r,H,center,F(1,2))+mixed.integrate_f_exp(r,H,center,F(-1,2)),84)
        constant=base.coarsen(-const_total.scale(f0),84)
        arch,aa=arch_series_jump_resolved(r,H,center,K_BY_CORR_DEGREE[r])
        prime_total=base.IV.point(0);blocks={};active=[]
        for n,p in pp.items():
            coeff=logs[p]/sqrts[n]
            plus=mixed.f_interval(r,H,center,logs[n]);minus=mixed.f_interval(r,H,center,-logs[n])
            term=base.coarsen(-(coeff*(plus+minus)),82)
            blocks[str(n)]=base.iv_json(term);prime_total=base.coarsen(prime_total+term,82)
            if not(plus.lo==plus.hi==0 and minus.lo==minus.hi==0):active.append(n)
        prime_free=base.coarsen(endpoint+constant+arch,80)
        total=base.coarsen(prime_free+prime_total,80)
        lft,rgt=mixed.support(r,H,center)
        return total,{'correlation_degree':r,'center':base.frac_json(center),'support':[base.frac_json(lft),base.frac_json(rgt)],'f0':base.frac_json(f0),'endpoint':base.iv_json(endpoint),'constant':base.iv_json(constant),'arch':base.iv_json(arch),'prime_free':base.iv_json(prime_free),'prime_total':base.iv_json(prime_total),'prime_blocks':blocks,'active':active,'arch_audit':aa,'total':base.iv_json(total)}

    lag_values={};lag_audits={}
    for pair,r in CORR_DEGREES.items():
        key=f'{pair[0]}x{pair[1]}';lag_values[key]=[];lag_audits[key]=[]
        for lag in range(N):
            val,audit=entry(r,F(lag)*D)
            lag_values[key].append(val);lag_audits[key].append(audit)
            print(f'{key} lag={lag} width={float(val.width()):.3e} active={audit["active"]}')

    dim=2*N
    M=[[base.IV.point(0) for _ in range(dim)] for _ in range(dim)]
    G=[[F(0) for _ in range(dim)] for _ in range(dim)]
    P={n:[[base.IV.point(0) for _ in range(dim)] for _ in range(dim)] for n in pp}
    for ca,a in enumerate(BASIS_DEGREES):
        for cb,b in enumerate(BASIS_DEGREES):
            pair=(min(a,b),max(a,b));key=f'{pair[0]}x{pair[1]}';r=CORR_DEGREES[pair]
            for i in range(N):
                for j in range(N):
                    I=ca*N+i;J=cb*N+j;lag=abs(i-j)
                    M[I][J]=lag_values[key][lag]
                    G[I][J]=mixed.f_value(r,H,F(i-j)*D,F(0))
                    for n in pp:P[n][I][J]=parse_iv(lag_audits[key][lag]['prime_blocks'][str(n)])
    gok,gp=ldlt(G)
    if not gok:raise ArithmeticError('Gram not positive')

    Mf=np.array([[float(x.midpoint()) for x in row] for row in M]);Gf=np.array([[float(x) for x in row] for row in G])
    vals,vec=eigh(Mf,Gf);v=vec[:,0]
    ok,eps,piv,C=certify(M,G,DELTA)
    if not ok:raise ArithmeticError(f'mixed lower certificate failed eps={float(eps):.3e}, min={vals[0]:.3e}')

    scale=10**10;vmax=max(abs(float(x)) for x in v)
    witness=[int(round(float(x)/vmax*scale)) for x in v]
    q=interval_quadratic(M,witness);g=exact_quadratic(G,witness)
    if q.hi>=UPPER*g:raise ArithmeticError(f'upper witness failed ratio={float(q.hi/g):.3e}')

    M11=[[M[i][j] for j in range(N)] for i in range(N)];G11=[[G[i][j] for j in range(N)] for i in range(N)]
    M33=[[M[N+i][N+j] for j in range(N)] for i in range(N)];G33=[[G[N+i][N+j] for j in range(N)] for i in range(N)]
    ok1,e1,p1,_=certify(M11,G11,DELTA_M1);ok3,e3,p3,_=certify(M33,G33,DELTA_M3)
    if not ok1 or not ok3:raise ArithmeticError('isolated certificate failed')

    w1,w3=witness[:N],witness[N:]
    q11=interval_quadratic(M11,w1);q33=interval_quadratic(M33,w3)
    q13=base.IV.point(0)
    for i in range(N):
        for j in range(N):q13+=M[i][N+j].scale(F(2*w1[i]*w3[j]))
    pcomp={str(n):base.iv_json(interval_quadratic(P[n],witness)) for n in pp}

    result={
      'schema':'RH-W-13-cross-regularity-continuation-v0.1','date':'2026-07-23','status':'CERTIFIED_NEAR_ZERO_POSITIVE_MIXED_BAND',
      'basis':{'h':base.frac_json(H),'spacing':base.frac_json(D),'relative_shift_sigma':base.frac_json(SIGMA),'basis_degrees':[1,3],'per_channel_dimension':N,'total_dimension':dim,'shifts':[base.frac_json(x) for x in SHIFTS]},
      'gauge_parameter':{'alpha_statement':'multiplying the full m=3 channel by alpha is a congruence T^T(M,G)T and leaves generalized eigenvalues invariant','alpha_is_genuine_continuation_parameter':False,'replacement_genuine_parameter':'relative channel shift sigma','selected_sigma':base.frac_json(SIGMA)},
      'support':{'max_correlation_radius':base.frac_json(max_radius),'exclusion_n':exclusion,'log_exclusion_n':base.iv_json(logs[exclusion]),'all_n_ge_exclusion_n_excluded':True},
      'prime_powers':{str(n):p for n,p in pp.items()},
      'activation_graph':{key:{str(k):a['active'] for k,a in enumerate(vals0)} for key,vals0 in lag_audits.items()},
      'lag_entries':{key:{str(k):base.iv_json(v0) for k,v0 in enumerate(vals0)} for key,vals0 in lag_values.items()},
      'lag_audits':{key:{str(k):a for k,a in enumerate(vals0)} for key,vals0 in lag_audits.items()},
      'matrix':[[base.iv_json(x) for x in row] for row in M],
      'gram':[[base.frac_json(x) for x in row] for row in G],
      'exploration':{'midpoint_generalized_eigenvalues_display_only':[float(x) for x in vals],'gram_eigenvalues_display_only':[float(x) for x in np.linalg.eigvalsh(Gf)],'selected_rational_parameters_from_corrected_search':True},
      'certificate':{'delta':base.frac_json(DELTA),'upper_ratio':base.frac_json(UPPER),'grid_denominator':str(GRID),'row_radius':base.frac_json(eps),'ldlt_pivots':[base.frac_json(x) for x in piv],'exact_bracket':'1e-8 < lambda_min(M,G) < 5e-8','method':'exact rational LDL^T lower bound plus rational Rayleigh witness upper bound'},
      'upper_witness':{'integer_vector':witness,'quadratic_interval':base.iv_json(q),'gram_exact':base.frac_json(g),'channel_components':{'m1_self':base.iv_json(q11),'cross_twice':base.iv_json(q13),'m3_self':base.iv_json(q33)},'prime_power_components':pcomp},
      'isolated_certificates':{'m1':{'delta':base.frac_json(DELTA_M1),'row_radius':base.frac_json(e1),'pivots':[base.frac_json(x) for x in p1]},'m3':{'delta':base.frac_json(DELTA_M3),'row_radius':base.frac_json(e3),'pivots':[base.frac_json(x) for x in p3]}},
      'tail_upgrade':{'method':'jump-resolved exact integration-by-parts','K_by_correlation_degree':{str(k):v for k,v in K_BY_CORR_DEGREE.items()},'reason':'coarse absolute derivative majorants cannot resolve the near-zero mixed band'},
      'scope_warning':'A certified positive finite-dimensional bracket does not imply RH. No negative Weil witness was found.'
    }
    (out/'mixed_10x10_nearzero_interval.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    summary='\n'.join([f'status={result["status"]}',f'dimension={dim}',f'midpoint_min_display={vals[0]:.18e}',f'row_radius={float(eps):.18e}','exact_lower=lambda_min>1e-8','exact_upper=lambda_min<5e-8',f'm1_lower>{float(DELTA_M1):.3e}',f'm3_lower>{float(DELTA_M3):.3e}','RH_CLAIM=False'])+'\n'
    (out/'BUILD_SUMMARY.txt').write_text(summary,encoding='utf-8');print(summary,end='')

if __name__=='__main__':main()
