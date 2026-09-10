# CSM_RH Paper 49
## Matching-Scale Local/Coarse Brownian Synthesis, Logarithmic Time Change, and the Centered Mellin Root-Energy Bridge

**Project:** CSM_RH  
**Paper:** 49  
**Version:** 0.2  
**Date:** 2026-09-08  
**Campaign:** 44 — `PESC_TRIANGULAR_LAG_KERNEL_ATTACK`  
**Track:** PK3 — `TRANSLATED_WINDOW_SYNTHESIS`  
**Candidate state transition:** v1.39 to v1.40

---

# 0. Trust boundary

This paper continues directly from CSM_RH Papers 46--48.

Paper 46 closed the structured-weight decoupling route at the component level. In particular, the exact restricted-convolution weight has natural exponent-scale energy,

$$
\sum_n r_X(n)^2=X^{1+o(1)},
$$

polynomial-prime Ramare marking has only bounded pointwise multiplicity, and factor bipartitions return to determinant fibres without a geometric fixed-power reserve. Consequently Paper 49 does not reopen coefficient-smallness, bounded-multiplicity marking, or absolute determinant-fibre counting as candidate fixed-power mechanisms.

Paper 47 then recombined the Heath--Brown $j$ -levels exactly back to the root prime observable and closed Campaign 43 as

```text
COMPONENT_MECHANISMS_EXHAUSTED_AND_EXACTLY_RECOUPLED_TO_ROOT_PRIME_ERROR
```

Paper 48 began Campaign 44 and proved that the exact PESC root quotient has Brownian covariance kernel

$$
H_N(i,j)=\min(i,j),
$$

with largest eigenvalue of order $N^2$, smallest eigenvalue of order $1$, and condition number

$$
\operatorname{cond}(H_N)
=
\frac{16}{\pi^2}N^2(1+o(1)).
$$

Paper 48 therefore left PK3 with the following non-negotiable requirements:

1. state the synthesis operator explicitly;
2. retain endpoint-position information as well as ratio/frequency information;
3. preserve the Brownian low-frequency root mode;
4. price every frame or reconstruction condition-number loss;
5. distinguish exact reconstruction from one-sided domination;
6. do not identify the Paper 42 translated Mellin kernel with the PESC root kernel without a deterministic bridge;
7. do not excise low frequencies and defer their recovery without charging the recovery cost.

The present paper closes the deterministic synthesis problem at this level.

It proves five main facts.

First, positive frame synthesis obeys a spectral-spread conservation law: the $N^2$ Brownian stiffness cannot disappear under a stable change of frame.

Second, the corresponding local/coarse scale is constructively attainable. An exact block-Fourier decomposition splits $H_N$ into compactly supported local integrated modes plus a coarse remainder of rank at most $\lceil N/L\rceil$ when the maximum local block length is $L$.

Third, a logarithmic endpoint coordinate transforms the Brownian root kernel into a Mellin-compatible Brownian kernel with only constant distortion:

$$
N G_N^{\log}
\preceq
H_N
\preceq
2N G_N^{\log}.
$$

Fourth, $G_N^{\log}$ admits an exact centered Fourier representation, which turns the PESC root energy into a centered Mellin $t^{-2}$ energy with only absolute constant distortion.

Fifth, Gaussian translated windows of this centered Mellin energy contain the Paper 42 ratio kernel as their first term, together with explicit endpoint-centering terms. Thus the earlier ratio-only kernel is recovered as a component of the root-observing synthesis rather than incorrectly identified with the root kernel itself.

No fixed-power PESC estimate is proved. No proof or disproof of RH is claimed. No fixed zero-free strip, fixed-power PNT remainder, fixed-power Mertens estimate, or unproved prime-correlation theorem is assumed.

---

# 1. Inherited PESC root quotient

Define the prime-error increments

$$
c_n
=
1_{\mathbb P}(n)\log n-1,
$$

and

$$
B(j)
=
\sum_{n\le j}c_n
=
\vartheta(j)-j.
$$

Paper 48 certified the dyadic root energy

$$
\boxed{
J_N^\vartheta
=
\sum_{j=N}^{2N-1}B(j)^2.
}
$$

The exact root quotient coordinates are

$$
y_0=B(N),
$$

and

$$
y_r=c_{N+r},
\qquad
1\le r\le N-1.
$$

After reversal,

$$
z_i=y_{N-i},
\qquad
1\le i\le N,
$$

so explicitly

$$
\boxed{
z_N=B(N)
}
$$

and

$$
\boxed{
z_i=c_{2N-i},
\qquad
1\le i<N.
}
$$

Paper 48 proved

$$
\boxed{
J_N^\vartheta
=
z^*H_Nz,
\qquad
H_N(i,j)=\min(i,j).
}
$$

For every fixed

$$
0<\kappa\le1,
$$

PESC $(\kappa)$ is exponent-equivalent to

$$
\boxed{
J_N^\vartheta
\ll
N^{3-\kappa+o(1)}.
}
$$

