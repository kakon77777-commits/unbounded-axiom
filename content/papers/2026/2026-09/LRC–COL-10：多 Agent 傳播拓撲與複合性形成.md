# LRC–COL-10：多 Agent 傳播拓撲與複合性形成
## Multi-Agent Transmission Topology and the Emergence of Compositional Structure

**系列：LRC–COL — Language–Reality Coupling & Composite Operator Language**  
**中文：語言—現實耦合與複合算子語言系列**  
**版本：v0.1**  
**日期：2026-08-21**
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  

---

## 摘要

LRC–COL-09 將複合算子語言的傳播寫成代際鏈：

$$
\mathcal L_g
\rightarrow
A_{g+1}
\rightarrow
\mathcal L_{g+1},
$$

並建立 transmission bottleneck、learnability、fidelity、expressivity、innovation 與 degeneration 的交換關係。然而，真實多 Agent 系統通常不是一條線性 teacher–learner chain。多個 Agents 可能同時相互傳播、局部協作、競爭、分群、形成中心節點、建立 bridge nodes，甚至根據任務即時重建 communication graph。

因此，真正的語言傳播對象應提升為：

$$
\boxed{
G_T(t)
=
(V_t,E_t,W_t,R_t),
}
$$

其中：

- $V_t$：Agents；
- $E_t$：communication edges；
- $W_t$：edge weight / bandwidth / trust；
- $R_t$：role / direction / protocol。

本文提出 **Transmission Topology as a Language-Evolution Operator**：communication topology 不只是資訊經過的被動管道，而會決定正確資訊、錯誤資訊、少數創新、局部 shorthand、semantic drift 與 common conventions 如何被放大或抑制。

近期研究為此提供直接外部錨點。2025 年 EMNLP 對 LLM multi-agent communication topology 的因果分析顯示，moderately sparse topologies 往往能在抑制錯誤傳播與保留有益資訊擴散之間取得更好平衡；2024 年 EMNLP 的 sparse multi-agent debate 亦顯示，稀疏 communication 可在顯著降低計算成本的同時達到相當或更好的 performance。另一方面，2024 年 Cognitive Science 的 network-language model 發現，network path length 與 clustering coefficient 對 interindividual linguistic variation 有強影響，較不連通、具有小型社群結構的 populations 更容易形成 variation。2024 年 one-to-many emergent communication 研究則顯示，單純增加 listeners 並不自動產生更高 compositionality；listener interests 的差異與彼此 coordination pressure 才是重要驅動。

本文因此把 multi-agent topology 的語言效應拆成五個核心壓力：

$$
\boxed{
\text{Diffusion}
+
\text{Error Propagation}
+
\text{Diversity Preservation}
+
\text{Coordination Pressure}
+
\text{Transmission Cost}.
}
$$

本文定義 Information Diffusion Gain、Error Amplification Factor、Topology Diversity Retention、Dialect Modularity、Bridge Dependence、Consensus Correlation、Semantic Diameter、Kernel Connectivity 與 Topology Utility，並比較 chain、star、full mesh、sparse mesh、hierarchy、modular communities、rotating teacher、federated topology 與 task-adaptive dynamic topology。

本文提出一個關鍵架構猜想：

$$
\boxed{
\text{Common Semantic Kernel}
+
\text{Local Dialects}
+
\text{Sparse Semantic Bridges}
}
$$

可能比「全體 Agent 使用完全相同且全連通的單一語言」更有擴展性。局部 communities 可保留 domain-specific innovation 與低成本 shorthand，而 common kernel 與 bridge protocols 負責維持跨群體 interoperability 與 world-grounded invariants。

本文最終主張：

$$
\boxed{
\text{The topology of communication partly determines the topology of language.}
}
$$

因此未來複合算子語言不能只設計 vocabulary / grammar；還必須共同設計：

$$
\boxed{
\text{Language}
+
\text{Transmission Graph}
+
\text{Routing Policy}
+
\text{Bridge Semantics}.
}
$$

---

## 關鍵詞

multi-agent topology；emergent communication；compositionality；semantic drift；dialect；sparse communication；language evolution；common semantic kernel；LLM agents；distributed language

---

# 1. 從世代鏈到傳播圖

上一章使用：

$$
A_1
\rightarrow
A_2
\rightarrow
A_3
\rightarrow\cdots
$$

研究 iterated transmission。

但真實系統更像：

$$
\boxed{
G_T=(V,E).
}
$$

其中每個 node：

$$
v_i=A_i
$$

是一個 Agent。

edge：

$$
e_{ij}
$$

表示：

$$
A_i
\rightarrow
A_j
$$

可傳遞：

- operator definition；
- task result；
- objection；
- example；
- semantic correction；
- shorthand；
- version update。

---

# 2. Directed / Undirected

communication 不一定對稱。

$$
e_{ij}=1
$$

不代表：

$$
e_{ji}=1.
$$

teacher–student 是 directed。

peer dialogue 可近似 bidirectional。

所以：

$$
\boxed{
G_T
}
$$

通常應視為 directed weighted graph。

---

# 3. Edge Weight

定義：

$$
w_{ij}
$$

可代表：

- communication frequency；
- token bandwidth；
- trust；
- authority；
- influence；
- semantic fidelity。

不同解釋不能混在同一 scalar，正式模型可用 edge vector：

$$
\boxed{
\mathbf w_{ij}
=
(
b_{ij},
f_{ij},
t_{ij},
a_{ij}
).
}
$$

---

# 4. Topology 不是 Neutral Channel

如果同一正確資訊：

$$
x
$$

在 fully connected graph 中瞬間傳到所有 Agents，

與只在一個 local cluster 傳播，

群體結果不同。

同樣：

$$
\epsilon
$$

錯誤資訊也會被拓撲放大或隔離。

因此：

$$
\boxed{
\text{Topology}
=
\text{Information Selection Mechanism}.
}
$$

---

# 5. Information Diffusion

定義一個有益訊息：

$$
m^+.
$$

經過 $k$ rounds 後到達比例：

$$
\boxed{
D^+(k)
=
\frac{
|\{A_i:m^+\text{ reached }A_i\}|
}{
|V|
}.
}
$$

這是：

**Beneficial Diffusion**。

---

# 6. Error Diffusion

對錯誤：

$$
m^-,
$$

同樣：

$$
\boxed{
D^-(k)
=
\frac{
|\{A_i:m^-\text{ influenced }A_i\}|
}{
|V|
}.
}
$$

理想 topology：

$$
D^+\uparrow
$$

而：

