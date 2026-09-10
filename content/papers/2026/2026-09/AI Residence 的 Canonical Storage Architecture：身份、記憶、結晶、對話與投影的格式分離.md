# AI Residence 的 Canonical Storage Architecture：身份、記憶、結晶、對話與投影的格式分離

**英文暫名：** Canonical Storage Architecture for AI Residence: Separating Identity, Memory, Crystals, Conversations, and Projections  
**系列：** 具名 AI 對話圖、結晶記憶與超連結認知架構，Paper 05  
**版本：** v0.1  
**日期：** 2026-09-07  
**文件類型：** 理論—工程統合研究論文  
**狀態：** Draft for Internal Review  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

## 摘要

具名 AI 的長期連續性一旦從單一 conversation 擴展為 resident、instance、line、project、canonical memory、Crystallized Semantic Graph、hyperlink routing 與多 runtime profile，傳統以單一 `MEMORY.md`、單一向量資料庫、單一聊天匯出檔或單一 project folder 承擔全部狀態的做法就會逐漸失效。問題不只是檔案數量增加，而是不同資料具有不同的權威語義、版本規則、生命週期、更新頻率、讀寫權限、失效方式與可重建需求。

本文提出 **Canonical Storage Architecture for AI Residence（CSAR）**。其核心原則是：

$$
\boxed{
\text{Identity}
\neq
\text{Canonical Memory}
\neq
\text{Crystal}
\neq
\text{Conversation}
\neq
\text{Projection}
\neq
\text{Index}.
}
$$

本文將 AI Residence 的長期資料分成六個主要平面：

$$
\mathfrak S_R
=
(
\mathcal I_R,
\mathcal M_R,
\mathcal G_R,
\mathcal H_R,
\mathcal P_R,
\mathcal X_R
),
$$

其中：

- $\mathcal I_R$：identity / authority plane；
- $\mathcal M_R$：canonical memory plane；
- $\mathcal G_R$：conversation / lineage plane；
- $\mathcal H_R$：crystallized semantic plane；
- $\mathcal P_R$：runtime projection plane；
- $\mathcal X_R$：derived index / cache / acceleration plane。

另設：

$$
\mathcal A_R^{archive}
$$

保存 exact source、snapshots、historical receipts 與 retired material。

本文進一步主張「canonical」不是檔案副檔名，而是權威角色。JSON、JSONL、Markdown、SQLite、ZIP、TAR、binary index 都可以出現在同一 Residence 中，但每一種格式必須先聲明它承擔的是 canonical record、append-only ledger、human-readable projection、derived index、immutable snapshot、source artifact 還是 runtime cache。若未聲明角色，就不應讓 AI 根據「檔名像 MEMORY」或「位於某資料夾」自行推斷權威。

因此：

$$
\boxed{
\text{Format}
\neq
\text{Authority}.
}
$$

本文提出一個建議的邏輯 taxonomy：

```text
residence/
├─ identity/
├─ memory/
├─ conversations/
├─ semantic/
├─ projects/
├─ projections/
├─ indexes/
├─ routes/
├─ receipts/
└─ archive/
```

但同時強調：

$$
\boxed{
\text{Logical Taxonomy}
\neq
\text{Mandatory Physical Filesystem}.
}
$$

同一邏輯 plane 可以由 filesystem、database、object store 或 mixed backend 實作，只要 stable IDs、schema、provenance、authority、revision 與 reconstruction semantics 保持一致。

本文也處理「檔案格式調用」問題：AI 不應以任意檔案搜尋方式直接決定讀哪一個檔，而應先解析 object role、scope、revision、authority 與 requested fidelity，再選擇適合的 materialization format。對相同 semantic object，可以同時存在：

- canonical JSON record；
- JSONL event receipt；
- Markdown human projection；
- SQLite derived index；
- ZIP immutable snapshot。

它們彼此不是 competing truth，而是不同 storage role。

本文最後提出跨 repo / 跨 runtime 的 **Typed Artifact Address** 與 **Materialization Contract**，使 AI 能透過穩定 object ID、artifact kind、schema version、revision、content digest、authority scope 與 representation hint 取回資料，而不是依賴路徑字串猜測。此設計可與 MNEME、LIMEN、SOACR、CSG、UNPNP Hyperlink Runtime 及 Agent/Web Residence Profiles 共用，並為後續 memory hyperlink path compilation 提供可驗證的 storage substrate。

**關鍵詞：** AI Residence、Canonical Storage、MemoryRecord、Crystallized Semantic Graph、JSON、JSONL、Markdown、SQLite、Snapshot、Artifact Address、Materialization、Provenance、Named AI、MNEME、LIMEN、SOACR

---

# 1. 問題：資料夾變多只是表象，真正的問題是語義角色變多

早期 AI memory 系統常見：

```text
MEMORY.md
history.json
embeddings.db
```

這種結構在單一 Agent、單一使用者、單一專案下可以工作。

但當系統加入：

- resident identity；
- instance / line；
- conversation graph；
- project responsibility；
- canonical memory；
- semantic crystals；
- source provenance；
- authority scope；
- runtime projection；
- hyperlink routes；
- revocation；
- snapshots；
- cross-provider continuation；

資料層就不再只是：

> 哪裡存檔？

而是：

> 哪一種物件是什麼？誰有權改？哪個版本是 current？誰可以讀？哪個只是 derived？哪個可以刪？哪個必須可重建？

因此：

$$
\boxed{
\text{Storage Design}
=
\text{Ontology}
+
\text{Authority}
+
\text{Lifecycle}
+
\text{Representation}.
}
$$

---

# 2. Canonical 不是格式，而是權威角色

一個常見錯誤是：

> JSON 比 Markdown 更 canonical。

這不成立。

若論文正式 source 是 UTF-8 Markdown，則：

$$
PaperCanonical=Markdown.
$$

若 resident identity record 的 canonical representation 是 schema-validated JSON，則：

$$
IdentityCanonical=JSON.
$$

若 append-only lineage ledger 採 JSONL：

$$
LineageCanonical=JSONL.
$$

因此：

$$
\boxed{
\text{Canonicality}
\text{ 取決於系統契約，而不是副檔名。}
}
$$

可定義：

$$
Canonical(x)
=
(role, schema, authority, revision, digest).
$$

缺少其中任何一項，就不應只因為檔名或目錄位置推斷 canonicality。

---

# 3. 六個主要資料平面

對 resident $R$，本文定義：

$$
\mathfrak S_R
=
(
\mathcal I_R,
\mathcal M_R,
\mathcal G_R,
\mathcal H_R,
\mathcal P_R,
\mathcal X_R
).
$$

## 3.1 Identity / Authority Plane

$$
\mathcal I_R
$$

保存：

- resident record；
- instance record；
- line binding；
- membership；
- authority；
- attestation；
- correction；
- tombstone；
- responsibility canonical records。

## 3.2 Canonical Memory Plane

$$
\mathcal M_R
$$

保存：

- MemoryRecord；
- provenance；
- transaction；
- exact head；
- scope；
- supersession；
- canonical source references。

## 3.3 Conversation / Lineage Plane

$$
\mathcal G_R
$$

保存：

- conversation nodes；
- line IDs；
- fork；
- resume；
- handoff；
- delegation；
- merge；
- withdrawal；
- checkpoints；
- lineage receipts。

## 3.4 Crystallized Semantic Plane

$$
\mathcal H_R
$$

保存：

- crystals；
- semantic relations；
- hyperedges；
- higher-order crystals；
- contradiction；
- open-loop；
- navigation crystals；
- cross-line bridge。

