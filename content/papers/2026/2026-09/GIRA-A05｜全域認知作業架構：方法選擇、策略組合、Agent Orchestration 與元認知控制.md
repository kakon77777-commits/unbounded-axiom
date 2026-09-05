# GIRA-A05｜全域認知作業架構：方法選擇、策略組合、Agent Orchestration 與元認知控制
## Global Cognitive Operating Architecture: Method Selection, Strategy Composition, Agent Orchestration, and Metacognitive Control

**系列：** Global Intelligence: Existence, Recognition, and Operational Reach（GIRA）  
**系列中文名：** 全域智能：存在、識別與操作域系列  
**篇次：** Paper 05 / 09  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-05  
**狀態：** Canonical Source / UTF-8 Markdown  
**文件性質：** Global AI 認知架構／策略編譯／Agent Runtime／元認知控制

---

## 摘要

GIRA-A01 至 A04 已依序處理四個 Global AI 前置條件：ASI 不等於 Global AI；真正全域認知需要多觀察者、多方法與多表示的 Global Cognitive Atlas；資訊海必須透過多層結構化轉換成可追溯世界狀態；而世界狀態變化又必須進一步轉換成動態關鍵性與有限注意力配置。到此形成：

$$
\boxed{
\Delta D_t
\rightarrow
\Delta W_t
\rightarrow
\Delta K_t
\rightarrow
\Delta a_t.
}
$$

然而，即使 AI 已經把注意力放到正確位置，仍然沒有回答更高階問題：

> **現在應該怎麼想？**

對同一問題，AI 可以選擇搜尋、統計、圖分析、因果推論、博弈分析、模擬、程式執行、形式證明、反例搜尋、多 Agent 辯證、專家查核、人類升級，甚至暫停推理。

因此本文提出：

$$
\boxed{
\text{Intelligence}
\neq
\text{Method Availability}
\neq
\text{Method Selection}
\neq
\text{Method Orchestration}.
}
$$

一個系統知道很多方法，不表示它知道當前應用哪一種；可以調用很多 Agent，也不表示每題都應調用全部 Agent；擁有更多 test-time compute，也不表示每一單位算力都應繼續投入同一條推理路徑。

本文將這一層稱為 **Global Cognitive Operating Architecture（GCOA，全域認知作業架構）**，定義：

$$
\boxed{
\mathfrak C_G
=
(
W,
A,
Q,
\mathcal R,
\mathcal M,
\mathcal G,
\mathcal T,
\mathcal V,
\mathcal B,
\Pi,
\mathcal L
).
}
$$

其中：

- $W$：world state；
- $A$：attention state；
- $Q$：task / question state；
- $\mathcal R$：representation / chart set；
- $\mathcal M$：method / cognitive primitive library；
- $\mathcal G$：Agent / specialist role set；
- $\mathcal T$：tool and execution substrate；
- $\mathcal V$：verifiers and evidence gates；
- $\mathcal B$：budget / authority / risk envelope；
- $\Pi$：strategy compiler and metacognitive policy；
- $\mathcal L$：strategy receipts, learning, and policy history。

本文將一次認知策略表示為：

$$
\boxed{
\sigma_t
=
(
r_t,
m_t,
g_t,
\tau_t,
v_t,
b_t,
s_t,
f_t,
\rho_t
),
}
$$

其中 $r_t$ 是表示， $m_t$ 是方法， $g_t$ 是 Agent / role， $\tau_t$ 是工具與執行程序， $v_t$ 是驗證器， $b_t$ 是預算， $s_t$ 是停止條件， $f_t$ 是 fallback / replan， $\rho_t$ 是 provenance / receipt。

GCOA 不直接等於模型 chain-of-thought，也不要求所有認知步驟由自然語言完成。它更接近一個持久、可審計的 semantic control plane：高階控制層決定「現在需要哪種認知操作」，低階執行層則由 LLM、搜尋器、程式、CAS、定理證明器、模擬器、資料庫與確定性演算法完成。

本文承接既有 CDI 的：

$$
\boxed{
\text{Execution Plane}
\neq
\text{Semantic Control Plane},
}
$$

並提升為：

$$
\boxed{
\text{Cognitive Execution Plane}
\neq
\text{Cognitive Strategy Plane}.
}
$$

本文亦承接 DDRA 對「Should I think more?」與「What should I think about next?」的分離，以 residual doubt vector：

$$
D_t
=
(
D_F,
D_S,
D_B,
D_R,
D_V,
\ldots
)
$$

描述尚未閉合的認知風險，並以 Value of Information、expected doubt reduction、task progress、cost、risk 與 authority 共同決定下一個 strategy action。

本文提出概念量：

$$
\boxed{
\operatorname{EEU}(\sigma_i\mid S_t)
=
\frac{
\mathbb E[
\Delta U_{\mathrm{epistemic}}
+
\Delta U_{\mathrm{task}}
-
\lambda R
]
}{
C(\sigma_i)
}
}
$$

作為 Expected Epistemic Utility。本文不宣稱此式為普適效用函數，而將其用作「下一單位認知資源應投入何處」的工程化接口。

本文進一步區分：

$$
\boxed{
\text{Strategy Proposal}
\neq
\text{Active Strategy}
\neq
\text{Knowledge Commit}.
}
$$

模型可以提出新方法、新角色、新工具組合，但策略 adoption 必須經過 capability gate、authority gate、risk gate、shadow evaluation 與 verifier gate。這承接 Memory Strategy Governor 的：

