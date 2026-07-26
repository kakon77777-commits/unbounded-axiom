# RH Validated Separation–Positivity Intersection Certificate v0.2

This package upgrades the floating-point intersection candidate from v0.1 to a replayable **validated-numerics certificate** for one explicitly defined compactly supported piecewise-linear test function.

For the same function \(\psi\), it verifies:

\[
2\operatorname{Re}(G(w)^2)<0
\qquad
\text{for every }w\in[8,8.5]+i[-0.2,-0.1],
\]

and

\[
Q_{\mathrm{arith}}(\psi)>0
\]

in the multiplicative Riemann–Weil normalization used by the preceding prototypes.

## Supplied certificate

The included run returns:

- continuous-region upper bound:
  \[
  2\operatorname{Re}(G(w)^2)\le -2.2416560\times10^{-6};
  \]
- arithmetic interval:
  \[
  Q_{\mathrm{arith}}(\psi)\in
  [0.0337626745,\,0.0613476964];
  \]
- 480 certified subrectangles;
- 0 unresolved subrectangles;
- 98 activated prime powers;
- endpoint residual interval containing zero with radius below \(7\times10^{-36}\).

## Run

```bash
python run_certificate.py \
  --config examples/certificate.json \
  --output outputs
```

Replay and compare the certificate:

```bash
python verify_certificate.py \
  --config examples/certificate.json \
  --reference outputs/certificate.json \
  --output outputs/replay
```

Tests:

```bash
pytest -q
```

A normal replay takes roughly 10–20 seconds on the reference environment.

## Exact model used by the verifier

The function is not an opaque sampled array. It is defined by

\[
\psi(t)=\sum_{i=0}^{600}y_i\,\max\!\left(1-\frac{|t-t_i|}{h},0\right),
\qquad
h=0.01,
\qquad
 t_i=-3+ih.
\]

The 601 base ordinates are decimal constants in `data/base_nodes.csv`. The central ordinate is corrected by an explicitly recomputed ratio so that

\[
G(i/2)=0.
\]

For this hat-spline model,

\[
G(w)=h\left(\frac{\sin(wh/2)}{wh/2}\right)^2
\sum_{i=0}^{600}y_i e^{iwt_i},
\]

and its autocorrelation is a finite sum of compact cubic B-spline kernels. These closed forms are what the verifier encloses.

## What the certificate means

It proves, relative to the stated formulas and the `mpmath` interval backend, that the same explicitly defined finite-dimensional test function belongs to both:

1. a continuously certified regional negative-direction class;
2. a certified positive arithmetic-scalar class.

It therefore rules out the claim that these two requirements are immediately incompatible in this model.

## What it does not mean

This package does **not**:

- prove that the arithmetic matrix is positive semidefinite on every vector;
- control all non-target zeta-zero contributions;
- prove that a zeta zero lies in the target rectangle;
- derive the Riemann–Weil formula inside a proof assistant;
- prove or disprove the Riemann hypothesis.

The interval verifier is stronger than dense-grid floating-point checking, but its trusted base includes Python, `mpmath`, the supplied explicit-formula normalization, and ordinary machine execution. See `TRUST_BOUNDARY.md`.
