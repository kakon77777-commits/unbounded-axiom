# RH-W-02 工程包 v0.1

本包處理 RH GAP Atlas 的 Weil 路線第二節點：測試函數核心、拓撲與閉包傳遞。

本輪最重要結果是精確值域定理：

$$
D(D+1)C_c^\infty(0,\infty)
=
\left\{
 g\in C_c^\infty(0,\infty):
 \int_0^\infty g(x)\frac{dx}{x}=0,
 \ \int_0^\infty g(x)\,dx=0
\right\}.
$$

因此上一輪的解析 `GBUMP` 核心並非任意小子族；它等於完整的緊支撐平滑雙消失矩核心。

本包同時：

- 固定核心的 LF 拓撲；
- 證明原子 bump 字典在核心中稠密；
- 證明 B0 算術二次型在此核心上連續；
- 建立「字典正性傳遞到完整核心」的合法閉包步驟；
- 排除未加解析結構的裸 $L^2$ 完成；
- 將通往 Lagarias 型帶狀解析空間的密度橋標為下一個真正 GAP。

## 文件

- `RH-W-02_核心值域與拓撲_v0.1.md`：完整數學推導與 GAP 判定。
- `RH-W-02_subgaps_v0.1.csv/json`：機器可讀狀態表。
- `rh_w02_validate.py`：值域反演、矩條件與 $L^2$ 失敗證人的數值回歸。
- `VALIDATION.txt`：驗證輸出。

## 執行

```bash
python rh_w02_validate.py
```

數值回歸只檢查實作與公式的一致性；閉合結果由主文件中的解析證明提供。
