# CSM_RH Paper 16
## Average Hardy–Littlewood Precision Floor, the BDH $q=1$ Isolation Law, and Arithmetic-Shell Exhaustion

**Project:** `CSM_RH`  
**Paper:** `16`  
**Version:** `v0.1`  
**Date:** `2026-09-05`  
**Parent state:** `CSM_RH v1.6 / Paper 15`  
**Campaign:** `15 — DIRECT_ALL_SHIFT_PRIME_CORRELATION_AUDIT`  
**Status:** current-technology audit / arithmetic-shell closure; not a proof or disproof of RH

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

The campaign returns to the shortest certified target path:

$$
\operatorname{PESC}(\kappa)
$$

and compares it directly with the strongest relevant average prime-pair, Selberg-integral, dispersion, and Barban–Davenport–Halberstam type interfaces.

The main conclusion is:

> the currently known methods already provide broad shift coverage and very strong subpower control, but no current bridge supplies a fixed $N$ -power for the exact signed endpoint-weighted all-shift aggregate.

Accordingly, this paper closes the present representation/mechanism shell and recommends that subsequent work generate proof candidates directly against PESC rather than create further surrogate gates.

No live GLM-5.3-Flash run is claimed.

---

# 1. Canonical all-shift target

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
q_n-1.
$$

Define the endpoint weight

$$
w_N(n)
=
\begin{cases}
N,
&
1\le n\le N,
\\
2N-n,
&
N<n<2N,
\\
0,
&
n\ge2N.
\end{cases}
$$

For a shift

$$
1\le h\le2N-2,
$$

define the exact prime-only weighted shift correlation

$$
\boxed{
\mathcal R_N^\vartheta(h)
=
\sum_{m<2N-h}
w_N(m+h)
c_m
c_{m+h}.
}
$$

Paper 15 gave

$$
\boxed{
\mathcal C_N^\vartheta
=
\sum_{h=1}^{2N-2}
\mathcal R_N^\vartheta(h).
}
$$

The fixed-power target is

$$
\boxed{
\left|
\sum_h
\mathcal R_N^\vartheta(h)
\right|
\ll
N^{3-\kappa+o(1)}
}
$$

for one fixed

$$
0<\kappa<\frac12.
$$

This is PESC.

---

# 2. Exact endpoint interpretation

Recall

$$
B(j)
=
\vartheta(j)-j
=
\sum_{n\le j}c_n.
$$

Then

$$
\boxed{
J_N^\vartheta
=
\sum_{j=N}^{2N-1}
B(j)^2
=
D_N^\vartheta
+
2
\sum_h
\mathcal R_N^\vartheta(h),
}
$$

where

$$
D_N^\vartheta
=
O(N^2\log N).
$$

Hence PESC and the prime-only dyadic energy PODEE are exponent-equivalent.

This exact identity is the canonical authority boundary for every average-correlation method considered below.

---

# 3. Small shifts are not the first fixed-power barrier

Let

$$
0<H_0<N.
$$

Since

$$
|c_n|
\ll
\log N
$$

and

$$
w_N(n)\le N,
$$

for every fixed shift $h$,

$$
\boxed{
|\mathcal R_N^\vartheta(h)|
\ll
N^2(\log N)^2.
}
$$

Therefore

$$
\boxed{
\sum_{h\le H_0}
|\mathcal R_N^\vartheta(h)|
\ll
H_0N^2(\log N)^2.
}
$$

Take

$$
\sigma
=
\frac8{33}.
$$

For

$$
H_0
=
N^{\sigma+\varepsilon},
$$

we obtain

$$
\boxed{
\sum_{h\le H_0}
|\mathcal R_N^\vartheta(h)|
\ll
N^{2+8/33+\varepsilon+o(1)}
=
N^{74/33+\varepsilon+o(1)}.
}
$$

Because

$$
\frac{74}{33}
<
\frac52,
$$

this is below every first target

$$
N^{3-\kappa}
$$

with

$$
0<\kappa<\frac12
$$

