# RSCT 05｜真與假的非原子性：關係極致張力的邊界語義

**系列**：關係語義構成論（Relational Semantic Construction Theory, RSCT）05  
**英文題名**：*The Non-Atomicity of Truth and Falsity: Boundary Semantics of Extremal Relational Tension*  
**作者**：Neo.K × GPT-5.6 Sol  
**機構**：EveMissLab（一言諾科技有限公司）  
**日期**：2026-08-27  
**版本**：v0.1  
**性質**：形式語義學／真值本體論／關係語義學／張力邊界理論／型別化評價  
**狀態**：系列正式初稿  
**前篇**：RSCT 04｜《關係張力態空間與邊界生成》

---

## 摘要

RSCT 00–04 已依序建立五個前置結構：異質語義型別、語義構造、結構作用性、雙向關係與生成式反身性，以及關係張力態空間與邊界生成。本篇首次正面處理本系列的核心問題之一：

> 真與假是否必須被視為不可再分析的 primitive truth values？

傳統二值形式常直接使用：

$$
V(P)\in\{T,F\}.
$$

此表示在大量封閉推理中極其有效，但它不回答：

> 為什麼恰好是 $T$ 與 $F$？  
> 它們是世界的最底層狀態、命題的內在性質、評價結果，還是某種更高維關係結構經投影後的極端標籤？

本文提出「邊界真值假說」（Boundary Truth Hypothesis, BTH）。其最低形式為：

$$
R
\xrightarrow{\Theta}
\mathcal T_R
\xrightarrow{\operatorname{Ext}}
\mathcal E_R
\xrightarrow{\pi_V}
\mathcal V,
$$

其中：

- $R$：待評價對象與參照結構之間的關係；
- $\Theta$：關係張力抽取；
- $\mathcal T_R$：關係張力態空間；
- $\operatorname{Ext}$：極端／邊界選取；
- $\mathcal E_R$：與某一評價方向相關的極端集合；
- $\pi_V$：真值標籤投影；
- $\mathcal V$：評價輸出空間。

在最簡一維情況：

$$
\mathcal T_R=[-1,1],
$$

若某評價方向已固定，可以暫定：

$$
\pi_V(+1)=T,
$$

$$
\pi_V(-1)=F.
$$

但本文拒絕把此一維模型提升成普遍本體。高維情況下：

$$
\mathcal T_R\subseteq\mathbb R^n
$$

或更一般：

$$
\mathcal T_R
=
\prod_{\alpha\in A}T_\alpha,
$$

真與假若仍要被壓成二值，就必須透過額外的評價方向、投影函數、觀察位置與判定條件完成。由此本文提出：

$$
\boxed{
T,F
\text{ 可以被視為關係張力空間之方向性極端邊界的低維語義標籤。}
}
$$

此句不是宣稱所有真值理論都應被取代，而是提出一個比「 $T$ 與 $F$ 是原子」更底層的可分析模型。

本文進一步區分：

$$
\text{Orientation}
\neq
\text{Negation}
\neq
\text{Evidence Polarity}
\neq
\text{Truth Polarity}.
$$

正向／反向只表示關係方向；否定是對命題或語義內容的算子；支持／反證是認識論證據軸；真／假則是特定評價關係下的邊界標籤。它們可以建立映射，但不能直接同一化。

本文同時提出「真值載體」「評價關係」「參照域」「極端選取」「真值投影」五層，並將經典形式：

$$
V(P)=T
$$

重寫成：

$$
\pi_V
\left(
\operatorname{Ext}_{\ell,o,c}
\left(
\Theta
\left(
R(P,\mathcal D\mid o,c)
\right)
\right)
\right)
=
T.
$$

此式不是要求實務推理都使用完整高維形式，而是揭示二值結果背後可能被壓縮的生成結構。

本篇最後建立一個重要限制：真與假若是邊界語義，不代表所有中間態都是「半真半假」，也不代表所有邊界都是真／假。真值投影只是眾多可能邊界投影中的一種。RSCT 05 因此不取代四態、支持／反證雙軸、模糊邏輯、多值邏輯或無限潛能場統一理論，而是為它們提供一個更底層的關係—張力—邊界接口。

