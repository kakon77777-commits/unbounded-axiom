# HIPG v0.9 — Finite Results / Theorem-Style Status Note

**Version**: v0.9  
**Date**: 2026-08-14

---

## Result 1 — Finite intervention-kernel identification

Let $\mathcal I$ be the v0.9 behavioral intervention library after kernel deduplication, with:

$$
|\mathcal I|=32.
$$

For the four canonical interventions and the fixed seeded sample set, maximum finite-model likelihood selects an intervention with exactly the same transition kernel as the hidden intervention.

This is an **executed finite identification result**, not a statement about arbitrary stochastic operators.

---

## Result 2 — Grounding number of the $S_3$ raw-action gauge class

Let the model class be all bijections:

$$
\iota:\{a_0,a_1,a_2\}\to\{E,J,O\}.
$$

Then:

$$
\boxed{G^*=2}.
$$

### Proof

There are $3!=6$ bijections. Fixing one correct anchor, e.g. $a_0\mapsto O$, leaves the remaining two semantic labels free to swap, hence two models remain. Therefore one anchor is insufficient.

Fixing two distinct correct anchors determines the third by bijectivity. Therefore two anchors are sufficient.

Hence $G^*=2$. $\square$

---

## Result 3 — Fixed-budget active POMDP empirical proposition

In the canonical 32-model finite POMDP family, with 30 seeded runs and budget 18:

$$
\operatorname{Acc}_{\mathrm{active}}=0.80,
$$

$$
\operatorname{Acc}_{\mathrm{random}}=0.633333\ldots
$$

for recovery of the correct predictive-equivalence signature.

This is an **empirical finite proposition**. It is not a theorem that active selection always dominates random selection.

---

## Result 4 — Arity lower-family insufficiency for Boolean majority

For the complete 3-input majority truth table:

$$
\operatorname{MAJ}_3,
$$

v0.9 exhaustively checks its bounded unary and pairwise-binary families.

Best unary accuracy:

$$
0.75.
$$

Best pairwise-binary accuracy:

$$
0.75.
$$

A ternary truth table reaches:

$$
1.0.
$$

Thus, inside the tested families, unary and pairwise-binary operators are insufficient for exact representation.

---

## Result 5 — Replayable finite temporal proof objects

For a finite directed graph, the v0.9 proof checker accepts:

- a safety-counterexample path iff every edge is present and the path ends at `bad`;
- a reachability witness iff every edge is present and the path ends at `goal`;
- an inductive-invariant set iff it contains the start state, excludes `bad`, and is closed under successors.

The canonical counterexample, witness, and invariant all replay successfully; a deliberately tampered path is rejected by unit test.

---

## Result 6 — Registry-bound theorem citations

In the finite v0.9 theorem registry, a citation is accepted only if:

1. `anchor_id` exists;
2. its content hash matches;
3. requested assumptions are contained in the registered assumption set.

Canonical stale-hash, nonexistent-anchor, and assumption-mismatch citations are all rejected.

---

## Result 7 — Online retirement result

For the canonical hidden drift stream, the change point is:

$$
t^*=20
$$

but is not supplied to the detector.

The Bayesian detector retires at:

$$
t=21
$$

and obtains cost:

$$
238<267,
$$

where $267$ is no-retirement cost.

This is an executed result for one stochastic toy stream, not an optimality theorem.

---

## Result 8 — Equivalence-class honesty invariant

The public artifact for the six-model semantic gauge class explicitly stores:

```text
selection_policy = DO_NOT_CHOOSE_REPRESENTATIVE_AS_TRUTH
```

and a content hash over the class description.

Thus an unresolved finite equivalence class is represented as an epistemic object rather than collapsed into a single semantic claim.

---

# Regression status

Canonical benchmarks:

$$
\boxed{58/58\ PASS}
$$

Certificates:

$$
\boxed{58/58\ PASS}
$$

Unit tests:

$$
\boxed{36/36\ PASS}
$$

---

# Theory status

### Elementary / finite proof

- $S_3$ grounding number $G^*=2$.
- finite path/invariant proof replay conditions.

### Exhaustive finite computation

- bounded intervention-kernel identification.
- operator-family search.

### Empirical finite result

- active POMDP identification advantage.
- online drift retirement cost advantage.

### Still conjectural at HIPG scale

- B-TSDPC.
- general minimal grounding theory.
- general active causal discovery.
- unrestricted intervention-language learning.
