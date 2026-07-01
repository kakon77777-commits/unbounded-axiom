# 反身時空記憶圖動力學：面向 AGI-like Agent 的記憶治理與幻覺失真分類理論

**Document ID:** RSMGD-2026-v0.1  
**Title:** Reflexive Spatiotemporal Memory Graph Dynamics  
**Chinese Title:** 反身時空記憶圖動力學  
**Subtitle:** A Memory-Governed Agent Runtime Theory for AGI-like Behavior and Hallucination Decomposition  
**Author:** Neo.K / EveMissLab  
**Status:** Theoretical Whitepaper / MD Paper Draft  
**Version:** v0.1  
**Date:** 2026  
**Relation to Previous Work:** Extends Temporal Loop Taxonomy and Temporal-Spatial Loop-Slice Dynamics by adding long-term memory governance and hallucination failure-mode decomposition.  
**Target Domains:** AI Agent runtime, long-term memory systems, local-first agent plugin runtime, EML/AST/CTS verification, hallucination mitigation, AGI-like engineering systems.

---

## 摘要

時間迴圈分類學處理 Agent 如何跨時間等待、恢復、重試與收斂；空間切片分類學處理 Agent 如何定位問題空間、切割任務範圍、擴張與收縮作用域；反身圖動力學處理 Agent 如何在失敗時修正自己的切片、策略與假設。

然而，若缺少長期記憶，Agent 仍只能在單次任務中表現出局部智能，難以跨任務累積經驗、避免重犯錯誤、保存專案規則、維持使用者偏好、追蹤假設失效與形成穩定的自我修正能力。

本文提出「反身時空記憶圖動力學」（Reflexive Spatiotemporal Memory Graph Dynamics, RSMGD）：一種將時間迴圈、空間切片、反身圖更新與長期記憶治理整合起來的 Agent runtime 理論。其核心命題是：

```text
時間迴圈解決 Agent 的時間持續性。
空間切片解決 Agent 的作用定位。
反身圖動力學解決 Agent 的策略修正。
長期記憶治理解決 Agent 的跨任務累積。
```

本文同時將「AI 幻覺」從單一問題拆解為多種失真機制：知識缺口、時間過期、空間定位錯誤、圖邊錯誤、檢索失敗、記憶污染、工具回饋錯誤、使用者錯前提、對齊誘導、獎勵猜測、不確定性治理不足等。本文不將 AI 幻覺視為單一病症，而是將其視為 Agent 時空記憶圖中的多類 failure modes。

在扣除主觀性與意識判斷後，若一個 Agent 具備工具使用、時間迴圈、空間切片、反身圖更新、長期記憶、記憶治理、來源追蹤與人類決策接口，則它在工程操作標準上已具備 AGI-like Agent 的主要結構。

---

## 0. 導論：從時空 Agent 到記憶 Agent

### 0.1 前置理論

前兩個理論層分別解決了 Agent 的時間與空間問題。

#### 時間迴圈分類學

時間迴圈分類學指出，現代 Agent 的任務不是一次性函式呼叫，而是：

```text
act
observe
suspend
wake
resume
retry
degrade
ask human
```

它處理的是：

```text
何時做？
何時等？
何時恢復？
何時重試？
何時停止？
```

#### 空間切片分類學

空間切片分類學指出，Agent 不會直接面對整個世界，而會先切割問題空間：

```text
repo → package → file → function → AST node → test → error trace
```

它處理的是：

```text
在哪裡看？
在哪裡改？
在哪裡測？
在哪裡擴張？
在哪裡收縮？
```

#### 反身圖動力學

反身圖動力學指出，Agent 不能只在既定切片內前向推進，也必須能在失敗時修正自己的切片、策略與假設。

它處理的是：

```text
如果我切錯了怎麼辦？
如果我重試錯方向怎麼辦？
如果錯不在當前檔案怎麼辦？
如果我誤解了錯誤訊息怎麼辦？
```

---

### 0.2 尚未解決的核心：記憶

若沒有記憶，Agent 仍會出現：

