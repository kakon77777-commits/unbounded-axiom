# Formal Kneser Research Kernel

This package separates three levels that must not be conflated:

1. **Kernel-checked finite theorems** in Lean 4;
2. **A Coq/Rocq port** of the same finite checker;
3. **Open mathematical obligations** required for the full $s=3,k=3$ theorem
   and for any generalization in $s$.

## Lean 4 status

`FormalKneser/FiniteKernel.lean` is compiled with Lean $4.28.0$ and proves by
finite reflection:

- the exact list of $3$-stable triples on the $9$-cycle;
- their pairwise disjointness;
- the absence of a $2$-colouring of this $K_3$ base graph;
- the exact vertex count $10$ for the $10$-cycle;
- that every intersecting subfamily of the $10$-cycle finite core is a star;
- the absence of a $3$-colouring of that finite graph.

Run a standard build with:

```bash
lake build
```

All named finite theorems use kernel reduction through `decide` or
`decide +kernel`.  The accompanying
`FormalKneser/AxiomAudit.lean` reports no dependent axioms for them, and the
module has also been re-checked with `leanchecker --fresh` in this research
environment.  This is a formal verification of the concrete finite models;
it is not yet a formalization of the asymptotic capacity lemma, the
classification theorem for maximal intersecting $3$-families, or star peeling.

## Coq/Rocq status

`Coq/KneserFiniteKernel.v` is a standard-library port of the same finite
checker.  It is designed to be checked with:

```bash
coqc KneserFiniteKernel.v
```

The present workspace has no Coq/Rocq executable, so this source is a
cross-system proof script awaiting compiler verification, not a completed Coq
certificate.

## Research scripts

- `research/explore_stable_k3_capacity.py` exactly enumerates maximal
  intersecting families for selected finite $(s,n)$ systems.
- `research/search_rotation_invariant_dual.py` reconstructs the rotation-
  invariant linear-program dual certificates used by the existing $s=3$ finite
  core and searches corresponding certificates for larger $s$.

Read `FORMALIZATION_AND_ADVANCE_v0.1.md` for the status boundary, the new
capacity pattern, and the next formalization targets.
