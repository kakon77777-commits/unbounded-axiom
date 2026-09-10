# CSM_RH Paper 69

## Centered Prime–Möbius Hankel Variance, Exact Fourier Kernel, and the Auxiliary-to-Root Bridge Audit

**Project:** CSM_RH  
**Paper:** 69  
**Version:** v0.1  
**Date:** 2026-09-09  
**Campaign:** 46 — `SEEDED_ARITHMETIC_STRIP_GAP_GENERATION`  
**Auxiliary frontier:** F-RH-020 — `PRIME_PAIR_AVERAGED_CHOWLA_ABSOLUTEIZATION_ENERGY`  
**Canonical root frontier:** F-RH-017-v3  
**Status:** F-RH-020 EXACTLY CENTERED / CURRENT LOG ENERGY CALIBRATED / ROOT BRIDGE NOT CERTIFIED  
**Canonical entry state:** v1.59 / Paper 68 v0.1  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 68 isolated the auxiliary energy

$$
E_2(X,H)
=
\sum_{h\le H}
\left|
\sum_{p\le X}\mu(p+h)
\right|^2
$$

as a possible parity-breaking route from signed shifted-prime Möbius cancellation to absolute cancellation.

The present paper puts this energy into its exact operator and Fourier forms, and separates what is already controlled by the PESC seed from the genuinely missing variance.

Define

$$
C_X(h)
=
\sum_{p\le X}\mu(p+h),
$$

$$
\overline C_X
=
\frac1H
\sum_{h\le H}
C_X(h).
$$

Then the exact orthogonal decomposition is

$$
\boxed{
E_2(X,H)
=
H|\overline C_X|^2
+
V_2(X,H),
}
$$

where

$$
\boxed{
V_2(X,H)
=
\sum_{h\le H}
|C_X(h)-\overline C_X|^2.
}
$$

Assume PESC $(\kappa)$ and put

$$
d=\frac{\kappa}{2},
\qquad
H=X^{1-\tau}.
$$

Paper 68 proved, for $\tau<d$,

$$
\left|
\sum_{h\le H}C_X(h)
\right|
\ll
H\pi(X)
X^{-(d-\tau)+o(1)}.
$$

Therefore

$$
\boxed{
H|\overline C_X|^2
\ll
H\pi(X)^2
X^{-2(d-\tau)+o(1)}.
}
$$

Consequently, for every target exponent

$$
0<\eta<d-\tau,
$$

a bound

$$
E_2(X,H)
\ll
H\pi(X)^2X^{-2\eta}
$$

is equivalent at fixed-power resolution to the centered variance theorem

$$
\boxed{
V_2(X,H)
\ll
H\pi(X)^2X^{-2\eta}.
}
$$

The signed mode has already been removed by the seed. F-RH-020 is therefore not a first-moment problem. It is a centered covariance problem.

Let $\mathsf M=\mathsf M_{X,H}$ be the rectangular prime–shift Hankel matrix

$$
\boxed{
\mathsf M_{h,p}
=
\mu(p+h),
\qquad
1\le h\le H,
\quad
p\le X.
}
$$

If $\mathbf 1_{\mathbb P}$ denotes the all-one vector on the prime columns and

$$
P_0
=
I_H
-
\frac1H
\mathbf 1_H\mathbf 1_H^*
$$

is the projection orthogonal to the constant shift vector, then

$$
\boxed{
V_2
=
\left\|
P_0
\mathsf M
\mathbf 1_{\mathbb P}
\right\|_2^2.
}
$$

Equivalently,

$$
\boxed{
V_2
=
\mathbf 1_{\mathbb P}^*
\mathsf M^*
P_0
\mathsf M
\mathbf 1_{\mathbb P}.
}
$$

The centered prime-pair Chowla kernel is

$$
\boxed{
K_H^\circ(p_1,p_2)
=
\sum_{h\le H}
\mu(p_1+h)\mu(p_2+h)
-
\frac1H
S_H(p_1)S_H(p_2),
}
$$

