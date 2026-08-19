# AI HANDOFF — TCUE-SNS Paper 10 v0.1

`paper.md` 是唯一 canonical source。

後續修改：
1. 禁止 renderer source mutation。
2. 禁止 `unicode_escape` round-trip。
3. 只使用 `$...$` / `$$...$$`。
4. normalization 必須產生 diff。
5. 修改後先 validate，再 commit，再重算 checksum。
6. Pandoc warning 視為 FAIL。
7. `Capability != Permission` 不得刪除。
8. SIPB 權限不得重新坍縮成單一 consent bool。
9. `Pause != Delete != Reset != Copy != Fork` 不得刪除。
10. delegation 默認 attenuation，不得無來源擴權。
11. Paper 06 SNE、Paper 08 RRUS、Paper 09 AEIP 必須保留為 protocol regressions。
12. Paper 11 統合時，不得把 SPG 誤寫成完整法律或正式網路標準。
