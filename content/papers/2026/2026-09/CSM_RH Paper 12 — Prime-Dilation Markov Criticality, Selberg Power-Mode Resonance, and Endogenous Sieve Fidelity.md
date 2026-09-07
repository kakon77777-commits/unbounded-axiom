# CSM_RH Paper 12
## Prime-Dilation Markov Criticality, Selberg Power-Mode Resonance, and Endogenous Sieve Fidelity

**Project:** `CSM_RH`  
**Paper:** `12`  
**Version:** `v0.1`  
**Date:** `2026-09-05`  
**Parent state:** `CSM_RH v1.2 / Paper 11`  
**Campaign:** `11 — ENDOGENOUS_PRIME_SAMPLING_MECHANISM`  
**Status:** operator / sieve-mechanism audit; not a proof or disproof of RH

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

The paper audits four mechanism families for the prime-error self-correlation target:

```text
refined Selberg feedback
signed sieve approximation
scale-local recurrence
direct prime correlation
```

No fixed-power estimate is proved.

The main closure gain is the identification of two precise mechanism barriers:

1. the normalized Selberg prime-dilation operator is Markov-critical at positive/absolute-value level;
2. a sieve approximation must be target-faithful against the endogenous prime-error weight, which requires parity-breaking bilinear information beyond ordinary sieve control.

No live GLM-5.3-Flash run is claimed.

---

# 1. Canonical prime-error core

Define

$$
q_n
=
\log n\,
\mathbf1_{\mathbb P}(n),
$$

$$
c_n
=
q_n-1,
$$

and

$$
B(j)
=
\vartheta(j)-j.
$$

Paper 11 defined

$$
\boxed{
\mathcal C_N^\vartheta
=
\sum_{n<2N}
w_N(n)c_nB(n-1)
}
$$

and proved

$$
\boxed{
J_N^\vartheta
=
D_N^\vartheta
+
2\mathcal C_N^\vartheta,
}
$$

with

$$
D_N^\vartheta
=
O(N^2\log N).
$$

Thus for fixed

$$
0<\kappa\le1,
$$

$$
\boxed{
\operatorname{PESC}(\kappa)
\Longleftrightarrow_{\rm exponent}
J_N^\vartheta
\ll
N^{3-\kappa+o(1)}.
}
$$

The first fixed-strip target requires only

$$
0<\kappa<\frac12.
$$

---

# 2. Prime-only Selberg feedback

The prime-only Selberg symmetry formula is

$$
\vartheta(x)\log x
+
\sum_{p\le x}
\log p\,
\vartheta(x/p)
=
2x\log x
+
O(x).
$$

Let

$$
B(x)
=
\vartheta(x)-x.
$$

Using

$$
\sum_{p\le x}
\frac{\log p}{p}
=
\log x
+
O(1),
$$

we obtain

$$
\boxed{
B(x)\log x
+
\sum_{p\le x}
\log p\,
B(x/p)
=
O(x).
}
$$

This is the prime-only error feedback equation.

---

# 3. Relative-error normalization

Define the relative prime error

$$
\boxed{
R(x)
=
\frac{B(x)}{x}.
}
$$

Then

$$
B(x/p)
=
\frac{x}{p}
R(x/p).
$$

Dividing Section 2 by $x$ gives

$$
\boxed{
R(x)\log x
+
\sum_{p\le x}
\frac{\log p}{p}
R(x/p)
=
O(1).
}
$$

Define

$$
L(x)
=
\sum_{p\le x}
\frac{\log p}{p}.
$$

Then

$$
L(x)
=
\log x+O(1).
$$

Define the normalized prime-dilation operator

$$
\boxed{
(\mathcal P_xf)
=
\frac1{L(x)}
\sum_{p\le x}
\frac{\log p}{p}
f(x/p).
}
$$

Its weights are nonnegative and have total mass one.

Therefore the normalized Selberg equation is

$$
\boxed{
R(x)
+
\frac{L(x)}{\log x}
\mathcal P_xR
=
O
\left(
\frac1{\log x}
\right).
}
$$

---

# 4. Prime-Dilation Markov Criticality

Because the weights of $\mathcal P_x$ are nonnegative and sum to one,

$$
\boxed{
|\mathcal P_xf|
\le
\mathcal P_x|f|.
}
$$

Also, by Jensen,

$$
\boxed{
|\mathcal P_xf|^2
\le
\mathcal P_x|f|^2.
}
$$

