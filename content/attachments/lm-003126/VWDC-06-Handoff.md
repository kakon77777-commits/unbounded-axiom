# VWDC-06 Handoff — Transport-Aware World Decisions, Policy Transfer, and Reality-Gap Robust Control

## Starting state

VWDC-05 defines a Reality Transport Contract:

$$
\mathsf{RTC}_Q
=
(
Q,
\mathcal Z,
\nu_W,
\nu_R,
T_Q,
\mathcal V,
\mathcal A,
\Delta_Q,
\mathcal D_{\mathrm{ext}},
\mathsf{Expiry},
\mathsf{Prov}
).
$$

It separates:

$$
D_{\mathrm{world}},
\quad
D_{\mathrm{transport}},
\quad
D_{\mathrm{measurement}}.
$$

It also labels unsupported / interpolated / extrapolated / structurally transported regions.

## Objective

Use transport validity directly inside world-to-reality decision and control.

## Main questions

1. When is a WDC-optimized policy deployable in reality?
2. How should local transport debt alter action choice?
3. What regret bound follows from bounded reward/value transport error?
4. What should happen when the best simulated action is unsupported in reality?
5. How should external probes compete with conservative fallback?
6. How does policy deployment shift the state distribution and invalidate its own RTC?
7. How should online reality feedback update both policy and transport contract?
8. When should HUMAN/SAFE_FALLBACK override simulated optimum?

## Desired form

$$
\boxed{
\text{world policy/value}
+
\mathsf{RTC}
+
\text{local transport debt}
+
\text{reality feedback}
\Longrightarrow
\text{deploy}
\vee
\text{robust deploy}
\vee
\text{probe}
\vee
\text{fallback}
\vee
\text{stop}.
}
$$

## Prohibitions

- Do not deploy an action whose relevant state/action region is unsupported without an explicit risk policy.
- Do not reuse a pre-deployment state-distribution RTC after the policy materially changes reality visitation without checking shift.
- Do not confuse simulated policy optimality with real-world policy optimality.
- Preserve every RTC/version used for every deployed decision.
