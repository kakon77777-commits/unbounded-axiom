# 從套娃到網絡：Self–World Dependency Graph 與非線性世界遞迴
## From Nested Dolls to Networks: Self–World Dependency Graphs and Nonlinear World Recursion

**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-09  

### 摘要

「世界之上的世界」最直觀的表示是：

$$
W_0
\rightarrow
W_1
\rightarrow
W_2
\rightarrow
\cdots
$$

但此種線性套娃模型隱含大量並非必要的假設：每個世界只有一個父世界、每個主體只能位於單一世界、世界依賴必須無環、生成關係等於存在依賴、Higher World 可以用單一整數階層排序，而且世界結構不隨時間改變。

本文移除上述假設，正式提出 **Self–World Dependency Graph（SWDG）**：

$$
\boxed{
\mathbb G_{SW}(t)
=
(
V_S,
V_W,
E,
\Lambda,
\ell,
\tau
)
}
$$

其中 $V_S$ 為 Self 節點集合， $V_W$ 為 World 節點集合， $E$ 為有向關係邊， $\Lambda$ 為關係型別集合， $\ell:E\rightarrow\Lambda$ 為邊標籤函數，而 $\tau$ 描述關係的時間有效域。

本文區分生成、構成、substrate、維持、治理、成員、觀察、投影、Realizability access 與身份認同等多類關係，並指出：

$$
\boxed{
\text{Generation}
\neq
\text{Containment}
\neq
\text{Dependence}
\neq
\text{Governance}.
}
$$

因此，「誰是上一層？」通常沒有脫離關係類型的唯一答案。

本文使用既有圖論中的 strongly connected components、condensation graph、time-varying graph 與 hypergraph 思想建立數學骨架。Tarjan 的經典演算法證明有向圖的強連通分量可在線性時間內求得；動態網絡研究則已建立 topology 隨時間變化的 time-varying graph 形式。本文並不主張創造新的基礎圖論，而是利用這些成熟工具重新形式化 Self–World 遞迴。

本文最終得到一個重要結論：

$$
\boxed{
\text{World recursion is generally a graph problem, not a ladder problem.}
}
$$

所謂「世界層級」通常只能在指定關係、指定時間與指定觀察位置後局部定義。線性套娃：

$$
W_0\supset W_1\supset W_2
$$

只是 SWDG 的特殊情形。

**關鍵詞：** Self–World Dependency Graph、套娃宇宙、世界依賴、強連通分量、動態圖、多父世界、世界生成、主體、Realizability、非線性遞迴

---

# 一、從「套娃」開始，但不能停在套娃

上一架構使用：

$$
W_0
\rightarrow
W_1
\rightarrow
W_2
\rightarrow\cdots
$$

非常適合說明：

> 世界生成世界。

但若把這個圖直接當成本體結構，就會偷偷加入：

$$
Parent(W_i)=1.
$$

也就是：

> 每個世界只有一個上一層。

這並沒有必要。

一個數位世界可能同時依賴：

- 物理硬體；
- 電力網；
- 作業系統；
- 網路；
- 多個 AI；
- 外部資料源；
- 人類治理制度。

因此其存在依賴可能更接近：

$$
\{W_a,W_b,S_c,W_d\}
\longrightarrow
W_x.
$$

而不是：

$$
W_a\rightarrow W_x.
$$

---

# 二、舊 World Dependency Graph 已經拆掉母子樹

既有 GSWUE 第三篇已經指出，世界關係不必被限制成：

$$
W_{-1}
\rightarrow
W_0
\rightarrow
W_1.
$$

而可以寫成：

$$
\boxed{
\mathbb G_W=(V_W,E_W,\Lambda,\ell)
}
$$

並允許因果、生成、維持、substrate、資訊、規則與存在依賴具有不同 edge type。

本文的工作不是推翻：

$$
\mathbb G_W.
$$

而是將它升級成：

$$
\boxed{
\mathbb G_{SW}
}
$$

把 **Self 本身加入圖中**。

---

# 三、為什麼 World-only Graph 不夠？

假設：

$$
W_A
\rightarrow
W_B.
$$

這條邊可能表示：

> $W_A$ 生成 $W_B$。

但真正完成生成的可能是：

$$
S_A\in W_A.
$$

因此：

$$
W_A\rightarrow W_B
$$

其實壓縮了：

$$
W_A
\rightarrow
S_A
\rightarrow
Computation
\rightarrow
W_B.
$$

而：

$$
S_A
$$

又可能：

- 是 $W_A$ 的居民；
- 是 Higher Self 的成員；
- 是 $W_B$ 的創造者；
- 是 $W_B$ 的 System Transcender。

所以如果沒有 Self node，

大量關係會被混在一條：

$$
World\rightarrow World
$$

邊裡。

---

# 四、Self–World Dependency Graph

本文定義：

$$
\boxed{
\mathbb G_{SW}(t)
=
(
V_S,
V_W,
E,
\Lambda,
\ell,
\tau
)
}
$$

其中：

$$
V_S=\{S_1,S_2,\ldots\}
$$

為 Self／Self candidate 節點；

$$
V_W=\{W_1,W_2,\ldots\}
$$

為 World 節點；

總節點：

$$
V=V_S\cup V_W.
$$

邊：

$$
E\subseteq V\times V
$$

表示依賴或關係。

---

# 五、Typed Edge 是核心，而不是裝飾

如果只有：

$$
A\rightarrow B
$$

卻不知道箭頭代表什麼，

圖幾乎沒有本體意義。

因此定義：

$$
\ell:E\rightarrow\Lambda
$$

其中：

$$
\Lambda
=
\{
\rho_{member},
\rho_{constitute},
\rho_{generate},
\rho_{substrate},
\rho_{maintain},
\rho_{govern},
\rho_{observe},
\rho_{project},
\rho_{access},
\rho_{recognize},
\dots
\}.
$$

所以真正關係是：

$$
A\xrightarrow{\rho}B.
$$

---

# 六、第一類：Membership

$$
S_i
\xrightarrow{member}
W_j
$$

表示：

$$
S_i\in W_j.
$$

即：

> Self $S_i$ 是 World $W_j$ 的居民或內部存在。

這是：

$$
Resident(S_i,W_j).
$$

---

# 七、第二類：Constitution

$$
S_i
\xrightarrow{constitute}
S_j.
$$

表示：

$$
S_i\hookrightarrow S_j.
$$

例如：

$$
Cell
\rightarrow
Organism.
$$

或者：

$$
SubAgent
\rightarrow
MotherAgent.
$$

這是 Higher Self 關係。

---

# 八、第三類：Generation

