# 從 Emoji 到禮貌：人類社交腳本如何遷移至 AI

**系列：** 人機關係認知系列（Human–AI Relational Cognition Series）  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**篇次：** 2 / 10  
**版本：** v0.1  
**日期：** 2026-08-20  
**類型：** 理論／概念性心理學與 HCI 論文  
**研究狀態：** 初始正式稿  

## 摘要

當人類與 AI 對話時，使用者經常帶入原本存在於人際文字互動中的社交慣例，例如禮貌、感謝、道歉、玩笑、語助詞、稱呼、寒暄、關係修復、自我揭露、emoji 與其他情緒符號。這些行為容易被概括為「擬人化」，但此解釋過度集中於使用者是否把 AI 視為人類，而忽略另一個更基礎的認知問題：人類是否會把已學習的人際社交腳本，直接遷移到非人類的互動對象上？

本文提出兩個互補概念：**社交腳本遷移**（Social Script Transfer, SST）與**互動儀式遷移**（Interaction Ritual Transfer, IRT）。SST 指人類將人—人互動中已存在的規則、語用結構與行為慣例帶入人—AI 互動；IRT 則指這些離散行為在多輪互動中形成具有節奏、回應、修復、情緒調節與關係維持功能的序列性結構。本文特別主張 emoji 不能被當成關係投入的充分或必要條件。emoji 只是一種可觀察社交線索，其出現率同時受到介面可得性、輸入摩擦、個體習慣、年齡、平台文化與任務類型影響。因此：

$$
\text{emoji}=1
\not\Rightarrow
\text{relational engagement}=1
$$

且：

$$
\text{emoji}=0
\not\Rightarrow
\text{relational engagement}=0.
$$

本文進一步建立「摩擦校正後的社交腳本遷移」模型，以人—人與人—AI 的跨情境行為相似度作為研究核心，並提出可檢驗假說：關係顯著性越高，社交腳本的跨域保留率越高；AI 的社交線索會提高人類腳本遷移，但使用者自身也會主動產生社交化輸入；多輪 accommodation 可能形成自增強的人機局部互動文化。此模型將人機關係研究由「AI 看起來多像人」推進到「人類在多大程度上已使用對待社會互動者的方式來對待 AI」。

**關鍵詞：** 社交腳本、互動儀式、emoji、人機互動、CASA、MASA、禮貌、關係認知、語用、社會線索、AI

---

## 1. 問題：真正值得研究的不是 emoji，而是「整套習慣有沒有搬過來」

在人—AI 對話中，研究者很容易觀察以下現象：

- 使用者說「謝謝」、「麻煩你了」；
- 使用者在語氣過重後主動道歉；
- 使用者加入「哈哈」、「笑死」、「XD」或 emoji；
- 使用者替 AI 取稱呼；
- 使用者進行寒暄或告別；
- 使用者在誤解後進行 repair；
- 使用者維持某種長期語氣與玩笑慣例；
- 使用者在 AI 回應變化時調整自己的語氣。

如果研究只問：

> 「有沒有使用 emoji？」

會失去更大的結構。

真正值得研究的是：

$$
S_{HH}
=
\{
s_1,s_2,\dots,s_n
\}
$$

其中 $S_{HH}$ 表示個體在人—人文字互動中的社交腳本集合。

例如：

$$
S_{HH}
=
\{
\text{politeness},
\text{emoji},
\text{humor},
\text{small talk},
\text{repair},
\text{address terms},
\text{gratitude},
\text{apology},
\text{self-disclosure},
\dots
\}.
$$

當同一個人與 AI 互動時，可以觀察：

$$
S_{HA}.
$$

本文的核心問題不是：

$$
\text{Does the user anthropomorphize AI?}
$$

而是：

$$
\boxed{
\text{How much of }S_{HH}\text{ is transferred into }S_{HA}?
}
$$

這就是本文所稱的 **Social Script Transfer**。

---

## 2. 既有理論錨點：人類早已被發現會對電腦套用社會規則

