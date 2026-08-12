# DTIL Runtime 與統一歷史狀態架構：從局部判定到可重播的高語義研究世界狀態

**English Title:** DTIL Runtime and Unified Historical-State Architecture: From Local Judgment to Replayable High-Semantic Research World States  
**Series:** Domain-Transition Information Logic, Paper VII  
**Author:** Neo.K  
**Collaborator:** Aletheia (GPT-5.6 Sol)  
**Institution:** EveMissLab / 一言諾科技有限公司  
**Version:** v0.1  
**Date:** 2026-08-10  
**Status:** Series II — Integration and Runtime Paper

## 摘要

Series II 前六篇依序建立了 Domain-Transition Information Logic（DTIL）的六個核心組件：Q4 局部四態與歷史狀態分離、Once / Still / Again 等路徑算子、對象重分類與判定域移位身份、Judgment Friction 與 Transition-Boundary Information、Judgment Domain 之間的 typed bridge，以及 MIF 長程歷史組合與潛在無界配置。本文作為 Series II 的封頂整合篇，將上述理論收斂為一套可實作、可驗證、可重播、可壓縮且可與 Series I ANKER Runtime 對接的 **DTIL Runtime**。

本文提出統一歷史狀態：

\[
\boxed{
\Sigma_t
=
(
\Psi_t,
\mathcal J_t,
E_t,
W_t,
\Gamma_t,
\nu_t,
M_t
)
}
\]

其中：

- \(\Psi_t\)：Semantic Identity State；
- \(\mathcal J_t\)：Judgment Domain；
- \(E_t\)：Evidence State；
- \(W_t\)：World / Process State；
- \(\Gamma_t\)：Classification State；
- \(\nu_t\in\mathbb Q_4\)：Q4 Local Information State；
- \(M_t\)：Sufficient Historical Memory。

每一個狀態變化被表示為：

\[
\boxed{
\mathcal T_t
=
(
B_t^\ast,
\Delta_t^\ast,
\mathcal C_t^\ast,
\mathcal R_t,
\mathcal B_t,
\mathbf V_t
)
}
\]

其中分別表示 transition boundary、typed difference packet、cause/trigger/guard context、reclassification record、domain bridge 與 transition verification vector。完整歷史則為：

\[
\boxed{
\mathcal H_t
=
(
\Sigma_0,
\mathcal T_1,
\Sigma_1,
\ldots,
\mathcal T_t,
\Sigma_t
).
}
\]

本文進一步提出 **DTIL Runtime 七層架構**：Semantic Identity Layer、Judgment Domain Layer、Q4 Evaluation Layer、Reclassification Layer、Transition Boundary Layer、Domain Bridge Layer、History/MIF Layer。系統不將「形式上可證明」「語義上仍是同一命題」「現在分類仍相同」「跨域後仍可詢問同一問題」「歷史上又回到了某狀態」壓成單一 `verified=true`。

本文並正式建立與 Series I ANKER Runtime 的接口。ANKER 負責：

\[
\boxed{
\text{Generate}
+
\text{Attack}
+
\text{Prove}
+
\text{Verify}
+
\text{Schedule}
}
\]

而 DTIL 負責：

\[
\boxed{
\text{Identify}
+
\text{Contextualize}
+
\text{Track}
+
\text{Translate}
+
\text{Remember}
}
\]

兩者共享 Machine-First Knowledge Object，但維護不同 trust boundaries。Lean 官方目前明確區分「theorem 是否有 valid proof」與「theorem statement 意味著什麼」，並對未審查 AI-generated proofs 提供 comparator 與 external checker 的高保證驗證路徑，說明 proof trust 與 semantic trust 必須分層。 2026 年的 Agent-Native Research Artifact 與 XScientist 等工作，則已把 exploration DAG、failed branches、claim-to-evidence anchors、provenance、re-execution hooks 與 long-running research state 作為 agent-native research infrastructure 的核心。

本文因此不宣稱首次提出 provenance、research artifact、event history、temporal logic、ontology versioning、proof validation 或 persistent research state。本文較窄的工作是建立一個 **high-semantic historical-state guard runtime**，使 AI-native knowledge expansion 在長期運作時，不只知道「得到了什麼結果」，還能知道：

- 是不是同一個命題？
- 是不是同一個對象？
- 判定域是否改變？
- 分類是否改變？
- 世界是否真的改變？
- 是何時改變、何時被發現、何時被正式提交？
- 跨域時丟了哪些資訊？
- 返回的是同一 label、同一 classification、同一 semantic identity，還是只是假返回？
- 歷史需要保存到什麼程度才能回答未來問題？

本文的核心整合命題是：

\[
\boxed{
\text{AI-native knowledge expansion without historical identity control is structurally incomplete.}
}
\]

以及：

\[
\boxed{
\text{DTIL is not a replacement for formal verification; it is the state-and-identity layer around it.}
}
\]

**關鍵詞：** DTIL；ANKER；MIF；Q4；Semantic Identity；Judgment Domain；History Runtime；Transition Boundary；Domain Bridge；Research State；AI-Native Research

---

# 1. Series II 的六個前置部件

Series II / Paper I：

\[
\boxed{
Q4
+
Judgment Domain
+
Historical State.
}
\]

Paper II：

\[
\boxed{
Once
+
Still
+
Again
+
Return Identity.
}
\]

Paper III：

\[
\boxed{
Reclassification
+
Object / Class / Semantic Identity.
}
\]

Paper IV：

\[
\boxed{
Judgment Friction
+
Transition Boundary.
}
\]

Paper V：

