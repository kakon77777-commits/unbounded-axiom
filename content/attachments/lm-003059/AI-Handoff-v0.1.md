# AI HANDOFF — TCUE-SNS Paper 01 v0.1

## Canonical-source rules

1. `paper.md` 是唯一 canonical paper source。
2. 數學只允許 `$...$` 與 `$$...$$`。
3. 不可把 LaTeX 公式轉成 Unicode 數學字元後覆寫 source。
4. 不可進行 `unicode_escape` 類 round-trip。
5. 不可靜默修改反斜線、空白、delimiter、公式換行或符號命名。
6. 若需要 renderer-specific normalization，必須：
   - 保留原 source；
   - 產生 machine-readable diff；
   - 在 provenance 明示；
   - 重新驗證後才可 commit。
7. 後續版本修改應優先新增版本檔，不應無痕覆寫 v0.1。

## Theory constraints to preserve

- 三域不是三個可直接平均的 scalar scores。
- `L`, `A`, `S^{1p}` 必須保持 non-collapse。
- 第一人稱 report 與外部 proxy model 必須分離。
- `Judgment` 與 `ActionPolicy / Authority` 必須分離。
- UBE expansion 不可被濫用成永不決策；需保留 bounded-action interface。
- 跨域反免疫化：不得靠重定義一域免費抹除另一域的 residual。

## Next paper

Paper 02：**主體不可替代論：表示、理解與第一人稱位置的本體差**。
