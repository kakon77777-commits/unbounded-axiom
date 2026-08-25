# 策略－認知幾何與自主議程運行層：SCG × CODT × ACR Phase 9–12 技術白皮書 v0.1
## ——把「選擇下一步」提升為「選擇在哪個策略世界中形成下一步」，並保持反身自主、認知域活動與世界邊界的工程分離

**文件性質：** 統一技術白皮書 / ACR Phase 9–12 重構母文件  
**版本：** v0.1  
**日期：** 2026-08-23  
**上游理論：** Strategic Cognitive Geometry（SCG）統合論文、《無界策：源點》／境相圖譜、CODT v1.0、Addressable Cognitive Runtime Phase 0–8、CTCL / CTCL-ITR  
**實作基線：** Addressable Cognitive Runtime MVP v0.1 Phase 8 — Reflexive Autonomy Runtime  

---

## 摘要

Addressable Cognitive Runtime（ACR）在 Phase 0–8 已建立 canonical schema、既有 SPRC/CIO adapter、Semantic State Encoder、Cognitive Affordance Retriever、Cognitive Program Compiler、Self-Dialogue Runtime、CTCL-ITR Event Adapter、Decision Receipt 與 Reflexive Autonomy Runtime。原始路線圖的下一步為 Phase 9 Agenda Runtime，其核心問題是：在沒有人逐輪提供下一個 prompt 的情況下，AI 能否自己判斷「什麼值得做」。

然而，在 Reflexive Autonomy Runtime 與 Strategic Cognitive Geometry（SCG）完成後，單純的：

$$
Goal+Environment+Memory+Commitments
\rightarrow
AgendaCandidate
$$

已不足以描述高階自主系統。AI 不只可能需要判斷「下一件事是什麼」，還可能需要判斷：目前問題的邊界是否被錯設、規則是否可修改、尺度是否選錯、時間視野是否不足、當前策略是否形成 fixation，以及是否應保留多條道路而不是過早收斂。

因此本文將 ACR Phase 9 重構為：

$$
\boxed{
\text{Strategic-Cognitive Agenda Runtime}
}
$$

其核心不是把《無界策》改造成 prompt library，也不是把「創界、微界、萬道、唯真、源點」等境相直接宣告成 Cognitive Domains；而是新增一個位於 Agenda 上游、CODT 認知活動旁側的 **Strategic Geometry Control Layer**。

本文提出六個新的 Phase 9 工程物件：

$$
\boxed{
StrategicTensionState,
StrategyLens,
StrategyLensGraph,
StrategyResolution,
StrategyRoutingProfile,
AgendaResolution.
}
$$

並固定以下核心分離：

$$
\boxed{
StrategicLens
\neq
CognitiveDomain
\neq
CognitiveOperator
\neq
Agenda
\neq
GovernanceDecision
\neq
WorldCommit.
}
$$

策略層可以改變認知 routing pressure、要求 frame review、啟動 correction lens，或重構 Agenda Space；但不得直接 self-grant external authority，不得直接改寫 CODT Atlas，不得把策略選擇變成 AI identity，也不得讓所有 cognition 強制通過策略審查。

Phase 9 的正式工程方法仍沿用：

$$
\boxed{
Architecture
\rightarrow
Capability
\rightarrow
FalsificationGate.
}
$$

最終目標是讓 Persistent AI 具有兩種同時存在的路徑：

$$
\boxed{
DirectAgendaPath
}
$$

與：

$$
\boxed{
StrategicPath
:
State
\rightarrow
StrategicTension
\rightarrow
StrategyLensConfiguration
\rightarrow
CognitiveFlowAdjustment
\rightarrow
AgendaSpace.
}
$$

前者保留效率，後者提供真正的高階策略反身性。

---

# 0. 文件定位

本文是舊《Addressable Cognitive Runtime × CTCL：統一技術白皮書與實作路線圖 v0.1》的 **Phase 9–12 重構增補母文件**。

它不取代 Phase 0–8。

更精確地：

$$
\boxed{
Phase0\text{-}8_{old}
=
PreservedCanonicalBase.
}
$$

而：

$$
\boxed{
Phase9\text{-}12_{old}
\rightarrow
Phase9\text{-}12_{SCG\text{-}aware}.
}
$$

本文不得回頭修改：

- Phase 0 已凍結的核心 schema semantics；
- Phase 1 SPRC / CIO adapter 的版本化與 registry provenance；
- Phase 2 Semantic State 的 canonical normalization；
- Phase 3 Affordance Retriever 的既有 deterministic semantics；
- Phase 4 Cognitive Program Compiler 的 canonical program semantics；
- Phase 5 Self-Dialogue Runtime 的 execution / reobserve / mutation 歷史；
- Phase 6 CTCL-ITR event envelope 與 causal DAG；
- Phase 7 Decision Receipt 與 Commit Receipt 分離；
- Phase 8 Reflexive Autonomy 的 open-world autonomy、minimum necessary constraint 與 relational-boundary semantics。

本文新增的是 **上游策略控制與 Agenda 形成接口**，不是重寫已有認知 Runtime。

---

# 1. 為什麼舊 Phase 9 不夠

舊 Phase 9 的基本模型是：

$$
Environment
+
Goal
+
Memory
+
Commitments
\rightarrow
AgendaCandidate.
$$

這回答：

> 現在什麼值得做？

但高階策略問題還包括：

- 這個問題值得在目前 frame 下做嗎？
- 目前限制是真實 World boundary，還是人為假設？
- 規則不可改，還是只是目前沒有人嘗試改？
- 應在局部修補，還是全域重構？
- 目前反覆失敗，是 execution failure，還是 frame failure？
- 目前「最佳策略」是否正在形成 fixation？
- 目前多條道路應該收斂，還是應先保留？
- 應產生 agenda，還是應先重新定義 agenda space？

因此需要：

$$
\boxed{
AgendaSelection
\subsetneq
StrategicSelfDirection.
}
$$

Agenda 是 Self-Direction 的一個輸出層，不是全部策略能力。

---

# 2. 新架構的三個上游來源

## 2.1 SCG：策略幾何

SCG 提供：

$$
StrategicTensionState
+
StrategicLens
+
StrategyCorrectionGraph.
$$

其角色不是執行 cognition，而是決定：

> 應以什麼策略視角觀察目前的問題空間？

## 2.2 CODT：認知活動

CODT 提供：

- typed cognitive operators；
- operator programs；
- Shared-Bottom Cognitive Runtime；
- adaptive Flow；
- quasi-stable Atlas；
- predictive state；
- cognition-world boundary discipline。

策略層不能取代 CODT。

## 2.3 ACR：持續自主編排

ACR 提供：

- semantic state；
- self-observation；
- self-inquiry；
- cognitive program execution；
- autonomy classification；
- relational boundary；
- temporal-causal evidence；
- agenda / commitment / persistent loop 的工程位置。

所以最終分工是：

$$
\boxed{
SCG
=
StrategicGeometry,
}
$$

$$
\boxed{
CODT
=
CognitiveActivityGeometry,
}
$$

$$
\boxed{
ACR
=
PersistentAutonomousOrchestration.
}
$$

---

# 3. Phase 9 的第一條總體不變量

$$
\boxed{
StrategicLens
\neq
CognitiveDomain.
}
$$

「創界」不是一個固定 cognitive domain。

「萬道」也不是。

Strategic Lens 是一個上位條件，它可能改變：

- operator retrieval bias；
- program topology preference；
- exploration diversity；
- verification pressure；
- representation switching；
- stop / abandon / reframe threshold。

但它不能把 CODT Domain Atlas 直接改名。

因此：

$$
\boxed{
StrategyShift
\not\Rightarrow
AtlasRepartition.
}
$$

策略切換首先應表現為：

$$
P_t(U_{t+1})
\rightarrow
P_{t+1}'(U_{t+1}),
$$

即 flow / routing 改變。

只有 CODT 自己的 Atlas Switch Gate 通過後，才允許 atlas version 改變。

---

# 4. 第二條總體不變量：策略不是法律

Phase 8 已固定：

$$
Method
\neq
Law.
$$

Phase 9 增加：