下一篇 RSCT 06 將把此模型帶回說謊者悖論，檢查：

$$
L\leftrightarrow\neg L
$$

是否把「假」作為語義對象、「假」作為評價標籤、方向交換、否定、反身回返與命題同一化等不同結構錯誤壓成同一個符號。

**關鍵詞**：真、假、真值、邊界語義、關係張力、極致、非原子真值、評價投影、高維語義、說謊者悖論、關係語義構成論

---

# 0. 問題：真與假為什麼會被當成最底層？

經典命題邏輯常寫：

$$
V(P)\in\{T,F\}.
$$

在形式系統中，這非常自然。

因為一旦：

$$
T
$$

與：

$$
F
$$

被定義為 primitive values，後續就可以建立：

$$
\neg,
\land,
\lor,
\rightarrow,
\leftrightarrow.
$$

問題是：

> 形式上把它們當 primitive，是否等於本體上它們真的不可再分析？

本文回答：

$$
\boxed{
\text{Formal Primitive}
\not\Rightarrow
\text{Ontological Primitive}.
}
$$

一個值可以在某個形式系統裡作為 primitive interface，但在更底層模型中仍然有生成結構。

---

# 1. 真值原子化

若系統直接寫：

$$
P\mapsto T
$$

或：

$$
P\mapsto F,
$$

中間的：

- 參照；
- 關係；
- 比較；
- 評價；
- 邊界；
- 投影；

全部被隱藏。

本文將這種表示稱為：

$$
\boxed{
\text{Truth-Value Atomization}.
}
$$

它不是錯誤。

它是一種壓縮。

真正的問題是：

$$
\boxed{
\text{壓縮結果是否被誤認為完整生成機制？}
}
$$

---

# 2. 真值至少需要一個關係

考慮命題：

> 雪是白的。

若要判定真值，至少要有：

$$
P
$$

與某個參照域：

$$
\mathcal D.
$$

因此更完整的評價不應只寫：

$$
V(P),
$$

而可寫：

$$
V
(
P,\mathcal D
).
$$

若加入觀察者與語境：

$$
V
(
P,\mathcal D\mid o,c
).
$$

所以：

$$
\boxed{
\text{Truth Evaluation}
\text{ is relational before it is scalar}.
}
$$

---

# 3. 真值載體與評價結果必須分開

令：

$$
P:\mathsf{Proposition}
$$

為真值載體候選。

令：

$$
V(P)
$$

為評價結果。

則：

$$
P
\neq
V(P).
$$

所以：

$$
\boxed{
\text{Truth Bearer}
\neq
\text{Truth Value}.
}
$$

這個區分對說謊者悖論極重要。

因為：

> 「假」

可以被提及為語義內容，

但：

> 整句被判定為假

則是另一個型別。

---

# 4. 評價不是被動讀取屬性

傳統直覺常像：

$$
P
\text{ 裡面本來就藏著 }T/F.
$$

而評價只是讀出來。

RSCT 提出另一種可能：

$$
\boxed{
\text{Evaluation}
\text{ may construct a relation to a reference domain}.
}
$$

也就是：

$$
R_{\mathrm{eval}}
(
P,\mathcal D
).
$$

真值因此可以是：

> 命題內容與參照域在某個評價條件下的關係結果。

---

# 5. 評價關係進入張力態空間

依 RSCT 04：

$$
R
\xrightarrow{\Theta}
\mathcal T_R.
$$

所以對評價關係可寫：

$$
R_{\mathrm{eval}}
(
P,\mathcal D\mid o,c
)
\xrightarrow{\Theta}
\tau_P.
$$

其中：

$$
\tau_P
\in
\mathcal T_{\mathrm{eval}}.
$$

因此：

$$
\boxed{
\text{Truth Evaluation}
\text{ can be modeled as a tension-state assignment}.
}
$$

但：

$$
\tau_P
$$

本身還不是 $T/F$。

---

# 6. 真／假不是任意張力態

若：

$$
\tau_P
\in
\mathcal T_{\mathrm{eval}},
$$

一般中間位置不必被叫做：

$$
T
$$

或：

