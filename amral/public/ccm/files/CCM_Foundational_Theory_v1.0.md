# Computational Composite Methodology

## Certificate Coverage, Representation Routing, and Adaptive Control of Mathematical Research

Version: v1.0  
Status: Foundational theory draft  
Scope: General mathematical methodology, extracted from CCM Benchmarks 01--13

## Abstract

Computational Composite Methodology (CCM) is a certificate-oriented methodology for organizing mathematical research across heterogeneous computational, symbolic, analytic, combinatorial, and formal methods. Its central claim is methodological rather than ontological: a mathematical research process can be represented as a changing state in which multiple representations, search operators, certificate languages, barriers, cost models, and route histories interact.

CCM separates four notions that are often conflated:

$$
\text{truth},
\qquad
\text{method coverage},
\qquad
\text{search success},
\qquad
\text{verification}.
$$

A method may be sound but incomplete. A search procedure may fail without showing that the target is false or even that no certificate exists in the chosen language. A verified method barrier can exclude a route without excluding the theorem. Conversely, a heuristic or AI-generated route may be logically safe if terminal closure is delegated to sound certificate verifiers and every representation transition preserves certificate semantics.

The foundational objects of CCM are: targets, representations, operators, certificate languages, coverage domains, barrier certificates, research states, route policies, and vector-valued computational costs. The theory yields several elementary but useful structural results: soundness of certificate-gated routing, monotonicity of ideal library coverage under certificate-language expansion, antimonotonicity of the unresolved region, sound composition of certificate-preserving representation changes, and a formal separation between coverage gain and routing gain. It also introduces static and dynamic route regret for cost-aware and online mathematical method selection.

Benchmarks 01--13 are treated here as empirical witnesses rather than as the theory itself. They range across extremal graph theory, numerical semigroups, recurrence, SAT, matrix identities, linear-programming duality, Farkas separation, convexity, polynomial nonnegativity, certificate-library routing, cost-aware selection, and online nonstationarity. Their role is to motivate and stress-test the abstract CCM framework.

CCM does not claim that every mathematical truth admits a finite certificate in the current library, that every certificate search is decidable, or that composite routing is universally superior to expert mathematics. Its purpose is to make method coverage, proof artifacts, failed routes, representation changes, and research-control decisions explicit enough to be measured, verified, accumulated, and improved.

## 1. Motivation

Mathematical research with computation is often described in a linear form:

$$
\text{conjecture}
\rightarrow
\text{computation}
\rightarrow
\text{proof}.
$$

This is too narrow for modern research practice.

A realistic process may instead contain:

$$
\text{enumeration},
\quad
\text{symbolic algebra},
\quad
\text{optimization},
\quad
\text{counterexample search},
\quad
\text{SAT/SMT},
\quad
\text{formal proof},
\quad
\text{numerical exploration},
\quad
\text{representation change},
\quad
\text{literature constraints},
\quad
\text{AI-generated hypotheses}.
$$

The central difficulty is not only whether a particular method can solve the target. It is also:

1. which representation should be used;
2. which certificate language can close the target;
3. whether a failed route is a theorem failure or merely a coverage failure;
4. whether a counterexample invalidates a theorem or only an intermediate hypothesis;
5. whether multiple successful routes have different computational costs;
6. whether method costs and target distributions change over time;
7. how verified artifacts should alter the next research state.

CCM treats these questions as part of mathematics methodology itself.

Its high-level architecture is

$$
\boxed{
\text{target}
\rightarrow
\text{representations}
\rightarrow
\text{certificate search}
\rightarrow
\text{verification / barrier}
\rightarrow
\text{state update}
\rightarrow
\text{route selection}.
}
$$

The process may iterate many times before a terminal certificate is produced.

## 2. Position Relative to Existing Traditions

CCM sits at the intersection of several established traditions.

Experimental mathematics studies computation as an active instrument for generating examples, detecting patterns, testing conjectures, and supporting discovery [R1]. Algorithm selection studies how features of a problem instance can guide the selection of an algorithm under a performance criterion [R2]. Portfolio systems such as SATzilla make this operational for families of solvers [R3]. Online algorithm selection extends the problem to sequential environments in which performance models are learned while solving instances [R4], and nonstationary online learning provides regret notions for changing environments [R5].

Proof complexity and proof-system theory distinguish proof languages and their efficiencies [R6]. Foundational proof certificate work explicitly separates proof production from proof checking and seeks a common checking architecture for heterogeneous proof evidence [R7]. Counterexample-guided abstraction refinement uses counterexamples to refine a computational state rather than treating every failed abstraction as terminal [R8]. Sum-of-squares and semidefinite methods provide important examples of sound but non-universal certificate languages for polynomial nonnegativity [R9].

CCM does not claim that these individual ideas are new. Its proposed unit of analysis is different: the mathematical research state that simultaneously contains representations, certificate coverage, method barriers, route costs, and adaptive method-selection policy.

The intended distinction is:

$$
\boxed{
\text{CCM is not one solver and not one proof system.}
}
$$

