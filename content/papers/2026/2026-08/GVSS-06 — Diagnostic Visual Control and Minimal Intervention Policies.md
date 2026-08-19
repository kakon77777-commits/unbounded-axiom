# GVSS-06 — Diagnostic Visual Control and Minimal Intervention Policies
## 診斷式視覺控制與最小介入策略：失敗信念、資訊價值、澄清行動與分層控制成本

**Series:** Global Visual Space & Generative Navigation — Paper 06  
**Bridge:** GVSS × frozen Reflexive Representation Theory (RRT)  
**Author:** Neo.K / EveMissLab  
**Version:** v0.1  
**Date:** 2026-08-17  
**Status:** Formal diagnostic-control paper. Controlled belief-state recursion, finite-horizon Bellman control, budget monotonicity, one-step value-of-diagnosis, perfect-information thresholds, human-clarification thresholds, repeated-cheap-versus-decisive diagnostic dominance, stopping optimality, posterior robustness under learned diagnostic likelihood error, finite-horizon policy-regret bounds, and myopic-action counterexamples are proved under the stated hypotheses. POMDP belief control, Bayesian value of information, Blackwell experiment comparison, sequential Bayesian experimental design, active visual reasoning, clarification policies, and state-aware agentic image generation are established neighboring work and are not claimed as GVSS inventions. No strong novelty claim is made.

**Keywords:** diagnostic visual control, value of information, POMDP, visual generation agent, failure belief, human clarification, evaluator calibration, minimal intervention, text-to-image control, GVSS, reflexive visual navigation

---

# Abstract

GVSS-05 introduced a latent visual failure state

$$
\boxed{
F_t
\in
\mathcal F
=
\{
F_{\mathrm{sample}},
F_{\mathrm{constraint}},
F_{\mathrm{compile}},
F_{\mathrm{search}},
F_{\mathrm{reach}},
F_{\mathrm{eval}},
F_{\mathrm{intent}}
\}
}
$$

and a posterior failure belief

$$
\boxed{
b_t(k)
=
P(F_t=F_k\mid H_t).
}
$$

It also defined one-step posterior action risk

$$
\boxed{
\rho_t(a)
=
c(a)
+
\sum_k b_t(k)L(a,k),
}
$$

together with a **least-cost justified intervention** heuristic.

GVSS-06 replaces that myopic heuristic with sequential belief-space control.

The controller must choose among actions with different roles:

$$
\boxed{
\mathcal A
=
\mathcal A_{\mathrm{diag}}
\cup
\mathcal A_{\mathrm{correct}}
\cup
\mathcal A_{\mathrm{clarify}}
\cup
\{\mathrm{STOP}\}.
}
$$

Examples include:

- independent reroll;
- evaluator calibration;
- alternate evaluator;
- alternate search policy;
- RECOMPILE;
- REPAIR;
- REBIND;
- SWITCH_BACKEND;
- HUMAN_REVIEW;
- human clarification question;
- STOP.

An action can change the hidden failure state.

Let

