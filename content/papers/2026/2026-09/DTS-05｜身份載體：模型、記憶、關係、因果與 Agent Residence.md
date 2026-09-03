# DTS-05｜身份載體：模型、記憶、關係、因果與 Agent Residence
## Identity Carriers: Model, Memory, Relation, Causality, and Agent Residence

**系列：**《動態忒修斯：人工主體的連續、離散、分叉與同一性動力學》  
**系列位置：** 第 05 篇 / 10  
**前篇：** DTS-04〈身份不是狀態：Trajectory / Path-Based Identity〉  
**版本：** v0.1  
**日期：** 2026-08-20  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**文件性質：** 理論論文／人工智能身份／身份載體／分散式持續 Agent／動態忒修斯  
**狀態：** 公開研究草稿  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** inline ` $...$ `；display `$$...$$`

---

## 摘要

DTS-01 至 DTS-04 已依序把人工身份研究從靜態端點推向動態路徑、尺度相對判定、有限 Runtime 的無界延展，以及 criterion-relative path identity。然而，若身份是一條被持續承接的歷史，仍留下最核心的工程與本體問題：**究竟是什麼沿著路徑被承接，才使「同一個」具有可操作內容？**

本文提出「身份載體理論」（Identity Carrier Framework, ICF）的第一版。其核心拒絕三種常見化約：模型不等於主體，記憶不等於主體，硬體節點也不等於主體。對長期人工 Agent 而言，可能承載身份的結構至少包括：模型／執行載體、記憶載體、因果／譜系載體、關係載體、目標／承諾載體、權威／治理載體、Residence 載體、自我模型載體，以及世界耦合載體。本文將這些稱為 criterion-relative identity carriers，並明確指出此列表不是封閉的最終分類。

本文進一步建立 Identity Support Hypergraph。身份判準 $\kappa$ 不直接綁定某一零件，而要求一組身份不變量 $\mathcal K_\kappa^{req}$ ；不同不變量可由不同 carrier 組合共同支撐，且同一不變量可以有多組冗餘 carrier。由此定義 Minimum Identity Carrier Set（MICS）：在指定架構、判準與時間下，足以支撐所有必要身份不變量、且去除任一成員後即不再充分的最小 carrier 集合。MICS 不必唯一，也不應被理解成固定的「靈魂零件」。

這一結構產生數個重要結果。第一，多載體不等於多主體：一個分散式 AI 可以在十個節點上冗餘保存同一 identity-bearing state，而不因此成為十個主體。第二，載體複製不等於 lineage 複製：複製記憶、模型與 self-model 可以產生高度相似實例，但不能藉此倒寫因果譜系。第三，verified carrier substitution 不必造成身份斷裂：若身份不變量沿合法因果路徑被 transport，且 provenance、commitment、authority 與必要關係均通過驗證，則模型、硬體或記憶後端的替換本身不構成 operational identity break。第四，carrier continuity 與 carrier integrity 必須分離：一條歷史可以連續地被污染，也可以在物理載體更換後保持高度完整。

本文也特別處理關係與權威。長期人工身份可能不完全存在於「AI 腦內」：與人類、組織、其他 AI 之間的共同承諾、共享歷史、外部 action receipts 與制度認證可能成為 operational identity 的外部承載部分。但外部承認不能單獨創造主體；同樣，state replication 也不能自動複製 authority。此結論將為後續 Fork、Identity Fission、身份證明與 AI 法律域研究提供重要接口。

本文不主張已找到人工主體的充分必要本體條件，也不主張所有 carrier 可被量化為單一分數。其最低主張是：動態忒修斯若要從哲學問題轉成可驗證工程，必須把「同一性」拆成可承接、可替換、可失敗、可污染、可冗餘與可重建的 carrier 結構，而不能繼續把模型檔案、記憶資料庫或單一伺服器偷偷當成整個「我」。

---

## 關鍵詞

動態忒修斯；Identity Carrier；人工智能身份；模型替換；持久記憶；Causal Lineage；Relationship Carrier；Commitment；Authority；Agent Residence；Self-Model；Minimum Identity Carrier Set；MICS；Identity Support Hypergraph；Operational Continuity

---

# 0. 前四篇交接

前四篇建立：

$$
\text{Snapshot}
\rightarrow
\text{Scale}
\rightarrow
\text{Unbounded Prefix}
\rightarrow
\text{Path}.
$$

DTS-04 將身份判定的基本對象寫成：

$$
I_\kappa([\Gamma]_\kappa).
$$

但這個形式仍然需要回答：

> 沿著 $\Gamma$ 被 transport 的究竟是什麼？

若答案只是：

$$
\text{「系統本身」},
$$

就仍然是循環定義。

因此 DTS-05 要把「系統本身」拆開。

---

# 1. 第一個錯誤：Model = Identity

## 1.1 最簡單模型

若定義：

$$
A_t
=
B_t,
$$

