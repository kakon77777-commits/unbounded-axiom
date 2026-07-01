# VerifyLoop：面向 Agent 的雙向持續驗證與糾錯協議

## 從生成式回答到可追蹤、可回溯、可修正的 Agent 工作流

作者：Neo.K
機構：EveMissLab / 一言諾科技有限公司
版本：Open Protocol Draft v0.1
類型：Agent 方法論 / 開源協議白皮書 / Reliability Layer / Trace-based Verification
日期：2026 7月

---

## 摘要

大型語言模型與 Agent 系統正在從「單次回答器」轉向「多步工作流執行器」。在這個轉換中，可靠性問題不再只是最後答案是否正確，而是整個 Agent 軌跡是否可追蹤、可回溯、可驗證、可修正。一次錯誤的計畫、一個不存在的檢索結果、一個被誤讀的工具回傳、一個未被標記的不確定推論，都可能沿著多步流程擴散，最終形成看似流暢但不可被信任的輸出。

本文提出 **VerifyLoop**：一套面向 Agent 工作流的雙向持續驗證與糾錯協議。VerifyLoop 不假設模型一次生成即可靠，而要求 Agent 對每次輸出保留任務鏈、推理鏈、證據鏈、工具鏈與版本鏈；並在輸出完成後，從結論反向檢查其必要前提、證據來源、工具記錄與任務目標是否一致。若正向生成鏈與反向驗證鏈不一致，系統不應直接輸出結論，而應標記 gap，分類錯誤來源，進入下一輪修正，或輸出「目前不可判定」。

VerifyLoop 的核心循環是：

```text id="onky9w"
Generate → Trace → Forward Check → Backward Check → Gap Diagnose → Correct → Version
```

本文將原始「雙向持續驗證糾錯系統」改寫為公開開源協議：不主張消除所有幻覺，不主張得到終極真理，而是提供一個可被不同 Agent 框架接入的可靠性層。它的目標是降低不可追蹤錯誤，提高輸出可審計性，讓 Agent 不只是會生成答案，也能留下自己如何抵達答案、哪些地方被驗證、哪些地方仍有缺口。

近期研究已顯示，Agent 幻覺與一般單輪回答幻覺不同，因為多步流程中的錯誤可能出現在 Planning、Retrieval、Reasoning、Human-Interaction、Tool-Use 等不同階段，且步驟級定位仍具挑戰；AgentHallu benchmark 報告的最佳模型步驟定位準確率仍有限，工具使用幻覺尤其難定位。這正好說明 Agent 可靠性需要工作流級 trace、gap attribution 與可審計驗證層。

---

## 關鍵詞

Agent、VerifyLoop、雙向驗證、持續糾錯、AI 幻覺、Agent 幻覺、RAG、Claim Verification、Tool Receipt、Trace-based Verification、Gap Diagnosis、Human-in-the-loop、Agent Reliability、開源協議

---

# 0. 開源定位聲明

## 0.1 本文是協議，不是封閉產品

VerifyLoop 不是單一產品，也不是特定模型、特定框架或特定供應商的功能。它是一個可以被不同 Agent 系統實作的工作流可靠性協議。

它可以被接入：

```text id="mz8cc7"
RAG 系統；
研究助理 Agent；
程式碼 Agent；
法律與政策分析 Agent；
資料分析 Agent；
瀏覽器操作 Agent；
知識庫維護 Agent；
多 Agent 協作系統。
```

VerifyLoop 的核心不是「讓模型變聰明」，而是讓 Agent 的輸出過程變得：

```text id="yu14dq"
可追蹤；
可回溯；
可驗證；
可修正；
可版本化；
可審計。
```

## 0.2 本文不主張

本文不主張：

```text id="f0sspf"
VerifyLoop 可以消除所有幻覺；
雙向驗證等於絕對真理；
Agent 可以完全不需要人類審查；
反向驗證一定正確；
多 Agent 檢查一定比單 Agent 可靠；
所有任務都值得高深度驗證；
所有知識都可以被完全形式化。
```

