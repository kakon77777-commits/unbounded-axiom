# SDPE Paper 05 — Fresh Literature Notes
## Discovery–Verification Inversion

**Search date:** 2026-08-14  
**Rule:** technical grounding uses primary sources only; domain-specific speedups are not promoted into universal mathematical laws.

---

# 1. Austin Shen and Yunong Shi — proof-state snapshotting

**Primary source:** Austin Shen, Yunong Shi, **Keep the Proof State Live: Snapshotting for Efficient Tactic Search in Lean 4**, arXiv:2605.25556, 2026.

Relevant results:

- Lean portfolio tactic branches can spend overwhelming wall time reconstructing import and elaborated theorem state rather than executing tactics;
- the paper reports 5.6--50x wall-time speedup over its fallback on 48 miniF2F-v2 problems, with average 14x and median 9.7x on the 45 hand-crafted prove-phase benchmarks;
- the authors explicitly state that the hand-crafted benchmark measures tactic-search infrastructure speed, not general proof discovery.

**Use in Paper 05:** establishes a concrete operational example in which reusing already-elaborated state radically lowers repeated branch startup cost.

**Boundary:** this is evidence for reconstruction avoidance / routine-resolution acceleration, not proof that frontier theorem discovery becomes easier.

---

# 2. Daniela Kaufmann and Clemens Hofstadler — certificate recycling

**Primary source:** Daniela Kaufmann, Clemens Hofstadler, **Recycling Algebraic Proof Certificates**, arXiv:2507.20267, 2025.

Relevant results:

- extends an algebraic proof calculus with explicit rules for capturing and reusing repeated proof fragments;
- integrates the rules into the Pacheck 2.0 proof checker;
- reports reductions in proof size and verification time.

**Use in Paper 05:** evidence that proof compilation can amortize not only search but verification itself.

**Boundary:** therefore a rising verification share does not imply verification absolute cost must rise.

---

# 3. CircuitProver — accumulated verified proof knowledge

**Primary source:** Ziyi Yang, Wenji Fang, Chen Chen, Zhiyao Xie, Hongce Zhang, **CircuitProver: Agentic Lean 4 Theorem Proving with Reusable Circuit Proof Library for Hardware Verification**, arXiv:2607.27259, 2026.

Relevant results:

- builds reusable proving traces and verified theorem libraries across related parameterized hardware tasks;
- evaluates 63 tasks;
- its ablation reports accumulated proof knowledge reduces proof length by 16.3% and verification time by 23.2%;
- a vanilla agent requires roughly twice as many proof rounds on average and does not solve the complete suite.

**Use in Paper 05:** domain-specific evidence that verified proof accumulation can reduce redundant construction and checking.

**Boundary:** hardware proof families are highly related and structured; the results do not establish universal DVI for open-ended mathematics.

---

# 4. LeanAgent — lifelong theorem proving

**Primary source:** Adarsh Kumarappan et al., **LeanAgent: Lifelong Learning for Formal Theorem Proving**, arXiv:2410.06209, 2024.

Relevant results:

- uses a dynamic database for evolving mathematical knowledge;
- studies continual transfer, stability, and backward transfer across multiple repositories;
- reports proof performance improvements as knowledge accumulates.

**Use in Paper 05:** supports treating proof accumulation as a longitudinal process rather than a static benchmark.

**Boundary:** learning-system transfer is not identical to certified proof-space contraction.

---

# 5. VeriSoftBench — frontier/context hardening evidence

**Primary source:** Yutong Xin, Qiaochu Chen, Greg Durrett, Işil Dillig, **VeriSoftBench: Repository-Scale Formal Verification Benchmarks for Lean**, arXiv:2602.18307, 2026.

Relevant results:

- 500 repository-scale Lean proof obligations;
- proof success is strongly correlated with transitive repository dependence;
- tasks requiring larger, multi-hop dependency closures are less likely to be solved;
- curated context restricted to the proof's dependency closure improves performance relative to exposing the whole repository, but still leaves substantial room for improvement.

**Use in Paper 05:** primary evidence that accumulated context / dependency depth can act as a counterforce to naive "more knowledge means easier theorem" narratives.

This is the closest fresh literature input to the Paper 05 concept of **Frontier Hardening**.

---

# 6. AXLE — scalable verification is its own systems layer

**Primary source:** Jimmy Xin et al., **AXLE: A Cloud Infrastructure for Lean 4 Theorem Proving Utilities**, arXiv:2606.26442, 2026.

Relevant results:

- provides strict proof verification, declaration metadata extraction, semantic source manipulation, proof repair/simplification, and lemma extraction;
- supports multi-version Lean / Mathlib and per-request isolation;
- explicitly motivates scalable verification infrastructure for modern AI theorem-proving workloads.

**Use in Paper 05:** supports separating verification workload from proof-generation workload in the cost ledger.

**Boundary:** AXLE throughput or scale is not itself evidence of a discovery-verification phase inversion.

---

# 7. Literature synthesis

The primary literature currently establishes several pieces separately:

$$
\boxed{
\text{state reuse can remove reconstruction cost}
}
$$

$$
\boxed{
\text{certificate reuse can reduce checking cost}
}
$$

$$
\boxed{
\text{verified knowledge accumulation can improve related proof tasks}
}
$$

and simultaneously:

$$
\boxed{
\text{large dependency closures can make remaining tasks harder}.
}
$$

What the fresh literature does **not** establish is a universal longitudinal theorem of the form

$$
\boxed{
\text{proof history grows}
\Longrightarrow
D_t^{\rm frontier}\downarrow
\Longrightarrow
\text{verification-dominated phase}.
}
$$

That stronger statement is exactly why SDPE Paper 05 treats Discovery–Verification Inversion as a falsifiable hypothesis rather than an external theorem.

---

# 8. Benchmark consequence

Any empirical test of DVI must separately measure:

1. reconstruction / repeated-query savings;
2. frontier theorem discovery;
3. formal checking;
4. coverage / boundary audit;
5. gluing where applicable;
6. maintenance / version / replay;
7. one-time compilation cost.

Otherwise snapshot/cache/retrieval improvements can be mistaken for theorem-discovery acceleration.
