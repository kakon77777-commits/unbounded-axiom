# GVSS-06 Handoff — Diagnostic Visual Control and Minimal Intervention Policies

## Starting state

GVSS-05 defines:

$$
F_t
\in
\{
F_{\mathrm{sample}},
F_{\mathrm{constraint}},
F_{\mathrm{compile}},
F_{\mathrm{search}},
F_{\mathrm{reach}},
F_{\mathrm{eval}},
F_{\mathrm{intent}}
\}
$$

and posterior:

$$
b_t(k)
=
P(F_t=F_k\mid H_t).
$$

It also defines one-step posterior diagnostic risk:

$$
\rho_t(a)
=
c(a)
+
\sum_kb_t(k)L(a,k).
$$

## Objective

Turn failure diagnosis into a sequential diagnostic-control policy.

## Main questions

1. When is it better to diagnose first versus directly correct?
2. What is the value of evaluator calibration?
3. When should the controller ask the user?
4. How should human review cost enter the policy?
5. Can diagnostic likelihoods be learned online without destabilizing the controller?
6. How does action choice change the failure state?
7. Can diagnostic regret be bounded over a horizon?
8. When do cheap repeated diagnostics become worse than one expensive decisive test?

## Desired form

$$
\boxed{
b_t(F)
+
B_t
+
\text{action costs}
\Longrightarrow
\text{diagnose}
\vee
\text{correct}
\vee
\text{clarify}
\vee
\text{stop}.
}
$$
