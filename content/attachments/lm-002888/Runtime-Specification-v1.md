# SDPE Runtime Specification v1

**Status:** Phase-I reference runtime contract  
**Date:** 2026-08-14

## 1. Canonical state

The runtime state is

$$
\boxed{
\mathbb S_t
=
\langle
\Omega_t,
RouteCert_t,
\mathbf G_t,
GCC_t,
\mathcal H_t,
Compiled_t,
DVI_t,
SurvProf_t,
RouteDecision_t,
Env_t
\rangle.
}
$$

Only certificate-gated commit events may change proof-authoritative closure state.

## 2. Authority channels

- **Proposer:** may create candidate actions; cannot shrink $\Omega_t$.
- **Verifier:** may issue pass/fail certificate records; cannot commit global closure.
- **Coverage / Boundary / Glue auditors:** certify their own obligations only.
- **Compiler:** may build indices, closure bases, snapshots, and support maps; these are accelerators, not new mathematical facts.
- **Commit controller:** may activate verified certificates and update the authoritative survivor state only after all required gates pass.
- **Observatory:** reads state and events and emits telemetry; it has zero proof authority.

## 3. Event sourcing

Let

$$
\mathcal L_t=(e_0,e_1,\ldots,e_t)
$$

be the append-only event ledger and let

$$
\mathcal R
$$

be the deterministic state reducer. The authoritative state is reconstructed by

$$
\boxed{
\mathbb S_t
=
\operatorname{Fold}(\mathcal R,\mathbb S_{-1},\mathcal L_t).
}
$$

Event sequence numbers must be contiguous. Every committed state is fingerprinted from canonical JSON serialization.

## 4. Minimal pipeline

$$
\boxed{
\begin{aligned}
&\mathsf{Detect}
\to\mathsf{Profile}
\to\mathsf{GapExtract}
\to\mathsf{ActionGenerate}
\to\mathsf{Route}
\to\mathsf{Propose}\\
&\to\mathsf{Verify}
\to\mathsf{CoverageAudit}
\to\mathsf{BoundaryAudit}
\to\mathsf{GlueAudit}
\to\mathsf{Compile}
\to\mathsf{Commit}.
\end{aligned}
}
$$

## 5. Commit gate

A certificate may become active only if:

1. the proposal exists;
2. the certificate has passed its registered checker;
3. declared dependencies and versions are active;
4. required route / representation contracts are active;
5. required coverage and boundary audits pass;
6. constructive-gluing mode additionally has a valid gluing certificate.

A diagnostic score, model confidence, sampled coverage estimate, or observatory metric can never substitute for these conditions.

## 6. Rollback

When a certificate becomes stale, the runtime recomputes active exclusion support. A region is reopened exactly when its last active sound support disappears.

For support multiplicity

$$
\kappa_t(x),
$$

the reopened set is

$$
\boxed{
R
=
\{x:\kappa_{\rm old}(x)>0,\;\kappa_{\rm new}(x)=0\}.
}
$$

## 7. Observatory contract

The observatory may report:

$$
D^{\rm resolve},
\quad
D^{\rm frontier},
\quad
W,
\quad
\sigma,
\quad
h,
\quad
\chi,
\quad
|Dirty|,
\quad
|R|,
\quad
SurvProf,
\quad
RouteValue.
$$

These are routing / performance diagnostics. They may not set

$$
\mathsf{GCC.Valid}.
$$

## 8. Benchmark reproducibility

Each benchmark run must pin at least:

- problem / statement fingerprint;
- formalization or adapter version;
- runtime schema version;
- verifier / proof-kernel version;
- dependency snapshot;
- routing policy version;
- model / prover version if applicable;
- hardware / concurrency metadata when measuring time;
- random seed and budget;
- benchmark audit version.

Compilation success alone is not a statement-fidelity certificate.
