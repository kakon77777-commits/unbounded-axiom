---
title: "AI Matrix Ledger Format：從試算表格式到可追溯計算結構"
title_en: "AI Matrix Ledger Format: From Spreadsheet Formats to Traceable Computational Structure"
series: "矩陣原生智能與可稽核計算系列"
series_en: "Matrix-Native Intelligence and Auditable Computation Series"
series_id: "EML-MNIAC-2026"
paper_id: "EML-MNIAC-2026-06"
version: "v0.1"
date: "2026-08-16"
language: "zh-Hant"
document_type: "系列第06篇／MLF 1.0 統一格式論文／Canonical Representation"
status: "Public Draft"
author: "Neo.K（許筌崴）／EveMissLab"
depends_on:
  - "EML-MNIAC-2026-05 試算表智能的可證偽實驗 v0.1"
internal_artifacts:
  - "MLF_1.0_技術規格_繁中.md"
  - "MLF_1.0_Specification_EN.md"
  - "MLF_1.0_Release_Notes.md"
  - "MLF_1.0_GitHub發布與命名說明.md"
  - "MLF Compiler 1.0.0"
  - "kakon77777-commits/matrix-ledger-format"
canonical_keywords:
  - MLF
  - AI Matrix Ledger Format
  - Canonical Structure
  - Traceable Projection
  - Formula AST
  - Dependency Graph
  - Route Graph
  - Provenance
  - Conversion Loss
  - Fingerprint
  - Human Projection
  - AI Projection
---

# AI Matrix Ledger Format
## 從試算表格式到可追溯計算結構

**AI Matrix Ledger Format:  
From Spreadsheet Formats to Traceable Computational Structure**

---

## 摘要

本文是《矩陣原生智能與可稽核計算》系列第 06 篇，正式整理 AI Matrix Ledger Format（MLF）1.0 的理論位置、穩定核心、格式結構、投影原則、損失模型與工程邊界。

前五篇的研究路徑由 CSV 模型狀態、帳本約束、Spreadsheet Runtime、MMR / MMLC 到 MMR-Bench，逐步揭露一個共同問題：**單一平面表示不足以同時保存計算物件的值、身份、公式、依賴、方向、來源、歷史、視覺角色與不同使用者／模型需要的讀取方式。**

因此 MLF 1.0 不再問：

> 「Excel 能不能成為 AI？」

而改問：

> **當同一計算／知識物件需要被試算表、人類、AI、圖演算法、張量模型與執行器以不同方式讀取時，哪一層應被視為 canonical，哪些只應被視為 projection？**

MLF 1.0 的核心答案為：

$$
\boxed{
\text{完整結構是規範核心；}
}
$$

$$
\boxed{
\text{線性、張量、圖、執行與人類閱讀皆是可追溯投影。}
}
$$

MLF 文件可形式化為：

$$
\boxed{
\mathcal F
=
(C,M,R,S,A,G,P,H,V,L)
}
$$

其中：

- $C$：computational substrate contract；
- $M$：matrices / cells；
- $R$：regions / semantic roles；
- $S$：semantic / presentation style；
- $A$：formula AST 與 derived assets；
- $G$：dependency graph；
- $P$：route / traversal graph；
- $H$：provenance 與 append-only history；
- $V$：human / model projections；
- $L$：conversion-loss / warnings。

MLF 的目的不是取代 ONNX、MLIR、Apache Arrow、資料庫、Spreadsheet、Workflow IR 或所有知識圖譜格式。ONNX 專注於可攜 computation graph；MLIR 專注於多層 compiler IR 與 lowering；Arrow 專注於跨語言高效率 columnar memory / transport；W3C PROV 提供跨系統 provenance 模型。MLF 的研究位置更窄：**保存「矩陣化知識與計算」從原始人類結構到模型／執行投影時容易遺失的 identity、formula source+AST、dependency、route、role、provenance 與 conversion-loss evidence。**

本文亦區分 MLF 1.0 的 stable core 與 repository 中的 research/governed modules。MLF 1.0 / MLF Compiler 1.0.0 的發布候選紀錄顯示 54 項自動測試通過、Manifest JSON Schema 通過、MLF 0.1 可讀、0.1→1.0 遷移保持 semantic 與 presentation fingerprints，且核心 CLI 可在不依賴 NumPy／PyTorch 的乾淨環境安裝執行。相對地，learned dependency inference、calibration、OOD routing、自動審核與外部自然工作簿授權仍屬研究或治理模組，不應被當成 MLF 1.0 已證實能力。

