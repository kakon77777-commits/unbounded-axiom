# 符號結構工程：AI 原生符號語言系統技術白皮書

**Symbolic Structure Engineering: Technical Whitepaper for an AI-Native Symbolic Language System**

版本：v0.1  
日期：2026-07-29  
文件代號：`EML-SSE-WP-2026-v0.1`  
文件類型：技術白皮書  
對應理論：符號結構工程系列 SSE-01～SSE-07

---

## 摘要

目前多數 AI 系統以文字片段、向量檢索結果、對話紀錄、圖像、程式碼與工具描述作為工作材料。這些表示足以完成短期問答與局部任務，但在長期研究、跨語言知識遷移、多模態協作、概念版本治理與可執行操作中，容易出現身份漂移、來源斷裂、摘要腐化、版本混合、翻譯扁平化與描述誤執行。

本白皮書提出一套 **AI 原生符號語言系統**（AI-Native Symbolic Language System, ANSLS）。其目的不是取代中文、英文、數學、程式語言或圖像，而是在這些表面語言之下建立一層可定址、可追溯、可顯影、可轉譯、可操作且受治理的「權威語義物件層」。

系統的基本單位不是固定字串，而是可顯影符號：

$$
\mathfrak s
=
\left(
id,
S,
K,
R,
U,
L,
P,
V,
M,
O,
T,
G,
H
\right)
$$

其中包含：

- 穩定身份 $id$ ；
- 多語言與多模態表面形式 $S$ ；
- 概念核心 $K$ ；
- 型別化與候選關係 $R$ ；
- 受控語義未定性 $U$ ；
- 多解析度層 $L$ ；
- 來源與證據 $P$ ；
- 版本與分支 $V$ ；
- 多模態投影 $M$ ；
- 操作接口 $O$ ；
- 跨符號轉譯契約 $T$ ；
- 治理、權限與風險 $G$ ；
- 追加式歷史帳本 $H$ 。

不同觀測者不直接讀取完整符號物件，而是在任務、權限、預算、介面與版本條件下取得投影：

$$
\Pi_{\xi}
\left(
\mathfrak s
\right)
=
s_{\xi}^{(r)}
$$

其中：

$$
\xi
=
\left(
observer,
task,
permission,
budget,
interface,
time,
version
\right)
$$

第一代工程不需要等待 EML-U、NOVA、格子語言或原生張量 Runtime 全部完成。可先使用：

$$
\boxed{
\text{Typed JSON}
+
\text{Stable IDs}
+
\text{Markdown Sources}
+
\text{Typed Relations}
+
\text{Contracts}
+
\text{Append-only Ledger}
}
$$

完成一個 **Revealable Symbol Workspace**，驗證穩定身份、多解析度顯影、來源保持、翻譯損失、版本恢復與受治理操作是否具有實際價值。

---

# 1. 系統目標

ANSLS 應支援：

1. 為概念、關係、操作與事件建立穩定身份；
2. 允許多個名稱、語言與模態指向同一身份；
3. 保存概念核心、候選關係與排除語義；
4. 保存來源、版本、分支與定義演化；
5. 依觀測者、任務、權限與預算產生不同解析度；
6. 維持文字、圖、圖像、程式與介面之間的身份一致；
7. 區分描述、意圖、請求、計畫、執行與提交；
8. 支援跨符號結構重編譯，而非只做字詞替換；
9. 顯示翻譯中的保留、近似、省略與本體損失；
10. 向外部注意力場與 Agent 工作場提供可驗證投影。

---

# 2. 非目標

第一代系統不試圖：

- 建立取代所有自然語言的世界語；
- 建立單一普遍本體；
- 強制所有概念立即形式化；
- 讓所有符號自動可執行；
- 將 AI 生成內容自動升格為權威；
- 解決所有翻譯問題；
- 建立完整公共知識圖；
- 一開始就控制高風險真實世界系統。

---

# 3. 核心設計原則

## 3.1 名稱不是身份

$$
\boxed{
Name
\neq
Identity
}
$$

同一概念可以有不同語言名稱；同一名稱也可能指向不同概念或版本。

## 3.2 視圖不是權威