$$
\boxed{
\text{Route Decision}
\neq
\text{Knowledge Decision}
}
$$

與：

$$
\boxed{
\text{Empirical Preference}
\neq
\text{Canonical Policy}.
}
$$

最後，本文提出 **Global Cognitive Control Loop**：

$$
\boxed{
\text{Frame}
\rightarrow
\text{Select Representation}
\rightarrow
\text{Estimate Residual Doubt}
\rightarrow
\text{Generate Strategy Candidates}
\rightarrow
\text{Route Resources}
\rightarrow
\text{Execute}
\rightarrow
\text{Verify}
\rightarrow
\text{Stop / Replan / Reframe}
\rightarrow
\text{Update World State}.
}
$$

這個架構使 Global AI 不再只被理解為「更會回答問題」，而是能持續決定：什麼問題值得算、應該用什麼表示、下一步該叫誰、應使用什麼工具、什麼時候不應再想、什麼時候應換方法，以及何時目前的方法論本身已經成為 bottleneck。

**關鍵詞：** Global AI、Metacognition、Strategy Selection、Agent Orchestration、Cognitive Runtime、Method Selection、Adaptive Routing、Value of Information、MSSP、DDRA、Semantic Control Plane、Strategy Compiler、GCOA

---

# 1. 注意力到了正確位置之後呢？

A04 回答：

$$
\boxed{
\text{Where should cognition be allocated?}
}
$$

但 attention 只回答「去哪裡」。

它沒有回答：

$$
\boxed{
\text{What should cognition do there?}
}
$$

如果沒有 strategy layer：

$$
\boxed{
\text{correct attention}
\not\Rightarrow
\text{correct cognition}.
}
$$

---

# 2. 方法很多，不等於方法選對

令方法庫：

$$
\mathcal M
=
\{m_1,m_2,\ldots,m_n\}.
$$

若 AI 知道所有 $m_i$，仍不代表最合適的：

$$
m_t^\ast
$$

會自然出現。

因此：

$$
\boxed{
\text{Method Knowledge}
\neq
\text{Method Selection}.
}
$$

---

# 3. 多 Agent 也不等於 Orchestration

令 Agent 集合：

$$
\mathcal G
=
\{g_1,g_2,\ldots,g_k\}.
$$

全部呼叫並不一定比只呼叫一個適合的 specialist 更好，因為會產生 duplicated work、consensus echo、coordination overhead 與 state contamination。

所以：

$$
\boxed{
\text{Multi-Agent Architecture}
\neq
\text{Adaptive Agent Allocation}.
}
$$

---

# 4. 更多推理時間也不等於更好

test-time compute 可以提升結果，但不同問題具有不同難度與可解性。

因此：

$$
\boxed{
\text{More Compute}
\not\Rightarrow
\text{More Value}.
}
$$

真正問題是：

$$
\boxed{
\text{where the next unit of compute should go}.
}
$$

---

# 5. 認知數量配置只是子問題

傳統 adaptive compute 可寫：

$$
x
\rightarrow
b(x).
$$

本文擴張 action space：

$$
a_t
\in
\{
\operatorname{Stop},
\operatorname{Reframe},
m_1,\ldots,m_n,
g_1,\ldots,g_k,
\tau_1,\ldots,\tau_j
\}.
$$

因此：

$$
\boxed{
\text{Compute Quantity Allocation}
\subset
\text{Cognitive Strategy Allocation}.
}
$$

---

# 6. GCOA 的總狀態

定義：

$$
\boxed{
\mathfrak C_G
=
(
W,
A,
Q,
\mathcal R,
\mathcal M,
\mathcal G,
\mathcal T,
\mathcal V,
\mathcal B,
\Pi,
\mathcal L
).
}
$$

這是一個操作性架構類，不是一個固定產品。

---

# 7. World State $W$

承接 A03， $W_t$ 包含 current state、history、provenance、uncertainty、conflict 與 unknown。

策略不能只看 prompt。

它需要看：

$$
\boxed{
\text{task in world state}.
}
$$

---

# 8. Attention State $A$

承接 A04：

$$
A_t
=
\mathcal A_t(\mathcal X_t).
$$

它表示哪些 world objects 目前取得多少 active cognitive resource。

---

# 9. Task State $Q$

任務不是單一字串。

可以表示：

$$
Q_t
=
(
\text{goal},
\text{scope},
\text{constraints},
\text{success},
\text{deadline},
\text{risk},
\text{authority}
).
$$

因此：

$$
\boxed{
\text{Prompt}
\neq
\text{Task State}.
}
$$

---

# 10. Representation Set $\mathcal R$

承接 A02：

$$
\mathcal R
=
\{r_1,r_2,\ldots,r_p\}.
$$

可以包含 natural language、graph、matrix、symbolic form、code、proof state、causal model 與 simulation state。

策略選擇必須包含：

$$
\boxed{
\text{representation selection}.
}
$$

---

# 11. Method Library $\mathcal M$

方法可以是 search、statistics、optimization、graph theory、causal inference、game theory、theorem proving、numerical experiment、counterexample search、decomposition、backtrace 與 simulation。

因此：

$$
\boxed{
\text{Method}
\neq
\text{Tool}.
}
$$

---

# 12. Specialist Set $\mathcal G$

specialist 是 functional role。

