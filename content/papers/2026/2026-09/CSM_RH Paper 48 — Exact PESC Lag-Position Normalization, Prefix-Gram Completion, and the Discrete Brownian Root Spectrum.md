# CSM_RH Paper 48
## Exact PESC Lag-Position Normalization, Prefix-Gram Completion, and the Discrete Brownian Root Spectrum

**Project:** CSM_RH  
**Paper:** 48  
**Version:** 0.1  
**Date:** 2026-09-07  
**Campaign:** 44 — `PESC_TRIANGULAR_LAG_KERNEL_ATTACK`  
**Tracks:** PK1 — `EXACT_PESC_TRIANGULAR_KERNEL_NORMALIZATION`; PK2 — `ROOT_SPECTRAL_REPRESENTATION`  
**Canonical state transition:** v1.38 to v1.39

---

# 0. Trust boundary

This paper continues directly from CSM_RH Paper 47.

Paper 47 closed the Heath--Brown component detour and returned the proof architecture to the root prime-error observable

$$
\mathcal C_N^\vartheta
=
\sum_{h\ge1}\sum_m w_N(m+h)c_mc_{m+h},
$$

where

$$
c_n=1_{\mathbb P}(n)\log n-1
$$

and

$$
w_N(n)
=
\begin{cases}
N,&1\le n\le N,\\
2N-n,&N<n<2N,\\
0,&n\ge2N.
\end{cases}
$$

Campaign 44 asks for root-observing control of this exact triangular positive-lag kernel.

The present paper completes two structural tracks.

PK1 gives the exact lag-position kernel, its lag mass, its plateau/ramp decomposition, and a positive-semidefinite completion.

PK2 passes to the exact quotient seen by the dyadic energy and diagonalizes it explicitly as the discrete Brownian covariance kernel.

The resulting spectrum proves that the root low-frequency mode is not removable: the lowest mode has weight of order $N^2$, and on the pure-prefix test direction of the exact root quotient it alone carries an asymptotic fraction $8/\pi^2$ of the quotient energy. This is a kernel-observability witness, not a statement about the modal distribution of the actual prime-error sequence.

No fixed-power PESC estimate is proved.
No proof or disproof of RH is claimed.
No fixed zero-free strip, fixed-power PNT remainder, or fixed-power Mertens estimate is assumed.

---

# 1. Inherited root identities

Define

$$
B(j)=\sum_{n\le j}c_n=\vartheta(j)-j.
$$

The dyadic root energy is

$$
\boxed{
J_N^\vartheta
=
\sum_{j=N}^{2N-1}B(j)^2.
}
$$

The diagonal is

$$
\boxed{
D_N^\vartheta
=
\sum_{n<2N}w_N(n)c_n^2.
}
$$

The PESC correlation is

$$
\boxed{
\mathcal C_N^\vartheta
=
\sum_{n<2N}w_N(n)c_nB(n-1).
}
$$

Paper 11 certified the exact identity

$$
\boxed{
J_N^\vartheta
=
D_N^\vartheta+2\mathcal C_N^\vartheta
}
$$

and the diagonal bound

$$
\boxed{
D_N^\vartheta=O(N^2\log N).
}
$$

Hence for every fixed

$$
0<\kappa\le1,
$$

PESC $(\kappa)$ is exponent-equivalent to

$$
J_N^\vartheta\ll N^{3-\kappa+o(1)}.
$$

The goal of PK1--PK2 is not to reprove that equivalence, but to expose the exact kernel and spectral geometry of the root energy that PESC must control.

---

# 2. PK1: exact lag-position kernel

Write

$$
n=m+h,
\qquad
h\ge1.
$$

Define

$$
\boxed{
K_N(m,h)
=
w_N(m+h).
}
$$

The support conditions are

$$
m\ge1,
\qquad
h\ge1,
\qquad
m+h<2N.
$$

Therefore the exact positive-lag kernel is

$$
\boxed{
K_N(m,h)
=
\begin{cases}
N,&m+h\le N,\\
2N-m-h,&N<m+h<2N,\\
0,&m+h\ge2N.
\end{cases}
}
$$

and

$$
\boxed{
\mathcal C_N^\vartheta
=
\sum_{h=1}^{2N-2}
\sum_{m=1}^{2N-h-1}
K_N(m,h)c_mc_{m+h}.
}
$$

This retains the full position dependence.
The kernel is not a function of lag $h$ alone.

Create:

```text
B-RH-032
EXACT_PESC_LAG_POSITION_KERNEL_NORMALIZATION
CERTIFIED
```

---

# 3. Exact lag mass

Define the unsigned lag mass

$$
M_N(h)=\sum_m K_N(m,h).
$$