$$
F.
$$

真／假若被理解為極端語義，至少要經過：

$$
\operatorname{Ext}
:
\mathcal T_{\mathrm{eval}}
\rightarrow
\mathcal E_{\mathrm{eval}}.
$$

所以：

$$
\boxed{
T,F
\text{ 不對應任意 tension state，而只可能對應某類極端／邊界狀態。}
}
$$

---

# 7. 邊界真值假說

本文正式提出：

## 假說 BTH：Boundary Truth Hypothesis

存在某些評價結構，使：

$$
\mathcal E_{\mathrm{eval}}
\subseteq
\mathfrak B
(
\mathcal T_{\mathrm{eval}}
),
$$

並存在：

$$
\pi_V:
\mathcal E_{\mathrm{eval}}
\rightarrow
\mathcal V.
$$

在二值投影下：

$$
\mathcal V
=
\{T,F\}.
$$

因此：

$$
\boxed{
\{T,F\}
=
\pi_V
\left(
\mathcal E_{\mathrm{eval}}
\right)
}
$$

可以作為一類真值模型。

注意：

$$
\boxed{
\text{BTH 是模型假說，不是已證普遍定律。}
}
$$

---

# 8. 最簡一維模型

令：

$$
\mathcal T_{\mathrm{eval}}
=
[-1,1].
$$

定義方向性評價：

$$
\ell:
\mathcal T_{\mathrm{eval}}
\rightarrow
[-1,1].
$$

在最簡情況可令：

$$
\ell(\tau)=\tau.
$$

然後：

$$
\pi_V(+1)=T,
$$

$$
\pi_V(-1)=F.
$$

則：

$$
\boxed{
T
=
\text{positive extremal label},
}
$$

$$
\boxed{
F
=
\text{negative extremal label}.
}
$$

這是「真與假為關係極致張力」最簡潔的形式版本。

---

# 9. 真與假首先是同一關係軸的兩個極端

在一維模型中：

$$
T
$$

與：

$$
F
$$

不是兩個互不相關的原子。

而是：

$$
\boxed{
\text{同一評價關係空間的兩個相反極端。}
}
$$

即：

$$
T
\sim
\partial_+
\mathcal T_{\mathrm{eval}},
$$

$$
F
\sim
\partial_-
\mathcal T_{\mathrm{eval}}.
$$

這就是本系列目前最精確的：

$$
\boxed{
\text{真／假＝關係的極致張力}
}
$$

之低維版本。

---

# 10. 「張力」與「方向」可以分離

若：

$$
\tau
=
\sigma\lambda,
$$

其中：

$$
\sigma\in\{-1,+1\},
$$

而：

$$
\lambda\in[0,1],
$$

則：

$$
\sigma
$$

表示方向，

$$
\lambda
$$

表示強度。

所以：

$$
T
\sim
(+1,1),
$$

$$
F
\sim
(-1,1).
$$

這表示真／假可以被理解為：

$$
\boxed{
\text{最大張力}
+
\text{相反方向}.
}
$$

---

# 11. 方向正反不等於真／假

RSCT 03 已區分：

$$
r_+,
\quad
r_-.
$$

這只是關係方向。

所以：

$$
\boxed{
r_+
\neq
T,
}
$$

$$
\boxed{
r_-
\neq
F.
}
$$

只有當：

$$
r_+,
r_-
$$

進入某個特定評價關係、張力空間與投影後，才可能得到：

$$
T/F.
$$

因此：

$$
\boxed{
\text{Orientation}
\neq
\text{Truth Polarity}.
}
$$

---

# 12. 否定也不等於反向

邏輯否定：

$$
\neg P
$$

是語義／邏輯算子。

方向交換：

$$
\mathcal J
:
(r_+,r_-)
\mapsto
(r_-,r_+)
$$

是結構交換。

所以：

$$
\boxed{
\neg
\neq
\mathcal J.
}
$$

若某模型讓：

$$
\neg
$$

對應到方向反轉，必須額外證明或定義該映射。

---

# 13. 支持／反證也不等於真／假

四態研究中：

$$
\nu_4(P)
=
(s,r)
$$

表示支持與反證。

其中：

