# DEST v0.8 — Fixed-Cost Certificate Cascade Model
## Weighted-Coverage Theorem, Exact Small-DAG Census, and Minimal Mixed-Utility Counterexamples

**Version:** v0.1  
**Date:** 2026-08-14  
**Engineering parent:** DEST Runtime v0.7-alpha  
**Status:** theorem-style mathematical submodel + executable exhaustive checks

---

## Abstract

DEST Runtime v0.7-alpha empirically separated three regimes:

1. pure certificate-cascade structure;
2. belief-conditioned evidence transfer;
3. deadline/dynamic-cost scheduling.

On its frozen holdout, sampled diminishing-return violations were:

\[
0/30000
\]

for the pure structural cascade,

\[
1963/30000
\]

after belief transfer, and

\[
20309/30000
\]

after deadline/dynamic-cost effects.

This paper asks whether the first zero-violation result reflects a genuine theorem.

The answer is **yes, but only after separating two different utilities that v0.7 had combined**.

### Pure Cascade Coverage

Let every inspection \(i\) have a fixed deterministic affected set \(A_i\), and let every affected certificate/debt target \(v\) have a fixed nonnegative weight \(w_v\). Define:

\[
\boxed{
F_{\mathrm{cov}}(S)
=
\sum_{v\in \cup_{i\in S}A_i}w_v.
}
\]

Then \(F_{\mathrm{cov}}\) is a weighted coverage function and therefore is:

\[
\boxed{
\text{normalized, monotone, and submodular}.
}
\]

For certificate DAGs, \(A_i\) may be the descendant closure of certificate \(i\). The proof does not actually require acyclicity; it requires only that each action's affected set be fixed independently of the selected set and history.

### Mixed Revoke–Release Utility

The v0.7 structural runtime additionally gave value to confirming a valid quarantined node, but removed that release value when an invalid ancestor revoked it.

That creates terms of the form:

\[
h_u(S)
=
r_u
\mathbf 1[u\in S]
\mathbf 1[S\cap B_u=\varnothing],
\]

where \(B_u\) is the set of invalid inspections whose cascade blocks the release of valid node \(u\).

This term is not universally submodular when:

\[
|B_u|\ge 2.
\]

A three-node counterexample exists.

Therefore:

\[
\boxed{
\text{Pure certificate cascade is a weighted-coverage submodular model;}
}
\]

but:

\[
\boxed{
\text{the full mixed revoke–release utility is not generally submodular.}
}
\]

The paper proves a useful sufficient condition:

\[
\boxed{
|B_u|\le1
\quad\forall u\text{ with }r_u>0
}
\]

implies that the mixed utility remains submodular, though it need not be monotone.

An exact exhaustive program accompanies this paper. It enumerates every ordered DAG up to \(n=5\), representing every finite DAG structure up to a topological relabeling, and checks the pure coverage diminishing-return inclusion property. It also searches all valid/invalid status assignments for minimal mixed-utility counterexamples.

---

# 1. Why v0.8 exists

The goal is not to claim that the complete DEST Runtime is submodular.

v0.7 already falsified that.

Instead, v0.8 asks:

> Which exact substructure generated the zero-violation empirical signal?

This is an inversion of the usual workflow:

```text
Runtime experiment
→ structural regularity
→ mathematical isolation
→ theorem
→ exact census
→ minimal counterexample to overgeneralization
```

---

# 2. Fixed Cascade Model

Let:

\[
I=\{1,\ldots,m\}
\]

be a finite inspection/action set and:

\[
U=\{1,\ldots,n\}
\]

be a finite target universe.

Each inspection \(i\in I\) has a fixed affected set:

\[
A_i\subseteq U.
\]

Each target \(u\in U\) has weight:

\[
w_u\ge0.
\]

For selected inspections \(S\subseteq I\), define:

\[
C(S)=\bigcup_{i\in S}A_i.
\]

Then:

\[
F_{\mathrm{cov}}(S)
=
\sum_{u\in C(S)}w_u.
\]

For a certificate DAG \(G=(V,E)\), one canonical choice is:

