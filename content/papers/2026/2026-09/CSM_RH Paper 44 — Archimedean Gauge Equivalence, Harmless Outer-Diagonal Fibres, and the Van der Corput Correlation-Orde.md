# CSM_RH Paper 44
## Archimedean Gauge Equivalence, Harmless Outer-Diagonal Fibres, and the Van der Corput Correlation-Order Barrier

**Project:** CSM_RH  
**Paper:** 44  
**Version:** 0.1  
**Date:** 2026-09-07  
**Campaign:** 43 — `WEIGHTED_LIOUVILLE_POLYNOMIAL_PHASE_ATTACK`  
**Track:** WL1 — `PHASE_FIRST_DETERMINANT_FIBRE_DISPERSION`  
**Canonical state transition:** v1.34 to v1.35

---

# 0. Trust boundary

This paper continues directly from CSM_RH Paper 43.

The inherited residual core is

$$
\boxed{
\begin{aligned}
\mathfrak R_{\lambda}(Q,Y)
=
Y
\sum_{h_\star<h\lesssim X^{o(1)}X/Y}
\sum_m
&\frac{\lambda(m)\lambda(m+h)
r_X(m)r_X(m+h)}{m(m+h)}\\
&\times e^{iQ\log(1+h/m)}
\widehat\Phi\!\left(Y\log(1+h/m)\right),
\end{aligned}
}
$$

where

$$
W=X^w,
\qquad
0<w\le\frac{\varepsilon}{1000},
$$

and

$$
h_\star
=
\frac{X}{Q}
X^{\varepsilon/2-61w/100}.
$$

Every residual determinant fibre has total phase variation at least

$$
\frac{Qh}{X}
\ge
X^{\varepsilon/2-61w/100}.
$$

The admission target remains

$$
\boxed{
|\mathfrak R_{\lambda}(Q,Y)|
\ll
X^{-3w/10+o(1)}.
}
$$

Paper 43 left open whether the polynomial phase variation can be converted into the required fixed power by a phase-first determinant-fibre dispersion argument.

This paper audits that possibility without replacing the actual arithmetic weights by generic bounded coefficients.

No claim of RH, no fixed zero-free strip, and no pointwise fixed-power Mertens or Liouville estimate is made.

---

# 1. Exact absorption of the translated phase

Define the completely multiplicative Archimedean-twisted Liouville function

$$
\boxed{
f_Q(n)
=
\lambda(n)n^{iQ}.
}
$$

Because $\lambda$ is real-valued,

$$
\overline{f_Q(m)}f_Q(m+h)
=
\lambda(m)\lambda(m+h)
\left(\frac{m+h}{m}\right)^{iQ}.
$$

Therefore

## Theorem 1.1 — Exact Archimedean twist absorption

The Paper 43 residual core has the exact form

$$
\boxed{
\begin{aligned}
\mathfrak R_{\lambda}(Q,Y)
=
Y
\sum_{h_\star<h\lesssim X^{o(1)}X/Y}
\sum_m
&\frac{r_X(m)r_X(m+h)}{m(m+h)}\\
&\times
\overline{f_Q(m)}f_Q(m+h)
\widehat\Phi\!\left(Y\log(1+h/m)\right).
\end{aligned}
}
$$

### Proof

Use

$$
\overline{f_Q(m)}f_Q(m+h)
=
\lambda(m)\lambda(m+h)
 e^{iQ\log((m+h)/m)}.
$$

Since

$$
\log\frac{m+h}{m}
=
\log\left(1+\frac hm\right),
$$

the identity follows term by term.

 $\square$

Create:

```text
B-RH-019
ARCHIMEDEAN_TWIST_ABSORPTION_OF_TRANSLATED_LIOUVILLE_CORE
status:
  CERTIFIED EXACT IDENTITY
```

The explicit oscillatory phase is therefore not an independent source of randomness.
It is exactly part of the completely multiplicative coefficient $f_Q$.

---

# 2. Determinant-kernel gauge equivalence

The Type-II expansion from Paper 43 uses pairs

$$
x=(u,v),
\qquad
n_x=uv,
$$

and

$$
y=(u',v'),
\qquad
n_y=u'v'.
$$

For a fixed $Q$ and a fixed support restriction, write the phase-free kernel as

$$
K_0(x,y),
$$

where $K_0$ may contain:

1. the determinant incidence condition;
2. the shift-shell cutoff;
3. the denominator;
4. the Gaussian factor;
5. any nonnegative support weight independent of the center phase.