---

# 1. 從 Spreadsheet 到 Format 的轉折

前一階段的工作簿研究已經顯示：

$$
Value
\neq
Formula
\neq
Cache
\neq
Dependency
\neq
Role
\neq
Provenance.
$$

但 `.xlsx` 的存在並不自動保證上述層全部能被：

- AI 讀懂；
- 圖演算法直接使用；
- 轉換器無損映射；
- 人類投影重建；
- 版本差分比較。

所以真正問題變成：

$$
\boxed{
\text{如何建立一個「結構先於投影」的交換層？}
}
$$

MLF 就是在這個問題上出現。

---

# 2. MLF 不應被理解成「更複雜的 Excel」

若：

$$
XLSX
$$

是輸入來源，

MLF 可以進行：

$$
XLSX
\rightarrow
MLF.
$$

但 MLF 本身不等於：

$$
XLSX'.
$$

因為它也可以接：

$$
CSV,
$$

$$
Markdown,
$$

$$
JSON,
$$

或其他 structured source。

因此：

$$
\boxed{
MLF
\neq
SpreadsheetFileFormat.
}
$$

更精確是：

$$
\boxed{
MLF
=
\text{Structured Interchange Format for Matrix-Shaped Knowledge and Computation}.
}
$$

---

# 3. Canonical 的真正意思

本文使用 canonical，不表示：

> MLF 是宇宙唯一正確的知識本體。

而表示：

> **在一個 MLF document scope 內，完整結構是格式契約中的規範來源；各種 projection 不應偷偷反過來覆蓋它。**

所以：

$$
\boxed{
Canonical_{MLF}
\neq
UltimateOntology.
}
$$

---

# 4. MLF 文件的十元組

MLF 1.0 將文件表示為：

$$
\boxed{
\mathcal F
=
(C,M,R,S,A,G,P,H,V,L).
}
$$

此結構的真正意義不是多放幾個 metadata 欄。

而是將先前容易互相坍縮的層拆開。

---

# 5. $C$ — Computational Substrate Contract

 $C$ 描述：

> 這個文件的計算語義需要哪些邏輯條件？

它不直接指定：

- CPU；
- GPU；
- specific spreadsheet engine；
- cluster vendor。

而可以描述：

- deterministic / nondeterministic；
- numeric precision；
- cycle semantics；
- required operators；
- execution assumptions；
- synchronization boundaries。

因此：

$$
\boxed{
LogicalExecutionContract
\neq
PhysicalHardware.
}
$$

---

# 6. 邏輯平行不等於實體平行

如果 graph 中有：

$$
T_1\parallel T_2,
$$

只代表：

$$
T_1
$$

與：

$$
T_2
$$

在 dependency 上可獨立。

不能推出：

$$
\boxed{
\text{它們在硬體上一定同時跑。}
}
$$

所以：

$$
\boxed{
LogicalParallelism
\neq
PhysicalParallelism.
}
$$

MLF 1.0 甚至明確把：

> 不保證 logical parallelism 帶來 physical speedup

列為 non-goal。

---

# 7. $M$ — Matrix and Cells

MLF 中一個 cell 不只是一個 scalar。

可以寫成：

$$
\boxed{
c_i
=
\langle
id,
matrix,
coordinate,
value,
type,
role,
style,
formula,
provenance
\rangle.
}
$$

其中：

$$
coordinate(c_i)
$$

與：

$$
id(c_i)
$$

不能被視為同一概念。

---

# 8. Coordinate 不等於 Identity

若一個 cell 從：

$$
B3
$$

移到：

$$
C7,
$$

它的 coordinate 改變。

但如果只是 presentation rearrangement，

stable：

$$
cell\_id
$$

不應改。

因此：

$$
\boxed{
Location
\neq
Identity.
}
$$

這是 MMR / MMLC 的 identity-preservation 原則正式進入交換格式。

---

# 9. Missing 不等於 Zero

MLF 要求：

$$
typed\_missing
$$

必須可區分於：

$$
0,
$$

$$
"",
$$

以及：

$$
formula\_error.
$$

所以：

$$
\boxed{
Absent
\neq
Zero
\neq
EmptyString
\neq
Error.
}
$$

這種 distinction 在 AI ingest 時尤其重要。

