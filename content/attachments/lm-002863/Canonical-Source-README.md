# 如果是一個國家・Paper 04 v0.1

本包包含「如果是一個國家」系列第四篇的 UTF-8 canonical source。

- `paper.md`：正式 Markdown 原始稿
- `SOURCES.md`：外部學術錨點與內部理論依賴
- `SERIES_STATE.md`：系列狀態與後續路線
- `validation.json`：基本來源完整性與 delimiter 驗證
- `CHECKSUMS.sha256`：SHA-256

## Canonical math rule

正式 source 的數學 delimiter 僅使用 `$...$` 與 `$$...$$`。
不執行 unicode escape round-trip。
不把 LaTeX 數學轉成 Unicode 數學字元後作為 source。