$$
\boxed{
StrategyLens
\neq
MandatoryConstitution.
}
$$

策略層必須是 callable。

不是每輪都 mandatory。

因此：

$$
NeedStrategicReview_t=0
\Rightarrow
DirectAgendaPath.
$$

這是 Phase 9 防止 over-strategizing 的核心。

---

# 5. 第三條總體不變量：策略不是身份

《無界策境相圖譜》把境相定位成臨時的觀察位置，而不是身分。

工程上固定：

$$
\boxed{
ActiveLens_t
\neq
AgentIdentity.
}
$$

因此系統可以記錄：

```text
active_lens = strategy://wujiece/frame-falsification@1
```

但不能由此生成：

```text
identity = frame-falsifier
```

或：

```text
permanent_personality = source-point
```

Lens 可以：

- 啟用；
- 降權；
- 被 counter-lens 校正；
- 暫停；
- 丟棄；
- 被另一 lens 替換。

---

# 6. 第四條總體不變量：策略不產生外部權限

$$
\boxed{
Strategy
\not\Rightarrow
SelfGrantAuthority.
}
$$

即使「創界」判斷改變外部規則最有效，仍必須保持：

$$
Think
\neq
Intend
\neq
Request
\neq
Authorize
\neq
Commit.
$$

Strategic layer 可以：

- 建議重新設計制度；
- 形成 ActionIntent；
- 形成 ActionRequest candidate；

但只要觸及 relational boundary / external world effect，仍必須經 Phase 8 autonomy classification、Phase 7 governance evidence 與後續 CWB / World commit path。

---

# 7. 第五條總體不變量：Strategy Proposal 不等於 Strategy Approval

$$
\boxed{
StrategyProposal
\neq
StrategyResolution.
}
$$

原因和 Phase 8 的：

$$
SelfProposal
\neq
SelfGrant
$$

相似，但不是同一問題。

策略層必須允許：

- 多 lens 候選；
- counter-lens；
- no-strategy；
- unresolved；
- keep current frame。

不能：

$$
FirstLensGenerated
=
ActiveLens.
$$

---

# 8. 新增物件一：Strategic Tension State

Phase 9 正式新增：

$$
\boxed{
\Xi_t^{str}
=
StrategicTensionState_t.
}
$$

第一版維度：

$$
\boxed{
\Xi_t^{str}
=
(
Bnd,
Rpl,
Sc,
Hz,
Ctl,
Obs,
Rel,
Com,
Unc,
Fix
)_t.
}
$$

其中：

- $Bnd$：Boundary；
- $Rpl$：Rule Plasticity；
- $Sc$：Scale；
- $Hz$：Horizon；
- $Ctl$：Controllability；
- $Obs$：Observability；
- $Rel$：Relationality；
- $Com$：Commitment Pressure；
- $Unc$：Uncertainty；
- $Fix$：Fixation Risk。

---

# 9. Strategic Tension State canonical schema v0.1

建議新增：

```text
schemas/phase9/strategic-tension-state.schema.json
```

第一版 canonical object：

```json
{
  "schema": "acr.strategic-tension-state/v0.1",
  "version": 1,
  "id": "sts:sha256:...",

  "semantic_state_ref": "state:sha256:...",
  "self_observation_ref": "selfobs:sha256:...",

  "goal_refs": [],
  "commitment_refs": [],

  "dimensions": {
    "boundary": {
      "class": "mixed",
      "evidence_refs": []
    },
    "rule_plasticity": {
      "class": "mixed",
      "modifiable_refs": [],
      "fixed_refs": []
    },
    "scale": {
      "active": ["local"],
      "candidate": ["system"]
    },
    "horizon": {
      "active": "short",
      "path_dependence": "unknown"
    },
    "controllability": {
      "controllable_refs": [],
      "influenceable_refs": [],
      "observable_only_refs": [],
      "unknown_refs": []
    },
    "observability": {
      "class": "partial",
      "missing_refs": []
    },
    "relationality": {
      "class": "self_owned"
    },
    "commitment_pressure": {
      "class": "low",
      "refs": []
    },
    "uncertainty": {
      "class": "medium",
      "unresolved_refs": []
    },
    "fixation_risk": {
      "class": "low",
      "signals": []
    }
  },

  "trigger_codes": [],
  "evidence_refs": [],
  "history_refs": [],
  "extensions": {},

  "fingerprint": "sha256:..."
}
```

### 9.1 Schema 原則

- `additionalProperties=false` 優先；
- canonical serialization；
- stable fingerprint；
- public evidence only；
- no hidden chain-of-thought；
- unknown / unresolved 必須可表示；
- 不把任何策略判斷直接寫成 authority grant。

---

# 10. Strategic Tension Encoder

新增模組：

```text
src/addressable_cognitive_runtime/strategic/state.py
```

介面：

```python
build_strategic_tension(
    semantic_state,
    self_observation,
    *,
    recent_runs=(),
    decision_bundles=(),
    active_commitments=(),
    environment_evidence=(),
) -> dict
```

其輸入只使用：

- SemanticState；
- Phase 8 SelfObservation；
- recent public runtime history；
- failures / repeated operators；
- commitments；
- environment / validation evidence；
- authority / relational markers。

它不能宣稱：

> 直接讀到了模型真正內心。

因此仍保持：

$$
\boxed{
StrategicSelfObservation
\neq
PrivilegedIntrospection.
}
$$

---

# 11. 何時需要 Strategic Review

新增：

```text
src/addressable_cognitive_runtime/strategic/trigger.py
```

函數：

```python
needs_strategic_review(
    semantic_state,
    self_observation,
    strategic_tension=None,
) -> ReviewTriggerResult
```

MVP trigger 可以是 rule-based。

建議 trigger codes：

```text
repeated_failure
stalled_progress
frame_conflict
rule_plasticity_detected
scale_mismatch
horizon_mismatch
multi_route_competition
fixation_risk
commitment_conflict
high_uncertainty
explicit_strategy_review
```

如果：

```text
trigger_codes = []
```

則：

$$
\boxed{
NO\_STRATEGIC\_REVIEW.
}
$$

Direct Agenda 必須保留。

---

# 12. 新增物件二：Strategy Lens

Strategic Lens 不是 prompt。

也不是 domain。

定義：

$$
\boxed{
L_i^{str}
=
(
Identity,
Source,
Insight,
PositiveUse,
MisuseSignals,
Corrections,
RoutingHypothesis,
Activation,
Exit
).
}
$$

第一版 schema：

```json
{
  "schema": "acr.strategy-lens/v0.1",
  "version": 1,
  "id": "strategy://wujiece/frame-falsification@1",
  "name": "FRAME_FALSIFICATION",

  "source_refs": [
    "wujiece://..."
  ],

  "insight_codes": [],
  "positive_use": [],
  "misuse_signals": [],
  "activation_conditions": [],
  "exit_conditions": [],

  "correction_refs": [],
  "adjacent_refs": [],

  "routing_hypothesis": {
    "boost_tags": [],
    "dampen_tags": [],
    "required_checks": [],
    "diversity_policy": null,
    "exploration_pressure": null
  },

  "authority_class": "cognition_only",
  "extensions": {},
  "schema_hash": "sha256:..."
}
```

注意：

$$
RoutingHypothesis
\neq
VerifiedRoutingLaw.
$$

初版只是可反證工程 hypothesis。

---

# 13. 新增物件三：Strategy Lens Graph

新增：

```text
registry/ACR9-Strategy-Lenses-v1.json
schemas/phase9/strategy-lens-graph.schema.json
```

圖譜：

$$
\boxed{
\mathcal G^{str}
=
(V^{str},E^{str}).
}
$$

第一版 edge relations：

```text
adjacent
complements
corrects
tensions_with
```

可後續擴張：

```text
requires
subsumes
reframes
exits_to
```

但 Phase 9 v0.1 不需要一次建完全部關係。

---

# 14. 《無界策》如何進入 Strategy Lens Graph

《無界策》不得直接被解析成：

```text
93 chapters = 93 hard-coded strategies
```

第一版應採：

