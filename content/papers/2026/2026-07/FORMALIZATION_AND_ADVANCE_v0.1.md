# 穩定 Kneser 圖的形式化核心與一般化推進

## ——Lean 4 有限證明、Coq 移植與 $s$-穩定 $3$-集合容量的新研究節點

**作者：Neo.K（研究方向）／Aletheia（形式化、計算與整理）**  
**版本：v0.1**  
**日期：2026-07-11**

---

## 摘要

本文件把既有的 Python verifier 分解為兩條不同但耦合的工作線：

$$
\text{形式化可檢查性}
\qquad\text{與}\qquad
\text{數學結構推進}.
$$

第一條線已得到一個可編譯的 Lean 4 有限核心。它以完全有限的方式重建
 $9$ 點與 $10$ 點的 $3$ -穩定 $3$ -集合圖： $9$ 點核心確為 $K_3$ 且不可二著色；
$10$ 點核心有恰好 $10$ 個穩定 triple，任何 intersecting 色類皆為 star，
故不可三著色。這些不是 Python 輸出的轉錄，而是 Lean kernel 接受的有限命題。

第二條線得到一個新的、仍待一般證明的結構模式。令

$$
M_s(n)
=
\max\left\{
|\mathcal F|:
\mathcal F
\text{ 是 }C_n\text{ 上 }s\text{-穩定 triple 的非 star intersecting family}
\right\}.
$$

對 pair-ray 型 family 的計數產生候選式：

$$
T_s(n)=3n-10s+2,
\qquad n\ge4s-1.
$$

針對 $s=3,4,5,6$ 的精確有限枚舉，在已測區間均得到

$$
M_s(n)=T_s(n).
$$

這是有限資料與結構推導，不是一般定理。更重要的是，分析顯示 $s=3$ 的
star-forcing 容量閉合有一個特殊的因子共振；這正說明為何原本證明不能被
天真地外推至一般 $s$ 。

---

# 1. 形式化邊界

## 1.1 已由 Lean 4 編譯的有限命題

`FormalKneser/FiniteKernel.lean` 實作：

- 圓環距離；
- 嚴格遞增 triple 的完整枚舉；
- $3$-stability；
- triple 是否相交；
- intersecting family 與 star；
- 有限著色的完整枚舉與 properness 檢查。

已編譯的定理為：

$$
\operatorname{StableTriples}_3(9)
=
\{\{0,3,6\},\{1,4,7\},\{2,5,8\}\},
$$

且三者兩兩不交，因此：

$$
\chi\!\left(KG(9,3)_{3\text{-stab}}\right)>2.
$$

同時，Lean 以窮舉驗證：

$$
|V(KG(10,3)_{3\text{-stab}})|=10,
$$

每個 intersecting 子族都有共同中心，並且：

$$
\chi\!\left(KG(10,3)_{3\text{-stab}}\right)>3.
$$

這個階段的價值在於建立了不依賴外部求解器輸出的 kernel-checked 最小底座。

所有上述 Lean 定理均使用 kernel reduction：

$$
\texttt{decide}
\quad\text{或}\quad
\texttt{decide +kernel},
$$

而不是 native evaluation。`AxiomAudit.lean` 對五個有限定理均回報：

$$
\text{does not depend on any axioms}.
$$

此外，建置後的 `FormalKneser.FiniteKernel` 已以：

```text
leanchecker --fresh FormalKneser.FiniteKernel
```

重放檢查且無錯誤。因此這一段的信任邊界比「外部程式回傳 true」更窄：它是
Lean kernel 與外部 checker 均接受的有限陳述。

## 1.2 尚未形式化的部分

目前不能宣稱 Lean 已形式化：

1. $10\le n\le14$ 的所有有理對偶證書；
2. maximal intersecting $3$-family 的一般分類；
3. $M_3(n)=3n-28$ 的解析容量引理；
4. star peeling 的一般遞歸；
5. $\chi(KG(n,3)_{3\text{-stab}})=n-6$ 的完整無公理機械證明。

因此現階段標記是：

$$
\boxed{\text{Finite formal kernel completed; full theorem formalization open.}}
$$

## 1.3 Coq/Rocq 的位置

`Coq/KneserFiniteKernel.v` 已寫成標準函式庫的對應有限 checker，使用
`vm_compute` 證明同一組有限等式。由於本工作環境沒有 `coqc` 或 Rocq 執行器，
它尚未得到第二個 kernel 的編譯回條。這是明確待辦，而非已完成的雙系統驗證。

---

# 2. 一般 $s$ 的 pair-ray 容量

取循環上的 kernel：

$$
(a,b,c)=(0,s,2s).
$$

考慮三條 pair-rays：

$$
\{abx\},\qquad\{acy\},\qquad\{bcz\}.
$$

對固定 pair，第三點必避開兩端點各自半徑 $s-1$ 的禁止鄰域。每個鄰域大小為：

$$
2s-1.
$$

若 pair 的循環距離是 $s$ ，兩個禁止鄰域交疊 $s-1$ 點，故其聯集大小為：

$$
3s-1,
$$

因此一條短 pair-ray 有：

$$
n-(3s-1)=n-3s+1
$$

個穩定 triple。

當 $n\ge4s-1$ 時，第三個 kernel pair 的距離至少為 $2s-1$ ，兩個禁止鄰域不再交疊，
其聯集大小為：

$$
4s-2.
$$

故三條 rays 的聯集大小為：

$$
2(n-3s+1)+(n-4s+2)-2
=
3n-10s+2.
$$

最後的 $-2$ 是因為 kernel triple 被三條 ray 重複計數三次，聯集只能保留一次。

因此得到候選容量：

$$
\boxed{T_s(n)=3n-10s+2}\qquad(n\ge4s-1).
$$

