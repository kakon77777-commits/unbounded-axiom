# AI-Native Unified Search Intelligence (AUSI) Series — Paper 03

## 任務驅動的自主搜尋規劃：AI Search Planner、動態方法選擇與 Search Plan Optimization

**English Title:** *Task-Driven Autonomous Search Planning: AI Search Planners, Dynamic Method Selection, and Search Plan Optimization*

**Version:** v0.1  
**Date:** 2026-08-30  
**Status:** Canonical Draft  
**Series:** AI-Native Unified Search Intelligence (AUSI)  
**Predecessor:** Paper 02 — *統一搜尋方法空間：Search Method Ontology 與可組合搜尋算子*  
**Reference Implementation Direction:** `ai-web-research`

---

## 摘要

當 AI 擁有多個搜尋方法與多個資料 provider 後，下一個核心問題不再是「如何搜尋」，而是「在此刻應該執行哪一個搜尋行動」。既有 interactive information retrieval、session search、reinforcement learning for IR、Agentic RAG、Search Agent 與 deep research 系統已分別研究多輪 query reformulation、狀態—行動—回饋建模、動態 retrieval、Web navigation 與 reasoning-time search。然而，對一個通用 AI 搜尋基礎設施而言，planner 的 action space 不應只由 query reformulation 或單一 search tool 構成，而應包含不同 Search Method、不同 Provider、不同參數、不同平行與條件式組合，以及停止本身。

本文提出 **AI Search Planner（AISP）** 的初步形式框架，將自主搜尋建模為一個具有部分可觀察性、外部世界變動、來源與合法性約束、有限資源與多目標效用的 sequential decision problem。本文延續 Paper 02 的 Search Method Ontology，將單一步驟行動表示為：

$$
a_t=(M_i,P_j,\theta_t,\Gamma_t)
$$

其中 $M_i$ 為搜尋方法、 $P_j$ 為 provider、 $\theta_t$ 為方法參數、 $\Gamma_t$ 為執行與 policy guards。Planner 根據任務 $T$ 、可觀察搜尋狀態 $S_t$ 、證據狀態 $E_t$ 、coverage / uncertainty 狀態與剩餘 budget，動態產生或修正 Search Graph。可行行動必須先通過 capability、合法性、授權、成本、隱私與其他 constraints，再進入效用排序。

本文提出一個多目標 Search Utility，其組成包含 expected evidence gain、coverage gain、uncertainty reduction、freshness、source authority、diversity、cost、latency 與 risk。本文進一步將 stopping 視為 planner 的正式 action，而不是搜尋流程之外的例外：當下一步搜尋的預期邊際價值低於其成本與風險，或任務的 evidence / coverage acceptance criteria 已滿足，系統可以停止；若高風險任務的缺口仍存在，則停止可以被禁止。本文也提出 parallelization、counter-evidence scheduling、provider substitution、replanning triggers、bounded planning horizon 與 Search Receipt 等機制。

本文不主張所有搜尋問題都需要 reinforcement learning，也不假設可求得全域最優搜尋策略。相反地，本文提出一個模型無關的 planner contract，使 rule-based、optimization-based、LLM-based、learned policy 與 hybrid planner 都能在同一 Search State、Method Registry 與 policy boundary 上工作。此框架為後續「合法資料取得與來源治理」以及「從搜尋結果到證據」提供決策層地基。

**關鍵詞：** Search Planner、AI-Native Search、Sequential Decision Making、POMDP、Interactive Information Retrieval、Session Search、Agentic RAG、Search Agent、Search Optimization、Evidence Gain、Search Stopping

---

# 1. 從「會搜尋」到「會決定怎麼搜尋」

Paper 01 建立了 AI-Native Search 的基本命題：

> 搜尋策略本身應成為 AI 可操作的物件。

Paper 02 接著建立 Search Method Ontology，將不同搜尋法抽象成：

$$
\mathcal{M}
=
\{M_1,M_2,\ldots,M_n\}
$$

並將不同資料來源或執行後端抽象成：

$$
\mathcal{P}
=
\{P_1,P_2,\ldots,P_k\}
$$

因此，新的問題不再是缺乏能力，而是能力過多：

> **AI 在什麼時候，應該從哪些方法與 provider 中選出哪一個組合？**

若沒有 Planner，一個具有 50 個搜尋工具的 AI 仍可能：

- 永遠只用其中一個；
- 隨機選工具；
- 選到技術上能執行但語義上不適合的方法；
- 重複發送近似 query；
- 在單一 provider 中陷入 confirmation loop；
- 一直搜尋而不知道何時停止；
- 忽略資料取得是否合法；
- 找到大量結果卻沒有形成更強的 evidence state。

因此：

$$
\boxed{
\text{Search Capability}
\neq
\text{Search Planning}
}
$$

而：

$$
\boxed{
\text{Search Intelligence}
=
\text{Capabilities}
+
\text{Planning}
+
\text{Evidence State}
+
\text{Constraints}
}
$$

---

# 2. 既有研究已證明搜尋可以被視為序列決策

AI Search Planner 並不是從無到有發明「搜尋可以多輪決策」。

## 2.1 Query Reformulation 與 Session Search

Web search 長期研究 query reformulation pattern、search session 與 successive queries。這些工作已經表明，一次搜尋後的觀察會改變下一次 query。

因此：

$$
Q_{t+1}
=
f(Q_t,O_t)
$$

比固定 query 更符合真實搜尋。

## 2.2 POMDP Session Search

Luo、Zhang、Dong 與 Yang 在 2015 年研究如何為 session search 設計 POMDP 的 states、actions 與 rewards；後續 Yang 等人在 2018 年完整使用 POMDP 建模 session search 的 rich interaction 與 temporal dependency。

這提供一個重要理論先例：

> Search process 可以被表示成 partially observable sequential decision problem。

## 2.3 Direct Policy Learning

Luo、Dong 與 Yang 也在 2015 年提出 Session Search by Direct Policy Learning，直接學習 search engine action policy。

這說明：

$$
\pi(a_t\mid S_t)
$$

本身可以成為搜尋研究對象，而不只是 retrieval score。

