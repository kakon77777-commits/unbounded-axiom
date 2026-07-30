#!/usr/bin/env python3
"""Higher-resolution rational enclosures used by RH-W-09."""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
import weil_interval_core as core

BERNOULLI = {
    2: F(1, 6),
    4: F(-1, 30),
    6: F(1, 42),
    8: F(-1, 30),
    10: F(5, 66),
    12: F(-691, 2730),
}


def euler_gamma_binet_iv(n: int = 100, terms: int = 4) -> core.IV:
    """Euler gamma via the digamma asymptotic expansion with signed remainder.

    For positive integer n, psi(n)=H_{n-1}-gamma.  The Binet remainder has the
    sign of the first omitted digamma term and magnitude below that term.
    """
    if 2 * terms + 2 not in BERNOULLI:
        raise ValueError("missing Bernoulli number")
    harmonic = sum((F(1, k) for k in range(1, n + 1)), F(0))
    result = core.IV.point(harmonic - F(1, 2 * n)) - core.log_rational_iv(F(n), 160)
    for k in range(1, terms + 1):
        result += core.IV.point(BERNOULLI[2 * k] / (F(2 * k) * F(n) ** (2 * k)))
    next_magnitude = abs(BERNOULLI[2 * terms + 2]) / (
        F(2 * terms + 2) * F(n) ** (2 * terms + 2)
    )
    # gamma correction is minus the digamma remainder.
    if (terms + 1) % 2 == 0:
        correction = core.IV(-next_magnitude, F(0))
    else:
        correction = core.IV(F(0), next_magnitude)
    return core.coarsen(result + correction, 85)


@lru_cache(maxsize=None)
def tail_sum_power_refined(K: int, p: int, cutoff: int = 20000) -> core.IV:
    """Enclose sum_{k=K}^inf (2k+1/2)^(-p).

    Thousands of rational terms are accumulated once and the remaining tail is
    enclosed by the monotone integral test.  Periodic coarsening keeps exact
    denominator growth bounded without introducing floating point.
    """
    if cutoff <= K:
        raise ValueError("cutoff must exceed K")
    partial = core.IV.point(0)
    for k in range(K, cutoff):
        partial += core.IV.point(F(2, 4 * k + 1) ** p)
        if (k - K + 1) % 250 == 0:
            partial = core.coarsen(partial, 90)
    u = F(4 * cutoff + 1)
    integral = F(2**p, 4 * (p - 1)) * u ** (1 - p)
    first = F(2, u) ** p
    return core.coarsen(partial + core.IV(integral, integral + first), 85)


def derivative_data7(center: F, pieces):
    first = pieces[0][2]
    values = [
        core.poly_eval(core.poly_derivative(first, order), F(0))
        for order in (0, 2, 4, 6)
    ]
    bound7 = F(0)
    for left, right, poly in pieces:
        d7 = core.poly_derivative(poly, 7)
        bound7 = max(
            bound7,
            abs(core.poly_eval(d7, left)),
            abs(core.poly_eval(d7, right)),
        )
    return (*values, bound7)


def arch_series_high_resolution(center: F, K: int = 180):
    radius, pieces = core.even_sum_pieces(center)
    fzero = core.f_value(center, F(0))
    F0, F2, F4, F6, B7 = derivative_data7(center, pieces)
    assert F0 == 2 * fzero

    partial = core.IV.point(0)
    leading_partial = F(0)
    for k in range(K):
        aa = F(4 * k + 1, 2)
        bb = F(2 * k + 1)
        integral = core.laplace_even_sum(center, aa, pieces)
        partial = core.coarsen(partial + integral - core.IV.point(F0 / bb), 65)
        leading_partial += F(1, aa) - F(1, bb)

    leading_total = (
        core.pi_iv().scale(F(1, 4))
        + core.log_rational_iv(F(2), 150).scale(F(1, 2))
    )
    leading_tail = (leading_total - core.IV.point(leading_partial)).scale(F0)
    known_tail = (
        tail_sum_power_refined(K, 3).scale(F2)
        + tail_sum_power_refined(K, 5).scale(F4)
        + tail_sum_power_refined(K, 7).scale(F6)
    )
    s8 = tail_sum_power_refined(K, 8)
    remainder = core.IV(-B7 * s8.hi, B7 * s8.hi)
    tail = leading_tail + known_tail + remainder
    arch = core.coarsen(-(partial + tail), 75)
    audit = {
        "radius": core.frac_json(radius),
        "series_terms": K,
        "tail_rational_cutoff": 20000,
        "F0": core.frac_json(F0),
        "F2": core.frac_json(F2),
        "F4": core.frac_json(F4),
        "F6": core.frac_json(F6),
        "B7_sup": core.frac_json(B7),
        "leading_tail": core.iv_json(leading_tail),
        "known_power_tail": core.iv_json(known_tail),
        "remainder_tail": core.iv_json(remainder),
        "tail_interval": core.iv_json(tail),
        "partial": core.iv_json(partial),
        "arch": core.iv_json(arch),
        "method": "signed derivative expansion plus refined rational power tails",
    }
    return arch, audit
