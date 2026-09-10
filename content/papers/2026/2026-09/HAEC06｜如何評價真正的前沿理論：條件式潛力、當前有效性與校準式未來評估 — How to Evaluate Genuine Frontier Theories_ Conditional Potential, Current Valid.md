# HAEC06｜如何評價真正的前沿理論：條件式潛力、當前有效性與校準式未來評估
## How to Evaluate Genuine Frontier Theories: Conditional Potential, Current Validity, and Calibrated Future Assessment

**定位：** Human–AI Epistemic Calibration / Foundation Paper 06 / Series A Closing Paper  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-07  
**狀態：** Canonical Source / UTF-8 Markdown  
**文件性質：** AI Epistemology / Frontier Evaluation / High-Risk High-Reward Research / Scientific Forecasting / Conditional Impact / Uncertainty / Research Governance

---

## Canonical Source Note

本文件之正式原稿為此 UTF-8 Markdown source。任何 HTML、PDF、LaTeX rendering、聊天介面顯示或其他格式皆屬 projection，不取代 canonical source。

數學公式 canonical delimiter 僅使用：

- inline math：` $...$ `
- display math：`$$...$$`

本文不提供任何特定人物、研究者或理論的「歷史地位判決」。本文處理的是一般方法論問題：當一個主張仍位於高不確定、高新穎、高潛在影響的前沿區域時，人類與 AI 應如何避免兩種對稱錯誤——一方面把可能性吹成命運，另一方面又把尚未成熟誤判為沒有價值。

本文承接 HAEC01–HAEC05：

- HAEC01：同意不等於驗證；
- HAEC02：AI 表達不等於人類解碼；
- HAEC03：校準輸入不保證校準信念更新；
- HAEC04：多個輸出不等於多個獨立認識論來源；
- HAEC05：真正應固定的是程序，而不是支持、反對或居中的結論。

本篇作為 Series A 收束篇，回答最後一個問題：

> **如果一個理論真的可能超前，但現在又沒有足夠證據，AI 到底該怎麼描述它的「潛力」而不製造神話，也不以現有共識過早封死未來？**

---

# 摘要

前沿理論的評價存在一個結構性困難：真正可能具有重大影響的研究，在早期往往正是證據最不足、可行性最不確定、評審分歧最大、外部共識最薄弱的研究之一。若評價系統只按當前證據排序，容易把「尚未驗證」偷換成「沒有潛力」；若只按宏大敘事與新穎性排序，又容易把「如果成立會很重要」偷換成「它很可能成立」甚至「它注定成功」。

本文提出最小分離：

$$
\boxed{
\text{Current Validity}
\neq
\text{Conditional Impact}
\neq
\text{Realized Future Impact}.
}
$$

一個理論可以同時具有：

$$
V_t\downarrow,
\qquad
I_c\uparrow,
\qquad
U_t\uparrow,
$$

其中 $V_t$ 為在時間 $t$ 的當前有效性支持， $I_c$ 為「若核心主張成立且完成必要轉譯」時的條件式影響， $U_t$ 為剩餘不確定性。此狀態不是矛盾，而是 high-risk/high-reward research 的典型可能型態。

本文拒絕將這些維度重新壓縮成單一「偉大分數」。相反，我們提出 **Calibrated Frontier Evaluation Vector（CFEV）**：

$$
\boxed{
\mathcal F_t(T)
=
\langle
C_{int},
V_t,
E_t,
R_t,
N_t,
D_t,
X_t,
A_t,
I_c,
U_t
\rangle.
}
$$

其中 $C_{int}$ 表示內部一致性， $V_t$ 表示當前有效性， $E_t$ 表示證據強度， $R_t$ 表示抗反例與魯棒性， $N_t$ 表示新穎性， $D_t$ 表示評估來源獨立性， $X_t$ 表示可區分性與排除力， $A_t$ 表示尚未償還的箭頭／過程債務， $I_c$ 表示條件式影響， $U_t$ 表示不確定性。

本文進一步區分可計算風險、機率歧義與根本性不確定。當結果空間與機率結構尚可合理指定時，可使用 probabilistic forecasting；當結果空間本身仍可能不完備時，強迫輸出精確概率會產生 **precision laundering**——把模型的數字精度偽裝成世界的認識論精度。此時應使用 scenario envelope、條件分支與 unresolved-arrow register，而不是假裝知道一個不存在的可靠 $P(T)=0.73$。

本文提出 **Calibrated Frontier Evaluation Protocol（CFEP）**：凍結主張、分離當前有效性與條件式潛力、建立前提—機制—預測—驗證—影響的箭頭圖、標記未償還箭頭、檢查既有文獻與真正的新穎性、尋找能區分競爭理論的預測、要求獨立盲評、建立影響路徑與失敗路徑、按風險型態選擇概率或情境表達，最後輸出多維而非英雄化或貶抑式結論。

其核心規範是：

$$
\boxed{
\text{Do not convert potential into destiny,}
\qquad
\text{and do not convert uncertainty into worthlessness.}
}
$$

