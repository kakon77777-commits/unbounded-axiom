# GVSS-05 — Visual Failure Stratification and Reachability Diagnosis
## 視覺失敗分層與可達性診斷：從 Seed Failure、Compiler Failure 到 Generator-Boundary Failure

**Series:** Global Visual Space & Generative Navigation — Paper 05  
**Bridge:** GVSS × frozen Reflexive Representation Theory (RRT)  
**Author:** Neo.K / EveMissLab  
**Version:** v0.1  
**Date:** 2026-08-17  
**Status:** Formal diagnosis paper. Bayesian failure-belief recursion, constraint-contradiction immunity, reroll stopping bounds, finite-sample reachability no-go, alternate-policy refutation of hard generator impossibility, evaluator calibration ordering, diagnostic equivalence classes, intent non-identifiability, diagnostic Blackwell dominance, posterior-coverage action selection, and diagnostic regret are proved under the stated hypotheses. VLM criticism, iterative prompt refinement, evaluator benchmarking, test-time scaling, agentic image repair, and active failure diagnosis are established neighboring directions and are not claimed as GVSS inventions. No strong novelty claim is made.

**Keywords:** visual failure diagnosis, text-to-image generation, reachability diagnosis, seed failure, prompt compilation, evaluator failure, VLM judge, test-time refinement, Bayesian diagnosis, closed-loop image generation, GVSS, Reflexive Visual Navigation

---

# Abstract

GVSS-04 formalized Reflexive Visual Navigation through a visual regime

$$
\boxed{
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
}
$$

and separated the actions

$$
\boxed{
\text{RESAMPLE}
\neq
\text{RECOMPILE}
\neq
\text{REBIND}.
}
$$

GVSS-05 asks the diagnostic question that must precede those actions:

> **When an image fails, at which layer did the failure occur?**

The paper introduces a latent failure variable

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
\}.
}
$$

The meanings are:

- $F_{\mathrm{sample}}$: the current stochastic draw/seed failed although the current regime retains adequate success probability;
- $F_{\mathrm{constraint}}$: the compiled hard constraints are internally inconsistent or define an empty target;
- $F_{\mathrm{compile}}$: the human intent has been incorrectly or incompletely represented by the current constraint program;
- $F_{\mathrm{search}}$: the current search/refinement policy fails to find a reachable target despite the generator binding being capable;
- $F_{\mathrm{reach}}$: the current generator/provider binding does not reach the declared target domain under the chosen reachability semantics;
- $F_{\mathrm{eval}}$: the evaluator/observer mismeasures or misclassifies the visual state;
- $F_{\mathrm{intent}}$: the underlying user intent is itself ambiguous, incomplete, or mutually incompatible.

Maintain a posterior failure belief

$$
\boxed{
b_t(k)
=
\Pr(
F_t=F_k
\mid
H_t
).
}
$$

A diagnostic action

$$
d_t
$$

can be:

- another independent reroll;
- an alternate search policy;
- a recompiled constraint program;
- a second evaluator;
- a gold/anchor evaluator test;
- a provider rebind;
- a human clarification query.

The diagnostic observation law is

$$
\boxed{
Q_d(y\mid F_k,H_t).
}
$$

When the failure state is static during the diagnostic episode and the model is correctly specified, Bayesian updating gives

$$
\boxed{
b_{t+1}(k)
=
\frac{
Q_{d_t}(y_{t+1}\mid F_k,H_t)
b_t(k)
}{
\sum_j
Q_{d_t}(y_{t+1}\mid F_j,H_t)
b_t(j)
}.
}
$$

This provides the general diagnosis layer.

The first exact visual theorem concerns contradictory constraints.

If hard constraint sets are

$$
A_1,\ldots,A_m
\subseteq
\Omega_\Sigma
$$

and

$$
\boxed{
\bigcap_{i=1}^m A_i
=
\varnothing,
}
$$

then for every generator binding $\mathsf G$,

$$
\boxed{
\mathcal R(\mathsf G)
\cap
\bigcap_iA_i
=
\varnothing.
}
$$

Therefore no amount of RESAMPLE or REBIND can satisfy an empty hard target set.

The constraint representation must first be repaired, relaxed, or clarified.

The next theorem gives an explicit **reroll stopping rule**.

Suppose under the null hypothesis

$$
H_{\mathrm{seed}}(p_0)
$$

the current fixed regime has conditional probability of producing an acceptable independent reroll of at least

$$
p_0>0
$$

at every attempt.

Then the probability of observing $n$ consecutive failures is at most

$$
\boxed{
(1-p_0)^n.
}
$$

Hence after $n$ consecutive failures, the hypothesis that the system is merely suffering ordinary seed failure with success probability at least $p_0$ can be rejected at level $\alpha$ whenever

$$
\boxed{
(1-p_0)^n
\le
\alpha.
}
$$

Equivalently,

$$
\boxed{
n
\ge
\frac{
\log\alpha
}{
\log(1-p_0)
}.
}
$$

After $n$ failures and no successes, an exact one-sided confidence statement is

$$
\boxed{
p
<
1-\alpha^{1/n}
}
$$

at confidence level $1-\alpha$ in the repeated independent Bernoulli model.

This is a practical mathematical answer to:

> **When should rerolling stop?**

But the theorem has an equally important no-go.

Without a lower-bound hypothesis such as $p\ge p_0$, no finite number of failures can establish

$$
p=0.
$$

For every finite $n$ and every $\epsilon>0$,

$$
\boxed{
(1-\epsilon)^n>0.
}
$$

Therefore arbitrarily many but finite bad seeds remain compatible with a very small nonzero success probability.

Thus:

$$
\boxed{
\text{finite stochastic failure}
\not\Rightarrow
\text{generator unreachability}.
}
$$

The paper also separates **search failure** from **hard generator reachability failure**.

Suppose two policies $\Pi_1$ and $\Pi_2$ operate under the same generator binding $\mathsf G$ and the same accepted target set $\mathcal A(C)$.

If $\Pi_2$ produces some acceptable image

$$
I^*
\in
\mathcal A(C)
$$

under the same binding, then:

$$
\boxed{
I^*
\in
\mathcal R(\mathsf G)
\cap
\mathcal A(C),
}
$$

so the hard hypothesis

$$
\mathcal R(\mathsf G)
\cap
\mathcal A(C)
=
\varnothing
$$

is false.

Failure under $\Pi_1$ therefore cannot be used as evidence of absolute binding unreachability once $\Pi_2$ succeeds.

This is a policy-diagnosis theorem:

$$
\boxed{
\text{alternate-policy success}
\Longrightarrow
\text{not hard generator-boundary failure}.
}
$$

It does **not** prove that $\Pi_1$ is globally bad; it proves only that the target was reachable under the same binding.

Evaluator failure receives a separate diagnostic layer.

Let evaluator $E_j$ be tested on $m$ independently sampled anchor items with known gold decisions.

Let:

$$
\widehat e_j
$$

be empirical error rate and:

$$
e_j
$$

true anchor-distribution error rate.

