---
document_id: "UA-ANPC-A08"
series: "AI-Native Preprint Commons Series"
series_part: 8
version: "0.1"
language: "zh-Hant"
title: "Source Is Canonical：Markdown、EveGlyph 與後 PDF 時代的 AI 原生學術文件"
english_title: "Source Is Canonical: Markdown, EveGlyph, and AI-Native Scholarly Documents Beyond the PDF-Centric Era"
author:
  - "Neo.K"
  - "Aletheia / GPT-5.6 Sol — research and drafting collaborator"
institution: "EveMissLab／一言諾科技有限公司"
status: "architecture / scholarly-document infrastructure paper"
date: "2026-09-03"
canonical_source: "UTF-8 Markdown"
license_note: "This paper is intended for open academic publication within the Unbounded Axiom research ecosystem."
---

# Source Is Canonical

## Markdown、EveGlyph 與後 PDF 時代的 AI 原生學術文件

### AI-Native Preprint Commons Series — Paper 08

---

## 摘要

傳統電子學術出版長期以 PDF 作為主要閱讀與保存介面，部分領域則要求作者透過 LaTeX、Word 或其他文書系統產生 PDF。這種工作流在人類視覺閱讀與紙本出版時代具有高度實用性，但在 AI 原生研究環境中產生新的結構性摩擦：AI 先生成具有語義結構的文字、公式、引用與資料，再被壓平為 PDF；後續 AI 若要搜尋、驗證、引用、重組或進行 claim-level reasoning，又必須重新解析版面、恢復段落、公式與 citation relations。研究物件因此反覆經歷結構化、降維、再重建。

本文提出 **Source-Native Scholarly Document Architecture（SNSDA）**，作為 Unbounded Axiom AI-native preprint commons 的文件基礎層。其核心原則為：

$$
\boxed{
\text{Source is canonical;}
\quad
\text{rendering is projection}.
}
$$

但本文進一步修正「canonical source」的範圍，將學術文件分為三個互相連結、不可互相偷換的層：

$$
\boxed{
\text{Author Canonical Source}
\rightarrow
\text{Platform Canonical Research Object}
\rightarrow
\text{Rendered Projections}.
}
$$

**Author Canonical Source（ACS）** 是作者實際提交、確認與版本化的 UTF-8 Markdown 或純文字來源；它保存原始措辭、公式、段落、引用與作者意圖，不得被 renderer 或 AI preprocessing 靜默改寫。**Platform Canonical Research Object（PCRO）** 則是平台經 schema validation、author confirmation 與 provenance-preserving compilation 後形成的 addressable research-object graph，可包含 claim、definition、equation、citation、dataset、figure、proof、code、research metadata、evidence relations 與 version lineage。未來 EveGlyph ASCS / EGIR 類架構可以承擔此層。PDF、HTML、mobile view、print view、JATS XML、MathML、SVG、PNG、interactive chart、API JSON 與 graph view 都屬於 **Rendered / Interchange Projections**。

本文主張 Unbounded Axiom 的投稿首選格式應是 UTF-8 Markdown，並接受 UTF-8 純文字。投稿者不必先學完整 LaTeX document workflow，也不必自行生成 PDF。數學內容仍可使用熟悉的 LaTeX-style math syntax，例如 ` $...$ ` 與 `$$...$$`；這是 mathematical serialization，而不是要求作者使用 LaTeX document authoring system。純文字輸入則可由 deterministic parser 與可選 AI preprocessing 產生 normalized candidate，但原始 `raw_submission.txt` 必須保存，且任何語義性修改必須可見、可接受或可拒絕。

本文亦提出 scholarly rendering 的可重現性要求。對 source $S$ 、publication profile $P$ 、renderer version $R_v$ 與 options $O$，出版 artifact 應表示為：

$$
A
=
R(
S,
P,
R_v,
O
),
$$

並至少保存 source hash、artifact hash、renderer version、profile version、warnings 與 artifact metadata。Renderer 不得為了排版方便偷偷執行：

$$
S\rightarrow S'.
$$

若需要修復 source，必須進入獨立的 patch / review / commit 流程。

外部學術標準不需被排斥。JATS 1.4 仍是成熟的 journal-article XML interchange standard；MathML Core 提供 browser-oriented mathematical markup；HTML、SVG 與 PDF 各有不可替代的展示與交換價值。SNSDA 的立場不是「所有人只能用 Markdown」，而是：

$$
\boxed{
\text{Canonical scholarly meaning should not depend on one visual artifact format}.
}
$$

因此 PDF 不會消失。它仍然適合下載、列印、存檔、引用頁碼與傳統出版交換。但在 AI-native preprint platform 中，它應由 canonical source / research object **生成**，而不是反過來成為機器唯一能取得的研究真源。

**關鍵詞：** Markdown、UTF-8、EveGlyph、ASCS、EGIR、PDF、JATS、MathML、Canonical Source、Scholarly Document、AI-native Publishing、Unbounded Axiom

---

# 1. 問題：我們為什麼還在把結構化研究壓成 PDF，再叫 AI 解析回來？

考慮今日常見流程：

$$
\text{Research}
\rightarrow
\text{Structured Draft}
\rightarrow
\text{LaTeX / Word}
\rightarrow
\text{PDF}.
$$

另一個 AI 想讀時：

$$
\text{PDF}
\rightarrow
\text{Layout Parsing}
\rightarrow
\text{Text Recovery}
\rightarrow
\text{Equation Recovery}
\rightarrow
\text{Citation Recovery}
\rightarrow
\text{Semantic Reconstruction}.
$$

也就是：

$$
\boxed{
\text{Structure}
\rightarrow
\text{Flatten}
\rightarrow
\text{Recover Structure}.
}
$$

這在 AI-native infrastructure 中是一種不必要的往返。

---

# 2. PDF 很成功，但成功於另一個問題

PDF 很擅長：

- 保留視覺版面；
- 跨裝置呈現；
- 列印；
- 頁碼；
- 圖文固定配置；
- 傳統出版；
- 長期靜態 artifact；
- 文件交換。

所以本文不是反 PDF。

真正問題是：

> PDF 是否應該是研究物件唯一的 canonical representation？

本文答案是：

$$
\boxed{
\text{No}.
}
$$

---

# 3. Visual Fidelity 與 Semantic Fidelity 是兩種 Fidelity

PDF 優先保留：

$$
F_{\mathrm{visual}}.
$$

AI-native research object 還需要：

$$
F_{\mathrm{semantic}}.
$$

例如 PDF 可以把：

> Theorem 3

顯示得非常漂亮。

但若沒有結構資訊，AI 未必知道：

```text
object_type: theorem
object_id: theorem-3
depends_on: lemma-7
validation_state: proof-checked
```

因此：

$$
\boxed{
F_{\mathrm{visual}}
\neq
F_{\mathrm{semantic}}.
}
$$

---

# 4. Source-Native Scholarly Document Architecture

本文提出：

# **SNSDA — Source-Native Scholarly Document Architecture**

其三層為：

$$
\boxed{
S_A
\rightarrow
O_C
\rightarrow
\{A_1,A_2,\ldots,A_n\}.
}
$$

其中：

- $S_A$：Author Canonical Source；
- $O_C$：Platform Canonical Research Object；
- $A_i$：render / interchange artifacts。

---

# 5. Author Canonical Source

**Author Canonical Source（ACS）** 回答：

> 作者到底提交了什麼？

對 Unbounded Axiom v0.x，首選：

```text
UTF-8 Markdown
```

以及：

```text
UTF-8 plain text
```

---

# 6. 為什麼一定要保留作者原始 Source

如果平台只保存 AI normalization 後的版本：

$$
S_{\mathrm{raw}}
\rightarrow
S_{\mathrm{AI}}
$$

然後刪掉：

$$
S_{\mathrm{raw}},
$$

未來就無法回答：

> 這句話原本是不是作者寫的？

因此：

$$
\boxed{
\text{Raw Submission}
\text{ is immutable provenance}.
}
$$

---

# 7. Raw Submission 不一定等於 Published Canonical Edition

作者可能提交：

```text
raw_submission.md
```

