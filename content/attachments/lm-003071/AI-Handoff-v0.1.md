# AI HANDOFF — TCUE-SNS Paper 08 v0.1

## Canonical artifact

`paper.md` 是唯一 canonical source。

後續修改規則：

1. 不得用渲染後公式覆蓋 source。
2. 不得做 `unicode_escape` round-trip。
3. 不得靜默改寫 `$...$` / `$$...$$`。
4. normalization 必須留下 diff。
5. 修改後先 validate，再 commit，再重算 checksum。
6. `R_{A<->B}^Theta` 是 counterfactual structural role swap，不是 token identity transfer。
7. `Sigma_A^{B|Theta} != Sigma_B` 必須保留。
8. RRUS 檢查 reason stability，不要求 preference equality。
9. 合理 role asymmetry 可保留，但必須有 `Delta_rel`。
10. `I_SNE` 必須在 admissible role permutations 中被保留。
11. 無法完整模擬第一人稱位置時必須保存 `Delta_RR` debt。
12. Paper 09 應處理規則在 role-reversal failure 後被免費重寫的 ethical immunization。
