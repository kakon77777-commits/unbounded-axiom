# Phase 14 Worker Registry / Lease / Heartbeat / Retry / Remote Launcher Design

## Goal

Connect Phase 12 scheduling and Phase 13 worker execution with a durable worker-control protocol that can safely assign tasks, track liveness, recover from worker loss, reject stale results, and launch the same WorkerEnvelope protocol through local/Ray/Kubernetes substrates without delegating epistemic authority.

## Architecture

The parent runtime owns a central `WorkerRegistry` and `WorkerCoordinator`. Workers register an immutable worker identity plus declared capabilities/resources, then renew heartbeats. The coordinator grants a time-bounded `TaskLease` for an existing `WorkerEnvelope`. Every assignment carries an incrementing attempt number and fencing token.

A launcher receives a `WorkerAssignment` and starts the already-defined Phase 13 worker protocol. The worker remains a pure executor. A returned `WorkerResult` is wrapped with the assignment context and must pass current-lease/fencing checks before the existing `WorkerResultIngestor` may import it. If a worker disappears or a lease expires, the coordinator marks the attempt expired and may create a retry directive for the same logical task/envelope. A late result from an older fencing token is rejected even if its WorkerResult digest is otherwise valid.

Phase 14 keeps registry/lease semantics local to the parent SQLite control plane. It does not introduce a network RPC service. Local leased execution is the fully executable reference path. Ray and Kubernetes adapters must map the same assignment/envelope semantics, but live cluster execution remains optional and dependency-gated.

## Core invariants

1. `RemoteWorker != Governor != EvidenceAuthority != CommitAuthority`.
2. Worker registration and heartbeat do not create EvidencePackets or TCD history.
3. At most one ACTIVE lease exists for a logical `task_id` at a time.
4. Every lease is bound to exact `task_id + envelope_digest + worker_id + attempt + fencing_token`.
5. Fencing tokens increase monotonically for a task.
6. Lease expiry is not itself scientific/task failure; it is an infrastructure-control event.
7. Retry reuses the same logical WorkerEnvelope identity/digest and increments attempt/fencing metadata.
8. A result from an expired/replaced attempt is stale and must be rejected before parent artifact ingest.
9. Result deduplication from Phase 13 still applies after lease validation.
10. Scheduler/launcher/lease records do not mutate Evidence, Commit, Learning, or TCD state.
11. Worker heartbeat must not require access to parent evidence or TCD tables.
12. Kubernetes cluster writes remain default-deny.

## Components

### `wdc.worker_registry`

Defines:

- `WorkerStatus`: ACTIVE, STALE, DRAINING, OFFLINE.
- `WorkerRecord`: identity, labels, capabilities, resource capacity, last heartbeat, generation.
- `TaskLeaseStatus`: ACTIVE, COMPLETED, EXPIRED, RELEASED.
- `TaskLease`: task/envelope/worker binding, attempt, fencing token, acquired/renew/expires timestamps.
- `RetryDirective`: same task/envelope with next attempt and reason.
- `WorkerRegistry`: durable SQLite persistence and queries.

The registry must use injected/current timestamps so lease expiry can be tested deterministically.

### `wdc.worker_coordinator`

Orchestrates:

- register worker;
- heartbeat worker;
- assign envelope to eligible worker;
- renew lease;
- mark worker stale/offline;
- expire leases;
- produce retry directives;
- validate assignment-bound results;
- complete/release lease after accepted result.

The coordinator does not launch processes itself and does not call Evidence/TCD APIs.

### `wdc.worker_launcher`

Defines a launcher protocol and fully executable `LocalWorkerLauncher`.

`LocalWorkerLauncher` uses Phase 13 task-directory staging + `StdioWorkerClient`, and reports results back through `WorkerCoordinator.accept_result()` before `WorkerResultIngestor.ingest()`.

### `wdc.worker_launcher_ray`

Optional adapter. It must be import-safe without Ray. It maps a `WorkerAssignment` to the existing Ray scheduler/placement-group semantics. When Ray is available, execution may run the Phase 13 worker protocol remotely; otherwise render/plan remains usable and live launch raises a clear dependency error.

### `wdc.worker_launcher_kubernetes`

Optional/default-deny adapter. It renders a `batch/v1 Job` plus WDC lease labels/annotations. Kubernetes-native Lease mapping uses `coordination.k8s.io/v1` fields compatible with `holderIdentity`, `leaseDurationSeconds`, and `renewTime`. Live Job/Lease mutation requires explicit enablement and `kubectl`; otherwise render-only behavior is allowed.

## Lease and retry state machine

```text
UNASSIGNED
  -> ACTIVE(attempt=1, fence=1)
  -> COMPLETED

ACTIVE
  -> EXPIRED
  -> RETRY_DIRECTIVE(attempt=2)
  -> ACTIVE(attempt=2, fence=2)
```

A late attempt-1 result after fence=2 exists is rejected as stale.

## Worker status state machine

```text
ACTIVE --heartbeat timeout--> STALE
STALE --heartbeat--> ACTIVE
ACTIVE --drain--> DRAINING
DRAINING --no active leases--> OFFLINE
```

A stale worker must not receive new assignments.

## Eligibility

Reference eligibility is deterministic and minimal:

- worker status ACTIVE;
- worker has free task slot;
- declared resources satisfy envelope budget/resource request if provided;
- optional labels match assignment requirements.

No epistemic ranking belongs in worker selection.

## Kubernetes mapping

Kubernetes Jobs are execution substrate only. Phase 14 render should include:

- `batch/v1 Job`;
- labels: task ID, worker/attempt/fencing metadata where applicable;
- `activeDeadlineSeconds` from workload timeout when available;
- `backoffLimit: 0` so WDC RetryCoordinator remains the retry authority;
- optional `ttlSecondsAfterFinished`;
- existing priority/runtime class mapping.

A separate `coordination.k8s.io/v1 Lease` manifest may represent WDC worker/assignment liveness, but WDC's parent SQLite lease remains the canonical semantic record in the reference runtime.

## Ray mapping

Ray placement groups remain the resource reservation substrate. Phase 14 must wait for placement group readiness before launching a worker task/actor, and assignment metadata is passed explicitly to the worker invocation. Ray's own retry/fault-tolerance features must not silently create new WDC logical attempts unless the adapter reports them back to the coordinator.

## Error handling

Hard failures:

- duplicate active lease for task;
- wrong worker renewing lease;
- expired lease renewal;
- stale fencing token result;
- envelope digest mismatch;
- assignment/result world/run mismatch;
- result from unregistered worker;
- live Kubernetes mutation when writes disabled;
- live Ray launch when dependency unavailable.

Worker loss and lease expiry are recoverable infrastructure events and may create retry directives.

## Testing

Use TDD. Cover:

- worker register/heartbeat/stale recovery;
- one-active-lease invariant;
- monotonic attempts/fencing;
- expiry and retry directive;
- late stale result rejection;
- accepted result completion;
- local leased end-to-end execution;
- zero evidence/TCD mutation from registry/lease/launcher activity;
- Ray import-safe render/dependency error;
- Kubernetes Job + Lease manifest render and default-deny cluster writes;
- CLI register/heartbeat/assign/sweep/status plus integrated demo.

## Scope exclusions

No HTTP/gRPC control plane, TLS/PKI worker authentication, distributed SQL, object-store artifact service, multi-region consensus, Byzantine workers, automatic external credentials, or autonomous evidence/commit authority in Phase 14.
