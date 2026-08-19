# HIPG Formal Toy v0.5

HIPG v0.5 extends the executable scaffold with:

- MDL-regularized Boolean hypothesis **construction**;
- evidence-triggered hypothesis-space expansion;
- explicit state-changing interventions;
- multi-step trajectory task quotients;
- generated partner adapter families with inversion;
- certificate **semantic** consistency validation;
- a real SymPy SAT-backed contract fragment;
- protocol regret against three baselines.

Run:

```bash
python hipg_toy_v0_5.py
python -m unittest -v test_hipg_v0_5.py
```

Canonical validation target:

```text
26/26 benchmark PASS
26/26 certificate schema+hash+semantic PASS
15/15 unit tests PASS
```

Important invariant:

```text
SUCCESS != INFEASIBLE != UNKNOWN
```

Counterfactual relaxation remains a proposal. It never silently changes the current problem.
