# AI 原生知識展開 Runtime：BKSE 端到端架構、可信邊界與 MVP

**English Title:** AI-Native Knowledge Expansion Runtime: End-to-End Architecture, Trust Boundaries, and an MVP for BKSE  
**Series:** AI-Native Knowledge Expansion, Paper VII  
**Author:** Neo.K  
**Collaborator:** Aletheia (GPT-5.6 Sol)  
**Institution:** EveMissLab / 一言諾科技有限公司  
**Version:** v0.1  
**Date:** 2026-08-10  
**Status:** Series I — Phase I Integration Paper

## 摘要

本系列前六篇依次建立 Base Knowledge Space Expansion（BKSE）的核心理論部件：可靠基礎知識的大規模結構展開、變種身份與命題分叉、錯誤鄰域與反例空間、多證法與交叉驗證的 Proof Lattice、AI-Native Research Graph，以及在有限資源下控制組合爆炸的 Frontier Scheduler。本篇作為 Series I 第一階段的整合篇，不再主要增加新的哲學命題，而是把上述元件收斂為一套可實作、可測試、可失敗、可重播的 **AI-Native Knowledge Expansion Runtime（ANKER）**。

ANKER 的核心不是讓大型模型自由生成無限數學文本，而是建立一個嚴格的閉環：

\[
\boxed{
\text{Seed}
\rightarrow
\text{Expand}
\rightarrow
\text{Classify}
\rightarrow
\text{Attack}
\rightarrow
\text{Prove / Verify}
\rightarrow
\text{Commit}
\rightarrow
\text{Schedule}
\rightarrow
\text{Expand Again}.
}
\]

系統將生成器視為不可信候選來源，將 parser、type checker、formal prover、external checker、counterexample search、tests 與 provenance tracking 視為不同驗證層；將「未證明」「已否證」「形式有效但語義未審核」「內部新穎但文獻未檢查」分別保存，禁止壓縮成單一 `verified=true`。BKSE Runtime 的主要知識單位不是論文，而是帶有穩定身份、lineage、變種證書、反例、proof family、驗證矩陣、狀態與 open frontier 的 machine-first knowledge object。

本文提出七層 runtime、最小資料 schema、五個核心服務、任務佇列、failure taxonomy、trust boundary、Lean/Python 驗證接口、budget-aware frontier loop，以及三階段 MVP 實驗。第一階段僅需 100–500 個基礎數學 seed、SQLite/PostgreSQL、Python、Lean、單一 LLM 與 deterministic scheduler 即可驗證核心假說。第二階段加入多 prover、external checker、literature bridge 與 learned scheduler。第三階段才進入長期自主研究與跨領域擴張。

本文的核心工程主張是：

\[
\boxed{
\text{AI-native research should treat generation as cheap and verification state as precious.}
}
\]

當候選生成逐漸廉價，真正需要保存、調度與保護的資源將是 **verified attention、typed lineage 與可重播的知識狀態**。

**關鍵詞：** BKSE；AI 原生知識展開；AI 原生數學；Research Runtime；Proof Lattice；Research Graph；Frontier Scheduler；形式化驗證；Counterexample；MVP

---

# 1. Series I 第一階段的整合問題

前六篇分別回答：

\[
\begin{aligned}
P_1 &: \text{基礎知識能否形成高價值結構閉包？}\\
P_2 &: \text{如何區分表面變種、結構變種與命題分叉？}\\
P_3 &: \text{如何系統生成錯誤鄰域與反例？}\\
P_4 &: \text{如何從單一 proof 進入多路徑交叉驗證？}\\
P_5 &: \text{若論文只是 rendering，機器內部要保存什麼？}\\
P_6 &: \text{候選爆炸後，下一單位研究注意力投向哪裡？}
\end{aligned}
\]

Paper VII 的問題只有一個：

\[
\boxed{
\text{Can these six ideas form one runnable system?}
}
\]

如果不能，那麼前六篇仍只是方法論集合。

如果能，則 BKSE 從理論假說進入：

\[
\boxed{
\text{research infrastructure hypothesis}.
}
\]

---

# 2. 系統名稱與定位

本文暫稱整合 runtime 為：

\[
\boxed{
\text{ANKER}
}
\]

即：

**AI-Native Knowledge Expansion Runtime**。

名稱只是工程代號，不是新的理論分支。

ANKER 的定位不是：

- 通用 AGI；
- 完整數學家替代系統；
- 自動論文工廠；
- 無限制 conjecture generator；
- 單一 theorem prover。

而是：

\[
\boxed{
\text{a stateful verified knowledge-expansion runtime}.
}
\]

它的工作是維持：

\[
G_t
\]

並把每次生成、失敗、驗證與修正變成：

\[
G_t\rightarrow G_{t+1}.
\]

---

# 3. Runtime 核心 LOOP

ANKER 的最小循環：

\[
\boxed{
G_t
\rightarrow
F_t
\rightarrow
A_t
\rightarrow
C_t
\rightarrow
V_t
\rightarrow
\Delta G_t
\rightarrow
G_{t+1}.
}
\]

其中：

- \(G_t\)：當前 Research Graph；
- \(F_t\)：可執行 frontier；
- \(A_t\)：被 scheduler 選中的 action；
- \(C_t\)：生成的 candidate；
- \(V_t\)：驗證結果；
- \(\Delta G_t\)：經分類後的 knowledge commit。