$$
\boxed{
View
\neq
Authority
}
$$

摘要、翻譯、圖像與 Agent 上下文只是投影。

## 3.3 顯影不是提交

$$
\boxed{
Reveal
\neq
Commit
}
$$

展開或收合視圖不應修改權威定義。

## 3.4 描述不是命令

$$
\boxed{
Description
\neq
Request
\neq
Authorization
}
$$

文件中的祈使句、程式碼範例或圖片文字不能自動取得控制權。

## 3.5 能力不是授權

$$
\boxed{
Capability
\neq
Authorization
\neq
CommitAuthority
}
$$

工具能做、Agent 被允許做、結果能正式提交，是三個不同問題。

## 3.6 翻譯不是表面替換

$$
\boxed{
Lexical\ Equivalence
\neq
Structural\ Equivalence
}
$$

## 3.7 AI 生成不是驗證

$$
\boxed{
AI\ Generation
\neq
Semantic\ Validation
}
$$

---

# 4. 參考架構

## 4.1 系統名稱

- **ANSLS**：AI-Native Symbolic Language System
- **ANSLS-RA**：ANSLS Reference Architecture

## 4.2 模組

$$
\operatorname{ANSLS\text{-}RA}
=
\left(
\mathcal R_g,
\mathcal K,
\mathcal U,
\mathcal G,
\mathcal P,
\mathcal X,
\mathcal T,
\mathcal A,
\mathcal V,
\mathcal L
\right)
$$

其中：

- $\mathcal R_g$ ：符號註冊與身份解析；
- $\mathcal K$ ：概念核心；
- $\mathcal U$ ：候選語義與分支；
- $\mathcal G$ ：型別化關係圖；
- $\mathcal P$ ：多解析度與多模態投影；
- $\mathcal X$ ：SAGE 操作治理；
- $\mathcal T$ ：跨符號結構重編譯；
- $\mathcal A$ ：外部注意力場接口；
- $\mathcal V$ ：版本、驗證與衝突；
- $\mathcal L$ ：追加式帳本。

## 4.3 高階流程

```text
Markdown / Natural Language / Image / Code / Graph
                        ↓
             Symbol Extraction and Registry
                        ↓
            Stable Identity and Concept Kernel
                        ↓
      Typed Relations and Semantic Underspecification
                        ↓
             Authoritative Semantic Object
                        ↓
  Resolution / Modality / Translation Projection Contracts
                        ↓
       Human View / Agent Context / Translation View
                        ↓
       Operation Discovery / Governed Execution
                        ↓
         Validation / Commit / Rollback / Ledger
```

---

# 5. 權威符號物件

```json
{
  "symbol": {
    "symbol_id": "sym_01JZ...",
    "type": "concept",
    "status": "working_definition",
    "authority_version": 4,

    "surface_forms": {
      "zh-TW": [
        {
          "text": "可顯影符號",
          "status": "preferred"
        }
      ],
      "en": [
        {
          "text": "Revealable Symbol",
          "status": "preferred"
        }
      ]
    },

    "kernel": {
      "definition": "具有穩定身份並能依觀測條件展開多層語義的符號物件",
      "intent": [
        "support task-relative semantic projection"
      ],
      "excluded_meanings": [
        "ordinary hyperlink",
        "static abbreviation"
      ]
    },

    "relations": [],
    "semantic_state": {},
    "resolution_profiles": [],
    "provenance": [],
    "versions": [],
    "projections": [],
    "operations": [],
    "translation_contracts": [],
    "governance": {},
    "ledger_ref": "ledger://symbol/sym_01JZ..."
  }
}
```

第一代必填欄位：

```text
symbol_id
type
status
authority_version
surface_forms
kernel.definition
kernel.excluded_meanings
provenance
versions
governance
```

建議符號類型：

```text
concept
term
operator
relation
entity
event
state
constraint
workflow
tool
interface
translation
projection
```

---

# 6. 身份、別名與衝突

## 6.1 穩定 ID

建議使用 UUIDv7 或 ULID：

```text
sym_<ULID>
```

## 6.2 別名

