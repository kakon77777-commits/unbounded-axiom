# Results

## Main comparison

Across 18 adaptive patches, the full Gram search reduces the sampled
axis-plus-tail majorant against the diagonal 72-ray cone by:

| Statistic | Reduction |
|---|---:|
| Minimum | $10.8866\%$ |
| Mean | $21.0776\%$ |
| Maximum | $28.6644\%$ |

All 18 known-zero holdout masses also decrease, by $0.9864\%$ to $28.2083\%$.
The optimized directions are $29.22^\circ$ to $70.15^\circ$ away from the
nearest inherited ray in the $C_0$ metric. Cross-term freedom therefore
discovers materially new phase-shaped directions.

## Failure scale

| Quantity | Minimum | Maximum | Target |
|---|---:|---:|---:|
| Sampled axis plus tail | $64.604$ | $142.731$ | $<1$ |
| Continuity-corrected axis plus tail | $89.771$ | $354.164$ | $<1$ |
| Sampled partial gap | $-141.930$ | $-63.604$ | $>0$ |
| Refined core continuous upper | $-0.9923$ | $-0.9606$ | $<0$ |

The axis correction is conservative on the higher-$x$ patches, but this does
not affect the research decision: even the uncorrected sampled majorant misses
the target by a factor of at least $64.60$.

## Dominant band

| Band | Mean sampled charge | Mean objective share | Dominant patches |
|---|---:|---:|---:|
| $[14,18]$ | $4.001$ | $3.98\%$ | $0$ |
| $[18,23]$ | $64.602$ | $61.73\%$ | $18$ |
| $[23,35]$ | $19.573$ | $18.70\%$ | $0$ |
| $[35,70]$ | $0.487$ | $0.49\%$ | $0$ |
| $[70,145]$ | $0.024$ | $0.02\%$ | $0$ |

The tail contributes on average $15.09\%$. The obstruction is spatially
localized: the target window lies near height $20$, and the $[18,23]$ band is
the dominant charge in every patch.

## Rank study

| Patch | Rank $1$ | Rank $2$ | Rank $4$ | Rank $8$ | Numerical rank |
|---|---:|---:|---:|---:|---:|
| `X1_Y0` | $64.6038463421$ | $64.6038463420$ | $64.6038463422$ | $64.6038463424$ | $1$ |
| `X1_Y1` | $137.7908257036$ | $137.7908257022$ | $137.7908257027$ | $137.7908257017$ | $1$ |
| `x2_Y2` | $84.4520409177$ | $84.4520409182$ | $84.4520409179$ | $84.4520409177$ | $1$ |
| `x2_Y3` | $121.8674577314$ | $121.8674577313$ | $121.8674577310$ | $121.8674577312$ | $1$ |

The largest within-patch objective range is below $2.0\times10^{-9}$. This is
empirical rank collapse, not a theorem that the convex SDP optimum has rank
one.

## Decision

The diagonal cone was too restrictive, but rank expansion is not the current
bottleneck. The next node should seek a dual lower bound showing how much
$[18,23]$ real-axis mass is forced by unit negativity on each off-axis patch.
This can either:

1. certify that the present compact-support/structural-zero family cannot
   reach budget $1$; or
2. identify exactly which basis enlargement or support change is required.

Until that dual question is answered, another broad primal search has poor
expected information value.
