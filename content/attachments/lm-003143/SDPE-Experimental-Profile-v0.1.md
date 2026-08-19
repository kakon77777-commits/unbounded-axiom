# SDPE Observer-Network Experimental Profile v0.1

**Date:** 2026-08-14  
**Status:** executable longitudinal experiment overlay  
**Authority:** observational only; zero proof authority

## 1. Goal

Use the existing SDPE Runtime as the authoritative proof engine while a separate observer-network sidecar records agent identity, role, model family, proposals, verification, rejection, repair, and cost.

The experiment asks whether two spaces contract together:

$$
\boxed{
\Omega_t
\quad\text{and}\quad
\mathcal A_t^{AI}
}
$$

where $\Omega_t$ is the authoritative SDPE survivor space and $\mathcal A_t^{AI}$ is the surviving Agent hypothesis space.

## 2. Non-contamination rule

The sidecar ledger must never be fed to `sdpe_runtime.py`.

Only the canonical proof ledger may change:

$$
\mathbb S_t.
$$

The observer ledger may reference canonical `proof_seq_ref`, but has no commit authority.

## 3. Oracle rule

During a run:

$$
\boxed{\text{hidden oracle access = forbidden}.}
$$

If a benchmark has hidden truth, it may be opened only after the episode is frozen and only for scoring.

## 4. Primary enclosure metrics

Proof enclosure ratio:

$$
\boxed{
PER_t
=
1-
\frac{|\Omega_t|}{|\Omega_0|}
}
$$

Epistemic enclosure ratio:

$$
\boxed{
EER_t
=
1-
\frac{|\mathcal A_t^{AI}|}{|\mathcal A_0^{AI}|}
}
$$

The key longitudinal question is whether $PER_t$ and $EER_t$ co-move under certificate-gated proof progress.

## 5. DVI metrics

Retain the SDPE distinction:

$$
D_t^{\mathrm{resolve}}
$$

versus

$$
D_t^{\mathrm{frontier}}.
$$

Never infer Strong DVI from falling routine-resolution cost alone.

Verification share:

$$
\sigma_t
=
\frac{W_t}{D_t+W_t}
$$

uses the canonical SDPE telemetry semantics.

## 6. Agent metrics

Record at least:

$$
F_t=\text{proposal / hypothesis rejection rate},
$$

$$
R_t=\text{repair count or repair rate},
$$

$$
V_t=\text{verification action count},
$$

plus tokens, wall time, model family, model version, role, harness, seed, and budget.

## 7. Experimental tracks

1. **Single-Agent Baseline** — one reasoning Agent; machine commit gate remains separate.
2. **Majority Control** — multiple Agents with simple vote/consensus.
3. **Observer Network** — proposer / verifier / auditors separated.
4. **Compiled History** — activate SDPE compiled proof history and measure routine resolution.
5. **Frontier** — count only nonredundant theorem cuts that change authoritative frontier state.
6. **Role Swap** — hold institution/harness fixed while rotating model families through roles.

## 8. Real-run crossed design

For cross-model inference, do not permanently bind one model to one role/harness.

Use a crossed design over:

$$
\boxed{
\text{model}
\times
\text{role}
\times
\text{harness}
\times
\text{task}
}
$$

and include silent-meta-observer episodes.

## 9. Baseline run

`baseline_structural_run` is only a structural dry-run. It replays the existing finite-closure proof ledger and attaches a synthetic observer sidecar. It does **not** claim empirical multi-model convergence.

Its purpose is to verify:
- no proof-authority contamination;
- PER timeline extraction;
- EER timeline extraction;
- rollback / repair visibility;
- DVI telemetry alignment;
- package reproducibility.
