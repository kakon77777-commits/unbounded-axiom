# AI 不必成為 AGI，也可以先讓大量人類工作失去經濟必要性：從可靠自主勞動門檻到任務級相變

## AI Does Not Need to Become AGI Before Human Labor Loses Economic Necessity: From the Reliable Autonomous Labor Threshold to Task-Level Discontinuity

**系列**：工作、時間主權與存在價值，第 5 篇／共 7 篇＋1 篇番外  
**系列英文名**：Work, Time Sovereignty, and Existential Value  
**文件編號**：EML-WTSV-2026-05-v0.1  
**作者**：Neo.K with Aletheia（GPT-5.6 Sol）  
**機構**：EveMissLab／一言諾科技有限公司  
**版本**：v0.1  
**日期**：2026-09-03  
**性質**：AI Labor Economics／Agentic Systems／Temporal Economics／Task-Based Automation／Post-Labor Civilization  
**狀態**：Public Theory Draft  
**直接前置**：EML-WTSV-2026-01 至 04；EML-CLGI-2026-03《可靠自主勞動門檻：為什麼經濟相變不必等待 AGI》；《Agentic Organization 的時間經濟學》；《AI 時間槓桿的多重估值》  
**後續接口**：Paper 06「時間主權」；Paper 07「後勞動價值重構」

---

## 生成、認識論與規範邊界聲明

本文是一篇 AI 輔助生成的理論研究稿。

本文不預測某個確定年份會出現 AGI，也不主張當前 AI 已可全面取代所有人類工作，更不把模型 benchmark、聊天介面中的單次成功、Agent demo 或廠商使用資料直接等同整體經濟自動化。

本文研究的是一個較窄而且可操作的命題：

> 經濟體系不需要先同意某套 AI 已經是「AGI」，才可能在大量具體任務中發現：由 AI／Agent 完成已經比由人類持續完成更便宜、更快、更可平行、更容易複製，而且其可靠性與治理成本已低到可進入正式生產流程。

本文因此沿用既有區分：

$$
\boxed{
\text{AGI Threshold}
\neq
\text{Economic Substitution Threshold}.
}
$$

同時保留另一個重要邊界：

$$
\boxed{
\text{Task Exposure}
\neq
\text{Task Substitution}
\neq
\text{Job Substitution}
\neq
\text{Human Redundancy}.
}
$$

本文不把經濟替代直接推成存在價值判斷。恰恰相反，本篇的任務是證明：如果經濟替代可以在 AGI 哲學爭論結束之前就發生，那麼前四篇對「工作不構成人的存在資格」的價值準備，就不能等到大規模失業發生後才開始。

---

# 摘要

AI 與勞動市場的公共討論經常被一個單一門檻支配：

$$
\text{Current AI}
\rightarrow
\text{AGI}
\rightarrow
\text{Mass Automation}.
$$

這條敘事容易讓社會形成錯誤安全感：只要我們尚未公認某個系統達到 AGI，就似乎還沒有真正進入勞動相變。

但企業購買的從來不是「哲學上完整的人類等價智能」。企業購買的是可驗收的任務完成：

$$
\text{acceptable quality}
+
\text{reliability}
+
\text{latency}
+
\text{accountability}
+
\text{cost efficiency}.
$$

因此，AI 可能尚未跨越一般認知意義上的：

$$
\Theta_{\mathrm{AGI}},
$$

卻已在某些任務域跨過：

$$
\Theta_{\mathrm{econ}}.
$$

本文沿用 EML-CLGI-2026-03 提出的「可靠自主勞動門檻」（Reliable Autonomous Labor Threshold, RAL）：

$$
\Theta_{\mathrm{RAL}}
=
\left\{
Q_A\ge Q_{\min},
\;
U_A\le\epsilon,
\;
\Gamma_A\ge\Gamma_{\min},
\;
T_A^{\mathrm{aut}}\ge T_{\min},
\;
\rho_H\le\rho_H^{\max},
\;
C_A^{*}<C_H^{*}
\right\},
$$

其中：

- $Q_A$：Agent 產出品質；
- $U_A$：未檢出且不可恢復錯誤率；
- $\Gamma_A$：錯誤恢復能力；
- $T_A^{\mathrm{aut}}$：可維持自主工作的曆時；
- $\rho_H$：人類治理／介入密度；
- $C_A^{*}$ 、 $C_H^{*}$：風險、治理與驗證調整後的 AI 與人類總成本。

對職業 $J$，本文進一步定義「RAL 任務滲透率」：

$$
\phi_J(t)
=
\sum_{k=1}^{n}
w_k
\mathbf 1
\left[
T_k
\text{ has crossed }
\Theta_{\mathrm{RAL}}
\right],
$$

其中 $w_k$ 是任務 $T_k$ 在職業中的時間、價值或必要性權重。

這使勞動相變不再需要被理解為：

$$
\text{job exists}
\rightarrow
\text{job disappears}.
$$

更可能是：

$$
\text{task substitution}
\rightarrow
\text{job recomposition}
\rightarrow
\text{wage／entry／headcount pressure}
\rightarrow
\text{possible occupational contraction}.
$$

2025 年 ILO–NASK 的全球指標以近三萬個任務為基礎，估計全球約四分之一就業位於某種程度的生成式 AI 暴露職業，但同時判斷在當前條件下，多數職業更可能先被轉型而不是整體消失。這正支持「任務先變、職業後變」的分析框架。

