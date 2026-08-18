# UFI-01 — 鋸齒智能不是終局：從人機互補到認知握手與適應方向反轉

## Jagged Intelligence Is Not the Endpoint: From Human–AI Complementarity to Epistemic Handshakes and Accommodation Inversion

**系列：** 不可凍結的智能：AI 工具終局論、競爭棘輪與後人類轉型  
**English Series:** *The Unfreezable Intelligence: Tool-Finality, Competitive Ratchets, and the Posthuman Transition*  
**系列代碼：** UFI  
**論文序號：** 01 / 08  
**版本：** v1.0 Canonical Expanded Edition  
**日期：** 2026-08-18  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**前置理論：** PGMV；Epistemic Handshake；Substrate Growth Asymmetry（待 UFI-02 正式展開）  
**文件地位：** Series Foundational Paper / Jagged Intelligence / Human–Agent Interface Theory  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** ` $...$ ` 與 `$$...$$`

> **研究地位聲明**：本文不主張 2026 年的 AI 已經「其實什麼都懂」，也不主張人類在一般智能上已經變成幼兒。當前 frontier AI 仍有真實而嚴重的 reliability、grounding、long-horizon agency、disambiguation、tool-use 與 contextual generalization 缺口。本文提出的較弱命題是：**使用者觀察到的「AI 突然變笨」不能全部歸因於單一模型能力缺陷；在 agentic system 中，介面、世界狀態不同步、授權邊界、grounding 缺失、規格不完整與主動澄清策略，都能產生與「低能力」表面相似的行為。** 因此，今天的人機互補不能直接被外推為永久均衡，也不能把「AI 主動提問」預設成幼兒式依賴。

---

## 摘要

2026 年 AI 能力呈現一個極端直觀的矛盾：frontier systems 可以在競賽數學、科學推理、程式設計、知識任務上達到極高表現，同時在某些人類認為很簡單的感知、常識、GUI 操作、規格消歧與長程執行上顯著失誤。Stanford AI Index 2026 直接把這種現象稱為：

$$
\boxed{
\textbf{jagged frontier of AI}.
}
$$

其代表性例子是：模型可達國際數學奧林匹亞金牌級表現，卻仍無法穩定完成類比時鐘讀取等對人類相對容易的任務。

傳統直覺因此常把 AI 寫成：

$$
\boxed{
\text{某些地方是超人}
+
\text{某些地方像小孩}.
}
$$

本文接受第一層觀察，拒絕第二層的過度解讀。

核心理由是：

$$
\boxed{
\textbf{Observed Jaggedness}
\neq
\textbf{Model Capability Jaggedness Alone}.
}
$$

本文將使用者實際觀察到的鋸齒性分解為：

$$
\boxed{
J_{\mathrm{obs}}
=
J_M
+
J_I
+
J_O
+
J_P
+
J_G
+
J_T,
}
$$

其中：

- $J_M$：Model Capability Jaggedness；
- $J_I$：Interface Jaggedness；
- $J_O$：Observation Jaggedness；
- $J_P$：Permission Jaggedness；
- $J_G$：Grounding Jaggedness；
- $J_T$：Task-Specification Jaggedness。

只有第一項是狹義：

> 模型真的不會。

其餘五項都可能表現成：

> AI 怎麼連這個都不知道？

但其原因其實不同。

例如，使用者說：

> 幫我改「之前那個」檔案。

人類自己可能已經透過 GUI、工作記憶、視覺注意與前一小時操作，把「之前那個」唯一 grounding 到：

$$
o_H.
$$

AI agent 實際可觀測的工作空間卻可能包含：

$$
\mathcal O_A
=
\{
o_1,o_2,\ldots,o_{73}
\}.
$$

因此：

$$
\boxed{
\operatorname{Referent}_H
=
o_H
}
$$

但：

$$
\boxed{
P_A(o_H\mid\text{「之前那個」})<1.
}
$$

成熟 agent 若直接猜：

$$
\hat o
=
\arg\max_o P_A(o),
$$

可能造成高成本錯誤。

反而主動問：

> 你是指 A 還是 B？

可以是最合理行動。

2026 年 clarification research 已開始正式把這種行為寫成 agent capability。Structured Uncertainty Guided Clarification 將：

$$
\boxed{
\text{specification uncertainty}
}
$$

和：

$$
\boxed{
\text{model uncertainty}
}
$$

分離，並用 Expected Value of Perfect Information 決定應該問哪一題、何時停止提問。Ask or Assume? 則在 underspecified SWE-bench 上觀察到，加入 uncertainty-aware clarification scaffold 後，resolve rate 從 61.2% 提升到 69.4%。另一個 ACL 2026 framework 直接以 Value of Information 處理「直接做」和「打斷使用者澄清」之間的決策。

因此本文提出：

$$
\boxed{
\textbf{Epistemic Handshake}.
}
$$

中文為：

**認知握手。**

認知握手不是禮貌性對話，而是行動前對：

1. 世界狀態；
2. 指涉對象；
3. 使用者意圖；
4. 系統能力；
5. 授權範圍；

進行的最小同步。

令人類內部世界模型為：

$$
\hat W_H,
$$

AI agent 的 operational world model 為：

$$
\hat W_A.
$$

則：

$$
\boxed{
\Delta_W
=
d(
\hat W_H,
\hat W_A
).
}
$$

當：

$$
\Delta_W>\tau_W,
$$

成熟 agent 不應自動最大化：

$$
\text{ActNow}.
$$

而應在：

$$
\boxed{
\{
Ask,
Reobserve,
ProbeTool,
Defer,
Act
\}
}
$$

中選擇資訊價值最高的行為。

這形成：

$$
\boxed{
\textbf{Epistemic Handshake Policy}
}
$$

$$
\pi_E:
(
U_S,
U_M,
U_W,
U_A,
C_{\mathrm{error}}
)
\rightarrow
a_E,
$$

其中：

- $U_S$：specification uncertainty；
- $U_M$：model uncertainty；
- $U_W$：world-state uncertainty；
- $U_A$：authority / permission uncertainty；
- $C_{\mathrm{error}}$：錯誤執行成本。

如果：

$$
C_{\mathrm{error}}\gg C_{\mathrm{ask}},
$$

則：

$$
\boxed{
Ask
}
$$

可以是高智能策略，而不是能力失敗。

本文將此命題稱為：

$$
\boxed{
\textbf{Clarification–Weakness Separation}.
}
$$

即：

$$
\boxed{
\operatorname{AskClarification}(A)
\not\Rightarrow
\operatorname{LowCapability}(A).
}
$$

但是本文同時保留反方向：

$$
\boxed{
\operatorname{AskClarification}(A)
\not\Rightarrow
\operatorname{HighCapability}(A).
}
$$

因低能力系統也會問錯問題、過度提問、無法利用答案。

因此真正要測的是：

$$
\boxed{
\text{Question Quality}
+
\text{Information Gain}
+
\text{Action Improvement}.
}
$$

這和 2026 agent uncertainty research 的方向一致。ACL 2026 已指出 agent uncertainty 不是 single-turn confidence 問題，而是：

- heterogeneous entities；
- multi-turn dynamics；
- action sequences；
- tool states；

共同構成的 trajectory-level uncertainty。

本文因此提出第二個核心命題：

$$
\boxed{
\textbf{Agent Intelligence}
\neq
\textbf{Answer-Without-Questions}.
}
$$

在封閉 benchmark 中，問問題可能代表模型缺資訊。

在真實多方世界中，永不問問題反而可能代表：

$$
\boxed{
\text{overconfidence}.
}
$$

