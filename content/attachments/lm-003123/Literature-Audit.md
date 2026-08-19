# VWDC-02 Literature Audit

**Date:** 2026-08-17  
**Policy:** Primary research sources only; conservative novelty language.

## 1. Multi-step visual tool workflows

### I2E
Yu et al., arXiv:2601.03741, 2026.

Decomposes images into discrete manipulable object layers and uses a physics-aware vision-language-action agent to convert complex instructions into atomic editing actions.

**VWDC relation:** direct precedent for typed/decomposed visual editing state rather than a monolithic pixel transformation.

### RS-Gen
Bian et al., arXiv:2606.23221, 2026.

Multi-stage reasoning/search-augmented image generation and editing with a closed-loop problem-posing/problem-solving workflow.

**VWDC relation:** direct precedent for multi-stage visual composition.

### PhotoAgent
arXiv:2602.22809, 2026.

Closed-loop editing system with editing/evaluation tools and long-horizon action-sequence planning.

**VWDC relation:** direct precedent for iterative visual tool paths.

### CanvasAgent
arXiv:2607.05465, 2026.

Uses specialized tools including generation, editing, localization, segmentation, extraction, compositing, geometric transformation, OCR, and super-resolution.

**VWDC relation:** strong current precedent for heterogeneous typed visual-tool pipelines.

### GenClaw
arXiv:2605.30248, 2026.

Separates cognitive structuring, executable canvas construction, visual generation, and review.

**VWDC relation:** direct precedent for multi-representation multi-stage visual workflows.

### Qwen-Image-Agent
arXiv:2606.26907, 2026.

Training-free image-generation agent with reasoning, search, memory, multi-image context, multi-turn interaction, and feedback.

**VWDC relation:** current precedent for visual generation embedded in an agentic context/tool loop.

## 2. Interactive/action-conditioned world systems

### COMBAT
Agarwal et al., arXiv:2603.00825, 2026.

Real-time action-controlled world model with reactive behavior in a fighting-game environment.

**VWDC relation:** direct precedent that world-state edges represent action-conditioned dynamics, not image editing.

### LIVE
Huang et al., arXiv:2602.03747, 2026.

Long-horizon interactive video world model explicitly addressing rollout-error accumulation.

**VWDC relation:** direct current evidence that defects accumulate across long world-generation paths.

### DreamX-World 1.0
arXiv:2606.16993, 2026.

Interactive world model supporting navigation, revisits, long-horizon generation, and promptable events.

**VWDC relation:** current world-trajectory precedent.

### DAWN
Lu et al., arXiv:2605.11550, 2026.

Recursively couples world prediction and action generation during inference.

**VWDC relation:** prior example of world/action transformations that are mutually conditioned.

### GameNGen
Valevski et al., arXiv:2408.14837, 2024.

Action/history-conditioned real-time neural game-engine generation.

### Genie
Bruce et al., arXiv:2402.15391, 2024.

Action-controllable generative interactive environments.

## 3. Classical provenance

The following mathematical pieces are classical and not VWDC inventions:

- typed/partial function composition;
- graph reachability;
- nonnegative shortest paths;
- cycle elimination in repeated exact nodes;
- Lipschitz perturbation propagation;
- vector affine error recursion;
- sigma-algebra/data-processing facts;
- Pareto necessity.

## 4. Candidate VWDC synthesis

Potential bridge-specific contribution, subject to wider audit:

1. one typed operation graph containing visual artifacts, world candidates, runnable worlds, checkpoints, and evidence packets;
2. a separate world-candidate type plus validation gate for LIFT;
3. strict composition beyond one-stage visual-provider union;
4. shared defect transport across visual and world operations;
5. exact-state-cycle versus productive type-level-loop distinction;
6. restore-as-new-lineage-node semantics;
7. evidence-policy labels for derived/world/interventional/external evidence.

No strong novelty claim is made.
