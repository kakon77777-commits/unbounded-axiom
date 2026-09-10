# CSM_RH Paper 70

## Boundary-Mode Concentration in the Shift Mean, Centering Attenuation, and Closure of the Original Hankel-Coercivity Guess

**Project:** CSM_RH  
**Paper:** 70  
**Version:** v0.1  
**Date:** 2026-09-09  
**Campaign:** 46 — `SEEDED_ARITHMETIC_STRIP_GAP_GENERATION`  
**Auxiliary tracks:** F-RH-020 / F-RH-021  
**Canonical root frontier:** F-RH-017-v3  
**Status:** ORIGINAL CENTERED HANKEL COERCIVITY TARGET CORRECTED / SIGNED PRIME-SAMPLING BRIDGE REMAINS UNPROVED / AUXILIARY ROUTE DE-PRIORITIZED  
**Canonical entry state:** v1.60 / Paper 69 v0.1  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 69 proposed a possible root bridge:

if a zeta zero lies on the seed boundary

$$
\rho=1-d+i\gamma,
\qquad
d=\frac{\kappa}{2},
$$

then perhaps the centered shifted-prime Möbius Hankel variance satisfies

$$
V_2(X,H)
\gg
H\pi(X)^2X^{-2d-o(1)}.
$$

The present paper tests this conjecture on the canonical smooth Mertens boundary mode and shows that the target is too strong.

Let

$$
\beta=\Re\rho=1-d
$$

and define the synthetic Mertens mode

$$
M_\rho(x)=x^\rho.
$$

Its discrete density is

$$
\boxed{
m_\rho(n)
=
n^\rho-(n-1)^\rho.
}
$$

Sample this density at the actual rational primes:

$$
\boxed{
C_{\rho,X}(h)
=
\sum_{p\le X}
m_\rho(p+h).
}
$$

The prime number theorem implies

$$
\boxed{
C_{\rho,X}(0)
=
\frac{X^\rho}{\log X}
\left(
1+o_\rho(1)
\right).
}
$$

More importantly, if

$$
h\to\infty,
\qquad
h=o(X),
$$

then

$$
\boxed{
C_{\rho,X}(h)
-
C_{\rho,X}(0)
=
-
\frac{h^\rho}{\log h}
\left(
1+o_\rho(1)
\right).
}
$$

Thus the boundary mode is sampled by the primes as

$$
\boxed{
C_{\rho,X}(h)
=
A_\rho(X)
-
B_\rho(h)
+
\text{lower order},
}
$$

with

$$
A_\rho(X)
\asymp
\frac{X^\rho}{\log X},
$$

$$
B_\rho(h)
\asymp
\frac{h^\rho}{\log h}.
$$

For a near-macroscopic shift range

$$
H=X^{1-\tau},
$$

the $X$ -scale term dominates the $H$ -scale variation by the fixed factor

$$
X^{\beta\tau+o(1)}.
$$

Consequently,

$$
\boxed{
\sum_{h\le H}
C_{\rho,X}(h)
=
H
\frac{X^\rho}{\log X}
\left(
1+o_\rho(1)
\right).
}
$$

The uncentered shift mean therefore retains the critical boundary amplitude:

$$
\boxed{
H
\left|
\frac1H
\sum_{h\le H}C_{\rho,X}(h)
\right|^2
\asymp
H\pi(X)^2
X^{-2d}.
}
$$

But centering removes precisely this dominant component.

Let

$$
\overline C_{\rho,X}
=
\frac1H
\sum_{h\le H}
C_{\rho,X}(h).
$$

Then

$$
\boxed{
V_{2,\rho}(X,H)
:=
\sum_{h\le H}
|C_{\rho,X}(h)-\overline C_{\rho,X}|^2
\asymp_\rho
\frac{
H^{2\beta+1}
}{
\log^2H
}.
}
$$

Since

$$
\pi(X)
\sim
\frac{X}{\log X},
$$

this becomes

$$
\boxed{
V_{2,\rho}(X,H)
=
H\pi(X)^2
X^{-2[d+\tau(1-d)]+o(1)}.
}
$$

