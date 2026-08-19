# HIPG Formal Toy v0.1 — v0.2 Handoff

## Verified v0.1 scope

The v0.1 runtime instantiates:

- Coupleability gate;
- exact quotient-cardinality information bound;
- finite protocol state;
- REMAP / SPLIT / ROLLBACK;
- version history;
- SUCCESS / INFEASIBLE / UNKNOWN separation;
- success / impossibility / unknown certificates.

## v0.2 target

1. **Infer the quotient instead of receiving only its class count.**
2. Add `MERGE`, then test SPLIT↔MERGE dynamics.
3. Add approximate TSSH:
   $$
   D_T=w_E\delta_E+w_R\delta_R+w_J\delta_J+w_O\delta_O.
   $$
4. Add noisy channels and empirical comparison against a Fano-style lower bound.
5. Add the first executable bridge:
   $$
   L_A\leftrightarrow L_F\leftrightarrow L_E\leftrightarrow L_H.
   $$
6. Add provenance anchors and a Gap Certificate.
7. Add mixed impossibility-aware diagnostics.

## Non-negotiable design constraint

Do not treat every failure as a protocol-repair problem.

The diagnostic branch remains first-class:

```text
repairable
resource-limited
information-limited
structurally impossible
non-identifiable
unknown
```