\[
I=U=V
\]

and:

\[
A_i=\operatorname{Desc}^{+}(i),
\]

the node together with every deterministic downstream certificate invalidated by the cascade.

---

# 3. Theorem 1 — Normalization

\[
\boxed{
F_{\mathrm{cov}}(\varnothing)=0.
}
\]

### Proof

\[
C(\varnothing)=\varnothing.
\]

Therefore the weighted sum over the covered set is zero. \(\square\)

---

# 4. Theorem 2 — Monotonicity

If:

\[
S\subseteq T,
\]

then:

\[
\boxed{
F_{\mathrm{cov}}(S)\le F_{\mathrm{cov}}(T).
}
\]

### Proof

Because union is monotone:

\[
\bigcup_{i\in S}A_i
\subseteq
\bigcup_{i\in T}A_i.
\]

All \(w_u\) are nonnegative, so adding covered targets cannot decrease total weight. \(\square\)

---

# 5. Theorem 3 — Submodularity

For:

\[
S\subseteq T\subseteq I,
\qquad
e\in I\setminus T,
\]

define marginal gain:

\[
\Delta(e\mid S)
=
F_{\mathrm{cov}}(S\cup\{e\})-F_{\mathrm{cov}}(S).
\]

Then:

\[
\boxed{
\Delta(e\mid S)\ge \Delta(e\mid T).
}
\]

### Proof

The newly covered targets after adding \(e\) to \(S\) are:

\[
N_S(e)
=
A_e
\setminus
\bigcup_{i\in S}A_i.
\]

Similarly:

\[
N_T(e)
=
A_e
\setminus
\bigcup_{i\in T}A_i.
\]

Since:

\[
S\subseteq T,
\]

we have:

\[
\bigcup_{i\in S}A_i
\subseteq
\bigcup_{i\in T}A_i.
\]

Hence:

\[
N_T(e)\subseteq N_S(e).
\]

Therefore:

\[
\Delta(e\mid S)
=
\sum_{u\in N_S(e)}w_u
\ge
\sum_{u\in N_T(e)}w_u
=
\Delta(e\mid T).
\]

Thus \(F_{\mathrm{cov}}\) is submodular. \(\square\)

---

# 6. Corollary — The DAG is not the source of submodularity

The proof uses only:

\[
A_i\text{ fixed}
\]

and:

\[
w_u\ge0.
\]

Therefore acyclicity is not necessary for the set-function theorem.

The DAG remains important to DEST because:

- it encodes certificate semantics;
- it gives a natural downstream closure;
- it supports revocation provenance and replay.

But the mathematical source of submodularity is:

\[
\boxed{
\text{fixed weighted set coverage}.
}
\]

---

# 7. Fixed Costs

Assign every inspection a fixed cost:

\[
c_i>0.
\]

A budget constraint is:

\[
\sum_{i\in S}c_i\le B.
\]

This changes the feasible family of sets, not the utility:

\[
F_{\mathrm{cov}}.
\]

Therefore:

\[
\boxed{
\text{fixed costs do not destroy utility submodularity}.
}
\]

They change the optimization problem from cardinality-constrained selection to a knapsack-type constraint.

For equal costs / cardinality \(k\), the classical monotone-submodular greedy result of Nemhauser, Wolsey, and Fisher applies to this model. This paper does not claim the same bound for naive cost-ratio greedy under arbitrary costs.

---

# 8. Why v0.7's full structural utility is different

v0.7 also modeled valid quarantined claims.

Let:

- \(I^-\): inspections with deterministic invalid outcomes;
- \(I^+\): inspections with deterministic valid outcomes.

Invalid inspection \(a\in I^-\) revokes a fixed closure \(A_a\).

For each valid node \(u\in I^+\), define blocker set:

\[
B_u
=
\{
a\in I^-:
u\in A_a
\}.
\]

A valid inspection \(u\) receives release value \(r_u\ge0\) only if no selected invalid blocker revokes it:

\[
\boxed{
h_u(S)
=
r_u
\mathbf1[u\in S]
\mathbf1[S\cap B_u=\varnothing].
}
\]