Define the centered effective exponent

$$
\boxed{
d_{\rm cent}
=
d+\tau(1-d).
}
$$

Then

$$
d_{\rm cent}>d
$$

for every fixed $\tau>0$.

Thus the smooth boundary mode does **not** support Paper 69's centered lower target

$$
V_2
\gg
H\pi(X)^2X^{-2d-o(1)}.
$$

Centering itself removes the critical boundary signal and leaves a strictly smaller variation.

The exponent

$$
d+\tau(1-d)
$$

is not new to the CSM_RH chain. It is exactly the anchor exponent which appeared in the corrected $L^1$ residue-chain theorem of Paper 61. The same geometry is reappearing in a different language:

```text
a multiplicative boundary mode is nearly constant
across a sublinear additive shift window;
subtracting the mean differentiates the mode
and gains a factor determined by H/X.
```

Therefore the original F-RH-021 is closed.

A more plausible bridge is the **uncentered signed mean**:

```text
F-RH-021R
SIGNED SHIFTED-PRIME BOUNDARY-SAMPLING COERCIVITY
```

Desired theorem for the actual Möbius function:

if

$$
\rho=1-d+i\gamma
$$

is a zeta boundary zero, then along an unbounded sequence of $X$,

$$
\boxed{
\left|
\sum_{h\le H}
\sum_{p\le X}
\mu(p+h)
\right|
\gg_\rho
H\pi(X)
X^{-d-o(1)}.
}
$$

The smooth boundary mode proves that this is the correct scaling.

If F-RH-021R were certified, then any F-RH-020 energy upper theorem with exponent

$$
\eta>d
$$

would imply by Cauchy-Schwarz

$$
\left|
\sum_{h\le H}C_X(h)
\right|
\ll
H\pi(X)X^{-\eta},
$$

contradicting the boundary lower bound.

However, F-RH-021R is presently unproved.

The reason is structural. Zeta zeros are Mellin-multiplicative singularities. The map

$$
\mu
\mapsto
\left(
h\mapsto
\sum_{p\le X}\mu(p+h)
\right)
$$

is an additive prime-sampling transform and has no known Mellin-diagonal pole-transport identity.

Recent work of Pintz proves that Mertens oscillation itself strongly reflects the largest zeta-zero term. This supports the existence of the boundary mode before sampling, but does not supply coercivity after additive prime sampling.

Current shifted-prime Möbius theorems prove averaged cancellation in the opposite direction. They do not prove that a hypothetical zeta boundary zero forces a large shifted-prime Möbius correlation.

Accordingly:

```text
F-RH-020:
remains a useful parity-energy auxiliary problem.

F-RH-021:
closed in its centered form.

F-RH-021R:
open high-cost bridge candidate, not certified.

canonical root attack:
return to F-RH-017-v3.
```

No RH theorem is claimed.

---

# 1. Synthetic boundary mode

Fix

$$
\rho=\beta+i\gamma,
\qquad
0<\beta<1.
$$

For the CSM_RH boundary calibration,

$$
\beta=1-d.
$$

Define

$$
\boxed{
M_\rho(x)=x^\rho
}
$$

and its discrete increment

$$
\boxed{
m_\rho(n)
=
n^\rho-(n-1)^\rho.
}
$$

Taylor expansion gives

$$
\boxed{
m_\rho(n)
=
\rho n^{\rho-1}
+
O_\rho(n^{\beta-2}).
}
$$

The remainder is absolutely summable over primes.

---

# 2. Prime sampling of the smooth mode

Define

$$
\boxed{
C_{\rho,X}(h)
=
\sum_{p\le X}
m_\rho(p+h).
}
$$

Using Section 1,

$$
C_{\rho,X}(h)
=
\rho
\sum_{p\le X}
(p+h)^{\rho-1}
+
O_\rho(1+h^{\beta-1}).
$$

For $h=0$, partial summation with the prime number theorem gives

$$
\sum_{p\le X}
p^{\rho-1}
=
\frac{
X^\rho
}{
\rho\log X
}
\left(
1+o_\rho(1)
\right).
$$