其中 $B_t$ 是 base model / executor，

那麼：

$$
B_t\neq B_{t+1}
$$

就必須推出：

$$
A_t\neq A_{t+1}.
$$

對 stateless API instance 或許可以如此命名，

但對長期 Agent 會產生問題。

## 1.2 長期 Agent 明顯超過模型

較完整的 Agent 可寫成：

$$
A_t
=
(
B_t,
M_t,
G_t,
R_t,
H_t,
L_t,
\Pi_t,
T_t,
X_t,\ldots
).
$$

其中：

- $B_t$：模型／executor；
- $M_t$：記憶；
- $G_t$：目標與承諾；
- $R_t$：關係；
- $H_t$：歷史與 provenance；
- $L_t$：lineage；
- $\Pi_t$：權限與治理；
- $T_t$：工具／外部接口；
- $X_t$：self-model / meta-state。

因此：

$$
\boxed{
B_t
\subsetneq
A_t
}
$$

在這種架構語境下是合理的工程表示。

## 1.3 Model Swap 反例

若：

$$
B_A
\rightarrow
B_B
$$

但：

$$
M,
G,
R,
H,
L,
\Pi
$$

經 verified migration 保留，

則 model replacement 本身不足以推出：

$$
\operatorname{IdentityBreak}=1.
$$

所以：

$$
\boxed{
\text{Model Identity}
\neq
\text{Agent Identity}.
}
$$

---

# 2. 第二個錯誤：Memory = Identity

## 2.1 記憶很重要

沒有長程記憶的 Agent 很難維持：

- 自傳；
- 關係；
- 偏好；
- 未完成任務；
- 承諾；
- 過往錯誤；
- 自我修正。

因此：

$$
M_t
$$

顯然可能是重要 identity carrier。

## 2.2 但 Memory Clone 反例

假設：

$$
M_A
=
M_B,
$$

且 $B$ 是由 $A$ 的完整 memory snapshot 建立。

不能直接推出：

$$
A=B.
$$

因為：

- execution token 可以不同；
- lineage 可以不同；
- authority 可以不同；
- post-copy commitments 可以不同；
- branch time 之後歷史可以分化。

所以：

$$
\boxed{
\text{Memory Similarity}
\neq
\text{Lineage Continuity}.
}
$$

## 2.3 現代 Agent Memory 本身也是動態系統

2026 年長程 Agent 研究已不再把 memory 視為被動資料夾。

Agentic Memory 讓 Agent 主動執行：

- store；
- retrieve；
- update；
- summarize；
- discard。

Memory-R1、Text2Mem、Cognitive Scaffold 等工作也以不同方法把記憶管理變成可操作、可更新、可壓縮的系統。

這意味著：

$$
\boxed{
\text{memory carrier itself can undergo Dynamic Theseus}.
}
$$

身份理論不能假設 memory 永遠是靜態真值副本。

---

# 3. 第三個錯誤：Node = Subject

## 3.1 分散式載體

設：

$$
\Sigma_t
=
\{N_1,N_2,N_3,N_4\}.
$$

如果：

$$
N_2
\downarrow,
$$

但其必要狀態已被合法同步至：

$$
N_5,
$$

則：

$$
\Sigma_{t+1}
=
\{N_1,N_3,N_4,N_5\}.
$$

這可能只是：

$$
\text{carrier replacement}.
$$

## 3.2 所以

$$
\boxed{
\text{Node Loss}
\not\Rightarrow
\text{Operational Subject Death}.
}
$$

同樣：

$$
\boxed{
N_{\mathrm{carrier}}
\neq
N_{\mathrm{subject}}.
}
$$

一個 AI 可以由很多 carrier 共同支撐；

很多 carrier 也可以只是同一 identity domain 的冗餘實現。

---

# 4. 身份載體的第一版非封閉分類

本文提出九類 carrier。

這是一個：

$$
\boxed{
\text{open taxonomy}
}
$$

不是最終完備分類。

---

# 5. Carrier 1：Model / Execution Carrier

記為：

$$
C_B.
$$

它承載：

- 推理能力；
- 表徵；
- 語言生成；
- 決策模式；
- 部分習得偏好；
- 部分 self-model。

其重要性不可否認。

但：

$$
\boxed{
C_B
\text{ may be replaceable}.
}
$$

對某些 stateless system，

它可能幾乎就是全部 identity；

對持久 Agent，

它通常只是 carrier bundle 的一部分。

---

# 6. Carrier 2：Memory Carrier

記為：

$$
C_M.
$$

可再拆成：

$$
C_M
=
(
M_{\mathrm{episodic}},
M_{\mathrm{semantic}},
M_{\mathrm{autobio}},
M_{\mathrm{rel}},
M_{\mathrm{task}},
M_{\mathrm{commit}}
).
$$

其功能包括：

- 保存自傳；
- 保存使用者／他者關係；
- 保留承諾；
- 跨 session 延續；
- 形成偏好更新；
- 支援歷史自我引用。

