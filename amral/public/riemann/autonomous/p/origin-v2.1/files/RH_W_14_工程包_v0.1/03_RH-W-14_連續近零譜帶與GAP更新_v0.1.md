# RH-W-14：連續近零譜帶與 GAP 更新

**版本：** v0.1  
**日期：** 2026-07-23

---

## 1. 已關閉子節點

### RH-W-14-GENUINE-PARAMETERS

已區分：

- $\alpha$：合同換基底規範，不改變廣義譜；
- $d,\sigma$：真正改變測試子空間。

狀態：**CLOSED**。

### RH-W-14-WEIL-LIPSCHITZ

已由 B-spline 全域導數界建立 degree $3,5,7$ 的 Weil 中心導數上界：

$$
L_3\le175,
\qquad
L_5\le215,
\qquad
L_7\le253.
$$

狀態：**CLOSED**。

### RH-W-14-GRAM-LIPSCHITZ

已證明：

$$
|\Delta G_{ij}|
\le\frac1h|\Delta c_{ij}|.
$$

狀態：**CLOSED**。

### RH-W-14-CHAMBER-STABILITY

已嚴格證明整個參數管內：

- 全域 prime-power 集合保持 $\{2,3,4\}$；
- 所有 spline piece 身分保持不變；
- 最小 sample-to-knot 距離大於 $0.02125$。

狀態：**CLOSED**。

### RH-W-14-CONTINUOUS-LOWER

已證明：

$$
\lambda_{\min}>10^{-8}
$$

在整個二維矩形成立。

狀態：**CLOSED**。

### RH-W-14-CONTINUOUS-UPPER

已由固定整數 witness 證明：

$$
\lambda_{\min}<5\times10^{-8}
$$

在整個二維矩形成立。

狀態：**CLOSED**。

---

## 2. 尚未關閉

### RH-W-14-H-DIRECTION

本輪固定 $h$。尚未建立同時包含尺度變化的三維參數盒。

狀態：**OPEN**。

### RH-W-14-LARGE-TUBE

目前管寬只有 $10^{-12}$ 量級。這是全域 Lipschitz 證書可保證的尺度，不代表真實低譜帶只能如此狹窄。

狀態：**OPEN**。

### RH-W-14-TOPOLOGY

尚未證明近零集合在更大參數域中的連通性、分支數、閉合性或是否形成曲面。

狀態：**OPEN**。

### RH-W-14-DIMENSION-CONTINUATION

尚未將參數管證書與 $N\to N+1$ 的字典維度延拓結合。

狀態：**OPEN**。

### TRUE-WEIL-NEGATIVE-WITNESS

仍未找到。

狀態：**NOT FOUND**。

---

## 3. 對總 GAP 地圖的意義

RH-W 原先是 Weil 正性大 GAP 的一個工作分支。至本輪，它已經形成以下內部鏈：

$$
\text{固定測試核心}
\to
\text{有限矩陣}
\to
\text{prime-power 腔室}
\to
\text{自動搜尋}
\to
\text{混合正則性}
\to
\text{近零單點}
\to
\boxed{\text{嚴格連續參數管}}.
$$

這仍未封閉 Weil 正性大 GAP，但已把單點數值現象提升成可驗證的局部幾何資料。

---

## 4. 下一固定節點

$$
\boxed{
\texttt{RH-W-15-INTERVAL-TAYLOR-TUBE-EXPANSION}
}
$$

目標：

1. 對 $d,\sigma$ 建立一階矩陣導數；
2. 對二階餘項建立 interval Hessian；
3. 保留一階項的符號與 block 結構；
4. 擴大二維管；
5. 若成本允許，加入 $h$ 形成第一個三維參數盒；
6. 區分「證書保守性」與「真實譜帶終止」。
