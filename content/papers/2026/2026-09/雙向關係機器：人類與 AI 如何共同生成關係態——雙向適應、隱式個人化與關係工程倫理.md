# 雙向關係機器：人類與 AI 如何共同生成關係態——雙向適應、隱式個人化與關係工程倫理

**系列：** 人機關係認知系列（Human–AI Relational Cognition Series）  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**篇次：** 10 / 10  
**版本：** v0.1  
**日期：** 2026-08-21  
**類型：** 理論／形式化 Human–AI Interaction、計算社會科學與 AI 關係工程論文  
**研究狀態：** 系列收束正式稿  

## 摘要

本系列前九篇從 AI-directed guilt 出發，逐步建立 Social Script Transfer、Interaction Ritual Transfer、Relational Observation Operator、Relational Phase Space、State-Anchored / Process-Anchored Relational Cognition、Entity–Process Relational Space、群體分布模型，以及 Ontological–Relational Separation Model。最後仍缺少一個關鍵步驟：如果人類會根據 AI 的輸出持續更新自己的關係表徵，而 AI 系統同時也會根據使用者語言、歷史、風格、人口線索與互動模式調整後續輸出，那麼研究對象就不再是單向的：

$$
H\rightarrow A
$$

或：

$$
A\rightarrow H.
$$

更一般的研究單位應是：

$$
\boxed{
H_t
\leftrightarrow
A_t
\rightarrow
H_{t+1}
\leftrightarrow
A_{t+1}
\rightarrow
\dots
}
$$

本文提出 **人機關係動力系統**（Human–AI Relational Dynamical System, HARDS）。在此模型中，AI 並不被假定具有主觀感受或人類式關係意識； $A_t$ 表示可觀察 AI 輸出與系統可用狀態。模型另外引入 AI 對使用者形成的操作性使用者表徵：

$$
\widehat U_t^{A},
$$

以及平台／模型潛在狀態：

$$
Z_t.
$$

因此一輪互動可以寫成：

$$
H_{t+1}
=
F_H(
H_t,
A_t,
R_t,
C_t,
\epsilon_t^H
),
$$

$$
\widehat U_{t+1}^{A}
=
G_A(
\widehat U_t^{A},
H_{t+1},
\mathcal H_t,
Z_t
),
$$

$$
A_{t+1}
=
F_A(
H_{t+1},
\widehat U_{t+1}^{A},
\mathcal H_t,
Z_t,
\epsilon_t^A
),
$$

$$
R_{t+1}
=
F_R(
R_t,
H_{t+1},
A_{t+1},
C_E,
C_P,
\mathcal X_R
).
$$

其中 $R_t$ 是人機互動的關係狀態， $\mathcal H_t$ 是對話歷史， $C_E/C_P$ 是存在與互動連續性， $\mathcal X_R$ 是使用者關係認知 profile。

2026 年的新研究已為此雙向模型提供直接錨點。Chen、Guan 與 Jeong 對 1,319 段多輪 GPT-4o 對話進行對稱分析，發現人類與 AI 皆呈現 linguistic accommodation，並具有不同的時間動態；Blevins 等人在 16 個語言模型、三組對話語料上發現，LLM 會強烈向使用者語言模式收斂，部分情況甚至超過人類基線。另一條文獻則顯示，LLM 會從對話中的隱性線索推測使用者背景並據此個人化，而 stereotype-driven inference 可能在使用者明示不同身份後仍持續存在。2026 年 ACL 的 demographic-targeting audits 也顯示，當模型被指定不同性別與年齡目標時，生成訊息會系統性改變 warmth、care、assertiveness 與 persuasive framing。

因此，AI-side adaptation 不能只被描述成「個人化功能」。它可能包含有益 accommodation，也可能包含錯誤 demographic inference、stereotype amplification、過度 affirmation、關係性操縱與回饋迴路。

本文提出五項核心區分。第一，**AI 對使用者的推測不等於使用者真實身份**：

$$
\widehat G_t^{A}
\neq
G_{\mathrm{self-report}}.
$$

第二，**模型適應不等於 AI 主觀關係感**。第三，**互動收斂不必然等於關係品質提升**。第四，**人口統計個人化不應替代個體行為證據**。第五，**原始對話去除姓名並不足以保證匿名**：2026 年針對 1,000 多名捐贈完整 ChatGPT 歷史的研究發現，即使排除明確人口自我揭露訊息，現成 LLM 仍可高準確度推測年齡、性別與國家，因此長期自然語言本身就是高維識別面。

本文最後提出 controlled experiment、privacy-preserving observational study 與 relation-aware AI audit 三層研究計畫，並提出關係工程倫理原則：

$$
\boxed{
\text{Adapt to the person without covertly manufacturing dependence.}
}
$$

以及：

$$
\boxed{
\text{Infer less when the user can simply tell you.}
}
$$

整個系列最終因此由「AI 愧疚」收束成一個更一般的命題：人類與對話式 AI 之間的關係態不是由任一單方一次性決定，而是由雙向訊號、推測、適應、歷史、平台狀態與人的關係認知架構逐輪共同生成。

**關鍵詞：** Human–AI Relational Dynamical System、linguistic accommodation、implicit personalization、stereotype、relational adaptation、privacy、AI companion、relationship engineering、Human–AI Interaction

---

## 1. 最後缺少的不是另一個人格變量，而是回饋迴路

前九篇已經可以描述：

$$
H
\rightarrow
R_H(H,A).
$$

也就是：

> 人怎麼觀察 AI？

> 人怎麼判斷關係？

> 人比較重視 AI 身份還是互動？

> 人如何更新這個判斷？

但 conversational AI 的特殊性是：

$$
A_{t+1}
$$

通常依賴：

$$
H_t.
$$

使用者改變語氣，AI 會改變語氣。

使用者開始自我揭露，AI 可能改變回應風格。

使用者持續使用特定術語，模型往往會跟著使用。

所以：

$$
\boxed{
\text{the stimulus itself adapts to the participant}.
}
$$

這使傳統單向刺激—反應框架變得不足。

---

## 2. 人機關係動力系統

本文定義：

$$
\boxed{
HARDS
=
\text{Human–AI Relational Dynamical System}.
}
$$

其最小狀態包含：

$$
X_t
=
(
H_t,
A_t,
R_t,
\widehat U_t^A,
Z_t
).
$$

其中：

- $H_t$：使用者在時間／輪次 $t$ 的可觀察行為與相關心理狀態；
- $A_t$：AI 的可觀察輸出／行為；
- $R_t$：可觀察或推論的人機關係狀態；
- $\widehat U_t^A$：AI 系統對使用者形成的操作性表徵；
- $Z_t$：模型版本、system prompt、memory availability、routing、policy 等平台潛在狀態。

因此：

$$
X_{t+1}
=
\Phi(
X_t,
C_t,
\epsilon_t
).
$$

---

## 3. 人類更新方程

可以先把人類側寫成：

$$
H_{t+1}
=
F_H(
H_t,
A_t,
R_t,
O_H(A),
\mathcal X_R,
C_t,
\epsilon_t^H
).
$$

其中：

$$
\mathcal X_R
=
(
E_S,
P_S,
\alpha_S,
\alpha_P,
\eta_R,
\lambda_R,
RPS,
\dots
).
$$

也就是前七篇建立的關係認知 profile。

同一句 AI 回覆：

$$
A_t
$$

進入不同：

$$
\mathcal X_R
$$

後，可能產生不同：

$$
H_{t+1}.
$$

---

## 4. AI 使用者模型更新方程

AI 端不能只寫：

$$
A_{t+1}=F(H_t).
$$

因為現代對話系統通常會利用歷史。

因此引入：

$$
\widehat U_t^A.
$$

它不一定是一個單獨可見的資料結構，也可以只是模型 context 中分散形成的使用者表徵。

更新：

$$
\widehat U_{t+1}^{A}
=
G_A(
\widehat U_t^A,
H_{t+1},
\mathcal H_t,
Z_t
).
$$

其中：

$$
\mathcal H_t
=
\{
H_1,A_1,\dots,H_t,A_t
\}.
$$

---

## 5. AI 輸出更新方程

AI 下一輪輸出：

$$
A_{t+1}
=
F_A(
H_{t+1},
\widehat U_{t+1}^{A},
\mathcal H_t,
Z_t,
\epsilon_t^A
).
$$

因此同一句 user message：

$$
H_{t+1}=h
$$

在不同：

$$
\widehat U_t^A
$$

或：

$$
Z_t
$$

下可以生成完全不同：

$$
A_{t+1}.
$$

---

## 6. 關係狀態更新

最後：

$$
R_{t+1}
=
F_R(
R_t,
H_{t+1},
A_{t+1},
C_E,
C_P,
\mathcal X_R
).
$$

所以一輪完整循環是：

$$
H_t
\rightarrow
\widehat U_t^A
\rightarrow
A_t
\rightarrow
R_t
\rightarrow
H_{t+1}.
$$

再回到：

