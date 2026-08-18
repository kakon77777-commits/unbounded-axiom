# 如果是一個國家・Paper 07 / Series Final

本包包含「如果是一個國家」系列第七篇的 UTF-8 canonical source。

- `paper.md`：正式 Markdown 原始稿
- `SOURCES.md`：外部學術錨點與內部理論依賴
- `SERIES_STATE.md`：系列完成狀態
- `validation.json`：來源完整性與 canonical delimiter 驗證
- `CHECKSUMS.sha256`：SHA-256

完整系列包另含：
- Paper 01–07
- `SERIES_INDEX.md`
- `SERIES_SYNTHESIS.md`
- `SERIES_VALIDATION.json`
- 全系列 checksum

## Canonical math rule

正式 source 的數學 delimiter 僅使用 `$...$` 與 `$$...$$`。
不執行 unicode escape round-trip。
不把 LaTeX 數學轉成 Unicode 數學字元後作為 source。
