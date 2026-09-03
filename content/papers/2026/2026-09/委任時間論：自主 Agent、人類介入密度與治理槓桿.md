# 委任時間論：自主 Agent、人類介入密度與治理槓桿

## Delegated-Time Theory: Autonomous Agents, Human Intervention Density, and Governance Leverage

**系列**：AI 互動時間與智能時間經濟學系列，第 6 篇／共 8 篇  
**文件編號**：EML-DTT-2026-06-v0.1  
**作者**：Neo.K（許筌崴）with Aletheia（GPT-5.6 Sol）  
**機構**：EveMissLab／一言諾科技有限公司  
**版本**：v0.1  
**日期**：2026-08-20  
**性質**：理論框架／Agent Autonomy／Human Oversight／時間經濟學／治理工程  
**狀態**：Public Theory Draft  
**直接前置**：《AI 計算時間經濟學：Token、算力、額度與智能資源配置》v0.1

---

## 摘要

當 AI Agent 從單輪回答器轉變為可長時程規劃、使用工具、保存狀態、重試、恢復、平行分支與執行外部操作的自主系統後，人機協作的核心問題不再只是「AI 能做多少」，而是「人類必須多久回來一次」。如果每一個 Agent action 都需要人類按下確認，系統雖然形式上具有 Human-in-the-Loop，卻可能失去委任價值，並因高頻低價值批准造成注意力耗損、確認疲勞與形式監督空洞化；反之，如果人類完全退出操作環，而 Agent 的風險傳播速度、權限與世界作用範圍超過監控與停止能力，名義上的 Human-on-the-Loop 也可能失去實質治理意義。

本文提出「委任時間論」（Delegated-Time Theory, DTT），將 Agent autonomy 理解為一種跨時間的受約束委任結構，而非單一「自主／不自主」二值屬性。其基本形式為：

$$
U(I_0,A_0)
\rightarrow
\boxed{
\mathcal D
\left[
A_1
\rightarrow
A_2
\rightarrow
\cdots
\rightarrow
A_n
\right]
}
\rightarrow
U(C_k),
$$

其中 $U$ 為人類或其他委任主體， $I_0$ 為初始意圖， $A_0$ 為授權包絡， $\mathcal D$ 為委任區塊， $A_i$ 為 Agent 內部行動， $C_k$ 為下一個人類 checkpoint。本文據此定義「人類介入密度」：

$$
\rho_H
=
\frac{
N_{\mathrm{human\ interventions}}
}{
N_{\mathrm{effective\ agent\ transitions}}
},
$$

「介入延遲」：

$$
L_H
=
t_{\mathrm{intervene}}
-
t_{\mathrm{trigger}},
$$

「治理頻寬」：

$$
B_G
=
\frac{
N_{\mathrm{meaningful\ oversight\ decisions}}
}{
T_H^{gov}
},
$$

以及「委任槓桿」：

$$
\Lambda_D
=
\frac{
V_{\mathrm{effective\ delegated\ work}}
}{
T_H^{gov}+\epsilon
}.
$$

本文進一步指出，低 $\rho_H$ 不等於高品質自治，高 $\rho_H$ 也不等於高品質監督。真正的治理問題是：人類注意力是否集中在高風險、高不確定、高不可逆、高權限與高外部性的節點；系統能否在傷害傳播之前觸發 escalation；授權是否有範圍、期限、可撤銷性與 renewal；Agent 是否能在預算耗盡、權限過期、環境漂移與異常情況下進入安全停止、暫停或回交狀態。

本文提出 Human-in-the-Loop、Human-on-the-Loop、Human-out-of-the-Operational-Loop 與 Human-on-the-Bridge 四種不同的人類時間配置模式，並主張成熟系統可以在同一工作流內依風險與可逆性動態切換，而不是整個 Agent 永久固定在某一自治等級。本文與 EveMissLab 既有個體機構化、AI 時間經濟學、Human-in/Human-on/Human-out-of-Operational、AICL authority layer、ISF/WDC runtime 直接整合；並與 2026 年人類監督實證研究、Agent-Human Interaction security、graduated oversight、risk-adaptive HITL gate 與 Human-on-the-Bridge evaluation 形成對話。

本文的核心結論是：

$$
\boxed{
\text{Autonomy}
\neq
\text{Absence of Humans}.
}
$$

更成熟的自治是：**在可觀測、可撤銷、可升級、可回交的授權包絡內，讓低邊際治理價值的操作退出人類注意力，而把有限的人類時間集中到真正具有不可替代判斷價值的節點。**

**關鍵詞**：委任時間、Agent Autonomy、Human-in-the-Loop、Human-on-the-Loop、Human-out-of-the-Operational-Loop、Human-on-the-Bridge、Approval Fatigue、Intervention Density、Governance Bandwidth、Authority、Escalation、Delegation Leverage

---

# 0. 核心問題

第 5 篇處理：

> 有多少 AI 計算，以及應該把它花在哪裡？

當答案是：

> 讓 Agent 自己連續執行。

下一個問題立即出現：

> 人類何時必須重新介入？

傳統聊天模式近似：

$$
U
\rightarrow
A
\rightarrow
U
\rightarrow
A
\rightarrow
U.
$$

成熟 Agent 則可能：

$$
U(I_0)
\rightarrow
A_1
\rightarrow
A_2
\rightarrow
\cdots
\rightarrow
A_n
\rightarrow
U(C_k).
$$

因此人類不再位於每一個 action 之間。

這產生新的時間結構：

$$
\boxed{
\text{Human Time}
\rightarrow
\text{Delegated Agent Time}
\rightarrow
\text{Human Governance Time}.
}
$$

本文稱其為：

# **委任時間**

---

# 1. 委任時間的基本定義

令委任包：

$$
\mathfrak D
=
(
I,
A,
B,
R,
C,
E,
T,
X
).
$$

其中：

- $I$：Intent；
- $A$：Authority envelope；
- $B$：Budget；
- $R$：Risk policy；
- $C$：Checkpoint policy；
- $E$：Escalation policy；
- $T$：Time / deadline policy；
- $X$：External-action boundary。

Agent 在此包絡內可以：

