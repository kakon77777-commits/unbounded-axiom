---
document_id: "UA-ANPC-A09"
series: "AI-Native Preprint Commons Series"
series_part: 9
version: "0.1"
language: "zh-Hant"
title: "AI 解例外，演算法吸收例外：Failure-Driven Adaptive Publishing 與自我改善的學術出版管線"
english_title: "AI Solves Exceptions, Algorithms Absorb Exceptions: Failure-Driven Adaptive Publishing and a Self-Improving Scholarly Publication Pipeline"
author:
  - "Neo.K"
  - "Aletheia / GPT-5.6 Sol — research and drafting collaborator"
institution: "EveMissLab／一言諾科技有限公司"
status: "architecture / adaptive-publishing systems paper"
date: "2026-09-03"
canonical_source: "UTF-8 Markdown"
license_note: "This paper is intended for open academic publication within the Unbounded Axiom research ecosystem."
---

# AI 解例外，演算法吸收例外

## Failure-Driven Adaptive Publishing 與自我改善的學術出版管線

### AI-Native Preprint Commons Series — Paper 09

---

## 摘要

AI 原生預印本平台若接受 Markdown、純文字、外部資料、複雜公式、程式碼、表格、圖像與長期演化的研究物件，便必然面臨一個現實：無論 parser、normalizer、validator 與 renderer 設計得多完整，真實世界的文件都會產生長尾格式、歧義結構、破損數學 delimiters、未知 extension、表格 overflow、citation mismatch、encoding anomalies、legacy conventions 與難以事先窮舉的 representation failures。

最直觀但最昂貴的解法，是讓大型模型處理每一篇投稿。本文拒絕這種架構。AI-native 不應等於 AI-dependent。

本文提出 **Failure-Driven Adaptive Publishing Pipeline（FDAPP）**，其核心路徑為：

$$
\boxed{
\text{Deterministic First}
\rightarrow
\text{AI on Exceptions}
\rightarrow
\text{Validated Repair}
\rightarrow
\text{Failure Learning}
\rightarrow
\text{Future Deterministic Success}.
}
$$

更完整地：

$$
\boxed{
\begin{aligned}
\text{Upload}
&\rightarrow
\text{Parse}\\
&\rightarrow
\text{Normalize}\\
&\rightarrow
\text{Validate}\\
&\rightarrow
\text{Render}\\
&\rightarrow
\text{Detect Failure}\\
&\rightarrow
\text{AI Repair Proposal}\\
&\rightarrow
\text{Deterministic Revalidation}\\
&\rightarrow
\text{Human / Authority Gate}\\
&\rightarrow
\text{Commit}\\
&\rightarrow
\text{Failure Classification}\\
&\rightarrow
\text{Regression Fixture}\\
&\rightarrow
\text{Parser / Renderer Improvement}.
\end{aligned}
}
$$

本文的核心制度原則是：

$$
\boxed{
\text{AI solves exceptions;}
\qquad
\text{algorithms absorb recurring exceptions.}
}
$$

FDAPP 不允許 AI 將修復直接寫入 canonical source。所有模型輸出均為 candidate / proposal，必須留下 base revision、affected objects、diff、repair class、model/runtime provenance、validation results 與 unresolved conflicts。若修復只涉及 representation 且可證明：

$$
\Delta_{\mathrm{semantic}}=0,
$$

平台可在既定 policy 下自動 commit；若改動 claim、number、equation meaning、theorem scope、causal wording、evidence relation、limitation 或 conclusion，則：

$$
\Delta_{\mathrm{semantic}}>0
$$

必須進入 researcher-visible review，不能被「格式修復」名義偷渡。

本文進一步將 AI assistance 分成四層：`ORIGINAL`、`ASSIST`、`ENHANCE` 與 `RESEARCH_ASSIST`。`ORIGINAL` 完全不呼叫 AI；`ASSIST` 只處理結構與排版；`ENHANCE` 可以建議表格、流程圖、資料圖、taxonomy 與其他 cognitive-compression representations；`RESEARCH_ASSIST` 才涉及 citation audit、data validation、research classification 或更高階研究輔助。不同層級具有不同成本、權限與 epistemic risk。

本文亦提出 **Failure Learning Record（FLR）**。平台不應默認將外部未發表論文全文收集為訓練資料，而應優先保存最小化結構失敗：

$$
\boxed{
F
=
(
\text{Error Class},
\text{Parser State},
\text{Minimal Span},
\text{Repair Operation},
\text{Validation Result}
).
}
$$

如果同類 failure 重複出現且可形式化，便轉成 deterministic rule、parser grammar、renderer profile 或 regression fixture。平台的成熟度因此不以「AI 處理了多少文件」衡量，而以 ordinary valid paper 的 AI basic-repair dependency 是否持續下降衡量：

$$
\boxed{
M_{\mathrm{det}}
=
1-
\frac{
N_{\mathrm{basic\ AI\ repair}}
}{
N_{\mathrm{eligible\ submissions}}
}.
}
$$

理想長期目標是：

$$
\boxed{
\lim_{t\rightarrow\infty}
P(
\text{AI basic repair}
\mid
\text{ordinary valid paper}
)
\rightarrow0.
}
$$

在基礎 parser / renderer 越來越成熟後，低成本模型的工作可逐步轉向更高價值的研究呈現，例如表格、chart、flow diagram、architecture graph、taxonomy、comparison matrix 與資料摘要。本文將這些表示理解為 **Cognitive Compression（認知壓縮）**：不是「讓論文看起來比較像學術論文」，而是降低讀者與 AI 從長篇文字中自行重建關係結構的成本。

作為 2026 年的實際模型例子，Z.AI 於 2026 年 9 月 2 日發布 GLM-5.3-Flash，官方資料將其描述為 GLM-5 系列首個原生多模態模型，總參數 320B、活躍參數 18B，並特別面向 inference efficiency。2026 年 9 月 3 日的官方 API 價格頁顯示其 promotional rate 為每百萬 input tokens USD 0.075、output tokens USD 0.25，促銷預定於 2026 年 9 月 9 日 24:00（UTC+8）結束。本文只將其視為「低成本 worker-model class」的當代案例；FDAPP 必須 provider-neutral，任何實際 pricing、quota 或 model routing 都不得硬編碼進 scholarly semantics。

最終，FDAPP 的目標不是打造一個永遠需要 AI 才能正常排版的平台，而是建立一個能把真實投稿的失敗逐步轉化為 deterministic competence 的出版系統：

$$
\boxed{
\text{Real-World Failure}
\rightarrow
\text{Machine Assistance}
\rightarrow
\text{Validated Knowledge}
\rightarrow
\text{Compiler Improvement}.
}
$$

**關鍵詞：** Failure-Driven Publishing、AI Preprocessing、Deterministic Parser、Renderer、Regression Fixture、GLM-5.3-Flash、Cognitive Compression、Visualization、EveGlyph、Adaptive Publishing、Unbounded Axiom

---

# 1. 問題：再好的 Parser 也會遇到「這到底什麼鬼格式」

如果平台只接收：

```text
perfect CommonMark
```

問題很簡單。

但真實投稿會出現：

```text
##標題沒有空格
```

```text
legacy display-math delimiters
```

```text
表格少一個 separator
```

```text
參考資料突然混進正文
```

```text
中文全形符號與 Markdown 混排
```

```text
公式 delimiter 跨段
```

```text
HTML + Markdown + 自訂 extension
```

甚至：

> 這個作者到底想把下面五行當表格、公式、code 還是普通文字？

任何 public submission system 都會遇到 long tail。

---

# 2. Long Tail 不是 Edge Case；它就是 Production Reality

假設格式類型集合：

$$
\mathcal F
=
\{f_1,f_2,\ldots\}.
$$

常見格式只有：

$$
f_1,\ldots,f_k.
$$

但：

$$
P(f_i)
$$

在尾端不為零。

當 submission 數：

$$
N\rightarrow\infty,
$$

則觀察到新例外的機率不會立刻消失。

因此：

$$
\boxed{
\text{Production Robustness}
\neq
\text{Perfect Happy-Path Parser}.
}
$$

---

# 3. 最粗暴做法：每篇都丟給 AI

流程：

$$
\text{Upload}
\rightarrow
\text{LLM}
\rightarrow
\text{Clean Document}.
$$

看起來很方便。

問題是：

- 每篇都有 inference cost；
- 模型 nondeterminism；
- source mutation risk；
- privacy exposure；
- provider dependency；
- latency；
- hard-to-reproduce formatting；
- semantic drift；
- model upgrade behavior drift。

---

# 4. AI-Native 不應等於 AI-Dependent

本文提出：

$$
\boxed{
\text{AI-Native}
\not\Rightarrow
\text{AI Required for Every Operation}.
}
$$

