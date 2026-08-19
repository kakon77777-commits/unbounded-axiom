# VWDC-07 Handoff — Closed-Loop Reality Feedback, Safe Policy Adaptation, and Transport-Aware Continual Worlds

## Starting state

VWDC-06 uses:

$$
(
\pi_v,
\mathsf{RTC}_u
)
$$

as a versioned deployment pair.

It establishes:

$$
D_\pi
\le
D_{\mathrm{val}}
+
M
TV(
d_\pi,
d_{\mathrm{val}}
)
$$

and shows policy deployment can destroy its own pre-deployment certification by moving reality visitation.

## Objective

Formalize the continual loop:

$$
\boxed{
World
\to
RTC
\to
Policy
\to
Reality
\to
Evidence
\to
World/RTC/Policy.
}
$$

## Main questions

1. How should real feedback update world model and RTC without circular self-confirmation?
2. When does feedback justify a policy update versus an RTC-only update?
3. How can a policy update preserve old certified regions?
4. When should world/reality drift create a new regime ID?
5. What rollback rule should apply after performance/safety degradation?
6. How should invalid real incidents propagate through model and branch evidence?
7. How should old policies/RTCs be retained as fallback?
8. What stability/invariance notion is appropriate for the full continual loop?

## Desired form

$$
\boxed{
\text{reality feedback}
+
\text{deployment provenance}
+
\text{drift}
+
\text{safety/transport contracts}
\Longrightarrow
\text{update}
\vee
\text{revalidate}
\vee
\text{rollback}
\vee
\text{freeze}
\vee
\text{fallback}.
}
$$

## Prohibitions

- Do not train and validate on deployment feedback as if it were independent evidence without accounting for selection.
- Do not overwrite old policy/RTC versions.
- Do not infer preserved safety from preserved reward.
- Do not continue adaptation after contract/safety rollback triggers fire.
