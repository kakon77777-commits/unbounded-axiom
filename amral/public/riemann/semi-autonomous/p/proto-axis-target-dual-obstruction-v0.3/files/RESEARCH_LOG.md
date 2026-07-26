# Research Log

## 2026-07-24

1. Inherited the 18-patch cover, 22-dimensional constrained model, band
   definitions, tail prototype, and saved v0.2 Gram matrices.
2. Re-derived the finite conic dual signs and normalization.
3. Checked the runtime and found no installed convex SDP solver.
4. Tested a minimal nonnegative measure: the uniform 26-point measure on
   $[18,23]$, with a downward-rounded count coefficient.
5. Found that adding only $10^{-3}$ of the tail matrix and
   $2C(z_P)$ makes all 18 patch-center witness matrices positive definite.
6. Exported one witness record per patch and cross-checked all saved parent
   primal Gram matrices.
7. Rationalized tail and transform data, then verified all 18 matrices with
   exact `Fraction` $LDL^{\mathsf T}$.
8. Repeated the rational check at 6, 8, 10, and 12 decimal places.
9. Ran quadrature-step, axis-grid, and tail-fraction sensitivity sweeps.
10. Diagnosed the support-radius frontier under approximately 8 bumps per
    unit: first sampled partial escape at $R=5.1$, stable sampled all-center
    escape from $R=8.5$ onward.
11. Retired the current $R=3$ patchwise finite-model class and selected
    `RH_Support_Prime_Dual_Frontier_v0.4` as the next node.

Technical choices, mathematical interpretations, and the node transition are
AI judgments by OpenAI Codex. Neo.K / EveMissLab supplied the research field,
authorization, and review setting.
