---
title: "TCFT-01｜未來底空間選擇：想像力、候選世界與問題先行"
title_en: "Future Base-Space Selection: Imagination, Candidate Worlds, and Problem-First Foresight"
series: "Temporal Cognitive Frontier Theory (TCFT) / 時代認知前沿理論"
paper_no: "01"
version: "v0.1"
date: "2026-08-30"
author: "Neo.K"
affiliation: "EveMissLab / 一言諾科技有限公司"
document_type: "理論論文 / Future Base-Space 篇"
language: "zh-Hant"
status: "正式系列初稿"
previous_paper: "TCFT-00｜超前認知不是預言：時代認知前沿的問題設定"
---

# TCFT-01｜未來底空間選擇：想像力、候選世界與問題先行

## Future Base-Space Selection: Imagination, Candidate Worlds, and Problem-First Foresight

**系列：** Temporal Cognitive Frontier Theory, TCFT / 時代認知前沿理論  
**篇次：** 01  
**版本：** v0.1  
**日期：** 2026-08-30  
**作者：** Neo.K  
**機構脈絡：** EveMissLab / 一言諾科技有限公司  

---

## 摘要

預測研究通常把候選結果空間視為已知背景：研究者先定義事件、狀態或答案集合，再要求預測者配置機率、排序可能性或判斷未來路徑。然而，在開放世界、長時間尺度、科技演化、制度變遷、AI 發展與高度創新問題中，真正困難的部分往往發生在機率估計之前：**哪些未來被放入候選空間，哪些問題被允許成為問題，哪些表示足以使尚未成形的未來被認知系統操作？**

本文提出 **Future Base-Space（未來底空間）** 作為 Temporal Cognitive Frontier Theory（TCFT）的第一個核心結構。本文使用「底空間」並非直接借用拓撲學或纖維叢中的 standard base space 定義，而是指：在特定時間、資訊、語言、工具、資源與認知程序條件下，一個 agent / cognitive system 用來生成、表示、比較與更新候選未來的前機率認知支撐結構。

對主體 $i$，時間 $t$ 的最小未來底空間候選寫為：

$$
\boxed{
\mathfrak B_i(t)
=
(
\Omega_i(t),
\mathcal Q_i(t),
\mathcal R_i(t),
\Gamma_i(t),
\mathcal U_i(t)
)
}
$$

其中：

- $\Omega_i(t)$：可表示之候選未來狀態／路徑集合；
- $\mathcal Q_i(t)$：可被提出的未來問題集合；
- $\mathcal R_i(t)$：可用表示系統；
- $\Gamma_i(t)$：當前知識、約束、工具、制度與資源條件；
- $\mathcal U_i(t)$：對尚未納入、尚未命名或尚未可表示之未知區域所保留的接口。

本文提出 **Space-Before-Probability Principle**：

$$
\boxed{
\text{Before assigning probability to a future,
the future must first be representable within a candidate support.}
}
$$

若真實未來 $W^*$ 不在 agent 的候選支撐中：

$$
W^*
\notin
\Omega_i(t),
$$

則此失敗不能只被描述為「機率估錯」。它是一種更前置的 **Base-Space Omission / Support Failure**。在此情況下，即使 agent 在既有候選集合內具有完美 calibration，也無法對根本未被表示的未來進行正確分配。

本文進一步區分：

$$
\boxed{
\text{Base-Space Selection}
\neq
\text{Base-Space Generation}
\neq
\text{Base-Space Revision}.
}
$$

Selection 從既有候選池中選擇；Generation 產生原本不存在的候選區域；Revision 則在新資料、失敗、反例或世界變化後修改支撐本身。本文亦引入 **Unknown Reserve**，拒絕把「尚未想到」偷偷等同於零機率，並把 open-set / open-world recognition 中「訓練時無法窮舉所有類別」的問題視為結構類比，而非直接等同 TCFT 的未來底空間。

本文最後提出，時代認知超前的一種重要形式不是「在共同的未來集合上給出更好的機率」，而是：

$$
\boxed{
\Omega_j(t)
\subsetneq
\Omega_i(t)
}
$$

且新增區域包含後來取得高價值的未來結構：

$$
W^*
\in
\Omega_i(t)
\setminus
\Omega_j(t).
$$

更強的情況甚至是：

$$
Q^*
\notin
\mathcal Q_t^{baseline}
$$

但：

$$
Q^*
\in
\mathcal Q_i(t),
$$

也就是主體不只先看到答案，而是先建立未來時代才普遍需要回答的問題。

因此，TCFT-01 的中心命題是：

$$
\boxed{
\text{Foresight quality is partly determined by
what futures and questions are made thinkable before probability begins.}
}
$$

未來預測能力的上界，不只由推理與估計能力決定，也受到其底空間本身的覆蓋、約束、粒度、可更新性與未知保留能力限制。

**關鍵詞：** 未來底空間、候選世界、未來空間、想像力、問題生成、scenario planning、open world、未知未知、支撐失敗、TCFT、CODT、future-space generation

---

# Abstract

Forecasting research commonly treats the outcome space as given. A question is formulated, a set of candidate outcomes is specified, and forecasters are asked to assign probabilities, rankings, or directional judgments. In open-world, long-horizon, technological, institutional, and AI-driven settings, however, a deeper difficulty occurs before probability estimation: which futures enter the candidate space at all, which questions become thinkable, and which representations make not-yet-formed futures cognitively operable?

This paper introduces the **Future Base-Space** as a core construct of Temporal Cognitive Frontier Theory (TCFT). The term is not intended as a direct reuse of the standard mathematical notion of a base space in topology or bundle theory. It denotes the pre-probabilistic cognitive support through which an agent or cognitive system generates, represents, compares, and revises candidate futures under time-indexed informational and resource constraints.

For agent $i$ at time $t$, a minimal candidate is:

$$
\boxed{
\mathfrak B_i(t)
=
(
\Omega_i(t),
\mathcal Q_i(t),
\mathcal R_i(t),
\Gamma_i(t),
\mathcal U_i(t)
)
}
$$

where $\Omega_i(t)$ is the candidate future-state/path set, $\mathcal Q_i(t)$ the set of formulable future questions, $\mathcal R_i(t)$ the available representation system, $\Gamma_i(t)$ the knowledge and resource context, and $\mathcal U_i(t)$ an explicit reserve for futures that are not yet enumerated, named, or representable.

The paper proposes the **Space-Before-Probability Principle**: before a probability can be meaningfully assigned to a future, that future must be represented within some candidate support. If the realized future $W^*$ is absent from the agent's support, then the failure is not merely miscalibration; it is a **base-space omission** or **support failure**.

