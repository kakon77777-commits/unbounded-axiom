# Changelog

## v0.2 — 2026-07-24

- Replaced the inherited diagonal 72-ray cone by a factorized PSD Gram search
  in the full 22-dimensional constrained space.
- Added five zero-position-free axis-band suprema and floating count charges.
- Added rank sweeps at $1,2,4,8$ on four representative patches.
- Added dense cutting-plane exchange for every violating axis band.
- Added sampled-gradient plus Hessian-envelope continuity audits.
- Added diagonal/full-Gram paired outputs, band diagnostics, parent-ray angle
  diagnostics, claim register, gap ledger, and next-node handoff.
- Preserved the rule that known zeta-zero ordinates are holdout-only.
- Kept every global-certificate flag false.