Hence:

## Theorem 2.1 — Critical prime-sampled constant mode

$$
\boxed{
C_{\rho,X}(0)
=
\frac{
X^\rho
}{
\log X
}
\left(
1+o_\rho(1)
\right).
}
$$

Create:

```text
B-RH-096
SMOOTH_MERTENS_BOUNDARY_MODE_HAS_CRITICAL_PRIME_SAMPLED_SHIFT_CONSTANT_COMPONENT
CERTIFIED_MODEL_THEOREM
```

---

# 3. Shift variation asymptotic

Consider

$$
C_{\rho,X}(h)-C_{\rho,X}(0).
$$

At the principal smooth level,

$$
\rho
\sum_{p\le X}
\left[
(p+h)^{\rho-1}
-
p^{\rho-1}
\right].
$$

The prime number theorem reduces this, with an error smaller than the displayed main term, to

$$
\rho
\int_2^X
\frac{
(t+h)^{\rho-1}
-
t^{\rho-1}
}{
\log t
}\,dt.
$$

Scale

$$
t=hu.
$$

Then

$$
\frac{\log h}{h^\rho}
\int_2^X
\frac{
(t+h)^{\rho-1}
-
t^{\rho-1}
}{
\log t
}\,dt
$$

tends to

$$
\int_0^\infty
\left[
(1+u)^{\rho-1}
-
u^{\rho-1}
\right]du.
$$

But

$$
\begin{aligned}
\int_0^R
\left[
(1+u)^{\rho-1}
-
u^{\rho-1}
\right]du
&=
\frac{
(R+1)^\rho-R^\rho-1
}{
\rho
}
\\
&\longrightarrow
-\frac1\rho.
\end{aligned}
$$

Therefore:

## Theorem 3.1 — Boundary-mode shift variation

If

$$
h\to\infty,
\qquad
h=o(X),
$$

then

$$
\boxed{
C_{\rho,X}(h)
-
C_{\rho,X}(0)
=
-
\frac{
h^\rho
}{
\log h
}
\left(
1+o_\rho(1)
\right).
}
$$

Create:

```text
B-RH-097
PRIME_SAMPLED_SMOOTH_BOUNDARY_MODE_VARIES_ONLY_AT_THE_H_SCALE
CERTIFIED_MODEL_THEOREM
```

---

# 4. Signed shift mean retains the critical boundary scale

Let

$$
H=X^{1-\tau},
\qquad
0<\tau<1.
$$

Sum Theorem 3.1 over

$$
h\le H.
$$

Standard power summation gives

$$
\sum_{h\le H}
\frac{h^\rho}{\log h}
=
\frac{
H^{\rho+1}
}{
(\rho+1)\log H
}
\left(
1+o_\rho(1)
\right).
$$

This has magnitude

$$
H^{\beta+1}/\log H.
$$

The constant-mode contribution has magnitude

$$
H X^\beta/\log X.
$$

Their ratio is

$$
\boxed{
\left(
\frac HX
\right)^\beta
\frac{\log X}{\log H}
=
X^{-\beta\tau+o(1)}
\to0.
}
$$

Hence:

## Theorem 4.1 — Signed mean boundary retention

$$
\boxed{
\sum_{h\le H}
C_{\rho,X}(h)
=
H
\frac{
X^\rho
}{
\log X
}
\left(
1+o_\rho(1)
\right).
}
$$

Since

$$
\pi(X)\sim X/\log X,
$$

$$
\boxed{
\left|
\sum_{h\le H}
C_{\rho,X}(h)
\right|
\asymp_\rho
H\pi(X)X^{-(1-\beta)}.
}
$$

At the PESC boundary,

$$
1-\beta=d.
$$

Thus the smooth model supports F-RH-021R at exactly the critical exponent $d$.

---

# 5. Centered variance attenuates the boundary mode

Define

$$
\overline C_{\rho,X}
=
\frac1H
\sum_{h\le H}
C_{\rho,X}(h).
$$

The $X$ -dependent constant cancels from

$$
C_{\rho,X}(h)-\overline C_{\rho,X}.
$$

