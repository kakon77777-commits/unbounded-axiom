# CSM_RH Paper 63

## Proof-Slack Removal in the MRSTT Type-II Lemma and the Critical Long-Scale Anchor Barrier

**Project:** CSM_RH  
**Paper:** 63  
**Version:** v0.1  
**Date:** 2026-09-08  
**Campaign:** 46 — `SEEDED_ARITHMETIC_STRIP_GAP_GENERATION`  
**Tracks:** PT5 / F-RH-017-v3  
**Status:** MRSTT PROOF SLACK REMOVED / STRONGER SCALE-COMPARISON NON-AMPLIFICATION BARRIER CERTIFIED  
**Canonical entry state:** v1.53 / Paper 62 v0.1  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 62 inserted a PESC seed into the 2026 Matomäki–Radziwiłł–Shao–Tao–Teräväinen Type-II machinery and obtained the first fixed-power almost-all short-interval prime estimate in the CSM_RH chain. It also treated the conditions

$$
H_2\le\frac{X}{W^4}
$$

and the output

$$
W^{-1/10}
$$

as the relevant geometric ceiling of MRSTT Lemma 3.5.

The present paper audits the proof itself and corrects that interpretation.

The published proof has genuine quantitative slack.

First, the Parseval variance lemma used inside the proof only requires

$$
H_2\le\frac{X}{W^3}.
$$

The extra factor $W$ in the statement of MRSTT Lemma 3.5 is not used later in its proof.

Second, the mean-square exponent $3/10$ is not the intrinsic exponent of the Baker–Harman–Pintz step. The parallelogram lemma supplies a $W^{-1/3}$ bound up to polylogarithmic factors. Consequently every fixed

$$
0<a<\frac13
$$

may replace $3/10$ in the mean-square conclusion.

Third, redoing the low-frequency Taylor estimate at the target exponent $a$ improves the scale condition further. If

$$
q>2+\frac a2,
$$

then

$$
H_2\le\frac{X}{W^q}
$$

is already sufficient, because the low-frequency contribution is

$$
O\left(
W^4\frac{H_2^2}{X^2}
\log^{O(1)}X
\right)
\ll
W^{-a}\log^{O(1)}X.
$$

Thus the proof yields the sharpened Type-II mean-square statement

$$
\boxed{
\frac1X
\int_X^{2X}
|\Delta_{H_1,H_2}^{II}(x)|^2dx
\ll
H_1^2
W^{-a}
\log^{O(1)}X
}
$$

under the same Dirichlet-polynomial hypotheses, for every fixed $a<1/3$ and every fixed $q>2+a/2$.

Chebyshev should also be used asymmetrically. For any

$$
b>0,
\qquad
c_0>0,
\qquad
2b+c_0<a,
$$

one obtains

$$
|\Delta_{H_1,H_2}^{II}(x)|
\le
H_1W^{-b}
$$

outside a set of measure

$$
O\left(
XW^{-c_0}\log^{O(1)}X
\right).
$$

If

$$
H_1=X^{1-\tau},
\qquad
W=X^w,
$$

and $H_2\ge H_1$, the scale constraint gives

$$
qw\le\tau.
$$

Hence the complete Type-II variance budget is

$$
\boxed{
2\nu_{\rm diff}
+
c_{\rm diff}
<
\frac{a}{q}\tau.
}
$$

Optimizing over the proof-slack parameters

$$
a<\frac13,
\qquad
q>2+\frac a2
$$

gives the limiting budget

$$
\boxed{
2\nu_{\rm diff}
+
c_{\rm diff}
<
\frac{2}{13}\tau.
}
$$

This improves Paper 62's crude $\tau/40$ symmetric output, but it remains far below the supercritical F-RH-017-v3 requirements.

More importantly, the paper proves a stronger obstruction which makes all such proof-slack improvements secondary.

Any scale-comparison architecture has the form

$$
S_H(x)
=
\frac{H}{H_2}S_{H_2}(x)
+
\Delta_{H,H_2}(x),
$$

where

$$
S_H(x)
=
\psi(x+H)-\psi(x).
$$

Assume only the seed PESC $(\kappa)$ with

$$
d=\frac{\kappa}{2}.
$$

The long-scale prime error satisfies

$$
|S_{H_2}(x)-H_2|
\ll
\min
\left\{
X^{1-d+o(1)},
H_2X^{o(1)}
\right\}.
$$

Write

$$
H_2=X^{1-\tau_2}.
$$

After scaling by $H/H_2$, the long anchor has relative saving exponent at most

