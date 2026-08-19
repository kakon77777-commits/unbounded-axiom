# HIPG Formal Toy Model v0.3

**Framework**: HIPG — Heterogeneous Intelligence Protocol Generation  
**Phase**: A — Formal Toy Model / Active Constructor  
**Version**: v0.3  
**Date**: 2026-08-14  
**Status**: Executable finite research scaffold

---

# 0. What Changed

v0.2 could repair a quotient after the evaluator exposed a counterexample and a distinguishing probe.

v0.3 removes that direct probe-selection oracle.

The constructor now chooses a probe by estimated conditional information gain:

$$
\boxed{
p^\ast
=
\arg\max_{p\notin P_t}
\widehat I(p;Y_T\mid P_t).
}
$$

The environment still provides finite task feedback and lets the constructor query available probe channels. This is intentionally weaker than an omniscient evaluator but stronger than a fully unsupervised setting.

The runtime also adds:

1. noisy active quotient learning;
2. finite-evidence statistical MERGE;
3. TSSH weight calibration from observed task loss;
4. $L_H\to L_F\to L_A\to L_H'$ round-trip checks;
5. direct-vs-formal path commutativity tests;
6. feasibility-point estimation;
7. a unified certificate layer.

---

# 1. Active Probe Selection

For current active probe set $P_t$ and candidate $p$, v0.3 estimates:

$$
\widehat I(p;Y_T\mid P_t).
$$

The learner samples triples:

$$
(C_t,p,Y_T),
$$

where $C_t$ is the currently observed signature.

It then chooses the candidate with maximum empirical conditional mutual information.

Therefore the update is no longer:

```text
counterexample -> evaluator says probe O -> activate O
```

but:

```text
task feedback + candidate observations
-> estimate information gain
-> select probe
-> re-partition
```

This is the first toy implementation of:

$$
\boxed{
\text{actively ask what distinction is worth learning next.}
}
$$

---

# 2. Noisy Quotient Learning

Probe values may flip with probability:

$$
p_{probe}.
$$

Task feedback labels may be corrupted with probability:

$$
p_{feedback}.
$$

For active probes, each private state is queried repeatedly and represented by majority vote.

The clean and noisy canonical cases both recover the task-sufficient partition in the supplied finite benchmark.

This is not a general consistency theorem.

---

# 3. Finite-Evidence MERGE

v0.2 MERGE was exact under active-probe equality.

v0.3 introduces a separate statistical merge decision.

For two Bernoulli task-outcome profiles with empirical means $\hat p_1,\hat p_2$:

$$
SE_{12}
=
\sqrt{
\frac{\hat p_1(1-\hat p_1)}{n}
+
\frac{\hat p_2(1-\hat p_2)}{n}
}.
$$

Define:

$$
U_{diff}
=
|\hat p_1-\hat p_2|
+zSE_{12}.
$$

Commit MERGE only if:

$$
\boxed{
U_{diff}\le\epsilon_{merge}.
}
$$

This is deliberately conservative: finite evidence must support similarity before a destructive semantic coarsening is committed.

The evidence is retained in a `MERGE_EVIDENCE` certificate.

---

# 4. TSSH Weight Calibration

Paper 04 wrote:

$$
D_T
=
w_E\delta_E+w_R\delta_R+w_J\delta_J+w_O\delta_O.
$$

Earlier toy versions supplied $w$ manually.

v0.3 includes a finite linear calibration experiment:

$$
y_k
=
\sum_c w_c\delta_{k,c}+\varepsilon_k.
$$

The learner estimates $w$ by least squares, clips negative values, and normalizes them.

The canonical case recovers a hidden evaluator weight profile within a fixed MAE tolerance.

This demonstrates only identifiability in a synthetic linear task-loss model; it does not claim real TSSH weights are linear or stationary.

---

# 5. Multi-Layer Round Trip

v0.3 implements:

$$
\boxed{
L_H\to L_F\to L_A\to L_H'.
}
$$

Task-core distance is computed on:

- action;
- target;
- permission;
- confidence.

The round-trip condition is:

$$
D_T(L_H,L_H')\le\delta_{rt}.
$$

It also compares:

$$
\tau_{FA}\circ\tau_{HF}
$$

against a direct path:

$$
\tau_{HA}.
$$

The commutativity condition is:

$$
\boxed{
D_T(
\tau_{FA}\circ\tau_{HF},
\tau_{HA}
)
\le\delta_{comm}.
}
$$

A canonical benchmark injects a direct-path permission drift (`read_only -> read_write`). The candidate is rejected and repaired from the formal contract before success.

---

# 6. Feasibility Point

Each result now carries a first empirical point:

$$
\boxed{
(D_T,C_{comm},C_{comp},C_{adapt},C_{audit},L_{latency}).
}
$$

These numbers are toy instrumentation, not theoretical minima.

The role is to make Paper 07's Protocol Feasibility Region executable enough to compare variants.

---

# 7. Unified Certificates

v0.3 standardizes top-level certificates.

Current certificate families include:

- `SUCCESS`;
- `STRUCTURAL_IMPOSSIBILITY`;
- `EXACT_BIT_BOUND`;
- `FANO_INFORMATION_BOUND`;
- `UNKNOWN_NONIDENTIFIABILITY`;
- `UNKNOWN_RESOURCE_OR_MODEL_LIMIT`;
- `MERGE_EVIDENCE`;
- `TSSH_CALIBRATION`;
- `BRIDGE_ROUNDTRIP`.

Every certificate preserves:

```text
certificate_type
status
assumptions
evidence
bounds
relaxation_options
provenance
```

---

# 8. Canonical v0.3 Claims

v0.3 supports the following deliberately narrow claims:

1. A finite constructor can choose a useful semantic probe from task feedback by empirical conditional information gain.
2. The same mechanism can survive moderate finite probe/feedback noise in the supplied canonical case.
3. Statistical MERGE can be guarded by finite-evidence confidence criteria instead of exact equality.
4. TSSH component weights can be estimated from task loss in a synthetic identifiable linear model.
5. A multi-layer bridge can reject permission drift using round-trip / commutativity contracts.
6. SUCCESS / INFEASIBLE / UNKNOWN remain distinct after these additions.

v0.3 still does **not** prove B-TSDPC.

---

# 9. Remaining Oracles

The evaluator still knows the true task state for benchmark scoring.

More importantly, the constructor still receives a task-feedback label $Y_T$ during active probe selection.

A harder v0.4 should replace rich labels with weaker signals such as:

$$
V_T\in\{0,1\}
$$

or scalar reward only.

Then active learning must discover distinctions from intervention outcomes rather than being told class identity.

---

# 10. Next Formal Target

The next theoretical/runtime target is:

$$
\boxed{
\text{Active Causal Quotient Discovery}
}
$$

where the constructor chooses both:

- which probe to observe;
- which action/intervention to execute;

using expected information gain over task outcomes.
