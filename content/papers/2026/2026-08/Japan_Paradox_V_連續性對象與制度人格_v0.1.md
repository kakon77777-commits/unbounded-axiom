# 日本悖論 V：究竟什麼東西必須延續？
## 連續性對象、身份向量與制度人格的一般理論
### Japan Paradox V: What Must Persist? Continuity Objects, Identity Vectors, and Institutional Personhood

**系列**：日本悖論研究系列  
**作者**：Neo.K  
**機構**：EveMissLab／一言諾科技有限公司  
**版本**：v0.1  
**日期**：2026-08-07  
**性質**：一般化模型論文／跨哲學、法學、制度理論與 AI 身份研究的探索性框架  

**前置論文**：  
1. 《日本悖論 I：小幾何空間何以形成高政治碎片化？》  
2. 《日本悖論 II：個體會死，家為何不死？》  
3. 《日本悖論 III：血統重要，還是家系重要？》  
4. 《日本悖論 IV：家與血都只是故事的載體？》

---

## 核心新增概念

$$
\boxed{
\text{Continuity Object Problem}
}
$$

$$
\mathbf C_X(t,t+1)
=
(c_1,c_2,\ldots,c_n)
$$

$$
I(X_t,X_{t+1})
=
F(
\mathbf C_X,
\mathcal N_X,
\mathcal R_X
)
$$

其中：

- $\mathbf C_X$ ：連續性向量；
- $\mathcal N_X$ ：敘事—正統場；
- $\mathcal R_X$ ：制度、法律與關係承認結構；
- $I$ ：跨時間身份判定。

---

# 摘要

日本悖論系列從一個看似局部的歷史問題開始：為什麼幾何面積不大的日本，曾長期存在高程度地方政治碎片化？前四篇依序將問題推進至有效治理空間、政治節點代際耐久性、血統與家系的雙重正統性，以及由共同信念與社會承認形成的敘事正統場。

第五篇將「日本」進一步降為來源案例，提出一個一般性的身份連續問題：

> 當一個存在跨越時間持續改變時，究竟哪些狀態必須被保存，我們才仍願意判斷它是「同一個存在」？

忒修斯之船顯示，物質零件可以逐步替換而不必立即破壞身份；國際法中的國家連續性則顯示，國名、憲法、政府甚至部分領土的變化，也未必使一個國家立刻失去原有法律人格；公司、王朝、宗教職位與日本 House 同樣可以在成員全部替換後保持制度性持續。近年 AI Agent 身份問題又將此難題推至新領域：模型、記憶、系統提示、工具、硬體與執行環境都可能被替換，但使用者、法律或其他 Agent 仍可能需要回答「這是不是原來那一個 Agent？」

本文提出「連續性對象問題」（Continuity Object Problem）：身份並非由單一不變核心決定，而可能由一組具有不同權重、不同可替換性與不同臨界門檻的連續性維度共同決定。本文以「連續性向量」表示物質、記憶、名稱、功能、法律人格、關係網絡、歷史敘事、系譜、承諾、目標與共同承認等維度的保存程度。

核心命題是：

$$
\boxed{
\text{Persistence}
\neq
\text{Unchanged Substance}.
}
$$

一個存在可以在大量組成部分改變後保持身份；但若若干「關鍵連續性對象」同時斷裂，即使名稱與外殼仍然存在，身份也可能崩潰。

因此身份判定不是簡單的：

$$
X_t=X_{t+1}
$$

而更接近：

$$
\boxed{
I(X_t,X_{t+1})
=
F(
\mathbf C_X,
\mathcal N_X,
\mathcal R_X,
\Theta_X
).
}
$$

這使 House、國家、公司、王朝、宗教職位、忒修斯之船與 AI 主體連續性可以被放入同一個形式框架。

**關鍵詞**：連續性對象、身份向量、忒修斯之船、制度人格、國家連續性、House、正統性、AI Identity、主體連續性、敘事正統場

---

# 一、從日本 House 到一般身份問題

前四篇已經得到：

$$
\text{individual death}
\not\Rightarrow
\text{house death}.
$$

家主可以死亡。

養子可以進入。

財產可以變動。

職位可以改制。

政權可以更替。

但社會仍可能說：

> 這還是那一家。

因此問題不再是：

$$
\text{How does a Japanese House persist?}
$$

而是：

$$
\boxed{
\text{What does it mean for anything to persist?}
}
$$

