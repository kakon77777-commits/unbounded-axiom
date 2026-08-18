# CCM Benchmarks 01--13 — Theory Extraction Map

Version: v1.0

This document records what each benchmark contributes to the foundational theory. The benchmarks are evidence and calibration artifacts; they are not definitions of CCM.

| Benchmark | Mathematical ecology | Primary methodological contribution |
|---|---|---|
| 01 Mantel | Extremal graph theory | Finite evidence to structural compression to global lift |
| 02 Frobenius | Numerical semigroups | Exact symbolic reconstruction, residue thresholds, state model |
| 03 Zeckendorf | Recurrence / greedy | Recursive partition, algorithm extraction, mutation test |
| 04 Ramsey | SAT / combinatorics | Falsification-as-constraint, robustness, impossibility mode |
| 05 Cayley--Hamilton | Matrix algebra | Symbolic recurrence, theorem-to-runtime, universal/minimal certificate |
| 06 Primal--Dual LP | Optimization | Cross-representation coupling, gap certificate, certificate hierarchy |
| 07 Farkas | Convex cones | Positive certificate of nonexistence, positive/negative certificate typing |
| 08 Jensen | Nonlinear convexity | Defect decomposition, sign domain, equality manifold |
| 09 SOS / Motzkin | Polynomial nonnegativity | Coverage versus truth, method-barrier certificate, route switching |
| 10 Composite Routing | Mixed polynomial targets | PROVED/DISPROVED/UNRESOLVED semantics, feature routing |
| 11 Certificate Expansion | Fixed target set | Library coverage monotonicity, marginal coverage, conservative extension |
| 12 Cost-Aware Routing | Overlapping certificates | Vector cost, route regret, representation cost |
| 13 Online Routing | Nonstationary stream | Dynamic state, drift, dynamic regret, switch latency |

## Phase I — Certificate Ecology Calibration

Benchmarks 01--09 establish that the upper-level CCM architecture is not tied to one proof ecology.

The recurring structure is:

$$
\boxed{
\text{controlled representation}
\rightarrow
\text{compression / coupling / separation / decomposition}
\rightarrow
\text{proof-bearing certificate}
\rightarrow
\text{general lift}.
}
$$

The domain-specific proof-bearing objects change.

The control architecture persists.

## Phase II — Composite Routing

Benchmarks 10--13 move the research target from individual certificate languages to the policy that selects them.

The progression is:

$$
\text{B10: feature-aware routing},
$$

$$
\text{B11: library expansion},
$$

$$
\text{B12: cost-aware routing},
$$

$$
\text{B13: online adaptive routing}.
$$

## Theory Elements Supported by More Than One Benchmark

### Defect decomposition

Observed independently in:

$$
\text{LP duality},
\qquad
\text{Jensen / variance},
\qquad
\text{SOS}.
$$

### Positive certificates for negative conclusions

Observed in:

$$
\text{SAT / UNSAT},
\qquad
\text{Farkas separation}.
$$

### Representation routing

Observed in:

$$
\text{primal / dual},
\qquad
\text{cone membership / separator},
\qquad
\text{quartic / lifted quadratic}.
$$

### Barrier preservation

Observed in:

$$
\text{failed Ramsey deletion hypothesis},
\qquad
\text{Motzkin non-SOS obstruction}.
$$

### Cost-aware overlap

Observed explicitly in Benchmarks 12--13.

## Benchmark Claim Boundary

The benchmark program supports the existence and reproducibility of the CCM workflow skeleton.

It does not establish universal superiority, completeness, or convergence of unresolved space to zero.

The foundational theory therefore treats empirical gains as benchmark-scoped measurements and keeps general theorems limited to structural statements that follow from definitions.