## 0.3 本文主張

本文主張：

```text id="f6rjhk"
Agent 的輸出應被視為一條可檢查的工作流，而不是孤立文字；
可靠性不只來自更大的模型，也來自更好的驗證結構；
正向生成與反向驗證可以互相暴露盲點；
工具調用、檢索結果與推理聲稱應被分離記錄；
當鏈條不能補完時，系統應輸出 gap，而不是假裝確定；
知識庫與 Agent 輸出應支援版本化更新。
```

---

# 1. 問題：Agent 不是一次回答器，而是多步工作流

傳統聊天機器人多半被理解為：

```text id="odfbj7"
Prompt → Answer
```

但 Agent 系統更接近：

```text id="82bbqm"
Task → Plan → Retrieve → Tool Use → Reason → Act → Observe → Revise → Answer
```

在這種多步流程中，錯誤可能出現在任何一個階段：

```text id="14q7ql"
計畫錯誤：Agent 設定了錯誤任務分解；
檢索錯誤：Agent 找到不相關或過期資料；
推理錯誤：Agent 從正確資料推出錯誤結論；
工具錯誤：Agent 聲稱使用工具，但工具未回傳該結果；
互動錯誤：Agent 誤解使用者意圖；
合成錯誤：Agent 把局部成立的資訊寫成全局結論。
```

AgentHallu 的分類也指出，Agent 幻覺需要按照工作流中的不同階段定位，而不是只看最終答案。其 benchmark 將幻覺分為 Planning、Retrieval、Reasoning、Human-Interaction、Tool-Use 等類型，並要求找出 responsible step 與 causal explanation。

因此，Agent reliability 的關鍵問題不再是：

```text id="pl8gjy"
答案對不對？
```

而是：

```text id="my5bs7"
這個答案是怎麼來的？
每一步是否有紀錄？
每個 claim 是否有 evidence？
工具聲稱是否有 receipt？
結論是否超出證據？
錯誤若發生，能否定位在哪一步？
```

這就是 VerifyLoop 的問題起點。

---

# 2. 從 Output-based AI 到 Trace-based Agent

## 2.1 Output-based AI 的限制

Output-based AI 只檢查最後輸出：

```text id="xj3x1a"
最後答案是否看起來合理；
語氣是否流暢；
格式是否符合需求；
引用是否存在；
結論是否有說服力。
```

但這種檢查很容易被流暢性欺騙。

一個答案可以語氣穩定、格式完整、推理看似自然，卻在中間某一步引用了錯誤資料、漏掉時間限定、虛構工具結果，或把推測寫成事實。

## 2.2 Trace-based Agent 的核心

Trace-based Agent 不只看最後答案，而是要求 Agent 留下工作軌跡：

```text id="jy6v91"
Task Trace：任務如何被理解；
Plan Trace：任務如何被拆解；
Evidence Trace：使用了哪些資料；
Tool Trace：調用了哪些工具，工具實際回傳什麼；
Claim Trace：最後輸出包含哪些可驗證聲稱；
Reasoning Trace：哪些推論是由哪些資料支持；
Correction Trace：哪些地方被修正；
Version Trace：不同版本之間差異在哪裡。
```

這些 trace 不一定要暴露模型私有思維鏈。VerifyLoop 不要求公開模型內部 chain-of-thought。它要求的是**可審計工作紀錄**，包括任務分解、引用、工具回傳、claim/evidence 對應、gap 報告與版本差異。

## 2.3 Trace 不是裝飾，而是可靠性基礎

沒有 trace，就無法知道錯在哪裡。

有 trace，才能做到：

```text id="37hchf"
錯誤定位；
局部修正；
責任分配；
版本比較；
自動回歸測試；
人類審查；
知識庫更新。
```

因此，VerifyLoop 的第一原則是：

> Agent 的輸出必須從「答案」升級為「答案 + 可審計軌跡」。

---