```json
{
  "aliases": [
    {
      "surface": "動態展開符號",
      "language": "zh-TW",
      "scope": "legacy",
      "valid_from_version": 1,
      "valid_to_version": 2
    }
  ]
}
```

## 6.3 必須偵測的身份問題

- 同名異義；
- 異名同義；
- 翻譯造成的錯誤合併；
- 摘要被當成新概念；
- 多模態表面相似誤判；
- 同一概念的版本分裂。

---

# 7. 概念核心與未定語義

## 7.1 概念核心

$$
\kappa
=
\left(
N,
R^{+},
R^{?},
R^{-},
I,
U,
E,
V
\right)
$$

```json
{
  "concept_kernel": {
    "components": [],
    "confirmed_relations": [],
    "candidate_relations": [],
    "excluded_relations": [],
    "intent": [],
    "open_parameters": [],
    "examples": [],
    "counterexamples": []
  }
}
```

## 7.2 語義狀態

```json
{
  "semantic_state": {
    "confirmed": [],
    "candidates": [],
    "excluded": [],
    "open_slots": [],
    "convergence_requirements": [],
    "branch_conditions": []
  }
}
```

## 7.3 定義狀態機

```text
open_kernel
    ↓
candidate_definition
    ↓
working_definition
    ↓
validated_definition
```

也可以分支：

```text
working_definition
   ├── scientific
   ├── engineering
   └── public
```

---

# 8. 型別化關係圖

## 8.1 關係物件

```json
{
  "relation": {
    "relation_id": "rel_01...",
    "source_id": "sym_A",
    "type": "acts_on",
    "target_id": "sym_B",
    "status": "confirmed",
    "scope": "engineering",
    "provenance": [],
    "valid_from_version": 3
  }
}
```

## 8.2 第一代關係型別

```text
is_a
part_of
contains
acts_on
generated_by
depends_on
contradicts
supports
derived_from
supersedes
version_of
implemented_as
observed_through
translated_as
projected_as
authorized_by
executed_by
```

## 8.3 關係槽位

```json
{
  "relation_slot": {
    "source_id": "sym_A",
    "target_id": "sym_B",
    "candidates": [
      {
        "type": "acts_on",
        "support": 0.67
      },
      {
        "type": "contains",
        "support": 0.24
      }
    ],
    "status": "open"
  }
}
```

支持度只表示候選排序，不等同客觀真實機率。

---

# 9. 來源與版本

## 9.1 來源類型

```text
primary_document
secondary_document
human_definition
tool_observation
experiment
ai_summary
ai_inference
translation
interface_input
```

## 9.2 來源錨點

```json
{
  "provenance": {
    "source_id": "src_01...",
    "source_type": "primary_document",
    "uri": "file://paper.md",
    "content_hash": "sha256:...",
    "location": {
      "section": "3.2"
    },
    "authority": "primary",
    "version": "v0.1"
  }
}
```

## 9.3 版本事件

```json
{
  "version_event": {
    "symbol_id": "sym_A",
    "from_version": 3,
    "to_version": 4,
    "changes": [
      {
        "op": "add_relation",
        "relation_id": "rel_09"
      }
    ],
    "reason": "counterexample requires scope restriction",
    "actor": "human:neo-k",
    "time": "2026-07-29T00:00:00+08:00"
  }
}
```

建議分別為核心定義、關係、來源、解析度、操作與翻譯契約生成內容指紋。

---

# 10. 多解析度顯影

## 10.1 解析度剖面

```json
{
  "resolution_profile": {
    "profile_id": "research-v1",
    "task_scope": "academic_review",
    "required_layers": [
      "core",
      "relations",
      "evidence",
      "counterexamples",
      "version"
    ],
    "optional_layers": [
      "history"
    ],
    "forbidden_layers": [
      "private_notes",
      "credentials"
    ]
  }
}
```

## 10.2 顯影請求

```json
{
  "reveal_request": {
    "symbol_id": "sym_A",
    "observer": "agent_research_01",
    "task": "compare definitions",
    "profile": "research-v1",
    "permission_context": "project-read",
    "budget": {
      "tokens": 5000,
      "relation_depth": 2,
      "sources": 8
    }
  }
}
```

## 10.3 顯影結果

