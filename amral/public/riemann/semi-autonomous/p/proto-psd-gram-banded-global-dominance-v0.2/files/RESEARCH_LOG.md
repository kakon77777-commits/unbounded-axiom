# Research Log

## 2026-07-24

1. Inherited the 18-patch adaptive cover, 72 candidate rays, structural
   constraints, and holdout discipline from v0.1.
2. Confirmed that no convex SDP solver was available in the runtime.
3. Reframed the full-Gram search as $A=LL^{\mathsf T}$ and recorded the
   nonconvex/global-optimality boundary before running experiments.
4. Replaced the earlier integral axis proxy by five zero-position-free band
   suprema times floating count majorants, plus a tail prototype.
5. Implemented diagonal LP and factorized Gram two-stage programs with
   dense-point exchange.
6. Ran ranks $1,2,4,8$ on four representative patches. All solutions
   numerically collapsed to rank one.
7. Ran the diagonal and full-Gram comparison on all 18 patches.
8. Replaced an overly crude global first-derivative continuity estimate by
   sampled derivatives plus a second-derivative envelope. The refined core
   audit passes all 18 patches; the conservative axis corrections remain in
   the reported budget.
9. Added diagnostics measuring band dominance and distance from the inherited
   ray library.
10. Chose the next node: dual axis-target transfer lower bounds centered on
    $[18,23]$, rather than another undirected primal expansion.

Technical research choices and mathematical interpretations in this node are
AI judgments by OpenAI Codex. Neo.K / EveMissLab supplied the research field,
authorization, and review setting.
