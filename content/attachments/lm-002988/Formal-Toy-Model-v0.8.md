# HIPG Formal Toy Model v0.8
## Unknown Intervention Semantics, Behavioral Operator Invention, Joint Reward–Dynamics Discovery, Gauge-Equivalence Preservation, Temporal Checking, and Drift-Aware Retirement

**Framework**: HIPG — Heterogeneous Intelligence Protocol Generation  
**Phase**: A — Formal Toy Model  
**Version**: v0.8  
**Date**: 2026-08-14  
**Status**: Executable finite research scaffold

---

# 0. Purpose

v0.7 already treated a latent model equivalence class as a first-class object:

$$
[(\rho,h)]_{\equiv}.
$$

But the semantics of interventions were still supplied as `TOGGLE_E/J/O`.

v0.8 extends the latent object to:

$$
\boxed{
[(\rho,h,\iota)]_{\equiv}
}
$$

where $\iota$ is the unknown mapping from raw intervention actions to latent semantic interventions.

The central change is epistemic:

> The constructor is no longer forced to choose a unique semantic decomposition when the available evidence leaves a symmetry class intact.

It may terminate with:

```text
UNKNOWN_EQUIVALENCE_CLASS
```

and return the surviving model class.

---

# 1. New v0.8 modules

v0.8 adds eight canonical benchmark families on top of the 42 v0.7 regressions.

1. behavioral residual operator invention;
2. joint reward + dynamics discovery;
3. unlabeled HMM observation-model discovery up to permutation;
4. unknown raw intervention semantics without grounding;
5. unknown raw intervention semantics with minimal external grounding;
6. diagnostic certificate bundles;
7. explicit finite-state temporal model checking;
8. drifting task-stream operator retirement.

Total canonical benchmark count:

$$
\boxed{50}.
$$

---

# 2. Behavioral operator invention

v0.7 still proposed an operator by abstracting repeated AST shape.

v0.8 introduces a second route: search a bounded finite **behavioral transformation space** rather than syntax templates.

For a binary Boolean operator, the constructor enumerates all:

$$
2^{2^2}=16
$$

truth tables.

The canonical hidden transformation has table:

$$
\boxed{0110}
$$

under input order:

$$
(0,0),(0,1),(1,0),(1,1).
$$

No semantic operator name is exposed to the learner.

After 14 residual examples, exactly one truth table remains consistent:

$$
\boxed{0110}.
$$

Held-out truth-table accuracy:

$$
\boxed{1.0}.
$$

Toy MDL accounting:

$$
C_{\text{baseline}}=14\times4=56,
$$

$$
C_{\text{derived}}=4+14=18,
$$

therefore:

$$
\boxed{\Delta_{\mathrm{MDL}}=38}.
$$

This is still **bounded finite operator invention**. The arity, Boolean domain, and 16-table search space are supplied by the researcher.

---

# 3. Joint reward + dynamics discovery

v0.7 active dynamics optimized transition uncertainty.

v0.8 introduces a finite joint candidate family:

$$
(P,R).
$$

There are 4 state-action transitions, each mapping to one of two terminal states, and two unknown terminal rewards:

$$
2^4\times2^2=64
$$

candidate models.

The relevant target is not exact model identity. It is the task value signature:

$$
\boxed{
V_T(s)=\max_a R(P(s,a)).
}
$$

The value-aware constructor chooses experiments by expected reduction in uncertainty over this value quotient.

Canonical result:

$$
\boxed{
N_{\mathrm{VALUE}}=3
<
N_{\mathrm{TRANSITION}}=4.
}
$$

Both recover the correct value signature:

$$
\boxed{(0,1)}.
$$

The learner is not given hidden $P$ or hidden $R$.

---

# 4. Unlabeled HMM discovery and permutation gauge

v0.7 learned an observation model using labeled hidden-state reset calibration.

v0.8 removes this label privilege in a finite HMM candidate benchmark.

The learner receives only an observation sequence.

It compares 32 generated two-state HMM candidates by forward likelihood.

The best likelihood has exactly two tied models related by latent-state permutation.

The transition/emission parameters are recovered exactly **up to permutation**, but semantic state identity remains unresolved:

$$
\boxed{
|[M]_{\mathrm{perm}}|=2.
}
$$

Therefore the correct status is:

```text
UNKNOWN_EQUIVALENCE_CLASS
```

rather than `SUCCESS` with an arbitrary hidden-state naming.

This demonstrates:

$$
\boxed{
\text{structural recovery}
\not\Rightarrow
\text{semantic label identifiability}.
}
$$

---

# 5. Unknown intervention semantics

The full finite latent model is now:

$$
\boxed{
(\rho,h,\iota),
}
$$

where:

- $\rho$: surface-to-canonical adapter;
- $h$: task semantic rule;
- $\iota$: raw-action-to-latent-intervention mapping.

With 12 passive $(\rho,h)$ decompositions and 6 possible intervention permutations:

$$
\boxed{12\times6=72}
$$

models are initially admissible.

The constructor is allowed only raw actions:

```text
a0
a1
a2
```

and selects the next raw action by expected equivalence-class information gain.

Canonical ungrounded trajectory:

$$
72
\xrightarrow[2.251629\ \mathrm{bits}]{a_0}
12
\xrightarrow[1\ \mathrm{bit}]{a_1}
6.
$$

After this:

$$
\max_a IG(a)=0.
$$

Hence:

$$
\boxed{
\texttt{UNKNOWN\_EQUIVALENCE\_CLASS}
}
$$

is terminal under the admissible action set.

The remaining six models form a genuine finite gauge class: raw behavioral evidence cannot distinguish their jointly permuted semantic decompositions.

---

# 6. Grounding breaks the gauge symmetry

A second benchmark adds two external grounding constraints:

$$
\iota(a_1)=E,
\qquad
\iota(a_2)=J.
$$

The constructor still chooses experiments using raw action names.

The admissible class begins at 12 models and evolves:

$$
12
\rightarrow
2
\rightarrow
1.
$$

Recovered model:

$$
\boxed{
\rho:
(p_0,p_1,p_2)=(\neg O,E,J)
}
$$

$$
\boxed{
h=(J\land O)\oplus E
}
$$

$$
\boxed{
\iota=(O,E,J)
}
$$

under raw action order $(a_0,a_1,a_2)$.

The point is not that two anchors are universally sufficient. It is that **external grounding changes identifiability**, and the runtime now represents that distinction explicitly.

---

# 7. Diagnostic certificate bundle

A diagnosis should not contain only a class label.

v0.8 adds a structured diagnostic bundle containing:

- theorem/lower-bound anchors;
- learned model likelihoods;
- OOD support score;
- calibrated confidence;
- abstention reason;
- alternative diagnoses;
- scope statement explaining the precedence of hard theorem guards.

Canonical off-support probe:

$$
P_{\mathrm{raw}}(\text{STRUCTURAL})\approx0.6684,
$$

but support score:

$$
S_{\mathrm{OOD}}\approx0.1581.
$$

Therefore calibrated confidence falls to:

$$
\approx0.1057<0.72,
$$

and the system emits:

```text
UNKNOWN_DIAGNOSIS
```

rather than laundering the highest raw classifier probability into certainty.

---

# 8. Explicit finite-state temporal model checking

The runtime still has no Z3, Lean, cvc5, or pySMT backend.

v0.8 does **not** pretend otherwise.

Instead, it adds an explicit finite-state checker for a tiny CTL-like fragment:

$$
AG\ \neg bad
$$

and:

$$
EF\ goal.
$$

Initial model:

$$
s_0\rightarrow s_1\rightarrow bad
$$

produces the concrete safety counterexample:

$$
\boxed{[s_0,s_1,bad]}.
$$

After repair, safety holds and reachability has witness:

$$
\boxed{[s_0,s_1,goal]}.
$$

This is a real finite model checker over an explicit graph, not a simulated solver label.

---

# 9. Drifting task stream and operator retirement

A cross-task library can become stale.

v0.8 compares:

1. no library;
2. static library;
3. learned library without retirement;
4. learned library with retirement.

The first 10 tasks benefit from a derived operator; the next 10 do not.

Toy meta-regrets:

$$
R_{\mathrm{NO\ LIBRARY}}=160,
$$

$$
R_{\mathrm{STATIC}}=158,
$$

$$
R_{\mathrm{NO\ RETIRE}}=138,
$$

$$
\boxed{
R_{\mathrm{RETIRE}}=130.
}
$$

So in this finite cost model:

$$
\boxed{
R_{\mathrm{RETIRE}}
<
R_{\mathrm{NO\ RETIRE}}.
}
$$

This instantiates protocol/library retirement under distribution shift.

---

# 10. Certificate v0.8

Every benchmark result is wrapped in:

```text
HIPG-CERT-0.8
```

and must pass:

$$
\boxed{
\text{JSON Schema}
+
\text{SHA-256 integrity}
+
\text{semantic consistency}.
}
$$

New semantic checks cover:

- behavioral operator uniqueness + held-out accuracy;
- value-aware reward/dynamics experiment advantage;
- explicit HMM permutation-equivalence unknown;
- raw-intervention permanent equivalence vs grounded uniqueness;
- diagnostic bundle completeness;
- temporal counterexample/witness validity;
- retirement advantage under shift.

---

# 11. Canonical validation

v0.8 preserves all v0.7 regressions and adds 8 new cases.

Expected result:

$$
\boxed{50/50\ \text{benchmarks PASS}}
$$

$$
\boxed{50/50\ \text{certificates PASS}}
$$

$$
\boxed{20/20\ \text{unit tests PASS}}.
$$

---

# 12. What v0.8 has not solved

v0.8 does **not** prove B-TSDPC.

Remaining supplied structure includes:

- Boolean operator arity and finite truth-table search domain;
- a finite 64-model reward/dynamics family;
- a finite HMM parameter grid;
- a finite adapter/task/intervention candidate class;
- external grounding constraints in the identifiable raw-action benchmark;
- explicit finite temporal state graph;
- hand-specified theorem/lower-bound anchor IDs;
- hand-designed cost model for retirement.

The important change is not oracle elimination in the absolute sense.

It is that **each remaining oracle is now more explicit, and several formerly hidden semantic assumptions have been turned into model classes, equivalence classes, or certificate fields.**