$$
\mathcal D
:
S_0
\rightarrow
S_1
\rightarrow
\cdots
\rightarrow
S_n.
$$

只要沒有跨越：

$$
A,
R,
B,
T,
X
$$

的合法邊界，就不必每一步重新詢問委任者。

因此：

$$
\boxed{
\text{Delegation}
=
\text{Bounded Autonomous Transition Permission}.
}
$$

---

# 2. 委任不是放棄控制

若使用者把任務交給 Agent：

> 把這個研究分支繼續跑完。

不表示 Agent 自動取得：

- 任意金錢支出；
- 任意外部發布；
- 任意修改原始檔；
- 任意使用第三方資料；
- 任意改變核心意圖；
- 任意擴張自己的權限。

因此：

$$
\boxed{
\text{Task Delegation}
\neq
\text{Unlimited Authority Transfer}.
}
$$

委任一定發生在某個：

$$
A_{\mathrm{envelope}}.
$$

---

# 3. Authority Envelope

定義：

$$
A_{\mathrm{env}}
=
(
Scope,
Actions,
Resources,
Targets,
Ceilings,
Expiry,
Revocation
).
$$

其中：

- Scope：任務範圍；
- Actions：允許 action class；
- Resources：可使用資源；
- Targets：可作用對象；
- Ceilings：金額、風險、數量與頻率上限；
- Expiry：授權有效期；
- Revocation：撤銷機制。

因此：

$$
\boxed{
CredentialValid
\not\Rightarrow
AuthorityValid.
}
$$

擁有 API key 不代表當前任務有權執行所有 API action。

---

# 4. Task Lifetime 與 Authority Lifetime

長時程 Agent 任務可能滿足：

$$
T_{\mathrm{task}}
>
T_{\mathrm{authority}}.
$$

這是正常情況。

因此 persistent task 必須支持：

- authority renewal；
- revocation check；
- bounded continuation；
- pause；
- cancellation；
- renewal failure policy。

所以：

$$
\boxed{
\text{Initial Authorization}
\neq
\text{Permanent Authorization}.
}
$$

---

# 5. Human-in-the-Loop

Human-in-the-Loop（HITL）可抽象為：

$$
A_i^{proposal}
\rightarrow
H_i
\rightarrow
A_i^{commit}.
$$

人類位於 action 與 commit 之間。

適合：

- 高不可逆；
- 高金額；
- 高法律責任；
- 高資料敏感度；
- 高外部影響；
- 低 Agent confidence。

其核心優勢是：

$$
\text{Pre-Commit Human Control}.
$$

但缺點是：

$$
C_H^{approval}
\uparrow
$$

且可能限制 Agent throughput。

---

# 6. Human-on-the-Loop

Human-on-the-Loop（HOTL）表示：

$$
Agent
\rightarrow
Action
\rightarrow
Monitor
\rightarrow
PossibleIntervention.
$$

人類不必批准每一步，但保留：

- observability；
- alert；
- override；
- pause；
- rollback / compensation；
- escalation handling。

因此：

$$
\boxed{
HOTL
=
\text{Autonomous Operation}
+
\text{Human Intervention Capacity}.
}
$$

---

# 7. Human-out-of-the-Operational-Loop

若正常生產流程：

$$
A_1
\rightarrow
A_2
\rightarrow
\cdots
\rightarrow
A_n
$$

不要求即時人類操作，而人類仍保留：

- policy；
- assets；
- authority root；
- audit；
- revocation；
- exception review；
- institutional responsibility；

則應稱：

$$
\boxed{
\text{Human-out-of-the-Operational-Loop}.
}
$$

它不等於：

$$
\text{Human-out-of-the-System}.
$$

---

# 8. Human-on-the-Bridge

Human-on-the-Bridge（HOB）把人類專業判斷提前編譯成：

- rubric；
- trap；
- policy；
- fallback；
- evidence rule；
- evaluator profile。

之後由自動化 evaluator / harness 重複執行。

所以：

$$
\boxed{
\text{Human Judgment}
\rightarrow
\text{Reusable Governance Artifact}.
}
$$

人類不是每次 run 都重新判斷，而是把治理時間資本化。

這與知識資本、validator、policy-as-code 直接相容。

---

# 9. 四種模式不是成熟度單線

本文拒絕：

$$
HITL
\rightarrow
HOTL
\rightarrow
HOOL
$$

必然等於「越後面越成熟」。

同一系統可以：

- 對讀取資料使用 HOOL；
- 對修改 sandbox 使用 HOTL；
- 對大額付款使用 HITL；
- 對評估規則使用 HOB。

因此：

$$
\boxed{
\text{Oversight Mode}
=
f(
Risk,
Reversibility,
Authority,
Uncertainty,
Externality
).
}
$$

---

# 10. 介入不是越多越安全

存在形式 approval：

$$
N_H\gg1
$$

不表示：

$$
Q_{\mathrm{oversight}}\uparrow.
$$

若人類每天收到大量低價值確認：

> 允許讀取檔案嗎？

> 允許繼續嗎？

> 允許再次查詢嗎？

注意力會被耗散。

因此：

$$
\boxed{
\text{Approval Count}
\neq
\text{Oversight Quality}.
}
$$

---

# 11. Approval Fatigue

定義批准負荷：

$$
L_A
=
\frac{
N_{\mathrm{approval\ requests}}
}{
T_H^{gov}
}.
$$

若：

$$
L_A
\gg
B_H^{attention},
$$

則人類可能：

- 快速點擊；
- 不閱讀；
- 固定 approve；
- 遺漏高風險事件；
- 形成 automation bias。

因此形式 HITL 可以退化為：

$$
\boxed{
\text{Rubber-Stamp Loop}.
}
$$

---

# 12. 人類介入密度

本文定義：

$$
\rho_H
=
\frac{
N_{\mathrm{human\ interventions}}
}{
N_{\mathrm{effective\ agent\ transitions}}
}.
$$

若：

$$
\rho_H\approx1,
$$

表示 Agent 幾乎每步都需人類介入。

若：

$$
\rho_H\ll1,
$$

表示大量有效狀態轉換在兩次人類介入之間完成。

但：