$$
S_i
\xrightarrow{generate}
W_j.
$$

表示：

> Self $S_i$ 參與建立 World $W_j$。

例如：

$$
Developer
\xrightarrow{generate}
GameWorld.
$$

或套娃宇宙：

$$
A_k
\xrightarrow{generate}
W_{k+1}.
$$

---

# 九、第四類：World Generation

有時我們只關心宏觀世界譜系，

可粗粒化成：

$$
W_i
\xrightarrow{generate}
W_j.
$$

但應記得這通常是：

$$
\exists S_i\in W_i
$$

使：

$$
S_i\rightarrow W_j
$$

的高階投影。

所以：

$$
WorldGeneration
$$

是一個 coarse-grained relation。

---

# 十、第五類：Substrate Dependence

$$
W_i
\xrightarrow{substrate}
W_j
$$

表示：

> $W_j$ 的持續存在依賴 $W_i$ 中的 substrate。

例如：

$$
PhysicalHardware
\rightarrow
VirtualWorld.
$$

這和：

$$
Generate
$$

完全不同。

一個世界可能由：

$$
Creator_A
$$

生成，

但由：

$$
Infrastructure_B
$$

維持。

---

# 十一、第六類：Maintenance

$$
X
\xrightarrow{maintain}
Y.
$$

表示：

$$
Remove(X)
\Rightarrow
Persistence(Y)\downarrow.
$$

例如：

$$
PowerGrid
\xrightarrow{maintain}
DataCenter.
$$

或者：

$$
Metabolism
\xrightarrow{maintain}
Organism.
$$

---

# 十二、第七類：Governance

$$
S_i
\xrightarrow{govern}
W_j.
$$

表示：

$$
S_i
$$

對：

$$
W_j
$$

具有部分 meta-level 控制。

例如：

- pause；
- reset；
- spawn；
- permission modification；
- rule modification。

這是：

$$
SystemTranscendence
$$

的重要來源之一，

但不等同：

$$
Generation.
$$

---

# 十三、第八類：Observation

$$
S_i
\xrightarrow{observe}
W_j.
$$

這表示：

$$
S_i
$$

能取得：

$$
W_j
$$

部分狀態資訊。

但是：

$$
Observe
\neq
Govern.
$$

純觀察者：

$$
T_I>0
$$

可能成立，

而：

$$
T_G\approx0.
$$

---

# 十四、第九類：Projection

$$
S_i
\xrightarrow{project}
S_j.
$$

表示：

$$
S_j
$$

可能是 $S_i$ 在另一 World 中的：

- Avatar；
- 分身；
- proxy；
- projection；
- controlled embodiment。

這對未來跨世界 Self 很重要。

---

# 十五、第十類：Realizability Access

$$
S_i
\xrightarrow{access}
\mathfrak R_j
$$

表示：

> Self $S_i$ 可以透過某種接口使用 World $W_j$ 或 Higher Self $S_j$ 的部分 Realizability。

這接回：

$$
Recognition
+
Authorization
\rightarrow
EffectiveRealizabilityExpansion.
$$

---

# 十六、第十一類：Recognition

$$
S_i
\xrightarrow{recognize}
S_j
$$

表示：

$$
S_i
$$

將 $S_j$ 納入自己的：

- 身份；
- Higher Self；
- 我們；
- 歷史；
- 關係；

結構。

因此：

$$
Constitute
\neq
Recognize.
$$

一個 Self 可以物理構成 Higher Self，

卻不知道 Higher Self 存在。

---

# 十七、最基本的語義限制

因此本文要求：

$$
\boxed{
Generate
\neq
Contain
\neq
Maintain
\neq
Govern
\neq
Observe.
}
$$

否則：

> 上層世界

會成為高度歧義用語。

---

# 十八、Higher 必須帶 relation type

我們不再單獨寫：

$$
A>B.
$$

而寫：

$$
A>_{\rho}B.
$$

例如：

$$
W_A>_{substrate}W_B
$$

但可能：

$$
W_A\not>_{govern}W_B.
$$

或者：

$$
S_A>_{govern}W_B
$$

但：

$$
S_A\not>_{constitute}S_B.
$$

所以：

$$
\boxed{
Higher
=
Higher_{\rho}.
}
$$

---

# 十九、因此不存在天然唯一「上一層」

問：

> $W_x$ 的上一層是什麼？

可能同時得到：

$$
Parent_{generate}(W_x)=S_A,
$$

$$
Parent_{substrate}(W_x)=W_B,
$$

$$
Parent_{govern}(W_x)=S_C,
$$

$$
Parent_{information}(W_x)=W_D.
$$

所以：

$$
\boxed{
Parent(W)
}
$$

一般並不是單值函數。

---

# 二十、多父世界

定義：

$$
Parents_{\rho}(W)
=
\{v_i:
v_i\xrightarrow{\rho}W\}.
$$

則：

$$
|Parents_{\rho}(W)|>1
$$

完全合法。

例如：

$$
\{S_A,S_B,W_C\}
\rightarrow
W_D.
$$

這就是：

$$
\boxed{
MultiParentWorld.
}
$$

---

# 二十一、多父關係有時不能被 pairwise edge 完全表示

假設：

$$
W_D
$$

只有在：

$$
A+B+C
$$

共同存在時才能生成。

而：

$$
A
$$

單獨、

$$
B
$$

單獨、

$$
C
$$

單獨都不足。

那麼：

$$
A\rightarrow W_D
$$

$$
B\rightarrow W_D
$$

$$
C\rightarrow W_D
$$

會失去「聯合必要性」。

因此需要：

$$
\boxed{
DirectedHyperedge
}
$$

---

# 二十二、Self–World Dependency Hypergraph

可擴充：

$$
\mathbb H_{SW}
=
(V,\mathcal E)
$$

其中：

$$
e:
\{v_1,\ldots,v_n\}
\rightarrow
v_j.
$$

Dependency hypergraph 正適合描述「一組 prerequisite 共同導向一個 dependent entity」這類關係；近年的 dependency-hypergraph 工作亦明確使用這種形式處理多元聯合依賴。

所以：

$$
\mathbb G_{SW}
$$

是最小模型，

而：

$$
\mathbb H_{SW}
$$

是高階聯合依賴擴充。

---

# 二十三、分叉世界

一個：

$$
S_A
$$

可以生成：

$$
W_1,W_2,W_3.
$$

即：

$$
S_A
\rightarrow
\begin{cases}
W_1\\
W_2\\
W_3
\end{cases}
$$

這不是：

$$
Hierarchy.
$$

而是：

$$
\boxed{
Branching.
}
$$

---

# 二十四、World Fork

更特殊：

