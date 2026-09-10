# CSM_RH Paper 74

## Ordinary-Prime Pair-Error Exponent Wall and Campaign 46 Structural Closure

**Project:** CSM_RH  
**Paper:** 74  
**Version:** v0.1  
**Date:** 2026-09-09  
**Campaign:** 46 — `SEEDED_ARITHMETIC_STRIP_GAP_GENERATION`  
**Track:** PAIR5D — `NEW_ORDINARY_PRIME_ARITHMETIC_CENTRAL_UPPER`  
**Status:** STANDARD ORDINARY-PRIME CANDIDATES AUDITED / RH-EQUIVALENT ARITHMETIC WALL REACHED / ROOT THEOREM OPEN  
**Canonical entry state:** v1.64 / Paper 73 v0.1  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 73 proved that the maximal fixed-power saving exponent in the smoothed $q=1$ central prime-error energy is exactly

$$
2(1-\beta_*),
$$

the maximal PESC exponent.

Thus any fixed-power improvement of the central principal sector beyond a seed PESC $(\kappa)$ is already a strict zero-strip improvement.

The present paper asks whether a known ordinary-prime inequality can nevertheless supply such an improvement directly, without first passing through zero-free-region information.

The audit finds no standard mechanism which does so.

A decisive independent calibration is supplied by Chou, Haag, Huryn and Ledoan's 2026 work on the total Hardy–Littlewood prime-pair error. They define

$$
\boxed{
E_{\rm pp}(N)
=
\sum_{1\le |k|\le N}
\left(
\psi_2(N,k)
-
(N-|k|)\mathfrak S(k)
\right)^2,
}
$$

where

