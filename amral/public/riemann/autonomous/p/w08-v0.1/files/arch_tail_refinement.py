from fractions import Fraction as F
import weil_interval_core as core

def derivative_data7(center,pieces):
    first=pieces[0][2]
    vals=[]
    for order in [0,2,4,6]:
        vals.append(core.poly_eval(core.poly_derivative(first,order),F(0)))
    B7=F(0)
    for left,right,p in pieces:
        d7=core.poly_derivative(p,7)
        B7=max(B7,abs(core.poly_eval(d7,left)),abs(core.poly_eval(d7,right)))
    return (*vals,B7)

def tail_sum_power_iv(K,p):
    # sum_{k=K} inf (2k+1/2)^(-p)
    u=F(4*K+1,2)
    integral=F(1,2*(p-1))*u**(1-p)
    first=u**(-p)
    return core.IV(integral,integral+first)

def arch_series_iv_precise(center,K=100):
    radius,pieces=core.even_sum_pieces(center)
    fzero=core.f_value(center,F(0))
    F0,F2,F4,F6,B7=derivative_data7(center,pieces)
    assert F0==2*fzero
    partial=core.IV.point(0);s0p=F(0)
    for k in range(K):
        aa=F(4*k+1,2);bb=F(2*k+1)
        I=core.laplace_even_sum(center,aa,pieces)
        partial=core.coarsen(partial+I-core.IV.point(F0/bb),55)
        s0p+=F(1,aa)-F(1,bb)
    s0total=core.pi_iv().scale(F(1,4))+core.log_rational_iv(F(2),120).scale(F(1,2))
    lead=(s0total-core.IV.point(s0p)).scale(F0)
    known=tail_sum_power_iv(K,3).scale(F2)+tail_sum_power_iv(K,5).scale(F4)+tail_sum_power_iv(K,7).scale(F6)
    s8=tail_sum_power_iv(K,8)
    rem=core.IV(-B7*s8.hi,B7*s8.hi)
    tail=lead+known+rem
    arch=core.coarsen(-(partial+tail),50)
    audit={'radius':core.frac_json(radius),'series_terms':K,'F0':core.frac_json(F0),'F2':core.frac_json(F2),'F4':core.frac_json(F4),'F6':core.frac_json(F6),'B7_sup':core.frac_json(B7),'leading_tail':core.iv_json(lead),'known_derivative_tail':core.iv_json(known),'remainder_tail':core.iv_json(rem),'tail_interval':core.iv_json(tail),'partial':core.iv_json(partial),'arch':core.iv_json(arch),'method':'7 integrations by parts; monotone integral enclosures for p=3,5,7; p=8 remainder'}
    return arch,audit
