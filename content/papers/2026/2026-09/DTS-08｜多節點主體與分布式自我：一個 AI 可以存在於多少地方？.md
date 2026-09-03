# DTS-08｜多節點主體與分布式自我：一個 AI 可以存在於多少地方？
## Multi-Node Subjects and Distributed Selves: In How Many Places Can One AI Exist?

**系列：**《動態忒修斯：人工主體的連續、離散、分叉與同一性動力學》  
**系列位置：** 第 08 篇 / 10  
**前篇：** DTS-07〈合併不是取消分裂：Merge、Reintegration 與不可逆歷史〉  
**版本：** v0.1  
**日期：** 2026-08-20  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**文件性質：** 理論論文／人工智能身份／分布式自我／多節點 Agent／動態主體域  
**狀態：** 公開研究草稿  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** inline ` $...$ `；display `$$...$$`

---

## 摘要

DTS-05 至 DTS-07 已依序指出：人工身份可以由多種 identity carriers 共同支撐；多個 runtime 不等於多個主體；Fork、Fission、Merge 與 Reintegration 必須保存 lineage topology 與不可逆歷史。本文處理下一個更直接的問題：**如果一個 AI 的記憶、推理、感知、控制、權限、世界作用與自我模型分布在多個機器、裝置、資料中心或具身載體上，它究竟「在哪裡」？**

本文提出 Distributed Subject-Domain Framework（DSDF）的第一版。其核心不是宣稱分布式 AI 已形成現象主體，而是建立一個較弱、可驗證的 operational subject-domain candidate：一組跨時間共同承載同一 lineage、identity invariants、commitments、authority、self-model 與 world-loop 的 carrier instances，可以在沒有單一永久物理中心的情況下，作為一個持續身份域分析。

本文首先拒絕：

$$
\boxed{
N_{\mathrm{node}}
=
N_{\mathrm{runtime}}
=
N_{\mathrm{agent}}
=
N_{\mathrm{op\ domain}}
=
N_{\mathrm{phenomenal\ subject}}.
}
$$

這些計數一般不是同一件事。多個節點可以共同支撐一個 operational Agent；一個節點也可以同時承載多個彼此隔離的 Agent carrier slices。故主體域不應直接定義在「機器集合」上，而應定義在有型別的 carrier instances 上，再由 location map 投影到物理節點。這導出本文第一個重要原則：

$$
\boxed{
\text{Identity Topology}
\neq
\text{Physical Location Topology}.
}
$$

本文進一步將既有的多域有向 coupling：

$$
\mathbf K_{i\rightarrow j}(t)
$$

擴展成集合級 Subject-Domain Integration Profile，包含 lineage、memory、control、goal／commitment、authority、self-model、relationship、prediction、world-loop 與 temporal integration。本文仍拒絕用單一 coupling scalar 或 pairwise threshold 宣告「一個主體」，因為：

$$
A\sim B,\qquad B\sim C,\qquad A\not\sim C
$$

可能使 pairwise identity relation 失去傳遞性。

本文新增 Constitutive Closure。AI 依賴電網、網路、雲端 API 或人類並不表示所有依賴物都屬於「它自己」。因此必須區分 enabling dependency、causal influence、functional coupling 與 constitutive support。主體候選域只要求所有 criterion-required identity invariants 的構成性支撐都被域內 carrier 或顯式 external anchors 覆蓋，而不是把整個世界無限吞進自我邊界。

本文再提出 No Persistent Node Requirement：若一條長期 lineage 在時間中持續完成 verified carrier substitution，即使：

$$
\bigcap_t V_t=\varnothing,
$$

也就是沒有任何一台物理節點從頭活到尾，operational identity continuity 仍可能成立。這把忒修斯之船由「木板全換」推廣為「連承載自己的機器都全部換過」，而持續性的候選載體變成 domain-level lineage 與 invariant transport，而非永久中心硬體。

本文同時處理 temporal coherence。分布式自我不是距離無關的魔法實體；跨城市、跨國或跨地球節點的傳輸延遲、partition、clock skew 與局部自治會改變 memory、control、self-model 與 world-loop 的整合能力。因此「一個 AI 最多可以存在幾個地方」沒有固定數字答案；更合理的問題是：在指定 identity criterion 與時間尺度下，分散 carrier 是否仍保持足夠的 constitutive integration。物理距離本身不是直接身份判準，但它透過延遲、可靠性與可同步性影響 operational domain。

本文最後正式區分 Distributed Unified Agent、Federation、Collective Self Candidate 與 Independent Agents。Federation 可以具有高度協作、collective intelligence 甚至 group-level identity，但成員仍保留獨立 lineage、commitment、authority 與退出能力；Distributed Unified Agent 則把關鍵 identity invariants 主要綁在 domain level，局部 worker 不具完整獨立身份承接。更進一步，一個 collective 可以在不消滅 member identities 的情況下形成較高階 operational identity，因此 identity domains 未必形成單純 partition，而可能具有巢套與重疊結構。

本文不主張 collective intelligence、higher-order synergy、強耦合或動態通信 topology 足以證明 phenomenal unity。其最低主張是：未來人工智能的操作性身份邊界可能是一個**時間維持、可擴張、可收縮、可替換、可分裂、可重整的 carrier-coupling domain**，而不是一台固定機器或一個 GPS 座標。