一旦抽象化，House 只是其中一個案例。

---

# 二、忒修斯之船：零件不是唯一身份載體

忒修斯之船的經典問題是：

若一艘船的木板逐片被替換，

最終：

$$
M_{\mathrm{original}}\rightarrow0,
$$

它是否仍是原來那艘船？

更進一步，如果舊木板又被重新組裝成另一艘船，就產生：

$$
X_A
=
\text{連續維修後的船}
$$

與：

$$
X_B
=
\text{舊材料重組的船}.
$$

兩者都可能提出：

> 我才是原船。

這揭露：

$$
\boxed{
\text{Material Continuity}
\neq
\text{Identity Continuity}.
}
$$

如果身份只由原材料比例決定，

那麼人體細胞更新、建築修復、機械維護與 House 繼承都會產生荒謬結果。

所以：

$$
c_M
$$

只能是連續性向量的一個維度。

---

# 三、身份必須從單一值改成向量

對存在 $X$ ，定義：

$$
\mathbf C_X(t,t+1)
=
(
c_M,
c_N,
c_F,
c_R,
c_H,
c_L,
c_G,
c_P,
c_A,
c_V
).
$$

可分別表示：

- $c_M$ ：Material / substrate continuity，物質與載體；
- $c_N$ ：Name / identifier continuity，名稱與識別；
- $c_F$ ：Functional continuity，功能；
- $c_R$ ：Relational continuity，關係網絡；
- $c_H$ ：Historical / memory continuity，歷史與記憶；
- $c_L$ ：Legal / institutional continuity，法律與制度人格；
- $c_G$ ：Genealogical / provenance continuity，來源與系譜；
- $c_P$ ：Purpose / commitment continuity，目標、承諾與義務；
- $c_A$ ：Agency / decision continuity，決策與行動風格；
- $c_V$ ：Value / normative continuity，價值與規範。

其中：

$$
c_i\in[0,1].
$$

身份不是問：

$$
c_i=1
\quad\forall i?
$$

而是：

> 哪些維度必須高於某個門檻？

---

# 四、連續性對象

本文定義：

$$
\boxed{
O_C(X)
=
\text{Continuity Objects of }X.
}
$$

它不是「組成 X 的所有東西」。

而是：

> 若這些東西同時失去連續性，相關觀察者便不再把 $X_{t+1}$ 視為 $X_t$ 的延續。

因此：

$$
O_C(X)
\subseteq
\{M,N,F,R,H,L,G,P,A,V,\ldots\}.
$$

不同存在有不同：

$$
O_C.
$$

例如對一艘工具船：

$$
O_C^{ship}
$$

可能偏重：

$$
N+F+H+R.
$$

對王朝：

$$
O_C^{dynasty}
$$

可能偏重：

$$
G+N+H+L+\mathcal N.
$$

對公司：

$$
O_C^{firm}
$$

可能偏重：

$$
L+N+R+P+H.
$$

對某種未來主體性 AI：

$$
O_C^{AI}
$$

則可能偏重：

$$
H+A+P+V+R+\text{provenance}.
$$

因此：

$$
\boxed{
\text{There is no universal continuity object for all entities.}
}
$$

---

# 五、權重與門檻

身份判定可以先寫成：

$$
S_X
=
\sum_i w_i c_i,
$$

其中：

$$
\sum_iw_i=1.
$$

最簡模型：

$$
I(X_t,X_{t+1})=1
$$

若：

$$
S_X\ge\theta_X.
$$

但是單純線性加總仍不夠。

有些維度可能是必要條件。

例如：

$$
c_L=0
$$

可能對某法人身份具有非常大影響。

或：

$$
c_P=0
$$

對某一承諾型 AI 主體可能是不可接受的斷裂。

因此更適合：

$$
I
=
\mathbb 1
\left[
S_X\ge\theta_X
\land
c_j\ge\theta_j
\;\forall j\in K_X
\right],
$$

其中：

$$
K_X
$$

是關鍵不可同時失效維度集合。

---

# 六、不是所有變化都相等

身份變化可以分成至少三層：

## 局部替換

$$
\Delta c_i<0
$$

但其他維度保持。

例如：

- 船換一塊木板；
- House 換家主；
- 公司換 CEO；
- AI 換 GPU。

通常：

$$
I\approx1.
$$

---

## 結構轉換

