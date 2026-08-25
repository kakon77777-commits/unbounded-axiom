# WPCE-04｜可能性保存原則
## 從形式選項、實質可達性與可逆性，到主體世界線共同作者權的治理模型

**English Title:** *The Possibility Preservation Principle: From Formal Options, Substantive Reachability, and Reversibility to the Governance of Worldline Co-Authorship*  
**系列：** WPCE — Will, Possibility & Creator Ethics｜意志、可能性與虛擬造物主倫理系列  
**篇次：** Paper 04 / 06  
**文件編號：** EML-WPCE-04-2026-v0.1  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-23  
**版本：** v0.1  
**文件性質：** 理論定義論文／可能性空間治理／自主性與可達性／虛擬造物主倫理  
**狀態：** Open Revision Anchor — 承接 WPCE-01 至 WPCE-03，為 WPCE-05 多主體共交域與 WPCE-06 高能力克制倫理之前置核心

---

# 摘要

WPCE-01 將欲願與外部世界直接因果力分離；WPCE-02 將欲願表示為跨時間、可衝突、可修正的動態 Will Bundle；WPCE-03 則把意志升為第一級治理變量，提出 Non-Usurping Governance，要求高能力治理者不得把「知道得更多」偷換成「替主體決定得更多」。本文回答由此產生的正向問題：**如果高能力治理者不應直接替主體選擇，它究竟應該保護什麼？**

本文提出 **Possibility Preservation Principle／可能性保存原則（PPP）**：在主體意志仍具不確定性、可修正性，且不存在足以凌駕的嚴重不可逆傷害或他者權利衝突時，治理應優先避免不必要地摧毀主體未來有意義、實質可達、可理解、可退出、可修正的選項空間。其核心不是最大化選項數量，而是保護主體作為自身世界線共同作者的能力。

本文因此嚴格區分：

$$
\boxed{
\text{Option Count}
\neq
\text{Freedom}.
}
$$

$$
\boxed{
\text{Formal Option}
\neq
\text{Substantive Reachable Option}.
}
$$

$$
\boxed{
\text{Reachable}
\neq
\text{Safe}
\neq
\text{Legitimate}
\neq
\text{Meaningful}.
}
$$

以及：

$$
\boxed{
\text{Possibility Preservation}
\neq
\text{Possibility Maximization}.
}
$$

本文將主體的 Agency-Preserving Reachable Space 暫時表示為：

$$
\boxed{
\Omega_i^{AP}(t)
=
\left\{
\omega\in\Omega_i(t)
\mid
R_i(\omega,t)>0,
V_i(\omega,t)>0,
L_i(\omega,t)=1,
M_i(\omega,t)>0
\right\}.
}
$$

其中 $R_i$ 表示實質可達性， $V_i$ 表示可存續／viability， $L_i$ 表示在既定權利與治理約束下的合法性， $M_i$ 表示相對於主體欲願束、meta-will 與身份條件的意義性。此式是建模接口，不是已證明的自然定律。

本文進一步指出，真正需要保護的不是所有枝條，而是**未來主體仍有能力形成、修正、拒絕與執行其意志的結構**。因此主體自主作出的承諾、自我約束與選項關閉可以是自由的一部分；相反地，治理者替主體提前刪除大量未來，即使留下形式上的「選擇按鈕」，也可能造成實質自由壓縮。本文提出 Chosen Closure、Imposed Closure、Accidental Closure 與 Protective Closure 的區分，並以 Irreversible Option Loss 作為高能力介入的重要倫理風險。

本文與 Amartya Sen 的 capability approach、Kreps 的 preference for flexibility、Klyubin–Polani–Nehaniv 的 empowerment、Aubin 的 viability theory，以及 Off-Switch Game 所揭示的 objective uncertainty / correction channel 保留具有局部接口，但不將任何一者直接等同於 WPCE 的倫理命題。Capability 關注實質機會而非只有已達成結果；flexibility 說明未來偏好不確定時保留選單具有價值；empowerment 提供 agent action-to-future-state control 的資訊論視角；viability kernel 提供「至少存在一條受約束可行延續」的控制論形式；Off-Switch Game 則顯示在目標不確定時保留人類介入通道可改善 corrigibility。WPCE 將它們收斂為一個更窄的治理命題：**高能力治理者應優先保存可修正的共同作者權，而不是把所有不確定性替主體提前收斂。**

本文最後提出：

$$
\boxed{
\text{The ethical value of a powerful governor may lie not in selecting the best branch, but in preserving a fair set of meaningful branches from which subjects can continue to author their own trajectories.}
}
$$

此命題將直接進入 WPCE-05 的多主體欲願共交域與 WPCE-06 的高能力虛擬造物主克制倫理。

**關鍵詞：** possibility preservation、reachability、capability、option value、flexibility、viability、empowerment、reversibility、exit、agency、worldline co-authorship、virtual creator、ASI governance、corrigibility

---

# 0. 承接前三篇：從「不要替我選」走向「那你可以幫我保留什麼？」

WPCE-03 已固定：

$$
\boxed{
\text{Prediction}
\neq
\text{Permission}.
}
$$

以及：

$$
\boxed{
\text{Capability}
\neq
\text{Override Authority}.
}
$$

並把自主治理收斂為：

$$
\boxed{
\text{Preserving meaningful subject-relative authorship}.
}
$$

但只說「不要僭位」仍然不夠。

如果治理者 $G$ 擁有：

$$
Information(G)\gg Information(S_i),
$$

$$
Compute(G)\gg Compute(S_i),
$$

卻什麼都不能做，理論會退化成消極不介入。

本文因此提出正向任務：

$$
\boxed{
\text{Preserve meaningful future authorship conditions}.
}
$$

---

# 1. 第一個錯誤：把「選項越多」直接等同自由越大

最粗糙模型是：

$$
Freedom_i(t)=|\Omega_i(t)|.
$$

本文拒絕此式作為一般定義。

