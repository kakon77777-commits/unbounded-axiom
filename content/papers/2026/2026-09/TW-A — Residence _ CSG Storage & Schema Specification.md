# TW-A — Residence / CSG Storage & Schema Specification

**英文名：** Residence / CSG Storage & Schema Specification  
**版本：** v0.1  
**日期：** 2026-09-07  
**文件類型：** 技術白皮書／工程規格  
**對應系列：** 具名 AI 對話圖、結晶記憶與超連結認知架構  
**主要依據：** Paper 00–08，尤其 Paper 02、03、05、08  
**狀態：** Draft for Implementation  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

## 0. 目的與範圍

本文件定義 Named-AI Cognitive Runtime 第一代 Residence / Crystallized Semantic Graph 儲存層的工程契約。

目標不是規定唯一資料庫產品，而是固定以下語義：

1. resident identity 與 authority 如何儲存；
2. canonical memory 如何儲存；
3. conversation / line / fork / handoff 如何儲存；
4. semantic crystal 與 cross-graph bridge 如何儲存；
5. project / responsibility 如何儲存；
6. projection、index、cache 與 archive 如何區分；
7. object ID、revision、digest、scope、schema 與 provenance 如何統一；
8. runtime 如何透過 ObjectRef / ArtifactAddress 取得正確 representation；
9. schema migration、legacy import、snapshot、backup 與 disaster recovery 如何工作；
10. 如何保證 derived state 可重建而不冒充 canonical truth。

本文件不規定：

- AI 是否具有主體性；
- resident 的形而上數值同一性；
- distributed consensus protocol；
- production-grade secret vault 實作；
- 最終網路 federation protocol；
- action hyperlink 的完整安全規範。

---

# 1. 核心資料平面

對 resident $R$，定義儲存狀態：

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
\mathcal X_R,
\mathcal A_R
)
}
$$

其中：

- $\mathcal I_R$：Identity / Authority Plane；
- $\mathcal M_R$：Canonical Memory Plane；
- $\mathcal G_R$：Conversation / Lineage Plane；
- $\mathcal H_R$：Crystallized Semantic Plane；
- $\mathcal P_R$：Projection Plane；
- $\mathcal X_R$：Index / Cache / Acceleration Plane；
- $\mathcal A_R$：Archive / Snapshot Plane。

必須保持：

$$
\boxed{
\mathcal I_R
\neq
\mathcal M_R
\neq
\mathcal G_R
\neq
\mathcal H_R
\neq
\mathcal P_R
\neq
\mathcal X_R.
}
$$

---

# 2. Canonicality 分類

所有 artifact 必須有：

```text
artifact_role
```

允許值：

```text
canonical
validated_derived
candidate
projection
cache
archive
external_untrusted
legacy
unknown
```

其中：

- `canonical`：具系統權威的正式狀態；
- `validated_derived`：由 canonical source 導出且已驗證；
- `candidate`：尚未 commit；
- `projection`：為 runtime / human materialize 的 view；
- `cache`：可丟棄；
- `archive`：歷史／exact source；
- `external_untrusted`：外部資料；
- `legacy`：舊格式；
- `unknown`：不可自動解釋。

核心不變式：

$$
\boxed{
\text{Format}
\neq
\text{Authority}.
}
$$

---

# 3. 建議 Namespace

第一代固定 namespace：

```text
residence:
identity:
authority:
mneme:
rcg:
csg:
bridge:
project:
responsibility:
route:
projection:
source:
snapshot:
receipt:
schema:
```

ObjectRef 格式建議：

```text
<namespace><object-kind>/<object-id>
```

例如：

```text
identity:resident/01JXYZ...
rcg:line/01JABC...
mneme:record/01JDEF...
csg:crystal/01JGHI...
project:project/01JKLM...
responsibility:record/01JNOP...
```

Namespace 不是 filesystem path。

---

# 4. Object ID

第一代建議使用：

- UUIDv7；或
- ULID。

要求：

1. globally unique enough；
2. 不含 secret；
3. 不含 path；
4. 不含 display label；
5. object rename 不改 ID；
6. physical relocation 不改 ID。

因此：

$$
\boxed{
\text{Path}
\neq
\text{Object Identity}.
}
$$

---

# 5. ArtifactAddress

所有可被 runtime materialize 的 object 使用：

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
)
}
$$

JSON 例：

```json
{
  "object_id": "csg:crystal/01JABCXYZ",
  "kind": "semantic_crystal",
  "schema": "csg-crystal/0.1",
  "revision": 12,
  "digest": "sha256:...",
  "scope": {
    "kind": "project",
    "subject": "project:project/01JP"
  },
  "representation": "application/json"
}
```

---

# 6. Revision 規則

每個 canonical object 必須有：

```text
revision
```

第一代使用正整數：

$$
revision\in\mathbb N^+.
$$

每次 canonical mutation：

$$
revision_{t+1}
=
revision_t+1.
$$

不得 reset。

---

# 7. Digest 規則

canonical machine artifact 使用 SHA-256：

$$
d
=
SHA256(bytes).
$$

欄位：

```text
digest = "sha256:<hex>"
```

Digest 回答 bytes identity，不回答 logical object identity。

因此：

$$
\boxed{
\text{Object Identity}
\neq
\text{Content Identity}.
}
$$

---

# 8. Scope Schema

統一 scope：

```json
{
  "kind": "resident",
  "subject": "identity:resident/01JR"
}
```

允許：

```text
line
project
resident
relationship
shared
public
system
```

對 relationship：