It is a methodology for composing many such systems while preserving semantic boundaries between them.

## 3. Target Semantics

Let

$$
\mathcal P
$$

be a universe of mathematical targets.

A target

$$
P\in\mathcal P
$$

may be a proposition, a parameterized claim, an optimization statement, an existence problem, a nonexistence problem, an identity, or an inequality.

For foundational discussion, assume an external truth semantics

$$
\tau:
\mathcal P
\rightarrow
\{0,1\},
$$

where

$$
\tau(P)=1
$$

means that $P$ is mathematically true in the intended interpretation.

CCM does not assume that $\tau$ is computationally available.

The purpose of certificates is precisely to support terminal judgments without direct access to a truth oracle.

## 4. Representations

A target need not be studied in a single representation.

Let

$$
\mathfrak R(P)
=
\{
R_1(P),
\ldots,
R_k(P)
\}
$$

denote available representations.

Examples include:

$$
\text{graph}
\leftrightarrow
\text{adjacency matrix},
$$

$$
\text{integer feasibility}
\leftrightarrow
\text{cone membership},
$$

$$
\text{quartic in }x,y
\leftrightarrow
\text{quadratic in }u=x^2,v=y^2,
$$

$$
\text{primal optimization}
\leftrightarrow
\text{dual optimization}.
$$

A representation change is not automatically sound.

### Definition 4.1 — Certificate-Preserving Representation Morphism

Let

$$
T:
R(P)
\rightarrow
R'(P)
$$

be a transformation.

It is certificate-preserving if there exists a certificate-lifting map

$$
\Lambda_T
$$

such that every accepted terminal certificate $c'$ for the transformed target yields a valid certificate

