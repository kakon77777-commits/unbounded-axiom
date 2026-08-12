# Series B / Paper 04
# 路徑傳輸、Holonomy 與關係記憶：回到同一位置為何不等於回到同一關係狀態
## Path Transport, Holonomy, and Relational Memory: Why Returning to the Same Position Need Not Mean Returning to the Same Relational State

**系列：** Series B — 觀察者、局部關係、非交換與全域守恆  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-08-10  
**性質：** 基礎定義／橋接論文  
**前篇：** Series B / Paper 03《嵌入觀察者與兩種不可全域性：全域截面的不存在、存在與不可達》

---

## 摘要

Series B 前三篇依序建立：(1) 局部關係順序的可計算差異；(2) 局部界面殘餘提升為 Čech 1-cocycle 與 $H^1$ 阻塞的條件；(3) 全域截面「不存在」與「存在但嵌入觀察者不可達」的形式區分。本文將三者第一次放入同一個動態框架：**觀察者與局部狀態沿路徑被 transport，而閉路 transport 可能留下非平凡 holonomy。**

設 $X$ 為基底脈絡空間， $\mathcal F_x$ 為位置／脈絡 $x$ 上的局部狀態纖維。對每條合法有向路徑

$$
\gamma:x\to y
$$

指定 transport

$$
T_\gamma:\mathcal F_x\to\mathcal F_y,
$$

並要求恆等路徑與路徑合成滿足函子型相容：

$$
T_{\operatorname{id}_x}
=
\operatorname{id}_{\mathcal F_x},
$$

$$
T_{\eta\circ\gamma}
=
T_\eta\circ T_\gamma.
$$

對閉路

$$
\gamma:x\to x,
$$

定義 holonomy

$$
H_x(\gamma)
:=
T_\gamma
\in
\operatorname{Aut}(\mathcal F_x).
$$

若

$$
H_x(\gamma)\neq I,
$$

則路徑雖在基底位置上返回 $x$，其纖維中的關係／frame／局部狀態並未返回原值。本文將這種「閉路後仍被保存的路徑效應」稱為**關係記憶（relational memory）**；但為避免把座標選擇誤認成物理／結構實在，真正的 gauge-stable 對象不是單一矩陣 $H$，而是其共軛類、譜、跡或其他在允許 frame 變換下不變的量。

本文證明一個基本等價：在路徑連通且 transport 可逆的情形，**端點相同的 transport 路徑無關**，當且僅當所有閉路 holonomy 為恆等：

$$
\boxed{
T_{\gamma_1}=T_{\gamma_2}
\ \forall \gamma_1,\gamma_2:x\to y
}
$$

當且僅當

$$
\boxed{
H_x(\ell)=I
\ \forall \ell:x\to x.
}
$$

因此 holonomy 是「歷史是否能被無損遺忘」的全局閉路判準。

本文進一步把 Paper 01 的非交換缺陷與 holonomy 接起來。對可逆局部操作 $A,B$，考慮交換子閉路

$$
\ell_{A,B}
=
ABA^{-1}B^{-1}.
$$

其 holonomy 為群交換子

$$
H(\ell_{A,B})
=
ABA^{-1}B^{-1}.
$$

若 $A=e^X$ 、 $B=e^Y$ 接近恆等，則

$$
\log H(\ell_{A,B})
=
[X,Y]
+
O(3),
$$

所以線性／Lie 意義下的對易子是**無窮小閉路 holonomy 的首階項**。這將 Paper 01 的「局部順序差」提升為 Paper 04 的「閉路關係記憶」。

在 Paper 02 的阿貝爾 Čech 模型中，若邊界殘餘為 $c_{ij}$，對 nerve 上閉路 $\gamma$ 定義

$$
\Omega_c(\gamma)
=
\sum_{(i,j)\in\gamma}c_{ij}.
$$

若 $c$ 改變一個 coboundary：

$$
c\mapsto c+\check db,
$$

則閉路和中的 $b$ 項望遠鏡相消，所以 $\Omega_c(\gamma)$ 不變。於一維 nerve 的適當情形， $[c]\neq0$ 因而可被某個 cycle pairing 偵測為非零 holonomy。這給出 Paper 02 的上同調阻塞與本文閉路記憶之間第一個嚴格接口。