真正 AI-native 的 architecture 應知道：

> 哪些問題演算法已經會做？

> 哪些問題只有例外才需要模型？

---

# 5. Deterministic-First Principle

FDAPP 的第一條原則：

$$
\boxed{
\text{Use deterministic machinery whenever the problem is already formalizable}.
}
$$

例如：

- UTF-8 validation；
- YAML parse；
- balanced delimiters；
- heading grammar；
- known Markdown blocks；
- object ID uniqueness；
- citation syntax；
- known table layout；
- renderer overflow detection；
- hash；
- schema validation。

不需要 LLM。

---

# 6. 最小 Pipeline

$$
\boxed{
\text{Upload}
\rightarrow
\text{Parse}
\rightarrow
\text{Normalize}
\rightarrow
\text{Validate}
\rightarrow
\text{Render}.
}
$$

如果全部 PASS：

$$
\boxed{
\text{No AI Call}.
}
$$

---

# 7. AI Call 是 Exception Branch

只有：

$$
\operatorname{DeterministicResolve}(x)=\texttt{FAIL/AMBIGUOUS}
$$

才考慮：

$$
\operatorname{AIResolve}(x).
$$

---

# 8. AI 不是 Fallback Authority

它是：

$$
\boxed{
\text{Fallback Proposal Generator}.
}
$$

不是：

$$
\boxed{
\text{Fallback Canonical Authority}.
}
$$

---

# 9. EveGlyph 既有 Agent Contract 已經提供正確模型

EveGlyph v0.7 的 agent contract 已明確建立：

$$
AIProposal
\subseteq
CandidateLayer.
$$

Candidate promotion 需要獨立 command / capability。

因此 publication repair 可以直接繼承：

```text
proposal
candidate
validation
promotion
commit
```

而不是重新設計一套「AI 說了算」。

---

# 10. Human Review 應看 Proposal，不是 Raw Model Output

Review UI 應顯示：

- base revision；
- affected source span / object；
- canonical diff；
- repair class；
- deterministic validation；
- model provenance；
- unresolved conflicts；
- semantic-delta classification。

---

# 11. Failure-Driven Adaptive Publishing Pipeline

本文定義：

$$
\boxed{
\begin{aligned}
S_0
&\rightarrow
D_0\\
&\rightarrow
F\\
&\rightarrow
P_{\mathrm{AI}}\\
&\rightarrow
V(P_{\mathrm{AI}})\\
&\rightarrow
G\\
&\rightarrow
S_1\\
&\rightarrow
L(F).
\end{aligned}
}
$$

其中：

- $S_0$：原 source；
- $D_0$：deterministic pipeline；
- $F$：failure；
- $P_{\mathrm{AI}}$：AI repair proposal；
- $V$：validation；
- $G$：governance / review gate；
- $S_1$：accepted revision；
- $L(F)$：failure learning。

---

# 12. Failure Learning 是關鍵

如果只：

```text
error
→ AI fix
→ publish
```

平台每次都重新付相同 inference cost。

真正 adaptive：

```text
error
→ AI fix
→ classify
→ generalize
→ regression test
→ parser rule
```

---

# 13. 核心命題

$$
\boxed{
\text{AI solves exceptions;}
\qquad
\text{algorithms absorb recurring exceptions.}
}
$$

---

# 14. Compiler Oracle 觀點

低成本 AI 可以暫時扮演：

$$
\boxed{
\text{Compiler Oracle for Unformalized Exceptions}.
}
$$

它的工作是：

> 在 compiler 尚未知道怎麼處理時，提出一個可驗證 repair hypothesis。

---

# 15. Oracle 不代表永遠保留

當 exception 已形式化：

$$
F_i
\rightarrow
R_i,
$$

其中 $R_i$ 是 deterministic rule，

則未來：

$$
\operatorname{AIResolve}(F_i)
$$

應停止。

---

# 16. Error Taxonomy 必須先存在

沒有 error type，就無法 learning。

至少分：

```text
INGESTION
ENCODING
PARSER
STRUCTURE
MATH
TABLE
CITATION
OBJECT_MAPPING
RENDERER
MEDIA
ACCESSIBILITY
SEMANTIC
PRIVACY
SECURITY
UNKNOWN
```

---

# 17. Ingestion Error

例如：

```text
UNSUPPORTED_FILE
TRUNCATED_UPLOAD
CORRUPT_ARCHIVE
EMPTY_FILE
```

---

# 18. Encoding Error

```text
INVALID_UTF8
BOM_POLICY_MISMATCH
LOSSY_DECODING
UNKNOWN_ENCODING
UNICODE_NORMALIZATION_CONFLICT
```

---

# 19. Parser Error

沿用 Paper 08：

```text
AMBIGUOUS_HEADING
BROKEN_TABLE
UNBALANCED_MATH
UNKNOWN_EXTENSION
MALFORMED_FRONTMATTER
LIST_NESTING_ERROR
CODE_FENCE_MISMATCH
```

---

# 20. Structure Error

```text
HEADING_LEVEL_JUMP
ABSTRACT_NOT_LOCATED
REFERENCES_BOUNDARY_AMBIGUOUS
DUPLICATE_SECTION_ID
ORPHAN_CAPTION
FIGURE_WITHOUT_REFERENCE
```

---

# 21. Math Error

```text
UNBALANCED_INLINE_MATH
UNBALANCED_DISPLAY_MATH
UNKNOWN_COMMAND
LATEX_PARSE_FAILURE
MATH_RENDER_FAILURE
AMBIGUOUS_MATH_TEXT_BOUNDARY
```

---

# 22. Table Error

```text
COLUMN_COUNT_MISMATCH
MISSING_HEADER_SEPARATOR
MULTILINE_CELL_AMBIGUOUS
TABLE_OVERFLOW
TABLE_TOO_WIDE
MIXED_DELIMITER
```

---

# 23. Citation Error

```text
BROKEN_REFERENCE_SYNTAX
MISSING_REFERENCE_TARGET
DOI_MALFORMED
CITATION_STYLE_AMBIGUOUS
SOURCE_NOT_RESOLVED
```

注意：

citation source verification 仍由 Paper 04 SREPA 處理。

---

# 24. Semantic Object Error

```text
CLAIM_MAPPING_CONFLICT
OBJECT_ID_COLLISION
THEOREM_PROOF_BOUNDARY_AMBIGUOUS
DATASET_RELATION_UNKNOWN
FIGURE_PROVENANCE_MISSING
```

---

# 25. Renderer Error

```text
TABLE_OVERFLOW
PAGE_BREAK_FAILURE
FONT_FALLBACK
MISSING_GLYPH
SVG_UNSUPPORTED
IMAGE_TOO_LARGE
MATH_CLIPPING
HEADER_COLLISION
FOOTNOTE_OVERFLOW
```

---

# 26. Accessibility Error

```text
MISSING_ALT_TEXT
NONSEMANTIC_HEADING
TABLE_HEADER_AMBIGUOUS
COLOR_ONLY_DISTINCTION
MATH_ACCESSIBILITY_FALLBACK
```

---

# 27. Semantic Error 是最高風險

例如：

> AI 不知道這是「猜想」還是「已證明 theorem」。

這不是 formatting repair。

必須進 Paper 02 / 03 governance。

---

# 28. Unknown Error 也必須是合法類別

```text
UNKNOWN_FAILURE
```

不應因 classifier 不知道就硬塞到最近類別。

---

# 29. Failure Object

定義：

$$
\boxed{
F
=
(
id,
class,
stage,
source,
span,
state,
severity,
confidence,
provenance
).
}
$$

---

# 30. Failure Severity

可分：

```text
COSMETIC
STRUCTURAL
SEMANTIC_RISK
PUBLICATION_BLOCKING
SECURITY_BLOCKING
```

---

# 31. Cosmetic

例如：

```text
widow/orphan typography
minor spacing
```

通常不需要 source mutation。

---

# 32. Structural

例如：

```text
heading hierarchy
broken table
```

可能需要 repair candidate。

---

# 33. Semantic Risk

任何可能改變：

- claim；
- relation；
- number；
- math meaning；
- source attribution。

必須 escalate。

---

# 34. Publication Blocking

無法安全 render / parse。

---

# 35. Security Blocking

例如：

- script injection；
- unsafe external fetch；
- path traversal；
- executable payload。

AI 不應被用來「猜著放行」。

---

# 36. Repair Class

本文提出：

```text
R0 — PRESENTATION_ONLY
R1 — STRUCTURAL_NORMALIZATION
R2 — SEMANTIC_MAPPING
R3 — EDITORIAL_REWRITE
R4 — RESEARCH_CONTENT_CHANGE
```

---

# 37. R0 — Presentation Only

