# SET02｜聽者的不可識別問題：當客觀評估與策略性真話產生相同表面訊息
## The Listener's Identification Problem: When Neutral Evaluation and Strategic Truth Produce the Same Observable Message

**定位：** Selective Truth and Epistemic Topology / Foundation Paper 02 / Listener-Side Identification  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-07  
**狀態：** Canonical Source / UTF-8 Markdown  
**文件性質：** Epistemology / Pragmatics / Strategic Communication / Information Design / Source Monitoring / Identifiability / Selective Disclosure

---

## Canonical Source Note

本文件之正式原稿為此 UTF-8 Markdown source。任何 HTML、PDF、LaTeX rendering、聊天介面顯示或其他格式皆屬 projection，不取代 canonical source。

數學公式 canonical delimiter 僅使用：

- inline math：` $...$ `
- display math：`$$...$$`

本文不針對任何特定人物、政黨、宗教、哲學學派、科學學派、媒體或 AI 系統。本文研究的是一個一般性的接收端問題：**當不同的資訊生成政策可以產生相同的表面訊息時，聽者是否能僅憑已收到的訊息辨認其認識論來源？**

本文承接 SET01 的基本命題：

$$
\boxed{
\text{Statement Truth}
\neq
\text{Selection Neutrality}
\neq
\text{Message Representativeness}.
}
$$

SET01 主要研究 sender 如何透過選擇、遺漏、排序與 framing，使句句真話仍可能形成失真世界；SET02 則把焦點移到 receiver：**如果訊息本身不足以識別其生成政策，那麼「我已經 fact-check 每一句」仍不足以恢復訊息的認識論地位。**

---

# 摘要

本文提出 **Listener Identification Problem（LIP）**：接收者通常只能觀察到訊息 $M$，卻看不到產生該訊息的完整世界狀態 $W$ 、可選訊息集合 $\mathcal A(W)$ 、資訊選擇政策 $\pi$ 、sender 的資訊可得性 $K_S$ 、目標 $G_S$ 與未被選中的反事實訊息。若兩個不同政策 $\pi_1$ 與 $\pi_2$ 在同一世界狀態下產生相同可觀測訊息，

$$
\pi_1(F(W))=\pi_2(F(W))=M,
$$

但

$$
\pi_1\neq\pi_2,
$$

則 receiver 僅憑 $M$ 無法唯一識別其生成政策。本文稱此為 **policy-level observational equivalence**。

此問題並不表示人類永遠無法推斷 speaker intent。語用學恰恰表明，聽者會利用上下文、替代句、speaker knowledge、intentionality 與 cooperative assumptions 反推「為什麼說這句而不是別句」。2025 年 Bohn 與 Frank 的實驗進一步顯示，成人的 pragmatic inference 會受到 speaker epistemic state 與 intentional action 的調節。然而，這種推斷依賴額外線索；當 selection policy、可選替代訊息與 sender incentives 不可見時，訊息本身仍可能存在不可識別性。

經濟學中的 strategic information transmission、Bayesian persuasion 與 information design 為此提供另一條正式脈絡：資訊提供者不必改變世界狀態，只需設計揭露政策，即可系統性改變 receiver 的 posterior 與行動。2026 年關於 endogenous verification 的研究甚至直接把 receiver 是否付出成本驗證納入模型，說明 sender 的 optimal disclosure policy 會同時影響「接受」與「是否驗證」。因此，驗證成本不是溝通之外的細節，而可能進入資訊設計本身。

心理學與記憶研究又增加第三層困難：receiver 不僅在當下看不到生成政策，隨時間經過，source-specifying cues 與 source credibility 也可能比 proposition familiarity 更快弱化。因而一段最初帶有「這是誰說的、為何這樣選、可信度如何」的訊息，日後可能只剩下內容本身的熟悉感。

本文因此主張：

$$
\boxed{
\text{Message Verification}
\not\Rightarrow
\text{Policy Identification}.
}
$$

以及：

$$
\boxed{
\text{Observed Message}
\not\Rightarrow
\text{Observed Selection Process}.
}
$$