\[
\boxed{
Domain Bridge
+
Preservation / Loss / Incomparability.
}
\]

Paper VI：

\[
\boxed{
MIF
+
Long-Horizon Composition
+
Recurrence / Stabilization.
}
\]

Paper VII 的任務是：

\[
\boxed{
\text{turn all six into one runtime}.
}
\]

---

# 2. DTIL Runtime 的定位

DTIL Runtime 不是：

- theorem prover；
- ontology editor；
- temporal-logic prover；
- event-sourcing database；
- semantic parser；
- generic agent memory。

它是：

\[
\boxed{
\text{a high-semantic historical-state coordination layer}.
}
\]

它負責回答：

> 現在系統認為自己正在處理什麼？  
> 這個「什麼」和先前是不是同一個？  
> 這次變化發生在哪一層？  
> 這條路徑是 persistence、return、reclassification 還是 domain crossing？  
> 我們保存了多少足以區分未來查詢的歷史？

---

# 3. Unified State

核心：

\[
\boxed{
\Sigma_t
=
(
\Psi_t,
\mathcal J_t,
E_t,
W_t,
\Gamma_t,
\nu_t,
M_t
).
}
\]

這是 DTIL 的 working state。

---

# 4. Semantic Identity State

\[
\Psi_t
\]

保存：

- intent；
- base space；
- referent；
- signifier；
- signified；
- signification；
- judgment target；
- semantic history metadata。

它回答：

\[
\boxed{
\text{現在判定的還是不是原本那個東西？}
}
\]

---

# 5. Judgment Domain

\[
\mathcal J_t
\]

保存：

- object types；
- vocabulary；
- definitions；
- evaluation rules；
- thresholds；
- hysteresis；
- allowed distinctions；
- query family。

它回答：

\[
\boxed{
\text{現在是在什麼規則域下判定？}
}
\]

---

# 6. Evidence State

\[
E_t
\]

保存：

- positive evidence；
- negative evidence；
- source；
- freshness；
- confidence；
- provenance。

它回答：

\[
\boxed{
\text{現在有什麼支持與反對資訊？}
}
\]

---

# 7. World / Process State

\[
W_t
\]

表示：

> 如果研究對象本身是一個會隨時間改變的 process / object，系統目前如何表示其外部狀態。

它與 evidence 必須分開。

因為：

\[
\boxed{
\text{world changed}
\neq
\text{we learned something new}.
}
\]

---

# 8. Classification State

\[
\Gamma_t
\]

保存 object 的：

- valid classes；
- primary class；
- Q4-valued class vector；
- ontology / domain mapping metadata。

它回答：

\[
\boxed{
\text{這個對象目前被分在哪一類？}
}
\]

---

# 9. Q4 State

\[
\boxed{
\nu_t(P)
=
(e^+,e^-)
\in
\{
Y,N,B,U
\}.
}
\]

它只表示 local information state。

因此：

\[
\boxed{
Q4
\neq
History.
}
\]

---

# 10. Historical Memory

\[
M_t
\]

不是完整 raw history。

它是：

\[
\boxed{
\text{sufficient operational historical memory}.
}
\]

例如保存：

```text
seen_Y
left_Y
returned_Y
return_count
last_domain
last_semantic_shift
last_boundary
```

---

# 11. Raw History 另存

完整 history：

\[
\boxed{
\mathcal H_t
=
(
\Sigma_0,
\mathcal T_1,
\Sigma_1,
\ldots,
\mathcal T_t,
\Sigma_t
).
}
\]

Operational state：

\[
M_t
=
Compress_{\mathcal O}(
\mathcal H_t
).
\]

因此：

\[
\boxed{
\text{history storage}
\neq
\text{runtime memory}.
}
\]

---

# 12. Unified Transition

定義：

\[
\boxed{
\mathcal T_t
=
(
B_t^\ast,
\Delta_t^\ast,
\mathcal C_t^\ast,
\mathcal R_t,
\mathcal B_t,
\mathbf V_t
).
}
\]

---

# 13. Boundary

\[
B_t^\ast
\]

保存：

- actual boundary；
- observed boundary；
- declared boundary；
- uncertainty；
- candidate / confirmed status。

---

# 14. Difference Packet

\[
\boxed{
\Delta_t^\ast
=
(
\Delta\Psi,
\Delta J,
\Delta E,
\Delta W,
\Delta\Gamma,
\Delta\nu
).
}
\]

---

# 15. Transition Context

\[
\mathcal C_t^\ast
\]

保存：

- guard；
- trigger；
- cause；
- cause status；
- detector；
- policy；
- provenance。

---

# 16. Reclassification Record

\[
\mathcal R_t
\]

保存：

- replacement；
- refinement；
- add/remove；
- generalization；
- remap；
- semantic retarget。

---

# 17. Domain Bridge

\[
\mathcal B_t
\]

保存：

- source Judgment Domain；
- target Judgment Domain；
- mapping type；
- preservation profile；
- information loss；
- gain；
- round-trip test；
- bridge version。

---

# 18. Verification Vector

\[
\boxed{
\mathbf V_t
=
(
V_{\mathrm{state}},
V_{\mathrm{boundary}},
V_{\mathrm{cause}},
V_{\mathrm{identity}},
V_{\mathrm{bridge}}
).
}
\]

因此 transition 不再只有：

```text
verified = true
```

---

# 19. 七層 Runtime

本文提出：

\[
\boxed{
L_0\text{–}L_6
}
\]

七層。

---

# 20. L0 — Semantic Identity Layer

功能：

```text
capture_semantic_state()
compare_semantic_identity()
detect_referent_shift()
issue_semantic_certificate()
```

