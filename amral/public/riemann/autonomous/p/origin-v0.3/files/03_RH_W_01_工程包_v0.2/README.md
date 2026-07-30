# RH-W-01 工程包 v0.2

本包延續 RH GAP Atlas 的第一個工程節點，建立一個可驗證的 `GBUMP` 測試函數族。

核心構造：

$$
D=x\frac{d}{dx},
\qquad
 g=D(D+1)h,
\qquad
 h\in C_c^\infty(0,\infty).
$$

其 Mellin 變換自動滿足：

$$
\widetilde g(s)=s(s-1)\widetilde h(s),
$$

所以 $\widetilde g(0)=\widetilde g(1)=0$ 為精確恆等式；同時 $f_g\in C_c^\infty\subset\mathcal W$。

## 文件

- `01_RH-W-01_基準規格_v0.1.md`：上一輪 B0 規格。
- `02_RH-W-01_DEFG_生成族閉合_v0.2.md`：本輪完整推導與 GAP 狀態。
- `rh_w01_generator.py`：參數化生成器與兩個獨立相關實作。
- `validate_w01_v02.py`：數值回歸與 metadata 驗證。
- `candidate_GBUMP_001.json`：第一個 proof-oriented 候選描述。
- `RH-W-01_subgaps_v0.2.csv/json`：子 GAP 狀態。
- `VALIDATION.txt`：本機驗證結果。

## 執行

```bash
python validate_w01_v02.py
```

數值測試只用於偵測實作錯誤；數學合法性由主文件中的解析推導提供。