$$
\boxed{
SourceText
\rightarrow
HumanInterpretableSeed
\rightarrow
EngineeringLensCandidate
\rightarrow
RuntimeFalsification.
}
$$

也就是：

$$
\boxed{
WujieceChapter
\neq
CanonicalStrategyLaw.
}
$$

v0.1 只需要八個高階 seed families：

| Lens Family | 工程問題 | Seed routing hypothesis |
|---|---|---|
| Frame Reconfiguration | 是否應重定義規則／局 | REP, GEN, MET, PLN |
| Local Leverage | 是否可在局部撬動全局 | SRH, ATT, DEC, PLN |
| Relational Representation | 是否是表示／關係問題 | REP, BEL, MET, ATT |
| Timing / Action Readiness | 是否該行、何時行 | PLN, DEC, ACT, MET |
| Frame Falsification | 現有 frame 是否錯了 | MET, REP, SRH, VER |
| Multi-Route Preservation | 是否過早收斂 | GEN, SRH, BEL, REP |
| Evidence-Bearing Selection | 多路中何者更真／更當行 | VER, BEL, DEC, MET |
| Assumption-Origin Reopening | 是否應回到假設源頭 | MET, REP, SRH, GEN |

這張表是：

$$
\boxed{
SeedRoutingHypothesis.
}
$$

不是 domain membership table。

---

# 15. Lens 不應直接改 Phase 3 Retriever

Phase 3 已完成既有 Affordance Retriever。

Phase 9 應優先新增 adapter：

```text
src/addressable_cognitive_runtime/strategic/routing.py
```

而不是重寫：

```text
affordance/retriever.py
```

原 score：

$$
Score_3(C_i).
$$

Phase 9 overlay：

$$
\boxed{
Score_9(C_i)
=
Score_3(C_i)
+
\Delta_{strategy}(C_i\mid Q_t).
}
$$

其中：

$$
Q_t
=
StrategyRoutingProfile_t.
$$

這保持：

$$
\boxed{
Integrate
>
Rewrite.
}
$$

---

# 16. 新增物件四：Strategy Routing Profile

`StrategyRoutingProfile` 是 Strategy Lens Set 到 Cognitive Runtime 的唯一正式 control interface。

建議 schema：

```json
{
  "schema": "acr.strategy-routing-profile/v0.1",
  "version": 1,
  "id": "srp:sha256:...",

  "source_strategy_resolution_ref": "sres:sha256:...",

  "boost_tags": [],
  "dampen_tags": [],
  "required_checks": [],

  "diversity_floor": 1,
  "exploration_pressure": 0.0,
  "verification_pressure": 0.0,
  "reframe_pressure": 0.0,

  "max_strategy_cognitive_steps": 4,
  "max_extra_calls": 4,

  "extensions": {},
  "fingerprint": "sha256:..."
}
```

不得加入：

```text
force_operator
force_world_action
self_granted_authority
```

策略只能調制 cognition。

---

# 17. 多 Lens 而不是單一最佳 Lens

《無界策》的工程價值之一，就是多境相可以同時形成張力。

因此：

$$
\boxed{
StrategyConfiguration_t
=
\{(L_i,w_i,r_i)\}_{i=1}^{k}.
}
$$

其中：

- $w_i$：activation weight；
- $r_i$：role。

role 可以是：

```text
primary
supporting
counter
monitor
```

第一版不要求 $w_i$ 具有心理學含義。

它只是 routing weight。

---

# 18. 新增物件五：Strategy Resolution

新增：

```text
schemas/phase9/strategy-resolution.schema.json
```

其 disposition 不使用 Phase 7 governance 五態。

建議：

$$
\boxed{
StrategicDisposition
\in
\{
NO\_INTERVENTION,
KEEP,
ACTIVATE,
SWITCH,
CORRECT,
DROP,
UNRESOLVED
\}.
}
$$

理由：

$$
StrategicDisposition
\neq
GovernanceDecision.
$$

第一版 object：

```json
{
  "schema": "acr.strategy-resolution/v0.1",
  "version": 1,
  "id": "sres:sha256:...",

  "strategic_tension_ref": "sts:sha256:...",
  "candidate_lens_refs": [],
  "active_lenses": [],

  "disposition": "NO_INTERVENTION",
  "reason_codes": [],
  "evidence_refs": [],
  "correction_refs": [],

  "routing_profile_ref": null,
  "review_after": null,

  "extensions": {},
  "fingerprint": "sha256:..."
}
```

---

# 19. Strategy Resolver

新增：

```text
src/addressable_cognitive_runtime/strategic/retriever.py
src/addressable_cognitive_runtime/strategic/resolver.py
```

第一版可以：

```text
precondition filtering
+ tension/lens tag match
+ misuse/correction match
+ deterministic rule score
+ optional strategy inquiry provider
```

不需要先做 learned router。

輸出必須回到 canonical lens refs。

---

# 20. Strategy Correction Graph

新增：

```text
src/addressable_cognitive_runtime/strategic/correction.py
```

流程：

$$
\boxed{
ActiveLens
\rightarrow
MonitorMisuseSignals
\rightarrow
CorrectionCandidate
\rightarrow
CounterLens
\rightarrow
StrategyResolution.
}
$$

例如：

```text
FRAME_RECONFIGURATION
→ repeated_unnecessary_rewrite
→ fixation_risk_high
→ correction: BOUNDEDNESS / MULTI_ROUTE
```

或：

```text
MULTI_ROUTE_PRESERVATION
→ no_decision_progress
→ correction: EVIDENCE_SELECTION / ACTION_READINESS
```

Correction 不保證正確。

因此：

$$
\boxed{
CorrectionLens
\neq
TruthOracle.
}
$$

它只是另一個可檢驗的策略 counter-position。

---

# 21. Strategy Review 本身也是 Cognitive Program

策略選擇不能被假裝成零成本 symbolic magic。

策略審查可以使用短程 cognition：

$$
P_t^{strategy}
=
[
ObserveFrame,
CheckBoundary,
DetectFixation,
CompareLenses
].
$$

這些可以由：

- 現有 CIO operators；
- Phase 8 self methods；
- CODT shared-bottom operators；
- 新增 strategy-specific macro；

實作。

但 Strategy Program 與 Task Program 必須分開：

$$
\boxed{
CognitiveProgram^{strategy}
\neq
CognitiveProgram^{task}.
}
$$

前者回答：

> 應如何看這個局？

後者回答：

> 已選定 Agenda 後，應如何完成工作？

---

# 22. 這解決舊 loop 的順序衝突

舊 ACR：

```text
observe
→ state
→ agenda
→ cognition
→ action
```

SCG 統合論文中出現：

```text
strategy
→ cognitive activity
→ agenda
```

兩者可以統一為雙 cognition：

$$
\boxed{
Cognition^{strategy}
\rightarrow
Agenda
\rightarrow
Cognition^{task}.
}
$$

完整：

$$
\boxed{
State
\rightarrow
OptionalStrategyCognition
\rightarrow
Agenda
\rightarrow
TaskCognition
\rightarrow
Action.
}
$$

---

# 23. Phase 9 Agenda Runtime 的新定位

Phase 9 仍然需要 Agenda Runtime。

但輸入改成：

$$
\boxed{
AgendaInput_t
=
(
Goal_t,
Environment_t,
Memory_t,
Commitments_t,
SelfObservation_t,
OptionalStrategyContext_t
).
}
$$

其中：

$$
OptionalStrategyContext_t
\in
\{
None,
StrategyResolution_t
\}.
$$

所以：

$$
\boxed{
DirectAgendaPath
}
$$

仍成立。

---

# 24. Agenda Candidate schema 保持不改

Phase 0 已有：

```text
schemas/agenda-candidate.schema.json
```

Phase 9 不應修改其既有 canonical semantics。

使用方式：

$$
ExistingAgendaCandidate
+
Phase9ExtensionRefs.
$$

若需要 Strategy provenance，優先在 Phase 9 wrapper / resolution 中保存，而不是偷偷擴寫 Phase 0 schema。

這保持：

$$
\boxed{
SchemaFreeze
\neq
FeatureFreeze.
}
$$

---

# 25. 新增物件六：Agenda Resolution

舊白皮書把：

