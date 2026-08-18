# SDPE Paper 04 — Fresh Literature Notes

**Date searched:** 2026-08-14  
**Scope:** proof-state reuse, proof certificate recycling, reusable theorem libraries, lifelong formal proving, strict multi-version verification  
**Rule:** technical grounding uses primary sources; external work is not promoted into an SDPE theorem.

---

## 1. Shen & Shi — Lean proof-state snapshotting

**Primary source:** Austin Shen and Yunong Shi, *Keep the Proof State Live: Snapshotting for Efficient Tactic Search in Lean 4*, arXiv:2605.25556, 2026.

The paper identifies repeated proof-state reconstruction as a large operational bottleneck in portfolio tactic search. It reports that import loading plus theorem-body elaboration account for more than $99\%$ of per-branch wall time in their setting. Their Lean server extension captures an already elaborated proof state and branches directly from it.

Reported benchmark result on 48 miniF2F-v2 problems:

- wall-time speedup: 5.6--50x;
- average: 14x;
- median: 9.7x.

**Use in SDPE Paper 04:** evidence that saving formal state can remove repeated reconstruction cost.

**Boundary:** snapshotting is operational state reuse. It does not by itself constitute a proof certificate or closure certificate.

---

## 2. Kaufmann & Hofstadler — recycling algebraic proof certificates

**Primary source:** Daniela Kaufmann and Clemens Hofstadler, *Recycling Algebraic Proof Certificates*, arXiv:2507.20267, 2025.

The paper extends LPAC with `PatternNew` and `PatternApply` rules. A proof fragment is checked once as a self-contained pattern; later applications verify an admissible mapping from pattern inputs / variables to the current proof state.

The authors report reduced proof steps, proof-file size, memory, and checking time on their circuit-verification benchmarks.

A particularly relevant structural feature is that after a pattern is verified, its internal proof steps need not be retained for each application; the reusable interface and correctness conditions are retained instead.

**Use in SDPE Paper 04:** direct external analogue for certificate compilation / reusable proof schemas.

---

## 3. CircuitProver — proof accumulation

**Primary source:** Ziyi Yang et al., *CircuitProver: Agentic Lean 4 Theorem Proving with Reusable Circuit Proof Library for Hardware Verification*, arXiv:2607.27259, 2026.

The system distills proving traces and verified theorems into reusable libraries. On 63 hardware tasks the reported ablation shows accumulated proof knowledge reducing proof length by $16.3\%$ and verification time by $23.2\%$ relative to the corresponding no-accumulation setting.

**Use here:** empirical evidence that verified proof accumulation can reduce redundant construction across related tasks.

**Boundary:** hardware benchmark result; not a universal theorem about mathematics.

---

## 4. Rtl2lean — hierarchical theorem generation and lemma reuse

**Primary source:** Hongqin Lyu et al., *Rtl2lean: Automated RTL-to-Lean Translation with Hierarchical Theorem Generation and Lemma Reuse*, arXiv:2607.16855, 2026.

The framework builds a hierarchical theorem library. Only Lean-kernel accepted lemmas enter the reusable pool. The paper reports 403 generated theorems across six SystemVerilog designs; among 358 foundational lemmas, 287 are available for automatic reuse, a ratio of $80.2\%$.

**Use here:** evidence for kernel-gated reusable theorem pools and hierarchy-aware proof reuse.

---

## 5. LeanAgent — evolving proof knowledge

**Primary source:** Adarsh Kumarappan et al., *LeanAgent: Lifelong Learning for Formal Theorem Proving*, arXiv:2410.06209, 2024.

LeanAgent studies theorem proving over evolving mathematical repositories, using a dynamic database and progressive learning. It reports 155 newly formalized theorems across 23 Lean repositories and explicitly evaluates stability and backward transfer.

**Use here:** context for a proof system whose knowledge base changes over time rather than remaining static.

**Boundary:** model learning / retrieval is not the same as logical certificate validity.

---

## 6. AXLE — strict scalable verification and versions

**Primary source:** Jimmy Xin et al., *AXLE: A Cloud Infrastructure for Lean 4 Theorem Proving Utilities*, arXiv:2606.26442, 2026.

AXLE emphasizes strict proof verification, metadata extraction, request isolation, and concurrent support for multiple Lean / Mathlib versions. The paper explicitly distinguishes compilation from strict verification and motivates version-aware infrastructure for AI-generated formal proofs.

**Use here:** supports SDPE's requirement that compiled traces bind to checker / representation / environment versions.

---

## 7. Literature conclusion

The fresh search supports five distinct reuse layers:

$$
\boxed{
\begin{aligned}
&\text{proof-state reuse},\\
&\text{proof-pattern reuse},\\
&\text{verified lemma reuse},\\
&\text{evolving theorem-library reuse},\\
&\text{strict version-aware replay}.
\end{aligned}
}
$$

No located primary source gives the exact SDPE combination of:

$$
\boxed{
\text{survivor-region support index}
+
\text{support-aware rollback}
+
\text{GCC dependency basis}
+
\text{incremental global replay}.
}
$$

Those are treated as Paper 04 internal constructions.