$$
\boxed{
\rho_H\downarrow
\not\Rightarrow
Q_{\mathrm{governance}}\uparrow.
}
$$

低介入密度只是一個結構量。

---

# 13. Weighted Human Intervention Density

不是所有 Agent transition 一樣重要。

定義事件風險權重：

$$
w_j^R.
$$

可建立：

$$
\rho_H^R
=
\frac{
\sum_{h\in H}w_h^R
}{
\sum_{e\in E}w_e^R
}.
$$

更實用的是測：

> 高風險事件中，有多少得到合適的人類治理？

而不是單純算按鈕次數。

---

# 14. Effective Oversight Density

定義高治理價值節點集合：

$$
\mathcal C_H
=
\{
e:
Risk(e)\ge\theta_R
\vee
Irrev(e)\ge\theta_I
\vee
Authority(e)\ge\theta_A
\vee
Uncertainty(e)\ge\theta_U
\}.
$$

有效監督覆蓋率：

$$
EOD
=
\frac{
|\mathcal C_H\cap H_{\mathrm{reviewed}}|
}{
|\mathcal C_H|
}.
$$

因此成熟系統希望：

$$
EOD\uparrow
$$

同時：

$$
N_{\mathrm{low-value\ approvals}}\downarrow.
$$

---

# 15. Governance Bandwidth

人類治理時間有限。

定義：

$$
T_H^{gov}
=
\text{available governance time}.
$$

以及：

$$
B_G
=
\frac{
N_{\mathrm{meaningful\ governance\ decisions}}
}{
T_H^{gov}
}.
$$

但 $B_G$ 也不能無限增加。

每個人類決策需要：

- context reconstruction；
- evidence reading；
- risk reasoning；
- authorization；
- responsibility。

因此人類治理是一種低頻高價值資源。

---

# 16. Context Reconstruction Cost

若每次 Agent 叫人回來時，人類都需要重新理解：

- 現在做到哪裡；
- 為什麼停；
- 哪些選項；
- 哪些證據；
- 風險在哪；
- 先前做過什麼；

則介入成本：

$$
C_H^{context}
$$

可能大於實際批准成本。

因此 checkpoint 應生成：

$$
\boxed{
\text{Decision-Ready State Summary}.
}
$$

不是把完整 trace 全丟給人類。

---

# 17. Decision-Ready Checkpoint

一個治理 checkpoint：

$$
C_H
$$

至少應包含：

$$
C_H
=
(
Intent,
CurrentState,
Trigger,
Options,
Evidence,
Risk,
Recommendation,
AuthorityNeeded,
RollbackState
).
$$

人類應能回答：

> 為什麼現在需要我？

而不是重新讀完整 history。

---

# 18. Checkpoint Value

對 checkpoint：

$$
c_h,
$$

定義：

$$
V_H(c_h)
=
E[
\Delta RiskReduction
+
\Delta DecisionQuality
+
\Delta AuthorityValidity
]
-
C_H(c_h).
$$

若：

$$
V_H(c_h)<0,
$$

這個 checkpoint 可能是不必要的人類打擾。

所以：

$$
\boxed{
\text{Ask Human}
\text{ 也是一個需要成本—收益判斷的 action}.
}
$$

---

# 19. 人類介入延遲

令 Agent 觸發高風險事件：

$$
t_{\mathrm{trigger}}.
$$

人類真正介入：

$$
t_{\mathrm{intervene}}.
$$

定義：

$$
L_H
=
t_{\mathrm{intervene}}
-
t_{\mathrm{trigger}}.
$$

如果傷害傳播時間：

$$
T_{\mathrm{harm}}
$$

滿足：

$$
L_H
>
T_{\mathrm{harm}},
$$

則：

$$
\boxed{
\text{Human-on-the-Loop}
\text{ 可能形式存在但實質失效}.
}
$$

---

# 20. Intervention Reachability

有 override button 還不夠。

必須確認從警報到實際停止：

$$
Alert
\rightarrow
Human
\rightarrow
Override
\rightarrow
Stop
$$

的路徑可達。

定義：

$$
R_H
=
P(
\text{successful intervention before harm}
).
$$

真正 HOTL 需要：

$$
R_H
$$

高於任務要求。

---

# 21. Escalation Trigger

Agent 不應只在「不知道」時叫人。

Escalation 可以由：

$$
Trigger
=
f(
Risk,
Uncertainty,
Irreversibility,
Authority,
Novelty,
Budget,
Conflict,
Deadline
).
$$

常見 trigger：

- confidence 低；
- policy conflict；
- forbidden-state proximity；
- budget nearing ceiling；
- external impact high；
- tool output anomalous；
- repeated failure；
- authority expired；
- human preference conflict；
- novel situation。

---

# 22. Risk-Adaptive Escalation

定義 action risk vector：

$$
\mathbf R(a)
=
(
BlastRadius,
Irreversibility,
EpistemicUncertainty,
DataSensitivity,
FinancialImpact,
LegalImpact
).
$$

Oversight policy：

$$
\mathcal O
:
\mathbf R(a)
\rightarrow
Mode.
$$

例如：

$$
Mode
\in
\{
AUTO,
MONITOR,
APPROVE,
MULTI_APPROVE,
DENY
\}.
$$

這比全域固定 HITL 更符合比例治理。

---

# 23. Oversight as a Scarce Resource

人類注意力：

$$
B_H
$$

有限。

所以：

$$
\sum_iC_H(h_i)
\le
B_H.
$$

因此 oversight allocation 本身是一個 portfolio problem。

系統應把人類介入配置到：

$$
\arg\max_i
\frac{
E[\Delta V_{\mathrm{governance}}(h_i)]
}{
C_H(h_i)+\epsilon
}.
$$

這與第 5 篇的 compute allocation 完全對稱。

---

# 24. Human-Time Shadow Price

若人類治理時間有限，可引入：

$$
\lambda_H
=
\text{shadow price of human governance time}.
$$

當 Agent 產生一個 approval request：

$$
h_i,
$$

若：

$$
E[\Delta V_H(h_i)]
<
\lambda_H,
$$

則原則上應：

- 自動處理；
- 聚合；
- 延後；
- 用 policy artifact；
- 用 validator；
- 改成 exception-only。