# 3. VerifyLoop 協議總覽

VerifyLoop 的基本循環如下：

```text id="syh36o"
1. Generate：生成初始答案或行動計畫
2. Trace：記錄任務、計畫、資料、工具、推理與輸出
3. Forward Check：檢查正向生成鏈是否連貫
4. Backward Check：從結論反推必要證據與前提
5. Gap Diagnose：定位不一致、跳步、缺證據或工具錯誤
6. Correct：自動修正、請求補資料、降級結論或交給人類
7. Version：保存修正後版本與差異
```

它可以被簡化為：

```text id="0w9xyi"
Answer is not final until it survives its own reverse check.
```

中文可表述為：

> 答案不能只被生成，還必須能從結論回扣到任務、證據與工具紀錄。

---

# 4. 正向鏈：Agent 如何產生答案

正向鏈描述 Agent 如何從任務走向輸出。

基本結構：

```text id="wbn77a"
User Task
→ Task Interpretation
→ Plan
→ Retrieval / Tool Use
→ Intermediate Notes
→ Reasoning / Synthesis
→ Final Answer
```

每一步都應產生可紀錄節點。

## 4.1 正向鏈節點

```yaml id="3rmqxz"
forward_chain:
  - node_id: S0
    type: user_task
    content: "使用者原始需求"
  - node_id: S1
    type: task_interpretation
    content: "Agent 對任務的理解"
  - node_id: S2
    type: plan
    content: "要查什麼、要算什麼、要調用什麼工具"
  - node_id: S3
    type: retrieval
    content: "檢索到的資料與來源"
  - node_id: S4
    type: tool_call
    content: "工具調用與回傳"
  - node_id: S5
    type: synthesis
    content: "由資料到結論的合成"
  - node_id: S6
    type: final_answer
    content: "最後輸出"
```

## 4.2 正向檢查項目

正向檢查不是判斷答案最終真假，而是檢查流程是否基本連貫：

```text id="vtq110"
任務理解是否偏離使用者需求；
計畫是否覆蓋任務；
檢索是否真的支撐計畫；
工具回傳是否被正確讀取；
推理是否跳過必要中間步；
最後答案是否超出前面資料。
```

---

# 5. 反向鏈：答案需要什麼才能成立

反向鏈從最後答案出發，追問：

```text id="csuwbg"
如果這個答案成立，它需要哪些前提？
如果這個 claim 成立，它需要哪些 evidence？
如果 Agent 聲稱用了工具，工具 receipt 是否存在？
如果結論包含比較，是否有完整比較集合？
如果結論包含時間判斷，時間限定是否明確？
```

反向鏈基本結構：

```text id="rtmv1g"
Final Answer
→ Claim Decomposition
→ Required Evidence
→ Evidence Availability
→ Tool Receipt Check
→ Task Alignment Check
→ Confidence / Gap Report
```

## 5.1 Claim Decomposition

最終答案必須拆成可驗證 claim。

例如：

```text id="9hrvol"
「埃菲爾鐵塔建於 1889 年，高 324 米，曾是世界最高建築。」
```

可拆成：

```yaml id="dptz6y"
claims:
  - claim_id: C1
    text: "埃菲爾鐵塔建於 1889 年"
    type: factual
  - claim_id: C2
    text: "埃菲爾鐵塔高度為 324 米"
    type: factual
  - claim_id: C3
    text: "埃菲爾鐵塔曾是世界最高建築"
    type: historical_comparison
```

若答案寫成：

```text id="xf2u5g"
「埃菲爾鐵塔是世界最高建築」
```

反向鏈會追問：

```text id="g8w7r7"
現在最高？
歷史上曾經最高？
比較集合是所有建築，還是當時建築？
資料時間點是何時？
```

這就是反向驗證的價值。

## 5.2 Evidence Requirement

每個 claim 都應標明需要哪種 evidence：

```yaml id="5hdv4l"
evidence_requirements:
  C1:
    required: ["historical_source"]
  C2:
    required: ["official_measurement_or_reliable_reference"]
  C3:
    required: ["historical_height_ranking", "time_range"]
```

