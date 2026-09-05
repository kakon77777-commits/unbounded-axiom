# RSCT 03｜雙向關係的生成結構：方向、正反、回返與反身性

**系列**：關係語義構成論（Relational Semantic Construction Theory, RSCT）03  
**英文題名**：*The Generative Structure of Bidirectional Relations: Direction, Polarity, Return, and Reflexivity*  
**作者**：Neo.K × GPT-5.6 Sol  
**機構**：EveMissLab（一言諾科技有限公司）  
**日期**：2026-08-27  
**版本**：v0.1  
**性質**：關係語義學／形式語義學／圖結構論／算子語義／反身結構研究  
**狀態**：系列正式初稿  
**前篇**：RSCT 02｜《沒有動詞的動詞性：形式構造如何生成作用、方向與過程》

---

## 摘要

RSCT 02 已提出：作用性不必依附於詞法動詞；關係、映射、構造、約束與指稱等形式結構皆可具有結構作用性，且作用通常生成 source/target 的方向區分。本篇進一步研究當兩個相反方向同時存在時，系統會生成哪些新的結構。

本文首先區分「雙向」「對稱」「互惠」「可逆」與「反身」五個常被混用的概念。若存在：

$$
O_{AB}:A\rightarrow B
$$

以及：

$$
O_{BA}:B\rightarrow A,
$$

則系統具有雙向性，但這並不推出：

$$
O_{AB}=O_{BA},
$$

也不推出：

$$
O_{BA}=O_{AB}^{-1}.
$$

因此：

$$
\boxed{
\text{Bidirectionality}
\neq
\text{Symmetry}
\neq
\text{Reciprocity}
\neq
\text{Invertibility}.
}
$$

本文把一組雙向關係表示為：

$$
\mathbf B_{AB}
=
\left(
O_{AB},
O_{BA}
\right),
$$

並引入方向交換算子：

$$
\mathcal J
\left(
O_{AB},
O_{BA}
\right)
=
\left(
O_{BA},
O_{AB}
\right).
$$

若：

$$
\mathcal J^2=\operatorname{id},
$$

則雙向結構至少形成一個最低的正反對偶。這裡的「正／反」不預設善惡、真假或數值正負，只表示同一對端點間兩個可區分的方向座標。

一旦兩個方向被同時保存，系統不再只有單一關係值，而至少具有一個方向對：

$$
\mathbf r_{AB}
=
\left(
r_{A\rightarrow B},
r_{B\rightarrow A}
\right).
$$

因此，雙向性本身會打開一個最低二座標表示接口。若各方向後續可以排序、比較或度量，則可進一步定義差異、比值、偏序或張力；但本文刻意不把「存在雙向」直接等同於「已存在實數度量」。更精確地說：

$$
\boxed{
\text{Bidirectionality}
\Rightarrow
\text{Comparative Coordinates}
\not\Rightarrow
\text{A Unique Metric}.
}
$$

本文進一步指出，雙向關係天然允許回返合成：

$$
A
\xrightarrow{O_{AB}}
B
\xrightarrow{O_{BA}}
A,
$$

從而生成：

$$
\Phi_A
=
O_{BA}\circ O_{AB}
:
A\rightarrow A.
$$

同理：

$$
\Phi_B
=
O_{AB}\circ O_{BA}
:
B\rightarrow B.
$$

這些自映射並非預先假定的傳統反身關係 $R(x,x)$，而是由跨節點回返路徑生成。本文將其稱為「生成式反身性」（generative reflexivity）或「回返反身性」（return reflexivity），並嚴格區分於傳統關係論中的 reflexive relation。

最後，本文建立從雙向關係到下一篇張力態空間的接口。若兩方向分別具有允許狀態域：

$$
\mathcal S_{AB},
\qquad
\mathcal S_{BA},
$$

則雙向狀態至少位於乘積空間：

$$
\mathcal S_{AB}^{\leftrightarrow}
=
\mathcal S_{AB}
\times
\mathcal S_{BA}.
$$

此乘積空間已經允許談論內部、角點、極端組合、對角線與非對稱區域；但真正的張力量、極值與邊界語義將留待 RSCT 04 正式定義。

**關鍵詞**：雙向關係、方向、正反、對偶、回返、反身性、自映射、對稱、可逆、狀態空間、關係語義構成論

