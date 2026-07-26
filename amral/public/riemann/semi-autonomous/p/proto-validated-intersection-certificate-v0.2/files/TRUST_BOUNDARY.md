# Trust boundary

The supplied result is a validated-numerics certificate, not a kernel-checked formal proof.

## Trusted components

1. CPython and the operating system.
2. `mpmath` interval arithmetic and its transcendental-function enclosures.
3. IEEE floating-point operations used only for geometric bookkeeping and outward-rounded scalar bounds.
4. The stated compact-support Riemann–Weil normalization.
5. The algebraic formulas for the hat Fourier transform and cubic autocorrelation kernel.
6. The input decimal ordinates in `data/base_nodes.csv`.

## Reduced trust compared with v0.1

The v0.2 sign conclusions do not depend on:

- a finite spectral sample being representative of a continuum;
- FFT correlation interpolation;
- a floating-point eigenvalue being positive;
- the SLSQP success flag;
- a hidden coefficient file from the earlier package.

The verifier reconstructs the function from 601 public ordinates and recomputes both enclosures.

## Remaining formalization work

For proof-assistant-level trust, the following should be ported:

- interval elementary functions;
- complex Taylor enclosure;
- hat-transform identity;
- cubic autocorrelation identity;
- composite-midpoint error theorem;
- the adopted explicit-formula theorem and its normalization;
- prime enumeration and primality certificates.