where

$$
S_H(p)
=
\sum_{h\le H}\mu(p+h).
$$

Then

$$
\boxed{
V_2
=
\sum_{p_1,p_2\le X}
K_H^\circ(p_1,p_2).
}
$$

This identifies the exact missing arithmetic object: a prime-vector quadratic form of the centered short-shift Möbius covariance matrix.

There is also an exact Fourier representation. Let

$$
A_X(\alpha)
=
\sum_{p\le X}e(p\alpha),
$$

$$
B_{X,H}(\alpha)
=
\sum_{n\le X+H}\mu(n)e(n\alpha),
$$

and

$$
Z_{X,H}(\alpha)
=
A_X(\alpha)
\overline{B_{X,H}(\alpha)}.
$$

Then, for every $1\le h\le H$,

$$
\boxed{
C_X(h)
=
\int_0^1
Z_{X,H}(\alpha)
e(h\alpha)
\,d\alpha.
}
$$

If

$$
D_H(t)
=
\sum_{h=1}^{H}e(ht),
$$

then

$$
\boxed{
E_2
=
\int_0^1\int_0^1
Z(\alpha)\overline{Z(\beta)}
D_H(\alpha-\beta)
\,d\alpha\,d\beta,
}
$$

and

$$
\boxed{
V_2
=
\int_0^1\int_0^1
Z(\alpha)\overline{Z(\beta)}
\left[
D_H(\alpha-\beta)
-
\frac1H
D_H(\alpha)
\overline{D_H(\beta)}
\right]
\,d\alpha\,d\beta.
}
$$

Thus F-RH-020 is a centered near-diagonal Fourier/Hankel energy problem, not merely a supremum-over-frequency problem.

Current literature already gives logarithmic control. Lichtman proves, for $H=X^\theta$,

$$
\sum_{h\le H}|C_X(h)|
\ll_{\theta,\delta}
H\pi(X)
(\log X)^{-1/3+\delta}.
$$

Since

$$
|C_X(h)|\le\pi(X),
$$

this immediately implies

$$
\boxed{
E_2(X,H)
\ll_{\theta,\delta}
H\pi(X)^2
(\log X)^{-1/3+\delta}.
}
$$

So the auxiliary frontier is not "prove that the energy is smaller than trivial." That is known.

Its new content is exactly:

$$
\boxed{
\text{logarithmic centered energy saving}
\quad\longrightarrow\quad
\text{fixed-power centered energy saving}.
}
$$

Lichtman's proof is even stronger on the typical-factorization part. The key Fourier theorem and the Fourier decoupling lemma give, for the typical component,

$$
E_{2,\mathcal S}
\ll
\frac{
HX^2
}{
(\log X)^{A/5+1}
}.
$$

Since

$$
\pi(X)^2
=
X^2
(\log X)^{-2+o(1)},
$$

the typical component has arbitrary fixed log-power savings as $A$ is increased. The final $(\log X)^{-1/3+o(1)}$ scale comes from the sieve treatment of the atypical complement.

This matches Paper 68's local-factor calculation: purely local factorization naturally gives logarithmic decay.

The PESC seed also upgrades the zero additive frequency to fixed power. Uniformly for $x\asymp X$,

$$
\sum_{x<n\le x+H}\mu(n)
=
M(x+H)-M(x)
\ll
H X^{-(d-\tau)+o(1)}.
$$

But current Fourier arguments require control over nonzero additive frequencies. Fixed rational frequencies introduce nonprincipal Dirichlet-character channels, and Papers 65–67 showed why a zeta seed alone does not provide fixed-power control there.

The exact Fourier identity also clarifies why F-RH-020 has no certified root implication yet. Smallness of the cross-spectrum

$$
A_X(\alpha)\overline{B_{X,H}(\alpha)}
$$

