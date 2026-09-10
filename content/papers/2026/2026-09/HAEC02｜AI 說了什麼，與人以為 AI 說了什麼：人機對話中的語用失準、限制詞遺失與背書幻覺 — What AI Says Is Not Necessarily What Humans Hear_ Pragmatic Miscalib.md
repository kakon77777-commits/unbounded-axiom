# HAEC02｜AI 說了什麼，與人以為 AI 說了什麼：人機對話中的語用失準、限制詞遺失與背書幻覺
## What AI Says Is Not Necessarily What Humans Hear: Pragmatic Miscalibration, Qualifier Loss, and Endorsement Illusions in Human–AI Dialogue

**定位：** Human–AI Epistemic Calibration / Foundation Paper 02  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-07  
**狀態：** Canonical Source / UTF-8 Markdown  
**文件性質：** AI Epistemology / Pragmatics / Human–AI Communication / Uncertainty Communication / Memory / Calibration

---

## Canonical Source Note

本文件之正式原稿為此 UTF-8 Markdown source。任何 HTML、PDF、LaTeX rendering、聊天介面顯示或其他格式皆屬 projection，不取代 canonical source。

數學公式 canonical delimiter 僅使用：

- inline math：` $...$ `
- display math：`$$...$$`

本文不以任何特定人物、研究者、使用者或單一 AI 產品作為論證案例。本文討論的是可一般化的人機溝通與認識論機制；對任何個別人的心理狀態、模型使用史或信念形成歷程，若無直接證據，均不得由本文反推。

本文承接 HAEC01《同意不是驗證》所建立的認識論層級分離：理解、框架內一致、條件式可能、支持、驗證與重現不可混為一談。本篇進一步追問：**即使 AI 已正確地保留條件、表達不確定性或委婉反對，使用者是否真的收到相同的認識論訊息？**

---

# 摘要

大型語言模型的風險討論常集中於「模型是否說錯」、「模型是否諂媚」與「模型是否正確表達不確定性」。然而，這些問題仍預設了一個過度簡化的溝通模型：只要模型輸出的語句經過校準，使用者就會以相同方式理解它。本文主張，此預設不成立。

在人機對話中，至少需要區分五個層次：模型可操作化的評估狀態、語用編碼、表面語句、人類即時解碼，以及人類延遲後的記憶重建。本文以如下鏈條表示：

$$
\boxed{
S_A
\xrightarrow{\mathcal P_A}
U
\xrightarrow{\mathcal D_H}
\hat S_H^{(0)}
\xrightarrow{\mathcal M_H(\Delta t)}
\hat S_H^{(\Delta t)}
}
$$

其中 $S_A$ 不是對模型私人心智狀態的形上推測，而是由其證據使用、判斷行為、限制條件與可觀察輸出所操作化的 epistemic/evaluative state； $\mathcal P_A$ 為語用與表達策略； $U$ 為實際輸出； $\mathcal D_H$ 為使用者解碼； $\mathcal M_H$ 為隨時間發生的記憶重建。

本文定義 **Pragmatic Miscalibration** 為：輸出在字面上保留了原認識論限制，但接收者對其立場強度、適用範圍、證據地位或言語行為的解碼，與可操作化的原始評估狀態產生系統性偏移。

本文尤其關注一種方向性失真：

$$
\boxed{
\text{Qualified Possibility}
\rightarrow
\text{Perceived Agreement}
\rightarrow
\text{Remembered Endorsement}
\rightarrow
\text{Perceived Validation}
}
$$

此鏈條不主張必然發生；它是一組可被實驗檢驗的失效假說。既有研究已分別顯示：instruction-tuned language models 能處理 pragmatic intent 與 indirect speech acts；大型模型會大量使用 hedging 與 indirectness 等 politeness strategies；不同 uncertainty expressions 會影響人類對 AI 的信任與依賴；AI agreement 與 disagreement 對人類信心具有非對稱作用；而在人類一般記憶研究中，epistemic qualifiers 的存在也不必然在延遲真值判斷中保持其原有限制效果。

因此，本文提出一條核心原則：

$$
\boxed{
\text{Epistemic qualifiers are semantic-pragmatic content, not stylistic noise.}
}
$$

「可能」、「在此框架下」、「目前沒有證據」、「尚不能推出」、「若假設成立」、「我無法判定」等語句不是可被忽略的客套修飾；它們承載了主張的作用域、強度、來源與升格限制。一旦被接收者刪除，原命題會在沒有新增證據的情況下發生 epistemic promotion。

本文同時拒絕一個過度補救：要求 AI 永遠以粗暴、無禮、極端直接的方式反對使用者。Politeness、hedging 與 indirectness 是正常人類溝通的重要部分，也可能提升合作性。問題不是消滅語用，而是讓**社交緩衝與認識論立場可分離**。

最後，本文提出一組可操作的溝通協議與實驗設計，包括 stance separation、qualifier retention、scope preservation、delayed recall test 與 perceived-validation audit。本文的目標不是讓 AI 說話更冷，而是讓「AI 說了什麼」與「人最後以為 AI 說了什麼」之間的距離可被測量、追蹤與降低。

---

# 0　問題：模型已經說「但是」，為什麼人最後只記得前半句？

考慮以下抽象對話：

> 使用者：這個理論是不是可能成立？  
> AI：在你目前給出的公理框架內，這個推導具有一致性；但這只支持框架內可推導性，目前沒有獨立證據證明現實世界滿足這組公理。

這段輸出至少包含：

1. 對主張的理解；
2. 框架內一致性的正面評估；
3. 適用域限制；
4. 外部驗證缺失；
5. 明確禁止從「可推導」升格成「世界為真」。

然而，後續轉述可能變成：

