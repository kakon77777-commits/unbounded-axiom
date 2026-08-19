# TCUE-SNS Paper 02 v0.1

正式標題：**主體不可替代論：表示、理解與第一人稱位置的本體差**

本封包是「三域耦合普世倫理與主體不可替代論系列」Paper 02 的 UTF-8 canonical-source release。

## Canonical source

- `paper.md`：唯一正式論文 source。
- 數學 delimiter 僅使用 `$...$` 與 `$$...$$`。
- 不使用 `unicode_escape` round-trip。
- 不將 LaTeX 數學轉為 Unicode 數學字元後再當 source。
- 不對反斜線、delimiter 或公式內容做未揭露 normalization。

## 核心理論增量

Paper 02 在 Paper 01 三域判定地基上，將「替代」拆成六個不同關係：

1. representation fidelity；
2. functional equivalence；
3. predictive equivalence；
4. proxy authorization；
5. first-person/token identity；
6. normative authority。

本篇核心不是證明主體永遠不可被完整表示，而是禁止從表示／預測／功能成功無條件跳到身份同一與第一人稱權威移轉。

## 驗證

- `validation.json`：本次驗證結果。
- `tools/verify_package.py`：可重跑的 source/package verifier。
- `CHECKSUMS.sha256`：封包檔案 SHA-256（不包含 checksum 檔本身）。
- `provenance/source_manifest.json`：來源與理論接口摘要。
- `provenance/normalization.diff`：v0.1 直接撰寫 canonical source，沒有 renderer/export normalization。

## 狀態

v0.1 / formal-framework proposal。未宣稱證明靈魂、意識本體、mind uploading 必然成功或失敗、任何現有 AI 具有感質，或第一人稱報告永遠正確。
