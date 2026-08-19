# HIPG Formal Toy v0.9 — v1.0 Handoff

## What v0.9 now has

- learned finite intervention kernels rather than only a permutation of named toggles;
- a first finite grounding number $G^*$;
- active finite POMDP model discovery without hidden-state resets;
- explicit operator-family expansion across arity/domain/time;
- replayable temporal proof objects;
- a content-addressed theorem-anchor registry;
- online drift detection before retirement;
- public semantic-equivalence-class artifacts.

---

# v1.0 Priority 1 — end-to-end constructor, not isolated feature demos

The current runtime still routes different capabilities through benchmark modes.

v1.0 should create one integrated episode:

$$
\boxed{
\text{raw observations/actions}
\to
\text{coupleability diagnosis}
\to
\text{model/equivalence class}
\to
\text{experiment selection}
\to
\text{grounding request if needed}
\to
\text{protocol}
\to
\text{formal bridge}
\to
\text{certificate}
}
$$

with a single evolving Master State $\Omega_t$.

---

# Priority 2 — grounding number over the full joint gauge class

v0.9 proves $G^*=2$ only for the six-element intervention permutation class.

v1.0 should compute or bound:

$$
G^*(\mathcal M)
$$

for a joint finite class containing:

$$
(\rho,h,\iota,P,O,R).
$$

Then distinguish:

- observational grounding;
- intervention grounding;
- semantic naming grounding;
- formal/verifier grounding.

---

# Priority 3 — active grounding acquisition

Do not merely calculate $G^*$ offline.

Let the constructor choose which external anchor to request:

$$
a^*_{\mathrm{ground}}
=
\arg\max_a
\frac{\operatorname{ExpectedClassReduction}(a)}{C_{\mathrm{ground}}(a)}.
$$

This is the beginning of a theory of **minimal shared reality acquisition**.

---

# Priority 4 — intervention language growth beyond the supplied finite DSL

v0.9 learns among 32 behavioral kernels generated from a supplied grammar.

v1.0 should allow:

- new stochastic probabilities;
- longer compositions;
- state-conditional interventions;
- learned macro-interventions;
- intervention library retirement/reuse.

Keep MDL/search cost explicit.

---

# Priority 5 — active POMDP quotient, not just predictive model ID

Current v0.9 active POMDP result measures predictive-signature identification accuracy.

v1.0 should select experiments directly for:

$$
\boxed{
\operatorname{Entropy}(\mathcal Q_T\mid H_t)
}
$$

and stop when the **task quotient** is identified even if full $P,O,R$ remains ambiguous.

---

# Priority 6 — equivalence artifact schema + transition lineage

Create a JSON Schema for `HIPG-EQUIV-1.0` and support:

```text
parent_equivalence_class_hash
split_by_intervention
split_by_grounding_anchor
child_classes
```

so epistemic refinement itself becomes a provenance DAG.

---

# Priority 7 — proof registry becomes executable

Each theorem anchor should point to a checker callable and a witness schema.

At minimum:

- exact-bit bound checker;
- Fano numerical checker;
- finite temporal proof replay;
- grounding-number exhaustive checker.

Certificates must fail if the registered checker cannot replay the cited witness.

---

# Priority 8 — v1.0 theorem/status paper

At v1.0, produce one consolidated paper:

**HIPG Formal Toy v1.0: What Has Actually Been Established**

Strictly split:

1. definitions;
2. finite theorems;
3. exhaustive computations;
4. empirical benchmark results;
5. conjectures;
6. known no-go boundaries.

---

# Non-negotiable constraint

A model class may shrink without becoming semantically unique.

Never replace:

$$
[\mathcal M]_{\equiv}
$$

with a representative model unless a declared grounding/identifiability criterion justifies that collapse.