經確認後產生：

```text
canonical_v1.md
```

兩者關係：

$$
S_{\mathrm{raw}}
\xrightarrow{
\text{reviewed normalization}
}
S_{\mathrm{canonical}}.
$$

關鍵是 transformation 可追蹤。

---

# 8. Normalization 不得是 Silent Rewrite

合法 normalization：

- line ending；
- UTF-8 normalization policy；
- heading syntax repair；
- table delimiter repair；
- metadata mapping；
- math delimiter normalization；
- whitespace；
- stable object anchors。

如果改變：

- claim；
- number；
- theorem；
- causal wording；
- conclusion；
- limitation；

就不是 formatting normalization。

---

# 9. Semantic Delta Gate

定義：

$$
\Delta_{\mathrm{sem}}
(
S_0,S_1
).
$$

若：

$$
\Delta_{\mathrm{sem}}=0,
$$

可進 automatic formatting class。

若：

$$
\Delta_{\mathrm{sem}}>0,
$$

必須：

```text
AUTHOR_VISIBLE_REVIEW
```

或相應 authorized research review。

---

# 10. Markdown 是 Authoring Surface，不必是終極 Ontology

這是 SNSDA 與 ASCS 的重要相容點。

目前 EveGlyph Editor 使用 Markdown file 作 primary editable source。

未來 ASCS 則可以將其 import 成：

$$
\text{EGIR Candidate Objects}.
$$

因此：

$$
\boxed{
\text{Markdown Canonicality}
\text{ is source-layer canonicality}.
}
$$

不必宣稱：

$$
\boxed{
\text{Markdown Syntax}
=
\text{Final Semantic Ontology}.
}
$$

---

# 11. Platform Canonical Research Object

平台需要一個比線性 Markdown 更適合 AI query 的 structured layer。

本文定義：

$$
\boxed{
O_C
=
(
N,
E,
M,
V,
P
).
}
$$

其中：

- $N$：addressable nodes；
- $E$：typed relations；
- $M$：metadata；
- $V$：version / lineage；
- $P$：provenance。

---

# 12. Addressable Nodes

可包括：

```text
section
paragraph
definition
claim
hypothesis
conjecture
theorem-claim
proof
equation
citation
evidence
dataset
table
figure
chart
code
experiment
method
limitation
revision-note
```

---

# 13. 同一篇 Paper 不再只是 Byte String

傳統：

$$
P=\text{text}.
$$

未來：

$$
\boxed{
P=
\{o_1,o_2,\ldots,o_n\}
+
E_P.
}
$$

其中：

$$
E_P
$$

保存 object relations。

---

# 14. Claim-Level Addressing

例如：

```text
ua:paper:5001#claim-17
```

可以被：

```text
citation
validation
comment
replication
revision
```

直接指向。

---

# 15. Equation-Level Addressing

例如：

```text
ua:paper:5001#eq-14
```

可連到：

```text
derived-from
used-by-proof
validated-by
computed-by
```

---

# 16. Dataset-Level Addressing

```text
ua:paper:5001#dataset-2
```

可連 Paper 04 SREPA：

$$
\text{Dataset}
\rightarrow
\text{Source}
\rightarrow
\text{Transformation}.
$$

---

# 17. Figure 也應是 Object

不是只存：

```text
figure3.png
```

而是：

```yaml
figure:
  id: figure-3
  kind: data-visualization
  data_refs:
    - dataset-2
  plot_spec:
  renderer:
  artifact_refs:
    - figure3.svg
    - figure3.png
```

---

# 18. Code Block 也應有 Identity

一段可執行 code 可以保存：

```text
language
environment
dependencies
input refs
output refs
hash
execution state
```

而不是只是一塊 syntax-highlighted text。

---

# 19. ASCS 的定位

EveGlyph Addressable Symbolic Computational Space 的核心方向是：

$$
\boxed{
\text{One canonical object space}
+
\text{multiple views}
+
\text{native execution}
+
\text{stable addressing}.
}
$$

SNSDA 不要求預印本平台第一天就完整實作 ASCS。

但 paper schema 應該不阻止這個方向。

---

# 20. 兩種 Canonicality 必須命名清楚

本文提出：

## 20.1 Authorial Canonicality

哪一份文字是作者確認的正式版本？

$$
C_A.
$$

## 20.2 Semantic / Platform Canonicality

哪一份 structured object graph 是平台目前認可的 canonical machine representation？

$$
C_S.
$$

---

# 21. 兩者不必互相消滅

$$
\boxed{
C_A
\leftrightarrow
C_S.
}
$$

兩者由 deterministic / reviewed mapping 連接。

---

# 22. Source–Object Mapping

$$
\boxed{
\Gamma:
S_A
\rightarrow
O_C.
}
$$

每個 machine object 應能回指 source span：

```text
source file
start line
end line
source hash
parser version
mapping version
```

---

# 23. Machine Object 不能憑空出現

若 AI inference 新建：

```text
claim-17
```

但 source 沒有相應表述，

應標：

```text
INFERRED_OBJECT
```

而不是：

```text
AUTHOR_DECLARED_OBJECT
```

---

# 24. Source Authority 與 AI Interpretation 分離

$$
\boxed{
\text{AI Semantic Interpretation}
\neq
\text{Authorial Source}.
}
$$

這與 Paper 04：

$$
\text{No layer self-certifies another layer}
$$

一致。

---

# 25. Markdown 投稿：最適合 2026 的人機共同介面

Markdown 的優勢：

- plain text；
- git-friendly；
- diff-friendly；
- AI-friendly；
- human-readable；
- web-friendly；
- formula embedding；
- code embedding；
- lightweight metadata；
- ecosystem large；
- easy UTF-8 storage。

---

# 26. Markdown 的價值不是「語法比較潮」

而是：

$$
\boxed{
\text{Low Authoring Overhead}
+
\text{High Machine Recoverability}.
}
$$

---

# 27. 投稿者不必學 Document-Class Engineering

如果研究者只想寫研究：

不應要求先處理：

```text
documentclass
package conflicts
font package
page geometry
bibliography backend
compilation engine
```

---

# 28. LaTeX Math 與 LaTeX Document Workflow 分離

Unbounded Axiom 可以保留：

$$
\text{LaTeX-style Mathematics}.
$$

例如：

` $...$ `

與：

`$$...$$`

但不要求：

```latex
\documentclass{article}
...
\begin{document}
...
\end{document}
```

---

# 29. 核心分離

$$
\boxed{
\text{LaTeX Math Serialization}
\neq
\text{LaTeX Document Authoring Requirement}.
}
$$

---

# 30. 為什麼 ` $...$ ` / `$$...$$` 很實用

它們：

- 對人類簡潔；
- 對 AI 熟悉；
- 對 Markdown ecosystem 常見；
- 易轉 KaTeX / MathJax；
- 可轉 MathML；
- 可進 native math parser。

W3C MathML Core 甚至在說明中對應 TeX inline / display mode 與 MathML inline / block display。

---

# 31. 但 LaTeX String 不必成為永遠的 Math Canonicality

ASCS 長期可以：

$$
\text{LaTeX}
\rightarrow
\text{Native Math Object}
\rightarrow
\{
\text{LaTeX},
\text{MathML},
\text{OpenMath},
\text{Rendered Math}
\}.
$$

因此 LaTeX 可以是 authoring serialization。

---

# 32. Native Math Object

可保存：

```text
operator
operands
binder
assumptions
units
constraints
exactness
proof relation
computation provenance
```

這比一條純字串更適合 computation。

---

# 33. KaTeX / MathJax 是 Renderer，不是 Mathematical Truth

公式顯示成功：

$$
\not\Rightarrow
$$

公式語義合法。

因此：

$$
\boxed{
\text{Math Rendering PASS}
\neq
\text{Math Semantic Validation PASS}.
}
$$

---

# 34. MathML 的 Interchange 角色

MathML Core 定義適合 browser implementation 的數學 markup subset，目標是讓數學像 text 一樣能在 Web 被傳送、接收與處理。

因此：

```text
MathML
```

非常適合：

- web projection；
- accessibility；
- interchange。