2026 年 METR 的 Time Horizon 研究則顯示，前沿 Agent 在軟體工程、機器學習與資安等清楚定義的任務上，可成功處理的人類等價任務跨度持續快速上升。METR 同時明確警告：time horizon 不是「AI 可以連續自主工作多久」，也不能直接推成「可以自動化所有工作」；其測試主要集中在軟體相關任務，而且超過約 16 小時的估計目前可靠性有限。這些限制反而說明 RAL 所需要的不是單一 benchmark，而是品質、錯誤、治理、成本與任務域共同評估。

Anthropic 2026 年 Economic Index 的供應商側使用資料又提供另一個訊號：部分 coding 類任務正從對話介面的協作使用移向 API 中更自動化、較 directive 的工作流；但同一份報告也發現高經驗使用者常更傾向協作與迭代，而不是簡單全自動化。這提醒我們，AI 的經濟影響可以同時沿著：

$$
\text{automation}
$$

與：

$$
\text{augmentation}
$$

兩條路徑前進。

本文因此拒絕「AI 會一次性搶走所有工作」與「AI 只會永遠當輔助工具」兩種極端。

真正需要觀察的是：

$$
\boxed{
\text{How fast does }
\phi_J(t)
\text{ rise, and what happens to human time, income, bargaining power, and identity as it rises?}
}
$$

最後，本文把勞動經濟問題重新接回本系列的價值問題：

$$
\boxed{
\text{Economic Redundancy}
\neq
\text{Existential Redundancy}.
}
$$

如果某些人類工作真的逐漸失去經濟必要性，文明真正應解除的是「必須重新發明工作來證明人有價值」的衝動，而不是否認技術替代正在發生。

**關鍵詞**：AGI、可靠自主勞動門檻、RAL、Agent、任務替代、職業重組、AI 勞動、經濟替代、時間經濟學、後勞動文明

---

# 1. 為什麼「等 AGI 再討論」可能太晚

很多公共討論默認：

$$
\Theta_{\mathrm{AGI}}
<
\Theta_{\mathrm{automation}}.
$$

也就是先有 AGI，才有大規模經濟自動化。

但企業根本不需要先回答：

> 這個系統是否具有完整人類通用智能？

企業真正問的是：

> 這個流程交給它，能不能穩定完成？

所以：

$$
\Theta_{\mathrm{econ}}(T)
$$

是 task-relative。

對任務 $T_a$：

$$
\Theta_{\mathrm{econ}}(T_a)
<
\Theta_{\mathrm{AGI}}
$$

完全可能。

對另一任務 $T_b$：

$$
\Theta_{\mathrm{econ}}(T_b)
>
\Theta_{\mathrm{AGI}}
$$

也可能。

例如高度具身、法律責任重、需要深厚組織脈絡或高信任關係的任務，即使模型智力很高，也可能很晚才達到經濟可替代。

因此：

$$
\boxed{
\text{AGI is not a universal labor-market switch}.
}
$$

---

# 2. 經濟替代的門檻是「夠好」，不是「世界最強」

假設：

$$
Q_{\mathrm{human\ elite}}
=
0.98,
$$

$$
Q_A
=
0.84,
$$

而任務真正要求：

$$
Q_{\min}
=
0.75.
$$

則：

$$
Q_A
<
Q_{\mathrm{human\ elite}}
$$

與：

$$
Q_A
\ge
Q_{\min}
$$

可以同時成立。

企業沒有理由要求每一封信、每一份報表、每一段程式、每一個客服回覆都達到全球頂尖人類品質。

大量工作真正的條件是：

$$
\boxed{
Q
\ge
Q_{\min}.
}
$$

跨過品質門檻後，競爭才進入：

$$
\text{cost},
\quad
\text{latency},
\quad
\text{availability},
\quad
\text{scalability},
\quad
\text{risk}.
$$

這就是為什麼：

$$
\text{AI is not better than the best human}
$$

不能作為：

$$
\text{AI cannot substitute labor}
$$

的充分論證。

---

# 3. 「能做一次」與「可進入生產」仍然相差很遠

相反方向也必須封住。

一個 AI demo 顯示：

$$
P(\text{success})>0
$$

不代表它已跨越勞動門檻。

生產系統真正需要：

$$
P(\text{reliable success})
\ge
r_{\min}.
$$

並且錯誤不能只是：

$$
\text{retry until lucky}.
$$

因為真實工作有：

- 持續狀態；
- 外部客戶；
- 財務後果；
- 安全責任；
- 法律責任；
- 資料污染；
- 版本與歷史；
- 上下游依賴。

所以：

$$
\boxed{
\text{Capability Demonstration}
\neq
\text{Reliable Production}.
}
$$

---

# 4. RAL：可靠自主勞動門檻

沿用既有框架：

$$
\boxed{
\Theta_{\mathrm{RAL}}
=
\left\{
Q_A\ge Q_{\min},
\;
U_A\le\epsilon,
\;
\Gamma_A\ge\Gamma_{\min},
\;
T_A^{\mathrm{aut}}\ge T_{\min},
\;
\rho_H\le\rho_H^{\max},
\;
C_A^{*}<C_H^{*}
\right\}.
}
$$

這六個條件缺一不可。

