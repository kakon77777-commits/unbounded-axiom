# wdc-runtime

Local reference implementation for **World-Domain Cognitive Runtime v0.1**.

Current scope: **Phase 0–14** — ledger/world/checkpoint/fork kernel, role/authority isolation, bounded Governor state, dependence-aware evidence, computation-portfolio routing, an explicit sandbox Commit Gate, versioned TCD evidence assimilation / Historical Sedimentation, and an auditable World Ensemble Learning layer with source gates, holdout validation, rollback, Governor misses, and self-sealing warnings.

## Run tests

```bash
python -m pytest -q
```

## Run the Branching Grid demo

```bash
PYTHONPATH=src:. python examples/branching_grid.py /tmp/wdc-branching-grid
```

The demo creates one parent world, checkpoints it, forks two child worlds from the same exact prefix, applies divergent actions, persists fork events, and prints divergent terminal states.


## Run the Governed Evidence Grid demo

```bash
PYTHONPATH=src:. python examples/governed_evidence_grid.py /tmp/wdc-governed-evidence-grid
```

The demo adds sibling branch blindness, bounded Governor allocation, dependence-aware support/counter evidence, counterexample escalation, and redundant-branch tombstoning on top of the exact fork kernel.

## Run the Tri-Temporal Commit Grid demo

```bash
PYTHONPATH=src:. python examples/tri_temporal_commit_grid.py /tmp/wdc-tri-temporal-grid
```

This demo closes the first controlled TCD/WDC loop: governed branching evidence produces an independence deficit and a `CROSS_BACKEND` computation proposal; the counterevidence revises Future/Present/Past-relevance at the same parent time; an approved sandbox-only commit executes; only that executed sandbox outcome is sedimented into the next parent historical state.


## Run the World Ensemble Learning demo

```bash
PYTHONPATH=src:. python -m examples.world_ensemble_learning /tmp/wdc-world-learning
```

This demo adds Phase 9 learning on top of the tri-temporal loop: world-relative evidence can update Generator/FutureSpace versions, WORLD-only evidence is denied reality-facing promotion, a registered external calibration anchor allows a WorldModel candidate into validation, a deliberate holdout regression rolls it back, a GovernanceMiss calibrates the Governor meta-policy, and deteriorating external quality triggers self-sealing warnings. Learning itself does not advance parent historical time.

## Hard invariants already implemented

- `WorldSpec != WorldRun`
- three clock fields are explicit in the event envelope
- exact checkpoints preserve state, local time, and RNG state
- each fork creates a new world ID
- fork provenance records parent run, checkpoint, delta, and seed policy
- lineage cycles are rejected
- sibling post-fork access is denied without an explicit channel
- fork authority profiles cannot silently escalate external permissions
- mutable Governor lifecycle does not mutate immutable `WorldSpec`
- active Governor allocation cannot exceed the global budget
- `INVALID` evidence is not counterevidence
- aggregates preserve packet inputs and expose evidence-family dependence
- v0.1 does not fabricate a universal effective evidence count
- event payloads are persisted as snapshots
- computation actions are proposals, not execution authority
- Commit Gate verifies referenced evidence aggregates exist
- sandbox proxy requires an approved exact action payload
- TCD world-evidence assimilation preserves parent-real past facts and parent time
- sandbox Historical Sedimentation requires an approved commit + executed sandbox action
- `EXTERNAL_REAL` sedimentation requires a verified `PARENT_REAL_OBSERVATION` external ingest
- WORLD/SYNTHETIC/DERIVED evidence cannot self-promote to `REALITY_FACING` learning
- `REAL`/`EXTERNAL` reality-facing learning requires a registered anchor backed by a `VERIFIED` external ingest
- learning candidates activate only after holdout validation and can rollback
- learning-health warnings are diagnostic and do not mutate evidence/history automatically
- blobs are content-addressed and integrity-checked

See `docs/specs/` for the implementation contracts and `docs/superpowers/plans/` for the executed Phase 0–2, Phase 3–5, Phase 6–8, Phase 9, Phase 10, Phase 11, Phase 12, Phase 13, and Phase 14 plans.

## Phase 10 CLI

Phase 10 exposes the Phase 0–9 kernel through one JSON-first local command surface.

Initialize a workspace:

```bash
wdc --root /tmp/wdc-runtime init
wdc --root /tmp/wdc-runtime status
```

Complex payloads may be inline JSON or `@file.json`:

```bash
wdc --root /tmp/wdc-runtime tcd init --json @tcd-init.json
wdc --root /tmp/wdc-runtime world create --json @world.json
wdc --root /tmp/wdc-runtime evidence claim-create --json @claim.json
wdc --root /tmp/wdc-runtime portfolio route --json @deficit.json
wdc --root /tmp/wdc-runtime commit assess --json @commit.json
wdc --root /tmp/wdc-runtime learning propose --json @learning-update.json
```

