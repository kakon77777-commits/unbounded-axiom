# SET04｜真誠的人也能產生選擇性世界：Sincere Selection Bias
## Sincere Selection Bias: How Honest Agents Can Construct Selective Worlds Without Intending to Deceive

**定位：** Selective Truth and Epistemic Topology / Foundation Paper 04 / Sincere Bias  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-07  
**狀態：** Canonical Source / UTF-8 Markdown  
**文件性質：** Epistemology / Confirmation Bias / Myside Bias / Motivated Reasoning / Selective Exposure / Objectivity Illusion / Information Selection / Belief Updating

---

## Canonical Source Note

本文件之正式原稿為此 UTF-8 Markdown source。任何 HTML、PDF、LaTeX rendering、聊天介面顯示或其他格式皆屬 projection，不取代 canonical source。

數學公式 canonical delimiter 僅使用：

- inline math：` $...$ `
- display math：`$$...$$`

本文不針對任何特定人物、政黨、宗教、哲學學派、科學學派、數學學派、媒體、企業或 AI 系統。本文研究的是一個一般性的認識論現象：**一個沒有欺騙意圖、甚至真誠追求真理的人，仍可能因 prior、identity、commitment、selection policy、evidence weighting 與 interpretation rule，而穩定地生成一個選擇性的世界表徵。**

本文承接前三篇：

$$
\boxed{
\text{Statement Truth}
\neq
\text{Selection Neutrality}
\neq
\text{Message Representativeness}
}
$$

$$
\boxed{
\text{Message Verification}
\not\Rightarrow
\text{Policy Identification}
}
$$

$$
\boxed{
\text{Presence of Criticism}
\not\Rightarrow
\text{Balance of Criticism}
}
$$

SET04 再加入：

$$
\boxed{
\text{Sincerity}
\not\Rightarrow
\text{Epistemic Neutrality}
}
$$

以及：

$$
\boxed{
\text{Absence of Deceptive Intent}
\not\Rightarrow
\text{Absence of Selection Bias}
}
$$

---

# 摘要

本文提出 **Sincere Selection Bias（SSB）**：資訊提供者或信念持有者並無欺騙意圖，所陳述的命題甚至可以全部為真，但其資訊搜尋、證據抽樣、證據加權、反證處理與世界模型更新受到既有信念、認同、承諾、目標或認知結構的系統性影響，使其最終生成的世界表徵不具充分代表性。

SSB 與 paltering 或 strategic omission 不同。後兩者至少在典型形式中涉及 sender 對 misleading effect 的某種策略性利用；SSB 則允許：

$$
D=0,
$$

其中 $D$ 表示欺騙意圖。

SSB 也不等於「無知」。一個人可能非常聰明、熟悉統計、懂 Bayesian updating、具備高領域專業，仍然在資訊來源選擇與 likelihood assignment 上產生方向性不對稱。Taber 與 Lodge 的經典 motivated skepticism 研究甚至觀察到，強 prior 與較高政治 sophistication 在其議題與樣本中可伴隨更強的態度極化；2025 年關於 myside bias 的研究則再次指出，一般認知能力或單次 scientific-reasoning intervention 並不自動消除 myside bias。

然而，本文拒絕把所有 prior-sensitive processing 都叫 bias。2025 年一項 selective-exposure 經濟實驗指出，在明確給定具有相反偏差的資訊來源時，Bayesian decision-maker 在部分條件下本來就可能合理地優先尋找 confirmatory information。2025 年 *Episteme* 亦提出對 identity-protective reasoning 的哲學辯護，指出在 division of epistemic labor、制度性資訊扭曲或高成本個人查證環境中，對可信群體的依賴未必總是非理性。

因此，SSB 的核心不在「你有 prior」；任何認識都不可能沒有 prior。真正的診斷條件是：**在控制 evidence quality、source reliability、decision relevance 與合理背景知識後，selection / weighting / updating 是否仍存在穩定的方向性不對稱，且該不對稱使 agent 的 posterior 或世界表徵持續遠離更具鑑別力的 evidence structure。**

本文建立四層選擇模型：

$$
W
\xrightarrow{\mathcal S_B}
E_B
\xrightarrow{\mathcal W_B}
\tilde E_B
\xrightarrow{\mathcal I_B}
\hat W_B
\xrightarrow{\mathcal U_B}
B'
$$

分別代表 evidence search、evidence weighting、interpretation 與 belief updating。2025 年 *Nature Communications* 的神經研究提供一個重要提醒：與既有判斷不一致的 sensory evidence 可以被精確編碼，但在 downstream readout 時對行為影響較小。這意味「偏差」不能只被理解成沒有看到反證；反證也可能被看到、被記住，卻沒有得到對等的更新權。

