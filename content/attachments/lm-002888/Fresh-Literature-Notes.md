# SDPE Paper 01 — Fresh Literature Notes

**Date:** 2026-08-14

## 1. Abstract Interpretation

Cousot & Cousot (POPL 1977) provide the canonical mathematical language for sound abstraction and fixpoint approximation. The relevant connection is the invariant

$$
\text{concrete bad states}
\subseteq
\text{abstract candidate states}.
$$

SDPE should therefore not claim novelty for sound over-approximation itself.

## 2. CEGAR

Clarke et al. (CAV 2000) introduced Counterexample-Guided Abstraction Refinement: begin with a coarse abstraction, inspect counterexamples, refine spurious behavior, and repeat until verification or a real counterexample emerges.

A recent 2025 generalization by König et al. applies CEGAR with abstract interpretation to generalized graph transformation / reactive systems with infinite state spaces.

SDPE differs mainly in intended scope: long-form mathematical research where refinements may be arbitrary theorem-derived necessary conditions rather than only predicates learned from spurious model-checking counterexamples.

## 3. Proof certificates and cover completeness

Szeider's LRAT-Catcher (arXiv:2607.00815, 2026) is particularly relevant because it combines per-cube refutations with a cover-completeness certificate and imports the resulting unsatisfiability result into Lean 4.

This is a concrete existing example of the logical pattern:

$$
\text{local certified exclusions}
+
\text{complete cover certificate}
\Longrightarrow
\text{global theorem}.
$$

## 4. Proof reuse / compilation

Kaufmann & Hofstadler (2025) show that reusable algebraic proof-certificate fragments can reduce proof size and checking time.

Shen & Shi (2026) show that proof-state snapshotting in Lean 4 can avoid repeated state reconstruction and produce large wall-time speedups in tactic search.

These do not prove the SDPE Discovery–Verification Inversion hypothesis, but they establish that verified historical structure can materially reduce repeated proof-search overhead.

## 5. Dependency graphs

TheoremGraph (Kurgan et al., 2026) explicitly models statement-level dependencies across formal and informal mathematics. This supports the feasibility of maintaining fine-grained proof dependency / provenance graphs, but it does not by itself provide survivor-domain semantics.

## 6. Novelty boundary for Paper 01

Do not claim:

- invention of search-space refinement;
- invention of counterexample-guided refinement;
- invention of sound over-approximation;
- invention of proof certificates or dependency graphs.

Potential contribution to test instead:

$$
\boxed{
\text{counterexample survivor enclosure}
+
\text{global coverage / gluing certificate}
+
\text{trace compilation}
+
\text{discovery–verification phase model}
}
$$

as a unified framework for long-horizon mathematical research, including AI-assisted research.