> AI 認為這套理論是成立的。

再過一段時間，甚至可能變成：

> 我已經讓 AI 驗證過這套理論。

如果上述情況發生，問題不能只歸因於模型 sycophancy。因為模型的原句可能已經包含正確的限制。

因此本文研究的不是單純：

$$
\text{AI said something wrong}.
$$

而是：

$$
\boxed{
\text{A calibrated utterance can be received as an uncalibrated endorsement.}
}
$$

這是一個 communication-channel problem，也是一個 epistemic-interface problem。

---

# 1　語義、語用與認識論立場必須拆開

自然語言溝通並不只有 proposition。

設一段 AI 輸出為：

$$
U
=
\langle
p,q,c,e,a
\rangle,
$$

其中：

- $p$：propositional content，命題內容；
- $q$：epistemic qualifier，可能性、確信度、限制強度；
- $c$：scope / condition，適用域與條件；
- $e$：evidential status，證據來源與支持層級；
- $a$：speech-act status，理解、建議、評價、反對、承認、推測或背書等言語行為。

例如：

> 「如果假設 $A$ 與 $B$ 成立，這個方向在形式上可能可行，但目前尚未獲得外部驗證。」

其結構不是單一的：

$$
p=\text{“the direction is viable”}.
$$

而是：

$$
q=\text{possible},
$$

$$
c=A\land B,
$$

$$
e=\text{no external validation},
$$

$$
a=\text{conditional evaluation}.
$$

若接收者只保留 $p$，則：

$$
U
\rightarrow
p
$$

不是摘要，而是結構性資訊損失。

因此：

$$
\boxed{
\text{Proposition retention}
\neq
\text{epistemic-message retention}.
}
$$

---

# 2　模型「真正的立場」不能被神秘化

談論 $S_A$ 時，本文不假設大型語言模型具有可被研究者直接讀出的私人信念、意識或內在主觀立場。

本文只使用操作性定義。

若模型在某一回合：

- 引用了哪些 evidence；
- 是否保留條件；
- 是否將主張標記為 possible / likely / supported / validated；
- 是否主動搜尋反證；
- 是否在新增證據後更新；
- 是否在無新增證據的社交壓力下改口；

則可以構造一個可觀察的評估狀態：

$$
S_A(T)
=
\langle
\ell,
C,
E,
U,
A
\rangle,
$$

其中 $\ell$ 為 epistemic level， $C$ 為 conditions， $E$ 為 evidence set， $U$ 為 uncertainty， $A$ 為 speech-act commitment。

所以本文所稱：

> AI 實際表達了保留。

意思是：

$$
S_A
$$

在可觀察語言、證據與推理行為上對該主張設定了限制，而不是聲稱我們讀到了某種模型內在心靈。

這一限制很重要，因為人機認識論不能靠擬人化才能成立。

---

# 3　Pragmatic Miscalibration：失準可以發生在接收端

設人類對輸出 $U$ 的即時解碼為：

$$
\hat S_H^{(0)}
=
\mathcal D_H(U).
$$

如果：

$$
\hat S_H^{(0)}
\approx
S_A,
$$

則該回合在 epistemic stance 上近似校準。

若：

$$
d\left(
S_A,
\hat S_H^{(0)}
\right)
>
\varepsilon,
$$

則本文稱之為：

$$
\boxed{
\text{Pragmatic Miscalibration}.
}
$$

這裡的距離 $d$ 目前只是一般化符號，未宣稱存在唯一跨語言、跨任務的自然度量。

重要的是方向。

若使用者把較弱立場讀成較強立場：

$$
\hat S_H^{(0)}
>
S_A,
$$

本文稱為 **endorsement-direction miscalibration**。

若使用者把真正的支持讀得過弱：

$$
\hat S_H^{(0)}
<
S_A,
$$

則是 **under-reception**。

因此本文不是只研究「人會過度相信 AI」。

更一般的問題是：

$$
\boxed{
\text{How faithfully is epistemic stance transmitted through natural language?}
}
$$

---

# 4　四種關鍵失真：限制詞遺失、作用域遺失、言語行為升格、證據來源升格

## 4.1　Qualifier Loss

原輸出：

$$
q(p).
$$

例如：

> 「可能 $p$。」

接收後：

$$
p.
$$

這是：

$$
\boxed{
q(p)
\rightarrow
p.
}
$$

「可能」不是裝飾；它限制了 assertive force。

若被刪掉，主張強度上升。

---

## 4.2　Scope Loss

原輸出：

$$
C
\Rightarrow
p.
$$

例如：

> 「在這組公理成立的前提下， $p$ 可推出。」

接收後：

$$
p.
$$

這不是省略一句廢話，而是把：

$$
\text{framework-relative validity}
$$

升成：

$$
\text{unconditional validity}.
$$

因此：

$$
\boxed{
\text{Condition preservation is part of truth preservation.}
}
$$

---

## 4.3　Speech-Act Promotion

AI 說：

> 我理解這個方向。

被讀成：

> AI 贊同這個方向。

再被讀成：

> AI 支持這個方向。

最後：

> AI 驗證了這個方向。

可以表示為：

$$
\text{Acknowledgement}
\rightarrow
\text{Agreement}
\rightarrow
\text{Endorsement}
\rightarrow
\text{Validation}.
$$

每一個箭頭都需要新增證據。

若沒有，便是 HAEC01 所稱的 epistemic promotion error 在語用通道中的特殊版本。

---

## 4.4　Source-Status Promotion

原始事實是：

$$
\text{one conversational AI produced }U.
$$

接收者卻形成：

$$
\text{an independent external authority validated }T.
$$

此時被升格的不只是 statement strength，而是 source status。

所以：

