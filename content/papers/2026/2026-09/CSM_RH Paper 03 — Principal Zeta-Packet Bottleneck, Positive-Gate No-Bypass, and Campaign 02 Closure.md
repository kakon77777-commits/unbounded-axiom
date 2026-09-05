# CSM_RH Paper 03
## Principal Zeta-Packet Bottleneck, Positive-Gate No-Bypass, and Campaign 02 Closure

**Project:** `CSM_RH`  
**Paper:** `03`  
**Version:** `v0.1`  
**Date:** `2026-09-05`  
**Parent state:** `CSM_RH v0.3 / Paper 02`  
**Status:** structural reduction / gate-strength theorem; not a proof or disproof of RH  
**中文標題：** CSM_RH 論文 03：主 Zeta 封包瓶頸、正閘門不可繞道與 Campaign 02 閉合  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**Language:** English

---

# 0. Trust boundary

This paper does not prove or disprove the Riemann Hypothesis.

Canonical root state:

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
CSM_RH_ROOT_STATUS = OPEN
```

The purpose of this paper is narrower:

1. isolate the $q=1$ principal zeta packet inside the positive EMAE gate;
2. prove an exact equivalence between its fixed-power bound and a fixed zeta zero strip;
3. show that conductor weights, character-family averaging, zero-density estimates, and Deuring–Heilbronn mechanisms cannot by themselves bypass this $q=1$ necessary condition;
4. close `CSM_RH Campaign 02` as a reduction campaign rather than a proof campaign;
5. define the next gate-minimality search.

No live GLM-5.3-Flash run is claimed.

---

# 1. Starting state

Paper 02 proved that the smooth $q=1$ zeta-zero packet has exact exponential type.

Let

$$
\Theta_\zeta
=
\sup_{\rho}
\Re\rho
$$

over nontrivial zeta zeros, and let

$$
\Delta_\zeta
=
\Theta_\zeta-\frac12.
$$

By functional-equation symmetry,

$$
\Theta_\zeta
=
\frac12+\Delta_\zeta.
$$

Paper 02 established, for the Hilbert packet $F(T)$,

$$
\inf
\left\{
a:
\|F(T)\|
=
O(e^{aT})
\right\}
=
\Theta_\zeta.
$$

For the associated positive $q=1$ pole-zero energy,

$$
\mathcal E_\zeta(e^T;U)
=
e^T
\|F(T)\|^2,
$$

the exact type is

$$
\boxed{
\tau_\zeta
=
1+2\Theta_\zeta
=
2+2\Delta_\zeta.
}
$$

This paper studies what that exact identity does to the full arithmetic EMAE program.

---

# 2. The $q=1$ packet is an unavoidable positive summand

The v3.18 character major-arc energy is

$$
\mathfrak Z_2(x;Q,U)
=
\sum_{\substack{
q\le Q\\
q\ {\rm squarefree}
}}
\frac{
|\mu(q)|^2
}{
\phi(q)^3
}
\sum_{\chi\bmod q}
|\tau(\chi)|^2
\int_{|\epsilon|\le U/x}
|W_{x,\epsilon}(1)|^2
|Z_\chi(x,\epsilon)|^2
d\epsilon.
$$

At

$$
q=1,
$$

all arithmetic weights are equal to one.

The unique character is the trivial character, and the corresponding primitive $L$ -function is the Riemann zeta function.

Therefore the $q=1$ term is exactly

$$
\boxed{
\mathcal E_\zeta(x;U)
=
\int_{|\epsilon|\le U/x}
|W_{x,\epsilon}(1)|^2
|Z_\zeta(x,\epsilon)|^2
d\epsilon.
}
$$

Since every term in $\mathfrak Z_2$ is nonnegative,

$$
\boxed{
\mathfrak Z_2(x;Q,U)
\ge
\mathcal E_\zeta(x;U).
}
$$

This inequality is independent of every nonprincipal character estimate.

---

# 3. Principal Zeta-Packet Fixed Power

For fixed

$$
0\le\eta\le1,
$$

define:

## ZPPF $(\eta)$

For every

$$
\varepsilon>0,
$$

$$
\boxed{
\mathcal E_\zeta(x;U)
\ll_{\varepsilon,w,U}
x^{3-\eta+\varepsilon}.
}
$$

Equivalently,

$$
\mathcal E_\zeta(x;U)
\ll
x^{3-\eta+o(1)}.
$$

The acronym is:

```text
ZPPF
PRINCIPAL ZETA-PACKET FIXED POWER
```

---

# 4. Exact ZPPF / zero-strip equivalence

## Theorem 4.1 — Principal Zeta-Packet Equivalence

For fixed

$$
0\le\eta\le1,
$$

the following are equivalent:

$$
\boxed{
\operatorname{ZPPF}(\eta)
}
$$

and

$$
\boxed{
\Theta_\zeta
\le
1-\frac{\eta}{2}.
}
$$

Equivalently,

$$
\boxed{
\Delta_\zeta
\le
\frac12-\frac{\eta}{2}.
}
$$

### Proof: ZPPF implies the strip

ZPPF $(\eta)$ gives

$$
\tau_\zeta
\le
3-\eta.
$$

Paper 02 gives

$$
\tau_\zeta
=
1+2\Theta_\zeta.
$$

Therefore

$$
1+2\Theta_\zeta
\le
3-\eta,
$$

so

$$
\Theta_\zeta
\le
1-\frac{\eta}{2}.
$$

### Proof: the strip implies ZPPF

Paper 02 also gives the direct upper bound

$$
\|F(T)\|
\le
e^{\Theta_\zeta T}
\sum_\rho
\|v_\rho\|.
$$

The coefficient sum is finite.

Hence

$$
\mathcal E_\zeta(e^T;U)
\ll
e^{(1+2\Theta_\zeta)T}.
$$

If

$$
\Theta_\zeta
\le
1-\frac{\eta}{2},
$$

then

$$
1+2\Theta_\zeta
\le
3-\eta.
$$

Therefore

$$
\mathcal E_\zeta(x;U)
\ll
x^{3-\eta}.
$$

Thus ZPPF $(\eta)$ holds. $\square$

---

# 5. RH endpoint

Set

$$
\eta=1.
$$

Theorem 4.1 gives

$$
\operatorname{ZPPF}(1)
\Longleftrightarrow
\Theta_\zeta
\le
\frac12.
$$

Functional-equation symmetry gives

$$
\Theta_\zeta
\ge
\frac12.
$$

Therefore

$$
\boxed{
\operatorname{ZPPF}(1)
\Longleftrightarrow
RH.
}
$$

The $q=1$ positive packet is therefore an exact RH diagnostic at the endpoint.

---

# 6. EMAE necessity theorem

Recall

$$
\operatorname{EMAE}(\eta):
\qquad
\mathfrak Z_2(x;Q,U)
+
\mathfrak Z_4(x;Q,U)
\ll
x^{3-\eta+o(1)}.
$$

Because

$$
\mathfrak Z_4\ge0
$$

and

$$
\mathfrak Z_2
\ge
\mathcal E_\zeta,
$$

we obtain:

## Theorem 6.1 — EMAE necessarily contains a zeta strip

For every fixed

$$
\eta>0,
$$

$$
\boxed{
\operatorname{EMAE}(\eta)
\Longrightarrow
\operatorname{ZPPF}(\eta)
\Longrightarrow
\Theta_\zeta
\le
1-\frac{\eta}{2}.
}
$$

Thus a proof of positive EMAE at any fixed power already proves a new fixed zero strip for zeta before any nonprincipal character issue is considered.

This is a necessary-condition theorem.

It is stronger than the earlier single-zero heuristic because the packet interference question was closed in Paper 02.

---

# 7. Positive-Gate No-Bypass theorem

The previous theorem extends beyond the exact EMAE definition.

Let

$$
\mathcal G(x)\ge0
$$

be any proposed positive sufficient gate.

Assume that for some nonnegative weight $c(x)$,

$$
\mathcal G(x)
\ge
c(x)
\mathcal E_\zeta(x;U).
$$

## Theorem 7.1 — Subpolynomial $q=1$ retention

Suppose

$$
c(x)
=
x^{-o(1)}.
$$

If

$$
\mathcal G(x)
\ll
x^{3-\eta+o(1)}
$$

for a fixed

$$
\eta>0,
$$

then

$$
\boxed{
\Theta_\zeta
\le
1-\frac{\eta}{2}.
}
$$

### Proof

Since

$$
c(x)^{-1}
=
x^{o(1)},
$$

we have

$$
\mathcal E_\zeta(x;U)
\le
c(x)^{-1}\mathcal G(x)
\ll
x^{3-\eta+o(1)}.
$$

Apply Theorem 4.1. $\square$

---

# 8. Fixed-power weight-loss law

More generally, suppose

$$
c(x)
\ge
x^{-\lambda+o(1)}
$$

for fixed

$$
\lambda\ge0.
$$

Then

$$
\mathcal G(x)
\ll
x^{3-\eta+o(1)}
$$

implies

$$
\mathcal E_\zeta(x;U)
\ll
x^{3-(\eta-\lambda)+o(1)}.
$$

Hence, if

$$
\eta>\lambda,
$$

then

$$
\boxed{
\Theta_\zeta
\le
1-\frac{\eta-\lambda}{2}.
}
$$

Consequently, a positive gate can avoid any fixed-strip consequence only by losing at least the full fixed power in its $q=1$ retention.

But such a loss creates a separate target-fidelity question:

> does the weakened gate still control the actual $q=1$ prime-pair mismatch?

That question cannot be assumed.

---

# 9. Why conductor weighting cannot solve the full EMAE gate

For

$$
q>1,
$$

v3.18 identified useful weights such as

$$
q^{-2+o(1)}
$$

in the pole-zero channel.

These weights can genuinely suppress high-conductor characters.

However, at

$$
q=1,
$$

the conductor weight is exactly one.

Therefore no conductor-weight argument can reduce the zeta exponent

$$
1+2\Theta_\zeta.
$$

Conductor weighting remains useful for the nonprincipal remainder after the $q=1$ problem has been separately handled.

It is not a bypass of the principal bottleneck.

---

# 10. Why height weights cannot change fixed exponential type

For each fixed zeta zero

$$
\rho=\beta+i\gamma,
$$

the smooth Mellin coefficient

$$
v_\rho
$$

may be very small for large

$$
|\gamma|.
$$

But Paper 02 proved

$$
v_\rho\neq0
$$

for every zero and

$$
\tau_F=\Theta_\zeta.
$$

Therefore any $x$ -independent nonzero coefficient suppression in zero height changes constants but not the exponential type.

In particular, rapid vertical decay is sufficient for convergence, but it does not turn

$$
x^\beta
$$

into

$$
x^{\beta-\delta}
$$

for a fixed zero.

This closes the following false inference:

```text
very small high-zero coefficient
->
fixed-power suppression of every near-extremal zero
```

The implication is invalid at the asymptotic exponent level.

---

# 11. Current prime exponential-sum input at the $q=1$ core

Maynard–Pandey–Radziwiłł (2026) prove that if

$$
\alpha=\frac aq+\epsilon
$$

and

$$
B=\max(q,qN|\epsilon|),
$$

then

$$
\left|
\sum_{n<N}
\Lambda(n)e(n\alpha)
\right|
\le
N^{o(1)}
\left(
\frac{N}{B^{1/2}}
+
N^{19/24}
\right).
$$

On the principal core arc,

$$
q=1,
\qquad
\epsilon=\frac{u}{N},
\qquad
|u|\le U,
$$

so

$$
B
=
\max(1,|u|)
=
O_U(1).
$$

Hence the theorem gives only

$$
\boxed{
|S_N(u/N)|
\le
N^{1+o(1)}
}
$$

at this core scale.

The new

$$
N^{19/24}
$$

generic term is dominated by the unsaved

$$
N/B^{1/2}
$$

term.

Thus the strongest current generic exponential-sum advance is fully consistent with the `CSM_RH` principal-bottleneck classification.

---

# 12. Current zero-density progress does not remove the principal bottleneck

Guth–Maynard (Annals of Mathematics, 2026) prove

$$
N(\sigma,T)
\le
T^{30(1-\sigma)/13+o(1)}.
$$

Chen–Gupta–Li, in the 2026 revision of their character large-values paper, prove

$$
\sum_{\chi\bmod q}
N(\sigma,T,\chi)
\ll_\varepsilon
(qT)^{7(1-\sigma)/3+\varepsilon}.
$$

These are major zero-population estimates.

But neither statement logically excludes one zeta zero with

$$
\Re\rho>1-\frac{\eta}{2}
$$

for a prescribed fixed

$$
\eta>0.
$$

By Theorem 4.1, one such zero is enough to rule out ZPPF $(\eta)$.

Therefore:

```text
ZERO POPULATION CONTROL
does not imply
ZPPF FIXED POWER.
```

This is now a direct consequence of the exact packet-type theorem.

---

# 13. Current zero-free regions are not fixed strips

Bellotti–Trudgian–Yang (2026) prove an explicit zeta zero-free region of the form

$$
\zeta(\sigma+it)\neq0
$$

when

$$
t\ge3
$$

and

$$
\sigma
\ge
1-\frac{1}{4.896\log t}.
$$

This is valuable explicit progress.

However the width

$$
\frac{1}{4.896\log t}
$$

tends to zero with height.

It does not imply a fixed

$$
\delta>0
$$

such that

$$
\Theta_\zeta
\le1-\delta.
$$

Therefore it does not close ZPPF $(\eta)$ for any fixed

$$
\eta>0.
$$

---

# 14. Deuring–Heilbronn does not bypass $q=1$

Modern explicit Deuring–Heilbronn results give zero repulsion for Dirichlet $L$ -functions under the existence of a Landau–Siegel zero.

This mechanism is relevant to exceptional real characters.

But the necessary principal subgate in Theorem 6.1 is the Riemann zeta packet at

$$
q=1.
$$

Therefore Deuring–Heilbronn may improve the nonprincipal character remainder but cannot, by itself, establish the $q=1$ ZPPF gate.

This is a scope obstruction, not a criticism of the theorem.

---

# 15. Correction to the v3.18 weighted-extreme-zero optimism

v3.18 correctly observed that the full character major-arc energy contains:

- conductor weights;
- arc widths;
- height localization;
- Mellin decay;
- Gauss-sum weights.

It therefore suggested that a weighted theorem might permit some zeros closer to one without requiring a uniform Dirichlet fixed strip.

Paper 03 refines that statement.

For nonprincipal characters, this opening remains valid.

For the complete positive EMAE gate, however, the $q=1$ zeta packet has:

```text
conductor weight = 1
character averaging = none
Gauss-sum discount = none
fixed nonzero Mellin coefficient per zero
```

Therefore:

$$
\boxed{
\text{weighted character flexibility}
\neq
\text{principal zeta flexibility}.
}
$$

Any full positive EMAE theorem still contains a fixed zeta zero-strip theorem as a necessary subresult.

---

# 16. Campaign 02 candidate audit

## Candidate C02-A — Density + conductor + height boxes

```text
status:
  REJECTED_AS_FULL_EMAE_BYPASS

