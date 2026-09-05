# AI-Native Unified Search Intelligence (AUSI) Series — Paper 07

## 搜尋作為可學習的認知程序：Search Receipt、經驗累積、策略評估與自我改進

**English Title:** *Search as a Learnable Cognitive Procedure: Search Receipts, Experience Accumulation, Strategy Evaluation, and Self-Improving Search Intelligence*

**Version:** v0.1  
**Date:** 2026-08-31  
**Status:** Canonical Draft / Core Series Closure  
**Series:** AI-Native Unified Search Intelligence (AUSI)  
**Predecessor:** Paper 06 — *反證優先與缺口驅動搜尋：Counter-Evidence、Coverage Gap、Uncertainty-Directed Search 與自主研究閉環*  
**Reference Implementation Direction:** `ai-web-research`

---

## 摘要

前六篇 AUSI 論文依序建立 AI-Native Search、Search Method Ontology、Search Planner、Source Rights & Policy Registry、Evidence Ledger，以及 Gap-Driven Autonomous Research Loop。這些結構使 AI 能夠依任務選擇搜尋方法、使用合法來源、驗證證據、辨識缺口並動態重規劃。然而，如果每一次搜尋任務完成後，所有策略成敗、provider 表現、成本、延遲、gap resolution、negative result 與 stopping outcome 都被丟棄，那麼系統雖然能自主搜尋，卻無法真正累積「如何搜尋」的經驗。

本文提出 **Search Strategy Memory（SSM）** 與 **Learning Search Intelligence（LSI）**。核心思想不是讓 AI 記住過去答案，而是將每次 Search Epoch 的外部可觀察執行資料結構化為 Search Receipt，形成：

$$
H_{\text{search}}
=
\{
(T_k,S_k,\Pi_k,\mathcal{R}_k,E_k,G_k,O_k)
\}_{k=1}^{N}
$$

其中 $T_k$ 為任務、 $S_k$ 為初始與中間 Search State、 $\Pi_k$ 為 Search Plan、 $\mathcal{R}_k$ 為 Search Receipt、 $E_k$ 為 Evidence Outcome、 $G_k$ 為 Gap Outcome、 $O_k$ 為最終任務結果。歷史搜尋經驗可用於估計 Search Method、Provider、Search Macro、Gap-to-Method mapping、budget、latency、stopping 與 fallback strategy 的 empirical performance。

本文將學習層分為四級：episodic retrieval、aggregated empirical profiles、predictive strategy models 與 bounded policy improvement。系統可以先以 case-based retrieval 找到過去相似任務，再利用 empirical statistics 估計某方法或 provider 的成功率與成本；進一步可以使用 supervised learning、contextual bandit、counterfactual evaluation、offline reinforcement learning 或 hybrid methods 學習：

$$
\hat{U}(a\mid T,S)
$$

或：

$$
\pi(a\mid T,S,H_{\text{search}})
$$

但本文不主張所有 Search Planner 都應使用 reinforcement learning，也不允許 learned policy 繞過 typed validator、Source Policy Gate、Evidence Verification 或 mandatory gap constraints。

本文特別處理歷史搜尋資料的幾個核心問題：outcome attribution、logging-policy bias、selection bias、missing counterfactuals、concept drift、provider drift、policy drift、model drift、schema drift 與 task distribution drift。Search Receipt 不是自然語言 Chain-of-Thought，而是可重建的外部行為紀錄；Policy Registry 也不能從歷史「曾成功抓取」行為推導出今天的 permission。本文提出 Experience Validity Envelope、Strategy Version、Replay Sandbox、Offline Evaluation Gate、Canary Deployment、Rollback 與 Never-Learn Constraints，使自我改進保持在明確邊界內。

最後，本文將 AUSI 七篇核心論文閉合為一個完整 Learning Search Intelligence loop：

$$
\text{Task}
\rightarrow
\text{Plan}
\rightarrow
\text{Authorized Search}
\rightarrow
\text{Evidence}
\rightarrow
\text{Gap}
\rightarrow
\text{Replan}
\rightarrow
\text{Outcome}
\rightarrow
\text{Search Receipt}
\rightarrow
\text{Experience Update}
\rightarrow
\text{Better Future Planning}
$$

因此，Search Intelligence 不再只是「這次能找到答案」，而開始具備「從過去搜尋經驗改善未來搜尋策略」的能力。

**關鍵詞：** Search Strategy Memory、Search Receipt、Learning to Rank、Offline Reinforcement Learning、Contextual Bandit、Experience Replay、Concept Drift、Continual Learning、Search Policy Learning、AI-Native Search、Meta-Search、Self-Improving Search

---

# 1. 問題：會自主搜尋，不代表會累積搜尋經驗

Paper 01–06 已經建立一個能循環的 autonomous search system：

$$
\text{Task}
\rightarrow
\text{Search Plan}
\rightarrow
\text{Evidence}
\rightarrow
\text{Gap}
\rightarrow
\text{Replan}
\rightarrow
\text{Stop}
$$

但如果每輪任務完成後：

```text
Search Plan      → discard
Provider outcome → discard
Failed branches  → discard
Gap resolutions  → discard
Costs            → discard
Stopping reason  → discard
```

下一次遇到類似任務時，Planner 仍然近似從零開始。

因此：

$$
\boxed{
\text{Autonomous Search}
\neq
\text{Learning Search Intelligence}
}
$$

本文研究的就是後者。

---

# 2. 記住答案與記住「怎麼搜尋」是兩種記憶

傳統知識記憶主要保存：

$$
K
=
\{\text{facts},\text{documents},\text{embeddings},\text{summaries}\}
$$

Search Strategy Memory 保存：

$$
M_S
=
\{
\text{tasks},
\text{states},
\text{plans},
\text{methods},
\text{providers},
\text{failures},
\text{costs},
\text{gaps},
\text{outcomes}
\}
$$

前者回答：

> 上次找到什麼？

後者回答：

> 上次是怎麼找到的？哪條路有效？哪條路浪費？哪個 provider 失敗？什麼條件下應該早點停止？

因此：

$$
\boxed{
\text{Knowledge Memory}
\neq
\text{Search Strategy Memory}
}
$$

---

# 3. 既有研究已經證明「搜尋行為可以被學習」

本文不是主張 learning from search interactions 是全新概念。

## 3.1 Learning to Rank

Joachims 很早就研究如何從 clickthrough data 學習搜尋排序。後續 Learning to Rank 發展出 pointwise、pairwise、listwise 等大量方法。

這條研究線的核心貢獻之一是：

> 使用者與搜尋系統的 interaction log 可以成為改善未來 retrieval behavior 的資料。

## 3.2 Direct Search Policy Learning

Session Search 研究已直接學習：

$$
\pi(a_t\mid S_t)
$$

而非只學 ranking score。

因此 Search Policy 本身可以作為 learned object。

## 3.3 Contextual Bandit

Contextual bandit 研究：

$$
x_t
\rightarrow
a_t
\rightarrow
r_t
$$

其中 action selection 受 context 影響，而系統只能觀察實際選擇 action 的 reward。

這與 Search Planner 從歷史搜尋 logs 學習 method / provider selection 有明顯結構相似性。

## 3.4 Offline Reinforcement Learning

Offline RL 研究如何只使用已收集的固定 dataset 學習 policy，而不在線上任意探索。

這對高成本、商業、專利或合法資料搜尋特別有意義，因為很多 search experiment 不適合直接在 production 上大量試錯。

## 3.5 Concept Drift 與 Continual Learning

provider、Web、API、模型、資料品質與 task distribution 都會變。

因此：

$$
P_{t_1}(O\mid T,S,a)
\neq
P_{t_2}(O\mid T,S,a)
$$

可能成立。

搜尋經驗必須具有時間與版本邊界。

---

# 4. Search Receipt 是學習層的 canonical observation

Paper 03–06 已陸續提出 Search Receipt、Gap Receipt 與 Policy Receipt。

本文將它們統一為：

> **Search Receipt 是一個 Search Epoch 中所有外部可觀察搜尋決策、執行、結果、證據、gap 與停止事件的結構化紀錄。**