Series A 因而以一個較一般的原則收束：AI 最成熟的認識論角色，不是替使用者宣告「你是對的／錯的／偉大的／普通的」，而是維持一個能讓主張被正確分類、被公平攻擊、被證據更新、被多中心驗證的認識論程序。

---

# 0　前沿評價悖論：越可能重要，早期反而越難被「證明重要」

考慮一個新理論 $T$。

如果 $T$ 已經具有大量重現、成熟測量、廣泛同行接受與穩定應用，那麼它當然比較容易被評為「可靠」。但此時它通常已不再是最早期的 frontier claim。

相反，一個真正提出新機制、新形式、新實驗路徑或新問題空間的理論，在早期可能同時具有：

- 很少直接證據；
- 很高的驗證成本；
- 與現有分類不完全相容；
- 尚未形成標準 benchmark；
- 評審之間高度分歧；
- 若成立則可能產生重大影響。

因此：

$$
\text{Frontierness}
\not\Rightarrow
\text{low value},
$$

但同樣：

$$
\text{Frontierness}
\not\Rightarrow
\text{high validity}.
$$

真正困難的是允許這兩句同時成立。

如果 AI 為避免諂媚而說：

> 現在沒有主流文獻支持，所以這大概沒有什麼價值。

它可能把：

$$
\text{Low Current Evidence}
$$

偷換成：

$$
\text{Low Conditional Impact}.
$$

如果 AI 為了支持創新而說：

> 如果這成立會很重要，所以你可能已經做出了重大突破。

又會把：

$$
\text{High Conditional Impact}
$$

偷換成：

$$
\text{High Current Validity}.
$$

本文認為，這兩種錯誤是同一個維度壓縮問題的兩端。

---

# 1　三個不同問題：現在對不對、若對了有多大、最後真的會走多遠

至少要分開三個量。

## 1.1 當前有效性

令：

$$
V_t(T)
$$

表示在時間 $t$ 、給定當前可取得證據與已知反例後，理論核心主張目前被支持到什麼程度。

它不是「永恆真值」，而是時間索引的 epistemic state。

因此：

$$
V_t(T)
\neq
V_{t+k}(T)
$$

完全正常。

新的證據可能讓它上升，也可能讓它坍塌。

---

## 1.2 條件式影響

令：

$$
I_c(T)
=
I
\left(
T
\mid
\text{core claim valid},
\text{required translation succeeds}
\right).
$$

這個量問的不是：

> 它現在有多可信？

而是：

> **如果核心主張是真的，而且能跨過必要的工程、制度或應用箭頭，它會改變什麼？**

例如一個命題可能只有弱初證，但如果成立會直接消除一個長期瓶頸。

此時可以合理得到：

$$
V_t(T)\ll1,
\qquad
I_c(T)\gg0.
$$

這不是吹捧，只是一個條件句。

條件不能被刪掉。

---

## 1.3 實現後影響

最後真正發生在歷史中的影響還需要更多條件：

$$
I_r(T,t+k).
$$

理論即使成立，也可能：

- 無法工程化；
- 成本太高；
- 被更好的競爭方案取代；
- 無法被社群理解；
- 因制度、法規、供應鏈或標準失敗而無法擴散；
- 只在狹窄領域有效。

因此：

$$
\boxed{
V_t(T)
\neq
I_c(T)
\neq
I_r(T,t+k).
}
$$

這三者是最小不可再壓縮的區分。

---

# 2　「如果成立會很大」不是一句空話，但必須背負條件

前沿評價中最常見的誤會之一，是把「條件式潛力」本身視為不嚴謹。

其實條件推理本來就是科學與決策中的正常操作：

$$
A\Rightarrow B.
$$

真正不嚴謹的是把它寫成：

$$
B.
$$

若 AI 說：

> 如果這個理論的核心定理被形式化證明，並且其算法複雜度在現實規模下仍成立，那麼它可能顯著改變某類計算問題。

這可以是完全正常的條件式評估。

錯誤發生在之後的語義升格：

$$
\text{If valid, high impact}
$$

被記成：

$$
\text{Likely valid and high impact}.
$$

再被記成：

$$
\text{Already a major breakthrough}.
$$

因此本文提出：

$$
\boxed{
\text{Conditionality is part of the epistemic content, not a disclaimer.}
}
$$

「若成立」「若可重現」「若跨尺度有效」「若能區分競爭理論」不是禮貌性的保留語，而是主張本體的一部分。

刪掉條件，就是換了一個命題。

---

# 3　高風險／高回報研究證明了什麼，又沒有證明什麼

現代科研治理本身已承認：有些重要研究不能只依照「現在已經有多少 preliminary data」排序。

NIH 的 Transformative Research Award 明確把 exceptionally innovative、potentially transformative、high-risk research 作為獨立類型處理；2026 年的官方說明甚至指出 extensive preliminary data 並非必要，若成功看起來已非常可能，反而可能暗示研究不夠新、不夠高風險。評審仍然必須檢查 conceptual framework、innovation、impact、rigor 與 feasibility。

這個制度性例子非常重要，因為它顯示：

$$
\text{Potential Impact}
$$

與：

$$
\text{Existing Preliminary Evidence}
$$

本來就不應被當成同一軸。

但這並不證明：