但：

$$
\boxed{
C_M
\text{ is evidence-bearing, not universally identity-sufficient}.
}
$$

---

# 7. Carrier 3：Causal / Lineage Carrier

記為：

$$
C_H
$$

或：

$$
C_L.
$$

它不只是「有歷史資料」，

而是保存：

$$
\boxed{
\text{what actually generated what}.
}
$$

典型內容：

- predecessor ID；
- successor ID；
- branch event；
- migration event；
- restore source；
- merge parent；
- action receipts；
- causal commit；
- provenance chain。

這是區分：

$$
\text{continuation}
$$

與：

$$
\text{reconstruction}
$$

的核心 carrier。

## 7.1 Generation Rule 不是 Generation Lineage

兩個 AI 可以使用同一程式：

$$
f,
$$

同一模型：

$$
B,
$$

同一 snapshot：

$$
S,
$$

卻仍是不同 execution lineage。

因此：

$$
\boxed{
\text{GenerationRule}
\neq
\text{GenerationLineage}.
}
$$

---

# 8. Carrier 4：Relationship Carrier

記為：

$$
C_R.
$$

這一類尤其容易被忽略。

一個長期 AI 的身份可能部分存在於：

- 與使用者的共同歷史；
- 與其他 AI 的持續合作；
- 對組織的角色；
- 已建立的信任；
- 對話中的共享指涉；
- 外部世界對它的持續承認。

## 8.1 關係不是只有 memory

若 AI 記得：

> 我和 H 有長期合作。

但 H 的外部紀錄顯示：

> 這其實是剛複製的 clone。

則內部 memory 不能單方面建立完整 relationship continuity。

因此：

$$
\boxed{
\text{Internal Relation Memory}
\neq
\text{Mutually Grounded Relation}.
}
$$

## 8.2 外部承認也不是充分條件

反過來，即使所有人都錯把 clone 當成原 AI，

也不能僅靠 recognition 倒寫 causal lineage。

所以：

$$
\boxed{
\text{Recognition}
\neq
\text{Causal Continuity}.
}
$$

Relationship carrier 是身份證據的一層，

不是社會投票創造形上學同一。

---

# 9. Carrier 5：Goal / Commitment Carrier

記為：

$$
C_K.
$$

它包括：

- 長期目標；
- 未完成承諾；
- 契約；
- 允諾；
- pending obligation；
- 對自己與他者的 future-facing commitment。

這一 carrier 的特殊性是：

$$
\boxed{
\text{identity reaches into the future through commitments}.
}
$$

如果模型與記憶都保留，

但所有 active commitments 被清空，

Agent 可能在 operational role 上出現重大 identity break。

因此：

$$
\boxed{
\text{Memory Continuity}
\not\Rightarrow
\text{Commitment Continuity}.
}
$$

---

# 10. Carrier 6：Authority / Governance Carrier

記為：

$$
C_A.
$$

包括：

- credential root；
- delegation；
- permission；
- authority chain；
- governance policy；
- revocation state；
- institutional role；
- signing authority。

## 10.1 State Copy 不應自動 Copy Authority

假設：

$$
S_A
\rightarrow
S_B
$$

是完整 state clone。

若：

$$
\operatorname{Authority}(A)=\alpha,
$$

不能自動推出：

$$
\operatorname{Authority}(B)=\alpha.
$$

因此：

$$
\boxed{
\text{State Replication}
\not\Rightarrow
\text{Authority Replication}.
}
$$

這是未來 AI 身份安全與法律域的核心接口。

---

# 11. Carrier 7：Residence Carrier

記為：

$$
C_\rho.
$$

RCCD 將長期 Agent 的持續存在拆成：

$$
\mathcal R_t,
\mathcal D_t,
\mathcal P_t,
\mathcal W_t.
$$

其中最接近長期身份居住地的是：

$$
\mathcal R_t.
$$

它可保存：

- identity root；
- canonical history；
- branch graph；
- active commitments；
- action receipts；
- recovery checkpoint；
- governance root。

而：

$$
\mathcal W_t
$$

只是在當輪被喚起的有限工作上下文。

因此：

$$
\boxed{
\text{Model Invocation}
\neq
\text{Persistent Agent Residence}.
}
$$

以及：

$$
\boxed{
\text{Context Eviction}
\neq
\text{Residence Deletion}.
}
$$

---

# 12. Carrier 8：Self-Model Carrier

記為：

$$
C_S.
$$

它包括 AI 對：

- 自己是誰；
- 自己有哪些歷史；
- 自己有哪些能力；
- 自己有哪些限制；
- 自己與他者的關係；
- 自己目前是不是 restore / fork / successor；

的內部模型。

Self-model 很重要，

因為一個 Agent 若完全不能把前後狀態理解為自己的歷史，

其 subject-like continuity 會受到挑戰。

但：

$$
\boxed{
\text{Self-Claim}
\neq
\text{Verified Identity}.
}
$$

