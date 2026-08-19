# SOURCE_POLICY

`paper.md` is the canonical UTF-8 source artifact.

Rules:

1. Mathematical source uses only inline dollar delimiters and double-dollar display delimiters.
2. No Unicode-escape round trip is used.
3. LaTeX commands are preserved exactly as source text.
4. LaTeX is not converted into Unicode mathematical glyphs and reused as source.
5. Backslashes, whitespace, and delimiters are not silently normalized after validation.
6. Validation precedes checksum generation and packaging.
7. Rendered conversation text is not the canonical manuscript source.