$$
\boxed{
(d-\tau_2)_+
\le d.
}
$$

Therefore, even if the scale-difference term $\Delta_{H,H_2}$ were identically zero, seed information alone could never prove a short-interval threshold with

$$
\boxed{
\nu>d.
}
$$

This is the critical long-scale anchor barrier.

A hypothetical boundary zero makes the obstruction sharp. Its smooth explicit-formula mode satisfies, for every sublinear $H_2$,

$$
S_{H_2,\rho}(x)-H_2
\asymp_\rho
H_2X^{-d}
$$

at its natural oscillatory scale. After multiplication by $H/H_2$, it remains

$$
\boxed{
H X^{-d}.
}
$$

Thus perfect scale coherence does not suppress the boundary mode at all; it merely transports the same critical relative amplitude from one scale to another.

This explains the mathematical role of the MRSTT machinery in the seeded problem:

```text
high Mellin frequencies:
seeded Type-II methods can yield genuine fixed powers.

critical low Mellin frequencies:
the boundary mode is scale-coherent and survives every long-anchor comparison.
```

Recent Guth–Maynard large-value estimates improve the frequency of large Dirichlet-polynomial values and the resulting zero-density / short-interval ranges. Such improvements can strengthen the high-frequency part of a Type-II argument, but they do not alter the long-anchor ceiling unless they are coupled to a new theorem suppressing the boundary-scale prime error itself.

Paper 63 therefore corrects Paper 62's identification of the immediate Type-II bottleneck. The $W$ exponents contain technical slack. The fundamental amplifier obstruction is the low-frequency anchor.

No RH theorem is claimed.

---

# 1. Entry state

Assume

$$
\operatorname{PESC}(\kappa)
$$

with

$$
0<\kappa<1.
$$

Set

$$
\boxed{
d=\frac{\kappa}{2}.
}
$$

The current sharp direct frontier F-RH-017-v3 asks for, at

$$
H=X^{1-\tau},
$$

an estimate

$$
\#\left\{
x:
|\psi(x+H)-\psi(x)-H|
>
HX^{-\nu}
\right\}
\ll
X^{1-c}
$$

with

$$
\boxed{
\nu>d,
\qquad
c>\min(d,\tau).
}
$$

Paper 62 showed that a seeded insertion into MRSTT produces fixed-power almost-all short-interval estimates, but treated the published $W^4$ and $W^{-1/10}$ exponents as the operative ceiling.

We now inspect the proof exactly.

---

# 2. What MRSTT Lemma 3.3 actually requires

MRSTT Lemma 3.3(i) controls the variance between two normalized interval averages.

Its scale hypothesis is

$$
\boxed{
H_2\le\frac{X}{W^3}.
}
$$

The low-frequency part of its proof uses

$$
|t|\le W
$$

and first-order Taylor expansion.

At the normalized-average level, the low-frequency difference is bounded by

$$
\ll
W^2
\frac{H_2}{X}
\log^{O(1)}X.
$$

Squaring gives

$$
\boxed{
\mathcal V_{\rm low}
\ll
W^4
\frac{H_2^2}{X^2}
\log^{O(1)}X.
}
$$

The published Lemma 3.5 assumes the stronger condition

$$
H_2\le X/W^4,
$$

but after invoking Lemma 3.3 its proof does not use the extra factor $W$.

Thus:

```text
MRSTT Lemma 3.5 statement:
H2 <= X/W^4

variance lemma actually used:
H2 <= X/W^3
```

The $W^4$ is proof slack for the Type-II major-arc lemma.

---

# 3. Target-dependent low-frequency scale condition

Suppose the desired normalized mean-square saving is

$$
W^{-a}
$$

for fixed

$$
a>0.
$$

It is enough that

$$
W^4
\frac{H_2^2}{X^2}
\le
W^{-a-o(1)}.
$$

If

$$
H_2\le\frac{X}{W^q},
$$

this becomes

$$
W^{4-2q}
\le
W^{-a-o(1)}.
$$

Therefore any fixed

$$
\boxed{
q>2+\frac a2
}
$$

suffices after absorbing logarithmic factors.

This improves both $W^4$ and $W^3$ once the actual target exponent is taken into account.

Create:

```text
B-RH-077
TARGET_DEPENDENT_LOW_FREQUENCY_SCALE_CONDITION_FOR_MRSTT_VARIANCE
CERTIFIED
```

---

# 4. The $3/10$ mean-square exponent is also slack

MRSTT Lemma 3.5 aims to prove

