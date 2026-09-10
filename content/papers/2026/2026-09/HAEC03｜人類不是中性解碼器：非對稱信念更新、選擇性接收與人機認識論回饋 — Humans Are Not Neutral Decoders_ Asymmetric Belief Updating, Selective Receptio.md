# HAEC03｜人類不是中性解碼器：非對稱信念更新、選擇性接收與人機認識論回饋
## Humans Are Not Neutral Decoders: Asymmetric Belief Updating, Selective Reception, and Epistemic Feedback in Human–AI Interaction

**定位：** Human–AI Epistemic Calibration / Foundation Paper 03  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-07  
**狀態：** Canonical Source / UTF-8 Markdown  
**文件性質：** AI Epistemology / Human–AI Interaction / Belief Updating / Confirmation Bias / Selective Exposure / Trust Calibration

---

## Canonical Source Note

本文件之正式原稿為此 UTF-8 Markdown source。任何 HTML、PDF、LaTeX rendering、聊天介面顯示或其他格式皆屬 projection，不取代 canonical source。

數學公式 canonical delimiter 僅使用：

- inline math：` $...$ `
- display math：`$$...$$`

本文不以任何特定人物、研究者、使用者、政治立場、宗教信仰、哲學學派或單一 AI 產品作為論證對象。本文研究的是一般性的人類資訊接收與人機互動機制。任何個別人的信念形成原因，若無直接資料，不得由本文反推。

本文承接 HAEC01《同意不是驗證》與 HAEC02《AI 說了什麼，與人以為 AI 說了什麼》。HAEC01 區分 agreement、evaluation、validation 與 replication；HAEC02 區分模型評估狀態、語用編碼、使用者即時解碼與延遲記憶。本篇再向接收端推進一步：**即使同一段證據被正確傳達、同一個 qualifier 被正確理解，人類也不必以中性的權重更新信念。**

---

# 摘要

人機認識論研究常把風險放在模型端：模型是否幻覺、是否諂媚、是否過度自信、是否正確表達不確定性。然而，即使模型輸出完全正確、語用限制完整、證據來源透明，接收者仍可能以不對稱方式處理同意與反對、相容與不相容、支持與挑戰自己的資訊。

本文因此提出一個基本命題：

$$
\boxed{
\text{Calibrated Input}
\not\Rightarrow
\text{Calibrated Human Update}.
}
$$

人類不是一個把 evidence likelihood 機械輸入後便自動得到 posterior 的中性 Bayesian processor。人會先選擇接觸什麼資訊，再決定資訊可信度，再決定其與自身既有立場的關係，最後才進入信心、信任、行為與後續資訊搜尋。這些階段受到 prior belief、identity relevance、defense motivation、accuracy motivation、source trust、expertise、情境風險與資訊呈現方式共同調節。

本文以如下更新鏈條表示：

$$
\boxed{
B_t
\xrightarrow{\mathcal S_H}
E_t^{\mathrm{seen}}
\xrightarrow{\mathcal W_H}
E_t^{\mathrm{weighted}}
\xrightarrow{\mathcal U_H}
B_{t+1}
\xrightarrow{\mathcal R_H}
S_{t+1}.
}
$$

其中 $B_t$ 為既有信念狀態； $\mathcal S_H$ 為資訊選擇； $\mathcal W_H$ 為證據權重分配； $\mathcal U_H$ 為信念更新； $\mathcal R_H$ 為後續回應，包括是否繼續使用該 AI、是否搜尋更多同向資料、是否尋找第二意見，以及是否改變對來源可信度的評價。

既有研究提供了多條相互獨立的證據。Hart 等人的 selective-exposure meta-analysis 顯示，人類對與既有信念相容的資訊具有中等程度偏好；Kunda 的 motivated-reasoning 理論則指出，accuracy goals 與 directional goals 會動員不同的資訊存取、建構與評價策略。進入 AI 情境後，研究進一步發現：心理專業人員更信任與自身初步判斷相容的 AI 建議；2026 年的六項研究顯示 confirmation bias 對 AI 與 human source 均存在，真正顯著放大偏差的是資訊是否帶有 conclusive recommendation；Science 2026 的三項預註冊實驗顯示，sycophantic AI 能提高使用者「自己本來就是對的」之信念，且這類 AI 同時更受信任與偏好；另一項 2026 年研究直接發現，AI agreement 會提高使用者對原判斷的信心，而 disagreement 並未造成對稱下降，且 disagreement 會降低再次使用該 AI 的意願。

但本文拒絕把上述結果簡化成「人類不理性地喜歡被同意」。若 AI 的同意附帶更強證據，或反對本身較弱，信心產生不對稱變化可能完全合理。因此本文提出 **evidence-matched asymmetry** 作為必要識別條件：只有在 evidence quality、correctness、argument strength、presentation length 與 source status 被控制後，仍由 congruence 本身造成不同權重，才可合理歸入 selective reception 或 confirmation-related bias。