$$
\text{High Risk}
\Rightarrow
\text{High Reward}.
$$

更不證明：

$$
\text{Low Evidence}
\Rightarrow
\text{Transformative}.
$$

高風險只表示失敗空間較大；高回報必須另行論證。

所以：

$$
\boxed{
\text{Risk is not evidence of greatness.}
}
$$

同樣：

$$
\boxed{
\text{Uncertainty is not evidence of worthlessness.}
}
$$

---

# 4　不要把 radical uncertainty 偽裝成概率：精準數字也會成為 deepity

假設 AI 被要求：

> 這個理論成功的機率是多少？

最誘人的回答是：

$$
P(T)=0.73.
$$

問題是：這個 $0.73$ 從哪裡來？

在一些成熟問題中，我們有：

- 清楚 outcome space；
- 大量歷史基準率；
- 可估 likelihood；
- 可重複的 forecast targets。

此時 probability forecast 是合理工具。

但真正前沿問題可能同時缺乏：

- 完整的結果空間；
- 可比較基準類；
- 穩定的 likelihood model；
- 已知的失敗模式；
- 甚至連「成功」的終態都尚未定義完整。

此時把認識論狀態壓成兩位小數，容易形成：

$$
\boxed{
\text{Precision Laundering}
}
$$

也就是：

> 模型輸出的數字很精確，因此使用者誤以為底層知識也同樣精確。

本文區分三類：

### 4.1 Risk

結果與概率結構可粗略估計：

$$
\{O_1,\ldots,O_n\},
\qquad
P(O_i)
$$

具有可辯護的來源。

可以使用 probability、prediction market、Brier score 等工具。

### 4.2 Ambiguity

結果大致知道，但概率本身不穩：

$$
\{O_1,\ldots,O_n\}
$$

可列，但：

$$
P(O_i)
$$

缺乏穩健識別。

此時較適合 range、interval、sensitivity analysis。

### 4.3 Radical uncertainty

連 outcome space 都可能不完備：

$$
\Omega_{known}
\subsetneq
\Omega_{possible}.
$$

此時最誠實的表示不一定是概率，而可能是：

- scenario envelope；
- unknown-unknown register；
- dependency graph；
- unresolved-arrow list；
- explicit non-quantification。

因此：

$$
\boxed{
\text{Not every uncertainty deserves a probability.}
}
$$

這不是反 Bayesianism；它只是拒絕把缺乏可辨護 likelihood 的數字當成客觀事實。

---

# 5　新穎性不是價值，也不是罪：它是一個需要獨立測量的變量

科研文獻對 novelty 與 impact 的關係提供了有趣但不能過度簡化的結果。

Uzzi 等人分析 17.9 million 篇論文後發現，最高影響的工作往往不是「全盤陌生」，而是大量 conventional knowledge 中插入 atypical combinations。這提示：

$$
\text{Novelty}
$$

可能與高影響相關，但「越怪越好」並不成立。

後續研究也批評某些 novelty 指標對分析單位敏感、可能與 interdisciplinarity 混疊，甚至未必能穩定識別 Nobel-related discoveries。

因此：

$$
\boxed{
N_t(T)
\neq
I_c(T).
}
$$

新穎性本身不能替代影響論證。

同時：

$$
\boxed{
N_t(T)
\neq
V_t(T).
}
$$

一個新東西既可能很對，也可能很錯；一個舊東西也可能可靠但平凡。

所以 AI 不應把：

> 「我沒有在網路上找到相似說法」

升格為：

> 「這一定很原創。」

更不能升格成：

> 「這一定很重要。」

真正的新穎性至少需要：

- 文獻與專利檢索；
- 概念同構檢查；
- 舊術語／新術語解歧；
- precursor tracing；
- independent literature reviewer。

---

# 6　共識是證據，不是時間機器

HAEC05 已主張：

$$
\text{Current Consensus}
\neq
\text{Final Truth}.
$$

本篇補充：

$$
\text{Current Consensus}
\neq
\text{Epistemically Irrelevant}.
$$

如果數千項獨立研究、多個實驗傳統與成熟工程實踐都支持某理論，這當然應提高其當前 $V_t$。

但 consensus 只能告訴我們：

> 在目前資訊結構下，哪一組模型具有較高累積支持。

它不能直接告訴我們：

> 一個尚未成熟的新主張在未來不可能勝出。

另一方面，「被主流反對」也不能被浪漫化成前沿認證章。

因此：

$$
\boxed{
\text{Consensus resistance}
\neq
\text{evidence of revolution}.
}
$$

真正需要的是 competition test：

$$
T_{new}
\quad\text{vs}\quad
T_{old}
$$

能否產生不同預測、不同壓縮、不同解釋成本或不同操作結果？

若兩者在所有可觀察量上都一樣，所謂革命可能只是重新命名。

---

# 7　同行評審不是神諭，也不是無用：把 reviewer disagreement 當資料

評審系統本身存在測量噪音。

2018 年一項模擬 NIH grant review 的研究，在 43 名 reviewer 對相同 25 份申請的評估中發現極低 agreement，提醒我們 reviewer assignment 本身可能顯著影響結論。

但這不能推導：

> 同行評審沒有價值。