The whole purpose of PK3 is therefore to construct a power-safe bridge from this exact root form to translated frequency variables without destroying its endpoint geometry.

---

# 2. Cumulative-sum factorization

Let $C_N$ be the lower-triangular cumulative-sum matrix

$$
(C_N)_{ij}
=
1_{j\le i}.
$$

Then

$$
(C_NC_N^*)_{ij}
=
\sum_{r=1}^N
1_{r\le i}1_{r\le j}
=
\min(i,j).
$$

Hence

$$
\boxed{
H_N=C_NC_N^*.
}
$$

For $u\in\mathbb C^N$ define suffix sums

$$
S_k(u)
=
\sum_{i=k}^N u_i.
$$

Since

$$
(C_N^*u)_k=S_k(u),
$$

we have the exact endpoint-position identity

$$
\boxed{
u^*H_Nu
=
\sum_{k=1}^N
\left|
\sum_{i=k}^Nu_i
\right|^2.
}
$$

This formula will be used twice: first to audit local/coarse synthesis and then to control the slowly varying dyadic multiplier that appears in the Mellin time change.

---

# 3. Spectral-spread conservation under positive frame synthesis

Let

$$
T:\mathbb C^N\to\mathbb C^M
$$

be a frame analysis operator satisfying

$$
A\|x\|_2^2
\le
\|Tx\|_2^2
\le
B\|x\|_2^2.
$$

Let

$$
W=\operatorname{diag}(w_1,\ldots,w_M)
$$

with

$$
0<w_{\min}\le w_\alpha\le w_{\max}.
$$

Assume the synthesized positive operator

$$
S=T^*WT
$$

is uniformly comparable to the Brownian root kernel:

$$
c_-H_N
\preceq
S
\preceq
c_+H_N.
$$

## Theorem 3.1 — Frame-weight spectral-spread conservation

Under the preceding assumptions,

$$
\boxed{
\frac BA
\frac{w_{\max}}{w_{\min}}
\ge
\frac{c_-}{c_+}
\operatorname{cond}(H_N).
}
$$

Therefore

$$
\boxed{
\frac BA
\frac{w_{\max}}{w_{\min}}
\ge
\frac{c_-}{c_+}
\frac{16}{\pi^2}N^2(1+o(1)).
}
$$

### Proof

The frame bounds give

$$
AI\preceq T^*T\preceq BI.
$$

Since

$$
w_{\min}I\preceq W\preceq w_{\max}I,
$$

we obtain

$$
w_{\min}A I
\preceq
T^*WT
\preceq
w_{\max}B I.
$$

Hence

$$
\operatorname{cond}(S)
\le
\frac BA
\frac{w_{\max}}{w_{\min}}.
$$

The comparison with $H_N$ gives

$$
\operatorname{cond}(S)
\ge
\frac{c_-}{c_+}
\operatorname{cond}(H_N).
$$

Combining the inequalities proves the theorem.

$$
\Box
$$

Create:

```text
B-RH-036
PESC_FRAME_WEIGHT_SPECTRAL_SPREAD_CONSERVATION
CERTIFIED
```

The theorem does not say translated windows are impossible. It says the $N^2$ root stiffness must remain visible somewhere in the synthesis ledger.

---

# 4. Submacroscopic positive synthesis tax

Suppose $T_L$ is built from physical windows of support length at most $L$ and has Bessel bound

$$
\|T_Lx\|_2^2
\le
B_0\|x\|_2^2,
$$

with

$$
B_0=N^{o(1)}.
$$

Assume positive coefficient weights obey the natural local Brownian scale

$$
0<w_\alpha
\le
C_0L^2N^{o(1)}.
$$

Set

$$
S_L=T_L^*W_LT_L.
$$

If full root domination requires

$$
H_N
\preceq
C_{\mathrm{rec}}S_L,
$$

then evaluation on the principal Brownian eigenvector gives

$$
\mu_1
\le
C_{\mathrm{rec}}C_0B_0L^2N^{o(1)}.
$$

Since

$$
\mu_1
=
\frac{4}{\pi^2}N^2(1+o(1)),
$$

we obtain

## Theorem 4.1 — Submacroscopic reconstruction tax

$$
\boxed{
C_{\mathrm{rec}}
\gtrsim
\left(\frac NL\right)^2N^{-o(1)}.
}
$$

Thus for

$$
L=N^{1-\eta},
$$

purely submacroscopic positive synthesis pays at least

$$
\boxed{
N^{2\eta-o(1)}.
}
$$

Equivalently, a local arithmetic gain $N^{-\delta}$ cannot be promoted to a root gain before the deterministic exponent tax is subtracted.

Create:

```text
O-RH-128
PESC_SUBMACROSCOPIC_POSITIVE_SYNTHESIS_PAYS_POWER_RECONSTRUCTION_TAX
CERTIFIED AS PK3 CONDITIONING BARRIER
```

This is the no-free-lunch side of PK3. The next section shows that its coarse-dimension scale is nevertheless attainable by an exact construction.

---

# 5. Exact block-Fourier local/coarse synthesis

Partition