$$
\boxed{
T_a(k'\mid k)
=
P(
F_{t+1}=F_{k'}
\mid
F_t=F_k,
a_t=a
)
}
$$

be the failure-transition kernel.

After taking action $a$, the predicted failure belief is

$$
\boxed{
\bar b^a(k')
=
\sum_k
T_a(k'\mid k)b(k).
}
$$

The action can then produce diagnostic report

$$
Y\sim Q_a(\cdot\mid F_{t+1}).
$$

Bayesian correction gives

$$
\boxed{
b^{a,y}(k')
=
\frac{
Q_a(y\mid k')\bar b^a(k')
}{
\sum_j
Q_a(y\mid j)\bar b^a(j)
}.
}
$$

This is the controlled failure-belief recursion.

Let

$$
B
$$

be remaining visual-control budget.

For finite horizon, define Bellman value

$$
\boxed{
V_t(b,B)
=
\min_{
a:
c(a)\le B
}
\left\{
c(a)
+
\ell(b,a)
+
\mathbb E_{
Y\mid b,a
}
V_{t+1}
(
b^{a,Y},
B-c(a)
)
\right\}.
}
$$

A STOP action terminates with current terminal correction/acceptance risk

$$
\boxed{
R(b)
=
\min_u
\sum_k
b(k)L(u,k).
}
$$

This gives the central GVSS-06 decision rule:

$$
\boxed{
\text{diagnose}
\vee
\text{correct}
\vee
\text{clarify}
\vee
\text{stop}
}
$$

as a function of belief, future value, and budget.

The first major theorem isolates the one-step value of diagnosis.

Suppose diagnostic action $d$:

- does not itself change the failure state;
- produces report $Y$ ;
- is followed immediately by the best terminal correction.

Then its total risk is

$$
\boxed{
J_d(b)
=
c(d)
+
\mathbb E_Y R(b^Y).
}
$$

Its **value of diagnosis** is

$$
\boxed{
\operatorname{VoD}(d\mid b)
=
R(b)
-
\mathbb E_YR(b^Y)
-
c(d).
}
$$

Therefore:

$$
\boxed{
d
\text{ is better than immediate terminal correction}
\iff
\operatorname{VoD}(d\mid b)>0.
}
$$

More information is useful only through the downstream decision it improves.

For a perfect diagnostic that reveals the exact failure state, define the expected value of perfect failure information

$$
\boxed{
\operatorname{EVPI}(b)
=
R(b)
-
\sum_k
b(k)
\min_u
L(u,k).
}
$$

A perfect diagnostic of cost $c_*$ is worth taking before terminal correction exactly when

$$
\boxed{
c_*
<
\operatorname{EVPI}(b).
}
$$

This yields a clean human-clarification threshold.

Consider two unresolved intents

$$
\theta_1,\theta_2
$$

with posterior

$$
p,
\quad
1-p.
$$

Suppose each intent has its own zero-loss correction, while applying the wrong correction incurs loss $L>0$.

Without clarification, optimal expected correction loss is

$$
\boxed{
L\min(p,1-p).
}
$$

If a human clarification query perfectly reveals the intended interpretation and costs $c_H$, then asking the human is optimal before correction exactly when

$$
\boxed{
c_H
<
L\min(p,1-p).
}
$$

Thus human clarification is not a last-resort social feature.

It is a value-of-information action whose worth depends on ambiguity, consequence, and cost.

This is closely aligned with current interactive multimodal work that explicitly learns when to clarify ambiguous visual questions and with progressive image-generation systems that use co-adaptive dialogue to reduce prompt ambiguity.

GVSS-06 also proves when one expensive decisive diagnostic dominates repeated cheap tests.

Let $D_c^{\otimes n}$ denote $n$ fixed cheap diagnostic tests, each costing $c_c$.

Let $D_*$ be a decisive diagnostic experiment such that

$$
\boxed{
D_*
\succeq_B
D_c^{\otimes n}
}
$$

in Blackwell order.

If

$$
\boxed{
c_*
\le
n c_c,
}
$$

then for every bounded terminal decision problem:

$$
\boxed{
\text{decisive-test total Bayes risk}
\le
\text{fixed-}n\text{ cheap-test total Bayes risk}.
}
$$

This theorem does not cover a sequential cheap-test policy that can stop early.

The correct comparison must include the whole adaptive policy.

The paper also provides a stopping theorem.

Let:

$$
R(b)
$$

be the cost of stopping now.

For every feasible continuation action $a$, let:

$$
Q_t(b,B,a)
$$

be its Bellman action value.

Then:

$$
\boxed{
\mathrm{STOP}
\text{ is optimal}
\iff
R(b)
\le
Q_t(b,B,a)
\quad
\forall a\neq\mathrm{STOP}.
}
$$

A controller should stop when no available diagnostic/corrective action has positive net future value.

This prevents infinite diagnostic loops just as GVSS-05 prevented infinite reroll loops.

GVSS-06 also corrects a limitation of the GVSS-05 **least-cost justified intervention**.

Suppose:

$$
P(F_1)=P(F_2)=1/2.
$$

There are two zero-cost correction actions $u_1,u_2$.

Each has zero loss on its matching failure and loss $100$ on the other.

With justification threshold $\eta=1/2$, both corrections are immediately justified and have zero action cost.

A myopic least-cost rule may choose one and incur expected loss:

$$
50.
$$

But a perfect diagnostic costing $1$ reveals which correction is appropriate, giving total expected loss:

$$
1.
$$

Therefore:

$$
\boxed{
\text{least-cost currently justified correction}
\not\Rightarrow
\text{optimal sequential control}.
}
$$

Information acquisition can dominate immediate intervention.

Online diagnostic learning introduces another RRT-style conditioning issue.

Let true diagnostic likelihood for observed report $y$ be

$$
q_k
=
Q(y\mid F_k),
$$

and learned approximation

$$
\widehat q_k.
$$

For prior $b$, assume weighted likelihood error

$$
\boxed{
\sum_k
b(k)
|
q_k-\widehat q_k
|
\le
\varepsilon.
}
$$

Let true evidence probability be

$$
\boxed{
Z
=
\sum_k
b(k)q_k
\ge
\zeta>0.
}
$$

If $\varepsilon<\zeta$, then the true and approximate posteriors satisfy

$$
\boxed{
\operatorname{TV}
(
b^y,
\widehat b^y
)
\le
\frac{
\varepsilon
}{
\zeta
}.
}
$$

Thus diagnostic-likelihood error is amplified by inverse evidence probability.

Rare reports can produce unstable posterior updates even when average likelihood error is small.

This is the diagnostic-control analogue of RRT conditioning debt.

Finally, GVSS-06 gives a finite-horizon diagnostic-regret theorem.

Let:

$$
V_t
$$

be optimal Bellman value.

Suppose implemented policy $\pi$ chooses an action whose optimal Bellman $Q$ -value satisfies

$$
\boxed{
Q_t(
b,\pi_t(b)
)
\le
V_t(b)
+
\epsilon_t
}
$$

for every reachable belief.

Then its finite-horizon excess expected cost satisfies

$$
\boxed{
V_t^\pi(b)
-
V_t(b)
\le
\sum_{s=t}^{T-1}
\epsilon_s.
}
$$

Therefore locally approximate diagnostic decisions accumulate at most additively under the stated finite-horizon model.

The central GVSS-06 principle is:

$$
\boxed{
\textbf{
Visual control should spend information only when the expected reduction in future correction risk exceeds the cost of acquiring that information.
}
}
$$

---

# 1. From diagnosis to control

GVSS-05 answers:

> Which failure layer is plausible?

GVSS-06 answers:

> Given uncertainty over failure layers, what should the controller do next?

The difference is fundamental.

A posterior belief is not yet a policy.

---

# 2. Current neighboring research

Modern agentic image generation already treats multi-turn generation as a state-dependent action problem.

Generation Navigator explicitly reformulates image generation as state-conditioned action making and trains a controller to adapt actions to an evolving generation trajectory.

GenAgent uses multimodal reasoning, tool invocation, judgment, reflection, and multi-turn refinement.

Twin-Co uses co-adaptive dialogue with the user to reduce ambiguity in image-generation prompts.

These systems demonstrate that dynamic action selection and human interaction are already active research directions.

GVSS-06 does not claim state-aware agentic image control as new.

---

# 3. Sequential information acquisition precedent

Active visual reasoning work in 2026 formulates visual information acquisition as sequential Bayesian optimal experimental design.

The agent decides which evidence is worth acquiring before committing to an answer.

This is mathematically close to GVSS-06's diagnostic-control layer.

GVSS specializes the hidden state to **visual generation failure causes** and the downstream decision to **visual corrective actions**.

---

# 4. Clarification precedent

Current multimodal-agent research explicitly studies whether an agent should clarify an ambiguous request rather than answer immediately.

Clarify-or-Answer introduces a dataset and policy-learning setup for choosing clarification questions when visual context is ambiguous.

Twin-Co applies iterative user dialogue directly to progressive image generation.

Therefore GVSS-06's clarification action is not claimed as a new interaction paradigm.

---

# 5. Evaluator uncertainty precedent

VLM Judges Can Rank but Cannot Score studies conformal uncertainty for multimodal judges and finds strongly task-dependent uncertainty.

Calibrating MLLM-as-a-judge via Multimodal Bayesian Prompt Ensembles studies calibration specifically for TTI evaluation.

GVSS-06 uses these as evidence that evaluator state should include uncertainty/calibration rather than treating judge scores as exact.

---

# 6. Controlled failure state

## Definition GVSS06-D1

Let:

$$
F_t
\in
\mathcal F.
$$

An action:

$$
a_t
$$

can change the failure state through:

$$
\boxed{
T_a(k'\mid k).
}
$$

Examples:

### RESAMPLE

May preserve the dominant structural failure state but refresh stochastic sample state.

### RECOMPILE

May convert:

$$
F_{\mathrm{compile}}
$$

into:

$$
F_{\mathrm{sample}}
$$

if the new compiler succeeds but a new stochastic draw is still needed.

### REPAIR

May remove a local artifact while leaving style or intent ambiguity.

### REBIND

May remove provider reachability failure while injecting switching/style-consistency risk.

### HUMAN_CLARIFY

May remove intent ambiguity without changing generator capability.

---

# 7. Predictive belief after action

## Definition GVSS06-D2

Before observing the action result:

$$
\boxed{
\bar b^a(k')
=
\sum_k
T_a(k'\mid k)b(k).
}
$$

This is the action-predicted failure belief.

---

# 8. Diagnostic report model

Let:

$$
Q_a(y\mid k')
$$

be the report likelihood after action $a$ if the post-action failure state is $F_{k'}$.

---

# 9. GVSS06-T1 — Controlled belief update

## Theorem GVSS06-T1

Given prior belief $b$, action transition $T_a$, and observation likelihood $Q_a$, the posterior after action $a$ and report $y$ is:

$$
\boxed{
b^{a,y}(k')
=
\frac{
Q_a(y\mid k')
\sum_kT_a(k'\mid k)b(k)
}{
\sum_j
Q_a(y\mid j)
\sum_kT_a(j\mid k)b(k)
}.
}
$$

whenever the denominator is positive.

### Proof

Predict with the transition kernel, then condition by Bayes' rule.

 $\square$

This is the standard controlled hidden-state belief update.

---

# 10. Belief-state sufficiency

Under the Markov failure model and known kernels, the full diagnostic history can be compressed into:

$$
\boxed{
(b_t,B_t,r_t)
}
$$

for optimal control, provided the visual regime coordinates needed to determine future kernels are included in $r_t$.

This is the standard POMDP sufficient-statistic principle.

---

# 11. GVSS06-T2 — Belief-state dynamic programming

## Theorem GVSS06-T2

Under finite hidden state/action/observation spaces, known controlled kernels, additive stage costs, and finite horizon, an optimal history-dependent policy can be represented as a policy on current belief and remaining budget:

$$
\boxed{
a_t
=
\pi_t^*(b_t,B_t,r_t).
}
$$

### Reason

The conditional law of future hidden states and reports depends on past history only through the current controlled belief and regime state.

This is classical POMDP theory.

GVSS does not claim the theorem as new.

---

# 12. Budget state

Let:

$$
\boxed{
B_t\ge0
}
$$

be remaining diagnostic/control budget.

Action $a$ is feasible when:

$$
\boxed{
c(a)\le B_t.
}
$$

Update:

$$
\boxed{
B_{t+1}
=
B_t-c(a_t).
}
$$

---

# 13. Terminal decision

Let:

$$
u
\in
\mathcal U
$$

be a terminal corrective decision.

Examples:

- ACCEPT;
- RESAMPLE;
- final RECOMPILE;
- final REPAIR;
- final REBIND;
- human handoff.

Let:

$$
\boxed{
L(u,k)
}
$$

be terminal loss if failure is $F_k$.

---

# 14. Terminal Bayes risk

## Definition GVSS06-D3

$$
\boxed{
R(b)
=
\min_{
u\in\mathcal U
}
\sum_k
b(k)L(u,k).
}
$$

This is the risk of stopping information acquisition and making the best current terminal decision.

---

# 15. Finite-horizon Bellman equation

## Definition GVSS06-D4

For $t<T$:

$$
\boxed{
V_t(b,B,r)
=
\min_{
a:
c(a)\le B
}
Q_t(b,B,r,a),
}
$$

where:

$$
\boxed{
Q_t
=
c(a)
+
\ell(b,r,a)
+
\mathbb E_Y
V_{t+1}
(
b^{a,Y},
B-c(a),
r'
).
}
$$

At terminal horizon:

$$
\boxed{
V_T(b,B,r)
=
R(b).
}
$$

The STOP action can be included at every time with:

$$
Q_t(\mathrm{STOP})
=
R(b).
$$

---

# 16. Pure diagnostic action

A pure diagnostic action $d$ has:

$$
\boxed{
T_d
=
I.
}
$$

It does not itself correct the failure state.

It changes only the belief through the observation.

Examples:

- evaluator calibration;
- second evaluator;
- human clarification;
- provider probe;
- anchor test.

---

# 17. Pure corrective action

A pure correction can change the hidden failure state while producing no useful diagnostic report.

Examples:

- blind REPAIR;
- fixed RECOMPILE;
- forced REBIND.

Real actions can combine both roles.

---

# 18. Diagnose-then-act one-step problem

Consider one diagnostic step followed by terminal correction.

Current immediate terminal risk is:

$$
R(b).
$$

After diagnostic $d$ and report $Y$:

$$
R(b^Y).
$$

---

# 19. Value of diagnosis

## Definition GVSS06-D5

$$
\boxed{
\operatorname{VoD}(d\mid b)
=
R(b)
-
\mathbb E_YR(b^Y)
-
c(d).
}
$$

---

# 20. GVSS06-T3 — One-step value-of-diagnosis theorem

## Theorem GVSS06-T3

In the one-diagnostic-step problem, taking diagnostic action $d$ before terminal correction is strictly better than correcting immediately if and only if:

$$
\boxed{
\operatorname{VoD}(d\mid b)>0.
}
$$

It is indifferent when the value is zero.

### Proof

Immediate correction costs:

$$
R(b).
$$

Diagnose-then-correct costs:

$$
c(d)
+
\mathbb E_YR(b^Y).
$$

Compare the two quantities.

 $\square$

---

# 21. Information has instrumental value

In this formulation, uncertainty reduction has no automatic intrinsic reward.

It is valuable only if it changes downstream correction risk enough to justify its cost.

This is standard POMDP/value-of-information logic.

---

# 22. Expected value of perfect information

Assume a perfect diagnostic reveals $F$ exactly.

After observing $F_k$, optimal terminal loss is:

$$
\min_uL(u,k).
$$

---

# 23. Definition of EVPI

$$
\boxed{
\operatorname{EVPI}(b)
=
R(b)
-
\sum_k
b(k)
\min_u
L(u,k).
}
$$

---

# 24. GVSS06-T4 — Perfect-diagnostic threshold

## Theorem GVSS06-T4

A perfect diagnostic of cost $c_*$ followed by optimal correction is better than immediate correction if and only if:

$$
\boxed{
c_*
<
\operatorname{EVPI}(b).
}
$$

### Proof

Perfect-diagnostic total risk is:

$$
c_*
+
\sum_k
b(k)\min_uL(u,k).
$$

Compare with $R(b)$.

 $\square$

EVPI is the maximum amount worth paying for perfect failure information in the one-step decision problem.

---

# 25. EVPI is zero when diagnosis cannot change action

If one terminal action $u^*$ is optimal for every failure state with positive posterior mass, then:

$$
R(b)
=
\sum_k
b(k)L(u^*,k)
=
\sum_k
b(k)\min_uL(u,k),
$$

so:

$$
\boxed{
\operatorname{EVPI}(b)=0.
}
$$

No diagnosis can improve the terminal decision.

---

# 26. GVSS06-C1 — No-decision-change information has no terminal value

If the same terminal action is optimal under every posterior report reachable from diagnostic $d$, then:

$$
\boxed{
R(b)
=
\mathbb E R(b^Y)
}
$$

for the decision problem, and:

$$
\boxed{
\operatorname{VoD}(d\mid b)
=
-c(d)
\le0.
}
$$

A diagnostic that cannot change the decision is not worth positive cost in the one-step model.

---

# 27. Human clarification as diagnosis

Let two latent intents be:

$$
\theta_1,
\theta_2.
$$

Posterior:

$$
p,
1-p.
$$

Correct action for intent $\theta_i$ is $u_i$.

---

# 28. Symmetric wrong-action loss model

Assume:

$$
L(u_1,\theta_1)=0,
$$

$$
L(u_2,\theta_2)=0,
$$

and:

$$
L(u_1,\theta_2)
=
L(u_2,\theta_1)
=
L>0.
$$

---

# 29. GVSS06-T5 — Perfect human-clarification threshold

## Theorem GVSS06-T5

Without clarification, optimal expected loss is:

$$
\boxed{
L\min(p,1-p).
}
$$

If a human clarification query perfectly reveals the true intent and costs $c_H$, then asking before correction is optimal if and only if:

$$
\boxed{
c_H
<
L\min(p,1-p).
}
$$

### Proof

Without clarification choose the more probable intent's action.

Wrong-action probability is:

$$
\min(p,1-p).
$$

Clarification eliminates wrong-action loss and adds cost $c_H$.

 $\square$

---

# 30. Clarification is consequence sensitive

If wrong visual interpretation has trivial cost, clarification may not be worthwhile.

If wrong interpretation destroys an expensive project asset or causes many downstream iterations, the same ambiguity can justify human input.

Thus the threshold depends on:

$$
\boxed{
\text{ambiguity}
\times
\text{consequence}
}
$$

relative to human-review cost.

---

# 31. Automated diagnostic equivalence

GVSS-05 showed that two intent states can be equivalent under all automated diagnostics.

More automated calls then cannot distinguish them.

A human query has value when it creates a new experiment that splits this equivalence class.

---

# 32. GVSS06-N1 — Compute cannot break an unchanged diagnostic equivalence class

If two intent/failure hypotheses have identical observation laws under every automated action allowed by the controller, then increasing the number of those actions does not create identifiability.

A new action with a different observation law is required.

This is inherited from GVSS-05 diagnostic equivalence.

---

# 33. Cheap repeated diagnostics

Suppose cheap diagnostic experiment:

$$
D_c
$$

costs:

$$
c_c.
$$

A fixed bundle of $n$ independent cheap tests is:

$$
\boxed{
D_c^{\otimes n}.
}
$$

Total diagnostic cost:

$$
\boxed{
n c_c.
}
$$

---

# 34. Decisive diagnostic

Let:

$$
D_*
$$

be another diagnostic experiment.

Assume:

$$
\boxed{
D_*
\succeq_B
D_c^{\otimes n}.
}
$$

This means all reports available from the $n$ cheap tests can be statistically simulated from the decisive diagnostic.

---

# 35. GVSS06-T6 — Decisive versus fixed repeated diagnostics

## Theorem GVSS06-T6

If:

$$
D_*
\succeq_B
D_c^{\otimes n}
$$

and:

$$
\boxed{
c_*
\le
n c_c,
}
$$

then for every bounded terminal decision loss, the minimum total expected cost of:

> decisive diagnostic $D_*$ then decide

is no larger than:

> run all $n$ cheap diagnostics then decide.

### Proof

Blackwell dominance implies terminal Bayes decision risk after $D_*$ is no greater than after $D_c^{\otimes n}$.

Diagnostic cost is also no greater.

Add the two components.

 $\square$

---

# 36. Sequential cheap tests are different

A cheap-test controller can:

- stop after one decisive observation;
- continue only when uncertain;
- change diagnostics.

Therefore GVSS06-T6 does not imply one expensive test dominates an **adaptive** cheap-testing policy.

The full Bellman comparison is required.

---

# 37. Repeated cheap diagnostics can still be optimal

If cheap tests often resolve uncertainty after one or two observations, their expected stopping cost can be much lower than the fixed $n c_c$ bundle.

This is a sequential-testing effect.

---

# 38. Stop action

STOP means:

- no further diagnostic/control spending;
- execute current terminal decision or accept/handoff current result.

Its cost is:

$$
\boxed{
R(b).
}
$$

---

# 39. GVSS06-T7 — Bellman stopping theorem

## Theorem GVSS06-T7

At state $(b,B,r)$, STOP is optimal if and only if:

$$
\boxed{
R(b)
\le
Q_t(b,B,r,a)
}
$$

for every feasible non-STOP action $a$.

### Proof

Bellman value is the minimum over STOP and all continuation actions.

 $\square$

---

# 40. Canonical stopping principle

$$
\boxed{
\textbf{
Stop when every available diagnostic or correction has expected future value no greater than its total cost.
}
}
$$

This is stronger than a fixed iteration cap, although hard caps remain useful.

---

# 41. Budget monotonicity

More available budget expands the feasible policy set if unused budget may be ignored.

---

# 42. GVSS06-T8 — Diagnostic-control budget monotonicity

## Theorem GVSS06-T8

If:

$$
B_1\le B_2
$$

and every policy feasible under $B_1$ remains feasible under $B_2$, then:

$$
\boxed{
V_t(b,B_2,r)
\le
V_t(b,B_1,r)
}
$$

for the cost-minimization problem.

### Proof

The minimization at budget $B_2$ is over a superset of policies/actions.

 $\square$

More budget cannot worsen the optimal achievable value.

A bad controller can still waste it.

---

# 43. Direct correction versus diagnosis

Suppose direct correction action $u$ has expected cost:

$$
\boxed{
J_{\mathrm{direct}}(u)
=
c(u)
+
\sum_k
b(k)L(u,k).
}
$$

Diagnosis is worthwhile only if its downstream reduction beats its cost.

---

# 44. Myopic least-cost justified rule

GVSS-05 defined:

$$
a^{\mathrm{LCJ}}
\in
\arg\min_{
a:
b(S_a)\ge\eta
}
c(a).
$$

It ignores:

- wrong-layer consequences;
- future information;
- state transition;
- future action opportunities.

---

# 45. GVSS06-N2 — Least-cost justified correction can be sequentially suboptimal

## Counterexample

Let:

$$
b(F_1)=b(F_2)=1/2.
$$

Actions:

$$
u_1,u_2
$$

each cost zero.

Loss:

$$
L(u_i,F_i)=0,
$$

$$
L(u_i,F_j)=100
\quad
(i\neq j).
$$

At threshold:

$$
\eta=1/2,
$$

both corrections are justified and cost zero.

Myopic direct correction has expected loss:

$$
\boxed{
50.
}
$$

Now add perfect diagnostic:

$$
d
$$

with cost:

$$
1.
$$

After diagnosis choose the correct zero-loss action.

Total expected loss:

$$
\boxed{
1.
}
$$

Therefore:

$$
\boxed{
\text{least-cost currently justified correction}
\not\Rightarrow
\text{optimal sequential action}.
}
$$

 $\square$

---

# 46. Minimal intervention is not minimum action cost

The correct objective is minimal **expected total cost**, including:

- diagnostic cost;
- correction cost;
- wrong-layer loss;
- future iterations.

A zero-cost wrong intervention can be expensive.

---

# 47. Evaluator calibration as an action

Let:

$$
d_E
$$

be evaluator-calibration action.

It can:

- query anchors;
- obtain conformal interval;
- compare two judges;
- request human reference;
- test position bias.

This does not directly fix the image.

It can change:

$$
b(F_{\mathrm{eval}}).
$$

---

# 48. Value of evaluator calibration

Calibration has value when it changes:

- whether the image is accepted;
- which failure layer is believed;
- whether RECOMPILE/REBIND is triggered;
- whether human review is requested.

If no downstream decision changes, the one-step value is only negative calibration cost.

---

# 49. Conformal uncertainty

Current VLM judge work shows that an absolute judge score can have task-dependent uncertainty.

A runtime can represent evaluator state with:

$$
\boxed{
(\widehat s,\mathcal I_s,\kappa_E)
}
$$

where:

- $\widehat s$ is score/ranking;
- $\mathcal I_s$ is calibrated uncertainty interval;
- $\kappa_E$ is evaluator calibration metadata.

This is an engineering specialization.

---

# 50. Deferral rule

If evaluator uncertainty is too large to determine which action is optimal, a deferral action can:

- acquire another evaluator;
- human-review;
- ask user;
- stop automatic escalation.

This converts uncertainty into policy rather than hiding it.

---

# 51. Human review cost

Let human action cost include:

$$
\boxed{
c_H
=
c_{\mathrm{latency}}
+
c_{\mathrm{attention}}
+
c_{\mathrm{interaction}}.
}
$$

Human input is not free and not infallible.

It competes with automated diagnostics in the same control problem.

---

# 52. Human clarification versus human evaluation

These are distinct actions.

### Human clarification

Queries the latent intent.

### Human evaluation

Judges whether a generated image matches already-known intent.

They produce different diagnostic information.

---

# 53. Current interactive multimodal precedent

Clarify-or-Answer learns when to ask ambiguity-resolving questions in visual question answering.

Twin-Co uses iterative co-adaptive user dialogue to progressively refine image generation.

InteractWeb-Bench includes Clarify as a first-class agent action in ambiguous requirements.

GVSS-06 treats clarification as a general experiment over intent hypotheses.

---

# 54. Current state-aware image-control precedent

Generation Navigator directly formulates image generation as a state-conditioned action-making problem.

Its trajectory objective rewards:

- peak quality;
- retention;
- efficiency.

This strongly overlaps the GVSS concern that an action should improve the trajectory without unnecessary turns or regression.

GVSS-06 adds explicit failure-belief and diagnostic-value semantics.

---

# 55. GenAgent precedent

GenAgent separates multimodal understanding from image-generation tools and performs multi-turn reasoning, generation, judgment, and reflection.

This is another direct precedent for an image-generation controller with tool actions and feedback.

GVSS-06 does not claim tool-using generation agents as new.

---

# 56. Information self-locking warning

Recent active-diagnosis research identifies a coupling between:

- action selection;
- belief tracking.

Weak action selection can starve the belief tracker of informative evidence.

Weak belief tracking can prevent informative actions from receiving credit.

GVSS visual controllers can suffer the same self-locking.

---

# 57. Visual self-locking example

Suppose controller falsely assigns almost all posterior mass to:

$$
F_{\mathrm{sample}}.
$$

It repeatedly RESAMPLEs.

But only a RECOMPILE diagnostic would reveal:

$$
F_{\mathrm{compile}}.
$$

The current belief suppresses the action that could correct the belief.

This is diagnostic self-locking.

---

# 58. Exploration requirement

A robust policy can reserve a small diagnostic exploration budget for actions that test low-probability but high-cost failure hypotheses.

GVSS-06 does not derive an optimal exploration schedule.

---

# 59. Learning diagnostic likelihoods online

The model:

$$
Q_a(y\mid F)
$$

may initially be unknown.

A runtime can learn it from:

- synthetic failure injections;
- historical projects;
- controlled ablations;
- human-labeled failure traces.

But online likelihood error affects belief stability.

---

# 60. Approximate diagnostic likelihood

For one observed report $y$, define:

$$
q_k
=
Q(y\mid F_k),
$$

$$
\widehat q_k
=
\widehat Q(y\mid F_k).
$$

Let:

$$
\boxed{
\varepsilon
=
\sum_k
b(k)
|
q_k-\widehat q_k
|.
}
$$

Let evidence probability:

$$
\boxed{
Z
=
\sum_k
b(k)q_k.
}
$$

---

# 61. GVSS06-T9 — Posterior robustness under likelihood error

## Theorem GVSS06-T9

Assume:

$$
\boxed{
Z\ge\zeta>0
}
$$

and:

$$
\boxed{
\varepsilon<\zeta.
}
$$

Let true posterior:

$$
p_k
=
\frac{
b(k)q_k
}{
Z
},
$$

and approximate posterior:

$$
\widehat p_k
=
\frac{
b(k)\widehat q_k
}{
\widehat Z
}.
$$

Then:

$$
\boxed{
\operatorname{TV}
(
p,\widehat p
)
\le
\frac{
\varepsilon
}{
\zeta
}.
}
$$

### Proof

Let:

$$
a_k=b(k)q_k,
\qquad
\widehat a_k=b(k)\widehat q_k.
$$

Then:

$$
\|a-\widehat a\|_1
\le
\varepsilon,
$$

and:

$$
|Z-\widehat Z|
\le
\varepsilon.
$$

Now:

$$
\begin{aligned}
\|p-\widehat p\|_1
&=
\left\|
\frac aZ
-
\frac{\widehat a}{\widehat Z}
\right\|_1
\\
&\le
\frac{
\|a-\widehat a\|_1
}{
Z
}
+
\widehat Z
\left|
\frac1Z
-
\frac1{\widehat Z}
\right|
\\
&=
\frac{
\|a-\widehat a\|_1
+
|Z-\widehat Z|
}{
Z
}
\\
&\le
\frac{
2\varepsilon
}{
\zeta
}.
\end{aligned}
$$

Total variation is half the $L^1$ distance.

 $\square$

---

# 62. Rare-evidence conditioning debt

When:

$$
\zeta
$$

is small, the posterior bound can be large.

Therefore rare diagnostic observations can make the belief update highly sensitive to likelihood misspecification.

This is a direct visual-diagnosis instance of RRT conditioning debt.

---

# 63. Likelihood learning rule

A learned controller should record:

- amount of diagnostic calibration data;
- uncertainty in $Q$ ;
- evidence probability;
- posterior sensitivity.

Do not expose a high-confidence failure posterior without modeling its diagnostic-likelihood uncertainty.

---

# 64. Robust diagnostic action

If posterior uncertainty is too large, the controller can prefer actions whose decision remains stable over a posterior uncertainty set.

This becomes robust POMDP/control.

GVSS-06 does not solve the general robust problem.

---

# 65. Policy regret

Let:

$$
V_t
$$

be optimal finite-horizon cost.

Let:

$$
V_t^\pi
$$

be expected cost under implemented policy $\pi$.

---

# 66. Approximate Bellman action

Suppose policy chooses action $\pi_t(b)$ satisfying:

$$
\boxed{
Q_t(
b,\pi_t(b)
)
\le
V_t(b)
+
\epsilon_t
}
$$

for all reachable beliefs.

---

# 67. GVSS06-T10 — Finite-horizon diagnostic-regret bound

## Theorem GVSS06-T10

For horizon $T$:

$$
\boxed{
V_t^\pi(b)
-
V_t(b)
\le
\sum_{
s=t
}^{T-1}
\epsilon_s.
}
$$

### Proof

Backward induction.

At final horizon the gap is zero.

Assume the future policy gap from $t+1$ is bounded by the remaining sum.

At time $t$, policy's chosen action has optimal continuation $Q$ at most $\epsilon_t$ above $V_t$.

Replacing optimal future continuation by policy future continuation adds at most the inductive bound.

Add.

 $\square$

This is a generic approximate dynamic-programming bound.

---

# 68. Diagnostic regret can be tracked separately

A runtime can log:

$$
\boxed{
\epsilon_t
}
$$

or an empirical proxy.

This reveals whether unnecessary turns come from:

- poor failure belief;
- poor action-value estimation;
- bad evaluator;
- insufficient action set.

---

# 69. Correction transitions

A correction action can leave residual failure.

For example RECOMPILE transition:

$$
F_{\mathrm{compile}}
\to
\begin{cases}
F_{\mathrm{sample}},&p\\
F_{\mathrm{compile}},&1-p.
\end{cases}
$$

The controller should not assume action success is deterministic.

---

# 70. REBIND transition

A provider switch can convert:

$$
F_{\mathrm{reach}}
$$

to successful/sampling state.

It can also inject:

- style drift;
- reference inconsistency;
- cost increase.

A failure-state model can include these secondary states or represent them in the visual deficit vector.

---

# 71. Diagnose-versus-correct frontier

For each action $a$, track:

$$
\boxed{
(
\operatorname{IG}(a),
\operatorname{CorrectionGain}(a),
c(a),
D_{\mathrm{switch}},
D_{\mathrm{regression}}
).
}
$$

The controller chooses on a multi-axis frontier.

---

# 72. Information gain is not correction gain

A perfect evaluator audit may tell the controller exactly what is wrong but leave the image unchanged.

A local repair may fix the image while revealing almost nothing about global reachability.

Do not conflate the two.

---

# 73. Combined diagnostic-corrective action

Some actions do both.

Example:

> run one alternate-search trajectory.

If it succeeds, it corrects the image and diagnoses search failure.

If it fails, it still supplies evidence about the search/reachability hypotheses.

This dual role is why Bellman control is more appropriate than a fixed diagnosis-then-correction pipeline.

---

# 74. Minimal intervention principle

The final GVSS notion of minimal intervention is:

> choose the action/policy with minimum expected total downstream cost among actions that appropriately trade diagnosis, correction, and stopping.

It is **not**:

> choose the action with the smallest immediate API price.

---

# 75. Minimal intervention under certainty

If belief is degenerate:

$$
b(F_k)=1,
$$

and one action deterministically fixes $F_k$ at lowest cost with no side effects, then diagnosis has zero value and direct correction is optimal.

This is the easy boundary case.

---

# 76. High ambiguity / high consequence

If failure belief is diffuse and wrong-layer correction is costly, information value increases.

This is when:

- evaluator calibration;
- human clarification;
- alternate-policy test;

become attractive.

---

# 77. Low ambiguity / low consequence

If one failure dominates and correction is cheap/reversible, directly correcting can beat further diagnosis.

This is why human review should not be mandatory on every image.

---

# 78. Query the user or not?

The controller should compare:

$$
\boxed{
c_H
}
$$

against expected avoided downstream loss.

The user's time becomes an explicit resource.

---

# 79. Clarification quality

A clarification question can itself be poor.

Let:

$$
Q_H(y\mid\theta)
$$

be human-response model.

A vague question may barely distinguish intents.

A targeted question has larger diagnostic value.

GVSS-06 does not derive optimal natural-language question generation.

---

# 80. Clarification selection as experiment design

Given candidate questions:

$$
q_1,\ldots,q_m,
$$

each defines a statistical experiment over latent intents.

Choose by:

- value of diagnosis;
- expected information gain;
- cost;
- user burden.

This is Bayesian experimental design applied to human-AI interaction.

---

# 81. Current Clarify-or-Answer relevance

Clarify-or-Answer explicitly trains a policy to decide whether to ask a clarification question in agentic VQA.

This supports treating clarification as an action rather than a conversational afterthought.

---

# 82. Twin-Co relevance

Twin-Co applies iterative human dialogue to progressive image generation.

Its existence strongly supports the practical feasibility of human clarification as part of the visual generation loop.

GVSS-06 supplies a cost/value criterion for when such interaction is justified.

---

# 83. Generation Navigator relevance

Generation Navigator is particularly close to GVSS-06 because it treats T2I generation as state-conditioned action making and penalizes wasted turns.

GVSS differs by explicitly separating:

- hidden failure belief;
- information acquisition;
- correction transition;
- stopping.

---

# 84. Active visual reasoning relevance

Sequential Bayesian optimal experimental design for visual reasoning demonstrates a current framework where a VLM chooses what evidence to acquire under perceptual bandwidth limits.

GVSS-06's diagnostic controller uses the same decision-theoretic logic but over visual-generation failure causes.

---

# 85. Evaluator calibration action value

VLM judge uncertainty can be wide on some tasks.

If the current action decision depends on whether a judge score is above a threshold, calibration can have high value.

If all feasible actions are identical regardless of the score interval, calibration has zero decision value.

---

# 86. Diagnostic control benchmark

A benchmark should provide:

- hidden failure state;
- diagnostic action models;
- correction transition models;
- costs;
- terminal losses;
- budget.

Then measure:

$$
\boxed{
\text{policy total expected cost}
}
$$

rather than final image score alone.

---

# 87. Synthetic benchmark 1 — perfect diagnostic threshold

Two equally likely failures.

Wrong repair loss:

$$
100.
$$

Perfect diagnosis cost varies from $0$ to $60$.

Optimal policy should diagnose exactly below:

$$
50.
$$

---

# 88. Synthetic benchmark 2 — clarification threshold

Intent posterior:

$$
p=0.9.
$$

Wrong-intent loss:

$$
L=10.
$$

Clarification value before cost is:

$$
10\times0.1=1.
$$

Ask only if clarification cost is below $1$ in the one-step model.

---

# 89. Synthetic benchmark 3 — evaluator calibration

Two judges have uncertain calibration.

An anchor test changes action choice only near a threshold.

Measure whether controller purchases calibration only when decision-sensitive.

---

# 90. Synthetic benchmark 4 — cheap tests versus decisive test

Cheap test:

- cost $1$ ;
- moderate information.

Decisive test:

- cost variable;
- perfect information.

Compare:

- fixed $n$ cheap tests;
- sequential cheap tests;
- decisive test.

This directly tests GVSS06-T6 boundary.

---

# 91. Synthetic benchmark 5 — self-locking

Initialize posterior incorrectly near:

$$
F_{\mathrm{sample}}.
$$

Only RECOMPILE diagnostic is informative.

Test whether exploration policy can escape repeated rerolling.

---

# 92. Runtime data structure

Suggested state:

```text
failure_belief
failure_transition_model
diagnostic_likelihood_model
diagnostic_likelihood_uncertainty
remaining_budget
action_costs
terminal_loss_matrix
action_value_estimates
diagnostic_regret
human_query_budget
stop_reason
```

---

# 93. Action record

Each action packet should record:

```text
action_type
diagnostic_role
corrective_role
cost
belief_before
belief_after_prediction
observation
belief_after_observation
regime_delta
image_delta
value_estimate
regret_estimate
```

---

# 94. Human query record

```text
question
candidate_intents
expected_value_of_clarification
human_cost
response
posterior_before
posterior_after
```

This makes user interaction part of provenance.

---

# 95. Evaluator calibration record

```text
evaluator_id
calibration_domain
sample_count
error_or_interval
confidence_level
last_calibration_time
decision_thresholds_affected
```

---

# 96. Online diagnostic learning

Update:

$$
\widehat Q_a(y\mid F)
$$

from labeled failure episodes.

Use held-out or synthetic failure injection to prevent the controller from teaching itself a self-confirming diagnostic model.

---

# 97. Self-confirming diagnosis risk

If the controller labels its own failures using its own current belief and then retrains on those labels, it can reinforce an incorrect failure taxonomy.

Ground-truth or independent audits are required.

---

# 98. GVSS06-N3 — Self-labeled diagnostic learning can be self-confirming

If training labels are deterministically set to the controller's current predicted failure state, a learner that fits those labels perfectly receives no evidence that the predictions were wrong.

Thus:

$$
\boxed{
\text{self-consistency}
\not\Rightarrow
\text{diagnostic correctness}.
}
$$

Independent labels or falsification experiments are required.

---

# 99. Diagnostic likelihood provenance

Every learned likelihood model should record:

- dataset;
- failure injection procedure;
- generator versions;
- evaluator versions;
- labeling source;
- calibration error.

This follows RRT provenance discipline.

---

# 100. Visual-control Pareto vector

A full controller can expose:

$$
\boxed{
\mathbf C_{\mathrm{control}}
=
(
V_t,
C_{\mathrm{GPU}},
C_{\mathrm{human}},
C_{\mathrm{switch}},
C_{\mathrm{verify}},
D_{\mathrm{style}},
D_{\mathrm{homog}},
D_{\mathrm{prov}}
).
}
$$

---

# 101. GVSS06-T11 — Control Pareto necessity

## Theorem GVSS06-T11

Every optimum of a scalar objective strictly increasing in all declared control costs/risks and strictly decreasing in all declared benefits lies on the diagnostic-control Pareto frontier.

### Proof

Standard dominance argument.

 $\square$

---

# 102. What is classical / neighboring

GVSS-06 does not claim as inventions:

- POMDP belief-state control;
- Bayesian dynamic programming;
- value of information;
- EVPI;
- Blackwell experiment comparison;
- sequential Bayesian optimal experimental design;
- active diagnosis;
- clarification policies;
- VLM calibration;
- agentic image-generation control.

---

# 103. Candidate GVSS-specific synthesis

Subject to broader literature audit, the GVSS-specific synthesis is:

1. using the GVSS-05 seven-layer visual failure posterior as the hidden state of a visual-control POMDP;
2. separating diagnostic, corrective, clarification, and stop actions in one image-generation controller;
3. deriving explicit perfect-diagnosis and human-clarification cost thresholds for visual failure correction;
4. connecting cheap repeated visual diagnostics and decisive tests through Blackwell dominance;
5. treating the GVSS-05 least-cost justified action as a myopic heuristic and providing an exact sequential counterexample;
6. deriving a posterior-sensitivity bound for learned diagnostic likelihood misspecification;
7. defining finite-horizon diagnostic-control regret;
8. making human time, evaluator calibration, provider switching, and image correction comparable as explicit decision resources.

No strong novelty claim is made in v0.1.

---

# 104. What GVSS-06 proves

Under explicit hypotheses, GVSS-06 proves:

1. the controlled failure posterior update under action-dependent state transitions;
2. finite-horizon belief-state dynamic programming under the standard POMDP assumptions;
3. one-step value of diagnosis equals avoided terminal Bayes risk minus diagnostic cost;
4. a perfect diagnostic is worth buying exactly below EVPI;
5. a perfect two-intent human clarification query is worth buying exactly below the ambiguity-weighted wrong-action loss;
6. a Blackwell-dominating decisive diagnostic with no greater fixed diagnostic cost dominates a fixed bundle of cheap tests;
7. STOP is optimal exactly when no feasible continuation action has lower Bellman cost;
8. optimal value is nonincreasing with available budget;
9. least-cost currently justified correction can be strictly sequentially suboptimal;
10. posterior TV error is bounded by likelihood-model error divided by evidence probability;
11. finite-horizon control regret is bounded by accumulated per-stage Bellman suboptimality;
12. strictly monotone scalar control optima lie on the control Pareto frontier.

---

# 105. What GVSS-06 does not prove

It does not prove:

- the seven-state failure model is complete;
- the controlled transition kernels are known in real T2I systems;
- Bayesian beliefs are calibrated without diagnostic data;
- human clarification is always accurate;
- conformal VLM-judge intervals directly transfer to every image project;
- one-step EVPI is sufficient for long-horizon optimal control;
- Blackwell dominance of one fixed test implies dominance over adaptive sequential testing;
- online likelihood learning is stable without external labels;
- a finite-horizon regret bound implies good real-world visual quality;
- the Bellman controller is computationally tractable for full-scale image-generation state spaces.

---

# 106. Proposed GVSS-07

The next paper should address the largest practical gap in GVSS-06:

> diagnostic kernels and action transitions are not known.

Proposed title:

$$
\boxed{
\textbf{
GVSS-07 — Online Visual System Identification and Diagnostic Model Learning
}
}
$$

Chinese:

**線上視覺系統辨識與診斷模型學習：失敗轉移、評估器校準與反身控制模型更新**

Main questions:

1. How should $Q_a(y\mid F)$ be learned?
2. How should $T_a(F'\mid F)$ be learned?
3. How can synthetic failure injection identify diagnostic models?
4. How should uncertainty in learned diagnostic models alter action selection?
5. Can provider-specific reachability beliefs be learned online?
6. How can self-confirming failure labels be prevented?

---

# 107. References

1. Jinming Liu et al., **Generation Navigator: A State-Aware Agentic Framework for Image Generation**, arXiv:2605.17969, 2026.
2. Kaixun Jiang et al., **GenAgent: Scaling Text-to-Image Generation via Agentic Multimodal Reasoning**, arXiv:2601.18543, 2026.
3. Jianhui Wang et al., **Twin Co-Adaptive Dialogue for Progressive Image Generation**, arXiv:2504.14868, 2025/revised 2026.
4. Anjie Liu et al., **The Perceptual Bandwidth Bottleneck in Vision-Language Models: Active Visual Reasoning via Sequential Experimental Design**, arXiv:2605.01345, 2026.
5. **Clarify or Answer: Reinforcement Learning for Agentic VQA with Ambiguous Visual Context**, arXiv:2601.16400, 2026.
6. Divake Kumar et al., **VLM Judges Can Rank but Cannot Score: Task-Dependent Uncertainty in Multimodal Evaluation**, arXiv:2604.25235, 2026.
7. Eric Slyman et al., **Calibrating MLLM-as-a-judge via Multimodal Bayesian Prompt Ensembles**, arXiv:2509.08777, 2025.
8. **On Information Self-Locking in Reinforcement Learning for Active Diagnosis**, arXiv:2603.12109, 2026.
9. GVSS-01 through GVSS-05, internal series artifacts, 2026.
10. RRT-20, **Reflexive Representation Theory: Unified Closure, Meta-Theorems, Limits, and Research Program**, internal series artifact, 2026.

---

# 108. Conclusion

GVSS-05 made visual failure a latent hypothesis.

GVSS-06 makes failure belief a control state.

The closed loop is now:

$$
\boxed{
b_t
\to
a_t
\to
F_{t+1}
\to
Y_{t+1}
\to
b_{t+1}.
}
$$

The controller can choose:

$$
\boxed{
\text{diagnose}
\vee
\text{correct}
\vee
\text{clarify}
\vee
\text{stop}.
}
$$

Information acquisition is valuable only insofar as it improves later correction decisions enough to repay its cost.

A perfect diagnostic has maximum price:

$$
\boxed{
\operatorname{EVPI}(b).
}
$$

A perfect clarification query for two intents has value:

$$
\boxed{
L\min(p,1-p).
}
$$

A cheap immediate correction can be globally expensive if it targets the wrong failure layer.

A rare diagnostic observation can make a learned likelihood model unstable through the inverse-evidence factor:

$$
\boxed{
\operatorname{TV}
(
b^y,\widehat b^y
)
\le
\varepsilon/\zeta.
}
$$

And a controller should stop when no remaining action has positive net future value.

The canonical GVSS-06 principle is:

$$
\boxed{
\textbf{
Do not buy information because uncertainty is aesthetically uncomfortable.
Buy information when it changes a visual decision enough to justify its cost.
}
}
$$

This completes the transition from failure diagnosis to diagnostic visual control.

---

# Canonical-source policy

This file is the canonical UTF-8 source artifact.

- Canonical inline mathematics uses ` $...$ `.
- Canonical display mathematics uses `$$...$$`.
- No Unicode mathematical-symbol conversion is used as source normalization.
- No `unicode_escape` round trip is used.
- Backslashes and delimiters are preserved literally.
- Validation is required before release.
- This paper does not reopen RRT numbering.