reason:
  useful for q>1 boxes;
  cannot discharge q=1 ZPPF
```

## Candidate C02-B — Nonexceptional-modulus prime exponential-sum improvement

```text
status:
  REJECTED_AS_PRINCIPAL_CORE_BYPASS

reason:
  q=1 core has B=O(1);
  N/B^(1/2) term retains N-scale
```

## Candidate C02-C — Deuring–Heilbronn exceptional-zero repulsion

```text
status:
  PARTIAL / NONPRINCIPAL ONLY

reason:
  does not solve q=1 zeta packet
```

## Candidate C02-D — Positive conductor / height reweighting

```text
status:
  REJECTED_IF_q1_WEIGHT_IS_x^(-o(1))

certificate:
  Theorem 7.1
```

## Candidate C02-E — Remove / subtract the principal zeta packet

```text
status:
  REJECTED_WITHOUT_TARGET_FIDELITY_BRIDGE

reason:
  deleting the blocker from the sufficient gate is not closure
  unless the resulting gate still controls the original prime-pair target
```

## Candidate C02-F — Direct zeta fixed-strip arithmetic theorem

```text
status:
  VALID TARGET
strength:
  BREAKTHROUGH_LEVEL

comment:
  not a simplification;
  exactly the required new mathematics
```

## Candidate C02-G — Signed principal mismatch / non-positive gate

```text
status:
  SURVIVOR