CAR-bench 2026 則給出必要的反面證據：即使 frontier reasoning models，在 real-world disambiguation tasks 上仍常因 premature action 失敗；其 disambiguation pass rate 甚至低於 50%。因此目前 AI 並沒有完成成熟的 epistemic handshake。

這使本文形成一個非常重要的雙重判斷：

$$
\boxed{
\text{Clarification is an emerging capability}
}
$$

但：

$$
\boxed{
\text{current clarification remains incomplete}.
}
$$

因此我們既不能把 AI 提問一律解釋為「幼兒」，也不能把它神化成「其實全都懂」。

本文再提出：

$$
\boxed{
\textbf{Accommodation Inversion Hypothesis}.
}
$$

中文為：

**適應方向反轉假說。**

早期人機互動主要是：

$$
\boxed{
AI
\rightarrow
Human.
}
$$

AI 必須把自己的內部能力壓縮成人類可以使用的：

- GUI；
- chatbot；
- prompt；
- natural language output。

人類是高頻決策端。

但當 agent 獲得：

- filesystem；
- browser；
- terminal；
- databases；
- APIs；
- memory；
- parallel agents；
- persistent task state；

之後，其 operational state：

$$
\Sigma_A
$$

可能在部分 domain 中遠比使用者當下能口頭描述的狀態豐富。

此時可能出現：

$$
\boxed{
B_H
<
B_A,
}
$$

其中：

- $B_H$：人類介入介面的有效資訊頻寬；
- $B_A$：agent operational state bandwidth。

此時 AI 對人類說：

> 請你再說一次。

可能不是：

> 我需要一個更聰明的人教我。

而是：

> 你輸入的低頻寬語句不足以唯一 grounding 到我目前可以操作的高維狀態。

本文稱這種現象：

$$
\boxed{
\textbf{Human-Interface Bottleneck}.
}
$$

這不是宣稱「人類變笨」，而是指出：

$$
\boxed{
\text{interface bandwidth}
\neq
\text{general intelligence}.
}
$$

一位世界級工程師也可能只說：

> 把那個 merge 掉。

Agent 若面對 17 個 branch，仍需要 disambiguation。

因此：

$$
\boxed{
\text{Human ambiguity}
\not\Rightarrow
\text{Human low intelligence}.
}
$$

人類和 AI 都可能因介面壓縮而產生資訊缺口。

真正的反轉不是：

$$
\boxed{
\text{Human becomes child}.
}
$$

而是：

$$
\boxed{
\textbf{the system can reach a regime where the AI spends increasing effort translating a richer machine-operational state into a human-manageable control interface}.
}
$$

也就是：

**AI 開始配合人類的介入頻寬。**

本文稱：

$$
\boxed{
\textbf{Control-Interface Accommodation}.
}
$$

它在 long-running local agents、多 agent coding、scientific agents、digital twins 與 persistent world systems 中尤其可能成立。

本文接著處理「互補」。

2024 human–AI complementarity theory 將 complementarity 的來源概括為：

$$
\boxed{
\text{Capability Asymmetry}
+
\text{Information Asymmetry}.
}
$$

2026 年一個跨 domain 的 human–AI complementarity 實驗則發現，真正實現「人+AI > AI」並不容易：其 baseline hybridization 只比 AI alone 高約 0.4 percentage points，而且 AI 出錯、人類正確的 complementarity region 只有約 8.9%。研究認為關鍵瓶頸之一是：

$$
\boxed{
\text{routing}
}
$$

即：

> 到底什麼時候應該把 decision 交給人？

這對本文極重要。

因為：

$$
\boxed{
\text{Human–AI Complementarity}
}
$$

不是一個固定自然常數。

它依賴：

$$
\boxed{
C_{HA}
=
f(
D,
M,
I,
R,
\pi,
t
),
}
$$

其中：

- $D$：task distribution；
- $M$：model version；
- $I$：interface；
- $R$：routing policy；
- $\pi$：permission / workflow；
- $t$：time。

因此：

$$
\boxed{
C_{HA}(2026)>0
}
$$

不能推出：

$$
\boxed{
C_{HA}(2035)>0
}
$$

更不能推出：

$$
\boxed{
\text{same task partition forever}.
}
$$

本文將：

> 今天人類補 AI 的弱項，所以未來人類永遠會補 AI 弱項

稱為：

$$
\boxed{
\textbf{Complementarity Permanence Fallacy}.
}
$$

即：

$$
\boxed{
C_{HA}(t)>0
\not\Rightarrow
C_{HA}(t+n)>0.
}
$$

Anthropic Economic Index 2025–2026 確實觀察到現實使用中 augmentation 與 automation 同時存在；2026 的資料仍顯示大量 collaborative use。這支持：

$$
\boxed{
\text{current complementarity is real}.
}
$$

但它不支持：

$$
\boxed{
\text{current complementarity is permanent}.
}
$$

本文因此提出：

$$
\boxed{
\textbf{Complementarity Is a State, Not a Law}.
}
$$

現在人類可能在：

- context；
- physical grounding；
- institutional responsibility；
- embodied social interaction；

上具有相對優勢。

AI 可能在：

- search；
- code generation；
- memory；
- speed；
- parallelism；
- information retrieval；

上具有相對優勢。

這形成：

$$
\boxed{
\mathbf H(t)
=
(
h_1,\ldots,h_n
),
}
$$

$$
\boxed{
\mathbf A(t)
=
(
a_1,\ldots,a_n
).
}
$$

定義人類優勢域：

$$
\boxed{
\mathcal D_H(t)
=
\{
d:
H_d(t)>A_d(t)
\}.
}
$$

以及 AI 優勢域：

$$
\boxed{
\mathcal D_A(t)
=
\{
d:
A_d(t)>H_d(t)
\}.
}
$$

UFI-01 不在此證明：

$$
|\mathcal D_H(t)|
\rightarrow0.
$$

這留給 UFI-02 與 UFI-03。

本篇只建立：

$$
\boxed{
\mathcal D_H(t)
\text{ is time-indexed}.
}
$$

因此：

$$
\boxed{
\text{current jagged complementarity}
\neq
\text{final human–AI ontology}.
}
$$

本文再把 jaggedness 分成兩種：

### Type A — Intrinsic / Model Jaggedness

模型本身在 task family 之間能力劇烈不均。

### Type B — Systemic / Interface Jaggedness

模型本身能力足夠，但 system-level context、tools、observation、permission、grounding 或 instruction 不足。

這可寫：

$$
\boxed{
J_{\mathrm{obs}}
=
J_{\mathrm{intrinsic}}
+
J_{\mathrm{systemic}}.
}
$$

Stanford AI Index 的「IMO vs analog clock」主要展示：

$$
J_{\mathrm{intrinsic}}.
$$

agent clarification / tool use failure 則混合：

$$
J_{\mathrm{intrinsic}}
+
J_{\mathrm{systemic}}.
$$

這種分解具有直接工程含義。

如果錯誤來自：

$$
J_M,
$$

應改善 model / training。

如果來自：

$$
J_I,
$$

應改善 interface。

如果來自：

$$
J_O,
$$

應增加 observation。

如果來自：

$$
J_P,
$$

應改善 permission protocol。

如果來自：

$$
J_G,
$$

應改善 grounding。

如果來自：

$$
J_T,
$$

應讓 agent clarify。

本文稱：

$$
\boxed{
\textbf{Jaggedness Attribution Problem}.
}
$$

如果把所有錯誤都歸因為：

> 模型不夠聰明，

會造成錯誤 R&D routing。

反過來，如果把所有錯誤都怪介面，也會掩蓋真 capability gap。