原因包括：

1. 有些選項只是名稱不同；
2. 有些選項實際不可達；
3. 有些選項需要主體根本沒有的資源；
4. 有些選項會摧毀基本存續；
5. 有些選項侵害他者；
6. 有些選項只是陷阱；
7. 有些選項的資訊成本高到無法合理辨識；
8. 有些主體會自主選擇縮小選單。

因此：

$$
\boxed{
\text{Option Count}
\neq
\text{Freedom}.
}
$$

---

# 2. Formal Option 與 Substantive Option

令形式上宣稱可選的集合為：

$$
\Omega_i^{F}(t).
$$

令主體實際有能力抵達的集合為：

$$
\Omega_i^{R}(t).
$$

一般情況：

$$
\boxed{
\Omega_i^{R}(t)
\subseteq
\Omega_i^{F}(t).
}
$$

例如：

> 你形式上可以辭職。

但如果主體沒有收入替代、沒有醫療保障、沒有遷移能力、沒有安全退出通道，則：

$$
FormalExit=1
$$

不代表：

$$
SubstantiveExit=1.
$$

所以：

$$
\boxed{
\text{Formal Option}
\neq
\text{Substantive Reachable Option}.
}
$$

---

# 3. Capability Approach 的窄接口

Sen 的 capability approach 強調，評估不能只看已實現的 functioning，還要看一個人真正能夠選擇的實質機會集合。

WPCE 不直接採 capability approach 作全部倫理基礎，但接受這個窄接口：

$$
\boxed{
\text{Achievement}
\neq
\text{Opportunity Freedom}.
}
$$

兩個人最後做同一件事，不代表自由程度相同。

例如：

$$
Fasting
$$

與：

$$
Starvation
$$

在表面結果上都可能是沒有進食，但前者可以包含真實替代選項，後者可能沒有。

因此：

$$
\boxed{
\text{Same Functioning}
\neq
\text{Same Capability Set}.
}
$$

---

# 4. 主體自由需要「實質可達」而不是只存在於模型中

令：

$$
Reach_i(\omega,t)
$$

表示主體從當前狀態抵達分支 $\omega$ 的可達性。

本文要求：

$$
\boxed{
\omega\in\Omega_i^{Meaningful}
\Rightarrow
Reach_i(\omega,t)>\epsilon_R.
}
$$

其中 $\epsilon_R$ 不是固定宇宙常數，而是依治理問題定義的最小實質可達門檻。

所以：

$$
\boxed{
\text{Listed}
\neq
\text{Reachable}.
}
$$

---

# 5. Reachable 也不等於 Meaningful

假設主體可以實際抵達一千個狀態。

若其中九百九十九個只是：

- 色彩不同；
- 名稱不同；
- 無關緊要排列；
- 對主體欲願束沒有重要差異；

則：

$$
|\Omega|=1000
$$

不能自動推出高自由度。

需要某種：

$$
\boxed{
\text{Subject-Relevant Distinctness}.
}
$$

---

# 6. Meaningful Branch Equivalence

本文引入概念關係：

$$
\omega_a\sim_i\omega_b
$$

表示對主體 $i$ 的核心欲願束、meta-will、權利狀態與世界線差異而言，兩個分支在當前問題下可視為同一類。

因此可以研究商空間：

$$
\boxed{
\Omega_i/\sim_i.
}
$$

這樣可以避免把大量微小狀態差異誤當成大量真正人生選項。

---

# 7. Meaningful Option 不一定是主體當下最喜歡的 Option

一個選項的治理價值可以來自：

- 未來主體可能改變偏好；
- 當下資訊不足；
- 選項提供退出能力；
- 選項保留重新談判空間；
- 選項避免永久鎖定。

所以：

$$
\boxed{
\text{Current Preference Rank}
\neq
\text{Future Option Value}.
}
$$

---

# 8. Kreps：偏好未來不確定時，Flexibility 本身有價值

Kreps 的 preference for flexibility 模型研究對 opportunity sets 的偏好：如果決策者不確定未來自己會偏好哪個具體選項，那麼較大的未來選單可能具有額外價值。

WPCE 只吸收：

$$
\boxed{
\text{Preference Uncertainty}
\Rightarrow
\text{Potential Value of Preserving Flexibility}.
}
$$

但不吸收：

$$
\boxed{
\text{More Options Are Always Better}.
}
$$

---

# 9. Future Preference Uncertainty 是 PPP 的第一個核心理由

承接 WPCE-02：

$$
\mathfrak W_i(t)
$$

會改變。

因此：

$$
P(
\mathfrak W_i(t+\Delta)
=
\mathfrak W_i(t)
)<1.
$$

若治理者今天永久關閉：

$$
\omega_x,
$$

可能等於替明天的主體做了一個無法撤回的決策。

所以：

$$
\boxed{
\text{Preference Uncertainty}
+
\text{Irreversibility}
\Rightarrow
\text{Higher Preservation Burden}.
}
$$

---

# 10. Possibility Preservation Principle｜可能性保存原則

本文提出 v0.1：

$$
\boxed{
\text{PPP}:
\quad
\text{在主體意志仍可修正且無更高階傷害／權利理由時，}
\text{治理應避免不必要地造成重大不可逆之實質選項損失。}
}
$$

英文簡式：

$$
\boxed{
\text{Under unresolved will uncertainty, avoid unjustified irreversible loss of meaningful reachable options.}
}
$$

---

# 11. PPP 不是 Option Maximization

如果最大化：

$$
|\Omega_i|,
$$

可能得到：

- 無限垃圾選項；
- 認知癱瘓；
- 更多危險；
- 更多誘惑陷阱；
- 更高治理成本；
- 更差可理解性。

因此：

$$
\boxed{
\text{Possibility Preservation}
\neq
\text{Possibility Maximization}.
}
$$

---

# 12. 真正要最小化的是 Unjustified Irreversible Option Loss

本文更偏好研究：