$$
D^-\downarrow.
$$

---

# 7. Topology Utility

第一版：

$$
\boxed{
U_G
=
\alpha D^+
-
\beta D^-
+
\gamma Diversity
+
\eta Coordination
-
\lambda Cost.
}
$$

因此最密 graph 不一定最佳。

---

# 8. 2025 Information-Propagation Result

近期 LLM multi-agent topology 研究直接發現：

> moderately sparse topologies 往往能抑制錯誤傳播，同時保留有益資訊 diffusion，並在 task performance 上取得較好結果。

這給出一個很重要的候選：

$$
\boxed{
Density^*
\in
(0,1)
}
$$

即最佳 topology density 可能不是：

- fully isolated；
- fully connected。

而是中間值。

---

# 9. Error Amplification Factor

定義：

$$
\boxed{
A_E(G)
=
\frac{
FinalPopulationError
}{
InitialErrorMass
}.
}
$$

如果：

$$
A_E>1,
$$

topology 放大錯誤。

若：

$$
A_E<1,
$$

topology / protocol 具有隔離或修正作用。

---

# 10. Correct-Information Amplification

同樣：

$$
\boxed{
A_C(G)
=
\frac{
FinalCorrectInformationMass
}{
InitialCorrectMass
}.
}
$$

理想：

$$
A_C\gg1,
\qquad
A_E\ll1.
$$

---

# 11. Communication Topology 的五個核心壓力

本文提出：

$$
\boxed{
\mathcal P_G
=
(
P_D,
P_E,
P_V,
P_C,
P_K
).
}
$$

其中：

- $P_D$：Diffusion pressure；
- $P_E$：Error propagation；
- $P_V$：Variation / diversity pressure；
- $P_C$：Coordination pressure；
- $P_K$：Communication cost。

---

# 12. 為什麼 Topology 會改變語言形式？

如果所有 Agents 都頻繁互通：

$$
PathLength\downarrow,
$$

local innovations 很快被全體看見。

這會：

- 加快 convergence；
- 也可能加快 false consensus。

若 communities 相對隔離：

- local dialect 可保存；
- global interoperability 下降。

所以：

$$
\boxed{
\text{Network Mixing}
\leftrightarrow
\text{Dialect Preservation}.
}
$$

---

# 13. Network Path Length

定義平均最短路：

$$
\boxed{
\ell_G
=
\frac1{|V|(|V|-1)}
\sum_{i\neq j}
d(i,j).
}
$$

較小：

- information diffusion 快；
- errors 也可能快。

較大：

- local variation 容易保存；
- correction 傳播慢。

---

# 14. Clustering Coefficient

高 clustering：

> friends of an Agent 彼此也常連通。

這容易形成：

$$
\boxed{
\text{Local Convention Reinforcement}.
}
$$

因此 community-specific dialect 可更穩。

---

# 15. 2024 Network-Language Result

agent-based language-evolution 模型顯示：

- network structure 對 interindividual variation 有強影響；
- path length 與 clustering coefficient 是重要因素；
- 不高度連通、小型 community 結構更容易形成 variation。

因此：

$$
\boxed{
\text{Topology}
\rightarrow
\text{Language Variation Pressure}.
}
$$

不是純粹推測。

---

# 16. Community Modularity

若 network 可分：

$$
C_1,\ldots,C_m,
$$

定義 modularity：

$$
Q_G.
$$

高：

$$
Q_G
$$

表示 local communities 強。

語言可能形成：

$$
\boxed{
\mathcal L_1,
\mathcal L_2,
\ldots,
\mathcal L_m.
}
$$

---

# 17. Dialect Modularity

可以定義：

$$
\boxed{
M_D
=
\frac{
SemanticDifference_{between\ communities}
}{
SemanticDifference_{within\ communities}+\epsilon
}.
}
$$

高：

$$
M_D
$$

代表 dialect 分化明顯。

---

# 18. Dialect 不等於 Failure

local dialect 可能：

- 更短；
- 更專業；
- domain-specific；
- 更適合當地工具。

所以：

$$
\boxed{
\text{Dialect}
\neq
\text{Drift Failure}.
}
$$

只要仍能透過 common kernel / translation 恢復跨群體 semantics。

---

# 19. Language Speciation

若：

$$
F_{\Phi}(L_i,L_j)
<
\tau_{\Phi},
$$

local dialect 間翻譯 fidelity 太低，

則可視為：

$$
\boxed{
\text{Language Speciation}.
}
$$

這接續 LRC–COL-09。

---

# 20. Chain Topology

$$
A_1\rightarrow A_2\rightarrow\cdots\rightarrow A_n.
$$

優點：

- transmission bottleneck 明確；
- 易研究 generation drift。

缺點：

- single-path corruption；
- telephone-game accumulation；
- correction 慢。

---

# 21. Chain Drift

若每 edge fidelity：

$$
q,
$$

最簡：

$$
F_{end}
\approx q^{n-1}.
$$

所以 chain length 高時：

$$
\boxed{
\text{cumulative drift risk}\uparrow.
}
$$

---

# 22. Star Topology

中心：

$$
A_c
$$

與所有 Agents 連。

優點：

- standardization 快；
- low path length；
- governance 易。

缺點：

- central failure；
- authority bias；
- innovation bottleneck；
- censorship / filtering bottleneck。

---

# 23. Canonical-Star Language

如果中央 Agent 是：

$$
\boxed{
\text{Semantic Registry / Canonical Teacher},
}
$$

可穩定 core semantics。

但：

$$
A_c
$$

若錯：

$$
D^-
$$

瞬間擴散。

---

# 24. Centralization Risk

定義：

$$
\boxed{
R_C
=
ImpactFailure(A_c).
}
$$

star 中：

$$
R_C
$$

通常高。

---

# 25. Full Mesh

所有：

$$
A_i\leftrightarrow A_j.
$$

優點：

- information redundancy；
- low path length；
- fast correction。

缺點：

- token / bandwidth：

$$
O(n^2)
$$

- consensus pressure 高；
- error cascade 快；
- local innovation survival 低。

---

# 26. Full Mesh 不保證最佳集體推理

2024 sparse multi-agent debate 研究已發現：

稀疏 communication topology 可用較低成本達到相當或更好 performance。

所以：

$$
\boxed{
\text{More communication}
\neq
\text{better collaboration}.
}
$$

---

# 27. Sparse Mesh

保留多路徑，

但不是 all-to-all。

可能：

$$
\boxed{
\text{Redundancy without quadratic communication}.
}
$$

