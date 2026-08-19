# WDC Runtime Phase 14 Implementation Report

**Phase:** 14 — Worker Registry / Lease / Heartbeat / Retry + Remote Launchers  
**Branch:** `feature/phase14`  
**Base:** Phase 13 `d2703316fe4d015ae89920fabb0f1d9bb144a26e`  
**Status:** implementation complete; tracked-only source archive gate verified; final artifact hashes recorded externally

## 1. Goal

Connect the Phase 13 `WorkerEnvelope` execution protocol to a durable worker fleet/control layer with liveness, task leases, fencing, retry, and protocol-aware Local/Ray/Kubernetes launchers while preserving parent epistemic and authority boundaries.

## 2. Implemented Components

### Worker Registry

`src/wdc/worker_registry.py`

- durable worker registration;
- resource capacity, labels and capabilities;
- `ACTIVE / STALE / DRAINING / OFFLINE` states;
- heartbeat renewal and stale-worker sweep.

### Task Leases and Retry

- at most one `ACTIVE` lease per logical task;
- lease binds exact task ID, envelope digest, worker ID, attempt and fencing token;
- attempts/fencing tokens increase monotonically;
- lease expiry and stale-worker loss return retry directives without classifying the world/scientific task as failed.

### Worker Coordinator

`src/wdc/worker_coordinator.py`

- resource/capability-aware worker eligibility;
- assignment and renewal;
- lease/worker sweep;
- stale-result fencing;
- wrong-worker result rejection;
- accepted result completes the current lease.

### Lease-Aware Local Launcher

`src/wdc/worker_launcher.py`

- stages and executes the existing Phase 13 task-directory protocol;
- validates current assignment before parent ingest;
- stale results are rejected before returned artifacts enter the parent BlobStore;
- parent ingest remains the only path to run/checkpoint/event updates.

### Ray Worker Launcher

`src/wdc/worker_launcher_ray.py`

- maps the same `WorkerEnvelope` protocol to Phase 12 Ray placement-group scheduling;
- carries task/lease/attempt/fencing metadata;
- worker workload uses `inherit_environment=False`, preventing generic Ray subprocess execution from reintroducing arbitrary remote-node environment inheritance;
- import-safe when Ray is absent.

### Kubernetes Worker Launcher

`src/wdc/worker_launcher_kubernetes.py`

- renders `batch/v1 Job` and `coordination.k8s.io/v1 Lease` objects;
- Job labels carry task/lease/attempt/fencing/world/run identity;
- `backoffLimit=0` leaves retry policy with WDC Coordinator;
- optional active deadline / finished TTL / RuntimeClass / PriorityClass;
- PVC task mount uses `subPath=<task_id>` by default;
- live cluster writes remain disabled unless explicitly enabled.

### CLI / Demo

New control-plane commands:

```text
wdc workers register
wdc workers list
wdc workers heartbeat
wdc workers assign
wdc workers sweep
wdc workers lease
wdc workers render-launch
wdc demo worker-leases
```

## 3. New Hard Invariants

$$
\boxed{
\text{Lease Expiry}
\neq
\text{Task / Scientific Failure}
}
$$

$$
\boxed{
\text{Late Result from Stale Attempt}
\neq
\text{Acceptable Result}
}
$$

$$
\boxed{
\text{Retry}
=
\text{Same Envelope Digest}
+
\text{New Attempt/Fencing Token}
}
$$

$$
\boxed{
\text{Worker Liveness / Scheduling}
\not\Rightarrow
\text{Evidence or TCD Mutation}
}
$$

## 4. Security / Provenance Hardening

The pre-delivery review found and fixed two important substrate leaks:

1. Generic Ray subprocess execution inherited the remote process environment. `WorkloadSpec` now has an `inherit_environment` policy (default `True` for compatibility), and Ray worker workloads explicitly set it to `False`. LocalScheduler has a regression test confirming explicit-only execution does not inherit an injected secret variable.
2. Kubernetes worker Jobs previously mounted the root of a shared PVC at `/wdc/task`. Worker Jobs now default to `subPath=<task_id>`, isolating each logical task directory within a shared PVC.

## 5. Reference Retry Demo

The Phase 14 demo deliberately runs attempt 1, lets its lease expire before ingest, then retries the exact same logical task on a second worker.

Observed source-tree demo values:

```text
attempt_1 = 1
fence_1 = 1
retry_reason = lease_expired
attempt_2 = 2
fence_2 = 2
stale_result_rejected = true
final_run_status = COMPLETED
final_lease_status = COMPLETED
worker_result_event_count = 1
evidence = 0 -> 0
parent_time = 0 -> 0
```

This demonstrates that the stale attempt can physically produce a result but cannot cross the fencing boundary into parent ingest.

## 6. Current Verification

At the pre-artifact stage after security hardening:

```text
python -m pytest -q
152 passed

python -m compileall -q src/wdc examples
PASS

git diff --check
PASS
```

Tracked-only Source ZIP verification from the pre-final metadata commit also passed:

```text
fresh extraction tests = 152 passed
fresh extraction compileall = PASS
fresh source demo = PASS
fresh wheel build/install = PASS
fresh installed demo = PASS
```

Final Source ZIP / Git bundle / wheel hashes and final-HEAD verification are recorded in the external delivery manifest so artifact hashes do not create a self-referential source commit.

## 7. Environment Limitations

The current execution environment does not provide a live Ray cluster or Kubernetes cluster/kubectl path suitable for mutation testing. Therefore:

- Local lease/heartbeat/retry/fencing/subprocess execution is actually executed end-to-end.
- Ray placement/render/dependency contracts are tested; live Ray remote execution is **not claimed**.
- Kubernetes Job/Lease render and default-deny mutation contracts are tested; live Kubernetes Job/Lease application is **not claimed**.
- No HTTP/gRPC control plane, TLS/mTLS worker identity, or distributed artifact server is included in Phase 14.

## 8. Result

Phase 14 turns Phase 13's one-shot worker protocol into a restartable distributed control model:

```text
Worker Registration
-> Assignment
-> Lease
-> Execute
-> Heartbeat/Renew
-> Expire/Loss
-> Retry with New Fence
-> Stale Result Reject
-> Current Result Accept
-> Parent Ingest
```

without moving evidence, Commit, or TCD authority onto the worker fleet.
