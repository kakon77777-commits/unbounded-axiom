# AI HANDOFF — TCUE-SNS Paper 03 v0.1

## Canonical-source rules

1. `paper.md` 是唯一 canonical paper source。
2. 數學只允許 `$...$` 與 `$$...$$`。
3. 不可把 LaTeX 公式轉成 Unicode 數學字元後覆寫 source。
4. 不可進行 `unicode_escape` 類 round-trip。
5. 不可靜默修改反斜線、空白、delimiter、公式換行或符號命名。
6. 若需要 renderer-specific normalization，必須保留原 source、產生 diff、在 provenance 明示並重新驗證。
7. 後續版本修改應新增版本，不應無痕覆寫 v0.1。

## Theory constraints to preserve

- `Subject != Choice Trace != Choice Operator != Choice Model`。
- `Choice Bottom-Space != Choice Set`。
- `BottomSpaceUpdate != OperatorUpdate`。
- `Observed Bottom-Space != True Bottom-Space`。
- 選擇束必須保留 action / rationale / response / external feedback / self-model update 的 typed separation。
- 由痕跡逆向得到的是候選算子族，不是 timeless essence。
- 高預測率不得升格為 predestination、choice ownership 或 normative authority。
- 多個可識別模型應允許保留，不可強迫收斂成唯一人格真相。
- 主體看到自己的模型後，模型可成為新的底空間輸入；需保存 subject-indexed anti-fixed-point interface。
- UBE reopening / meta expansion 必須保存 provenance、versioning 與 anti-immunization。
- 高解析個體模型需遵守 minimal necessary resolution 與 inferability / permission separation。

## Next paper

Paper 04：**元認知非免疫原則：反思、包裝與遞迴自我模型**。