$$
\{1,\ldots,N\}
$$

into consecutive blocks

$$
I_1,\ldots,I_B
$$

with block lengths

$$
\ell_b=|I_b|\le L.
$$

One may choose all but the last block to have length $L$, so

$$
\boxed{
B\le\left\lceil\frac NL\right\rceil.
}
$$

On each block $I_b$, let

$$
q_{b,r},
\qquad
0\le r<\ell_b,
$$

be the normalized discrete Fourier basis. In local coordinates $s=0,\ldots,\ell_b-1$,

$$
q_{b,r}(s)
=
\ell_b^{-1/2}
\exp\left(
\frac{2\pi i r s}{\ell_b}
\right).
$$

Extend each $q_{b,r}$ by zero outside $I_b$. The family over all blocks is an orthonormal basis of $\mathbb C^N$.

Define integrated atoms

$$
\boxed{
\psi_{b,r}=C_Nq_{b,r}.
}
$$

Since the $q_{b,r}$ form an orthonormal basis,

$$
I
=
\sum_{b,r}q_{b,r}q_{b,r}^*,
$$

and therefore

$$
\boxed{
H_N
=
C_NIC_N^*
=
\sum_{b,r}
\psi_{b,r}\psi_{b,r}^*.
}
$$

This reconstruction is exact.

## 5.1 Zero-mean local modes stay local after integration

For

$$
r\ne0,
$$

we have

$$
\sum_{s=0}^{\ell_b-1}q_{b,r}(s)=0.
$$

Before the block begins, $C_Nq_{b,r}$ is zero. After the block ends, the cumulative sum is the total block sum, which is also zero. Hence

$$
\boxed{
\operatorname{supp}(\psi_{b,r})
\subseteq
I_b,
\qquad
r\ne0.
}
$$

Thus every nonconstant block-Fourier increment mode becomes a genuinely compact local window after cumulative integration.

## 5.2 Exact local atom energy

For

$$
1\le r<\ell_b,
$$

inside the block the partial Fourier sum gives

$$
\left|
\sum_{s=0}^{m-1}
q_{b,r}(s)
\right|^2
=
\frac1{\ell_b}
\frac{
\sin^2(\pi r m/\ell_b)
}{
\sin^2(\pi r/\ell_b)
}.
$$

Summing over the block and using

$$
\sum_{m=1}^{\ell_b}
\sin^2\left(
\frac{\pi r m}{\ell_b}
\right)
=
\frac{\ell_b}{2},
$$

we obtain

$$
\boxed{
\|\psi_{b,r}\|_2^2
=
\frac1{
2\sin^2(\pi r/\ell_b)
}.
}
$$

In particular the largest local integrated-mode energy is

$$
\asymp
\ell_b^2,
$$

and hence at most $O(L^2)$.

## 5.3 The only nonlocal block modes are the constants

For

$$
r=0,
$$

 $q_{b,0}$ is constant on $I_b$. Its cumulative integral ramps across the block and remains constant after the block, so it is nonlocal.

Define

$$
H_{N,L}^{\mathrm{loc}}
=
\sum_b
\sum_{r=1}^{\ell_b-1}
\psi_{b,r}\psi_{b,r}^*
$$

and

$$
H_{N,L}^{\mathrm{coarse}}
=
\sum_b
\psi_{b,0}\psi_{b,0}^*.
$$

Then

## Theorem 5.1 — Exact local/coarse Brownian synthesis

$$
\boxed{
H_N
=
H_{N,L}^{\mathrm{loc}}
+
H_{N,L}^{\mathrm{coarse}}.
}
$$

Every atom in $H_{N,L}^{\mathrm{loc}}$ is supported on an interval of length at most $L$, while

$$
\boxed{
\operatorname{rank}
H_{N,L}^{\mathrm{coarse}}
\le
\left\lceil\frac NL\right\rceil.
}
$$

Create:

```text
B-RH-037
EXACT_BLOCK_FOURIER_LOCAL_COARSE_BROWNIAN_SYNTHESIS
CERTIFIED
```

The construction is the finite discrete analogue of integrating zero-mean Haar/Fourier increment modes into compact Schauder-type position modes. The Brownian covariance remains exact because the orthonormal increment resolution of the identity is exact.

The conclusion is important for interpreting the previous obstruction. Local synthesis is not impossible. What is unavoidable is a coarse nonlocal channel whose natural dimension is of order $N/L$ when all retained local atoms are restricted to scale $L$.

---

# 6. Logarithmic endpoint time change

The exact block construction solves the position-localization ledger but does not yet place the frequency variable in the multiplicative coordinate natural for Paper 42.

For the exact root quotient define

$$
\boxed{
n_i=2N-i,
\qquad
1\le i\le N.
}
$$

Thus

$$
N\le n_i<2N,
$$

and

$$
z_i
=
\begin{cases}
c_{n_i},&i<N,\\
B(N),&i=N.
\end{cases}
$$

Define the logarithmic endpoint coordinate

$$
\boxed{
x_i
=
\log\frac{2N}{n_i}.
}
$$

