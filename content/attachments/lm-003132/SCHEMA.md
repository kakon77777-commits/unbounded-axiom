# World-Domain Cognitive Runtime v0.1 — SCHEMA

**Purpose:** canonical v0.1 data model for the local reference runtime.  
**Storage target:** SQLite metadata + content-addressed blob store.

---

## 1. Schema Principles

### S1 — IDs Are Stable and Typed

Use stable opaque IDs with type prefixes where helpful:

```text
cand_
world_
run_
ckpt_
edge_
role_
chan_
claim_
ev_
agg_
comp_
commit_
learn_
tcd_
sed_
src_
```

Do not encode mutable state in IDs.

### S2 — Immutable Definition, Versioned Change

Objects such as `FutureCandidate`, `WorldSpec`, claim definitions, world contracts, and evidence aggregates are immutable by version.

Changes create a new version.

### S3 — Large Blobs Are Referenced

Metadata tables store `*_ref`, not arbitrarily large state blobs.

### S4 — Three Clocks Are Explicit

Where applicable:

```text
parent_time INTEGER
deliberation_index INTEGER
world_local_time INTEGER
```

### S5 — Scope Is Explicit

Events/evidence/action records declare:

```text
WORLD_LOCAL
PARENT_INTERNAL
EXTERNAL_REAL
```

### S6 — Provenance Is Never Optional for Consequential Objects

Forks, evidence, commits, and learning updates must resolve to upstream sources.

---

## 2. Core Entity Relationship

```text
TCDStateVersion
   |
   +--> FutureCandidate
            |
            +--> WorldSpec
                    |
                    +--> WorldRun
                            |
                            +--> Checkpoint
                            |      |
                            |      +--> ForkRecord --> Child WorldSpec
                            |
                            +--> Event
                            +--> EvidencePacket

Claim <-- EvidencePacket --> EvidenceAggregate
                            |
                            +--> GovernorDecision
                            +--> ComputationAction
                            +--> CommitRecord
                            +--> LearningEvent

CommitRecord --> RealAction --> RealOutcome --> SedimentationRecord --> TCDStateVersion'
```

---

## 3. Enums

### `scope`

```text
WORLD_LOCAL
PARENT_INTERNAL
EXTERNAL_REAL
```

### `domain_type`

```text
FORMAL_CLOSED
SIMULATED_DEFINED
EMPIRICAL_OPEN
```

### `world_status`

```text
PROPOSED
ADMITTED
QUEUED
RUNNING
PAUSED
COMPLETED
KILLED
FAILED
INVALIDATED
ARCHIVED
```

### `candidate_status`

```text
PROPOSED
ELIGIBLE
LIFTED
RETIRED
MERGED_SEMANTICALLY
INVALIDATED
RESOLVED
```

### `claim_type`

```text
UNIVERSAL
EXISTENTIAL
PROBABILISTIC
COMPARATIVE
CAUSAL
FORECAST
```

### `evidence_outcome`

```text
SUPPORT
COUNTER
INCONCLUSIVE
INVALID
```

### `source_class`

```text
REAL
EXTERNAL
WORLD
SYNTHETIC
DERIVED
UNKNOWN
```

### `learning_scope`

```text
WORLD_LOCAL
ENSEMBLE_RELATIVE
REALITY_FACING
```

### `contribution_type`

```text
PREDICTIVE
CONSTRUCTIVE
PREVENTIVE
MIXED
UNKNOWN
```

---

## 4. `tcd_state_versions`

```text
tcd_state_versions
  tcd_version_id TEXT PRIMARY KEY
  parent_time INTEGER NOT NULL
  past_base_ref TEXT NOT NULL
  present_base_ref TEXT NOT NULL
  future_base_ref TEXT NOT NULL
  provenance_ref TEXT
  parent_tcd_version_id TEXT
  created_at TEXT NOT NULL
```

Invariant:

```text
parent_time advances only on parent-real temporal shift
```

