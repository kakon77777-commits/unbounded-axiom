# RSCT 02｜沒有動詞的動詞性：形式構造如何生成作用、方向與過程

**系列**：關係語義構成論（Relational Semantic Construction Theory, RSCT）02  
**英文題名**：*Verbality Without Verbs: How Formal Structures Generate Actuation, Direction, and Process*  
**作者**：Neo.K × GPT-5.6 Sol  
**機構**：EveMissLab（一言諾科技有限公司）  
**日期**：2026-08-27  
**版本**：v0.1  
**性質**：形式語義學／語言哲學／算子語義／關係結構論／構造語義學  
**狀態**：系列正式初稿  
**前篇**：RSCT 01｜《異質語義型別組合：為何「說謊者」不等於「說謊」加「者」》

---

## 摘要

自然語言通常把「動作」與「動詞」聯繫在一起，因此容易產生一個隱含預設：只有出現動詞，語句才真正具有作用、變化、方向或過程。然而，形式數學、邏輯、程式、圖結構與關係表示顯示，作用性可以在完全沒有詞法動詞的情況下存在。一個箭頭、一個映射、一個關係、一個構造子、一個約束、一個偏序、一個重寫規則，甚至一個靜態配置本身，都可能決定「什麼可以作用於什麼」「作用方向為何」「哪些狀態可被轉換」「哪些路徑合法」「哪些回返會形成自映射」。

本文提出「結構作用性」（structural actuation）與「結構動詞性」（structural verbality）概念，主張：

$$
\boxed{
\text{Verbality}
\neq
\text{Verb Word}.
}
$$

詞法動詞只是作用性投影到特定自然語言後的一種表面形式。更底層的作用可由：

$$
R(x,y),
$$

$$
f:x\mapsto y,
$$

$$
\mathcal C:\alpha\rightarrow\beta,
$$

$$
x\preceq y,
$$

$$
K(x)=1,
$$

$$
x\rightsquigarrow y
$$

等形式結構承載。這些結構可能沒有任何自然語言動詞，卻已經包含關係、方向、允許、限制、生成、轉換與回返等作用。

本文進一步區分五個容易混淆的概念：詞法動詞、謂詞性、算子性、方向性與過程性。它們可以重疊，但不彼此等價。尤其，方向不必意味時間，過程不必意味物理運動，靜態結構也可以編碼可執行的作用規則。為避免把所有箭頭都誤解成時間演化，本文提出「作用圖」：

$$
\mathfrak A
=
(V,E,\tau,\sigma,\kappa),
$$

其中 $\tau$ 記錄型別， $\sigma$ 記錄方向語義， $\kappa$ 記錄作用條件或約束。作用圖可以是靜態的，但其結構本身定義了可能的操作、生成與路徑。

本文進一步提出三種作用性：直接作用性、構造作用性與關係作用性。直接作用性對狀態產生轉換；構造作用性生成新型別或新物件；關係作用性則透過位置、方向與約束改變可接受推理，即使沒有任何顯式狀態更新。由此可說明為何「關係」「極致」「張力」等表面名詞，在形式化後仍具有高度作用性：它們不只命名物件，更建立可比較方向、作用邊界與狀態空間。

本篇不把「作用」直接等同於時間，不處理雙向關係的完整反身結構，也不重定義真與假。其任務是為下一篇建立接口：一旦作用性與方向性可在靜態形式中存在，就可以進一步研究雙向關係如何生成正反、回返、自映射與反身性。

**關鍵詞**：結構作用性、結構動詞性、動詞、算子、關係、方向性、過程性、語義型別、形式語義、關係語義構成論

---

# 0. 問題：沒有動詞的公式，為什麼仍然「在做事」？

考慮：

$$
f(x)=y.
$$

此式沒有自然語言中的顯式動詞。

但我們仍會自然理解成：

> $x$ 經由 $f$ 被映射到 $y$。

又如：

$$
A\rightarrow B.
$$

它表面上只有兩個符號與一支箭頭，卻立即產生：

- 起點；
- 終點；
- 方向；
- 可達；
- 作用；
- 轉移；
- 依賴；