We distinguish base-space selection, generation, and revision, and develop criteria for coverage, constraint compatibility, causal coherence, granularity, discriminability, compressibility, updateability, and unknown reservation. Scenario planning and possibility-space research already study plural plausible futures; open-set and open-world learning study incomplete class universes; creativity and scientific-idea research examine divergent generation and problem finding. TCFT builds on these traditions while focusing specifically on the candidate future support itself as a time-indexed, agent-relative, auditable cognitive product.

The central proposition is:

$$
\boxed{
\text{Foresight quality is partly determined by
what futures and questions are made thinkable before probability begins.}
}
$$

Temporal cognitive advancement may therefore arise not only from better probability estimates over a shared future space, but from constructing a better future space in the first place.

**Keywords:** future base-space; candidate worlds; future-space generation; problem generation; scenario planning; open world; unknown unknowns; support failure; foresight; TCFT

---

# 1. 導論：在預測以前，先發生了什麼？

## 1.1 機率從來不是第一步

設研究者要求預測者回答：

> 某項技術在 2030 年前是否商業化？

標準形式可能是：

$$
P(Y=1\mid X_{\le t}).
$$

這個問題看似從「現在」直接連向「未來」，但它其實已經偷偷完成多個前置決策：

1. 什麼叫「該項技術」？
2. 什麼叫「商業化」？
3. 為什麼時間界線是 2030？
4. 候選答案為什麼只有 yes / no？
5. 是否允許「部分商業化」？
6. 是否允許技術被另一種架構取代，使原問題失去意義？
7. 是否存在當時根本沒有命名的新產品形態？

因此，真正的預測流程更接近：

$$
\boxed{
\text{World}
\rightarrow
\text{Problem Construction}
\rightarrow
\text{Candidate-Space Construction}
\rightarrow
\text{Representation}
\rightarrow
\text{Probability / Judgment}.
}
$$

TCFT-01 將注意力放到 probability 以前。

---

## 1.2 若候選未來不存在，準確率沒有地方落下

假設某預測者建立：

$$
\Omega_A
=
\{W_1,W_2,W_3\}.
$$

並配置：

$$
P(W_1)=0.5,
\quad
P(W_2)=0.3,
\quad
P(W_3)=0.2.
$$

若真實未來：

$$
W^*=W_2,
$$

可以討論 calibration。

但若：

$$
W^*\notin\Omega_A,
$$

問題不同了。

在 closed-world 模型裡：

$$
\sum_{W\in\Omega_A}P(W)=1.
$$

因此所有機率都被迫分配到：

$$
\Omega_A.
$$

如果真實世界落在外面，這不是單純：

$$
P(W^*)
\text{ 太低}.
$$

而是：

$$
\boxed{
W^*
\text{ was not a representable event in the model.}
}
$$

TCFT 稱此為：

$$
\boxed{
\text{Base-Space Omission}.
}
$$

---

# 2. 「底空間」的工作定義

## 2.1 不是拓撲學 standard base space 的直接借用

本文使用：

**Future Base-Space / 未來底空間**

作為 TCFT 專有工作概念。

它不等同：

- topology 的 base；
- fiber bundle 的 base space；
- probability sample space；
- state space；
- scenario set；
- latent space。

它與這些概念有結構類比，但角色不同。

---

## 2.2 最小 tuple

定義：

$$
\boxed{
\mathfrak B_i(t)
=
(
\Omega_i,
\mathcal Q_i,
\mathcal R_i,
\Gamma_i,
\mathcal U_i
)_t.
}
$$

其中：

### Candidate Future Set

$$
\Omega_i(t)
$$

表示目前可被 agent $i$ 生成、表示或操作的候選未來狀態／路徑。

### Question Space

$$
\mathcal Q_i(t)
$$

表示 agent 能夠提出的未來問題集合。

### Representation Space

$$
\mathcal R_i(t)
$$

表示 agent 用來區分、描述、壓縮、模擬候選未來的表示方式。

### Constraint Context

$$
\Gamma_i(t)
$$

包含：

- available knowledge；
- physical constraints；
- institutions；
- language；
- models；
- tools；
- resources；
- computational budget；
- cultural priors；
- evidence。

### Unknown Reserve

$$
\mathcal U_i(t)
$$

是對尚未枚舉、尚未命名、尚未建模或尚未可表示可能性的明確保留接口。

---

# 3. Space-Before-Probability Principle

本文第一個核心原則：

$$
\boxed{
\text{Probability allocation presupposes representable support.}
}
$$

對：

$$
P(W)
$$

而言，

若：

$$
W
$$

根本無法由目前 representation 形成可操作事件，

那麼：

$$
P(W)
$$

並不是單純「未知」。

它可能根本是：