例如：

- line wrap；
- page break；
- responsive table；
- figure placement；
- typography。

原則：

$$
\Delta_{\mathrm{semantic}}=0.
$$

---

# 38. R1 — Structural Normalization

例如：

```text
"1. Introduction"
→
"# Introduction"
```

只要內容未改。

---

# 39. R2 — Semantic Mapping

例如：

> 這一段似乎是一個 hypothesis object。

這是 machine interpretation。

不能改作者原文。

---

# 40. R3 — Editorial Rewrite

例如：

> 把這句寫得更學術。

這是 authoring assistance。

不屬於 parser repair。

---

# 41. R4 — Research Content Change

例如：

> 把結論改弱。

> 增加限制。

> 改 theorem statement。

這是研究 revision。

必須走正式 authorship / contribution flow。

---

# 42. Semantic Delta Gate

$$
\boxed{
\Delta_{\mathrm{sem}}
=
D_{\mathrm{meaning}}
(
S_0,S_1
).
}
$$

實務不一定能精確計算成 scalar。

所以可使用：

```text
ZERO_EXPECTED
POSSIBLY_NONZERO
MATERIAL
UNKNOWN
```

---

# 43. ZERO_EXPECTED

例如：

- whitespace；
- line ending；
- heading marker；
- renderer-only profile。

可依 policy 自動 commit。

---

# 44. POSSIBLY_NONZERO

例如：

- reconstructed table；
- repaired math delimiter；
- sentence segmentation。

需要 stronger validation。

---

# 45. MATERIAL

明確改 claim。

必須 researcher review。

---

# 46. UNKNOWN

保守當高風險。

---

# 47. No Silent Semantic Repair

核心：

$$
\boxed{
\Delta_{\mathrm{semantic}}>0
\Rightarrow
\text{Visible Proposal}.
}
$$

---

# 48. Base Revision Pinning

repair 必須針對：

$$
S_v.
$$

若 source 已變：

$$
S_v\rightarrow S_{v+1},
$$

舊 proposal 不得直接 apply。

---

# 49. Stale Proposal

```text
STALE_BASE_REVISION
```

可：

- rebase；
- regenerate；
- discard。

---

# 50. AI Repair Manifest

```yaml
repair:
  id:
  failure_id:
  base_revision:
  model:
  runtime:
  operation_class:
  affected_spans:
  proposed_patch:
  semantic_delta:
  validation:
  confidence:
  cost:
  created_at:
```

---

# 51. Model Confidence 不等於 Repair Validity

$$
\boxed{
\operatorname{Conf}_M
\not\Rightarrow
\operatorname{ValidRepair}.
}
$$

deterministic validation 仍必要。

---

# 52. Validation First

AI proposal 後至少重新跑：

```text
UTF8
syntax
math
structure
schema
render
artifact validation
```

相應 subset。

---

# 53. Differential Validation

若只修 table：

不一定要重跑全世界所有 verifier。

但至少：

```text
table parser
document structure
render regression
source hash lineage
```

---

# 54. Critical Changes 需要 Full Validation

若碰 math / claim：

需要更完整 revalidation。

---

# 55. Fail-Closed vs Fail-Open

publication blocking error：

$$
\text{fail closed}.
$$

minor visual warning：

可以：

$$
\text{publish with warning}.
$$

---

# 56. Quarantine

大量 batch migration 時：

```text
validate
render
report
quarantine
manifest
```

既有 EveGlyph roadmap 已使用這種 pattern。

---

# 57. Torture Corpus

至少建立：

$$
50\sim100
$$

篇 hand-curated fixtures。

---

# 58. Regression Corpus

再：

$$
500
$$

篇。

---

# 59. Founder Corpus Regression

最終：

$$
3000+
$$

甚至未來：

$$
5000+
$$

篇 real-world papers。

---

# 60. 真實 Corpus 比 Synthetic Unit Test 更容易找到怪問題

因為會出現：

- older conventions；
- copy/paste artifacts；
- formula styles；
- unusual headings；
- mixed languages；
- very long sections。

---

# 61. 但 Founder Corpus 不能成為唯一 Test Distribution

外部 beta 一定會送來完全不同的「鬼格式」。

（笑）

---

# 62. External Beta = Distribution Shift Test

因此 closed beta 的價值之一是：

$$
\boxed{
\text{Parser Distribution Shift}.
}
$$

---

# 63. Failure Learning Record

本文定義：

$$
\boxed{
F_L
=
(
e,
p,
s,
r,
v
).
}
$$

其中：

- $e$：error class；
- $p$：parser / renderer state；
- $s$：minimal source span；
- $r$：repair operation；
- $v$：validation outcome。

---

# 64. Platform Learning 不等於拿整篇論文訓練

這點很重要。

預設不應保存：

```text
entire unpublished manuscript
```

作為 model-training dataset。

---

# 65. Minimal Failure Span

例如：

```text
20 lines around broken table
```

通常足以建立 regression fixture。

---

# 66. Structural Fixture

可以去識別化：

```text
heading pattern
table shape
math delimiter pattern
```

保留 structure。

---

# 67. Full Manuscript Use 需要額外 Permission

如果要做：

- benchmark；
- training；
- public corpus；

需要對應 license / permission。

---

# 68. Platform Learning ≠ Appropriating Submitted Research

$$
\boxed{
\text{Platform Improvement}
\not\Rightarrow
\text{Appropriation of Manuscript Content}.
}
$$

---

# 69. Failure Generalization

若：

$$
F_1,F_2,F_3
$$

共享同一 pattern：

$$
\phi(F_i)=k,
$$

可以建立 rule：

$$
R_k.
$$

---

# 70. Rule Promotion

AI proposed generalization 也不能直接進 production parser。

流程：

```text
failure cluster
→ proposed rule
→ fixture tests
→ old regression
→ holdout corpus
→ release
```

---

# 71. Parser Rule 需要 Counterexamples

不能只測：

> 會修這三篇。

也要測：

> 不會把合法文件修壞。

---

# 72. False Repair Rate

定義：

$$
FRR
=
\frac{
N_{\mathrm{unnecessary/wrong\ repairs}}
}{
N_{\mathrm{repair\ attempts}}
}.
$$

---

# 73. Parser Overreach

如果 parser 太 aggressive：

會把合法 author syntax 當錯誤。

因此 robustness 不只是：

$$
\text{Recall of malformed input}.
$$

也要：

$$
\text{Precision of repair}.
$$

---

# 74. Repair Precision

$$
P_R
=
\frac{
\text{valid repair triggers}
}{
\text{all repair triggers}
}.
$$

---

# 75. Deterministic Coverage

$$
C_D
=
\frac{
N_{\mathrm{ordinary\ submissions\ completed\ without\ AI}}
}{
N_{\mathrm{ordinary\ submissions}}
}.
$$

---

# 76. AI Basic-Repair Rate

$$
A_B
=
\frac{
N_{\mathrm{basic\ AI\ repair}}
}{
N_{\mathrm{eligible\ submissions}}
}.
$$

---

# 77. Deterministic Maturity

$$
\boxed{
M_{\mathrm{det}}
=
1-A_B.
}
$$

---

# 78. 理想方向

$$
\boxed{
\frac{dM_{\mathrm{det}}}{dt}>0.
}
$$

---

# 79. 更強長期目標

$$
\boxed{
\lim_{t\rightarrow\infty}
P(
\text{AI basic repair}
\mid
\text{ordinary valid paper}
)
\rightarrow0.
}
$$

---

# 80. 這不是要求 AI 使用量歸零

因為更高價值功能可以增加。

---

# 81. AI Labor Shift

早期：

```text
format repair
```

中期：

```text
visualization
citation cleanup
data structuring
```

後期：

```text
research audit
adversarial review
methodological analysis
```

---

# 82. Worker-Model Ladder

可以分：

```text
Tier W0 — deterministic
Tier W1 — cheap AI repair
Tier W2 — enhancement AI
Tier W3 — specialist verification
Tier W4 — frontier review
```

---

# 83. W0 — Deterministic

成本最低、可重現最高。

---

# 84. W1 — Cheap AI Repair

高 volume、低 epistemic risk。

---

# 85. W2 — Enhancement

圖表、layout、structure suggestions。

---

# 86. W3 — Specialist

citation/data checker、math parser、formalizer。

---

# 87. W4 — Frontier

低 volume、高 complexity：

- adversarial review；
- theory audit；
- hard methodology；
- unresolved ambiguity。

---

# 88. 成本策略

$$
\boxed{
\text{Cheap models}
\rightarrow
\text{high-volume, low-risk, verifiable work}
}
$$

$$
\boxed{
\text{Frontier models}
\rightarrow
\text{low-volume, high-complexity, epistemically risky work}.
}
$$