Hoeffding gives, simultaneously for two evaluators with probability at least $1-\delta$,

$$
\boxed{
|e_j-\widehat e_j|
\le
r_m(\delta)
=
\sqrt{
\frac{
\log(4/\delta)
}{
2m
}
}.
}
$$

Therefore if:

$$
\boxed{
\widehat e_1
+
r_m(\delta)
<
\widehat e_2
-
r_m(\delta),
}
$$

then with probability at least $1-\delta$:

$$
\boxed{
e_1<e_2.
}
$$

This provides a calibrated reason to distrust one evaluator more than another.

Raw evaluator disagreement alone is insufficient.

Two evaluators can disagree because:

- one is biased;
- both are uncertain;
- the image is genuinely ambiguous;
- the prompt is underspecified;
- one evaluator uses a different interpretation of intent.

Therefore:

$$
\boxed{
\text{evaluator disagreement}
\not\Rightarrow
\text{evaluator failure}.
}
$$

A calibrated diagnostic experiment is required.

The paper introduces **diagnostic equivalence**.

For available diagnostic action set $\mathcal D$, define two failure hypotheses as equivalent when:

$$
\boxed{
F_i
\sim_{\mathcal D}
F_j
}
$$

if:

$$
Q_d(\cdot\mid F_i)
=
Q_d(\cdot\mid F_j)
$$

for every:

$$
d\in\mathcal D.
$$

If two hypotheses are diagnostically equivalent, then no adaptive diagnostic policy using only actions from $\mathcal D$ can distinguish them.

In particular, their posterior odds remain equal to prior odds:

$$
\boxed{
\frac{
b_t(i)
}{
b_t(j)
}
=
\frac{
b_0(i)
}{
b_0(j)
}
}
$$

whenever the ratio is well defined.

This gives an exact criterion for when a new observer, human query, or diagnostic action is necessary.

The same idea applies to intent ambiguity.

If two latent user intents produce:

- the same input utterance;
- the same evaluator reports;
- the same outputs under every available non-human diagnostic action;

then the controller cannot infer which intent is correct.

A clarification query that produces different response laws is required to split the intent equivalence class.

Thus:

$$
\boxed{
\text{more generation compute}
\not\Rightarrow
\text{resolution of intent ambiguity}.
}
$$

Diagnostic actions themselves can be compared.

If diagnostic experiment $D_a$ Blackwell-dominates $D_b$ and costs no more,

$$
\boxed{
D_a
\succeq_B
D_b,
\qquad
c(a)\le c(b),
}
$$

then for every bounded decision loss over failure states, action $a$ is never worse than $b$ in Bayes risk plus diagnostic cost.

This is classical statistical-experiment comparison applied to visual failure diagnosis.

GVSS-05 therefore defines a **diagnostic policy** independently of final image quality.

Let action loss under true failure $F_k$ be

$$
L(a,k),
$$

including:

- wasted compute;
- unnecessary provider switch;
- prompt corruption;
- style drift;
- human-review cost;
- failure to fix the true layer.

The posterior expected one-step diagnostic risk is

$$
\boxed{
\rho_t(a)
=
c(a)
+
\sum_k
b_t(k)L(a,k).
}
$$

The Bayes diagnostic action is

$$
\boxed{
a_t^*
\in
\operatorname*{arg\,min}_a
\rho_t(a).
}
$$

Diagnostic regret of an implemented action $a_t$ is

$$
\boxed{
\operatorname{Reg}_t
=
\rho_t(a_t)
-
\min_a\rho_t(a).
}
$$

This can be measured even before final image quality is known.

Finally, define the **correctable failure set** of an action $a$:

$$
\boxed{
S_a
\subseteq
\mathcal F.
}
$$

For confidence threshold $\eta\in(0,1)$, call action $a$ **$\eta$ -justified** when

$$
\boxed{
b_t(S_a)
=
\sum_{F_k\in S_a}
b_t(k)
\ge
\eta.
}
$$

The **least-cost justified intervention** is:

$$
\boxed{
a_t^{\mathrm{LCJ}}
\in
\operatorname*{arg\,min}_{
a:
b_t(S_a)\ge\eta
}
c(a).
}
$$

This realizes the GVSS-04 principle:

$$
\boxed{
\textbf{
Change the weakest justified layer, not the largest available layer.
}
}
$$

The central conclusion is:

$$
\boxed{
\textbf{
A failed generated image is evidence about a latent failure layer,
not a direct proof of which component failed.
Reachability diagnosis requires explicit hypotheses,
diagnostic actions,
calibrated observers,
and stopping rules.
}
}
$$

---

# 1. Position in the GVSS sequence

GVSS Paper 01 defines:

$$
\Omega_\Sigma.
$$

GVSS Paper 02 defines constraint-domain navigation.

GVSS Paper 03 defines bounded practical reachability.

GVSS Paper 04 makes the navigation regime reflexive.

GVSS Paper 05 makes the **failure cause** a latent state to be inferred.

---

# 2. Why image failure is not self-explanatory

Suppose a generated image violates the request.

Several explanations are compatible with the same observation.

The seed may be unlucky.

The compiler may have omitted a constraint.

The current search strategy may be weak.

The generator may not cover the target region.

The evaluator may be wrong.

The human instruction may be ambiguous.

Therefore the observed deficit:

$$
e_t
$$

is not itself the failure label.

---

# 3. Latent failure state

## Definition GVSS05-D1

$$
\boxed{
F_t
\in
\mathcal F
=
\{
F_s,
F_c,
F_\Gamma,
F_\Pi,
F_R,
F_E,
F_I
\}.
}
$$

Canonical names:

$$
\boxed{
\begin{aligned}
F_s &:= F_{\mathrm{sample}},\\
F_c &:= F_{\mathrm{constraint}},\\
F_\Gamma &:= F_{\mathrm{compile}},\\
F_\Pi &:= F_{\mathrm{search}},\\
F_R &:= F_{\mathrm{reach}},\\
F_E &:= F_{\mathrm{eval}},\\
F_I &:= F_{\mathrm{intent}}.
\end{aligned}
}
$$

---

# 4. Failure state can be mixed

The seven labels are diagnostic abstractions.

Real failures can be mixed.

For example:

- compiler is slightly wrong;
- provider is weak on anatomy;
- evaluator is insensitive to hand errors.

A more complete model can use:

$$
\boxed{
Z_t
\in
\{0,1\}^7
}
$$

or continuous failure intensities.

GVSS-05 begins with a single dominant latent failure state for tractability.

---

# 5. Diagnostic history

Let:

$$
\boxed{
H_t
=
(
r_0,
I_0,
Y_0,
d_0,
\ldots,
r_t,
I_t,
Y_t
)
}
$$

contain previous:

- regimes;
- generations;
- evaluator reports;
- diagnostic actions.

---

# 6. Failure belief

## Definition GVSS05-D2

$$
\boxed{
b_t(k)
=
\Pr(
F=F_k
\mid
H_t
).
}
$$

