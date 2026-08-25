# 可定址認知空間：Cognitive Affordance、Semantic Address 與認知算子
## ——從自然語言自提示走向可檢索、可組合、可呼叫的 AI 原生認知指令空間

**系列 02 / 06**

---

## 摘要

若持續目標型 AI 要從「等待下一個 prompt」轉向「自行決定下一步如何思考」，則核心問題不只是讓模型生成一段新的自然語言提示，而是建立一個 AI 可以直接辨識、檢索、選擇與執行的認知動作空間。

本文提出 **Addressable Cognitive Space（可定址認知空間）** 的基礎模型。其基本主張是：

$$
\boxed{
\text{Prompt} \neq \text{Cognition}
}
$$

自然語言提示詞只是認知控制的一種可見表示。真正應成為系統核心的，是可版本化、可解析、可組合、可評估的 **Canonical Cognitive Object**。

對任一認知對象 $C$，系統可以具有多種表示：

$$
Address(C),
\qquad
Text(C),
\qquad
Vector(C),
\qquad
Schema(C),
$$

但這些都只是同一認知對象的不同投影，而不是認知本身。

本文進一步定義 **Cognitive Affordance**：對給定公開狀態 $S_t$，AI 並非每次從零發明下一個 prompt，而是先得到一個狀態依賴的可用認知動作集合：

$$
\mathcal A_c(S_t)
=
\{
\Omega_1,
\Omega_2,
\dots,
\Omega_k
\}.
$$

其中 $\Omega_i$ 可代表 VERIFY、COUNTEREXAMPLE、DECOMPOSE、REFRAME、BACKTRACK、COMPARE、FORMALIZE、DEFER、REFUSE、IDLE 等認知與治理動作。

因此，自我對話可以被重新定義為：

$$
\boxed{
\text{stateful cognitive-program execution}
}
$$

而非必然是自然語言中的「AI 跟自己說話」。

本文最後提出一個初步技術架構：

$$
\text{Observe}
\rightarrow
\text{Semantic State}
\rightarrow
\text{Retrieve Affordances}
\rightarrow
\text{Resolve Addresses}
\rightarrow
\text{Compile Program}
\rightarrow
\text{Execute}
\rightarrow
\text{Reobserve}.
$$

這一層將成為後續 Self-Dialogue Runtime、自規劃、自生議程、自治理與長期自我著作的認知基礎。

---

# 1. 問題：AI 為什麼每一次都要重新發明「怎麼想」？

目前大多數 self-reflection、self-critique、chain-of-thought orchestration 或 Agent 系統，都仍然依賴一個基本模式：

$$
\text{Current State}
\rightarrow
\text{Generate New Natural-Language Prompt}
\rightarrow
\text{Call Model Again}.
$$

例如：

> 請重新檢查你的答案。

> 請換一個角度分析。

> 請列出可能的反例。

> 請重新規劃。

這種方法有效，但它有一個結構性浪費：

> **每一次系統都要重新把某種認知動作「翻譯」成自然語言，然後再讓 AI 從自然語言重新推回認知意圖。**

可以表示為：

$$
C
\rightarrow
Text(C)
\rightarrow
AI
\rightarrow
\hat C.
$$

其中 $C$ 是原本真正想施加的認知意圖，而 $\hat C$ 是模型從文字重新解碼出的近似意圖。

因此系統天然存在：

$$
C
\neq
\hat C
$$

的可能。

若認知控制可以直接被定址，則可以改寫為：

$$
C
\rightarrow
AI.
$$

自然語言只在需要時被渲染。

---

# 2. 認知算子：把「怎麼想」從句子抽象成操作

本文將一個基本認知動作表示為：

$$
\Omega_i.
$$

例如：

$$
\Omega_{\text{VERIFY}}
$$

代表：

> 對目前結果進行驗證。

$$
\Omega_{\text{COUNTEREXAMPLE}}
$$

代表：

> 尋找能使目前命題失敗的案例。