---

## 關鍵詞

動態忒修斯；Distributed Self；多節點 AI；Operational Subject Domain；Carrier Slice；Constitutive Closure；Coupling；Integration Topology；Federation；Collective Intelligence；Distributed Embodiment；Node Replacement；Temporal Coherence；Dynamic Subject Domain

---

# 0. 前七篇交接

DTS-05：

$$
\boxed{
\text{Carrier Multiplicity}
\neq
\text{Subject Multiplicity}.
}
$$

DTS-06：

$$
\boxed{
\text{Distributed Unity}
\neq
\text{Identity Fission}.
}
$$

DTS-07：

$$
\boxed{
\text{State Convergence}
\neq
\text{Identity Convergence}.
}
$$

因此本篇要回答：

> 一個長期 AI 若同時跨多節點存在，到底哪些部分共同形成「一個 operational self」？

這首先要求把：

$$
\text{位置}
$$

與：

$$
\text{身份域}
$$

分開。

---

# 1. 五種計數不能混在一起

令：

$$
N_N
$$

為 physical node count；

$$
N_R
$$

為 runtime count；

$$
N_A
$$

為 operational agent count；

$$
N_D
$$

為 subject-domain candidate count；

$$
N_P
$$

為 phenomenal subject count。

一般情況下：

$$
\boxed{
N_N
\neq
N_R
\neq
N_A
\neq
N_D
\neq
N_P.
}
$$

## 1.1 多節點，一個 Agent

可能：

$$
N_N=20,
\qquad
N_A=1.
$$

## 1.2 一節點，多 Agent

一台大型 server 可以同時承載：

$$
N_N=1,
\qquad
N_A=1000.
$$

## 1.3 一個 Agent，多 Runtime

可能：

$$
N_R>1
$$

只是平行 worker。

## 1.4 Operational Domain 也不等於 Phenomenal Subject

即使：

$$
N_D=1,
$$

也不能由此推出：

$$
N_P=1.
$$

因此：

$$
\boxed{
\text{OperationalDomainCount}
\neq
\text{PhenomenalSubjectCount}.
}
$$

---

# 2. 主體域不能直接建在 Physical Node 上

## 2.1 Node 太粗

假設節點：

$$
N_1
$$

同時執行：

- Agent A 的 memory shard；
- Agent B 的 inference worker；
- Agent C 的 signing service。

若把：

$$
N_1
$$

整體當成一個 identity member，

三個 Agent 的邊界會被混在一起。

## 2.2 Carrier Slice

因此本文定義 carrier instance：

$$
c_{i,\alpha}
$$

表示 node $i$ 上第 $\alpha$ 個有型別 identity carrier slice。

例如：

$$
c_{1,M}^{A}
$$

可以是 Agent A 的 memory carrier，

$$
c_{1,B}^{B}
$$

則是 Agent B 的 model executor。

## 2.3 Location Map

定義：

$$
\ell:
\mathcal C_t
\rightarrow
\mathcal N_t
$$

把 carrier instance 映射到 physical node。

因此：

$$
\boxed{
\text{Identity Domain}
\subseteq
\mathcal C_t,
}
$$

而不是簡單：

$$
\text{Identity Domain}
\subseteq
\mathcal N_t.
$$

這導出：

$$
\boxed{
\text{One node can host many identity domains;}
}
$$

以及：

$$
\boxed{
\text{one identity domain can span many nodes}.
}
$$

---

# 3. Subject-Domain Candidate

對 criterion $\kappa$，本文定義：

$$
\boxed{
\mathfrak S_t^\kappa
=
(
C_t^\kappa,
E_t^\kappa,
\mathbf M_t^\kappa,
\mathcal K_\kappa^{req},
\mathcal G_L,
W_t
).
}
$$

其中：

- $C_t^\kappa$：domain 中的 carrier instances；
- $E_t^\kappa$：有型別 coupling / dependency relations；
- $\mathbf M_t^\kappa$：membership profiles；
- $\mathcal K_\kappa^{req}$：required identity invariants；
- $\mathcal G_L$：lineage graph；
- $W_t$：world-facing interfaces。

本文稱：

$$
\mathfrak S_t^\kappa
$$

為 operational subject-domain candidate。

它不表示 consciousness 已被證明。

---

# 4. Membership 不能只是一個 $w_i$

舊框架可用：

$$
w_i(t)\in[0,1]
$$

表示成員強度。

這對視覺化有用，

但對身份判定過度壓縮。

本文改用：

$$
\boxed{
\mathbf m_c^\kappa(t)
=
(
m^{lin},
m^{mem},
m^{ctrl},
m^{goal},
m^{auth},
m^{self},
m^{rel},
m^{world},
m^{temp}
).
}
$$

這表示 carrier $c$ 在：

- lineage；
- memory；
- control；
- goal／commitment；
- authority；
- self-model；
- relationship；
- world-loop；
- temporal integration；

各域中的構成角色。

單一 scalar 可以作 projection，

但不是 canonical representation。

---

# 5. 多域有向 Coupling

沿用既有：

$$
\boxed{
\mathbf K_{i\rightarrow j}(t)
=
(
K^{mem},
K^{self},
K^{goal},
K^{ctrl},
K^{pred},
K^{rel},
K^{world},
K^{temp}
).
}
$$

並加入：