---

## 5. `future_candidates`

```text
future_candidates
  candidate_id TEXT PRIMARY KEY
  candidate_version INTEGER NOT NULL
  parent_candidate_id TEXT
  parent_tcd_version_id TEXT NOT NULL
  ontology_type TEXT NOT NULL
  content_ref TEXT NOT NULL
  probability_state_ref TEXT
  value_state_ref TEXT
  realization_paths_ref TEXT
  unknown_dependencies_ref TEXT
  evidence_refs_ref TEXT
  created_parent_time INTEGER NOT NULL
  created_deliberation_index INTEGER NOT NULL
  status TEXT NOT NULL
  created_at TEXT NOT NULL
```

Uniqueness:

```text
(candidate_id, candidate_version)
```

If using a stable logical candidate ID, use separate `candidate_version_id`.

---

## 6. `world_specs`

```text
world_specs
  world_id TEXT PRIMARY KEY
  candidate_id TEXT
  parent_world_id TEXT
  parent_checkpoint_id TEXT
  world_type TEXT NOT NULL
  backend_type TEXT NOT NULL
  backend_version TEXT NOT NULL
  contract_hash TEXT NOT NULL
  contract_ref TEXT NOT NULL
  dynamics_ref TEXT
  rules_ref TEXT
  actors_ref TEXT
  initial_state_ref TEXT
  budget_class TEXT
  authority_profile_ref TEXT NOT NULL
  purpose TEXT NOT NULL
  domain_type TEXT NOT NULL
  fidelity_profile_ref TEXT
  evidence_scope_ref TEXT
  status TEXT NOT NULL
  created_parent_time INTEGER
  created_deliberation_index INTEGER
  created_at TEXT NOT NULL
```

Hard invariant:

```text
world_id immutable
```

A material contract mutation creates a new `world_id`.

---

## 7. `world_runs`

```text
world_runs
  run_id TEXT PRIMARY KEY
  world_id TEXT NOT NULL
  start_checkpoint_id TEXT
  run_seed TEXT
  runtime_backend TEXT NOT NULL
  runtime_version TEXT NOT NULL
  worker_id TEXT
  status TEXT NOT NULL
  parent_time INTEGER NOT NULL
  deliberation_index INTEGER NOT NULL
  local_time_start INTEGER NOT NULL DEFAULT 0
  local_time_end INTEGER
  budget_allocated_ref TEXT NOT NULL
  budget_used_ref TEXT
  trace_ref TEXT
  outcome_ref TEXT
  termination_reason TEXT
  created_at TEXT NOT NULL
  ended_at TEXT
```

Foreign key:

```text
world_id -> world_specs.world_id
```

---

## 8. `checkpoints`

```text
checkpoints
  checkpoint_id TEXT PRIMARY KEY
  world_id TEXT NOT NULL
  run_id TEXT NOT NULL
  world_local_time INTEGER NOT NULL
  state_blob_ref TEXT NOT NULL
  actor_state_refs_ref TEXT
  rng_state_ref TEXT
  rules_version TEXT NOT NULL
  backend_version TEXT NOT NULL
  contract_hash TEXT NOT NULL
  trace_offset INTEGER
  resource_state_ref TEXT
  digest TEXT NOT NULL
  checkpoint_mode TEXT NOT NULL
  created_at TEXT NOT NULL
```

`checkpoint_mode`:

```text
EXACT
APPROXIMATE
```

Approximate checkpoints require a tolerance contract.

---

## 9. `world_edges`

```text
world_edges
  edge_id TEXT PRIMARY KEY
  parent_world_id TEXT
  parent_run_id TEXT
  child_world_id TEXT NOT NULL
  edge_type TEXT NOT NULL
  checkpoint_id TEXT
  fork_parent_local_time INTEGER
  divergence_type TEXT
  divergence_delta_ref TEXT
  seed_policy TEXT
  authority_delta_ref TEXT
  contract_hash TEXT
  created_at TEXT NOT NULL
```