The mixed utility is:

\[
F_{\mathrm{mix}}(S)
=
F_{\mathrm{revocation}}(S\cap I^-)
+
\sum_{u\in I^+}h_u(S).
\]

The first term is weighted coverage and is submodular.

The second term is where the theorem can break.

---

# 9. Proposition 4 — Monotonicity is not guaranteed

Consider two inspections:

\[
a\to u,
\]

where \(a\) is invalid and \(u\) is valid.

Let:

\[
r_u=1,
\qquad
w_a=0.1.
\]

Then:

\[
F_{\mathrm{mix}}(\{u\})=1,
\]

while:

\[
F_{\mathrm{mix}}(\{a,u\})=0.1.
\]

Thus:

\[
F_{\mathrm{mix}}(\{a,u\})
<
F_{\mathrm{mix}}(\{u\}).
\]

Therefore mixed revoke–release utility need not be monotone. \(\square\)

---

# 10. Lemma 5 — A release term with zero blockers is modular

If:

\[
B_u=\varnothing,
\]

then:

\[
h_u(S)=r_u\mathbf1[u\in S].
\]

This is modular, hence submodular. \(\square\)

---

# 11. Lemma 6 — A release term with one blocker is submodular

Suppose:

\[
B_u=\{a\}.
\]

Then:

\[
h_u(S)
=
r_u\mathbf1[u\in S]\mathbf1[a\notin S].
\]

The only nonzero positive marginal is adding \(u\) before blocker \(a\) is selected.

Adding \(a\) has marginal:

\[
-r_u
\]

when \(u\) is present and zero otherwise.

For every:

\[
S\subseteq T,
\qquad
e\notin T,
\]

the marginal at \(T\) never exceeds the marginal at \(S\).

Hence \(h_u\) is submodular. \(\square\)

---

# 12. Theorem 7 — Blocker-At-Most-One Sufficient Condition

If:

\[
\boxed{
|B_u|\le1
\quad
\forall u\in I^+\text{ with }r_u>0,
}
\]

then:

\[
\boxed{
F_{\mathrm{mix}}
\text{ is submodular}.
}
\]

### Proof

The revocation term is a weighted coverage function, hence submodular.

By Lemmas 5 and 6, every release term \(h_u\) is submodular.

A finite sum of submodular functions is submodular.

Therefore \(F_{\mathrm{mix}}\) is submodular. \(\square\)

This theorem does **not** imply monotonicity.

---

# 13. Proposition 8 — Two blockers destroy the universal guarantee

Suppose a valid node \(u\) has two distinct blockers:

\[
a,b\in B_u,
\qquad
a\neq b,
\]

and:

\[
r_u>0.
\]

Consider only the release term \(h_u\).

Set:

\[
S=\{u\},
\qquad
T=\{u,b\},
\qquad
e=a.
\]

Then:

\[
\Delta_{h_u}(a\mid S)=-r_u,
\]

because adding \(a\) removes the release of \(u\).

But \(u\) is already blocked in \(T\), so:

\[
\Delta_{h_u}(a\mid T)=0.
\]

Submodularity would require:

\[
-r_u\ge0,
\]

which is false.

Thus \(h_u\) is not submodular.

Therefore if any positive-release valid node has two blockers, no universal submodularity guarantee exists for all nonnegative revocation weights: choose those revocation weights to be zero, or sufficiently small, and the violation survives. \(\square\)

---

# 14. Universal Characterization for the Mixed Model

For the model class in which revocation coverage weights may be arbitrary nonnegative values:

\[
\boxed{
F_{\mathrm{mix}}
\text{ is guaranteed submodular for every such weight assignment}
}
\]

if and only if:

\[
\boxed{
|B_u|\le1
\quad
\forall u\text{ with }r_u>0.
}
\]

The forward direction is Theorem 7.

The reverse universal statement follows from Proposition 8.

---

# 15. Minimal counterexamples

## 15.1 Non-monotonicity

Minimum ground-set size:

\[
\boxed{2}.
\]

Structure:

```text
a (invalid)
|
v
u (valid release)
```

