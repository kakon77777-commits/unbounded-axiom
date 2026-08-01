# RH-W-07：證書架構與 GAP 更新

**版本：** v0.1  
**日期：** 2026-07-23

---

# 1. 四層信任架構

本輪把多素數計算分成四層：

## L0：探索層

可使用：

- NumPy 特徵值；
- 浮點參數掃描；
- AI 產生基底與 witness；
- 中點矩陣的快速 inertia。

這一層只能輸出：

```text
NUMERICAL_CANDIDATE
```

## L1：區間生成層

`build_multiprime_chamber.py` 負責：

- 嚴格列舉 von Mangoldt 非零索引；
- 證明 $n\ge8$ 不可能作用；
- 區間求值 $f_{ij}(\pm\log n)$；
- 計算端點、常數、阿基米德與 prime-power 區塊；
- 輸出有理區間 JSON。

## L2：小型 exact verifier

`verify_multiprime_certificate.py` 只使用：

```python
int
fractions.Fraction
```

它驗證：

1. activation graph；
2. 固定有理中心與 row-radius；
3. $C-\delta I$ 的 exact $LDL^T$；
4. $\delta-\epsilon>0$；
5. 四個 strict sign-flip witnesses。

## L3：形式化層

尚未完成。未來把：

- B-spline 支撐；
- von Mangoldt 篩選；
- 有理區間運算；
- $LDL^T$ 正定性；

移植到 Lean 或 Coq。

---

# 2. 為何固定有理網格很重要

高精度區間的自然中點可能具有極大的分母。直接做 exact $LDL^T$，驗證成本會因分數膨脹而失控。

本輪改為選定：

$$
C_{ij}\in10^{-20}\mathbb Z,
$$

並把中心量化誤差重新併入 $E=M-C$ 的區間半徑。

因此：

$$
\text{分析精度}
$$

與：

$$
\text{驗證器分母複雜度}
$$

被正式分離。

這個動作不犧牲嚴格性，只稍微擴大誤差預算。

---

# 3. 證書內容

主證書：

```text
multiprime_9x9_interval.json
```

包含：

- 九個基底與支撐參數；
- 每個 lag 的完整顯式公式 audit；
- $2,3,4,5,7$ 各 prime-power block；
- $9\times9$ 有理區間矩陣；
- 有理中心矩陣的正定裕度；
- cumulative ablation 的探索摘要；
- 四個 exact witness sign flips；
- 明確的非 RH 宣稱契約。

驗證結果：

```text
schema=OK
activation_graph=OK
dimension=9
delta=1/2000
ldlt_pivots_positive=9
strict_sign_flips=4
status=CERTIFIED_POSITIVE_ON_THIS_9D_SUBSPACE
RH_CLAIM=False
```

---

# 4. GAP 狀態

| GAP | 狀態 |
|---|---|
| von Mangoldt prime-power 篩選 | `CLOSED_FOR_N_LE_7` |
| shifted support-window 判定 | `CLOSED_FOR_CURRENT_SPLINES` |
| 九個 lag 的 activation graph | `CLOSED` |
| 真實多素數 $9\times9$ 區間矩陣 | `CLOSED` |
| exact 九維正定證書 | `CLOSED` |
| 四個 cumulative sign-flip witnesses | `CLOSED_FOR_FIXED_WITNESSES` |
| 任意有理基底的通用編譯器 | `PARTIAL_FIXED_FAMILY` |
| 無界 prime-power 尾 | `OPEN_ENGINEERING` |
| 自動參數／腔室搜尋 | `OPEN_ENGINEERING` |
| 真實負證人 | `NOT_FOUND` |
| 形式化後端 | `OPEN` |

---

# 5. 本輪沒有被證明的敘述

不得輸出：

$$
\text{「加入每一個素數都會使 Weil 形式更正」}.
$$

本輪只證明四個指定方向上的符號翻轉。

不得輸出：

$$
\text{「九維矩陣正定支持 RH 因而接近證明」}.
$$

有限維正定是預期現象之一，不具全域充分性。

不得把人工消融矩陣稱為 zeta 的新形式。只有全部合法 prime-power 區塊同時存在時，才是本輪固定顯式公式的真實矩陣。

---

# 6. 下一輪的驗收條件

`RH-W-08` 至少必須具備：

1. 參數化輸入：degree、$h$、shifts、最大支撐；
2. 快速但不可信的 chamber 搜尋器；
3. 候選矩陣最小特徵向量轉有理 witness；
4. 嚴格重建選定候選；
5. 若證書失敗，區分：
   - 真實接近零；
   - 阿基米德尾太寬；
   - 中心量化太粗；
   - 基底條件數太差；
   - prime-power 枚舉不完整；
6. 禁止由正的有限矩陣回推出 RH。