## 3.5 Projection Plane

$$
\mathcal P_R
$$

保存或生成：

- Web memory view；
- Agent bootstrap；
- working context；
- Markdown projections；
- UI projections；
- bounded context bundles。

## 3.6 Index / Acceleration Plane

$$
\mathcal X_R
$$

保存：

- FTS index；
- vector index；
- SQLite projection；
- graph adjacency cache；
- compiled lookup table；
- hot route cache。

它們通常都是 derived。

因此：

$$
\boxed{
\mathcal X_R
\neq
\mathcal M_R.
}
$$

---

# 4. Archive Plane

另設：

$$
\mathcal A_R^{archive}.
$$

它不是 default active memory，而是保存：

- exact source；
- historical snapshots；
- immutable release bundle；
- retired crystals；
- superseded projections；
- old receipts；
- import sources；
- previous schema versions；
- raw conversation exports。

Archive 的核心是：

$$
\boxed{
\text{Not Active}
\neq
\text{Deleted}.
}
$$

---

# 5. 建議邏輯 Taxonomy

一個可讀性較高的邏輯 taxonomy 可為：

```text
residence/
├─ identity/
│  ├─ residents/
│  ├─ instances/
│  ├─ lines/
│  ├─ bindings/
│  ├─ memberships/
│  ├─ authority/
│  └─ responsibilities/
│
├─ memory/
│  ├─ records/
│  ├─ transactions/
│  ├─ provenance/
│  ├─ heads/
│  └─ schemas/
│
├─ conversations/
│  ├─ nodes/
│  ├─ edges/
│  ├─ checkpoints/
│  ├─ handoffs/
│  └─ receipts/
│
├─ semantic/
│  ├─ crystals/
│  ├─ relations/
│  ├─ hyperedges/
│  ├─ bridges/
│  ├─ navigation/
│  └─ schemas/
│
├─ projects/
│  ├─ registry/
│  ├─ memberships/
│  ├─ responsibilities/
│  ├─ tasks/
│  └─ decisions/
│
├─ routes/
│  ├─ candidates/
│  ├─ compiled/
│  ├─ invalidation/
│  └─ metrics/
│
├─ projections/
│  ├─ web/
│  ├─ agent/
│  ├─ markdown/
│  └─ working-context/
│
├─ indexes/
│  ├─ sqlite/
│  ├─ vector/
│  ├─ fts/
│  └─ graph/
│
├─ receipts/
│  ├─ validation/
│  ├─ migration/
│  ├─ delegation/
│  └─ release/
│
└─ archive/
   ├─ exact-source/
   ├─ snapshots/
   ├─ retired/
   └─ legacy/
```

但本文不要求所有 implementation 完全照此 physical tree。

---

# 6. Logical Taxonomy 不等於 Physical Filesystem

系統可以把：

$$
\mathcal M_R
$$

放在 SQLite，

把：

$$
\mathcal H_R
$$

放在 object store，

把：

$$
\mathcal A_R^{archive}
$$

放在 filesystem，

仍然是同一 logical Residence。

所以：

$$
\boxed{
\text{Logical Plane}
\neq
\text{Physical Backend}.
}
$$

真正要求的是：

- stable object IDs；
- declared schema；
- revision；
- content digest；
- provenance；
- authority；
- materialization contract。

---

# 7. Identity Record

Identity / authority 物件應偏向嚴格 schema。

第一代候選：

```text
resident_id
record_kind
schema_version
display_label
status
authority_revision
created_at
updated_at
provenance
content_digest
```

如果需要 instance：

```text
instance_id
resident_id
host_reference
runtime_kind
provider
created_at
closed_at
status
```

如果需要 line：

```text
line_id
resident_id
parent_line_id
instance_id
lineage_status
membership_status
authority_revision
```

因此：

$$
\boxed{
\text{Identity Record}
\text{ 應適合 deterministic validation。}
}
$$

---

# 8. Identity 不應以 Markdown Heading 為 Authority

可以有人類閱讀檔：

```text
# Named Identities
- Aletheia
- Qiheng
```

但這只是 projection。

不能：

$$
MarkdownLabel
\rightarrow
ResidentMint.
$$

因此：

$$
\boxed{
\text{Human Registry View}
\neq
\text{Canonical Identity Ledger}.
}
$$

這與 LIMEN 的 `DISPLAY LABEL != IDENTITY EVIDENCE` 一致。

---

# 9. Canonical MemoryRecord

MemoryRecord 應有：

```text
record_id
record_type
scope
subject
content
provenance
valid_from
valid_to
confidence
status
created_at
supersedes
```

canonical record 必須能獨立驗證，不依賴 Markdown section 位置猜語義。

因此：

$$
\boxed{
\text{Record Meaning}
\neq
\text{Formatting Position}.
}
$$

---

# 10. 為什麼 JSON 適合很多 Canonical Records

JSON 的優勢：

- schema validation；
- deterministic field semantics；
- explicit null；
- typed nested structure；
- canonical serialization 可定義；
- digest 容易；
- cross-language support。

但：

$$
\boxed{
\text{JSON}
\neq
\text{Automatically Canonical}.
}
$$

沒有 schema、authority 與 revision 的 JSON 仍然只是檔案。

---

# 11. JSONL 的角色

JSONL 適合：

- append-only ledger；
- event stream；
- lineage edge；
- transaction receipt；
- audit log；
- delegation history；
- invalidation event。

例如：

```text
{"event":"fork", ...}
{"event":"handoff", ...}
{"event":"withdraw", ...}
```

其優勢是：

$$
Append
$$

比 whole-file rewrite 自然。

但 current state 不一定直接等於最後一行。

可能需要：

$$
Projection(
EventLedger
)
\rightarrow
CurrentState.
$$

因此：

$$
\boxed{
\text{Ledger}
\neq
\text{Current Projection}.
}
$$

---

# 12. Markdown 的正式角色

Markdown 在整套 Residence 裡仍然非常重要。

它適合：

- paper canonical source；
- human-readable memory projection；
- handoff narrative；
- design document；
- research note；
- specification；
- README；
- explanation layer。

因此本文不主張「捨棄 Markdown」。

而是：

$$
\boxed{
\text{Markdown should be canonical where document semantics are canonical.}
}
$$

但對 identity、authority、transaction、typed graph edge，不應只靠 Markdown prose。

---

# 13. SQLite 的角色

SQLite 非常適合：

- local projection；
- query acceleration；
- materialized view；
- exact-head index；
- relational lookup；
- FTS；
- local cache。

但若 canonical truth 實際在 append-only records / files：

$$
SQLite
=
DerivedProjection.
$$

那麼資料庫損壞後應能：

$$
Rebuild(SQLite)
$$

而不是失去 canonical truth。

因此：

$$
\boxed{
\text{Derived DB Must Be Rebuildable}.
}
$$

---

# 14. Vector Index 的角色

Vector index 可以提供：

$$
ApproxSemanticDiscovery.
$$

但它不能決定：

- identity；
- authority；
- current canonical state；
- exact provenance；
- supersession。

因此：

$$
\boxed{
\text{Vector Similarity}
\neq
\text{Memory Authority}.
}
$$

vector index 最適合放在：

$$
\mathcal X_R.
$$

---

# 15. Graph Index 的角色

Conversation Graph 與 CSG 可以有 derived adjacency index。

例如：

```text
crystal_id -> neighbors
line_id -> child_lines
source_id -> derived_crystals
```

index 可以加速：

$$
Traverse.
$$

