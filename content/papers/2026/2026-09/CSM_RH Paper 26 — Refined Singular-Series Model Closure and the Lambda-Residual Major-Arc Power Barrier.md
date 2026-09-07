# CSM_RH Paper 26
## Refined Singular-Series Model Closure and the Lambda-Residual Major-Arc Power Barrier

**Project:** `CSM_RH`  
**Paper:** `26`  
**Version:** `v0.1`  
**Date:** `2026-09-06`  
**Parent state:** `CSM_RH v1.16 / Paper 25`  
**Campaign:** `25 — FULLY_DISTINCT_FOUR_POINT_ATTACK`  
**Status:** model/residual localization and current-method strength audit; not a proof or disproof of RH

# 0. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
CSM_RH_ROOT_STATUS = OPEN
```

Paper 25 reduced the centered fourth-moment candidate to the fully distinct four-point aggregate.

Campaign 25 asks where the missing fixed $H$ -power actually sits.

# 1. Fully distinct aggregate

Let

$$
a_n=\Lambda(n)-1.
$$

Define

$$
\boxed{
\mathcal A_{4,\mathrm{dist}}(X,H)
=
\sum_{\substack{
1\le d_1,d_2,d_3,d_4\le H\\
d_i\text{ distinct}
}}
\sum_x
\prod_{i=1}^{4}a_{x+d_i}.
}
$$

D4HEG asks for

$$
\mathcal A_{4,\mathrm{dist}}(X,H)
\ll
XH^{4-\eta}(\log X)^{O(1)}
$$

for some fixed $0<\eta\le1$.

# 2. Refined singular series

Define the centered singular series

$$
\boxed{
\mathfrak S_0(\mathcal D)
=
\sum_{\mathcal Q\subseteq\{1,\ldots,k\}}
(-1)^{k-|\mathcal Q|}
\mathfrak S(\mathcal D_{\mathcal Q}).
}
$$

and

$$
\boxed{
R_k(H)
=
\sum_{\substack{
1\le d_1,\ldots,d_k\le H\\
d_i\text{ distinct}
}}
\mathfrak S_0(d_1,\ldots,d_k).
}
$$

For even $k$, Montgomery–Soundararajan give Gaussian-pairing scale.

For $k=4$,

$$
\boxed{
R_4(H)
=
3(-H\log H+AH)^2
+
O_\varepsilon(H^{2-1/28+\varepsilon}),
}
$$

hence

$$
\boxed{
R_4(H)\ll H^2(\log H)^2.
}
$$

Therefore the centered Hardy–Littlewood model is not the $H^4$ barrier.

Create:

```text
O-RH-055
REFINED_SINGULAR_SERIES_MODEL_NOT_THE_H4_BARRIER
status: CERTIFIED
```

# 3. Actual correlation error

Define

$$
C_{\Lambda,4}(\mathcal D;X)
=
\sum_x
\prod_{i=1}^{4}[\Lambda(x+d_i)-1].
$$

Define

$$
E_4(\mathcal D;X)
=
C_{\Lambda,4}(\mathcal D;X)
-
X\mathfrak S_0(\mathcal D).
$$

Then

$$
\boxed{
\mathcal A_{4,\mathrm{dist}}(X,H)
=
XR_4(H)
+
\mathcal E_{4,\mathrm{dist}}(X,H),
}
$$

where

$$
\mathcal E_{4,\mathrm{dist}}(X,H)
=
\sum_{\mathcal D\text{ distinct}}E_4(\mathcal D;X).
$$

Thus for $0<\eta\le1$, a bound

$$
\boxed{
\mathcal E_{4,\mathrm{dist}}(X,H)
\ll
XH^{4-\eta}(\log X)^{O(1)}
}
$$

implies D4HEG.

# 4. Lambda-sharp split

Use the 2026 approximant

$$
\Lambda^\sharp(n)
=
\frac{P(R)}{\varphi(P(R))}
1_{(n,P(R))=1},
$$

with

$$
R=\exp((\log X)^{1/10}).
$$

Set

$$
f=\Lambda-\Lambda^\sharp,
\qquad
b=\Lambda^\sharp-1.
$$

Then

$$
\Lambda-1=f+b.
$$

Substitution into the fully distinct four-point aggregate yields exactly sixteen sectors:

$$
\boxed{
\mathcal A_{4,\mathrm{dist}}
=
\sum_{S\subseteq\{1,2,3,4\}}
\mathcal T_S.
}
$$

The empty $S$ sector is pure model. Every other sector contains at least one true prime residual.

# 5. Current residual strength

For $H\ge X^{1/3+\varepsilon}$, current higher-uniformity theory gives

$$
\boxed{
\Lambda-\Lambda^\sharp:
\quad
H\log^{-A}X
}
$$

against nilsequences outside an exceptional set of measure $O(X\log^{-A}X)$.

The associated Gowers-uniformity strength is subpower.

By contrast, in the same theorem,

$$
\boxed{
d_k-d_k^\sharp:
\quad
HX^{-c_{k,\dots}}
}
$$

outside a power-saving exceptional set.

# 6. Generalized von Neumann exponent audit

Suppose a transference estimate controls a residual-containing normalized linear-forms average by

$$
\Phi(\rho_X),
$$

where $\rho_X$ is the relevant local residual uniformity and $\Phi(t)\ll t^c$ for some fixed $c>0$.

If

$$
\rho_X=\log^{-A}X,
$$

then

$$
\Phi(\rho_X)=X^{-o(1)}.
$$

If instead

$$
\rho_X\le X^{-c_0},
$$

then

$$
\Phi(\rho_X)\le X^{-cc_0}
=
H^{-cc_0/\alpha}
$$

at $H=X^\alpha$.

Therefore a power residual would generate a fixed $H$ -exponent. Current Lambda residual uniformity cannot do so through fixed algebraic transference.

# 7. Proof-level W split

In the 2026 proof, the major-arc parameter is chosen as

$$
\delta=\log^{-A}X
$$

for $\Lambda$ and $\mu$, but

$$
\delta=X^{-c_{k,C}\varepsilon}
$$

for $d_k$.

The Type-II input uses

$$
\boxed{
W_\Lambda=\log^{A}X,
}
$$

whereas

$$
\boxed{
W_{d_k}=X^{c_k}.
}
$$

The Type-II output saves a fixed negative power of $W$.

Hence

```text
W polylogarithmic
  -> log/subpower output