reason:
  Theorem 7.1 blocks positive gates retaining q=1,
  but does not rule out a genuinely signed target-faithful cancellation mechanism.

proof status:
  OPEN
```

---

# 17. Campaign 02 closure verdict

Campaign 02 asked:

> find the weakest genuinely arithmetic theorem that yields EMAE $(\eta)$ for some fixed $\eta>0$.

The result is:

```text
DIRECT FULL EMAE BY CURRENT CHARACTER-FAMILY TECHNOLOGY
= NOT CLOSED

PRINCIPAL NECESSARY SUBGATE
= EXACTLY IDENTIFIED

q=1 POSITIVE GATE STRENGTH
= EXACTLY FIXED ZERO STRIP

CURRENT DENSITY / CONDUCTOR / HEIGHT / REPULSION INPUTS
= INSUFFICIENT TO BYPASS q=1

SIGNED TARGET-FAITHFUL ALTERNATIVE
= SURVIVOR / OPEN
```

Therefore Campaign 02 is closed as a reduction and no-go audit.

It is not closed as a proof of EMAE.

---

# 18. New canonical frontier object

Create:

```text
F-RH-005
PRINCIPAL_ZETA_PACKET_FIXED_POWER
abbrev:
  ZPPF
status:
  OPEN
type:
  EXACT_EQUIVALENCE_FRONTIER