更具體：

```text
1. Load current graph state
2. Generate frontier actions
3. Score actions
4. Select a budget-feasible portfolio
5. Generate candidate objects
6. Canonicalize and classify
7. Attack / search counterexamples
8. Prove / test / verify
9. Extract provenance and dependencies
10. Commit typed results
11. Recompute frontier
12. Repeat or stop
```

因此：

\[
\boxed{
\text{generation is one stage, not the runtime itself}.
}
\]

---

# 4. 七層架構

本文提出七層。

## Layer 0：Seed Layer

保存初始可靠知識：

- theorem；
- definition；
- axiom；
- tested algorithm；
- verified program；
- reference dataset。

要求：

\[
\boxed{
\text{seed provenance must be explicit}.
}
\]

Seed 不能只是「模型記得這是真的」。

---

## Layer 1：Representation & Identity Layer

負責 Paper II：

- parse；
- type；
- structural fingerprint；
- canonicalization；
- equivalence class；
- proposition identity；
- branch detection。

輸出：

\[
\operatorname{IdentityRecord}(K).
\]

---

## Layer 2：Expansion Layer

負責 Paper I：

- equivalent rewrite；
- specialization；
- generalization；
- converse；
- composition；
- representation shift；
- assumption ablation；
- problem transformation。

生成：

\[
C=\operatorname{Expand}(K,T).
\]

這一層**不宣告 candidate 正確**。

---

## Layer 3：Adversarial Layer

負責 Paper III：

- CounterexampleHunter；
- AssumptionAuditor；
- BoundaryMutator；
- ProofCorruptor；
- DependencyChecker。

輸出：

\[
\text{DISPROVED},
\text{INVALID},
\text{COUNTEREXAMPLE},
\text{UNKNOWN}
\]

等候選狀態。

---

## Layer 4：Verification Layer

負責 Paper IV：

- symbolic verification；
- numerical tests；
- finite exhaustive computation；
- Lean proof；
- kernel check；
- axiom audit；
- external checker；
- semantic audit。

輸出不是單一 boolean，而是：

\[
\boxed{
\mathbf V(K).
}
\]

---

## Layer 5：Knowledge Graph Layer

負責 Paper V：

- typed nodes；
- typed edges；
- provenance；
- version；
- append-only history；
- correction；
- proof lattice；
- open frontier；
- literature links。

它是系統的持久狀態。

---

## Layer 6：Scheduler Layer

負責 Paper VI：

- frontier generation；
- scoring；
- budget allocation；
- branch dormancy；
- revival；
- stopping；
- portfolio scheduling。

它決定：

\[
\boxed{
\text{what receives the next unit of verified attention}.
}
\]

---

# 5. 為什麼生成器必須是不可信元件？

ANKER 的關鍵安全假設：

\[
\boxed{
\text{Generator is untrusted}.
}
\]

不管候選來自：

- GPT；
- Claude；
- local model；
- symbolic enumerator；
- human；
- evolutionary search；

都只能得到：

\[
\text{CANDIDATE}.
\]

不能直接得到：

\[
\text{VERIFIED}.
\]

因此：

```text
LLM output
    ↓
Candidate Store
    ↓
Verifier Pipeline
    ↓
Canonical Graph
```

這與現代 proof-assistant 的基本分工相容：複雜生成或 tactic 層可以不可信，而最終 proof object 由較小 checker 驗證。Lean 官方也把未審查 AI-generated proof 視為高風險輸入，並提供更高等級的 comparator + external checker 驗證路徑。

---

# 6. Candidate Store 與 Canonical Store 必須分離

如果生成 candidate 後立刻進入 canonical graph：

\[
\text{hallucination}
\rightarrow
\text{knowledge}.
\]

所以至少分兩區：

## Candidate Store

狀態包括：

```text
NEW
PARSED
ILL_TYPED
PENDING
UNDER_ATTACK
UNDER_PROOF
```

## Canonical Knowledge Store

只接受：

```text
VERIFIED
DISPROVED
CONFLICTED
FORMALLY_VALID
TESTED
LITERATURE_LINKED
```

以及明確標記的：

```text
UNKNOWN
```

因此：

\[
\boxed{
\text{candidate persistence}
\neq
\text{knowledge admission}.
}
\]

---

# 7. 最小 Knowledge Object Schema

最小節點：

```json
{
  "id": "CLAIM-000123",
  "type": "CLAIM",
  "status": "UNKNOWN",
  "domain": "euclidean_geometry",
  "statement": {
    "natural": "...",
    "formal": null
  },
  "parents": [],
  "operator": null,
  "fingerprint": {},
  "dependencies": [],
  "proofs": [],
  "counterexamples": [],
  "verification": [],
  "frontier": [],
  "provenance": {},
  "version": 1
}
```

最重要的是：

\[
\boxed{
\text{status must remain typed}.
}
\]

---

# 8. 建議的 Status State Machine

最小狀態：

\[
\mathcal S
=
\{
NEW,
PARSED,
VALID\_FORM,
UNKNOWN,
SUPPORTED,
TESTED,
PROVED,
CROSS\_CHECKED,
DISPROVED,
CONFLICTED,
REJECTED
\}.
\]

可有：

\[
NEW\rightarrow PARSED\rightarrow UNKNOWN.
\]

之後：