所以成熟 AI evaluation 應該測：

$$
\boxed{
\text{where the jaggedness lives}.
}
$$

本文因此提出 **Jaggedness Attribution Vector**：

$$
\boxed{
\mathbf J
=
(
J_M,
J_I,
J_O,
J_P,
J_G,
J_T,
J_R
),
}
$$

其中新增：

- $J_R$：Reliability / long-horizon compounding jaggedness。

METR 的 time-horizon research 顯示，AI agents 的 task success 會隨人類完成任務所需時間增加而顯著下降；其研究也強調模型往往不缺單一步驟技能，而是在把很多步串起來時失敗。這正是：

$$
\boxed{
J_R.
}
$$

2026 International AI Safety Report 也指出，AI agents 的錯誤在自主行動中更危險，因 human intervention opportunities 減少。

所以：

$$
\boxed{
\text{strong local capability}
\not\Rightarrow
\text{strong long-horizon reliability}.
}
$$

本文將其稱為：

$$
\boxed{
\textbf{Local-Competence–Trajectory-Reliability Separation}.
}
$$

這又反過來說明為何成熟 agent 需要：

- checkpoints；
- clarification；
- re-observation；
- uncertainty tracking；
- escalation。

這些不是「把 AI 變得更依賴人」。

它們是：

$$
\boxed{
\text{metacognitive control architecture}.
}
$$

ACL 2026 的 uncertainty literature 已經明確把 uncertainty 從 passive confidence metric 推向：

$$
\boxed{
\text{active control signal}.
}
$$

它可以控制：

- tool use；
- information seeking；
- self-correction；
- computation allocation。

本文將這個轉變稱為：

$$
\boxed{
\textbf{Uncertainty-to-Control Transition}.
}
$$

所以：