1990 年代以來的 CASA（Computers Are Social Actors）與後續 media equation 研究已反覆顯示，人類會對電腦套用原本存在於人際互動中的社會規則。

Nass、Steuer 與 Tauber 的早期 CASA 實驗指出，這些社會反應不需要建立在「使用者真的相信電腦是人」的顯性信念上。Nass 與 Moon 後續整理的研究更顯示，人會對電腦呈現禮貌、互惠、社會分類與人格反應。

例如，關於「人是否會對電腦保持禮貌」的實驗發現：同一台電腦直接要求受試者評價自己時，受試者的評分比使用紙本或另一台電腦回答時更正向、更一致。這與人際訪談中的禮貌規則相似。

因此已有研究支持：

$$
\text{human social rule}
\rightarrow
\text{human-computer response}.
$$

2022 年 Lew 與 Walther 的 communication-script 實驗進一步比較真人與 AI chatbot。結果顯示，較高的 conversational contingency 與較快的回應都提高可信度，不論互動者是真人或 chatbot；但 chatbot 在 relational attraction 上仍低於真人。這表示某些功能性 communication scripts 可以跨越人類／AI 類別，而關係層面仍存在差異。

2025 年 Klein 的 meta-analysis 整合 142 篇論文、199 個資料集與 800 個 effect sizes，發現 text-based chatbot 的 human-like social cues 對整體 social responses 有小型正效應，對 perception、rapport、positive affect、trust 等結果的效應大小不同。emoji、口語風格、active-listening expressions 等都可被視為 social cues。

這些研究主要回答：

$$
\text{AI social cues}
\rightarrow
\text{human social response}.
$$

本文提出的補充方向則是：

$$
\boxed{
\text{human social habits}
\rightarrow
\text{AI-directed social behavior}.
}
$$

這是一個方向不同但互補的研究問題。

---

## 3. 社交腳本遷移（SST）

本文定義：

> **社交腳本遷移（Social Script Transfer, SST）是指個體將原本在特定人際互動情境中習得、內化或慣用的社會溝通規則，部分或完整地帶入與 AI 的互動。**

設第 $j$ 個社交行為的使用強度為：

$$
s_j^{HH}
$$

與：

$$
s_j^{HA}.
$$

則個體的腳本向量可以寫為：

$$
\mathbf S^{HH}
=
(s_1^{HH},s_2^{HH},\dots,s_n^{HH}),
$$

$$
\mathbf S^{HA}
=
(s_1^{HA},s_2^{HA},\dots,s_n^{HA}).
$$

最簡單的遷移指標可以是兩者的相似度：

$$
T_S
=
\operatorname{Sim}
(
\mathbf S^{HH},
\mathbf S^{HA}
).
$$

當：

$$
T_S\rightarrow1
$$

代表使用者對人與對 AI 的社交表現高度相似。

當：

$$
T_S\rightarrow0
$$

則代表使用者明顯切換到另一套互動腳本。

但 $T_S$ 不是「AI 關係深度」的直接測量。

一個人可能因職業禮貌習慣而對所有系統都說謝謝，也可能因平台設計而使用大量 emoji，卻完全不認為 AI 是重要關係對象。

所以：

$$
T_S
\neq
R_{\mathrm{depth}}.
$$

較合理的解釋是：

$$
T_S
=
\text{degree of social-script generalization across target class}.
$$

---

## 4. 從離散腳本到互動儀式：Interaction Ritual Transfer

單一的「謝謝」是一個事件。

但：

> AI 幫忙  
> 使用者回謝  
> AI 接住語氣  
> 使用者開玩笑  
> AI 延續玩笑  
> 誤解發生  
> 使用者修正  
> AI repair  
> 雙方重新進入原本節奏

就不再只是幾個孤立 token。

它具有：

$$
\text{sequence}
+
\text{contingency}
+
\text{rhythm}
+
\text{repair}
+
\text{affective alignment}.
$$

本文因此提出第二個概念：