Then

$$
0<x_1<\cdots<x_N=\log2,
$$

and, crucially,

$$
\boxed{
x_i-x_j
=
\log\frac{n_j}{n_i}.
}
$$

Thus differences in the new endpoint coordinate are exactly Mellin ratio variables.

Define the logarithmic Brownian matrix

$$
\boxed{
G_N^{\log}(i,j)
=
\min(x_i,x_j).
}
$$

Let

$$
x_0=0
$$

and

$$
\Delta x_r=x_r-x_{r-1}.
$$

Since

$$
\Delta x_r
=
\log\left(
1+
\frac1{2N-r}
\right),
$$

and for $u>0$

$$
\frac1{u+1}
\le
\log\left(1+\frac1u\right)
\le
\frac1u,
$$

we obtain

$$
\boxed{
\frac1{2N}
\le
\Delta x_r
\le
\frac1N.
}
$$

Both Brownian kernels are cumulative Gram matrices:

$$
H_N
=
C_NIC_N^*
$$

and

$$
G_N^{\log}
=
C_N
\operatorname{diag}(\Delta x_1,\ldots,\Delta x_N)
C_N^*.
$$

Therefore the increment comparison gives the Loewner comparison

## Theorem 6.1 — Power-safe logarithmic Brownian time change

$$
\boxed{
N G_N^{\log}
\preceq
H_N
\preceq
2N G_N^{\log}.
}
$$

The distortion is an absolute factor of at most $2$. No power of $N$ is lost.

Create:

```text
B-RH-038
PESC_LOGARITHMIC_BROWNIAN_TIME_CHANGE_WITH_CONSTANT_DISTORTION
CERTIFIED
```

This is the deterministic endpoint-position to Mellin-ratio bridge that Paper 48 required but did not yet possess.

---

# 7. Exact centered Fourier representation of the logarithmic Brownian kernel

For $x,y\ge0$ we have

$$
\min(x,y)
=
\frac{x+y-|x-y|}{2}.
$$

Using the standard identity

$$
\int_{\mathbb R}
\frac{1-\cos(tu)}{t^2}
\,dt
=
\pi|u|,
$$

we obtain the exact centered representation

## Lemma 7.1 — Centered Brownian Fourier identity

$$
\boxed{
\min(x,y)
=
\frac1{2\pi}
\int_{\mathbb R}
\frac{
(e^{itx}-1)(e^{-ity}-1)
}{t^2}
\,dt.
}
$$

The apparent singularity at $t=0$ is removable because each centered factor vanishes linearly there.

Consequently, for every $a\in\mathbb C^N$,

$$
\boxed{
a^*G_N^{\log}a
=
\frac1{2\pi}
\int_{\mathbb R}
\frac{
\left|
\sum_{i=1}^Na_i(e^{itx_i}-1)
\right|^2
}{t^2}
\,dt.
}
$$

This identity is exact and positive. No frequency band has been removed.

---

# 8. The dyadic multiplier costs only a constant

To connect the exact root vector $z$ to Mellin-normalized coefficients, define

$$
\boxed{
a_i=\frac{z_i}{n_i}
}
$$

and

$$
\boxed{
d_i=\frac{n_i}{N}=2-\frac{i}{N}.
}
$$

Then

$$
1\le d_i<2
$$

and

$$
\boxed{
z=N D a,
\qquad
D=\operatorname{diag}(d_1,\ldots,d_N).
}
$$

Pointwise bounds $1\le d_i<2$ alone do not automatically imply comparability in the Brownian norm, because the Brownian norm is a cumulative-sum norm. The slow variation of $d_i$ must be used.

Let

$$
S_k
=
\sum_{i=k}^Na_i
$$

and

$$
T_k
=
\sum_{i=k}^Nd_i a_i.
$$

Then

$$
a^*H_Na
=
\sum_k|S_k|^2
$$

and

$$
(Da)^*H_N(Da)
=
\sum_k|T_k|^2.
$$

Discrete Abel summation gives

$$
\boxed{
T_k
=
d_kS_k
-
\frac1N
\sum_{j=k+1}^NS_j.
}
$$

The strict suffix-sum matrix has operator norm at most $N$, so

$$
\|T\|_2
\le
3\|S\|_2.
$$

For the reverse inequality set

$$
e_i=d_i^{-1}.
$$

Then

$$
\frac12<e_i\le1
$$

and

$$
S_k
=
e_kT_k
+
\sum_{j=k+1}^N
(e_j-e_{j-1})T_j.
$$

The second operator has maximum row sum at most $1/2$ and maximum column sum below $1$, so the Schur test gives operator norm below $1$. Hence

$$
\|S\|_2
\le
2\|T\|_2.
$$

We have proved:

## Theorem 8.1 — Slow dyadic multiplier is Brownian-norm stable

$$
\boxed{
\frac14
a^*H_Na
\le
(Da)^*H_N(Da)
\le
9a^*H_Na.
}
$$

No power of $N$ is lost in passing from $z_i$ to the $1/n_i$ Mellin normalization.