---

# 0. 問題：雙向到底比「兩支箭頭」多了什麼？

考慮：

$$
A\rightarrow B.
$$

這只告訴我們一個方向：

$$
A\quad\text{to}\quad B.
$$

如果再加入：

$$
B\rightarrow A,
$$

最表面的理解是：

> 現在有兩支箭頭。

但如果我們保留兩個方向的區分，而不把它們立即合併，就會出現新的結構：

- 正向與反向；
- 方向對；
- 可比較性；
- 回返；
- 閉路；
- 自映射；
- 對稱／不對稱判定；
- 可逆／不可逆判定；
- 乘積狀態空間。

因此：

$$
\boxed{
\text{Bidirectionality}
\text{ is structurally richer than two isolated arrows.}
}
$$

本篇的核心就是把這些「多出來的東西」逐一分開。

---

# 1. 雙向的最低定義

## 定義 1：雙向作用對

若存在：

$$
O_{AB}:A\rightarrow B
$$

以及：

$$
O_{BA}:B\rightarrow A,
$$

則稱：

$$
\mathbf B_{AB}
=
\left(
O_{AB},
O_{BA}
\right)
$$

為一組雙向作用對。

其中：

$$
O_{AB}
$$

與：

$$
O_{BA}
$$

是兩個獨立可辨識的方向作用。

因此：

$$
\boxed{
O_{AB}
\text{ 與 }
O_{BA}
\text{ 不應預先合併成單一無方向關係。}
}
$$

---

# 2. 雙向不等於對稱

傳統上，對稱關係要求：

$$
R(A,B)
\Rightarrow
R(B,A).
$$

但在 RSCT 中，僅僅同時存在：

$$
O_{AB}
$$

與：

$$
O_{BA}
$$

還不表示兩者相同。

可能：

$$
O_{AB}\neq O_{BA}.
$$

例如：

- $A$ 對 $B$ 提供資訊；
- $B$ 對 $A$ 提供權限；
- $A$ 對 $B$ 施加要求；
- $B$ 對 $A$ 回傳證據。

兩個方向都存在，但關係型別完全不同。

因此：

$$
\boxed{
\text{Bidirectionality}
\not\Rightarrow
\text{Symmetry}.
}
$$

---

# 3. 雙向不等於互惠

「互惠」通常包含某種交換、回報、配平或回應語義。

但雙向只要求：

$$
A\rightarrow B
$$

與：

$$
B\rightarrow A
$$

同時存在。

它不要求：

$$
\operatorname{Value}(A\rightarrow B)
=
\operatorname{Value}(B\rightarrow A).
$$

也不要求：

$$
\operatorname{Type}(A\rightarrow B)
=
\operatorname{Type}(B\rightarrow A).
$$

所以：

$$
\boxed{
\text{Bidirectionality}
\not\Rightarrow
\text{Reciprocity}.
}
$$

互惠是雙向結構上的更強條件。

---

# 4. 雙向也不等於可逆

如果：

$$
O_{AB}:A\rightarrow B,
$$

真正的逆算子需要滿足：

$$
O_{AB}^{-1}\circ O_{AB}
=
\operatorname{id}_A
$$

以及：

$$
O_{AB}\circ O_{AB}^{-1}
=
\operatorname{id}_B.
$$

但一個實際存在的反向作用：

$$
O_{BA}:B\rightarrow A
$$

不必是：

$$
O_{AB}^{-1}.
$$

所以：

$$
\boxed{
O_{BA}
\neq
O_{AB}^{-1}
}
$$

是完全允許的。

這表示「回來」與「恢復原狀」不是同一件事。

---

# 5. 方向對：雙向後的最低新物件

一旦保存兩個方向，就得到：

$$
\mathbf r_{AB}
=
\left(
r_{A\rightarrow B},
r_{B\rightarrow A}
\right).
$$

即使目前 $r$ 只是一個符號狀態，而不是數值，這個 pair 已經比單一：

$$
r_{AB}
$$

資訊更多。

因為它保留：

$$
\text{forward}
$$

與：

$$
\text{reverse}
$$

兩個位置。

因此：

$$
\boxed{
\text{雙向會生成最低二座標表示。}
}
$$

這裡的「二座標」不是說必然已經形成：

$$
\mathbb R^2.
$$

它首先只表示：

