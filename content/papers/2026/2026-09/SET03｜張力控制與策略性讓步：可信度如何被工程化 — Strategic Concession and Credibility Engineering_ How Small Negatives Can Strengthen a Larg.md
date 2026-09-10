# SET03｜張力控制與策略性讓步：可信度如何被工程化
## Strategic Concession and Credibility Engineering: How Small Negatives Can Strengthen a Larger Positive Narrative

**定位：** Selective Truth and Epistemic Topology / Foundation Paper 03 / Credibility Structure  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-07  
**狀態：** Canonical Source / UTF-8 Markdown  
**文件性質：** Epistemology / Persuasion / Pragmatics / Two-Sided Messaging / Credibility / Information Selection / Strategic Disclosure

---

## Canonical Source Note

本文件之正式原稿為此 UTF-8 Markdown source。任何 HTML、PDF、LaTeX rendering、聊天介面顯示或其他格式皆屬 projection，不取代 canonical source。

數學公式 canonical delimiter 僅使用：

- inline math：` $...$ `
- display math：`$$...$$`

本文不針對任何特定人物、政黨、宗教、哲學學派、科學學派、媒體、企業或 AI 系統。本文研究的是一般性的訊息結構：**為何加入有限、真實、可承受的負面資訊，有時不會削弱一個正向敘事，反而會提高其可信度、確定感或最終說服力；以及 receiver 如何區分真誠平衡與策略性讓步。**

本文承接 SET01 與 SET02：

$$
\boxed{
\text{Statement Truth}
\neq
\text{Selection Neutrality}
\neq
\text{Message Representativeness}
}
$$

以及：

$$
\boxed{
\text{Message Verification}
\not\Rightarrow
\text{Policy Identification}
}
$$

SET03 再加入第三個問題：

$$
\boxed{
\text{Presence of Criticism}
\not\Rightarrow
\text{Balance of Criticism}
}
$$

一個訊息含有負面內容，只能證明「有負面內容被揭露」，不能自動證明「高權重反證被公平揭露」。

---

# 摘要

人們通常把「一面倒」視為不可信，把「有正有反」視為較客觀。然而，既有 persuasion、two-sided messaging、advertising 與 consumer judgment 研究顯示，兩面訊息的效果並不單純。經典 meta-analysis 發現，在部分非廣告情境中，帶有反駁的 two-sided messages 比 one-sided messages 具有更高 credibility 與 persuasiveness；在部分廣告情境中，非反駁式 two-sided messages 可能提高 credibility，但未必提高 persuasiveness。Two-sided advertising 的 meta-analysis 也指出，負面資訊的量、品質、位置、與正面屬性的關係，以及揭露是否自願，都會調節效果。

更直接地，Ein-Gar、Shiv 與 Tormala 所研究的 **blemishing effect** 顯示，在特定條件下，一小段輕度負面資訊加入原本正向的描述，反而使整體評價更正面；此效果受 processing effort 與 presentation order 調節。Eisend 的研究則顯示，自願揭露負面資訊可能引發 source-credibility inference，而且在 cognitive load 下，receiver 可能更容易完成「這個來源很可信」的推論，而未充分處理負面屬性本身。

這些結果支持一個一般性問題：**負面資訊不只具有內容效應，也可能具有來源效應。** 一段批評可以同時降低 target evaluation，又提高 source credibility；如果後者的正向效應大於前者的負向效應，加入批評可能提升整體說服結果。

本文因此提出 **Strategic Concession Structure（SCS）**：sender 主動揭露一個真實但低決策權重的負面項目，以換取更高的 perceived neutrality、honesty 或 credibility，同時可能省略更高權重的反證。本文不主張所有 two-sided messages 都是操縱；真誠平衡、科學自我批判、風險揭露與 refutational communication 都可能合理且必要。真正要審查的是：

$$
\boxed{
\text{Concession Cost}
\quad
\text{versus}
\quad
\text{Credibility Dividend}
}
$$

以及：

$$
\boxed{
\text{Disclosed Negative Weight}
\quad
\text{versus}
\quad
\text{Omitted Negative Weight}
}
$$

本文建立 **Concession Cost Ratio（CCR）**、**Credibility Dividend Index（CDI）**、**Negative Weight Coverage（NWC）**、**Tension Asymmetry（TA）** 與 **Fatal-Counterevidence Omission（FCO）** 等啟發式量，並提出 **Strategic Concession Audit Protocol（SCAP）**。

