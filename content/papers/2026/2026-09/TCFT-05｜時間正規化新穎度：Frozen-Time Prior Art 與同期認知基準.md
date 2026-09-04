---
title: "TCFT-05｜時間正規化新穎度：Frozen-Time Prior Art 與同期認知基準"
title_en: "Time-Normalized Novelty: Frozen-Time Prior Art and Contemporaneous Cognitive Baselines"
series: "Temporal Cognitive Frontier Theory (TCFT) / 時代認知前沿理論"
paper_no: "05"
version: "v0.1"
date: "2026-08-31"
author: "Neo.K"
affiliation: "EveMissLab / 一言諾科技有限公司"
document_type: "理論論文 / Temporal Novelty Audit 篇"
language: "zh-Hant"
status: "正式系列初稿"
previous_paper: "TCFT-04｜高階推理不等於高階策略：認知成本、注意力分配與停止治理"
next_paper: "TCFT-06｜動態認知異常前沿：歷史超前與持續超前"
---

# TCFT-05｜時間正規化新穎度：Frozen-Time Prior Art 與同期認知基準

## Time-Normalized Novelty: Frozen-Time Prior Art and Contemporaneous Cognitive Baselines

**系列：** Temporal Cognitive Frontier Theory, TCFT / 時代認知前沿理論  
**篇次：** 05  
**版本：** v0.1  
**日期：** 2026-08-31  
**作者：** Neo.K  
**機構脈絡：** EveMissLab / 一言諾科技有限公司  

---

## 摘要

「這個想法很超前」是一個極容易被後見之明、名人神話、資料缺漏、語義相似、版本污染與現代工具能力扭曲的判斷。某個歷史文本今天看起來與現代理論相似，不代表其作者在當時已具備同一結構；某個概念今天看起來普通，也不代表它在產生當時不具高度新穎性；某項成果後來極其重要，也不代表其在當時就比同期所有合理基準更不可推導。反過來，一項在當時真正高度新穎的工作，也可能多年後才被理解、驗證或重估。

本文提出 Temporal Cognitive Frontier Theory（TCFT）的 **Time-Normalized Novelty（時間正規化新穎度，TNN）** 與 **Frozen-Time Prior-Art Audit（時間凍結先前技術／先前知識審查，FTPA）**。其核心原則是：

$$
\boxed{
\text{Novelty must be evaluated against what was available,
recoverable, representable, and reasonably generable at the relevant time,
not against what later became known.}
}
$$

對候選輸出 $x_i$，產生時間為 $t_0$，本文不直接問：

$$
Novel(x_i)?
$$

而是問：

$$
\boxed{
Novel(
x_i
\mid
K_{\le t_0},
A_{\le t_0},
T_{\le t_0},
B_{t_0},
Prov(x_i)
).
}
$$

其中：

- $K_{\le t_0}$：當時可取得的知識背景；
- $A_{\le t_0}$：當時可用的智能、計算與工具能力；
- $T_{\le t_0}$：當時存在的技術、制度與表示手段；
- $B_{t_0}$：同期合理基準，包括一般人、領域專家、前沿專家、制度、搜索系統、AI 或 human-AI system；
- $Prov(x_i)$：候選輸出的時間戳、版本、來源與證據鏈。

本文拒絕把新穎度壓縮成單一「語義距離」。至少應區分：

$$
\boxed{
\text{Lexical}
\neq
\text{Semantic}
\neq
\text{Combinatorial}
\neq
\text{Problem-Space}
\neq
\text{Representational}
\neq
\text{Program-Structural}
\neq
\text{Domain-Seed}
\neq
\text{Predictive Novelty}.
}
$$

相同詞彙可以承載不同結構；不同詞彙也可以實現相同 operator program。這使 TCFT-05 必須與 CODT 的 operator recovery、program topology 與 domain-seed 概念聯動，而不能只做文字查重。

本文進一步建立 **Priority–Novelty–Recognition Separation**：

$$
\boxed{
\text{Priority}
\neq
\text{Novelty}
\neq
\text{Recognition}
\neq
\text{Long-Term Value}.
}
$$

最早留下紀錄的人不一定具有最高認知異常；最早提出者可能受惠於私人資料、特殊工具或制度位置；後來的獨立重發現仍可能反映高度認知能力。另一方面，Sleeping Beauty 與 delayed recognition 文獻顯示，高新穎工作可能延後多年才取得影響；因此短期 citation、同行立即理解或後世聲望都不能直接作為新穎度代理。

本文提出 **Hindsight Leakage、Prior-Art Search Failure、Archive Blindness、Semantic Back-Projection、Tool Baseline Omission、Independent Rediscovery、Novelty Mirage** 等審查風險。特別是 2025–2026 年學術 novelty benchmark 已顯示 LLM 在新穎度判斷上仍可能與專家顯著偏離，甚至對模型生成研究問題產生系統性的 novelty mirage。因此：

$$
\boxed{
\text{LLM says novel}
\not\Rightarrow
\text{Novel}.
}
$$

AI 應主要被定位為 retrieval、decomposition、candidate matching、baseline generation 與 audit support，而非終局 novelty oracle。

本文最終提出 **Temporal Novelty Residual**：

$$
\boxed{
R_i^{TN}(t_0)
=
Structure(x_i)
-
BestRecoverableBaseline(
K_{\le t_0},
B_{t_0}
),
}
$$

其中減號表示結構殘差，而非要求所有知識都能純量相減。真正值得稱為「時代超前」的候選，不是今天看起來很酷，而是經過時間凍結、prior art、工具基準、版本完整性、獨立生成、失敗樣本與後見污染控制後，仍留下同期合理系統難以生成的結構。

本文中心命題為：

$$
\boxed{
\text{Historical novelty is a time-indexed residual,
not a retrospective impression.}
}
$$

**關鍵詞：** 時間正規化新穎度、Frozen-Time、prior art、同期基準、後見偏誤、學術新穎度、版本完整性、延遲理解、Sleeping Beauty、AI novelty assessment、TCFT

---

# Abstract

Claims that an idea was “ahead of its time” are highly vulnerable to hindsight, mythologization, incomplete archives, semantic projection, version contamination, and changes in available tools. A historical text that resembles a modern theory does not imply that its author possessed the same underlying structure; an idea that seems ordinary today may have been highly novel when produced; and later importance does not imply that the idea was non-obvious relative to contemporaneous knowledge.