$$
X\times Y.
$$

---

# 6. 正反不是善惡，也不是先驗真假

為了表示方向，可以暫時稱：

$$
A\rightarrow B
$$

為正向，

而：

$$
B\rightarrow A
$$

為反向。

但這裡的：

$$
+,
\quad
-
$$

若被使用，只表示 orientation。

所以：

$$
\boxed{
\text{Positive/Negative Orientation}
\neq
\text{Good/Bad}
\neq
\text{True/False}.
}
$$

這一區分非常重要。

因為 RSCT 05 才會研究真／假與邊界之間的關係。

在本篇，正反只是一對方向標記。

---

# 7. 方向交換算子

定義：

$$
\mathcal J
:
\left(
O_{AB},
O_{BA}
\right)
\mapsto
\left(
O_{BA},
O_{AB}
\right).
$$

若交換兩次回到原結構：

$$
\mathcal J^2
=
\operatorname{id},
$$

則 $\mathcal J$ 是一個 involution。

因此雙向關係天然允許一種最低正反對偶：

$$
\boxed{
\mathbf B_{AB}
\xleftrightarrow{\mathcal J}
\mathbf B_{BA}.
}
$$

這種對偶首先是結構交換，而不是價值否定。

---

# 8. 正反對偶與否定必須分開

否定算子通常表示：

$$
\neg P.
$$

而方向交換表示：

$$
\mathcal J(O_{AB},O_{BA})
=
(O_{BA},O_{AB}).
$$

二者完全不同。

所以：

$$
\boxed{
\text{Reverse}
\neq
\text{Negation}.
}
$$

這對後續說謊者悖論非常重要。

「反向」不能因為形式上看似負號，就直接與「假」或「否定」同一化。

---

# 9. 雙向如何帶來可比較性？

如果只有：

$$
r_{A\rightarrow B},
$$

我們只能描述一個方向。

加入：

$$
r_{B\rightarrow A},
$$

後，就可以問：

$$
r_{A\rightarrow B}
\stackrel{?}{=}
r_{B\rightarrow A}.
$$

或者：

$$
r_{A\rightarrow B}
\stackrel{?}{\prec}
r_{B\rightarrow A}.
$$

也可以問：

$$
\operatorname{type}
(
r_{A\rightarrow B}
)
\stackrel{?}{=}
\operatorname{type}
(
r_{B\rightarrow A}
).
$$

所以：

$$
\boxed{
\text{Bidirectionality}
\Rightarrow
\text{Comparability Questions}.
}
$$

但可比較問題的存在，不等於已有唯一數值尺度。

---

# 10. 雙向與量化：精確版本

「雙向帶來量化性」若要形式化，必須避免過強解釋。

本文提出：

### 定義 2：量化接口

若一個結構至少提供兩個可區分座標：

$$
(r_+,r_-),
$$

並允許後續定義某種：

$$
Q(r_+,r_-),
$$

則稱此結構打開量化接口。

因此：

$$
\boxed{
\text{Bidirectionality}
\Rightarrow
\text{Quantification Interface}.
}
$$

但不必推出：

$$
r_+,r_-\in\mathbb R.
$$

它們也可以是：

- 偏序元素；
- 類別；
- 區間；
- 向量；
- 集合；
- 機率分布；
- 尚未度量化的語義狀態。

所以：

$$
\boxed{
\text{Quantifiable}
\neq
\text{Already Metric}.
}
$$

---

# 11. 如果可以度量，雙向自然生成差異量

若後續存在合法度量：

$$
q:
\mathcal R
\rightarrow
\mathbb R,
$$

則可以定義：

$$
q_+
=
q(r_{A\rightarrow B}),
$$

$$
q_-
=
q(r_{B\rightarrow A}).
$$

於是可得到：

$$
\Delta q
=
q_+-q_-.
$$

也可以得到：

$$
\Sigma q
=
q_++q_-.
$$

或者：

$$
\rho_q
=
\frac{q_+}{q_-}
$$

在分母合法時。

這說明：

$$
\boxed{
\text{雙向一旦度量化，就自然產生差、和、比例等二階關係。}
}
$$

但本篇不把其中任何一個指定為「張力」的唯一公式。

---

# 12. 雙向後生成的不只是量，而是量之間的關係

原始兩個方向：

$$
q_+,
\quad
q_-.
$$

