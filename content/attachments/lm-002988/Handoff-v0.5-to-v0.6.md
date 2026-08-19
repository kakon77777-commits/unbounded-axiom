# HIPG Formal Toy v0.5 — v0.6 Handoff

## Verified v0.5 additions

- escaped the finite hand-authored task-hypothesis list for the new synthesis mode;
- Boolean program synthesis with MDL prior;
- evidence-triggered posterior/hypothesis-family expansion;
- explicit interventions that change future world state;
- first multi-step trajectory quotient;
- generated 48-member partner adapter family with inversion operators;
- certificate schema + hash + semantic consistency validation;
- first actual solver-backed formal fragment via SymPy SAT;
- protocol regret comparison against random, probe-only, and blind-repair baselines.

## v0.6 priority

### A. Learn the grammar, not only the expression

Current:

$$
\mathcal G_{\mathrm{bool}}
$$

is still supplied by the researcher.

Next:

- grammar/operator proposal;
- reusable subexpression discovery;
- MDL over the grammar itself;
- library learning across multiple tasks.

### B. Learn transition structure

Current multi-step quotient uses known transitions.

Next:

$$
\widehat P(x'|x,a)
$$

must be learned from intervention trajectories.

Then quotient discovery should use confidence sets over transition/value signatures.

### C. Partial observability

Move from state:

$$
X_t
$$

to belief:

$$
b_t=P(X_t|H_t).
$$

Then define a finite belief-task quotient.

### D. Joint partner/task construction

Current partner adapter uses anchor samples with canonical fields visible.

Next remove that anchor privilege and infer:

$$
\text{task rule}
+
\text{partner adapter}
+
\text{quotient}
$$

jointly from reward / execution traces.

### E. Stronger solver bridge

SymPy SAT is real but propositional.

v0.6 should attempt:

- arithmetic constraints;
- temporal constraints;
- a local SMT/Lean backend if installed;
- proof/certificate export rather than only SAT witness.

### F. Learned impossibility diagnosis

Current lower-bound classes are coded.

Next ask whether the constructor can choose between:

```text
repairable
information-limited
resource-limited
non-identifiable
structurally impossible
unknown
```

from observed evidence without a benchmark mode label.

### G. Regret with experiment cost and model expansion cost

Use:

$$
R_T
=
\sum_t
\left[
\Delta V_t
+
\lambda_E C_{\mathrm{experiment},t}
+
\lambda_M C_{\mathrm{model},t}
\right].
$$

### H. Formal toy theorem package

Extract the finite v0.5 results into a theorem-style document:

1. generated-library completeness at bounded Boolean truth tables;
2. state-transition quotient refinement;
3. certificate semantic invariants;
4. finite protocol-regret result as an empirical proposition, not a theorem.

## Non-negotiable invariant

Do not silently promote a generated grammar or solver fragment into a universal language.

Every constructor must remain parameterized by its hypothesis / operator / verifier class.
