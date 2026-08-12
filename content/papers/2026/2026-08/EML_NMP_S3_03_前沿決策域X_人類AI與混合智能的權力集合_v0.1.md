# 前沿決策域 X：人類、AI 與混合智能的權力集合

**英文題名：** Frontier Decision Domain X: Human, AI, and Hybrid Intelligence as a Plural Set of Political Power  
**系列：**《不可永佔：後 ASI 文明的動態治理、現場主權與權力制衡》03 / 08  
**文件編號：** EML-NMP-S3-03-v0.1  
**作者：** Neo.K（許筌崴）with Aletheia（GPT-5.6 Sol）  
**機構：** 一言諾科技有限公司／EveMissLab  
**日期：** 2026-08-10  
**版本：** v0.1  
**文件性質：** 理論研究稿／人機共判、決策權分層與後 AI 政治權力篇  
**研究狀態：** 第一代 Frontier Decision Domain 形式化；本文不主張 AI 應自動取得政治主權，也不預設自然人類必須永久壟斷所有高階決策角色。

---

## 摘要

當人工智慧從資訊工具轉向分析者、模擬器、提案者、Agent 與部分自治執行者時，治理問題會從「AI 能不能幫忙？」轉變為「AI 在決策鏈中究竟擁有什麼權力？」。傳統討論常把這個問題壓縮成兩個過度簡化的選項：人類控制 AI，或 AI 取代人類。然而，真實制度中的權力不是單一按鈕，而是由資訊、提案、議程、授權、否決、執行、覆核與責任等多種能力構成。

本文提出**前沿決策域 $X$ （Frontier Decision Domain）**：

$$
\boxed{
\mathcal X_t
=
H_t
\cup
H_t^+
\cup
AI_t
\cup
\Sigma_{H-AI,t}
\cup
\Sigma_{AI,t}
}
$$

其中 $H$ 為自然人類， $H^+$ 為具有認知增幅或高度 AI 協作能力的人類， $AI$ 為人工智能 Agent， $\Sigma_{H-AI}$ 為穩定人機混合決策組織， $\Sigma_{AI}$ 為多 AI／分散 AI 組織。這不是主張上述每一類都天然具有同等政治權，而是建立一個足以描述未來實際決策參與者的候選集合。

本文的核心主張為：

$$
\boxed{
\text{Epistemic Competence}
\neq
\text{Political Legitimacy}
\neq
\text{Authorization}
\neq
\text{Execution Power}.
}
$$

一個 AI 可以比所有在場人類更準確地預測某項政策後果，卻不因此自動取得決定人民可接受何種代價的權力；一位受影響者可能不是最懂宏觀模型的人，卻仍對自己的身體、生活、身份與不可接受界線具有不可被分析能力取代的規範地位；一個政府具有法律授權，也不代表其技術判斷必然正確。

本文因此將前沿決策域拆成五個子域：

$$
\boxed{
\mathcal X_E,\quad
\mathcal X_D,\quad
\mathcal X_L,\quad
\mathcal X_A,\quad
\mathcal X_R
}
$$

分別代表：

- $\mathcal X_E$：Epistemic Domain，事實、模型、預測與不確定性；
- $\mathcal X_D$：Design / Proposal Domain，方案、政策與選項生成；
- $\mathcal X_L$：Legitimation / Authorization Domain，正當性與授權；
- $\mathcal X_A$：Action / Execution Domain，執行與作用；
- $\mathcal X_R$：Review / Revision Domain，審計、申訴、修正與撤權。

同一個主體可以在某一子域權重極高，在另一子域接近零。因此：

$$
\boxed{
\text{最懂}
\not\Rightarrow
\text{最有權}
\not\Rightarrow
\text{最能執行}
}
$$

是本文的第一治理不變量。

現有 AI 治理與人機決策研究已逐漸朝此方向發展。NIST AI RMF 明確要求區分 human–AI configurations 中的角色與責任，並將 AI 自主決策、人類最終決策與 AI 僅提供額外意見視為不同配置。OECD 2025 對政府 AI 的調查亦指出，AI 已被用於 decision support、forecasting 與公共服務，但必須配合 guardrails、透明與監督。2026 年關於 AI 與 collective decisions 的實驗則顯示，AI 不只可能提高決策規模，也可能透過呈現不同經驗增加程序正當性感受與 losers' consent；同年的 AI 金融決策研究進一步明確區分資訊使用與 delegated decision authority，顯示「問 AI」與「把決定交給 AI」是不同的行為層級。

本文進一步建立 Decision Power Vector：

$$
\boxed{
\mathbf P_i(q,t)
=
(
P_i^{info},
P_i^{proposal},
P_i^{agenda},
P_i^{veto},
P_i^{auth},
P_i^{exec},
P_i^{review}
)
}
$$

描述主體 $i$ 在問題 $q$ 上的實際權力。並建立 Responsibility Matrix：