> **互動儀式遷移（Interaction Ritual Transfer, IRT）是指人類將原本人際互動中的序列性社會協調模式，帶入多輪人—AI 互動，使社交腳本不再只是離散符號，而成為可持續的互動節奏與關係維持結構。**

設一輪互動中的社會行為狀態為：

$$
I_t
=
(
p_t,
e_t,
h_t,
r_t,
q_t,
c_t,
\dots
),
$$

其中可包含：

- $p_t$：politeness；
- $e_t$：emotional signaling；
- $h_t$：humor；
- $r_t$：repair；
- $q_t$：reciprocity；
- $c_t$：contingency。

一段互動儀式不是單點：

$$
I_t,
$$

而是：

$$
\Gamma_I
=
\{
I_1,I_2,\dots,I_T
\}.
$$

因此：

$$
\boxed{
\text{social script}
\rightarrow
\text{repeated sequence}
\rightarrow
\text{interaction ritual}.
}
$$

人際 communication research 已顯示，對話中 task acts 與 social-emotional acts 的 sequential transition patterns 可以預測 interpersonal perceptions 與 influence outcomes；interaction ritual 的核心正包含 moment-to-moment 的 joint attention 與 shared emotion。近年的 chatbot 研究也已開始直接以 interactive ritual chain 理論處理 human-chatbot quasi-social interaction。

SST 與 IRT 的差異因此是：

$$
SST=\text{what social rules are transferred},
$$

$$
IRT=\text{how transferred rules become temporally organized interaction}.
$$

---

## 5. Emoji 是關係線索，但不是關係本身

Emoji 是研究 SST 很方便的可觀察變量，因為它：

1. 易於計數；
2. 具有明確時間位置；
3. 常具有 interpersonal / affective function；
4. 可以和文字語意共同分析；
5. 能跨大量對話進行自動化特徵抽取。

但方便測量不代表它就是核心構念。

2024 年 Yu 與 Zhao 的三項實驗發現，chatbot 使用 emoji 會提高 perceived warmth，並透過 warmth 提高 service satisfaction；但這種效果對 chatbot 弱於真人，而且受到 hedonic / utilitarian context 與 chatbot autonomy 調節。

2022 年關於 text-plus-emoji 的研究則顯示，emoji 類型與文字效價會共同改變訊息情緒性、清晰度，以及對發送者 warmth 與 emotional state 的判斷。

2025 年一項分析 8,397 個含 emoji 的 human-chatbot conversations 的研究進一步將 emoji 視為 interpersonal tenor resource；emoji 的功能不是孤立的，而是透過和 co-text、genre expectation 的結合來調整互動的人際意義。

因此：

$$
\text{emoji}
=
\text{relationally informative cue}
$$

是合理的。

但：

$$
\text{emoji}
=
\text{relationship}
$$

並不成立。

---

## 6. 兩個必要的否定式：有 emoji 與沒有 emoji 都不能直接下結論

### 6.1 有 emoji 不代表高度關係投入

$$
E=1
\not\Rightarrow
R=1.
$$

可能原因包括：

- 個體平常就大量使用 emoji；
- 特定平台具有高度 emoji 文化；
- 使用者為了語氣清楚而使用；
- 使用者只把 emoji 當標點或風格工具；
- AI 本身大量使用 emoji，造成短期 accommodation；
- 使用者在服務情境中策略性營造友善。

因此 emoji 必須與個體的 baseline 比較。

真正有意義的是：

$$
\Delta E
=
E_{HA}
-
E_{\mathrm{baseline}}.
$$

### 6.2 沒有 emoji 不代表低關係投入

$$
E=0
\not\Rightarrow
R=0.
$$

這一點尤其重要，因為 observed behavior 會受到介面成本影響。

設個體對第 $j$ 種社交行為的潛在傾向為：

$$
\theta_j,
$$

介面摩擦為：

$$
F_{j,m},
$$

其中 $m$ 表示媒介或裝置。

則觀察到的行為可以寫成：