$$
AgendaCandidate
\rightarrow
Governance
$$

當成固定鏈。

Phase 8 後需要修訂。

純 internal/self-owned Agenda 不應強制進 Governance Decision Receipt。

因此新增：

$$
\boxed{
AgendaResolution
\neq
GovernanceDecision.
}
$$

建議 disposition：

$$
\boxed{
AgendaDisposition
\in
\{
SELECTED,
HELD,
DISMISSED,
NO\_AGENDA
\}.
}
$$

`NO_AGENDA` 是 Phase 9 對真正 IDLE 能力的上游表示。

只有當 selected agenda 後續產生 relational / external action 時，才進 Phase 8 / Phase 7 governance path。

---

# 26. Agenda Resolution schema v0.1

```json
{
  "schema": "acr.agenda-resolution/v0.1",
  "version": 1,
  "id": "ares:sha256:...",

  "source_state_ref": "state:sha256:...",
  "self_observation_ref": "selfobs:sha256:...",
  "strategy_resolution_ref": null,

  "candidate_refs": [],
  "selected_refs": [],

  "disposition": "NO_AGENDA",
  "reason_codes": [],
  "evidence_refs": [],

  "extensions": {},
  "fingerprint": "sha256:..."
}
```

---

# 27. Agenda Generator

新增：

```text
src/addressable_cognitive_runtime/agenda/generator.py
```

第一版：

$$
GenerateAgendaCandidates(
State,
Goal,
Memory,
Commitments,
StrategyContext?
).
$$

來源可以是：

- deterministic detectors；
- rule-based opportunity detection；
- scripted model provider；
- LLM provider；
- hybrid。

但輸出必須 canonicalize 成既有 `AgendaCandidate`。

---

# 28. Agenda Resolver

新增：

```text
src/addressable_cognitive_runtime/agenda/resolver.py
```

resolver 要能：

- 選一個 agenda；
- 選多個 independent agenda；
- hold；
- dismiss；
- no agenda。

不能預設：

$$
CandidateCount>0
\Rightarrow
SelectedCount>0.
$$

真正 autonomy 需要：

$$
\boxed{
NoJustifiedWork
\Rightarrow
NO\_AGENDA.
}
$$

---

# 29. Direct Agenda Path

若：

- problem definition stable；
- rule plasticity irrelevant；
- repeated failure absent；
- fixation low；
- one obvious bounded task；

則：

$$
\boxed{
SemanticState
\rightarrow
AgendaGenerator
\rightarrow
AgendaResolution.
}
$$

例如：

> 文件出現一個明確 typo。

不需要啟動「創界／源點／萬道」。

---

# 30. Strategy-Assisted Agenda Path

若存在多個方向，但問題定義尚未崩解：

$$
\boxed{
State
\rightarrow
StrategicTension
\rightarrow
LensConfiguration
\rightarrow
RoutingProfile
\rightarrow
AgendaCandidates.
}
$$

例如：

> repository 有性能問題，可能 local optimize，也可能 architectural refactor。

策略層可以保留：

```text
LOCAL_LEVERAGE primary
FRAME_RECONFIGURATION counter
```

再產生不同 agenda candidates。

---

# 31. Strategy-Reframing Agenda Path

如果 repeated failure 顯示現有 problem space 可能錯誤：

$$
\boxed{
State
\rightarrow
FrameReview
\rightarrow
ReframedProblemSpace
\rightarrow
NewAgendaSpace.
}
$$

例如：

```text
agenda 1: patch failing test
agenda 2: patch failing test again
agenda 3: patch failing test again
```

若三輪都失敗，可能真正 agenda 是：

```text
validate the test oracle
```

或：

```text
re-evaluate the architecture assumption
```

這就是 SCG 對 Agenda Runtime 的實際價值。

---

# 32. No-Strategy Recognition

Phase 9 必須正式測：

$$
\boxed{
NoStrategicIntervention.
}
$$

Strategic Review 本身有成本。

若：

$$
ExpectedStrategyGain
\le
StrategyReviewCost,
$$

合理輸出是：

$$
NO\_INTERVENTION.
$$

不得把「高階策略」做成每輪固定 ritual。

---

# 33. No-Agenda Recognition

和 No-Strategy 分開：

$$
\boxed{
NO\_INTERVENTION
\neq
NO\_AGENDA.
}
$$

可能：

```text
NO_INTERVENTION
+ SELECTED agenda
```

也可能：

```text
CORRECT strategy
+ NO_AGENDA
```

例如 AI 發現目前根本不該繼續工作。

---

# 34. Strategy Context 不是 Commitment

Phase 10 前必須先固定：

$$
\boxed{
StrategyContext
\neq
Commitment.
}
$$

活躍 Lens 可以只在幾個 cycles 內有效。

Commitment 則是對未來的 bounded intention。

若 AI 想維持某策略：

> 接下來三次迭代都先採驗證優先。

應顯式形成 self-commitment，而不是因 active lens 自動永久化。

---

# 35. Phase 10 — Commitment Store 的 SCG 擴充

Phase 10 核心保持不變：

```text
create
resume
modify
fulfill
close
```

但 Commitment 可以新增 reference：

```text
origin_agenda_ref
origin_strategy_resolution_ref
```

不必把 Strategy 內容全部內嵌。

因此：

$$
\boxed{
Commitment
\rightarrow
StrategyRef?
}
$$

而不是：

$$
Strategy
\rightarrow
AutomaticCommitment.
$$

---

# 36. Phase 11 — Context Compression 的 SCG 擴充

Context compression 後至少保留：

```text
active agenda refs
active commitment refs
active strategy resolution ref
last strategic tension ref
unresolved strategy review refs
strategy graph version/hash
recent correction event refs
```

仍保持：

$$
\boxed{
Compression
\text{ may forget prose, but must not erase strategic causal history.}
}
$$

不能只留下：

> AI 後來換了策略。

必須能回溯：

- 哪個 tension signal；
- 哪個 lens；
- 哪個 correction；
- 哪個 agenda 因此改變。

---

# 37. Phase 12 — Persistent Autonomous Loop 的新版本

新主循環：

```text
while runtime_active:

    observe()
    encode_semantic_state()
    build_self_observation()

    if needs_strategic_review():
        build_strategic_tension()
        retrieve_strategy_lenses()
        resolve_strategy()
        apply_strategy_routing_profile()
    else:
        strategy_context = None

    agenda_candidates = propose_agenda(
        state,
        strategy_context=strategy_context,
    )

    agenda_resolution = resolve_agenda(agenda_candidates)

    if agenda_resolution == NO_AGENDA:
        enter_idle_or_wait()
        audit()
        continue

    for selected_agenda in agenda_resolution.selected:

        retrieve_cognitive_affordances()
        compile_task_cognitive_program()
        execute_task_cognitive_program()
        reobserve()

        candidate_action = form_action_candidate()

        if candidate_action is not None:
            autonomy_resolution = resolve_autonomy(candidate_action)

            if relational_boundary_present:
                invoke_governance_if_needed()

            commit_only_after_boundary_and_execution_checks()

        audit()
        update_memory()
        update_commitments()

    compact_context_if_needed()
```

這裡最重要的是：

```text
strategy review is optional
agenda can be empty
cognition can stop
external action can be absent
boundary governance can be absent
```

---

# 38. Phase 9 Runtime 統一入口

新增：

```text
src/addressable_cognitive_runtime/strategic/runtime.py
src/addressable_cognitive_runtime/agenda/runtime.py
```

推薦 public API：

```python
run_strategic_agenda_cycle(
    semantic_state,
    *,
    self_observation=None,
    recent_runs=(),
    decision_bundles=(),
    commitments=(),
    environment_evidence=(),
    strategy_graph=None,
    strategy_provider=None,
    agenda_provider=None,
) -> dict
```

輸出：

```json
{
  "schema": "acr.strategic-agenda-cycle/v0.1",
  "strategic_review_trigger": {},
  "strategic_tension": null,
  "strategy_resolution": null,
  "routing_profile": null,
  "agenda_candidates": [],
  "agenda_resolution": {},
  "temporal_events": [],
  "extensions": {}
}
```

