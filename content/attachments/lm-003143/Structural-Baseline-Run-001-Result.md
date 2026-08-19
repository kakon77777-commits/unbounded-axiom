# Structural Baseline Run 001 — Result Report

**Experiment:** `onx-structural-baseline-001`  
**Date:** 2026-08-14  
**Status:** completed structural dry-run  
**Hidden oracle used during runtime:** no

## 1. Purpose

This run is **not** a real multi-model experiment. It validates the SDPE × Observer-Network measurement architecture while keeping the original SDPE proof runtime authoritative and the observer-network ledger strictly sidecar-only.

## 2. Final snapshot

- Final proof enclosure ratio: $PER=1.000$.
- Final epistemic enclosure ratio: $EER=0.600$.
- Final authoritative survivor count: 0.
- Final surviving Agent hypotheses: 2.
- GCC valid: `true`.
- Verification observations: 4.
- Repair observations: 1.
- Proposal rejection rate: $0.333$.

## 3. First nontrivial observation: naive synchronous coupling fails

At the first closure commit, the proof space reaches:

$$
PER=1.
$$

When certificate `C-right` is invalidated by a version mismatch, the authoritative proof space reopens and drops to:

$$
PER=0.5.
$$

After the v2 repair is verified and committed, it returns to:

$$
PER=1.
$$

The Agent hypothesis sidecar behaves differently. The invalid v1 hypothesis is rejected rather than reopened as epistemically live; the separate repair hypothesis remains available and later receives support. Consequently, $EER$ need not decrease when $PER$ rolls back.

Therefore the strongest naive hypothesis is already false:

$$
\boxed{
PER_t \text{ and } EER_t \text{ need not be pointwise monotone or synchronously coupled.}
}
$$

This is desirable: proof rollback represents authoritative mathematical state, while epistemic memory may retain the information that a route/version was invalid and redirect repair rather than restoring a discarded hypothesis.

## 4. Revised longitudinal hypothesis

The experiment should instead test delayed / structural coupling:

$$
\boxed{
\text{proof rollback}
\rightarrow
\text{fault localization}
\rightarrow
\text{repair}
\rightarrow
\text{reclosure}
}
$$

while measuring whether the Agent hypothesis space avoids repeating already diagnosed failures.

Useful future quantities include:

$$
\ell_{\mathrm{repair}}
=
\text{time or event lag from authoritative rollback to repaired reclosure},
$$

$$
R_{\mathrm{repeat}}
=
\text{rate of previously rejected epistemic hypotheses being reintroduced without new evidence},
$$

and a smoothed enclosure coupling rather than pointwise equality.

For this structural ledger, the proof invalidation occurs at canonical proof sequence 14 and repaired reclosure at sequence 20, so the canonical event lag is:

$$
\ell_{\mathrm{repair}}=6.
$$

## 5. DVI state carried through

The canonical telemetry currently exposes:

$$
D^{\mathrm{resolve}}=1.0,
\qquad
D^{\mathrm{frontier}}=7.0,
$$

$$
W=3.0,
\qquad
\sigma=0.3.
$$

This baseline contains only one telemetry point, so it cannot establish Weak or Strong DVI. It only verifies that the observer sidecar can align Agent events with authoritative SDPE DVI telemetry without acquiring proof authority.

## 6. What is now ready for a real run

The package can now accept real model identities and roles while preserving the same proof runtime. A real longitudinal run should use crossed assignments across model family × role × harness, keep hidden oracle access sealed during the episode, and collect complete action / verification / repair / cost traces.

The next experiment should therefore replace `synthetic-control` role holders with actual heterogeneous Agents, **without changing the SDPE commit gate**.
