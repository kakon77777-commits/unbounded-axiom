# GVSS-04 Literature Audit

**Date:** 2026-08-17  
**Policy:** Primary research papers only. Conservative novelty language.

## Foundational controllable generation

### Latent Diffusion Models
Rombach et al., arXiv:2112.10752 / CVPR 2022.

Relevance:
- image generation in learned latent representation;
- cross-attention conditioning;
- computational representation differs from raster ambient space.

### Classifier-Free Guidance
Ho and Salimans, arXiv:2207.12598.

Relevance:
- inference-time guidance changes fidelity/diversity tradeoff;
- a control coordinate modifies sampling geometry.

### ControlNet
Zhang, Rao, and Agrawala, arXiv:2302.05543.

Relevance:
- explicit structural controls beyond text prompt;
- supports GVSS Paper 02's multi-provider constraint view.

### Prompt-to-Prompt
Hertz et al., arXiv:2208.01626.

Relevance:
- cross-attention control for localized/global semantic editing;
- prior art for structure-preserving edit/refinement.

## Evaluation

### GenEval
Ghosh, Hajishirzi, and Schmidt, arXiv:2310.11513.

Relevance:
- fine-grained object/composition evaluation;
- demonstrates that different visual properties require explicit evaluators.

### ImageReward
Xu et al., arXiv:2304.05977.

Relevance:
- learned human-preference reward model;
- shows evaluator/reward models can guide image optimization.

### VQAScore
Lin et al., arXiv:2404.01291.

Relevance:
- compositional text-image evaluation with VQA;
- directly relevant to verifier-gated navigation.

## Closed-loop and test-time refinement

### Test-time Prompt Refinement for Text-to-Image Models
Khan et al., arXiv:2507.22076.

Relevance:
- generate -> inspect with MLLM -> rewrite prompt -> regenerate;
- direct precedent for RECOMPILE closed-loop refinement.

### Iterative Refinement Improves Compositional Image Generation
Jaiswal et al., arXiv:2601.15286.

Relevance:
- VLM critic proposes corrections;
- iterative refinement can outperform compute-matched parallel sampling on reported compositional benchmarks.

### VisionDirector
Chu et al., arXiv:2512.19243.

Relevance:
- structured goals;
- semantic verification;
- staged edits;
- rollback;
- especially close operational overlap with GVSS runtime.

### Agentic Retoucher
Shen et al., arXiv:2601.02046.

Relevance:
- perception-reasoning-action loop;
- localized artifact diagnosis and repair.

### Qwen-Image-Agent
arXiv:2606.26907.

Relevance:
- Context Gap between user context and sufficient generation context;
- plan, reason, search, memory, feedback;
- strong overlap with the high-level Intent Compiler / context construction idea.

### An Efficient Test-Time Scaling Approach for Image Generation
Sundaresha et al., arXiv:2512.08985.

Relevance:
- verifier-guided noise search;
- inference budget allocation;
- direct precedent for budgeted visual navigation.

## Novelty boundary

Do **not** claim as GVSS inventions:

- feedback refinement;
- iterative prompt rewriting;
- VLM critics;
- multimodal verification;
- best-of-N test-time scaling;
- diffusion guidance;
- ControlNet-like structural control;
- agentic image generation.

Potential GVSS-04 synthesis contribution:

1. one state-space formalization joining ambient image space, constraints, bounded reachability, and reflexive control;
2. action-level geometric separation of RESAMPLE / RECOMPILE / REBIND;
3. policy-dependent practical reachability;
4. RRT vector-defect transport applied to the existing eight-axis visual runtime;
5. style map as representation chart rather than intrinsic geometry;
6. evaluator gating as part of accepted reachability;
7. lineage-preserving regime evolution.

No strong novelty claim is made in v0.1.
