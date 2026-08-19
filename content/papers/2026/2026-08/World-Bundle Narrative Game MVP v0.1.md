# World-Bundle Narrative Game MVP v0.1
## 世界束敘事遊戲：從固定世界線到即時可達未來束

**定位：** 遊戲設計／技術白皮書／MVP 可行性規格  
**版本：** v0.1

---

## 0. 一句話定義

這不是「AI 每回合隨機生成下一段故事」。

而是：

\[
\boxed{
PlayerIntent
\xrightarrow{AI}
SemanticAction
\xrightarrow{WorldRules}
CandidateFutureBundle
\xrightarrow{Simulator}
ValidatedFutureBundle
\xrightarrow{Commit}
S_{t+1}
}
\]

AI 即時理解玩家意圖，展開「目前可能成立的未來束」；真正哪些未來可發生，仍由遊戲狀態機與世界規則決定。

---

## 1. 同一個遊戲，又不是同一個遊戲

所有玩家共享同一個 canonical world kernel：

\[
\mathcal W=(Rules,Characters,Locations,History,StateVariables,CausalConstraints)
\]

但玩家 \(p\) 在時間 \(t\) 的可達未來集合：

\[
\mathcal B_{p,t}
\]

可以與玩家 \(q\) 不同：

\[
\mathcal W_p=\mathcal W_q
\quad\land\quad
\mathcal B_{p,t}\neq\mathcal B_{q,t}.
\]

因此共享同一套世界法則，卻不共享同一個未來空間。

---

## 2. 從世界線到世界束

傳統 AVG：

\[
S_t\rightarrow S_{t+1}^{(i)}.
\]

世界束：

\[
S_t\rightarrow
\mathcal B_t=\{F_1,F_2,\ldots,F_n\}.
\]

玩家行為 \(a_t\) 不只是選 branch，而是改變未來空間本身：

\[
\boxed{
a_t:\mathcal B_t\rightarrow\mathcal B_{t+1}.
}
\]

一次選擇可能：

1. 刪除部分未來；
2. 解鎖新未來；
3. 改變 NPC 可達狀態；
4. 改變事件順序；
5. 改變誰知道什麼；
6. 讓原本不可能的支線變成可能。

---

## 3. Hard Bundle / Soft Bundle

### Hard Future Bundle

\[
\mathcal B_t^{hard}
\]

由作者與 deterministic rules 鎖定：

- 世界設定；
- 核心秘密；
- NPC 生死；
- 重大事件前置條件；
- 關鍵物品；
- 結局條件；
- 不可逆狀態。

AI 不得越界。

### Soft Future Bundle

\[
\mathcal B_t^{soft}
\]

AI 可以動態展開：

- NPC 語氣；
- 小事件組合；
- 誰先找玩家；
- 支線出現時機；
- 某伏筆如何被揭露；
- 同一 hard outcome 的不同表現。

概念上：

\[
\boxed{
\mathcal B_t=
\mathcal B_t^{hard}\ltimes\mathcal B_t^{soft}.
}
\]

MVP 不必真的實作半直積；它只表示 soft 層永遠受 hard 層約束。

---

## 4. 玩家輸入不再只是 Choice ID

NPC：

> 「你是不是早就知道我父親是兇手？」

玩家：

> 「我不想直接騙她，但現在讓她知道會害死她。先把她帶走，安全後再說。」

AI 不直接寫死下一章，而先解析：

```json
{
  "truth_policy": "delay_truth",
  "lie_policy": "avoid_direct_lie",
  "protect_target": "aya",
  "trust_goal": "preserve",
  "candidate_actions": [
    "redirect_topic",
    "partial_truth",
    "move_to_safe_location"
  ]
}
```

遊戲規則再驗證：

- Aya 是否已經看過證據；
- Ren 是否在場；
- 出口是否開啟；
- 玩家過去是否欺騙 Aya；
- 當前剩餘時間；
- Aya 的 suspicion / trust。

---