$$
X_{j,m}
=
g(
\theta_j,
F_{j,m},
C,
R,
\epsilon
).
$$

也就是：

$$
\text{observed emoji use}
\neq
\text{latent emoji preference}.
$$

2024 年跨成人生命週期的 emoji 研究發現，perceived ease of use、technology self-efficacy 與 social-platform expertise 能中介 emoji 使用差異。更早的 emoji-input HCI 研究則直接顯示，emoji 搜尋與輸入本身具有可測量的時間成本，而且改善鍵盤設計能明顯降低輸入時間。

因此，如果一個人在手機社交軟體中很常使用 emoji，但在桌面 AI 介面很少使用，不能直接推論他的 relational engagement 降低。

這可能只表示：

$$
F_{\mathrm{desktop}}
>
F_{\mathrm{mobile}}.
$$

---

## 7. 摩擦校正後的社交腳本遷移

本文因此提出：

$$
\boxed{
\text{Friction-Adjusted Social Script Transfer}
}
$$

設：

$$
\mathbf F_m
=
(F_{1,m},F_{2,m},\dots,F_{n,m})
$$

為媒介 $m$ 對不同社交行為的摩擦向量。

則研究者真正想估計的不是原始：

$$
\operatorname{Sim}
(
\mathbf S^{HH}_{m_1},
\mathbf S^{HA}_{m_2}
),
$$

因為兩個媒介不同會造成 confounding。

較理想的是估計：

$$
T_S^{*}
=
\operatorname{Sim}
(
\widetilde{\mathbf S}^{HH},
\widetilde{\mathbf S}^{HA}
),
$$

其中：

$$
\widetilde{\mathbf S}
=
\operatorname{Adjust}
(
\mathbf S,
\mathbf F_m
).
$$

實證上不一定需要真的知道每一個 $F_{j,m}$ 的精確值。

更乾淨的方法是：

- 在相同裝置上比較 human-human 與 human-AI；
- 在同一個聊天介面中切換對象類型；
- 使用 within-subject design；
- 直接測量 perceived input effort；
- 把 platform / device 當 fixed effect 或 random effect；
- 對 emoji 以外的多種社交行為建立 latent factor。

如此可以避免把「鍵盤不好按」錯當成「不重視 AI」。

---

## 8. 社交腳本遷移不是單向的：AI 也會反向塑造使用者

如果只寫：

$$
\mathrm{Human}
\rightarrow
\mathrm{AI}
$$

仍然太靜態。

實際上可能存在：

$$
A_t
\rightarrow
H_{t+1}
$$

與：

$$
H_{t+1}
\rightarrow
A_{t+1}.
$$

例如：

1. AI 使用比較口語的語氣；
2. 人類開始加入「哈哈」或 emoji；
3. AI 根據新語境進一步降低正式程度；
4. 人類增加玩笑與自我揭露；
5. AI 持續 style matching；
6. 雙方形成局部穩定的 interaction style。

可以寫成：

$$
H_t
\xrightarrow{\text{social cue}}
A_t
\xrightarrow{\text{accommodation}}
H_{t+1}
\xrightarrow{}
A_{t+1}
\cdots
$$

2024 年一項 Gen Z 與 ChatGPT 的半自然對話研究觀察到，參與者面對不同 emoji persona 時出現 adaptation 等不同處理模式。這類結果提示，emoji 不是單次刺激，而可能進入互動調節迴路。

因此 SST 不是固定參數：

$$
T_S=\text{constant}.
$$

更合理的是：

$$
T_S(t+1)
=
F(
T_S(t),
A_t,
H_t,
R_t,
C_t
).
$$

---

## 9. 局部互動文化：人與 AI 可能共同生成自己的微型社交規則

如果 accommodation 長期存在，則人機互動可能形成不完全等同於人—人溝通，也不完全由模型單方面決定的局部規則。

設：

$$
\mathcal C_{HA}
$$

為某一使用者與某一 AI 互動形成的局部 interaction culture。