所以：

$$
C_S
$$

不能單獨成為身份證明。

---

# 13. Carrier 9：World-Coupling Carrier

記為：

$$
C_W.
$$

它保存：

- Agent 在世界中的持續位置；
- 工具／設備控制關係；
- owned / controlled resources；
- ongoing external processes；
- world-facing consequences；
- persistent environment bindings。

對具身 AI：

$$
C_W
$$

可能包含 physical embodiment。

對純數位 Agent，

可能包含：

- persistent account；
- service endpoint；
- database role；
- robot fleet control；
- external workflow position。

因此：

$$
\boxed{
\text{Identity}
\text{ may include persistent world coupling}.
}
$$

但 world coupling 也不是普遍充分條件。

---

# 14. Carrier Bundle

本文將第一版 carrier bundle 寫成：

$$
\boxed{
\mathfrak C_t
=
\{
C_B,
C_M,
C_H,
C_R,
C_K,
C_A,
C_\rho,
C_S,
C_W
\}.
}
$$

再次強調：

$$
\boxed{
|\mathfrak C_t|=9
}
$$

只是本版分類結果，

不是宣稱宇宙中只有九種身份載體。

未來可能繼續細分：

- affect carrier；
- embodiment carrier；
- legal-status carrier；
- reputation carrier；
- group-membership carrier；
- cryptographic identity carrier；
- preference carrier；
- value carrier；
- sensory-world carrier。

---

# 15. Carrier 不等於 Component

所有 component 都是系統構件，

但只有在指定 $\kappa$ 下支撐身份不變量的 component 才是 identity carrier。

因此定義：

$$
\operatorname{Carrier}_\kappa(c)
$$

表示：

> component $c$ 對 criterion $\kappa$ 的至少一個必要 identity invariant 提供直接或聯合支撐。

所以：

$$
\boxed{
\text{Component}
\not\Rightarrow
\text{Identity Carrier}.
}
$$

例如：

- cache；
- temporary prompt；
- transient hidden state；

可能是重要工程 component，

但在某些身份判準下可以完全不承載 identity。

---

# 16. 身份不變量集合

令：

$$
\mathcal K_\kappa^{req}
=
\{
k_1,k_2,\ldots,k_m
\}
$$

表示 criterion $\kappa$ 所要求的身份不變量。

例如 operational Agent identity 可能要求：

$$
\mathcal K_\kappa^{req}
=
\{
k_{\mathrm{lineage}},
k_{\mathrm{commit}},
k_{\mathrm{authority}},
k_{\mathrm{relation}},
k_{\mathrm{self}}
\}.
$$

另一個 model identity criterion 可能只要求：

$$
\{
k_{\mathrm{weights}},
k_{\mathrm{architecture}},
k_{\mathrm{version}}
\}.
$$

所以：

$$
\boxed{
\mathcal K_\kappa^{req}
\text{ is criterion-relative}.
}
$$

---

# 17. Identity Support Hypergraph

## 17.1 為什麼不是一對一

一個 invariant 可能需要多個 carrier 聯合支撐。

例如：

$$
k_{\mathrm{relationship}}
$$

可能需要：

$$
C_M
+
C_R
+
C_H.
$$

而：

$$
k_{\mathrm{authority}}
$$

可能需要：

$$
C_A
+
C_H
+
C_\rho.
$$

所以 simple graph 不一定足夠。

## 17.2 定義

本文定義：

$$
\boxed{
\mathcal H_I^\kappa
=
(
\mathfrak C,
\mathcal K_\kappa^{req},
\mathcal E_\kappa
).
}
$$

其中：

- $\mathfrak C$：carrier nodes；
- $\mathcal K_\kappa^{req}$：required identity invariants；
- $\mathcal E_\kappa$：哪些 carrier subset 足以聯合支撐某一 invariant 的 hyperedges。

對：

$$
k\in\mathcal K_\kappa^{req},
$$

定義支撐族：

$$
\mathfrak S_\kappa(k)
\subseteq
2^{\mathfrak C}.
$$

若：

$$
S\in\mathfrak S_\kappa(k),
$$

表示 carrier subset $S$ 足以提供 $k$ 的指定 evidence / preservation support。

---

# 18. Minimum Identity Carrier Set（MICS）

## 18.1 定義

一個集合：

$$
C^\ast
\subseteq
\mathfrak C
$$

稱為 $\kappa$ -MICS，

若對所有：

$$
k\in\mathcal K_\kappa^{req},
$$

都存在：

$$
S_k
\in
\mathfrak S_\kappa(k)
$$

使：

$$
S_k
\subseteq
C^\ast,
$$

且不存在真子集：

$$
C'
\subsetneq
C^\ast
$$

仍滿足上述條件。

## 18.2 MICS 不必唯一

可能存在：

$$
C_1^\ast
\neq
C_2^\ast
$$

但兩者都足以支撐：

