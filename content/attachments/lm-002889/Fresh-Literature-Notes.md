# SDPE Paper 02 — Fresh Literature Notes

**Search date:** 2026-08-14  
**Scope:** route-domain completeness, representation non-collapse, abstraction completeness, strong preservation, refinement  
**Rule:** technical grounding uses primary publication records / author pages / original papers where available.

---

## 1. Cousot & Cousot — Abstract Interpretation

**Primary work:** P. Cousot and R. Cousot, *Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs by Construction or Approximation of Fixpoints*, POPL 1977, DOI `10.1145/512950.512973`.

Relevant grounding:

- concrete / abstract domains;
- Galois-style abstraction / concretization;
- sound over-approximation;
- fixed-point approximation.

**Use in Paper 02:** structural ancestor for the distinction between sound abstraction and exact representation. The elementary powerset Galois connection induced by an arbitrary function $\phi:D\to X$ is proved directly in Paper 02.

---

## 2. Clarke–Grumberg–Long — Model Checking and Abstraction

**Primary work:** *Model Checking and Abstraction*, ACM TOPLAS 16(5), 1512–1542, 1994, DOI `10.1145/186025.186051`.

Relevant grounding:

- reduction of model-checking complexity through abstraction;
- preservation conditions are required before abstract results can be lifted to concrete systems.

**Use in Paper 02:** external grounding for the claim that representation reduction is only useful for proof when the specification semantics is preserved.

---

## 3. Clarke et al. — CEGAR

**Primary work:** E. Clarke, O. Grumberg, S. Jha, Y. Lu, H. Veith, *Counterexample-Guided Abstraction Refinement*, CAV 2000, DOI `10.1007/10722167_15`.

Relevant grounding:

- coarse abstraction may contain spurious behavior;
- a spurious counterexample can trigger refinement;
- soundness does not require full precision at the initial abstraction.

**Use in Paper 02:** supports the Conservative-Envelope Strategy. Mixed fibers need not invalidate a proof route if they are retained/refined rather than falsely excluded.

---

## 4. Giacobazzi–Ranzato–Scozzari — Completeness

**Primary work:** *Making Abstract Interpretations Complete*, Journal of the ACM 47(2), 361–416, 2000, DOI `10.1145/333979.333989`.

Relevant grounding:

- completeness is distinct from soundness;
- abstract domains can lose information even while remaining correct;
- complete extensions / restrictions characterize ways of repairing precision.

**Use in Paper 02:** direct conceptual grounding for separating weak counterexample-completeness from strong proof-language/operator completeness.

---

## 5. Ranzato–Tapparo — Strong Preservation

**Primary work:** *Generalized Strong Preservation by Abstract Interpretation*, Journal of Logic and Computation 17(1), 157–197, 2007; arXiv:`cs/0401016`.

Relevant grounding:

- strong preservation means concrete and abstract models agree on formulas in a specification language;
- strong preservation is characterized through abstract-interpretation completeness;
- minimal refinement can restore strong preservation for the language of interest.

**Use in Paper 02:** motivates proof-relevant language $\Sigma$ and the statement that non-collapse must be relative to the predicates/operators the proof actually uses, not global injectivity.

---

## 6. Giacobazzi–Ranzato — The Best of Abstract Interpretations (2025)

**Primary work:** Proc. ACM Program. Lang. 9 (POPL), Article 46, 2025, DOI `10.1145/3704882`.

Fresh relevance:

- even composing locally best abstract transfer functions does not automatically make the whole abstract interpretation globally best;
- optimal abstraction can be difficult or impossible to obtain uniformly.

**Use in Paper 02:** reinforces a key SDPE warning: a chain of individually plausible representation steps is not automatically globally faithful. Representation composition needs an end-to-end preservation certificate.

---

## 7. Ganty–Manini–Ranzato — Reachability-Guided Abstraction Refinement (2026)

**Primary work:** FM 2026, LNCS 16556, pp. 599–618, DOI `10.1007/978-3-032-26204-2_31`.

Fresh relevance:

- introduces reachability-guided abstraction refinement;
- develops semi-completeness rather than demanding globally expensive full completeness;
- refines abstraction over regions relevant to reachable states.

**Use in Paper 02:** especially close to SDPE's route-domain philosophy. SDPE similarly does not require a representation to preserve everything in $D$; it needs sufficient soundness/completeness on counterexample-relevant regions and proof-relevant operations.

---

## 8. Fresh-search conclusion

The mature literature already contains:

$$
\text{sound abstraction},
\quad
\text{completeness},
\quad
\text{strong preservation},
\quad
\text{refinement},
\quad
\text{region-sensitive semi-completeness}.
$$

Therefore SDPE Paper 02 should not claim novelty for any of those components individually.

The potentially distinctive contribution is the **proof-research route contract** that combines:

$$
\boxed{
\text{counterexample coverage}
+
\text{proof-relevant fiber analysis}
+
\text{fiber-safe exclusion}
+
\text{operator preservation}
+
\text{multi-representation route atlas}
+
\text{versioned replay certificate}.
}
$$

The paper deliberately allows lossy representations as long as loss is explicitly managed and cannot create false exclusions.