等結構。

再例如：

$$
\mathcal C:
\alpha
\rightarrow
\beta.
$$

它可以表示一個構造子把 $\alpha$ 型物件轉成 $\beta$ 型物件。

因此：

$$
\boxed{
\text{形式結構可以沒有動詞詞彙，卻具有動詞性。}
}
$$

這正是本篇要研究的問題。

---

# 1. 詞法動詞與結構動詞性

## 1.1 詞法動詞

令：

$$
\mathsf{LexVerb}
$$

表示某一自然語言中被詞法／句法系統分類為動詞的項目。

例如：

- 說；
- 跑；
- 改變；
- 生成；
- 判定；
- 連接；
- 推動。

它們在語句表面直接提供某種行為或事件結構。

## 1.2 結構動詞性

本文定義：

### 定義 1：結構動詞性

若一個形式物件 $X$ 的存在，會改變其他物件之間允許的關係、映射、方向、構造、限制、可達性或狀態轉換，則稱 $X$ 具有結構動詞性。

記作：

$$
\mathsf{Verbality}(X)=1
$$

僅表示存在此性質，不預設其必為二值本體。

因此：

$$
\boxed{
\mathsf{LexVerb}(X)
\not\Leftrightarrow
\mathsf{Verbality}(X).
}
$$

一個詞法動詞通常具有動詞性，但具有動詞性的形式物件不一定是詞法動詞。

---

# 2. 為什麼數學符號會具有動詞性？

## 2.1 函數

若：

$$
f:X\rightarrow Y,
$$

則 $f$ 定義：

$$
x\mapsto f(x).
$$

這裡的 $f$ 不只是名稱。

它規定：

> 哪些輸入如何被轉換成哪些輸出。

因此 $f$ 具有操作位置。

## 2.2 關係

若：

$$
R\subseteq X\times Y,
$$

且：

$$
R(x,y)
$$

成立，則 $x$ 與 $y$ 被放進一個特定關係結構。

即使 $R$ 不改變 $x$ 或 $y$ 的內部狀態，它仍改變：

$$
\operatorname{Structure}(x,y).
$$

因此關係也可能具有作用性。

## 2.3 約束

若：

$$
K(x)=1
$$

表示 $x$ 滿足約束 $K$，則 $K$ 會將允許空間限制為：

$$
\Omega_K
=
\{x\in\Omega:K(x)=1\}.
$$

所以約束雖然看似靜態，卻會改變：

$$
\text{哪些狀態可被接受}.
$$

因此：

$$
\boxed{
\text{限制也是作用。}
}
$$

---

# 3. 五個概念必須分開

RSCT 02 區分：

$$
\mathsf{LexVerb},
$$

$$
\mathsf{Predication},
$$

$$
\mathsf{Operation},
$$

$$
\mathsf{Direction},
$$

$$
\mathsf{Process}.
$$

它們常一起出現，但不能互相等同。

---

# 4. 詞法動詞不等於謂詞性

例如：

> A 是紅色的。

形式化：

$$
\mathsf{Red}(A).
$$

「紅」在自然語言中可能被分類為形容詞，但在形式邏輯中：

$$
\mathsf{Red}
$$

扮演謂詞。

因此：

$$
\boxed{
\text{Predication}
\neq
\text{Verb Part of Speech}.
}
$$

謂詞性是一種結構位置，而不是詞性本身。

同理：

> A 是說謊者。

可以寫：

$$
\mathsf{Liar}(A).
$$

這時「說謊者」表面是名詞性角色，但整個：

$$
\mathsf{Liar}(\cdot)
$$

正在執行謂述。

所以一個名詞化結果仍可進入作用位置。

---

# 5. 謂詞性不等於算子性

謂詞：

$$
P(x)
$$

主要回答：

> $x$ 是否滿足某個條件？

算子：

$$
O(x)=y
$$

則更接近：

> $x$ 經某個規則得到 $y$。

兩者可能重疊，但並不相同。

因此：

$$
\mathsf{Predicate}
\not\equiv
\mathsf{Operator}.
$$

在語言分析中，如果把所有具有作用的結構都強迫改寫成謂詞，可能會遺失：