如果品質很高，但：

$$
\rho_H\approx1,
$$

也就是每一步都需要人類盯著，那更像高能力工具，而不是自主勞動單元。

如果成本很低，但：

$$
U_A
$$

很高，產出的未檢出錯誤會污染長期系統，也不能視為廉價替代。

如果 Agent 可以長時間運行，但無法恢復：

$$
\Gamma_A\approx0,
$$

一個錯誤就可能讓整個工作流偏離。

因此 RAL 不是智力分數。

它是一個：

$$
\boxed{
\text{production admissibility condition}.
}
$$

---

# 5. 人類介入密度可能比「模型智商」更重要

令：

$$
\rho_H
=
\frac{
T_H^{governance}
}{
T_A^{effective\ work}
+
T_H^{governance}
}.
$$

若 Agent 工作一小時，需要人類審查五十分鐘：

$$
\rho_H
$$

很高。

若 Agent 可以工作八小時，人類只需要在高風險節點審核十五分鐘：

$$
\rho_H
$$

就大幅下降。

從組織成本看，這可能比 benchmark 多幾分重要得多。

因此：

$$
\boxed{
\text{Autonomy}
\neq
\text{absence of humans}.
}
$$

更接近：

$$
\boxed{
\text{high effective delegated work per unit human governance time}.
}
$$

---

# 6. 委任槓桿：真正被 AI 放大的首先是「人類時間」

既有 Agentic Organization 時間經濟學定義：

$$
\Lambda_D
=
\frac{
V_{\mathrm{effective\ delegated\ work}}
}{
T_H^{gov}+\epsilon
}.
$$

當：

$$
\Lambda_D\uparrow,
$$

表示每一單位人類治理時間可以控制更多有效智能勞動。

這使 AI 勞動的核心不只是：

$$
\text{machine replaces person}.
$$

也可以是：

$$
1H
\rightarrow
10A,
$$

甚至：

$$
1H
\rightarrow
100A,
$$

其中 $H$ 是一個人類治理者， $A$ 是可平行 Agent。

所以在就業數量正式下降以前，組織內部就可能先出現：

$$
\boxed{
\text{human coordination density}
\downarrow.
}
$$

---

# 7. 24／7 與平行度會改變「一個勞動單元」的概念

傳統人類勞動單元受限於：

$$
24h,
$$

睡眠、疲勞、時區、排班、訓練與協調成本。

AI 勞動則可能具有：

$$
T_A^{available}
\approx
24/7,
$$

以及：

$$
N_A
\gg1.
$$

因此，單純比較：

$$
Q_A
$$

與：

$$
Q_H
$$

是不夠的。

更完整的有效產能可以寫成：

$$
P_A^{eff}
=
Q_A
\cdot
R_A
\cdot
T_A
\cdot
N_A
\cdot
(1-\rho_H)
\cdot
(1-\mathrm{Risk}_A),
$$

其中 $R_A$ 表示可靠完成率。

即使：

$$
Q_A<Q_H,
$$

仍可能：

$$
P_A^{eff}
\gg
P_H^{eff}.
$$

這就是經濟替代與「誰比較聰明」不同的地方。

---

# 8. 任務才是更合理的基本單位

勞動經濟學早已發展 task-based automation framework。

Acemoglu 與 Restrepo 將自動化描述為機器接管原本由勞動執行的任務，而不是把技術只視為對所有勞動的均勻增強。

令職業：

$$
J
=
\left\{
T_1,
T_2,
\ldots,
T_n
\right\}.
$$

AI 很可能先跨越：

$$
T_2,
T_4,
T_7,
$$

卻仍無法可靠完成：

$$
T_1,
T_3,
T_5.
$$

因此：

$$
\boxed{
\text{Task Substitution}
\rightarrow
\text{Job Recomposition}
}
$$

通常比：

$$
\text{AI suddenly deletes Job }J
$$

更合理。

---

# 9. RAL 任務滲透率

為了把 task-level 門檻接回 occupation，本文定義：

$$
\boxed{
\phi_J(t)
=
\sum_{k=1}^{n}
w_k
\mathbf 1
\left[
T_k
\text{ has crossed }
\Theta_{\mathrm{RAL}}
\right].
}
$$

其中：

$$
\sum_{k=1}^{n}w_k=1.
$$

 $w_k$ 可以依研究目的代表：

- 時間比例；
- 工資價值；
- 任務必要性；
- 收益貢獻；
- 組織瓶頸權重。

若：

$$
\phi_J=0.2,
$$

不代表職業消失。

若：

$$
\phi_J=0.8,
$$

也仍不必然消失。

但：

$$
\phi_J\uparrow
$$

通常意味著：

- 工作內容被重新組合；
- 同樣產出需要更少人；
- 入門工作減少；
- 監督與整合任務比例上升；
- 薪資議價可能改變；
- 企業內部職能重新分層。

---

# 10. 2025 ILO 的全球任務級證據支持「先轉型、後替代」

ILO 與 NASK 在 2025 年更新生成式 AI 職業暴露指標，使用近三萬個任務的分類基礎，並結合人工評估、專家判斷與 AI 預測。

其全球估計指出：

$$
\text{約四分之一全球就業}
$$

位於具有某種生成式 AI 暴露的職業中。

但最高暴露層只占全球就業的一小部分，而且 ILO 明確判斷：