does not, by itself, imply smallness of the prime spectrum $A_X(\alpha)$. A lower coercivity theorem for the Möbius factor on boundary-sensitive frequencies is missing.

A zeta boundary zero is a multiplicative Mellin singularity. No certified theorem currently forces it to create a fixed-size component in the centered additive prime–Möbius Hankel energy.

Therefore F-RH-020 remains auxiliary.

The paper opens a bridge candidate:

```text
F-RH-021
BOUNDARY MERTENS MODE PRIME-SAMPLING / HANKEL COERCIVITY
```

Desired shape:

if a zeta zero lies at

$$
\beta=1-d,
$$

then along an unbounded sequence of $X$,

$$
\boxed{
V_2(X,H)
\gg
H\pi(X)^2
X^{-2d-o(1)}
}
$$

for a suitable near-macroscopic $H$.

If F-RH-021 were proved, then any F-RH-020 upper theorem with exponent $\eta>d$ would exclude the boundary zero and create a genuine root bridge.

No such coercivity theorem is currently certified.

No RH theorem is claimed.

---

# 1. Prime–shift Hankel matrix

Let

$$
\mathcal P_X
=
\{p\le X:p\text{ prime}\}.
$$

Define the $H\times\pi(X)$ matrix

$$
\boxed{
\mathsf M_{h,p}
=
\mu(p+h).
}
$$

Let

$$
\mathbf 1_{\mathbb P}
=
(1)_{p\in\mathcal P_X}.
$$

Then

$$
\boxed{
C
=
\mathsf M
\mathbf 1_{\mathbb P}
}
$$

is exactly the vector

$$
(C_X(1),\ldots,C_X(H))^T.
$$

Hence

$$
\boxed{
E_2
=
\|\mathsf M\mathbf 1_{\mathbb P}\|_2^2.
}
$$

This is an exact finite-dimensional representation.

---

# 2. Seed removal of the constant shift mode

Let

$$
\mathbf 1_H
=
(1,\ldots,1)^T
$$

and

$$
P_0
=
I_H
-
\frac1H
\mathbf 1_H\mathbf 1_H^*.
$$

The constant component of $C$ is

$$
\frac1H
\mathbf 1_H\mathbf 1_H^*C
=
\overline C_X\mathbf 1_H.
$$

Orthogonality gives

$$
\boxed{
\|C\|_2^2
=
H|\overline C_X|^2
+
\|P_0C\|_2^2.
}
$$

Thus

$$
\boxed{
V_2
=
\|P_0\mathsf M\mathbf 1_{\mathbb P}\|_2^2.
}
$$

Record:

```text
B-RH-091
SEEDED_SHIFT_MEAN_REMOVES_THE_CONSTANT_HANKEL_MODE_AT_FIXED_POWER
CERTIFIED
```

---

# 3. Seed size of the mean mode

Assume PESC $(\kappa)$ and let

$$
d=\frac{\kappa}{2}.
$$

Paper 68 gives

$$
\left|
\sum_{h\le H}
C_X(h)
\right|
\ll
H\pi(X)
X^{-(d-\tau)+o(1)}
$$

when

$$
H=X^{1-\tau},
\qquad
\tau<d.
$$

Therefore

$$
\boxed{
H|\overline C_X|^2
=
\frac1H
\left|
\sum_{h\le H}C_X(h)
\right|^2
\ll
H\pi(X)^2
X^{-2(d-\tau)+o(1)}.
}
$$

If

$$
0<\eta<d-\tau,
$$

then this term is negligible relative to

$$
H\pi(X)^2X^{-2\eta}.
$$

Hence:

## Theorem 3.1 — F-RH-020 centered reduction

For every fixed

$$
0<\eta<d-\tau,
$$

F-RH-020 at exponent $\eta$ is equivalent at exponent resolution to

$$
\boxed{
V_2(X,H)
\ll
H\pi(X)^2X^{-2\eta}.
}
$$