$$
s=1
$$

不等於：

$$
P=T.
$$

而：

$$
r=1
$$

也不等於：

$$
P=F.
$$

支持與反證屬於：

$$
\mathsf{EpistemicEvidence}.
$$

而真／假屬於：

$$
\mathsf{EvaluationLabel}.
$$

所以：

$$
\boxed{
\text{Evidence Polarity}
\neq
\text{Truth Polarity}.
}
$$

---

# 14. 四個容易混淆的正反結構

本文正式區分：

$$
\boxed{
\text{Directional Polarity}
}
$$

$$
\boxed{
\text{Logical Negation}
}
$$

$$
\boxed{
\text{Evidence Polarity}
}
$$

$$
\boxed{
\text{Truth Polarity}
}
$$

它們都可能呈現：

$$
+/-,
$$

但型別不同。

這是 RSCT 06 分析說謊者悖論的核心防錯條件。

---

# 15. 高維情況下，真／假不是天然兩個點

若：

$$
\mathcal T_{\mathrm{eval}}
=
[-1,1]^n,
$$

則：

$$
\partial
\mathcal T_{\mathrm{eval}}
$$

包含大量邊界點。

因此不存在天然唯一：

$$
+1,
\quad
-1
$$

可直接叫作：

$$
T,
\quad
F.
$$

需要再指定：

$$
\ell:
\mathcal T_{\mathrm{eval}}
\rightarrow
\mathbb R.
$$

---

# 16. 評價方向

定義：

$$
\ell
$$

為評價方向或評價函數。

則：

$$
\ell(\tau)
$$

把高維張力態投影到一條可排序方向。

真值極端可以相對於：

$$
\ell
$$

定義：

$$
\mathcal E_T
=
\operatorname*{arg\,max}_{\tau\in\mathcal T_{\mathrm{eval}}}
\ell(\tau),
$$

$$
\mathcal E_F
=
\operatorname*{arg\,min}_{\tau\in\mathcal T_{\mathrm{eval}}}
\ell(\tau).
$$

因此：

$$
\boxed{
T
\text{ 與 }
F
\text{ 是相對於評價方向的極端。}
}
$$

---

# 17. 真與假可以是一整個邊界面

若：

$$
\ell(\tau_1,\tau_2)=\tau_1,
$$

且：

$$
\mathcal T_{\mathrm{eval}}
=
[-1,1]^2,
$$

則：

$$
\mathcal E_T
=
\{1\}\times[-1,1],
$$

而：

$$
\mathcal E_F
=
\{-1\}\times[-1,1].
$$

因此：

$$
\boxed{
\text{Truth/Falsity extremality need not be point-valued}.
}
$$

真與假可以是整個邊界族經標籤壓縮後的結果。

---

# 18. 真值標籤可以是等價類

如果：

$$
\pi_V(\tau)=T
$$

對所有：

$$
\tau\in\mathcal E_T
$$

成立，

則：

$$
T
$$

實際上代表：

$$
[\mathcal E_T]_{\pi_V}.
$$

同理：

$$
F
=
[\mathcal E_F]_{\pi_V}.
$$

所以：

$$
\boxed{
\text{Truth Value}
\text{ can be an equivalence-class label}.
}
$$

這提供「二值如何壓縮高維邊界」的形式解釋。

---

# 19. 真值投影是有損的

若：

$$
\tau_1\neq\tau_2,
$$

但：

$$
\pi_V(\tau_1)
=
\pi_V(\tau_2)
=
T,
$$

則：

$$
\pi_V
$$

不是單射。

因此：

$$
\boxed{
\text{Truth Projection}
\text{ can be lossy}.
}
$$

這與前置「世界到型別錯誤」中的投影不可逆限制一致。

---

# 20. 真值有損不代表真值無用

二值判定：

$$
T/F
$$

可以非常有效。

例如安全檢查可能只需要：

$$
\text{pass/fail}.
$$

資料庫約束可能只需要：

$$
\text{satisfied/violated}.
$$

所以：

$$
\boxed{
\text{Lossy}
\not\Rightarrow
\text{Invalid}.
}
$$

真正的要求是：