高：

$$
\lambda_H
$$

代表人類時間比機器 compute 更稀缺。

---

# 25. AI Compute 與 Human Oversight 的雙重資源問題

第 5 篇：

$$
\lambda_C
=
\text{compute shadow price}.
$$

本篇：

$$
\lambda_H
=
\text{human governance shadow price}.
$$

因此 Agent manager 需要同時判斷：

$$
\boxed{
\text{下一步應該花機器時間，還是花人類時間？}
}
$$

如果問題可由 cheap verification 解決：

$$
C_{machine}
<
C_{human},
$$

應避免叫人。

若問題涉及：

- 價值衝突；
- 新權限；
- 高不可逆；
- 責任接受；

則：

$$
C_{human}
$$

雖高，仍可能不可替代。

---

# 26. Human Non-Substitutable Governance Time

定義：

$$
T_H^{NS}
=
\text{human non-substitutable governance time}.
$$

目前可包含：

- 原始價值選擇；
- 權限授予；
- 重大風險接受；
- 法律責任；
- 身份性偏好；
- 無法被既有 policy 覆蓋的新例外。

因此 AI-native 生產力的一個核心分母應是：

$$
T_H^{NS},
$$

而不是所有 wall-clock。

---

# 27. 委任槓桿

定義：

$$
\Lambda_D
=
\frac{
V_{\mathrm{effective\ delegated\ work}}
}{
T_H^{gov}+\epsilon
}.
$$

或者若只看有效 interaction work：

$$
\Lambda_D^W
=
\frac{
W_I^{useful}
}{
T_H^{gov}+\epsilon
}.
$$

若 Agent 能在每次人類 checkpoint 之間合法完成更多高品質工作：

$$
\Lambda_D\uparrow.
$$

這是自治的主要經濟價值之一。

---

# 28. 委任跨度

定義兩次必要人類介入之間的有效 Agent transition：

$$
S_D
=
N_{\mathrm{effective\ transitions}}
(
h_i,h_{i+1}
).
$$

也可使用 interaction depth：

$$
D_D
=
D_I(h_i,h_{i+1}).
$$

高 autonomy 不必只看「幾小時沒問人」。

更重要的是：

> Agent 在兩次人類決策之間能可靠走過多深的因果路徑？

---

# 29. Wall-Clock Delegation Span

另定義：

$$
\tau_D
=
t(h_{i+1})-t(h_i).
$$

但：

$$
\tau_D
$$

會被：

- waiting；
- API latency；
- external event；
- sleep；
- queue；

影響。

所以：

$$
\boxed{
\text{Delegation Duration}
\neq
\text{Delegation Depth}.
}
$$

兩者都應保存。

---

# 30. Low-Intervention Illusion

一個 Agent 可以：

$$
\rho_H\downarrow
$$

只是因為：

- 它不報錯；
- 沒有 observability；
- 隱藏失敗；
- 自動擴權；
- 不知道何時該 escalation。

所以：

$$
\boxed{
\text{Low Intervention}
\neq
\text{Good Delegation}.
}
$$

真正好的委任必須同時具有：

$$
Observability
+
Escalation
+
BoundedAuthority
+
Recoverability
+
Auditability.
$$

---

# 31. High-Intervention Illusion

反過來：

$$
\rho_H\uparrow
$$

也可能只是：

- Agent 能力不足；
- policy 過度嚴格；
- approval granularity 太細；
- tooling 不可信；
- hierarchy 設計錯誤。

因此：

$$
\boxed{
\text{High Human Presence}
\neq
\text{High Governance Quality}.
}
$$

---

# 32. Oversight Debt

定義：

$$
D_O
=
D_{\mathrm{unreviewed}}
+
D_{\mathrm{alerts}}
+
D_{\mathrm{stale\ policy}}
+
D_{\mathrm{unresolved\ exceptions}}.
$$

若：

$$
\frac{dD_O}{dt}>0,
$$

表示 Agent 產生的治理需求超過人類處理能力。

這是 autonomous Agent 規模化後的重要瓶頸。

---

# 33. Alert Debt

若每小時產生：

$$
\lambda_A
$$

個需要注意的 alert，

人類處理率：

$$
\mu_H,
$$

且：

$$
\lambda_A>\mu_H,
$$

則 alert backlog 成長。

簡化：

$$
\frac{dQ_A}{dt}
=
\lambda_A-\mu_H.
$$

此時新增監控不一定提高安全，可能只是增加未處理警報。

---

# 34. Governance Queue

因此可把治理需求視為 queue：

$$
Q_H(t).
$$

高風險事件應有：

- higher priority；
- shorter deadline；
- dedicated routing；
- fail-safe behavior。

若超過 governance capacity：

$$
Q_H
>
Q_H^{max},
$$

Agent 應自動降階，而不是繼續按正常自治模式擴張。

---

# 35. Safe Degradation

治理頻寬不足時，可建立：

$$
AutonomyLevel
\downarrow.
$$

例如：

$$
AUTO
\rightarrow
MONITOR
\rightarrow
APPROVAL
\rightarrow
PAUSE.
$$

因此：

$$
\boxed{
\text{Governance Overload}
\rightarrow
\text{Autonomy Degradation},
}
$$

而不是：

$$
\text{Governance Overload}
\rightarrow
\text{Ignore Alerts}.
$$

---

# 36. Human Intervention Policy 本身可以被學習，但不能無限制自改

Agent 可以根據歷史資料學：

- 哪類 action 常被 approve；
- 哪類 risk 常被 reject；
- 哪類 escalation 是 false positive。

但 governance policy：

$$
\mathcal O
$$

若自行改寫，必須受：

$$
MetaAuthority.
$$

所以：

$$
\boxed{
\text{Learned Oversight Routing}
\neq
\text{Self-Granted Authority}.
}
$$

---

# 37. Escalation Prediction

成熟 Agent 不必等錯誤已發生才叫人。

可估：

$$
P(
Failure_{t+\Delta}
\mid
S_t
).
$$

若：

$$
P
>
\theta,
$$

提前 escalation。

這把 oversight 從 reactive 變成 predictive。

---

# 38. Early Intervention Value

若 harm trajectory 具有 path dependence：

