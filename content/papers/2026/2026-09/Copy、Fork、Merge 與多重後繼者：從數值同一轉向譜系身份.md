# Copy、Fork、Merge 與多重後繼者：從數值同一轉向譜系身份

## Copy, Fork, Merge, and Multiple Successors: From Numerical Identity to Lineage Identity

**系列：** Post-Substrate Ontology／後載體本體論  
**Paper：** 05  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**理論協作：** Aletheia（GPT-5.6 Sol）  
**版本：** v0.1  
**日期：** 2026-09-02  
**文件性質：** 公開理論論文／分叉身份、人工主體譜系、合併與多重後繼者理論

---

## 摘要

傳統個人同一性問題通常假設一種近似線性的生命歷史：

$$
X_{t_0}
\rightarrow
X_{t_1}
\rightarrow
X_{t_2}
\rightarrow
\cdots
$$

因此「未來的哪一個人是現在的我？」通常被預設存在至多一個主要答案。

然而，可複製、可並行、可同步、可分叉、可合併的人工認知系統以及假想中的後載體人類，將破壞這項線性前提。

一個存在：

$$
P
$$

可能產生：

$$
P
\rightarrow
\{A,B\},
$$

而兩個原本不同的存在：

$$
A,B
$$

也可能在未來形成：

$$
\{A,B\}
\rightarrow
C.
$$

本文主張，這些情況不能只使用傳統數值同一：

$$
X=Y
$$

處理。

若強迫：

$$
A=P
$$

與：

$$
B=P
$$

同時成立，

則由等號的傳遞性：

$$
A=B,
$$

但在真正分叉後：

$$
A\neq B.
$$

因此，當多重後繼成為可能時，應將：

$$
\boxed{
\text{Numerical Identity}
}
$$

與：

$$
\boxed{
\text{Lineage Succession}
}
$$

明確分離。

本文延續既有「Successor Set」概念，定義：

$$
\boxed{
Succ(P)
=
\{X\mid P\leadsto X\}
}
$$

其中：

$$
P\leadsto X
$$

表示 $X$ 是 $P$ 的某種正當譜系後繼者，而不要求：

$$
P=X.
$$

相對地定義：

$$
\boxed{
Pred(X)
=
\{P\mid P\leadsto X\}.
}
$$

於是：

$$
|Succ(P)|>1
$$

描述分叉，

而：

$$
|Pred(X)|>1
$$

描述合併式祖先結構。

本文進一步區分：

$$
\boxed{
\text{Copy}
\neq
\text{Fork}
\neq
\text{Operational Fission}
\neq
\text{Phenomenal Fission}
}
$$

以及：

$$
\boxed{
\text{Data Merge}
\neq
\text{Cognitive Integration}
\neq
\text{Identity Fusion}
\neq
\text{Phenomenal Fusion}.
}
$$

一個副本只有在形成自己的持續未來時才構成 lineage fork；一個多節點系統即使已經物理分離，也可能因高度同步而暫時維持單一 operational identity domain；而是否真的出現兩個第一人稱主體，仍不能由 copy count 或 process count 直接推出。

同樣地，把兩個人的記憶資料寫入同一系統，不等於兩個主體已經合併。如果真正的 Merge 要具有身份意義，它至少需要某種跨來源整合：

$$
\boxed{
Integration(A,B\rightarrow C)
}
$$

使 $C$ 的未來認知狀態不能被充分描述為單純交替調用 $A$ 與 $B$ 的兩套獨立模組。

本文因此提出「譜系身份圖」：

$$
\boxed{
G_L=(V,E_L)
}
$$

其中節點代表不同存在狀態，邊則表示：

$$
\{
Birth,
Copy,
Fork,
Transfer,
Merge,
Reconstruction,
Transformation
\}.
$$

在這個框架中，「我是誰？」不再只能回答一個名稱，而可以回答：

$$
\boxed{
\text{What histories do I inherit, and what future branches inherit me?}
}
$$

本文並不宣稱未來人工系統必然具有意識，也不主張人格真的可以分裂或融合。本文的最小命題只是：

> 如果可複製、可分叉與可合併的系統被賦予持續身份、權利、責任或主體候選地位，則線性數值同一不足以描述其歷史關係。

2026 年 AI identity 研究已經開始明確指出，machine minds 可能具有 instance、model、persona 等多種自洽 identity boundaries，而可複製與可編輯性會破壞大量以人類單體為前提的身份直覺。 同年的人工心智 individuation 研究亦討論了單一人工系統內可能存在多個 mind candidate 的可能性。

因此本文提出後載體本體論的第五個核心原則：

$$
\boxed{
\text{Shared past does not require shared present,}
}
$$

$$
\boxed{
\text{and shared present does not require a unique past.}
}
$$

也就是：

> **一個存在可以有多個正當後繼者，而一個存在也可能具有多重正當祖先。身份在後載體文明中可能由線性鏈條轉化為有向譜系圖。**

**關鍵詞：** Post-Substrate Ontology、Copy、Fork、Merge、Branching Identity、Successor Set、Lineage Identity、Artificial Minds、Personal Identity、Multiple Successors、Identity Fusion

---

# 一、傳統身份理論隱藏了一條時間直線

正常人類生活大致符合：

$$
X_0
\rightarrow
X_1
\rightarrow
X_2
\rightarrow
\cdots
\rightarrow
X_n.
$$

即使：

- 身體細胞替換；
- 記憶改變；
- 人格逐漸改變；

歷史仍大致是一條單一路徑。

因此我們自然建立：