For

$$
1\le h\le N-1,
$$

the plateau contributes

$$
N(N-h),
$$

while the descending tail contributes

$$
1+2+\cdots+(N-1)
=
\frac{N(N-1)}2.
$$

Hence

$$
\boxed{
M_N(h)
=
N(N-h)+\frac{N(N-1)}2,
\qquad
1\le h\le N-1.
}
$$

For

$$
N\le h\le2N-2,
$$

there is no plateau and

$$
\boxed{
M_N(h)
=
\frac{(2N-h-1)(2N-h)}2.
}
$$

Thus the root kernel has a macroscopic plateau at short and medium lags and a genuinely triangular terminal tail.

The lag mass is useful for normalization, but replacing the signed position-dependent sum by

$$
M_N(h)
\left|
\text{average correlation at lag }h
\right|
$$

would already invoke an absolute value not present in PESC.
No such replacement is made here.

---

# 4. The early prefix block is not a lower-order boundary term

Split at the plateau endpoint $N$.
Then

$$
\mathcal C_N^\vartheta
=
N\sum_{1\le m<n\le N}c_mc_n
+
\sum_{N<n<2N}(2N-n)c_nB(n-1).
$$

The first term is exactly

$$
\boxed{
N\sum_{1\le m<n\le N}c_mc_n
=
\frac N2
\left(
B(N)^2-
\sum_{n\le N}c_n^2
\right).
}
$$

The term

$$
\frac N2B(N)^2
$$

can be of the full trivial root scale $N^3$.
Therefore the plateau cannot be reclassified as a harmless endpoint correction.

Only the already certified diagonal

$$
D_N^\vartheta=O(N^2\log N)
$$

is automatically lower order for a fixed-power PESC target with $0<\kappa\le1$.

Create:

```text
O-RH-125
PESC_EARLY_PREFIX_PLATEAU_IS_ROOT_SCALE_NOT_A_BOUNDARY_ERROR
CERTIFIED
```

---

# 5. Symmetric prefix-Gram completion

For

$$
1\le m,n<2N,
$$

define the symmetric kernel

$$
\boxed{
G_N(m,n)
=
w_N(\max\{m,n\}).
}
$$

Let the endpoint-incidence matrix be

$$
V_N(j,n)=1_{n\le j},
\qquad
N\le j\le2N-1,
\quad
1\le n<2N.
$$

Then

$$
(V_N^TV_N)(m,n)
=
\#\{j\in[N,2N-1]:\max(m,n)\le j\}
=
w_N(\max\{m,n\}).
$$

Hence

$$
\boxed{
G_N=V_N^TV_N.
}
$$

In particular $G_N$ is positive semidefinite.
Moreover

$$
\boxed{
J_N^\vartheta
=
\sum_{m,n<2N}G_N(m,n)c_mc_n.
}
$$

Its diagonal is exactly

$$
\sum_{n<2N}G_N(n,n)c_n^2
=
D_N^\vartheta.
$$

Therefore

$$
\boxed{
\mathcal C_N^\vartheta
=
\frac12
\left(
\sum_{m,n<2N}G_N(m,n)c_mc_n
-
D_N^\vartheta
\right).
}
$$

This is the exact positive-semidefinite completion of the triangular positive-lag kernel.

Create:

```text
B-RH-033
PESC_PREFIX_GRAM_PSD_COMPLETION_AND_QUOTIENT
CERTIFIED
```

---

# 6. Rank, nullspace, and the exact root quotient

The matrix $V_N$ has $N$ linearly independent rows, so

$$
\boxed{
\operatorname{rank}G_N=N.
}
$$

Since $G_N$ acts on $2N-1$ coordinates,

$$
\dim\ker G_N=N-1.
$$

The nullspace is exactly

$$
\boxed{
\ker G_N
=
\left\{
(x_1,\ldots,x_N,0,\ldots,0):
\sum_{n=1}^N x_n=0
\right\}.
}
$$

Thus the dyadic root energy does not separately observe all first- $N$ increments.
It observes them through the single aggregate coordinate

$$
\boxed{
y_0=B(N).
}
$$

For the tail define

$$
\boxed{
y_r=c_{N+r},
\qquad
1\le r\le N-1.
}
$$

Then for

$$
0\le s\le N-1,
$$

$$
B(N+s)
=
\sum_{r=0}^{s}y_r.
$$

Hence

$$
\boxed{
J_N^\vartheta
=
\sum_{s=0}^{N-1}
\left(
\sum_{r=0}^{s}y_r
\right)^2.
}
$$

Equivalently,