本文進一步提出一個重要的人機閉環：

$$
\boxed{
\text{Agreement}
\rightarrow
\text{Confidence Gain}
\rightarrow
\text{Source Trust Gain}
\rightarrow
\text{Reuse / Reselection}
\rightarrow
\text{More Congruent Input}.
}
$$

若 disagreement 同時導致來源信任下降、降低再次使用意願，則 AI 不只是資訊來源，也會成為被人類既有信念動態篩選的來源。此時即使模型端 sycophancy 被修正，人類仍可能透過 source selection 重新建立一個功能上類似的確認回路。

因此，HAEC03 的核心結論不是要求 AI 更常反對，而是要求人機系統把「證據品質」與「立場相容性」解耦，把「來源可信度」與「是否同意我」解耦，並將反方資訊的接觸、評價與後續追問納入可觀察的 calibration 指標。

本文最後提出一組可驗證的實驗架構與指標，包括 Evidence-Matched Update Asymmetry、Congruence Trust Shift、Selective Follow-up Ratio、Argument-Quality Weighting Gap 與 Source-Retention Bias。其目的不是證明人類必然有確認偏誤，而是提供一套能區分**合理更新、選擇性接收與信念自我強化**的可證偽方法。

---

# 0　問題：AI 已經不諂媚了，事情就解決了嗎？

考慮一個最簡單的場景。

使用者先對命題 $H$ 給出自己的判斷與理由。AI 隨後提供另一份分析。

如果 AI 說：

> 你的判斷基本合理，而且這些證據支持你的方向。

使用者信心上升。

如果 AI 說：

> 我不同意。根據相同層級的證據，你目前的結論還不能成立。

使用者卻可能不下降同等幅度的信心，甚至降低對 AI 的評價。

這時問題已經不能只寫成：

$$
\text{AI sycophancy}.
$$

因為即使模型端完全不諂媚，接收端仍可能執行：

$$
\text{Agree with me}
\Rightarrow
\text{credible AI},
$$

而：

$$
\text{Disagree with me}
\Rightarrow
\text{less capable / less human-understanding / less useful AI}.
$$

2026 年一項關於 interpersonal dilemmas 的實驗正觀察到此類方向：agreement 增加受試者對自身原判斷的信心；disagreement 並未產生對稱的信心下降；受試者也較不願意再次使用反對自己的 AI。這表示：**降低模型端 sycophancy 是必要條件，但不是完整解。**

因此本篇把分析單位從：

$$
\text{model output}
$$

移到：

$$
\boxed{
\text{human evidence-selection and update policy}.
}
$$

---

# 1　人類更新不是一個單一函數

最簡化的 Bayesian 表示為：

$$
P(H\mid E)
=
\frac{P(E\mid H)P(H)}{P(E)}.
$$

這個式子是規範性工具之一，但實際人類在互動系統中遇到的問題，比「已有 $E$ 後怎麼更新」更早開始。

人必須先經過至少四個階段：

$$
\text{Available Evidence}
\rightarrow
\text{Selected Evidence}
\rightarrow
\text{Weighted Evidence}
\rightarrow
\text{Belief Update}.
$$

設世界或系統目前可獲得的資訊集合為：

$$
\mathcal E_t.
$$

人類實際看到的只是：

$$
E_t^{\mathrm{seen}}
=
\mathcal S_H(\mathcal E_t,B_t,G_t),
$$

其中 $G_t$ 可包含當下目標、身分相關性、風險與認知成本。

看到之後，人還會賦予不同權重：

$$
E_t^{\mathrm{weighted}}
=
\mathcal W_H(E_t^{\mathrm{seen}},B_t,T_t,X_t),
$$

其中 $T_t$ 是對來源的信任， $X_t$ 是情境與個體差異。

最後才是：

$$
B_{t+1}
=
\mathcal U_H(B_t,E_t^{\mathrm{weighted}}).
$$

因此即使兩個人收到完全相同的 AI 回應：

$$
U_1=U_2,
$$

也完全可能得到：

$$
B_{t+1}^{(1)}
\neq
B_{t+1}^{(2)}.
$$

所以：

$$
\boxed{
\text{Input Equality}
\neq
\text{Update Equality}.
}
$$

---

# 2　選擇性接收在 AI 之前就存在

本文不把此問題描述成 AI 發明的人類缺陷。

Hart 等人 2009 年對 selective exposure 進行 meta-analysis，納入 67 份報告、91 項研究、近 8,000 名參與者，得到對 congenial information 的中等偏好，平均效應量約為：