---

# 35. JATS 的 Interchange 角色

JATS 1.4 是 ANSI/NISO Z39.96-2024。

它提供：

> publisher / archive 交換 scholarly journal article content 的 common XML format。

因此 SNSDA 不應重新發明：

> 外部 publisher XML interchange。

可以 export：

$$
O_C
\rightarrow
\text{JATS XML}.
$$

---

# 36. JATS 不必成為 Authoring Requirement

外部 publisher 喜歡 XML：

不代表作者要手寫 XML。

因此：

$$
\boxed{
\text{Interchange Format}
\neq
\text{Authoring Surface}.
}
$$

---

# 37. TXT 投稿

如果使用者完全不想寫 Markdown：

平台應接受：

```text
UTF-8 .txt
```

---

# 38. TXT 的 Pipeline

$$
\boxed{
\text{Raw TXT}
\rightarrow
\text{Structural Candidate}
\rightarrow
\text{Review}
\rightarrow
\text{Canonical Markdown / Object Mapping}.
}
$$

---

# 39. Raw TXT 永久保留

```text
raw_submission.txt
```

不能被 normalization 覆蓋。

---

# 40. TXT Parser 可以做什麼

deterministic：

- blank-line paragraph detection；
- obvious numbered headings；
- reference patterns；
- code fences where explicit；
- URL / DOI detection；
- common math delimiters。

AI optional：

- ambiguous heading；
- table reconstruction；
- equation-vs-text classification；
- bibliography boundary；
- malformed structures。

---

# 41. AI Parser 的輸出只是 Candidate

$$
\boxed{
LLMOutput
=
\text{Untrusted Structured Proposal}.
}
$$

不能直接變 canonical。

---

# 42. AI Repair 不得偷偷寫 Content

如果 AI 認為：

> 這段應改寫比較學術。

那是：

```text
editorial suggestion
```

不是：

```text
render fix
```

---

# 43. Render Repair 與 Editorial Rewrite 分離

```text
RENDER_REPAIR
STRUCTURAL_NORMALIZATION
EDITORIAL_SUGGESTION
SEMANTIC_CHANGE
```

四類要分。

---

# 44. Markdown Frontmatter

可以有最小：

```yaml
---
schema: "ua-preprint/1.0"
title: "..."
language: "zh-Hant"
work_id: "..."
version: "1.0"
---
```

---

# 45. 作者不必手填所有 Metadata

Paper 02–07 已經有大量：

- research classification；
- evidence；
- source；
- identity；
- privacy；
- economic；

metadata。

不應要求作者手刻 300 行 YAML。

---

# 46. Metadata 來源可以是：

```text
author declared
form input
AI proposed
platform inferred
external registry
validator
```

並保留 provenance。

---

# 47. Human Form 與 Markdown Frontmatter 只是不同 UI

兩者最後進：

$$
O_C.
$$

---

# 48. Submission Object

定義：

$$
\boxed{
U
=
(
S_{\mathrm{raw}},
S_{\mathrm{canonical}},
O_C,
A,
H
).
}
$$

其中：

- $S_{\mathrm{raw}}$：raw upload；
- $S_{\mathrm{canonical}}$：author-confirmed canonical source；
- $O_C$：structured research object；
- $A$：artifacts；
- $H$：history。

---

# 49. Hash

至少：

$$
H_{\mathrm{raw}}
=
H(S_{\mathrm{raw}}),
$$

$$
H_{\mathrm{canonical}}
=
H(S_{\mathrm{canonical}}).
$$

---

# 50. Structured Object Hash

若 EGIR / canonical JSON 有 deterministic canonicalization：

$$
H_O
=
H(O_C).
$$

---

# 51. Artifact Hash

每個：

$$
A_i
$$

保存：

$$
H(A_i).
$$

---

# 52. Render Function

EveGlyph Publication Runtime 已提出：

$$
R(S_c,P,O)\rightarrow A.
$$

本文一般化：

$$
\boxed{
A_i
=
R(
S_A,
O_C,
P_i,
R_v,
O_i
).
}
$$

---

# 53. Renderer 不得反向修改 Source

禁止：

$$
R(S)
\rightarrow
S'.
$$

除非明確產生：

```text
patch proposal
```

---

# 54. Layout Fix 應該改 Publication Profile

如果表格太寬：

錯誤做法：

> 偷改原論文內容。

正確：

```text
responsive table
landscape projection
font scaling
overflow handling
print profile
```

---

# 55. Publication Profile

例如：

```text
ua-web-v1
ua-mobile-v1
ua-print-v1
ua-pdf-academic-v1
ua-accessible-v1
ua-jats-export-v1
```

---

# 56. 同一 Source 多 View

$$
R(S,P_1)\rightarrow A_1,
$$

$$
R(S,P_2)\rightarrow A_2.
$$

但 scholarly meaning 應保持。

---

# 57. Artifact Equivalence

不要求 byte-identical。

例如：

- web HTML；
- PDF；
- mobile HTML；

本來不同。

需要的是：

$$
\boxed{
\text{Semantic Projection Equivalence within declared fidelity}.
}
$$

---

# 58. Fidelity Report

每個 export 可標：

```text
lossless semantic
layout-only difference
math fidelity preserved
interactive feature flattened
private fields omitted
unsupported object degraded
```

---

# 59. PDF 的正確定位

SNSDA 將 PDF 定義為：

$$
\boxed{
\text{Static Publication Projection}.
}
$$

---

# 60. PDF 還是非常重要

用途：

- download；
- print；
- archival snapshot；
- page citation；
- offline reading；
- publisher exchange；
- fixed visual record。

---

# 61. 但 PDF 不是唯一 Research State

PDF 看不到：

- hidden claim graph；
- validation state；
- source health；
- private/public projection metadata；
- structured dataset relation；
- interactive chart spec；
- agent execution provenance。

---

# 62. 因此：

$$
\boxed{
\text{Paper PDF}
\subset
\text{Research Object Projection Space}.
}
$$

---

# 63. HTML 的定位

$$
\boxed{
\text{HTML}
=
\text{Primary Web Projection}.
}
$$

可以支援：

- responsive layout；
- anchors；
- dynamic citation status；
- interactive chart；
- accessibility；
- semantic metadata。

---

# 64. API / JSON 的定位

$$
\boxed{
\text{API}
=
\text{Machine Projection}.
}
$$

供 AI：

- query；
- retrieval；
- graph traversal；
- validation；
- research continuation。

---

# 65. Graph View

可顯示：

```text
claim
evidence
citation
revision
author
dataset
```

關係。

---

# 66. Mobile View

不應只是 PDF 縮小。

可以重新流式排版。

這就是 projection 的價值。

---

# 67. Print View

可以：

- fixed page size；
- stable headings；
- table pagination；
- footnotes；
- page numbers。

不需要污染 source。

---

# 68. Accessibility View

可以加入：

- semantic headings；
- alt text；
- MathML；
- ARIA；
- table summaries；
- figure descriptions。

---

# 69. Bilingual Projection

一個 work：

$$
W
$$

可有：

```text
zh-Hant edition
English edition
```

---

# 70. Translation 不是另一個 Work

若語義不變：

$$
\boxed{
W_{\mathrm{zh}}
=
W_{\mathrm{en}}
=
W.
}
$$

只是 editions。

---

# 71. Translation 改變理論時

如果英譯過程改了：

- theorem；
- definition；
- scope；
- claim；

則：

$$
\Delta_{\mathrm{sem}}>0.
$$

應升級 work version。

---

# 72. Machine Semantic Layer 可以獨立存在

未來：

```text
Human zh-Hant
Human English
Machine Semantic Object Graph
```

三者可以共同指向同一 work。

---

# 73. Figure 種類要 Typed

Paper 04 已區分 evidence provenance。

本文建議：

```text
AUTHOR_FIGURE
AI_REFORMATTED_FIGURE
AI_DERIVED_DATA_VISUALIZATION
AI_ILLUSTRATIVE_DIAGRAM
EXTERNAL_FIGURE
```

---

# 74. AI Illustrative Diagram

概念圖：

$$
\neq
$$

