# External Search Notes — EML-ONTO-CORE-03

A fresh external literature search was run immediately before drafting Paper 03.

The technical comparison layer uses primary research papers / author manuscripts.

## 1. ShaLa — shared latent representation

Jiali Cui, Yan-Ying Chen, Yanxia Zhang, Matthew Klenk.
`ShaLa: Multimodal Shared Latent Space Modelling`.
arXiv:2508.17376 (2025).

Relevance:
- explicit shared latent representations across modalities;
- joint multimodal inference and synthesis;
- demonstrates that shared representation is an engineering object.

Use in SSDC:
- methodological precedent for the `Share` layer.
- not evidence that all existence pairs possess a natural shared latent space.

## 2. LatentUMM — transformation alignment matters

Yinyi Luo, Wenwen Wang, Hayes Bai, Marios Savvides, Jindong Wang.
`LatentUMM: Dual Latent Alignment for Unified Multimodal Models`.
arXiv:2605.17766 (2026).

Relevance:
- shared representations can exist while transformations into/out of the latent space remain inconsistently aligned;
- semantic drift can appear during modality transitions.

Use in SSDC:
- strong precedent for separating `Share` from `Transport` and transport fidelity.

## 3. Pairwise modalities and shared latent alignment

Yan Li, Yunlong Deng, Yuewen Sun, Gongxu Luo, Kun Zhang, Guangyi Chen.
`Multimodal LLMs under Pairwise Modalities`.
arXiv:2605.21059 (2026).

Relevance:
- studies when shared latent representations can be identified/aligned from pairwise multimodal observations.

Use:
- comparison point for pairwise-vs-global SSDC questions.

## 4. Shared latent space for cross-modal mapping

Shah Nawaz et al.
`Deep Latent Space Learning for Cross-modal Mapping of Audio and Visual Signals`.
arXiv:1909.08685 (2019).

Relevance:
- shared latent representation used for cross-modal verification/matching.

Use:
- earlier engineering precedent for common representation plus cross-modal mapping.

## 5. Adaptive coupling strength

Xiwei Liu, Tianping Chen.
`Network Synchronization with an Adaptive Coupling Strength`.
arXiv:math/0610580 (2006).

Relevance:
- coupling strength and synchronization are explicitly separate objects;
- synchronization may rely on observed functions of states when full states are unobservable.

Use:
- precedent for typed coupling coefficient and observable-relative synchronization.

## 6. Partial-state coupled dynamical systems

Jiahu Qin, Qichao Ma, Xinghuo Yu, Long Wang.
`On Synchronization of Dynamical Systems over Directed Switching Topologies: An Algebraic and Geometric Perspective`.
arXiv:1807.07840 (2018).

Relevance:
- partial-state coupling;
- projected state dynamics;
- synchronization conditions depend on coupling/network assumptions.

Use:
- supports SSDC's partial-state and directionality design.

## 7. Open-system interfaces

Brendan Fong.
`Decorated Cospans`.
arXiv:1502.00872 (2015).

David Vagner, David I. Spivak, Eugene Lerman.
`Algebras of Open Dynamical Systems on the Operad of Wiring Diagrams`.
arXiv:1408.1598 (2014).

Relevance:
- systems with explicit interfaces and compositional interconnection.

Use:
- precedent for an edge/interface carrying more structure than binary adjacency.

## Boundary rule

These papers are comparison points and mathematical precedents. They do not prove that SSDC is universal, minimal, or ontologically fundamental.
