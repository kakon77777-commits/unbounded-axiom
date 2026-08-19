# HIPG Formal Toy v0.8

v0.8 adds:

- behavioral operator invention from all 16 binary truth tables;
- joint reward + dynamics discovery using value-quotient information gain;
- unlabeled HMM recovery up to latent permutation;
- first-class $[(\rho,h,\iota)]_{\equiv}$;
- permanent `UNKNOWN_EQUIVALENCE_CLASS` when raw interventions cannot break semantic symmetry;
- grounded raw-intervention identification;
- diagnostic bundles with theorem anchors, learned likelihoods, OOD support, alternatives, and abstention;
- explicit finite-state temporal counterexample/witness checking;
- operator retirement under task-stream drift.

Run:

```bash
python hipg_toy_v0_8.py
python -m unittest -v test_hipg_v0_8.py
```

Canonical target:

```text
50/50 benchmark PASS
50/50 certificate schema+hash+semantic PASS
20/20 unit tests PASS
```

Core invariant:

```text
SUCCESS != INFEASIBLE != UNKNOWN
```

New epistemic invariant:

```text
GOOD MODEL FIT != UNIQUE SEMANTIC IDENTIFICATION
```
