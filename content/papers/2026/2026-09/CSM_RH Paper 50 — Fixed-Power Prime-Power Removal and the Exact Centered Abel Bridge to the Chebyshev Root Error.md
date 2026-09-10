# CSM_RH Paper 50

## Fixed-Power Prime-Power Removal and the Exact Centered Abel Bridge to the Chebyshev Root Error

**Project:** CSM_RH  
**Paper:** 50  
**Version:** v0.1  
**Date:** 2026-09-08  
**Campaign:** 44 — `PESC_TRIANGULAR_LAG_KERNEL_ATTACK`  
**Track:** PK4 — `CENTERED_LAMBDA_PRIME_ONLY_BRIDGE`  
**Status:** PK4 CLOSURE CANDIDATE  
**Canonical entry state:** v1.40 / Paper 49 v0.2  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 49 reduced the fixed-power PESC problem, with only absolute constant deterministic distortion, to the centered Mellin middle-band energy

$$
\int_{N^{-\kappa}\le |t|\le N^\kappa}
\frac{|\mathfrak M_N(t)|^2}{t^2}\,dt,
$$

where

$$
\mathfrak M_N(t)
=
\sum_{m<2N}
\left(
1_{\mathbb P}(m)\log m-1
\right)
\omega_{N,t}(m),
$$

and

$$
\omega_{N,t}(m)
=
\begin{cases}
\dfrac{2^{it}-1}{N},&m\le N,\\[2mm]
\dfrac{(2N/m)^{it}-1}{m},&N<m<2N,\\[2mm]
0,&m\ge2N.
\end{cases}
$$

The present paper closes the prime-only-to-von-Mangoldt interface required by Campaign 44 / PK4.

Define the centered von Mangoldt transform

$$
\mathfrak L_N(t)
=
\sum_{m<2N}
(\Lambda(m)-1)\omega_{N,t}(m).
$$

The difference between $\mathfrak L_N$ and the prime-only transform is exactly the prime-power correction

$$
\mathfrak R_N(t)
=
\sum_{\substack{p^a<2N\\a\ge2}}
(\log p)\omega_{N,t}(p^a).
$$

Using only the Chebyshev-scale estimate for prime powers, this paper proves the uniform centered bound

$$
|\mathfrak R_N(t)|
\ll
N^{-1/2}\min(|t|,1),
$$

and therefore

$$
\int_{N^{-\kappa}\le |t|\le N^\kappa}
\frac{|\mathfrak R_N(t)|^2}{t^2}\,dt
\ll
N^{-1}.
$$

Hence for every fixed $0<\kappa\le1$, the prime-only and von Mangoldt centered middle-band energies are fixed-power equivalent. The prime/background cross term is not discarded; it is controlled in the weighted Hilbert norm.

The second main result is an exact discrete Abel identity. Let

$$
E_\psi(m)=\psi(m)-m
$$

and

$$
g_{N,t}(x)
=
\frac{(2N/x)^{it}-1}{x}.
$$

Then

$$
\boxed{
\mathfrak L_N(t)
=
\sum_{m=N}^{2N-1}
E_\psi(m)
\left(
g_{N,t}(m)-g_{N,t}(m+1)
\right).
}
$$

This identity is exact. It automatically retains the entire $m\le N$ aggregate branch because the centered weight is constant on that range and satisfies

$$
g_{N,t}(N)
=
\frac{2^{it}-1}{N},
\qquad
g_{N,t}(2N)=0.
$$

Thus PK4 is reduced without logarithmic-to-power promotion, without a tail-only replacement, and without an unpriced prime-power substitution.

No fixed-power PESC estimate is proved. The next obstruction is the arithmetic behavior of the exact centered Abel transform of $\psi(m)-m$, which is the object that must be attacked in PK5.

---

# 1. Inherited state from Paper 49

Paper 49 certified the centered prime-error transform

$$
\mathfrak M_N(t)
=
\sum_{m<2N}
c_m\omega_{N,t}(m),
$$

where

$$
c_m
=
1_{\mathbb P}(m)\log m-1.
$$