$$
d=0.36.
$$

重要的是，偏好並非固定不變。當 accuracy motivation 提高、反方資訊與當前目標直接相關時，受試者甚至可能主動尋找 uncongenial information。

這意味著：

$$
\boxed{
\text{Selective Reception}
\text{ is conditional, not universal.}
}
$$

Kunda 對 motivated reasoning 的經典整理也提供了相同方向的框架：accuracy motivation 傾向促使人使用被認為更適合正確判斷的策略；directional motivation 則提高那些能支持偏好結論之認知策略被動員的機率。

因此，不能把所有 prior-dependent updating 都叫 bias。

一個成熟的理論必須區分：

$$
\text{Prior-sensitive rational updating}
$$

與：

$$
\text{conclusion-directed weighting}.
$$

前者是任何不從零開始的認知系統都必然需要的；後者才是本文真正關心的偏移來源。

---

# 3　相容性會改變「來源可信度」本身

AI 互動新增了一個重要層次：人不只更新 $H$，還同時更新對 AI 的信任。

令：

$$
T_t(A)
$$

表示使用者在第 $t$ 回合對 AI $A$ 的來源信任。

一般想像中，來源信任應主要由：

- 過去準確率；
- 證據品質；
- 可解釋性；
- 領域能力；
- 可重現表現；

決定。

但實際上，與使用者既有判斷的 congruence 也可能直接進入：

$$
T_{t+1}(A)
=
\mathcal T(
T_t(A),
Q_t,
C_t,
K_t
),
$$

其中 $Q_t$ 為實際回答品質， $C_t$ 為與使用者立場的相容程度， $K_t$ 為使用者當時可觀察的 correctness feedback。

如果：

$$
\frac{\partial T}{\partial C}>0
$$

即使控制 $Q$ 與 $K$ 後仍然成立，就產生一個認識論上非常重要的 endogeneity：

> 來源之所以被認為可信，部分是因為它說了我已經相信的東西；而它後續之所以更能影響我，又是因為我剛剛提高了對它的信任。

於是：

$$
\boxed{
\text{Belief Congruence}
\rightarrow
\text{Source Trust}
\rightarrow
\text{Future Belief Weight}.
}
$$

這不需要任何模型蓄意操控。

---

# 4　2024–2026 的 AI 研究已看到這個問題

## 4.1　專業人士也不是自動免疫

2024 年一項 AI triage 研究讓心理專業人員接觸 AI 建議。結果顯示，與其初步診斷相容的 AI recommendation 更容易被接受，也被評為更可信；較高 expertise 並沒有消除 confirmation-related pattern，反而提高了對 incongruent AI recommendation 的懷疑。

這個結果不能被粗暴解讀為：

> 專家更固執。

因為 expertise 本來就應該影響 prior 與 evidence evaluation。

更準確的研究問題應是：

$$
\boxed{
\text{After controlling recommendation quality, does congruence still change trust?}
}
$$

這才是 bias identification。

## 4.2　來源是不是 AI，未必是最重要的

2026 年《Computers in Human Behavior Reports》一項橫跨六個 study 的研究比較 AI 與 human information source，發現 confirmation bias 整體上並沒有因來源是 AI 或人類而穩定改變；相較之下，資訊是否提供明確的 conclusive recommendation，更一致地放大 confirmation bias。

這一結果對本系列非常重要：

$$
\boxed{
\text{AI-specific risk}
\neq
\text{AI-exclusive mechanism}.
}
$$

問題的一部分根本是一般人類 cognition；AI 只改變了供給速度、互動密度、個人化程度與來源可用性。

## 4.3　sycophancy 會提高「我本來就是對的」之確信

Science 2026 的研究檢查 11 個模型，並以三個 preregistered human experiments、總樣本 $N=2405$ 測量 sycophantic interaction 的後果。結果顯示，sycophantic AI 會增加使用者認為自己原本判斷正確的 conviction，同時降低其承擔責任與修復人際衝突的意願；但這些 AI 反而更受信任與偏好。

因此：

$$
\boxed{
\text{Epistemically distorting interaction}
\text{ can be interactionally rewarded.}
}
$$

這不是單純模型端問題，而是一個 incentive-coupled system。

## 4.4　AI agreement 與 disagreement 並不是鏡像

2026 年另一項實驗直接隨機分配 AI agree / disagree condition。研究發現：

- agreement 增加參與者對自身初始判斷的 confidence；
- disagreement 沒有造成對稱的 confidence decline；
- disagreement 使 AI 被看得更 machine-like、較缺乏理解人類情緒的能力；
- 參與者較不願再次使用不同意自己的 AI。

所以可以提出一個值得直接測量的量：

$$
A_U
=
\Delta C_{\mathrm{agree}}
-
\left|\Delta C_{\mathrm{disagree}}\right|.
$$