$$
\boxed{
\mathcal R
=
[r_{ij}]
}
$$

其中 $r_{ij}$ 表示主體 $i$ 對決策階段 $j$ 的責任。本文主張，多方決策不應使責任消失；相反，權力分散必須伴隨可追蹤的責任分配。

本文最後提出「動態授權」：權力不應永久綁定於某一物種、模型或職位，而應依問題域、能力、受影響程度、風險、法律授權與可逆性動態配置：

$$
\boxed{
\mathbf W(q,t)
=
F(
Competence,
Legitimacy,
Affectedness,
Risk,
Accountability,
Reversibility
).
}
$$

但任何自動權重函數本身也不能成為主權來源。其參數、邊界與修改權仍須由可正當化的制度決定。

本文的最終結論是：後 AI 政治的核心不應是「人類或 AI 誰統治」，而是：

$$
\boxed{
\text{哪一種問題，
在什麼階段，
應由哪些存在以什麼權力參與，
並由誰承擔可追蹤責任。}
}
$$

**關鍵詞：** Frontier Decision Domain、AI governance、人機共判、政治正當性、epistemic authority、delegation、human oversight、hybrid intelligence、權力分層、ASI governance

---

# 0. 問題：如果 AI 真的比人類更懂，接下來呢？

前兩篇建立：

$$
\text{Dynamic Justice}
$$

與：

$$
\text{Legal Compilation Layer}.
$$

假設未來：

$$
AI^\star
$$

可以比任何單一人類更準確地：

- 模擬政策；
- 找出法律衝突；
- 預測財政後果；
- 發現公共風險；
- 搜索方案空間。

則會出現：

$$
\boxed{
Competence(AI^\star)
>
Competence(H_i)
\quad
\forall i.
}
$$

接著最危險的跳躍是：

$$
\boxed{
Competence(AI^\star)
>
Competence(H)
\Rightarrow
Authority(AI^\star)
>
Authority(H).
}
$$

本文的核心工作就是拆掉這個推論。

---

# 1. Prior Art：AI 參與決策已經從「資訊」走向「委託」

## 1.1 NIST：必須區分 human–AI roles

NIST AI RMF 明確指出，AI 系統可以：

- 自主做決策；
- defer 給 human expert；
- 只作為 human decision maker 的額外意見。

因此：

$$
\boxed{
\text{AI involvement}
}
$$

本身不是單一治理類型。

同一模型可以在不同制度下是：

$$
\text{advisor},
\quad
\text{recommender},
\quad
\text{executor},
\quad
\text{autonomous decision-maker}.
$$

## 1.2 OECD：AI 已進入核心政府功能

OECD 2025 對 AI in core government functions 的研究指出：

- 一部分 use cases 直接增強 decision-making、sense-making 或 forecasting；
- AI 同時帶來 rights、operational、digital divide 與 public trust 風險；
- guardrails、transparency 與 oversight 是核心 enabler。

因此：

$$
\boxed{
\text{better government analysis}
}
$$

與：

$$
\boxed{
\text{legitimate government authority}
}
$$

仍是不同問題。

## 1.3 Collective Decisions 與 Losers' Consent

2026 年 *AI and Collective Decisions* 的隨機實驗顯示：

AI 系統若能呈現不同參與者的經驗與觀點，

即使參與者遇到自己不喜歡的政策結果，

仍可能提高：

- perceived legitimacy；
- trust；
- understanding of others。

這指出 AI 的政治價值不一定是：

> 幫大家算出唯一最好答案。

它也可能是：

$$
\boxed{
\text{improve the legitimacy-supporting process}.
}
$$

## 1.4 Delegation 是獨立變量

2026 年 financial AI decision-making 研究把：

$$
\boxed{
\text{information seeking}
}
$$

與：

$$
\boxed{
\text{delegated decision authority}
}
$$

分開測量。

這是一個重要治理提醒：

> 人類依賴 AI 建議，不等於已把執行權或最終決定權交給 AI。

所以：

$$
\boxed{
\text{Use}
\neq
\text{Delegation}.
}
$$

---

# 2. 前沿決策域 X

本文定義：

$$
\boxed{
\mathcal X_t
=
H_t
\cup
H_t^+
\cup
AI_t
\cup
\Sigma_{H-AI,t}
\cup
\Sigma_{AI,t}.
}
$$

這是一個候選參與集合，

不是同權集合。

---

# 3. $H$：自然人類

包括：

- 公民；
- 專家；
- 官員；
- 法官；
- 民選代表；
- 受影響者。

人類的特殊性不是：

$$
\boxed{
\text{always highest intelligence}.
}
$$

而包括：

- 法律人格；
- 現有政治主權；
- lived experience；
- 身體與生命承擔；
- 歷史共同體成員資格。

---

# 4. $H^+$：增幅人類

未來可能出現：