## 2.4 Agentic Retrieval 與 Deep Research

2025 年的 Search-o1 將搜尋插入 reasoning process，使模型在知識不足時動態取得外部資訊；WebThinker 則進一步讓 reasoning model 自主搜尋 Web、瀏覽頁面、提取資訊與撰寫研究報告。

因此到 AI Agent 時代，問題已從：

$$
\text{query reformulation}
$$

逐步擴大為：

$$
\text{tool selection}
+
\text{navigation}
+
\text{retrieval}
+
\text{reasoning-time adaptation}
$$

本文的工作是在這條歷史線上再做一層抽象：

> **把 planner 的 action space 從「搜尋詞或某個搜尋工具」擴張為整個 Search Method Ontology。**

---

# 3. Planner 的工作不是產生一串 query

最簡化的搜尋規劃器可能輸出：

```text
query_1
query_2
query_3
```

但這仍是 query-centric model。

本文將 Search Planner 定義為：

> 根據任務、搜尋狀態、可用方法、provider、證據缺口與約束，產生並動態修訂 Search Plan 的決策系統。

因此 Planner 的輸出可以是：

```text
1. Exact identifier lookup
2. If unresolved:
   ├─ lexical high-recall search
   └─ semantic search
3. Fuse candidates
4. Resolve primary sources
5. Search counter-evidence
6. Verify versions
7. Stop if acceptance criteria satisfied
```

這裡：

- query 只是 method parameter；
- provider 可以在執行前才 resolve；
- branch 可以 conditional；
- search 可以 parallel；
- stop 是正式 decision。

---

# 4. Task Specification

定義搜尋任務：

$$
T
=
(
G,
D,
Q_0,
C_T,
A_T,
F_T,
B_T,
R_T,
V_T
)
$$

其中：

- $G$：goal；
- $D$：domain；
- $Q_0$：初始問題、seed 或 request；
- $C_T$：task constraints；
- $A_T$：acceptance criteria；
- $F_T$：freshness requirement；
- $B_T$：budget；
- $R_T$：risk profile；
- $V_T$：verification requirement。

例如：

> 「請找出台灣某經濟指標最新官方數值。」

與：

> 「請全面搜尋一項軟體技術是否可能已有 prior art。」

雖然都叫「搜尋」，但它們的 $T$ 幾乎完全不同。

---

# 5. Task Interpreter：先判斷需要哪一種認知效果

Planner 不應直接從自然語言跳到 provider。

應先取得 task interpretation：

$$
I_T
=
\operatorname{Interpret}(T)
$$

其中至少可以包含：

```text
intent
domain
target_entities
target_relations
required_evidence
freshness
coverage_requirement
precision_requirement
recall_requirement
risk
legal/policy context
acceptable uncertainty
```

例如：

「找最新 CPI」

可能被解析為：

```text
intent = factual-data-retrieval
source_preference = official-primary
freshness = latest
versioning = required
coverage = narrow
verification = metadata + date + series identity
```

「找所有可能 prior art」

則可能是：

```text
intent = high-recall-discovery
source_scope = multi-provider
terminology_expansion = required
classification_search = required
citation_search = useful
coverage = broad
counter-path-search = required
stopping = conservative
```

因此：

$$
\operatorname{Planner}(T)
\neq
\operatorname{Planner}(Q_0)
$$

Task 比 query 更大。

---

# 6. Observable Search State

本文延續 Paper 02，定義：

$$
S_t
=
(
T,
X_t,
C_t,
E_t,
U_t,
K_t,
B_t,
H_t
)
$$

其中：

- $T$：task；
- $X_t$：當前顯式搜尋表示；
- $C_t$：candidate set；
- $E_t$：evidence state；
- $U_t$：uncertainty / uncovered state；
- $K_t$：已知 source / method / provider operational state；
- $B_t$：remaining budget；
- $H_t$：observable execution history。

這裡特別強調：

> $S_t$ 是外部可操作與可記錄的 Search State，而不是模型私人思考鏈。

Planner 不需要暴露完整 internal reasoning。

它只需要顯式表示足以：

- 檢查下一步是否合法；
- 判斷方法是否適用；
- 重建執行歷史；
- 評估 coverage；
- 驗證 stopping condition。

---

# 7. 部分可觀察性

搜尋世界天然是 partially observable。

例如：

- 我們不知道還有多少未發現來源；
- 不知道某 provider 沒找到是因為不存在，還是 index 缺漏；
- 不知道一個 keyword 是否漏掉某個專業歷史術語；
- 不知道某個網站明天是否更新；
- 不知道所有相關 prior art 是否已被覆蓋。

因此，可以引入 belief state：

$$
b_t(z)
=
P(z\mid H_t,E_t,C_t)
$$

其中 $z$ 表示尚未直接觀察的任務相關世界狀態。

但本文不要求 runtime 必須實作完整 Bayesian POMDP。

實務上可以用：

```text
coverage map
uncertainty tags
missing-source flags
unexplored branches
confidence intervals
heuristic gap scores
```

近似 belief state。

因此：

$$
\text{POMDP interpretation}
$$

是一個有用理論模型，而不是唯一 implementation。

---

# 8. Search Action

Paper 02 已定義 Method 與 Provider 分離。

本文定義單一 action：

$$
a_t
=
(
M_i,
P_j,
\theta_t,
\Gamma_t
)
$$

其中：

- $M_i$：Search Method；
- $P_j$：Provider；
- $\theta_t$：method parameters；
- $\Gamma_t$：guards / execution conditions。

例如：

$$
a_t
=
(
M_{\text{backward-citation}},
P_{\text{OpenAlex}},
\{\text{seed}=d_7,\text{depth}=1\},
\Gamma_{\text{allowed}}
)
$$

或者：

$$
a_t
=
(
M_{\text{structured-retrieval}},
P_{\text{official-api}},
\{\text{series}=x,\text{period}=y\},
\Gamma_{\text{freshness}}
)
$$

---

# 9. Stop 也是 Action

本文把停止明確加入 action space：

$$
a_{\text{stop}}
\in
\mathcal{A}_t
$$

因為：

> 不知道何時停止的 autonomous search 不是完整 planner。