For fixed $0<\kappa\le1$, fixed-power PESC is exponent-equivalent to

$$
\boxed{
\mathcal E_{\mathbb P}(N,\kappa)
:=
\int_{\mathcal B_{N,\kappa}}
\frac{|\mathfrak M_N(t)|^2}{t^2}\,dt
\ll
N^{-\kappa+o(1)},
}
$$

where

$$
\mathcal B_{N,\kappa}
=
\left\{
t\in\mathbb R:
N^{-\kappa}\le |t|\le N^\kappa
\right\}.
$$

The taskpack for PK4 imposed the following restrictions:

1. preserve the exact centered weight $\omega_{N,t}(m)$ ;
2. retain the $m\le N$ aggregate branch;
3. keep the prime/background cross term until it is bounded;
4. do not replace prime-only increments by $\Lambda$ without pricing prime powers;
5. obtain a fixed power rather than a logarithmic saving;
6. do not assume a fixed zero-free strip or fixed-power PNT remainder.

The present paper meets these requirements directly.

---

# 2. The centered von Mangoldt transform

Define

$$
\boxed{
\mathfrak L_N(t)
=
\sum_{m<2N}
(\Lambda(m)-1)\omega_{N,t}(m).
}
$$

The exact difference from the prime-only transform is

$$
\boxed{
\mathfrak R_N(t)
=
\mathfrak L_N(t)-\mathfrak M_N(t)
=
\sum_{\substack{p^a<2N\\a\ge2}}
(\log p)\omega_{N,t}(p^a).
}
$$

No term has been dropped.

Equivalently,

$$
\mathfrak M_N(t)
=
\mathfrak L_N(t)-\mathfrak R_N(t).
$$

The only question is whether $\mathfrak R_N$ is power-admissible in the exact middle-band norm.

---

# 3. Prime-power mass is square-root sized

Let

$$
\Pi_{\mathrm{pp}}(X)
=
\sum_{\substack{p^a\le X\\a\ge2}}
\log p.
$$

Since

$$
\Pi_{\mathrm{pp}}(X)
=
\sum_{a=2}^{\lfloor\log_2 X\rfloor}
\vartheta(X^{1/a}),
$$

the Chebyshev estimate

$$
\vartheta(y)\ll y
$$

gives

$$
\Pi_{\mathrm{pp}}(X)
\ll
X^{1/2}
+
(\log X)X^{1/3}.
$$

Consequently,

$$
\boxed{
\Pi_{\mathrm{pp}}(X)
\ll
X^{1/2}.
}
$$

at fixed-power resolution.

This is the only prime-power counting input required below.

---

# 4. The centered weight suppresses the prime-power correction

For $m\le N$,

$$
|\omega_{N,t}(m)|
=
\frac{|2^{it}-1|}{N}
\ll
\frac{\min(|t|,1)}{N}.
$$

For $N<m<2N$,

$$
\left|
\left(\frac{2N}{m}\right)^{it}-1
\right|
\le
\min\left(
|t|\log\frac{2N}{m},
2
\right)
\ll
\min(|t|,1),
$$

and therefore

$$
|\omega_{N,t}(m)|
\ll
\frac{\min(|t|,1)}{N}.
$$

Combining the two ranges gives:

## Theorem 4.1 — Uniform centered prime-power correction

For every real $t$,

$$
\boxed{
|\mathfrak R_N(t)|
\ll
N^{-1/2}\min(|t|,1).
}
$$

### Proof

By the preceding weight bound,

$$
|\mathfrak R_N(t)|
\ll
\frac{\min(|t|,1)}{N}
\sum_{\substack{p^a<2N\\a\ge2}}
\log p.
$$

Using

$$
\Pi_{\mathrm{pp}}(2N)\ll N^{1/2}
$$

gives the result.

$$
\Box
$$

This bound uses the centered factor. A non-centered prime-power replacement would lose the useful linear vanishing at $t=0$.

---

# 5. Prime powers cost an entire fixed power in energy

Define

$$
\mathcal E_{\mathrm{pp}}(N,\kappa)
=
\int_{\mathcal B_{N,\kappa}}
\frac{|\mathfrak R_N(t)|^2}{t^2}\,dt.
$$

