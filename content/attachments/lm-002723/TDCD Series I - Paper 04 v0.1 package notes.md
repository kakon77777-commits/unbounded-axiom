# TDCD Series I / Paper 04 v0.1

Canonical source: `paper.md`

This package contains:
- `paper.md` — canonical UTF-8/LF source
- `references.bib` — bibliography source
- `validation.json` — source validation report
- `CHECKSUMS.sha256` — SHA-256 checksums

Validation policy:
- UTF-8
- LF line endings
- canonical math delimiters only: `$...$` and `$$...$$`
- no `unicode_escape` round-trip
- no conversion of LaTeX source into Unicode math glyphs
- checksums generated after validation