同一 foundation model 可以透過不同 prompt、context、objective、tool access 與 verifier 扮演不同 $g_i$。

因此：

$$
\boxed{
\text{Specialist Identity}
\neq
\text{Model Identity}.
}
$$

---

# 13. Tool Substrate $\mathcal T$

工具包括 web search、database、code runtime、CAS、Lean / Coq、simulator、compiler、browser、sensor 與 external API。

工具主要回答：

> 可以執行什麼？

不是：

> 現在應該執行什麼？

---

# 14. Verifier Set $\mathcal V$

Verifier 可以包括 source check、unit test、formal proof、independent model、consistency checker、human review 與 simulation validation。

所以：

$$
\boxed{
\text{Generator}
\neq
\text{Verifier}.
}
$$

---

# 15. Budget / Authority / Risk Envelope $\mathcal B$

定義：

$$
\mathcal B_t
=
(
B_{\mathrm{compute}},
B_{\mathrm{time}},
B_{\mathrm{cost}},
B_{\mathrm{authority}},
B_{\mathrm{privacy}},
B_{\mathrm{risk}}
).
$$

某策略即使理論上最強，也可能：

$$
\sigma
\notin
\operatorname{Feasible}(\mathcal B_t).
$$

---

# 16. Strategy Compiler $\Pi$

核心函數：

$$
\boxed{
\Pi:
(
W_t,
A_t,
Q_t,
\mathcal R,
\mathcal M,
\mathcal G,
\mathcal T,
\mathcal V,
\mathcal B_t
)
\rightarrow
\Sigma_t.
}
$$

其中：

$$
\Sigma_t
=
\{\sigma_1,\sigma_2,\ldots,\sigma_n\}
$$

是候選策略集合。

---

# 17. Cognitive Strategy Object

本文定義：

$$
\boxed{
\sigma_t
=
(
r_t,
m_t,
g_t,
\tau_t,
v_t,
b_t,
s_t,
f_t,
\rho_t
).
}
$$

它把 representation、method、specialist、tool、verifier、budget、stop、fallback 與 receipt 綁成可執行物件。

---

# 18. Strategy 不是固定 Workflow

固定 workflow：

$$
\mathcal F_{\mathrm{fixed}}
$$

只是 strategy 的一種退化。

高階系統應允許：

$$
\boxed{
\sigma_t
\neq
\sigma_{t+1}
}
$$

在必要時成立。

---

# 19. Representation First

很多推理失敗不是推理不夠深，而是表示錯了。

因此方法選擇前應問：

$$
\boxed{
\text{Is the current representation still appropriate?}
}
$$

若：

$$
q_t
\rightarrow
\partial U_r,
$$

應允許：

$$
r_i
\rightarrow
r_j.
$$

---

# 20. Reframe 是合法 Strategy Action

策略 action space 應包含：

$$
\boxed{
\operatorname{Reframe}.
}
$$

也就是改寫 problem statement、variables、decomposition、representation、target 或 scope。

---

# 21. MSSP：從少看一點到有秩序地看更多

MSSP 的 AI 版本提出：

$$
\boxed{
\text{Avoid Global Attention}
\rightarrow
\text{Construct Global Understanding by Traversal}.
}
$$

GCOA 採用同樣原則。

---

# 22. Structured Traversal

令整體結構圖：

$$
G=(V,E).
$$

當前 subset：

$$
G_t\subseteq G.
$$

選擇：

$$
G_t
=
\operatorname{Select}(
q,
G,
M_{t-1},
A,
R
).
$$

局部推理後：

$$
M_t
=
\operatorname{Update}(
M_{t-1},
\operatorname{Reason}(G_t)
).
$$

---

# 23. Traversal 不等於 Retrieval

Retrieval 常回答哪些內容最像 query。

Traversal 還回答下一個 dependency、未驗證 parent、authority boundary 與 revisit order。

因此：

$$
\boxed{
\text{Retrieval}
\subset
\text{Structural Traversal}.
}
$$

---

# 24. 中間狀態必須外部化

如果每次策略切換都丟失中間結果，就會重複計算。

因此：

$$
\boxed{
\text{Reason}
\rightarrow
\text{Record}
\rightarrow
\text{Route}.
}
$$

中間狀態應是 typed object，而不只是聊天 transcript。

---

# 25. Residual Doubt Vector

承接 DDRA：

$$
\boxed{
D_t
=
(
D_F,
D_S,
D_B,
D_P,
D_R,
D_V,
D_C,
\ldots
).
}
$$

它可以表示 formal、source、bridge、representation、verification 與 closure doubt。

---

# 26. Doubt 是 Operational Risk

這裡的 doubt 不是情緒，而是：

$$
\boxed{
\text{operational unresolved risk}.
}
$$

它表示某個 load-bearing 問題仍未閉合。

---

# 27. Doubt Value Function

最簡單：

$$
V(D_t)
=
\sum_j
\lambda_jD_j.
$$

更一般：

$$
V:
\mathbb R_{\geq0}^m
\rightarrow
\mathbb R_{\geq0}.
$$

---

# 28. Specialist Expected Effect

對 specialist $g_i$：

$$
R_i(D_t)
=
\mathbb E[
D_t-D_{t+1}
\mid
g_i,S_t
].
$$

這是一個向量。

---

# 29. Expected Epistemic Utility

本文提出：