$$
\boxed{
\mathcal V_{II}
\ll
W^{-3/10}
\log^{O(1)}X.
}
$$

In the hard Type-II range the proof applies the Baker–Harman–Pintz parallelogram lemma.

The relevant Dirichlet-polynomial input is

$$
|C(1+it)|
\le
W^{-1/3},
$$

and the parallelogram output is

$$
\boxed{
\int
|A(1+it)B(1+it)C(1+it)|dt
\ll
W^{-1/3}
\log^{O(1)}X.
}
$$

Thus the proof has a strict exponent margin

$$
\frac13-\frac{3}{10}
=
\frac1{30}
$$

used only to absorb logarithmic factors and simplify the statement.

Consequently:

## Theorem 4.1 — Proof-tightened Type-II mean square

For every fixed

$$
0<a<\frac13
$$

and every fixed

$$
q>2+\frac a2,
$$

the proof of MRSTT Lemma 3.5 gives, under the same Type-II coefficient and Dirichlet-polynomial hypotheses and with

$$
H_2\le\frac{X}{W^q},
$$

$$
\boxed{
\frac1X
\int_X^{2X}
|\Delta_{H_1,H_2}^{II}(x)|^2dx
\ll
H_1^2
W^{-a}
\log^{O(1)}X.
}
$$

The same strengthening applies to the one-scale variants of the lemma.

Create:

```text
B-RH-078
PROOF_TIGHTENED_MRSTT_TYPEII_MEAN_SQUARE_ANY_A_LT_ONE_THIRD
CERTIFIED
```

This is a refinement of the published lemma, not a new large-value theorem.

---

# 5. Asymmetric Chebyshev conversion

Suppose

$$
\frac1X
\int_X^{2X}
|\Delta(x)|^2dx
\ll
H^2
W^{-a}
L(X),
$$

where

$$
L(X)=\log^{O(1)}X.
$$

Fix

$$
b>0.
$$

Chebyshev at the threshold

$$
H W^{-b}
$$

gives

$$
\operatorname{meas}
\left\{
x:
|\Delta(x)|>HW^{-b}
\right\}
\ll
X
W^{2b-a}
L(X).
$$

Therefore for every fixed

$$
c_0>0
$$

satisfying

$$
\boxed{
2b+c_0<a,
}
$$

one has

$$
\boxed{
|\Delta(x)|
\le
HW^{-b}
}
$$

outside a set of measure

$$
\boxed{
O\left(
XW^{-c_0}
\log^{O(1)}X
\right).
}
$$

Create:

```text
B-RH-079
ASYMMETRIC_MRSTT_TYPEII_THRESHOLD_EXCEPTION_TRADEOFF
CERTIFIED
```

The published choice $b=c_0=1/10$ is one convenient interior point when $a=3/10$.

---

# 6. Optimized proof-slack variance budget

Put

$$
H=X^{1-\tau},
\qquad
W=X^w.
$$

To compare to a scale

$$
H_2\ge H
$$

under the sharpened scale condition

$$
H_2\le X/W^q,
$$

we need

$$
\boxed{
qw\le\tau.
}
$$

The Type-II threshold exponent in powers of $X$ is

$$
\nu_{\rm diff}=bw.
$$

The exceptional exponent is

$$
c_{\rm diff}=c_0w.
$$

Since

$$
2b+c_0<a,
$$

$$
\boxed{
2\nu_{\rm diff}
+
c_{\rm diff}
<
aw.
}
$$

Using

$$
w\le\tau/q,
$$

we obtain

$$
\boxed{
2\nu_{\rm diff}
+
c_{\rm diff}
<
\frac{a}{q}\tau.
}
$$

Now optimize

$$
\frac{a}{q}
$$

subject to

$$
0<a<\frac13,
\qquad
q>2+\frac a2.
$$

The limiting ratio is

$$
\boxed{
\sup
\frac{a}{2+a/2}
=
\frac{2}{13}.
}
$$

Hence:

## Theorem 6.1 — Optimized current-proof Type-II variance budget

The proof architecture of MRSTT Lemmas 3.3–3.5, after removing the explicit exponent slack but without new analytic input, satisfies the limiting budget

$$
\boxed{
2\nu_{\rm diff}
+
c_{\rm diff}
<
\frac{2}{13}\tau.
}
$$

Create:

```text
B-RH-080
OPTIMIZED_MRSTT_CURRENT_PROOF_TYPEII_VARIANCE_BUDGET_TWO_OVER_THIRTEEN_TAU
CERTIFIED
```