Reference demos are available through the installed runtime surface:

```bash
wdc --root /tmp/wdc-demo demo branching-grid
wdc --root /tmp/wdc-demo demo governed-evidence
wdc --root /tmp/wdc-demo demo tri-temporal
wdc --root /tmp/wdc-demo demo learning
```

All successful CLI commands emit JSON to stdout. Expected domain/runtime failures emit a JSON error object to stderr with exit code `2`. The CLI delegates to the existing kernel services; it does not define alternate evidence, authority, TCD, or learning semantics.

## Phase 11 External Evidence / Adapter Layer

Phase 11 adds the first controlled non-WDC evidence boundary. External artifacts are read by adapters, stored as content-addressed blobs, registered with immutable source provenance, and only then may be converted into ordinary `EvidencePacket` objects.

Reference commands:

```bash
wdc --root /tmp/wdc-runtime external adapters
wdc --root /tmp/wdc-runtime external ingest --json @external-ingest.json
wdc --root /tmp/wdc-runtime external show <ingest_id>
wdc --root /tmp/wdc-runtime external evidence-add <ingest_id> --json @evidence.json
wdc --root /tmp/wdc-runtime demo external-evidence
```

The v0.1 reference adapter is `local-json`; it supports canonical inline JSON and local JSON files and performs no network access. A manual `learning source-anchor` record is no longer sufficient to unlock `REALITY_FACING` learning: the provenance must also resolve to a `VERIFIED` external ingest.

`EXTERNAL_REAL` Historical Sedimentation is now available only for verified ingests whose observation scope is `PARENT_REAL_OBSERVATION`. Ordinary external datasets remain evidence and cannot silently become parent-real historical facts.

## Phase 12 Distributed Runtime Adapters

Phase 12 adds an infrastructure scheduling layer **below** the WDC Governor. The semantic boundary is:

```text
Governor: Should this computation run, and with what epistemic/resource priority?
Scheduler: Is the workload feasible, where should it run, and what substrate state did it reach?
```

The scheduler layer does not create EvidencePackets, advance TCD parent time, grant external authority, or update learning versions.

Reference commands:

```bash
wdc scheduler adapters
wdc scheduler render --adapter ray --json @workload.json
wdc scheduler render --adapter kubernetes --json @workload.json
wdc --root /tmp/wdc-runtime scheduler local-run --json @local-workload.json
wdc --root /tmp/wdc-runtime demo distributed-runtime
```

Adapters:

- `local`: executable reference adapter with logical capacity/reservation accounting and synchronous subprocess execution.
- `ray`: optional adapter. Rendering works without Ray installed; execution requires an initialized Ray runtime. WDC maps one workload bundle to Ray placement-group resources and placement strategy.
- `kubernetes`: renders a `batch/v1 Job` with resource requests/limits plus optional `priorityClassName` and `runtimeClassName`. Cluster writes are disabled by default and require explicit adapter construction with write permission.

The Phase 12 reference environment validates LocalScheduler execution and Ray/Kubernetes render contracts. It does not claim a live Ray cluster or Kubernetes cluster was exercised.


## Phase 13 Worker Protocol / Remote World Execution

Phase 13 adds a transport-neutral worker boundary above the Phase 12 scheduler substrate. A parent runtime stages an immutable `WorkerEnvelope` plus content-addressed input artifacts; a worker process executes only a registered handler and returns a signed-by-digest `WorkerResult` plus content-addressed outputs. Parent-side ingest revalidates every digest before updating the original `WorldRun`, importing trace/outcome blobs, creating a checkpoint, and appending a `PARENT_INTERNAL` worker-result event.

Reference commands:

```bash
wdc --root /tmp/wdc-runtime worker stage --json @worker-task.json
wdc --root /tmp/wdc-runtime worker execute /tmp/wdc-runtime/worker_tasks/<task_id> --worker-id worker-a
wdc --root /tmp/wdc-runtime worker ingest /tmp/wdc-runtime/worker_tasks/<task_id>
wdc --root /tmp/wdc-runtime demo remote-world
```

Hard Phase 13 boundaries:

- `RemoteWorker != Governor != EvidenceAuthority`.
- the worker subprocess is not given the parent runtime root or SQLite path;
- arbitrary parent environment variables are not forwarded to the child worker;
- task directories are immutable once staged;
- worker result identity is bound to exact `task_id + envelope_digest + world_id + run_id`;
- returned artifacts are SHA-256 validated before parent import;
- duplicate result ingestion is rejected;
- worker execution/import does not create `EvidencePacket` automatically;
- worker execution/import does not advance TCD parent historical time;
- parent evaluation must explicitly turn an imported outcome into evidence.

