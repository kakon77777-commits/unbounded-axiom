# CCM Formal Core v1.0

## Canonical Definitions and Elementary Theorems

This document extracts the minimal formal core of Computational Composite Methodology from the longer foundational paper.

## Definition 1 — Target

A mathematical target is

$$
P\in\mathcal P.
$$

Truth is represented externally by

$$
\tau(P)\in\{0,1\}.
$$

CCM does not assume direct access to $\tau$.

## Definition 2 — Certificate Language

A certificate language is

$$
\mathcal C
=
(
D,
\Gamma,
A,
V,
\sigma,
K
).
$$

Here $D$ is an applicability domain, $\Gamma$ is a certificate space, $A$ is a search procedure, $V$ is a verifier, $\sigma$ is certificate semantics, and $K$ is a cost descriptor.

## Definition 3 — Positive Coverage

$$
\operatorname{Cov}^{+}(\mathcal C)
=
\{
P:
\exists c,\,
V(P,c)=1
\land
\sigma(c)=+
\}.
$$

## Definition 4 — Negative Coverage

$$
\operatorname{Cov}^{-}(\mathcal C)
=
\{
P:
\exists c,\,
V(P,c)=1
\land
\sigma(c)=-
\}.
$$

## Definition 5 — Total Coverage

$$
\operatorname{Cov}(\mathcal C)
=
\operatorname{Cov}^{+}(\mathcal C)
\cup
\operatorname{Cov}^{-}(\mathcal C).
$$

For library

$$
\mathfrak C,
$$

define

$$
\operatorname{Cov}(\mathfrak C)
=
\bigcup_{\mathcal C\in\mathfrak C}
\operatorname{Cov}(\mathcal C).
$$

## Definition 6 — Unresolved Region

For benchmark or research domain $\Omega$:

$$
U(\mathfrak C;\Omega)
=
\Omega
\setminus
\operatorname{Cov}(\mathfrak C).
$$

## Theorem 1 — Coverage Monotonicity

If

$$
\mathfrak C_1
\subseteq
\mathfrak C_2,
$$

then

$$
\operatorname{Cov}(\mathfrak C_1)
\subseteq
\operatorname{Cov}(\mathfrak C_2).
$$

## Corollary 1 — Unresolved Antimonotonicity

If

$$
\mathfrak C_1
\subseteq
\mathfrak C_2,
$$

then

$$
U(\mathfrak C_2;\Omega)
\subseteq
U(\mathfrak C_1;\Omega).
$$

## Definition 7 — Method Barrier

A method-barrier certificate verifies a meta-proposition restricting a method or certificate language.

It does not by itself verify

$$
P
$$

or

$$
\neg P.
$$

## Proposition 2 — Method Failure Is Not Falsity

If a sound certificate language is incomplete, then

$$
P\notin\operatorname{Cov}(\mathcal C)
$$

is compatible with

$$
\tau(P)=1.
$$

Therefore

$$
\text{search failure}
\not\Rightarrow
\text{target falsity}.
$$

## Definition 8 — Certificate-Preserving Representation Morphism

A transformation

$$
T:
R(P)\rightarrow R'(P)
$$

is certificate-preserving if accepted certificates in the transformed representation can be lifted to valid certificates of the original target.

## Theorem 3 — Composition of Representation Morphisms

The composition of certificate-preserving representation morphisms is certificate-preserving.

## Definition 9 — Terminal Router Semantics

$$
\mathcal R(P)
\in
\{
\mathrm{PROVED},
\mathrm{DISPROVED},
\mathrm{UNRESOLVED}
\}.
$$

Soundness means:

$$
\mathrm{PROVED}\Rightarrow\tau(P)=1,
$$

$$
\mathrm{DISPROVED}\Rightarrow\tau(P)=0.
$$

UNRESOLVED has no truth semantics.

## Theorem 4 — Verification Firewall