after choosing $\varepsilon$ sufficiently small.

Thus the shift ranges below the Matomäki–Radziwiłł–Tao threshold are already harmless for the first fixed-strip objective.

---

# 4. Averaged Hardy–Littlewood theorem

Matomäki, Radziwiłł, and Tao prove the following averaged prime-pair theorem.

Let

$$
\sigma=\frac8{33}.
$$

If

$$
X^{\sigma+\varepsilon}
\le
H
\le
X^{1-\varepsilon},
$$

then for every fixed

$$
A>0,
$$

one has

$$
\boxed{
\sum_{X<n\le2X}
\Lambda(n)\Lambda(n+h)
=
\mathfrak S(h)X
+
O_{A,\varepsilon}
\left(
X\log^{-A}X
\right)
}
$$

for all but

$$
O_{A,\varepsilon}
\left(
H\log^{-A}X
\right)
$$

values of $h$ in a shift window of length $O(H)$.

They explicitly note that their divisor-correlation cases can be modified to yield power savings, while their von Mangoldt correlation case does not provide power-saving error terms.

This distinction is exactly the distinction relevant to PESC.

---

# 5. Abstract almost-all-to- $L^1$ transfer

Let a shift block $\mathcal H$ contain $H$ shifts.

Suppose a residual $E(h)$ satisfies:

## Good shifts

For all but

$$
O
\left(
H\log^{-A}N
\right)
$$

shifts,

$$
|E(h)|
\ll
N\log^{-A}N.
$$

## Exceptional shifts

For every shift,

$$
|E(h)|
\ll
N(\log N)^B
$$

for some fixed $B$.

Then:

## Lemma 5.1

For every fixed $A'>0$, by choosing $A$ sufficiently large in terms of $A',B$,