The reference transport uses a task directory plus a stdio subprocess so protocol semantics can be validated without a network service. It is **not** a security sandbox: the child process still runs under the same operating-system identity unless combined with the Phase 4 container/gVisor/microVM isolation layer. Network RPC, worker authentication, Ray actor workers, and Kubernetes Job workers are deferred to later transport adapters.

## Phase 14 Worker Registry / Lease / Heartbeat / Retry / Remote Launchers

Phase 14 adds a durable distributed-control layer around the Phase 13 `WorkerEnvelope` protocol without moving Governor, evidence, Commit, or TCD authority onto workers.

Core components:

- `WorkerRegistry`: worker identity, resource capacity, labels/capabilities, heartbeat and stale-state tracking.
- `TaskLease`: one active lease per logical task, with monotonic attempt and fencing tokens.
- `WorkerCoordinator`: resource/capability-aware assignment, heartbeat renewal, stale-worker/lease sweep, retry directives, and stale-result fencing.
- `LocalWorkerLauncher`: lease-aware subprocess execution and parent ingest.
- `RayWorkerLauncher`: optional placement-group-based worker launch plan/execution using the existing Phase 12 Ray adapter.
- `KubernetesWorkerLauncher`: `batch/v1 Job` plus `coordination.k8s.io/v1 Lease` manifests with task/lease/attempt/fencing metadata; live cluster mutation remains default-deny.

Reference commands:

```bash
wdc --root /tmp/wdc-runtime workers register --json @worker.json
wdc --root /tmp/wdc-runtime workers list
wdc --root /tmp/wdc-runtime workers heartbeat <worker_id>
wdc --root /tmp/wdc-runtime workers assign <task_dir> --json @assignment.json
wdc --root /tmp/wdc-runtime workers sweep --json @sweep.json
wdc --root /tmp/wdc-runtime workers lease <task_id>
wdc --root /tmp/wdc-runtime workers render-launch <task_dir> --adapter ray --json @launch.json
wdc --root /tmp/wdc-runtime workers render-launch <task_dir> --adapter kubernetes --json @launch.json
wdc --root /tmp/wdc-runtime demo worker-leases
```

Hard Phase 14 boundaries:

- `RemoteWorker != Governor != EvidenceAuthority != CommitAuthority`.
- lease expiry is infrastructure state, not scientific/world failure.
- retry preserves the exact `WorkerEnvelope.digest`; only attempt/fencing identity changes.
- stale/late results are rejected before parent artifact ingest.
- only the current active lease holder may complete a task.
- worker registration/heartbeat/lease activity creates no evidence and does not advance TCD parent time.
- Ray worker workloads explicitly disable arbitrary environment inheritance.
- Kubernetes worker PVC mounts use a task-specific `subPath`, preventing multiple logical task directories from sharing the same `/wdc/task` view.
- Kubernetes Job `backoffLimit=0` keeps retry authority in WDC Coordinator instead of the substrate.

The reference environment fully exercises local leased subprocess execution, lease expiry/retry, fencing, stale-result rejection, and result deduplication. Ray and Kubernetes render/dependency/default-deny contracts are tested, but no live Ray cluster or live Kubernetes mutation is claimed for this environment.

## Phase 15 Authenticated Worker Control Plane + Distributed Artifact Service

Phase 15 replaces the Phase 13/14 shared-filesystem worker transport with an authenticated HTTP/JSON reference control plane. Worker credentials are HMAC-SHA256 bearer tokens bound to worker identity, registry generation, expiry, and explicit scopes. Re-registering a worker invalidates its previous credentials.

Reference commands:

```bash
wdc --root /tmp/wdc-runtime control credential --secret-file ./worker.secret --json @credential.json
wdc --root /tmp/wdc-runtime control submit --json @network-task.json
wdc --root /tmp/wdc-runtime control serve --secret-file ./worker.secret --host 127.0.0.1 --port 8765
wdc remote-worker once --base-url http://127.0.0.1:8765 --worker-id worker-a --token-file ./worker.token --work-root /tmp/wdc-worker
wdc --root /tmp/wdc-runtime demo network-worker
```

Hard Phase 15 boundaries:

- `RemoteWorker != Governor != EvidenceAuthority != CommitAuthority != TCDAuthority`.
- workers use scoped bearer credentials; worker-specific routes enforce token/path identity equality.
- worker re-registration increments generation and invalidates older bearer credentials.
- artifacts are SHA-256 addressed and reverified on transfer.
- artifact HTTP access is active-task-bound: workers may read only declared input artifacts and may upload only while holding the active lease for that task.
- stale attempt/fencing results are rejected before parent ingest.
- remote execution and transport do not create EvidencePacket and do not advance parent historical time.
- remote workers no longer need access to the parent runtime root, SQLite file, or shared worker task directory.

The Phase 15 HTTP server is a standard-library reference implementation for localhost/private-network protocol validation. It does not provide TLS/mTLS, public-internet hardening, production secret management, HA controller/database behavior, artifact quotas, or DDoS protection.