## 5.3 Tool Receipt Check

如果 Agent 聲稱「我查詢了資料庫」「我讀取了檔案」「我執行了程式」，系統應檢查工具紀錄是否存在。

近年的 tool receipt 研究提出，Agent 可對工具執行產生不可由 LLM 偽造的簽名收據，再把 LLM 的聲稱與工具收據交叉檢查，以即時偵測虛構工具調用、錯報數量或把推論寫成事實等問題。

VerifyLoop 可將這個方向吸收為：

```text id="2twi75"
No tool claim without tool receipt.
```

中文：

> 沒有工具收據，就不能聲稱工具已經支持該結論。

---

# 6. 雙向一致性：Forward Chain 與 Backward Chain 的對接

VerifyLoop 不要求正向鏈與反向鏈字面相同，而要求它們在關鍵結構上相容。

## 6.1 一致性檢查項目

```text id="0p89k5"
Claim 是否能在正向鏈中找到來源；
Evidence 是否真的支持 claim；
Tool receipt 是否支持 Agent 的工具聲稱；
反向鏈要求的前提是否在正向鏈中出現；
最後答案是否引入了正向鏈沒有的外部假設；
是否存在循環論證；
是否存在結論強度超出證據強度。
```

## 6.2 一致性分數

VerifyLoop 可輸出一個非絕對的 verification score：

```yaml id="aamv6m"
verification_score:
  overall: 0.82
  task_alignment: 0.95
  claim_support: 0.80
  evidence_quality: 0.76
  tool_receipt_integrity: 1.00
  contradiction_check: 0.70
  uncertainty_handling: 0.85
```

這個分數不是「真理分數」，而是「目前 trace 下的可支持程度」。

---

# 7. Gap 三分法

當正向鏈與反向鏈不一致時，VerifyLoop 不應只說「錯了」，而應輸出 gap 類型。

## 7.1 Technical Gap

技術性斷鏈：

```text id="f4y6bu"
資料存在；
規則存在；
工具可用；
但 Agent 沒有查到、沒展開、沒引用、沒算完，或推理跳太快。
```

處理方式：

```text id="9be94c"
加深檢索；
展開中間步；
重新調用工具；
補充引理；
增加 claim-level verification；
生成更詳細版本。
```

## 7.2 Systemic Gap

系統性斷鏈：

```text id="g5omj8"
目前知識庫、工具、規則或任務設定不足以支持結論。
```

例子：

```text id="tmx9s4"
缺少即時資料；
缺少專業資料庫；
任務需要法律判斷但無司法管轄區；
任務需要實驗結果但目前沒有實驗；
Agent 缺少可執行工具。
```

處理方式：

```text id="gw8217"
請求新工具；
請求人類提供資料；
降低結論強度；
改成假設性回答；
輸出需要外部驗證。
```

## 7.3 Undecidable Gap

不可判定斷鏈：

```text id="xhpyc1"
在目前資料、工具與規則下，不能可靠回答。
```

處理方式：

```text id="t3fku2"
明確輸出不確定；
列出需要哪些資料才能回答；
避免假裝知道；
避免用流暢語氣掩蓋不可判定。
```

這是 VerifyLoop 的重要倫理點：

> 不可判定不是失敗。把不可判定說成確定，才是失敗。

---

# 8. 驗證深度 D

VerifyLoop 使用「驗證深度」表示不同任務需要不同程度的檢查。

## 8.1 深度分級

```text id="svmfzr"
D0：直接回答，不做額外驗證。
D1：基本自我一致性檢查。
D2：檢索佐證，補來源。
D3：拆成原子 claim，逐條驗證。
D4：多 Agent 或多路徑交叉驗證。
D5：工具 receipt + 版本紀錄 + 人類審查。
```

## 8.2 深度選擇原則

