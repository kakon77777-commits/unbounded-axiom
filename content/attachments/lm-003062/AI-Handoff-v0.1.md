# AI HANDOFF — TCUE-SNS Paper 02 v0.1

## Canonical-source rules

1. `paper.md` 是唯一 canonical paper source。
2. 數學只允許 `$...$` 與 `$$...$$`。
3. 不可把 LaTeX 公式轉成 Unicode 數學字元後覆寫 source。
4. 不可進行 `unicode_escape` 類 round-trip。
5. 不可靜默修改反斜線、空白、delimiter、公式換行或符號命名。
6. 若需要 renderer-specific normalization，必須保留原 source、產生 diff、在 provenance 明示並重新驗證。
7. 後續版本修改應新增版本，不應無痕覆寫 v0.1。

## Theory constraints to preserve

- 主體不可替代 `!=` 主體不可表示。
- 第一人稱權威 `!=` 第一人稱永遠正確。
- `representation / function / prediction / proxy / token identity / authority` 六層必須保持 typed separation。
- `proxy authorization` 不得被升格成 `token identity`。
- `predictive superiority` 不得被升格成 `choice ownership`。
- 若 replica 形成新主體，允許 `R != S AND R in CandidateSubject`。
- branching / fission 必須保存 distinct instance histories。
- live subject update 對 current-state judgment 優先於 stale historical model，但保留緊急代理與能力不足的制度例外。
- 高 fidelity 可能增加 impersonation / steering risk，不假定 fidelity 與 authority 單調正相關。
- UBE / meta-rule rewrite 必須遵守 anti-immunization，不可藉重定義免費抹除 non-substitution invariant。

## Next paper

Paper 03：**選擇底空間與選擇算子族：從人格描述到動態主體建模**。
