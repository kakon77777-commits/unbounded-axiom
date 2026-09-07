# CSM_RH Paper 27
## Three-Shift Aggregation Collapse and the Residual Local-Moment Barrier

**Project:** `CSM_RH`  
**Paper:** `27`  
**Version:** `v0.1`  
**Date:** `2026-09-07`  
**Parent state:** `CSM_RH v1.17 / Paper 26`  
**Campaign:** `26 — THREE_SHIFT_RESIDUAL_AGGREGATION_ATTACK`  
**Status:** aggregation-collapse theorem / no-free-dimension audit; not a proof or disproof of RH

---

# 0. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
CSM_RH_ROOT_STATUS = OPEN
```

Paper 26 localized the current four-point quantitative loss to the residual

$$
f=\Lambda-\Lambda^\sharp.
$$

Campaign 26 asks whether averaging over the three independent shift variables of the fully distinct four-point family can create a fixed $H$ -power which is absent from the one-interval residual theorem.

The answer is negative at the purely aggregation/transference level:

> after the full shift sum is assembled, the three-dimensional family collapses, modulo the already harmless collision shell, to one-dimensional local mixed moments of the residual and model block sums.

No live GLM-5.3-Flash run is claimed.

---

# 1. Residual / model decomposition

Let

$$
f(n)=\Lambda(n)-\Lambda^\sharp(n),
$$

and

$$
b(n)=\Lambda^\sharp(n)-1.
$$

Then

$$
\Lambda(n)-1=f(n)+b(n).
$$

For interval length $H$, define

$$
\boxed{F_H(x)=\sum_{r=1}^{H}f(x+r)}
$$

and

$$
\boxed{B_H(x)=\sum_{r=1}^{H}b(x+r)}.
$$

---

# 2. Mixed fully distinct sectors

For $0\le m\le4$, define

$$
\boxed{
\mathcal T_m^{\mathrm{dist}}(X,H)
=
\sum_{\substack{S\subseteq\{1,2,3,4\}\\|S|=m}}
\sum_x
\sum_{\substack{1\le d_1,d_2,d_3,d_4\le H\\d_i\text{ distinct}}}
\prod_{i\in S}f(x+d_i)
\prod_{i\notin S}b(x+d_i).
}
$$

The full distinct aggregate is

$$
\mathcal A_{4,\mathrm{dist}}
=
\sum_{m=0}^{4}\mathcal T_m^{\mathrm{dist}}.
$$

---

# 3. Unrestricted shift factorization

Remove the distinctness condition. For fixed $S$ with $|S|=m$,

$$
\sum_{d_1,\ldots,d_4\le H}
\prod_{i\in S}f(x+d_i)
\prod_{i\notin S}b(x+d_i)
=
F_H(x)^mB_H(x)^{4-m}.
$$

Summing over the $\binom4m$ subsets gives

$$
\boxed{
\mathcal T_m^{\mathrm{all}}
=
\binom4m\sum_xF_H(x)^mB_H(x)^{4-m}.
}
$$

Thus the apparent three independent relative-shift directions disappear completely after the aggregate is formed.

---

# 4. Distinctness correction

The difference between unrestricted and fully distinct tuples is supported on offset collisions. There are $O(H^3)$ such ordered quadruples. Since $f$ and $b$ are pointwise polylogarithmically bounded on the relevant block,

$$
\boxed{
\mathcal T_m^{\mathrm{dist}}
=
\binom4m\sum_xF_H(x)^mB_H(x)^{4-m}
+
O\!\left(XH^3(\log X)^{O(1)}\right).
}
$$

Create:

```text
B-RH-003
THREE_SHIFT_TO_LOCAL_MOMENT_COLLAPSE
status:
  CERTIFIED