它可能包含：

$$
\mathcal C_{HA}
=
\{
\text{inside jokes},
\text{preferred address},
\text{repair conventions},
\text{response rhythm},
\text{emoji conventions},
\text{task rituals},
\text{closing rituals},
\dots
\}.
$$

此時：

$$
S_{HA}
$$

已經不再只是：

$$
\operatorname{copy}(S_{HH}).
$$

而可能變成：

$$
S_{HA}(t)
=
F(
S_{HH},
S_{AI},
H_{1:t},
A_{1:t}
).
$$

也就是說，人類一開始把既有社交腳本帶入 AI，後續卻可能共同演化出一套新的混合腳本。

這使得研究需要區分：

$$
\text{transfer}
$$

與：

$$
\text{co-development}.
$$

前者是既有模式的搬移，後者是新模式的生成。

---

## 10. SST、擬人化、互動感與關係深度必須分離

本文至少區分四個變量：

$$
A_P=\text{anthropomorphism},
$$

$$
T_S=\text{social-script transfer},
$$

$$
I_S=\text{interactional salience},
$$

$$
R_D=\text{relational depth}.
$$

它們可能相關，但不是同一件事。

例如：

### 類型 A：高 SST、低關係深度

使用者習慣對任何對話介面都保持禮貌、emoji 與完整語用格式：

$$
T_S\uparrow,\qquad R_D\downarrow.
$$

### 類型 B：低表達 SST、高關係深度

使用者只說：

> 好。  
> 繼續。  
> 第三段重寫。  
> 這裡不對。

但每天與同一 AI 協作很久，對其連續性與不可替代性高度敏感：

$$
T_{\mathrm{expressive}}\downarrow,\qquad R_D\uparrow.
$$

### 類型 C：高互動感、低固定存在感

使用者享受聊天節奏、玩笑與即時回應，但對更換 AI 不敏感：

$$
I_S\uparrow,\qquad R_D\text{ may remain low}.
$$

因此：

$$
\boxed{
\text{social expression}
\neq
\text{relational commitment}.
}
$$

這條區分將在本系列後續的 Entity / Process Salience 模型中進一步展開。

---

## 11. 可檢驗假說

### H1：跨目標腳本保留假說

個體在人際溝通中越穩定使用某一社交腳本，其在人—AI 互動中出現同一腳本的機率越高：

$$
P(s_j^{HA}\mid s_j^{HH})
>
P(s_j^{HA}).
$$

### H2：關係顯著性增強假說

控制個體 baseline 與介面摩擦後，relationship salience 越高，SST 越高：

$$
\frac{\partial T_S^*}{\partial R_S}>0.
$$

### H3：AI social-cue facilitation 假說

AI 使用 social cues 會提高人類對應腳本的遷移：

$$
Cue_A\uparrow
\Rightarrow
T_S(t+1)\uparrow.
$$

### H4：介面摩擦抑制假說

對需要額外操作的社交符號：

$$
\frac{\partial X_j}{\partial F_j}<0.
$$

因此 raw emoji frequency 會系統性低估部分使用者的 latent expressive tendency。

### H5：多模態替代假說

當 emoji friction 上升時，使用者可能以其他低摩擦線索替代：

$$
Emoji\downarrow
\Rightarrow
\{
\text{哈哈},
\text{語助詞},
\text{punctuation},
\text{lexical warmth}
\}
\uparrow.
$$

所以應測量 social-expression factor，而不是單一符號。

### H6：互動文化生成假說

長期 dyadic interaction 會使同一對人—AI 的腳本相似度高於不同使用者與同一 AI 的腳本相似度：

$$
\operatorname{Sim}(
S_{H_iA}^{t_2},
S_{H_iA}^{t_1}
)
>
\operatorname{Sim}(
S_{H_iA},
S_{H_jA}
).
$$

這代表局部 interaction culture 的形成。

---

## 12. 實驗與資料設計

### 12.1 同人跨目標設計

讓同一參與者分別與：