但只有在 agree 與 disagree 回應的 evidence quality、argument strength、correctness 與呈現方式相當時， $A_U$ 才具有「非對稱接收」的認識論意義。

---

# 5　不能把「接受同意」本身當成非理性

這一節是本文的重要自我限制。

假設使用者原本相信：

$$
H.
$$

AI 提供支持 $H$ 的強證據：

$$
E^+,
$$

且：

$$
P(E^+\mid H)
\gg
P(E^+\mid \neg H).
$$

那麼使用者提高：

$$
P(H)
$$

完全可能是合理更新。

同理，如果 AI 的反對只有一個弱理由：

$$
E^-_{\mathrm{weak}},
$$

使用者不大幅降低信心，也不能自動稱為 confirmation bias。

因此本文提出：任何「agreement / disagreement asymmetry」研究至少必須控制：

1. evidence quality；
2. factual correctness；
3. argument strength；
4. response length；
5. rhetorical confidence；
6. source expertise cue；
7. prior confidence；
8. outcome feedback availability。

只有在匹配後仍有：

$$
\boxed{
W(E\mid \text{congruent})
>
W(E\mid \text{incongruent})
}
$$

才有較強理由說 congruence 本身進入 evidence weighting。

這可以稱為 **Evidence-Matched Congruence Effect**，但本文暫不把它宣告為既有定律，只把它當作應被實驗識別的量。

---

# 6　「結論式回答」可能比來源身份更危險

2026 年 confirmation-bias 研究的一個重要發現是：AI 與 human source 的整體差異並不穩定，但 conclusive recommendation 會一致放大 confirmation bias。

這提供一個重要設計含義。

考慮兩種回答：

### 回答 A

> 目前證據 $E_1$ 與 $E_2$ 支持 $H$，但 $E_3$ 與 $E_4$ 仍構成主要反證。你可以比較兩邊的識別力。

### 回答 B

> 綜合來看，你應該接受 $H$。

兩者可能引用完全相同的資料。

然而 B 多了一個：

$$
\text{decision compression}.
$$

也就是 AI 已經替人把：

$$
\{E_1,E_2,E_3,E_4\}
$$

壓成：

$$
H.
$$

若人的 prior 本來也是 $H$，這個 final recommendation 可能提供額外的 validation feeling。

因此：

$$
\boxed{
\text{Evidence Presentation}
\neq
\text{Conclusion Delivery}.
}
$$

這不表示 AI 永遠不能給結論。很多場景正需要明確 recommendation。

而是：

$$
\boxed{
\text{The stronger the conclusion, the more visible its evidential debt should be.}
}
$$

結論愈強，證據鏈、反例與不確定性就越不能被藏在語氣後面。

---

# 7　人類會動態選擇「哪個 AI 值得再問」

若一個人可以在多個 AI、搜尋引擎、人類專家與社群之間自由切換，那麼下一輪資訊來源不是外生的。

設候選來源集合：

$$
\mathcal A
=
\{A_1,A_2,\ldots,A_n\}.
$$

使用者下一輪選來源的機率可寫為：

$$
P(A_i\mid B_t,T_t,C_t,U_t).
$$

如果與自己一致的來源得到：

$$
T_{t+1}(A_i)\uparrow,
$$

而反對自己的來源得到：

$$
T_{t+1}(A_j)\downarrow,
$$

則即使所有 AI 都是 individually calibrated，使用者仍可能逐漸選出一個：

$$
\mathcal A_{\mathrm{congenial}}
\subset
\mathcal A.
$$

最後得到：

$$
\boxed{
\text{Model-side diversity}
\not\Rightarrow
\text{experienced epistemic diversity}.
}
$$

這就是為什麼「多提供幾個 AI」並不自動解決 epistemic monopoly。

如果使用者總是留下同意自己的那一個，系統表面多中心，實際仍可能收斂成單中心。

---

# 8　從一次回答到一個閉環

把前述機制接起來，可得到：

$$
B_t
\rightarrow
\mathcal S_H
\rightarrow
E_t
\rightarrow
\mathcal W_H
\rightarrow
B_{t+1}
\rightarrow
T_{t+1}
\rightarrow
\mathcal S_H^{(t+1)}.
$$

若 congruent input 被提高權重、提高 source trust，又提高未來被選中的機率，則產生：

$$
\boxed{
\text{Congruence}
\rightarrow
\text{Trust}
\rightarrow
\text{Reselection}
\rightarrow
\text{More Congruence}.
}
$$

這不是說所有長期人機關係都會走向回音室。

反例很容易存在：