本文建立 **Message-Policy Equivalence Class（MPEC）**、**Policy Opacity Gap（POG）**、**Counterfactual Disclosure Asymmetry（CDA）**、**Alternative-Set Visibility（ASV）** 與 **Verification Cost Exposure（VCE）** 等啟發式量，並提出 **Listener Identification Audit Protocol（LIAP）**。LIAP 不要求 receiver 猜中 sender 的內心，而是要求將不可識別性本身顯式化：列出可能生成政策、要求替代抽樣、檢查反事實揭露對稱性、追問來源獨立性、降低驗證成本，最後才決定訊息可被賦予多高的認識論權重。

本文的核心結論不是「不要相信別人」，而是：

$$
\boxed{
\text{When the generator is hidden, confidence should track identifiability, not fluency.}
}
$$

一段話愈流暢、愈平衡、愈像客觀評估，並不自動使其生成過程更可識別。真正的客觀性不只是一種表面語氣，而是一種可追溯、可反事實檢查、可比較替代抽樣政策的生成結構。

---

# 0　問題起點：同一句話，可以來自完全不同的世界模型

考慮一段訊息：

> 這個方案確實有若干重要優點，也存在幾個需要正視的限制；綜合目前資料，我傾向認為它值得推進，但不應高估其成熟度。

這段話可以由至少兩種不同政策產生。

政策一：

$$
\pi_N=\text{neutral evidence sampler}.
$$

sender 檢視正反證、按照相關性與權重抽樣，再產生平衡結論。

政策二：

$$
\pi_S=\text{strategic credibility sampler}.
$$

sender 想讓 receiver 支持方案，因此主動加入一個低成本負面項目以建立可信度，同時省略真正可能改變決策的高權重反證。

兩者最後都可以生成完全相同的字串 $M$：

$$
M_{\pi_N}=M_{\pi_S}.
$$

如果 receiver 只觀察到 $M$，則：

$$
M_{\pi_N}=M_{\pi_S}
\not\Rightarrow
\pi_N=\pi_S.
$$

這就是本文的最小不可識別問題。

問題不是：

> 這句話是真是假？

因為兩個 sender 都可以句句為真。

真正的問題是：

> 這段話是從什麼母集合裡、透過什麼政策、在什麼可選替代訊息中，被選出來的？

---

# 1　從訊息真值到生成政策

## 1.1 可觀測訊息與隱藏生成變量

令：

- $W$：世界狀態；
- $F(W)$：與問題相關的事實集合；
- $K_S$：sender 可取得的資訊；
- $G_S$：sender 的目標或效用結構；
- $\mathcal A(W)$：sender 當下可生成的替代訊息集合；
- $\pi$：selection / disclosure policy；
- $M$：receiver 實際觀察到的訊息。

可寫成：

$$
M=\pi(F(W),K_S,G_S,\mathcal A(W),C),
$$

其中 $C$ 代表對話、制度、時間與媒介 context。

receiver 通常只看到：

$$
M.
$$

但真正決定訊息認識論地位的變量至少包含：

$$
(W,K_S,G_S,\mathcal A,\pi,C).
$$

因此：

$$
\boxed{
\text{message content is an observation of a generative process, not the process itself}.
}
$$

---

## 1.2 Message-Policy Equivalence Class

對一個已觀察訊息 $M$，定義其可能生成政策集合：

$$
\mathcal P(M)
=
\left\{
\pi:
\exists W,K_S,G_S,\mathcal A,C
\text{ such that }
\pi(F(W),K_S,G_S,\mathcal A,C)=M
\right\}.
$$

若：

$$
|\mathcal P(M)|>1,
$$

則 $M$ 對 selection policy 非唯一識別。

進一步，定義 **Message-Policy Equivalence Class（MPEC）**：