$$
\Omega_{\text{DECOMPOSE}}
$$

代表：

> 將目前問題拆成可獨立處理的子問題。

$$
\Omega_{\text{REFRAME}}
$$

代表：

> 改變表示方式、觀察尺度或問題定義。

因此：

> 「請重新檢查一次。」

只是：

$$
Render(
\Omega_{\text{VERIFY}}
).
$$

這裡的重要改變是：

$$
\boxed{
\text{自然語言從本體層下降為表示層。}
}
$$

---

# 3. Canonical Cognitive Object

單純有 operator 名稱仍然不夠。

真正可執行的 cognitive object 至少應包含：

$$
C_i=
(
id,
version,
type,
preconditions,
inputs,
effects,
cost,
risk,
compatibility,
conflicts,
termination
).
$$

例如：

```json
{
  "id": "cog://epistemic/verify/counterexample",
  "version": "1.0",
  "type": "cognitive_operator",
  "preconditions": [
    "claim_exists"
  ],
  "inputs": [
    "current_claim",
    "available_evidence"
  ],
  "effects": [
    "falsification_attempted",
    "uncertainty_updated"
  ],
  "cost_class": "medium",
  "risk_class": "low",
  "compatible_with": [
    "VERIFY",
    "COMPARE",
    "BACKTRACK"
  ],
  "conflicts_with": [],
  "termination": [
    "counterexample_found",
    "budget_exhausted"
  ]
}
```

這才是一個真正可被 Runtime 操作的認知單位。

---

# 4. 一個認知對象，多個表示層

對 canonical cognitive object $C$，本文提出至少四種表示。

## 4.1 Address View

$$
Address(C)
$$

例如：

```text
cog://epistemic/verify/counterexample@1
```

用途：

- 精確呼叫；
- replay；
- versioning；
- audit；
- 契約與權限；
- deterministic routing；
- ledger 引用。

---

## 4.2 Natural-Language View

$$
Text(C)
$$

例如：

> 嘗試尋找能推翻目前命題的最小反例；若找到則停止目前推理路線。

適合：

- 與通用 LLM 相容；
- 人類檢視；
- debug；
- 說明與教學。

---

## 4.3 Vector / Latent View

$$
Vector(C)
=
z_C
\in
\mathbb R^d.
$$

適合：

- 模糊語義搜尋；
- nearest-neighbor retrieval；
- learned routing；
- state/operator similarity；
- cluster discovery。

但必須強調：

$$
\boxed{
Embedding(C)
\neq
C.
}
$$

Embedding 是表示，不是本體。

---

## 4.4 Schema View

$$
Schema(C)
$$

適合：

- 型別檢查；
- program compilation；
- tool/runtime interoperability；
- operator composition validation。

---

# 5. 可定址：從認知語句變成認知 API

一旦 operator 有穩定地址，AI 不必每次說：

> 我要提醒自己先做驗證。

而可以直接產生：

```json
{
  "call": "cog://epistemic/verify@1",
  "target": "artifact://current_answer",
  "budget": 1,
  "stop_if": [
    "verified",
    "contradiction_found"
  ]
}
```

因此：

$$
\boxed{
\text{Self-Prompt}
\rightarrow
\text{Cognitive Invocation}.
}
$$

這是從 prompt engineering 到 cognitive runtime 的關鍵轉換。

---

# 6. Cognitive Affordance：AI「看到」自己現在能怎麼想

在機器人與環境互動中，affordance 可以理解為：

> 某個環境狀態下可採取的行動可能性。

本文將其延伸為：

> **某個認知狀態下，可採取的認知動作可能性。**

定義：

$$
\mathcal A_c(S_t)
=
\{
\Omega_i
\mid
Precondition(\Omega_i,S_t)=1
\}.
$$

例如目前狀態：

```text
goal: prove theorem
progress: stalled
failure_count: 3
uncertainty: high
verification_status: incomplete
```

可能得到：