Stop 可以有不同 reason code：

```text
goal_satisfied
coverage_sufficient
evidence_sufficient
budget_exhausted
policy_blocked
provider_exhausted
marginal_gain_too_low
human_review_required
unresolvable_uncertainty
```

因此 Search Receipt 可以區分：

> 「找完了」

與：

> 「因為已經不能合法或合理地繼續，所以停止」。

---

# 10. 可行行動集合

不是所有方法都可以隨時執行。

先由 method precondition：

$$
\operatorname{Pre}(M_i,S_t)=1
$$

篩選。

再要求 provider capability：

$$
P_j\models M_i
$$

再要求政策與執行 guard：

$$
\operatorname{Allowed}(M_i,P_j,T,S_t)=1
$$

因此：

$$
\mathcal{A}_t^{\text{feasible}}
=
\{
(M_i,P_j,\theta)
\mid
\operatorname{Pre}=1,
P_j\models M_i,
\operatorname{Allowed}=1
\}
\cup
\{a_{\text{stop}}\}
$$

這個集合非常重要。

Planner 不應先想：

> 「最好的搜尋方法是什麼？」

而應先問：

> 「哪些行動現在是可行而且允許的？」

---

# 11. Hard Constraints 與 Soft Objectives 必須分離

某些條件不能透過 utility compensation。

例如：

- 不允許的自動化存取；
- 不足的使用授權；
- 不允許將私人資料送給外部 provider；
- 超過不可突破的費用上限；
- 需要人類核准的高風險動作。

因此：

$$
\operatorname{Allowed}=0
$$

時，即使預期資訊價值再高，也不能由其他正分抵銷。

所以：

$$
\text{hard constraints}
\neq
\text{negative utility}
$$

這將在 Paper 04 的合法資料取得與來源治理中完整展開。

---

# 12. Planner Utility

對可行行動，Planner 才進行 ranking。

定義：

$$
U(a_t\mid S_t,T)
=
w_E\hat{E}
+
w_C\hat{C}
+
w_U\hat{U}
+
w_F\hat{F}
+
w_A\hat{A}
+
w_D\hat{D}
-
w_K\hat{K}
-
w_L\hat{L}
-
w_R\hat{R}
$$

其中：

- $\hat{E}$：expected evidence gain；
- $\hat{C}$：expected coverage gain；
- $\hat{U}$：expected uncertainty reduction；
- $\hat{F}$：freshness value；
- $\hat{A}$：source authority / appropriateness；
- $\hat{D}$：diversity gain；
- $\hat{K}$：cost；
- $\hat{L}$：latency；
- $\hat{R}$：remaining execution / epistemic risk。

權重：

$$
w_*
$$

由 task 決定，而不是全域固定。

---

# 13. 多目標而不是單一分數

實務上，所有 objective 壓成一個 scalar 可能造成錯誤。

因此可以把 planner objective 表示成向量：

$$
\mathbf{u}(a)
=
(
E,
C,
U,
F,
A,
D,
-K,
-L,
-R
)
$$

再使用：

- lexicographic priority；
- Pareto frontier；
- constrained optimization；
- task-specific scalarization；
- rule + score hybrid。

例如 high-risk patent search 可以先要求：

$$
C\ge C_{\min}
$$

與：

$$
E\ge E_{\min}
$$

再在可行計畫中最小化 cost。

這比：

> 「便宜很多，所以 coverage 少一點也沒關係」

更符合專業搜尋。

---

# 14. Expected Evidence Gain

Candidate 數量不是 planner 最重要的 reward。

定義：

$$
\Delta E(a_t)
=
\mathbb{E}
[
Q_E(E_{t+1})-Q_E(E_t)
\mid a_t
]
$$

其中 $Q_E$ 是 evidence quality function。

Evidence gain 可以來自：

- 找到 primary source；
- 找到獨立 corroboration；
- 找到 contradiction；
- 找到 version history；
- 將來源身份解析清楚；
- 將 claim 與 source passage 建立對應。

因此：

$$
100\text{ new URLs}
$$

可能比：

$$
1\text{ primary-source confirmation}
$$

價值更低。

---

# 15. Coverage Gain

定義 coverage space：

$$
\Omega_T
$$

它可以依任務分解成：

- terminology；
- provider；
- source type；
- time；
- jurisdiction；
- language；
- classification；
- perspective；
- entity；
- evidence role。

已覆蓋集合：

$$
\Omega_t^{\text{covered}}
$$

則：

$$
C_t
=
\frac{
\mu(\Omega_t^{\text{covered}})
}{
\mu(\Omega_T)
}
$$

在實際系統中 $\mu$ 不一定是真正 measure。

它可以是：

- checklist coverage；
- weighted category coverage；
- graph-region coverage；
- provider coverage；
- domain-specific coverage rubric。

重要的是：

> coverage 必須成為可觀察 state，而不是模型一句「應該差不多了」。

---

# 16. Uncertainty Reduction

定義：

$$
U_t
=
\operatorname{Uncertainty}(S_t)
$$

下一步搜尋的價值可以是：

$$
\Delta U(a_t)
=
U_t-\mathbb{E}[U_{t+1}\mid a_t]
$$

但是「不知道」至少要區分：

```text
not searched
searched_not_found
provider_not_covered
contradicted
version_ambiguous
source_unverified
insufficient_evidence
```

因此：

$$
\text{missing}
\neq
\text{false}
$$

而：

$$
\text{searched-not-found}
\neq
\text{globally absent}
$$

這對 stopping 特別重要。

---

# 17. Value of Information

搜尋本質上是付出成本來改變資訊狀態。

因此可以借用 Value of Information 的一般思想：

$$
\operatorname{VOI}(a_t)
=
\mathbb{E}
[
V(S_{t+1})-V(S_t)
\mid a_t
]
$$

若：

$$
\operatorname{VOI}(a_t)
>
\operatorname{Cost}(a_t)
$$

則搜尋具有繼續價值。

但在 AUSI 中，Cost 不只金錢：

$$
\operatorname{Cost}
=
C_{\text{money}}
+
C_{\text{time}}
+
C_{\text{compute}}
+
C_{\text{quota}}
+
C_{\text{risk}}
$$