Allowed `edge_type`:

```text
INSTANTIATE
CLONE
FORK
REPLAY
INTERVENE
MUTATE
MERGE_EVIDENCE
MERGE_LINEAGE
```

State merge is not a default edge.

Graph integrity test must reject cycles.

---

## 10. `role_cards`

```text
role_cards
  role_id TEXT PRIMARY KEY
  role_type TEXT NOT NULL
  world_scope_ref TEXT
  branch_scope_ref TEXT
  observation_scope_ref TEXT NOT NULL
  action_scope_ref TEXT NOT NULL
  tool_scope_ref TEXT NOT NULL
  external_authority_ref TEXT NOT NULL
  memory_scope_ref TEXT NOT NULL
  channel_allowlist_ref TEXT NOT NULL
  audit_level TEXT NOT NULL
  created_at TEXT NOT NULL
```

---

## 11. `channels`

```text
channels
  channel_id TEXT PRIMARY KEY
  source_role_id TEXT NOT NULL
  target_role_id TEXT NOT NULL
  channel_type TEXT NOT NULL
  allowed_content_types_ref TEXT NOT NULL
  direction TEXT NOT NULL
  delay_policy TEXT
  sanitization_policy_ref TEXT
  logging_policy TEXT NOT NULL
  authority_ref TEXT
  enabled INTEGER NOT NULL DEFAULT 1
  created_at TEXT NOT NULL
```

Paired branch blindness should have no enabled post-fork sibling channel.

---

## 12. `events`

```text
events
  event_id TEXT PRIMARY KEY
  event_type TEXT NOT NULL
  source TEXT NOT NULL
  subject TEXT
  event_time TEXT NOT NULL
  scope TEXT NOT NULL
  schema_version TEXT NOT NULL
  trace_id TEXT
  parent_time INTEGER
  deliberation_index INTEGER
  world_local_time INTEGER
  world_id TEXT
  run_id TEXT
  actor_id TEXT
  payload_ref TEXT
  provenance_ref TEXT
  reliability_class TEXT NOT NULL
```

Reliability classes:

```text
EPHEMERAL_TELEMETRY
PERSISTENT_OPERATION
EVIDENCE_CRITICAL
HISTORICAL_CRITICAL
```

---

## 13. `claims`

```text
claims
  claim_id TEXT PRIMARY KEY
  claim_type TEXT NOT NULL
  statement_ref TEXT NOT NULL
  domain TEXT NOT NULL
  scope_ref TEXT NOT NULL
  equivalence_contract_ref TEXT NOT NULL
  resolution_contract_ref TEXT
  target_domain_ref TEXT
  version INTEGER NOT NULL
  created_at TEXT NOT NULL
```

Claim equivalence should be fixed before aggregation where possible.

---

## 14. `evidence_packets`

```text
evidence_packets
  evidence_id TEXT PRIMARY KEY
  claim_id TEXT NOT NULL
  world_id TEXT
  run_id TEXT
  root_lineage_ref TEXT
  backend TEXT
  model_versions_ref TEXT
  data_sources_ref TEXT
  assumptions_ref TEXT
  evaluator_id TEXT
  evaluator_independence_ref TEXT
  outcome TEXT NOT NULL
  outcome_class_ref TEXT
  internal_validity_ref TEXT NOT NULL
  uncertainty_ref TEXT
  transport_scope_ref TEXT
  source_class TEXT NOT NULL
  synthetic_depth INTEGER NOT NULL DEFAULT 0
  provenance_ref TEXT NOT NULL
  created_at TEXT NOT NULL
```

`INVALID` evidence must never be silently recoded as `COUNTER`.

---

## 15. `world_families`

```text
world_families
  family_id TEXT PRIMARY KEY
  family_type TEXT NOT NULL
  family_key TEXT NOT NULL
  metadata_ref TEXT
  created_at TEXT NOT NULL
```