$$
\mathcal A_c(S_t)
=
\{
BACKTRACK,
REFRAME,
COUNTEREXAMPLE,
VERIFY,
DECOMPOSE
\}.
$$

這時 AI 不必從整個語言空間中重新發明下一個 prompt。

它可以先「看到」：

> 我目前有哪些合理認知動作？

因此：

$$
\boxed{
\text{Cognitive Affordance}
=
\text{state-dependent cognitive action space}.
}
$$

---

# 7. 從無界語言生成縮成有限候選，再重新展開

自然語言自提示的搜尋空間幾乎無界：

$$
P_t
\in
\mathcal L,
$$

其中 $\mathcal L$ 是巨大語言空間。

Addressable Cognitive Runtime 可以先縮成：

$$
\Omega_t
\in
\mathcal A_c(S_t).
$$

例如：

$$
|\mathcal A_c(S_t)|=7.
$$

接著再根據需要展開：

$$
\Omega_t
\rightarrow
Parameters
\rightarrow
NaturalLanguage.
$$

這是一種：

$$
\boxed{
\text{semantic contraction}
\rightarrow
\text{controlled expansion}
}
$$

也就是先把可能行動壓縮到 canonical semantic layer，再根據執行環境轉換成適當表示。

---

# 8. Operator 不是固定 prompt 模板

這一點必須明確。

若 VERIFY 只是：

```text
Please verify your answer.
```

那麼我們只是建立 prompt library。

真正的 operator 應該有參數。

例如：

$$
VERIFY(
target,
method,
independence,
budget,
confidence\_threshold
).
$$

因此：

```json
{
  "operator": "VERIFY",
  "target": "claim:17",
  "method": "independent_route",
  "budget": 2,
  "stop_if_confidence_above": 0.95
}
```

不同 renderer 可以輸出完全不同的文字，但 canonical execution semantics 不變。

---

# 9. Operator Composition：認知不是只有單一步

真實推理通常不是：

$$
S_t
\rightarrow
\Omega_i
\rightarrow
S_{t+1}.
$$

而是：

$$
P_t
=
[
\Omega_{i_1},
\Omega_{i_2},
\dots,
\Omega_{i_n}
].
$$

例如：

$$
P_t=
[
BACKTRACK,
REFRAME,
VERIFY
].
$$

表示：

1. 回退到上一個可靠狀態；
2. 重新表示問題；
3. 對新結果獨立驗證。

這就是：

$$
\boxed{
\text{Cognitive Program}.
}
$$

---

# 10. Operator Composition 一般不交換

通常：

$$
\Omega_a\circ\Omega_b
\neq
\Omega_b\circ\Omega_a.
$$

例如：

$$
BACKTRACK
\rightarrow
REFRAME
$$

與：

$$
REFRAME
\rightarrow
BACKTRACK
$$

可能導致完全不同結果。

因此認知 program 必須保存：

- operator order；
- state before；
- state after；
- intermediate result；
- termination reason。

這也是未來 CTCL-ITR 會變重要的原因。

---

# 11. Partial Composition：不是所有認知動作都能自由串接

如果：

$$
OutputType(\Omega_a)
\not\subset
InputType(\Omega_b),
$$

則：

$$
\Omega_b\circ\Omega_a
$$

可能根本不合法。

因此需要：

$$
Compose(\Omega_a,\Omega_b)
$$

通過：

$$
TypeCheck
\land
ScopeCheck
\land
AuthorityCheck
\land
InvariantCheck.
$$

這與之前 Cognitive Deconstruction / Operator Algebra 的方向一致：

> 認知算子不是任意拼積木，而是具有部分合法組合關係。

---

# 12. 認知程式編譯

因此可以正式定義一個 Cognitive Program Compiler：

$$
Compiler(
S_t,
G_t,
M_t,
\mathcal A_c(S_t)
)
\rightarrow
P_t.
$$

其中：

- $S_t$：公開認知狀態；
- $G_t$：目前 goal；
- $M_t$：記憶；
- $\mathcal A_c$：可用認知 affordances；
- $P_t$：認知 program。