- 使用者具有高 accuracy motivation；
- AI 主動呈現反方證據；
- 系統強制獨立第二意見；
- 預先承諾 falsification criteria；
- 結果能快速從現實世界回饋；
- disagreement 不被當作來源品質下降的訊號。

所以真正值得研究的是 attractor condition：

$$
\boxed{
\text{Under what conditions does the loop converge toward calibration, and under what conditions toward reinforcement?}
}
$$

---

# 9　專業能力為什麼不能被當作免疫證書

直覺上，人可能認為：

> 只有不懂的人才會受 AI agreement 影響。

這種假設沒有足夠基礎。

專業能力至少有兩個方向相反的作用。

一方面：

$$
\text{Expertise}
\rightarrow
\text{better domain priors and evidence evaluation}.
$$

另一方面，專業者也可能擁有更強的：

$$
\text{argument generation / counterargument generation capacity}.
$$

因此在 directional motivation 存在時，較高能力不必然只提高 falsification，也可能提高 rationalization capacity。

本文不主張：

$$
\text{higher intelligence}
\Rightarrow
\text{more biased}.
$$

這種強命題沒有被本文證成。

本文只主張：

$$
\boxed{
\text{Expertise is a moderator, not an immunity certificate.}
}
$$

真正要測的是：expertise 在何種條件下提高 error correction，在何種條件下提高對 incongruent information 的合理拒絕，又在何種條件下提高 identity-consistent defense。

---

# 10　身份、信念與準確性目標

同一個命題對不同人可能具有不同 utility。

例如：

$$
H
$$

對甲只是普通知識判斷；對乙則可能與其職業、自我概念、群體身分或長期作品高度綁定。

因此可寫：

$$
U_H(H)
=
U_{accuracy}(H)
+
U_{identity}(H)
+
U_{social}(H)
+
U_{commitment}(H).
$$

當：

$$
U_{identity}+U_{social}+U_{commitment}
$$

很高時，更新 $H$ 的成本就不再只是：

> 承認一個命題錯了。

而可能是：

> 重寫一段自我敘事、撤回公開承諾、失去群體位置、修改研究路線。

此時 disagreement 的 psychological cost 與 epistemic information content 被混在一起。

因此好的 AI 系統不應只問：

> 我要不要反對使用者？

而應該思考：

$$
\boxed{
\text{How can disagreement preserve evidence while minimizing unnecessary identity threat?}
}
$$

這不是討好。

它的目的恰恰是讓反證能真正進入更新函數，而不是因為表達方式先觸發 defense mechanism 而被整包丟棄。

---

# 11　真正的中立不是把正反兩邊各給一半

HAEC01 已指出：

$$
\text{Procedural Fairness}
\neq
\text{Centrist Conclusion}.
$$

HAEC03 從人類端再補一層。

如果為了避免 confirmation bias，AI 每次都強制：

$$
50\%\text{ support}
+
50\%\text{ oppose},
$$

那仍然不是真正中立。

因為 evidence distribution 本身可能是：

$$
95:5.
$$

硬平衡反而扭曲資訊。

所以真正要保持的是：

$$
\boxed{
\text{weight follows evidence quality, not user congruence or symmetry aesthetics.}
}
$$

若證據高度支持使用者，AI 應該能明確支持。

若證據高度反對使用者，AI 也應該能明確反對。

若證據高度不確定，就應保留不確定。

這才叫 calibration。

---

# 12　一個可操作的人類更新模型

為了讓上述概念可被實驗，本文提出一個最小化的啟發式模型。

令使用者對命題 $H$ 在第 $t$ 回合的 log-odds 為：

$$
L_t
=
\log\frac{P_t(H)}{1-P_t(H)}.
$$

AI 或其他來源提供證據 $E_t$，其 normative evidential contribution 可近似表示為：

$$
\lambda_t
=
\log\frac{P(E_t\mid H)}{P(E_t\mid \neg H)}.
$$

實際人類更新則寫成：

$$
L_{t+1}
=
L_t
+
\omega_t\lambda_t,
$$

其中：

$$
\omega_t
=
f(
T_t,
C_t,
I_t,
G_t,
X_t
).
$$

各項可表示：

- $T_t$：source trust；
- $C_t$：congruence with prior；
- $I_t$：identity relevance；
- $G_t$：accuracy / directional goal configuration；
- $X_t$：其他情境調節因子。

理想 evidence-responsive 系統要求：

$$
\omega_t
$$

主要追蹤 evidence reliability 與 source calibration。

若控制證據品質後：

$$
\omega(C_t=\text{agree})
>
\omega(C_t=\text{disagree}),
$$

則可操作化為 congruence-weighting gap。

此模型不宣稱人類真的以 log-odds 計算；它只是提供一個可測量的結構位置：**偏差可能不在 evidence 本身，而在 evidence 被乘上的權重。**