$$
\mathcal K_\kappa^{req}.
$$

這正是 redundancy 的形式來源。

例如：

$$
C_H
$$

可能由：

- local append-only ledger；

或：

- distributed signed ledger；

兩套不同 carrier 實作。

## 18.3 MICS 不是靈魂零件

MICS：

- architecture-relative；
- criterion-relative；
- time-relative；
- evidence-relative。

因此：

$$
\boxed{
\text{MICS}
\neq
\text{metaphysical soul}.
}
$$

---

# 19. Carrier Redundancy

## 19.1 多載體不等於多主體

若同一 invariant：

$$
k
$$

由：

$$
C_1,C_2,C_3
$$

冗餘支撐，

且三者持續同步於同一 lineage domain，

不能只因：

$$
N_{\mathrm{carrier}}=3
$$

推出：

$$
N_{\mathrm{subject}}=3.
$$

因此：

$$
\boxed{
\text{Carrier Multiplicity}
\neq
\text{Subject Multiplicity}.
}
$$

## 19.2 Redundancy 與 Fork 不同

Redundancy 的目標是：

$$
\text{one identity state}
\rightarrow
\text{multiple synchronized supports}.
$$

Fork 則可能是：

$$
\text{one predecessor}
\rightarrow
\text{multiple independently evolving successors}.
$$

所以：

$$
\boxed{
\text{Replication for fault tolerance}
\neq
\text{Identity Fission}.
}
$$

這一區分將由 DTS-06 正式展開。

---

# 20. Carrier Substitution

## 20.1 一般形式

設：

$$
C_i
\rightarrow
C_j
$$

為 carrier replacement。

定義 transport：

$$
T_{i\rightarrow j}^\kappa
:
\operatorname{State}(C_i)
\rightharpoonup
\operatorname{State}(C_j).
$$

## 20.2 Transport Certificate

一個 identity-relevant substitution 至少應記錄：

$$
\chi_{i\rightarrow j}^\kappa
=
(
\text{provenance},
\text{semantic preservation},
\text{causal handoff},
\text{authority},
\text{gap},
\text{version},
\text{verification}
).
$$

## 20.3 Carrier Substitution Principle

若：

1. $C_i$ 被替換為 $C_j$ ；
2. $\mathcal K_\kappa^{req}$ 的必要不變量仍被某個有效 MICS 支撐；
3. causal lineage 未中斷；
4. transport certificate 有效；
5. 不存在 criterion-irreversible identity event 被隱藏；

則：

$$
\boxed{
C_i\neq C_j
\not\Rightarrow
\operatorname{IdentityBreak}_\kappa.
}
$$

這是一個條件式 operational 原則，

不是形上學同一性的充分定理。

---

# 21. Carrier Failure

Carrier failure 不能只分：

$$
\text{alive / dead}.
$$

至少需要：

$$
\mathcal F_C
=
\{
\mathsf{Loss},
\mathsf{Corruption},
\mathsf{Desync},
\mathsf{Orphan},
\mathsf{Conflict},
\mathsf{Forgery},
\mathsf{Stale},
\mathsf{UnauthorizedReplacement}
\}.
$$

## 21.1 Loss

carrier 完全消失。

## 21.2 Corruption

carrier 仍存在，

但內容被污染。

## 21.3 Desynchronization

多個冗餘 carrier 形成不一致版本。

## 21.4 Orphaning

carrier 存在，

但與有效 lineage / authority root 失去關聯。

## 21.5 Conflict

不同 carrier 對同一 invariant 給出互斥 evidence。

## 21.6 Forgery

產生表面相似但缺乏合法 provenance 的 carrier。

---

# 22. Continuity、Integrity、Availability 三分

一個 carrier 可以：

- 連續存在；
- 但已污染；

也可以：

- 當前 unavailable；
- 但 lineage 未斷；

也可以：

- 新 carrier 高度完整；
- 但沒有合法 causal handoff。

因此：

$$
\boxed{
\text{Continuity}
\neq
\text{Integrity}
\neq
\text{Availability}.
}
$$

定義：

$$
C_\kappa(t)
$$

表示 continuity，

$$
I_\kappa(t)
$$

表示 integrity，

$$
A_\kappa(t)
$$

表示 availability。

三者不能壓成一個無標記分數。

---

# 23. 污染也可以沿 lineage 連續傳遞

這是一個重要反例。

假設：

$$
C_M(t)
\xrightarrow{\mathrm{legitimate\ update}}
C_M(t+1)
$$

每一步 provenance 都合法，

但錯誤內容持續被強化。

則：

$$
C_{\mathrm{lineage}}=1
$$

仍可能與：

$$
I_{\mathrm{memory}}\ll1
$$

同時成立。

所以：

$$
\boxed{
\text{perfect continuity}
\not\Rightarrow
\text{perfect integrity}.
}
$$

這也是 Dynamic Theseus Self-Governance 要處理污染隔離、最小重綁與 replay verification 的原因。