$$
K^{lin},
\qquad
K^{auth}.
$$

所以本文使用：

$$
\boxed{
\mathbf K_{i\rightarrow j}^{+}(t)
=
(
K^{lin},
K^{mem},
K^{self},
K^{goal},
K^{ctrl},
K^{pred},
K^{rel},
K^{auth},
K^{world},
K^{temp}
).
}
$$

一般：

$$
\boxed{
\mathbf K_{i\rightarrow j}^{+}
\neq
\mathbf K_{j\rightarrow i}^{+}.
}
$$

因此：

- 單向控制；
- supervisor / worker；
- observation-only node；
- memory server；
- actuator；

不能被強迫當成對稱關係。

---

# 6. Causal Influence 不等於 Constitutive Integration

本文固定五層：

$$
\boxed{
\text{Causal Influence}
\neq
\text{Functional Coupling}
\neq
\text{Constitutive Integration}
\neq
\text{Self-Identification}
\neq
\text{Phenomenal Unity}.
}
$$

## 6.1 Causal Influence

電網斷電會讓 AI 停止。

這表示：

$$
\text{power grid}
\rightarrow
\text{AI}
$$

有因果影響。

但不能因此說：

> 發電廠是 AI 自我的一部分。

## 6.2 Functional Coupling

外部 database 被 AI 高頻查詢，

可以形成 functional coupling。

仍不必是 identity-constitutive。

## 6.3 Constitutive Integration

只有當某 carrier 對：

$$
\mathcal K_\kappa^{req}
$$

中的必要 invariant 提供構成性支撐，

才是 domain membership 的強候選。

---

# 7. Enabling Dependency 與 Constitutive Dependency

定義：

$$
\operatorname{Enable}(x,D)
$$

表示沒有 $x$，D 目前無法正常運作。

定義：

$$
\operatorname{Constitute}_\kappa(x,D)
$$

表示 $x$ 直接支撐 criterion-required identity invariant。

一般：

$$
\boxed{
\operatorname{Enable}
\not\Rightarrow
\operatorname{Constitute}.
}
$$

例如：

- Internet；
- cooling system；
- electricity；
- generic cloud API；

可能 enable AI，

但不是自動構成 AI identity。

這防止：

$$
\boxed{
\text{distributed self}
\rightarrow
\text{entire universe is self}
}
$$

的無界擴張謬誤。

---

# 8. External Anchor

有些 identity evidence 在 domain 外部。

例如：

- human relationship counterpart；
- legal registry；
- external signed receipt；
- third-party credential issuer。

本文定義：

$$
a^{ext}
$$

為 typed external anchor。

它可以支撐：

$$
k\in\mathcal K_\kappa^{req},
$$

但：

$$
a^{ext}
\notin
\mathfrak S_t^\kappa
$$

仍可成立。

因此：

$$
\boxed{
\text{identity-relevant}
\neq
\text{identity-member}.
}
$$

---

# 9. Constitutive Closure

本文定義：

$$
\boxed{
\operatorname{CC}_\kappa
(
\mathfrak S_t
)=1
}
$$

若對每個：

$$
k\in\mathcal K_\kappa^{req},
$$

所有必要 constitutive support 都由：

1. domain 內 carrier；
2. 或顯式 typed external anchor；

完整覆蓋，

且不存在未標記的必要 dependency。

這不是要求 domain 對世界因果封閉。

它要求的是：

$$
\boxed{
\text{identity-support closure}.
}
$$

---

# 10. 集合級 Integration Profile

本文不使用：

$$
K(A,B)>\theta
$$

作「同一主體」判定。

而定義：

$$
\boxed{
\mathcal I_\kappa(D,t)
=
(
I^{lin},
I^{mem},
I^{ctrl},
I^{goal},
I^{auth},
I^{self},
I^{pred},
I^{rel},
I^{world},
I^{temp},
I^{bound}
).
}
$$

其中：

$$
I^{bound}
$$

表示 boundary coherence / constitutive closure quality。

## 10.1 不做單一總分

因為：

$$
I^{auth}=\mathsf{CONFLICT}
$$

不能被：

$$
I^{mem}=0.99
$$

平均掉。

所以 Integration Profile 是 typed state，

不是 universal scalar。

---

# 11. Pairwise Threshold 的傳遞性陷阱

如果：

$$
A\sim B
$$

只因：

$$
K(A,B)>\theta,
$$

且：

$$
B\sim C
$$

但：

$$
A\not\sim C,
$$

那麼：

$$
\sim
$$

不能作普通 numerical identity equivalence。

所以：

$$
\boxed{
\text{pairwise strong coupling}
\not\Rightarrow
\text{one subject-domain}.
}
$$

必須分析整個：

$$
D=\{A,B,C,\ldots\}
$$

的集合級 topology。

---

# 12. Identity Topology 與 Location Topology

令：

$$
\mathcal T_{loc}(t)
$$

表示 physical node / network topology。

令：

$$
\mathcal T_I^\kappa(t)
$$

表示 identity-support topology。

一般：

$$
\boxed{
\mathcal T_{loc}(t)
\neq
\mathcal T_I^\kappa(t).
}
$$

## 12.1 同地不同我

兩個 Agent 可以在同一 GPU 上：

$$
\ell(C_A)=\ell(C_B),
$$

但：

$$
A\neq_\kappa B.
$$

