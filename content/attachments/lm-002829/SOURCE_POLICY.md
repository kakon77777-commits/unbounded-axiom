# SOURCE_POLICY

`paper.md` is the canonical UTF-8 source artifact.

Rules:

1. Mathematical source uses only inline dollar delimiters and double-dollar display delimiters.
2. No Unicode-escape round trip is used.
3. LaTeX commands are preserved as source text.
4. LaTeX is not converted into Unicode mathematical glyphs and reused as source.
5. Backslashes, whitespace, and mathematical delimiters are not silently normalized after validation.
6. Validation precedes checksum generation and release packaging.
7. Rendered conversation text is not the canonical manuscript source.
8. Current OECD, EU AI Act, Council of Europe, NIST, program-synthesis, code-world-model, and AI-regulation literature was freshly re-searched before drafting.
9. Legal statements are descriptive and conditional; this package is not legal advice.
10. Functional equivalence is always domain-relative and is kept distinct from architecture identity and risk equivalence.