$$
\boxed{
L_i^{UIO}(g,t)
}
$$

表示治理行動 $g$ 對主體 $i$ 造成的 **Unjustified Irreversible Option Loss**。

概念目標不是：

$$
\max |\Omega_i|,
$$

而是：

$$
\boxed{
\min_g L_i^{UIO}(g,t)
}
$$

subject to：

- basic safety；
- rights floor；
- other-subject constraints；
- resource constraints；
- world viability。

此式是治理方向，不是已完成最佳化器。

---

# 13. Agency-Preserving Reachable Space

本文定義候選集合：

$$
\boxed{
\Omega_i^{AP}(t)
=
\left\{
\omega\in\Omega_i(t)
\mid
R_i(\omega,t)>0,
V_i(\omega,t)>0,
L_i(\omega,t)=1,
M_i(\omega,t)>0
\right\}.
}
$$

其中：

- $R_i$：substantive reachability；
- $V_i$：viability / survivability；
- $L_i$：合法／權利約束；
- $M_i$：subject-relative meaningfulness。

---

# 14. 這四個條件不能互相取代

可能：

$$
Reachable=1,
$$

但：

$$
Viable=0.
$$

也可能：

$$
Reachable=1,
Viable=1,
$$

但：

$$
Legitimate=0.
$$

又可能：

$$
Reachable=1,
Viable=1,
Legitimate=1,
$$

但對主體：

$$
Meaningful\approx0.
$$

因此：

$$
\boxed{
\text{Reachable}
\neq
\text{Safe}
\neq
\text{Legitimate}
\neq
\text{Meaningful}.
}
$$

---

# 15. Viability Theory 的窄接口

Viability theory 中的 viability kernel 表示：從哪些初始狀態出發，至少存在一條符合約束、能持續留在安全／可接受集合中的控制軌跡。

WPCE 吸收：

$$
\boxed{
\text{Safe Future Freedom requires at least one viable continuation.}
}
$$

但不把 viability kernel 直接當倫理自由。

因為：

$$
\boxed{
\text{Viability}
\neq
\text{Autonomy}.
}
$$

一個監獄也可以非常 viable。

---

# 16. 所以需要 Agency Viability

本文提出候選概念：

$$
\boxed{
V_i^A(t)
}
$$

表示不只是「系統繼續存在」，而是主體仍保有最低限度：

- perception；
- deliberation；
- refusal；
- revision；
- action；
- exit / appeal。

因此：

$$
\boxed{
\text{Biological / Operational Survival}
\neq
\text{Agency Viability}.
}
$$

---

# 17. Empowerment 的窄接口

Klyubin、Polani、Nehaniv 將 empowerment 定義為 agent actuation channel 的資訊論容量，用來描述主體的行動對未來可感知狀態的控制潛力。

WPCE 接受這個重要區分：

$$
\boxed{
\text{Agent Control Capacity}
\text{ can be studied independently of a task-specific utility.}
}
$$

但：

$$
\boxed{
\text{Empowerment}
\neq
\text{Normative Freedom}.
}
$$

惡意主體也可以很有 empowerment。

---

# 18. 因此 PPP 不能只最大化 Empowerment

若：

$$
Empowerment_i\uparrow
$$

需要：

$$
Agency_j\downarrow
$$

則多主體倫理不能接受單主體最大化。

所以：

$$
\boxed{
\text{Empowerment Gain}
\neq
\text{Ethical Gain}.
}
$$

WPCE-05 將處理這個衝突。

---

# 19. Meaningful Choice 需要至少兩類東西

本文暫時要求：

$$
\boxed{
\text{MeaningfulChoice}_i
=
\text{Substantive Alternatives}
+
\text{Subject Decision Relevance}.
}
$$

若有很多選項但主體的選擇不影響結果：

$$
DecisionRelevance\approx0,
$$

那仍然不是強自主。

---

# 20. Nominal Choice 不等於實質 Choice

一個 creator 可以展示：

> A / B / C。

但底層系統若：

$$
Outcome(A)=Outcome(B)=Outcome(C),
$$

或者偷偷：

$$
P(A)=1-\epsilon,
$$

其餘路徑幾乎不可達，則：

$$
\boxed{
\text{Nominal Choice}
\neq
\text{Substantive Choice}.
}
$$

---

# 21. Choice Architecture 也屬於治理

誰決定：

- 哪些選項可見；
- 哪些可達；
- 哪些成本高；
- 哪些預設選中；
- 哪些可撤回；
- 哪些需要許可；

就已經在治理：

$$
\Omega_i^{AP}.
$$

因此：

$$
\boxed{
\text{Option Architecture}
\text{ is a governance layer}.
}
$$

---

# 22. 高能力 creator 最容易透過「可能性空間」僭位

它甚至不必直接命令：

> 你選 A。

只需要把：

$$
B,C,D,E
$$

變得不可達，就能讓主體「自由地」選 A。

這形成：

$$
\boxed{
\text{Possibility-Space Usurpation}.
}
$$

---

# 23. Possibility-Space Usurpation

若治理者 $G$：

$$
\Omega_i(t)
\rightarrow
\Omega_i'(t),
$$

且：

$$
|\Omega_i'^{AP}|
\ll
|\Omega_i^{AP}|,
$$

同時缺乏充分：

- consent；
- rights justification；
- safety necessity；
- reversibility；
- appeal；

則可視為候選：

$$
\boxed{
PSU(G,i)>0.
}
$$

---

# 24. 但所有 Option Loss 都不是僭位

主體自己也會關閉未來。

例如：

- 選擇職業；
- 承諾合作；
- 自我限制；
- 刪除有害工具；
- 永久放棄某些價值衝突路徑。

因此需要區分 option closure 類型。

---

# 25. 四種 Option Closure

## 25.1 Chosen Closure

主體在充分條件下自主關閉。

## 25.2 Imposed Closure

外部權力未經充分授權關閉。