如果 flatten 過程把它們全部轉成：

```text
0
```

則已發生語義損失。

---

# 10. $R$ — Region and Semantic Role

Region 對矩陣的某個 meaningful subset 給予 stable identity。

例如：

- header；
- data body；
- formula band；
- assumption；
- summary；
- table；
- named range。

所以：

$$
\boxed{
Region
\neq
JustBoundingBox.
}
$$

bounding box 是位置，

region 還具有角色。

---

# 11. Semantic Role 與 Presentation Style 必須拆開

例如：

```text
黃色底
```

可能表示：

$$
warning
$$

也可能只是：

$$
theme.
$$

因此 MLF 將：

$$
\boxed{
semantic\ style
}
$$

與：

$$
\boxed{
presentation\ style
}
$$

分離。

所以 theme change 可以：

$$
PresentationFingerprint
\rightarrow
PresentationFingerprint'
$$

但：

$$
SemanticFingerprint
$$

保持不變。

---

# 12. $A$ — Formula Source + AST

一個公式至少有三個互相關聯但不應互相取代的表示：

1. source formula；
2. normalized semantic AST；
3. dependency edges。

因此：

$$
\boxed{
FormulaSource
+
AST
+
DependencyGraph.
}
$$

---

# 13. 為什麼三個都要保存？

例如：

```text
=SUM(A1:A3)
```

source formula 保留：

- 原語言；
- human-editable syntax。

AST 保留：

- operator structure；
- normalized semantics。

dependency graph 保留：

- 哪些 cells 是 prerequisites。

如果只保留 source：

$$
Parser
$$

每次都要重新猜。

如果只保留 AST：

原始：

$$
source syntax
$$

可能丟失。

如果只保留 dependency：

$$
SUM
$$

這個 operator semantics 又消失。

因此：

$$
\boxed{
No Single Formula Representation Is Sufficient.
}
$$

---

# 14. 三者衝突時不能偷偷選一個

假設：

$$
SourceFormula
$$

表示：

$$
A+B,
$$

但 AST 表示：

$$
A-B.
$$

同時 dependency 又引用：

$$
A,C.
$$

系統不能：

> 「我覺得 AST 比較像真的。」

而直接抹掉其餘兩層。

正確處置：

$$
\boxed{
ConflictRecord.
}
$$

---

# 15. $G$ — Dependency Graph

Dependency edge 應保存：

- stable edge ID；
- dependent cell；
- prerequisite cell；
- relation；
- required flag；
- reference kind；
- evidence / provenance。

MLF reference orientation 中：

$$
source
$$

是 dependent，

$$
target
$$

是 prerequisite。

這需要明文定義，避免不同 graph convention 互相顛倒。

---

# 16. Dependency Graph 不等於 Route Graph

這是整個格式最重要的分離之一。

$$
G
$$

回答：

> **什麼依賴什麼？**

而：

$$
P
$$

回答：

> **我要怎麼讀／查／執行這個結構？**

因此：

$$
\boxed{
Dependency
\neq
Traversal.
}
$$

---

# 17. $P$ — Route Graph

可定義：

- row-major；
- column-major；
- dependency-topological；
- reverse dependency；
- region-first；
- conflict-first；
- task-specific route。

一個 route 可以用於：

- summary；
- formula audit；
- evidence trace；
- conflict check；
- model training；
- human review。

---

# 18. Route 不是完整文件

如果 AI 只拿到：

$$
\pi_Q(\mathcal F),
$$

那只是：

$$
\boxed{
TaskProjection.
}
$$

不是：

$$
\boxed{
\mathcal F.
}
$$

所以 route / projection 必須留下：

$$
source\ linkage.
$$

---

# 19. Reversible Projection 的最低定義

設：

$$
\Phi:
\mathcal F
\rightarrow
V.
$$

若 $V$ 是 task projection，

則至少應保存反向 linkage：

$$
\lambda:
V
\rightarrow
\mathcal P(\mathcal F)
$$

使每個 projection element 能指出：

- 來自哪些 cells；
- 哪些 regions；
- 哪些 edges；
- 省略哪些 material。

因此：

$$
\boxed{
Projection
\neq
Destructive Flattening.
}
$$

---

# 20. Human-Readable 不等於永遠攤平

MLF 的設計句可以寫成：

$$
\boxed{
HumanReadable
\neq
PermanentlyFlattened.
}
$$