Selecting \(u\) first produces release value.

Adding \(a\) removes it.

## 15.2 Non-submodularity

Minimum ground-set size:

\[
\boxed{3}.
\]

Structure:

```text
a (invalid) ─┐
             ├─> u (valid release)
b (invalid) ─┘
```

With:

\[
S=\{u\},
\quad
T=\{u,b\},
\quad
e=a,
\]

the marginal of \(a\) rises from negative to zero after more information/actions have already blocked \(u\).

That is increasing returns, not diminishing returns.

---

# 16. Exact Small-DAG Census

The accompanying program performs two exact censuses:

1. pure coverage: every forward-edge DAG on \(n\le5\);
2. mixed valid/invalid assignment regression: every forward-edge DAG and assignment on \(n\le4\) satisfying the tested scope.

The smaller mixed cutoff is an execution bound, not a theorem bound.

For fixed topological labels, the number of DAG edge sets is:

\[
\sum_{n=1}^{5}
2^{n(n-1)/2}
=
1+2+8+64+1024
=
1099.
\]

Every finite DAG admits a topological ordering, so every DAG structure can be relabeled into this forward-edge representation.

For pure coverage, the program checks the stronger set inclusion:

\[
N_T(e)\subseteq N_S(e)
\]

for every:

\[
S\subseteq T,
\qquad
e\notin T.
\]

This implies diminishing returns for **every nonnegative weight vector**, not merely one sampled weight assignment.

The program separately:

1. finds the minimum non-monotone mixed model;
2. finds the minimum non-submodular mixed model;
3. exhaustively checks all status assignments through \(n\le4\) satisfying \( |B_u|\le1 \) with deterministic positive regression weights.

The theorem for arbitrary nonnegative weights is analytic; the mixed census is a regression companion rather than its proof.


## 16.1 Exact census result

The completed executable census reports:

### Pure cascade coverage

- ordered DAGs through $n\le5$: **1099**;
- exact $S\subseteq T,e\notin T$ new-coverage inclusion checks: **421861**;
- violations: **0**.

### Full mixed model at $n\le4$

Using fixed positive regression weights

$$
w_{\mathrm{invalid}}=0.1,
\qquad
r_{\mathrm{release}}=1.0,
$$

the census contains **1098** complete DAG/status models.

Among them:

- **537** are non-monotone;
- **160** are non-submodular;
- exactly **160** contain at least one positive-release valid node with two or more invalid blockers;
- all **160/160** of those models are non-submodular under this fixed regression weight assignment.

### Blocker-at-most-one regression region

The $n\le4$ census contains **938** models satisfying $|B_u|\le1$ for every valid release node.
Observed submodularity violations: **0/938**.

This computational result is consistent with Theorem 7. The proof, not the census, carries the arbitrary-weight claim.

### Minimal exact witnesses

The first non-monotone model has two nodes:

```text
0 invalid -> 1 valid
```

with $F(\{1\})=1$ and $F(\{0,1\})=0.1$.

The first non-submodular model has three nodes:

```text
0 invalid -> 1 invalid -> 2 valid
```

where valid node 2 has blockers $B_2=\{0,1\}$.
The exact witness is

$$
S=\{2\},\qquad T=\{0,2\},\qquad e=1,
$$

with

$$
\Delta(e\mid S)=-0.9 < 0 = \Delta(e\mid T).
$$

Thus even a single chain, rather than a branching fork, is enough to destroy the universal mixed-utility guarantee.

---

# 17. Belief Transfer

Once inspection results update another debt's estimated probability:

\[
p_j
\to
p_j',
\]

the objective becomes history-conditioned.

It is no longer represented by one fixed set function:

\[
F:2^I\to\mathbb R.
\]

Classical submodularity is therefore no longer automatically the right object.

One may ask whether an adaptive-submodular model exists, but only after specifying:

- outcome space;
- partial realizations;
- conditional expected marginal values;
- prior;
- observation model.

v0.7 empirically observed nonzero diminishing-return violations after belief transfer.

Therefore DEST currently has no general adaptive-submodularity theorem.