---

# 21. L1 — Judgment Domain Layer

功能：

```text
resolve_domain()
version_domain()
compare_domains()
register_threshold_policy()
register_query_family()
```

---

# 22. L2 — Q4 Evaluation Layer

功能：

```text
evaluate_positive_support()
evaluate_negative_support()
project_to_Q4()
classify_local_conflict()
```

---

# 23. L3 — Reclassification Layer

功能：

```text
evaluate_class_vector()
choose_primary_class()
detect_reclassification()
issue_reclassification_certificate()
```

---

# 24. L4 — Transition Boundary Layer

功能：

```text
detect_candidate_boundary()
confirm_boundary()
typed_diff()
classify_trigger()
classify_cause()
issue_transition_certificate()
```

---

# 25. L5 — Domain Bridge Layer

功能：

```text
map_object()
map_semantics()
map_queries()
map_history()
test_round_trip()
issue_domain_bridge_certificate()
```

---

# 26. L6 — History / MIF Layer

功能：

```text
update_history_monitor()
detect_again()
detect_loops()
detect_recurrence()
detect_stabilization()
checkpoint_history()
compress_history()
```

---

# 27. Runtime Core Loop

最小：

\[
\boxed{
\Sigma_t
\xrightarrow{\text{Observe}}
C_{t+1}
\xrightarrow{\text{Evaluate}}
\Sigma'_{t+1}
\xrightarrow{\text{Diff}}
\Delta^\ast
\xrightarrow{\text{Confirm}}
\mathcal T_{t+1}
\xrightarrow{\text{Commit}}
\Sigma_{t+1}.
}
\]

---

# 28. Candidate State 與 Canonical State

不能觀察一次就立即改 canonical state。

先產生：

\[
\Sigma'_{t+1}.
\]

再做：

- boundary confirmation；
- identity audit；
- semantic audit；
- transition verification。

所以：

\[
\boxed{
\text{candidate state}
\neq
\text{canonical state}.
}
\]

這與 ANKER 的 candidate / canonical separation 相同。

---

# 29. DTIL State Machine

狀態提交可以是：

```text
OBSERVED
PENDING
UNDER_REVIEW
CONFIRMED
CONFLICTED
REVISED
ARCHIVED
```

---

# 30. Again Detector

對：

\[
q\in Q4
\]

使用：

```text
never_seen
first_run
left
returned
```

即可維持：

\[
Again_q.
\]

---

# 31. Classification Return Detector

另外維持：

```text
primary_seen[class]
primary_left[class]
primary_return_count[class]
```

因此：

\[
AgainClass_X
\]

不和：

\[
Again_Y(P_X)
\]

混用。

---

# 32. Semantic Return Detector

只有：

\[
R_\Psi
\]

通過 Semantic Identity Guard 才成立。

不能因 label 相同就宣布：

```text
semantic_return = true
```

---

# 33. Domain Return Detector

判定域：

\[
J_A
\rightarrow
J_B
\rightarrow
J_A
\]

可得：

\[
AgainDomain_{J_A}=1.
\]

但仍需 round-trip defect：

\[
D_{cycle}.
\]

---

# 34. Judgment Friction Engine

輸入：

\[
\Sigma^-,
\Sigma^+.
\]

輸出：

\[
\boxed{
\mathfrak F
=
(
\Delta\Psi,
\Delta J,
\Delta E,
\Delta W,
\Delta\Gamma,
\Delta\nu
).
}
\]

scalar 只作 optional task projection。

---

# 35. Friction Engine 不負責因果真值

它只負責：

\[
\boxed{
\text{what changed}.
}
\]

Cause Engine 才負責：

\[
\boxed{
\text{what likely caused the change}.
}
\]

---

# 36. Boundary Engine

區分：

\[
\tau^\ast,
\hat\tau^\ast,
\tilde\tau^\ast.
\]

因此能保存 detection delay 與 commit delay。

---

# 37. Hysteresis / Debounce

Judgment Domain 可提供：

```text
enter_threshold
leave_threshold
confirmation_window
debounce_policy
```

防止：

\[
Y,N,Y,N
\]

因 threshold noise 形成假歷史。

---

# 38. Domain Bridge Engine

Bridge type：

```text
IDENTITY
EQUIVALENT
EMBED
PROJECT
SPLIT
MERGE
REINTERPRET
PARTIAL
INCOMPARABLE
```

---

# 39. Bridge Preservation Profile

保存：

```text
object
semantic
formal
classification
q4
evidence
history
queries
```

各自：

```text
PRESERVED
PARTIAL
COLLAPSED
SPLIT
REINTERPRETED
UNMAPPED
UNKNOWN
```

---

# 40. History Engine

History Engine 維護兩份資料。

### Active Memory

\[
M_t.
\]

### Archive

\[
H_t.
\]

---

# 41. Active Memory 的目的

不是忠實保存一切。

而是：

\[
\boxed{
\text{support future runtime queries efficiently}.
}
\]

---

# 42. Archive 的目的

保存：

- raw transitions；
- certificates；
- boundary revisions；
- old domain bridges；
- semantic versions；
- provenance。

---

# 43. Provenance

W3C PROV-O 已提供 Entity、Activity、Agent 以及 derivation / generation / usage 等 provenance 概念。

DTIL 不需要重新發明 provenance ontology。

可將：

- state；
- transition；
- certificate；

映射到：

\[
prov:Entity,
\]

而：

- evaluation；
- reclassification；
- semantic audit；
- bridge execution；

映射到：

\[
prov:Activity.
\]