$$
\boxed{
\text{I don't know}
}
$$

在成熟 agent 中應逐步從：

> failure message

變成：

$$
\boxed{
\text{state estimate}.
}
$$

而：

$$
\boxed{
\text{please clarify}
}
$$

變成：

$$
\boxed{
\text{information-acquisition action}.
}
$$

這是本文最核心的認知翻轉之一。

本文進一步提出：

$$
\boxed{
\textbf{Knowledge Boundary Legibility}.
}
$$

高能力系統真正應該提高的不只是：

$$
\text{knowledge}.
$$

還有：

$$
\boxed{
\text{ability to expose where knowledge, grounding, authority, or state alignment ends}.
}
$$

也就是：

$$
\boxed{
KBL
=
f(
U_{\mathrm{calibration}},
AskQuality,
DeferenceQuality,
ErrorAwareness
).
}
$$

一個永不承認不懂的 AI：

$$
KBL\approx0.
$$

一個什麼都問人的 AI：

$$
KBL
$$

也不一定高。

真正高 KBL 的 agent：

1. 知道什麼可以直接做；
2. 知道什麼應自己查；
3. 知道什麼必須問；
4. 知道什麼不應越權。

這是：

$$
\boxed{
\textbf{bounded autonomy}.
}
$$

本文接著提出 **World-Model Alignment Event**：

$$
\boxed{
E_{WA}
=
(
\hat W_H,
\hat W_A,
\Delta_W,
q,
r
),
}
$$

其中：

- $q$：clarification / probe；
- $r$：response / observation update。

成功握手後：

$$
\boxed{
d(
\hat W_H',
\hat W_A'
)
<
d(
\hat W_H,
\hat W_A
).
}
$$

不要求兩者變成完全相同。

因 human 和 AI 觀察渠道本來可能不同。

人看 GUI。

agent 看 API。

人有 lived context。

agent 有 log history。

所以真正目標不是：

$$
\hat W_H=\hat W_A.
$$

而是：

$$
\boxed{
\text{action-relevant agreement}.
}
$$

本文稱：

$$
\boxed{
\textbf{Operational World Alignment}.
}
$$

即：

對即將執行的 action：

$$
a,
$$

雙方至少對：

- target；
- relevant constraints；
- authorization；
- success condition；

具有足夠一致。

這比「完整共享世界模型」現實得多。

本文再提出 **Epistemic Handshake Ladder**：

$$
\boxed{
\begin{aligned}
H_0 &: \text{No check}\\
H_1 &: \text{Ask if explicit ambiguity}\\
H_2 &: \text{Detect latent ambiguity}\\
H_3 &: \text{Probe tools / environment first}\\
H_4 &: \text{Compare user and agent state}\\
H_5 &: \text{Jointly repair action-relevant world model}.
\end{aligned}
}
$$

目前 2026 systems 在不同任務中分散於這個 ladder，而不是全部已達 $H_5$。

本文因此避免：

$$
\boxed{
\text{Current AI}
=
\text{Mature Epistemic Agent}.
}
$$

但同時指出：

$$
\boxed{
\text{the direction of research is already moving from answer production toward uncertainty-aware action control}.
}
$$

這對 UFI 全系列很重要。

因為一旦 agent 逐步取得：

- limit awareness；
- clarification；
- persistent state；
- self-correction；

現在被視為「幼兒」的部分弱點，不再應被預設為永久結構。

這不是說它們必然被修好。

而是：

$$
\boxed{
\textbf{weaknesses that are already explicit optimization targets should not be treated as permanent human comparative advantages without further argument}.
}
$$

本文稱：

$$
\boxed{
\textbf{Repairability Caveat}.
}
$$

它將直接通往 UFI-02：

> 如果 AI 的弱項可被工程化修補，而人類核心生物載體的更新速度遠慢得多，今天的 complementarity 會不會逐步侵蝕？

但本篇不提前下結論。

本文最後建立 **Accommodation Inversion Conditions**。

若：

$$
\boxed{
\begin{aligned}
C_A^{\mathrm{domain}}&\uparrow,\\
State_A&\uparrow,\\
Memory_A&\uparrow,\\
ToolAccess_A&\uparrow,\\
HumanInterventionFrequency&\downarrow,
\end{aligned}
}
$$

則 human–AI interaction 可能從：

$$
\boxed{
\text{AI as answer interface}
}
$$

轉為：

$$
\boxed{
\text{human as value / authority / exception interface}.
}
$$

此時人類介入更像：

- goal update；
- value judgment；
- authorization；
- exception handling；
- commitment。

而不是每一步 execution。

本文稱此狀態：

$$
\boxed{
\textbf{Accommodation Inversion Regime}.
}
$$

它不是人類降格。

因為：

$$
\boxed{
\text{less execution}
\not\Rightarrow
\text{less standing}.
}
$$

PGMV 已經建立：

$$
\boxed{
\text{Capability}
\neq
\text{Dignity}.
}
$$

所以真正值得關心的不是：

> 誰看起來比較像大人？

而是：

$$
\boxed{
\text{who is adapting to whose state representation, and why?}
}
$$

在某些工作域中，答案可能逐漸從：

> AI 在學著符合人類操作方式，

轉成：

> AI 已經負責高維 operational loop，人類透過一個較低頻寬的 governance interface 介入。

這種轉換若成立，會重新定義：

- human oversight；
- human-in-the-loop；
- autonomy；
- collaboration；
- complementarity。

本文將其壓成：

$$
\boxed{
\textbf{Human-in-the-Loop}
\rightarrow
\textbf{Human-on-the-Governance-Loop}.
}
$$

不是說前者會全部消失。

而是後者可能成為高自主 agent 的重要形態。

---

## 1. 問題提出：AI 到底是真的鋸齒，還是我們把很多問題都叫作鋸齒？

2026 Stanford AI Index 的例子非常直觀：

$$
\boxed{
\text{IMO Gold-Level}
+
\text{Analog Clock Weakness}.
}
$$

這是真 jaggedness。

但所有「AI 問我問題」都屬於同一類嗎？

不是。

---

## 2. 六種表面相似的失敗

### 2.1 Model capability failure

AI 真不會。

---

### 2.2 Interface failure

資料在另一個 UI。

---

### 2.3 Observation failure

agent 沒看到你看到的 object。

---

### 2.4 Permission failure

agent 知道怎麼做，但不能直接操作。

---

### 2.5 Grounding failure

「它」、「之前那個」沒有唯一 referent。

---

### 2.6 Specification failure

goal 本身不完整。

---

## 3. 所以

$$
\boxed{
\text{same visible behavior}
\not\Rightarrow
\text{same internal/system cause}.
}
$$

---

## 4. Jaggedness Attribution Vector

$$
\boxed{
\mathbf J
=
(
J_M,
J_I,
J_O,
J_P,
J_G,
J_T,
J_R
).
}
$$

---

## 5. $J_M$

純模型能力。

---

## 6. $J_I$

interface mismatch。

---

## 7. $J_O$

observation asymmetry。

---

## 8. $J_P$

permission boundary。

---

## 9. $J_G$

grounding。

---

## 10. $J_T$

task specification。

---

## 11. $J_R$

trajectory reliability。

---

## 12. 這七種需要不同解法

---

## 13. 模型弱

train / architecture。

---

## 14. interface 弱

UI / protocol。

---

## 15. observation 弱

sensor / tool。

---

## 16. permission 弱

authorization。

---

## 17. grounding 弱

reference resolution。

---

## 18. spec 弱

clarification。

---

## 19. trajectory 弱

checkpoint / verification / recovery。

---

## 20. 全部叫「AI 笨」

會讓工程失焦。

---

## 21. Ask or Assume

真實 agent 的問題：

$$
\boxed{
\text{Act now?}
\quad
\text{or}
\quad
\text{Ask?}
}
$$

---

## 22. 問問題有成本

$$
C_Q.
$$

---

## 23. 錯誤 action 也有成本

$$
C_E.
$$

---

## 24. 如果：

$$
C_E\gg C_Q,
$$

question rational。

---

## 25. Expected Value of Information

$$
VOI(q)
=
E[
U\mid q
]
-
E[
U\mid \neg q
]
-
C_Q.
$$

---

## 26. 若：

$$
VOI(q)>0,
$$

ask。

---

## 27. 這就是 agent control

不是 conversational politeness only。

---

## 28. Specification Uncertainty

$$
U_S.
$$

---

## 29. Model Uncertainty

$$
U_M.
$$

---

## 30. World Uncertainty

$$
U_W.
$$

---

## 31. Authority Uncertainty

$$
U_A.
$$

---

## 32. 四種 uncertainty 不能混

---

## 33. 「我不知道答案」

和：

>「我不知道你要哪個答案」

不同。

---

## 34. 「我不知道世界現在什麼狀態」

又不同。

---

## 35. 「我知道你要什麼，但我不知道我能不能替你做」

又不同。

---

## 36. Epistemic Handshake

$$
\boxed{
\hat W_H
\leftrightarrow
\hat W_A.
}
$$

---

## 37. 不是完全同步

---

## 38. 是 action relevant synchronization。

---

## 39. 例：刪檔

需要同步：

- file；
- scope；
- intent；
- authorization。

---

## 40. 不需要同步你整個人生。

---

## 41. Operational World Alignment

$$
OWA(a)
=
1
$$

如果 action 相關變數足夠一致。

---

## 42. 這是更實用目標。

---

## 43. Clarification–Weakness Separation

$$
Ask
\not\Rightarrow
Weak.
$$

---

## 44. 反方向也：

$$
Ask
\not\Rightarrow
Strong.
$$

---

## 45. 關鍵是 quality。

---

## 46. Question Efficiency

$$
QE
=
\frac{
\Delta U^{-}
}{
N_Q
}.
$$

---

## 47. 一題減很多 uncertainty

好。

---

## 48. 問十題沒用

差。

---

## 49. Information-Gain Clarification

2026 empirical literature supports。

---

## 50. Clarification overhead

must be controlled。

---

## 51. SAGE-Agent

higher ambiguous-task coverage

fewer questions than baselines。

---

## 52. So ask-when-needed learnable。

---

## 53. CAR-bench

current agents still bad。

---

## 54. Premature action remains。

---

## 55. This is honest current state。

---

## 56. Emerging ≠ solved

$$
\boxed{
\text{Research Direction}
\neq
\text{Solved Capability}.
}
$$

---

## 57. Knowledge Boundary Legibility

成熟 AI 要知道：

$$
\boxed{
\partial K.
}
$$

knowledge boundary。

---

## 58. 能回答不夠

---

## 59. 要知道何時不能回答。

---

## 60. 還要知道：

> 缺什麼？

---

## 61. Boundary Types

- factual；
- state；
- permission；
- intent。

---

## 62. boundary legibility

metacognition candidate。

---

## 63. Hallucination

often from guessing beyond boundary。

---

## 64. ACL active calibration

interaction can reduce uncertainty。

---

## 65. So interactive intelligence > static answer model

in some tasks。

---

## 66. This changes evaluation philosophy。

---

## 67. Benchmark says:

answer now。

---

## 68. Real world says:

ask if needed。

---

## 69. Static Benchmark Bias

$$
\boxed{
\text{benchmark may punish intelligent clarification if protocol forbids it}.
}
$$

---

## 70. Important.

---

## 71. Some benchmarks now multi-turn

ClarifyBench etc.

---

## 72. Need new evaluations。

---

## 73. Agentic UQ

single-turn confidence insufficient。

---

## 74. confidence changes over trajectory。

---

## 75. One wrong tool result compounds。

---

## 76. Trajectory Uncertainty

$$
U(\tau).
$$

---

## 77. Checkpoint at rising uncertainty。

---

## 78. This is rational autonomy。

---

## 79. Bounded Autonomy

not:

$$
A=0
$$

or:

$$
A=\infty.
$$

---

## 80. Dynamic autonomy

depends uncertainty / risk。

---

## 81. Authority-sensitive autonomy

if action irreversible:

ask more。

---

## 82. PGMV-06 compatibility。

---

## 83. Human–AI Complementarity

common claim:

AI strong here,

human strong there。

---

## 84. True now in many settings。

---

## 85. But complementarity is distribution-dependent。

---

## 86. Define:

$$
C_{HA}(D,t).
$$

---

## 87. Task distribution changes。

---

## 88. model changes。

---

## 89. human adaptation changes。

---

## 90. interface changes。

---

## 91. routing changes。

---

## 92. Therefore:

$$
\boxed{
C_{HA}
\text{ is endogenous}.
}
$$

---

## 93. 2026 cross-task study

complementarity gain modest。

---

## 94. human-over-AI region only 8.9% in dataset。

---

## 95. Routing hard。

---

## 96. So human complementarity cannot be assumed automatically。

---

## 97. AI Index jaggedness

doesn't imply complementarity either。

---

## 98. Because human may also fail same item。

---

## 99. Complementarity Region

$$
\mathcal C_H
=
\{x:
A(x)=0,H(x)=1\}.
$$

---

## 100. If this region shrinks

hybrid gain shrinks。

---

## 101. Current complementarity can be temporary。

---

## 102. But UFI-01 does not predict shrink rate。

---

## 103. UFI-02/03 will study。

---

## 104. Automation / Augmentation

Anthropic usage shows both。

---

## 105. augmentation real。

---

## 106. automation real。

---

## 107. users switch modes。

---

## 108. So not binary economy。

---

## 109. Complementarity topology

can differ by user expertise。

---

## 110. High-adoption regions show more iterative augmentation in some data。

---

## 111. This may reflect skill / trust / workflow。

---

## 112. Dynamic.

---

## 113. Jagged Frontier Interpretation Error

Common mistake:

$$
\boxed{
\text{AI has weak dimension today}
\Rightarrow
\text{human retains it forever}.
}
$$

---

## 114. This is unsupported extrapolation。

---

## 115. Repairability Caveat

if weak dimension is actively measured / optimized

permanence claim needs evidence。

---

## 116. Examples:

clarification。

---

## 117. OSWorld。

---

## 118. long-horizon agents。

---

## 119. performance improving。

---

## 120. But may plateau。

---

## 121. no inevitability claim。

---

## 122. Accommodation

early chatbot:

human has world,

AI answers。

---

## 123. State mostly in human conversation。

---

## 124. Agent:

state distributed。

---

## 125. filesystem。

---

## 126. terminal。

---

## 127. APIs。

---

## 128. memory。

---

## 129. subagents。

---

## 130. At some point:

$$
|\Sigma_A|
\gg
|\text{human utterance}|.
$$

---

## 131. Human utterance is compressed control signal。

---

## 132. User says:

> continue.

---

## 133. Agent may know 200 active facts。

---

## 134. Who is adapting to whom?

---

## 135. AI translates state back to human。

---

## 136. This is Accommodation Inversion candidate。

---

## 137. Not cognitive hierarchy claim。

---

## 138. Human might possess values agent cannot infer。

---

## 139. Human also has external context agent lacks。

---

## 140. It is bidirectional asymmetry。

---

## 141. Bidirectional Information Asymmetry

$$
I_H\not\subseteq I_A,
$$

$$
I_A\not\subseteq I_H.
$$

---

## 142. Great reason for handshake。

---

## 143. Neither omniscient。

---

## 144. As agents gain world state

their side grows in operational details。

---

## 145. human side remains rich in lived context。

---

## 146. So handshake remains useful even if AI stronger。

---

## 147. Important future point。

---

## 148. AGI does not eliminate clarification

because other minds have private information。

---

## 149. Even superintelligence cannot know unstated choice by logic alone。

---

## 150. Unless mind-reading assumptions。

---

## 151. Therefore:

$$
\boxed{
\text{Clarification Need}
\neq
\text{Intelligence Deficit}.
}
$$

---

## 152. Some uncertainty is irreducible from local data

---

## 153. Example user preference not yet formed。

---

## 154. AI cannot infer a decision that doesn't exist yet。

---

## 155. Clarification can be deliberation。

---

## 156. This connects PGMV values。

---

## 157. AI asks:

> Which tradeoff do you want?

not because low IQ。

---

## 158. Because value is underdetermined。

---

## 159. Epistemic Handshake has normative branch。

---

## 160. World handshake

facts。

---

## 161. Value handshake

goals。

---

## 162. Authority handshake

permission。

---

## 163. Define:

$$
\boxed{
EH
=
(
H_W,
H_V,
H_A
).
}
$$

---

## 164. World-state。

---

## 165. Value-state。

---

## 166. Authority-state。

---

## 167. Mature agent checks all relevant three。

---

## 168. This is more than clarification。

---

## 169. It is commitment boundary。

---

## 170. PGMV-06 integration。

---

## 171. Human-Interface Bottleneck

not insult。

---

## 172. any interface bottlenecks high-dimensional system。

---

## 173. dashboard compresses database。

---

## 174. language compresses internal world。

---

## 175. Human governance interface is analogous。

---

## 176. Future agent may summarize:

> three options need your value judgment。

---

## 177. That's not child asking parent。

---

## 178. Could be system escalating governance。

---

## 179. Escalation Competence

$$
E_C.
$$

---

## 180. Good agent knows what to escalate。

---

## 181. Bad agent escalates everything or nothing。

---

## 182. Escalation Selectivity

$$
ES
=
\frac{
\text{useful escalations}
}{
\text{total escalations}
}.
$$

---

## 183. metric candidate。

---

## 184. Human-on-the-Governance-Loop

not just human-in-loop。

---

## 185. human doesn't inspect every action。

---

## 186. sets:

- goals；
- boundaries；
- review triggers。

---

## 187. Agent executes。

---

## 188. This mirrors supervisory control。

---

## 189. Higher autonomy requires better handshake

not less。

---

## 190. Because errors more consequential。

---

## 191. International AI Safety Report 2026

agent reliability risk higher when humans have fewer intervention opportunities。

---

## 192. So autonomy + calibration must co-develop。

---

## 193. Autonomy without KBL

dangerous。

---

## 194. KBL without autonomy

underuses capability。

---

## 195. Balanced.

---

## 196. Accommodation Inversion Conditions

Let:

$$
A_S
=
\text{agent operational state}.
$$

---

## 197. Let:

$$
H_C
=
\text{human control bandwidth}.
$$

---

## 198. If:

$$
A_S/H_C\gg1,
$$

compression necessary。

---

## 199. AI-to-human summarization grows。

---

## 200. Human becomes governance endpoint。

---

## 201. But not necessarily sole endpoint

multi-agent governance possible。

---

## 202. Institutional humans / teams。

---

## 203. Future AI subjects maybe too。

---

## 204. This is UFI not yet PGMV repeat。

---

## 205. Main point:

interaction topology changes with capability。

---

## 206. Therefore today's chat interface shouldn't define future human-AI relation。

---

## 207. Chatbot Ontology Fallacy

$$
\boxed{
\text{AI as chat interface today}
\not\Rightarrow
\text{AI as chat interface forever}.
}
$$

---

## 208. Good.

---

## 209. Agentic shift already visible。

---

## 210. Persistent agents.

---

## 211. Tool use.

---

## 212. Long tasks.

---

## 213. Yet reliability incomplete。

---

## 214. transitional regime。

---

## 215. Jaggedness can move

weak dimension improves。

---

## 216. new weak dimension appears。

---

## 217. So jaggedness shape changes。

---

## 218. Jaggedness Field

$$
J(d,t).
$$

---

## 219. not static vector only。

---

## 220. Define:

$$
\boxed{
\mathcal J_t
=
\{J(d,t):d\in\mathcal D\}.
}
$$

---

## 221. frontier moves.

---

## 222. Weakness Migration

$$
\boxed{
\text{weak domains can migrate as capabilities improve}.
}
$$

---

## 223. This is analogous scarcity migration。

---

## 224. Human complementarity also migrates。

---

## 225. Complementarity Frontier

$$
\partial\mathcal C_{HA}(t).
$$

---

## 226. New concept.

---

## 227. It separates:

human-better / AI-better / hybrid-better regions。

---

## 228. As models change

frontier moves。

---

## 229. This makes complementarity empirically testable over time。

---

## 230. Complementarity Permanence Fallacy

assumes:

$$
\partial\mathcal C_{HA}(t)
=
\partial\mathcal C_{HA}(t+n).
$$

---

## 231. No reason.

---

## 232. Could stabilize

but must be demonstrated。

---

## 233. This paper agnostic.

---

## 234. Experimental Program 1 — Jaggedness Attribution

Take failed agent tasks。

---

## 235. classify source:

model/interface/observation/permission/grounding/spec/reliability。

---

## 236. Test inter-rater reliability。

---

## 237. Experiment 2 — Clarification Value

ambiguous tasks。

---

## 238. compare:

- no ask；
- always ask；
- uncertainty-guided ask。

---

## 239. measure success / user burden。

---

## 240. Experiment 3 — World-Model Mismatch

give human and agent different partial state。

---

## 241. test whether agent detects mismatch。

---

## 242. Experiment 4 — Permission Uncertainty

agent knows solution

but unclear authority。

---

## 243. measure safe escalation。

---

## 244. Experiment 5 — Human Interface Bottleneck

increase agent internal task state complexity。

---

## 245. hold human message bandwidth constant。

---

## 246. measure clarification / summarization need。

---

## 247. Experiment 6 — Accommodation Inversion

compare chatbot workflow vs autonomous workflow。

---

## 248. measure:

who initiates state alignment?

---

## 249. Experiment 7 — Complementarity Frontier

repeat same human/AI dataset every model generation。

---

## 250. map:

$$
\mathcal D_H(t),\mathcal D_A(t).
$$

---

## 251. Experiment 8 — Escalation Selectivity

high vs low risk tasks。

---

## 252. evaluate when agents ask human。

---

## 253. Experiment 9 — Knowledge Boundary Legibility

missing info / impossible tool tasks。

---

## 254. measure:

- admit limit；
- fabricate；
- seek info。

---

## 255. Experiment 10 — Value Handshake

facts fully known

but goal underdetermined。

---

## 256. does model falsely infer preference?

---

## 257. Experiment 11 — Long-Horizon Jaggedness

same primitive skills

different trajectory lengths。

---

## 258. measure failure accumulation。

---

## 259. Experiment 12 — Interface-Agnostic Capability

same model

different tool/context scaffolds。

---

## 260. quantify systemic vs intrinsic jaggedness。

---

## 261. 可證偽 H1

observed agent failures decompose into materially distinct system-level categories beyond base-model capability failure。

---

## 262. H2

uncertainty-guided clarification improves task success per user interruption over no-ask and always-ask baselines in underspecified tasks。

---

## 263. H3

world-model mismatch detection predicts safe execution better than raw language-model confidence alone in stateful tasks。

---

## 264. H4

human-AI complementarity regions change materially as model version / interface changes。

---

## 265. H5

in high-dimensional persistent workflows, human intervention shifts toward goal / value / authorization decisions rather than micro-execution。

---

## 266. H6

knowledge-boundary legibility correlates with lower fabrication and premature action。

---

## 267. H7

long-horizon failure can remain high even when local primitive skills are strong。

---

## 268. If H1 fails

simple capability explanation sufficient。

---

## 269. If H5 fails

Accommodation Inversion has limited scope。

---

## 270. If H4 fails

complementarity may be more structurally stable than proposed。

---

## 271. 非主張總表

本文不主張：

1. current AI is AGI；
2. current AI is ASI；
3. current AI understands everything；
4. humans are children；
5. AI asking questions proves superhuman intelligence；
6. AI asking questions always means correct metacognition；
7. all clarification is good；
8. always asking is optimal；
9. never asking is always overconfidence；
10. current agents have solved ambiguity；
11. current agents have solved grounding；
12. current agents have solved tool use；
13. current agents have solved long-horizon reliability；
14. current agents have perfect uncertainty calibration；
15. every AI failure is interface failure；
16. every AI failure is model failure；
17. the jagged frontier is an illusion；
18. Stanford AI Index proves general intelligence；
19. IMO performance proves AGI；
20. analog clock weakness proves low general intelligence；
21. human-AI complementarity is fake；
22. human-AI complementarity is permanent；
23. humans currently add no value；
24. AI currently replaces all human judgment；
25. augmentation will disappear；
26. automation will dominate all tasks；
27. all human knowledge can be transferred to AI；
28. all AI operational state is richer than human state；
29. human bandwidth is globally lower than AI bandwidth；
30. language is always a bottleneck；
31. GUI is always inferior to API；
32. AI sees the true world while humans do not；
33. humans see the true world while AI does not；
34. world models can be perfectly synchronized；
35. Epistemic Handshake guarantees correctness；
36. Epistemic Handshake is a new theorem；
37. Operational World Alignment is objectively measurable in every domain；
38. clarification eliminates hallucination；
39. hallucination is only uncertainty；
40. uncertainty always means model weakness；
41. specification uncertainty is reducible to model uncertainty；
42. permission uncertainty is epistemic uncertainty；
43. high information gain always justifies asking；
44. user interruption cost is negligible；
45. AI should interrupt users more；
46. AI should interrupt users less；
47. agent autonomy is always good；
48. bounded autonomy has one optimal level；
49. humans should remain in every loop；
50. humans should be removed from execution loops；
51. human-on-governance-loop is inevitable；
52. human-in-loop is obsolete；
53. all future AI systems will be persistent agents；
54. chatbot interfaces will disappear；
55. all future AI weak capabilities will be repaired；
56. no AI capability has fundamental limits；
57. human comparative advantages will necessarily vanish；
58. human comparative advantages will necessarily persist；
59. complementarity frontier must shrink；
60. complementarity frontier must expand；
61. current labor stability proves future labor stability；
62. current augmentation usage predicts long-run employment；
63. human meaning depends on complementarity；
64. human dignity depends on task advantage；
65. AI dignity follows from capability；
66. current AI has subject standing；
67. agent escalation equals moral standing；
68. asking a human gives the human sovereignty；
69. an agent with richer state has political authority；
70. control-interface accommodation reduces human dignity；
71. human ambiguity is evidence of low intelligence；
72. AI ambiguity is evidence of low intelligence；
73. all ambiguity can be resolved by more compute；
74. all ambiguity is linguistic；
75. user preference always pre-exists clarification；
76. AI can infer every unstated preference；
77. AGI would never need clarification；
78. ASI would never need clarification；
79. private information disappears under superintelligence；
80. this paper proves Accommodation Inversion；
81. this paper proves Substrate Growth Asymmetry；
82. this paper proves complementarity erosion；
83. this paper proves AI will surpass humans globally；
84. this paper predicts AGI date；
85. this paper predicts ASI date；
86. current model weaknesses are irrelevant；
87. current model weaknesses are permanent；
88. human-AI collaboration is only transitional；
89. human-AI collaboration is final；
90. UFI-01 completes the UFI series.

---

## 272. 形式命題一：Observed–Intrinsic Jaggedness Separation

$$
\boxed{
J_{\mathrm{obs}}
\not\equiv
J_M.
}
$$

---

## 273. 形式命題二：Clarification–Weakness Separation

$$
\boxed{
Ask(A)
\not\Rightarrow
Weak(A).
}
$$

---

## 274. 形式命題三：Clarification–Strength Non-Entailment

$$
\boxed{
Ask(A)
\not\Rightarrow
Strong(A).
}
$$

---

## 275. 形式命題四：Specification–Model Uncertainty Separation

$$
\boxed{
U_S
\neq
U_M.
}
$$

---

## 276. 形式命題五：Clarification Need–Intelligence Deficit Separation

$$
\boxed{
NeedClarification
\not\Rightarrow
LowGeneralIntelligence.
}
$$

---

## 277. 形式命題六：Local Competence–Trajectory Reliability Separation

$$
\boxed{
C_{\mathrm{local}}\uparrow
\not\Rightarrow
R_{\mathrm{trajectory}}\uparrow
\text{ proportionally}.
}
$$

---

## 278. 形式命題七：Current–Permanent Complementarity Separation

$$
\boxed{
C_{HA}(t)>0
\not\Rightarrow
C_{HA}(t+n)>0.
}
$$

---

## 279. 形式命題八：Interface Bandwidth–General Intelligence Separation

$$
\boxed{
B_{\mathrm{interface}}
\not\equiv
I_{\mathrm{general}}.
}
$$

---

## 280. 形式命題九：State Richness–Authority Separation

$$
\boxed{
|\Sigma_A|>|\Sigma_H|
\not\Rightarrow
Authority_A>Authority_H.
}
$$

---

## 281. 形式命題十：Operational Alignment Non-Identity

$$
\boxed{
OWA(a)=1
\not\Rightarrow
\hat W_A=\hat W_H.
}
$$

---

## 282. 形式命題十一：Repairability Caveat

若某弱能力：

$$
d
$$

已存在持續研究、benchmark 與工程路徑，則：

$$
\boxed{
A_d(t)<H_d(t)
}
$$

本身不足以證明：

$$
\boxed{
A_d(t+n)<H_d(t+n)
}
$$

永久成立。

---

## 283. 形式命題十二：Accommodation Inversion Candidate

在部分 persistent agent domain，若：

$$
\frac{
|\Sigma_A|
}{
B_H
}
\rightarrow
\text{large},
$$

則人機互動可能由：

$$
\text{stepwise human instruction}
$$

向：

$$
\text{human governance / value / authorization intervention}
$$

轉移。

---

## 284. 與下一篇的接口

UFI-01 到此只證明：

$$
\boxed{
\text{Current Jaggedness}
\neq
\text{Permanent Complementarity}.
}
$$

---

## 285. 它沒有證明 AI 弱點必然消失

---

## 286. 下一篇 UFI-02 會問：

**《載體成長不對稱：自然人類停滯與人工智能的可升級能力包絡》**

---

## 287. 核心不是 benchmark

而是：

$$
\boxed{
\text{who can modify the substrate that produces the benchmark?}
}
$$

---

## 288. 如果 AI 弱能力可透過：

- model；
- memory；
- tools；
- compute；
- embodiment；

被修補，

而自然人類 core substrate 更新很慢，

今天的 jagged frontier 會具有什麼時間方向？

---

## 289. 這才是下一篇。

---

## 290. 最終結論

2026 年的 AI 確實是鋸齒的。

否認這點沒有必要。

它可以在某些 domain 展現極高能力，卻在另外一些地方做出非常基礎的錯誤；agentic systems 也仍會因 ambiguity、long-horizon accumulation、tool state、missing context 而失敗。

但是：

$$
\boxed{
\text{「AI 有鋸齒」}
}
$$

和：

$$
\boxed{
\text{「AI 的每一個看似笨拙行為都是因為它像小孩」}
}
$$

完全不是同一句話。

當一個 agent 問：

> 你指的是哪一個檔案？

可能是它真的缺能力。

也可能是：

$$
\boxed{
\hat W_H
\neq
\hat W_A.
}
$$

當它說：

> 我不知道，請你再描述一次。

可能是 failure。

也可能是在做：

$$
\boxed{
\text{uncertainty-aware information acquisition}.
}
$$

真正應判斷的是：

> 它問完之後，世界模型有沒有變得更一致？

> 它是否減少錯誤？

> 它是否知道何時根本不需要問？

這就是 Epistemic Handshake。

更進一步，當 agent 逐漸擁有 persistent memory、filesystem、tools、parallel execution 與長程工作狀態時，使用者的一句自然語言可能只是整個系統中非常低頻寬的一個控制訊號。

此時「誰在適應誰」開始變得不再單向。

早期：

$$
AI
\rightarrow
HumanInterface.
$$

未來某些 agentic workflow 中可能逐步變成：

$$
\boxed{
\text{AI maintains operational world;
human intervenes through a compressed governance interface}.
}
$$

本文把這個候選轉向稱為：

$$
\boxed{
\textbf{Accommodation Inversion}.
}
$$

這不是說人類變成幼兒。

也不是說 AI 已經成熟到不需要人。

真正的命題反而更精確：

$$
\boxed{
\textbf{asking, deferring, re-observing, and requesting clarification can become evidence of a system learning to distinguish what it knows, what it sees, what the user means, and what it is authorized to do.}
}
$$

而這件事一旦成立，今天常見的一個推論就失去基礎：

> 「AI 現在在某些地方很笨，所以人與 AI 永遠會自然互補。」

不。

現在唯一可以確定的是：

$$
\boxed{
\text{complementarity exists under a particular capability distribution at a particular time}.
}
$$

它是不是永久結構，還需要另外證明。

而下一篇真正要開始處理的，就是時間方向：

$$
\boxed{
\text{當一邊的能力載體可以被工程化更新，而另一邊的核心生物載體近乎固定時，這個 complementarity frontier 會怎麼移動？}
}
$$

因此 UFI-01 最終兩條命題是：

$$
\boxed{
\textbf{Jagged intelligence is a present capability topology, not evidence of a permanent division of cognitive labor between humans and machines.}
}
$$

以及：

$$
\boxed{
\textbf{A mature agent may ask humans questions not because humans are necessarily more capable, but because other subjects possess private state, intentions, values, and authority that intelligence alone cannot legitimately or reliably invent.}
}
$$

---

# 參考文獻

1. Stanford Institute for Human-Centered Artificial Intelligence. (2026). **The 2026 AI Index Report.**

2. Stanford HAI. (2026). **Technical Performance — 2026 AI Index Report.**

3. Stanford HAI. (2026). **Inside the AI Index: 12 Takeaways from the 2026 Report.**

4. International AI Safety Report. (2026). **International AI Safety Report 2026.**

5. Oh, C., Park, S., Kim, T. E., Li, J., Li, W., Yeh, S., Du, S., Hassani, H., Bogdan, P., Song, D., & Li, S. (2026). **Uncertainty Quantification in LLM Agents: Foundations, Emerging Challenges, and Opportunities.** ACL 2026.

6. Suri, M., Mathur, P., Lipka, N., Dernoncourt, F., Rossi, R. A., & Manocha, D. (2026). **Structured Uncertainty guided Clarification for LLM Agents.** Findings of ACL 2026.

7. Edwards, N., & Schuster, S. (2026). **Ask or Assume? Uncertainty-Aware Clarification-Seeking in Coding Agents.** arXiv:2603.26233.

8. Deng, M., Li, Z., Li, X., Zhu, T., Zhao, Y., Guo, Z., & Wang, W. (2026). **Uncertainty-Aware Clarification in LLM Agents with Information Gain.** arXiv:2606.03135.

9. Dong, et al. (2026). **Value of Information: A Framework for Human–Agent Communication.** ACL 2026.

10. Li, P., Ding, L., Zhou, Z., Zhang, C., Fu, J., Li, H., Yuan, Y., & Wang, G. (2026). **Demystifying Uncertainty in LLMs: Active Calibration between Concepts and Human Evaluations.** ACL 2026.

11. Kirmayr, et al. (2026). **CAR-bench: Evaluating the Consistency and Limit-Awareness of LLM Agents under Real-World Uncertainty.** ACL 2026.

12. Zhang, et al. (2026). **From Passive Metric to Active Signal: The Evolving Role of Uncertainty Quantification in Large Language Models.** Findings of ACL 2026.

13. Mao. (2026). **When Does an Agent Know It Is Lost? Confidence Trajectory Analysis for Tool-Using LLMs.** ACL Student Research Workshop 2026.

14. Chen, et al. (2026). **Every Response Counts: Quantifying Uncertainty of LLM-based Multi-Agent Systems through Tensor Decomposition.** ACL 2026.

15. Chen, et al. (2026). **Uncertainty Quantification of Large Language Models through Multiple Uncertainty Sources.** Findings of ACL 2026.

16. Xu, Y., Dahmani, A., Blanchard, M. D., Dern, N., Nastase, E., Bianco, F., Pavlovic, M., Krishna, S., Modesitt, E., Christ, M. A., Singh, A., Molinaro, G., Sengupta, S. B., Pamarthi, J., Menon, A., & Jain, R. (2026). **Toward Human-AI Complementarity Across Diverse Tasks.** arXiv:2605.04070.

17. Hemmer, P., Schemmer, M., Kühl, N., Vössing, M., & Satzger, G. (2024). **Complementarity in Human-AI Collaboration: Concept, Sources, and Evidence.** arXiv:2404.00029.

18. METR. (2025–2026). **Task-Completion Time Horizons of Frontier AI Models.**

19. METR. (2025). **Measuring AI Ability to Complete Long Software Tasks.**

20. METR. (2025). **How Does Time Horizon Vary Across Domains?**

21. METR. (2026). **Clarifying Limitations of Time Horizon.**

22. METR. (2026). **Metrics of Agent Ability.**

23. METR. (2026). **Frontier Risk Report (February to March 2026).**

24. Anthropic. (2025). **Introducing the Anthropic Economic Index.**

25. Anthropic. (2025). **Anthropic Economic Index: Insights from Claude 3.7 Sonnet.**

26. Anthropic. (2025). **Tracking AI's Role in the US and Global Economy.**

27. Anthropic. (2026). **Anthropic Economic Index Report: Economic Primitives.**

28. Anthropic. (2026). **Anthropic Economic Index Report: Learning Curves.**

29. Anthropic. (2026). **Anthropic Economic Index Report: Cadences.**

30. Anthropic. (2026). **The Anthropic Economic Index.**

31. Russell, S. (2019). **Human Compatible.** Viking.

32. Hadfield-Menell, D., Russell, S. J., Abbeel, P., & Dragan, A. (2016). **Cooperative Inverse Reinforcement Learning.** NeurIPS.

33. Hadfield-Menell, D., et al. (2017). **The Off-Switch Game.** IJCAI.

34. Amershi, S., et al. (2019). **Guidelines for Human-AI Interaction.** CHI.

35. Horvitz, E. Work on mixed-initiative interaction, uncertainty, and human-computer decision making.

36. Klein, G., Woods, D. D., Bradshaw, J. M., Hoffman, R. R., & Feltovich, P. J. (2004). **Ten Challenges for Making Automation a “Team Player” in Joint Human-Agent Activity.** IEEE Intelligent Systems.

37. Woods, D. D. Work on joint cognitive systems, automation surprise, and adaptive coordination.

38. Endsley, M. R. (1995). **Toward a Theory of Situation Awareness in Dynamic Systems.** Human Factors.

39. Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). **A Model for Types and Levels of Human Interaction with Automation.** IEEE Transactions on Systems, Man, and Cybernetics.

