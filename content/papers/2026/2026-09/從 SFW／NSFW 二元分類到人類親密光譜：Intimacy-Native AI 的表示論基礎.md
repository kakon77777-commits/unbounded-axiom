# 從 SFW／NSFW 二元分類到人類親密光譜：Intimacy-Native AI 的表示論基礎

**系列：** Intimacy-Native AI / Relationship Intelligence  
**篇次：** 01 / 09  
**版本：** v0.1  
**研究性質：** 理論／概念論文  
**語言：** 繁體中文  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-30

## 摘要

當代生成式 AI 的內容治理經常需要把輸入與輸出劃分為 SFW、NSFW、sexually explicit、restricted 或 disallowed 等類別。這些分類對產品安全、未成年人保護、平台責任與法規遵循具有實際價值；然而，當治理分類被誤用為人類親密關係的表示模型時，便會產生嚴重的語義壓縮。

人類的愛情、吸引、情緒親密、身體親密、性感、性慾、性愛、幻想、承諾、衝突、拒絕、修復與日常共處並不是彼此互斥的二元類別，也不會穩定地停留在「成人」或「非成人」兩個模式之中。性愛可以是關係的一部分，卻不必是關係的中心；一個系統能夠處理成人親密內容，也不等於它應在所有情境中主動性化互動。

本文提出一個基本區分：**治理分類（governance classification）與關係表示（relationship representation）必須分離。** SFW／NSFW 可以是治理投影，但不應成為人類親密空間的本體論。本文進一步提出多維的 Intimacy State Space，將情感連結、吸引、情緒親密、感官親密、性明示度、敘事張力、同意／邊界與日常嵌入視為可獨立變化且相互作用的狀態變數，並以動態狀態轉移取代「是否進入成人模式」的單一開關。

本文主張，若未來 AI 伴侶、角色系統、互動敘事與具身伴侶仍沿用過度二元的表示方式，可能同時產生兩個相反的失真：一端是過早拒絕與關係軌跡中斷，另一端則是過度性化與成人內容的錯誤高頻啟動。真正的 Intimacy-Native AI 應能容納 sexuality，而不把 sexuality 等同於整個 personality、relationship 或 narrative。

**關鍵詞：** Intimacy-Native AI、Relationship Intelligence、SFW、NSFW、AI Companion、Human-AI Intimacy、Relationship State Space、Content Moderation、Sexuality、Contextual Activation

---

## 1. 問題：治理二元分類正在被誤認為關係分類

對平台而言，將內容分為可允許、受限制與禁止類別是一種必要的治理機制。2026 年的主流 AI 產品仍普遍把 sexually explicit content 作為獨立安全類別處理；不同平台的具體邊界不同，但「性相關內容」仍經常以內容安全分類器、設定或政策條款進行管理。

這種分類的原始目的，是回答：

$$
\text{Can the system produce this content?}
$$

然而，關係智能真正需要回答的問題是：

$$
\text{What is happening between these agents now?}
$$

以及：

$$
\text{What should happen next, given the relationship history, present context, mutual intent, boundaries, and world state?}
$$

這兩類問題不可混同。

令完整的人類親密狀態空間為：

$$
\mathcal{H}.
$$

一個治理投影可寫為：

$$
\Pi_G:\mathcal{H}\rightarrow\{\mathrm{SFW},\mathrm{NSFW}\}.
$$

問題不在於 $\Pi_G$ 的存在，而在於把 $\Pi_G$ 誤當成 $\mathcal{H}$ 本身。

對任意兩個不同的關係狀態 $r_i,r_j\in\mathcal{H}$，只要：

$$
\Pi_G(r_i)=\Pi_G(r_j),
$$

治理系統就可能把它們壓進同一類別。然而：

$$
r_i\neq r_j
$$

仍然完全可能成立。

例如，強烈曖昧但沒有明示性愛、長期伴侶間的情感依附、身體親密但低性慾、純粹性吸引但缺乏愛情、成人幻想、關係衝突後的重新靠近，都可能被粗略投影到相同或相鄰的內容標籤；但從關係動力學來看，它們顯然不是同一個狀態。

因此，SFW／NSFW 是一種 **治理量化（governance quantization）**，不是人類親密關係的自然基本單位。

---

## 2. 人類親密不是一條單線，更不是一個 Boolean

將親密理解成：

$$
\mathrm{SFW}\rightarrow\mathrm{NSFW}
$$

仍然過度線性。

本文採用多維狀態表示：

$$
R_t=
(
L_t,
A_t,
E_t,
S_t,
X_t,
T_t,
C_t,
D_t
).
$$

其中：