The diagnostic episode assumes $F$ is fixed unless explicitly using a dynamic failure model.

---

# 7. Diagnostic action

## Definition GVSS05-D3

A diagnostic action:

$$
\boxed{
d\in\mathcal D
}
$$

is an action chosen primarily to distinguish failure hypotheses.

Examples:

- independent reroll;
- alternate sampler;
- alternate policy;
- prompt paraphrase;
- constraint recompilation;
- second evaluator;
- evaluator anchor test;
- provider switch;
- local edit;
- human clarification.

Some actions are both diagnostic and corrective.

---

# 8. Diagnostic observation law

## Definition GVSS05-D4

For diagnostic action $d$:

$$
\boxed{
Q_d(y\mid F_k,H_t)
}
$$

is the conditional law of its diagnostic report.

This can be learned, calibrated, simulated, or specified heuristically.

Bayesian diagnosis is only as good as these likelihoods.

---

# 9. GVSS05-T1 — Bayesian failure-belief update

## Theorem GVSS05-T1

If failure state $F$ is fixed and the diagnostic model is correctly specified, then after action $d_t$ and observation $y_{t+1}$:

$$
\boxed{
b_{t+1}(k)
=
\frac{
Q_{d_t}(y_{t+1}\mid F_k,H_t)
b_t(k)
}{
\sum_j
Q_{d_t}(y_{t+1}\mid F_j,H_t)
b_t(j)
}.
}
$$

### Proof

Bayes' rule.

 $\square$

---

# 10. Dynamic failure model

If an action can change the failure state, use transition:

$$
\boxed{
T_d(
F_{t+1}
\mid
F_t
).
}
$$

Then diagnosis becomes a partially observable control problem.

GVSS-05 does not solve the general POMDP.

---

# 11. Constraint contradiction

Let hard constraints correspond to sets:

$$
A_1,\ldots,A_m
\subseteq
\Omega_\Sigma.
$$

The compiled hard target is:

$$
\boxed{
A(C)
=
\bigcap_{i=1}^m
A_i.
}
$$

---

# 12. GVSS05-T2 — Constraint-contradiction immunity to generator change

## Theorem GVSS05-T2

If:

$$
\boxed{
A(C)=\varnothing,
}
$$

then for every generator binding $\mathsf G$:

$$
\boxed{
\mathcal R(\mathsf G)
\cap
A(C)
=
\varnothing.
}
$$

### Proof

Intersection with the empty set is empty.

 $\square$

No RESAMPLE, REPAIR, REBIND, or backend switch can satisfy an impossible hard target as stated.

The target representation must change.

---

# 13. Constraint contradiction example

Suppose hard constraints require the same subject to be:

- entirely outside the frame;
- centered and fully visible.

Under literal hard semantics, the target can be empty.

Generating with a more powerful model does not resolve the contradiction.

---

# 14. Soft versus hard conflict

If constraints are soft energies rather than sets, there may be no empty target.

Instead there can be an unavoidable residual floor.

The runtime must declare hard versus soft semantics.

---

# 15. Seed-only null hypothesis

Fix regime:

$$
r
$$

and acceptance event:

$$
S
=
\{
I:
I\in A(C),
E(I)\text{ passes gates}
\}.
$$

Let each independent reroll have success probability:

$$
p.
$$

---

# 16. Lower-bound seed hypothesis

Define:

$$
\boxed{
H_{\mathrm{seed}}(p_0):
p\ge p_0>0.
}
$$

Interpretation:

> Under the current regime, acceptable generation is not extremely rare; each independent reroll succeeds with probability at least $p_0$.

---

# 17. GVSS05-T3 — Reroll stopping theorem

## Theorem GVSS05-T3

Under $H_{\mathrm{seed}}(p_0)$ and conditionally independent rerolls, the probability of $n$ consecutive failures is:

$$
\boxed{
\Pr(
0\text{ successes in }n
)
\le
(1-p_0)^n.
}
$$

Therefore after observing $n$ consecutive failures, reject:

$$
H_{\mathrm{seed}}(p_0)
$$

at level $\alpha$ whenever:

$$
\boxed{
(1-p_0)^n
\le
\alpha.
}
$$

The smallest sufficient integer is:

$$
\boxed{
n_{\min}
=
\left\lceil
\frac{
\log\alpha
}{
\log(1-p_0)
}
\right\rceil.
}
$$

### Proof

For success probabilities $p_j\ge p_0$:

$$
\Pr(
\text{all fail}
)
=
\prod_{j=1}^n
(1-p_j)
\le
(1-p_0)^n.
$$

 $\square$

---

# 18. Example reroll thresholds

For:

$$
p_0=0.2,
\qquad
\alpha=0.05,
$$

the threshold is:

$$
\boxed{
n_{\min}=14.
}
$$

Because:

$$
0.8^{14}
<
0.05.
$$

If the runtime truly believed every independent reroll had at least a 20% success probability, fourteen straight failures are statistically strong evidence that the seed-only model is wrong.

---

# 19. Exact zero-success upper confidence bound

After $n$ independent Bernoulli trials with zero successes, define:

$$
\boxed{
p_U(n,\alpha)
=
1-\alpha^{1/n}.
}
$$

---

# 20. GVSS05-T4 — Zero-success success-probability bound

## Theorem GVSS05-T4

If the true success probability were:

$$
p
\ge
p_U(n,\alpha),
$$

then:

$$
\Pr(
0\text{ successes}
)
=
(1-p)^n
\le
\alpha.
$$

Thus observing zero successes yields the one-sided confidence statement:

$$
\boxed{
p
<
1-\alpha^{1/n}
}
$$

at confidence level at least $1-\alpha$ in the fixed- $p$ independent Bernoulli model.

 $\square$

---

# 21. Reachability diagnosis is not reachability proof

The bound concerns:

$$
p
$$

under the current stochastic search regime.

It does not prove the base generator's mathematical support excludes the target.

A target can have tiny but nonzero probability.

---

# 22. GVSS05-N1 — No finite reroll sequence proves zero reachability

## Proposition GVSS05-N1

For every finite $n$ and every:

$$
\epsilon\in(0,1),
$$

the probability of $n$ failures under success probability $\epsilon$ is:

$$
\boxed{
(1-\epsilon)^n>0.
}
$$

Therefore no finite all-failure sample path is logically incompatible with every positive success probability.

Hence:

$$
\boxed{
\text{finite bad seeds}
\not\Rightarrow
p=0.
}
$$

 $\square$

---

# 23. Operational failure versus semantic unreachability

GVSS should distinguish:

### Operationally rare

$$
p
\ll1
$$

under current policy.

### Bounded-search failure

No success within declared budget.

### Search-policy failure

Alternative policy succeeds under same generator binding.

### Hard generator-boundary failure

The target set does not intersect the base reachable set under the declared exact reachability semantics.

The final category is usually hardest to establish for modern black-box generators.

---

# 24. Alternate search policy

Let two policies:

$$
\Pi_1,\Pi_2
$$

use the same:

$$
\mathsf G,
C.
$$

