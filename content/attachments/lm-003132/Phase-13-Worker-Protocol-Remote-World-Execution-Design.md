# Phase 13 Worker Protocol / Remote World Execution Design

## Goal

Make an existing WDC `WorldRun` portable across a worker boundary while preserving identity, artifact integrity, checkpoint provenance, and parent-only evidence/authority semantics.

## Architecture

The parent creates an immutable `WorkerEnvelope` that names `world_id`, `run_id`, backend handler, clocks, budget, input artifact descriptors, and execution payload. A transport stager writes the envelope and content-addressed inputs into an isolated task directory. A worker process reads only that task directory, executes a registered handler, and writes a `WorkerResult` plus content-addressed outputs.

The parent `WorkerResultIngestor` validates the original envelope digest, world/run identity, result digest, and every returned artifact digest before importing anything into the parent blob store. It may update `WorldRun`, create a checkpoint, and append parent-internal worker events. It may not create evidence or mutate TCD. A later parent-side evaluator may explicitly turn the imported outcome into an `EvidencePacket`.

## Core invariants

1. `RemoteWorker != Governor != EvidenceAuthority`.
2. Worker never opens the parent `wdc.sqlite3`.
3. Worker inputs/outputs are content-addressed and digest-verified.
4. A result is accepted only for the exact staged envelope digest + `world_id` + `run_id`.
5. Remote execution does not advance parent historical time.
6. Remote execution does not create `EvidencePacket` automatically.
7. Returned checkpoints are imported only after digest verification and are attached to the original run.
8. Worker protocol stays transport-neutral: stdio/task-directory is reference transport; Ray/Kubernetes may launch the same protocol later.

## Components

### `wdc.worker_protocol`

Defines `ArtifactDescriptor`, `WorkerEnvelope`, `WorkerResult`, statuses, deterministic JSON serialization, and envelope/result digests.

### `wdc.worker_transport`

Stages task directories:

```text
<task-dir>/
  envelope.json
  inputs/<sha256>
  outputs/<sha256>
  result.json
```

It verifies filenames, sizes, and SHA-256 values.

### `wdc.worker_runtime`

Contains handler registry and reference handler `python-state-grid-v1`. The handler creates a `PythonStateWorld`, optionally restores an input checkpoint, executes a bounded action sequence, then emits trace, outcome, and exact checkpoint artifacts.

### `wdc.worker_client`

Reference subprocess client launches `python -m wdc.worker execute --task-dir ...`. It does not pass the parent database path.

### `wdc.worker_ingest`

Parent-only ingest validates identity and digests, imports artifacts, updates `WorldRun`, creates checkpoint rows, and emits parent-internal events.

## Error handling

Tampered envelopes, missing artifacts, digest mismatches, world/run mismatch, unsupported handler, and malformed result are hard failures. A failed worker result may be imported as run failure provenance only if its result envelope itself validates.

## Testing

Use TDD. Tests cover deterministic round trips, tamper rejection, task-directory staging, in-process handler execution, real subprocess execution, result identity checks, checkpoint import, run update, zero automatic evidence creation, and no TCD time advance.

## Scope exclusions

No network RPC protocol, TLS, worker authentication PKI, distributed artifact service, Ray actor execution, Kubernetes Job execution, remote external tools, or autonomous evidence/commit authority in Phase 13.