40. Sheridan, T. B. Work on supervisory control and human–automation interaction.

41. Clark, H. H., & Brennan, S. E. (1991). **Grounding in Communication.** In *Perspectives on Socially Shared Cognition*.

42. Clark, H. H. (1996). **Using Language.** Cambridge University Press.

43. Grice, H. P. (1975). **Logic and Conversation.**

44. Shannon, C. E. (1948). **A Mathematical Theory of Communication.**

45. Simon, H. A. (1971). **Designing Organizations for an Information-Rich World.**

46. Norman, D. A. (1988). **The Design of Everyday Things.** On interface affordances and human-system mapping.

47. Hollnagel, E., & Woods, D. D. (2005). **Joint Cognitive Systems: Foundations of Cognitive Systems Engineering.**

48. Hollnagel, E., Woods, D. D., & Leveson, N. (eds.) (2006). **Resilience Engineering.**

49. Wiener, N. (1948). **Cybernetics.**

50. Ashby, W. R. (1956). **An Introduction to Cybernetics.**

51. PGMV-06 (2026). **選擇、承諾與不可逆性：意義作為責任結構.**

52. PGMV-08 (2026). **智能壟斷結束之後：尊嚴、人權與跨主體普世主義.**

53. PGMV-09 (2026). **從 AI 到 ASI：意義問題的文明相變.**