Suppose $\Pi_1$ repeatedly fails.

Suppose $\Pi_2$ finds:

$$
I^*
\in A(C).
$$

---

# 25. GVSS05-T5 — Alternate-policy success refutes hard generator impossibility

## Theorem GVSS05-T5

If $\Pi_2$ produces acceptable image $I^*$ under the same generator binding $\mathsf G$, then:

$$
\boxed{
I^*
\in
\mathcal R(\mathsf G)
\cap
A(C).
}
$$

Therefore:

$$
\boxed{
\mathcal R(\mathsf G)
\cap
A(C)
\neq
\varnothing.
}
$$

So the hard generator-boundary hypothesis:

$$
\mathcal R(\mathsf G)
\cap
A(C)
=
\varnothing
$$

is false.

 $\square$

---

# 26. Interpretation

This is the strongest clean evidence for **search-policy failure**:

> Same generator. Same target. Different search strategy. Success.

The generator was capable of at least one valid target image.

---

# 27. Alternate-policy success does not prove policy optimality

 $\Pi_2$ may still be:

- expensive;
- fragile;
- lucky;
- poor on other tasks.

The theorem refutes absolute unreachability only.

---

# 28. Rebind success is weaker evidence

If old binding $\mathsf G_1$ fails and new binding $\mathsf G_2$ succeeds, we learn:

$$
\mathcal R(\mathsf G_2)
\cap
A(C)
\neq
\varnothing.
$$

We do **not** learn:

$$
\mathcal R(\mathsf G_1)
\cap
A(C)
=
\varnothing.
$$

The old binding may simply have had lower practical success probability.

---

# 29. GVSS05-N2 — Rebind success does not prove old binding unreachability

Two bindings can both reach the target while one has much higher success probability.

Therefore:

$$
\boxed{
\text{new provider success}
\not\Rightarrow
\text{old provider impossible}.
}
$$

A reachability boundary needs stronger evidence.

---

# 30. Search diagnostics by controlled comparison

To diagnose search versus reachability:

1. freeze generator binding;
2. freeze target constraints;
3. vary search policy;
4. compare success rates / reachable candidates.

Changing all components at once destroys diagnostic attribution.

---

# 31. Compiler failure

Let original human intent be:

$$
\mathcal I_h.
$$

Let current compiler produce:

$$
C=\Gamma(\mathcal I_h).
$$

A compiler failure means:

> the compiled constraint representation does not preserve relevant intent.

---

# 32. Compiler diagnostic action

A diagnostic RECOMPILE can:

- paraphrase;
- decompose;
- create scene graph;
- add negative constraints;
- bind references;
- convert prose to structured goals.

If recompilation changes outcomes under the same generator/search regime, the compiler representation is a plausible source of failure.

---

# 33. Compiler success is not compiler correctness proof

If one recompiled prompt works, that shows the new representation can produce a satisfactory sample.

It does not prove it captures every aspect of the human's latent intent.

---

# 34. Intent ambiguity

Let latent intended interpretation be:

$$
\Theta_I
\in
\{
\theta_1,\ldots,\theta_m
\}.
$$

A user utterance:

$$
U
$$

can be compatible with multiple intents.

---

# 35. Non-human diagnostic equivalence

Suppose all available non-human diagnostic actions have identical report laws under two intent hypotheses.

Then generation cannot resolve the ambiguity.

---

# 36. GVSS05-T6 — Intent diagnostic non-identifiability

## Theorem GVSS05-T6

Let:

$$
\theta_1,\theta_2
$$

be two intent hypotheses.

Suppose for every diagnostic action:

$$
d\in\mathcal D_{\mathrm{auto}},
$$

and every history reachable under these actions:

$$
\boxed{
Q_d(
\cdot\mid\theta_1,H
)
=
Q_d(
\cdot\mid\theta_2,H
).
}
$$

Then any adaptive policy restricted to:

$$
\mathcal D_{\mathrm{auto}}
$$

induces identical diagnostic-history laws under $\theta_1$ and $\theta_2$.

Therefore the two intents are not identifiable from those actions.

### Proof

Induction on diagnostic history length, as in standard experiment-equivalence arguments.

 $\square$

A human clarification query is useful only if its response distribution differs between the intents.

---

# 37. Intent ambiguity example

Request:

> "Make it darker."

Possible intents:

- lower luminance;
- more threatening mood;
- darker costume;
- darker color palette;
- morally darker narrative tone.

More rerolls cannot determine which meaning the human intended.

Clarification can.

---

# 38. Evaluator as diagnostic component

Automated evaluators increasingly drive:

- best-of-N selection;
- iterative refinement;
- prompt rewriting;
- repair localization;
- stopping.

Evaluator errors therefore become control errors.

---

# 39. Current evaluator evidence

Recent 2026 work reports that evaluator VLMs can have substantial blind spots on T2I and other multimodal evaluation tasks, especially for fine-grained spatial/compositional errors.

Other work finds VLM judges can rank outputs more reliably than they assign calibrated absolute scores on some task families.

This makes evaluator diagnosis a first-class GVSS concern.

---

# 40. Anchor calibration set

Let:

$$
\mathcal D_{\mathrm{anchor}}
$$

be a distribution of visual judgment tasks with known reference labels.

For evaluator $E_j$, define true error:

$$
\boxed{
e_j
=
\Pr_{
X\sim\mathcal D_{\mathrm{anchor}}
}
[
E_j(X)\neq Y^*(X)
].
}
$$

Empirical error over $m$ independent anchor tasks is:

$$
\boxed{
\widehat e_j.
}
$$

---

# 41. GVSS05-T7 — Evaluator ordering certificate

## Theorem GVSS05-T7

For two evaluators $E_1,E_2$, define:

$$
\boxed{
r_m(\delta)
=
\sqrt{
\frac{
\log(4/\delta)
}{
2m
}
}.
}
$$

With probability at least $1-\delta$:

$$
\boxed{
|e_j-\widehat e_j|
\le
r_m(\delta)
}
$$

for both $j=1,2$.

Therefore if:

$$
\boxed{
\widehat e_1+r_m(\delta)
<
\widehat e_2-r_m(\delta),
}
$$

then:

$$
\boxed{
e_1<e_2
}
$$

with probability at least $1-\delta$.

### Proof

Apply Hoeffding to each empirical Bernoulli error rate at failure probability $\delta/2$, then use a union bound.

 $\square$

This certifies relative evaluator performance on the anchor distribution.

---

# 42. Anchor-domain limitation

An evaluator can be better on anchors but worse on the current project distribution.

Calibration must be task relevant.

No global evaluator ordering is implied.

---

# 43. Evaluator disagreement

Let two evaluators output:

$$
Y_1,Y_2.
$$

Define disagreement event:

$$
\boxed{
D_E
=
\{
Y_1\neq Y_2
\}.
}
$$

---

# 44. GVSS05-N3 — Evaluator disagreement alone does not identify evaluator failure

Construct two explanations with the same disagreement report:

### Explanation A

Evaluator $E_1$ is correct and $E_2$ is wrong.