## 5. Same Choice ≠ Same Future

兩名玩家都輸入：

> 「我相信她。」

但如果：

\[
S_{p,t}\neq S_{q,t},
\]

可能分別成為：

- genuine trust；
- political alliance；
- pragmatic compliance；
- trap trigger。

所以：

\[
\boxed{
SameSurfaceChoice

ot\Rightarrow
SameSemanticAction

ot\Rightarrow
SameFutureBundle.
}
\]

---

## 6. MVP 世界規模

第一版只做封閉場景。

### 場景

暴雨夜的研究設施／旅館／避難所。

### 角色

- Player
- Aya
- Ren
- Director

### 核心秘密

一個事故真相；有人知道部分真相，但證據不完整。

### 可見核心變數

```text
time
trust_aya
trust_ren
danger
evidence
```

### 隱藏狀態

```text
aya_knows_truth
ren_suspects_player
director_covering_up
power_online
exit_open
```

第一版 hard state variables 控制在約 20 個量級。

---

## 7. 每回合 Gameplay Loop

\[
\boxed{
Observe
\rightarrow
PlayerIntent
\rightarrow
SemanticParse
\rightarrow
BundleExpand
\rightarrow
Validate
\rightarrow
Present
\rightarrow
Commit
\rightarrow
StateTransition
}
\]

### Observe
顯示場景、NPC、危機與玩家已知資訊。

### PlayerIntent
同時保留傳統選項與自由文字。

### SemanticParse
AI 只輸出受限結構，不直接寫遊戲真實 state。

### BundleExpand
根據 Intent + WorldState 產生候選 future nodes。

### Validate
deterministic rule engine 驗證 requirements / blocks / effects。

### Present
只顯示玩家當下應該看到的 narrative consequence。

### Commit
玩家行為真正寫入 world state。

---

## 8. World State 範例

```json
{
  "turn": 7,
  "location": "lab_hall",
  "npcs": {
    "aya": {
      "trust": 61,
      "knows_truth": false,
      "suspicion": 40
    },
    "ren": {
      "trust": 30,
      "suspicion": 72
    }
  },
  "world": {
    "danger": 55,
    "power_online": false,
    "exit_open": true
  },
  "history_tags": [
    "lied_to_aya_once",
    "ren_saw_evidence"
  ]
}
```

---

## 9. Event Rule

```json
{
  "event_id": "aya_demands_truth",
  "requirements": [
    "aya.suspicion >= 60",
    "aya.knows_truth == false"
  ],
  "blocking": [
    "aya.unconscious == true"
  ],
  "effects": {
    "aya.suspicion": "+10"
  },
  "next_bundle_tags": [
    "truth_confrontation"
  ]
}
```

AI 可以提議這個 event；只有 rule engine 能確認它是否合法。

---

## 10. World-Bundle Node

```json
{
  "bundle_node": "B_aya_truth_04",
  "hard_constraints": [
    "aya_alive",
    "evidence_exists"
  ],
  "soft_options": [
    "direct_truth",
    "partial_truth",
    "redirect",
    "leave",
    "ask_ren"
  ],
  "possible_events": [
    "aya_demands_truth",
    "ren_interrupts",
    "power_failure"
  ]
}
```

---

## 11. AI 的工作

AI 只做高價值語義層：

### A. Intent Parsing

\[
NaturalLanguage\rightarrow SemanticAction.
\]

### B. Bundle Ranking

\[
\{F_i\}\rightarrow Ranking.
\]

### C. Soft Narrative Realization

把已確定的 state change 轉成人類可讀敘事。

### D. Speculative Precomputation

玩家仍在閱讀時，提前展開：

\[
\{\mathcal B_{t+1}^{(1)},\mathcal B_{t+1}^{(2)},\mathcal B_{t+1}^{(3)}\}.
\]

---

## 12. 傳統計算機的工作

傳統程式負責：

- state transition；
- event legality；
- time；
- inventory；
- location；
- save/load；
- invalid-state rejection；
- replay；
- deterministic tests。