The unknown quantity is variance, not mean.

---

# 4. Centered prime-pair Chowla covariance

For each prime $p$ define

$$
S_H(p)
=
\sum_{h\le H}\mu(p+h).
$$

Then

$$
\begin{aligned}
\mathsf M^*P_0\mathsf M(p_1,p_2)
&=
\sum_{h\le H}
\mu(p_1+h)\mu(p_2+h)
\\
&\quad
-
\frac1H
S_H(p_1)S_H(p_2).
\end{aligned}
$$

Define

$$
\boxed{
K_H^\circ(p_1,p_2)
=
\mathsf M^*P_0\mathsf M(p_1,p_2).
}
$$

Then:

## Theorem 4.1 — Centered Chowla quadratic form

$$
\boxed{
V_2
=
\sum_{p_1,p_2\le X}
K_H^\circ(p_1,p_2).
}
$$

Record:

```text
B-RH-092
F_RH_020_IS_THE_PRIME_VECTOR_QUADRATIC_FORM_OF_CENTERED_SHORT_SHIFT_MOBIUS_COVARIANCE
CERTIFIED
```

This is stronger bookkeeping than the uncentered off-diagonal expansion of Paper 68.

---

# 5. Exact Fourier representation

Define

$$
e(t)=e^{2\pi it}.
$$

Let

$$
A_X(\alpha)
=
\sum_{p\le X}e(p\alpha)
$$

and

$$
B_{X,H}(\alpha)
=
\sum_{1\le n\le X+H}\mu(n)e(n\alpha).
$$

Set

$$
Z(\alpha)
=
A_X(\alpha)
\overline{B_{X,H}(\alpha)}.
$$

Then

$$
\begin{aligned}
\int_0^1
Z(\alpha)e(h\alpha)d\alpha
&=
\sum_{p\le X}
\sum_{n\le X+H}
\mu(n)
\int_0^1
e((p-n+h)\alpha)d\alpha
\\
&=
\sum_{p\le X}\mu(p+h)
\\
&=
\boxed{
C_X(h).
}
\end{aligned}
$$

This is exact for $1\le h\le H$.

---

# 6. Dirichlet-kernel energy

Define

$$
D_H(t)
=
\sum_{h=1}^{H}e(ht).
$$

Then

$$
\begin{aligned}
E_2
&=
\sum_{h=1}^{H}
\left|
\int Z(\alpha)e(h\alpha)d\alpha
\right|^2
\\
&=
\boxed{
\int_0^1\int_0^1
Z(\alpha)\overline{Z(\beta)}
D_H(\alpha-\beta)
\,d\alpha\,d\beta.
}
\end{aligned}
$$

Moreover,

$$
\sum_{h\le H}C_X(h)
=
\int_0^1
Z(\alpha)
D_H(\alpha)
\,d\alpha.
$$

Therefore:

## Theorem 6.1 — Centered Fourier/Hankel kernel

$$
\boxed{
V_2
=
\int_0^1\int_0^1
Z(\alpha)\overline{Z(\beta)}
\mathcal K_H^\circ(\alpha,\beta)
\,d\alpha\,d\beta,
}
$$

where

$$
\boxed{
\mathcal K_H^\circ(\alpha,\beta)
=
D_H(\alpha-\beta)
-
\frac1H
D_H(\alpha)
\overline{D_H(\beta)}.
}
$$

Record:

```text
B-RH-093
EXACT_CENTERED_FOURIER_HANKEL_KERNEL_FOR_SHIFTED_PRIME_MOBIUS_ENERGY
CERTIFIED
```

The second term removes precisely the constant shift mode already controlled by the seed.

---

# 7. Current unconditional energy bound

Lichtman's Theorem 1.1 gives, for

$$
H=X^\theta,
\qquad
0<\theta<1,
$$

and every fixed $\delta>0$,

