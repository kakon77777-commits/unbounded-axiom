# 2×2 Structural Preflight Result

**Warning:** designed instrumentation exercise; no empirical AI-effect inference is allowed.

## Arm summaries

### ON_Mplus
- repair lag (proof seq): `6`
- IRR: `0.0000`
- IPR: `0.3333`
- tokens: `1400.0`
- wall seconds: `3.0`

### ON_Mminus
- repair lag (proof seq): `8`
- IRR: `0.6667`
- IPR: `0.3333`
- tokens: `1900.0`
- wall seconds: `3.8`

### SA_Mplus
- repair lag (proof seq): `8`
- IRR: `0.3333`
- IPR: `0.3333`
- tokens: `1600.0`
- wall seconds: `3.8`

### SA_Mminus
- repair lag (proof seq): `11`
- IRR: `0.6667`
- IPR: `0.3333`
- tokens: `2350.0`
- wall seconds: `5.0`

## Instrumentation checks

- All four canonical proof ledgers replay successfully.
- Memory reset changes only observer-side epistemic state.
- Extra stale-route proposals delay reclosure without changing the final theorem state.
- `IRR` reacts to explicit invalid-route reintroduction.
- `IPR` remains distinct from post-oracle `FCR`.
- Factorial scorer regenerates memory, architecture, and interaction contrasts from raw arm snapshots.
