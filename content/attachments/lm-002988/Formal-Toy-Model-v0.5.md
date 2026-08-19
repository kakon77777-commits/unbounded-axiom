# HIPG Formal Toy Model v0.5
## Hypothesis Construction, Multi-Step Quotients, Learned Adapters, Semantic Certificates, Solver Bridge, and Protocol Regret

**Framework**: HIPG — Heterogeneous Intelligence Protocol Generation  
**Phase**: A — Formal Toy Model  
**Version**: v0.5  
**Date**: 2026-08-14  
**Status**: Executable finite research scaffold

---

# 0. What changed from v0.4

v0.4 still assumed a finite, hand-authored task-hypothesis family:

$$
\mathcal H=\{H_E,H_J,H_O,H_{J\oplus O}\}.
$$

v0.5 removes that assumption for its new synthesis benchmark.

The constructor now has a grammar:

$$
\boxed{
\mathcal G_{\mathrm{bool}}
=
\{
0,1,E,J,O,\neg E,\neg J,\neg O,
\land,\lor,\oplus
\}
}
$$

and generates candidate task semantics by program synthesis.

A hypothesis is scored by:

$$
\boxed{
P(h\mid H_t)
\propto
P(H_t\mid h)
e^{-\lambda\,\mathrm{MDL}(h)}.
}
$$

The runtime begins with a small description-length bound and expands the hypothesis space only after accumulated binary-reward evidence falsifies the current family.

---

# 1. New canonical result: hypothesis construction

Ground-truth task rule:

$$
Y_T
=
E\oplus(J\land O).
$$

This rule is **not** present in the initial hypothesis library.

Initial:

$$
\mathrm{MDL}_{\max}=1.
$$

The active constructor first queries informative interventions, then performs model criticism. After a contradictory binary reward eliminates the current family, it expands:

$$
1
\rightarrow
2
\rightarrow
3
\rightarrow
4
\rightarrow
5.
$$

The unique generated solution becomes:

$$
\boxed{
((J\land O)\oplus E)
}
$$

with:

$$
\mathrm{MDL}=5,
\qquad
\text{truth-table accuracy}=1.
$$

At MDL bounds 2, 3, 4, 5 the generated unique Boolean truth-table counts are:

$$
8,\;17,\;32,\;59.
$$

No task-class label is exposed to the learner. Experiment history contains only:

- state intervention;
- prediction action;
- binary reward.

---

# 2. Causal interventions now change world state

v0.4 intervention affected reward generation.

v0.5 makes state transition explicit:

$$
\boxed{
X_t
\xrightarrow{a_t}
X_{t+1}.
}
$$

For hypothesis synthesis, an experiment can execute:

```text
SET:110
```

and the runtime records:

```text
state_before
intervention
state_after
binary_reward
```

This makes observation and intervention distinct runtime objects.

---

# 3. Multi-step task quotient

v0.5 introduces a finite deterministic transition system.

The immediate-reward quotient is:

$$
\{\text{goal}\},
\qquad
\{\text{s0},\text{s1},\text{trap}\}.
$$

So:

$$
\text{s0}\sim_{T,0}\text{s1}.
$$

But under horizon-2 admissible action sequences:

$$
\operatorname{Sig}_2(\text{s0})
=
(2,2,0,0),
$$

$$
\operatorname{Sig}_2(\text{s1})
=
(0,0,2,2).
$$

Hence:

$$
\boxed{
\text{s0}\not\sim_{T,2}\text{s1}.
}
$$

The multi-step quotient becomes:

$$
\boxed{
\{
\{\text{goal}\},
\{\text{s0}\},
\{\text{s1}\},
\{\text{trap}\}
\}.
}
$$

This is the first executable move from one-step reward equivalence toward trajectory / bisimulation-like task equivalence.

---

# 4. Learned partner adapter family

v0.4 inferred among six hard-coded surface permutations.

v0.5 generates an adapter family algorithmically from:

1. all bijections between canonical and surface fields;
2. optional literal inversion on each field.

For 3 fields:

$$
3!\times2^3=48
$$

candidate adapters.

Canonical OOD adapter:

$$
\boxed{
p_0=\neg O,\qquad
p_1=E,\qquad
p_2=J.
}
$$

With 80 noisy anchor samples and bit noise $0.04$, v0.5 recovers exactly that adapter.