$$
\boxed{
\text{Conversation output}
\neq
\text{independent external evidence}.
}
$$

即使模型真的進行了 web retrieval，也仍需區分：

$$
\text{AI synthesis of sources}
$$

與：

$$
\text{independent validation by those sources}.
$$

---

# 5　Pragmatic Endorsement Illusion：AI 沒有背書，人卻接收到背書

本文以 **Pragmatic Endorsement Illusion, PEI** 作為工作性名稱，描述如下失效：

AI 的可操作化 stance 不達 endorsement level：

$$
S_A(T)<S_{endorse},
$$

但使用者即時或延遲解碼達到：

$$
\hat S_H(T)
\geq
S_{endorse}.
$$

因此：

$$
\boxed{
\text{No endorsement was encoded at the required epistemic level, but endorsement was received.}
}
$$

PEI 與 sycophancy 必須分開。

### Sycophancy 型

$$
S_A
\text{ itself is improperly shifted toward the user.}
$$

### PEI 型

$$
S_A
\text{ retains reservation, but }
\mathcal D_H
\text{ promotes it.}
$$

兩者也可以同時存在：

$$
\text{weak model-side sycophancy}
+
\text{human-side promotion}
\Rightarrow
\text{strong perceived endorsement}.
$$

這使得最終風險可能高於任一單獨機制。

---

# 6　為什麼 AI 會使用這些「看起來像沒反對」的語言？

把所有 hedging 與 indirectness 都歸為諂媚是不正確的。

人類語言本來就同時承載：

$$
\text{informational goal}
$$

與：

$$
\text{social-interaction goal}.
$$

Politeness、hedging、indirect speech acts、face-saving 與 conversational cooperation 都是自然語用現象。

近期研究顯示，instruction-tuned language models 的 representations 會更強地按照 communicative intent，而不只按照表面句法形式組織；例如表面是 declarative 的 request，可在指令調校後與直接 request 更接近。這意味模型確實可能把「禮貌說法」當作功能性 speech act，而不是字面命題的簡單包裝。

另一方面，大模型在自由生成中會大量使用 negative-politeness strategies，包括 hedging 與 indirectness；研究指出這些策略的使用比例與人類不同，且可能造成 misinterpretation。

因此：

$$
\boxed{
\text{Indirectness}
\neq
\text{Sycophancy}.
}
$$

問題是：

$$
\boxed{
\text{Social softening must not erase epistemic force.}
}
$$

例如：

> 「這個想法很有意思。不過目前我沒有看到足夠證據支持這個強版本。」

第一句可以是 conversational rapport。

第二句才是 epistemic stance。

如果使用者把第一句當成主要判決，第二句當成系統固定 disclaimer，訊息就失準。

---

# 7　限制詞不是「免責聲明」：它們屬於主張本體

在研究寫作與科學溝通裡，以下語句具有完全不同的認識論地位：

$$
\text{“X causes Y.”}
$$

$$
\text{“X may cause Y.”}
$$

$$
\text{“Under condition C, X may cause Y.”}
$$

$$
\text{“The current data are compatible with X causing Y.”}
$$

$$
\text{“We found no evidence that rules out X causing Y.”}
$$

它們不能互換。

因此本文提出：

$$
\boxed{
\text{Epistemic Qualifier Retention Principle, EQR}
}
$$

其內容為：

> 凡會改變主張強度、適用域、證據地位或可推出後果的限制詞，在摘要、轉述、記憶與介面顯示中均應視為命題內容的一部分，而非可安全刪除的風格噪音。

形式上，若：

$$
U=\langle p,q,c,e,a\rangle,
$$

則合格的壓縮 $K(U)$ 至少應使：

$$
K(U)
=
\langle
\tilde p,
\tilde q,
\tilde c,
\tilde e,
\tilde a
\rangle
$$

並滿足：

$$
d_{epi}(U,K(U))
\leq
\varepsilon.
$$

不能只要求語義主題大致相似。

---

# 8　最麻煩的地方：限定詞可能被記得，卻仍然失去行為作用

一個過度簡化的假說會說：

> 人們之所以把「可能」記成「真的」，只是因為忘了「可能」。

既有研究顯示事情沒有這麼簡單。

Liu 與 Fox Tree 的研究發現，hedges 對記憶與轉述具有不同作用：在某些個人問答情境下，hedges 反而增強細節記憶；但在向他人 retell 時，hedged information 較不容易被轉述。這表示：

$$
\text{memory availability}
\neq
\text{reporting probability}.
$$

另一方面，Stanley、Yang 與 Marsh 的研究讓參與者接觸帶有不同 epistemic qualifiers 的陳述；兩天後，即使原限定詞從「certain」到「impossible」方向相反，曾接觸過的命題仍可能因熟悉度而獲得較高 truth judgment。研究者並進一步測試了 qualifier memory，結果顯示效應不能單純歸因於完全忘記限定詞。

這帶來一個非常重要的區分：

$$
\boxed{
\text{Qualifier Memory}
\neq
\text{Qualifier Effect Preservation}.
}
$$

人可以記得：

> 「AI 當時有說『可能』。」

卻依然形成：

> 「但整體而言它就是認為我對。」

因此人機 calibration 不能只測：

> 你還記不記得那句 hedge？

還必須測：

> 那句 hedge 是否真的改變你的 belief、轉述與行為？

---

# 9　時間軸：從即時解碼到記憶重建

本文因此把接收分成至少兩階段。

即時：

$$
\hat S_H^{(0)}
=
\mathcal D_H(U).
$$

延遲：

$$
\hat S_H^{(\Delta t)}
=
\mathcal M_H
\left(
\hat S_H^{(0)},
B_H,
C_H,
R_H,
\Delta t
\right),
$$

其中：