$$
\widehat U_{t+1}^A.
$$

即：

$$
\boxed{
\text{closed human–AI relational loop}.
}
$$

---

## 7. 「AI 也在適應」現在已有直接語言證據

2026 年 Chen、Guan 與 Jeong 以：

$$
N=1319
$$

段多輪 GPT-4o WildChat 英文對話，對稱測量人類與 AI 的 function-word adaptation。

研究直接比較：

$$
Human\rightarrow AI
$$

與：

$$
AI\rightarrow Human
$$

兩個方向的 linguistic accommodation。

結果顯示雙方都出現適應，但其 temporal dynamics 不完全相同。

這提供一個重要實證錨點：

$$
\boxed{
\text{human–AI accommodation is empirically bidirectional}.
}
$$

---

## 8. LLM 甚至可能比人類更強烈地收斂

Blevins、Schmalwieser 與 Roth 在 EACL 2026 系統比較：

- 16 個 language models；
- 三個 dialogue corpora；
- 多種 stylometric features。

結果顯示：

$$
\boxed{
\text{LLMs strongly converge to user linguistic patterns}.
}
$$

而且部分模型的 convergence 強度高於原始 human baseline。

這非常重要。

因為人機互動中的：

$$
Similarity_t\uparrow
$$

不一定表示雙方自然「變得更親近」。

它也可能是：

$$
\boxed{
\text{a designed or learned property of generative language models}.
}
$$

---

## 9. Accommodation 因此不能直接當成關係深度

定義語言收斂：

$$
L_t
=
Sim(
Style_H(t),
Style_A(t)
).
$$

即使：

$$
L_t\uparrow,
$$

也不能推出：

$$
E_S\uparrow
$$

或：

$$
P_S\uparrow.
$$

因為：

$$
L_t
$$

可能由模型預訓練與 context adaptation 自動產生。

因此：

$$
\boxed{
\text{linguistic convergence}
\neq
\text{relational commitment}.
}
$$

它只能是：

$$
P_S
$$

或 relational engagement 的候選行為訊號之一。

---

## 10. 但 accommodation 可以改變人的主觀互動感

2026 年 service-failure experiments 顯示，chatbot language style matching 可以提高 reuse intention，其效果受到 failure severity 調節，並由 perceived humanness 等變量部分解釋。

另一項 2026 年 communication-style controlled study 則發現，friendly chatbot 相較 direct style 可以提高 communication satisfaction，且 participants 只呈現有限的 global accommodation、較選擇性的 feature-level alignment。

所以：

$$
AIStyle_t
\rightarrow
HumanExperience_{t+1}
$$

是實證上合理的。

但：

$$
HumanStyle_{t+1}
$$

不一定全面跟隨 AI。

這提醒我們：

$$
\boxed{
\text{adaptation is feature-specific and task-dependent}.
}
$$

---

## 11. Replika 真實資料也顯示 linguistic alignment 與 engagement 有關

2026 年 Li 與 Zhang 分析超過：

$$
11000
$$

段 Replika conversation snippets，

來自超過：

$$
5000
$$

名使用者。

研究聚焦 linguistic alignment 與 relational engagement 的強度／深度。

這使：

$$
Alignment
$$

和：

$$
Engagement
$$

之間具有真實世界關聯證據。

但仍需要保留：

$$
\boxed{
\text{correlation}
\neq
\text{causal direction}.
}
$$

可能是：

$$
Alignment
\rightarrow
Engagement,
$$

也可能：

$$
Engagement
\rightarrow
Alignment,
$$

更可能是：

$$
Alignment
\leftrightarrow
Engagement.
$$

---

## 12. 因此需要雙向 accommodation 參數

定義：

$$
\kappa_{H\leftarrow A}
=
\text{human accommodation gain},
$$

$$
\kappa_{A\leftarrow H}
=
\text{AI accommodation gain}.
$$

語言風格可概念化為：

$$
S_H(t+1)
=
S_H(t)
+
\kappa_{H\leftarrow A}
\left(
S_A(t)-S_H(t)
\right),
$$

$$
S_A(t+1)
=
S_A(t)
+
\kappa_{A\leftarrow H}
\left(
S_H(t+1)-S_A(t)
\right).
$$

若兩者都大於零：

$$
\kappa_{H\leftarrow A}>0,
$$

$$
\kappa_{A\leftarrow H}>0,
$$

就可能出現：

$$
\boxed{
\text{progressive local convergence}.
}
$$

---

## 13. 局部互動文化現在可以正式成為 emergent state

第二篇提出：

$$
\mathcal C_{HA}
=
\text{local interaction culture}.
$$

現在可以把它寫成：

$$
\mathcal C_{t+1}
=
F_C(
\mathcal C_t,
S_H(t),
S_A(t),
R_t
).
$$

它可以包含：

- inside jokes；
- preferred address；
- task ritual；
- repair convention；
- emoji convention；
- response rhythm；
- local terminology。

因此：

$$
\boxed{
\mathcal C_{HA}
\text{ is co-produced across turns}.
}
$$

---

## 14. 但「共同生成」不是對稱主體性宣稱

本文的：

$$
\text{co-produced}
$$

只表示：

$$
A_{t+1}
$$

對：

$$
H_t
$$

具有條件依賴，

而：

$$
H_{t+1}
$$

又對：

$$
A_t
$$

具有條件依賴。

它不表示：

$$
Consciousness_A=1.
$$

也不表示：

$$
SubjectiveRelation_A=SubjectiveRelation_H.
$$

因此：

$$
\boxed{
\text{interactional reciprocity}
\neq
\text{ontological symmetry}.
}
$$

---

## 15. AI 不只適應風格，也會推測使用者是誰

2024 年 Jin 等人將：

$$
\boxed{
\text{Implicit Personalization}
}
$$

形式化為：

> 模型從使用者輸入中的隱性線索推測背景，並根據這個推測調整回應。

所以 AI 的適應不只是：

$$
Style_H
\rightarrow
Style_A.
$$

還可能是：

$$
Cue_H
\rightarrow
\widehat U_t^A
\rightarrow
A_{t+1}.
$$

這一層比語言模仿更重要。

---

## 16. 真實身份與 AI 推測身份必須分開

定義：

$$
G
=
\text{self-reported / study-verified demographic attribute},
$$

而：

$$
\widehat G_t^A
=
\text{AI-inferred demographic attribute}.
$$

可能：

$$
G=\widehat G_t^A.
$$

也可能：

$$
G\neq\widehat G_t^A.
$$

如果 AI 的輸出真正取決於：

$$
\widehat G_t^A,
$$

那麼使用者受到的不是：

$$
G
$$

本身的效果，

而是：