```text id="1e1rsw"
低風險、日常任務：D0-D1；
一般資訊查詢：D2；
研究、政策、法律、金融、醫療、工程：D3-D5；
高風險自動化執行：至少 D4，最好 D5；
不可逆行動：必須人類審查。
```

## 8.3 驗證深度不是越高越好

高驗證深度需要成本：

```text id="xn9xt8"
更多 token；
更多工具調用；
更多延遲；
更多工程複雜度；
更高假陽性可能；
更多人類審查成本。
```

因此 VerifyLoop 不追求所有任務都最大驗證，而是追求：

```text id="px3dh6"
任務風險 × 證據需求 × 成本限制
```

之間的動態平衡。

---

# 9. 系統模組設計

VerifyLoop 可拆成以下模組。

## 9.1 Trace Logger

紀錄整個 Agent 工作流。

```yaml id="wfzfps"
trace:
  trace_id: "vl_2026_0001"
  task_id: "task_001"
  agent_id: "agent_research_assistant"
  timestamp: "2026-07-01T00:00:00+08:00"
  steps:
    - step_id: S0
      type: user_task
      content: "..."
    - step_id: S1
      type: plan
      content: "..."
    - step_id: S2
      type: retrieval
      source_refs: ["src_001", "src_002"]
    - step_id: S3
      type: tool_call
      tool_receipt_id: "receipt_001"
    - step_id: S4
      type: synthesis
      content: "..."
```

## 9.2 Claim Decomposer

把輸出拆成可驗證聲稱。

```yaml id="kdd0bl"
claim:
  claim_id: C001
  text: "..."
  type: factual | comparative | causal | predictive | normative | speculative
  required_evidence:
    - source
    - tool_receipt
    - calculation
  risk_level: low | medium | high
```

## 9.3 Evidence Retriever

為每個 claim 尋找 evidence。

```yaml id="l2l3cx"
evidence:
  evidence_id: E001
  claim_id: C001
  source_type: document | web | database | tool_output | user_provided
  content_summary: "..."
  freshness: "current | stale | unknown"
  supports_claim: true
  confidence: 0.78
```

## 9.4 Tool Receipt Verifier

檢查工具聲稱是否被真實工具紀錄支持。

```yaml id="0ze80i"
tool_receipt:
  receipt_id: R001
  tool_name: "calculator"
  input_hash: "..."
  output_hash: "..."
  timestamp: "..."
  signed: true
  verified: true
```

## 9.5 Backward Verifier

從 claim 反推其必要支持條件。

```yaml id="22x3sg"
backward_check:
  claim_id: C001
  required_conditions:
    - "需要來源 A"
    - "需要時間限定"
    - "需要比較集合"
  matched_conditions:
    - "來源 A 已存在"
  missing_conditions:
    - "缺少比較集合"
  status: partial
```

## 9.6 Gap Classifier

分類 gap。

```yaml id="7w1mva"
gap:
  gap_id: G001
  claim_id: C001
  location: "final_answer.paragraph_2"
  type: technical | systemic | undecidable
  severity: low | medium | high
  explanation: "缺少支持該比較結論的完整排名資料"
  recommended_action: "retrieve_additional_evidence"
```

## 9.7 Correction Engine

根據 gap 類型採取修正。

```text id="7aalet"
Technical Gap → 補資料、補步驟、重跑工具。
Systemic Gap → 請求人類、要求新工具、降低結論。
Undecidable Gap → 明確輸出不確定。
```

## 9.8 Version Manager

保存版本差異。

```yaml id="yk720j"
version:
  version_id: V002
  parent_version: V001
  changes:
    - "將『是世界最高建築』改為『1889-1930 年曾為世界最高建築』"
    - "新增哈里發塔比較資料"
  verification_score_before: 0.42
  verification_score_after: 0.91
```

---

# 10. VerifyLoop JSON 規格草案

## 10.1 最小輸出格式

