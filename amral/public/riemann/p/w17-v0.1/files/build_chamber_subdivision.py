#!/usr/bin/env python3
"""RH-W-17: chamber-aware subdivision across a simultaneous B-spline knot event.

A fixed-h, sigma=0 mixed-order dictionary is followed along a one-dimensional
d-slice.  The slice crosses the event 4 d = log 2, where the n=2 sample moves
through the central spline knot for the farthest lag in the degree 3, 5 and 7
correlation blocks simultaneously.  The master interval is subdivided into a
left chamber, a rigorous event slab, and a right chamber.  Every cell receives
an exact rational positivity certificate based on endpoint convexity plus a
C^2 interpolation remainder.

Finite dimensional only.  No RH claim.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import csv, json, math, sys
import numpy as np
from scipy.linalg import eigvalsh

import weil_interval_core as base
import mixed_order_core as mixed
import build_interval_taylor_tube as w15
from rigorous_refinement_tools import euler_gamma_binet_iv

sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent
H=F(1797,10000)
SIGMA=F(0)
N=5
DIM=10
DELTA=F(1,100_000_000)
MASTER_LO=F(17328669,100_000_000)
EVENT_SLAB_LO=F(17328679,100_000_000)
EVENT_SLAB_HI=F(17328680,100_000_000)
MASTER_HI=F(17328690,100_000_000)
EXP_SUM_K=1500
GRID=10**38
CORR={(0,0):3,(0,1):5,(1,0):5,(1,1):7}
CELLS=(
    ('C0_LEFT',MASTER_LO,EVENT_SLAB_LO,'FIXED_LEFT_PIECE'),
    ('C1_EVENT',EVENT_SLAB_LO,EVENT_SLAB_HI,'EVENT_SLAB'),
    ('C2_RIGHT',EVENT_SLAB_HI,MASTER_HI,'FIXED_RIGHT_PIECE'),
)

# The original routine already includes a rigorous geometric tail.  Reducing
# the partial recurrence from 5000 to 1500 changes cost, not validity.
_ORIG_EXP_POWER_SUM=w15.exp_power_sum
def calibrated_exp_power_sum(x:F,p:int,K:int=EXP_SUM_K):
    return _ORIG_EXP_POWER_SUM(x,p,EXP_SUM_K)
w15.exp_power_sum=calibrated_exp_power_sum
w15._EXP_POWER_CACHE.clear()
w15.H=H


def frac(q:F): return base.frac_json(q)
def ivj(x:base.IV): return base.iv_json(x)
def fq(o): return F(int(o['num']),int(o['den']))
def iv(o): return base.IV(fq(o['lower']),fq(o['upper']))

def ldlt(A):
    n=len(A);L=[[F(0) for _ in range(n)] for _ in range(n)];p=[]
    for i in range(n):
        L[i][i]=F(1)
        z=A[i][i]-sum(L[i][k]*L[i][k]*p[k] for k in range(i))
        if z<=0:return False,p+[z]
        p.append(z)
        for j in range(i+1,n):
            L[j][i]=(A[j][i]-sum(L[j][k]*L[i][k]*p[k] for k in range(i)))/z
    return True,p

def grid_center(x:base.IV)->F:
    m=x.midpoint();q=m.numerator*GRID//m.denominator
    a,b=F(q,GRID),F(q+1,GRID)
    return a if abs(m-a)<=abs(b-m) else b

def point_path(d:F)->Path:
    return ROOT/f'point_d_{d.numerator}_{d.denominator}.json'

def save_point(d,Fdata):
    M,G,act,ncache=Fdata
    obj={'d':frac(d),'h':frac(H),'sigma':frac(SIGMA),'cache_entries':ncache,
         'matrix':[[ivj(x) for x in row] for row in M],
         'gram':[[frac(x) for x in row] for row in G],
         'activation':act}
    point_path(d).write_text(json.dumps(obj,indent=2),encoding='utf-8')

def load_point(d:F):
    p=point_path(d)
    if not p.exists():return None
    o=json.loads(p.read_text())
    M=[[iv(x) for x in row] for row in o['matrix']]
    G=[[fq(x) for x in row] for row in o['gram']]
    return M,G,o['activation'],int(o['cache_entries'])

def build_point(d:F,const_total,pp,logs,sqrts):
    old=load_point(d)
    if old is not None:
        print(f'loading cached point d={float(d):.10f}',flush=True);return old
    print(f'building point d={float(d):.10f}',flush=True)
    out=w15.build_point(d,SIGMA,const_total,pp,logs,sqrts)
    save_point(d,out)
    return out

def event_catalog(logs):
    events=[]
    for ca in range(2):
      for cb in range(2):
        r=CORR[(ca,cb)];q=(r+1)//2
        for i in range(N):
          for j in range(N):
            a=i-j
            if a==0:continue
            for n,sample0 in logs.items():
              for sign in (1,-1):
                sample=sample0 if sign==1 else -sample0
                for k in range(-q,q+1):
                    num=base.IV(sample.lo-F(k)*H,sample.hi-F(k)*H)
                    d_iv=(base.IV(num.lo/F(a),num.hi/F(a)) if a>0
                          else base.IV(num.hi/F(a),num.lo/F(a)))
                    if d_iv.hi<MASTER_LO or d_iv.lo>MASTER_HI:continue
                    events.append({'channels':[ca,cb],'indices':[i,j],
                                   'matrix_indices':[ca*N+i,cb*N+j],
                                   'correlation_degree':r,'prime_power':n,
                                   'sample_sign':sign,'knot_index':k,
                                   'd_interval':ivj(d_iv)})
    events.sort(key=lambda e:(e['matrix_indices'],e['correlation_degree']))
    return events

def cell_remainders(lo:F,hi:F,L2,LG2):
    rho=(hi-lo)/2
    ER=[[F(0) for _ in range(DIM)] for _ in range(DIM)]
    GR=[[F(0) for _ in range(DIM)] for _ in range(DIM)]
    rows=[];grows=[]
    for I in range(DIM):
        ca,i=divmod(I,N);mr=gr=F(0)
        for J in range(DIM):
            cb,j=divmod(J,N);r=CORR[(ca,cb)];a=F(i-j)
            ER[I][J]=L2[r]*a*a*rho*rho/2
            GR[I][J]=LG2*a*a*rho*rho/2
            mr+=ER[I][J]+DELTA*GR[I][J];gr+=GR[I][J]
        rows.append(mr);grows.append(gr)
    return ER,GR,max(rows),max(grows)

def main():
    gamma=euler_gamma_binet_iv(100,4);const_total=base.log4pi_iv()+gamma
    pp={n:p for n in range(2,5) if (p:=w15.prime_power_base(n)) is not None}
    logs={n:base.log_rational_iv(F(n),260) for n in range(2,6)}
    sqrts={n:base.sqrt_rational_iv(F(n),180) for n in pp}
    log2quarter=logs[2].scale(F(1,4))
    if not (EVENT_SLAB_LO<log2quarter.lo<=log2quarter.hi<EVENT_SLAB_HI):
        raise ArithmeticError('event slab does not contain log(2)/4')
    events=event_catalog(logs)
    if len(events)!=8:raise ArithmeticError(f'unexpected event multiplicity {len(events)}')
    if sorted(set(e['correlation_degree'] for e in events)) != [3,5,7]:
        raise ArithmeticError('expected simultaneous degree 3,5,7 event')

    # Conservative C^2 bounds inherited from the corrected W-15 derivation.
    L2={r:w15.second_derivative_bound(r)['ceil'] for r in (3,5,7)}
    LG2=F(4,H**2)
    points={}
    for d in sorted({x for _,lo,hi,_ in CELLS for x in (lo,hi)}):
        points[d]=build_point(d,const_total,pp,logs,sqrts)
    activations=[json.dumps(points[d][2],sort_keys=True) for d in sorted(points)]
    activation_constant=len(set(activations))==1
    if not activation_constant:raise ArithmeticError('activation graph changed; event is not knot-only')

    cell_objs=[]
    for cid,lo,hi,kind in CELLS:
        ER,GR,eps,geps=cell_remainders(lo,hi,L2,LG2)
        endpoint_cert={}
        for d in (lo,hi):
            M,G,act,ncache=points[d]
            C=[[grid_center(M[i][j]) for j in range(DIM)] for i in range(DIM)]
            pe=max(sum(max(abs(C[i][j]-M[i][j].lo),abs(M[i][j].hi-C[i][j]))
                       for j in range(DIM)) for i in range(DIM))
            T=[[C[i][j]-DELTA*G[i][j]-((pe+eps) if i==j else F(0))
                for j in range(DIM)] for i in range(DIM)]
            ok,piv=ldlt(T)
            GT=[[G[i][j]-(geps if i==j else F(0)) for j in range(DIM)] for i in range(DIM)]
            gok,gp=ldlt(GT)
            if not ok or not gok:raise ArithmeticError(f'cell {cid} endpoint failed')
            endpoint_cert[str(d)]={'point_row_error':frac(pe),
                'ldlt_pivots':[frac(x) for x in piv],
                'gram_ldlt_pivots':[frac(x) for x in gp]}
        cell_objs.append({'id':cid,'kind':kind,'interval':[frac(lo),frac(hi)],
            'width':frac(hi-lo),'radius':frac((hi-lo)/2),
            'entry_remainders':[[frac(x) for x in row] for row in ER],
            'gram_entry_remainders':[[frac(x) for x in row] for row in GR],
            'combined_row_remainder':frac(eps),'gram_row_remainder':frac(geps),
            'endpoint_certificates':endpoint_cert,
            'lower_bound':'lambda_min(M(d),G(d)) > 1e-8 throughout the closed cell'})

    maxR=4*MASTER_HI+4*H
    if maxR>=logs[5].lo:raise ArithmeticError('n>=5 not excluded')
    adjacency={'nodes':[c[0] for c in CELLS],
               'edges':[{'from':'C0_LEFT','to':'C1_EVENT','shared_boundary':frac(EVENT_SLAB_LO)},
                        {'from':'C1_EVENT','to':'C2_RIGHT','shared_boundary':frac(EVENT_SLAB_HI)}],
               'aggregate_path':['FIXED_LEFT_PIECE','EVENT_SLAB','FIXED_RIGHT_PIECE']}

    point_objs={}
    spectrum_rows=[]
    for d,(M,G,act,ncache) in sorted(points.items()):
        point_objs[str(d)]={'d':frac(d),'matrix':[[ivj(x) for x in row] for row in M],
                           'gram':[[frac(x) for x in row] for row in G],
                           'activation':act,'cache_entries':ncache}
        Mm=np.array([[float(x.midpoint()) for x in row] for row in M],dtype=float)
        Gm=np.array([[float(x) for x in row] for row in G],dtype=float)
        vals=eigvalsh(Mm,Gm)
        spectrum_rows.append({'d':f'{float(d):.10f}','lambda0_midpoint':f'{vals[0]:.18e}',
                              'lambda1_midpoint':f'{vals[1]:.18e}',
                              'rigor':'FLOATING_OBSERVATION_ONLY'})

    cert={'schema':'RH-W-17-chamber-aware-subdivision-v0.1','date':'2026-07-24',
          'status':'CERTIFIED_CHAMBER_AWARE_EVENT_SUBDIVISION',
          'basis':{'h':frac(H),'sigma':frac(SIGMA),'degrees':[1,3],
                   'correlation_degrees':[3,5,7],'per_channel_dimension':N,'total_dimension':DIM},
          'master_domain':{'parameter':'d','interval':[frac(MASTER_LO),frac(MASTER_HI)],
                           'width':frac(MASTER_HI-MASTER_LO)},
          'event':{'equation':'4 d = log 2','type':'SIMULTANEOUS_CENTRAL_SPLINE_KNOT_CROSSING',
                   'rigorous_d_interval':ivj(log2quarter),'event_slab':[frac(EVENT_SLAB_LO),frac(EVENT_SLAB_HI)],
                   'multiplicity':len(events),'correlation_degrees':[3,5,7],
                   'prime_power':2,'activation_graph_changes':False,
                   'polynomial_piece_changes':True,'oriented_witnesses':events},
          'prime_power_chamber':{'max_support_radius':frac(maxR),'log5':ivj(logs[5]),
                                 'active_global_prime_powers':[2,3,4],
                                 'activation_constant_over_master_domain':activation_constant},
          'numerical_contract':{'exp_power_partial_terms':EXP_SUM_K,
               'exp_power_tail':'rigorous positive geometric tail retained after the partial recurrence',
               'matrix_interval_generator':'CPython Fraction plus outward Decimal.exp under documented terminating-decimal contract'},
          'second_derivative_bounds':{str(r):frac(L2[r]) for r in (3,5,7)},
          'gram_second_derivative_bound':frac(LG2),
          'delta_lower':frac(DELTA),'cells':cell_objs,'points':point_objs,
          'adjacency_graph':adjacency,
          'global_conclusion':'lambda_min(M(d),G(d)) > 1e-8 for every d in the master interval, including the event slab',
          'scope_warning':'A finite-dimensional positive chamber crossing neither proves nor disproves RH.'}
    (ROOT/'chamber_subdivision_certificate.json').write_text(json.dumps(cert,indent=2),encoding='utf-8')
    (ROOT/'chamber_adjacency_graph.json').write_text(json.dumps(adjacency,indent=2),encoding='utf-8')
    with (ROOT/'event_surface_catalog.csv').open('w',newline='',encoding='utf-8-sig') as f:
        wr=csv.DictWriter(f,fieldnames=['channels','indices','matrix_indices','correlation_degree','prime_power','sample_sign','knot_index','d_lower','d_upper'])
        wr.writeheader()
        for e in events:
            q=e['d_interval'];wr.writerow({'channels':e['channels'],'indices':e['indices'],'matrix_indices':e['matrix_indices'],
                'correlation_degree':e['correlation_degree'],'prime_power':e['prime_power'],'sample_sign':e['sample_sign'],
                'knot_index':e['knot_index'],'d_lower':q['decimal_lower'],'d_upper':q['decimal_upper']})
    with (ROOT/'local_chamber_spectrum.csv').open('w',newline='',encoding='utf-8-sig') as f:
        wr=csv.DictWriter(f,fieldnames=spectrum_rows[0].keys());wr.writeheader();wr.writerows(spectrum_rows)
    summary='\n'.join([
        f'status={cert["status"]}',f'dimension={DIM}',
        f'master_d_interval=[{float(MASTER_LO):.10f},{float(MASTER_HI):.10f}]',
        f'event_d_interval=[{float(log2quarter.lo):.18e},{float(log2quarter.hi):.18e}]',
        f'event_multiplicity={len(events)}',f'cells={len(cell_objs)}',
        'cell_types=FIXED_LEFT_PIECE,EVENT_SLAB,FIXED_RIGHT_PIECE',
        'activation_graph_constant=[2,3,4]',
        'exact_global_lower_bound=lambda_min>1e-8',
        'RH_CLAIM=False'])+'\n'
    (ROOT/'BUILD_SUMMARY.txt').write_text(summary,encoding='utf-8');print(summary,end='')
if __name__=='__main__':main()
