# TEST REPORT

**Date:** 2026-07-26  
**Python:** 3.13.5

## Exact arithmetic verification

- GPLM rational cases checked: 7
- Rational axis-aligned curve cases checked: 40
- Acceptance arithmetic: exact `fractions.Fraction`
- Floating-point acceptance tests: none
- All tests passed: `true`

## What was verified

1. For all included rational cases:

$$
\max\left\{\frac xa,\frac bx\right\}^2\ge\frac ba.
$$

2. Equality cases satisfy both:

$$
x^2=ab
$$

and:

$$
\frac xa=\frac bx.
$$

3. For each generated rational axis-aligned polyline, the exact arc-length midpoint and rational squared-distance certificates show that all segments are contained in the disk of radius $L/2$.

4. The straight-segment lower bound is checked by the polynomial identity:

$$
\frac{\|c-p\|^2+\|c-q\|^2}{2}-\frac{L^2}{4}
=
u^2+v^2
\ge0.
$$

## Scope warning

Finite computational verification supports the implementation and certificate format. It does not replace the general analytic proofs for all real inputs or all rectifiable curves.