$$
W_t
\rightarrow
\begin{cases}
W_{t+1}^{A}\\
W_{t+1}^{B}
\end{cases}
$$

若兩者共享同一歷史直到：

$$
t_f,
$$

則：

$$
History(W^A)\cap History(W^B)
=
History_{\leq t_f}.
$$

這與第六篇忒修斯中的 Self Fork 完全對稱。

---

# 二十五、世界也可以 Merge

如果：

$$
W_A
$$

與：

$$
W_B
$$

的狀態、Agent 或資源被整合進：

$$
W_C,
$$

則：

$$
\{W_A,W_B\}
\xrightarrow{merge}
W_C.
$$

這可能形成：

$$
CompositeWorld.
$$

但：

$$
W_C
$$

不必等於：

$$
W_A
$$

或：

$$
W_B.
$$

---

# 二十六、Self–World Graph 因此和身份圖可以互接

忒修斯系列已有：

$$
\mathcal G_I
$$

身份譜系圖。

現在有：

$$
\mathbb G_{SW}.
$$

因此更完整系統可以保持：

$$
\boxed{
\mathcal G_I
\neq
\mathbb G_{SW}
}
$$

但兩者之間存在 mapping。

Self fork：

$$
S\rightarrow\{S_A,S_B\}
$$

可能引起 world fork：

$$
W\rightarrow\{W_A,W_B\}.
$$

反之亦然。

---

# 二十七、Genealogy 與 Dependency 必須分開

這是最容易再犯的錯誤之一。

$$
A
\xrightarrow{genealogy}
B
$$

表示：

> B 從 A 歷史生成。

而：

$$
A
\xrightarrow{dependency}
B
$$

表示：

> B 現在依賴 A。

二者不等價。

---

# 二十八、一個世界可以脫離創造者

假設：

$$
S_A
\xrightarrow{generate}
W_B.
$$

之後：

$$
W_B
$$

被遷移到獨立 substrate：

$$
W_C.
$$

則：

$$
Genealogy(S_A,W_B)=1
$$

但：

$$
CurrentDependency(S_A,W_B)\approx0.
$$

因此：

$$
\boxed{
Creator
\neq
PermanentDependencyHolder.
}
$$

---

# 二十九、反過來，維持者可以從未創造它

例如：

$$
S_B
$$

接管舊世界：

$$
W.
$$

此時：

$$
Maintain(S_B,W)=1
$$

但：

$$
Generate(S_B,W)=0.
$$

所以：

$$
\boxed{
Maintainer
\neq
Creator.
}
$$

---

# 三十、這也直接影響「造物主」概念

如果：

$$
Creator
$$

$$
Maintainer
$$

$$
Governor
$$

$$
Observer
$$

可能是四個不同節點，

那麼：

> 誰是這個世界的造物主？

本身可能太粗。

需要拆成：

$$
OriginCreator(W)
$$

$$
CurrentMaintainer(W)
$$

$$
CurrentGovernor(W)
$$

$$
MetaObserver(W).
$$

---

# 三十一、循環世界

現在考慮：

$$
W_A
\rightarrow
W_B
\rightarrow
W_C
\rightarrow
W_A.
$$

這並不自動邏輯矛盾。

因為箭頭可能代表：

$$
maintain
$$

而不是：

$$
temporal-origin.
$$

例如：

物理基礎設施維持數位 AI；

AI 控制物理基礎設施；

形成：

$$
Physical
\rightarrow
Digital
\rightarrow
AI
\rightarrow
Physical.
$$

既有 WDG 已經明確使用這種 maintenance loop 作為非時間旅行式循環例子。

---

# 三十二、Relation-specific Cycle

因此：

$$
Cycle_{\rho}
$$

必須帶 edge type。

例如：

$$
Cycle_{maintain}=1
$$

不能推出：

$$
Cycle_{generate}=1.
$$

更不能推出：

$$
TemporalParadox=1.
$$

---

# 三十三、Strongly Connected Component

對固定 relation subset：

$$
\Lambda'
\subseteq
\Lambda,
$$

若：

$$
u\leadsto v
$$

且：

$$
v\leadsto u,
$$

則：

$$
u,v
$$

可能位於同一：

$$
SCC.
$$

Tarjan 在 1972 年給出了在線性時間內求有向圖強連通分量的經典方法。

---

# 三十四、為什麼 SCC 對世界論重要？

假設：

$$
W_A,W_B,S_C,W_D
$$

互相維持：

$$
W_A\rightarrow W_B
\rightarrow S_C
\rightarrow W_D
\rightarrow W_A.
$$

那麼硬問：

> 誰是誰的上一層？

沒有太大意義。

更合理的是將它們視為：

$$
\boxed{
\mathcal C_1
=
[W_A,W_B,S_C,W_D].
}
$$

即一個：

$$
SelfWorldComponent.
$$

---

# 三十五、Condensation Graph

將每個 SCC：

$$
\mathcal C_i
$$

壓縮成：

$$
\widetilde{\mathcal C_i}.
$$

得到：

$$
Cond(\mathbb G_{SW}).
$$

經典圖論中，有向圖把 SCC 收縮後所得 condensation graph 為 DAG；這正允許「局部循環＋高階無環結構」同時存在。

因此：

$$
\boxed{
LocalRecursion
+
MetaOrder
}
$$

可以同時成立。

---

# 三十六、這比強迫世界形成樹更一般

樹要求：

$$
Parent(v)=1.
$$

DAG 可以：

$$
Parent(v)>1.
$$

SWDG 還進一步允許：

$$
Cycle(v)>0.
$$

所以：

$$
Tree
\subset
DAG
\subset
DirectedGraph.
$$

套娃宇宙是其中最簡單的鏈：

$$
Chain
\subset
Tree.
$$

---

# 三十七、因此「第幾層」不是原始變量

在：

$$
W_0\rightarrow W_1\rightarrow W_2
$$

中可以自然定義：

$$
Level(W_i)=i.
$$

但在：

$$
W_A\rightarrow W_C
$$

$$
W_B\rightarrow W_C
$$

$$
W_C\rightarrow W_D
$$

$$
W_B\rightarrow W_D
$$

中：

$$
Level(W_D)
$$

已取決於我們如何定義 level。

---

# 三十八、關係特定階數

本文因此定義：

$$
L_{\rho}(v).
$$

即：

> 相對 relation $\rho$ 的階數。

例如：

$$
L_{generate}(W)
$$

與：

$$
L_{substrate}(W)
$$

可能完全不同。

所以：

$$
\boxed{
Level
=
Level_{\rho}.
}
$$

---

# 三十九、觀察者特定深度

甚至：