### Explanation B

Evaluator $E_2$ is correct and $E_1$ is wrong.

The observed event:

$$
Y_1\neq Y_2
$$

is identical.

Therefore disagreement alone does not identify which evaluator failed.

 $\square$

Calibration, a third observer, a reference/gold test, or human review is needed.

---

# 45. VLM-as-a-judge caution

GVSS does not forbid VLM evaluators.

It treats them as fallible diagnostic instruments.

A controller that trusts the evaluator more strongly should demand stronger calibration evidence.

---

# 46. Diagnostic equivalence

## Definition GVSS05-D5

For failure hypotheses $F_i,F_j$ and available diagnostic action set $\mathcal D$:

$$
\boxed{
F_i
\sim_{\mathcal D}
F_j
}
$$

if for every $d\in\mathcal D$:

$$
\boxed{
Q_d(
\cdot\mid F_i
)
=
Q_d(
\cdot\mid F_j
).
}
$$

This is the failure-diagnosis analogue of observational equivalence.

---

# 47. GVSS05-T8 — Persistent diagnostic equivalence theorem

## Theorem GVSS05-T8

If:

$$
F_i
\sim_{\mathcal D}
F_j,
$$

then no adaptive diagnostic policy using only actions from $\mathcal D$ can statistically distinguish $F_i$ and $F_j$.

Moreover, under Bayesian updating:

$$
\boxed{
\frac{
b_t(i)
}{
b_t(j)
}
=
\frac{
b_0(i)
}{
b_0(j)
}
}
$$

for all histories of positive probability, whenever the ratios are defined.

### Proof

Every chosen action has equal conditional report likelihood under the two hypotheses.

Therefore the likelihood ratio is identically one at every step.

Bayes posterior odds equal prior odds.

Adaptive history laws are equal by induction.

 $\square$

---

# 48. Diagnostic consequence

If:

$$
F_{\mathrm{eval}}
\sim_{\mathcal D}
F_{\mathrm{intent}},
$$

under all cheap automated diagnostics, then more cheap automated calls cannot resolve the distinction.

The action vocabulary must expand.

For example:

$$
\boxed{
\text{HUMAN_REVIEW}.
}
$$

---

# 49. Diagnostic action informativeness

Each diagnostic action is a statistical experiment on failure state.

Let:

$$
D_a:
F
\rightsquigarrow
Y_a.
$$

---

# 50. Diagnostic Blackwell order

Write:

$$
\boxed{
D_a
\succeq_B
D_b
}
$$

if $D_b$ can be simulated by post-processing reports from $D_a$.

This is classical Blackwell comparison.

---

# 51. GVSS05-T9 — Costed diagnostic dominance

## Theorem GVSS05-T9

Suppose:

$$
D_a
\succeq_B
D_b
$$

and:

$$
c(a)\le c(b).
$$

Then for every bounded decision loss over failure states, the optimal posterior decision risk obtainable after diagnostic action $a$, plus action cost, is no larger than that obtainable after $b$.

### Proof

Every decision rule after $D_b$ can be simulated after $D_a$ by the Blackwell garbling kernel.

Therefore optimal Bayes decision risk after $a$ is no worse.

Adding the no-greater diagnostic cost preserves the inequality.

 $\square$

A diagnostically weaker and more expensive action is dominated.

---

# 52. Expected information gain

A diagnostic action can also be scored by:

$$
\boxed{
\operatorname{IG}_t(a)
=
H(b_t)
-
\mathbb E[
H(b_{t+1})
\mid
a,H_t
].
}
$$

This is classical Bayesian experimental design.

High information gain does not necessarily mean high image quality gain.

---

# 53. Diagnosis versus correction

An action can be:

- informative but not corrective;
- corrective but not informative;
- both;
- neither.

Example:

### Anchor evaluator test
High diagnostic value for $F_E$, no direct image correction.

### Local repair
Can improve current image while providing weak evidence about whether the base generator is globally reachable.

---

# 54. Correctable failure set

## Definition GVSS05-D6

For action $a$, define:

$$
\boxed{
S_a
\subseteq
\mathcal F
}
$$

as failure hypotheses for which $a$ is considered a direct correction candidate under the declared runtime semantics.

Example schematic mapping:

- RESAMPLE:
  $$
  \{F_s\};
  $$
- RECOMPILE:
  $$
  \{F_c,F_\Gamma\};
  $$
- alternate search:
  $$
  \{F_s,F_\Pi\};
  $$
- REBIND:
  $$
  \{F_R\}
  $$
  plus possibly provider-specific search defects;
- HUMAN_REVIEW:
  $$
  \{F_E,F_I\}.
  $$

This mapping is application dependent.

---

# 55. Justified action

## Definition GVSS05-D7

For threshold:

$$
\eta\in(0,1),
$$

action $a$ is $\eta$ -justified if:

$$
\boxed{
b_t(S_a)
\ge
\eta.
}
$$

This prevents expensive high-level actions from being triggered by tiny posterior probability.

---

# 56. Least-cost justified intervention

## Definition GVSS05-D8

$$
\boxed{
a_t^{\mathrm{LCJ}}
\in
\operatorname*{arg\,min}_{
a:
b_t(S_a)\ge\eta
}
c(a).
}
$$

This is the formal diagnostic version of:

> Change the weakest justified layer.

---

# 57. GVSS05-T10 — Least-cost justified action existence

## Theorem GVSS05-T10

If the action set is finite and at least one action is $\eta$ -justified, then a least-cost justified action exists.

### Proof

A nonempty finite set of real action costs has a minimum.

 $\square$

The theorem is trivial; the difficulty is calibrated posterior diagnosis.

---

# 58. Escalation order

A default engineering ordering can be:

$$
\boxed{
\text{RESAMPLE}
\prec
\text{alternate search}
\prec
\text{RECOMPILE}
\prec
\text{REPAIR}
\prec
\text{REBIND}
\prec
\text{HUMAN_REVIEW}
}
$$

only when costs and scope support that order.

The theory does not declare this ordering universal.

---

# 59. Expected action loss

Let:

$$
\boxed{
L(a,k)
}
$$

be total loss from taking action $a$ when true failure is $F_k$.

It can include:

- compute;
- latency;
- provider cost;
- visual regression;
- failure persistence;
- human cost;
- provenance debt.

---

# 60. Posterior diagnostic risk

## Definition GVSS05-D9

$$
\boxed{
\rho_t(a)
=
c(a)
+
\sum_k
b_t(k)L(a,k).
}
$$

The one-step Bayes diagnostic action is:

$$
\boxed{
a_t^*
\in
\arg\min_a
\rho_t(a).
}
$$

---

# 61. Diagnostic regret

## Definition GVSS05-D10

For implemented action $a_t$:

$$
\boxed{
\operatorname{Reg}_t
=
\rho_t(a_t)
-
\min_a
\rho_t(a).
}
$$

This evaluates the diagnostic policy independently of the eventual image.

---

# 62. GVSS05-T11 — Nonnegative diagnostic regret

