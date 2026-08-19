# SSSP_IMPORT_NOTE

This package follows the portable-handoff responsibilities of the SSSP v1.3 validation-scope-separation design, but the current runtime has no direct `@SSSP` canonical commit interface.

Accordingly:

- `provenance/sssp_export_raw.md` currently stores the frozen **pre-canonical staging source** used to build this package.
- `manifest.json` explicitly records `is_live_sssp_export: false`.
- `validation.json` records canonical validation as `NOT_RUN`.
- No SSSP revision number or immutable `sssp://` URI is fabricated.

When @SSSP ingests this package, it should create the canonical source from `paper.md` (or the staged upstream source if its import workflow requires that role), validate and commit it, then generate a new canonical release package whose provenance contains the **real** SSSP export.