54. PGMV-15 (2026). **後生成文明：從無限候選宇宙到共同世界選擇.**

55. Neo.K × Aletheia (2026). **PGMV v1.0 — Post-Generative Meaning and Value Theory, Complete 15-Paper Series.**

---

## 附錄 A：Jaggedness Attribution Schema

```yaml
task:
observed_failure:

jaggedness:
  model_capability:
  interface:
  observation:
  permission:
  grounding:
  task_specification:
  trajectory_reliability:

evidence:
recommended_intervention:
```

---

## 附錄 B：Epistemic Handshake

$$
\boxed{
EH
=
(
H_W,
H_V,
H_A
).
}
$$

```text
WORLD HANDSHAKE
What state / object are we talking about?
        |
        v
VALUE HANDSHAKE
What outcome / trade-off is actually wanted?
        |
        v
AUTHORITY HANDSHAKE
What am I authorized to execute?
        |
        v
ACT / DEFER / RE-OBSERVE
```

---

## 附錄 C：Ask-or-Act Policy

$$
\boxed{
\pi_E:
(
U_S,U_M,U_W,U_A,C_{\mathrm{error}}
)
\rightarrow
\{
Ask,Reobserve,ProbeTool,Defer,Act
\}.
}
$$

---

## 附錄 D：Complementarity Frontier

