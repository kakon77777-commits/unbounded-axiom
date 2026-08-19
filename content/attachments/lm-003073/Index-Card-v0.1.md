# TCUE-SNS Paper 03 v0.1

正式標題：**選擇底空間與選擇算子族：從人格描述到動態主體建模**

本封包是「三域耦合普世倫理與主體不可替代論系列」Paper 03 的 UTF-8 canonical-source release。

## Canonical source

- `paper.md`：唯一正式論文 source。
- 數學 delimiter 僅使用 `$...$` 與 `$$...$$`。
- 不使用 `unicode_escape` round-trip。
- 不將 LaTeX 數學轉成 Unicode 數學字元後再當 source。
- 不對反斜線、delimiter 或公式內容做未揭露 normalization。

## 核心理論增量

Paper 03 在 Paper 01 三域判定與 Paper 02 主體不可替代地基上，引入：

1. Choice Bottom-Space：條件化的選擇底空間；
2. Choice-Operator Family：非單一固定人格／政策的選擇算子族；
3. Choice Bundle：選擇、理由、後果反應、外部回饋與自我模型更新的選擇束；
4. `BottomSpaceUpdate != OperatorUpdate`；
5. 選擇束改寫下一個底空間；
6. 條件化逆向與多模型保留；
7. 預測非命定、預測非所有權、可推論非許可；
8. UBE / DEST / GCORF / RMRM 的統一接口。

## 驗證

- `validation.json`：本次驗證結果。
- `tools/verify_package.py`：可重跑的 source/package verifier。
- `CHECKSUMS.sha256`：封包檔案 SHA-256（不包含 checksum 檔本身）。
- `provenance/source_manifest.json`：來源與理論接口摘要。
- `provenance/normalization.diff`：v0.1 直接撰寫 canonical source，沒有 renderer/export normalization。

## 狀態

v0.1 / formal-framework proposal。未宣稱人格可被完整還原、未宣稱有限歷史唯一決定未來、未宣稱選擇算子等於主體、未宣稱任何現有 AI 具有第一人稱主體域。