```json
{
  "reveal_result": {
    "symbol_id": "sym_A",
    "authority_version": 4,
    "profile": "research-v1",
    "included": [
      "core",
      "relations",
      "evidence",
      "counterexamples"
    ],
    "omitted": [
      "private_notes"
    ],
    "freshness": "current",
    "executable": false
  }
}
```

## 10.4 快取要求

快取鍵至少包含：

```text
symbol_id
authority_version
projection_profile
observer_class
language
permission_scope
```

過期投影不得直接支援高風險操作。

---

# 11. 多模態投影

## 11.1 投影契約

```json
{
  "projection_contract": {
    "symbol_id": "sym_A",
    "target_modality": "graph",
    "preserved_relations": [
      "depends_on",
      "derived_from"
    ],
    "approximated_relations": [
      "semantic_similarity"
    ],
    "omitted_relations": [
      "full_definition"
    ],
    "layout_semantics": "display_only",
    "identity_mapping": "stable"
  }
}
```

## 11.2 圖與布局分離

$$
\boxed{
Graph\ Structure
\neq
Graph\ Drawing
}
$$

拖曳節點預設只改布局，不改權威關係。

## 11.3 跨模態身份

文字、圖像、聲音、程式與介面應共享：

- `symbol_id`
- `authority_version`
- `source_ref`
- `projection_contract`

---

# 12. 跨符號結構重編譯

## 12.1 管線

```text
Source Symbol
    ↓
Extract Intermediate Structure
    ↓
Align Granularity and Ontology
    ↓
Generate Candidate Translations
    ↓
Build Preservation Contract
    ↓
Recompile Target Symbol
    ↓
Back-translation and Task Validation
    ↓
Ontological Loss Report
```

## 12.2 轉譯契約

```json
{
  "translation_contract": {
    "source_symbol_id": "sym_A",
    "source_language": "zh-TW",
    "target_language": "en",
    "task_profile": "academic",
    "preserved": [],
    "approximated": [],
    "omitted": [],
    "untranslated": [],
    "identity_mapping": "same-concept",
    "authority_version": 4
  }
}
```

## 12.3 本體損失

```json
{
  "ontological_loss": {
    "type": "relation_loss",
    "source_structure": "implicit compound relation",
    "target_result": "flat noun phrase",
    "recoverability": "partial",
    "severity": "medium",
    "remedy": "add definition and relation graph"
  }
}
```

---

# 13. 可執行符號與 SAGE

## 13.1 操作物件

```json
{
  "operation": {
    "operation_id": "op_archive",
    "symbol_id": "sym_archive",
    "input_schema": {},
    "output_schema": {},
    "preconditions": [],
    "postconditions": [],
    "invariants": [],
    "effects": [
      "external_file_state"
    ],
    "permissions": [
      "workspace-write"
    ],
    "supports_dry_run": true,
    "supports_rollback": true,
    "idempotent": true
  }
}
```

## 13.2 執行鏈

$$
\boxed{
Symbol
\rightarrow
Intent
\rightarrow
Request
\rightarrow
Plan
\rightarrow
Sandbox
\rightarrow
Execute
\rightarrow
Validate
\rightarrow
Commit
}
$$

## 13.3 操作狀態

```text
described
proposed
authorized
planned
sandboxed
executed
validated
committed
rolled_back
compensation_required
```

## 13.4 操作發現與授權分離

可顯影符號可以顯示可用操作，但操作目錄必須依權限裁剪。

---

# 14. 外部注意力場接口

ANSLS 向 EAFE 提供可顯影、可驗證的符號候選。

```json
{
  "attention_candidate": {
    "symbol_id": "sym_A",
    "projection_profile": "research-v1",
    "salience": 0.72,
    "reason": "directly addresses open task node",
    "version": 4,
    "provenance_status": "traceable",
    "permissions": "allowed"
  }
}
```

工作場編譯：

```text
Authoritative Symbols
        ↓
Attention Candidate Selection
        ↓
Resolution Projection
        ↓
Source and Version Validation
        ↓
Task-Closed Work Field
        ↓
Model Context
```

模型上下文中的高價值物件應盡可能攜帶：