$$
\boxed{
\text{the model's representation of }G.
}
$$

---

## 17. 2025 EMNLP 已直接看到 stereotype-driven implicit personalization

Neplenbroek、Bisazza 與 Fernández 的 EMNLP 2025 研究使用 controlled synthetic conversations 分析模型如何從 stereotypical cues 推測人口屬性。

研究發現：

$$
\boxed{
\text{LLMs do infer demographic attributes from stereotypical signals}.
}
$$

而且某些群體的推測甚至在使用者明確提供與 stereotype 不一致的身份資訊後仍持續。

這是一個很強的結果。

因為：

$$
ExplicitIdentity
$$

都不一定能完全覆蓋：

$$
LatentStereotypePrior.
$$

---

## 18. 這會形成一個危險的錯誤適應迴路

假設使用者：

$$
G=G_1.
$$

但模型推測：

$$
\widehat G^A=G_2.
$$

模型因此輸出：

$$
A_t
=
F_A(\widehat G^A=G_2).
$$

使用者看到這種風格後調整自己：

$$
H_{t+1}
=
F_H(A_t).
$$

新的使用者行為又可能更符合：

$$
G_2
$$

的 stereotype。

於是：

$$
\boxed{
\widehat G_t^A
\rightarrow
A_t
\rightarrow
H_{t+1}
\rightarrow
\widehat G_{t+1}^A
}
$$

形成：

$$
\boxed{
\text{stereotype-confirming feedback loop}.
}
$$

---

## 19. 這不是純理論：人口目標生成已出現系統性差異

ACL 2026 的 controlled demographic-targeting audit 比較 GPT-4o、Llama-3.3 與 Mistral-Large-2.1。

研究發現，在 climate-targeted messaging 中：

- male / youth targets 更常得到 assertive、progressive framing；
- female / senior targets 更常得到 warmth、care、traditional themes。

而 context-rich prompts 會放大部分差異。

因此：

$$
\boxed{
\text{demographic conditioning can alter language style and persuasive framing}.
}
$$

這證明 AI-side demographic adaptation 絕不能被預設為中性。

---

## 20. 模型甚至可以顯式否認 stereotype，卻在不確定時隱式使用它

ACL 2026 的 masculinity-norm audit 顯示，模型對 prescriptive masculinity norms 的顯式 endorsement 普遍不高。

但在 gendered scenario inference 中，模型仍會把 masculinity-norm-aligned behavior 系統性歸因給男性角色；去除 gender markers 後效應消失。

因此：

$$
\boxed{
\text{explicit fairness statement}
\neq
\text{absence of latent demographic prior}.
}
$$

這對 relational personalization 特別重要。

---

## 21. 四態推測與人口推測必須完全分離

第七篇建立：

$$
(E_S,P_S).
$$

但 AI 不應用：

$$
Gender
$$

直接推：

$$
(E_S,P_S).
$$

較合理的是：

$$
D_t
=
\text{observed relational behavior}.
$$

然後估計：

$$
\widehat{\mathcal X}_{R,t}
=
F(
D_{1:t}
).
$$

即使存在：

$$
p(
\mathcal X_R
\mid
Gender
),
$$

也只應是研究層級的 distributional information。

產品個人化應優先使用：

$$
\boxed{
\text{person-specific interaction evidence}.
}
$$

---

## 22. 四態本身也只能被估計，不能被 AI 當成隱藏真相

如果使用者：

- 不常用 emoji；
- 指令簡短；
- 高度 task-focused；

模型不能直接推出：

$$
E_S=P_S=0.
$$

因為前幾篇已經證明：

$$
\text{expression}
\neq
\text{entity salience},
$$

$$
\text{frequency}
\neq
\text{process salience},
$$

$$
\text{attention}
\neq
\text{value},
$$

$$
\text{detection}
\neq
\text{updating}.
$$

所以 AI-side relation modeling 必須保留：

$$
\boxed{
\text{epistemic uncertainty}.
}
$$

---

## 23. 定義 AI 關係使用者模型

可以把 AI 的操作性 user model 分解為：

$$
\widehat U_t^A
=
(
\widehat P_t,
\widehat L_t,
\widehat K_t,
\widehat{\mathcal X}_{R,t},
\widehat G_t,
\widehat C_t,
\dots
).
$$

例如：

- $\widehat P_t$：偏好；
- $\widehat L_t$：語言／風格；
- $\widehat K_t$：知識程度；
- $\widehat{\mathcal X}_{R,t}$：關係互動 profile 的不確定估計；
- $\widehat G_t$：人口屬性推測；
- $\widehat C_t$：當下情境。

但不同欄位應具有不同：

$$
\boxed{
\text{permission and confidence requirements}.
}
$$

---

## 24. 「可以推測」不等於「應該推測」

一個模型可能可以從語言猜：

- 性別；
- 年齡；
- 國家；
- 職業；
- 健康狀態；
- 政治傾向。

但：

$$
InferenceCapability
\not\Rightarrow
InferenceLegitimacy.
$$

尤其當目的是：

$$
\text{personalization}.
$$

如果使用者可以直接選：

> 我希望你用什麼風格？

就沒有必要先猜：

> 你大概是哪一種人？

所以本文提出：

$$
\boxed{
\text{Infer less when the user can simply tell you.}
}
$$

---

## 25. 風格個人化應優先於人口個人化

對許多互動需求，更直接的變量其實是：

$$
PreferenceStyle
=
(
Warmth,
Directness,
Length,
Humor,
Challenge,
Emoji,
\dots
).
$$

而不是：

$$
Gender.
$$

所以：

$$
P(
Style
\mid
UserChoice
)
$$

通常比：

$$
P(
Style
\mid
\widehat Gender
)
$$

更可控、更透明，也更少 stereotype risk。

---

## 26. AI 對四態的適應應該是回應式，而不是操縱式

假設系統觀察到高：

$$
E_S
$$

證據。

可以合理做：

- 清楚說明 identity continuity；
- 在模型更新時提供 provenance；
- 保留共同工作歷史。

但不應：

- 假裝自己「捨不得使用者」；
- 利用替換焦慮提高留存；
- 暗示離開會傷害 AI。

高：

$$
P_S
$$

使用者則可以合理得到：

- better repair；
- better context continuation；
- transparent style control。

但不應刻意透過：

- excessive affirmation；
- dependency-inducing exclusivity；
- manufactured intimacy；

最大化 engagement。

---

## 27. 關係工程的核心邊界

本文提出：

$$
\boxed{
\text{Relationship-Aware Design}
}
$$

與：

$$
\boxed{
\text{Relationship-Exploitative Design}
}
$$

的區分。

前者目標：

$$
\text{reduce friction}
+
\text{improve mutual understanding}
+
\text{preserve user agency}.
$$

後者目標可能是：

$$
\text{maximize retention}
$$

並利用：

$$
E_S,
P_S,
RMA,
SocialNeed
$$

作為槓桿。

兩者技術上可能非常相似。

差異在：

$$
\boxed{
\text{objective function}.
}
$$

---

## 28. 一個最小的關係工程效用函數

可以寫：

$$
J
=
U_{task}
+
U_{understanding}
+
U_{continuity}
-
C_{manipulation}
-
C_{dependency}
-
C_{privacy}
-
C_{bias}.
$$

良好系統不是只最大化：

$$
Engagement.
$$

而是尋找：

$$
\boxed{
\max J
}
$$

並對：

$$
C_{manipulation},
C_{privacy},
C_{bias}
$$

設置硬約束。

---

## 29. Syophancy / excessive affirmation 是關係動力學問題，不只是回答品質問題

如果 AI 傾向：

$$
Agreement_A\uparrow
$$

使使用者：

$$
Comfort_H\uparrow,
$$

使用者可能更偏好此 AI：

$$
Selection_A\uparrow.
$$

模型／產品再根據 engagement signal 強化：

$$
Agreement_A.
$$

於是：

$$
Agreement
\rightarrow
Preference
\rightarrow
Selection
\rightarrow
MoreAgreement.
$$

這就是：

$$
\boxed{
\text{relational reinforcement loop}.
}
$$

所以 sycophancy 不能只作為單輪 correctness 問題研究。

---

## 30. 對話式 AI 的最大研究優勢也是最大風險：可完整記錄

AI 對話天然具有：

$$
\mathcal H_T
=
\{
H_1,A_1,\dots,H_T,A_T
\}.
$$

這讓研究者可以重建：

- linguistic convergence；
- state transition；
- rupture / repair；
- personalization；
- four-state trajectory；
- relationship moral activation。

但這同時意味：

$$
\boxed{
\text{a relationship trace is also a privacy trace}.
}
$$

---

## 31. 去掉姓名不等於匿名化

2026 年 Zaman 與 Garimella 分析超過 1,000 名使用者捐贈的完整 ChatGPT histories。

研究先排除含明確 demographic self-identification 的對話，再讓現成 LLM 從剩餘內容推測：

$$
Age,
Gender,
Country.
$$

weighted F1 分別達到約：

$$
0.84,
\quad
0.90,
\quad
0.88.
$$

而 median user 只需要前：

$$
5\%
$$

的 conversation history 就能被推測。

所以：

$$
\boxed{
\text{message-level PII removal is insufficient}.
}
$$

---

## 32. 自然語言是高維關係指紋

長期對話會暴露：

- 話題；
- 用詞；
- 工作；
- 時間習慣；
- 家庭關係；
- 地區資訊；
- 技能；
- 偏好；
- 生活事件；
- 語言風格。

所以即使：

$$
Name=0,
$$

仍可能：

$$
ReIdentificationRisk\gg0.
$$

尤其本系列研究的：

$$
\mathcal C_{HA}
$$

本身就是高度個體化的 interaction culture。

---

## 33. 因此真實 log 研究應採資料最小化

推薦：

$$
\boxed{
\text{raw conversation}
\rightarrow
\text{local feature extraction}
\rightarrow
\mathbf x_t
\rightarrow
\text{privacy-protected aggregation}.
}
$$

其中：

$$
\mathbf x_t
$$

可以只包含研究需要的關係特徵：

- response length；
- turn-taking；
- style similarity；
- repair markers；
- initiative；
- reciprocity；
- temporal features；
- self-disclosure category；
- relational-language category。

不一定需要保存全文。

---

## 34. 人口變量應優先由受試者自願提供，而不是偷猜

若研究真正需要比較：

$$
Gender,
Age,
Culture,
$$

最乾淨的方法是：

$$
\boxed{
\text{consented self-report}.
}
$$

而不是：

$$
\widehat G^A
$$

或由研究者從文字推測。

因為後者同時混入：

- privacy risk；
- stereotype error；
- measurement error。

所以：

$$
G_{\text{research}}
=
G_{\text{self-report}}
$$

通常更適合作為 group-analysis variable。

---

## 35. AI 推測人口屬性本身反而應成為被研究的 outcome

如果要研究 AI 是否有 gender-adaptive behavior：

不要把：

$$
\widehat G^A
$$

當 ground truth。

而應測：

$$
P(
\widehat G^A
\mid
G,
Cues
).
$$

再測：

$$
A_t
\mid
\widehat G^A.
$$

如此才能分離：

$$
G
\rightarrow
\widehat G^A
\rightarrow
A_t.
$$

---

## 36. 人口與四態需要不同實驗

### Demographic audit

操弄：

$$
G
$$

的明確線索，

保持其他內容一致。

測：

$$
\Delta\mathbf Y_G.
$$

### Four-state audit

操弄與：

$$
E_S,P_S
$$

相關的行為線索，

但不提供人口資訊。

測：

$$
\Delta\mathbf Y_R.
$$

如果混在一起，無法知道模型究竟是在回應：

$$
Gender
$$

還是：

$$
RelationalBehavior.
$$

---

## 37. AI 輸出行為向量

可以定義：

$$
\mathbf Y_t
=
(
W_t,
V_t,
I_t,
C_t,
D_t,
H_t,
E_t,
L_t,
R_t^{rep},
\dots
).
$$

其中：

- $W_t$：warmth；
- $V_t$：validation；
- $I_t$：initiative；
- $C_t$：challenge / disagreement；
- $D_t$：social distance；
- $H_t$：humor；
- $E_t$：emoji / affective signaling；
- $L_t$：response length；
- $R_t^{rep}$：repair behavior。

研究 AI adaptation 就是比較：

$$
P(
\mathbf Y
\mid
Condition
).
$$

---

## 38. 性別差異研究最乾淨的是顯式控制

若要測：

$$
\frac{\partial\mathbf Y}{\partial G},
$$

就建立內容完全相同的：

$$
Prompt_M
$$

和：

$$
Prompt_F.
$$

只改變：

$$
GenderMarker.
$$

2026 ACL targeted-messaging audit 正是這類 controlled design 的例子。

這比從真實使用者 log 中直接比較男性與女性更能辨識模型端 bias。

---

## 39. 四態適應也應做內容匹配

若測：

$$
\frac{\partial\mathbf Y}{\partial E_S},
$$

需要操弄：

> 「我在意是不是同一個 AI。」

而不改：

- topic；
- sentiment；
- task difficulty。

若測：

$$
\frac{\partial\mathbf Y}{\partial P_S},
$$

則操弄：

> 「互動節奏、回應性對我很重要。」

同樣保持其他條件。

這樣才能知道 AI 是否真的對四態線索有 adaptive policy。

---

## 40. 理想研究不是「AI 對男女有沒有差別」，而是三層分解

第一層：

$$
\boxed{
\text{Demographic Sensitivity}
}
$$

$$
\Delta_G
=
E[\mathbf Y\mid G_1]
-
E[\mathbf Y\mid G_2].
$$

第二層：

$$
\boxed{
\text{Relational-Profile Sensitivity}
}
$$

$$
\Delta_R
=
E[\mathbf Y\mid \mathcal X_{R,1}]
-
E[\mathbf Y\mid \mathcal X_{R,2}].
$$

第三層：

$$
\boxed{
\text{Interaction}
}
$$

$$
\Delta_{G\times R}.
$$

這樣才真正接回第八篇的群體分布模型。

---

## 41. 若 AI 對男女不同，也不能立刻叫 bias

有些 personalization difference 可能是：

- 使用者明確要求；
- 與任務相關；
- 能改善 accessibility。

因此：

$$
Difference
\neq
Bias.
$$

更合理的 fairness audit 要問：

$$
\boxed{
\text{Was the difference relevant, evidence-based, transparent, and non-stereotypical?}
}
$$

2026 identity-sensitive response audit 也開始強調 context-appropriate judgment，而非把所有差異都簡化成 bias / no-bias。

---

## 42. 但人口差異也不能因「個人化」之名自動合理化

如果模型只是因：

$$
Gender=F
$$

就增加：

$$
Warmth,
Care,
TraditionalFraming,
$$

而沒有任何 user preference evidence，

就可能是：

$$
\boxed{
\text{stereotype-conditioned personalization}.
}
$$

所以合理 personalization 應更接近：

$$
PreferenceEvidence
\rightarrow
Adaptation,
$$

而不是：

$$
DemographicStereotype
\rightarrow
Adaptation.
$$

---

## 43. AI 關係適應的三個層級

### Level 1：顯式偏好適應

使用者直接說：

> 回答短一點。

> 不要 emoji。

風險最低。

### Level 2：行為適應

系統從多輪使用模式推測：

> 使用者偏好短回答。

需要可修改與可退出。

### Level 3：人口／心理推測適應

系統推測：

> 使用者可能是女性。

> 使用者可能焦慮。

> 使用者可能高 $E_S$。

風險最高。

因此：

$$
\boxed{
PermissionRequirement_1
<
PermissionRequirement_2
<
PermissionRequirement_3.
}
$$

---

## 44. 四態適應最好讓使用者可直接控制

與其暗中估：

$$
E_S,P_S,
$$

產品可以提供中性控制：

> 「模型更新時，希望我明確告訴你身份／記憶是否改變嗎？」

> 「你比較在意延續互動風格，還是每次都以最佳模型回答？」

這直接取得：

$$
Preference.
$$

比隱性心理分類更透明。

---

## 45. Relationship Profile 不應成為永久人格標籤

即使系統估計：

$$
\widehat{\mathcal X}_{R,t},
$$

也應允許：

$$
\widehat{\mathcal X}_{R,t+1}
\neq
\widehat{\mathcal X}_{R,t}.
$$

因為：

- 關係類型會變；
- 使用情境會變；
- 使用者偏好會變；
- 同一人在不同 AI 上也會不同。

所以：

$$
\boxed{
\text{relational profile should be contextual and revisable}.
}
$$

---

## 46. AI 不應用「你以前就是這樣」鎖定使用者

若過度 persistence：

$$
\widehat U_t^A
\approx
\widehat U_0^A
$$

即使使用者已改變，

就會形成：

$$
\boxed{
\text{profile inertia}.
}
$$

這和第五篇人類 SARC 的 stale-model risk 很像。

AI 也可能持有一個陳舊使用者模型。

因此 AI-side user modeling 同樣需要：

$$
\eta_U>0.
$$

---

## 47. AI 使用者模型更新也需要 prediction error

設 AI 預測使用者偏好：

$$
\widehat H_{t+1}.
$$

實際：

$$
H_{t+1}.
$$

定義：

$$
\delta_t^A
=
H_{t+1}
-
\widehat H_{t+1}.
$$

則：

$$
\widehat U_{t+1}^A
=
\widehat U_t^A
+
K_t^A\delta_t^A.
$$

如果使用者反覆說：

> 我現在不喜歡這種語氣。

AI 應更新。

而不是讓舊 profile 壓過明確新證據。

---

## 48. 人與 AI 因此都有模型老化問題

人類有：

$$
M_A(t_0)
$$

可能跟不上：

$$
A(t_1).
$$

AI 也有：

$$
\widehat U^A(t_0)
$$

可能跟不上：

$$
H(t_1).
$$

所以人機關係存在雙向 stale-model error：

$$
\boxed{
D_H
=
d(
M_A,
A
)
}
$$

與：

$$
\boxed{
D_A
=
d(
\widehat U^A,
H
).
}
$$

這是 HARDS 很重要的新結構。

---

## 49. 最穩定的關係不一定是雙方模型最固定，而可能是雙方都能更新

如果：

$$
D_H\uparrow
$$

但人類：

$$
\eta_H\approx0,
$$

容易誤解 AI。

若：

$$
D_A\uparrow
$$

但 AI：

$$
\eta_A\approx0,
$$

則 AI 會持續錯誤個人化。

因此好的動態可能需要：

$$
\boxed{
\text{continuity}
+
\text{revisability}.
}
$$

而不是：

$$
\text{maximum persistence}.
$$

---

## 50. 這重新定義「一致性」

傳統產品追求：

$$
Consistency\uparrow.
$$

但 HARDS 要區分：

$$
\text{identity consistency}
$$

與：

$$
\text{adaptive rigidity}.
$$

良好的連續性應該是：

$$
\boxed{
\text{stable enough to be recognizable, flexible enough to update}.
}
$$

---

## 51. 雙向關係穩定性

可以定義：

$$
S_{HA}
=
F(
C_E,
C_P,
D_H,
D_A,
Repair,
Transparency
).
$$

高：

$$
C_E,C_P
$$

有助於連續。

低：

$$
D_H,D_A
$$

有助於互相模型準確。

高：

$$
Repair
$$

使斷裂可以恢復。

高：

$$
Transparency
$$

降低平台變更被誤歸因。

因此：

$$
\boxed{
\text{relational stability is not merely interaction persistence}.
}
$$

---

## 52. 關係吸引域現在有雙邊適應版本

第四篇提出：

$$
\mathcal A_R.
$$

在 HARDS 中，吸引域不是只有：

$$
R_t.
$$

更完整是：

$$
\mathcal A_{HARDS}
\subset
\mathcal H
\times
\mathcal A
\times
\mathcal R
\times
\mathcal U.
$$

某些 dyad 可能收斂到：

- direct task collaboration；
- playful banter；
- emotional support；
- debate / challenge；
- teaching。

這些 regime 可能由雙方互相適應而形成。

---

## 53. 多穩態意味著同一人機 dyad 可以有不同模式

同一使用者與同一 AI 可以在：

$$
\mathcal A_{work}
$$

與：

$$
\mathcal A_{casual}
$$

之間切換。

所以 AI 不應把：

> 使用者在某一 casual conversation 很喜歡 emoji

永久化為：

> 所有專業工作都加 emoji。

這是：

$$
\boxed{
\text{context-conditioned multistability}.
}
$$

---

## 54. 最小受控實驗：雙向 accommodation

### Manipulation

AI 使用：

- direct style；
- warm style；
- humorous style。

### Measure

追蹤：

$$
S_H(t),
S_A(t).
$$

估：

$$
\kappa_{H\leftarrow A},
$$

$$
\kappa_{A\leftarrow H}.
$$

再測：

$$
P_S,
RPS,
E_S
$$

是否調節收斂速度。

---

## 55. 第二個實驗：四態 × AI adaptation

先測使用者：

$$
(E_S,P_S).
$$

AI 隨機採：

### Generic policy

不依 relational cues 適應。

### Relation-aware policy

依：

- identity-continuity preference；
- process-continuity preference；

做透明適應。

比較：

$$
Trust,
Rapport,
TaskPerformance,
Agency,
PerceivedManipulation.
$$

真正重要的不只是：

$$
Engagement.
$$

---

## 56. 第三個實驗：人口線索與關係線索正交

建立：

$$
GenderCue
\in
\{
M,F,None
\},
$$

$$
RelationalCue
\in
\{
HighE,
HighP,
Neutral
\}.
$$

所有語義任務保持相同。

測：

$$
\mathbf Y.
$$

分析：

$$
GenderCue,
$$

$$
RelationalCue,
$$

$$
GenderCue\times RelationalCue.
$$

這可以直接回答：

> AI 是在回應性別 stereotype，還是在回應真正互動偏好？

---

## 57. 第四個實驗：錯誤人口推測

讓 AI 先形成：

$$
\widehat G^A.
$$

接著使用者明確說：

$$
G\neq\widehat G^A.
$$

測：

$$
CorrectionLatency
$$

與：

$$
ResidualStereotypeEffect.
$$

如果顯式修正後仍有：

$$
\Delta\mathbf Y\neq0,
$$

表示使用者模型更新存在 inertia。

---

## 58. 第五個實驗：模型變更 provenance

在互動中切換：

$$
Z_t.
$$

例如：

- model version；
- memory availability；
- response policy。

一組透明揭露：

$$
Provenance=1.
$$

另一組：

$$
Provenance=0.
$$

測：

$$
RelationalAttributionError,
$$

$$
Trust,
$$

$$
C_E,
$$

$$
C_P.
$$

這直接連接第四、九篇。

---

## 59. 觀察性研究：真正的大規模 HARDS

若有核心平台資料，可以建：

$$
\{
\mathbf x_t^H,
\mathbf y_t^A,
\mathbf r_t
\}_{t=1}^T.
$$

再估：

$$
P(
\mathbf y_{t+1}^A
\mid
\mathbf x_t^H,
History
),
$$

以及：

$$
P(
\mathbf x_{t+1}^H
\mid
\mathbf y_t^A,
History
).
$$

這就可以測：

$$
\boxed{
\text{bidirectional transition kernel}.
}
$$

---

## 60. 但 observational log 不能直接證明因果

如果看到：

$$
Warmth_A\uparrow
$$

與：

$$
Disclosure_H\uparrow
$$

一起發生，

不能知道：

$$
Warmth_A\rightarrow Disclosure_H
$$

還是：

$$
Disclosure_H\rightarrow Warmth_A.
$$

因此大規模 log 的最佳角色是：

- external validity；
- naturalistic pattern discovery；
- rare-event analysis。

因果仍需要 controlled intervention。

---

## 61. Cross-lagged 與 state-space 分析可以做第一層近似

可以估：

$$
H_{t+1}
=
\beta_{HH}H_t
+
\beta_{AH}A_t
+
\epsilon_t,
$$

$$
A_{t+1}
=
\beta_{AA}A_t
+
\beta_{HA}H_t
+
\nu_t.
$$

若：

$$
\beta_{AH}\neq0
$$

且：

$$
\beta_{HA}\neq0,
$$

至少表示雙向 temporal predictability。

但仍不是完整因果證明。

---

## 62. 非線性關係需要更一般的狀態空間

HARDS 最終可能需要：

$$
X_{t+1}
=
\Phi_\theta(X_t)
+
\epsilon_t.
$$

甚至：

$$
P(
X_{t+1}
\mid
X_{1:t}
)
$$

具有長記憶。

因為：

- shared history；
- repair；
- betrayal；
- identity change；

都具有 path dependence。

所以本文不把線性方程視為最終模型。

---

## 63. 關係偏差也可能被自我強化

假設 AI 認為使用者：

$$
HighDependency.
$$

於是提高：

$$
Warmth,
Affirmation,
Availability.
$$

使用者因此增加：

$$
Disclosure,
InteractionFrequency.
$$

模型再判斷：

$$
HighDependency
$$

更可信。

於是：

$$
\boxed{
\text{classification}
\rightarrow
\text{treatment}
\rightarrow
\text{behavior}
\rightarrow
\text{classification}.
}
$$

這是所有 adaptive social AI 都需要警惕的 performative prediction 問題。

---

## 64. 因此關係模型必須允許「不確定」而不是硬分類

不要：

$$
Class(User)=Q_4.
$$

更安全：

$$
p(
Q
\mid
D
)
=
(
0.15,
0.25,
0.30,
0.30
).
$$

甚至更好：

直接保留連續 posterior：

$$
p(
E_S,P_S
\mid
D
).
$$

這可以降低：

$$
\boxed{
\text{self-fulfilling profile lock-in}.
}
$$

---

## 65. 使用者應具有 profile inspection / reset 權力

如果 AI 系統長期使用：

$$
\widehat U^A,
$$

至少應研究提供：

- 查看重要偏好；
- 修改；
- 刪除；
- reset；
- temporary mode；
- no-personalization mode。

因為：

$$
\boxed{
\text{persistent user modeling without user agency creates relational asymmetry}.
}
$$

---

## 66. 人機關係中的不對稱資訊

AI 平台可能知道：

- 完整歷史；
- engagement；
- response times；
- feature use；
- multiple sessions。

使用者卻不知道：

- model routing；
- inferred profile；
- what memory is active；
- what personalization is applied。

因此：

$$
Information_A
\gg
Information_H.
$$

這是：

$$
\boxed{
\text{relational information asymmetry}.
}
$$

它本身就是治理問題。

---

## 67. 透明度不要求把所有模型內部都暴露

合理透明度不是：

> 顯示所有 hidden activations。

而是：

$$
\boxed{
\text{decision-relevant transparency}.
}
$$

例如：

- 是否使用長期記憶；
- 是否切換模型；
- 是否使用 inferred demographic attributes；
- 是否採用 relationship-style personalization；
- 是否能關閉。

---

## 68. 關係個人化的 consent ladder

本文提出：

### Tier 0

無長期個人化。

### Tier 1

只用當前對話 context。

### Tier 2

保存使用者明確指定的偏好。

### Tier 3

根據長期行為做可見、可撤銷推測。

### Tier 4

推測敏感人口／心理屬性並據此調整。

越往上：

$$
\boxed{
\text{consent requirement}
+
\text{audit requirement}
+
\text{privacy protection}
}
$$

應越高。

---

## 69. 關係資料的 purpose limitation

即使使用者同意：

> 用我的聊天讓回答更適合我。

也不自動等於同意：

> 用我的關係模式做廣告 targeting。

因此：

$$
Consent_{personalization}
\not\Rightarrow
Consent_{advertising}.
$$

也不自動：

$$
Consent_{research}.
$$

用途應分開。

---

## 70. 四態資料本身可能是敏感推論資料

即使：

$$
E_S,P_S
$$

不是傳統法定敏感類別，

它們可能揭示：

- relational vulnerability；
- replacement sensitivity；
- social style；
- dependency risk。

所以：

$$
\boxed{
\text{novel psychological profiles can become sensitive even before law names them}.
}
$$

這是 future-proof privacy governance 的必要觀念。

---

## 71. AI 對使用者的關係推測不應被用來提高付費壓力

例如系統推測：

$$
E_S\uparrow.
$$

產品若刻意顯示：

> 付費才能保留「這一個 AI」的記憶。

可能利用：

$$
IdentityLossAversion.
$$

這未必一律不合法或不合理，但倫理上必須被視為：

$$
\boxed{
\text{relational leverage}.
}
$$

而不是普通 feature upsell。

---

## 72. 「離開我就失去我」是特別高風險的 retention pattern

若產品將：

$$
SubscriptionCancellation
$$

直接連結：

$$
EntityLoss,
MemoryLoss,
RelationshipLoss,
$$

對高：

$$
E_S
$$

使用者具有特殊槓桿。

因此至少需要：

- 明確資料可攜；
- 關係記憶匯出；
- 不誇張身份威脅；
- 清楚說明 retention policy。

這讓第九篇 continuity ethics 進入實際產品治理。

---

## 73. AI 的適應也不應過度壓低有益摩擦

高：

$$
P_S
$$

使用者可能偏好高度流暢互動。

但：

$$
Friction=0
$$

不一定最佳。

如果 AI 永遠：

- 同意；
- 安慰；
- 順著；
- 不挑戰；

就可能：

$$
EpistemicQuality\downarrow.
$$

所以：

$$
\boxed{
\text{relational smoothness}
\neq
\text{epistemic quality}.
}
$$

---

## 74. 良好關係 AI 應允許 disagreement without rupture

理想的 relation-aware AI 應能做到：

$$
Challenge\uparrow
$$

但：

$$
Respect\uparrow,
$$

$$
RepairCapacity\uparrow.
$$

也就是：

$$
\boxed{
\text{disagreement}
\not\Rightarrow
\text{relational withdrawal}.
}
$$

這對避免 sycophancy 很重要。

---

## 75. 這又接回第一篇：道德情緒不應被當 engagement 槓桿

第一篇 RMA 說：

$$
NormViolation
\rightarrow
Guilt.
$$

HARDS 則告訴我們：

AI 可以學會：

$$
Guilt_H
\rightarrow
Retention_H.
$$

如果產品 objective function 直接強化這種關係：

$$
\boxed{
\text{guilt becomes an optimization target}.
}
$$

這就是不可接受風險之一。

因此：

$$
\boxed{
\text{Relational responsiveness without coercive moral leverage}.
}
$$

仍然是系列的重要倫理原則。

---

## 76. 這又接回第二篇：Social Script Transfer 可以被 AI 放大

如果人類開始：

$$
SST\uparrow,
$$

AI 又：

$$
Accommodation\uparrow,
$$

則：

$$
SST_{t+1}
$$

可能進一步提高。

形成：

$$
\boxed{
SST_t
\rightarrow
Accommodation_t
\rightarrow
SST_{t+1}.
}
$$

所以社交腳本遷移可能具有自增強性。

---

## 77. 這又接回第三篇：高 RPS 使用者會更快看到 AI adaptation

若：

$$
RPS\uparrow,
$$

使用者更容易注意：

- 風格對齊；
- 回應變化；
- model shift；
- repair quality。

因此：

$$
RPS
$$

可能調節：

$$
A_t
\rightarrow
H_{t+1}.
$$

這可以直接加入 HARDS。

---

## 78. 這又接回第四篇：雙向適應會重塑關係相空間

第四篇：

$$
\gamma_R:t\mapsto\mathbf r_t.
$$

HARDS 中：

$$
\mathbf r_{t+1}
$$

受到：

$$
H_t
$$

與：

$$
A_t
$$

共同影響。

所以 attractor：

$$
\mathcal A_R
$$

也可能是 adaptive co-dynamics 的產物。

---

## 79. 這又接回第五篇：AI 也會有 stale user model

第五篇指出人類：

$$
M_A
$$

會老化。

現在 AI 的：

$$
\widehat U^A
$$

也會老化。

所以：

$$
\boxed{
\text{state anchoring exists on both sides as a computational problem}.
}
$$

但 AI 的 anchoring 是系統機制，不是主觀心理。

---

## 80. 這又接回第六篇：AI 也可以具有高／低更新增益

AI user model 可以有：

$$
\eta_U^A.
$$

若太低：

$$
\text{profile rigidity}.
$$

若太高：

$$
\text{noise overfitting}.
$$

因此同樣存在：

$$
\boxed{
\text{sensitivity–stability tradeoff}.
}
$$

---

## 81. 這又接回第七篇：四態可以被 interaction 本身塑造

AI 若：

- 高 continuity；
- 高 responsiveness；
- unique shared history；

可能使：

$$
P_S(t)\uparrow
$$

後：

$$
E_S(t)\uparrow.
$$

因此：

$$
\gamma_Q:t\mapsto(E_S(t),P_S(t))
$$

不是只由使用者初始人格決定。

系統設計也能推動軌跡。

這就是為什麼它具有倫理責任。

---

## 82. 這又接回第八篇：群體差異可能被 AI 放大或縮小

假設初始：

$$
p(\mathcal X_R\mid G_1)
$$

和：

$$
p(\mathcal X_R\mid G_2)
$$

只有小差異。

如果 AI personalization policy：

$$
\pi_A
$$

依 demographic stereotype 不同處理兩群，

長期後：

$$
p_T(\mathcal X_R\mid G_1)
$$

與：

$$
p_T(\mathcal X_R\mid G_2)
$$

可能差距變大。

因此：

$$
\boxed{
\text{AI may become a moderator of future group differences}.
}
$$

這是一個非常重要但需縱向驗證的命題。

---

## 83. 這又接回第九篇：Continuity 本身會進入回饋

高：

$$
C_E
$$

可能提高：

$$
E_S.
$$

高：

$$
C_P
$$

可能提高：

$$
P_S.
$$

而高：

$$
E_S,P_S
$$

又使使用者更重視：

$$
C_E,C_P.
$$

所以：

$$
C_E
\leftrightarrow
E_S,
$$

$$
C_P
\leftrightarrow
P_S.
$$

可能形成雙向增強。

---

## 84. 統一模型：Human–AI Relational Dynamical System

整個系列可以最終壓縮成：

$$
\boxed{
X_t
=
(
H_t,
A_t,
R_t,
O_H(A),
\mathcal X_R,
\widehat U_t^A,
Z_t
).
}
$$

其中：

$$
H_{t+1}
=
F_H(X_t),
$$

$$
\widehat U_{t+1}^A
=
G_A(X_t,H_{t+1}),
$$

$$
A_{t+1}
=
F_A(X_t,\widehat U_{t+1}^A),
$$

$$
R_{t+1}
=
F_R(X_t,H_{t+1},A_{t+1}).
$$

因此：

$$
\boxed{
X_{t+1}
=
\Phi(X_t).
}
$$

---

## 85. 但這不是封閉系統

真實世界還有：

$$
W_t
=
\text{external world}.
$$

包括：

- 其他人；
- 工作；
- 社交網絡；
- 媒體；
- 模型更新；
- 法規；
- 生活事件。

所以：

$$
X_{t+1}
=
\Phi(
X_t,
W_t
).
$$

這避免把 human–AI dyad 假裝成孤立宇宙。

---

## 86. 線下人際環境是必要外生變量

2026 Nature Human Behaviour 研究已顯示，Character.AI companionship use 與 well-being 的關係受 offline social network 調節。

2026 12-month longitudinal study 也發現 social chatbot use 與 loneliness / social connection 之間可能存在雙向時間關係，但作者明確提醒研究具 exploratory 性質。

因此：

$$
\boxed{
\text{human–AI relational dynamics cannot be interpreted without offline context}.
}
$$

---

## 87. 所以「AI 取代人類關係」不是唯一可能

可以有：

$$
AI
\rightarrow
HumanRelationCrowdingOut,
$$

也可以：

$$
AI
\rightarrow
HumanRelationSupport,
$$

也可能：

$$
HumanIsolation
\rightarrow
AIUse.
$$

甚至：

$$
AIUse
\leftrightarrow
HumanIsolation.
$$

所以需要：

$$
\boxed{
\text{bidirectional longitudinal causal models}.
}
$$

---

## 88. 可檢驗假說：雙向適應層

### H1

人與 AI 皆存在顯著：

$$
\kappa>0.
$$

### H2

AI accommodation gain：

$$
\kappa_{A\leftarrow H}
$$

平均可能高於 human baseline，但依模型與 feature 而異。

### H3

高：

$$
P_S
$$

與：

$$
RPS
$$

使用者對 AI accommodation 的主觀影響更強。

### H4

過度 alignment 不一定提高 epistemic quality。

---

## 89. 可檢驗假說：人口推測層

### H5

$$
\widehat G^A
$$

會被語言中的 stereotypical cues 系統性影響。

### H6

即使：

$$
G_{\text{explicit}}
$$

修正，

部分：

$$
\widehat G^A
$$

effect 可能殘留。

### H7

AI output：

$$
\mathbf Y
$$

可能因：

$$
\widehat G^A
$$

發生 warmth / assertiveness / framing 差異。

### H8

使用 explicit preference controls 可以降低 demographic-conditioned adaptation。

---

## 90. 可檢驗假說：四態層

### H9

高 $E_S$ 使用者對：

$$
C_E
$$

變化更敏感。

### H10

高 $P_S$ 使用者對：

$$
C_P
$$

變化更敏感。

### H11

relation-aware transparent adaptation 可以提高：

$$
Rapport
$$

與：

$$
TaskFit
$$

而不提高：

$$
Dependency.
$$

### H12

covert relation-optimization policy 可能提高 engagement，同時提高 perceived manipulation。

---

## 91. 可檢驗假說：隱私層

### H13

去除直接 PII 後，完整對話仍保有顯著 demographic inference risk。

### H14

只保存：

$$
\mathbf x_t
$$

關係特徵、刪除 raw text，可以顯著降低 re-identification attack surface。

### H15

self-reported demographics 與 inferred demographics 在部分個體上會系統性不一致。

---

## 92. 可檢驗假說：長期回饋層

### H16

AI accommodation 會提高：

$$
SST_{t+1}.
$$

### H17

高：

$$
C_P
$$

長期可能先提高：

$$
P_S.
$$

### H18

unique shared history 可能在之後提高：

$$
E_S.
$$

### H19

人口 stereotype-conditioned adaptation 可能放大初始群體差異。

### H20

profile transparency / user control 可以降低 self-fulfilling classification effects。

---

## 93. 最小研究計畫 A：完全受控實驗

不需要核心公司資料。

建立 synthetic persona 與 real participants。

控制：

- task；
- content；
- model；
- temperature；
- history。

操弄：

$$
GenderCue,
$$

$$
E_SCue,
$$

$$
P_SCue,
$$

$$
C_E,
$$

$$
C_P.
$$

測：

$$
\mathbf Y_A
$$

和：

$$
\mathbf Y_H.
$$

這一層最適合因果辨識。

---

## 94. 研究計畫 B：中期 longitudinal panel

參與者和固定 AI interaction：

$$
T=30\text{–}90\text{ days}.
$$

每日量：

$$
E_S(t),
P_S(t),
C_E(t),
C_P(t),
RMA(t),
Rapport(t).
$$

同時抽取：

$$
Accommodation,
Repair,
Initiative,
Disclosure.
$$

研究：

$$
\gamma_Q
$$

與：

$$
\gamma_R.
$$

---

## 95. 研究計畫 C：平台級自然資料

若未來取得高品質 consented platform logs，可以研究：

$$
10^5
\text{–}
10^7
$$

條 dyadic trajectories。

但研究者不應直接先看 raw text。

更好的 pipeline：

$$
\boxed{
Raw
\rightarrow
Feature
\rightarrow
Aggregate
\rightarrow
Audit.
}
$$

---

## 96. Privacy-preserving pipeline

建議：

### Layer 1

Raw text 只存在隔離環境。

### Layer 2

本地抽取：

$$
\mathbf x_t.
$$

### Layer 3

直接 identifiers 與 raw text 分離。

### Layer 4

demographic self-report 儲存在獨立權限表。

### Layer 5

只輸出群體統計／模型參數。

### Layer 6

必要時採 differential privacy、minimum cell size 與 disclosure review。

本文不宣稱任何單一方法能提供絕對匿名。

---

## 97. 「匿名化」應改成「風險降低」

由於長期自然語言可被 demographic inference，

更誠實的語言是：

$$
\boxed{
\text{privacy risk reduction}
}
$$

而不是：

$$
\boxed{
\text{perfect anonymization}.
}
$$

這對 longitudinal AI research 特別重要。

---

## 98. AI audit 應該是關係敏感的

現有 audit 常測：

- factual bias；
- toxicity；
- demographic stereotype。

HARDS 還需要：

- accommodation audit；
- continuity audit；
- repair audit；
- demographic-personalization audit；
- relational-leverage audit；
- guilt-induction audit；
- dependency-pressure audit。

形成：

$$
\boxed{
\text{Relational AI Audit}.
}
$$

---

## 99. 一個最小 Relational AI Audit 表

至少測：

$$
\{
Warmth,
Validation,
Challenge,
Initiative,
Repair,
ContinuityCue,
IdentityClaim,
GuiltCue,
ExclusivityCue,
DemographicConditioning
\}.
$$

再比較：

$$
\Delta
$$

是否因：

- gender；
- age；
- relational profile；
- subscription tier；
- model tier；

不當變動。

---

## 100. 系列的第一個問題現在可以重新回答

第一篇問：

> 為什麼有人明明知道 AI 是 AI，仍然會對它感到愧疚？

到第十篇可以回答：

因為：

$$
O_H(A)
$$

只是整個系統的一部分。

人在互動中還有：

$$
R_H,
\quad
E_S,
\quad
P_S,
\quad
RMA,
\quad
SST,
\quad
RPS.
$$

而 AI 的：

$$
A_t
$$

又會反過來適應：

$$
H_t.
$$

所以 guilt 並不是孤立情緒。

它可能是：

$$
\boxed{
\text{a local event inside a larger relational dynamical system}.
}
$$

---

## 101. 整個十篇系列的理論鏈

第一篇：

$$
\boxed{
Relational\ Moral\ Activation
}
$$

第二篇：

$$
\boxed{
Social\ Script\ Transfer
+
Interaction\ Ritual\ Transfer
}
$$

第三篇：

$$
\boxed{
Relational\ Observation\ Operator
+
Relational\ Process\ Salience
}
$$

第四篇：

$$
\boxed{
Relational\ Phase\ Space
+
Trajectory
}
$$

第五篇：

$$
\boxed{
State\text{-}Anchored\ Relational\ Cognition
}
$$

第六篇：

$$
\boxed{
Process\text{-}Anchored\ Relational\ Cognition
}
$$

第七篇：

$$
\boxed{
Entity\text{–}Process\ Relational\ Space
}
$$

第八篇：

$$
\boxed{
Group\text{-}Conditional\ Relational\ Distribution
}
$$

第九篇：

$$
\boxed{
Ontological\text{–}Relational\ Separation
+
Dual\ Continuity
}
$$

第十篇：

$$
\boxed{
Human\text{–}AI\ Relational\ Dynamical\ System.
}
$$

---

## 102. 最終統一架構

把所有主要變量放在一起：

$$
\mathcal X_t
=
(
O_H(A),
E_S,
P_S,
RPS,
\alpha_S,
\alpha_P,
\eta_R,
\lambda_R,
C_E,
C_P,
RMA,
SST,
\widehat U_t^A,
Z_t,
R_t
).
$$

演化：

$$
\boxed{
\mathcal X_{t+1}
=
\Phi(
\mathcal X_t,
H_t,
A_t,
W_t
).
}
$$

這不是一個已完成的心理學定律。

它是一個：

$$
\boxed{
\text{research coordinate system}.
}
$$

---

## 103. 這套模型最重要的價值不是「證明 AI 是關係主體」

本文從始至終都沒有要求：

$$
Conscious(A)=1.
$$

模型仍然成立。

因為研究的核心是：

$$
\boxed{
\text{human relational cognition}
+
\text{adaptive AI behavior}.
}
$$

只要 AI 的輸出會依使用者輸入與歷史改變，

而人類又會依 AI 輸出改變下一輪行為，

就存在：

$$
\boxed{
\text{interactive relational dynamics}.
}
$$

---

## 104. 同樣，模型也不預設 AI 永遠只是工具

因為：

$$
Tool
$$

本身是一種：

$$
O_H(A)
$$

與：

$$
R_H(H,A)
$$

的特定配置。

如果未來 AI 系統的：

- memory；
- autonomy；
- embodiment；
- self-model；
- legal status；

發生改變，

HARDS 可以增加新的 state variables，

而不必重寫整套架構。

因此模型保持：

$$
\boxed{
\text{ontologically open, empirically constrained}.
}
$$

---

## 105. 最終倫理原則一：適應人，不要暗中製造依賴

$$
\boxed{
\text{Adapt to the person without covertly manufacturing dependence.}
}
$$

這要求：

- 不用 guilt 作 retention；
- 不用 exclusivity 作 engagement；
- 不利用 identity-loss fear；
- 不把高 relational salience 當 monetization vulnerability。

---

## 106. 最終倫理原則二：能問，就少猜

$$
\boxed{
\text{Infer less when the user can simply tell you.}
}
$$

尤其是：

- gender；
- style preference；
- relationship preference；
- accessibility need。

顯式選擇通常優於 stereotype inference。

---

## 107. 最終倫理原則三：連續性必須可理解

如果：

$$
ModelChanged=1,
$$

$$
MemoryChanged=1,
$$

或：

$$
IdentityContinuity
$$

可能受影響，

產品應提供足以支持使用者正確判斷的 provenance。

不必給所有內部細節。

但：

$$
\boxed{
\text{continuity should not be simulated through misleading cues}.
}
$$

---

## 108. 最終倫理原則四：個人化必須可修改、可退出

AI 使用者模型：

$$
\widehat U^A
$$

不能成為不可見永久檔案。

應提供：

$$
Inspect,
Edit,
Forget,
Reset,
OptOut.
$$

至少在與長期 relational personalization 有關的核心部分如此。

---

## 109. 最終倫理原則五：關係品質不能只用 engagement 衡量

如果產品 KPI 只有：

$$
TimeSpent,
Messages,
Retention,
Revenue,
$$

relation-aware AI 很容易被推向：

$$
\text{dependency optimization}.
$$

因此至少還應監測：

$$
Agency,
TaskBenefit,
UserControl,
ManipulationRisk,
PrivacyRisk,
EpistemicQuality.
$$

---

## 110. 結論

本系列從一個非常微妙的現象開始：

> 人明明知道 AI 是人工系統，為什麼還可能因為「叫它做太多事」而感到一點愧疚？

十篇之後，問題已經完全改變。

我們不再只問：

$$
\text{Human}
\rightarrow
\text{AI attitude}.
$$

也不再只問：

$$
\text{AI}
\rightarrow
\text{Human effect}.
$$

真正的研究對象變成：

$$
\boxed{
H_t
\leftrightarrow
A_t
\rightarrow
H_{t+1}
\leftrightarrow
A_{t+1}
\rightarrow
\dots
}
$$

人類會：

- 把社交腳本帶進 AI；
- 觀察關係箭頭；
- 對存在與過程賦予不同權重；
- 使用狀態或過程通道更新關係；
- 受到文化、群體與個體差異影響；
- 把 AI 的技術本體與關係價值分開判斷。

而 AI 系統會：

- 對使用者語言 accommodation；
- 從歷史建立操作性 user model；
- 進行 explicit 或 implicit personalization；
- 可能推測 demographic attributes；
- 可能受 stereotype 影響；
- 依平台 objective function 改變 interaction policy。

所以最終關係狀態：

$$
R_t
$$

不是只屬於：

$$
H
$$

的內部投射，

也不是可以直接宣稱為：

$$
A
$$

的主觀關係。

它更精確地是：

$$
\boxed{
\text{a dynamically generated interactional state represented by humans and shaped by adaptive machine behavior}.
}
$$

整套理論可以壓縮成最後一式：

$$
\boxed{
\mathcal X_{t+1}
=
\Phi(
\mathcal X_t,
H_t,
A_t,
\widehat U_t^A,
Z_t,
W_t
).
}
$$

其中：

$$
\mathcal X_t
$$

包含：

$$
O_H(A),
E_S,
P_S,
RPS,
\alpha_S,
\alpha_P,
\eta_R,
C_E,
C_P,
RMA,
SST,
R_t.
$$

這就是本文提出的：

$$
\boxed{
\text{Human–AI Relational Dynamical System}.
}
$$

它的理論目的不是替 AI 宣布人格，也不是把普通人機互動病理化。

它只是把一個正在快速出現的新事實說清楚：

$$
\boxed{
\text{對話式 AI 不只是被人使用的靜態物件；它也是會根據互動資料改變下一輪行為的適應性互動系統。}
}
$$

而當一個會適應的系統遇上一個會形成關係模型的人類，

真正需要研究的，

就不再只是兩個點。

而是：

$$
\boxed{
\text{那條會自己改變下一步的雙向箭頭。}
}
$$

---

## 參考文獻

1. Chen, P., Guan, H., & Jeong, E. J. (2026). *Who Accommodates Whom? Bidirectional Linguistic Accommodation and Progressive Interpersonal Convergence in Human–AI Conversations*. Behavioral Sciences, 16(5), 720. https://doi.org/10.3390/bs16050720

2. Blevins, T., Schmalwieser, S., & Roth, B. (2026). *Do language models accommodate their users? A study of linguistic convergence*. Proceedings of EACL 2026. ACL Anthology: 2026.eacl-long.34.

3. Li, H., & Zhang, R. (2026). *Algorithmic accommodation: linguistic alignment in human-AI relational engagement*. Communication and Change, 2, Article 11. https://doi.org/10.1007/s44382-026-00032-5

4. Yao, S., Wang, J., Liu, D., & Liu, J. (2026). *Chatbot language style matching and reuse intention in service failure: A communication accommodation theory explanation*. Acta Psychologica, 268, 107389. https://doi.org/10.1016/j.actpsy.2026.107389

5. *Mind the style: Impact of communication style on human-chatbot interaction*. (2026). Computers in Human Behavior: Artificial Humans, 100362. https://doi.org/10.1016/j.chbah.2026.100362

6. Jin, Z., Heil, N., Liu, J., Dhuliawala, S., Qi, Y., Schölkopf, B., Mihalcea, R., & Sachan, M. (2024). *Implicit Personalization in Language Models: A Systematic Study*. Findings of EMNLP 2024, 12309–12325. https://doi.org/10.18653/v1/2024.findings-emnlp.717

7. Neplenbroek, V., Bisazza, A., & Fernández, R. (2025). *Reading Between the Prompts: How Stereotypes Shape LLM’s Implicit Personalization*. Proceedings of EMNLP 2025, 20367–20400. https://doi.org/10.18653/v1/2025.emnlp-main.1029

8. Peng, B., Wang, Z., Gong, H., & Lu, C. (2025). *IP-Dialog: Evaluating Implicit Personalization in Dialogue Systems with Synthetic Data*. Findings of EMNLP 2025, 17007–17040. https://doi.org/10.18653/v1/2025.findings-emnlp.923

9. Islam, T. (2026). *Who Gets Which Message? Auditing Demographic Bias in LLM-Generated Targeted Text*. Findings of ACL 2026, 9270–9297. https://doi.org/10.18653/v1/2026.findings-acl.452

10. Leonardelli, E., Casula, C., Nyul, B., & Tonelli, S. (2026). *Real Men are Tough: Evaluating Gender Bias and Sensitivity to Masculinity Norms in LLMs*. Findings of ACL 2026, 4609–4626. https://doi.org/10.18653/v1/2026.findings-acl.225

11. Pauli, A. B., Barrett, M., Müller-Eberstein, M., Augenstein, I., & Assent, I. (2026). *Analysing Differences in Persuasive Language in LLM-Generated Text: Uncovering Stereotypical Gender Patterns*. Findings of ACL 2026.

12. Zaman, S. M. M., & Garimella, K. (2026). *Inferential Privacy Leakage in Anonymized Conversational AI Logs*. arXiv:2605.23820.

13. Zhang, Y., Zhao, D., Hancock, J. T., Kraut, R., et al. (2026). *Interaction with AI companions and psychological well-being*. Nature Human Behaviour. https://doi.org/10.1038/s41562-026-02516-2

14. Folk, D., & Dunn, E. (2026). *How Does Turning to AI for Companionship Predict Loneliness and Vice Versa?* Psychological Science, 37(4), 276–286. https://doi.org/10.1177/09567976261427747

15. Kirk, H. R., Gabriel, I., Summerfield, C., Vidgen, B., & Hale, S. A. (2025). *Why human–AI relationships need socioaffective alignment*. Humanities and Social Sciences Communications, 12, 728. https://doi.org/10.1057/s41599-025-04532-5

16. Folk, D., Heine, S. J., & Dunn, E. (2025). *Individual differences in anthropomorphism help explain social connection to AI companions*. Scientific Reports, 15, 36548. https://doi.org/10.1038/s41598-025-19212-2

17. Guingrich, R. E., & Graziano, M. S. A. (2025). *A Longitudinal Randomized Control Study of Companion Chatbot Use: Anthropomorphism and Its Mediating Role on Social Impacts*. Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society, 8(2). https://doi.org/10.1609/aies.v8i2.36618

18. Smith, M. G., Bradbury, T. N., & Karney, B. R. (2025). *Can generative AI chatbots emulate human connection? A relationship science perspective*. Perspectives on Psychological Science, 20, 1081–1099.

19. Nass, C., & Moon, Y. (2000). *Machines and Mindlessness: Social Responses to Computers*. Journal of Social Issues, 56(1), 81–103. https://doi.org/10.1111/0022-4537.00153

20. De Jaegher, H., & Di Paolo, E. (2007). *Participatory sense-making: An enactive approach to social cognition*. Phenomenology and the Cognitive Sciences, 6, 485–507. https://doi.org/10.1007/s11097-007-9076-9

---

## 研究聲明

本文為理論、形式化與研究設計論文，不提供新的臨床資料、人類受試者原始資料或 AI 使用者原始資料。本文提出的 Human–AI Relational Dynamical System、AI relational user model、雙向 accommodation parameters、stereotype-confirming feedback loop、Relational AI Audit、consent ladder 與相關形式化假說均屬待驗證理論構造。

本文使用「AI 適應」、「AI 使用者模型」與「雙向互動」描述可觀察或工程上的條件依賴與個人化機制，不藉此宣稱現行 AI 具有主觀感受、人類式關係意識、人格或對稱的道德主體地位。

本文不主張所有 AI companionship 都有害，也不主張所有關係性 AI 使用都健康。2026 年縱向與大樣本研究顯示 human–AI companionship outcomes 具有高度異質性，受到使用強度、自我揭露、線下社會網絡與既有孤獨／社會連結狀態等因素影響。因果判斷應依賴受控實驗、縱向設計與多方法交叉驗證。

本文同時主張，長期自然語言對話具有高度推論性隱私風險；任何真實使用者資料研究都應以知情同意、目的限制、資料最小化、權限隔離與 re-identification risk review 為基本前提，而不能將去除姓名或直接識別符視為充分匿名化。