$$
\boxed{
\operatorname{EEU}(\sigma_i\mid S_t)
=
\frac{
\mathbb E[
\Delta U_{\mathrm{epistemic}}
+
\Delta U_{\mathrm{task}}
-
\lambda R
]
}{
C(\sigma_i)
}.
}
$$

它是 routing interface，不是普適真理分數。

---

# 30. Strategy Candidate Generation

候選可以包含：

$$
\Sigma_t
=
\{
\sigma_{\mathrm{search}},
\sigma_{\mathrm{formal}},
\sigma_{\mathrm{simulate}},
\sigma_{\mathrm{counterexample}},
\sigma_{\mathrm{delegate}},
\sigma_{\mathrm{stop}},
\sigma_{\mathrm{reframe}}
\}.
$$

候選生成與候選選擇應分離。

---

# 31. Hard Gate 先於 Utility

如果策略違反 authority、privacy、safety、exactness requirement 或 evidence floor，即使 EEU 很高也不可執行。

因此：

$$
\boxed{
\text{Eligibility}
\prec
\text{Utility Ranking}.
}
$$

---

# 32. Cognitive Need 不等於 Method Command

Memory Strategy Governor 已提出：

$$
\text{Memory Need}
\neq
\text{Search Command}.
$$

GCOA 一般化成：

$$
\boxed{
\text{Cognitive Need}
\neq
\text{Method Command}.
}
$$

使用者不必先知道該用什麼方法。

---

# 33. Route Decision 不是 Knowledge Decision

策略層可以說：

> 下一步使用 formal verifier。

但不能因此說：

> verifier 還沒執行，命題已被證成。

所以：

$$
\boxed{
\text{Route Decision}
\neq
\text{Knowledge Decision}.
}
$$

---

# 34. Capability 不等於 Authority

一個 specialist 即使能力很強，也不能自動取得 source authority、write authority、action authority 或 policy authority。

因此：

$$
\boxed{
\text{Capability}
\neq
\text{Authority}.
}
$$

---

# 35. Strategy Proposal 不等於 Active Strategy

模型可以提出：

$$
\sigma_{\mathrm{new}}.
$$

但流程應為：

$$
\boxed{
\text{Proposal}
\rightarrow
\text{Gate}
\rightarrow
\text{Shadow}
\rightarrow
\text{Evaluate}
\rightarrow
\text{Adopt}.
}
$$

---

# 36. Empirical Preference 不等於 Canonical Policy

即使：

$$
\operatorname{Perf}(\sigma_{\mathrm{new}})
>
\operatorname{Perf}(\sigma_{\mathrm{old}}),
$$

也不應直接修改 global policy。

因此：

$$
\boxed{
\text{Benchmark Improvement}
\neq
\text{Policy Adoption}.
}
$$

---

# 37. Cognitive Strategy Policy

定義：

$$
P_\sigma
=
(
\text{eligibility},
\text{preference},
\text{fallback},
\text{stop},
\text{risk},
\text{verification},
\text{budget}
).
$$

每個 policy 必須 versioned。

---

# 38. Deterministic Baseline

對相同 state、policy、capabilities 與 budget，第一版系統應能產生可重播 plan。

因此：

$$
\boxed{
\text{same input state}
\rightarrow
\text{same strategy digest}.
}
$$

---

# 39. Adaptive 不等於不可審計

AI 可以自適應，但每次：

$$
\sigma_t
\rightarrow
\sigma_{t+1}
$$

都應有 reason code。

所以：

$$
\boxed{
\text{Adaptive}
\neq
\text{Opaque}.
}
$$

---

# 40. Strategy Receipt

每次 strategy decision 至少保存：

```yaml
strategy_receipt:
  task_id: "..."
  state_version: "..."
  representation: "..."
  method: "..."
  specialist: "..."
  tools: ["..."]
  verifier: "..."
  budget: "..."
  residual_doubt_before: "..."
  expected_utility: "..."
  stop_condition: "..."
  fallback: "..."
  policy_version: "..."
  reason_codes: ["..."]
```

---

# 41. Cognitive Execution Plane

執行平面負責：

$$
\boxed{
\text{Execute the selected cognitive operation}.
}
$$

它可以由 LLM、traditional algorithm、code、prover 或 simulator 完成。

---

# 42. Cognitive Strategy Plane

策略平面負責：

$$
\boxed{
\text{Choose and govern the operation}.
}
$$

因此：

$$
\boxed{
\text{Cognitive Execution Plane}
\neq
\text{Cognitive Strategy Plane}.
}
$$

---

# 43. 承接 CDI Semantic Control Plane

CDI 已提出：

$$
\boxed{
\text{Execution Plane}
\neq
\text{Semantic Control Plane}.
}
$$

GCOA 把這個思想從計算 routing 提升到 cognition routing。

---

# 44. AI 不需要親自算全部

若 traditional tool $\tau_j$ 更快、更便宜、更可靠，AI 應路由給它。

例如：

$$
\text{LLM}
\rightarrow
\text{CAS}.
$$

所以：

$$
\boxed{
\text{AI-native cognition}
\neq
\text{LLM computes everything}.
}
$$

---

# 45. AI 作為 Semantic Governor

高階 AI 的角色可以是 interpret、route、compose、verify、reframe 與 stop，而不必成為每個低階 kernel。

---

# 46. Orchestration Topology

多 Agent orchestration 可以是 centralized、decentralized 或 hierarchical。

本文不預設唯一拓樸。