```text
同一 repo 的錯誤下次又重犯。
同一使用者偏好下次又忘記。
同一專案禁忌下次又踩線。
同一錯誤假設下次又提出。
同一修法造成副作用卻沒有留下反身記錄。
```

因此，真正接近 AGI-like 的 Agent，不只需要時間、空間與反身性，還需要記憶。

但記憶不是單純向量資料庫，也不是把聊天紀錄全部塞進 context。記憶需要：

```text
分類
範圍
來源
可信度
有效期限
觸發條件
遺忘機制
人類審核
反身修正
```

本文因此提出一個完整的「時空記憶 Agent」框架。

---

## 1. AGI-like Agent 的工程邊界

### 1.1 不是哲學意義上的 AGI

本文不主張解決以下問題：

```text
意識
主觀性
自由意志
感受性
自我存在感
道德主體地位
```

這些屬於哲學、認知科學與倫理學層面的問題。

本文討論的是工程意義上的 AGI-like Agent，也就是：

```text
可跨任務遷移
可長期累積
可使用工具
可修正策略
可處理多領域任務
可管理自身記憶
可在失敗後調整行動模式
可在人類治理下長期協作
```

---

### 1.2 工程標準下的 AGI-like

若一個 Agent 具備：

```text
Tool Use
+ Temporal Loop
+ Spatial Slice
+ Reflexive Graph
+ Long-term Memory
+ Governance
+ Verification
```

則它不再只是聊天模型，而是具有持續任務能力的工程智能體。

本文將這種系統稱為：

```text
AGI-like Runtime Agent
```

或：

```text
工程型類 AGI 智能體
```

這不是宣稱它具備意識，而是指出它在行動結構上已接近一般任務智能。

---

## 2. 基本形式化

### 2.1 時空記憶任務狀態

令 Agent 在時間 `t` 的任務狀態為：

```text
Ω_t = <G_t, Σ_t, Τ_t, M_t, Π_t, F_t>
```

其中：

```text
G_t = 任務圖
Σ_t = 空間切片
Τ_t = 時間迴圈
M_t = 記憶狀態
Π_t = 策略與治理規則
F_t = 回饋與驗證結果
```

任務演化為：

```text
Ω_t → Action_t → Observation_t → Ω_{t+1}
```

若任務成功，更新成果記憶。

若任務失敗，更新反身記憶。

若發生不確定性，進入人類決策或來源查證。

---

### 2.2 記憶作為圖上的持久層

記憶不是附屬資料，而是任務圖中的持久層：

```text
M_t ⊆ G_t
```

記憶節點可以是：

```text
UserPreference
ProjectInvariant
PastError
FailedHypothesis
SuccessfulPatch
RiskPolicy
SourceEvidence
ToolBehavior
SemanticRule
TemporalPattern
SpatialPattern
```

記憶邊可以是：

```text
supports
contradicts
derived_from
invalidated_by
applies_to
expires_at
retrieved_by
caused_failure
prevented_error
requires_human_review
```

因此，記憶不是一串文字，而是一組可查證、可失效、可作用於未來任務的圖節點。

---

## 3. Agent 記憶分類學

本文將 Agent 記憶分為十類。

---

### 3.1 Episodic Memory：事件記憶

事件記憶保存「發生過什麼」。

例子：

```text
2026-06-20：Agent 修復 EML parser 的 SumExpression 測試失敗。
第 3 次嘗試後發現問題不在 parser，而在 Unicode normalization。
```

用途：

```text
回顧過去任務
避免重複走錯路
提供 temporal trace
```

---

### 3.2 Semantic Memory：語義記憶

語義記憶保存「概念與規則」。

例子：

```text
EML 的 x^+n 若符號未定義，表示初始化。
若符號已定義，表示加法更新。
```

用途：

```text
維持規格一致
生成文件
協助推理
```

---

### 3.3 Procedural Memory：程序記憶

程序記憶保存「怎麼做」。

例子：

