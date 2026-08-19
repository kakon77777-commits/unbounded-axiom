# GVSS-07 Handoff — Online Visual System Identification and Diagnostic Model Learning

## Starting state

GVSS-06 assumes controlled kernels:

$$
T_a(F'\mid F)
$$

and diagnostic likelihoods:

$$
Q_a(y\mid F).
$$

These are generally unknown in real image-generation systems.

GVSS-06 proves a sensitivity bound:

$$
\operatorname{TV}
(
b^y,\widehat b^y
)
\le
\varepsilon/\zeta
$$

under weighted likelihood error $\varepsilon$ and evidence lower bound $\zeta$.

## Objective

Learn and calibrate the diagnostic-control model online.

## Main questions

1. How should $Q_a(y\mid F)$ be estimated?
2. How should $T_a(F'\mid F)$ be estimated?
3. How can synthetic failure injection provide ground truth?
4. How should provider/model versions index the learned dynamics?
5. How can self-confirming failure labels be avoided?
6. How should uncertainty sets around $Q,T$ affect the GVSS-06 controller?
7. Can active diagnostic experiments identify the transition model efficiently?
8. When should old diagnostic models be invalidated after a backend update?

## Desired form

$$
\boxed{
\text{failure traces}
+
\text{controlled interventions}
\Longrightarrow
\widehat Q,\widehat T
+
\text{uncertainty}
\Longrightarrow
\text{robust diagnostic control}.
}
$$

## Prohibitions

- Do not train diagnostic ground truth solely from the controller's own predictions.
- Do not pool provider versions without testing stationarity.
- Do not ignore rare-observation posterior conditioning.
- Preserve calibration/provenance for every learned diagnostic model.