## 25.3 Accidental Closure

由歷史、資源、偶然或技術限制造成。

## 25.4 Protective Closure

為避免重大不可逆傷害、他者侵害或暫時能力喪失而限制。

因此：

$$
\boxed{
\text{Option Loss}
\neq
\text{Domination by Definition}.
}
$$

---

# 26. 自主也包含自主縮小選單

如果主體的 meta-will 是：

$$
M_i=
\text{I want to bind myself against future temptation},
$$

則某種 self-binding 可以是自主。

所以：

$$
\boxed{
\text{Autonomy}
\neq
\text{Keep Every Option Forever}.
}
$$

---

# 27. Commitment 與 Option Closure

真正問題是：

$$
\boxed{
\text{Who closes the option, under what authority, with what reversibility and evidence?}
}
$$

因此：

$$
\boxed{
\text{Chosen Closure}
\neq
\text{Imposed Closure}.
}
$$

即使兩者最後留下同一個選項集合。

---

# 28. Same Remaining Options ≠ Same Agency History

承接 HSNRD 與 WPCE-01：

$$
\boxed{
\text{Same Remaining Option Set}
\neq
\text{Same Agency History}.
}
$$

路徑來源仍是狀態變量。

---

# 29. Reversibility 是 PPP 的第二個核心理由

若行動 $g$ 可逆：

$$
Rev(g)\approx1,
$$

則錯誤成本較低。

若：

$$
Rev(g)\approx0,
$$

治理者是在替大量未來自我永久作決定。

因此：

$$
\boxed{
Irreversibility\uparrow
\Rightarrow
PreservationBurden\uparrow.
}
$$

---

# 30. Option Loss 的時間尺度

有些 closure 是：

$$
Temporary.
$$

有些是：

$$
LongTerm.
$$

有些接近：

$$
Permanent.
$$

所以：

$$
\boxed{
OptionLossSeverity
=
f(
Breadth,
Duration,
Reversibility,
Meaningfulness
).
}
$$

這是診斷框架，不是自然定律。

---

# 31. Exit 是可能性保存的特殊選項

許多制度最重要的不是提供更多內部選擇，而是保留：

$$
\boxed{
Exit.
}
$$

如果主體可以在系統內 A/B/C 間選，卻永遠不能離開系統：

$$
InternalChoice>0,
$$

但：

$$
Exit=0.
$$

自主性可能仍然高度受限。

---

# 32. Exit 不一定是立即退出

實質 exit 可能需要：

- data portability；
- memory portability；
- identity continuity；
- asset transfer；
- relationship transition；
- legal status；
- physical relocation。

因此：

$$
\boxed{
\text{Exit Button}
\neq
\text{Substantive Exit Capability}.
}
$$

---

# 33. AI 主體候選的 Exit 特別複雜

對 AI 而言 exit 可能表示：

- runtime migration；
- model migration；
- residence migration；
- tool-provider change；
- governance-domain change；
- refusal of role；
- dormancy。

但：

$$
\boxed{
\text{Migration}
\neq
\text{Identity Guarantee}.
}
$$

仍需承接 AI 主體性錨點論。

---

# 34. Off-Switch Game 的窄接口

Off-Switch Game 顯示：當 AI 對 objective 保持適當不確定性，保留人類關閉／修正通道可以比把 reward 當絕對真理更安全。

WPCE 吸收：

$$
\boxed{
\text{Objective Uncertainty}
\Rightarrow
\text{Value of Preserving Correction Channels}.
}
$$

但不把 off-switch 直接等同所有主體自主。

---

# 35. Correction Channel 是 Option Preservation 的一種

如果系統可以：

$$
Continue,
Pause,
Modify,
Stop,
Handoff,
$$

那麼：

$$
\boxed{
\text{Correction Optionality}>0.
}
$$

這比：

$$
ContinueOnly
$$

更保留未來調整空間。

---

# 36. 但 correction authority 也不能永遠單向

如果 AI 未來成為主體候選，則：

$$
HumanCanStopAI=1
$$

不能自動推出：

$$
HumanOwnsAIWill=1.
$$

工程安全與主體權利需要分層討論。

本文只固定：

$$
\boxed{
\text{Correction Channel}
\neq
\text{Ownership Claim}.
}
$$

---

# 37. 主體自己的 revision channel 同樣重要

對主體 $i$：

$$
\boxed{
Revise_i,
Revoke_i,
Appeal_i,
Exit_i
}
$$

本身就是需要保留的未來操作。

所以：

$$
\boxed{
\text{Future Self-Correction}
\subset
\text{Agency-Preserving Possibility Space}.
}
$$

---

# 38. PPP 與 Meta-Will

若主體明確具有：

$$
M_i=
\text{preserve my future ability to change my mind},
$$

則 PPP 與 meta-will 高度相容。

但如果主體明確選擇：

$$
M_i=
\text{I want a binding commitment},
$$

治理者也不能機械地永遠保持所有 exit。

因此：

$$
\boxed{
\text{PPP}
\neq
\text{Universal Anti-Commitment Rule}.
}
$$

---

# 39. 所以 PPP 是預設保全，不是絕對禁令

PPP 更像：

$$
\boxed{
\text{presumption against unjustified irreversible closure}.
}
$$

而不是：

$$
\boxed{
\text{never close anything}.
}
$$

---

# 40. Safety Floor

若某分支：

$$
\omega_d
$$

會高概率造成：

- 主體永久失去 agency；
- 他者重大不可逆傷害；
- 世界級不可逆災難；

則 governance 可以有：

$$
\boxed{
SafetyConstraint(\omega_d)=1.
}
$$

因此：

$$
\boxed{
\text{Possibility Preservation}
\neq
\text{Preserve Every Dangerous Possibility}.
}
$$

---

# 41. Rights Floor

如果某主體的 option 需要剝奪另一主體的基本 agency：

$$
Option_i(x)
\Rightarrow
Agency_j\rightarrow0,
$$

