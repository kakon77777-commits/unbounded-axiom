# SSSP MCP Import Order

Recommended order:

GCORF-00
→ GCORF-01
→ GCORF-02
→ GCORF-03
→ GCORF-04
→ GCORF-05
→ GCORF-06
→ GCORF-07
→ GCORF-08
→ GCORF-09
→ GCORF-U

For each package:

1. Verify its `CHECKSUMS.sha256`.
2. Read `AI_HANDOFF.md`.
3. Treat `paper.md` as the portable formal source.
4. Import/canonicalize through SSSP MCP.
5. Run SSSP canonical validation.
6. Commit only after validation passes.
7. Record the actual revision/hash returned by SSSP.
8. Do not reuse `NOT_RUN` portable validation as canonical validation.
9. If SSSP normalization changes the source, mechanically preserve/export the diff.
10. Import GCORF-U only after the 00–09 references are resolvable if cross-document linking is desired.