> 系統必須知道自己正在投影。

---

# 21. Primitive-like interface

即使底層：

$$
T,F
$$

不是本體 primitive，

在高階形式系統中仍可以把它們當作：

$$
\boxed{
\text{primitive-like interface}.
}
$$

即：

> 為了推理效率而停止繼續展開。

所以：

$$
\boxed{
\text{Non-Atomic Ontology}
\not\Rightarrow
\text{No Binary Logic}.
}
$$

---

# 22. 中間態不是「半真半假」

如果：

$$
\tau
$$

不在：

$$
\mathcal E_T
$$

或：

$$
\mathcal E_F,
$$

不能自動稱：

$$
\tau
$$

為：

> 半真半假。

它可能是：

- 未定；
- 未充分對齊；
- 高維衝突；
- 不可比較；
- 未觀察；
- 尚未投影；
- 屬於另一個評價維度。

因此：

$$
\boxed{
\text{Non-Extreme}
\neq
\text{Half-True}.
}
$$

---

# 23. 邊界也不一定只有真與假

一個邊界可能有：

$$
\mathcal E_1,
\mathcal E_2,
\ldots,
\mathcal E_k.
$$

只有其中某些被：

$$
\pi_V
$$

映射為：

$$
T/F.
$$

所以：

$$
\boxed{
\text{Boundary Richness}
>
\text{Truth Label Richness}
}
$$

在一般情況下是可能的。

---

# 24. 真／假與模糊真值的關係

模糊邏輯可能使用：

$$
v(P)\in[0,1].
$$

RSCT 不把：

$$
[0,1]
$$

直接等同於張力空間。

模糊值可以是：

$$
\mu:
\mathcal T_{\mathrm{eval}}
\rightarrow
[0,1]
$$

的投影結果。

所以：

$$
\boxed{
\text{Fuzzy Value}
\text{ can be a measure on tension space rather than the space itself}.
}
$$

---

# 25. 真／假與多值邏輯的關係

若：

$$
\mathcal V
=
\{v_1,\ldots,v_n\},
$$

則可以理解為：

$$
\pi_n:
\mathcal T_{\mathrm{eval}}
\rightarrow
\mathcal V.
$$

所以多值邏輯可以被視為：

> 使用更多離散標籤對張力／評價空間做更細投影。

但這不是所有多值邏輯的唯一解釋。

---

# 26. 真／假與四態的關係

四態：

$$
\mathbf U,
\mathbf Y,
\mathbf N,
\mathbf B
$$

首先是證據狀態。

因此可能存在：

$$
\pi_4:
\mathcal E_{\mathrm{evidence}}
\rightarrow
\mathbb Q_4.
$$

而 RSCT 05 的真值映射則是：

$$
\pi_V:
\mathcal E_{\mathrm{eval}}
\rightarrow
\{T,F\}.
$$

所以：

$$
\boxed{
\pi_4
\neq
\pi_V.
}
$$

即使兩者都從高維空間投影。

---

# 27. 真／假與無限潛能場統一理論的關係

無限潛能場統一理論處理更高維、開放、可展開的潛能／狀態母體。

RSCT 不宣稱：

$$
\mathcal T_{\mathrm{eval}}
=
\mathcal U_{\mathrm{IPF}}.
$$

更保守地，只建立可能接口：

$$
\mathcal U_{\mathrm{IPF}}
\xrightarrow{\Pi_{\mathrm{rel}}}
\mathcal T_{\mathrm{eval}}
\xrightarrow{\pi_V}
\mathcal V.
$$

因此：

$$
\boxed{
\text{Infinite Potential Field}
\neq
\text{Truth Space}.
}
$$

---

# 28. 真值生成的五層模型

本文正式提出：

## 第一層：真值載體

$$
P:\mathsf{TruthBearer}.
$$

## 第二層：參照關係

$$
R_{\mathrm{eval}}
(
P,\mathcal D
\mid o,c
).
$$

## 第三層：張力態

$$
\tau_P
=
\Theta
\left(
R_{\mathrm{eval}}
(
P,\mathcal D
\mid o,c
)
\right).
$$

## 第四層：極端選取