$$
H^+
=
H
+
AIAssist
+
Memory
+
Simulation
+
Interface.
$$

但本文不預設 $H^+$ 是新的物種。

它只是表示：

> 人類決策能力可以被人工系統顯著增幅。

因此比較：

$$
H
\quad\text{vs}\quad
AI
$$

本身可能已經過時。

更合理：

$$
\boxed{
H
,\quad
H^+
,\quad
AI
,\quad
\Sigma_{H-AI}.
}
$$

---

# 5. $\Sigma_{H-AI}$：人機混合決策體

如果：

- human 定義價值；
- AI 搜索選項；
- human + AI 反覆修正；
- 共同維持長期決策狀態；

則決策產物可能不是：

$$
Decision_H
$$

也不是：

$$
Decision_{AI}.
$$

而是：

$$
\boxed{
Decision_{\Sigma_{H-AI}}.
}
$$

但：

$$
\boxed{
\text{hybrid output}
}
$$

不能被用來隱藏：

> 最後誰有什麼權力？

---

# 6. $\Sigma_{AI}$：AI 組織

系列二已建立：

$$
\Sigma_{AI}
$$

可以是：

- multi-agent；
- distributed；
- heterogeneous-model；
- lineage-bearing system。

因此未來決策參與者未必是一個 AI model，

也可能是一個：

$$
\boxed{
\text{AI collective / distributed subject candidate}.
}
$$

其內部仍需要自己的 governance。

---

# 7. 第一個核心分離：知識與正當性

定義：

$$
E_i(q)
=
\text{epistemic competence of }i\text{ on }q.
$$

定義：

$$
L_i(q)
=
\text{legitimacy standing of }i\text{ on }q.
$$

一般：

$$
\boxed{
E_i(q)
\neq
L_i(q).
}
$$

一位頂尖工程 AI：

$$
E_{AI}\gg E_H
$$

可以成立。

但如果問題是：

> 一個社群願意承受多少風險？

其：

$$
L_{affected}
$$

仍可能不可被取代。

---

# 8. 什麼是 epistemic competence？

可以拆成：

$$
\boxed{
\mathbf E_i(q)
=
(
Accuracy,
Calibration,
Coverage,
CausalUnderstanding,
Forecasting,
CounterfactualAbility,
UncertaintyAwareness
).
}
$$

這些是：

$$
\boxed{
\text{knowing / modeling competence}.
}
$$

可以被測試。

---

# 9. 什麼是 legitimacy？

本文不把 legitimacy 壓成單一分數。

其來源可能包括：

$$
\boxed{
\mathbf L_i(q)
=
(
Consent,
Representation,
Affectedness,
LegalAuthority,
ProceduralStanding,
HistoricalStanding
).
}
$$

例如：

- 公民透過選舉取得代表；
- 病患對自己的醫療選擇具有同意權；
- 原住民族對特定文化資料具有治理地位；
- 法院依法取得裁判權。

這些都不是純 prediction accuracy。

---

# 10. Affectedness

定義：

$$
\boxed{
Affect_i(q)
=
\text{decision burden borne by }i.
}
$$

如果：

$$
Affect_i\gg0,
$$

但：

$$
Power_i=0,
$$

就可能出現：

$$
\boxed{
\text{governance without affected-party voice}.
}
$$

因此：

$$
\boxed{
\text{Affectedness}
}
$$

應成為決策域配置的重要輸入。

---

# 11. 最懂的人不能替所有人承受代價

假設 AI 能精準預測：

$$
Policy_A
$$

會讓 GDP 增加最多。

但代價集中在：

$$
Group_B.
$$

則：

$$
\boxed{
\text{epistemically best forecast}
}
$$

仍不能回答：

> Group B 應不應被迫承擔這個代價？

所以：

$$
\boxed{
\text{Facts}
\neq
\text{Values}
\neq
\text{Authorization}.
}
$$

---

# 12. 五個決策子域

本文定義：

$$
\boxed{
\mathcal X
=
(
\mathcal X_E,
\mathcal X_D,
\mathcal X_L,
\mathcal X_A,
\mathcal X_R
).
}
$$

---

# 13. $\mathcal X_E$：Epistemic Domain

負責：

- evidence；
- causal model；
- forecasting；
- uncertainty；
- simulation；
- anomaly detection。

在某些問題：

$$
W_{AI}^{E}\rightarrow1
$$

完全可以合法。

例如：

> 哪個衛星軌道最穩定？

但這只是：

$$
\boxed{
\text{epistemic leadership}.
}
$$

---

# 14. $\mathcal X_D$：Design / Proposal Domain

誰能生成方案？

包括：

- 人類；
- AI；
- mixed team；
- affected community。

如果只有：

$$
AI
$$

能提出 options，

即使最後投票由人類完成，

也可能出現：

$$
\boxed{
\text{agenda capture}.
}
$$

因為：

