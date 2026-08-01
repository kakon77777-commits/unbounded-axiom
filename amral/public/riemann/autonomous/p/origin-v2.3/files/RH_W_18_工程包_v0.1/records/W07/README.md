# RH-W-07 多素數支撐腔室工程包 v0.1

本包把單一 $n=2$ 支撐腔室擴展為包含 $2,3,4,5,7$ 的九維真實 Riemann–Weil 區間矩陣，並建立：

- shifted-window prime-power activation graph；
- 稀疏 Toeplitz 算術區塊；
- 改良的阿基米德 leading-tail 包絡；
- 固定有理網格 midpoint-margin 正定證書；
- 四個 cumulative prime-power exact sign-flip witnesses；
- 純 `Fraction` 小型驗證器。

## 主要檔案

- `01_RH-W-07_多素數支撐腔室編譯器_v0.1.md`：完整推導與結果。
- `02_RH-W-07_證書架構與GAP更新_v0.1.md`：信任邊界與 GAP。
- `build_multiprime_chamber.py`：嚴格矩陣生成器。
- `weil_interval_core.py`：有理區間、B-spline 與顯式公式核心。
- `multiprime_9x9_interval.json`：完整機器證書。
- `verify_multiprime_certificate.py`：純有理驗證器。
- `prime_power_activation_graph.csv`：lag／prime-power 活化表。
- `RH-W-07_subgaps_v0.1.csv`：GAP 登錄。
- `EXACT_VERIFY.txt`、`VALIDATION.txt`：執行快照。

## 重播

```bash
python build_multiprime_chamber.py
python verify_multiprime_certificate.py
```

## 結論邊界

```text
CERTIFIED_POSITIVE_ON_THIS_9D_SUBSPACE
RH_CLAIM=False
```
