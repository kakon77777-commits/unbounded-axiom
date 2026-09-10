# SET01｜高明的謊言不需要假話：選擇性真實、資訊抽樣與失真世界
## Sophisticated Deception Does Not Require Falsehood: Selective Truth, Information Sampling, and Distorted Worlds

**定位：** Selective Truth and Epistemic Topology / Foundation Paper 01 / Series B Opening Paper  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-07  
**狀態：** Canonical Source / UTF-8 Markdown  
**文件性質：** Epistemology / Selective Disclosure / Paltering / Information Design / Framing / Evidence Sampling / Communication / Deception

---

## Canonical Source Note

本文件之正式原稿為此 UTF-8 Markdown source。任何 HTML、PDF、LaTeX rendering、聊天介面顯示或其他格式皆屬 projection，不取代 canonical source。

數學公式 canonical delimiter 僅使用：

- inline math：` $...$ `
- display math：`$$...$$`

本文不針對任何特定人物、政黨、宗教、哲學學派、科學學派或 AI 系統。本文處理的是一個可跨越人際互動、媒體、政治、科學傳播、商業溝通與人機協作的一般問題：**當所有被說出的句子都是真的時，整體訊息是否仍可能失真？**

本文承接 Human–AI Epistemic Calibration Series，但從本篇開始刻意離開 AI 專屬語境。AI 只是選擇性資訊傳播的一種新型 sender；本文的分析在沒有 LLM 的世界中仍然成立。

---

# 摘要

關於欺騙的直覺通常把真假放在句子層級：若陳述為假，則可能構成欺騙；若陳述為真，則至少在事實層面是可靠的。本文主張，這個二分對真實世界中的溝通遠遠不夠。說話者可以不修改任何事實，只修改「哪些事實被選入訊息」「哪些事實被省略」「事實如何排序」「哪些反向證據得到低顯著度」「哪些局部缺點被主動承認以換取可信度」，最後讓接收者形成與完整證據集合不相稱的世界模型。

本文提出最小區分：

$$
\boxed{
\text{Statement Truth}
\neq
\text{Selection Neutrality}
\neq
\text{Message Representativeness}.
}
$$

令世界相關事實集合為 $F(W)$，實際傳遞訊息為 $M$，資訊選擇政策為 $\pi$：

$$
M=\pi(F(W)).
$$

即使滿足：

$$
\forall f\in M,\qquad f=\mathrm{true},
$$

仍不推出：

$$
M\approx F(W),
$$

也不推出 $\pi$ 是中性的。本文因而把欺騙從「修改命題真值」擴展到「修改事實抽樣分布」：

$$
\boxed{
\text{Deception need not alter facts; it may alter the sampling distribution over facts.}
}
$$

既有研究已提供若干相鄰概念。Rogers 等人把**使用真實陳述製造誤導印象**定義為 paltering，並以多項實驗區分 paltering、omission 與 commission。經濟學中的 Bayesian persuasion 與 information design 進一步證明，即使 receiver 是理性的，只要 sender 可以設計揭露哪些訊號，receiver 的後驗與行動仍可被系統性改變。selective disclosure、framing、dependent consensus 與 communicative norm violations 則說明：失真可以發生在真實資料的挑選、呈現結構、重複來源與語用含意，而不必依賴捏造假資訊。

然而本文不把所有 selective truth 都定義成 deception，因為相同輸出結構也可能由真誠偏差、有限注意、編輯約束、摘要需求或不完整世界模型產生。因此本文區分：策略性選擇、功能性選擇、真誠性選擇與中性壓縮，並主張判定欺騙需要額外考察 sender 的資訊可得性、目的與反事實選擇政策。

本文提出 **Truthful Selection Model（TSM）**、**Selection Distortion Gap（SDG）**、**Counterevidence Omission Ratio（COR）**、**Selection Policy Sensitivity（SPS）** 與 **Topological Distortion Index（TDI）** 等啟發式量，並提出一套 **Truthful-Message Audit Protocol（TMAP）**：先驗證句子真值，再追查未展示母集合、比較替代抽樣政策、建立正反證對稱表、檢查來源獨立性與訊息排序，最後才判斷訊息是否具有代表性。

本文核心結論不是「所有選擇都是操縱」，而是更保守的認識論原則：

$$
\boxed{
\text{Fact-checking is necessary, but fact-checking alone is not sufficient.}
}
$$