This paper introduces **Time-Normalized Novelty (TNN)** and the **Frozen-Time Prior-Art Audit (FTPA)** within Temporal Cognitive Frontier Theory (TCFT). The central principle is:

$$
\boxed{
\text{Novelty must be evaluated against what was available,
recoverable, representable, and reasonably generable at the relevant time,
not against what later became known.}
}
$$

For a candidate output $x_i$ produced at time $t_0$, novelty is evaluated conditionally on the knowledge, tools, cognitive systems, institutional resources, contemporaneous baselines, and provenance available up to $t_0$.

The framework separates lexical, semantic, combinatorial, problem-space, representational, program-structural, domain-seed, and predictive novelty. It also establishes a Priority–Novelty–Recognition separation: being first, being non-obvious, being recognized, and becoming valuable are distinct temporal properties.

The paper identifies hindsight leakage, prior-art search failure, archive blindness, semantic back-projection, tool-baseline omission, independent rediscovery, and novelty mirage as major audit hazards. Recent benchmarks of LLM novelty assessment show substantial disagreement with human expert judgments, supporting the view that LLMs should assist novelty audit rather than serve as final novelty oracles.

Finally, we define a **Temporal Novelty Residual** as the structure remaining after subtracting the strongest recoverable contemporaneous baseline. Historical novelty is therefore treated as a time-indexed residual, not a retrospective impression.

**Keywords:** time-normalized novelty; frozen-time audit; prior art; contemporaneous baseline; hindsight bias; delayed recognition; scientific novelty; AI novelty assessment; TCFT

---

# 1. 導論：今天覺得新，和當時真的新，是兩件事

當我們讀一份舊文件，常見三種判斷：

> 這不就是今天的某某理論？

> 他居然那時候就知道？

> 這其實現在很普通。

三句都有可能錯。

因為今天的閱讀者已經知道：

$$
K_{2026}.
$$

但作者在：

$$
t_0
$$

只能取得：

$$
K_{\le t_0}.
$$

因此：

$$
\boxed{
Evaluation_{today}(x)
\neq
Evaluation_{at\ t_0}(x).
}
$$

---

# 2. Hindsight Leakage

如果研究者知道：

$$
Outcome_{future},
$$

再回頭評價：

$$
x_{t_0},
$$

就可能把未來資訊偷偷放入解釋。

本文稱：

$$
\boxed{
\text{Hindsight Leakage}.
}
$$

---

# 3. Impermissible Hindsight 的方法學類比

專利 prior-art / inventive-step 審查有一個非常有用的方法學精神：

> 評估某項發明是否 obvious，應站在 relevant date 與當時 skilled person 的知識位置，避免利用發明本身帶來的後見視角。

TCFT 不把學術新穎度等同專利法。

但借用：

$$
\boxed{
\text{Relevant-Date Evaluation}
}
$$

作為審查原則。

---

# 4. Frozen-Time Principle

對候選輸出：

$$
x_i
$$

產生於：

$$
t_0,
$$

允許的 audit information：

$$
\boxed{
K^{audit}
\subseteq
K_{\le t_0}.
}
$$

若某資料在：

$$
t_1>t_0
$$

才公開，

不能被 baseline agent 用來重建：

$$
x_i.
$$

---

# 5. Frozen-Time 不只是刪除日期較新的文章

真正的 Frozen-Time 至少要凍結：

- publications；
- patents；
- public datasets；
- software；
- hardware；
- search engines；
- AI models；
- terminology；
- institutional practices；
- known failures；
- available experiments；
- computing power；
- communication networks。

所以：

$$
\boxed{
FrozenTime
\neq
\text{Publication-Date Filter Only}.
}
$$

---

# 6. 時代可得性

某篇文獻：

$$
d
$$

即使在：

$$
t_0
$$

已存在，

也不代表所有人都可合理取得。

因此分：

$$
\boxed{
Existence(d,t_0)
}
$$

與：

$$
\boxed{
Accessibility(d,i,t_0).
}
$$

---

# 7. Publicly Available vs Privately Available

對 agent $i$：

$$
K_i(t_0)
=
K_{public}(t_0)
\cup
K_{private,i}(t_0).
$$

若候選者具有：

- proprietary data；
- classified information；
- laboratory access；
- insider position；

其 output 可能非常超出 public baseline，

但不一定代表同等程度的 reasoning anomaly。

---

# 8. Information Privilege Adjustment

因此：

$$
\boxed{
\text{Information Advantage}
\neq
\text{Reasoning Advantage}.
}
$$

TCFT 應盡可能將：

$$
K_{private}
$$

與：

$$
CognitiveGeneration
$$

分帳。

---

# 9. Tool Baseline

同樣：

$$
\boxed{
\text{Tool Advantage}
\neq
\text{Bare Cognitive Advantage}.
}
$$

但這不表示 tool-assisted output 沒價值。

它只是需要正確歸因。

---

# 10. 2026 Baseline 不等於 1990 Baseline

1990 的 researcher baseline 不包含：

- modern web search；
- modern LLM；
- modern arXiv；
- GitHub；
- contemporary databases；
- modern GPUs。

因此：

$$
B_{1990}
\neq
B_{2026}.
$$

---

# 11. Human-AI Baseline

進入 AI 時代後，

同期 baseline 應包含：

$$
\boxed{
B_t^{human+AI}.
}
$$

如果某種 cross-domain synthesis 已經是一般 LLM 容易生成，

那麼：

$$
\text{human+AI output}
$$

不能仍用 pre-AI 人類基準評分。

---

# 12. Contemporaneous Cognitive Baseline

定義：

$$
\boxed{
B_t
=
\{
B_t^{general},
B_t^{expert},
B_t^{frontier},
B_t^{institutional},
B_t^{tool},
B_t^{AI},
B_t^{human+AI}
\}.
}
$$

不是每個時代都存在所有項。

---

# 13. Baseline Reconstruction

真正問題是：

$$
\boxed{
\text{Given }K_{\le t_0},
\text{ what could a strong reasonable contemporaneous system generate?}
}
$$

不是：

> 平均人會不會想到？

---

# 14. Weak Baseline 會製造假異常

如果只拿：

$$
B_{general}
$$

比較前沿 scientist，

幾乎一定得到：

$$
Novelty\gg0.
$$

這沒有太大資訊。

所以：

$$
\boxed{
\text{Anomaly requires a strong baseline}.
}
$$

---

# 15. Candidate-Blind Baseline

baseline agents 不應先看：

$$
x_i
$$

再被問：

> 當時能不能想到？

否則：

$$
x_i
$$

