# GVSS-10 Handoff — Task-Conditioned Visual Routing, Capability Attribution, and Portfolio Learning

## Starting state

GVSS-09 defines provider portfolio:

$$
S\subseteq\mathcal P
$$

with provider reachable sets:

$$
\mathcal R_\nu.
$$

Raw coverage:

$$
f(S)
=
\mu
\left(
\bigcup_{\nu\in S}\mathcal R_\nu
\right).
$$

Robust $r$-outage reachability:

$$
\mathcal R_{\mathrm{rob}}^{(r)}(S)
=
\{
I:
m_S(I)\ge r+1
\}.
$$

GVSS-09 also shows failure dependence matters and pairwise correlation is insufficient for higher-order tail risk.

## Objective

Learn task-conditioned provider capability and route prompts/projects online.

## Main questions

1. How should provider success/quality/cost be conditioned on task $\theta$?
2. How should capability models be learned without routing-selection bias?
3. How should a router explore underused providers?
4. What is regret versus an oracle provider selector?
5. How should provider cold-start calibration enter routing?
6. How should higher-order common-mode failure affect sequential routing?
7. Can provider contribution be attributed after multi-stage cross-provider edits?
8. How should capability drift trigger router retraining?

## Desired form

$$
\boxed{
\theta_t
+
\widehat{\mathcal C}_\nu(\theta)
+
\text{cost}
+
\text{uncertainty}
+
\text{failure dependence}
\Longrightarrow
\text{route}
\vee
\text{probe}
\vee
\text{fallback}
\vee
\text{multi-stage compose}.
}
$$

## Prohibitions

- Do not infer provider quality only from traffic already routed to it without accounting for selection.
- Do not starve a new provider of all exploration and then claim it has no capability.
- Preserve provider/version identity through multi-stage outputs.
- Do not reduce provider diversity to one global average score.