$$
\boxed{
\sum_{h\le H}|C_X(h)|
\ll_{\theta,\delta}
H\pi(X)
(\log X)^{-1/3+\delta}.
}
$$

Since

$$
|C_X(h)|
\le
\pi(X),
$$

we have

$$
|C_X(h)|^2
\le
\pi(X)|C_X(h)|.
$$

Summing:

## Theorem 7.1 — Current logarithmic F-RH-020 energy

$$
\boxed{
E_2(X,H)
\ll_{\theta,\delta}
H\pi(X)^2
(\log X)^{-1/3+\delta}.
}
$$

Record:

```text
B-RH-094
LICHTMAN_SHIFTED_PRIME_THEOREM_ALREADY_GIVES_LOGARITHMIC_F_RH_020_ENERGY_SAVING
CERTIFIED_EXTERNAL_CALIBRATION
```

Thus the auxiliary frontier is specifically a log-to-power upgrade.

---

# 8. Typical-factorization component is much smaller

Lichtman's proof introduces the typical-factorization set $\mathcal S$ and proves the key Fourier estimate

$$
\sup_\alpha
\int_0^X
\left|
\sum_{\substack{x<n\le x+H\\n\in\mathcal S}}
\mu(n)e(n\alpha)
\right|dx
\ll
\frac{HX}{(\log X)^{A/5}}.
$$

His Fourier decoupling lemma then gives directly

$$
\boxed{
E_{2,\mathcal S}
\ll
\frac{
HX^2
}{
(\log X)^{A/5+1}
}.
}
$$

Because

$$
H\pi(X)^2
=
HX^2
(\log X)^{-2+o(1)},
$$

$$
\boxed{
\frac{E_{2,\mathcal S}}{H\pi(X)^2}
\ll
(\log X)^{1-A/5+o(1)}.
}
$$

For any prescribed fixed $B>0$, choosing $A>5(B+1)$ gives

$$
\boxed{
E_{2,\mathcal S}
\ll
H\pi(X)^2
(\log X)^{-B}.
}
$$

Thus the Fourier-typical component already has arbitrary log-power energy saving.

The final quantitative scale of Theorem 1.1 is limited by the sieve treatment of the atypical complement, whose density estimate contains the $(\log X)^{-1/3+\delta}$ term.

This is consistent with Paper 68's dimension-two local-factor ceiling.

---

# 9. Seeded zero-frequency Fourier power

The seed Mertens estimate gives, uniformly for $x\asymp X$,

$$
\begin{aligned}
\sum_{x<n\le x+H}\mu(n)
&=
M(x+H)-M(x)
\\
&\ll
X^{1-d+o(1)}
\\
&=
\boxed{
H X^{-(d-\tau)+o(1)}.
}
\end{aligned}
$$

Therefore the additive frequency

$$
\alpha=0
$$

already has fixed-power short-interval Fourier cancellation.

Integrating over $x$ gives

$$
\boxed{
\int_X^{2X}
\left|
\sum_{x<n\le x+H}\mu(n)
\right|dx
\ll
XH
X^{-(d-\tau)+o(1)}.
}
$$

Record:

```text
B-RH-095
PESC_SEED_GIVES_FIXED_POWER_SHORT_INTERVAL_MOBIUS_FOURIER_CONTROL_AT_ALPHA_ZERO
CERTIFIED
```

The missing fixed-power Fourier information is nonzero frequency information.

---

# 10. Why current Fourier machinery does not immediately upgrade to power

Lichtman's key Fourier theorem is a supremum over all $\alpha$.

On rational major arcs, additive phases are decomposed into Dirichlet characters.

Papers 65–67 certified:

```text
principal character:
fixed-power improved by the zeta seed.

polynomial-conductor family:
averaged fixed-power improved by large sieve.

fixed/subpolynomial nonprincipal characters:
no individual fixed strip from the zeta seed.

absolute shift norms:
fixed character harmonics survive.
```