最後，本文將 holonomy 放回 Paper 03 的 observer accessibility。對觀察者 $O$ 的局部觀察映射

$$
A_{O,x}:\mathcal F_x\to\mathcal D_O,
$$

若

$$
A_{O,x}\circ H_x(\gamma)
=
A_{O,x},
$$

則該閉路雖有纖維 holonomy，對 $O$ 不可觀察；若不相等，則 observer 能從返回後的局部資料辨識出「曾經走過某條路」。因此本文首次正式區分：

$$
\boxed{
\text{holonomy exists}
}
$$

與

$$
\boxed{
\text{holonomy is observable}.
}
$$

這一區分將成為後續跨觀察者 transport 與守恆階層的基礎。

**關鍵詞：** 路徑傳輸、holonomy、關係記憶、非交換、群交換子、observer accessibility、Čech cocycle、局部—全域、歷史依賴、gauge covariance

---

# 1. 從「順序不同」進入「走一圈仍留下東西」

Paper 01 研究：

$$
\Delta_x(\gamma,\eta)
=
d(F_\gamma(x),F_\eta(x)),
$$

即兩條路徑從同一點出發，最後可能到不同狀態。

Paper 02 則研究：

$$
[c]\in H^1,
$$

即一族局部界面差是否能被全域局部 frame 重新選擇消掉。

本文考慮第三種、位於兩者中間的重要結構：

> 路徑的起點與終點是同一個局部位置，但沿途的 transport 使內部關係狀態發生不可消去的變化。

即：

$$
\gamma:x\to x,
$$

但：

$$
T_\gamma\neq I.
$$

這就是 holonomy 型現象。

本文不宣稱 holonomy 是新數學；它是微分幾何、規範理論、纖維叢與群胚理論中的標準結構。Series B 的工作是把它重新放入：

$$
\boxed{
\text{observer}
+
\text{local relation}
+
\text{ordered path}
+
\text{global accessibility}
}
$$

這條統一研究線裡。

---

# 2. 基底、纖維與 transport

## 定義 2.1（局部關係纖維系統）

取基底空間：

$$
X.
$$

對每個：

$$
x\in X,
$$

指定一個局部狀態／frame／關係資料空間：

$$
\mathcal F_x.
$$

所有纖維的集合可記為：

$$
\mathcal F
=
\bigsqcup_{x\in X}\mathcal F_x.
$$

本文不要求一開始就是光滑纖維叢；離散圖、groupoid、有限狀態系統也允許。

---

## 定義 2.2（合法路徑）

記：

$$
\Gamma(x,y)
$$

為從 $x$ 到 $y$ 的合法有向路徑集合。

若：

$$
\gamma\in\Gamma(x,y),
$$

寫作：

$$
\gamma:x\to y.
$$

---

## 定義 2.3（路徑傳輸）

對每條合法路徑：

$$
\gamma:x\to y,
$$

指定：

$$
\boxed{
T_\gamma:
\mathcal F_x
\to
\mathcal F_y.
}
$$

若所有 $T_\gamma$ 可逆，則：

$$
T_{\gamma^{-1}}
=
T_\gamma^{-1}.
$$

要求：

$$
T_{\operatorname{id}_x}
=
I_x,
$$

以及：

$$
\boxed{
T_{\eta\circ\gamma}
=
T_\eta\circ T_\gamma.
}
$$

因此 transport 是路徑 groupoid 到局部狀態轉換範疇的一個函子型表示。

---

# 3. 為什麼局部狀態不能只寫成一個全域 $x$

如果所有：

$$
\mathcal F_x
$$

都已經被 canonical 地識別成同一個空間 $\mathcal F$，並且識別方式本身與路徑無關，那麼很多 transport 結構會被提前消掉。

Series B 刻意保留：

$$
\mathcal F_x
$$

與：

$$
\mathcal F_y
$$

的區別。

原因是：

> 在局部—觀察者數學中，「同一類型的資料」不代表「已經有一個無路徑成本的全域同一化」。

transport 本身就是那個「如何把此處的局部資料拿到彼處比較」的結構。

---

# 4. Holonomy

## 定義 4.1（閉路）

若：

$$
\gamma:x\to x,
$$