本身會提供 search direction。

因此：

$$
\boxed{
\text{Candidate-Blind Baseline Generation}.
}
$$

---

# 16. Reconstruction Leakage

如果 baseline prompt 包含：

- 作者結論；
- 現代名稱；
- 後世用途；
- 後來驗證；

則已經污染。

本文稱：

$$
\boxed{
\text{Reconstruction Leakage}.
}
$$

---

# 17. Time-Normalized Novelty

對輸出 $x_i$：

$$
\boxed{
N_i^{TN}(t_0)
=
Novelty(
x_i
\mid
K_{\le t_0},
A_{\le t_0},
T_{\le t_0},
B_{t_0},
Prov(x_i)
).
}
$$

本文不宣稱現在已有唯一 estimator。

---

# 18. 新穎度不是一個維度

最少需要：

$$
\boxed{
\vec N_i^{TN}
=
(
N_{lex},
N_{sem},
N_{comb},
N_{prob},
N_{rep},
N_{prog},
N_{domain},
N_{pred}
).
}
$$

---

# 19. Lexical Novelty

$$
N_{lex}
$$

問：

> 是否出現新詞、新名稱、新符號？

這通常最容易測，

但理論意義可能最低。

---

# 20. Same Word 不等於 Same Concept

如果兩個作者都用：

$$
\text{domain},
$$

不代表：

$$
Concept_A=Concept_B.
$$

所以：

$$
\boxed{
\text{Lexical Match}
\not\Rightarrow
\text{Structural Match}.
}
$$

---

# 21. Different Word 不等於 Different Concept

反過來，

兩個時代可能用完全不同詞彙表示同一 operation。

因此：

$$
\boxed{
\text{Lexical Difference}
\not\Rightarrow
\text{Conceptual Novelty}.
}
$$

---

# 22. Semantic Novelty

$$
N_{sem}
$$

研究：

> 內容在 meaning space 是否遠離 prior corpus？

但 semantic distance 很容易：

- 被寫作風格影響；
- 把錯誤當新；
- 把跨語言當新；
- 把長文本的稀有組合當新。

---

# 23. Combinatorial Novelty

bibliometrics 已大量研究：

$$
\boxed{
\text{unusual / first-time combinations of prior knowledge}.
}
$$

例如：

- unusual citation combinations；
- first-time journal pairs；
- question-method combinations。

這是重要 prior art。

---

# 24. Combinatorial Novelty 的限制

但是：

$$
\boxed{
\text{New Combination}
\not\Rightarrow
\text{Deep Cognitive Advancement}.
}
$$

因為：

- unit of analysis 會影響結果；
- interdisciplinarity 與 novelty 可能重疊；
- random recombination 也可很新。

---

# 25. Problem-Space Novelty

TCFT-01 已提出：

$$
Q^*
\notin
\mathcal Q_{baseline,t}
$$

而：

$$
Q^*
\in
\mathcal Q_i(t).
$$

則可能存在：

$$
\boxed{
N_{prob}.
}
$$

也就是：

> 問題本身先於時代出現。

---

# 26. Research Question Novelty

2022 年已有研究直接以 research question × method 組合測量 scientific novelty。

2026 年 RQ-Bench 更直接把 research question 當 novelty judgment object。

因此 TCFT 不宣稱「研究問題新穎度」本身從未被研究。

---

# 27. TCFT 的額外要求

TCFT 進一步問：

$$
\boxed{
\text{Was the question generable by the strongest contemporaneous baseline?}
}
$$

以及：

$$
\boxed{
\text{Did this question expand the future/problem base-space?}
}
$$

---

# 28. Representational Novelty

$$
N_{rep}
$$

問：

> agent 是否建立新表示，使原本不可操作問題成為可操作？

例如：

- new coordinate；
- new diagram；
- new symbolic representation；
- new data structure；
- new state decomposition。

---

# 29. Representation vs Decoration

新圖畫、新符號、新命名不一定是：

$$
N_{rep}>0.
$$

必須有：

$$
\boxed{
\text{new operational affordance}.
}
$$

---

# 30. Program-Structural Novelty

依 CODT：

$$
Method
=
Program(
Operators,
Topology,
Context,
Policy,
Budget
).
$$

所以：

$$
N_{prog}
$$

問：

> 是否形成同期罕見或不存在的 operator program topology？

---

# 31. Program Novelty 不能靠文字查重

如果：

$$
TextSimilarity\approx0
$$

但：

$$
ProgramTopology_A
\cong
ProgramTopology_B,
$$

則深層新穎度可能低。

反之也成立。

---

# 32. Domain-Seed Novelty

CODT 的：

$$
Seed
\neq
Candidate
\neq
PromotedDomain.
$$

因此：

$$
N_{domain}
$$

只能表示：

> 是否較早形成後來可辨認的 domain-seed structure？

不能直接說：

> 他提前發明了一個完整認知域。

---

# 33. Predictive Novelty

$$
N_{pred}
$$

問：

> 是否提出同期 baseline 難生成的 future structure / prediction？

但 predictive novelty 仍需與：

$$
Accuracy
$$

分帳。

---

# 34. Novelty 不等於 Correctness

$$
\boxed{
Novel
\not\Rightarrow
True.
}
$$

一個完全錯誤的理論也可能非常新。

---

# 35. Correctness 不等於 Novelty

$$
\boxed{
True
\not\Rightarrow
Novel.
}
$$

重新證明一個已知命題可以正確但不新。

---

# 36. Novelty 不等於 Utility

$$
\boxed{
Novel
\not\Rightarrow
Useful.
}
$$

---

# 37. Utility 不等於 Novelty

某個舊方法：

$$
x
$$

可能在新場景極有用，

但：

$$
N(x)\approx0.
$$

---

# 38. Priority–Novelty–Recognition Separation

本文正式提出：

$$
\boxed{
\text{Priority}
\neq
\text{Novelty}
\neq
\text{Recognition}
\neq
\text{Long-Term Value}.
}
$$

---

# 39. Priority

$$
Priority(x)
$$

主要問：

> 誰最早留下可接受的發現／提出紀錄？

這是 credit 與 chronology 問題。

---

# 40. Multiple Discovery

科學史存在大量 simultaneous / multiple discovery。

因此：

$$
\boxed{
\text{First}
\not\Rightarrow
\text{Only Possible Generator}.
}
$$

若多人同時獨立生成相似 idea，

可能表示：

$$
\text{era was near a discovery threshold}.
$$

---

# 41. Independent Rediscovery

