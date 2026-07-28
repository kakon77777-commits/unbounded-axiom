# RH-W-02 工程包 v0.2

本版本完成 `RH-W-02-NORMALIZATION`：

$$
Q_{B0}(g)
=-E_{B0}[C_g]
=W[C_g]
=\langle g,g\rangle_W
$$

在緊支撐平滑、雙 Mellin 消失矩核心上精確成立。

## 檔案

- `01_RH-W-02_核心值域與拓撲_v0.1.md`：前一輪核心值域與拓撲結果。
- `02_RH-W-02_正規化對齊_v0.2.md`：本輪完整推導與 GAP 更新。
- `RH-W-02_subgaps_v0.2.csv/json`：更新後的機器可讀登錄。
- `normalization_contract.json`：後續 AI／程式不可偷換的唯一符號契約。
- `rh_w02_normalization_validate.py`：相關積分、卷積、Mellin 因子化及有限零點和回歸。
- `VALIDATION_v0.2.txt`：實際執行結果。

## 執行

```bash
python rh_w02_normalization_validate.py
```

## 邊界

本包沒有證明 Weil 正性、核心充分性或 RH。下一節點是 `RH-W-03-SEPARATION`。
