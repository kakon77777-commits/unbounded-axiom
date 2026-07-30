# RH-W-11：混合階字典與 Pareto 設計 v0.1

- 節點：`RH-W-11-MIXED-KERNEL-PARETO`
- 日期：2026-07-23
- 狀態：設計規格已完成；真實混合階 Weil 矩陣留待 `RH-W-12`

---

## 1. 為什麼單一核不夠

若只看 prime boundary 靈敏度，最低階核最好；若只看尾界與頻域衰減，高階核最好。兩個目標相反：

$$
\text{boundary sensitivity}
\quad\leftrightarrow\quad
\text{certification regularity}.
$$

所以不應把核選擇壓成單一排名。

本工程採 Pareto 規則：只淘汰同時在靈敏度、正則性、尾界成本與數值條件上都更差的核。對目前 $m=0,1,2,3,4,5$ 的 B-spline 族，沒有一個核在所有指標上支配其餘核。

---

## 2. 建議的雙通道核心

第一版混合階字典選擇：

$$
\boxed{m=1\quad\text{與}\quad m=3}.
$$

### 感測通道：$m=1$

線性 B-spline 的自相關為 degree-$3$：

$$
\beta_1*\beta_1=\beta_3.
$$

prime boundary 以

$$
\varepsilon^3
$$

出現，對 `RH-W-10` 的穿透深度可產生約 $10^{-11}$ 的 prime-$3$ 局部元素。

它比 cubic 自相關的 $10^{-28}$ 大約十六個數量級，仍保持連續基底與 $C^2$ 相關核。

### 證書通道：$m=3$

cubic B-spline 的自相關為 degree-$7$：

$$
\beta_3*\beta_3=\beta_7.
$$

它的 prime boundary 靈敏度低，但：

- 相關核為 $C^6$；
- Fourier 衰減為 $|\xi|^{-8}$；
- 阿基米德 Laplace 尾可使用更高階導數展開；
- 既有 `RH-W-05` 至 `RH-W-10` 程式可重用。

---

## 3. 交叉通道自動形成中間階

混合字典最有價值的地方不是簡單拼接兩套基底，而是交叉相關自動產生第三層：

$$
\beta_1*\beta_3=\beta_5.
$$

所以 $m=1/3$ 混合字典中的相關階數為：

| 配對 | 相關 degree | prime 啟動階數 | 邊界正則性 |
|---|---:|---:|---:|
| $1\times1$ | 3 | 3 | $C^2$ |
| $1\times3$ | 5 | 5 | $C^4$ |
| $3\times3$ | 7 | 7 | $C^6$ |

因此同一個矩陣天然包含：

$$
\boxed{
\varepsilon^3,
\quad
\varepsilon^5,
\quad
\varepsilon^7
}
$$

三個算術感測尺度。

這比「先用低階找候選，再完全換一套高階基底驗證」更好，因為不同尺度在同一個 Hermitian 矩陣中耦合，最低模態可以自行選擇需要的靈敏度層。

---

## 4. mixed-order block Toeplitz 結構

對相同平移格點

$$
t_j=jd,
$$

定義兩族基底：

$$
v^{(1)}_j=v_{1,h,t_j},
\qquad
v^{(3)}_j=v_{3,h,t_j}.
$$

若每族有 $N$ 個平移，完整 Weil 矩陣為 $2N\times2N$ block Toeplitz：

$$
M=
\begin{pmatrix}
M^{11} & M^{13}\\
M^{31} & M^{33}
\end{pmatrix},
$$

其中：

$$
M^{11}_{ij}\leftrightarrow\beta_3,
$$

$$
M^{13}_{ij}\leftrightarrow\beta_5,
$$

$$
M^{33}_{ij}\leftrightarrow\beta_7.
$$

Gram 矩陣具有同樣區塊結構：

$$
G=
\begin{pmatrix}
G^{11} & G^{13}\\
G^{31} & G^{33}
\end{pmatrix}.
$$

每個 block 只依 lag $i-j$，所以不需要重新計算 $O(N^2)$ 個互不相關的元素；只需編譯每個 block 的有限 lag 表。

---

## 5. `RH-W-12` 的證書契約

下一輪的真實矩陣必須同時滿足：

### 5.1 完整顯式公式

每一個 $M^{ab}_{ij}$ 必須分解為：

$$
\text{端點／pole}
+
\text{常數}
+
\text{阿基米德}
+
\sum_{p^k}\text{prime-power sample}.
$$

不能只計算 local prime block。

### 5.2 完整 prime-power 枚舉

對每個 cross-correlation 支撐，必須證明：

- 哪些 $\pm\log p^k$ 位於支撐中；
- 位於哪個 spline piece；
- 其區間不跨 knot 或支撐邊界。

### 5.3 exact Gram

由 B-spline 卷積閉合，Gram 元素可由相應 $\beta_{m+n+1}$ 在 lag 點的值精確給出。

### 5.4 譜判定

探索層可使用浮點廣義特徵值；正式層必須使用：

$$
C-\delta G-E\succ0
$$

的純有理 $LDL^T$，或對有理 witness 證明：

$$
c^TMc<0.
$$

### 5.5 不能輸出的結論

即使 $2N\times2N$ 混合矩陣正定，也只能輸出：

$$
\texttt{CERTIFIED\_POSITIVE\_ON\_THIS\_MIXED\_SUBSPACE}.
$$

不能輸出 RH。

---

## 6. 新 GAP

### `RH-W-12-CROSS-ARCH`

需要把目前 degree-$7$ 專用的阿基米德積分器泛化到 degree-$3,5,7$。

### `RH-W-12-CROSS-PRIME`

需要讓 prime-power 編譯器依 block 自動使用不同支撐半徑與 knot 表。

### `RH-W-12-GRAM-CONDITION`

混合不同 degree 後可能出現近線性依賴，必須嚴格控制 $G\succ0$ 與條件數。

### `RH-W-12-MODE-ATTRIBUTION`

若最低模態下降，需要分解它在 $m=1$ 與 $m=3$ 通道中的能量比例，避免把交叉耦合誤讀成單一 prime 事件。

### `RH-W-12-COMPLETENESS`

固定 $h,d,N$ 的混合字典仍是有限維。若要形成可枚舉完備族，需要同時設計：

$$
h\downarrow0,
\qquad
N\uparrow\infty,
\qquad
\text{支撐範圍擴張}.
$$

---

## 7. 設計結論

下一代字典不再只有一種光滑度，而是一個「核階梯」：

$$
\boxed{
\text{低階看見事件，}
\quad
\text{高階壓住尾項，}
\quad
\text{交叉階連接兩者。}
}
$$

這不是把數值方法變複雜，而是承認 Weil 幾何中的感測與證書本來就是兩個不同任務。