The translated kernel is

$$
\boxed{
K_Q(x,y)
=
K_0(x,y)
 e^{iQ\log(n_y/n_x)}.
}
$$

Define the diagonal unitary operator

$$
\boxed{
(D_Qa)(x)
=
n_x^{iQ}a(x).
}
$$

Then

$$
(D_Q^\ast K_0D_Q)(x,y)
=
n_x^{-iQ}K_0(x,y)n_y^{iQ}.
$$

Hence

## Theorem 2.1 — Global Archimedean gauge equivalence

For every fixed support kernel $K_0$,

$$
\boxed{
K_Q
=
D_Q^\ast K_0D_Q.
}
$$

Consequently $K_Q$ and $K_0$ have exactly the same operator norm and singular values.
If $K_0$ is Hermitian, they also have the same spectrum.

### Proof

The identity follows from

$$
n_x^{-iQ}n_y^{iQ}
=
 e^{iQ\log(n_y/n_x)}.
$$

Unitary conjugation preserves operator norm and singular values, and preserves eigenvalues in the Hermitian case.

 $\square$

This result applies simultaneously across all determinant fibres.
It is not a one-fibre approximation.

The shift support itself can depend on $Q$ through $h_\star$ ; the statement is that once the support is fixed, the center phase contributes no additional generic operator-norm gain.

---

# 3. Exact simultaneous phase-matched resonance

The same fact has a coefficient-level formulation.

Let $A(u)$ and $B(v)$ be arbitrary coefficient sequences and define

$$
A_Q(u)=A(u)u^{iQ},
\qquad
B_Q(v)=B(v)v^{iQ}.
$$

Then on every determinant incidence

$$
u'v'-uv=h,
$$

we have

$$
\begin{aligned}
&A_Q(u)B_Q(v)
\overline{A_Q(u')B_Q(v')}
 e^{iQ\log(u'v'/(uv))}\\
&\qquad=
A(u)B(v)\overline{A(u')B(v')}.
\end{aligned}
$$

Thus one global choice of Archimedean twist neutralizes the translated phase on all fibres simultaneously.

This is the determinant-kernel analogue of the one-frequency generic resonance isolated in Paper 40, but it is stronger in one respect:
it is an exact gauge identity for the specific translated kernel already produced by Papers 42-43.

Create:

```text
O-RH-111
GLOBAL_ARCHIMEDEAN_GAUGE_NEUTRALIZES_PHASE_ONLY_DISPERSION
status:
  CERTIFIED
scope:
  generic coefficient classes stable under unit-modulus Archimedean twisting
```

## Corollary 3.1 — No generic phase-only fixed-power theorem

Suppose a proposed WL1 estimate uses only:

1. the determinant support;
2. coefficient magnitudes or divisor bounds;
3. Hilbert-space or large-sieve geometry of $K_Q$ ;
4. the size of $Qh/X$ ;

and is uniform over a coefficient class stable under multiplication by $n^{it}$.

Then the center phase cannot by itself improve the generic operator bound, because the same estimate is unitarily equivalent to the phase-free kernel.

Any genuine fixed-power gain must use arithmetic information not invariant under forgetting the actual Liouville carrier.

This does not rule out a Liouville-aware phase argument.
It rules out the Campaign 43 rejection-filter R1 route in exact operator form.

---

# 4. The only equal-slope determinant fibres are outer diagonal

Paper 43 parametrized a determinant fibre by