```

For fixed $\eta$:

$$
\boxed{
F\text{-}RH\text{-}005(\eta)
\Longleftrightarrow
\Theta_\zeta
\le
1-\frac{\eta}{2}.
}
$$

This frontier is intentionally marked as an exact-equivalence frontier.

It is not advertised as an easier reformulation.

---

# 19. New obstruction

Create:

```text
O-RH-006
POSITIVE_GATE_PRINCIPAL_NO_BYPASS
status:
  CERTIFIED
```

Statement:

> Any positive fixed-power sufficient gate which retains the $q=1$ principal zeta packet with only subpolynomial loss already contains a fixed zeta zero-strip theorem.

This obstruction applies to:

```text
positive character-family energies
positive conductor reweightings
positive height reweightings
positive large-sieve envelopes
positive zero-density envelopes
```

whenever they retain the principal packet at $x^{-o(1)}$ strength.

---

# 20. New survivor

Create:

```text
S-RH-008
SIGNED_TARGET_FAITHFUL_PRINCIPAL_GATE
status:
  OPEN / SURVIVOR
```

The survivor asks whether the original prime-pair target admits a sufficient gate that:

1. preserves the actual signed structure;
2. does not dominate $\mathcal E_\zeta$ as a positive summand;
3. still controls the target pair-spectrum deviation;
4. has a weaker fixed-power strength profile than ZPPF;
5. does not subtract zeta zeros by assumption;
6. does not insert RH into the model.

This is not known to exist.

It is the only structural bypass left by the present positive-gate audit.

---

# 21. Campaign 03 — Principal Gate Minimality Audit

The next worker campaign is:

```text
CSM_RH Campaign 03
PRINCIPAL_GATE_MINIMALITY
```

Primary question:

> Is the current positive $q=1$ energy gate stronger than necessary for the actual prime-pair target, or is every target-faithful fixed-power principal gate still forced to have zero-strip strength?

This is a gate-design question before it is a new estimate question.

---

# 22. Campaign 03 candidate families

Workers may generate candidates from:

```text
A
SIGNED PRINCIPAL MISMATCH