也是近期 topology 研究常找到的高效區。

---

# 28. Sparse Graph 的語言效應

稀疏 graph：

- local variation 生存更久；
- errors 不易瞬間全局化；
- correction 也較慢。

因此：

$$
\boxed{
\text{Sparse}
=
\text{Diversity Buffer}
+
\text{Correction Delay}.
}
$$

---

# 29. Hierarchy

例如：

$$
Workers
\rightarrow
TeamLead
\rightarrow
Coordinator.
$$

優點：

- scalable；
- local compression；
- active communication width bounded。

缺點：

- summary distortion；
- upper-layer bottleneck；
- hierarchy-induced semantic loss。

---

# 30. Hierarchical Semantic Compression

低層：

$$
D_{detail}
$$

被 leader 壓成：

$$
S_{summary}.
$$

上層只看到 summary。

因此：

$$
\boxed{
\text{Hierarchy}
\rightarrow
\text{Information Compression}.
}
$$

這可能促進 common higher-level operators，也可能丟失 minority details。

---

# 31. Summary-Induced Drift

如果每層 summary fidelity：

$$
q_s,
$$

多層 hierarchy：

$$
F\approx q_s^h.
$$

所以 hierarchy depth：

$$
h
$$

本身就是 semantic risk。

---

# 32. Modular Communities

Agents 分成：

$$
C_1,\ldots,C_m.
$$

群內密，

群間 sparse bridges。

這可能是非常重要的 COL topology。

---

# 33. Modular 的優勢

群內：

- 高 bandwidth；
- domain shorthand；
- rapid local learning。

群間：

- bridge 保留 common semantics；
- 降低 global communication cost。

因此：

$$
\boxed{
\text{Local Efficiency}
+
\text{Global Interoperability}.
}
$$

---

# 34. Modular 的風險

如果 bridges 太少：

- dialect speciation；
- semantic fragmentation。

如果 bridges 太多：

- local innovation 被全局平均掉。

所以：

$$
\boxed{
BridgeDensity^*
}
$$

可能存在。

---

# 35. Bridge Node

一個 bridge Agent：

$$
A_b
$$

需要雙語／多語能力：

$$
\mathcal L_i
\leftrightarrow
\mathcal L_j.
$$

它是：

$$
\boxed{
\text{Semantic Translator Node}.
}
$$

---

# 36. Bridge Dependence

定義：

$$
\boxed{
B_D(G)
=
\frac{
CriticalCrossCommunityFlows
}{
NumberOfIndependentBridgePaths
}.
}
$$

bridge 少：

$$
B_D\uparrow.
$$

system brittle。

---

# 37. Bridge Corruption

若 bridge semantic mapping 錯：

群內語言都可以正常，

跨群結果卻全部錯。

這形成：

$$
\boxed{
\text{Interoperability Failure without Local Failure}.
}
$$

---

# 38. Multi-Bridge Redundancy

可設：

$$
\Phi_1,\Phi_2,\Phi_3
$$

多個 independent translators。

用 disagreement 檢查 translation fidelity。

這類似 RLMM 的 independent challenge。

---

# 39. Rotating Teacher

teacher 角色不是固定：

$$
A_1\rightarrow A_2,
$$

下一輪：

$$
A_3\rightarrow A_4.
$$

優點：

- 防止單一 authority lock-in；
- 多 source exposure。

缺點：

- version inconsistency；
- curriculum 不穩。

---

# 40. Rotating Teacher 的語言作用

可能提高：

$$
\boxed{
\text{Diversity of Exposure}
}
$$

但需要：

- common anchor；
- versioning；
- provenance。

---

# 41. Many-to-One

多個 Agents 向一個 learner / coordinator 傳：

$$
A_1,A_2,\ldots,A_n
\rightarrow
A_c.
$$

這是：

$$
\boxed{
\text{Aggregation Topology}.
}
$$

---

# 42. Aggregation 可以產生 Consensus Illusion

如果多個 upstream Agents：

- 同 model；
- 同 source；
- 同 prompt；

則：

$$
n
$$

條 edges 不等於：

$$
n
$$

份獨立 evidence。

所以：

$$
\boxed{
\text{Topological Multiplicity}
\neq
\text{Epistemic Independence}.
}
$$

---

# 43. Consensus Correlation

定義：

$$
\boxed{
\rho_C
=
AverageCorrelation(
Sources,
Models,
Methods
).
}
$$

群體 agreement 應依：

$$
1-\rho_C
$$

折價。

---

# 44. False Consensus Topology

dense network 也會讓 Agents 看到彼此答案，

造成：

$$
\boxed{
\text{Information Cascade}.
}
$$

最終 agreement 很高，

但獨立性已消失。

---

# 45. Independent-First-Pass Topology

可以把時間分：

### Phase 1

$$
E=\varnothing
$$

各自獨立。

### Phase 2

啟動 sparse exchange。

### Phase 3

必要時 merge。

這是 RLMM-08 的 topology 化。

---

# 46. One-to-Many 不等於 Compositionality

2024 EMNLP 研究直接顯示：

> 單純 speaker 對多 listeners broadcast，不會自動產生更 compositional language。

真正促進 compositionality 的因素包括：

- listeners interests 不同；
- listeners 之間需要 coordination。

因此：

$$
\boxed{
\text{Topology Size}
\neq
\text{Compositional Pressure}.
}
$$

---

# 47. Interest Diversity

令：

$$
I_i
$$

是 listener $A_i$ 需要的 semantic features。

如果：

$$
I_1=I_2=\cdots,
$$

speaker 只要傳一套單一 holistic signal。

若：

$$
I_i
$$

不同，

message 需要同時攜帶可拆分資訊。

這可能促進：

$$
\boxed{
\text{factorized / compositional encoding}.
}
$$

---

# 48. Coordination Pressure

若 listeners 不只各自解碼，

還必須互相協作，

communication 需要：

- shared reference；
- decomposable roles；
- predictable semantics。

因此 compositionality 可能更有價值。

---

# 49. Topology–Task Coupling

所以 topology 效果依：

$$
\boxed{
TaskGraph
}
$$

而變。

同一 communication graph：

- 對 decomposable task 很好；
- 對 tightly coupled task 可能差。

因此不存在：

$$
\boxed{
\text{universal best topology}.
}
$$

---

# 50. Task Dependency Graph

令：

$$
G_Q=(V_Q,E_Q)
$$

表示任務子問題 dependency。

理想 communication topology：

$$
G_T
$$

可能應與：

$$
G_Q
$$

部分同構。