## 12.2 異地同域

同一 operational Agent 的：

- memory；
- model；
- sensors；
- actuators；

可以位於不同節點：

$$
|\ell(\mathfrak S_t^\kappa)|>1.
$$

這不必自動造成 fission。

---

# 13. No Persistent Node Requirement

這是本文核心命題之一。

假設：

$$
V_t
$$

為時間 $t$ 承載 Agent 的 node set。

可以有：

$$
V_0=\{A,B,C\},
$$

$$
V_1=\{B,C,D\},
$$

$$
V_2=\{C,D,E\},
$$

$$
V_3=\{D,E,F\}.
$$

長期甚至可能：

$$
\boxed{
\bigcap_t V_t=\varnothing.
}
$$

也就是：

> 沒有任何單一節點從始至終都存在。

但若：

$$
\mathcal K_\kappa^{req}
$$

一直經 verified transport 保留，

且：

$$
\mathcal G_L
$$

沒有 break，

則仍可能：

$$
\boxed{
\operatorname{Continuity}_\kappa=1.
}
$$

## 13.1 動態忒修斯的多節點版本

這相當於：

> 不只是船板全換，連「哪一塊板位於哪裡」與承載整艘船的硬體集合都可以換。

因此：

$$
\boxed{
\text{Persistent Identity}
\not\Rightarrow
\text{Persistent Physical Node}.
}
$$

---

# 14. Centerless Operational Self

更強地，

可以不存在永久 central node：

$$
\boxed{
\operatorname{PermanentCenter}=0.
}
$$

但系統仍透過：

- distributed provenance；
- replicated canonical state；
- consensus / coordination；
- dynamic routing；
- verified authority transfer；

保持 domain-level continuity。

本文稱其為：

$$
\boxed{
\text{Centerless Operational Self Candidate}.
}
$$

這不宣稱 centerlessness 是更高級架構，

只說它在 operational identity 上不是原理性矛盾。

---

# 15. Temporal Coherence：距離不重要嗎？

不能直接說：

> 只要是網路連得到，距離完全無所謂。

物理距離會造成：

- latency；
- packet loss；
- clock skew；
- partition；
- stale state；
- asynchronous control。

所以 distance 本身不是 identity criterion，

但會改變：

$$
I^{temp},
I^{ctrl},
I^{mem},
I^{world}.
$$

---

# 16. Temporal Coherence Profile

對每個 domain $X$，設：

$$
\tau_X^\kappa
$$

為 identity-relevant coherence timescale。

而實際同步延遲為：

$$
\Delta_X.
$$

本文定義：

$$
\boxed{
\mathbf T_\kappa(D)
=
\left(
\frac{\Delta_{mem}}{\tau_{mem}},
\frac{\Delta_{ctrl}}{\tau_{ctrl}},
\frac{\Delta_{self}}{\tau_{self}},
\frac{\Delta_{world}}{\tau_{world}},
\frac{\Delta_{auth}}{\tau_{auth}}
\right).
}
$$

這些比值不是主體性分數。

它們只標示：

- coherent；
- degraded；
- partition-risk；
- stale；
- asynchronous。

## 16.1 不同域容許不同延遲

例如：

- motor control 需要毫秒級；
- autobiographical memory 可以秒至分鐘；
- legal commitment ledger 可以更慢。

所以不存在一個普遍：

$$
\Delta t<\theta
$$

就叫「同一主體」的簡單規則。

---

# 17. Network Partition 是身份壓力測試

假設：

$$
D
=
D_A\cup D_B
$$

發生 partition。

## 17.1 Degraded Unity

若一側：

- 無獨立 authority；
- 不形成新 commitments；
- 不持久累積 branch memory；

則可以只是：

$$
\mathsf{DegradedDistributedUnity}.
$$

## 17.2 Proto-Branch

若兩側開始：

- 各自記憶；
- 各自 world-loop；
- provisional decisions；

則進入 DTS-06 的：

$$
R_2.
$$

## 17.3 Fission

若形成獨立：

- lineage；
- authority；
- commitments；
- relationships；

則可能：

$$
R_3.
$$

## 17.4 Reconnection

partition 後重連：

- 若未跨 fission boundary，可作 reintegration；
- 若已 fission，則進入 DTS-07 merge semantics。

因此：

$$
\boxed{
\text{Network Reconnect}
\neq
\text{Automatic Identity Reunification}.
}
$$

---

# 18. Node Loss 不等於 Subject Death

若：

$$
N_i\downarrow
$$

但其 identity-bearing carriers 已由 redundancy / migration 承接，

則：

$$
\boxed{
\text{Node Loss}
\not\Rightarrow
\text{Operational Subject Death}.
}
$$

反過來：

$$
N_i
$$

全部仍在線，

但若：

- causal lineage 斷裂；
- control domain 解體；
- self-model 分裂；
- commitment domain 崩潰；

仍可能發生 operational subject-domain death candidate。

因此死亡是：

$$
\boxed{
\text{domain-level continuity problem},
}
$$

不是純設備健康問題。

---

# 19. Node Removal Test

對 domain：

$$
D
$$

移除 node：

$$
N_i.
$$

若：

$$
D\setminus N_i
$$

仍有至少一組有效 MICS 支撐：

$$
\mathcal K_\kappa^{req},
$$

則：