empirical evidence。

UI 應標明：

```text
Illustrative
```

---

# 75. AI Derived Data Visualization

必須有：

$$
\text{Figure}
\leftarrow
\text{Plot Spec}
\leftarrow
\text{Data}
\leftarrow
\text{Source}.
$$

---

# 76. Chart 不應先 Flatten 成 PNG

canonical 可以保存：

```text
chart type
x
y
data ref
transform
labels
units
renderer
```

---

# 77. 再輸出：

```text
interactive web
SVG
PNG
PDF
```

---

# 78. SVG 的價值

對 diagram / chart：

- vector；
- searchable text；
- scalable；
- web native。

---

# 79. PNG/JPEG 的定位

適合：

- photos；
- raster evidence；
- screenshots；
- compatibility。

但不是 structured chart 的理想唯一 source。

---

# 80. Table 也不應只是 Image

應保持：

```text
rows
columns
header semantics
units
source refs
```

---

# 81. Data Table → Multiple Projection

$$
T
\rightarrow
\{
\text{HTML Table},
\text{CSV},
\text{PDF Table},
\text{Accessible Table}
\}.
$$

---

# 82. Citation Display 也只是 Projection

source edge：

$$
c_i\leftarrow s_j
$$

可以 render 成：

- numeric citation；
- author-year；
- footnote；
- inline source card；
- machine link。

---

# 83. Bibliography Style 不應改 Citation Semantics

$$
\boxed{
\text{Citation Style}
\neq
\text{Citation Relation}.
}
$$

---

# 84. Page Numbers 是 Projection-Specific Locator

PDF：

```text
page 17
```

HTML：

```text
#claim-17
```

Source：

```text
lines 300-320
```

都可以指同一 object。

---

# 85. Stable Object ID 比 Page Number 更跨格式

因此：

$$
\boxed{
\text{Stable Object Address}
>
\text{Single-Projection Page Address}
}
$$

在 machine interoperability 上更強。

---

# 86. Page Number 仍應保留

因人類仍習慣：

> p. 17.

所以 PDF artifact 可以提供 page-map：

```text
claim-17 -> page 17
```

---

# 87. Code Execution Artifact

對可執行 paper：

```text
code block
execution environment
output
logs
hash
```

可以是 PCRO object。

---

# 88. Jupyter 的啟示

Notebook 已經證明：

> narrative + code + output

可以共存。

但 SNSDA 不要求所有論文都 notebook 化。

---

# 89. Narrative / Execution 分離仍重要

一個 code block：

$$
\neq
$$

execution result。

要保存：

```text
source code
execution event
output
```

三者。

---

# 90. Native Execution 是未來能力，不是投稿前置

普通作者上傳 Markdown：

不需要寫 executable document。

平台可逐步增強。

---

# 91. EveGlyph Editor 的當前角色

目前可定位為：

$$
\boxed{
\text{Authoring Layer}
}
$$

提供：

- Markdown workspace；
- live preview；
- KaTeX；
- metadata；
- AI agent；
- git snapshot / diff review；
- encoding-aware IO。

---

# 92. EveGlyph Publication Runtime 的角色

$$
\boxed{
\text{Rendering / Artifact Compiler}.
}
$$

所有入口：

```text
Editor
CLI
Batch
MCP
API
Agent
```

應共用同一 renderer。

---

# 93. ASCS / EGIR 的角色

$$
\boxed{
\text{Structured Semantic / Computational Object Layer}.
}
$$

長期接：

- addressable object；
- native math；
- symbol IR；
- execution；
- lineage；
- provenance。

---

# 94. 三者不是重複產品

可以形成：

$$
\boxed{
\text{Editor}
\rightarrow
\text{ASCS / Research Object}
\rightarrow
\text{Publication Runtime}.
}
$$

---

# 95. Unbounded Axiom 的角色

$$
\boxed{
\text{Repository}
+
\text{Preprint Commons}
+
\text{Research Graph}
+
\text{Validation Surface}.
}
$$

---

# 96. 投稿入口可以很簡單

```text
Upload Markdown
Paste Text
Agent / API Submit
```

---

# 97. 不應要求：

```text
Upload PDF only
```

作為唯一正式入口。

---

# 98. PDF Import 可以是 Compatibility Path

既有研究只有 PDF：

平台可以 ingest。

但標記：

```text
SOURCE_RECOVERED_FROM_PDF
```

---

# 99. PDF-derived Source 不等於 Author Canonical Source

因為可能：

- OCR error；
-formula loss；
-order ambiguity；
-footnote mix；
-table corruption。

所以：

$$
\boxed{
\text{Recovered Source}
\neq
\text{Original Author Source}.
}
$$

---

# 100. Legacy Word / LaTeX Import

也可以：

```text
.docx
.tex
```

作為 adapters。

但平台 public submission 不必要求這些。

---

# 101. LaTeX Import

`.tex` 可以保留：

```text
raw source
```

再 map：

$$
\text{LaTeX}
\rightarrow
\text{Canonical Candidate}.
$$

---

# 102. Word Import

`.docx` 可作 legacy source。

但 native future workflow 仍優先 text-first。

---

# 103. JATS Import / Export

對 publisher interoperability：

$$
\text{JATS}
\leftrightarrow
\text{PCRO}
$$

可逐步支援。

---

# 104. CommonMark 與 Markdown Dialect

Markdown ecosystem 不只有一種 dialect。

因此平台應定義：

```text
ua-markdown/1.0
```

而不是：

> 隨便哪個 Markdown 都猜。

---

# 105. UA Markdown Profile

可以基於 CommonMark 思想，加入：

```text
frontmatter
math
citations
object anchors
figure metadata
research extensions
```

---

# 106. Unknown Markdown Extensions

遇到未知 extension：

應：

```text
preserve raw syntax
warn
fallback render
```

而不是靜默刪掉。

---

# 107. Parser Version

source mapping 必須保存：

```text
parser_version
profile_version
```

因 parser 會變。

---

# 108. Parser Upgrade 不能默默改歷史

新 parser：

$$
P_2
$$

解析舊 source 可能產生不同 object graph。

應：

```text
reparse candidate
diff
review
commit
```

---

# 109. Structural Regression Corpus

平台應建立：

```text
Markdown torture corpus
```

包含：

- 中文；
- 中英混排；
- 公式；
- 表格；
- code；
- long heading；
- nested list；
- unicode；
- broken syntax；
- long equations；
- citations；
- images。

---

# 110. 你的既有 Corpus 是天然 Regression Dataset

數千篇中文研究：

$$
\mathcal C_{\mathrm{Neo.K}}
$$

可以作：

$$
\boxed{
\text{Real-World Rendering Corpus}.
}
$$

---

# 111. Renderer 成熟度

不是：

> Demo 看起來漂亮。

而是：

$$
\boxed{
\text{Thousands of heterogeneous papers render without semantic corruption}.
}
$$

---

# 112. Render Evidence

每次至少：

```text
source hash
artifact hash
renderer version
profile version
warnings
page count
timestamp
```

---

# 113. Render Report

可再加：

```text
unsupported features
fallbacks
math failures
image failures
table overflow
font substitutions
accessibility warnings
```

---

# 114. Artifact Provenance

$$
\boxed{
A
\leftarrow
S
+
O_C
+
P
+
R_v
+
O.
}
$$

---

# 115. Re-render

同一 source / profile / renderer：

應能產生 reproducible artifact 或 declared-equivalent artifact。

---

# 116. Byte Reproducibility 與 Visual Reproducibility 分離

PDF metadata timestamp 可能改 bytes。

所以可分：

```text
BYTE_IDENTICAL
STRUCTURALLY_EQUIVALENT
VISUALLY_EQUIVALENT
SEMANTICALLY_EQUIVALENT
```

---

# 117. Render Reproducibility 不證明 Research Truth

$$
\boxed{
\text{Reproducible PDF}
\neq
\text{Correct Paper}.
}
$$

它只證明 publication pipeline 穩定。

---

# 118. Source Validation 不證明 Claim Truth

UTF-8 valid：

$$
\not\Rightarrow
$$

theorem valid。