對某些 high-risk task，還需要將未搜尋的 residual risk 納入。

---

# 18. Search Graph 而不是固定 Pipeline

Planner 產生：

$$
G_t^{\text{search}}
=
(V_t,E_t^G)
$$

其中 node 可以是：

- method action；
- fusion；
- verification；
- branch；
- guard；
- stop。

Search Graph 可以一開始只有粗略 skeleton：

```text
discover
  ↓
fuse
  ↓
verify
  ↓
stop?
```

執行後再動態展開。

這種：

$$
\text{Plan}
\rightarrow
\text{Execute}
\rightarrow
\text{Observe}
\rightarrow
\text{Replan}
$$

比一次產生 30 個固定 query 更適合 open-world search。

---

# 19. Planning Horizon

若每次都規劃到搜尋終點，可能產生：

- 計畫成本過高；
- 外部資訊很快使遠期計畫失效；
- provider 可用性改變；
- query branches 爆炸。

因此可以使用 receding horizon：

$$
\pi_H(S_t)
=
(a_t,\ldots,a_{t+H})
$$

只規劃有限 horizon $H$。

執行前幾步後重新估計。

這與 Model Predictive Control 類似，但本文只借用 bounded replanning 的思想，不主張 Search Planner 等同於控制系統。

---

# 20. Replanning Triggers

不必每一個 observation 都完整重新規劃。

可以定義 trigger：

$$
\rho(S_t,O_t)\in\{0,1\}
$$

例如以下狀況觸發：

```text
new_entity_discovered
unexpected_contradiction
primary_source_found
provider_failed
coverage_gap_changed
budget_threshold_crossed
freshness_conflict
version_conflict
policy_state_changed
high-value branch emerged
```

這可以降低 planner overhead。

---

# 21. Method Selection 與 Provider Selection 分兩階段

Planner 可以先問：

> 現在需要什麼 epistemic effect？

例如：

$$
g_{\text{verify}}
$$

然後 Registry 找到：

$$
\{
M_{\text{primary-source-resolve}},
M_{\text{cross-source-corroborate}},
M_{\text{version-check}}
\}
$$

再根據 provider capabilities 選擇：

$$
P_j
$$

因此：

$$
\text{Need}
\rightarrow
\text{Method}
\rightarrow
\text{Provider}
$$

通常比：

$$
\text{Need}
\rightarrow
\text{Provider}
$$

更可重用。

---

# 22. Provider Routing

若多個 provider 都支援同一方法，Planner 可以估計：

$$
U(P_j\mid M_i,T,S_t)
$$

考慮：

- coverage；
- authority；
- freshness；
- cost；
- quota；
- latency；
- jurisdiction；
- rights；
- prior success；
- duplicate-source risk。

Provider routing 因此本身也是 decision problem。

若首選 provider 失敗：

$$
P_1
\xrightarrow{\text{fail}}
P_2
$$

但 fallback 必須保留 semantic equivalence。

不能把：

> 官方資料 API 失敗

直接 fallback 成：

> LLM 自己回憶一個數字

然後仍標記為相同 evidence type。

---

# 23. Parallelization

什麼時候應該平行搜尋？

若兩個 action：

$$
a_i,a_j
$$

具有高資訊互補性：

$$
\operatorname{Complement}(a_i,a_j)
$$

且共享 dependency 少，可以 parallel。

例如：

$$
M_{\text{lexical}}
\parallel
M_{\text{semantic}}
$$

或：

$$
M_{\text{official-source}}
\parallel
M_{\text{counter-evidence}}
$$

但若 $a_j$ 高度依賴 $a_i$ 的結果，就不應平行。

因此可以估計：

$$
\operatorname{ParallelScore}
=
\operatorname{Complementarity}
-
\operatorname{Dependency}
-
\operatorname{DuplicateCost}
$$

---

# 24. Exploration–Exploitation

搜尋也存在 exploration / exploitation trade-off。

Exploitation：

> 對已知高價值來源深入取得更多證據。

Exploration：

> 尋找新的來源、術語、provider、分類與反向路徑。

如果只 exploitation，可能 method collapse。

如果只 exploration，可能成本爆炸。

可以定義：

$$
a_t
=
\begin{cases}
a_{\text{explore}}, & \text{coverage gaps high}\\
a_{\text{exploit}}, & \text{high-value branch unresolved}
\end{cases}
$$

也可以用 learned policy 或 bandit-style estimation。

本文不限定具體方法。

---

# 25. Counter-Evidence Scheduling

反證不應只是最後補一下。

定義當前 proposition set：

$$
\mathcal{H}_t
=
\{h_1,\ldots,h_m\}
$$

若某命題對最終結論影響很大：

$$
\operatorname{Impact}(h_k)\gg 0
$$

但目前只有支持證據：

$$
E^+(h_k)\gg E^-(h_k)
$$

Planner 可以增加 counter-search priority：

$$
U_{\text{counter}}(h_k)
\propto
\operatorname{Impact}(h_k)
\cdot
\operatorname{Asymmetry}(E^+,E^-)
$$

這不是假設每個命題都必須找到反證。

而是：

> 高影響且高度單邊的 evidence state 應觸發主動反證搜尋。

---

# 26. Source Diversity 與 Independence

多 provider 不等於多獨立來源。

例如十個新聞頁面都引用同一新聞稿。

因此 Planner 應考慮：

$$
D_t
=
\operatorname{SourceIndependence}(E_t)
$$

若新增結果只是同源轉載：

$$
\Delta D\approx 0
$$

則 utility 應降低。

這能避免：

> 數量很多，看起來就比較可信

的錯誤。

---

# 27. Temporal Planning

對 current-data task，搜尋順序與時間有關。

可以區分：

$$
t_{\text{event}}
$$

$$
t_{\text{publication}}
$$

$$
t_{\text{revision}}
$$

$$
t_{\text{retrieval}}
$$

Planner 若發現兩個數值不同，不能立即判定 contradiction。

可能只是：

$$
\text{different vintage}
$$

因此需要插入：

$$
M_{\text{version-reconcile}}
$$