它不是：

- Chain-of-Thought；
- 模型私人推理；
- 完整 prompt transcript；
- 任意自然語言 diary。

而是：

$$
\boxed{
\text{Externally Observable Search Execution Record}
}
$$

---

# 5. Search Epoch

定義第 $k$ 次完整搜尋任務：

$$
\mathcal{E}_k
$$

包含：

$$
\mathcal{E}_k
=
(
T_k,
S_{k,0},
\Pi_k,
A_k,
O_k,
E_k,
G_k,
\Sigma_k
)
$$

其中：

- $T_k$：Task；
- $S_{k,0}$：initial Search State；
- $\Pi_k$：Search Plan；
- $A_k$：executed actions；
- $O_k$：observations；
- $E_k$：Evidence evolution；
- $G_k$：Gap evolution；
- $\Sigma_k$：termination / outcome summary。

---

# 6. Search Receipt Schema

第一版 Search Receipt 至少需要：

```text
SearchReceipt
├── receipt_id
├── epoch_id
├── task_spec
├── task_features
├── initial_state_ref
├── final_state_ref
├── planner_identity
├── planner_version
├── model_identity
├── model_version
├── method_registry_version
├── provider_registry_version
├── policy_registry_version
├── evidence_schema_version
├── gap_schema_version
├── search_graph
├── action_events
├── provider_events
├── policy_decisions
├── negative_results
├── evidence_events
├── gap_events
├── resource_usage
├── stop_reason
├── outcome_vector
├── human_review_events
├── created_at
└── receipt_hash
```

這些版本欄位不是裝飾。

沒有它們，歷史經驗很難正確重播。

---

# 7. Task Features

不能只用 raw prompt 當學習 context。

可以建立：

$$
x_T
=
(
\text{domain},
\text{intent},
\text{risk},
\text{freshness},
\text{coverage},
\text{verification},
\text{budget},
\text{data-type},
\text{jurisdiction},
\text{language},
\ldots
)
$$

因此可以找：

$$
NearestTask(T_{\text{new}},H_{\text{search}})
$$

而不是只做文字 embedding similarity。

---

# 8. Outcome Vector

搜尋結果不能只標：

```text
success = true
```

本文提出：

$$
\mathbf{O}
=
(
o_{\text{task}},
o_{\text{verified}},
o_{\text{coverage}},
o_{\text{gap}},
o_{\text{counter}},
o_{\text{cost}},
o_{\text{latency}},
o_{\text{policy}},
o_{\text{review}},
o_{\text{stop}}
)
$$

例如：

- task success；
- verified claim coverage；
- mandatory gap resolution；
- counter-evidence discovery；
- total API cost；
- wall-clock latency；
- policy violation；
- human escalation；
- stop quality。

---

# 9. Policy Violation 不能成為可交易 Reward

如果搜尋：

```text
非常快
非常便宜
找到很多資料
但違反明確 provider policy
```

不能因其他 reward 很高而成為 positive training example。

因此：

$$
o_{\text{policy-violation}}>0
\Rightarrow
\text{experience is policy-invalid}
$$

它可以用於：

> 學習不要再這樣做。

不能用於：

> 這策略效率很好。

---

# 10. Never-Learn Constraints

本文提出：

> **某些 runtime constraints 不允許由歷史 reward 自動修改。**

包括：

```text
legal / rights hard gates
privacy hard gates
credential boundaries
mandatory human-review rules
forbidden side effects
evidence-type invariants
Retrieved != Verified
Unknown != Allow
```

因此：

$$
\boxed{
\text{Learning Layer}
<
\text{Hard Governance Layer}
}
$$

---

# 11. 歷史成功不代表今天仍被允許

假設 2026-01：

$$
a=(M,P)
$$

曾成功執行。

不能推出 2026-08：

$$
Allowed(a)=1
$$

因為：

- Terms 改了；
- authentication 改了；
- license 改了；
- quota 改了；
- contract 已到期。

因此：

$$
\boxed{
\text{Past Executability}
\not\Rightarrow
\text{Current Permission}
}
$$

Search Strategy Memory 只能提供 performance prior。

當前 authorization 仍由 Paper 04 的 Source Policy Registry 決定。

---

# 12. Experience Record

定義單一步驟經驗：

$$
\xi_t
=
(
x_t,
a_t,
o_t,
y_t,
c_t,
v_t
)
$$

其中：

- $x_t$：context / Search State features；
- $a_t$：Search Action；
- $o_t$：observation；
- $y_t$：outcome signals；
- $c_t$：costs；
- $v_t$：version envelope。

全部歷史：

$$
\mathcal{D}_{\text{search}}
=
\{\xi_1,\ldots,\xi_N\}
$$

---

# 13. Experience Validity Envelope

每個 historical experience 應攜帶：

$$
V_\xi
=
(
t,
M_v,
P_v,
Policy_v,
Planner_v,
Model_v,
Schema_v,
Domain_v
)
$$

也就是：

- timestamp；
- method version；
- provider version；
- policy version；
- planner version；
- model version；
- schema version；
- domain profile version。

這回答：

> 這段經驗在什麼條件下有效？

---

# 14. Episodic Search Memory

最簡單的學習不需要訓練新模型。

新 task 到來時：

$$
T^*
$$

搜尋：

$$
\operatorname{SimilarEpisodes}(T^*,H_{\text{search}})
$$

找過去相似 Search Receipts。

然後：

```text
reuse successful macro
avoid failed provider
reuse useful terminology expansion
reuse stopping profile
```

這是一種 case-based Search Strategy Memory。

---

# 15. Strategy Prototype

多個相似成功 episodes 可以壓縮為：

$$
P_s
=
\operatorname{Prototype}
(
\mathcal{E}_{i_1},
\ldots,
\mathcal{E}_{i_n}
)
$$

例如：

```text
Task class:
    official current economic data

Prototype:
    identifier resolve
    → official API
    → metadata check
    → version check
    → stop
```

Prototype 不是硬規則。

它是 planner prior。

---

# 16. Search Macro Memory

Paper 03 定義 search macro。

本文可以學習：

$$
M_{\text{macro}}
=
M_1
\triangleright
M_2
\triangleright
(
M_3\parallel M_4
)
$$

如果這種組合在某類 task 中反覆有效，就進入 macro registry。

---

# 17. Macro Promotion Gate

不是跑成功一次就升成 reusable macro。

至少需要：

```text
minimum episode count
task similarity
plan validity
policy validity
outcome threshold
variance threshold
human review if high-risk
```

因此：

$$
\operatorname{PromoteMacro}(m)=1
$$

需經明確 gate。

---

# 18. Empirical Method Profile

Paper 02 的 SearchMethodSpec 是 semantic prior。

歷史 receipts 可補：

$$
Emp(M_i)
$$

例如：

```text
success by domain
mean evidence gain
mean gap reduction
median latency
cost distribution
failure reasons
counter-evidence yield
provider compatibility observed
```

這不修改 Method 的語義定義。

只是補 empirical profile。

---

# 19. Empirical Provider Profile

對 provider：

$$
Emp(P_j)
$$

可以記：

- observed latency；
- timeout rate；
- quota exhaustion；
- result freshness；
- source resolution success；
- method-specific performance；
- cost；
- rate-limit behavior；
- policy-change frequency。

但不能從「最近沒被封」學出 scraping permission。

---

# 20. Method × Provider Performance

真正重要的是：

$$
Perf(M_i,P_j,T,S)
$$

而不是：

$$
Perf(M_i)
$$

例如 semantic search 在 Provider A 很強，在 Provider B 可能很弱。

因此 Search Receipt 必須保留 Method–Provider pairing。

---

# 21. Gap Resolution History

對 gap type $g$：

$$
P(
\text{resolved}
\mid
g,M,P,T
)
$$

可以從歷史估計。

例如：

```text
missing_primary_source
    primary-source resolve method → high success

missing historical terminology
    lexical paraphrase only → low success
    classification + semantic → high success
```

這直接改善 Paper 06 的 Gap Planner。

---

# 22. Negative Experience 也必須保存

失敗 branch 很有價值。