- 輸入／輸出；
- 構造方向；
- 狀態變換；
- 型別轉換；
- 多步路徑。

---

# 6. 方向性不等於時間性

考慮：

$$
A\rightarrow B.
$$

最容易犯的錯誤是立即理解成：

$$
A
\text{ 先發生，}
B
\text{ 後發生}.
$$

但箭頭可以表示：

- 推論方向；
- 型別轉換；
- 資料流；
- 因果；
- 可達；
- 指稱；
- 權限；
- 語義構造；
- 依賴。

因此：

$$
\boxed{
\text{Direction}
\not\Rightarrow
\text{Physical Time}.
}
$$

方向首先只表示：

$$
\text{source}
\neq
\text{target}.
$$

時間語義需要額外結構。

---

# 7. 過程性也不等於時間演化

若一個構造：

$$
\alpha
\xrightarrow{\mathcal C}
\beta
$$

可以被理解為：

> 由 $\alpha$ 生成 $\beta$。

它具有過程性。

但若我們只是在一張靜態型別圖中表示這個規則，並不需要指定物理時間：

$$
t_0<t_1.
$$

因此：

$$
\boxed{
\text{Process Structure}
\not\Rightarrow
\text{Temporal Execution}.
}
$$

可以有：

$$
\text{靜態規則空間}
$$

而其元素描述：

$$
\text{可能過程}.
$$

這是本篇重要區分。

---

# 8. 靜態結構如何承載作用？

考慮一張靜態圖：

$$
G=(V,E).
$$

只要邊有方向：

$$
e=(u,v),
$$

就已經存在：

$$
u\rightarrow v.
$$

即使圖完全不隨時間變化，它仍然定義：

- 哪裡可以到哪裡；
- 哪些節點依賴哪些節點；
- 哪些操作允許接續；
- 哪些回路存在；
- 哪些節點是源；
- 哪些節點是匯。

所以：

$$
\boxed{
\text{靜態}
\neq
\text{無作用}.
}
$$

靜態只是：

$$
\text{結構本身不必改變}.
$$

但結構可以決定一整套可能作用。

---

# 9. 作用圖

為了區分普通圖與語義作用結構，本文定義：

$$
\mathfrak A
=
(V,E,\tau,\sigma,\kappa).
$$

其中：

- $V$：語義物件；
- $E$：作用邊；
- $\tau$：節點與邊的型別；
- $\sigma$：方向語義；
- $\kappa$：作用條件、約束或有效域。

若：

$$
e=(x,y)\in E,
$$

則：

$$
\sigma(e)
$$

不必等於時間。

它可以是：

$$
\mathsf{construct},
$$

$$
\mathsf{reference},
$$

$$
\mathsf{evaluate},
$$

$$
\mathsf{bind},
$$

$$
\mathsf{negate},
$$

$$
\mathsf{restrict},
$$

等。

因此：

$$
\boxed{
\mathfrak A
\text{ 是作用可能性的靜態表示。}
}
$$

---

# 10. 三種最低作用性

## 10.1 直接作用性

若：

$$
O(x)=y
$$

且 $y$ 與 $x$ 在某狀態維度上不同：

$$
y\neq x,
$$

則 $O$ 具有直接作用性。

例如：

$$
\mathsf{Neg}(T)=F.
$$

## 10.2 構造作用性

若：

$$
C(x):\beta
$$

由：

$$
x:\alpha
$$

生成新型別：

$$
\alpha\neq\beta,
$$

則 $C$ 具有構造作用性。

例如：

$$
\mathsf{Agentize}:
\mathsf{ActRel}
\rightarrow
\mathsf{Role}.
$$

## 10.3 關係作用性

若 $R(x,y)$ 不直接改寫 $x,y$，但會改變它們在系統中的：

- 可達；
- 權限；
- 解釋；
- 約束；
- 比較；
- 推理；

則 $R$ 具有關係作用性。

這一類最容易被低估，因為它看起來「沒有真的改變物件」。

但：

$$
\boxed{
\text{改變關係位置，本身就可能改變可行世界。}
}
$$

---