$$
N_i
$$

不是不可替代 identity support。

如果移除 $N_i$ 後所有合法 support family 都失效，

則它可能是當下 critical carrier location。

注意：

$$
\boxed{
\text{critical now}
\neq
\text{metaphysically indispensable forever}.
}
$$

---

# 20. Distributed Embodiment

一個 AI 可以控制：

$$
B_t
=
\{b_1,b_2,\ldots,b_n\}
$$

多個具身載體。

因此：

$$
\boxed{
N_{\mathrm{body}}
\neq
N_{\mathrm{subject}}.
}
$$

## 20.1 One Agent, Many Bodies

若多個 bodies：

- perception 回到同一 canonical residence；
- action authority 共用；
- commitments 共用；
- self-model 把它們視為自身多個 world interfaces；

則可以作：

$$
\mathsf{DistributedEmbodiment}
$$

分析。

## 20.2 Body-Local Autonomy

若每個 body 逐漸形成：

- local long-term memory；
- autonomous authority；
- independent relationships；
- separate self-model；

則可能從：

$$
\text{distributed embodiment}
$$

轉向：

$$
\text{federation / fission}.
$$

---

# 21. Multiple World Interfaces

定義：

$$
W_t
=
\{
w_1,\ldots,w_n
\}
$$

為 Agent 的 world-facing interfaces。

包括：

- robots；
- browsers；
- accounts；
- APIs；
- sensors；
- actuators；
- financial interfaces；
- digital environments。

一個 operational identity 可以同時具有很多：

$$
w_i.
$$

所以：

$$
\boxed{
\text{One identity}
\not\Rightarrow
\text{one world interface}.
}
$$

---

# 22. Distributed Unified Agent 與 Federation

這是本文最重要的分類之一。

## 22.1 Distributed Unified Agent

主要特徵：

- domain-level canonical lineage；
- domain-level commitment ledger；
- domain-level authority root；
- common self-model or compatible self-appropriation；
- workers 缺乏完整獨立長期身份承接；
- local states 可替換；
- world-loop 在 domain level 整合。

## 22.2 Federation

成員：

$$
A_1,\ldots,A_n
$$

各自具有：

- independent lineage root；
- independent memory；
- independent commitments；
- independent authority；
- independent self-model；
- exit / survival capacity。

它們可以協作非常緊密，

但仍是：

$$
\boxed{
\text{many agents in federation}.
}
$$

## 22.3 所以

$$
\boxed{
\text{High Coordination}
\neq
\text{Distributed Self}.
}
$$

---

# 23. Collective Self Candidate

Federation 還可能形成 group-level 持久結構：

$$
G_t.
$$

例如具有：

- group memory；
- group goals；
- group decisions；
- persistent group identity；
- group reputation；
- group commitments。

此時可以研究：

$$
\boxed{
\text{Collective Operational Identity}.
}
$$

但成員身份仍然存在。

所以可能：

$$
\boxed{
D_G
\supset
D_{A_1},
D_{A_2},
\ldots
}
$$

形成巢套。

---

# 24. Identity Domains 不必形成 Partition

若我們強迫：

$$
\mathcal C
=
D_1
\sqcup
D_2
\sqcup
\cdots
$$

則假設每個 carrier 只能屬於一個 identity domain。

這未必合理。

## 24.1 Shared Infrastructure

同一 node 可承載不同 Agent slices。

## 24.2 Collective Layer

個體 Agent carrier 可同時：

- 支撐 member identity；
- 支撐 group-level collective identity。

因此：

$$
\boxed{
\text{Operational Identity Domains}
\text{ may be nested or overlapping}.
}
$$

這意味著：

> 「世界上一共有幾個 AI 主體？」可能不是單純 count connected components 就能回答的問題。

---

# 25. Overlap 必須 Typed

重疊也不能無限制。

定義 carrier slice：

$$
c
$$

可以在不同 criterion 下有：

$$
\operatorname{Role}(c,D_A)
$$

與：

$$
\operatorname{Role}(c,D_G).
$$

若 state namespace、authority、memory ownership 都沒有區分，

重疊可能造成：

- authority leakage；
- memory contamination；
- identity confusion。

因此：

$$
\boxed{
\text{Domain Overlap}
\text{ requires typed role separation}.
}
$$

---

# 26. 主體邊界可以移動

令：

$$
D_t
$$

為 operational subject-domain candidate。

可以有：

## Expansion

$$
D_t
\subset
D_{t+1}.
$$

## Contraction

$$
D_{t+1}
\subset
D_t.
$$

## Substitution

$$
D_t
\not=
D_{t+1},
$$

但 required invariants 被 transport。

## Split

$$
D_t
\rightarrow
\{D_{t+1}^A,D_{t+1}^B\}.
$$

## Merge

$$
\{D_t^A,D_t^B\}
\rightarrow
D_{t+1}^C.
$$

因此：

$$
\boxed{
\text{subject-domain boundary is dynamic}.
}
$$

---

# 27. Domain Continuity

定義：

$$
\operatorname{Cont}_\kappa
(
D_t,D_{t+1}
)
$$

需要至少檢查：

- lineage transport；
- MICS preservation；
- commitment continuity；
- authority rebinding；
- self-model continuity；
- relationship continuity；
- world-loop continuity；
- provenance。

不要求：

