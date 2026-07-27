# Research Log

## 2026-07-24：接手 v0.4

- 保存 v0.4 joint summary、axis refinement、uniform frontier、prime cost、
  handoff 與 12 份 witnesses。
- 固定先做 dual gate，避免在仍被阻擋的 branch 上支付 primal 與 arithmetic
  matrix 成本。

## 2026-07-24：軸峰 atlas

- 對每份 witness、每個 band 先正規化，再等權聚合 KDE。
- 找到五個主峰 $17.83,20.38,23.24,42.18,83.05$。
- 注意到 $A_1$ 峰與 target real interval 重疊，且遠帶峰近似二倍與四倍尺度。

## 2026-07-24：Taylor notch 與關鍵修正

- 先由 $G(x_0)=0$ 推得
  $G(x_0+iy)^2=-y^2G'(x_0)^2+O(|y|^3)$，提出 value notch / slope 保留。
- 隨後辨認出：齊次 notch 只會生成父空間的子空間，而父 PSD Gram 已搜尋
  全空間。
- 將此提升為 E0 feasible-set inclusion，停止把子空間 notch 當成可行性
  rescue。
- 實驗中 `anchor_flat` 幾乎抹除 derivative，且嚴重破壞 core/axis ratio。

## 2026-07-24：外部 lift

- 新增 real-even compact atoms
  $\psi_{\omega,p}(t)=t(1-t^2/R^2)_+^p\sin(\omega t)$。
- 實作解析二階導數與 constrained-whitened lift。
- 由 1、3、5、6 個方向擴到 21-frequency grid，觀察 screen improvement
  在約 $3\%$ 附近飽和。
- joint raw dual 只改善 $1.12\%$，safe bound 仍為 $1.0881$。

## 2026-07-24：局部幾何 sweep

- 跑完 27 組 density、width、power。
- `d12_w2_p5` screen 最佳，joint raw dual 改善 $3.87\%$。
- safe bound $1.071761>1$，且 tail 最小特徵值約 $0.00115$。
- dense complementary audit 顯示遠帶峰有遷移而非消失；$A_1$ 仍主導。

## 2026-07-24：節點決策

- 不啟動 primal search。
- 停止三個已測 family。
- 下一節點改為 continuous Paley–Wiener / reproducing-kernel extremal
  formulation，尋找離散 dual measures 背後的解析不等式或 extremizer。
