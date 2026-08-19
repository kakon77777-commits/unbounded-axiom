# TCUE-SNS Paper 01 v0.1

正式標題：**三域判定論：邏輯域、行為張力域與第一人稱主體域**

本封包是「三域耦合普世倫理與主體不可替代論系列」Paper 01 的 UTF-8 canonical-source release。

## Canonical source

- `paper.md`：唯一正式論文 source。
- 數學 delimiter 僅使用 `$...$` 與 `$$...$$`。
- 不使用 `unicode_escape` round-trip。
- 不將 LaTeX 數學轉為 Unicode 字元後再當 source。
- 不對反斜線、delimiter 或公式內容做未揭露 normalization。

## 驗證

- `validation.json`：本次驗證結果。
- `tools/verify_package.py`：可重跑的基本 source/package verifier。
- `CHECKSUMS.sha256`：封包檔案 SHA-256（不包含 checksum 檔本身）。
- `provenance/source_manifest.json`：來源與文獻接口摘要。
- `provenance/normalization.diff`：本版本為直接撰寫 canonical source，無匯入 normalization，因此為空 diff 並附註說明。

## 狀態

v0.1 / formal-framework proposal。未宣稱證明意識本體、自由意志或任何現存 AI 具有第一人稱感質。