而不是繼續 general web search。

---

# 28. Search Stopping

停止條件應至少包含三類。

## 28.1 Goal-Based Stop

$$
A_T(S_t)=1
$$

任務 acceptance criteria 已滿足。

## 28.2 Marginal-Value Stop

若所有可行非停止 action：

$$
\max_{a\in\mathcal{A}_t^{\text{feasible}}\setminus\{\text{stop}\}}
\operatorname{NetGain}(a)
<
\epsilon
$$

則停止。

## 28.3 Forced Stop

例如：

- budget exhausted；
- legal/policy blocked；
- rate limit；
- provider unavailable；
- human escalation required。

Forced stop 不代表 task success。

---

# 29. High-Risk Stopping Gate

對高風險搜尋，不能只看 marginal value。

定義 mandatory coverage set：

$$
\Omega_T^{\text{must}}
$$

若：

$$
\Omega_T^{\text{must}}
\not\subseteq
\Omega_t^{\text{covered}}
$$

則：

$$
a_{\text{stop}}
$$

可能被禁止，除非 stop reason 是：

```text
blocked
unavailable
human_escalation
```

這對 prior-art、regulatory、safety-critical research 特別重要。

---

# 30. Planner 不應宣稱「全面搜完」

Open-world search 通常無法證明：

$$
\Omega_t^{\text{covered}}
=
\Omega_{\text{world}}
$$

因此 Search Receipt 應該說：

```text
searched scope
covered providers
covered methods
covered languages
covered dates
known gaps
unavailable sources
policy-blocked regions
residual uncertainty
```

而不是：

> 已經搜尋全部網路。

這是 epistemic honesty 的架構要求。

---

# 31. Search Receipt 與 Planner Audit

Planner 每一步至少記錄：

$$
r_t
=
(
S_t^{\text{summary}},
M_i,
P_j,
\theta_t,
\Gamma_t,
O_t,
\Delta E_t,
\Delta C_t,
cost_t,
status_t
)
$$

整個 Receipt：

$$
\mathcal{R}
=
\{r_1,\ldots,r_n\}
+
\Sigma
$$

其中 $\Sigma$ 是 stop / completion summary。

Receipt 不保存私人 Chain-of-Thought。

它保存：

> 外部搜尋行為與可審計決策資料。

---

# 32. Planner Architecture 不綁定 LLM

本文刻意不定義：

$$
\pi=\text{LLM}
$$

Planner 可以是：

## 32.1 Rule-Based

例如：

```text
if official_current_data:
    official_api_first
```

優點：

- deterministic；
- easy to audit。

## 32.2 Optimization-Based

在明確 utility / constraints 下求解。

## 32.3 Learned Policy

從 Search Receipt 或 benchmark 學習。

## 32.4 LLM-Based Planner

利用語義理解與 flexible plan generation。

## 32.5 Hybrid Planner

例如：

```text
LLM proposes plan
↓
typed validator
↓
policy gate
↓
optimizer / router
↓
runtime execution
```

本文認為 Hybrid 在近期工程上特別合理，因為 LLM 適合 task interpretation 與 method proposal，而 deterministic validators 適合守住 hard constraints。

---

# 33. Planner Proposal 與 Execution Authority 分離

即使 AI Planner 建議：

$$
a_t
$$

也不代表它可以直接執行。

可以定義：

$$
\operatorname{Propose}(a_t)
$$

與：

$$
\operatorname{Authorize}(a_t)
$$

分離。

因此：

$$
\text{Planning Capability}
\neq
\text{Execution Authority}
$$

例如：

- public read-only API 可自動執行；
- 付費昂貴 provider 需要 budget gate；
- 私人企業資料需要 data-policy gate；
- 可能觸發外部副作用的工具需要額外 authority。

---

# 34. Composition-Level Planning

Paper 02 定義：

$$
M_a\triangleright M_b
$$

$$
M_a\parallel M_b
$$

$$
M_a\oplus M_b
$$

$$
M^*_{\sigma}
$$

Planner 不只選單一步驟，也可以選 macro-plan。

例如：

$$
\pi(S_t)
=
M_{\text{diverge}}
\triangleright
(
M_{\text{lexical}}
\parallel
M_{\text{semantic}}
)
\triangleright
M_{\text{fusion}}
$$

Macro 可以降低 action-space complexity。

但是 macro 必須可以被 runtime 展開與 audit。

---

# 35. Hierarchical Planning

因此可以引入兩層：

$$
\pi_{\text{high}}
:
T,S_t
\rightarrow
\text{Search Strategy}
$$

$$
\pi_{\text{low}}
:
\text{Strategy},S_t
\rightarrow
(M_i,P_j,\theta_t)
$$

例如：

High-level：

```text
high-recall discovery
→ evidence verification
→ counter-search
```

Low-level：

```text
CPC expansion
→ EPO lexical search
→ semantic patent provider
→ family normalization
```

這與 Hierarchical RL 有概念上的相似性，但本文不限定訓練方式。

---

# 36. Planner Memory

Planner 需要的記憶不是完整對話。

至少可以拆成：

## 36.1 Task Memory

本輪目標與 constraint。

## 36.2 Search State Memory

已執行哪些方法與 query。

## 36.3 Evidence Memory

哪些候選已進入 evidence ledger。

## 36.4 Provider Memory

quota、failure、latency、coverage observation。

## 36.5 Strategy Memory

哪些 branch 已失敗、哪些仍未探索。

這些皆可被結構化。

---

# 37. Domain Example A：經濟研究

任務：

> 找某國某指標最新官方值並比較最近五次 historical revision。

Task Interpreter：

```text
goal = authoritative structured data
freshness = latest
versioning = mandatory
coverage = narrow
risk = medium
```

Planner：

$$
M_{\text{series-resolve}}
\triangleright
M_{\text{official-provider-route}}
\triangleright
M_{\text{structured-retrieve}}
$$

接著：

$$
M_{\text{vintage-retrieve}}
\triangleright
M_{\text{version-reconcile}}
$$

若 series identity 有歧義，才新增：

$$
M_{\text{metadata-search}}
$$

不應一開始大量 general Web Search。