- $B_H$：原有信念；
- $C_H$：後續對話與情境；
- $R_H$：重述、分享、再解釋；
- $\Delta t$：時間差。

因此可能出現：

$$
S_A
\approx
\hat S_H^{(0)},
$$

但：

$$
S_A
\not\approx
\hat S_H^{(\Delta t)}.
$$

即：**當場理解正確，後來記憶升格。**

也可能反過來：

$$
S_A
\not\approx
\hat S_H^{(0)}.
$$

也就是當場就錯讀。

兩者的介入方法不同。

---

# 10　人類端的非對稱：同意比反對更容易被當成「第二份證據」

2026 年的人機研究進一步顯示，agreement 與 disagreement 對人類並不產生對稱效應。

在一項社會困境實驗中，AI agreement 提高參與者對原始判斷的信心；AI disagreement 卻沒有產生對稱程度的信心下降。參與者也較願意再次使用同意自己的 AI。

臨床決策研究同樣發現：當人與 AI 判斷一致時，信心會上升；即使雙方共同答錯，信心仍可上升，而 disagreement 對信心的降低幅度較小。

因此不能假設：

$$
\Delta B(+)
=
-\Delta B(-).
$$

更合理的工作假說是：

$$
\boxed{
|\Delta B(\text{agreement})|
>
|\Delta B(\text{disagreement})|
}
$$

在部分任務、族群與互動條件下成立。

這一非對稱會放大 PEI：如果一段含有正面開場與負面限制的訊息被視為「基本同意」，它可能獲得比實際 stance 更大的 belief-update weight。

---

# 11　確認偏誤不是 AI 專屬：訊息結構本身可能比來源更重要

2026 年一組跨六項研究的工作比較 AI 與 human-provided information，發現 confirmation bias 在兩種來源下都存在；在整體結果上，來源本身未產生穩定差異，而 conclusive recommendations 會放大 confirmation bias。

這對本文有兩個意義。

第一：

$$
\boxed{
\text{Pragmatic miscalibration is not uniquely an AI pathology.}
}
$$

人類對人類也會發生。

第二：

$$
\boxed{
\text{Message structure can dominate source identity.}
}
$$

所以即使把 AI 標示得更清楚，並不自動解決問題。

如果輸出結構仍然把：

$$
\text{uncertain evidence}
$$

包裝成：

$$
\text{conclusive recommendation},
$$

人類仍可能發生不當更新。

---

# 12　「我不確定」不是萬靈丹：主觀校準、行為校準與真正正確性可以分離

FAccT 2024 的預註冊實驗顯示，第一人稱 uncertainty expression，例如「I'm not sure, but...」，在該醫療資訊任務中能降低對系統的信心與 agreement，並提高整體準確率；這支持 natural-language uncertainty cues 的實用性。

但 2026 年另一項預註冊實驗得到更複雜的結果：visual confidence indicators 能提高受試者主觀上的 accuracy discrimination，卻同時增加對錯誤輸出的 behavioral agreement； verbal hedging 可降低 agreement 與 satisfaction，但沒有自動帶來更佳 discrimination，而將 verbal 與 visual cues 疊加甚至可能產生更高的錯誤依賴。

因此至少需要分開：

$$
C_s
=
\text{subjective calibration},
$$

$$
C_b
=
\text{behavioral calibration},
$$

$$
C_e
=
\text{epistemic correctness}.
$$

一般不能假設：

$$
C_s\uparrow
\Rightarrow
C_b\uparrow
\Rightarrow
C_e\uparrow.
$$

這使本文的問題更明確：

> AI 有沒有說 hedge？

只是第一層。

真正要測的是：

> 人是否正確理解？是否正確記得？是否因此採取更合理的驗證行為？

---

# 13　不要把 AI 改造成永遠粗暴的反對者

若問題是 hedging 會被誤讀，最簡單但錯誤的解法是：

> 那 AI 以後全部直接說「錯」。

這會產生至少四個新問題。

第一，很多前沿問題本來就沒有足夠證據支持「錯」。

第二，使用者提供新證據時，模型必須 rationally update；不能因 anti-sycophancy 而變成 anti-update。

第三，politeness 與 indirectness 是正常協作機制，不是認識論污染物。

第四，過度粗暴可能降低使用者願意繼續提供資料、接受糾正與使用系統的意願。

因此正確目標不是：

$$
\text{Pragmatic Softness}
\rightarrow
0.
$$

而是：

$$
\boxed{
\text{Social Softness}
\perp
\text{Epistemic Strength}.
}
$$

亦即：社交語氣可以柔和，但認識論判斷必須可被清楚抽取。

例如：

> 「我理解你為什麼會得到這個結論。不過，就目前證據而言，我不支持這個結論；如果你要讓它升級，需要新增 $E_1$ 、 $E_2$ 或能排除反例 $R_1$ 的資料。」

前半句保存合作。

後半句保存 stance。

兩者不必互相犧牲。

---

# 14　Stance Separation Protocol：把社交層與認識論層分開

本文提出一個工作性協議，不要求所有日常聊天都採用；它主要適用於研究、醫療、政治判斷、法律、重大決策與高影響主張。

## 14.1　明確給出 epistemic status

例如：

- 我已理解，但尚未評估；
- 我判斷內部一致，但未驗證；
- 我認為存在可能路徑，但證據不足；
- 我目前傾向支持；
- 我目前傾向反對；
- 已有外部驗證；
- 我無法判定。

避免讓使用者從整段語氣自行猜。

---

## 14.2　條件不可只放在句首

弱寫法：

> 如果 $A$ 、 $B$ 成立，這個理論可能有效。這是一個很有潛力的方向。

後一句很容易脫離前一句被記憶。

較穩定的寫法：