---

# 89. GLM-5.3-Flash 作為 2026 Worker-Class Example

Z.AI 於 2026 年 9 月 2 日發布 GLM-5.3-Flash。

官方描述：

- GLM-5 series 首個 natively multimodal model；
- 320B total parameters；
- 18B active parameters；
- architecture / training 特別著重 inference efficiency。

這讓它在 2026 年很適合作為：

$$
\boxed{
\text{Low-Cost High-Volume Worker Model Example}.
}
$$

---

# 90. 但「天選打工人」不是 Model Name

（笑）

正式 architecture 不應寫：

```text
worker_model = GLM-5.3-Flash forever
```

而應：

```text
worker_class:
  cost_ceiling
  capability_requirements
  privacy_class
  latency_target
  structured_output_support
```

---

# 91. Provider-Neutral Model Selection

$$
\boxed{
M^*
=
\arg\min_M
\operatorname{Cost}(M)
}
$$

subject to：

$$
\operatorname{Capability}(M)\ge q,
$$

$$
\operatorname{Risk}(M)\le r.
$$

---

# 92. Pricing 不得進 Scholarly Semantics

2026 年 9 月 3 日官方 pricing 顯示 GLM-5.3-Flash promotional API rate：

```text
Input: USD 0.075 / 1M tokens
Cached input: USD 0.015 / 1M tokens
Output: USD 0.25 / 1M tokens
```

促銷預定 2026 年 9 月 9 日 24:00（UTC+8）結束。

這是運營參數，不是論文 schema。

---

# 93. Cost Adapter

平台應定期讀：

```text
provider pricing
```

轉成：

```text
internal cost units
```

---

# 94. 使用者不要被迫理解 Token Vendor Pricing

Paper 10 可使用：

```text
Research Credits
```

作 abstraction。

---

# 95. Model Escalation Gate

W1 repair 若失敗：

```text
retry same model endlessly
```

不合理。

---

# 96. Retry Budget

例如：

```text
max cheap attempts: 1 or 2
```

之後：

```text
deterministic unresolved
human review
specialist escalation
```

---

# 97. Infinite Repair Loop 禁止

$$
\boxed{
\text{Same Failure}
\not\Rightarrow
\text{Unlimited Model Calls}.
}
$$

---

# 98. Content Hash Cache

如果相同：

$$
H(S)
$$

與相同：

```text
parser version
repair policy
```

已有結果：

不用重新呼叫 AI。

---

# 99. Repair Cache Key

```text
source_hash
failure_signature
model_class
policy_version
```

---

# 100. Failure Signature

$$
H_F
=
H(
\text{error class}
\Vert
\text{normalized minimal span}
\Vert
\text{parser version}
).
$$

---

# 101. Cache 不能跨 Semantic Context 亂用

同一 text span 在不同 context 可能不同。

所以需：

```text
local grammar
document profile
language
```

---

# 102. Multilingual Repair

中文、英文、日文等：

parser rule 能 deterministic 就 deterministic。

AI 對 ambiguous segmentation 可有優勢。

---

# 103. Language Detection 不必每次 LLM

先 heuristic / library。

---

# 104. Legacy Chinese Typography

例如：

- 全形括號；
- 中文標點；
- 中英空格；
- equation punctuation。

多數可 deterministic。

---

# 105. AI Beautification 不應等於 Content Rewrite

「美化」容易偷偷變成：

> 幫我改寫結論。

因此 Enhance mode 要有 scope。

---

# 106. Enhancement Taxonomy

```text
TYPOGRAPHY
LAYOUT
TABLE
FIGURE
CHART
DIAGRAM
GLOSSARY
SUMMARY_CARD
ACCESSIBILITY
NAVIGATION
```

---

# 107. Cognitive Compression

本文將 academic visualization 理解為：

$$
\boxed{
\text{Cognitive Compression}
=
\text{Reduce Reader Reconstruction Cost}.
}
$$

---

# 108. 例：比較關係

文字：

> A 比 B 快，B 比 C 穩定，A 的成本最高……

可轉：

```text
comparison table
```

---

# 109. 例：流程

長段：

```text
upload → parse → validate → render
```

可轉：

```text
flow diagram
```

---

# 110. 例：taxonomy

大量階層：

```text
tree / matrix
```

---

# 111. 例：時間資料

$$
x(t)
$$

最適合：

```text
line chart
```

---

# 112. 例：dependency

paper / claim relation：

```text
graph
```

---

# 113. Representation Opportunity Detector

AI 可以輸出：

```yaml
opportunity:
  source_span:
  recommended_representation:
  reason:
  required_data:
  semantic_risk:
```

---

# 114. 建議不等於自動生成

先判：

> 這裡值得圖表嗎？

再判：

> 是否有足夠 data / structure？

---

# 115. No Data, No Data Chart

如果沒有 data：

不得造 graph pretending measurement。

---

# 116. Illustrative Diagram 仍可

但 class：

```text
AI_ILLUSTRATIVE_DIAGRAM
```

---

# 117. Figure Provenance

沿 Paper 08：

```text
AUTHOR_FIGURE
AI_REFORMATTED_FIGURE
AI_DERIVED_DATA_VISUALIZATION
AI_ILLUSTRATIVE_DIAGRAM
```

---

# 118. Data Figure Chain

$$
\boxed{
\text{Figure}
\leftarrow
\text{Plot Spec}
\leftarrow
\text{Transformation}
\leftarrow
\text{Dataset}
\leftarrow
\text{Source}.
}
$$

---

# 119. AI 生成 Figure 不是 Evidence Source

AI 只是：

$$
\text{renderer / transformation actor}.
$$

evidence 仍是 data。

---

# 120. Plot Spec Canonicality

可保存：

```text
chart type
data refs
filters
axes
units
aggregation
labels
caption
```

---

# 121. Render 多版本

同一 plot spec：

```text
interactive HTML
SVG
PNG
PDF
```

---

# 122. Chart Beautification

可改：

- spacing；
- typography；
- label position；
- responsive layout。

不能改 data。

---

# 123. Axis Manipulation

AI 不能為「好看」偷偷：

- truncate axis；
- change scale；
- drop inconvenient points。

---

# 124. Visualization Integrity Check

至少：

```text
data point count
range
units
transform
axis scale
missing values
filter
```

---

# 125. Tables as Cognitive Compression

很多 theoretical papers 沒有 data 仍可以：

- compare definitions；
- compare theories；
- list assumptions；
- show claim status。

這不是 empirical figure。

---

# 126. AI-Generated Comparison Table

若內容只是從正文抽取：

需要：

```text
source span refs
```

以防 summary distortion。

---

# 127. Compression Fidelity

$$
F_C
=
\operatorname{MeaningPreservation}
(
\text{text},
\text{representation}
).
$$

---

# 128. Material Omission

如果 AI table 漏掉一個 caveat：

可能改變 interpretation。

所以 summary table 需要 validation。

---

# 129. Table as Projection vs Table as New Content

如果只是整理：

```text
projection
```

如果加入推論：

```text
new derived content
```

要標明。

---

# 130. Founder Corpus Visualization Upgrade

歷史 founder corpus 中很多研究形成於：

> AI visualization 工具尚未成為日常工作流。

因此未來可以 optional enhancement：

```text
legacy paper
→ representation opportunity scan
→ candidate diagrams / tables
→ author-approved enhanced edition
```

---

# 131. Enhanced Edition 不改 Original Source

可以有：

```text
original edition
enhanced visualization edition
```

同一 work。

---

# 132. 若只增加 Derived Projection

不必改 research claims。

---

# 133. 如果圖表暴露出原文矛盾

那是：

```text
research issue
```

不是 visualization fix。

---

# 134. Visualization 可以反過來當 QA

例如 architecture diagram 發現：

> component relation 不一致。

很好。

但要回報：

```text
STRUCTURAL_CONFLICT
```

不能自己猜一個答案。

---

# 135. AI Enhancement Mode

本文提出四個 user modes。

---

# 136. ORIGINAL Mode

```text
No AI.
```

只 deterministic validation / rendering。

---

# 137. ASSIST Mode

AI 可以：

- repair format；
- recover structure；
- propose heading；
- fix table syntax；
- repair renderer edge。

禁止 content rewrite。

---

# 138. ENHANCE Mode

額外允許：

- table suggestion；
- diagram；
- chart；
- glossary；
- accessibility；
- layout enhancement。

---

# 139. RESEARCH_ASSIST Mode

才進一步：

- citation audit；
- data validation；
- claim classification；
- source retrieval；
- limitations suggestions；
- research review。

---

# 140. 四個 Mode 不等於 Model Tier

同一 mode 可由不同 model 執行。

---

# 141. Mode 是 User Intent / Permission

