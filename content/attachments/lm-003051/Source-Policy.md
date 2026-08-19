# SOURCE_POLICY

This release treats `paper.md` as the canonical UTF-8 source artifact.

Rules:

1. Mathematical source uses only inline dollar delimiters and double-dollar display delimiters.
2. No Unicode-escape round trip is used.
3. LaTeX commands are preserved as source text and are not replaced by Unicode mathematical glyphs.
4. No silent normalization of backslashes, spacing, or delimiters is performed after validation.
5. Validation runs before checksums and release packaging.
6. Rendered chat text is not the canonical source.