# 11. 第四種作用性：選擇作用

若：

$$
S:
\Omega
\rightarrow
\Omega'
$$

且：

$$
\Omega'
\subsetneq
\Omega,
$$

則 $S$ 透過排除可能性產生作用。

例如：

$$
\Omega'
=
\{x\in\Omega:K(x)=1\}.
$$

所以：

$$
\boxed{
\text{Selection}
=
\text{Actuation by exclusion}.
}
$$

在語言中，修飾語、限定詞、量詞與語境條件都可能具有這種作用。

---

# 12. 第五種作用性：地址作用

若：

$$
\mathsf{Ref}(s)=x,
$$

則「指稱」本身也具有作用性。

因為它把：

$$
s
$$

與某個目標：

$$
x
$$

綁定。

所以：

$$
\boxed{
\text{Reference}
\neq
\text{Passive Labeling}.
}
$$

指稱會改變：

> 這個符號後續作用於哪個對象。

因此在說謊者問題中：

> 「這句話」

不能被視為一個沒有作用的代名詞。

它至少執行：

$$
\mathsf{Ref}:
\mathsf{Expression}
\rightarrow
\mathsf{Target}.
$$

---

# 13. 「者」為什麼看似名詞化，卻高度動詞化？

RSCT 01 寫：

$$
\mathsf{Agentize}:
\mathsf{ActRel}
\rightarrow
\mathsf{Role}.
$$

自然語言表面上，「者」是一個名詞化成分。

但在形式結構中，它執行：

$$
\text{predicate-like}
\rightarrow
\text{role}.
$$

因此：

$$
\boxed{
\text{名詞化形式}
\text{ 可以由動詞性的構造算子生成。}
}
$$

結果是名詞型，不代表生成操作沒有作用性。

這說明：

$$
\text{surface category}
$$

與：

$$
\text{constructional actuation}
$$

必須分開。

---

# 14. 「關係」為什麼是名詞，又同時具有動詞性？

「關係」表面是名詞。

但若：

$$
R(A,B)
$$

成立，則：

$$
A
\xleftrightarrow{R}
B
$$

的結構被建立。

只要：

$$
R(A,B)
\neq
R(B,A),
$$

我們立刻得到：

$$
\boxed{
\text{方向差異}.
}
$$

所以「關係」一旦形式化，就不只是命名「某個東西」。

它會決定：

$$
\text{誰對誰},
$$

$$
\text{從哪裡到哪裡},
$$

$$
\text{哪個方向有效}.
$$

因此關係天然具有結構作用性。

---

# 15. 「張力」為什麼也具有作用性？

假設：

$$
\Theta(R)
$$

表示某種關係差異、不平衡、不相容或更新驅動。

即使我們暫時不把：

$$
\Theta
$$

數值化，它仍可建立：

$$
R_1
\prec_\Theta
R_2
$$

或：

$$
R_1
\sim_\Theta
R_2.
$$

一旦可比較，就產生：

- 方向；
- 偏序；
- 接近；
- 遠離；
- 增強；
- 減弱；

等語義。

因此：

$$
\boxed{
\text{Tension}
\text{ can be structurally active before metricization.}
}
$$

這與既有前度量張力思想相容。

---

# 16. 「極致」為什麼也不是純形容詞？

「極致」表面像是在描述程度。

但如果狀態空間為：

$$
\mathcal S,
$$

「極致」實際上要求辨識：

$$
\partial\mathcal S
$$

或某種極值集合：

$$
\operatorname{Ext}(\mathcal S).
$$

於是「極致」其實在執行：

$$
\mathcal S
\rightarrow
\operatorname{Ext}(\mathcal S).
$$

這是一個選擇／邊界抽取作用。

因此：

$$
\boxed{
\text{極致}
\text{ 也可以形式化為作用算子。}
}
$$

這正是後續 RSCT 04–05 的接口。

---

# 17. 關係、極致、張力為什麼組合後具有更強作用性？

考慮：

$$
\text{關係的極致張力}.
$$

表面上幾乎全部是名詞／修飾結構。

但形式上可以拆成：