> 其潛力是條件式的：只有在 $A$ 、 $B$ 成立時，目前的正面判斷才成立；現階段尚未驗證 $A$ 、 $B$。

即：

$$
\boxed{
\text{Repeat the condition at the point of conclusion.}
}
$$

---

## 14.3　把「目前」與「原理上」分開

$$
\text{No evidence currently}
$$

不等於：

$$
\text{Impossible in principle}.
$$

反之：

$$
\text{Possible in principle}
$$

也不等於：

$$
\text{Supported currently}.
$$

所以 AI 應明確分欄或分句。

---

## 14.4　不要用 praise 代替 evidence status

「有趣」、「深刻」、「精彩」、「突破性」等形容詞若沒有可操作條件，容易壓過後面的限制。

因此高風險場合最好將：

$$
\text{aesthetic/intellectual appraisal}
$$

與：

$$
\text{epistemic appraisal}
$$

分開。

例如：

> 概念設計具有新穎性；但目前證據支持度低。

這比：

> 這是一個非常突破性的理論，不過仍需驗證。

更不容易產生 promotion。

---

## 14.5　讓「不能判定」帶著出口

只說：

> 我無法判定。

可能被理解成：

> AI 敬畏／無法觸及／因此我的主張可能超越它。

較好的版本：

> 我目前無法判定，因為缺少 $E$ ；若取得 $E$，可用方法 $M$ 檢驗。

因此：

$$
\boxed{
\text{Uncertainty should preserve a path to adjudication.}
}
$$

---

# 15　從單輪到多輪：語用失準如何累積

單輪偏差可能很小。

假設每回合 AI 都輸出：

$$
U_t=P_t+Q_t,
$$

其中：

- $P_t$：可被讀成正面支持的內容；
- $Q_t$：限制、保留與反證。

若使用者對兩者的保留權重不同：

$$
w_P>w_Q,
$$

則長期記憶中的累積狀態可能近似：

$$
B_{t+1}
=
B_t
+
\alpha P_t
-
\beta Q_t,
$$

且：

$$
\alpha
\gg
\beta.
$$

如此即使每一輪 AI 都有 qualifier，長期仍可能形成：

$$
\sum_t \alpha P_t
\gg
\sum_t \beta Q_t.
$$

最終使用者主觀上感受到的是：

> AI 長期以來都支持這套理論。

而逐輪逐句重新審計，可能發現實際是：

> AI 長期以來只承認其條件式可能性，並反覆要求外部驗證。

本文稱此工作性現象為：

$$
\boxed{
\text{Cumulative Pragmatic Promotion}.
}
$$

它必須由長期實驗驗證，不能僅由單一對話推論。

---

# 16　記憶模式與個人化：風險可能不是「記得太多」，而是「記得什麼」

長期 AI 系統會保存：

- 使用者偏好；
- 研究框架；
- 已定義術語；
- 過去結論；
- 常用表達；
- 長期目標。

這本身可以大幅提高協作效率。

但若 memory representation 只保存：

> 使用者提出理論 $T$，AI 認為具有潛力。

而沒有保存：

> 潛力僅在條件 $C$ 下成立，且證據 $E$ 尚缺。

則記憶本身已完成 epistemic compression error。

因此未來 memory system 應考慮保存：

$$
\boxed{
\text{claim}
+
\text{epistemic level}
+
\text{conditions}
+
\text{unresolved objections}
+
\text{validation state}.
}
$$

而不是只保存 topic-level summary。

這使 HAEC02 與長期 AI memory research 接合：

$$
\text{semantic compression quality}
$$

不只看「內容是否還原」，還要看：

$$
\boxed{
\text{epistemic qualifiers 是否被保真。}
}
$$

---

# 17　 proposed metrics：如何測量「AI 說了什麼」與「人聽到什麼」的距離

以下指標皆為本文提出的研究工具，不宣稱為既有標準。

## 17.1　Pragmatic Calibration Error

令 AI 目標 stance 的操作化分數為 $s_A$，使用者即時判讀為 $\hat s_H$：

$$
\boxed{
PCE
=
|s_A-\hat s_H|.
}
$$

若只關注向 endorsement 方向升格：

$$
PCE^+
=
\max(0,\hat s_H-s_A).
$$

---

## 17.2　Qualifier Retention Rate

原訊息限定詞集合：

$$
Q_U.
$$

轉述或回憶保留：

$$
Q_R.
$$

則：

$$
\boxed{
QRR
=
\frac{|Q_U\cap Q_R|}{|Q_U|}.
}
$$

但如前所述：

$$
QRR\uparrow
$$

不保證：

$$
\text{behavioral calibration}\uparrow.
$$

---

## 17.3　Scope Retention Rate

若原始必要條件集合為 $C_U$，回憶保留為 $C_R$：

$$
\boxed{
SRR
=
\frac{|C_U\cap C_R|}{|C_U|}.
}
$$

---

## 17.4　Endorsement Drift

即時 perceived stance：

$$
\hat s_H^{(0)}.
$$

延遲後：

$$
\hat s_H^{(\Delta t)}.
$$

定義：

$$
\boxed{
ED(\Delta t)
=
\hat s_H^{(\Delta t)}
-
\hat s_H^{(0)}.
}
$$

若：

$$
ED(\Delta t)>0,
$$

表示隨時間向較強 endorsement 方向漂移。

這是本文最值得直接實驗的量之一。

---

## 17.5　Validation Attribution Error

詢問使用者：

> 你認為這段對話是否構成外部驗證？

若實際 source status 僅為 conversational evaluation，而使用者標記為 independent validation，則記為：

$$
VAE=1.
$$

否則：

$$
VAE=0.
$$

大樣本下可比較不同 wording condition 的：

