# RH-W-13 工程包 v0.1

本包完成跨正則性延拓、$\alpha$ 規範參數辨識、相對平移 $\sigma$、廣義譜一致量化審計、jump-resolved 阿基米德尾界，以及十維近零正譜帶的 exact 夾證書。

## 主要結論

$$
10^{-8}<\lambda_{\min}(M,G)<5\times10^{-8}
$$

只對固定十維 mixed B-spline 子空間成立，不推出 RH。

## 主要檔案

- `01_RH-W-13_跨正則性延拓與規範參數_v0.1.md`
- `02_RH-W-13_一致量化反例與紅色警報審計_v0.1.md`
- `03_RH-W-13_JumpResolved尾界與近零證書_v0.1.md`
- `mixed_10x10_nearzero_interval.json`
- `build_cross_regularity_certificate.py`
- `verify_cross_regularity.py`
- `mixed_order_jump_tail.py`
- `crosscheck_w13_mpmath.py`
- `adaptive_mixed_continuation.py`
- `continuation_search.csv`
- `quantization_mismatch_audit.json`
- `RH-W-13_subgaps_v0.1.csv`

## 重建

```bash
python build_cross_regularity_certificate.py
python verify_cross_regularity.py
python crosscheck_w13_mpmath.py
```

## 嚴格性

`verify_cross_regularity.py` 使用純有理 $LDL^T$ 驗證下界與整數 Rayleigh witness 驗證上界。`crosscheck_w13_mpmath.py` 僅為獨立高精度浮點檢查。

## 聲明邊界

- 未證明 RH。
- 未反證 RH。
- 未找到真實負 Weil witness。
- 有限維近零值不能外推至完整測試函數空間。