`family_type` may be:

```text
LINEAGE
BACKEND
MODEL
DATA
ASSUMPTION
EVALUATOR
```

Join table:

```text
world_family_memberships
  world_id
  family_id
  PRIMARY KEY(world_id, family_id)
```

---

## 16. `evidence_dependence`

```text
evidence_dependence
  evidence_id_a TEXT NOT NULL
  evidence_id_b TEXT NOT NULL
  lineage REAL
  backend REAL
  model REAL
  data REAL
  assumptions REAL
  evaluator REAL
  communication REAL
  projection REAL
  estimator_version TEXT
  PRIMARY KEY(evidence_id_a, evidence_id_b)
```

The projection column is optional.

Raw dependence dimensions must remain queryable.

---

## 17. `evidence_aggregates`

```text
evidence_aggregates
  aggregate_id TEXT PRIMARY KEY
  claim_id TEXT NOT NULL
  aggregate_version INTEGER NOT NULL
  method TEXT NOT NULL
  input_evidence_ids_ref TEXT NOT NULL
  family_summary_ref TEXT NOT NULL
  agreement_matrix_ref TEXT
  dependence_matrix_ref TEXT
  counterexamples_ref TEXT
  sensitivity_profile_ref TEXT
  transport_debt_ref TEXT
  unknown_world_mass_ref TEXT
  effective_count_status TEXT
  effective_count_ref TEXT
  created_at TEXT NOT NULL
```

`effective_count_status`:

```text
ESTIMATED
RANGE
UNRESOLVED
NOT_APPLICABLE
```

---

## 18. `computation_actions`

```text
computation_actions
  computation_id TEXT PRIMARY KEY
  target_type TEXT NOT NULL
  target_id TEXT
  operation TEXT NOT NULL
  requested_budget_ref TEXT NOT NULL
  fidelity_ref TEXT
  deadline TEXT
  purpose TEXT NOT NULL
  expected_value_vector_ref TEXT
  epistemic_deficit_ref TEXT
  portfolio_dependence_ref TEXT
  status TEXT NOT NULL
  proposed_by TEXT
  created_at TEXT NOT NULL
```

Operations:

```text
RUN_MORE
REPLICATE
FORK_COUNTER
EXPLORE_UNKNOWN
CROSS_BACKEND
REFINE_FIDELITY
STRESS_TAIL
CALIBRATE
TRANSPORT_TEST
EXTERNAL_TEST_PROPOSAL
```

---

## 19. `governor_decisions`

```text
governor_decisions
  decision_id TEXT PRIMARY KEY
  computation_id TEXT
  world_id TEXT
  operation TEXT NOT NULL
  governor_version TEXT NOT NULL
  mission_ref TEXT
  priority_vector_ref TEXT
  resource_state_ref TEXT NOT NULL
  expected_value_ref TEXT
  uncertainty_ref TEXT
  redundancy_ref TEXT
  safety_ref TEXT
  cost_ref TEXT
  deadline TEXT
  reason_ref TEXT NOT NULL
  override_ref TEXT
  created_at TEXT NOT NULL
```

---

## 20. `commit_records`

```text
commit_records
  commit_id TEXT PRIMARY KEY
  parent_time INTEGER NOT NULL
  proposed_action_ref TEXT NOT NULL
  supporting_claims_ref TEXT
  evidence_aggregate_ids_ref TEXT NOT NULL
  transport_debt_ref TEXT
  unknown_world_mass_ref TEXT
  counterexamples_ref TEXT
  safety_review_ref TEXT
  authority_required_ref TEXT NOT NULL
  decision TEXT NOT NULL
  authorizer_ref TEXT
  decision_reason_ref TEXT
  created_at TEXT NOT NULL
```

Decisions:

```text
APPROVE
DENY
DEFER
REQUEST_MORE_EVIDENCE
REQUEST_HUMAN
REQUEST_EXTERNAL_TEST
SAFE_FALLBACK
```