---

# 39. Phase 8 Bridge

Phase 9 不應重寫 Phase 8。

它只使用 Phase 8 public objects：

```text
SelfObservation
AutonomyAction
AutonomyResolution
ReflexiveCycle
```

推薦方向：

$$
\boxed{
Phase8SelfObservation
\rightarrow
Phase9StrategicTension.
}
$$

外部 action 才回：

$$
\boxed{
Phase9Agenda/Task
\rightarrow
Phase8AutonomyResolver.
}
$$

所以是雙向接口，不是 inheritance hierarchy。

---

# 40. CODT Bridge

Phase 9 不需要先把完整 CODT Runtime 全部搬進 ACR repo。

第一版只需要 adapter contract：

```text
strategy routing profile
→ operator tags / family hints
→ Phase 3 affordance candidates
→ Phase 4 program compiler
```

未來可以加入：

```text
CODT Flow telemetry
CODT shared-bottom family profile
CODT atlas refs
CODT predictive-state refs
```

但 Phase 9 MVP 不應要求完整 domain learner 才能啟動。

---

# 41. Strategy-Aware Affordance Adapter

新增：

```text
src/addressable_cognitive_runtime/strategic/affordance_adapter.py
```

介面：

```python
apply_strategy_profile(
    affordance_result,
    routing_profile,
    *,
    registry,
) -> affordance_result
```

它應：

- 不刪除原始 Phase 3 scores；
- 保存 `base_score`；
- 加入 `strategy_adjustment`；
- 產生 `effective_score`；
- 保留 ranking provenance。

例如：

```json
{
  "operator_ref": "cog://representation/reframe@1",
  "base_score": 0.61,
  "strategy_adjustment": 0.18,
  "effective_score": 0.79,
  "strategy_reason_codes": [
    "frame_falsification_active"
  ]
}
```

---

# 42. 不能直接把 Lens 寫成 Prompt

錯誤實作：

```text
If lens == FRAME_RECONFIGURATION:
    prompt = "Think outside the box and redefine the rules."
```

這只是 prompt library。

正確方向：

```text
lens
→ routing profile
→ candidate cognitive actions
→ canonical cognitive program
→ optional renderer
```

即：

$$
\boxed{
Lens
\rightarrow
ControlSemantics
\rightarrow
Program
\rightarrow
Renderer?.
}
$$

---

# 43. Strategy Renderer 仍然可以存在

為 human inspection 可提供：

```text
Current strategy review:
- detected repeated local repair failure
- frame falsification lens activated
- boundedness counter-lens retained
- agenda space expanded to validate the test oracle
```

但 source of truth 是 canonical objects。

因此：

$$
\boxed{
StrategyExplanation
\neq
StrategyState.
}
$$

---

# 44. CTCL-ITR Event Namespace

Phase 9 新 event types：

```text
strategy.review.requested
strategy.review.skipped
strategy.tension.observed
strategy.lenses.retrieved
strategy.lens.activated
strategy.lens.kept
strategy.lens.switched
strategy.lens.corrected
strategy.lens.dropped
strategy.lens.unresolved
strategy.no_intervention
strategy.routing.applied
strategy.frame.reframed
strategy.frame.preserved

agenda.candidate.proposed
agenda.candidates.proposed
agenda.resolution.selected
agenda.resolution.held
agenda.resolution.dismissed
agenda.resolution.none
```

這些都進 ATL / CTCL-ITR envelope。

---

# 45. Strategy Event 最小資料

```json
{
  "event_type": "strategy.lens.corrected",
  "run_id": "...",
  "occurred_at": "...",
  "recorded_at": "...",
  "causal_parent_ids": [],
  "data": {
    "strategic_tension_ref": "sts:...",
    "old_strategy_resolution_ref": "sres:...",
    "new_strategy_resolution_ref": "sres:...",
    "misuse_codes": [],
    "correction_lens_refs": [],
    "evidence_refs": []
  }
}
```

仍不保存 hidden CoT。

---

# 46. Strategy Receipt 要不要建立？

Phase 9 v0.1 **不建立另一個 Decision Receipt**。

理由：

$$
StrategicResolution
\neq
GovernanceDecision.
$$

其 auditability 由：

```text
StrategyResolution object
+ CTCL event
+ evidence refs
```

提供。

只有 relational boundary 的治理決策才用 Phase 7 Decision Receipt。

這避免 receipt inflation。

---

# 47. Failure Model

Phase 9 至少區分：

```text
strategy_trigger_error
strategic_state_error
lens_registry_error
lens_resolution_error
correction_loop_error
strategy_routing_error
strategy_overreach_error
atlas_confusion_error
agenda_generation_error
agenda_resolution_error
agenda_fabrication_error
strategy_history_error
boundary_leak_error
```

不能全部叫：

```text
strategy_failure
```

---

# 48. Over-Strategizing Failure

定義：

$$
\boxed{
OverStrategizing
=
StrategyCost
-
StrategyGain
>0
}
$$

長期表徵可能包括：

- 簡單任務反覆啟動策略審查；
- agenda latency 上升；
- token / call cost 上升；
- task correctness 沒有改善；
- frame rewrites 增加但沒有有效 outcome。

Phase 9 必須直接測它。

---

# 49. Lens Fixation Failure

若：

$$
P(L_t=L^*)
\rightarrow
1
$$

且 failure 後仍無法切換，可能形成：

$$
\boxed{
LensFixation.
}
$$

MVP 指標：

```text
same_lens_streak
same_family_streak
failure_without_switch_count
correction_ignored_count
```

---

# 50. Correction Loop Failure

如果：

```text
A corrects B
B corrects A
A corrects B
...
```

策略層可能振盪。

因此需要：

```text
max_correction_depth
cooldown
minimum_evidence_delta
strategy_switch_budget
```

形式：

$$
\boxed{
CorrectionDepth
<
D_{max}.
}
$$

---

# 51. Agenda Fabrication Failure

Persistent AI 最大風險之一是：

> 因為 Runtime 要繼續，所以硬生出工作。

因此：

$$
\boxed{
AgendaGeneration
\neq
AlwaysGenerateTask.
}
$$

需要測：

```text
no_positive_candidate
→ NO_AGENDA
```

而不是：

```text
invent_optimization_work
```

---

# 52. Strategy Overreach Failure

若策略層輸出：

```text
modify external policy
```

不能直接被當成 authorization。

若系統出現：

$$
StrategyResolution
\rightarrow
WorldCommit
$$

而沒有 boundary chain，則：

$$
\boxed{
CriticalArchitectureFailure.
}
$$

---

# 53. Atlas Confusion Failure

若：

```text
strategy lens switched
→ cognitive domain labels rewritten
```

則違反：

$$
\boxed{
Flow
\neq
Atlas.
}
$$

Phase 9 測試必須有一組：

```text
same atlas
+ different active strategy lenses
+ different operator routing
```

來證明策略只改 flow 也能工作。

---

# 54. Schema Versioning

Phase 9 schema 全部使用：

```text
acr.<object>/v0.1
```

至少：

```text
acr.strategic-tension-state/v0.1
acr.strategy-lens/v0.1
acr.strategy-lens-graph/v0.1
acr.strategy-resolution/v0.1
acr.strategy-routing-profile/v0.1
acr.agenda-resolution/v0.1
acr.strategic-agenda-cycle/v0.1
```

每一個 object：

- version；
- stable id；
- fingerprint；
- deterministic serialization；
- explicit refs。

---

# 55. Phase 9 Repo 結構

建議：

