# GCORF-02 v0.1 Portable Handoff

本包為 **GCORF Canonical Core Paper 02** 的 portable handoff。

主要正文：`paper.md`

主題：
- Atomic Operator / Operator Cluster / Implementation Mode
- Partial Composition Algebra
- Serial / Parallel / Recursive / Alternating / Coupled Composition
- Self-Rewriting Coupling
- Composition guards, closure, spectra, cost and failure propagation

## SSSP MCP 狀態

此包 **未聲稱已建立 SSSP canonical revision**。

`validation.json` 中 canonical scope 應保持 `NOT_RUN`，直到真正由 SSSP MCP 完成 import / validate / commit。

## Package verification

```bash
python tools/verify_package.py
```

驗證包含：
- UTF-8；
- SHA-256 coverage；
- LaTeX delimiter balance；
- mechanically reproducible normalization diff；
- math inventory；
- schema presence；
- canonical-state non-fabrication。