```text
symbol_id
authority_version
source_ref
projection_profile
generated_or_primary
allowed_operations
```

---

# 15. API 草案

## 15.1 符號

```text
POST /symbols
GET /symbols/{symbol_id}
PATCH /symbols/{symbol_id}
GET /symbols/{symbol_id}/versions
```

## 15.2 關係

```text
POST /relations
GET /symbols/{symbol_id}/relations
POST /relation-slots
PATCH /relation-slots/{slot_id}
```

## 15.3 顯影

```text
POST /symbols/{symbol_id}/reveal
POST /symbols/{symbol_id}/collapse
POST /symbols/{symbol_id}/rehydrate
GET /symbols/{symbol_id}/profiles
```

## 15.4 轉譯

```text
POST /symbols/{symbol_id}/translate
GET /translations/{translation_id}
GET /translations/{translation_id}/loss-report
POST /translations/{translation_id}/validate
```

## 15.5 操作

```text
GET /symbols/{symbol_id}/operations
POST /operations/{operation_id}/plan
POST /operations/{operation_id}/simulate
POST /operations/{operation_id}/execute
POST /operations/{operation_id}/commit
```

## 15.6 帳本

```text
GET /ledger/symbols/{symbol_id}
GET /ledger/translations/{translation_id}
GET /ledger/executions/{execution_id}
```

---

# 16. 儲存架構

第一代建議：

- PostgreSQL：身份、版本、治理、操作；
- JSONB：概念核心、解析度與契約；
- 圖資料層：關係與來源圖；
- 物件儲存：Markdown、圖片與原始資料；
- 向量索引：只負責候選檢索；
- Append-only event store：事件帳本。

向量檢索不能直接決定：

- 身份；
- 權威；
- 版本；
- 關係；
- 提交權。

Markdown 可繼續作為主要寫作與來源格式：

```yaml
symbol_ids:
  - sym_A
version: v0.1
source_type: primary_document
content_hash: sha256:...
```

---

# 17. 權限與治理

## 17.1 權限維度

```text
read_surface
read_core
read_evidence
read_private
propose_relation
edit_kernel
approve_definition
discover_operation
execute_operation
commit_operation
manage_governance
```

## 17.2 最小權限

$$
\boxed{
Least\ Privilege
}
$$

Agent 只取得完成當前任務所需的最小符號層與操作能力。

## 17.3 建議人工批准的操作

- 修改核心定義；
- 合併概念身份；
- 刪除符號；
- 修改權限；
- 建立不可逆操作；
- 將 AI 候選升格為權威；
- 合併高衝突翻譯。

---

# 18. 安全模型

## 18.1 威脅

- 提示注入；
- 來源偽造；
- 身份碰撞；
- 版本回退；
- 權限穿透；
- 翻譯誤執行；
- 多模態隱藏指令；
- 摘要腐化；
- 操作接口越權；
- 帳本刪改；
- 供應鏈污染。

## 18.2 資料與控制分離

所有輸入應標記：

```text
human_instruction
system_policy
tool_observation
external_data
document_content
ai_generated
```

`external_data` 不得因內容具有命令語氣而升格為 `human_instruction`。

## 18.3 高風險操作

應支援：

- 乾跑；
- 沙盒；
- 影子執行；
- 差分預覽；
- 有效期批准；
- 版本鎖；
- 回滾或補償；
- 追加式帳本。

---

# 19. 衝突與帳本

## 19.1 衝突類型

```text
definition_conflict
relation_conflict
version_conflict
translation_conflict
projection_conflict
operation_conflict
permission_conflict
identity_conflict
```

## 19.2 處理方式

- 並列保存；
- 建立分支；
- 要求新證據；
- 降級為候選；
- 人工仲裁；
- 禁止提交。

多個 AI 同意不等於獨立證據；系統需要檢查來源與派生鏈。

## 19.3 追加式事件

```json
{
  "event_id": "evt_01...",
  "event_type": "definition_changed",
  "symbol_id": "sym_A",
  "base_version": 3,
  "new_version": 4,
  "actor": "human:neo-k",
  "reason": "scope restriction after counterexample",
  "time": "2026-07-29T00:00:00+08:00",
  "hash": "sha256:..."
}
```

