# TCUE-SNS Paper 05 v0.1

正式標題：**認知僭越論：從可知、可推論到可控制的權力跨越**

本封包是「三域耦合普世倫理與主體不可替代論系列」Paper 05 的 UTF-8 canonical-source release。

## Canonical source

- `paper.md`：唯一正式論文 source。
- 數學 delimiter 僅使用 `$...$` 與 `$$...$$`。
- 不使用 `unicode_escape` round-trip。
- 不將 LaTeX 數學轉成 Unicode 數學字元後再當 source。
- 不對反斜線、delimiter 或公式內容做未揭露 normalization。

## 核心理論增量

Paper 05 在 Paper 01–04 上引入：

1. Cognitive Capability Graph `G_C`；
2. Permission Graph `G_R`；
3. `Capability != Permission`；
4. inferential privacy 與 inferential closure；
5. delayed inferential sensitivity；
6. prediction / intervention / control 分離；
7. choice-space compression `kappa`；
8. 九類 Cognitive Usurpation；
9. minimum necessary cognitive resolution；
10. contestability / reversibility / traceability / exit protocol；
11. UBE / DEST / GCORF 的能力—許可治理接口；
12. 與 Paper 06「主體不可歸零公理」的銜接。

## 驗證

- `validation.json`：canonical-source 驗證結果。
- `tools/verify_package.py`：可重跑 source/package verifier。
- `CHECKSUMS.sha256`：封包檔案 SHA-256（不包含 checksum 檔本身）。
- `provenance/source_manifest.json`：理論依賴與外部研究接口摘要。
- `provenance/normalization.diff`：v0.1 直接撰寫 canonical source，沒有 renderer/export normalization。

## 狀態

v0.1 / formal-framework proposal。未宣稱所有推論皆不正當，未宣稱所有個人化皆構成操控，未宣稱公眾人物失去隱私，未宣稱任何現有 AI 已完成全域人物逆向或取得主體治理資格。
