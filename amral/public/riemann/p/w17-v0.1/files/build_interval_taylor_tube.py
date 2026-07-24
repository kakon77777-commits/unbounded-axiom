#!/usr/bin/env python3
"""RH-W-15: rigorous bilinear/interval-Taylor tube expansion.

The fixed-h mixed-order dictionary is evaluated rigorously at the four corners
of a (d,sigma) rectangle.  On a fixed spline/prime-power chamber, every entry
is C^2.  Tensor-product linear interpolation is a convex combination of the
four corner matrices.  A global second-derivative remainder is then absorbed
by exact rational LDL^T certificates.

This is finite-dimensional and makes no RH claim.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json, math, sys

import weil_interval_core as base
import mixed_order_core as mixed
from mixed_order_jump_tail import arch_series_jump_resolved
from rigorous_refinement_tools import euler_gamma_binet_iv

sys.set_int_max_str_digits(0)
H=F(1797,10000)
D0=F(893,5000)
S0=F(0)
RHO_D=F(1,10_000_000)      # 1e-7
RHO_S=F(1,10_000_000)      # 1e-7
N=5
DEGREES=(1,3)
CORR={(0,0):3,(0,1):5,(1,0):5,(1,1):7}
K_BY_R={3:4000,5:1500,7:700}
DELTA=F(1,100_000_000)
UPPER=F(1,20_000_000)
GRID=10**42


def fq(o): return F(int(o['num']),int(o['den']))
def frac(q): return base.frac_json(q)
def ivj(x): return base.iv_json(x)

def prime_power_base(n:int)->int|None:
    for p in range(2,n+1):
        if any(p%q==0 for q in range(2,math.isqrt(p)+1)): continue
        v=p
        while v<n: v*=p
        if v==n:return p
    return None

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

def interval_quadratic(A,c):
    z=base.IV.point(0)
    for i in range(len(c)):
        for j in range(len(c)): z += A[i][j].scale(F(c[i]*c[j]))
    return base.coarsen(z,72)

def exact_quadratic(A,c):
    return sum((F(c[i]*c[j])*A[i][j] for i in range(len(c)) for j in range(len(c))),F(0))

def atanh_exp_minus_iv(R:F)->base.IV:
    """Enclose atanh(exp(-R)) for terminating-decimal positive R."""
    e=base.exp_iv(-R,115)
    lo_ratio=(F(1)+e.lo)/(F(1)-e.lo)
    hi_ratio=(F(1)+e.hi)/(F(1)-e.hi)
    lo=base.log_rational_iv(lo_ratio,220).lo/2
    hi=base.log_rational_iv(hi_ratio,220).hi/2
    return base.coarsen(base.IV(lo,hi),70)

def active_coeff_sum(R:F):
    coeff=base.IV.point(0); active=[]; n=2
    while base.log_rational_iv(F(n),220).lo<=R:
        p=prime_power_base(n)
        if p is not None:
            active.append(n)
            coeff += base.log_rational_iv(F(p),220)/base.sqrt_rational_iv(F(n),160)
        n+=1
    return active,coeff

def first_derivative_bound(r:int, rd:F, rs:F):
    q=F(r+1,2)
    R=F(N-1)*(D0+rd)+(rs if r==5 else F(0))+q*H
    e=base.exp_iv(R/2,110).hi
    const=(base.log4pi_iv()+euler_gamma_binet_iv(100,4)).hi
    active,coeff=active_coeff_sum(R)
    endpoint=4*q*e
    constant=const/H
    prime=2*coeff.hi/H
    inside=R*(e/(2*H)+4/H**2)
    outside=2*atanh_exp_minus_iv(R).hi/H
    arch=inside+outside
    total=endpoint+constant+prime+arch
    ceil=F((total.numerator+total.denominator-1)//total.denominator)
    return {'R':R,'active':active,'endpoint':endpoint,'constant':constant,'prime':prime,'arch_inside':inside,'arch_outside':outside,'total':total,'ceil':ceil}

def second_derivative_bound(r:int):
    q=F(r+1,2)
    # Max radius over the new tube.
    R=F(N-1)*(D0+RHO_D)+(RHO_S if r==5 else F(0))+q*H
    e=base.exp_iv(R/2,110).hi
    const=(base.log4pi_iv()+euler_gamma_binet_iv(100,4)).hi
    active,coeff=active_coeff_sum(R)
    # beta'' <= 4, beta''' <= 8 from cardinal B-spline finite differences.
    endpoint=16*q*e/H
    constant=4*const/H**2
    prime=8*coeff.hi/H**2
    inside=R*(2*e/H**2+8/H**3)
    outside=8*atanh_exp_minus_iv(R).hi/H**2
    arch=inside+outside
    total=endpoint+constant+prime+arch
    ceil=F((total.numerator+total.denominator-1)//total.denominator)
    return {'R':R,'active':active,'endpoint':endpoint,'constant':constant,'prime':prime,'arch_inside':inside,'arch_outside':outside,'total':total,'ceil':ceil}


_POWER_SUM_CACHE={}
_EXP_POWER_CACHE={}

def power_sum_all(p:int)->base.IV:
    if p not in _POWER_SUM_CACHE:
        _POWER_SUM_CACHE[p]=__import__('rigorous_refinement_tools').tail_sum_power_refined(0,p,20000)
    return _POWER_SUM_CACHE[p]

def exp_power_sum(x:F,p:int,K:int=5000)->base.IV:
    """Decimal-directed enclosure of the exponential power sum.

    Recurrence avoids thousands of transcendental calls.  The initial
    exponential intervals come from base.exp_iv; all subsequent Decimal
    additions/multiplications/divisions are performed with directed rounding.
    """
    key=(x,p,K)
    if key in _EXP_POWER_CACHE:return _EXP_POWER_CACHE[key]
    from decimal import Decimal, Context, ROUND_FLOOR, ROUND_CEILING, localcontext
    def dec(q:F)->Decimal:
        return Decimal(q.numerator)/Decimal(q.denominator)
    def fracd(z:Decimal)->F:
        sign,digits,exponent=z.as_tuple();n=0
        for d in digits:n=n*10+d
        if sign:n=-n
        return F(n*(10**exponent),1) if exponent>=0 else F(n,10**(-exponent))
    e0=base.exp_iv(-x/2,115); ratio=base.exp_iv(-2*x,115)
    clo=Context(prec=105,rounding=ROUND_FLOOR); chi=Context(prec=105,rounding=ROUND_CEILING)
    with localcontext(clo):
        elo=dec(e0.lo); rlo=dec(ratio.lo); rklo=Decimal(1); slo=Decimal(0)
    with localcontext(chi):
        ehi=dec(e0.hi); rhi=dec(ratio.hi); rkhi=Decimal(1); shi=Decimal(0)
    for k in range(K):
        aden=F(4*k+1,2)**p
        with localcontext(clo):
            slo += elo*rklo/dec(aden); rklo *= rlo
        with localcontext(chi):
            shi += ehi*rkhi/dec(aden); rkhi *= rhi
    aden=F(4*K+1,2)**p
    with localcontext(chi):
        first=ehi*rkhi/dec(aden)
        tail=first/(Decimal(1)-rhi)
        shi += tail
    out=base.coarsen(base.IV(fracd(slo),fracd(shi)),80)
    _EXP_POWER_CACHE[key]=out
    return out

def arch_series_closed(degree:int,h:F,center:F):
    """Infinite jump-resolved archimedean series without termwise exp calls."""
    radius,deriv0,top0,jumps=__import__('mixed_order_jump_tail').jump_data(degree,h,center)
    lead=(base.pi_iv().scale(F(1,4))+base.log_rational_iv(F(2),200).scale(F(1,2))).scale(deriv0[0])
    total=lead
    deriv_terms={}
    for j,val in enumerate(deriv0[1:],start=1):
        if val:
            term=power_sum_all(j+1).scale(val);total+=term;deriv_terms[str(j+1)]=ivj(term)
    top=power_sum_all(degree+1).scale(top0);total+=top
    jump_terms=[]
    for x,jump in jumps:
        raw=exp_power_sum(x,degree+1)
        term=raw.scale(jump);total+=term
        jump_terms.append({'x':frac(x),'jump':frac(jump),'sum':ivj(raw),'term':ivj(term)})
    arch=base.coarsen(-total,78)
    return arch,{'method':'closed infinite power sums plus recurrent exponential jump sums','radius':frac(radius),'derivatives_at_zero':{str(i):frac(v) for i,v in enumerate(deriv0)},'leading':ivj(lead),'derivative_terms':deriv_terms,'top_term':ivj(top),'jump_terms':jump_terms,'arch':ivj(arch)}

def build_point(d:F,sigma:F, const_total, pp, logs, sqrts):
    cache={}
    def entry(r:int,center:F):
        # W is even in the center for the symmetrized explicit formula.
        c=abs(center); key=(r,c)
        if key in cache:return cache[key]
        f0=mixed.f_value(r,H,c,F(0))
        endpoint=base.coarsen(mixed.integrate_f_exp(r,H,c,F(1,2))+mixed.integrate_f_exp(r,H,c,F(-1,2)),84)
        constant=base.coarsen(-const_total.scale(f0),84)
        arch,audit=arch_series_closed(r,H,c)
        prime=base.IV.point(0); active=[]
        for n,p in pp.items():
            coeff=logs[p]/sqrts[n]
            plus=mixed.f_interval(r,H,c,logs[n]); minus=mixed.f_interval(r,H,c,-logs[n])
            term=base.coarsen(-(coeff*(plus+minus)),82)
            prime=base.coarsen(prime+term,82)
            if not(plus.lo==plus.hi==0 and minus.lo==minus.hi==0):active.append(n)
        val=base.coarsen(endpoint+constant+arch+prime,80)
        cache[key]=(val,active)
        return cache[key]
    dim=2*N
    M=[[base.IV.point(0) for _ in range(dim)] for _ in range(dim)]
    G=[[F(0) for _ in range(dim)] for _ in range(dim)]
    shifts=[]
    for ca in range(2):
        soff=(-sigma/2 if ca==0 else sigma/2)
        shifts.append([F(i-N//2)*d+soff for i in range(N)])
    activation={}
    for I in range(dim):
        ca,i=divmod(I,N)
        for J in range(I,dim):
            cb,j=divmod(J,N)
            r=CORR[(ca,cb)]
            c=shifts[ca][i]-shifts[cb][j]
            val,act=entry(r,c)
            M[I][J]=M[J][I]=val
            gv=mixed.f_value(r,H,c,F(0))
            G[I][J]=G[J][I]=gv
            activation[f'{I},{J}']=act
    return M,G,activation,len(cache)

def chamber_margin():
    logs={n:base.log_rational_iv(F(n),260) for n in (2,3,4,5)}
    best=None; wit=None
    for ca in range(2):
      for cb in range(2):
        r=CORR[(ca,cb)]; q=(r+1)//2
        b=0 if ca==cb else 1
        for i in range(N):
          for j in range(N):
            a=i-j; c0=F(a)*D0
            if ca!=cb: c0 += (-S0 if ca==0 else S0) # zero, explicit bookkeeping
            cr=abs(a)*RHO_D+b*RHO_S
            civ=base.IV(c0-cr,c0+cr)
            for n,x in logs.items():
              for sign in (1,-1):
                sample=x if sign==1 else -x
                for k in range(-q,q+1):
                    # Knot center is c+k h.
                    knot=civ+base.IV.point(F(k)*H)
                    if sample.hi<knot.lo: dist=knot.lo-sample.hi
                    elif knot.hi<sample.lo: dist=sample.lo-knot.hi
                    else: dist=F(0)
                    if best is None or dist<best:
                        best=dist;wit={'channels':[ca,cb],'indices':[i,j],'r':r,'n':n,'sign':sign,'k':k,'center_interval':ivj(civ),'knot_interval':ivj(knot),'sample':ivj(sample)}
    return best,wit

def main():
    root=Path(__file__).resolve().parent
    gamma=euler_gamma_binet_iv(100,4);const_total=base.log4pi_iv()+gamma
    maxR=F(N-1)*(D0+RHO_D)+RHO_S+4*H
    log5=base.log_rational_iv(F(5),260)
    if maxR>=log5.lo: raise ArithmeticError('n>=5 not excluded')
    pp={n:p for n in range(2,5) if (p:=prime_power_base(n)) is not None}
    logs={n:base.log_rational_iv(F(n),260) for n in range(2,6)}
    sqrts={n:base.sqrt_rational_iv(F(n),180) for n in pp}

    # Backward audit: corrected RH-W-14 first-derivative bounds.
    old_rd=old_rs=F(4,10**12)
    first={r:first_derivative_bound(r,old_rd,old_rs) for r in (3,5,7)}
    second={r:second_derivative_bound(r) for r in (3,5,7)}

    corners={}
    labels=[('mm',D0-RHO_D,-RHO_S),('mp',D0-RHO_D,RHO_S),('pm',D0+RHO_D,-RHO_S),('pp',D0+RHO_D,RHO_S)]
    for name,d,s in labels:
        print(f'building corner {name} d={d} sigma={s}',flush=True)
        M,G,act,ncache=build_point(d,s,const_total,pp,logs,sqrts)
        corners[name]={'d':d,'sigma':s,'M':M,'G':G,'activation':act,'cache_entries':ncache}

    dim=2*N
    # Tensor-linear interpolation remainder.  For F(a d+b sigma):
    # |F-Bilinear(F)| <= .5 sup|Fcc| (a^2 rho_d^2+b^2 rho_s^2).
    rem_rows=[]; grem_rows=[]
    L2={r:second[r]['ceil'] for r in second}; LG2=F(4,H**2)
    entry_remainders=[[F(0) for _ in range(dim)] for _ in range(dim)]
    gram_remainders=[[F(0) for _ in range(dim)] for _ in range(dim)]
    for I in range(dim):
        ca,i=divmod(I,N);mr=gr=F(0)
        for J in range(dim):
            cb,j=divmod(J,N);r=CORR[(ca,cb)]
            a=F(i-j); b=F(0 if ca==cb else 1)
            shape=(a*a*RHO_D**2+b*b*RHO_S**2)/2
            em=L2[r]*shape; eg=LG2*shape
            entry_remainders[I][J]=em;gram_remainders[I][J]=eg
            mr += em+DELTA*eg;gr += eg
        rem_rows.append(mr);grem_rows.append(gr)
    eps_rem=max(rem_rows);eps_grem=max(grem_rows)

    corner_cert={}
    witness=json.loads((root/'mixed_10x10_nearzero_interval.json').read_text())['upper_witness']['integer_vector']
    witness=list(map(int,witness))
    qcorner=[];gcorner=[]
    for name,_,_ in labels:
        obj=corners[name];M=obj['M'];G=obj['G']
        C=[[grid_center(M[i][j]) for j in range(dim)] for i in range(dim)]
        point_rows=[sum(max(abs(C[i][j]-M[i][j].lo),abs(M[i][j].hi-C[i][j])) for j in range(dim)) for i in range(dim)]
        ep=max(point_rows)
        T=[[C[i][j]-DELTA*G[i][j]-((ep+eps_rem) if i==j else F(0)) for j in range(dim)] for i in range(dim)]
        ok,piv=ldlt(T)
        if not ok: raise ArithmeticError(f'corner lower failed {name}: {float(piv[-1]):.3e}')
        GT=[[G[i][j]-(eps_grem if i==j else F(0)) for j in range(dim)] for i in range(dim)]
        gok,gp=ldlt(GT)
        if not gok:raise ArithmeticError(f'corner gram failed {name}')
        q=interval_quadratic(M,witness);g=exact_quadratic(G,witness)
        qcorner.append(q);gcorner.append(g)
        corner_cert[name]={'point_row_error':ep,'combined_remainder':eps_rem,'pivots':piv,'gram_pivots':gp,'q':q,'g':g,'cache_entries':obj['cache_entries']}

    # Bilinear convex-combination upper witness plus Hessian remainder.
    dq=sum(abs(F(witness[i]*witness[j]))*entry_remainders[i][j] for i in range(dim) for j in range(dim))
    dg=sum(abs(F(witness[i]*witness[j]))*gram_remainders[i][j] for i in range(dim) for j in range(dim))
    qt=base.IV(min(x.lo for x in qcorner)-dq,max(x.hi for x in qcorner)+dq)
    gt=base.IV(min(gcorner)-dg,max(gcorner)+dg)
    if gt.lo<=0 or qt.hi>=UPPER*gt.lo: raise ArithmeticError(f'upper tube failed {float(qt.hi/gt.lo):.3e}')

    margin,mwit=chamber_margin()
    if margin<=0:raise ArithmeticError('chamber unstable')

    def bj(d):
        return {
          'd':frac(d['d']),'sigma':frac(d['sigma']),'cache_entries':d['cache_entries'],
          'matrix':[[ivj(x) for x in row] for row in d['M']],
          'gram':[[frac(x) for x in row] for row in d['G']],
          'activation':d['activation']}
    result={
      'schema':'RH-W-15-interval-taylor-tube-v0.1','date':'2026-07-23','status':'CERTIFIED_BILINEAR_INTERVAL_TAYLOR_TUBE',
      'basis':{'h':frac(H),'degrees':[1,3],'per_channel_dimension':N,'total_dimension':dim},
      'tube':{'d_center':frac(D0),'sigma_center':frac(S0),'d_radius':frac(RHO_D),'sigma_radius':frac(RHO_S),'d_interval':[frac(D0-RHO_D),frac(D0+RHO_D)],'sigma_interval':[frac(-RHO_S),frac(RHO_S)],'area':frac(4*RHO_D*RHO_S),'radius_expansion_over_RH_W_14':frac(RHO_D/old_rd)},
      'backward_audit_RH_W_14':{'issue':'the support-exterior -2 f(0) archimedean derivative tail was omitted from the published global Lipschitz derivation','correction':'add derivative-order-specific multiples of atanh(exp(-R))','corrected_first_derivative_bounds':{str(r):{k:(frac(v) if isinstance(v,F) else v) for k,v in x.items()} for r,x in first.items()},'RH_W_14_reverification_required':True},
      'second_derivative_bounds':{str(r):{k:(frac(v) if isinstance(v,F) else v) for k,v in x.items()} for r,x in second.items()},
      'chamber':{'max_support_radius':frac(maxR),'log5':ivj(log5),'active_global_prime_powers':[2,3,4],'minimum_sample_to_knot_margin':frac(margin),'margin_witness':mwit,'constant_on_tube':True},
      'interpolation':{'method':'tensor-product linear interpolation of four rigorous corner matrices plus pure second-derivative remainder','entry_remainders':[[frac(x) for x in row] for row in entry_remainders],'gram_entry_remainders':[[frac(x) for x in row] for row in gram_remainders],'combined_row_remainders':[frac(x) for x in rem_rows],'global_combined_row_remainder':frac(eps_rem),'global_gram_row_remainder':frac(eps_grem)},
      'corners':{name:bj(corners[name]) for name,_,_ in labels},
      'certificate':{'delta_lower':frac(DELTA),'upper_ratio':frac(UPPER),'corner_certificates':{name:{'point_row_error':frac(v['point_row_error']),'combined_remainder':frac(v['combined_remainder']),'ldlt_pivots':[frac(x) for x in v['pivots']],'gram_ldlt_pivots':[frac(x) for x in v['gram_pivots']]} for name,v in corner_cert.items()},'exact_bracket':'1e-8 < lambda_min(M(d,sigma),G(d,sigma)) < 5e-8 for every point in the rectangle'},
      'upper_witness':{'integer_vector':witness,'corner_quadratic_intervals':[ivj(x) for x in qcorner],'corner_gram_exact':[frac(x) for x in gcorner],'quadratic_remainder_bound':frac(dq),'gram_remainder_bound':frac(dg),'tube_quadratic_interval':ivj(qt),'tube_gram_interval':ivj(gt)},
      'scope_warning':'A continuous finite-dimensional near-zero positive tube neither proves nor disproves RH.'
    }
    (root/'interval_taylor_tube_2d_certificate.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    summary='\n'.join([
      f'status={result["status"]}',f'dimension={dim}',f'd_radius={float(RHO_D):.3e}',f'sigma_radius={float(RHO_S):.3e}',f'radius_expansion={float(RHO_D/old_rd):.0f}x',f'combined_second_order_row_remainder={float(eps_rem):.18e}',f'minimum_knot_margin={float(margin):.18e}','exact_tube_bracket=1e-8<lambda_min<5e-8','RH_W_14_DERIVATIVE_TAIL_ISSUE=CORRECTED_AND_REAUDIT_PENDING','RH_CLAIM=False'])+'\n'
    (root/'BUILD_SUMMARY.txt').write_text(summary,encoding='utf-8');print(summary,end='')
if __name__=='__main__':main()
