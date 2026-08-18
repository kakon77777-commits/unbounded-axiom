# Game Intelligence Archaeology v0.2

這一版把 v0.1 的 Markdown 研究矩陣轉成可讓多 AI / Agent 共用的機器可讀格式。

## 核心檔案

- `game_intelligence_archaeology_research_unit_v0.2.schema.json`
  - 一個研究單元的 JSON Schema。
  - 單位為：
    `Game × Version × Platform × Subsystem × Behavior`.

- `taxonomy_v0.2.json`
  - 固定研究深度、Evidence Type、Composition Relation、Intelligence Branch。

- `examples_v0.2.json`
  - 三個完整 seed records：
    - Spore
    - Majesty Gold HD
    - OpenTTD blind→source calibration

- `examples_v0.2.jsonl`
  - 同一批範例的 JSONL 版本，方便批次 Agent ingestion。

- `blank_record_template_v0.2.json`
  - 空白模板。

- `validate_records.py`
  - 使用 `jsonschema` 驗證單筆 JSON 或 JSONL。

## 核心規則

### 1. 不允許把猜測升格成事實

機制欄位使用：
- `documented`
- `observed`
- `inferred`
- `reconstructed`
- `validated`
- `unknown`

並保留 `confidence`。

### 2. Unknown 是合法值

資料不完整時不要求 Agent 補齊不存在的答案。

### 3. 一款遊戲不是一筆資料

一款遊戲應產生多個 research units，例如：

```text
rimworld:...:job_selection:interrupt_fire
rimworld:...:storyteller:raid_pacing
rimworld:...:needs:mood_break
```

### 4. Evidence 與 Claim 分離

每筆 Evidence 都有 `evidence_id`。
機制假說用 `evidence_ids` 引用證據。

### 5. 研究經濟學直接內建

每筆研究單元保留：
- acquisition cost
- setup cost
- time to trigger
- observability
- reproducibility
- tooling friction
- version entropy

因此後續可直接自動排 priority。

### 6. 公開與內部分層

`publication` 區塊區分：
- `internal_raw`
- `derived_public_safe`
- `legal_notes`

避免未來資料庫把內部 raw research 與公開衍生知識混在一起。

## 建議下一步 v0.3

直接建立第一批 30 款遊戲的 `L0` seed records，然後讓 AI 自動計算：

```text
coverage gap
research cost
expected information gain
direct project relevance
```

再排序出第一輪真正值得深挖的 8–12 款。