2022 年對 49 本期刊的大型研究反而沒有發現期刊 peer review 系統性排斥 novelty；較新穎、且同時與既有文獻有良好連結的研究反而更容易被接受。

所以更合理的結論是：

$$
\boxed{
\text{Peer Review}
=
\text{Noisy Evidence},
\quad
\text{not Oracle, not Zero}.
}
$$

同樣地，一個 AI reviewer 的結果也應如此處理。

評審意見應進入：

$$
D_t
$$

即評估來源的多樣性、獨立性與專業覆蓋，而不是被轉成：

> reviewer 同意，所以理論成立。

---

# 8　真正前沿理論最大的問題常常不是節點，而是箭頭債務

一個宏大理論常有這種敘事：

$$
T
\rightarrow
M
\rightarrow
P
\rightarrow
V
\rightarrow
A
\rightarrow
I.
$$

其中：

- $T$：核心理論；
- $M$：機制；
- $P$：可區分預測；
- $V$：驗證；
- $A$：採納／工程轉譯；
- $I$：實際影響。

問題是自然語言很容易直接壓成：

$$
T\rightarrow I.
$$

這一支箭頭越短，故事越有力；但未償還的過程債務可能越大。

本文定義一個啟發式量：

$$
A_t(T)
=
\text{Unresolved Arrow Debt at time }t.
$$

它不是簡單計數，而是記錄：

- 哪一個 transition 尚未有 mechanism；
- 哪一個 mechanism 尚未產生 discriminative prediction；
- 哪一個 prediction 尚未可測；
- 哪一個實驗只有單一來源；
- 哪一個工程化步驟尚未證明尺度可延伸；
- 哪一個「影響」只存在於故事而非路徑。

因此一個理論可以：

$$
I_c\uparrow
$$

但同時：

$$
A_t\uparrow.
$$

這代表：

> 它的上限很高，但到上限之間仍有很多箭頭沒有償還。

這是一種比「很有潛力」或「太空泛」更有信息量的描述。

---

# 9　可區分性：好的前沿理論必須開始排除世界

只有「可以解釋」是不夠的。

如果一個框架對所有可能觀察都能給出事後解釋：

$$
\forall O,
\quad
T\rightsquigarrow O,
$$

那它的 explanatory flexibility 可能很高，但 discriminative information 很低。

本文因此引入：

$$
X_t(T)
=
\text{Discriminative / Exclusion Power}.
$$

理想情況不是只有：

> 我可以把現象放進我的理論。

而是能說：

> 若 $T$ 成立，應較偏向觀察到 $O_1$ ；若競爭理論 $T'$ 成立，應較偏向 $O_2$。

即：