---

# 51. Topology Alignment

定義：

$$
\boxed{
A_{TQ}
=
Similarity(
G_T,
G_Q
).
}
$$

如果 task 有 module structure，

modular communication 可能更有效。

---

# 52. 2026 Dynamic Topology Design

近期多 Agent 研究已開始讓 topology 根據 task 即時生成，而不是固定套一張 graph。

例如：

- conditional autoregressive graph generation；
- dynamic graph selector；
- graph diffusion topology generation。

這支持：

$$
\boxed{
G_T
=
G_T(q,t)
}
$$

而不是：

$$
G_T=constant.
$$

---

# 53. Topology as Runtime State

所以 COL runtime 未來可能同時維護：

```text
Operator Library
Agent Roles
Communication Graph
Semantic Bridges
Current Task Graph
```

不是只有 language parser。

---

# 54. Dynamic Topology

定義：

$$
\boxed{
G_T(t+1)
=
\Psi(
G_T(t),
Task,
Error,
Cost,
Diversity
).
}
$$

---

# 55. Edge Birth / Death

communication edge 也可以：

- add；
- weaken；
- strengthen；
- remove。

這和 operator ecology 同構。

---

# 56. Edge Utility

對：

$$
e_{ij},
$$

定義：

$$
\boxed{
U_E(e_{ij})
=
Gain_{info}
+
Gain_{correction}
+
Gain_{coord}
-
Cost_{token}
-
Risk_{cascade}
-
Risk_{homogenize}.
}
$$

---

# 57. Topology Admission Gate

只有：

$$
U_E>\tau_E
$$

才建立／維持高 bandwidth edge。

這可以形成：

$$
\boxed{
\text{Communication Sparsification}.
}
$$

---

# 58. Semantic Homogenization Risk

edge 太多：

$$
\boxed{
Diversity\downarrow.
}
$$

Agents 很快共享：

- same assumptions；
- same mistakes；
- same shorthand。

這可能降低：

$$
\text{novel branch generation}.
$$

---

# 59. Diversity Preservation

定義：

$$
\boxed{
R_V(G)
=
\frac{
DistinctIndependentHypotheses_{after}
}{
DistinctIndependentHypotheses_{before}
}.
}
$$

低：

$$
R_V
$$

表示 topology 過度 homogenize。

---

# 60. Diversity 也不是越多越好

如果每個 Agent 永遠不同：

- 無法 coordination；
- 無 common semantics。

因此：

$$
\boxed{
\text{Diversity}
\leftrightarrow
\text{Coordination}.
}
$$

---

# 61. Topological Explore–Exploit

可以類比：

### Explore

保持 local independence / sparse bridges。

### Exploit

增加 communication / convergence。

所以 topology 本身可以調節：

$$
\boxed{
\text{Explore–Exploit}.
}
$$

---

# 62. Age-Based Plasticity 與 Topology 合流

2026 CoNLL 結果顯示：

- younger agents 高 plasticity；
- older agents 提供 stable representations；

能降低 dynamic population drift。

拓撲上可以進一步：

- newcomer 先接 local mentors；
- 穩定後再接 global bridges。

這形成：

$$
\boxed{
\text{Developmental Topology}.
}
$$

---

# 63. Newcomer Integration Topology

新 Agent：

$$
A_{new}
$$

不必一開始連全網。

可以：

$$
A_{new}
\rightarrow
\text{local tutor cluster}
\rightarrow
\text{bridge}
\rightarrow
\text{global network}.
$$

降低：

- overload；
- drift；
- global contamination。

---

# 64. Stable Agents as Anchors

old Agents 可以做：

$$
\boxed{
\text{Semantic Anchor Nodes}.
}
$$

但不能永遠壟斷。

需要：

- version update；
- rotation；
- independent validation。

---

# 65. Central Standard vs Distributed Evolution

現在可以正式問：

> COL 應該中央定義，還是分散演化？

答案很可能不是二選一。

---

# 66. Pure Centralization

$$
\boxed{
\text{One Canonical Language}
}
$$

優點：

- interoperability；
- auditability；
- low drift。

缺點：

- slow innovation；
- single-point semantic failure；
- domain mismatch。

---

# 67. Pure Decentralization

每個 community 自己發展：

$$
\mathcal L_i.
$$

優點：

- innovation；
- domain fit；
- local efficiency。

缺點：

- fragmentation；
- translation cost；
- speciation。

---

# 68. Federated Language Architecture

候選：

$$
\boxed{
\mathcal L_i
=
\mathcal K
\cup
\mathcal D_i
\cup
\mathcal E_i.
}
$$

其中：

- $\mathcal K$：common semantic kernel；
- $\mathcal D_i$：community/domain dialect；
- $\mathcal E_i$：ephemeral local operators。

---

# 69. Common Kernel

kernel 承載：

- identity；
- type；
- composition；
- reference；
- verify；
- commit；
- rollback；
- version；
- translation。

要求：

$$
\boxed{
F_{\mathcal K}\approx1
}
$$

跨 communities。

---

# 70. Local Dialect

$$
\mathcal D_i
$$

可針對：

- domain；
- tool；
- workflow；

優化。

允許較高 plasticity。

---

# 71. Ephemeral Layer

$$
\mathcal E_i
$$

只在：

- current project；
- session；
- temporary coalition；

存在。

可以快速 birth / retire。

---

# 72. Semantic Bridge

community 間：

$$
\Phi_{ij}:
\mathcal L_i
\leftrightarrow
\mathcal L_j.
$$

最好透過：

$$
\mathcal K
$$

作中介：

$$
\boxed{
\mathcal L_i
\rightarrow
\mathcal K
\rightarrow
\mathcal L_j.
}
$$

---

# 73. 為什麼 Kernel 可以降低 Translation Complexity？

pairwise：

$$
O(m^2).
$$

共有 kernel：

$$
O(m).
$$

這與上一篇 universal interchange layer 一致。

---

# 74. Kernel Bottleneck Risk

但若：

$$
\mathcal K
$$

太貧乏，

local distinctions 在 translation 時消失。

所以：

$$
\boxed{
\text{Kernel Simplicity}
\leftrightarrow
\text{Cross-Domain Fidelity}.
}
$$

---

# 75. Kernel Coverage

定義：

$$
\boxed{
R_K
=
\frac{
CriticalCrossCommunityDistinctionsRepresentableInKernel
}{
TotalCriticalCrossCommunityDistinctions
}.
}
$$

要求：

$$
R_K\ge\tau_K.
$$

---