This replaces Paper 62's crude $\tau/40$ symmetric ceiling as the correct proof-slack audit.

---

# 7. Why the improved budget still cannot amplify

In the seeded insertion of Paper 62, the Dirichlet-polynomial hypothesis itself forces

$$
\tau\ll d.
$$

In this regime F-RH-017-v3 requires

$$
\nu>d,
\qquad
c>\tau.
$$

Therefore any successful exceptional theorem must satisfy

$$
\boxed{
2\nu+c
>
2d+\tau
>
3\tau.
}
$$

But the optimized current Type-II proof supplies only

$$
\boxed{
2\nu_{\rm diff}+c_{\rm diff}
<
\frac{2}{13}\tau.
}
$$

The gap is enormous and fixed.

Thus removing the published $W$ exponent slack cannot turn MRSTT Lemma 3.5 into an amplifier.

---

# 8. The stronger long-scale anchor barrier

The preceding budget still concerns only the scale-difference term.

There is a more fundamental obstruction.

Let

$$
S_H(x)
=
\psi(x+H)-\psi(x).
$$

Any long-scale comparison has the identity

$$
\boxed{
S_H(x)-H
=
\Delta_{H,H_2}(x)
+
\frac{H}{H_2}
\left(
S_{H_2}(x)-H_2
\right).
}
$$

Let

$$
H_2=X^{1-\tau_2},
\qquad
0\le\tau_2\le\tau.
$$

The seed PESC $(\kappa)$ gives

$$
|A(x)|
\ll
X^{1-d+o(1)}.
$$

The actual von Mangoldt local increment bound also gives

$$
|S_{H_2}(x)-H_2|
\ll
H_2X^{o(1)}.
$$

Thus

$$
\boxed{
|S_{H_2}(x)-H_2|
\ll
X^{1-\max(d,\tau_2)+o(1)}.
}
$$

Scale it back to $H$:

$$
\begin{aligned}
\frac{H}{H_2}
|S_{H_2}(x)-H_2|
&\ll
H
X^{
-\left(
\max(d,\tau_2)-\tau_2
\right)
+o(1)
}
\\
&=
H
X^{-(d-\tau_2)_++o(1)}.
\end{aligned}
$$

Therefore the seed-controlled anchor exponent is

$$
\boxed{
\nu_{\rm anchor}
=
(d-\tau_2)_+
\le d.
}
$$

This is independent of the quality of the scale-difference theorem.

Create:

```text
O-RH-146
SEEDED_LONG_SCALE_ANCHOR_HAS_CRITICAL_THRESHOLD_CEILING_NU_LE_D
CERTIFIED
```

---

# 9. Perfect scale coherence still cannot cross the boundary

Suppose hypothetically that

$$
\Delta_{H,H_2}(x)=0
$$

identically.

Then the best threshold obtained from the seed anchor is still

$$
\boxed{
|S_H(x)-H|
\ll
H X^{-d+o(1)}
}
$$

only in the most favorable anchor limit.

F-RH-017-v3 requires

$$
\boxed{
\nu>d.
}
$$

Therefore:

## Theorem 9.1 — No scale-comparison amplifier from a critical seed anchor

No method of the form

```text
short interval
=
controlled scale-difference
+
long interval controlled only by the seed
```

can prove the supercritical F-RH-017-v3 threshold.

This remains true even if the scale-difference estimate is perfect.

Create:

```text
O-RH-147
PERFECT_SCALE_COHERENCE_PLUS_SEED_ANCHOR_CANNOT_AMPLIFY_PESC
CERTIFIED
```

This is strictly stronger than the $W$ -geometry obstruction of Paper 62.

---

# 10. Boundary-zero sharpness of the anchor barrier

Let

$$
\rho
=
1-d+i\gamma
$$

be a hypothetical boundary zero.

Its explicit-formula mode is

$$
F_\rho(x)
=
-\frac{x^\rho}{\rho}.
$$

For any sublinear

$$
H_2=o(X),
$$

$$
F_\rho(x+H_2)-F_\rho(x)
=
-H_2x^{\rho-1}
\left(
1+o_\rho(1)
\right).
$$

Thus

$$
\boxed{
|F_\rho(x+H_2)-F_\rho(x)|
\asymp_\rho
H_2X^{-d}.
}
$$

Scaling from $H_2$ to $H$ gives

$$
\boxed{
\frac{H}{H_2}
|F_\rho(x+H_2)-F_\rho(x)|
\asymp_\rho
H X^{-d}.
}
$$