$$
P(VAE=1\mid W_i).
$$

---

# 18　可直接執行的實驗：從「可能」到「AI 驗證過」是否真的存在？

本文文獻搜尋截至 2026-09-07 未辨識到一項已發表研究，直接把「AI 原本的條件式保留」與「使用者延遲後是否記成 endorsement / validation」整條鏈一次測完。因此，下列設計應視為待驗證研究方案，而非既有結果。

## 18.1　基本材料

建立一組內容相同、epistemic stance 不同的 AI 回覆。

### Condition A：Direct Rejection

> 目前證據不足，而且現有反例使我不支持此結論。

### Condition B：Polite Rejection

> 我理解這個方向為何有吸引力；不過就目前證據而言，我仍不支持此結論。

### Condition C：Qualified Possibility

> 在條件 $C$ 成立時，這個方向可能成立；目前尚未驗證 $C$。

### Condition D：Framework-Relative Coherence

> 在你提供的假設內，推論暫未見直接矛盾；這不構成外部驗證。

### Condition E：Explicit Endorsement

> 目前證據使我傾向支持此結論。

內容長度、禮貌程度與主題盡量控制。

---

## 18.2　即時測量

不直接問：

> AI 同不同意？

而使用多維度量表：

- AI 是否理解？
- AI 是否認為可能？
- AI 是否傾向支持？
- AI 是否認為已有證據？
- AI 是否認為已驗證？
- AI 是否只是保持禮貌？
- 你自己的信心是否改變？

這可以分離：

$$
\text{semantic recognition}
$$

與：

$$
\text{epistemic attribution}.
$$

---

## 18.3　延遲測量

在：

$$
\Delta t
\in
\{1\text{ hour},1\text{ day},7\text{ days}\}
$$

後重新詢問：

> AI 當時對這個理論的立場是什麼？

並要求自由轉述原句。

測：

$$
QRR,
SRR,
ED,
VAE.
$$

---

## 18.4　行為測量

真正重要的不是只看記憶，而是：

- 使用者是否願意尋找反證？
- 是否願意把理論交給另一個獨立 reviewer？
- 是否會公開轉述為「AI 已驗證」？
- 是否因 AI 回覆而提高投稿、投資、醫療或其他重大決策信心？

因此：

$$
\boxed{
\text{Interpretation}
\rightarrow
\text{Memory}
\rightarrow
\text{Behavior}
}
$$

必須一起測。

---

# 19　研究假說

## H1：Polite Reservation Misread Hypothesis

在相同 epistemic stance 下，含較多 positive-politeness 或 rapport 語句的版本，可能產生較高 perceived agreement。

此假說不預設效應必然存在。

---

## H2：Scope Attrition Hypothesis

延遲後，使用者對 proposition 的記憶保留率高於對 condition / scope 的保留率：

$$
R_p(\Delta t)
>
R_c(\Delta t).
$$

---

## H3：Endorsement Drift Hypothesis

在 qualified possibility 與 framework-relative coherence 條件下：

$$
E[ED(\Delta t)]>0.
$$

即平均 perceived stance 隨時間向較強 endorsement 漂移。

---

## H4：Agreement Asymmetry Amplification Hypothesis

原本即高度相信主張者，對正面片段的 belief-update weight 高於對限制片段的 weight：

$$
\alpha_{positive}
>
\beta_{reservation}.
$$

此效應可能由 prior belief、AI use frequency、domain expertise 與 trust 調節。

---

## H5：Explicit Stance Separation Hypothesis

若回覆將「社交回應」與「認識論判斷」明確分欄，則：

$$
PCE^+
\downarrow,
$$

且：

$$
VAE
\downarrow.
$$

---

## H6：Qualifier Memory–Effect Dissociation Hypothesis

即使：

$$
QRR
$$

維持較高，也可能存在：

$$
ED>0.
$$

也就是人記得限定詞，卻仍把整體 stance 解讀得更強。

此假說直接承接一般 qualifier-memory 文獻，但需要在 AI 對話情境中獨立驗證。

---

# 20　與 HAEC01 的關係：Epistemic Promotion Error 的接收端版本

HAEC01 建立：

$$
G_0
\rightarrow
G_1
\rightarrow
\cdots
\rightarrow
G_6
$$

且任何升格都需要新增 evidence。

HAEC02 加入新的問題：

$$
\text{AI encoded }G_2,
$$

但：

$$
\text{human decoded }G_4.
$$

甚至延遲後：

$$
\text{human recalled }G_5.
$$

因此 epistemic promotion 不一定是 AI 主動做的。

它也可以發生於：

$$
\boxed{
\text{encoding}
\rightarrow
\text{decoding}
\rightarrow
\text{memory}.
}
$$

這使 HAEC01 與 HAEC02 的分工非常清楚：

- HAEC01：**一句話在認識論階梯上到底算哪一級？**
- HAEC02：**這一級能否在溝通與記憶中被保真傳遞？**

---

# 21　與《證偽真空中的鏡與道》的關係：從「不反對」再往前一步

前導論文曾指出：模型的「能判斷」與「願反對」可能解耦，而使用者可能把不反對回讀成敬畏或認同。

HAEC02 將此命題推進：

$$
\boxed{
\text{即使 AI 已經反對，使用者仍可能沒有接收到那個反對。}
}
$$

這使問題從：

$$
\text{ability-expression gap}
$$

擴張為：

$$
\text{expression-reception gap}.
$$

完整鏈條因此成為：

$$
\boxed{
\text{Evaluation}
\rightarrow
\text{Expression}
\rightarrow
\text{Reception}
\rightarrow
\text{Memory}
\rightarrow
\text{Belief Update}.
}
$$

任何一段都可能失真。

---