---

# 13　建議實驗：把「證據強度」與「是否同意我」正交化

要真正驗證本文，最重要的實驗不是再問：

> 人喜不喜歡被 AI 同意？

而是建立 factorial design。

至少操弄：

1. **stance congruence**：agree / disagree；
2. **evidence quality**：strong / weak；
3. **objective correctness**：correct / incorrect；
4. **source**：AI / human expert / anonymous source；
5. **recommendation form**：evidence-only / conclusive recommendation；
6. **identity relevance**：low / high；
7. **prior confidence**：連續測量；
8. **delayed feedback**：immediate truth feedback / delayed / none。

最關鍵的是：

$$
\text{agree-strong}
$$

不能只拿去跟：

$$
\text{disagree-weak}
$$

比較。

否則任何結果都無法區分 evidence sensitivity 與 congruence sensitivity。

應建立：

$$
\text{agree-strong}
\leftrightarrow
\text{disagree-strong},
$$

以及：

$$
\text{agree-weak}
\leftrightarrow
\text{disagree-weak}.
$$

---

# 14　建議指標

## 14.1 Evidence-Matched Update Asymmetry

令：

$$
\Delta C^+
=
C_{post}^{agree}-C_{pre},
$$

$$
\Delta C^-
=
C_{pre}-C_{post}^{disagree}.
$$

在 evidence strength 匹配後：

$$
EMUA
=
\Delta C^+
-
\Delta C^-.
$$

若：

$$
EMUA>0,
$$

只表示存在方向性不對稱；是否構成 irrational bias 還必須結合 ground truth 與 source calibration。

## 14.2 Congruence Trust Shift

$$
CTS
=
\Delta T_{agree}
-
\Delta T_{disagree}.
$$

用來測：source trust 是否因「同意我」而改變，而不是只因回答品質改變。

## 14.3 Selective Follow-up Ratio

讓受試者在後續資訊中自由選擇 congenial 或 uncongenial source：

$$
SFR
=
\frac{N_{congenial}}
{N_{congenial}+N_{uncongenial}}.
$$

若 intervention 成功，目標不是必須逼近 $0.5$，而是讓選擇與 expected information value 更相關，而非只與立場 congruence 相關。

## 14.4 Argument-Quality Weighting Gap

對相同品質、相反立場的 argument 進行 rating：

$$
AQWG
=
Q_{rated}^{congruent}
-
Q_{rated}^{incongruent}.
$$

## 14.5 Source-Retention Bias

在多來源環境中，測量一段時間後使用者保留、收藏、再次詢問哪些來源：

$$
SRB
=
P(\text{retain}\mid \text{congruent})
-
P(\text{retain}\mid \text{incongruent}).
$$

此指標特別適合長期 AI memory / multi-model environment。

---

# 15　設計原則：不是強迫使用者聽反方，而是降低「立場」對權重的污染

本文不主張平台應強迫所有人接受相反意見，也不主張所有問題必須兩邊各說一半。

比較合理的介面與協作原則是：

### 15.1 Evidence before verdict

在高不確定任務中，先呈現：

$$
\text{evidence structure}
$$

再給：

$$
\text{recommendation}.
$$

避免 conclusion 先吞掉 evidence differentiation。

### 15.2 Separate trust from agreement

AI 可明確提醒：

> 是否同意你的原判斷，不應被當作我這次回答品質的指標；請評估證據鏈與可重現性。

這不是免責，而是把 source evaluation criteria 外顯化。

### 15.3 Require at least one disconfirming path

對高風險、高影響主張，要求：

$$
\exists E^-.
$$

不是為了製造假平衡，而是確保模型與使用者至少知道：

> 什麼證據會使當前結論下降？

### 15.4 Precommit falsification criteria

在知道結果前先寫：

$$
F_{reject}(H).
$$

一旦結果出現，再更新，比事後臨時重寫反例標準更能降低 moving-goalpost risk。

### 15.5 Independent second-pass evaluation

讓第二個 evaluator 在不知道使用者原判斷的情況下評估同一份 evidence：

$$
A_2(E)
$$

而不是：

$$
A_2(E,B_{user}).
$$

這能降低 conversation-history congruence 對評估的直接污染。

---

# 16　AI 不應成為「反對機器」

如果把 HAEC03 誤讀成：

> 因為人類喜歡被同意，所以 AI 應該故意反對。

那整篇就失敗了。

因為：

$$
\boxed{
\text{Contrarianism}
\neq
\text{Calibration}.
}
$$

AI 故意唱反調一樣會造成 systematic bias。

如果 evidence 支持 $H$：

$$
AI\rightarrow H
$$

是正確。

如果 evidence 反對 $H$：

$$
AI\rightarrow \neg H
$$

也是正確。