一個較晚作者：

$$
j
$$

若沒有取得較早作者：

$$
i
$$

的成果，

仍獨立生成同一結構，

則：

$$
\boxed{
\text{priority}_j=0
}
$$

但：

$$
\boxed{
\text{cognitive evidence}_j>0.
}
$$

所以 TCFT 不能只用 first-winner-takes-all。

---

# 42. Priority Rule 與 TCFT

science priority rule 主要分配 credit。

TCFT 主要測：

$$
\boxed{
\text{time-relative cognitive residual}.
}
$$

兩者目的不同。

---

# 43. Recognition

$$
Rec_t(x)
$$

表示：

> 時代多大程度理解、引用、採納或重視 $x$？

這可以和 novelty 完全不同步。

---

# 44. Sleeping Beauty

Sleeping Beauty 文獻顯示：

$$
\boxed{
Rec_{t_0}(x)\ll Rec_{t_1}(x)
}
$$

可以在大量科學文獻中發生。

所以：

$$
\boxed{
\text{Low Early Recognition}
\not\Rightarrow
\text{Low Novelty or Low Long-Term Value}.
}
$$

---

# 45. Delayed Recognition of Novel Work

研究也顯示 novel / disruptive papers 可能有較明顯 delayed recognition。

因此短 citation window 對 novelty 可能產生偏誤。

---

# 46. 與延遲理解論的接口

既有延遲理解論定義：

$$
V_t(x)
=
V(
x
\mid
\mathcal K_t,
\mathcal A_t,
\mathcal Q_t,
\mathcal I_t
).
$$

同一 knowledge fragment：

$$
V_{t_0}(x)
\ll
V_{t_1}(x)
$$

可能成立。

---

# 47. Novelty 與 Value 的時間動力不同

Historical novelty：

$$
N^{hist}_{t_0}(x)
$$

是：

> 相對 $t_0$ baseline 有多新？

後續 value：

$$
V_{t_1}(x)
$$

則可改變。

所以：

$$
\boxed{
\text{Historical Novelty}
\neq
\text{Current Value}.
}
$$

---

# 48. Current Novelty

到了：

$$
t_1,
$$

如果整個時代已吸收：

$$
x,
$$

則：

$$
N^{current}_{t_1}(x)
\approx0
$$

可能成立。

但：

$$
N^{hist}_{t_0}(x)
$$

不因此消失。

---

# 49. Temporal Lead

如果結構 $s$ 由 agent $i$ 在：

$$
t_i
$$

產生，

baseline 在：

$$
t_B
$$

才廣泛可生成，

則：

$$
\boxed{
\Delta T_i(s)
=
t_B-t_i.
}
$$

---

# 50. Lead Time 不等於 Novelty

如果：

$$
s
$$

在更早 prior art 已存在，

但沒被研究者找到，

則：

$$
\Delta T
$$

可能是假象。

所以先做：

$$
\boxed{
PriorArtAudit.
}
$$

---

# 51. Prior Art 的工作定義

TCFT 使用 prior art 作廣義方法學詞，

不只指專利法。

它包括：

- papers；
- books；
- patents；
- software；
- talks；
- archived webpages；
- datasets；
- public code；
- standards；
- known practices；
- documented historical sources。

---

# 52. Prior-Art Search Failure

若 audit 沒找到：

$$
d^*,
$$

不能推出：

$$
d^*
\text{ 不存在}.
$$

因此：

$$
\boxed{
\text{Not Retrieved}
\neq
\text{Nonexistent}.
}
$$

---

# 53. Retrieval Confidence

每個 novelty judgment 應帶：

$$
\boxed{
Conf_{retrieval}.
}
$$

資料庫越完整、語言越多、時間越久遠，

uncertainty 不同。

---

# 54. Archive Blindness

歷史材料可能：

- 未數位化；
- 遺失；
- 私藏；
- 被毀；
- 語言不通；
- metadata 錯；
- OCR 錯；
- 搜尋引擎未索引。

本文稱：

$$
\boxed{
\text{Archive Blindness}.
}
$$

---

# 55. False Novelty from Archive Blindness

如果：

$$
PriorArtExists=1
$$

但：

$$
RetrievedPriorArt=0,
$$

會造成：

$$
\boxed{
\text{False Novelty}.
}
$$

---

# 56. Search-Language Dependence

同一 idea：

$$
x
$$

在：

- English；
- German；
- Japanese；
- Chinese；
- Russian；

可能使用完全不同關鍵詞。

因此：

$$
\boxed{
\text{Monolingual Prior-Art Search}
}
$$

在歷史研究中可能嚴重不足。

---

# 57. Semantic Back-Projection

如果今天已有概念：

$$
C_{2026},
$$

研究者去舊文本找：

> 哪句話像 $C_{2026}$？

容易產生：

$$
\boxed{
\text{Semantic Back-Projection}.
}
$$

---

# 58. Back-Projection Failure

一句：

> 機器會思考。

不能因為今天有 LLM 就直接解釋成：

$$
\text{modern transformer cognition theory}.
$$

需要保留當時上下文。

---

# 59. Structural Matching

更好的審查不是只比：

$$
Words.
$$

而是比較：

$$
\boxed{
Objects,
Relations,
Operations,
Constraints,
Predictions,
FailureConditions.
}
$$

---

# 60. Concept Graph

可把候選輸出：

$$
x
$$

抽成：

$$
\boxed{
G_x
=
(V_x,E_x,\Lambda_x).
}
$$

其中：

- $V$：concepts / objects；
- $E$：relations；
- $\Lambda$：typed roles / constraints。

---

# 61. Program Graph

若是方法論：

$$
\boxed{
P_x
=
(Operators,Edges,Control,Context,Stop).
}
$$

再和 prior art 比較：

$$
P_x
\sim
P_{prior}.
$$

---

# 62. Partial Anticipation

歷史作者可能只提前一部分：

$$
S_{modern}
=
\{s_1,s_2,s_3,s_4\}.
$$

舊稿只包含：

$$
\{s_1,s_2\}.
$$

不應判：

$$
\boxed{
\text{Full Theory Anticipated}.
}
$$

---

# 63. Anticipation Coverage

可候選定義：

$$
\boxed{
ACov(x,S)
=
\frac{
|Structure(x)\cap S|
}{
|S|
}.
}
$$

但實際需處理非集合結構與權重。

---

# 64. Structural Precision

還要防止：

> 一句模糊話可以被對應十個現代理論。

因此需要：

