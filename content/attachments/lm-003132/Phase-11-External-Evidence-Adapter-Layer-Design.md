# Phase 11 External Evidence / Adapter Layer Design

## Goal

Add the first controlled boundary from non-WDC data into the local WDC runtime without allowing external data to bypass provenance, evidence, learning, or historical-sedimentation gates.

## Scope

Phase 11 implements:

- an `ExternalEvidenceAdapter` protocol;
- one reference `LocalJSONExternalAdapter`;
- durable external ingest records with content hashes and blob references;
- canonical external source-anchor registration;
- conversion of a verified ingest into an `EvidencePacket`;
- controlled `EXTERNAL_REAL` TCD sedimentation from a verified parent-real observation ingest;
- CLI commands under `wdc external`;
- one end-to-end external-evidence demo.

Phase 11 explicitly defers:

- HTTP polling;
- Gmail/Drive/web connectors;
- Ray/Kubernetes scheduling;
- automatic real-world actions;
- background monitoring;
- neural world-model training.

## Architecture

The selected approach is **pull/ingest first**:

```text
External Artifact
  -> ExternalEvidenceAdapter
  -> content-addressed BlobStore
  -> ExternalIngestRecord
  -> SourceRegistry anchor
  -> EvidencePacket
  -> Evidence Aggregate / Learning / TCD
```

An adapter never writes `EvidencePacket`, TCD history, or learning state directly. It only produces a validated external observation artifact. The manager layer creates provenance and evidence objects.

## External Adapter Contract

```python
class ExternalEvidenceAdapter(Protocol):
    adapter_type: str

    def capabilities(self) -> ExternalAdapterCapabilities: ...
    def read(self, request: Mapping[str, object]) -> ExternalArtifact: ...
```

`ExternalArtifact` contains raw bytes, MIME type, producer reference, observation time, and metadata. It does not contain an evidence verdict.

The reference adapter is `LocalJSONExternalAdapter`, which accepts either an inline JSON object or a local JSON file path and serializes it canonically to UTF-8 JSON bytes.

## External Ingest Record

A durable ingest records:

```text
ingest_id
adapter_type
source_id
source_class
producer_ref
provenance_ref
content_sha256
content_size
content_mime_type
content_storage_uri
observed_at
ingested_at
validation_status
observation_scope
metadata_json
```

Allowed source classes are `EXTERNAL` and `REAL` only.

Allowed observation scopes:

```text
PARENT_INTERNAL
PARENT_REAL_OBSERVATION
```

Only `PARENT_REAL_OBSERVATION` may later support `EXTERNAL_REAL` sedimentation.

## Source Registry

`source_registry` remains the canonical anchor table. Phase 11 adds a small `SourceRegistry` service so external ingestion and learning share the same provenance rule.

`LearningCoordinator.register_source_anchor()` remains backward compatible and delegates to this service.

## Evidence Conversion

A verified ingest may be converted to an external `EvidencePacket` only when:

- the claim exists;
- the ingest exists and is `VERIFIED`;
- its source anchor exists and matches the ingest provenance;
- the packet uses the ingest's immutable provenance and source class.

The caller still supplies claim-relative semantics such as `SUPPORT`, `COUNTER`, `INCONCLUSIVE`, `internal_validity`, uncertainty, and transport scope. The adapter never decides scientific truth.

## Historical Sedimentation

Phase 8 previously rejected `EXTERNAL_REAL` because no adapter existed. Phase 11 permits:

```text
source_scope = EXTERNAL_REAL
```

only when an `external_ingest_id` is provided and the ingest:

- is `VERIFIED`;
- has source class `REAL` or `EXTERNAL`;
- has observation scope `PARENT_REAL_OBSERVATION`;
- has a matching registered source anchor.

No commit record is required for passive external observation. A commit remains required for WDC-initiated sandbox/real actions.

## CLI

Add:

```text
wdc external adapters
wdc external ingest --json ...
wdc external show <ingest_id>
wdc external evidence-add <ingest_id> --json ...
```

Extend:

```text
wdc tcd sediment --json '{..., "source_scope":"EXTERNAL_REAL", "external_ingest_id":"..."}'
```

All output remains machine-readable JSON.

## Error Handling

Reject:

- non-EXTERNAL/REAL source classes;
- missing local files;
- malformed JSON;
- unsupported adapter types;
- unverified/unknown ingests;
- mismatched source registry provenance;
- `EXTERNAL_REAL` sedimentation from `PARENT_INTERNAL` ingest;
- direct world-local -> external-real history laundering.

## Tests

Required tests:

1. adapter canonicalizes inline/file JSON consistently;
2. ingest stores exact hash/blob and source anchor;
3. forged EXTERNAL label without ingest/anchor cannot count as verified external ingest;
4. verified ingest converts to `EvidencePacket` with immutable provenance;
5. `EXTERNAL_REAL` sedimentation rejects unknown/internal-only ingest;
6. verified parent-real ingest can advance TCD parent time by exactly one;
7. CLI external commands preserve all gates;
8. end-to-end demo: external observation -> packet -> reality-facing learning candidate -> holdout validation -> TCD external sedimentation.

## Non-Goals / Invariants

```text
External artifact != Evidence verdict
External evidence != automatic truth
External ingest != automatic history
External adapter != authority to act
External label != registered provenance anchor
```
