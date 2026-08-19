# WDC Runtime Phase 11 — External Evidence / Adapter Layer Implementation Report

Date: 2026-08-17  
Branch: `feature/phase11`  
Code HEAD before report/checklist commit: `4915c001da6922f218b0184d959b1beaa4cd8a40`

## Scope Delivered

Phase 11 adds the first controlled non-WDC evidence boundary:

- canonical `SourceRegistry` shared by learning and external ingestion;
- `ExternalEvidenceAdapter` protocol;
- `LocalJSONExternalAdapter` reference backend for inline/local-file JSON;
- content-addressed external artifact storage;
- durable `external_ingests` provenance records;
- verified ingest -> ordinary `EvidencePacket` conversion;
- adapter-backed reality-facing learning gate;
- verified `PARENT_REAL_OBSERVATION` -> `EXTERNAL_REAL` Historical Sedimentation;
- `wdc external adapters|ingest|show|evidence-add` CLI surface;
- `wdc demo external-evidence` end-to-end reference loop.

## Hardening Added During Review

Phase 9 previously allowed a manually registered `REAL`/`EXTERNAL` source anchor to satisfy the reality-facing learning gate. Phase 11 intentionally tightens that boundary:

```text
manual source_registry anchor
!=
verified external ingest anchor
```

A reality-facing update now requires an evidence provenance that resolves to both:

1. a registered source anchor; and
2. a `VERIFIED` row in `external_ingests` with matching provenance/source class.

The old `learning source-anchor` API remains available as provenance metadata, but it is no longer sufficient to unlock reality-facing learning.

## History Firewall

`EXTERNAL_REAL` sedimentation is no longer unconditionally disabled. It is allowed only when the supplied ingest is:

- present in `external_ingests`;
- `VERIFIED`;
- source class `REAL` or `EXTERNAL`;
- backed by a matching registered anchor;
- observation scope `PARENT_REAL_OBSERVATION`.

A `PARENT_INTERNAL` external dataset remains evidence and cannot be silently promoted into parent-real history.

## Preliminary Verification Evidence

Fresh verification on the implementation tree before final archive generation:

```text
git diff --check: PASS
python -m pytest -q: 94 passed
python -m compileall -q src/wdc examples: PASS
live source-tree external-evidence demo: PASS
wheel build: PASS
clean venv wheel install: PASS
installed wdc external adapters: PASS
installed wdc demo external-evidence: PASS
```

Reference installed adapter output:

```json
{"adapters": ["local-json"]}
```

Reference demo properties:

```text
ingest_validation_status = VERIFIED
observation_scope = PARENT_REAL_OBSERVATION
evidence_source_class = REAL
evidence_provenance_matches_ingest = true
learning_source_classes = [REAL]
learning_status = APPLIED
parent_time_before = 0
parent_time_after = 1
sedimentation_external_ingest_matches = true
world_history_laundered = false
```

## Deferred to Phase 12+

- network/HTTP polling adapters;
- Gmail/Drive/web connector adapters;
- distributed Ray/Kubernetes scheduler adapters;
- background monitoring;
- automatic external actions;
- external source trust scoring beyond explicit provenance/validation contracts.

## Pre-Completion Archive Verification

The tracked-only pre-completion Source ZIP was extracted into a fresh directory and independently verified:

```text
python -m pytest -q: 94 passed
python -m compileall -q src/wdc examples: PASS
PYTHONPATH=src:. python -m wdc ... demo external-evidence: PASS
```

Pre-completion archive SHA-256 values:

```text
Source ZIP: b78f0cfe2065dd66f20ef2326e3d72238b8b20b75e1565127baba8dffd6507db
Git bundle: f964cf6b8fdb864f57a8de05998977fd4dad6d4932a6c4cf16e068c3134b78c2
```

Final delivery artifacts are rebuilt from the subsequent metadata/checklist commit. Their hashes and final-archive verification are emitted outside the tracked source tree to avoid changing the artifact while recording its own hash.