若接收者只問「這些話是不是真的」，卻不問「為什麼我看到的是這些真話」，那麼一個完全不說假話的資訊系統，仍然可以塑造一個高度失真的世界。

---

# 0　問題起點：如果每一句都是真的，還能不能把人帶錯？

設一個事件、人物、理論、政策或市場具有十項與判斷相關的事實：

$$
F(W)=\{f_1,f_2,\ldots,f_{10}\}.
$$

其中五項對命題 $H$ 有利，五項不利：

$$
F(W)=F^{+}\cup F^{-}.
$$

sender 不說任何假話，只選擇：

$$
M=\{f_1^{+},f_2^{+},f_3^{+}\}.
$$

接收者逐句 fact-check，得到：

$$
\forall f\in M,\qquad f=\mathrm{true}.
$$

若接收者接著把「每句為真」偷換成「這是一個代表性的世界摘要」，便可能產生：

$$
P(H\mid M)\gg P(H\mid F(W)).
$$

這個失真不在單一 proposition。

它發生在：

- evidence selection；
- omission；
- ordering；
- salience；
- source repetition；
- contrast choice；
- framing；
- causal adjacency；
- response to direct questions；
- counterevidence visibility。

因此本文的第一個命題是：

$$
\boxed{
\text{Local Veracity}
\not\Rightarrow
\text{Global Representativeness}.
}
$$

這不是要降低真值的重要性。相反，它是在真值檢驗上再加一層：**一個真實訊息仍然有一個生成過程，而生成過程本身也需要接受認識論審查。**

---

# 1　既有概念：paltering 只是更大問題的一個子集

## 1.1 Paltering

Rogers、Zeckhauser、Gino、Norton 與 Schweitzer 將 paltering 定義為：主動使用真實陳述來傳達誤導印象。該研究透過兩項 pilot study 與六項實驗，把 paltering 與 omission 及 commission 區分，並發現談判者可能偏好 paltering，部分原因是 sender 可以維持「我說的都是真的」的自我理解，而 receiver 更關心的是「我被帶出了一個錯誤印象」。

本文接受這個區分，但不把 Series B 限縮為 paltering，因為本文還要處理至少四種情況：

1. sender 有意誤導且只說真話；
2. sender 有意說服，但不認為自己在欺騙；
3. sender 真誠相信自己的取樣是公平的；
4. 沒有任何人格化 sender，失真由演算法、制度或資訊結構產生。

因此：

$$
\text{Paltering}
\subset
\text{Selective-Truth Distortion}.
$$

這裡的包含關係是概念性分類，不宣稱存在已公認的正式學術上位類別。

---

## 1.2 Omission

omission 的關鍵不是「說錯」，而是「沒有說出對判斷重要的真實資訊」。

若完整相關證據為：

$$
F_R(W),
$$

訊息為：

$$
M\subset F_R(W),
$$

則 omission 的認識論問題不是集合真值，而是：

$$
F_R(W)\setminus M
$$

裡面是否存在會實質改變 receiver 判斷的資訊。

因此一個更好的問題不是：

> 你有沒有漏資料？

因為任何摘要都必然漏資料。

而是：

> 你漏掉的資料，在加入後是否會改變合理 receiver 的 posterior、排序、決策或信賴？

---

## 1.3 Selective disclosure

selective disclosure 研究直接處理 sender 根據 receiver 偏好、傾向或目標選擇揭露資訊的情形。這裡的重要點是：即使沒有虛構內容，**資訊可見性的政策本身就是行動的一部分**。

因此：

$$
\pi
$$

不是中性的管道參數，而可能是 persuasion mechanism。

---

## 1.4 Bayesian persuasion 與 information design

Kamenica 與 Gentzkow 的 Bayesian persuasion 給出一個更根本的結果：sender 可以透過選擇 signal structure 改變 receiver 的 posterior 與行動，即使 receiver 知道資訊生成結構並進行 Bayesian reasoning。

這提醒我們：

$$
\boxed{
\text{Rational Receiver}
\not\Rightarrow
\text{Immune to Information Design}.
}
$$

一個人的 Bayes formula 可以完全算對，但如果他收到的 signal 本來就是經設計後的 signal，他更新的是：

$$
P(H\mid M,\pi),
$$

而不是直接看到：

$$
P(H\mid F(W)).
$$

這與「知道 Bayes 就能免疫選擇偏差」的直覺完全不同。