---

# 9. Centered Mellin root-energy bridge

Define

$$
\boxed{
\mathfrak M_N(t)
=
\sum_{i=1}^N
a_i
\left[
\left(\frac{2N}{n_i}\right)^{it}-1
\right].
}
$$

Using the exact root quotient, this is

$$
\boxed{
\begin{aligned}
\mathfrak M_N(t)
={}&
\frac{B(N)}{N}
(2^{it}-1)
\\
&+
\sum_{N<n<2N}
\frac{c_n}{n}
\left[
\left(\frac{2N}{n}\right)^{it}-1
\right].
\end{aligned}
}
$$

The first term is not an optional boundary correction. It is the exact aggregate coordinate through which the PESC quotient observes all increments up to $N$.

Combining Theorems 6.1 and 8.1 with Lemma 7.1 yields the main deterministic bridge.

## Theorem 9.1 — Centered Mellin root-energy comparison

Let

$$
\boxed{
\mathcal E_N^{\mathrm{CM}}
=
\int_{\mathbb R}
\frac{
|\mathfrak M_N(t)|^2
}{t^2}
\,dt.
}
$$

Then

$$
\boxed{
\frac{N^3}{8\pi}
\mathcal E_N^{\mathrm{CM}}
\le
J_N^\vartheta
\le
\frac{9N^3}{\pi}
\mathcal E_N^{\mathrm{CM}}.
}
$$

### Proof

From $z=NDa$,

$$
J_N^\vartheta
=
N^2(Da)^*H_N(Da).
$$

Theorem 8.1 gives

$$
\frac{N^2}{4}a^*H_Na
\le
J_N^\vartheta
\le
9N^2a^*H_Na.
$$

Theorem 6.1 gives

$$
N a^*G_N^{\log}a
\le
 a^*H_Na
\le
2N a^*G_N^{\log}a.
$$

Lemma 7.1 gives

$$
a^*G_N^{\log}a
=
\frac1{2\pi}
\mathcal E_N^{\mathrm{CM}}.
$$

Combining the three inequalities proves the result.

$$
\Box
$$

Create:

```text
B-RH-039
PESC_CENTERED_MELLIN_ROOT_ENERGY_WITH_CONSTANT_DISTORTION
CERTIFIED
```

For every fixed $0<\kappa\le1$, Theorem 9.1 implies the exponent equivalence

$$
\boxed{
J_N^\vartheta
\ll
N^{3-\kappa+o(1)}
}
$$

if and only if

$$
\boxed{
\mathcal E_N^{\mathrm{CM}}
\ll
N^{-\kappa+o(1)}.
}
$$

This is a root-observing Mellin reformulation with no power-sized deterministic loss.

---

# 10. The centered transform as a single prime-error linear statistic

Because

$$
B(N)=\sum_{m\le N}c_m,
$$

we may write the centered Mellin transform without an abstract endpoint variable.

Define

$$
\boxed{
\omega_{N,t}(m)
=
\begin{cases}
\dfrac{2^{it}-1}{N},&m\le N,\\
\dfrac{(2N/m)^{it}-1}{m},&N<m<2N,\\
0,&m\ge2N.
\end{cases}
}
$$

Then

$$
\boxed{
\mathfrak M_N(t)
=
\sum_{m<2N}c_m\omega_{N,t}(m).
}
$$

Since

$$
c_m=1_{\mathbb P}(m)\log m-1,
$$

we also have the exact prime/background split

$$
\boxed{
\mathfrak M_N(t)
=
\sum_{p<2N}
(\log p)\omega_{N,t}(p)
-
\sum_{m<2N}
\omega_{N,t}(m).
}
$$

This identity is not yet an arithmetic estimate. It is the exact interface to Campaign 44 / PK4 `CENTERED_LAMBDA_PRIME_ONLY_BRIDGE`.

The crucial structural point is that the weight is centered at $t=0$ and remains root-observing on both halves of the dyadic interval.

---

# 11. Extreme Mellin frequencies are deterministically harmless

The centered factors give a useful automatic bound.

By the unconditional Chebyshev estimate

$$
\vartheta(x)=O(x),
$$

we have

$$
\frac{|B(N)|}{N}=O(1).
$$

Moreover

$$
\sum_{N<n<2N}
\frac{|c_n|}{n}
=O(1).
$$

Indeed the composite contribution is $O(1)$, while partial summation with $\vartheta(x)=O(x)$ gives

$$
\sum_{N<p<2N}
\frac{\log p}{p}
=O(1).
$$

Therefore

$$
\boxed{
\sum_{i=1}^N|a_i|=O(1).
}
$$

Since

$$
0<x_i\le\log2,
$$

we obtain

$$
|e^{itx_i}-1|
\le
\min(|t|\log2,2).
$$

Thus

## Lemma 11.1 — Centered Mellin envelope

$$
\boxed{
|\mathfrak M_N(t)|
\ll
\min(|t|,1).
}
$$

Let $0<\kappa\le1$ be fixed. Then