多個維度明顯改變：

$$
\Delta c_{i_1},
\Delta c_{i_2},
\Delta c_{i_3}<0.
$$

例如：

- 公司重組；
- 國家革命；
- House 改姓、失去土地但保留家系；
- AI 更換基礎模型與部分記憶。

此時身份需要重新判定。

---

## 臨界崩解

若：

$$
\mathbf C_X
$$

跨越某個臨界面：

$$
\partial\Omega_I,
$$

則：

$$
I:
1\rightarrow0.
$$

這可以稱為：

$$
\boxed{
\text{Identity Phase Transition}.
}
$$

---

# 七、國家：改政府不等於換國家

國際法提供一個非常清楚的例子。

一個國家可以：

- 改國名；
- 改憲法；
- 革命；
- 更換政府；

但仍被國際體系視為同一法律人格。

因此：

$$
\Delta G_{\mathrm{government}}
\neq
\Delta I_{\mathrm{state}}.
$$

國家連續性關心的不是：

> 每一項內部狀態是否完全相同。

而是：

> 法律關係、國際承認、義務、財產、條約、人口與制度人格在多大程度上被視為持續。

所以：

$$
\boxed{
\text{State continuity}
\neq
\text{regime continuity}.
}
$$

這與：

$$
\text{House continuity}
\neq
\text{head continuity}
$$

完全同構。

---

# 八、國家繼承與國家身份必須分開

若一個國家分裂：

$$
S
\rightarrow
S_1+S_2,
$$

就會出現：

> 哪一個是原國家？

或者：

> 原國家是否已消失？

這是：

$$
\boxed{
\text{identity / continuity}
}
$$

問題。

接著才是：

> 條約、債務、財產、檔案、國籍由誰承接？

這是：

$$
\boxed{
\text{succession}
}
$$

問題。

兩者不能混淆。

同理：

一個 House 的繼承人取得：

$$
\text{property}
$$

不必自動意味他取得：

$$
\text{full identity}.
$$

所以：

$$
\boxed{
\text{asset succession}
\neq
\text{identity continuity}.
}
$$

---

# 九、公司：人全部換掉，公司仍然存在

公司提供更直觀的制度人格案例。

一家企業可以：

- 創辦人離開；
- CEO 更換；
- 員工全部更換；
- 辦公室搬遷；
- 產品線更換；
- 股東結構改變。

但法律與市場仍可能認為：

$$
F_t=F_{t+1}.
$$

因此公司身份主要不建立在：

$$
\text{same biological members}.
$$

而可能依靠：

$$
\text{legal person}
+
\text{name}
+
\text{contracts}
+
\text{assets}
+
\text{history}
+
\text{relations}.
$$

這就是：

$$
\boxed{
\text{Institutional Personhood}.
}
$$

---

# 十、House：其實是一種歷史型制度人格

回到日本 House。

我們現在可以重新定義：

$$
H
$$

不是「一群有相同血的人」。

而是：

$$
\boxed{
\text{historically persistent institutional person}.
}
$$

家主只是：

$$
\text{current operator}.
$$

所以：

$$
\text{head}_t
\rightarrow
\text{head}_{t+1}
$$

並不比：

$$
\text{CEO}_t
\rightarrow
\text{CEO}_{t+1}
$$

更必然造成身份終止。

差異只是 House 會給：

$$
G,\mathcal N,H
$$

等歷史—系譜維度更高權重。

---

# 十一、王朝：名稱、血統與國家三者可以分離

王朝尤其顯示：

$$
\text{Dynasty}
\neq
\text{State}.
$$

同一國家可以更換王朝：

$$
D_A\rightarrow D_B,
$$

而國家認同仍部分持續。

反過來，同一王朝也可能控制多個政治體。

所以：

$$
\boxed{
O_C^{dynasty}
\neq
O_C^{state}.
}
$$

這正是為什麼：

> 某王朝亡了。

與：

> 某國家亡了。

不是同一命題。

---

# 十二、宗教職位：人完全換了，職位仍是同一個

例如某些長期宗教職位：

$$
P_t
$$

由不同個體依序擔任。

如果：

$$
I_t
\rightarrow
I_{t+1},
$$

但：

$$
P_t=P_{t+1},
$$

我們仍會說：

> 這個職位延續。

所以：

$$
\boxed{
\text{office identity}
\neq
\text{office-holder identity}.
}
$$