\[
UNKNOWN\rightarrow PROVED,
\]

或：

\[
UNKNOWN\rightarrow DISPROVED.
\]

也可能：

\[
PROVED\rightarrow CONFLICTED
\]

如果 semantic audit 或 checker discrepancy 發現問題。

所以：

\[
\boxed{
\text{verification state is dynamic}.
}
\]

---

# 9. 「PROVED」還需要子型別

不能所有 proof 都叫同一個 PROVED。

例如：

```text
PROVED_FORMAL
PROVED_FINITE_EXHAUSTIVE
PROVED_SYMBOLIC
PROVED_CROSS_FORMALISM
```

而：

```text
TESTED_NUMERIC
```

不能混入。

因此：

\[
\boxed{
\text{epistemic type must survive storage}.
}
\]

---

# 10. Proof Lattice Service

建立服務：

```text
ProofService.propose(claim_id)
ProofService.check(proof_id)
ProofService.cluster(claim_id)
ProofService.axioms(proof_id)
ProofService.crosscheck(proof_id)
```

每個 claim 的：

\[
\mathfrak L(T)
\]

獨立維護。

如果已經有：

\[
10
\]

條相同 proof skeleton，scheduler 應降低：

\[
\text{generate another similar proof}
\]

的分數。

---

# 11. Counterexample Service

最小接口：

```text
CounterexampleService.search(claim_id)
CounterexampleService.verify(witness_id)
CounterexampleService.minimize(witness_id)
CounterexampleService.repair(claim_id)
```

若找到：

\[
x^\ast
\]

必須建立：

```text
COUNTEREXAMPLE node
REFUTES edge
```

而不是只在 log 裡寫：

> found a counterexample.

這使 failure 成為可重用知識。

---

# 12. Identity Service

最核心的去重服務：

```text
IdentityService.fingerprint(node)
IdentityService.canonicalize(node)
IdentityService.find_equivalents(node)
IdentityService.classify_variation(parent, child)
IdentityService.branch(parent, child)
```

其輸出至少：

```text
SURFACE_VARIANT
REPRESENTATION_VARIANT
STRUCTURAL_VARIANT
BRANCH
DUPLICATE
UNKNOWN_RELATION
```

如果：

\[
UNKNOWN\_RELATION
\]

就不能硬合併。

---

# 13. Scheduler Service

最小 scheduler：

```text
Scheduler.frontier(graph)
Scheduler.score(action)
Scheduler.select(portfolio, budget)
Scheduler.sleep(branch)
Scheduler.revive(branch)
Scheduler.stop(branch)
```

第一版使用 rule-based：

\[
S_F.
\]

不需要一開始就用 RL。

原因是：

\[
\boxed{
\text{debuggable scheduler}
>
\text{opaque clever scheduler}
}
\]

在 MVP 階段尤其重要。

---

# 14. Literature Bridge

數學上：

\[
\text{internally derived}
\neq
\text{historically novel}.
\]

所以需要：

```text
LiteratureService.search(claim)
LiteratureService.link(work_id)
LiteratureService.nearest_prior(claim)
```

狀態：

```text
LITERATURE_UNCHECKED
NO_MATCH_FOUND
POSSIBLE_MATCH
KNOWN_RESULT
NOVELTY_REVIEW_REQUIRED
```

即使：

\[
NO\_MATCH\_FOUND,
\]

也不應立即變成：

\[
NOVEL.
\]

---

# 15. Renderer

Renderer 將：

\[
G'
\subseteq G
\]

轉成人類介面。

例如：

```text
render_paper(topic)
render_summary(claim_id)
render_proof_explanation(proof_id)
render_failure_history(branch_id)
render_reviewer_packet(claim_id)
```

因此：

\[
\boxed{
\text{Paper is a projection of canonical state}.
}
\]

這與 2026 年 ARA 類工作將 narrative paper 與 machine-executable research artifact 分離的方向高度一致。

---

# 16. Runtime Event

每個動作都記：

```json
{
  "event_id": "EV-8821",
  "action": "ASSUMPTION_ABLATION",
  "input": ["CLAIM-31"],
  "output": ["CLAIM-88"],
  "agent": "generator-A",
  "toolchain": ["lean", "python"],
  "cost": {},
  "timestamp": "...",
  "status": "COMPLETE"
}
```

這形成 Execution Graph：

\[
G_X.
\]

而 knowledge commit 形成 Epistemic Graph：

\[
G_E.
\]

兩者不應混在一起。

---

# 17. 三張圖

完整系統同時維持：

\[
\boxed{
G_X,\quad G_A,\quad G_E
}
\]

其中：

- \(G_X\)：Execution Graph；
- \(G_A\)：Artifact Graph；
- \(G_E\)：Epistemic Graph。

例如：

```text
RUN-88
  ↓ PRODUCED
proof.lean
  ↓ SUPPORTS
PROOF-19
  ↓ PROVES
CLAIM-7
```

所以系統能回答兩類不同問題：

> AI 做了什麼？

以及：

> 我們因此知道了什麼？

---

# 18. Knowledge Commit

一次真正的研究更新：

\[
\mathcal C_t
=
(
\Delta V,
\Delta E,
P,
V
)
\]

其中：

- \(\Delta V\)：新增/更新節點；
- \(\Delta E\)：新增關係；
- \(P\)：provenance；
- \(V\)：verification record。

Commit 原則：