$$
\int_{|t|\le N^{-\kappa}}
\frac{|\mathfrak M_N(t)|^2}{t^2}
\,dt
\ll
N^{-\kappa},
$$

and

$$
\int_{|t|\ge N^\kappa}
\frac{|\mathfrak M_N(t)|^2}{t^2}
\,dt
\ll
N^{-\kappa}.
$$

Consequently:

## Theorem 11.2 — Fixed-power PESC reduces to the centered Mellin middle band

For fixed $0<\kappa\le1$,

$$
\boxed{
J_N^\vartheta
\ll
N^{3-\kappa+o(1)}
}
$$

is exponent-equivalent to

$$
\boxed{
\int_{N^{-\kappa}\le|t|\le N^\kappa}
\frac{|\mathfrak M_N(t)|^2}{t^2}
\,dt
\ll
N^{-\kappa+o(1)}.
}
$$

Create:

```text
B-RH-040
PESC_FIXED_POWER_EQUIVALENT_TO_CENTERED_MELLIN_MIDDLE_BAND
CERTIFIED
```

This does not excise the Brownian low mode. The full Brownian energy has already been transferred to $\mathcal E_N^{\mathrm{CM}}$ with constant distortion. The tiny- $t$ estimate is an actual deterministic bound on a part of that exact representation.

---

# 12. Exact Gaussian translated-window identity

The remaining middle band can be partitioned into $O(\log N)$ dyadic frequency scales. Away from zero, the factor $t^{-2}$ is comparable to the inverse square of the local frequency center, so Gaussian translated windows can be inserted with only logarithmic overlap.

To make the connection with Paper 42 exact, let

$$
\Phi(u)
=
\exp\left(\frac{1-u^2}{2}\right),
$$

so that

$$
\widehat\Phi(\xi)
=
 e^{1/2}\sqrt{2\pi}e^{-\xi^2/2}
$$

under the convention

$$
\widehat\Phi(\xi)
=
\int_{\mathbb R}\Phi(u)e^{-iu\xi}\,du.
$$

Define the centered root window moment

$$
\boxed{
\mathcal I_N^{\mathrm{CM}}(Q,Y)
=
\int_{\mathbb R}
\Phi\left(\frac{t-Q}{Y}\right)
|\mathfrak M_N(t)|^2
\,dt.
}
$$

Using

$$
\mathfrak M_N(t)
=
\sum_i a_i(e^{itx_i}-1),
$$

we obtain:

## Theorem 12.1 — Root-observing centered Gaussian window kernel

$$
\boxed{
\mathcal I_N^{\mathrm{CM}}(Q,Y)
=
Y\sum_{i,j}
a_i\overline{a_j}
\mathcal K_{Q,Y}(x_i,x_j),
}
$$

where

$$
\boxed{
\begin{aligned}
\mathcal K_{Q,Y}(x,y)
={}&
 e^{iQ(x-y)}
\widehat\Phi(Y(x-y))
\\
&-
 e^{iQx}
\widehat\Phi(Yx)
\\
&-
 e^{-iQy}
\widehat\Phi(Yy)
\\
&+
\widehat\Phi(0).
\end{aligned}
}
$$

Because

$$
x_i-x_j
=
\log\frac{n_j}{n_i},
$$

the first term is

$$
\boxed{
 e^{-iQ\log(n_i/n_j)}
\widehat\Phi\left(
Y\log(n_i/n_j)
\right),
}
$$

which is exactly the ratio/frequency geometry appearing in Paper 42.

The remaining three terms are the endpoint-centering corrections. They depend on $x_i$ and $x_j$ separately rather than only on the ratio $n_i/n_j$.

Therefore Paper 42's ratio kernel is recovered as a genuine component of the root window, while Paper 48's endpoint-position dependence is retained exactly.

Create:

```text
B-RH-041
PESC_CENTERED_GAUSSIAN_TRANSLATED_WINDOW_KERNEL_WITH_ENDPOINT_CORRECTION
CERTIFIED
```

This is the precise deterministic reconciliation of Paper 42 and Paper 48 required by PK3.

---

# 13. Dyadic translated-window synthesis of the middle band

Let

$$
T_-=N^{-\kappa}
$$

and

$$
T_+=N^\kappa.
$$

Choose a smooth dyadic partition of unity on

$$
T_-\le|t|\le T_+.
$$

There are only

$$
O(\log N)
=
N^{o(1)}
$$

frequency scales.

On a window centered at

$$
|Q|\asymp Y
$$

or, more generally, with

$$
Y\le c|Q|
$$

for fixed $c<1$, one has

$$
t^{-2}\asymp Q^{-2}
$$

throughout the window. Hence the middle-band energy is controlled, up to $N^{o(1)}$ overlap, by translated moments of the form

$$
Q^{-2}
\mathcal I_N^{\mathrm{CM}}(Q,Y).
$$

The arithmetic burden is therefore no longer an unspecified frame problem. It is the explicit family of centered root moments

$$
\boxed{
\mathcal I_N^{\mathrm{CM}}(Q,Y)
}
$$