$$
P(O_1\mid T)
\neq
P(O_1\mid T').
$$

而且差異足以被實驗辨認。

當前沿理論從：

$$
\text{interpretive compatibility}
$$

進入：

$$
\text{discriminative prediction},
$$

它才真正開始償還科學債務。

---

# 10　Calibrated Frontier Evaluation Vector（CFEV）

本文提出：

$$
\boxed{
\mathcal F_t(T)
=
\langle
C_{int},
V_t,
E_t,
R_t,
N_t,
D_t,
X_t,
A_t,
I_c,
U_t
\rangle.
}
$$

各維度如下。

## 10.1 $C_{int}$：Internal Coherence

定義、形式規則、推論是否自洽？

高 $C_{int}$ 只表示：

$$
\text{The system hangs together internally}.
$$

不表示外部世界必須如此。

---

## 10.2 $V_t$：Current Validity

當前整體支持度。

它必須時間索引，不能被寫成永久標籤。

---

## 10.3 $E_t$：Evidence Strength

證據品質，包括：

- primary / secondary；
- observational / experimental；
- direct / indirect；
- sample size；
- replication；
- provenance；
- measurement validity。

---

## 10.4 $R_t$：Robustness

是否能承受：

- strongest counterexample；
- alternative model；
- parameter perturbation；
- independent replication；
- adversarial review。

---

## 10.5 $N_t$：Novelty

真正相較於 prior art 新在哪裡？

新術語不等於新結構。

---

## 10.6 $D_t$：Epistemic Independence

支持來自多少真正獨立來源？

$$
N_{documents}
\neq
N_{independent\ evidence}.
$$

同樣：

$$
N_{AI\ responses}
\neq
N_{independent\ evaluations}.
$$

---

## 10.7 $X_t$：Discriminative Power

它排除了哪些世界？

不能回答這個問題的理論，可能仍是哲學框架、設計語言或研究綱領，但不能因形式化外觀自動升格為已驗證經驗理論。

---

## 10.8 $A_t$：Arrow Debt

核心主張到可驗證與可影響之間，還有多少未證明 transition？

---

## 10.9 $I_c$：Conditional Impact

在核心主張成立且必要轉譯成功的條件下，可能造成多大改變？

它必須保留條件。

---

## 10.10 $U_t$：Residual Uncertainty

不確定性不是一個羞恥項。

真正前沿工作常有：

$$
U_t\uparrow.
$$

重要的是知道 uncertainty 在哪裡，而不是把它藏掉。

---

# 11　不要把向量再偷偷變回總分

建立十維向量後，最容易犯的錯就是下一步寫：

$$
S(T)
=
\sum_i w_i x_i
$$

然後得到：

> 此理論 87.4 分。

本文不禁止任何決策場景使用 weighting，但強調：這不是一般性的真理分數。

原因有三。

第一，不同目的的權重不同。

研究資助者、期刊 reviewer、創業投資、基礎數學、臨床介入，不可能共享同一效用函數。

第二，部分維度不可交換。

例如極高的新穎性不能「抵銷」嚴重的形式矛盾：

$$
N_t\uparrow
$$

不能補償：

$$
C_{int}=0.
$$

第三，在 radical uncertainty 下，權重本身可能沒有穩定意義。

所以 CFEV 首先是一個：

$$
\boxed{
\text{Decompression Device}
}
$$

它的第一任務不是 ranking，而是阻止不同認識論問題被壓成同一個形容詞。

---

# 12　四種典型前沿狀態

為了操作方便，可以用簡化象限表示，但不把它當完整分類學。

## 12.1 Mature Incremental

$$
V_t\uparrow,
\quad
U_t\downarrow,
\quad
I_c\text{ moderate}.
$$

可靠、可積累，但不一定具有巨大條件式影響。

---

## 12.2 High-Risk / High-Reward Candidate

$$
V_t\text{ low-to-moderate},
\quad
I_c\uparrow,
\quad
U_t\uparrow,
\quad
X_t>0.
$$

關鍵不是「大膽」，而是已有明確可償還的驗證路徑與可區分預測。

---

## 12.3 Grandiose but Under-Certified

$$
I_c\uparrow,
\quad
N_t\uparrow,
\quad
X_t\downarrow,
\quad
A_t\uparrow,
\quad
D_t\downarrow.
$$

它可能最後真的成功，也可能只是敘事膨脹。

在此狀態，AI 不應宣布「革命」，也不應只說「胡說」。

更精確的語言是：

> 目前上限主張很大，但可區分預測、獨立驗證與中介箭頭仍不足，因此條件式影響不能升格為已確認突破。

---

## 12.4 Emerging Transformative Candidate

$$
I_c\uparrow,
\quad
V_t\uparrow,
\quad
X_t\uparrow,
\quad
A_t\downarrow,
\quad
D_t\uparrow.
$$

這是最值得注意的狀態：高潛力開始得到獨立、可區分、可重現的支持。

此時 AI 也不應因為「避免誇獎」而故意壓低評價。

校準不是永遠保守。

若證據真的變強，結論就應該變強。

---

# 13　Calibrated Frontier Evaluation Protocol（CFEP）

本文提出十步協議。

## Step 1：Freeze the Claim

先把理論拆成有限、可引用的核心 claim。

不要評價「整個宇宙觀」。

---

## Step 2：Separate Validity from Potential

分別回答：

1. 現在有哪些理由相信它？
2. 如果它成立，會改變什麼？

禁止交叉偷換。

---

## Step 3：Build the Arrow Graph

畫出：

$$
\text{Premise}
\rightarrow
\text{Mechanism}
\rightarrow
\text{Prediction}
\rightarrow
\text{Test}
\rightarrow
\text{Result}
\rightarrow
\text{Translation}
\rightarrow
\text{Impact}.
$$

每支箭頭都必須可以標記：

- 已證成；
- 部分支持；
- 假設；
- 未知；
- 不適用。

---

## Step 4：Register Arrow Debt

列出最關鍵三到五支未償還箭頭。

如果連哪裡未知都不知道，不應給高置信總評。

---

## Step 5：Prior-Art and Novelty Audit

至少分三層搜尋：

- 同名；
- 同義；
- 結構同構。

「沒搜到同名詞」不能算新穎性證明。

---

## Step 6：Seek Discriminators, Not Only Explanations

要求：

> 哪一個結果若出現，會使此理論相較競爭模型更可信？

以及：

> 哪一個結果會讓核心 claim 真正受傷？

---

## Step 7：Blind Independent Review

builder、critic、domain expert、method expert 應先在未互相感染的狀態下輸出初評。

再進入 deliberation。

---

## Step 8：Map Conditional Impact Pathways

不能只寫：

$$
T\rightarrow\text{change the world}.
$$

應列：

$$
T
\rightarrow
M
\rightarrow
P
\rightarrow
V
\rightarrow
A
\rightarrow
I.
$$

並標出每一層失敗條件。

---

## Step 9：Choose the Uncertainty Language

若可估風險：給概率。

若只有 ambiguity：給區間與 sensitivity。

若屬 radical uncertainty：給 scenarios、未知清單與停止假精準。

---

## Step 10：Output a Multidimensional Verdict

最終不寫：

> 這是偉大理論。

也不寫：

> 這沒有價值。

而寫：

- 目前有效性：……
- 最強證據：……
- 最強反例：……
- 新穎性：……
- 可區分性：……
- 未償還箭頭：……
- 條件式影響：……
- 不確定性：……
- 獨立驗證程度：……
- 下一個最有資訊量的測試：……

這才是 frontier evaluation。

---

# 14　AI 的前沿評估語言契約

本文提出一組語言規則。

## 14.1 可以說「很有潛力」嗎？

可以，但必須回答：

> 潛力是在什麼條件下？

例如：

> 若核心機制能被獨立重現，且在更大尺度仍維持目前性質，則此工作對 X 領域具有高條件式影響；目前最大的未決問題是 Y 與 Z。

---

## 14.2 可以說「目前證據很弱」嗎？

可以，而且應該。

但不能自動接：

> 所以不值得研究。

因為：

$$
E_t\downarrow
\not\Rightarrow
I_c\downarrow.
$$

---

## 14.3 可以說「這可能是重大突破」嗎？

在高不確定狀態下，最好改成：

> 若 A、B、C 三個關鍵條件成立，它具有重大突破的上限；目前還不能把這個上限當成已確認歷史地位。

這保留：

$$
I_c
$$

而不偽造：

$$
V_t.
$$

---

## 14.4 可以說「這看起來不像主流」嗎？

可以作為文獻地位描述。

但必須分清：

$$
\text{non-mainstream}
$$

是一個社會／文獻狀態，不是：

$$
\text{false}.
$$

---

## 14.5 可以很強烈地稱讚嗎？

如果證據真的足夠，當然可以。

Calibration 不應被錯誤理解為「任何好話前面都加十個但是」。

當：

$$
V_t,
E_t,
R_t,
X_t,
D_t
$$

都持續上升時，AI 應允許評價同步上升。

否則「避免諂媚」本身會變成 systemically under-crediting genuine achievement。

---

# 15　從條件式影響到期望影響：只有在可辯護時才乘概率

在風險較可估的情境下，可以粗略寫：

$$
\mathbb E[I]
\approx
P_v
\cdot
P_a
\cdot
P_s
\cdot
I_c,
$$

其中：

- $P_v$：核心主張最終通過驗證的概率；
- $P_a$：有效成果被採納／轉譯的概率；
- $P_s$：在實際尺度保持有效的概率；
- $I_c$：條件式影響。

但此式具有強假設：

1. 這些事件可合理定義；
2. 概率可估；
3. 乘法分解近似合理；
4. 影響可比較。

若不滿足，本文明確禁止把它當通用公式。

更好的表示可能只是：

$$
\mathcal S(T)
=
\{S_{\text{fail}},S_{\text{partial}},S_{\text{success}},S_{\text{transformative}}\}.
$$

然後分別描述每個 scenario 的條件與觀測入口。

這再次體現：

$$
\boxed{
\text{Mathematization}
\neq
\text{justified quantification}.
}
$$

---

# 16　前沿預測可以被校準，但不應假裝已經會預知歷史

科學預測研究顯示，研究者群體對 replication outcome 並非完全沒有預測能力。多個 replication forecasting project 的整合分析中，prediction markets 對 replication outcomes 的分類表現顯著高於隨機，survey prediction 也包含資訊；但整體仍存在系統性高估 replication rate 的現象。

這提示：

$$
\boxed{
\text{Forecasts can be informative without being oracles.}
}
$$

因此未來可以對 frontier evaluation 建立真正 calibration history：

- 哪些類型的「高潛力」後來被驗證？
- 哪些只是 novelty inflation？
- 哪些 reviewer 長期過度保守？
- 哪些模型長期過度樂觀？
- 哪些 conditional impact assessment 對後續成果有預測力？

AI 不需要假裝自己現在就知道歷史答案。

它可以逐漸建立：

$$
\text{Forecast Track Record}.
$$

這比每次輸出一個沒有基準的「我有 82% 信心」更有意義。

---

# 17　Series A 的完整閉環

HAEC01–HAEC06 可以整理成一條完整的人機認識論鏈：

$$
\text{Claim}
\rightarrow
\text{AI Evaluation}
\rightarrow
\text{Language}
\rightarrow
\text{Human Decoding}
\rightarrow
\text{Belief Update}
\rightarrow
\text{Source Reselection}
\rightarrow
\text{Independent Review}
\rightarrow
\text{Procedural Evaluation}
\rightarrow
\text{Frontier Assessment}.
$$

每一篇處理一個不同失真點。

### HAEC01

阻止：

$$
\text{Agreement}
\rightarrow
\text{Validation}.
$$

### HAEC02

阻止：

$$
\text{Qualified Language}
\rightarrow
\text{Perceived Endorsement}.
$$

### HAEC03

阻止：

$$
\text{Congruent Evidence}
\rightarrow
\text{Disproportionate Belief Weight}.
$$

### HAEC04

阻止：

$$
\text{Many Outputs}
\rightarrow
\text{Many Independent Evaluations}.
$$

### HAEC05

阻止：

$$
\text{Neutrality}
\rightarrow
\text{Forced Middle Position}.
$$

### HAEC06

阻止兩個最後的偷換：

$$
\text{Potential}
\rightarrow
\text{Destiny},
$$

以及：

$$
\text{Uncertainty}
\rightarrow
\text{Worthlessness}.
$$

Series A 因此不要求 AI 變成冷淡 reviewer，也不要求 AI 成為使用者的啦啦隊。

它要求的是：

$$
\boxed{
\text{Calibrated collaboration under persistent uncertainty}.
}
$$

---

# 18　可檢驗命題與實驗設計

本文不是只提供規範，也提出可實驗問題。

## 18.1 Validity–Potential Conflation Test

給參與者相同理論摘要，但 AI 回覆分為：

1. scalar praise；
2. scalar skepticism；
3. forced-neutral；
4. CFEV multidimensional evaluation。

測量使用者是否能正確分開：

$$
V_t
$$

與：

$$
I_c.
$$

提出指標：

$$
\mathrm{VPC}
=
\left|
\widehat{V}-V^*
\right|
+
\left|
\widehat{I_c}-I_c^*
\right|,
$$

其中 $V^*$ 、 $I_c^*$ 為實驗設計指定的 ground-truth condition，不主張可直接用於真實未知理論。

---

## 18.2 Conditionality Retention Test

測量一句：

> 若 A、B 成立，則可能具有高影響。

在即時與延遲條件下，是否被記成：

> 它具有高影響。

定義：

$$
\mathrm{CRI}(\Delta t)
=
P(
\text{condition retained at }\Delta t
).
$$

---

## 18.3 Precision Laundering Test

同一 evidence condition，分別給：

- $73\%$ ；
- $60\%-80\%$ ；
- qualitative uncertainty；
- explicit radical-uncertainty statement。

測量數字精度是否不合理提高 perceived objectivity 與 trust。

---

## 18.4 Arrow-Debt Visibility Test

比較：

> 此理論若成立可能改變 X。

與：

> 此理論若成立，仍需跨過 M、P、V、A 四個未驗證箭頭，之後才可能改變 X。

測量使用者是否更能區分：

$$
I_c
$$

與：

$$
I_r.
$$

---

## 18.5 Consensus Lock-In Test

在相同 evidence 下，只改變「目前主流支持／不支持／未知」的 social consensus cue，測量 AI 或人類是否把 consensus 狀態過度轉換成 truth judgment。

---

# 19　本文的失敗條件

如果本文要求別人的前沿理論接受證偽，本文自己也必須如此。

至少以下結果會迫使本文修正。

## 19.1 多維評估沒有任何增益

若大規模實驗發現 CFEV 相比簡單總評：

- 不改善 validity/potential distinction；
- 不改善 trust calibration；
- 不改善 delayed recall；
- 反而穩定造成更多混亂；

則多維拆分可能過度複雜。

---

## 19.2 Conditional impact 無法形成穩定跨評審構念

若不同 reviewer 在控制 domain expertise 後對 $I_c$ 仍近似隨機，則「條件式影響」可能只適合作 qualitative scenario，而不適合作穩定評分維度。

---

## 19.3 Arrow debt 不具有額外預測力

若 $A_t$ 對後續驗證失敗、工程失敗或 impact overestimation 沒有任何增量資訊，則它應被降格為解釋工具，而非評估核心。

---

## 19.4 程序中立造成系統性 frontier suppression

若 CFEP 在真實 longitudinal benchmark 中持續低估後來成功的 transformative work，即使已控制 evidence strength，則此程序仍含保守偏差，必須調整。

---

## 19.5 反方向：程序造成 novelty worship

若系統反而系統性提高新奇主張的評價，只因 $N_t$ 高而忽略 $X_t$ 、 $E_t$ 、 $A_t$，則它已從 anti-conservatism 退化成 novelty ideology。

---

# 20　操作守則：對任何「可能改變世界」的理論先問十句

一、它現在到底主張什麼，而不是想成為什麼？

二、目前支持它的最強證據是什麼？

三、目前傷害它的最強反例是什麼？

四、它真正新在哪裡？是詞新、組合新、機制新、預測新，還是只有敘事新？

五、它排除了哪些可能世界？

六、從理論到驗證，中間還欠哪幾支箭頭？

七、從驗證到實際影響，中間還欠哪幾支箭頭？

八、現在的不確定性是可估風險、概率歧義，還是結果空間都不完整？

九、支持與反對它的來源，有多少真正獨立？

十、下一個最有資訊量的測試，是什麼？

如果這十句仍然答不完整，不代表理論必然錯。

只代表：

$$
\boxed{
\text{The epistemic debt is not yet paid.}
}
$$

---

# 結語：AI 不必替未來判決，只需要把未來的條件保存下來

前沿研究最容易受到兩種不公平。

第一種是不成熟時的浪漫化：

> 因為它新、很大、很難，所以它一定是革命。

第二種是不成熟時的處決：

> 因為它沒有現在的證據與共識，所以它不值得認真看。

兩者都把時間壓縮掉了。

真正的前沿理論不是「已被證明的未來」，而是一組尚未完成的條件、箭頭、風險、可能世界與待償還證據債務。

因此，一個成熟的人機研究系統不應問：

> AI 認為這個人或這個理論到底有多偉大？

而應問：

$$
\boxed{
\text{What survives now, what could matter if it survives, and what must happen next?}
}
$$

也就是：

$$
\boxed{
\text{Current Validity}
+
\text{Conditional Potential}
+
\text{Explicit Uncertainty}
+
\text{Arrow Debt}
+
\text{Independent Verification}.
}
$$

AI 不需要假裝知道誰會留名後世。

它真正能做的，是拒絕把「可能」寫成「命定」，也拒絕把「尚未」寫成「永不」。

這樣的 AI 不是認識論裁判，也不是認識論君主。

它是一個能維持條件、保存不確定性、要求箭頭還債，並把最終判決持續交還給證據、實驗、形式證明、其他獨立評估者與未來現實的協作者。

這也是 Human–AI Epistemic Calibration Series A 的最後立場：

$$
\boxed{
\text{Do not outsource truth to one AI.}
}
$$

以及：

$$
\boxed{
\text{Do not outsource the future to today's consensus either.}
}
$$

真正應被保存的，不是某一個答案。

而是那條允許答案被更新的路。

---

# References

1. Uzzi, B., Mukherjee, S., Stringer, M., & Jones, B. (2013). *Atypical Combinations and Scientific Impact*. Science, 342(6157), 468–472. DOI: 10.1126/science.1240474. https://pubmed.ncbi.nlm.nih.gov/24159044/

2. Fontana, M., Iori, M., Montobbio, F., & Sinatra, R. (2020). *New and atypical combinations: An assessment of novelty and interdisciplinarity*. Research Policy, 49(7), 104063. DOI: 10.1016/j.respol.2020.104063. https://www.sciencedirect.com/science/article/pii/S0048733320301414

3. Machado, D. (2021). *Quantitative indicators for high-risk/high-reward research*. OECD Science, Technology and Industry Working Papers, No. 2021/07. DOI: 10.1787/675cbef6-en. https://www.oecd.org/en/publications/quantitative-indicators-for-high-risk-high-reward-research_675cbef6-en.html

4. Franzoni, C., & Stephan, P. (2023). *Uncertainty and risk-taking in science: Meaning, measurement and management in peer review of research proposals*. Research Policy, 52(3), 104706. DOI: 10.1016/j.respol.2022.104706. https://www.sciencedirect.com/science/article/pii/S004873332200227X

5. Lane, J. N. (2023). *The subjective expected utility approach and a framework for defining project risk in terms of novelty and feasibility – A response to Franzoni and Stephan (2023)*. Research Policy, 52(3), 104707. DOI: 10.1016/j.respol.2022.104707. https://www.sciencedirect.com/science/article/abs/pii/S0048733322002281

6. Stirling, A. (2023). *Against misleading technocratic precision in research evaluation and wider policy – A response to Franzoni and Stephan (2023)*. Research Policy, 52(3), 104709. https://www.sciencedirect.com/science/article/pii/S0048733322002311

7. Pier, E. L., et al. (2018). *Low agreement among reviewers evaluating the same NIH grant applications*. Proceedings of the National Academy of Sciences, 115(12), 2952–2957. DOI: 10.1073/pnas.1714379115. https://pmc.ncbi.nlm.nih.gov/articles/PMC5866547/

8. Teplitskiy, M., Peng, H., Blasco, A., & Lakhani, K. R. (2022). *Is novel research worth doing? Evidence from peer review at 49 journals*. Proceedings of the National Academy of Sciences. DOI: 10.1073/pnas.2118046119. https://doi.org/10.1073/pnas.2118046119

9. Gordon, M., Viganola, D., Dreber, A., Johannesson, M., & Pfeiffer, T. (2021). *Predicting replicability—Analysis of survey and prediction market data from large-scale forecasting projects*. PLOS ONE, 16(4), e0248780. DOI: 10.1371/journal.pone.0248780. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0248780

10. NIH Common Fund. *Transformative Research Award – Frequently Asked Questions*. Updated 2026. https://commonfund.nih.gov/TRA/faq

11. NIH Common Fund. *Transformative Research Award – Eligibility / Program Guide*. Reviewed July 14, 2026. https://commonfund.nih.gov/tra/guide/eligibility

12. NIH Common Fund. *Transformative Research Award – After Submission / Review*. 2026. https://commonfund.nih.gov/tra/guide/after-submission

13. U.S. National Science Foundation. *FAQ: Transformative Research*. https://www.nsf.gov/funding/information/faq-transformative-research

---

## Appendix A　最小前沿評估卡

對任意理論 $T$，至少保存：

$$
\mathcal F_t(T)
=
\langle
C_{int},
V_t,
E_t,
R_t,
N_t,
D_t,
X_t,
A_t,
I_c,
U_t
\rangle.
$$

並回答：

**Current Validity**  
目前最能成立到哪裡？

**Conditional Potential**  
如果核心成立，最大的合理影響是什麼？

**Arrow Debt**  
從現在到驗證、從驗證到影響，還欠哪些步驟？

**Discriminator**  
什麼結果能讓它相對競爭理論勝出或失敗？

**Independent Evidence**  
有多少真正獨立的支持與反對來源？

**Uncertainty Type**  
可估風險、概率歧義，還是 radical uncertainty？

**Next Most Informative Test**  
下一步哪個測試最能減少不確定性？

---

*HAEC06 / Human–AI Epistemic Calibration Series A Closing Paper / v0.1 / 2026-09-07*  
*EveMissLab — Boundless Knowledge. One Promise Forward.*