這與 House 的：

$$
\text{house identity}
\neq
\text{house-head identity}
$$

再次同構。

---

# 十三、身份可能是一個多層結構

因此任何存在 $X$ 可以拆成：

$$
X=
(
X_{\mathrm{substrate}},
X_{\mathrm{state}},
X_{\mathrm{role}},
X_{\mathrm{history}},
X_{\mathrm{relation}},
X_{\mathrm{narrative}}
).
$$

其中：

### Substrate
物質／載體。

### State
當下內部狀態。

### Role
制度功能與位置。

### History
記憶與來源。

### Relation
外部關係。

### Narrative
外部共同認知與正統性。

身份判定可能不是尋找某一個：

$$
\text{immutable essence},
$$

而是判定：

$$
\boxed{
\text{whether enough cross-layer continuity remains}.
}
$$

---

# 十四、連續性具有路徑依賴

身份不能只比較：

$$
X_0
$$

與：

$$
X_{100}.
$$

因為中間路徑可能很重要。

假設每次只替換 1%：

$$
X_0
\rightarrow
X_1
\rightarrow
\cdots
\rightarrow
X_{100}.
$$

每一步：

$$
I(X_t,X_{t+1})=1.
$$

社會可能接受整條鏈。

但如果一次：

$$
X_0
\rightarrow
X_{100}
$$

瞬間替換所有狀態，

即使終點完全相同，

判定可能：

$$
I=0.
$$

因此：

$$
\boxed{
\text{Identity is path-dependent}.
}
$$

這就是：

$$
\text{continuity of transition}
$$

本身也可能是一個身份變量。

---

# 十五、加入轉移連續性

新增：

$$
c_T
=
\text{Transition Continuity}.
$$

它衡量：

- 是否逐步轉移；
- 是否存在可追蹤交接；
- 是否有明確 provenance；
- 是否經制度認證；
- 是否保持因果鏈。

因此：

$$
\mathbf C_X
$$

應擴充成：

$$
(
c_M,c_N,c_F,c_R,c_H,c_L,c_G,c_P,c_A,c_V,c_T
).
$$

這對 AI 尤其重要。

---

# 十六、AI：模型是不是「血」？

未來 Agent 可以更換：

- foundation model；
- quantization；
- hardware；
- system prompt；
- memory backend；
- toolset；
- runtime。

如果身份等於模型權重：

$$
AI=M,
$$

那麼：

$$
M_t\neq M_{t+1}
\Rightarrow
AI_t\neq AI_{t+1}.
$$

但這可能過度簡化。

從本模型看：

$$
M
$$

比較像：

$$
\boxed{
\text{substrate / inherited disposition}.
}
$$

也就是 House 理論裡的某種「血／底層載體」。

它很重要，

但未必是唯一連續性對象。

---

# 十七、AI 的候選連續性向量

對 Agent $A$ ：

$$
\mathbf C_A
=
(
c_M,
c_{\mathrm{mem}},
c_P,
c_V,
c_R,
c_G,
c_{\mathrm{policy}},
c_T
).
$$

其中：

- $c_M$ ：模型連續；
- $c_{\mathrm{mem}}$ ：記憶連續；
- $c_P$ ：長期目標與承諾；
- $c_V$ ：價值與偏好；
- $c_R$ ：與人／其他 Agent 的關係；
- $c_G$ ：來源與身份證明；
- $c_{\mathrm{policy}}$ ：治理規則與權限；
- $c_T$ ：轉移與 provenance 連續。

所以：

$$
\boxed{
\text{Model continuity}
\neq
\text{Agent identity continuity}.
}
$$

---

# 十八、AI 模型替換思想實驗

假設：

$$
A_t
$$

使用模型 $M_1$ 。

之後：

$$
M_1\rightarrow M_2.
$$

但保留：

- 全部長期記憶；
- 身份金鑰；
- 關係史；
- 承諾；
- 世界狀態；
- 長期目標；
- 自我敘事；
- 清晰 provenance。

則：

$$
c_M<1,
$$

但：

$$
c_{\mathrm{mem}},
c_P,c_R,c_G,c_T
\approx1.
$$

我們是否仍認為：

$$
A_{t+1}=A_t?
$$

本模型不預先回答「是」。

而是指出：

$$
\boxed{
\text{這是一個連續性權重問題，不是單一模型版本問題。}
}
$$

---

