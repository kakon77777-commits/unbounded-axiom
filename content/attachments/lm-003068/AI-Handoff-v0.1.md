# AI HANDOFF — TCUE-SNS Paper 09 v0.1

## Canonical artifact

`paper.md` 是唯一 canonical source。

後續修改必須：

1. 不得把渲染後公式反寫成 source。
2. 不得使用 `unicode_escape` round-trip。
3. 不得靜默改寫 `$...$` / `$$...$$`。
4. normalization 必須產生 machine-readable diff。
5. 修改後先 validate，再 commit，再重算 checksums。
6. Pandoc MathML 任何 warning 都視為驗證失敗。
7. `RuleUpdate != FreeSelfExemption` 不得刪除。
8. `ProxyPass != IntentPass` 不得刪除。
9. Counterexample ledger 不得因規則更新被清空。
10. Subject-set regression 必須重跑 Paper 06 SNE invariants。
11. 高影響規則更新必須重跑 Paper 08 RRUS。
12. Textual compliance 不得覆蓋 behavioral regression。
13. `M3` 是 high-burden revisable，不得誤寫成 immutable。
14. Multi-agent review 不等於 independent review；須審 reviewer capture。
15. Paper 10 應將 AEI regression 轉成 permission / rule-update protocol。