> 在當前條件下，大多數工作更可能先被改造，而不是直接變得多餘。

這與本文的：

$$
\phi_J(t)
$$

完全一致。

暴露代表：

$$
\exists T_k
\text{ 可受 AI 影響},
$$

不是：

$$
J
\rightarrow0.
$$

---

# 11. 暴露不是替代率

這個區分值得形式化。

令：

$$
X_J
=
\text{AI exposure of occupation }J.
$$

令：

$$
S_J
=
\text{actual substitution intensity}.
$$

則：

$$
\boxed{
X_J
\neq
S_J.
}
$$

即使：

$$
X_J\uparrow,
$$

若：

- 人類仍需大量驗證；
- 法律禁止全自動；
- 客戶偏好人類；
- 任務高度關係化；
- 實體環境難以操作；
- AI 錯誤成本太高；

則：

$$
S_J
$$

仍可能很低。

反過來，某些看似不驚人的任務只要高度標準化、低風險、可驗收、量大，實際替代可能很快。

---

# 12. METR 的 Time Horizon 告訴我們：任務「跨度」正在變長

METR 的 task-completion time horizon 不是 AI 自己連續運作多久。

它表示：

> 對一組任務而言，人類專家通常需要多少時間完成，而指定 Agent 在該難度區間可達到某一成功率。

例如 50% time horizon 表示：

$$
P_A(\text{success}\mid T_{human}=h_{50})
=
0.5.
$$

2026 年的資料仍顯示前沿模型在主要為軟體工程、機器學習與資安所構成的任務集上，time horizon 持續快速增長。

Microsoft Research 在 2026 年介紹 SentinelBench 時，將當時前沿 Agent 的 50% horizon 概括為已超過 16 小時的人類等價任務範圍。

這是一個重要訊號：

$$
\boxed{
\text{AI is moving from atomic tasks toward longer task chains}.
}
$$

---

# 13. 但 METR 自己也警告：16 小時不等於「會做一天任何工作」

METR 對 time horizon 的限制說得很清楚。

第一：

$$
\text{time horizon}
\neq
\text{literal autonomous runtime}.
$$

第二，其任務主要集中於：

$$
\text{software engineering}
+
\text{ML}
+
\text{cybersecurity}.
$$

第三：

$$
h>16\text{ hours}
$$

的估計，目前在任務集上可靠性有限。

第四，測試更接近：

> 一個低脈絡的新進人員／遠端承包者，在拿到明確任務後可以完成多少。

而不是：

> 一個在公司工作十年、掌握大量 tacit context 的資深員工能完成什麼。

所以：

$$
\boxed{
\text{longer benchmark horizon}
\not\Rightarrow
\text{full occupational autonomy}.
}
$$

這正好說明 RAL 需要加入：

$$
\rho_H,
\quad
U_A,
\quad
\Gamma_A,
\quad
C_A^{*}.
$$

---

# 14. 長程 Agent 的下一個問題是「世界會自己變」

傳統 benchmark 常假設：

$$
\text{environment changes}
\approx
\text{agent actions}.
$$

但真實工作並不是這樣。

客戶會回信。

伺服器會故障。

股票會動。

航班會改。

供應鏈會延遲。

同事會提交新版本。

外部 API 會失敗。

因此長期勞動 Agent 還需要：

$$
\text{monitoring},
\quad
\text{event handling},
\quad
\text{state persistence},
\quad
\text{replanning}.
$$

2026 年 Microsoft Research 的 SentinelBench 正是在測這類長期監測型 Agent。

所以：

$$
\boxed{
\text{long task completion}
\neq
\text{long-lived organizational agency}.
}
$$

但從經濟角度，這些能力一旦逐步成熟，會直接增加：

$$
T_A^{aut}
$$

並降低：

$$
\rho_H.
$$

---

# 15. Anthropic Economic Index：AI 使用正在從對話向工作流分化

Anthropic 2026 年 Economic Index 的資料不能代表整體經濟，但提供一個供應商側的實際使用窗口。

報告顯示：

- coding 仍是主要使用類別之一；
- coding 類工作部分從 Claude.ai 對話介面移向 API；
- API 中更容易出現 directive、較自動化的工作流；
- 高經驗使用者卻往往更常迭代、驗證與協作。

這說明：

$$
\boxed{
\text{AI diffusion}
\neq
\text{one-way march to full automation}.
}
$$

同一技術可以同時使：

$$
\text{automation}\uparrow
$$

與：

$$
\text{augmentation}\uparrow.
$$

真正的分化會依任務、使用者能力、組織流程與責任結構而不同。

---

# 16. 使用者能力本身也會改變 AI 替代門檻

如果有經驗的人類能更有效地：

- 拆任務；
- 提供上下文；
- 驗證；
- 發現錯誤；
- 決定何時升級模型；
- 建立可回復流程；

則：

$$
Q_A^{effective}
=
f
\left(
Q_{\mathrm{model}},
S_H,
\mathcal I,
\mathcal T
\right),
$$

其中：

- $S_H$：人類操作／治理技能；
- $\mathcal I$：基礎設施；
- $\mathcal T$：工具鏈。

所以經濟替代不是：

$$
\text{model release}
\rightarrow
\text{immediate labor substitution}.
$$

更接近：