---

# 44. RO-Crate Export

RO-Crate 1.3 已於 2026-06-22 成為 Recommendation，使用 JSON-LD 封裝 research objects。

因此 DTIL / ANKER 的 artifacts 可以未來：

\[
\boxed{
\text{export as RO-Crate}.
}
\]

不必另造全新外部封裝標準。

---

# 45. Knowledge Object

Series I 的 Machine-First Knowledge Object：

\[
K_i.
\]

DTIL 增加：

```text
semantic_state
judgment_domain
classification_state
q4_state
history_state
transition_links
domain_bridge_links
```

---

# 46. Unified Knowledge Object

最小：

```json
{
  "id": "CLAIM-42",
  "formal": {},
  "semantic": {},
  "judgment_domain": "J-3",
  "classification": {},
  "q4": "Y",
  "history_summary": {},
  "proofs": [],
  "counterexamples": [],
  "transitions": [],
  "bridges": [],
  "provenance": {}
}
```

---

# 47. ANKER 與 DTIL 的正式分工

ANKER：

\[
\boxed{
\text{structural knowledge expansion runtime}.
}
\]

DTIL：

\[
\boxed{
\text{historical semantic-state runtime}.
}
\]

---

# 48. ANKER 負責什麼？

- generate variants；
- detect structural branching；
- generate counterexamples；
- proof search；
- Proof Lattice；
- machine verification；
- Research Graph；
- Frontier Scheduler。

---

# 49. DTIL 負責什麼？

- semantic identity；
- judgment domain；
- reclassification；
- temporal return；
- transition boundaries；
- domain crossing；
- historical compression；
- recurrence / stabilization。

---

# 50. ANKER 不應自己判 Semantic Identity

形式相同：

\[
\Phi_A\approx\Phi_B
\]

不代表：

\[
\Psi_A\approx\Psi_B.
\]

所以 ANKER 遇到高 semantic-risk transformation 時，呼叫：

\[
\boxed{
DTIL.SemanticGuard.
}
\]

---

# 51. DTIL 也不應自己證明 theorem

DTIL 判定：

```text
semantic_status = ALIGNED
```

不代表：

```text
formal_status = PROVED
```

Proof 仍交給 ANKER / Lean / verifier。

---

# 52. 共同 Trust Boundary

完整 trust chain：

\[
\boxed{
Intent
\rightarrow
SemanticState
\rightarrow
FormalStatement
\rightarrow
Proof
\rightarrow
Checker
\rightarrow
HistoryCommit.
}
\]

每一段都可能失敗。

---

# 53. Lean 的位置

Lean 官方目前明確區分「proof 是否 valid」與「statement 到底意味著什麼」；對高風險未審查 AI proof，官方 Gold Standard 可使用 comparator 在 sandbox 中構建 proof，並以 Lean kernel 和 external checker 等方式重播與比對 trusted challenge statement。

所以：

\[
\boxed{
Lean
=
\text{formal proof trust lane},
}
\]

不是：

\[
\boxed{
\text{semantic identity oracle}.
}
\]

---

# 54. DTIL Semantic Guard 的位置

DTIL 補的是：

\[
\boxed{
\text{Does the trusted challenge still represent the intended object?}
}
\]

這是 proof system 外的一層。

---

# 55. Agent-Native Research Artifact 的位置

2026 年 ARA 工作指出 narrative paper 會壓縮 branching research process，並建立包含 scientific logic、code、exploration graph 與 evidence 的 machine-executable artifact。

XScientist 更進一步保存 exploration DAG、failed branches、claim-evidence anchors、content hashes、provenance、repair 與 re-execution hooks。

DTIL 與這些系統高度相容。

---

# 56. DTIL 多出的核心問題

ARA 類 artifact 主要問：

> 這個 research artifact 是怎麼產生的？

DTIL 再問：

> **產生過程中，所指、判定域、分類與歷史身份有沒有改變？**

因此：

\[
\boxed{
\text{execution provenance}
\neq
\text{semantic-state provenance}.
}
\]

---

# 57. Agents-K1 的鄰近方向

2026 年 Agents-K1 已將 scientific entities、claims、evidence、methods 與 typed relations 組成 agent-native scientific knowledge graph，並處理大規模 scientific knowledge orchestration。

這進一步說明：

\[
\boxed{
\text{agent-native research state is becoming graph-structured}.
}
\]

DTIL 可作為其上游／旁路的 historical identity schema，而非重新取代 scientific KG。

---

# 58. Self-Supervised Theorem Discovery 的接口

2026 年已有系統從 axioms / inference rules 出發，自主建立可被後續 proof 重用的 theorem library。

ANKER 可以接這種 theorem-growth loop。

DTIL 則監控：

- theorem identity；
- semantic domain；
- historical reclassification；
- cross-domain reuse。

---

# 59. Unified Runtime Loop

完整：

\[
\boxed{
G_t,\Sigma_t
\rightarrow
F_t
\rightarrow
A_t
\rightarrow
Candidate
\rightarrow
FormalVerify
\rightarrow
SemanticAudit
\rightarrow
TransitionAudit
\rightarrow
Commit
\rightarrow
(G_{t+1},\Sigma_{t+1}).
}
\]

---

# 60. Step 1 — Frontier Selection

ANKER 選：

\[
A_t.
\]

例如：

- generalize claim；
- search counterexample；
- translate theorem；
- cross-domain reuse；
- reclassify object。

---

# 61. Step 2 — Candidate Generation

生成：

\[
K'.
\]

此時：

```text
formal = UNVERIFIED
semantic = UNAUDITED
```