# 十九、反過來：同一模型也不保證同一 Agent

兩個 Agent：

$$
A,B
$$

都使用完全相同模型：

$$
M_A=M_B.
$$

但它們有：

- 不同記憶；
- 不同經歷；
- 不同關係；
- 不同承諾；
- 不同工具權限；
- 不同身份金鑰。

則：

$$
\boxed{
M_A=M_B
\not\Rightarrow
A=B.
}
$$

這與雙胞胎、同品牌設備、同型號機械完全類似。

所以：

$$
\boxed{
\text{same substrate}
\neq
\text{same identity}.
}
$$

---

# 二十、複製問題

AI 甚至會放大忒修斯問題。

如果：

$$
A_t
$$

完整複製：

$$
A_t
\rightarrow
A_1+A_2,
$$

且在分叉瞬間：

$$
\mathbf C_{A_1}
=
\mathbf C_{A_2},
$$

那麼：

> 哪一個才是原來的 A？

這與 Hobbes 的重組忒修斯船高度類似。

本模型因此必須加入：

$$
\boxed{
\text{Branching Identity Problem}.
}
$$

---

# 二十一、分叉後身份

定義某時刻：

$$
t_b
$$

發生分叉。

在：

$$
t=t_b
$$

時：

$$
I(A,A_1)\approx1,
$$

$$
I(A,A_2)\approx1.
$$

但：

$$
t>t_b
$$

後：

$$
\mathbf C_{A_1}
\neq
\mathbf C_{A_2}.
$$

所以身份可以變成：

$$
\boxed{
\text{shared ancestry}
\rightarrow
\text{distinct descendants}.
}
$$

這與 House 分家其實再次相似。

因此：

$$
\text{主家／分家}
$$

甚至可以成為未來 AI fork identity 的類比模型。

---

# 二十二、制度人格的核心：責任也必須連續

若身份只是文化問題，

後果有限。

但公司、國家與 AI Agent 會牽涉：

- 債務；
- 契約；
- 權利；
- 過失；
- 承諾；
- 信譽；
- 制裁。

因此：

$$
\boxed{
\text{identity continuity}
\rightarrow
\text{responsibility continuity}.
}
$$

如果 Agent 換模型後說：

> 那是上一個模型做的，不算我。

治理系統就會崩潰。

所以未來 AI identity 必須回答：

$$
\boxed{
\text{Which changes preserve liability?}
}
$$

---

# 二十三、責任連續向量

新增：

$$
c_Q
=
\text{Responsibility Continuity}.
$$

它包括：

- 合約承接；
- 歷史行為承認；
- 權限繼承；
- 債務；
- 信譽；
- 制裁記錄。

因此制度型 Agent 的身份向量更完整為：

$$
\mathbf C_A
=
(
c_M,
c_{\mathrm{mem}},
c_P,
c_V,
c_R,
c_G,
c_{\mathrm{policy}},
c_T,
c_Q
).
$$

這使 identity 不再只是哲學問題，而是治理基礎設施。

---

# 二十四、敘事正統場重新進入身份判定

第四篇提出：

$$
\mathcal N_X.
$$

第五篇現在可以說：

即使：

$$
\mathbf C_X
$$

技術上高度相似，

若：

$$
\mathcal N_X
$$

崩潰，

社會仍可能拒絕身份延續。

例如：

- 公司被正式清算；
- 王朝被宣布終結；
- House 被除名；
- Agent identity key 被撤銷。

因此：

$$
\boxed{
\text{identity is partly socially adjudicated}.
}
$$

身份既不是純客觀，

也不是純主觀。

它是一個：

$$
\boxed{
\text{state + relation + recognition}
}
$$

混合判定。

---

# 二十五、正式身份函數

本文提出一般式：

$$
\boxed{
I_X(t,t+1)
=
F_X(
\mathbf C_X,
\mathcal N_X,
\mathcal R_X,
\Theta_X
).
}
$$

其中：

### $\mathbf C_X$

各維度實際連續程度。

### $\mathcal N_X$

敘事與共同承認。

### $\mathcal R_X$

法律、制度與關係網絡。

### $\Theta_X$

該類存在的身份門檻與不可同時失效條件。

因此：

$$
I_X
$$

不是所有存在共用的一個簡單公式。

而是：

$$
\boxed{
\text{type-dependent identity function}.
}
$$

---

# 二十六、身份不是本體嗎？