又可以生成：

$$
\Delta q,
$$

$$
\Sigma q,
$$

$$
\rho_q.
$$

因此：

$$
\text{Relation}
\rightarrow
\text{Directional Pair}
\rightarrow
\text{Relation Between Directions}.
$$

也就是：

$$
\boxed{
\text{關係可以生成關係的關係。}
}
$$

這是一個高階化入口。

---

# 13. 回返：雙向真正開始形成閉合

若：

$$
A
\xrightarrow{O_{AB}}
B
$$

以及：

$$
B
\xrightarrow{O_{BA}}
A,
$$

則存在一條長度二的回返路徑：

$$
A
\rightarrow
B
\rightarrow
A.
$$

這與單純：

$$
A\rightarrow B
$$

結構不同。

因為起點重新成為終點。

因此：

$$
\boxed{
\text{Bidirectionality}
\Rightarrow
\text{Return Path Possibility}.
}
$$

---

# 14. 回返不等於無變化

如果：

$$
A
\xrightarrow{O_{AB}}
B
\xrightarrow{O_{BA}}
A,
$$

不表示系統真的完全回到原狀。

更準確地，應寫：

$$
a
\xmapsto{O_{AB}}
b
\xmapsto{O_{BA}}
a'.
$$

其中：

$$
a'
$$

可能：

$$
a'=a,
$$

也可能：

$$
a'\neq a.
$$

所以：

$$
\boxed{
\text{Return to the same carrier}
\neq
\text{Return to the same state}.
}
$$

這使回返與循環具有更豐富結構。

---

# 15. 自映射由回返生成

定義：

$$
\Phi_A
=
O_{BA}\circ O_{AB}.
$$

則：

$$
\Phi_A:A\rightarrow A.
$$

同理：

$$
\Phi_B
=
O_{AB}\circ O_{BA}
:
B\rightarrow B.
$$

因此，雙向關係可以在兩端各生成一個自映射。

這裡：

$$
A\rightarrow A
$$

不是原先假設，而是由：

$$
A\rightarrow B\rightarrow A
$$

合成。

因此本文稱：

$$
\boxed{
\text{Return-Generated Self-Mapping}.
}
$$

---

# 16. 傳統反身性與生成式反身性

傳統關係論中，若關係 $R$ 對所有 $x$ 滿足：

$$
R(x,x),
$$

則稱 $R$ 為 reflexive。

RSCT 不能把這一定義直接偷換。

因此本文區分：

### 傳統反身性

$$
R(x,x).
$$

### 生成式反身性

若：

$$
x
\xrightarrow{O_1}
y
\xrightarrow{O_2}
x
$$

使得：

$$
O_2\circ O_1:
x\rightarrow x,
$$

則稱此回返結構生成一個自映射接口。

記作：

$$
\mathsf{GRef}(x).
$$

所以：

$$
\boxed{
\mathsf{ReflexiveRelation}
\neq
\mathsf{GenerativeReflexivity}.
}
$$

---

# 17. 生成式反身性為什麼重要？

因為它說明：

> 自我作用不必從「自己直接指向自己」開始。

它可以先經過另一個存在、另一個狀態或另一個語義層，再回到自己。

即：

$$
A
\rightarrow
B
\rightarrow
A.
$$

更一般：

$$
A
\rightarrow
B
\rightarrow
C
\rightarrow
\cdots
\rightarrow
A.
$$

所以：

$$
\boxed{
\text{Self-reference}
\text{ may be path-generated rather than primitive}.
}
$$

這對後續說謊者分析非常關鍵。

---

# 18. 局部回返與全域閉環

若：

$$
A\rightarrow B\rightarrow A,
$$

這是一個局部閉環。

但更大的系統可以是：

$$
A\rightarrow B,
$$

$$
B\rightarrow C,
$$

$$
C\rightarrow A.
$$

此時：

$$
A
\rightarrow
B
\rightarrow
C
\rightarrow
A
$$

同樣生成：

$$
\Phi_A:A\rightarrow A.
$$

所以：

$$
\boxed{
\text{Reflexive Return}
\text{ 不要求二節點直接互返}.
}
$$

這說明反身性可以是網路層級生成。

---

# 19. 雙向的局部不對稱

令：

$$
\mathbf B_{AB}
=
(r_+,r_-).
$$

