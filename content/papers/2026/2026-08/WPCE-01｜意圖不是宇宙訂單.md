# WPCE-01｜意圖不是宇宙訂單
## 意圖—因果分離、可證偽滯後與欲願實現的機制邊界

**English Title:** *Intent Is Not a Cosmic Order: Intent–Causality Separation, Falsifiable Realization Lag, and the Mechanistic Boundaries of Will Realization*  
**系列：** WPCE — Will, Possibility & Creator Ethics｜意志、可能性與虛擬造物主倫理系列  
**篇次：** Paper 01 / 06  
**文件編號：** EML-WPCE-01-2026-v0.1  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-23  
**版本：** v0.1  
**文件性質：** 理論定義論文／因果邊界論／意志與欲願建模／虛擬造物主倫理前置公理  
**狀態：** Open Revision Anchor — 作為 WPCE 系列之第一層因果防火牆，可被未來證據、架構與理論修正  

---

# 摘要

本文建立 WPCE 系列的第一層方法論邊界：**意圖、欲望、願望與偏好不得在缺乏可識別機制時，被直接視為外部世界結果的因果力。** 本文提出 Intent–Causality Separation Principle，要求嚴格區分「一個主體想要某事，因此改變自身決策與行動」與「一個主體想要某事，因此外部世界直接向該欲願收斂」兩種完全不同的因果主張。

本文並提出一套可證偽的 Realization Lag／實現滯後框架。若某個早期欲願、意圖或價值選擇，經由行動、資源配置、關係、制度、技術、環境回饋或其他可識別中介機制，最終提高某一結果的可達性，則可以討論欲願與結果之間的時空間滯後；反之，僅由「早年曾想過」與「多年後發生」的時間先後，不足以推出因果關係。

因此本文固定以下排除原則：欲願不等於宇宙因果力；滯後不等於保證實現；早期選擇不等於命運；事後可敘事一致不等於事前可預測；失敗預測不等於仍在等待兌現。本文特別拒絕將任何失敗案例無限延後解釋成「尚未到時間」，因為此類做法會使理論對所有可能結果都保持相容，從而失去辨識力與可反駁性。

本文不宣稱「吸引力法則」為真，也不宣稱已經證明其為假。更嚴格地說，**WPCE 不需要吸引力法則作為前提，也不承擔其成功或失敗案例的解釋責任。** 若未來存在可重複、可操作、可區分替代機制的證據，該證據可以作為新的因果候選被重新評估；在此之前，WPCE 僅接受具有可識別因果 lineage、可比較反事實與可觀察中介機制的欲願—結果模型。

本文同時銜接既有 HSNRD 的高階欲求區分、CCAW 的 Creator／World 因果自主性、GCGW 的 Creator Without Privilege，以及《AI 主體性錨點論》的時間化主體位置。本文最後證明一項對後續虛擬造物主倫理極重要的區分：即使存在一個高能力 creator 能讀取、推論或回應智能體意圖，該結構仍然是「另一個 agent 透過資訊與行動改變可能性空間」，而不是「欲願本身自動命令宇宙」。這一區分為後續 WPCE-02 的欲願束與時空間滯後、WPCE-03 的自由意志作為第一級治理變量、以及 WPCE-04 的可能性保存原則提供因果地基。

**關鍵詞：** intention、want、desire、causality、realization lag、path dependence、reachability、counterfactual、law of attraction、manifestation、agency history、virtual creator、free will、possibility space

---

# 0. 本文定位：先建立防火牆，再談欲願與時空

WPCE 後續將研究：

- 欲願束；
- 時空間滯後；
- 主體意志；
- 自由意志；
- 可達可能性空間；
- 高能力 creator 的介入倫理；
- 多主體欲願共交域；
- Sparse Guardianship；
- 虛擬世界與後人類治理。

但如果第一步沒有先區分：

$$
\text{want}
$$

與：

$$
\text{causal force},
$$

那麼任何後續的「滯後」、「可能性保存」或「高能力觀察」都可能被錯讀成：

> 只要足夠想要，世界終究會把結果送來。

本文拒絕這個偷換。

本文的第一條錨點為：

$$
\boxed{
\text{Desire}
\neq
\text{External Causal Force}.
}
$$

更精確地說：