```text
修 parser 前先跑 pnpm test parser。
修 transpiler 後要跑 golden test。
發布前要跑 typecheck。
```

用途：

```text
工作流自動化
減少 prompt 重複
維持專案流程
```

---

### 3.4 Project Memory：專案記憶

專案記憶保存特定專案的不變式。

例子：

```text
EML MVP 不碰時間迴圈 runtime。
LAPR MVP 先做 Local Daemon + Plugin Manifest。
不要在 v0.1 加完整 C+++。
```

用途：

```text
防止 scope creep
維持 roadmap
避免 Agent 亂加功能
```

---

### 3.5 Reflexive Memory：反身記憶

反身記憶保存「我上次怎麼判斷錯」。

例子：

```text
上次修 case-03-sum 時，Agent 誤判為 parser bug；
實際根因是 lexer normalization 未處理 superscript。
```

用途：

```text
避免重複錯誤假設
改善切片策略
改善 loop 策略
```

這是 AGI-like Agent 的關鍵記憶。

---

### 3.6 Governance Memory：治理記憶

治理記憶保存權限、安全與風險規則。

例子：

```text
不可自動 git push。
不可自動刪除大量檔案。
修改 public API 必須 human approval。
插件不可預設讀取 home directory。
```

用途：

```text
降低 Agent 高風險行為
啟動 human-decision loop
建立安全邊界
```

---

### 3.7 Source Memory：來源記憶

來源記憶保存某項知識從哪裡來。

例子：

```json
{
  "claim": "SWE-agent uses an agent-computer interface for software engineering tasks.",
  "source": "SWE-agent paper",
  "confidence": 0.9
}
```

用途：

```text
來源追蹤
降低 hallucination
支援引用
```

---

### 3.8 Negative Memory：負例記憶

負例記憶保存「不要再做什麼」。

例子：

```text
不要把 all fixtures 一次重寫。
不要在 parser test failure 時先改 README。
不要把 failing expected output 當成 actual output。
```

用途：

```text
避免錯誤修法復發
加強反身治理
```

---

### 3.9 Temporal Validity Memory：時間有效性記憶

有些記憶只在特定時間有效。

例子：

```text
目前 Claude Code CLI 參數為 X。
目前 EML grammar v0.1 支援 14 個 case。
目前 repo 還沒有正式 release。
```

用途：

```text
避免過期資訊污染
提示重新查證
```

---

### 3.10 Preference Memory：偏好記憶

偏好記憶保存使用者或團隊的風格偏好。

例子：

```text
使用者偏好直接、結構化、少空泛稱讚。
技術文檔偏好 Markdown。
理論先命名，再工程化。
```

用途：

```text
長期協作
文件風格一致
減少重複溝通
```

---

## 4. 記憶生命週期

Agent 記憶不應只被「存入」，而應有完整生命週期。

```text
Observe
→ Extract
→ Classify
→ Store
→ Retrieve
→ Apply
→ Validate
→ Update
→ Forget / Archive
```

---

### 4.1 Extract：抽取

從任務事件、對話、測試結果、文件、工具輸出中抽取候選記憶。

問題：

```text
這件事值得長期記住嗎？
它是偏好、規則、錯誤、來源還是流程？
```

---

### 4.2 Classify：分類

每個記憶必須被分類：

```text
episodic
semantic
procedural
project
reflexive
governance
source
negative
temporal_validity
preference
```

---

### 4.3 Scope：作用範圍

記憶必須有作用範圍：

```text
global
user
project
repo
file
task
session
plugin
provider
```

例子：

```json
{
  "scope": "project:EML",
  "appliesTo": ["parser", "transpiler", "grammar"]
}
```

---

### 4.4 Provenance：來源

每個重要記憶應記錄來源：

```text
user_statement
test_result
tool_output
document
web_source
human_approval
agent_inference
```

Agent 推論出的記憶與人類明確確認的記憶必須分開。

---

### 4.5 Confidence：可信度

記憶應有可信度：

```text
confirmed
high
medium
low
hypothesis
deprecated
```

---