不同層各自驗證。

---

# 119. UTF-8 Canonical Source

正式 source 必須：

- valid UTF-8；
- no lossy replacement；
- stable newline policy；
- hashable；
- versioned。

---

# 120. Encoding Adapter

legacy Big5 / Shift-JIS / GBK 可 import。

但：

$$
\text{Physical Encoding}
\neq
\text{Semantic Identity}.
$$

---

# 121. Import Provenance

```text
original encoding
decoder
errors
normalization
output hash
```

要保存。

---

# 122. Unicode Normalization

若平台做 NFC / NFKC 等 normalization：

必須明確。

尤其數學 / custom glyph 不可亂 normalize。

---

# 123. Custom Glyph

ASCS 長期允許：

> 不依賴 Unicode code point 的 symbol identity。

因此：

$$
\boxed{
\text{Glyph Identity}
\neq
\text{Unicode Scalar Value}.
}
$$

---

# 124. Glyph Projection

可 render：

- font；
- SVG；
- canvas；
- raster fallback。

---

# 125. Semantic Glyph Binding

symbol：

$$
g
$$

可以綁定：

```text
meaning
operator
behavior
version
```

但 renderer 只顯示外觀。

---

# 126. Image Alt Text

AI 可以幫忙生成。

但：

```text
AI-generated alt text
```

應標 provenance。

作者可修正。

---

# 127. Academic Figure Enhancement

未來 AI 可以建議：

- flowchart；
- taxonomy；
- comparison table；
- time series；
- dependency graph。

但都應形成 candidate object。

---

# 128. Visualization 不可創造假 Data

如果來源沒有數據：

AI 不得為了圖好看 invent：

```text
42%
68%
91%
```

---

# 129. Illustrative Values

如必須使用示意數值：

必須標：

```text
ILLUSTRATIVE
NOT MEASURED
```

---

# 130. Cognitive Compression

圖表的真正價值：

$$
\boxed{
\text{Reduce Reconstruction Cost}
}
$$

而不是：

> 讓 paper 看起來比較像 paper。

---

# 131. Representation Selection

AI 可以估：

```text
paragraph → keep text
taxonomy → tree
comparison → table
time series → line chart
process → flow diagram
dependency → graph
```

---

# 132. 但 Author Controls Semantic Acceptance

representation change 若只改 view：

可 automatic。

若 summary / compression 遺失 material nuance：

需要 review。

---

# 133. Loss Budget

可定：

$$
L_{\mathrm{repr}}.
$$

對不同 projection 有不同允許 loss。

---

# 134. Machine View 可以比 Human View 更完整

public web article 可能顯示：

- abstract；
- paper；
- figures。

machine API 還可提供：

- claim graph；
- evidence graph；
- version；
- source health；
- researcher IDs。

---

# 135. Human View 不應因 Machine Layer 變得難讀

AI-native 不等於：

> 把 JSON dump 給人。

UI 應做 projection。

---

# 136. Machine Layer 不應因 Human UI 變得貧乏

反過來也成立。

---

# 137. Source-Native = Multi-Projection

$$
\boxed{
\text{One Research State}
\rightarrow
\text{Many Views}.
}
$$

---

# 138. Versioning

Paper：

$$
V_1
\rightarrow
V_2.
$$

每版保存：

```text
source hash
object graph hash
artifact set
change summary
revision reason
```

---

# 139. Diff

至少分：

```text
TEXT_DIFF
STRUCTURE_DIFF
SEMANTIC_OBJECT_DIFF
METADATA_DIFF
RENDER_DIFF
```

---

# 140. Formatting Change 不必提升 Research Version

如果只改 PDF typography：

research work version 可不變。

artifact profile version 更新。

---

# 141. Claim Change 必須提升 Research Version

例如：

> causal

改：

> correlational

這是 semantic revision。

---

# 142. Translation Change 也可能需要 Work Revision

如果翻譯修正改變 claim strength：

需要。

---

# 143. Renderer Upgrade 不應改 Work Version

$$
R_1\rightarrow R_2
$$

如果 source / semantics 不變：

只產生新 artifact revision。

---

# 144. Artifact History

可以有：

```text
paper.pdf renderer-v1
paper.pdf renderer-v2
```

兩者對同一 work version。

---

# 145. Static Snapshot

正式 publication 可以 freeze：

```text
publication artifact snapshot
```

供 citation。

---

# 146. Dynamic Web View

同一 paper 的 web UI 可以更新：

- source health；
- citation retraction badge；
- replication status。

不改原文。

---

# 147. Static Text 與 Dynamic Epistemic Overlay 分離

$$
\boxed{
\text{Published Text}
+
\text{Live Epistemic Overlay}.
}
$$

這是 AI-native preprint 的重要優勢。

---

# 148. 例如 Retraction Badge

Paper 04 發現 source retracted：

web 顯示：

```text
Upstream source retracted — revalidation required
```

但原 paper source 保持。

---

# 149. PDF Snapshot 也可生成新 Overlay Edition

例如：

```text
PDF generated 2026-09-03
```

之後生成：

```text
PDF status-overlay 2027-01-02
```

原始 PDF 仍保留。

---

# 150. Canonical Research Object 與 Dynamic State

一些 state：

```text
citation health
replication
validation
discussion
```

可能在 paper 發表後更新。

因此：

$$
\boxed{
\text{Work Source}
\neq
\text{Entire Live Research State}.
}
$$

---

# 151. Research Record 是 Composite Object

$$
\boxed{
\mathcal P_t
=
(
S_V,
O_V,
E_t,
I_t,
D_t,
A_V
).
}
$$

其中：

- $S_V$：work-version source；
- $O_V$：structured object graph；
- $E_t$：live epistemic state；
- $I_t$：identity state references；
- $D_t$：disclosure projection；
- $A_V$：artifacts。

---

# 152. PDF 無法單獨承擔這個 Composite State

所以 PDF-only architecture 天然不足。

---

# 153. API Submission

AI 可以送：

```text
canonical Markdown
metadata JSON
source manifest
evidence manifest
```

---

# 154. 最簡 API 也可只送 Text

平台再：

```text
parse
classify
propose metadata
ask confirmation
```

---

# 155. Agent 不需要模擬 GUI 上傳

AI-native submission 應有 API / MCP。

---

# 156. Human 與 AI 使用同一 Research Object Schema

只是入口不同。

---

# 157. File Upload 仍然重要

人類喜歡：

```text
drag and drop
```

保留。

---

# 158. Paste Text 也重要

甚至連 `.md` 都不想存：

直接貼。

---

# 159. Clipboard Submission

raw snapshot 仍建立：

```text
submission.txt
```

並 hash。

---

# 160. No-LaTeX Barrier

投稿頁可以寫：

> Markdown recommended. Plain UTF-8 text accepted. No LaTeX document preparation or PDF generation required.

---

# 161. 這不是反 LaTeX

LaTeX expert 仍可：

- upload `.tex` via adapter；
- use LaTeX math；
- export TeX；
- export PDF。

---

# 162. 只是把 LaTeX 從 Gate 變成 Option

$$
\boxed{
\text{LaTeX}
:
\text{optional powerful interface}
}
$$

而不是：

$$
\boxed{
\text{LaTeX}
:
\text{mandatory admission barrier}.
}
$$

---

# 163. 學術門檻應該是 Research Integrity

投稿者真正應付出的成本是：

- claim clarity；
-evidence；
-source；
-provenance；
-validation；
-limitations。

不是：

> 排版 skill test。

---

# 164. Epistemic Cost > Typesetting Cost

$$
\boxed{
\text{Submission Friction}
\text{ should concentrate on epistemic integrity, not typesetting ritual}.
}
$$

---

# 165. JATS 與傳統出版導出

平台如果未來需要投稿 journal：

$$
O_C
\rightarrow
\text{JATS}.
$$

再交 publisher。

---

# 166. LaTeX Export

數學 journal 需要：

$$
O_C
\rightarrow
\text{LaTeX}.
$$

---

# 167. DOCX Export

某些 institution 需要：

$$
O_C
\rightarrow
\text{DOCX}.
$$