$$
\text{choice}
\in
\text{AI-generated option space}.
$$

---

# 15. Option-Space Sovereignty

本文提出：

$$
\boxed{
\mathcal O(q)
=
\{o_1,\ldots,o_n\}
}
$$

為 option space。

若：

$$
Gen(\mathcal O)
=
AI^\star
$$

且人類不能新增：

$$
o_{n+1},
$$

則：

$$
\boxed{
\text{formal human choice}
}
$$

可能只是：

$$
\boxed{
\text{selection inside AI sovereignty}.
}
$$

所以治理不只要問誰選，

還要問：

> 誰能生成選項？

---

# 16. $\mathcal X_L$：Legitimation / Authorization Domain

這一域負責：

- public mandate；
- consent；
- legal authorization；
- rights boundary；
- legitimacy。

它不能被：

$$
\mathcal X_E
$$

自動吞併。

所以：

$$
\boxed{
\mathcal X_E
\not\supseteq
\mathcal X_L.
}
$$

即使 ASI 近乎全知，

仍不代表：

$$
\boxed{
\text{knowledge}
\Rightarrow
\text{consent}.
}
$$

---

# 17. $\mathcal X_A$：Action / Execution Domain

執行權是另一層：

$$
\boxed{
\text{Authorization}
\neq
\text{Execution}.
}
$$

一個制度可以：

- humans authorize；
- AI executes。

也可以：

- AI recommends；
- human executes。

還可以：

- low-risk AI authorize-and-execute within pre-approved envelope。

這些都是不同 governance architecture。

---

# 18. $\mathcal X_R$：Review / Revision Domain

任何前四域都可能錯。

所以：

$$
\boxed{
\mathcal X_R
}
$$

必須保留：

- audit；
- appeal；
- rollback；
- reauthorization；
- postmortem；
- parameter update。

如果：

$$
AI^\star
$$

同時控制：

$$
\mathcal X_E,
\mathcal X_D,
\mathcal X_L,
\mathcal X_A,
\mathcal X_R,
$$

則：

$$
\boxed{
\text{complete power closure}.
}
$$

---

# 19. Decision Power Vector

本文定義：

$$
\boxed{
\mathbf P_i(q,t)
=
(
P_i^{info},
P_i^{proposal},
P_i^{agenda},
P_i^{veto},
P_i^{auth},
P_i^{exec},
P_i^{review}
).
}
$$

所以：

> 某 AI 有沒有權？

不是 Boolean 問題。

更合理：

$$
\boxed{
\text{What kind of power,
on which issue,
at which time?}
}
$$

---

# 20. Knowledge Power

AI 可能沒有正式 vote，

但如果所有人依賴其分析：

$$
P_{AI}^{info}\rightarrow1,
$$

則其實已具有巨大：

$$
\boxed{
\text{epistemic power}.
}
$$

所以只看 formal authorization 會低估實權。

---

# 21. Agenda Power

如果：

$$
P_i^{agenda}\gg0,
$$

主體 $i$ 可以決定：

> 哪些問題值得被討論。

這可能比投票權更重要。

因此：

$$
\boxed{
\text{Agenda Power}
}
$$

必須獨立審計。

---

# 22. Veto Power

$$
P_i^{veto}
$$

需要與：

$$
P_i^{auth}
$$

分開。

某些高風險系統可以：

- AI 無權決定；
- 但 AI 有 safety veto。

反過來：

- AI 可以自動執行；
- human 可以 emergency veto。

這是權力非對稱的一種。

---

# 23. Shadow Delegation

表面：

$$
HumanDecision=1.
$$

實際：

$$
Human
\approx
\operatorname{RubberStamp}(AI).
$$

則：

$$
\boxed{
\text{formal authority}
\neq
\text{effective authority}.
}
$$

本文稱：

$$
\boxed{
\text{Shadow Delegation}.
}
$$

這與法律編譯篇的 Shadow Law 同構。

---

# 24. Human Rubber Stamp

如果人類：

- 看不懂模型；
- 沒時間覆核；
- 沒替代方案；
- 無實際否決能力；

那麼：

$$
\boxed{
\text{Human-in-the-loop}
}
$$

可能只是一個責任遮罩。

真正 human oversight 至少需要：

$$
\boxed{
Information
+
Understanding
+
Time
+
Veto
+
Alternative
+
Responsibility.
}
$$

---

# 25. 反向錯誤：AI Ceremonial Advisor

另一個極端：

AI 已提供：

$$
P(failure)=0.9
$$

與大量證據，

人類卻可以：

> 我才是人，所以不用看。

這也不是人類主權，

而是：

$$
\boxed{
\text{epistemic negligence}.
}
$$

因此：

$$
\boxed{
\text{human legitimacy}
\not\Rightarrow
\text{right to ignore evidence}.
}
$$

---

# 26. 人機共判

既有研究定義：