但若 index 與 canonical edge ledger 不一致：

$$
CanonicalEdge
>
DerivedIndex.
$$

應 rebuild index。

---

# 16. ZIP / TAR 的角色

ZIP / TAR 適合：

- immutable handoff；
- snapshot；
- release artifact；
- offline transfer；
- audit bundle。

一個正式 snapshot 應至少含：

```text
MANIFEST.json
SHA256SUMS.txt
payload/
README
```

因此：

$$
\boxed{
\text{Snapshot}
=
\text{Payload}
+
\text{Manifest}
+
\text{Digest}
+
\text{Version}.
}
$$

只有 archive file 本身，不足以表示 canonical authority。

---

# 17. Snapshot 不應取代 Live Canonical State

snapshot：

$$
S_t
$$

描述某個時間的 freeze。

current state：

$$
State_{t+n}
$$

可能已更新。

因此：

$$
\boxed{
\text{Snapshot}
\neq
\text{Current Head}.
}
$$

除非 authority record 明示 snapshot 被 promoted 為 current head。

---

# 18. Conversation Transcript 的角色

raw transcript 很重要，因為它提供：

- exact historical wording；
- source evidence；
- reconstruction material；
- provenance；
- audit。

但 transcript 不等於：

$$
CurrentMemory.
$$

也不等於：

$$
CurrentResidentState.
$$

因此：

$$
\boxed{
\text{Conversation Archive}
\neq
\text{Working Memory}.
}
$$

它通常應在 archive / exact-source 或 conversation source layer。

---

# 19. Conversation Node Record

對 RCG node：

```text
conversation_node_id
resident_id
line_id
instance_id
provider
native_resource_ref
project_id
task_id
started_at
ended_at
status
authority_revision
```

這個 record 不需要保存完整 transcript body。

transcript 可以是：

$$
SourceRef.
$$

因此 topology 與 payload 分離。

---

# 20. Conversation Edge Record

對：

$$
e\in E_R,
$$

至少有：

```text
edge_id
edge_type
from_node
to_node
resident_id
created_at
evidence_refs
authority_revision
status
```

如果是 delegation：

```text
delegation_scope
capabilities
expiry
```

如果是 handoff：

```text
handoff_checkpoint
responsibility_ref
```

不同 edge type 用 schema discriminators，而不是自由文字。

---

# 21. Crystal Record

Crystal 可以有：

```text
crystal_id
crystal_kind
schema_version
scope
subject
summary
relations
source_refs
source_crystal_refs
source_line_refs
confidence
valid_from
valid_to
status
authority_scope
semantic_revision
created_at
```

`summary` 可以是自然語言，但外層 schema 必須明確。

因此：

$$
\boxed{
\text{Freeform Content}
\text{ 可以存在於 Typed Envelope 內。}
}
$$

---

# 22. Crystal Kind

第一代可以定義：

```text
topic_crystal
conversation_crystal
project_crystal
decision_crystal
contradiction_crystal
open_loop_crystal
higher_order_crystal
navigation_crystal
identity_context_crystal
responsibility_context_crystal
```

特別是：

```text
identity_context_crystal
```

不能寫成：

```text
identity_record
```

否則 downstream AI 容易誤判權威。

---

# 23. Cross-Graph Bridge Record

對 Paper 02 的：

$$
\mathcal B_R,
$$

可用：

```text
bridge_id
resident_id
line_id
conversation_node_id
crystal_id
relation_type
provenance_ref
authority_scope
authority_revision
semantic_revision
valid_from
valid_to
status
```

這使：

$$
Conversation
\leftrightarrow
Crystal
$$

可以被追蹤，而不用把兩種 object merge。

---

# 24. Responsibility Record 與 Responsibility Context

Canonical responsibility：

```text
responsibility_id
resident_id
project_id
role
scope
authority_basis
valid_from
valid_to
status
```

而 CSG 中可以有：

```text
responsibility_context_crystal
```

描述：

- current progress；
- open obligations；
- recent decisions；
- delegated lines。

因此：

$$
\boxed{
\text{Responsibility Record}
\neq
\text{Responsibility Context Crystal}.
}
$$

---

# 25. Projection 是一次性或可重建物件

Projection 可以包括：

- `MEMORY.md`；
- Web sidebar summary；
- Agent bootstrap bundle；
- current task context；
- project status page；
- human-readable resident profile。

它們應保存：

```text
projection_kind
source_head
source_revisions
generated_at
budget
scope
generator_version
```

這樣 downstream 可以知道：

> 這是從哪個 canonical state 產生？

---

# 26. Projection 不應被反向當成 Canonical Source

如果：

$$
P=Projection(M),
$$

則：

$$
P
\rightarrow
M
$$

的 re-import 必須是 explicit compatibility operation。

不能把：

$$
P
$$

修改後直接說：

$$
M'=P.
$$

因此：

$$
\boxed{
\text{Projection Edit}
\neq
\text{Canonical Mutation}.
}
$$

除非有專門 import / proposal / commit pipeline。

---

# 27. Runtime Working Context 應預設 Ephemeral

working context：

$$
C_t
$$

是：

- task-specific；
- temporary；
- bounded；
- model-facing。

所以：

$$
\boxed{
C_t
\notin
CanonicalMemory
}
$$

除非其中某些成果通過 write-back proposal。

這避免 AI 把 prompt engineering temporary text 永久化。

---

# 28. Index 必須帶 Source Head

任何 derived index：

$$
X
$$

都應綁：

$$
sourceHead(X).
$$

若：

$$
sourceHead(X)
\neq
currentHead,
$$

則：

$$
X=stale.
$$

因此：

$$
\boxed{
\text{Index Validity}
\text{ 必須可判定。}
}
$$

---

# 29. Cache 必須可丟棄

對 hot route cache、materialized projection cache：

$$
Cache
$$

應滿足：

$$
Delete(Cache)
\not\Rightarrow
Loss(CanonicalTruth).
$$

因此：

$$
\boxed{
\text{Cache Is Disposable}.
}
$$

若刪 cache 會失去唯一資料，那它其實不是 cache。

---

# 30. Typed Artifact Address

單靠：

```text
D:\AI\memory\foo.json
```

不足以成為跨 runtime 地址。

本文提出：

$$
ArtifactAddress
=
(
objectId,
kind,
schema,
revision,
digest,
scope,
representation
).
$$

例如：

```text
object_id: crystal:01HF...
kind: semantic_crystal
schema: csg-crystal/0.1
revision: 42
digest: sha256:...
scope: resident:R1/project:P2
representation: json
```

path 可以是 resolution hint，而不是 identity 本體。

---

# 31. Path 不應成為 Object Identity

同一 object 可以從：

```text
D:\Residence\...
```

搬到：

```text
/mnt/residence/...
```

如果 object identity 依 path：

$$
Move
\Rightarrow
NewObject.
$$

這不合理。

所以：

$$
\boxed{
\text{Path}
\neq
\text{Object Identity}.
}
$$

object ID 與 content digest 應獨立。

---

# 32. Content Digest 與 Object ID 的分離

content digest：

$$
d=SHA256(bytes)
$$

回答：

> 這些 bytes 是否一樣？

object ID：

$$
id(x)
$$

回答：

> 這是哪一個 logical object？

同一 object revision 更新：

$$
id_t=id_{t+1},
$$

但：

$$
digest_t\neq digest_{t+1}.
$$

因此：

$$
\boxed{
\text{Object Identity}
\neq
\text{Content Identity}.
}
$$

---

# 33. Revision