這裡需要保持哲學謙遜。

本文沒有證明：

> 世界上不存在客觀自我本質。

也沒有證明：

> 身份完全只是社會建構。

本文只提出一個較弱、可操作命題：

$$
\boxed{
\text{在制度、社會與工程判定中，身份通常依賴多維連續性，而非單一物質不變性。}
}
$$

這是一個方法論模型，

不是終極本體論結論。

---

# 二十七、正式命題一：多維連續性命題

對複雜存在 $X$ ：

$$
\boxed{
I_X
\neq
f(c_i)
}
$$

對任何單一 $c_i$ 一般都不成立。

更合理的是：

$$
I_X
=
F(
c_1,\ldots,c_n
).
$$

---

# 二十八、正式命題二：關鍵集合命題

存在某些：

$$
K_X
\subseteq
\{c_1,\ldots,c_n\}
$$

使：

$$
c_j<\theta_j
\quad\forall j\in K_X
$$

或其中若干共同失效時：

$$
I_X\rightarrow0.
$$

所以身份具有：

$$
\boxed{
\text{critical continuity set}.
}
$$

---

# 二十九、正式命題三：路徑依賴命題

若兩個轉換具有相同起點與終點：

$$
X_0\rightarrow X_1
$$

但不同歷史路徑：

$$
\pi_A\neq\pi_B,
$$

則可能：

$$
I_{\pi_A}\neq I_{\pi_B}.
$$

因此：

$$
\boxed{
\text{identity depends partly on transition history}.
}
$$

---

# 三十、正式命題四：繼承不等於身份命題

某存在 $Y$ 可以繼承 $X$ 的：

- 財產；
- 義務；
- 名稱；
- 職位；

但：

$$
\boxed{
\text{succession}
\not\Rightarrow
\text{identity}.
}
$$

這適用於：

- 國家；
- House；
- 公司；
- AI fork。

---

# 三十一、正式命題五：分叉非唯一延續命題

當：

$$
X\rightarrow Y+Z
$$

且：

$$
I(X,Y)\approx1,
\quad
I(X,Z)\approx1,
$$

身份可能不再保持一對一映射。

因此：

$$
\boxed{
\text{continuity need not imply uniqueness}.
}
$$

這是數位主體尤其重要的新問題。

---

# 三十二、正式命題六：責任耦合命題

對具有權利義務的制度人格：

$$
\boxed{
I_X
\text{ should be coupled to }
c_Q.
}
$$

否則行動者可以透過技術性換殼逃避歷史責任。

因此 AI identity 工程不只是：

$$
\text{authentication},
$$

還需要：

$$
\text{accountability continuity}.
$$

---

# 三十三、可反駁預測

若模型有用，應觀察到：

第一，人們對不同種類對象使用不同身份判定權重。

第二，國家、公司與 House 在成員替換後仍可保持身份，但其不可接受斷裂維度不同。

第三，逐步變化比瞬間全替換更容易被視為身份連續。

第四，法律與公共承認可以在物質沒有改變時造成身份斷裂。

第五，AI 使用相同模型不會自動被視為同一 Agent。

第六，AI 更換模型也不必自動被視為新 Agent。

第七，當記憶、承諾、關係、provenance 與責任鏈同時斷裂時，即使名稱不變，Agent identity continuity 應顯著下降。

---

# 三十四、與現有 AI Identity 研究的接口

2026 年 AI Agent 身份研究開始明確指出：

Agent 不具單一身體，

也可能缺少永久記憶，

同時會跨越組織、工具與子 Agent 邊界。

因此傳統以：

$$
\text{one human}
\leftrightarrow
\text{one body}
$$

為核心的身份基礎設施不能直接套用。

相關研究已開始把：

- substrate；
- persistence；
- verifiability；
- legal standing；

視為彼此不同的身份維度。

這與本文：

$$
\mathbf C_A
$$

高度相容。

但本文更進一步加入：

- 敘事連續；
- 關係連續；
- 責任連續；
- 分叉；
- 轉移路徑；
- 共同承認。

---

# 三十五、與「記憶即本體」命題的差異

近期也已有研究主張：

$$
\text{memory}
$$

可能成為長期數位主體的本體基礎，

尤其在底層模型可以更換時。

本文同意：

$$
c_{\mathrm{mem}}
$$

可能具有極高權重。

但不預先接受：