---

# 47. Topology 也是 Strategy Variable

簡單任務可能 single-agent 最優；可分解任務可能 hierarchical 較好；多利益主體則可能更適合 decentralized。

因此：

$$
\boxed{
\text{Orchestration Topology}
=
\text{Strategy Variable}.
}
$$

---

# 48. Dynamic Role Allocation

固定角色集合：

$$
\mathcal G_0
$$

可能不足。

高階系統可以：

$$
\mathcal G_t
\rightarrow
\mathcal G_{t+1}
$$

動態生成 specialist role。

---

# 49. Role Synthesis 不等於 Model Creation

新 role 可由現有模型透過不同 objective、context、tool 與 verifier 構成。

因此：

$$
\boxed{
\text{Role Synthesis}
\neq
\text{New Model Training}.
}
$$

---

# 50. 新 Specialist 的觸發條件

若某 residual doubt $D_j$ 高，但現有 specialists 對它的預期 reduction 都低，可觸發：

$$
\operatorname{SynthesizeSpecialist}(D_j).
$$

---

# 51. 新 Specialist 先進 Sandbox

流程：

$$
\boxed{
\text{Synthesize}
\rightarrow
\text{Sandbox}
\rightarrow
\text{Benchmark}
\rightarrow
\text{Register}
\rightarrow
\text{Route}.
}
$$

---

# 52. Strategy Composition

方法可以序列組合：

$$
m_1
\rightarrow
m_2
\rightarrow
m_3,
$$

也可平行：

$$
m_1
\parallel
m_2,
$$

再由 verifier 做 reconciliation。

---

# 53. Strategy Shape

常見 shape 可包括：

- SINGLE；
- SEQUENTIAL；
- PARALLEL_DISCOVERY；
- DISCOVERY_THEN_VERIFY；
- STRUCTURE_THEN_EXECUTE；
- COUNTEREXAMPLE_THEN_PROVE；
- SIMULATE_THEN_FORMALIZE；
- MULTI_AGENT_CORROBORATIVE；
- FREEZE；
- REFRAME。

---

# 54. Always-Hybrid 不是合理預設

每題都搜尋、三 Agent、verifier、simulator 會浪費大量資源。

因此：

$$
\boxed{
\text{Hybrid Capability}
\neq
\text{Always-Hybrid Policy}.
}
$$

---

# 55. Stop 是一等 Action

Global AI 不只要知道 how to think，還要知道：

$$
\boxed{
\text{when not to think more}.
}
$$

---

# 56. Freeze Controller

若：

$$
V(D_t)
<
\tau_D
$$

且：

$$
\max_i
\operatorname{EEU}(\sigma_i\mid S_t)
<
\tau_E,
$$

則：

$$
\boxed{
\operatorname{Freeze}.
}
$$

---

# 57. Freeze 不等於永久真理

Freeze 只表示：在目前 task identity、evidence、budget 與 risk 下停止認知擴張。

之後可以被：

$$
\Delta W_t
$$

重新喚醒。

---

# 58. Stop Condition 必須進 Strategy

每個 $\sigma_t$ 都應帶 $s_t$。

否則 Agent 容易陷入 infinite search、infinite critique、infinite planning 或 endless verification。

---

# 59. Fallback 必須預先存在

如果：

$$
\sigma_1
$$

失敗，策略應知道：

$$
f(\sigma_1)
=
\sigma_2.
$$

---

# 60. Failure Taxonomy

至少區分：

- zero result；
- insufficient evidence；
- timeout；
- tool unavailable；
- verifier disagreement；
- representation mismatch；
- budget exhausted；
- authority denied；
- policy conflict。

不同 failure 對應不同 fallback。

---

# 61. Retry、Replan、Reframe

Retry：

$$
\sigma
\rightarrow
\sigma.
$$

Replan：

$$
\sigma_i
\rightarrow
\sigma_j.
$$

Reframe 則改變問題表示。

因此：

$$
\boxed{
\text{Retry}
<
\text{Replan}
<
\text{Reframe}.
}
$$

---

# 62. Architecture Backtrace 作為 Reframe Primitive

ABFR 提出 declared、observed、effective structure 回溯與 fresh reconstruction。

對 GCOA，長時間卡住時可以：

$$
\boxed{
\text{Backtrace}
\rightarrow
\text{Reconstruct Problem Architecture}.
}
$$

---

# 63. 局部成功不等於架構正確

一個策略可以：

$$
\text{Result}=\text{Pass}
$$

但 task framing 仍可能錯。

因此高風險任務可加入 architecture-level revalidation。

---

# 64. Operational Metacognition 的三層

本文拆成：

$$
\boxed{
\text{Self-Assessment}
+
\text{Strategy Selection}
+
\text{Self-Regulation}.
}
$$

---

# 65. Competence Awareness

對策略 $\sigma_i$，系統需要估計：

$$
P(
\operatorname{Success}
\mid
\sigma_i,S_t
).
$$

如果不知道自己不擅長什麼，routing 會失真。

---

# 66. Calibration

若估計：

$$
p_i=0.9
$$

但實際成功率只有 $0.5$，就需要更新 competence model。

所以：

$$
\boxed{
\text{Metacognition requires calibration}.
}
$$

---

# 67. Strategy Learning

策略歷史 $\mathcal L_t$ 可以記錄 chosen strategy、cost、result、doubt reduction、failure 與 verifier outcome。

