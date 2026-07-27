# Trust Boundary

## Supported in this package

- Exact rational breakpoint audit of the 18-patch cover.
- Deterministic regeneration of the floating arithmetic matrix, candidates,
  conic programs, dense grids, holdout diagnostics, and ablation.
- Algebraic preservation of real-axis nonnegativity by nonnegative conic
  aggregation.
- Nine unit tests covering the model, exact cover, adaptive refinement,
  conic LP, real-axis positivity, and tail coefficient.

## Floating evidence only

- Candidate coefficients and arithmetic scalar values.
- Sampled regional negativity.
- The $L^1$-Lipschitz sign audit.
- Continuous axis-energy quadrature.
- Evaluations at the first 50 listed ordinates.
- Derivative-variation tail majorants.
- LP and SLSQP optimality.
- Coarse-versus-adaptive reduction factors.

These are labeled E2. Optimizer success flags are not proof of global or even
global-in-class optimality.

## Explicitly not supported

- That any target patch contains a zeta zero.
- That the 18 regional sign bounds are interval-certified.
- That the arithmetic quadratic form is interval-certified.
- That the first 50 ordinates plus the prototype tail exhaust the zero side.
- That all unknown off-axis contributions are bounded.
- That any partial or global domination gap is positive.
- That RH is proved or disproved.

## Data-separation statement

The first 50 zero ordinates are present in `data/first_50_ordinates.csv`.
Candidate generation and conic optimization use only continuous real-axis
quadrature on fixed intervals. The ordinates are evaluated after fitting and
serve only as a holdout diagnostic.

This is not a statistical independence claim: the continuous axis bands cover
the same height range. It is a precise statement that no individual zero
location is fitted or annihilated.

## Provenance boundary

Neo.K / EveMissLab supplied the prior research field and authorized
semi-autonomous continuation. Mathematical architecture, numerical choices,
interpretation, failure classification, and the next-node decision in this
package are attributed to the AI research collaborator. The package does not
represent those technical judgments as Neo.K's mathematical claims.
