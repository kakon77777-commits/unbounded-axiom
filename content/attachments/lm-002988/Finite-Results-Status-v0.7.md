# HIPG Finite Results v0.7 — Theorem-Style Status Note

**Version**: v0.7  
**Date**: 2026-08-14

---

## A. Derived-operator MDL break-even — elementary result

Let a repeated program fragment have base cost $c$, derived call cost $k<c$, definition cost $d$, and occur $n$ times.

$$
L_0=nc,\qquad L_1=d+nk.
$$

Therefore

$$
\boxed{L_1<L_0\iff n(c-k)>d.}
$$

**Proof.** Rearrangement of $d+nk<nc$. $\square$

Canonical instance:

$$
n=12,\quad c=5,\quad k=4,\quad d=8,
$$

so $12(5-4)>8$ and exact MDL saving is **4**.

---

## B. Finite equivalence-class intervention gain — elementary result

Let the current latent-model equivalence class contain $N$ uniformly weighted models. An intervention partitions it into deterministic outcome blocks $B_1,\ldots,B_m$.

$$
H(M)=\log_2N,
$$

$$
\mathbb E[H(M\mid a)]=\sum_j\frac{|B_j|}{N}\log_2|B_j|.
$$

Thus

$$
\boxed{IG(a)=\log_2N-\sum_j\frac{|B_j|}{N}\log_2|B_j|.}
$$

The canonical first intervention partitions 12 models as $(2,2,2,2,4)$, giving $2.251629$ bits. The second intervention partitions the remaining four models into four singletons, giving $2$ bits and a unique model.

This is exact conditional on the supplied intervention model.

---

## C. Active dynamics — empirical executable result

Clean canonical mean experiment count:

$$
32.0<62.0.
$$

Noisy canonical mean:

$$
35.33<90.13.
$$

No general active-learning optimality theorem is claimed.

---

## D. Observation-model learning — empirical executable result

Mean belief L1 error is

$$
\boxed{0.041336}
$$

and the learned belief policy matches the evaluator policy on the canonical queries. Reset-state identity remains supplied.

---

## E. OOD diagnosis — selective empirical result

Coverage is `0.7917`, selective accuracy is `1.0000`, and the runtime has a first-class `UNKNOWN_DIAGNOSIS` output for off-support cases.

---

## F. Mixed formal bridge — executable solver result

The canonical invalid candidate is rejected by both the discrete permission fragment and the arithmetic contract fragment. After repair it is accepted by both. This does not imply general program verification.

---

## G. Meta-regret — exact benchmark accounting

$$
R_{baseline}=140.0,\qquad R_{HIPG}=112.0,\qquad \Delta R=28.0.
$$

The result depends on the explicit benchmark cost model.

---

# Status boundary

v0.7 supplies finite examples of derived operator proposal, posterior-guided dynamics experiments, learned observation models, latent equivalence classes, active class splitting, selective OOD diagnosis, mixed solver validation, and cross-task amortization.

It does **not** prove B-TSDPC, general grammar induction, general causal discovery, or general semantic identifiability.