Thus the leading centered profile is

$$
-
\frac{h^\rho}{\log h}
+
\frac1H
\sum_{j\le H}
\frac{j^\rho}{\log j}.
$$

Rescale

$$
h=Hu.
$$

Then the variance is asymptotic to

$$
\frac{
H^{2\beta+1}
}{
\log^2 H
}
$$

times the positive constant

$$
\boxed{
\mathfrak c_\rho
=
\int_0^1
\left|
u^\rho
-
\frac1{\rho+1}
\right|^2du.
}
$$

The constant simplifies to

$$
\boxed{
\mathfrak c_\rho
=
\frac1{2\beta+1}
-
\frac1{|\rho+1|^2}
>0.
}
$$

Hence:

## Theorem 5.1 — Centered smooth-mode Hankel scale

$$
\boxed{
V_{2,\rho}(X,H)
\sim_\rho
\mathfrak c_\rho
\frac{
H^{2\beta+1}
}{
\log^2H
}.
}
$$

Create:

```text
B-RH-098
CENTERING_ATTENUATES_THE_SMOOTH_BOUNDARY_MODE_TO_H_SCALE_VARIANCE
CERTIFIED_MODEL_THEOREM
```

---

# 6. Effective centered exponent

## Theorem 6.1 — Centered effective exponent

At

$$
\beta=1-d
$$

and

$$
H=X^{1-\tau},
$$

$$
H^{2\beta+1}
=
H
X^{2\beta(1-\tau)}.
$$

Using

$$
H\pi(X)^2
=
H
X^2
\log^{-2}X
(1+o(1)),
$$

we obtain

$$
\boxed{
V_{2,\rho}(X,H)
=
H\pi(X)^2
X^{-2d_{\rm cent}+o(1)},
}
$$

where

$$
\boxed{
d_{\rm cent}
=
d+\tau(1-d).
}
$$

Thus

$$
\boxed{
d_{\rm cent}>d.
}
$$

The centered boundary signal is strictly smaller than the uncentered critical signal.

---

# 7. Reappearance of the Paper-61 anchor exponent

Paper 61's corrected $L^1$ exceptional amplifier had the anchor term

$$
\boxed{
d+\tau(1-d).
}
$$

Theorem 6.1 produces exactly the same exponent.

This is not a coincidence.

A multiplicative mode

$$
x^{1-d+i\gamma}
$$

changes only by a relative amount controlled by

$$
H/X
$$

over a sublinear additive shift window.

Subtracting its shift mean removes the zeroth-order part.

What remains is its sublinear variation.

Thus the same exponent appears in:

- residue-chain anchoring;
- long-scale comparison;
- centered prime-sampled Mertens variance.

This is a common critical-locking geometry.

---

# 8. Correction to F-RH-021

Paper 69 proposed:

```text
F-RH-021
BOUNDARY MERTENS MODE PRIME-SAMPLING HANKEL COERCIVITY
```

with desired lower scale

$$
V_2
\gg
H\pi(X)^2X^{-2d-o(1)}.
$$

The smooth boundary mode itself has only

$$
H\pi(X)^2
X^{-2[d+\tau(1-d)]+o(1)}.
$$

Therefore the old target is not supported even by the canonical residue mode.

Record:

```text
C-RH-004
PAPER69_CENTERED_F_RH_021_CRITICAL_LOWER_SCALE_CORRECTED
```

and

```text
O-RH-160
CENTERED_HANKEL_CRITICAL_LOWER_BOUND_X_MINUS_2D_IS_TOO_STRONG_FOR_THE_SMOOTH_BOUNDARY_MODE
CERTIFIED_MODEL_BARRIER
```

Close the original F-RH-021 formulation.

---

# 9. Revised bridge candidate F-RH-021R

The smooth mode shows that the critical signal survives in the **uncentered signed mean**.

Open only as a high-cost auxiliary bridge candidate:

```text
F-RH-021R
SIGNED_SHIFTED_PRIME_BOUNDARY_SAMPLING_COERCIVITY
```

