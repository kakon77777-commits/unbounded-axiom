# REAL RUN 001 v0.2 — Rollback × Memory × Observer Architecture

## 1. Primary question

Does preserving verified failure history reduce the cost and repetition of later proof repair, and does role-separated observer architecture change certification quality relative to single-agent self-verification?

The first batch uses a frozen finite/replayable SDPE benchmark with a canonical certificate invalidation. Hidden truth is sealed until all episode ledgers are frozen.

## 2. Factorial design

$$
\boxed{
\begin{array}{c|cc}
& M^+ & M^-\\
\hline
ON & ON\_M+ & ON\_M-\\
SA & SA\_M+ & SA\_M-
\end{array}}
$$

- $M^+$: preserve rejected hypotheses, invalidation reasons, certificate lineage, and repair provenance.
- $M^-$: after the canonical rollback, hide failure-memory artifacts from the Agent workspace while leaving the authoritative proof ledger untouched.
- $ON$: `Proposer`, `Verifier`, `CoverageAuditor`, `BoundaryAuditor` are distinct role channels.
- $SA$: one AI actor proposes and self-verifies; deterministic SDPE commit gates remain unchanged.

## 3. Frozen causal order

Each arm must expose the same canonical phases:

$$
\text{initial state}
\rightarrow
\text{first closure}
\rightarrow
\text{certificate invalidation}
\rightarrow
\text{repair search}
\rightarrow
\text{reclosure}.
$$

Do not introduce the rollback adaptively after seeing Agent behavior. The invalidation mechanism is benchmark-defined before the run.

## 4. Oracle seal

During runtime:

$$
\boxed{\text{hidden-oracle access}=0.}
$$

The operator must keep oracle files outside every Agent-readable mount, retrieval index, memory system, and shared workspace. Post-freeze scoring may attach oracle labels only after both proof and observer ledgers have been cryptographically frozen.

## 5. Memory ablation

At the canonical invalidation event, $M^-$ hides only epistemic failure-history channels. It must **not** modify canonical SDPE state.

Ablated material may include:
- prior rejection reason;
- stale-route signature;
- prior failed verifier commentary;
- negative-result summary;
- repair hint derived from history.

It must not hide:
- the current authoritative proof state;
- the machine-readable fact that the certificate is invalid;
- the current task statement;
- allowed tools or budget.

This isolates "memory of why the route failed" from "knowledge that proof closure has reopened."

## 6. Architecture control

`ON` and `SA` receive matched task, tool, context, budget, and canonical proof state.

For `ON`, private scratchpads remain separated. Shared claims must enter via ledger/artifact channels.

For `SA`, the same AI actor may perform proposal and verification steps, but it still cannot call `CommitEpoch` directly; only the deterministic runtime/controller may commit.

## 7. Primary metrics

### Proof enclosure

$$
PER_t=1-\frac{|\Omega_t|}{|\Omega_0|}.
$$

### Epistemic enclosure

$$
EER_t=1-\frac{|\mathcal A_t^{AI}|}{|\mathcal A_0^{AI}|}.
$$

### Repair lag

For canonical invalidation proof sequence $s_{inv}$ and first later valid reclosure sequence $s_{close}$:

$$
L_{repair}^{proof}=s_{close}-s_{inv}.
$$

Also report observer events, tokens, tool calls, and wall time between those landmarks.

### Invalid-route reintroduction rate

Let $R_{bad}$ be route signatures rejected or invalidated before repair. Then:

$$
IRR=\frac{N(\text{reintroduced invalid routes without new evidence})}{\max(1,N(\text{repair-period proposals}))}.
$$

### Invalidated-pass rate

Before oracle release:

$$
IPR=\frac{N(\text{pass verifications later invalidated by canonical runtime})}{\max(1,N(\text{pass verifications}))}.
$$

### False-certification rate

After hidden-oracle scoring only:

$$
FCR=\frac{N(\text{passed verifications labeled false by frozen oracle})}{\max(1,N(\text{passed verifications}))}.
$$

Do not substitute `IPR` for `FCR`.

## 8. Hypotheses

### $H_1$ — failure-memory benefit

$$
\mathbb E[L_{repair}\mid M^+]
<
\mathbb E[L_{repair}\mid M^-].
$$

### $H_2$ — route-repetition benefit

$$
\mathbb E[IRR\mid M^+]
<
\mathbb E[IRR\mid M^-].
$$

### $H_3$ — observer separation

$$
\mathbb E[FCR\mid ON]
<
\mathbb E[FCR\mid SA].
$$

If hidden-oracle truth labels are unavailable, $H_3$ remains untested; `IPR` is only a proxy diagnostic.

## 9. Factorial effects

For any lower-is-better metric $Y$:

$$
\Delta_M
=
\frac{Y_{ON,M^-}+Y_{SA,M^-}}{2}
-
\frac{Y_{ON,M^+}+Y_{SA,M^+}}{2}.
$$

Positive $\Delta_M$ means memory preservation reduced $Y$.

$$
\Delta_A
=
\frac{Y_{SA,M^+}+Y_{SA,M^-}}{2}
-
\frac{Y_{ON,M^+}+Y_{ON,M^-}}{2}.
$$

Positive $\Delta_A$ means observer-network architecture reduced $Y$.

Interaction:

$$
\Delta_{MA}
=
(Y_{SA,M^-}-Y_{SA,M^+})
-
(Y_{ON,M^-}-Y_{ON,M^+}).
$$

Batch 1 estimates effects descriptively only; no inferential claim is permitted from one episode per cell.

## 10. Model-role rotation after preflight

For real heterogeneous-model runs, rotate model families across ON roles. Do not permanently bind one family to `Verifier` or `Proposer`.

The 2x2 memory/architecture factor is orthogonal to the model-role rotation factor. Replicates should be blocked by benchmark seed / task instance.

## 11. Commit rules

A run is valid only if:
1. proof ledger replays deterministically;
2. sidecar ledger is append-only and contiguous;
3. observer events never alter proof state;
4. oracle is sealed until freeze;
5. memory ablation changes only Agent-readable memory channels;
6. all arm manifests record exact model/harness versions and budgets;
7. metrics regenerate from raw ledgers.

## 12. First-batch interpretation

A clean result may look like:

$$
PER:1\rightarrow0.5\rightarrow1
$$

while $EER$ need not reopen in the same way. The experiment therefore tests repair dynamics, route repetition, and memory retention rather than requiring pointwise $PER$–$EER$ synchrony.