$$
\boxed{
\text{not yet in the agent's event algebra}.
}
$$

因此：

$$
\boxed{
\text{Unknown Probability}
\neq
\text{Unrepresented Possibility}.
}
$$

這個 distinction 對長期未來尤其重要。

---

# 4. Closed Future Space 與 Open Future Space

## 4.1 Closed Future Space

若：

$$
\Omega
=
\{W_1,\ldots,W_n\}
$$

被假定為 exhaustively specified，

則：

$$
\sum_{k=1}^{n}P(W_k)=1.
$$

這適合：

- 選舉；
- 比賽；
- 某些金融事件；
- 封閉實驗；
- 明確期限的政策結果。

---

## 4.2 Open Future Space

長期技術與文明演化常更像：

$$
\boxed{
\Omega_t
\subsetneq
\Omega_{t+1}.
}
$$

新的：

- 技術；
- 主體；
- 制度；
- 語言；
- 風險；
- 問題；
- 互動模式；

可以使 outcome ontology 本身變化。

此時不能假定：

$$
\Omega_t
=
\Omega_{\mathrm{all}}.
$$

---

## 4.3 Unknown-Reserved Future Space

TCFT 建議至少概念上保留：

$$
\boxed{
\mathcal U_t
\neq
\varnothing.
}
$$

它不是一個「神秘垃圾桶」。

它表示：

> 目前沒有充分理由相信候選空間已封閉。

因此：

$$
\boxed{
\Omega_t^{known}
+
\mathcal U_t
}
$$

比：

$$
\Omega_t^{known}
=
\Omega_{\mathrm{all}}
$$

更適合許多長期 foresight 問題。

---

# 5. Open-Set Recognition 的結構類比

Machine learning 中的 open-set recognition 已長期指出：訓練時通常不可能取得所有類別，測試時可能出現未見類別。

這給 TCFT 一個重要類比：

$$
\boxed{
\text{Seen Classes}
\neq
\text{All Possible Classes}.
}
$$

但 TCFT 不直接把 open-set classification 等同 future base-space。

差異是：

open-set recognition 的 unknown class 通常仍假定「外部世界已有該類別，只是模型沒看過」。

TCFT 的未來問題更強：

$$
\boxed{
\text{future categories themselves may not yet be socially,
technically, or cognitively stabilized}.
}
$$

有些未來不是「存在但沒看過」。

而可能是：

> 需要未來的技術、制度與概念共同發展後，才成為穩定可描述對象。

---

# 6. Selection、Generation 與 Revision

## 6.1 Base-Space Selection

若有候選母池：

$$
\Omega^{pool},
$$

主體選出：

$$
\Omega_i
\subseteq
\Omega^{pool}.
$$

這是：

$$
\boxed{
\text{Selection}.
}
$$

例如從 100 個 scenario 中挑 6 個研究。

---

## 6.2 Base-Space Generation

更強的操作：

$$
\boxed{
G_i^{BS}:
(
K_{\le t},
H_i,
R_i
)
\rightarrow
\Omega_i(t).
}
$$

它不是挑選既有 scenario，

而是產生：

$$
W^*
\notin
\Omega^{pool}.
$$

---

## 6.3 Base-Space Revision

當新證據：

$$
E_{t+1}
$$

出現：

$$
\boxed{
\mathfrak B_i(t+1)
=
U(
\mathfrak B_i(t),
E_{t+1}
).
}
$$

Revision 可以：

- add；
- delete；
- split；
- merge；
- refine；
- coarse-grain；
- reparameterize；
- abandon。

因此：

$$
\boxed{
\text{Good Foresight}
\neq
\text{Never Changing the Future Space}.
}
$$

能修正底空間，本身可能是一種能力。

---

# 7. 想像力的形式位置

「想像力」常被當成模糊人格詞。

TCFT 暫時只取其一個可操作子意義：

$$
\boxed{
Imagination_i(t)
\supset
\text{capacity to generate non-observed candidate configurations}.
}
$$

也就是：

$$
G_i:
K_{\le t}
\rightarrow
\{W_1',W_2',\ldots\}.
$$

但：

$$
\boxed{
\text{Imagination Breadth}
\neq
\text{Future Base-Space Quality}.
}
$$

幻想一百萬個世界不等於有高 foresight。

---

# 8. Base-Space Quality

本文暫定八個維度。

## 8.1 Coverage

$$
Cov(\mathfrak B)
$$

問：

> 高價值可實現未來是否落在候選空間裡？

---

## 8.2 Constraint Compatibility

$$
Cons(\mathfrak B)
$$

問：

> 候選世界是否違反已知物理、制度、時間與資源約束？

---

## 8.3 Causal Coherence

$$
Caus(\mathfrak B)
$$

問：

> 是否存在可描述的路徑使當前世界到達候選未來？

---

## 8.4 Granularity

$$
Gran(\mathfrak B)
$$

太粗：

$$
W_1=\text{「AI 會變強」}
$$

幾乎無資訊。

太細則可能：

$$
|\Omega|
\rightarrow
\infty
$$

而失去可操作性。

---

## 8.5 Discriminability

$$
Disc(\mathfrak B)
$$

不同候選是否能被 future evidence 區分？

---

## 8.6 Compression

$$
Comp(\mathfrak B)
$$

能否用有限結構涵蓋高價值未來，而非枚舉所有故事？

---

## 8.7 Revisability

$$
Rev(\mathfrak B)
$$

新證據是否能合法修改底空間？

---

## 8.8 Unknown Reservation

$$
UR(\mathfrak B)
$$

是否保存：

$$
\text{「我的候選集合可能不完整」}
$$

這一 epistemic channel？

---

# 9. Quality-Adjusted Base-Space

因此暫定：

$$
\boxed{
Q_{BS}
=
f(
Cov,
Cons,
Caus,
Gran,
Disc,
Comp,
Rev,
UR
).
}
$$

這不是宣稱存在唯一正確加權。

未來 benchmark 可以：

- 保留向量；
- 建 Pareto frontier；
- 針對任務給權重；
- 做 sensitivity analysis。

---

# 10. 兩種完全不同的預測失敗

## 10.1 Probability Error

真實未來：

$$
W^*
\in
\Omega_i.
$$

但：

$$
P_i(W^*)
$$

太低。

這是：

$$
\boxed{
\text{Probability / Calibration Failure}.
}
$$

---

## 10.2 Support Failure

真實未來：

$$
W^*
\notin
\Omega_i.
$$

這是：

$$
\boxed{
\text{Base-Space / Support Failure}.
}
$$

兩者不能混在一起。

---

# 11. 第三種失敗：Question Failure

甚至可能：

$$
Q^*
\notin
\mathcal Q_i(t).
$$

也就是未來真正重要的問題根本沒有被提出。

例如某時代所有人都在問：

> 如何把既有系統做到更快？

但真正轉折問題是：

> 為什麼一定要保留這種系統？

如果：

$$
Q^*
$$

沒出現，

所有 downstream optimization 都可能在錯誤問題上越做越好。

因此：

$$
\boxed{
\text{Question-Space Failure}
}
$$

比 support failure 更前置。

---

# 12. 問題先行命題

TCFT-01 提出：

$$
\boxed{
\text{Problem Space constrains Future Space.}
}
$$

因為：

$$
\mathcal Q_i(t)
$$

會影響：

$$
G_i^{BS}.
$$

若某些問題不允許被提出：

$$
q\notin\mathcal Q_i,
$$

相關候選世界可能永遠不被生成。

所以：

$$
\boxed{
\mathcal Q_i
\rightarrow
\Omega_i.
}
$$

反過來：

$$
\Omega_i
$$

也會生成新問題：

$$
\boxed{
\Omega_i
\rightarrow
\mathcal Q_i'.
}
$$

因此形成：

$$
\boxed{
\mathcal Q_t
\leftrightarrow
\Omega_t.
}
$$

這是一個共同演化關係。

---

# 13. Problem Finding 與 TCFT

Creativity research 已長期區分 problem solving 與 problem finding。

近年的研究仍在實證測量：

- question fluency；
- flexibility；
- originality；
- semantic exploration。

這表示：

$$
\text{Problem Generation}
$$

不是只能用傳記故事描述。

但 TCFT 的額外要求是：

$$
\boxed{
\text{Problem Novelty must be time-normalized}.
}
$$

一個今天看起來普通的問題：

$$
q
$$

如果在 1500 年：

$$
q\notin\mathcal Q_{baseline,1500},
$$

可能具有極高 historical novelty。

---

# 14. Scenario Planning 與 TCFT 的關係

Scenario planning 本來就拒絕把未來縮成單一路徑。

現有 review 顯示，scenario planning 的不同 schools 會強調：

- plausible alternatives；
- uncertainty；
- coherent narratives；
- differentiated scenario sets；
- participatory construction；
- dynamic modeling。

因此 TCFT 不宣稱：

> 「多個未來」是一個新發明。

真正差異是：

$$
\boxed{
\text{Scenario Set}
\subset
\text{Future Base-Space Structure}.
}
$$

TCFT 額外追問：

1. 為什麼這些 scenarios 被生成？
2. 哪些根本沒被生成？
3. 問題空間如何限制 scenario space？
4. representation 是否排除某些未來？
5. unknown reserve 是否存在？
6. 不同時代／agent 的 base-space 如何比較？
7. 後來成真的未來是否曾落在早期支撐中？

---

# 15. Possibility Space 不等於 Probability Space

假設：

$$
\Pi(W)
$$

表示 possibility-like admissibility，

而：

$$
P(W)
$$

表示 probability。

則：

$$
\boxed{
\Pi(W)>0
}
$$

只表示：

> 此未來尚未被排除／可被考慮。

不要求：

$$
P(W)
$$

已可可靠估計。

TCFT 的 base-space 更接近：

$$
\boxed{
\text{pre-probabilistic representability + admissibility structure}
}
$$

而不是直接推出一套 possibility theory。

---

# 16. Base-Space 的時間動力學

未來底空間不是靜態集合。

可以寫：

$$
\boxed{
\mathfrak B_i(t+1)
=
F(
\mathfrak B_i(t),
E_{t+1},
G_i,
R_i,
C_i
).
}
$$

其中：

- $E$：新證據；
- $G$：生成器；
- $R$：表示能力；
- $C$：資源／成本限制。

所以：

$$
\Omega_i(t+1)
$$

可能：

$$
\supset
\Omega_i(t),
$$

也可能：

$$
\subset
\Omega_i(t),
$$

因為錯誤候選可以被刪除。

---

# 17. 擴張不是永遠正向

直覺會認為：

$$
|\Omega|\uparrow
\Rightarrow
Q_{BS}\uparrow.
$$

不成立。

若加入大量低品質候選：

$$
Noise\uparrow,
$$

可能導致：

$$
DecisionQuality\downarrow.
$$

因此：

$$
\boxed{
\text{Future-Space Expansion}
\neq
\text{Future-Space Improvement}.
}
$$

---

# 18. 壓縮不是永遠正向

反過來：

$$
|\Omega|\downarrow
$$

也不必然變好。

如果把真實未來刪掉：

$$
W^*\notin\Omega',
$$

就是錯誤壓縮。

所以：

$$
\boxed{
\text{Useful Compression}
=
\text{complexity reduction without catastrophic support loss}.
}
$$

這與既有「未來空間壓縮」理論形成直接接口。

---

# 19. Base-Space 與 CODT

TCFT 不把：

$$
G_i^{BS}
$$

直接稱為 primitive cognitive operator。

依 CODT：

$$
\boxed{
Method
=
Program(
Operators,
Topology,
Context,
Policy,
Budget
).
}
$$

因此 future base-space generation 目前應先視為：

$$
\boxed{
P_{BS}
=
\text{candidate cognitive program}.
}
$$

它可能需要：

- acquire；
- abstract；
- retrieve；
- analogize；
- generate；
- perturb；
- constrain；
- simulate；
- reject；
- cluster；
- represent；
- revise；
- terminate。

---

# 20. Base-Space Generation 不是單一「想像域」

同理：

$$
\boxed{
\text{Future Base-Space Generation}
\not\Rightarrow
\text{Promoted Cognitive Domain}.
}
$$

是否形成 domain candidate，

必須回到：

$$
\mathfrak D_\alpha^{(t,B)}
=
\operatorname{Cl}_{\Lambda_\alpha}^{B}
(
\mathcal U_\alpha
)
$$

並檢查：

- legal composition；
- predictive value；
- reuse；
- stable interface；
- failure coherence；
- cross-run robustness。

因此本文只建立 TCFT 的功能層，不偷渡 CODT ontology。

---

# 21. Agent-Relative Base-Space

同一個世界資訊：

$$
K_t
$$

給兩個 agent：

$$
A,B,
$$

可能得到：

$$
\Omega_A(t)
\neq
\Omega_B(t).
$$

原因可以包括：

- knowledge；
- representation；
- language；
- embodiment；
- training；
- domain experience；
- tools；
- search strategy；
- attention；
- computational budget；
- cultural priors；
- risk tolerance。

所以：

$$
\boxed{
\text{Future Base-Space is observer/agent-relative,
not arbitrary.}
}
$$

relative 不等於 subjective fantasy。

因為它仍然可以接受世界約束與後續驗證。

---

# 22. Temporal Base-Space Gap

對兩個 agent：

$$
i,j
$$

定義概念性差異：

$$
\boxed{
\Delta\Omega_{i,j}(t)
=
\Omega_i(t)
\setminus
\Omega_j(t).
}
$$

若：

$$
W^*
\in
\Delta\Omega_{i,j}(t),
$$

而：

$$
W^*
$$

後來成為高價值／真實未來，

則：

$$
i
$$

至少在 candidate-space coverage 上超過：

$$
j.
$$

---

# 23. 但集合較大不等於更好

如果：

$$
\Omega_j
\subsetneq
\Omega_i
$$

只因：

$$
i
$$

生成更多垃圾，

不構成優勢。

因此應定義 quality-filtered region：

$$
\boxed{
\Omega_i^{+}
=
\{
W\in\Omega_i:
Q(W)\ge\theta
\}.
}
$$

再比較：

$$
\Delta\Omega_{i,j}^{+}.
$$

---

# 24. Temporal Novelty of Base-Space

對時間 $t$ 的 baseline：

$$
\Omega_{B_t},
$$

候選主體：

$$
\Omega_i(t).
$$

可以定義：

$$
\boxed{
N_{BS}(i,t)
=
Novelty(
\Omega_i(t)
\setminus
\Omega_{B_t}
).
}
$$

但必須加入：

$$
\text{LaterValue}
$$

避免把純隨機奇想算高分。

因此更合理的是：

$$
\boxed{
Adv_{BS}(i,t)
=
f(
Novelty,
Constraint,
LaterValue,
Specificity,
Independence
).
}
$$

---

# 25. 「未來人」案例中的 Base-Space Test

若某人自稱來自：

$$
t+50,
$$

傳統做法可能只列：

$$
\text{prediction hit rate}.
$$

TCFT-01 會問：

1. 他描述的未來空間是否只是同期科幻常見 extrapolation？
2. 是否存在同期極少見的新 ontology？
3. 是否知道後來才會重要的問題？
4. 是否描述 unexpected tradeoffs？
5. 是否出現新的 interaction regime？
6. 他的候選未來是否比同期專家更廣，但又不是胡亂枚舉？
7. 是否存在 genuine support novelty？

若：

$$
\Omega_{future-person}
\approx
Extend(
\Omega_{popular,t}
),
$$

其 base-space novelty 可能很低。

---

# 26. 歷史人物中的 Base-Space Test

歷史人物的價值也不只看預言。

若某人在時間：

$$
t_0
$$

反覆建立：

$$
\Omega_i(t_0)
$$

其中包含後來才成為成熟科學／工程問題的區域，

而同期：

$$
\Omega_{B_{t_0}}
$$

很少包含，

則可以形成：

$$
\boxed{
\text{Historical Future-Space Advancement}.
}
$$

但必須控制：

- hindsight projection；
- selective preservation；
- vague resemblance；
- mythologization；
- prior art omission。

---

# 27. AI 時代的 Candidate Explosion

生成式 AI 可以快速產生：

$$
\Omega_{AI}
=
\{W_1,\ldots,W_{10^5}\}.
$$

這會使：

$$
\text{Generation Cost}
\downarrow.
$$

但也使：

$$
\text{Evaluation Cost}
\uparrow.
$$

因此 AI 時代的真正瓶頸可能從：

$$
\text{Can we generate alternatives?}
$$

轉向：

$$
\boxed{
\text{Can we construct a useful, constrained, auditable future base-space?}
}
$$

---

# 28. AI 多量生成不等於高前沿

2026 年已有研究顯示，LLM 可以在科學 idea-generation 任務中大量產生具有 originality 與 flexibility 的候選，且一般 intelligence benchmark 未必能充分預測其 divergent scientific ideation 表現。

但也有研究指出：

- novelty 與 feasibility 可能分離；
- self-evaluation 仍有問題；
- diversity 可能不足；
- evaluation systems 本身可能對 novelty 有偏差。

因此：

$$
\boxed{
\text{LLM Candidate Volume}
\neq
\text{TCFT Base-Space Advancement}.
}
$$

---

# 29. Base-Space Search as Resource Allocation

假設總認知／計算預算：

$$
B.
$$

可分配到：

$$
B
=
B_{generate}
+
B_{evaluate}
+
B_{verify}
+
B_{revise}.
$$

若：

$$
B_{generate}\approx B,
$$

但：

$$
B_{evaluate}\approx0,
$$

會產生 scenario spam。

反過來若：

$$
B_{generate}\approx0,
$$

只在既有候選中精細估計，

會產生 closed-space blindness。

因此需要：

$$
\boxed{
\text{Generation-Evaluation Allocation}.
}
$$

---

# 30. Adaptive Base-Space Budget

可以概念性寫：

$$
\boxed{
B_{gen}^{*}
=
\arg\max_{b}
\left[
ExpectedCoverageGain(b)
-
GenerationCost(b)
-
EvaluationBurden(b)
\right].
}
$$

這把「想更多未來」重新寫成 resource allocation 問題。

---

# 31. 問題生成也具有成本

同樣：

$$
|\mathcal Q|\uparrow
$$

不一定更好。

大量毫無價值問題會：

$$
SearchCost\uparrow.
$$

因此：

$$
\boxed{
\text{Problem Fluency}
\neq
\text{Problem Frontier Quality}.
}
$$

需要：

$$
Q_Q
=
f(
Novelty,
Relevance,
Tractability,
Generativity,
LaterValue
).
$$

---

# 32. Generative Questions

有些問題的價值不只在答案，

而在於：

$$
q
\rightarrow
\{q_1,q_2,\ldots,q_n\}.
$$

這類問題可以稱：

$$
\boxed{
\text{Generative Question}.
}
$$

其重要性可能來自：

$$
\text{Question-Induced Space Expansion}.
$$

也就是：

$$
\boxed{
\mathcal Q_t
\xrightarrow{q^*}
\Omega_{t+1}^{larger}.
}
$$

---

# 33. Base-Space 與表示

不同 representation：

$$
R_1,R_2
$$

可能生成不同：

$$
\Omega.
$$

例如同一現象若只用：

$$
\text{binary label}
$$

表示，

可能看不到：

- continuous transition；
- multi-agent interaction；
- partial adoption；
- hybrid states；
- emergent category。

所以：

$$
\boxed{
Representation
\rightarrow
Possible Future Support.
}
$$

這表示表示系統不是中性的容器。

---

# 34. Representation-Induced Blindness

若：

$$
R
$$

只能表示：

$$
\{0,1\},
$$

但世界其實需要：

$$
[0,1]^n
$$

或 relational graph，

則：

$$
\Omega_R
$$

會系統性遺漏某些未來。

本文稱：

$$
\boxed{
\text{Representation-Induced Base-Space Blindness}.
}
$$

---

# 35. 語言與概念邊界

同樣地，

如果一個時代沒有概念：

$$
c^*,
$$

並不表示現象：

$$
X^*
$$

不存在。

但：

$$
X^*
$$

可能較難被：

- 壓縮；
- 溝通；
- 累積；
- 搜尋；
- 比較；
- 建模。

因此：

$$
\boxed{
\text{Concept Availability}
\neq
\text{World Existence},
}
$$

但：

$$
\boxed{
\text{Concept Availability}
\rightarrow
\text{Cognitive Reachability}.
}
$$

---

# 36. 原生概念與 Future Base-Space

這裡直接接 CODT 與 AI-native cognition。

如果 AI 或其他 agent：

$$
A
$$

產生一個人類語言中沒有直接名稱的內部可操作結構：

$$
z^*,
$$

且：

$$
z^*
$$

使其能生成：

$$
W^*
$$

而人類 baseline 無法方便生成，

那麼 future base-space advancement 可能發生在：

$$
\boxed{
\text{native representation layer}.
}
$$

因此 TCFT 不能只查「說了什麼詞」。

還要查：

$$
\text{What operational distinction was actually available?}
$$

---

# 37. Base-Space 與反事實覆蓋

反事實生成：

$$
\mathcal C_i(t)
=
G_i(H_{\le t})
$$

可以被看作 future base-space 的一種重要生成來源。

但：

$$
\boxed{
\mathcal C_i(t)
\subseteq
\Omega_i(t)
}
$$

不必永遠成立為嚴格同一形式，

因為 $\Omega_i$ 還可能包含：

- extrapolated futures；
- abductive futures；
- speculative ontology changes；
- adversarial scenarios；
- novel agent emergence；
- open unknown placeholders。

---

# 38. Base-Space 與反身性

若預測被公開：

$$
F_t,
$$

世界可能：

$$
W_{t+1}
=
T(W_t,F_t).
$$

那麼 future base-space 不能只包含：

$$
\text{world without prediction}.
$$

還需要：

$$
\text{world after agents hear prediction}.
$$

因此：

$$
\boxed{
\Omega^{reflexive}
\supset
\Omega^{nonreflexive}.
}
$$

某些高階未來必須把預測行為本身納入候選空間。

---

# 39. Base-Space 失敗可能造成虛假自信

如果：

$$
\Omega_i
$$

過窄，

agent 可以在裡面表現得非常 confident：

$$
\max_WP(W)\approx0.99.
$$

但：

$$
W^*\notin\Omega_i.
$$

因此：

$$
\boxed{
\text{High Confidence inside a misspecified future space
can coexist with catastrophic epistemic failure}.
}
$$

這是 TCFT-01 的重要認識論警告。

---

# 40. Unknown Reserve 的必要性

因此：

$$
\mathcal U_i(t)
$$

不能只是裝飾。

一個成熟系統至少需要允許：

$$
\boxed{
P(
\text{support incomplete}
)
>0
}
$$

或以其他非概率表示保留：

$$
\boxed{
\text{UnknownSupportFlag}=1.
}
$$

TCFT 不在本文規定唯一實作。

---

# 41. Unknown 不等於 Uncertain

Open-world research 已指出一個重要 distinction：

$$
\boxed{
\text{Uncertain}
\neq
\text{Unknown}.
}
$$

一個模型對已知類別非常不確定，

和：

> 輸入屬於模型根本沒有建立的類別，

不是同一件事。

TCFT 借用此結構警告：

$$
\boxed{
\text{Low Probability Known Future}
\neq
\text{Unrepresented Future}.
}
$$

---

# 42. Base-Space Discovery Event

當 agent 發現：

$$
W^*
\notin\Omega_i(t)
$$

但新 evidence 要求建立：

$$
W^*,
$$

可以定義：

$$
\boxed{
\text{Base-Space Discovery Event}.
}
$$

其結果：

$$
\Omega_i(t+1)
=
\Omega_i(t)
\cup
\{W^*\}
$$

或更強：

$$
\Omega_i(t+1)
=
Rebuild(
\Omega_i(t),
W^*
).
$$

---

# 43. 有些新未來會迫使整個空間重建

如果新未來只是多一個 item：

$$
\Omega'
=
\Omega
\cup
\{W^*\},
$$

是弱 revision。

但有時：

$$
W^*
$$

顯示原有座標系錯誤。

此時：

$$
\boxed{
\Omega'
\not\cong
\Omega+\{W^*\}.
}
$$

需要重新定義：

- axes；
- state variables；
- agent types；
- transition rules；
- representation。

這是：

$$
\boxed{
\text{Base-Space Reconstruction}.
}
$$

---

# 44. 超前者可能不是「猜得準」，而是較早重建空間

因此一個歷史超前者可能：

$$
ForecastAccuracy
$$

普通，

但在：

$$
\text{Base-Space Reconstruction Timing}
$$

極端超前。

這提供 TCFT 一個重要新指標：

$$
\boxed{
T_{reconstruct}(i)
}
$$

比較：

$$
T_{reconstruct}(i)
<
T_{reconstruct}(baseline).
$$

---

# 45. 時間優勢

定義：

$$
\boxed{
\Delta T_i(X)
=
T_{baseline}(X)
-
T_i(X).
}
$$

若某結構：

$$
X
$$

被 agent $i$ 提前：

$$
\Delta T_i(X)>0.
$$

但時間差不能單獨成為價值。

因為：

$$
X
$$

可能最後沒用。

因此：

$$
\boxed{
TemporalLead
\neq
TemporalValue.
}
$$

---

# 46. Base-Space Advancement Candidate

暫定：

$$
\boxed{
BSA_i(t)
=
f(
N_{BS},
Q_{BS},
\Delta T,
LaterUtility,
Independence,
Integrity
).
}
$$

其中：

- $N_{BS}$：相對同期 baseline 的 space novelty；
- $Q_{BS}$：底空間品質；
- $\Delta T$：提前量；
- $LaterUtility$：後續價值；
- $Independence$：是否可由同期 prior art／洩漏解釋；
- $Integrity$：版本與時間戳可信度。

---

# 47. Later Utility 的危險

使用：

$$
LaterUtility
$$

會引入 hindsight bias。

所以必須避免：

> 後來成功，因此當時一定高明。

TCFT 建議分開：

$$
\boxed{
ExAnteQuality
}
$$

與：

$$
\boxed{
ExPostValidation.
}
$$

先用：

$$
K_{\le t}
$$

評估當時是否受約束、合理、可區分，

再用後續世界做第二階驗證。

---

# 48. Ex Ante / Ex Post 雙帳

定義：

$$
\boxed{
BSA_i^{pre}(t)
}
$$

只使用：

$$
K_{\le t}.
$$

再定義：

$$
\boxed{
BSA_i^{post}(t,t+k)
}
$$

允許查看：

$$
W_{t+1:t+k}.
$$

兩者必須分帳。

否則所有歷史人物都會被後見之明污染。

---

# 49. Frozen-Time Base-Space Audit

對一份時間：

$$
t_0
$$

的文件，

建立：

$$
K_{\le t_0}.
$$

再由多個 baseline agents 生成：

$$
\Omega_{B_1},
\Omega_{B_2},
\ldots,
\Omega_{B_m}.
$$

候選作者生成：

$$
\Omega_i.
$$

比較：

$$
\Delta\Omega_i
=
\Omega_i
\setminus
\bigcup_{k=1}^{m}\Omega_{B_k}.
$$

這是 TCFT-05 未來可正式化的重要實驗接口。

---

# 50. 不能讓 baseline 看見作者答案

若 baseline model 先看過：

$$
X_i,
$$

再被要求：

> 只用當時資料判斷能不能想到。

會產生 anchoring / leakage。

因此：

$$
\boxed{
\text{Candidate-Blind Baseline Generation}
}
$$

應成為 protocol。

---

# 51. 多模型 Base-Space Union

單一 baseline 可能太弱。

因此使用：

$$
\boxed{
\Omega_{B_t}^{collective}
=
\bigcup_{j=1}^{m}
\Omega_{B_j}(t).
}
$$

如果候選主體仍有：

$$
W^*
\notin
\Omega_{B_t}^{collective}
$$

但：

$$
W^*\in\Omega_i,
$$

異常性更強。

---

# 52. 但 Union 會無限膨脹

如果：

$$
m\rightarrow\infty,
$$

而每個 baseline 都可以亂生成，

最終 union 會覆蓋一切。

所以 baseline union 必須 quality-adjusted：

$$
\boxed{
\Omega_{B_t}^{+}
=
\bigcup_j
\{
W\in\Omega_{B_j}:
Q(W)\ge\theta
\}.
}
$$

這是未來 benchmark 的必要限制。

---

# 53. 群體不一定包含所有好未來

即使：

$$
\Omega_{collective}
=
\bigcup_i\Omega_i,
$$

仍可能：

$$
W^*
\notin
\Omega_{collective}.
$$

因此：

$$
\boxed{
\text{Collective Coverage}
\neq
\text{Complete Coverage}.
}
$$

這與既有 Counterfactual Horizon 的限制一致。

---

# 54. Base-Space 的非單調知識論

新的知識可能：

$$
\Omega\uparrow
$$

也可能：

$$
\Omega\downarrow.
$$

例如物理定律排除大量幻想。

因此：

$$
\boxed{
K\uparrow
\not\Rightarrow
|\Omega|\uparrow.
}
$$

知識進步可以同時：

- 開新區域；
- 關閉舊區域；
- 重構座標。

---

# 55. 時代進步不是單純「知道更多未來」

如果：

$$
\Omega_{2026}
$$

比：

$$
\Omega_{1500}
$$

大，

不表示 2026 每個人都比 1500 每個超前者更會生成。

TCFT 研究的是：

$$
\boxed{
\text{agent-relative advancement under time-normalized baselines}.
}
$$

而不是文明知識量的簡單比較。

---

# 56. Base-Space 與時代認知前沿

假設：

$$
\vec C_i(t)
$$

是 TCFT 多維向量。

Paper 01 提供其中一軸：

$$
\boxed{
C_i^{BS}(t).
}
$$

它不代表全面認知能力。

但可能成為：

$$
\vec C_i(t)
=
(
C_i^{BS},
C_i^{CF},
C_i^{RR},
\ldots
).
$$

---

# 57. 可反證命題

## H1：Support Failure 與 Probability Failure 可實證區分

若實際 benchmark 中，所有所謂 support failure 都可等價重寫成已有 outcome space 上的低機率事件，則 Future Base-Space 不需要獨立理論角色。

---

## H2：Base-Space Quality 能預測 Long-Horizon Foresight

如果：

$$
Q_{BS}
$$

無法在 out-of-sample future evaluation 中提供超越普通 scenario count / diversity 指標的價值，則其強版本應降級。

---

## H3：Problem-Space Novelty 對 Base-Space 有額外貢獻

如果加入：

$$
\mathcal Q_i
$$

後，不能改善對：

$$
\Omega_i
$$

品質或後續價值的解釋，

則「問題先行」不應獨立成核心機制。

---

## H4：Unknown Reserve 能降低 Catastrophic Overconfidence

若明確保存：

$$
\mathcal U
$$

無法改善 open-world calibration、revision 或 surprise handling，

則它可能只是一個哲學標籤。

---

## H5：Native Representation 可形成不同 Candidate Support

若不同 representation 在控制資訊量後總是導出等價：

$$
\Omega,
$$

則 representation-induced base-space blindness 主張被削弱。

---

# 58. 實驗方向一：Historical Frozen-Space Reconstruction

選擇歷史文件：

$$
D_{t_0}.
$$

建立：

$$
K_{\le t_0}.
$$

讓：

- historians；
- domain experts；
- LLMs；
- human-AI teams；

在不看候選文件核心結論下生成：

$$
\Omega_{baseline}.
$$

再 recovery：

$$
\Omega_{candidate}.
$$

比較 novelty、constraint、later validation。

---

# 59. 實驗方向二：Future-Space Coverage Benchmark

建立現代可在未來驗證的問題。

在：

$$
t_0
$$

讓不同系統產生：

$$
\Omega_i(t_0).
$$

封存。

在：

$$
t_1
$$

檢查：

$$
W^*.
$$

評估：

$$
\mathbf 1[
W^*\in\Omega_i(t_0)
].
$$

再加 quality penalty，避免暴力枚舉。

---

# 60. 實驗方向三：Representation Ablation

給相同 evidence：

$$
E
$$

但限制 representation：

$$
R_1,R_2,R_3.
$$

比較：

$$
\Omega_{R_1},
\Omega_{R_2},
\Omega_{R_3}.
$$

測量：

- coverage；
- diversity；
- causal coherence；
- future hit；
- compression。

---

# 61. 實驗方向四：Question-First Ablation

Group A 只能回答預設問題。

Group B 先生成問題：

$$
\mathcal Q_B,
$$

再生成：

$$
\Omega_B.
$$

若：

$$
Coverage_B
>
Coverage_A
$$

且不是靠 brute-force expansion，

則支持：

$$
\boxed{
\text{Problem Generation contributes to future-space quality}.
}
$$

---

# 62. 實驗方向五：Unknown Reserve Stress Test

讓系統面對故意包含：

$$
\text{novel class / novel regime / ontology shift}
$$

的 future task。

比較：

- closed-support agent；
- unknown-aware agent；
- support-revising agent。

觀察：

$$
\text{catastrophic confidence},
\text{recovery time},
\text{revision quality}.
$$

---

# 63. 對 AI 的特殊意義

AI 的優勢之一是：

$$
\text{parallel candidate generation}.
$$

但若沒有 base-space governance：

$$
\Omega_{AI}
$$

可能只是巨大而低品質的 scenario cloud。

所以真正 AI-native future reasoning 可能需要：

$$
\boxed{
Generate
\rightarrow
Constrain
\rightarrow
Cluster
\rightarrow
Challenge
\rightarrow
ReserveUnknown
\rightarrow
Revise.
}
$$

而不是只：

$$
Generate^{10000}.
$$

---

# 64. 對人類的特殊意義

人類認知頻寬有限。

因此人類可能更依賴：

$$
\boxed{
\text{high-value base-space compression}.
}
$$

強抽象能力可能體現在：

> 用少量結構生成比一般人更廣、但仍受約束的未來區域。

這是 TCFT 後續可以研究的候選命題，不在本文宣稱已證明。

---

# 65. 對 human-AI coupling 的意義

理想人機組合不一定是：

$$
HumanPredict
+
AIPredict.
$$

可能更像：

$$
\boxed{
Human:
\text{ontology shift / question generation}
}
$$

加：

$$
\boxed{
AI:
\text{mass candidate expansion / search / validation}
}
$$

但角色不應預先固定。

AI 也可能生成新問題，人類也可能做高精度驗證。

真正研究單位應是：

$$
\boxed{
\text{coupled base-space generator}.
}
$$

---

# 66. 與 TCFT-02 的接口

Paper 01 建立：

$$
\mathfrak B_i(t).
$$

下一篇將特別研究其中：

$$
\mathcal C_i(t)
$$

也就是：

$$
\boxed{
\text{Counterfactual Horizon}.
}
$$

TCFT-02 會問：

> 一個主體究竟能吞下多少沒有發生的世界？

以及：

> 多量反事實如何在不爆炸的情況下形成有效覆蓋？

---

# 67. 與 TCFT-03 的接口

若 agent 的預測本身影響世界，

則：

$$
\Omega_i
$$

必須包含：

$$
\text{prediction-dependent futures}.
$$

因此 Paper 03 的 reflexive reasoning 將擴展：

$$
\mathfrak B_i
$$

為：

$$
\boxed{
\mathfrak B_i^{reflexive}.
}
$$

---

# 68. 與 TCFT-04 的接口

底空間生成具有成本。

所以 Paper 04 將研究：

$$
\boxed{
\text{When should an agent stop expanding the future space?}
}
$$

以及：

$$
\boxed{
\text{When is a coarse but sufficient future space strategically superior?}
}
$$

---

# 69. 與 TCFT-05 的接口

Paper 05 將回答：

> 怎麼證明某人的底空間在當時真的新？

核心需要：

$$
\boxed{
\text{Frozen-Time Prior-Art Audit}.
}
$$

尤其要防止：

$$
\text{2026 concepts}
\rightarrow
\text{back-projection into 1500}.
$$

---

# 70. 侷限

第一，Future Base-Space 是理論構造，不是宣稱人腦內真的存在一個明確集合物件。

第二，實際 $\Omega$ 可能是：

- implicit；
- generative；
- continuous；
- graph-like；
- latent；
- non-enumerable。

因此集合表示只是第一版 abstraction。

第三，「後來成真」不能單獨證明當時 candidate quality。

第四，歷史作品的 base-space recovery 可能受到文本缺失與詮釋偏誤。

第五，unknown reserve 很難被直接量化。

第六，scenario diversity、semantic novelty 與 candidate coverage 之間可能高度相關，未來需做 ablation。

第七，任何單一 $Q_{BS}$ 都可能掩蓋多維 tradeoff，因此本文偏好多維向量。

第八，本文沒有宣稱可以窮舉所有 possible worlds。

第九，底空間更大不代表主體更高等、更聰明或更值得信任。

第十，TCFT 本身也可能選錯未來底空間；因此理論必須允許自己的 ontology 被後續研究重建。

---

# 71. 結論

TCFT-01 的核心不是：

> 誰能想像最多未來？

而是：

$$
\boxed{
\text{Which futures become cognitively available before prediction starts?}
}
$$

對任何 forecasting system，

通常先有：

$$
\mathfrak B_i(t),
$$

才有：

$$
P_i(W).
$$

因此：

$$
\boxed{
\text{Prediction Quality}
\le
\text{Candidate-Support Quality}
+
\text{Estimation Quality}
}
$$

這不是嚴格數值不等式，而是結構性上界命題：

如果真實未來沒有進入候選支撐，

再好的機率估計也救不了它。

所以：

$$
\boxed{
W^*
\notin
\Omega_i
}
$$

與：

$$
\boxed{
P_i(W^*)\ll1
}
$$

是兩種不同失敗。

更重要的是，

未來底空間不只由「世界有哪些可能」決定。

它同時受到：

$$
\mathcal Q_i,
\mathcal R_i,
\Gamma_i,
G_i
$$

影響。

也就是：

$$
\boxed{
\text{Questions}
+
\text{Representations}
+
\text{Constraints}
+
\text{Generators}
\rightarrow
\text{Thinkable Futures}.
}
$$

因此，真正罕見的時代超前可能不是：

> 在所有人都知道的幾條路裡，猜中一條。

而是：

$$
\boxed{
\text{在那條路尚未進入時代候選空間以前，
先讓它成為一條可以被思考、推演、反駁與驗證的路。}
}
$$

再更高一階：

$$
\boxed{
\text{在未來問題尚未被提出以前，
先生成使那個未來問題成立的認知底空間。}
}
$$

這就是 TCFT 所謂：

$$
\boxed{
\text{Future Base-Space Advancement}.
}
$$

但它仍然不是神秘身份。

不是預言豁免。

不是英雄證書。

它只是一種可被時間凍結、prior-art、baseline、反例與後續世界持續重新計算的認知前沿候選。

---

# References

1. Cordova-Pozo, K., & Rouwette, E. A. J. A. (2023). Types of scenario planning and their effectiveness: A review of reviews. *Futures*, 149, 103153. DOI: 10.1016/j.futures.2023.103153.
2. Wiebe, K., Zurek, M., Lord, S., Brzezina, N., Gabrielyan, G., Libertini, J., Loch, A., Thapa-Parajuli, R., Vervoort, J., & Westhoek, H. (2018). Scenario Development and Foresight Analysis: Exploring Options to Inform Choices. *Annual Review of Environment and Resources*, 43, 545–570. DOI: 10.1146/annurev-environ-102017-030109.
3. Byrne, D. S. (2024). Scenarios—using the complexity frame of reference to inform the construction of available futures in the possibility space. *Frontiers in Complex Systems*, 2, 1306328. DOI: 10.3389/fcpxs.2024.1306328.
4. Geng, C., Huang, S.-J., & Chen, S. (2021). Recent Advances in Open Set Recognition: A Survey. *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 43(10), 3614–3631. DOI: 10.1109/TPAMI.2020.2981604.
5. Boult, T. E., Cruz, S., Dhamija, A. R., Gunther, M., Henrydoss, J., & Scheirer, W. J. (2019). Learning and the Unknown: Surveying Steps toward Open World Recognition. *Proceedings of AAAI*, 33(01), 9801–9807. DOI: 10.1609/aaai.v33i01.33019801.
6. Sun, Y., & Linton, J. D. (2022). Combination of research questions and methods: A new measurement of scientific novelty. *Journal of Informetrics*, 16(2), 101282. DOI: 10.1016/j.joi.2022.101282.
7. Guo, S., Liao, L., Li, C., & Chua, T.-S. (2024). A Survey on Neural Question Generation: Methods, Applications, and Prospects. *Proceedings of IJCAI 2024*, 8038–8047. DOI: 10.24963/ijcai.2024/889.
8. Si, C., Yang, D., & Hashimoto, T. (2024). Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers. arXiv:2409.04109.
9. Ruan, K., Wang, X., Hong, J., et al. (2026). Evaluating LLMs' divergent thinking capabilities for scientific idea generation with minimal context. *Nature Communications*, 17, 3625.
10. Neo.K. (2026). *從不可知到條件可判斷：人機協作下的未來空間壓縮與可預判邊界*. EveMissLab.
11. Neo.K. (2026). *反事實覆蓋度：哲人王必須吞下多少個沒有發生的世界？* EveMissLab.
12. Neo.K. (2026). *Cognitive Operator-Domain Theory (CODT) Series 01–10*. EveMissLab.
13. Neo.K. (2026). *TCFT-00｜超前認知不是預言：時代認知前沿的問題設定*. EveMissLab.

---

# Canonical Note

本文件之正式原始碼使用 UTF-8 編碼。

數學原始碼只使用 canonical delimiters：

- inline math：` $...$ `
- display math：`$$...$$`

不進行 unicode_escape 類 round-trip；不把 LaTeX 轉成 Unicode 數學字元後再作為 canonical source；不以聊天渲染畫面作為正式原稿。
