# SOURCE_POLICY

`paper.md` is the canonical UTF-8 source artifact.

Rules:

1. Mathematical source uses only inline dollar delimiters and double-dollar display delimiters.
2. No Unicode-escape round trip is used.
3. LaTeX commands are preserved as source text.
4. LaTeX is not converted into Unicode mathematical glyphs and then reused as source.
5. Backslashes, whitespace, and math delimiters are not silently normalized after validation.
6. Validation precedes checksum generation and release packaging.
7. Rendered chat content is not the canonical manuscript source.