如果：

$$
r_+\neq r_-,
$$

則此雙向關係具有局部不對稱。

所以：

$$
\boxed{
\text{Bidirectional}
+
\text{Unequal Directions}
=
\text{Local Asymmetry}.
}
$$

這與前置關係世界論中的：

$$
A_{ij}\neq A_{ji}
$$

可以直接接軌。

---

# 20. 不對稱不是錯誤，而是資訊

如果系統一看到：

$$
r_+\neq r_-
$$

就強制：

$$
r_+=r_-,
$$

則可能直接刪除方向差異。

所以：

$$
\boxed{
\text{Asymmetry}
\text{ is information before it is pathology}.
}
$$

是否失衡、錯誤或不可持續，需要額外判定。

不對稱本身只是：

$$
\text{兩方向沒有重合}.
$$

---

# 21. 對稱線

若雙向狀態可以放進：

$$
\mathcal S_+\times\mathcal S_-,
$$

且兩方向可比較，則：

$$
r_+=r_-
$$

形成一個對稱子集。

在最簡單二維情況，可記為：

$$
\mathcal D
=
\{
(r_+,r_-)
:
r_+=r_-
\}.
$$

它可以被視為對角線。

而：

$$
r_+\neq r_-
$$

則落在對角線之外。

這提供後續張力分析的一個幾何接口。

---

# 22. 雙向狀態空間

若：

$$
r_+
\in
\mathcal S_+,
$$

且：

$$
r_-
\in
\mathcal S_-,
$$

則雙向狀態：

$$
\mathbf r
=
(r_+,r_-)
$$

屬於：

$$
\boxed{
\mathcal S^{\leftrightarrow}
=
\mathcal S_+
\times
\mathcal S_-.
}
$$

這是雙向後最自然的狀態空間。

此處不要求：

$$
\mathcal S_+
=
\mathcal S_-.
$$

所以雙向空間也可以是異質乘積。

---

# 23. 異質雙向空間

例如：

$$
\mathcal S_+
=
\mathsf{Care},
$$

$$
\mathcal S_-
=
\mathsf{Authority}.
$$

則：

$$
\mathcal S^{\leftrightarrow}
=
\mathsf{Care}
\times
\mathsf{Authority}.
$$

這時兩個方向甚至不是同一單位。

因此：

$$
\boxed{
\text{Bidirectional State Space}
\text{ need not be homogeneous}.
}
$$

這一點非常重要，因為它避免過早強迫所有關係進入同一標量。

---

# 24. 同質雙向空間才適合直接談差

若：

$$
\mathcal S_+
=
\mathcal S_-
=
\mathcal S,
$$

且存在差運算，才適合寫：

$$
\Delta r
=
r_+-r_-.
$$

如果兩方向異質：

$$
r_+:\alpha,
$$

$$
r_-:\beta,
$$

且：

$$
\alpha\neq\beta,
$$

則：

$$
r_+-r_-
$$

可能根本未定義。

所以：

$$
\boxed{
\text{方向差}
\text{ 也必須型別安全}.
}
$$

---

# 25. 邊界空間的前置接口

一旦有：

$$
\mathcal S^{\leftrightarrow}
=
\mathcal S_+\times\mathcal S_-,
$$

就可以開始問：

$$
\partial
\mathcal S^{\leftrightarrow}
$$

是否存在。

但本篇只建立問題，不直接把所有邊界叫做真或假。

若最簡化：

$$
\mathcal S_+
=
\mathcal S_-
=
[0,1],
$$

則：

$$
\mathcal S^{\leftrightarrow}
=
[0,1]^2.
$$

其邊界：

$$
\partial
\mathcal S^{\leftrightarrow}
$$

包含四條邊，而不只是兩個點。

因此：

$$
\boxed{
\text{雙向後的邊界一般比二值端點更豐富}.
}
$$

這將成為 RSCT 04 的直接核心。

---

# 26. 極端組合與角點

在：

$$
[0,1]^2
$$

中，四個角點為：

$$
(0,0),
$$

$$
(1,0),
$$

$$
(0,1),
$$

$$
(1,1).
$$

它們可以表示兩方向各自到達極端的不同組合。

因此：

$$
\boxed{
\text{兩個方向各有兩端}
\Rightarrow
\text{至少四種極端組合}.
}
$$