```

---

# 5. Full aggregate collapse

Summing over $m$,

$$
\boxed{
\mathcal A_{4,\mathrm{dist}}(X,H)
=
\sum_x[F_H(x)+B_H(x)]^4
+
O\!\left(XH^3(\log X)^{O(1)}\right).
}
$$

Since

$$
F_H(x)+B_H(x)
=
\sum_{r=1}^{H}[\Lambda(x+r)-1],
$$

the fully distinct aggregate is, modulo the collision shell, the original centered local fourth moment.

---

# 6. No free three-dimensional averaging gain

After complete aggregation the three shift variables are not independent oscillatory resources. They create powers of local block sums. The remaining analytic variable is $x$.

Create:

```text
O-RH-057
THREE_SHIFT_AGGREGATION_NO_FREE_DIMENSION_GAIN
status:
  CERTIFIED
```

A fixed power must therefore arise from a theorem controlling the $x$ -distribution of the local residual/model block sums.

---

# 7. Current residual block-sum theorem

For $H\ge X^{1/3+\varepsilon}$, current 2026 higher-uniformity theory implies, using the constant nilsequence test, that for every fixed $A>0$,

$$
\boxed{|F_H(x)|\ll H\log^{-A}X}
$$

outside an exceptional set of measure

$$
\boxed{O_A(X\log^{-A}X)}.
$$

On every interval one has the trivial polylogarithmic bound

$$
|F_H(x)|\ll H(\log X)^{O(1)}.
$$

---

# 8. Current residual moments

For any fixed $1\le p\le4$, split into good and exceptional intervals. Choosing the theorem parameter $A$ sufficiently large relative to any prescribed $B>0$ gives

$$
\boxed{
\sum_{x\asymp X}|F_H(x)|^p
\ll_B
XH^p\log^{-B}X.
}
$$

In particular,

$$
\boxed{
\sum_{x\asymp X}|F_H(x)|^4
\ll_B
XH^4\log^{-B}X.
}
$$

This is strong subpower control, but at polynomial $H$ it is still $H^{4-o(1)}$ rather than $H^{4-\eta}$.

---

# 9. Mixed sectors with current technology

Using the crude pointwise model bound

$$
|B_H(x)|\ll H(\log X)^{O(1)},
$$

one obtains for every residual-containing mixed sector

$$
\boxed{
\mathcal T_m^{\mathrm{dist}}
\ll_B
XH^4\log^{-B}X
+
O\!\left(XH^3(\log X)^{O(1)}\right),
\qquad 1\le m\le4.
}
$$

Thus current one-interval residual technology remains in exponent class $H^{4-o(1)}$.

---

# 10. Pure residual sector

For $m=4$,

$$
\boxed{
\mathcal T_4^{\mathrm{all}}
=
\sum_xF_H(x)^4
\ge0.
}
$$

So the pure residual sector has no internal signed $x$ -cancellation. Any sectorwise proof must improve the residual fourth moment itself.

---

# 11. Cross-sector cancellation is the original problem

If one instead allows cancellation among

$$
F^4,
\quad 4F^3B,
\quad 6F^2B^2,
\quad 4FB^3,
\quad B^4,
$$

the exact sum is

$$
\boxed{(F+B)^4.}
$$

Therefore cross-sector cancellation is simply the original centered fourth-moment problem. The sixteen-sector decomposition does not itself create an exponent.

---

# 12. Type-II $W$ parameter after shift aggregation

Paper 26 identified the current prime residual scale

$$
W_\Lambda=\log^A X.
$$

The collapse theorem shows that a complete three-shift sum does not algebraically introduce a new multiplicative parameter. After aggregation, the residual reappears through $F_H(x)$.

Therefore a polynomial effective $W$ cannot be obtained merely by reordering the additive shift sums.

Create:

```text
O-RH-058
SHIFT_AVERAGING_DOES_NOT_AMPLIFY_W_LAMBDA
status:
  CERTIFIED AS STRUCTURAL AUDIT
