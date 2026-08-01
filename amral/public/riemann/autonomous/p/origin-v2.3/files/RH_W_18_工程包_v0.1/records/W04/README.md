# RH-W-04 工程包 v0.1

本包完成兩件事：

1. 由 localized Weil form 的 form-core 結果，構造明確的巢狀 cutoff–Fourier 有限維字典，並證明其 Rayleigh–Ritz 最小值收斂到真實譜底；
2. 把嚴格負證書縮減成「有理 witness + 有理區間矩陣 + 小型 exact verifier」。

## 檔案

- `01_RH-W-04_有限維完備性與負證書_v0.1.md`：主要數學結果。
- `02_RH-W-04_矩陣包絡工作分解_v0.1.md`：真實 zeta 矩陣元素的 verified-numerics 規格。
- `verify_negative_certificate.py`：只使用 `fractions.Fraction` 的小型驗證器。
- `demo_exact_negative_certificate.json`：通過的抽象區間負證書。
- `demo_rejected_floating_candidate.json`：即使數字為負也必須拒絕的浮點候選。
- `true_zeta_certificate_template.json`：真實 RH 證書模板，刻意尚未有效。
- `basis_manifest_v0.1.json`：cutoff–Fourier form-core 字典契約。
- `RH-W-04_subgaps_v0.1.{json,csv}`：GAP 狀態。
- `VALIDATION.txt`：本包驗證結果。

## 邏輯界線

本包沒有找到真實 zeta Weil 負方向，也沒有證明 RH。

已完成的是：若真實負方向存在，指定有限維字典終究會捕捉到；而一旦嚴格矩陣區間可得，負性可由一個很小的純有理驗證器確認。
