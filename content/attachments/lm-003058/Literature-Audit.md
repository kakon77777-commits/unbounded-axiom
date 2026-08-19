# VWDC-01 Literature Audit

**Date:** 2026-08-17  
**Policy:** Primary research sources/current research-lab release; conservative novelty language.

## 1. Interactive generative environments

### Genie
Bruce et al., arXiv:2402.15391, 2024.

Genie is a generative interactive environment trained from unlabeled video. It uses a spatiotemporal video tokenizer, autoregressive dynamics model, and latent action model and supports frame-by-frame action control.

**VWDC relation:** strong evidence that visual generation can become interactive only by adding temporal/action dynamics beyond isolated frame synthesis.

### GameNGen
Valevski et al., arXiv:2408.14837, 2024.

A diffusion model acts as a real-time neural game engine for DOOM. The next frame is generated conditioned on a sequence of past frames and actions.

**VWDC relation:** especially direct precedent for the static-frame dynamics no-go: interactive generation uses history/action state.

### DIAMOND
Alonso et al., arXiv:2405.12399, 2024.

Uses diffusion models as environment/world models for RL and demonstrates an interactive neural game engine.

**VWDC relation:** shows that image-generative models can implement meaningful environment dynamics while remaining learned models.

### Genie 3
Google DeepMind research release, 2025.

Described as a real-time interactive world model generating controllable environments with multi-minute consistency, promptable world events, and explicit current limitations such as limited action space and finite interaction duration.

**VWDC relation:** current engineering evidence that generated interactive worlds are real system objects, but also bounded and incomplete.

## 2. Inverse rendering / visual scene reconstruction

### Neural Inverse Rendering of an Indoor Scene from a Single Image
Sengupta et al., arXiv:1901.02453.

Estimates albedo, normals, and lighting from a single image using learned/physical rendering structure.

### NeRF
Mildenhall et al., arXiv:2003.08934.

Optimizes a continuous volumetric scene representation from multiple posed images for novel-view synthesis.

### pixelNeRF
Yu et al., arXiv:2012.02190.

Uses learned scene priors to infer neural scene representations from one or a few images.

**VWDC boundary:** these methods reconstruct scene representations/attributes. They do not establish unique full runnable-world identity, hidden causal state, action semantics, replay, or world evidence.

## 3. Partial observability / latent state

### Latent World Models for Intrinsically Motivated Exploration
Ermolov and Sebe, arXiv:2010.02302.

Studies partially observable image-based environments and uses a latent world model to estimate missing environmental information.

**VWDC relation:** direct prior precedent for the fact that visual observation can be incomplete relative to environment/world state.

## 4. Novelty boundary

Do not claim as VWDC inventions:

- observation functions;
- inverse maps/injectivity facts;
- observational equivalence;
- quotient dynamics/lumpability;
- POMDP belief states;
- inverse rendering;
- scene reconstruction;
- latent world models;
- interactive generative environments.

Potential VWDC-01 synthesis contribution:

1. precise GVSS-to-WDC interface through a visual observation operator;
2. contract-relative visual liftability;
3. explicit separation of render inversion from runnable-world validation;
4. static-frame dynamics closure criterion as a bridge requirement;
5. bridge-compatible reachability as visual reachability intersected with world-contract liftability;
6. separate visual/world lineages and evidence boundaries.

No strong novelty claim is made.
