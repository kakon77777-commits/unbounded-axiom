# SDPE Paper 07 — Fresh Literature Notes

**Date:** 2026-08-14  
**Rule:** technical grounding uses primary papers / publisher records; theorem-transfer assumptions are kept explicit.

## 1. Nemhauser--Wolsey--Fisher: deterministic submodular coverage

Primary publication:

- G. L. Nemhauser, L. A. Wolsey, M. L. Fisher, **An Analysis of Approximations for Maximizing Submodular Set Functions—I**, *Mathematical Programming* 14 (1978), 265–294, DOI `10.1007/BF01588971`.
- G. L. Nemhauser, L. A. Wolsey, **Best Algorithms for Approximating the Maximum of a Submodular Set Function**, *Mathematics of Operations Research* 3(3) (1978), 177–188, DOI `10.1287/moor.3.3.177`.

Use in SDPE:

If a routing objective has actually been proved monotone submodular under a cardinality budget, greedy approximation theory can be imported.

Boundary:

General theorem discovery is not assumed submodular.

## 2. Golovin--Krause: adaptive submodularity

Primary source:

- Daniel Golovin, Andreas Krause, **Adaptive Submodularity: Theory and Applications in Active Learning and Stochastic Optimization**, arXiv:`1003.3967`.

The paper generalizes submodular reasoning to adaptive decisions under uncertain observations and proves guarantees for adaptive greedy when adaptive monotonicity / adaptive submodularity hold.

Use in SDPE:

A conditional model for uncertain research actions.

Boundary:

The structure must be proved for the chosen SDPE routing utility; sequential uncertainty alone is not enough.

## 3. HyperTree Proof Search

Primary source:

- Guillaume Lample et al., **HyperTree Proof Search for Neural Theorem Proving**, arXiv:`2205.11491`.

The work explicitly treats theorem proving as learned search over proof states and demonstrates that search policy is a first-class component of prover performance.

Use in SDPE:

External evidence that proof-state routing is a real algorithmic object.

## 4. DeepSeek-Prover-V1.5

Primary source:

- Huajian Xin et al., **DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search**, arXiv:`2408.08152`.

The system combines formal proof-assistant feedback with reinforcement learning and a Monte-Carlo-tree-search variant for proof-path exploration.

Use in SDPE:

Context for uncertainty-aware path selection and search/exploration tradeoffs.

## 5. BFS-Prover

Primary source:

- Ran Xin et al., **BFS-Prover: Scalable Best-First Tree Search for LLM-based Automatic Theorem Proving**, arXiv:`2502.03438`.

The paper studies scalable best-first proof search and state/tactic prioritization.

Use in SDPE:

Context that simpler priority policies can be competitive when the ranking signal and data loop are appropriate.

## 6. LeanProgress

Primary source:

- Suozhi Huang et al., **LeanProgress: Guiding Search for Neural Theorem Proving via Proof Progress Prediction**, arXiv:`2502.17925`.

The paper predicts proof progress / remaining steps and injects this estimate into best-first search, improving the reported downstream proof-search result on its evaluation.

Use in SDPE:

A direct precedent for learned progress estimation as a routing feature.

Boundary:

Predicted proof progress is not the same as global closure value.

## 7. LeanSearch v2

Primary source:

- Guoxiong Gao et al., **LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving**, arXiv:`2605.13137`.

The work studies theorem-level premise retrieval and reports downstream proof-success differences under a fixed prover loop when retrieval quality changes.

Use in SDPE:

External precedent that selecting the right theorem/premise neighborhood changes proof success.

Boundary:

Premise retrieval optimizes local proof completion, not SDPE's multi-epoch GCC closure objective.

## 8. Literature conclusion

Existing theory already gives mature guarantees for special routing geometries:

$$
\text{submodular}
\Rightarrow
\text{greedy approximation},
$$

and

$$
\text{adaptive submodular}
\Rightarrow
\text{adaptive greedy approximation}.
$$

Modern ATP systems also make search priority, value estimation, premise retrieval and path exploration explicit.

The SDPE-specific problem begins where these structures are not given in advance: closure value may combine bulk exclusion, zero-measure core separability, boundary ownership, representation refinement, bridge option value and certificate debt. Therefore Paper 07 treats routing geometry classification as a proof obligation before algorithm selection.