B
LINEARIZED POLE-RESIDUAL OBSERVABLE

C
POLARIZED CROSS-CORRELATION

D
SCALE-FREQUENCY SIGNED TRANSFORM

E
DIRECT PAIR-SPECTRUM DIFFERENCE WITHOUT POSITIVE DOMINATION

F
CERTIFIED CANCELLATION BETWEEN PRINCIPAL SUBTERMS
```

These are search classes, not theorem claims.

---

# 23. Campaign 03 rejection tests

Every candidate must answer:

## T1. Target fidelity

Does the proposed gate still imply the original prime-pair / pair-spectrum target?

## T2. Principal retention

Has the zeta packet merely been deleted, renamed, or assumed small?

## T3. Hidden positivity

Does the proof eventually dominate a positive object containing

$$
x^{-o(1)}
\mathcal E_\zeta?
$$

If yes, `O-RH-006` applies.

## T4. Hidden fixed strip

Does any intermediate estimate already imply

$$
\Theta_\zeta
\le1-\delta
$$

for fixed $\delta>0$?

If yes, classify it honestly as breakthrough-strength.

## T5. Signed cancellation certificate

If cancellation is used, is it structurally forced or only heuristic?

## T6. Quantifier audit

Does the argument work uniformly as

$$
x\to\infty
$$

for all fixed zero witnesses?

## T7. Supremum audit

Does it avoid assuming that $\Theta_\zeta$ is attained?

---

# 24. Worker architecture

`CSM_RH` remains the protocol.

GLM-5.3-Flash may be used as a current high-volume worker provider.

Canonical roles:

```text
Designer
Builder
Verifier
```

The provider remains replaceable.

Worker agreement is not theorem authority.

Campaign artifacts must be promoted only after:

```text
strength audit
target-fidelity audit
counterexample attempt
quantifier audit
independent frontier review
```

---

# 25. External evidence snapshot

As of 2026-09-05:

## Maynard–Pandey–Radziwiłł

`Exponential sums over primes`, arXiv:2608.14777, submitted 2026-08-14.

Main current pointwise estimate:

$$
|S_N(\alpha)|
\le
N^{o(1)}
\left(
\frac{N}{B^{1/2}}
+
N^{19/24}
\right).
$$

The authors explicitly interpret the first term morally as reflecting possible exceptional zeros close to one.

## Guth–Maynard

`New large value estimates for Dirichlet polynomials`, Annals of Mathematics 203 (2026), 623–675.

Zero-density consequence:

$$
N(\sigma,T)
\le
T^{30(1-\sigma)/13+o(1)}.
$$

## Chen–Gupta–Li

`Large Value Estimates for Dirichlet Polynomials with Characters and Zero Density of Dirichlet L-Functions`, arXiv:2507.08296v2, revised 2026-07-27.

Character-family zero-density estimate:

$$
\sum_{\chi\bmod q}
N(\sigma,T,\chi)
\ll_\varepsilon
(qT)^{7(1-\sigma)/3+\varepsilon}.
$$

## Bellotti–Trudgian–Yang

`Zero-free regions inspired by work of Heath-Brown`, arXiv:2603.21490.

Explicit region:

$$
\sigma
\ge
1-\frac{1}{4.896\log t},
\qquad
t\ge3.
$$

## Benli–Goel–Twiss–Zaman

`Explicit Deuring-Heilbronn phenomenon for Dirichlet L-functions`, arXiv:2410.06082v3, revised 2026-01-08.

Scope:

```text
Landau-Siegel-zero conditional repulsion
for Dirichlet L-functions modulo q
```

These results are external inputs or consistency checks only.

None is promoted here into a fixed zeta zero strip.

---

# 26. State transition

The canonical transition is:

```text
CSM_RH v0.3
  ->
