# RH Axis-Target Dual Obstruction v0.3

這個半 AI 自主研究節點回答 v0.2 留下的問題：$[18,23]$ 的高 charge
只是 primal 搜尋失敗，還是目前 $R=3$ 函數類的結構障礙？

答案是後者。在 18 個 patch 的每個有理中心，套件都建立

$$
W_P=10^{-3}T+M_1+2C(z_P)\succ0,
$$

從而對任何滿足中心 unit negativity 的 $A\succeq0$ 推出

$$
J(A)\ge2>1.
$$

主要結果：

- floating witness：18/18 通過，最小特徵值至少
  $3.1042101910\times10^{-5}$；
- exact rational surrogate：tail 與 18 張 witness 的
  $LDL^{\mathsf T}$ pivots 全正；
- quadrature、axis mesh 與 6–12 位有理化擾動全部穩定；
- v0.2 的 18 張 primal Gram matrices 全部通過 dual pairing
  cross-check；
- 支撐掃描顯示第一個抽樣逃逸在 $R=5.1$，穩定全中心逃逸從抽樣
  $R=8.5$ 起，但質數截斷代理相對 $R=3$ 增加約 $59874$ 倍。

這不是 RH 證明或反證。Exact positivity 只屬於匯出的有限有理
surrogate；Fourier 積分、零點計數與 tail theorem 的形式 transfer 尚未
完成。

主研究稿：
`RH軸帶目標對偶障礙_顯式下界與支撐質數成本前沿_v0.3_半AI自主研究稿.md`

快速重播：

```bash
python run_dual_experiment.py
python verify_rational_witnesses.py
python run_sensitivity.py
python -m unittest discover -s tests -v
python validate_package.py
```

下一節點：`RH_Support_Prime_Dual_Frontier_v0.4`。執行前請先閱讀
`TRUST_BOUNDARY.md` 與 `NEXT_NODE_SUPPORT_PRIME_FRONTIER.md`。