Using Theorem 4.1, split the integral at $|t|=1$.

For

$$
N^{-\kappa}\le |t|\le1,
$$

we have

$$
\frac{|\mathfrak R_N(t)|^2}{t^2}
\ll
N^{-1}.
$$

For

$$
1\le |t|\le N^\kappa,
$$

we have

$$
\frac{|\mathfrak R_N(t)|^2}{t^2}
\ll
\frac{N^{-1}}{t^2}.
$$

Therefore:

## Theorem 5.1 — Fixed-power prime-power admissibility

For every fixed $0<\kappa\le1$,

$$
\boxed{
\mathcal E_{\mathrm{pp}}(N,\kappa)
\ll
N^{-1}.
}
$$

In particular,

$$
N^{-1}
\le
N^{-\kappa}
$$

for $0<\kappa\le1$, so the prime-power correction is admissible at every PESC exponent currently under consideration.

At the original PESC root scale, Paper 49 gives a factor $N^3$. Thus the prime-power correction contributes at most

$$
N^3\mathcal E_{\mathrm{pp}}
\ll
N^2,
$$

which is exactly lower-order at every fixed $\kappa<1$ and remains exponent-admissible at $\kappa=1$.

---

# 6. The cross term is explicitly priced

Introduce the weighted middle-band Hilbert norm

$$
\|F\|_{\kappa,N}^2
=
\int_{\mathcal B_{N,\kappa}}
\frac{|F(t)|^2}{t^2}\,dt.
$$

Then

$$
\mathfrak M_N
=
\mathfrak L_N-\mathfrak R_N.
$$

Hence the triangle inequality gives

$$
\left|
\|\mathfrak M_N\|_{\kappa,N}
-
\|\mathfrak L_N\|_{\kappa,N}
\right|
\le
\|\mathfrak R_N\|_{\kappa,N}
\ll
N^{-1/2}.
$$

Equivalently, if the energy is expanded,

$$
\mathcal E_{\mathbb P}
=
\mathcal E_{\Lambda}
+
\mathcal E_{\mathrm{pp}}
-
2\operatorname{Re}
\left\langle
\mathfrak L_N,\mathfrak R_N
\right\rangle_{\kappa,N},
$$

and Cauchy gives

$$
\left|
\left\langle
\mathfrak L_N,\mathfrak R_N
\right\rangle_{\kappa,N}
\right|
\le
\mathcal E_{\Lambda}^{1/2}
\mathcal E_{\mathrm{pp}}^{1/2}.
$$

Therefore the cross term has not been discarded. It is explicitly bounded by the prime-power Hilbert norm.

We obtain:

## Theorem 6.1 — Fixed-power prime-only / von Mangoldt equivalence

For every fixed $0<\kappa\le1$,

$$
\boxed{
\mathcal E_{\mathbb P}(N,\kappa)
\ll
N^{-\kappa+o(1)}
}
$$

if and only if

$$
\boxed{
\mathcal E_{\Lambda}(N,\kappa)
:=
\int_{\mathcal B_{N,\kappa}}
\frac{|\mathfrak L_N(t)|^2}{t^2}\,dt
\ll
N^{-\kappa+o(1)}.
}
$$

Create:

```text
B-RH-042
PESC_CENTERED_PRIME_TO_VON_MANGOLDT_FIXED_POWER_EQUIVALENCE
CERTIFIED
```

This is the fixed-power bridge demanded by PK4.

---

# 7. Exact discrete Abel reconstruction

The centered von Mangoldt transform has a second structure that is even more useful.

Let

$$
a_m=\Lambda(m)-1
$$

and define its exact integer cumulative sum

$$
A(m)
=
\sum_{n\le m}a_n.
$$

Since

$$
\sum_{n\le m}\Lambda(n)
=
\psi(m),
$$

we have exactly

$$
\boxed{
A(m)=\psi(m)-m.
}
$$

Define

$$
g_{N,t}(x)
=
\frac{(2N/x)^{it}-1}{x}.
$$