本文提出 **Selection Directionality Index（SDI）**、**Counterevidence Weight Ratio（CWR）**、**Revision Resistance（RR）**、**Objectivity-Claim Gap（OCG）**、**Epistemic Escape Capacity（EEC）** 與 **Sincere Selection Audit Protocol（SSAP）**。本文的最終主張不是「每個信念系統都是偏見」，而是：

$$
\boxed{
\text{A worldview can be sincerely maintained, locally truthful, and globally selective at the same time}
}
$$

真正需要防範的不是信念本身，而是信念取得一種特殊權力：**決定哪些資訊值得被看見、哪些箭頭值得被連接、以及哪些反證即使已經看見也不需要改變任何東西。**

---

# 0　最麻煩的偏差，不需要騙子

SET01 至 SET03 很容易讓人產生一個錯覺：

> 只要找到操縱者，就能找到問題來源。

但歷史與日常認識活動中，更常見也更穩定的情況可能是：

$$
\text{sender sincerely believes the selected world}
$$

而不是：

$$
\text{sender knows the fuller world and strategically hides it}.
$$

設完整相關世界資訊為：

$$
F(W).
$$

策略性選擇者可能知道：

$$
F(W),
$$

但故意輸出：

$$
M=\pi_S(F(W)).
$$

真誠選擇者則可能自己的可用世界就已經是：

$$
F_B(W)
=
\pi_B(F(W)).
$$

此時他不是在「隱藏另一半」。

對他而言，那另一半可能：

- 不重要；
- 不可靠；
- 不相關；
- 已被反駁；
- 屬於例外；
- 是對方的宣傳；
- 是測量錯誤；
- 是尚未成熟的研究；
- 不符合他信任的理論結構。

因此：

$$
\boxed{
\text{selection can occur before conscious communication begins}
}
$$

這是 SSB 與策略性欺騙的根本差異。

---

# 1　Sincere Selection Bias 的最小定義

令 agent $A$：

1. 沒有形成誤導 receiver 的目標；
2. 對自己陳述的命題具有真誠信念；
3. 其 observable statements 可以全部為真；
4. 其 evidence selection、weighting 或 interpretation 存在可辨認的方向性不對稱；
5. 該不對稱在控制合理的 evidence-quality 差異後，仍系統性有利於既有 belief state。

則稱存在候選 **Sincere Selection Bias**。

形式上：

$$
D_A=0
$$

但：

$$
\pi_A
\neq
\pi_{\mathrm{reference}}.
$$

其中 $\pi_{\mathrm{reference}}$ 不是「上帝視角的絕對中立政策」，而是依研究問題明確定義的比較政策，例如：

- evidence-quality matched；
- source-reliability matched；
- preregistered sampling；
- blind evaluation；
- symmetric search；
- counterfactual disclosure rule。

因此：

$$
\boxed{
\text{SSB is comparative, not metaphysically absolute}
}
$$

---

# 2　Confirmation Bias：搜尋與解釋都可能偏向既有信念

Nickerson 對 confirmation bias 的經典綜述將其描述為：人們以偏向既有 belief、expectation 或 hypothesis 的方式搜尋或解釋 evidence。

這個定義本身已包含兩條不同箭頭：

$$
\text{belief}
\rightarrow
\text{evidence search}
$$

以及：

$$
\text{belief}
\rightarrow
\text{evidence interpretation}.
$$

因此 SSB 不需要假設 receiver 沒有反方資料。

可能只是：

$$
P(e\in E_B\mid e\text{ congruent})
>
P(e\in E_B\mid e\text{ incongruent}),
$$

或：

$$
w(e\mid e\text{ congruent})
>
w(e\mid e\text{ incongruent}).
$$

前者是 selection asymmetry。

後者是 weighting asymmetry。

兩者可獨立存在。

---

# 3　Motivated Reasoning：理性工具也可以被方向性目標使用

Kunda 的經典模型指出，motivation 可以透過對 cognitive strategies 的偏向性存取、建構與評估影響 reasoning。

一個人若有 accuracy goal，可能尋找最適合準確判斷的策略。

若有 directional goal，則可能更容易動員那些能產生期望結論的策略。

這裡最重要的不是「人會故意騙自己」。

相反，directionally motivated reasoning 的穩定性恰恰常來自：

$$
\boxed{
\text{the agent can construct a justification that feels reasonable from the inside}
}
$$

所以主觀體驗完全可能是：

> 我只是按證據推理。

而不是：

> 我正在偏向自己。

---

# 4　Myside Bias：同一份 evidence，不一定得到同樣的 weight

Lord、Ross 與 Lepper 的經典 biased-assimilation 研究指出，持有不同 prior position 的人對同一組混合證據可能給出不同可信度與方法品質評價。

Taber 與 Lodge 後來在政治議題上進一步觀察到：

- congruent arguments 被評為更強；
- contrary arguments 引發更多 counterarguing；
- 自由選擇資訊時出現 confirmatory search；
- 在其研究條件下，強 prior 與較高 political sophistication 可伴隨更強 polarization。