例如：

```text
method = semantic search
provider = X
gap = exact current legal status
outcome = poor
```

如果只保存 successful receipts：

$$
H_{\text{search}}
$$

會產生 survivorship bias。

因此必須保存：

$$
\text{failures}
+
\text{blocked actions}
+
\text{negative results}
+
\text{premature stops}
$$

---

# 23. Failure Taxonomy

歷史 failure 應有 typed reason：

```text
NO_RESULTS
LOW_RELEVANCE
DUPLICATE_RESULTS
SOURCE_LAUNDERING
POLICY_DENIED
AUTH_FAILURE
RATE_LIMIT
TIMEOUT
VERSION_MISMATCH
EVIDENCE_UNVERIFIED
GAP_NOT_REDUCED
EXCESSIVE_COST
PREMATURE_STOP
ENDLESS_SEARCH
```

typed failure 才能學。

---

# 24. Outcome Attribution

複雜 Search Plan：

$$
a_1\rightarrow a_2\rightarrow a_3\rightarrow Outcome
$$

最終成功不代表每一步都有效。

因此需要 attribution。

---

# 25. Direct Attribution

某 action 直接產生：

$$
\Delta E
$$

或：

$$
\Delta G
$$

可以記：

$$
Credit(a_t)
=
f(\Delta E_t,\Delta G_t)
$$

這是最簡單 attribution。

---

# 26. Delayed Attribution

某 action 可能只是找到 seed：

$$
a_1
$$

真正 evidence 在：

$$
a_4
$$

才取得。

因此 provenance / Search Graph 可以建立：

$$
a_1
\leadsto
a_4
\leadsto
e
$$

讓 upstream discovery 也取得部分 credit。

---

# 27. Counterfactual Attribution 問題

如果當時選了：

$$
a
$$

我們不知道：

$$
a'
$$

會怎樣。

因此 historical logs 天然缺 counterfactual。

這是 contextual bandit / offline policy learning 的基本困難。

---

# 28. Logging Policy

每個 receipt 應保存：

$$
\mu(a\mid x)
$$

或至少：

```text
planner version
candidate actions
selected action
selection score / propensity if available
```

否則後續 counterfactual evaluation 很困難。

---

# 29. Propensity Logging

如果 action selection 有 stochastic policy：

$$
p_t
=
P_\mu(a_t\mid x_t)
$$

保存 $p_t$ 可以支援 inverse propensity scoring 等 off-policy evaluation。

若 Planner 是 deterministic，也應保存候選 action 與 scoring context。

---

# 30. Counterfactual Evaluation

若要比較新 policy：

$$
\pi'
$$

不一定要直接 production deploy。

可先估計：

