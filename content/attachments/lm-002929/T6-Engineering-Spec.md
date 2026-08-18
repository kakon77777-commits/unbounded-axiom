# T6：Dynamic Logic Schema Pack
## Claim / Evidence / Judgment / Event / Policy / Live Paper Manifest

**版本：** v0.1  
**日期：** 2026-08-16  
**格式：** JSON Schema Draft 2020-12

---

# 一、目的

本文件把前面 T1–T5 的概念從文字規格進一步落成機器可驗證 schema。

本包包含：

```text
schemas/
├─ claim.schema.json
├─ evidence.schema.json
├─ judgment-state.schema.json
├─ event.schema.json
├─ policy.schema.json
└─ live-paper-manifest.schema.json
```

核心原則：

$$
\boxed{
\text{先定型別，再讓 AI 填內容。}
}
$$

---

# 二、Claim

Claim 是被判斷對象。

必要欄位：

```text
id
statement
created_at
```

不得把 current judgment 直接寫進 Claim。

因此：

$$
\boxed{
\text{Claim}
\neq
\text{Judgment}.
}
$$

---

# 三、Evidence

Evidence 必須帶：

```text
claim_id
direction
source_type
observed_at
```

其中：

```text
source_type = inference
```

是合法的，但不得假裝：

```text
source_type = observation
```

這直接落實：

$$
\boxed{
\text{推論不能偽裝成證據。}
}
$$

---

# 四、Judgment State

第一版狀態：

```text
open
generating
conflicted
provisionally_true
provisionally_false
```

runtime status：

```text
ok
blocked
error
```

兩者分開。

因此 schema 本身阻止：

$$
\Omega=\mathrm{ERROR}
$$

這種型別混淆。

---

# 五、Event

Event 是 event-sourced runtime 的 canonical transition input。

必須包含：

```text
event_id
sequence
type
claim_id
timestamp
runtime_version
payload
```

sequence 建議 workspace／stream 內單調。

---

# 六、Model Output

LLM output 不要求每次 replay 重新生成。

當某輸出被 system 接納進判斷流程，寫入：

```text
MODEL_OUTPUT_COMMITTED
```

其 payload 可保存：

```text
provider
model
model_version
prompt_hash
output
output_hash
```

---

# 七、Policy

Closure／reopen policy 不應硬編碼在 UI。

Policy schema 抽出：

```text
support_threshold
oppose_threshold
min_evidence_completeness
max_counterpressure_for_support
reopen_threshold
```

這使不同研究域可使用不同政策。

---

# 八、Manifest

Live Paper manifest 確認：

```text
format: eve-live-paper
canonical_encoding: utf-8
runtime.dynamic_logic: true
runtime.aimdc: true
```

並固定 math delimiter 規則。

---

# 九、驗證層級

至少：

```text
L0 JSON parse
L1 JSON Schema
L2 cross-reference
L3 graph consistency
L4 replay consistency
```

JSON Schema 只完成前兩層的一部分。

---

# 十、Cross-reference

例如 Evidence：

```text
claim_id
```

必須存在於 claims。

JSON Schema 本身不保證跨檔 referential integrity。

需 Runtime validator。

---

# 十一、Event Sequence

Validator 應拒絕：

```text
sequence: 5
sequence: 4
```

逆序提交。

除非使用多 stream 架構並有明確 merge protocol。

---

# 十二、Projection Validation

若：

```text
state: provisionally_true
```

則：

```text
projection_3
```

應為：

```text
true
```

可由 deterministic validator 強制。

---

# 十三、Schema Versioning

每個 persisted object 應最終補：

```text
schema_version
```

v0.1 先以 runtime manifest 統一管理也可。

---

# 十四、Migration

若：

$$
Schema_{0.1}\rightarrow Schema_{0.2},
$$

必須提供 migration。

不得 silently reinterpret 舊 event。

---

# 十五、AI Structured Output

LLM 可被要求直接輸出符合 schema 的 JSON。

但：

$$
\boxed{
\text{LLM says valid}
\neq
\text{schema validated}.
}
$$

一定再由 deterministic validator 驗證。

---

# 十六、EveGlyph 接法

T2 中新增：

```text
src/dynamiclogic/
```

可以由：

```text
schema registry
```

載入本包 schema。

解析後才允許：

```text
commit event
```

---

# 十七、最小 Data Flow

$$
\text{AI / Human Input}
\rightarrow
\text{JSON}
\rightarrow
\text{Schema Validate}
\rightarrow
\text{Cross Validate}
\rightarrow
\text{Commit Event}
\rightarrow
\text{Reduce}
\rightarrow
\text{Render}.
$$

---

# 十八、最終原則

$$
\boxed{
\text{生成可以自由，
提交必須有型別。}
}
$$

這正是可不可論在工程上的一個最小投影。
