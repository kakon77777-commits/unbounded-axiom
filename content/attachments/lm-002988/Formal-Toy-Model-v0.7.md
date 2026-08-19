# HIPG Formal Toy Model v0.7
## Derived Operators, Active Dynamics, Learned Observation Models, Latent Equivalence Classes, OOD Abstention, Mixed Solver Bridges, and Meta-Regret

**Framework**: HIPG — Heterogeneous Intelligence Protocol Generation  
**Version**: v0.7  
**Date**: 2026-08-14  
**Status**: Executable finite research scaffold

---

# 0. Main transition

v0.7 moves the finite scaffold from supplied structures toward actively discovered structure:

$$
\boxed{
\text{fixed macro}
\rightarrow
\text{parameterized derived operator proposal}
}
$$

$$
\boxed{
\text{exhaustive dynamics sampling}
\rightarrow
\text{posterior-guided active experiments}
}
$$

$$
\boxed{
O(o\mid x)\text{ given}
\rightarrow
\widehat O(o\mid x)\text{ learned}
}
$$

$$
\boxed{
\text{latent point estimate}
\rightarrow
[(\rho,h)]_{\equiv}
\rightarrow
\text{active equivalence-class split}
}
$$

It also adds selective OOD diagnosis, a mixed SAT+LP bridge, and meta-regret across task streams.

---

# 1. Derived operator proposal

Across 12 independently named programs with the repeated shape

$$
((x\oplus y)\land z),
$$

the constructor abstracts variable names and proposes

$$
\boxed{D_0(p_0,p_1,p_2)=((p_0\oplus p_1)\land p_2).}
$$

Canonical support: **12**.  Corpus MDL saving: **4**.

The proposal rule is bounded: the primitive AST meta-language is still supplied. This is not universal grammar induction.

---

# 2. Active dynamics learning

For each state-action pair, v0.7 maintains a categorical Dirichlet posterior. Experiments are chosen from task-relevant start states by expected transition-entropy reduction plus a confidence term.

The hidden transition table is not given to the learner.

Clean benchmark, 30 runs:

$$
\boxed{\bar N_{active}=32.0<\bar N_{uniform}=62.0}
$$

Noisy benchmark with transition-observation noise $0.06$:

$$
\boxed{\bar N_{active}=35.33<\bar N_{uniform}=90.13}
$$

Both recover the same hidden horizon-2 task quotient in all canonical runs.

---

# 3. Learned observation model and belief quotient

v0.7 estimates

$$
\widehat O(o\mid x)
$$

from calibration interventions, then performs Bayes updates and constructs the belief-task quotient.

Mean belief L1 error:

$$
\boxed{0.041336}
$$

The learned policy preserves:

```text
red  -> A
amb  -> TIE
blue -> B
```

Remaining oracle: `RESET_h0` / `RESET_h1` reveal the calibration hidden-state identity.

---

# 4. Latent semantic equivalence class

Passive behavior leaves 12 exact `(partner adapter, task semantics)` decompositions.

v0.7 keeps the epistemic state as

$$
\boxed{[(\rho,h)]_{\equiv}}
$$

and chooses interventions by expected posterior class entropy.

Canonical trajectory:

$$
12
\xrightarrow[2.2516\text{ bits}]{TOGGLE_E}
4
\xrightarrow[2.0000\text{ bits}]{TOGGLE_J}
1.
$$

Identified finite model:

$$
\boxed{p_0=\neg O,\quad p_1=E,\quad p_2=J,\quad h=((J\land O)\oplus E).}
$$

---

# 5. OOD-aware failure diagnosis

The diagnostic layer combines:

- theorem-backed hard guards;
- a calibrated learned classifier;
- support-distance confidence degradation under shift;
- an explicit `UNKNOWN_DIAGNOSIS` abstention branch.

Canonical OOD metrics:

$$
\boxed{coverage=0.7917,\quad selective\ accuracy=1.0000,\quad abstention=0.2083}
$$

Covered-sample ECE:

$$
\boxed{0.000816}
$$

The deliberately off-support probe is abstained rather than forced into a known class.

---

# 6. Mixed discrete + arithmetic bridge

The same bridge now invokes two real installed backends:

- `sympy.logic.inference.satisfiable` for permission/scope logic;
- `scipy.optimize.linprog(method="highs")` for arithmetic constraints.

An invalid `read_only + mutation` candidate is UNSAT in the discrete fragment, while its confidence/latency/error tuple violates the arithmetic fragment.

After repair, both fragments validate. Minimum arithmetic L1 repair cost:

$$
\boxed{3.2}
$$

Each formal clause carries a SHA-256 provenance anchor.

---

# 7. Cross-task meta-regret

The canonical score includes program representation, grammar expansion, and partner adaptation:

$$
R_{meta}=\sum_T\left(C_{program,T}+\lambda_GC_G+\lambda_PC_P\right).
$$

Over 20 tasks:

$$
\boxed{R_{baseline}=140.0,\qquad R_{HIPG}=112.0}
$$

with saving

$$
\boxed{28.0}.
$$

This is exact toy accounting under the stated cost model, not a universal regret theorem.

---

# 8. Validation target

The public package contains 42 canonical benchmark cases and preserves

$$
\boxed{\text{SUCCESS}\neq\text{INFEASIBLE}\neq\text{UNKNOWN}.}
$$

Certificates require schema validity, SHA-256 lineage integrity, and semantic consistency.

---

# 9. Remaining oracles

v0.7 still receives:

1. primitive AST operators in a bounded meta-language;
2. named task-start states and reward semantics in active dynamics;
3. reset interventions that identify calibration hidden states;
4. known semantics of `TOGGLE_E/J/O` in latent-model splitting;
5. theorem-backed hard diagnostic guards;
6. a hand-selected discrete+linear formal contract family.

Accordingly, v0.7 does **not** establish general autonomous ontology induction or B-TSDPC.