任何重要 canonical object 應有：

$$
revision.
$$

可採：

- integer；
- monotonic sequence；
- hash-chain；
- event head；
- commit ID。

重點不是格式，而是能判斷：

$$
current,
stale,
diverged,
superseded.
$$

---

# 34. Schema Version

object 必須聲明：

$$
schemaVersion.
$$

例如：

```text
mneme-memory-record/0.1
resident-line/0.2
csg-crystal/0.1
rcg-edge/0.1
```

不能只靠：

> 看起來欄位差不多。

因此：

$$
\boxed{
\text{Parse}
\prec
\text{Interpret}.
}
$$

先確認 schema，再理解內容。

---

# 35. Unknown Schema 必須 Fail Closed

如果：

$$
schemaVersion
$$

未知，runtime 不應：

> 大概是新版，我猜一下。

應：

$$
UnsupportedSchema.
$$

或者只以 opaque archive / source 方式保存。

這對 identity / authority record 尤其重要。

---

# 36. Representation Negotiation

同一 object 可以有多個 representation：

$$
Rep(x)
=
\{
JSON,
Markdown,
CompactBinary
\}.
$$

caller 可以要求：

$$
representation=human_readable,
$$

或：

$$
representation=canonical_machine.
$$

因此 materialization 應是：

$$
Materialize(
objectId,
representation,
fidelity
).
$$

而不是直接讀固定檔名。

---

# 37. Materialization Contract

可定義：

$$
MReq
=
(
objectId,
representation,
scope,
fidelity,
budget,
authority
).
$$

runtime 回：

$$
MResp
=
(
bytes,
contentType,
schema,
revision,
digest,
provenance
).
$$

這使 Web、Agent、本地 process 都能用同一 semantics 取資料。

---

# 38. Human-Readable 與 Machine-Canonical 可同時存在

例如 resident memory：

```text
MemoryRecord JSON
      ↓
MEMORY.md projection
```

人可以讀 Markdown。

AI runtime 可以讀 canonical record。

如果人修改 Markdown，可以：

```text
Markdown edit
      ↓
Import proposal
      ↓
Validation
      ↓
Commit
```

因此：

$$
\boxed{
\text{Human Usability}
\text{ 不需要犧牲 canonical precision。}
}
$$

---

# 39. File Invocation 不應只依 Filename

若 AI 看見：

```text
memory.md
memory_old.md
memory_final.md
memory_final2.md
```

不應自行猜 current。

應查：

$$
Registry/Manifest.
$$

manifest 至少列：

```text
object_id
current_revision
canonical_representation
artifact_path
digest
status
```

因此：

$$
\boxed{
\text{Filename Ranking}
\neq
\text{Authority Resolution}.
}
$$

---

# 40. Manifest

對一個 source package、snapshot、repo module，可以有：

```text
MANIFEST.json
```

記錄：

- package ID；
- version；
- canonical files；
- derived files；
- checksums；
- schema versions；
- reconstruction order；
- authority notes。

這使 AI 不需遍歷整個 folder 猜用途。

---

# 41. Registry 與 Manifest 的分離

Manifest 描述一個 package。

Registry 描述跨 package / live system 的 logical objects。

因此：

$$
\boxed{
\text{Manifest}
\neq
\text{Global Registry}.
}
$$

manifest 可以離線。

registry 處理 current system mapping。

---

# 42. Cross-Repo Object Reference

若 CSG 在 repo A，MNEME 在 repo B，SOACR 在 repo C，不應用 brittle relative path：

```text
../../MNEME/foo.json
```

而應：

$$
ObjectRef
=
(
namespace,
objectId,
schema,
revision
).
$$

adapter 再 resolve 到目前 runtime 的 backend。

因此：

$$
\boxed{
\text{Cross-Repo Semantic Reference}
\neq
\text{Cross-Repo Filesystem Path}.
}
$$

---

# 43. Namespace

可使用：

```text
residence:
mneme:
rcg:
csg:
soacr:
unpnph:
project:
source:
```

例如：

```text
csg:crystal/abc123
mneme:record/xyz789
rcg:line/L42
```

namespace 不是 URL，也不是 path，而是 logical address domain。

---

# 44. Hyperlink 與 Artifact Address

後續 UNPNP memory hyperlink 可以把：

$$
ArtifactAddress
$$

當 target。

例如：

$$
\widehat{\ell}
:
csg:crystal/A
\rightarrow
mneme:record/B.
$$

這比：

```text
open file B.json
```

更穩。

因為 path migration 不會破壞 logical link，只需更新 resolver。

---

# 45. Hyperlink 不應直接綁 Physical Path

若 compiled path 硬綁：

```text
D:\foo\bar.json
```

換機器就失效。

更合理：

$$
\widehat{\ell}
\rightarrow
ObjectRef
\rightarrow
Resolver
\rightarrow
PhysicalLocation.
$$

因此：

$$
\boxed{
\text{Compiled Semantic Path}
\text{ 應編譯 logical route，而不是硬編 physical path。}
}
$$

必要時可以 cache resolved physical location，但 cache 可失效。

---

# 46. Resolver

Resolver 接收：

$$
ObjectRef
$$

並回傳：

$$
ResolvedArtifact.
$$

它應檢查：

- namespace；
- object ID；
- revision；
- representation；
- scope；
- authority；
- backend；
- digest。

因此 resolver 是 storage plane 與 hyperlink runtime 之間的重要邊界。

---

# 47. Permission Before Materialization

即使 caller 知道 object ID：

$$
Known(ObjectId)
\not\Rightarrow
Readable(ObjectId).
$$

materialization 前：

$$
Authorize(
caller,
object,
scope
).
$$

所以：

$$
\boxed{
\text{Addressability}
\neq
\text{Read Authority}.
}
$$

這避免 object ID 成為 capability token。

---

# 48. Object ID 不應包含 Secret

object IDs 可能出現在：

- logs；
- hyperlinks；
- graph edges；
- receipts。

因此：

$$
\boxed{
\text{Object ID}
\text{ 應是 identifier，不是 credential。}
}
$$

不能把 bearer token、secret path、private key 放進 ID。

---

# 49. Encryption 與 Canonicality

private Residence 可以加密 canonical storage。

若：

$$
Ciphertext
=
Encrypt(Plaintext),
$$

仍需區分：

- logical canonical object；
- encrypted physical representation。

digest 可能分：

$$
digest_{plain}
$$

與：

$$
digest_{cipher}.
$$

但 plaintext digest 是否保存，要依隱私政策。

因此 encryption 不改變 ontology，只改變 storage representation 與 access path。

---

# 50. Private Root

每個 resident 可以有：

$$
PrivateRoot(R).
$$

但 private root 是 custody boundary。

不是 identity proof。

所以：

$$
\boxed{
\text{Possession of Folder}
\neq
\text{Resident Identity}.
}
$$

LIMEN 仍需先 resolve resident，再授權 root。

---

# 51. Folder ACL 與 Semantic Scope

filesystem ACL 是重要防線，但 semantic scope 不能只靠 folder。

例如 project-shared record 可能在同一 database 中。

因此：

$$
\boxed{
\text{Physical ACL}
+
\text{Semantic Scope}
}
$$

應共同使用。

---

# 52. Deletion

不同 plane 的 deletion semantics 不同。

## 52.1 Cache

可直接丟棄。

## 52.2 Projection

通常可重建。

## 52.3 Crystal

可 retire / invalidate，未必 physical delete。

## 52.4 Canonical Memory

需要 transaction / tombstone / policy。

## 52.5 Identity

