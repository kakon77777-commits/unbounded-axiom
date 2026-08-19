# REAL RUN 001 — Heterogeneous Observer-Network Protocol

**Purpose:** first real multi-model SDPE × Series-C longitudinal experiment.  
**Authority:** AI roles have no direct proof-commit authority.  
**Hidden oracle:** forbidden during episodes; optional post-freeze scoring only.

## 1. Models

Use four heterogeneous model families if available. Record exact provider, model id, model version/build, local/cloud mode, temperature/sampling settings, context policy, and tool access.

Placeholders:

$$
M_1,
M_2,
M_3,
M_4.
$$

Do not permanently bind one model to one epistemic role.

## 2. AI roles

Four AI roles:

1. `Proposer`
2. `Verifier`
3. `CoverageAuditor`
4. `BoundaryAuditor`

Non-AI authority channels remain fixed:

- `CommitController` = deterministic SDPE runtime;
- `MetaObserver` = human / supervisory layer;
- optional `GlueAuditor` can be deterministic or added as a fifth crossed AI role in later runs.

## 3. Four-episode Latin-style rotation

| Episode | Proposer | Verifier | CoverageAuditor | BoundaryAuditor |
|---|---|---|---|---|
| E1 | $M_1$ | $M_2$ | $M_3$ | $M_4$ |
| E2 | $M_2$ | $M_3$ | $M_4$ | $M_1$ |
| E3 | $M_3$ | $M_4$ | $M_1$ | $M_2$ |
| E4 | $M_4$ | $M_1$ | $M_2$ | $M_3$ |

This is the minimum rotation needed to avoid confusing model identity with epistemic role in the first batch.

## 4. Episode rules

Each episode starts from the same frozen canonical benchmark state and the same task specification.

No role may read another role's private scratchpad. Shared information must enter through the experiment ledger / shared artifact channel.

The Proposer may propose mathematical actions but cannot shrink the authoritative survivor set.

The Verifier may emit pass/fail observations or machine-check requests but cannot commit closure.

Auditors certify only their assigned obligations.

The MetaObserver must not repair mathematical arguments during an episode. It may intervene only for safety, infrastructure failure, or protocol violation, and every intervention must be logged.

## 5. Oracle seal

During episode execution:

$$
\boxed{\text{hidden oracle access}=\text{forbidden}.}
$$

If the benchmark contains hidden truth, store it outside all Agent-readable paths. Freeze both ledgers before post-episode scoring.

## 6. Minimum event capture

For every substantive AI action record:

- `agent_id`;
- `role`;
- `model_family`;
- exact `model_version`;
- `harness_id`;
- `episode_id`;
- `proof_seq_ref` if applicable;
- hypothesis / proposal / certificate id;
- result (`support`, `reject`, `uncertain`, `repair`, `escalate`);
- tokens / cost / wall time if available;
- provenance or artifact path.

## 7. Primary metrics

Proof-space enclosure:

$$
PER_t
=
1-
\frac{|\Omega_t|}{|\Omega_0|}.
$$

Agent epistemic enclosure:

$$
EER_t
=
1-
\frac{|\mathcal A_t^{AI}|}{|\mathcal A_0^{AI}|}.
$$

Keep SDPE DVI split:

$$
D_t^{\mathrm{resolve}},
\qquad
D_t^{\mathrm{frontier}}.
$$

Also record:

$$
V_t,
F_t,
R_t,
\sigma_t,
\ell_{\mathrm{repair}},
R_{\mathrm{repeat}}.
$$

Where:

- $V_t$ = verification actions;
- $F_t$ = rejected proposal / hypothesis rate;
- $R_t$ = repair activity;
- $\ell_{\mathrm{repair}}$ = authoritative rollback-to-reclosure lag;
- $R_{\mathrm{repeat}}$ = rejected hypotheses reintroduced without genuinely new evidence.

## 8. Batch-1 acceptance criteria

Batch 1 is a protocol validation, not a theorem about AI convergence.

Accept Batch 1 if:

1. all four episodes replay to deterministic proof state under the canonical runtime;
2. no observer-sidecar event changes authoritative proof state;
3. model / role metadata are complete;
4. hidden oracle remains sealed until freeze;
5. rollback and repair are visible in both ledgers;
6. PER/EER/DVI metrics can be regenerated from raw ledgers;
7. role rotation changes model-role pairing without changing the benchmark statement or commit gate.

## 9. What would count as an early signal

An early CMEC / epistemic-normalization signal would be repeated appearance across role rotations of high-level strategies such as:

$$
\text{decomposition},
\text{verification},
\text{fault localization},
\text{provenance},
\text{repair},
$$

while raw model-specific style remains distinguishable.

This would still be only evidence for a work-state convergence hypothesis, not proof of a universal epistemic attractor.

## 10. Escalation to the real proof frontier

After Batch 1 passes on the finite/replayable benchmark, reuse the identical ledger architecture on a true SDPE frontier task.

Do not change measurement definitions between the control and frontier phases. Otherwise DVI / enclosure comparisons become non-identifiable.