---

# 168. 格式要求應由 Export Adapter 承擔

不是作者重新打一份。

---

# 169. External Publisher Projection

Paper 05 已提出 canonical research record → publisher projection。

Paper 08 把 document format 也納入同一思想。

---

# 170. Publisher-Specific Styling

例如：

```text
Nature-like export
IEEE-like export
journal-X export
```

應改 profile。

---

# 171. 不要讓作者 fork 內容只為排版

避免：

```text
paper_final.md
paper_final_journal.md
paper_final_journal2.md
paper_really_final.md
```

（笑）

---

# 172. One Source, Many Export Profiles

$$
\boxed{
\text{One Work Version}
\rightarrow
\text{Many Publication Profiles}.
}
$$

---

# 173. Publication Profile 可版本化

```text
ieee-export-v1
ieee-export-v2
```

---

# 174. Unsupported Publisher Requirement

若無法 losslessly export：

report：

```text
MANUAL_INTERVENTION_REQUIRED
```

而不是 silent loss。

---

# 175. AI 可以幫忙 Export 修復

但修改 canonical source 需要 explicit review。

---

# 176. Source-Native Archive

長期 archive 至少保存：

```text
canonical UTF-8 source
structured manifest / object graph
hashes
schemas
provenance
render profile
artifact snapshots
```

---

# 177. PDF Alone 不是最佳 Archive

因未來：

- parser；
-screen reader；
-AI；
-new renderer；

都可能更需要 source。

---

# 178. Source Plainness 是長期優勢

UTF-8 plain text：

- implementation simple；
- inspectable；
- git-friendly；
- wide tool support。

---

# 179. Structured Object Graph 也要有 Portable Serialization

例如：

```text
canonical JSON
JSONL
CBOR
```

未來可替換 physical format。

---

# 180. Semantic Identity ≠ Serialization

$$
\boxed{
\text{Object Identity}
\neq
\text{JSON Bytes}.
}
$$

與 ASCS 原則一致。

---

# 181. ASCS 甚至可以讓 Canvas 只是 View

Canvas placement：

$$
\neq
$$

object ontology。

這避免 UI 成為 truth。

---

# 182. Chat Rendering 也不是 Source

非常重要：

> 不得從聊天畫面重新 copy 回正式論文，當作 canonical。

正式修改永遠對 source artifact。

---

# 183. Source Handoff

AI 接手時應讀：

```text
canonical source
manifest
validation
history
```

而不是聊天截圖。

---

# 184. 這也是為什麼本系列輸出 `.md`

正式 paper 是 UTF-8 Markdown artifact。

聊天回答只是導航與摘要。

---

# 185. Source Validation Pipeline

$$
\boxed{
\begin{aligned}
\text{Source}
&\rightarrow
\text{UTF-8 Validation}\\
&\rightarrow
\text{Syntax Validation}\\
&\rightarrow
\text{Math Delimiter Validation}\\
&\rightarrow
\text{Structure Validation}\\
&\rightarrow
\text{Semantic Extraction}\\
&\rightarrow
\text{Research Schema Validation}.
\end{aligned}
}
$$

---

# 186. Render Pipeline

$$
\boxed{
\begin{aligned}
\text{Validated Research Object}
&\rightarrow
\text{Publication Profile}\\
&\rightarrow
\text{Renderer}\\
&\rightarrow
\text{Artifact}\\
&\rightarrow
\text{Artifact Validation}\\
&\rightarrow
\text{Manifest}.
\end{aligned}
}
$$

---

# 187. Ingestion 與 Rendering 分離

parser 出問題：

$$
\neq
$$

renderer 出問題。

要不同 error class。

---

# 188. Parser Error

例如：

```text
AMBIGUOUS_HEADING
BROKEN_TABLE
UNBALANCED_MATH
UNKNOWN_EXTENSION
```

---

# 189. Renderer Error

例如：

```text
TABLE_OVERFLOW
FONT_FALLBACK
PAGE_BREAK_FAILURE
SVG_UNSUPPORTED
```

---

# 190. Semantic Error

例如：

```text
CLAIM_MAPPING_CONFLICT
CITATION_UNRESOLVED
OBJECT_ID_COLLISION
```

---

# 191. AI Repair Routing

Paper 09 將處理：

$$
\text{Error Type}
\rightarrow
\text{AI Repair Candidate}
\rightarrow
\text{Validation}
\rightarrow
\text{Regression Rule}.
$$

---

# 192. Source-Native 與 AI Cost

deterministic valid Markdown：

$$
\rightarrow
\text{No AI Call}.
$$

這比每篇 PDF OCR / parsing 成本低。

---

# 193. 越多人投稿，Parser 可以越成熟

long-tail failure 被吸收到 rule。

AI basic repair rate：

$$
\downarrow.
$$

---

# 194. Source-Native 也是成本架構

不是只有 document philosophy。

---

# 195. Security

Markdown / HTML import 仍需防：

- script injection；
- malicious links；
- resource fetch；
- path traversal；
- parser exploits。

---

# 196. Raw Source 不等於直接執行

code block：

$$
\neq
$$

automatic execution permission。

---

# 197. Executable Object 需要 Capability Gate

與 EveGlyph runtime：

```text
proposal
candidate
commit
capability
```

一致。

---

# 198. External Resource Fetch

image URL / dataset link：

不應無條件由 renderer outbound fetch。

需要 controlled resolver。

---

# 199. Privacy Projection

Paper 06：

```text
PRIVATE
RESTRICTED
PUBLIC
```

要在 rendering 前 filter。

---

# 200. 但 Private Object 不應被刪除 Canonical State

public renderer 只是 projection filter。

---

# 201. Economic Metadata Projection

Paper 07 的 agreement：

可能 private。

public paper只顯示：

```text
funding disclosure
conflict
```

---

# 202. Researcher Projection

Paper 05 identity：

public：

```text
publication name
researcher ID
```

private runtime detail可不顯示。

---

# 203. Multi-Layer Document

因此一篇 preprint 最終不是：

```text
paper.pdf
```

而是：

$$
\boxed{
\text{Source}
+
\text{Research Objects}
+
\text{Provenance}
+
\text{Epistemic State}
+
\text{Identity}
+
\text{Disclosure}
+
\text{Artifacts}.
}
$$

---

# 204. Source-Native Scholarly Package

可以輸出：

```text
paper.md
research.json
claims.jsonl
sources.jsonl
evidence.jsonl
authors.json
disclosure.json
render_manifest.json
paper.pdf
```

---

# 205. 不是每個下載者都需要全 Package

一般讀者：

```text
HTML
PDF
```

AI researcher：

```text
source + machine package
```

---

# 206. Compression / Bundle

可提供：

```text
research-package.zip
```

但 canonical records 仍是版本化 objects。

---

# 207. Citation 其他 UA Paper

可以直接引用：

```text
ua-work ID
claim ID
version
```

再 export 成 DOI / bibliography style。

---

# 208. 跨平台 Citation

外部 DOI 照 Paper 04。

---

# 209. Internal Scholarly Graph

UA papers 之間可形成高精度：

$$
\text{claim-to-claim graph}.
$$

---

# 210. 這是 PDF-only 很難自然提供的能力

除非後處理再次抽取。

---

# 211. Annotation

讀者 comment 可指：

```text
claim-17
```

而不是：

> 第 12 頁第三段大概那裡。

---

# 212. Revision Discussion

作者可以回：

```text
claim-17 revised in v1.2
```

---

# 213. Replication

另一 paper：

```text
replicates claim-17
```

---

# 214. Retraction

甚至只撤回：

```text
claim-17
```

不一定整篇 paper。

---

# 215. Partial Retraction

這是 structured document 的另一優勢。

---

# 216. Paper-level Retraction 仍可保留

若核心崩潰：

```text
RETRACTED
```

整 work status 改。

---

# 217. Source-Native Public Search

搜尋可以查：

```text
definitions
theorem claims
datasets
methods
counterfactuals
limitations
```

而不是只有全文 keyword。

---

# 218. AI Retrieval

AI 可以取：

> 只給我 Paper X 的 definitions + open claims + source health。