但 SET04 不把這些舊研究當作「所有人面對相反證據都必然極化」的普遍定律。

近年的政治科學研究也重新檢查 attitude polarization 的可重現性、測量方式與 boundary conditions。

所以本文採較弱主張：

$$
\boxed{
\text{prior-dependent evidence evaluation is empirically possible and context-sensitive}
}
$$

而不是：

$$
\text{all exposure to mixed evidence increases polarization}.
$$

---

# 5　2025 的神經證據：看見反證，不等於讓反證發揮作用

Park 等人在 2025 年 *Nature Communications* 的研究區分兩個機制：

1. evidence encoding 本身被 bias；
2. evidence 被精確 encoding，但 downstream readout 對 congruent evidence 賦予更大行為權重。

研究結果較支持第二種。

也就是：

$$
\text{encoded}(e^-)
$$

可以成立，但：

$$
w_{\mathrm{behavior}}(e^-)
<
w_{\mathrm{behavior}}(e^+).
$$

這給 SSB 一個非常重要的拆分：

$$
\boxed{
\text{Not Seen}
\neq
\text{Not Encoded}
\neq
\text{Not Believed}
\neq
\text{Not Used}
}
$$

人可以完整地看到反證，甚至能準確複述它，但仍讓它對 belief update 的貢獻極低。

---

# 6　四層選擇模型

令當前 belief state 為 $B$。

世界提供候選 evidence pool：

$$
\mathcal E(W).
$$

## 6.1 Search Layer

$$
E_B
=
\mathcal S_B(\mathcal E(W)).
$$

決定：

> 我去看什麼？

---

## 6.2 Weight Layer

$$
\tilde E_B
=
\mathcal W_B(E_B).
$$

決定：

> 我讓哪一項證據有多大分量？

---

## 6.3 Interpretation Layer

$$
\hat W_B
=
\mathcal I_B(\tilde E_B,B).
$$

決定：

> 這項 evidence 在我的世界模型裡到底意味著什麼？

---

## 6.4 Update Layer

$$
B'
=
\mathcal U_B(B,\hat W_B).
$$

決定：

> 我是否真的修改原 belief？

所以：

$$
\boxed{
\text{information availability}
\not\Rightarrow
\text{information uptake}
}
$$

---

# 7　Selective Exposure：人確實傾向選 congenial information，但不是任何時候

Hart 等人的 meta-analysis 綜合 selective exposure 文獻，估計人們對 congenial information 存在中度偏好：

$$
d\approx0.36.
$$

但效果受 defense motivation 與 accuracy motivation 調節。

尤其重要的是：

> 當 incongruent information 對完成當前目標有用時，偏好可以反轉。

因此：

$$
\boxed{
\text{selective exposure is motivationally conditional}
}
$$

不是人類無法避免的固定常數。

這也意味 intervention 不能只靠：

> 多給他看反方資料。

若 agent 的目標函數仍然是 belief defense，更多資料可以只是提供更多 rationalization material。

---

# 8　2025 的重要反例：Confirmatory Search 也可能是合理的

*Journal of the Economic Science Association* 2025 年一項實驗建立兩個具有相反偏差的資訊來源。

當來源未取得 state information 時，它們會偏向自己喜歡的 state；取得資訊時則如實報告。

在該模型中，Bayesian decision-maker 在來源 reliability 對稱時，本來就可能更應該查 confirmatory source，因為那個來源的報告在當前 prior 下具有更高資訊價值。

所以：

$$
\boxed{
\text{confirmatory information seeking}
\not\Rightarrow
\text{confirmation bias}
}
$$

這是 SET04 非常重要的限制。

我們不能只看：

$$
\text{direction of search}
$$

就判 bias。

必須比較：

$$
\text{expected information value}
$$

以及：

$$
\text{source reliability}.
$$

---

# 9　Prior 不是罪：沒有 prior 的認識不存在

Bayesian inference 本身就要求 prior：

$$
P(H).
$$

因此「你有 prior，所以你不客觀」沒有意義。

真正問題是：

$$
P(H\mid E)
\propto
P(E\mid H)P(H)
$$

裡的三個部分都可能受世界模型影響：

1. $P(H)$ 如何形成；
2. 哪些 $E$ 被抽樣；
3. $P(E\mid H)$ 如何估計。

所以一個人完全可以做到：

$$
\text{formally correct Bayes update}
$$

但使用：

$$
\text{biased evidence sample}
$$

或：

$$
\text{misspecified likelihood}.
$$

因此：

$$
\boxed{
\text{Bayesian coherence}
\not\Rightarrow
\text{epistemic neutrality}
}
$$

---

# 10　「Bayesian believer」悖論：方法也可以變成信念身份

如果一個 agent 把某認識方法 $M$ 視為工具：