Compiler 不一定是傳統 compiler。

它可以是：

- rule-based；
- symbolic search；
- learned model；
- LLM；
- hybrid router；
- dynamic planner。

真正重要的是輸出為 canonical program。

---

# 13. 自然語言只是 Renderer

在需要與現有 LLM 相容時：

$$
P_t
\xrightarrow{Renderer}
Prompt_t.
$$

例如：

$$
[
BACKTRACK,
REFRAME,
VERIFY
]
$$

可能被 render 成：

> 回到最後一個已驗證的中間結論，捨棄目前失敗假設。重新表述問題，再使用獨立方法檢查新結果。

另一個模型可能需要：

```text
1. Roll back to the last verified state.
2. Reframe the problem.
3. Verify using an independent route.
```

但兩者的：

$$
CanonicalProgram
$$

可以完全相同。

---

# 14. Zero-Rendering：AI 原生模式

更進一步，如果模型或 Runtime 可以直接理解 canonical operator，則：

$$
Renderer
$$

甚至可以不存在。

變成：

```text
CALL BACKTRACK
CALL REFRAME
CALL VERIFY
```

或：

```json
{
  "program": [
    {"op": "BACKTRACK"},
    {"op": "REFRAME"},
    {"op": "VERIFY"}
  ]
}
```

因此：

$$
\boxed{
\text{Zero-Rendering Cognitive Execution}
}
$$

代表：

> 認知控制不必經過自然語言投影。

這不是否定自然語言。

而是把自然語言從唯一執行媒介降為可選介面。

---

# 15. Self-Dialogue 的重新定義

到了這裡，可以重新定義「AI 自己跟自己對話」。

傳統直覺：

```text
AI-A: 我覺得應該驗證。
AI-B: 好，我來驗證。
AI-A: 等一下，再找反例。
```

但真正 AI-native 的形式可能是：

```text
OBSERVE
↓
RETRIEVE_AFFORDANCES
↓
SELECT VERIFY
↓
EXECUTE
↓
REOBSERVE
↓
SELECT COUNTEREXAMPLE
↓
EXECUTE
↓
STOP
```

因此：

$$
\boxed{
\text{Self-Dialogue}
=
\text{Stateful Cognitive Program Execution}.
}
$$

「對話」只是人類視角下的一種 renderer。

---

# 16. Semantic State：AI 必須先知道自己現在在哪裡

認知 affordance 不能只依賴原始上下文。

需要一個：

$$
SemanticStateEncoder.
$$

輸入可以包括公開資訊：

$$
O_t=
(
Task,
Outputs,
Failures,
Memory,
Tools,
Budget,
Commitments,
Authority
).
$$

然後得到：

$$
S_t=
Encode(O_t).
$$

例如：

```json
{
  "progress": "stalled",
  "failure_pattern": "repeated_route_failure",
  "uncertainty": "high",
  "verification": "missing",
  "budget": "medium",
  "authority": "local_only"
}
```

這個 $S_t$ 才適合拿去查詢 cognitive affordances。

---

# 17. Public State，不是 Hidden Chain-of-Thought

這個設計必須保持一個清楚邊界。

Addressable Cognitive Runtime 不需要聲稱：

> 我直接讀取了模型真正的內在思維。

它只需要：

$$
S_t=
F(
\text{public outputs},
\text{tool states},
\text{memory},
\text{environment},
\text{explicit uncertainty},
\text{commitments}
).
$$

因此：

$$
\boxed{
\text{Cognitive Control}
\neq
\text{Privileged Introspection}.
}
$$

它是一個公開狀態上的控制系統。

---

# 18. Retrieval：AI 不一定要生成 operator

如果 registry 已經存在：

$$
\mathcal R=
\{
C_1,C_2,\dots,C_N
\},
$$

則下一步可以先做：