同樣：

$$
\boxed{
AIReadable
\neq
Opaque.
}
$$

AI 不需要因為「吃 tensor」就失去：

- source identity；
- provenance；
- dependency；
- route origin。

---

# 21. $H$ — Provenance and Append-Only History

MLF provenance event 可以記錄：

- import；
- migration；
- validation；
- inference；
- review；
- promotion；
- deidentification；
- export。

所以：

$$
\boxed{
State
+
History
}
$$

被同時保存。

---

# 22. 與 W3C PROV 的關係

W3C PROV 已經提供：

- Entity；
- Activity；
- Agent；

以及跨系統 provenance interchange 的一般模型。

因此 MLF 不應宣稱：

> 「第一次發明 provenance。」

MLF 的研究重點是：

> 如何把 provenance 直接綁到 matrix/cell/formula/edge/projection 的 AI-native exchange context。

---

# 23. Prediction、Decision、Promotion 三分

MLF governed inference 明確分：

$$
\boxed{
prediction
}
$$

$$
\boxed{
decision
}
$$

$$
\boxed{
promotion.
}
$$

因此：

$$
ModelConfidence=0.999
$$

不能直接：

$$
\Rightarrow
FormalEdge.
$$

---

# 24. 為什麼這三層重要？

AI 可以產生：

$$
prediction:
A\rightarrow B.
$$

review policy 決定：

$$
decision:
accept.
$$

最後才：

$$
promotion:
G
\leftarrow
G\cup\{A\rightarrow B\}.
$$

所以：

$$
\boxed{
Inference
\neq
Authority.
}
$$

---

# 25. $L$ — Conversion Loss

MLF 的一個關鍵思想是：

> **轉換失敗不是非黑即白。**

匯入可能是：

$$
lossless,
$$

$$
partial,
$$

$$
unsupported,
$$

$$
warning.
$$

因此：

$$
\boxed{
CompilationSuccess
\neq
LosslessConversion.
}
$$

---

# 26. CSV 是最好的反例

CSV 可以保留：

- 二維位置；
-文字；
-基本數值。

但通常無法自然保存：

- multiple sheets；
- semantic style；
- formula AST；
- dependency history；
- role；
- provenance。

所以：

$$
CSV
\rightarrow
MLF
$$

時可以建立新結構，

但如果原 CSV 本身沒有這些資訊，

不能假裝：

$$
\boxed{
\text{它們原本就存在。}
}
$$

---

# 27. XLSX Import 也不是無損神話

XLSX 可以嘗試映射：

$$
Worksheet
\rightarrow
Matrix,
$$

$$
Cell
\rightarrow
Cell,
$$

$$
Formula
\rightarrow
Source+AST,
$$

$$
NamedRange
\rightarrow
Region.
$$

但：

$$
Style
\rightarrow
SemanticRole
$$

常常只是 inference。

所以必須標記：

$$
\boxed{
InferredRole
\neq
ExplicitRole.
}
$$

---

# 28. Export Loss 也必須寫出來

假設：

$$
MLF
\rightarrow
CSV.
$$

則 export report 可以寫：

```json
{
  "target": "csv",
  "losses": [
    "dependency_graph",
    "provenance_history",
    "style_semantics",
    "human_projection_policies"
  ]
}
```

這表示：

$$
\boxed{
\text{Loss is a first-class output.}
}
$$

---

# 29. 四層 Fingerprint

MLF 支援四種 fingerprint：

$$
\boxed{
F_{struct}
}
$$

$$
\boxed{
F_{content}
}
$$

$$
\boxed{
F_{semantic}
}
$$

$$
\boxed{
F_{presentation}.
}
$$

這使不同類型變更可以被分開判定。

---

# 30. 為什麼一個 hash 不夠？

若只 hash 全文件 bytes：

$$
H_{bytes},
$$

只要改：

- 換行；
- ZIP packing；
- style；
- field order；

就可能完全不同。

但我們想問的可能是：

> 語義有沒有改？

所以需要：

$$
\boxed{
CanonicalSemanticFingerprint.
}
$$

---

# 31. Presentation-only Change

若只是：

- theme；
- fill；
- font；
- border；

改變，

而 formula、value、dependency 不變，

則希望：

$$
F_{presentation}\neq F'_{presentation},
$$

但：

$$
\boxed{
F_{semantic}=F'_{semantic}.
}
$$

