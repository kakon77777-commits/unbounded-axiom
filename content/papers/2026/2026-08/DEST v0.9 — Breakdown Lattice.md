# DEST v0.9 — Breakdown Lattice
## From Weighted Cascade Coverage to Mixed Release, Correlated Beliefs, Deadlines, and Dynamic Feasibility

**Version:** v0.1  
**Date:** 2026-08-14  
**Parent:** DEST v0.8 Fixed-Cost Certificate Cascade Model  
**Document type:** theorem/counterexample classification paper + executable small-model census

---

## Abstract

DEST v0.8 isolated a genuine theorem region inside the research Runtime:

\[
F_{\mathrm{cov}}(S)
=
\sum_{v\in\cup_{i\in S}A_i}w_v,
\qquad
w_v\ge0,
\]

is normalized, monotone, and submodular whenever each inspection has a fixed deterministic affected set \(A_i\).

The present paper asks what happens when the Runtime mechanisms removed by v0.8 are restored one at a time.

The answer is not one linear "submodularity disappears" story.

Different mechanisms break different mathematical assumptions:

1. **valid-release utility** can destroy monotonicity while preserving submodularity under a one-blocker condition;
2. **multiple blockers** can destroy submodularity in a three-node deterministic model;
3. **correlated belief updates** can destroy adaptive submodularity with only two stochastic items, even when the realized utility is pointwise modular;
4. **deadlines** make value depend on clock/order, so a static set function is generally the wrong object;
5. **dynamic costs** need not alter utility submodularity at all, but they destroy the fixed feasible family of a static knapsack problem.

Therefore the correct object is not a one-dimensional ladder but a **Breakdown Lattice** separating:

- utility structure;
- stochastic observation structure;
- sequence/time structure;
- feasibility/cost structure.

The paper introduces a four-state property language:

\[
\boxed{
\{\mathrm{TRUE},\mathrm{FALSE},\mathrm{CONDITIONAL},\mathrm{NOT\ APPLICABLE}\}
}
\]

to avoid confusing a genuine counterexample with a type change.

---

# 1. Property language

For every model class we track:

1. `static_set_function`;
2. `normalized`;
3. `monotone`;
4. `submodular`;
5. `adaptive_model_required`;
6. `adaptive_submodular_general`;
7. `order_time_invariant`;
8. `static_feasible_family`.

A property may be:

\[
\mathrm{TRUE}
\]

or:

\[
\mathrm{FALSE}.
\]

But two additional states are required.

### CONDITIONAL

The property may hold only under additional assumptions.

### NOT_APPLICABLE

The model is no longer the mathematical object to which the property directly applies.

Example:

> An order-sensitive deadline scheduler is not automatically a "non-submodular set function"; it may simply no longer be a set function at all.

---


# 1.1 Terminology guardrail: "Breakdown Lattice"

`Breakdown Lattice` is the engineering name of this classification program.

The canonical formal object established in v0.9 is currently:

\[
\boxed{
\text{a typed regime DAG plus a property-label map}.
}
\]

This paper does **not** claim that the eight named regimes themselves form a lattice in the strict order-theoretic sense. In particular, closure under meet and join has not been established for the named regime family.

If a later version defines a mechanism-configuration poset and proves the required meet/join structure, the word "lattice" may be promoted from project name to mathematical theorem.


# 2. The Breakdown Lattice

The main utility branch is:

```text
PURE CASCADE COVERAGE
        |
        + release value
        |
        +-- blocker count <= 1
        |      → submodular
        |      → may be non-monotone
        |
        +-- blocker count >= 2
               → no universal submodularity guarantee
```

The stochastic branch is:

```text
fixed outcome
   |
   + uncertain outcome
   |
   +-- independent modular outcomes
   |      → adaptive modular special case
   |
   +-- correlated outcomes
          → adaptive-submodularity can fail
```

The time/feasibility branch is:

```text
fixed utility + fixed cost
        |
        + deadline/time value
        |      → order/time-dependent objective
        |
        + dynamic cost
               → changing feasible family
```

The full Runtime combines all three branches.

---

# 3. Layer L0 — Pure Cascade Coverage

From v0.8:

\[
F_{\mathrm{cov}}(S)
=
\sum_{v\in\cup_{i\in S}A_i}w_v.
\]

With:

\[
w_v\ge0
\]

and fixed \(A_i\),

\[
\boxed{
F_{\mathrm{cov}}
\text{ is normalized, monotone, and submodular}.
}
\]

This is the theorem region.

---

# 4. Layer L1 — Add Valid Release

For valid quarantined node \(u\),

\[
h_u(S)
=
r_u
\mathbf1[u\in S]
\mathbf1[S\cap B_u=\varnothing].
\]

If:

\[
|B_u|\le1
\]

for every positive-release valid node, v0.8 proved the mixed utility remains submodular.

But a 2-node model already destroys monotonicity:

```text
a invalid → u valid
```

with:

\[
r_u=1,\qquad w_a=0.1.
\]

Thus:

\[
F(\{u\})=1
>
0.1
=
F(\{a,u\}).
\]

So Layer L1 is:

\[
\boxed{
\text{submodular but not generally monotone}.
}
\]

---

# 5. Layer L2 — Multiple Blockers

A positive-release valid node with:

\[
|B_u|\ge2
\]

admits a universal-weight counterexample.

The minimum deterministic witness has three nodes:

```text
0 invalid → 1 invalid → 2 valid release
```

For:

\[
S=\{2\},
\qquad
T=\{0,2\},
\qquad
e=1,
\]

v0.8 obtained:

\[
\Delta(e\mid S)=-0.9
<
0
=
\Delta(e\mid T).
\]

Therefore:

\[
\boxed{
\text{multiple blockers are the first deterministic submodularity-break region}.
}
\]

---

# 6. Layer L3 — Belief Update Requires a New Object

Suppose item outcomes are unknown.

A policy observes selected outcomes and updates beliefs about unselected items.

The relevant object is now a realization-dependent utility:

\[
f(S,\phi)
\]

and a partial realization:

\[
\psi.
\]

For an unobserved action \(e\), adaptive marginal utility is:

\[
\Delta(e\mid\psi)
=
\mathbb E[
f(\operatorname{dom}\psi\cup\{e\},\Phi)
-
f(\operatorname{dom}\psi,\Phi)
\mid
\Phi\sim\psi
].
\]

Adaptive submodularity requires:

\[
\psi\subseteq\psi'
\quad\Longrightarrow\quad
\Delta(e\mid\psi)
\ge
\Delta(e\mid\psi').
\]

---

# 7. Theorem 9 — Independent Modular Outcomes Form an Adaptive-Modular Special Case

Let each binary item \(e\) have outcome:

\[
\Phi(e)\in\{0,1\}.
\]

Define realized utility:

\[
f(S,\phi)
=
\sum_{e\in S}v_e\phi(e),
\qquad
v_e\ge0.
\]

Assume item outcomes are mutually independent.

For unobserved \(e\),

\[
\Delta(e\mid\psi)
=
v_e
P(\Phi(e)=1\mid\psi).
\]

By independence:

\[
P(\Phi(e)=1\mid\psi)
=
P(\Phi(e)=1).
\]

Hence:

\[
\boxed{
\Delta(e\mid\psi)
=
v_eP(\Phi(e)=1)
}
\]

for every compatible partial realization not already observing \(e\).

So the adaptive marginal is constant.

Therefore this model is an **adaptive modular** special case and hence adaptive submodular. \(\square\)

---

# 8. Proposition 10 — Correlation Alone Can Break Adaptive Submodularity

Two binary items \(A,B\).

Let:

\[
P(A=0,B=0)=\frac12,
\]

\[
P(A=1,B=1)=\frac12.
\]

All other outcomes have probability zero.

Use pointwise modular utility:

\[
f(S,\phi)
=
\sum_{e\in S}\phi(e).
\]

Before any observation:

\[
\Delta(B\mid\varnothing)
=
P(B=1)
=
\frac12.
\]

After observing:

\[
A=1,
\]

perfect correlation gives:

\[
P(B=1\mid A=1)=1.
\]

Thus:

\[
\Delta(B\mid A=1)=1.
\]

Therefore:

\[
\boxed{
\frac12<1
}
\]

and adaptive diminishing returns fails.

So:

\[
\boxed{
\text{pointwise modularity does not imply adaptive submodularity under correlated priors}.
}
\]

The minimum action count is two.

---

# 9. Exact Binary Prior Census

The executable census enumerates all rational two-item joint distributions with denominator:

\[
D\le8.
\]

The first violation already exists at:

\[
\boxed{D=2}.
\]

That witness is exactly:

```text
P(00)=1/2
P(11)=1/2
```

The same program separately checks a grid of independent product distributions and confirms that the modular adaptive marginal remains invariant under observing the other item.

The proof, not the grid, establishes the independent special case.

---

# 10. Layer L4 — Deadlines

Deadlines produce a different type of breakdown.

Consider two unit-time inspections:

```text
A: deadline 1, reward 1
B: deadline 2, reward 1
```

Selecting the same set:

\[
\{A,B\}
\]

in order:

\[
A\to B
\]

gives value:

\[
2.
\]

But order:

\[
B\to A
\]

gives value:

\[
1.
\]

Thus:

\[
\boxed{
\text{same selected set}
\neq
\text{same utility}.
}
\]

There is no static set function:

\[
F(\{A,B\})
\]

that represents both schedules.

Therefore the right classification is not simply:

> `submodular = false`.

It is:

\[
\boxed{
\text{static_set_function = FALSE}
}
\]

and:

\[
\boxed{
\text{submodular = NOT_APPLICABLE}
}
\]

for the full order-sensitive objective.

At a fixed time slice, a residual coverage component may remain submodular; the schedule-level problem has changed type.

---

# 11. Minimal Deadline Breaks

A single action is enough to show time dependence.

If:

\[
V(\{e\},t_0)=1
\]

but:

\[
V(\{e\},t_1)=0,
\]

one static set-function value:

\[
F(\{e\})
\]

cannot equal both.

Two actions are the minimum needed to exhibit order dependence while holding the selected set fixed.

---

# 12. Layer L5 — Dynamic Cost

Dynamic cost is yet another orthogonal breakdown.

Let budget:

\[
B=1.
\]

One inspection \(e\) has:

\[
c_e(t_0)=2,
\]

\[
c_e(t_1)=1.
\]

Then:

\[
\{e\}
\]

is infeasible at \(t_0\) and feasible at \(t_1\).

Therefore there is no one fixed feasible family:

\[
\mathcal F\subseteq2^I
\]

representing both times.

But if the underlying utility is still:

\[
F_{\mathrm{cov}},
\]

that utility remains submodular.

Hence:

\[
\boxed{
\text{dynamic cost does not necessarily break utility submodularity;}
}
\]

it breaks the **static constrained-optimization formulation**.

---

# 13. Why Deadline and Dynamic Cost Must Not Be Collapsed

Deadline value modifies:

\[
\text{objective}.
\]

Dynamic cost modifies:

\[
\text{feasibility / resource state}.
\]

The two can coexist but are mathematically distinct.

Treating both as:

> "submodularity violation"

throws away useful structure.

---

# 14. Property Matrix

The machine-readable canonical matrix uses:

```text
TRUE
FALSE
CONDITIONAL
NOT_APPLICABLE
```

The principal rows are:

| Model | Static set function | Monotone | Submodular | Adaptive-submodular general | Order/time invariant | Static feasible family |
|---|---|---|---|---|---|---|
| Pure cascade coverage | TRUE | TRUE | TRUE | N/A | TRUE | TRUE |
| Mixed release, blocker ≤1 | TRUE | FALSE | TRUE | N/A | TRUE | TRUE |
| Mixed release, multi-blocker | TRUE | FALSE | FALSE | N/A | TRUE | TRUE |
| Independent modular belief | Conditional | TRUE | TRUE | TRUE | TRUE | TRUE |
| Correlated belief update | Conditional | Conditional | Conditional | FALSE | Conditional | TRUE |
| Deadline value | FALSE | N/A | N/A | N/A | FALSE | Conditional |
| Dynamic cost only | TRUE | Conditional | Conditional | Conditional | Conditional | FALSE |
| Full Runtime | FALSE | N/A | N/A | FALSE | FALSE | FALSE |

---

# 15. Breakdown Events Are Not All the Same

We can now distinguish four kinds of transition.

## 15.1 Property loss

Example:

\[
\text{monotone}
\to
\text{non-monotone}.
\]

## 15.2 Guarantee loss

Example:

\[
|B_u|=1
\to
|B_u|=2.
\]

Some instances may remain submodular, but the universal theorem disappears.

## 15.3 Object-type change

Example:

\[
\text{set utility}
\to
\text{sequence/time utility}.
\]

## 15.4 Constraint-type change

Example:

\[
\text{fixed knapsack}
\to
\text{dynamic feasibility}.
\]

This is why the final object is a lattice rather than a scalar "complexity level".

---

# 16. Breakdown Lattice as a Runtime Router

The Runtime can now carry a structural certificate:

```yaml
optimization_regime:
  utility:
    type: PURE_CASCADE_COVERAGE
    monotone: true
    submodular: true

  stochastic:
    belief_update: false

  temporal:
    deadline_value: false

  cost:
    dynamic: false
```

and choose a backend consistent with certified structure.

Example routes:

```text
PURE_CASCADE_COVERAGE
→ monotone submodular optimizer candidate

MIXED_RELEASE + blocker<=1
→ non-monotone submodular optimizer candidate

MIXED_RELEASE + blocker>=2
→ generic combinatorial / exact / heuristic backend

CORRELATED_BELIEF_UPDATE
→ adaptive diagnostic required

DEADLINE
→ scheduling / sequence backend

DYNAMIC_COST
→ online/dynamic constrained backend
```

No route may be selected only because the word "submodular" appeared earlier in the lineage.

---

# 17. Relation to Classical Submodular Optimization

The classical static theory assumes a set function:

\[
f:2^N\to\mathbb R.
\]

Nemhauser, Wolsey, and Fisher analyze greedy approximation for nondecreasing submodular set functions under cardinality constraints.

The v0.8 pure cascade model fits this static family.

Once release interaction makes the function non-monotone, a different optimization literature is relevant.

Once stochastic observations affect future marginal values, adaptive submodularity is the relevant candidate notion — but only if its conditional diminishing-return property actually holds.

Once deadlines make order matter or costs change with time, the object is no longer the same static set-function problem.

---

# 18. Formal External Boundary

Golovin and Krause define adaptive submodularity as a diminishing-return property over partial realizations and show greedy-style guarantees when the property is satisfied.

DEST does **not** infer:

\[
\text{belief update}
\Rightarrow
\text{adaptive submodular}.
\]

Proposition 10 gives an explicit two-item counterexample.

This means correlation structure belongs inside the theorem assumptions, not in a footnote.

---

# 19. Exact Minimality Summary

\[
\boxed{
\text{Monotonicity break: 2 deterministic nodes.}
}
\]

\[
\boxed{
\text{Static submodularity break: 3 deterministic nodes.}
}
\]

\[
\boxed{
\text{Adaptive-submodularity break: 2 stochastic items.}
}
\]

\[
\boxed{
\text{Time-dependence break: 1 action + 2 clock states.}
}
\]

\[
\boxed{
\text{Order-dependence break: 2 actions.}
}
\]

\[
\boxed{
\text{Static feasible-family break: 1 action + dynamic cost.}
}
\]

---

# 20. Main conclusion

The v0.9 Breakdown Lattice replaces the vague statement:

> Dynamic features break submodularity.

with a typed statement:

\[
\boxed{
\text{release can break monotonicity;}
}
\]

\[
\boxed{
\text{multiple blockers can break static submodularity;}
}
\]

\[
\boxed{
\text{correlation can break adaptive submodularity;}
}
\]

\[
\boxed{
\text{deadlines can replace set utility with sequence/time utility;}
}
\]

\[
\boxed{
\text{dynamic cost can replace a fixed feasible family with dynamic feasibility.}
}
\]

The resulting boundary is substantially sharper than a binary "submodular / not submodular" label.

DEST therefore gains a new machine-checkable question:

> Before selecting an optimization theorem or scheduler, what mathematical regime is the current verification-debt problem actually in?

That is the purpose of the Breakdown Lattice.