$$
R
\xrightarrow{\Theta}
\mathcal T_R
\xrightarrow{\operatorname{Ext}}
\partial\mathcal T_R.
$$

所以整句隱含：

$$
\boxed{
\text{關係}
\rightarrow
\text{張力映射}
\rightarrow
\text{極值／邊界抽取}.
}
$$

它不是被動名詞串。

它是一條操作鏈。

因此，語言中的「名詞化」可以只是把整段過程壓縮成一個穩定可引用的表面形式。

---

# 18. 動詞性可以被壓縮進名詞

定義一個作用鏈：

$$
x
\xrightarrow{O_1}
x_1
\xrightarrow{O_2}
x_2.
$$

若自然語言把整段作用鏈命名為：

$$
N,
$$

則：

$$
N
=
\operatorname{Name}
\left(
O_2\circ O_1
\right).
$$

此時 $N$ 表面是名詞，但內部仍保存：

$$
O_2\circ O_1.
$$

因此：

$$
\boxed{
\text{Nounization}
\text{ can compress process structure}.
}
$$

這對「說謊者」極其重要。

「說謊者」可以看似是一個角色名詞，但其生成歷史包含：

$$
\text{說謊}
\xrightarrow{\mathsf{Agentize}}
\text{說謊者角色}.
$$

---

# 19. 作用不等於物理因果

RSCT 必須避免另一種過度擴張。

若：

$$
A\rightarrow B
$$

表示型別轉換，

不代表：

$$
A
$$

在物理上造成：

$$
B.
$$

因此：

$$
\boxed{
\text{Semantic Actuation}
\not\Rightarrow
\text{Physical Causation}.
}
$$

本文使用「作用」是一個更一般的結構概念。

至少要區分：

$$
\mathsf{Semantic},
$$

$$
\mathsf{Computational},
$$

$$
\mathsf{Epistemic},
$$

$$
\mathsf{Normative},
$$

$$
\mathsf{Physical}
$$

等作用域。

不同作用域可能同構，但不能直接同一化。

---

# 20. 作用的方向性

若：

$$
O:X\rightarrow Y,
$$

則至少有：

$$
\operatorname{dom}(O)=X,
$$

$$
\operatorname{cod}(O)=Y.
$$

因此：

$$
\boxed{
\text{作用性通常會生成方向區分。}
}
$$

但：

$$
X\rightarrow Y
$$

不代表：

$$
Y\rightarrow X
$$

不存在。

可以另外存在：

$$
O^{-}:Y\rightarrow X.
$$

兩者可能：

$$
O^{-}\neq O^{-1}.
$$

也就是反向作用不必是正向作用的數學逆。

這一點將直接進入 RSCT 03。

---

# 21. 從方向到雙向

若同時存在：

$$
O_{AB}:A\rightarrow B,
$$

與：

$$
O_{BA}:B\rightarrow A,
$$

則我們得到：

$$
A
\xrightleftarrows[O_{BA}]{O_{AB}}
B.
$$

此時：

$$
O_{AB}
$$

與：

$$
O_{BA}
$$

可以是：

- 相同；
- 不同；
- 不可比較；
- 不同強度；
- 不同型別；
- 不同條件下有效。

所以：

$$
\boxed{
\text{Bidirectionality}
\neq
\text{Symmetry}.
}
$$

這是下一篇最重要的起點。

---

# 22. 回返與自映射的萌芽

一旦有：

$$
A
\xrightarrow{O_{AB}}
B
\xrightarrow{O_{BA}}
A,
$$

便可構成：

$$
\Phi_A
=
O_{BA}\circ O_{AB}.
$$

所以：

$$
\Phi_A:
A\rightarrow A.
$$

這是一個自映射。

注意：

$$
A\rightarrow A
$$

不是因為一開始假設反身性，而是由雙向路徑組合生成。

因此後續可研究：

$$
\boxed{
\text{Bidirectionality}
\rightarrow
\text{Return}
\rightarrow
\text{Self-map}.
}
$$

本篇只建立這個接口，不提前把它稱為完整反身性理論。

---

# 23. 作用與狀態空間

若系統允許若干作用：