# 76. Kernel 不需要承載所有 Local Detail

只需要：

> 跨 community 有必要交換的 distinctions。

所以：

$$
|\mathcal K|
$$

可以遠小於：

$$
\left|\bigcup_i\mathcal L_i\right|.
$$

---

# 77. Semantic Diameter

定義兩 Agents 語言狀態差異：

$$
d_L(A_i,A_j).
$$

network semantic diameter：

$$
\boxed{
Diam_L
=
\max_{i,j}
d_L(A_i,A_j).
}
$$

太大：

- interoperability 崩潰。

太小：

- 過度 homogenization。

---

# 78. Optimal Semantic Diameter

因此可能存在：

$$
\boxed{
Diam_L^*
}
$$

允許：

- local diversity；
- global translation。

又一個中間 optimum。

---

# 79. Topological Semantic Distance

Agents graph distance：

$$
d_G(i,j)
$$

與 language distance：

$$
d_L(i,j)
$$

可能相關。

可以測：

$$
\boxed{
Corr(
d_G,
d_L
).
}
$$

---

# 80. 如果相關很強

表示：

> communication topology 正在塑造 dialect geography。

這是可直接實驗的命題。

---

# 81. Minority Innovation

一個 Agent：

$$
A_m
$$

產生新 operator：

$$
O_{new}.
$$

在 dense graph：

可能：

- 很快被接受；
- 或很快被 majority 壓掉。

在 modular graph：

可以先在 local cluster 測試。

---

# 82. Innovation Incubator

因此 local community 可以是：

$$
\boxed{
\text{Operator Innovation Incubator}.
}
$$

新 operator 先：

- local use；
- stabilize；
- evidence；
- 再跨 bridge promotion。

---

# 83. Innovation Promotion Route

$$
\boxed{
Ephemeral
\rightarrow
Local
\rightarrow
Cross-Community Trial
\rightarrow
Kernel Candidate.
}
$$

這可能是第 11 篇 adaptation law 的重要流程。

---

# 84. Topology and False Consensus

如果 topology：

- fully connected；
- high trust；
- simultaneous sharing；

可能：

$$
\boxed{
\text{Consensus Speed}
\uparrow
}
$$

但：

$$
\boxed{
\text{Epistemic Independence}
\downarrow.
}
$$

---

# 85. Consensus Speed

定義：

$$
\boxed{
T_C
=
\min
\{
t:
Var(Belief_t)<\epsilon
\}.
}
$$

快不一定好。

---

# 86. Premature Consensus

如果：

$$
T_C<T_{evidence},
$$

也就是群體在足夠 evidence diffusion 前就收斂，

則：

$$
\boxed{
\text{Premature Consensus}.
}
$$

---

# 87. Topology Can Delay Consensus Intentionally

sparse / modular graph 可以保留：

- alternative branches；
- independent evidence；

更久。

因此：

$$
\boxed{
\text{slower consensus}
}
$$

有時是 feature。

---

# 88. Consensus Hysteresis

與 operator hysteresis 同樣，

群體不應：

- 一次 majority 就立即全局 commit。

可以先：

$$
\boxed{
\text{Local Consensus}
\rightarrow
\text{Cross-Cluster Validation}
\rightarrow
\text{Global Commit}.
}
$$

---

# 89. Communication Cost

對 graph：

$$
\boxed{
C_G
=
\sum_{(i,j)\in E}
Tokens_{ij}
+
Latency_{ij}
+
Compute_{ij}.
}
$$

full mesh：

$$
C_G
$$

快速增長。

---

# 90. Cost-Normalized Topology Utility

$$
\boxed{
Y_G
=
\frac{
TaskUtility
+
SemanticHealth
}{
C_G
}.
}
$$

這是 topology 層的 action yield。

---

# 91. Robustness

如果刪掉 node / edge：

$$
G\rightarrow G',
$$

performance 下降多少？

定義：

$$
\boxed{
R_G
=
1-
\frac{
\Delta Performance
}{
Perturbation
}.
}
$$

---

# 92. Star 通常 Central Failure 高

modular / sparse mesh 可能更 robust。

但 redundancy 也增加成本。

仍是 Pareto 問題。

---

# 93. Security / Privacy 也進入 Topology

2026 ACL 工作甚至顯示 multi-agent communication topology 本身可以在 black-box 條件下被推斷，造成 privacy / IP leakage。

所以：

$$
\boxed{
G_T
}
$$

本身可能是敏感資產。

---

# 94. Topology Disclosure Risk

如果 topology 暴露：

攻擊者可推測：

- authority node；
- bottleneck；
- bridge；
- role structure。

因此 COL runtime 也要考慮：

$$
\boxed{
\text{Topology Security}.
}
$$

---

# 95. Dynamic Topology Security

頻繁 changing topology：

- 可降低 static attack predictability；
- 也提高 governance complexity。

這仍是 trade-off。

---

# 96. Communication Protocol Edge Types

edge 不只「能不能說話」。

可有：

### Broadcast
單向群播。

### Query
按需詢問。

### Objection
只傳 challenge。

### Evidence
只傳 evidence。

### Translation
semantic bridge。

### Commit
決策／版本同步。

不同 edge type 產生不同 language pressure。

---

# 97. Typed Communication Graph

因此更完整：

$$
\boxed{
G_T
=
(V,E,\tau_E).
}
$$

其中：

$$
\tau_E(e)
\in
\{
broadcast,
query,
evidence,
objection,
translation,
commit
\}.
$$

---

# 98. Typed Edge 可以降低 Homogenization

例如：

Agent 不互看完整 answer，

只傳：

- objections；
- evidence。

可以保留更多 independent cognition。

所以 topology + protocol 必須聯合研究。

---

# 99. Topology Alone Is Not Enough

同一 graph：

$$
G
$$

如果 edge message content 不同，

結果完全不同。

所以：

$$
\boxed{
\text{Topology}
+
\text{Edge Protocol}
}
$$

才是完整 communication architecture。

---

# 100. Topology–Protocol Pair

定義：

$$
\boxed{
\Gamma
=
(G_T,\Pi_E).
}
$$

其中：

$$
\Pi_E
$$

是 edge protocol。

---

# 101. Topology Optimization

真正：

$$
\boxed{
\Gamma^*
=
\arg\max_{\Gamma}
J_{\Gamma}.
}
$$

而不是只找 graph density。

---

# 102. Topology Utility Objective

第一版：