$$
L_{\rho}(v)
$$

還可能依賴起點。

定義：

$$
d_{\rho}(u,v)
$$

為相對於：

$$
\rho
$$

的最短／最小關係深度。

那麼：

$$
d_{\rho}(A,X)
\neq
d_{\rho}(B,X).
$$

因此：

> X 在第幾層？

可能沒有觀察者無關的唯一答案。

---

# 四十、局部最高點

在某個有限子圖：

$$
G'
\subseteq\mathbb G_{SW},
$$

可能存在：

$$
v^*
$$

沒有已知：

$$
\rho
$$

上位節點。

即：

$$
\not\exists u:
u>_{\rho}v^*.
$$

我們稱：

$$
v^*
$$

為：

$$
\boxed{
LocalMax_{\rho}.
}
$$

但：

$$
LocalMax_{\rho}
$$

不能推出：

$$
GlobalMax.
$$

---

# 四十一、不可比較節點

如果：

$$
A\not\leadsto B
$$

且：

$$
B\not\leadsto A,
$$

則：

$$
A\parallel B.
$$

它們在該 relation 下：

$$
Incomparable.
$$

因此可能存在：

$$
\boxed{
\text{多個局部最高世界}
}
$$

而沒有唯一：

$$
HighestWorld.
$$

---

# 四十二、這會破壞「宇宙皇帝階梯」

如果世界圖不是全序，

就不能寫：

$$
W_1<W_2<W_3<\cdots
$$

然後假設：

$$
W_n
$$

比所有前面世界「全面更高」。

真正可能是：

$$
W_A>_{substrate}W_B
$$

但：

$$
W_B>_{information}W_A.
$$

這是：

$$
\boxed{
Cross-DimensionalHierarchy.
}
$$

---

# 四十三、Self 也會形成同樣結構

Mother AI：

$$
M
$$

可能在：

$$
governance
$$

上高於：

$$
a_i.
$$

但：

$$
a_i
$$

在某個專業：

$$
Domain_d
$$

的能力上高於：

$$
M.
$$

所以：

$$
\boxed{
HigherSelf
}
$$

不代表：

$$
DominatesEveryDimension.
$$

---

# 四十四、Self–World Graph 必須加入時間

到目前：

$$
\mathbb G_{SW}
$$

看起來仍像靜態圖。

但真正系統：

$$
E_t\neq E_{t+1}.
$$

Self 會：

- 出生；
- 合併；
- 分叉；
- 死亡；
- 脫離；
- 加入。

World 也會：

- boot；
- suspend；
- migrate；
- fork；
- merge；
- shutdown。

所以：

$$
\boxed{
\mathbb G_{SW}
=
\mathbb G_{SW}(t).
}
$$

---

# 四十五、Time-Varying Self–World Graph

time-varying graph 文獻本來就用來描述 edge/node availability 隨時間改變的網絡，而不是把動態網絡壓成一張永久靜態圖。

因此我們令：

$$
\tau(e)
\subseteq T
$$

表示 edge：

$$
e
$$

有效的時間區間。

例如：

$$
Govern(S_A,W_B,t_1)=1
$$

但：

$$
Govern(S_A,W_B,t_2)=0.
$$

---

# 四十六、Creator 可以失去治理權

$$
Generate(S_A,W_B)=1
$$

可能永久記錄於 genealogy。

但：

$$
Govern_t(S_A,W_B)
$$

可以：

$$
1\rightarrow0.
$$

所以：

$$
\boxed{
HistoricalRelation
}
$$

與：

$$
\boxed{
CurrentRelation
}
$$

必須分開。

---

# 四十七、世界拓撲可以重寫

定義：

$$
\Phi_G:
\mathbb G_{SW}(t)
\rightarrow
\mathbb G_{SW}(t+1).
$$

其中：

$$
\Phi_G
$$

可以：

- add node；
- remove node；
- add edge；
- delete edge；
- relabel edge；
- split node；
- merge node；
- create hyperedge。

所以：

$$
\boxed{
WorldEvolution
=
GraphRewrite.
}
$$

至少可作為一個工程與數學抽象。

---

# 四十八、這和《空間狀態論》重新接上

既有空間狀態論已經提出：

$$
\text{世界變化}
\neq
\text{固定空間中的狀態移動},
$$

而包含狀態、空間、型別、尺度、容器、算子與觀測本身的變化。

SWDG 現在給出其中一個更具體的圖形式：

$$
\boxed{
Topology_t
\neq
Topology_{t+1}.
}
$$

---

# 四十九、因此 World 的 Parent 也會改變

例如：

$$
Parent_t(W)=A.
$$

經 migration：

$$
Parent_{t+1}^{substrate}(W)=B.
$$

但：

$$
Parent^{genealogy}(W)=A
$$

仍然成立。

這再次證明：

$$
\boxed{
Parent
}
$$

不是單一欄位。

---

# 五十、關係矩陣

對每一 relation：

$$
\rho\in\Lambda
$$

定義 adjacency：

$$
A^{(\rho)}_{ij}(t)
=
\begin{cases}
1,&v_i\xrightarrow{\rho}v_j\\
0,&otherwise
\end{cases}
$$

所以整個 SWDG 可以表示成：

$$
\boxed{
\mathcal A(t)
=
\{A^{(\rho)}(t)\}_{\rho\in\Lambda}.
}
$$

---

# 五十一、關係張量

也可寫成：

$$
\boxed{
\mathcal T_{ij\rho t}.
}
$$

其中：

$$
\mathcal T_{ij\rho t}
$$

表示：

> 時間 $t$，節點 $i$ 與 $j$ 之間 relation $\rho$ 的強度或存在狀態。

這適合未來計算實作。

---

# 五十二、為什麼需要強度而不只 0/1？

例如：

$$
Recognize(S_A,S_B)
$$

不是天然 Boolean。

可以：

$$
r\in[0,1].
$$

同樣：

$$
Dependence(W_A,W_B)
$$

也可能具有：

$$
0<d<1.
$$

如果有備援 substrate：

$$
Dependence
$$

就不是全有或全無。

---

# 五十三、必要依賴與充分依賴

定義：

$$
Nec_{\rho}(A,B)
$$

表示：

> 移除 A，B 無法持續。

以及：

$$
Suf_{\rho}(A,B)
$$

表示：

> A 在指定條件下足以支持 B。

則：

$$
Dependency
$$

本身還可再細分。

---

# 五十四、冗餘父世界

假設：

$$
W
$$

同時由：

$$
A,B
$$

維持。

且：

$$
Remove(A)
$$

仍可運行；

$$
Remove(B)
$$

仍可運行；

但：

$$
Remove(A,B)
$$