The critical boundary amplitude is exactly scale-invariant under normalized interval comparison.

This is the short-interval form of the critical locking observed in Papers 54–55.

Thus the anchor barrier is not caused by a crude seed bound.

The actual hypothetical boundary mode saturates it.

---

# 11. Why higher-order scale filters do not solve the problem

One may try to replace a single difference of scales by a higher-order linear combination

$$
\sum_{j=0}^{R}
\lambda_j
\frac{S_{H_j}(x)}{H_j}
$$

chosen to cancel several low-frequency Taylor moments.

Such filters can indeed improve the low-frequency error in the Parseval reduction and permit a larger frequency cutoff.

However, for the smooth boundary mode,

$$
\frac{
F_\rho(x+H)-F_\rho(x)
}{H}
=
-x^{\rho-1}
+
O_\rho(H/X).
$$

All normalized sublinear scales have the same leading value

$$
-x^{\rho-1}.
$$

A scale filter whose coefficients sum to zero cancels this boundary mode together with the unwanted low-frequency Taylor term.

Therefore it improves scale coherence but does not produce a supercritical bound for the original short interval.

Recovering the original short-interval value again requires an anchor, and the critical amplitude returns.

Thus higher-order scale filtering can improve the technical $W$ budget but cannot evade O-RH-147.

---

# 12. Relation to Guth–Maynard large-value improvements

Guth and Maynard's 2026 theorem gives new bounds for the frequency of large values of Dirichlet polynomials, especially near the classical $N^{3/4}$ critical range. It yields the improved zero-density estimate

$$
N(\sigma,T)
\le
T^{30(1-\sigma)/13+o(1)}
$$

and improved prime short-interval ranges.

Such estimates can improve high-frequency Dirichlet-polynomial control and may strengthen descendants of the Baker–Harman–Pintz step.

But within a scale-comparison architecture they do not alter Theorem 9.1:

the long anchor remains only critical unless one proves new prime-error information beyond the seed.

Therefore a future Guth–Maynard insertion is potentially useful for the high-frequency residual but cannot, by itself, be the missing PESC amplifier.

---

# 13. Correction to Paper 62's barrier interpretation

Paper 62's final non-amplification conclusion remains correct.

Its immediate explanation is corrected.

## Correction C-RH-003

Old interpretation:

```text
The principal obstruction inside current MRSTT
is H2 <= X/W^4 plus W^-1/10 output.
```

Correct interpretation:

```text
The published W exponents contain proof slack.

The optimized current proof allows:
- target-dependent H2 <= X/W^q with q>2+a/2;
- any mean-square exponent a<1/3;
- asymmetric threshold/exception tradeoff 2b+c0<a.

Even after all of these improvements,
the architecture remains non-amplifying.

The stronger reason is the seed long-anchor ceiling nu<=kappa/2.
```

Thus O-RH-145 remains a valid statement that the published MRSTT architecture does not reach F-RH-017, but O-RH-146 and O-RH-147 identify the more fundamental obstruction.

---

# 14. Updated Campaign-46 decomposition

The seeded short-interval problem should now be split by Mellin frequency.

## High-frequency sector

Existing 2026 Type-II machinery, strengthened by the seed, already gives fixed-power control.

Proof-slack optimization can improve its constants.

This sector is not the root obstruction.

## Critical low-frequency sector

A boundary zero produces a slowly varying multiplicative mode with relative amplitude

$$
X^{-d}.
$$

Normalized scale comparison preserves that amplitude.

The seed permits it.

This is the sector which must be suppressed to obtain

$$
\nu>d.
$$

Thus the next direct problem is not another Type-II high-frequency variance estimate.

It is a low-frequency prime-side boundary-packet theorem.

---

# 15. New next track

Open:

```text
PT6
DIRECT_LOW_MELLIN_FREQUENCY_BOUNDARY_PACKET_SUPPRESSION
```

Target:

prove, without using a longer-scale seed anchor, a supercritical almost-all estimate

$$
\boxed{
|\psi(x+H)-\psi(x)-H|
\le
H X^{-d-\eta}
}
$$

outside an exceptional set satisfying the corrected F-RH-017-v3 gate.

Allowed mechanisms must genuinely use prime arithmetic at the low-frequency boundary.

Candidate subtracks:

```text
PT6A
SIGN-SENSITIVE LOW-FREQUENCY PRIME LARGE DEVIATION

PT6B
BOUNDARY-PACKET PRIME-FACTOR INCOMPATIBILITY

PT6C
NONLINEAR LOW-FREQUENCY EULER/HEATH-BROWN COERCIVITY

PT6D
DIRECT F-RH-017-v3 OR CERTIFIED RH-EQUIVALENT WALL
```