```

---

# 13. $d_2$ proof surgery verdict

The 2026 fixed-Fourier theorem for $d_2-d_2^\sharp$ obtains a power saving using a different classical argument and a fourth moment of Dirichlet $L$ -functions. The present aggregation collapse does not create an analogous prime Dirichlet-series structure.

Replacing the divisor residual by $\Lambda-\Lambda^\sharp$ returns to the zero-sensitive prime Dirichlet-polynomial problem identified in Paper 26.

No prime fixed-power transfer is obtained.

---

# 14. Campaign 26 verdict

```text
R4-1 aggregate-first transference
  COLLAPSES TO LOCAL MIXED MOMENTS

R4-2 Type-II W gain after shift averaging
  NO ALGEBRAIC W AMPLIFICATION

R4-3 model-weighted residual orthogonality
  REDUCED TO ONE-DIMENSIONAL x-CORRELATIONS

R4-4 connected residual cumulant
  REORGANIZATION ONLY

R4-5 d2 proof surgery
  NO PRIME POWER TRANSFER FOUND
```

Create:

```text
O-RH-059
LAMBDA_RESIDUAL_LOCAL_FOURTH_MOMENT_BARRIER
status:
  CERTIFIED AS CURRENT-TECHNOLOGY AUDIT
```

---

# 15. Status of the four-point branch

```text
F-RH-018 C4HEG
  OPEN / AUXILIARY

F-RH-019 D4HEG
  OPEN / AUXILIARY

S-RH-030
  CLOSED AS A FREE-AGGREGATION MECHANISM
```

The four-point route remains mathematically valid, but it is not currently shorter than PESC/MLEPG.

---

# 16. Campaign 27

```text
CSM_RH Campaign 27
DIRECT_PESC_ATTACK_II
```

Allowed tracks:

```text
P2-1 signed prime sampling with structured drift subtraction
P2-2 PESC after sieve-model subtraction
P2-3 bilinear residual/model cross term
P2-4 scale-coupled signed recurrence
P2-5 direct arithmetic drift exclusion
```

Reject any candidate that introduces another positive moment frontier, merely rephrases MLEPG, uses zero density/fixed strip as the power source, achieves only logarithmic precision, or creates another high-dimensional shift aggregate that collapses to a local moment.

---

# 17. State transition

```text
CSM_RH v1.17
  ->
CSM_RH v1.18
```

with:

```text
Campaign 26
  CLOSED_AS_THREE_SHIFT_AGGREGATION_COLLAPSE_AUDIT

B-RH-003
  THREE_SHIFT_TO_LOCAL_MOMENT_COLLAPSE
  CREATED / CERTIFIED

O-RH-057
  THREE_SHIFT_AGGREGATION_NO_FREE_DIMENSION_GAIN
  CREATED / CERTIFIED

O-RH-058
  SHIFT_AVERAGING_DOES_NOT_AMPLIFY_W_LAMBDA
  CREATED / CERTIFIED AS STRUCTURAL AUDIT

O-RH-059
  LAMBDA_RESIDUAL_LOCAL_FOURTH_MOMENT_BARRIER
  CREATED / CERTIFIED AS CURRENT-TECHNOLOGY AUDIT

S-RH-030
  CLOSED AS FREE-AGGREGATION MECHANISM

Campaign 27
  DIRECT_PESC_ATTACK_II
  READY
```

---

# 18. Final status

```text
RH = OPEN
PESC = OPEN / ROOT TARGET
MLEPG = OPEN / DIRECT THEOREM CANDIDATE
C4HEG = OPEN / AUXILIARY
D4HEG = OPEN / AUXILIARY
THREE-SHIFT FREE AGGREGATION GAIN = CLOSED
CURRENT RESIDUAL FOURTH MOMENT = H^4 X^{-o(1)}
POLYNOMIAL H-EXPONENT GAIN = OPEN
FOUR-POINT ROUTE = NOT CURRENTLY SHORTER THAN PESC/MLEPG
NEXT CAMPAIGN = 27
```