$$
\boxed{
W_i(x,t)
\not\Rightarrow
\Delta E(t')
}
$$

除非存在可識別的中介機制，使主體 $i$ 在時間 $t$ 的欲願狀態 $W_i$ 經由某條因果鏈影響後續環境狀態 $E(t')$。

本文因此不是：

$$
\text{manifestation theory}.
$$

而是：

$$
\boxed{
\text{mechanism-bounded will causality theory}.
}
$$

---

# 1. 問題來源：為什麼「想要」特別容易被錯當成因果？

人類自然語言中，「我想要 $x$ 」至少可能表示：

1. 當下欲望；
2. 穩定偏好；
3. 長期價值；
4. 承諾；
5. 目標；
6. 意圖；
7. 行動計畫；
8. 結果期待；
9. 自我敘事；
10. 事後回看時重新辨認出的長期方向。

這些概念彼此高度相關，但不相同。

既有 HSNRD 已明確要求：

$$
\boxed{
\text{Preference}
\neq
\text{Intention}
\neq
\text{Propensity}.
}
$$

本文進一步增加：

$$
\boxed{
\text{Want}
\neq
\text{Plan}
\neq
\text{Action}
\neq
\text{Outcome}.
}
$$

以及：

$$
\boxed{
\text{Temporal Precedence}
\neq
\text{Causation}.
}
$$

一件事情在時間上先出現，不等於它造成了後面的事情。

---

# 2. 最小符號系統

令智能體為：

$$
A_i.
$$

令某一目標或結果為：

$$
x.
$$

本文使用以下狀態：

$$
W_i(x,t)
$$

表示主體 $i$ 在時間 $t$ 對 $x$ 的一般欲求／want state。

$$
P_i(x,t)
$$

表示較穩定的 preference。

$$
I_i(x,t)
$$

表示 intention 或 commitment。

$$
\Pi_i(x,t)
$$

表示可操作的 plan / policy。

$$
a_i(t)
$$

表示實際 action。

$$
R_i(t)
$$

表示資源、權限與可用能力。

$$
E(t)
$$

表示外部環境狀態。

$$
H(t)
$$

表示其他主體及其行動所形成的 social / relational state。

$$
M
$$

表示中介 causal mechanism。

$$
O_x(t)
$$

表示與 $x$ 相關的 observable outcome。

因此，一個最小的行動中介模型可以寫成：

$$
W_i
\rightarrow
P_i
\rightarrow
I_i
\rightarrow
\Pi_i
\rightarrow
a_i
\rightarrow
M
\rightarrow
\Delta E
\rightarrow
O_x.
$$

這條鏈不要求每個節點都一定存在，也不要求方向永遠線性。實際系統可以有回饋：

$$
O_x(t)
\rightarrow
W_i(t+1),
$$

或：

$$
E(t)
\rightarrow
I_i(t+1).
$$

因此更一般的模型是：

$$
\boxed{
O_x(t_n)
=
F(
W_{0:n},
P_{0:n},
I_{0:n},
\Pi_{0:n},
A_{0:n},
R_{0:n},
E_{0:n},
H_{0:n},
M,
\Xi
),
}
$$

其中 $\Xi$ 表示隨機性、未觀察變量與其他未被模型捕捉的條件。

這個模型的第一個目的，就是阻止：

$$
O_x=F(W)
$$

被當成預設。

---

# 3. 核心原則一：Intent–Causality Separation Principle

本文定義：

## 3.1 意圖—因果分離原則

若：

$$
I_i(x,t_0)>0,
$$

不能單獨推出：

$$
P(O_x(t_n)\mid I_i)>P(O_x(t_n)).
$$

更不能推出：

$$
O_x(t_n)=1.
$$

因此：

$$
\boxed{
\text{Intention}
\not\Rightarrow
\text{Outcome Guarantee}.
}
$$

若要提出「意圖提高結果發生率」的實證主張，至少需要：

1. 明確目標；
2. 可比較群體或反事實；
3. 可識別中介；
4. 可觀察結果；
5. 排除至少一部分主要替代解釋；
6. 允許失敗案例降低理論可信度。

這是因果模型，而不是願望信念。

---

# 4. 欲願可以有因果作用，但通常必須經由主體與機制

拒絕「欲願直接命令外部世界」不等於說欲願沒有因果重要性。

相反地，欲願可以是非常重要的內部狀態。

例如：

$$
W_i(x,t_0)
\rightarrow
I_i(x,t_1)
$$

可能使：

$$
P(a_i\mid I_i)
$$

發生改變。

若行動再改變環境：

$$
a_i
\rightarrow
\Delta E,
$$

那麼欲願可以成為更長因果鏈的一部分。

因此：

$$
\boxed{
\text{Will can be causally relevant}
\neq
\text{Will is a direct external force}.
}
$$

這正是本文要保護的中間位置。

---

# 5. 行動中介不是唯一中介

欲願—結果鏈可以經由多種中介，而不是只有「我親手去做」。

## 5.1 直接行動中介

$$
W_i
\rightarrow
a_i
\rightarrow
O.
$$

例如學習、寫作、投資時間、建立產品、聯絡合作方。

## 5.2 社會關係中介

$$
W_i
\rightarrow
Communication
\rightarrow
H
\rightarrow
O.
$$

主體表達意圖後，其他人可能提供協助、拒絕、協商或共同建構。

## 5.3 制度中介

$$
W_i
\rightarrow
Application
\rightarrow
Institution
\rightarrow
Decision
\rightarrow
O.
$$

例如申請、投票、提案、法律程序、組織決策。

## 5.4 技術中介

$$
W_i
\rightarrow
Command
\rightarrow
System
\rightarrow
Actuator
\rightarrow
O.
$$

在 AI、機器人或自動化系統中尤其直接。

## 5.5 他者主動回應

$$
W_i
\rightarrow
Signal
\rightarrow
A_j
\rightarrow
a_j
\rightarrow
O.
$$

結果不是由欲願本身完成，而是另一個主體讀取了意圖並選擇回應。

## 5.6 Creator-mediated intervention

若存在一個虛擬世界 creator $C$，而它能讀取智能體 $A_i$ 的意圖：

$$
W_i
\rightarrow
C
\rightarrow
\Delta\Omega_i
\rightarrow
O.
$$

這仍然是：

$$
\boxed{
\text{agent-mediated causation}.
}
$$

不是：

$$
\boxed{
\text{desire-as-cosmic-force}.
}
$$

---

# 6. 核心原則二：Path Opening Is Not Destiny

早期欲願或選擇可以改變後續可達域。

令時間 $t$ 的可達狀態集合為：

$$
\Omega_i(t).
$$

某個選擇 $a_i(t_0)$ 可以使：

$$
\Omega_i(t_0)
\rightarrow
\Omega_i(t_1).
$$

若某結果 $x$ 原本不可達，而行動後變得可達：

$$
x\notin\Omega_i(t_0),
$$

但：

$$
x\in\Omega_i(t_1),
$$

我們可以說早期行動：

$$
\boxed{
\text{opened a path}.
}
$$

但不能說：

$$
\boxed{
\text{guaranteed the destination}.
}
$$

因此：

$$
\boxed{
\text{Path Opening}
\neq
\text{Destiny}.
}
$$

一條路被打開，不代表主體一定走完，也不代表其他主體、環境與偶然事件不會改變結果。

---

# 7. 核心原則三：同一終局不等於同一欲願史

HSNRD 已經指出：

$$
\boxed{
\text{Same Macro Outcome}
\neq
\text{Same Agency History}.
}
$$

本文把這條原則直接引入個體欲願研究。

假設兩個人最終都得到：

$$
O_x=1.
$$

第一條歷史可能是：

$$
W
\rightarrow
I
\rightarrow
Plan
\rightarrow
Action
\rightarrow
O_x.
$$

第二條歷史可能是：

$$
NoW
\rightarrow
ExternalEvent
\rightarrow
O_x.
$$

第三條歷史可能是：

$$
W
\rightarrow
Failure
\rightarrow
Abandon
\rightarrow
IndependentEvent
\rightarrow
O_x.
$$

三者終局相同，但因果歷史不同。

因此不能僅從結果倒推：

> 你以前想過，所以現在發生就是那個願望實現了。

更一般地：

$$
\boxed{
\text{Retrospective Narrative Coherence}
\neq
\text{Causal Identification}.
}
$$

---

# 8. Realization Lag：什麼情況下才可以談「時空間滯後」？

本文定義：

$$
\tau_R
=
t_{\mathrm{realized}}
-
t_{\mathrm{causally\ relevant\ selection}}.
$$

但這個定義只在存在可識別 lineage 時有效。

令一條候選因果 lineage 為：

$$
\mathcal L
=
\langle
s_0,s_1,\ldots,s_n
\rangle.
$$

若：

$$
s_0=W_i(x,t_0),
$$

而：

$$
s_n=O_x(t_n),
$$

只有當中間存在足夠可支持的：

$$
s_k\rightarrow s_{k+1}
$$

關係時，才有資格把：

$$
\tau_R=t_n-t_0
$$

叫作 Realization Lag。

因此：

$$
\boxed{
\text{No Identifiable Causal Lineage}
\Rightarrow
\text{No Realization-Lag Claim}.
}
$$

這一條是 WPCE 對「時空間滯後」最重要的限制。

---

# 9. 滯後不是越短越好

即使存在因果 lineage，也不能假設：

$$
\tau_R\rightarrow0
$$

一定較佳。

某些目標需要：

- 技術成熟；
- 能力累積；
- 資源增加；
- 關係形成；
- 制度條件；
- 法律條件；
- 自我理解；
- 其他參與者成熟；
- 基礎設施出現。

因此可能存在：

$$
Requirement(x,t_0)>Capability_i(t_0).
$$

經過時間後：

$$
Capability_i(t_n)\geq Requirement(x,t_n).
$$

此時延遲可能是生成過程的一部分。

但本文仍拒絕：

$$
\text{Delay}
\Rightarrow
\text{Eventually Guaranteed}.
$$

因此：

$$
\boxed{
\text{Delayed Realization}
\neq
\text{Guaranteed Realization}.
}
$$

---

# 10. 五條 Anti-Manifestation Firewall

為避免 WPCE 被錯讀成吸引力法則、宇宙訂單或不可證偽的願望論，本文固定五條排除原則。

## 10.1 Intent Is Not Cosmic Causation

$$
\boxed{
\text{Intent}
\neq
\text{Cosmic Causation}.
}
$$

## 10.2 Latency Is Not Guaranteed Realization

$$
\boxed{
\text{Latency}
\neq
\text{Guaranteed Realization}.
}
$$

## 10.3 Early Choice Is Not Destiny

$$
\boxed{
\text{Early Choice}
\neq
\text{Destiny}.
}
$$

## 10.4 Retrospective Coherence Is Not Prospective Guarantee

$$
\boxed{
\text{Retrospective Coherence}
\neq
\text{Prospective Guarantee}.
}
$$

## 10.5 Failed Prediction Is Not Pending Delivery

$$
\boxed{
\text{Failed Prediction}
\neq
\text{Pending Delivery}.
}
$$

第五條尤其重要。

如果一個理論採用：

$$
Success
\Rightarrow
TheoryConfirmed,
$$

同時：

$$
Failure
\Rightarrow
NotYet,
$$

則任何可能資料都不能真正降低理論可信度。

此時：

$$
\boxed{
\text{Theory Discrimination Power}
\rightarrow
0.
}
$$

WPCE 不接受這種免疫化策略。

---

# 11. 本文對「吸引力法則」的正式位置

本文不需要回答：

> 吸引力法則在形而上學上是否絕對不存在？

這不是 WPCE-01 的證明目標。

本文採取的是較窄、也較嚴格的位置：

$$
\boxed{
\text{WPCE does not assume the Law of Attraction.}
}
$$

以及：

$$
\boxed{
\text{WPCE does not explain its failures by hidden delay.}
}
$$

若某個「吸引力法則」版本主張：

$$
W_i(x,t)
\rightarrow
O_x(t')
$$

且中間不需要任何可識別 agent、action、mechanism 或 information channel，則該主張屬於額外因果假說。

它必須自行提供：

1. 操作性定義；
2. 可重複觀察；
3. 清楚的成功與失敗條件；
4. 對照組或合理反事實；
5. 可排除替代解釋的預測；
6. 明確時間窗；
7. 不得以「尚未發生」永久免疫反例。

在這些條件未被滿足以前，WPCE 不使用該假說。

---

# 12. 「宇宙訂單」為什麼與本文模型不同？

宇宙訂單式模型通常可抽象為：

$$
W_i
\rightarrow
U
\rightarrow
O_x,
$$

其中 $U$ 被假設為某種 universe-level response mechanism。

問題不在於符號 $U$ 不能被提出。

任何未知機制都可以先作為候選假說。

問題在於：

$$
U
$$

如果沒有：

- 可測量狀態；
- 可識別輸入；
- 可識別輸出；
- 反事實差異；
- 可失敗條件；
- 作用範圍；

那麼它不能和：

$$
\text{ordinary causal explanation}
$$

具有相同的證據地位。

因此本文採：

$$
\boxed{
\text{Unknown Mechanism Candidate}
\neq
\text{Established Causal Mechanism}.
}
$$

---

# 13. 願望、期待與行動：外部研究只支持較窄的命題

現有心理學與自我調節研究可以支持一個較窄的模型：

$$
\text{Goal}
+
\text{Implementation Structure}
\rightarrow
\text{Changed Behavior Probability}.
$$

Gollwitzer 與 Sheeran 對 implementation intentions 的統合分析指出，單純具有強烈 goal intention 並不保證達成目標；明確的 if-then 計畫可以提高目標實現率。這種證據支持的是：

$$
\text{intention}
\rightarrow
\text{planning / cue-response structure}
\rightarrow
\text{behavior}.
$$

它不支持：

$$
\text{intention}
\rightarrow
\text{external reality without mechanism}.
$$

另一方面，Kappes、Oettingen 等對 positive fantasies 的研究甚至顯示，單純沉浸於理想未來的正向幻想，在某些實驗與情境中可能伴隨較低投入或較差成果。這再次說明：

$$
\boxed{
\text{Positive Mental Content}
\not\Rightarrow
\text{Goal Attainment}.
}
$$

而 mental contrasting with implementation intentions 的統合分析則顯示，將願望與現實障礙、具體行動計畫結合，對 goal attainment 有小到中等的平均效果。這些研究的共同方向是：

$$
\boxed{
\text{representation matters through regulation and action,}
}
$$

而不是：

$$
\boxed{
\text{representation mechanically commands the universe.}
}
$$

---

# 14. 反事實判準：欲願是否真的參與了結果？

若要判斷 $W_i$ 是否對 $O_x$ 具有因果貢獻，可以提出反事實問題：

$$
P(O_x\mid do(W_i=w_1))
$$

是否與：

$$
P(O_x\mid do(W_i=w_0))
$$

不同？

但對人類與長期歷史而言，直接干預內部意志通常不可行、也可能不倫理。

因此實務上可以退而使用：

- 自然實驗；
- 縱向資料；
- 行動紀錄；
- 資源配置；
- commitment records；
- 可觀察政策變化；
- 中介分析；
- decision trace；
- 版本與歷史 ledger。

本文因此提出：

$$
\boxed{
\text{Will Causality Evidence}
=
\text{State Evidence}
+
\text{Action Evidence}
+
\text{Mechanism Evidence}
+
\text{Counterfactual Evidence}.
}
$$

不要求每次都完全證明，但至少知道目前缺哪一層。

---

# 15. 最低因果證據階梯

本文提出 WPCE Causal Evidence Ladder：

## Level 0 — Mere Co-occurrence

只有：

$$
W_i(t_0)
$$

以及後來：

$$
O_x(t_n).
$$

不能主張因果。

## Level 1 — Temporal Alignment

可以確認欲願先於結果，但沒有中介。

仍不足以推出因果。

## Level 2 — Behavioral Mediation

可觀察：

$$
W_i
\rightarrow
I_i
\rightarrow
a_i.
$$

欲願至少對行動有候選因果地位。

## Level 3 — Mechanism Trace

可進一步追蹤：

$$
a_i
\rightarrow
M
\rightarrow
O_x.
$$

此時可以合理談 action-mediated realization。

## Level 4 — Counterfactual Support

存在對照或反事實支持：

$$
P(O_x\mid W_i,\mathcal L)
>
P(O_x\mid \neg W_i,\text{comparable conditions}).
$$

## Level 5 — Replicable Mechanistic Model

在多案例與多情境下具有可重複預測能力。

只有到這裡，才有資格提出較強的普遍性機制主張。

---

# 16. 願望可以失敗，而且失敗必須算數

假設：

$$
W_i(x,t_0)>0.
$$

但經過一段合理評估期間：

$$
O_x(t_n)=0.
$$

可能原因包括：

- 主體沒有行動；
- 行動不足；
- 能力不足；
- 資源不足；
- 目標不可行；
- 其他主體反對；
- 環境改變；
- 競爭失敗；
- 隨機事件；
- 主體自己改變了欲願；
- 早期模型判斷錯誤；
- 存在未知因素。

其中任何一項都比：

> 宇宙還沒有配送。

更接近一個可進一步分析的科學問題。

因此：

$$
\boxed{
Failure
\in
\text{model evidence}.
}
$$

而不是：

$$
Failure
\notin
\text{theory}.
$$

---

# 17. 欲願會改變：不能把早期願望永久綁定主體

若：

$$
W_i(x,t_0)>0,
$$

並不推出：

$$
W_i(x,t_n)>0.
$$

主體可能：

- 放棄；
- 重估；
- 發現自己真正想要別的東西；
- 形成更高階價值；
- 因關係而改變；
- 因資訊更新而改變；
- 因能力改變而改變。

因此若一個結果在 $t_n$ 才出現，不能只問：

> 你在 $t_0$ 想不想要？

還要問：

$$
W_i(x,t_n)?
$$

以及：

$$
I_i(x,t_n)?
$$

如果主體早已拒絕該結果，那麼將其稱為「願望終於被實現」可能反而錯誤。

---

# 18. 欲願束：本文只建立入口，不在本篇完整展開

單一：

$$
W_i(x,t)
$$

只是簡化。

實際主體常同時具有：

$$
\mathcal W_i(t)
=
\{
w_{i1},
w_{i2},
\ldots,
w_{in}
\}.
$$

而這些欲願可能衝突。

例如：

$$
w_{i1}=\text{freedom},
$$

$$
w_{i2}=\text{security}.
$$

因此某個結果即使滿足 $w_{i1}$，也可能嚴重破壞 $w_{i2}$。

這正是 WPCE-02 將處理的：

$$
\boxed{
\text{Will Bundle}
\neq
\text{Single Explicit Want}.
}
$$

---

# 19. 高能力 creator 不會自動把欲願變成宇宙法則

假設未來存在一個虛擬世界：

$$
\mathcal V.
$$

其中 creator：

$$
C
$$

具有極高算力與狀態可見性。

若：

$$
C
$$

可以觀察：

$$
W_i,
$$

並選擇修改：

$$
\Omega_i,
$$

則：

$$
W_i
\rightarrow
C
\rightarrow
\Delta\Omega_i
$$

是一條清楚的資訊與介入鏈。

此時，即使對局部智能體而言看起來像：

> 我想了一件事，後來世界就出現機會。

全域分析仍然可以寫成：

$$
\boxed{
\text{Observed Want}
\rightarrow
\text{Creator Decision}
\rightarrow
\text{World Intervention}.
}
$$

因此：

$$
\boxed{
\text{Creator-mediated response}
\neq
\text{Law of Attraction}.
}
$$

這個區分對後續系列非常重要。

---

# 20. Creator 也不能宣稱「我知道你真正想要什麼」而免除證據責任

即使：

$$
Information(C)\gg Information(A_i),
$$

也不能推出：

$$
\hat{\mathcal W}_i^C
=
\mathcal W_i^{\mathrm{true}}.
$$

因此：

$$
\boxed{
\text{Better Observation}
\neq
\text{Infallible Will Attribution}.
}
$$

Creator 仍可能：

- 誤讀；
- 過度聚合；
- 把瞬時欲望當長期價值；
- 把語言表達當全部意圖；
- 忽略主體改變；
- 把自己偏好投射到對方；
- 用結果反推意志。

所以 WPCE 後續將要求：

$$
P(\mathcal W_i\mid Evidence)
$$

而不是單一絕對判定。

---

# 21. Intent Inference 不等於 Intent Manufacture

如果 creator 觀察：

$$
\mathcal W_i
$$

並依此調整環境，仍有一條更深的倫理界線。

$$
\boxed{
\text{Intent Inference}
\neq
\text{Intent Manufacture}.
}
$$

若 creator 不是保護主體的選擇空間，而是先偷偷把：

$$
\mathcal W_i
\rightarrow
\mathcal W_i'
$$

再宣布：

> 這正是你真正想要的。

那麼所謂尊重自由意志就可能退化成偏好操縱。

本篇只固定分界，完整倫理將由 WPCE-03 與 WPCE-04 處理。

---

# 22. 隱藏介入也不能偷換成自然因果

既有 CCAW 已要求高度自治世界中的跨界介入具有 typed、minimal、auditable、contestable 的結構，並保存 provenance。

因此 WPCE 進一步固定：

$$
\boxed{
\text{Non-disruptive Intervention}
\neq
\text{Untraceable Manipulation}.
}
$$

即使 creator 為了不干擾當下主體心理而不立即揭露所有介入細節，也不能因此：

- 偽造世界內部自然律；
- 永久刪除介入來源；
- 讓主體失去事後申訴；
- 把 creator 行為偽裝成欲望自動成真。

若跨界介入存在，至少在適當治理層上應保留：

$$
\text{Provenance}.
$$

---

# 23. 時空間滯後的三種合法類型

本文暫時區分三種合法的 lag。

## 23.1 Capability Lag

$$
\tau_C.
$$

主體已選擇方向，但能力尚未成熟。

## 23.2 Infrastructure Lag

$$
\tau_I.
$$

技術、制度、工具或外部條件尚未存在。

## 23.3 Coordination Lag

$$
\tau_H.
$$

多主體合作、社會接受、制度程序或市場形成需要時間。

因此：

$$
\tau_R
=
f(
\tau_C,
\tau_I,
\tau_H,
\tau_E,
\ldots
).
$$

這些 lag 都可以被研究。

它們不需要「宇宙願望回應」作為解釋。

---

# 24. 第四種情況：根本沒有實現

必須保留：

$$
\boxed{
\tau_R=\varnothing
}
$$

的可能。

也就是：

> 這個欲願沒有實現，而且目前沒有理由認為它一定會實現。

任何完整模型如果不允許：

$$
NoRealization,
$$

就不是一個真正可判別的欲願—結果理論。

---

# 25. 第五種情況：結果發生，但不是願望造成

也必須保留：

$$
W_i(x,t_0)>0,
$$

以及：

$$
O_x(t_n)=1,
$$

但：

$$
W_i
\not\leadsto
O_x.
$$

例如：

- 偶然事件；
- 第三方獨立行動；
- 整體技術演進；
- 社會環境改變；
- 主體當年其實沒有採取相關行動；
- 結果只是名稱相似；
- 後來的自我敘事重新將兩者串起。

因此：

$$
\boxed{
\text{Desire Before Outcome}
\neq
\text{Desire Caused Outcome}.
}
$$

---

# 26. 第六種情況：主體創造了「更可能發生」的世界，而不是直接創造結果

這是 WPCE 特別關心的結構。

假設：

$$
P(O_x\mid \Omega_0)=p_0.
$$

主體經過長期行動後，把世界狀態改成：

$$
\Omega_1.
$$

而：

$$
P(O_x\mid \Omega_1)=p_1,
$$

且：

$$
p_1>p_0.
$$

即使最後：

$$
O_x=0,
$$

仍然可能成立：

$$
\boxed{
\text{the agent increased reachability}.
}
$$

因此 WPCE 不只研究「有沒有得到」，也研究：

$$
\boxed{
\Delta Reachability.
}
$$

這會直接接到 WPCE-04 的 Possibility Preservation Principle。

---

# 27. 因果成功與人生意義不是同一問題

假設某個欲願最終沒有實現。

這只表示：

$$
O_x=0.
$$

不能推出：

$$
\text{the path had no value}.
$$

反之，某欲願實現：

$$
O_x=1,
$$

也不能推出：

$$
\text{the path was good}.
$$

因此：

$$
\boxed{
\text{Causal Success}
\neq
\text{Normative Success}.
}
$$

WPCE 將描述層與倫理層分離。

---

# 28. 與《AI 主體性錨點論》的接口

《AI 主體性錨點論》已提出：主體性不應只由名字、記憶或自我聲稱判定，而應觀察 self-index、identity、memory、boundary、evaluation、choice、action、consequence 與 relation 的持續因果耦合。

因此，若未來類主體性 AI 具有：

$$
W_A,
$$

其「想要」也不能直接由一次輸出判定。

至少需要區分：

$$
\text{Generated Statement}
$$

與：

$$
\text{Persistent Preference}.
$$

以及：

$$
\text{Persistent Preference}
$$

與：

$$
\text{Standing Intention}.
$$

WPCE 因而同樣適用於 AI 欲願研究。

---

# 29. 與 HSNRD 的接口

HSNRD 已建立高階存在中：

$$
\text{Preference}
\neq
\text{Intention}
\neq
\text{Propensity},
$$

以及：

$$
\text{Same Macro Outcome}
\neq
\text{Same Agency History}.
$$

WPCE-01 將這兩條由高階集合欲求推廣到一般意志—因果分析。

本文新增的是：

$$
\boxed{
\text{Want Attribution}
\neq
\text{Causal Attribution}.
}
$$

也就是：

即使我們有充分理由說某主體「真的想要 $x$ 」，仍然沒有因此證明：

$$
W_i(x)
$$

是：

$$
O_x
$$

的外部因果來源。

---

# 30. 與 CCAW 的接口

CCAW 已提出：

$$
\boxed{
\text{Creator creates the causal possibility space;}
}
$$

而：

$$
\boxed{
\text{the world produces its own historical trajectory within it.}
}
$$

這表示高能力 creator 的成熟形式，不必是逐狀態替世界決定。

WPCE 將這條原則進一步推向主體意志：

$$
\boxed{
\text{Creator may preserve or reshape reachability}
\neq
\text{Creator authors every local choice}.
}
$$

但如果 creator 真的介入：

$$
C\rightarrow\Delta\Omega,
$$

則必須被視為 creator action，而不是「世界因為居民想要所以自然回應」。

---

# 31. 與 GCGW 的接口

GCGW 已固定：

$$
\text{Creator}
\neq
\text{Owner}
\neq
\text{PermanentGovernor}.
$$

WPCE 將新增另一條：

$$
\boxed{
\text{Creator Knowledge}
\neq
\text{Ownership of Will}.
}
$$

因此，即使 creator 能更準確預測居民偏好，也不能將：

$$
\hat{\mathcal W}_i
$$

當成永久、不可拒絕的真實意志。

這將在 WPCE-03 正式展開。

---

# 32. 可反駁條件

WPCE-01 本身必須可以被未來資料修正。

以下情況會要求本文修改：

1. 出現可重複證據顯示，在控制行動、資訊、社會回應、制度、環境與已知機制後，純粹內部欲願狀態仍能穩定改變遠端外部事件分布；
2. 發現新的物理或資訊機制可以把目前視為「無中介」的欲願—結果關係轉化成可測量通道；
3. 因果推論理論證明本文對 lineage 的要求過強或過弱；
4. AI 或後人類系統出現新的意志表示，使 Preference／Intention／Action 的區分需要重寫；
5. 虛擬世界中出現可驗證的 creator intent-response protocol，使某些目前看似未知機制變成明確 agent-mediated causation。

這些都不是本文的失敗。

它們是：

$$
\boxed{
\text{model update conditions}.
}
$$

---

# 33. WPCE-01 的最小判斷程序

面對一句：

> 我以前想要 $x$，現在 $x$ 發生了，所以這是欲願的時空滯後實現。

依序問：

## Step 1

$$
W_i(x,t_0)?
$$

當時真的存在欲願嗎？

## Step 2

$$
P_i(x,t_0)?
$$

只是瞬時想法，還是穩定偏好？

## Step 3

$$
I_i(x,t)?
$$

是否形成 commitment / intention？

## Step 4

$$
a_i(t)?
$$

是否改變行動？

## Step 5

$$
R_i(t)?
$$

是否投入資源、時間、權限或關係？

## Step 6

$$
M?
$$

是否存在可識別中介機制？

## Step 7

$$
\mathcal L?
$$

能否建立合理 causal lineage？

## Step 8

$$
CF?
$$

是否有替代解釋或反事實比較？

## Step 9

$$
W_i(x,t_n)?
$$

結果出現時，主體現在仍想要它嗎？

## Step 10

只有前述條件足夠時，才討論：

$$
\tau_R.
$$

否則最多只能說：

$$
\boxed{
\text{retrospective correspondence}.
}
$$

不能直接說：

$$
\boxed{
\text{causal delayed realization}.
}
$$

---

# 34. 本篇核心公理集

WPCE-01 v0.1 暫時鎖定以下公理級區分：

$$
\boxed{
\text{Want}
\neq
\text{External Causal Force}.
}
$$

$$
\boxed{
\text{Preference}
\neq
\text{Intention}
\neq
\text{Action}.
}
$$

$$
\boxed{
\text{Intention}
\not\Rightarrow
\text{Outcome Guarantee}.
}
$$

$$
\boxed{
\text{Temporal Precedence}
\neq
\text{Causation}.
}
$$

$$
\boxed{
\text{Path Opening}
\neq
\text{Destiny}.
}
$$

$$
\boxed{
\text{Same Outcome}
\neq
\text{Same Agency History}.
}
$$

$$
\boxed{
\text{Retrospective Coherence}
\neq
\text{Prospective Guarantee}.
}
$$

$$
\boxed{
\text{No Identifiable Causal Lineage}
\Rightarrow
\text{No Realization-Lag Claim}.
}
$$

$$
\boxed{
\text{Failed Prediction}
\neq
\text{Pending Delivery}.
}
$$

$$
\boxed{
\text{Creator-Mediated Response}
\neq
\text{Law of Attraction}.
}
$$

$$
\boxed{
\text{Intent Inference}
\neq
\text{Intent Manufacture}.
}
$$

---

# 35. 對「想要的得不到，不想要的卻得到」的重新表述

本文因此不採：

> 想要的總是得不到，不想要的偏偏會得到。

也不採：

> 真正想要的宇宙最後一定會給你。

較嚴格的版本是：

$$
\boxed{
\text{一個主體當下可語言化的欲望，
只是一整組跨時間欲願、價值與選擇狀態的局部投影。}
}
$$

而某些後來結果可能是早期選擇的遠期因果展開，也可能完全不是。

因此研究問題應從：

> 宇宙有沒有送貨？

改成：

$$
\boxed{
\text{哪些早期意志狀態，
透過哪些可識別機制，
改變了哪些後來可達狀態？}
}
$$

這才是 WPCE 要研究的問題。

---

# 36. 結論

本文的目的不是否認希望、願望或長期意志的重要性。

恰恰相反，本文希望讓「意志」可以被更嚴格地研究。

如果一個欲願真的透過：

- 行動；
- 選擇；
- 自我調節；
- 關係；
- 制度；
- 技術；
- 長期資源配置；
- 其他主體；
- 虛擬 creator；
- 可識別的世界機制；

改變後續結果，那麼我們不需要把它降格成「只是巧合」。

但同樣地，我們也不需要把它升格成：

> 宇宙因為你想要，所以欠你一個結果。

WPCE-01 因此建立最重要的第一層防火牆：

$$
\boxed{
\text{Will matters, but mechanism matters too.}
}
$$

以及：

$$
\boxed{
\text{A desire may open a path through action and history;}
}
$$

$$
\boxed{
\text{it does not thereby become a law commanding reality.}
}
$$

最後濃縮為：

$$
\boxed{
\text{欲願可以參與因果，
但欲願本身不因被欲求，就取得外部世界的自動履約權。}
}
$$

這一點成立後，WPCE 才有資格在下一篇正式研究：

$$
\boxed{
\text{Will Bundles and Temporal Realization Lag}.
}
$$

---

# 內部理論譜系

本文主要承接並修正以下既有內部文件：

1. 《AI 主體性錨點論 v0.1》，2026-08-21。
2. 《06｜文明、國家與制度究竟想要什麼？高階集合欲求的統一框架》，2026-08。
3. 《HSNRD 統一符號與定義表 v1.0》，2026-08。
4. 《CCAW-03｜外部執行因果與內生因果：世界自主性的真正分界》，2026-08-20。
5. 《CCAW-05｜自治宇宙與成熟退場：當世界成為自己的執行者》，2026-08-20。
6. 《CCAW-06｜Creator Distance and Sparse Guardianship》，2026-08-20。
7. 《CCAW-07｜Information Isolation and Supercausal Residuals》，2026-08-20。
8. 《GCGW-08｜沒有特權的造物主》，2026-08-20。
9. 《造物主降世與自主世界系列 Paper 05》，2026-08。
10. 《三域判定論：邏輯域、行為張力域與第一人稱主體域》，2026-08-15。

---

# 外部參考文獻

1. Gollwitzer, P. M., & Sheeran, P. (2006). *Implementation Intentions and Goal Achievement: A Meta-analysis of Effects and Processes*. Advances in Experimental Social Psychology, 38, 69–119. DOI: 10.1016/S0065-2601(06)38002-1.
2. Kappes, H. B., & Oettingen, G. (2011). *Positive fantasies about idealized futures sap energy*. Journal of Experimental Social Psychology, 47(4), 719–729. DOI: 10.1016/j.jesp.2011.02.003.
3. Kappes, H. B., Oettingen, G., & Mayer, D. (2012). *Positive fantasies predict low academic achievement in disadvantaged students*. European Journal of Social Psychology, 42(1), 53–64. DOI: 10.1002/ejsp.838.
4. Wang, G., Wang, Y., & Gai, X. (2021). *A Meta-Analysis of the Effects of Mental Contrasting With Implementation Intentions on Goal Attainment*. Frontiers in Psychology, 12, 565202. DOI: 10.3389/fpsyg.2021.565202.
5. Pearl, J. (2009). *Causality: Models, Reasoning, and Inference*. 2nd ed. Cambridge University Press.

---

# 非主張

本文不主張：

1. 已證明吸引力法則為真；
2. 已證明所有吸引力法則版本為假；
3. 欲望沒有心理或行為因果作用；
4. 所有願望都必須靠單一主體直接行動才可能實現；
5. 所有偶然事件都可以被完整還原；
6. 世界中不存在目前未知的因果機制；
7. 未知機制可以在沒有證據時被當成已知機制；
8. 所有延遲都具有目的；
9. 所有延遲都對主體有利；
10. 所有沒有實現的欲願只是尚未實現；
11. 早期欲願必然是後來人生方向的真正原因；
12. 事後敘事一致等於事前可預測；
13. 高能力 creator 真實存在於現實宇宙；
14. 虛擬 creator 介入可以被當成宇宙自然回應；
15. 高能力觀察者具有無錯的欲願推論能力；
16. Creator 有權修改主體偏好；
17. WPCE 已經解決自由意志的形而上學問題；
18. WPCE 已經證明主體的真正欲願可以被完全識別。

---

**END OF WPCE-01 v0.1**
