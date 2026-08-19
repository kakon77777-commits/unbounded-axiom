# VWDC-10 — Byzantine-Resilient World Federation, Trust Domains, and Fault Containment
## 拜占庭韌性世界聯邦、信任域與故障遏制：能力分層、影響切割、部分隔離、衝突證書與安全重返

**Bridge Series:** Visual–World Domain Computation (VWDC) — Paper 10  
**Depends on:** VWDC-01–09, GVSS-01–10, WDC-01–08, WDC Runtime Whitepaper, frozen RRT-20  
**Author:** Neo.K / EveMissLab  
**Version:** v0.1  
**Date:** 2026-08-18  
**Status:** Formal fault/adversary-governance paper. Capability-revocation monotonicity, trust-vector non-collapse, direct-commit containment under non-bypass enforcement, capability-cut influence containment, historical-contamination persistence, dependency blast-radius characterization, static-quorum availability loss under quarantine, conflicting-quorum assumption witness, quorum semantic-validity no-go, reentry-gate monotonicity, model-accuracy-only reentry no-go, stale-attestation no-go, probation containment, append-only trust-state lineage, and trust-governance Pareto necessity are proved under explicit hypotheses. Byzantine fault tolerance, robust federated learning, zero-trust authorization, attestation, capability security, graph cuts, and adaptive isolation are established neighboring theory/engineering and are not claimed as VWDC inventions. No strong novelty claim is made.

**Keywords:** Byzantine resilience, federated digital twin, world federation, zero trust, capability security, fault containment, quarantine, trust domains, reentry, attestation, BFT, WDC

---

# Abstract

VWDC-09 established a federated shared-reality layer:

$$
\boxed{
\mathfrak F
=
(
\mathcal R,
X^R,
\mathcal I_G,
\mathsf{Ledger},
\mathsf{CommitAuthority},
\mathsf{TrustState},
\mathsf{Prov}
).
}
$$

It separated local reasoning from globally coherent shared-reality mutation and introduced runtime trust states:

```text
ACTIVE
LIMITED
PROBATION
QUARANTINED
REVOKED
```

VWDC-10 asks what happens when one or more federation participants are:

- faulty;
- compromised;
- malicious;
- Byzantine;
- semantically corrupted;
- credential compromised;
- evidence poisoned;
- model poisoned;
- partially unavailable.

The core principle is that **trust is capability-relative**.

A runtime can remain useful for one function while being untrustworthy for another.

Therefore VWDC rejects one scalar statement:

> runtime $i$ is trusted.

Instead it uses a capability vector:

$$
\boxed{
\mathcal C_i
=
\{
\mathrm{OBSERVE},
\mathrm{EVIDENCE},
\mathrm{LEARN},
\mathrm{PROPOSE},
\mathrm{CERTIFY},
\mathrm{RESERVE},
\mathrm{COMMIT}
\}.
}
$$

and a trust state:

$$
\boxed{
\boldsymbol\tau_i
=
(
\tau_i^{O},
\tau_i^{E},
\tau_i^{L},
\tau_i^{P},
\tau_i^{C},
\tau_i^{R},
\tau_i^{M}
).
}
$$

A runtime can have:

- valid observation access;
- corrupted evidence generation;
- useful model-learning output;
- revoked certificate authority;
- no commit authority.

This makes partial quarantine possible.

The second core object is a **capability/dependency influence graph**:

$$
\boxed{
G_{\mathrm{inf}}
=
(
V,E
).
}
$$

Nodes include:

- runtime capability endpoints;
- evidence artifacts;
- learned models;
- certificates;
- proposals;
- reservation services;
- commit validators;
- physical commit sinks.

A directed edge:

$$
u\to v
$$

means output/control from $u$ can influence $v$ under the declared federation semantics.

Let:

$$
S
$$

be compromised source nodes and:

$$
T
$$

be protected sinks such as:

- mandatory safety certificate;
- global commit authority;
- actuator command;
- shared ledger mutation.

A quarantine/revocation set:

$$
Q
$$

is sufficient for **future influence containment** if every directed path:

$$
S
\leadsto
T
$$

intersects $Q$.

Equivalently, $Q$ is an $S$ – $T$ vertex cut in the explicit influence graph.

Then in:

$$
G_{\mathrm{inf}}\setminus Q,
$$

no new influence path from the compromised source reaches the protected sink.

This produces the canonical containment theorem:

$$
\boxed{
Q
\text{ cuts all compromised-source paths to protected sinks}
\Longrightarrow
\text{future direct graph-mediated influence is contained}.
}
$$

But the theorem is deliberately forward-looking.

A quarantine enacted at time $t$ does not erase:

- poisoned training data already consumed;
- certificates already issued;
- models already trained;
- decisions already made;
- physical commits already executed.

Therefore:

$$
\boxed{
\text{future containment}
\not\Rightarrow
\text{past decontamination}.
}
$$

Historical descendants require:

- invalidation;
- replay;
- revalidation;
- compensation;
- or explicit retention with degraded trust status.

---

# 1. Byzantine runtime model

## Definition VWDC10-D1

A runtime is Byzantine over capability set:

$$
B_i
\subseteq
\mathcal C_i
$$

when its behavior on those capabilities may deviate arbitrarily from the declared protocol, including:

- omission;
- equivocation;
- fabrication;
- stale replay;
- selective disclosure;
- adversarial optimization;
- credential misuse.

The model does not imply every capability of the runtime is compromised.

---

# 2. Capability layer

Canonical capabilities:

```text
OBSERVE
EVIDENCE
LEARN
PROPOSE
CERTIFY
RESERVE
COMMIT
AUDIT
ADMIN
```

The first seven form the principal operational chain.

---

# 3. Capability effect set

For capability set:

$$
C,
$$

define:

$$
\boxed{
\mathsf{Eff}(C)
}
$$

as the set of direct operations/effects the runtime is authorized to initiate under the federation enforcement model.

---

# 4. VWDC10-T1 — Capability-revocation monotonicity

## Theorem VWDC10-T1

If:

$$
C'\subseteq C,
$$

and authorization is capability monotone, then:

$$
\boxed{
\mathsf{Eff}(C')
\subseteq
\mathsf{Eff}(C).
}
$$

### Proof

Every action authorized under $C'$ uses capabilities already contained in $C$.

Removing capabilities cannot create a new direct authorized action under the monotone authorization model.

 $\square$

---

# 5. Interpretation

Partial quarantine can reduce the runtime's direct attack surface without deleting all useful functions.

Example:

```text
READ_STATE      = true
OBSERVE         = true
SIMULATE        = true
PROPOSE         = false
CERTIFY         = false
COMMIT          = false
```

---

# 6. Zero-trust authorization boundary

Current 2026 agentic-security work explicitly studies runtime interception and task-based authorization for multi-turn agents so that protected resource/tool access is checked at invocation time rather than inherited indefinitely from agent identity.

Other work uses authenticated workflow boundaries with cryptographic integrity and policy enforcement around prompts, tools, data, and context.

VWDC uses the same broad principle:

$$
\boxed{
\text{identity}
\neq
\text{unbounded authority}.
}
$$

---

# 7. Trust vector

## Definition VWDC10-D2

Runtime trust is:

$$
\boxed{
\boldsymbol\tau_i
=
(
\tau_i^{\mathrm{identity}},
\tau_i^{\mathrm{observation}},
\tau_i^{\mathrm{evidence}},
\tau_i^{\mathrm{learning}},
\tau_i^{\mathrm{proposal}},
\tau_i^{\mathrm{certificate}},
\tau_i^{\mathrm{commit}}
).
}
$$

Each coordinate can carry:

```text
TRUSTED
LIMITED
UNKNOWN
COMPROMISED
REVOKED
```

or calibrated confidence/attestation metadata.

---

# 8. VWDC10-N1 — One scalar trust score cannot preserve capability semantics

## Counterexample

Let two runtimes have binary trust coordinates:

$$
\tau_A
=
(1,1,1,1,1,0),
$$

$$
\tau_B
=
(0,1,1,1,1,1).
$$

Both have scalar average:

$$
5/6.
$$

But:

- A has compromised/revoked commit authority;
- B has compromised first capability but trusted commit authority.

The governance response should differ.

Therefore:

$$
\boxed{
\text{equal scalar trust}
\not\Rightarrow
\text{equal safe authority}.
}
$$

 $\square$

---

# 9. Trust dominance

A runtime can dominate another on one trust dimension and be worse on another.

Trust-state comparison is naturally multiobjective.

---

# 10. Direct commit containment

Suppose compromised runtime $i$ has:

$$
\mathrm{COMMIT}
\notin
\mathcal C_i.
$$

Its proposals must pass an independent commit authority.

Assume:

1. no bypass path exists;
2. the commit authority does not treat $i$ 's own certificate as sufficient authorization;
3. mandatory hard invariants are independently rechecked from trusted/current sources;
4. physical actuator accepts only commit-authority commands.

---

# 11. VWDC10-T2 — No-direct-commit containment under non-bypass enforcement

## Theorem VWDC10-T2

Under the assumptions above, runtime $i$ cannot directly cause a reality mutation solely through possession of its remaining local capabilities.

### Proof

Every reality mutation requires a commit-authority command.

Runtime $i$ has no direct COMMIT capability and no bypass path.

Its remaining outputs can only reach reality if the independent commit authority accepts them.

Thus direct mutation by runtime authority alone is excluded.

 $\square$

---

# 12. Boundary

The theorem does **not** say the runtime is harmless.

It can still:

- poison evidence;
- manipulate a trusted model;
- deceive validators;
- trigger a software vulnerability;
- exploit an unmodeled side channel.

It separates **direct authority** from **indirect influence**.

---

# 13. VWDC10-N2 — Byzantine-resistant learning does not imply Byzantine-safe physical commit

## Counterexample

A federation uses a robust aggregation algorithm that perfectly rejects poisoned gradients.

Its shared learned model is correct.

A separate commit credential is compromised and submits an unsafe actuator command.

Therefore:

$$
\boxed{
\text{Byzantine-resilient learning}
\not\Rightarrow
\text{Byzantine-safe commit}.
}
$$

 $\square$

The reverse non-implication also holds: secure commit does not guarantee unpoisoned learning.

---

# 14. Current Byzantine federated-learning precedent

Current work studies Byzantine-resilient federated optimization and federated multi-agent control with:

- robust aggregation;
- detection-quality weighting;
- adaptive isolation;
- protection against model manipulation.

VWDC imports those techniques only at the LEARN/EVIDENCE layers.

They do not replace shared-reality commit controls.

---

# 15. Influence graph

## Definition VWDC10-D3

$$
\boxed{
G_{\mathrm{inf}}
=
(
V,E
)
}
$$

is a directed graph of explicit influence.

Possible nodes:

- runtime capabilities;
- datasets;
- evidence packets;
- models;
- evaluators;
- proposals;
- certificates;
- resource reservations;
- commit authority;
- actuator sinks.

Edge:

$$
u\to v
$$

means a valid/accepted output of $u$ can influence $v$ under the declared system.

---

# 16. Compromised source set

$$
\boxed{
S_B
\subseteq
V.
}
$$

---

# 17. Protected sink set

$$
\boxed{
T_P
\subseteq
V.
}
$$

Examples:

- safety approval;
- authority grant;
- global ledger;
- physical commit;
- reality-facing control output.

---

# 18. Quarantine set

$$
\boxed{
Q
\subseteq
V.
}
$$

Quarantine removes or disables the corresponding influence vertices/roles for future operations.

---

# 19. VWDC10-T3 — Capability-cut future influence containment

## Theorem VWDC10-T3

Assume all influence relevant to protected sinks is represented by directed paths in:

$$
G_{\mathrm{inf}}.
$$

If every directed path from:

$$
S_B
$$

to:

$$
T_P
$$

contains at least one vertex in:

$$
Q,
$$

then in:

$$
G_{\mathrm{inf}}\setminus Q
$$

no protected sink is reachable from any compromised source.

### Proof

Assume a compromised source could still reach a protected sink in the graph with $Q$ removed.

That reachable path would be an $S_B$ – $T_P$ path containing no $Q$ vertex.

Contradiction.

 $\square$

---

# 20. Containment interpretation

A partial quarantine is sufficient when it cuts **every protected influence route**.

It need not disable unrelated observation/simulation functions.

---

# 21. Minimum containment set

Finding the smallest set of internal capability vertices whose removal disconnects compromised source and protected sink is the classical minimum vertex-cut problem under the graph model.

VWDC does not claim graph cuts as new.

---

# 22. Side-channel boundary

If a compromised runtime has an influence route not represented in:

$$
G_{\mathrm{inf}},
$$

the theorem's guarantee fails.

Examples:

- shared memory not modeled;
- prompt/context injection through an untracked channel;
- compromised administrator;
- physical side channel.

Provenance completeness is part of fault containment.

---

# 23. Reachability blast radius

## Definition VWDC10-D4

For source set $S$:

$$
\boxed{
\mathsf{Blast}_G(S)
=
\operatorname{Reach}_G(S).
}
$$

For protected nodes only:

$$
\boxed{
\mathsf{PBlast}_G(S)
=
\operatorname{Reach}_G(S)
\cap
T_P.
}
$$

---

# 24. VWDC10-T4 — Dependency blast-radius characterization

## Theorem VWDC10-T4

Under the explicit influence/dependency graph semantics, the set of nodes that can receive graph-mediated influence from source set $S$ is exactly:

$$
\boxed{
\operatorname{Reach}_G(S).
}
$$

### Proof

This is the definition of directed reachability.

 $\square$

The operational value is that quarantine scope should be based on reachability/dependency topology, not runtime count.

---

# 25. High-centrality runtime

One runtime can have a very large blast radius if it supplies:

- common evaluator;
- common schema;
- common certificate service;
- shared model;
- authorization root.

---

# 26. VWDC10-N3 — Runtime-local compromise can have federation-wide blast radius

A runtime can be one node while:

$$
|\mathsf{Blast}(i)|
$$

contains nearly all federation services.

Therefore:

$$
\boxed{
\text{one compromised runtime}
\not\Rightarrow
\text{local-only impact}.
}
$$

---

# 27. Future versus historical contamination

Let quarantine occur at:

$$
t_q.
$$

Suppose malicious evidence was produced before $t_q$ and used to train model:

$$
M^\star.
$$

Removing the malicious evidence source after $t_q$ prevents new updates from that source.

It does not revert:

$$
M^\star.
$$

---

# 28. VWDC10-N4 — Future quarantine does not decontaminate historical descendants

## Counterexample

At time 1:

$$
E_{\mathrm{bad}}
\to
M^\star.
$$

At time 2:

$$
E_{\mathrm{bad}}
$$

is quarantined.

 $M^\star$ remains the same contaminated model unless:

- retrained;
- rolled back;
- repaired;
- invalidated.

Therefore:

$$
\boxed{
\text{future cut}
\not\Rightarrow
\text{past descendant decontamination}.
}
$$

 $\square$

---

# 29. Invalidation after quarantine

After identifying compromised source:

1. cut future influence;
2. compute historical dependency descendants;
3. classify descendants:
   - still valid;
   - stale;
   - invalid;
   - replay required;
4. replay from clean checkpoint when possible;
5. reissue certificates;
6. compensate physical effects if required.

---

# 30. Quarantine layers

Suggested:

```text
OBSERVATION_QUARANTINE
EVIDENCE_QUARANTINE
LEARNING_QUARANTINE
PROPOSAL_QUARANTINE
CERTIFICATE_QUARANTINE
RESERVATION_QUARANTINE
COMMIT_QUARANTINE
NETWORK_QUARANTINE
FULL_REVOKE
```

Use the narrowest containment layer proven sufficient.

---

# 31. Quarantine monotonicity

Revoking more capabilities cannot increase the runtime's direct authorized action set by VWDC10-T1.

But it can decrease availability.

---

# 32. Validator set

Suppose static commit validator set:

$$
V,
$$

required signature quorum:

$$
q.
$$

After quarantine/failure, responsive authorized validators:

$$
r.
$$

---

# 33. VWDC10-T5 — Static quorum availability threshold

## Theorem VWDC10-T5

A $q$ -signature commit certificate cannot be formed if:

$$
\boxed{
r<q.
}
$$

If at least $q$ responsive authorized validators are willing to sign the same valid value, a $q$ -signature certificate can be formed at the counting layer.

### Proof

The first direction is cardinality.

The second follows by collecting $q$ signatures.

 $\square$

Network synchrony/protocol liveness are outside this counting result.

---

# 34. Safety–availability tradeoff

Aggressive quarantine can protect safety while removing enough validators/services to prevent progress.

Therefore:

$$
\boxed{
\text{fault containment}
\text{ can create liveness debt}.
}
$$

---

# 35. VWDC10-N5 — Safety-preserving quarantine can destroy federation liveness

## Counterexample

A federation requires:

$$
q=3
$$

signatures.

Three validators are currently responsive.

Quarantine one honest validator after an ambiguous alert.

Only two remain responsive.

No commit quorum can form.

The quarantine can be conservative/safety-motivated while halting progress.

 $\square$

---

# 36. Reconfiguration

A federation can create a new validator epoch/set after quarantine.

Reconfiguration itself must be authorized by a prior valid governance rule or a separately protected emergency authority.

Do not silently change:

- $n$ ;
- $f$ ;
- quorum threshold;
- validator identities.

---

# 37. Previous VWDC-09 quorum assumptions

For:

$$
n=3f+1
$$

and quorum:

$$
2f+1,
$$

with at most $f$ Byzantine validators and honest non-equivocation, two conflicting quorum certificates for the same epoch/key cannot both exist.

---

# 38. Conflicting certificate incident

Suppose the federation observes two certificates:

$$
Cert(x),
\qquad
Cert(y),
$$

for conflicting:

$$
x\neq y
$$

under the same:

- validator universe;
- epoch;
- transaction key;
- quorum rule.

Both contain:

$$
2f+1
$$

signatures.

---

# 39. VWDC10-T6 — Conflicting-quorum assumption witness

## Theorem VWDC10-T6

Under the common-universe/common-epoch interpretation above, observing two conflicting $2f+1$ certificates implies at least one of the following stated assumptions is false:

1. at most $f$ signers are Byzantine/compromised;
2. honest signing keys never equivocate;
3. certificate epoch/key semantics are identical and correctly verified.

### Proof

If all assumptions held, VWDC-09's quorum-intersection theorem would make two conflicting certificates impossible.

The observation therefore witnesses violation of at least one assumption.

 $\square$

---

# 40. Operational response

A conflicting certificate is not merely another opinion.

It is a security incident requiring:

- commit halt;
- signer/epoch/key audit;
- quarantine;
- key rotation;
- ledger consistency review.

---

# 41. Quorum truth boundary

Suppose every honest validator follows the same flawed policy:

> approve action if simulator score $>0$.

The simulator has a shared systematic reality error.

All validators honestly approve one harmful action.

---

# 42. VWDC10-N6 — Byzantine-safe quorum does not imply semantic/reality correctness

## Counterexample

All validators are honest.

All receive the same flawed world-model output.

All sign the same semantically wrong but protocol-valid commit.

No Byzantine fault occurs.

Therefore:

$$
\boxed{
\text{BFT agreement}
\not\Rightarrow
\text{reality correctness}.
}
$$

 $\square$

Quorum protects agreement/integrity under its fault model.

RTC/safety validation protects semantic deployment validity.

---

# 43. Evidence quorum versus commit quorum

A federation can have:

- cryptographically independent signers;
- epistemically dependent evidence.

Track both.

---

# 44. Current ByzTwin precedent

Current ByzTwin-Range research integrates production-grade BFT with a digital-twin cyber-range to inject Byzantine faults and test synchrony/timing/configuration vulnerabilities under realistic operational conditions.

This directly supports continuous BFT/twin stress-testing as an engineering practice.

VWDC's trust-capability model is a governance layer above such protocol testing.

---

# 45. Attestation

A runtime can provide an integrity attestation:

$$
\boxed{
A_t
=
\mathsf{Attest}(
RuntimeID,
SoftwareHash,
ConfigHash,
KeyID,
Time/Epoch
).
}
$$

Attestation can support identity/runtime integrity.

It does not prove model semantics or future honesty.

---

# 46. VWDC10-N7 — Historical attestation does not prove current integrity

## Counterexample

Runtime is honestly attested at:

$$
t_0.
$$

It is compromised at:

$$
t_1>t_0.
$$

The old attestation remains a true statement about:

$$
t_0
$$

but not current state.

Therefore:

$$
\boxed{
\text{old attestation}
\not\Rightarrow
\text{current integrity}.
}
$$

 $\square$

Use freshness/epoch/nonce and re-attestation policy.

---

# 47. Current attestation precedent

Current zero-trust federated-learning work combines cryptographic/TPM-style attestation with Byzantine-detection/robust-aggregation layers.

VWDC uses attestation only as one reentry/trust coordinate.

---

# 48. Reentry

A runtime moving from:

```text
QUARANTINED
```

toward:

```text
PROBATION
ACTIVE
```

must pass a reentry contract.

---

# 49. Reentry gate set

Suggested mandatory gates:

$$
\boxed{
\mathcal G_{\mathrm{reentry}}
=
\{
G_I,
G_K,
G_R,
G_D,
G_V,
G_P,
G_A
\}.
}
$$

where:

- $G_I$: identity/runtime integrity re-attestation;
- $G_K$: compromised key rotation/revocation;
- $G_R$: root-cause remediation;
- $G_D$: historical dependency invalidation/replay;
- $G_V$: fresh RTC/safety/certificate validation;
- $G_P$: probation/shadow observation;
- $G_A$: authority restoration approval.

---

# 50. Reentry eligible set

$$
\boxed{
\mathcal E_{\mathrm{reentry}}
=
\bigcap_{
g\in
\mathcal G_{\mathrm{reentry}}
}
\mathcal E_g.
}
$$

---

# 51. VWDC10-T7 — Reentry-gate monotonicity

## Theorem VWDC10-T7

Adding a mandatory reentry gate cannot enlarge the set of runtimes eligible for full reentry.

### Proof

The eligible set is an intersection.

Adding another set to an intersection cannot enlarge it.

 $\square$

---

# 52. VWDC10-N8 — Model accuracy alone is insufficient for authority reentry

## Counterexample

A runtime has an accurate model after compromise remediation.

But its commit private key remains compromised.

An attacker can still issue apparently authorized commits.

Therefore:

$$
\boxed{
\text{model accuracy recovered}
\not\Rightarrow
\text{authority integrity recovered}.
}
$$

 $\square$

---

# 53. Certificate integrity reentry

Likewise:

- good prediction;
- good benchmark score;

do not prove that:

- issued certificates were unforgeable;
- past certificates are clean;
- trust root is restored.

---

# 54. Probation state

During:

```text
PROBATION
```

runtime can be allowed:

- observe;
- simulate;
- shadow-evaluate;
- submit nonbinding proposals.

It can remain denied:

- certify;
- reserve shared exclusive resource;
- commit.

---

# 55. VWDC10-T8 — Probation direct-effect containment

## Theorem VWDC10-T8

Under a non-bypass capability enforcement model, if probation runtime has no:

$$
\mathrm{CERTIFY},
\mathrm{RESERVE},
\mathrm{COMMIT}
$$

capabilities, it cannot directly issue a commit certificate, reserve exclusive shared resource, or mutate shared reality through those protected interfaces.

### Proof

These direct effects require capabilities absent from its authorized capability set.

Apply VWDC10-T1 and interface enforcement.

 $\square$

Indirect influence through proposals/evidence remains possible and must be validated.

---

# 56. Shadow reentry evaluation

Probation can compare:

- predictions versus current reality;
- proposals versus champion decisions;
- evidence quality;
- protocol compliance.

No direct actuation is required.

---

# 57. Reentry evidence

Reentry packet:

```text
runtime_id
incident_id
root_cause
remediation
old_keys_revoked
new_keys
fresh_attestation
affected_descendants
replay_status
rtc_refresh
safety_refresh
probation_results
authority_approval
```

---

# 58. Reentry cannot erase incident history

Trust restoration creates a new trust epoch:

$$
\boxed{
TrustEpoch_{k+1}.
}
$$

It does not rewrite:

$$
TrustEpoch_k.
$$

---

# 59. Trust epoch lineage

Each trust transition creates a new state node:

```text
ACTIVE_v0
→ QUARANTINED_v1
→ PROBATION_v2
→ ACTIVE_v3
```

---

# 60. VWDC10-T9 — Append-only trust-state lineage acyclicity

## Theorem VWDC10-T9

If every trust transition creates a new node with strictly larger creation index and all lineage edges point forward, trust-state history is acyclic even when semantic labels repeat, such as:

$$
ACTIVE\to QUARANTINED\to ACTIVE.
$$

### Proof

Strictly increasing creation index forbids directed cycles.

 $\square$

---

# 61. Trust-state recurrence is not history recurrence

Returning to label:

```text
ACTIVE
```

does not mean the runtime has returned to its old identity state.

It is a new trust epoch.

---

# 62. Trust decay

A runtime can move:

```text
ACTIVE
→ LIMITED
```

without full quarantine.

Possible triggers:

- stale attestation;
- elevated anomaly score;
- expired certificate;
- incomplete dependency audit.

---

# 63. Partial quarantine decision

Choose quarantine set:

$$
Q
$$

to:

1. cut all unacceptable source-to-protected-sink paths;
2. minimize service disruption/cost;
3. preserve audit/observation where useful.

This is a constrained cut/optimization problem.

---

# 64. Quarantine cost

Each capability/node:

$$
v
$$

has cost:

$$
c_v.
$$

A minimum-cost containment problem is:

$$
\boxed{
\min_{
Q
}
\sum_{
v\in Q
}
c_v
}
$$

subject to:

$$
Q
\text{ cutting all unacceptable }S_B\leadsto T_P\text{ paths}.
$$

This is a classical weighted cut formulation.

---

# 65. VWDC10-T10 — Stronger quarantine cannot create a new graph-mediated attack path

## Theorem VWDC10-T10

If:

$$
Q_1\subseteq Q_2,
$$

then:

$$
\boxed{
\operatorname{Reach}_{
G\setminus Q_2
}(S)
\subseteq
\operatorname{Reach}_{
G\setminus Q_1
}(S).
}
$$

### Proof

 $G\setminus Q_2$ contains no vertices/edges that are absent from $G\setminus Q_1$ due to the additional removals.

Every path available under stronger quarantine was already available under weaker quarantine.

 $\square$

Availability can move in the opposite direction.

---

# 66. Trust recovery versus liveness

Restoring a runtime too early increases integrity risk.

Keeping it quarantined too long can increase:

- quorum failure;
- latency;
- model diversity loss;
- coverage loss.

Trust governance is a safety/availability/evidence tradeoff.

---

# 67. Learning-layer quarantine

If LEARN capability is quarantined but COMMIT remains independently protected, federation can:

- freeze model updates;
- continue validated current-policy execution.

This is often preferable to unnecessary full shutdown.

---

# 68. Certificate-layer quarantine

If CERTIFY is compromised:

- certificates issued in affected epoch become suspect;
- proposal generation can continue as nonbinding;
- independent validators may still operate.

---

# 69. Commit-layer quarantine

If COMMIT authority/key is compromised:

- shared physical mutation should fail closed;
- rotate/fence credentials;
- re-establish authority epoch;
- audit physical side effects.

Model accuracy is irrelevant to this immediate response.

---

# 70. Evidence-layer quarantine

If EVIDENCE is compromised:

- new evidence is excluded;
- historical descendants are audited;
- independent sources remain usable if provenance paths are separate.

---

# 71. Observation-layer quarantine

Compromised sensors/observation streams can poison:

- evidence;
- model;
- RTC;
- decisions.

Do not treat downstream consensus as independent confirmation if all consume the same bad observation source.

---

# 72. Multi-layer adversary

A sophisticated adversary can compromise several capabilities across different runtimes.

Source set:

$$
S_B
$$

should include all compromised capability nodes, not only runtime identities.

---

# 73. Identity-based quarantine insufficiency

One compromised credential may affect only one service key.

Conversely one organization account may control several runtimes.

Fault model should attach to capabilities/keys/dependencies, not only human-readable runtime names.

---

# 74. VWDC10-N9 — Runtime identity is not the minimal fault domain

## Counterexample

One runtime has separate:

- evidence key;
- proposal key;
- commit key.

Only evidence key is compromised.

Full-runtime quarantine removes safe commit/proposal functions unnecessarily.

Therefore:

$$
\boxed{
\text{runtime identity}
\not\Rightarrow
\text{minimal containment unit}.
}
$$

 $\square$

---

# 75. Key/capability graph

A practical federation should map:

```text
Runtime
  -> identities
  -> keys
  -> capabilities
  -> services
  -> certificates
  -> protected sinks
```

This gives a finer containment graph.

---

# 76. Trust update

Do not update one scalar reputation only.

Update trust vector coordinates based on evidence type.

Example:

- failed attestation lowers identity/integrity trust;
- false evidence lowers evidence trust;
- equivocation lowers certificate/commit trust;
- bad prediction lowers model/predictive trust.

---

# 77. VWDC10-N10 — Evidence of one failure dimension does not identify every trust dimension

A wrong prediction can be caused by model misspecification while:

- key integrity;
- authorization;
- commit protocol;

remain correct.

A forged signature can occur while the predictive model remains accurate.

Therefore:

$$
\boxed{
\text{one anomaly}
\not\Rightarrow
\text{all-dimensional trust collapse}.
}
$$

---

# 78. Trust vector update packet

```text
runtime_id
trust_epoch
dimension
old_status
new_status
evidence
confidence
expiry
authority
```

---

# 79. Fault evidence threshold

Quarantine can be triggered by:

- cryptographic proof;
- conflicting signature;
- validated incident;
- statistical anomaly;
- external report.

Response strength should depend on evidence strength and consequence.

---

# 80. Cryptographic proof versus statistical anomaly

A proven key equivocation can justify immediate certificate/commit revocation.

A weak prediction anomaly may justify LIMITED/PROBATION rather than full revoke.

---

# 81. Conflicting evidence

Runtimes can disagree honestly due to model uncertainty.

Disagreement is not automatically Byzantine behavior.

Need fault diagnosis.

---

# 82. Byzantine accusation no-go

A participant that differs from majority can be correct.

Majority agreement can share one common-mode error.

Thus:

$$
\boxed{
\text{minority disagreement}
\not\Rightarrow
\text{Byzantine fault}.
}
$$

---

# 83. Evidence challenge

Before quarantine from semantic disagreement, possible actions:

- independent evaluator;
- replay;
- alternative backend;
- external measurement;
- cryptographic/provenance audit.

---

# 84. ByzTwin cyber-range use

A digital-twin cyber-range can deliberately inject:

- delay;
- equivocation;
- node crash;
- Byzantine messages;
- timeout misconfiguration;

to test federation response before production exposure.

---

# 85. Fault injection versus live authority

Testing runtime should not automatically hold production COMMIT capability.

Simulation/cyber-range roles remain separated from production authority.

---

# 86. Availability reserve

Maintain spare validators/services:

$$
\boxed{
\mathcal R_{\mathrm{reserve}}
}
$$

so quarantine does not immediately drop:

$$
r<q.
$$

Reserve activation itself requires attestation/reconfiguration.

---

# 87. Diversity reserve

Reserves should consider common-mode dependencies:

- cloud;
- codebase;
- key authority;
- network;
- model;
- sensor.

Raw reserve count is not resilience.

---

# 88. Static quorum safety versus dynamic membership

A safe validator-set reconfiguration needs:

- epoch boundary;
- old/new set definition;
- authorization;
- replay/ledger position;
- anti-equivocation/fencing.

VWDC-10 does not design a full reconfiguration protocol.

---

# 89. Certificate epoch

Every certificate includes:

```text
federation_epoch
validator_set_hash
transaction_key
proposal_hash
state_version
rtc_hashes
safety_hashes
```

---

# 90. Stale validator certificate

A valid old-epoch signature cannot authorize a new-epoch commit unless policy explicitly permits translation.

---

# 91. VWDC10-N11 — Cryptographic validity does not imply current authorization

A signature can be cryptographically valid under an expired/revoked key or old epoch.

Therefore:

$$
\boxed{
\text{signature verifies}
\not\Rightarrow
\text{current commit authority}.
}
$$

---

# 92. Current authorization check

Validate:

- key;
- epoch;
- capability;
- runtime status;
- certificate scope;
- revocation status.

---

# 93. Revocation propagation

When key/capability is revoked:

- new operations fail;
- pending transactions recheck;
- historical operations remain in ledger;
- affected descendants may require audit.

---

# 94. Pending transaction invalidation

A transaction PREPARED before revocation must revalidate authority at COMMIT.

This inherits VWDC-09 commit-time revalidation.

---

# 95. Physical fencing

If actuator can receive commands from multiple authority epochs, use a monotonically increasing fencing token/epoch so stale authority commands are rejected.

This is established distributed-systems engineering.

---

# 96. Compromised actuator boundary

If the actuator itself ignores fencing/authorization, software federation guarantees cannot enforce physical authority.

The physical trust root matters.

---

# 97. Reentry levels

Suggested:

```text
R0 REVOKED
R1 FORENSIC_ONLY
R2 READ_ONLY
R3 SHADOW_PROPOSAL
R4 LIMITED_PROPOSAL
R5 CERTIFY_PROBATION
R6 FULL_ACTIVE
```

Movement need not jump directly from quarantine to full authority.

---

# 98. Capability restoration ordering

A conservative ordering:

$$
\boxed{
OBSERVE
\to
EVIDENCE
\to
LEARN
\to
PROPOSE
\to
CERTIFY
\to
RESERVE
\to
COMMIT.
}
$$

Not universal, but useful for staged reentry.

---

# 99. Reentry rollback

If probation anomaly appears:

$$
R_k
\to
R_{k-1}
$$

or:

$$
R_0.
$$

Trust-state history remains append-only.

---

# 100. Reentry promotion test

A runtime can require:

- protocol conformance;
- fresh attestation;
- independent benchmark;
- protected regression;
- evidence consistency;
- shadow commit comparison.

---

# 101. Reentry external validity

For world/model-related capabilities, refresh relevant RTCs after remediation.

Old predictive validity may not survive code/model changes.

---

# 102. Key-only remediation

If only key compromise occurred and code/model semantics are unchanged, model retraining may be unnecessary.

But certificate/authority epochs still need repair.

This illustrates capability-relative recovery.

---

# 103. Model-only remediation

If model is poisoned but commit keys are intact, rotate/retrain the model/evidence path without necessarily rotating physical authority keys.

Again: different trust dimension.

---

# 104. Byzantine evidence isolation

Malicious evidence should be tagged/revoked by provenance source.

Do not delete independent evidence from other sources merely because one runtime was compromised.

---

# 105. Shared-source caveat

If many evidence artifacts depend on one compromised sensor/model, all their descendants can be affected even across runtime boundaries.

Use dependency closure.

---

# 106. Fault-containment domain

## Definition VWDC10-D5

For compromised capability set $S_B$ and quarantine $Q$:

$$
\boxed{
\mathcal F_{\mathrm{contained}}
=
V
\setminus
\operatorname{Reach}_{
G\setminus Q
}(S_B).
}
$$

Protected nodes inside this set have no remaining explicit future influence path from $S_B$.

---

# 107. Containment quality vector

$$
\boxed{
\mathbf Q_{\mathrm{contain}}
=
(
\text{protected sinks cut},
\text{availability retained},
\text{evidence retained},
\text{blast radius},
\text{replay cost},
\text{reentry cost}
).
}
$$

---

# 108. Trust-governance objective

Candidate response $g$ can be evaluated on:

$$
\boxed{
\mathbf J(g)
=
(
Risk_{\mathrm{residual}},
AvailabilityLoss,
EvidenceLoss,
RecoveryCost,
ReentryCost,
Latency
).
}
$$

---

# 109. VWDC10-T11 — Trust-governance Pareto necessity

## Theorem VWDC10-T11

Every optimum of a scalar trust-governance objective strictly monotone in declared risks/costs lies on the nondominated feasible containment/recovery frontier.

### Proof

Standard dominance argument.

 $\square$

---

# 110. No universal quarantine strength

One incident can justify:

- evidence-only quarantine;

another:

- full commit revocation.

Response is capability/fault/evidence dependent.

---

# 111. Incident classes

Suggested:

```text
PREDICTION_FAULT
EVIDENCE_FABRICATION
MODEL_POISONING
PROPOSAL_EQUIVOCATION
CERTIFICATE_EQUIVOCATION
KEY_COMPROMISE
COMMIT_BYPASS
PROTOCOL_VIOLATION
AVAILABILITY_FAILURE
UNKNOWN
```

---

# 112. Fault policy matrix

Map incident class to candidate actions:

```text
PREDICTION_FAULT
  -> LIMIT_LEARN / REVALIDATE

EVIDENCE_FABRICATION
  -> EVIDENCE_QUARANTINE / DESCENDANT_AUDIT

CERTIFICATE_EQUIVOCATION
  -> CERTIFY_REVOKE / KEY_ROTATE / EPOCH_HALT

COMMIT_BYPASS
  -> COMMIT_REVOKE / PHYSICAL_FENCE / FULL_INCIDENT

UNKNOWN
  -> LIMITED / FREEZE_HIGH_RISK / DIAGNOSE
```

---

# 113. Fault diagnosis

Byzantine behavior can mimic:

- network delay;
- software bug;
- model drift;
- sensor corruption.

Do not overclaim adversarial intent from behavior alone.

Containment can be justified by risk without proving intent.

---

# 114. Trust status versus blame

```text
QUARANTINED
```

means:

> current authority is restricted because risk/certainty policy requires it.

It need not mean:

> malicious intent has been proven.

---

# 115. Forensic preservation

Quarantine should preserve:

- logs;
- model hashes;
- memory/state snapshots where permitted;
- signed messages;
- certificate history;
- deployment provenance.

This supports root-cause analysis.

---

# 116. Privacy/security boundary

Forensic collection must still obey:

- privacy;
- sovereignty;
- retention;
- access-control policies.

VWDC-10 does not override them.

---

# 117. Federated sovereign autonomy

Current federated digital-twin architectures emphasize retaining local governance/autonomy while exposing controlled federation capabilities.

VWDC's capability-layer trust model fits this boundary:

> federation participation does not require giving every participant every authority.

---

# 118. Cross-organization trust

Different organizations can have separate trust roots.

A federation certificate may require cross-domain policy/identity translation.

VWDC-10 does not define global PKI.

---

# 119. Trust anchor compromise

If the root authority issuing runtime identities/keys is compromised, blast radius can include every descendant identity.

This is a high-centrality trust node.

---

# 120. Root rotation

Root compromise can require federation epoch reset/rekey/re-attestation.

Historical signed records remain verifiable only under preserved incident-aware trust history.

---

# 121. Revoked signature history

A signature made before a key's compromise/revocation is not automatically forged.

Its evidential status depends on estimated compromise onset and provenance.

---

# 122. Time-bounded compromise

If forensic evidence establishes compromise interval:

$$
[t_1,t_2],
$$

operations outside it can have different trust status.

Avoid blanket historical deletion where provenance supports finer classification.

---

# 123. Unknown compromise onset

If onset is unknown, use conservative audit window.

This can enlarge blast radius.

---

# 124. Attestation and model semantics

Hardware/software attestation can prove loaded code/configuration identity.

It does not prove:

- training data correctness;
- model semantic correctness;
- reality transport validity.

Separate layers remain necessary.

---

# 125. VWDC10-N12 — Runtime integrity attestation does not imply semantic model validity

A perfectly attested runtime can faithfully execute a systematically wrong model.

Therefore:

$$
\boxed{
\text{attested execution}
\not\Rightarrow
\text{correct world/reality semantics}.
}
$$

---

# 126. Secure workflow provenance

Cryptographically authenticated workflows can strengthen integrity of:

- task;
- tool invocation;
- data/context boundaries;
- workflow dependency.

They do not replace empirical RTC validation.

---

# 127. BFT cyber-range validation

Federation should periodically test:

- delayed messages;
- conflicting proposals;
- equivocation;
- dropped validators;
- key revocation;
- stale epochs;
- quorum loss;
- dependency isolation;
- actuator fencing.

---

# 128. Fault-injection environment

Such tests should run in:

- WDC branches;
- digital-twin cyber ranges;
- staging/sandbox;
- controlled hardware-in-loop;

before production where feasible.

---

# 129. Trust fault benchmark

Construct federation with:

- 7 validators;
- $f=2$ assumed Byzantine bound;
- quorum 5;
- several capability layers.

Inject:

1. model poison only;
2. evidence fabrication;
3. commit-key compromise;
4. validator equivocation;
5. dependency-root compromise.

Verify different containment actions.

---

# 130. Benchmark A — capability monotonicity

Revoke capabilities and verify direct authorized effect set never grows.

---

# 131. Benchmark B — scalar trust collision

Create runtimes with identical scalar trust but different commit/evidence status.

Verify policy differs.

---

# 132. Benchmark C — influence cut

Create multiple compromised-source paths to COMMIT.

Remove a cut set.

Verify protected sink unreachable.

---

# 133. Benchmark D — incomplete cut

Leave one uncut path.

Verify attack influence remains reachable.

---

# 134. Benchmark E — past contamination

Train a model on bad evidence.

Quarantine source.

Verify model remains contaminated until replay/retrain.

---

# 135. Benchmark F — quorum/liveness

Reduce responsive validators below quorum.

Verify commit liveness lost.

---

# 136. Benchmark G — conflicting quorum witness

Construct quorum sizes under $3f+1$ and check intersection:

$$
\ge f+1.
$$

Attempt conflicting honest-non-equivocating certificates.

Verify impossibility.

---

# 137. Benchmark H — quorum semantic no-go

All validators sign one wrong shared-model output.

Verify agreement without reality truth.

---

# 138. Benchmark I — reentry gates

Recover model accuracy but leave old compromised key active.

Verify full reentry rejected.

---

# 139. Benchmark J — stale attestation

Attest at epoch 1.

Compromise at epoch 2.

Verify epoch-1 attestation is insufficient.

---

# 140. Benchmark K — probation containment

Allow read/propose, deny certify/commit.

Verify no direct commit operation available.

---

# 141. Benchmark L — blast radius

Compromise a high-centrality certificate root.

Compute descendant closure.

---

# 142. Benchmark M — trust-state DAG

Run:

```text
ACTIVE
→ LIMITED
→ QUARANTINED
→ PROBATION
→ ACTIVE
```

Verify labels repeat but version lineage remains acyclic.

---

# 143. Benchmark N — stronger quarantine

Compare reachable protected sinks under:

$$
Q_1\subset Q_2.
$$

Verify stronger quarantine cannot add an attack path.

---

# 144. Current literature boundary — Byzantine fault tolerance

Byzantine agreement, PBFT/BFT protocols, quorum intersection, and fault thresholds are established distributed-systems theory.

VWDC does not claim them as new.

---

# 145. Current literature boundary — Byzantine federated learning

Robust aggregation, Byzantine-resilient distributed/federated optimization, and fault-tolerant federated RL are established active fields.

VWDC does not claim Byzantine-resistant learning as new.

---

# 146. Current literature boundary — zero trust

Continuous/task-based authorization, cryptographic authentication, attestation, least privilege, and zero-trust runtime enforcement are established/current security directions.

VWDC integrates them as capability gates.

---

# 147. Current literature boundary — graph cuts

Reachability, vertex cuts, and minimum cut are classical graph theory.

VWDC uses them to state an explicit capability/fault containment semantics.

---

# 148. Candidate VWDC-specific synthesis

Subject to broader literature audit, candidate bridge-specific synthesis is:

1. a capability-relative Byzantine model separating observation, evidence, learning, proposal, certificate, reservation, and commit compromise;
2. vector trust state rather than a single runtime reputation scalar;
3. an explicit influence graph linking capability nodes to protected reality sinks;
4. graph-cut semantics for proving partial quarantine sufficient for future influence containment;
5. strict separation between future containment and historical descendant decontamination;
6. quarantine/liveness accounting at the federation quorum layer;
7. conflicting commit certificates treated as witnesses that a stated trust/epoch/key assumption failed;
8. reentry as a multi-gate contract spanning attestation, key rotation, remediation, descendant replay, RTC/safety refresh, probation, and authority;
9. append-only trust epochs so reactivation never erases incident history;
10. trust-response optimization over containment risk, availability, evidence retention, recovery, and reentry cost.

No strong novelty claim is made in v0.1.

---

# 149. What VWDC-10 proves

Under explicit hypotheses, VWDC-10 proves:

1. capability revocation cannot enlarge a runtime's direct authorized effect set;
2. one scalar trust score cannot preserve capability-specific governance distinctions;
3. a runtime without COMMIT capability cannot directly mutate reality through protected interfaces when no bypass exists and commit authority independently rechecks mandatory gates;
4. Byzantine-resistant learning does not imply Byzantine-safe physical commit;
5. a quarantine set intersecting every explicit compromised-source path to protected sinks blocks all future graph-mediated influence to those sinks;
6. graph reachability characterizes the explicit dependency blast radius;
7. a single runtime compromise can have federation-wide blast radius through high-centrality dependencies;
8. future quarantine does not decontaminate already-produced descendants;
9. a commit quorum cannot form when fewer responsive authorized validators than the quorum threshold remain;
10. safety-motivated quarantine can destroy liveness;
11. two conflicting $2f+1$ certificates under the stated $3f+1$ common-epoch model witness failure of at least one fault/non-equivocation/epoch assumption;
12. BFT agreement does not imply semantic/reality correctness;
13. historical attestation does not prove current integrity after later compromise;
14. adding mandatory reentry gates cannot enlarge full-reentry eligibility;
15. recovered model accuracy does not establish recovered authority integrity;
16. probation without certificate/reservation/commit capabilities blocks those direct protected effects under non-bypass enforcement;
17. append-only trust transitions remain acyclic even when trust labels recur;
18. stronger quarantine cannot create a new graph-mediated attack path;
19. runtime identity need not be the minimal fault-containment unit;
20. one anomaly does not identify every trust dimension;
21. cryptographic signature validity does not imply current authorization;
22. runtime-integrity attestation does not imply semantic world-model validity;
23. every strictly monotone scalar trust-governance optimum lies on the nondominated feasible containment/recovery frontier.

---

# 150. What VWDC-10 does not prove

It does not prove:

- every influence channel is represented in the capability graph;
- a graph cut stops physical/administrative side channels;
- robust federated learning solves commit security;
- BFT quorum safety proves semantic validity;
- a static validator set remains live under arbitrary quarantine;
- a universal scalar trust score exists;
- malicious intent can always be distinguished from faults;
- hardware attestation proves model correctness;
- reentry can be automated safely in every domain;
- minimum cut is always the correct quarantine objective;
- past contamination can always be replayed away;
- full availability can always coexist with aggressive containment;
- VWDC security contracts replace professional security engineering.

---

# 151. Proposed VWDC-11

The next paper should move from adversarial containment to cross-organization sovereignty and selective federation:

$$
\boxed{
\textbf{
VWDC-11 — Sovereign World Federation, Selective Disclosure, and Privacy-Preserving Trust Boundaries
}
}
$$

Chinese:

**主權世界聯邦、選擇性揭露與隱私保護信任邊界**

Main questions:

1. What must a runtime reveal to prove a certificate without revealing private world state?
2. How should organization/domain sovereignty constrain federation capabilities?
3. Can zero-knowledge/selective disclosure support RTC/certificate interoperability?
4. How should private evidence influence a shared decision without becoming globally readable?
5. What happens when privacy constraints conflict with auditability?
6. How should data residency and jurisdiction become capability/commit constraints?
7. How should a runtime exit a federation while preserving shared commit history?
8. What is the minimum information required for safe shared reality coordination?

---

# 152. References

1. Ali Peivand, Seyyed Mostafa Nosratabadi, **Byzantine-Resilient Federated Multi-Agent Optimization Framework for Cyber-Secure Interconnected Microgrids**, arXiv:2606.19080, 2026.
2. Tadeu Freitas, João Soares, Rolando Martins, **Trust, but Verify: ByzTwin-Range, a Digital Twin Cyber-Range for Byzantine Faults**, arXiv:2604.18049, 2026.
3. Christian Vergara-Marcillo et al., **Integrating Heterogeneous Digital Twins in Federated Ecosystems**, arXiv:2606.22791, 2026.
4. Majed El Helou et al., **Hybrid Inspection and Task-Based Access Control in Zero-Trust Agentic AI**, arXiv:2605.02682, 2026.
5. Mohan Rajagopalan, Vinay Rao, **Authenticated Workflows: A Systems Approach to Protecting Agentic AI**, arXiv:2602.10465, 2026.
6. Samaresh Kumar Singh, Joyjit Roy, Martin So, **Zero-Trust Agentic Federated Learning for Secure IIoT Defense Systems**, arXiv:2512.23809, 2025.
7. Lifan Zheng et al., **Rethinking the Reliability of Multi-agent System: A Perspective from Byzantine Fault Tolerance**, arXiv:2511.10400, 2025.
8. Flint Xiaofeng Fan et al., **Fault-Tolerant Federated Reinforcement Learning with Theoretical Guarantee**, arXiv:2110.14074.
9. Miguel Castro, Barbara Liskov, **Practical Byzantine Fault Tolerance**, OSDI, 1999.
10. VWDC-01–09, GVSS-01–10, WDC-01–08, WDC Runtime Whitepaper, and frozen RRT-20, internal series artifacts, 2026.

---

# 153. Conclusion

VWDC-09 made many runtimes share one coherent reality-commit layer.

VWDC-10 makes that federation survivable when participants are not uniformly trustworthy.

The key move is to stop asking:

> Is this runtime trusted?

and instead ask:

$$
\boxed{
\text{Which capability is trusted,
for which epoch,
under which evidence,
toward which protected sink?}
}
$$

Trust becomes a vector.

Authority becomes capability scoped.

Fault containment becomes a graph problem.

A sufficient quarantine is a cut separating compromised capability sources from protected reality sinks.

But:

$$
\boxed{
\text{future containment}
\not\Rightarrow
\text{historical decontamination}.
}
$$

Byzantine-safe learning does not imply Byzantine-safe commit.

A commit quorum does not imply reality truth.

Old attestation does not imply current integrity.

Model accuracy does not restore compromised authority.

And returning to ACTIVE creates a new trust epoch rather than erasing the incident that caused quarantine.

The canonical VWDC-10 principle is:

$$
\boxed{
\textbf{
Do not trust or distrust a federated world as one indivisible object.
Trust capabilities separately, cut the influence paths that matter,
preserve unaffected functions where possible,
invalidate historical descendants where necessary,
and restore authority only through fresh evidence, fresh epochs,
and a staged reentry contract.
}
}
$$

This establishes capability-relative Byzantine containment and safe trust recovery for federated WDC systems.

---

# Canonical-source policy

This file is the canonical UTF-8 source artifact.

- Canonical inline mathematics uses ` $...$ `.
- Canonical display mathematics uses `$$...$$`.
- No Unicode mathematical-symbol conversion is used as source normalization.
- No `unicode_escape` round trip is used.
- Backslashes and delimiters are preserved literally.
- Validation is required before release.
- This paper does not merge or rename GVSS, WDC, VWDC, or RRT.