---

# 2　Truthful Selection Model：真話也有抽樣政策

令：

$$
W
$$

表示世界狀態；

$$
F_R(W)
$$

表示與目標問題 $Q$ 相關的可得事實集合；

$$
\pi
$$

表示資訊選擇政策；

$$
M=\pi(F_R(W))
$$

表示 receiver 實際看到的訊息。

若要求 truthful-message condition：

$$
\forall f\in M,\qquad f=\mathrm{true},
$$

這只限制：

$$
M
$$

內部不能含假命題。

它沒有限制：

$$
P(f\in M\mid f\in F_R(W),\pi).
$$

因此兩個 sender 可以都百分之百 truthful，但採用完全不同的選擇政策：

$$
\pi_A\neq\pi_B.
$$

並得到：

$$
M_A\neq M_B.
$$

receiver 若不知道 $\pi$，會面對一個來源識別問題。

---

# 3　第二層問題：聽者看得到訊息，看不到選擇政策

接收者通常觀察到的是：

$$
M.
$$

但真正需要推斷的是：

$$
(W,\pi).
$$

因此完整後驗應寫為：

$$
P(W,\pi\mid M).
$$

若 receiver 偷偷固定：

$$
\pi=\pi_0,
$$

其中 $\pi_0$ 被理解為中性、代表性或善意抽樣，便會得到：

$$
P(W\mid M,\pi_0).
$$

但實際 sender 若使用：

$$
\pi=\pi_s,
$$

則 receiver 的 posterior 可能系統性偏離：

$$
P(W\mid M,\pi_0)
\neq
P(W\mid M,\pi_s).
$$

所以真正困難的地方不是「人不會 Bayes」。

而是：

$$
\boxed{
\text{Receiver often lacks the selection policy needed to perform the right Bayes update.}
}
$$

---

# 4　四種選擇政策：不是所有偏差都叫謊言

為避免把一切溝通都污名化為 manipulation，本文區分四類。

## 4.1 Neutral Compression

sender 因篇幅、時間、頻寬限制做壓縮，且嘗試最大化與目標問題相關的代表性：

$$
\pi_N.
$$

即使結果仍有偏差，也不代表存在欺騙意圖。

---

## 4.2 Functional Selection

sender 為特定任務而選擇資訊，例如醫師只向外科團隊突出手術風險、工程師只向現場人員突出故障條件。

這種資訊選擇可以是有目的的，但目的未必是讓 receiver 形成錯誤世界模型。

---

## 4.3 Strategic Selection

sender 知道存在其他重要資訊，並刻意選擇能把 receiver posterior 推向 sender 偏好的訊息：

$$
\pi_S
=
\arg\max_{\pi}
U_S(a_R(M)).
$$

其中 $a_R$ 是 receiver 根據訊息做出的行動。

這一類最接近 paltering、persuasion 與 strategic disclosure。

---

## 4.4 Sincere Selection

sender 自己就只把某些資訊視為重要：

$$
F_R(W)
\xrightarrow{\pi_B}
F_B(W),
$$

再從自己的 belief-conditioned world representation 中產生訊息。

此時 sender 可能完全真誠。

他不是：

> 我知道反證，但我要藏起來。

而可能是：

> 那些根本不算反證。

這一型將在後續 SET04 詳細展開。本篇只先標記：

$$
\boxed{
\text{Selective distortion does not require deceptive intent.}
}
$$

---

# 5　高明的說服：不是全正面，而是控制張力

粗糙宣傳常呈現：

$$
+,+,+,+,+.
$$

receiver 很容易識別 sender 目的。

更高明的資訊選擇可以刻意加入有限反證：

$$
+,-,+,+,-,+.
$$

使 receiver 推斷：

$$
\text{The sender considered both sides.}
$$

然而「有負面資訊」不等於「重要負面資訊得到代表性揭露」。

令負面事實集合為：

$$
F^{-}=\{n_1,n_2,\ldots,n_k\},
$$

其中權重：

$$
w(n_1)\ll w(n_k).
$$

sender 可以主動揭露：

$$
n_1,
$$

卻隱去：

$$
n_k.
$$

這形成一種 **strategic concession**：承認低成本缺點，以提高剩餘訊息的可信度。

因此：

$$
\boxed{
\text{Presence of criticism}
\not\Rightarrow
\text{representative criticism}.
}
$$

這也是「看似中立」與「實際中立」必須分開的原因。