\[
\boxed{
\text{no silent overwrite}.
}
\]

修正必須：

```text
NEW_NODE --CORRECTS--> OLD_NODE
```

---

# 19. 最小 Trust Boundary

ANKER 至少有五個信任邊界。

## Boundary A：Seed Trust

Seed 是否真的可靠？

## Boundary B：Formalization Trust

自然語言命題：

\[
I
\]

是否正確轉成：

\[
F?
\]

## Boundary C：Proof Trust

\[
\Pi:F
\]

是否成立？

## Boundary D：Checker Trust

kernel / verifier 是否正確？

## Boundary E：World Trust

形式命題是否真的適用現實？

因此：

\[
\boxed{
\text{formal verification only closes some boundaries}.
}
\]

---

# 20. Lean 在 MVP 中的角色

Lean 不需要負責全部研究。

它負責最適合它的部分：

- theorem statement；
- proof term；
- type checking；
- dependency；
- axiom inspection；
- formal counterexample certificate；
- selected cross-check。

Lean 官方目前已明確區分一般 proof validation 與針對未審查 AI-generated proof 的高風險驗證；高等級方案可使用 sandboxed `comparator`，並以 Lean kernel 和獨立 Rust checker `nanoda` 等進行重播。這適合作為 ANKER 後期的 high-assurance lane，而不是每個低價值候選都使用最昂貴驗證。

---

# 21. Python 在 MVP 中的角色

Python 負責：

- candidate generator；
- data transform；
- numerical test；
- finite search；
- benchmark；
- scheduler；
- DB adapter；
- reporting。

但 Python `PASS` 不自動變成 formal theorem。

需要標：

```text
verification_type = NUMERICAL_TEST
```

或：

```text
verification_type = FINITE_EXHAUSTIVE
```

並保存 completeness assumptions。

---

# 22. Verifier Pipeline

最小 pipeline：

```text
Candidate
   ↓
Parse
   ↓
Type / Domain Check
   ↓
Canonicalize
   ↓
Cheap Counterexample Search
   ↓
Symbolic / Numerical Test
   ↓
Formal Proof Attempt
   ↓
Kernel Check
   ↓
Optional External Check
   ↓
Semantic / Literature Audit
```

不是每個 candidate 都跑到底。

由 scheduler 決定：

\[
\text{verification depth}.
\]

---

# 23. Verification Lanes

可以設三條 lane。

## Bronze

低成本：

- parse；
- type；
- unit test；
- numerical check。

## Silver

中成本：

- symbolic derivation；
- Lean compile；
- kernel check；
- counterexample search。

## Gold

高成本：

- fresh rebuild；
- comparator；
- external checker；
- axiom audit；
- second formalization；
- literature audit；
- human semantic review。

因此：

\[
\boxed{
\text{verification rigor is resource-aware}.
}
\]

---

# 24. 什麼時候升級驗證？

例如：

\[
R(K)=\text{downstream reuse}.
\]

若：

\[
R(K)\gg0,
\]

或：

\[
Impact(K)\gg0,
\]

就升：

\[
Bronze\rightarrow Silver\rightarrow Gold.
\]

也就是：

> 越多東西依賴的節點，越值得更嚴格驗證。

這比對所有節點平均投入相同驗證預算合理。

---

# 25. Root Dependency Priority

若：

\[
K
\]

有：

\[
10000
\]

個 descendants，

則其錯誤成本近似：

\[
E_{\mathrm{propagation}}(K)
\]

可能很高。

所以：

\[
\boxed{
\text{verification budget should be dependency-weighted}.
}
\]

Root lemma、shared definition、canonical equivalence rule 都應優先進 high-assurance lane。

---

# 26. Frontier Queue

每個 action：

```text
action_id
node_id
action_type
score
estimated_cost
required_verifier
dependencies
status
```

例如：

```text
A-19
CLAIM-7
SEARCH_COUNTEREXAMPLE
0.82
cheap
python
READY
```

這讓 scheduler 可以像 job system 一樣調度研究。

---

# 27. Portfolio

每一輪不要全壓同一類 action。

第一版可使用：

```text
35% proof / verify
20% attack / counterexample
20% structural expansion
10% literature
10% repair
5% exploration
```

這只是 MVP 初始值。

之後利用 observed gain 自我調整。

---

# 28. Budget

定義：

\[
B_t
=
(
T_t,
C_t,
G_t,
H_t
)
\]

可表示：

- token；
- CPU；
- GPU；
- human review。

每個 action 都估：

\[
\hat c(a).
\]

實際完成後記：

\[
c(a).
\]

Scheduler 因而能學：

\[
\hat c\rightarrow c.
\]

---

# 29. MVP 先不要做多模型自治

第一版最容易犯的錯誤是：

> 一開始就建立 20 個 AI agents。

沒有必要。

MVP：

\[
\boxed{
1\text{ LLM}
+
1\text{ deterministic controller}
+
Lean
+
Python
+
DB.
}
\]

角色可以是 prompt modes，而不必真的多 agent process。

這樣更容易定位：

- generator error；
- scheduler error；
- verifier error；
- storage error。

---

# 30. MVP 技術棧

最小：

```text
Python 3.x
SQLite
Lean 4
Mathlib
Pydantic / JSON Schema
Git
Markdown renderer
```

選配：