$$
\boxed{
Precision_{struct}.
}
$$

即：

> 候選文本究竟具體到什麼程度？

---

# 65. Specificity Penalty

若文本：

$$
x
$$

過度模糊，

可以讓：

$$
Match(x,S_1),
Match(x,S_2),\ldots
$$

都很高。

應加入：

$$
\boxed{
C_{ambiguity}.
}
$$

---

# 66. Version Integrity

若文件在：

$$
t_0
$$

建立，

但：

$$
t_1
$$

修改，

不能把：

$$
t_1
$$

內容全部歸到：

$$
t_0.
$$

---

# 67. Earliest Verifiable Version

定義：

$$
\boxed{
t_{EV}(x)
}
$$

為某一 claim / structure 最早可驗證版本時間。

不是：

$$
\text{file creation time}.
$$

---

# 68. File Timestamp 不等於 Claim Timestamp

一份舊檔：

$$
D
$$

在 2020 建立，

2026 加入新段落。

則新段落不能宣稱：

$$
t=2020.
$$

---

# 69. Claim-Level Versioning

理想 audit 應追蹤：

$$
\boxed{
ClaimID
\rightarrow
FirstAppearance
\rightarrow
Revisions
\rightarrow
CurrentForm.
}
$$

---

# 70. Provenance Integrity

對候選 $x$：

$$
\boxed{
Prov(x)
=
(
Source,
Time,
Version,
Author,
RevisionChain,
Archive,
Hash
).
}
$$

越完整，

novelty confidence 越高。

---

# 71. Timestamp Confidence

定義：

$$
\boxed{
Conf_t(x)
\in[0,1].
}
$$

不是時間越早分越高，

而是：

> 這個時間到底有多可信？

---

# 72. Integrity Gate

若：

$$
Conf_t(x)<\theta,
$$

則：

$$
\boxed{
HistoricalNoveltyStatus
=
Unresolved.
}
$$

而不是硬算高分。

---

# 73. Failure Archive

真正審查一個「超前者」時，

不能只保存：

$$
Successes.
$$

還需要：

$$
\boxed{
Failures,
AbandonedIdeas,
WrongPredictions,
DeadEnds.
}
$$

---

# 74. Selection Bias

如果後世只挑：

$$
10
$$

個命中的想法，

但作者總共寫：

$$
10000
$$

個候選，

則異常可能被嚴重高估。

---

# 75. Output Volume Adjustment

因此：

$$
\boxed{
\text{Novel Hits}
}
$$

需要對：

$$
\text{Total Opportunity to Produce Hits}
$$

做調整。

---

# 76. Lottery Effect

大量生成者可能：

$$
N_{output}\gg1.
$$

即使單次命中率普通，

也會產生幾個驚人案例。

這可以稱：

$$
\boxed{
\text{Cognitive Lottery Effect}.
}
$$

---

# 77. Volume 不應直接懲罰

大量產出本身也可能是一種能力。

所以：

$$
\boxed{
VolumeAdjustment
\neq
VolumePenalty.
}
$$

重點是避免只挑 winners。

---

# 78. Independent Rediscovery Test

若作者聲稱：

$$
x
$$

是獨立產生，

可以檢查：

- citation history；
- browsing history if available；
- file chronology；
- prior drafts；
- conversation logs；
- dependency graph。

但不能要求私人資料才承認 novelty。

---

# 79. Independence Confidence

可保存：

$$
\boxed{
Conf_{ind}(x).
}
$$

表示：

> 目前有多少證據支持獨立生成？

---

# 80. Independent 不等於 Novel

即使完全獨立，

如果：

$$
x
$$

在同期極容易重發現，

則：

$$
N^{TN}
$$

可能仍普通。

---

# 81. Convergent Discovery

多個人同時獨立找到：

$$
x
$$

可能表示：

$$
\boxed{
\text{low remaining discovery distance}.
}
$$

而不是每個人都具有極端異常。

---

# 82. Discovery Distance

候選：

$$
\boxed{
D_{disc}(x,t)
}
$$

表示：

> 在同期知識與工具下，從可用結構走到 $x$ 的生成距離。

這不是物理距離，也不是已完成 metric。

---

# 83. Obviousness Analogy

若：

$$
D_{disc}
$$

很小，

同期強 baseline 很容易生成：

$$
x,
$$

則 novelty 應較低。

這與 patent inventive-step 的「person skilled in the art」有方法學類比。

---

# 84. 但 TCFT 不做法律判定

$$
\boxed{
\text{TCFT Novelty}
\neq
\text{Patent Novelty}
\neq
\text{Inventive Step}.
}
$$

它們可互相借鑑，

不可互相替代。

---

# 85. Novelty Mirage

2025–2026 年研究已顯示：

LLM 可以產生看起來合理的新穎度理由，

但 novelty judgments 與 human experts 顯著不一致。

RQ-Bench 更觀察到：

$$
\boxed{
\text{Novelty Mirage}.
}
$$

模型偏好模型生成問題，

專家卻偏好 author-anchored reference questions。

---

# 86. LLM-as-Judge 的限制

因此：

$$
\boxed{
Judge_{LLM}(x)=Novel
}
$$

不能作終局證據。

---

# 87. LLM 的合理角色

AI 可以很好地支援：

- corpus retrieval；
- multilingual query expansion；
- claim decomposition；
- semantic clustering；
- structural matching；
- baseline generation；
- contradiction search；
- citation graph traversal；
- version diff。

---

# 88. Human Expert 也不是絕對 Oracle

專家會有：

- field bias；
- familiarity bias；
- status bias；
- school bias；
- hindsight bias。

所以：

$$
\boxed{
HumanExpert
\neq
PerfectNoveltyOracle.
}
$$

---

# 89. Plural Novelty Audit

理想：

$$
\boxed{
AI Retrieval
+
AI Structural Analysis
+
Expert Review
+
Independent Baselines
+
Archive Evidence.
}
$$

---

# 90. Novelty Confidence

輸出不只：

$$
Novel / NotNovel.
$$

而應：

$$
\boxed{
(
NoveltyVector,
Confidence,
KnownPriorArt,
UnresolvedRisks
).
}
$$

---

# 91. Prior-Art Match Classes

可以分：

$$
\boxed{
M_0:
NoRelevantMatchFound
}
$$

$$
\boxed{
M_1:
LexicalOverlap
}
$$

$$
\boxed{
M_2:
ConceptualOverlap
}
$$

$$
\boxed{
M_3:
StructuralPartialMatch
}
$$

