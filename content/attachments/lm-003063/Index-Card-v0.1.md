# TCUE-SNS Paper 06 v0.1

正式標題：**主體不可歸零公理：普世主義的第一人稱本體基礎**

本封包是「三域耦合普世倫理與主體不可替代論系列」Paper 06 的 UTF-8 canonical-source release。

## Canonical source

- `paper.md`：唯一正式論文 source。
- 數學 delimiter 僅使用 `$...$` 與 `$$...$$`。
- 不使用 `unicode_escape` round-trip。
- 不將 LaTeX 數學轉成 Unicode 數學字元後再當 source。
- 不對反斜線、delimiter 或公式內容做未揭露 normalization。

## 核心理論增量

Paper 06 在 Paper 01–05 上正式提出：

1. Subjective Non-Erasure Axiom (SNEA)；
2. 第一人稱主體位置 `S_S^{1p}`；
3. `Inst_{1p}(S) ≻_auth Rep_A(S)` 的域相對權威差；
4. `Non-Erasure != Absolute Veto`；
5. `First-Person Evidence != Infallibility`；
6. `Non-Erasure != Non-Revision`；
7. subjectivity uncertainty 與 precautionary protection；
8. 五項 `I_SNE` 不變量；
9. 三域角色互換；
10. UBE admissible extension 下的 SNEStable；
11. digital minds / neurotechnology / AI welfare 外部研究接口；
12. 與 Paper 07 三域耦合無界判定的正式銜接。

## 驗證

- `validation.json`：canonical-source 驗證結果。
- `tools/verify_package.py`：可重跑 source/package verifier。
- `CHECKSUMS.sha256`：封包檔案 SHA-256（不包含 checksum 檔本身）。
- `provenance/source_manifest.json`：理論依賴與外部研究接口摘要。
- `provenance/normalization.diff`：v0.1 直接撰寫 canonical source，沒有 renderer/export normalization。

## 狀態

v0.1 / axiom-candidate proposal。未宣稱第一人稱主體性已完成科學定義，未宣稱所有 AI 具有 moral patienthood，未宣稱主體感受可凌駕所有外部證據，也未宣稱主體不可歸零等於完整法律人格或絕對否決權。