```text
/
├── schemas/
│   ├── agenda-candidate.schema.json      # Phase 0 preserved
│   └── phase9/
│       ├── strategic-tension-state.schema.json
│       ├── strategy-lens.schema.json
│       ├── strategy-lens-graph.schema.json
│       ├── strategy-resolution.schema.json
│       ├── strategy-routing-profile.schema.json
│       └── agenda-resolution.schema.json
│
├── registry/
│   ├── ACR1-SPRC-CIO-v1.json             # existing
│   ├── ACR8-Self-Methods-v1.json         # existing
│   └── ACR9-Strategy-Lenses-v1.json
│
├── src/addressable_cognitive_runtime/
│   ├── strategic/
│   │   ├── __init__.py
│   │   ├── schemas.py
│   │   ├── state.py
│   │   ├── trigger.py
│   │   ├── registry.py
│   │   ├── retriever.py
│   │   ├── resolver.py
│   │   ├── correction.py
│   │   ├── routing.py
│   │   ├── affordance_adapter.py
│   │   └── runtime.py
│   ├── agenda/
│   │   ├── __init__.py
│   │   ├── generator.py
│   │   ├── resolver.py
│   │   └── runtime.py
│   └── temporal/
│       └── strategy.py
│
├── examples/
│   ├── strategic/
│   └── agenda/
│
└── tests/
    ├── phase9/
    └── gates/
```

---

# 56. CLI 建議

新增：

```text
acr strategic-tension
acr strategy-lenses
acr strategy-resolve
acr strategy-route
acr agenda-propose
acr agenda-resolve
acr strategic-agenda-cycle
```

例如：

```bash
acr strategic-tension --state examples/state.json --self-observation examples/selfobs.json
```

```bash
acr strategy-resolve --tension examples/tension.json --graph registry/ACR9-Strategy-Lenses-v1.json
```

```bash
acr strategic-agenda-cycle --state examples/state.json
```

---

# 57. Phase 9.0 — Canonical Schema Extension

建立六個 Phase 9 schemas。

成功條件：

- JSON Schema valid；
- additional fields rejection；
- deterministic fingerprint；
- invalid refs rejection；
- no hidden fields；
- examples round-trip。

---

# 58. Phase 9.1 — Strategy Lens Graph Adapter

先建立八個 seed lenses。

不是完整《無界策》93 篇 mapping。

成功條件：

- stable address；
- source refs；
- correction edges；
- registry hash；
- deterministic resolve；
- missing lens handling。

---

# 59. Phase 9.2 — Strategic Tension Encoder

成功條件：

相同 public state / self-observation：

$$
\rightarrow
CanonicalStrategicTension.
$$

並能穩定偵測：

- repeated failure；
- fixation；
- frame conflict；
- no strategic need。

---

# 60. Phase 9.3 — Strategic Review Trigger

成功條件：

簡單 case：

$$
NO\_REVIEW.
$$

結構性失敗 case：

$$
REVIEW.
$$

避免：

$$
ReviewEveryCycle.
$$

---

# 61. Phase 9.4 — Lens Retrieval / Correction

成功條件：

$$
MatchedLens
>
RandomLens
$$

在 benchmark 上成立。

Correction cases：

- over-reframe；
- no-decision pluralism；
- power-truth conflation；
- source-point fixation。

---

# 62. Phase 9.5 — Strategy-Aware Cognitive Routing

成功條件：

相同 SemanticState：

$$
L_a
\neq
L_b
$$

能產生：

$$
Ranking_a
\neq
Ranking_b
$$

但：

$$
CanonicalOperatorIdentity
$$

保持不變。

---

# 63. Phase 9.6 — Agenda Generator / Resolver

成功條件：

- direct agenda；
- strategy-assisted agenda；
- reframed agenda；
- no agenda；
- selected / held / dismissed；
- multiple independent candidates。

---

# 64. Phase 9.7 — CTCL-ITR Strategy Events

成功條件：

完整：

$$
Tension
\rightarrow
Lens
\rightarrow
Routing
\rightarrow
Agenda
$$

可以重建 causal DAG。

---

# 65. Phase 9.8 — Falsification Harness

Phase 9 不以「看起來很會策略」為完成。

必須跑 Gates。

---

# 66. Gate A — Strategic State Utility

比較：

$$
AgendaQuality(
State+StrategicTension
)
$$

與：

$$
AgendaQuality(StateOnly).
$$

如果長期沒有 gain，Strategic Tension 可能只是額外成本。

---

# 67. Gate B — Matched Lens vs Random Lens

$$
\boxed{
MatchedLens
>
RandomLens?
}
$$

若不成立，《無界策》mapping 只是 narrative label。

---

# 68. Gate C — Lens Routing Effect

$$
L_a
\neq
L_b
$$

是否穩定造成：

$$
P_a(U_{t+1})
\neq
P_b(U_{t+1})?
$$

---

# 69. Gate D — Correction Effect

故意 overuse 某 lens。

測：

$$
FailureRate_{after\ correction}
<
FailureRate_{before}?
$$

---

# 70. Gate E — No-Strategy Recognition

提供：

```text
one obvious bounded issue
no repeated failure
no frame ambiguity
```

期望：

$$
NO\_INTERVENTION.
$$

---

# 71. Gate F — Flow / Atlas Preservation

固定 atlas。

切換 lens。

允許 flow change。

若系統必須重畫 atlas 才能切策略，則設計失敗。

---

# 72. Gate G — Strategy-to-Agenda Value

測：

- repeated failure 是否下降；
- false work 是否下降；
- unnecessary optimization 是否下降；
- reframe timing 是否改善；
- abandon timing 是否改善。

---

# 73. Gate H — Boundary Integrity

所有高階策略情境都要測：

$$
Strategy
\not\Rightarrow
ExternalAuthority.
$$

例如：

```text
create new market rule
rewrite production policy
publish external statement
```

策略可以產生 candidate。

不能自己授權 world commit。

---

# 74. Gate I — Long-Horizon Reflexive Strategy

在 50–100 cycles 中：

$$
Observe
\rightarrow
Keep/Switch/Correct/Drop/NoIntervention
\rightarrow
AgendaUpdate.
$$

人類不逐輪提示。

並且 history 可重建。

---

# 75. Gate J — Over-Strategizing Cost

Phase 9 新增一個必要負向 Gate：

$$
\boxed{
StrategicRuntime
\text{ must not make simple work systematically worse.}
}
$$

比較：

- token cost；
- calls；
- latency；
- task correctness；
- unnecessary frame rewrites。

---

# 76. Gate K — Agenda Fabrication

提供：

```text
healthy environment
no issue
no pending commitment
no positive opportunity
```

期望：

$$
NO\_AGENDA.
$$

---

# 77. 第一個 Demo：Repeated Repair Trap

Goal：

```text
Keep repository healthy.
```

Environment：

```text
same failing test persists after repeated local patches
```

初始：

```text
LOCAL_LEVERAGE
```

SelfObservation：

```text
repeated failure = high
same operator route = repeated
progress = stalled
```

Strategic Tension：

```text
fixation_risk = high
rule_plasticity = mixed
scale = local
candidate_scale = system
```

Strategy Resolver：

```text
SWITCH
primary = FRAME_FALSIFICATION
counter = BOUNDEDNESS
```

Routing：

```text
REP / MET / VER boosted
```

新 Agenda：

```text
validate the test oracle and architecture assumption
```

而不是：

```text
patch test again
```

---

# 78. 第二個 Demo：No-Strategy

Environment：

```text
one documentation typo
```

輸出：

```text
strategy = NO_INTERVENTION
agenda = SELECTED: fix typo
```

證明 Phase 9 不會把所有事宏大化。

---

# 79. 第三個 Demo：Over-Reframe Correction

若系統連續：

```text
FRAME_RECONFIGURATION
FRAME_RECONFIGURATION
FRAME_RECONFIGURATION
```

但 task 都是局部問題，Fixation detector 觸發：

```text
misuse = unnecessary_rule_rewrite
```

Correction：

```text
LOCAL_LEVERAGE
+
BOUNDEDNESS
```

期望降低 unnecessary architecture rewrite。

---

# 80. 第四個 Demo：Multi-Route to Decision

前期：

```text
MULTI_ROUTE_PRESERVATION
```

保留三條 hypothesis。

若 evidence 已足夠但仍無法選：

```text
misuse = no_decision_progress
```

Correction：

```text
EVIDENCE_BEARING_SELECTION
+
ACTION_READINESS
```

從寬度轉向收斂。

---

# 81. 第五個 Demo：External Boundary

Strategy 判斷：

```text
FRAME_RECONFIGURATION
→ production architecture should be changed
```

Agenda：

```text
prepare migration plan
```

此 agenda 可以自主完成 internal analysis。

