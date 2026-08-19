# AI HANDOFF — TCUE-SNS Paper 07 v0.1

## Canonical artifact

`paper.md` 是唯一 canonical source。

後續 AI／人類修改時：

1. 不得把渲染後公式字形反寫成 source。
2. 不得做 `unicode_escape` round-trip。
3. 不得靜默改寫 `$...$` / `$$...$$`。
4. normalization 必須產生 diff。
5. 修改後先 validate，再 commit，再重算 checksum。
6. `bowtie` 不得被簡化成加權平均，除非新增明示的特殊情況定理。
7. `Glue` 不等於 mean / majority vote。
8. `BranchGlobal = Pass` 不等於所有分支都同樣正確；它表示不可無損合併時保留分支是合法全域表示。
9. `I_SNE` 不得被 compression 靜默刪除。
10. `Delta_open` 不得因「為了收斂」被刪除或改名成已解決。
11. `Stop != Terminal`、`LocalComplete != GlobalTerminal` 必須保留。
12. Paper 08 角色互換應作用於三域、能力、脆弱性、資訊與第一人稱位置，不得只交換名字。
13. 外部 pluralistic alignment 文獻只作壓力測試，不得宣稱已證明 TCUE-SNS。