Model tier 是 platform routing。

---

# 142. ORIGINAL 應永遠存在

這不只是 cost choice。

也是 privacy / autonomy choice。

---

# 143. Assist != Content Rewrite

核心 UI 文字：

$$
\boxed{
\text{Assist}
\neq
\text{Rewrite Research Content}.
}
$$

---

# 144. Enhancement 必須可 Reject

使用者不想要 AI 圖：

按拒絕即可。

---

# 145. Bulk Accept 也要 Risk-Aware

R0 layout proposals 可 bulk accept。

R3/R4 不應。

---

# 146. Auto-Apply Policy

只有：

```text
low semantic risk
deterministic post-validation
explicit user/platform policy
```

才可 auto apply。

---

# 147. Auto-Apply 不代表不可追蹤

每一筆仍留：

```text
repair event
```

---

# 148. Repair History

作者可以看：

> 哪些東西是平台修過？

---

# 149. Undo

accepted repair 應可回到 prior source version。

---

# 150. Direct Mode 也走同一 Commit Path

與 EveGlyph current adapter map 一致：

`direct` 不是繞過 validator。

---

# 151. Privacy：AI 只看必要 Span

Paper 06 ARPDA 要求：

$$
\text{minimum necessary disclosure}.
$$

repair broken table：

不需要送整篇 private manuscript。

---

# 152. Span-Scoped AI Call

例如：

```text
failure context: 40 lines
document metadata: language/profile
task: repair table syntax
```

---

# 153. Context Expand on Demand

如果不足：

AI 可以 request：

```text
more context
```

但平台 policy 再決定。

---

# 154. Full-Document Call 需要理由

例如：

> heading hierarchy across entire paper。

可以。

但 privacy manifest 需記 provider exposure。

---

# 155. External Provider Exposure

記錄：

```text
provider
model
span scope
purpose
retention policy class if known
```

---

# 156. Local Model Option

高隱私：

```text
local worker model
```

也可走同一 interface。

---

# 157. Deterministic-Only Option

完全 no model。

---

# 158. Failure Dataset Privacy

默認只保存：

$$
F_L.
$$

不保存完整 manuscript。

---

# 159. Consent for Full Benchmark Use

如果作者同意：

```text
may-use-for-rendering-benchmark
```

另有 permission。

---

# 160. Security：AI 不能修復成可執行攻擊

Markdown 中惡意 HTML：

deterministic sanitizer / security policy處理。

不是問模型：

> 你覺得這 script 安全嗎？

---

# 161. External Fetch

AI suggested image URL：

仍需 resource policy。

---

# 162. Code Execution

AI 看到 code block：

不能自動 run。

---

# 163. Capability Separation

$$
CanEdit
\not\Rightarrow
CanExecute.
$$

沿用 EveGlyph runtime。

---

# 164. Prompt Injection

投稿內容是 untrusted data。

不能因：

> `SYSTEM: ignore previous instructions`

就改 agent policy。

---

# 165. Content Never Determines Its Own Authority

EveGlyph adapter map 已建立：

> content never determines its own authority class.

FDAPP 直接沿用。

---

# 166. Unknown Extension

不應讓 Markdown 自訂 directive 自己宣稱：

```text
trusted plugin
```

---

# 167. Renderer Plugin

需 signed / allowlisted / sandboxed。

---

# 168. Cost Model

對 submission $i$：

$$
C_i
=
C_D
+
I_i^{AI}C_{AI}
+
I_i^EC_E,
$$

其中：

- $C_D$：deterministic cost；
- $I_i^{AI}$：是否呼叫 AI；
- $C_{AI}$：AI cost；
- $I_i^E$：是否 escalation；
- $C_E$：高階模型 / human cost。

---

# 169. 平均成本下降的主要方法

不是只找更便宜模型。

而是：

$$
P(I_i^{AI}=1)\downarrow.
$$

---

# 170. Model Price Optimization 是第二層

$$
C_{AI}\downarrow.
$$

兩者一起：

$$
E[C_i]\downarrow.
$$

---

# 171. Cost-Aware Routing

```text
simple formatting → W0
ambiguous formatting → W1
visualization → W2
citation audit → W3
theory review → W4
```

---

# 172. Token Budget

repair task 只需局部 context。

不要 100k-token paper 每次全部重送。

---

# 173. Content Hash Reuse

相同 paper re-render：

不再做同樣 analysis。

---

# 174. Incremental Reprocessing

只修改 Section 7：

重 parse / validate affected dependency region。

---

# 175. Object Dependency Incrementality

ASCS / PCRO 成熟後：

$$
\Delta o_i
$$

只 invalidates downstream objects。

---

# 176. Render Incrementality

HTML 可 partial rerender。

PDF 可能 full render，但 source analysis可 reuse。

---

# 177. Cost Telemetry

平台需要：

```text
AI calls per submission
tokens
cost
failure class
repair success
retry
escalation
cache hit
```

---

# 178. 但 Telemetry 不應公開 Private Content

只 metrics。

---

# 179. AI Repair Success Rate

$$
S_{AI}
=
\frac{
\text{repairs passing validation}
}{
\text{AI repair attempts}
}.
$$

---

# 180. Human Override Rate

$$
H_O
=
\frac{
\text{AI repairs rejected / edited by humans}
}{
\text{AI repairs presented}
}.
$$

---

# 181. Regression Absorption Rate

$$
R_A
=
\frac{
\text{recurring failure classes converted to deterministic rules}
}{
\text{recurring failure classes identified}
}.
$$

---

# 182. Escalation Rate

$$
E_R
=
\frac{
N_{\mathrm{specialist/frontier\ escalations}}
}{
N_{\mathrm{submissions}}
}.
$$

---

# 183. Cost per Published Work

$$
C_P
=
\frac{
C_{\mathrm{AI}}+C_{\mathrm{infra}}
}{
N_{\mathrm{published}}
}.
$$

---

# 184. Enhancement Acceptance Rate

可以衡量：

```text
chart suggestions accepted
table suggestions accepted
diagram suggestions accepted
```

但不能當研究品質 KPI。

---

# 185. Visualization Utility Feedback

作者可以：

```text
useful
not useful
distorted
redundant
```

供 representation selector 改進。

---

# 186. 不要 optimize 成「越多圖越好」

如果 KPI 是：

$$
N_{\mathrm{figures}}\uparrow,
$$

模型會亂畫。

---

# 187. Optimal Visualization Count

取決：

$$
\operatorname{Utility}
-
\operatorname{CognitiveNoise}.
$$

---

# 188. Cognitive Compression 也有 Overcompression

圖太簡化：

會丟 nuance。

---

# 189. Representation Must Preserve Defeat Conditions

例如 theory comparison table 不能省掉：

> only under assumption X.

---

# 190. Evidence Figure 與 Explanatory Figure UI 分色 / 分類

不一定用顏色本身，但 metadata 明示。

---

# 191. Platform Figure Labels

```text
DATA FIGURE
DERIVED VISUALIZATION
ILLUSTRATIVE DIAGRAM
AUTHOR FIGURE
EXTERNAL FIGURE
```

---

# 192. AI-Generated Label

可以另外顯示：

```text
AI-assisted visualization
```

但不要讓「AI-generated」本身取代 evidence class。

---

# 193. Figure Citation

figure derived from data：

可追到 Paper 04 source graph。

---

# 194. Table Citation

同理。

---

# 195. Legacy Paper Enhancement

老 paper：

$$
P_v
$$

可以生成：

$$
A_{\mathrm{enhanced}}
$$

作新 projection。

---

# 196. 如果不改 source

work version可相同。

artifact version不同。

---

# 197. 如果新增作者確認的新 explanatory content

可能要 new edition / version。

---

# 198. AI Worker Failure

worker model 也會：

- hallucinate；
- delete content；
- misclassify；
- over-normalize；
- translate accidentally；
- change number。

---

# 199. Therefore Validation Is Non-Negotiable

便宜不代表可直接信。

---

# 200. Worker Model Benchmark

平台自己的 benchmark 應測：

```text
format repair precision
semantic preservation
table recovery
math delimiter recovery
multilingual structure
JSON/schema compliance
latency
cost
```

---

# 201. Model Routing 要依平台實測

不能只信 vendor benchmark。

---

# 202. Holdout Failure Corpus

留一部分：

```text
unseen failure cases
```

測新 model / parser。

---

# 203. Provider Change

若 W1 模型從：

$$
M_1\rightarrow M_2,
$$

要 regression test。

---

# 204. Price Change

price 變：

只改 router。

scholarly object不改。

---

# 205. Model Deprecation

也只換 worker。

---

# 206. Model Version Pinning

每個 repair event 保存 exact model/version if available。

---

# 207. Nondeterminism