Then

$$
g_{N,t}(N)
=
\frac{2^{it}-1}{N},
$$

which is exactly the centered weight on the whole prefix $m\le N$, while

$$
g_{N,t}(2N)=0.
$$

Therefore the full weight may be viewed as

$$
w_m
=
\begin{cases}
g_{N,t}(N),&m\le N,\\
g_{N,t}(m),&N<m\le2N.
\end{cases}
$$

with $w_{2N}=0$.

Discrete summation by parts yields:

## Theorem 7.1 — Exact centered Abel root-error bridge

For every real $t$,

$$
\boxed{
\mathfrak L_N(t)
=
\sum_{m=N}^{2N-1}
(\psi(m)-m)
\left(
g_{N,t}(m)-g_{N,t}(m+1)
\right).
}
$$

### Proof

For any finite sequences,

$$
\sum_{m=1}^{M}a_mw_m
=
A(M)w_M
+
\sum_{m=1}^{M-1}
A(m)(w_m-w_{m+1}).
$$

Take

$$
M=2N.
$$

Because

$$
w_{2N}=0,
$$

the boundary term vanishes. Because $w_m$ is constant for $m\le N$, all differences with $m<N$ vanish. Hence

$$
\mathfrak L_N(t)
=
\sum_{m=N}^{2N-1}
A(m)
\left(
g_{N,t}(m)-g_{N,t}(m+1)
\right).
$$

Finally substitute

$$
A(m)=\psi(m)-m.
$$

$$
\Box
$$

Create:

```text
B-RH-043
PESC_CENTERED_VON_MANGOLDT_EXACT_DYADIC_ABEL_ROOT_ERROR_BRIDGE
CERTIFIED
```

The $m\le N$ aggregate branch has not been approximated or deleted. It is exactly what creates the initial value $g_{N,t}(N)$ in the Abel transform.

---

# 8. Kernel scale

Differentiate the continuous kernel:

$$
g_{N,t}(x)
=
(2N)^{it}x^{-1-it}-x^{-1}.
$$

Then

$$
g_{N,t}'(x)
=
x^{-2}
\left[
1-(1+it)\left(\frac{2N}{x}\right)^{it}
\right].
$$

For $N\le x\le2N$,

$$
\left|
1-(1+it)\left(\frac{2N}{x}\right)^{it}
\right|
\ll
|t|.
$$

The estimate is linear for $|t|\le1$ by Taylor expansion and is trivially $O(|t|)$ for $|t|\ge1$.

Therefore

$$
\boxed{
|g_{N,t}(m)-g_{N,t}(m+1)|
\ll
\frac{|t|}{N^2}.
}
$$

This estimate alone does not prove the fixed-power PESC bound. It only shows the physical scale of the exact Abel kernel.

Using only a pointwise PNT error estimate in Theorem 7.1 would immediately expose the circularity: RH is classically equivalent to

$$
\psi(x)
=
x+O(x^{1/2+\varepsilon})
$$

for every $\varepsilon>0$.

Thus PK5 cannot simply insert a fixed-power estimate for $\psi(x)-x$ unless that estimate has been independently established.

---

# 9. Why generic Dirichlet-polynomial mean square is not the missing theorem

The passage from $\mathfrak M_N$ to $\mathfrak L_N$ is now power-safe, but this does not make the remaining estimate generic.

A standard mean-value estimate for a length- $N$ Dirichlet polynomial with coefficients of natural prime size does not by itself produce

$$
N^{-\kappa}
$$

in the centered $t^{-2}$ middle-band norm. Such an argument sees coefficient energy and interval length, whereas the required gain is a root-scale cancellation statement for $\psi(m)-m$.

This is consistent with the Gallagher/Selberg philosophy: mean squares of Dirichlet or exponential sums are related to short-interval arithmetic energy, but the theorem needed here is the arithmetic contraction itself, not merely the transform identity.

Therefore PK5 should not be framed as "apply a generic mean-square theorem." It must exploit the specific centered root-error structure.

---

# 10. Zero-response calibration for PK5

This section is a calibration, not a certified replacement for a rigorous explicit-formula argument.