---

# 38. Domain Example B：氣象研究

任務：

> 取得特定地點過去 30 年每日降雨觀測。

Planner 可能先：

$$
M_{\text{spatial-resolve}}
\triangleright
M_{\text{station-discovery}}
$$

再判斷 station coverage。

若 missingness 過高：

$$
M_{\text{alternate-station}}
\parallel
M_{\text{alternate-dataset}}
$$

再：

$$
M_{\text{temporal-filter}}
\triangleright
M_{\text{structured-acquisition}}
\triangleright
M_{\text{quality-metadata}}
$$

此任務的主要瓶頸可能不是 query quality，而是：

- station identity；
- observation continuity；
- metadata；
- missing data；
- dataset version。

---

# 39. Domain Example C：Patent Prior-Art Search

任務：

> 對一項新軟體功能做高覆蓋率 prior-art discovery。

Task profile：

```text
recall = high
coverage = broad
jurisdiction = multi
language = multi
classification = required
citation = required
stopping = conservative
```

Planner 初始圖：

$$
M_{\text{feature-decompose}}
\triangleright
(
M_{\text{term-expand}}
\parallel
M_{\text{classification-expand}}
\parallel
M_{\text{semantic-discovery}}
)
$$

候選融合後：

$$
M_{\text{family-resolve}}
\triangleright
M_{\text{priority-date}}
$$

對 high-value seed：

$$
M_{\text{backward-citation}}
\parallel
M_{\text{forward-citation}}
$$

coverage gap 若顯示某語言 / classification 未覆蓋：

$$
M_{\text{gap-directed-search}}
$$

最後生成：

```text
coverage map
search receipt
candidate prior art
family map
unsearched regions
residual uncertainty
```

而不是宣稱：

> AI 已證明沒有其他專利。

---

# 40. Domain Example D：學術研究

任務：

> 建立某研究問題主要理論、支持與反對文獻。

Planner：

$$
M_{\text{concept-diverge}}
\triangleright
(
M_{\text{lexical}}
\parallel
M_{\text{semantic}}
\parallel
M_{\text{academic-provider-search}}
)
$$

取得 seeds 後：

$$
M_{\text{citation-expand}}^*
$$

但若 citation expansion 只集中於同一研究群：

$$
M_{\text{source-diversify}}
$$

若支持遠多於反對：

$$
M_{\text{counter-evidence}}
$$

若近期研究尚未累積 citation：

$$
M_{\text{recent-date-search}}
$$

因此 Planner 可以針對 method bias 主動補洞。

---

# 41. Planner Failure Modes

## 41.1 Method Collapse

幾乎總是選同一方法。

## 41.2 Provider Collapse

多 provider 架構最後只用一個。

## 41.3 Plan Hallucination

產生 provider 不支援的 method / parameter。

## 41.4 Invalid Composition

前一方法輸出無法成為下一方法輸入。

## 41.5 Budget Blindness

忽略 quota、token、API cost、latency。

## 41.6 Endless Search

無 stopping policy。

## 41.7 Premature Stop

找到一個合理答案就停止，但 mandatory coverage 尚未滿足。

## 41.8 Confirmation Planning

只產生支持當前結論的 search branch。

## 41.9 Coverage Theater

執行大量近似 query，卻錯誤認為 coverage 很高。

## 41.10 Evidence Blindness

Planner 最佳化 result count，不最佳化 evidence quality。

## 41.11 Policy Blindness

先決定最佳 action，再忽略它其實不允許執行。

## 41.12 Replanning Thrash

每取得一個小 observation 就完全重建 plan，造成 planner overhead 與策略不穩定。

---

# 42. Safety 與合法性不是後處理

對 Search Planner 最重要的治理原則之一是：

$$
\text{Allowed Search Space}
\subseteq
\text{Technically Possible Search Space}
$$

因此 future runtime 應：

```text
candidate action
↓
capability validation
↓
policy / rights validation
↓
resource validation
↓
utility ranking
↓
execution
```

而不是：

```text
best action
↓
execute
↓
later check whether it was allowed
```

這也將直接連接 Paper 04。

---

# 43. Planner Benchmark

為驗證 AI Search Planner，需要與多種 baseline 比較。

## B0 — Single Search

固定 provider + 單 query。

## B1 — Query Expansion

LLM 產生多個 query，但方法與 provider 固定。

## B2 — Multi-Tool Agent

AI 可自由選工具，但沒有 Method Ontology / hard planner state。

## B3 — Static Search Graph

人工預先定義完整 pipeline。

## Proposed — Dynamic Method-Aware Planner

具備：

- Task Interpreter；
- Search State；
- Method Registry；
- Provider Router；
- Constraint Gate；
- Evidence / Coverage State；
- Replanning；
- Stopping；
- Receipt。

---

# 44. Benchmark Metrics

不能只測 final answer accuracy。

至少應測：

$$
\text{Task Success}
$$

$$
\text{Plan Validity}
$$

$$
\text{Evidence Quality}
$$

$$
\text{Coverage}
$$

$$
\text{Contradiction Discovery}
$$

$$
\text{Source Independence}
$$

$$
\text{Freshness Correctness}
$$

$$
\text{Provider Substitution Success}
$$

$$
\text{Cost}
$$

$$
\text{Latency}
$$

$$
\text{Stopping Quality}
$$

$$
\text{Policy Violation Rate}
$$

$$
\text{Unsupported Claim Rate}
$$

尤其：

$$
\text{Cost per Verified Finding}
$$

可能比：

$$
\text{queries executed}
$$

更有意義。

---

# 45. Ablation Experiments

可以依序移除：

- Method Ontology；
- Provider separation；
- evidence state；
- coverage state；
- counter-search；
- hard policy gate；
- dynamic replanning；
- stopping policy。

觀察：

$$
\Delta \text{performance}
$$

這才能知道真正有效的是哪一層。

---

# 46. 初步研究命題

## P3.1 — Method-Aware Planning Hypothesis

在具有多種異質搜尋能力的任務中，顯式 Method Ontology 應能提高可執行 Search Plan 的比例。

## P3.2 — Evidence-Aware Planning Hypothesis