### 4.6 Retrieval：檢索

記憶應被觸發，而不是無差別塞入上下文。

觸發方式：

```text
keyword
semantic similarity
task type
space slice
loop type
error pattern
user identity
project state
```

---

### 4.7 Validation：驗證

記憶被使用前應檢查：

```text
是否過期？
是否與新資訊衝突？
是否只適用於舊版本？
是否由人類確認？
是否需要重新查證？
```

---

### 4.8 Forget / Archive：遺忘與封存

記憶治理需要遺忘。

應遺忘：

```text
短期狀態
過期 CLI 參數
被證明錯誤的假設
不再適用的專案規則
使用者明確要求刪除的內容
```

應封存：

```text
歷史決策
重大失敗
版本轉折
安全事故
```

---

## 5. 記憶治理：真正困難的部分

記憶的難點不是儲存，而是治理。

### 5.1 核心問題

```text
什麼值得記？
什麼應該忘？
什麼只是暫時狀態？
什麼是長期規則？
什麼是錯誤經驗？
什麼是使用者偏好？
什麼記憶會污染未來判斷？
什麼記憶需要人類批准？
```

---

### 5.2 記憶污染

記憶污染是指錯誤資訊進入長期記憶後，反覆影響未來任務。

例子：

```text
Agent 錯誤記住「sum parser 的問題在 emitter」。
之後每次遇到 sum 測試失敗，都先改 emitter。
```

處理：

```text
source tracking
confidence decay
contradiction detection
human correction
negative memory update
```

---

### 5.3 反身記憶比普通記憶更重要

普通記憶：

```text
我記得發生過什麼。
```

反身記憶：

```text
我記得我上次為什麼判斷錯。
```

反身記憶會直接改善 Agent 的未來切片與迴圈策略。

---

## 6. AI 幻覺的重新定位

### 6.1 AI 幻覺不是單一問題

本文不將 AI 幻覺視為單一機制。

更準確地說：

```text
AI 幻覺不是一種病。
它是一組不同來源的失真現象，被同一個名稱包起來。
```

幻覺可能來自：

```text
知識缺口
訓練資料不完整
資料清洗造成底層缺口
版權與安全策略造成內容缺失
RLHF 與對齊誘導
公司憲法 / safety policy 造成表達轉向
評估指標獎勵猜測
檢索失敗
記憶污染
工具輸出錯誤
使用者問題帶錯前提
模型生成機制偏向流暢補洞
不確定性治理不足
```

因此，空泛地說「解決 AI 幻覺」沒有意義。需要把幻覺拆成 failure modes。

---

### 6.2 人類也有幻覺

人類也會：

```text
記錯
誤判
合理化
迎合
不懂裝懂
為了面子亂答
為了利益欺騙
被錯誤前提帶走
用流暢敘事掩蓋不確定性
```

因此，AI 幻覺不是「人類沒有、AI 才有」的現象。

差異在於：

```text
AI 以機器速度、機器規模、機器流暢度重現並放大了類似失真。
```

因此，AI 幻覺之所以危險，不是因為它完全異於人類，而是因為它把錯誤包裝成高流暢、高速度、高擴散性的輸出。

---

### 6.3 為什麼 AI 需要更高標準

雖然人類也會錯，但 AI 被視為工具、搜尋助手、工程助手與決策輔助系統，所以使用者自然期待：

```text
更客觀
更穩定
更可查證
更不該亂編
```

這種期待不完全公平，但工程上必須面對。

因此，重點不是為 AI 幻覺辯護，而是建立一套可追蹤、可定位、可修正的失真治理架構。

---

## 7. 幻覺失真分類學

本文將 AI 幻覺拆為十二類。

---

### 7.1 Knowledge Gap Hallucination：知識缺口幻覺

模型不知道答案，但仍生成看似合理內容。

處理：

```text
uncertainty declaration
source retrieval
human-decision loop
```

---

### 7.2 Temporal Staleness Hallucination：時間過期幻覺

模型使用過期資訊回答當前問題。

處理：