核心結論為：

$$
\boxed{
\text{A message can buy credibility with a small truth while withholding a larger truth}
}
$$

但更重要的是另一面：

$$
\boxed{
\text{Not every concession is strategic, and not every two-sided message is manipulative}
}
$$

真正的問題不是「有沒有批評」，而是批評在完整 evidence topology 中佔什麼位置、花了 sender 多少代價、對 receiver 決策有多少權重，以及如果證據方向反過來，sender 是否仍會採取相同揭露規則。

---

# 0　從「一路誇」到「控制張力」

最低階的正向說服結構很簡單：

$$
(+,+,+,+,+)
$$

它容易被 receiver 辨認為單向推銷、奉承或 advocacy。

更成熟的訊息可能變成：

$$
(+,-,+,+,-,+)
$$

表面上具有起伏。

receiver 因此可能推斷：

> 這個來源不是只挑好話，他連缺點都願意講，所以後面的正面判斷應該更可信。

這個推斷有時完全合理。

一個真正做過完整評估的人，本來就應該能指出限制。

但同一個表面結構也可以被策略性使用：

$$
(+,-_{\mathrm{cheap}},+,+,+)
$$

其中被揭露的負面項目：

$$
n_{\mathrm{cheap}}
$$

是真的，但決策權重低；而真正可能改變結論的：

$$
n_{\mathrm{fatal}}
$$

沒有進場。

因此：

$$
\boxed{
\text{two-sided appearance}
\neq
\text{two-sided evidence coverage}
}
$$

這就是 SET03 的起點。

---

# 1　批評具有雙重效應

令一段負面資訊 $n$ 對 target evaluation 造成影響：

$$
\Delta V_T(n)<0.
$$

但同時，它可能提升 receiver 對 source 的 credibility：

$$
\Delta C_S(n)>0.
$$

若後續正向訊息的有效權重會隨 source credibility 增加，可寫成：

$$
W^{+}_{\mathrm{eff}}
=
g(C_S)W^{+}.
$$

那麼加入 $n$ 的總效果可概念化為：

$$
\Delta U(n)
=
\Delta V_T(n)
+
\lambda \Delta C_S(n)
+
\Delta R(n),
$$

其中：

- $\Delta V_T(n)$：負面內容對 target 的直接成本；
- $\Delta C_S(n)$：來源可信度紅利；
- $\lambda$：source credibility 對後續資訊權重的轉換係數；
- $\Delta R(n)$：其他接收端效應，例如 certainty、contrast、processing order。

若：

$$
\lambda\Delta C_S(n)+\Delta R(n)
>
|\Delta V_T(n)|,
$$

則可能出現：

$$
\Delta U(n)>0.
$$

也就是：

$$
\boxed{
\text{adding a negative can produce a net positive persuasive effect}
}
$$

這只是概念模型，不是已建立的一般定律。

---

# 2　Two-Sided Messages：不是「有反方就更可信」那麼簡單

O'Keefe 對 one-sided 與 two-sided persuasive messages 的 random-effects meta-analysis 顯示，效果受至少兩個重要 moderator 影響：

1. two-sided message 是否包含對 opposing argument 的 refutation；
2. 情境是否為 consumer advertising。

在非廣告議題中，refutational two-sided messages 相較 one-sided messages，平均具有較高 credibility 與 persuasiveness；但 nonrefutational two-sided messages 並未普遍產生同樣結果。

因此不能寫成：

$$
\text{two-sided}
\Rightarrow
\text{more persuasive}.
$$

比較合理的是：

$$
\boxed{
\text{message sidedness effect is structure-dependent}
}
$$

這正好適合本文：張力不是只有「正與負的數量」，還包括：

- 是否反駁；
- 反駁強度；
- 負面資訊位置；
- 負面資訊重要性；
- source 自願程度；
- receiver processing effort；
- receiver 原始態度；
- 正負證據是否處於同一決策維度。

---

# 3　Blemishing Effect：小缺點有時反而讓整體更好

Ein-Gar、Shiv 與 Tormala 在四項實驗中觀察到：當一個原本正向的描述後面加入小幅負面資訊時，在特定條件下，受試者反而對 target 產生更正向評價。