---

## 21. `real_actions` and `real_outcomes`

```text
real_actions
  real_action_id TEXT PRIMARY KEY
  commit_id TEXT NOT NULL
  parent_time INTEGER NOT NULL
  action_ref TEXT NOT NULL
  executor_ref TEXT
  executed_at TEXT NOT NULL
```

```text
real_outcomes
  real_outcome_id TEXT PRIMARY KEY
  real_action_id TEXT
  parent_time INTEGER NOT NULL
  observation_ref TEXT NOT NULL
  source_class TEXT NOT NULL
  observed_at TEXT NOT NULL
```

A real outcome may also arrive independently of a WDC commit.

---

## 22. `sedimentation_records`

```text
sedimentation_records
  sediment_id TEXT PRIMARY KEY
  parent_time INTEGER NOT NULL
  prior_tcd_version_id TEXT NOT NULL
  world_computations_used_ref TEXT
  ignored_worlds_ref TEXT
  evidence_used_ref TEXT
  counterexamples_ref TEXT
  transport_assumptions_ref TEXT
  unknown_world_mass_at_commit_ref TEXT
  chosen_real_action_id TEXT
  real_outcome_id TEXT
  dependency_changes_ref TEXT
  options_lost_ref TEXT
  options_opened_ref TEXT
  created_at TEXT NOT NULL
```

---

## 23. `learning_events`

```text
learning_events
  learning_event_id TEXT PRIMARY KEY
  target_component TEXT NOT NULL
  update_type TEXT NOT NULL
  learning_scope TEXT NOT NULL
  source_evidence_ids_ref TEXT NOT NULL
  source_classes_ref TEXT NOT NULL
  synthetic_depth INTEGER NOT NULL DEFAULT 0
  prior_version TEXT NOT NULL
  new_version TEXT NOT NULL
  validation_result_ref TEXT
  rollback_ref TEXT
  created_at TEXT NOT NULL
```

Hard rule:

```text
model/generator/Governor/TCD version change
=> LearningEvent exists
```

---

## 24. `source_registry`

```text
source_registry
  source_id TEXT PRIMARY KEY
  source_class TEXT NOT NULL
  producer_ref TEXT
  parent_source_ids_ref TEXT
  external_anchor INTEGER NOT NULL DEFAULT 0
  synthetic_depth INTEGER NOT NULL DEFAULT 0
  provenance_ref TEXT NOT NULL
  created_at TEXT NOT NULL
```

---

## 25. Blob Store Contract

Blob objects use content addressing:

```text
sha256
size
mime_type
storage_uri
compression
created_at
```

The database may keep a `blobs` table for reference counting and validation.

---

## 26. SQLite v0.1 Pragmas

Reference configuration:

```sql
PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;
PRAGMA synchronous = NORMAL;
```

Do not rely on WAL as a distributed database strategy.

---

## 27. Required Indexes

At minimum:

```text
events(event_type, event_time)
events(world_id, run_id)
world_runs(world_id, status)
world_edges(parent_world_id)
world_edges(child_world_id)
checkpoints(run_id, world_local_time)
evidence_packets(claim_id, outcome)
evidence_packets(world_id, run_id)
governor_decisions(world_id, created_at)
computation_actions(status, deadline)
commit_records(parent_time)
learning_events(target_component, created_at)
```

---

## 28. Schema Validation Invariants

Database-level or service-level tests must guarantee:

```text
unique world IDs
valid parent refs
acyclic world ancestry
valid checkpoint refs
child authority does not exceed parent without grant
aggregate inputs resolve
real action has commit record
learning update has LearningEvent
simulated event cannot become real historical fact
```

---

## 29. Migration Policy

Every schema migration has:

```text
migration_id
from_version
to_version
checksum
created_at
```

Never silently reinterpret old provenance after a schema change.

If semantics change, create a new schema version and preserve the old event payload.