$$
[\pi]_M
=
\left\{
\pi':
P(M\mid \pi')=P(M\mid \pi)
\right\}.
$$

若多個具有不同認識論品質的政策落在同一個 equivalence class，receiver 只看 $M$ 時就無法知道自己面對的是：

- neutral sampling；
- strategic sampling；
- sincere biased sampling；
- editorial compression；
- random omission；
- algorithmic ranking；
- adversarial persuasion。

這裡的「不可識別」不是形上學宣稱，而是相對於 receiver 可取得的 observation set。

---

# 2　語用學其實早就在問：為什麼你說這句？

Gricean pragmatics 的核心之一，就是聽者不只解碼字面內容，也會推斷 speaker 為什麼在可選語句中選擇當前語句。

若 sender 可說：

$$
u_1,u_2,\ldots,u_n,
$$

卻選擇 $u_k$，則 receiver 會把「選擇 $u_k$ 」本身當成資訊。

因此：

$$
P(W\mid u_k)
$$

實際上依賴 receiver 對 speaker choice model 的假設：

$$
P(u_k\mid W,\pi).
$$

2025 年 Bohn 與 Frank 以六項線上實驗研究 pragmatic inference，發現成人的推論會隨 speaker epistemic state 與 action intentionality 改變。這支持一個重要原則：

$$
\boxed{
\text{utterance interpretation depends partly on inferred choice conditions}.
}
$$

但這也暴露 LIP：如果 receiver 不知道 speaker 實際知道什麼、不知道有哪些替代句可選、不知道選擇是否有意識，也不知道 sender incentives，那麼 pragmatic inference 必然帶有模型不確定性。

因此本文不否定 pragmatic competence，而是主張：

$$
\text{pragmatic inference}
\neq
\text{guaranteed policy identification}.
$$

---

# 3　speaker intention 與 hearer meaning：私有變量與接收端結果

2025 至 2026 年 Journal of Pragmatics 關於 speaker intention 與 Hearer's Meaning 的討論，重新凸顯一個老問題：speaker intention 是私有心理狀態，receiver 不能直接讀取，只能從 utterance、context、roles 與其他線索推斷。

本文不需要在「speaker intention 是否最終決定 meaning」這個哲學爭議上選邊。對 LIP 而言，只需要較弱的命題：

$$
\boxed{
\text{receiver does not directly observe speaker intention}.
}
$$

因此，無論採 speaker-centered 或 hearer-centered 理論，都不能把：

$$
\text{surface utterance}
$$

直接等同：

$$
\text{generation policy}.
$$

這也解釋了為什麼「他聽起來很客觀」只是一個 observation，而不是 policy certificate。

---

# 4　策略溝通：truthfulness 不消除 incentive problem

## 4.1 Crawford-Sobel 型問題

Strategic Information Transmission 的經典 sender-receiver 模型指出：當 sender 擁有 receiver 沒有的資訊，且雙方偏好不完全一致時，訊息的 informativeness 取決於 incentive alignment。

關鍵不是 sender 一定說假話。

即使 communication 在某些 equilibrium 中包含 truthful partition information，receiver 仍必須把：

$$
\text{sender incentives}
$$

納入解碼。

因此：

$$
\boxed{
\text{truthful communication}
\not\Rightarrow
\text{interest-free communication}.
}
$$

---

## 4.2 Bayesian persuasion 與 information design

Bayesian persuasion 更直接把「資訊怎麼被揭露」本身視為設計變量。

令 state 為 $\theta$，sender 選擇 signal structure $\sigma$，receiver 根據 signal $s$ 更新：

$$
P(\theta\mid s,\sigma).
$$

receiver 的 rationality 並不能消除 persuasion，因為 posterior 本來就取決於 signal structure。

因此：

$$
\boxed{
\text{rational receiver}
+
\text{strategic disclosure}
\neq
\text{neutral posterior}.
}
$$

這對 SET02 很重要：LIP 並不是「聽者太笨」才發生。只要 receiver 不知道或無法充分識別 disclosure policy，就算他的 Bayesian update 在給定模型下完全正確，model uncertainty 仍然存在。

---

# 5　驗證成本：為什麼「自己去查」不是免費解法

2026 年 Yang 的 information design with endogenous state verification，把 receiver 是否驗證世界狀態納入模型，並讓驗證具有成本。

令驗證成本為：

$$
c_v>0.
$$

receiver 在看到訊息 $M$ 後，可以：

1. 直接接受；
2. 直接拒絕；
3. 支付 $c_v$ 進行額外驗證。

sender 的 optimal disclosure policy 會考慮 receiver 的這個選擇。

因此：

$$
\boxed{
\text{verification cost enters the communication game}.
}
$$

這指出一個現實問題：如果每一段訊息都要求 receiver 自己重建所有 primary sources、反證與未揭露母集合，認識論成本可能高到不可行。

所以「不要相信，自己查」不是完整制度解。

真正需要的是降低：

$$
c_v,
$$

例如：

- 顯示 primary source；
- 提供完整 evidence table；
- 標記省略範圍；
- 公開 selection criteria；
- 提供可重跑搜尋式；
- 保存 provenance；
- 分離原始資料與評論；
- 提供 counterevidence channel。

客觀性不應只靠 receiver 的懷疑能力，而應部分由資訊系統的可驗證設計承擔。

---

# 6　omission 為什麼特別難從表面偵測

2025 年 Vrij、Leal、Deeb 與 Fisher 的 omission-lie 研究讓 participants 在訪談中刻意省略部分事件。結果顯示，omission-liars 所說內容仍大部分是真實的，而且傳統 verbal veracity cues 並沒有提供簡單、穩健的辨識方式。

這支持本文的一個保守判斷：

$$
\boxed{
\text{surface truthfulness cues are weak evidence about completeness}.
}
$$

但本文不把「omission」一律等同 deception。摘要、新聞、教學、科學論文與一般對話都必然省略大量資訊。

真正應檢查的是：

$$
\text{decision-relevant omission}.
$$

也就是被省略項目一旦加入，是否會顯著改變：

$$
P(H\mid M),
$$

排序、決策、風險估計或信任判斷。

---

# 7　看起來誠實，不等於生成政策中性

2025 年 Mac Giolla 與 Stenbock 的 self-presentational deception 實驗發現，在該研究條件下，參與者「以誠實者方式呈現」比陳述本身真或假更能預測 receiver 的 credibility judgment。

本文不把單一實驗外推成普遍法則，但它提供一個重要提醒：

$$
\boxed{
\text{credibility cues}
\neq
\text{veracity cues}
\neq
\text{policy-neutrality cues}.
}
$$

一個 sender 可以：

- 語氣冷靜；
- 主動承認小缺點；
- 使用精確數字；
- 引用可靠來源；
- 表示不確定；
- 避免誇張詞；
- 提供看似對稱的 pros/cons；

而仍然使用高度策略性的 selection policy。

因此「像客觀的人」與「採用客觀抽樣政策」必須分開。

---

# 8　source monitoring：時間會把生成條件從內容上剝離

receiver 當下即使知道：

- 這句話來自誰；
- 該來源可靠度如何；
- 它是廣告、評論、研究、轉述還是朋友意見；

這些 source-specifying cues 也不一定與 proposition 同等穩定地保留。

Henkel 與 Mattson 的五項實驗顯示，重複陳述會提高 perceived truth，即使資訊來自不可靠來源；在 source memory 薄弱時，familiarity 更容易成為 truth judgment 的替代線索。

更早的 source-monitoring misinformation 研究也觀察到，隨 retention interval 拉長，人更可能把後來看到的 misinformation 錯誤歸因到原始事件。

因此 SET02 再增加一個時間維度：

$$
(M,\pi,S)_{t_0}
\longrightarrow
(M,\hat\pi,\hat S)_{t_1},
$$

其中：

$$
d(\hat S,S)
$$

與

$$
d(\hat\pi,\pi)
$$

可能隨時間增大。

最後留下的是：

$$
\text{message familiarity},
$$

而不是：

$$
\text{generation-policy memory}.
$$

---

# 9　正式命題一：Observed Message 不識別 Selection Policy

**命題 1（Policy Non-Identification）**

若存在：

$$
\pi_1\neq\pi_2
$$

使得對某一可觀測條件集合 $\mathcal O$，

$$
P(M\mid\pi_1,\mathcal O)
=
P(M\mid\pi_2,\mathcal O),
$$

則 receiver 僅憑 $M$ 與 $\mathcal O$ 無法區分 $\pi_1$ 與 $\pi_2$。

這不是新數學定理，而是 identifiability 的直接定義性結果。其認識論意義在於：

$$
\boxed{
\text{identical observable outputs can conceal different epistemic generators}.
}
$$

因此「訊息看起來一樣」不能作為「生成政策一樣」的證據。

---

# 10　正式命題二：Bayesian 更新也需要 policy prior

receiver 若想根據 $M$ 更新 hypothesis $H$，更完整的形式不是：

$$
P(H\mid M)
\propto
P(M\mid H)P(H),
$$

而是：

$$
P(H\mid M)
=
\sum_{\pi}
P(H,\pi\mid M).
$$

其中：

$$
P(H,\pi\mid M)
\propto
P(M\mid H,\pi)P(H,\pi).
$$

若 receiver 偷偷假設：

$$
\pi=\pi_N
$$

為 neutral sampler，但真實政策可能是 $\pi_S$，則即使 Bayes rule 算得完全正確，posterior 仍可能因 model misspecification 而失真。

因此：

$$
\boxed{
\text{Bayesian coherence}
\neq
\text{correct generator model}.
}
$$

這也回應一個更一般的問題：知道 Bayesian updating 並不能自動免疫 selection bias，因為 evidence 本身不是從真空掉下來的。

---

# 11　Counterfactual Disclosure Test：如果方向反過來，你還會這樣說嗎？

判斷 selection policy 的一個實用方法不是讀 sender 的內心，而是做反事實檢查。

令 $F^{+}$ 為支持 $H$ 的證據， $F^{-}$ 為反對 $H$ 的證據。

問：

> 若證據方向完全反過來，sender 是否仍會用同樣的揭露規則？

可定義啟發式 **Counterfactual Disclosure Asymmetry（CDA）**：

$$
\mathrm{CDA}
=
d\left(
\pi(F^{+}),
\mathcal R\left(\pi(F^{-})\right)
\right),
$$

其中 $\mathcal R$ 是把正反方向交換後的對稱映射， $d$ 是政策差異量。

若：

$$
\mathrm{CDA}\approx0,
$$

表示政策對證據方向相對對稱。

若：

$$
\mathrm{CDA}\gg0,
$$

則可能存在方向性 selection。

此量尚無公認測度，本文僅提出概念骨架。

---

# 12　Alternative-Set Visibility：你看得到「他本來還能說什麼」嗎？

聽者常只看到 actual message：

$$
M.
$$

但 pragmatic inference 真正需要的是：

$$
M
\in
\mathcal A(W),
$$

以及：

$$
\mathcal A(W)\setminus\{M\}.
$$

也就是 sender 還有哪些可選訊息。

本文定義啟發式 **Alternative-Set Visibility（ASV）**：

$$
\mathrm{ASV}\in[0,1].
$$

當 receiver 完全不知道：

- 有哪些資料被考慮；
- 有哪些資料被排除；
- 哪些反證存在；
- 哪些來源沒有被選；
- 搜尋條件如何設定；

則：

$$
\mathrm{ASV}\rightarrow0.
$$

當 selection criteria、候選來源、excluded evidence 與檢索式高度可追溯：

$$
\mathrm{ASV}\rightarrow1.
$$

ASV 的核心不是要求所有內容都展示，而是要求**選擇空間可被稽核**。

---

# 13　Policy Opacity Gap

令 receiver 對 policy 的估計為：

$$
\hat\pi_R.
$$

真實生成政策為：

$$
\pi.
$$

定義概念性 **Policy Opacity Gap（POG）**：

$$
\mathrm{POG}
=
d(\pi,\hat\pi_R).
$$

實務上 $\pi$ 通常不可直接觀察，所以 POG 不能被直接精確計算。

因此本文更重視可觀測 proxies：

- policy disclosure；
- provenance completeness；
- counterfactual consistency；
- alternative-set visibility；
- source independence；
- verification accessibility。

POG 的用途是提醒：

$$
\boxed{
\text{confidence in message}
\text{ should not exceed confidence in the generator model without justification}.
}
$$

---

# 14　Verification Cost Exposure

令 receiver 若要從 $M$ 重建重要生成條件，所需成本為：

$$
C_V(M).
$$

定義 **Verification Cost Exposure（VCE）**：

$$
\mathrm{VCE}
=
\frac{C_V(M)}
{C_{\mathrm{decision}}},
$$

其中 $C_{\mathrm{decision}}$ 是該決策合理可承擔的驗證成本尺度。

若：

$$
\mathrm{VCE}\gg1,
$$

則即使理論上「可以自行查證」，實際上 receiver 也高度依賴 sender。

因此：

$$
\boxed{
\text{nominal verifiability}
\neq
\text{practical verifiability}.
}
$$

一個健康資訊制度應降低 VCE，而不是只把驗證責任推回個體。

---

# 15　Listener Identification Audit Protocol（LIAP）

本文提出以下可執行程序。

## Step 1：Freeze the Message

保存原始訊息，不先改寫。

確認：

$$
M_{\mathrm{raw}}.
$$

避免後續記憶把 qualification、source 與 context 洗掉。

---

## Step 2：Separate Truth from Generation

先問：

> 句子是真的嗎？

再獨立問：

> 為什麼是這些真話？

即：

$$
\text{Veracity Audit}
\neq
\text{Generator Audit}.
$$

---

## Step 3：Reconstruct Candidate Policies

至少建立：

$$
\Pi_M
=
\{
\pi_N,
\pi_S,
\pi_B,
\pi_C,\ldots
\},
$$

例如：

- neutral sampler；
- strategic persuader；
- sincere biased sampler；
- compression policy；
- ranking algorithm；
- incomplete-knowledge sender。

不要求猜中，而是拒絕假設唯一政策。

---

## Step 4：Expose the Alternative Set

追問：

- 你考慮過哪些資料？
- 哪些沒有納入？
- 搜尋式是什麼？
- 哪些來源被排除？
- 為什麼？
- 有沒有高權重反證？

提高：

$$
\mathrm{ASV}.
$$

---

## Step 5：Run Counterfactual Disclosure

把 evidence direction 反轉。

問：

> 如果結果支持相反立場，你是否仍會採相同標準？

估計：

$$
\mathrm{CDA}.
$$

---

## Step 6：Audit Source Topology

區分：

$$
N_{\mathrm{documents}}
$$

與：

$$
N_{\mathrm{independent\ origins}}.
$$

避免重複來源被誤認為獨立共識。

---

## Step 7：Lower Verification Cost

優先要求：

- primary source；
- exact citation；
- data table；
- code；
- search log；
- preregistration；
- independent replication；
- provenance graph。

降低：

$$
C_V(M).
$$

---

## Step 8：Delay the Verdict

若：

$$
|\mathcal P(M)|\gg1
$$

且 ASV 低、VCE 高，則不必急著判 sender 惡意。

只需降低訊息的 epistemic weight：

$$
w(M)\downarrow.
$$

不可識別性本身就是一個合理的 uncertainty source。

---

# 16　這不是「懷疑所有人」

若 SET02 被讀成：

> 所有訊息都可能有 hidden policy，所以任何人都不可信。

那本文就失敗了。

因為這會造成：

$$
\text{universal skepticism}.
$$

而 universal skepticism 同樣不能工作。

本文真正主張的是 risk-sensitive identification：

$$
\text{audit intensity}
\propto
\text{decision stakes}
\times
\text{policy opacity}
\times
\text{verification asymmetry}.
$$

日常低風險溝通不需要每句都建 provenance graph。

但在：

- 科學理論；
- 醫療；
- 投資；
- 政策；
- 法律；
- 戰爭；
- 公共傳播；
- 高影響 AI 建議；

中，selection policy 的不可見性就應得到更高權重。

---

# 17　AI 時代：生成政策可以比 speaker 更不可見

本文不是 AI 專論，但 AI 讓 LIP 更尖銳。

人類 speaker 至少通常具有相對可理解的社會角色。

AI system 的訊息生成卻可能同時依賴：

$$
\text{training data}
+
\text{alignment}
+
\text{system instructions}
+
\text{memory}
+
\text{retrieval ranking}
+
\text{tool results}
+
\text{context compression}
+
\text{sampling}.
$$

所以：

$$
\pi_{\mathrm{AI}}
$$

甚至不是單一簡單政策。

一段看似「AI 的意見」，可能是多層 generator 的 composition：

$$
\pi_{\mathrm{AI}}
=
\pi_8\circ\pi_7\circ\cdots\circ\pi_1.
$$

因此人機協作若只保留 final answer，而不保留 sources、search path、tool provenance 與 evaluation procedure，LIP 會被放大。

---

# 18　與 SET01 的關係

SET01 的問題是：

$$
\boxed{
\text{How can truthful selection distort a world model?}
}
$$

SET02 的問題是：

$$
\boxed{
\text{How can a listener know which selection process produced the message?}
}
$$

兩者連起來：

$$
F(W)
\xrightarrow{\pi}
M
\xrightarrow{\mathcal D_R}
\hat W_R.
$$

SET01 研究第一支箭頭：

$$
F(W)\xrightarrow{\pi}M.
$$

SET02 研究 receiver 從 $M$ 反推 $\pi$ 與 $W$ 時的不可識別性：

$$
M
\not\Rightarrow
\pi.
$$

因此：

$$
\boxed{
\text{A truthful message can be epistemically underdetermined by its surface form.}
}
$$

---

# 19　可證偽性與研究議程

本文的若干部分是概念建模，不應假裝已被實證。

以下命題需要獨立驗證。

## H1：Identical-Message Policy Ambiguity

向受試者呈現完全相同訊息 $M$，但改變其已知生成政策資訊。

預測：

$$
P(\text{trust}\mid M,\pi_N)
\neq
P(\text{trust}\mid M,\pi_S).
$$

若 policy disclosure 幾乎不影響 receiver 判斷，本文對 policy-level cue 的重要性可能被高估。

---

## H2：Alternative-Set Visibility Effect

固定 $M$，分成：

- 只看 final message；
- 同時看候選 evidence pool；
- 同時看 included / excluded evidence；
- 同時看完整 selection rule。

測量：

$$
\Delta\mathrm{Calibration}.
$$

若 ASV 增加不改善判斷，則本文對 alternative-set audit 的價值需要修正。

---

## H3：Counterfactual Disclosure Detection

給 receiver 觀察 sender 在正反方向 evidence 下的 disclosure behavior。

測量 receiver 是否更能識別：

$$
\pi_N
$$

與：

$$
\pi_S.
$$

若無改善，CDA 的操作價值有限。

---

## H4：Verification-Cost Threshold

操縱查證成本：

$$
c_v^{(1)}
<
c_v^{(2)}
<
c_v^{(3)}.
$$

測量 receiver 是否在高 $c_v$ 下更依賴 sender 的 final framing。

若沒有關係，VCE 的制度重要性應降低。

---

## H5：Source-Policy Memory Decay

測量：

$$
t_0,\quad t_1,\quad t_2
$$

下 receiver 對：

- proposition；
- source；
- source credibility；
- selection policy；
- omitted evidence；

的記憶。

若 policy memory 並不比 proposition memory 更快衰退，本文的時間放大機制需要重寫。

---

# 20　自反性：本篇也有自己的不可識別問題

本文本身也是一段被選擇過的訊息。

它引用了：

- pragmatic inference；
- strategic communication；
- information design；
- omission；
- source monitoring；
- deception presentation。

但沒有引用所有可能相關文獻。

因此本文不能只要求別人公開 $\pi$，自己卻把自己的 selection policy 隱藏。

本篇目前的政策是：

1. 優先選取能支撐「message 與 generator 應分離」的經典與近期研究；
2. 同時納入至少一組會削弱過度懷疑的反方：人類確實有 pragmatic inference 能力，且 framing / selection 並非必然欺騙；
3. 不把「speaker intention」爭論假裝已有統一答案；
4. 不把任何 proposed metric 寫成已驗證測度；
5. 不把 policy non-identification 從特定 observation set 偷換成絕對不可知。

若未來研究顯示 receiver 在低成本條件下其實能非常準確地由表面訊息反推 selection policy，本文必須縮小 LIP 的適用域。

---

# 21　結論

接收者面對訊息時，通常最先問：

> 這是真的嗎？

這是必要問題。

但不是最後一個問題。

因為：

$$
M=\text{true}
$$

仍然沒有告訴你：

$$
\pi.
$$

而：

$$
\pi
$$

決定了你究竟看到世界的哪一部分。

本文因此提出三個最小原則。

第一：

$$
\boxed{
\text{Message Verification}
\not\Rightarrow
\text{Policy Identification}.
}
$$

第二：

$$
\boxed{
\text{Truthful communication can remain strategically or sincerely selective}.
}
$$

第三：

$$
\boxed{
\text{When the generator is hidden, confidence should track identifiability, not fluency}.
}
$$

真正高階的資訊素養，不只是辨認一句話是真是假。

而是知道：

> **同一句真話，可能由完全不同的世界模型與資訊政策產生；如果你看不到那些政策，就不要把表面的客觀語氣誤認成生成過程的客觀性。**

這不是要求每個人猜測別人的內心。

相反，它是一個更節制的要求：

$$
\boxed{
\text{When policy cannot be identified, represent the uncertainty instead of inventing certainty}.
}
$$

---

# References

1. Bohn, M., & Frank, M. C. (2025). Pragmatics as Social Inference About Intentional Action. *Open Mind*, 9, 290-304. https://doi.org/10.1162/opmi_a_00191

2. Crawford, V. P., & Sobel, J. (1982). Strategic Information Transmission. *Econometrica*, 50(6), 1431-1451.

3. Kamenica, E., & Gentzkow, M. (2011). Bayesian Persuasion. *American Economic Review*, 101(6), 2590-2615.

4. Yang, L. L. (2026). Information Design with Endogenous State Verification. *Journal of Economic Theory*, 235, 106182. https://doi.org/10.1016/j.jet.2026.106182

5. Vrij, A., Leal, S., Deeb, H., & Fisher, R. P. (2025). Omission Lies: The Effect of Omitting Little or Much Information on Verbal Veracity Cues. *European Journal of Psychology Applied to Legal Context*, 17(1), 25-37. https://doi.org/10.5093/ejpalc2025a3

6. Mac Giolla, E., & Stenbock, S. (2025). Acting Like a Liar: An Experimental Test of the Self-Presentational Theory of Deception. *Journal of Nonverbal Behavior*, 49, 377-391. https://doi.org/10.1007/s10919-025-00486-z

7. Henkel, L. A., & Mattson, M. E. (2011). Reading Is Believing: The Truth Effect and Source Credibility. *Consciousness and Cognition*, 20(4), 1705-1721. https://doi.org/10.1016/j.concog.2011.08.018

8. Echterhoff, G., Groll, S., & Hirst, W. (2007). Tainted Truth: Overcorrection for Misinformation Influence on Eyewitness Memory. *Social Cognition*, 25(3), 367-409. https://doi.org/10.1521/soco.2007.25.3.367

9. Wyler, H., & Oswald, M. E. (2016). Why Misinformation Is Reported: Evidence from a Warning and a Source-Monitoring Task. *Memory*, 24(10), 1419-1434. https://doi.org/10.1080/09658211.2015.1117641

10. Hall, A., & Mazzarella, D. (2023). Pragmatic Inference, Levels of Meaning and Speaker Accountability. *Journal of Pragmatics*, 205, 92-110. https://doi.org/10.1016/j.pragma.2022.12.007

11. Li, Y., & Xie, C. (2025). Defending Speaker Intention in a Model of the Hearer's Meaning. *Journal of Pragmatics*, 242, 126-140. https://doi.org/10.1016/j.pragma.2025.04.007

12. Hansen, M. B. M., & Terkourafi, M. (2026). Hearer's Meaning 2.0: A Reply to Li & Xie. *Journal of Pragmatics*, 261, 4-18. https://doi.org/10.1016/j.pragma.2026.04.007

---

## 系列位置

**Selective Truth and Epistemic Topology**

- SET01：高明的謊言不需要假話：選擇性真實、資訊抽樣與失真世界
- **SET02：聽者的不可識別問題：當客觀評估與策略性真話產生相同表面訊息**
- SET03：張力控制與策略性讓步：可信度如何被工程化
- SET04：真誠的人也能產生選擇性世界：Sincere Selection Bias
- SET05：信念系統不是信念集合，而是允許箭頭的系統
- SET06：真節點，假拓撲：資訊操縱如何發生在關係而非命題
- SET07：認識論吸引子與自我封閉：吸收無限資訊而幾乎不學習

---

*SET02 / Selective Truth and Epistemic Topology / EveMissLab / v0.1 / 2026-09-07*