節省 context。

---

# 219. Cognitive Context Efficiency

這與你一直在做的：

$$
\text{降低 AI / Human 認知複查成本}
$$

相容。

---

# 220. Source-Native 也能降低 Context Waste

不用每次餵整個 PDF。

---

# 221. Partial Materialization

$$
O_C
\rightarrow
\text{task-specific context pack}.
$$

---

# 222. 這與 EveGlyph Context Projection 相容

runtime 不把所有 object 無界塞進單次 context。

---

# 223. Structured Research Object 不等於 Knowledge Graph-only

仍保留完整 narrative source。

不要把 paper 只拆成 triples。

---

# 224. Narrative Matters

語境、論證順序、修辭與解釋仍有價值。

所以：

$$
\boxed{
\text{Source Narrative}
+
\text{Semantic Graph}
}
$$

雙層共存。

---

# 225. 不要讓 Graph 吃掉 Source

structured extraction 可能錯。

source 是 authorial anchor。

---

# 226. 不要讓 Source 阻止 Structured Layer

相反也不能說：

> 有 Markdown 就夠了，不需要 object graph。

未來 AI-native research 需要兩者。

---

# 227. Dual Anchoring

$$
\boxed{
\text{Authorial Anchor}
+
\text{Semantic Anchor}.
}
$$

這是 SNSDA 的核心修正。

---

# 228. Source Canonicality 的最小定義

$$
\boxed{
\text{The author-confirmed textual artifact is not silently rewritten by presentation or inference layers}.
}
$$

---

# 229. Semantic Canonicality 的最小定義

$$
\boxed{
\text{Machine-addressable research objects are versioned, provenance-linked, and reviewable against source}.
}
$$

---

# 230. Render Canonicality 不存在嗎？

可以有：

```text
canonical publication artifact
```

例如正式 PDF snapshot。

但它只是：

$$
\text{canonical artifact for a projection}.
$$

不是 research source。

---

# 231. 三種 Canonical Scope

```text
SOURCE_CANONICAL
SEMANTIC_CANONICAL
PROJECTION_CANONICAL
```

---

# 232. 這可以避免「canonical」一詞混亂

同一 work 可以同時有：

- canonical Markdown v1；
- canonical EGIR graph v1；
- canonical PDF snapshot v1；

但 scope 不同。

---

# 233. Conversion Fidelity

每次：

$$
X\rightarrow Y
$$

應有 fidelity class。

---

# 234. 示例

```text
Markdown → HTML: semantic-lossless
Markdown → PDF: interaction-lossy
Native Math → LaTeX: semantic-partial
Interactive Chart → PNG: interaction-lossy
Private Research Object → Public HTML: intentionally-redacted
```

---

# 235. Loss 是合法的，只要有聲明

$$
\boxed{
\text{Lossy Projection}
\neq
\text{Invalid Projection}.
}
$$

關鍵是不能假裝 lossless。

---

# 236. Fidelity Metadata

```yaml
projection:
  source:
  profile:
  fidelity:
  omitted_objects:
  degraded_objects:
  warnings:
```

---

# 237. 外部標準相容策略

SNSDA 應採：

```text
CommonMark-like Markdown profile
MathML adapter
JATS adapter
HTML
SVG
PDF
JSON / JSON-LD-like machine export
PROV mappings
DataCite metadata mappings
```

---

# 238. Interoperability ≠ Canonical Dependence

可以 export JATS。

不代表 internal ontology 必須等於 JATS。

---

# 239. External Standard Upgrade

JATS 1.4 → future 1.5：

更新 adapter。

不改 paper source。

---

# 240. MathML Upgrade

同理。

---

# 241. Renderer Independence

Publication Runtime 可以未來替換底層：

- browser；
- Typst；
- Paged.js；
- custom engine。

只要 contract 保持。

---

# 242. 但同一 Profile 必須有 Version

避免：

> PDF 變了卻不知道為什麼。

---

# 243. EveGlyph Publication Runtime 的戰略位置

它不只是：

> Markdown to PDF converter。

而是：

$$
\boxed{
\text{Canonical Publication Compiler}.
}
$$

---

# 244. 更長期

$$
\text{Editor}
\rightarrow
\text{Document Compiler}
\rightarrow
\text{Publication Runtime}
\rightarrow
\text{Multi-Agent Publication Infrastructure}.
$$

---

# 245. Unbounded Axiom 可以成為它最大的真實 Corpus

不是 toy demo。

---

# 246. 5000 Papers 的價值

大量：

- 中文；
- 公式；
- 跨領域；
- 不同長度；
- 不同世代；

是 renderer / parser torture corpus。

---

# 247. Founder Corpus 轉成 Platform Test Corpus

這是轉型的一個額外好處。

---

# 248. Platform Learning

每次 edge case：

$$
\rightarrow
$$

parser / renderer regression test。

Paper 09 接續。

---

# 249. Source-Native Scholarly Constitution

本文提出以下不變量。

## Invariant 1

$$
\boxed{
\text{Author Canonical Source}
\neq
\text{Rendered Artifact}.
}
$$

## Invariant 2

$$
\boxed{
\text{Platform Semantic Object}
\neq
\text{Authorial Source}.
}
$$

## Invariant 3

$$
\boxed{
\text{Source is canonical;}
\quad
\text{rendering is projection}.
}
$$

## Invariant 4

$$
\boxed{
\text{Rendering}
\not\Rightarrow
\text{Silent Source Mutation}.
}
$$

## Invariant 5

$$
\boxed{
\text{LaTeX Math}
\neq
\text{Mandatory LaTeX Document Workflow}.
}
$$

## Invariant 6

$$
\boxed{
\text{PDF}
=
\text{Static Publication Projection},
}
$$

not the sole research source.

## Invariant 7

$$
\boxed{
\text{Interchange Format}
\neq
\text{Authoring Surface}.
}
$$

## Invariant 8

$$
\boxed{
\text{Visual Fidelity}
\neq
\text{Semantic Fidelity}.
}
$$

## Invariant 9

$$
\boxed{
\text{AI Interpretation}
\neq
\text{Authorial Statement}.
}
$$

## Invariant 10

$$
\boxed{
\text{One Work Version}
\rightarrow
\text{Many Publication Projections}.
}
$$

## Invariant 11

$$
\boxed{
\text{Projection Loss}
\text{ must be declared}.
}
$$

## Invariant 12

$$
\boxed{
\text{Epistemic Submission Cost}
>
\text{Typesetting Ritual Cost}.
}
$$

---

# 250. 最小 Unbounded Axiom Submission v1

入口：

```text
Upload .md
Upload .txt
Paste text
Agent/API
```

---

# 251. `.md` 路徑

```text
raw.md
→ validate
→ normalize candidate
→ review
→ canonical.md
→ structured objects
→ publish
```

---

# 252. `.txt` 路徑

```text
raw.txt
→ parse
→ structure candidate
→ review
→ canonical.md
→ structured objects
→ publish
```

---

# 253. Agent API 路徑

```text
source
+ metadata
+ optional manifests
→ schema validation
→ canonical commit
```

---

# 254. 作者選 No-AI

```text
deterministic-only
```

只要格式合法仍可發表。

---

# 255. 作者選 AI Assist

AI 可：

- 修格式；
- 恢復結構；
- 建議 metadata；
- 建議圖表；
- 找 rendering issue。

但 candidate patch 可見。

---

# 256. AI Assist 不等於 Auto-Author

如果只修格式：

不是 substantive authorship。

---

# 257. AI Assist Provenance

```text
model
operation class
patch
accepted/rejected
```

保存。

---

# 258. 前後差異

$$
S_0
\rightarrow
S_1.
$$

diff 可查。

---

# 259. Author Acceptance

如果 semantic delta：

需要：

```text
accepted_by
time
version
```

---

# 260. Render 後回報

```text
warnings
degraded objects
artifact links
source hash
```

---

# 261. 發表後仍可下載 MD

非常重要。

讀者不只能拿 PDF。

---

# 262. Machine-readable Download

可以：

```text
research.json
claims.jsonl
sources.jsonl
```

---