這使：

$$
\boxed{
VisualChange
\neq
SemanticChange.
}
$$

成為可測命題。

---

# 32. Content Change

若：

$$
A1=3
$$

改成：

$$
A1=4,
$$

那麼：

$$
F_{content}
$$

應改。

若 formula：

$$
=A1+B1
$$

改為：

$$
=A1-B1,
$$

則：

$$
F_{semantic}
$$

也應改。

---

# 33. Checksums 與 Fingerprints 不是同一層

`checksums.json` 回答：

> 這些 package bytes 有沒有被改？

Fingerprint 回答：

> 結構／內容／語義／呈現是否等價？

所以：

$$
\boxed{
ByteIntegrity
\neq
SemanticIdentity.
}
$$

---

# 34. Checksums 也不能證明作者身份

SHA-256 可以證明：

$$
bytes
$$

和紀錄一致。

不能證明：

- authorship；
- authorization；
- lawful authority；
- truth。

所以：

$$
\boxed{
Hash
\neq
Authority.
}
$$

---

# 35. Physical Container

MLF 1.0 有：

$$
.mlfdir
$$

開發／檢查形態，

以及：

$$
.mlf
$$

single-file exchange container。

`.mlf` 是 deterministic ZIP-compatible container。

唯一 mandatory entry：

$$
\boxed{
manifest.json.
}
$$

---

# 36. 為什麼 Manifest 是唯一入口？

因為 reader 不應靠：

> 猜資料夾長什麼樣。

而應從：

$$
Manifest
$$

取得：

- version；
- document ID；
- conformance；
- matrices；
- graphs；
- provenance；
- projections；
- reports。

這是一個：

$$
\boxed{
Self-Describing Package Contract.
}
$$

---

# 37. Conformance Profile

MLF 1.0 不要求：

> 支援一個 feature 就自稱完整 MLF。

reader / writer 必須聲明 profile。

例如：

$$
core,
$$

$$
ledger,
$$

$$
ai\text{-}projection,
$$

$$
distributed,
$$

以及 human-related profile。

這種設計避免：

$$
\boxed{
PartialSupport
\rightarrow
FalseCompleteClaim.
}
$$

---

# 38. Core Profile

Core 至少處理：

- container；
- manifest；
- matrices；
- cells；
- type；
- coordinate；
- stable ID；
- checksums；
- validation。

這是：

$$
\boxed{
Minimum Structural Interchange.
}
$$

---

# 39. Ledger Profile

Ledger 再加入：

- provenance；
- append-only history；
- source reference；
- conversion loss；
- explicit conflict。

所以：

$$
\boxed{
Structure
\rightarrow
TraceableStructure.
}
$$

---

# 40. AI Projection Profile

AI projection 保存：

- sequence view；
- matrix view；
- tensor view；
- graph view；
- mask；
- task projection。

但重要的是：

$$
\boxed{
ProjectionMetadata
}
$$

而不是：

$$
\boxed{
「丟給模型的 tensor 就是全部真相」。
}
$$

---

# 41. Distributed Profile

Distributed profile 可以描述：

- shardability；
- partition hints；
- dependency stages；
- synchronization boundary。

但：

$$
\boxed{
DistributedMetadata
\neq
ActualDistributedExecution.
}
$$

這延續了：

$$
LogicalParallelism
\neq
PhysicalExecution.
$$

---

# 42. AI Training Task 也可以被格式化

MLF 可保存：

```text
task_id
type
visible_regions
masked_cells
allowed_routes
targets
leakage_policy
evaluation
```

例如：

$$
cell\ reconstruction.
$$

這使 dataset generation 不再只是：

$$
Input,
Label.
$$

而可以保存：

$$
\boxed{
InputStructure
+
AllowedView
+
HiddenTarget
+
LeakagePolicy.
}
$$

---

# 43. 這直接吸收 MMR-Bench 的教訓

MMR-Bench v0.1 曾因：

$$
direction\ token
$$

洩漏答案。

所以 MLF task profile 明確要求：

$$
\boxed{
TrainingInput
\neq
Answer.
}
$$

並可保存：

$$
leakage\_policy.
$$

這是 benchmark 失敗經驗進入格式治理的例子。

---

# 44. 參考讀取流程

MLF reference flow：