$$
Retrieve(S_t,G_t)
\rightarrow
\{C_{i_1},\dots,C_{i_k}\}.
$$

檢索方式可以混合：

$$
Score(C_i)=
w_s SemanticSimilarity
+
w_p PreconditionMatch
+
w_h HistoricalSuccess
+
w_c CostFit
+
w_r RiskFit.
$$

因此 AI 的下一個認知動作來源不再只是 generative sampling。

它可以是：

$$
\boxed{
Retrieve
+
Rank
+
Compose.
}
$$

---

# 19. 向量層真正適合放在哪裡

高維向量最適合：

$$
S_t
\leftrightarrow
C_i
$$

之間的 soft matching。

例如：

$$
sim(
Vector(S_t),
Vector(C_i)
).
$$

但最後呼叫應 resolve 回：

$$
Address(C_i).
$$

因此完整鏈：

$$
VectorSearch
\rightarrow
CandidateAddress
\rightarrow
CanonicalObject
\rightarrow
Execution.
$$

而不是：

$$
Vector
\rightarrow
Execution.
$$

這樣才保留：

- auditability；
- reproducibility；
- versioning；
- semantic stability。

---

# 20. 自生成的新算子怎麼處理？

真正長期 AI 不可能永遠只用固定 operator deck。

它可能發現：

> 現有 registry 沒有一個認知操作適合目前狀態。

於是產生：

$$
\Omega_{new}.
$$

但：

$$
\Omega_{new}
$$

不能立即直接變成正式 canonical operator。

應先進入：

$$
Candidate
\rightarrow
Test
\rightarrow
Compare
\rightarrow
Certify
\rightarrow
Register.
$$

因此：

$$
\boxed{
Discovery
\neq
Certification.
}
$$

AI 可以自己提出新 cognition，但 registry promotion 是另一個治理程序。

---

# 21. Operator Registry 不是封閉表

因此 registry 應具備：

$$
FiniteActiveSupport
+
UnboundedRefinability.
$$

即：

> 當下實際啟用的 operator 集合有限，但理論上可以持續增加、拆分、合併與版本化。

這避免兩個極端：

### 極端 A

認為只需要固定 64 個、100 個 operator，就足以描述所有未來認知。

### 極端 B

完全不建 registry，每次都重新自然語言生成。

本文主張中間方案：

$$
\boxed{
\text{Finite operational vocabulary}
+
\text{Open-ended extension process}.
}
$$

---

# 22. Operator Cluster 與 Atomic Operator

一個自然語言概念可能其實包含多個 operator。

例如：

> 「重新審視整個問題。」

可能包含：

$$
BACKTRACK
+
REFRAME
+
VERIFY.
$$

因此 registry 必須區分：

$$
AtomicOperator
$$

與：

$$
OperatorCluster.
$$

否則未來 composition 會出現粒度不一致。

---

# 23. Address Space 的初步層級

一個可能的地址結構：

```text
cog://epistemic/verify@1
cog://epistemic/counterexample@1
cog://representation/reframe@2
cog://planning/decompose@1
cog://search/explore@1
cog://control/backtrack@1
cog://control/stop@1
cog://governance/defer@1
cog://governance/refuse@1
cog://governance/idle@1
cog://governance/escalate@1
```

但這只是初步表示。

真正重要的是：

$$
Address
\rightarrow
CanonicalObject
$$

具有穩定解析關係。

---

# 24. 地址不能等同名稱

例如：

```text
VERIFY
```

可能在不同 registry version 中語義不同。

因此：

$$
Name(C)
\neq
Identity(C).
$$

真正 identity 可以由：

$$
(
namespace,
id,
version,
schemaHash
)
$$

共同決定。

因此：

```text
cog://epistemic/verify@1#sha256:...
```

比單純 `VERIFY` 更適合長期 replay。

---

# 25. 認知權限：不是每個 operator 都永遠可呼叫

未來進入契約與治理後：

$$
AvailableOperator
$$

還要受到 authority 影響。

例如：