$$
\mathcal O
=
\{O_i\}_{i\in I},
$$

則所有可由合法作用到達的狀態形成：

$$
\mathcal S_{\mathcal O}.
$$

所以：

$$
\boxed{
\text{作用規則可以張成狀態空間。}
}
$$

更一般地：

$$
\mathcal S_{\mathcal O}
=
\operatorname{Reach}
(
S_0,\mathcal O
).
$$

這裡的「張成」不必是線性代數意義，只表示：

> 一組作用規則定義可達狀態集合。

因此：

$$
\text{Actuation}
\rightarrow
\text{Reachability}
\rightarrow
\text{State Space}.
$$

這條鏈將與後續張力空間連接。

---

# 24. 結構作用性的守恆要求

為避免任何符號都被無限制宣稱「有作用」，本文提出最低要求。

若宣稱：

$$
\mathsf{Verbality}(X)=1,
$$

至少必須能指出 $X$ 改變了什麼。

可形式化為：

$$
\Delta_X\neq\varnothing.
$$

其中：

$$
\Delta_X
$$

可以是：

- 狀態差；
- 型別差；
- 可達差；
- 約束差；
- 關係差；
- 推理結果差；
- 指稱目標差。

若完全不存在任何可辨識差異：

$$
\Delta_X=\varnothing,
$$

則不應把 $X$ 的「作用性」只當作修辭。

所以：

$$
\boxed{
\text{作用必須對某個結構差異負責。}
}
$$

---

# 25. 靜態作用與動態執行

本文正式區分：

$$
\mathsf{StaticActuation}
$$

與：

$$
\mathsf{DynamicExecution}.
$$

靜態作用表示：

> 結構定義哪些作用可能成立。

動態執行表示：

> 某個作用在某個更新序列中實際被執行。

所以：

$$
\boxed{
\mathsf{StaticActuation}
\not\equiv
\mathsf{DynamicExecution}.
}
$$

例如一個函數定義：

$$
f:X\rightarrow Y
$$

可以靜態存在。

真正計算：

$$
f(x)
$$

則是執行事件。

這一區分可以避免把所有形式結構誤讀成時間流程。

---

# 26. 說謊者案例中的作用鏈

現在重新只看最小案例：

$$
\text{說謊}
+
\text{者}.
$$

RSCT 01 將它寫成：

$$
L
\xrightarrow{\mathsf{Agentize}}
\mathsf{LiarRole}.
$$

本篇進一步指出：

$$
\mathsf{Agentize}
$$

本身就是作用。

再把角色綁到某存在：

$$
\mathsf{Bind}
(
\mathsf{LiarRole},
x
).
$$

又是一個作用。

如果後面加入：

$$
\mathsf{Ref},
$$

$$
\mathsf{Eval},
$$

$$
\mathsf{Neg},
$$

則說謊者悖論完整分析會變成多個異質作用串接，而不是單一：

$$
L\leftrightarrow\neg L.
$$

所以：

$$
\boxed{
\text{悖論句是一條高度壓縮的作用鏈。}
}
$$

這是本系列往後的重要工作假說。

---

# 27. 作用鏈的型別安全

若：

$$
O_1:\alpha\rightarrow\beta,
$$

且：

$$
O_2:\beta\rightarrow\gamma,
$$

則可以合法組合：

$$
O_2\circ O_1:
\alpha\rightarrow\gamma.
$$

但若：

$$
O_2:\delta\rightarrow\gamma,
$$

而：

$$
\beta\neq\delta,
$$

則：

$$
O_2\circ O_1
$$

不必合法。

因此作用鏈需要型別安全：

$$
\boxed{
\operatorname{cod}(O_i)
=
\operatorname{dom}(O_{i+1})
}
$$

或至少存在合法 coercion。

這會成為 RSCT 06 檢查「說謊者」完整作用鏈的重要工具。

---

# 28. 作用鏈不必線性

自然語言可能同時啟動多條作用：

$$
x
\xrightarrow{O_1}
y,
$$

$$
x
\xrightarrow{O_2}
z.
$$

也可能匯聚：

$$
y
\xrightarrow{O_3}
w,
$$