$$
\boxed{
J_N^\vartheta
=
\sum_{r,s=0}^{N-1}
\left(N-\max\{r,s\}\right)y_ry_s.
}
$$

This $N$ -dimensional quotient is the exact root-observing state for PK2.

---

# 7. Discrete Brownian covariance form

Reverse the quotient coordinates by setting

$$
z_i=y_{N-i},
\qquad
1\le i\le N.
$$

Then

$$
N-\max\{N-i,N-j\}
=
\min\{i,j\}.
$$

Therefore

$$
\boxed{
J_N^\vartheta
=
z^TH_Nz,
\qquad
H_N(i,j)=\min\{i,j\}.
}
$$

The matrix $H_N$ is the standard discrete Brownian covariance kernel.
It is positive definite.

Its inverse is the tridiagonal matrix

$$
\boxed{
H_N^{-1}
=
\begin{pmatrix}
2&-1&0&\cdots&0\\
-1&2&-1&\ddots&\vdots\\
0&\ddots&\ddots&\ddots&0\\
\vdots&\ddots&-1&2&-1\\
0&\cdots&0&-1&1
\end{pmatrix}.
}
$$

Thus the root energy is exactly the inverse of a first-difference Laplacian with one free endpoint.

---

# 8. PK2: exact spectral diagonalization

For

$$
k=1,\ldots,N,
$$

define

$$
\theta_k
=
\frac{(2k-1)\pi}{2N+1}
$$

and

$$
\boxed{
\phi_k(i)
=
\frac{2}{\sqrt{2N+1}}
\sin(i\theta_k),
\qquad
1\le i\le N.
}
$$

These vectors form an orthonormal basis.
The corresponding eigenvalues of $H_N$ are

$$
\boxed{
\mu_k
=
\frac{1}{2-2\cos\theta_k}
=
\frac{1}{4\sin^2(\theta_k/2)}.
}
$$

Therefore:

## Theorem 8.1 — Exact PESC root spectrum

If

$$
a_k=\langle z,\phi_k\rangle,
$$

then

$$
\boxed{
J_N^\vartheta
=
\sum_{k=1}^{N}
\mu_k|a_k|^2.
}
$$

The lowest spectral mode has

$$
\boxed{
\mu_1
=
\frac{1}{4\sin^2\left(\frac{\pi}{4N+2}\right)}
=
\frac{4N^2}{\pi^2}(1+o(1)).
}
$$

The highest mode has

$$
\boxed{
\mu_N
=
\frac{1}{4\cos^2\left(\frac{\pi}{2N+1}\right)}
=
\frac14+o(1).
}
$$

Hence

$$
\boxed{
\operatorname{cond}(H_N)
=
\frac{\mu_1}{\mu_N}
=
\frac{16}{\pi^2}N^2(1+o(1)).
}
$$

Create:

```text
B-RH-034
DISCRETE_BROWNIAN_ROOT_SPECTRAL_DIAGONALIZATION
CERTIFIED
```

---

# 9. The lowest mode is a genuine root-kernel mode

Consider the pure-prefix test vector in the exact root quotient

$$
y_0=B(N),
\qquad
y_1=\cdots=y_{N-1}=0.
$$

Equivalently

$$
z_N=B(N),
\qquad
z_1=\cdots=z_{N-1}=0.
$$

Then every endpoint has the same prefix error and

$$
\boxed{
J_N^\vartheta
=
N B(N)^2.
}
$$

The contribution of the first spectral mode alone is

$$
\mu_1|a_1|^2
=
\mu_1\phi_1(N)^2B(N)^2.
$$

Let

$$
\alpha_N=\frac{\pi}{4N+2}.
$$

Since

$$
\phi_1(N)^2
=
\frac{4}{2N+1}\cos^2\alpha_N
$$

and

$$
\mu_1
=
\frac{1}{4\sin^2\alpha_N},
$$

we obtain

$$
\boxed{
\frac{\mu_1|a_1|^2}{J_N^\vartheta}
=
\frac{\cot^2\alpha_N}{N(2N+1)}
\longrightarrow
\frac{8}{\pi^2}.
}
$$

Thus the first mode alone carries asymptotically about $81\%$ of this root-kernel quotient direction.

Consequently a deterministic spectral bridge that excises the principal low-frequency mode is not root-observing on the full exact quotient space.
It loses a fixed positive fraction on an explicit quotient test direction before any arithmetic estimate begins.
This does not assert that the actual prime-error vector places $81\%$ of its energy in the first mode.

Create:

```text
O-RH-126
PESC_LOWEST_BROWNIAN_MODE_CARRIES_A_FIXED_FRACTION_OF_A_ROOT_SCALE_PREFIX_DIRECTION
CERTIFIED AS ROOT-OBSERVABILITY BARRIER
```