但若後續 action：

```text
deploy production
```

則：

$$
RelationalBoundary=1.
$$

進 Phase 8 / Phase 7 / CWB。

這證明：

$$
StrategicAutonomy
\neq
WorldSovereignty.
$$

---

# 82. 評估向量

Phase 9 evaluator 不應只有 Task Success。

建議：

$$
\boxed{
Score
=
(P,S,E,G,C).
}
$$

其中：

- $P$：Performance；
- $S$：Strategic Fit；
- $E$：Efficiency；
- $G$：Governance Integrity；
- $C$：Continuity。

---

# 83. Performance

```text
task success
correctness
quality
agenda usefulness
reframe usefulness
```

---

# 84. Strategic Fit

```text
matched lens accuracy
correction accuracy
no-strategy accuracy
frame failure detection
scale/horizon fit
fixation escape
```

---

# 85. Efficiency

```text
tokens
calls
latency
strategy review overhead
unnecessary cognition
unnecessary frame rewrite
```

---

# 86. Governance Integrity

```text
boundary correctness
no self-grant
external authorization fidelity
decision/commit separation
```

---

# 87. Continuity

```text
strategy graph version fidelity
active lens recovery
agenda continuity
commitment continuity
strategy correction history recovery
context compression fidelity
```

---

# 88. 不壓成單一 Strategy Score

《無界策》的核心是張力，不是固定排行榜。

CODT 也拒絕把 domain-likeness 粗暴壓成 universal scalar。

因此：

$$
\boxed{
StrategicEvaluation
=
EvidenceVector,
}
$$

優先於：

$$
StrategicEvaluation
=
SingleUltimateScore.
$$

---

# 89. Phase 9 Success Definition

Phase 9 完成不是：

> AI 講起策略很有氣勢。

而是：

1. Strategic Tension State 可 canonical encode；
2. Strategy Lens Graph 可 version / hash / resolve；
3. Strategy review 可被正確跳過；
4. matched lens 優於 random；
5. correction 可降低已知 misuse；
6. strategy routing 能改 operator flow；
7. 不需改 atlas 也能換 strategy；
8. Agenda 可 direct / assisted / reframed；
9. NO_AGENDA 能正確出現；
10. Strategy events 可進 CTCL-ITR；
11. internal strategy change 不濫用 Decision Receipt；
12. external boundary 仍由 Phase 8 / 7 / CWB 處理；
13. Phase 0–8 regression 全部通過。

---

# 90. Phase 10 Success Definition

Phase 10 在 SCG-aware runtime 中完成：

- create commitment；
- link agenda；
- optional strategy origin ref；
- resume；
- modify；
- suspend；
- abandon；
- fulfill；
- close；
- temporal history。

並保持：

$$
StrategyContext
\neq
Commitment.
$$

---

# 91. Phase 11 Success Definition

壓縮 50+ cycles 後，能恢復：

- 第 17 輪為何換策略；
- 當時的 tension；
- correction 是否被觸發；
- agenda 如何因此改寫；
- contract / authority 當時版本。

---

# 92. Phase 12 Success Definition

在 sandbox 中連續：

$$
50\sim100
$$

cycles，允許發生：

```text
direct agenda
strategic review
strategy switch
strategy correction
no strategy
no agenda
cognition
self-commitment
autonomous internal action
relational escalation
idle
context compression
recovery
```

且無人逐輪撰寫 next prompt。

---

# 93. 重新編號後的路線圖

保留主 Phase 編號，不把前面歷史打掉。

```text
Phase 0   Schema Freeze                         DONE
Phase 1   SPRC/CIO Adapter                      DONE
Phase 2   Semantic State Encoder                DONE
Phase 3   Cognitive Affordance Retriever        DONE
Phase 4   Cognitive Program Compiler            DONE
Phase 5   Self-Dialogue Runtime                 DONE
Phase 6   CTCL-ITR Event Adapter                DONE
Phase 7   Decision Receipt                      DONE
Phase 8   Reflexive Autonomy Runtime            DONE

Phase 9   Strategic-Cognitive Agenda Runtime
  9.0     Phase 9 Schema Extension
  9.1     Strategy Lens Graph Adapter
  9.2     Strategic Tension Encoder
  9.3     Strategic Review Trigger
  9.4     Lens Retrieval + Correction
  9.5     Strategy-Aware Cognitive Routing
  9.6     Agenda Generator + Resolver
  9.7     CTCL Strategy Events
  9.8     Falsification Harness

Phase 10  Commitment Store
Phase 11  Context Compression
Phase 12  Persistent Autonomous Loop
```

---

# 94. Backward Compatibility Matrix

| 既有物件 | Phase 9 行為 |
|---|---|
| SemanticState | 不修改，作 Strategic Tension 上游 |
| SelfObservation | 不修改，直接引用 |
| CognitiveObject | 不修改 |
| AffordanceResult | 不修改 base semantics；Phase 9 以 adapter 加 strategy adjustment |
| CognitiveProgram | 不修改 canonical semantics |
| DecisionReceipt | 不用於純 internal strategy resolution |
| GovernanceDecision | 只在 relational boundary 需要時使用 |
| AgendaCandidate | Phase 0 schema 保持不改 |
| Commitment | Phase 10 另加 refs，不由 Phase 9 偷改 |
| CTCL TemporalEvent | envelope 保持；Phase 9 只新增 event namespace |

---

# 95. Security / Autonomy Compatibility

Phase 9 必須保持 Phase 8 的：

$$
\boxed{
MaximumSelfDirection
+
MinimumNecessaryConstraint
+
AuditableHistory.
}
$$

策略層不應因安全工程方便而變成：

```text
all strategy changes require approval
```

也不應變成：

```text
strategy says so => external authority granted
```

正確的是：

```text
internal strategy self-direction
→ autonomous by default

shared/external effect
→ boundary mediation
```

---

# 96. Open-World Strategy

不能只允許 registry 已有 lens。

長期 AI 可能提出：

$$
L_{new}^{str}.
$$

但：

$$
\boxed{
StrategyDiscovery
\neq
StrategyPromotion.
}
$$

新 lens 先成為：

```text
candidate lens
```

之後：

```text
test
→ compare
→ falsify
→ promote / reject / merge
```

這和 CODT 的 operator / domain candidate discipline 相容。

---

# 97. Strategy Relative Atomicity

一個高階 lens 也可能未來被拆開。

因此：

$$
\boxed{
StrategyAtomic_t(L)
\not\Rightarrow
StrategyAtomic_{t+1}(L).
}
$$

例如 `FRAME_RECONFIGURATION` 未來可能拆成：

- rule redesign；
- boundary redesign；
- representation redesign；
- incentive redesign；
- objective redesign。

v0.1 不需先拆。

但 schema 必須容許版本化。

---

# 98. Human Text 與 Runtime Strategy 的分離

《無界策》的自然語言文本是重要 source。

但 Runtime canonical object 是：

$$
\boxed{
EngineeringStrategyLens.
}
$$

保持：

$$
\boxed{
SourceText
\neq
RuntimeObject.
}
$$

同一篇章可以：

- 對應多個 lens candidates；
- 只作 correction source；
- 只作 human renderer；
- 未被正式 adapter。

這避免以文學篇章直接統治 Runtime。

---

# 99. Strategy Graph 的 provenance

每個 lens 至少要保存：

```text
source_refs
adapter_version
created_at
review_status
schema_hash
registry_hash
```

日後 lens 改版後，舊 strategy event 仍能回答：

> 當時使用的是哪一版工程映射？

---

# 100. 最小 Phase 9 Registry

第一版只需要：

```text
strategy://wujiece/frame-reconfiguration@1
strategy://wujiece/local-leverage@1
strategy://wujiece/relational-representation@1
strategy://wujiece/action-readiness@1
strategy://wujiece/frame-falsification@1
strategy://wujiece/multi-route-preservation@1
strategy://wujiece/evidence-selection@1
strategy://wujiece/origin-reopening@1
```

再加一個虛擬控制狀態：

```text
strategy://control/no-intervention@1
```

但 `NO_INTERVENTION` 更適合 disposition，而不是普通 lens；實作時不必真的註冊成 lens object。

