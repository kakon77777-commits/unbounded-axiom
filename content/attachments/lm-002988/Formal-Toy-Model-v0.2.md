# HIPG Formal Toy Model v0.2

**Framework**: HIPG — Heterogeneous Intelligence Protocol Generation  
**Phase**: A — Formal Toy Model  
**Version**: v0.2  
**Date**: 2026-08-14  
**Status**: Executable finite model / benchmark scaffold

---

# 0. Goal

v0.1 proved only an engineering fact: the HIPG vocabulary can be instantiated as a finite executable state machine without collapsing `SUCCESS`, `INFEASIBLE`, and `UNKNOWN`.

v0.2 strengthens the toy model in five directions:

1. **The task quotient is inferred from probes instead of being supplied as a class count to the learner.**
2. `MERGE` is added, so the quotient can move in both directions:
   $$
   \text{SPLIT}\rightleftarrows\text{MERGE}.
   $$
3. Approximate TSSH is measured by a weighted component distortion:
   $$
   D_T=w_E\delta_E+w_R\delta_R+w_J\delta_J+w_O\delta_O.
   $$
4. A noisy finite channel is compared against a Fano-style lower bound.
5. The first executable multi-layer bridge is added:
   $$
   L_A\leftrightarrow L_F\leftrightarrow L_E\leftrightarrow L_H,
   $$
   with provenance anchors, permission/uncertainty invariants, and a Gap Certificate.

The diagnostic branch remains first-class:

```text
repairable
resource-limited
information-limited
structurally impossible
non-identifiable
bridge-contract violation
unknown
```

---

# 1. Benchmark truth vs learner-visible state

A benchmark case contains a hidden **full task signature** for each private state:

$$
\sigma_T(x)=(E,R,J,O).
$$

The evaluator may inspect the full signature. The learner initially receives only a subset of probes, for example:

$$
P_0=\{E,R\}.
$$

The learner's current equivalence relation is:

$$
x\sim_t y
\iff
\sigma_T(x)|_{P_t}=\sigma_T(y)|_{P_t}.
$$

Therefore its estimated quotient is:

$$
\boxed{
\widehat{\mathcal Q}_{T,t}=X/\sim_t.
}
$$

The benchmark's true quotient is induced by the full task signature:

$$
\boxed{
\mathcal Q_T^\ast=X/\sim_T.
}
$$

The learner is never handed the integer $|\mathcal Q_T^\ast|$ as an adaptation hint.

---

# 2. MERGE by quotient inference

v0.2 starts from the maximally fine singleton partition.

If two singleton/classes have the same active probe signature, they are merged:

$$
C_i,C_j\mapsto C_{ij}.
$$

This is not a semantic oracle. It is exactly the current observable equivalence relation under $P_t$.

---

# 3. Counterexample-driven SPLIT

If a current estimated quotient class contains two states with different full task signatures, the evaluator can produce a counterexample pair:

$$
x,y\in C,
\qquad
\sigma_T(x)\neq\sigma_T(y).
$$

The learner searches the available but inactive probes for one that distinguishes the pair.

If it finds probe $p$:

$$
\sigma_p(x)\neq\sigma_p(y),
$$

then:

$$
P_{t+1}=P_t\cup\{p\}.
$$

The quotient is re-inferred. This is recorded as a `SPLIT` operation.

If no available probe can distinguish the counterexample, the runtime does **not** invent a symbol and declare victory. It returns an unresolved diagnosis.

---

# 4. Approximate TSSH

The task core in v0.2 is:

$$
\mathcal K_T=\{E,R,J,O\}.
$$

For each component $k$:

$$
\delta_k
=
\frac{1}{|X|}
\sum_{x\in X}
\mathbf 1[
\widehat\sigma_k(x)\neq\sigma_k(x)
].
$$

Then:

$$
\boxed{
D_T
=
w_E\delta_E+w_R\delta_R+w_J\delta_J+w_O\delta_O.
}
$$

The default weights are uniform, but benchmark cases can override them.

This is a finite operational proxy for Paper 04's $\delta$-TSSH. It is not claimed to be the unique semantic metric.

---

# 5. Exact quotient cardinality lower bound

The evaluator derives the number of exact task classes from the full signatures:

$$
m=|\{\sigma_T(x):x\in X\}|.
$$

If an exact one-shot protocol has only $b$ binary channel bits, then:

$$
\boxed{
b\ge\lceil\log_2m\rceil.
}
$$

The learner is not told $m$ for quotient repair. The evaluator uses it only for impossibility diagnosis.

---

# 6. Noisy channel and Fano comparison

For the canonical noisy benchmark:

- $m=8$ equiprobable task classes;
- each class is mapped bijectively to a 3-bit code;
- each bit passes through a binary symmetric channel with flip probability $p=0.2$.