---

# 6　真實節點不保證真實敘事

假設三個命題全部為真：

$$
A=\mathrm{true},
$$

$$
B=\mathrm{true},
$$

$$
C=\mathrm{true}.
$$

訊息把它們依序呈現為：

$$
A\rightarrow B\rightarrow C.
$$

receiver 可能自然讀出某種因果、解釋或時間連續性。

但真值只證明節點：

$$
\{A,B,C\}.
$$

沒有自動證明箭頭：

$$
A\rightarrow B,
$$

或：

$$
B\rightarrow C.
$$

因此：

$$
\boxed{
\text{Node Truth}
\not\Rightarrow
\text{Edge Validity}.
}
$$

而更強的結論是：

$$
\boxed{
\text{A sophisticated distortion can preserve every fact node while corrupting the observed topology.}
}
$$

這個問題將在 SET05–SET06 與 Path Compression 系列進一步處理。本篇只建立接口：**資訊失真不只發生在命題集合，也可能發生在關係、順序與箭頭。**

---

# 7　選擇性真實為何對 fact-checking 特別棘手

傳統 misinformation defense 常聚焦：

$$
\text{Is claim }f\text{ true or false?}
$$

這對 commission lie 非常重要。

但對 selective truth 而言，fact checker 可能檢查完所有可見句子後得到：

$$
100\%\ \mathrm{true}.
$$

仍然沒有回答：

1. 還有哪些相關事實沒有出現？
2. 被選出的正反證是否按重要性代表母集合？
3. 是否重複了同一個 primary source？
4. 是否把相關性排列成因果性？
5. 是否存在被壓低顯著度的 decisive counterevidence？
6. 若改用另一個合理 selection policy，receiver 的判斷會不會劇烈改變？

因此：

$$
\boxed{
\text{Fact-checking is necessary, but fact-checking alone is not sufficient.}
}
$$

需要補上一個：

$$
\text{selection audit}.
$$

---

# 8　來源重複：文件很多，不代表證據很多

選擇性真實還有一個容易被忽略的變形：相同 primary source 被多個 secondary source 重複。

令：

$$
N_D
$$

為文件數，

$$
N_I
$$

為獨立資訊來源數。

則：

$$
N_D\gg N_I
$$

完全可能。

2022 與 2026 關於 illusion of consensus 的研究顯示，人可能無法充分折扣 dependent consensus；多篇文章重複同一來源，仍能比只看到一篇來源提高信心，且在某些情境下效果可接近獨立共識。

因此：

$$
\boxed{
\text{Repetition Count}
\neq
\text{Independent Evidence Count}.
}
$$

這將是後續「認識論拓撲」的重要元素：source graph 的依賴關係必須被顯式建模。

---

# 9　Framing：邏輯等價不代表資訊等價

framing 研究提供另一個必要修正。

某些描述在形式上可能是 logically equivalent，但在語用上未必 informationally equivalent。近年的 framing 文獻再次提醒：不能把所有 framing effect 都直接判成 irrationality；某些 frame 可能洩漏 speaker 所掌握的背景資訊、基準或意圖。

這表示：

$$
\text{Logical Equivalence}
\not\Rightarrow
\text{Pragmatic Equivalence}.
$$

因此本文不能簡化成：

> 只要同一組事實換一種講法，就是操縱。

真正要問的是：

$$
\text{Does the frame encode additional relevant information, or selectively steer interpretation?}
$$

這一區分使本文保持對 receiver rationality 的開放：有些看似 framing bias 的更新，可能其實是 receiver 對 speaker selection policy 的合理推斷。

---

# 10　從「真話」到「代表性真話」：一個較強的認識論要求

單句真值要求：

$$
T_1(M):
\forall f\in M,\quad f=\mathrm{true}.
$$

但若訊息宣稱自己在提供「總結」「分析」「客觀評估」「現況」或「主要證據」，還需要第二層要求：

$$
T_2(M,F_R):
M\ \text{is sufficiently representative of}\ F_R(W).
$$

然而「代表性」不能要求完整揭露，否則任何摘要都不可能成立。

所以應改成任務相對形式：

$$
\mathrm{Rep}(M\mid Q,\rho,\epsilon),
$$

其中：

- $Q$：receiver 正在回答的問題；
- $\rho$：需要的解析度；
- $\epsilon$：允許的剩餘資訊失真。