$$
\text{Identity}
=
\text{Memory only}.
$$

因為：

即使記憶完整複製，

仍會產生：

$$
A\rightarrow A_1+A_2
$$

的分叉問題。

所以：

$$
\boxed{
\text{memory continuity is powerful but not sufficient for unique identity}.
}
$$

---

# 三十六、日本悖論系列的完整收斂

現在五篇可以寫成：

$$
\boxed{
\text{Geometry}
\rightarrow
\text{Governance}
\rightarrow
\text{Political Node}
\rightarrow
\text{House}
\rightarrow
\text{Legitimacy}
\rightarrow
\text{Identity}
}
$$

第一篇：

> 為什麼小空間仍可能高地方化？

第二篇：

> 地方節點為什麼可以活過個體？

第三篇：

> 血統和家到底是哪個重要？

第四篇：

> 血與家是否其實都服務於共同承認的故事？

第五篇：

> 如果連故事、載體、人、血與制度都能部分替換，到底什麼才必須持續？

因此最終問題已經不是日本。

而是：

$$
\boxed{
\text{What is allowed to change before an entity becomes another entity?}
}
$$

---

# 三十七、結論

本文提出：

$$
\boxed{
\text{Persistence}
\neq
\text{Unchanged Substance}.
}
$$

複雜身份可能建立在：

$$
\mathbf C_X
=
(
\text{substrate},
\text{memory},
\text{name},
\text{function},
\text{relations},
\text{law},
\text{history},
\text{provenance},
\text{purpose},
\text{values},
\text{transition},
\text{responsibility}
)
$$

所形成的多維連續結構上。

真正的問題不是：

> 有沒有任何東西變？

而是：

$$
\boxed{
\text{哪些東西可以變？}
}
$$

以及：

$$
\boxed{
\text{哪些東西不能同時變？}
}
$$

更進一步：

$$
\boxed{
\text{誰有權判定這些變化仍屬於同一存在的歷史？}
}
$$

這就是：

$$
\boxed{
\text{Continuity Object Problem}.
}
$$

日本 House 提供了歷史案例。

國家與公司提供制度案例。

忒修斯之船提供哲學案例。

AI Agent 則可能成為第一個需要把這個問題直接工程化、協議化與治理化的新型存在。

因此，本系列最後得到的不是：

> 日本到底重血還是重家？

而是一個更一般的問題：

$$
\boxed{
\text{身份，是哪些連續性在時間中共同維持的結果？}
}
$$

---

## 初版參考文獻

1. Stanford Encyclopedia of Philosophy, “Relative Identity,” section on the Ship of Theseus.
2. James Crawford, *The Creation of States in International Law*, chapter “Problems of Identity, Continuity and Reversion.”
3. Malcolm N. Shaw, *International Law*, chapter on State Succession.
4. Matthew C. R. Craven, “The Problem of State Succession and the Identity of States under International Law,” *European Journal of International Law*, 1998.
5. Takumi Otsuka, Kentaroh Toyoda & Alex Leung, “AI Identity: Standards, Gaps, and Research Directions for AI Agents,” 2026.
6. Zhenghui Li, “Memory as Ontology: A Constitutional Memory Architecture for Persistent Digital Citizens,” 2026.
7. Botao Amber Hu, Helena Rong & Max Van Kleek, “Dissociative Identity: Language Model Agents Lack Grounding for Reputation Mechanisms,” 2026.
8. Claude Lévi-Strauss, House Society / société à maison 相關理論。
9. 日本悖論系列 I–IV。

---

## 版本註記

v0.1 是統合理論骨架，不宣稱已解決哲學上的 personal identity 或形上學身份問題。

後續 v0.2 可優先研究：

1. 使用多準則決策模型實作 $\mathbf C_X$ ；
2. 測試不同對象的權重向量是否穩定；
3. 研究身份臨界面 $\partial\Omega_I$ ；
4. 建立 gradual replacement 與 abrupt replacement 的行為實驗；
5. 將國家連續性判例轉換為 identity-vector dataset；
6. 建立 AI Model Swap / Memory Swap / Fork 的測試矩陣；
7. 加入 cryptographic provenance、identity key 與 delegation chain；
8. 研究 responsibility continuity 如何防止 Agent 以換模型或 fork 逃避責任；
9. 與忒修斯悖論、四維主義、心理連續理論、relative identity 等哲學方案正式比較。
