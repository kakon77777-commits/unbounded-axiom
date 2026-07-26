# Results

## Primary dual family

| Quantity | Result |
|---|---:|
| Patch count | $18$ |
| Coordinate dimension | $22$ |
| Axis band | $[18,23]$ |
| Axis grid | $26$ points, step $0.2$ |
| Downward count | $7.113998598824$ |
| Tail fraction | $10^{-3}$ |
| Dual lower bound | $2$ |
| Target budget | $<1$ |
| Floating pass | $18/18$ |

Floating minimum-eigenvalue range:

$$
[3.1042101910186086,3.1042422674836540]\times10^{-5}.
$$

At $\rho=10^{-6}$ the family still passes $18/18$; at $\rho=0$ every
axis-only matrix has a numerically nonpositive minimum eigenvalue. The
primary claim therefore retains its explicit tail regularizer.

## Exact rational surrogate

The exported 12-decimal rational model has:

- exact positive $LDL^{\mathsf T}$ pivots for the tail matrix;
- exact positive pivots for all 18 witness matrices;
- 22 pivots per witness;
- minimum reported pivot $3.240761260825524\times10^{-5}$.

The same pass occurs at 6, 8, 10, and 12 decimal places.

## Sensitivity

| Sweep | Values | Pass |
|---|---|---:|
| Model step | $0.02,0.015,0.01,0.0075$ | $18/18$ each |
| Axis step | $0.2,0.1,0.05,0.025,0.0125$ | $18/18$ each |
| Tail fraction | $10^{-6}$ through $10^{-3}$ | $18/18$ each |
| Rational decimals | $6,8,10,12$ | all exact |

## Support–cost diagnostic

| Event | Sampled $R$ | Cutoff proxy $e^{2R}$ | Ratio vs. $R=3$ |
|---|---:|---:|---:|
| Last sampled all-patch tail kill | $5.0$ | $22026.47$ | $54.60$ |
| First sampled any-patch escape | $5.1$ | $26903.19$ | $66.69$ |
| First stable sampled all-center escape | $8.5$ | $24154952.75$ | $59874.14$ |

These are center-only, floating, fixed-density diagnostics. They neither
construct a primal candidate nor prove a critical support radius.

## Decision

The current $R=3$ patchwise finite-model function class is rejected. The next
node will map the support–prime dual frontier and gate expensive primal work
by dual lower bounds.
