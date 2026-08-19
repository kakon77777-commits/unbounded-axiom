# HIPG Formal Toy v0.6

v0.6 extends HIPG with eight new canonical cases:

- meta-operator subset learning + reusable macro discovery;
- learned transition model before trajectory quotient construction;
- partial-observability belief-task quotient;
- joint partner/task behavioral non-identifiability;
- causal interventions that break that finite symmetry;
- continuous linear solver-backed contract repair;
- learned impossibility/repair diagnosis;
- experiment-cost + model-cost protocol regret.

Run:

```bash
python hipg_toy_v0_6.py
python -m unittest -v test_hipg_v0_6.py
```

Canonical target:

```text
34/34 benchmark PASS
34/34 certificate schema+hash+semantic PASS
24/24 unit tests PASS
```

Core invariant:

```text
SUCCESS != INFEASIBLE != UNKNOWN
```

Additional v0.6 invariant:

```text
behavioral success != unique semantic identification
```