The family is generated from the schema and operator grammar; it is not a six-entry hand-authored list.

---

# 5. Certificate semantics

v0.4 certificate validation checked:

- JSON Schema;
- SHA-256 lineage.

v0.5 adds semantic consistency checks.

Each `HIPG-CERT-0.5` verifies:

$$
\boxed{
\text{structure}
+
\text{hash integrity}
+
\text{semantic consistency}.
}
$$

Checks include:

- status ↔ outcome-class consistency;
- feasibility coordinates stay in legal domains;
- an information-bound certificate must contain a real contradiction:
  - exact-bit: `required_bits > available_bits`, or
  - Fano: `lower_bound > target_error`;
- `SUCCESS` cannot simultaneously carry an active impossibility marker;
- counterfactual relaxations cannot mutate the original input lineage.

A deliberately inconsistent information certificate is rejected by the unit tests.

---

# 6. First actual solver-backed bridge

The v0.4 restricted contract DSL was checked by hand-written logic.

v0.5 adds a real installed solver backend:

```text
sympy.logic.inference.satisfiable
```

Contract core:

$$
\text{read\_only}
\Rightarrow
\neg\text{mutation}.
$$

Injected candidate:

$$
\text{read\_only}=1,
\qquad
\text{mutation}=1
$$

is:

$$
\boxed{\text{UNSAT}}.
$$

After repair:

$$
\text{mutation}=0,
$$

the same contract becomes:

$$
\boxed{\text{SAT}}.
$$

This is still a very small propositional fragment, but it is genuinely solver-backed.

---

# 7. Protocol regret

v0.5 compares four experiment policies on the generated MDL hypothesis library:

1. `ACTIVE_HIPG`;
2. `RANDOM`;
3. `PROBE_ONLY`;
4. `BLIND_REPAIR`.

With 100 runs and experiment budget 6, the canonical mean cumulative task regrets are:

$$
\boxed{
R_{\mathrm{ACTIVE}}=2.0000
}
$$

$$
R_{\mathrm{RANDOM}}=2.4300
$$

$$
R_{\mathrm{PROBE}}=2.5000
$$

$$
R_{\mathrm{BLIND}}=2.14125.
$$

Thus in this finite benchmark:

$$
\boxed{
R_{\mathrm{ACTIVE}}
<
\min(
R_{\mathrm{RANDOM}},
R_{\mathrm{PROBE}},
R_{\mathrm{BLIND}}
).
}
$$

This is not a universal performance theorem. It is the first executable regret comparison for HIPG experiment selection.

---

# 8. What v0.5 now instantiates

The runtime now contains executable fragments of:

$$
\boxed{
\begin{aligned}
&\text{Coupleability Gate}\\
&\rightarrow
\text{Active Experiment Selection}\\
&\rightarrow
\text{Hypothesis Construction}\\
&\rightarrow
\text{Task Quotient}\\
&\rightarrow
\text{Protocol Repair}\\
&\rightarrow
\text{Multi-Step World Transition}\\
&\rightarrow
\text{Partner Adapter Learning}\\
&\rightarrow
\text{Formal/Solver Bridge}\\
&\rightarrow
\text{Semantic Certificate Validation}\\
&\rightarrow
\text{SUCCESS / INFEASIBLE / UNKNOWN}.
\end{aligned}
}
$$

---

# 9. What remains deliberately unresolved

v0.5 does **not** prove B-TSDPC.

The following are still toy assumptions:

- Boolean feature grammar is supplied;
- maximum grammar complexity is finite;
- hypothesis synthesis is over a tiny state space;
- multi-step quotient is computed exactly from known transition tables;
- adapter anchors expose canonical feature values;
- SAT fragment is propositional;
- no adversarial strategic partner;
- no continuous state;
- no large population protocol;
- no learned verifier;
- no general theorem prover.

---

# 10. v0.5 research claim

The strongest justified claim is:

$$
\boxed{
\text{HIPG can move from selecting among hand-authored hypotheses
to constructing finite task hypotheses from evidence,
while preserving explicit INFEASIBLE and UNKNOWN branches.}
}
$$

The next difficult question is no longer only:

> Which hypothesis is correct?

It becomes:

> **Who chooses the hypothesis grammar, state abstraction, intervention vocabulary, and verifier itself?**