稱 $\gamma$ 為以 $x$ 為基點的閉路。

---

## 定義 4.2（Holonomy）

對閉路 $\gamma$，定義：

$$
\boxed{
H_x(\gamma)
=
T_\gamma
\in
\operatorname{Aut}(\mathcal F_x).
}
$$

若：

$$
H_x(\gamma)=I_x,
$$

稱該閉路 transport-trivial。

若：

$$
H_x(\gamma)\neq I_x,
$$

稱其具有非平凡 holonomy。

---

# 5. 「回到同一位置」和「回到同一狀態」正式分裂

令：

$$
v\in\mathcal F_x.
$$

沿閉路 $\gamma$ transport：

$$
v
\mapsto
H_x(\gamma)v.
$$

若：

$$
H_x(\gamma)v
\neq
v,
$$

則：

$$
\boxed{
\text{base position returned}
}
$$

但：

$$
\boxed{
\text{fiber state did not return}.
}
$$

這是本文標題的精確內容。

因此「位置」只記基底：

$$
x.
$$

真正的完整局部狀態至少是：

$$
(x,v).
$$

閉路可以滿足：

$$
x_{\mathrm{final}}
=
x_{\mathrm{initial}},
$$

卻：

$$
v_{\mathrm{final}}
\neq
v_{\mathrm{initial}}.
$$

---

# 6. 關係記憶

## 定義 6.1（原始關係記憶）

對閉路 $\gamma$，稱：

$$
H_x(\gamma)
$$

為該路徑在 $x$ 留下的**原始關係記憶**。

但這個名稱只是一個 Series B 的解讀名稱；數學對象本身仍是標準 holonomy。

---

## 為什麼叫「記憶」

因為若只知道終點位置：

$$
x,
$$

不足以知道系統是否曾經：

1. 留在原地；
2. 繞過閉路 $\gamma_1$ ；
3. 繞過閉路 $\gamma_2$。

如果：

$$
H_x(\gamma_1)
\neq
H_x(\gamma_2),
$$

那麼路徑歷史已被保存在纖維變換中。

因此：

$$
\boxed{
\text{history survives endpoint projection}.
}
$$

這正是「記憶」一詞的技術直覺。

---

# 7. Gauge / frame 改變：單一 $H$ 不一定是 invariant

令每個纖維重新選擇 frame：

$$
g_x:
\mathcal F_x
\to
\mathcal F_x.
$$

transport 變成：

$$
T_\gamma'
=
g_y
T_\gamma
g_x^{-1}.
$$

若 $\gamma$ 為閉路：

$$
x\to x,
$$

則：

$$
\boxed{
H_x'(\gamma)
=
g_x
H_x(\gamma)
g_x^{-1}.
}
$$

因此單一矩陣表示 $H_x(\gamma)$ 依 frame 而變。

真正穩定的對象應取：

- 共軛類；
- trace；
- determinant；
- spectrum；
- characteristic polynomial；
- 或其他 gauge-invariant function。

---

## 定義 7.1（Gauge-stable relational memory）

若 $\mathcal I$ 是對共軛不變的函數：

$$
\mathcal I(gHg^{-1})
=
\mathcal I(H),
$$

則：

$$
\boxed{
M_{\mathcal I}(\gamma)
=
\mathcal I(H_x(\gamma))
}
$$

稱為該閉路的 gauge-stable relational memory。

因此 Series B 不把「矩陣元素變了」直接當成世界留下記憶；必須先排除純 frame artifact。

---

# 8. 主定理：路徑無關 $\Longleftrightarrow$ 閉路 holonomy 平凡

## 定理 8.1（路徑無關判準）

假設：

1. transport 可逆；
2. 相關區域路徑連通。

則下列兩條等價。

### (A) 端點 transport 路徑無關

對任意：

$$
\gamma_1,\gamma_2:x\to y,
$$

皆有：

$$
T_{\gamma_1}
=
T_{\gamma_2}.
$$

### (B) 所有閉路 holonomy 平凡

對任意：

$$
\ell:x\to x,
$$

皆有：

$$
H_x(\ell)=I_x.
$$

---

## 證明

### $(A)\Rightarrow(B)$

取閉路：

$$
\ell:x\to x.
$$

另取恆等路徑：