這個效果受到兩個重要邊界條件調節：

$$
\text{processing effort}
$$

與：

$$
\text{presentation order}.
$$

在該研究中，blemish 更容易在低 processing effort、且小幅負面資訊出現在正面資訊之後時出現。

因此：

$$
\boxed{
\text{small negative}
\not\Rightarrow
\text{lower total evaluation}
}
$$

但同樣不能倒過來宣稱：

$$
\text{small negative}
\Rightarrow
\text{higher total evaluation}.
$$

SET03 將 blemishing effect 視為「張力可能有非線性效果」的實證例，而不是通用操縱公式。

---

# 4　自願揭露與可信度紅利

Eisend 對 two-sided messages 的研究指出，自願揭露負面資訊會影響 receiver 的 attribution。

receiver 可能推斷：

> 如果這個來源願意主動說自己的缺點，他應該比較誠實。

這可概念化為：

$$
P(\text{credible source}\mid n_{\mathrm{voluntary}})
>
P(\text{credible source}\mid n_{\mathrm{forced}}).
$$

但同一研究也顯示，receiver 對 source credibility 的推論與對 product uniqueness / attribute consequence 的推論具有不同 cognitive requirements；在 cognitive load 下，receiver 可能更容易取得「來源可信」的印象，而沒有同等充分地處理負面資訊本身。

這提供一個重要機制：

$$
\boxed{
\text{negative disclosure can be processed more strongly as a source cue than as target evidence}
}
$$

這並不意味 sender 一定在操縱。

它只意味 receiver 的資訊處理具有不同通道與成本。

---

# 5　Strategic Concession Structure

本文定義一個最小 **Strategic Concession Structure（SCS）**。

令：

- $P$：正向 evidence；
- $N_D$：被揭露的負向 evidence；
- $N_O$：未被揭露但 sender 可取得的負向 evidence；
- $w(e)$：證據 $e$ 對決策的權重；
- $C_S$：receiver 對 source 的 credibility。

若 sender 選擇：

$$
N_D
\subset
N
$$

且：

$$
\sum_{n\in N_D}w(n)
\ll
\sum_{n\in N_O}w(n),
$$

但 $N_D$ 的揭露使：

$$
C_S\uparrow,
$$

則存在 strategic-concession risk。

最典型形式：

$$
\boxed{
\text{reveal a cheap negative}
\rightarrow
\text{gain credibility}
\rightarrow
\text{increase weight of later positives}
}
$$

若同時存在高權重反證省略：

$$
\boxed{
\text{cheap concession}
+
\text{fatal omission}
}
$$

則問題更嚴重。

---

# 6　Cheap Concession 不等於 Small Concession

「小缺點」有兩種完全不同的意思。

第一種：

$$
|n|\text{ small in linguistic intensity}.
$$

例如語氣上聽起來很輕。

第二種：

$$
w(n)\text{ small in decision relevance}.
$$

SET03 真正在意的是第二種。

一句語氣很重的批評：

> 這個產品外觀非常難看。

如果決策核心是醫療安全，它可能仍是：

$$
w(n)\approx0.
$$

反過來，一句語氣非常平淡：

> 在長期追蹤中，主要效果未達預先註冊終點。

可能具有：

$$
w(n)\gg0.
$$

因此：

$$
\boxed{
\text{rhetorical negativity}
\neq
\text{epistemic weight}
}
$$

---

# 7　Concession Cost Ratio

令 sender 揭露負面資訊的決策成本為：

$$
C(n).
$$

成本不是情緒成本，而是如果 receiver 真正吸收該資訊，sender 的目標會受多少損害。

定義啟發式 **Concession Cost Ratio（CCR）**：

$$
\mathrm{CCR}
=
\frac{
\sum_{n\in N_D}C(n)
}{
\sum_{n\in N}C(n)
}.
$$

若：

$$
\mathrm{CCR}\rightarrow0,
$$

表示 sender 揭露的負面內容幾乎不傷其核心目標。

若：

$$
\mathrm{CCR}\rightarrow1,
$$

表示重要負面內容也被納入。

低 CCR 不證明欺騙，但高 credibility claim 若建立在極低 CCR 的自我批評上，就應被降權。

---

# 8　Credibility Dividend Index

令揭露負面資訊前後的 perceived source credibility 為：

$$
C_S^{(0)}
$$