Hence the positive operator has norm one in the basic sup and pointwise Jensen senses.

Since

$$
\frac{L(x)}{\log x}
=
1
+
O
\left(
\frac1{\log x}
\right),
$$

the direct positive closure of the Selberg equation has no fixed contraction factor below one.

Create:

```text
O-RH-024
PRIME_DILATION_MARKOV_CRITICALITY
status:
  CERTIFIED
```

Statement:

> The normalized prime-dilation operator in the classical Selberg feedback has asymptotic mass one. Triangle inequality or Jensen alone cannot produce a fixed multiplicative contraction.

This does not exclude a signed spectral or nonlinear contraction theorem.

---

# 5. Power-mode calibration

For fixed

$$
0<\delta<1,
$$

consider the model relative error

$$
\boxed{
R_\delta(x)
=
x^{-\delta}.
}
$$

This corresponds formally to an absolute error of power size

$$
B_\delta(x)
=
x^{1-\delta}.
$$

The prime-dilation term is

$$
\begin{aligned}
\sum_{p\le x}
\frac{\log p}{p}
R_\delta(x/p)
&=
x^{-\delta}
\sum_{p\le x}
\log p\,
p^{\delta-1}.
\end{aligned}
$$

The prime number theorem and partial summation give

$$
\boxed{
\sum_{p\le x}
\log p\,
p^{\delta-1}
=
\frac{x^\delta}{\delta}
+
o(x^\delta).
}
$$

Therefore:

## Theorem 5.1 — Selberg Power-Mode Response

For every fixed

$$
0<\delta<1,
$$

$$
\boxed{
\sum_{p\le x}
\frac{\log p}{p}
R_\delta(x/p)
=
\frac1\delta
+
o(1).
}
$$

Meanwhile,

$$
R_\delta(x)\log x
=
x^{-\delta}\log x
=
o(1).
$$

Hence the complete normalized Selberg left side is

$$
\boxed{
\frac1\delta
+
o(1),
}
$$

which is fully compatible with the classical

$$
O(1)
$$

forcing.

---

# 6. Constant mode versus power modes

For the constant relative-error mode

$$
R_0(x)=1,
$$

the normalized Selberg left side is

$$
\log x
+
L(x)
=
2\log x+O(1),
$$

which is not

$$
O(1).
$$

Thus the classical Selberg feedback can exclude a persistent nonzero constant relative error.

But Theorem 5.1 shows that it is directly compatible with every fixed decaying power mode

$$
x^{-\delta},
\qquad
\delta>0.
$$

Create:

```text
O-RH-025
SELBERG_POWER_MODE_RESONANCE
status:
  CERTIFIED_AS_MODE_RESOLUTION_CALIBRATION
```

Interpretation:

```text
relative error ~ constant
  resolved

relative error ~ x^(-delta), any fixed delta>0
  not resolved by O(1) forcing magnitude
```

This sharpens the direct-resolution obstruction from Paper 11.

---

# 7. Why a sharper Selberg residual is not automatically lower strength

Saidak proved for the $\psi$ version of Selberg's lemma that, after extracting an explicit linear secondary term, the remainder is bounded in terms of the PNT error itself:

$$
O
\left(
E(x)
(\log x)^2
\right),
$$

where

$$
E(x)
=
\psi(x)-x.
$$

This is an important strength calibration.

A power-accurate refinement of the Selberg residual may simply be another coordinate for a power-accurate PNT error.

This paper does not assert a new exact $\vartheta$ analogue of Saidak's theorem.

It uses the result only to enforce:

```text
SELBERG RESIDUAL STRENGTH MUST BE AUDITED
```

before a refined residual is treated as a low-strength input.

---

# 8. Generic signed sieve decomposition

Let

$$
\lambda_n
$$

be any chosen arithmetic approximation to

$$
q_n
=
\log n\,\mathbf1_{\mathbb P}(n).
$$

Define the detector residual

$$
\boxed{
r_n
=
q_n-\lambda_n.
}
$$

Then

$$
c_n
=
[
\lambda_n-1
]
+
r_n.
$$

Therefore PESC splits exactly as

$$
\boxed{
\mathcal C_N^\vartheta
=
\mathcal M_{\lambda,N}
+
\mathcal E_{\lambda,N},
}
$$

where

$$
\mathcal M_{\lambda,N}
=
\sum_{n<2N}
w_N(n)
[
\lambda_n-1
]
B(n-1),
$$