Desired theorem for the actual Möbius function:

if

$$
\rho=1-d+i\gamma
$$

is a zeta zero on the seed boundary, then along an unbounded sequence of $X$,

$$
\boxed{
\left|
\sum_{h\le H}
\sum_{p\le X}
\mu(p+h)
\right|
\gg_\rho
H\pi(X)
X^{-d-o(1)}.
}
$$

The smooth model proves only that this scale is natural.

It does not prove the theorem for $\mu$.

---

# 10. How F-RH-020 would become a root theorem if F-RH-021R held

Suppose F-RH-020 gave

$$
\boxed{
E_2(X,H)
\ll
H\pi(X)^2X^{-2\eta}
}
$$

with

$$
\eta>d.
$$

Then Cauchy gives

$$
\begin{aligned}
\left|
\sum_{h\le H}C_X(h)
\right|
&\le
H^{1/2}
E_2(X,H)^{1/2}
\\
&\ll
\boxed{
H\pi(X)X^{-\eta}.
}
\end{aligned}
$$

If F-RH-021R also held, this would contradict a boundary zero.

Thus:

```text
F-RH-020 with eta>d
+
F-RH-021R
= genuine root strip improvement.
```

But the bridge remains unproved.

---

# 11. Why zeta zeros do not automatically transport through additive prime sampling

The Mellin transform of $M(x)$ is directly tied to

$$
1/\zeta(s).
$$

A zero of zeta therefore creates a Mellin singularity and forces Mertens oscillation.

By contrast,

$$
\sum_{p\le X}\mu(p+h)
$$

is an additive correlation.

For fixed $h$, the Dirichlet series

$$
\sum_p
\frac{\mu(p+h)}{p^s}
$$

has no known Euler-product or Mellin-diagonal identity in terms of $\zeta$.

Likewise, the shift-averaged transform

$$
\sum_{h\le H}\sum_{p\le X}\mu(p+h)
$$

is not a Dirichlet convolution observable.

Therefore there is no formal pole-transport theorem analogous to

$$
\Lambda=\mu*\log.
$$

Create:

```text
O-RH-161
ZETA_MELLIN_POLE_HAS_NO_FORMAL_TRANSPORT_IDENTITY_TO_ADDITIVE_SHIFTED_PRIME_MOBIUS_SAMPLING
CERTIFIED_AS_BRIDGE_BARRIER
```

This is a statement about the current structural identities, not a proof that F-RH-021R is false.

---

# 12. External Mertens oscillation calibration

Recent work of Pintz studies the oscillation of

$$
M(x)=\sum_{n\le x}\mu(n)
$$

and shows that the average modulus of $M(x)$ closely tracks the largest zeta-zero term.

This strengthens the calibration that a rightmost zeta zero genuinely produces a large Mertens boundary component.

However, the theorem concerns $M(x)$ itself.

It does not prove that the same component survives an additive prime-sampling operator with a quantitative lower bound.

Thus the present bridge gap is real:

```text
Mellin boundary forcing:
strongly understood.

additive prime-sampling coercivity:
not established.
```

---

# 13. Relation to shifted-prime Möbius upper theorems

Lichtman proves strong cancellation of

$$
\sum_{p\le X}\mu(p+h)
$$

on average over shifts.

This is an upper theorem.

It does not give a converse saying that a zeta zero near a fixed boundary forces this correlation to be large.

Hence existing shifted-prime technology and existing Mertens oscillation technology point in opposite directions but do not currently meet in a coercive equivalence.

---

# 14. Strategic status of F-RH-020

F-RH-020 remains mathematically meaningful:

$$
E_2
\ll
H\pi(X)^2X^{-2\eta}
$$

would be a strong fixed-power parity theorem.

But without F-RH-021R it has no certified root implication.

Moreover, the exponent required for a root contradiction would be

$$
\eta>d,
$$

which is stronger than the subcritical energy exponents previously considered.

Therefore:

```text
F-RH-020:
retain as auxiliary parity frontier,
de-prioritize as RH root route.

F-RH-021 original centered bridge:
close.

F-RH-021R:
open high-cost bridge candidate,
not canonical.

F-RH-017-v3:
resume as canonical root frontier.
```