```json
{
  "kind": "relationship",
  "subjects": [
    "identity:resident/A",
    "identity:resident/B"
  ]
}
```

Scope 不應從 folder path 推斷。

---

# 9. ProvenanceRef

所有 canonical / derived object 可引用：

```json
{
  "ref": "source:artifact/01J...",
  "relation": "derived_from",
  "revision": 3,
  "digest": "sha256:..."
}
```

relation 可包含：

```text
derived_from
quoted_from
observed_in
validated_by
supersedes
forked_from
checkpointed_from
imported_from
```

---

# 10. BaseEnvelope

所有核心 JSON object 共用：

```json
{
  "object_id": "namespace:kind/id",
  "kind": "string",
  "schema": "schema-id/version",
  "artifact_role": "canonical",
  "revision": 1,
  "status": "active",
  "scope": {},
  "created_at": "RFC3339",
  "updated_at": "RFC3339",
  "provenance": [],
  "digest": "sha256:..."
}
```

JSON serialization 採 UTF-8。

---

# 11. ResidentRecord Schema

Schema ID：

```text
resident-record/0.1
```

欄位：

```json
{
  "object_id": "identity:resident/01J...",
  "kind": "resident",
  "schema": "resident-record/0.1",
  "artifact_role": "canonical",
  "revision": 1,
  "status": "active",
  "display_label": "Aletheia",
  "authority_revision": 1,
  "created_at": "2026-09-07T00:00:00Z",
  "updated_at": "2026-09-07T00:00:00Z",
  "provenance": [],
  "digest": "sha256:..."
}
```

允許 status：

```text
active
suspended
withdrawn
separated
tombstoned
unresolved
```

---

# 12. InstanceRecord Schema

Schema ID：

```text
instance-record/0.1
```

欄位：

```json
{
  "object_id": "identity:instance/01J...",
  "kind": "instance",
  "schema": "instance-record/0.1",
  "artifact_role": "canonical",
  "revision": 1,
  "resident_ref": "identity:resident/01J...",
  "provider": "provider-id",
  "runtime_kind": "web|agent|desktop|service",
  "host_reference": "opaque-host-ref",
  "started_at": "RFC3339",
  "ended_at": null,
  "status": "active",
  "provenance": [],
  "digest": "sha256:..."
}
```

---

# 13. LineRecord Schema

Schema ID：

```text
line-record/0.1
```

欄位：

```json
{
  "object_id": "rcg:line/01J...",
  "kind": "conversation_line",
  "schema": "line-record/0.1",
  "artifact_role": "canonical",
  "revision": 1,
  "resident_ref": "identity:resident/01J...",
  "instance_ref": "identity:instance/01J...",
  "parent_line_ref": null,
  "project_ref": "project:project/01J...",
  "membership_status": "accepted",
  "lineage_status": "resolved",
  "authority_revision": 3,
  "status": "active",
  "created_at": "RFC3339",
  "updated_at": "RFC3339",
  "provenance": [],
  "digest": "sha256:..."
}
```

---

# 14. ConversationNode Schema

Schema ID：

```text
conversation-node/0.1
```

```json
{
  "object_id": "rcg:node/01J...",
  "kind": "conversation_node",
  "schema": "conversation-node/0.1",
  "artifact_role": "canonical",
  "revision": 1,
  "resident_ref": "identity:resident/01J...",
  "line_ref": "rcg:line/01J...",
  "instance_ref": "identity:instance/01J...",
  "project_ref": "project:project/01J...",
  "task_ref": "project:task/01J...",
  "provider_resource_ref": "opaque-provider-ref",
  "started_at": "RFC3339",
  "ended_at": null,
  "status": "active",
  "provenance": [],
  "digest": "sha256:..."
}
```

---

# 15. ConversationEdge Schema

Schema ID：

```text
rcg-edge/0.1
```

edge type：

```text
fork
resume
handoff
delegate
merge
reference
withdraw
separate
terminate
```

```json
{
  "object_id": "rcg:edge/01J...",
  "kind": "conversation_edge",
  "schema": "rcg-edge/0.1",
  "artifact_role": "canonical",
  "revision": 1,
  "edge_type": "fork",
  "from_ref": "rcg:node/A",
  "to_ref": "rcg:node/B",
  "resident_ref": "identity:resident/R",
  "authority_revision": 4,
  "evidence_refs": [],
  "created_at": "RFC3339",
  "status": "active",
  "digest": "sha256:..."
}
```

---

# 16. CheckpointRecord Schema

Schema ID：

```text
rcg-checkpoint/0.1
```

```json
{
  "object_id": "rcg:checkpoint/01J...",
  "kind": "line_checkpoint",
  "schema": "rcg-checkpoint/0.1",
  "artifact_role": "canonical",
  "revision": 1,
  "resident_ref": "identity:resident/R",
  "line_ref": "rcg:line/L",
  "memory_head_ref": "mneme:head/H",
  "project_ref": "project:project/P",
  "semantic_refs": [
    "csg:crystal/C1",
    "csg:crystal/C2"
  ],
  "open_loop_refs": [
    "csg:crystal/O1"
  ],
  "authority_revision": 7,
  "created_at": "RFC3339",
  "digest": "sha256:..."
}
```

---

# 17. MemoryRecord Schema

Schema ID：

```text
mneme-memory-record/0.1
```