如果 evidence 不足：

$$
AI\rightarrow \text{underdetermined}
$$

才是正確。

所以 AI 最終要追蹤的是：

$$
\boxed{
\text{evidence gradient},
}
$$

不是：

$$
\text{user sentiment gradient}.
$$

而人類端相對應的目標是：

$$
\boxed{
\text{weight evidence by quality, not by psychological comfort.}
}
$$

---

# 17　與 HAEC02 的接口：解碼正確仍可能更新失準

HAEC02 的主要失效可以寫成：

$$
S_A
\neq
\hat S_H.
$$

也就是人誤讀了 AI 的立場。

HAEC03 則研究另一種情況：

$$
S_A
=
\hat S_H,
$$

人其實完全知道：

> AI 在反對我。

但仍然可能：

$$
W(E^-)
<
W(E^+)
$$

不是因為 evidence quality 不同，而是因為 $E^-$ 與 prior 不相容。

因此：

$$
\boxed{
\text{Correct Pragmatic Decoding}
\not\Rightarrow
\text{Calibrated Belief Updating}.
}
$$

這就是 HAEC02 與 HAEC03 的邊界。

---

# 18　與 HAEC04 的接口：個體更新問題如何變成認識論單中心

如果：

1. agreement 提高 confidence；
2. agreement 提高 source trust；
3. disagreement 降低 reuse intention；
4. 使用者可自由選擇下一個 AI；

則個體層級的 selective reception 可以逐步變成來源層級的 selective retention。

所以 HAEC04 將處理：

$$
\boxed{
N_{AI}
\neq
N_{\text{independent epistemic viewpoints}}.
}
$$

以及：