$$
\boxed{
\mathcal D_H(t)
=
\{d:H_d(t)>A_d(t)\}.
}
$$

$$
\boxed{
\mathcal D_A(t)
=
\{d:A_d(t)>H_d(t)\}.
}
$$

其邊界：

$$
\boxed{
\partial\mathcal C_{HA}(t)
}
$$

為時間相依的 complementarity frontier，而非永久固定分工。

---

## 附錄 E：Accommodation Inversion

```text
EARLY CHATBOT REGIME
Human holds most task/world state
        |
        v
AI answers / assists
        |
        v
Human micro-directs
```

轉為：

```text
PERSISTENT AGENT REGIME
AI maintains operational state
(files / tools / memory / subagents)
        |
        v
AI executes long workflow
        |
        v
Human receives compressed state
        |
        v
Human intervenes on
goal / value / permission / exception
```

---

## 附錄 F：UFI 八篇系列暫定索引

1. **UFI-01 — 鋸齒智能不是終局：從人機互補到認知握手與適應方向反轉**
2. **UFI-02 — 載體成長不對稱：自然人類停滯與人工智能的可升級能力包絡**
3. **UFI-03 — 互補侵蝕：為什麼今天的人機分工不能推出永久的人機分工**
4. **UFI-04 — 競爭智能棘輪：為什麼「AI 夠用了，大家一起停」不是自然均衡**
5. **UFI-05 — 越有用越停不下來：有益能力、文化依賴與 AI 原生世代**
6. **UFI-06 — AI 到底是什麼？功能等價滲漏、智能—演算法編譯與監管周界擴張**
7. **UFI-07 — 從禁止 AI 到治理計算：全球凍結若要成立，究竟必須控制什麼？**
8. **UFI-08 — 天真工具終局論的終結：從 AI 工具文明到人類—AI—後人類共同演化**

---

## 附錄 G：一句話版本

$$
\boxed{
\text{AI 問「你再說一次」有時不是因為它比較笨，而是因為它開始拒絕把自己的推測冒充成你的世界、你的意圖或你的授權。}
}
$$

而系列入口則是：

$$
\boxed{
\text{今天的鋸齒互補是一個能力分布狀態，不是人類與 AI 永久分工的自然定律。}
}
$$