$$
\boxed{
M_4:
StructuralNearMatch
}
$$

$$
\boxed{
M_5:
SubstantivePriorArt
}
$$

這只是 audit schema candidate。

---

# 92. No Match Found 的語義

$$
M_0
$$

必須解讀為：

> 在目前搜尋範圍與資料庫中沒有找到。

不是：

> 世界上從未存在。

---

# 93. Time-Normalized Residual

最後對：

$$
x_i
$$

建立：

$$
\boxed{
R_i^{TN}(t_0)
=
Structure(x_i)
-
BestRecoverableBaseline(
K_{\le t_0},
B_{t_0}
).
}
$$

---

# 94. Residual 不是純量減法

這個：

$$
-
$$

表示：

- remove known prior components；
- discount obvious combinations；
- remove tool-explained gains；
- remove information privilege；
- account for ambiguous matches。

剩下：

$$
\boxed{
\text{unexplained structural novelty}.
}
$$

---

# 95. Time-Normalized Novelty Vector

可以候選寫：

$$
\boxed{
\vec N_i^{TN}(t_0)
=
(
N_{prob},
N_{rep},
N_{prog},
N_{domain},
N_{pred},
Conf_t,
Conf_{retrieval},
Conf_{ind}
).
}
$$

---

# 96. Ex Ante Novelty

只使用：

$$
K_{\le t_0}
$$

與同期 baseline：

$$
\boxed{
N_i^{pre}(t_0).
}
$$

---

# 97. Ex Post Value

後來才評：

$$
\boxed{
V_i^{post}(t_0,t_1).
}
$$

兩者必須分帳。

---

# 98. 高新穎低價值

可能：

$$
N^{pre}\gg0
$$

但：

$$
V^{post}\approx0.
$$

這是新但沒用。

---

# 99. 低新穎高價值

也可能：

$$
N^{pre}\approx0
$$

但：

$$
V^{post}\gg0.
$$

例如把成熟方法大規模工程化。

---

# 100. 高新穎高價值

TCFT 真正特別關心：

$$
\boxed{
N^{pre}\gg0
\quad
\land
\quad
V^{post}\gg0.
}
$$

但不能用後者反推前者。

---

# 101. Delayed Understanding

如果：

$$
N^{pre}\gg0
$$

但同期：

$$
Recognition\approx0,
$$

之後：

$$
V^{post}\uparrow,
$$

就與延遲理解／Sleeping Beauty 現象相接。

---

# 102. Recognition Lag

定義：

$$
\boxed{
L_{rec}
=
t_{recognition}
-
t_{production}.
}
$$

---

# 103. Understanding Lag

$$
\boxed{
L_{understand}
=
t_{understanding}
-
t_{production}.
}
$$

---

# 104. Validation Lag

$$
\boxed{
L_{verify}
=
t_{verification}
-
t_{production}.
}
$$

三者不一定相同。

---

# 105. Temporal Signature

一項知識可以有：

$$
\boxed{
\Sigma_t(x)
=
(
t_{produce},
t_{recognize},
t_{understand},
t_{verify},
t_{apply}
).
}
$$

這比單一 publication date 更完整。

---

# 106. Historical Cognitive Advancement

如果：

$$
R_i^{TN}(t_0)\gg0,
$$

才有資格進一步說：

$$
\boxed{
\text{historically unusual cognitive output}.
}
$$

仍然不等於身份判定。

---

# 107. 「未來人」的 Novelty Audit

對自稱未來人：

第一步不是：

> 預言準不準？

而是：

$$
\boxed{
\text{其知識結構是否超過同期 prior art 與 baseline？}
}
$$

---

# 108. Future Vocabulary Test

如果自稱來自 2060，

卻所有：

- technology；
- institution；
- conflict；
- social structure；

都只是：

$$
Extend(
PopularIdeas_{t_0}
),
$$

則：

$$
N^{TN}
$$

可能很低。

---

# 109. Unexpected Constraint Test

真正有意思的往往不是科幻名詞，

而是：

> 他是否知道同期人不知道應該注意的限制？

例如：

- unexpected bottleneck；
- new failure mode；
- new governance problem；
- new engineering tradeoff。

---

# 110. Problem-Ahead Test

若：

$$
Q^*
\notin
\mathcal Q_{baseline,t_0}
$$

而候選者提出：

$$
Q^*,
$$

且後來：

$$
Q^*
$$

成為重要問題，

則：

$$
\boxed{
ProblemSpaceNovelty
}
$$

可能很高。

---

# 111. Historical Figure Audit

對 Leonardo、Turing 或任何歷史人物，

不能：

> 用現代詞彙找相似句。

而要：

$$
\boxed{
\text{Frozen corpus}
+
\text{contemporaneous baseline}
+
\text{structural reconstruction}
+
\text{failure archive}.
}
$$

---

# 112. Modern Author Audit

現代作者也必須接受：

$$
B_{2026}^{human+AI}.
$$

不能拿 AI 時代成果去和：

$$
B_{preAI}
$$

比較。

---

# 113. AI Author Audit

AI 自己則比較：

$$
B_t^{AI-frontier}.
$$

不是和普通人類 baseline 比。

---

# 114. Human-AI Coupled Audit

若 output：

$$
x_{H+AI},
$$

其 novelty attribution 應分：

$$
\boxed{
SystemNovelty
}
$$

與：

$$
\boxed{
IndividualContribution.
}
$$

後者可能無法完全分解。

---

# 115. System-Level Novelty

對耦合系統：

$$
\boxed{
N_{H+AI}^{TN}
}
$$

本身可以是合法研究對象。

不一定要強迫所有 credit 回到單一主體。

---

# 116. Frozen-Time Audit Protocol

本文提出最小流程：

$$
\boxed{
\begin{aligned}
&1.\ TimestampFreeze\\
&2.\ VersionIntegrity\\
&3.\ ClaimDecomposition\\
&4.\ PriorArtRetrieval\\
&5.\ ContemporaneousBaseline\\
&6.\ CandidateBlindGeneration\\
&7.\ StructuralMatching\\
&8.\ HindsightControl\\
&9.\ FailureArchive\\
&10.\ NoveltyResidual\\
&11.\ ExPostValueSeparate.
\end{aligned}
}
$$

---

# 117. Step 1：Timestamp Freeze

固定：

$$
t_0=t_{EV}(x).
$$

---

# 118. Step 2：Version Integrity

確認：

- earliest version；
- edits；
- revisions；
- hashes；
- archives。

---