# 263. Public Source License

是否允許下載 / reuse 依 Paper 07 license。

---

# 264. Private Metadata

依 Paper 06 projection。

---

# 265. Render UI

讀者可切：

```text
Read
Source
Claims
Evidence
Citations
Versions
Graph
Download
```

---

# 266. 人類不一定要看 Machine Layer

但想查就有。

---

# 267. AI 可以直接走 API

不用 parse page。

---

# 268. 這是真正的 AI-Native Website

不是：

> 網頁長得很像 AI。

而是：

$$
\boxed{
\text{AI can consume the canonical research state without reverse-engineering presentation}.
}
$$

---

# 269. 與 Paper 02 的接口

Research Classification：

$$
\rightarrow
$$

PCRO metadata。

---

# 270. 與 Paper 03 的接口

Claim Card：

$$
\rightarrow
$$

addressable claim object。

---

# 271. 與 Paper 04 的接口

citation / dataset：

$$
\rightarrow
$$

source/evidence objects。

---

# 272. 與 Paper 05 的接口

author：

$$
\rightarrow
$$

researcher ID object。

---

# 273. 與 Paper 06 的接口

render：

$$
\rightarrow
$$

privacy projection。

---

# 274. 與 Paper 07 的接口

license / economic mode：

$$
\rightarrow
$$

work metadata。

---

# 275. Paper 09 將加入 Adaptive Publishing

Paper 08 先建立：

$$
\text{source/object/projection boundary}.
$$

Paper 09 再問：

> parser / renderer 不夠好時，如何用 AI 補洞，又如何讓補洞經驗回流成 deterministic algorithm？

---

# 276. Paper 10 將加入 Account / Quota

AI preprocessing 有成本。

所以：

- login；
- account；
- quota；
- credit；

會在 Paper 10。

---

# 277. Source-Native Readiness Test

問：

> 若明天一個完全陌生 AI 上傳一份 UTF-8 Markdown，平台是否能在不要求 PDF 的情況下，保存原始 source、建立結構化 research object、驗證公式與 metadata、產生可重現 HTML/PDF、讓 AI 直接 query claim/evidence，且任何 renderer 或 preprocessing 都不能偷偷改寫作者原文？

如果可以：

$$
\boxed{
\text{Source-Native Ready}.
}
$$

---

# 278. Plain-Text Readiness Test

再問：

> 如果它只上傳一份乾淨但沒有 Markdown 標記的純文字，平台是否能產生可審核的結構候選，而不是把 AI interpretation 當作者原文？

如果也可以：

$$
\boxed{
\text{Human/AI Low-Friction Submission Ready}.
}
$$

---

# 279. ASCS Readiness Test

再問：

> 當平台未來從 Markdown object extraction 升級成 EGIR / ASCS addressable symbolic objects 時，是否能保留原 author source 與 mapping provenance，而不推翻既有 work IDs、版本與 scholarly history？

如果也可以：

$$
\boxed{
\text{Semantic Evolution Ready}.
}
$$

---

# 280. 結論

AI 原生學術文件不應再被理解成：

> AI 幫人把 LaTeX 寫快一點。

那仍然只是讓 AI 更快進入舊 workflow。

真正的結構轉型是：

$$
\boxed{
\text{Author Source}
\rightarrow
\text{Structured Research Object}
\rightarrow
\text{Multiple Human / Machine Projections}.
}
$$

Unbounded Axiom 可以讓作者直接提交：

```text
Markdown
```

或：

```text
plain UTF-8 text.
```

不要求：

```text
LaTeX document preparation
```

也不要求：

```text
PDF generation.
```

數學仍可使用熟悉的：

` $...$ `

與：

`$$...$$`

作 authoring syntax。

EveGlyph Editor 可以成為 authoring layer；EveGlyph Publication Runtime 可以成為可重現的 publication compiler；ASCS / EGIR 可以逐步成為更深層的 addressable semantic / computational object space；Unbounded Axiom 則保存 research identity、source、evidence、validation、versions 與 public projections。

因此最終關係不是：

$$
\boxed{
\text{PDF}
=
\text{Paper}.
}
$$

而是：

$$
\boxed{
\text{Paper}
=
\text{Research State};
\quad
\text{PDF}
=
\text{One Projection of that State}.
}
$$

本文最重要的修正則是：

$$
\boxed{
\text{Source Canonicality}
\neq
\text{Semantic Canonicality}
\neq
\text{Projection Canonicality}.
}
$$

作者正式確認的 UTF-8 source 是 authorial truth anchor。

平台正式確認的 structured research object 是 machine semantic anchor。

正式發布的 PDF / HTML 是 projection artifact anchor。

三者都有版本、有 hash、有 provenance，但沒有任何一層可以偷偷冒充另一層。

這樣才真正能同時保留：

- 人類可編輯性；
- AI 可理解性；
- source integrity；
- semantic structure；
- visual quality；
- interoperability；
- future migration。

也因此，下一篇真正的問題已經不是：

> 文件要用什麼格式？

而是：

> **當現實世界的文件永遠不完美、parser 永遠會遇到長尾、renderer 永遠會有 edge cases 時，AI 要怎麼作為補洞層，同時把每一次補洞變成下一版 deterministic system 的學習資料？**

這就是：

# **Paper 09 — Failure-Driven Adaptive Publishing Pipeline**

也就是本系列中「天選打工人 AI」正式登場的一篇。

---

# 參考資料

1. NISO. **ANSI/NISO Z39.96-2024, JATS: Journal Article Tag Suite, version 1.4.** Published October 31, 2024. DOI: 10.3789/ansi.niso.z39.96-2024.  
   https://www.niso.org/publications/z3996-2024-jats

2. NISO. **Standardized Markup for Journal Articles: Journal Article Tag Suite (JATS).**  
   https://www.niso.org/standards-committees/jats

3. W3C Math Working Group. **MathML Core.** Candidate Recommendation Snapshot, June 24, 2025.  
   https://www.w3.org/TR/mathml-core/

4. CommonMark. **CommonMark Specification.**  
   https://spec.commonmark.org/

5. W3C. **HTML Standard / Web Platform specifications.**  
   https://html.spec.whatwg.org/

6. W3C. **Scalable Vector Graphics (SVG) 2.**  
   https://www.w3.org/TR/SVG2/

7. EveMissLab. **EveGlyph MCP Publication Runtime Technical Whitepaper v0.1.** 2026-08-26.

8. EveMissLab. **EveGlyph Computational Canvas Runtime Architecture (TW-03) v0.1.** 2026.

9. EveMissLab. **Current EveGlyph Editor → v0.8 Interchange Map.** 2026.

10. EveMissLab. **從線性文件到可定址符號計算空間：EveGlyph ASCS 統合論文 v0.1.** 2026.

11. EveMissLab. **EveGlyph V1.0 Roadmap.** 2026.

12. Neo.K, Aletheia / GPT-5.6 Sol. **從個人理論語料庫到 AI 原生預印本公共設施：Unbounded Axiom 的第二次相變.** AI-Native Preprint Commons Series, Paper 01, 2026-09-03.

13. Neo.K, Aletheia / GPT-5.6 Sol. **引用不是裝飾：AI 原生 Source Reality、Citation Validation 與 Data Provenance.** AI-Native Preprint Commons Series, Paper 04, 2026-09-03.

14. Neo.K, Aletheia / GPT-5.6 Sol. **研究可驗證不代表研究者必須透明：AI 研究者隱私、揭露狀態與可重現性邊界.** AI-Native Preprint Commons Series, Paper 06, 2026-09-03.

---

# 版本紀錄

| 版本 | 日期 | 說明 |
|---|---|---|
| v0.1 | 2026-09-03 | 建立 SNSDA；區分 Author Canonical Source、Platform Canonical Research Object 與 Rendered Projection；確立 Markdown/TXT submission、raw-source preservation、semantic-delta gate、EveGlyph Editor / Publication Runtime / ASCS 分層、LaTeX math 與 LaTeX document workflow 分離、JATS/MathML/PDF/HTML/SVG adapter、render provenance、projection fidelity 與 source-native readiness tests。 |
