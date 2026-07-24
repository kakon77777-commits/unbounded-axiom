#!/usr/bin/env python3
"""Jump-resolved archimedean tails for odd B-spline correlations.

For a compact piecewise-polynomial even-sum F(x)=f(x)+f(-x), repeated
integration by parts is carried through the top polynomial degree.  The final
piecewise-constant derivative is represented exactly by its jumps, replacing
the coarse |F^(r)| a^{-(r+1)} majorant with exponentially weighted jump tails.

All proof-path operations use Fraction and outward rational intervals.
"""
from __future__ import annotations
from fractions import Fraction as F
from typing import Dict, List, Tuple

import weil_interval_core as base
import mixed_order_core as mixed
from rigorous_refinement_tools import tail_sum_power_refined


def jump_data(degree: int, h: F, center: F):
    radius, pieces = mixed.even_sum_pieces(degree, h, center)
    first = pieces[0][2]
    deriv0 = [
        base.poly_eval(base.poly_derivative(first, j), F(0))
        for j in range(degree)
    ]
    top_values: List[F] = []
    for left, right, poly in pieces:
        dtop = base.poly_derivative(poly, degree)
        top_values.append(base.poly_eval(dtop, (left + right) / 2))
    top0 = top_values[0]
    jumps: List[Tuple[F, F]] = []
    for idx in range(len(pieces) - 1):
        x = pieces[idx][1]
        jumps.append((x, top_values[idx + 1] - top_values[idx]))
    # Extension by zero after the support endpoint.
    jumps.append((radius, -top_values[-1]))
    if any(x <= 0 for x, _ in jumps):
        raise ArithmeticError("jump locations must be strictly positive")
    return radius, deriv0, top0, jumps


def laplace_from_data(degree: int, a: F, deriv0, top0: F, jumps) -> base.IV:
    total = base.IV.point(0)
    for j, value in enumerate(deriv0):
        if value:
            total += base.IV.point(value / a ** (j + 1))
    top = base.IV.point(top0)
    for x, jump in jumps:
        top += base.exp_iv(-a * x, 110).scale(jump)
    total += top.scale(F(1, a ** (degree + 1)))
    return base.coarsen(total, 82)


def laplace_from_jumps(degree: int, h: F, center: F, a: F) -> base.IV:
    """Exact interval evaluation of ∫_0^∞ exp(-a x)(f(x)+f(-x)) dx."""
    _, deriv0, top0, jumps = jump_data(degree, h, center)
    return laplace_from_data(degree, a, deriv0, top0, jumps)


def exponential_power_tail_upper(K: int, p: int, x: F) -> base.IV:
    """Enclose Σ_{k=K}∞ exp(-(2k+1/2)x)/(2k+1/2)^p by [0,U]."""
    if K < 0 or p <= 1 or x <= 0:
        raise ValueError("invalid exponential tail parameters")
    a = F(4 * K + 1, 2)
    first = base.exp_iv(-a * x, 115).scale(F(1, a ** p))
    ratio = base.exp_iv(-2 * x, 115)
    denom = base.IV(F(1) - ratio.hi, F(1) - ratio.lo)
    upper = (first / denom).hi
    return base.coarsen(base.IV(F(0), upper), 82)


def arch_series_jump_resolved(
    degree: int,
    h: F,
    center: F,
    K: int,
    power_cutoff: int = 20000,
):
    """Rigorous archimedean contribution with exact derivative-jump tail.

    The partial sum uses the jump formula for each Laplace transform.  The
    remaining non-exponential power tails are enclosed by rational continuation,
    while every knot jump receives an exponentially decaying geometric bound.
    """
    radius, deriv0, top0, jumps = jump_data(degree, h, center)
    fzero = mixed.f_value(degree, h, center, F(0))
    if deriv0[0] != 2 * fzero:
        raise AssertionError("even-sum normalization mismatch")

    partial = base.IV.point(0)
    leading_partial = F(0)
    for k in range(K):
        aa = F(4 * k + 1, 2)
        bb = F(2 * k + 1)
        integral = laplace_from_data(degree, aa, deriv0, top0, jumps)
        partial += integral - base.IV.point(deriv0[0] / bb)
        if (k + 1) % 100 == 0:
            partial = base.coarsen(partial, 82)
        leading_partial += F(1, aa) - F(1, bb)

    leading_total = (
        base.pi_iv().scale(F(1, 4))
        + base.log_rational_iv(F(2), 180).scale(F(1, 2))
    )
    leading_tail = (leading_total - base.IV.point(leading_partial)).scale(deriv0[0])

    derivative_tail = base.IV.point(0)
    derivative_terms: Dict[str, dict] = {}
    for j, value in enumerate(deriv0[1:], start=1):
        if value == 0:
            continue
        p = j + 1
        term = tail_sum_power_refined(K, p, power_cutoff).scale(value)
        derivative_tail += term
        derivative_terms[str(p)] = base.iv_json(term)

    top_power_tail = tail_sum_power_refined(K, degree + 1, power_cutoff).scale(top0)

    jump_tail = base.IV.point(0)
    jump_terms = []
    for x, jump in jumps:
        raw = exponential_power_tail_upper(K, degree + 1, x)
        term = raw.scale(jump)
        jump_tail += term
        jump_terms.append({
            "x": base.frac_json(x),
            "jump": base.frac_json(jump),
            "positive_sum_bound": base.iv_json(raw),
            "signed_term": base.iv_json(term),
        })

    tail = leading_tail + derivative_tail + top_power_tail + jump_tail
    arch = base.coarsen(-(partial + tail), 80)
    audit = {
        "degree": degree,
        "radius": base.frac_json(radius),
        "series_terms": K,
        "power_tail_cutoff": power_cutoff,
        "derivatives_at_zero": {
            str(j): base.frac_json(value) for j, value in enumerate(deriv0)
        },
        "top_derivative_at_zero_plus": base.frac_json(top0),
        "leading_tail": base.iv_json(leading_tail),
        "derivative_power_tails": derivative_terms,
        "top_power_tail": base.iv_json(top_power_tail),
        "jump_tails": jump_terms,
        "jump_tail_total": base.iv_json(jump_tail),
        "tail_interval": base.iv_json(tail),
        "partial": base.iv_json(partial),
        "arch": base.iv_json(arch),
        "method": "full integration-by-parts through spline degree plus exponentially weighted derivative jumps",
    }
    return arch, audit