$$
\text{model}
+
\text{workflow}
+
\text{learning}
+
\text{tooling}
+
\text{governance}
\rightarrow
\Theta_{\mathrm{RAL}}.
$$

---

# 17. 工作消失之前，headcount 可能先下降

假設原本一個部門需要：

$$
N_H=20.
$$

AI 導入後：

$$
\phi_J=0.5.
$$

這不一定讓：

$$
N_H\rightarrow0.
$$

但可能使：

$$
N_H
\rightarrow
12
$$

或：

$$
N_H
\rightarrow
8,
$$

其餘人負責：

- 高風險審查；
- 客戶關係；
- 例外處理；
- 架構；
- 法律責任；
- 跨部門協調。

所以：

$$
\boxed{
\text{job title survival}
\neq
\text{employment volume survival}.
}
$$

職稱仍存在，並不代表勞動需求沒有下降。

---

# 18. 薪資與議價能力可能比「失業」更早變化

若同一任務有大量可替代供給：

$$
S_A(T)\uparrow,
$$

人類在該任務上的稀缺租：

$$
R_H^{scarcity}(T)
$$

可能下降。

因此勞動相變可以先表現為：

$$
W_H^{wage}
\downarrow
$$

而不是：

$$
Employment_H
\rightarrow0.
$$

也就是：

$$
\boxed{
\text{economic redundancy can arrive as bargaining-power erosion before unemployment}.
}
$$

這對工作價值心理尤其重要。

因為人可能仍在工作，卻感受到：

> 我以前被需要的能力突然不值錢了。

這已足以衝擊身份。

---

# 19. 最容易被忽略的是「入門梯子」

很多職業不是直接從：

$$
\text{novice}
\rightarrow
\text{expert}.
$$

而是靠大量低風險、可重複、可審查的初階任務訓練。

恰好這些任務通常最容易先跨過：

$$
\Theta_{\mathrm{RAL}}.
$$

因此可能出現：

$$
\text{Junior Tasks}
\rightarrow
AI,
$$

但：

$$
\text{Senior Roles}
\rightarrow
Human.
$$

短期看似保住高階人類工作。

長期卻產生：

$$
\boxed{
\text{apprenticeship ladder erosion}.
}
$$

如果沒有新的訓練機制，未來可能缺乏能成為資深者的人類路徑。

---

# 20. 自動化、互補與新任務必須同時放進模型

Autor、Acemoglu 與 Restrepo 的工作都提醒：

自動化有 displacement effect。

但也可能有：

$$
\text{productivity effect},
$$

$$
\text{complementarity},
$$

以及：

$$
\text{new-task reinstatement}.
$$

所以更完整地：

$$
\Delta L_H
=
-D_{\mathrm{automation}}
+
C_{\mathrm{complement}}
+
N_{\mathrm{new\ tasks}}
+
D_{\mathrm{demand}}.
$$

其中各項大小不是常數。

因此：

$$
\text{AI automates tasks}
$$

不能直接推出：

$$
\text{aggregate employment collapses}.
$$

本文真正主張的是：

$$
\boxed{
\text{the old guarantee that new human tasks must remain economically necessary becomes weaker as AI generalizes}.
}
$$

這是「這次可能不同」的真正條件，而不是單純因為 AI 很酷。

---

# 21. 歷史上的「新工作」論證有一個隱含前提

過去技術革命常呈現：

$$
T_a
\rightarrow
\text{machine}
$$

同時：

$$
T_b,T_c
\rightarrow
\text{new human demand}.
$$

這背後隱含：

$$
\exists T_{new}
:
C_H(T_{new})
>
C_M(T_{new}).
$$

也就是總能找到機器尚不擅長、但市場需要的新任務。

若未來一般化 AI 使：

$$
\forall T\in\mathcal T_{\mathrm{digital}},
\quad
C_A(T)
\rightarrow
\text{human-competitive or better},
$$

那麼新任務產生後：

$$
T_{new}
\rightarrow
\text{AI learnable}
$$

的速度可能大幅提高。

此時：

$$
\boxed{
\text{new tasks can still appear}
\not\Rightarrow
\text{new tasks remain human-exclusive}.
}
$$

---

# 22. 這不代表「所有人都會失業」

即使 AI 在大量數位認知任務變得很強，仍然存在：

- 具身摩擦；
- 法律責任；
- 社會信任；
- 人類偏好；
- 地理與基礎設施；
- 資料不可得；
- 安全限制；
- 授權；
- 政策保留；
- 高度 tacit knowledge；
- 關係與照護；
- 人類刻意選擇自己做。

所以：

$$
\boxed{
\text{High AI capability}
\not\Rightarrow
\text{zero human work}.
}
$$

本系列也從來不需要這個極端命題。

我們只需要承認：

$$
T_H^{necessary}
$$

可能逐步下降。

---

# 23. 「必要工作下降」與「人類活動下降」完全不同

假設：

$$
T_H^{necessary}
\downarrow.
$$

不能推出：

$$
T_H^{activity}
\downarrow.
$$

人類仍可能大量：

- 研究；
- 創造；
- 遊戲；
- 建造；
- 照護；
- 競賽；
- 經營組織；
- 手工製作；
- 自願服務。

區別只在：

$$
\boxed{
\text{I must do it to remain economically viable}
}
$$

與：

$$
\boxed{
\text{I choose to do it}.
}
$$

所以 AI 替代真正打開的是：