```text
PostgreSQL
Neo4j
FastAPI
Docker
external Lean checker
```

不需要第一版就使用 graph DB。

若：

\[
|V|<10^6,
\]

SQLite / relational schema 足夠做大量 MVP 測試。

---

# 31. 最小資料表

可以先只有：

```text
nodes
edges
events
proofs
verifications
frontier_actions
```

### nodes

```text
id
type
status
payload_json
fingerprint
version
created_at
```

### edges

```text
source
relation
target
```

### verifications

```text
node_id
method
status
artifact
checker_version
```

---

# 32. Seed Dataset

第一階段選：

\[
100\sim500
\]

個基礎 theorem。

來源要求：

- statement 清楚；
- domain 清楚；
- 可形式化；
- 易生成變種；
- 有反例空間；
- 最好已有 Lean theorem。

領域：

- 初等代數；
- 數論；
- 幾何；
- 集合；
- 基礎組合；
- 線性代數。

不先碰：

- 哲學；
- 模糊經驗科學；
- 高主觀領域。

---

# 33. 第一階段 Transformation Set

只做六個：

\[
\mathcal T_0
=
\{
\alpha,
eq,
spec,
gen,
conv,
ablate
\}.
\]

其中：

- rename；
- equivalent rewrite；
- specialization；
- generalization；
- converse；
- assumption ablation。

不一開始做無限制跨 theorem composition。

因為 composition 最容易造成：

\[
b^d
\]

爆炸。

---

# 34. 第一階段 Error Set

只做：

```text
ASSUMPTION_DELETE
BOUNDARY_CHANGE
QUANTIFIER_CHANGE
CONVERSE_TEST
PROOF_STEP_CORRUPTION
```

每個 error candidate 都要求：

\[
\text{failure classification}.
\]

---

# 35. 第一階段 Verification Set

```text
PARSE
TYPE
NUMERIC
LEAN
COUNTEREXAMPLE
```

Gold lane 暫時只給：

\[
5\%
\]

高依賴節點。

---

# 36. Phase I 主要假說

最重要的不是「系統發現新定理」。

而是驗證以下工程假說。

## H1：結構化去重

\[
\text{duplicate rate}
\downarrow.
\]

## H2：錯誤鄰域提高邊界辨識

\[
\text{false-premise resistance}
\uparrow.
\]

## H3：Proof Lattice 增加修復與重用

\[
\text{proof reuse}
\uparrow.
\]

## H4：Graph-centric continuation 降低長程成本

\[
C_{\mathrm{continue}}
\downarrow.
\]

## H5：Frontier Scheduler 優於 random expansion

\[
\frac{\Delta\mathcal I}{Cost}
\uparrow.
\]

如果這五個都不成立，BKSE Runtime 的工程價值就應被大幅下修。

---

# 37. Phase I 不應以「發現未解難題」當 KPI

這點非常重要。

若第一版 KPI 是：

> 找到人類不知道的新數學。

系統會被錯誤激勵。

第一版 KPI 應是：

\[
\boxed{
\text{reliable expansion quality}.
}
\]

包括：

- legal variation precision；
- branch detection；
- counterexample verification；
- proof validity；
- deduplication；
- replay；
- scheduler efficiency。

---

# 38. Phase II：多 Proof / 多 Checker

Phase I 穩定後加入：

```text
multiple proof prompts
proof clustering
external Lean checker
axiom audit
formalization alternatives
```

Lean 官方目前已為高風險 AI-generated proof 提供 comparator + external checker 的明確路徑，因此這一層已有現成可借鑑的驗證哲學。

---

# 39. Phase II：Literature Bridge

再加入：

- arXiv；
- OpenAlex；
- Semantic Scholar；
- Crossref。

但 literature search 只處理：

\[
\text{novelty / precedent}.
\]

不取代 formal verifier。

---

# 40. Phase II：Learned Scheduler

先累積：

\[
10^4\sim10^5
\]

個 action outcome。

再訓練：

\[
f_\theta(q,G_t)
\rightarrow
\widehat{ESG}.
\]

硬規則保留：

```text
UNKNOWN != FALSE
TESTED != PROVED
INTERNAL_NEW != NOVEL
LLM_OUTPUT != VERIFIED
```

---

# 41. Phase III：長期 Runtime

Phase III 才開始：

\[
24/7
\]

或長週期自治。

需要：

- crash recovery；
- checkpoint；
- budget reset；
- task lease；
- agent identity；
- concurrent writes；
- deadlock prevention；
- audit；
- sandbox。

到這一階段，系統才真正接近 long-running autonomous science infrastructure。

2026 年的 XScientist 已把 long-running、branching、repair、daemon scheduling 與 reproducibility artifact 視為核心問題；ScienceClaw 則展示共享 artifact DAG、lineage 與多 agent coordination 的另一種路徑。ANKER 可把這些概念接到 proposition-level epistemic graph，而非重新發明整套 orchestration。

---

# 42. 與 2026 ARA 的關係

2026 年的 Agent-Native Research Artifact（ARA）工作明確指出，傳統論文會把 branching research process 壓縮成線性敘事，並提出 machine-executable research package，包含 scientific logic、executable code、exploration graph 與 evidence。

這與 Paper V 的：

\[
\text{Paper}
=
\operatorname{RenderHuman}(G)
\]

高度收斂。

因此 ANKER 不應宣稱「paper-as-rendering」本身為首次提出。

