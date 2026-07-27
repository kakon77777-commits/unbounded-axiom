# RH Axis-Notch Cover Co-design v0.5

本節點承接 v0.4 的 12 份 joint-dual witnesses，檢查「在反覆出現的實軸峰值
附近做 value/derivative notch」能否解除有限 Gram 模型的軸側阻擋。

結論分成三層：

1. **齊次缺口的 E0 單調性障礙。** 若加入缺口後的函數空間
   $V'\subseteq V$，則原本已在 $V$ 上做的 PSD Gram 搜尋已包含 $V'$。
   因而單靠 $G(a)=0$ 或 $G'(a)=0$ 縮小空間，不可能創造原問題沒有的
   primal feasible point。
2. **外部頻譜 lift 有改善但飽和。** 加入
   $\psi_\omega(t)=tq_R(t)\sin(\omega t)$ 的新方向後，$R=16$ 的
   uniform/core 指標最多改善約 $3.10\%$；joint raw dual 下界只改善
   $1.12\%$，安全下界仍為 $1.0881>1$。
3. **局部 bump 幾何改善較大但仍被阻擋。** 27 組幾何中最佳
   `d12_w2_p5` 將 joint raw dual 下界改善 $3.87\%$，但
   $\alpha_{\rm safe}=1.071761>1$，故不啟動高成本 primal search。

本節點因此停止三條支線：純齊次 notch、目前的 spectral-slope lift family，
以及更多 polynomial-bump scaling。下一節點改寫成連續
Paley–Wiener axis/core 極值問題，嘗試找出可證的連續下界或極值函數。

主要入口：

- 主研究稿：
  `RH軸缺口共設計的單調性障礙_子空間失效外部升維飽和與PaleyWiener轉向_v0.5_半AI自主研究稿.md`
- 方法：`METHOD.md`
- 結果：`RESULTS.md`
- 信任邊界：`TRUST_BOUNDARY.md`
- 重播：`REPLAY.md`
- 下一節點：`NEXT_NODE_PALEY_WIENER.md`
- machine-readable claims、GAP 與 handoff：`metadata/`

本套件不是 RH 證明或反證，也沒有把離散 floating obstruction 提升成連續
Paley–Wiener 定理。