$$
g=(u,u'),
\qquad
u=ga,
\qquad
u'=gb,
\qquad
(a,b)=1,
$$

and

$$
v=v_0+bt,
\qquad
v'=v_0'+at.
$$

The two affine forms have equal slope only if

$$
a=b.
$$

Since

$$
(a,b)=1,
$$

this forces

$$
\boxed{a=b=1.}
$$

Hence

$$
\boxed{u=u'=g.}
$$

Therefore the only identically equal-slope fibre family is the outer-diagonal family $u=u'$.

---

# 5. Outer-diagonal determinant fibres are harmless

On the outer diagonal $u=u'$, the determinant equation becomes

$$
u(v'-v)=h.
$$

Thus

$$
u\mid h,
\qquad
v'-v=\frac hu.
$$

For fixed $h$, the number of admissible $u\sim M$ is at most

$$
h^{o(1)},
$$

and for each such $u$ there are at most

$$
O(N)
$$

admissible $v\sim N$.

Since the grouped fixed- $L$ coefficients are divisor bounded,

$$
|\alpha(u)|,
|\beta(v)|
\le
X^{o(1)}.
$$

Also

$$
uv\asymp u'v'\asymp X,
$$

so the denominator contributes

$$
X^{-2+o(1)}.
$$

The Gaussian restricts the effective total shift range to

$$
h\lesssim X^{o(1)}\frac{X}{Y}.
$$

Therefore the total outer-diagonal contribution is

$$
\begin{aligned}
|\mathfrak R_{u=u'}|
&\ll
Y
\left(X^{o(1)}\frac{X}{Y}\right)
\frac{N}{X^2}
X^{o(1)}\\
&=
\frac{N}{X}X^{o(1)}\\
&=
M^{-1+o(1)}.
\end{aligned}
$$

The pure-Mobius Type-II grouping from Paper 41 gives

$$
M\ge X^{\varepsilon/10}.
$$

Hence

## Theorem 5.1 — Outer-diagonal fibre elimination

$$
\boxed{
|\mathfrak R_{u=u'}|
\ll
X^{-\varepsilon/10+o(1)}.
}
$$

Because

$$
w\le\frac{\varepsilon}{1000},
$$

we have

$$
\frac{\varepsilon}{10}
-
\frac{3w}{10}
\ge
\frac{997\varepsilon}{10000}>0.
$$

Thus

$$
\boxed{
X^{-\varepsilon/10+o(1)}
=o\!\left(X^{-3w/10+o(1)}\right)
}
$$

at the exponent-ledger level.

Create:

```text
B-RH-020
OUTER_DIAGONAL_DETERMINANT_FIBRES_ARE_FIXED_POWER_HARMLESS
status:
  CERTIFIED
```

After removing this contribution, WL1 may assume

$$
\boxed{a\neq b.}
$$

---

# 6. First van der Corput differencing raises the Liouville order

On a non-outer-diagonal fibre define

$$
L_1(t)=v_0+bt,
\qquad
L_2(t)=v_0'+at,
\qquad
a\neq b.
$$

The arithmetic part of the fibre sum has schematic form

$$
A(t)
=
\lambda(L_1(t))
\lambda(L_2(t))
\rho(t),
$$

where $\rho(t)\ge0$ contains the inherited structured multiplicity and smooth weights.

A first van der Corput differencing with nonzero integer shift $r$ introduces

$$
A(t+r)\overline{A(t)}.
$$

Since $\lambda$ is real,

$$
\boxed{
\begin{aligned}
A(t+r)\overline{A(t)}
=
&\lambda(L_1(t+r))
\lambda(L_2(t+r))\\
&\times
\lambda(L_1(t))
\lambda(L_2(t))
\rho(t+r)\rho(t).
\end{aligned}
}
$$

## Theorem 6.1 — Four distinct affine Liouville forms after one differencing

If $a\neq b$ and $r\neq0$, the four affine functions

$$
L_1(t),
\qquad
L_2(t),
\qquad
L_1(t+r),
\qquad
L_2(t+r)
$$

are pairwise non-identical as affine polynomials.

### Proof

The two $L_1$ forms have common slope $b$ but intercepts differing by $br\neq0$.
The two $L_2$ forms have common slope $a$ but intercepts differing by $ar\neq0$.
Any identity between an $L_1$ form and an $L_2$ form would require equality of slopes, hence $a=b$, contrary to the outer-diagonal removal.

 $\square$

Therefore the first standard differencing step transforms a two-form Liouville correlation into a four-form Liouville correlation.

Create:

```text
O-RH-112
FIBRE_VAN_DER_CORPUT_DOUBLES_LIOUVILLE_CORRELATION_ORDER
status:
  CERTIFIED
```

This is an arithmetic-complexity statement, not a claim that van der Corput is universally useless.
A successful use would have to control the resulting four-form object with the structured weights and growing affine coefficients still present.

---

# 7. Repeated differencing does not create a free escape

After $k$ generic differencing steps, the Liouville part is supported on translates

$$
L_j\left(t+\sum_{\ell=1}^{k}\omega_\ell r_\ell\right),
\qquad
j\in\{1,2\},
\qquad
\omega\in\{0,1\}^k.
$$

Before coincidences are identified, the formal correlation order is therefore

$$
\boxed{2^{k+1}.}
$$

The first step already reaches four forms.

The standard two-point logarithmic Chowla theorem does not supply a uniform fixed-dyadic, structured-weight, growing-coefficient four-form estimate of the strength required here.
The odd-order logarithmic results of Tao-Teravainen likewise do not directly close this even four-form object.

No global impossibility theorem for all higher-order methods is claimed.
The certified conclusion is narrower:

```text
standard fibre Weyl/VdC differencing
  does not reduce the Liouville arithmetic complexity;
  its first step increases it from 2 to 4.
```

---

# 8. Pretentious distance saturates at logarithmic scale

The exact twist absorption suggests comparing

$$
f_Q(n)=\lambda(n)n^{iQ}
$$

with the Archimedean character

$$
n^{iQ}.
$$

For $1$ -bounded multiplicative functions define the standard prime-harmonic pretentious distance

$$
\mathbb D(f,g;X)^2
=
\sum_{p\le X}
\frac{1-\operatorname{Re}(f(p)\overline{g(p)})}{p}.
$$

At every prime,

$$
f_Q(p)\overline{p^{iQ}}
=
\lambda(p)
=-1.
$$

Thus

$$
\boxed{
\mathbb D(f_Q,n^{iQ};X)^2
=
2\sum_{p\le X}\frac1p
=
2\log\log X+O(1).
}
$$

This is already maximal at the prime-harmonic scale, since for any two $1$ -bounded multiplicative functions

$$
\mathbb D(f,g;X)^2
\le
2\sum_{p\le X}\frac1p
=
2\log\log X+O(1).
$$

Therefore any mechanism whose entire quantitative gain has the form

$$
\exp\!\left(-c\mathbb D(f,g;X)^2\right)
$$

can yield at most a fixed negative power of $\log X$ from this distance scale:

$$
\exp\!\left(-c\mathbb D^2\right)
\ge
(\log X)^{-2c+o(1)}
$$

at the maximal possible distance.

It cannot by itself yield

$$
X^{-\delta}
$$

for fixed $\delta>0$.

Create:

```text
O-RH-113
PRIME_HARMONIC_PRETENTIOUS_DISTANCE_CANNOT_BY_ITSELF_SUPPLY_FIXED_X_POWER
status:
  CERTIFIED AS MECHANISM-SCOPE BARRIER
```

This does not reject pretentious methods as a whole.
It rejects a specific promotion error: treating prime-harmonic nonpretentiousness alone as a fixed- $X$ -power source.

---

# 9. WL1 audit

Campaign 43 track WL1 asked whether the polynomial lower bound

$$
\frac{Qh}{X}
\ge
X^{\varepsilon/2-61w/100}
$$

could itself be converted into the fixed-power target by phase-first determinant-fibre dispersion.

The audit now gives four exact conclusions.

## WL1-A — explicit phase is an arithmetic twist

$$
\lambda(m)\lambda(m+h)e^{iQ\log((m+h)/m)}
=
\overline{f_Q(m)}f_Q(m+h).
$$

## WL1-B — generic kernel geometry is gauge invariant

$$
K_Q=D_Q^\ast K_0D_Q.
$$

So the center phase alone cannot improve a generic operator norm.

## WL1-C — the only equal-slope fibre family is harmless

$$
u=u'
$$

contributes

$$
\ll X^{-\varepsilon/10+o(1)}.
$$

## WL1-D — standard differencing raises arithmetic order

After one nontrivial differencing step on every remaining fibre, two Liouville forms become four distinct affine Liouville forms.

Therefore WL1 is closed as

```text
CLOSED_AS_ARCHIMEDEAN_GAUGE_AND_EVEN_ORDER_LIOUVILLE_BARRIER
```

with no fixed-power theorem proved.

---

# 10. What remains genuinely live

The negative WL1 verdict does not erase the polynomial phase information from Paper 43.
It changes how that information may legally be used.

The phase can matter only after coupling it to arithmetic structure which is not invariant under generic coefficient twisting.
The next live track is therefore WL2:

```text
LIOUVILLE_AWARE_RAMARE_EXTRACTION
```

The exact identity

$$
f_Q(n)=\lambda(n)n^{iQ}
$$

makes prime extraction natural, because for $p\nmid m$,

$$
f_Q(pm)
=
-f_Q(m)p^{iQ}.
$$

But any Ramaré-type decomposition must preserve:

1. the common-prime structure of $m$ and $m+h$ ;
2. the nonnegative factorisation weights $r_X$ ;
3. the fixed- $X$ -power exponent ledger;
4. the single prescribed dyadic scale.

No success of WL2 is claimed in this paper.

---

# 11. Relation to earlier CSM_RH obstructions

Paper 40 certified that a generic divisor-bounded Type-II class admits explicit one-frequency resonances, so a generic polynomial- $W$ mean-square theorem cannot hold without arithmetic input.

Paper 44 sharpens that observation inside the later translated-window formulation:

$$
\boxed{
\text{translated center phase}
=
\text{diagonal unitary gauge}
}
$$

for every fixed support kernel.

Thus the Paper 40 resonance obstruction and the Paper 44 gauge obstruction are compatible but not identical.

Paper 43's positive result also remains valid:
all residual fibres have polynomial total phase variation.
The new conclusion is that polynomial variation is not, by itself, a generic source of cancellation once arbitrary phase-matched coefficient twists are admitted.

---

# 12. External calibration

The following literature calibrates only the scope of the obstruction statements.

1. A. Granville and K. Soundararajan, *Pretentious multiplicative functions and an inequality for the zeta-function*, arXiv:`math/0608407`. This supplies the standard prime-harmonic pretentious-distance framework.

2. A. Granville, A. J. Harper, and K. Soundararajan, *A new proof of Halasz's theorem, and its consequences*, arXiv:`1706.03749`. This calibrates the role of pretentious distance in multiplicative mean-value estimates.

3. T. Tao, *The logarithmically averaged Chowla and Elliott conjectures for two-point correlations*, arXiv:`1509.05422`. This proves the logarithmically averaged two-point affine Liouville correlation theorem, not the fixed-dyadic fixed- $X$ -power estimate required here.

4. T. Tao and J. Teravainen, *The structure of logarithmically averaged correlations of multiplicative functions, with applications to the Chowla and Elliott conjectures*, arXiv:`1708.02610`. This includes logarithmically averaged odd-order Chowla results; it does not directly provide the even four-form single-scale estimate generated by WL1 differencing.

5. J. Guo, *Quantitative Logarithmic Chowla Correlations Uniformly over Growing Shifts*, arXiv:`2608.23500` (2026). This gives quantitative logarithmically weighted two-point cancellation for a polylogarithmic shift range and explicitly does not prove ordinary Cesaro two-point Chowla.

No cited theorem is claimed to prove or disprove the Paper 44 weighted determinant-fibre target.

---

# 13. State transition

The canonical state advances from v1.34 to v1.35.

New bridges:

```text
B-RH-019
ARCHIMEDEAN_TWIST_ABSORPTION_OF_TRANSLATED_LIOUVILLE_CORE
CERTIFIED

B-RH-020
OUTER_DIAGONAL_DETERMINANT_FIBRES_ARE_FIXED_POWER_HARMLESS
CERTIFIED
```

New obstructions:

```text
O-RH-111
GLOBAL_ARCHIMEDEAN_GAUGE_NEUTRALIZES_PHASE_ONLY_DISPERSION
CERTIFIED

O-RH-112
FIBRE_VAN_DER_CORPUT_DOUBLES_LIOUVILLE_CORRELATION_ORDER
CERTIFIED

O-RH-113
PRIME_HARMONIC_PRETENTIOUS_DISTANCE_CANNOT_BY_ITSELF_SUPPLY_FIXED_X_POWER
CERTIFIED AS MECHANISM-SCOPE BARRIER
```

Campaign 43 remains open.

Track status:

```text
WL1:
  CLOSED_AS_ARCHIMEDEAN_GAUGE_AND_EVEN_ORDER_LIOUVILLE_BARRIER

WL2:
  NEXT

WL3:
  OPEN

WL4:
  OPEN

WL5:
  OPEN
```

The correct continuation point is

$$
\boxed{
\text{Campaign 43 / WL2 — Liouville-aware Ramare extraction.}
}
$$

---

# 14. RH status

This paper does not prove or disprove RH.

```text
RH_PROVED = false
RH_DISPROVED = false
GLOBAL_RH_CERTIFICATE = false
```

The root frontiers remain

```text
F-RH-010  PRIME_ERROR_SELF_CORRELATION (PESC)  OPEN
F-RH-016  MESOSCOPIC_LAG_ENERGY_POWER_GAIN (MLEPG)  OPEN
```

The component bridge B-RH-014 remains certified but uninvoked for the pure-Mobius core because the required polynomial- $W$ input has not been obtained.
