#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json, math
import weil_interval_core as core

H=F(87,400)
D_MINUS=F(117,512)
D_PLUS=D_MINUS+F(1,5000)
FACT7=F(math.factorial(7))
core.H=H


def activation(d:F):
    log3=core.log_rational_iv(F(3),220)
    sqrt3=core.sqrt_rational_iv(F(3),150)
    mu=core.IV.point(d+4*H)-log3
    positive_sample_gap=log3-core.IV.point(-d+4*H)  # log3 - right endpoint
    if mu.hi <= 0:
        p=core.IV.point(0); state='INACTIVE'
    elif mu.lo > 0 and mu.hi < H:
        u=mu/core.IV.point(H)
        beta=core.IV.point(1)
        for _ in range(7): beta=core.coarsen(beta*u,90)
        beta=beta.scale(F(1,math.factorial(7)))
        coeff=log3/sqrt3
        p=core.coarsen(-(coeff*beta),85)
        state='ACTIVE_FIRST_SPLINE_PIECE'
    else:
        raise ArithmeticError('state not isolated by interval')
    return {
        'd':core.frac_json(d),'mu_d_plus_4h_minus_log3':core.iv_json(mu),
        'state':state,'prime3_lag1_entry':core.iv_json(p),
        'positive_log3_sample_outside_gap':core.iv_json(positive_sample_gap)
    }


def main():
    minus=activation(D_MINUS); plus=activation(D_PLUS)
    payload={
      'schema':'RH-W-10-prime3-soft-activation-v0.1','date':'2026-07-23',
      'basis':{'h':core.frac_json(H),'degree_of_correlation_spline':7,'dimension':15},
      'boundary':{
        'equation':'mu=d+4h-log(3)=0',
        'symbolic_lag1_prime3_entry':'p3(mu)=-(log(3)/sqrt(3))*(mu_+/h)^7/7! for 0<mu<h',
        'regularity':'C^6 but not C^7 at mu=0',
        'derivatives_0_through_6_at_boundary':'all zero from both sides',
        'seventh_derivative_jump':'-(log(3)/sqrt(3))/h^7'
      },
      'theta_minus':minus,
      'theta_zero':{'mu':'0 exactly (symbolic transcendental boundary)','prime3_lag1_entry':'0','state':'BOUNDARY'},
      'theta_plus':plus,
      'quadratic_effect':{
        'formula':'Delta Q_3(c)=2*p3(mu)*sum_{i=1}^{N-1} c_i c_{i+1}',
        'sign_rule':'since p3(mu)<0, positive adjacent correlation lowers Q; negative adjacent correlation raises Q'
      },
      'scope_warning':'This certificate isolates the new prime-3 lag-1 block only. It is not an RH proof and not a full chamber certificate.'
    }
    out=Path(__file__).resolve().parent/'prime3_soft_activation_certificate.json'
    out.write_text(json.dumps(payload,indent=2),encoding='utf-8')
    print(out)
    print('minus_mu_hi',minus['mu_d_plus_4h_minus_log3']['decimal_upper'])
    print('plus_mu_lo',plus['mu_d_plus_4h_minus_log3']['decimal_lower'])
    print('plus_p3',plus['prime3_lag1_entry']['decimal_lower'],plus['prime3_lag1_entry']['decimal_upper'])

if __name__=='__main__':main()