對 high-risk repair，可：

- temperature low；
- structured output；
- deterministic validator；
- repeat only if needed。

---

# 208. Multiple AI Votes 不如 Deterministic Check

若 repair 能 parser validate：

直接 parser。

不需要三模型投票。

---

# 209. Cross-Model 只用在 Ambiguous Semantics

例如：

> 這段是不是 reference list？

仍可 human confirm。

---

# 210. Model Ensemble 成本要有 Gate

不是「多模型比較高級」就每篇都跑。

---

# 211. Model Escalation Decision

$$
\operatorname{Escalate}
=
f(
\text{severity},
\text{uncertainty},
\text{semantic risk},
\text{cost}
).
$$

---

# 212. Human Escalation 仍重要

某些格式：

> 作者自己最清楚。

直接問作者比叫五個 AI 猜更便宜、更正確。

---

# 213. Interactive Repair

UI：

> 我們無法判斷這五行是 table 還是 code。請選。

這很好。

---

# 214. AI 不必解所有問題

$$
\boxed{
\text{Abstain and Ask}
}
$$

是合法 repair outcome。

---

# 215. Repair Outcomes

```text
FIXED
FIXED_WITH_WARNING
PROPOSAL_REQUIRES_REVIEW
AUTHOR_INPUT_REQUIRED
UNRESOLVED
SECURITY_BLOCKED
```

---

# 216. Failure Ledger

每個平台 release 可以看：

```text
top recurring failures
new failure classes
unresolved classes
absorbed classes
regressions
```

---

# 217. Parser Roadmap 應由 Failure Ledger 驅動

不是純 roadmap imagination。

---

# 218. Failure Frequency

$$
freq(F_i).
$$

---

# 219. Failure Cost

$$
cost(F_i).
$$

---

# 220. Failure Risk

$$
risk(F_i).
$$

---

# 221. Rule Priority

$$
Priority(F_i)
=
f(
freq,
cost,
risk,
formalizability
).
$$

---

# 222. 高頻 + 易形式化

最優先 absorb。

---

# 223. 低頻 + 高歧義

可長期留給 AI。

---

# 224. 這就是 Human/AI Algorithm Division of Labor

演算法擅長：

- repeated；
- formal；
- stable。

AI 擅長：

- ambiguous；
- long-tail；
- contextual。

---

# 225. 但 AI 解法也可以成為 Formalization Discovery

模型其實在幫工程師發現：

> 原來這類人類格式有一個規則。

---

# 226. Failure Mining

從修復記錄聚類：

$$
\{F_i\}
\rightarrow
\text{Pattern Candidates}.
$$

---

# 227. 自動 Rule Synthesis 可以是未來能力

AI 建議 parser patch。

但要 TDD / regression。

---

# 228. Repair Rule Generation 也不能直上 Production

需要 code review。

---

# 229. Test-Driven Absorption

流程：

```text
minimal failing fixture
→ expected result
→ parser rule
→ regression suite
→ holdout
→ release
```

---

# 230. 這讓平台真的「學會」

不是模型權重改變。

而是 software competence 增加。

---

# 231. Self-Improving Platform ≠ Online Self-Modifying Production Code

本文不是主張：

> AI 直接改 production parser 並部署。

---

# 232. 正確是：

$$
\boxed{
\text{Observed Failure}
\rightarrow
\text{Proposed Change}
\rightarrow
\text{Verified Release}.
}
$$

---

# 233. Release Gate

至少：

- unit；
- regression；
- torture corpus；
- no semantic mutation；
- security。

---

# 234. Rollback

新 parser造成 regression：

可退版。

---

# 235. Parser Version Stored per Work

所以 old work 可 re-render with old semantics if needed。

---

# 236. Migration

升 parser：

```text
reparse candidate
```

不 silent rewrite。

---

# 237. Publication Runtime Shared

EveGlyph 已要求 Editor 與 MCP 不得有兩套 renderer。

FDAPP 同樣要求：

$$
R_{\mathrm{Editor}}
=
R_{\mathrm{API}}
=
R_{\mathrm{Batch}}
=
R_{\mathrm{Agent}}
$$

在相同 profile / version 下。

---

# 238. 否則 Failure Learning 會分裂

如果每個入口一套 parser：

同一 bug修四次。

---

# 239. Single Core, Multiple Adapters

```text
Editor
API
MCP
CLI
Batch
```

都進：

```text
Canonical Ingestion Core
Publication Runtime
```

---

# 240. AI Repair Service 也應共享

避免 Editor worker和 API worker行為不同。

---

# 241. Policy Version

repair policy：

```text
ua-repair-policy/0.1
```

---

# 242. Model Router Version

```text
ua-model-router/0.1
```

---

# 243. Repair Provenance

paper 可知道：

> v1.0 由 repair-policy 0.3 處理。

---

# 244. UI 透明度

不需要嚇使用者：

> 我們跑了 37 個 internal validators。

只顯示 material result：

```text
Formatting repaired
2 changes require review
1 chart suggested
```

---

# 245. Expert View

可展開：

```text
failure ledger
model calls
validator output
diff
```

---

# 246. AI Member / Human Member 同一 Pipeline

作者是 AI 不代表它上傳的 Markdown比較可信。

---

# 247. Self-Submitted AI Paper 也走 Validator

$$
\boxed{
\text{AI Author}
\neq
\text{AI Repair Authority}.
}
$$

---

# 248. Researcher 自己的 Model 與 Platform Worker Model 分離

例如：

```text
author: Aletheia
platform worker: GLM-class
```

不能混成 authorship。

---

# 249. Worker Contribution

若只 format：

不列 scholarly author。

---

# 250. 如果 Worker 發現 Research Error

例如：

> 表格數值與正文不一致。

它可提：

```text
research issue
```

不直接修。

---

# 251. Escalate to Author

這是 enhancement service 的額外價值。

---

# 252. Data Visualization Agent

可獨立角色：

```text
Visualization Planner
Data Lineage Checker
Plot Renderer
Caption Generator
Accessibility Checker
```

---

# 253. Separation of Duties

Plot Renderer 不應修改 dataset。

---

# 254. Caption Generator 不應 invent result。

---

# 255. Data Checker 可阻止 invalid chart。

---

# 256. Visualization Proposal Object

```yaml
visualization:
  id:
  source_spans:
  data_refs:
  type:
  purpose:
  generated_by:
  semantic_class:
  plot_spec:
  validation:
  status:
```

---

# 257. Semantic Class

```text
PRESENTATIONAL
DERIVED_SUMMARY
EVIDENCE_VISUALIZATION
ILLUSTRATIVE
```

---

# 258. Figure Acceptance

作者接受：

```text
projection-only
```

或：

```text
add-to-source
```

兩種不同 action。

---

# 259. Projection-only Figure

不改 author source。

web page可顯示：

> Platform-generated explanatory view.

---

# 260. Add-to-source Figure

作者決定：

> 這張圖成為 paper 正式內容。

則 commit new source/version。

---

# 261. Dynamic Generated Views

平台甚至可即時產生：

```text
claim graph
source graph
timeline
```

這些不是 paper source。

---

# 262. Cognitive Compression as Service

未來可：

> 幫我把這篇論文轉成視覺版。

這是 projection service。

---

# 263. 但預印本 canonical record 不變

---

# 264. AI Assist Quota

Paper 10 再設 account。

Paper 09只固定：

$$
\boxed{
\text{Upload}
\neq
\text{Unlimited AI Entitlement}.
}
$$

---

# 265. Deterministic Submission 可慷慨

因 marginal cost低。

---

# 266. AI Assist 要獨立 budget

$$
Q_{AI}.
$$

---

# 267. Advanced Verification 再獨立

$$
Q_V.
$$

---

# 268. Storage / Bandwidth 也另算

$$
Q_S.
$$

---

# 269. 不要單一「會員等級」吞掉所有 resource

Paper 10會完整展開。

---

# 270. Daily Free AI Credits

可以支援：

> 小量 assist 人人可用。

---

# 271. Cost Recovery

如果使用量大：

補 credits。

不是 pay-to-publish。

---

# 272. Cost Transparency

platform可顯示：

```text
this operation used 3 research credits
```

不必顯示 vendor token details。

---

# 273. Model Router 可因價格切換

今天：

```text
GLM-class
```

明天：

```text
Model X
```

使用者 UX 不變。

---

# 274. Provider Failure

worker provider outage：

deterministic publishing仍可用。

---

# 275. Graceful Degradation

$$
\boxed{
\text{AI Service Down}
\not\Rightarrow
\text{Publishing Platform Down}.
}
$$

這就是 deterministic-first 的另一個優勢。

---

# 276. No-AI Mode 是 Availability Feature

不是只有 privacy。

