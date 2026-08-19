# HIPG Formal Toy v0.4 — v0.5 Handoff

## Verified v0.4 additions

- task-class labels removed from the new active-causal learner;
- joint probe/intervention selection by Bayesian expected information gain;
- posterior $P(x\sim_Ty\mid H_t)$ over quotient equivalence;
- OOD partner surface-probe permutation inference;
- counterfactual relaxation diagnostics for infeasible configurations;
- all certificates validated against a v0.4 JSON Schema;
- hash-linked input → result → certificate lineage;
- first restricted typed formal contract fragment for permission/scope preservation.

## v0.5 priority

### A. Escape the finite hand-authored hypothesis list

Current:

$$
\mathcal H=\{H_E,H_J,H_O,H_{J\oplus O}\}.
$$

Next:

- program-synthesis / decision-tree hypothesis generation;
- MDL-regularized quotient hypotheses;
- posterior expansion when all current hypotheses fit badly.

### B. Causal interventions that change world state

Current action changes reward only.

v0.5 should let intervention $a$ change future state:

$$
X_t\xrightarrow{a_t}X_{t+1}.
$$

Then distinguish observation from intervention more sharply.

### C. Multi-step task quotient

Replace one-step reward-equivalence with trajectory equivalence:

$$
x\sim_T y
\iff
\text{future task-value distributions remain equivalent under admissible policies}.
$$

This moves closer to bisimulation / MDP homomorphism.

### D. Learned partner model family

Replace the six hard-coded surface permutations with learned adapter hypotheses.

### E. Certificate semantics

Current schema validation checks structure + hashes.

v0.5 should add semantic consistency checks between:

- status;
- bound;
- relaxation options;
- feasibility point.

### F. Real solver bridge

Move the restricted DSL to one actual solver-backed fragment:

- SMT-LIB with an installed solver, or
- Lean if local toolchain is available.

### G. Protocol regret

Compare active HIPG against:

- random experiment selection;
- probe-only active learner;
- blind repair.

Measure cumulative task regret and experiment cost.

## Non-negotiable invariant

Do not let counterfactual relaxation mutate the current problem silently.

`INFEASIBLE under Θ` remains infeasible until a new explicit $\Theta'$ is created.