```text
temporal validity check
web / source refresh
memory expiration
```

---

### 7.3 Spatial Mislocalization Hallucination：空間定位錯誤幻覺

Agent 找錯問題空間。

例子：

```text
錯把 parser bug 當 emitter bug。
錯把 A 公司資訊套到 B 公司。
```

處理：

```text
space slice verification
dependency graph inspection
expand / switch slice
```

---

### 7.4 Graph Edge Hallucination：圖邊幻覺

Agent 建立不存在的關係。

例子：

```text
A 函式其實沒有呼叫 B 函式，但 Agent 說有。
某論文其實沒有支持某命題，但 Agent 說支持。
```

處理：

```text
graph edge provenance
source citation
static analysis
```

---

### 7.5 Retrieval Mismatch Hallucination：檢索錯配幻覺

RAG 或搜尋找到錯資料，Agent 卻將其當成正確依據。

處理：

```text
source ranking
cross-source check
claim-source alignment
```

---

### 7.6 Memory Contamination Hallucination：記憶污染幻覺

錯誤記憶被保存，之後反覆導致錯誤輸出。

處理：

```text
memory confidence
human correction
contradiction tracking
memory invalidation
```

---

### 7.7 Tool Feedback Corruption：工具回饋污染

工具輸出錯誤、環境錯誤或解析錯誤，Agent 卻相信工具結果。

處理：

```text
tool output validation
rerun
secondary tool check
runtime trace
```

---

### 7.8 Reward-Induced Guessing：獎勵猜測幻覺

模型在訓練或評估中被鼓勵回答，而不是承認不知道。

處理：

```text
abstention reward
uncertainty calibration
confidence threshold
```

---

### 7.9 Alignment-Induced Distortion：對齊誘導失真

RLHF、公司憲法、安全策略或風格對齊造成模糊、轉向、過度保守或迎合式輸出。

處理：

```text
policy transparency
uncertainty labeling
separate safety refusal from factual uncertainty
```

---

### 7.10 Data-Cleaning Void Hallucination：資料清洗缺口幻覺

底層資料因清洗、版權、隱私、安全或品質篩選出現缺口，模型仍嘗試補全。

處理：

```text
dataset limitation awareness
source retrieval
do-not-infer policy
```

---

### 7.11 User-Premise Hallucination：使用者錯前提幻覺

使用者問題本身含有錯誤前提，模型順著答。

處理：

```text
premise check
clarifying question
counterfactual detection
```

---

### 7.12 Fluency-Completion Hallucination：流暢補洞幻覺

模型為維持語句完整與敘事連貫，自動補出未驗證細節。

處理：

```text
claim segmentation
fact-check checkpoints
source-required mode
```

---

## 8. 幻覺在 RSMGD 中的映射

| 幻覺類型 | 對應系統層 |
|---|---|
| 知識缺口 | memory / retrieval gap |
| 時間過期 | temporal validity failure |
| 空間定位錯誤 | spatial slice failure |
| 圖邊幻覺 | graph edge error |
| 檢索錯配 | source retrieval failure |
| 記憶污染 | memory governance failure |
| 工具回饋污染 | feedback corruption |
| 獎勵猜測 | training/evaluation incentive |
| 對齊誘導失真 | governance / policy distortion |
| 資料清洗缺口 | base-space data void |
| 使用者錯前提 | premise validation failure |
| 流暢補洞 | generation fluency pressure |

因此，幻覺不是單點錯誤，而是時空記憶圖中的多點失真。

---

## 9. 幻覺治理策略

### 9.1 不確定性標註

Agent 應能標註：

```text
known
unknown
uncertain
inferred
source-backed
memory-backed
tool-backed
needs-verification
```

---

### 9.2 Claim-Level Source Grounding

不是整段回答引用一個來源，而是每個重要 claim 都應能對應來源或記憶。

---

### 9.3 Memory Provenance

每段記憶要知道來源：

```text
誰說的？
何時說的？
哪個任務產生的？
是否被驗證？
是否過期？
是否被否定？
```