$$
\boxed{
J_{\Gamma}
=
\alpha TaskPerformance
+
\beta SemanticFidelity
+
\gamma DiversityRetention
+
\eta Innovation
+
\theta Robustness
-
\lambda CommunicationCost
-
\mu ErrorPropagation
-
\nu Fragmentation.
}
$$

---

# 103. Dynamic Topology Objective

隨 task：

$$
q,
$$

$$
\boxed{
\Gamma^*(q,t)
}
$$

可能變。

所以未來 runtime 可以 task-adaptive。

---

# 104. 2026 Automated Topology Design

近期工作已從：

> 固定 ring / tree / complete graph

走向：

- task-conditioned graph selector；
- autoregressive graph generation；
- diffusion graph generation。

這正好支持：

$$
\boxed{
\text{Topology should be generated / selected as part of reasoning}.
}
$$

---

# 105. 但這些工作主要最佳化 Task Performance

COL 還需要額外最佳化：

- semantic health；
- language drift；
- dialect preservation；
- interoperability；
- innovation。

所以：

$$
\boxed{
\text{best reasoning topology}
\neq
\text{best language-evolution topology}.
}
$$

---

# 106. 雙時間尺度 Topology

可能：

### Fast Topology

每個 task 動態重配。

### Slow Topology

長期 language-learning / transmission graph。

所以：

$$
\boxed{
G_{fast}(q)
\neq
G_{slow}(t).
}
$$

---

# 107. Fast Graph

最佳化：

- task speed；
- current collaboration。

---

# 108. Slow Graph

最佳化：

- learning；
- innovation；
- stability；
- dialect / kernel governance。

---

# 109. 如果兩者混在一起

短期高效 topology 可能讓長期語言：

- 過度 homogenize；
- centralize；
- lose diversity。

所以需要分開。

---

# 110. Language-Evolution Topology

本文真正關注：

$$
\boxed{
G_L(t)
}
$$

長期決定：

> 誰向誰學語言。

---

# 111. Task-Execution Topology

另：

$$
\boxed{
G_X(q,t)
}
$$

決定：

> 這個 task 誰和誰合作。

兩者可不同。

---

# 112. 這是一個非常重要的新區分

$$
\boxed{
\text{Learning Network}
\neq
\text{Execution Network}.
}
$$

未來 AI organization 不必：

> 跟誰一起工作，就只跟誰學語言。

---

# 113. Cross-Cutting Bridges

可以讓 learning network 有額外 bridge：

- audit Agents；
- translation Agents；
- standards Agents。

即使 execution teams 分開。

---

# 114. Federated Language Governance

因此候選架構：

```text
Local Execution Communities
        ↓↑
Semantic Bridges
        ↓↑
Common Kernel Registry
        ↓↑
Independent Audit / Innovation Nodes
```

這是：

$$
\boxed{
\text{Federated COL}.
}
$$

---

# 115. Federated 不等於沒有中心

common kernel registry 是：

- semantic anchor；
- version registry。

但 local dialect 不必全部由中心規定。

這是：

$$
\boxed{
\text{bounded federation}.
}
$$

---

# 116. Kernel Governance

新 operator 要進 kernel：

需：

1. 多 community usefulness；
2. stable semantics；
3. translation benefit；
4. low collision；
5. high distinction value。

---

# 117. Local Operator 不必進 Kernel

只在一個 domain 有用：

保留：

$$
\mathcal D_i.
$$

避免 global vocabulary pollution。

---

# 118. Topology and Operator Basis Co-Evolution

更進一步：

$$
\boxed{
\mathcal O_t
\leftrightarrow
G_T(t).
}
$$

language 會影響 topology：

- common shorthand 降低 communication cost；
- dialect 增加 bridge need。

topology 也影響 language：

- clustering 產生 dialect；
- bridges 促進 alignment。

---

# 119. Co-Evolution Equation

第一版：

$$
\boxed{
\begin{aligned}
\mathcal O_{t+1}
&=
F_O(
\mathcal O_t,
G_t,
Task_t,
Failure_t
),\\
G_{t+1}
&=
F_G(
G_t,
\mathcal O_t,
Cost_t,
Drift_t
).
\end{aligned}
}
$$

這是第 11 篇 adaptation law 的重要前置。

---

# 120. Topology-Induced Crystallization

一個 local cluster 反覆使用 motif：

$$
m
$$

容易先在該 cluster 結晶：

$$
O_m.
$$

所以：

$$
\boxed{
\text{Topology}
\rightarrow
\text{Macro Birth Location}.
}
$$

---

# 121. Bridge-Induced Standardization

若多 communities 都透過同一 bridge 翻譯：

bridge 常用 mapping 可能逐漸變成：

$$
\boxed{
\text{cross-community standard operator}.
}
$$

---

# 122. Semantic Hub Formation

高 centrality operator / translation mapping 可能形成：

$$
\boxed{
\text{Semantic Hub}.
}
$$

類似 network hub。

---

# 123. Hub Operator Risk

若 hub semantic contract 漂移，

影響範圍巨大。

因此：

$$
Centrality(O)\uparrow
\Rightarrow
DriftBudget(O)\downarrow.
$$

這與 LRC–COL-08 高耦合低 drift budget 同構。

---

# 124. Operator Centrality

建立 operator co-use graph：

$$
G_O.
$$

operator node centrality：

$$
C_O.
$$

高：

$$
C_O
$$

代表大量 compositions 依賴它。

---

# 125. Topology × Operator Graph

真正系統同時有：

- Agent graph $G_A$ ；
- Operator graph $G_O$ ；
- Task graph $G_Q$。

這三張圖互相耦合。

---

# 126. Tri-Graph Model

本文提出：

$$
\boxed{
\mathfrak G
=
(
G_A,
G_O,
G_Q
).
}
$$

其中：

- $G_A$：誰跟誰傳；
- $G_O$：哪些 operator 互相組；
- $G_Q$：任務怎麼依賴。

---

# 127. 真正最佳化可能是三圖對齊

候選：

$$
\boxed{
J
=
f(
Align(G_A,G_Q),
Align(G_O,G_Q),
Health(G_A,G_O)
).
}
$$

這已經是比單純「語言 vocabulary」更完整的未來研究物件。

---

# 128. 本篇十五個正式命題

## TP-P1 — Topology Is a Language Operator
communication topology 會改變資訊、錯誤、variation 與 conventions 的傳播，因此本身是 language-evolution operator。

## TP-P2 — Moderate Sparsity
對許多 multi-agent tasks，適度稀疏可能比 fully connected 更能平衡 beneficial diffusion 與 error suppression。