由此學習：

$$
\Pi_{t+1}.
$$

---

# 68. Learning 不應直接改 Production Policy

承接 MSG：

$$
\boxed{
\text{Performance Observation}
\neq
\text{Policy Mutation}.
}
$$

應先經：

$$
\text{Observation}
\rightarrow
\text{Proposal}
\rightarrow
\text{Shadow}
\rightarrow
\text{Adoption}.
$$

---

# 69. Strategy Drift

world state 改變時，過去最好策略可能失效。

因此：

$$
\Pi_t
\neq
\Pi_{t+1}
$$

可能成立，需要 policy version。

---

# 70. Method Discovery Mode

若現有方法長期無法降低某 residual doubt，可進入：

$$
\boxed{
\text{Method Discovery Mode}.
}
$$

---

# 71. 新方法必須有 Contract

候選：

$$
m_{\mathrm{new}}
$$

至少需要 input contract、output contract、validity domain、transformation rule、known failure、verifier 與 benchmark。

---

# 72. Method Synthesis

可以由既有方法組合：

$$
m_{\mathrm{new}}
=
\Gamma(
m_i,
m_j,
r_k
).
$$

---

# 73. Method Adoption Gate

流程：

$$
\boxed{
\text{Invent}
\rightarrow
\text{Specify}
\rightarrow
\text{Test}
\rightarrow
\text{Compare}
\rightarrow
\text{Adopt}.
}
$$

---

# 74. Method Contract

每個方法至少保存：

```yaml
method_contract:
  method_id: "..."
  version: "..."
  valid_domains: ["..."]
  input_types: ["..."]
  output_types: ["..."]
  required_tools: ["..."]
  verifier_types: ["..."]
  expected_cost: "..."
  known_failure_modes: ["..."]
  authority_ceiling: "..."
```

---

# 75. Method Availability 不等於 Internalization

如果模型知道某方法文字描述：

$$
\operatorname{KnowText}(m)=1,
$$

不代表：

$$
\operatorname{Operationalize}(m)=1.
$$

因此：

$$
\boxed{
\text{Theory Access}
\neq
\text{Operational Method}.
}
$$

---

# 76. Method Internalization 的最低判準

至少要能：

1. 判定適用域；
2. 生成合法輸入；
3. 執行方法；
4. 理解失敗；
5. 驗證輸出；
6. 與其他方法組合；
7. 知道何時不用它。

---

# 77. Strategy Graph

一次複雜認知可表示成：

$$
\boxed{
G_\sigma
=
(V_\sigma,E_\sigma).
}
$$

節點是 cognitive operation，邊是 dependency、data flow 或 authority relation。

---

# 78. Strategy Graph 可以動態改寫

新 evidence 到來時：

$$
G_{\sigma,t}
\rightarrow
G_{\sigma,t+1}.
$$

因此：

$$
\boxed{
\text{Plan}
\neq
\text{Immutable Script}.
}
$$

---

# 79. Plan Drift 需要 Receipt

每次 graph mutation 保存：

$$
\Delta G_{\sigma,t}.
$$

並記錄 why changed。

---

# 80. Global Cognitive Control Loop

本文正式提出：

$$
\boxed{
\text{Frame}
\rightarrow
\text{Select Representation}
\rightarrow
\text{Estimate Residual Doubt}
\rightarrow
\text{Generate Strategy Candidates}
\rightarrow
\text{Route Resources}
\rightarrow
\text{Execute}
\rightarrow
\text{Verify}
\rightarrow
\text{Stop / Replan / Reframe}
\rightarrow
\text{Update World State}.
}
$$

---

# 81. 控制平面也會失敗

高階 controller 可能選錯 representation、over-decompose、under-decompose、call too many agents、stop too early、never stop、misuse verifier 或 policy-stale。

所以 GCOA 自身也需要評測。

---

# 82. Strategy Selection Regret

可定義：

$$
\boxed{
R_\sigma(T)
=
\sum_{t=1}^{T}
[
U(\sigma_t^\ast)
-
U(\sigma_t)
].
}
$$

其中 $\sigma_t^\ast$ 是事後參考最優策略，同樣需要避免 hindsight bias。

---

# 83. Routing Efficiency

定義：

$$
\boxed{
\eta_R
=
\frac{
\text{verified task progress}
}{
\text{cognitive resource cost}
}.
}
$$

高風險任務不應單獨最大化 $\eta_R$，因為可能需要冗餘驗證。

---

# 84. Method Switching Cost

換方法存在：

$$
C_{\mathrm{switch}}(
m_i
\rightarrow
m_j
).
$$

包含 state conversion、context loading、representation translation 與 verifier setup。

---

# 85. Strategy Hysteresis

若：

$$
\operatorname{EEU}_j-\operatorname{EEU}_i
<
\tau_{\mathrm{switch}},
$$

可保持現策略，避免 strategy thrashing。

---

# 86. Emergency Reframe

若出現 contradiction、invalid authority、source identity collapse 或 catastrophic verifier failure，可觸發：

$$
\boxed{
\operatorname{EmergencyReframe}.
}
$$

---

# 87. Multi-Agent Agreement 不等於 Evidence

若多個 Agent 共享同一來源或高度相同 reasoning pattern：

$$
\boxed{
\text{Agreement}
\neq
\text{Independent Corroboration}.
}
$$

---

# 88. Agent Diversity 不是越多越好

真正有價值的是：