```text
Open container
→ validate manifest / safe paths
→ load substrate
→ build matrix index
→ validate cells / roles
→ load formula AST
→ build dependency graph
→ check cycles / consistency
→ load routes / projections
→ generate task view
→ retain reverse mapping
```

因此 projection 並不是最後才臨時 flatten。

它建立在完整 source index 上。

---

# 45. 參考寫入流程

寫入原則：

```text
Do not overwrite original snapshot
→ create candidate change
→ validate structure / dependency
→ compute impact
→ apply policy
→ human review if required
→ append new event/version
→ update semantic fingerprint
```

所以：

$$
\boxed{
Edit
\neq
SilentMutation.
}
$$

---

# 46. MLF 與 ONNX：不是競爭同一問題

ONNX 是：

$$
\boxed{
PortableSerializedComputationGraph.
}
$$

它主要保存：

- model；
- graph；
- operators；
- tensors；
- metadata。

ONNX graph 還要求 main computation graph 依 data dependencies 拓撲排序，並使用 SSA-style value definitions。

MLF 則保留：

- human regions；
- spreadsheet identity；
- source formula；
- AST；
- dependency；
- routes；
- provenance history；
- conversion loss；
- presentation fingerprint。

因此：

$$
\boxed{
ONNX
\neq
MLF.
}
$$

較合理關係是：

$$
MLF
\xrightarrow{\Phi_{model}}
ONNX
$$

或某些 MLF tensor / graph projection 成為模型工具鏈輸入。

---

# 47. MLF 與 MLIR

MLIR 提供：

$$
Operation
+
Value
+
Block
+
Region
+
Dialect
$$

的 extensible compiler IR，

並可同時有：

- human-readable text；
- in-memory form；
- compact serialized form；

且這些形式描述相同 semantic content。

這和 MLF 有很強的哲學近鄰：

$$
\boxed{
\text{一個 semantic object 可以有多種 physical representation}.
}
$$

但 MLIR 的目標是：

$$
\boxed{
CompilerTransformation
+
Lowering.
}
$$

MLF 的目標則更偏：

$$
\boxed{
Cross-Interface Structural Preservation
+
Audit
+
Projection.
}
$$

---

# 48. MLF 與 Apache Arrow

Arrow 專注：

$$
\boxed{
LanguageAgnosticColumnarMemory
}
$$

與：

- metadata serialization；
- zero-copy-friendly transport；
- SIMD / locality；
- analytical access。

所以 Arrow 的核心優化目標是：

$$
\boxed{
PhysicalDataLayoutEfficiency.
}
$$

MLF 不是。

MLF 可以把某些 dense / tabular projection：

$$
\Phi_{arrow}(\mathcal F)
$$

交給 Arrow，

但 MLF 仍保存 Arrow 不負責的：

- formula AST；
- route；
- provenance event；
- conversion loss；
- human projection semantics。

---

# 49. MLF 與 W3C PROV

PROV-O 提供一般：

$$
Entity
+
Activity
+
Agent
$$

provenance vocabulary。

MLF 沒必要重造一般 provenance ontology。

更合理方向：

$$
\boxed{
MLFProvenance
\leftrightarrow
PROV.
}
$$

也就是讓 MLF 的 cell/formula/projection events 可以映射到標準 provenance 世界。

---

# 50. MLF 的真正研究主張

所以 MLF 的研究增量不是：

> 「我們做了一個 ZIP 裝 JSON。」

真正命題是：

$$
\boxed{
\textbf{
如果一個計算／知識物件會在多種表示之間流動，
那麼 identity、dependency、semantics、provenance 與 loss
應該成為跨 projection 保存的一等公民。
}
}
$$

---

# 51. Stable Core 與 Research Module

MLF 1.0 stable core 包含：

- containers；
- Manifest；
- cells / IDs；
- regions / roles；
- formula source + AST；
- dependency graph；
- route / projection；
- provenance；
- conversion loss；
- fingerprints；
- checksums；
- migration；
- validation。

---

# 52. Research / Governed Modules

repository 另外保留：

- dataset generation；
- anti-leakage splitting；
- runtime projections；
- model comparison；
- inference ledger；
- review / promotion；
- calibration；
- OOD routing；
- natural workbook intake。

但：

$$
\boxed{
RepositoryFeature
\neq
NormativeMLF1.0.
}
$$

---

# 53. 為什麼保留負面結果？

如果 repository 只留下：

> 最後成功版。

就會失去：