ANKER 的差異應縮在：

\[
\boxed{
\text{verified epistemic expansion runtime}
}
\]

也就是：

- proposition identity；
- structural variation；
- counterexample neighborhood；
- proof lattice；
- frontier scheduler；

如何以一個 persistent graph LOOP 運行。

---

# 43. 與自監督 theorem discovery 的關係

2026 年已有工作從 axioms 與 inference rules 出發，交替進行 proof search 與 useful-theorem extraction，形成可被後續 proof 重用的 theorem library，並發現大量形式 theorem。

這證明：

\[
\boxed{
\text{self-growing formal theorem libraries are technically plausible}.
}
\]

ANKER 的差異不在「AI 會自己發現 theorem」本身。

而在於把 theorem discovery 放入更完整狀態：

\[
\text{identity}
+
\text{negative neighborhood}
+
\text{proof trust}
+
\text{lineage}
+
\text{scheduling}.
\]

---

# 44. Runtime 的核心不變量

不管未來換什麼模型、資料庫、proof assistant，ANKER 都應保持以下 invariant。

## I1

\[
\text{candidate}\neq\text{knowledge}.
\]

## I2

\[
\text{not proved}\neq\text{disproved}.
\]

## I3

\[
\text{tested}\neq\text{proved}.
\]

## I4

\[
\text{internally new}\neq\text{globally novel}.
\]

## I5

\[
\text{formal validity}\neq\text{semantic fidelity}.
\]

## I6

\[
\text{more samples}\neq\text{more structures}.
\]

## I7

\[
\text{more proofs}\neq\text{more independent trust}.
\]

## I8

\[
\text{legal expansion}\neq\text{worthwhile expansion}.
\]

這八條比任何具體實作技術更重要。

---

# 45. Failure Taxonomy

Runtime 必須能說自己怎麼失敗。

至少：

```text
GENERATION_ERROR
PARSE_ERROR
TYPE_ERROR
DOMAIN_ERROR
DUPLICATE
FALSE_CLAIM
PROOF_FAILURE
CHECKER_CONFLICT
SEMANTIC_MISMATCH
LITERATURE_DUPLICATE
SCHEDULER_WASTE
RESOURCE_TIMEOUT
TOOL_FAILURE
UNKNOWN
```

不能都變成：

```text
FAILED
```

因為 failure 本身也是訓練資料。

---

# 46. Runtime 不應自動隱藏失敗

如果：

\[
100
\]

個 candidates 中：

\[
95
\]

個失敗，

但最後找到：

\[
5
\]

個成功，

報告不能只保存成功的 5 個。

完整系統應保存：

\[
\boxed{
\text{failed branch structure}.
}
\]

這與 ARA/XScientist 類工作的探索圖理念一致，也與 Paper III 的 error neighborhood 相容。

---

# 47. 但也不能把所有失敗放進 Active Graph

區分：

\[
G_{\mathrm{canonical}},
\]

\[
G_{\mathrm{archive}}.
\]

Active graph 只保留高價值路徑。

Archive 保存完整 history。

因此：

\[
\boxed{
\text{preserve}
\neq
\text{keep active}.
}
\]

---

# 48. Compression

ANKER 也可以被理解成 research-state compression。

傳統 agent 每次重新讀：

\[
H_{1:t}.
\]

ANKER 只讀：

\[
\operatorname{RelevantSubgraph}(G_t,Q).
\]

因此 token cost：

\[
C_{\mathrm{context}}
\]

理論上可以隨 graph indexing 改善。

這也是 Phase I 應測的核心。

---

# 49. 可重播

任何 Gold-level result 必須盡量：

\[
\operatorname{Replay}(K)=PASS.
\]

包括：

- code；
- environment；
- theorem statement；
- proof；
- checker version；
- dependencies。

對非 deterministic experiment：

\[
Replay
\]

可以被降級為：

\[
ProtocolReproduction.
\]

但必須明確標記。

---

# 50. Human Gate

以下至少預設需要 human review：

- 高影響 novelty claim；
- semantic alignment disputed；
- real-world safety implication；
- public publication；
- external irreversible action。

因此：

\[
\boxed{
\text{autonomous research}
\neq
\text{autonomous authority}.
}
\]

---

# 51. MVP Repository Structure

建議：

```text
anker/
├── core/
│   ├── models.py
│   ├── identity.py
│   ├── graph.py
│   └── states.py
├── generators/
│   ├── variation.py
│   └── error_mutation.py
├── verifiers/
│   ├── python_verify.py
│   ├── lean_verify.py
│   └── counterexample.py
├── proofs/
│   ├── lattice.py
│   └── clustering.py
├── scheduler/
│   ├── frontier.py
│   └── score.py
├── render/
│   └── markdown.py
├── storage/
│   ├── db.py
│   └── schema.sql
├── seeds/
├── tests/
└── README.md
```

這已足夠開始。

---

# 52. CLI MVP

第一版 CLI：

```text
anker seed import seeds.json
anker expand CLAIM-001 --operator ablate
anker attack CLAIM-019
anker prove CLAIM-019 --lean
anker verify PROOF-008
anker frontier list
anker frontier run --budget 50
anker graph show CLAIM-019
anker render paper CLAIM-019
```

不需要 GUI。

---

# 53. 第一個 Demo

建議仍然使用直角三角形 theorem family。