若 planner 的 state 包含 evidence quality，而非只包含 retrieved candidates，則其後續行動更可能提升 verified finding quality。

## P3.3 — Coverage-Aware Planning Hypothesis

對高 recall 任務，顯式 coverage map 應降低過早停止與 method collapse。

## P3.4 — Dynamic Replanning Hypothesis

在中間 observation 會顯著改變 task state 的任務上，receding-horizon / dynamic replanning 應優於完全 static pipeline。

## P3.5 — Hard-Gate Hypothesis

將 legality / permission / privacy 等條件實作成 action-space hard constraints，比將其作為 utility penalty 更能避免 policy-invalid search plan。

## P3.6 — Counter-Evidence Scheduling Hypothesis

對 hypothesis-driven research，依 proposition impact 與 evidence asymmetry 動態排程 counter-search，應能提高 contradiction discovery rate。

## P3.7 — Explicit Stopping Hypothesis

將 stopping 建模為 planner action，並使用 acceptance + marginal-value + forced-stop 三類條件，應能降低 endless search 與 premature stop。

---

# 47. Search Planner 的最小介面

Reference runtime 可以先提供：

```text
interpret_task(task)
build_initial_state(task)
enumerate_feasible_actions(state)
score_actions(state, actions)
propose_plan(state, horizon)
validate_plan(plan)
execute_step(step)
update_state(observation)
should_replan(state, observation)
evaluate_stop(state)
emit_receipt(state)
```

這些介面並不要求 planner 是 LLM。

---

# 48. 對 `ai-web-research` 的工程含義

現有 search / crawler / research capabilities 可以保留。

但長期 architecture 應新增：

```text
planning/
    task.py
    interpreter.py
    state.py
    action.py
    feasibility.py
    utility.py
    planner.py
    replanner.py
    stopping.py
    receipt.py

search_methods/
    spec.py
    registry.py
    composition.py

providers/
    registry.py
    policy.py
```

執行路徑：

```text
Task
↓
Task Interpreter
↓
Search State
↓
Method Candidates
↓
Provider Candidates
↓
Hard Constraint Gate
↓
Search Planner
↓
Search Graph
↓
Executor
↓
Observation
↓
Evidence / Coverage Update
↓
Replan or Stop
```

這應比直接把更多 API 一個個塞進 `research.py` 更可持續。

---

# 49. 與 MCP / Tool Protocol 的關係

MCP 或其他 tool protocol 可以暴露：

- provider capabilities；
- Search Methods；
- executor；
- evidence fetch；
- metadata resolution。

但是：

$$
\text{Tool Protocol}
\neq
\text{Search Planner}
$$

Planner 可以透過 MCP 呼叫能力。

MCP 不應決定：

- 何時需要 citation search；
- 何時需要反證；
- 何時 provider coverage 不足；
- 何時停止。

這些屬於 Search Intelligence layer。

---

# 50. Planner 與 Domain Pack

通用 planner 不可能自己知道所有專業搜尋規則。

因此 Domain Pack 可以提供：

```text
task templates
mandatory methods
preferred providers
coverage schema
risk rules
verification rules
stopping gates
```

例如 Patent Domain Pack 可規定：

```text
prior_art:
    classification_search = mandatory
    family_resolution = mandatory
    priority_date_check = mandatory
    coverage_report = mandatory
```

Planner 再在 domain constraints 內自主選擇。

因此：

$$
\text{Autonomy}
=
\text{choice within explicit domain constraints}
$$

而不是毫無邊界。

---

# 51. Planner 的學習

初期可以 rule + LLM。

隨 Search Receipt 累積：

$$
\mathcal{D}
=
\{
(T,S_t,a_t,O_t,\Delta E,\Delta C,cost)
\}
$$

可以訓練：

$$
\hat{U}(a\mid T,S)
$$

或：

$$
\pi(a\mid T,S)
$$

但 learned policy 不能取代 hard validator。

因此未來可能是：

$$
\pi_{\text{learned}}
\rightarrow
\operatorname{Validate}
\rightarrow
\operatorname{Authorize}
\rightarrow
\operatorname{Execute}
$$

---

# 52. Optimal 不代表全域最佳

本文使用 Search Plan Optimization，但需要避免誤解。

對 open-world search：

- action space 很大；
- provider state 會變；
- 結果可能 stochastic；
- coverage 未知；
- 世界資訊持續更新；
- utility 難以精確估計。

因此：

$$
\pi^*
$$

通常不可精確求得。

實際目標更合理地寫成：

$$
\hat{\pi}
=
\operatorname{GoodEnoughPlan}
(
T,S_t,B_t,\text{constraints}
)
$$

也就是：

> 在有限資源與明確約束下，產生可驗證、可審計、可逐步改善的搜尋策略。

---

# 53. 限制

第一，本文的 utility components 尚未給出跨領域通用估計器；不同 domain 必須採用不同 proxy。

第二，coverage 在 open-world search 中無法完全觀察，因此本文的 coverage map 只能作為 operational approximation。

第三，POMDP 是有用的理論參照，但對大規模 Web / multi-provider search，完整求解通常不切實際。

第四，LLM-based planner 仍可能產生無效 method、錯誤 parameter 或不穩定 Search Graph，因此 typed validation 與 runtime checks 仍必要。

第五，本文沒有證明 parallel search 一定降低總 latency；provider quota、shared bottleneck 與 duplicated retrieval 可能使平行化反而更差。

第六，stopping 的「足夠」高度 task-dependent。高風險法律、專利或科研任務不能沿用一般 QA 的 stopping threshold。

第七，本文尚未完整定義 legal / rights / access policy model。這是下一篇的主要工作。

---

# 54. 結論

AI 搜尋真正困難的部分，不只是取得資訊。

當系統同時具有：

- lexical search；
- semantic search；
- classification search；
- citation search；
- graph search；
- structured APIs；
- crawlers；
- multiple Web providers；
- domain databases；
- verification tools；

真正的智能問題變成：

> **下一步應做什麼？**

本文因此將 AI Search Planner 建模為：

$$
\boxed{
\pi:
(T,S_t,\mathcal{M},\mathcal{P})
\rightarrow
a_t
}
$$