$$
z
\xrightarrow{O_4}
w.
$$

所以真正結構可以是：

$$
\boxed{
\text{Actuation Graph}
}
$$

而不是單一序列。

這也是為什麼語句的複合語義不能只靠線性 token 順序窮盡。

---

# 29. 核心命題

## 命題 1：動詞性非詞性命題

$$
\boxed{
\text{Verbality}
\neq
\text{Verb Word}.
}
$$

## 命題 2：靜態作用命題

$$
\boxed{
\text{Static Structure}
\not\Rightarrow
\text{No Actuation}.
}
$$

## 命題 3：方向非時間命題

$$
\boxed{
\text{Direction}
\not\Rightarrow
\text{Time}.
}
$$

## 命題 4：作用域區分命題

$$
\boxed{
\text{Semantic Actuation}
\not\Rightarrow
\text{Physical Causation}.
}
$$

## 命題 5：選擇即作用命題

若一個結構改變允許狀態集合：

$$
\Omega
\rightarrow
\Omega',
$$

且：

$$
\Omega'\neq\Omega,
$$

則它具有作用性。

## 命題 6：雙向非對稱命題

$$
\boxed{
A\rightarrow B
\land
B\rightarrow A
\not\Rightarrow
R_{AB}=R_{BA}.
}
$$

---

# 30. 可檢驗性與失敗條件

第一，若一個形式結構被宣稱具有作用性，卻找不到任何：

$$
\Delta_X\neq\varnothing,
$$

則該作用性主張應被拒絕。

第二，如果所有所謂「結構動詞性」都能無損還原成隱含自然語言動詞，且結構層分析不提供額外預測或錯誤辨識能力，則本理論價值下降。

第三，如果方向性一律必須依賴時間才能被定義，則本文「方向先於時間語義」的部分需要修正。

第四，如果雙向路徑不能形成任何有意義的回返、自映射或關係差異，則下一篇的反身生成路徑被削弱。

第五，本篇不證明所有名詞都具有作用性。只有在：

$$
\Delta_X\neq\varnothing
$$

時，作用性才成立。

---

# 31. 與 RSCT 03 的接口

本篇最後得到：

$$
A
\xrightarrow{O_{AB}}
B,
$$

以及可能存在：

$$
B
\xrightarrow{O_{BA}}
A.
$$

下一篇將專門研究：

$$
\boxed{
\text{雙向}
\neq
\text{對稱}
}
$$

以及：

$$
\boxed{
\text{雙向}
\rightarrow
\text{正反方向}
\rightarrow
\text{回返}
\rightarrow
\text{自映射}
\rightarrow
\text{生成式反身性}.
}
$$

也就是：

> **RSCT 03｜《雙向關係的生成結構：方向、正反、回返與反身性》**。

---

# 32. 結論

自然語言中的動詞不是作用的唯一來源。

當一個形式結構寫成：

$$
R(A,B),
$$

$$
A\rightarrow B,
$$

$$
f:A\rightarrow B,
$$

$$
\mathcal C:\alpha\rightarrow\beta,
$$

$$
K(x)=1,
$$

它已經可能在指定：

- 哪些物件相關；
- 哪個方向有效；
- 什麼可以轉成什麼；
- 哪些狀態允許存在；
- 哪些路徑可以被走；
- 哪些角色可以被生成；
- 哪些對象可以被指稱。

因此「作用」不是由某個動詞字詞憑空創造，而可以被更底層的關係、映射、約束與型別結構承載。

這使得：

$$
\text{關係},
$$

$$
\text{張力},
$$

$$
\text{極致}
$$

即使表面上不是動詞，也可以在形式化後形成一條：

$$
R
\xrightarrow{\Theta}
\mathcal T_R
\xrightarrow{\operatorname{Ext}}
\partial\mathcal T_R
$$

的作用鏈。

由此：

$$
\boxed{
\text{語言的動詞性可以存在於詞彙之外。}
}
$$

而一旦作用帶來方向，下一個問題自然出現：

$$
\boxed{
\text{如果兩個方向同時存在，會生成什麼？}
}
$$

這正是 RSCT 03 的起點。