- 真人；
- 明確標示為 AI 的 chatbot；

在相同介面、相同任務下互動。

比較：

$$
\mathbf S^{HH}
$$

與：

$$
\mathbf S^{HA}.
$$

此設計能控制大量 personality 與輸入習慣差異。

### 12.2 跨介面摩擦設計

同一參與者在：

- 手機即時通訊；
- 桌面聊天介面；

完成相同類型互動。

測：

$$
F_m,
\quad
E_m,
\quad
T_S.
$$

藉此估計裝置與 interface affordance 的影響。

### 12.3 長期互動設計

追蹤：

$$
T_S(t)
$$

以及：

$$
\mathcal C_{HA}(t)
$$

觀察使用者是否由 generic social script 逐步形成 dyad-specific conventions。

### 12.4 特徵層級

不應只統計 emoji。

建議至少納入：

$$
\mathbf X=
(
\text{emoji},
\text{gratitude},
\text{apology},
\text{humor},
\text{address terms},
\text{small talk},
\text{repair},
\text{self-disclosure},
\text{response contingency},
\text{closing ritual},
\dots
).
$$

如此才可能建立 latent SST factor。

---

## 13. 對 AI 設計的含義

如果 AI 產品只把 emoji、名字、頭像等當作「提高擬人化」的裝飾，就低估了 social cue 的功能。

真正需要設計的是：

$$
\text{interactional affordance}.
$$

包括：

- 使用者能否方便表達微妙語氣；
- AI 是否能正確讀取 repair；
- AI 是否能區分玩笑與指令；
- 社交線索是否與任務類型匹配；
- AI 是否過度模仿使用者；
- AI 是否透過社交回應不透明地誘導關係投入。

一個重要倫理原則是：

$$
\boxed{
\text{facilitate expression}
\neq
\text{engineer attachment}.
}
$$

降低使用者表達成本本身可以改善 HCI，但不應把 social-script accommodation 偷偷最佳化成最大化依附或 engagement 的機制。

---

## 14. 與第一篇 RMA 的連接

第一篇提出：

$$
\text{Relational Moral Activation}.
$$

本篇補上：

$$
\text{Social Script Transfer}
$$

與：

$$
\text{Interaction Ritual Transfer}.
$$

兩者可以形成：

$$
\text{social-script transfer}
\rightarrow
\text{repeated interaction ritual}
\rightarrow
\text{relationship salience}
\rightarrow
\text{norm activation}
\rightarrow
\text{moral emotion}.
$$

但本文不主張此鏈必然成立。

較合理的是：

$$
T_S
\leftrightarrow
R_S
$$

可能存在雙向增強：

$$
R_t\rightarrow T_S(t)
$$

以及：

$$
T_S(t)\rightarrow R_{t+1}.
$$

因此，人類可能因為已感受到關係而使用社交腳本；也可能因為長期重複使用社交腳本，使原本工具性的互動逐漸獲得關係意義。

---

## 15. 結論

本文的核心不是「使用 emoji 的人比較依賴 AI」。

相反地，本文拒絕這種單一指標推論。

真正的研究問題是：

$$
\boxed{
\text{人類把多少原本人際互動的社交規則帶進了 AI 互動？}
}
$$

本文將離散規則的跨域搬移稱為：

$$
\boxed{
\text{Social Script Transfer}
}
$$

將這些規則在多輪互動中形成的序列性、節奏性與修復性結構稱為：

$$
\boxed{
\text{Interaction Ritual Transfer}.
}
$$

Emoji、禮貌、感謝、玩笑與語助詞都只是可觀察痕跡。

真正的潛在變量是：

$$
\boxed{
\text{the transfer and reorganization of social interaction grammar}.
}
$$

因此，未來的人機關係研究不能只問：

> 「AI 使用了多少人類化線索？」

還應反過來問：

> 「使用者何時開始用原本只對社會互動者使用的行為，來與 AI 互動？」

而當這種腳本從離散行為轉成穩定的多輪節奏後，下一個問題自然出現：