$$
\boxed{
\text{effective cognitive diversity}.
}
$$

不是 agent count。

---

# 89. Human as Specialist

人類可以是：

$$
g_H
\in
\mathcal G.
$$

當 authority required、tacit knowledge needed、high-stakes ambiguity 或制度判斷出現時，路由到 human 是合法 strategy。

---

# 90. Global AI 不要求 Unbounded Autonomy

Global AI 可以高度自主，但：

$$
\boxed{
\text{Global Cognition}
\neq
\text{Unbounded Autonomous Action}.
}
$$

Strategy Plane 與 Action Authority 必須分離。

---

# 91. Meta-Methodological Cognition

當系統能選方法、換方法、組方法、生成 specialist、提出 method candidate、驗證 method 並更新 policy，就開始進入：

$$
\boxed{
\text{meta-methodological cognition}.
}
$$

---

# 92. 這才是「知道怎麼使用自己的智能」

一個高能力模型：

$$
I\gg0
$$

若缺乏：

$$
\Pi,
$$

仍可能很會解被指定的題，卻不擅長決定下一步應使用自己的哪種能力。

所以：

$$
\boxed{
\text{Intelligence}
+
\text{Metacognitive Strategy Control}
}
$$

在長時複雜任務上可能遠強於單純提高 $I$。

---

# 93. 與 A01 的核心修正

A01 提出：

$$
\text{ASI}
\neq
\text{Global AI}.
$$

A05 補上中間層：

$$
\boxed{
\text{High Intelligence}
\rightarrow
\text{Metacognitive Strategy Control}
\rightarrow
\text{Operational Global Intelligence}.
}
$$

但第一個箭頭不是邏輯必然。

---

# 94. 與 A04 的整合

A04：

$$
\Delta W_t
\rightarrow
\Delta K_t
\rightarrow
\Delta a_t.
$$

A05：

$$
\Delta a_t
\rightarrow
\Delta\sigma_t.
$$

因此：

$$
\boxed{
\Delta D_t
\rightarrow
\Delta W_t
\rightarrow
\Delta K_t
\rightarrow
\Delta a_t
\rightarrow
\Delta\sigma_t.
}
$$

---

# 95. Strategy 反過來改變 Observation

不同 $\sigma_t$ 會調用不同工具與觀察方法。

因此：

$$
\sigma_t
\rightarrow
D_{t+1},
$$

又回到 A03。

形成：

$$
\boxed{
W
\rightarrow
A
\rightarrow
\sigma
\rightarrow
\text{Observe / Act}
\rightarrow
W'.
}
$$

---

# 96. GCOA 的核心不變量

$$
\boxed{
\text{Attention}
\neq
\text{Method}
}
$$

$$
\boxed{
\text{Method}
\neq
\text{Tool}
}
$$

$$
\boxed{
\text{Specialist}
\neq
\text{Model}
}
$$

$$
\boxed{
\text{Route}
\neq
\text{Truth}
}
$$

$$
\boxed{
\text{Capability}
\neq
\text{Authority}
}
$$

$$
\boxed{
\text{More Compute}
\neq
\text{More Value}
}
$$

$$
\boxed{
\text{Retry}
\neq
\text{Replan}
\neq
\text{Reframe}
}
$$

$$
\boxed{
\text{Adaptive}
\neq
\text{Opaque}
}
$$

$$
\boxed{
\text{Strategy Proposal}
\neq
\text{Policy Adoption}.
}
$$

---

# 97. 可觀測預測

本文提出八個預測：

1. frontier Agent 系統的提升會越來越多來自 strategy routing，而不只來自 base model。
2. test-time compute 會從「多算多少」發展為「下一單位算力交給哪種 cognitive operation」。
3. multi-agent systems 會由固定 role graph 走向 dynamic role / topology allocation。
4. production Agent runtime 會顯式保存 strategy receipt、policy version、stop condition 與 fallback。
5. reframe capability 會成為 long-horizon Agent 的重要能力維度。
6. 方法庫會逐步採用 capability contract 與 verifier contract。
7. 高自治系統會需要 policy-adoption gate，避免短期 empirical gain 直接改寫 global strategy。
8. 真正高階 Global AI 會自主管理「方法空間」，而不只是問題空間。

---

# 98. 與既有 EveMissLab 研究的關係

## 98.1 MSSP / ABFR

MSSP 已提出 Structured Global Attention：

$$
\text{Select}
\rightarrow
\text{Attend}
\rightarrow
\text{Record}
\rightarrow
\text{Traverse}
\rightarrow
\text{Reconcile}.
$$

A05 將 structural traversal 提升為一般 cognition orchestration。

## 98.2 DDRA

DDRA 已分離：

$$
\boxed{
\text{Should I think more?}
}
$$

與：

$$
\boxed{
\text{What should I think about next?}
}
$$

本文將其從研究級數學 specialist routing 推廣到 Global AI 通用 cognitive strategy plane。

## 98.3 Memory Strategy Governor

MSG 已建立：

$$
\text{Need}
\rightarrow
\text{Purpose}
\rightarrow
\text{Strategy Plan}
$$

與 deterministic / versioned / replayable routing。

本文將 memory strategy pattern 提升為 general cognitive strategy。

## 98.4 CDI Semantic-Causal Control Plane

CDI 已提出：

$$
\text{Execution Plane}
\neq
\text{Semantic Control Plane}.
$$