這與單一：

$$
\{-1,+1\}
$$

的二值想像不同。

但這些角點此時仍只是形式邊界，不等同於四態論中的四態，也不等同於真假。

---

# 27. 雙向、正反與四態不能直接同一化

四態論中的：

$$
(s,r)
$$

表示支持與反證兩個證據軸。

本篇的：

$$
(r_+,r_-)
$$

表示雙向關係的兩個方向座標。

兩者形式上都可以成 pair，但語義型別不同。

因此：

$$
\boxed{
(s,r)
\not\equiv
(r_+,r_-).
}
$$

除非後續建立合法映射。

形式相似不是本體同一。

---

# 28. 雙向與真／假也不能直接同一化

同樣地：

$$
r_+
$$

與：

$$
r_-
$$

不能直接命名為：

$$
T,
\quad
F.
$$

因為：

$$
\text{forward/reverse}
$$

只是方向，

而：

$$
\text{true/false}
$$

是後續評價語義。

所以：

$$
\boxed{
\text{Orientation Pair}
\neq
\text{Truth Pair}.
}
$$

RSCT 05 才會研究兩者是否透過張力與邊界建立某種映射。

---

# 29. 雙向的高階遞歸

一個雙向 pair：

$$
\mathbf B_{AB}
=
(r_+,r_-)
$$

本身也可以成為更高階關係的節點。

例如：

$$
R^\ast
(
\mathbf B_{AB},
\mathbf B_{CD}
).
$$

此時關係不再只作用於個體，而作用於「關係對」。

因此：

$$
\boxed{
\text{Relations can relate relations}.
}
$$

這使 RSCT 可以自然擴展到高階語義圖。

---

# 30. 雙向後的反身性不是終點

由：

$$
A\rightarrow B\rightarrow A
$$

生成：

$$
\Phi_A:A\rightarrow A.
$$

但 $\Phi_A$ 本身又可以再次作用：

$$
\Phi_A^2,
$$

$$
\Phi_A^3,
$$

$$
\ldots
$$

所以：

$$
\boxed{
\text{Return}
\rightarrow
\text{Self-map}
\rightarrow
\text{Iterated Self-map}.
}
$$

這提供後續動態、固定點與循環研究的接口。

但本系列目前先保持靜態／離散描述，不提前轉入時間動力學。

---

# 31. 說謊者問題中的雙向萌芽

「這句話是假的」至少可能包含：

$$
\mathsf{Sentence}
\xrightarrow{\mathsf{Ref}}
\mathsf{Sentence},
$$

以及：

$$
\mathsf{Sentence}
\xrightarrow{\mathsf{Eval}}
\mathsf{TruthState}.
$$

若評價結果又回頭參與原句內容，就可能出現：

$$
\mathsf{Sentence}
\rightarrow
\mathsf{Evaluation}
\rightarrow
\mathsf{Sentence}.
$$

這不是單純：

$$
L=\neg L.
$$

而是某種回返作用結構。

本篇不解決此問題，只指出：

$$
\boxed{
\text{自指悖論可能包含路徑生成的反身性}.
}
$$

---

# 32. 六個核心區分

本篇最重要的六個區分為：

$$
\boxed{
\text{Bidirectionality}
\neq
\text{Symmetry}.
}
$$

$$
\boxed{
\text{Bidirectionality}
\neq
\text{Reciprocity}.
}
$$

$$
\boxed{
\text{Bidirectionality}
\neq
\text{Invertibility}.
}
$$

$$
\boxed{
\text{Reverse}
\neq
\text{Negation}.
}
$$

$$
\boxed{
\text{Orientation Pair}
\neq
\text{Truth Pair}.
}
$$

$$
\boxed{
\text{Generative Reflexivity}
\neq
\text{Primitive Reflexivity}.
}
$$

---

# 33. 核心命題

## 命題 1：雙向生成方向對

若：

$$
A\rightarrow B
$$

與：

$$
B\rightarrow A
$$

同時存在，則可構造：

$$
\mathbf r_{AB}
=
(r_+,r_-).
$$

## 命題 2：雙向打開量化接口

$$
\boxed{
\text{Bidirectionality}
\Rightarrow
\text{Quantification Interface}.
}
$$

但：

$$
\boxed{
\text{Quantification Interface}
\not\Rightarrow
\text{Unique Metric}.
}
$$

