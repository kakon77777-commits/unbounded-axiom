# GVSS-09 Handoff — Multi-Provider Visual Capability Portfolios, Fallback Geometry, and Federated Reachability

## Starting state

GVSS-08 maintains provider/version uncertainty explicitly and supports:

- nominal control;
- robust control;
- recalibration;
- fallback;
- quarantine;
- stop.

It maintains a joint belief:

$$
\beta_t(F,\nu).
$$

## Objective

Move from provider uncertainty to provider **portfolio geometry**.

## Main questions

1. What is the reachable-set union of a provider portfolio?
2. What is the marginal reachability gain of adding provider $\nu$?
3. When is a provider reachability-redundant?
4. How should switching cost reduce practical portfolio reachability?
5. How does correlated provider failure reduce diversification value?
6. What is the robust reachable set under provider outages/drift?
7. How should calibration debt enter provider selection?
8. Can a small stable fallback provider dominate a large unstable provider on critical regions?

## Desired form

$$
\boxed{
\{\mathcal R_{\nu}\}
+
\text{switch costs}
+
\text{failure correlations}
+
\text{calibration debt}
\Longrightarrow
\text{provider portfolio frontier}.
}
$$

## Prohibitions

- Do not treat union reachability as zero-cost practical reachability.
- Do not assume provider failures are independent.
- Do not infer provider diversity from brand/model-name diversity.
- Preserve provider/version provenance in every fused capability estimate.