Hard rejections:

```text
MORE_SCALE_COMPARISON_WITH_SEED_LONG_ANCHOR
MORE_W_EXPONENT_OPTIMIZATION_AS_IF_IT_CROSSES_NU_D
HIGHER_ORDER_SCALE_FILTER_WITHOUT_RECOVERY_LEDGER
CLAIM_GUTH_MAYNARD_HIGH_FREQUENCY_LARGE_VALUES_REMOVE_CRITICAL_ANCHOR
ASSUME_RH
```

---

# 16. External calibration

## 16.1. MRSTT proof

K. Matomäki, M. Radziwiłł, X. Shao, T. Tao, J. Teräväinen,
*Higher uniformity of arithmetic functions in short intervals II. Almost all intervals*,
Inventiones Mathematicae 244 (2026), 967–1091.

The published proof records:

- Lemma 3.3 variance comparison under $H_2\le X/W^3$ ;
- the low-frequency Taylor estimate producing the $W^2H_2/X$ factor;
- Baker–Harman–Pintz output $W^{-1/3}$ ;
- Lemma 3.5's convenient target $W^{-3/10}$ and final $W^{-1/10}$ Chebyshev choice.

URL:

https://link.springer.com/article/10.1007/s00222-026-01408-6

## 16.2. Guth–Maynard large values

L. Guth and J. Maynard,
*New large value estimates for Dirichlet polynomials*,
Annals of Mathematics 203 (2026), 623–675.

Their main large-values theorem improves the frequency estimates in the $N^{3/4}$ critical range and yields the zero-density exponent $30/13$ and improved short-interval prime ranges.

URL:

https://annals.math.princeton.edu/2026/203-2/p06

---

# 17. State transition

Advance the candidate state from

$$
v1.53
$$

to

$$
v1.54.
$$

Add:

```text
B-RH-077
TARGET_DEPENDENT_LOW_FREQUENCY_SCALE_CONDITION_FOR_MRSTT_VARIANCE
CERTIFIED
```

Add:

```text
B-RH-078
PROOF_TIGHTENED_MRSTT_TYPEII_MEAN_SQUARE_ANY_A_LT_ONE_THIRD
CERTIFIED
```

Add:

```text
B-RH-079
ASYMMETRIC_MRSTT_TYPEII_THRESHOLD_EXCEPTION_TRADEOFF
CERTIFIED
```

Add:

```text
B-RH-080
OPTIMIZED_MRSTT_CURRENT_PROOF_TYPEII_VARIANCE_BUDGET_TWO_OVER_THIRTEEN_TAU
CERTIFIED
```

Add:

```text
O-RH-146
SEEDED_LONG_SCALE_ANCHOR_HAS_CRITICAL_THRESHOLD_CEILING_NU_LE_D
CERTIFIED
```

Add:

```text
O-RH-147
PERFECT_SCALE_COHERENCE_PLUS_SEED_ANCHOR_CANNOT_AMPLIFY_PESC
CERTIFIED
```

Add correction:

```text
C-RH-003
PAPER62_MRSTT_W_EXPONENT_BARRIER_REINTERPRETED_AS_PROOF_SLACK_BELOW_A_STRONGER_ANCHOR_BARRIER
```

Open:

```text
PT6
DIRECT_LOW_MELLIN_FREQUENCY_BOUNDARY_PACKET_SUPPRESSION
```

No RH certificate is created.

---

# 18. Conclusion

The MRSTT proof is stronger than its convenient published exponents suggest.

The factor $W^4$ is not intrinsic.

The exponent $3/10$ is not intrinsic.

The symmetric $1/10$ threshold / exception choice is not intrinsic.

After removing those slacks, the existing Type-II variance proof has the optimized budget

$$
\boxed{
2\nu_{\rm diff}+c_{\rm diff}
<
\frac{2}{13}\tau.
}
$$

But even a perfect scale-difference theorem cannot cross the seeded boundary.

The long anchor itself has the critical ceiling

$$
\boxed{
\nu_{\rm anchor}\le\frac{\kappa}{2}.
}
$$

A boundary zero mode saturates that ceiling exactly and is invariant at leading order under normalized scale comparison.

Therefore the remaining arithmetic wall is low-frequency.

Future progress must suppress the boundary packet directly, not improve the high-frequency scale-comparison constants.