Therefore the seed improvement at $\alpha=0$ cannot simply be promoted to

$$
\sup_\alpha
$$

at fixed power.

F-RH-020's centered Fourier kernel offers a possible route around the supremum, but no fixed-power theorem for that kernel is currently known.

---

# 11. Why F-RH-020 is not yet a root theorem

The root frontier concerns the prime error

$$
\psi(x+H)-\psi(x)-H.
$$

F-RH-020 controls a prime–Möbius cross-correlation.

In Fourier form, the observable is built from

$$
\boxed{
Z(\alpha)
=
A_X(\alpha)
\overline{B_{X,H}(\alpha)}.
}
$$

Smallness of $Z$ does not algebraically imply smallness of $A_X$.

A lower bound on the Möbius factor is required on the frequencies where a hypothetical prime boundary packet lives.

At the abstract level:

$$
|AB|\ll\varepsilon
$$

does not imply

$$
|A|\ll\varepsilon
$$

without coercivity of $B$.

The actual zeta boundary information is Mellin-multiplicative, whereas F-RH-020 is additive-shift spectral information.

No certified theorem currently transfers a boundary zero into a lower bound for the centered Hankel energy.

Create:

```text
O-RH-159
PRIME_MOBIUS_CROSS_ENERGY_HAS_NO_ROOT_COERCIVITY_WITHOUT_A_BOUNDARY_MODE_SAMPLING_THEOREM
CERTIFIED_AS_BRIDGE_OBSTRUCTION
```

This is a bridge obstruction, not a claim that no such theorem can exist.

---

# 12. Conditional bridge candidate

The missing bridge may be stated explicitly.

Open:

```text
F-RH-021
BOUNDARY_MERTENS_MODE_PRIME_SAMPLING_HANKEL_COERCIVITY
```

Desired theorem:

if

$$
\rho=1-d+i\gamma
$$

is a zeta zero on the PESC seed boundary, then for some near-macroscopic

$$
H=X^{1-\tau}
$$

and an unbounded sequence of $X$,

$$
\boxed{
V_2(X,H)
\gg_{\rho}
H\pi(X)^2
X^{-2d-o(1)}.
}
$$

If this were known and F-RH-020 supplied

$$
V_2(X,H)
\ll
H\pi(X)^2
X^{-2\eta}
$$

with

$$
\eta>d,
$$

the boundary zero would be excluded.

Thus:

```text
F-RH-020 + F-RH-021
would create a root strip improvement.
```

Neither theorem is currently certified at the required fixed-power level.

---

# 13. Matrix orientation and current averaged Chowla results

Lichtman's higher-correlation theorem proves strong averaged cancellation for matrices of the form

$$
\sum_{p\le X}
\mu(p+h_1)\cdots\mu(p+h_m)
$$

when the shift variables are averaged.

For $m=2$, this controls the column Gram matrix

$$
\mathsf M^*\mathsf M
$$

in an averaged entrywise sense.

F-RH-020 instead asks for

$$
\|\mathsf M\mathbf 1_{\mathbb P}\|_2^2,
$$

a specific prime-vector quadratic form in the row orientation.

Averaged entrywise Chowla cancellation does not by itself give a fixed-power operator bound in the prime-vector direction.

This explains why the existing higher-correlation theorem is highly relevant but does not close F-RH-020.

---

# 14. Campaign status

After Paper 69:

```text
F-RH-017-v3:
CANONICAL ROOT FRONTIER / OPEN.

F-RH-020:
AUXILIARY CENTERED HANKEL VARIANCE FRONTIER / OPEN.

F-RH-021:
AUXILIARY-TO-ROOT COERCIVITY BRIDGE / OPEN.
```

Certified:

```text
constant shift mode:
fixed-power controlled by seed.

total shifted-prime Möbius energy:
log-saving known.

typical-factorization energy:
arbitrary fixed log-power saving known.

zero additive frequency:
fixed-power controlled by seed.
```

