# Ontology Genealogy & Symbol Migration Map v0.1 — Release Pack

This ZIP is a UTF-8 source package.

Contents:

- `Ontology_Genealogy_and_Symbol_Migration_Map_v0.1_2026-08-15.md`
- `symbol_registry_v0.1.json`
- `genealogy_edges_v0.1.csv`
- `SOURCE_LEDGER.md`
- `validation.json`
- `CHECKSUMS.sha256`

## Intended use

Before writing or automatically rewriting a new ontology-related paper:

1. identify source theory / file;
2. identify local symbol definition;
3. resolve namespace and version;
4. consult `symbol_registry_v0.1.json`;
5. map to canonical concept;
6. preserve historical symbol in provenance;
7. do not rewrite the historical source in place;
8. if ambiguous, emit an ambiguity instead of guessing.

## Encoding rules

- UTF-8, no BOM
- LF newlines
- Markdown math uses `$...$` and `$$...$$`
- no LaTeX-to-Unicode math round-trip
- UI-only citation markers are not embedded
