# Results

## Main experiment

The adaptive cover contains 18 rational patches and the candidate library
contains 72 rank-one test functions.

All 18 patches satisfy:

- dense-core maximum at most $-0.99999999999989$ after unit normalization;
- positive arithmetic scalar, with imposed aggregate floor $10^{-3}$;
- negative crude floating Lipschitz upper bound.

The worst crude continuous upper bound is

$$
-0.3715422433640927.
$$

This closes the sampled/local-sign engineering objective for this window at
evidence level E2. It does not supply an interval certificate.

## Coarse versus adaptive cover

| Metric | Coarse 6-patch cover | Adaptive 18-patch cover | Reduction factor |
| --- | ---: | ---: | ---: |
| Patches passing crude continuous sign audit | 3/6 | 18/18 | — |
| Worst axis-band energy | 10521.354469 | 48.907282 | 215.13 |
| Worst first-50 holdout mass | 1122.654086 | 13.079704 | 85.83 |
| Worst prototype tail majorant | 4063.657732 | 8.471493 | 479.69 |
| Worst partial-budget deficit magnitude | 5196.499341 | 20.401803 | 254.71 |

The decisive refinement is anisotropic: near the symmetry axis, reducing the
height-window width from $0.20$ to $0.10$ removes the numerical catastrophe.
Refining only the distance coordinate does not.

## What multiple test functions did

At zero energy slack, stage-one axis-energy minimization agrees with the best
single candidate to numerical precision on every patch. The diagonal cone
therefore does not improve the primary leakage optimum.

Multi-test mixtures become useful on the transition stratum
$y\in[-0.17,-0.135]$:

- X0_Y1: guard improves by about 1.93%;
- X1_Y1: guard improves by about 9.41%;
- X2_Y1: guard improves by about 18.06%.

The corresponding energy overheads range from about 0.45% to 5%. On most
other patches the optimized guard is already nonpositive and a single
candidate remains optimal.

## Global-budget failure

After normalizing the target core margin to one, every partial gap

$$
\Delta_\alpha^{\mathrm{partial}}
=
1-Z_{50}-E_{\mathrm{tail}}-\max(E_{\mathrm{guard}},0)
$$

is negative. Across the adaptive family it ranges approximately from
$-8.97$ to $-20.40$.

This calculation does not even charge all unknown off-axis bands, so it cannot
support a global certificate. The experiment succeeds as a localization and
architecture result, while failing the required global-dominance test.

## Research decision

Further blind rectangular refinement is not the next bottleneck. The adaptive
cover has already converted the near-axis blow-up into a bounded but still
insufficient leakage ratio.

The next node should introduce a PSD Gram variable:

$$
f_A
=
\sum_{j,k}A_{jk}
\left(g_j*\widetilde g_k\right),
\qquad
A\succeq0.
$$

The diagonal cone tested here is the special case where $A$ is diagonal.
Off-diagonal terms are the next available degrees of freedom that can preserve
real-axis positivity while changing off-axis phase and leakage trade-offs.
