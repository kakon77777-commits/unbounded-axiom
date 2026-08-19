# Phase 12 Distributed Runtime Adapters Design

## Goal

Add a scheduler/execution substrate below the existing WDC Governor so existing world workloads can be placed and executed locally or translated to Ray/Kubernetes without changing evidence, TCD, commit, or learning semantics.

## Architecture

Introduce `wdc.scheduler` as the semantic boundary between epistemic governance and infrastructure scheduling. The Governor continues to decide whether/how much to compute. Scheduler adapters only decide feasibility, resource reservation, placement/execution, status, preemption, and release.

The canonical translation is:

```text
WorldRun / ComputationAction
        + Governor allocation
        -> WorkloadSpec
        -> SchedulerAdapter
        -> Local / Ray / Kubernetes substrate
```

No scheduler adapter may update evidence, TCD, commit records, learning versions, or world truth/moral-worth fields.

## Core Types

`ResourceBundle` carries CPU, GPU, memory MiB, and numeric custom resources.

`WorkloadSpec` carries workload identity, optional world/run/computation IDs, command, resources, placement strategy, priority/runtime class hints, image/namespace for Kubernetes, timeout, environment, and labels.

`SchedulerCapabilities` declares whether an adapter can execute, reserve atomically, preempt, render manifests, and whether it requires an optional dependency/external tool.

`Reservation` records a scheduler-side resource reservation.

`WorkloadHandle` records adapter, substrate ID, state, return code, captured stdout/stderr refs or text, and timestamps.

`SchedulerAdapter` exposes:

```text
capabilities()
feasible(workload)
reserve(workload)
submit(workload, reservation=None)
status(handle)
preempt(handle, reason)
release(reservation)
render(workload)
```

## Local Scheduler

`LocalScheduler` is the only v0.1 adapter guaranteed to execute in the reference environment. It has an explicit numeric capacity, supports reservations, and runs command workloads synchronously with `subprocess.run`. Resource accounting is logical, matching existing WDC Governor accounting; it does not attempt OS-level cgroup enforcement.

It persists scheduler workload/reservation records to SQLite so CLI output and demos remain auditable.

## Ray Adapter

`RaySchedulerAdapter` is optional and import-safe when Ray is not installed.

It must always support `render(workload)` without importing Ray. The rendered plan contains Ray resource bundles and placement strategy (`PACK`, `SPREAD`, `STRICT_PACK`, `STRICT_SPREAD`). When Ray is installed and execution is explicitly requested, it may create a placement group and submit a remote command task. No Ray dependency is added to core `dependencies`.

## Kubernetes Adapter

`KubernetesSchedulerAdapter` renders a `batch/v1 Job` manifest with:

```text
resources.requests / resources.limits
priorityClassName
runtimeClassName
restartPolicy: Never
labels containing WDC workload/world/run IDs
```

Actual cluster mutation is disabled by default. `submit` only executes `kubectl apply -f -` when the adapter is constructed with `allow_cluster_writes=True`; otherwise it rejects with an explicit error. No Kubernetes Python client dependency is required.

## Persistence

Add:

```text
scheduler_reservations
scheduler_workloads
```

These tables are infrastructure provenance only. They never become evidence packets automatically.

## CLI

Add:

```text
wdc scheduler adapters
wdc scheduler render --adapter local|ray|kubernetes --json ...
wdc scheduler local-run --json ...
```

`render` is side-effect free. `local-run` is synchronous and persists its workload record.

Do not expose Kubernetes cluster writes in the default CLI surface for Phase 12.

## Integration Demo

`wdc demo distributed-runtime`:

1. create a world spec/run;
2. allocate CPU/memory through `WorldGovernor`;
3. translate the allocation into a `WorkloadSpec`;
4. run a harmless local Python command through `LocalScheduler`;
5. render equivalent Ray and Kubernetes plans;
6. assert world evidence/TCD/history counts did not change merely because scheduling occurred.

## Hard Invariants

```text
Governor decides SHOULD-COMPUTE; Scheduler decides WHERE/WHEN/RUN.
Scheduler records are not evidence.
Scheduler execution does not advance parent_time.
Scheduler execution does not grant external authority.
Kubernetes cluster writes are default-deny.
Ray/Kubernetes optional dependencies are import-safe.
```

## Testing

TDD coverage must include resource feasibility/reservation, capacity release, local execution/status, Ray render mapping, Kubernetes Job manifest mapping, default-deny cluster mutation, CLI render/local-run, and the distributed-runtime integration demo.