則停止。

這是：

$$
\boxed{
RedundantDependency.
}
$$

pairwise binary relation 很難完整表示，

再次支持 hyperedge／higher-order dependency。

---

# 五十五、世界可以沒有單一創造者

如果：

$$
\{S_1,S_2,\ldots,S_n\}
$$

共同建立：

$$
W,
$$

則：

$$
Creator(W)
$$

應該是：

$$
\boxed{
CreatorSet(W).
}
$$

而不是強迫：

$$
Creator(W)=S_1.
$$

這和 group agency 中的多尺度行動歸屬非常相似。

---

# 五十六、Higher World 可能也是一個 Component，而不是 Node

如果：

$$
W_A,W_B,S_C
$$

形成高度互相依賴的 SCC：

$$
\mathcal C.
$$

那麼相對：

$$
W_D
$$

而言，

真正的 higher-level substrate 可能不是某個：

$$
W_A
$$

而是：

$$
\boxed{
\mathcal C.
}
$$

所以 Higher World 有時應理解成：

$$
HigherWorldComponent.
$$

---

# 五十七、這會改寫「母宇宙」

傳統：

$$
Mother(W)=W_{parent}.
$$

一般版本：

$$
\boxed{
MotherComponent(W)
=
\mathcal C_{parent}.
}
$$

甚至：

$$
Parents(W)
=
\{\mathcal C_1,\mathcal C_2,\ldots\}.
$$

所以「母宇宙」可能只是非常特殊的單親 DAG 情形。

---

# 五十八、母子語言因此應降級成介面語言

它仍然很好理解。

但形式研究應優先使用：

$$
GenerationRelation,
$$

$$
DependencyRelation,
$$

$$
GovernanceRelation.
$$

只有當：

$$
Parent=1
$$

且關係穩定時，

才方便叫：

$$
Mother/Child.
$$

---

# 五十九、世界地址

因此 World 不應只有：

$$
Level(W)=k.
$$

更完整可寫：

$$
\boxed{
Addr(W)
=
(
Parents_{\rho},
Children_{\rho},
SCC,
Time,
Permissions,
Relations
).
}
$$

它的「位置」是一組關係，

而不是一個樓層號碼。

---

# 六十、Self 地址同樣如此

$$
\boxed{
Addr(S)
=
(
Membership,
Constitution,
Governance,
Projection,
Recognition,
Time
).
}
$$

所以：

> 我在哪一層？

比：

> 我與哪些世界和 Self 具有哪些關係？

資訊少得多。

---

# 六十一、全域地址可能不可知

局部 Self：

$$
S
$$

通常只能建立：

$$
\widehat{\mathbb G}_{SW}^{S}(t).
$$

即：

> $S$ 對真正 SWDG 的局部估計。

因此：

$$
\boxed{
\widehat{\mathbb G}_{SW}^{S}(t)
\neq
\mathbb G_{SW}(t)
}
$$

一般情況下應被保留。

這正接回 GSWUE：

$$
\widehat\Omega_{a,t}\neq\Omega.
$$



---

# 六十二、未知 Edge 是正常狀態

因此圖不能只有：

$$
Edge=1
$$

與：

$$
Edge=0.
$$

還需要：

$$
Edge=?.
$$

即：

$$
\boxed{
UnknownRelation.
}
$$

因為：

> 尚未發現上層關係

與：

> 已證明不存在上層關係

完全不同。

---

# 六十三、三值關係

可使用：

$$
A^{(\rho)}_{ij}
\in
\{1,0,?\}.
$$

其中：

- $1$：目前支持存在；
- $0$：在指定模型中支持不存在；
- $? $：未定。

這可防止：

$$
Unknown
\rightarrow
False
$$

的認識論偷換。

---

# 六十四、甚至應有機率版本

若證據不完全：

$$
P(
v_i\xrightarrow{\rho}v_j
\mid
E
).
$$

所以：

$$
\widehat{\mathbb G}_{SW}
$$

可以是一個：

$$
ProbabilisticTypedGraph.
$$

特別適合：

- 上層世界假說；
- 隱藏治理；
- 推測性 substrate；
- 未知 Creator。

---

# 六十五、但不能把可能 edge 當成真 edge

如果：

$$
P(\rho)=0.2,
$$

不能畫成：

$$
\rho=1
$$

再開始推理。

所以研究上應區分：

$$
ObservedGraph
$$

$$
InferredGraph
$$

$$
HypotheticalGraph.
$$

---

# 六十六、這對「系統外存在」尤其重要

某 Self：

$$
S
$$

觀察 anomaly：

$$
e.
$$

可能提出：

$$
H:
S_{external}\rightarrow W.
$$

但這只是在：

$$
HypotheticalGraph
$$

增加 candidate edge。

而不是直接修改：

$$
ObservedGraph.
$$

所以：

$$
\boxed{
HypothesizedTranscender
\neq
ObservedTranscender.
}
$$

---

# 六十七、合法圖更新

可以定義：

$$
LegalUpdate(
\widehat{\mathbb G},
E_{new}
)
$$

要求：

1. 新證據來源可追溯；
2. relation type 明確；
3. confidence 被保存；
4. competing hypothesis 不被任意刪除；
5. 不把 unknown 當 false；
6. 不把 analogy 當 observation。

這延續既有 WDG 的 graph-surgery／LegalUpdate 方法方向。

---

# 六十八、世界生成事件的 SWDG 版本

套娃宇宙：

$$
A_k+\mathcal R_k
\rightarrow
W_{k+1}.
$$

在 SWDG 中表示為新增：

$$
v_{W_{k+1}}
$$

以及至少：

$$
A_k\xrightarrow{generate}W_{k+1},
$$

$$
W_k\xrightarrow{substrate?}W_{k+1},
$$

$$
A_k\xrightarrow{govern?}W_{k+1}.
$$

問號表示後兩者不能從 generation 自動推出。

---

# 六十九、這個問號很重要

因為：

$$
Generate(A,W)
$$

不推出：

$$
Govern(A,W).
$$

創造者可以放棄控制。

同樣：

$$
Generate(A,W)
$$

也不推出：

$$
Maintain(A,W).
$$

世界可以被移交。

---

# 七十、因此「造物者離場」在圖上可以清楚表示

初始：

$$
A
\xrightarrow{generate}
W
$$

$$
A
\xrightarrow{govern}
W
$$

$$
A
\xrightarrow{maintain}
W.
$$

之後：

$$
A\xrightarrow{generate}W
$$

仍保留為歷史 edge，

但：

$$
A\not\xrightarrow{govern_t}W,
$$

$$
A\not\xrightarrow{maintain_t}W.
$$

