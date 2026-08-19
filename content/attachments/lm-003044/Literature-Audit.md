# GVSS-09 Literature Audit

**Date:** 2026-08-17  
**Policy:** Primary research sources; conservative novelty language.

## 1. Multi-model T2I routing

### Cost-Aware Routing for Efficient Text-To-Image Generation
Li et al., arXiv:2506.14753, 2025.

Routes each prompt to a T2I generation function/model chosen to balance expected image quality and compute cost. The evaluated router uses nine already-trained image models/functions and reports average quality above any one model alone under its setup.

**GVSS relation:** direct current precedent for treating multiple T2I models as a routable provider portfolio.

### Adaptive Routing of Text-to-Image Generation Requests between Edge and Cloud Models
arXiv:2411.13787.

Studies prompt-aware routing between lightweight edge and larger cloud T2I models under quality/cost tradeoffs.

**GVSS relation:** direct precedent for provider fallback and switching-cost geometry.

### OctoT2I
arXiv:2606.01803, 2026.

Uses stateful multi-round routing among T2I tools and a self-evolving knowledge base to adapt tool choice.

**GVSS relation:** close current precedent for capability-aware, multi-round provider routing.

### HADIS
arXiv:2509.00642, 2025.

Studies adaptive diffusion serving/cascading to improve cost efficiency across prompts of different complexity.

**GVSS relation:** current serving-system precedent for dynamic model selection.

## 2. Internal expert routing

### RAPHAEL
Xue et al., arXiv:2305.18295.

Uses large mixture-of-experts diffusion paths specialized across concepts, regions, and timesteps.

### ERNIE-ViLG 2.0
Feng et al., arXiv:2210.15257.

Uses knowledge-enhanced mixtures of denoising experts.

**GVSS boundary:** these systems route internal experts inside one model; GVSS-09 addresses external, versioned provider portfolios with switching, calibration, and failure semantics.

## 3. Design diversity and correlated failures

### Exploring Resiliency to Natural Image Corruptions in Deep Learning using Design Diversity
Rosales, Munoz, Paulitsch, arXiv:2303.09283.

Studies how architectural/design diversity relates to error diversity and resilience under natural image corruptions.

**GVSS relation:** prior empirical evidence that diversity is usefully measured through failure behavior rather than merely model count.

## 4. Classical mathematical provenance

The following GVSS-09 components are classical mathematics:

- union coverage;
- monotone submodular coverage;
- maximum coverage;
- greedy $1-1/e$ approximation under cardinality constraints;
- Fréchet probability bounds;
- correlated-failure/ensemble reliability analysis.

These are not GVSS inventions.

## 5. Candidate GVSS synthesis

Potential GVSS-specific synthesis, subject to wider audit:

1. external image providers represented as reachable subsets of a common visual state space;
2. provider marginal value as uncovered visual-state measure;
3. explicit separation of union redundancy from robustness redundancy;
4. exact multiplicity characterization of $r$-provider worst-case outage reachability;
5. critical-region weighted visual fallback geometry;
6. integration of switching/calibration debt with visual reachability;
7. higher-order failure warning for visual provider portfolios;
8. capability/failure/cost diversity as separate provider-portfolio dimensions.

No strong novelty claim is made in v0.1.