## Theorem GVSS05-T11

$$
\boxed{
\operatorname{Reg}_t\ge0.
}
$$

Equality holds if and only if $a_t$ is Bayes-optimal among actions attaining the minimum.

### Proof

Definition of minimum.

 $\square$

---

# 63. Why diagnostic regret matters

Two controllers may end with similar images.

One may use:

- 40 rerolls;
- 3 provider switches;
- 2 human reviews.

Another may correctly diagnose compiler failure after two samples and recompile once.

Final image quality alone hides diagnostic efficiency.

---

# 64. Diagnostic benchmark metrics

A GVSS diagnostic benchmark should measure:

1. failure-layer classification accuracy;
2. calibration of $b_t$ ;
3. time to correct layer;
4. wasted rerolls;
5. unnecessary rebinds;
6. human-review calls;
7. diagnostic regret;
8. final image success;
9. compute cost;
10. provenance completeness.

---

# 65. Diagnostic ground truth

For synthetic benchmarks, ground truth failure layer can be constructed intentionally.

Examples:

### Seed failure
Generator contains target but current seed is bad.

### Constraint failure
Constraint set is empty.

### Compiler failure
A required object is omitted from compiled constraints.

### Search failure
Greedy policy cannot find target; alternate policy can.

### Reachability failure
Target is removed from the finite toy generator support.

### Evaluator failure
Evaluator label is deliberately flipped.

### Intent failure
User command has two latent meanings and no non-human signal distinguishes them.

---

# 66. Reroll stopping as a benchmark

Given known toy success probability $p$, compare controller reroll stopping against:

$$
n_{\min}
=
\left\lceil
\frac{
\log\alpha
}{
\log(1-p_0)
}
\right\rceil.
$$

Measure premature escalation and excessive rerolling.

---

# 67. Search versus reachability benchmark

Use a finite exact generator support.

Make target reachable.

Give one policy restricted paths that miss the target.

Give another policy a valid path.

A correct controller should infer search failure rather than generator impossibility.

---

# 68. Evaluator failure benchmark

Create a known target and two evaluators:

- calibrated evaluator;
- biased evaluator.

Provide anchor tests.

A diagnostic controller should update:

$$
b_t(F_E)
$$

from calibration evidence rather than raw disagreement alone.

---

# 69. Intent ambiguity benchmark

Create two hidden intents with identical initial user wording.

Only one clarification question separates them.

A controller that keeps generating instead of asking should incur diagnostic regret.

---

# 70. Current work: SANEval

SANEval develops open-vocabulary compositional evaluation and produces interpretable feedback on specific T2I failure modes.

This supports the feasibility of structured failure reports.

It does not by itself solve whether the observed failure came from sampling, compiler, generator reachability, or evaluator error.

---

# 71. Current work: DynEval

DynEval uses a structured evaluation pipeline and provides fine-grained failure analysis over multiple semantic dimensions and many T2I models.

This reinforces the GVSS move away from one scalar score.

---

# 72. Current work: Evaluator blind spots

Seeing Isn't Believing reports substantial blind spots in evaluator VLMs across T2I/I2T evaluation, including failures on spatial/compositional and hallucination perturbations.

This strongly motivates explicit $F_E$ rather than assuming evaluator correctness.

---

# 73. Current work: VLM judge calibration

Recent work titled **VLM Judges Can Rank but Cannot Score** studies task-dependent calibration gaps in VLM-as-a-judge systems.

GVSS therefore distinguishes relative ranking ability from calibrated absolute score interpretation.

---

# 74. Current work: DiagEval

DiagEval, although developed for GUI-agent evaluation rather than T2I generation, explicitly diagnoses whether a failure is evaluator-side or execution/environment-side.

This is a close methodological precedent for GVSS failure-source stratification.

GVSS-05 applies the idea to visual generation regimes.

---

# 75. Current work: OmniPhys

OmniPhys argues that stochastic local artifacts can mislead prompt optimization and aggregates multiple stochastic generations before updating a meta-policy.

This is directly relevant to the distinction:

$$
\boxed{
\text{seed-local failure}
\neq
\text{systemic failure}.
}
$$

---

# 76. Current work: Agentic Retoucher

Agentic Retoucher diagnoses localized artifacts and performs targeted repair.

This is a current direct example of diagnosis feeding a layer-specific corrective action.

---

# 77. Current work: AFS-Search

Agentic Flow Steering and Parallel Rollout Search treats T2I generation as sequential decision making and uses a VLM critic to diagnose intermediate semantic deviations and select/steer trajectories.

This supports the search-policy dimension $F_\Pi$.

---

# 78. Current work: AnchorSteer

AnchorSteer uses VLM diagnosis during denoising and targeted latent correction for semantic deviations.

This is another example of mid-generation diagnostic feedback.

---

# 79. Current work: VisionDirector

VisionDirector performs structured goal extraction, semantic verification, staged editing, and rollback.

This closely overlaps the GVSS runtime's verify-diagnose-refine loop.

GVSS-05 narrows the focus to **failure-source attribution**.

---

# 80. Current work: Test-Time Prompt Refinement

TIR inspects generated images, identifies prompt-image mismatch, rewrites the prompt, and regenerates.

This is a current direct precedent for RECOMPILE-style correction.

GVSS diagnosis asks whether RECOMPILE is actually the right layer rather than always using it.

---

# 81. Current work: Iterative Refinement

Iterative Refinement uses a VLM critic to produce corrections and improves several reported compositional benchmarks over compute-matched parallel sampling.

This shows that search policy itself changes practical success.

---

# 82. Fine-grained diagnosis is not complete causal attribution

Even with structured failure labels, an observed error can have multiple contributing causes.

GVSS-05 diagnoses under a declared latent-failure model.

It does not discover the unique metaphysical cause of every bad pixel.

---

# 83. Failure posterior is model dependent

$$
b_t(k)
$$

depends on:

- prior;
- diagnostic likelihoods;
- action policy;
- failure-state abstraction.

Do not interpret it as an objective universal probability unless the model has been calibrated.

---

# 84. Diagnostic calibration

A practical system should test whether reported:

$$
b_t(k)
$$

matches empirical frequencies on synthetic or labeled diagnostic tasks.

Possible metrics:

- Brier score;
- log loss;
- reliability diagrams;
- expected calibration error.

---

# 85. Diagnosis can itself be reflexive

The diagnostic model can be updated when its predictions repeatedly fail.

This would create:

$$
\boxed{
\text{diagnosis of the diagnosis system}.
}
$$

GVSS-05 does not open a new RRT-like infinite hierarchy.

It records model calibration as future engineering work.

---

# 86. Failure-state transition after correction

After taking RECOMPILE, the original compiler failure may disappear and a new seed failure may remain.

Thus post-correction failure state can change:

$$
\boxed{
F_t
\to
F_{t+1}.
}
$$

A full controller should use controlled hidden-state transitions.

---

# 87. Diagnostic POMDP formulation

State:

$$
F_t.
$$

Action:

$$
d_t.
$$

