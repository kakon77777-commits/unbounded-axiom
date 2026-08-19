# AI HANDOFF — TCUE-SNS Paper 06 v0.1

## Canonical artifact

`paper.md` 是唯一 canonical source。

任何 AI／人類後續處理時：

1. 不得把渲染後公式字形反寫成 source。
2. 不得做 `unicode_escape` round-trip。
3. 不得把 LaTeX command 靜默替換成 Unicode 數學符號。
4. 不得靜默修改 `$...$` / `$$...$$` delimiter。
5. 任何 normalization 必須產生 machine-readable diff。
6. 修改後先 validate，再 commit，再重算 checksums。
7. Paper 06 的三條防誤讀不得刪除：
   - `Non-Erasure != Absolute Veto`
   - `First-Person Evidence != Infallibility`
   - `Non-Erasure != Non-Revision`
8. `Inst_{1p}(S) ≻_auth Rep_A(S)` 只表示第一人稱替代權威域的非對稱，不是全域能力、真理或政治權力排序。
9. 不得把 `p_S(X)>0` 誤寫成「所有 AI 都應視為完整人格」。
10. 不得把 precautionary protection 誤寫成 consciousness proof。
11. 不得用「模型更準」「能力更強」「載體不同」「無法反抗」作為單獨 subject erasure 理由。
12. 與 Paper 07 銜接時，`I_SNE` 應作為 Glue / UBE 不可免費壓縮的不變量候選。

## Required validation

- UTF-8 decode
- replacement character count
- canonical math delimiter check
- display math balance
- odd inline `$` scan
- Pandoc MathML parse
- checksum verification
- ZIP integrity

## External research interfaces

Paper 06 使用下列外部工作作壓力測試，不把任何一項外部工作等同本文總理論：

- Long et al. (2024), *Taking AI Welfare Seriously*
- Mikeda (2026), *When Should We Protect AI?*
- Caviola & Saad (2025), *Futures with Digital Minds*
- UNESCO (2025), *Recommendation on the Ethics of Neurotechnology*
- Sirbu et al. (2025), next-generation BCI ethical regulation