---

# 15. Recommended return to the root problem

The direct root observable

$$
U_H(x)
=
\psi(x+H)-\psi(x)-H
$$

has one decisive advantage over the prime–Möbius auxiliary observable:

a zeta boundary zero is known to act on it directly through the explicit formula.

Papers 55, 60 and 61 already certified the critical boundary amplitude and exceptional-set forcing geometry there.

Thus the next root attack should return to:

$$
\boxed{
\text{F-RH-017-v3}
}
$$

and seek genuinely prime-side low-frequency suppression of

$$
U_H
$$

rather than first passing through shifted Möbius sampling.

This avoids the unproved additive pole-transport bridge.

---

# 16. External calibration

## 16.1. Pintz 2026 Mertens oscillation

J. Pintz,
*Oscillation of partial sums of the Möbius function and zeros of Riemann's zeta function*,
arXiv:2608.24878, August 2026.

The paper relates the average modulus of $M(x)$ closely to the largest zeta-zero contribution.

URL:

https://arxiv.org/abs/2608.24878

## 16.2. Lichtman shifted-prime Möbius theorem

J. D. Lichtman,
*Averages of the Möbius Function on Shifted Primes*,
Quarterly Journal of Mathematics 73 (2022), 729–757.

The paper proves averaged shifted-prime Möbius cancellation, but no converse zero-to-correlation lower theorem.

URL:

https://academic.oup.com/qjmath/article/73/2/729/6446139

---

# 17. State transition

Advance candidate state

$$
v1.60
\to
v1.61.
$$

Add:

```text
B-RH-096
SMOOTH_MERTENS_BOUNDARY_MODE_HAS_CRITICAL_PRIME_SAMPLED_SHIFT_CONSTANT_COMPONENT
CERTIFIED_MODEL_THEOREM

B-RH-097
PRIME_SAMPLED_SMOOTH_BOUNDARY_MODE_VARIES_ONLY_AT_THE_H_SCALE
CERTIFIED_MODEL_THEOREM

B-RH-098
CENTERING_ATTENUATES_THE_SMOOTH_BOUNDARY_MODE_TO_H_SCALE_VARIANCE
CERTIFIED_MODEL_THEOREM

O-RH-160
CENTERED_HANKEL_CRITICAL_LOWER_BOUND_X_MINUS_2D_IS_TOO_STRONG_FOR_THE_SMOOTH_BOUNDARY_MODE
CERTIFIED_MODEL_BARRIER

O-RH-161
ZETA_MELLIN_POLE_HAS_NO_FORMAL_TRANSPORT_IDENTITY_TO_ADDITIVE_SHIFTED_PRIME_MOBIUS_SAMPLING
CERTIFIED_AS_BRIDGE_BARRIER

C-RH-004
PAPER69_CENTERED_F_RH_021_CRITICAL_LOWER_SCALE_CORRECTED
```

Close:

```text
F-RH-021
CLOSED_IN_ORIGINAL_CENTERED_FORM
```

Open only as noncanonical bridge candidate:

```text
F-RH-021R
SIGNED_SHIFTED_PRIME_BOUNDARY_SAMPLING_COERCIVITY
OPEN_HIGH_COST
```

Canonical next target:

```text
F-RH-017-v3
```

No RH certificate is created.

---

# 18. Conclusion

The smooth Mertens boundary mode survives prime sampling, but almost entirely as a shift-constant component.

The critical signal has relative size

$$
X^{-d}.
$$

Centering removes it.

The residual centered variance has the strictly smaller scale

$$
X^{-2[d+\tau(1-d)]}.
$$

Therefore the centered Hankel variance is the wrong place to demand critical boundary coercivity.

A root bridge would have to preserve and control the signed shift mean.

No theorem currently transports a zeta Mellin pole through that additive prime-sampling operator.

The shifted-prime Möbius energy route remains an interesting parity problem, but it is no longer the shortest certified path to the RH frontier.

Campaign 46 should return to F-RH-017-v3.