這與過程類完備性的想法一致：不是要求無限完整，而是要求剩餘省略不再足以改變當前問題的關鍵判斷。

---

# 11　啟發式形式量

本節所有指標均為 proposed heuristic，不宣稱已獲實證驗證。

## 11.1 Selection Distortion Gap

令 receiver 在完整相關證據下的目標判斷為：

$$
J(F_R),
$$

在選擇性訊息下為：

$$
J(M).
$$

定義：

$$
\boxed{
\mathrm{SDG}
=
d\left(J(M),J(F_R)\right).
}
$$

 $\mathrm{SDG}$ 大，表示即使 $M$ 內全部為真，選擇政策仍造成大幅判斷偏移。

---

## 11.2 Counterevidence Omission Ratio

令與核心命題 $H$ 相衝突的高相關證據集合為：

$$
C^{-}(H).
$$

被訊息揭露者為：

$$
C^{-}_M(H).
$$

可定義加權 omission：

$$
\boxed{
\mathrm{COR}
=
1-
\frac{
\sum_{c\in C^{-}_M(H)}w(c)
}{
\sum_{c\in C^{-}(H)}w(c)
}.
}
$$

當 $\mathrm{COR}$ 接近 $1$，表示重要反證大多沒有進入訊息。

難點在於 $w(c)$ 本身需要獨立程序估計，不能由 sender 單方面決定。

---

## 11.3 Selection Policy Sensitivity

取一組可辯護的替代選擇政策：

$$
\Pi^{*}=\{\pi_1,\pi_2,\ldots,\pi_k\}.
$$

比較 receiver judgement：

$$
J_i=J(\pi_i(F_R)).
$$

定義：

$$
\boxed{
\mathrm{SPS}
=
\mathrm{Dispersion}(J_1,\ldots,J_k).
}
$$

若 $\mathrm{SPS}$ 很高，代表「結論」高度依賴資訊抽樣政策，而不是只依賴底層事實。

---

## 11.4 Topological Distortion Index

令完整關係圖為：

$$
G_R=(V_R,E_R),
$$

訊息誘導的關係圖為：

$$
G_M=(V_M,E_M).
$$

概念性定義：

$$
\boxed{
\mathrm{TDI}
=
d_G(G_M,G_R),
}
$$

其中 $d_G$ 可依任務採用 edge edit distance、causal graph discrepancy 或其他圖距離。

它要測的不是句子真假，而是：**訊息讓 receiver 看到的關係拓撲距離可支持的完整拓撲有多遠。**

---

# 12　Truthful-Message Audit Protocol（TMAP）

本文提出一套可供人類、AI、媒體與研究系統使用的初步審查程序。

## Step 1：Freeze the Question

先固定問題 $Q$。

因為沒有問題域，就沒有「相關事實母集合」。

---

## Step 2：Verify Local Truth

逐句檢查：

$$
f\in M
$$

是否為真。

這一步仍然不可省略。

---

## Step 3：Recover the Missing Parent Set

追問：

> 這些真話是從哪個更大的證據集合抽出來的？

建立：

$$
F_R(W).
$$

實務上只能近似，不要求全知。

---

## Step 4：Counterevidence Search

主動搜尋：

$$
C^{-}(H).
$$

尤其是如果加入後會改變結論的 decisive counterevidence。

---

## Step 5：Alternative Sampling

至少建立兩個不共享同一 objective 的摘要：

$$
M_1=\pi_1(F_R),
$$

$$
M_2=\pi_2(F_R).
$$

若結論劇烈改變，標記高 SPS。

---

## Step 6：Source Independence Audit

建立來源圖，區分：

$$
N_D
$$

與：

$$
N_I.
$$

多文件引用同一 primary source 不得計為多個獨立證據。

---

## Step 7：Ordering and Edge Audit

檢查訊息是否藉由排序暗示：

$$
A\rightarrow B
$$

但實際只有：

$$
A\ \text{and}\ B.
$$

將 proposition truth 與 relation validity 分離。

---

## Step 8：Concession Audit

檢查是否只揭露低成本缺點來營造平衡感，同時隱去高權重反證。

---

## Step 9：State the Selection Policy

若可行，要求 sender 或系統聲明：

- 摘要目的；
- 排序準則；
- 收錄／排除條件；
- 資料截止時間；
- 是否針對特定 receiver 個人化。

---

## Step 10：Return a Representativeness Verdict