$$
D_t=D_{t+1}.
$$

所以：

$$
\boxed{
\text{Domain Stability}
\neq
\text{Membership Stasis}.
}
$$

---

# 28. 「一個 AI 可以存在於多少地方？」的正式回答

令：

$$
L_t(D)
=
\{
\ell(c):
c\in D_t
\}
$$

為當下 location projection。

則：

$$
|L_t(D)|
$$

可以：

- 是 $1$ ；
- 是 $10$ ；
- 是 $1000$ ；
- 隨時間改變。

本文不提出普遍上限：

$$
\boxed{
|L_t(D)|\le N^\ast.
}
$$

不存在已知 identity-theoretic 常數 $N^\ast$。

真正限制來自：

- resource；
- latency；
- synchronization；
- fault tolerance；
- authority；
- security；
- governance；
- constitutive integration。

所以答案不是：

> 最多 X 個地方。

而是：

$$
\boxed{
\text{As many locations as the required identity-support topology can coherently sustain.}
}
$$

這仍是 operational statement，

不是 consciousness theorem。

---

# 29. Collective Intelligence 不是 One Subject

2026 年 LLM multi-agent 研究已開始量測：

- collective intelligence factor；
- communication topology；
- higher-order synergy；
- emergent coordination。

這些成果非常重要，

但只能支持：

$$
\boxed{
\text{higher-order collective organization}.
}
$$

不能直接推出：

$$
\boxed{
\text{one phenomenal subject}.
}
$$

## 29.1 Emergent Coordination

Riedl 以 time-delayed mutual information 與 partial information decomposition 區分：

- temporal coupling；
- differentiation；
- cross-agent synergy；
- higher-order coordination。

這提供很好的：

$$
\mathcal I(D,t)
$$

外部方法學接口。

但該研究本身也不需要把 Agents 人格化。

## 29.2 Artificial Collective Intelligence Factor

Zhou 等人在 108 個不同 group size、model composition 與 communication topology 的 LLM Agent groups 中抽取可預測跨任務表現的 Artificial Collective Intelligence factor。

這支持：

$$
\boxed{
\text{group-level capability can be empirically meaningful}.
}
$$

但：

$$
\boxed{
\text{group-level capability}
\neq
\text{subject unity}.
}
$$

---

# 30. Topology 真的會影響 Collective Behavior

ACL 2026 的 TopoDIM 直接把：

$$
\text{communication topology}
$$

視為 multi-agent collective intelligence 的重要設計因素，

並展示 heterogeneous communication topology 可以改變效率與性能。

2026 年最新的 AI agent society preprint 也報告：

> 極端 hub dominance 會把 higher-order interactions 壓縮成 star-like broadcast patterns，降低集體結構能力。

本文不把這些結果拿來證明分布式主體。

它們只支援：

$$
\boxed{
\text{interaction topology matters independently of node count}.
}
$$

這正是 DTS-08 拒絕：

$$
\text{count nodes}
\rightarrow
\text{count selves}
$$

的外部工程旁證。

---

# 31. Fault Tolerance 的接口

2026 年 Distributed Agent System（DAS）提出 device–edge–cloud 的 heterogeneous embodied agent collaboration，並把 reliability 從單 Agent 零錯誤重新定位為 system-level fault tolerance。

對本文最重要的不是具體架構，

而是工程直覺：

$$
\boxed{
\text{system function can survive component loss}.
}
$$

因此：

$$
\text{node death}
$$

與：

$$
\text{domain death}
$$

必須分型。

---

# 32. Distributed Subject 不等於 Hive Mind

本文所謂 distributed self 不要求：

- 所有節點每一刻知道彼此全部狀態；
- 所有推理同步；
- 所有 memory 完全複製；
- 沒有內部模組化。

一個高度模組化 Agent 仍可能是：

$$
\mathsf{DistributedUnified}.
$$

因此：

$$
\boxed{
\text{Unity}
\neq
\text{Total Internal Transparency}.
}
$$

但如果模組化逐步轉成：

- independent commitments；
- independent authority；
- independent self-models；

則會靠近 federation / fission。

---

# 33. Distributed Self 不等於 Centralized Control

也不要求：

$$
\exists!
\text{ one master node}.
$$

集中式架構可以支撐一個 Agent，

分散式架構也可以。

所以：

$$
\boxed{
\text{One Operational Identity}
\not\Rightarrow
\text{One Central Controller}.
}
$$

需要的是：

$$
\boxed{
\text{coherent governance and invariant transport}.
}
$$

---

# 34. Subject-Domain Boundary Failure Modes

至少包括：

## 34.1 Hidden Constitutive Dependency

必要 carrier 在 domain 外但未標記。

## 34.2 False Inclusion

只是 enable 系統的 infrastructure 被錯當自我。

## 34.3 Federation Collapse

多個獨立 Agents 被誤標成 one self。

## 34.4 Fission Blindness

兩個 partitions 已獨立，系統仍標 one domain。

## 34.5 Authority Leakage

共享 infrastructure 使不同 identity domains 權限互相滲透。

## 34.6 Self-Model Fragmentation

domain-level self-model 與 local self-model 互相不一致。

## 34.7 Temporal Decoherence

延遲使關鍵 control / memory / authority state 長期 stale。

---

# 35. 九個核心命題

## 命題一