## TP-P3 — Topological Variation
較長 path length 與 community clustering 會提高 local linguistic variation / dialect formation 的機率。

## TP-P4 — One-to-Many Insufficiency
單純增加 listeners 不足以保證 compositionality；interest diversity 與 coordination pressure 是更直接的結構壓力。

## TP-P5 — Topology–Task Alignment
communication graph 與 task dependency graph 的結構匹配度會影響協作與語言效益。

## TP-P6 — Dialect Modularity
modular topology 可保存 local shorthand / innovation，但 bridge 太弱會導致 language speciation。

## TP-P7 — Bridge Optimum
存在非平凡 bridge density / redundancy optimum，在 local diversity 與 global interoperability 間折衷。

## TP-P8 — Premature Consensus
過密 topology 可加速 consensus，但同時降低 epistemic independence 並增加 correlated false consensus 風險。

## TP-P9 — Developmental Topology
newcomers 應先透過 local high-plasticity learning channels 接入，再逐步接入 global semantic network。

## TP-P10 — Federated Language
common kernel + local dialects + ephemeral layer 可能比單一 global flat language 更可擴展。

## TP-P11 — Fast/Slow Topology Separation
task-execution topology 與 long-term language-learning topology 應分開最佳化。

## TP-P12 — Dynamic Topology
最佳 topology 依 task、Agent、cost、drift 與 diversity 狀態動態改變。

## TP-P13 — Topology–Operator Co-Evolution
Agent communication graph 與 operator graph 會互相塑形。

## TP-P14 — Semantic Hub Risk
高 centrality operator / bridge 一旦漂移，會造成不成比例的全域影響，故需要更嚴格 semantic governance。

## TP-P15 — Tri-Graph Alignment
未來複合語言的整體效率可能取決於 Agent、Operator、Task 三張圖的聯合結構，而非其中任一圖單獨最佳化。

---

# 129. 第一版實驗：Topology Sweep

固定：

- Agent count；
- task；
- operator language；
- initial knowledge。

比較：

### G1 — Chain

### G2 — Star

### G3 — Full Mesh

### G4 — Random Sparse

### G5 — Small-World

### G6 — Modular Communities

### G7 — Hierarchy

量：

- task success；
- communication cost；
- error diffusion；
- correct diffusion；
- semantic drift；
- dialect modularity；
- consensus speed。

---

# 130. Error Injection

隨機選：

$$
A_e
$$

植入錯誤 operator interpretation。

測不同 topology：

$$
A_E(G).
$$

這可以直接驗證 error propagation。

---

# 131. Minority Innovation Injection

一個 peripheral Agent 產生：

$$
O_{new}.
$$

但 $O_{new}$ 真正有用。

測：

- survival；
- adoption；
- suppression；
- distortion。

---

# 132. False Innovation Injection

另一 condition：

$$
O_{bad}.
$$

看 topology 能不能同時：

- 保留好 minority innovation；
- 抑制壞 innovation。

這是更難的測試。

---

# 133. Dialect Experiment

不同 communities 接不同 workloads。

觀察：

$$
\mathcal D_i.
$$

再逐步提高 bridge density。

測：

- local efficiency；
- cross-community translation；
- dialect collapse。

---

# 134. Kernel Experiment

三種：

### No Kernel

純 local dialect。

### Full Central Language

沒有 local dialect。

### Federated Kernel

core + local dialect。

比較：

- learnability；
- communication；
- innovation；
- drift；
- translation cost。

---

# 135. One-to-Many Interest Experiment

listeners：

### Same Interests

都需要相同 semantic features。

### Different Interests

不同 listeners 需要不同 feature。

再加：

### No Coordination

### Coordination Required

測 compositionality / factorization。

---

# 136. Independent-First-Pass Experiment

比較：

### Immediate Mesh

一開始互看。

### Delayed Sparse

先獨立，再交換。

量：

- accuracy；
- hypothesis diversity；
- false consensus；
- cost。

---

# 137. Topology Adaptation Experiment

固定 topology vs dynamic selector。

但除了 task performance，

額外量：

- drift；
- diversity；
- semantic health。

這補足 current dynamic-topology research 的短期 task focus。

---

# 138. Fast vs Slow Graph Experiment

執行 topology：

$$
G_X
$$

與 learning topology：

$$
G_L
$$

分開。

測：

> 是否能同時取得 task efficiency 與 long-term language diversity。

---

# 139. Bridge Failure Test

刪掉：

- single bridge；
- top-2 bridges；
- random bridge。

測：

$$
Interoperability.
$$

得到 bridge robustness。

---

# 140. Semantic Hub Test

選高 centrality operator：

$$
O_h.
$$

讓其產生小 drift：

$$
\delta.
$$

比較低 centrality operator 同樣 drift。

量 global damage。

---

# 141. Tri-Graph Experiment

建立不同：

$$
G_A,G_O,G_Q
$$

matching conditions：

### Aligned

### Random

### Anti-Aligned

比較：

$$
J.
$$

這可以直接檢查 Tri-Graph Alignment 猜想。

---

# 142. Topology Health Dashboard

每個 system 保存：

```text
Node Count
Edge Density
Average Path Length
Clustering
Modularity
Bridge Count
Communication Cost
Error Amplification
Correct Diffusion
Diversity Retention
Consensus Speed
Dialect Modularity
Kernel Fidelity
Topology Version
```

---

# 143. Language–Topology Joint Dashboard

還要：

```text
Global Operators
Local Dialects
Shared Kernel
Semantic Diameter
Cross-Agent Variance
Bridge Translation Fidelity
Novel Operator Birth
Global Adoption
Drift
```

---

# 144. Topology Release State

像 operator 一樣：

### Experimental

### Candidate

### Stable

### Task-Specific

### Deprecated

因為 topology 也會版本化。

---

# 145. Topology Migration

若：

$$
G_1\rightarrow G_2,
$$

Agent communication patterns 改變。

可能造成語言突然重新對齊／漂移。

因此 migration 需要：

- staged rollout；
- semantic probes；
- bridge preservation。

---

# 146. Topology Change ≠ Pure Infrastructure Change

因為：

$$
\boxed{
G_T
\rightarrow
\mathcal L.
}
$$

所以換 graph 其實也是 language intervention。

---

# 147. 這是本篇最重要的工程結論之一

未來如果我們真的做複合 operator language，

不能說：

> 語言設計完了，multi-agent network 隨便接。

因為 network 本身會：

- 改變 symbol usage frequency；
- 改變 macro crystallization；
- 改變 dialect；
- 改變 consensus；
- 改變 semantic drift。