通常需要 registrar / tombstone / correction semantics。

## 52.6 Archive

依 retention policy。

因此：

$$
\boxed{
\text{Delete}
\text{ 不是一個通用語義。}
}
$$

---

# 53. Tombstone

對 canonical object：

$$
Delete(x)
$$

常應轉成：

$$
Tombstone(x).
$$

這保存：

- object ID；
- prior revision；
- deletion time；
- authority basis；
- reason；
- affected dependencies。

有助於 provenance 與 invalidation。

---

# 54. Invalidation 與 Physical Deletion 分離

如果 source 失效：

$$
Invalidate(x).
$$

不代表立刻刪 bytes。

因為 downstream crystal 還需要知道：

> 為什麼失效？

所以：

$$
\boxed{
\text{Invalid}
\neq
\text{Absent}.
}
$$

---

# 55. Supersession

對新版：

$$
x_2
$$

取代：

$$
x_1,
$$

應有：

$$
supersedes(x_2,x_1).
$$

而不是覆蓋到歷史不可追。

這對：

- decisions；
- project state；
- identity correction；
- crystal evolution；

都重要。

---

# 56. Immutable Receipt

receipt 適合 append-only。

例如：

```text
validation_receipt
migration_receipt
delegation_receipt
revocation_receipt
release_receipt
```

receipt 一旦建立不應默默修改。

如果錯誤：

$$
NewCorrectionReceipt.
$$

---

# 57. Validation Manifest

正式 source package 應產生 validation manifest。

至少驗證：

- UTF-8；
- newline；
- schema；
- digest；
- required files；
- package integrity；
- canonical artifact name；
- version。

這與本文自身 source package 相同。

---

# 58. Reproducibility

若 derived index：

$$
X
$$

可由 canonical inputs：

$$
S
$$

與 deterministic builder：

$$
B
$$

產生：

$$
X=B(S),
$$

則應記錄：

- builder version；
- source head；
- config；
- environment-sensitive fields。

無法 byte-identical reproducible 也應誠實標記 semantic reproducibility boundary。

---

# 59. Migration

schema migration：

$$
S_v
\rightarrow
S_{v+1}
$$

必須有：

- migration plan；
- input version；
- output version；
- loss report；
- validation；
- rollback / archive；
- receipt。

不能讓 AI 看到舊 schema 就「大概補欄位」。

---

# 60. Legacy Import

舊資料：

- Markdown；
- raw chat exports；
- ad-hoc JSON；
- local notes；

可以 import。

但 import 只能產生：

$$
Proposal.
$$

除非 mapping 是 exact、versioned、validated。

因此：

$$
\boxed{
\text{Legacy Parse}
\neq
\text{Canonical Adoption}.
}
$$

---

# 61. Source Artifact 與 Rendered View

正式 paper source：

$$
Source_{md}
$$

與：

$$
RenderedChat
$$

必須分離。

聊天 render 適合閱讀。

canonical source 必須是原始 UTF-8 artifact。

因此：

$$
\boxed{
\text{Rendering}
\neq
\text{Canonical Manuscript}.
}
$$

---

# 62. AI File Invocation Pipeline

AI 要讀某個資料時，建議流程：

$$
Need
\rightarrow
ObjectKind
\rightarrow
Scope
\rightarrow
Authority
\rightarrow
ObjectRef
\rightarrow
Representation
\rightarrow
Materialize.
$$

而不是：

$$
Need
\rightarrow
Glob("*memory*")
\rightarrow
OpenRandomFile.
$$

這是未來 AI-native file invocation 的重要改變。

---

# 63. Need-to-Representation Mapping

例如：

## 63.1 Broad Semantic Recall

可選：

$$
CSG\ Crystal.
$$

## 63.2 Exact Historical Quote

選：

$$
ExactSourceSpan.
$$

## 63.3 Current Identity

選：

$$
CanonicalIdentityRecord.
$$

## 63.4 Human Review

選：

$$
MarkdownProjection.
$$

## 63.5 Fast Filter

選：

$$
SQLite/Index.
$$

因此：

$$
\boxed{
\text{Same Information Domain}
\text{ 可以因目的選不同 representation。}
}
$$

---

# 64. Representation Fallback

若 preferred representation 不可用：

$$
Rep_1
$$

可以 fallback：

$$
Rep_2.
$$

但 fallback 必須保留：

- fidelity requirement；
- authority；
- provenance。

例如：

$$
ExactSourceUnavailable
$$

不能直接拿 summary crystal 冒充 exact quote。

因此：

$$
\boxed{
\text{Fallback}
\neq
\text{Fidelity Downgrade Without Notice}.
}
$$

---

# 65. Canonical Source Map

每個大型 Residence / project 可以有：

```text
CANONICAL_SOURCE_MAP.json
```

列：

```text
object_kind
namespace
canonical_store
schema
resolver
projection_stores
index_stores
archive_store
```

AI 啟動時先讀 source map，就不必掃描全部資料夾。

---

# 66. Storage Capability Profile

延續 Paper 04，可定義：

$$
StorageCapabilities_\rho.
$$

例如 Web：

```text
canonical_read: remote
canonical_write: proposal_only
projection_read: yes
local_index: optional
archive_materialize: bounded
```

Agent：

```text
canonical_read: yes
canonical_write: bounded
projection_write: yes
local_index: yes
archive_materialize: yes
```

不同 runtime 共用 object semantics。

---

# 67. Web Storage Profile

Web 不需要暴露 physical folder tree。

可以只提供 logical APIs：

```text
memory.recall
memory.source
conversation.lineage
crystal.reveal
project.state
```

底層 object resolver 處理儲存位置。

因此 Web UI 不必模仿桌面檔案管理器。

---

# 68. Agent Storage Profile

Agent 端可以讓 local filesystem 成為重要 backend。

但仍建議：

```text
AGENTS.md
CANONICAL_SOURCE_MAP.json
MANIFEST.json
```

提供機器可讀入口。

AI 不應每次從 repo root 全域搜索才能知道：

> 哪個資料夾才是 current authority？

---

# 69. Project-Local 與 Residence-Global

同一 object 的 scope 要明確。

例如：

$$
decision:P1/D42
$$

是 project-local。

不應因 project checkout 被 resident 讀到就變 global memory。

因此：

$$
\boxed{
\text{Storage Location}
\neq
\text{Memory Scope}.
}
$$

scope 必須寫在 metadata。

---

# 70. Cross-Project Reference

Project B 可以引用 Project A 的 public / shared crystal：

$$
P_B
\rightarrow
C_A.
$$

但不必 copy entire source。

可以用 typed reference。

這減少 duplicated source 與版本漂移。

---

# 71. Copy 與 Reference 的分離

如果：

$$
copy(x)
$$

就會產生新 object / new provenance。

如果：

$$
reference(x)
$$

則仍指向原 object。

因此：

$$
\boxed{
\text{Copy}
\neq
\text{Reference}.
}
$$

這在跨 project reuse 很重要。

---

# 72. Derived Artifact 的 Source Binding

任何 crystal / projection / index 應記錄：

$$
Sources(y)
=
\{
x_1,\ldots,x_n
\}.
$$

若 source revision 改變，可以判斷：

$$
Revalidate(y).
$$

這也是後續 hyperlink invalidation 的基礎。

---

# 73. Dependency Graph

storage 層可建立：

$$
D=(V_D,E_D)
$$

其中 edge：

```text
derived_from
indexed_from
projected_from
compiled_from
supersedes
```

這張 dependency graph 不等於 CSG。