If all terminal verifiers are sound and all representation transformations are certificate-preserving, then any router that emits terminal truth judgments only after verification is sound independently of how its search and routing heuristics are chosen.

## Definition 10 — Research State

A full CCM state may be written

$$
\mathcal S_t
=
(
P,
\mathcal R_t,
\mathcal H_t,
\mathcal E_t,
\mathcal I_t,
\mathcal C_t^{+},
\mathcal C_t^{-},
\mathcal B_t,
\mathfrak C_t,
\mathcal A_t,
\widehat\Theta_t,
w_t
).
$$

## Definition 11 — State Operator

$$
\mathcal S_{t+1}
=
\Phi_i(\mathcal S_t).
$$

Operators include search, compression, representation change, certificate generation, verification, mutation, barrier extraction, and route update.

## Proposition 5 — Nonnegative Defect Decomposition

If

$$
G
=
\sum_\alpha
\lambda_\alpha D_\alpha,
$$

with

$$
\lambda_\alpha\ge0,
\qquad
D_\alpha\ge0,
$$

then

$$
G\ge0.
$$

If all active $\lambda_\alpha>0$, then $G=0$ implies every active $D_\alpha=0$.

## Definition 12 — Cost Vector

$$
K(\rho,P)
\in
\mathbb R_{\ge0}^{d}.
$$

Environment-specific scalarized cost is

$$
C_t(\rho,P)
=
\langle
w_t,
K(\rho,P)
\rangle.
$$

## Definition 13 — Marginal Coverage Gain

On finite domain $\Omega$:

$$
G_{\mathrm{coverage}}
=
\frac{
|
(
\operatorname{Cov}(\mathcal C_{\mathrm{new}})
\setminus
\operatorname{Cov}(\mathfrak C)
)
\cap\Omega
|
}{
|\Omega|
}.
$$

## Definition 14 — Routing Gain

For equal certificate libraries:

$$
G_{\mathrm{route}}
=
1-
\frac{
C(\pi_{\mathrm{adaptive}})
}{
C(\pi_{\mathrm{baseline}})
}.
$$

## Proposition 6 — Coverage and Cost Are Independent Axes

Library expansion can preserve or increase ideal coverage while increasing the cost of a naive fixed portfolio.

Hence

$$
G_{\mathrm{coverage}}
$$

and

$$
G_{\mathrm{route}}
$$

must be measured separately.

## Definition 15 — Route Regret

$$
R_\pi(P)
=
C(\pi(P),P)
-
\min_{\rho\in\mathcal R(P)}
C(\rho,P).
$$

## Definition 16 — Online Routing

$$
\pi_t
=
\Pi(
F(P_t),
\mathfrak C_t,
\widehat\Theta_t,
w_t,
\mathcal A_t
).
$$

## Definition 17 — Online Update

$$
\widehat\Theta_{t+1}
=
U(
\widehat\Theta_t,
O_t
).
$$

## Definition 18 — Dynamic Regret

$$
R_{\mathrm{dynamic}}
=
C_T(\pi)
-
C_T(\pi^*_{\mathrm{dynamic}}).
$$

## Definition 19 — Switch Latency

$$
L_{\mathrm{switch}}
$$

is the number of relevant target events between a genuine route-preference change and adoption of the new preferred route.

## Definition 20 — CCM Performance State

$$
\boxed{
\mathcal G_t
=
(
G_{\mathrm{coverage}},
G_{\mathrm{route}},
R_{\mathrm{static}},
R_{\mathrm{dynamic}},
L_{\mathrm{switch}},
E_{\mathrm{sound}}
).
}
$$

## Canonical Methodological Separation

CCM requires that the following remain distinct:

$$
\boxed{
\text{truth}
\neq
\text{coverage}
\neq
\text{search success}
\neq
\text{verification}
\neq
\text{cost}.
}
$$

## Canonical Closure Rule

$$
\boxed{
\text{heuristic search may propose;
verified certificates close}.
}
$$