with kernel $\mathcal K_{Q,Y}$ from Theorem 12.1.

Any fixed-power estimate must preserve the endpoint terms or prove that their contribution is separately admissible. Dropping them and keeping only the ratio term returns to the non-root-observing interface rejected by Paper 48.

---

# 14. PK3 audit

We now audit the exact requirements inherited from the Campaign 44 taskpack.

## Required check 1 — state the synthesis/frame operator explicitly

Passed.

The exact position synthesis is

$$
H_N=C_NIC_N^*,
$$

with exact block-Fourier resolution

$$
H_N
=
\sum_{b,r}\psi_{b,r}\psi_{b,r}^*.
$$

The Mellin-compatible synthesis is the exact centered Fourier representation of $G_N^{\log}$ combined with the constant-distortion comparison to $H_N$.

## Required check 2 — retain endpoint-position and ratio/frequency localization

Passed.

Endpoint position is retained through

$$
x_i=\log(2N/n_i),
$$

and the translated kernel contains both

$$
\log(n_i/n_j)
$$

and the separate endpoint terms $x_i,x_j$.

## Required check 3 — preserve the Brownian low-frequency root mode

Passed.

No Brownian eigenmode is projected out. The full operator satisfies

$$
N G_N^{\log}
\preceq
H_N
\preceq
2N G_N^{\log}.
$$

Thus the complete root energy, including the principal Brownian mode, survives with constant distortion.

## Required check 4 — compute or bound frame/reconstruction conditioning

Passed.

Theorem 3.1 records the general $N^2$ spectral-spread conservation law. The logarithmic time change costs at most a factor $2$, and the dyadic Mellin normalization costs only absolute constants in the Brownian norm.

## Required check 5 — charge every $N^\delta$ reconstruction loss

Passed.

The root-to-centered-Mellin bridge has no $N^\delta$ loss. The positive submacroscopic-window route is separately recorded as paying

$$
(N/L)^2
$$

unless a coarse channel is retained.

## Required check 6 — distinguish exact reconstruction from one-sided domination

Passed.

The following are exact:

$$
H_N=C_NC_N^*,
$$

$$
H_N=H_{N,L}^{\mathrm{loc}}+H_{N,L}^{\mathrm{coarse}},
$$

and

$$
a^*G_N^{\log}a
=
\frac1{2\pi}
\int_{\mathbb R}
\frac{|\mathfrak M_N(t)|^2}{t^2}\,dt.
$$

The comparison between $H_N$ and $NG_N^{\log}$ is explicitly one-sided in both directions with constants $1$ and $2$.

## Required check 7 — do not declare the Paper 42 ratio kernel equal to PESC

Passed.

Theorem 12.1 shows the ratio kernel plus the three exact endpoint-centering terms.

## Required check 8 — do not remove low frequencies without priced recovery

Passed.

No low-frequency recovery operator is invoked. The exact centered transform is used first, and only the tiny interval

$$
|t|\le N^{-\kappa}
$$

is then bounded directly by the certified envelope

$$
|\mathfrak M_N(t)|\ll|t|.
$$

---

# 15. PK3 closure

The deterministic question posed by PK3 was whether the exact position-dependent PESC Brownian root kernel could be synthesized in translated frequency variables without erasing the principal low mode or paying an unrecorded power-sized reconstruction cost.

The answer is yes.

The route is

$$
\boxed{
H_N
\longleftrightarrow
N G_N^{\log}
\longleftrightarrow
\frac{N}{2\pi}
\int_{\mathbb R}
\frac{
(e^{itx}-1)(e^{-ity}-1)
}{t^2}
\,dt,
}
$$

combined with the Brownian-norm-stable dyadic normalization

$$
z_i=n_i a_i.
$$

The full PESC root energy is therefore constant-distortion equivalent to a centered Mellin energy.

Close PK3 as

```text
CLOSED_AS_POWER_SAFE_LOG_BROWNIAN_TO_CENTERED_MELLIN_ROOT_SYNTHESIS
```

This closure is structural only. It does not establish the fixed-power estimate required by PESC.

---

# 16. Campaign 44 continuation

The next inherited track is

```text
PK4
CENTERED_LAMBDA_PRIME_ONLY_BRIDGE
```

The exact PK4 input is now

$$
\boxed{
\mathfrak M_N(t)
=
\sum_{m<2N}
\left(1_{\mathbb P}(m)\log m-1\right)
\omega_{N,t}(m).
}
$$

The arithmetic problem is to exploit the prime structure of this centered root statistic, or the exact translated-window kernel $\mathcal K_{Q,Y}$, strongly enough to obtain

$$
\int_{N^{-\kappa}\le|t|\le N^\kappa}
\frac{|\mathfrak M_N(t)|^2}{t^2}
\,dt
\ll
N^{-\kappa+o(1)}
$$

for some fixed $\kappa>0$.

At this point the deterministic frame problem is no longer the blocker. The blocker is a root-observing arithmetic contraction for the centered prime-error transform.

The following routes remain prohibited unless genuinely new evidence appears:

1. reopening Paper 46 coefficient-smallness or mark-multiplicity mechanisms;
2. returning to the isolated pure-Mobius component after Paper 47's exact root recoupling;
3. discarding the endpoint-centering terms in Theorem 12.1;
4. replacing a logarithmic saving by a fixed power;
5. assuming a fixed zero-free strip or fixed-power PNT remainder;
6. removing a low-frequency/root block and claiming later recovery without charging the recovery map.

---

# 17. New certified objects

Create:

```text
B-RH-036
PESC_FRAME_WEIGHT_SPECTRAL_SPREAD_CONSERVATION
CERTIFIED
```

Create:

```text
B-RH-037
EXACT_BLOCK_FOURIER_LOCAL_COARSE_BROWNIAN_SYNTHESIS
CERTIFIED
```

Create:

```text
B-RH-038
PESC_LOGARITHMIC_BROWNIAN_TIME_CHANGE_WITH_CONSTANT_DISTORTION
CERTIFIED
```

Create:

```text
B-RH-039
PESC_CENTERED_MELLIN_ROOT_ENERGY_WITH_CONSTANT_DISTORTION
CERTIFIED
```

Create:

```text
B-RH-040
PESC_FIXED_POWER_EQUIVALENT_TO_CENTERED_MELLIN_MIDDLE_BAND
CERTIFIED
```

Create:

```text
B-RH-041
PESC_CENTERED_GAUSSIAN_TRANSLATED_WINDOW_KERNEL_WITH_ENDPOINT_CORRECTION
CERTIFIED
```

Create:

```text
O-RH-128
PESC_SUBMACROSCOPIC_POSITIVE_SYNTHESIS_PAYS_POWER_RECONSTRUCTION_TAX
CERTIFIED AS PK3 CONDITIONING BARRIER
```

No new RH certificate is created.

---

# 18. External calibration

The mathematical identities used for the deterministic synthesis are self-contained in this paper. The following literature is calibration rather than a substituted proof.

1. The Brownian covariance kernel $\min(s,t)$ and its basis expansions are classical. The Levy--Ciesielski construction represents Brownian motion in the integrated Haar/Schauder basis; see T. Kleyntssens and S. Nicolay, *From the Brownian motion to a multifractal process using the Levy--Ciesielski construction*, Statistics & Probability Letters 186 (2022), 109450.

2. The connection between frequency mean squares of exponential/Dirichlet sums and short-sum or Selberg-type energies is classical Gallagher territory. For a modern weighted formulation, see G. Coppola and M. Laporta, *A generalization of Gallagher's lemma for exponential sums*, arXiv:1411.1739.

3. Paper 42 already certified the Gaussian translated ratio kernel internally. Theorem 12.1 does not reuse that result as a root theorem; it derives the centered root window independently and then identifies the Paper 42 ratio geometry as its first term.

---

# 19. State transition

Candidate project state:

```text
CSM_RH v1.40
```

Campaign 44:

```text
ACTIVE
```

Track states:

```text
PK1 CLOSED_AS_EXACT_LAG_POSITION_NORMALIZATION_WITH_PREFIX_GRAM_COMPLETION
PK2 CLOSED_AS_EXACT_BROWNIAN_SPECTRAL_REPRESENTATION_WITH_LOW_MODE_PRESERVED
PK3 CLOSED_AS_POWER_SAFE_LOG_BROWNIAN_TO_CENTERED_MELLIN_ROOT_SYNTHESIS
PK4 OPEN_CENTERED_LAMBDA_PRIME_ONLY_BRIDGE
PK5 OPEN_FIXED_POWER_PESC_ADMISSION
```

Root frontiers remain

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

# 20. Final status

Paper 49 resolves the deterministic synthesis ambiguity left by Paper 48.

The exact Brownian root kernel has a genuine $N^2$ spectral spread, and positive submacroscopic synthesis cannot make that stiffness disappear. Nevertheless an exact local/coarse construction exists, and a separate logarithmic time change provides a power-safe route into Mellin frequency.

The central identity is the constant-distortion root bridge

$$
\boxed{
J_N^\vartheta
\asymp
N^3
\int_{\mathbb R}
\frac{|\mathfrak M_N(t)|^2}{t^2}\,dt,
}
$$

with

$$
\boxed{
\mathfrak M_N(t)
=
\frac{B(N)}{N}(2^{it}-1)
+
\sum_{N<n<2N}
\frac{c_n}{n}
\left[
\left(\frac{2N}{n}\right)^{it}-1
\right].
}
$$

The centering is essential. It regularizes $t=0$, preserves the endpoint aggregate, and produces the exact correction terms missing from a ratio-only translated kernel.

The very low and very high Mellin frequencies are deterministically admissible at the fixed-power scale, leaving the polynomial middle band as the next root arithmetic battlefield.

The resulting continuation is therefore no longer

```text
find a frame for PESC
```

but

```text
prove a fixed-power arithmetic contraction for the centered prime-error Mellin middle band
```

inside Campaign 44 / PK4.