$$
\operatorname{id}_x:x\to x.
$$

由路徑無關：

$$
T_\ell
=
T_{\operatorname{id}_x}
=
I_x.
$$

故：

$$
H_x(\ell)=I_x.
$$

---

### $(B)\Rightarrow(A)$

取：

$$
\gamma_1,\gamma_2:x\to y.
$$

考慮閉路：

$$
\ell
=
\gamma_2^{-1}\circ\gamma_1
:
x\to x.
$$

由假設：

$$
T_\ell=I_x.
$$

而：

$$
T_\ell
=
T_{\gamma_2^{-1}}
T_{\gamma_1}
=
T_{\gamma_2}^{-1}
T_{\gamma_1}.
$$

故：

$$
T_{\gamma_2}^{-1}
T_{\gamma_1}
=
I.
$$

所以：

$$
T_{\gamma_1}
=
T_{\gamma_2}.
$$

∎

---

# 9. 歷史何時可以被無損遺忘

由定理 8.1：

$$
\boxed{
H(\ell)=I
\ \forall \ell
}
$$

意味：

> transport 只依賴起終點，不依賴中間走過哪一條路。

這正是最強的 history-free régime。

反之，只要存在：

$$
H(\ell)\neq I,
$$

就存在至少兩條相同起終點路徑具有不同 transport。

所以：

$$
\boxed{
\text{nontrivial holonomy}
\Rightarrow
\text{path history cannot be globally erased}.
}
$$

這是 Paper 01 「history-sensitive」概念的閉路版本。

---

# 10. Paper 01 的交換子如何變成閉路

Paper 01 的最小非交換量是：

$$
[A,B]
=
AB-BA.
$$

如果 $A,B$ 可逆，更自然的閉路量是**群交換子**：

$$
\boxed{
K(A,B)
=
ABA^{-1}B^{-1}.
}
$$

若：

$$
AB=BA,
$$

則：

$$
K(A,B)=I.
$$

反之若：

$$
K(A,B)\neq I,
$$

表示：

> 先沿 $A$ 、再 $B$ 、再撤銷 $A$ 、再撤銷 $B$，即使基底操作形式上「走回來」，纖維仍留下殘餘。

---

# 11. 一個完全有限的矩陣閉路例

取：

$$
A=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix},
$$

$$
B=
\begin{pmatrix}
1&0\\
1&1
\end{pmatrix}.
$$

兩者皆可逆，且：

$$
\det A=\det B=1.
$$

計算：

$$
K
=
ABA^{-1}B^{-1}
=
\begin{pmatrix}
3&-1\\
1&0
\end{pmatrix}.
$$

顯然：

$$
K\neq I.
$$

所以交換子閉路具有非平凡 holonomy。

例如取：

$$
v=
\begin{pmatrix}
1\\
0
\end{pmatrix},
$$

則：

$$
Kv
=
\begin{pmatrix}
3\\
1
\end{pmatrix}
\neq
v.
$$

即：

$$
\boxed{
\text{走完 }A,B,A^{-1},B^{-1}
\text{ 後，局部纖維仍記得順序。}
}
$$

---

# 12. 無窮小版本：Lie 交換子是首階 holonomy

令：

$$
A=e^X,
\qquad
B=e^Y,
$$

且 $X,Y$ 足夠小。

群交換子：

$$
K
=
e^Xe^Ye^{-X}e^{-Y}.
$$

由 BCH 型展開：

$$
\boxed{
\log K
=
[X,Y]
+
O\!\left(
\|X\|^2\|Y\|
+
\|X\|\|Y\|^2
\right).
}
$$

所以：

$$
[X,Y]
$$

不是和 holonomy 無關的另一個東西。

它是：

$$
\boxed{
\text{無窮小交換閉路所留下的首階關係記憶}.
}
$$

這給 Paper 01 與 Paper 04 一條直接數學橋。

---

# 13. 從局部對易子到曲率的接口

在光滑 connection 情況下，無窮小閉路 holonomy 的首階面積項由 curvature 控制。

Series B 暫時不重建整套微分幾何，只記錄結構位置：

$$
\boxed{
\text{local commutator}
\to
\text{infinitesimal loop residue}
\to
\text{curvature}
\to
\text{finite holonomy}.
}
$$