- leakage history；
- failed model comparison；
- unsupported semantics；
- calibration boundary。

因此 negative result 本身應進：

$$
\boxed{
ResearchProvenance.
}
$$

這和 MMR-Bench 的自我否證路線一致。

---

# 54. 1.0 發布驗證

MLF 1.0 / Compiler 1.0.0 的 release candidate 記錄：

- 54 automated tests PASS；
- Python syntax compilation PASS；
- Manifest JSON Schema PASS；
- README 24 relative links 存在；
- fresh MLF 1.0 validate；
- MLF 0.1 readable；
- migration preserves semantic / presentation fingerprints；
- repository scan 無本機 absolute paths / cache / hard-coded secret；
- wheel 在無 NumPy / PyTorch 的 fresh environment 可安裝核心 CLI；
- release ZIP 解壓後再次 54 tests PASS。

所以：

$$
\boxed{
StableSpec
+
ReferenceImplementation
+
ReleaseVerification.
}
$$

三層都已有對應。

---

# 55. 這些驗證不能證明什麼？

不能證明：

- MLF 是最佳格式；
- MLF 比 ONNX / MLIR / Arrow 更快；
- AI 用 MLF 一定更準；
- enterprise XLSX 全支援；
- learned dependency inference 已 production-ready；
- conversion 能普遍 lossless。

所以：

$$
\boxed{
Conformance
\neq
Superiority.
}
$$

---

# 56. MLF 的 Falsification Plan

MLF 的價值仍應與：

- flat JSON；
- CSV；
- spreadsheet；
- graph-only IR；
- AST-only IR；

比較。

---

# 57. F1 — No Structural Benefit

如果：

$$
FlatJSON+Metadata
$$

可以更簡單、低成本地保存全部 MLF useful semantics，

那 MLF 應被降格為：

$$
\boxed{
NamingConvention.
}
$$

---

# 58. F2 — Projection Overhead

如果任何 AI task 都必須：

$$
MLF
\rightarrow
HugeFlattening
$$

且：

$$
TokenCost_{MLF}
>
TokenCost_{baseline},
$$

沒有 accuracy / audit benefit，

則 AI projection value 失敗。

---

# 59. F3 — Conversion Loss Too Large

若 real workbook import 長期產生大量：

$$
unsupported,
$$

$$
ambiguous,
$$

使：

$$
UsefulStructureRatio
$$

過低，

則 XLSX bridge 只適合小子集。

---

# 60. F4 — Fingerprints Unstable

若 semantic-preserving repackaging：

$$
R_1\sim_{sem}R_2
$$

卻頻繁得到：

$$
F_{semantic}(R_1)
\neq
F_{semantic}(R_2),
$$

則 canonicalization 設計失敗。

---

# 61. F5 — Projection Not Reversible Enough

若模型 projection 無法回答：

> 「這個 token / node / tensor slice 原來來自哪個 cell / region / formula？」

則：

$$
\boxed{
TraceableProjection
}
$$

主張失敗。

---

# 62. F6 — Governance Becomes Metadata Theater

如果 prediction / decision / promotion 雖然被分欄，

但實際 runtime 還是：

$$
ModelOutput
\rightarrow
CanonicalGraph
$$

直接寫入，

那治理欄位只是裝飾。

因此：

$$
\boxed{
Governance
}
$$

必須在 runtime policy 中真正生效。

---

# 63. 從 Spreadsheet 到 Canonical Structure 的最終轉折

現在可以重新畫整條歷史：

$$
\boxed{
Excel\ Cell
}
$$

$$
\downarrow
$$

$$
\boxed{
Cell+Formula
}
$$

$$
\downarrow
$$

$$
\boxed{
Cell+Dependency+Role
}
$$

$$
\downarrow
$$

$$
\boxed{
MMR\ Route
}
$$

$$
\downarrow
$$

$$
\boxed{
MMLC\ Transaction+Audit
}
$$

$$
\downarrow
$$

$$
\boxed{
MMR\text{-}Bench\ Evidence
}
$$

$$
\downarrow
$$

$$
\boxed{
MLF\ CanonicalStructure.
}
$$

---

# 64. Excel 最終成為 Projection

這是整個系列最重要的一次概念反轉。

最早：

> Excel 能不能成為 AI？

到 MLF：

$$
\boxed{
Excel
=
\Phi_{sheet}(\mathcal F).
}
$$

同時：