The classical explicit formula writes the Chebyshev error in terms of nontrivial zeta zeros. To understand what the centered Abel kernel does to one model zero, suppose formally that

$$
E_\psi(x)
=
-\frac{x^\rho}{\rho},
$$

where

$$
\rho=\beta+i\gamma.
$$

Replace the discrete Abel sum by its continuous scale model. Then the zero response is

$$
\mathfrak Z_{\rho,N}(t)
=
-\frac{N^{\rho-1}}{\rho}
\mathcal R_\rho(t),
$$

where

$$
\boxed{
\mathcal R_\rho(t)
=
\frac{(1+it)(2^{\rho-1}-2^{it})}
{\rho-1-it}
-
\frac{2^{\rho-1}-1}{\rho-1}.
}
$$

The centering is visible in

$$
\mathcal R_\rho(0)=0.
$$

When $t$ is near the zero ordinate $\gamma$, the denominator contains

$$
\rho-1-it
=
(\beta-1)+i(\gamma-t).
$$

Thus the translated Mellin variable is naturally aligned with zero ordinates.

For large fixed $|\gamma|$ and $t=\gamma$, the outside factor $1/\rho$ cancels the linear $t$ -growth of the first numerator, leaving the scale

$$
|\mathfrak Z_{\rho,N}(\gamma)|
\asymp_\rho
N^{\beta-1}
$$

away from accidental coefficient cancellation.

Consequently the natural weighted energy scale of an isolated zero is heuristically

$$
N^{2\beta-2}.
$$

On the critical line,

$$
\beta=\frac12,
$$

this is

$$
N^{-1}.
$$

This explains why the endpoint $\kappa=1$ is the natural RH-scale PESC exponent.

However, this calibration is not a proof of a zero-by-zero lower or upper bound for the full transform. A rigorous PK5 argument must price:

1. truncation in the explicit formula;
2. zero-zero cross terms;
3. possible cancellation between nearby ordinates;
4. low zeros and conjugate pairing;
5. the difference between the discrete Abel sum and any continuous response model.

No zero-response theorem is certified in this section.

---

# 11. External calibration

Two classical facts are used only as calibration boundaries.

First, the Chebyshev function is

$$
\psi(x)
=
\sum_{n\le x}\Lambda(n),
$$

and the explicit formula relates $\psi(x)-x$ to the nontrivial zeros of $\zeta(s)$.

Second, RH is equivalent to

$$
\psi(x)
=
x+O(x^{1/2+\varepsilon})
$$

for every $\varepsilon>0$.

A standard reference is NIST DLMF, Section 25.16.

The use of Gallagher-type mean-square transforms as a bridge between exponential/Dirichlet sums and short-interval arithmetic energy is also classical. This paper does not claim that such transform philosophy is new. Its internal contribution is the exact centered PESC-compatible weight, the fixed-power prime-power ledger, and the exact Abel reconstruction of the inherited root transform.

---

# 12. PK4 audit

## Check 1 — preserve the exact centered weight

PASS.

The same $\omega_{N,t}(m)$ from Paper 49 is used throughout.

## Check 2 — retain the $m\le N$ aggregate branch

PASS.

The exact Abel identity uses

$$
g_{N,t}(N)
=
\frac{2^{it}-1}{N},
$$

so the prefix aggregate is built into the initial value of the kernel.

## Check 3 — keep the prime/background cross term

PASS.

The weighted Hilbert-space cross term is explicitly bounded by Cauchy and is not deleted.

## Check 4 — price prime powers

PASS.

The entire prime-power correction has middle-band energy

$$
O(N^{-1}).
$$

## Check 5 — obtain a fixed power

PASS.

The correction is one full power $N^{-1}$, not merely logarithmic.

## Check 6 — remain on the polynomial middle band

PASS.

All energy comparisons are made on

$$
N^{-\kappa}\le|t|\le N^\kappa.
$$

## Check 7 — do not assume a fixed zero-free strip

PASS.

No zero-free strip stronger than classical unconditional knowledge is used.

## Check 8 — do not assume a fixed-power PNT remainder

