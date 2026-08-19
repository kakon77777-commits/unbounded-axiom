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


## v0.2-alpha: Tier-1 Interaction Benchmark

This package adds a second benchmark layer:

```bash
python -m dest_runtime.cli interaction
```

Unlike the 100-case contract benchmark:

- policies see only `observation`;
- the oracle reads a separate `hidden_state`;
- expected answers are not stored in the visible case;
- every case has a semantic mutation expected to change the oracle;
- every case has a neutral mutation expected not to change the oracle.

The interaction benchmark currently contains 60 cases:

- Coverage × View
- Gap × Representation
- Boundary × Evolution
- Glue × Branch
- Certificate × Version
- Core × View

This remains synthetic. Its purpose is to test cross-module behavior and benchmark-oracle discipline before moving to an independent open-world benchmark.


## v0.3-alpha: Tier-2 End-to-End Benchmark

Run:

```bash
python -m dest_runtime.cli e2e
```

Tier-2 contains 10 stateful scenarios × 100 environment steps.

Each scenario begins with claim formation and verification, then injects delayed events such as:

- certified counterexample
- version drift and re-verification
- source revocation
- branch fork
- retrieval miss
- representation-relaxation cheat
- loaded-but-unused critical evidence
- partially observable hidden invalidation

The benchmark validates **two replay surfaces**:

1. DEST knowledge-state hash
2. certificate dependency graph digest

This upgrade was necessary because v0.2 could replay knowledge events while certificate table mutation was not itself fully represented in the ledger.

v0.3 records:
- `CERT_CREATE`
- `CERT_DEPENDENCY`
- `CERT_STATUS`

and provides certificate-table reconstruction from ledger events.

### Important limitation

Two scenarios intentionally contain hidden truth that the runtime cannot yet infer from the observable certificate state (`UNKNOWN`). These are not patched by cheating against hidden state. They measure partial-observability limits.


### Measured Tier-2 result

```text
DEST composite integrity: 97.1%
Flat baseline:           82.9%

DEST final canonical accuracy: 80.0%
Flat canonical accuracy:       60.0%

Knowledge-state replay:   100%
Certificate-graph replay: 100%
```

The two DEST canonical misses are deliberately retained partial-observability cases.
See `TIER2_REPORT.md`.


## v0.4-alpha: Active Inspection, Verification Debt, and Risk-Conditioned Quarantine

Run:

```bash
python -m dest_runtime.cli inspection
```

The new benchmark tests a different capability from Tier-2:

> When evidence is `UNKNOWN`, does the runtime merely wait, or can it create an explicit evidence debt and ask for the right next observation?

v0.4 adds:

- `verification_debts` to replayed DEST state
- `inspection_tasks` to replayed DEST state
- `DEBT_CREATE` / `DEBT_STATUS` events
- `INSPECTION_CREATE` / `INSPECTION_STATUS` events
- risk-conditioned quarantine
- an inspection priority scheduler
- risk/coverage evaluation

Inspection results are returned by the synthetic environment **only if a matching inspection task is open**. This prevents the runtime from passively receiving evidence it did not request.

### Risk/coverage rule

A high-risk unknown can be quarantined without being declared false.

```text
UNKNOWN
→ debt
→ inspection task
→ optional quarantine
→ evidence
→ restore canonical OR revoke/reopen
```

This separates:

```text
epistemic invalidation
```

from:

```text
temporary governance abstention
```

and prevents the runtime from collapsing UNKNOWN into PASS or FAIL.


### Measured Active Inspection result

```text
DEST v0.4:
  final-state accuracy  100.0%
  decision coverage     83.3%
  selective risk        0.0%
  debt creation recall  100.0%

DEST v0.3:
  final-state accuracy  50.0%
  decision coverage     100.0%
  selective risk        50.0%
```

See `ACTIVE_INSPECTION_REPORT.md`.


## v0.5-alpha: Budgeted Evidence Acquisition

Run:

```bash
python -m dest_runtime.cli budget
```

v0.5 converts the open verification-debt queue into a finite-budget portfolio problem.

The benchmark contains:

```text
30 episodes
× 25 simultaneous evidence debts
= 750 candidate inspections
```

Each debt has observable:
- risk tier
- impact
- downstream leverage
- uncertainty
- inspection cost
- estimated invalidity probability
- estimated resolution probability
- current quarantine state
- coverage value

and hidden benchmark-only:
- actual validity outcome
- whether the inspection will resolve
- realized value

Schedulers are not allowed to use hidden fields.

Compared policies:

```text
FIFO
Risk-only
v0.4 static priority
v0.5 expected-inspection-value knapsack
```

The v0.5 expected inspection value estimates both:
1. value of detecting an invalid active claim;
2. value of releasing a valid quarantined claim.

This is intentionally a risk–coverage portfolio rather than a pure “highest risk first” queue.


### Measured Budgeted Evidence result

```text
v0.5 EIV:
  total realized value / oracle  62.4%
  residual exposure              3.426
  decision coverage              88.1%

v0.4 static:
  total realized value / oracle  60.4%
  residual exposure              3.484
  decision coverage              88.7%
```

This is a multi-objective trade-off, not a universal v0.5 victory.
See `BUDGETED_EVIDENCE_REPORT.md`.


## v0.6-alpha: Adaptive Multi-Round Evidence Acquisition

Run:

```bash
python -m dest_runtime.cli adaptive
```

v0.5 chooses an inspection portfolio once from initial estimates.

v0.6 instead performs:

```text
select one inspection
→ observe result
→ update related verification-debt beliefs
→ recompute priorities
→ select next inspection
→ repeat until budget is exhausted
```

The benchmark contains 40 episodes × 25 debts = 1,000 debts.

Debts are organized into public relation groups. Hidden validity outcomes are correlated within a group. A resolved inspection result can therefore increase or decrease the estimated invalidity of related debts.

New replayed state:
- `evidence_beliefs`
- `evidence_relations`

New event types:
- `BELIEF_INIT`
- `RELATION_INIT`
- `EVIDENCE_OBSERVED`
- `BELIEF_UPDATE`

The belief update is a heuristic log-odds rule. It is not labeled Bayesian because the runtime update model is not assumed to match the benchmark's exact hidden data-generating process.


### Measured v0.6 frozen holdout result

```text
v0.5 static total value:       135.777
v0.6 calibrated adaptive:      139.564
v0.6 coupling-gated:           136.224

static avg residual exposure:  3.8995
adaptive residual exposure:    3.8374
```

The calibrated adaptive policy has a positive holdout point estimate, but paired bootstrap intervals still cross zero. See `ADAPTIVE_EVIDENCE_REPORT.md`.
