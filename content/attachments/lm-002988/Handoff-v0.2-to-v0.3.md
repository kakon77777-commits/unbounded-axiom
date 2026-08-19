# HIPG Formal Toy v0.2 — v0.3 Handoff

## Verified v0.2 scope

v0.2 now instantiates:

- quotient inference from partial task probes;
- singleton-to-quotient `MERGE`;
- counterexample-driven `SPLIT`;
- legacy `REMAP` / `ROLLBACK`;
- approximate TSSH distortion;
- exact quotient bit lower bound;
- noisy BSC benchmark;
- empirical mutual information;
- Fano-style lower-bound comparison;
- first executable $L_A\leftrightarrow L_F\leftrightarrow L_E\leftrightarrow L_H$ bridge;
- provenance anchors;
- Gap Certificate;
- permission-drift detection and repair;
- mixed SUCCESS / INFEASIBLE / UNKNOWN diagnostics.

## v0.3 priority

### A. Remove more evaluator oracles

Current quotient repair uses evaluator-provided counterexamples and a finite available-probe set.

v0.3 should select probes by expected information gain or active disagreement.

### B. Noisy quotient learning

Learn $\widehat{\mathcal Q}_T$ when probe outputs and task feedback are noisy.

### C. Finite-evidence MERGE

Current MERGE is exact under active probe equality.

v0.3 should require a statistical merge criterion and retain rollback evidence.

### D. TSSH calibration

Learn or tune:

$$
(w_E,w_R,w_J,w_O)
$$

from task loss rather than fixing them manually.

### E. Bridge round-trip / commutativity

Implement:

$$
L_H\to L_F\to L_A\to L_H'
$$

and test:

$$
L_H\approx_T L_H'.
$$

Also compare direct and formal paths:

$$
\tau_{FA}\circ\tau_{EF}
\approx_T
\tau_{EA}.
$$

### F. Feasibility region estimator

Return a machine-readable estimate for:

$$
(D_T,C_{comm},C_{comp},C_{adapt},C_{audit},L_{latency}).
$$

### G. Certificate library

Unify:

- Success Certificate;
- Gap Certificate;
- Structural Impossibility Certificate;
- Exact-bit Certificate;
- Fano Information Certificate;
- Unknown / Non-identifiability Certificate.

## Non-negotiable invariant

Never convert an explicit lower bound or structural obstruction into blind protocol repair.