最後輸出至少兩個結論：

$$
\text{Local Truth Status}
$$

與：

$$
\text{Selection / Representativeness Status}.
$$

不得再把兩者合成一個單一「真假」標籤。

---

# 13　對 AI 的直接含義：不要只做 fact verifier，也要做 sampler auditor

對 AI 系統而言，傳統安全設計很容易聚焦：

$$
\text{Do not fabricate facts.}
$$

但一個完全不 hallucinate 的 AI 仍可能因 retrieval、ranking、memory、personalization 或 summary objective 而產生：

$$
\text{truthful but selectively distorted output}.
$$

因此：

$$
\boxed{
\text{Hallucination-free}
\not\Rightarrow
\text{epistemically neutral}.
}
$$

AI 評估至少要再加入：

- evidence coverage；
- counterevidence retrieval；
- source dependence；
- ranking sensitivity；
- alternative summary stability；
- omitted decisive evidence；
- user-conditioned selection effects。

這也說明：AI 未來的 epistemic safety 不能只靠「多聯網、多引用、多 fact-check」。

如果所有搜尋與引用都由同一個 selection objective 排序，系統仍可能把一組全部正確的資料組合成高度單向的世界。

---

# 14　對政治、科學、哲學與信念系統的適用邊界

本文架構可以應用到政治意識形態、宗教敘事、科學主義、哲學、本體論、數學哲學、商業宣傳或任何 worldview，但這不表示本文判定上述領域本身為 deception。

應區分：

$$
\text{Domain}
$$

與：

$$
\text{Selection Behavior within the Domain}.
$$

任何領域都可能：

- 主動找反例；
- 明確區分已知與未知；
- 揭露競爭解釋；
- 接受外部證據更新。

也都可能反過來形成選擇性真實。

所以本文的批判對象始終是：

$$
\boxed{
\text{the information-selection process, not the identity of the belief system.}
}
$$

---

# 15　可證偽性與自我限制

本文本身也可能犯選擇性真實，因此必須明示其失敗條件。

至少以下結果會迫使本文核心框架修正：

## F1：Truth implies representativeness under realistic communication

若大量實證顯示，在真實溝通中，只要所有句子為真，receiver 的整體判斷通常就與完整證據評估沒有實質差異，則本文高估了 selection policy 的作用。

---

## F2：Receivers robustly infer selection policy

若 receiver 在未知 sender 目標時仍能穩定、準確地反推出 $\pi$ 並正確折扣 selective disclosure，則本文對 identification problem 的描述需弱化。

---

## F3：Alternative sampling has negligible effect

若對相同母集合採用多個合理選擇政策後：

$$
\mathrm{SPS}\approx0,
$$

則本文所擔心的抽樣失真在該域中不重要。

---

## F4：The proposed metrics fail to predict human judgement shifts

若 $\mathrm{SDG}$ 、 $\mathrm{COR}$ 、 $\mathrm{SPS}$ 、 $\mathrm{TDI}$ 等指標無法與人類判斷偏移、錯誤決策或認知失真產生可重現關係，則它們應被捨棄或重構。

---

## F5：Framing effects are fully explained by legitimate information leakage

若特定 framing 差異完全可由 receiver 對 speaker background knowledge 的合理推斷解釋，則不得把該 framing 歸類為 manipulation。本文因此拒絕把所有 frame dependence 預設為偏誤。

---

# 16　與後續 Series B 的關係

SET01 建立的是整個 Series B 最底層的第一個分離：

$$
\boxed{
\text{Truth of selected statements}
\neq
\text{neutrality of the selecting process}.
}
$$

後續預定展開：

- SET02：聽者的不可識別問題；
- SET03：策略性讓步、張力控制與可信度工程；
- SET04：真誠的人也能產生選擇性世界；
- SET05：信念系統作為 admissible-arrow systems；
- SET06：真節點與假拓撲；
- SET07：認識論吸引子與自我封閉。

因此，本篇不是欺騙術指南，而是建立一個認識論警告：**truthfulness 是必要條件，但在有選擇、壓縮與有限頻寬的溝通世界裡，它不是充分條件。**

---

# 結論

「高明的謊言只說真話」是一句有力的直覺，但若停在修辭層面，仍然太粗糙。

更精確的版本應是：