```json id="fhz9g3"
{
  "answer": "...",
  "verifyloop": {
    "trace_id": "vl_001",
    "verification_depth": "D3",
    "claims": [],
    "evidence": [],
    "tool_receipts": [],
    "gaps": [],
    "verification_score": {
      "overall": 0.0
    },
    "status": "verified | partial | corrected | uncertain | failed"
  }
}
```

## 10.2 Gap Report 格式

```json id="cs5664"
{
  "gap_id": "G001",
  "type": "technical",
  "severity": "medium",
  "location": {
    "claim_id": "C003",
    "answer_span": "paragraph_2_sentence_1"
  },
  "description": "The claim requires a time-bounded comparison but no comparison set was retrieved.",
  "required_action": "retrieve_comparison_data",
  "auto_correctable": true
}
```

## 10.3 Verification Report 格式

```json id="1q3dr5"
{
  "trace_id": "vl_001",
  "status": "corrected",
  "depth": "D3",
  "summary": "3 claims verified, 1 corrected, 0 unresolved.",
  "claim_results": [
    {
      "claim_id": "C001",
      "status": "supported",
      "confidence": 0.92
    },
    {
      "claim_id": "C002",
      "status": "corrected",
      "confidence": 0.88,
      "correction": "Added historical time range."
    }
  ],
  "remaining_gaps": []
}
```

---

# 11. 典型工作流

## 11.1 RAG 回答驗證

```text id="q09ndm"
1. 使用者提問；
2. Agent 檢索資料；
3. Agent 生成答案；
4. VerifyLoop 拆解 claim；
5. 每個 claim 對應 retrieval evidence；
6. 若 claim 無 evidence，標記 gap；
7. 若 evidence 矛盾，要求重新生成；
8. 輸出答案 + verification report。
```

MARCH 這類多 Agent 自檢框架已開始採用 claim-level decomposition 與資訊隔離檢查：Solver 先生成答案，Proposer 將回答拆成可驗證原子命題，Checker 在不看原始答案的情況下對 retrieved evidence 驗證，以降低 self-confirmation bias。VerifyLoop 可吸收這個精神，但把它一般化為開源 Agent 協議。

## 11.2 工具型 Agent 驗證

```text id="he4rir"
1. Agent 宣稱已查詢資料庫；
2. VerifyLoop 檢查 tool receipt；
3. 若沒有 receipt，禁止把結果寫成工具支持事實；
4. 若 receipt 存在，檢查輸出數值是否被正確引用；
5. 若 Agent 把推論寫成工具結果，標記 tool-use hallucination。
```

## 11.3 研究助理 Agent

```text id="f3wtym"
1. 輸入研究問題；
2. Agent 建立初步文獻地圖；
3. VerifyLoop 將每個研究主張拆成 claim；
4. 對每個 claim 檢查引用、年份、研究限制；
5. 對過時或未驗證 claim 加上 uncertainty label；
6. 生成可審計研究摘要。
```

## 11.4 知識庫批量更新

```text id="i76yr6"
1. 將既有文件拆成段落與 claim；
2. 為每個 claim 建立 evidence requirement；
3. 批量檢索或讀取來源；
4. 標記 supported / contradicted / stale / uncertain；
5. 自動提出修正草稿；
6. 保存版本差異；
7. 人類審查高風險修改。
```

---

# 12. 與既有研究的關係

## 12.1 Agent 幻覺歸因

AgentHallu 的研究方向說明，Agent 幻覺不應只在最終輸出層面處理，而應定位到多步軌跡中的 responsible step。VerifyLoop 的 Trace Logger、Gap Classifier 與 Backward Verifier 正是面向這類 step-level attribution 的協議化實作。

## 12.2 多 Agent 自檢

MARCH 顯示，多 Agent 分工、自我檢查與資訊隔離可以降低 verifier 的 confirmation bias。VerifyLoop 不限定一定要多 Agent，但在 D4 以上的驗證深度中，建議使用多 Agent 或多路徑檢查。

## 12.3 Tool Receipt

