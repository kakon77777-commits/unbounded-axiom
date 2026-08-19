# EveMissLab Ontology Core Series — Paper 05 v0.1 Release Pack

Main paper:
- `EML_ONTO_CORE_05_Identity_Boundary_Subject_Object_Edges_v0.1_2026-08-15.md`

Companion files:
- `SYMBOL_TABLE.md`
- `claims_registry_v0.1.json`
- `typed_identity_certificate_schema_v0.1.json`
- `typed_boundary_certificate_schema_v0.1.json`
- `subject_object_edge_schema_v0.1.json`
- `TIBRF_TOY_EXAMPLES.md`
- `dependency_manifest_v0.1.json`
- `EXTERNAL_SEARCH_NOTES.md`
- `validation.json`
- `CHECKSUMS.sha256`

Canonical corrections:

1. Exact typed identity:
   `x ≡_{q,J} y`.
2. Approximate tolerance:
   `x ≈_{q,J,epsilon} y`.
   Do not assume transitivity.
3. Generic typed boundary:
   `B_q^xi(X)`.
   Use topological `partial` notation only when topology/neighborhood structure justifies it.
4. Subject/object are relation-relative roles by default.
5. SSDC, synchronization and relational self-inclusion do not imply strict identity.

Encoding:
- UTF-8, no BOM
- LF
- math: `$...$` and `$$...$$`
- no UI citation tokens embedded