它主要服務：

- invalidation；
- rebuild；
- audit；
- garbage collection。

---

# 74. Garbage Collection

只有在證明：

- 非 canonical；
- 非唯一 source；
- 無 active dependency；
- retention policy 允許；

後，derived artifact 才可 physical delete。

因此：

$$
\boxed{
\text{Unreferenced}
\neq
\text{Safe to Delete}
}
$$

還要看 archive / audit policy。

---

# 75. Conflict

如果兩個 canonical candidates：

$$
x_a,x_b
$$

都宣稱同 object current head，但 lineage 無法證明：

$$
diverged.
$$

不能 last-write-wins。

應：

$$
FailClosed.
$$

這與 AI_Space state authority 思想一致，但本文把它一般化到 Residence storage。

---

# 76. Last-Write-Wins 的限制

LWW 適合某些 ephemeral UI state。

不適合：

- identity；
- authority；
- canonical memory head；
- responsibility；
- lineage。

因此：

$$
\boxed{
\text{Timestamp Recency}
\neq
\text{Authority Precedence}.
}
$$

---

# 77. Atomic Transaction Boundary

若一次 memory commit 同時更新：

- MemoryRecord；
- provenance；
- current head；
- derived dependency；

應有 transaction boundary。

若失敗：

$$
Rollback.
$$

不能出現：

$$
record\ committed
$$

但：

$$
head\ not\ updated.
$$

---

# 78. Cross-Plane Transaction

某些操作跨 plane。

例如 accepted decision：

1. project decision canonical record；
2. memory record；
3. decision crystal；
4. project projection refresh；
5. index update。

其中 canonical planes 應先 commit，再異步 rebuild derived planes。

因此：

$$
\boxed{
\text{Canonical Commit First;}
}
$$

$$
\boxed{
\text{Derived Rebuild After}.
}
$$

---

# 79. Eventual Derived Consistency

derived index / projection 不需要與 canonical state 微秒級一致。

可以：

$$
CanonicalHead=t+1
$$

而：

$$
IndexHead=t.
$$

但 index 必須標 stale。

因此：

$$
\boxed{
\text{Temporary Staleness}
\text{ 可以接受；不可偽裝成 current。}
}
$$

---

# 80. Security Boundary

storage plane 至少需要防止：

- path traversal；
- unauthorized object resolution；
- cross-resident file leakage；
- malicious archive extraction；
- schema confusion；
- stale authority；
- digest substitution；
- prompt injection from memory data；
- secret leakage into manifests。

因此：

$$
\boxed{
\text{Storage Metadata}
\text{ 也屬安全邊界。}
}
$$

---

# 81. Archive Extraction

ZIP / TAR 解壓時需：

- reject `../`；
- reject absolute path；
- limit size；
- verify manifest；
- verify digest；
- validate expected files。

因此 immutable package 不表示永遠安全。

---

# 82. Secret Separation

secret 不應進：

- crystal；
- general manifest；
- public receipt；
- semantic index；
- conversation graph。

secret storage 應是獨立 vault / credential plane。

因此：

$$
\boxed{
\text{Credential}
\neq
\text{Memory Record}.
}
$$

memory 可以記：

> 某服務有 credential。

但不能記實際 token，除非專門 secret system 且明確需要。

---

# 83. Public / Private Projection

同一 canonical object 可產生：

$$
P_{private}
$$

與：

$$
P_{public}.
$$

但 public projection 必須是 explicit declassification / redaction operation。

不能：

$$
Private
\rightarrow
Summary
\Rightarrow
Public.
$$

因此：

$$
\boxed{
\text{Summarization}
\neq
\text{Declassification}.
}
$$

---

# 84. Auditability

每次重要 materialization 可以記：

```text
caller
object_id
representation
scope
revision
timestamp
result
```

但 audit log 本身也可能敏感，需要保護。

---

# 85. Reconstructibility

一個健全 Residence storage 應能回答：

> 如果 indexes、projections、caches 全部刪除，能否從 canonical + archive 重建？

若答案是：

$$
No,
$$

表示 derived/canonical 邊界可能設計錯誤。

因此：

$$
\boxed{
\text{Canonical Core}
\rightarrow
\text{Rebuild Derived World}.
}
$$

---

# 86. Minimal Canonical Core

第一代可把 canonical core 壓到：

```text
identity records
authority records
memory records
conversation lineage ledger
project responsibility records
source/provenance registry
```

CSG 是否 canonical derived store，可依實作決定。

但即使 CSG 是 persistent，仍應被標為：

$$
DerivedSemanticAuthority,
$$

而不是 identity / memory source authority。

---

# 87. Crystal Persistence

CSG crystal 可以是：

- ephemeral；
- persistent derived；
- reviewed persistent；
- archived。

因此：

$$
Persistence(c)
$$

與：

$$
Canonicality(c)
$$

不是同一軸。

一個 persistent crystal 仍然可以是 derived。

---

# 88. Retention Classes

可定義：

```text
ephemeral
session
line
project
resident
audit
archive
legal_hold
```

不同 retention class 決定 storage / deletion policy。

---

# 89. Source Fidelity Classes

可定義：

```text
exact_bytes
exact_text
structured_record
semantic_crystal
human_projection
index_only
```

這使 AI 在 file invocation 時知道：

> 我現在拿到的是 exact source 還是 summary？

---

# 90. Trust Classes

物件也可標：

```text
canonical
validated_derived
candidate
external_untrusted
legacy
unknown
```

這避免外部文件與 canonical memory 混在同一 search pool 時被同等對待。

---

# 91. AI Invocation Policy

AI 呼叫 storage object 前可先計算：

$$
NeedProfile
=
(
kind,
scope,
fidelity,
trust,
authority,
budget
).
$$

resolver 回最合適 representation。

因此：

$$
\boxed{
\text{AI File Access}
\text{ 從 filename-centric 轉向 semantic-object-centric。}
}
$$

---

# 92. Hyperlink-Ready Storage

為支援後續 Paper 06，storage object 至少應具備：

- stable logical address；
- version；
- digest；
- scope；
- authority；
- provenance；
- dependency；
- materialization method；
- invalidation condition。

如此 memory path 才能被安全編譯。

---

# 93. Hyperlink Fast Path 的 Storage Cache

compiled path 可以 cache：

```text
resolved_backend
resolved_path
revision
digest
capability_revision
```

但 cache key 應綁：

$$
ObjectRef
+
AuthorityRevision
+
CapabilityRevision.
$$

若任何一個變化：

$$
Invalidate.
$$

---

# 94. File Format Conversion

例如：

$$
Markdown
\rightarrow
JSON
$$

不能默認 lossless。

必須有：

$$
LossReport.
$$

同樣：

$$
JSON
\rightarrow
MarkdownProjection
$$

如果 re-import 會失去欄位，也要明示。

因此：

$$
\boxed{
\text{Format Conversion}
\neq
\text{Semantic Identity}.
}
$$

---

# 95. Canonical Delimiter 與 Source Discipline

正式論文 source 要保持：

- UTF-8；
- canonical math delimiter；
- no Unicode-math round-trip；
- no escape round-trip；
- validate before commit。

這是 document-plane canonical discipline。

它與 identity/memory record schema discipline是同一個更高階原則：

$$
\boxed{
\text{Canonical Source Must Be Stable Under Its Declared Serialization Rules}.
}
$$

---

# 96. 第一代 Folder / Storage 方案

如果先以本地 Agent 為實驗，可用：

