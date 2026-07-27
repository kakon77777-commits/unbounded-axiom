# RH Occupancy Operator Family v0.9

本節點把 v0.8 留下的「位置量詞」正式做成三層可重播物件：

1. 精確的 occupancy-to-operator transfer theorem；
2. 全有理 Dirichlet Green–Schur 自適應覆蓋證書；
3. 由 v0.7 抽象母證書推出的 $58$-cell clamped Green 微半徑證書。

核心修正是：不再尋找通常只能為零的固定共同 PSD floor，也不把 scalar
count lower profile 乘上任意對偶測度。若每個 cell 的 occupancy 已有來源，
則保留未知位置

$$
x_{rk}\in I_r
$$

並直接證明

$$
W(\{x_{rk}\})\succeq0
$$

對所有允許位置共同成立。

## 本輪精確結果

- 同樣總計數為 $2$，若兩點都落在 $1/5$，合成 Green 模型的 Schur
  determinant 為

  $$
  -\frac{254}{558009}<0.
  $$

  因此 scalar count 仍不足以支援 operator positivity。

- 加入兩個分離 occupancy cells

  $$
  I_1=\left[\frac15,\frac25\right],
  \qquad
  I_2=\left[\frac35,\frac45\right],
  $$

  後，根盒的自然區間算術仍無法判定，但自適應二分得到 $8$ 個 certified
  leaves，最大深度為 $7$，全部葉盒的 $2\times2$ Sylvester determinant
  lower bound 嚴格為正。

- 以 v0.7 的固定原子證書為母定理，把 $58$ 個 axis atoms 各自擴成獨立
  closed cell，半徑

  $$
  h=\frac{1}{500000000000000}=2\times10^{-15},
  $$

  可證在 $\alpha=1$ 時整個不確定位置算子族有下界

  $$
  W_1(\mathbf x)
  \succeq
  \frac{
  13498624663403281109
  }{
  2095807970851259765625
  }I
  \succ0.
  $$

- 浮點對抗角點診斷在 cell 半徑 $0.016$ 時仍得到門檻約
  $1.0004702$，在 $0.017$ 時約為 $0.9880614$。這不是 universal
  certificate，但顯示精確微半徑與浮點局部尺度之間約有
  $8\times10^{12}$ 的 proof-budget gap。

## 結論邊界

本輪完成的是位置量詞的合法語義、精確合成模型、覆蓋驗證器，以及一張
條件式抽象 clamped-Green 微半徑證書。它沒有提供 $\zeta$ 零點的
theorem-backed occupancy cells，也沒有完成顯式公式的全域正錐轉移。

因此：

- `exact_synthetic_occupancy_family = true`；
- `conditional_abstract_clamped_family = true`；
- `actual_zeta_occupancy_family = false`；
- `global_rh_certificate = false`。

## 快速重播

在本目錄執行：

```bash
python run_all.py
python run_tests.py
python validate_package.py
```

完整步驟與乾淨解壓重播見 `REPLAY.md`。

## 主要輸出

- `outputs/occupancy_semantic_bridge.json`
- `outputs/dirichlet_green_cover_certificate.json`
- `outputs/dirichlet_green_cover_verification.json`
- `outputs/clamped_58cell_radius_certificate.json`
- `outputs/clamped_58cell_radius_verification.json`
- `outputs/floating_clamped_location_study.json`
- `outputs/experiment_summary.json`
- `metadata/dependency_graph.json`
- `metadata/gap_ledger.json`

