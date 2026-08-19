# HIPG Formal Toy v0.6 — v0.7 Handoff

## What v0.6 actually removed

- task expression need not come from a finite hand-authored list;
- binary operator subset is selected across tasks;
- reusable subexpressions can become learned macros;
- trajectory quotient no longer receives the hidden transition table;
- a first belief-state quotient handles raw observation aliasing;
- partner/task decomposition is explicitly diagnosed as non-identifiable when only behavior is available;
- causal interventions can break that symmetry in the finite benchmark;
- failure diagnosis can be learned from examples rather than selected by a benchmark mode label;
- arithmetic bridge uses a real LP solver.

## Remaining supplied structures

v0.6 still receives:

1. a finite operator superset $\{\land,\lor,\oplus\}$;
2. named state and action spaces for dynamics learning;
3. a known observation/belief model in the POMDP toy;
4. known intervention semantics `TOGGLE_E/J/O` in the identifiable joint case;
5. a synthetic labeled distribution to train failure diagnosis;
6. a hand-authored linear contract family.

These are the next oracles.

---

# v0.7 priority A — open operator proposal

Move from:

$$
\mathcal G\subseteq\mathcal O_0
$$

to a constructor that can propose derived operators:

$$
\phi(x_1,\ldots,x_k)
$$

from repeated program fragments and evaluate them by cross-task compression / regret.

Do not call this universal grammar induction. Keep a bounded meta-language explicit.

---

# Priority B — active dynamics learning with confidence sets

Current transition exploration covers every state-action pair.

Next let the constructor choose:

$$
(x,a)^*
=
\arg\max
\text{expected quotient / value uncertainty reduction}.
$$

Maintain:

$$
\mathcal P_t(P)
$$

or confidence sets rather than a single majority transition table.

---

# Priority C — learned observation model / belief update

Current belief quotient receives beliefs directly.

Next infer:

$$
\widehat O(o\mid x),
\qquad
b_{t+1}
\propto
\widehat O(o_{t+1}\mid x')
\sum_x
\widehat P(x'\mid x,a)b_t(x).
$$

Then construct the quotient over learned belief states.

---

# Priority D — joint latent model only up to equivalence

The non-identifiability result should become first-class.

Instead of demanding a unique hidden ontology, output:

$$
[(\rho,h)]_{\equiv}
$$

—the equivalence class of latent decompositions compatible with all current evidence.

Then ask which intervention maximally splits that class.

---

# Priority E — OOD-calibrated failure diagnosis

The v0.6 decision tree learns on one synthetic distribution.

Next:

- distribution shift;
- probability calibration;
- abstention threshold;
- explicit `UNKNOWN_DIAGNOSIS` when confidence is low;
- compare learned routing with theorem-backed hard guards.

---

# Priority F — mixed discrete + arithmetic formal bridge

Combine:

- permission/type SAT constraints;
- arithmetic LP constraints;
- provenance anchors.

If a local SMT/Lean backend becomes available, add it as a new backend rather than replacing the existing restricted, verified fragments.

---

# Priority G — meta-regret

Measure cost across multiple tasks:

$$
R_{\mathrm{meta}}
=
\sum_T
\left(
R_T
+
\lambda_G C_{\mathrm{grammar\ expansion}}
+
\lambda_P C_{\mathrm{partner\ adaptation}}
\right).
$$

This is the natural metric for evaluating whether learned macros/operators genuinely amortize across tasks.

---

# Non-negotiable invariant

Never convert latent non-identifiability into semantic `SUCCESS` merely because observable task behavior is perfect.