The power-sized spectral spread also implies that any reconstruction argument based on inverting a low-frequency-suppressing first-difference representation must explicitly pay its conditioning cost.
The spread itself is

$$
\Theta(N^2)
$$

in energy.

Create:

```text
O-RH-127
PESC_ROOT_KERNEL_HAS_POWER_SIZED_SPECTRAL_SPREAD
CERTIFIED AS SYNTHESIS-CONDITIONING WARNING
```

This does not by itself close PK3.
It only fixes the ledger against unpriced low-frequency recovery.

---

# 10. Fixed-power PESC in spectral form

By the inherited identity

$$
J_N^\vartheta
=
D_N^\vartheta+2\mathcal C_N^\vartheta
$$

and

$$
D_N^\vartheta=O(N^2\log N),
$$

Theorem 8.1 gives:

## Theorem 10.1 — PESC / root-spectrum equivalence

For every fixed

$$
0<\kappa\le1,
$$

the following are exponent-equivalent:

$$
\boxed{
|\mathcal C_N^\vartheta|
\ll
N^{3-\kappa+o(1)}
}
$$

and

$$
\boxed{
\sum_{k=1}^{N}
\mu_k|a_k|^2
\ll
N^{3-\kappa+o(1)}.
}
$$

This is a root-observing spectral reformulation, not a new fixed-power estimate.

Create:

```text
B-RH-035
PESC_FIXED_POWER_EQUIVALENT_TO_WEIGHTED_ROOT_SPECTRAL_ENERGY
CERTIFIED
```

---

# 11. What PK1 and PK2 do and do not solve

PK1 now supplies:

1. the exact positive-lag position kernel;
2. the exact lag mass;
3. the non-negligible prefix plateau;
4. the PSD prefix-Gram completion;
5. the exact $N$ -dimensional root quotient.

PK2 now supplies:

1. the exact discrete Brownian covariance form;
2. a complete orthonormal sine basis;
3. explicit eigenvalues;
4. an exact low-frequency root witness;
5. the power-sized conditioning ledger that PK3 must respect.

Neither track proves

$$
J_N^\vartheta
\ll
N^{3-\kappa+o(1)}
$$

for any fixed $\kappa>0$.

No arithmetic contraction has yet been obtained.

PK1 closes as

```text
CLOSED_AS_EXACT_LAG_POSITION_NORMALIZATION_WITH_PREFIX_GRAM_COMPLETION
```

PK2 closes as

```text
CLOSED_AS_EXACT_BROWNIAN_SPECTRAL_REPRESENTATION_WITH_LOW_MODE_PRESERVED
```

---

# 12. Interface with translated windows

Paper 42 used Gaussian translated Mellin kernels of the form

$$
\frac{1}{mn}
\exp\left(-iQ\log(m/n)\right)
\widehat\Phi\left(Y\log(m/n)\right).
$$

The PESC root completion is instead

$$
G_N(m,n)=w_N(\max\{m,n\}),
$$

which is explicitly position dependent.

Therefore PK3 cannot consist only of declaring the Paper 42 high-frequency window to be the root kernel.
A successful synthesis must account for both:

1. ratio/frequency localization;
2. endpoint-position localization.

Moreover it must retain the $k=1$ Brownian mode and price any reconstruction conditioning against the fixed-power ledger.

This paper does not decide whether such a power-safe frame exists.
That is the next track.

---

# 13. Campaign status

Campaign 44 remains active.

PK1:

```text
CLOSED_AS_EXACT_LAG_POSITION_NORMALIZATION_WITH_PREFIX_GRAM_COMPLETION
```

PK2:

```text
CLOSED_AS_EXACT_BROWNIAN_SPECTRAL_REPRESENTATION_WITH_LOW_MODE_PRESERVED
```

No fixed-power theorem has been proved.

The root frontiers remain

```text
F-RH-010 PESC  OPEN
F-RH-016 MLEPG OPEN
```

and

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 14. Next continuation

Proceed to

```text
CSM_RH Campaign 44 / PK3
TRANSLATED_WINDOW_SYNTHESIS
```

The required question is now sharply posed:

Can the exact Brownian root kernel, including its principal low-frequency mode and endpoint-position dependence, be reconstructed or dominated by a controlled family of translated frequency windows with no power-sized loss?

A valid PK3 theorem must state the synthesis operator and its condition number explicitly.
A logarithmic or $N^{o(1)}$ loss may be admissible at exponent resolution.
A loss $N^{\delta}$ for fixed $\delta>0$ consumes fixed-power gain and must be charged explicitly.

Paper 49 does not yet exist.