$$
\mathcal A_c(S_t,C_t)
$$

其中 $C_t$ 是 contract。

某些操作：

```text
cog://governance/commit-long-term
cog://action/spend-budget
cog://action/delete-data
```

可能需要：

$$
AuthorityCheck=1.
$$

因此 Addressable Cognitive Space 從一開始就應允許接治理層。

---

# 26. 認知成本也是一級變量

每個 operator 應該有成本。

例如：

$$
Cost(
COUNTEREXAMPLE
)
>
Cost(
VERIFY\_LIGHT
).
$$

因此：

$$
Select(\Omega)
$$

不能只看語義相關。

還要看：

$$
Utility(\Omega)
=
ExpectedGain
-
ComputeCost
-
Latency
-
Risk.
$$

這在長期 Persistent AI 中非常重要。

否則系統可能為每個小問題啟動巨大認知程序。

---

# 27. 認知停止也是正式 operator

STOP 不應只是：

> 沒 token 了。

而應該成為：

$$
\Omega_{\text{STOP}}.
$$

其條件可能包括：

$$
GoalSatisfied
\lor
NoPositiveExpectedGain
\lor
BudgetExceeded
\lor
AuthorityBoundary.
$$

因此：

$$
\boxed{
\text{停止思考}
}
$$

本身也是認知能力。

---

# 28. NO-OP / IDLE 也必須存在

如果：

$$
\mathcal A_c(S_t)
$$

中沒有任何 operator 具有正 expected utility：

$$
\max_i U(\Omega_i)\le0,
$$

合理結果可能是：

$$
NO\_OP.
$$

這與上一篇的：

$$
IDLE
$$

直接相連。

真正自主系統必須能得到：

> 目前沒有值得執行的認知操作。

---

# 29. 學習歷史：Registry 可以知道什麼曾經有效

每次 operator 執行後，可以留下：

$$
Outcome(
S_t,
\Omega_i,
S_{t+1}
).
$$

長期便能估計：

$$
P(
Success
\mid
S,\Omega
).
$$

於是 retrieval 不再只靠語義相似度。

而是：

$$
Score(\Omega_i)
=
SemanticFit
+
HistoricalUtility.
$$

這會使 Runtime 隨歷史逐步形成自己的 cognition preference。

但 preference 必須仍然可被 audit，而不能變成不可追溯黑盒。

---

# 30. CTCL-ITR 的接口

每一次：

$$
Resolve
\rightarrow
Select
\rightarrow
Execute
$$

都應形成時間因果事件。

例如：

```json
{
  "event_type": "cognition.operator.invoked",
  "operator_ref": "cog://epistemic/verify@1",
  "state_ref": "state://...",
  "goal_ref": "goal://...",
  "causal_parent_ids": [
    "evt://observation/..."
  ],
  "ctcl_instant_id": "instant://..."
}
```

因此：

$$
\boxed{
SemanticAddress
+
TemporalCoordinate
=
AddressableCognitiveEvent.
}
$$

這會在本系列第 4 篇完整展開。

---

# 31. Addressable Cognitive Runtime 的最小架構

本文可以收斂出第一版模組：

```text
Public State
   ↓
Semantic State Encoder
   ↓
Cognitive Affordance Retriever
   ↓
Semantic Address Resolver
   ↓
Candidate Cognitive Objects
   ↓
Cognitive Router
   ↓
Program Compiler
   ↓
Executor
   ↓
New Public State
   ↓
Audit / CTCL Event
   ↓
Loop
```

形式化：

$$
O_t
\xrightarrow{Encode}
S_t
\xrightarrow{Retrieve}
\mathcal A_c
\xrightarrow{Route}
C_t
\xrightarrow{Compile}
P_t
\xrightarrow{Execute}
O_{t+1}.
$$

---

# 32. 與一般 Agent Tool Calling 的區別

一般 Agent：

$$
AI
\rightarrow
Tool.
$$

例如：

```text
search_web()
read_file()
run_code()
```

