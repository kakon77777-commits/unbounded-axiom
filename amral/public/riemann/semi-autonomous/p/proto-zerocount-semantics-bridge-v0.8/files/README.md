# RH Zero-Count Semantics Bridge v0.8

本節點修正 v0.2–v0.7 的係數語義，而不是再替同一 witness 調參。

核心結論有三項：

1. 零點計數上界 $U_j$ 合法支配的是

   $$
   \sum_{\gamma\in\Gamma_j}H(\gamma)
   \le
   U_j\sup_{x\in A_j}H(x),
   $$

   所以 v0.6–v0.7 的 upper-profile operator 可解讀為「保守上包絡方法
   的 no-go 證書」，不能解讀為實際零點和的正下界。

2. 零點計數下界 $L_j$ 只無條件給出

   $$
   \sum_{\gamma\in\Gamma_j}H(\gamma)
   \ge
   L_j\inf_{x\in A_j}H(x).
   $$

   它不能乘上一個任意選擇的 dual probability measure。套件內含精確
   二點反例與 rank-one operator 共下界反例。

3. 在 inherited floating lower candidate profile

   $$
   (0,0,0,5.069962795568,26.742367141539)
   $$

   下重新最佳化後，有限 Galerkin 門檻由有效維度 $22$ 的
   $2.666266$ 下降到維度 $190$ 的 $0.129704786$；固定原子測度的
   direct Green 值為 $0.129703128$。因此 lower-profile robust
   obstruction 消失。

這些結果保留 v0.7 的 abstract interval certificate，但否定把 scalar
count interval 直接重型別為 zero-side operator mass。

## 快速重播

```bash
python run_all.py
python run_tests.py
```

主要輸出位於 `outputs/`：

- `semantic_bridge.json`
- `typed_count_profile.json`
- `lineage_semantic_audit.json`
- `lower_profile_experiment.json`
- `experiment_summary.json`
- `output_verification.json`

本套件不是 RH 證明或反證。高度約 $20.4$ 的 patch 只作 prototype；
Platt–Trudgian 已以嚴格 interval computation 驗證 RH 至
$3\cdot10^{12}$，所以它不是未決的實際 $\zeta$ 偏軸目標。