and

$$
\mathcal E_{\lambda,N}
=
\sum_{n<2N}
w_N(n)
r_nB(n-1).
$$

A sieve approximation is useful only if both terms are controlled.

---

# 9. Endogenous target-fidelity norm

Define

$$
\boxed{
\mathcal R_{\lambda,N}
=
\sum_{n<2N}
w_N(n)
|r_n|^2
}
$$

and

$$
\boxed{
\mathcal H_N
=
\sum_{n<2N}
w_N(n)
|B(n-1)|^2.
}
$$

Cauchy-Schwarz gives

$$
\boxed{
|\mathcal E_{\lambda,N}|
\le
\mathcal R_{\lambda,N}^{1/2}
\mathcal H_N^{1/2}.
}
$$

Using Chebyshev bounds,

$$
B(n)
=
O(n),
$$

and

$$
\sum_{n<2N}
w_N(n)
=
O(N^2),
$$

we obtain

$$
\boxed{
\mathcal H_N
=
O(N^4).
}
$$

Therefore:

## Proposition 9.1 — Generic $L^2$ detector-fidelity threshold

A sufficient condition for

$$
\mathcal E_{\lambda,N}
\ll
N^{3-\kappa+o(1)}
$$

through generic Cauchy closure is

$$
\boxed{
\mathcal R_{\lambda,N}
\ll
N^{2-2\kappa+o(1)}.
}
$$

This is a sufficient condition.

It is not claimed to be necessary.

---

# 10. Natural detector scale

For the trivial approximation

$$
\lambda_n=0,
$$

the detector energy is

$$
\mathcal R_{0,N}
=
\sum_{p<2N}
w_N(p)
(\log p)^2.
$$

The prime number theorem gives the natural scale

$$
\boxed{
\mathcal R_{0,N}
=
N^{2+o(1)}
\log N
}
$$

at exponent resolution.

Thus Proposition 9.1 requires a fixed-power improvement in the detector approximation whenever

$$
\kappa>0.
$$

This does not prove that no clever signed approximation can achieve it.

It shows that generic $L^2$ target-fidelity is itself a power-accurate prime-detection problem.

---

# 11. Why an upper-bound sieve is not enough

The PESC test function

$$
B(n-1)
$$

changes sign and is generated by the same prime sequence being detected.

Therefore a pointwise majorant

$$
q_n
\le
\lambda_n
$$

does not imply useful control of

$$
\sum_n
w_N(n)
[
\lambda_n-q_n
]
B(n-1).
$$

Likewise, an unweighted estimate for the total sieve error does not automatically control the endogenous weighted error.

Thus the required notion is not:

```text
prime majorization
```

but:

```text
signed endogenous target fidelity
```

---

# 12. Sieve parity calibration

Classical combinatorial and Selberg sieves face the parity problem: they cannot by their ordinary sieve information alone reliably distinguish primes from certain almost-prime configurations.

Friedlander and Iwaniec's asymptotic sieve for primes breaks this barrier by adding genuinely new analytic information in the form of a bilinear hypothesis.

This provides the correct calibration for the present route:

> if a sieve-based PESC proof exists, the decisive input must be parity-breaking arithmetic information beyond ordinary sieve majorization.

For the present endogenous target, that additional information must also remain valid against the weight

$$
B(n-1).
$$

Create the typed warning:

```text
O-RH-026
ENDOGENOUS_SIEVE_PARITY_FIDELITY
status:
  STRUCTURAL_WARNING / NOT UNIVERSAL NO-GO
```

It records the proof obligation without claiming a universal impossibility theorem.

---

# 13. Asymptotic-sieve comparison

The Friedlander-Iwaniec asymptotic sieve treats a nonnegative external sequence

$$
(a_n)
$$

and adds a bilinear condition strong enough to overcome parity and recover prime asymptotics.

The PESC sequence is qualitatively different:

$$
a_n^{\rm PESC}
=
w_N(n)
B(n-1)
$$

is signed and endogenous.

Direct application of a nonnegative asymptotic-sieve theorem is therefore not available without additional transformation.

Splitting

$$
B
=
B_+-B_-
$$

does not remove the difficulty, because one would then need distribution information for two prime-generated sequences.

Thus:

```text
ASYMPTOTIC SIEVE
  supplies the correct type of parity-breaking lesson

but

STANDARD ASYMPTOTIC SIEVE
  does not directly close PESC
```

