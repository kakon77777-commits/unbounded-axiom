# HIPG Formal Toy v0.3 — v0.4 Handoff

## Verified v0.3 additions

- active probe selection by empirical conditional mutual information;
- noisy active quotient recovery;
- finite-evidence MERGE with confidence-bound evidence;
- TSSH weight calibration in a synthetic linear task-loss model;
- $L_H\to L_F\to L_A\to L_H'$ round-trip checks;
- direct/formal commutativity checks and repair;
- empirical Protocol Feasibility points;
- unified certificate format;
- full backward compatibility with v0.2 canonical cases.

## v0.4 priority: Active Causal Quotient Discovery

### A. Remove rich task-label feedback

Current active probe learner sees a noisy class label $Y_T$.

Replace it with weaker task feedback:

$$
V_T\in\{0,1\}
$$

or scalar reward.

### B. Action/intervention selection

Choose not only a probe $p$, but an intervention $a$:

$$
(p^\ast,a^\ast)
=
\arg\max_{p,a}
\mathbb E[\mathrm{InformationGain}\mid p,a].
$$

### C. Bayesian / confidence-aware quotient state

Represent:

$$
P(x\sim_T y\mid H_t)
$$

rather than a hard partition only.

### D. OOD partner transfer

Train/calibrate constructor on one private ontology, then test on unseen symbol permutations / encoders.

### E. Counterfactual impossibility diagnostics

When a target is infeasible, estimate which relaxation changes feasibility most:

- more bits;
- better feedback;
- fewer task distinctions;
- more latency;
- stronger verifier.

### F. Certificate validation

Validate all emitted certificates against `certificate_schema.json` and add hash-linked provenance lineage.

### G. Formal methods bridge

Start one actually machine-checkable contract fragment (Lean/SMT or a restricted typed DSL) for permission/scope preservation.

## Non-negotiable invariant

Explicit lower bounds and structural obstructions remain terminal diagnostic branches unless assumptions are changed.
