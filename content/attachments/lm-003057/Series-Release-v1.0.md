# LSI-PSD Series v1.0 Release

本資料夾是《邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics》正式 Markdown source release。

## 內容

- `00_SERIES_OVERVIEW.md`：系列總覽與閱讀順序。
- `LSI_PSD_Complete_Series_v1.0.md`：十二篇合併版 canonical-readable source。
- `papers/`：十二篇獨立 UTF-8 Markdown。
- `case_study/NS_Proof_Space_Sampling_Observatory_v0.1.zip`：NS-203 初步觀測資料。
- `RESEARCH_LOG.md`：2026-08-17 文獻檢索與 paper-level routing。
- `SOURCE_POLICY.md`：source 與數學 delimiter 規則。
- `SERIES_MANIFEST.json`：版本、依賴、指紋與檔案 metadata。
- `PAPER_FINGERPRINTS.md`：十二篇 paper SHA-256。
- `VALIDATION.json`：canonical source validation。
- `CHECKSUMS.sha256`：release checksum。
- `tools/validate_release.py`：可重跑的 source validator。

## 研究地位

本系列不宣稱解決 Navier--Stokes、P vs NP 或其他未解問題。NS corpus 只作長程 AI proof-space dynamics 的案例資料。

## 驗證

在 release 根目錄執行：

```bash
python tools/validate_release.py
sha256sum -c CHECKSUMS.sha256
```
