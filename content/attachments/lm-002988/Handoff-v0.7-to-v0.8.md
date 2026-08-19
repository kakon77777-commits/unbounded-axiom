# HIPG Formal Toy v0.7 — v0.8 Handoff

## Verified v0.7 additions

- parameterized derived operator proposal from repeated program structure;
- Dirichlet confidence sets and active dynamics experiments;
- learned observation model before belief quotienting;
- latent `(partner adapter, task semantics)` equivalence class as a first-class object;
- intervention selection by expected equivalence-class split;
- OOD support-aware confidence and `UNKNOWN_DIAGNOSIS` abstention;
- mixed SymPy SAT + SciPy LP bridge with provenance anchors;
- cross-task meta-regret including grammar and partner-adaptation costs.

## Remaining oracles

1. primitive AST operators are supplied;
2. active dynamics knows task-start states and reward semantics;
3. observation learning uses reset interventions with known hidden-state identity;
4. latent splitting knows `TOGGLE_E/J/O` semantics;
5. diagnostic hard guards are coded;
6. formal constraint families are selected by the researcher.

## v0.8 Priority A — behavioral operator invention

Move beyond shared AST shape. Search a bounded finite truth-table transformation space and propose operators because they compress **behaviorally equivalent residuals** and improve held-out meta-regret.

Do not call this universal language invention.

## Priority B — joint reward + dynamics discovery

Learn

$$
\widehat P(x'|x,a),\qquad \widehat R(x,a,x')
$$

and choose experiments by expected reduction in value / quotient uncertainty rather than transition entropy alone.

## Priority C — unlabeled observation-model discovery

Remove `RESET_h0/RESET_h1` state labels. Use a finite HMM / EM or intervention-induced separation, and keep permutation-equivalent latent models when labels are not identifiable.

## Priority D — unknown intervention semantics

Maintain

$$
[(\rho,h,\iota)]_{\equiv}
$$

rather than assuming the semantic meaning of `TOGGLE_E/J/O`. Select raw actions by expected class split.

## Priority E — diagnostic certificates

Combine theorem/lower-bound anchors, learned likelihood, OOD support score, abstention reason, and alternative diagnoses in one certificate. Consider conformal coverage if practical.

## Priority F — temporal formal fragment

No Z3, Lean, or cvc5 backend is installed in the current runtime. Do not fake one. Add an explicit finite-state temporal model checker and export witnesses/counterexamples, while preserving the existing SAT and LP fragments.

## Priority G — drifting task-stream meta-regret

Compare no library, static library, learned operators, and operator retirement under distribution shift:

$$
R_{meta}=\sum_T(R_T+\lambda_GC_G+\lambda_PC_P+\lambda_DC_{drift}).
$$

## Priority H — permanent non-identifiability

Allow terminal `UNKNOWN_EQUIVALENCE_CLASS` with the surviving model class when all admissible finite interventions fail to split it.
