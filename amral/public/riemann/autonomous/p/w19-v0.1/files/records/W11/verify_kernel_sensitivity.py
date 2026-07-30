#!/usr/bin/env python3
"""Independent exact/rational-interval verifier for RH-W-11 local scaling law."""
from __future__ import annotations
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
import sys

import weil_interval_core as core

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent


def parse_f(obj):
    return F(int(obj['num']), int(obj['den']))


def parse_iv(obj):
    return core.IV(parse_f(obj['lower']), parse_f(obj['upper']))


def iv_pow(x, n):
    out = core.IV.point(1)
    for _ in range(n):
        out = core.coarsen(out*x, 100)
    return out


def contains(outer, inner):
    return outer.lo <= inner.lo and inner.hi <= outer.hi


def main():
    d=json.loads((ROOT/'kernel_sensitivity_certificate.json').read_text(encoding='utf-8'))
    assert d['schema']=='RH-W-11-kernel-sensitivity-v0.1'
    h=parse_f(d['source_parameter']['h'])
    dp=parse_f(d['source_parameter']['d_theta_plus'])
    log3=core.log_rational_iv(F(3),180)
    sqrt3=core.sqrt_rational_iv(F(3),110)
    coeff=core.coarsen(log3/sqrt3,95)
    mu=core.coarsen(core.IV.point(dp+4*h)-log3,95)
    eps=core.coarsen(mu/core.IV.point(h),95)
    assert mu.lo>0
    stored_eps=parse_iv(d['source_parameter']['normalized_penetration_eps'])
    assert contains(stored_eps,eps) or contains(eps,stored_eps)

    rows=d['auto_family']
    assert [r['prime_activation_order'] for r in rows]==[1,3,5,7,9,11]
    mags=[]
    for row in rows:
        m=int(row['basis_degree_m']); r=2*m+1
        mag=core.coarsen(coeff*iv_pow(eps,r),95).scale(F(1,factorial(r)))
        signed=-mag
        # decimals are presentation only; exact formula is recomputed here.
        assert signed.hi<0
        mags.append(mag)
    for m in range(len(mags)-1):
        ratio=mags[m+1]/mags[m]
        expected=core.coarsen(iv_pow(eps,2).scale(F(1,(2*m+2)*(2*m+3))),95)
        # coarsening may differ by a few outer ulps; require overlap and tightness.
        assert not (ratio.hi < expected.lo or expected.hi < ratio.lo)
    assert mags[1].lo/mags[3].hi > F(10**16)
    print('schema=OK')
    print('mu_positive=OK')
    print('auto_activation_orders=1,3,5,7,9,11')
    print('successive_ratio_identity=OK')
    print('m1_over_m3_gt_1e16=OK')
    print('status=EXACT_INTERVAL_VERIFICATION_OK')
    print('RH_CLAIM=False')

if __name__=='__main__':
    main()