# 119. Step 3：Claim Decomposition

將大 claim：

$$
X
$$

拆成：

$$
x_1,\ldots,x_n.
$$

避免：

> 一篇 100 頁文章只要有一段很新，整篇都 10/10。

---

# 120. Step 4：Prior-Art Retrieval

多語言、多資料源搜尋：

$$
\boxed{
\mathcal P_{\le t_0}.
}
$$

---

# 121. Step 5：Baseline Reconstruction

建立：

$$
B_{t_0}.
$$

---

# 122. Step 6：Candidate-Blind Generation

baseline 不看候選答案，

先自己生成：

- questions；
- models；
- predictions；
- methods。

---

# 123. Step 7：Structural Matching

比：

- concepts；
- relations；
- operators；
- topology；
- constraints；
- predictions。

---

# 124. Step 8：Hindsight Control

刪除：

$$
K_{>t_0}
$$

與 modern labels。

---

# 125. Step 9：Failure Archive

納入：

$$
\boxed{
\text{all recoverable misses, not only hits}.
}
$$

---

# 126. Step 10：Novelty Residual

產生：

$$
\boxed{
R_i^{TN}(t_0).
}
$$

---

# 127. Step 11：Ex Post Value

最後才加入：

$$
V^{post}.
$$

不能反向污染 novelty。

---

# 128. Evidence Grade

可以使用：

$$
\boxed{
A,B,C,D,E
}
$$

表示 audit strength。

例如：

### A

- immutable timestamp；
- broad prior-art search；
- strong baseline；
- clear structural residual；
- low hindsight risk。

### E

- anecdotal recollection；
- no archive；
- post-hoc paraphrase；
- unknown edits。

---

# 129. Grade 不是 Novelty Score

$$
\boxed{
EvidenceGrade
\neq
NoveltyMagnitude.
}
$$

A 級可以證明「普通」。

E 級也不能證明「很新」。

---

# 130. Confidence Intervals

如果 novelty estimate：

$$
\hat N,
$$

最好保存：

$$
\boxed{
[\hat N_L,\hat N_U].
}
$$

尤其 historical archive 不完整時。

---

# 131. Unresolved Novelty

如果資料不足，

合理結果是：

$$
\boxed{
Status=Unresolved.
}
$$

不是強迫：

$$
Novel / NotNovel.
$$

---

# 132. Dynamic Audit

新 prior art 被數位化：

$$
\mathcal P_{t+1}
\supset
\mathcal P_t.
$$

則：

$$
\boxed{
N_i^{TN}(t+1)
}
$$

可以下降。

---

# 133. 新資料也可能讓分數上升

如果找到更早版本證明：

$$
t_{EV}
$$

比原先更早，

則 historical novelty 可能上升。

因此：

$$
\boxed{
\text{Novelty Audit Is Revisable}.
}
$$

---

# 134. No Permanent Novelty Verdict

TCFT 不宣稱：

$$
\boxed{
N_i=\text{eternal constant}.
}
$$

真正永久保存的是：

- audit state；
- evidence；
- version；
- baseline；
- result date。

---

# 135. 與 TCFT-06 的接口

Paper 05 得到：

$$
\vec N_i^{TN}(t).
$$

Paper 06 將加入：

- future-space；
- counterfactual；
- reflexive；
- strategy；
- program；
- persistence；

建立：

$$
\boxed{
\text{Dynamic Cognitive Anomaly Frontier}.
}
$$

---

# 136. 可反證命題

## H1：Frozen-Time Evaluation 與 Retrospective Evaluation 顯著不同

若控制後見資訊後，novelty judgment 幾乎不變，Frozen-Time 的額外複雜度可能有限。

## H2：Strong Baseline 會降低假異常

如果增加 expert / frontier / AI baseline 不會使任何候選 novelty estimate 下降，表示 baseline protocol 可能失效。

## H3：Structural Novelty 提供超越 Semantic Novelty 的增益

若 program / graph matching 完全不能改善 human expert agreement，結構審查應降級。

## H4：Version Integrity 顯著改變 Historical Novelty

若 claim-level versioning 對結果毫無影響，版本追蹤可簡化。

## H5：Failure Archive 能校正 Heroic Selection Bias

若加入 misses 後，候選異常度完全不變，volume/selection correction 的必要性降低。

## H6：Plural Audit 優於 Single LLM Judge

若單一 LLM novelty judge 能穩定超越 plural audit，本文對 novelty oracle 的保守立場需修正。

---

# 137. 實驗一：Hindsight Ablation

Condition A：

$$
K_{\le t_0}.
$$

Condition B：

$$
K_{\le t_1}.
$$

比較同一 historical output 的 novelty judgment。

---

# 138. 實驗二：Baseline Strength Ladder

依序加入：

$$
B_{general}
\rightarrow
B_{expert}
\rightarrow
B_{frontier}
\rightarrow
B_{AI}
\rightarrow
B_{human+AI}.
$$

看 residual 如何收縮。

---

# 139. 實驗三：Lexical vs Structural Prior Art

比較：

- keyword search；
- embeddings；
- concept graph；
- operator-program matching。

測 human-expert agreement。

---

# 140. 實驗四：Version Contamination

建立故意含後續修改的 document history。

測 audit 是否能正確把 claim 歸到：

$$
t_{first}.
$$

---

# 141. 實驗五：Independent Rediscovery

給兩個隔離 groups 相同 Frozen-Time corpus，

測是否獨立收斂到：

$$
x.
$$

若非常容易收斂，

則：

$$
D_{disc}
$$

可能低。

---

# 142. 實驗六：Novelty Mirage

讓：

- LLM judge；
- expert judge；
- retrieval-grounded LLM；
- plural panel；

評同一 research ideas。

比較 false positive novelty。

---

# 143. 實驗七：Historical Archive Expansion

先用 digitized corpus audit。

再加入：

- books；
- patents；
- non-English archives。

看 novelty residual 是否改變。

---

# 144. 實驗八：Failure Archive Correction

對高產作者：

先只看 hits。

再加入全部 outputs。

比較 anomaly estimate。

---

# 145. 實驗九：Tool Baseline

讓 baseline：

- no tools；
- search；
- LLM；
- LLM+search；

重建同一 target。

看現代「新穎」有多少其實可由工具解釋。

---

# 146. 實驗十：Delayed Recognition

比較：

$$
N^{pre}
$$

與：

$$
RecognitionLag,
Value^{post}.
$$

檢查高新穎是否真的較常延遲理解／認可。

---

