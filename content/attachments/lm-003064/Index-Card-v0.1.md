# TCUE-SNS Paper 04 v0.1

正式標題：**元認知非免疫原則：反思、包裝與遞迴自我模型**

本封包是「三域耦合普世倫理與主體不可替代論系列」Paper 04 的 UTF-8 canonical-source release。

## Canonical source

- `paper.md`：唯一正式論文 source。
- 數學 delimiter 僅使用 `$...$` 與 `$$...$$`。
- 不使用 `unicode_escape` round-trip。
- 不將 LaTeX 數學轉成 Unicode 數學字元後再當 source。
- 不對反斜線、delimiter 或公式內容做未揭露 normalization。

## 核心理論增量

Paper 04 在 Paper 03 的 Choice Bottom-Space / Choice-Operator Family 上引入：

1. Recursive Self-Model Hierarchy `M_S^[n]`；
2. Presentation Recursion `P_S^[n]`；
3. deliberate naturalness / 包裝後的非包裝；
4. `Detect != Interpret != Evaluate != Control != Rewrite`；
5. Metacognitive Non-Immunity Principle (MNIP)；
6. Reflexive Capture：元認知算子可被既有目標／算子重新利用；
7. `Self-Certification != Safety Certification`；
8. External Corrigibility 作為獨立安全維度；
9. Self-Model 作為下一輪 Choice Bottom-Space 的因果輸入；
10. 元認知模型的隱私、最小必要解析度與 choice-space steering 風險。

## 驗證

- `validation.json`：本次 canonical-source 驗證結果。
- `tools/verify_package.py`：可重跑 source/package verifier。
- `CHECKSUMS.sha256`：封包檔案 SHA-256（不包含 checksum 檔本身）。
- `provenance/source_manifest.json`：理論依賴與外部研究接口摘要。
- `provenance/normalization.diff`：v0.1 直接撰寫 canonical source，沒有 renderer/export normalization。

## 狀態

v0.1 / formal-framework proposal。未宣稱高元認知等同心理健康，未宣稱低元認知等同病理，未宣稱角色扮演等同欺騙，未宣稱任何現有 AI 的 metacognitive behavior 已證明第一人稱主體性。