---

### 9.4 Contradiction Detection

新資訊與舊記憶衝突時，不應直接覆蓋，而應建立 contradiction edge。

---

### 9.5 Human-Decision Loop

高風險、不確定、來源不足、語義爭議時，應進入人類決策迴圈。

---

### 9.6 Reflexive Memory Update

每次幻覺或錯誤被發現，都應更新反身記憶：

```text
這次錯誤屬於哪類失真？
錯誤來源是什麼？
下次如何避免？
```

---

## 10. RSMGD Metadata Schema

```json
{
  "taskId": "task_001",
  "space": {
    "sliceType": "semantic_slice",
    "center": "AI hallucination taxonomy",
    "scope": "theory"
  },
  "time": {
    "loopType": "convergent",
    "condition": "theory is internally consistent",
    "maxAttempts": 5
  },
  "memory": {
    "retrieved": [
      {
        "id": "mem_001",
        "type": "reflexive",
        "content": "Previous hallucination discussion should be treated as failure-mode classification, not as a single root cause.",
        "scope": "theory:RSMGD",
        "confidence": "high",
        "source": "user_statement",
        "validity": "until theory revision"
      }
    ],
    "newCandidates": [
      {
        "type": "negative",
        "content": "Do not claim hallucination is caused only by RLHF.",
        "source": "reasoning",
        "requiresReview": true
      }
    ]
  },
  "governance": {
    "uncertaintyPolicy": "mark_inference",
    "sourcePolicy": "source_required_for_external_claims",
    "humanDecision": "required_for_theory_boundary_changes"
  }
}
```

---

## 11. 最小工程實作

### 11.1 MVP 記憶欄位

第一版 Agent memory 不需要複雜，只要有：

```ts
export interface AgentMemory {
  id: string;
  type:
    | "episodic"
    | "semantic"
    | "procedural"
    | "project"
    | "reflexive"
    | "governance"
    | "source"
    | "negative"
    | "temporal_validity"
    | "preference";

  content: string;
  scope: string;
  confidence: "confirmed" | "high" | "medium" | "low" | "hypothesis" | "deprecated";
  source: "user" | "tool" | "test" | "document" | "web" | "agent_inference";
  createdAt: string;
  updatedAt: string;
  validUntil?: string;
  retrievalTriggers: string[];
  invalidatedBy?: string[];
}
```

---

### 11.2 記憶使用規則

```text
1. 只檢索與當前 task / slice / loop 相關的記憶。
2. 低可信記憶只能作為假設，不可作為事實。
3. 過期記憶必須重新驗證。
4. 反身記憶優先用於防止重複錯誤。
5. governance memory 可覆蓋其他任務目標。
```

---

### 11.3 幻覺檢測事件

```ts
export interface DistortionEvent {
  id: string;
  taskId: string;
  type:
    | "knowledge_gap"
    | "temporal_staleness"
    | "spatial_mislocalization"
    | "graph_edge_error"
    | "retrieval_mismatch"
    | "memory_contamination"
    | "tool_feedback_corruption"
    | "reward_induced_guessing"
    | "alignment_induced_distortion"
    | "data_cleaning_void"
    | "user_premise_error"
    | "fluency_completion";

  claim: string;
  evidence?: string[];
  severity: "low" | "medium" | "high";
  action: "mark_uncertain" | "retrieve_source" | "ask_human" | "invalidate_memory" | "revise_answer";
}
```

---

## 12. 與 LAPR / EML / TSGD 的整合

### 12.1 LAPR

LAPR 可以將 memory 作為 task runtime 的一部分：

```text
task
→ retrieve project memory
→ select space slice
→ run temporal loop
→ validate output
→ update reflexive memory
```

### 12.2 EML / AST / CTS

EML 提供結構化驗證層：

```text
source
→ AST
→ CTS
→ symbolTable
→ crossRefTable
→ round-trip validator
```

這些可以降低以下幻覺：

```text
graph edge hallucination
spatial mislocalization
semantic inconsistency
round-trip loss
```