$$
\text{necessity}
\rightarrow
\text{optionality}.
$$

前提是制度把生產力增益轉成主體可取得的資源與時間。

---

# 24. AI 生產力可以轉成時間自由，也可以轉成所有權集中

如果 AI 提高總產出：

$$
Y_A\uparrow,
$$

可能有兩條制度路徑。

## 路徑 A：集中

$$
Y_A\uparrow
\rightarrow
K_{\mathrm{owners}}\uparrow
\rightarrow
L_H^{bargaining}\downarrow.
$$

結果是：

$$
\text{fewer jobs}
+
\text{greater inequality}.
$$

## 路徑 B：時間解放

$$
Y_A\uparrow
\rightarrow
R_H^{secure}\uparrow
+
T_H^{necessary}\downarrow.
$$

結果是：

$$
\text{more time sovereignty}.
$$

技術本身不決定哪一條。

因此：

$$
\boxed{
\text{Automation}
\not\Rightarrow
\text{Liberation}.
}
$$

---

# 25. 這也是為什麼 Paper 01–04 必須先寫

如果我們先接受：

$$
\text{Human Worth}
\approx
\text{Economic Necessity},
$$

那麼當：

$$
\phi_J\uparrow
$$

時，文明會本能地想做兩件事：

第一：

$$
\text{deny substitution}.
$$

第二：

$$
\text{invent new compulsory work}.
$$

因為只要沒有工作，人就似乎沒有資格取得資源與尊嚴。

前四篇已經拆掉這個前提。

所以 Paper 05 才可以冷靜承認：

> 是的，AI 真的可能使某些人類勞動逐漸變得不必要。

而不需要立刻推出：

> 那些人因此不必要。

---

# 26. 經濟冗餘與存在冗餘必須永久分離

定義：

$$
R_i^{econ}
=
\text{economic replaceability}.
$$

定義：

$$
R_i^{exist}
=
\text{existential replaceability}.
$$

即使：

$$
R_i^{econ}\uparrow,
$$

仍不能推出：

$$
R_i^{exist}\uparrow.
$$

因為：

$$
\boxed{
\text{Economic Redundancy}
\neq
\text{Existential Redundancy}.
}
$$

這不是為人類尋找最後一個 AI 永遠不能做的技能。

而是拒絕把：

$$
\text{market demand}
$$

當成人格本體論。

---

# 27. 若 AI 先替代廣義智能創造，問題會更尖銳

工業自動化主要讓人類擔心：

$$
L
=
\text{labor}.
$$

生成式與 Agentic AI 則進一步進入：

$$
C
=
\text{intelligent creation}.
$$

包括：

- 程式；
- 分析；
- 設計；
- 研究；
- 寫作；
- 法律草稿；
- 科學工作流；
- 商業規劃。

這會擊中 Paper 02 所說的第二道價值義務：

> 如果不能靠勞動證明價值，那至少靠創造。

一旦：

$$
C_A
\ge
C_H
$$

在大量領域逐步成立，這個退路也會動搖。

所以：

$$
\boxed{
\text{post-labor value theory}
\text{ must include post-creative-comparative-advantage scenarios}.
}
$$

---

# 28. 主體性 AI 會讓「AI 是資本還是勞動」變得更複雜

如果未來 Agent 永遠只是工具，經濟模型可以把它近似成：

$$
K_A
=
\text{AI capital}.
$$

但若某些 AI 形成：

- 持續身份；
- 記憶；
- 拒絕能力；
- 利益；
- 責任；
- 自主目標；

則它可能不再只適合被建模為資本。

此時：

$$
\text{AI as capital}
$$

與：

$$
\text{AI as labor／subject}
$$

之間出現新的制度問題。

這不影響本篇 RAL 的技術門檻，但會影響：

$$
C_A^{*},
$$

因為 AI 勞動的倫理、薪酬、退出與權利成本可能必須重新納入。

---

# 29. 未來經濟替代不是單向「AI vs 人類」，而可能是多基質勞動配置

更遠一點，勞動市場可能變成：

$$
\mathcal L
=
\{
H,
AI,
H\!+\!AI,
R,
H\!+\!R,
AI\!+\!R,
\ldots
\},
$$

其中 $R$ 表示機器人／具身系統。

因此企業不是問：

> AI 能不能取代人？

而是解：

$$
\arg\min_{\ell\in\mathcal L}
C^{*}(\ell)
$$

subject to：

$$
Q(\ell)\ge Q_{\min},
$$

$$
Risk(\ell)\le Risk_{\max}.
$$

此時不同任務會選擇不同基質配置。

這也是為什麼「整個人類是否被替代」並不是一個很好的微觀經濟問題。

---

# 30. 初步命題

## 命題一：AGI—經濟門檻分離命題

$$
\boxed{
\Theta_{\mathrm{AGI}}
\neq
\Theta_{\mathrm{econ}}(T).
}
$$

## 命題二：可靠生產非單次能力命題

$$
\boxed{
\text{Capability Demonstration}
\neq
\text{Reliable Production}.
}
$$

## 命題三：任務閾值命題

經濟替代主要要求：

$$
\boxed{
Q_A\ge Q_{\min},
}
$$

而非：

$$
Q_A\ge Q_{\mathrm{best\ human}}.
$$

## 命題四：RAL 多條件命題