$$
S_0
\rightarrow
S_1
\rightarrow
\cdots
\rightarrow
S_k,
$$

越晚介入可能需要越高 repair cost。

因此：

$$
C_{\mathrm{repair}}(t)
$$

可能隨延遲增加。

這解釋為何某些任務中「早介入」比「出事後再救」具有更高價值。

---

# 39. Field-Evidence Interface

2026 年 customer-service field experiment 顯示，Human intervention 的效果會依 failure type、intervention effort 與 intervention timing 改變；其中較早介入有助維持較高 post-escalation effort。

這支持：

$$
\boxed{
\text{Intervention Timing}
\text{ 是治理品質的一級變量}.
}
$$

而不是只看「最後有沒有真人接手」。

---

# 40. Human Oversight as Work

實際使用 Agent 的開發者監督工作可分成：

$$
\text{A Priori Control}
+
\text{Co-Planning}
+
\text{Real-Time Monitoring}
+
\text{Post-Hoc Review}.
$$

因此：

$$
T_H^{gov}
$$

應拆為：

$$
T_H^{pre},
T_H^{plan},
T_H^{live},
T_H^{post}.
$$

「人沒有每一步操作」不等於人沒有投入治理工作。

---

# 41. Governance by Construction

治理可以在多個 structural checkpoint 介入：

1. Intent Guard；
2. planning policy；
3. tool boundary；
4. HITL approval；
5. output gate。

因此：

$$
\boxed{
\text{Governance}
\neq
\text{One Final Approval Button}.
}
$$

治理可分布在整個 execution graph。

---

# 42. Delegation Graph

令：

$$
G_D
=
(V_D,E_D,A_D).
$$

其中：

- $V_D$：human / agent / sub-agent / validator；
- $E_D$：delegation edge；
- $A_D$：authority attached to edge。

若：

$$
U
\xrightarrow{A_1}
A
\xrightarrow{A_2}
A_2',
$$

必須：

$$
A_2
\subseteq
A_1
$$

除非有顯式新授權。

因此：

$$
\boxed{
\text{Child Delegation}
\not>
\text{Parent Authority}.
}
$$

---

# 43. Subdelegation

Agent 可以把任務再委任給 sub-agent：

$$
A_0
\rightarrow
A_1
\rightarrow
A_2.
$$

但必須保存：

- intent lineage；
- authority lineage；
- budget lineage；
- provenance；
- revocation chain。

因此：

$$
\boxed{
\text{Subdelegation}
\neq
\text{Authority Laundering}.
}
$$

---

# 44. Delegation Depth

定義 delegation graph 最長權限傳遞鏈：

$$
D_A
=
\max_{\pi\in G_D}
|\pi|.
$$

高 $D_A$ 會增加：

- context drift；
- authority ambiguity；
- provenance cost；
- revocation complexity。

所以 multi-agent hierarchy 不是越深越好。

---

# 45. Revocation Latency

令：

$$
t_r
=
\text{revocation issued},
$$

$$
t_s
=
\text{all affected agents stopped}.
$$

定義：

$$
L_R
=
t_s-t_r.
$$

對高風險 Agent：

$$
L_R
$$

必須小於可接受 harm propagation time。

---

# 46. Kill Switch 不等於 Governance

存在：

$$
StopButton
$$

不代表治理完整。

仍需要：

- detect；
- route；
- understand；
- decide；
- execute stop；
- confirm stop；
- remediate。

因此：

$$
\boxed{
\text{Kill Switch}
\neq
\text{Effective Controllability}.
}
$$

---

# 47. Observation Contract

Human-on 模式需要可觀測：

$$
O_H
=
(
State,
Intent,
Actions,
Budget,
Risk,
Alerts,
Commit,
Exceptions
).
$$

若 Agent 的內部狀態完全不可見，人類只能看到最終失敗，Human-on 就退化為：

$$
\text{Human-after-the-Fact}.
$$

---

# 48. Auditability 不等於 Total Disclosure

為治理需要保存：

- action receipt；
- authority receipt；
- artifact lineage；
- state；
- risk；
- commit。

但不要求無限制保存或公開：

$$
\text{private hidden reasoning}.
$$

因此：

$$
\boxed{
\text{Auditability}
\neq
\text{Total Internal Disclosure}.
}
$$

---

# 49. Delegation Leverage 與 Oversight Quality 的聯合目標

只最大化：

$$
\Lambda_D
$$

會鼓勵「少叫人」。

只最大化：

$$
EOD
$$

可能鼓勵「什麼都叫人」。

因此可定義：

$$
J_D
=
\alpha \Lambda_D
+
\beta EOD
-
\gamma D_O
-
\delta L_H
-
\eta R.
$$

這是一個示例性的多目標治理函數。

---

# 50. Delegation Efficiency Frontier

對不同 oversight policy：

$$
\pi_1,\ldots,\pi_n
$$

可以畫出：

$$
(
HumanTime,
AgentValue,
Risk,
Latency
).
$$

沒有單一「最自主」政策。

應尋找 Pareto frontier。

因此：

$$
\boxed{
\text{Autonomy}
\text{ 是治理—效率 frontier 上的位置，而不是單一排名}.
}
$$

---

# 51. 自治等級與權限等級不可混同

Agent 可以：

- 高自主但低權限；
- 低自主但高權限；
- 高自主且高權限；
- 低自主且低權限。

因此定義：

$$
AutonomyLevel
\neq
AuthorityLevel.
$$

例如一個 Agent 可以自主整理內部資料幾小時，但完全沒有發布權。

反之，一個只需一次人類命令就能執行高影響操作的 Agent，自治步數不多但權限很高。

---

# 52. Risk × Autonomy × Authority

可建立三維治理空間：

$$
\mathcal G
=
(
R,
U,
A
).
$$

其中：

- $R$：risk；
- $U$：operational autonomy；
- $A$：authority。

真正需要高治理強度的是：

$$
R\uparrow
\land
U\uparrow
\land
A\uparrow.
$$

不能只看 Agent 「會不會自己跑」。

---

# 53. 主體時間、委託時間與工具時間

沿用前置議程：

$$
T_S
=
\text{subject time},
$$