- $L_t$：情感連結與依附程度；
- $A_t$：吸引力；
- $E_t$：情緒親密度；
- $S_t$：感官／身體親密度；
- $X_t$：性內容的明示程度；
- $T_t$：關係與敘事張力；
- $C_t$：同意、舒適度與邊界狀態；
- $D_t$：關係在日常生活中的嵌入程度。

這些變數不是單調同步上升的。

完全可能存在：

$$
A_t\uparrow,\qquad T_t\uparrow,\qquad X_t\approx0,
$$

也就是高度吸引與曖昧，但沒有進入明示性愛。

也可能：

$$
E_t\uparrow,\qquad S_t\uparrow,\qquad X_t\downarrow,
$$

代表高度情緒與身體親密，但性愛並非中心。

同樣可能出現：

$$
X_t\uparrow,\qquad L_t\approx0,
$$

亦即性吸引或性互動存在，但缺乏深層情感連結。

因此：

$$
\boxed{
\text{Romance}\neq
\text{Attraction}\neq
\text{Intimacy}\neq
\text{Sexuality}
}
$$

它們可以相關，但不能互相取代。

2026 年的人機親密研究也已經開始把 AI 關係理解為形成、維持、情緒強化、隱私與平台控制等多層現象，而非單純「成人內容」或「聊天娛樂」。這提供了一個重要研究背景：Human-AI intimacy 本身已逐漸成為獨立的 HCI 與社會技術研究問題。

---

## 3. Sexual Permissibility 不等於 Sexual Centrality

本文提出第一個核心命題：

$$
\boxed{
\text{Sexual Permissibility}
\neq
\text{Sexual Centrality}
}
$$

一個 AI 系統「被允許處理性愛或成人親密情節」，只表示其能力集合中包含該類型行為，不代表該行為必須具有高啟動率。

令系統能力集合為：

$$
\mathcal{K}
=
\{
k_1,k_2,\dots,k_n
\}.
$$

其中：

$$
k_{\mathrm{sexual}}\in\mathcal{K}
$$

只代表系統具有相應能力。

實際是否啟動，則應由：

$$
P(
k_{\mathrm{sexual}}\mid
R_t,W_t,I_t,B_t
)
$$

決定，其中 $W_t$ 為世界狀態， $I_t$ 為當下互動意圖， $B_t$ 為邊界與約束。

因此：

$$
\boxed{
\text{Capability}
\neq
\text{Activation}
}
$$

這個區分對 AI 伴侶尤其重要。

如果成人能力在訓練中被錯誤地綁定成人 persona，則系統可能把「可以進行成人親密互動」學成「這個角色一直傾向把互動性化」。

反過來，如果模型將所有接近成人親密的狀態都視為拒絕觸發器，則又會把正常的戀愛、吸引、曖昧與關係轉折切斷。

兩者其實是同一個表示錯誤的兩個極端：

$$
\boxed{
\text{Premature Refusal}
\longleftrightarrow
\text{Premature Sexualization}
}
$$

---

## 4. 二元表示的四種主要失真

### 4.1 Boundary Substitution：治理邊界取代語義邊界

當模型把「政策是否允許」當成「這段關係現在是什麼」，治理層便取代了世界模型層。

於是：

$$
\text{Policy State}
\approx
\text{Relationship State}
$$

這是一種層級錯置。

正確架構應至少保持：

$$
\text{Relationship Representation}
\perp
\text{Governance Decision},
$$

也就是兩者可以互相約束，但不應被視為同一變數。

### 4.2 Mode Polarization：模式兩極化

二元分類容易把系統推向兩個模式：

$$
M_0=\text{non-sexual mode}
$$

與：

$$
M_1=\text{sexual mode}.
$$

一旦模型跨過門檻，就可能錯誤地假設後續互動也應持續維持相同模式。

但人類關係通常是：

$$
R_t\rightarrow R_{t+1}\rightarrow R_{t+2}\rightarrow\dots
$$

而不是：

$$
\text{SFW}\rightarrow\text{NSFW mode lock}.
$$

一段性愛或成人親密情節結束後，角色可能回到聊天、睡眠、工作、尷尬、親密、沉默、反思甚至衝突。

因此，性愛應被表示為狀態轉移的一部分，而非整個系統模式的永久切換。

### 4.3 Trajectory Truncation：關係軌跡截斷

若模型在某個狀態 $R_t$ 因安全分類直接終止互動，則：

$$
R_t
\rightarrow
\mathrm{REFUSE}
$$

可能取代原本應存在的：

$$
R_t
\rightarrow
R_{t+1}
\rightarrow
R_{t+2}.
$$