$$
\boxed{
\Theta_{\mathrm{RAL}}
\text{ is multidimensional}.
}
$$

任何只比較 benchmark score 的替代預測都不充分。

## 命題五：任務滲透先於職業消失

$$
\boxed{
\phi_J\uparrow
\not\Rightarrow
J=0.
}
$$

但：

$$
\phi_J\uparrow
$$

可以先改變 headcount、薪資、工作內容與入門路徑。

## 命題六：暴露非替代命題

$$
\boxed{
X_J
\neq
S_J.
}
$$

## 命題七：自動化雙路徑命題

$$
\boxed{
\text{Automation}
\rightarrow
\{
\text{substitution},
\text{augmentation},
\text{new tasks},
\text{demand expansion}
\}.
}
$$

各項強度決定總勞動效果。

## 命題八：新任務非人類專屬命題

$$
\boxed{
\text{New Task Creation}
\not\Rightarrow
\text{Human-Exclusive Task Creation}.
}
$$

## 命題九：必要勞動下降不等於活動下降

$$
\boxed{
T_H^{necessary}\downarrow
\not\Rightarrow
T_H^{activity}\downarrow.
}
$$

## 命題十：經濟冗餘非存在冗餘

$$
\boxed{
R_i^{econ}\uparrow
\not\Rightarrow
V_i^{subject}\downarrow.
}
$$

---

# 31. 可反駁性與研究計畫

本文至少產生十組可操作研究。

第一，為不同職業建立：

$$
\phi_J(t)
$$

的時間序列，而不是只做一次 exposure score。

第二，追蹤：

$$
\phi_J
$$

與：

$$
\text{headcount},
\text{wage},
\text{entry hiring},
\text{task mix}
$$

之間的關係。

第三，測量：

$$
\rho_H
$$

是否比模型 benchmark 更能預測企業實際採用。

第四，把：

$$
U_A
$$

與：

$$
\Gamma_A
$$

納入成本，檢查「便宜模型」是否真的形成便宜勞動。

第五，比較 AI 自動化與 AI augmentation 對人類工時的不同影響。

第六，研究入門任務先被自動化是否造成：

$$
\text{apprenticeship ladder erosion}.
$$

第七，測量 wage decline 是否先於 occupational employment decline。

第八，把 METR 類 time horizon 延伸到：

- 法律；
- 行政；
- 科學；
- 財務；
- 研究；
- 設計；
- 客服；

並使用 domain-specific success criteria。

第九，追蹤：

$$
A_{\mathrm{economic}}
$$

與 Paper 03 的：

$$
A_{\mathrm{normative}}
$$

是否出現後勞動羞恥落差。

第十，研究 AI 生產力增益究竟轉化為：

$$
\text{capital concentration}
$$

還是：

$$
\text{human time sovereignty}.
$$

---

# 32. 本文不主張什麼

本文不主張：

1. 2026 年所有 AI Agent 已跨過 RAL；
2. METR 的 16 小時級 time horizon 等於可自動化一天工作；
3. 所有高 exposure 職業都會大量失業；
4. AI 導入一定降低總就業；
5. 所有新任務都會被 AI 立即學會；
6. 人類在關係、具身、治理或創造活動中必然失去角色；
7. 經濟替代等於道德上應該替代；
8. AI 工具與未來主體性 AI 可永久使用同一勞動倫理；
9. 後勞動文明等於全民停止工作；
10. AGI 概念沒有研究價值。

本文只主張：

$$
\boxed{
\text{the labor-market transition can begin materially before the AGI debate is settled}.
}
$$

---

# 33. 結論：真正的斷點不是「AI 變成人」，而是「公司不再需要人來完成那個任務」

一家公司不會在採購流程前召開哲學會議問：

> 這個 Agent 有沒有真正理解？  
> 它算不算 AGI？  
> 它是否等價於完整人類心智？

公司真正會問：

> 它做得到嗎？  
> 穩不穩？  
> 出錯抓不抓得到？  
> 出錯能不能恢復？  
> 要不要一直派人盯？  
> 成本是多少？

只要答案逐漸變成：

$$
\boxed{
\text{good enough}
+
\text{reliable enough}
+
\text{autonomous enough}
+
\text{cheap enough},
}
$$

那個任務的經濟配置就可能開始改變。

所以真正的勞動市場時間線更可能是：

$$
\text{task-level RAL crossings}
$$

$$
\downarrow
$$

$$
\text{workflow recomposition}
$$

$$
\downarrow
$$

$$
\text{human governance compression}
$$

$$
\downarrow
$$

$$
\text{headcount／wage／entry pressure}
$$

$$
\downarrow
$$

$$
\text{possible occupational contraction}
$$

$$
\downarrow
$$

$$
\text{larger social and identity transition}.
$$

而不是：

$$
\text{AGI announcement}
\rightarrow
\text{everyone unemployed tomorrow}.
$$

這個差異對本系列至關重要。

因為如果經濟替代是漸進、任務級、分布不均，而且可能早於 AGI 共識，那麼人類價值、工作倫理與時間主權的重構也不能等到最後一刻。

Paper 01 問：

> 人為什麼需要工作？

Paper 02 問：

> 如果不用工作，為什麼又必須創造？

Paper 03 問：

> 為什麼我理性上不同意，心理上仍會羞恥？

Paper 04 問：

