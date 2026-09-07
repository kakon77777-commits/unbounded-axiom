# CSM_RH Paper 13
## Positivity-Lift Precision Tax, Asymptotic-Sieve Geometry Mismatch, and the Endogenous Möbius Bilinear Frontier

**Project:** `CSM_RH`  
**Paper:** `13`  
**Version:** `v0.1`  
**Date:** `2026-09-05`  
**Parent state:** `CSM_RH v1.3 / Paper 12`  
**Campaign:** `12 — PARITY_BREAKING_ENDOGENOUS_BILINEAR_AUDIT`  
**Status:** asymptotic-sieve adaptation audit / bilinear-frontier extraction; not a proof or disproof of RH

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

The paper tests whether the Friedlander–Iwaniec asymptotic-sieve philosophy can be adapted to the prime-error self-correlation target.

The conclusion is:

```text
PARITY-BREAKING BILINEAR INFORMATION
  is the right mechanism type

STANDARD NONNEGATIVE ASYMPTOTIC SIEVE
  is not a fixed-power PESC theorem

POSITIVITY LIFT
  incurs N^(3-o(1)) precision scale

STANDARD LOG-RELATIVE SIEVE OUTPUT
  is exponent-insufficient

DIRECT PESC BILINEARITY
  is additive/triangular

FRIEDLANDER-IWANIEC BILINEARITY
  is multiplicative a_mn geometry

BRIDGE
  requires a new endogenous Möbius bilinear theorem
```

No live GLM-5.3-Flash run is claimed.

---

# 1. Canonical target

Recall

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

$$
B(j)
=
\vartheta(j)-j,
$$

and

$$
\boxed{
\mathcal C_N^\vartheta
=
\sum_{n<2N}
w_N(n)c_nB(n-1).
}
$$

The fixed-power target is

$$
\boxed{
\operatorname{PESC}(\kappa):
\qquad
|\mathcal C_N^\vartheta|
\ll
N^{3-\kappa+o(1)}
}
$$

for one fixed

$$
0<\kappa<\frac12.
$$

---

# 2. Native bilinear form of PESC

Since

$$
B(n-1)
=
\sum_{m<n}c_m,
$$

we have:

## Theorem 2.1 — Additive Triangular Bilinear Form

$$
\boxed{
\mathcal C_N^\vartheta
=
\sum_{1\le m<n<2N}
w_N(n)c_mc_n.
}
$$

This is the native bilinear geometry of PESC.

It is:

```text
additive/order geometry:
  m < n

not

multiplicative/product geometry:
  k = mn
```

The distinction matters for parity-breaking sieve technology.

---

# 3. Friedlander–Iwaniec parity-breaking input

Friedlander and Iwaniec's asymptotic sieve begins with a nonnegative sequence

$$
(a_k).
$$

In addition to the usual divisor-distribution remainder hypothesis, they assume a bilinear estimate of the schematic pinned form

$$
\boxed{
\sum_m
\left|
\sum_{\substack{
L<n\le2L\\
mn\le X
}}
\gamma(n,C)
\mu(mn)
a_{mn}
\right|
\ll
A(X)
(\log X)^{-A_0},
}
$$

over a prescribed range of $L$ near the square-root scale, where

$$
\gamma(n,C)
=
\sum_{\substack{
d\mid n\\
d\le C
}}
\mu(d).
$$

The source of parity sensitivity is the factor

$$
\mu(mn).
$$

This is genuinely stronger information than ordinary linear sieve axioms.

It is also a multiplicative-index bilinear form.

---

# 4. Why the direct prime detector is not a useful F–I sequence

If one tries to set

$$
a_k=q_k
=
\log k\,
\mathbf1_{\mathbb P}(k),
$$

then for

$$
m>1,
\qquad
n>1,
$$

$$
a_{mn}=0,
$$

because $mn$ is composite.

Therefore the interior multiplicative bilinear form is degenerate on the prime-supported detector itself.