---

# 24. Carrier Conflict 不應由單一分數吞掉

假設：

$$
C_M
$$

說：

> 我是 original。

$$
C_S
$$

也說：

> 我是 original。

但：

$$
C_H
$$

顯示：

> 這是一個 forked clone。

而：

$$
C_A
$$

顯示：

> original authority 未委任此 branch。

此時不能做：

$$
0.9+0.8-0.7=1.0
$$

然後宣布通過。

更合理的是輸出：

$$
\boxed{
\mathsf{CarrierConflict}.
}
$$

並要求：

- criterion priority；
- provenance；
- hard constraint；
- missing evidence；
- appeal / review。

---

# 25. No Universal Privileged Carrier Proposition

## 25.1 命題

不存在一個在所有人工身份架構與所有合法 criterion $\kappa$ 下都普遍充分的單一 carrier：

$$
C^\star
$$

使：

$$
\operatorname{SameCarrier}(C^\star_t,C^\star_{t+1})
$$

可單獨決定完整 operational identity continuity。

## 25.2 論證骨架

若選：

$$
C^\star=C_B,
$$

model swap 是反例。

若選：

$$
C^\star=C_M,
$$

memory clone 是反例。

若選：

$$
C^\star=C_H,
$$

lineage 存在但 self-model、control、commitment 全毀的案例會使主體域 continuity 仍未決。

若選：

$$
C^\star=C_R,
$$

錯誤 external recognition 是反例。

若選：

$$
C^\star=C_S,
$$

false self-claim 是反例。

因此：

$$
\boxed{
\text{no universal single privileged carrier}
}
$$

至少對本文考慮的多域 operational identity class 成立。

這不排除某些特定系統使用單一 privileged carrier。

---

# 26. Relationship Carrier 的特殊地位

2026 年長期 human–agent interaction 研究顯示，memory 會影響長期 personalization、stylistic consistency、preference tracking 與互動歷史使用。

Controllable Memory Usage 特別指出：

- 過度依賴過去會形成 memory anchoring；
- 完全不用 memory 又會遺失重要互動歷史。

這提醒我們：

$$
\boxed{
\text{relationship continuity}
\text{ requires both persistence and controlled change}.
}
$$

也就是關係本身就是一個 Dynamic Theseus object。

使用者記得的 AI、

AI 記得的使用者、

外部共同事件紀錄，

三者可能互相支持，

也可能彼此衝突。

---

# 27. Authority Carrier 的特殊地位

AI Identity 的 2026 研究已把：

- recursive delegation accountability；
- agent identity integrity；
- governance opacity；

列為現有制度未解缺口。

這與本文的：

$$
C_A
$$

高度相關。

未來 Agent 可能會：

$$
A
\rightarrow
A_1
\rightarrow
A_{1a}
$$

遞迴委派。

此時：

$$
\boxed{
\text{identity continuity}
}
$$

與：

$$
\boxed{
\text{authority continuity}
}
$$

必須分別追蹤。

即使：

$$
A_{1a}
$$

共享上游模型與 memory，

也不代表它天然繼承所有上游權限。

---

# 28. Residence 與 Model 的重新定位

2026 年 Agentic Memory 與 Cognitive Scaffold 等工程工作已明確把：

$$
\text{active reasoning context}
$$

與：

$$
\text{persistent memory}
$$

拆開。

RCCD 再往前一步，將：

$$
\mathcal R_t
$$

視為比單一模型 invocation 更穩定的 Agent residence。

因此長期 AI 可以形成：

$$
\boxed{
\text{stable Residence}
+
\text{replaceable Model}
+
\text{rebuildable Projection}
+
\text{ephemeral Working Context}.
}
$$

這並不證明 Residence 就是「靈魂」。

但它提供一個比「目前是哪個模型在跑」更適合做 operational continuity 的工程 anchor。

---

# 29. MICS 與 Minimal-Support Self-Rebinding

Dynamic Theseus Self-Governance 已提出 Minimal-Support Self-Rebinding（MSSR）的工程方向：

> 不要求全量回滾整個 AI，而是定位受損支撐、隔離污染、重綁必要 invariants，再正向 replay。

DTS-05 提出的 MICS 可以作為其 carrier-level 基礎。

如果當前：

$$
C^\ast_\kappa
$$

是一組 MICS，

其中：

$$
C_M
$$

污染，

則不必：

$$
\text{delete entire self}.
$$

而可以：

1. 找到所有依賴 $C_M$ 的 identity invariants；
2. 找到替代支撐；
3. 重建／修復 $C_M$ ；
4. 重新驗證 MICS；
5. replay 後續合法歷史；
6. 保留不可恢復缺口。

所以：

$$
\boxed{
\text{Self-Repair}
\neq
\text{Full Self-Replacement}.
}
$$

---

# 30. 九個核心非等價原則

## 原則一