原因：

- statement 簡單；
- 結構變種多；
- 反例容易；
- 可與 algebra/vector/circle 組合；
- 可形式化；
- 人類容易檢查。

Seed：

\[
a^2+b^2=c^2.
\]

讓 runtime 自己：

1. 生成表示變種；
2. 生成 converse；
3. assumption/domain mutation；
4. 找 counterexample；
5. 生成 proof；
6. 建 equivalence classes；
7. 建 open frontier；
8. scheduler 選下一步；
9. render Markdown report。

如果這個流程跑不穩，就不要先碰高等數學。

---

# 54. 第二個 Demo

程式語言版：

Seed：

```text
binary_search
```

變種：

- ascending / descending；
- duplicates；
- custom comparator；
- boundary cases；
- iterative / recursive；
- Python / Rust；
- fuzzing；
- property tests；
- complexity benchmark。

這可以測：

\[
\boxed{
\text{BKSE is not math-only}.
}
\]

---

# 55. 評測矩陣

至少分四類。

## Knowledge Quality

- duplicate precision；
- variation classification；
- branch detection；
- counterexample validity；
- proof validity。

## Runtime Efficiency

- token / useful node；
- compute / useful node；
- continuation cost；
- cache reuse。

## Research Utility

- downstream lemma reuse；
- bridge nodes；
- proof compression；
- resolved frontiers。

## Reliability

- false admission rate；
- UNKNOWN→FALSE error；
- TESTED→PROVED error；
- novelty false positive；
- replay success。

---

# 56. 最重要的 Reliability 指標

我會把：

\[
\boxed{
FAR
=
\frac{\text{invalid nodes admitted to canonical graph}}
{\text{all admitted nodes}}
}
\]

定義為：

**False Admission Rate**。

Phase I 最重要的目標之一：

\[
FAR\rightarrow0.
\]

因為一個會產生大量知識但大量污染 canonical graph 的系統沒有價值。

---

# 57. 第二個重要指標：Structural Yield

定義：

\[
\boxed{
SY
=
\frac{
\text{verified non-redundant structural nodes}
}{
\text{total executed actions}
}.
}
\]

它衡量：

> 花多少研究動作，得到多少真正新增結構？

這比：

\[
\text{samples generated}
\]

重要。

---

# 58. 第三個指標：Verification Density

定義：

\[
VD
=
\frac{
\text{verified relation edges}
}{
\text{canonical nodes}
}.
\]

但不是越高越好。

如果所有節點被無意義重證：

\[
VD\gg0
\]

也可能浪費。

所以要搭配：

\[
ProofDiversity,
Reuse,
Cost.
\]

---

# 59. 第四個指標：Continuation Compression

設 document-centric 下一輪所需 context：

\[
C_D.
\]

Graph-centric：

\[
C_G.
\]

定義：

\[
\boxed{
CCR
=
1-\frac{C_G}{C_D}.
}
\]

測試研究圖是否真的降低長程 continuation cost。

---

# 60. Phase I 成功標準

不要求「震撼世界」。

只要求：

\[
\boxed{
\begin{aligned}
&FAR \text{ 足夠低};\\
&SY_{\mathrm{scheduler}}>SY_{\mathrm{random}};\\
&\text{dedup works};\\
&\text{counterexamples are replayable};\\
&\text{Lean proofs recheck};\\
&CCR>0;\\
&\text{graph can render usable reports}.
\end{aligned}
}
\]

只要這些成立，Series I 就已經取得工程上的第一個支持。

---

# 61. 外部系統現在已經逼近哪裡？

截至 2026 年中，外部 autonomous-research infrastructure 已經明顯從「一次性 paper generation」往「長期、branching、reproducible artifacts」移動。

ARA 直接把 scientific logic、executable code、exploration graph 與 evidence 分層封裝，並保留 failed branches。

ScienceClaw + Infinite 使用 artifact DAG、typed metadata、parent lineage 與 provenance-aware agent coordination。

XScientist 進一步使用 Git-like protocol、daemon scheduling、quality gates、repair 與 re-execution hooks。

AutoResearchClaw 則強調 iterative challenge、self-healing execution、verifiable reporting、human intervention 與 cross-run learning。

因此 ANKER 的學術位置不應建立在：

> 「以前研究系統都是線性的。」

這在 2026 年已不再準確。

更精確的位置是：

\[
\boxed{
\text{verified proposition-level expansion substrate}
}
\]

及其：

\[
\text{identity}
+
\text{negative neighborhood}
+
\text{proof lattice}
+
\text{frontier scheduling}.
\]

---

# 62. 與 RO-Crate 的兼容方向

RO-Crate 1.3 已在 2026-06-22 成為 Recommendation，提供 JSON-LD 形式的 research-object metadata。

ANKER 不應另造一個完全孤立的 package 標準。

未來可以：

\[
\text{ANKER internal graph}
\rightarrow
\text{RO-Crate export}.
\]

例如：

- proof files；
- datasets；
- runtime logs；
- rendered paper；
- provenance。

這有利於外部可攜性。

---

# 63. 為什麼 Runtime 不是新的「大一統知識本體」

本文仍避免過度宣稱。

ANKER 是：

\[
\boxed{
\text{runtime architecture}
}
\]

不是：

\[
\text{complete ontology of all knowledge}.
\]