$$
\psi_2(N,k)
=
\sum_{\substack{n,n'\le N\\n'-n=k}}
\Lambda(n)\Lambda(n').
$$

Let

$$
\Theta
=
\sup_{\zeta(\rho)=0}
\Re\rho.
$$

They prove, for every fixed $\varepsilon>0$,

$$
\boxed{
E_{\rm pp}(N)
=
\Omega
\left(
N^{1+2\Theta-\varepsilon}
\right).
}
$$

Consequently, any all-large- $N$ upper bound

$$
\boxed{
E_{\rm pp}(N)
\ll
N^{3-s+o(1)}
}
$$

forces

$$
\boxed{
\Theta
\le
1-\frac{s}{2}.
}
$$

Indeed,

$$
1+2\Theta
\le
3-s.
$$

Thus the saving exponent $s$ in this genuinely ordinary-prime pair-error norm has the same horizontal zero-strip conversion law as PESC and as the central energy of Paper 73.

If a PESC seed is saturated by a rightmost zero with

$$
\Theta
=
1-\frac{\kappa}{2},
$$

then

$$
\boxed{
E_{\rm pp}(N)
=
\Omega
\left(
N^{3-\kappa-\varepsilon}
\right).
}
$$

Hence any ordinary-prime pair-error theorem with a fixed excess

$$
E_{\rm pp}(N)
\ll
N^{3-\kappa-\eta}
$$

would itself exclude the seed boundary.

Chou et al. conjecture the much smaller scale

$$
E_{\rm pp}(N)
\asymp
N^2(\log N)^2,
$$

and prove that their conjecture implies RH. They also obtain, assuming GRH for Dirichlet $L$ -functions, only an upper bound of order

$$
\boxed{
N^{5/2}
(\log N)^{O(1)},
}
$$

still larger than the conjectural prime-pair-error scale by a factor $N^{1/2}$.

This is a particularly useful calibration: even a broad family-GRH assumption does not automatically give the conjectural ordinary prime-pair error norm.

The standard arithmetic candidates are then audited.

### Selberg / GPY / Maynard positive weights

These methods exploit nonnegative sieve weights and local divisor structure to obtain one-sided estimates, existence theorems and bounded-gap information.

They do not provide a sign-sensitive fixed-power estimate for the Hardy–Littlewood pair residual at the $q=1$ central frequency.

At the scale relevant here, a generic upper-bound sieve leaves errors of main-term size and therefore cannot supply a residual exponent

$$
\xi>\kappa
$$

without a genuinely new cancellation theorem.

### Dispersion and Kloosterman methods

Dispersion can produce true power-saving errors when an additional dense or divisor-like structure is present.

For example, power-saving Titchmarsh-divisor estimates are obtained by combining primes with divisor coefficients and deep Kloosterman-sum bounds.

This mechanism does not transfer formally to the prime–prime central error, where both sides are sparse and the root $q=1$ boundary mode remains.

### Modulus-family averaging

Modern family averaging can produce genuine power cancellation.

In 2026, Parry proved power-saving sign cancellation in a cubic average of prime errors in arithmetic progressions when the modulus range $Q$ is close to $x$.

This demonstrates that current dispersion technology is not intrinsically limited to logarithmic savings.

However, its gain comes from averaging over a large modulus family and therefore does not act on the fixed $q=1$ central sector identified in Papers 72–73.

### Pair-correlation / variance methods

Goldston–Montgomery and later Selberg-class generalizations establish deep correspondences between short-interval variance and zero-pair statistics.

But Paper 73 proves that, without horizontal removal of the rightmost zero, the central diagonal fixes the exponent.

Vertical pair decorrelation cannot supply a persistent fixed-power deficit beyond the seed.

The conclusion is therefore not that no proof of RH can use Selberg, sieve, dispersion, or prime-pair ideas.

The conclusion is narrower and rigorous:

```text
within the Campaign-46 seeded architecture,
all identifiable standard mechanisms have been reduced
to a central ordinary-prime inequality whose fixed-power gain
is itself strict zero-strip progress.
```

There is no remaining "free structural amplifier."

The open root statements remain:

```text
F-RH-017-v3
direct supercritical short-interval exceptional set;

F-RH-022
fixed-power aggregate Hardy–Littlewood pair residual;

PAIR5D
new ordinary-prime q=1 central upper.
```

But these are now different formulations of the genuinely missing arithmetic input, not unexplored representation changes.

Campaign 46 is therefore structurally closed at an RH-equivalent arithmetic wall.

No RH theorem is claimed.

---

# 1. Independent ordinary-prime pair-error norm

Define

$$
\boxed{
\psi_2(N,k)
=
\sum_{\substack{n,n'\le N\\n'-n=k}}
\Lambda(n)\Lambda(n').
}
$$

For $k\ne0$, Hardy–Littlewood predicts

$$
\psi_2(N,k)
\sim
(N-|k|)
\mathfrak S(k).
$$

Define the total squared error

$$
\boxed{
E_{\rm pp}(N)
=
\sum_{1\le |k|\le N}
\left(
\psi_2(N,k)
-
(N-|k|)
\mathfrak S(k)
\right)^2.
}
$$

This is a purely ordinary-prime observable.

No zeta zeros appear in its definition.

---

# 2. 2026 lower bound in terms of the rightmost zero

Let

$$
\boxed{
\Theta
=
\sup_{\zeta(\rho)=0}
\Re\rho.
}
$$

Chou, Haag, Huryn and Ledoan prove:

## Theorem 2.1 — Prime-pair-error lower exponent

For every fixed $\varepsilon>0$,

$$
\boxed{
E_{\rm pp}(N)
=
\Omega
\left(
N^{1+2\Theta-\varepsilon}
\right).
}
$$

They also prove an unconditional lower bound

$$
E_{\rm pp}(N)
=
\Omega
\left(
N^2
(\log\log\log N)^2
\right).
$$

The rightmost-zero lower bound is stronger if RH is false.

Record:

```text
B-RH-113
GLOBAL_ORDINARY_PRIME_PAIR_ERROR_HAS_RIGHTMOST_ZERO_LOWER_EXPONENT
CERTIFIED_EXTERNAL_THEOREM
```

---

# 3. Prime-pair-error power upper implies a zero strip

Assume for some fixed $s>0$

$$
\boxed{
E_{\rm pp}(N)
\ll
N^{3-s+o(1)}
}
$$

for all sufficiently large $N$.

If

$$
\Theta>1-\frac{s}{2},
$$

choose $\varepsilon>0$ small enough that

$$
1+2\Theta-\varepsilon
>
3-s.
$$

Theorem 2.1 then contradicts the upper bound along its $\Omega$ sequence.

Therefore:

## Theorem 3.1 — Ordinary prime-pair-error inverse strip theorem

$$
\boxed{
E_{\rm pp}(N)
\ll
N^{3-s+o(1)}
\quad\Longrightarrow\quad
\Theta
\le
1-\frac{s}{2}.
}
$$

Record:

```text
B-RH-114
FIXED_POWER_GLOBAL_PRIME_PAIR_ERROR_UPPER_FORCES_MATCHING_ZERO_FREE_STRIP
CERTIFIED_FROM_EXTERNAL_THEOREM
```

This is a one-way implication. No converse at this strength is claimed.

---

# 4. Seed-critical pair-error scale

Suppose PESC $(\kappa)$ is saturated:

$$
\boxed{
\Theta
=
1-\frac{\kappa}{2}.
}
$$

Then Theorem 2.1 gives

$$
\boxed{
E_{\rm pp}(N)
=
\Omega
\left(
N^{3-\kappa-\varepsilon}
\right).
}
$$

Thus any upper bound

$$
E_{\rm pp}(N)
\ll
N^{3-\kappa-\eta}
$$

with fixed $\eta>0$ rules out the boundary.

Create:

```text
O-RH-167
GLOBAL_PRIME_PAIR_ERROR_CANNOT_HAVE_FIXED_SAVING_BEYOND_A_SATURATED_PESC_BOUNDARY
CERTIFIED
```

This is the all-shift arithmetic analogue of Paper 73's central-energy wall.

---

# 5. Endpoint calibration

The Prime Pair Error Conjecture of Chou et al. is

$$
\boxed{
E_{\rm pp}(N)
\sim
c_3
N^2
(\log N)^2.
}
$$

At power resolution this is

$$
s=1.
$$

Theorem 3.1 then gives

$$
\boxed{
\Theta\le\frac12,
}
$$

which is RH.

Thus the conjecture implies RH.

The converse is not known and should not be assumed.

Indeed, the same authors obtain under GRH for Dirichlet $L$ -functions only

$$
\boxed{
E_{\rm pp}(N)
\ll
N^{5/2}
(\log N)^{c_4},
}
$$

corresponding to the weaker power saving

$$
s=\frac12.
$$

This demonstrates that the prime-pair-error conjecture contains arithmetic information beyond a routine application of GRH.

---

# 6. Comparison with the PAIR5 central exponent identity

Paper 73 proved for the smoothed $q=1$ central energy

$$
\boxed{
s_{\rm central}^*
=
2(1-\Theta).
}
$$

Theorem 3.1 now provides an independent arithmetic statement:

a global prime-pair-error upper with saving exponent $s$ cannot exceed

$$
2(1-\Theta)
$$

without moving the rightmost zero left.

The two quantities are different norms and no equality between them is asserted.

Their common feature is the horizontal exponent law

$$
\boxed{
s
\mapsto
1-\frac{s}{2}.
}
$$

Thus both the spectral central sector and a purely arithmetic prime-pair error norm detect the same rightmost-zero barrier.

---

# 7. Selberg upper-bound sieve audit

A Selberg upper-bound sieve can majorize prime-pair counts at the natural Hardy–Littlewood scale.

Such an estimate is typically one-sided and of main-term magnitude.

The CSM_RH amplifier requires instead a **signed residual theorem**:

$$
\boxed{
|\mathcal R_{\rm HL}^{(2)}(N,H)|
\ll
NH^2
N^{-\kappa-\eta}.
}
$$

A nonnegative majorant alone does not supply cancellation between positive and negative pair errors.

Likewise, GPY and Maynard weights turn suitable prime correlations into positive quadratic forms in order to prove small gaps and multiplicity results.

That positivity is valuable for existence questions but does not directly estimate the signed $q=1$ pair-error residual below the seed-critical scale.

Record as a method audit:

```text
O-RH-168
POSITIVE_SELBerg_GPY_MAYNARD_WEIGHTS_DO_NOT_BY_THEMSELVES_SUPPLY_SIGNED_FIXED_POWER_Q1_PAIR_RESIDUAL_CANCELLATION
CERTIFIED_AS_METHOD_SCOPE
```

This does not rule out a future new sieve identity with additional information.

---

# 8. Dispersion audit

The dispersion method can turn arithmetic averaging into true power savings.

A representative example is the Titchmarsh divisor problem

$$
\sum_{p\le x}\tau(p-1),
$$

where the divisor function supplies an additional dense multiplicative structure.

Deep Kloosterman-sum estimates can then yield power-saving error terms.

This is structurally different from the prime-pair correlation

$$
\sum_n
\Lambda(n)\Lambda(n+r),
$$

where both sequences are sparse prime-supported objects.

The second prime factor is exactly the unresolved source of parity / pair-error cancellation.

Thus known dispersion power savings do not give PAIR5D for free.

---

# 9. 2026 modulus-family power cancellation

Parry's 2026 work considers prime errors in arithmetic progressions

$$
E_x(q,a)
=
\sum_{\substack{p\le x\\p\equiv a\pmod q}}
\log p
-
\frac{x}{\phi(q)}
$$

and a cubic average over $q$ and $a$.

For $Q$ close to $x$, he proves power-saving sign cancellation beyond the naive square-root expectation.

This is important calibration:

```text
modern prime dispersion can produce genuine powers.
```

But the gain is obtained from averaging over a large modulus family.

The PAIR5D obstruction sits at the single principal channel

$$
q=1.
$$

There is no family-size dilution there.

Therefore Parry's theorem supports, rather than contradicts, the Campaign-46 localization:

high-family-dimension arithmetic can be power-saving while the central single-channel problem remains root-critical.

---

# 10. Prime-pair variance / pair-correlation equivalence audit

Goldston–Montgomery connect prime variance in short intervals to pair correlation of zeta zeros.

Bui, Keating and Smith extend analogous equivalences to arithmetic functions associated with $L$ -functions in the Selberg class.

These correspondences show that variance problems naturally encode zero statistics.

Paper 73 adds the stronger local conclusion needed here:

at the $q=1$ central fixed-power scale, removing vertical off-diagonal interactions still leaves the rightmost diagonal.

Thus pair-correlation technology may explain the expected **shape** of the variance after RH-level horizontal information is available, but it does not provide a free mechanism for eliminating a rightmost off-critical zero.

---

# 11. PAIR5D verdict

The question was:

```text
Does a standard ordinary-prime identity or inequality
give a q=1 fixed-power central upper
without already constituting zero-strip progress?
```

The audit answer is:

```text
NO SUCH STANDARD MECHANISM IS CURRENTLY IDENTIFIED.
```

More precisely:

- Selberg/GPY/Maynard positivity gives no signed residual power;
- high-modulus large sieve and dispersion do not act on $q=1$ ;
- prime × divisor dispersion has an extra structured factor absent in prime × prime;
- zero-pair decorrelation cannot remove the rightmost diagonal;
- the central energy itself is exponent-equivalent to the zero strip;
- an independent ordinary prime-pair-error norm has a rightmost-zero lower exponent.

Therefore any successful PAIR5D theorem is genuine root progress.

This is a research-status statement, not an impossibility theorem.

---

# 12. Campaign 46 closure theorem

Campaign 46 began with a seed PESC exponent and asked whether known arithmetic structure could generate a strict exponent improvement.

Across Papers 54–74 the following routes were audited:

1. deterministic seeded lag amplification;
2. shrinking-threshold exceptional sets;
3. Turán–Gallagher single-zero detection;
4. Euler-product positivity;
5. higher logarithmic derivatives;
6. Heath–Brown component and joint covariance routes;
7. $L^p$ residue-chain optimization;
8. local von Mangoldt increment caps;
9. MRSTT short-interval Type-II machinery;
10. long-scale comparison and anchor methods;
11. Selberg symmetry;
12. positive integer-lattice pseudo-primes;
13. Beurling-prime calibration;
14. additive Dirichlet-character decomposition;
15. high-conductor large-sieve averaging;
16. low-conductor local-factor renormalization;
17. shifted-prime Möbius parity energy;
18. aggregate Hardy–Littlewood pair residual;
19. $q=1$ zero-pair Gram cancellation;
20. standard ordinary-prime sieve / dispersion candidates.

The campaign has reduced all surviving root routes to a fixed-power arithmetic theorem which, by an exact or one-way inverse theorem, already improves the zero strip.

Hence:

## Campaign-46 Structural Closure

```text
CLOSED_AT_RH_EQUIVALENT_ARITHMETIC_WALL
```

This means:

```text
the structural search is complete enough
that another representation change is not justified
without a genuinely new arithmetic input.
```

It does **not** mean RH is proved or that no proof exists.

---

# 13. Open canonical frontiers after closure

The following statements remain open.

## F-RH-017-v3

Direct supercritical short-interval exceptional set:

$$
\#\left\{
x:
|U_H(x)|>HN^{-\nu}
\right\}
\ll
N^{1-c}
$$

with

$$
\nu>\frac{\kappa}{2},
\qquad
c>
\min
\left(
\tau,\frac{\kappa}{2}
\right).
$$

## F-RH-022

Aggregate Hardy–Littlewood pair residual:

$$
\boxed{
|\mathcal R_{\rm HL}^{(2)}(N,H)|
\ll
NH^2N^{-\kappa-\eta}.
}
$$

## PAIR5D

A genuinely new ordinary-prime $q=1$ arithmetic upper theorem which implies either F-RH-022 or a strict central-energy exponent improvement.

These are not three independent structural mysteries.

They are three root-level manifestations of the same missing fixed-power arithmetic excess.

---

# 14. State transition

Advance candidate state

$$
v1.64
\to
v1.65.
$$

Add:

```text
B-RH-113
GLOBAL_ORDINARY_PRIME_PAIR_ERROR_HAS_RIGHTMOST_ZERO_LOWER_EXPONENT
CERTIFIED_EXTERNAL_THEOREM

B-RH-114
FIXED_POWER_GLOBAL_PRIME_PAIR_ERROR_UPPER_FORCES_MATCHING_ZERO_FREE_STRIP
CERTIFIED_FROM_EXTERNAL_THEOREM

O-RH-167
GLOBAL_PRIME_PAIR_ERROR_CANNOT_HAVE_FIXED_SAVING_BEYOND_A_SATURATED_PESC_BOUNDARY
CERTIFIED

O-RH-168
POSITIVE_SELBerg_GPY_MAYNARD_WEIGHTS_DO_NOT_BY_THEMSELVES_SUPPLY_SIGNED_FIXED_POWER_Q1_PAIR_RESIDUAL_CANCELLATION
CERTIFIED_AS_METHOD_SCOPE
```

Campaign status:

```text
CAMPAIGN_46
CLOSED_AT_RH_EQUIVALENT_ARITHMETIC_WALL
```

No root frontier is closed.

No RH certificate is created.

---

# 15. Recommended next phase

If research continues, the next phase should **not** begin by choosing another transform.

It should begin by positing or discovering one genuinely new ordinary-prime inequality and immediately testing it against the three canonical counter-calibrations:

1. boundary zero mode;
2. integer-lattice pseudo-prime model;
3. Beurling-prime model.

A useful next campaign could be:

```text
Campaign 47
ORDINARY_PRIME_BOUNDARY_BREAKING
```

with a single entry rule:

```text
Every proposed mechanism must produce
an explicit fixed-power q=1 arithmetic inequality
before any new representation is developed.
```

That would prevent the research from reopening already exhausted structural loops.

---

# 16. External calibration

## 16.1. Chou–Haag–Huryn–Ledoan, 2026

*The error term in counting prime pairs*, Journal of Number Theory 278 (2026), 422–450.

They define the global squared Hardy–Littlewood pair error, prove

$$
E_{\rm pp}(N)
=
\Omega(N^{1+2\Theta-\varepsilon}),
$$

show their Prime Pair Error Conjecture implies RH, and obtain under GRH for Dirichlet $L$ -functions an upper bound of order $N^{5/2}$ times logarithms.

URL:

https://arxiv.org/abs/2308.14888

## 16.2. Parry, 2026

*Primes in arithmetic progressions on average I*, Bulletin of the London Mathematical Society 58 (2026).

Parry proves power-saving sign cancellation in a cubic average of prime progression errors when $Q$ is close to $x$.

This is used as calibration that family dispersion can produce true power savings.

## 16.3. Drappeau

*Sums of Kloosterman sums in arithmetic progressions, and the error term in the dispersion method*, Proceedings of the London Mathematical Society 114 (2017), 684–732.

Power-saving errors are obtained in Titchmarsh-divisor type problems using additional divisor structure and Kloosterman estimates.

## 16.4. Bui–Keating–Smith

*On the variance of sums of arithmetic functions over primes in short intervals and pair correlation for L-functions in the Selberg class*, Journal of the London Mathematical Society 94 (2016), 161–185.

They establish variance / zero-pair-correlation equivalences extending Goldston–Montgomery.

---

# 17. Conclusion

The PAIR5D search did not reveal a final hidden standard inequality.

Instead, a 2026 ordinary-prime theorem independently confirms the same exponent geometry already found spectrally in Paper 73.

Prime-pair error norms themselves know the rightmost zero.

A fixed-power ordinary-prime improvement beyond a saturated PESC seed is therefore not a technical corollary waiting to be extracted from standard sieve or dispersion machinery.

It is the missing root theorem.

Campaign 46 has reached that wall cleanly.

RH remains open.