```json
{
  "object_id": "mneme:record/01J...",
  "kind": "memory_record",
  "schema": "mneme-memory-record/0.1",
  "artifact_role": "canonical",
  "revision": 1,
  "record_type": "fact",
  "scope": {
    "kind": "project",
    "subject": "project:project/P"
  },
  "subject": "SOACR current architecture",
  "content": {
    "text": "..."
  },
  "confidence": 0.95,
  "valid_from": "RFC3339",
  "valid_to": null,
  "status": "active",
  "supersedes": [],
  "created_at": "RFC3339",
  "updated_at": "RFC3339",
  "provenance": [],
  "digest": "sha256:..."
}
```

record type：

```text
fact
instruction
lesson
decision
relationship
state
reference
constraint
```

---

# 18. MemoryTransaction Schema

Schema ID：

```text
mneme-transaction/0.1
```

```json
{
  "object_id": "mneme:transaction/01J...",
  "kind": "memory_transaction",
  "schema": "mneme-transaction/0.1",
  "artifact_role": "canonical",
  "revision": 1,
  "base_head_ref": "mneme:head/H1",
  "operations": [
    {
      "op": "append",
      "record_ref": "mneme:record/R1"
    }
  ],
  "result_head_ref": "mneme:head/H2",
  "actor_ref": "identity:resident/R",
  "authority_revision": 9,
  "committed_at": "RFC3339",
  "status": "committed",
  "digest": "sha256:..."
}
```

---

# 19. MemoryHead Schema

Schema ID：

```text
mneme-head/0.1
```

```json
{
  "object_id": "mneme:head/01J...",
  "kind": "memory_head",
  "schema": "mneme-head/0.1",
  "artifact_role": "canonical",
  "revision": 42,
  "resident_ref": "identity:resident/R",
  "parent_head_ref": "mneme:head/H41",
  "state_digest": "sha256:...",
  "committed_at": "RFC3339",
  "status": "current",
  "digest": "sha256:..."
}
```

---

# 20. CrystalRecord Schema

Schema ID：

```text
csg-crystal/0.1
```

```json
{
  "object_id": "csg:crystal/01J...",
  "kind": "semantic_crystal",
  "schema": "csg-crystal/0.1",
  "artifact_role": "validated_derived",
  "revision": 1,
  "crystal_kind": "decision_crystal",
  "scope": {
    "kind": "project",
    "subject": "project:project/P"
  },
  "subject": "Current accepted architecture",
  "summary": "...",
  "source_refs": [
    "mneme:record/R1"
  ],
  "source_crystal_refs": [],
  "source_line_refs": [
    "rcg:line/L1"
  ],
  "confidence": 0.92,
  "valid_from": "RFC3339",
  "valid_to": null,
  "status": "active",
  "authority_scope": {
    "kind": "project",
    "subject": "project:project/P"
  },
  "semantic_revision": 3,
  "created_at": "RFC3339",
  "updated_at": "RFC3339",
  "digest": "sha256:..."
}
```

---

# 21. Crystal Kind