這意味：

> 非交換不只可以被看成兩步順序差，也可以在適當幾何結構下成為曲率／閉路 transport 的局部生成元。

但這個結論需要 connection 等額外結構；一般 DPE 缺陷 $\delta$ 不自動等於曲率。

---

# 14. Paper 02 的 $H^1$ 如何變成環路量

現在回到 Paper 02 的阿貝爾係數版本。

令 nerve 上每條有向邊：

$$
i\to j
$$

帶一個：

$$
c_{ij}\in A,
$$

其中 $A$ 為阿貝爾群。

對閉路：

$$
\gamma:
i_0\to i_1\to\cdots\to i_n=i_0,
$$

定義：

$$
\boxed{
\Omega_c(\gamma)
=
\sum_{k=0}^{n-1}
c_{i_k i_{k+1}}.
}
$$

這就是阿貝爾化的 loop transport residue。

---

# 15. Coboundary 不改變閉路和

若：

$$
c'
=
c+\check db,
$$

則：

$$
c'_{ij}
=
c_{ij}+b_j-b_i.
$$

沿閉路相加：

$$
\Omega_{c'}(\gamma)
=
\sum(c_{ij}+b_j-b_i).
$$

 $b$ 項望遠鏡相消：

$$
\sum(b_j-b_i)=0.
$$

故：

$$
\boxed{
\Omega_{c'}(\gamma)
=
\Omega_c(\gamma).
}
$$

因此閉路殘餘只依賴 cohomology class：

$$
[c],
$$

而不依賴代表元的局部 frame 選擇。

這是 Paper 02 與 holonomy 最乾淨的數學接口之一。

---

# 16. 三脈絡環例再次出現

Paper 02 的三脈絡環：

$$
U_1\leftrightarrow U_2
\leftrightarrow U_3
\leftrightarrow U_1
$$

取：

$$
A=\mathbb Z/2,
$$

以及：

$$
c_{12}=c_{23}=c_{31}=1.
$$

對環路：

$$
\gamma:
1\to2\to3\to1,
$$

有：

$$
\Omega_c(\gamma)
=
1+1+1
=
1
\pmod2.
$$

因此：

$$
\boxed{
\Omega_c(\gamma)\neq0.
}
$$

這正是：

$$
[c]\neq0
$$

在該基本 cycle 上的可見殘餘。

所以 Paper 02 的「不能全域消掉」可以在這個例子裡直接讀成：

> 繞完整個局部脈絡環後，回到起點卻留下 $1$。

---

# 17. Holonomy 和 $H^1$ 不是一般情況下同一物

這裡必須再次劃界。

一般：

$$
\boxed{
\text{holonomy}
\neq
H^1.
}
$$

原因包括：

1. holonomy 可以是非阿貝爾群值；
2. $H^1$ 可能使用不同係數；
3. holonomy 通常依賴 connection／transport；
4. cohomology 描述等價類與阻塞；
5. 高維結構還可能需要更高 cohomology。

因此本文只主張：

> 在阿貝爾、1-dimensional nerve／flat transition 等適當 régime 下，cycle pairing 提供 $H^1$ 類與閉路 transport residue 的直接接口。

不把此接口偷渡成普遍等同。

---

# 18. 觀察者加入：Holonomy 存在不代表觀察者看得到

Paper 03 定義觀察者存取映射：

$$
A_{O,x}:
\mathcal F_x
\to
\mathcal D_O.
$$

閉路之後：

$$
v
\mapsto
H_x(\gamma)v.
$$

觀察者看到：

$$
A_{O,x}(v)
$$

和：

$$
A_{O,x}(H_x(\gamma)v).
$$

---

## 定義 18.1（對觀察者不可見 holonomy）

若：

$$
A_{O,x}\circ H_x(\gamma)
=
A_{O,x},
$$

則稱 $\gamma$ 的 holonomy 對 $O$ **不可見**。

---

## 定義 18.2（對觀察者可見 holonomy）

若存在：

$$
v\in\mathcal F_x
$$

使：

$$
A_{O,x}(H_x(\gamma)v)
\neq
A_{O,x}(v),
$$

則稱 holonomy 對 $O$ **可見**。

---

# 19. 第二主區分：存在的記憶 vs 可觀察的記憶

因此：

$$
H_x(\gamma)\neq I
$$

只說明纖維 transport 具有非平凡閉路效應。

但：

$$
A_{O,x}\circ H_x(\gamma)
=
A_{O,x}
$$

可能仍使該效應完全落在觀察者 kernel 裡。

所以：

$$
\boxed{
\text{relational memory exists}
\not\Rightarrow
\text{observer detects it}.
}
$$

這和 Paper 03 的基本紀律完全平行：

$$
\boxed{
\text{global exists}
\not\Rightarrow
\text{observer accesses it}.
}
$$

Series B 的 observer layer 因此再次阻止我們從結構存在直接跳到經驗可見。

---

# 20. Kernel 形式

若 $A_O$ 為線性，則閉路對 $O$ 不可見的條件可以寫成：

$$
A_O(H-I)=0.
$$

也就是：

$$
\operatorname{im}(H-I)
\subseteq
\ker A_O.
$$

因此：

> holonomy 所改變的所有方向，都落在觀察者無法分辨的自由度裡。

這提供一個非常具體的 observer-relative invisibility 判準。

---

# 21. 多觀察者可以共同看見單人看不到的 holonomy

定義聯合觀察：

$$
A_{\mathcal O}
=
\prod_{O\in\mathcal O}A_O.
$$

可能每一個：

$$
A_O(H-I)
$$

都只能看見一部分效應，

但：

$$
A_{\mathcal O}(H-I)
$$

足以區分完整 holonomy。

因此：

$$
\boxed{
\text{individual holonomy blindness}
\not\Rightarrow
\text{collective holonomy blindness}.
}
$$

這是 Paper 03 「聯合觀察完備」在動態閉路上的版本。

---

# 22. 觀察者自身也可以被 transport

更一般情況下，觀察者不是固定在纖維外面讀數。

觀察者本身沿路徑移動。

此時應同時 transport：

$$
v_O
\in
\mathcal O_x.
$$

令觀察者 frame transport：

$$
S_\gamma:
\mathcal O_x
\to
\mathcal O_y.
$$

那麼「走一圈後觀察到的差」取決於：

$$
H_x^{\mathrm{system}}(\gamma)
$$

與：

$$
H_x^{\mathrm{observer}}(\gamma)
$$

的相對作用。

如果兩者同步變換：

$$
H^{\mathrm{system}}
=
H^{\mathrm{observer}},
$$

觀察者可能感覺「什麼都沒有變」。

所以真正的 observable holonomy 可能是**相對 holonomy**，而不是單獨的系統 holonomy。

本文只提出接口，不在此完成 observer-transport theory；這將是 Paper 05 的主題。

---

# 23. 關係記憶的四階分類

本文暫定四階。

## M0：閉路平凡

$$
H(\gamma)=I.
$$

無閉路關係記憶。

---

## M1：Holonomy 非平凡但 gauge-equivalent 表示可變

$$
H(\gamma)\neq I,
$$

但只討論單一 frame 中的 $H$，尚未抽取 invariant。

---

## M2：Gauge-stable 關係記憶

存在：

$$
\mathcal I(H)\neq\mathcal I(I)
$$

且 $\mathcal I$ 對合法 frame transformation 不變。

---

## M3：Observer-visible 關係記憶

除 M2 外，還存在觀察者 $O$ 使：

$$
A_O\circ H
\neq
A_O.
$$

因此：

$$
\boxed{
\text{structural memory}
}
$$

與：

$$
\boxed{
\text{observable memory}
}
$$

再次被分離。

---

# 24. Flatness 的 Series B 讀法

如果一個區域內所有 contractible closed loops 都有：

$$
H(\gamma)=I,
$$

在適當 connection 條件下，這對應局部 flatness。

Series B 的讀法是：

> 在該區域內，局部路徑歷史不會留下可由 transport 偵測的閉路殘餘。

但不要把 flatness 理解成：

> 世界沒有任何歷史。

它只表示：

$$
\boxed{
\text{這一個 transport 結構不記錄這些閉路歷史。}
}
$$

更高層、不同係數或不同觀察通道仍可能保存其他資訊。

---

# 25. 與「守恆」第一次真正接觸

設：

$$
Q_x:
\mathcal F_x
\to V
$$

為候選局部量。

若希望 $Q$ 沿 transport 守恆，應要求：

$$
\boxed{
Q_y(T_\gamma v)
=
Q_x(v)
}
$$

對合法路徑 $\gamma:x\to y$ 成立。

對閉路：

$$
\gamma:x\to x,
$$

則：

$$
Q_x(H_x(\gamma)v)
=
Q_x(v).
$$

因此一個量可以在：

$$
H(\gamma)\neq I
$$

時仍然守恆。

也就是：

$$
\boxed{
\text{state changes around a loop}
\not\Rightarrow
\text{every invariant changes}.
}
$$

這一點對 Series B 後面的「全域守恆」極為重要。

---

# 26. Holonomy 群與守恆量

固定基點 $x$，所有閉路 holonomy 形成：

$$
\operatorname{Hol}_x
\subseteq
\operatorname{Aut}(\mathcal F_x).
$$

若：

$$
Q_x
$$

對所有：

$$
H\in\operatorname{Hol}_x
$$

都不變：

$$
Q_x(Hv)=Q_x(v),
$$

則 $Q_x$ 是 holonomy 群作用下的不變量。

所以未來守恆問題可以被改寫成：

$$
\boxed{
\text{尋找 transport / holonomy action 的 invariants}.
}
$$

這比單純寫：

$$
Q(t)=\text{constant}
$$

更適合 observer-local framework。

---

# 27. 一個重要可能性：狀態不閉合，但 invariant 閉合

可能：

$$
H(\gamma)\neq I,
$$

但：

$$
Q\circ H(\gamma)=Q.
$$

這表示：

$$
\boxed{
\text{關係狀態有記憶}
}
$$

但：

$$
\boxed{
\text{某個量沒有記憶}.
}
$$

因此：

> 非交換、holonomy、歷史依賴，都不自動推出「不守恆」。

這一句必須在真正進入宇宙守恆命題之前先釘死。

---

# 28. 反方向：有路徑獨立 invariant，不代表完整 state 路徑獨立

即使：

$$
Q(T_{\gamma_1}v)
=
Q(T_{\gamma_2}v)
$$

對同起終點路徑成立，

仍可能：

$$
T_{\gamma_1}v
\neq
T_{\gamma_2}v.
$$

因此：

$$
\boxed{
\text{invariant path-independence}
\not\Rightarrow
\text{state path-independence}.
}
$$

這將在守恆階層中形成一條重要分類軸。

---

# 29. Series B 前四篇現在形成一條完整鏈

## Paper 01

$$
\boxed{
\text{順序是否改變終態／合法性？}
}
$$

核心：

$$
\delta,\Delta.
$$

---

## Paper 02

$$
\boxed{
\text{局部差能否形成不可消去全域阻塞？}
}
$$

核心：

$$
c,[c]\in H^1.
$$

---

## Paper 03

$$
\boxed{
\text{global 是否存在？存在時 observer 能否取得？}
}
$$

核心：

$$
\mathcal G,
A_O,R_O.
$$

---

## Paper 04

$$
\boxed{
\text{observer / state 沿路徑 transport 後，閉路會留下什麼？}
}
$$

核心：

$$
T_\gamma,
H(\gamma),
M(\gamma).
$$

因此四篇的共同主線已可寫成：

$$
\boxed{
\text{order}
\rightarrow
\text{gluing}
\rightarrow
\text{access}
\rightarrow
\text{transport}.
}
$$

---

# 30. 下一個必然問題：不同觀察者的 transport 如何比較

Paper 04 已留下：

$$
A_{O,x}
$$

以及可能的 observer transport：

$$
S_\gamma.
$$

下一篇真正要問：

給定兩個觀察者：

$$
O,P,
$$

是否存在合法轉換：

$$
F_{O\to P}
$$

使：

$$
\boxed{
F_{O\to P,y}
\circ
T^O_\gamma
=
T^P_\gamma
\circ
F_{O\to P,x}.
}
$$

如果交換圖成立，兩觀察者的 transport 描述是 compatible / covariant。

如果不成立，就會出現新的：

$$
\boxed{
\text{observer-transport defect}.
}
$$

這將是 Series B / Paper 05。

---

# 31. 本文的禁止推論

本文正式禁止以下推論：

## 禁止一

$$
H(\gamma)\neq I
\Rightarrow
\text{全域截面不存在}.
$$

不成立。

---

## 禁止二

$$
H(\gamma)\neq I
\Rightarrow
\text{所有守恆量都破壞}.
$$

不成立。

---

## 禁止三

$$
H(\gamma)\neq I
\Rightarrow
\text{觀察者一定看得到}.
$$

不成立。

---

## 禁止四

$$
[c]\neq0
\Longleftrightarrow
H(\gamma)\neq I
$$

一般情形不成立；只在明確係數、transport 與 cycle pairing 條件下建立接口。

這四條是後續進守恆論之前的重要紀律。

---

# 32. 結論

本文把 Series B 從靜態的「局部／全域」推進到真正的路徑動力學。

核心對象為：

$$
\boxed{
T_\gamma:
\mathcal F_x
\to
\mathcal F_y.
}
$$

閉路：

$$
\gamma:x\to x
$$

則產生：

$$
\boxed{
H_x(\gamma)
=
T_\gamma.
}
$$

若：

$$
H_x(\gamma)\neq I,
$$

則「返回同一位置」不等於「返回同一關係狀態」。

本文將此解讀為關係記憶，但真正可比較的記憶必須取 gauge-stable invariant。

本文得到三條主要橋接結果：

第一，

$$
\boxed{
\text{all loop holonomies trivial}
\Longleftrightarrow
\text{endpoint transport path-independent}
}
$$

在可逆、路徑連通的基本條件下成立。

第二，Paper 01 的交換子可以被視為無窮小交換閉路 holonomy 的首階生成量：

$$
\log
\left(
e^Xe^Ye^{-X}e^{-Y}
\right)
=
[X,Y]+O(3).
$$

第三，在 Paper 02 的阿貝爾 1-cocycle régime 中，

$$
\Omega_c(\gamma)
=
\sum_\gamma c_{ij}
$$

對 coboundary 變換不變，因此 cohomology class 可以透過 cycle pairing 表現成閉路關係殘餘。

最後，加入 Paper 03 的觀察映射後：

$$
\boxed{
H\neq I
}
$$

仍不等於：

$$
\boxed{
A_O\circ H\neq A_O.
}
$$

所以 Series B 到此已經形成一個非常清楚的多層結構：

$$
\boxed{
\text{關係會留下歷史}
}
$$

與：

$$
\boxed{
\text{觀察者能否看到這段歷史}
}
$$

是兩個不同問題。

而真正的守恆問題，現在才第一次有了足夠清楚的數學語言可以開始問：

> 即使完整關係狀態沿閉路發生非平凡 holonomy，是否仍存在某些量、某些關係律、或某些觀察者間可比較的 invariant，在所有合法 transport 下保持不變？

Series B 將在後續論文逐步回答這個問題。

---

## 參考文獻與既有工作

1. EveMissLab, **EML-OO-2026-DPE-v0.1**, *過程即存在：對話算子、回合映射與 agent 的本體論*, 2026-06-15.
2. EveMissLab, **EML-OO-2026-NSF-v0.2**, *關係先於物件：不可分數學的三根支柱與對話算子的上同調升級*, 2026-06-15.
3. EveMissLab, **EML-OO-2026-CONV-v0.1**, *殊途同歸：信息守恆封閉宇宙下「不可分數學」與「閉合性理論」的收斂猜想*, 2026-06-15.
4. S. Kobayashi and K. Nomizu, *Foundations of Differential Geometry*, Vol. I.
5. M. Nakahara, *Geometry, Topology and Physics*.
6. R. Bott and L. W. Tu, *Differential Forms in Algebraic Topology*.
7. S. Abramsky and A. Brandenburger, *The Sheaf-Theoretic Structure of Non-Locality and Contextuality*, New Journal of Physics 13 (2011).
8. C. A. Rossi, *Principal bundles with groupoid structure: local vs. global theory and nonabelian Čech cohomology*, arXiv:math/0404449.

---

**系列定位：** Series B / Paper 04  
**下一篇：** *觀察者轉換與關係協變性：跨觀察者 transport、交換圖與相對 Holonomy*