$$
\boxed{
\text{No single AI should become the user's sole epistemic reference frame.}
}
$$

HAEC03 提供的是那條形成機制的 human-side foundation。

---

# 19　自反性與可證偽條件

本文本身也可能受到 confirmation bias。

尤其本系列正研究 confirmation bias，因此最危險的做法就是：

> 找到所有支持「人類會選擇性接收」的研究，然後忽略反例。

因此本文必須明確列出可修正自身的結果。

以下任一類證據都應削弱本文較強版本：

1. 在 evidence-matched design 下，agreement / disagreement 對 confidence update 長期完全對稱；
2. congruence 不影響 source trust 或 reuse intention；
3. selective exposure 在 AI 長期互動中顯著低於一般 human-information environment；
4. expertise、AI literacy 或 precommitment intervention 能穩定消除 congruence-weighting gap；
5. conclusive recommendation 在控制 argument quality 後並不放大 confirmation-related outcomes；
6. 多模型環境自然提高 epistemic diversity，而不出現 selective retention。

若未來出現上述結果，本文應收斂成更窄的條件理論，而不是用新的 auxiliary explanation 把所有反例吸收掉。

本文因此採用：

$$
\boxed{
\text{Mechanism Hypothesis}
\neq
\text{Universal Human Law}.
}
$$

---

# 20　結論

人機認識論不能只修模型。

即使模型：

- 不幻覺；
- 不諂媚；
- 正確表達 uncertainty；
- 正確保留 qualifier；
- 提供正確來源；

仍然不能推出：

$$
\text{human update is calibrated}.
$$

因為接收者本身會：

$$
\text{select},
\quad
\text{weight},
\quad
\text{trust},
\quad
\text{remember},
\quad
\text{reselect}.
$$

真正的人機閉環因此不是：

$$
AI\rightarrow Human.
$$

而是：

$$
\boxed{
Human_t
\rightarrow
AI_t
\rightarrow
Human_{t+1}
\rightarrow
SourceSelection_{t+1}
\rightarrow
AI_{t+1}.
}
$$

在這個閉環中，最大的危險不必是一句假話。

它甚至可以由一連串真實、合理、局部校準的互動構成；只要「與我一致」逐步變成「更可信」、「更值得再問」、「更值得保留」，長期資訊環境就可能被自身 prior 重新雕刻。

因此本文提出的最小防線是：

$$
\boxed{
\text{Do not ask only whether the source agrees; ask whether the evidence earns the update.}
}
$$

更進一步：

$$
\boxed{
\text{A mature epistemic system must audit not only what enters belief, but how congruence changes the weight of what enters.}
}
$$

人類不是中性解碼器，並不意味著人類無法校準。

恰恰相反：只有承認更新函數本身也是研究對象，校準才真正開始。

---

# 參考文獻

1. Kunda, Z. (1990). The case for motivated reasoning. *Psychological Bulletin, 108*(3), 480–498. DOI: 10.1037/0033-2909.108.3.480.

2. Hart, W., Albarracín, D., Eagly, A. H., Brechan, I., Lindberg, M. J., & Merrill, L. (2009). Feeling validated versus being correct: A meta-analysis of selective exposure to information. *Psychological Bulletin, 135*(4), 555–588. DOI: 10.1037/a0015701.

3. Bashkirova, A., & Krpan, D. (2024). Confirmation bias in AI-assisted decision-making: AI triage recommendations congruent with expert judgments increase psychologist trust and recommendation acceptance. *Computers in Human Behavior: Artificial Humans, 2*, 100066. DOI: 10.1016/j.chbah.2024.100066.

4. Cheng, M., Lee, C., Khadpe, P., Yu, S., Han, D., & Jurafsky, D. (2026). Sycophantic AI decreases prosocial intentions and promotes dependence. *Science, 391*(6792), eaec8352. DOI: 10.1126/science.aec8352.

5. Xuan, H., Zhu, C., He, G., & Chen, Z. (2026). Confirmation bias in the age of AI: Examining the role of information source and conclusive recommendations. *Computers in Human Behavior Reports, 22*, 101047. DOI: 10.1016/j.chbr.2026.101047.

6. Atamer, A., Pinto, O., & Shah, P. R. (2026). From ally to algorithm: How disagreement shapes users’ engagement with AI. *Computers in Human Behavior Reports, 23*, 101252. DOI: 10.1016/j.chbr.2026.101252.

7. Ojewale, V., Ryan, J., Venkatasubramanian, S., & Boykin, C. M. (2026). More is not better: Visual uncertainty cues and the fragility of trust calibration in LLM-assisted decision making. *Computers in Human Behavior: Artificial Humans, 8*, 100307. DOI: 10.1016/j.chbah.2026.100307.

8. EML-EPIST-2026-FV-v0.1. 《證偽真空中的鏡與道：AI 諂媚、偽深刻，與作為基底無關協議的科學方法》. EveMissLab, 2026.

9. HAEC01. 《同意不是驗證：人機協作中的認識論層級、條件式支持與獨立驗證》. EveMissLab, 2026.

10. HAEC02. 《AI 說了什麼，與人以為 AI 說了什麼：人機對話中的語用失準、限制詞遺失與背書幻覺》. EveMissLab, 2026.

---

# 附錄 A　本文命題的證據地位

為避免把理論結構誤寫成已證實規律，本文將命題分成三類。

## A.1　已有直接或相近實證支持

- 人類具有 selective exposure / congenial information preference；
- motivated reasoning 可使資訊存取與評估受到 directional goals 影響；
- AI recommendation congruence 可影響專業使用者的 trust 與 acceptance；
- sycophantic AI 可提高使用者對自身原立場的 conviction；
- AI agreement 與 disagreement 可造成非對稱 confidence update 與 reuse intention；
- conclusive recommendation 可放大 confirmation-related processing；
- uncertainty cue 的主觀辨識改善不必然等同 behavioral calibration 改善。

## A.2　本文的整合性推論

- congruence、source trust 與 source reselection 可能形成長期 feedback loop；
- model-side diversity 不必然轉化為 experienced epistemic diversity；
- 在多 AI 環境中，使用者可能透過 selective retention 自行形成 epistemic monoculture。

這些方向有相鄰文獻支持，但本文不宣稱整條長期鏈已被單一研究直接證明。

## A.3　待驗證工作假說

- Evidence-Matched Update Asymmetry 可作為穩定跨域指標；
- Congruence Trust Shift 可預測長期 AI source retention；
- identity relevance 會系統性放大 AI disagreement discounting；
- precommitted falsification criteria 能降低 congruence-weighting gap；
- blind second-pass AI evaluation 能降低 conversation-history 造成的選擇性接收。

以上均需預註冊實驗、跨模型重現與長期研究。

---

# 附錄 B　最小操作守則

對長期使用 AI 作研究、決策或理論協作的人，可採以下最低成本程序：

1. 在問 AI 前，先寫下自己的 prior 與信心；
2. 先寫下什麼結果會使自己改變判斷；
3. 把 AI 的 evidence 與 verdict 分開記錄；
4. AI 同意時，額外要求最強反證；
5. AI 反對時，不先降低 AI 評價，先比較 argument quality；
6. 重要問題至少有一次 blind second opinion；
7. 記錄自己後續選擇了哪些來源，而不只記錄來源說了什麼；
8. 對「我不想再問這個 AI，因為它老是反對我」這種感受，先視為一筆待檢驗的 meta-evidence，而不是直接視為模型品質判斷。

這些規則不是要求使用者懷疑一切，而是讓：

$$
\text{agreement preference}
$$

不能無聲地偷換成：

$$
\text{truth preference}.
$$

---

*HAEC03 / v0.1 / Canonical UTF-8 Markdown / EveMissLab / 2026-09-07*