與：

$$
C_S^{(1)}.
$$

定義：

$$
\mathrm{CDI}
=
C_S^{(1)}
-
C_S^{(0)}.
$$

若：

$$
\mathrm{CDI}>0,
$$

表示 concession 帶來 credibility dividend。

再定義概念性 leverage：

$$
L_C
=
\frac{\mathrm{CDI}}
{\mathrm{CCR}+\epsilon},
$$

其中 $\epsilon>0$ 防止分母為零。

若：

$$
L_C\gg1,
$$

表示 sender 用相對低成本的 concession 換到高 credibility redirection。

此量僅為研究設計骨架，不是已驗證的心理測量工具。

---

# 9　Negative Weight Coverage

定義完整可得負面 evidence 的總決策權重：

$$
W_N
=
\sum_{n\in N}w(n).
$$

已揭露負面 evidence 權重：

$$
W_D
=
\sum_{n\in N_D}w(n).
$$

定義 **Negative Weight Coverage（NWC）**：

$$
\mathrm{NWC}
=
\frac{W_D}{W_N}.
$$

若：

$$
\mathrm{NWC}\ll1,
$$

但 message 表面上高度 two-sided，則存在：

$$
\boxed{
\text{two-sided appearance with low counterevidence coverage}
}
$$

這比單純計算正負句數更有意義。

---

# 10　Fatal-Counterevidence Omission

令某一反證 $n_f$ 滿足：

$$
P(H\mid M,n_f)
\ll
P(H\mid M).
$$

或使 receiver 的決策：

$$
a(M,n_f)
\neq
a(M).
$$

則稱 $n_f$ 為 decision-critical 或 fatal counterevidence。

定義 **Fatal-Counterevidence Omission（FCO）**：

$$
\mathrm{FCO}
=
\mathbf 1
\left[
\exists n_f\in N_O
\text{ such that }
a(M,n_f)\neq a(M)
\right].
$$

若：

$$
\mathrm{FCO}=1,
$$

那麼「訊息裡有批評」幾乎不能作為 balanced disclosure 的證明。

因為真正會改變決策的反證仍被排除。

---

# 11　Tension Profile：張力不只是一個平均數

將訊息切成按順序出現的 evidence units：

$$
m_1,m_2,\ldots,m_k.
$$

令每一單位的方向與權重為：

$$
s_i
=
\operatorname{sign}(m_i)w(m_i).
$$

得到 **Tension Profile**：

$$
\tau(M)
=
(s_1,s_2,\ldots,s_k).
$$

例如：

$$
\tau_1
=
(+8,-1,+7,+6)
$$

與：

$$
\tau_2
=
(+8,-8,+7,+6)
$$

表面上都「有正有負」，但 epistemic tension 完全不同。

因此：

$$
\boxed{
\text{message sidedness}
\neq
\text{evidence-weight symmetry}
}
$$

---

# 12　Tension Asymmetry

定義：

$$
W^{+}
=
\sum_{s_i>0}s_i,
$$

以及：

$$
W^{-}
=
\sum_{s_i<0}|s_i|.
$$

概念性 **Tension Asymmetry（TA）**：

$$
\mathrm{TA}
=
\frac{
|W^{+}-W^{-}|
}{
W^{+}+W^{-}+\epsilon
}.
$$

但本文特別警告：

低 TA 不等於客觀。

因為 sender 可以故意挑選大量低品質負證據，使重量看似平衡。

所以 TA 必須和：

$$
\mathrm{NWC},
\quad
\mathrm{CCR},
\quad
\mathrm{FCO}
$$

一起看。

---

# 13　策略性讓步與真誠平衡的不可識別性

以下兩個 sender 都可能說：

> 這套方案有明顯限制，而且目前證據並不完整；但在現有替代方案中，我仍認為它最值得推進。

Sender A：

$$
\pi_A=\text{sincere balanced evaluator}.
$$

Sender B：

$$
\pi_B=\text{strategic concession policy}.
$$

表面訊息可能相同：

$$
M_A=M_B.
$$

因此 SET03 不提出「從一句話辨認操縱者」的魔法 classifier。

真正需要的是回到 SET02：

$$
\boxed{
\text{audit the policy, not the tone}
}
$$

檢查：