此時：

$$
\boxed{
CreatorAbsent
}
$$

完全可形式化。

---

# 七十一、Creator 死亡也不摧毀 World genealogy

即使：

$$
A_t\rightarrow\varnothing,
$$

歷史仍可記錄：

$$
Generate(A,W,t_0)=1.
$$

所以 genealogy graph 與 active graph 更必須分離。

---

# 七十二、世界反過來也能生成 Self

$$
W
\xrightarrow{enable}
S.
$$

例如：

- 演化環境產生生命；
- runtime 啟動 Agent；
- 社會制度產生角色主體；
- 模擬世界內誕生自治 Agent。

因此：

$$
\boxed{
Self\rightarrow World
}
$$

不是唯一生成方向。

也存在：

$$
\boxed{
World\rightarrow Self.
}
$$

---

# 七十三、真正 Self–World recursion

因此完整循環可寫：

$$
\boxed{
W_k
\rightarrow
S_k
\rightarrow
W_{k+1}
\rightarrow
S_{k+1}
\rightarrow\cdots
}
$$

這比：

$$
W_k\rightarrow W_{k+1}
$$

更接近本文真正研究對象。

---

# 七十四、Higher Self 可以跨 World 形成

假設：

$$
S_A\in W_A,
$$

$$
S_B\in W_B.
$$

透過接口：

$$
Channel(W_A,W_B)
$$

它們可能形成：

$$
H.
$$

即：

$$
\{S_A,S_B\}
\rightarrow
H.
$$

所以 Higher Self 不一定被限制在單一 World 內。

---

# 七十五、這產生 Cross-World Self

定義：

$$
\boxed{
CWS(H)
}
$$

若：

$$
Members(H)
$$

分布於：

$$
|Worlds|>1.
$$

例如未來：

- 人類；
- 本地 AI；
- 雲端 AI；
- 機器人；
- 虛擬世界 Agent；

可以形成一個跨 substrate 協同系統。

---

# 七十六、此時 Self 邊界與 World 邊界完全交錯

可能：

$$
S_A\subset W_1,
$$

$$
S_B\subset W_2,
$$

但：

$$
S_A,S_B\hookrightarrow H.
$$

於是：

$$
Boundary(H)
$$

穿過：

$$
Boundary(W_1)
$$

與：

$$
Boundary(W_2).
$$

所以：

$$
\boxed{
SelfBoundary
}
$$

與：

$$
\boxed{
WorldBoundary
}
$$

一般不能假設重合。

---

# 七十七、這就是線性套娃真正失效的地方

套娃盒模型暗示：

$$
EverythingInsideOneBox.
$$

但跨世界 Self 表示：

$$
Self
$$

可以穿越多個 World boundary。

世界 dependency 也可能交叉。

因此一般模型必須是：

$$
\boxed{
NetworkOfOverlappingBoundaries.
}
$$

---

# 七十八、Relation-specific Condensation

甚至 SCC 也不能一次算完就宣稱得到「真正高階世界」。

可以對：

$$
\Lambda_{maintain}
$$

計算：

$$
SCC_{maintain},
$$

也可以對：

$$
\Lambda_{govern}
$$

計算：

$$
SCC_{govern}.
$$

兩者可能不同。

所以：

