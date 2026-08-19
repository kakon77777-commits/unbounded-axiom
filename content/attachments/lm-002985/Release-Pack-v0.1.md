# EveMissLab Ontology Core Series — Paper 04 v0.1 Release Pack

Main paper:
- `EML_ONTO_CORE_04_Typed_Information_Distortion_Restoration_v0.1_2026-08-15.md`

Companion files:
- `SYMBOL_TABLE.md`
- `claims_registry_v0.1.json`
- `information_preservation_contract_schema_v0.1.json`
- `TICDR_TOY_EXAMPLES.md`
- `dependency_manifest_v0.1.json`
- `EXTERNAL_SEARCH_NOTES.md`
- `validation.json`
- `CHECKSUMS.sha256`

Canonical core:

1. Define required information as a typed query/invariant family `J`.
2. `j` is preserved by `T` iff `j = j_hat o T`.
3. Equivalently, `j` is constant on every fiber of `T`.
4. Information completeness is task-relative.
5. Distortion is a typed spectrum, not one universal scalar.
6. Inaccessibility, decoder absence, representation irrecoverability, side-information recoverability, and physical destruction are different claims.
7. Restoration must state which information family is restored.
8. Plausible generative reconstruction is not restoration.
9. Pure post-processing cannot recreate distinctions already merged by the upstream transformation.
10. Provenance/history/boundary/causal channels are first-class when the task requires them.

Encoding:
- UTF-8, no BOM
- LF
- `$...$` and `$$...$$`
- no LaTeX-to-Unicode math round-trip
- no UI citation markers embedded