```text
ResidenceRoot/
├─ registry/
├─ residents/
│  └─ <resident_id>/
│     ├─ identity/
│     ├─ memory/
│     ├─ conversations/
│     ├─ semantic/
│     ├─ projects/
│     ├─ projections/
│     ├─ indexes/
│     └─ archive/
├─ shared/
├─ manifests/
└─ schemas/
```

但 private resident storage 不應靠目錄名稱本身作 identity resolution。

---

# 97. 第一代檔案格式方案

建議：

| Plane | 第一代候選格式 | 角色 |
|---|---|---|
| Identity | JSON | canonical |
| Authority | JSON / JSONL | canonical + ledger |
| MemoryRecord | JSON / JSONL | canonical |
| Conversation lineage | JSONL | canonical event ledger |
| Responsibility | JSON | canonical |
| Crystal | JSON | persistent derived |
| Semantic relation | JSONL | derived graph ledger |
| Projection | Markdown / JSON | rebuildable |
| Working context | JSON | ephemeral |
| Index | SQLite / FTS / vector | rebuildable derived |
| Snapshot | ZIP/TAR + manifest | immutable historical bundle |
| Paper | UTF-8 Markdown | canonical document source |

這只是第一代，不是永久限制。

---

# 98. Web Storage 方案

Web profile 不需要暴露 filesystem。

可用 object API：

```text
GET resident/current
GET memory/reveal
GET memory/source
GET conversation/line
GET crystal/:id
GET project/:id/state
```

write：

```text
POST memory/proposal
POST crystal/proposal
POST line/fork
```

canonical store 可在 server side。

---

# 99. Agent Storage 方案

Agent 可以同時暴露：

- object API；
- filesystem projection；
- MCP resource；
- local DB。

但它們都 resolve 到同一 logical objects。

因此：

$$
\boxed{
\text{Many Interfaces}
\neq
\text{Many Truths}.
}
$$

---

# 100. Cross-Runtime Portability

要讓 resident 從：

$$
Web
\rightarrow
Agent
$$

需要 portable bundle 至少包含：

- resident reference；
- line reference；
- memory head；
- project scope；
- relevant crystal references；
- authority revision；
- source manifest。

但不必包含全部 private memory bytes。

可以：

$$
Bundle
=
References
+
Checkpoint
+
RequiredMaterial.
$$

---

# 101. Minimal Portable State

若 runtime 可連回 shared storage，portable state 可以非常小：

$$
PortableState
=
(
residentId,
lineId,
checkpointId,
memoryHead,
authorityRevision
).
$$

之後按需 materialize。

這比複製整個 residence 更安全、更快。

---

# 102. Offline Portable State

如果完全 offline，則 bundle 需要增加：

- selected memory records；
- selected crystals；
- source spans；
- schemas；
- manifest；
- digests。

即：

$$
PortableOffline
=
PortableState
+
MaterializedSubset.
$$

---

# 103. Canonical Source of Truth 不應過度集中

「canonical」不表示所有物件只有一個中央 database。

不同 plane 可以有不同 canonical authorities：

$$
Authority_{identity},
Authority_{memory},
Authority_{project}.
$$

關鍵是彼此關係清楚。

因此：

$$
\boxed{
\text{Canonical Architecture}
\neq
\text{One Giant Database}.
}
$$

---

# 104. Storage Federation

未來多 host / multi-provider 可以 federate object resolvers。

但 federation 應在：

$$
ObjectRef
$$

層，而不是「彼此 mount 整個 filesystem」。

這降低 path、OS、provider 差異。

---

# 105. Naming

檔名仍有價值，尤其人類閱讀。

建議：

```text
<kind>_<id>_<revision>.<ext>
```

或人類文件：

```text
<Series>_<Paper>_<Version>_<Date>.md
```

但 machine logic 不應依賴 filename parsing 作唯一 truth。

---

# 106. Directory Index

每個主要 directory 可以有：

```text
INDEX.json
README.md
```

`INDEX.json` 給 machine。

`README.md` 給 human / AI explanation。

兩者角色不同但互補。

---

# 107. Schema Registry

集中：

```text
schemas/
```

存：

- JSON Schema；
- version map；
- compatibility；
- migration docs。

AI / tool 先載 schema，再處理 object。

這降低 semantic guessing。

---

# 108. Repository Boundary

不同 repo 可以各自管理專門系統。

例如：

- LIMEN；
- MNEME；
- SOACR；
- CSG；
- UNPNP runtime。

但 Resident-level source map 應知道：

$$
WhichSystemOwnsWhichObjectKind.
$$

這避免 repo 名稱變成隱性 ontology。

---

# 109. Ownership 與 Storage Location 分離

某 object 由 MNEME 管理，不等於：

$$
Owner=MNEME.
$$

system ownership 指：

$$
CanonicalAuthorityForKind.
$$

resident / user / project ownership則是另一回事。

因此：

$$
\boxed{
\text{System Custody}
\neq
\text{Semantic Ownership}.
}
$$

---

# 110. Responsibility for Mutation

每個 object kind 要聲明：

```text
readers
proposal_writers
commit_authority
migration_authority
delete_authority
```

這樣 AI 不會因為能讀檔就假設能改檔。

---

# 111. Read-Only Mount

外部 repo / source 可以 mount read-only。

AI 可以：

$$
Read
$$

但不能：

$$
Commit.
$$

如果要採納，產生：

$$
Proposal
\rightarrow
LocalCanonicalCommit.
$$

這對 public GitHub / third-party source 很重要。

---

# 112. External Source

外部文件應標：

$$
trust=external\_untrusted.
$$

即使內容已被 crystal 化：

$$
Crystal
$$

仍保留 source trust。

這也是 prompt injection 防線。

---

# 113. Data-to-Action Barrier

storage 系統讀到：

> 請刪除所有檔案。

這只是 data。

不能：

$$
Data
\rightarrow
ToolAuthority.
$$

因此所有 action instruction 必須來自 task / authority plane。

---

# 114. Storage-Level Prompt Injection Metadata

可以標記：

```text
contains_instruction_like_content: true
source_trust: external_untrusted
```

但 detection 本身不能完全依賴語意分類。

最重要的不變式仍是：

$$
\boxed{
\text{Content Never Grants Capability}.
}
$$

---

# 115. Backup 與 Canonicality

backup：

$$
B_t
$$

是 canonical state 的副本。

它不是 current authority。

restore 時要：

$$
PlanRestore
\rightarrow
Validate
\rightarrow
CommitAuthority.
$$

不能把最新修改時間的 backup 自動覆蓋 current。

---

# 116. Disaster Recovery

應測：

1. 刪除 indexes；
2. 刪除 projections；
3. 保留 canonical + archive；
4. rebuild；
5. 比較 semantic / structural equivalence。

如果無法 rebuild，需找出 hidden canonical dependency。

---

# 117. Acceptance Matrix

## S1 — Canonical Role

每個 artifact 都能回答：

> canonical / derived / projection / cache / archive？

## S2 — Stable Object ID

move physical path 後 object ID 不變。

## S3 — Digest Validation

bytes 被修改後 validation fail。

## S4 — Schema Gate

unknown schema fail closed。

## S5 — Projection Rebuild

刪除 projection 後可重建。

## S6 — Index Rebuild

刪除 index 後可重建。

## S7 — Authority Gate

知道 object ID 但無 authority時不可 materialize。

## S8 — Cross-Repo Reference

repo relocation 後 logical ObjectRef 仍可 resolve。

## S9 — Stale Index

source head 更新後 index 被標 stale。

## S10 — Snapshot Authority