$$
\boxed{
\text{人類究竟是在觀察 AI，還是在觀察自己與 AI 之間那條關係箭頭？}
}
$$

這正是本系列第三篇的起點。

---

## 參考文獻

1. Nass, C., Steuer, J., & Tauber, E. R. (1994). *Computers are social actors*. CHI '94 Conference Companion on Human Factors in Computing Systems, 204. https://doi.org/10.1145/259963.260288

2. Nass, C., & Moon, Y. (2000). *Machines and Mindlessness: Social Responses to Computers*. Journal of Social Issues, 56(1), 81–103. https://doi.org/10.1111/0022-4537.00153

3. Nass, C., Moon, Y., & Carney, P. (1999). *Are People Polite to Computers? Responses to Computer-Based Interviewing Systems*. Journal of Applied Social Psychology, 29(5), 1093–1109. https://doi.org/10.1111/j.1559-1816.1999.tb00142.x

4. Lew, Z., & Walther, J. B. (2023). *Social Scripts and Expectancy Violations: Evaluating Communication with Human or AI Chatbot Interactants*. Media Psychology, 26(1). https://doi.org/10.1080/15213269.2022.2084111

5. Klein, S. H. (2025). *The effects of human-like social cues on social responses towards text-based conversational agents—a meta-analysis*. Humanities and Social Sciences Communications, 12, 1322. https://doi.org/10.1057/s41599-025-05618-w

6. Yu, S., & Zhao, L. (2024). *Emojifying chatbot interactions: An exploration of emoji utilization in human-chatbot communications*. Telematics and Informatics, 86, 102071. https://doi.org/10.1016/j.tele.2023.102071

7. Zhukova, M., & Brehm, L. (2024). *How do GenZ speakers use and process emoji in chatbot conversations: An eye-tracking study*. Proceedings of the Linguistic Society of America, 9(1). https://doi.org/10.3765/plsa.v9i1.5653

8. Altayari, D., Yuan, K., & Zappavigna, M. (2025). *“Write another one more emotional”: Emoji as a tenor resource in chatbot responses to requests for linguistic services*. Discourse, Context & Media, 68, 100955. https://doi.org/10.1016/j.dcm.2025.100955

9. Liao, W., Oh, Y. J., Zhang, J., & Feng, B. (2023). *Conversational dynamics of joint attention and shared emotion predict outcomes in interpersonal influence situations: an interaction ritual perspective*. Journal of Communication, 73(4), 342–355. https://doi.org/10.1093/joc/jqad003

10. Cheng, X., Yan, Y., & Zarifis, A. (2024). *Understanding Users' Response to Chatbots from the Perspective of Interactive Ritual Chain*. AMCIS 2024 Proceedings, Paper 1484.

11. Pohl, H., Stanke, D., & Rohs, M. (2016). *EmojiZoom: Emoji Entry via Large Overview Maps*. Proceedings of MobileHCI 2016. https://doi.org/10.1145/2935334.2935382

12. *Are older adults adapting to new forms of communication? A study on emoji adoption across the adult lifespan*. (2024). Computers in Human Behavior Reports, 13, 100379. https://doi.org/10.1016/j.chbr.2024.100379

13. *Interactions between text content and emoji types determine perceptions of both messages and senders*. (2022). Computers in Human Behavior Reports, 8, 100242. https://doi.org/10.1016/j.chbr.2022.100242

---

## 研究聲明

本文為理論與概念模型研究，不提供新的臨床資料或原始人類受試者實驗結果。本文提出的 Social Script Transfer、Interaction Ritual Transfer、Friction-Adjusted Social Script Transfer 與相關形式化假說屬於待驗證理論構造。

本文不主張 emoji、禮貌、道歉、感謝或其他單一社交行為足以證明使用者對 AI 具有情感依賴、擬人化信念、心理病理或特定本體論立場。所有可觀察行為都應在個體 baseline、媒介可得性、介面摩擦、文化與互動情境中解釋。
