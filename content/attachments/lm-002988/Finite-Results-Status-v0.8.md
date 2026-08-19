# HIPG v0.8 — Finite Results and Theorem-Style Status Note

**Version**: v0.8  
**Date**: 2026-08-14

This note separates elementary finite results, exact computational results, empirical benchmark results, and still-open conjectures.

---

## Result 1 — Finite behavioral operator identification

For a binary Boolean operator, there are exactly:

$$
2^{2^2}=16
$$

truth tables.

If the evidence contains the output on all four binary input pairs, then any two distinct truth tables disagree on at least one observed input. Therefore exactly one truth table remains.

In the canonical benchmark the surviving table is:

$$
\boxed{0110}.
$$

This is an elementary finite identification result. It does not imply universal operator-language invention.

---

## Result 2 — Exact MDL saving in the finite behavioral benchmark

With 14 uses, baseline storage cost 4 per use, a 4-bit operator definition, and unit call cost:

$$
C_0=56,
$$

$$
C_1=18,
$$

so:

$$
\boxed{C_0-C_1=38}.
$$

This is exact under the stated toy cost model.

---

## Result 3 — Joint reward/dynamics value-quotient discovery

In a finite 64-model family, the value-aware experiment selector identifies the correct task value signature in 3 experiments, while a transition-only selector requires 4:

$$
\boxed{3<4}.
$$

This is an exact finite benchmark result for the supplied candidate family and tie-breaking rule, not a general theorem that value-aware experimentation always dominates transition-focused exploration.

---

## Result 4 — Latent-label permutation invariance

Consider an HMM with hidden state set $S$ and a permutation $\pi:S\to S$.

If initial distribution, transition matrix, and emission matrix are simultaneously relabeled by $\pi$, then every observable sequence has the same probability.

Therefore, without an external semantic grounding of hidden-state names:

$$
\boxed{
M
\equiv_{\mathrm{obs}}
\pi(M).
}
$$

This is a standard latent-label symmetry consequence.

The v0.8 finite benchmark explicitly preserves both tied models and returns:

```text
UNKNOWN_EQUIVALENCE_CLASS
```

rather than choosing an arbitrary label orientation.

---

## Result 5 — Finite intervention gauge class

The canonical raw-action benchmark starts with:

$$
12
$$

passively equivalent $(\rho,h)$ decompositions and:

$$
3!=6
$$

raw-intervention semantic permutations.

Hence:

$$
\boxed{12\times6=72}
$$

initial $(\rho,h,\iota)$ models.

Active raw interventions reduce:

$$
72\to12\to6,
$$

then every admissible single raw action has:

$$
\boxed{IG=0}.
$$

Therefore the surviving six-model class is permanently non-identifiable under that finite intervention language.

This is an exact enumeration result for the toy model.

---

## Result 6 — External grounding changes identifiability

Adding the two grounding constraints:

$$
\iota(a_1)=E,
\qquad
\iota(a_2)=J
$$

reduces the initial class to 12.

The same active splitting process yields:

$$
12\to2\to1.
$$

Thus, in this toy class:

$$
\boxed{
\text{ungrounded: non-identifiable},
\qquad
\text{grounded: identifiable}.
}
$$

This does not establish that two anchors are generally necessary or sufficient.

---

## Result 7 — Finite temporal safety counterexample

For the explicit graph:

$$
s_0\to s_1\to bad,
$$

property:

$$
AG\ \neg bad
$$

is false, with shortest BFS counterexample:

$$
\boxed{[s_0,s_1,bad]}.
$$

After deleting the unsafe edge, the repaired graph satisfies safety and has reachability witness:

$$
\boxed{[s_0,s_1,goal]}.
$$

This is exact finite graph checking.

---

## Result 8 — Operator retirement under a fixed drift cost model

Under the v0.8 20-task stream:

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
R_{\mathrm{RETIRE}}=130.
$$

Hence:

$$
\boxed{
R_{\mathrm{RETIRE}}<R_{\mathrm{NO\ RETIRE}}.
}
$$

This is exact under the stated toy cost schedule, not a universal retirement theorem.

---

# Framework-level interpretation

The strongest conceptual result of v0.8 is the executable distinction:

$$
\boxed{
\text{model fit}
\neq
\text{semantic identifiability}.
}
$$

The runtime can now recover observable structure extremely well and still terminate with a surviving semantic equivalence class.

That is a feature, not a failure.

It implements the HIPG principle:

> Do not collapse an observational gauge class merely because one representative is convenient to name.

---

# Still conjectural / open

v0.8 does not establish:

- universal behavioral operator invention;
- general causal intervention semantics discovery;
- HMM identifiability beyond the finite candidate family;
- general task-aware active model learning bounds;
- general temporal verification;
- general OOD diagnostic coverage guarantees;
- B-TSDPC.