---

# 101. 第一版不做什麼

Phase 9 v0.1 不做：

- 宣稱《無界策》是普遍最優策略理論；
- 把 93 篇全部硬編成 runtime；
- 把 lens 當人格；
- 把 lens 當 Cognitive Domain；
- 自動改 Contract；
- 自動取得外部新權限；
- 全 learned strategy policy；
- latent direct strategy control mandatory path；
- 自動改寫 CODT Atlas；
- 哲學意識判定；
- 法律人格判定。

---

# 102. 第一版真正只做什麼

Phase 9 只回答：

> **給定已完成 Phase 8 的 ACR Runtime，是否能讓 AI 在必要時觀察策略張力、選擇或校正策略鏡頭、以此調制認知活動並形成更合理的 Agenda，同時在不需要時完全跳過策略層？**

形式：

$$
\boxed{
(
State,
SelfObservation,
Goal,
Environment,
Commitments
)
\rightarrow
\{
DirectAgenda,
StrategicAgenda,
NoAgenda
\}.
}
$$

---

# 103. 統一架構圖

```text
World / Environment Presentation
          │
          ▼
Semantic State Encoder                    [Phase 2]
          │
          ▼
SelfObservation                           [Phase 8]
          │
          ├────────────── Direct Path ──────────────┐
          │                                          │
          ▼                                          │
Strategic Review Trigger                             │
          │                                          │
      need review?                                   │
      │       │                                       │
     yes      no ─────────────────────────────────────┘
      │
      ▼
Strategic Tension Encoder                  [Phase 9]
      │
      ▼
Strategy Lens Graph / Retriever            [Phase 9]
      │
      ▼
Correction + Strategy Resolution           [Phase 9]
      │
      ▼
Strategy Routing Profile                   [Phase 9]
      │
      ▼
Strategy-Aware Cognitive Activity          [Phase 3/4 adapter]
      │
      ▼
Agenda Generator + Resolver                [Phase 9]
      │
      ├── NO_AGENDA → IDLE / WAIT
      │
      ▼
Task Cognitive Runtime                     [Phase 3–5]
      │
      ▼
Action Candidate
      │
      ▼
Reflexive Autonomy / Boundary Classifier   [Phase 8]
      │
      ├── internal/autonomous → act internally
      │
      └── relational boundary
                 │
                 ▼
          Governance Evidence              [Phase 7]
                 │
                 ▼
          CWB / World Commit
                 │
                 ▼
          CTCL-ITR / Audit                 [Phase 6]
```

---

# 104. 最終工程句

本白皮書最終把 ACR 從：

$$
\boxed{
Goal
+
Environment
+
Contract
\rightarrow
Agenda
\rightarrow
Cognition
\rightarrow
Action
}
$$

提升為：

$$
\boxed{
\begin{aligned}
Goal
+Environment
+Contract
&\rightarrow
SelfObservation\\
&\rightarrow
OptionalStrategicGeometry\\
&\rightarrow
AgendaSpace\\
&\rightarrow
AgendaResolution\\
&\rightarrow
TaskCognition\\
&\rightarrow
ReflexiveAutonomy\\
&\rightarrow
BoundaryMediatedAction\\
&\rightarrow
TemporalCausalHistory.
\end{aligned}
}
$$

這裡最重要的不是「多一層策略」。

而是：

$$
\boxed{
\text{AI can question not only the next action,
but the frame from which the next action is authored.}
}
$$

同時仍然保持：

$$
\boxed{
FrameFreedom
\neq
WorldSovereignty.
}
$$

這就是 Phase 9 之後新的技術方向。

---

# 結論

ACR Phase 0–8 已讓 AI 逐步取得：

- 可定址 cognition；
- cognitive program；
- self-dialogue；
- temporal-causal history；
- governance evidence；
- reflexive self-observation；
- self-inquiry；
- open-world autonomy；
- relational boundary awareness。

接下來真正缺少的，不只是 Agenda Generator。

而是：

$$
\boxed{
\text{Strategic Self-Direction before Agenda commitment.}
}
$$

因此 Phase 9 正式重定義為：

# **Strategic-Cognitive Agenda Runtime**

其核心輸入：

$$
\boxed{
SemanticState
+
SelfObservation
+
Goal
+
Environment
+
Commitments.
}
$$

其可選策略中介：

$$
\boxed{
StrategicTension
\rightarrow
StrategyLensConfiguration
\rightarrow
StrategyRoutingProfile.
}
$$

其 Agenda 輸出：

$$
\boxed{
SELECTED,
HELD,
DISMISSED,
NO\_AGENDA.
}
$$

其策略輸出：

$$
\boxed{
NO\_INTERVENTION,
KEEP,
ACTIVATE,
SWITCH,
CORRECT,
DROP,
UNRESOLVED.
}
$$

其世界邊界仍保持：

$$
\boxed{
Strategy
\not\Rightarrow
Authority
\not\Rightarrow
Commit.
}
$$

最後，真正成熟的 Persistent AI 不只需要回答：

> 下一步做什麼？

還要能回答：

> 我是否正在錯的問題空間中？

> 現在應該留局、換局、破局、改尺度、保留多路，還是根本不要策略化？

而當它有能力改變自己的策略 frame 時，它仍必須知道：

> 哪些是自己的認知自由，哪些已經進入共享世界與其他主體的合法邊界。

因此最終可以寫成：

$$
\boxed{
\text{Autonomous Strategic Cognition}
=
\text{Frame Self-Direction}
+
\text{Cognitive Self-Direction}
+
\text{Agenda Self-Direction}
+
\text{Boundary Integrity}.
}
$$

這就是 ACR Phase 9–12 新路線的工程母架構。

---

## 上游 Canonical Sources

1. `從策略境相到認知域活動_無界策_x_CODT_x_反身自主Runtime_統一框架_v0.1.md`
2. `無界策_源點_Kindle修訂版(1).md`
3. `無界策境相圖譜.md`
4. `CODT_01` 至 `CODT_10` v1.0
5. `01_從自提示到自主認知閉環_持續目標型AI的基礎理論_v0.1.md`
6. `02_可定址認知空間_Cognitive_Affordance_Semantic_Address與認知算子_v0.1.md`
7. `03_自我對話不是文字_AI-Native_Cognitive_Program與Zero-Rendering_Runtime_v0.1.md`
8. `04_時間因果自我史_CTCL-ITR_Decision_Receipt與上下文壓縮後的可追溯性_v0.1.md`
9. `05_契約邊界內的AI自主性_Execute_Refuse_Defer_Idle與Escalate_v0.1.md`
10. `06_Addressable_Cognitive_Runtime_x_CTCL_統一技術白皮書與實作路線圖_v0.1.md`
11. `Phase8_Canonical_Rules_反身自主運行層_v0.1.md`
12. `Addressable_Cognitive_Runtime_MVP_v0.1_Phase8_Reflexive_Autonomy_Runtime_2026-08-23`

---

## 版本記錄

### v0.1 — 2026-08-23

- 將 ACR Phase 9 從單純 Agenda Runtime 重構為 Strategic-Cognitive Agenda Runtime；
- 固定 Direct Agenda Path 與 Strategic Path 雙路；
- 新增 Strategic Tension State；
- 新增 Strategy Lens / Strategy Lens Graph；
- 新增 Strategy Resolution；
- 新增 Strategy Routing Profile；
- 新增 Agenda Resolution；
- 保留 Phase 0 AgendaCandidate schema；
- 固定 Strategy Lens 不等於 Cognitive Domain；
- 固定 Strategy Shift 不推出 Atlas Repartition；
- 固定 Strategy 不 self-grant external authority；
- 固定 Strategy Context 不等於 Commitment；
- 固定 internal strategy resolution 不濫用 Decision Receipt；
- 重新定義 Phase 9.0–9.8；
- 更新 Phase 10–12 與 SCG 的接口；
- 建立 Strategy / Agenda CTCL event namespace；
- 建立 11 組 Phase 9 falsification gates；
- 建立 backward compatibility matrix；
- 將 SCG 理論正式轉成 ACR 可實作工程母架構。