PASS.

The Abel bridge is an identity. No power estimate for $\psi(x)-x$ is inserted.

---

# 13. PK4 closure

The prime-only centered PESC transform has now been converted to a von Mangoldt transform with a fixed-power-admissible correction:

$$
\mathfrak M_N
=
\mathfrak L_N
-
\mathfrak R_N,
$$

where

$$
\|\mathfrak R_N\|_{\kappa,N}^2
\ll
N^{-1}.
$$

The von Mangoldt transform has then been recast exactly as

$$
\mathfrak L_N(t)
=
\sum_{m=N}^{2N-1}
(\psi(m)-m)
\Delta g_{N,t}(m).
$$

Therefore close PK4 as:

```text
CLOSED_AS_FIXED_POWER_PRIME_POWER_REMOVAL_AND_EXACT_CENTERED_ABEL_ROOT_ERROR_BRIDGE
```

This closure is structural. It proves no fixed-power PESC estimate.

---

# 14. State transition

Advance the research state candidate from

$$
v1.40
$$

to

$$
v1.41.
$$

Campaign 44 becomes:

```text
PK1 CLOSED
PK2 CLOSED
PK3 CLOSED
PK4 CLOSED
PK5 OPEN_FIXED_POWER_PESC_ADMISSION
```

Add:

```text
B-RH-042
PESC_CENTERED_PRIME_TO_VON_MANGOLDT_FIXED_POWER_EQUIVALENCE
CERTIFIED
```

and

```text
B-RH-043
PESC_CENTERED_VON_MANGOLDT_EXACT_DYADIC_ABEL_ROOT_ERROR_BRIDGE
CERTIFIED
```

No RH certificate is created.

---

# 15. Exact next target

PK5 now receives the exact root object

$$
\boxed{
\mathfrak L_N(t)
=
\sum_{m=N}^{2N-1}
(\psi(m)-m)
\left(
g_{N,t}(m)-g_{N,t}(m+1)
\right).
}
$$

The fixed-power admission target is

$$
\boxed{
\int_{N^{-\kappa}\le|t|\le N^\kappa}
\frac{|\mathfrak L_N(t)|^2}{t^2}\,dt
\ll
N^{-\kappa+o(1)}.
}
$$

The recommended attack order is:

```text
PK5/Z1  RIGOROUS_TRUNCATED_EXPLICIT_FORMULA_INSERTION
PK5/Z2  CENTERED_ZERO_RESPONSE_KERNEL_EXTRACTION
PK5/Z3  ZERO_WINDOW_CROSS_TERM_AND_NEAR_ORDINATE_AUDIT
PK5/Z4  OFF_CRITICAL_ANTI_CANCELLATION_OR_CRITICAL_LINE_ADMISSION
```

Hard rejections:

```text
ASSUME_RH_SIZED_PNT_ERROR
ASSUME_FIXED_ZERO_FREE_STRIP
DROP_ZERO_ZERO_CROSS_TERMS
TREAT_SINGLE_ZERO_CALIBRATION_AS_FULL_EXPLICIT_FORMULA
USE_GENERIC_DIRICHLET_MEAN_SQUARE_AS_FIXED_POWER_CONTRACTION
IGNORE_EXPLICIT_FORMULA_TRUNCATION
```

---

# 16. Conclusion

Campaign 44 has moved from a prime-only root statistic to the exact Chebyshev root error without paying a power-sized loss.

The key chain is now

$$
\boxed{
\begin{aligned}
\text{PESC Brownian root energy}
&\longleftrightarrow
\text{centered prime Mellin energy}
\\
&\longleftrightarrow
\text{centered von Mangoldt Mellin energy}
\\
&=
\text{centered Abel transform of }\psi(m)-m.
\end{aligned}
}
$$

The first equivalence is Paper 49. The second and third are the content of this paper.

The remaining obstacle is no longer prime powers, endpoint aggregation, local frame conditioning, or prime/background bookkeeping.

It is the fixed-power arithmetic contraction of the centered Chebyshev root error itself.

That is precisely where a genuine RH-scale argument must now operate.
