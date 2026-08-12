# Active Observer Design and Gauge Breaking

## Problem
The existing observer network uses only measurements invariant under:

z -> -z.

Therefore the global observer map has an exact Z2 ambiguity.

At a representative point z=[0.8, -0.55, 0.4, 0.95]:
- local nonlinear Jacobian rank = 4/4
- smallest eigenvalue of J^T J = 0.723798
- exact global symmetry mismatch q(z)-q(-z) = 0.000e+00

This is the crucial result:

local differential/Fisher identifiability can look complete while a discrete global gauge remains exactly unresolved.

## Active measurement rule
The current provisional global model is an ambiguity set:

H={z_hat,-z_hat}.

For each candidate next measurement h_m, compute a branch-separation utility:

U(m)=|h_m(z_hat)-h_m(-z_hat)| / sigma.

Choose the measurement with maximum U.

No hidden truth is used in selecting the measurement.

## Monte Carlo
Trials: 2000
Measurement noise sigma = 0.08

Active design:
- gauge-breaking odd-channel selection rate = 100.000%
- correct branch identification = 100.000%
- mean predicted separation score = 33.9906

Random design:
- odd-channel selection rate = 39.450%
- correct branch identification = 68.450%
- mean predicted separation score = 8.08554

## Hypothesis-set design
For a four-hypothesis provisional ambiguity set, candidate measurements were also ranked by predicted variance across hypotheses.

Mean active hypothesis variance: 1.30316
Mean random hypothesis variance: 0.293216

## Series-B interpretation

A stronger AI cannot infer information that is exactly erased by every current observer channel.

The correct response to a non-identifiable global model is not:
"infer harder."

It is:
"change the observation."

Thus Series B gains an active layer:

1. infer provisional global equivalence class;
2. identify unresolved transformations/gauges;
3. generate candidate measurements;
4. score how strongly each candidate separates currently equivalent hypotheses;
5. acquire the most informative observation;
6. refine the global equivalence class.

Symbolically:

[S]_O
 --choose measurement m*-->
[S]_(O + m*)
subseteq
[S]_O.

## Local vs global identifiability

The experiment explicitly shows:

rank(J)=4 and J^T J positive definite

does NOT imply global uniqueness.

The Z2 branch ambiguity survives because local Fisher information only probes a neighborhood of one representative.

Therefore a Series-B analyzer needs two distinct diagnostics:
- local identifiability / Fisher information;
- global hypothesis/gauge identifiability.

## Quantum relevance

Adaptive quantum tomography already uses measurement choice based on current information to improve reconstruction.

The Series-B extension proposed here is specifically gauge/observer aware:
choose measurements not merely to reduce local variance, but to break global observer-equivalence classes that the current measurement network cannot distinguish.

This is the natural bridge from passive embedded observers to active scientific observers.