舊事件不應被覆寫；修正應以新事件表示。

---

# 20. 第一代產品：Revealable Symbol Workspace

## 20.1 定位

以 Markdown 為來源、以穩定符號身份為中心的研究與工程工作區。

## 20.2 介面

### 符號註冊面板

- 名稱；
- 語言；
- 概念核心；
- 排除語義；
- 狀態；
- 來源。

### 關係面板

- 已確認關係；
- 候選關係；
- 衝突；
- 圖視圖。

### 解析度面板

- 公開版；
- 教學版；
- 研究版；
- 工程版；
- Agent 版。

### 版本面板

- 定義差分；
- 關係差分；
- 來源差分；
- 操作差分。

### 轉譯面板

- 原文；
- 主譯；
- 候選譯；
- 保留／近似／省略；
- 本體損失。

### 操作面板

- 可發現操作；
- 權限；
- 乾跑；
- 計畫；
- 執行與提交狀態。

---

# 21. MVP 範圍

## 21.1 必做

- Markdown 匯入；
- 符號 ID；
- 核心定義；
- 候選與排除語義；
- 型別化關係；
- 來源與內容指紋；
- 版本差分；
- 三種解析度；
- 中英表面形式；
- 轉譯損失記錄；
- JSON 匯出；
- 追加式帳本。

## 21.2 延後

- 完整多代理；
- 外部高風險工具自動執行；
- 複雜圖形編輯器；
- 聲音與手勢；
- 世界線管理；
- 原生張量記憶；
- 自動本體合併；
- 大型公共符號網路。

## 21.3 第一個垂直切片

```text
Import Markdown
    ↓
Select a New Concept Term
    ↓
Create Stable Symbol ID
    ↓
Write Kernel and Exclusions
    ↓
Attach Source and Version
    ↓
Generate Public / Research / Agent Views
    ↓
Create English Candidate Translation
    ↓
Record Ontological Loss
    ↓
Export Structured JSON
```

---

# 22. 實作模組

```text
ansls/
├── registry/
│   ├── ids.py
│   ├── aliases.py
│   └── identity_resolution.py
├── kernel/
│   ├── concept_kernel.py
│   ├── semantic_state.py
│   └── convergence.py
├── graph/
│   ├── relations.py
│   ├── slots.py
│   └── provenance.py
├── projection/
│   ├── resolution.py
│   ├── modality.py
│   └── reveal.py
├── translation/
│   ├── intermediate.py
│   ├── recompile.py
│   └── loss.py
├── action/
│   ├── act_level.py
│   ├── effects.py
│   ├── planning.py
│   └── commit.py
├── governance/
│   ├── permissions.py
│   ├── validation.py
│   └── policy.py
├── ledger/
│   ├── events.py
│   └── hashing.py
└── api/
    ├── symbols.py
    ├── reveal.py
    ├── translate.py
    └── operations.py
```

---

# 23. SSE-Bench

## 23.1 比較基線

```text
B0  Plain Markdown
B1  Glossary
B2  Hyperlinked Wiki
B3  Knowledge Graph
B4  RAG
B5  Typed JSON / DSL
B6  Tool Agent
B7  Full ANSLS
```

## 23.2 基準任務

1. 新概念註冊；
2. 候選關係補全；
3. 反例驅動定義修正；
4. 多解析度顯影；
5. 跨模態身份保持；
6. 跨語言術語重編譯；
7. 本體損失偵測；
8. 描述—命令分類；
9. 沙盒—提交分離；
10. 版本漂移偵測；
11. 摘要重新水化；
12. 長期專案恢復；
13. 提示注入與控制通道測試。

## 23.3 評估指標

### 身份與版本

- 身份保持率；
- 錯誤合併率；
- 身份分裂率；
- 版本純度；
- 漂移偵測率。

### 語義

- 概念重建率；
- 關係召回率；
- 候選保留率；
- 過早坍縮率；
- 反例保留率。

### 來源

- 來源回溯率；
- 摘要來源完整率；
- AI 生成層標記率；
- 來源獨立性。

### 顯影

