# HIPG Formal Toy v0.7

Run:

```bash
python hipg_toy_v0_7.py
python -m unittest -v test_hipg_v0_7.py
```

Canonical validation target:

```text
42/42 benchmark PASS
42/42 certificate schema+hash+semantic PASS
28/28 unit tests PASS
```

New result files: derived operator, active dynamics, observation model, latent equivalence, OOD diagnosis, mixed solver, and meta-regret.

Invariant: `SUCCESS != INFEASIBLE != UNKNOWN`.