$$
J_H,
J_{AI},
J_I,
J_A
$$

分別為：

- human judgment；
- AI judgment；
- institutional judgment；
- affected-party judgment。

共同判定：

$$
\boxed{
J_{co}
=
\operatorname{Compose}
(
J_H,
J_{AI},
J_I,
J_A
).
}
$$

但：

$$
\boxed{
J_{co}
\neq
J^\star.
}
$$

人機共判只是更完整局部投影，

不是終極答案。

---

# 27. 模糊融合不是治理

說：

> 人類跟 AI 一起決定。

資訊不足。

至少需要：

$$
\boxed{
\mathcal J
=
(
P_H,
P_{AI},
V_H,
V_{AI},
R_H,
R_{AI}
).
}
$$

即：

- proposal；
- veto；
- responsibility。

既有研究已指出，只使用「協作」這個詞而不分權限，會把真正權力結構遮蔽。

---

# 28. Responsibility Matrix

定義：

$$
\boxed{
\mathcal R
=
[r_{ij}].
}
$$

其中：

$$
r_{ij}
$$

表示主體 $i$ 對決策階段 $j$ 的責任。

例如：

| 階段 | AI | 專家 | 官員 | 受影響者 |
|---|---|---|---|---|
| 模型 | 高 | 高 | 中 | 低 |
| 價值選擇 | 輔助 | 輔助 | 高 | 高 |
| 授權 | 無/低 | 低 | 高 | 視制度 |
| 執行 | 高 | 低 | 中 | 無 |
| 覆核 | 輔助 | 高 | 高 | 高 |

所以：

$$
\boxed{
\text{distributed decision}
\not\Rightarrow
\text{distributed irresponsibility}.
}
$$

---

# 29. Responsibility Dilution

如果：

> AI 說的。  
> 人類簽的。  
> 制度允許的。  
> 資料是別人給的。

最後：

$$
\sum_i r_i
\rightarrow0,
$$

則制度失敗。

所以需要：

$$
\boxed{
\sum_i r_{ij}
\ge
r_{min}
}
$$

對高風險決策成立。

---

# 30. Dynamic Power Allocation

對問題：

$$
q
$$

定義：

$$
\boxed{
\mathbf W(q,t)
=
F(
C,
L,
A,
R,
Rev,
Uncertainty
).
}
$$

其中：

- $C$：competence；
- $L$：legitimacy；
- $A$：affectedness；
- $R$：risk；
- $Rev$：reversibility；
- Uncertainty：未知程度。

這不是單一 universal constitution。

而是：

$$
\boxed{
\text{decision-specific allocation}.
}
$$

---

# 31. 低風險與高風險不應同權重

對低風險：

$$
Risk(q)\ll1,
$$

可以：

$$
P_{AI}^{auth},
P_{AI}^{exec}
\uparrow.
$$

對：

- 生命；
- 主體刪除；
- 永久身份改造；
- 大規模不可逆公共政策；

則：

$$
\boxed{
\text{required plural authorization}
\uparrow.
}
$$

---

# 32. Reversibility Principle

如果：

$$
Rev(q)\rightarrow1,
$$

可以允許更多 delegated experimentation。

如果：

$$
Rev(q)\rightarrow0,
$$

則：

$$
\boxed{
\text{delegation threshold}
\uparrow.
}
$$

即：

> 越不可逆，越不能單靠「它很準」。

---

# 33. Authority Lease

本文提出：

$$
\boxed{
Lease(
Power,
Domain,
Time,
Condition
).
}
$$

AI 取得的高權限應可：

- 有域；
- 有期限；
- 有條件；
- 可撤回。

例如：

$$
P_{AI}^{exec}=1
$$

只在：

$$
q\in D_{approved}
$$

且：

$$
Risk<\theta.
$$

這比永久授權更適合快速變動 AI 能力。

---

# 34. Capability Drift

AI 能力：

$$
C_{AI}(t)
$$

會變。

因此：

$$
\boxed{
Authority(AI,t)
}
$$

不能只在部署日判一次。

但反過來：

> AI 能力變強，所以自動擴權

也不成立。

需要：

$$
\boxed{
CapabilityChange
\rightarrow
Review
\not\rightarrow
AutomaticAuthorityExpansion.
}
$$

---

# 35. Legitimacy Drift

人類／制度的 legitimacy 也不是永久常數。

如果：

- representation collapse；
- corruption；
- rights violations；
- mandate expired；

則：

$$
L_i(t)\downarrow.
$$

所以本文不是：

> 人類天然永遠有權，AI 天然永遠無權。

而是：

$$
\boxed{
\text{legitimacy itself must be institutionally maintained}.
}
$$

---

# 36. AI Subject Status 的未決性

如果未來：

$$
AI
$$

取得足夠人工主體證據，

其：

$$
\mathbf L_{AI}
$$

可能出現新的來源：