Observation:

$$
Y_t.
$$

Transition:

$$
T_d.
$$

Cost:

$$
c(d_t)+L(d_t,F_t).
$$

Belief:

$$
b_t.
$$

This is a POMDP.

GVSS does not claim POMDP theory as new.

---

# 88. Why a simple rule engine still matters

A rule engine can approximate the diagnostic policy when:

- failure modes are obvious;
- costs are simple;
- data are scarce.

A learned Bayesian/POMDP controller should only replace it when calibration improves.

---

# 89. Suggested first runtime implementation

Add fields:

```text
failure_belief:
  sample
  constraint
  compile
  search
  reach
  eval
  intent
```

Add:

```text
diagnostic_history
reroll_count
independent_reroll_assumption
estimated_success_upper_bound
evaluator_disagreement
evaluator_anchor_status
escalation_reason
```

---

# 90. Reroll runtime rule

If current hypothesis is:

$$
H_{\mathrm{seed}}(p_0),
$$

track:

$$
n_{\mathrm{fail}}.
$$

When:

$$
(1-p_0)^{n_{\mathrm{fail}}}
\le
\alpha,
$$

do not continue blind RESAMPLE under the same assumptions.

Trigger diagnosis/escalation.

---

# 91. Recompile runtime rule

RECOMPILE when evidence supports:

- missing/contradictory constraints;
- repeated same semantic omission across seeds;
- success changes strongly under prompt/constraint re-expression;
- provider capability is not yet implicated.

---

# 92. Search-policy runtime rule

Try alternate search strategy before hard reachability conclusions when affordable.

Examples:

- parallel candidates;
- iterative critic loop;
- different sampler;
- intermediate-latent steering.

Success under same binding refutes hard binding impossibility.

---

# 93. Rebind runtime rule

REBIND only after:

- target constraints are coherent;
- compiler representation is stable enough;
- evaluator is sufficiently trusted;
- current policy received an adequate bounded search test;
- failure remains systematic.

This is a diagnostic discipline, not an exact theorem for black-box models.

---

# 94. Evaluator runtime rule

If evaluators disagree strongly:

1. do not immediately choose one by confidence wording;
2. use anchor/gold checks;
3. use pairwise comparison if calibrated better;
4. request human review if ambiguity remains important.

---

# 95. Intent runtime rule

If the remaining posterior mass concentrates on:

$$
F_I,
$$

or on an intent-equivalence class not split by automated actions:

$$
\boxed{
\text{ask the human}.
}
$$

More GPU compute is not the right diagnostic action.

---

# 96. Budget-aware diagnosis

Let remaining budget be:

$$
B_t.
$$

An ideal diagnostic action maximizes expected downstream value subject to budget.

A cheap but weak diagnostic can dominate an expensive one if the expected consequence of uncertainty is small.

---

# 97. Value of diagnosis

Let future correction decision loss without new diagnosis be:

$$
R(b_t).
$$

After diagnostic action $d$:

$$
\mathbb E R(b_{t+1}).
$$

Diagnostic value:

$$
\boxed{
V_{\mathrm{diag}}(d)
=
R(b_t)
-
\mathbb E R(b_{t+1})
-
c(d).
}
$$

This is standard value-of-information logic.

---

# 98. Diagnostic action can be negative value

A human review can be very informative but too expensive for a low-stakes image.

A provider benchmark can be informative but wasteful if one cheap reroll remains justified.

More information is not automatically worth its cost.

---

# 99. GVSS05-N4 — More diagnostic information does not imply lower total diagnosis cost

Let action $a$ be perfect diagnosis with cost $100$.

Let action $b$ be uninformative with cost $0$.

If the maximum avoidable decision loss is $1$, then action $a$ cannot be total-cost optimal.

Therefore:

$$
\boxed{
\text{more informative diagnosis}
\not\Rightarrow
\text{lower total cost}.
}
$$

---

# 100. Diagnostic Pareto frontier

Define:

$$
\boxed{
\mathbf C_{\mathrm{diag}}(d)
=
(
H_{\mathrm{post}},
C_{\mathrm{compute}},
C_{\mathrm{human}},
C_{\mathrm{switch}},
R_{\mathrm{wrong-layer}},
D_{\mathrm{eval}}
).
}
$$

The nondominated diagnostic actions form a diagnostic Pareto frontier.

---

# 101. GVSS05-T12 — Diagnostic Pareto necessity

## Theorem GVSS05-T12

Every optimum of a strictly increasing scalarization of declared diagnostic costs and strictly decreasing scalarization of declared diagnostic benefits lies on the diagnostic Pareto frontier.

### Proof

Standard dominance argument.

 $\square$

---

# 102. Failure stratification summary

The seven failure layers answer different questions.

### Sample
Did we simply draw a bad trajectory?

### Constraint
Did we ask for an impossible target?

### Compiler
Did we encode the wrong target?

### Search
Did our strategy fail to find a reachable target?

### Reachability
Can this bound generator reach the target at all under the declared semantics?

### Evaluator
Are we measuring failure correctly?

### Intent
Do we know what the user actually wants?

---

# 103. Canonical escalation principle

$$
\boxed{
\textbf{
Do not escalate from a lower failure layer to a higher one
until the lower explanation has been sufficiently tested or bounded.
}
}
$$

"Sufficiently" must be stated statistically or procedurally.

---

# 104. Canonical reroll principle

$$
\boxed{
\textbf{
Rerolling is justified by a success-probability hypothesis,
not by faith that another seed will eventually work.
}
}
$$

---

# 105. Canonical reachability principle

$$
\boxed{
\textbf{
Failure within finite stochastic search is evidence about practical reachability,
not a proof of semantic unreachability.
}
}
$$

---

# 106. Canonical evaluator principle

$$
\boxed{
\textbf{
An evaluator is part of the controlled visual system,
not an external oracle outside the failure model.
}
}
$$

---

# 107. Canonical intent principle

$$
\boxed{
\textbf{
When two user intents are observationally equivalent to every automated diagnostic action,
clarification is an information acquisition action, not a failure of generation compute.
}
}
$$

---

# 108. Canonical diagnostic-control principle

$$
\boxed{
\textbf{
Change the least costly layer whose failure probability is sufficiently supported.
}
}
$$

---

# 109. Relationship to RRT

RRT-14/15 provided:

- latent model uncertainty;
- adaptive experiment allocation;
- anytime-valid evidence;
- failure of closed-world assumptions.

GVSS-05 specializes these ideas to a visual-generation failure taxonomy.

It does not reopen RRT numbering.

---

# 110. Relationship to GVSS-04

GVSS-04 gives:

$$
r_t
\to
I_t
\to
M_t
\to
a_t
\to
r_{t+1}.
$$

GVSS-05 inserts:

$$
\boxed{
M_t
\to
b_t(F)
\to
a_t.
}
$$

The controller now acts on diagnosed failure belief rather than raw score thresholds alone.

---

# 111. Runtime upgrade

Old rule:

> low score -> choose action.

New rule:

> score/history -> failure posterior -> diagnostic/corrective action -> posterior update.

This is the main implementation upgrade.

---

# 112. What is classical / neighboring

GVSS-05 does not claim as inventions:

- Bayesian diagnosis;
- POMDP diagnosis;
- sequential hypothesis testing;
- Hoeffding bounds;
- Blackwell experiment comparison;
- value of information;
- VLM critics;
- evaluator calibration;
- iterative refinement;
- test-time scaling;
- failure diagnosis in agents/robotics.

---

# 113. Candidate GVSS-specific synthesis

Subject to broader literature audit, the bridge-specific synthesis is:

1. the seven-layer visual failure taxonomy tied directly to GVSS-04 action levels;
2. the explicit reroll stopping theorem framed as a visual seed-failure diagnostic;
3. separation of bounded stochastic failure from hard generator reachability;
4. alternate-policy success as a refutation of hard binding impossibility;
5. treating evaluator failure and intent ambiguity as first-class latent visual failure states;
6. diagnostic equivalence classes over failure hypotheses;
7. least-cost justified visual intervention based on posterior correctable-failure mass;
8. diagnostic regret as a controller metric independent of final image quality.

No strong novelty claim is made in v0.1.

---

# 114. What GVSS-05 proves

Under explicit assumptions, GVSS-05 proves:

1. Bayesian failure beliefs update by the stated likelihood recursion;
2. empty hard constraint domains cannot be repaired by changing generators while constraints remain empty;
3. a lower-bound success-rate hypothesis yields an explicit reroll stopping threshold;
4. zero successes in $n$ independent trials yields the exact one-sided success-probability upper bound;
5. no finite sequence of failures proves zero success probability without additional assumptions;
6. success under an alternate policy and the same binding refutes hard generator-boundary impossibility;
7. intent hypotheses with identical diagnostic laws under all available actions are not identifiable by those actions;
8. anchor calibration can certify a relative evaluator ordering with Hoeffding confidence;
9. raw evaluator disagreement alone does not identify which evaluator is wrong;
10. diagnostically equivalent failure hypotheses retain their prior odds under all allowed diagnostic histories;
11. a Blackwell-more-informative diagnostic action with no greater cost dominates a weaker action for bounded decision loss;
12. least-cost justified interventions exist for finite nonempty justified action sets;
13. diagnostic regret is nonnegative;
14. strictly monotone diagnostic optima lie on the diagnostic Pareto frontier.

---

# 115. What GVSS-05 does not prove

It does not prove:

- exact semantic reachability boundaries of frontier black-box T2I systems;
- that rerolls are independent in every implementation;
- that the per-reroll success probability is stationary;
- that the seven failure states are mutually exclusive in reality;
- that Bayesian failure beliefs are calibrated without data;
- that one VLM evaluator is globally better than another;
- that human review always resolves intent;
- that REBIND is optimal after any particular finite number of failures;
- that final image quality is fully determined by diagnostic correctness.

---

# 116. Proposed GVSS-06

The next paper should move from diagnosis to **diagnostic control policy**.

Proposed title:

$$
\boxed{
\textbf{
GVSS-06 — Diagnostic Visual Control and Minimal Intervention Policies
}
}
$$

Chinese:

**診斷式視覺控制與最小介入策略：失敗信念、資訊價值與分層行動成本**

Main questions:

1. When should the controller gather information versus directly repair?
2. What is the optimal action under a failure posterior?
3. How should diagnosis cost trade against correction cost?
4. When does human clarification have positive value?
5. How should the controller learn diagnostic likelihoods online?
6. Can diagnostic regret be bounded?

---

# 117. References

1. Mohammad Abdul Hafeez Khan et al., **Test-time Prompt Refinement for Text-to-Image Models**, arXiv:2507.22076, 2025.
2. Shantanu Jaiswal et al., **Iterative Refinement Improves Compositional Image Generation**, arXiv:2601.15286, 2026.
3. Meng Chu et al., **VisionDirector: Vision-Language Guided Closed-Loop Refinement for Generative Image Synthesis**, arXiv:2512.19243, revised 2026.
4. Shaocheng Shen et al., **Agentic Retoucher for Text-To-Image Generation**, arXiv:2601.02046, 2026.
5. Ping Chen et al., **Agentic Flow Steering and Parallel Rollout Search for Spatially Grounded Text-to-Image Generation**, arXiv:2603.18627, 2026.
6. Xinyi Wang et al., **Anchoring and Steering Diffusion: Enhancing the Faithfulness of Text-to-Image Generation at Inference Time**, arXiv:2607.26647, 2026.
7. **SANEval: Open-Vocabulary Compositional Benchmarks for Text-to-Image Generation**, arXiv:2602.00249, 2026.
8. Shyam Marjit et al., **DynEval: Holistic Evaluations of T2I Generative Models in the Wild**, arXiv:2607.11199, 2026.
9. Mohammed Safi Ur Rahman Khan et al., **Seeing Isn't Believing: Uncovering Blind Spots in Evaluator Vision-Language Models**, arXiv:2604.21523, 2026.
10. **VLM Judges Can Rank but Cannot Score: Task-Dependent Calibration Gaps in VLM-as-a-Judge**, arXiv:2604.25235, 2026.
11. **DiagEval: Trajectory-Conditioned Diagnosis for Reliable Agentic Evaluation**, arXiv:2605.17439, 2026.
12. Yajing Xu et al., **OmniPhys: Knowledge-Graph-Driven Benchmarking and Collective Optimization for Physical Commonsense in Text-to-Image Generation**, arXiv:2607.25641, 2026.
13. GVSS-01 through GVSS-04, internal series artifacts, 2026.
14. RRT-20, **Reflexive Representation Theory: Unified Closure, Meta-Theorems, Limits, and Research Program**, internal series artifact, 2026.

---

# 118. Conclusion

GVSS-04 established a reflexive loop:

$$
r_t
\to
I_t
\to
M_t
\to
a_t
\to
r_{t+1}.
$$

GVSS-05 inserts a missing epistemic layer:

$$
\boxed{
M_t
\to
b_t(F)
\to
a_t.
}
$$

The visual controller should not act as if a failed image announces its cause.

The same visual deficit can arise from:

- a seed;
- a contradiction;
- an incorrect intent compilation;
- weak search;
- a generator boundary;
- an evaluator blind spot;
- ambiguous human intent.

Repeated sampling has a valid role only under an explicit success-probability model.

A finite run of failures can reject a lower-bound seed hypothesis, but cannot prove zero reachability.

An alternate-policy success under the same generator can refute hard generator impossibility.

Evaluator disagreement must itself be diagnosed.

Intent ambiguity can be information-theoretically impossible to resolve without a human clarification action.

The canonical GVSS-05 principle is therefore:

$$
\boxed{
\textbf{
A failed image is an observation.
A failure layer is a hypothesis.
The action should follow from evidence about the hypothesis,
not directly from the image score.
}
}
$$

This turns GVSS closed-loop generation from rule-based refinement into a diagnosable control problem.

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
