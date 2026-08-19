# GVSS-05 Handoff — Visual Failure Stratification and Reachability Diagnosis

## Starting state

GVSS-04 defines visual regime

$$
r_t
=
(
\mathsf G_t,
\Gamma_t,
C_t,
\Lambda_t,
\Pi_t,
O_t,
E_t,
B_t,
\mathsf{Prov}_t
)
$$

and separates:

$$
\text{RESAMPLE}
\neq
\text{RECOMPILE}
\neq
\text{REBIND}.
$$

## Objective

Make the failure diagnosis itself quantitative.

## Candidate latent failure state

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
\}.
$$

Maintain belief:

$$
b_t(k)
=
P(F_t=F_k\mid H_t).
$$

## Main questions

1. When should rerolling stop?
2. What evidence justifies RECOMPILE?
3. What evidence justifies REBIND?
4. How does evaluator disagreement update failure belief?
5. How should budget affect diagnostic escalation?
6. Can a diagnostic policy be evaluated independently of final image quality?
7. What is the regret of choosing the wrong failure layer?

## Desired theorem form

$$
\boxed{
\text{observed visual deficit}
+
\text{history}
\Longrightarrow
\text{failure belief}
\Longrightarrow
\text{least-cost justified intervention}.
}
$$

## Prohibitions

- Do not infer generator reachability failure from a few bad seeds.
- Do not infer intent failure solely from one evaluator.
- Do not assume the current style chart is intrinsic.
- Keep diagnostic confidence separate from image quality score.