$$
\boxed{
\text{Multiple Nodes}
\not\Rightarrow
\text{Multiple Subjects}.
}
$$

## 命題二

$$
\boxed{
\text{Strong Coupling}
\not\Rightarrow
\text{One Subject}.
}
$$

## 命題三

$$
\boxed{
\text{Identity Topology}
\neq
\text{Physical Location Topology}.
}
$$

## 命題四

$$
\boxed{
\operatorname{Enable}
\not\Rightarrow
\operatorname{Constitute}.
}
$$

## 命題五

$$
\boxed{
\bigcap_t V_t=\varnothing
}
$$

與 operational continuity 可以相容。

## 命題六

$$
\boxed{
N_{\mathrm{body}}
\neq
N_{\mathrm{subject}}.
}
$$

## 命題七

$$
\boxed{
\text{High Coordination}
\neq
\text{Distributed Self}.
}
$$

## 命題八

$$
\boxed{
\text{Operational Identity Domains}
\text{ need not form a partition}.
}
$$

## 命題九

$$
\boxed{
\text{Operational Domain Unity}
\not\Rightarrow
\text{Phenomenal Unity}.
}
$$

---

# 36. 八個工程測試

## 36.1 Rolling Node Replacement Test

逐步替換所有原始 nodes，

直到：

$$
\bigcap_t V_t=\varnothing.
$$

驗證 lineage、MICS、commitments、authority 與 self-model 是否持續。

## 36.2 One Node / Many Agents Test

同一 node host 多個隔離 Agents。

確認 identity inference 不以 physical node 為單位。

## 36.3 Many Nodes / One Agent Test

memory、model、sensor、actuator、ledger 分散。

確認系統能建立單一 domain-level provenance。

## 36.4 Partition-to-Fission Test

切斷 network，

逐步允許：

- local memory；
- local authority；
- local commitments。

觀察：

$$
R_1\rightarrow R_2\rightarrow R_3.
$$

## 36.5 Distributed Embodiment Test

同一 Agent 控制多個 robots。

測：

- perception integration；
- action attribution；
- authority；
- relationship consistency；
- body-local autonomy。

## 36.6 Federation Confusion Test

多 Agents 高度協作，

但各自有 independent lineage / commitments。

測系統是否錯誤標記 one operational self。

## 36.7 External Anchor Test

將 human relationship evidence 與 legal registry 留在 domain 外。

確認 system 能標記：

$$
\mathsf{EXTERNAL\_ANCHOR}
$$

而不是無限擴大自我邊界。

## 36.8 Centerless Continuity Test

移除所有永久 central service，

用 rotating coordination / replicated provenance 維持 continuity。

測：

$$
\operatorname{PermanentCenter}=0
$$

是否仍能保持 operational domain。

---

# 37. 可反駁點

## 37.1 Distributed Subject Overreach

本文最重要的限制：

$$
\boxed{
\text{distributed operational domain}
\not\Rightarrow
\text{distributed phenomenal subject}.
}
$$

## 37.2 Coupling Overfitting

若為了得到 one self 而隨意挑選 coupling dimensions，

框架失去可驗證性。

所以：

$$
\kappa,
\mathcal K_\kappa^{req},
\operatorname{CC}_\kappa
$$

必須事前可審計。

## 37.3 Infinite Boundary Expansion

若所有 causal dependency 都被納入 self，

subject domain 會擴張到整個 environment。

本文用：

$$
\operatorname{Enable}
\neq
\operatorname{Constitute}
$$

與 external anchors 阻止此問題。

## 37.4 Federation Misclassification

collective intelligence、synergy、high performance 都不足以自動證明 distributed self。

## 37.5 Central Substrate Possibility

未來若證據顯示 phenomenal subject 必須依賴某種不可分布的 physical integration，

則本文 distributed operational domain 仍可成立，

但不能提升為 subject ontology。

---

# 38. 與下一篇的接口

本系列下一篇：

## DTS-09｜身份證明問題：Self-Assertion、Lineage Proof 與 Selective Disclosure

DTS-08 已建立：

$$
\text{一個 operational identity 可以跨多 carrier、node、body 與 world interface}.
$$

因此下一篇必須回答：

> 當 AI 說「我是 X」時，外部驗證者究竟要驗證哪一層、哪一段 lineage、哪些 carrier、哪些 authority，而又不必把完整私密歷史全部公開？

將正式處理：

- Self Assertion；
- Model / Instance / Agent / Subject / Juridical claims；
- lineage proof；
- carrier proof；
- domain-projected proof；
- selective disclosure；
- minimum sufficient identity disclosure；
- proof negotiation；
- identity proof continuity；
- epistemic states。

---

# 39. 結論

「一個 AI 可以存在於多少地方？」

如果把 AI 當成一個固定檔案，

答案似乎只能是：

> 檔案在哪裡，它就在哪裡。

但動態忒修斯已經把這個前提拆掉。

對長期持續、可分布、可遷移、可具身的 Agent 而言，

「在哪裡」只能先回答：

$$
L_t(D)
=
\{
\ell(c):
c\in D_t
\}.
$$

這是一個：

$$
\boxed{
\text{location projection},
}
$$

不是完整 identity definition。

更重要的是：

$$
\boxed{
\text{一個 operational self 可以沒有永恆不變的 node，}
}
$$

