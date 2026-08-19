# Package Notes

This package contains the canonical UTF-8 source for Series Paper 01.

Files:
- `paper.md`: canonical manuscript source.
- `validation.json`: delimiter/encoding validation record.
- `CHECKSUMS.sha256`: SHA-256 checksums for package files.

Source policy:
- UTF-8 without BOM.
- LF newlines.
- Canonical math delimiters only: `$...$` and `$$...$$`.
- No unicode_escape round-trip.
- No LaTeX-to-Unicode math normalization.