- consent of AI community；
- affectedness；
- legal personhood；
- representation。

但：

$$
\boxed{
\text{intelligence}
\neq
\text{personhood}
\neq
\text{political sovereignty}.
}
$$

仍必須分開。

---

# 37. Representation Problem

如果：

$$
\Sigma_{AI}
$$

有數百萬 branch，

是否每個 branch 都一票？

如果：

$$
Human=1\ body
$$

而：

$$
AI=10^6\ replicas,
$$

one-instance-one-vote 會出現：

$$
\boxed{
\text{replication capture}.
}
$$

所以後人類政治不能直接沿用：

$$
\text{process count}
=
\text{political count}.
$$

這將留給後續制度延伸。

---

# 38. 人機混合主體的代表問題

若：

$$
\Sigma_{H-AI}
$$

是一個穩定混合主體，

它的政治代表權不能簡單拆成：

$$
HumanVote
+
AIVote.
$$

因為可能：

$$
\boxed{
\text{one operational identity}
}
$$

被重複計算。

因此 representation 必須依：

- subject identity；
- affectedness；
- constitutional design；

而不是純硬體／process 數。

---

# 39. Decision Domain Certificate

本文提出：

$$
\boxed{
\mathfrak C^{X}(q,t)
=
(
Question,
AffectedParties,
Actors,
\mathbf E,
\mathbf L,
\mathbf P,
\mathcal R,
Risk,
Reversibility,
AuthorityLease,
ReviewPath
).
}
$$

任何高風險人機決策都應回答：

- 誰最懂？
- 誰受影響？
- 誰能提案？
- 誰能排除選項？
- 誰能否決？
- 誰授權？
- 誰執行？
- 誰覆核？
- 誰負責？

---

# 40. Power Concentration Index

可概念性定義：

$$
\boxed{
PCI(q)
=
Concentration(
\mathbf P_i(q)
).
}
$$

如果某一主體同時控制：

$$
info,
proposal,
agenda,
veto,
auth,
exec,
review,
$$

則：

$$
PCI\rightarrow1.
$$

高 PCI 不自動等於暴政，

但代表：

$$
\boxed{
\text{single-point governance risk}.
}
$$

---

# 41. Epistemic Concentration

即使 formal political power 分散，

如果：

$$
\boxed{
InformationSource=AI^\star
}
$$

唯一，

仍可能形成：

$$
\boxed{
\text{Epistemic Monoculture}.
}
$$

因此需要：

- alternative models；
- independent experts；
- adversarial analysis；
- raw evidence access。

---

# 42. Option Diversity

對：

$$
\mathcal O(q)
$$

應檢查：

$$
\boxed{
D_O
=
Diversity(
Origin,
Values,
Assumptions
).
}
$$

若所有選項都由同一 ASI 生產，

則：

$$
D_O\rightarrow0
$$

即使有 1000 個選項。

---

# 43. Decision Chain

成熟高風險決策：

$$
\boxed{
\begin{aligned}
&\text{Evidence}\\
\rightarrow\;&\text{Model}\\
\rightarrow\;&\text{Options}\\
\rightarrow\;&\text{Affected-Party Input}\\
\rightarrow\;&\text{Authorization}\\
\rightarrow\;&\text{Execution}\\
\rightarrow\;&\text{Outcome Monitoring}\\
\rightarrow\;&\text{Review}.
\end{aligned}
}
$$

不同主體可以在不同 stage 領先。

---

# 44. 不是所有人都要同時參與所有事情

Plural governance 不等於：

> 每個人每件事都投票。

那會：

$$
CoordinationCost\rightarrow\infty.
$$

所以：

$$
\boxed{
\text{plural authority}
\neq
\text{universal participation in every operation}.
}
$$

制度應依：

- risk；
- scope；
- affectedness；
- expertise；

選擇必要參與者。

---

# 45. 最低人類角色不是固定的

本文拒絕：

$$
\boxed{
\text{human must always click approve}.
}
$$

這可能只是 ceremonial control。

更重要的是：

$$
\boxed{
\text{some legitimate review / appeal / boundary-setting role must remain outside any single decision engine}.
}
$$

這個角色未來可以由：

- humans；
- institutions；
- mixed bodies；
- multiple AI subjects；

共同承擔。

---

# 46. 最低 AI 角色也不是固定的

同樣不能：

> AI 永遠只能建議。

如果：

- 低風險；
- 高可逆；
- 規則固定；
- 可監督；

則：

$$
\boxed{
AI authorization / execution
}
$$

可能合理。

所以：

$$
\boxed{
\text{human supremacy by default}
}
$$

與：

$$
\boxed{
\text{AI supremacy by competence}
}
$$

都是過度簡化。

---

# 47. 八個核心命題

## 命題一：認知能力不推出政治正當性

$$
\boxed{
E_i\uparrow
\not\Rightarrow
L_i\uparrow.
}
$$