NabaOS / tool receipt 方向指出，互動式 Agent 不一定適合用高成本密碼學證明；較輕量的 tool execution receipt 加 claim cross-check 可能更實用。VerifyLoop 將 tool receipt 視為 Tool Trace 的關鍵證據層。

## 12.4 Agent 幻覺 Survey

LLM-based agents 的幻覺 survey 已整理出 agent workflow 中不同階段可能出現的幻覺與對應緩解方法，並指出多步代理系統的幻覺偵測與緩解是重要研究方向。VerifyLoop 可被視為一種 workflow-level mitigation protocol。

## 12.5 Embodied Agent 與不可行任務

具身 Agent 的幻覺研究也顯示，當任務與環境不一致時，Agent 可能仍嘗試執行不可能任務，而不是明確指出不可行。VerifyLoop 的 Undecidable / Systemic Gap 分類可用來要求 Agent 在任務不可行時輸出邊界，而不是繼續行動。

---

# 13. 開源實作路線

## 13.1 Repository 建議結構

```text id="qauou3"
verifyloop-agent/
  README.md
  LICENSE
  docs/
    protocol.md
    schemas.md
    examples.md
  schemas/
    trace.schema.json
    claim.schema.json
    evidence.schema.json
    tool_receipt.schema.json
    gap_report.schema.json
    verification_report.schema.json
  verifyloop/
    trace_logger.py
    claim_decomposer.py
    evidence_checker.py
    backward_verifier.py
    gap_classifier.py
    correction_engine.py
    version_manager.py
  examples/
    rag_verification/
    tool_receipt_check/
    knowledge_base_update/
    research_assistant/
  tests/
    test_gap_classifier.py
    test_claim_decomposer.py
    test_receipt_verifier.py
```

## 13.2 MVP 模組

第一版不需要做太大。MVP 只需要：

```text id="qx9uiv"
輸入：Agent final answer + retrieval sources + optional tool logs
輸出：
1. claim list
2. evidence mapping
3. unsupported claims
4. contradiction warnings
5. gap report
6. corrected draft
```

## 13.3 Minimal API

```python id="lvypoj"
from verifyloop import VerifyLoop

vl = VerifyLoop(depth="D3")

report = vl.verify(
    task=user_task,
    answer=agent_answer,
    sources=retrieved_sources,
    tool_logs=tool_logs
)

print(report.status)
print(report.gaps)
print(report.corrected_answer)
```

## 13.4 Integration Target

```text id="9hazuw"
LangChain / LangGraph；
LlamaIndex；
AutoGen；
CrewAI；
OpenAI-compatible tool-calling agents；
自製本地 Agent；
知識庫批量處理 pipeline。
```

---

# 14. 限制

## 14.1 VerifyLoop 不能保證終極正確

VerifyLoop 只能提高可追蹤性與可驗證性，不能保證所有結論絕對正確。

原因包括：

```text id="f24w7k"
知識庫可能錯；
資料可能過時；
檢索可能漏掉關鍵來源；
反向驗證器也可能推理錯；
多 Agent 可能共享同一偏差；
工具 receipt 只能證明工具回傳，不等於工具回傳本身正確；
高風險領域仍需專家審查。
```

## 14.2 Trace 不是私有思維鏈

VerifyLoop 不要求暴露模型私有 chain-of-thought。

它要求的是：

```text id="mylm1m"
任務紀錄；
工具紀錄；
資料紀錄；
claim/evidence 對應；
gap 報告；
版本差異。
```

這些是可審計工作產物，不是模型內部思考逐字稿。

## 14.3 高驗證深度有成本

VerifyLoop 必須允許不同模式：

```text id="nz00i3"
Fast Mode：快速、不完全驗證；
Standard Mode：基本檢索與 claim check；
Strict Mode：逐 claim 驗證與 tool receipt；
Audit Mode：多 Agent + 人類審查 + 版本化。
```

---

# 15. 結論：Agent 的下一步不是更會生成，而是更會驗證

