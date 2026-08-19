# GVSS-08 Handoff — Robust Visual Diagnostic Control under Model Uncertainty and Regime Drift

## Starting state

GVSS-07 learns versioned diagnostic models:

$$
\mathsf{DM}_\nu=(\widehat T_\nu,\widehat Q_\nu,\mathcal U_\nu,\mathsf{Prov}_\nu).
$$

GVSS-07 proves one-step posterior sensitivity:

$$
\operatorname{TV}(b^{a,y},\widehat b^{a,y})
\le
\frac{2\varepsilon_T+\varepsilon_Q}{\zeta}.
$$

## Objective

Use model uncertainty and drift probability explicitly in the GVSS-06 controller.

## Main questions

1. When should nominal and robust policies differ?
2. How should uncertainty-set size affect HUMAN_REVIEW and STOP?
3. How should provider drift probability affect REBIND or recalibration?
4. What is the cost of using a stale diagnostic model?
5. How should evaluator/provider fallback and quarantine work?
6. Can multiple provider-specific models be fused without hiding version conflict?
7. How should change-point belief enter the Bellman state?
8. When should calibration budget be spent instead of generation budget?

## Desired form

$$
\boxed{
b_t(F)+\mathcal U_t(T,Q)+P(\text{regime change})+B_t
\Longrightarrow
\text{nominal act}\vee\text{robust act}\vee\text{recalibrate}\vee\text{fallback}\vee\text{stop}.
}
$$

## Prohibitions

- Do not treat a confidence set as proof of truth without coverage assumptions.
- Do not pool incompatible provider versions for convenience.
- Do not interpret robust worst-case value as true-model optimality.
- Preserve model-version and calibration provenance through every fallback.