- sender 還知道哪些反證；
- 揭露了多少高權重反證；
- 如果反證方向倒轉是否仍會揭露；
- 哪些反證會真正改變 receiver 決策；
- concession 對 sender 到底有沒有成本。

---

# 14　Strategic Concession 與 Paltering 的關係

Paltering 指主動使用真實陳述造成 misleading impression。

Strategic concession 可以成為 paltering 的一種工具，但兩者不等價。

可能存在：

$$
\text{Strategic Concession}
+
\text{No Misleading Intent}.
$$

例如 sender 真心相信自己已公平平衡，只是 selection policy 有偏。

也可能：

$$
\text{Strategic Concession}
+
\text{Deliberate Misleading Impression}.
$$

後者才更接近 paltering。

因此 SET03 保持三層區分：

$$
\text{structure},
\quad
\text{function},
\quad
\text{intent}.
$$

先描述結構，再測功能；除非有額外證據，不直接猜 intent。

---

# 15　與 inoculation 的邊界

Two-sided communication 也可能完全出於防禦性教育目的。

Inoculation theory 的典型做法是：

1. forewarning；
2. 暴露 weakened counterargument；
3. 提供 refutational preemption。

目標是提高 receiver 對未來 persuasion 的抵抗能力。

這與 strategic concession 表面都可能包含「先提出反方，再回應」。

但功能可以完全不同：

$$
\text{inoculation}
\rightarrow
\text{build counterarguing capacity}
$$

而：

$$
\text{strategic concession}
\rightarrow
\text{build source credibility or persuasion leverage}.
$$

2021 年對 inoculation mechanism 的實驗並未支持「弱反論點加強反駁必然最優」這種簡單版本；2026 年一項 systematic review 也指出，許多數位 inoculation interventions 對 theory-core mechanism 的直接測量不足。

因此本文不把「先放弱反方」直接宣稱為固定心理操縱公式。

---

# 16　低處理與高處理：張力工程的邊界條件

Blemishing effect 與 two-sided disclosure 文獻都提醒：

$$
\text{processing mode matters}.
$$

receiver 若進行高投入、逐項 evidence-weighting：

$$
w(n)
$$

本身可能得到充分處理。

receiver 若處於低 processing effort 或高 cognitive load：

$$
\text{source cue}
$$

可能比：

$$
\text{target consequence}
$$

更容易影響判斷。

因此本文提出工作假說：

$$
\boxed{
\text{credibility engineering risk increases when source inference is cheaper than evidence integration}
}
$$

但此命題需要跨場景實驗，不能直接視為既定定律。

---

# 17　Strategic Concession Audit Protocol（SCAP）

## Step 1：列出全部已揭露正負 evidence

建立：

$$
P_D,
\quad
N_D.
$$

不要先按句數判平衡。

---

## Step 2：建立 decision-weight scale

對每項 evidence $e$ 評估：

$$
w(e).
$$

優先問：

> 如果加入這一項，決策會不會改？

而不是：

> 這句聽起來負不負面？

---

## Step 3：追查 omitted counterevidence

建立：

$$
N_O.
$$

特別搜尋：

$$
n_f
$$

是否存在。

---

## Step 4：計算概念性 coverage

估計：

$$
\mathrm{NWC},
\quad
\mathrm{CCR},
\quad
\mathrm{FCO}.
$$

不要將這些量當假精準分數；其作用是迫使 reviewer 問對問題。

---

## Step 5：測 concession 是否帶來 credibility dividend

比較 receiver：

$$
C_S^{(0)}
$$

與：

$$
C_S^{(1)}.
$$

若加入批評後來源可信度明顯上升，進一步檢查：

> 這份可信度紅利是否大於被揭露負面資訊真正造成的決策成本？

---

## Step 6：做 reversed-evidence test

若 evidence direction 反過來：

> sender 是否仍然願意揭露同等權重的負面項目？

這與 SET02 的 counterfactual disclosure test 接軌。

---

## Step 7：重新排列順序

比較：

$$
P\rightarrow n
$$

與：

$$
n\rightarrow P.
$$

若結論對順序高度敏感，則訊息效果可能受到 presentation architecture 而非純 evidence weight 驅動。

---

## Step 8：提高 processing demand

讓 receiver：

- 逐項評 evidence weight；
- 寫出 counterargument；
- 分離 source credibility 與 target validity；
- 對每項 claim 要求 primary source。