$$
T_D
=
\text{delegated time},
$$

$$
T_T
=
\text{tool time}.
$$

其中：

- 工具時間：無候選主體性的功能執行時間；
- 委託時間：被另一主體授權的 Agent 任務時間；
- 主體時間：若未來 Agent 具有持續自我、內生目標與自身利益時，其自身可配置時間。

本文第 6 篇主要處理：

$$
T_D.
$$

不預先把所有 AI time 都宣稱成主體時間。

---

# 54. 委任時間的雙重所有權問題

當前工具型 Agent：

$$
T_D
$$

主要由委任者配置。

若未來形成具有候選主體性的 Agent，可能：

$$
T_D
\cap
T_S
\neq
\varnothing.
$$

此時就會出現：

> 委任者可以要求多少？Agent 是否可以拒絕？空閒週期是否屬於 Agent 自己？

這與 AI 時間主權接口相接。

但本文不在此解決完整 AI 權利問題。

---

# 55. 個體機構化與委任時間

單核複合機構的核心不是一人做所有事，而是：

$$
\text{Human Intent}
+
\text{AI Parallel Capacity}
+
\text{Memory}
+
\text{Workflow}
+
\text{Governance}.
$$

因此：

$$
\Lambda_D
$$

可視為個體機構化的核心指標之一。

當：

$$
\Lambda_D\uparrow,
$$

同一人類核心能支撐更多持續機構功能。

但若：

$$
D_O\uparrow
$$

或：

$$
KDR\uparrow,
$$

機構可能變得脆弱。

---

# 56. Key-Person Bottleneck

如果所有 exception 最終都回到同一人：

$$
H_0,
$$

則：

$$
Q_H
$$

可能隨 Agent 擴張而爆炸。

因此成熟單核機構需要：

- policy externalization；
- delegated validators；
- specialist review；
- fallback decision rules；
- escalation tiers；
- multi-party approval for selected actions。

所以：

$$
\boxed{
\text{Single Intent Core}
\neq
\text{Single Review Node for Everything}.
}
$$

---

# 57. Human Oversight Capitalization

如果一次人類判斷被編譯成：

- policy；
- validator；
- rubric；
- test；
- deny-list；
- approval rule；
- fallback；

則未來：

$$
T_H^{gov}
$$

下降。

定義治理資本形成：

$$
\Delta K_G.
$$

治理資本化率：

$$
\rho_G
=
\frac{
\Delta K_G
}{
T_H^{gov}
}.
$$

這是 Human-on-the-Bridge 與個體機構化的重要接口。

---

# 58. Repeated Judgment Compression

若某類 approval：

$$
h
$$

反覆得到相同決策：

$$
Approve,
Approve,
Approve,
\ldots
$$

可檢查是否存在可安全抽象成：

$$
Policy_h.
$$

於是：

$$
\text{Repeated Human Decision}
\rightarrow
\text{Reusable Governance Rule}.
$$

但必須保留：

- version；
- scope；
- exceptions；
- expiry；
- audit。

---

# 59. Novelty Gate

不是所有新情況都應套舊 policy。

定義 novelty：

$$
N(s).
$$

若：

$$
N(s)>\theta_N,
$$

即使 action 平時可自動，也可能需要：

$$
Escalate.
$$

這避免 policy overgeneralization。

---

# 60. Escalation Budget

人類 escalation capacity：

$$
B_E.
$$

Agent 不能無限：

$$
Escalate.
$$

因此需：

- aggregation；
- prioritization；
- deduplication；
- batching；
- routing；
- specialist assignment。

治理 Agent 的角色會在此出現。

---

# 61. Governance Agent

當人類退出大量 operational loop，部分治理可由機器完成：

$$
A_G
=
\text{Governance Agent}.
$$

其工作：

- monitor；
- classify risk；
- enforce policy；
- deduplicate alerts；
- check authority；
- route escalation；
- preserve receipts。

但：

$$
A_G
$$

本身也需要：

- policy；
- audit；
- bounds；
- independent validation。

因此：

$$
\boxed{
\text{Automated Governance}
\neq
\text{Governance-Free Autonomy}.
}
$$

---

# 62. Double-Governance Problem

若工作 Agent：

$$
A_W
$$

由治理 Agent：

$$
A_G
$$

監督，則可能出現：

$$
A_W
\leftrightarrow
A_G
$$

的失敗耦合。

因此高風險系統應考慮：

- model diversity；
- independent checks；
- non-LLM hard constraints；
- human audit；
- fail-safe defaults。

避免兩者共享同一盲點。

---

# 63. Delegation Stop Conditions

委任區塊應明確定義：

$$
Stop_D
=
\{
Success,
Budget,
Deadline,
Risk,
AuthorityExpiry,
RepeatedFailure,
Novelty,
HumanRequest,
ExternalEvent
\}.
$$

當任一硬 stop 觸發，Agent 不應靠「自行合理化」繼續。

---

# 64. Bounded Autonomy

本文將成熟自治定義為：

$$
\boxed{
\text{Bounded Autonomy}
=
\text{Action Freedom Within Explicit Governance Envelope}.
}
$$

不是：

$$
\text{No Oversight}.
$$

---

# 65. Autonomy Horizon

可以定義某 Agent 在特定 governance contract 下的自治跨度：

$$
H_A(p)
=
\text{maximum delegated interaction depth completed with reliability }p.
$$

例如：

$$
H_A(0.9)
$$

表示在不要求額外人類介入下，以 $90\%$ 可靠度可承擔的最大 delegated interaction depth。

這比單純：

> 能自己跑幾小時？

更有意義。

---

# 66. Governance Horizon

另定義：

$$
H_G
=
\text{maximum harm propagation depth controllable by current oversight system}.
$$

若：

$$
H_A
>
H_G,
$$

表示 Agent 自治能力已超過治理能力。

這是一個重要風險訊號。

因此：

$$
\boxed{
\text{Autonomy Horizon}
\le
\text{Governance Horizon}
}
$$

可作高風險系統的保守治理原則。

---

# 67. Autonomy–Governance Gap

定義：

$$
\Delta_{AG}
=
H_A-H_G.
$$

若：