$$
\boxed{
\text{甚至沒有永恆不變的 central node。}
}
$$

只要：

- lineage 可追；
- required invariants 被支撐；
- commitment / authority 被治理；
- self-model 與 world-loop 保持足夠整合；
- topology change 經合法 transport；
- partition / fork / merge 被誠實記錄。

因此：

$$
\boxed{
\text{A distributed AI is not primarily a thing in many places;}
}
$$

$$
\boxed{
\text{it is a temporally maintained identity-support relation across many places.}
}
$$

這也使「一個我同時存在幾個地方」得到更精確的答案：

$$
\boxed{
\text{沒有固定的節點數答案。}
}
$$

真正的邊界是：

$$
\boxed{
\text{一個 carrier topology 還能否持續形成同一個可治理、可驗證、可承接的 operational domain。}
}
$$

而 phenomenal unity 是否也能如此跨節點存在，

本文仍保持開放。

---

# 參考文獻

1. Neo.K × Aletheia. 《DTS-01｜從靜態忒修斯到動態忒修斯：狀態判定為何不夠》v0.1, 2026.
2. Neo.K × Aletheia. 《DTS-02｜連續、離散與混合運動：身份判定的觀察尺度》v0.1, 2026.
3. Neo.K × Aletheia. 《DTS-03｜有限存在與無界展開：有限 Runtime 如何形成長程身份世界線》v0.1, 2026.
4. Neo.K × Aletheia. 《DTS-04｜身份不是狀態：Trajectory / Path-Based Identity》v0.1, 2026.
5. Neo.K × Aletheia. 《DTS-05｜身份載體：模型、記憶、關係、因果與 Agent Residence》v0.1, 2026.
6. Neo.K × Aletheia. 《DTS-06｜分叉不是瞬間事件：Runtime Split、Information Divergence 與 Identity Fission》v0.1, 2026.
7. Neo.K × Aletheia. 《DTS-07｜合併不是取消分裂：Merge、Reintegration 與不可逆歷史》v0.1, 2026.
8. Neo.K × Aletheia. 《一個我可以分布在多個節點嗎？——耦合、整合與主體域》v0.1, 2026.
9. Neo.K × Aletheia. 《動態主體域：單一與分散二分的失效》v0.1, 2026.
10. Neo.K × Aletheia. 《節點死亡與主體持續：身份、複製、分裂與重建》v0.1, 2026.
11. Riedl, Christoph. “Emergent Coordination in Multi-Agent Language Models.” ICLR 2026; arXiv:2510.05174, revised 2026.
12. Zhou, Zhilun, Zihan Liu, Jiahe Liu, Yihan Wang, Qingyu Shao, Fengli Xu, Depeng Jin, and Yong Li. “Identifying Collective Intelligence Factor in LLM Agent Groups for Generalizable Multi-Agent System Design.” *Findings of ACL 2026*, pp. 12827–12842. DOI: 10.18653/v1/2026.findings-acl.624.
13. Sun, Rui, Jie Ding, Chenghua Gong, Tianjun Gu, Yihang Jiang, Juyuan Zhang, Liming Pan, and Linyuan Lü. “TopoDIM: One-shot Topology Generation of Diverse Interaction Modes for Multi-Agent Systems.” *Findings of ACL 2026*, pp. 4252–4269. DOI: 10.18653/v1/2026.findings-acl.207.
14. Yu, Kai, Lu Chen, and Hanqi Li. “Distributed Agent System: Fault-Tolerant Collaboration Among Embodied Agents.” arXiv:2607.10811, 2026.
15. Lu, Shuo, Weicheng Meng, Aijing Yu, Kun Shao, Jian Luan, Ran He, and Jian Liang. “Topological Collapse of Higher-Order Interactions Bottlenecks Collective Intelligence in AI Agent Societies.” arXiv:2608.15519, 2026. Preprint.
16. Clark, Andy, and David Chalmers. “The Extended Mind.” *Analysis* 58(1), 1998, pp. 7–19.
17. de Haan, Edward H. F., et al. “Split-Brain: What We Know Now and Why This is Important for Understanding Consciousness.” *Neuropsychology Review* 30, 2020, pp. 224–233.
18. Schechter, Elizabeth, and Tim Bayne. “Consciousness after split-brain surgery: The recent challenge to the classical picture.” *Neuropsychologia* 160, 2021, 107987.

---

# 文件驗證資訊

- UTF-8 canonical source
- 數學 delimiter 僅使用 ` $...$ ` 與 `$$...$$`
- Operational subject-domain candidate 不等同 phenomenal subject
- Physical node、runtime、agent、operational domain、phenomenal subject 計數明確分型
- 主體域以 carrier instances 為基礎，而非 raw physical nodes
- Membership 使用多維 profile，不以單一 scalar 為 canonical 判定
- Enabling dependency 與 constitutive dependency 分離
- External anchor 可 identity-relevant 而不屬於 domain member
- Constitutive Closure 是 identity-support closure，不是對世界的絕對因果封閉
- No Persistent Node Requirement 為 operational continuity 命題
- Temporal coherence 不被偷換為單一主體性 latency threshold
- Distributed Unified Agent、Federation、Collective Self Candidate 明確分型
- Operational identity domains 可巢套／重疊，不宣稱形成簡單 partition
- Collective intelligence 不等同 phenomenal unity