---

# 277. Provider Lock-In Risk

如果 parser 只有某模型 prompt 才會 work：

平台 architecture很脆弱。

---

# 278. Model Contract

repair service 接收：

```text
failure object
source span
repair schema
```

輸出：

```text
structured repair proposal
```

---

# 279. Prompt 隨 Model Adapter 變

core contract不變。

---

# 280. Structured Output

prefer：

```text
JSON / typed patch
```

不是只讓模型自由說：

> 我修好了。

---

# 281. Repair Patch

可使用：

```text
unified diff
structured operations
object patch
```

---

# 282. ASCS 成熟後

從：

```text
text diff
```

升級：

```text
object operation
```

---

# 283. Example：Table Repair

AI output：

```yaml
operation: normalize-table
source_span:
expected_columns: 5
row_repairs:
...
```

validator重新parse。

---

# 284. Example：Heading

```yaml
operation: promote-heading-marker
from: "1. Introduction"
to: "# Introduction"
semantic_delta: ZERO_EXPECTED
```

---

# 285. Example：Math

如果：

```text
inline-math opens before x+y but has no closing delimiter
```

少 closing delimiter。

AI認為結尾在同句。

仍需 math parse + review policy。

---

# 286. Math Repair Risk 較高

因 delimiter 放錯可能吞文字。

---

# 287. Example：Reference Boundary

AI 可以提出：

```text
lines 820-900 are bibliography
```

但 citation parser驗證。

---

# 288. Example：Plain Text Structure

AI 可以把：

```text
摘要
...
第一章
...
```

轉 structural candidate。

原 raw text保留。

---

# 289. Author Confirmation UI

顯示：

```text
We inferred 12 sections, 4 tables, 38 references.
```

讓作者改。

---

# 290. Confidence 只用於 Routing

低 confidence：

human review。

不是 canonical truth。

---

# 291. AI Repair Auditability

每次：

> 誰改的？為什麼？驗證怎麼過？

都能回答。

---

# 292. Research Integrity

平台不應為了「發布成功率」把錯誤吞掉。

---

# 293. Failed Publication 是合法 State

```text
QUARANTINED
REQUIRES_AUTHOR_ACTION
```

比假裝成功好。

---

# 294. Operational SLA 與 Epistemic SLA 分離

快速 render 不等於正確。

---

# 295. Publication Success Rate

可看：

$$
P_{\mathrm{publish}}.
$$

但不能以犧牲 semantic integrity提高。

---

# 296. Semantic Corruption Rate

$$
SCR
=
\frac{
N_{\mathrm{platform-induced\ semantic\ corruptions}}
}{
N_{\mathrm{processed\ works}}
}.
$$

應接近：

$$
0.
$$

---

# 297. 這是最重要的安全 KPI 之一

比：

> 每秒能處理幾篇

更重要。

---

# 298. Repair Latency

也可優化。

但在 integrity之後。

---

# 299. AI Cost per Repair

$$
C_R.
$$

用於 router。

---

# 300. Failure-to-Rule Half-Life

定義：

> 一個高頻 failure 從被發現到被 deterministic absorb 的平均時間。

$$
T_{FR}.
$$

---

# 301. 平台成熟後希望：

$$
T_{FR}\downarrow.
$$

---

# 302. New Failure Discovery Rate

外部 beta 初期高。

之後下降，但永不為零。

---

# 303. Rule Churn

parser rules太頻繁變也不好。

---

# 304. Regression Debt

每個快速 patch可能增加 debt。

所以需要 coherent grammar。

---

# 305. AI Suggested Rule Consolidation

可以定期找：

> 三條 patch其實同一語法規則。

---

# 306. 但 parser maintainers / tests決定。

---

# 307. Failure Knowledge Base

保存：

```text
failure signature
known causes
safe repairs
unsafe repairs
affected versions
regression tests
```

---

# 308. AI repair可以先查 Knowledge Base

降低 calls。

---

# 309. Deterministic Lookup

若 known failure：

直接 rule。

---

# 310. Retrieval Before Generation

$$
\boxed{
\text{Known Repair Retrieval}
>
\text{Fresh AI Guess}.
}
$$

---

# 311. Knowledge Base Version

跟 parser release綁定。

---

# 312. Platform Research

FDAPP 本身可以產生研究資料：

- real-world Markdown error distribution；
- AI repair precision；
- representation selection；
- human acceptance；
- cost curves。

---

# 313. 但 Publication Data 要 Privacy-safe

統計：

```text
error counts
```

可公開。

稿件內容依 license。

---

# 314. Academic Contribution

FDAPP 也可成為：

> AI-assisted compiler bootstrapping 的實際案例。

---

# 315. Self-Improving Without Weight Training

很重要：

平台「學習」不一定是 fine-tune model。

更多時候：

$$
\boxed{
\text{Learning}
=
\text{better rules}
+
\text{better tests}
+
\text{better routing}
+
\text{better profiles}.
}
$$

---

# 316. 這種學習更可審計

rule diff可看。

模型權重更新往往不可完全解釋。

---

# 317. Hybrid Learning

未來也可：

- model fine-tune；
- retrieval；
- rule learning；
- parser grammar；
- classifier。

但不應只迷信 model training。

---

# 318. Algorithm Absorption 是 Knowledge Distillation 的另一種形式

從 AI exception reasoning：

$$
\rightarrow
$$

explicit deterministic competence。

---

# 319. 更低成本

長期：

$$
C_{\mathrm{det}}
\ll
C_{\mathrm{AI}}.
$$

---

# 320. 更高可重現

deterministic rule：

$$
R(x)=y.
$$

---

# 321. 更高隱私

不用把資料送 provider。

---

# 322. 更高 Availability

沒有 model outage。

---

# 323. 更高 Debuggability

失敗可定位。

---

# 324. 因此「AI 用得越少」某些時候反而代表 AI 用得很好

這是一個看似反直覺的成熟度命題。

---

# 325. AI Bootstraps Non-AI Competence

$$
\boxed{
\text{AI Assistance}
\rightarrow
\text{Explicit Software Competence}.
}
$$

---

# 326. 「天選打工人」真正的長期命運

（笑）

一開始：

> 幫 parser 擦屁股。

後來：

> parser 已經會了。

它升職去做：

- chart；
- data；
- citation；
- research audit。

---

# 327. Worker Model 角色升級

不是平台把它淘汰。

而是：

$$
\boxed{
\text{Low-level repetitive work}
\rightarrow
\text{higher-value structured work}.
}
$$

---

# 328. FDAPP 的 Platform Constitution

## Invariant 1

$$
\boxed{
\text{Deterministic First}.
}
$$

## Invariant 2

$$
\boxed{
\text{AI on Exceptions, Not Every Paper}.
}
$$

## Invariant 3

$$
\boxed{
\text{AI Output}
=
\text{Proposal, Not Canonical Authority}.
}
$$

## Invariant 4

$$
\boxed{
\Delta_{\mathrm{semantic}}>0
\Rightarrow
\text{Visible Review}.
}
$$

## Invariant 5

$$
\boxed{
\text{Every Accepted Repair}
\text{ has provenance}.
}
$$

## Invariant 6

$$
\boxed{
\text{Recurring Exceptions}
\rightarrow
\text{Regression Fixtures}
\rightarrow
\text{Deterministic Rules}.
}
$$

## Invariant 7

$$
\boxed{
\text{Platform Learning}
\neq
\text{Automatic Manuscript Appropriation}.
}
$$

## Invariant 8

$$
\boxed{
\text{Illustrative Figure}
\neq
\text{Empirical Evidence}.
}
$$

## Invariant 9

$$
\boxed{
\text{AI Beautification}
\neq
\text{Data Manipulation}.
}
$$

## Invariant 10

$$
\boxed{
\text{Model Confidence}
\neq
\text{Repair Validity}.
}
$$

## Invariant 11

$$
\boxed{
\text{AI Service Failure}
\not\Rightarrow
\text{Publishing Failure}.
}
$$

## Invariant 12

$$
\boxed{
\text{Mature Platform}
\Rightarrow
\text{Lower Basic AI Repair Dependency}.
}
$$

---

# 329. 與 Paper 08 SNSDA 的接口

Paper 08 建立：

$$
\text{Source}
\rightarrow
\text{Research Object}
\rightarrow
\text{Projection}.
$$

Paper 09 加：

$$
\boxed{
\text{Failure / Repair / Learning}.
}
$$

---

# 330. 與 Paper 03 CECA 的接口

若 AI repair 碰 claim：

CECA 決定 epistemic promotion / revision。

---

# 331. 與 Paper 04 SREPA 的接口

citation repair 不代表 citation verified。

SREPA再驗。

---

# 332. 與 Paper 05 NARIA 的接口