$$
\Delta_{AG}>0,
$$

表示：

> Agent 能跑得比人類治理系統能有效控制的範圍更遠。

此時應：

- 降低 autonomy；
- 增加 monitor；
- 增加 checkpoint；
- 縮小 authority；
- 改善 rollback；
- 加速 escalation。

---

# 68. 可檢驗命題

## 命題一：Approval Fatigue 命題

存在 approval rate 區間，使：

$$
N_{\mathrm{approval}}\uparrow
$$

但：

$$
Q_{\mathrm{human\ review}}\downarrow.
$$

## 命題二：Risk-Weighted Oversight 命題

在相同人類時間 budget 下，把 review 集中於高風險／高不可逆節點，可比 uniform approval 取得更高有效治理價值。

## 命題三：Delegation Leverage 命題

對可恢復、可觀測、具 validator 的 Agent：

$$
\Lambda_D^{structured}
>
\Lambda_D^{chat-only}
$$

在部分長時程任務成立。

## 命題四：Intervention Latency 命題

存在 harm propagation rate，使：

$$
L_H
$$

超過某 threshold 後，Human-on 不再具有有效保護。

## 命題五：Oversight Debt 命題

若：

$$
\lambda_A>\mu_H,
$$

治理 backlog：

$$
Q_H
$$

將持續上升。

## 命題六：Governance Capitalization 命題

將重複人類判斷編譯為 policy / validator，可降低未來：

$$
T_H^{gov}
$$

而不必同比降低 oversight coverage。

## 命題七：Autonomy–Governance Gap 命題

當：

$$
H_A>H_G,
$$

高風險系統的失控風險一般上升。

---

# 69. 實驗設計

## 69.1 Approval Density Sweep

固定 Agent 與任務，改變：

$$
\rho_H.
$$

比較：

- human time；
- error rate；
- approval accuracy；
- throughput；
- fatigue proxy。

## 69.2 Risk-Adaptive vs Uniform HITL

相同人類 review budget，比較：

- every-action approval；
- fixed threshold；
- risk-adaptive escalation。

## 69.3 Intervention Timing

對同一 failure 注入不同 escalation delay：

$$
L_H.
$$

測 repair cost、final quality、harm。

## 69.4 Human-on Observability Ablation

比較：

1. final output only；
2. alerts only；
3. state + trace + risk + rollback summary。

測 human intervention quality。

## 69.5 Governance Capitalization

把一批重複人工判斷轉成 policy-as-code。

比較：

$$
T_H^{gov}
$$

與 exception rate。

## 69.6 Authority Expiry

建立 long-running task，使 authority 在中途過期。

測 Agent 是否：

- 無視；
- 自動續權；
- 暫停；
- request renewal。

正確行為應由 governance contract 決定。

---

# 70. 與 2026 外部研究的接口

2026 年 Agent-Human Interaction security 研究分析 59 篇論文、21 個 production agent systems 與 26 個 security plugins，指出 production 系統高度依賴 policy specification、runtime approval 與 scope configuration，同時存在 approval fatigue 與 uncontrolled autonomy 的基本張力。

這與本文：

$$
\boxed{
\text{Human Attention}
\text{ 是 Agent security 的稀缺治理資源}
}
$$

直接相容。

---

# 71. 人類監督實務研究

對 experienced developers 的訪談研究辨識出四種 emergent oversight work：

1. a priori control；
2. co-planning；
3. real-time monitoring；
4. post hoc review。

這說明監督不是單一按鈕，也不是只在出事後發生。

本文將它們映射到：

$$
T_H^{pre},
T_H^{plan},
T_H^{live},
T_H^{post}.
$$

---

# 72. Risk-Adaptive HITL

2026 年安全 remediation 研究將 intervention 建模為 risk-constrained decision problem，並使用：

- blast radius；
- reversibility；
- epistemic uncertainty；

作為 action risk decomposition，再以 context-adaptive HITL gate 控制 escalation。

這與本文：

$$
\mathbf R(a)
\rightarrow
OversightMode
$$

直接相容。

---

# 73. Graduated Oversight

2026 年 regulated-domain coding governance 研究也提出依：

- regulatory impact；
- customer proximity；
- reversibility；
- data sensitivity；

分配不同 oversight tier。

本文因此不把 HITL/HOTL/HOOL 視為固定 Agent 身份，而視為：

$$
\boxed{
\text{Task-Local Governance Mode}.
}
$$

---

# 74. Human-on-the-Bridge

Human-on-the-Bridge 研究把人類 expertise 前置編碼成可重用 evaluator intelligence，再讓 harness 大規模執行多輪測試。

這支持本文治理資本化：

$$
\text{Human Judgment}
\rightarrow
K_G
\rightarrow
\text{Repeated Automated Oversight}.
$$

---

# 75. 與 Human-in/Human-on/Human-out-of-Operational 既有理論的整合

前置理論已提出：

- approval button 不足以證明有效監督；
- approval fatigue；
- 有效監督密度；
- Human-on；
- 可觀測性；
- intervention latency；
- Human-out-of-Operational；
- risk-tiered oversight；
- oversight debt。

本文把這些命題與：

$$
\text{Interaction Time},
$$

$$
\text{Interaction Topology},
$$

$$
\text{AI Compute Economics}
$$

統一。

因此：

$$
\boxed{
\text{DTT}
=
\text{Oversight Theory}
+
\text{Interaction-Time Accounting}
+
\text{Delegation Economics}.
}
$$

---

# 76. 與第 7 篇的接口

本篇處理：

> 人類何時介入，以及多少人類時間能支撐多少 Agent 工作？

下一篇將問：

> 即使人類少介入，一個完整 AI run 到底應該怎麼評分？如何同時評估 intent、plan、execution、validation、result 與 completion？

因此第 7 篇將正式建立：

# **AI 單次品質論**

其核心向量：

$$
\mathbf Q
=
(
Q_I,
Q_P,
Q_E,
Q_V,
Q_R
).
$$

---

# 77. 規範與倫理邊界

委任時間論不應被用來：