$$
\Lambda_T(c')
$$

for the original target.

The transformation need not be syntactically invertible.

What matters is preservation of certificate semantics.

### Theorem 4.2 — Compositional Representation Soundness

If

$$
T_1,
T_2,
\ldots,
T_m
$$

are certificate-preserving representation morphisms, then

$$
T_m\circ\cdots\circ T_1
$$

is certificate-preserving.

#### Proof

Compose the lifting maps in reverse order:

$$
\Lambda
=
\Lambda_{T_1}
\circ
\Lambda_{T_2}
\circ
\cdots
\circ
\Lambda_{T_m}.
$$

An accepted certificate in the terminal representation is successively lifted to a valid certificate in every preceding representation and finally to the original target. Therefore the composite route preserves terminal semantics. $\square$

This theorem formalizes representation routing as a first-class CCM operation.

## 5. Certificate Languages

### Definition 5.1 — Certificate Language

A CCM certificate language is a tuple

$$
\mathcal C_i
=
(
D_i,
\Gamma_i,
A_i,
V_i,
\sigma_i,
K_i
),
$$

where:

- $D_i\subseteq\mathcal P$ is an applicability domain;
- $\Gamma_i(P)$ is the certificate space for target $P$;
- $A_i$ is a certificate-search procedure;
- $V_i(P,c)$ is a verifier;
- $\sigma_i(c)$ is the semantic type of the certificate;
- $K_i$ is a computational cost descriptor.

The search procedure may be heuristic, incomplete, randomized, numerical, AI-assisted, or human-guided.

The verifier is the semantic gate.

### Definition 5.2 — Positive and Negative Terminal Certificates

A certificate $c$ is positive if

$$
V_i(P,c)=1
\Longrightarrow
\tau(P)=1.
$$

A certificate $c$ is negative if

$$
V_i(P,c)=1
\Longrightarrow
\tau(P)=0.
$$

Negative certificates include explicit counterexamples and theorem-of-alternatives style infeasibility witnesses.

### Definition 5.3 — Method-Barrier Certificate

A barrier certificate does not decide $P$.

It decides a method-level proposition such as

$$
P\notin\operatorname{Cov}(\mathcal C_i)
$$

or a weaker rigorously stated obstruction to using $\mathcal C_i$.

Hence a barrier certificate has meta-semantics:

$$
\boxed{
\text{route blocked}
\not\Rightarrow
\text{target false}.
}
$$

A mere search failure is not a barrier certificate unless the search procedure is complete for the stated domain or an independent obstruction is verified.

## 6. Coverage Domains

### Definition 6.1 — Positive and Negative Coverage

For certificate language $\mathcal C_i$, define

$$
\operatorname{Cov}^{+}(\mathcal C_i)
=
\{
P\in D_i:
\exists c\in\Gamma_i(P),
V_i(P,c)=1,
\sigma_i(c)=+
\},
$$

and

$$
\operatorname{Cov}^{-}(\mathcal C_i)
=
\{
P\in D_i:
\exists c\in\Gamma_i(P),
V_i(P,c)=1,
\sigma_i(c)=-
\}.
$$

Define total terminal coverage

$$
\operatorname{Cov}(\mathcal C_i)
=
\operatorname{Cov}^{+}(\mathcal C_i)
\cup
\operatorname{Cov}^{-}(\mathcal C_i).
$$

### Definition 6.2 — Certificate Library

A certificate library is

$$
\mathfrak C
=
\{
\mathcal C_1,
\ldots,
\mathcal C_r
\}.
$$

Its coverage is

$$
\boxed{
\operatorname{Cov}(\mathfrak C)
=
\bigcup_{\mathcal C_i\in\mathfrak C}
\operatorname{Cov}(\mathcal C_i).
}
$$

### Theorem 6.3 — Library Coverage Monotonicity

If

$$
\mathfrak C_1
\subseteq
\mathfrak C_2,
$$

then

$$
\boxed{
\operatorname{Cov}(\mathfrak C_1)
\subseteq
\operatorname{Cov}(\mathfrak C_2).
}
$$

#### Proof

The union defining $\operatorname{Cov}(\mathfrak C_1)$ is taken over a subset of the certificate languages occurring in the union defining $\operatorname{Cov}(\mathfrak C_2)$. $\square$

This is ideal library-level monotonicity.

It does not by itself imply that a particular router will discover every newly available certificate.

### Definition 6.4 — Unresolved Region

Relative to a target domain

$$
\Omega\subseteq\mathcal P,
$$

define

$$
\boxed{
U(\mathfrak C;\Omega)
=
\Omega
\setminus
\operatorname{Cov}(\mathfrak C).
}
$$

### Corollary 6.5 — Unresolved Antimonotonicity

If

$$
\mathfrak C_1
\subseteq
\mathfrak C_2,
$$

then

$$
\boxed{
U(\mathfrak C_2;\Omega)
\subseteq
U(\mathfrak C_1;\Omega).
}
$$

This is the cleanest formal expression of CCM's proof-space enclosure intuition.

Adding sound certificate languages cannot enlarge the ideal unresolved region.

## 7. Truth Is Not Coverage

The distinction

$$
\boxed{
\text{truth domain}
\neq
\text{certificate coverage domain}
}
$$

is foundational.

### Proposition 7.1 — Coverage Failure Does Not Imply Falsity

Suppose a sound certificate language $\mathcal C$ is incomplete for a truth class $\mathcal T$:

$$
\operatorname{Cov}^{+}(\mathcal C)
\subsetneq
\mathcal T.
$$

Then there exists a true target $P$ such that

$$
P\notin\operatorname{Cov}^{+}(\mathcal C).
$$

Therefore failure to obtain a certificate in $\mathcal C$ does not imply

$$
\tau(P)=0.
$$

#### Proof

Strict inclusion provides a target in

$$
\mathcal T
\setminus
\operatorname{Cov}^{+}(\mathcal C).
$$

By definition it is true but not positively certifiable in the language. $\square$

The Motzkin nonnegative but non-SOS example is a concrete witness of this logic.

## 8. Search Failure, Barrier, and Falsity

CCM distinguishes three states:

$$
\boxed{
\text{search failure},
\qquad
\text{verified method barrier},
\qquad
\text{target falsification}.
}
$$

They are not interchangeable.

A certificate search may terminate with

$$
\texttt{NOT\_FOUND}.
$$

This means only that the current search did not produce a certificate.

A verified barrier can establish a stronger statement:

$$
\texttt{METHOD\_BLOCKED}.
$$

A negative terminal certificate establishes

$$
\texttt{DISPROVED}.
$$

Thus:

$$
\boxed{
\texttt{NOT\_FOUND}
\not\Rightarrow
\texttt{METHOD\_BLOCKED}
\not\Rightarrow
\texttt{DISPROVED}.
}
$$

The first implication may hold only with completeness of search.

The second may hold only when the method language is complete for the relevant truth class.

## 9. Terminal Semantics and Abstention

A CCM router has terminal outputs

$$
\mathcal R(P)
\in
\{
\mathrm{PROVED},
\mathrm{DISPROVED},
\mathrm{UNRESOLVED}
\}.
$$

Soundness requires

$$
\mathrm{PROVED}
\Longrightarrow
\tau(P)=1,
$$

and

$$
\mathrm{DISPROVED}
\Longrightarrow
\tau(P)=0.
$$

No truth assertion is attached to

$$
\mathrm{UNRESOLVED}.
$$

Abstention is therefore a mathematical safety state, not a failure of interface design.

## 10. Verification Firewall

### Theorem 10.1 — Certificate-Gated Routing Soundness

Assume:

1. every terminal positive verifier is sound;
2. every terminal negative verifier is sound;
3. every representation transformation used in the route is certificate-preserving;
4. the router returns PROVED or DISPROVED only after successful verification.

Then terminal judgments are sound regardless of how the router selected its methods.

#### Proof

The routing policy can influence which certificate candidates are searched for, but it cannot alter verifier semantics. If a terminal certificate is accepted in a transformed representation, compositional representation soundness lifts it back to the original target. Positive acceptance implies truth; negative acceptance implies falsity. Therefore heuristic search or routing cannot by itself create a false terminal judgment under the stated assumptions. $\square$

This theorem is the central soundness firewall of CCM.

It permits exploratory components to be non-rigorous while requiring terminal closure to be rigorous.

## 11. Research State

A compact CCM state is

$$
\boxed{
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
}
$$

The components are:

- $P$: target;
- $\mathcal R_t$: active representations;
- $\mathcal H_t$: active hypotheses;
- $\mathcal E_t$: controlled computational evidence;
- $\mathcal I_t$: extracted invariants;
- $\mathcal C_t^{+}$: verified positive certificates;
- $\mathcal C_t^{-}$: verified negative certificates;
- $\mathcal B_t$: verified barriers and excluded routes;
- $\mathfrak C_t$: current certificate library;
- $\mathcal A_t$: route history;
- $\widehat\Theta_t$: learned routing model;
- $w_t$: current computational-cost metadata.

A CCM operator

$$
\Phi_j
$$

acts by

$$
\mathcal S_{t+1}
=
\Phi_j(\mathcal S_t).
$$

Operators include search, symbolic reconstruction, representation transformation, certificate generation, verification, mutation, falsification, barrier extraction, compression, cost estimation, and route update.

## 12. Certified Knowledge and Non-Monotone Hypotheses

The full research state need not be monotone.

Hypotheses may be added and removed.

Representations may be abandoned.

Routing estimates may change.

However verified artifacts can be retained monotonically.

If

$$
\mathcal C_t^{+}
\subseteq
\mathcal C_{t+1}^{+},
$$

$$
\mathcal C_t^{-}
\subseteq
\mathcal C_{t+1}^{-},
$$

and

$$
\mathcal B_t
\subseteq
\mathcal B_{t+1},
$$

then the certified portion of research knowledge is monotone even when the speculative portion is not.

This is the basis of CCM's accumulation principle:

$$
\boxed{
\text{failed ideas may disappear;
verified information should not}.
}
$$

## 13. Falsification as State Update

Suppose an intermediate hypothesis

$$
H\in\mathcal H_t
$$

is falsified by a verified counterexample.

CCM updates:

$$
\mathcal H_{t+1}
=
\mathcal H_t
\setminus
\{H\},
$$

and records the exclusion:

$$
\mathcal B_{t+1}
=
\mathcal B_t
\cup
\{\neg H\}.
$$

Thus falsification is converted into a persistent routing constraint.

This differs from silently discarding a failed attempt.

The route space is changed by the failure.

## 14. Mutation and Boundary Detection

Let

$$
\mu_\delta(P)
$$

be a controlled mutation family.

A certificate language may change status across a parameter boundary:

$$
\mu_{\delta_1}(P)
\in
\operatorname{Cov}^{+}(\mathcal C),
$$

while

$$
\mu_{\delta_2}(P)
\in
\operatorname{Cov}^{-}(\mathcal C').
$$

Such mutations can identify:

- sign requirements;
- tight constants;
- uniqueness conditions;
- robustness radii;
- deletion distances;
- certificate phase boundaries.

Mutation is therefore not only stress testing.

It is an operator for discovering the validity domain of an invariant or certificate language.

## 15. Defect-Decomposition Certificate Schema

A recurring certificate grammar appears in optimization, convexity, and polynomial nonnegativity.

### Proposition 15.1 — Nonnegative Defect Decomposition

Suppose a target gap satisfies

$$
G
=
\sum_{\alpha}
\lambda_\alpha D_\alpha
$$

with

$$
\lambda_\alpha\ge0
$$

and

$$
D_\alpha\ge0.
$$

Then

$$
G\ge0.
$$

If additionally every active coefficient satisfies

$$
\lambda_\alpha>0,
$$

then

$$
G=0
$$

implies

$$
D_\alpha=0
$$

for every active term.

#### Proof

The sum of nonnegative terms is nonnegative. Equality of the sum to zero forces each strictly weighted nonnegative term to vanish. $\square$

Examples include:

$$
b^Ty-c^Tx
=
y^T(b-Ax)
+
x^T(A^Ty-c),
$$

$$
\sum_iw_ix_i^2-\mu^2
=
\sum_{i<j}w_iw_j(x_i-x_j)^2,
$$

and

$$
p
=
\sum_kq_k^2.
$$

CCM treats defect decomposition as a reusable certificate schema rather than a theorem specific to one field.

## 16. Nonexistence as a Positive Object

Failed search is not a proof of nonexistence.

When a theorem of alternatives or separation theorem is available, CCM prefers a positive artifact certifying the negative conclusion.

For example:

$$
Ax=b,
\qquad
x\ge0
$$

may be ruled out by

$$
A^Ty\ge0,
\qquad
b^Ty<0.
$$

The nonexistence claim is negative, but the certificate is a finite positive object.

This motivates the methodological principle:

$$
\boxed{
\text{compile nonexistence into a checkable witness whenever possible}.
}
$$

The principle is conditional.

Not every nonexistence problem is guaranteed to admit a short certificate in the chosen formal system.

## 17. Universal and Minimal Certificates

A certificate can be universally valid yet instance-redundant.

For a matrix $A$, the characteristic polynomial gives a universal annihilator:

$$
p_A(A)=0.
$$

But the minimal polynomial may have smaller degree.

CCM therefore distinguishes:

$$
C_{\mathrm{universal}}
$$

from

$$
C_{\mathrm{minimal}}(P).
$$

The first prioritizes guaranteed coverage.

The second prioritizes instance-specific compression.

This distinction matters whenever certificates become executable reduction rules.

## 18. Certificate Strength

For certificates concerning the same target, define a semantic preorder.

Write

$$
c_1
\preceq
c_2
$$

if the verified conclusion of $c_2$ implies the verified conclusion of $c_1$.

Examples include:

$$
\text{feasibility}
\preceq
\text{optimality},
$$

or:

$$
\text{nonnegative gap}
\preceq
\text{quantitative lower bound}.
$$

Certificate strength is independent of certificate search cost.

A stronger certificate can be more expensive to find or easier to verify.

## 19. Certificate-Language Metadata

A practical certificate language should expose metadata:

$$
\boxed{
\mathcal C_i
=
(
D_i,
S_i,
V_i,
K_i,
M_i
).
}
$$

Here:

- $D_i$: structural applicability domain;
- $S_i$: semantic certificate type;
- $V_i$: verification procedure;
- $K_i$: cost model;
- $M_i$: known limitations or barriers.

This metadata is the interface between mathematical proof languages and route selection.

## 20. Marginal Coverage

For a library $\mathfrak C$ and new language $\mathcal C$, define marginal coverage set

$$
\Delta_{\mathrm{Cov}}
(
\mathcal C\mid\mathfrak C
)
=
\operatorname{Cov}(\mathcal C)
\setminus
\operatorname{Cov}(\mathfrak C).
$$

On a finite benchmark domain

$$
\Omega,
$$

define normalized marginal coverage gain

$$
\boxed{
G_{\mathrm{coverage}}
=
\frac{
\left|
\Delta_{\mathrm{Cov}}
(
\mathcal C\mid\mathfrak C
)
\cap\Omega
\right|
}{
|\Omega|
}.
}
$$

This metric asks:

> How much new target space does the added certificate language close?

It is different from routing efficiency.

## 21. Cost Vectors

Computational cost should not be collapsed too early into wall-clock time.

Let route workload be

$$
\boxed{
K(\rho,P)
=
(
K_1,
\ldots,
K_d
)
\in
\mathbb R_{\ge0}^{d}.
}
$$

Coordinates may count:

- solver calls;
- symbolic factorizations;
- SAT branches;
- exact grid evaluations;
- matrix operations;
- proof-checking steps;
- memory;
- token consumption;
- human interventions.

An environment-specific scalarization is

$$
C_t(\rho,P)
=
\langle
w_t,
K(\rho,P)
\rangle.
$$

The weight vector

$$
w_t
$$

may change with hardware, software, model quality, or economic cost.

Hence:

$$
\boxed{
\text{canonical workload}
\neq
\text{environment-specific runtime}.
}
$$

## 22. Routing Policy

A router is a policy

$$
\pi_t:
\mathcal S_t
\rightarrow
\mathcal M
\cup
\{
\mathrm{ABSTAIN}
\},
$$

where $\mathcal M$ includes certificate searches and representation transformations.

A static router depends only on fixed features.

A cost-aware router uses $K$ and $w_t$.

An online router also uses learned state

$$
\widehat\Theta_t.
$$

## 23. Conservative Routing Extension

Suppose a library is expanded:

$$
\mathfrak C_t
\subseteq
\mathfrak C_{t+1}.
$$

A routing extension is conservative on a target set $\Omega$ if every previously terminal target retains a terminal certificate with the same truth semantics.

This is stronger than library coverage monotonicity.

Ideal coverage can grow while a badly implemented router regresses.

Therefore CCM separates:

$$
\boxed{
\text{library monotonicity}
}
$$

from

$$
\boxed{
\text{router monotonicity}.
}
$$

## 24. Coverage Gain and Routing Gain

Let two systems use the same certificate library on the same target set.

Routing gain may be defined by a cost scalarization:

$$
\boxed{
G_{\mathrm{route}}
=
1-
\frac{
C(\pi_{\mathrm{adaptive}})
}{
C(\pi_{\mathrm{baseline}})
}.
}
$$

Coverage gain instead measures newly closed targets.

Therefore:

$$
\boxed{
G_{\mathrm{coverage}}
\neq
G_{\mathrm{route}}.
}
$$

One can increase without the other.

### Proposition 24.1 — Coverage Monotonicity Does Not Imply Cost Monotonicity

Adding a sound certificate language can increase or preserve ideal coverage while increasing the cost of a naive router.

#### Proof

Take a router that executes every available method sequentially before returning an already available certificate. Add a sound method with positive cost that contributes no new certificate for the target. Coverage is unchanged, but route cost increases. $\square$

Thus larger libraries require routing discipline.

## 25. Route Regret

For target $P$, let

$$
\mathcal R(P)
$$

be candidate routes.

Given scalarized cost $C$, define oracle route cost

$$
C^*(P)
=
\min_{\rho\in\mathcal R(P)}
C(\rho,P).
$$

For policy $\pi$:

$$
\boxed{
R_\pi(P)
=
C(\pi(P),P)
-
C^*(P).
}
$$

Aggregate regret over targets is

$$
R_\pi
=
\sum_P
R_\pi(P).
$$

Regret measures method-selection inefficiency separately from proof correctness.

## 26. Dynamic Routing

In changing research environments, write

$$
w_t
$$

for computational cost metadata and

$$
\theta_t
$$

for latent target-distribution state.

An online routing model maintains

$$
\widehat\Theta_t
$$

and updates it from observed route outcomes:

$$
\boxed{
\widehat\Theta_{t+1}
=
U(
\widehat\Theta_t,
O_t
).
}
$$

The policy becomes

$$
\boxed{
\pi_t
=
\Pi(
F(P_t),
\mathfrak C_t,
\widehat\Theta_t,
w_t,
\mathcal A_t
).
}
$$

CCM distinguishes:

$$
\text{epistemic drift}
$$

from

$$
\text{infrastructure drift}.
$$

The first concerns the changing distribution of mathematical targets or route success.

The second concerns the changing computational price of methods.

## 27. Static and Dynamic Regret

For a sequence of targets, define policy cost

$$
C_T(\pi)
=
\sum_{t=1}^{T}
C_t(
\pi_t(P_t),
P_t
).
$$

Static regret against a fixed comparator class $\Pi_{\mathrm{stat}}$ is

$$
\boxed{
R_{\mathrm{static}}
=
C_T(\pi)
-
\min_{\pi'\in\Pi_{\mathrm{stat}}}
C_T(\pi').
}
$$

Dynamic regret against a time-varying oracle class is

$$
\boxed{
R_{\mathrm{dynamic}}
=
C_T(\pi)
-
C_T(\pi^*_{\mathrm{dynamic}}).
}
$$

Switch latency

$$
L_{\mathrm{switch}}
$$

measures how quickly the router adopts a newly preferable route after a genuine environmental change.

These quantities describe routing quality, not theorem truth.

## 28. CCM Performance Vector

A single scalar is insufficient.

A minimal performance state is

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

Here:

- $G_{\mathrm{coverage}}$: marginal closure of target space;
- $G_{\mathrm{route}}$: computational savings from routing;
- $R_{\mathrm{static}}$: regret against best static policy;
- $R_{\mathrm{dynamic}}$: regret against dynamic comparator;
- $L_{\mathrm{switch}}$: adaptation latency;
- $E_{\mathrm{sound}}$: unsound terminal judgments.

In a rigorous system,

$$
E_{\mathrm{sound}}
$$

should be treated as a hard safety dimension rather than an ordinary optimization objective.

## 29. The Composite Route Graph

CCM can be represented as a directed research graph.

Nodes include:

$$
\text{representations},
\quad
\text{hypotheses},
\quad
\text{evidence states},
\quad
\text{certificate states},
\quad
\text{barrier states}.
$$

Edges are operators:

$$
\text{transform},
\quad
\text{search},
\quad
\text{verify},
\quad
\text{mutate},
\quad
\text{compress},
\quad
\text{route}.
$$

A terminal truth closure is a node containing a verified positive or negative certificate.

A method barrier is a nonterminal node that removes or penalizes future route edges.

This graph interpretation connects proof-space enclosure with routing.

As barriers and terminal certificates accumulate, the active route graph can shrink even when the original mathematical universe does not.

## 30. A Canonical CCM Research Loop

A disciplined CCM loop is:

1. **Normalize the target.**  
   Specify the exact claim, domain, quantifiers, and acceptable closure semantics.

2. **Generate representations.**  
   Record certificate-preserving transformations rather than informal reformulations.

3. **Extract structural features.**  
   Identify degree, symmetry, support, convexity, recurrence, duality, combinatorial type, or other route-relevant information.

4. **Choose a route.**  
   Select a certificate language or cheap falsifier using current coverage and cost metadata.

5. **Search.**  
   Use symbolic, numeric, combinatorial, formal, human, or AI-assisted procedures.

6. **Verify.**  
   Do not promote search output to theorem status before certificate validation.

7. **Classify failure.**  
   Distinguish NOT_FOUND, METHOD_BLOCKED, DISPROVED, and UNRESOLVED.

8. **Preserve artifacts.**  
   Retain certificates, counterexamples, barriers, exact data, route logs, and provenance.

9. **Update state.**  
   Remove falsified hypotheses, change route priors, update method costs, and expand or prune the active route graph.

10. **Commit only after validation.**  
    Formal source, mathematical delimiters, checksums, and provenance are part of the research artifact.

This loop is methodological.

It can be implemented with or without AI.

## 31. CCM and AI

AI is not part of the definition of CCM.

An AI system may serve as:

$$
\text{hypothesis generator},
$$

$$
\text{representation proposer},
$$

$$
\text{certificate-search controller},
$$

$$
\text{literature synthesizer},
$$

or

$$
\text{routing policy}.
$$

But CCM does not grant semantic authority to the generator.

The authority lies in certificate verification and representation soundness.

This produces a useful separation:

$$
\boxed{
\text{high-variance discovery}
+
\text{low-variance verification}.
}
$$

The architecture is therefore compatible with human-only, computer-only, or human--AI--computer research configurations.

## 32. CCM and Computational Mathematicalism

CCM supports a weak methodological form of computational mathematicalism.

The weak claim is:

> Computation can be part of the state, evidence, transformation, certificate, and control structure of mathematics rather than merely an auxiliary calculator.

The theory does not require the stronger ontological claim that all mathematical truth is reducible to feasible computation.

Nor does it claim that finite computation replaces proof.

Instead:

$$
\boxed{
\text{computation organizes the search space;
certificates organize closure}.
}
$$

This distinction preserves classical rigor while expanding the operational role of computation.

## 33. Evidence from Benchmarks 01--13

The benchmark program is not the definition of CCM.

It provides empirical witnesses for the framework.

### Benchmark 01 — Mantel

Witnessed:

$$
\text{finite evidence}
\rightarrow
\text{structural invariant}
\rightarrow
\text{global lift}.
$$

### Benchmark 02 — Frobenius Two-Coin

Added exact symbolic reconstruction and residue-threshold compression.

### Benchmark 03 — Zeckendorf

Added recursive state partition, algorithm extraction, and mutation-based necessity testing.

### Benchmark 04 — Ramsey $R(3,3)=6$

Added SAT/UNSAT representations, falsification-as-constraint, multiplicity strengthening, and deletion-distance robustness.

### Benchmark 05 — Cayley--Hamilton

Extended CCM to symbolic algebra, theorem-to-runtime reduction, and universal-versus-minimal certificates.

### Benchmark 06 — Primal--Dual Linear Programming

Added dual-space coupling, certificate hierarchy, and nonnegative gap decomposition.

### Benchmark 07 — Farkas Lemma

Added positive certificates of nonexistence and explicit positive/negative certificate typing.

### Benchmark 08 — Jensen / Variance

Extended defect-decomposition certificates into nonlinear convexity and sign-domain mutation.

### Benchmark 09 — SOS / Motzkin

Established the operational distinction between truth domain and certificate-language coverage, and introduced method-barrier certificates.

### Benchmark 10 — Composite Routing

Introduced PROVED / DISPROVED / UNRESOLVED routing semantics and structure-aware method selection.

### Benchmark 11 — Certificate-Library Expansion

Demonstrated controlled ideal-coverage expansion and conservative router extension on a fixed target set.

### Benchmark 12 — Cost-Aware Routing

Introduced overlapping certificate languages, vector-valued workload, representation cost, and route regret.

### Benchmark 13 — Online Adaptive Routing

Introduced nonstationary target and infrastructure drift, online state updates, dynamic regret, and switch latency.

The cross-benchmark conclusion is not that one universal proof trick has been found.

It is that a stable control architecture persists while the domain-level certificate objects change.

## 34. Core Principles

The foundational CCM principles can be summarized as follows.

### Principle I — Certificate Closure

A target reaches terminal mathematical status only through a verified certificate or a formally accepted proof object.

### Principle II — Search / Verification Separation

Search may be heuristic.

Verification must satisfy the semantics required for closure.

### Principle III — Coverage / Truth Separation

Failure of a certificate language is not failure of the theorem.

### Principle IV — Barrier Preservation

A verified method barrier is retained as positive research information and used to alter future routing.

### Principle V — Representation First-Classness

Equivalent or certificate-preserving representations are first-class research objects with their own costs and certificate affordances.

### Principle VI — Nonexistence Compilation

When possible, nonexistence should be represented by a positive finite witness rather than by exhausted search.

### Principle VII — Cost Vectorization

Method cost is multidimensional and environment-dependent.

### Principle VIII — Coverage / Routing Separation

Library capacity and routing efficiency are distinct dimensions.

### Principle IX — Adaptive Routing

Research history and changing infrastructure can rationally alter future method selection.

### Principle X — Provenance-Preserving Accumulation

Verified certificates, counterexamples, barriers, and route metadata should survive across iterations even when hypotheses do not.

## 35. Claims Supported by the Current Theory and Benchmarks

The following claims are supported at the level stated.

1. Heterogeneous mathematical methods can be represented inside a common certificate-and-routing state model.

2. Sound certificate-gated routing remains logically sound even if search or route selection is heuristic, provided representation morphisms and verifiers are sound.

3. Ideal certificate-library coverage is monotone under library inclusion.

4. The unresolved region is correspondingly antimonotone.

5. Method coverage is not the same as mathematical truth.

6. Verified method barriers can guide route switching without deciding the target.

7. Certificate overlap creates a genuine cost optimization problem.

8. Dynamic method costs and target distributions justify time-dependent routing policies.

9. The 13 benchmark studies provide controlled examples of these mechanisms across substantially different mathematical ecologies.

## 36. Claims Not Established

CCM v1.0 does not establish:

1. that CCM is universally better than expert single-route mathematics;

2. that every mathematical target has a finite positive or negative certificate;

3. that the proposed certificate library is complete for any broad class unless separately proven;

4. that an AI or computer can autonomously discover all relevant representations;

5. that route-cost models learned on one domain transfer without calibration;

6. that online routing can learn from cold start without historical route data;

7. that wall-clock speedups observed in one environment are universal;

8. that unresolved-region shrinkage necessarily converges to zero;

9. that all barriers are decidable;

10. that formal verification is computationally cheap.

These are research questions, not hidden assumptions.

## 37. Research Program after the Foundational Version

The foundational theory suggests several separate research programs.

### 37.1 Coverage Geometry

Study overlaps and differences among certificate coverage domains:

$$
\operatorname{Cov}(\mathcal C_i)
\cap
\operatorname{Cov}(\mathcal C_j),
$$

$$
\operatorname{Cov}(\mathcal C_i)
\setminus
\operatorname{Cov}(\mathcal C_j).
$$

### 37.2 Certificate Translation

Study when proofs or certificates in one language can be translated into another with bounded overhead, connecting CCM to proof-system simulation.

### 37.3 Cold-Start Routing

Remove historical route priors and learn method success and cost profiles online.

### 37.4 Formal CCM Kernel

Implement a small trusted kernel for:

- target declarations;
- representation morphisms;
- certificate types;
- verifier interfaces;
- barrier objects;
- provenance;
- route logs.

### 37.5 Blind Benchmarks

Use theorem statements hidden from the routing model or newly generated formal targets to reduce prior-knowledge contamination.

### 37.6 Human--AI--Computer Comparative Studies

Separate contributions of:

$$
\text{human insight},
\quad
\text{AI generation},
\quad
\text{exact computation},
\quad
\text{formal verification}.
$$

### 37.7 Proof-Space Enclosure

Define measurable target domains and study whether accumulation of certificates and barriers yields useful rates of unresolved-space contraction.

## 38. Conclusion

Computational Composite Methodology treats mathematics research as a certificate-directed, representation-aware, dynamically routed process.

Its core separation is:

$$
\boxed{
\text{truth}
\neq
\text{coverage}
\neq
\text{search success}
\neq
\text{cost}.
}
$$

Its core soundness rule is:

$$
\boxed{
\text{heuristic discovery is allowed;
terminal closure is certificate-gated}.
}
$$

Its core growth rule is:

$$
\boxed{
\mathfrak C_t
\subseteq
\mathfrak C_{t+1}
\Longrightarrow
\operatorname{Cov}(\mathfrak C_t)
\subseteq
\operatorname{Cov}(\mathfrak C_{t+1}).
}
$$

Its core routing problem is:

$$
\boxed{
\text{choose the representation and certificate language that best advances the current research state}.
}
$$

The 13 calibration benchmarks indicate that this architecture can persist across very different mathematical proof ecologies.

CCM v1.0 should therefore be read as a general mathematical methodology and research-control theory, not as a solver for one conjecture and not as a claim of universal automation.

The next stage is no longer to keep adding unrelated calibration examples.

It is to formalize, compare, and test the theory itself.

## References

[R1] D. H. Bailey and J. M. Borwein, “Experimental Mathematics: Examples, Methods and Implications,” Notices of the American Mathematical Society, 52(5), 502--514, 2005.

[R2] J. R. Rice, “The Algorithm Selection Problem,” Advances in Computers, 15, 65--118, 1976.

[R3] L. Xu, F. Hutter, H. H. Hoos, and K. Leyton-Brown, “SATzilla: Portfolio-Based Algorithm Selection for SAT,” Journal of Artificial Intelligence Research, 32, 565--606, 2008. DOI: 10.1613/JAIR.2490.

[R4] M. Gagliolo and J. Schmidhuber, “Algorithm Selection as a Bandit Problem with Unbounded Losses,” arXiv:0807.1494, 2008; later work developed the portfolio-selection formulation.

[R5] W. C. Cheung, D. Simchi-Levi, and R. Zhu, “Hedging the Drift: Learning to Optimize under Non-Stationarity,” arXiv:1903.01461, 2019.

[R6] S. A. Cook and R. A. Reckhow, “The Relative Efficiency of Propositional Proof Systems,” The Journal of Symbolic Logic, 44(1), 36--50, 1979. DOI: 10.2307/2273702.

[R7] Z. Chihani, D. Miller, and F. Renaud, “Foundational Proof Certificates in First-Order Logic,” CADE-24, Lecture Notes in Computer Science 7898, 162--177, 2013.

[R8] E. Clarke, O. Grumberg, S. Jha, Y. Lu, and H. Veith, “Counterexample-Guided Abstraction Refinement,” CAV 2000, Lecture Notes in Computer Science 1855, 154--169, 2000. DOI: 10.1007/10722167_15.

[R9] P. A. Parrilo, “Semidefinite Programming Relaxations for Semialgebraic Problems,” Mathematical Programming, Series B, 96, 293--320, 2003. DOI: 10.1007/s10107-003-0387-5.