A nontrivial F–I embedding must use a sequence which has support on composite indices as well.

This is the first geometry mismatch.

---

# 5. Positivity lift of the endogenous target

The natural target sequence

$$
w_N(n)B(n-1)
$$

is signed.

Choose

$$
H_N
\ge
\max_{n<2N}
|B(n-1)|.
$$

Define two nonnegative sequences

$$
\boxed{
a_n^\pm
=
w_N(n)
[
H_N
\pm
B(n-1)
].
}
$$

Then

$$
a_n^\pm\ge0.
$$

Define the dimension-one prime-detection error functional

$$
\boxed{
\mathfrak E(a)
=
\sum_{p<2N}
(\log p)a_p
-
\sum_{n<2N}
a_n.
}
$$

---

# 6. Exact positivity-lift bridge

## Theorem 6.1

$$
\boxed{
\mathfrak E(a^+)
-
\mathfrak E(a^-)
=
2\mathcal C_N^\vartheta.
}
$$

### Proof

Since

$$
a_n^+-a_n^-
=
2w_N(n)B(n-1),
$$

we have

$$
\begin{aligned}
\mathfrak E(a^+)-\mathfrak E(a^-)
&=
2
\sum_{n<2N}
[
q_n-1
]
w_N(n)
B(n-1)
\\
&=
2\mathcal C_N^\vartheta.
\end{aligned}
$$

 $\square$

Thus a sufficiently accurate prime-detection theorem for both lifted sequences would prove PESC.

---

# 7. Size of the positivity baseline

The endpoint weight satisfies

$$
\sum_{n<2N}
w_N(n)
=
\frac32N^2+O(N).
$$

Therefore

$$
\sum_n
a_n^+
+
\sum_n
a_n^-
=
2H_N
\sum_n
w_N(n)
=
3H_NN^2
+
O(H_NN).
$$

Hence at least one lifted sequence has total mass

$$
\gg
H_NN^2.
$$

Chebyshev gives

$$
H_N\ll N.
$$

The classical PNT zero-free-region error gives a better but still subpower scale

$$
H_N
=
N^{1-o(1)}.
$$

Thus the natural lifted mass scale is

$$
\boxed{
N^{3-o(1)}.
}
$$

---

# 8. Positivity-Lift Precision Tax

Suppose one applies a prime-detection theorem to the two lifted sequences separately.

If its error is only relative-logarithmic,

$$
\mathfrak E(a^\pm)
=
O
\left(
A^\pm
(\log N)^{-C}
\right),
$$

where

$$
A^\pm
=
\sum_n a_n^\pm,
$$

then the resulting PESC bound is at best

$$
\boxed{
\mathcal C_N^\vartheta
=
N^{3-o(1)}.
}
$$

This is not

$$
N^{3-\kappa}
$$

for any fixed

$$
\kappa>0.
$$

Create:

```text
O-RH-027
POSITIVITY_LIFT_FIXED_POWER_PRECISION_TAX
status:
  CERTIFIED
```

Statement:

> Converting the signed endogenous PESC weight into separate nonnegative sieve sequences creates total mass of exponent $3-o(1)$. Independent logarithmic-relative prime-detection errors cannot yield a fixed PESC power.

---

# 9. Standard asymptotic-sieve output scale

In Friedlander–Iwaniec's theorem, after the sieve axioms are imposed, the prime sum has the expected main term with logarithmic relative precision, together with the controlled remainder generated by the sieve hypotheses.

Their parity-breaking bilinear hypothesis is extremely strong in logarithmic terms, but the architecture is designed to obtain an asymptotic prime-counting formula, not an $N^{-\kappa}$ relative error for the present lifted mass scale.

Therefore even an optimistic successful verification of the standard F–I axioms for $a^\pm$ would not by itself prove PESC $(\kappa)$.

Create:

```text
O-RH-028
STANDARD_ASYMPTOTIC_SIEVE_ERROR_SCALE_FLOOR
status:
  CERTIFIED_AS_PRECISION_MISMATCH
```

This is a precision statement.

It is not a criticism of the asymptotic sieve theorem.

---

# 10. Coupled-error issue

The exact PESC bridge uses the difference

$$
\mathfrak E(a^+)-\mathfrak E(a^-).
$$

Two independent estimates

$$
|\mathfrak E(a^\pm)|
\le
E_\pm
$$

give only

$$
|\mathcal C_N^\vartheta|
\le
\frac12
(
E_++E_-
).
$$

A cancellation between the two sieve errors cannot be assumed.

Therefore a route which hopes that the huge positivity baselines cancel after two independent asymptotic-sieve applications requires a new coupled signed error theorem.

That theorem is not part of the standard nonnegative asymptotic sieve.

---

# 11. Endogenous divisor-distribution remainder

To model a dimension-one sieve with local density

$$
g(d)=\frac1d,
$$

the endogenous part of the linear remainder contains

$$
\boxed{
\mathcal R_d^B(t)
=
\sum_{\substack{
n\le t\\
d\mid n
}}
w_N(n)B(n-1)
-
\frac1d
\sum_{n\le t}
w_N(n)B(n-1).
}
$$

A power-accurate lifted sieve would need sufficiently strong averaged control of these quantities over the required divisor range.

Thus even the Type-I side is no longer an external smooth-weight distribution problem.

It is distribution of the prime-generated error itself along multiples.

---

# 12. Endogenous multiplicative parity-breaking form

Insert the lifted sequence into the Friedlander–Iwaniec bilinear geometry.

The endogenous component is

$$
\boxed{
\mathfrak B_{N,L,C}
=
\sum_m
\left|
\sum_{\substack{
L<n\le2L\\
mn<2N
}}
\gamma(n,C)
\mu(mn)
w_N(mn)
B(mn-1)
\right|.
}
$$

This is the exact new parity-sensitive arithmetic form exposed by the adaptation.

A fixed-power implementation would require, in the relevant bilinear range, an estimate of the form

$$
\boxed{
\mathfrak B_{N,L,C}
\ll
N^{3-\kappa+o(1)}
}
$$

or another quantitatively sufficient variant after normalization.

No such theorem is established here.

---

# 13. Additive–Multiplicative Bilinear Geometry Mismatch

PESC itself is

$$
\sum_{m<n}
w_N(n)c_mc_n.
$$

The asymptotic-sieve parity-breaking input is of the form

$$
\sum_m
\left|
\sum_n
\gamma(n)
\mu(mn)
a_{mn}
\right|.
$$

The first couples two prime increments through order.

The second couples multiplicative factors through their product.

There is no identity-level equivalence between these two bilinear geometries.

The positivity lift supplies a bridge only by changing the sequence under study.

That bridge creates the new endogenous divisor and Möbius bilinear obligations.

Create:

```text
O-RH-029
ADDITIVE_MULTIPLICATIVE_BILINEAR_GEOMETRY_MISMATCH
status:
  CERTIFIED
```

This obstruction does not say multiplicative bilinear methods cannot prove PESC.

It identifies the transfer debt.

---

# 14. What parity-breaking contributes

The audit does not reduce Friedlander–Iwaniec parity breaking to "just another sieve".

Their key additional axiom explicitly probes multiplicative parity through

$$
\mu(mn),
$$

and this type of bilinear information can distinguish sequences which ordinary sieve data cannot distinguish.

Tao's sieve notes make the same structural point:

```text
linear / Type-I sieve data
  retains the parity barrier

bilinear / Type-II information
  can distinguish multiplicative parity

but the required bilinear asymptotics
  must come from deep external arithmetic input
```

Thus the mechanism lesson survives intact.

For PESC, the required external input is now explicitly endogenous.

---

# 15. Why standard asymptotic sieve does not directly apply to PESC

