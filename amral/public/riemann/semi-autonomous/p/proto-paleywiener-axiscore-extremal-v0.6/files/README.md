# RH Paley–Wiener Axis/Core Extremal v0.6

本節點把 v0.5 的有限字典問題提升為一個連續
Paley–Wiener-type Hilbert-space extremal。

主要成果：

1. 在 real-even clamped $H_0^2(-R,R)$ 上建立 positive trace-class primal
   與軸帶／核心 measure dual，並證明 weak duality。
2. 將一軸點、一核心點問題精確降為 rank-two 閉式公式。
3. 導出 clamped bi-Laplacian Green kernel與結構零點的有限秩投影。
4. 用 nested Chebyshev–Galerkin 將 joint dual 從 $7.7882$ 單調降至
   $1.132475$。
5. 將最高維的 58 個軸原子、2 個核心原子直接移入 Green RKHS；字典無關的
   floating threshold 收斂至 $1.1324412$。
6. 將 $\alpha=21/20$、weights、supports 與係數有理化；連續 PSD 判定再降為
   一個 $2\times2$ Schur matrix。其 floating 最小特徵值為
   $0.0698852$。

因此下一節點不再擴充字典，而是對這個小型、顯式、有理化的 Green-kernel
witness 做 interval certification。

入口：

- 主研究稿：
  `PaleyWiener軸核極值_RH連續核對偶原子障礙與二階Schur證書化_v0.6_半AI自主研究稿.md`
- 定理：`THEORY.md`
- 方法：`METHOD.md`
- 結果：`RESULTS.md`
- 信任邊界：`TRUST_BOUNDARY.md`
- 下一節點：`NEXT_NODE_INTERVAL_GREEN.md`
- machine-readable claims、GAP 與 handoff：`metadata/`

本套件不是 RH 證明或反證。`continuous_kernel_floating_obstruction=true`
仍不是 interval-certified analytic certificate。