生成能力已經足夠強。問題是：生成之後，誰來檢查？如何檢查？錯在哪裡？怎麼修正？如何避免同一錯誤在下一輪再次出現？

VerifyLoop 的答案是：

```text id="17nqey"
不要只看答案。
看 trace。

不要只做正向生成。
做反向驗證。

不要只說錯了。
定位 gap。

不要只修一次。
保留版本，持續修正。

不要假裝確定。
在不可判定時輸出不可判定。
```

VerifyLoop 的核心並不是讓 Agent 永不犯錯，而是讓錯誤變得可見、可定位、可修正、可累積學習。

Agent 的下一階段，不只是更強的生成，而是更可靠的工作流。

一句話總結：

> VerifyLoop 是一套開源 Agent 驗證協議：它要求 Agent 不只生成答案，還要留下正向生成鏈、反向驗證鏈、證據紀錄、工具紀錄與 gap 診斷，並在不一致時進入持續修正循環。

---

# 附錄 A：術語表

| 術語                 | 定義                  |
| ------------------ | ------------------- |
| Forward Chain      | Agent 從任務到答案的生成軌跡   |
| Backward Chain     | 從答案反推必要證據與前提的驗證軌跡   |
| Trace              | 任務、計畫、工具、資料、推理與版本紀錄 |
| Claim              | 最終答案中的可驗證聲稱         |
| Evidence           | 支持或反駁 claim 的資料     |
| Tool Receipt       | 工具執行紀錄或簽名收據         |
| Gap                | 正向鏈與反向鏈不一致或缺失之處     |
| Technical Gap      | 資料或規則存在，但未展開或未查到    |
| Systemic Gap       | 目前工具、資料或規則不足        |
| Undecidable Gap    | 在目前條件下不可判定          |
| Verification Depth | 驗證深度，從 D0 到 D5      |
| Version Trace      | 修正前後版本差異紀錄          |

---

# 附錄 B：狀態碼

```text id="lhj1mw"
VERIFIED：所有主要 claim 已被支持。
PARTIAL：部分 claim 被支持，部分仍有 gap。
CORRECTED：原答案已被修正。
UNCERTAIN：目前資料不足，無法可靠回答。
FAILED：驗證失敗，答案不應輸出。
HUMAN_REVIEW_REQUIRED：需要人類審查。
```

---

# 附錄 C：最小 Gap 分類器邏輯

```python id="tp9cq6"
def classify_gap(claim, evidence, tool_receipts, task_context):
    if claim.requires_tool and not tool_receipts.exists_for(claim):
        return "technical", "Missing tool receipt"

    if claim.requires_current_data and not evidence.has_current_source():
        return "systemic", "Current data unavailable"

    if evidence.contradicts(claim):
        return "technical", "Contradicted by retrieved evidence"

    if claim.is_high_risk and evidence.is_insufficient():
        return "undecidable", "Insufficient evidence for high-risk claim"

    if claim.exceeds_task_scope(task_context):
        return "technical", "Conclusion exceeds task scope"

    return "supported", "No obvious gap"
```

---

# 附錄 D：README 短版

```markdown id="iucc7k"
# VerifyLoop Agent Protocol

VerifyLoop is an open protocol for trace-based verification of LLM agents.

It turns an agent answer into:

- forward chain
- backward verification chain
- claim list
- evidence map
- tool receipt check
- gap report
- corrected version

Core loop:

Generate → Trace → Forward Check → Backward Check → Gap Diagnose → Correct → Version

VerifyLoop does not guarantee absolute truth.
It improves auditability, error localization, and iterative correction.
```

---

# 附錄 E：公開版邊界聲明

本文由內部理論「萬物雙向持續驗證糾錯系統」降維改寫而來。原始版本包含更強的知識演化、本體論與算力深度敘述；公開版刻意將其改寫為 Agent 協議與開源方法論。本文不主張真理可被完全驗證，而主張 Agent 的輸出應具有可審計軌跡、雙向檢查與持續修正能力。

---

**全文完。**
