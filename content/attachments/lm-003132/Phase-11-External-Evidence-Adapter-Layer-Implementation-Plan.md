# Phase 11 External Evidence / Adapter Layer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox syntax for tracking.

**Goal:** Add a provenance-gated external evidence ingestion layer and unlock verified `EXTERNAL_REAL` observation sedimentation without weakening existing evidence/authority boundaries.

**Architecture:** `ExternalEvidenceAdapter` reads an artifact; `ExternalEvidenceManager` stores content-addressed bytes, creates a durable ingest record and source anchor, and converts verified ingests into ordinary `EvidencePacket` objects. TCD external sedimentation verifies the ingest/anchor before advancing parent time. CLI is a thin translation layer over these services.

**Tech Stack:** Python 3.11+, standard library, SQLite, existing `BlobStore`, pytest, argparse CLI.

## Global Constraints

- No new runtime dependency.
- Use `python -m pytest`, not bare `pytest`, for verification.
- No HTTP/network adapter in Phase 11.
- No external adapter may directly create TCD history, learning updates, or commits.
- `EXTERNAL_REAL` sedimentation requires a verified `PARENT_REAL_OBSERVATION` ingest.
- Preserve all 77 Phase 0-10 tests.

---

### Task 1: Source Registry Service

**Files:**
- Create: `src/wdc/sources.py`
- Modify: `src/wdc/learning.py`
- Test: `tests/test_source_registry.py`

**Interfaces:**
- Produces: `SourceRegistry.register_anchor(...)`, `SourceRegistry.get_by_provenance(...)`, `SourceRegistry.is_registered_anchor(...)`.
- `LearningCoordinator.register_source_anchor(...)` delegates while preserving its current signature.

- [x] Write failing tests proving only REAL/EXTERNAL anchors are allowed, provenance is unique, and learning delegation remains compatible.
- [x] Run `python -m pytest tests/test_source_registry.py -q` and verify failure is due to missing source registry implementation.
- [x] Implement the minimal service and delegation.
- [x] Run targeted tests, then `python -m pytest -q`.
- [x] Commit `feat: add canonical external source registry`.

### Task 2: External Adapter + Ingest Persistence

**Files:**
- Create: `src/wdc/external.py`
- Modify: `src/wdc/db.py`
- Test: `tests/test_external_ingest.py`

**Interfaces:**
- Produces: `ExternalAdapterCapabilities`, `ExternalArtifact`, `ExternalIngestRecord`, `ExternalEvidenceAdapter`, `LocalJSONExternalAdapter`, `ExternalEvidenceManager.ingest(...)`, `get_ingest(...)`.
- Consumes: `BlobStore`, `SourceRegistry`, `SourceClass`.

- [x] Write failing tests for inline/file JSON canonicalization, content hash persistence, source anchor creation, invalid source class, malformed/missing file, and unsupported adapter.
- [x] Run targeted tests and verify the missing external module is the cause.
- [x] Add `external_ingests` migration/table and minimal implementation.
- [x] Run targeted tests and full suite.
- [x] Commit `feat: add external evidence ingest adapters`.

### Task 3: Verified Ingest -> EvidencePacket

**Files:**
- Modify: `src/wdc/external.py`
- Test: `tests/test_external_evidence_conversion.py`

**Interfaces:**
- Produces: `ExternalEvidenceManager.add_evidence_packet(...) -> EvidencePacket`.
- Consumes: existing `EvidenceEngine.add_packet(...)`.

- [x] Write failing tests proving verified ingest provenance/source class are forced into the packet, unknown ingest is rejected, and a forged label cannot substitute for an ingest.
- [x] Run targeted tests and verify expected failure.
- [x] Implement minimal conversion method.
- [x] Run targeted tests and full suite.
- [x] Commit `feat: convert verified external ingests into evidence packets`.

### Task 4: External-Real History Gate

**Files:**
- Modify: `src/wdc/tcd.py`
- Modify: `src/wdc/db.py`
- Test: `tests/test_external_tcd_sedimentation.py`

**Interfaces:**
- Extend `TCDStateManager.sediment_transition(..., external_ingest_id: str | None = None)`.
- Extend `SedimentationRecord` with `external_ingest_id`.

- [x] Write failing tests for unknown ingest, `PARENT_INTERNAL` ingest rejection, and verified `PARENT_REAL_OBSERVATION` advancing parent time exactly once.
- [x] Run targeted tests and verify current unconditional `EXTERNAL_REAL` rejection.
- [x] Add sedimentation column migration and verification logic.
- [x] Run targeted tests and full suite.
- [x] Commit `feat: gate external-real historical sedimentation by verified ingest`.

### Task 5: CLI External Surface

**Files:**
- Modify: `src/wdc/cli.py`
- Test: `tests/test_cli_external.py`

**Interfaces:**
- Add `wdc external adapters|ingest|show|evidence-add`.
- Extend `wdc tcd sediment` payload with optional `external_ingest_id`.

- [x] Write failing CLI tests covering inline/file ingest, show, evidence-add, and external sedimentation gate.
- [x] Run targeted tests and verify missing parser group is the cause.
- [x] Implement thin handlers over `ExternalEvidenceManager`.
- [x] Run targeted tests and full suite.
- [x] Commit `feat: expose external evidence adapters through CLI`.

### Task 6: End-to-End External Evidence Demo

**Files:**
- Create: `examples/external_evidence.py`
- Modify: `src/wdc/cli.py`
- Test: `tests/test_phase11_external_integration.py`

**Interfaces:**
- Add `wdc demo external-evidence`.

- [x] Write failing integration test for external observation -> evidence packet -> registered reality-facing learning source -> TCD external sedimentation.
- [x] Run targeted test and verify demo is missing.
- [x] Implement demo using only Phase 0-11 public services.
- [x] Run targeted test, full suite, `python -m compileall -q src/wdc examples`, and live CLI demo.
- [x] Commit `feat: add phase11 external evidence demo`.

### Task 7: Packaging, Report, Fresh-Archive Verification

**Files:**
- Modify: `README.md`
- Create: `PHASE11_IMPLEMENTATION_REPORT.md`
- Modify: this plan checklist only after verification evidence exists.

- [x] Run `git diff --check`.
- [x] Run full test suite.
- [x] Compile all source/examples.
- [x] Build wheel and install it into a clean venv; run `wdc external adapters` and `wdc demo external-evidence` outside the source tree.
- [x] Create tracked-only pre-completion Source ZIP and Git bundle.
- [x] Extract the pre-completion Source ZIP to a fresh directory and rerun full tests + demo.
- [x] Record verification output in the implementation report; final delivery hashes/HEAD are emitted in an external delivery manifest after the metadata commit to avoid self-referential artifact hashes.
- [ ] Commit docs/report after all evidence is available.