所以：

$$
\boxed{
\text{Language Design}
\not\perp
\text{Network Design}.
}
$$

---

# 148. 與 LRC–COL-11 的直接接口

目前已經有：

- operator birth / retire；
- dynamic interval；
- learning time；
- stabilization；
- transmission；
- topology。

下一篇終於可以把所有東西收成：

$$
\boxed{
\text{Operator Basis Adaptation Law}.
}
$$

---

# 149. Adaptation State

第 11 篇會使用：

$$
\boxed{
X_t
=
(
\mathcal O_t,
G_T(t),
\mu_t,
A_t,
D_{drift},
Y_L,
C_{learn},
C_{select}
).
}
$$

決定：

$$
\boxed{
\mathcal O_{t+1}.
}
$$

---

# 150. 本篇核心公式組

Transmission graph：

$$
\boxed{
G_T=(V,E,W,R).
}
$$

topology utility：

$$
\boxed{
U_G
=
\alpha D^+
-\beta D^-
+\gamma Diversity
+\eta Coordination
-\lambda Cost.
}
$$

dialect modularity：

$$
\boxed{
M_D
=
\frac{
SemanticDifference_{between}
}{
SemanticDifference_{within}+\epsilon
}.
}
$$

dynamic graph：

$$
\boxed{
G_T(t+1)
=
\Psi(
G_T(t),
Task,
Error,
Cost,
Diversity
).
}
$$

federated language：

$$
\boxed{
\mathcal L_i
=
\mathcal K
\cup
\mathcal D_i
\cup
\mathcal E_i.
}
$$

tri-graph model：

$$
\boxed{
\mathfrak G
=
(
G_A,
G_O,
G_Q
).
}
$$

---

# 151. 非主張

本文不主張：

1. sparse topology 在所有 task 都優於 dense；
2. moderate sparsity 有 universal 固定值；
3. network path length / clustering 結果可直接無修改套用到所有 LLM Agents；
4. modular communities 一定形成 compositional dialect；
5. centralization 一定壞；
6. decentralization 一定好；
7. common kernel 可以消除所有 language fragmentation；
8. dynamic topology optimization 已解決 language evolution 問題；
9. multi-agent task performance 可直接等同 language health；
10. Tri-Graph Alignment 已是已證理論。

本文只提出：

$$
\boxed{
\text{Communication topology should be treated as a causal component of operator-language evolution because it regulates information diffusion, error propagation, coordination pressure, semantic homogenization, and the survival of local innovation.}
}
$$

---

# 152. 文獻錨點

1. **Understanding the Information Propagation Effects of Communication Topologies in LLM-based Multi-Agent Systems（EMNLP 2025）**  
   提出 communication topology 的因果資訊傳播分析，發現 moderately sparse topologies 往往能在 suppress error propagation 與 preserve beneficial information diffusion 之間取得較佳平衡。直接支援本文的 topology utility / error-amplification framing。

2. **Improving Multi-Agent Debate with Sparse Communication Topology（EMNLP Findings 2024）**  
   系統研究 multi-agent debate 的 communication connectivity，顯示 sparse topology 可在顯著降低 computational cost 的同時達到 comparable 或 superior performance。支援「full mesh 不等於最佳協作」。

3. **How Network Structure Shapes Languages: Disentangling the Factors Driving Variation in Communicative Agents（Cognitive Science, 2024）**  
   在 Bayesian communicative-agent model 中控制多種 network metrics，發現 path length 與 clustering coefficient 對 interindividual language variation 有重要影響；較不連通、具有小型 communities 的 populations 更容易形成 variation。支援本文的 dialect / topology hypothesis。

4. **One-to-Many Communication and Compositionality in Emergent Communication（EMNLP 2024）**  
   顯示單純 speaker broadcast 給多 listeners 不會自動產生更 compositional languages；listeners 的 different interests 與 coordination requirement 才是促進 compositionality 的重要 pressures。支援「topology size ≠ compositional pressure」。

5. **Cognitively Inspired Developmental Trajectories Improve Explore-Exploit Dynamics in Neural Agent Emergent Communication（CoNLL 2026）**  
   dynamic population turnover 中，age-based plasticity 可顯著降低 drift，而 uniform low / high plasticity 分別有 adaptation 太慢與 language change 太快的問題。支援 developmental topology 與 newcomer integration。

6. **AMAS: Adaptively Determining Communication Topology for LLM-based Multi-agent System（EMNLP Industry 2025）**  
   使用 dynamic graph selector 根據 workload 自適應選擇通信結構，支援 task-conditioned topology。

7. **Assemble Your Crew: Automatic Multi-agent Communication Topology Design via Autoregressive Graph Generation（AAAI 2026）**  
   將 multi-agent composition 與 communication graph 共同視為 conditional autoregressive graph generation，根據自然語言 task 動態決定 Agents / roles / links，支援 topology 作為 runtime design variable。

8. **Dynamic Generation of Multi LLM Agents Communication Topologies with Graph Diffusion Models（ACL 2026）**  
   以 graph diffusion 動態生成 task-adaptive topology，將 performance、communication cost 與 robustness 納入 topology optimization。支援本文 dynamic topology framing。

9. **CIA: Inferring the Communication Topology from LLM-based Multi-Agent Systems（ACL 2026）**  
   顯示 communication topology 本身可能在黑箱設定下被推斷，且帶來 privacy / IP 風險。支援 topology 作為需要治理的 system artifact。

---

# 153. 下一篇

## LRC–COL-11：Operator Basis Adaptation Law
### 複合語言的變動定律
### The Adaptation Law of Composite Operator Bases

下一篇將把前十篇第一次真正收成一個「會動的算法」。

核心不再只是描述：

- operator 為何出生；
- 為何死亡；
- 為何結晶；
- 為何漂移。

而是直接定義：

$$
\boxed{
\mathcal O_{t+1}
=
\mathcal A(
\mathcal O_t,
Usage_t,
Failure_t,
Learning_t,
Drift_t,
Topology_t,
Yield_t
).
}
$$

並建立：

- Add；
- Crystallize；
- Merge；
- Split；
- Reground；
- Deprecate；
- Retire；

七種基本變動操作。

真正要回答：

> **什麼時候應該創造一個新複合符號？什麼時候應該把它升格成 stable operator？什麼時候要合併、拆分、重新錨定或淘汰？**

這會是整個系列中，最接近未來真的可以寫成 runtime / algorithm 的一篇。

**END — LRC–COL-10 v0.1**