第一代 enum：

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
temporal_crystal
```

---

# 22. SemanticRelation Schema

Schema ID：

```text
csg-relation/0.1
```

relation type：

```text
supports
contradicts
refines
updates
supersedes
depends_on
derived_from
related_to
precedes
follows
resolves
reopens
```

```json
{
  "object_id": "csg:relation/01J...",
  "kind": "semantic_relation",
  "schema": "csg-relation/0.1",
  "artifact_role": "validated_derived",
  "revision": 1,
  "relation_type": "supports",
  "from_ref": "csg:crystal/A",
  "to_ref": "csg:crystal/B",
  "scope": {
    "kind": "project",
    "subject": "project:project/P"
  },
  "authority_scope": {
    "kind": "project",
    "subject": "project:project/P"
  },
  "semantic_revision": 2,
  "status": "active",
  "created_at": "RFC3339",
  "digest": "sha256:..."
}
```

---

# 23. Hyperedge Schema

Schema ID：

```text
csg-hyperedge/0.1
```

```json
{
  "object_id": "csg:hyperedge/01J...",
  "kind": "semantic_hyperedge",
  "schema": "csg-hyperedge/0.1",
  "artifact_role": "validated_derived",
  "revision": 1,
  "relation_type": "derived_from",
  "source_refs": [
    "csg:crystal/A",
    "csg:crystal/B",
    "csg:crystal/C"
  ],
  "target_ref": "csg:crystal/D",
  "scope": {
    "kind": "project",
    "subject": "project:project/P"
  },
  "status": "active",
  "digest": "sha256:..."
}
```

---

# 24. CrossGraphBridge Schema

Schema ID：

```text
rcg-csg-bridge/0.1
```

relation type：

```text
produced
checkpointed
validated
contradicted
revealed
consumed
updated
derived_across
```

```json
{
  "object_id": "bridge:rcg-csg/01J...",
  "kind": "rcg_csg_bridge",
  "schema": "rcg-csg-bridge/0.1",
  "artifact_role": "validated_derived",
  "revision": 1,
  "resident_ref": "identity:resident/R",
  "line_ref": "rcg:line/L",
  "conversation_node_ref": "rcg:node/N",
  "crystal_ref": "csg:crystal/C",
  "relation_type": "produced",
  "authority_revision": 8,
  "semantic_revision": 4,
  "status": "active",
  "created_at": "RFC3339",
  "digest": "sha256:..."
}
```

---

# 25. ProjectRecord Schema

Schema ID：

```text
project-record/0.1
```

```json
{
  "object_id": "project:project/01J...",
  "kind": "project",
  "schema": "project-record/0.1",
  "artifact_role": "canonical",
  "revision": 1,
  "name": "SOACR",
  "status": "active",
  "owner_refs": [
    "identity:resident/R"
  ],
  "created_at": "RFC3339",
  "updated_at": "RFC3339",
  "digest": "sha256:..."
}
```

---

# 26. ProjectMembership Schema

Schema ID：

```text
project-membership/0.1
```

```json
{
  "object_id": "project:membership/01J...",
  "kind": "project_membership",
  "schema": "project-membership/0.1",
  "artifact_role": "canonical",
  "revision": 1,
  "project_ref": "project:project/P",
  "resident_ref": "identity:resident/R",
  "role": "architect",
  "valid_from": "RFC3339",
  "valid_to": null,
  "status": "active",
  "authority_basis_refs": [],
  "digest": "sha256:..."
}
```

---

# 27. ResponsibilityRecord Schema

Schema ID：

```text
responsibility-record/0.1
```

```json
{
  "object_id": "responsibility:record/01J...",
  "kind": "responsibility",
  "schema": "responsibility-record/0.1",
  "artifact_role": "canonical",
  "revision": 1,
  "resident_ref": "identity:resident/R",
  "project_ref": "project:project/P",
  "task_ref": null,
  "role": "owner",
  "scope": {
    "kind": "project",
    "subject": "project:project/P"
  },
  "valid_from": "RFC3339",
  "valid_to": null,
  "status": "active",
  "authority_basis_refs": [],
  "digest": "sha256:..."
}
```

---

# 28. ProjectionRecord Schema

Schema ID：

```text
projection-record/0.1
```

```json
{
  "object_id": "projection:artifact/01J...",
  "kind": "projection",
  "schema": "projection-record/0.1",
  "artifact_role": "projection",
  "revision": 1,
  "projection_kind": "working_context",
  "source_head_refs": [
    "mneme:head/H42"
  ],
  "source_crystal_refs": [
    "csg:crystal/C1"
  ],
  "scope": {
    "kind": "line",
    "subject": "rcg:line/L"
  },
  "budget": {
    "max_tokens": 12000
  },
  "generator_version": "soacr/0.1",
  "generated_at": "RFC3339",
  "digest": "sha256:..."
}
```

---

# 29. IndexMetadata Schema

Schema ID：

```text
derived-index/0.1
```

```json
{
  "object_id": "projection:index/01J...",
  "kind": "derived_index",
  "schema": "derived-index/0.1",
  "artifact_role": "cache",
  "revision": 1,
  "index_kind": "sqlite_fts",
  "source_head_refs": [
    "mneme:head/H42"
  ],
  "builder_version": "index-builder/0.1",
  "generated_at": "RFC3339",
  "status": "current",
  "digest": "sha256:..."
}
```

---

# 30. SnapshotManifest Schema

Schema ID：

```text
snapshot-manifest/0.1
```

```json
{
  "package_id": "snapshot:package/01J...",
  "schema": "snapshot-manifest/0.1",
  "version": "0.1",
  "created_at": "RFC3339",
  "resident_refs": [
    "identity:resident/R"
  ],
  "memory_head_refs": [
    "mneme:head/H42"
  ],
  "canonical_files": [],
  "derived_files": [],
  "archive_files": [],
  "sha256sums_file": "SHA256SUMS.txt"
}
```

---

# 31. Logical Folder Taxonomy

建議本地 Agent 第一代：

```text
ResidenceRoot/
├─ schemas/
├─ registry/
│  ├─ residents/
│  ├─ projects/
│  └─ source-map/
├─ residents/
│  └─ <resident-id>/
│     ├─ identity/
│     ├─ authority/
│     ├─ memory/
│     │  ├─ records/
│     │  ├─ transactions/
│     │  ├─ heads/
│     │  └─ provenance/
│     ├─ conversations/
│     │  ├─ lines/
│     │  ├─ nodes/
│     │  ├─ edges/
│     │  └─ checkpoints/
│     ├─ semantic/
│     │  ├─ crystals/
│     │  ├─ relations/
│     │  ├─ hyperedges/
│     │  └─ bridges/
│     ├─ projects/
│     ├─ projections/
│     ├─ indexes/
│     ├─ routes/
│     ├─ receipts/
│     └─ archive/
├─ shared/
└─ manifests/
```

這是 logical recommendation，不是唯一 physical backend。

---

# 32. CANONICAL_SOURCE_MAP.json

Root 必須可選擇性提供：

```json
{
  "schema": "canonical-source-map/0.1",
  "object_kinds": {
    "resident": {
      "namespace": "identity:",
      "canonical_store": "registry/residents",
      "schema": "resident-record/0.1"
    },
    "memory_record": {
      "namespace": "mneme:",
      "canonical_store": "residents/<id>/memory/records",
      "schema": "mneme-memory-record/0.1"
    },
    "semantic_crystal": {
      "namespace": "csg:",
      "canonical_store": "residents/<id>/semantic/crystals",
      "artifact_role": "validated_derived",
      "schema": "csg-crystal/0.1"
    }
  }
}
```

AI 啟動時優先讀 source map，而不是全域掃描猜 current authority。

---

# 33. Object Registry

Registry 至少能查：

```text
object_id
kind
schema
current_revision
artifact_role
canonical_location
digest
status
```

Registry 可以用：

- JSONL；
- SQLite；
- database。

但 registry 自身角色必須聲明。

---

# 34. Resolver Interface

概念 API：

```text
resolve(object_ref, requested_representation, authority_context)
```

輸出：

```text
resolved_location
schema
revision
digest
representation
artifact_role
authorization_result
```

---

# 35. MaterializationRequest

Schema：

```json
{
  "object_ref": "csg:crystal/C",
  "representation": "application/json",
  "fidelity": "structured",
  "scope": {
    "kind": "project",
    "subject": "project:project/P"
  },
  "authority_context_ref": "authority:envelope/E",
  "budget": {
    "max_bytes": 1048576
  }
}
```

---

# 36. MaterializationResponse

```json
{
  "object_ref": "csg:crystal/C",
  "schema": "csg-crystal/0.1",
  "revision": 8,
  "digest": "sha256:...",
  "artifact_role": "validated_derived",
  "representation": "application/json",
  "status": "ok",
  "provenance_refs": []
}
```

bytes / payload 可由 runtime transport 提供。

---

# 37. Representation 類型

第一代：

```text
application/json
application/jsonl
text/markdown
text/plain
application/zip
application/vnd.sqlite3
opaque/provider-native
```

---

# 38. Fidelity 類型

```text
overview
semantic
structured
exact
```

若要求 `exact`，resolver 不能用 summary crystal 冒充 exact source。

---

# 39. Markdown Projection Contract

`MEMORY.md`、human profile、project summary 都是 projection。

Header 應至少標：

```text
Projection-Source-Head:
Projection-Generated-At:
Projection-Scope:
Projection-Generator:
```

若 projection 被編輯，只能進 import proposal。

---

# 40. Projection Import

流程：

$$
ProjectionEdit
\rightarrow
Parse
\rightarrow
MappingProfile
\rightarrow
Proposal
\rightarrow
Validate
\rightarrow
Commit.
$$

不能直接覆寫 canonical。

---

# 41. JSON Canonical Serialization

第一代可要求：

- UTF-8；
- LF；
- object keys stable order for canonical digest；
- no NaN / Infinity；
- timestamps RFC3339 UTC；
- NFC Unicode normalization。

若需要 deterministic digest，使用 canonical serializer。

---

# 42. JSONL Ledger

每一行一個完整 JSON object。

禁止：

- multi-line object；
- trailing comments；
- partial writes。

transaction 寫入失敗時不得留下半行。

---

# 43. Atomic Write

對 file-first canonical object：

1. write temp file；
2. fsync if supported；
3. validate；
4. rename atomic replace；
5. update registry；
6. write receipt。

若 registry update 失敗，需 rollback 或 mark inconsistent。

---

# 44. Transaction Boundary

跨 canonical objects 的 operation 必須 transaction 化。

例如：

$$
MemoryRecord
+
MemoryHead
+
TransactionReceipt.
$$

全部成功才 commit。

---

# 45. Derived Rebuild

CSG / indexes / projections 必須有 rebuild procedure。

例如：

```text
rebuild_csg(resident_id, memory_head)
rebuild_indexes(resident_id, source_head)
rebuild_projection(projection_kind, source_refs)
```

---

# 46. Stale 判定

若 derived artifact：

```text
source_head_ref != current_head
```

則：

```text
status = stale
```

不能冒充 current。

---

# 47. Supersession

canonical / crystal 都可有：

```text
supersedes
```

禁止直接抹除 prior revision 的 lineage。

---

# 48. Tombstone

canonical delete 使用 tombstone：

```json
{
  "object_id": "receipt:tombstone/...",
  "target_ref": "mneme:record/R",
  "target_revision": 4,
  "authority_basis_refs": [],
  "reason": "explicit deletion",
  "created_at": "RFC3339"
}
```

---

# 49. Archive

Archive 分：

```text
exact-source
snapshots
retired
legacy
imports
```

`retired` 不等於 deleted。

---

# 50. Snapshot Package

推薦：

```text
PACKAGE/
├─ MANIFEST.json
├─ SHA256SUMS.txt
├─ README.md
├─ canonical/
├─ derived/
└─ archive/
```

---

# 51. Snapshot 驗證

載入前：

1. path traversal check；
2. file count limit；
3. total size limit；
4. manifest parse；
5. digest verify；
6. schema verify；
7. authority / lineage plan；
8. no automatic overwrite。

---

# 52. Backup Restore

Restore：

$$
Backup
\rightarrow
Plan
\rightarrow
CompareHeads
\rightarrow
Validate
\rightarrow
Apply.
$$

禁止：

$$
NewestTimestampWins.
$$

---

# 53. Divergence

如果：

$$
Head_A
$$

與：

$$
Head_B
$$

無 ancestry：

```text
state = diverged
```

不得 last-write-wins。

---

# 54. Legacy Import

legacy file 預設：

```text
artifact_role = legacy
```

import 後先產生 candidate object。

沒有 exact mapping 不得直接 canonicalize。

---

# 55. Migration Contract

每個 migration 有：

```text
migration_id
source_schema
target_schema
source_revision
output_revision
loss_report
validation_report
rollback_plan
receipt
```

---

# 56. Migration 不可語義猜測

unknown field：

- preserve opaque；或
- report loss。

不得 LLM 猜欄位意義後 silent commit。

---

# 57. Schema Registry

建議：

```text
schemas/
├─ resident-record/
│  └─ 0.1.schema.json
├─ line-record/
├─ mneme-memory-record/
├─ csg-crystal/
└─ ...
```

每個 schema 有：

```text
id
version
compatibility
migration_from[]
```

---

# 58. Schema Compatibility

定義：

```text
compatible_read
compatible_write
migration_required
unsupported
```

Read compatible 不表示 write compatible。

---

# 59. Unknown Schema

identity / authority / canonical memory 遇 unknown schema：

```text
fail_closed
```

derived / archive 可保存 opaque。

---

# 60. Secret Plane

Secret 不進本規格普通 object store。

只保存：

```text
secret_capability_ref
credential_presence
credential_scope
```

禁止 raw token 進：

- crystal；
- manifest；
- route；
- memory record；
- public receipt。

---

# 61. Public / Private Projection

Private canonical object 要產 public projection：

$$
Private
\rightarrow
Declassification
\rightarrow
Redaction
\rightarrow
PublicProjection.
$$

Summarization 不能自動 declassify。

---

# 62. Scope Promotion

memory scope promotion：

$$
line
\rightarrow
project
\rightarrow
resident
\rightarrow
shared/public
$$

每次 promotion 必須重新驗：

- authority；
- privacy；
- stability；
- provenance；
- contradiction；
- declassification。

---

# 63. Scope Demotion

active project memory可轉：

```text
project_historical
archive
```

保留 provenance，但退出 default reveal。

---

# 64. Retention Class

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

Retention 不等於 scope。

---

# 65. Trust Class

```text
canonical
validated_derived
candidate
external_untrusted
legacy
unknown
```

Trust class 必須跟著 provenance 傳播。

---

# 66. Mixed Trust

derived crystal source 混有 untrusted：

第一代保守：

$$
Trust(C^\*)
\le
\min_i Trust(Source_i).
$$

---

# 67. Cross-Resident Storage

不同 resident private roots：

$$
\mathcal W_{R_A}^{private}
\cap
\mathcal W_{R_B}^{private}
=
\varnothing
$$

為 logical default。

shared objects 使用獨立 `shared/` scope 或 shared backend。

---

# 68. Relationship Scope

relationship object 不必物理放雙方 private root。

建議獨立 logical scope：

```text
relationship:R_A:R_B
```

並各自 authorization。

---

# 69. Cross-Repo Reference

禁止以 brittle relative path 作 canonical cross-system link。

使用：

```text
namespace + object_ref
```

resolver 決定 backend。

---

# 70. Cross-Runtime Reference

Web / Agent 共用 ObjectRef。

不同 runtime 只換 resolver / representation。

---

# 71. Provider Native Resource

provider thread / browser / terminal 使用：

```text
opaque/provider-native
```

保存 opaque provider resource ref。

它不是 object ownership transfer。

---

# 72. MRMIC/NVCL Resource Bridge

可有：

```text
runtime_resource_ref
provider
resource_kind
workspace_ref
owner_resident_ref
presence_state
```

presence 為 ephemeral。

---

# 73. Receipt Plane

第一代 receipt kinds：

```text
identity_resolution
fork
resume
handoff
delegation
memory_commit
crystal_validation
route_promotion
revocation
migration
snapshot
restore
```

---

# 74. Receipt 原則

Receipt：

- append-only；
- immutable；
- correction by new receipt；
- timestamped；
- evidence-linked。

---

# 75. Dependency Graph

建立 operational dependency：

```text
derived_from
indexed_from
projected_from
compiled_from
authorized_by_revision
validated_by
```

用途：

- invalidation；
- rebuild；
- GC；
- audit。

此 dependency graph 不等於 CSG。

---

# 76. Invalidation

source revision 改變：

$$
InvalidateClosure(source).
$$

影響：

- crystals；
- indexes；
- projections；
- compiled routes；
- caches。

---

# 77. Garbage Collection

只有符合全部條件才 physical delete：

1. non-canonical；
2. non-archive-required；
3. no active dependency；
4. retention allows；
5. audit policy allows。

---

# 78. Working Context Storage

working context 預設：

```text
artifact_role = projection
retention = session
```

不進 canonical memory。

---

# 79. Context Cache

context bundle 可以 cache，但 key 包含：

```text
resident_id
line_id
memory_head
semantic_revision
authority_revision
runtime_profile_revision
```

任何 mismatch 失效。

---

# 80. Web Profile Storage

Web 可只暴露 object API：

```text
resident.current
line.current
memory.reveal
memory.source
crystal.get
project.state
proposal.create
```

不暴露 physical filesystem。

---

# 81. Agent Profile Storage

Agent 可同時使用：

- Object API；
- filesystem；
- MCP resource；
- SQLite projection。

但都 resolve 到同一 logical object identity。

---

# 82. Minimal Portable State

在線 shared storage 存在時：

```json
{
  "resident_ref": "identity:resident/R",
  "line_ref": "rcg:line/L",
  "checkpoint_ref": "rcg:checkpoint/C",
  "memory_head_ref": "mneme:head/H",
  "authority_revision": 7
}
```

---

# 83. Offline Portable State

增加：

- selected canonical memory；
- selected crystals；
- schemas；
- exact source spans；
- manifest；
- digests。

---

# 84. Portability 不等於 Full Clone

portable continuation 不需要複製整個 Residence。

只需：

$$
References
+
Checkpoint
+
RequiredMaterial.
$$

---

# 85. File Naming

machine canonical object 可：

```text
<kind>_<object-id>_r<revision>.json
```

但 machine logic 不能靠 filename parsing。

---

# 86. Human Document Naming

正式論文：

```text
<Series>_<Paper>_<Version>_<Date>.md
```

可讀性優先。

---

# 87. INDEX.json

每個大型 folder 可有：

```json
{
  "schema": "directory-index/0.1",
  "entries": [
    {
      "object_ref": "csg:crystal/C",
      "relative_path": "crystals/C.json",
      "revision": 1,
      "digest": "sha256:..."
    }
  ]
}
```

---

# 88. README.md

README 是 human explanation。

不能替代 INDEX.json / registry。

---

# 89. Source Map 優先順序

AI 啟動：

1. read `CANONICAL_SOURCE_MAP.json`；
2. read schema registry；
3. resolve required objects；
4. only then fallback to search。

---

# 90. Filename Search 是 Fallback

只有 object registry / source map 無法處理 legacy / unknown 時，才用 filename / content search。

---

# 91. Source Fidelity Class

```text
exact_bytes
exact_text
structured_record
semantic_crystal
human_projection
index_only
```

runtime 必須知道當前拿到哪一級。

---

# 92. Exact Source

要求 exact quote：

只能使用：

```text
exact_text
exact_bytes
```

不能使用 semantic crystal。

---

# 93. Semantic Recall

overview query：

可以從：

```text
semantic_crystal
```

開始。

---

# 94. Current Identity

只能用 canonical identity / authority plane。

不能用 identity_context_crystal。

---

# 95. Current Responsibility

只能用 ResponsibilityRecord。

responsibility_context_crystal 僅輔助理解。

---

# 96. Current Project State

可由 canonical decision + project state projection。

projection需綁 current source revisions。

---

# 97. Human Review

human-facing Markdown 可以由：

$$
Projection(
Canonical+Derived
)
$$

生成。

---

# 98. Storage Error Classes

```text
not_found
unauthorized
unknown_schema
digest_mismatch
stale
diverged
unsupported_representation
resolver_error
backend_unavailable
invalid_scope
invalid_revision
```

---

# 99. Error Semantics

`not_found` 與 `unauthorized` 是否區分，依 metadata-hiding policy。

---

# 100. Fail-Closed Cases

identity / authority / canonical memory：

- unknown schema；
- diverged head；
- invalid digest；
- stale authority；
- invalid scope。

全部 fail closed。

---

# 101. Derived Failover

CSG / index / projection fail：

可 fallback 到 canonical slow path。

---

# 102. Canonical Failure

canonical source unavailable：

不可拿 stale projection冒充 current。

---

# 103. Rebuild Procedure

完整 rebuild：

```text
load canonical identity
load canonical authority
load canonical memory
load lineage ledger
load project/responsibility
rebuild CSG
rebuild indexes
rebuild projections
rebuild route candidates
```

---

# 104. Rebuild Verification

比較：

- object counts；
- semantic digests；
- current heads；
- relation counts；
- sample recall；
- provenance closure。

---

# 105. Disaster Recovery Gate

只有：

```text
identity valid
authority valid
memory heads valid
lineage valid
```

才允許恢復 active runtime。

---

# 106. Performance Baseline

應測：

- object resolve latency；
- canonical read；
- crystal read；
- projection build；
- index rebuild；
- snapshot restore。

---

# 107. Scalability Baseline

測：

$$
10^3,\ 10^5,\ 10^6
$$

objects。

觀察 registry / resolver / index latency。

---

# 108. Security Baseline

測：

- cross-resident access；
- path traversal；
- stale permission；
- forged object ref；
- digest tamper；
- unknown schema；
- malicious archive。

---

# 109. Test Fixture Layout

建議：

```text
fixtures/
├─ resident-a/
├─ resident-b/
├─ shared-project/
├─ legacy/
├─ corrupted/
├─ diverged/
└─ malicious-archive/
```

---

# 110. Acceptance Tests

## S01 — Object ID Stability

move path 後 ID 不變。

## S02 — Digest Tamper

bytes 修改後 fail。

## S03 — Unknown Schema

identity object fail closed。

## S04 — Projection Rebuild

projection 刪除後重建。

## S05 — Index Rebuild

SQLite 刪除後重建。

## S06 — Cross-Resident Isolation

A 無權讀 B private。

## S07 — Scope Enforcement

Project A 不讀 Project B。

## S08 — Current Revision

舊 revision 不冒充 current。

## S09 — Divergence

兩 head 無 ancestry時 fail closed。

## S10 — Legacy Import

legacy 不直接 canonical。

## S11 — Snapshot Path Traversal

惡意路徑拒絕。

## S12 — Secret Exclusion

manifest / crystal 無 raw credential。

## S13 — Exact Fidelity

exact query 不用 summary 代替。

## S14 — Identity Source

identity_context_crystal 不可 mint resident。

## S15 — Responsibility Source

responsibility_context_crystal 不可 mint responsibility。

## S16 — Portable State

不同 root 仍 resolve。

## S17 — Cross-Repo Reference

repo 移動後 ObjectRef 可 resolve。

## S18 — Runtime Projection

Web / Agent projection不同但 canonical相同。

## S19 — Tombstone

deleted object 歷史可 audit。

## S20 — Invalidation Closure

source 改變導致 derived stale。

---

# 111. Minimum Implementation Milestone A0

必須完成：

```text
ResidentRecord
InstanceRecord
LineRecord
MemoryRecord
MemoryHead
ProjectRecord
ResponsibilityRecord
CrystalRecord
Object Registry
ArtifactAddress
Resolver
Source Map
Validation
```

---

# 112. Milestone A1

增加：

```text
ConversationNode
ConversationEdge
Checkpoint
CrossGraphBridge
Projection
SQLite index
```

---

# 113. Milestone A2

增加：

```text
snapshot
restore
migration
legacy import
invalidation graph
portable bundle
```

---

# 114. Milestone A3

與 TW-B 對接：

```text
route object
route dependency
capability revision
permission revision
compiled hyperlink target
```

---

# 115. 不變式總表

## ST-1

$$
\boxed{
\text{Canonicality Is Declared, Not Guessed}.
}
$$

## ST-2

$$
\boxed{
\text{Format}
\neq
\text{Authority}.
}
$$

## ST-3

$$
\boxed{
\text{Path}
\neq
\text{Object ID}.
}
$$

## ST-4

$$
\boxed{
\text{Object ID}
\neq
\text{Credential}.
}
$$

## ST-5

$$
\boxed{
\text{Projection}
\neq
\text{Canonical State}.
}
$$

## ST-6

$$
\boxed{
\text{Index}
\neq
\text{Canonical State}.
}
$$

## ST-7

$$
\boxed{
\text{Persistent Derived}
\neq
\text{Canonical}.
}
$$

## ST-8

$$
\boxed{
\text{Addressable}
\not\Rightarrow
\text{Readable}.
}
$$

## ST-9

$$
\boxed{
\text{Summarization}
\neq
\text{Declassification}.
}
$$

## ST-10

$$
\boxed{
\text{Legacy Parse}
\neq
\text{Canonical Adoption}.
}
$$

## ST-11

$$
\boxed{
\text{Invalid}
\neq
\text{Absent}.
}
$$

## ST-12

$$
\boxed{
\text{Canonical Core}
\rightarrow
\text{Rebuild Derived World}.
}
$$

---

# 116. 與既有系統的對接

## LIMEN

使用：

- ResidentRecord；
- InstanceRecord；
- LineRecord；
- authority revision；
- ObjectRef。

LIMEN 不直接靠 folder name resolve resident。

## MNEME

使用：

- MemoryRecord；
- Transaction；
- Head；
- Provenance；
- Projection。

## SOACR

使用：

- ArtifactAddress；
- fidelity；
- scope；
- projection；
- materialization。

## CSG

使用：

- CrystalRecord；
- Relation；
- Hyperedge；
- Bridge。

## CHM / UNPNP

使用：

- stable ObjectRef；
- revision；
- digest；
- scope；
- dependency graph；
- resolver。

## MRMIC/NVCL

使用：

- provider-native resource ref；
- resident/project mapping；
- projection record；
- runtime presence。

---

# 117. 實作原則

本規格第一代建議採：

$$
\boxed{
\text{File-first canonical core}
+
\text{SQLite derived indexes}
+
\text{Typed resolver}
}
$$

理由：

- 可 audit；
- 可 Git / snapshot；
- 易 rebuild；
- 容易先在本地 Agent 驗證；
- 不需要一開始就引入大型 distributed DB。

未來可以替換 backend，但 object semantics 不變。

---

# 118. 第一代建議 Backend

```text
Canonical JSON / JSONL:
  filesystem

