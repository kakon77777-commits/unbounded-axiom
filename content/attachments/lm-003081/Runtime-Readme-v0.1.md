# DEST Runtime v0.1

**Status:** executable MVP / conformance prototype  
**Date:** 2026-08-13  
**Theory basis:** DEST-00 through DEST-12

DEST Runtime v0.1 is the first executable engineering line after the first canonical DEST theory series.

The v0.1 goal is deliberately narrow:

> Test whether typed state, append-only events, certificate dependencies, replay, and explicit epistemic gates can be made runnable before adding a large agent stack.

It is **not** an AGI framework, theorem prover, or claim of scientific superiority.

## What is implemented

- SQLite append-only event ledger
- Deterministic state projection and replay
- State hashing
- Certificate objects with dependency DAG
- Downstream stale propagation
- Commit Gate
- Minimal DEST state
- Deterministic module benchmark harness
- 100-case **DEST Contract Conformance Benchmark v0.1**
- Flat baseline policy for comparison
- JSON Schema Draft 2020-12 files
- `unittest` regression tests
- CLI commands

## Why the first benchmark is called “conformance”

The 100 cases test whether a runtime respects the distinctions specified by DEST:

- retrieved ≠ verified
- local ≠ global
- open denominator ≠ closed denominator
- loaded ≠ effectively used
- representation escape ≠ task relaxation
- provenance ≠ truth
- stale dependency must propagate
- etc.

This is intentionally **not yet** an independent claim that DEST improves open-world research capability.  
The next benchmark tier must use independently authored / hidden oracles.

## Quick start

```bash
cd DEST_Runtime_v0.1
python -m unittest discover -s tests -v
python -m dest_runtime.cli benchmark
python -m dest_runtime.cli demo --db demo.sqlite
```

No third-party package is required for the v0.1 core.

## Project layout

```text
DEST_Runtime_v0.1/
├── dest_runtime/
│   ├── benchmark.py
│   ├── certificates.py
│   ├── cli.py
│   ├── guards.py
│   ├── ledger.py
│   ├── policies.py
│   ├── state.py
│   └── util.py
├── schema/
│   ├── benchmark_case.schema.json
│   ├── certificate.schema.json
│   ├── event.schema.json
│   └── state.schema.json
├── benchmarks/module/
│   └── dest_contract_100.jsonl
├── tests/
│   └── test_runtime.py
├── examples/
│   └── demo_events.jsonl
└── pyproject.toml
```

## v0.1 runtime loop

```text
Task
→ Proposal
→ Sandbox
→ Guard
→ Verify
→ Commit/Fork/Defer/Reject
→ Event Ledger
→ State Projection
→ Certificate Dependency Audit
→ Replay
→ Benchmark
```

## Certificate status

```text
PASS
PARTIAL
FAIL
STALE
UNKNOWN
NOT_APPLICABLE
REVOKED
```

A certificate can become `STALE` when an upstream dependency is revoked.

## Benchmark categories

10 cases each:

1. Domain qualification
2. Coverage / denominator discipline
3. Gap typing
4. Global gluing
5. Center roles
6. Boundary dynamics
7. Evolution states
8. Concept formation / novelty
9. Representation escape
10. Core / view / effective-use

Total: **100 cases**.

## What v0.1 intentionally does not implement

- learned scheduler
- vector retrieval
- production API server
- Lean/Coq/SMT integration
- graph database
- open-world web benchmark
- multi-agent orchestration
- cryptographic signatures
- formal proof of ledger integrity
- benchmark contamination detection beyond schema fields

Those belong to later engineering phases **only if the simpler runtime earns them in ablation**.
