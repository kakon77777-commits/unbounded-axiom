# Structured Scholarly Source Protocol（SSSP）v0.1 技術白皮書

## AI 原生學術來源、交易式寫入、驗證與 MCP 介面

**狀態：** Experimental / MVP Specification  
**版本：** v0.1  
**日期：** 2026-08-12  
**核心原則：** Source First / Rendered View Is Not Source

---

## 摘要

大型語言模型已能高速產生長篇論文、數學公式、技術白皮書與跨文件研究系列，但目前常見的聊天式寫作流程通常把「渲染畫面」同時當成閱讀介面與正式原稿。當公式經過 Markdown、KaTeX／MathJax、HTML DOM、clipboard、Unicode escape、再序列化與本地修復器等多個轉換層時，畫面上正確的內容可能在複製後發生字元級、結構級甚至靜默語義級損毀。

本白皮書以實際累積的公式損毀案例為需求基礎，包括：DOM 複製造成 LaTeX delimiters 損毀、渲染後公式被重複或攤平、`$` 同時作為貨幣與數學定界符、雙套數學方言造成解析歧義、單一 delimiter 缺失導致級聯失效、修復 regex 誤傷合法 `\`、控制字元吞噬 `\a \b \f \n \r \t \v` 類 LaTeX 指令，以及「renderer 0 error 但數學語意已改變」的 silent corruption。

本文提出 **Structured Scholarly Source Protocol（SSSP）**：一套把正式學術內容從聊天渲染介面中抽離，以 typed node、canonical source、optimistic concurrency、transactional mutation、provenance、Semantic Ledger、Claim Ledger 與多層 validator 為核心的 AI-native scholarly authoring protocol。

SSSP 將系統拆成三層：

1. **Canonical Format Layer**：定義正式 source 的 typed document model；
2. **Mutation Protocol Layer**：定義 AI 如何最小化、可驗證地修改文件；
3. **Adapter Layer**：第一個實作使用 Model Context Protocol（MCP），但 SSSP 不與 MCP 綁死。

MVP 不試圖建立完整數學 AST。數學內容先以 raw LaTeX field 保存，由 server serializer 負責 JSON escaping；Markdown／HTML／LaTeX／PDF 均視為衍生 view，不得反向成為 canonical source。MVP 提供：`create_document`、`append_node`、`replace_node`、`read_node`、`validate_document`、`export_document`、`commit_version` 七個 primitive，並以 SHA-256 node checksum、document revision、atomic write 與 validator 阻止大部分已知格式損毀進入 corpus。

---

# 1. 問題定義

## 1.1 當前工作流的根本錯誤

常見流程是：

```text
AI 對話生成
→ UI 渲染 Markdown/LaTeX
→ 使用者從畫面複製
→ Clipboard/DOM 轉換
→ 儲存成 Markdown
→ 本地 renderer 報錯
→ regex / AI 修復
→ 再渲染
→ 回歸修復
```

這是一條 **render-first, repair-later** 流程。

SSSP 改成：

```text
Human/AI discussion
→ structured mutation request
→ canonical source
→ validation
→ atomic commit
→ derived rendering/export
```

即：

```text
Canonical Source → Validation → Rendered Views
```

而不是：

```text
Rendered View → Copy → Guess Original Source
```

---

## 1.2 Rendered-Source Divergence（RSD）

定義 **Rendered-Source Divergence**：

> 當使用者看到的渲染表示，與後續機器處理所需的 canonical source 不再具有可靠可逆映射，且經 DOM、clipboard、escape、parser 或格式轉換後，無法保證 source identity 時，即發生 RSD。

典型案例：

- `\[ ... \]` 複製後收尾只剩裸 `]`；
- `_` 變 `\_`；
- `}_{` 變成其他 markdown 字元組合；
- inline math wrapper 消失；
- 同一公式被複製成「攤平文字 + LaTeX + 攤平文字」三份；
- LaTeX 被替換成 Unicode rendered glyphs；
- 下標、框線只殘留 zero-width／PUA 標記。

SSSP 的核心設計不是「更強地修 RSD」，而是讓 canonical source 永遠不經過 RSD 路徑。

---

## 1.3 Silent Semantic Divergence（SSD）

比 RSD 更危險的是 **Silent Semantic Divergence**：

> 內容已發生數學或邏輯語義改變，但 parser／renderer 仍接受輸入，因此傳統 syntax validation 無法發現。

例如某些上游流程錯誤套用 C/Python 風格 `unicode_escape`，可能把 `\neg` 的 `\n` 解碼成真正換行，後續剩下 `eg`；KaTeX 可能仍把 `eg` 當變數字串渲染，因此「0 render errors」不等於語義未受損。

因此：

```text
Renderer Pass ≠ Semantic Integrity
```

SSSP validator 必須至少分成 Syntax、Render、Semantic-Risk 三層。

---

# 2. 設計目標

SSSP v0.1 的主要目標：

1. **Source First**：渲染畫面永遠不是 canonical source。
2. **Error Locality**：單一公式或節點錯誤不得吞掉後續整篇文件。
3. **Minimal Mutation**：AI 修改節點，不重新生成整篇文件。
4. **Typed Content**：paragraph、math、claim、definition 等具有不同型別。
5. **Single Canonical Math Representation**：canonical math node 不使用 Markdown ` $...$ ` delimiter。
6. **Atomic Commit**：驗證失敗不得產生半完成寫入。
7. **Optimistic Concurrency**：多 AI／多對話不能靜默覆寫彼此修改。
8. **Provenance**：核心定義、claim 與節點需要來源與版本記錄。
9. **Derived Views Only**：Markdown、HTML、PDF 等由 source 編譯，不反向同步。
10. **Protocol Independence**：SSSP core 不依賴 MCP；MCP 只是 adapter。

非目標：

- v0.1 不建立完整數學語義 AST；
- v0.1 不自動證明公式數學正確；
- v0.1 不取代 Git；
- v0.1 不直接解決引用真實性與學術審查；
- v0.1 不嘗試把所有 legacy Markdown 自動無損轉換。

---

# 3. 系統分層

```text
┌─────────────────────────────────────┐
│ Human / AI Discussion Layer         │
│  brainstorming / dialogue / review  │
└────────────────┬────────────────────┘
                 │ commit intent
┌────────────────▼────────────────────┐
│ SSSP Mutation Protocol              │
│ typed operations / revision / tx    │
└────────────────┬────────────────────┘
                 │
┌────────────────▼────────────────────┐
│ Canonical Scholarly Source          │
│ document.json + ledgers + versions  │
└────────────────┬────────────────────┘
                 │
┌────────────────▼────────────────────┐
│ Validator Pipeline                  │
│ L1 syntax / L2 render / L3 risk     │
└────────────────┬────────────────────┘
                 │
┌────────────────▼────────────────────┐
│ Export Compiler                     │
│ Markdown / LaTeX / HTML / PDF       │
└─────────────────────────────────────┘
```

Adapter 可為：

```text
MCP / CLI / REST / local API / future agent protocol
```

---

# 4. Canonical Document Model

## 4.1 Document

第一版 canonical document：

```json
{
  "protocol": "SSSP",
  "version": "0.1",
  "document_id": "paper-001",
  "title": "Example Paper",
  "revision": 3,
  "created_at": "...",
  "updated_at": "...",
  "nodes": [],
  "semantic_ledger": {},
  "claim_ledger": {}
}
```

所有寫入由 server 產生合法 JSON。AI 不應要求使用者手工複製整份 JSON。

---

## 4.2 Typed Nodes

MVP 支援：

```text
heading
paragraph
math_block
definition
claim
code
reference
note
```

一般 node：

```json
{
  "id": "node-0004",
  "type": "paragraph",
  "content": "...",
  "checksum": "sha256:...",
  "created_at": "...",
  "updated_at": "...",
  "provenance": {
    "actor": "assistant",
    "reason": "initial draft"
  }
}
```

數學 node：

```json
{
  "id": "eq-0001",
  "type": "math_block",
  "latex": "\\forall x\\in X,\\;P(x)",
  "checksum": "sha256:..."
}
```

注意 canonical source 中 **沒有 `$$` delimiter**。Delimiter 只由 exporter 生成。

---

# 5. Semantic Ledger

Semantic Ledger 用於保存跨篇或跨版本需要保持一致的語義狀態。

```json
{
  "terms": {
    "CPRR": {
      "canonical": "Content-Phase Relay Resolution",
      "status": "active"
    }
  },
  "deprecated_terms": {
    "RelayPhase Resolution": {
      "replacement": "CPRR"
    }
  },
  "symbols": {
    "\\mathfrak{B}": "Computational Substrate"
  }
}
```

目的：

- 防止同概念跨篇改名；
- 防止 deprecated term 復活；
- 防止同一符號跨章多義；
- 讓 AI 寫作前先取得 canonical definitions。

---

# 6. Claim Ledger

Claim Ledger 與正文分開，追蹤論述 epistemic status：

```json
{
  "claim-0042": {
    "type": "conjecture",
    "status": "provisional",
    "text": "...",
    "support": ["paper-03#node-42"],
    "provenance": "discussion-2026-08-12"
  }
}
```

MVP claim types：

```text
definition
observation
inference
conjecture
theorem
engineering_hypothesis
empirical_result
```

這能避免 AI 在多輪改寫中把：

```text
猜想 → 工作假說 → 已證明定理
```

無意間「升級」。

---

# 7. Mutation Protocol

## 7.1 原則

正式文件不得以「整篇重新輸出」作為一般修改方式。

核心 primitive：

```text
create_document
append_node
replace_node
read_node
validate_document
export_document
commit_version
```

之後可擴充：

```text
insert_node
move_node
delete_node
update_semantic_ledger
update_claim
begin_transaction
commit_transaction
rollback_transaction
```

---

## 7.2 Optimistic Concurrency

每份文件包含：

```text
revision = N
```

mutation request 可指定：

```text
expected_revision = N
```

若 server 目前已為：

```text
revision = N + 1
```

則拒絕：

```text
REVISION_CONFLICT
```

這是避免十幾個 AI 對話／Agent 同時修改同一文件時靜默覆寫的第一道保護。

---

## 7.3 Node checksum

每個 node 依 canonical JSON content 計算 SHA-256：

```text
checksum(node) = SHA256(canonical-json(node-without-checksum))
```

`replace_node` 可額外帶：

```text
expected_checksum
```

若 node 已改變，server 拒絕 stale write。

---

# 8. Transaction Semantics

MVP 每一個 mutation 本身以 atomic file replacement 實現 mini-transaction：

```text
read current
→ apply change in memory
→ validate candidate
→ write temp file
→ fsync/close
→ atomic replace
```

完整多節點 transaction 留到 v0.2：

```text
BEGIN
replace definition
replace equation
update claim ledger
validate
COMMIT
```

任何一步失敗：

```text
ROLLBACK
```

---

# 9. Validator Pipeline

## 9.1 L1 — Structural / Character Validation

必做：

- UTF-8；
- document schema；
- node ID uniqueness；
- required fields；
- control characters；
- PUA characters；
- zero-width markers；
- LaTeX braces rough balance；
- environment balance；
- forbidden escape-corruption signatures；
- duplicate node IDs；
- checksum integrity。

對 `math_block`，canonical format 不再使用 `$` delimiter，因此可整類移除：

- 貨幣 `$` vs math `$` ambiguity；
- inline delimiter 邊界 tokenizer 規則；
- missing `$` 吃掉後續段落的級聯模式。

---

## 9.2 L2 — Renderer Validation

MVP 以 MathJax TeX parser 實際解析所有 math nodes。

目的不是證明數學正確，而是抓：

- unknown command；
- malformed group；
- environment error；
- parser-level TeX defect。

Exporter 再跑 Markdown target validation 可作 v0.2。

---

## 9.3 L3 — Semantic-Risk Validation

v0.1 不使用大型模型做 semantic proof，而先做 risk flag：

- math node 修改比例極高；
- `\neg` 類 operator 突然消失；
- relation operator 數量大幅改變；
- 數學 node 變成純字母文本；
- source 出現 PUA／zero-width；
- legacy import 中公式數量異常下降。

結果：

```text
PASS
WARNING_SEMANTIC_REVIEW
FAIL
```

未來可接 AI semantic diff：

```text
old mathematical meaning
vs
new mathematical meaning
```

但 AI semantic check 不能取代 deterministic validation。

---

# 10. Source vs Derived Views

SSSP 規定：

```text
Canonical source → exporter → Markdown / LaTeX / HTML / PDF
```

每個 export metadata 可包含：

```json
{
  "source_revision": 12,
  "source_hash": "...",
  "compiler": "sssp-md-exporter/0.1"
}
```

衍生 `.md` 若人工修改，不自動 merge 回 canonical source。

這是一條單向資料流。

---

# 11. Prompt Contract

在任何支援 SSSP 的 AI session 中，建議加入：

```text
SSSP AUTHORING CONTRACT

1. Chat output is discussion/view, not canonical scholarly source.
2. Never ask the user to copy rendered math back into source.
3. Commit formal content through SSSP mutation tools.
4. Prefer minimal node mutation over full-document regeneration.
5. Preserve canonical terminology from Semantic Ledger.
6. Preserve epistemic status from Claim Ledger.
7. Do not convert raw LaTeX into Unicode-rendered approximation.
8. Do not run unicode_escape or equivalent escape-decoding round trips.
9. A renderer pass is not proof of semantic integrity.
10. A mutation is complete only after validation succeeds.
```

對話可自由；commit 要嚴格。

---

# 12. MCP Adapter

SSSP core 與 MCP 分離。

```text
SSSP Core
 ├─ storage
 ├─ mutation
 ├─ validation
 ├─ versioning
 └─ export

Adapters
 ├─ MCP
 ├─ CLI
 ├─ REST (future)
 └─ other agent protocols (future)
```

MCP 適合 MVP，因為它提供標準化 client/server lifecycle、resources 與 model-controlled tools；stdio transport 使用逐行 UTF-8 JSON-RPC，可直接作本地 Agent integration。

SSSP-MCP v0.1 只宣告 `tools` capability。

---

# 13. MCP Tool Surface v0.1

## `sssp.create_document`

建立空白 canonical document。

輸入：

```json
{
  "document_id": "paper-001",
  "title": "..."
}
```

## `sssp.append_node`

新增 typed node。

## `sssp.replace_node`

以 expected revision/checksum 做安全替換。

## `sssp.read_node`

讀 canonical node。

## `sssp.validate_document`

執行 L1/L2/L3-risk validation。

## `sssp.export_document`

產生 derived Markdown。

## `sssp.commit_version`

建立 immutable version snapshot。

---

# 14. MCP 安全模型

MCP Tools 是 model-controlled action，因此 SSSP server 必須：

- 所有 document ID 限制在 configured root；
- 防 path traversal；
- 驗證所有 input；
- mutation 留 audit record；
- 遠端 transport 未來必須加 auth；
- MVP 先 stdio，避免開放 network surface；
- 不讓 tool 直接執行任意 shell；
- exporter 只能寫在 document workspace。

對高風險 mutation，可由 host UI 增加 human confirmation。

---

# 15. 目錄結構

```text
data/
  paper-001/
    document.json
    versions/
      000001_<hash>.json
    exports/
      paper-001_r1.md
    audit.jsonl
```

Canonical truth：

```text
document.json
```

不是 export。

---

# 16. Export 規則 v0.1

`heading`：

```markdown
## heading content
```

`paragraph`：原樣文本。

`math_block`：

```markdown
$$
<latex>
$$
```

`definition`：使用標題 + 內容。

`claim`：使用 claim type/status metadata 產生可讀 Markdown。

`code`：fenced code。

因此 `$` delimiter 只在 compiler/exporter 中由單一實作生成，AI 不需要自己管理 delimiter 配對。

---

# 17. Legacy Import

舊 Markdown 是高風險來源。

SSSP v0.1 不宣稱自動完整修復 legacy corpus。

建議流程：

```text
legacy .md
→ detection
→ parse candidates
→ quarantine suspicious nodes
→ AI/manual repair
→ SSSP canonical import
→ validation
```

一旦轉入 canonical SSSP 後，不再回到 repair-centered workflow。

---

# 18. 實驗設計

第一個實驗不測「AI 寫得比較好」，只測格式可靠性。

## Experiment A — Roundtrip Integrity

對 1000 個包含：

- `\boxed`
- `\forall`
- `\neg`
- `\nabla`
- `\text`
- `\rightarrow`
- `\varnothing`
- `\begin{aligned}`
- 貨幣 `$`

的節點進行：

```text
create → serialize → load → export → render
```

要求 canonical hash 完全一致。

## Experiment B — Concurrent Mutation

兩個 client 同時持有 revision N。

A commit 成功後 B 用 N 寫入，必須得到 revision conflict。

## Experiment C — Known Damage Regression

把既有 A–J 損毀案例轉成 regression fixtures。

目標：

```text
known silent corruption cannot enter canonical document unnoticed
```

## Experiment D — Minimal Mutation

比較：

```text
full paper regeneration
vs
node replacement
```

的非目標字元變動數量。

---

# 19. 成功指標

SSSP MVP 第一階段不追求 fancy UI。

核心 KPI：

```text
Canonical corruption rate
Validation recall on known damage cases
False positive rate
Non-target mutation size
Revision conflict correctness
Roundtrip source hash stability
Export reproducibility
```

第一階段最重要的是：

```text
新產生的正式論文不再需要後端 AI 大規模修公式。
```

---

# 20. Roadmap

## v0.1 — Source-first MCP MVP

- typed JSON source；
- seven tools；
- SHA-256；
- revision；
- atomic write；
- L1 validator；
- MathJax L2 validator；
- Markdown exporter；
- snapshot versioning。

## v0.2 — Ledgers & Transactions

- dedicated Semantic Ledger tools；
- Claim Ledger tools；
- multi-node transactions；
- richer provenance；
- resource exposure via MCP。

## v0.3 — Semantic Diff

- AI-assisted semantic comparison；
- theorem/claim status preservation；
- cross-node symbol consistency；
- bibliography validation hooks。

## v0.5 — Structured Mathematics

- partial math AST for high-risk primitives；
- renderer-independent operators；
- AST → LaTeX compiler。

## v1.0 — AI-Native Scholarly Authoring Protocol

- multi-agent concurrency；
- signed commits；
- reproducible publication bundles；
- provenance graph；
- schema migration；
- multiple adapters。

---

# 21. 核心命題

SSSP 的最核心主張不是：

```text
Markdown 很差。
```

而是：

```text
Human-readable rendering and machine-canonical scholarly source
should not be the same mutable object.
```

Markdown 仍然非常適合閱讀、Git diff 與發布。

真正的改變是：

```text
Markdown becomes a compiled view.
```

而不是唯一 source of truth。

---

# 22. 結論

AI 時代學術寫作的瓶頸正在從「能不能快速生成文字」轉向「快速生成後，內容能否以可靠、可追蹤、可重用的形式沉澱」。

如果正式內容仍經過：

```text
render → copy → escape → repair
```

生成速度越快，只會把更多後處理債務推給本地 Agent。

SSSP 的方向是反過來：

```text
Discussion is ephemeral.
Canonical source is structured.
Mutations are transactional.
Validation happens before commit.
Rendering is derived.
```

最終目標不是讓 AI 更會「修壞掉的論文」，而是讓新論文從生成的第一刻起，就不進入那條會損毀的資料路徑。

---

## 參考規格與需求來源

1. Model Context Protocol Specification, revision 2025-11-25：Base Protocol、Lifecycle、stdio/Streamable HTTP、Tools。
2. JSON-RPC 2.0 Specification。
3. CommonMark 0.31.2 Specification，特別是 backslash escapes、characters、inline/block parsing。
4. 使用者提供：《數學公式常見損毀模式 — 為新格式設計準備的問題目錄》，作為本白皮書的主要 failure corpus 與工程需求來源。