因此：

\[
\boxed{
AI\neq WorldAuthority.
}
\]

而是：

\[
\boxed{
AI=
SemanticInterpreter+
FutureBundleProposer+
SoftNarrativeRealizer.
}
\]

Computer：

\[
\boxed{
Computer=
WorldStateAuthority+
RuleValidator+
TransitionExecutor.
}
\]

Human：

\[
\boxed{
Human=
IntentSource+
ExperienceObserver+
CommitAuthority.
}
\]

---

## 13. 異質觀察者非同步

\[
O_H,\quad O_A,\quad O_C.
\]

三者可能各自擁有：

\[
\mathcal B_H,\quad
\mathcal B_A,\quad
\mathcal B_C.
\]

並且：

\[
\tau_H\neq\tau_A\neq\tau_C.
\]

AI 可以先預測幾條玩家可能走的 future bundles；Simulator 只驗證合法性；Human 仍停留在當前情節。

這就是「超前計算」在敘事遊戲裡最自然的形式。

---

## 14. Bundle Cache

可以快取：

```text
(StateSignature, IntentClass, RulesVersion)
    -> ValidatedFutureBundle
```

所以 AI 不必每次從零生成。

---

## 15. Bundle Pruning

候選過多時：

\[
Score(F_i)=
w_1Relevance+
w_2CausalReachability+
w_3PlayerPreference+
w_4NarrativeValue-
w_5ComputeCost.
\]

MVP 只保留 Top-K：

\[
K=3\sim6.
\]

---

## 16. 收連 / Convergent Re-linking

若多條 speculative future 最後落到同一 hard-state class：

\[
State(F_1)=State(F_2),
\]

且差異只有 soft dialogue，可合併。

若：

```text
aya.knows_truth = true
```

與：

```text
aya.knows_truth = false
```

不同，必須保留 divergence。

所以：

\[
\boxed{
CRL=
MergeEquivalentFutures+
PreserveMeaningfulDivergence.
}
\]

---

## 17. 防止 Branch Explosion 的真正方法

不是少生成文字。

而是限制：

\[
\boxed{
HardStateDimension.
}
\]

因此：

\[
\boxed{
NarrativeVariation
\gg
HardStateVariation.
}
\]

表面故事可以非常多，底層 causal state classes 仍有限。

這是世界束遊戲可工程化的核心。

---

## 18. 技術選型

### MVP 首選

```text
Godot 4.x
GDScript
Custom Resources / JSON
Rule Engine
LLM HTTP/local adapter
AVG UI
```

### Dialogue Layer

MVP 第一版建議直接用 Godot Resource / JSON。

後續可以接：

- Yarn Spinner：authored dialogue、variables、commands；
- Ink：複雜 authored branching、variables、compiled JSON runtime。

---

## 19. AI Interface

AI 不輸出 authoritative prose state，只輸出 schema：

```json
{
  "intent_class": "protect_and_delay_truth",
  "targets": ["aya"],
  "candidate_action_ids": [
    "redirect",
    "move_to_exit"
  ],
  "confidence": 0.78
}
```

如果模型支援 JSON Schema / structured output，可以直接要求結構；否則 runtime 必須 validation / retry。

---

## 20. AI Fail-Safe

AI timeout / parse failure 時：

1. 回退傳統選項；
2. keyword intent parser；
3. 使用最近合法 intent；
4. world state 不變。

因此：

\[
\boxed{
AIFailure
ot\Rightarrow GameFailure.
}
\]

---

## 21. MVP UI

表面仍是一個 AVG：

```text
┌─────────────────────────────────┐
│ Aya portrait                    │
│ 「你是不是早就知道？」          │
├─────────────────────────────────┤
│ [自然語言輸入框]                │
│                                 │
│ 建議：坦白 / 迴避 / 離開        │
├─────────────────────────────────┤
│ 時間 │ 危險 │ 關係 │ 已知證據  │
└─────────────────────────────────┘
```