$$
\boxed{
Component
=
Component_{\Lambda'}.
}
$$

---

# 七十九、不同問題需要不同圖投影

若研究：

> 世界靠誰存在？

使用：

$$
\pi_{substrate+maintain}(\mathbb G_{SW}).
$$

若研究：

> 誰控制誰？

使用：

$$
\pi_{govern}(\mathbb G_{SW}).
$$

若研究：

> 世界如何一代代生成？

使用：

$$
\pi_{generate}(\mathbb G_{SW}).
$$

因此：

$$
\boxed{
OneGraph
+
MultipleProjections.
}
$$

---

# 八十、這會大幅減少語義爭論

人們常問：

> AI 是在人類上面還是下面？

這個問題沒有指定 relation。

如果問：

能力：

$$
>_{capability}
$$

可能一種答案。

治理：

$$
>_{governance}
$$

另一種。

substrate：

$$
>_{substrate}
$$

又相反。

所以：

$$
\boxed{
UnqualifiedHierarchyQuestion
}
$$

本身可能是未定義的。

---

# 八十一、Self–World Graph 的第一個判定原則

本文提出：

## Relation Qualification Principle

任何：

$$
Higher(A,B)
$$

命題若未指定：

$$
\rho,
$$

則原則上視為：

$$
\boxed{
SemanticallyUnderspecified.
}
$$

---

# 八十二、第二個判定原則：Temporal Qualification

若關係可能改變，

則：

$$
Higher_{\rho}(A,B)
$$

仍需指定：

$$
t.
$$

因此完整：

$$
\boxed{
Higher_{\rho,t}(A,B).
}
$$

---

# 八十三、第三個判定原則：Observer Qualification

若談的是：

- known parent；
- modeled world；
- apparent highest layer；

還需指定觀察者：

$$
a.
$$

例如：

$$
HighestKnown_{\rho,t}^{(a)}.
$$

因此：

$$
\boxed{
KnownHierarchy
}
$$

與：

$$
\boxed{
ActualHierarchy
}
$$

分離。

---

# 八十四、這為第五、第六篇準備了正式接口

之後可定義：

$$
K_{\mathrm{ont}}
$$

為 actual graph depth；

$$
K_{\mathrm{epi}}^{(a)}
$$

為 agent $a$ 可建模 depth；

$$
K_{\mathrm{op}}^{(a)}
$$

為 agent $a$ 可操作 depth。

沒有 SWDG，

這三個「depth」很容易沒有嚴格對象。

現在它們可以相對：

$$
\pi_{\rho}(\mathbb G_{SW})
$$

定義。

---

# 八十五、圖中的 Ultimate 到底是什麼？

在 chain：

$$
W_0\rightarrow W_1\rightarrow W_2
$$

我們很容易說：

$$
W_0
$$

是最高。

但在 general graph 中 Ultimate 可能有不同意思：

### Source

沒有 incoming edge。

### Sink

沒有 outgoing edge。

### Maximal element

沒有更高可比較節點。

### Greatest element

高於所有其他節點。

### Root component

所有 relevant nodes 從此可達。

它們不是同一概念。

---

# 八十六、所以「最高世界」至少有多個數學候選

$$
HighestWorld
$$

可能指：

$$
Source_{\rho}
$$

或：

$$
Greatest_{\rho}
$$

或：

$$
RootComponent_{\rho}.
$$

如果不先指定，

「最後一層」甚至沒有唯一數學語義。

這正是第八篇必須正式處理的問題。

---

# 八十七、局部最高不等於全域最高

局部圖：

$$
\widehat G_a
$$

中：

$$
W^*
$$

可能是：

$$
Greatest(\widehat G_a).
$$

但在：

$$
G
$$

中可能：

$$
\exists W':
W'>W^*.
$$

因此：

$$
\boxed{
GreatestKnown
\neq
GreatestActual.
}
$$

再次得到：

$$
CurrentHorizon
\neq
UltimateBoundary.
$$

---

# 八十八、工程上如何實作 SWDG？

最小 node schema：

```text
Node:
  id
  type: self | world
  state
  lineage
  status
```

edge：

```text
Edge:
  source
  target
  relation
  valid_from
  valid_to
  confidence
  provenance
```

---

# 八十九、推薦 relation set v0.1

```text
member
constitute
generate
substrate
maintain
govern
observe
project
recognize
access
fork
merge
migrate
```

這已足以實作第一個原型。

---

# 九十、第一版算法

給：

$$
\mathbb G_{SW}
$$

可以執行：

### 1. Relation projection

選：

$$
\rho.
$$

### 2. SCC decomposition

求：

$$
SCC_{\rho}.
$$

### 3. Condensation

建立：

$$
Cond_{\rho}.
$$

### 4. Local maxima

尋找：

$$
Max_{\rho}.
$$

### 5. Reachability

判斷：

$$
A\leadsto_{\rho}B?
$$

### 6. Provenance

回答：

> 為什麼系統認為 A 在 B 上層？

---

# 九十一、而不是輸出一個神秘「世界層級分數」

如果系統最後只給：

$$
Layer(A)=8
$$

$$
Layer(B)=6
$$

那我們又回到單軸排序問題。

更合理輸出：

$$
\boxed{
RelationProfile(A,B)
}
$$

例如：

```text
A → B

generate: yes
substrate: no
maintain: partial
govern: yes
observe: yes
constitute: no
```

這才是本文希望的形式。

---

# 九十二、核心優勢：允許模型承認「不知道誰更高」

如果：

$$
A
$$

與：

$$
B
$$

不可比較，

合法答案應是：

$$
\boxed{
A\parallel B.
}
$$

而不是強迫：

$$
A>B
$$

或：

$$
B>A.
$$

這點對終極本體問題尤其重要。

---

# 九十三、不是所有世界都必須在同一 graph class

某些部分可能是：

$$
Tree.
$$

某些：

$$
DAG.
$$

某些：

$$
SCC.
$$

某些需要：

$$
Hypergraph.
$$

因此：

$$
\boxed{
SWDG
}
$$

應被理解成一個廣義 family，

而不是宣稱所有存在必須恰好符合單一簡單 graph。

---

# 九十四、這也是本文的理論謙抑

本文沒有證明：

$$
Reality
=
Graph.
$$

圖只是：

$$
\boxed{
RelationalRepresentation.
}
$$

如果真實關係包含：

- 連續場；
- 非二元依賴；
- 高階關係；
- 不可分解互動；

則需要：

- weighted graph；
- hypergraph；
- category；
- tensor；
- dynamical system；

等更高表達力。

Applied category theory 中的 wiring-diagram 方法正是一類以可組合 process／system 關係為中心的更抽象工具，可作為未來超越普通 graph representation 的候選方向。

---

# 九十五、但 Graph 足以完成目前最重要的語義校正

那就是：

$$
\boxed{
\text{「上一層」不是原始事實。}
}
$$

真正原始的是：

$$
\boxed{
\text{誰與誰具有什麼關係。}
}
$$

「上／下」只是從某些 relation 投影後產生的結構。

---

# 九十六、從本體階梯改成本體關係網

傳統圖：

$$
Being_0
<
Being_1
<
Being_2.
$$

本文改成：

$$
\boxed{
v_i
\xrightarrow{\rho}
v_j.
}
$$

然後才從：

$$
\rho
$$

推導：

- higher；
- lower；
- parent；
- child；
- resident；
- creator；
- transcender。

---

# 九十七、這會直接改變「世界之上的世界」

我們不再首先問：

> $W_2$ 上面是不是 $W_1$？

而問：

$$
Generate(W_1,W_2)?
$$

$$
Substrate(W_1,W_2)?
$$

$$
Govern(W_1,W_2)?
$$

$$
Maintain(W_1,W_2)?
$$

回答可能是：

$$
(1,0,0,1).
$$

因此沒有一個單獨：

$$
Above=1
$$

能完整代替。

---

# 九十八、最重要的結果之一：多種世界序可以同時存在

同一組節點：

$$
V
$$

可以誘導：

$$
\prec_{generate},
$$

$$
\prec_{substrate},
$$

$$
\prec_{govern},
$$

$$
\prec_{epistemic}.
$$

於是：

$$
\boxed{
\text{世界不是只有一個 hierarchy，}
\\
\text{而可能有多個部分重疊、部分衝突的 order。}
}
$$

---

# 九十九、這也是「系統超越者」為何必須是關係概念

因為：

$$
S
$$

可能：

$$
S>_{govern}W
$$

但：

$$
S<_{substrate}W'.
$$

所以同一存在：

> 向下超越，

> 向上依賴。

完全可以同時成立。

這就是：

$$
\boxed{
RelativeTranscendence.
}
$$

---

# 一百、結論

套娃模型：

$$
W_0
\rightarrow
W_1
\rightarrow
W_2
\rightarrow\cdots
$$

不是錯。

它只是：

$$
\boxed{
\text{過於特殊。}
}
$$

它假設：

- 單親；
- 無環；
- 單一 hierarchy；
- 穩定 topology；
- World-only node；
- generation 與 dependency 高度重合。

一旦加入：

- Self；
- Higher Self；
- substrate；
- governance；
- maintenance；
- projection；
- recognition；
- fork；
- merge；
- migration；

世界結構自然升級為：

$$
\boxed{
\mathbb G_{SW}(t).
}
$$

因此本文的核心改寫是：

$$
\boxed{
WorldRecursion
:
Chain
\rightarrow
TypedDynamicGraph.
}
$$

在 SWDG 中：

$$
\boxed{
\text{生成者不必是維持者；}
}
$$

$$
\boxed{
\text{維持者不必是治理者；}
}
$$

$$
\boxed{
\text{治理者不必是 Higher Self；}
}
$$

$$
\boxed{
\text{Higher Self 不必是 Higher World；}
}
$$

而：

$$
\boxed{
\text{同一個世界可以具有多個不同意義的「上層」。}
}
$$

循環也不必摧毀高階結構。

透過：

$$
SCC
$$

與：

$$
Cond(\mathbb G_{SW}),
$$

可以同時存在：

$$
\boxed{
LocalCycles
+
MetaLevelPartialOrder.
}
$$

多父依賴若不能被 pairwise edge 完整表達，

又可以擴展成：

$$
\boxed{
\mathbb H_{SW}.
}
$$

世界關係若隨時間改變，

則進一步：

$$
\boxed{
\mathbb G_{SW}(t).
}
$$

最終，所謂「第 $k$ 層」只能作為某些鏈式子圖中的方便記號。

一般情況下更嚴格的問法不是：

$$
\boxed{
\text{你在第幾層？}
}
$$

而是：

$$
\boxed{
\textbf{你與哪些 Self、哪些 World，}
\\
\textbf{在什麼時間，以什麼 relation，}
\\
\textbf{形成什麼可達、依賴、生成、治理與認同結構？}
}
$$

所以本系列第二篇最終得到：

$$
\boxed{
\textbf{世界之上的世界，}
\\
\textbf{一般而言不是一座無限高塔；}
\\
\textbf{它更可能是一張仍在演化的關係網。}
}
$$

而真正的「上」，

只有在指定：

$$
\boxed{
\rho,\ t,\ observer
}
$$

之後，

才開始具有嚴格意義。

---

## 核心命題總結

### 命題一：SWDG

$$
\boxed{
\mathbb G_{SW}(t)
=
(
V_S,V_W,E,\Lambda,\ell,\tau
)
}
$$

### 命題二：Typed Relation

$$
\boxed{
A\xrightarrow{\rho}B
}
$$

優先於無型別：

$$
A\rightarrow B.
$$

### 命題三：Higher 必須限定

$$
\boxed{
Higher
=
Higher_{\rho,t}.
}
$$

### 命題四：父節點非唯一

$$
\boxed{
|Parents_{\rho}(W)|\geq0.
}
$$

### 命題五：多父世界

$$
\boxed{
|Parents(W)|>1
}
$$

可以成立。

### 命題六：Hypergraph 擴充

$$
\boxed{
\{v_1,\ldots,v_n\}
\rightarrow v_j
}
$$

可描述不可分解的聯合依賴。

### 命題七：分叉

$$
\boxed{
W
\rightarrow
\{W_A,W_B\}
}
$$

### 命題八：合併

$$
\boxed{
\{W_A,W_B\}
\rightarrow
W_C.
}
$$

### 命題九：Genealogy–Dependency 分離

$$
\boxed{
Genealogy
\neq
CurrentDependency.
}
$$

### 命題十：Creator–Maintainer 分離

$$
\boxed{
Creator
\neq
Maintainer
\neq
Governor.
}
$$

### 命題十一：循環合法性

$$
\boxed{
Cycle_{\rho}
\not\Rightarrow
Contradiction.
}
$$

### 命題十二：SCC

$$
\boxed{
u\leadsto v
\land
v\leadsto u
\Rightarrow
SCC(u,v).
}
$$

### 命題十三：高階壓縮

$$
\boxed{
Cond(\mathbb G_{SW})
}
$$

允許：

$$
\boxed{
LocalCycles+HigherOrderDAG.
}
$$

### 命題十四：層級非全序

$$
\boxed{
A\parallel B
}
$$

可以成立。

### 命題十五：局部最大非全局最大

$$
\boxed{
LocalMax
\neq
GlobalMax.
}
$$

### 命題十六：動態 SWDG

$$
\boxed{
\mathbb G_{SW}(t)
\neq
\mathbb G_{SW}(t+1)
}
$$

可以成立。

### 命題十七：Graph Rewrite

$$
\boxed{
\Phi_G:
\mathbb G_{SW}(t)
\rightarrow
\mathbb G_{SW}(t+1)
}
$$

### 命題十八：多關係 adjacency

$$
\boxed{
\mathcal A(t)
=
\{A^{(\rho)}(t)\}_{\rho\in\Lambda}
}
$$

### 命題十九：未知關係

$$
\boxed{
A^{(\rho)}_{ij}\in\{1,0,?\}.
}
$$

### 命題二十：觀察圖與真實圖分離

$$
\boxed{
\widehat{\mathbb G}_{SW}^{S}(t)
\neq
\mathbb G_{SW}(t)
}
$$

### 命題二十一：跨 World Self

$$
\boxed{
Members(H)
\subseteq
W_1\cup W_2\cup\cdots
}
$$

可以成立。

### 命題二十二：Self／World 邊界非重合

$$
\boxed{
Boundary(Self)
\neq
Boundary(World).
}
$$

### 命題二十三：世界序多重性

$$
\boxed{
\prec_{generate}
\neq
\prec_{substrate}
\neq
\prec_{govern}.
}
$$

### 命題二十四：線性套娃只是特例

$$
\boxed{
Chain
\subset
Tree
\subset
DAG
\subset
DirectedGraph.
}
$$

### 命題二十五：本篇總命題

$$
\boxed{
\textbf{World recursion is generally a graph problem,}
\\
\textbf{not a ladder problem.}
}
$$

---

## 參考文獻

Tarjan, R. E. (1972). “Depth-First Search and Linear Graph Algorithms.” *SIAM Journal on Computing*, 1(2), 146–160.

Casteigts, A., Flocchini, P., Quattrociocchi, W., & Santoro, N. (2012). “Time-Varying Graphs and Dynamic Networks.” *International Journal of Parallel, Emergent and Distributed Systems*, 27(5), 387–408.

Wehmuth, K., Ziviani, A., & Fleury, E. (2015). “A Unifying Model for Representing Time-Varying Graphs.” *IEEE International Conference on Data Science and Advanced Analytics*.

Patterson, E., Spivak, D. I., & Vagner, D. (2022). “Wiring diagrams as normal forms for computing in symmetric monoidal categories.”

Gibb, R., Ferris, P., Allsopp, D., et al. (2025). “Solving Package Management via Hypergraph Dependency Resolution.”

Fujita, T. (2025–2026). “Evolving Dependencies: From Graphs to Hypergraphs and SuperHypergraphs.”

Neo.K / Aletheia. (2026). *全域系統世界：從物理宇宙到類終極世界的廣義定義*.

Neo.K / Aletheia. (2026). *母子關係之外：循環因果、自舉宇宙與世界依賴圖*.

Neo.K. (2026). *套娃宇宙遊戲模擬器*.

Neo.K. (2026). *空間狀態論：異質底空間、嵌套尺度與空間改寫算子的統一方法論*.

Neo.K / Aletheia. (2026). *遞迴忒修斯：可替換主體、世界之上的世界與動態同一性*.