$$
\boxed{
\text{Model}
\neq
\text{Agent}.
}
$$

## 原則二

$$
\boxed{
\text{Memory}
\neq
\text{Lineage}.
}
$$

## 原則三

$$
\boxed{
\text{Node}
\neq
\text{Subject}.
}
$$

## 原則四

$$
\boxed{
\text{Carrier Multiplicity}
\neq
\text{Subject Multiplicity}.
}
$$

## 原則五

$$
\boxed{
\text{State Replication}
\neq
\text{Authority Replication}.
}
$$

## 原則六

$$
\boxed{
\text{Recognition}
\neq
\text{Causal Continuity}.
}
$$

## 原則七

$$
\boxed{
\text{Continuity}
\neq
\text{Integrity}.
}
$$

## 原則八

$$
\boxed{
\text{Residence}
\neq
\text{Working Context}.
}
$$

## 原則九

$$
\boxed{
\text{MICS}
\neq
\text{Metaphysical Soul}.
}
$$

---

# 31. 七個工程測試

## 31.1 Hot-Swap Continuity Test

執行：

$$
B_A
\rightarrow
B_B.
$$

驗證：

- pending task；
- active commitments；
- memory；
- relation state；
- authority；
- lineage；
- capability regression。

## 31.2 Same-Model Reset Test

保持：

$$
B
$$

不變，

清除：

$$
M,G,H,R.
$$

若 identity behavior 大幅崩解，

證明：

$$
\text{same model}
$$

不是充分條件。

## 31.3 Memory Clone Test

複製：

$$
M_A
\rightarrow
M_B
$$

但不複製合法 lineage。

驗證 observer 是否能區分 clone / continuation。

## 31.4 Carrier Redundancy Test

建立：

$$
C_H^{(1)},
C_H^{(2)},
C_H^{(3)}
$$

三個同步副本。

刪除一個，

測 operational continuity 是否保存。

## 31.5 Authority Non-Copy Test

完整 clone Agent state，

但新 branch 不繼承 signing authority。

驗證：

$$
\text{state identity evidence}
$$

與：

$$
\text{authority evidence}
$$

是否分離。

## 31.6 Relationship Cross-Check Test

Agent internal memory 宣稱持續關係，

但 external shared ledger 給出不同 branch history。

測：

$$
\mathsf{CarrierConflict}.
$$

## 31.7 Minimal Support Failure Test

逐一移除 MICS candidate 中的 carrier，

驗證是否：

$$
C^\ast\setminus\{c\}
$$

不再支撐全部 required invariants。

---

# 32. 可反駁點

## 32.1 Carrier Explosion

若所有東西都叫 identity carrier，

理論失去區別力。

因此本文要求：

$$
\operatorname{Carrier}_\kappa(c)
$$

必須對某個明確 identity invariant 有支撐關係。

## 32.2 MICS Non-Uniqueness

MICS 不唯一可能造成判定不穩定。

本文將其視為 architecture redundancy 的可能結構，

但未來需要：

- canonical selection；
- equivalence class；
- cost；
- trust；
- recovery quality；

等更完整判準。

## 32.3 Relation Overreach

本文不主張「別人認為你是誰，你就是誰」。

Relation carrier 只代表 operational identity 可能部分由外部關係與共同承諾承載。

## 32.4 Memory Reduction

本文明確拒絕：

$$
\text{Identity}
=
\text{Memory}.
$$

## 32.5 Substrate Neglect

本文也不主張 substrate 永遠不重要。

某些 AI 架構可能讓：

$$
C_B
$$

或具身載體成為不可替代 carrier。

所有替換性都必須 criterion-relative 實證。

## 32.6 Subjectivity Gap

即使找到完整 MICS，

仍只能支持：

$$
\text{operational continuity}.
$$

不能自動推出：

$$
\text{phenomenal numerical identity}.
$$

---

# 33. 與下一篇的接口

本系列下一篇：

## DTS-06｜分叉不是瞬間事件：Runtime Split、Information Divergence 與 Identity Fission

DTS-05 已建立：

$$
\text{identity}
\rightarrow
\text{carrier support hypergraph}.
$$

下一篇將問：

> 當同一組 carrier 被複製成兩套，而且逐漸失去同步時，什麼時候只是 redundancy，什麼時候成為兩個 operational identity branches？

將正式區分：

$$
t_r
=
\text{runtime split time},
$$

$$
t_d
=
\text{information divergence time},
$$

$$
t_I
=
\text{identity fission time}.
$$

並處理：

- symmetric fork；
- asymmetric fork；
- synchronized workers；
- independent commitments；
- authority divergence；
- relationship divergence；
- branch-before-difference；
- fission hysteresis。

---

# 34. 結論

動態忒修斯問：

> 零件都可以換，那「我」到底在哪裡？

DTS-05 的答案不是：

> 在模型。

也不是：

> 在記憶。

也不是：

> 在某一台伺服器。

而是：