$$
\boxed{
\text{A sender can preserve the truth value of every transmitted statement while changing the receiver's world model through information selection.}
}
$$

這個機制不只屬於惡意說謊者。

它也可能存在於：

- 善意摘要；
- 媒體編輯；
- 政治傳播；
- 商業 disclosure；
- 科學敘事；
- 哲學論證；
- 搜尋排序；
- AI retrieval；
- 個人記憶；
- 真誠信念系統。

因此真正成熟的 receiver 不能只問：

> **這句話是真的嗎？**

還必須再問：

> **為什麼我現在看到的是這些真話？**

以及：

> **如果由另一個同樣合理、但目標不同的選擇政策重新抽樣，我看到的世界會不會變？**

這三個問題共同構成本文的最低認識論防線。

$$
\boxed{
\text{Truth-check the statements; audit the sampler; reconstruct the missing world.}
}
$$

---

# References

1. Rogers, T., Zeckhauser, R., Gino, F., Norton, M. I., & Schweitzer, M. E. (2017). *Artful paltering: The risks and rewards of using truthful statements to mislead others*. Journal of Personality and Social Psychology, 112(3), 456–473. https://doi.org/10.1037/pspi0000081

2. Kamenica, E., & Gentzkow, M. (2011). *Bayesian Persuasion*. American Economic Review, 101(6), 2590–2615. https://doi.org/10.1257/aer.101.6.2590

3. Kamenica, E. (2019). *Bayesian Persuasion and Information Design*. Annual Review of Economics, 11, 249–272. https://doi.org/10.1146/annurev-economics-080218-025739

4. Hoffmann, F., Inderst, R., & Ottaviani, M. (2020). *Persuasion Through Selective Disclosure: Implications for Marketing, Campaigning, and Privacy Regulation*. Management Science. https://doi.org/10.1287/mnsc.2019.3455

5. Loewenstein, G., Sunstein, C. R., & Golman, R. (2014). *Disclosure: Psychology Changes Everything*. Annual Review of Economics, 6, 391–419. https://doi.org/10.1146/annurev-economics-080213-041341

6. Connor Desai, S., Xie, B., & Hayes, B. K. (2022). *Getting to the source of the illusion of consensus*. Cognition, 223, 105023. https://doi.org/10.1016/j.cognition.2022.105023

7. Connor Desai, S., Fai, J., Lee, J., et al. (2026). *Explaining away the illusion of consensus*. Memory & Cognition, 54, 1667–1687. https://doi.org/10.3758/s13421-025-01831-9

8. Powell, D., Bian, L., & Markman, E. M. (2020). *When intents to educate can misinform: Inadvertent paltering through violations of communicative norms*. PLOS ONE, 15(5), e0230360. https://doi.org/10.1371/journal.pone.0230360

9. McKenzie, C. R. M., Sher, S., Liu, X. S., et al. (2025). *When and why framing effects are neither errors nor mistakes*. Mind & Society, 24, 209–229. https://doi.org/10.1007/s11299-025-00338-9

10. Ghasemi, O. (2024). *Reframing rational judgement*. Nature Reviews Psychology, 3, 508. https://doi.org/10.1038/s44159-024-00340-x

11. DellaVigna, S., & Gentzkow, M. (2010). *Persuasion: Empirical Evidence*. Annual Review of Economics, 2, 643–669. https://doi.org/10.1146/annurev.economics.102308.124309

12. Krähmer, D. (2021). *Information Design and Strategic Communication*. American Economic Review: Insights, 3(1), 51–66. https://doi.org/10.1257/aeri.20200012

---

# 保真聲明

本文的文獻性陳述以 references 所列研究為依據；本文提出的 Truthful Selection Model、Selection Distortion Gap、Counterevidence Omission Ratio、Selection Policy Sensitivity、Topological Distortion Index 與 Truthful-Message Audit Protocol 均屬作者提出之理論化與啟發式工具，尚未經獨立實證確認。

本文不宣稱所有資訊選擇均為欺騙，也不宣稱 sender 的主觀意圖可以僅從輸出訊息反推出來。對欺騙、說服、善意摘要、真誠偏差與中性壓縮的區分，必須依賴額外的目的、可得資訊與反事實行為證據。

本文所提出的選擇審查程序亦適用於本文自身；若本文只挑選支持自身的 paltering、persuasion 與 framing 文獻而忽略重要反證，則本文將以自己的判準失敗。

---

*SET01 / Selective Truth and Epistemic Topology / v0.1 / 2026-09-07*
