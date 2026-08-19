# EveMissLab Ontology Core Series — Paper 03 v0.1 Release Pack

Main artifact:
- `EML_ONTO_CORE_03_Shared_State_Domain_Coupling_v0.1_2026-08-15.md`

Companion artifacts:
- `SYMBOL_TABLE.md`
- `claims_registry_v0.1.json`
- `ssdc_profile_schema_v0.1.json`
- `SSDC_TOY_EXAMPLES.md`
- `dependency_manifest_v0.1.json`
- `EXTERNAL_SEARCH_NOTES.md`
- `validation.json`
- `CHECKSUMS.sha256`

## Canonical statement

`SSDC = Shared-State Domain Coupling`.

The canonical object is a directional structured profile, not a single scalar.

Core decomposition:

`Share -> Transport -> Couple -> Measure`

with explicit no-go boundaries:

- Share != Transport
- Transport != Active Coupling
- Coupling != Synchronization
- Synchronization != Identity
- Pairwise SSDC != Global Shared State

Legacy `Co` migrates to an SSDC snapshot/version-synchronization subtype.

## Encoding

- UTF-8, no BOM
- LF
- `$...$` and `$$...$$` only
- no LaTeX-to-Unicode math round-trip
- no UI-only citation tokens embedded