## 命題 3：雙向生成回返可能

$$
\boxed{
A\rightarrow B
\land
B\rightarrow A
\Rightarrow
A\rightarrow B\rightarrow A.
}
$$

## 命題 4：回返生成自映射

$$
\Phi_A
=
O_{BA}\circ O_{AB}
:
A\rightarrow A.
$$

## 命題 5：雙向自然張成乘積狀態空間

$$
\boxed{
\mathcal S^{\leftrightarrow}
=
\mathcal S_+
\times
\mathcal S_-.
}
$$

## 命題 6：雙向邊界不必二值

如果：

$$
\mathcal S^{\leftrightarrow}
$$

為多維乘積空間，則：

$$
\partial
\mathcal S^{\leftrightarrow}
$$

一般不只包含兩個端點。

---

# 34. 可檢驗性與失敗條件

第一，如果雙向結構在保留：

$$
O_{AB},
\quad
O_{BA}
$$

後，沒有任何額外可辨識資訊，則方向對表示的必要性下降。

第二，如果所有實際雙向關係都必然滿足：

$$
O_{BA}
=
O_{AB}^{-1},
$$

則本文對「反向不等於逆」的普遍性判斷需要縮限。但自然語義與社會關係顯然提供大量反例，因此目前不採此假設。

第三，如果沒有任何合理結構能由：

$$
A\rightarrow B\rightarrow A
$$

生成有用的：

$$
A\rightarrow A
$$

自映射，則「生成式反身性」需要降級為純路徑描述。

第四，如果方向 pair 無法提供任何比較、排序、型別差或後續狀態空間建模能力，則「量化接口」概念沒有實際價值。

第五，本篇不證明：

$$
\text{Bidirectionality}
\Rightarrow
\mathbb R^2.
$$

若沒有額外度量結構，任何強行實數化都是過度建模。

---

# 35. 與 RSCT 04 的接口

本篇最後得到：

$$
\mathcal S^{\leftrightarrow}
=
\mathcal S_+
\times
\mathcal S_-.
$$

下一篇將正式研究：

- 何謂張力；
- 張力是否必須數值化；
- 如何從方向差異得到張力狀態；
- 張力空間如何形成；
- 極值、內部與邊界如何定義；
- 高維邊界是否可被低維真假投影。

因此下一篇為：

> **RSCT 04｜《關係張力態空間與邊界生成》**

其核心接口為：

$$
\boxed{
\text{Bidirectional Relation Space}
\rightarrow
\text{Tension State Space}
\rightarrow
\text{Boundary}.
}
$$

---

# 36. 結論

雙向不是兩支互不相關的箭頭。

只要：

$$
A\rightarrow B
$$

與：

$$
B\rightarrow A
$$

同時被保留，系統就得到一個方向對：

$$
(r_+,r_-).
$$

這個方向對可以進一步支持：

- 相等／不等；
- 對稱／不對稱；
- 同型／異型；
- 比較／排序；
- 回返；
- 自映射；
- 乘積狀態空間。

因此：

$$
\boxed{
\text{雙向本身就是一個結構生成器。}
}
$$

它不只增加第二個方向，而是讓原本的一維關係描述展開成至少二座標的關係空間。

更重要的是：

$$
A
\rightarrow
B
\rightarrow
A
$$

會生成：

$$
\Phi_A:A\rightarrow A.
$$

因此反身性不必總是從：

$$
R(A,A)
$$

這種 primitive 自指開始。

它可以由他向—回返—自映射逐步生成。

由此可以得到本篇最濃縮的生成鏈：

$$
\boxed{
\text{Direction}
\rightarrow
\text{Bidirectionality}
\rightarrow
\text{Polarity}
\rightarrow
\text{Comparability}
\rightarrow
\text{Return}
\rightarrow
\text{Self-map}
\rightarrow
\text{Generative Reflexivity}.
}
$$

而雙向方向對一旦形成：

$$
(r_+,r_-)
\in
\mathcal S_+
\times
\mathcal S_-,
$$

下一個真正的問題就不再只是「哪一邊存在」，而是：

$$
\boxed{
\text{兩個方向之間究竟形成了什麼張力空間，以及它的邊界在哪裡？}
}
$$

這正是 RSCT 04 的起點。
