"""Moser Skew Lab v0.5: explicit contact-event system.

Unknowns:
    p = (l1, l2, beta, delta)
    s = common scale
    mu_1,...,mu_4 = branch pressures

Equations:
    m_r(p) = s, r=1,...,4
    sum_r mu_r = 1
    sum_r mu_r grad m_r(p) = 0

This yields nine equations in nine unknowns.
"""