$$
\tau_P
\in
\mathcal E_T
\quad\text{or}\quad
\tau_P
\in
\mathcal E_F.
$$

## 第五層：真值投影

$$
\pi_V(\tau_P)
=
T
$$

或：

$$
\pi_V(\tau_P)
=
F.
$$

因此：

$$
\boxed{
\text{Truth Value}
\text{ is the endpoint of an evaluation construction chain}.
}
$$

---

# 29. 經典式子的展開

傳統：

$$
V(P)=T
$$

可以展開成：

$$
\pi_V
\left(
\operatorname{Ext}_{\ell,o,c}
\left(
\Theta
\left(
R_{\mathrm{eval}}
(
P,\mathcal D
\mid o,c
)
\right)
\right)
\right)
=
T.
$$

這不是要求所有推理都使用長式子。

它只是揭示：

$$
V(P)=T
$$

可能是高度壓縮表示。

---

# 30. 真值不是命題內部的靜態貼紙

在此模型下：

$$
T
$$

與：

$$
F
$$

不是貼在 $P$ 身上的不可分析性質。

而是：

$$
\boxed{
P
\text{ 與某參照域形成評價關係後的極端投影結果。}
}
$$

因此真值具有關係性。

---

# 31. 關係性不等於任意相對主義

如果：

$$
V(P\mid o,c)
$$

依賴：

$$
o,c,
$$

不代表任何觀察者都能任意決定真值。

因為：

$$
R_{\mathrm{eval}}
$$

仍受到：

- 世界狀態；
- 證據；
- 語義；
- 型別；
- 參照域；
- 評價規則；

約束。

所以：

$$
\boxed{
\text{Relational}
\neq
\text{Arbitrary}.
}
$$

---

# 32. 真值與完全一致

在最簡模型中，「真」可以理解為：

> 命題內容與參照域在選定評價方向上達到最大正向一致。

寫作：

$$
\ell(\tau_P)
=
\sup
\ell
(
\mathcal T_{\mathrm{eval}}
).
$$

而「假」為：

$$
\ell(\tau_P)
=
\inf
\ell
(
\mathcal T_{\mathrm{eval}}
).
$$

所以：

$$
\boxed{
\text{Truth/Falsity}
\text{ can be modeled as extremal relational alignment}.
}
$$

---

# 33. 「一致」也不能當 primitive

若：

$$
\operatorname{Align}(P,\mathcal D)
$$

本身又是複合關係，

則仍可繼續拆：

- 對象一致；
- 屬性一致；
- 時間一致；
- 條件一致；
- 範圍一致；
- 型別一致；
- 因果一致。

所以：

$$
\boxed{
\text{Alignment}
\text{ may itself be high-dimensional}.
}
$$

這正是為什麼真／假不必只有單一底層尺度。

---

# 34. 真值可以是局部完備而全域未完備

假設：

$$
P
$$

只描述：

$$
\mathcal D_1.
$$

對：

$$
\mathcal D_1
$$

可能有：

$$
V(P)=T.
$$

但在更大參照域：

$$
\mathcal D_2
\supset
\mathcal D_1
$$

中，仍可能出現其他未包含條件。

因此：

$$
\boxed{
\text{Local Extremality}
\neq
\text{Global Exhaustiveness}.
}
$$

這使「真」與「全知」正式分開。

---

# 35. 真值極端與穩定性

如果一個命題達到：

$$
T
$$

但加入極小擾動：

$$
\epsilon
$$

便立即離開：

$$
\mathcal E_T,
$$

則其真值邊界可能非常脆弱。

因此可進一步定義：

$$
\operatorname{Robust}_T(P).
$$

這表示：

> 真值極端附近是否存在穩定鄰域。

所以：

$$
\boxed{
\text{Truth}
\neq
\text{Truth Robustness}.
}
$$

本篇只建立接口。

---

# 36. 真值與可判定性

即使存在：

$$
\mathcal E_T,
\quad
\mathcal E_F,
$$

一個有限評價器也未必能決定：

$$
\tau_P
\in
\mathcal E_T
$$

或：

$$
\tau_P
\in
\mathcal E_F.
$$

因此：