---

# 18. Deadlines and Dynamic Costs

If the score of inspection \(i\) depends on clock time:

\[
Score_i(t),
\]

then the same selected set can have different value depending on ordering and time.

Likewise:

\[
c_i=c_i(t)
\]

changes the feasible continuation as time evolves.

Thus the full runtime is not one static set-function maximization problem unless time is explicitly encoded into the state/ground elements.

v0.7's high violation rate in the deadline/dynamic-cost diagnostic is therefore not surprising: the fixed-set diminishing-return law is being tested outside its natural static scope.

---

# 19. What v0.8 proves

\[
\boxed{
\textbf{Theorem A:}
\quad
\text{Fixed deterministic certificate cascade coverage with nonnegative target weights is normalized, monotone, and submodular.}
}
\]

\[
\boxed{
\textbf{Theorem B:}
\quad
\text{Fixed inspection costs preserve utility submodularity.}
}
\]

\[
\boxed{
\textbf{Theorem C:}
\quad
|B_u|\le1\ \forall u
\text{ is sufficient for mixed revoke–release submodularity.}
}
\]

\[
\boxed{
\textbf{Counterexample D:}
\quad
\text{mixed revoke–release utility is not monotone in general.}
}
\]

\[
\boxed{
\textbf{Counterexample E:}
\quad
\text{two blockers of one positive-release valid node are enough to destroy the universal submodularity guarantee.}
}
\]

---

# 20. What v0.8 does not prove

It does not prove:

- full DEST is submodular;
- full DEST is adaptive submodular;
- v0.7 scheduler has a greedy approximation guarantee;
- deadline urgency preserves submodularity;
- probability calibration preserves adaptive diminishing returns;
- dynamic costs preserve an approximation factor;
- branch interactions can always be reduced to coverage;
- quarantine release is harmless to monotonicity.

---

# 21. External alignment

Coverage functions are a standard special case of submodular functions.

The classical Nemhauser–Wolsey–Fisher analysis studies greedy maximization of nondecreasing submodular set functions under a cardinality constraint and obtains the familiar limiting \(1-1/e\) guarantee.

Adaptive submodularity generalizes diminishing returns to partial observations, but its guarantees require its structural assumptions to hold.

DEST v0.8 uses these theories only where their hypotheses match the isolated submodel.

---

# 22. Engineering consequence

The Runtime should stop asking:

> Is DEST submodular?

The correct question is:

> Which utility components are submodular, which are not, and which runtime transitions move us between those classes?

This suggests a future scheduler can route by certified structural regime:

```text
PURE_CASCADE_COVERAGE
  → monotone submodular backend allowed

MIXED_RELEASE, blocker_count <= 1
  → submodular but possibly non-monotone backend

MIXED_RELEASE, blocker_count >= 2
  → no universal submodularity guarantee

BELIEF_UPDATE
  → adaptive diagnostic required

DEADLINE / DYNAMIC_COST
  → state/time-dependent optimization backend
```

---

# 23. Final conclusion

The empirical zero-violation signal from v0.7 was real, but its correct interpretation was narrower than:

\[
\text{DEST is submodular}.
\]

What survives mathematical isolation is:

\[
\boxed{
\text{fixed deterministic certificate cascade}
=
\text{weighted coverage}.
}
\]

And therefore:

\[
\boxed{
\text{normalized}
+
\text{monotone}
+
\text{submodular}.
}
\]

The first principled break occurs not merely because "AI is dynamic", but already in a three-node deterministic mixed utility:

\[
\boxed{
\text{two revocation blockers}
+
\text{one positive release value}.
}
\]

That gives DEST a sharper mathematical boundary:

\[
\boxed{
\text{cascade coverage is the theorem region;}
}
\]

\[
\boxed{
\text{release interaction is the first deterministic counterexample region;}
}
\]

\[
\boxed{
\text{belief, deadlines, and dynamic costs belong to still richer state-dependent regimes.}
}
\]

This is the first point in the Runtime engineering line where an empirical regularity has been compressed into a theorem and then deliberately surrounded by exact counterexamples.