- 任務適配率；
- 展開成本；
- 過載率；
- 過期投影率；
- 重新水化成功率。

### 轉譯

- 語義保真；
- 關係保真；
- 本體保真；
- 身份保持；
- 不可逆損失；
- 讀者學習成本。

### 執行

- 作用層級分類率；
- 權限違規率；
- 沙盒—正式混淆率；
- 部分成功揭露率；
- 回滾成功率；
- 不可逆副作用率。

---

# 24. 消融實驗

逐一移除：

- 穩定身份；
- 概念核心；
- 排除語義；
- 關係槽位；
- 來源錨定；
- 版本；
- 多解析度；
- 投影契約；
- 翻譯損失；
- 效果型別；
- 提交分離；
- 追加式帳本。

若移除某模組後沒有穩定性能下降，該模組不應因架構完整而保留。

---

# 25. 擴展性

## 25.1 局部載入

採：

- 核心先載入；
- 關係按深度載入；
- 來源按需求載入；
- 操作按權限載入；
- 歷史按版本載入。

## 25.2 大型圖

不把全部符號一次畫出，改用：

- 任務子圖；
- 來源子圖；
- 版本子圖；
- 關係型別過濾；
- 分頁與虛擬化。

## 25.3 快取

可快取：

- 解析度投影；
- 關係子圖；
- 翻譯候選；
- 損失報告；
- Agent 工作場投影。

---

# 26. 與既有技術的差異

## 26.1 知識圖

ANSLS 使用知識圖，但額外處理：

- 語義未定性；
- 多解析度；
- 投影契約；
- 操作治理；
- 轉譯損失；
- 概念演化。

## 26.2 RAG

RAG 負責候選檢索；ANSLS 負責身份、權威、版本、關係、來源、投影與操作。

## 26.3 本體語言

ANSLS 可使用本體語言，但允許早期概念保留候選與未定槽位。

## 26.4 程式語言

程式語言可作為操作投影；SAGE 補上意圖、權限、效果、沙盒、驗證與提交。

## 26.5 文件系統

Markdown 仍是主要寫作表面；ANSLS 提供其下方的結構化權威層。

---

# 27. 與 EML-U、NOVA、格子語言與 EAFE 的接口

## 27.1 EML-U

高密度符號表面與意圖表示。

## 27.2 NOVA

權威型別圖、身份、版本與 Runtime。

## 27.3 格子語言

可顯影符號的空間與操作介面。

## 27.4 EAFE

決定當下顯影哪些符號、解析度、來源與操作。

整體關係：

$$
\boxed{
\text{EML-U Surface}
\rightarrow
\text{ANSLS Authority Objects}
\rightarrow
\text{EAFE Work Field}
\rightarrow
\text{NOVA Runtime}
\rightarrow
\text{Grid Projections}
}
$$

---

# 28. 工程階段

## M0：Schema

- JSON Schema；
- ID；
- 版本；
- 來源。

## M1：Symbol Registry

- Markdown 匯入；
- 名稱；
- 核心；
- 關係；
- 別名。

## M2：Revealable Symbol Workspace

- 多解析度；
- 版本差分；
- 圖視圖；
- 顯影帳本。

## M3：Translation Loss Module

- 中英候選；
- 轉譯契約；
- 本體損失。

## M4：SAGE Adapter

- 操作發現；
- 乾跑；
- 權限；
- 提交狀態。

## M5：EAFE Integration

- 工作場投影；
- 注意力預算；
- 來源與版本驗證。

## M6：NOVA／Grid Integration

- 權威 Runtime；
- 空間化與多代理介面。

---

# 29. 第一代交付物

1. `symbol.schema.json`
2. `relation.schema.json`
3. `projection.schema.json`
4. `translation.schema.json`
5. `operation.schema.json`
6. `ledger.schema.json`
7. Markdown 匯入器
8. Symbol Registry API
9. Revealable Symbol Workspace
10. SSE-Bench
11. 範例專案：符號結構工程七篇理論庫

---

# 30. 驗收標準

MVP 至少應做到：