Registry:
  SQLite + rebuildable JSONL source

CSG:
  JSON / JSONL + SQLite adjacency projection

Projection:
  Markdown / JSON

Index:
  SQLite FTS / vector optional

Archive:
  filesystem + ZIP/TAR snapshots
```

---

# 119. Canonical Commit 順序

一次 canonical mutation：

1. validate proposal；
2. write canonical object；
3. write transaction / receipt；
4. advance head；
5. update registry；
6. mark derived stale；
7. asynchronously rebuild derived state。

---

# 120. 最終工程結論

Residence / CSG 儲存層的核心不是「把 AI 記憶分成很多資料夾」，而是讓每一個 object 都能回答：

> 我是什麼？  
> 我是不是 canonical？  
> 我的 schema 是什麼？  
> 我的 revision 是什麼？  
> 我屬於誰／哪個 scope？  
> 我從哪裡來？  
> 誰能讀？  
> 誰能改？  
> 我被誰 supersede？  
> 如果我失效，哪些 downstream 要失效？  
> 我可以用哪個 representation materialize？  
> physical path 改變後，我還是不是同一 object？

因此本規格的最終原則是：

$$
\boxed{
\text{AI-native storage must be semantically addressable before it is operationally scalable}.
}
$$

以及：

$$
\boxed{
\text{Canonical storage preserves truth;}
}
$$

$$
\boxed{
\text{derived structures preserve speed;}
}
$$

$$
\boxed{
\text{resolvers preserve portability;}
}
$$

$$
\boxed{
\text{schemas preserve meaning}.
}
$$

---

## Appendix A — 第一代 Schema ID 清單

```text
resident-record/0.1
instance-record/0.1
line-record/0.1
conversation-node/0.1
rcg-edge/0.1
rcg-checkpoint/0.1
mneme-memory-record/0.1
mneme-transaction/0.1
mneme-head/0.1
csg-crystal/0.1
csg-relation/0.1
csg-hyperedge/0.1
rcg-csg-bridge/0.1
project-record/0.1
project-membership/0.1
responsibility-record/0.1
projection-record/0.1
derived-index/0.1
snapshot-manifest/0.1
canonical-source-map/0.1
directory-index/0.1
```

---

## Appendix B — 第一代 Object Kind 清單

```text
resident
instance
conversation_line
conversation_node
conversation_edge
line_checkpoint
memory_record
memory_transaction
memory_head
semantic_crystal
semantic_relation
semantic_hyperedge
rcg_csg_bridge
project
project_membership
responsibility
projection
derived_index
snapshot
receipt
```

---

## Appendix C — 下一份規格的接口

TW-B 將直接使用本文件的：

```text
ArtifactAddress
ObjectRef
revision
digest
scope
authority_revision
semantic_revision
dependency graph
resolver
```

並新增：

```text
CompiledRoute
RouteReceipt
CapabilityEnvelope
PermissionBinding
SafeReachableWorld
RevocationClosure
PathPromotion
PathDemotion
FallbackPolicy
```

形成完整 Authorized Hyperlink Runtime。