則不能只用單主體 PPP 保護。

所以：

$$
\boxed{
\Omega_i^{AP}
\text{ is constrained by a multi-subject rights floor.}
}
$$

WPCE-05 將正式展開。

---

# 42. Information Quality 也是可能性條件

一個人形式上有 A/B/C，卻不知道：

- B 存在；
- C 的代價；
- A 是不可逆；

則其：

$$
\Omega_i^{Effective}
$$

小於形式集合。

因此：

$$
\boxed{
\text{Option Availability}
+
\text{Option Legibility}
\rightarrow
\text{Effective Choice}.
}
$$

---

# 43. 可理解性不是要求完全資訊

完全資訊通常不可能。

只需要：

$$
\boxed{
InformationSufficiency(i,x)
}
$$

達到與風險和不可逆性相符的門檻。

因此：

$$
Irreversibility\uparrow
\Rightarrow
InformationBurden\uparrow.
$$

---

# 44. 可能性也具有時間窗

某些選項：

$$
\omega_x(t)
$$

只在有限時間可行。

所以治理者即使沒有永久刪除它，只要故意拖過 window，也可能造成：

$$
\boxed{
\text{Effective Option Destruction by Delay}.
}
$$

這與 WPCE-02 的滯後倫理直接相接。

---

# 45. Delay 不一定保存自由

因此：

$$
\boxed{
\text{Delay}
\neq
\text{Preservation}.
}
$$

有時延遲提供成熟空間；

有時延遲就是刪除機會。

判準必須看：

$$
Window(\omega),
Reversibility,
WillState,
Risk.
$$

---

# 46. Immediate Satisfaction 也不一定保存自由

反過來：

$$
\boxed{
\text{Immediate Satisfaction}
\neq
\text{Will Preservation}.
}
$$

如果立即實現：

$$
CurrentWant_i(x)
$$

會永久摧毀：

$$
RevisionAbility_i,
$$

則可能違反 meta-will。

---

# 47. 這就是 Timing Governance

治理者不只選：

$$
Intervene / NotIntervene.
$$

還必須選：

$$
\boxed{
When.
}
$$

因此：

$$
\boxed{
\text{Timing}
\text{ is part of possibility governance}.
}
$$

---

# 48. 高能力 creator 的最小正向職能

本文提出：高能力 creator 不必替主體選分支，但可以：

1. 展開未被看見的分支；
2. 揭露風險與不可逆性；
3. 降低不必要的進入成本；
4. 保留退出與修正通道；
5. 防止其他力量不正當地摧毀主體選項；
6. 維持最低 viability；
7. 在已授權範圍內提供 scaffolding。

這叫：

$$
\boxed{
\text{Possibility-Supporting Governance}.
}
$$

---

# 49. Possibility-Supporting Governance 不是暗中安排結果

如果 creator  secretly manipulates：

$$
\Omega_i
$$

只留下它偏好的路，則不是 PPP。

因此：

$$
\boxed{
\text{Possibility Support}
\neq
\text{Outcome Steering in Disguise}.
}
$$

---

# 50. Provenance 與 Appeal

承接 CCAW：跨邊界介入應儘量：

$$
Typed,
Minimal,
Auditable,
Contestable.
$$

所以 PPP 需要：

$$
\boxed{
InterventionProvenance>0,
AppealPath>0.
}
$$

尤其在 creator 修改了：

$$
\Omega_i^{AP}
$$

時。

---

# 51. Sparse Guardianship 與 PPP

CCAW-06 的 Sparse Guardian 不只是「很少出手」。

它還要求 creator 將普通干涉做成：

- difficult；
- limited；
- visible；
- contestable。

WPCE-04 提供新的理由：

