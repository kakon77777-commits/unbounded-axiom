# 下一節點規格：RH 全域支配證書最佳化器 v0.2

**節點 ID：** `N1`  
**狀態：** 待實作  
**輸入前置：** `C4`、`C5`、`C6`  
**核心 GAP：** `G06`、`G07`、`G08`、`G09`

## 1. 研究目標

建立一個最佳化與證書管線，使同一個明確測試函數 $\psi$ 同時滿足：

$$
Q_{\mathrm{arith}}(\psi)\ge\delta>0,
$$

以及嚴格全域支配：

$$
\Delta_K(\psi)>0.
$$

其中：

$$
\Delta_K(\psi)
=
c_K(\psi)
-
E_{\mathrm{axis}}(\psi)
-
E_{\mathrm{mid}}(\psi)
-
E_{\mathrm{tail}}(\psi)
-
E_{\mathrm{unknown}}(\psi).
$$

## 2. 目標負裕量

對合成或條件性偏軸矩形 $K$，定義：

$$
c_K(\psi)
=
-\sup_{w\in K}
2\operatorname{Re}\!\left(G_\psi(w)^2\right).
$$

必要條件：

$$
c_K(\psi)>0.
$$

若輸入包含正繞數下界：

$$
\omega_R(F)\ge m,
$$

則目標總負值至少應以：

$$
mc_K(\psi)
$$

計入。

## 3. 全域誤差預算

### 3.1 軸上項

不得只使用已知前 $50$ 個零點作為完整上界。需以已知前綴加無條件零點計數 majorant：

$$
E_{\mathrm{axis}}
\ge
\sum_{\gamma\in\Gamma_{\mathrm{known}}}
|G(\gamma)|^2
+
\int_{T_0}^{\infty}
W_G(t)\,dN_{\mathrm{maj}}(t).
$$

### 3.2 有限中間窗

對 $T_{\mathrm{target}}<|\operatorname{Re}w|\le T_0$，以分帶上界：

$$
E_{\mathrm{mid}}
\ge
\sum_j
N_{\mathrm{maj}}(I_j)
\sup_{w\in S_j}
\max\!\left(B_w(G),0\right).
$$

### 3.3 未知偏軸項

不得假設非目標零點位於實軸。對臨界帶內未知點，使用：

$$
E_{\mathrm{unknown}}
\ge
\sum_j
N_{\mathrm{maj}}(S_j)
\sup_{w\in S_j}
\max\!\left(B_w(G),0\right).
$$

### 3.4 尾部

使用 Paley–Wiener 衰減、導數總變差與零點計數，形成可區間化的殼層和：

$$
E_{\mathrm{tail}}
\ge
\sum_{n\ge n_0}
N_{\mathrm{maj}}([T_n,T_{n+1}])
\sup_{w\in S_n}|B_w(G)|.
$$

## 4. 約束

必要約束：

$$
G\!\left(\frac i2\right)
=
G\!\left(-\frac i2\right)
=0,
$$

$$
\psi(t)\in\mathbb R,
\qquad
\psi(-t)=\psi(t),
$$

$$
\operatorname{supp}\psi\subseteq[-R,R],
$$

$$
\mathcal N(\psi)=1,
$$

$$
Q_{\mathrm{arith}}(\psi)\ge\delta.
$$

所有正規化必須在矩陣評價與直接函數重算之間交叉核對。

## 5. 搜尋策略

建議分四層：

1. 浮點搜尋：找候選與 Pareto 前緣；
2. 有理化／十進位固定：消除隱藏二進位候選；
3. 驗證數值：連續區域、算術純量與全部誤差外包絡；
4. 小型獨立驗證器：只讀候選與證書，不重新執行最佳化。

## 6. 主輸出

每個候選至少輸出：

```text
candidate_id
exact_test_function
support_radius
endpoint_certificate
normalization_certificate
target_region_certificate
arithmetic_interval
axis_budget
middle_window_budget
unknown_off_axis_budget
tail_budget
global_domination_interval
dependency_list
trust_boundary
```

## 7. 成功與失敗標準

### 成功

只有當：

$$
\inf\Delta_K(\psi)>0
$$

且：

$$
\inf Q_{\mathrm{arith}}(\psi)>0
$$

兩者均以嚴格證書成立，才標記 `global_dominance_candidate_passed=true`。

### 有價值的失敗

若在增加基底、支撐與消去階數後，算術正子空間持續先於全域支配出現而塌縮，應輸出：

$$
\text{positive-dimension frontier}
$$

與：

$$
\text{domination frontier}.
$$

這可以形成「本函數族中的結構性不相容」負結果。

## 8. 禁止偷渡

不得使用：

- RH 下的零點間距或密度界；
- 「其他未知零點都在臨界線」；
- 完整 Weil 正性；
- 只對已知零點表成立的洩漏和；
- 最佳化器成功旗標作為全域最優證明。

## 9. 完成定義

本節點完成時，必須同時交付：

1. 原始碼；
2. 精確候選；
3. 驗證器；
4. 證書 JSON；
5. trust boundary；
6. failure log；
7. 對 `gap_map.json` 的狀態更新；
8. 可由另一個 AI 在沙盒中重播的命令。