在邊界 $n=4s-2$ ，第三 pair 的禁止鄰域仍有一點交疊，容量提高一：

$$
T_s(4s-2)+1.
$$

這正好解釋有限枚舉中的例外，而不是隨機的常數漂移。

---

# 3. 精確有限資料

下表的 $M_s(n)$ 由 maximal intersecting family 的完整枚舉取得；`type-2` 是明確
pair-ray 構造的大小。

| $s$ | $n$ | 實測 $M_s(n)$ | type-2 | $3n-10s+2$ | 判讀 |
|---:|---:|---:|---:|---:|---|
| 3 | 11 | 5 | 5 | 5 | 門檻後吻合 |
| 3 | 15 | 17 | 17 | 17 | 門檻後吻合 |
| 4 | 14 | 5 | 5 | 4 | $n=4s-2$ 的 $+1$ 邊界例外 |
| 4 | 15 | 7 | 7 | 7 | 門檻後吻合 |
| 4 | 18 | 16 | 16 | 16 | 門檻後吻合 |
| 5 | 18 | 7 | 7 | 6 | $n=4s-2$ 的 $+1$ 邊界例外 |
| 5 | 19 | 9 | 9 | 9 | 門檻後吻合 |
| 5 | 20 | 12 | 12 | 12 | 門檻後吻合 |
| 6 | 22 | 9 | 9 | 8 | $n=4s-2$ 的 $+1$ 邊界例外 |
| 6 | 23 | 11 | 11 | 11 | 門檻後吻合 |

這支持下列可證偽猜想：

$$
\boxed{
M_s(n)=3n-10s+2
\quad
\text{for }s\ge3,\ n\ge4s-1.
}
$$

它仍需要逐型分類證明；目前資料不足以把它升格為定理。

---

# 4. 為何 $s=3$ 是一個結構共振點

$s$-穩定 triple 的頂點數為：

$$
V_s(n)
=
\frac{n(n-3s+1)(n-3s+2)}6.
$$

若採用一般化目標：

$$
\chi\!\left(KG(n,3)_{s\text{-stab}}\right)=n-2s,
$$

則反設色數為：

$$
q=n-2s-1.
$$

在 $s=3$ ，恰有：

$$
q=n-7=n-3s+2.
$$

於是頂點數中的一個因子能直接消去：

$$
\frac{n(n-7)(n-8)}6
\le
(n-7)(3n-28)
$$

化為：

$$
(n-12)(n-14)\le0.
$$

所以 $n\ge15$ 時，非 star 色類不可能覆蓋全部頂點，必出現 star。

但：

$$
n-2s-1=n-3s+2
\iff
s=3.
$$

因此這個一行式容量閉合不是一般 $s$ 的普遍技巧；它是 $s=3,k=3$ 的特殊代數共振。

這不是壞消息，而是精確定位了下一個 GAP：

$$
\boxed{
\text{一般 }s\text{ 需要加權 star-forcing，而不能只靠均勻容量計數。}
}
$$

---

# 5. 加權對偶的新路徑

令 $\tau(A)$ 表示 triple $A$ 的循環 gap multiset。對 rotation-invariant 權重
$w_{\tau(A)}\ge0$ ，考慮線性規劃：

$$
\max\sum_{A\in V}w_{\tau(A)}
$$

subject to:

$$
\sum_{A\in\mathcal F}w_{\tau(A)}\le1
$$

for every maximal non-star intersecting family $\mathcal F$.

若最優值嚴格大於 $q=n-2s-1$ ，則任何 $q$ 個 non-star 色類都不能覆蓋全部頂點，
從而強迫至少一個 star 色類。

這個程序先精確重現了既有 $s=3,n=11,12,13,14$ 的有理證書。例如：

$$
(s,n)=(3,13)
\quad\Rightarrow\quad
\sum_A w_A=\frac{377}{56}>6.
$$

它也在尚未被原路線覆蓋的有限案例找到 rotation-invariant 最優解，並將下列選定
案例有理化後逐個 maximal non-star family 做 exact recheck：

| 案例 | 精確對偶總重 | $q=n-2s-1$ | 精確餘裕 |
|---|---:|---:|---:|
| $s=4,n=14$ | $7$ | $5$ | $2$ |
| $s=4,n=16$ | $\frac{26}{3}$ | $7$ | $\frac{5}{3}$ |
| $s=4,n=18$ | $\frac{1362}{113}$ | $9$ | $\frac{345}{113}$ |
| $s=5,n=17$ | $\frac{17}{2}$ | $6$ | $\frac{5}{2}$ |
| $s=5,n=20$ | $\frac{25}{2}$ | $9$ | $\frac{7}{2}$ |

上述表中的權重已通過 Python 的 exact rational recheck，即每個 maximal non-star
family 的總重不超過 $1$ 。它們仍不是形式化定理：下一步必須輸入 Lean/Coq 的
certificate checker，讓有理算術與列舉結果也受 proof assistant 檢查。

---

# 6. 下一輪的具體研究義務

1. 把 $s=3,n=11\ldots14$ 的有理對偶證書正式移入 Lean checker；
2. 將 Coq/Rocq port 實際編譯，形成第二 kernel 的回條；
3. 對 $s=4,5$ 的 LP 解做有理化與 exact recheck；
4. 證明或反駁：

$$
M_s(n)=3n-10s+2
\qquad(n\ge4s-1);
$$

5. 尋找可取代 $s=3$ 因子消去的加權遞歸不變量。

最重要的規則保持不變：

$$
\text{有限資料}
\not\Rightarrow
\text{一般證明},
$$

但有限資料可以把下一個真正需要證明的命題壓縮成可形式化的單一 GAP。
