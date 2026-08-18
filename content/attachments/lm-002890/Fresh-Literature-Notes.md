# SDPE Paper 03 — Fresh Literature Notes

**Date searched:** 2026-08-14  
**Scope:** cover completeness, local-to-global composition, proof-carrying coverage, gluing  
**Rule:** technical grounding uses primary papers/preprints; none is treated as proving SDPE as a whole.

## 1. Stefan Szeider — LRAT-Catcher

**Primary source:** *LRAT-Catcher: Importing SAT Solver Certificates into Lean4 by Reflection*, arXiv:2607.00815v1, 2026-07-01.

The cube-and-conquer workflow requires two independently checked ingredients: every cube leaf is UNSAT, and the cubes cover every assignment. Cover completeness is itself reduced to an UNSAT problem and certified by LRAT before Lean composes the global theorem.

**SDPE use:** strongest current concrete analogue of

$$
\text{local refutations}
+
\text{cover completeness}
\Rightarrow
\text{global refutation}.
$$

## 2. Joshua Gibson — sheaf-based local-to-global consistency

**Primary source:** *Sheaves as a Means of Maintaining Consistency in Model-based Systems Engineering*, arXiv:2605.08609v1, 2026-05-09.

The paper gives a Lean-verified sheaf setting in which compatible local designs on pairwise overlaps glue uniquely to a global design.

**SDPE use:** contemporary formal context for ConstructiveGluing mode.

**Boundary:** this does not imply arbitrary proof atlases satisfy a sheaf law. Paper 03 therefore requires a proved gluing theorem before pairwise overlap checks can be promoted to global consistency.

## 3. Andreas Florath — proof-carrying covering-code certificates

**Primary source:** *Formal Foundations and Proof-Carrying Certificates for q-ary Covering Codes in Lean 4*, arXiv:2606.09600v1, 2026-06-08.

The paper organizes covering-code bounds as replayable Lean certificate predicates and a proof-carrying database.

**SDPE use:** supports the principle that coverage claims should be replayable proof artifacts, not dashboard percentages.

## 4. Andreas Florath — Lean-certified exact cover result

**Primary source:** *A Lean-Certified Proof of $K_8(4,2)=23$*, arXiv:2606.16688v1, 2026-06-15.

The proof combines explicit cover witnesses, fiber-counting reductions, projected graph structure, and Lean-checked LRAT refutations in a proof-carrying artifact.

**SDPE use:** context for representation bridges plus heterogeneous local certificates inside one global proof.

## 5. Historical large-certificate context

**Primary source:** Heule, Kullmann, Marek, *Solving and Verifying the Boolean Pythagorean Triples Problem via Cube-and-Conquer*, arXiv:1605.00723, 2016.

Use: historical context for splitting a vast search space while retaining independently checkable proof artifacts.

## 6. Fresh-search conclusion

The new contribution claimed by Paper 03 is not cover certificates or sheaf gluing themselves. It is the common SDPE closure contract:

$$
\boxed{
\text{Master Envelope}
+
\text{Route Atlas}
+
\text{Typed Gaps}
+
\text{Cover Certificate}
+
\text{Mode-Dependent Glue Certificate}
\to
\text{Global Closure Certificate}.
}
$$

The key distinction is

$$
\boxed{
\text{Refutation Closure}
\neq
\text{Constructive Gluing}.
}
$$
