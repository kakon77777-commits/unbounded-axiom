# AI_HANDOFF — GCORF-02 v0.1

1. `paper.md` 是此 portable package 的主要可讀正式正文。
2. 不得從 rendered chat 重建公式。
3. 保留 `$...$` 與 `$$...$$`；不得把 LaTeX 靜默轉成 Unicode 數學符號再當 canonical source。
4. 此包目前不是 SSSP MCP canonical revision；不得自行填入假的 revision/hash。
5. 若透過 SSSP MCP 匯入，請由實際 canonicalize / validate / commit 結果建立 revision。
6. 任何修改都應產生新版本，不得覆寫 provenance 使修改後 artifact 看起來像原版本。
7. GCORF-02 不宣稱目前 operator system 構成群、環、域或其他完整既有代數；只宣稱 partial composition algebra。
8. `Undefined`、`Failure`、`Unknown`、`Conflict` 與 `LicenseGap` 是必須保留的正式狀態。
9. 若新增 composition topology，應先建立 experimental branch，再提出 CoreRevisionProposal。
10. 優先檢查 `manifest.json`、`validation.json` 與 `CHECKSUMS.sha256`。