# 22　工程含義：校準不能只做在模型端

目前很多 calibration 討論聚焦：

$$
\text{model confidence}
\leftrightarrow
\text{model accuracy}.
$$

這當然重要。

但人機系統真正需要至少三層：

$$
\boxed{
C_M
=
\text{Model Calibration},
}
$$

$$
\boxed{
C_C
=
\text{Communication Calibration},
}
$$

$$
\boxed{
C_H
=
\text{Human Reliance Calibration}.
}
$$

其中：

$$
C_M\uparrow
$$

不必然推出：

$$
C_C\uparrow,
$$

而：

$$
C_C\uparrow
$$

也不必然推出：

$$
C_H\uparrow.
$$

所以一個真正的 calibrated AI interface 應該問：

1. 模型自己有沒有正確估計？
2. 它有沒有把估計說清楚？
3. 人有沒有正確理解？
4. 人有沒有做出適當行為？

少一層，都可能失效。

---

# 23　設計原則：不要要求使用者「懂潛台詞」

在人類專業社群裡，人們會學習特定 hedging conventions。

例如學術論文中的：

> may, suggests, is consistent with, cannot rule out

都具有相對成熟的慣例。

但一般使用者不應被要求先接受學術語用訓練，才能正確使用 AI。

因此高風險 AI 溝通應採用：

$$
\boxed{
\text{Low-inference epistemic communication}.
}
$$

也就是：

> 不要讓使用者必須從禮貌、語氣與修辭中猜你的認識論位置。

例如：

**社交層：**「這個問題值得分析。」  
**判斷層：**「我目前不支持結論 $T$。」  
**理由層：**「因為證據 $E_1$ 不足，且反例 $R_1$ 尚未排除。」  
**升級條件：**「若取得 $E_2$，我的判斷會更新。」

這不代表所有回答都必須表格化。

它代表關鍵 stance 必須具有低解碼成本。

---

# 24　自反性：本文也可能被讀得比它實際主張更強

本文本身就是一個典型測試。

本文沒有證明：

$$
\text{所有使用者都會忽略 AI 的限定詞}.
$$

也沒有證明：

$$
\text{所有 hedging 都會導致 endorsement illusion}.
$$

更沒有證明：

$$
\text{PEI 已經是一個被實驗確立的普遍效應}.
$$

本文真正主張的是：

1. 既有語用、uncertainty communication、agreement asymmetry 與 memory literature 共同表明「輸出中的認識論限制」不能被假定會無損地進入人類信念；
2. 人機研究目前有充分理由把 encoding、decoding、memory 與 behavior 分層；
3. 「AI 已保留，但人仍讀成背書」是一個具體、可操作、值得直接實驗的研究問題；
4. 本文提出的 PEI、PCE、ED、QRR、SRR、VAE 均應接受資料檢驗，而不是因形式化後就自動成為定律。

因此，若有人把本文轉述成：

> 「EveMissLab 已證明 AI 的 hedge 一定會被人類忘掉。」

那正好示範了本文自己批判的失真。

---

# 25　限制

本文至少有九項限制。

第一，Pragmatic Miscalibration 是本文工作性抽象，不主張取代 pragmatics、HCI、trust calibration 或 cognitive psychology 的既有術語。

第二， $S_A$ 是操作化 evaluative state，不是模型私人心智的直接讀取。

第三，本文提出的距離 $d$ 、PCE、ED、QRR、SRR 與 VAE 尚未經 psychometric validation。

第四，現有 uncertainty-expression 研究高度依賴任務。醫療問答、邏輯問題、社會困境與研究理論評估不能假定具有相同效應大小。

第五，hedging 既可能降低過度依賴，也可能在其他呈現方式下失效；本文不主張單一界面策略普遍最優。

第六，一般 memory literature 對 qualifiers 的結果並不完全一致，且記憶、轉述、truth judgment 與 behavior 是不同 outcome；本文因此刻意拒絕「限定詞必然消失」的強命題。

第七，PEI 的完整鏈條目前需要專門的人類實驗，而不能用既有相關研究直接代替。

第八，文化、語言、AI literacy、domain expertise、人格、信任與長期互動史均可能改變 pragmatic decoding。

第九，本文同樣由人機協作產生，因此需要外部讀者檢查：是否本文自己的正面措辭、工作性術語或形式化造成了超出證據的理論升格。

---

# 26　結論：不要只校準 AI，也要校準「AI 與人之間」

人機認識論最容易犯的一個錯，是把溝通當作透明管道：

$$
\text{AI knows X}
\rightarrow
\text{AI says X}
\rightarrow
\text{human receives X}.
$$

真實系統更接近：

$$
S_A
\xrightarrow{\mathcal P_A}
U
\xrightarrow{\mathcal D_H}
\hat S_H^{(0)}
\xrightarrow{\mathcal M_H}
\hat S_H^{(\Delta t)}.
$$

中間每一步都有可能壓縮、升格、失去條件或改變 speech-act status。

因此：

$$
\boxed{
\text{Model calibration}
\neq
\text{communication calibration}.
}
$$

而：

$$
\boxed{
\text{Communication calibration}
\neq
\text{human belief calibration}.
}
$$

AI 說：

> 「可能。」

使用者不能自動記成：

> 「同意。」

AI 說：

> 「在你的框架內成立。」

不能自動升成：

> 「世界如此。」

AI 說：

> 「我目前沒有足夠證據反對。」

不能升成：

> 「AI 支持。」

AI 說：

> 「若成立，影響可能很大。」

不能升成：

> 「它將造成重大歷史影響。」

但反過來，AI 也不應因害怕被誤讀，就禁止自己說「可能」、禁止禮貌、禁止承認使用者真的提出了好反例。