$$
M:\text{evidence}\mapsto\text{updated belief},
$$

它可以接受：

> 在某些 domain， $M$ 的假設不成立。

但如果 $M$ 進一步成為 identity：

$$
I(M),
$$

那麼對 $M$ 的批評也可能被重新分類成：

$$
\text{misunderstanding of }M,
$$

$$
\text{bad implementation},
$$

或：

$$
\text{opponent lacks rigor}.
$$

本文不主張 Bayesianism、falsificationism、scientism、rationalism、empiricism、formalism 或任何具體學派必然如此。

本文只提出一般性自反命題：

$$
\boxed{
\text{An epistemic method can become identity-protective when exemption from its own audit becomes part of the method's use}
}
$$

---

# 11　Identity-Protective Reasoning：不能只寫成「愚蠢」

Identity-protective reasoning 常被當成 epistemic vice。

但 Flores 在 2025 年 *Episteme* 提出一個重要反方：在 epistemic labor division、institutional distortion 與資訊取得成本存在時，依賴自己所信任群體的 judgment 有時可能具有 epistemic insurance 或 resistance 功能。

這對 SET04 很重要。

因為：

$$
\boxed{
\text{identity dependence}
\not\Rightarrow
\text{epistemic failure}
}
$$

任何人都無法親自驗證現代知識體系中的每一個 claim。

我們本來就依賴：

- 專家；
- institution；
- community；
- citation networks；
- replication systems；
- trusted collaborators。

所以真正問題不是「你信誰」。

而是：

> 你的信任網路是否具有可退出性、反證入口與跨網路校驗能力？

---

# 12　Objectivity Illusion：真誠感可能增加，而不是降低風險

Pronin、Lin 與 Ross 提出的 bias blind spot 顯示，人們往往比評估自己更容易辨認他人的 bias。

Schwalbe、Cohen 與 Ross 進一步以 objectivity illusion 描述：

> 我方觀點是 evidence-based 的；對方觀點則受偏見與身份影響。

SET04 關心其中一個結構問題：

$$
\boxed{
\text{felt sincerity}
\neq
\text{absence of bias}
}
$$

甚至：

$$
\boxed{
\text{felt objectivity}
\neq
\text{measured neutrality}
}
$$

因為 agent 評估自己的 bias 時，只能直接 introspect 自己的 conscious reasons，卻看不到那些沒有進入意識的 selection policy。

---

# 13　但 bias blindness 也不是絕對

Cusimano 與 Lombrozo 2023 年的研究提供重要限制：人在某些 morally motivated reasoning 情境中，可以辨認自己正在偏向一個 evidentially weaker 但 morally desirable 的 belief，甚至認可這種偏向。

因此不能寫：

$$
\text{biased reasoner}
\Rightarrow
\text{unaware reasoner}.
$$

較合理的是：

$$
\boxed{
\text{awareness of bias is variable}
}
$$

並且：

$$
\text{awareness}
\not\Rightarrow
\text{correction}.
$$

一個人可以知道自己有立場，仍相信這個立場合理。

所以 SSB 包含：

- unaware sincere selection；
- partially aware sincere selection；
- consciously endorsed asymmetric selection。

只要沒有 deceptive intent，且偏差主要發生在 agent 自己相信合理的認識程序內，都屬本文研究域。

---

# 14　2024 Selection Neglect：樣本不代表世界，但人常把樣本當世界

Brundage、Little 與 You 在 2024 年 *Annual Review of Political Science* 將 selection neglect 整理為一個統一框架。

人們經常從：

- 朋友；
- 電視；
- 社群媒體；
- 可見群體；
- 高聲量事件

形成對世界的信念，卻未充分修正 sampling process 的非代表性。

因此：

$$
\boxed{
\text{observed frequency}
\neq
\text{population frequency}
}
$$

如果 agent 又真誠地相信：

$$
\text{what I repeatedly observe}
\approx
\text{what the world is like},
$$

就會形成：

$$
\text{environmental selection}
+
\text{sincere inference}.
$$

這是 SSB 的重要外部來源。

偏差不一定起源於 agent 自己的主動選擇。

環境、平台、社群與制度可以先替他選。

---

# 15　Myside Bias 並不容易靠「更會思考」消失

Wimmer 與 Keck 在 2025 年的 preregistered experiment 測試 processing-based 與 conviction-based intervention。

研究仍觀察到：

$$
\text{belief-consistent arguments}
$$

被評為較 persuasive，而且兩種 intervention 都未顯著降低 myside bias。

作者整理的既有文獻亦指出，myside bias 和一般 intelligence 或某些 general rational-thinking measures 的關聯可以很弱。

這支持一個危險但重要的命題：

$$
\boxed{
\text{more reasoning capacity}
\not\Rightarrow
\text{more symmetric evidence processing}
}
$$

但本文不進一步宣稱：

$$
\text{intelligence increases bias}.
$$

能力可以幫助糾錯，也可以幫助 rationalization；方向取決於目標、程序與外部校驗。

---

# 16　Sincere Selection Bias 的形式模型

令 belief system：

$$
B_t.
$$

候選 evidence space：

$$
\mathcal E_t.
$$

selection kernel：

$$
K_S(e\mid B_t).
$$

weighting kernel：

$$
K_W(w\mid e,B_t).
$$

interpretation operator：

$$
\mathcal I(e,B_t).
$$

更新：

$$
B_{t+1}
=
\mathcal U
\left(
B_t,
\mathcal I
\left(
\mathcal W
\left(
\mathcal S(\mathcal E_t,B_t),
B_t
\right),
B_t
\right)
\right).
$$

若在 evidence quality 與 source reliability 配對後仍有：

$$
K_S(e^+\mid B_t)
>
K_S(e^-\mid B_t),
$$

且：

$$
K_W(w\mid e^+,B_t)
>
K_W(w\mid e^-,B_t),
$$

則存在候選方向性不對稱。

其中：

$$
e^+
$$

表示支持當前 belief 的 evidence，

$$
e^-
$$

表示與當前 belief 衝突的 evidence。

---

# 17　Selection Directionality Index

定義：

$$
p^+
=
P(e\text{ selected}\mid e\text{ congruent}),
$$

$$
p^-
=
P(e\text{ selected}\mid e\text{ incongruent}).
$$

啟發式 **Selection Directionality Index（SDI）**：

$$
\mathrm{SDI}
=
p^+-p^-.
$$

若：

$$
\mathrm{SDI}\approx0,
$$

不能直接證明中立。

因為兩邊可能被等量選中、但權重不同。

若：

$$
\mathrm{SDI}\gg0,
$$

也不能直接證明 bias。

因為如第 8 節所示，來源 reliability 與 information value 可能使 confirmatory search 合理。

因此 SDI 必須在 matched-quality condition 下解讀。

---

# 18　Counterevidence Weight Ratio

令：

$$
\bar w^+
=
E[w(e)\mid e^+],
$$

$$
\bar w^-
=
E[w(e)\mid e^-].
$$

定義 **Counterevidence Weight Ratio（CWR）**：

$$
\mathrm{CWR}
=
\frac{\bar w^-}{\bar w^++\epsilon}.
$$

若：

$$
\mathrm{CWR}\ll1
$$

且 quality-matched evidence 本應得到近似權重，則表示反證進場後仍被降權。

這正好對應：

$$
\text{Not Used}
$$

而不是單純：

$$
\text{Not Seen}.
$$

---

# 19　Revision Resistance

令新 evidence batch 為 $E_{\mathrm{new}}$。

belief update magnitude：

$$
\Delta_B
=
d(B_{t+1},B_t).
$$

定義 **Revision Resistance（RR）** 的概念形式：

$$
\mathrm{RR}
=
1-
\frac{
\Delta_B
}{
\Delta_B^{\mathrm{reference}}+\epsilon
}.
$$

reference 可以是：

- blind evaluator；
- matched opposite-prior group；
- preregistered Bayesian benchmark；
- independent expert panel。

若：

$$
\mathrm{RR}\rightarrow1,
$$

表示相對於 reference，agent 對應有更新的 evidence 幾乎不移動。

但若 prior 本身非常強且 evidence 很弱，高 RR 完全可能合理。

所以：

$$
\boxed{
\text{revision resistance must be evidence-strength conditioned}
}
$$

---

# 20　Objectivity-Claim Gap

令 agent 自評客觀性：

$$
O_{\mathrm{self}}.
$$

外部測得 selection / weighting symmetry：

$$
O_{\mathrm{audit}}.
$$

概念性：

$$
\mathrm{OCG}
=
O_{\mathrm{self}}
-
O_{\mathrm{audit}}.
$$

若：

$$
\mathrm{OCG}\gg0,
$$

代表 agent 對自己中立程度的主觀估計高於 audit 結果。

這不是人格診斷。

它是一個 experimental construct。

---

# 21　Epistemic Escape Capacity

本文認為最重要的量可能不是「你目前偏不偏」，而是：

> 你能不能出去？

定義 **Epistemic Escape Capacity（EEC）**，評估 agent 是否能：

1. 主動搜尋最高品質反證；
2. 指定什麼證據會改變自己；
3. 接受 blind evaluation；
4. 讓 independent source 重新抽樣；
5. 修改 likelihood model；
6. 承認原本被排除的 arrow；
7. 在 evidence 足夠時真正更新。

概念上：

$$
\mathrm{EEC}\in[0,1].
$$

低 EEC 的系統才容易進入後續 SET07 所談的 self-sealing attractor。

---

# 22　Sincere Selection Audit Protocol（SSAP）

## Step 1：先取消道德判斷

不要先問：

> 你是不是在騙自己？

改問：

> 你的資訊是怎麼進來的？

把：

$$
\text{intent}
$$

與：

$$
\text{selection structure}
$$

分離。

---

## Step 2：畫出 Evidence Intake Map

列出：

- 主動搜尋來源；
- 被動接收來源；
- 不會接觸的來源；
- 被排除來源；
- source reliability rule；
- 搜尋停止條件。

建立：

$$
\mathcal E_{\mathrm{seen}}
$$

與：

$$
\mathcal E_{\mathrm{unseen}}.
$$

---

## Step 3：做 Matched Evidence Test

找品質、方法、樣本量、來源地位近似的一組：

$$
e^+,
\quad
e^-.
$$

比較：

$$
w(e^+)
$$

與：

$$
w(e^-).
$$

避免把真正的 quality difference 誤判成 bias。

---

## Step 4：要求 Disconfirmation Forecast

在看到新資料前先寫：

> 什麼結果會讓我降低信念？

建立：

$$
F_{\mathrm{revise}}.
$$

如果結果出現後判準被移動，記錄：

$$
\text{goalpost shift}.
$$

---

## Step 5：Blind the Identity

能做到時，移除：

- 作者；
- 學派；
- 政黨；
- institution；
- AI model name；
- ideological label。

測試：

$$
w(e\mid\text{identity visible})
$$

和：

$$
w(e\mid\text{identity blinded}).
$$

---

## Step 6：Reverse the Arrow

將相同 argument structure 換成支持相反結論。

問：

> 我還接受這個推理規則嗎？

測：

$$
\text{rule symmetry}.
$$

---

## Step 7：Independent Resampling

讓另一個獨立 evaluator 重新建立 evidence pool：

$$
\mathcal E'.
$$

比較：

$$
\mathcal E_B
$$

與：

$$
\mathcal E'.
$$

真正重要的是 independent sampling，不只是多一個人評論同一份資料。

---

## Step 8：Update or Register Resistance

若 evidence 達到事先門檻：

$$
E\geq E^*,
$$

就要求：

$$
B_{t+1}\neq B_t.
$$

如果不更新，必須新增可公開檢查的理由，而不是只說：

> 我還是不相信。

---

# 23　AI 與 SSB：AI 可以放大，也可以幫忙拆

AI 不是 SSB 的來源。

但 AI 可以進入四層中的任何一層：

$$
\mathcal S_B,
\quad
\mathcal W_B,
\quad
\mathcal I_B,
\quad
\mathcal U_B.
$$

若 AI 搜尋時持續按照 user framing 找資料：

$$
\mathcal S_B^{\mathrm{AI}}
$$

會放大 selection。

若 AI 在相同 evidence 上對 congruent argument 更寬鬆：

$$
\mathcal W_B^{\mathrm{AI}}
$$

會放大 weighting bias。

但 AI 也可以反過來做：

- blind adversarial search；
- opposite-prior simulation；
- source-independent resampling；
- counterevidence ranking；
- preregistered disconfirmation test；
- likelihood comparison。

因此：

$$
\boxed{
\text{AI is an amplifier of epistemic procedure, not inherently of truth or bias}
}
$$

---

# 24　科學、哲學、政治與宗教只是應用域，不是本文靶子

SSB 可出現在任何具有：

$$
\text{belief}
+
\text{selection}
+
\text{interpretation}
+
\text{updating}
$$

的系統。

包括：

- 科學研究；
- 哲學本體論；
- 數學基礎立場；
- 政治意識形態；
- 宗教信仰；
- 反宗教立場；
- 商業策略；
- 醫療判斷；
- 歷史敘事；
- AI alignment；
- Bayesian methodology；
- falsificationist methodology。

本文的對稱原則是：

$$
\boxed{
\text{No epistemic tribe receives exemption}
}
$$

而不是：

$$
\text{all tribes are equally wrong}.
$$

---

# 25　方法一旦豁免於自己的方法，就開始信仰化

本文提出一條自反原則：

$$
\boxed{
\text{Any epistemic method exempted from its own audit can become ideology}
}
$$

關鍵詞是：

$$
\text{can},
$$

不是：

$$
\text{must}.
$$

科學方法可以自我修正。

Bayesianism 可以比較 prior 與 model misspecification。

形式主義可以檢查 formal system 的限制。

哲學可以做 meta-philosophy。

宗教傳統也可能具有內部勘驗與反省制度。

真正危險的是：

> 方法只用來檢查別人，不再檢查自己。

---

# 26　研究假說與可證偽條件

## H1：Sincere Search Directionality

讓 participants 真誠以 accuracy goal 搜尋，控制 source quality，測：

$$
\mathrm{SDI}.
$$

若 matched condition 下：

$$
\mathrm{SDI}\approx0,
$$

則 SSB 的 search-layer 普遍性應降低。

---

## H2：Readout Without Encoding Loss

提供 matched evidence，測：

- comprehension；
- memory；
- behavioral weight。

若：

$$
\text{memory}(e^-)
\approx
\text{memory}(e^+)
$$

但：

$$
w(e^-)
<
w(e^+),
$$

支持「看見但不使用」模型。

---

## H3：Identity Blinding

比較：

$$
w(e\mid I_{\mathrm{visible}})
$$

與：

$$
w(e\mid I_{\mathrm{blind}}).
$$

若 identity blinding 不減少方向性差異，identity 不是主要機制。

---

## H4：Explicit Revision Threshold

要求 participants 事先指定：

$$
E^*.
$$

若達到 $E^*$ 後仍不更新，而且產生新的 ad hoc 條件，表示 revision resistance。

若大多數人按門檻更新，則 SSB 的 self-sealing 風險被高估。

---

## H5：Expertise Interaction

比較不同 expertise。

本文不預測單調關係。

可能：

$$
\text{expertise}
\rightarrow
\text{better discrimination},
$$

也可能在 identity-charged domain：

$$
\text{expertise}
\rightarrow
\text{better rationalization}.
$$

若只有前者，則「高能力者同樣危險」需要縮小。

---

# 27　什麼結果會削弱 SET04？

以下結果若穩定成立，本文核心應被修正：

1. evidence-quality matching 後，selection directionality 幾乎消失；
2. receiver 對反證的 weighting 與支持證據高度對稱；
3. objectivity self-rating 能高度準確預測 audit neutrality；
4. expertise 普遍大幅降低 myside bias；
5. precommitted revision thresholds 幾乎完全消除 resistance；
6. identity blinding 對 evidence weighting 沒有可重現影響；
7. independent resampling 與 self-selected evidence pool 高度一致。

SET04 不應因為「confirmation bias 很有名」而免除自己的證偽責任。

---

# 28　與 SET05 的接口：信念不只決定節點，也決定允許的箭頭

SET04 目前主要描述：

$$
\text{what enters}
$$

以及：

$$
\text{how much weight it receives}.
$$

但更深一層是：

> 同樣的 true facts，為什麼不同 worldview 會連出不同 causal / explanatory structure？

這將進入 SET05。

令信念系統不只是：

$$
B=\{b_1,b_2,\ldots,b_n\},
$$

而是：

$$
\mathcal B
=
(V,E,\pi,\Phi),
$$

其中：

- $V$：可承認的 nodes；
- $E$：可承認的 arrows；
- $\pi$：selection policy；
- $\Phi$：新 evidence 的 interpretation / absorption rule。

SET04 研究 $\pi$ 與 evidence weighting。

SET05 將研究：

$$
E
$$

與：

$$
\Phi.
$$

---

# 29　自反性：SET04 也可能只是另一種「我們比別人客觀」

寫一篇關於 sincere bias 的文章，非常容易產生最諷刺的結果：

> 我知道 confirmation bias，所以我比那些不知道的人客觀。

這正是 bias blind spot 的典型入口。

因此本文必須承認：

$$
\boxed{
\text{knowing the name of a bias does not grant immunity from the bias}
}
$$

本文作者與 AI 協作者同樣具有：

- literature-selection policy；
- framing choice；
- preferred theoretical vocabulary；
- prior commitment；
- source-quality judgment；
- narrative structure。

所以 SET04 對自己的最低要求是：

1. 納入 confirmatory search 可能合理的反例；
2. 納入 identity-protective reasoning 可能有 epistemic value 的反方；
3. 不把 awareness 與 correction 混為一談；
4. 不把 sophistication 與 bias 寫成必然正相關；
5. 不把 Bayesian reasoning 當作批評對象，而只批評任何方法的豁免化；
6. 若 future evidence 顯示 matched evidence 下的大部分 asymmetry 消失，必須縮小 SSB。

本文沒有「因為談偏差，所以免於偏差」的特權。

---

# 30　結論

最穩定的失真世界，不一定由騙子建造。

它可以由一群完全真誠的人共同維持。

每個人都說真話。

每個人都認為自己在看 evidence。

每個人都能解釋為什麼反方資料不夠好。

每個人甚至都願意告訴你：

> 如果真的有足夠證據，我當然會改。

真正的問題因此不在 sincerity。

而在：

$$
\boxed{
\text{selection}
+
\text{weighting}
+
\text{interpretation}
+
\text{revision}
}
$$

四層是否仍保有反證的進場權。

本文最後留下四條原則：

$$
\boxed{
\text{Sincerity is a moral property, not a neutrality certificate}
}
$$

$$
\boxed{
\text{Prior dependence is unavoidable; asymmetric evidence treatment is the auditable target}
}
$$

$$
\boxed{
\text{Seeing counterevidence is not enough if counterevidence has no update power}
}
$$

以及：

$$
\boxed{
\text{The health of a worldview is measured less by what it currently believes than by its capacity to leave itself}
}
$$

真正重要的認識論能力，不是沒有信念。

而是：

> **當世界真的給出足夠強的反證時，你的系統裡還有沒有一條合法的路，可以從「我相信」走到「我改變了」。**

---

# References

1. Nickerson, R. S. (1998). Confirmation Bias: A Ubiquitous Phenomenon in Many Guises. *Review of General Psychology*, 2(2), 175-220. https://doi.org/10.1037/1089-2680.2.2.175

2. Kunda, Z. (1990). The Case for Motivated Reasoning. *Psychological Bulletin*, 108(3), 480-498. https://doi.org/10.1037/0033-2909.108.3.480

3. Lord, C. G., Ross, L., & Lepper, M. R. (1979). Biased Assimilation and Attitude Polarization: The Effects of Prior Theories on Subsequently Considered Evidence. *Journal of Personality and Social Psychology*, 37(11), 2098-2109. https://doi.org/10.1037/0022-3514.37.11.2098

4. Taber, C. S., & Lodge, M. (2006). Motivated Skepticism in the Evaluation of Political Beliefs. *American Journal of Political Science*, 50(3), 755-769. https://doi.org/10.1111/j.1540-5907.2006.00214.x

5. Hart, W., Albarracín, D., Eagly, A. H., Brechan, I., Lindberg, M. J., & Merrill, L. (2009). Feeling Validated Versus Being Correct: A Meta-Analysis of Selective Exposure to Information. *Psychological Bulletin*, 135(4), 555-588. https://doi.org/10.1037/a0015701

6. Pronin, E., Lin, D. Y., & Ross, L. (2002). The Bias Blind Spot: Perceptions of Bias in Self Versus Others. *Personality and Social Psychology Bulletin*, 28(3), 369-381. https://doi.org/10.1177/0146167202286008

7. Schwalbe, M. C., Cohen, G. L., & Ross, L. D. (2020). The Objectivity Illusion and Voter Polarization in the 2016 Presidential Election. *Proceedings of the National Academy of Sciences*, 117(35), 21218-21229. https://doi.org/10.1073/pnas.1912301117

8. Cusimano, C., & Lombrozo, T. (2023). People Recognize and Condone Their Own Morally Motivated Reasoning. *Cognition*, 234, 105379. https://doi.org/10.1016/j.cognition.2023.105379

9. Brundage, M., Little, A. T., & You, S. (2024). Selection Neglect and Political Beliefs. *Annual Review of Political Science*, 27, 63-85. https://doi.org/10.1146/annurev-polisci-041322-033325

10. Glüer-Pagin, K., & Spectre, L. (2025). Where Is the Motivation in Motivated Numeracy? *Review of Philosophy and Psychology*, 16, 481-498. https://doi.org/10.1007/s13164-024-00737-w

11. Flores, C. (2025). Identity-Protective Reasoning: An Epistemic and Political Defense. *Episteme*, 22(3), 707-730. https://doi.org/10.1017/epi.2025.17

12. Park, H., Arazi, A., Talluri, B. C., et al. (2025). Confirmation Bias Through Selective Readout of Information Encoded in Human Parietal Cortex. *Nature Communications*, 16, 5391. https://doi.org/10.1038/s41467-025-61010-x

13. Wimmer, L., & Keck, K. (2025). How to Reduce Myside Bias? Testing the Effectiveness of Processing- and Conviction-Based Intervention Measures. *Collabra: Psychology*, 11(1), 150250. https://doi.org/10.1525/collabra.150250

14. Nunnari, S., & Montanari, G. (2025). Audi alteram partem: An Experiment on Selective Exposure to Information. *Journal of the Economic Science Association*, 11(1), 139-150. https://doi.org/10.1017/esa.2025.8

15. Özkan, F. E., & Ronfard, S. (2026). The Boundaries and Ontogeny of Myside Bias. *Journal of Experimental Psychology: General*, 155(6), 1523-1535. https://doi.org/10.1037/xge0001932

---

## 系列位置

**Selective Truth and Epistemic Topology**

- SET01：高明的謊言不需要假話：選擇性真實、資訊抽樣與失真世界
- SET02：聽者的不可識別問題：當客觀評估與策略性真話產生相同表面訊息
- SET03：張力控制與策略性讓步：可信度如何被工程化
- **SET04：真誠的人也能產生選擇性世界：Sincere Selection Bias**
- SET05：信念系統不是信念集合，而是允許箭頭的系統
- SET06：真節點，假拓撲：資訊操縱如何發生在關係而非命題
- SET07：認識論吸引子與自我封閉：吸收無限資訊而幾乎不學習

---

*SET04 / Selective Truth and Epistemic Topology / EveMissLab / v0.1 / 2026-09-07*
