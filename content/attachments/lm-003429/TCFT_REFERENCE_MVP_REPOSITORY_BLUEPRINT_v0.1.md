# TCFT-BTAP Reference MVP — Repository Blueprint v0.1

```text
tcft-btap/
├─ README.md
├─ pyproject.toml
├─ docs/
│  ├─ TCFT_Benchmark_Temporal_Audit_Protocol_v0.1.md
│  ├─ architecture.md
│  ├─ governance.md
│  └─ benchmark_policy.md
├─ schemas/
│  ├─ tcft_audit_v0.1.schema.json
│  ├─ metric_plugin_v0.1.schema.json
│  └─ benchmark_case_v0.1.schema.json
├─ src/tcft/
│  ├─ __init__.py
│  ├─ models/
│  │  ├─ audit.py
│  │  ├─ evidence.py
│  │  ├─ baseline.py
│  │  └─ frontier.py
│  ├─ provenance/
│  │  ├─ hashing.py
│  │  └─ registry.py
│  ├─ temporal/
│  │  ├─ cutoff.py
│  │  └─ date_confidence.py
│  ├─ decomposition/
│  │  └─ trace.py
│  ├─ prior_art/
│  │  ├─ base.py
│  │  └─ providers/
│  ├─ baselines/
│  │  ├─ base.py
│  │  ├─ contamination.py
│  │  └─ ensemble.py
│  ├─ structure/
│  │  ├─ problems.py
│  │  ├─ future_space.py
│  │  ├─ counterfactual.py
│  │  ├─ reflexive.py
│  │  ├─ operator.py
│  │  ├─ program.py
│  │  └─ domain_seed.py
│  ├─ metrics/
│  │  ├─ base.py
│  │  ├─ tn.py
│  │  ├─ pg.py
│  │  ├─ cf.py
│  │  ├─ rg.py
│  │  ├─ rp.py
│  │  └─ nc.py
│  ├─ correction/
│  │  ├─ failures.py
│  │  └─ volume.py
│  ├─ evidence/
│  │  └─ confidence.py
│  ├─ frontier/
│  │  ├─ normalize.py
│  │  ├─ pareto.py
│  │  └─ longitudinal.py
│  ├─ ledger/
│  │  ├─ append_only.py
│  │  └─ revision.py
│  ├─ governance/
│  │  ├─ anti_crown.py
│  │  ├─ language_guard.py
│  │  └─ policy.py
│  ├─ reporting/
│  │  └─ markdown.py
│  └─ cli.py
├─ benchmarks/
│  ├─ b0_synthetic/
│  │  ├─ fixtures/
│  │  └─ expected/
│  ├─ b1_historical/
│  ├─ b2_contemporary/
│  └─ b3_reflexive/
├─ tests/
│  ├─ unit/
│  ├─ integration/
│  ├─ regression/
│  └─ acceptance/
└─ examples/
   └─ minimal_audit/
```

## Implementation Order

### Phase 0 — Protocol Kernel
- schema
- provenance
- temporal gate
- ledger
- B0 fixtures
- governance blockers

### Phase 1 — Retrieval / Baseline
- provider abstraction
- contamination classes C0–C4
- baseline ensemble
- prior-art records

### Phase 2 — Functional Metrics
- TN
- PG
- CF
- RG

### Phase 3 — Structural Metrics
- RP
- NC
- CODT recovery interface

### Phase 4 — Dynamic Frontier
- normalization
- Pareto
- historical/current/persistent
- revision dashboard

## First PR Boundary

第一個可審核 PR 應只包含：

- schemas
- audit models
- temporal cutoff
- contamination enum
- append-only ledger
- B0 synthetic fixtures
- unit / acceptance tests

**不要**在第一個 PR 就加入 LLM provider、historical celebrities 或漂亮 UI。

原因：先證明 protocol kernel 不會洩漏、不會覆寫、會降級，再加入智能層。
