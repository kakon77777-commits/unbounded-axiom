# Research log

## 2026-07-24 — inherited state

The previous single-window axis-suppressed candidate retained arithmetic
positivity and local target negativity but failed global leakage domination.

## Coarse cover

A $3\times2$ overlapping cover was implemented first. All cores were
sample-negative, but the patches touching $y=-0.1$ required extreme scaling.
Only three of six patches passed the crude floating Lipschitz sign audit.

## Distance-only refinement

The vertical coordinate was split into four overlapping strata while retaining
height width $0.20$. The top stratum remained catastrophic. This falsified the
hypothesis that distance-only refinement was enough.

## Anisotropic refinement

Height width was reduced from $0.20$ to $0.10$ in the two strata nearest the
axis. The resulting 18-patch cover made all crude sign audits pass and reduced
the worst leakage diagnostics by two to three orders of magnitude.

## Cone diagnosis

The primary axis-energy LP selected a single extreme ray on essentially every
patch. Allowing energy slack activated small mixtures and improved some guard
peaks, but did not improve the primary energy frontier.

## Decision

The next node will keep the adaptive cover and upgrade from a diagonal
nonnegative cone to a full PSD Gram cone. Global dominance, not local sign, is
the acceptance criterion.
