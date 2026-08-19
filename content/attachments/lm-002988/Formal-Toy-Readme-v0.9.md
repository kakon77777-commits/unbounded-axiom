# HIPG Formal Toy v0.9

v0.9 extends HIPG with:

- finite intervention-language learning;
- multi-variable / non-invertible / stochastic / composite intervention kernels;
- finite minimal grounding number $G^*$;
- active POMDP discovery of $P,O,R$ without hidden-state resets;
- operator search across arity, multi-valued domains, and sequential structure;
- independently replayable finite temporal proof objects;
- theorem-anchor registry with assumption + content-hash checks;
- online drift detection before retirement;
- equivalence classes as stable public artifacts.

Run:

```bash
python hipg_toy_v0_9.py
python -m unittest -v test_hipg_v0_8.py test_hipg_v0_9.py
```

Canonical target:

```text
58/58 benchmark PASS
58/58 certificate PASS
36/36 unit tests PASS
```

Core invariants:

```text
SUCCESS != INFEASIBLE != UNKNOWN
GOOD FIT != UNIQUE SEMANTIC IDENTITY
PERMANENT EQUIVALENCE CLASS != CHOOSE REPRESENTATIVE AS TRUTH
```