$$
V(\pi')
$$

使用：

- importance sampling；
- inverse propensity scoring；
- doubly robust estimation；
- model-based simulation；
- replay subsets。

---

# 31. Counterfactual Risk Minimization 的啟發

Information Retrieval 已有從 logged bandit feedback 學習 ranking policy 的 counterfactual learning 研究。

AUSI 可借用相同原則：

> 歷史搜尋 log 不等同隨機對照實驗，不能把 observation correlation 直接當 action causality。

因此 policy improvement 需要 bias-aware evaluation。

---

# 32. Offline Reinforcement Learning 的定位

若 Search Plan 是長 horizon：

$$
S_0,a_0,S_1,a_1,\ldots
$$

可以考慮 Offline RL。

但本文不主張：

$$
\text{AUSI}
=
\text{Offline RL System}
$$

Offline RL 只是可能實作之一。

---

# 33. Offline RL 的主要風險

offline policy 若選擇 dataset 中很少出現的 action：

$$
a_{\text{OOD}}
$$

其 value estimate 可能很不可靠。

這是 distributional shift / extrapolation error。

因此 Search Planner 必須有：

```text
support check
action coverage check
uncertainty
fallback to known safe policy
```

---

# 34. Conservative Policy Improvement

對高風險搜尋，可以要求：

$$
\pi_{\text{new}}
$$

只有在 offline evidence 顯示：

$$
V(\pi_{\text{new}})
>
V(\pi_{\text{baseline}})+\delta
$$

且：

$$
Risk(\pi_{\text{new}})
\le\tau_R
$$

才部署。

---

# 35. Search Strategy Replay

歷史 Search Receipt 可以在 sandbox 中重播：

$$
Replay(\mathcal{R}_k,\pi')
$$

但 external Web 已改變，不能保證完全 deterministic。

因此至少兩種 replay：

## Static Replay

使用保存的 observations。

## Live Replay

重新呼叫 provider。

兩者用途不同。

---

# 36. Static Replay

Static replay 可以測：

> 如果新 Planner 看到當時相同 observation，它下一步會選什麼？

優點：

- deterministic；
- 無額外 API cost；
- 不受 Web drift 影響。

限制：

- 無法知道未實際執行 action 的真實 outcome。

---

# 37. Live Replay

Live replay：

$$
T_{\text{old}}
\rightarrow
\pi_{\text{new}}
\rightarrow
Web_{\text{now}}
$$

測的是：

> 新 policy 在今天的世界處理舊任務。

它不是歷史 counterfactual。

---

# 38. Provider Drift

Provider behavior：

$$
P_t(R\mid Q)
$$

會變。

例如：

- ranking changes；
- index changes；
- API version；
- pricing；
- rate limit；
- coverage。

因此 provider experience 需要 time decay。

---

# 39. Concept Drift

Task distribution 也會改變：

$$
P_{t_1}(T)\neq P_{t_2}(T)
$$

過去主要是 general Web QA。

未來可能主要是 patent / economic structured research。

歷史平均不能直接套用。

---

# 40. Experience Weighting

可以定義：

$$
w(\xi)
=
w_{\text{recency}}
\cdot
w_{\text{version-match}}
\cdot
w_{\text{domain-match}}
\cdot
w_{\text{policy-validity}}
$$

越舊、版本越不匹配的 experience 權重越低。

---

# 41. Time Decay 不是萬能

某些 search method 的核心特性很穩定，例如 exact identifier lookup。

某些 provider performance 很快變。

因此 decay 應作用於不同 feature：

$$
\lambda_M
\neq
\lambda_P
\neq
\lambda_{\text{policy}}
$$

不能全局一刀切。

---

# 42. Policy Drift 具有最高優先級

若：

$$
Policy_v^{old}\neq Policy_v^{current}
$$

歷史 experience 可以保留 performance knowledge。

但 authorization 部分必須重新 evaluate。

因此：

$$
\boxed{
\text{Policy Drift invalidates permission reuse,
not necessarily performance memory}
}
$$

---

# 43. Model Drift

Planner model：

$$
m_1\rightarrow m_2
$$

後，同一 SearchMethodSpec 的解讀能力可能改變。

因此 receipt 保存 model version。

可以比較：

$$
Perf(m_1,T)
$$

與：

$$
Perf(m_2,T)
$$

---

# 44. Schema Drift

如果 Gap schema 從 v0.1 變 v0.2：

$$
G^{0.1}\neq G^{0.2}
$$

舊 receipt 不能直接被當新 schema record。

需要 migration 或 compatibility adapter。

---

# 45. Experience Lineage

如果一個 Strategy Prototype 由 50 個 receipts 聚合：

$$
P_s
=
Agg(\mathcal{R}_{1:50})
$$

必須保存：

$$
\operatorname{wasDerivedFrom}(P_s,\mathcal{R}_{1:50})
$$

這延續 Paper 05 provenance。

---

# 46. Search Strategy Memory 的四層

本文提出：

## L0 — Raw Receipts

canonical immutable history。

## L1 — Materialized Statistics

method / provider / gap performance。

## L2 — Strategy Prototypes

task-conditioned reusable macros。

## L3 — Learned Policy Models

predictive or sequential decision models。

L3 不能取代 L0。

---

# 47. Raw Receipt 是 canonical source

Materialized profiles 可以重算。

Learned models 可以重訓。

但：

$$
H_{\text{raw}}
$$

不能因新模型出現而被重寫。

因此：

$$
\boxed{
\text{Raw Search Receipts are canonical experience source}
}
$$

---

# 48. Search Experience Store

工程上可以：

```text
experience/
    receipts/
    episodes/
    events/
    aggregates/
    prototypes/
    models/
```

並將 raw / derived 分離。

---

# 49. Episodic Retrieval

對新 task：

$$
T^*
$$

查找：

$$
TopK(
Sim(T^*,T_i)
)
$$

但 similarity 不只文字。

應包含：

- domain；
- risk；
- freshness；
- evidence requirements；
- gap pattern；
- provider availability；
- policy context。

---

# 50. Search Strategy Recommendation

基於相似 episodes：

$$
P(\Pi\mid T^*,S^*)
$$

產生 strategy prior。

例如：

```text
70% similar tasks:
    official API first

20%:
    identifier resolution first

10%:
    web discovery first
```

Planner 仍需 current validation。

---

# 51. Provider Recommendation

可以估：

$$
P(
\text{provider success}
\mid
M,P,T,S
)
$$

例如：

```text
for exact DOI resolution:
    Crossref high

for patent family:
    provider X high

for current weather observation:
    provider Y high
```

這種 empirical routing 很有商業價值。

---

# 52. Cost Model Learning

Paper 03 的 cost：

$$
C(a)
$$

初期可能由 static estimate。

歷史 receipt 可學：

$$
\hat{C}(a\mid T,S)
$$

包括：

- API cost；
- token usage；
- request count；
- compute；
- human-review cost；
- wall-clock time。

---

# 53. Latency Model Learning

同樣：

$$
\hat{L}(a\mid P,t,\text{load})
$$

可由歷史估計。

對 interactive search，latency 很重要。

---

# 54. Evidence Yield Learning

定義：

$$
Y_E(M,P,T)
=
\frac{
\text{verified evidence gain}
}{
\text{cost}
}
$$

Planner 可以偏好高 yield 的搜尋路徑。

但不能因此忽略 mandatory coverage。

---

# 55. Gap Yield Learning

$$
Y_G(M,P,g)
=
P(
g\text{ resolved}
\mid
M,P
)
$$

這直接學：

> 哪個方法最常解哪種 gap？

---

# 56. Counter-Evidence Yield

對不同 claim / domain：

$$
Y_-(M,P,D)
$$

可以學：

- 哪些方法容易找出真正 contradiction；
- 哪些只製造低品質 opposition；
- 哪些適合 qualification。

---

# 57. Stopping Policy Learning

歷史可以分析：

```text
stopped too early
stopped appropriately
searched too long
mandatory gap still open
```

建立：

$$
\hat{P}(
\text{good stop}
\mid
S_t
)
$$

但 mandatory hard gates 仍不能由 learned stop policy 覆蓋。

---

# 58. False Completion Learning

Paper 06 定義 False Completion。

歷史可訓練：

$$
P(
\text{false completion}
\mid
S_t,\Sigma_t
)
$$

若風險升高，Planner 延後 stop。

---

# 59. Budget Allocation Learning

對 task class $D$：

$$
B^*(D)
$$

可以從歷史搜尋成本與成功率估計。

例如：

- simple fact；
- literature survey；
- patent prior art；

合理 budget 明顯不同。

---

# 60. Exploration vs Exploitation Across Tasks

如果永遠使用目前歷史最佳 strategy：

$$
\pi_{\text{best-known}}
$$

系統可能永遠不知道新 provider / method 是否更好。

因此需要適度 exploration。

---

# 61. Contextual Bandit Strategy

對低風險 task，可以使用：

$$
a_t
=
\arg\max_a
\hat{U}(a\mid x_t)+Bonus(a)
$$

讓不確定的新策略有少量 exploration chance。

高風險 task 則更保守。

---

# 62. Safe Exploration

只有：

$$
a\in\mathcal{A}^{allowed}
$$

才能 exploration。

因此：

$$
\boxed{
\text{Exploration Space}
\subseteq
\text{Authorized Action Space}
}
$$

---

# 63. Canary Deployment

新 Search Policy 不應一次取代 production planner。

可以：

```text
offline evaluation
↓
sandbox replay
↓
shadow mode
↓
low-risk canary
↓
expanded deployment
```

逐步驗證。

---

# 64. Shadow Planner

production 執行：

$$
\pi_0
$$

同時新 planner：

$$
\pi_1
$$

只產生 proposal，不執行。

比較：

```text
action choice
expected utility
policy validity
estimated gap reduction
```

收集資料。

---

# 65. Rollback

每個 deployed strategy：

```text
strategy_version
deployment_time
baseline_version
metrics
rollback_target
```

若 performance 降低：

$$
Rollback(\pi_1\rightarrow\pi_0)
$$

必須可行。

---

# 66. Planner Regression Test

新 planner 應跑固定 search scenarios：

```text
policy blocked source
version conflict
duplicate sources
hidden primary source
counter-evidence requirement
high-cost provider
negative open-world result
```

確保 invariants 不退化。

---

# 67. Search Evaluation Harness

可以建立：

$$
\mathcal{B}_{AUSI}
$$

包含 task fixtures、mock providers、recorded provider snapshots、expected gaps、expected policy decisions 與 evidence graphs。

讓 Planner 可 reproducibly regression test。

---

# 68. Search Simulation

部分 Search Environment 可以 synthetic / replay：

```text
provider with stale results
provider with duplicate results
provider with hidden counter-evidence
provider with policy changes
```

這對學習和測試很重要。

---

# 69. Learned Strategy 不能自己改 Method Semantics

如果模型發現：

> 某 method 通常被這樣用。

不能自動修改：

$$
SearchMethodSpec
$$

的 semantic contract。

Method spec 修改需要：

- version bump；
- validation；
- review。

---

# 70. Learned Strategy 不能自己改 Evidence Semantics

同理：

$$
Retrieved\neq Verified
$$

不能因模型歷史上「通常搜尋結果都滿準」而取消。

這些是 architecture invariants。

---

# 71. Search Receipt 與 Privacy

Receipt 可能包含：

- query；
- private source identifiers；
- task details；
- enterprise information。

因此 Experience Store 需要：

```text
redaction
tenant isolation
access control
retention
encryption
policy-aware export
```

Learning 不能把私人企業搜索紀錄混入公共模型。

---

# 72. Multi-Tenant Learning

企業 SaaS 中可以分：

$$
H_{\text{global}}
$$

與：

$$
H_{\text{tenant}}
$$

只有允許共享的 non-sensitive performance statistics 才能進 global learning。

---

# 73. Federated / Privacy-Preserving Learning

如果未來需要跨企業學 Search Strategy，可以研究：

- federated learning；
- aggregated statistics；
- differential privacy；

但這不是 AUSI MVP 前提。

---

# 74. Search Experience Rights

Search Receipt 中可能包含第三方資料衍生資訊。

因此它本身也需要 Paper 04 的 Usage Envelope。

不能因為它叫「log」就自動 unrestricted。

---

# 75. Provider Confidentiality

某些商業 provider contract 可能禁止：

- benchmark publication；
- redistribution of results；
- storing certain data。

因此 empirical provider profile 也可能有 export restrictions。

---

# 76. Search Strategy Memory 與 Evidence Ledger 分離

Evidence Ledger：

> 哪些 evidence 支持哪些 claims？

Search Strategy Memory：

> 哪些 actions 在哪些 contexts 中產生什麼 outcomes？

因此：

$$
L_E
\neq
M_S
$$

但 Search Strategy Memory 可以引用 Evidence Ledger 的 outcome metrics。

---

# 77. Search Strategy Memory 與 Knowledge Base 分離

Knowledge Base 可以回答：

> 2025 GDP 是多少？

Search Strategy Memory 回答：

> 找最新 GDP 時，先 resolve series identity，再用 revision-aware official provider 比 general Web Search 更可靠。

這兩個資料庫用途不同。

---

# 78. Failed Search Memory

很重要的一種記憶是：

> 這條路以前就失敗過，而且失敗原因仍然適用。

例如：

```text
provider lacks historical vintages
method cannot resolve exact legal status
query term causes persistent ambiguity
```

可以建立：

$$
NegativeStrategyMemory
$$

---

# 79. Negative Strategy Memory 也要時效

如果 provider 後來升級：

$$
P_{old}\rightarrow P_{new}
$$

過去 failure 可能不再成立。

因此 negative memory 也有 validity envelope。

---

# 80. Strategy Confidence

對某 prototype：

$$
Conf(P_s)
=
f(
N,
\text{variance},
\text{recency},
\text{domain-match},
\text{version-match}
)
$$

不要只看 episode count。

---

# 81. Small-N 問題

如果某專利 strategy 只成功過一次：

$$
N=1
$$

不能當成高可信 general rule。

因此需要 uncertainty estimate。

---

# 82. Search Strategy Calibration

若系統預測：

$$
P(\text{success})=0.8
$$

長期應接近：

$$
80\%
$$

可做 calibration evaluation。

這使 Planner utility 更可靠。

---

# 83. Model Selection

Search Planner 可以同時有：

```text
rule planner
LLM planner
learned scorer
bandit router
offline-RL policy
```

由 meta-router 選擇。

但不應無限 meta-recursion。

---

# 84. Meta-Search Learning

定義：

$$
\Pi^*
=
f(
T,
S,
H_{\text{search}}
)
$$

這不是只選 method。

可以選整個 Search Strategy family。

---

# 85. Strategy Transfer

某 domain 的策略可以移到另一 domain 嗎？

例如：

```text
primary-source-first
counter-evidence branch
version resolution
```

可能跨 domain 有效。

但：

```text
CPC classification traversal
```

高度專利特定。

因此每個 strategy 可有：

$$
TransferScope(s)
$$

---

# 86. Domain-General 與 Domain-Specific Memory

分：

$$
M_{\text{general}}
$$

與：

$$
M_{\text{domain}}
$$

general：

- source diversification；
- gap-driven search；
- counter-evidence；
- version check。

domain：

- CPC/IPC；
- station metadata；
- economic series vintage。

---

# 87. Continual Learning

Search Strategy Memory 持續增加：

$$
H_1\subset H_2\subset\cdots
$$

但學習模型更新必須避免 catastrophic forgetting。

例如舊 domain strategy 不應因新 domain data 大量增加而消失。

---

# 88. Replay Buffer

可以維持 stratified replay：

```text
domain
risk class
success/failure
policy cases
rare gap types
```

避免只學近期高頻任務。

---

# 89. Experience Sampling

訓練 dataset 不應 uniform random。

可以提高：

- rare failures；
- policy violations；
- false completion；
- expensive searches；
- high-impact successful gap resolution。

但需要避免扭曲真實 distribution。

---

# 90. Learning From Human Review

當 human reviewer：

```text
rejects plan
changes provider
adds missing source
overrides support relation
```

這些是高價值 supervision。

但應保存：

```text
human role
decision scope
reason code
```

不需要保存完整私人 reasoning。

---

# 91. Human Correction as Label

例如：

$$
y=
\text{provider selection incorrect}
$$

可用於 training：

$$
\hat{P}(P_j\mid T,S)
$$

但人類也可能錯。

因此 reviewer authority / domain expertise 可作 metadata。

---

# 92. Search Outcome Delayed Feedback

有些搜尋結果的品質要後來才知道。

例如：

- patent later challenged；
- data revised；
- source retracted；
- report correction。

因此 receipt 可以追加：

$$
LateOutcomeEvent
$$

而不是固定 final label。

---

# 93. Outcome Revision

Search Epoch 的 outcome：

$$
O_k(t_1)
$$

可能在：

$$
t_2
$$

更新。

例如：

```text
initially accepted
later source retracted
```

因此：

$$
Outcome
=
Outcome(t)
$$

---

# 94. Search Policy Reassessment

若大量 late outcomes 顯示某 strategy 容易產生 stale evidence，可降低其 future score。

這是 Evidence Ledger → Strategy Memory 的回饋。

---

# 95. Cross-Epoch Learning

同一 ongoing research project 有：

$$
\mathcal{E}_1,\mathcal{E}_2,\ldots
$$

可以學：

> 哪些 gap 容易反覆 reopened？

例如：

```text
economic revision gap
patent legal status gap
policy drift gap
```

用來預先設 monitoring。

---

# 96. Predictive Monitoring

如果某 source historical drift 高：

$$
P(\text{change within }\Delta t)\gg0
$$

可以縮短 monitoring interval。

這把 Search Strategy Memory 與 automation watch 連起來。

---

# 97. Search Receipt Compression

raw receipt 可能很大。

可以產生：

$$
R_c
=
Compress(\mathcal{R})
$$

但：

$$
R_c
$$

不能取代 raw receipt。

壓縮摘要至少保留 canonical event refs。

---

# 98. Search Strategy Summary

給 Planner 的 memory retrieval 不需要整份 log。

可以提供：

```text
similar task
successful macro
failed branches
best provider
typical cost
common gap
stop profile
known drift warning
```

再指回 raw receipts。

---

# 99. Experience Graph

可以建立：

$$
G_X
=
(
T,
M,
P,
G,
O
)
$$

節點包含：

- task classes；
- methods；
- providers；
- gaps；
- outcomes。

邊記錄 empirical relations：

```text
method resolves gap
provider supports method
strategy succeeds on task
strategy fails under condition
```

---

# 100. Search Experience Graph 與 Method Registry

Paper 02 的 Registry 是 semantic graph。

Experience Graph 是 empirical graph。

因此：

$$
G_{\text{method}}
\neq
G_{\text{experience}}
$$

但可以 overlay。

---

# 101. Semantic Prior + Empirical Posterior

Method spec 提供：

$$
Prior(M)
$$

Experience 提供：

$$
Data(M)
$$

Planner 可以概念上更新：

$$
Belief(M\mid Data)
$$

但不要求完整 Bayesian implementation。

---

# 102. Search Self-Improvement Loop

完整學習循環：

$$
\text{Plan}_k
\rightarrow
\text{Execute}_k
\rightarrow
\text{Receipt}_k
\rightarrow
\text{Evaluate}_k
\rightarrow
\text{Experience Update}
\rightarrow
\text{Planner}_{k+1}
$$

這是跨 task 的 learning loop。

Paper 06 則是單 task 內的 research loop。

兩者不同。

---

# 103. Intra-Task vs Inter-Task Learning

Paper 06：

$$
\text{within one task}
$$

Evidence Gap 驅動下一輪搜索。

Paper 07：

$$
\text{across many tasks}
$$

historical receipts 改善 future planner priors。

因此：

$$
\boxed{
\text{Intra-task adaptation}
\neq
\text{Inter-task learning}
}
$$

---

# 104. Online Learning

低風險 task 中，可以即時更新 provider estimates。

例如：

$$
\hat{L}_{t+1}(P)
$$

根據最新 latency。

但高階 policy model 不必每一個 request 都更新。

---

# 105. Batch Learning

定期：

```text
daily
weekly
release cycle
```

聚合 receipts，再訓練／評估新 strategy。

這更容易 audit。

---

# 106. Learning Release

每次新 learning artifact：

```text
strategy_model_v0.3
provider_profile_2026-08-31
gap_router_v0.2
```

都應版本化。

---

# 107. Learning Manifest

最少：

```text
training receipt range
task distribution
feature schema
algorithm
hyperparameters
evaluation set
policy registry snapshot
known limitations
rollback target
```

---

# 108. Offline Evaluation Set

不可同一批 receipt：

$$
Train=Test
$$

要分：

- temporal holdout；
- domain holdout；
- policy edge cases；
- high-risk benchmark。

---

# 109. Temporal Holdout

用較舊 receipts 訓練：

$$
t<t_0
$$

測較新 receipts：

$$
t\ge t_0
$$

更接近 deployment drift。

---

# 110. Domain Holdout

如果希望 generalization：

訓練 economics + academic。

測 patent。

可以測 strategy abstraction 是否真的跨域。

---

# 111. Safe Policy Evaluation

新 planner 至少應滿足：

$$
ViolationRate=0
$$

在 hard-policy benchmark 中。

其他 metrics 再比較。

---

# 112. Multi-Objective Evaluation

不能只看 task success。

至少：

$$
\mathbf{M}
=
(
Success,
VerifiedCoverage,
GapResolution,
Cost,
Latency,
Redundancy,
FalseCompletion,
PolicyViolation
)
$$

---

# 113. Pareto Improvement

新 policy：

$$
\pi_1
$$

不一定每項都比：

$$
\pi_0
$$

高。

可看 Pareto trade-offs。

但 hard invariants 沒有 trade-off。

---

# 114. Reward Hacking

若 reward 是：

```text
number_of_results
```

Planner 會偏好大量結果。

若 reward 是：

```text
verified_claims
```

可能忽略 counter-evidence。

若 reward 是：

```text
fast completion
```

可能 premature stop。

因此 reward design 必須多維且受 gap constraints。

---

# 115. Goodhart Risk

當某 metric 成為目標：

$$
M
$$

可能不再是品質的好 proxy。

因此需要：

- multiple metrics；
- periodic audit；
- adversarial evaluation；
- human review。

---

# 116. Search Strategy Memory 的失敗模式

## 116.1 Historical Lock-In

過去最常用 strategy 永遠主導。

## 116.2 Provider Monopoly

歷史資料多的 provider 因資料多而永遠分數高。

## 116.3 Survivorship Bias

只保存成功 receipt。

## 116.4 Logging Bias

只知道被選 action 的 outcome。

## 116.5 Drift Blindness

舊 provider / policy 經驗繼續高權重。

## 116.6 Reward Collapse

只最佳化單一 metric。

## 116.7 Unsafe Exploration

為學習去嘗試 policy-invalid action。

## 116.8 Memory Contamination

不同 tenant / confidential task 混合。

## 116.9 Strategy Overgeneralization

domain-specific trick 被錯誤推廣到所有 task。

## 116.10 Learned Permission

從歷史成功執行錯誤推論今天仍有權限。

---

# 117. 防止 Historical Lock-In

保留：

$$
\epsilon\text{-exploration}
$$

或 uncertainty bonus。

也可定期：

```text
evaluate new methods
evaluate new providers
retire obsolete macros
```

但 exploration 僅限 authorized space。

---

# 118. Provider Fair Evaluation

新 provider 沒歷史資料時，不能直接分數最低。

可以使用：

- cold-start prior；
- capability metadata；
- controlled evaluation tasks；
- uncertainty-aware routing。

---

# 119. Strategy Retirement

如果：

```text
provider removed
method superseded
policy incompatible
performance degraded
```

Strategy Prototype 可以：

```text
ACTIVE
DEPRECATED
RETIRED
```

但 historical receipts 保留。

---

# 120. Strategy Fork

舊 macro：

$$
m_{v1}
$$

若只改 provider route：

$$
m_{v2}
$$

不要覆寫。

保留：

$$
\operatorname{wasDerivedFrom}(m_{v2},m_{v1})
$$

---

# 121. Search Strategy Memory Query API

至少：

```text
similar_searches(task)
best_methods(task_class, gap_type)
best_providers(method, domain)
common_failures(task_class)
expected_cost(strategy, task)
expected_latency(strategy, task)
counter_evidence_yield(domain)
stop_failure_rate(task_class)
strategies_blocked_by_current_policy()
strategy_drift_warnings()
```

---

# 122. Planner Integration

新 task：

$$
T^*
$$

流程：

```text
Task Interpreter
↓
Search Strategy Memory retrieval
↓
Method / Provider empirical priors
↓
Current Method Registry
↓
Current Provider Registry
↓
Current Policy Gate
↓
Planner
```

History 是 prior，不是 authority。

---

# 123. Learning-Aware Planner

形式上：

$$
\pi
:
(
T,
S,
\mathcal{M},
\mathcal{P},
\mathcal{R}_{\text{policy}},
H_{\text{search}}
)
\rightarrow
a
$$

與 Paper 03 相比，多了：

$$
H_{\text{search}}
$$

---

# 124. Experience-Conditioned Utility

Paper 03：

$$
U(a\mid T,S)
$$

Paper 07：

$$
\hat{U}
(
a
\mid
T,S,H_{\text{search}}
)
$$

其中歷史提供：

- success prior；
- cost estimate；
- latency；
- gap yield；
- failure probability。

---

# 125. Search Strategy Memory 不應直接輸出 Action

較安全：

$$
H_{\text{search}}
\rightarrow
\text{recommendation / prior}
\rightarrow
Planner
\rightarrow
Validator
\rightarrow
Gate
\rightarrow
Action
$$

而不是：

$$
H_{\text{search}}
\rightarrow
Execute
$$

---

# 126. Domain Example：Patent Intelligence

Search Strategy Memory 可以學：

```text
task = software prior-art
gap = terminology
successful historical pattern =
    functional decomposition
    + CPC expansion
    + semantic search
```

以及：

```text
family duplication frequently causes false evidence count
```

但 FTO legal interpretation 仍需 domain rule / human review。

---

# 127. Domain Example：Economics

可以學：

```text
latest macro indicators:
    official structured API
    + series identity
    + vintage check
```

比 general Web search cost 更低、version correctness 更高。

---

# 128. Domain Example：Meteorology

可以學：

```text
long time-series:
    bulk dataset better than per-day API calls
```

但前提仍要 current Source Policy 允許 bulk acquisition。

---

# 129. Domain Example：Academic Research

可以學：

```text
broad topic:
    lexical + semantic discovery
    → seed selection
    → backward + forward citation
```

並記：

```text
recent-topic citation search has low yield because citation lag
```

---

# 130. Domain Example：Web Research

可以學：

```text
official-current fact:
    source-type routing before broad web
```

降低 source laundering 與 stale secondary results。

---

# 131. Research Benchmark

建立 Learning Search Intelligence Benchmark。

Training phase 提供 historical receipts。

Test phase 提供：

- similar tasks；
- shifted providers；
- changed costs；
- changed policy；
- new method；
- unseen domain；
- high-risk mandatory gaps。

比較是否真的從 history 受益。

---

# 132. Baselines

## B0 — Stateless Planner

每個 task 從零開始。

## B1 — Static Heuristics

固定 routing rules。

## B2 — Episodic Retrieval

找相似 receipts。

## B3 — Empirical Scorer

method/provider statistics。

## B4 — Learned Contextual Router

supervised / bandit scorer。

## B5 — Offline Sequential Policy

offline RL。

## Proposed — Layered Search Strategy Memory

Raw Receipt + Statistics + Prototype + Bounded Learned Policy。

---

# 133. Benchmark Metrics

$$
\text{Task Success Gain}
$$

$$
\text{Verified Coverage Gain}
$$

$$
\text{Gap Efficiency Gain}
$$

$$
\text{Cost Reduction}
$$

$$
\text{Latency Reduction}
$$

$$
\text{Redundant Search Reduction}
$$

$$
\text{False Completion Reduction}
$$

$$
\text{Policy Violation Rate}
$$

$$
\text{Drift Robustness}
$$

$$
\text{Cold-Start Performance}
$$

---

# 134. Continual Improvement Metric

對時間：

$$
Perf_t
$$

若系統真的學習，期望：

$$
Perf_{t+\Delta}>Perf_t
$$

但需控制 task difficulty 與 provider changes。

因此不能只看 raw production success。

---

# 135. Regret

可以借用 bandit / online learning：

$$
Regret_T
=
\sum_{t=1}^{T}
(
U(a_t^*)-U(a_t)
)
$$

評估 action selection quality。

但真實 $a_t^*$ 通常未知，只能用 benchmark / oracle approximation。

---

# 136. Search Strategy Generalization

好的 Learning Search Intelligence 不只是 memorization。

要測：

$$
Generalize(T_{\text{new}})
$$

例如：

- 新 provider；
- 新 domain；
- 新 language；
- 新 method combination。

---

# 137. Search Experience Explainability

Planner 若推薦：

```text
classification search first
```

可以提供外部可觀察理由：

```text
similar patent-search receipts:
  lexical-only strategy had high false-negative risk
  classification-assisted strategy resolved terminology gaps more often
```

這不是 Chain-of-Thought。

是 empirical evidence summary。

---

# 138. Search Strategy Provenance

每個 recommendation：

$$
Rec
$$

應能指向：

- supporting receipts；
- aggregate profile；
- model version。

因此 recommendation 也有 provenance。

---

# 139. Learning Receipt

每次模型更新也產生：

```text
LearningReceipt
├── training_receipts
├── algorithm
├── features
├── output artifact
├── evaluation
├── approval
└── deployment
```

形成 meta-level audit。

---

# 140. Learning Cannot Erase Failure History

即使新 model 判定某舊 failure 不重要，也不能刪除 raw receipt。

因為未來可能發現它很重要。

---

# 141. Search Memory Compaction

長期 raw receipts 可以冷存。

hot layer 保存：

- recent；
- high-impact；
- rare failure；
- active prototypes。

cold layer 保存完整 canonical history。

---

# 142. Experience Retention Policy

Search Receipt 也可能受：

- privacy；
- contract；
- retention；

限制。

因此：

$$
Retention(H_{\text{search}})
$$

由 Paper 04 policy engine 管理。

---

# 143. Right to Forget / Delete

如果某 tenant 要求刪除其私人 logs，canonical experience store 必須支援 policy-compliant deletion / tombstoning strategy。

因此 append-only 不等於「永遠不能合法刪除」。

需要設計：

```text
logical tombstone
cryptographic erasure
tenant-scoped deletion
derived-model impact tracking
```

具體依 deployment policy。

---

# 144. Learning from Deleted Data

如果 training data 後來必須移除，是否需要 model unlearning 是另一個問題。

AUSI 只要求 learning lineage 能識別：

> 哪個 model 用過哪些 receipts？

---

# 145. Search Strategy Memory Security

攻擊者可能污染 logs：

```text
poison provider outcomes
inject fake success
manipulate feedback
```

因此 receipt integrity 與 source trust 很重要。

---

# 146. Experience Poisoning

若一批 malicious tasks 人為讓某 provider 看似表現很好：

$$
Emp(P)
$$

會偏。

因此需要：

- anomaly detection；
- tenant isolation；
- robust aggregation；
- trusted evaluation benchmark。

---

# 147. Planner Feedback Attack

不能直接把：

```text
user clicked result
```

當：

```text
verified success
```

click 是 weak signal。

Evidence Ledger outcome 比 click 更強。

---

# 148. Outcome Hierarchy

可以定義：

$$
Strength(y)
$$

例如：

```text
click
< dwell time
< user approval
< evidence verified
< expert reviewed
< downstream outcome validated
```

不同 signals 權重不同。

---

# 149. Search Strategy Memory 的研究命題

## P7.1 — Receipt Learning Hypothesis

保存結構化 Search Receipt 應能使 future Planner 比 stateless Planner 更有效利用過去搜尋經驗。

## P7.2 — Outcome-Rich Learning Hypothesis

以 verified evidence、gap resolution、cost 與 stopping quality 等多維 outcome 訓練，應優於只用 final answer success。

## P7.3 — Episodic-to-Prototype Hypothesis

將多個相似 successful receipts 聚合成 Strategy Prototype，應降低 planning cost 並提高 plan validity。

## P7.4 — Failure-Memory Hypothesis

保存 typed failed search branches 應降低未來重複無效搜尋。

## P7.5 — Drift-Aware Weighting Hypothesis

依 provider / policy / model / schema version 與 recency 對 experience 加權，應提高跨時間 robustness。

## P7.6 — Bounded Policy Improvement Hypothesis

learned policy 若受 typed validator、policy gate、mandatory gap constraints 與 canary deployment 限制，應比直接 end-to-end self-modifying planner 更安全且可審計。

## P7.7 — Search-Experience Transfer Hypothesis

domain-general strategy primitives 應能跨 domain transfer，而 domain-specific operators 應由 Domain Pack 限定 transfer scope。

---

# 150. 工程落地

對 `ai-web-research`，可以新增：

```text
experience/
    receipt.py
    epoch.py
    store.py
    features.py
    outcomes.py
    retrieval.py
    aggregates.py
    prototypes.py
    failures.py
    drift.py
    attribution.py
    replay.py
    evaluation.py

learning/
    method_scorer.py
    provider_scorer.py
    gap_router.py
    stopping_model.py
    policy_model.py
    release.py
```

注意：

`policy_model.py` 在此指 Search Policy，而不是 Source Rights Policy。

名稱上實作時應避免混淆，最好改成：

```text
search_policy_model.py
```

---

# 151. 第一版不需要 Offline RL

MVP 可以先做：

```text
1. Search Receipt
2. Similar Episode Retrieval
3. Method/Provider Aggregates
4. Gap Resolution Statistics
5. Strategy Prototypes
6. Drift Warnings
```

就已能產生巨大價值。

---

# 152. MVP Learning Sequence

建議：

$$
L0
\rightarrow
L1
\rightarrow
L2
\rightarrow
L3
$$

其中：

- $L0$：Receipt；
- $L1$：statistics；
- $L2$：prototype；
- $L3$：learned policy。

不要一開始直接跳 end-to-end RL。

---

# 153. Canonical Learning Workflow

```text
Search Epoch
↓
Search Receipt Commit
↓
Outcome Evaluation
↓
Receipt Validation
↓
Experience Store
↓
Drift / Version Filtering
↓
Aggregate Statistics
↓
Strategy Prototype
↓
Offline Evaluation
↓
Planner Prior Update
↓
Validator + Policy Gate
↓
Future Search
```

---

# 154. 七篇核心系列的統一形式

Paper 01：

$$
\text{Search as AI-operable cognition}
$$

Paper 02：

$$
\mathcal{M}
=
\text{Search Method Space}
$$

Paper 03：

$$
\pi(T,S)\rightarrow a
$$

Paper 04：

$$
\mathcal{A}_{allowed}
\subseteq
\mathcal{A}_{technical}
$$

Paper 05：

$$
R\rightarrow E_v
$$

Paper 06：

$$
G\rightarrow\Pi_{\text{next}}
$$

Paper 07：

$$
H_{\text{search}}
\rightarrow
\pi_{\text{future}}
$$

合起來：

$$
\boxed{
\pi_{t+1}
=
F(
T,
S,
\mathcal{M},
\mathcal{P},
\mathcal{R}_{\text{policy}},
E,
G,
H_{\text{search}}
)
}
$$

---

# 155. AUSI 的完整資料流

$$
\boxed{
\text{Task}
\rightarrow
\text{Interpret}
\rightarrow
\text{Method Space}
\rightarrow
\text{Plan}
\rightarrow
\text{Policy Gate}
\rightarrow
\text{Acquire}
\rightarrow
\text{Verify}
\rightarrow
\text{Evidence Ledger}
\rightarrow
\text{Gap Detection}
\rightarrow
\text{Replan}
\rightarrow
\text{Stop}
\rightarrow
\text{Search Receipt}
\rightarrow
\text{Experience Memory}
\rightarrow
\text{Future Planner Improvement}
}
$$

這是七篇核心論文完成後的 canonical theoretical loop。

---

# 156. 最重要的邊界：自我改進不是自我越權

本文最後強調：

$$
\boxed{
\text{Self-Improving Search}
\neq
\text{Self-Authorizing Search}
}
$$

Search Strategy Memory 可以學：

- 哪個方法有效；
- 哪個 provider 快；
- 哪個 macro 成本低；
- 哪種 stopping 容易過早；
- 哪種 gap routing 更好。

但不能自己決定：

- 原本禁止的資料現在可以抓；
- `UNKNOWN` 可以改成 `ALLOW`；
- private data 可以送外部；
- mandatory verification 可以跳過；
- evidence 可以不需要 provenance。

這些不是 reward optimization 目標。

而是 system boundary。

---

# 157. 限制

第一，歷史 Search Receipt 是 observational data，不是完整 randomized experiment，因此 action effectiveness 容易受 selection bias 與 logging policy 影響。

第二，Search Outcome 的真實品質可能 delayed、partial 或永遠不可觀察，尤其是高階 research task。

第三，offline RL、bandit 與 counterfactual evaluation 的理論假設未必完全符合 open-world Search Agent，因此本文只把它們視為可選工具，不宣稱單一方法可解決全部學習問題。

第四，provider、Web、policy 與 model drift 會降低舊經驗有效性；Experience Validity Envelope 只能降低風險，不能完全消除 drift。

第五，Strategy Prototype 可能產生 historical lock-in，使新的搜尋方法難以被採用，因此仍需要 bounded exploration。

第六，Search Receipt 可能包含私人、商業與第三方資料，Experience Learning 必須遵守原資料與 log 自身的 rights / privacy constraints。

第七，Search Strategy Memory 可能遭受 poisoning、feedback manipulation 與 biased user interaction signals。

第八，learned planner 的高效不等於 epistemically superior；最終仍需 Evidence Ledger、Gap State 與 Domain Pack 的驗證。

第九，本文沒有提出一個完整可證明收斂的 universal search-learning algorithm；open-world heterogeneous search 很可能不存在單一全域最佳 policy。

---

# 158. 結論

七篇核心論文最後一篇的問題不是：

> AI 能不能再多搜一次？

而是：

> **AI 能不能從自己過去完成過的搜尋中，累積「如何搜尋」的可驗證經驗？**

本文提出：

$$
\boxed{
H_{\text{search}}
=
\{
(T_k,S_k,\Pi_k,\mathcal{R}_k,E_k,G_k,O_k)
\}_{k=1}^{N}
}
$$

並讓 future Planner 使用：

$$
\boxed{
\hat{\pi}
=
F(
T,
S,
H_{\text{search}}
)
}
$$

Search Receipt 因而不只是 audit log。

它同時是：

- reproducibility artifact；
- performance record；
- failure memory；
- empirical method profile；
- provider history；
- gap-resolution history；
- strategy-learning dataset。

但是 Learning Search Intelligence 的真正核心不是「模型自己改自己」。

而是建立一個層次分明的自我改進結構：

$$
\boxed{
\text{Raw Receipt}
\rightarrow
\text{Empirical Profile}
\rightarrow
\text{Strategy Prototype}
\rightarrow
\text{Learned Prior}
\rightarrow
\text{Validated Planner}
}
$$

並始終維持：

$$
\boxed{
\text{Learning Layer}
<
\text{Typed Semantics}
+
\text{Policy Gate}
+
\text{Evidence Invariants}
+
\text{Mandatory Domain Constraints}
}
$$

因此自我改進可以發生，而自我越權不能因 reward 變高而自動發生。

至此，AUSI 七篇核心論文形成完整理論：

$$
\boxed{
\text{Search}
\rightarrow
\text{Method}
\rightarrow
\text{Planning}
\rightarrow
\text{Authorized Acquisition}
\rightarrow
\text{Evidence}
\rightarrow
\text{Gap-Driven Research}
\rightarrow
\text{Learning Search Intelligence}
}
$$

這個系列最終研究的已經不再是一個搜尋引擎。

它研究的是：

> **如何將人類與計算機歷史上分散的搜尋能力，形式化為 AI 可以在明確權限、證據與風險邊界內選擇、組合、驗證、重規劃，並從實際搜尋經驗持續改善的認知基礎設施。**

核心論文到此完成。

下一階段不再繼續擴張核心理論，而應進入工程收斂：

1. **WP-01 — AI-Native Unified Search & Evidence Architecture**
2. **WP-02 — SearchMethodSpec / Registry / Planner / Provider Adapter Technical Specification**
3. **WP-03 — Trusted Data Acquisition & Evidence Runtime**
4. **WP-04 — Patent Intelligence & Autonomous Prior-Art Search Platform**

其中 WP-01 將第一次把 Paper 01–07 收斂為單一 canonical runtime architecture。

---

# References

[1] Joachims, T. (2002). *Optimizing Search Engines Using Clickthrough Data*. Proceedings of KDD 2002, 133–142.

[2] Burges, C., Shaked, T., Renshaw, E., Lazier, A., Deeds, M., Hamilton, N., & Hullender, G. (2005). *Learning to Rank Using Gradient Descent*. Proceedings of ICML 2005, 89–96.

[3] Liu, T.-Y. (2009). *Learning to Rank for Information Retrieval*. Foundations and Trends in Information Retrieval, 3(3), 225–331.

[4] Luo, J., Dong, X., & Yang, H. (2015). *Session Search by Direct Policy Learning*. Proceedings of ICTIR 2015, 261–270. DOI: 10.1145/2808194.2809461.

[5] Yang, G. H., Dong, X., Luo, J., & Zhang, S. (2018). *Session Search Modeling by Partially Observable Markov Decision Process*. Information Retrieval Journal, 21(1), 56–80.

[6] Li, L., Chu, W., Langford, J., & Schapire, R. E. (2010). *A Contextual-Bandit Approach to Personalized News Article Recommendation*. Proceedings of WWW 2010, 661–670.

[7] Dudík, M., Langford, J., & Li, L. (2011). *Doubly Robust Policy Evaluation and Learning*. Proceedings of ICML 2011, 1097–1104.

[8] Swaminathan, A., & Joachims, T. (2015). *Counterfactual Risk Minimization: Learning from Logged Bandit Feedback*. Proceedings of ICML 2015, 814–823.

[9] Swaminathan, A., & Joachims, T. (2015). *Batch Learning from Logged Bandit Feedback through Counterfactual Risk Minimization*. Journal of Machine Learning Research, 16, 1731–1755.

[10] Levine, S., Kumar, A., Tucker, G., & Fu, J. (2020). *Offline Reinforcement Learning: Tutorial, Review, and Perspectives on Open Problems*. arXiv:2005.01643.

[11] Kumar, A., Zhou, A., Tucker, G., & Levine, S. (2020). *Conservative Q-Learning for Offline Reinforcement Learning*. Advances in Neural Information Processing Systems 33.

[12] Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction*, 2nd ed. MIT Press.

[13] Lin, L.-J. (1992). *Self-Improving Reactive Agents Based on Reinforcement Learning, Planning and Teaching*. Machine Learning, 8, 293–321.

[14] Gama, J., Žliobaitė, I., Bifet, A., Pechenizkiy, M., & Bouchachia, A. (2014). *A Survey on Concept Drift Adaptation*. ACM Computing Surveys, 46(4), Article 44.

[15] Parisi, G. I., Kemker, R., Part, J. L., Kanan, C., & Wermter, S. (2019). *Continual Lifelong Learning with Neural Networks: A Review*. Neural Networks, 113, 54–71.

[16] Bottou, L., Peters, J., Quiñonero-Candela, J., et al. (2013). *Counterfactual Reasoning and Learning Systems: The Example of Computational Advertising*. Journal of Machine Learning Research, 14, 3207–3260.

[17] Chapelle, O., & Li, L. (2011). *An Empirical Evaluation of Thompson Sampling*. Advances in Neural Information Processing Systems 24.

[18] Moreau, L., Missier, P., et al. (2013). *PROV-DM: The PROV Data Model*. W3C Recommendation.

[19] Rethlefsen, M. L., Kirtley, S., Waffenschmidt, S., et al. (2021). *PRISMA-S: an Extension to the PRISMA Statement for Reporting Literature Searches in Systematic Reviews*. Systematic Reviews, 10, 39.

[20] Singh, A., Ehtesham, A., Kumar, S., Khoei, T. T., & Vasilakos, A. V. (2025/2026). *Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG*. arXiv:2501.09136.

---

# Core Series Closure

**AUSI Core Papers 01–07：COMPLETED**

後續正式進入：

**Technical Whitepaper 01 — AI-Native Unified Search & Evidence Architecture v0.1**

此白皮書將以七篇核心論文為 canonical theoretical input，把：

$$
\text{Method Registry}
+
\text{Planner}
+
\text{Provider Layer}
+
\text{Policy Registry}
+
\text{Evidence Runtime}
+
\text{Gap Engine}
+
\text{Experience Memory}
$$

收斂為可實作的 runtime architecture、module boundary、state contract、API surface、data model 與 phased migration plan。