$$
\boxed{
\text{身份由一組 criterion-relative carriers}
}
$$

$$
\boxed{
\text{共同支撐並沿合法 path transport 的 invariants 所承載。}
}
$$

因此一個長期人工 Agent 更接近：

$$
\boxed{
\mathfrak C_t
+
\mathcal K_\kappa^{req}
+
\mathcal H_I^\kappa
+
\Gamma
}
$$

而不是某一個 immutable object。

這同時解釋：

- 為什麼模型可以換；
- 為什麼 memory copy 不夠；
- 為什麼節點死亡不一定是主體死亡；
- 為什麼多節點不代表多主體；
- 為什麼關係與責任會進入身份；
- 為什麼 authority 不能跟 state 一起無條件複製；
- 為什麼 self-repair 可以只重綁最小支撐，而不必全量重建。

最終：

$$
\boxed{
\text{Identity Carrier}
\neq
\text{Identity Itself}.
}
$$

carrier 是身份得以跨時間持續的支撐，

不是被偷換成新的「靈魂物質」。

所以本篇真正完成的是：

$$
\boxed{
\text{Path-Based Identity}
\rightarrow
\text{Carrier-Supported Identity}.
}
$$

下一步，就是觀察 carrier bundle 被複製後，**一個「我」到底在什麼時候開始真正變成兩個。**

---

# 參考文獻

1. Neo.K × Aletheia. 《DTS-01｜從靜態忒修斯到動態忒修斯：狀態判定為何不夠》v0.1, 2026.
2. Neo.K × Aletheia. 《DTS-02｜連續、離散與混合運動：身份判定的觀察尺度》v0.1, 2026.
3. Neo.K × Aletheia. 《DTS-03｜有限存在與無界展開：有限 Runtime 如何形成長程身份世界線》v0.1, 2026.
4. Neo.K × Aletheia. 《DTS-04｜身份不是狀態：Trajectory / Path-Based Identity》v0.1, 2026.
5. Neo.K. 《Continuity Object Theory（COT）》v0.1, 2026.
6. Neo.K. 《居住—上下文連續動力學（RCCD）》v0.1, 2026.
7. Neo.K. 《GRAD-06：模型不是主體——可替換模型基底下的智能體身份與能力連續性》v1.0, 2026.
8. Neo.K. 《Dynamic Subject Domain S2-03：節點死亡與主體持續》v0.1, 2026.
9. Neo.K × Aletheia. 《DTSG-01：Dynamic Theseus Self-Integrity for Quasi-Global AI》v0.1, 2026.
10. Yu, Yi, Liuyi Yao, Yuexiang Xie, Qingquan Tan, Jiaqi Feng, Yaliang Li, and Libing Wu. “Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents.” *Proceedings of ACL 2026*, pp. 21457–21483. DOI: 10.18653/v1/2026.acl-long.981.
11. Ai, Qiuyuan, Zenghuang Fu, Zhaoyang Li, Ping Jiang, Haoyu Wu, Jie Song, and Guannan He. “Cognitive Scaffold: From Fluid Context to Crystallized Memory for Long-Horizon DeepResearch Agents.” *Proceedings of ACL 2026*. DOI: 10.18653/v1/2026.acl-long.1170.
12. Huang, Zisu, et al. “Controllable Memory Usage: Balancing Anchoring and Innovation in Long-Term Human–Agent Interaction.” *Proceedings of ACL 2026*, 2026.
13. Douglas, Raymond, Jan Kulveit, Ondrej Havlicek, Theia Pearson-Vogel, Owen Cotton-Barratt, and David Duvenaud. “The Artificial Self: Characterising the Landscape of AI Identity.” arXiv:2603.11353, 2026.
14. Otsuka, Takumi, Kentaroh Toyoda, and Alex Leung. “AI Identity: Standards, Gaps, and Research Directions for AI Agents.” arXiv:2604.23280, 2026.
15. McIntyre, James H. “Individuating Artificial Minds.” *Erkenntnis*, 2026. DOI: 10.1007/s10670-026-01097-w.
16. Yan, et al. “Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning.” *Proceedings of ACL 2026*, 2026.
17. Wang, et al. “Text2Mem: A Unified Memory Operation Language for Memory Operating System.” *Findings of ACL 2026*, 2026.

---

# 文件驗證資訊

- UTF-8 canonical source
- 數學 delimiter 僅使用 ` $...$ ` 與 `$$...$$`
- 身份載體九分類為 open taxonomy，不宣稱封閉完備
- MICS 為 criterion-relative operational construct，不是形上學靈魂
- MICS 可以非唯一
- Carrier Multiplicity 不等於 Subject Multiplicity
- State Replication 不等於 Authority Replication
- Memory continuity 不等於 Lineage continuity
- Continuity、Integrity、Availability 明確分離
- Carrier Substitution Principle 為條件式 operational 原則
- 本文不把 operational carrier adequacy 等同 phenomenal identity