$$
\boxed{
\sum_{h\in\mathcal H}
|E(h)|
\ll
HN\log^{-A'}N.
}
$$

### Proof

The good shifts contribute

$$
O
\left(
HN\log^{-A}N
\right).
$$

The exceptional shifts contribute

$$
O
\left(
H\log^{-A}N
\cdot
N(\log N)^B
\right).
$$

Choose

$$
A>A'+B.
$$

 $\square$

Thus almost-all Hardy–Littlewood with arbitrary logarithmic savings converts into arbitrary logarithmic $L^1$ savings over shifts.

It does not convert into a fixed power.

---

# 6. Endpoint-weight precision transfer

The PESC shift carries an additional endpoint weight of size at most $N$.

Consequently, any shift-block theorem whose unweighted residual has only the precision

$$
HN\log^{-A}N
$$

produces, at best under direct absolute transfer,

$$
\boxed{
HN^2\log^{-A}N
}
$$

on the endpoint-weighted aggregate.

For macroscopic shift blocks

$$
H=N^{1-o(1)},
$$

this is

$$
\boxed{
N^{3-o(1)}
}
$$

with arbitrary logarithmic savings.

It is not

$$
N^{3-\kappa}
$$

for fixed $\kappa>0$.

This creates:

```text
O-RH-035
AVERAGED_HARDY_LITTLEWOOD_FIXED_POWER_PRECISION_FLOOR
status:
  CERTIFIED AS CURRENT-THEOREM PRECISION AUDIT
```

---

# 7. Shift coverage versus precision

The averaged Hardy–Littlewood technology solves a major coverage problem:

```text
most shifts in polynomially long windows
```

can be treated with the expected singular-series main term.

The 2019 theorem reaches shift windows down to

$$
H
=
X^{8/33+\varepsilon}.
$$

More recent short-interval uniformity work for the von Mangoldt function proves strong logarithmic decay against nilsequence tests and obtains Hardy–Littlewood conclusions with a short average over one variable.

But the precision in the von Mangoldt uniformity statement is still of the form

$$
\log^{-A}X,
$$

not a fixed $X^{-\delta}$.

Thus:

```text
SHIFT COVERAGE
  largely solved for present reduction purposes

FIXED-POWER ERROR PRECISION
  not solved
```

---

# 8. Why the small-shift threshold does not rescue the argument

Section 3 shows that small shifts up to

$$
N^{8/33+\varepsilon}
$$

are harmless even by a trivial bound.

Therefore the obstruction is not caused by the average theorem failing on very small $h$.

The obstruction lies in the macroscopic family of shifts:

$$
h
\gg
N^{8/33+\varepsilon},
$$

where the average theorem has broad coverage but only logarithmic-relative precision.

This cleanly separates:

```text
range problem
from
precision problem.
```

---

# 9. Current PNT remainder is stronger than the average-HL aggregate bound but still subpower

The direct relation

$$
B(x)=\vartheta(x)-x
$$

gives

$$
J_N^\vartheta
\le
N
\max_{N\le x\le2N}
|B(x)|^2.
$$

Modern zero-free-region-to-PNT-error results provide very strong subpower estimates for $B(x)$.

The corresponding PESC bound is therefore stronger than an arbitrary fixed logarithmic saving:

$$
\boxed{
\mathcal C_N^\vartheta
=
N^{3-o(1)}.
}
$$

But a shrinking zero-free region gives a shrinking exponent improvement.

It does not give

$$
N^{3-\kappa}
$$

for fixed $\kappa>0$.

Recent work by Johnston and Broucke sharpens the quantitative correspondence between zero-free contours and PNT remainder terms, reinforcing that distinction.

Thus average prime-pair technology does not currently improve the exponent class already visible from the direct PNT route.

---

# 10. Power-accurate average Hardy–Littlewood would solve the target

Suppose one could upgrade the averaged prime-pair theorem so that, after the correct endpoint weighting and deterministic centering, the complete signed error satisfies

$$
\boxed{
\left|
\sum_h
E_N(h)
\right|
\ll
N^{3-\kappa+o(1)}.
}
$$

Then PESC follows.

But by Section 2 the resulting theorem is already exponent-equivalent to the prime-only PNT mean square.

Therefore a power-accurate signed average Hardy–Littlewood theorem is not a lower-strength substitute for PESC.

It is a proof interface for PESC.

Create:

```text
F-RH-015
POWER_ACCURATE_SIGNED_AVERAGE_HARDY_LITTLEWOOD
abbrev:
  PASAHL
status:
  INTERFACE-EQUIVALENT / NOT A LOWER-STRENGTH FRONTIER
```

---

# 11. Standard prime-pair variance is stronger than the signed target

The standard pair-error variance has the shape

$$
\sum_h
|E(h)|^2.
$$

PESC needs only

$$
\left|
\sum_h
E(h)
\right|.
$$

Cauchy transfers the variance gate to the signed gate, but not conversely.

Thus variance results are analytically convenient but stronger than the minimal target.

The 2026 Chou–Haag–Huryn–Ledoan lower bound for prime-pair error variance already shows that fixed-power improvement of that positive object carries rightmost-zero strength.

Campaign 15 therefore does not promote prime-pair variance as a shorter route.

---

# 12. Barban–Davenport–Halberstam geometry

For a finite sequence $(u_n)$ and one endpoint $j$, define

$$
V_j(q)
=
\sum_{a\bmod q}
\left|
\sum_{\substack{
n\le j\\
n\equiv a\pmod q
}}
u_n
\right|^2.
$$

Expanding gives

$$
\boxed{
V_j(q)
=
\sum_{m,n\le j}
u_m\overline{u_n}
\mathbf1_{q\mid(m-n)}.
}
$$

Thus a linear combination

$$
\sum_q
\beta_qV_j(q)
$$

weights a nonzero difference

$$
h=m-n
$$

by

$$
\boxed{
K_\beta(h)
=
\sum_{q\mid h}
\beta_q.
}
$$

This is divisor-weight geometry.

---

# 13. The $q=1$ isolation law

Suppose

$$
K_\beta(h)=1
$$

for every positive integer $h$.

Then:

## Theorem 13.1 — BDH Constant-Kernel Isolation

$$
\boxed{
\beta_1=1,
\qquad
\beta_q=0
\quad
(q>1).
}
$$

### Proof

The condition is

$$
\sum_{q\mid h}\beta_q=1.
$$

By Möbius inversion,

$$
\beta_n
=
\sum_{d\mid n}
\mu(n/d)
\cdot1.
$$

This is $1$ for $n=1$ and $0$ for every $n>1$. $\square$

Therefore the constant all-shift kernel is exactly the $q=1$ divisor mode.

High-modulus progression variances cannot reconstruct it by an exact divisor-weight linear combination.

Create:

```text
O-RH-036
BDH_Q1_CONSTANT_KERNEL_ISOLATION
status:
  CERTIFIED
```

---

# 14. Endpointwise interpretation of the BDH obstruction

For each endpoint $j$,

$$
B(j)
=
\sum_{n\le j}c_n.
$$

The $q=1$ progression sum is precisely the complete cumulative sum.

Its square is

$$
|B(j)|^2.
$$

The PODEE target is an endpoint average of these $q=1$ energies:

$$
J_N^\vartheta
=
\sum_{j=N}^{2N-1}
|B(j)|^2.
$$

Thus the exact BDH mode required by PESC is not hidden among large moduli.

It is the trivial modulus itself.

This explains why strong distribution of primes in nontrivial arithmetic progressions does not automatically control PESC.

---

# 15. Harper 2025 and the AP-variance frontier

Recent work gives simple asymptotics for Barban–Davenport–Halberstam type variances for broad classes of sequences, and recovers prime cases.

These theorems improve understanding of progression variance and its main/error terms.

But the geometry remains:

$$
\mathbf1_{q\mid h}
$$

or averages of such divisor kernels.

Campaign 15's target uses the constant difference kernel after endpoint accumulation.

Theorem 13.1 therefore blocks a direct exact transfer from nontrivial-modulus BDH information to PESC.

This is a geometry mismatch, not a weakness of BDH.

---

# 16. Selberg integral as a triangular correlation potential

For an arithmetic sequence $u_n$, a short-interval quadratic mean expands into additive correlations with a triangular shift weight of the schematic form

$$
\boxed{
\sum_{|h|<H}
(H-|h|)
C_u(h).
}
$$

This is the basic correlation structure behind Selberg integrals.

It is a positive quadratic mean.

The PESC target is instead a signed all-shift endpoint aggregate.

Passing between a triangular correlation potential and its unweighted signed partial sums requires discrete differentiation in $H$ and exact control of the boundary/main terms.

A bound on the positive Selberg integral therefore does not by itself create a lower-strength PESC theorem.

At fixed-power precision, the same prime-error energy obstruction reappears.

---

# 17. Selberg-integral shell status

The literature connecting Selberg integrals, prime correlations, and zeta-zero pair correlation is deep and useful.

But for the present CSM target:

```text
Selberg quadratic mean
  positive and stronger/different

PESC
  signed endpoint all-shift aggregate
```

No current Selberg-integral theorem identified in this audit produces a fixed power for PESC without importing equivalent prime-error strength.

Therefore the Selberg-integral route remains a proof tool, not a lower-strength canonical frontier.

---

# 18. Current-technology comparison

The direct target can now be compared with the main available technologies.

## Average Hardy–Littlewood

Strength:

$$
\text{arbitrary log-power saving for almost all shifts}.
$$

Fixed power:

```text
NO for von Mangoldt correlations.
```

## 2024 higher uniformity / short-average Hardy–Littlewood

Strength:

$$
\log^{-A}X
$$

for the von Mangoldt uniformity statements in the stated ranges.

Fixed power:

```text
NO.
```

## Direct PNT zero-free-region route

Strength:

```text
strong subpower / stretched-logarithmic exponential type.
```

Fixed power:

```text
NO without a fixed zero strip.
```

## BDH

Strength:

```text
strong AP variance information.
```

Exact constant-shift-kernel transfer:

```text
NO except q=1.
```

## Selberg integral

Strength:

```text
quadratic short-interval information.
```

Lower-strength direct PESC bridge:

```text
NOT IDENTIFIED.
```

---

# 19. Arithmetic shell exhaustion

The sequence of CSM_RH campaigns has now tested:

```text
positive zero packets
character major arcs
density estimates
Weil local/globalization
fixed aperture
positive prime variance
signed centered shifts
Fourier zero frequency
Vaughan
fixed-K Heath-Brown
growing-K Heath-Brown
prime-only energy
Selberg feedback
signed sieve
asymptotic sieve
Möbius parity bilinear forms
Möbius dilate second moments
averaged Chowla
average Hardy-Littlewood
BDH
Selberg integral
```

Every surviving fixed-power statement either:

1. is exponent-equivalent to PESC/PODEE;
2. is stronger than PESC;
3. requires a second new bridge theorem;
4. or currently supplies only subpower precision.

Create:

```text
O-RH-037
CURRENT_ARITHMETIC_SHELL_EXHAUSTION
status:
  CERTIFIED RELATIVE TO AUDITED ROUTES
```

This is not a universal impossibility theorem.

It is a closure-state result:

> no audited representation or standard mechanism has produced a strictly lower-strength fixed-power frontier than PESC.

---

# 20. Stop creating surrogate frontiers

Because PASAHL is interface-equivalent rather than lower strength, this paper does not recommend another surrogate target.

The canonical target remains:

```text
F-RH-010
PESC
```

with

$$
\boxed{
\left|
\sum_{h=1}^{2N-2}
\mathcal R_N^\vartheta(h)
\right|
\ll
N^{3-\kappa+o(1)}
}
$$

for some fixed

$$
0<\kappa<\frac12.
$$

Further progress should be judged by whether it proves a genuinely new estimate inside a proof of this statement.

---

# 21. Campaign 16

The next campaign changes research mode.

```text
CSM_RH Campaign 16
DIRECT_PESC_THEOREM_GENERATION
```

There is no new representation target.

Workers must generate actual candidate lemmas for PESC.

---

# 22. Campaign 16 allowed candidate types

## G1 — Signed error cancellation across shifts

Prove a new theorem on the signs or correlations of Hardy–Littlewood prime-pair errors after endpoint weighting.

## G2 — New circle-method power estimate

Obtain a fixed power in the signed integrated minor/major-arc residual without passing through a stronger positive variance gate.

## G3 — New prime-sampling contraction

Prove a genuine contraction for

$$
\sum_n
w_N(n)c_nB(n-1).
$$

## G4 — New scale recursion

Derive a recurrence with linear cumulative contraction mass for PESC/PODEE.

## G5 — New arithmetic identity with immediate power-bearing remainder

An identity counts only if its remainder already has a proved fixed power.

---

# 23. Campaign 16 prohibited outputs

Reject:

```text
new notation for PESC;
another equivalent mean-square criterion;
another positive gate with no estimate;
a hypothetical average Hardy-Littlewood power theorem merely restated;
a fixed zero strip assumed as input;
density-only arguments;
finite numerics as asymptotic evidence;
log-power or stretched-log savings labeled fixed power.
```

The campaign is now theorem-generation, not representation-generation.

---

# 24. Campaign 16 worker roles

`CSM_RH` remains the protocol.

GLM-5.3-Flash may be used as a replaceable high-volume worker provider.

## Designer

Must output:

```text
one concrete new lemma;
exact hypotheses;
exact conclusion;
why it is not equivalent by definition;
where the fixed exponent enters;
known theorem inputs;
failure modes.
```

## Builder

Must output:

```text
full derivation attempt;
all exponent bookkeeping;
all uniformity ranges;
all use of external theorems;
first unproved step.
```

## Verifier

Must output:

```text
strength audit;
hidden zero-strip audit;
PESC-equivalence audit;
triangle leakage audit;
subpower-vs-power audit;
countermodel attempt;
verdict.
```

A candidate is not progress merely because it is novel-looking.

---

# 25. External calibration

The present audit relies on the following external state.

1. K. Matomäki, M. Radziwiłł, T. Tao, *Correlations of the von Mangoldt and higher divisor functions I. Long shift ranges*, Proc. Lond. Math. Soc. 118 (2019), 284–350.  
   Their Theorem 1.3 proves averaged Hardy–Littlewood prime-pair asymptotics for $H\ge X^{8/33+\varepsilon}$ with arbitrary logarithmic savings for almost all shifts, and explicitly distinguishes the absence of power-saving errors for the von Mangoldt case from the divisor-function cases.

2. K. Matomäki, M. Radziwiłł, X. Shao, T. Tao, J. Teräväinen, *Higher uniformity of arithmetic functions in short intervals II. Almost all intervals*, arXiv:2411.05770.  
   Their von Mangoldt uniformity statements provide arbitrary logarithmic decay in the stated short-interval ranges and yield Hardy–Littlewood conclusions with a short average over one variable.

3. A. J. Harper, *Simple Barban–Davenport–Halberstam type asymptotics for general sequences*, J. Lond. Math. Soc. (2025).  
   This supplies current AP-variance calibration.

4. F. Broucke, *On the connection between zero-free regions and the error term in the prime number theorem*, Analysis Mathematica (2026).  
   This supplies current zero-free-region/PNT-remainder calibration.

None proves PESC with a fixed power.

---

# 26. State transition

The canonical transition is:

```text
CSM_RH v1.6
  ->
CSM_RH v1.7
```

with:

```text
Campaign 15
  CLOSED_AS_DIRECT_CURRENT_TECHNOLOGY_AUDIT

O-RH-035
  AVERAGED_HARDY_LITTLEWOOD_FIXED_POWER_PRECISION_FLOOR
  CREATED / CERTIFIED AS CURRENT-THEOREM AUDIT

O-RH-036
  BDH_Q1_CONSTANT_KERNEL_ISOLATION
  CREATED / CERTIFIED

O-RH-037
  CURRENT_ARITHMETIC_SHELL_EXHAUSTION
  CREATED / CERTIFIED RELATIVE TO AUDITED ROUTES

F-RH-015
  PASAHL
  RECORDED AS INTERFACE-EQUIVALENT
  NOT PROMOTED AS A LOWER-STRENGTH FRONTIER

F-RH-010
  PESC
  REMAINS OPEN / CANONICAL

Campaign 16
  DIRECT_PESC_THEOREM_GENERATION
  READY
```

---

# 27. Final status

```text
RH = OPEN

PESC = OPEN

AVERAGE PRIME-PAIR COVERAGE = STRONG

AVERAGE PRIME-PAIR FIXED POWER = NOT AVAILABLE

CURRENT DIRECT PNT CONTROL = STRONG SUBPOWER

BDH NONTRIVIAL MODULI = WRONG EXACT SHIFT KERNEL

SELBERG INTEGRAL = USEFUL QUADRATIC TOOL / NO LOWER-STRENGTH BRIDGE FOUND

AUDITED ARITHMETIC SHELLS = EXHAUSTED RELATIVE TO CURRENT ROUTES

NEXT MODE = DIRECT THEOREM GENERATION
```

At the present closure state, the research target should no longer move.

The unresolved statement is the arithmetic theorem itself:

$$
\boxed{
\left|
\sum_{h=1}^{2N-2}
\sum_{m<2N-h}
w_N(m+h)
\bigl(
\log m\,\mathbf1_{\mathbb P}(m)-1
\bigr)
\bigl(
\log(m+h)\,\mathbf1_{\mathbb P}(m+h)-1
\bigr)
\right|
\ll
N^{3-\kappa+o(1)}
}
$$

for one fixed

$$
0<\kappa<\frac12.
$$

Future CSM_RH work should generate and test actual proof lemmas for this statement rather than further repackage it.
