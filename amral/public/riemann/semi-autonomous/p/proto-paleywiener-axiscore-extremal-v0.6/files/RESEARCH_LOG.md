# Research Log

## 2026-07-25：連續問題定義

- 採 real-even clamped $H_0^2(-R,R)$。
- 將 tail quadratic form 內積化，使 continuous tail operator 為 identity。
- 將 multi-test Gram 提升成 positive trace-class operator。
- 導出軸帶 probability measures 與 core probability measure 的 weak dual。

## 2026-07-25：rank-two closed form

- 將 complex core evaluation 分解為 real／imaginary representers。
- 識別
  $C_z=2(u_z\otimes u_z-v_z\otimes v_z)$。
- 用 generalized eigenvalue 與 Sherman–Morrison 導出一軸點、一核心點閉式值。
- direct scan 顯示每個單帶 lower bound 都小於 $1$；full obstruction 必須是
  multi-band。

## 2026-07-25：Galerkin family

- 建立 clamped-even Chebyshev family。
- 完成 10 個 nested dimensions。
- joint alpha 由 $7.7882$ 單調降至 $1.132475$。
- high-dimensional plateau 出現在約 $1.1324$。

## 2026-07-25：獨立 Green solver

- 導出 clamped bi-Laplacian Green kernel。
- 以 cumulative moments 直接解 representer ODE。
- simplified point extremal 與 raw-dimension-192 Galerkin 對到約 $10^{-9}$。
- 將 58+2 atomic measures 直接放入 Green RKHS，得到
  $1.1324412$ floating threshold。

## 2026-07-25：Schur reduction

- 將 58 axis positive directions 與 2 core-real positive directions吸收到
  $B_\alpha$。
- 剩餘 negative rank 只有 2。
- continuous PSD 等價於 $2\times2$ Schur matrix PSD。
- v0.6 safe alpha 的 Schur margin 約 $0.05609$。

## 2026-07-25：rational handoff

- weights rationalized to denominator $10^{12}$。
- supports 轉為 exact decimal rationals。
- target alpha 固定為 $21/20$。
- rationalized floating Schur margin 約 $0.0698852$。
- 停止 dictionary/Galerkin expansion，轉向 interval certification。