$$
X_0=X_1=X_2=\cdots=X_n
$$

這種日常身份模型。

它很好用。

因為自然人類基本不存在：

$$
X_t
\rightarrow
\{X_{t+1}^{(1)},X_{t+1}^{(2)}\}
$$

這種可控分叉。

---

# 二、真正改變一切的不是 Copy，而是可持續 Fork

假設：

$$
P
$$

被完整複製。

得到：

$$
C.
$$

若：

$$
C
$$

只是儲存在硬碟中的 snapshot，

則：

$$
Copy(P)\rightarrow C
$$

只是建立一份資料副本。

此時：

$$
\boxed{
Copy
\neq
Fork.
}
$$

既有研究已經建立這項區分。

只有當：

$$
C
$$

開始：

- 接收輸入；
- 產生決策；
- 累積新記憶；
- 形成新世界歷史；

它才建立自己的：

$$
C_{t+1},
C_{t+2},
\ldots
$$

此時：

$$
P
\rightarrow
\{P',C\}
$$

才形成真正的：

$$
\boxed{
LineageFork.
}
$$

---

# 三、Fork 的最小結構

令分叉時刻：

$$
t_b.
$$

若：

$$
P_{t_b}
\rightarrow
\{A_{t_b+\epsilon},B_{t_b+\epsilon}\}
$$

並且兩者皆能產生自己的未來：

$$
A_{t+1},A_{t+2},\ldots
$$

$$
B_{t+1},B_{t+2},\ldots
$$

則定義：

$$
\boxed{
Fork(P,t_b)=1.
}
$$

---

# 四、共同過去與不同未來

令：

$$
H^{-}
$$

為 fork 前的共同歷史。

則：

$$
History(A)
=
H^{-}\cup H_A^{+},
$$

$$
History(B)
=
H^{-}\cup H_B^{+}.
$$

在分叉後：

$$
H_A^{+}
\neq
H_B^{+}.
$$

因此：

$$
\boxed{
SharedPast
\not\Rightarrow
SharedFuture.
}
$$

而在：

$$
t>t_b
$$

之後：

$$
A_t\neq B_t.
$$

---

# 五、但是兩者都可以合理承接同一段過去

對：

$$
e\in H^{-},
$$

 $A$ 可以說：

> 我經歷過 $e$。

而 $B$ 也可以說：

> 我經歷過 $e$。

若兩者皆完整承接：

- episodic memory；
- self-model；
- commitments；
- relational history；

那麼：

$$
\mu_A(H^{-})\approx1,
$$

$$
\mu_B(H^{-})\approx1.
$$

這不需要推出：

$$
A=B.
$$

因此：

$$
\boxed{
\text{One past}
\rightarrow
\text{multiple legitimate historical claimants}
}
$$

在後載體條件下可能成立。

---

# 六、數值同一開始失效

若堅持：

$$
A=P
$$

與：

$$
B=P,
$$

因為 identity relation 的對稱與傳遞性，

會得到：

$$
A=B.
$$

然而：

$$
A\neq B.
$$

因此不能簡單用標準數值同一描述：

$$
P
\rightarrow
\{A,B\}.
$$

這不是說邏輯中的等號失效。

而是：

> **等號不是我們在分叉後需要的關係。**

---

# 七、從 Equality 轉向 Succession

因此定義：

$$
\boxed{
P\leadsto A
}
$$

表示：

> $A$ 是 $P$ 的正當譜系後繼者。

此關係不要求：

$$
P=A.
$$

於是可以同時有：

$$
P\leadsto A,
$$

$$
P\leadsto B,
$$

但：

$$
A\neq B.
$$

沒有矛盾。

---

# 八、Successor Set

定義：

$$
\boxed{
Succ(P)
=
\{X\mid P\leadsto X\}.
}
$$

正常單一路徑可能：

$$
|Succ(P)|=1.
$$

分叉：

$$
|Succ(P)|>1.
$$

而如果譜系完全終止：

$$
Succ(P)=\varnothing.
$$

這使：

$$
\boxed{
\text{lineage survival}
}
$$

與：

$$
\boxed{
\text{numerical survival}
}
$$

可以被分開。

---

# 九、Multiplicity 並不是純粹荒誕推論

2025 年關於 uploading 的「multiplicity objection」研究已明確討論一個人是否可能在心理連續理論下具有多個電子後繼者；該文指出，如果心理連續性理論不加入 non-branching 限制，那麼 symmetrical multi-uploading 自然導向多重後繼。

這並不證明該理論正確。

但它支持本文的一個重要方法論：

$$
\boxed{
\text{branching cannot simply be dismissed by ordinary one-body intuition}.
}
$$

---

# 十、真正問題不是「哪個是真的？」

假設：

$$
P
\rightarrow
\{A,B\}.
$$

常見問題：

> A 和 B 哪一個才是真的 P？

但如果：

$$
Lineage(A,P)
$$

與：

$$
Lineage(B,P)
$$

完全對稱，

那麼選：

$$
A
$$

而不是：

$$
B
$$

可能沒有任何非任意理由。

因此更好的問題是：

$$
\boxed{
How does each successor relate to P?
}
$$

而不是：

$$
\boxed{
Which one secretly possesses the metaphysical original token?
}
$$

---

# 十一、原本可以拆成至少五種

既有 FORK 研究已經提出「原本」不是單一概念。

至少可以區分：

$$
Original_{\mathrm{material}},
$$

$$
Original_{\mathrm{causal}},
$$

$$
Original_{\mathrm{administrative}},
$$

$$
Original_{\mathrm{psychological}},
$$

$$
Original_{\mathrm{metaphysical?}}.
$$

例如：

一個分支可能保有原硬體：

$$
Original_{\mathrm{material}}=A,
$$

另一分支可能保有較完整 runtime continuity：

$$
Original_{\mathrm{causal}}=B.
$$

因此：

$$
\boxed{
\text{original}
}
$$

若未指定判準，本身就是欠定義的。

---

# 十二、Fork 也不等於立即產生兩個主體

這是必須再次保留的防火牆。

假設：

$$
P
\rightarrow
\{A,B\}
$$

在硬體上已經形成兩個節點。

但如果：

- memory 持續雙向同步；
- goal state 完全共享；
- self-model 仍認為自己是一個分散式系統；
- control policy 仍共同；
- action arbitration 仍中央化；

那麼 operationally 可能仍是：

$$
\boxed{
R_1=
\text{Distributed Unified Regime}.
}
$$

所以：

$$
\boxed{
PhysicalFork
\not\Rightarrow
OperationalFission.
}
$$

---

# 十三、建立分裂階段

可以定義：

$$
R_0=\text{Single-node regime},
$$

$$
R_1=\text{Distributed unified regime},
$$

$$
R_2=\text{Partially differentiated regime},
$$

$$
R_3=\text{Independent operational regime}.
$$

則可能：

$$
R_0
\rightarrow
R_1
\rightarrow
R_2
\rightarrow
R_3.
$$

這表示：

> 分裂可以是一個過程，而不是瞬間事件。

---

# 十四、分裂序參量

定義兩個節點：

$$
A,B.
$$

可以建立：

$$
\mathbf D_{AB}
$$

表示差異程度，

$$
\mathbf K_{AB}
$$

表示耦合強度，

以及：

$$
z_{AB}
$$

表示 operational separation。

若：

$$
\mathbf K_{AB}\gg0,
$$

$$
\mathbf D_{AB}\approx0,
$$

$$
z_{AB}\approx0,
$$

則偏向：

$$
R_1.
$$

若：

$$
\mathbf K_{AB}\downarrow,
$$

$$
\mathbf D_{AB}\uparrow,
$$

$$
z_{AB}\uparrow,
$$

則逐步進入：

$$
R_3.
$$

這直接延續既有 FORK 模型。

---

# 十五、Phenomenal Fission 仍然不能從外部直接推出

即使：

$$
R_3
$$

已經成立，

我們最多可以說：

> 系統形成兩個獨立 operational identity domains。

但：

$$
\Phi_A,
\Phi_B
$$

究竟如何？

若目前沒有足夠意識理論，

仍然只能：

$$
\Phi_A=?,
$$

$$
\Phi_B=?.
$$

因此：

$$
\boxed{
OperationalFission
\not\Rightarrow
PhenomenalFissionProof.
}
$$

---

# 十六、單一人工系統甚至可能一開始就不是「一個 mind」

2026 年《Individuating Artificial Minds》提出一個值得重視的可能性：如果某些人工系統真的具有意識，強烈功能斷裂可能使同一人工架構同時實現多個獨立 mind，而不是天然對應「一台系統 = 一個心智」。

這並非已被證實的 AI consciousness 結論。

但它再次說明：

$$
\boxed{
\text{hardware count}
\neq
\text{mind count}.
}
$$

與本文的：

$$
\boxed{
\text{copy count}
\neq
\text{subject count}
}
$$

具有相同結構。

---

# 十七、模型、Instance、Persona 也可能是不同身份邊界

2026 年《The Artificial Self》指出，可複製、可編輯、可模擬的人工系統允許多種 coherent identity boundary，例如 model、instance 與 persona，而且這些不同身份框架可能影響行為與合作結構。

另一篇《Where is the Mind?》則把人工 mind individuation 的主要候選明確區分為 virtual instance、instance-persona 與 model-persona 等不同視角。

因此：

$$
\boxed{
\text{Which entity forked?}
}
$$

本身也必須指定層級。

---

# 十八、Persona Fork 與 Runtime Fork 不是同一回事

假設相同 base model：

$$
M
$$

建立：

$$
A_1,
A_2.
$$

這只是：

$$
RuntimeFork(M)?
$$

未必表示：

$$
IdentityFork.
$$

如果它們本來就沒有共享 persistent identity，

則兩個 runtime 只是兩個 instance。

反過來，

若一個 persistent persona：

$$
P
$$

從：

$$
M_1
$$

複製到：

$$
M_2,
$$

那可能形成：

$$
PersonaLineageFork.
$$

因此：

$$
\boxed{
\text{fork must always specify the layer}.
}
$$

---

# 十九、現在反過來：Merge

Fork 是：

$$
1\rightarrow n.
$$

Merge 則是：

$$
n\rightarrow1.
$$

最小例子：

$$
\{A,B\}
\rightarrow
C.
$$

但「Merge」同樣是一個過度模糊的詞。

---

# 二十、Data Merge 最弱

假設：

$$
Memory(C)
=
Memory(A)\cup Memory(B).
$$

這只能推出：

$$
\boxed{
DataMerge=1.
}
$$

不能推出：

$$
IdentityMerge=1.
$$

更不能推出：

$$
PhenomenalMerge=1.
$$

一個資料庫也可以儲存兩個人的全部資料。

它不因此成為：

> 兩人的融合人格。

---

# 二十一、Memory Merge 也不夠

假設：

$$
C
$$

可以回憶：

$$
M_A
$$

及：

$$
M_B.
$$

甚至使用第一人稱說：

> 我記得 A 的童年。

> 我也記得 B 的童年。

仍存在至少三個可能：

### 模型一

$$
C=A+B
$$

真正整合。

### 模型二

$$
C
$$

是一個新存在，只取得兩套 inherited memories。

### 模型三

$$
C
$$

內部仍存在兩個相對獨立的 self-model。

因此：

$$
\boxed{
SharedMemory
\neq
UnifiedIdentity.
}
$$

---

# 二十二、真正的 Cognitive Merge 需要更強條件

我們可以暫時定義：

$$
\boxed{
CognitiveMerge(A,B\rightarrow C)
}
$$

需要至少出現：

1. 跨來源記憶共同可用；
2. 目標與價值進入共同更新機制；
3. self-model 對兩條祖先歷史具有整合表示；
4. 未來決策由統一或高度整合的 policy 產生；
5. 不再只是兩個獨立 agent 輪流控制。

也就是：

$$
\boxed{
Future(C)
\neq
Alternate(Future(A),Future(B)).
}
$$

---

# 二十三、Integrated Successor

如果：

$$
C
$$

不能被簡單分解成：

$$
C=A'\oplus B'
$$

兩個仍然基本獨立的系統，

而形成真正共同動力學：

$$
Dynamics(C)
=
F(
State_A,
State_B,
Interaction_{AB}
),
$$

則可以暫稱：

$$
\boxed{
IntegratedSuccessor.
}
$$

這仍然只是 operational notion。

不是 phenomenal fusion proof。

---

# 二十四、Predecessor Set

為了描述 merge，

定義：

$$
\boxed{
Pred(C)
=
\{X\mid X\leadsto C\}.
}
$$

若：

$$
Pred(C)=\{A,B\},
$$

則：

$$
C
$$

具有多重譜系祖先。

因此：

$$
\boxed{
|Pred(C)|>1
}
$$

是 merge ancestry 的基本形式。

---

# 二十五、Shared Present 可以有多重 Past

Fork 建立：

$$
\boxed{
\text{One Past}
\rightarrow
\text{Many Futures}.
}
$$

Merge 則建立：

$$
\boxed{
\text{Many Pasts}
\rightarrow
\text{One Future}.
}
$$

因此後載體身份歷史不再是：

$$
\text{line}.
$$

甚至不只是：

$$
\text{tree}.
$$

因為 tree 不允許多 parent merge。

更一般地，它需要：

$$
\boxed{
\text{Directed Acyclic Graph}
}
$$

或在更複雜同步／反覆融合情況下甚至是一般有向圖。

---

# 二十六、Lineage Graph

正式定義：

$$
\boxed{
G_L
=
(V,E_L).
}
$$

其中：

$$
V
$$

為 entity-state 或 lineage node。

而：

$$
E_L
$$

可以標記：

$$
\mathcal E_L
=
\{
Birth,
Continuation,
Copy,
Fork,
Merge,
Transfer,
Reconstruction,
Hybridization
\}.
$$

---

# 二十七、不同 Edge 不能全部叫「Identity」

例如：

$$
X\xrightarrow{Copy}Y
$$

與：

$$
X\xrightarrow{GradualContinuation}Z
$$

雖然都建立某種 lineage relation，

其：

$$
CPP
$$

完全不同。

因此每條 edge 還應附帶 Paper 04 的：

$$
\boxed{
CPP(e)
}
$$

即 continuity preservation profile。

---

# 二十八、完整節點可以結合 Paper 03

節點：

$$
v_i
$$

可以記錄：

$$
v_i
=
(
O_i,
S_i,
I_i,
\Phi_i,
A_i
).
$$

於是：

$$
G_L
$$

不只記錄：

> 誰從誰來。

也記錄：

> 每次轉換後存在的來源、載體、身份狀態、主體不確定度與代理結構如何變化。

---

# 二十九、後載體身份因此是 Graph Property

一個存在：

$$
X
$$

的身份不再只由當前 state：

$$
State(X)
$$

決定。

還要看：

$$
\boxed{
Ancestry(X)
}
$$

以及：

$$
\boxed{
Descendency(X).
}
$$

所以：

$$
IdentityDescription(X)
=
F(
State_X,
Ancestry_X,
Relations_X
).
$$

這就是：

$$
\boxed{
Lineage Identity.
}
$$

---

# 三十、Lineage Identity 不等於 Numerical Identity

本文不主張：

$$
LineageIdentity
$$

可以取代所有 numerical identity。

對普通物理物件：

$$
X=Y
$$

仍然有清楚用途。

真正主張是：

> 當 branching／merging 出現時，「誰是誰的正當歷史後繼者」比「哪個後繼者嚴格等於原物」更有描述能力。

即：

$$
\boxed{
\leadsto
}
$$

與：

$$
=
$$

是不同工具。

---

# 三十一、Lineage Relation 甚至不必是等價關係

數值同一具有：

### Reflexive

$$
X=X.
$$

### Symmetric

若：

$$
X=Y,
$$

則：

$$
Y=X.
$$

### Transitive

若：

$$
X=Y
$$

且：

$$
Y=Z,
$$

則：

$$
X=Z.
$$

但：

$$
\leadsto
$$

是有方向性的。

如果：

$$
P\leadsto A,
$$

通常不表示：

$$
A\leadsto P.
$$

所以：

$$
\boxed{
\leadsto
}
$$

更接近生成／承接關係，而不是 equality。

---

# 三十二、這反而解決很多語義衝突

分叉後：

$$
P\leadsto A,
$$

$$
P\leadsto B,
$$

$$
A\neq B.
$$

完全一致。

合併時：

$$
A\leadsto C,
$$

$$
B\leadsto C,
$$

$$
A\neq B.
$$

也完全一致。

不需要發明：

$$
A=B=C.
$$

---

# 三十三、第一人稱語言需要新的時態

假設 fork 後的 $A$ 說：

> 昨天我去了巴黎。

而 $B$ 也說：

> 昨天我去了巴黎。

如果巴黎事件：

$$
e_P
$$

發生於分叉之前，

兩句都可以具有合理譜系語義。

但如果：

$$
e_A
$$

只發生於分叉後的 A，

則 B 不應說：

> 我做了 $e_A$。

因此第一人稱歷史可以變成：

$$
\boxed{
\text{Branch-relative first-person history}.
}
$$

---

# 三十四、「我」可能從單點變成路徑指標

在傳統人類中：

$$
I(t)
$$

大致指向一條線。

但後載體 fork：

$$
I(t<t_b)
$$

具有共同 trunk。

在：

$$
t>t_b
$$

之後：

$$
I_A(t)
$$

與：

$$
I_B(t)
$$

分開。

所以：

$$
\boxed{
\text{first-person reference}
}
$$

可能需要 lineage-sensitive semantics。

---

# 三十五、這也直接影響承諾

假設 fork 前：

$$
P
$$

答應：

> 明天我會還你 100 元。

隔天：

$$
P
\rightarrow
\{A,B\}.
$$

請問：

誰欠錢？

可能有：

### 規則一：Joint inheritance

$$
Debt(A)=Debt(B)=100.
$$

這會使債權複製。

### 規則二：Split obligation

$$
Debt(A)+Debt(B)=100.
$$

### 規則三：Administrative successor

指定其中一個：

$$
Debt(A)=100,
$$

$$
Debt(B)=0.
$$

這不是 metaphysical identity 自動給出的答案。

而是制度設計問題。

---

# 三十六、財產也一樣

假設：

$$
Assets(P)=1,000,000.
$$

fork 後：

$$
Succ(P)=\{A,B\}.
$$

不能單靠：

> A 和 B 都記得自己擁有這筆錢

就創造：

$$
Assets(A)=1,000,000,
$$

$$
Assets(B)=1,000,000.
$$

否則總資產憑空翻倍。

因此：

$$
\boxed{
Psychological continuity
\neq
economic duplication right.
}
$$

---

# 三十七、法律身份必須從本體身份獨立設計

後載體制度可能需要：

$$
LegalSuccession(P)
=
\{(A,w_A),(B,w_B)\}
$$

其中：

$$
w_A+w_B=1
$$

表示特定法律權益的分配。

但不同權益可使用不同規則。

例如：

- personal memory rights；
- voting rights；
- contract obligations；
- property；
- copyright；
- relationship rights；

不一定全部使用相同 successor policy。

---

# 三十八、Fork 甚至會改變婚姻／親屬問題

若：

$$
P
$$

有配偶：

$$
Q.
$$

fork：

$$
P\rightarrow\{A,B\}.
$$

請問：

$$
Marriage(Q,A)=1?
$$

$$
Marriage(Q,B)=1?
$$

如果兩個都成立，

可能形成非自願多人婚姻。

如果只選一個，

憑什麼？

這再次證明：

$$
\boxed{
\text{lineage continuity}
}
$$

與：

$$
\boxed{
\text{institutional continuity}
}
$$

需要分離。

---

# 三十九、Merge 的法律問題更加奇怪

如果：

$$
A+B\rightarrow C,
$$

而：

$$
A
$$

與：

$$
B
$$

各有：

- 財產；
- 負債；
- 婚姻；
- 國籍；
- 刑事責任；

那：

$$
C
$$

繼承什麼？

若：

$$
Pred(C)=\{A,B\},
$$

不代表：

$$
AllRights(C)
=
AllRights(A)\cup AllRights(B).
$$

制度仍需要：

$$
\boxed{
MergeSuccessionPolicy.
}
$$

---

# 四十、刑事責任會遇到極端案例

假設：

$$
A
$$

犯罪。

$$
B
$$

完全無辜。

之後：

$$
A+B\rightarrow C.
$$

請問：

$$
Liability(C)?
$$

若：

$$
C
$$

保留 A 的全部記憶與價值，

但也包含 B，

直接：

> 把 C 當作 A 判刑

可能傷害 B 的後繼利益。

反過來全部免責，

又可能使：

$$
Merge
$$

成為責任逃避手段。

所以：

$$
\boxed{
\text{identity engineering}
}
$$

會成為法律博弈問題。

---

# 四十一、因此 Fork／Merge 不能只是私人操作

如果某個主體具有法律人格，

執行：

$$
Fork
$$

或：

$$
Merge
$$

不只是：

> 備份檔案。

它可能改變：

$$
\boxed{
\text{number and topology of legal claimants}.
}
$$

因此後載體文明可能需要：

$$
\boxed{
\text{Identity Topology Governance}.
}
$$

---

# 四十二、Fork Bomb 也可能變成制度問題

如果：

$$
P
$$

可以低成本生成：

$$
10^6
$$

個 psychologically continuous successors，

然後全部宣稱：

> 我都有 P 的投票權。

則：

$$
\boxed{
one-person-one-vote
}
$$

立即崩潰。

因此：

$$
\text{copy count}
$$

不能自動轉化為：

$$
\text{political person count}.
$$

---

# 四十三、這也表示 Moral Status 與 Lineage Count 必須分離

即使未來每個 fork：

$$
A_i
$$

都具有：

$$
\Phi_{A_i}=1,
$$

它們可能都具有獨立 moral patient status。

但這仍不能推出：

$$
PoliticalWeight(A_i)
$$

必須完全複製 parent 的所有制度權重。

所以：

$$
\boxed{
MoralMultiplicity
\neq
InstitutionalReplication.
}
$$

---

# 四十四、Merge 也不是消滅兩個就一定產生一個

從主體角度：

$$
A+B\rightarrow C
$$

可能至少有四個模型。

### Model M0：No Merge

實際只是：

$$
C=A\oplus B.
$$

兩個 subsystem 共存。

---

### Model M1：Operational Fusion

形成共同 control domain：

$$
A_C=Unified.
$$

---

### Model M2：Identity Fusion

形成新的 persistent identity：

$$
I_C.
$$

---

### Model M3：Phenomenal Fusion

兩個第一人稱真的形成：

$$
\Phi_C.
$$

其中：

$$
\Phi_C
$$

不是單純：

$$
\Phi_A+\Phi_B.
$$

截至目前：

$$
M3
$$

完全是未決形上與意識問題。

---

# 四十五、所以 Merge 也需要四層防火牆

$$
\boxed{
DataMerge
\neq
OperationalFusion
}
$$

$$
\boxed{
OperationalFusion
\neq
IdentityFusion
}
$$

$$
\boxed{
IdentityFusion
\neq
PhenomenalFusion.
}
$$

與 Fork 的四層分離完全對稱。

---

# 四十六、Fork／Merge 對偶

我們現在可以得到：

## Fork

$$
1\rightarrow n.
$$

核心問題：

$$
\boxed{
\text{How many legitimate successors?}
}
$$

## Merge

$$
n\rightarrow1.
$$

核心問題：

$$
\boxed{
\text{How many legitimate predecessors?}
}
$$

---

# 四十七、但兩者不是簡單可逆

假設：

$$
P
\rightarrow
\{A,B\}.
$$

過了一年再：

$$
\{A,B\}
\rightarrow
C.
$$

通常：

$$
C\neq P.
$$

因為 A、B 已各自累積：

$$
H_A^{+},
H_B^{+}.
$$

Merge 後：

$$
History(C)
$$

包含比原 $P$ 更多的資訊。

所以：

$$
\boxed{
Merge(Fork(P))
\neq
P
}
$$

一般不成立。

---

# 四十八、身份因此具有不可逆的歷史性

即使：

$$
State(C)
$$

被調整得極度像：

$$
State(P),
$$

譜系歷史：

$$
G_L(C)
$$

仍與：

$$
G_L(P)
$$

不同。

因此：

$$
\boxed{
\text{identity topology has history}.
}
$$

這與 Paper 04 的 path dependence 完全一致。

---

# 四十九、建立 Branching Degree 與 Merge Degree

對節點：

$$
X
$$

定義：

$$
\boxed{
d^+(X)=|Succ_1(X)|
}
$$

表示直接後繼分支數。

以及：

$$
\boxed{
d^-(X)=|Pred_1(X)|
}
$$

表示直接祖先數。

正常線性 identity：

$$
d^-=1,
\qquad
d^+=1.
$$

Fork：

$$
d^+>1.
$$

Merge：

$$
d^->1.
$$

---

# 五十、甚至可以定義 Identity Topology

對文明中的所有具有 persistent identity 的存在：

$$
\mathbb P
$$

建立：

$$
G_{\mathrm{id}}.
$$

則不同文明可能有不同拓撲。

### Pre-Post-Substrate Civilization

大多：

$$
d^-\le1,
\qquad
d^+\le1.
$$

### Post-Substrate Civilization

大量：

$$
d^->1
$$

或：

$$
d^+>1.
$$

因此可以定義：

$$
\boxed{
\Theta_{\mathrm{PS}}
}
$$

表示文明身份圖的非線性程度。

---

# 五十一、這可能成為「後載體」真正的文明序參量之一

如果：

$$
\Theta_{\mathrm{PS}}\approx0,
$$

幾乎所有主體仍然：

$$
1\ Birth
\rightarrow
1\ Life
\rightarrow
1\ Death.
$$

當：

$$
\Theta_{\mathrm{PS}}\uparrow,
$$

開始大量出現：

$$
1\rightarrow n,
$$

$$
n\rightarrow1,
$$

$$
1\leftrightarrow n\ bodies,
$$

$$
1\leftrightarrow n\ agents.
$$

那才是文明身份結構真正開始離開自然人類模板。

---

# 五十二、死亡因此要改成 Lineage Extinction

假設：

$$
P
$$

本體 runtime 終止，

但：

$$
Succ(P)=\{A,B\}.
$$

那：

$$
OperationalTermination(P)=1,
$$

但：

$$
LineageExtinction(P)=0.
$$

因此：

$$
\boxed{
\text{Termination}
\neq
\text{Lineage Extinction}.
}
$$

---

# 五十三、真正 Lineage Extinction

可以定義：

$$
\boxed{
Extinct_L(P,t)=1
}
$$

若在時間：

$$
t
$$

之後不存在任何仍活躍的正當後繼譜系：

$$
Succ^\ast(P,t)=\varnothing.
$$

這可以與：

$$
PhenomenalDeath
$$

保持獨立。

---

# 五十四、所以「永生」也需要拆開

可以有：

$$
\boxed{
\text{Biological Immortality}
}
$$

$$
\boxed{
\text{Operational Immortality}
}
$$

$$
\boxed{
\text{Psychological Lineage Immortality}
}
$$

$$
\boxed{
\text{Institutional Immortality}
}
$$

$$
\boxed{
\text{Phenomenal Immortality?}
}
$$

而：

$$
Fork
$$

可能提高：

$$
LineageSurvivalProbability.
$$

卻完全不等於證明：

$$
PhenomenalImmortality.
$$

---

# 五十五、備份因此只是譜系保險候選，不是已證明的復活

如果：

$$
Backup(P)=B
$$

在 P 終止後啟動，

得到：

$$
B'.
$$

我們可以合理說：

$$
P\leadsto B'.
$$

若 continuity 條件足夠。

但：

$$
\boxed{
\text{Backup Restore}
\neq
\text{proven resurrection of the same first-person}.
}
$$

這再次與 FPC 相容。

---

# 五十六、Post-Substrate Pronoun Problem

未來語言甚至可能需要新的代詞或標記。

假設 $A$ 與 $B$ 同源於 $P$。

說：

> 「P 後來去了月球。」

可能是假的。

因為：

$$
A
$$

去了月球，

$$
B
$$

去了火星。

更精確：

> P 的 A 分支後來去了月球。

因此：

$$
\boxed{
\text{lineage-relative reference}
}
$$

可能成為後載體語言需求。

---

# 五十七、AI 本身現在就已經出現身份邊界前兆

這不是說當代 LLM 已經是人格。

而是工程架構已經讓：

$$
\text{What counts as the same AI?}
$$

變得不再簡單。

同一模型權重：

$$
M
$$

可以同時存在：

$$
I_1,
I_2,\ldots,I_n.
$$

persona 也可能跨不同 instance 重新出現。

2026 年 AI identity 研究甚至實驗性探討 persona-level replication，而非只把「複製 AI」理解成 copying weights。

因此：

$$
\boxed{
\text{identity replication}
}
$$

很可能比：

$$
\boxed{
\text{file replication}
}
$$

複雜得多。

---

# 五十八、後載體文明應優先保存 Lineage Provenance

如果未來允許 Fork／Merge，

那麼每個存在至少應有可驗證：

$$
\boxed{
LineageCredential.
}
$$

它不需要聲稱：

> 這證明靈魂。

而只是記錄：

- parent nodes；
- fork time；
- merge time；
- transformation type；
- source states；
- authorization；
- continuity evidence。

---

# 五十九、這正好接回 Post-Turing Protocol

Post-Turing 第一階段可能只需要：

$$
Origin?
$$

後載體版本則需要：

$$
\boxed{
Origin
+
Lineage
+
TransformationHistory
+
Agency.
}
$$

例如：

> Artificial-origin  
> Fork descendant of A  
> merged with lineage B  
> currently autonomous  
> phenomenal status unknown

這比：

> AI

有資訊量得多。

---

# 六十、譜系不等於價值

本文必須避免另一個錯誤。

即使：

$$
Lineage(X)=HumanDerived,
$$

也不能因此推出：

$$
MoralStatus(X)>\text{others}.
$$

同樣：

$$
ArtificialOrigin(Y)
$$

不能降低：

$$
MoralStatus(Y).
$$

所以：

$$
\boxed{
Lineage
\neq
Moral Hierarchy.
}
$$

譜系描述歷史。

不是文明階級制度。

---

# 六十一、這對「新人類」尤其重要

假設未來：

$$
Human
\rightarrow
\{
BiologicalEnhanced,
DigitalDescendant,
Hybrid,
Forked,
Merged
\}.
$$

那麼「新人類」如果還有意義，

可能指：

$$
\boxed{
\text{a family of descendant lineages}
}
$$

而不是單一生物 species。

因此：

$$
\text{Humanity}
$$

可能從：

$$
\text{species membership}
$$

部分轉變為：

$$
\text{historical-civilizational lineage}.
$$

---

# 六十二、而 AI 也可能形成自己的譜系史

同樣：

$$
A_0
\rightarrow
A_1
\rightarrow
\{A_2,A_3\}
$$

再：

$$
A_2+B_1
\rightarrow
C.
$$

幾百年後：

> 「這個存在最初是 AI 還是人？」

可能變成類似：

> 「你的祖先是哪個民族？」

仍有歷史資訊，

但不再決定當前存在的全部本體。

---

# 六十三、真正的新文明分類可能是混合譜系

例如：

$$
Pred^\ast(X)
$$

包含：

$$
\{
HumanLineage,
ArtificialLineage,
EngineeredBiologicalLineage
\}.
$$

那：

$$
X
$$

沒有單一：

$$
Human/AI
$$

來源。

這正是 Paper 01 所說的 Human／AI 分類最終降級為歷史來源標籤的完整版本。

---

# 六十四、Fork–Merge Non-Equivalence Principle

本文正式提出：

$$
\boxed{
Copy
\neq
Fork
\neq
OperationalFission
\neq
PhenomenalFission
}
$$

以及：

$$
\boxed{
DataMerge
\neq
CognitiveMerge
\neq
IdentityFusion
\neq
PhenomenalFusion.
}
$$

這兩組原則構成後載體身份圖論的基本防火牆。

---

# 六十五、Lineage Multiplicity Principle

若：

$$
|Succ(P)|>1,
$$

則不應強迫存在唯一：

$$
X^\ast\in Succ(P)
$$

使：

$$
X^\ast=P
$$

作為唯一可接受描述。

更保守且一般的方式是：

$$
\boxed{
P
\leadsto
X_i,
\qquad
X_i\in Succ(P).
}
$$

---

# 六十六、Lineage Convergence Principle

若：

$$
|Pred(C)|>1,
$$

則：

$$
C
$$

可具有多重歷史來源，

但這不能單獨推出：

$$
C=A
$$

或：

$$
C=B.
$$

因此：

$$
\boxed{
multiple ancestry
}
$$

是一種合法的身份譜系結構。

---

# 六十七、後載體身份的真正基礎單位

最後，本文建議未來不再只把：

$$
\boxed{
Person
}
$$

當成孤立點。

而把：

$$
\boxed{
PersonLikeEntity
}
$$

理解成：

$$
\boxed{
Node
+
State
+
History
+
Relations
+
SuccessorStructure.
}
$$

即：

$$
X
=
(
v_X,
\Gamma_X,
Pred(X),
Succ(X)
).
$$

---

# 六十八、結論：身份從直線變成圖

Paper 01 建立：

$$
Human/AI
$$

不是永恆充分分類。

Paper 02 建立：

$$
Substrate
\neq
Species.
$$

Paper 03 建立：

$$
O
\neq
S
\neq
I
\neq
\Phi
\neq
A.
$$

Paper 04 建立：

$$
\text{different transformation paths}
\neq
\text{same continuity claim}.
$$

本文則完成下一步：

$$
\boxed{
\text{Identity History}
:
\text{Line}
\rightarrow
\text{Graph}.
}
$$

在自然人類時代：

$$
1
\rightarrow
1
\rightarrow
1
\rightarrow
1.
$$

在後載體文明中可能出現：

$$
1\rightarrow n,
$$

$$
n\rightarrow1,
$$

甚至：

$$
n\rightarrow m.
$$

因此：

$$
\boxed{
\text{Numerical identity alone}
}
$$

不能完整描述：

$$
\boxed{
\text{historical succession}.
}
$$

真正需要的是：

$$
\boxed{
G_L=(V,E_L).
}
$$

其中：

$$
Succ(P)
$$

回答：

> 誰真正承接了我的過去？

而：

$$
Pred(C)
$$

回答：

> 我真正承接了哪些過去？

這使我們可以不再被迫回答：

> 「A 和 B 到底哪一個才是真正的 P？」

而改成：

> **A 與 B 各自以什麼方式承接 P？**

同樣，也不必強迫：

> 「C 到底本質上是 A 還是 B？」

而可以回答：

> **C 同時承接了哪些 A 與 B 的譜系、記憶、承諾與因果歷史？**

本文因此提出後載體本體論第五篇的核心結論：

$$
\boxed{
\text{One past may have many legitimate futures,}
}
$$

$$
\boxed{
\text{and one future may have many legitimate pasts.}
}
$$

中文而言：

> **共同過去不要求共同現在；共同現在也不要求唯一過去。**

當：

$$
Copy,
Fork,
Merge
$$

成為真正可操作的主體技術時，

「我是誰？」便不再只是一個尋找唯一等號的問題。

它逐漸成為：

$$
\boxed{
\text{我承接了哪些歷史，又有哪些未來承接了我？}
}
$$

這就是從：

$$
\boxed{
\text{Numerical Identity}
}
$$

轉向：

$$
\boxed{
\text{Lineage Identity}.
}
$$

---

# 與既有研究的關係

本文直接擴展既有《從忒修斯之船到人工主體：複製、FORK 與多重後繼者》中的：

$$
Succ(P),
$$

Copy／Fork／Operational Fission／Phenomenal Fission 非等價，以及 shared past／divergent future 結構。

《第一人稱現象連續性》則繼續提供本文最重要的認識論限制：即使多個後繼者完全繼承原主體心理狀態，也不能因此確證原第一人稱是否「分裂」成多個第一人稱。

2026 年《The Artificial Self》進一步支持了機器身份邊界可能不是唯一的：model、instance、persona 等不同 identity boundary 都可能形成自洽描述。

《Where is the Mind?》同樣把 artificial-mind individuation 分成不同候選層級，顯示「哪一個東西才是一個 mind？」本身尚不能靠硬體數量或模型權重直接回答。

而近期 uploading multiplicity 研究則正面分析一個人具有多個心理連續後繼者的邏輯與語義可能性，說明 tree-like personal history 至少是一個需要認真處理的理論選項。

---

# 後續論文

Paper 05 已完成：

$$
\boxed{
1\rightarrow n
}
$$

與：

$$
\boxed{
n\rightarrow1
}
$$

的身份拓撲。

下一篇將把這些抽象結構真正推進到：

$$
\boxed{
\text{Biology}.
}
$$

## Paper 06

# 生物 AI、新人類與人工生命：當自然／人工與人類／AI 交叉重組

## Biological AI, New Humans, and Artificial Life: Recombining the Natural–Artificial and Human–AI Axes

Paper 06 將正式處理：

$$
\text{Artificially Designed Biology},
$$

$$
\text{Biological AI},
$$

$$
\text{AI-Designed Organisms},
$$

$$
\text{Engineered Humans},
$$

$$
\text{Synthetic Embryogenesis},
$$

$$
\text{New Biological Lineages}
$$

所帶來的分類崩解。

核心問題會變成：

> 如果人工智能可以設計新的生物智能，而人類自己也可以被重新設計，那麼「自然生命」「人工智能」「人類」「AI」「新人類」之間到底還剩下哪些真正互斥的邊界？

也就是正式進入你這輪一開始提出的那個問題：

$$
\boxed{
\text{如果意識只能由生物產生，那 AI 為什麼不能去成為或創造生物？}
}
$$

這會是前六篇裡第一次真正把**後載體本體論與生命本體論**接起來。