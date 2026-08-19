# WDC Runtime Phase 13 Implementation Report

**Phase:** 13 — Worker Protocol / Remote World Execution
**Date:** 2026-08-17
**Branch:** `feature/phase13`
**Base:** Phase 12 (`6c171c843f50268280145cc4606b6ff2a67ea037`)

## Scope completed

Phase 13 makes an existing WDC `WorldRun` portable across an isolated worker-process protocol boundary without delegating parent epistemic or historical authority.

Implemented:

- immutable `ArtifactDescriptor`, `WorkerEnvelope`, and `WorkerResult` protocol objects;
- canonical JSON serialization and SHA-256 envelope/result binding;
- content-addressed task-directory staging for worker inputs and outputs;
- immutable task-directory staging guard;
- registered `WorkerHandlerRegistry` with reference `python-state-grid-v1` handler;
- bounded action execution through `PythonStateWorld`;
- checkpoint-resume input support;
- worker-produced `trace.jsonl`, `outcome.json`, and exact checkpoint artifacts;
- subprocess worker entrypoint: `python -m wdc.worker execute ...`;
- `StdioWorkerClient` with allowlisted child environment rather than arbitrary parent-env forwarding;
- parent-only `WorkerResultIngestor`;
- exact envelope/result/world/run identity validation;
- parent BlobStore re-import and SHA-256 validation;
- original `WorldRun` completion update;
- exact returned checkpoint import;
- `PARENT_INTERNAL` `WorkerResultAccepted` event;
- duplicate result-ingest rejection;
- CLI `worker stage / execute / ingest`;
- `remote-world` end-to-end demo;
- explicit parent-side EvidencePacket creation after ingest.

## Reference execution flow

```text
Parent WorldRun
  -> WorkerEnvelope
  -> task directory + input artifacts
  -> subprocess worker
  -> WorkerResult + output artifacts
  -> parent digest/identity validation
  -> WorldRun + checkpoint + event import
  -> explicit parent evaluator
  -> EvidencePacket
```

## Hard boundaries verified

```text
RemoteWorker != Governor
RemoteWorker != EvidenceAuthority
WorkerExecution != HistoricalSedimentation
WorkerResultImport != EvidenceCreation
```

Worker execution and result ingest preserve parent TCD time. The reference integration demo shows evidence count remains zero through worker execution and ingest, then becomes one only when the parent explicitly registers a claim and evaluator-created packet.

## Security / isolation note

The Phase 13 stdio worker is a **protocol isolation reference**, not a process-security sandbox. It deliberately does not receive the parent runtime root/database argument and arbitrary parent environment variables are filtered, but it still runs under the same OS identity as the parent process. Strong host isolation remains the responsibility of the Phase 4 sandbox layer (container / gVisor / microVM) or future remote worker deployment.

## Preliminary verification evidence

Before completion metadata and final artifact generation:

```text
python -m pytest -q                  -> 130 passed
python -m compileall -q src/wdc examples -> PASS
git diff --check                    -> PASS
source-tree remote-world demo       -> PASS
wheel build                         -> PASS
clean-venv wheel install            -> PASS
installed wdc demo remote-world     -> PASS
```

## Deferred

- network RPC transport;
- mTLS / worker identity authentication;
- distributed artifact/object-store transport;
- Ray actor worker launcher;
- Kubernetes Job worker launcher;
- remote external-tool authority;
- automatic worker-result-to-evidence promotion.

These are intentionally deferred so Phase 13 remains a small, auditable protocol layer.