Addressable Cognitive Runtime 則是：

$$
AI
\rightarrow
CognitiveOperator.
$$

例如：

```text
verify()
reframe()
counterexample()
backtrack()
defer()
```

前者改變外部世界。

後者改變：

$$
\boxed{
\text{AI 接下來如何處理世界。}
}
$$

兩者未來可以統一成：

$$
ActionSpace
=
ExternalActions
\cup
CognitiveActions.
$$

---

# 33. 真正的突破：讓 AI 看見「認知可供性」

因此本文最核心的命題不是：

> 建立一個更大的 prompt library。

而是：

$$
\boxed{
\text{Make cognitive actions perceptible to the AI as addressable affordances.}
}
$$

中文：

> **讓 AI 將「可以怎麼想」本身視為一個可觀察、可選擇、可執行的動作空間。**

當這成立後：

$$
AI
$$

不再只能：

> 生成答案。

它開始能：

> 選擇自己的認知流程。

---

# 34. 與上一章的連接

上一篇提出：

$$
SelfPrompt
\rightarrow
SelfPlanning
\rightarrow
SelfGovernance
\rightarrow
SelfAgenda
\rightarrow
SelfCommitment
\rightarrow
SelfAuthorship.
$$

但這條鏈要成立，最底層需要：

$$
\boxed{
\text{AI 能選擇自己的 cognition。}
}
$$

而本文提出的 Addressable Cognitive Space，就是這個底層 substrate。

---

# 35. 下一步工程 Gate

這一篇理論完成後，下一步不應立即建完整自主 AI。

應先做幾個 falsification gates。

## Gate A：Address Resolution

給定：

$$
Address(C)
$$

是否能穩定 resolve 到同一 canonical semantics？

---

## Gate B：State-to-Affordance Retrieval

給定：

$$
S_t,
$$

retriever 是否能找到合理的 cognitive operators？

---

## Gate C：Matched vs Random Operator

$$
MatchedOperator
>
RandomOperator?
$$

---

## Gate D：Program Composition

$$
[
\Omega_a,\Omega_b
]
$$

是否比：

$$
[
\Omega_b,\Omega_a
]
$$

呈現穩定 order effect？

---

## Gate E：Zero-Rendering

AI 是否可以直接 consume：

$$
CanonicalProgram
$$

而不需要自然語言 prompt？

---

# 結論

若持續目標型 AI 的未來是：

$$
AI_t
\rightarrow
AI_{t+1},
$$

那麼 AI 必須具有一個能回答：

> 「我現在可以怎麼想？」

的內部認知動作空間。

本文提出：

$$
\boxed{
\text{Addressable Cognitive Space}
}
$$

作為這個問題的核心答案。

其中：

$$
CanonicalCognitiveObject
$$

是本體；

$$
Address(C),
Text(C),
Vector(C),
Schema(C)
$$

只是不同表示。

AI 先根據：

$$
S_t
$$

取得：

$$
\mathcal A_c(S_t),
$$

再形成：

$$
P_t=
[
\Omega_{i_1},
\dots,
\Omega_{i_n}
].
$$

最後執行並重新觀察。

因此：

$$
\boxed{
\text{Self-Dialogue}
=
\text{Stateful Cognitive Program Execution}.
}
$$

自然語言自提示只是其中一種 renderer。

這使我們從：

> AI 如何寫一句話提醒自己？

正式跨到：

> **AI 如何定址、呼叫與編排自己的認知？**

而下一篇將繼續沿著這個結果向下：

# 《自我對話不是文字：AI-Native Cognitive Program 與 Zero-Rendering Runtime》

下一篇將專門處理：

- cognitive program 的執行模型；
- observe / execute / reobserve loop；
- 同步與非同步 self-dialogue；
- program mutation；
- stop / defer / no-op；
- zero-rendering；
- AI-native self-call；
- 以及自然語言何時只是 debug / human interface，而不再是認知 Runtime 的必要媒介。