---

# 14. Scale-local positive recurrence

The normalized Selberg relation can be written schematically as

$$
R(x)
=
-
[
1+o(1)
]
\mathcal P_xR
+
O
\left(
\frac1{\log x}
\right).
$$

Taking absolute values gives

$$
|R(x)|
\le
[
1+o(1)
]
\mathcal P_x|R|
+
O
\left(
\frac1{\log x}
\right).
$$

Because $\mathcal P_x$ has mass one, this is a critical recurrence.

Squaring and using Jensen gives the same conclusion at positive $L^2$ level.

Therefore a scale-local Selberg proof of a fixed power must use at least one of:

```text
signed cancellation inside the prime-dilation operator
a nonlinear contraction stronger than Jensen
a power-accurate residual
a multiscale mechanism with linear cumulative contraction mass
```

None is supplied by the classical positive closure.

---

# 15. Campaign 11 mechanism audit

## C11-S — refined Selberg operator

```text
status:
  CRITICAL

positive operator mass:
  1 + O(1/log x)

power-mode resolution:
  classical forcing compatible with every delta>0

fixed-power gain:
  NONE
```

Survives only if a new signed/nonlinear operator theorem is proved.

---

## C11-W — endogenous signed sieve

```text
status:
  OPEN TOOL

generic L2 fidelity:
  requires fixed-power detector approximation

ordinary upper-bound sieve:
  insufficient for signed endogenous target

parity-breaking input:
  required
```

No free fixed power is identified.

---

## C11-R — scale-local recurrence

```text
status:
  CRITICAL UNDER POSITIVE/JENSEN CLOSURE

fixed cumulative contraction mass:
  NOT OBTAINED
```

---

## C11-C — direct PESC theorem

```text
status:
  OPEN
  REMAINS THE CANONICAL CORE
```

---

# 16. Campaign 11 verdict

Campaign 11 does not close PESC.

It does close several possible claims of easy mechanism progress:

```text
CLASSICAL SELBERG POSITIVE OPERATOR GAP
  NO

CLASSICAL SELBERG POWER-MODE RESOLUTION
  NO FOR ANY FIXED DELTA>0

GENERIC SIEVE MAJORANT
  NO SIGNED TARGET FIDELITY

GENERIC L2 SIEVE CLOSURE
  REQUIRES POWER-ACCURATE PRIME DETECTOR

POSITIVE SCALE RECURRENCE
  CRITICAL
```

The remaining mechanism must be genuinely parity-breaking and endogenous.

---

# 17. New survivors

Create:

```text
S-RH-020
SIGNED_PRIME_DILATION_NONLINEAR_CONTRACTION
status:
  OPEN
```

Create:

```text
S-RH-021
ENDOGENOUS_PARITY_BREAKING_BILINEAR_INPUT
status:
  OPEN
```

Create:

```text
S-RH-022
POWER_ACCURATE_ENDOGENOUS_SIEVE_FIDELITY
status:
  OPEN
```

These are mechanism families.

They are not theorem claims.

---

# 18. New canonical mechanism frontier

Create:

```text
F-RH-011
ENDOGENOUS_PARITY_BREAKING_PRIME_FEEDBACK
abbrev:
  EPBPF
status:
  OPEN
type:
  MECHANISM FRONTIER
```

A valid EPBPF certificate must do at least one of:

## Mode A — signed prime-dilation contraction

Prove a noncircular contraction for the actual prime-generated relative error under the Selberg dilation operator.

## Mode B — parity-breaking bilinear sieve fidelity

Prove the required prime detector approximation against the endogenous weight through genuinely bilinear or parity-sensitive information.

## Mode C — direct PESC

Prove PESC without introducing a stronger intermediate gate.

EPBPF is not asserted to be weaker than PESC.

It is the current mechanism-level frontier.

---

# 19. Campaign 12

The next campaign is:

```text
CSM_RH Campaign 12
PARITY_BREAKING_ENDOGENOUS_BILINEAR_AUDIT
```

The purpose is to test whether the Friedlander-Iwaniec asymptotic-sieve philosophy can be adapted at all to the signed endogenous PESC setting.

It is not to assume their bilinear hypothesis.

---

# 20. Campaign 12 first task

The worker must define a canonical signed bilinear form whose fixed-power control would imply PESC.

The form must expose:

```text
prime detector
endogenous B-weight
two genuine multiplicative variables
sign structure
range of variables
required power saving
```

A candidate does not count merely because it resembles a standard asymptotic-sieve bilinear form.

---

# 21. Campaign 12 required questions

```text
Q1
Can PESC be embedded into a canonical bilinear form without triangle leakage?

Q2
Can the B(n-1) dependence be frozen, linearized, or transferred without circularity?

Q3
Does the resulting bilinear hypothesis already imply a fixed zero strip by itself?

Q4
Does parity-sensitive input from an asymptotic sieve survive the signed weight?

Q5
What exact variable range must carry the fixed power?

Q6
Is the needed estimate already equivalent to PESC after recombination?

Q7
If no useful bilinear embedding exists, can EPBPF be closed as an exhausted mechanism shell?
```

---

# 22. Campaign 12 rejection filters

Reject a candidate if:

## R1. It treats $B(n-1)$ as an external fixed smooth function.

## R2. It applies a nonnegative asymptotic-sieve theorem directly to a signed endogenous sequence.

## R3. It imports a fixed-power Mertens or zero-strip estimate.

## R4. It obtains only log-power detector fidelity.

## R5. It takes absolute values before the proposed parity-breaking cancellation.

## R6. It states a bilinear hypothesis without proving it or calibrating its theorem strength.

---

# 23. External calibration

Relevant external results:

1. Selberg's elementary prime number theorem supplies the prime-only symmetry formula.

2. Saidak, *On the prime number lemma of Selberg*, Math. Scand. 103 (2008), 5–10, proves a quantitative relation between the refined Selberg remainder and the PNT error.

3. Friedlander and Iwaniec, *Asymptotic sieve for primes*, Annals of Mathematics 148 (1998), 1041–1065, add a bilinear hypothesis to break the parity barrier and detect primes.

4. Standard sieve theory discussions emphasize that ordinary sieve information alone encounters the parity problem; parity-breaking requires additional analytic input.

These results calibrate mechanism strength.

None proves PESC.

---

# 24. State transition

The canonical transition is:

```text
CSM_RH v1.2
  ->
CSM_RH v1.3
```

with:

```text
Campaign 11
  CLOSED_AS_OPERATOR_AND_SIEVE_MECHANISM_AUDIT

O-RH-024
  PRIME_DILATION_MARKOV_CRITICALITY
  CREATED / CERTIFIED

O-RH-025
  SELBERG_POWER_MODE_RESONANCE
  CREATED / CERTIFIED AS MODE CALIBRATION

O-RH-026
  ENDOGENOUS_SIEVE_PARITY_FIDELITY
  CREATED / STRUCTURAL WARNING

F-RH-010
  PESC
  REMAINS OPEN

F-RH-011
  EPBPF
  CREATED / OPEN

S-RH-020
  SIGNED_PRIME_DILATION_NONLINEAR_CONTRACTION
  CREATED / OPEN

S-RH-021
  ENDOGENOUS_PARITY_BREAKING_BILINEAR_INPUT
  CREATED / OPEN

S-RH-022
  POWER_ACCURATE_ENDOGENOUS_SIEVE_FIDELITY
  CREATED / OPEN

Campaign 12
  PARITY_BREAKING_ENDOGENOUS_BILINEAR_AUDIT
  READY
```

---

# 25. Final status

```text
RH = OPEN

PESC FIXED POWER = OPEN

CLASSICAL SELBERG POSITIVE CLOSURE = CRITICAL

CLASSICAL SELBERG O(x) POWER-MODE RESOLUTION = INSUFFICIENT

GENERIC SIGNED SIEVE = TARGET-FIDELITY LIMITED

PURE SIEVE PARITY BREAKING = NOT AVAILABLE

ASYMPTOTIC-SIEVE STYLE BILINEAR INPUT = POSSIBLE MECHANISM / NOT YET ADAPTED

EPBPF = OPEN

NEXT CAMPAIGN = 12
```

The main new operator identity is:

$$
\boxed{
R(x)
+
\frac{L(x)}{\log x}
\mathcal P_xR
=
O
\left(
\frac1{\log x}
\right),
}
$$

with

$$
\mathcal P_x
$$

a positive prime-dilation averaging operator of mass one.

The main mechanism conclusion is:

> any fixed-power advance must introduce genuinely signed, parity-breaking arithmetic information that survives the endogenous dependence of the prime-error weight.