### 12.3 TSGD

TSGD 提供時空控制：

```text
where to act
when to retry
when to expand slice
when to ask human
```

RSMGD 則在 TSGD 上增加：

```text
what was learned
what was wrong
what should be remembered
what must be forgotten
```

---

## 13. 理論邊界

本文不宣稱：

```text
完全解決 AI 幻覺
證明 AI 有意識
證明 AI 等同人類
保證 Agent 不犯錯
```

本文主張：

```text
AI 幻覺應被拆解為多類時空記憶圖失真。
長期記憶與反身治理是 AGI-like Agent 的核心缺口。
記憶治理比單純記憶儲存更重要。
```

---

## 14. Roadmap

### v0.1：理論定義

1. 記憶分類學。
2. 幻覺失真分類學。
3. RSMGD metadata。
4. 與 TSGD / LAPR / EML 對接。

### v0.2：Memory Schema MVP

1. AgentMemory interface。
2. Scope / confidence / provenance。
3. Retrieval trigger。
4. InvalidatedBy。
5. Negative memory。

### v0.3：Reflexive Memory Runtime

1. Failed hypothesis tracking。
2. Repeated failure detection。
3. Memory contamination detection。
4. Slice strategy memory。
5. Loop strategy memory。

### v0.4：Hallucination Governance Layer

1. DistortionEvent。
2. Claim-level source tracking。
3. Uncertainty policy。
4. Contradiction graph。
5. Human-decision loop integration。

### v0.5：AGI-like Agent Runtime

1. Long-term project memory。
2. Multi-agent shared memory。
3. Source-backed reasoning。
4. Tool-verified action loop。
5. Temporal-spatial-memory graph visualization。

---

## 15. 結論

時間迴圈讓 Agent 能跨時間持續。

空間切片讓 Agent 能定位作用範圍。

反身圖動力學讓 Agent 能在失敗時修正自己的策略。

長期記憶治理讓 Agent 能跨任務累積經驗。

四者合起來，構成了 AGI-like Agent 的工程骨架：

```text
Temporal Loop
+ Spatial Slice
+ Reflexive Graph
+ Governed Long-term Memory
= AGI-like Agent Runtime
```

AI 幻覺不應被視為單一神祕缺陷，而應被拆解為時空記憶圖中的多類失真。人類也會犯錯、誤判、迎合與合理化；AI 的特殊性在於它以更高速度、更大規模、更流暢形式生成失真。因此，真正的解法不是空泛要求「不要幻覺」，而是建立：

```text
不確定性標註
來源追蹤
記憶治理
反身修正
空間切片驗證
時間迴圈控制
人類決策接口
```

在排除意識與主觀性判定後，若一個 Agent 能長期記憶、跨任務修正、使用工具、定位問題空間、管理時間迴圈、追蹤來源並在不確定時請人類決策，那麼它在工程意義上已經非常接近 AGI-like 系統。

本文的最終命題是：

```text
AGI-like Agent 的關鍵不是單次推理，而是可治理的長期時空記憶動力學。
```

---

## References

1. Charles Packer et al., **MemGPT: Towards LLMs as Operating Systems**, 2023.  
   https://arxiv.org/abs/2310.08560

2. John Yang et al., **SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering**, 2024.  
   https://arxiv.org/abs/2405.15793

3. Adam Tauman Kalai et al., **Why Language Models Hallucinate**, 2025.  
   https://arxiv.org/abs/2509.04664

4. Yuntao Bai et al., **Constitutional AI: Harmlessness from AI Feedback**, 2022.  
   https://arxiv.org/abs/2212.08073

5. Yuanchen Bei et al., **Mem-Gallery: Benchmarking Multimodal Long-Term Conversational Memory for MLLM Agents**, 2026.  
   https://arxiv.org/abs/2601.03515

6. Yihang Ding et al., **MemGround: Long-Term Memory Evaluation Kit for Large Language Models in Gamified Scenarios**, 2026.  
   https://arxiv.org/abs/2604.14158