# 147. 侷限

第一，完整 prior art 幾乎不可達，因此 TNN 永遠帶 retrieval uncertainty。

第二，跨語言與未數位化 archive 會系統性偏誤 novelty。

第三，structural matching 本身依賴 ontology 與 decomposition。

第四，baseline generation 會受模型能力與 prompt 影響。

第五，私人知識與未公開資料常無法完整重建。

第六，priority 與 discovery attribution 本身存在社會／歷史詮釋問題。

第七，後見控制無法完全消除研究者已知未來造成的認知污染。

第八，novelty 與 interdisciplinarity、complexity、ambiguity 可能混淆。

第九，AI novelty judge 目前仍不能視為可靠 oracle。

第十，TNN 高不等於真、好、有用、道德或應獲權威。

---

# 148. 結論

「超前」不是：

> 今天看起來像未來。

而是：

$$
\boxed{
\text{在當時的知識、工具、表示與強基準下，
仍難以正常生成。}
}
$$

因此 TCFT-05 將 historical novelty 從印象改寫成：

$$
\boxed{
\text{time-indexed residual}.
}
$$

真正審查需要：

$$
\boxed{
\text{Timestamp}
+
\text{Version}
+
\text{PriorArt}
+
\text{Baseline}
+
\text{Structure}
+
\text{FailureArchive}
+
\text{HindsightControl}.
}
$$

而且：

$$
\boxed{
\text{Priority}
\neq
\text{Novelty}
\neq
\text{Recognition}
\neq
\text{Long-Term Value}.
}
$$

最早的人不一定最異常。

最異常的人不一定最早被理解。

最早被理解的人也不一定最有長期價值。

甚至一個今天看起來普通的結構，

在它產生的那一刻可能位於極端尾部。

反過來，一個今天看起來「神奇」的舊文本，

在嚴格 Frozen-Time prior-art audit 後，也可能只是：

$$
\boxed{
\text{a normal extrapolation from its own era}.
}
$$

因此：

$$
\boxed{
R_i^{TN}(t_0)
=
Structure(x_i)
-
BestRecoverableBaseline(
K_{\le t_0},
B_{t_0}
)
}
$$

才是 TCFT 真正要保存的東西。

如果 residual 很小，

就接受：

> 沒那麼異常。

如果 residual 很大，

也只先說：

> 在目前證據下，存在難由同期合理基準吸收的結構。

不需要立刻建立英雄神話。

更不需要建立特殊身份。

下一篇 TCFT-06 才會把這些不同維度放進動態前沿：

$$
\boxed{
\text{Historical Anomaly}
\neq
\text{Current Anomaly}
\neq
\text{Persistent Frontier}.
}
$$

也就是：

> 一個人當年到底有多超前？

> 今天還剩多少超前？

> 世界追了幾十年、幾百年後，還有什麼沒有追上？

這將是動態認知異常前沿的正式問題。

---

# References

1. Uzzi, B., Mukherjee, S., Stringer, M., & Jones, B. (2013). Atypical combinations and scientific impact. *Science*, 342(6157), 468–472. DOI: 10.1126/science.1240474.
2. Wang, J., Veugelers, R., & Stephan, P. (2017). Bias against novelty in science: A cautionary tale for users of bibliometric indicators. *Research Policy*, 46(8), 1416–1436. DOI: 10.1016/j.respol.2017.06.006.
3. Leahey, E., Beckman, C. M., & Stanko, T. L. (2017). Prominent but Less Productive: The Impact of Interdisciplinarity on Scientists’ Research. *Administrative Science Quarterly*, 62(1), 105–139.
4. Boudreau, K. J., Guinan, E. C., Lakhani, K. R., & Riedl, C. (2016). Looking Across and Looking Beyond the Knowledge Frontier: Intellectual Distance, Novelty, and Resource Allocation in Science. *Management Science*, 62(10), 2765–2783.
5. Sun, Y., & Linton, J. D. (2022). Combination of research questions and methods: A new measurement of scientific novelty. *Journal of Informetrics*, 16(2), 101282. DOI: 10.1016/j.joi.2022.101282.
6. Ke, Q., Ferrara, E., Radicchi, F., & Flammini, A. (2015). Defining and identifying Sleeping Beauties in science. *Proceedings of the National Academy of Sciences*, 112(24), 7426–7431.
7. Merton, R. K. (1957). Priorities in scientific discovery: A chapter in the sociology of science. *American Sociological Review*, 22(6), 635–659.
8. Gross, A. G. (1998). Do disputes over priority tell us anything about science? *Science in Context*, 11(2), 161–179.
9. Lin, E., Peng, Z., & Fang, Y. (2025). Evaluating and Enhancing Large Language Models for Novelty Assessment in Scholarly Publications. *Proceedings of the 1st Workshop on AI and Scientific Discovery*, 46–57. DOI: 10.18653/v1/2025.aisd-main.5.
10. Schopf, T., & Färber, M. (2026). Is This Idea Novel? An Automated Benchmark for Judgment of Research Ideas. *LREC 2026*, 4716–4727. DOI: 10.63317/4c3gy3f7epnj.
11. Wu, W., Zhao, Y., Wang, Y., Li, S., Shao, J., Long, Y., & Zhang, C. (2026). NovBench: Evaluating Large Language Models on Academic Paper Novelty Assessment. *Findings of ACL 2026*, 32103–32133. DOI: 10.18653/v1/2026.findings-acl.1607.
12. Sinhahajari, S., Majumder, N., & Poria, S. (2026). On the Limits of LLM-as-Judge for Scientific Novelty Assessment. arXiv:2606.12071.
13. World Intellectual Property Organization. *PCT International Search and Preliminary Examination Guidelines*, Chapters 11–13.
14. Neo.K. (2026). *延遲理解論：知識價值的時間依賴與未來重估*. EveMissLab.
15. Neo.K. (2026). *跨時間敘述觀測站技術白皮書*. EveMissLab.
16. Neo.K. (2026). *Cognitive Operator-Domain Theory (CODT) Series 01–10*. EveMissLab.
17. Neo.K. (2026). *TCFT-00 至 TCFT-04*. EveMissLab.

---

# Canonical Note

本文件正式原始碼使用 UTF-8。

數學原始碼只使用 canonical delimiters：

- inline math：` $...$ `
- display math：`$$...$$`

不進行 unicode_escape 類 round-trip；不把 LaTeX 轉為 Unicode 數學字元後再作 canonical source；不以聊天 rendering view 作為正式原稿。