$$
Sequence
=
\Phi_{seq}(\mathcal F),
$$

$$
Tensor
=
\Phi_{tensor}(\mathcal F),
$$

$$
Graph
=
\Phi_{graph}(\mathcal F),
$$

$$
HumanView
=
\Phi_{human}(\mathcal F).
$$

沒有任何一個 projection 天然擁有全域特權。

---

# 65. 但 Projection 也不是「假的」

若：

$$
V=\Phi(\mathcal F),
$$

不能說：

> V 只是幻影。

因為不同 projection 可以是：

- 真實可執行；
- 真實可讀；
- 真實可訓練；
- 真實可視化。

真正差異是：

$$
\boxed{
\text{它們只保存任務需要的部分結構。}
}
$$

---

# 66. Conversion Loss 讓投影不再假裝完整

所以 MLF 最值得保留的一個概念其實可能是：

$$
\boxed{
L.
}
$$

也就是：

$$
\boxed{
\text{每個 projection 都應該有勇氣說自己丟了什麼。}
}
$$

這讓：

$$
Projection
$$

從一個形上學詞彙，

變成工程可檢查物件。

---

# 67. 本文結論

MLF 1.0 的核心不是：

> 再發明一個通用格式。

而是建立一個明確界線：

$$
\boxed{
\textbf{
完整結構負責保存；
投影負責使用；
損失負責誠實；
來源負責追蹤；
指紋負責判定何種同一性。
}
}
$$

因此：

$$
\boxed{
\text{Storage}
\neq
\text{Projection}
\neq
\text{Execution}
\neq
\text{ModelInput}
\neq
\text{HumanView}.
}
$$

MLF 不要求這些層最後長得一樣。

它要求：

> **它們不同時，不要失去彼此的來源關係。**

這就是：

$$
\boxed{
\text{Traceable Multi-Projection Structure}.
}
$$

從這裡開始，下一個問題自然變成：

> 如果同一 canonical structure 可以被人類、AI、試算表、Runtime 同時投影，那麼如何保證它們真的仍然指向同一份執行狀態，而不是各自長成不同真實？

這就是下一篇的：

$$
\boxed{
\text{Executable Identity}.
}
$$

---

# 68. 下一篇

## EML-MNIAC-2026-07

**《單一狀態、多重投影：人類、AI、試算表與 Runtime 的執行同一性》**

下一篇將正式整合：

- MLF；
- MMLC Runtime；
- PHOSPHOR-SHEET；
- canonical state；
- human / AI / spreadsheet projection；
- authority；
- write-back；
- conflict；
- executable identity；
- state divergence；
- round-trip control。

---

# 參考資料

## 內部規格與工程

1. EveMissLab, **AI Matrix Ledger Format (MLF) 1.0 — Traditional Chinese Specification**.
2. EveMissLab, **AI Matrix Ledger Format (MLF) 1.0 — English Specification**.
3. EveMissLab, **MLF 1.0 / MLF Compiler 1.0.0 Release Notes**.
4. EveMissLab, **MLF 1.0 GitHub 發布與命名說明**.
5. EveMissLab, **MLF Compiler 1.0.0**.
6. Repository: `kakon77777-commits/matrix-ledger-format`.
7. EML-MNIAC-2026-05, 《試算表智能的可證偽實驗》.

## 外部技術近鄰

8. ONNX, **Open Neural Network Exchange Intermediate Representation Specification**.  
   https://onnx.ai/onnx/repo-docs/IR.html

9. LLVM Project, **MLIR Language Reference**.  
   https://mlir.llvm.org/docs/LangRef/

10. Apache Arrow, **Arrow Columnar Format**.  
    https://arrow.apache.org/docs/format/Columnar.html

11. W3C, **PROV-O: The PROV Ontology**.  
    https://www.w3.org/TR/prov-o/

這些外部系統已分別處理 computation graph、compiler IR、多形態 semantic IR、columnar data transport 與 provenance interchange。MLF 的合理定位不是宣稱取代它們，而是將 matrix/spreadsheet-originated knowledge 的 identity、formula AST、dependency、route、human/model projection 與 conversion loss 放進同一可追蹤交換契約，並在需要時投影到這些既有工具鏈。

---

**系列狀態：** 第 06 篇完成。  
**下一篇：** EML-MNIAC-2026-07 —《單一狀態、多重投影：人類、AI、試算表與 Runtime 的執行同一性》