CSM_RH v0.4
```

with:

```text
Campaign 02:
  CLOSED_AS_REDUCTION_AUDIT

F-RH-003:
  EMAE
  OPEN
  but now has certified necessary subgate F-RH-005

F-RH-005:
  PRINCIPAL_ZETA_PACKET_FIXED_POWER
  CREATED
  OPEN / EXACT_EQUIVALENCE_FRONTIER

O-RH-006:
  POSITIVE_GATE_PRINCIPAL_NO_BYPASS
  CREATED / CERTIFIED

S-RH-008:
  SIGNED_TARGET_FAITHFUL_PRINCIPAL_GATE
  CREATED / OPEN

next:
  Campaign 03
  PRINCIPAL_GATE_MINIMALITY
```

---

# 27. Final status

```text
RH = OPEN

MAJOR-ARC PACKET GLOBALIZATION
= CLOSED_AT_EXPONENTIAL_TYPE

FULL POSITIVE EMAE
= OPEN

q=1 PRINCIPAL POSITIVE FIXED POWER
= EXACTLY EQUIVALENT TO A FIXED ZETA ZERO STRIP

CURRENT CHARACTER-FAMILY ADVANCES
= DO NOT BYPASS q=1

POSITIVE-GATE BYPASS
= CLOSED / NO

SIGNED TARGET-FAITHFUL BYPASS
= OPEN / SURVIVOR

NEXT CAMPAIGN
= PRINCIPAL_GATE_MINIMALITY
```

The central result is:

$$
\boxed{
\operatorname{ZPPF}(\eta)
\Longleftrightarrow
\Theta_\zeta
\le
1-\frac{\eta}{2}.
}
$$

and therefore:

$$
\boxed{
\operatorname{EMAE}(\eta)
\Longrightarrow
\Theta_\zeta
\le
1-\frac{\eta}{2}.
}
$$

The remaining design choice is now explicit:

> either prove genuinely new fixed-strip mathematics, or abandon the current positive-dominating principal gate and prove that a weaker signed target-faithful gate is sufficient.

That is the canonical output of Campaign 02.
