# Moser 歪度場半自主研究：第 12 輪

## ——獨立 `mpmath.iv` 重播、Interval Newton 與 Arb 缺席邊界

**日期：** 2026 年 7 月 27 日  
**狀態：** 部分獨立區間重播；不是 Arb 證書；非形式證明

---

# 1. 環境結果

本環境沒有 `python-flint`、Arb 或 Sage；套件庫也沒有可安裝的 `python-flint`。

因此本輪沒有宣稱完成 Arb 重播，而採用：

$$
\boxed{\texttt{mpmath.iv}\text{ directed interval arithmetic}}
$$

作為獨立後備驗證。

# 2. 特殊競爭分支

$$
s_{270}\in[0.9989143389428913213797012975,0.9989143392263741131243407093].
$$

$$
\boxed{s_{120}-s_{270}\in[1.584622955726897820027e-9,1.692045182662177229601e-9]}.
$$

下界仍嚴格為正。

平滑候選相對固定事件控制：

$$
\boxed{s_{270}-s_{\mathrm{event},B1}\in[0.00001058181038264642457147,0.00001058209386543816921088]}.
$$

同樣保持嚴格正下界。

# 3. 解析接觸邊界

$19$ 個解析相位邊界重新由 interval balls 計算：

$$
\boxed{19/19}
$$

全部包含第 11 輪保存的浮點值。

# 4. 十二個駐點根盒

| 根 | 簽章 | 類型 | $N(X)\subset\operatorname{int}X$ | 端點換號 | 尺度下界距離 |
|---:|---|---|---:|---:|---:|
| 1 | `L|p0|p2` | smooth_minimum | True | True | 4.6581599e-8 |
| 2 | `L|p0|p2` | smooth_maximum | True | True | 8.1974837e-6 |
| 3 | `L|p0|p2` | smooth_minimum | True | True | 4.5455127e-8 |
| 4 | `p1|p0|p3` | smooth_maximum | True | True | 0.24896511 |
| 5 | `p2|L|p3` | smooth_minimum | True | True | 0.030437642 |
| 6 | `p2|p1|p3` | smooth_maximum | True | True | 0.035237883 |
| 7 | `p2|p1|p0` | smooth_maximum | True | True | 0.17278687 |
| 8 | `p3|p2|p0` | smooth_maximum | True | True | 0.18060899 |
| 9 | `p3|p2|L` | smooth_minimum | True | True | 0.12867719 |
| 10 | `p3|p2|p1` | smooth_maximum | True | True | 0.17020992 |
| 11 | `p0|p3|p1` | smooth_maximum | True | True | 0.089684617 |
| 12 | `p0|p3|p2` | smooth_maximum | True | True | 0.22111049 |

結果：

$$
\boxed{12/12}
$$

個根盒滿足 interval Newton 包含條件；端點導數符號也全部符合極小／極大分類。

# 5. 邊界盒重播

| 邊界 | 公式 | 直接 IV 定號 | 第 11 輪全域安全 | 狀態 |
|---:|---|---:|---:|---|
| 1 | `\pi/2-\alpha` | False | True | dependency_inflation |
| 2 | `\pi/2-\beta` | False | True | dependency_inflation |
| 3 | `\beta-\pi/3` | False | True | dependency_inflation |
| 4 | `\alpha-\pi/3` | False | True | dependency_inflation |
| 5 | `\pi/2` | True | True | direct_pass |
| 6 | `\pi-\alpha` | False | True | dependency_inflation |
| 7 | `\pi-\beta` | False | True | dependency_inflation |
| 8 | `2\pi/3` | True | True | direct_pass |
| 9 | `\pi/2+\beta` | False | True | dependency_inflation |
| 10 | `\pi/2+\alpha` | False | True | dependency_inflation |
| 11 | `\pi` | True | True | direct_pass |
| 12 | `5\pi/3-\alpha` | False | True | dependency_inflation |
| 13 | `5\pi/3-\beta` | False | True | dependency_inflation |
| 14 | `\pi+\beta` | False | True | dependency_inflation |
| 15 | `\pi+\alpha` | False | True | dependency_inflation |
| 16 | `3\pi/2` | True | True | direct_pass |
| 17 | `5\pi/3` | True | True | direct_pass |

直接由 `mpmath.iv` 完成左右定號的邊界：

$$
\boxed{5/17}.
$$

其餘邊界集中在 `L/R` 平滑支撐點生成或消失處。反解公式接近 $\operatorname{atanh}(\pm1)$，普通自然區間擴張非常嚴重，因此本函式庫無法重現第 11 輪的窄盒。

這是 **dependency inflation**，不是發現反例。第 11 輪的解析誤差界與尺度排除仍保留，但未被本輪後備函式庫獨立重播。

# 6. 未完成的部分

原計畫逐一重播第 11 輪的 $579$ 個導數葉盒。實作顯示，每個盒都重新反解平滑支撐點會超過本環境執行上限。

因此本輪沒有把「未跑完」寫成「通過」。正式狀態為：

- 特殊差值：通過；
- 平滑—事件比較：通過；
- 解析邊界 balls：通過；
- 十二根盒 interval Newton：通過；
- 邊界直接 IV：部分通過；
- $579$ 葉盒獨立重播：未完成；
- Arb 重播：未完成。

# 7. 研究判定

最重要的低值競爭與所有光滑駐點，均被另一套區間運算重現。

所以目前可提升到：

$$
\boxed{\text{核心候選與駐點結構具有獨立 IV 重播支持。}}
$$

但不能提升為：

$$
\boxed{\text{完整 Arb 全相位機器證書。}}
$$

# 8. 第 13 輪方向

完整相位框架已經足夠穩定；下一輪轉向平滑五參數事件—KKT 系統：

$$
p=(w,\beta,\delta,c,\varepsilon).
$$

將兩個低相位光滑極小、$120^\circ$ 與 $270^\circ$ 尖點同時等高，再加入分支壓力駐定，判定目前平滑候選是否為該族內的數值孤立點。

真正 Arb 重播則由本輪腳本移交具備 `python-flint` 的外部環境。