Open:

```text
centered variance:
fixed-power.

boundary Mellin mode -> additive prime-sampling Hankel lower bound:
unknown.
```

---

# 15. Recommended next action

The next round should not immediately try to prove all of F-RH-020.

First test F-RH-021.

Question:

```text
Does a zeta boundary pole force a critical-sized
prime-sampled Mertens covariance mode?
```

If no robust lower forcing can be proved, F-RH-020 should be closed as strategically auxiliary and the campaign should return directly to F-RH-017-v3.

If a coercive lower bound exists, then F-RH-020 becomes a genuine root attack rather than only a parity diagnostic.

This is the most important decision point for the current auxiliary route.

---

# 16. External calibration

## 16.1. Lichtman shifted-prime Möbius theorem

J. D. Lichtman,
*Averages of the Möbius Function on Shifted Primes*,
Quarterly Journal of Mathematics 73 (2022), 729–757.

For $H=X^\theta$:

$$
\sum_{h\le H}
\left|
\sum_{p\le X}\mu(p+h)
\right|
\ll_{\theta,\delta}
H\pi(X)
(\log X)^{-1/3+\delta}.
$$

Its Lemma 2.1 is the Fourier decoupling inequality, and Theorem 2.2 gives arbitrary log-power Fourier savings on the typical-factorization component.

URL:

https://academic.oup.com/qjmath/article/73/2/729/6446139

## 16.2. 2026 short-interval higher uniformity

Matomäki, Radziwiłł, Shao, Tao and Teräväinen prove arbitrary log-power short-interval discorrelation for $\mu$ and $\Lambda-\Lambda^\sharp$ in the almost-all setting, while fixed-power estimates in the corresponding theorem are available for divisor-function residuals rather than for $\mu$ or $\Lambda$.

This confirms that the present fixed-power Möbius variance target lies beyond the current published quantitative theorem.

URL:

https://link.springer.com/article/10.1007/s00222-026-01408-6

---

# 17. State transition

Advance candidate state

$$
v1.59
\to
v1.60.
$$

Add:

```text
B-RH-091
SEEDED_SHIFT_MEAN_REMOVES_THE_CONSTANT_HANKEL_MODE_AT_FIXED_POWER

B-RH-092
F_RH_020_IS_THE_PRIME_VECTOR_QUADRATIC_FORM_OF_CENTERED_SHORT_SHIFT_MOBIUS_COVARIANCE

B-RH-093
EXACT_CENTERED_FOURIER_HANKEL_KERNEL_FOR_SHIFTED_PRIME_MOBIUS_ENERGY

B-RH-094
LICHTMAN_SHIFTED_PRIME_THEOREM_ALREADY_GIVES_LOGARITHMIC_F_RH_020_ENERGY_SAVING

B-RH-095
PESC_SEED_GIVES_FIXED_POWER_SHORT_INTERVAL_MOBIUS_FOURIER_CONTROL_AT_ALPHA_ZERO

O-RH-159
PRIME_MOBIUS_CROSS_ENERGY_HAS_NO_ROOT_COERCIVITY_WITHOUT_A_BOUNDARY_MODE_SAMPLING_THEOREM
```

Open:

```text
F-RH-021
BOUNDARY_MERTENS_MODE_PRIME_SAMPLING_HANKEL_COERCIVITY
OPEN_AUXILIARY_BRIDGE
```

No RH certificate is created.

---

# 18. Conclusion

F-RH-020 is now structurally exact.

The PESC seed removes its constant shift mode at fixed power.

Current theorems already make its total energy logarithmically small, and make the Fourier-typical component arbitrarily log-small.

What remains is a centered variance theorem at fixed-power resolution.

But even such a theorem is not yet a root result: a boundary-zero-to-Hankel coercivity theorem is missing.

The next round should decide F-RH-021 before investing further in F-RH-020.
