# IPFC Lean Formalization — Batch 01

**Status:** READY-FOR-LOCAL-VERIFICATION  
**Target:** Lean 4 v4.30.0 + mathlib v4.30.0  
**Date:** 2026-08-15

This package formalizes the first five high-value IPFC core nodes:

1. Fiber Invariance.
2. Generic Fiber Factorization.
3. Lineage Factorization.
4. Exact Phase Module Morphism Composition.
5. Non-Branching Identity No-Go.

## Important verification status

The ChatGPT execution container used to produce this package does **not** contain `lean` or `lake`.
Therefore this release is intentionally **not** labeled machine-verified.

The toolchain is pinned to Lean 4 v4.30.0 and mathlib v4.30.0 because both official projects publish that release.

## Local verification

Windows PowerShell:

```powershell
cd IPFC_Lean_Batch01_v0.1_2026-08-15
.\verify.ps1
```

Unix-like shell:

```bash
cd IPFC_Lean_Batch01_v0.1_2026-08-15
chmod +x verify.sh
./verify.sh
```

A successful run must end with:

```text
PASS: IPFC Lean Batch 01
```

## Source map

- `IdentityFiber.lean` — IPFC Paper 01 / Phase Canon v1.2 T10.
- `Factorization.lean` — Phase Canon v1.2 P15 universal fiber-factorization principle.
- `Lineage.lean` — IPFC Paper 01 / Phase Canon v1.2 T11.
- `PhaseModule.lean` — IPFC Paper 05 exact morphism composition core.
- `ForkNoGo.lean` — IPFC Paper 06 / Phase Canon v1.2 T24.

## Next batch after local PASS

Batch 02 should add:
- Phase Module category laws/extensionality.
- Module quotient structure, not only generic factorization.
- Approximate defect composition.
- Transport/Holonomy conjugacy.
- Symmetric Fork No-Unique-Original.