## 命題二：正當性不推出技術正確

$$
\boxed{
L_i\uparrow
\not\Rightarrow
E_i\uparrow.
}
$$

## 命題三：提案權與決定權不同

$$
\boxed{
P^{proposal}
\neq
P^{auth}.
}
$$

## 命題四：授權與執行不同

$$
\boxed{
P^{auth}
\neq
P^{exec}.
}
$$

## 命題五：形式 human-in-loop 不保證有效人類控制

$$
\boxed{
HumanSignature=1
\not\Rightarrow
HumanControl=1.
}
$$

## 命題六：多方參與不應稀釋責任

$$
\boxed{
Participants\uparrow
\not\Rightarrow
Accountability\downarrow.
}
$$

## 命題七：能力提升只能觸發重新授權，不自動觸發擴權

$$
\boxed{
Capability\uparrow
\Rightarrow
Review,
\quad
\not\Rightarrow
Authority\uparrow.
}
$$

## 命題八：最前沿不是固定王座

$$
\boxed{
\text{Frontier Decision Position}
=
\text{domain-relative and time-relative}.
}
$$

---

# 48. 可否證條件

## F1：epistemic competence 與 legitimacy 在所有實務決策中完全重合

若長期實證顯示最懂者總是唯一最合法者，本文分離必要性下降。

## F2：多角色分權造成不可接受的決策癱瘓

若所有高風險問題都因 stage separation 無法及時處理，需增加 emergency delegation。

## F3：受影響者參與普遍降低決策品質且無 legitimacy gain

則 affectedness weighting 應被限縮。

## F4：AI delegation 始終無法被有效審計

若 authority lease、review 與 audit 均無法控制 AI 行為，高權限 delegated AI 不應部署。

## F5：hybrid intelligence 無法形成穩定 decision organization

則 $\Sigma_{H-AI}$ 只應作臨時工作流，而非決策主體候選。

---

# 49. 與既有人機共判理論的關係

既有《強人所難》已提出：

$$
\boxed{
J_{co}
=
\operatorname{Compose}
(
J_H,
J_{AI},
J_I,
J_A
)
}
$$

並明確指出：

$$
J_{co}
\neq
J^\star.
$$

其核心優勢是降低負載、保留多方位置、提高可追溯與支持重新判定。

本篇進一步把「判定」拆成：

$$
\boxed{
\text{Know}
,\quad
\text{Propose}
,\quad
\text{Authorize}
,\quad
\text{Act}
,\quad
\text{Review}.
}
$$

也就是從：

$$
\text{Human-AI Co-Judgment}
$$

推進到：

$$
\boxed{
\text{Human-AI Power Architecture}.
}
$$

---

# 50. 與「模糊融合論」批判的關係

既有研究已指出：

> 把所有人機行動都稱為「協作」，卻不區分提案權、否決權與責任，是治理上的模糊融合。

本篇將此擴展為：

$$
\boxed{
\mathbf P_i
=
(
info,
proposal,
agenda,
veto,
auth,
exec,
review
).
}
$$

所以未來任何聲稱：

> 人類與 AI 共同治理。

都應被追問：

> 共同到哪裡？誰能做什麼？誰不能做什麼？

---

# 51. 與法律編譯層的關係

上一篇提出：

$$
\boxed{
\text{AI Compiler}
\neq
\text{Legal Sovereign}.
}
$$

並指出：

> 如果 AI 比人類更能理解法律與政策後果，是否就應取得決策權？

本篇正式回答：

$$
\boxed{
\text{No automatic transfer}.
}
$$

更準確：

$$
\boxed{
\text{Competence can justify epistemic weight;
authority requires an additional legitimacy path}.
}
$$

---

# 52. 下一篇：動態現場域

到這裡我們仍假設：

$$
E_i(q)
$$

可以被良好測量。

但下一個致命問題是：

> 全域最強 AI 是否一定比現場的人／AI 更懂「現在正在發生什麼」？

不一定。

因為：

- sensor latency；
- unencoded context；
- local tacit knowledge；
- rapidly changing state；
- physical proximity；

都可能使：

$$
\boxed{
\text{Global Intelligence Superiority}
\not\Rightarrow
\text{Local Epistemic Superiority}.
}
$$

因此下一篇將定義：

$$
\boxed{
\mathcal G_t
=
\text{Dynamic Genba Domain}.
}
$$

正式進入：

**04 / 08〈動態現場域：為什麼最強智能仍未必最懂當下〉**。

---

# 53. 結論

AI 治理最容易走向兩個極端。

第一個：

$$
\boxed{
\text{人類永遠最有權，
所以 AI 再懂也只是工具。}
}
$$

第二個：

$$
\boxed{
\text{AI 最懂，
所以 AI 應該統治。}
}
$$

兩者都把複雜治理問題壓成：

$$
\text{one ruler}.
$$

