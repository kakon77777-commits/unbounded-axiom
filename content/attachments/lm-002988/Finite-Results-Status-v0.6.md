# HIPG v0.6 — Finite Results and Theorem-Style Status Note

**Version**: v0.6  
**Date**: 2026-08-14  
**Purpose**: Separate finite mathematical consequences, executable propositions, empirical benchmark results, and still-open conjectures.

---

# 1. Lemma — operator-subset sufficiency in the canonical task family

Let the operator superset be:

$$
\mathcal O_0=\{\land,\lor,\oplus\}.
$$

For the finite training task family:

$$
\mathfrak T
=
\{
E\oplus J,
(E\oplus J)\land O,
(E\oplus J)\oplus O
\},
$$

the subset:

$$
\boxed{
\mathcal O^\ast=\{\land,\oplus\}
}
$$

is sufficient to represent all tasks under the v0.6 bounded Boolean grammar.

The operator $\lor$ is not required for exact representation of this finite family.

This is a finite library fact, not a claim that $\lor$ is generally unnecessary.

---

# 2. Executable proposition — reusable macro lowers finite description length

The three learned expressions contain:

$$
M_0:=E\oplus J
$$

three times.

Using the v0.6 MDL accounting:

$$
L_{\mathrm{before}}=13,
$$

$$
L_{\mathrm{after}}=10.
$$

For the novel task:

$$
(E\oplus J)\land\neg O,
$$

plain MDL is:

$$
6,
$$

and macro-based MDL is:

$$
4.
$$

Therefore the learned macro strictly reduces description length in this finite corpus.

---

# 3. Executable proposition — learned dynamics recover the canonical horizon-2 quotient

Given the canonical hidden deterministic transition system, sampled seven times per state-action pair with observation noise 0.08, the seeded v0.6 experiment recovers the exact evaluator transition table.

Using the learned model:

$$
\widehat P=P^\ast
$$

for this run, and therefore:

$$
\widehat{\mathcal Q}_{T,2}
=
\mathcal Q_{T,2}^\ast
=
\{
\{\text{goal}\},
\{s_0\},
\{s_1\},
\{\text{trap}\}
\}.
$$

This is a seeded finite empirical proposition, not a stochastic convergence theorem.

---

# 4. Proposition — behavior does not identify semantic decomposition

Let:

$$
\rho
$$

be a partner adapter and:

$$
h
$$

a task rule.

Define composite surface behavior:

$$
B_{\rho,h}:\{0,1\}^3\to\{0,1\}.
$$

In the canonical v0.6 joint benchmark, the exact observed surface behavior admits:

$$
\boxed{12}
$$

distinct pairs:

$$
(\rho_i,h_i)
$$

with identical:

$$
B_{\rho_i,h_i}.
$$

Hence exact behavioral prediction alone is insufficient to identify a unique latent semantic decomposition in this model.

The correct top-level state is therefore:

```text
UNKNOWN_NONIDENTIFIABLE
```

rather than semantic `SUCCESS`.

---

# 5. Proposition — canonical intervention set breaks that finite symmetry

Add three interventions with known semantics:

$$
\operatorname{TOGGLE}_E,
\quad
\operatorname{TOGGLE}_J,
\quad
\operatorname{TOGGLE}_O.
$$

For the canonical hidden adapter, their observed surface changes reduce the 48 generated adapter candidates to exactly one:

$$
\boxed{
p_0=\neg O,
p_1=E,
p_2=J.
}
$$

Conditioned on this adapter, the bounded task library contains exactly one expression matching the complete binary-reward surface behavior:

$$
\boxed{
(J\land O)\oplus E.
}
$$

Thus the intervention set identifies the canonical pair inside this finite hypothesis family.

This is not a general identifiability theorem for latent ontologies.

---

# 6. Solver result — minimum L1 repair under the linear contract

The v0.6 arithmetic bridge solves:

$$
\min
\|x-x_0\|_1
$$

subject to:

$$
\text{confidence}\ge0.70,
$$

$$
\text{latency}\le5,
$$

$$
\text{error}\le0.10,
$$

$$
\text{confidence}-\text{error}\ge0.65.
$$

For:

$$
x_0=(0.60,8.0,0.15),
$$

SciPy HiGHS returns a feasible optimum with objective:

$$
\boxed{3.2}
$$

and one optimal repaired point:

$$
\boxed{
(0.70,5.0,0.05).
}
$$

---

# 7. Empirical proposition — learned diagnostic routing

A decision tree trained on synthetic finite HIPG diagnostic examples reaches:

$$
\boxed{0.977}
$$

held-out classification accuracy over:

```text
STRUCTURAL
INFORMATION
NONIDENTIFIABLE
RESOURCE
REPAIRABLE
```

and correctly classifies all five canonical probe cases.

This result demonstrates learnability in the finite generator distribution only.

---

# 8. Empirical proposition — cost-aware experiment selection

Under the v0.6 cost-aware regret:

$$
R_T
=
\sum_t
\left[
\Delta V_t
+
\lambda_E C_{\mathrm{experiment},t}
+
\lambda_M C_{\mathrm{model},t}
\right],
$$

100 seeded runs yield:

$$
R_{\mathrm{COST\text{-}AWARE}}=4.1150,
$$

$$
R_{\mathrm{ACTIVE\ EIG}}=4.7644,
$$

$$
R_{\mathrm{RANDOM}}=4.7586,
$$

$$
R_{\mathrm{BLIND}}=4.7586.
$$

Thus cost-aware HIPG has the lowest mean total regret on this finite benchmark.

No universal regret dominance is claimed.

---

# 9. Preserved invariants

v0.6 continues to enforce:

$$
\boxed{
\text{SUCCESS}
\neq
\text{INFEASIBLE}
\neq
\text{UNKNOWN}.
}
$$

It additionally enforces:

$$
\boxed{
\text{perfect behavioral prediction}
\not\Rightarrow
\text{unique semantic identification}.
}
$$

---

# 10. Open conjectural step

The next unresolved frontier is no longer merely expression synthesis.

It is joint construction of:

$$
\boxed{
(\mathcal G,
\widehat P,
\widehat O,
\rho,
\mathcal Q_T,
\Pi)
}
$$

from bounded interaction.

That is: grammar, dynamics, observation model, partner mapping, task quotient and protocol must eventually become mutually inferred rather than separately supplied modules.
