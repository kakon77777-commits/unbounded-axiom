# Research Log

## 2026-07-25

### 1. Handoff

Accepted v0.7 handoff:

- fixed abstract interval certificate succeeds at
  $\alpha=21/20$;
- stored band coefficients match upper profiles;
- fixed witness fails after direct lower-profile substitution.

### 2. Lineage trace

Read v0.1–v0.7 methods and code. Identified that:

- v0.2 intentionally constructs an upper supremum leakage envelope;
- v0.3 dual lower-bounds that artificial envelope objective;
- v0.4–v0.6 preserve the same epigraph semantics;
- v0.7 interval-certifies the abstract operator but temporarily treats
  coefficient legitimacy mainly as a lower-count problem.

### 3. Semantic repair

Separated:

$$
Z_\Gamma,
\qquad
U\sup H,
\qquad
L\inf H.
$$

Built an exact two-point countermodel to the arbitrary-measure transfer and an
exact rank-one common-floor countermodel.

### 4. Robust search

Re-ran lower-profile Galerkin optimization. The first tests at effective
dimensions $62$ and $94$ gave approximately $0.4566$ and $0.2363$, showing
that the previous $\alpha>1$ obstruction was not robust.

Expanded through effective dimension $190$, obtaining

$$
0.1297047862.
$$

### 5. Direct Green transfer

Transferred final atomic measures to the clamped Green RKHS. Three time steps
converged to approximately

$$
0.12970313.
$$

### 6. Primal diagnostic

Reconstructed the minimum generalized direction and audited a
$101\times101$ core grid plus axis step $0.01$. Obtained sampled normalized
objective

$$
0.1297069814.
$$

### 7. Prototype status

Added the Platt–Trudgian verified-height fact. Classified the height-$20.4$
patch as calibration geometry only.

### 8. Decision

Stopped robust-witness search. Defined v0.9 as a location-aware occupancy and
uncertain-operator-family node, with upper-envelope no-go retained as a
separate track.