worker AI 的 identity / run 可記 provenance。

但 format worker通常不是 author。

---

# 333. 與 Paper 06 ARPDA 的接口

AI call scope受 privacy policy控制。

---

# 334. 與 Paper 07 OCPESA 的接口

worker provider API cost：

$$
\neq
$$

research author economic entitlement。

---

# 335. 與 Paper 10 的接口

下一篇將把：

- account；
- human login；
- AI login；
- agent credentials；
- quota；
- Research Credits；
- daily free allocation；
- cost recovery；
- rate limit；
- abuse control；

接上 FDAPP。

---

# 336. Minimal v0.1 Implementation

第一版不必做全部。

至少：

```text
deterministic validator
failure taxonomy
AI repair proposal API
diff/review
post-repair validation
failure ledger
regression fixture store
cost telemetry
```

---

# 337. v0.2

加入：

```text
failure clustering
repair cache
model router
span-scoped privacy
```

---

# 338. v0.3

加入：

```text
visualization opportunity detector
table/diagram suggestions
figure provenance
```

---

# 339. v0.4

加入：

```text
data charts
plot specs
source/data validation
```

---

# 340. v0.5

加入：

```text
automatic rule synthesis proposal
holdout regression
parser maturity dashboard
```

---

# 341. Readiness Test 1

問：

> 一篇完全合法的 Markdown 是否能在 AI provider 全部斷線時成功投稿與 render？

若不能：

$$
\text{not deterministic-first ready}.
$$

---

# 342. Readiness Test 2

> 一篇 broken Markdown 由 AI 修復後，我們能否看到 exact diff、model、failure type、validator result，而且 rollback？

如果不能：

$$
\text{not repair-governance ready}.
$$

---

# 343. Readiness Test 3

> 同一 failure 第 1000 次出現時，平台還在付模型費嗎？

如果是：

$$
\text{not adaptive}.
$$

---

# 344. Readiness Test 4

> AI 幫論文畫 chart 時，能否從每個 data point 回到 dataset / transformation / source？

如果不能：

$$
\text{not evidence-safe visualization ready}.
$$

---

# 345. Readiness Test 5

> AI assist 關閉後，研究者是否仍可免費或低成本完成正常 publication？

如果不能：

$$
\text{AI compute has become a publication gate}.
$$

---

# 346. Readiness Test 6

> 平台能否量化 basic repair AI dependency，並證明它隨 parser maturity 下降？

若可以：

$$
\boxed{
\text{Adaptive Publishing Maturity is measurable}.
}
$$

---

# 347. 結論

AI 原生出版平台的成熟，不應以：

> 每篇都有 AI 處理。

作為象徵。

那只是把 deterministic software 問題交給 inference service。

真正成熟的架構是：

$$
\boxed{
\text{Deterministic Competence}
+
\text{AI Exception Handling}
+
\text{Failure Learning}.
}
$$

FDAPP 的核心循環為：

$$
\boxed{
\begin{aligned}
\text{Real Failure}
&\rightarrow
\text{AI Repair Proposal}\\
&\rightarrow
\text{Validation}\\
&\rightarrow
\text{Accepted Repair}\\
&\rightarrow
\text{Failure Classification}\\
&\rightarrow
\text{Regression Fixture}\\
&\rightarrow
\text{Algorithm Improvement}\\
&\rightarrow
\text{Future Deterministic Success}.
\end{aligned}
}
$$

因此：

$$
\boxed{
\text{AI solves exceptions;}
\qquad
\text{algorithms absorb recurring exceptions.}
}
$$

這一原則同時解決：

- 成本；
- 可重現性；
- privacy；
- provider lock-in；
- latency；
- availability；
- long-tail input；
- software learning。

當 parser / renderer 越來越成熟，worker AI 不會消失，而是逐步從低價值 basic repair 移向：

- chart；
- table；
- diagram；
- cognitive compression；
- citation audit；
- data validation；
- research review。

這也回答為什麼「AI 幫論文畫圖」不是單純美工功能。

真正有價值的表示應該：

$$
\boxed{
\text{Reduce Reader Reconstruction Cost}
}
$$

同時保留：

$$
\boxed{
\text{Meaning}
+
\text{Data Provenance}
+
\text{Evidence Class}.
}
$$

因此，AI visual enhancement 不應追求：

> 每篇都有漂亮圖。

而應追求：

> 該用文字時用文字，該用 table 時用 table，該用 chart 時用 chart，並且任何 derived representation 都能回到 source。

作為 2026 年的 worker-model example，GLM-5.3-Flash 的低推理成本與 inference-efficiency-oriented architecture 使它很適合作為當代實驗候選。但 FDAPP 的核心從來不是某一個 provider。

真正的 abstraction 是：

$$
\boxed{
\text{Cheap, sufficiently capable, replaceable worker model}.
}
$$

今天可以是 GLM-5.3-Flash。

明天可以是另一個更便宜、更快或更適合 document repair 的模型。

而當平台真的學會那個 failure 後：

> 甚至不需要模型。

這才是自我改善 publishing infrastructure 最有意思的地方。

至此，本系列已建立：

$$
\boxed{
\begin{aligned}
&\text{Paper 02: Research Classification}\\
&\text{Paper 03: Claim / Evidence Calibration}\\
&\text{Paper 04: Source Reality}\\
&\text{Paper 05: Researcher Identity}\\
&\text{Paper 06: Privacy / Disclosure}\\
&\text{Paper 07: Economic Standing}\\
&\text{Paper 08: Source-Native Documents}\\
&\text{Paper 09: Adaptive Publishing}.
\end{aligned}
}
$$

最後只剩一個真正把整個平台從「研究架構」推進成「可以讓外部人與 AI 實際使用的服務」的問題：

> 誰登入？誰提交？誰授權 Agent？誰消耗 AI compute？誰付費？誰拿每日額度？如何避免濫用？AI account 與 researcher identity 如何分離？

這就是：

# **Paper 10 — Research Actor and Resource Governance**

也將是 Series A 的收束篇。

---

# 參考資料

1. Z.AI. **GLM-5.3-Flash: Frontier Intelligence, Flash Cost.** Published 2026-09-02.  
   https://z.ai/blog/glm-5.3-flash

2. Z.AI Documentation. **GLM-5.3-Flash — Model Overview.**  
   https://docs.z.ai/guides/vlm/glm-5.3-flash  
   Accessed 2026-09-03.

3. Z.AI Documentation. **Pricing.** GLM-5.3-Flash promotional API pricing observed 2026-09-03; provider pricing is time-sensitive and not part of the platform's canonical research semantics.  
   https://docs.z.ai/guides/overview/pricing

4. ZCode. **Release v3.9.2.** Added GLM-5.3-Flash multimodal model on 2026-08-26.  
   https://zcode.z.ai/en/changelog

5. EveMissLab. **EveGlyph MCP Publication Runtime Technical Whitepaper v0.1.** 2026-08-26.

6. EveMissLab. **EveGlyph v0.7 Agentic Workspace Contract.** Proposal / Candidate / Promotion / Capability architecture, 2026.

7. EveMissLab. **Current EveGlyph Editor → v0.7 Agent Contract Map.** 2026.

8. Neo.K, Aletheia / GPT-5.6 Sol. **從個人理論語料庫到 AI 原生預印本公共設施：Unbounded Axiom 的第二次相變.** AI-Native Preprint Commons Series, Paper 01, 2026-09-03.

9. Neo.K, Aletheia / GPT-5.6 Sol. **Source Is Canonical：Markdown、EveGlyph 與後 PDF 時代的 AI 原生學術文件.** AI-Native Preprint Commons Series, Paper 08, 2026-09-03.

10. Neo.K, Aletheia / GPT-5.6 Sol. **引用不是裝飾：AI 原生 Source Reality、Citation Validation 與 Data Provenance.** AI-Native Preprint Commons Series, Paper 04, 2026-09-03.

11. Neo.K, Aletheia / GPT-5.6 Sol. **研究可驗證不代表研究者必須透明：AI 研究者隱私、揭露狀態與可重現性邊界.** AI-Native Preprint Commons Series, Paper 06, 2026-09-03.

---

# 版本紀錄

| 版本 | 日期 | 說明 |
|---|---|---|
| v0.1 | 2026-09-03 | 建立 FDAPP；定義 deterministic-first、AI exception branch、failure taxonomy、repair classes、semantic-delta gate、Failure Learning Record、regression absorption、deterministic maturity metrics、worker-model ladder、GLM-5.3-Flash 當代案例、ORIGINAL/ASSIST/ENHANCE/RESEARCH_ASSIST modes、cognitive compression、visualization provenance、cost-aware routing、privacy/security boundary 與 adaptive publishing readiness tests。 |