若張力效果在高處理下消失，則 source-cue route 可能比 substantive-evidence route 更重要。

---

# 18　可檢驗研究設計

## H1：Cheap-Concession Credibility Effect

三組：

1. one-sided positive；
2. positive + low-weight negative；
3. positive + high-weight negative。

測量：

$$
C_S,
\quad
V_T,
\quad
A_T.
$$

其中：

- $C_S$：source credibility；
- $V_T$：target evaluation；
- $A_T$：adoption intention。

預測不是「第二組一定最高」，而是檢驗不同 negative weight 是否產生 source 與 target effect 的分離。

---

## H2：Fatal Omission Blindness

固定表面 two-sidedness，操縱：

$$
\mathrm{FCO}=0
$$

與：

$$
\mathrm{FCO}=1.
$$

測試 receiver 是否仍把兩者評為相近的「客觀」。

若能輕易區分，本文對 cheap concession 的風險可能被高估。

---

## H3：Order Sensitivity

操縱：

$$
P\rightarrow n_{\mathrm{cheap}}
$$

與：

$$
n_{\mathrm{cheap}}\rightarrow P.
$$

測量 blemishing / credibility / certainty effect。

若完全不受 order 影響，則 SET03 的 tension-profile 部分需要縮小適用域。

---

## H4：Processing Load Interaction

比較：

$$
L_{\mathrm{low}}
$$

與：

$$
L_{\mathrm{high}}.
$$

預測 source credibility inference 與 target evidence integration 的相對權重會不同。

---

## H5：Voluntary versus Forced Disclosure

比較：

$$
n_{\mathrm{voluntary}}
$$

與：

$$
n_{\mathrm{required}}.
$$

測試：

$$
\Delta C_S.
$$

如果自願性不改變 source inference，strategic-concession 的其中一條機制需要修正。

---

# 19　制度應用：真正的平衡不是「一定要講缺點」

科學論文、媒體、政策報告、風險揭露與 AI 評估若把 SET03 粗暴化成：

> 每次都加一句缺點，看起來比較客觀。

那反而正中本文批判。

真正應要求的是：

$$
\boxed{
\text{decision-weighted counterevidence coverage}
}
$$

而不是：

$$
\boxed{
\text{cosmetic negativity}
}
$$

例如好的研究摘要不是機械加入：

> 本研究仍有若干限制。

而是指出：

- 哪一項限制最可能改變結論；
- 哪一個替代解釋仍未排除；
- 哪一個 boundary condition 已知；
- 哪一個 replication 尚缺；
- 哪一個 causal arrow 仍只是推測。

也就是讓負面資訊真正做工。

---

# 20　AI 的特殊風險：自動生成「平衡語氣」

AI 很容易產生：

> 一方面……另一方面……
>
> 雖然存在限制，但……
>
> 這並不表示……然而……

這種結構本身沒有錯。

問題是：

$$
\text{linguistic balance}
$$

可能被誤認為：

$$
\text{evidential balance}.
$$

如果 AI 的生成 policy 只是為了 stylistic balance：

$$
\pi_{\mathrm{style}}
$$

那它可能自動補一個低成本反面句，使答案看起來更成熟，卻沒有真的搜尋高權重 counterevidence。

因此 AI 系統最好區分：

$$
\text{rhetorical counterpoint}
$$

與：

$$
\text{evidence-backed counterargument}.
$$

前者是文風。

後者才是認識論內容。

---

# 21　自反性：SET03 本身也不能用「我有反方」來買可信度

本文已經主動寫入：

- two-sided effects 有 moderator；
- blemishing effect 有 boundary conditions；
- inoculation mechanism 並非所有簡單說法都得到支持；
- strategic concession 不必然有 deceptive intent。

但這些反方段落本身，也可能變成本文自己的 cheap concession。

所以本文不能說：

> 因為我也寫了限制，因此我一定客觀。

本文只能要求：

1. 是否引用了真正可能削弱核心命題的研究；
2. 若 two-sided messages 在大量高品質研究中並不帶來 credibility dividend，是否願意降低 CDI 的理論地位；
3. 若 receiver 對 high-weight omission 很敏感，是否願意縮小 FCO-blindness 的風險敘述；
4. 若 processing effort 對結果沒有穩定調節，是否願意修改 source-cue route；
5. 所有 proposed metrics 是否清楚標成 heuristic，而非既成心理量表。