A05 將其改寫為：

$$
\boxed{
\text{Cognitive Execution Plane}
\neq
\text{Cognitive Strategy Plane}.
}
$$

---

# 99. 外部研究支點

2026 年 adaptive test-time compute 研究已顯示，把更多計算集中於 unresolved / difficult queries 可以提高 compute efficiency，證明 uniform reasoning budget 並非必要預設。

2025–2026 年 multi-agent orchestration 研究已廣泛討論 centralized、decentralized、hierarchical 與 dynamic-adaptive coordination，並出現 high-level planner、dynamic role creation、specialist agents 與 workflow search 等設計。

MUSE 類 metacognitive agent framework 更直接把 competence self-assessment 與 strategy selection 放入 iterative self-regulation loop，顯示 operational metacognition 可以成為 autonomous-agent architecture，而不只是哲學詞彙。

本文與上述研究的差異在於：GCOA 不是另一個固定 agent framework，而是一個更一般的 Global AI 認知控制類別，使 representation、method、Agent、tool、verifier、budget、stop、fallback 與 policy evolution 都成為可路由 cognitive objects。

---

# 100. 結論

本文提出：

$$
\boxed{
\text{Global Cognitive Operating Architecture}
}
$$

作為 Global AI 的第五個基礎層。

如果 A03 回答：

> 世界變了什麼？

A04 回答：

> 現在什麼最重要？

那麼 A05 回答：

> **現在應該怎麼想？**

其完整架構為：

$$
\boxed{
\mathfrak C_G
=
(
W,
A,
Q,
\mathcal R,
\mathcal M,
\mathcal G,
\mathcal T,
\mathcal V,
\mathcal B,
\Pi,
\mathcal L
).
}
$$

真正成熟的 Global AI 不只是能調用工具，而是能：

$$
\boxed{
\text{select}
+
\text{compose}
+
\text{route}
+
\text{verify}
+
\text{stop}
+
\text{replan}
+
\text{reframe}
+
\text{learn}.
}
$$

因此：

$$
\boxed{
\text{Intelligence}
\neq
\text{Knowing How to Organize Intelligence}.
}
$$

而 Global AI 需要的恰好是後者。

將 A03、A04 與 A05 串聯，可以得到目前為止最完整的動態鏈：

$$
\boxed{
\Delta D_t
\rightarrow
\Delta W_t
\rightarrow
\Delta K_t
\rightarrow
\Delta a_t
\rightarrow
\Delta\sigma_t
\rightarrow
\text{Observe / Verify / Act}
\rightarrow
W_{t+1}.
}
$$

下一篇 GIRA-A06 將轉向另一個問題：

$$
\boxed{
\text{如果這樣的系統已經開始存在，人類是否有能力認出它？}
}
$$

也就是 Global AI 的存在、觀察、概念化、識別與正式承認之間的時間差。

---

# 參考文獻與前置研究

## EveMissLab / Neo.K 既有研究

1. Neo.K with Aletheia, **GIRA-A01｜ASI 不等於 Global AI：智能能力類別與全域操作架構類別的分離**, 2026.
2. Neo.K with Aletheia, **GIRA-A02｜局部全域與真正全域認知：觀察者、方法論座標與認知域**, 2026.
3. Neo.K with Aletheia, **GIRA-A03｜資訊海不是世界模型：去重、版本、時態、語義與 X 次結構化**, 2026.
4. Neo.K with Aletheia, **GIRA-A04｜動態關鍵結構與注意力重配置**, 2026.
5. Neo.K, **MSSP 作為 AI 結構注意力基底**, ABFR Series Paper 02, 2026.
6. Neo.K, **疑點驅動的推理資源配置：Freeze Controller、Value of Information 與自適應 Specialist Routing**, 2026.
7. Neo.K, **Memory Strategy Governor：自主記憶策略編譯與路由控制技術白皮書**, 2026.
8. Neo.K with Aletheia, **AI 不必替代計算：從傳統執行平面到語義—因果控制平面**, CDI / AIVS Paper 01, 2026.

## 外部參考

9. Zuo, B., Zhou, D. & Zhu, Y., **Adaptive Test-Time Compute Allocation with Evolving In-Context Demonstrations**, Findings of ACL 2026.
10. Zuo, B. & Zhu, Y., **Strategic Scaling of Test-Time Compute: A Bandit Learning Approach**, ICLR 2026.
11. Hou, Z., Tang, J. & Wang, Y., **HALO: Hierarchical Autonomous Logic-Oriented Orchestration for Multi-Agent LLM Systems**, 2025.
12. Zhang, W. et al., **AgentOrchestra: A Hierarchical Multi-Agent Framework for General-Purpose Task Solving**, 2025.
13. **Metacognition for Unknown Situations and Environments (MUSE)**, *Neural Networks*, 2025/2026.
14. **LLM-Based Multi-Agent Orchestration: A Survey of Frameworks, Communication Protocols, and Emerging Patterns**, *Future Internet*, 2026.

---

# Canonical Source Note

本文件的正式原稿為此 UTF-8 Markdown source。聊天介面的渲染版本不應被視為 canonical source。

數學公式 canonical delimiter 僅使用：

- inline math：` $...$ `
- display math：`$$...$$`

不得以 Unicode 數學字元替換 LaTeX source，不進行 `unicode_escape` 類 round-trip，不自行改寫反斜線、delimiter 或公式原始碼。