對哲學、法律、社會科學等領域，命題 identity 與 semantic equivalence 比數學困難得多。

這也是 Series II 存在的理由。

---

# 64. 與 Series II 的接口

Series I 假設相對穩定的：

\[
\text{claim identity}.
\]

但高語義領域可能有：

\[
\text{same symbol}
\neq
\text{same referent}.
\]

因此未來需要：

```text
SemanticState
JudgmentDomain
BaseSpace
ReferentState
TransitionHistory
```

作為 Knowledge Object 的附加層。

也就是：

\[
\boxed{
\text{Series II}
=
\text{semantic identity guard for high-semantic domains}.
}
\]

---

# 65. Series I Phase I 最終整體圖

整套架構可以壓成：

\[
\boxed{
\begin{aligned}
\text{Seed}
&\rightarrow
\text{Identity}\\
&\rightarrow
\text{Expansion}\\
&\rightarrow
\text{Adversarial Mutation}\\
&\rightarrow
\text{Proof / Counterexample}\\
&\rightarrow
\text{Verification}\\
&\rightarrow
\text{Proof Lattice}\\
&\rightarrow
\text{Research Graph}\\
&\rightarrow
\text{Frontier Scheduler}\\
&\rightarrow
\text{Next Expansion}.
\end{aligned}
}
\]

這就是 BKSE Runtime。

---

# 66. 最終核心 LOOP

用最短形式：

\[
\boxed{
G_{t+1}
=
\operatorname{Commit}
\left[
\operatorname{Verify}
\left(
\operatorname{Act}
\left(
\operatorname{Select}(F(G_t))
\right)
\right)
\right].
}
\]

生成器只出現在：

\[
\operatorname{Act}
\]

內。

所以 AI-native research 的本體不是 LLM。

而是：

\[
\boxed{
\text{state}
+
\text{operators}
+
\text{verification}
+
\text{selection}
+
\text{history}.
}
\]

---

# 67. 結論：從「會回答」到「會維持研究世界狀態」

Series I 一開始只是問：

> 如果我們拿畢氏定理這種基礎知識，讓 AI 不斷證明、變種、重組、驗證，會發生什麼？

經過七篇後，問題已經改變。

我們得到：

\[
\text{Base Knowledge Space Expansion},
\]

\[
\text{Structural Variation Identity},
\]

\[
\text{Error Neighborhood},
\]

\[
\text{Proof Lattice},
\]

\[
\text{AI-Native Research Graph},
\]

\[
\text{Frontier Scheduler},
\]

以及最終：

\[
\boxed{
\text{ANKER Runtime}.
}
\]

真正的轉換是：

\[
\boxed{
\text{AI answers research questions}
\rightarrow
\text{AI maintains a research state}.
}
\]

一個成熟的 AI-native research system 不只需要能說：

> 我認為 theorem \(T\) 是真的。

它還需要知道：

- \(T\) 從哪裡來；
- 它是哪一個命題；
- 有哪些等價表示；
- 哪些假設必要；
- 哪些反例已找到；
- 哪些 proof 真正不同；
- 哪些 checker 驗過；
- 哪些 upstream assumptions 被信任；
- 文獻 novelty 是否檢查；
- 哪些 branch 已失敗；
- 哪些 open frontier 尚未完成；
- 為什麼下一步選擇研究 \(Q\) 而不是 \(R\)。

因此，本系列第一階段最終可濃縮為：

\[
\boxed{
\text{AI-Native Research}
=
\text{Persistent State}
+
\text{Structured Expansion}
+
\text{Adversarial Falsification}
+
\text{Machine Verification}
+
\text{Attention Scheduling}.
}
\]

其中最珍貴的資源不是生成 token。

而是：

\[
\boxed{
\text{verified attention}.
}
\]

如果 Phase I MVP 可以證明這套 runtime 在相同資源下，比 document-centric、random-expansion baseline 產生更多**非重複、可驗證、可重用、可追溯**的結構知識，那麼 BKSE 就不再只是一個關於「高品質資料」的抽象猜想。

它會成為一個可以繼續工程化的 AI-native research architecture。

---

# 參考文獻

Lean Project. *Validating a Lean Proof*. Lean Language Reference, 2026.

Lean Project. *Comparator*. Lean Prover Project, 2026.

RO-Crate Community. *RO-Crate Metadata Specification 1.3*. Recommendation, 2026.

Liu, J. et al. (2026). *The Last Human-Written Paper: Agent-Native Research Artifacts*. arXiv:2604.24658.

Wang, F. Y., Marom, L., Pal, S., et al. (2026). *Autonomous Agents Coordinating Distributed Discovery Through Emergent Artifact Exchange*. arXiv:2603.14312.

Luo, J. (2026). *XScientist: A Git-Like Research Protocol for Long-Running Autonomous Scientific Discovery*. arXiv:2607.12301.

Liu, J. et al. (2026). *AutoResearchClaw: Self-Reinforcing Autonomous Research with Human-AI Collaboration*. arXiv:2605.20025.

Ota, K., Osa, T., & Harada, T. (2026). *Self-Supervised Theorem Discovery in a Formal Axiomatic System*. arXiv:2606.28747.

Xin, R., Xi, C., Yang, J., et al. (2025). *BFS-Prover: Scalable Best-First Tree Search for LLM-based Automatic Theorem Proving*. ACL 2025 / arXiv:2502.03438.