本文不能因「自我批評」本身獲得免疫。

這正是 SET03 對自己的第一個測試。

---

# 22　結論

「有優點，也有缺點」不是客觀性的證書。

因為：

$$
\boxed{
\text{Presence of Negatives}
\not\Rightarrow
\text{Coverage of Counterevidence}
}
$$

一個真誠 evaluator 會講缺點。

一個高明 persuader 也可能講缺點。

甚至一個沒有自覺偏差的 sincere sender，也可能只看得到低成本缺點，而看不到真正能推翻自己結論的反證。

因此 receiver 真正應問的是：

$$
\boxed{
\text{What did the concession cost?}
}
$$

以及：

$$
\boxed{
\text{What stronger counterevidence was available but absent?}
}
$$

SET03 最後留下兩條原則：

$$
\boxed{
\text{A small truth can purchase a large credibility dividend}
}
$$

以及：

$$
\boxed{
\text{Real balance is measured by decision-relevant coverage, not rhetorical symmetry}
}
$$

真正的客觀，不是讓文章看起來有正有負。

而是讓最可能改變結論的證據，也有進場的權利。

---

# References

1. O'Keefe, D. J. (1999). How to Handle Opposing Arguments in Persuasive Messages: A Meta-Analytic Review of the Effects of One-Sided and Two-Sided Messages. *Communication Yearbook*, 22, 209-249. https://doi.org/10.1080/23808985.1999.11678963

2. Eisend, M. (2006). Two-Sided Advertising: A Meta-Analysis. *International Journal of Research in Marketing*, 23(2), 187-198. https://doi.org/10.1016/j.ijresmar.2005.11.001

3. Eisend, M. (2010). Explaining the Joint Effect of Source Credibility and Negativity of Information in Two-Sided Messages. *Psychology & Marketing*, 27(11), 1032-1049. https://doi.org/10.1002/mar.20372

4. Ein-Gar, D., Shiv, B., & Tormala, Z. L. (2012). When Blemishing Leads to Blossoming: The Positive Effect of Negative Information. *Journal of Consumer Research*, 38(5), 846-859. https://doi.org/10.1086/660807

5. Rucker, D. D., Petty, R. E., & Brinol, P. (2008). What's in a Frame Anyway? A Meta-Cognitive Analysis of the Impact of One Versus Two Sided Message Framing on Attitude Certainty. *Journal of Consumer Psychology*, 18(2), 137-149. https://doi.org/10.1016/j.jcps.2008.01.008

6. Rogers, T., Zeckhauser, R., Gino, F., Norton, M. I., & Schweitzer, M. E. (2017). Artful Paltering: The Risks and Rewards of Using Truthful Statements to Mislead Others. *Journal of Personality and Social Psychology*, 112(3), 456-473. https://doi.org/10.1037/pspi0000081

7. Barbati, J. L., Rains, S. A., Ivanov, B., & Banas, J. A. (2021). Evaluating Classic and Contemporary Ideas About Persuasion Resistance in Inoculation Theory: Argument Strength, Refutation Strength, and Forewarning. *Communication Research Reports*, 38(4). https://doi.org/10.1080/08824096.2021.1956450

8. Loughnan, D., van Stekelenburg, A., Pouwels, J. L., Fransen, M. L., & Kleemans, M. (2026). An Analysis of Studies Testing Digital Interventions to Inoculate Against Misinformation: A Systematic Review. *Communication Research*. https://doi.org/10.1177/00936502251411467

---

## 系列位置

**Selective Truth and Epistemic Topology**

- SET01：高明的謊言不需要假話：選擇性真實、資訊抽樣與失真世界
- SET02：聽者的不可識別問題：當客觀評估與策略性真話產生相同表面訊息
- **SET03：張力控制與策略性讓步：可信度如何被工程化**
- SET04：真誠的人也能產生選擇性世界：Sincere Selection Bias
- SET05：信念系統不是信念集合，而是允許箭頭的系統
- SET06：真節點，假拓撲：資訊操縱如何發生在關係而非命題
- SET07：認識論吸引子與自我封閉：吸收無限資訊而幾乎不學習

---

*SET03 / Selective Truth and Epistemic Topology / EveMissLab / v0.1 / 2026-09-07*