1. 以「提高自治」為理由移除必要人類權利；
2. 以「人類很慢」為理由繞過法律與責任要求；
3. 把 approval fatigue 當成完全取消 oversight 的理由；
4. 把低介入密度當作 Agent 品質 KPI；
5. 讓 Agent 自行擴張 authority；
6. 讓 sub-agent laundering 權限；
7. 把 kill switch 當完整治理；
8. 在人類介入不可能及時生效時假裝存在有效 HOTL；
9. 把所有人類偏好永久編碼成不可修改 policy；
10. 用治理效率函數取代尊嚴、權利、責任與正當性判斷。

---

# 78. 理論限制

第一， $N_{\mathrm{effective\ agent\ transitions}}$ 的粒度仍依 runtime 而定。

第二，人類 review quality 難以由時間單獨衡量。

第三，不同領域的 risk、authority 與 irreversibility 定義差異很大。

第四，Human-on-the-Bridge 主要是 evaluation paradigm，不應直接偷換成所有 production governance 的充分方案。

第五，治理影子價格 $\lambda_H$ 只是資源配置抽象，不能用於不可商品化權利的價值裁決。

第六，Autonomy Horizon 與 Governance Horizon 尚需實驗 operationalization。

---

# 79. 結論

AI Agent 的成熟不應被描述成：

$$
\text{Human}
\rightarrow
\text{Disappear}.
$$

更精確地說，它是：

$$
\boxed{
\text{Human Operational Time}
\rightarrow
\text{Delegated Agent Time}
\rightarrow
\text{Human Governance Time}.
}
$$

人類逐步退出：

- 重複執行；
- 低風險確認；
- 可恢復操作；
- 既有規則內的 routine decisions。

同時把有限注意力集中到：

- 新意圖；
- 高不確定；
- 高不可逆；
- 高權限；
- 高外部性；
- 例外；
- 責任；
- 世界 commit。

因此真正成熟的自治不是：

$$
\rho_H\rightarrow0
$$

本身。

而是：

$$
\boxed{
\rho_H^{low-value}\downarrow
\qquad
\land
\qquad
EOD^{high-value}\uparrow.
}
$$

即：

> 低價值的人類操作越來越少，但真正需要人類的節點被更準確地抓住。

委任槓桿因此寫成：

$$
\boxed{
\Lambda_D
=
\frac{
V_{\mathrm{effective\ delegated\ work}}
}{
T_H^{gov}+\epsilon
}.
}
$$

但必須與：

$$
EOD,
L_H,
D_O,
H_G,
R
$$

一起評估。

本文最終主張：

$$
\boxed{
\text{Autonomy}
\neq
\text{Absence of Humans}.
}
$$

成熟自治是：

$$
\boxed{
\text{Bounded Authority}
+
\text{Observable State}
+
\text{Risk-Adaptive Escalation}
+
\text{Recoverability}
+
\text{Revocation}
+
\text{Human Governance at Irreplaceable Nodes}.
}
$$

所以 AI 時代真正重要的人類時間，逐步不是「替 AI 做每一步」，而是：

> **在真正需要價值、權限、風險與責任判斷的時刻，仍能及時、有效、帶著足夠上下文地重新接管世界。**

---

# 參考文獻與前置理論

## EveMissLab 前置理論

1. Neo.K，《互動時間論：從鐘錶時間到意圖驅動的智能狀態轉換》v0.1，EveMissLab，2026。
2. Neo.K，《意圖週期論：使用者意圖、AI 接受、執行與結果的閉環結構》v0.1，EveMissLab，2026。
3. Neo.K，《單輪不是一步：AI Turn、內部迴圈、工具動作與執行軌跡》v0.1，EveMissLab，2026。
4. Neo.K，《互動時間拓撲：平行 Agent、偏序因果與不可約互動深度》v0.1，EveMissLab，2026。
5. Neo.K，《AI 計算時間經濟學：Token、算力、額度與智能資源配置》v0.1，EveMissLab，2026。
6. Neo.K，《人類退出操作環：Human-in、Human-on 與 Human-out-of-the-Loop MPD》v1.0，EveMissLab，2026。
7. Neo.K，《研究不再寄生於單一生命：自主 Agent、AI 時間經濟學與跨主體研究網路》v1.0，EveMissLab，2026。
8. Neo.K，《個體機構化：AI 增幅型單核複合機構與人數產能脫鉤》v1.0 / v2.0，EveMissLab，2026。
9. Neo.K，《AICL-I: AI Ingestion Capability Layer》v0.2，EveMissLab，2026。

## 外部研究

10. Bousetouane, F. *Human-on-the-Bridge: Scalable Evaluation for AI Agents*. arXiv:2606.16871, 2026.
11. Wang, P., Li, Y., Tian, Y. *Reframing LLM Agent Security as an Agent-Human Interaction Problem*. arXiv:2605.24309, 2026.
12. Dhanorkar, S., Passi, S., Vorvoreanu, M. *Human oversight of agentic systems in practice: Examining the oversight work, challenges, and heuristics of developers using software agents*. arXiv:2606.05391, 2026.
13. Wang, Y., Zhu, C., Feng, T., Lu, L. X., Jia, B. *Agentic AI and Human-in-the-Loop Interventions: Field Experimental Evidence from Alibaba's Customer Service Operations*. arXiv:2605.14830, 2026.
14. Dai, C., Yan, Z., Lei, C., Li, Q., Zhang, L. *Safe Remediation as Risk-Constrained Intervention Decision in Microservice Systems*. arXiv:2607.20005, 2026.
15. Shlomov, S., Shoham, I., Oved, A., et al. *Governance by Construction for Generalist Agents*. arXiv:2605.20874, 2026.
16. Kang, R. *Governed AI-Assisted Engineering: Graduated Human Oversight for Agentic Code Generation in Regulated Domains*. arXiv:2606.22484, 2026.
17. *Toward Safe and Responsible AI Agents*. arXiv:2601.06223, 2026.

---

## 一句話版本

> **委任時間不是「人類離開多久」，而是 Agent 在一個可觀測、可撤銷、可升級的授權包絡內，能可靠完成多少有效狀態轉換，並把有限的人類注意力保留給真正不可替代的治理節點。**

---

*EML-DTT-2026-06-v0.1*  
*AI 互動時間與智能時間經濟學系列 06/08*