其中：

$$
a_t
=
(M_i,P_j,\theta_t,\Gamma_t)
$$

且所有非停止 action 必須先滿足：

$$
\operatorname{Pre}
\land
\operatorname{Capability}
\land
\operatorname{Allowed}
$$

再以：

$$
\text{Evidence Gain}
+
\text{Coverage Gain}
+
\text{Uncertainty Reduction}
+
\text{Freshness}
+
\text{Authority}
+
\text{Diversity}
-
\text{Cost}
-
\text{Latency}
-
\text{Risk}
$$

進行 task-conditioned evaluation。

完整 Search Intelligence 因而變成：

$$
\boxed{
\text{Task}
\rightarrow
\text{Interpret}
\rightarrow
\text{Plan}
\rightarrow
\text{Search}
\rightarrow
\text{Observe}
\rightarrow
\text{Update}
\rightarrow
\text{Replan}
\rightarrow
\text{Verify}
\rightarrow
\text{Stop}
}
$$

這個 loop 的關鍵不是讓 AI 無限制自主，而是讓 AI 在：

- 明確方法空間；
- 明確 provider 能力；
- 明確合法與政策 boundary；
- 明確 evidence state；
- 明確資源 budget；
- 明確 stopping condition；

之內自主規劃。

Paper 01 定義了 AI-Native Search。

Paper 02 定義了 AI 可以操作的 Search Method Space。

Paper 03 則第一次回答：

> **AI 如何在這個空間中行動。**

下一步將進入整個系列不可省略的治理地基：

> **Paper 04 — 合法資料取得與來源治理：AI 搜尋中的授權、條款、資料權利與 Policy-Constrained Acquisition**

因為從 Planner 開始能自主選擇 provider 之後，下一個不能逃避的問題就是：

$$
\text{Can retrieve}
\not\Rightarrow
\text{May retrieve}
$$

---

# References

[1] Bates, M. J. (1979). *Information Search Tactics*. Journal of the American Society for Information Science, 30(4), 205–214. DOI: 10.1002/asi.4630300406.

[2] Bates, M. J. (1989). *The Design of Browsing and Berrypicking Techniques for the Online Search Interface*. Online Review, 13(5), 407–424.

[3] Boldi, P., Bonchi, F., Castillo, C., Donato, D., Gionis, A., & Vigna, S. (2011). *Query Reformulation Mining: Models, Patterns, and Applications*. Information Retrieval, 14, 257–289. DOI: 10.1007/s10791-010-9155-3.

[4] Luo, J., Zhang, S., Dong, X., & Yang, H. (2015). *Designing States, Actions, and Rewards for Using POMDP in Session Search*. Advances in Information Retrieval, ECIR 2015, 526–537. DOI: 10.1007/978-3-319-16354-3_58.

[5] Luo, J., Dong, X., & Yang, H. (2015). *Session Search by Direct Policy Learning*. Proceedings of ICTIR 2015, 261–270. DOI: 10.1145/2808194.2809461.

[6] Luo, J., Dong, X., & Yang, H. (2015). *Learning to Reinforce Search Effectiveness*. Proceedings of ICTIR 2015, 271–280.

[7] Yang, G. H., Dong, X., Luo, J., & Zhang, S. (2018). *Session Search Modeling by Partially Observable Markov Decision Process*. Information Retrieval Journal, 21(1), 56–80. DOI: 10.1007/s10791-017-9316-8.

[8] Avriel, M., & Williams, A. C. (1970). *The Value of Information and Stochastic Programming*. Operations Research, 18(5), 947–954. DOI: 10.1287/opre.18.5.947.

[9] Morehead, D. R., Pejtersen, A. M., & Rouse, W. B. (1984). *The Value of Information and Computer-Aided Information Seeking: Problem Formulation and Application to Fiction Retrieval*. Information Processing & Management, 20(5–6), 583–601. DOI: 10.1016/0306-4573(84)90075-X.

[10] Li, X., Dong, G., Jin, J., Zhang, Y., Zhou, Y., Zhu, Y., Zhang, P., & Dou, Z. (2025). *Search-o1: Agentic Search-Enhanced Large Reasoning Models*. Proceedings of EMNLP 2025, 5420–5438. DOI: 10.18653/v1/2025.emnlp-main.276.

[11] Li, X., Jin, J., Dong, G., Qian, H., Wu, Y., Wen, J.-R., Zhu, Y., & Dou, Z. (2025). *WebThinker: Empowering Large Reasoning Models with Deep Research Capability*. Advances in Neural Information Processing Systems 38. DOI: 10.52202/085713-4011.

[12] Lewis, P., Perez, E., Piktus, A., et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. Advances in Neural Information Processing Systems 33. arXiv:2005.11401.

[13] Yao, S., Zhao, J., Yu, D., et al. (2023). *ReAct: Synergizing Reasoning and Acting in Language Models*. International Conference on Learning Representations. arXiv:2210.03629.

[14] Singh, A., Ehtesham, A., Kumar, S., Khoei, T. T., & Vasilakos, A. V. (2025/2026). *Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG*. arXiv:2501.09136.

[15] Xi, Y., Lin, J., Xiao, Y., et al. (2025). *A Survey of LLM-based Deep Search Agents: Paradigm, Optimization, Evaluation, and Challenges*. arXiv:2508.05668.

---

# Series Continuation

**Paper 04 — 合法資料取得與來源治理：AI 搜尋中的授權、條款、資料權利與 Policy-Constrained Acquisition**

下一篇將正式定義：

$$
\Pi_{\text{allowed}}
\subseteq
\Pi_{\text{technically-possible}}
$$

並建立 Source Policy / Rights Registry，使 Search Planner 在 method / provider selection 階段就能處理：

- API terms；
- automated access；
- scraping permission；
- bulk acquisition；
- caching；
- redistribution；
- commercial use；
- authentication；
- rate limits；
- privacy；
- jurisdiction；
- retention；
- provenance obligations。

也就是讓：

$$
\operatorname{Allowed}(M_i,P_j,T,S_t)
$$

從本文中的抽象 guard，變成正式可實作的治理模型。