$$
\boxed{
\text{Truth Existence}
\neq
\text{Truth Decidability}.
}
$$

這將直接影響悖論與不可判定問題的分析。

---

# 37. 真值與語義可形成性

甚至在求值以前，命題可能尚未形成合法：

$$
P:\mathsf{TruthBearer}.
$$

如果語義構造失敗：

$$
\mathcal C(E)\uparrow,
$$

則：

$$
V(P)
$$

根本沒有合法輸入。

因此：

$$
\boxed{
\text{Semantic Well-Formedness}
\prec
\text{Truth Evaluation}.
}
$$

這再次呼應 RSCT 00–01。

---

# 38. 真值與型別錯誤

如果：

$$
F_{\mathrm{semantic}}
$$

是「假」這個被提及的語義對象，

而：

$$
F_{\mathrm{eval}}
$$

是整句評價結果，

則：

$$
F_{\mathrm{semantic}}
\neq
F_{\mathrm{eval}}.
$$

若直接同一化：

$$
F_{\mathrm{semantic}}
\equiv
F_{\mathrm{eval}},
$$

可能產生：

$$
\boxed{
\text{Truth-Type Collapse}.
}
$$

這將是 RSCT 06 的核心分析工具。

---

# 39. 真值與自我指涉

若：

$$
P
$$

的內容包含：

$$
V(P),
$$

則評價輸出重新進入評價輸入。

在 RSCT 05 的模型中，這不只是一個：

$$
P\leftrightarrow\neg P
$$

問題，

而可能是：

$$
P
\rightarrow
R_{\mathrm{eval}}
\rightarrow
\mathcal T_{\mathrm{eval}}
\rightarrow
\pi_V
\rightarrow
P.
$$

所以：

$$
\boxed{
\text{Self-Referential Truth}
\text{ can be a boundary feedback structure}.
}
$$

這是 RSCT 06 的直接接口。

---

# 40. 真值不是單純狀態，也可能是關係閉合結果

如果：

$$
V(P)
$$

只能在：

$$
P
$$

與：

$$
\mathcal D
$$

之間建立完整關係後得到，

則：

$$
T/F
$$

更接近：

$$
\boxed{
\text{evaluation closure labels}.
}
$$

即：

> 某個評價鏈閉合到極端邊界後的命名。

這使真值從「物件屬性」轉為「關係閉合」。

---

# 41. 核心定義收斂

## 定義 1：真值載體

$$
P:\mathsf{TruthBearer}.
$$

## 定義 2：評價關係

$$
R_{\mathrm{eval}}
(
P,\mathcal D\mid o,c
).
$$

## 定義 3：評價張力態

$$
\tau_P
=
\Theta
(
R_{\mathrm{eval}}
).
$$

## 定義 4：真極端集合

$$
\mathcal E_T
=
\operatorname*{arg\,max}
\ell.
$$

## 定義 5：假極端集合

$$
\mathcal E_F
=
\operatorname*{arg\,min}
\ell.
$$

## 定義 6：真值投影

$$
\pi_V:
\mathcal E_T\cup\mathcal E_F
\rightarrow
\{T,F\}.
$$

---

# 42. 核心命題

## 命題 1：真值非必然原子

$$
\boxed{
\text{Truth/Falsity}
\not\Rightarrow
\text{Ontological Primitive}.
}
$$

## 命題 2：真值先是關係結果

$$
\boxed{
\text{Truth Evaluation}
\text{ is relational before binary projection}.
}
$$

## 命題 3：真／假可作極端標籤

在 BTH 成立的模型中：

$$
\boxed{
T,F
=
\pi_V
(
\mathcal E_T,
\mathcal E_F
).
}
$$

## 命題 4：方向與真假不同型

$$
\boxed{
\text{Orientation Polarity}
\neq
\text{Truth Polarity}.
}
$$

## 命題 5：證據與真假不同型

$$
\boxed{
\text{Evidence State}
\neq
\text{Truth State}.
}
$$

## 命題 6：二值可以是合法但有損的接口

$$
\boxed{
\text{Binary Truth}
=
\text{Possible low-dimensional projection}.
}
$$

---

# 43. 可檢驗性與失敗條件