The analytic direct-decoding error is:

$$
P_e^{\mathrm{exact}}
=1-(1-p)^3
=0.488.
$$

For uniform 3-bit inputs, the channel mutual information is:

$$
I(Y;M)=3[1-h_2(p)].
$$

The coarse Fano lower bound is:

$$
\boxed{
P_e
\ge
\max\left(0,
1-\frac{I(Y;M)+1}{\log_2m}
\right).
}
$$

v0.2 computes:

- analytic error;
- Monte-Carlo empirical error;
- empirical mutual information;
- Fano lower bound;
- whether the target error lies below the lower bound.

A target below the Fano lower bound is classified as an **information-limited infeasible target**, not as a repair problem.

---

# 7. Multi-layer bridge v0.2

The first executable bridge uses four structured layers.

## $L_A$ — native

A machine-operational artifact contains:

```json
{
  "action": "inspect_file",
  "target": "paper.md",
  "permission": "read_only",
  "confidence": 0.63,
  "evidence": ["trace:17"],
  "native_only": {"cluster": "z17"}
}
```

## $L_F$ — formal contract

The formal layer preserves:

- action;
- target;
- permission;
- a confidence interval;
- evidence anchors;
- source hash.

## $L_E$ — expert layer

The expert layer exposes assumptions, operational scope, confidence, and evidence references.

## $L_H$ — human layer

The human layer gives a decision-sufficient explanation while retaining:

- action/target;
- permission;
- uncertainty label;
- claim anchors.

---

# 8. Bridge invariants

The validator checks:

$$
\boxed{
\text{action fidelity}
+
\text{target fidelity}
+
\text{permission fidelity}
+
\text{uncertainty fidelity}
+
\text{provenance coverage}.
}
$$

A bridge candidate with permission drift is repaired before commit when the source contract is available.

---

# 9. Gap Certificate

Not every native detail is required to appear in $L_H$.

If an untranslated field is outside the benchmark task core, v0.2 emits:

```json
{
  "type": "GAP_CERTIFICATE",
  "untranslated_region": ["native_only.cluster"],
  "known_task_impact": "none_in_current_task",
  "unknown_impact": false,
  "fallback_access": "L_A"
}
```

This means:

$$
\boxed{
\text{bridge success}\neq\text{complete humanization of }L_A.
}
$$

---

# 10. Canonical benchmark cases

v0.2 includes:

| Case | Purpose | Expected |
|---|---|---|
| `quotient_split_merge` | infer quotient, MERGE then counterexample SPLIT | `SUCCESS` |
| `legacy_remap_split` | preserve v0.1 REMAP/SPLIT behavior | `SUCCESS` |
| `zero_channel` | structural no-channel obstruction | `INFEASIBLE_STRUCTURAL` |
| `insufficient_bits` | exact quotient cardinality lower bound | `INFEASIBLE_INFORMATION_BOUND` |
| `no_feedback_ambiguous_mapping` | no discriminating feedback | `UNKNOWN_NONIDENTIFIABLE` |
| `noisy_fano_feasible` | noisy approximate task above lower bound | `SUCCESS` |
| `noisy_fano_too_strict` | target error below Fano lower bound | `INFEASIBLE_INFORMATION_BOUND` |
| `bridge_permission_repair` | detect/repair permission drift + provenance + gap cert | `SUCCESS` |
| `adaptation_budget_exhausted` | repairable in principle but budget too small | `UNKNOWN_RESOURCE_LIMIT` |

---

# 11. v0.2 claims and non-claims

## What is now executable

- inferred finite task quotient from probe signatures;
- MERGE and counterexample-driven SPLIT;
- legacy REMAP / ROLLBACK;
- approximate TSSH metric;
- exact bit lower bound;
- noisy-channel empirical Fano comparison;
- first four-layer bridge;
- provenance anchors;
- Gap Certificate;
- bridge permission repair;
- mixed impossibility-aware diagnostics.

## What is not proved

- B-TSDPC;
- universal quotient discovery;
- optimal probe acquisition;
- universal semantic distance;
- universal bridge correctness;
- Fano as a complete semantic converse;
- general program equivalence;
- FLP-like runtime diagnosis;
- human cognition equivalence.

---

# 12. v0.3 frontier

The next high-value step is no longer “add more cases.” It is to make the constructor itself less oracle-dependent:

1. active probe selection by information gain;
2. learned task-core weights $w_k$;
3. MERGE decisions under finite evidence rather than exact active signatures;
4. noisy quotient discovery;
5. multi-agent population / newcomer onboarding;
6. bridge round-trip and commutativity tests;
7. explicit Protocol Feasibility Region estimation;
8. lower-bound library with machine-readable certificates.