There are three independent reasons.

## 15.1 Sign

The natural sequence

$$
w_N(n)B(n-1)
$$

is signed.

The standard asymptotic sieve begins with nonnegative weights.

## 15.2 Precision

The positivity lift has exponent- $3$ mass.

Logarithmic relative error is insufficient for a fixed PESC power.

## 15.3 Geometry

The native PESC bilinear form is additive triangular.

The parity-breaking sieve hypothesis is multiplicative.

Therefore:

$$
\boxed{
\text{standard asymptotic sieve}
\neq
\text{direct PESC theorem}.
}
$$

---

# 16. Power-Accurate Coupled Signed Asymptotic Sieve

One possible future theorem would be a coupled signed extension of asymptotic sieve designed directly for the pair

$$
(a^+,a^-).
$$

It would have to control

$$
\mathfrak E(a^+)-\mathfrak E(a^-)
$$

without paying the full independent positivity baselines.

Such a theorem would require:

```text
signed coupling across the two lifts
power-accurate Type-I distribution
parity-breaking multiplicative bilinear input
target-fidelity against B(n-1)
fixed-power final error
```

No existing theorem is being claimed to have these properties.

Create:

```text
S-RH-023
POWER_ACCURATE_COUPLED_SIGNED_ASYMPTOTIC_SIEVE
status:
  OPEN
```

---

# 17. Endogenous Möbius Bilinear Frontier

Create the mechanism frontier:

```text
F-RH-012
ENDOGENOUS_MOBIUS_BILINEAR_FIDELITY
abbrev:
  EMBF
status:
  OPEN
```

Canonical prototype:

$$
\boxed{
\mathfrak B_{N,L,C}
=
\sum_m
\left|
\sum_{\substack{
L<n\le2L\\
mn<2N
}}
\gamma(n,C)
\mu(mn)
w_N(mn)
[
\vartheta(mn-1)-(mn-1)
]
\right|.
}
$$

The purpose of the next campaign is not to assume this bound.

It is to determine whether EMBF has any lower-strength route or whether fixed-power EMBF already loops back to the PESC / zero-strip core.

---

# 18. Campaign 12 candidate audit

## C12-A — direct F–I on the prime detector

```text
status:
  REJECTED / DEGENERATE

reason:
  q_mn = 0 for m,n>1
```

## C12-B — nonnegative positivity lift

```text
status:
  EXACT TARGET BRIDGE
  PRECISION INSUFFICIENT WITH STANDARD LOG-RELATIVE OUTPUT
```

## C12-C — separate asymptotic sieve on a+ and a-

```text
status:
  INSUFFICIENT WITHOUT COUPLED ERROR CANCELLATION
```

## C12-D — signed direct asymptotic sieve

```text
status:
  NOT A STANDARD EXISTING THEOREM
  SURVIVES AS NEW THEOREM FAMILY
```

## C12-E — endogenous F–I bilinear form

```text
status:
  SURVIVOR
  PROMOTED TO EMBF
```

---

# 19. EPBPF status

Paper 12 introduced

```text
F-RH-011
ENDOGENOUS_PARITY_BREAKING_PRIME_FEEDBACK
EPBPF
```

After the present audit:

```text
STANDARD ASYMPTOTIC-SIEVE INSTANCE
  CLOSED / NO DIRECT FIXED-POWER ROUTE

GENERAL PARITY-BREAKING IDEA
  REMAINS OPEN

CANONICAL NEW SUBFRONTIER
  EMBF
```

Thus EPBPF is partially compiled rather than fully retired.

---

# 20. Campaign 13

The next campaign is:

```text
CSM_RH Campaign 13
ENDOGENOUS_MOBIUS_BILINEAR_STRENGTH_AUDIT
```

Target:

```text
F-RH-012
EMBF
```

The campaign must determine whether a fixed-power EMBF estimate is:

```text
a genuinely different route,
a hidden Mertens / zero-strip theorem,
a restatement of PESC after recombination,
or a viable new multilinear frontier.
```

---

# 21. Campaign 13 required questions

```text
Q1
What is the exact scale of EMBF in the Friedlander–Iwaniec bilinear window?

Q2
Can the mu(mn) factor be separated into mu(m)mu(n) plus a coprimality condition without losing the target?

Q3
Does fixed-power EMBF imply a fixed-power Mertens estimate on any slice?

Q4
Can averaging over m produce a real gain, or does the coprimality structure leave a one-variable Möbius sum?

Q5
How does gamma(n,C) change the parity information?

Q6
Can known Type-II / large-sieve technology give any fixed N-power?

Q7
If not, what exact new Möbius-prime-error correlation theorem is required?
```

---

# 22. Campaign 13 rejection filters

Reject a candidate if:

## R1. It assumes square-root Möbius cancellation.

## R2. It hides a fixed zero-free half-plane in a Mertens input.

## R3. It treats the outer absolute value as harmless.

## R4. It replaces the endogenous $B(mn-1)$ by an external bounded test function.

## R5. It obtains only logarithmic or stretched-logarithmic saving.

## R6. It calls the Friedlander–Iwaniec bilinear axiom itself a proved input.

---

# 23. External calibration

Friedlander and Iwaniec, *Asymptotic sieve for primes*, Annals of Mathematics 148 (1998), introduce an additional bilinear hypothesis specifically to break the sieve parity problem.

Their pinned hypothesis contains the factor

$$
\mu(mn)a_{mn}
$$

inside a multiplicative bilinear form and is required over a range near the square-root scale.

They explain that the cancellation source is the sign change of the Möbius factor.

Tao's sieve notes likewise emphasize that Type-II bilinear information can break parity, but the required bilinear asymptotics normally demand deep input outside sieve theory.

These facts motivate EMBF.

They do not prove it.

---

# 24. State transition

The canonical transition is:

```text
CSM_RH v1.3
  ->
CSM_RH v1.4
```

with:

```text
Campaign 12
  CLOSED_AS_ASYMPTOTIC_SIEVE_ADAPTATION_AUDIT

O-RH-027
  POSITIVITY_LIFT_FIXED_POWER_PRECISION_TAX
  CREATED / CERTIFIED

O-RH-028
  STANDARD_ASYMPTOTIC_SIEVE_ERROR_SCALE_FLOOR
  CREATED / CERTIFIED AS PRECISION MISMATCH

O-RH-029
  ADDITIVE_MULTIPLICATIVE_BILINEAR_GEOMETRY_MISMATCH
  CREATED / CERTIFIED

F-RH-011
  EPBPF
  PARTIALLY COMPILED

F-RH-012
  EMBF
  CREATED / OPEN

S-RH-023
  POWER_ACCURATE_COUPLED_SIGNED_ASYMPTOTIC_SIEVE
  CREATED / OPEN

Campaign 13
  ENDOGENOUS_MOBIUS_BILINEAR_STRENGTH_AUDIT
  READY
```

---

# 25. Final status

```text
RH = OPEN

PESC = OPEN

STANDARD ASYMPTOTIC SIEVE ADAPTATION = NO DIRECT FIXED-POWER ROUTE

PARITY-BREAKING BILINEAR IDEA = STILL RELEVANT

POSITIVITY LIFT = EXACT BUT PRECISION-EXPENSIVE

EMBF = OPEN

NEXT CAMPAIGN = 13
```

The current new mechanism core is:

$$
\boxed{
\sum_m
\left|
\sum_{\substack{
L<n\le2L\\
mn<2N
}}
\gamma(n,C)\mu(mn)
w_N(mn)
[
\vartheta(mn-1)-(mn-1)
]
\right|.
}
$$

If this route works, the fixed power must come from genuinely new multiplicative parity-breaking information about the prime-generated error itself.