不要做成 AI dashboard。

---

## 22. 第一個 MVP 實驗

同一 scenario 重玩多次。

固定輸入：

> 我相信她。

只改：

- trust；
- evidence；
- who_knows；
- danger；
- prior_lie。

測：

\[
SameInput\rightarrow DifferentValidatedBundles.
\]

若玩家能感覺差異來自歷史狀態，而非 AI 亂寫，核心成立。

---

## 23. 第二個 MVP 實驗

固定 WorldState，改變玩家語句：

```text
我相信她。
她大概沒說謊。
現在先照她說的做。
我沒別的選擇，只能相信她。
```

預期分出：

```text
genuine_trust
tentative_trust
pragmatic_compliance
forced_compliance
```

這是自由語義選擇相較固定 AVG option 的主要價值。

---

## 24. 第三個 MVP 實驗

AI 預展 Top-3 future bundles。

玩家最後輸入 Top-3 外行為：

> 我把證據燒掉。

測：

- runtime 能否建立新 bundle；
- hard constraint 是否仍成立；
- 舊 speculative branches 能否安全回收；
- world history 是否完整保存。

---

## 25. MVP Success Criteria

### S1 — Semantic Distinction
不同自然語言意圖可映射不同 intent classes。

### S2 — State Sensitivity
相同輸入在不同 world state 下得到不同 validated bundle。

### S3 — World Legality
AI 不能越過 hard constraints。

### S4 — Replayability
相同 hard state + semantic action + rules version 能重放同一 hard transition。

### S5 — Narrative Variation
同一 hard outcome 可有多種 soft realization。

### S6 — Graceful AI Failure
AI 掛掉時遊戲仍可繼續。

---

## 26. MVP 不需要

第一版不要做：

- 開放世界；
- 100 NPC；
- AI 自由新增 lore；
- 無限制 procedural quest；
- 3D 戰鬥；
- 多 Agent 社會；
- 即時語音；
- 無限記憶。

這些會掩蓋世界束實驗本身。

---

## 27. 第一版九個模組

```text
WorldState
EventRuleEngine
IntentParser
BundleExpander
BundleValidator
BundleRanker
DialogueRealizer
CommitManager
SaveReplay
```

加一個 AVG UI 即可。

---

## 28. 建議資料夾

```text
world_bundle_mvp/
├─ scenes/
├─ scripts/
│  ├─ world_state.gd
│  ├─ rule_engine.gd
│  ├─ intent_parser.gd
│  ├─ bundle_expander.gd
│  ├─ bundle_validator.gd
│  ├─ bundle_ranker.gd
│  ├─ dialogue_realizer.gd
│  └─ commit_manager.gd
├─ data/
│  ├─ characters/
│  ├─ events/
│  ├─ bundles/
│  └─ rules/
├─ ui/
└─ tests/
```

---

## 29. 最小 playable loop

只需跑 10–20 個回合：

\[
\boxed{
看劇情
\rightarrow
自由輸入
\rightarrow
AI理解
\rightarrow
世界束展開
\rightarrow
規則驗證
\rightarrow
NPC回應
\rightarrow
世界改變.
}
\]

這已足夠判定概念是否成立。

---

## 30. 可行性結論

\[
\boxed{
MVP\ 可行。
}
\]

工程上真正困難的不是「生成故事」，而是：

\[
\boxed{
State
\leftrightarrow
SemanticIntent
\leftrightarrow
CausalRules
}
\]

三者的接口。

而這正好是前面 T Query Runtime、異質觀察者非同步語義因果計算、Speculative Expansion、CRL、Commit 可以直接落地的地方。

最終不是：

> AI 幫每個玩家現場寫一款不同遊戲。

而是：

\[
\boxed{
每個玩家在同一套世界法則中，
因自身歷史、語義選擇與 AI 的即時預展，
持續擁有不同的可達未來空間。
}
\]

這就是 World-Bundle Narrative Game。
