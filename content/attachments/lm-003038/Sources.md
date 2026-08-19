# SOURCES v0.8

Primary research checked before writing this version:

1. Ma et al., **Scaling Inference Time Compute for Diffusion Models**, CVPR 2025. Verifier-guided search over noise / candidate trajectories improves sample quality with additional inference-time compute.
2. Koulischer et al., **Feedback Guidance of Diffusion Models**, arXiv:2506.06085 (2025). Introduces state- and time-dependent closed-loop guidance rather than a fixed open-loop scale.
3. Qiao et al., **TTGen: Incorporating Test-time Scaling to Diffusion Models**, CVPR Workshops 2025. Uses step-wise prompt refinement and best-of-N trajectory selection.
4. Xin et al., **dMLLM-TTS: Self-Verified and Efficient Test-Time Scaling for Diffusion Multi-Modal Large Language Models**, CVPR 2026. Combines trajectory exploration, iterative refinement, and self-verification.
5. Guo et al., **Toward Early Quality Assessment of Text-to-Image Diffusion Models**, CVPR 2026. Shows intermediate denoiser activations can support early prediction / selection of final quality.
6. Shen et al., **Agentic Retoucher for Text-To-Image Generation**, CVPR 2026. Demonstrates an agentic local-retouching direction for correcting text-to-image defects.
7. Yang et al., **M3: High-fidelity Text-to-Image Generation via Multi-Modal, Multi-Agent and Multi-Round Visual Reasoning**, arXiv:2602.06166 (2026). Planner / Checker / Refiner / Editor / Verifier iterative refinement framework.
8. Papalampidi et al., **Dynamic Classifier-Free Diffusion Guidance via Online Feedback**, arXiv:2509.16131 (2025). Online latent-space evaluation dynamically selects CFG schedules per prompt/sample.

Design note: v0.8 uses these works as engineering evidence that dynamic verification, test-time search, early quality assessment, and iterative correction are viable. The exact AADS/GAR policy graph and anti-homogenization logic remain our own experimental system design.