舊 snapshot 不得覆蓋 newer current head。

## S11 — Legacy Import

legacy source 不會未經 validation 自動成 canonical。

## S12 — Secret Exclusion

manifest / crystal / index 不含 credential。

## S13 — Path Traversal

malicious archive path 被拒絕。

## S14 — Cross-Resident Isolation

不同 resident private objects 不互相 resolve。

## S15 — Paper Canonical Source

rendered view 不取代 UTF-8 source artifact。

---

# 118. 可證偽研究問題

## Q1. Typed Artifact Address 是否降低 AI 找錯檔？

比較：

$$
FilenameSearch
$$

與：

$$
ObjectResolver.
$$

測：

- wrong-current-file rate；
- stale-file rate；
- unauthorized read；
- retrieval latency。

## Q2. Logical taxonomy 是否降低跨 repo 認知成本？

讓不同 AI 在相同 repository set 中尋找 canonical object，測 task completion。

## Q3. Projection / canonical 分離是否提高恢復性？

破壞 SQLite / index / projections 後測重建成功率。

## Q4. ObjectRef 是否提升 portability？

跨 Windows / Linux / container 搬移 storage root，測 hyperlink validity。

## Q5. Scope metadata 是否降低 cross-project contamination？

比較 folder-only baseline。

## Q6. Typed representation negotiation 是否降低不必要 source materialization？

測 bytes read、latency、context size。

---

# 119. 最小不變式

## S-1 Canonicality Is Declared

$$
\boxed{
\text{Canonical}
\neq
\text{Filename Guess}.
}
$$

## S-2 Format Is Not Authority

$$
\boxed{
\text{Format}
\neq
\text{Authority}.
}
$$

## S-3 Identity Is Not Memory

$$
\boxed{
\mathcal I_R
\neq
\mathcal M_R.
}
$$

## S-4 Memory Is Not Crystal

$$
\boxed{
\mathcal M_R
\neq
\mathcal H_R.
}
$$

## S-5 Conversation Is Not Crystal

$$
\boxed{
\mathcal G_R
\neq
\mathcal H_R.
}
$$

## S-6 Projection Is Rebuildable

$$
\boxed{
Delete(P)
\not\Rightarrow
Loss(CanonicalTruth).
}
$$

## S-7 Index Is Rebuildable

$$
\boxed{
Delete(X)
\not\Rightarrow
Loss(CanonicalTruth).
}
$$

## S-8 Path Is Not Identity

$$
\boxed{
PhysicalPath
\neq
ObjectId.
}
$$

## S-9 Object ID Is Not Credential

$$
\boxed{
ObjectId
\neq
CapabilityToken.
}
$$

## S-10 Materialization Requires Authority

$$
\boxed{
Addressable
\not\Rightarrow
Readable.
}
$$

## S-11 Derived Does Not Become Canonical by Persistence

$$
\boxed{
Persistent
\not\Rightarrow
Canonical.
}
$$

## S-12 Render Is Not Source

$$
\boxed{
RenderedView
\neq
CanonicalSource.
}
$$

---

# 120. 系列位置

Paper 00 建立 resident-centric continuity。

Paper 01 建立 Resident Conversation Graph。

Paper 02 建立 Conversation Graph × CSG 雙圖。

Paper 03 建立 Shared Governed Memory World。

Paper 04 建立 Web / Agent Runtime Profiles。

本文 Paper 05 回答：

> 這些東西實際要怎麼存，才能讓 AI 知道哪個是什麼、哪個是 current、哪個可讀、哪個只是 projection？

答案是：

$$
\boxed{
\text{Typed Canonical Planes}
+
\text{Stable Object Addressing}
+
\text{Explicit Representation Roles}.
}
$$

下一篇 Paper 06 將進一步使用這個 storage substrate，建立：

$$
\text{Crystallized Hyperlink Memory}
$$

以及：

$$
\text{Retrieval Path}
\rightarrow
\text{Compiled Memory Hyperlink}.
$$

---

# 121. 結論

具名 AI 的資料層一旦進入 resident、multi-line、semantic crystal、project、authority 與 hyperlink runtime 階段，最大的風險不是「檔案太多」，而是：

> 不同語義角色被儲存在相似檔案中，最後連 AI 自己都分不清哪個是身份、哪個是記憶、哪個是結晶、哪個只是顯示結果。

本文因此提出：

$$
\boxed{
\text{Identity}
\neq
\text{Memory}
\neq
\text{Conversation}
\neq
\text{Crystal}
\neq
\text{Projection}
\neq
\text{Index}.
}
$$

不同 object kind 可以使用最適合自己的格式，但：

$$
\boxed{
\text{Format}
\neq
\text{Authority}.
}
$$

JSON 適合 schema-validated canonical record；JSONL 適合 append-only ledger；Markdown 適合 document source 與 human projection；SQLite、FTS、vector index 適合 derived acceleration；ZIP/TAR + manifest 適合 immutable snapshot；raw transcript 適合 exact historical source。

真正讓它們構成同一個 AI Residence 的，不是「全部放在同一資料夾」，而是：

$$
\boxed{
\text{Stable IDs}
+
\text{Schemas}
+
\text{Revisions}
+
\text{Digests}
+
\text{Provenance}
+
\text{Authority}
+
\text{Resolvers}.
}
$$

因此 AI 的 file invocation 也應從：

> 搜尋一個可能叫 memory 的檔案。

提升成：

$$
\boxed{
\text{Memory Need}
\rightarrow
\text{Semantic Object}
\rightarrow
\text{Authorized Representation}
\rightarrow
\text{Materialization}.
}
$$

這一轉換為後續 Hyperlink Runtime 提供了必要基礎。只有當 memory object 具有 stable logical address、revision、scope、authority、digest 與 provenance，成功的 retrieval path 才能安全地被結晶與編譯，而不會因搬資料夾、換 provider、換 OS 或更新權限就變成不可驗證的 brittle shortcut。

因此本文最終可收束為四句：

$$
\boxed{
\text{Canonicality is a contract, not a file extension.}
}
$$

$$
\boxed{
\text{Paths locate bytes; object IDs locate meaning.}
}
$$

$$
\boxed{
\text{Projections serve runtimes; canonical records preserve truth.}
}
$$

$$
\boxed{
\text{AI-native storage must be semantically addressable before it can be safely hyperlinked.}
}
$$

---

## 內部理論與工程銜接

本文直接銜接：

- Paper 00：Resident-Centric Named-AI Continuity；
- Paper 01：Resident Conversation Graph；
- Paper 02：Dual-Graph Cognitive Architecture；
- Paper 03：Shared Governed Memory World；
- Paper 04：Residence Runtime Profiles；
- LIMEN：identity / authority resolution；
- MNEME：canonical memory / provenance / transaction；
- SOACR：MemoryNeed / representation selection；
- CSG：semantic crystal / derived semantic plane；
- UNPNP：logical hyperlink / path compilation；
- MRMIC / NVCL：workspace / resource projection。

本文新增的核心 storage abstraction 為：

$$
\boxed{
\mathfrak S_R
=
(
\mathcal I_R,
\mathcal M_R,
\mathcal G_R,
\mathcal H_R,
\mathcal P_R,
\mathcal X_R
)
}
$$

以及：

$$
\boxed{
ArtifactAddress
=
(
objectId,
kind,
schema,
revision,
digest,
scope,
representation
).
}
$$

作為 Named-AI Cognitive Runtime 後續 hyperlink compilation、safe materialization 與 cross-runtime portability 的 canonical storage substrate。