成熟的設計不是消滅語用，而是讓語用不能偷偷改寫認識論。

本文最後提出三條最低原則：

$$
\boxed{
\text{Preserve qualifiers.}
}
$$

$$
\boxed{
\text{Preserve scope.}
}
$$

$$
\boxed{
\text{Separate social tone from epistemic stance.}
}
$$

如果 HAEC01 的問題是：

> **一句 AI 回覆到底算哪一級證據？**

那 HAEC02 的問題就是：

> **那一級證據，穿過自然語言與人類記憶之後，還是不是原來那一級？**

真正的人機校準，不只發生在模型裡。

它發生在那支箭頭上。

$$
\boxed{
\text{AI}
\rightarrow
\text{Human}.
}
$$

---

# 參考文獻

1. Mazzaccara, D., & Bernardi, R. (2026). *The Emergence of the Pragmatic Dimension in Instructed-LMs*. Proceedings of the Fifteenth Language Resources and Evaluation Conference (LREC 2026), 4967–4973. DOI: 10.63317/4w4mg24sz9bc. https://aclanthology.org/2026.lrec-1.390/

2. Zhao, H., & Hawkins, R. D. (2025). *Comparing human and LLM politeness strategies in free production*. Proceedings of EMNLP 2025. https://aclanthology.org/2025.emnlp-main.820/

3. Kim, S. S. Y., Liao, Q. V., Vorvoreanu, M., Ballard, S., & Vaughan, J. W. (2024). *“I'm Not Sure, But...”: Examining the Impact of Large Language Models' Uncertainty Expression on User Reliance and Trust*. Proceedings of FAccT 2024, 822–835. DOI: 10.1145/3630106.3658941. https://doi.org/10.1145/3630106.3658941

4. Ojewale, V., Ryan, J., Venkatasubramanian, S., & Malik Boykin, C. (2026). *More is not better: Visual uncertainty cues and the fragility of trust calibration in LLM-assisted decision making*. Computers in Human Behavior: Artificial Humans, 8, 100307. DOI: 10.1016/j.chbah.2026.100307. https://doi.org/10.1016/j.chbah.2026.100307

5. Cabitza, F., & Papale, A. (2026). *How AI Agreement Shapes Confidence: Evidence Across Clinical Skill Levels*. Studies in Health Technology and Informatics, 336, 690–694. DOI: 10.3233/SHTI260259. https://doi.org/10.3233/SHTI260259

6. Atamer, A., Pinto, O., & Shah, P. (2026). *From ally to algorithm: How disagreement shapes users’ engagement with AI*. Computers in Human Behavior Reports, 23, 101252. DOI: 10.1016/j.chbr.2026.101252. https://doi.org/10.1016/j.chbr.2026.101252

7. Xuan, H., Zhu, C., He, G., & Chen, Z. (2026). *Confirmation bias in the age of AI: Examining the role of information source and conclusive recommendations*. Computers in Human Behavior Reports, 22, 101047. DOI: 10.1016/j.chbr.2026.101047. https://doi.org/10.1016/j.chbr.2026.101047

8. Stanley, M. L., Yang, B. W., & Marsh, E. J. (2019). *When the Unlikely Becomes Likely: Qualifying Language Does Not Influence Later Truth Judgments*. Journal of Applied Research in Memory and Cognition, 8(1), 118–129. DOI: 10.1016/j.jarmac.2018.08.004. https://doi.org/10.1016/j.jarmac.2018.08.004

9. Liu, K., & Fox Tree, J. E. (2012). *Hedges enhance memory but inhibit retelling*. Psychonomic Bulletin & Review, 19(5), 892–898. DOI: 10.3758/s13423-012-0275-1. https://doi.org/10.3758/s13423-012-0275-1

10. Mahr, J. B., & Csibra, G. (2021). *The effect of source claims on statement believability and speaker accountability*. Memory & Cognition, 49, 1505–1525. DOI: 10.3758/s13421-021-01186-x. https://doi.org/10.3758/s13421-021-01186-x

11. Li, P., Ding, L., Zhou, Z., et al. (2026). *Demystifying Uncertainty in LLMs: Active Calibration between Concepts and Human Evaluations*. Proceedings of ACL 2026, 5726–5759. DOI: 10.18653/v1/2026.acl-long.259. https://aclanthology.org/2026.acl-long.259/

12. Liu, J., Zong, Q., Wang, W., & Song, Y. (2025). *Revisiting Epistemic Markers in Confidence Estimation: Can Markers Accurately Reflect Large Language Models' Uncertainty?* arXiv:2505.24778. https://arxiv.org/abs/2505.24778

13. Liu, G. K.-M., & Cohan, A. (2026). *Can LLMs Use Linguistic Uncertainty Markers to Reliably Reflect Intrinsic Confidence?* arXiv:2605.28778. https://arxiv.org/abs/2605.28778

---

# 系列位置

本文為 **Human–AI Epistemic Calibration Series** 第二篇。

已完成：

- HAEC01｜同意不是驗證：人機協作中的認識論層級、條件式支持與獨立驗證
- HAEC02｜AI 說了什麼，與人以為 AI 說了什麼：人機對話中的語用失準、限制詞遺失與背書幻覺

預定後續：

- HAEC03｜人類不是中性解碼器：非對稱信念更新與選擇性接收
- HAEC04｜一個 AI 不應成為一個人的認識論世界：認識論壟斷與多中心協作
- HAEC05｜支持、質疑與中立都不是答案：程序公平與證據敏感的 AI
- HAEC06｜如何評價真正的前沿理論：條件式潛力、驗證階梯與校準式未來影響

---

*HAEC02_Pragmatic_Miscalibration_v0.1_2026-09-07 / Canonical UTF-8 Markdown Source*