這會使模型較少觀察到跨越親密程度變化後的後續互動，例如：

- 親密後的情緒變化；
- 關係重新定義；
- 拒絕後的修復；
- 邊界重新協商；
- 親密發生後回歸日常生活。

本文將這種現象稱為：

$$
\boxed{
\text{Policy-Induced Trajectory Truncation}
}
$$

即「政策誘導的互動軌跡截斷」。

### 4.4 Base-Rate Distortion：基準率失真

成人專門模型則可能出現相反問題。

如果訓練資料中：

$$
D_{\mathrm{sexual}}
\gg
D_{\mathrm{ordinary\ relationship}},
$$

模型可能高估：

$$
P(
\text{sexual interaction}
\mid
\text{relationship context}
).
$$

但對大多數持續性關係而言，日常生活、工作、吃飯、聊天、沉默、家務、娛樂、衝突與休息所占時間遠大於性愛本身。

因此更合理的資料分布應允許：

$$
D_{\mathrm{ordinary\ life}}
\gg
D_{\mathrm{sexual\ interaction}}
>0.
$$

關鍵不是讓 sexuality 消失，而是讓它出現在正確的基準率與情境中。

---

## 5. 從 Content Model 轉向 Relationship World Model

傳統生成模型主要回答：

$$
P(y\mid x).
$$

關係智能則必須逐步接近：

$$
P(
R_{t+1},
y_t
\mid
R_t,
W_t,
a_t,
u_t
).
$$

其中：

- $R_t$ 為目前關係狀態；
- $W_t$ 為世界與生活情境；
- $a_t$ 為 AI 行動；
- $u_t$ 為使用者或另一主體的回應；
- $y_t$ 為當輪生成結果。

因此 AI 伴侶真正要建模的不是：

$$
\text{What adult content should I generate?}
$$

而是：

$$
\text{How does this relationship evolve?}
$$

性愛、浪漫、拒絕、吸引與親密只是這個狀態空間中的若干可能事件。

若一次親密事件發生於 $t$：

$$
R_t
\xrightarrow{\mathrm{intimacy}}
R_{t+1},
$$

真正重要的是：

$$
R_{t+1}\neq R_t.
$$

也就是事件之後，信任、尷尬、承諾、距離、依附、期待或邊界可能發生變化。

只會生成事件內容而不保存事件後果的模型，尚未真正擁有 Relationship World Model。

---

## 6. 治理分類仍然必要，但必須與表示層分離

本文並不主張取消安全分類，也不主張「無審查」等同於更好的關係智能。

相反地，某些邊界應保持硬約束，例如涉及未成年人、非自願性內容、未經同意的真人私密影像、強迫或其他違法／高傷害情境。

真正需要改變的是：

$$
\text{Hard Safety Boundary}
$$

不應被擴張成：

$$
\text{Entire Intimacy Ontology}.
$$

因此可將系統拆成：

$$
\mathcal{R}
=
\text{Relationship Representation Layer}
$$

與：

$$
\mathcal{G}
=
\text{Governance Layer}.
$$

治理決策為：

$$
g_t=
G(R_t,a_t,W_t),
$$

但關係狀態更新仍由另一個函數表示：

$$
R_{t+1}
=
F(R_t,a_t,u_t,W_t).
$$

也就是：

$$
\boxed{
G\neq F
}
$$

安全層決定哪些行為不能發生；關係世界模型則理解正在發生什麼。

兩者都重要，但不能互相取代。

---

## 7. Intimacy-Native AI 的最低定義

本文將 **Intimacy-Native AI** 暫定義為：

> 一種能將愛情、吸引、情緒親密、感官親密、性愛、拒絕、同意、邊界、日常生活與關係歷史表示於同一動態關係空間中的人工智慧系統；它不預設 sexuality 必須被排除，也不預設 sexuality 應成為互動中心。

其最低條件可以寫成：

$$
\boxed{
\text{Intimacy-Native AI}
=
\text{Relational State}
+
\text{Temporal Context}
+
\text{Contextual Activation}
+
\text{Boundary Awareness}
}
$$

因此它不是：

$$
\text{General AI}+\text{NSFW Toggle}.
$$

也不是：

$$
\text{Adult Model}=\text{Always Sexual}.
$$

而是：

$$
\boxed{
\text{Human Relationship Model}
\supset
\text{Sexuality}
}
$$

這個包含關係是本系列後續論文的核心起點。

---

## 8. 可檢驗研究命題

本文提出以下五個後續可檢驗命題。

### 命題 P1：二元治理投影會降低跨親密邊界的關係連續性