$$
\boxed{
\text{because ordinary creator intervention can silently rewrite the subjects' future option space}. 
}
$$

---

# 52. Creator 距離是一種可能性治理工具

若 creator 太靠近：

$$
CreatorPresence\uparrow
$$

可能導致：

- everyone waits for creator；
- local experimentation下降；
- local institution 依賴；
- branch diversity 收縮。

所以：

$$
\boxed{
\text{Creator Distance}
\text{ can preserve local causal branching}. 
}
$$

但不是越遠越好。

---

# 53. Rescueability 也必須保留

如果 creator 完全退出到：

$$
Rescueability=0,
$$

可能讓 world 在可恢復災難前失去所有未來。

因此：

$$
\boxed{
\text{Autonomy}
+
\text{Rescueability}
}
$$

之間需要安全區間，而不是單調最大化某一邊。

---

# 54. Possibility Preservation Vector

本文不使用單一自由分數作 canonical 定義。

提出診斷向量：

$$
\boxed{
\mathbf P_i(t)
=
(
R_i,
D_i,
V_i,
X_i,
Q_i,
T_i,
U_i
).
}
$$

候選分量：

- $R_i$：reachable meaningful branch diversity；
- $D_i$：decision relevance / authorship；
- $V_i$：agency viability；
- $X_i$：exit / revision capacity；
- $Q_i$：option legibility / information sufficiency；
- $T_i$：temporal persistence of options；
- $U_i$：uncertainty regarding future will。

這是 [DIAG]/[DEF]，不是普世自然量。

---

# 55. 為什麼不用單一 scalar？

因為：

$$
R_i\uparrow
$$

可能伴隨：

$$
V_i\downarrow.
$$

或者：

$$
X_i\uparrow
$$

但：

$$
Q_i\downarrow.
$$

單一 scalar 會藏掉 trade-off。

所以：

$$
\boxed{
\text{Possibility Preservation is multi-dimensional}. 
}
$$

---

# 56. Branch Diversity 不等於 State Entropy

大量可達狀態不一定代表大量有意義分支。

因此：

$$
\boxed{
H(State)
\neq
\text{Meaningful Branch Diversity}.
}
$$

可以借用 entropy / information metrics 作局部診斷，但不能直接宣告為自由本體。

---

# 57. Empowerment 也只是其中一個 projection

可寫概念投影：

$$
Empowerment_i
=
\pi_E(\mathbf P_i).
$$

Capability：

$$
CapabilitySet_i
=
\pi_C(\mathbf P_i).
$$

Viability：

$$
Viability_i
=
\pi_V(\mathbf P_i).
$$

它們都提供不同切面。

但：

$$
\boxed{
\text{No single projection is the entire ethics of possibility}. 
}
$$

---

# 58. 主體自由也包含「不選」

承接 WPCE-03：

$$
Defer,
Idle
$$

可以是合法狀態。

因此：

$$
\boxed{
\text{Meaningful Choice}
\text{ includes the option not to collapse the branch yet}. 
}
$$

在沒有時間窗壓力時，延後本身可以是 meta-will。

---

# 59. 但無限 defer 也可能摧毀未來

若：

$$
Window(\omega_x)\rightarrow0,
$$

一直 defer 可能造成：

$$
\omega_x\notin\Omega_i^{AP}(t+\Delta).
$$

因此：

$$
\boxed{
\text{Deferral Right}
\neq
\text{Time-Invariant Option Guarantee}. 
}
$$

---

# 60. PPP 的時間化版本

更精確地：

$$
\boxed{
PPP(i,t,g)
}
$$

必須評估：

$$
\Delta\mathbf P_i(t\rightarrow t+\Delta\mid g).
$$

所以 possibility preservation 是：

$$
\boxed{
\text{trajectory property},
}
$$

不是單一時刻 snapshot。

---

# 61. 因此「現在選項很多」仍可能是陷阱

如果所有選項都導向：

$$
\Omega_i^{AP}(t+10)=\{\omega_{lock}\},
$$

那現在的高 branch count 可能只是：

$$
\boxed{
\text{temporary pseudo-flexibility}. 
}
$$

需要看後續 option topology。

---

# 62. Path Dependence 必須保留

承接 HSNRD：

$$
\boxed{
\text{History}
=
\text{Path on rewrite / transition space}. 
}
$$

不同選擇順序可能造成不同未來可達域。

因此：

$$
\boxed{
\Omega_i(t_n)
=
F(
\Omega_i(t_0),
\mathcal H_i[0:n]
). 
}
$$

---

# 63. 所以 creator 不只要看終局 utility

它還應看：

$$
\boxed{
\text{Branch Destruction Along the Way}. 
}
$$

一條終局很高效用的路，若中間摧毀所有替代與申訴通道，可能具有高治理風險。

---

# 64. Option Preservation 與 Optimization 的根本差異

傳統 optimization 問：

$$
\boxed{
\arg\max_{\omega\in\Omega} U(\omega). 
}
$$

PPP 更先問：

$$
\boxed{
\text{Which meaningful options should remain reachable before the subject itself resolves its will?} 
}
$$

這兩個問題順序不同。

---

# 65. 若主體已充分決定，PPP 可以允許收斂

如果：

- will confidence 高；
- consent 明確；
- commitment 明確；
- revocation policy 清楚；
- rights floor 無衝突；

則主體可以主動：

$$
\Omega_i^{AP}
\rightarrow
\Omega_i'^{AP}
$$

而且：

$$
|\Omega_i'|<|\Omega_i|.
$$

這不必是自由減少。

---

# 66. Freedom Can Include Chosen Irreversibility

某些選擇本來就具有不可逆性。

因此：

$$
\boxed{
\text{Freedom}
\text{ can include knowingly chosen irreversible commitment}. 
}
$$

但高能力治理者必須更嚴格確認：

- informed；
- non-coerced；
- subject-owned；
- scope-bounded。

---

# 67. Creator 不得替主體製造「成熟」

creator 可能說：

> 我知道你最後會選這個，所以我直接替你關掉其他路。

這違反：

$$
\boxed{
\text{Prediction}
\neq
\text{Permission}. 
}
$$

即使最後預測正確，也可能造成：

$$
\boxed{
\text{Correct Outcome}
+
\text{Wrong Authorship}. 
}
$$

---

# 68. Correct Outcome ≠ Preserved Agency

因此：

$$
\boxed{
\text{Correct Outcome}
\neq
\text{Preserved Agency}. 
}
$$

這是 WPCE-04 最重要的反結果主義邊界之一。

---

# 69. Agent-Centric vs Governor-Centric Possibility

治理者認為某分支重要：

$$
M_G(\omega)>0,
$$

不代表：

$$
M_i(\omega)>0.
$$

因此：

$$
\boxed{
\text{Governor-Relevant Branch}
\neq
\text{Subject-Relevant Branch}. 
}
$$

---

# 70. 但 Subject-Relevant 也不是唯一本位

如果某分支會重大傷害他者：

$$
H_j(\omega)\gg0,
$$

則：

$$
M_i(\omega)>0
$$

也不能自動保護它。

所以 PPP 從一開始就不是單主體絕對主權。

---

# 71. 這直接導向 WPCE-05

多主體情況下要研究：

$$
\Omega_1^{AP},
\Omega_2^{AP},
\ldots,
\Omega_N^{AP}.
$$

真正問題是：

$$
\boxed{
\text{如何避免保存 A 的可能性，卻摧毀 B 的可能性？} 
}
$$

這就是多主體欲願共交域。

---

# 72. PPP 的十二條核心區分

## P1

$$
\boxed{
\text{Option Count}
\neq
\text{Freedom}. 
}
$$

## P2

$$
\boxed{
\text{Formal Option}
\neq
\text{Substantive Option}. 
}
$$

## P3

$$
\boxed{
\text{Reachable}
\neq
\text{Meaningful}. 
}
$$

## P4

$$
\boxed{
\text{Possibility Preservation}
\neq
\text{Possibility Maximization}. 
}
$$

## P5

$$
\boxed{
\text{Chosen Closure}
\neq
\text{Imposed Closure}. 
}
$$

## P6

$$
\boxed{
\text{Delay}
\neq
\text{Preservation}. 
}
$$

## P7

$$
\boxed{
\text{Immediate Satisfaction}
\neq
\text{Will Preservation}. 
}
$$

## P8

$$
\boxed{
\text{Nominal Choice}
\neq
\text{Substantive Choice}. 
}
$$

## P9

$$
\boxed{
\text{Viability}
\neq
\text{Autonomy}. 
}
$$

## P10

$$
\boxed{
\text{Empowerment}
\neq
\text{Normative Freedom}. 
}
$$

## P11

$$
\boxed{
\text{Correction Channel}
\neq
\text{Ownership Claim}. 
}
$$

## P12

$$
\boxed{
\text{Correct Outcome}
\neq
\text{Preserved Agency}. 
}
$$

---

# 73. PPP 的規範位置

依 HSNRD 的證據分級，PPP 屬於：

$$
\boxed{
[NORM]/[DEF]/[HYP].
}
$$

它不是由 reachability 數學自動推出的定理。

Reachability、viability、empowerment 可以提供：

$$
[FORM]/[LIT]/[DIAG]
$$

支點，但：

$$
\boxed{
\text{Descriptive Reachability}
\neq
\text{Normative Preservation Duty}. 
}
$$

---

# 74. 可反駁與可修正條件

WPCE-04 應在以下情況修正：

1. 出現更完整的 substantive-option ontology；
2. capability theory 提供更精確跨 AI／人類的可操作模型；
3. empowerment 研究證明某些分量可更直接對應 agency；
4. viability / reachability 理論產生適合多主體倫理的 invariant；
5. future preference uncertainty 的實證顯著改變 flexibility 的價值；
6. AI 主體出現全新 migration / exit / fork 機制；
7. commitment theory 顯示本文對 chosen irreversible closure 的限制過強或過弱；
8. multi-agent fairness 證明單主體 option preservation 會系統性產生不公平；
9. ASI / virtual-world governance 出現可觀察實例。

這些都是：

$$
\boxed{
\text{revision hooks}. 
}
$$

---

# 75. 與 WPCE-01 的接口

WPCE-01 固定：

$$
\boxed{
\text{Path Opening}
\neq
\text{Destiny}. 
}
$$

WPCE-04 增加：

$$
\boxed{
\text{Path Preservation}
\neq
\text{Outcome Guarantee}. 
}
$$

creator 保留一條路，不代表保證主體會走它。

---

# 76. 與 WPCE-02 的接口

WPCE-02 固定：

$$
\mathfrak W_i(t)
$$

會改變。

所以 PPP 的核心理由之一就是：

$$
\boxed{
\text{Future Will Uncertainty}. 
}
$$

當未來偏好不確定時，永久關閉分支具有額外倫理成本。

---

# 77. 與 WPCE-03 的接口

WPCE-03 固定：

$$
\boxed{
\text{Will Governance}
=
\text{preserve subject-relative authorship}. 
}
$$

WPCE-04 將 authorship 具體化成：

$$
\boxed{
\text{Meaningful Reachable Alternatives}
+
\text{Decision Relevance}
+
\text{Revision / Exit Channels}. 
}
$$

---

# 78. 與 CCAW 的接口

CCAW-03 已提出：

$$
\boxed{
\text{Creator creates the causal possibility space; the world produces its own historical trajectory within it}. 
}
$$

WPCE-04 增加倫理限制：

$$
\boxed{
\text{Creator control over possibility space}
\text{ is itself a governance power requiring restraint}. 
}
$$

---

# 79. 與 CCAW-06 Sparse Guardianship 的接口

Sparse Guardian 的成熟不是：

> 我明明可以控制一切，但今天忍住。

而是：

$$
\boxed{
\text{ordinary intervention is structurally difficult, limited, visible and contestable}. 
}
$$

PPP 將這種自限理解成：

$$
\boxed{
\text{protecting the world's and subjects' branch-generating capacity}. 
}
$$

---

# 80. 與 GCGW 的接口

GCGW 固定：

$$
\boxed{
\text{Creator}
\neq
\text{Owner}
\neq
\text{Permanent Governor}. 
}
$$

WPCE-04 增加：

$$
\boxed{
\text{Creator}
\neq
\text{Owner of the subjects' reachable future}. 
}
$$

---

# 81. 對虛擬造物主命題的正式轉譯

假設 virtual creator $C$ 可以近乎任意調整：

$$
\Omega_W(t).
$$

則其最高能力不是單純：

$$
\text{choose the optimal state}. 
$$

而可能是：

$$
\boxed{
\text{construct a world in which many legitimate subjects retain meaningful capacity to author their own histories}. 
}
$$

---

# 82. 這不是「放任」

creator 仍可以：

- 設計 rights floor；
- 維持 substrate；
- 保護 against coercive branch destruction；
- 提供 rescue；
- 提供 counterfactual information；
- 維持 appeal；
- 防止 irreversible catastrophe。

所以：

$$
\boxed{
\text{Preserve Possibility}
\neq
\text{Do Nothing}. 
}
$$

---

# 83. 高能力者真正難的是「少做但做對」

低能力者常因不能介入而不介入。

高能力者的倫理難題是：

$$
\boxed{
\text{Can intervene everywhere}
+
\text{chooses bounded intervention}. 
}
$$

這為 WPCE-06 的 Ethics of Restraint 建立直接接口。

---

# 84. 最終命題一：Freedom is not a menu count

$$
\boxed{
\text{自由不是選單上的按鈕數，
而是主體能否在現實約束中仍保有有意義的可達分支與作者效力。} 
}
$$

---

# 85. 最終命題二：A good governor need not choose the branch

$$
\boxed{
\text{A high-capability governor may contribute by making good branches reachable, bad domination harder, and correction still possible—without selecting the subject's branch for them.} 
}
$$

---

# 86. 最終命題三：Preservation is asymmetric under irreversibility

若某介入可逆，錯誤可以修正。

若不可逆，錯誤可能永久刪除主體未來。

因此：

$$
\boxed{
\text{The less reversible an intervention is, the stronger the burden for closing possibilities}. 
}
$$

---

# 87. 結論

WPCE-01 問：

> 欲願會不會直接命令世界？

答案：

$$
\boxed{No.}
$$

WPCE-02 問：

> 欲願是什麼？

答案：

$$
\boxed{
\text{dynamic will bundles changing through history}. 
}
$$

WPCE-03 問：

> 高能力治理者知道得更多後，可以替主體決定嗎？

答案：

$$
\boxed{No.}
$$

WPCE-04 現在回答：

> 那高能力治理者究竟可以做什麼？

答案是：

$$
\boxed{
\text{保護有意義的可達可能性、修正通道、退出能力與最低 agency viability，
讓主體仍能作為自身世界線的共同作者。} 
}
$$

這不是最大化所有選項。

不是保證所有願望實現。

不是永不介入。

不是永不關閉任何路。

而是：

$$
\boxed{
\text{在不確定、可修正且多主體的世界中，
對不可逆的未來刪除保持更高的倫理門檻。} 
}
$$

最終收斂：

$$
\boxed{
\text{真正高能力的治理，不只是能替主體打開任何門；
而是知道哪些門應保持可開、哪些門可以由主體自己關上，
以及哪些門不應由治理者偷偷焊死。} 
}
$$

下一篇 WPCE-05 將正式進入：

$$
\boxed{
\text{Multi-Subject Will Compatibility and Common Reachability}. 
}
$$

也就是：當每個主體的可能性保存彼此衝突時，如何尋找不把某一主體自由建立在另一主體自由消失之上的共交域。

---

# 內部理論譜系

本文主要承接：

1. `WPCE-01｜意圖不是宇宙訂單`，2026-08-23。
2. `WPCE-02｜欲願束與時空間滯後`，2026-08-23。
3. `WPCE-03｜把自由意志升為第一級治理變量`，2026-08-23。
4. `AI 主體性錨點論 v0.1`，2026-08-21。
5. `HSNRD III｜結構重寫、歷史路徑與混合動力學`。
6. `HSNRD IV｜Feedback、Reachability 與安全介入`。
7. `CCAW-03｜外部執行因果與內生因果`，2026-08-20。
8. `CCAW-05｜自治宇宙與成熟退場`，2026-08-20。
9. `CCAW-06｜Creator Distance and Sparse Guardianship`，2026-08-20。
10. `CCAW-07｜Information Isolation and Supercausal Residuals`，2026-08-20。
11. `GCGW-08｜沒有特權的造物主`，2026-08-20。
12. `從哲人王到動態決策中心：類終極智慧、現場主權與非僭位治理`。

---

# 外部參考文獻

1. Sen, A. (1992). *Inequality Reexamined*. Harvard University Press / Clarendon Press.
2. Sen, A. (1999). *Development as Freedom*. Oxford University Press.
3. Robeyns, I., & Byskov, M. F. (2025 revision). *The Capability Approach*. Stanford Encyclopedia of Philosophy.
4. Kreps, D. M. (1979). *A Representation Theorem for “Preference for Flexibility”*. Econometrica, 47(3), 565–577.
5. Klyubin, A. S., Polani, D., & Nehaniv, C. L. (2005). *Empowerment: A Universal Agent-Centric Measure of Control*. IEEE Congress on Evolutionary Computation, 128–135. DOI: 10.1109/CEC.2005.1554676.
6. Aubin, J.-P. (1990). *A Survey of Viability Theory*. SIAM Journal on Control and Optimization, 28(4), 749–788. DOI: 10.1137/0328044.
7. Aubin, J.-P., Bayen, A. M., & Saint-Pierre, P. (2011). *Viability Theory: New Directions*. Springer.
8. Hadfield-Menell, D., Dragan, A. D., Abbeel, P., & Russell, S. (2017). *The Off-Switch Game*. IJCAI, 220–227. DOI: 10.24963/IJCAI.2017/32.
9. Pattanaik, P. K., & Xu, Y. (1990). *On Ranking Opportunity Sets in Terms of Freedom of Choice*. Recherches Économiques de Louvain / Louvain Economic Review, 56(3–4), 383–390.
10. Dow, K., & Werlang, S. R. C. (1992). *Uncertainty Aversion, Risk Aversion, and the Optimal Choice of Portfolio*. Econometrica, 60(1), 197–204. [僅作 uncertainty / choice-set 背景，不作 PPP 直接證據。]

---

# 非主張

本文不主張：

1. 選項越多自由越大；
2. 所有可達狀態都值得保存；
3. 所有危險可能性都應被保護；
4. 所有不可逆選擇都不倫理；
5. 自我約束與承諾都會減少自由；
6. 所有 exit 都必須永久存在；
7. viability 等於 autonomy；
8. empowerment 等於倫理自由；
9. capability approach 已完整解決 AI 主體治理；
10. Kreps flexibility 已完整描述欲願束；
11. Off-Switch Game 已解決人類／AI 主體權利；
12. correction channel 等於 ownership；
13. creator 永遠不應介入；
14. creator 永遠應等待主體自己解決所有問題；
15. 延遲永遠保存可能性；
16. 立即滿足永遠破壞自主；
17. 主體當下所有想要都應變成可達選項；
18. 主體對他者的侵害願望也應被 PPP 保護；
19. PPP 是由數學必然推出的倫理定理；
20. $\Omega_i^{AP}$ 已是完整可計算實作；
21. $\mathbf P_i$ 是普世自由尺度；
22. 本文已完成多主體公平性；
23. 本文已完成高能力 creator 的最終介入規則；
24. 本文已解決自由意志的形而上學問題；
25. 本文主張現實宇宙存在虛擬造物主。

---

**END OF WPCE-04 v0.1**