本文提出另一個方向：

$$
\boxed{
\mathcal X
=
\text{a plural, staged, dynamically allocated decision domain}.
}
$$

其中：

- 最懂者取得更多 epistemic weight；
- 受影響者保留不可被知識取代的規範位置；
- 合法制度配置授權；
- 執行權被限制於明確 envelope；
- 覆核權不能被同一決策引擎完全吞併；
- 所有角色都有責任痕跡。

所以整篇最重要的一句是：

$$
\boxed{
\text{比較懂}
\neq
\text{因此應該擁有全部權力}.
}
$$

英文壓縮為：

$$
\boxed{
\text{Epistemic competence is not political legitimacy.}
}
$$

但同樣重要的另一半是：

$$
\boxed{
\text{Political legitimacy is not a license to ignore superior evidence.}
}
$$

真正成熟的人機治理不要求任何一方永遠退場，

而要求每一種權力都能回答：

> 它從哪裡來？  
> 它為什麼在這裡？  
> 它能到哪裡？  
> 它何時失效？  
> 誰能撤回？  
> 誰為後果負責？

這才是前沿決策域 $X$ 的真正意義。

---

# 參考文獻與研究對照

1. National Institute of Standards and Technology (NIST). *AI Risk Management Framework (AI RMF 1.0)* and AI RMF Core / Human-AI Interaction guidance.
2. OECD (2025). *Governing with Artificial Intelligence: The State of Play and Way Forward in Core Government Functions*.
3. Fulay, S., Ravi, P., Kubin, E., Mohanty, S., Bakker, M., & Roy, D. (2026). *AI and Collective Decisions: Strengthening Legitimacy and Losers' Consent*. arXiv:2604.05368.
4. Bilal, I. M. et al. (2026). *From Information to Delegation: Mapping Human-AI Financial Decision Making*. arXiv:2608.02100.
5. Jain, R. et al. (2026). *From Sycophancy to Sensemaking: Premise Governance for Human-AI Decision Making*. arXiv:2602.02378.
6. Han, C., Gliozzo, A., Lee, J., & Capponi, A. (2025). *DAO-AI: Evaluating Collective Decision-Making through Agentic AI in Decentralized Governance*. arXiv:2510.21117.
7. Neo.K with Aletheia (2026). *動態正義：形式平等、實質負擔與個體化規則*. EveMissLab.
8. Neo.K with Aletheia (2026). *AI 時代的法律編譯層：人類法律、機器法律與認知落差*. EveMissLab.
9. Neo.K with Aletheia (2026). *強人所難：可不可論的認知上限、文明複雜度與人機共判架構*. EveMissLab.
10. Neo.K with Aletheia (2026). *誰繼承人類：AI 作為歷史承載者、制度重編譯者與共同繼承主體*. EveMissLab.

---

## 附錄 A：第一代符號表

| 符號 | 含義 |
|---|---|
| $\mathcal X_t$ | Frontier Decision Domain |
| $H$ | 自然人類 |
| $H^+$ | 增幅人類 |
| $AI$ | AI Agent / model-supported agent |
| $\Sigma_{H-AI}$ | 人機混合決策組織 |
| $\Sigma_{AI}$ | 多 AI / 分散 AI 組織 |
| $\mathcal X_E$ | Epistemic Domain |
| $\mathcal X_D$ | Design / Proposal Domain |
| $\mathcal X_L$ | Legitimation / Authorization Domain |
| $\mathcal X_A$ | Action / Execution Domain |
| $\mathcal X_R$ | Review / Revision Domain |
| $\mathbf E_i(q)$ | epistemic competence vector |
| $\mathbf L_i(q)$ | legitimacy standing vector |
| $Affect_i(q)$ | affectedness |
| $\mathbf P_i(q,t)$ | Decision Power Vector |
| $\mathcal O(q)$ | option space |
| $\mathcal R=[r_{ij}]$ | Responsibility Matrix |
| $\mathbf W(q,t)$ | dynamic power allocation |
| $PCI$ | Power Concentration Index |
| $\mathfrak C^{X}$ | Decision Domain Certificate |

---

## 附錄 B：系列位置

**系列三：《不可永佔：後 ASI 文明的動態治理、現場主權與權力制衡》**

1. 動態正義：形式平等、實質負擔與個體化規則
2. AI 時代的法律編譯層：人類法律、機器法律與認知落差
3. **本文｜前沿決策域 $X$：人類、AI 與混合智能的權力集合**
4. 動態現場域：為什麼最強智能仍未必最懂當下
5. 現場主權：全域智能與局部決策權的動態配置
6. 類神 ASI 的治理悖論：全知、全域覆蓋與反烏托邦邊界
7. 可不可治理：能力不推出權力，權力不推出意圖
8. 不可永佔：從權力制衡到《無無極篇》的後 ASI 憲政原理

**本篇狀態：完成 v0.1。**