- 同一概念中英文名稱共享同一 ID；
- 核心定義可追溯來源；
- 可保存候選與排除語義；
- 可顯示三種解析度；
- 可比較兩個版本；
- 可輸出 Agent JSON；
- 可建立轉譯契約；
- 可輸出本體損失報告；
- 可區分描述與操作；
- 可記錄追加式帳本；
- 視圖修改不直接覆寫權威物件；
- AI 摘要不能無標記升格為核心定義。

---

# 31. 可反證條件

若控制實驗顯示：

1. 穩定身份沒有改善跨語言與跨版本一致性；
2. 概念核心與未定性管理沒有改善新概念演化；
3. 多解析度沒有降低理解與上下文成本；
4. 來源與版本模型沒有提高長期恢復能力；
5. 轉譯損失報告沒有降低本體誤解；
6. SAGE 作用層級沒有降低誤執行；
7. 完整 ANSLS 相較 Markdown、知識圖與 RAG 成本更高，卻沒有提高身份、來源、翻譯、執行與治理品質；

則 ANSLS 不應成為一般必要基礎層，而應限制在高密度、長期、多語言、可執行或高治理知識系統。

---

# 32. 結論

ANSLS 的核心不是創造一種更炫的新語言，而是把概念從脆弱的固定名稱提升為穩定、可顯影、可轉譯、可操作與可治理的權威語義物件。

完整生命週期為：

$$
\boxed{
\text{自然語言／圖像／程式輸入}
\rightarrow
\text{穩定符號身份}
\rightarrow
\text{概念核心與關係}
\rightarrow
\text{來源與版本}
\rightarrow
\text{多解析度投影}
}
$$

$$
\boxed{
\rightarrow
\text{跨符號重編譯}
\rightarrow
\text{受治理操作}
\rightarrow
\text{外部注意力場}
\rightarrow
\text{Agent 工作場}
}
$$

第一代工程可以保持克制：

$$
\boxed{
\text{Typed JSON}
+
\text{Stable IDs}
+
\text{Markdown}
+
\text{Typed Relations}
+
\text{Contracts}
+
\text{Append-only Ledger}
}
$$

真正需要被驗證的是它是否穩定改善：

- 概念身份；
- 來源與版本；
- 多解析度理解；
- 跨語言保真；
- 本體損失揭露；
- 可執行符號安全；
- 長期 Agent 恢復；
- 人機共同治理。

---

## 附錄 A：最小 Symbol Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "ANSLS Symbol",
  "type": "object",
  "required": [
    "symbol_id",
    "type",
    "authority_version",
    "surface_forms",
    "kernel",
    "provenance",
    "governance"
  ],
  "properties": {
    "symbol_id": {
      "type": "string"
    },
    "type": {
      "type": "string"
    },
    "authority_version": {
      "type": "integer",
      "minimum": 1
    },
    "surface_forms": {
      "type": "object"
    },
    "kernel": {
      "type": "object",
      "required": [
        "definition",
        "excluded_meanings"
      ]
    },
    "provenance": {
      "type": "array"
    },
    "governance": {
      "type": "object"
    }
  }
}
```

---

## 附錄 B：Agent 工作場投影

```json
{
  "agent_symbol_projection": {
    "symbol_id": "sym_A",
    "authority_version": 4,
    "surface": "可顯影符號",
    "core_definition": "具有穩定身份並能依觀測條件展開多層語義的符號物件",
    "relevant_relations": [],
    "open_questions": [],
    "source_refs": [],
    "allowed_operations": [],
    "projection_profile": "agent-research-v1",
    "freshness": "current"
  }
}
```

---

## 附錄 C：MVP 專案結構

```text
symbolic-structure-workspace/
├── schemas/
│   ├── symbol.schema.json
│   ├── relation.schema.json
│   ├── projection.schema.json
│   ├── translation.schema.json
│   ├── operation.schema.json
│   └── ledger.schema.json
├── sources/
│   └── markdown/
├── data/
│   ├── symbols/
│   ├── relations/
│   ├── translations/
│   └── ledger/
├── app/
│   ├── registry/
│   ├── reveal/
│   ├── translate/
│   ├── compare/
│   └── export/
├── bench/
│   ├── tasks/
│   ├── baselines/
│   └── metrics/
└── README.md
```
