# AI HANDOFF — TCUE-SNS Paper 05 v0.1

## Canonical artifact

`paper.md` 是唯一 canonical source。

任何 AI／人類後續處理時：

1. 不得把渲染後公式字形反寫成 source。
2. 不得做 `unicode_escape` round-trip。
3. 不得把 LaTeX command 靜默替換成 Unicode 數學符號。
4. 不得靜默修改 `$...$` / `$$...$$` delimiter。
5. 任何 normalization 必須產生 machine-readable diff。
6. 修改後先 validate，再 commit，再重算 checksums。
7. Paper 05 的核心 non-identity 不得在摘要時被抹平：
   - `Capability != Permission`
   - `Inference != Ownership`
   - `Prediction != Predestination`
   - `Prediction != Control Right`
   - `Public Trace != Unrestricted Inferential Use`
   - `Local Data Legality != Global Profile Legality`
8. 認知僭越不是「推論本身有罪」；必須保留 purpose / authority / effect / tension 判定。
9. 第一人稱報告不是絕對真理，但不得被外部模型免費歸零。
10. 與 Paper 06 銜接時，不得把「主體不可歸零」誤寫成「主體永遠擁有絕對否決權」。

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

Paper 05 使用下列外部工作作壓力測試，不把任何一篇外部論文等同本文總理論：

- ACL 2026 AutoProfiler / automated profile inference
- ACL 2026 intermediate-representation attribute inference
- CHI 2026 / arXiv implicit LLM inference user study
- 2025 AI-driven manipulation randomized controlled study
- EU AI Act Article 5
- UNESCO 2025 Recommendation on the Ethics of Neurotechnology
