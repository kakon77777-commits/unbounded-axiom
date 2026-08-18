# SDPE Paper 08 — Fresh Literature Notes

**Search date:** 2026-08-14  
**Scope:** proof infrastructure, event/state reuse, benchmark fidelity, dependency-rich theorem proving, verifier-grounded agent loops.  
**Rule:** external material is grounding only unless explicitly imported as a classical or formal systems premise.

## 1. AXLE — scalable strict Lean infrastructure

**Primary source:** Jimmy Xin et al., **AXLE: A Cloud Infrastructure for Lean 4 Theorem Proving Utilities**, arXiv:`2606.26442`, 2026.

Relevant points:

- strict Lean proof verification at large request volume;
- proof manipulation and metadata extraction as separate services;
- concurrent support for multiple Lean / Mathlib versions;
- per-request isolation;
- infrastructure is a first-class bottleneck in AI theorem proving.

**Use in SDPE P08:** grounding for version-pinned verifier services, strict verification, isolation, and separating proof search from proof-checking infrastructure.

## 2. Faults in Our Formal Benchmarking — kernel validity is not benchmark fidelity

**Primary source:** Pawan Sasanka Ammanamanchi, Siddharth Bhat, Stella Biderman, **Faults in Our Formal Benchmarking: Dataset Defects and Evaluation Failures in Lean Theorem Proving**, arXiv:`2606.29493`, 2026.

The authors audit five Lean theorem-proving benchmarks with static checkers and report thousands of findings, including mechanically certified issues such as vacuous theorems, counterexamples, and unsound axioms, together with semantic defects such as missing hypotheses or incorrect translations.

**Use in SDPE P08:** establishes a critical runtime distinction:

$$
\boxed{
\text{kernel-checked proof validity}
\neq
\text{problem / benchmark fidelity}.
}
$$

Therefore benchmark statement audit is a separate authority channel from proof checking.

## 3. TheoremBench — dependency-rich and theorem-level evaluation

**Primary source:** QuocViet Pham et al., **TheoremBench: Evaluating LLMs on Theorem Proving in Formal Mathematics**, arXiv:`2606.09450`, 2026.

The benchmark provides both target-only and premise-expanded theorem families and introduces theorem-level coverage and token-efficiency measures.

**Use in SDPE P08:** grounding for benchmark tracks that preserve internal dependency structure instead of scoring only isolated terminal theorem success.

## 4. OpenProver — observable Planner / Worker / Verifier architecture

**Primary source:** Matěj Kripner, Milan Straka, **OpenProver: Agentic and Interactive Theorem Proving with Lean 4**, arXiv:`2607.09217`, 2026.

OpenProver separates Planner, Worker, Repository/Whiteboard state, and formal Verifier, while supporting reproducible automatic evaluation and human steering.

**Use in SDPE P08:** contemporary precedent for an agentic proof runtime in which planning state, persistent findings, and verifier authority are distinct.

## 5. Proof-state snapshotting — state reuse can dominate runtime

**Primary source:** Austin Shen, Yunong Shi, **Keep the Proof State Live: Snapshotting for Efficient Tactic Search in Lean 4**, arXiv:`2605.25556`, 2026.

The work reports substantial wall-time reductions by reusing elaborated proof states rather than reconstructing them for every branch.

**Use in SDPE P08:** grounding for checkpoints / compiled operational state. A snapshot is treated as an accelerator, not as a proof certificate.

## 6. Testing-style semantic evaluation

**Primary source:** Jongyoon Kim, Hojae Han, Seung-won Hwang, **Benchmarking Testing in Automated Theorem Proving**, arXiv:`2604.23698`, 2026.

The paper evaluates generated formal theorems by whether dependent successor theorems continue to compile, revealing a gap between ordinary compilation success and stronger semantic metrics.

**Use in SDPE P08:** supports maintaining downstream dependency / regression tests in addition to local kernel acceptance.

## 7. Literature boundary

No located primary source implements the exact SDPE state tuple

$$
\mathbb S_t
=
\langle
\Omega_t,
RouteCert_t,
\mathbf G_t,
GCC_t,
\mathcal H_t,
Compiled_t,
DVI_t,
SurvProf_t,
RouteDecision_t
\rangle
$$

or the specific certificate-gated survivor-enclosure semantics developed across Papers 01--07.

Paper 08 therefore presents the runtime integration as an internal framework and prototype, not as an attribution claim about existing theorem-proving systems.