W polynomial
  -> fixed-power output
```

The prime/divisor exponent-class split is already built into the proof.

# 8. Why Lambda has only polylogarithmic W

The Dirichlet-polynomial bound for $\Lambda$ and $\mu$ is obtained from the Vinogradov–Korobov zero-free region.

The divisor bound is instead obtained from the divisor convolution representation.

Thus the current prime residual inherits a zero-sensitive major-arc limitation that the divisor residual does not.

Create:

```text
O-RH-056
LAMBDA_RESIDUAL_MAJOR_ARC_W_PARAMETER_BARRIER
status: CERTIFIED AS CURRENT-METHOD AUDIT
```

# 9. d2 as comparator

The same 2026 paper proves a fixed-Fourier estimate for $d_2-d_2^\sharp$ of size

$$
HX^{-\varepsilon/1000}
$$

outside a power-saving exceptional set.

That proof uses a different classical route, with a fourth moment of Dirichlet $L$ -functions at the decisive stage.

This demonstrates that short-interval power discorrelation is technically possible for divisor objects.

It does not provide a prime analogue.

# 10. Campaign 25 verdict

```text
pure centered singular-series model
  harmless

collision shell
  harmless

Lambda-sharp / residual decomposition
  exact

generalized von Neumann route
  current Lambda input subpower

divisor-to-prime transfer
  fails quantitatively at major-arc / Type-II W

D4HEG
  open / auxiliary nonlinear route
```

Create:

```text
S-RH-030
FULLY_DISTINCT_RESIDUAL_AGGREGATE_POWER_CANCELLATION
status: OPEN
```

Prototype:

$$
\boxed{
\mathcal E_{4,\mathrm{dist}}(X,H)
\ll
XH^{4-\eta}(\log X)^{O(1)}.
}
$$

# 11. Campaign 26

```text
CSM_RH Campaign 26
THREE_SHIFT_RESIDUAL_AGGREGATION_ATTACK
```

The question is:

> can averaging the residual over three independent shifts create a fixed $H$ -power that is absent from the current one-interval residual theorem?

Tracks:

```text
R4-1 aggregate-first transference
R4-2 Type-II W gain after shift averaging
R4-3 model-weighted residual orthogonality
R4-4 connected residual cumulant
R4-5 d2 proof surgery
```

Reject any candidate that assumes power uniformity of $\Lambda-\Lambda^\sharp$, imports a fixed zero strip, obtains only subpower saving, reopens the already solved model main term, or transfers the $d_2$ theorem without re-proving the prime Dirichlet-series step.

# 12. State transition

```text
CSM_RH v1.16
  ->
CSM_RH v1.17
```

with:

```text
Campaign 25
  CLOSED_AS_MODEL_RESIDUAL_AND_W_PARAMETER_AUDIT

O-RH-055
  CREATED / CERTIFIED

O-RH-056
  CREATED / CERTIFIED AS CURRENT-METHOD AUDIT

F-RH-019
  D4HEG
  REMAINS OPEN / AUXILIARY

S-RH-030
  CREATED / OPEN

Campaign 26
  READY
```

# 13. Final status

```text
RH = OPEN
PESC = OPEN
MLEPG = OPEN
C4HEG = OPEN / AUXILIARY
D4HEG = OPEN / AUXILIARY

CENTERED FOUR-POINT MODEL = HARMLESS
FULLY DISTINCT PRIME RESIDUAL = OPEN
CURRENT LAMBDA RESIDUAL UNIFORMITY = SUBPOWER
CURRENT DIVISOR RESIDUAL UNIFORMITY = FIXED POWER
PRIME/DIVISOR LOSS POINT = MAJOR-ARC TYPE-II W PARAMETER

NEXT CAMPAIGN = 26
```
