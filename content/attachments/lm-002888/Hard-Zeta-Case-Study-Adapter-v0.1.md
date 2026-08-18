# SDPE Hard-Zeta Case-Study Adapter v0.1

**Status:** interface specification only; no new Collatz theorem is claimed here.  
**Date:** 2026-08-14

## 1. Purpose

This adapter maps an already-existing Hard-Zeta research package into SDPE runtime objects. It does **not** promote chat text, numerical experiments, or unchecked paper statements into proof authority.

## 2. Problem record

A Hard-Zeta adapter should pin:

- exact Collatz / accelerated-map convention;
- statement / counterexample convention;
- phase / branch convention;
- canonical source artifacts;
- checker versions;
- literature-input versions;
- route-map version.

## 3. Survivor representation

The current B-side research frontier may be represented symbolically as typed branch obligations, for example:

$$
\boxed{
\text{Sparse}
\vee
\text{Huge Partial Quotients}
\vee
\text{Structured Highly-Nested Survivor}.
}
$$

If the latest verified Hard-Zeta package refines the third branch further, the adapter records the new branch label and its upstream certificate IDs rather than silently replacing old history.

## 4. Theorem / no-go mapping

Each Hard-Zeta result enters the proof DAG as one of:

- theorem cut;
- reduction;
- bridge theorem;
- no-go / invalid route;
- external input;
- heuristic / finite computation;
- checker artifact.

Only theorem / reduction certificates that have passed their designated verification path may affect the authoritative survivor constraints.

## 5. Symbolic region payloads

An inequality such as

$$
r\le F(L,y,M_\beta,\ldots)
$$

is stored as a symbolic constraint payload with:

- variable declarations;
- scope / branch assumptions;
- theorem ID;
- dependency IDs;
- exact constants / rounding conventions;
- checker or formal proof reference;
- source fingerprint.

The SDPE reference runtime does not itself decide symbolic implication between arbitrary inequalities. A domain-specific checker / SMT / CAS / theorem prover must issue the relevant certificate.

## 6. Typed gaps

Examples:

- branch not eliminated;
- exact residue bridge missing;
- continued-fraction escape unresolved;
- representation / convention ambiguity;
- unverified external Diophantine constant;
- checker / source mismatch;
- global-density / local-chain bridge incomplete.

These become explicit $G_B$, $G_C$, $G_R$, $G_{\rm core}$ or domain-specific gap records.

## 7. Observatory telemetry

The observatory may show:

- number of active theorem cuts;
- number of closed / open routes;
- dependency depth;
- compiled support multiplicity;
- survivor-parameter bounds;
- frontier branch count;
- DVI cost telemetry;
- checker status;
- literature freshness.

None of these metrics can set a Collatz proof-complete flag.

## 8. Commit rule

A Hard-Zeta artifact becomes authoritative only through:

$$
\boxed{
\text{artifact}
\to
\text{typed candidate}
\to
\text{verification}
\to
\text{certificate node}
\to
\text{coverage / dependency audit}
\to
\text{commit}.
}
$$

The adapter is therefore a provenance and orchestration layer, not a substitute for mathematical verification.