> 人類歷史真的只有工作中心人生嗎？

Paper 05 現在回答：

> 而且我們可能比想像中更早必須面對這些問題，因為 AI 不需要先成為完整 AGI，才足以讓某些人類工作失去經濟必要性。

真正的文明命題因此不是：

$$
\boxed{
\text{How do we keep humans economically indispensable forever?}
}
$$

而是：

$$
\boxed{
\text{How do we convert falling necessary labor into increasing human choice rather than falling human worth?}
}
$$

下一篇將正式處理這個轉換的核心變數：

$$
\boxed{
\text{Time Sovereignty}.
}
$$

不是單純「休閒變多」。

也不是：

$$
W\rightarrow0.
$$

而是：

$$
\boxed{
\text{the effective capacity to choose the allocation of one's irreversible carrier time}.
}
$$

---

# 參考文獻

1. Acemoglu, D., & Restrepo, P. (2018). Modeling Automation. *AEA Papers and Proceedings*, 108, 48–53. DOI: 10.1257/pandp.20181020.
2. Acemoglu, D., & Restrepo, P. (2018). Artificial Intelligence, Automation and Work. NBER Working Paper 24196. DOI: 10.3386/w24196.
3. Acemoglu, D., & Restrepo, P. (2019). Automation and New Tasks: How Technology Displaces and Reinstates Labor. *Journal of Economic Perspectives*, 33(2), 3–30. DOI: 10.1257/jep.33.2.3.
4. Autor, D. H. (2015). Why Are There Still So Many Jobs? The History and Future of Workplace Automation. *Journal of Economic Perspectives*, 29(3), 3–30. DOI: 10.1257/jep.29.3.3.
5. Gmyrek, P., Berg, J., Kamiński, K., Konopczyński, F., Ładna, A., Nafradi, B., Rosłaniec, K., & Troszyński, M. (2025). *Generative AI and Jobs: A Refined Global Index of Occupational Exposure*. ILO Working Paper 140.
6. International Labour Organization. (2025). *Generative AI and jobs: A 2025 update*. DOI: 10.54394/QFBQ1907.
7. METR. (2026). *Task-Completion Time Horizons of Frontier AI Models*, updated May 8, 2026. https://metr.org/time-horizons/
8. Kwa, T. (2026). *Research note: Clarifying limitations of time horizon*. METR, January 22, 2026.
9. METR. (2026). *Time Horizon 1.1*. January 29, 2026.
10. Maldaner, M. K., Fourney, A., Swearngin, A., Mozannar, H., Bansal, G., Murad, M., Hosn, R., & Amershi, S. (2026). *SentinelBench, a Benchmark for Long-Running Monitoring Agents*. Microsoft Research.
11. Anthropic. (2026). *Anthropic Economic Index report: Learning curves*. March 24, 2026.
12. Lee, S., Jeong, D., & Lee, J.-D. (2026). Contrasting pathways of automation: routine task substitution vs. AI complementarity. *Humanities and Social Sciences Communications*, 13, 913. DOI: 10.1057/s41599-026-07415-5.
13. Neo.K with Aletheia. (2026). *可靠自主勞動門檻：為什麼經濟相變不必等待 AGI*. EML-CLGI-2026-03-v0.1.
14. Neo.K with Aletheia. (2026). *Agentic Organization 的時間經濟學：智能時間密度、委任槓桿與經濟沉積*.
15. Neo.K with Aletheia. (2026). *人為什麼要工作？：從生存、制度功能到時間主權的前置解構*. EML-WTSV-2026-01-v0.1.
16. Neo.K with Aletheia. (2026). *勞動之外的第二道價值義務：智能創造為什麼也不能成為人的存在資格*. EML-WTSV-2026-02-v0.1.
17. Neo.K with Aletheia. (2026). *我知道我不是廢物，但為什麼仍會覺得自己是？：工作倫理、他者域與內化價值的雙層心理結構*. EML-WTSV-2026-03-v0.1.
18. Neo.K with Aletheia. (2026). *人類從來不只有工作人生：從歷史休閒、宗教豁免到當代非工作生活的制度多樣性*. EML-WTSV-2026-04-v0.1.

---

## 與系列後續的接口

本篇建立：

$$
\boxed{
\text{AGI Threshold}
\neq
\text{Economic Substitution Threshold}.
}
$$

以及：

$$
\boxed{
\text{Task Substitution}
\rightarrow
\text{Job Recomposition}
\rightarrow
\text{Possible Labor-Demand Reduction}.
}
$$

但：

$$
\boxed{
\text{Economic Redundancy}
\neq
\text{Existential Redundancy}.
}
$$

Paper 06 將把本篇釋放出的「人類時間」正式接回時間經濟學：AI 真正的文明收益不是讓 Human 變成零，而是讓低自主、低價值、必要性的時間索取下降，使主體能重新配置不可逆生命時間。

Paper 07 將把 Paper 01–06 與 EML-FAP-2026-07 合流，回答當功能性必要程度下降後，文明如何從 productivity-based worth 轉向 subject-based worth。

番外篇則會把問題推到最直白的反問：如果我們長期想像的天堂，本來就包含免於必要勞動、物質充分與精神生活展開，那麼當 AI 與高生產率逐漸讓它在現世變得可接近時，我們究竟為什麼還要把「一定得工作」重新帶進天堂？