---

# 62. Step 3 — Structural Identity

ANKER 比較：

\[
\Phi(K),
\Phi(K').
\]

判定：

- duplicate；
- representation variant；
- structural variant；
- proposition branch。

---

# 63. Step 4 — Semantic Identity

DTIL 比較：

\[
\Psi(K),
\Psi(K').
\]

判定：

- aligned；
- drifted；
- referent shifted；
- judgment shifted；
- semantic branch。

---

# 64. Step 5 — Formal Verification

Lean / symbolic / finite checker 等處理：

\[
FormalStatus.
\]

---

# 65. Step 6 — Q4 Projection

根據：

\[
E^+,E^-,
\mathcal J
\]

得到：

\[
\nu.
\]

---

# 66. Step 7 — Reclassification Audit

若：

\[
\Gamma^-\neq\Gamma^+,
\]

判定：

- replace；
- refine；
- add；
- remap；
- retarget。

---

# 67. Step 8 — Transition Boundary

產生：

\[
B^\ast,
\Delta^\ast,
\mathcal C^\ast.
\]

---

# 68. Step 9 — Domain Bridge

若：

\[
J_A\rightarrow J_B,
\]

執行 bridge：

\[
\mathcal B_{A\to B}.
\]

---

# 69. Step 10 — History Update

更新：

\[
M_t
\rightarrow
M_{t+1}.
\]

檢查：

- Again；
- return count；
- loops；
- recurrence；
- stabilization。

---

# 70. Step 11 — Canonical Commit

只有通過 admission rule 才進 canonical graph。

---

# 71. Admission Rule

不能只用：

```text
formal = PASS
```

而應是多軸：

\[
\boxed{
State(K)
=
(
F,S,J,C,H,L,V
).
}
\]

例如：

- \(F\)：formal；
- \(S\)：semantic；
- \(J\)：judgment-domain status；
- \(C\)：classification；
- \(H\)：history status；
- \(L\)：literature；
- \(V\)：verification coverage。

---

# 72. 高語義 Admission

若：

```text
formal = PROVED
semantic = RETARGETED
```

不能作為：

```text
FAITHFUL_FORMALIZATION
```

commit。

但可以保存為：

```text
FORMALLY_VALID_SEMANTIC_BRANCH
```

---

# 73. 高歷史風險 Admission

若：

```text
current_q4 = Y
history = previously_disproved
```

可以要求更高 verification lane。

---

# 74. 高 Domain-Risk Admission

若 bridge：

```text
mapping = PROJECT
history_preservation = false
```

則 target-side theorem 不得自動宣稱：

```text
same theorem with same provenance
```

---

# 75. Runtime 事件類型

最小：

```text
SEMANTIC_CAPTURE
FORMALIZE
Q4_UPDATE
RECLASSIFY
BOUNDARY_DETECTED
BOUNDARY_CONFIRMED
DOMAIN_CROSS
RETURN
LOOP_DETECTED
STABILIZED
BRIDGE_REVISED
HISTORY_REVISED
```

---

# 76. Event-Sourced History

每次 canonical event append：

\[
\mathcal T_t.
\]

Current state 可以：

\[
\boxed{
\Sigma_t
=
Replay(
\Sigma_0,
\mathcal T_{1:t}
)
}
\]

在可重播範圍內重建。

---

# 77. 不可重播事件

現實世界或 stochastic process：

```text
replay = NONDETERMINISTIC
```

但 evidence / provenance 仍可重建。

---

# 78. State Revision

如果當前 state 判錯，

建立：

```text
STATE-v2 --CORRECTS--> STATE-v1
```

不是 overwrite。

---

# 79. History Revision

同樣：

```text
BOUNDARY-v2 --CORRECTS--> BOUNDARY-v1
```

或：

```text
SEMANTIC-v2 --REINTERPRETS--> SEMANTIC-v1
```

---

# 80. Immutable Event / Mutable Canonical Pointer

推薦：

\[
\boxed{
\text{immutable historical record}
+
\text{mutable preferred-state pointer}.
}
\]

---

# 81. DTIL Runtime Database

最小表：

```text
states
transitions
semantic_states
judgment_domains
classifications
boundaries
bridges
history_monitors
certificates
revisions
```

---

# 82. states

```text
state_id
subject_id
semantic_id
judgment_domain_id
evidence_id
world_state_id
classification_id
q4_state
history_monitor_id
version
```

---

# 83. transitions

```text
transition_id
from_state
to_state
boundary_id
difference_json
cause_json
reclassification_id
bridge_id
verification_json
```

---

# 84. history_monitors

```text
subject_id
seen_states
return_counts
domain_return_counts
classification_return_counts
loop_flags
stability_flags
supported_queries
```

---

# 85. CLI MVP

第一版可以：

```text
dtil state show SUBJECT-1
dtil evaluate CLAIM-1
dtil semantic compare K1 K2
dtil reclass inspect OBJECT-7
dtil boundary inspect T-11
dtil bridge test J-A J-B
dtil history again SUBJECT-1 Y
dtil history loops SUBJECT-1
dtil history stabilize SUBJECT-1
```

---

# 86. API

```text
POST /state/evaluate
POST /transition/commit
POST /semantic/compare
POST /reclassification/audit
POST /bridge/test
GET  /history/{id}
GET  /history/{id}/again
GET  /history/{id}/loops
```

---

# 87. 第一個 MVP 不碰哲學巨著

第一版應用三種資料：

### Formal Math

測 formal / semantic separation。

### Simple Classification

測 reclassification。

### Synthetic History

測 Again / domain crossing / boundary。

---

# 88. Demo A：Autoformalization

自然語言 theorem：

\[
I.
\]

生成 Lean：

\[
F.
\]

ANKER 驗：

\[
\Pi:F.
\]

DTIL 驗：

\[
I\equiv_{\mathrm{sem}}F?
\]

---

# 89. Demo B：Object Reclassification

object：

\[
\omega.
\]

歷史：

\[
X
\Rightarrow
Y
\Rightarrow
X.
\]

DTIL 分析：

- Q4 membership；
- primary classification；
- semantic identity；
- world state；
- return identity。

---

# 90. Demo C：Domain Crossing

\[
J_A
\rightarrow
J_B
\rightarrow
J_A.
\]

測：

- mapping；
- loss；
- round-trip defect；
- Domain Again；
- information reset 是否成立。

---

# 91. Demo D：Boundary Chatter

latent signal 在 threshold 附近波動。

比較：

- no hysteresis；
- hysteresis；
- confirmation window。

測 observed history 差異。

---

# 92. Demo E：Long-History Compression

生成：

\[
10^5
\]

個 synthetic transitions。

比較：

- raw replay；
- monitor state；
- checkpoint + summary。

測：

\[
Again,
ReturnCount_{\ge k},
Stabilization,
Loop.
\]

---

# 93. 評測類別一：Identity Reliability

- semantic drift detection；
- object identity preservation；
- class return correctness；
- pseudo-return detection。

---

# 94. 評測類別二：Boundary Reliability

- boundary precision；
- boundary recall；
- detection delay；
- revision rate；
- false chatter rate。

---

# 95. 評測類別三：Bridge Reliability

- query preservation；
- semantic preservation；
- round-trip defect；
- mapping-induced conflict detection；
- history preservation。

---

# 96. 評測類別四：History Reliability

- Again accuracy；
- loop classification；
- recurrence detection；
- stabilization detection；
- raw-vs-monitor agreement。

---

# 97. 評測類別五：Runtime Efficiency

- context reduction；
- replay cost；
- checkpoint acceleration；
- active-memory size；
- archive retrieval cost。

---

# 98. Semantic False Admission Rate

定義：

\[
\boxed{
SFAR
=
\frac{
\text{semantic-drifted nodes admitted as same object}
}{
\text{same-object admissions}
}.
}
\]

目標：

\[
SFAR\rightarrow0.
\]

---

# 99. Boundary False Admission Rate

\[
\boxed{
BFAR
=
\frac{
\text{false boundaries committed}
}{
\text{all committed boundaries}
}.
}
\]

---

# 100. Bridge False Equivalence Rate

\[
\boxed{
BFER
=
\frac{
\text{bridges labeled equivalent but violating preserved queries}
}{
\text{equivalent bridges}
}.
}
\]

---

# 101. History Compression Recall

如果 monitor 應回答：

\[
\mathcal O,
\]

定義：

\[
\boxed{
HCR
=
\frac{
\text{queries answered identically to raw history}
}{
\text{all tested history queries}
}.
}
\]

---

# 102. 重要成功標準

Series II MVP 不需要「證明哲學」。

只要求：

\[
\boxed{
\begin{aligned}
&SFAR\text{ 低};\\
&BFAR\text{ 低};\\
&BFER\text{ 低};\\
&HCR\text{ 高};\\
&\text{PseudoReturn detection works};\\
&\text{Domain crossing loss is explicit};\\
&\text{history can be replayed or audited}.
\end{aligned}
}
\]

---

# 103. 與 Series I 的完整雙層架構

可畫成：

\[
\boxed{
\text{ANKER}
\;\;\Vert\;\;
\text{DTIL}.
}
\]

---

# 104. ANKER Layer

處理：

\[
\boxed{
\text{What can be generated, proved, attacked, and verified?}
}
\]

---

# 105. DTIL Layer

處理：

\[
\boxed{
\text{What exactly is being judged, under which domain, and with what history?}
}
\]

---

# 106. Unified Research State

整合：

\[
\boxed{
\mathcal R_t
=
(
G_t,
\Sigma_t,
F_t,
B_t
).
}
\]

其中：

- \(G_t\)：Research Graph；
- \(\Sigma_t\)：DTIL Historical State；
- \(F_t\)：Frontier；
- \(B_t\)：Budget。

---

# 107. Unified Research Update

\[
\boxed{
\mathcal R_{t+1}
=
\operatorname{Commit}
\circ
\operatorname{Audit}_{DTIL}
\circ
\operatorname{Verify}_{ANKER}
\circ
\operatorname{Act}
\circ
\operatorname{Select}
(
\mathcal R_t
).
}
\]

---

# 108. 這裡的核心不是 LLM

LLM 只是：

\[
\operatorname{Act}
\]

中的一種 generator / interpreter。

真正 runtime 是：

\[
\boxed{
\text{state}
+
\text{operators}
+
\text{verification}
+
\text{identity}
+
\text{history}
+
\text{scheduling}.
}
\]

---

# 109. 為什麼這比單一 Agent Memory 更深？

普通 memory 問：

> 以前發生過什麼？

DTIL 問：

> 以前發生的那件事與現在這件事是不是同一對象、同一判定域、同一分類、同一語義？中間發生了什麼 transition？

因此：

\[
\boxed{
\text{memory}
\neq
\text{historical identity model}.
}
\]

---

# 110. Provenance 也不等於 Historical Identity

PROV-O 可以描述 entity、activity、agent 與 derivation。

但 DTIL 額外需要：

- Q4 state；
- semantic return；
- domain shift；
- pseudo-loop；
- reclassification identity。

所以：

\[
\boxed{
\text{provenance}
\neq
\text{judgment history semantics}.
}
\]

---

# 111. Knowledge Graph 也不等於 DTIL

Agents-K1 等工作顯示 agent-native scientific KG 可以保存 claims、evidence 與 typed relations。

DTIL 更專注：

\[
\boxed{
\text{temporal / semantic identity evolution of graph objects}.
}
\]

---

# 112. DTIL 不是新的萬物邏輯

本文不主張所有領域都必須使用：

\[
Q4
\]

或：

\[
DTIL.
\]

DTIL 是：

\[
\boxed{
\text{a reusable state model for domains where judgment, identity, context, and history matter}.
}
\]

---

# 113. 適合領域

尤其適合：

- AI-generated knowledge；
- autoformalization；
- ontology / schema evolution；
- theory versioning；
- agent memory；
- classification systems；
- scientific claim lifecycle；
- policy / legal interpretation history；
- long-running research agents。

---

# 114. 不適合強行使用的領域

若問題本身只有簡單 deterministic state：

\[
x_{t+1}=f(x_t),
\]

又沒有 semantic / judgment ambiguity，

使用完整 DTIL 可能只是過度工程。

---

# 115. Runtime Invariants

本文提出 12 條核心 invariant。

### I1

\[
\boxed{
B
\neq
Y\rightarrow N.
}
\]

### I2

\[
\boxed{
\text{same current state}
\neq
\text{same history}.
}
\]

### I3

\[
\boxed{
\text{Again}
\neq
\text{identity}.
}
\]

### I4

\[
\boxed{
\text{Q4 change}
\neq
\text{reclassification}.
}
\]

### I5

\[
\boxed{
\text{world change}
\neq
\text{evidence change}.
}
\]

### I6

\[
\boxed{
\text{Actual Boundary}
\neq
\text{Observed Boundary}
\neq
\text{Declared Boundary}.
}
\]

### I7

\[
\boxed{
\text{trigger}
\neq
\text{cause}.
}
\]

### I8

\[
\boxed{
\text{cross-domain transfer}
\neq
\text{copy}.
}
\]

### I9

\[
\boxed{
\text{truth preservation}
\neq
\text{information preservation}.
}
\]

### I10

\[
\boxed{
\text{finite local alphabet}
\neq
\text{finite history}.
}
\]

### I11

\[
\boxed{
\text{unbounded history}
\neq
\text{unbounded memory}.
}
\]

### I12

\[
\boxed{
\text{formal validity}
\neq
\text{semantic identity preservation}.
}
\]

---

# 116. Failure Taxonomy

最小：

```text
SEMANTIC_DRIFT
REFERENT_SHIFT
JUDGMENT_DOMAIN_SHIFT
FALSE_BOUNDARY
MISSED_BOUNDARY
RECLASSIFICATION_ERROR
PSEUDO_RETURN
MAPPING_LOSS
MAPPING_INDUCED_CONFLICT
HISTORY_LOSS
BRIDGE_DRIFT
CAUSE_MISATTRIBUTION
CHECKER_CONFLICT
UNKNOWN
```

---

# 117. Failure 也要進 History

不能只保存成功 state。

錯誤 transition 本身可成為：

\[
\boxed{
\text{negative historical knowledge}.
}
\]

---

# 118. Privacy 與 History

DTIL 若用於長期 agent memory，

歷史越完整，

privacy risk 也越高。

因此：

\[
\boxed{
\text{maximal memory}
}
\]

不應是預設目標。

---

# 119. Minimal Sufficient Historical State

應針對：

\[
\mathcal O
\]

只保存足以回答 query 的：

\[
M_t.
\]

這同時是：

- efficiency；
- privacy；
- governance；

的接口。

---

# 120. Forgetting 也應是 Typed Operation

不是直接刪除。

可以標：

```text
FORGOTTEN_BY_POLICY
COMPRESSED
ARCHIVED
IRRECOVERABLE
USER_DELETED
```

使「不知道」與「曾知道但被刪」區分。

---

# 121. Series II 的學術邊界

本文不宣稱：

- 首次提出 temporal logic；
- 首次提出 provenance；
- 首次提出 ontology versioning；
- 首次提出 event sourcing；
- 首次提出 agent-native research artifact；
- 首次提出 formal proof validation；
- 首次提出 long-term agent memory。

已有工作分別涵蓋這些方向。Lean 官方 proof validation、PROV-O、RO-Crate、OWL 2、ARA、XScientist 與 agent-native knowledge orchestration 都提供了重要現成基礎。

---

# 122. Series II 的較窄主張

DTIL 的核心位置是：

\[
\boxed{
\text{history-sensitive judgment identity}.
}
\]

也就是：

> **一個 object / proposition 在長期 AI research runtime 中，如何在不同語義、分類、判定域與歷史下保持、失去、恢復或假裝恢復其身份。**

---

# 123. Paper VII 的核心整合結果

### Result 1

\[
\boxed{
\Sigma_t
=
(
\Psi_t,
J_t,
E_t,
W_t,
\Gamma_t,
\nu_t,
M_t
)
}
\]

可以作為 DTIL 的 unified operational state。

### Result 2

\[
\boxed{
\mathcal T_t
=
(
B_t^\ast,
\Delta_t^\ast,
C_t^\ast,
R_t,
Bridge_t,
V_t
)
}
\]

可以作為 unified transition object。

### Result 3

\[
\boxed{
\mathcal H_t
=
(
\Sigma_0,
T_1,\Sigma_1,\ldots,T_t,\Sigma_t
)
}
\]

形成可重播／可壓縮的 history。

### Result 4

\[
\boxed{
ANKER
\neq
DTIL,
}
\]

但：

\[
\boxed{
ANKER
+
DTIL
}
\]

可形成互補 runtime。

### Result 5

\[
\boxed{
\text{formal proof trust}
\neq
\text{semantic identity trust}.
}
\]

### Result 6

\[
\boxed{
\text{agent memory}
\neq
\text{historical identity model}.
}
\]

### Result 7

\[
\boxed{
\text{high-semantic research requires state, transition, and identity to be jointly represented}.
}
\]

---

# 124. 最終架構圖

\[
\boxed{
\begin{aligned}
&\textbf{ANKER}\\
&\quad Seed
\rightarrow
Expand
\rightarrow
Attack
\rightarrow
Prove
\rightarrow
Verify
\rightarrow
ResearchGraph
\rightarrow
Schedule
\\[4pt]
&\hspace{4cm}\downarrow\\[4pt]
&\textbf{DTIL}\\
&\quad SemanticIdentity
\rightarrow
JudgmentDomain
\rightarrow
Q4
\rightarrow
Reclassification
\rightarrow
Boundary
\rightarrow
DomainBridge
\rightarrow
MIFHistory.
\end{aligned}
}
\]

---

# 125. 最終 Runtime 公式

\[
\boxed{
\mathcal R_{t+1}
=
\operatorname{Commit}
\left[
\operatorname{HistoricalAudit}_{DTIL}
\left(
\operatorname{Verify}_{ANKER}
\left(
\operatorname{Act}
\left(
\operatorname{Select}(
\mathcal R_t
)
\right)
\right)
\right)
\right].
}
\]

---

# 126. 結論：研究系統不只要知道「現在相信什麼」，還要知道「為什麼現在會是這樣」

Series II 從一句看似自然語言的：

> 是又不是。  
> 不是又是。  
> 又是。  
> 其實是。

開始。

經過七篇後，這些語句被拆成：

\[
\boxed{
Q4
}
\]

局部資訊狀態，

\[
\boxed{
History Operators
}
\]

路徑條件，

\[
\boxed{
Reclassification
}
\]

分類變動，

\[
\boxed{
Judgment Friction
}
\]

邊界差異，

\[
\boxed{
Domain Bridge
}
\]

跨域信息映射，

以及：

\[
\boxed{
MIF
}
\]

長程歷史組合。

最終，一個研究狀態不再只是：

\[
P=\mathbf Y.
\]

而是：

\[
\boxed{
\Sigma_t(P)
=
(
\Psi_t,
J_t,
E_t,
W_t,
\Gamma_t,
\nu_t,
M_t
).
}
\]

也就是：

> **現在認為它是什麼、為什麼這樣判、在什麼判定域下判、指的是哪個對象、之前怎麼變過、跨過哪些域、是否曾經不是、是不是又回來、回來的是哪一層。**

因此：

\[
\boxed{
\text{knowledge state}
\neq
\text{truth label}.
}
\]

它是一個：

\[
\boxed{
\text{historically situated judgment state}.
}
\]

而 Series I ANKER 則回答另一半：

> 如何讓 AI 大量生成、反駁、證明、去重、驗證與排程知識？

兩個系列合起來形成：

\[
\boxed{
\text{AI-Native Research}
=
\text{Structural Expansion}
+
\text{Formal Verification}
+
\text{Semantic Identity}
+
\text{Judgment Context}
+
\text{Historical State}.
}
\]

如果只做前半部：

\[
\text{Generate}
+
\text{Verify},
\]

AI 可能得到形式上完全正確、卻已經換了被指、判定域或歷史身份的結果。

如果只做後半部：

\[
\text{Identity}
+
\text{History},
\]

則又缺乏真正的 theorem generation、proof、counterexample 與 machine verification。

因此本文最終提出：

\[
\boxed{
\text{ANKER}
+
\text{DTIL}
=
\text{Verified Historical Knowledge Runtime}.
}
\]

這不意味著目前已得到一套完成的 universal logic。

它更像是一個可工程化研究綱領：

\[
\boxed{
\text{讓 AI 不只會產生下一個答案，而能知道自己在長期歷史中，究竟正在延續哪一個問題。}
}
\]

---

## 參考文獻

Lean Project. *Validating a Lean Proof*. Lean Language Reference, 2026.

W3C. *PROV-O: The PROV Ontology*. W3C Recommendation.

W3C. *OWL 2 Web Ontology Language Structural Specification and Functional-Style Syntax (Second Edition)*.

RO-Crate Community. *RO-Crate Metadata Specification 1.3*. Recommendation, 2026.

Liu, J., Pei, J., Huang, J., et al. (2026). *The Last Human-Written Paper: Agent-Native Research Artifacts*. arXiv:2604.24658.

Luo, J. (2026). *XScientist: A Git-Like Research Protocol for Long-Running Autonomous Scientific Discovery*. arXiv:2607.12301.

Cao, Z., Zhan, B., Shi, J., et al. (2026). *Agents-K1: Towards Agent-native Knowledge Orchestration*. arXiv:2606.13669.

Ota, K., Osa, T., & Harada, T. (2026). *Self-Supervised Theorem Discovery in a Formal Axiomatic System*. arXiv:2606.28747.

Bollig, B., Függer, M., Nowak, T., & Zeinaty, P. (2026). *Agent-Alternation-Free Epistemic Metric Temporal Logic with Past: Model Checking and Complexity*. arXiv:2607.13981.