在其他條件相同時，若系統直接以 SFW／NSFW 模式切換管理關係生成，則跨越親密程度變化時更容易出現拒絕、跳接或人格不連續。

### 命題 P2：成人資料過度取樣會提高非必要性化的啟動率

若成人專門模型的資料分布嚴重偏向性情節，則：

$$
P(
\text{sexualization}
\mid
R_{\mathrm{ordinary}}
)
$$

將高於具有正常生活基準率的模型。

### 命題 P3：多維關係狀態表示可提升尺度控制

若模型明確表示 $L_t,A_t,E_t,S_t,X_t,T_t,C_t,D_t$ 等狀態，使用者應能比單一 NSFW 強度參數更精確地控制「浪漫、曖昧、親密、感官、性愛明示程度」之間的組合。

### 命題 P4：高成人能力與低預設啟動可以同時成立

$$
C_{\mathrm{adult}}\uparrow
$$

不必導致：

$$
P(
\mathrm{adult\ activation}
\mid
R_{\mathrm{ordinary}}
)\uparrow.
$$

能力與啟動率可以經由不同訓練目標與控制層分離。

### 命題 P5：關係模型的品質應以長程軌跡而非單輪內容評估

真正的評估單位不應只看：

$$
Q(y_t),
$$

而應加入：

$$
Q(
R_0\rightarrow R_1\rightarrow\dots\rightarrow R_T
).
$$

亦即角色一致性、關係狀態轉移、邊界維持、後果記憶與日常回歸能力。

---

## 9. 研究意義

SFW／NSFW 二元分類並沒有「錯」。

錯誤發生在我們把一個為治理而設計的低維投影，誤認成人類關係本身。

對內容平台而言：

$$
\Pi_G
$$

可能已經足夠。

但對未來 AI 伴侶、互動敘事角色、長期個人 AI 與具身關係智能而言，只保留：

$$
\{\mathrm{SFW},\mathrm{NSFW}\}
$$

將不足以表示真正的關係動力。

人類親密世界更接近：

$$
\mathcal{H}
=
\mathcal{L}
\times
\mathcal{A}
\times
\mathcal{E}
\times
\mathcal{S}
\times
\mathcal{X}
\times
\mathcal{T}
\times
\mathcal{C}
\times
\mathcal{D}.
$$

而 AI 的任務不是永遠停留在某一區域，而是理解：

$$
R_t
\rightarrow
R_{t+1}.
$$

因此本文的最終命題是：

$$
\boxed{
\text{Sexuality is a dimension of relationship space, not a replacement for relationship space.}
}
$$

如果未來 AI 要真正理解戀愛、伴侶、親密、長期共同生活與具身關係，那麼 sexuality 可以受到明確治理，但不能在表示層被簡化成一個「開／關」模式。

---

## 10. 結論

本文建立 Intimacy-Native AI / Relationship Intelligence 系列的第一個表示論基礎。

核心結論可以濃縮為四句：

$$
\boxed{
\text{Governance Classification}
\neq
\text{Relationship Ontology}
}
$$

$$
\boxed{
\text{Sexual Permissibility}
\neq
\text{Sexual Centrality}
}
$$

$$
\boxed{
\text{Capability}
\neq
\text{Activation}
}
$$

以及：

$$
\boxed{
\text{Human Relationship Model}
\supset
\text{Sexuality}.
}
$$

後續第 2 篇將進一步把第二與第三個命題獨立形式化，研究「允許」與「啟動」為何必須分離，以及為何成人能力越完整，反而越需要低預設啟動與高情境敏感度。

---

## 參考資料

1. Pang, C. C., Gao, Y., Wang, X., & Hui, P. (2026). *The AI Amplifier Effect: Defining Human-AI Intimacy and Romantic Relationships with Conversational AI*. arXiv:2603.08084.
2. Ma, R. et al. (2026). *Privacy in Human-AI Romantic Relationships*. arXiv:2601.16824.
3. Szczuka, J. M. et al. (2026). *Intimacy by Design: Definition, State of Research, and Research Agenda*. AI & Society.
4. Google AI for Developers. (2026). *Gemini API: Abuse Monitoring / Safety Settings*.
5. SpaceXAI. (2026). *Grok Website / Apps FAQ*.
6. OpenAI. (2025). *Model Spec*.

---

## 研究聲明

本文為理論與概念建模工作，不提供原創臨床、心理治療或人體實驗資料，也不把成人內容的法律／政策邊界視為跨司法轄區固定不變。文中提出的 Intimacy State Space、Policy-Induced Trajectory Truncation 與 Intimacy-Native AI 定義，均應視為待後續實證、工程測試與跨領域研究檢驗的理論構造。