第一，如果真／假無法在任何非牽強模型中由關係極端、邊界或對齊結構生成，則 BTH 應被拒絕。

第二，如果所有高維邊界在真值分析中都沒有額外資訊價值，而：

$$
V(P)\in\{T,F\}
$$

已經完全足夠，則 RSCT 05 只具有哲學解釋力，而非計算必要性。

第三，如果：

$$
\mathcal E_T,
\mathcal E_F
$$

無法在不同語境中穩定定義，則「極端真值」模型需要改為局部或相對模型。

第四，如果「真／假是極致張力」導致把任何方向極端都誤標為真假，則模型失敗。方向極端只有在合法評價映射：

$$
\ell,
\quad
\pi_V
$$

存在時才有真值語義。

第五，若說謊者悖論在完整型別與邊界模型下仍完全等價於：

$$
L\leftrightarrow\neg L
$$

且沒有額外可區分結構，則 RSCT 對該悖論的解釋優勢會被削弱。

---

# 44. 與 RSCT 06 的接口

本篇已建立：

$$
P
\rightarrow
R_{\mathrm{eval}}
\rightarrow
\mathcal T_{\mathrm{eval}}
\rightarrow
\mathcal E
\rightarrow
\pi_V
\rightarrow
T/F.
$$

下一篇將把「這句話是假的」拆成：

$$
\mathsf{SentenceToken},
$$

$$
\mathsf{Reference},
$$

$$
\mathsf{PropositionalContent},
$$

$$
F_{\mathrm{semantic}},
$$

$$
R_{\mathrm{eval}},
$$

$$
F_{\mathrm{eval}},
$$

$$
\mathsf{Negation},
$$

$$
\mathsf{Return},
$$

$$
\mathsf{SelfMap}.
$$

並檢查傳統：

$$
L\leftrightarrow\neg L
$$

究竟在哪些步驟發生：

- 型別塌縮；
- 關係塌縮；
- 真值塌縮；
- 邊界塌縮；
- 自指同一化；
- 評價結果回灌。

因此下一篇為：

> **RSCT 06｜《說謊者悖論的關係語義重構：異質型別、反身邊界與投影錯誤》**

---

# 45. 結論

真與假可以在形式系統中被當作 primitive。

但這不迫使我們在更底層本體論中也把：

$$
T,
\quad
F
$$

視為不可再分析的原子。

RSCT 05 提出的替代模型是：

$$
\boxed{
\text{Truth Bearer}
\rightarrow
\text{Evaluation Relation}
\rightarrow
\text{Relational Tension}
\rightarrow
\text{Extremal Boundary}
\rightarrow
\text{Truth Projection}.
}
$$

在最簡一維模型中：

$$
\mathcal T_{\mathrm{eval}}
=
[-1,1],
$$

真與假可以被寫成：

$$
T
\sim
+1,
$$

$$
F
\sim
-1,
$$

但更精確地說，它們不是數字本身，而是：

$$
\boxed{
\text{同一評價關係空間在最大張力下的兩個相反方向性極端標籤。}
}
$$

在高維情況下：

$$
T
$$

與：

$$
F
$$

甚至可能各代表一整個極端邊界族，而不是單一點。

因此：

$$
\boxed{
\text{Truth/Falsity}
=
\text{Low-Dimensional Labels of Extremal Relational Evaluation}
}
$$

是本篇提出的核心工作假說。

這個模型最重要的價值，不是宣稱二值邏輯錯了，而是把：

$$
T/F
$$

從不可分析的終點，重新打開成：

$$
\boxed{
\text{關係}
\rightarrow
\text{張力}
\rightarrow
\text{極致}
\rightarrow
\text{邊界}
\rightarrow
\text{投影}.
}
$$

到這一步，本系列終於具備重新分析說謊者悖論的完整前置工具。

下一篇不再只是問：

$$
L=T
\quad\text{還是}\quad
L=F?
$$

而會真正問：

$$
\boxed{
\text{「假」在這句話裡究竟是哪一種型別、哪一個邊界、哪一個作用，以及它如何被回灌到自身？}
}
$$

這就是 RSCT 06 的起點。
