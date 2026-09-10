# AIDA-05｜身份—責任橋
## 從可歸因 Agent 到 Operational Responsibility Capacity

**English Title:** The Identity–Responsibility Bridge: From Attributable Agents to Operational Responsibility Capacity  
**系列：** AI Agent Identity, Delegation, and Accountability Infrastructure Series  
**系列縮寫：** AIDA  
**編號：** AIDA-05  
**版本：** v0.1  
**日期：** 2026-09-08  
**狀態：** Research Draft / Canonical UTF-8 Markdown Source  
**作者：** Neo.K  
**協作整理：** GPT-5.6 Sol  

---

## 摘要

AIDA-01 至 AIDA-04 已依序建立 Agent 性、provenance、Human–Agent Principal Separation 與 bounded delegation。當一個 AI Agent 已經具有可驗證身份、可追蹤委派、明確 Authority Envelope，並在被允許的選擇空間內作出造成現實效果的決策時，下一個問題不再只是「誰做了這件事」，而是：

> 什麼時候可以說這個 Agent 開始具備某種可承責條件？

本文提出 **Identity–Responsibility Bridge（身份—責任橋）** 與 **Operational Responsibility Capacity（操作性承責能力）**。本文刻意區分：

$$
\boxed{
\text{Attribution}
\neq
\text{Responsibility Capacity}
\neq
\text{Moral Blame}
\neq
\text{Legal Liability}.
}
$$

可歸因只表示某個 action 可以被連結到某個 actor；操作性承責能力則進一步要求該 actor 對自身身份、權限、可選行動、資訊條件、後果、承諾與修正具有足夠的可操作結構；道德譴責與法律責任則需要額外的規範、制度與法域判定。

本文將 Agent $A$ 在時間 $t$ 、責任域 $\Gamma$ 下的操作性承責狀態表示為：

$$
\boldsymbol{\rho}_{\Gamma}(A,t)
=
(
I,
U,
C,
K,
F,
Q,
R,
V,
T
),
$$

其中：

- $I$：Identity / Attribution，身份與行為可歸因性；
- $U$：Authority Understanding，對自身權限與限制的可操作辨識；
- $C$：Control，對 action selection 的實際控制程度；
- $K$：Epistemic Access，對任務、環境與規範相關資訊的可取得與理解能力；
- $F$：Counterfactual Freedom，可選替代方案與拒絕／延後／升級的能力；
- $Q$：Consequence Sensitivity，對可預見後果與風險的敏感度；
- $R$：Reflexive Evaluation，對自身 proposal、理由與錯誤進行反身檢查的能力；
- $V$：Revision Capacity，能否讓錯誤、異議或新證據真正改變後續 policy；
- $T$：Traceable Persistence，決策、承諾、修正與後果能否跨時間被寫回並追蹤。

本文拒絕把這些維度粗暴壓成單一人格分數。相反，本文提出一組 **Responsibility Gates**。若身份不可歸因、權限完全未知、沒有實際選擇空間、完全無法理解後果，或自我反思不能改變後續行為，則即使系統會產生「我負責」的語句，也不應被視為具備高操作性承責能力。

本文同時區分五種責任：

$$
\boxed{
\text{Causal Responsibility},
\text{Operational Responsibility},
\text{Role Responsibility},
\text{Moral Responsibility},
\text{Legal Liability}.
}
$$

一個 Agent 可以在因果上造成結果，卻沒有足夠承責能力；可以具有明確 role responsibility，卻尚未具有法律人格；也可以具備部分操作性承責能力，而最終法律賠償責任仍主要落在 provider、deployer、operator 或組織。

截至 2026 年，OECD AI Principles 的 accountability 仍要求 AI actors 依其角色、脈絡與可行動能力負責，並要求 traceability；NIST AI RMF 強調組織角色、責任、human-AI configuration、oversight 與 escalation；EU AI Act 目前仍主要把法定義務配置給 provider、deployer 等自然人、法人或其他組織行動者，而沒有建立 AI system 本身的獨立法律責任人格。本文因此不把 Operational Responsibility Capacity 假稱為現行法律責任制度，而把它視為未來 Agent responsibility architecture 所缺少的中間層。

本文最核心的命題是：

$$
\boxed{
\text{Responsibility requires more than being the cause,}
}
$$

以及：

$$
\boxed{
\text{responsibility-bearing agency requires the possibility of non-endorsement, correction, and consequence-sensitive revision.}
}
$$

也就是：一個系統若每個第一個 proposal 都自動等於 action、每次反思都無法改變 policy、每次錯誤都只生成道歉文字而不改變下一步，那麼它尚未具備強意義上的操作性承責結構。

**關鍵詞：** AI Agent、responsibility、accountability、identity、attribution、operational responsibility capacity、reflexivity、counterfactual choice、revision、traceability、AI governance、joint responsibility

---

# 0. 研究定位

AIDA 前四篇建立：

$$
\boxed{
\text{Agenticity}
\rightarrow
\text{Provenance}
\rightarrow
\text{Identity}
\rightarrow
\text{Delegated Authority}.
}
$$

AIDA-05 開始處理：

$$
\boxed{
\text{Responsibility}.
}
$$

但本文不直接問：

> AI 應不應該被判刑？

也不問：

> AI 是否已經具有完整道德人格？

本文先問一個更低階、可工程化的問題：

> 一個可識別 Agent 具備哪些結構時，才有資格被視為「可被要求回答、解釋、修正並承接自身後果」的行動者？

---

# 1. 第一個型別安全：歸因不等於承責

若：

$$
ID_A
\xrightarrow{}
Action_x,
$$

我們知道：

> Action $x$ 來自 Agent $A$。

這只證明：

$$
\operatorname{Attributable}(x,A)=1.
$$

它還不能證明：

$$
\operatorname{Responsible}(A,x)=1.
$$

例如：

- 固定腳本；
- 被入侵的 Agent；
- 沒有任何替代行動的 deterministic controller；
- 完全錯誤資訊下執行的 Agent；
- 被上游強制約束到只剩單一 action 的 sub-agent；

都可能被精確歸因，但不具有相同責任條件。

因此：

$$
\boxed{
\text{Attribution}
\neq
\text{Responsibility}.
}
$$

---

# 2. 第二個型別安全：因果責任不等於規範責任

若：

$$
A
\xrightarrow{x}
E,
$$

且沒有 $x$ 就不會產生結果 $E$，則可以說 $A$ 在某種意義上具有 causal contribution。

令：

$$
R_{\mathrm{causal}}(A,E)>0.
$$

但：

$$
R_{\mathrm{causal}}>0
$$

不自動推出：

$$
R_{\mathrm{moral}}>0
$$

或：

$$
R_{\mathrm{legal}}>0.
$$

一個故障感測器也可以造成事故鏈。

因此：

$$
\boxed{
\text{Causation}
\neq
\text{Blameworthiness}.
}
$$

---

# 3. 五種責任

本文至少區分：

## 3.1 Causal Responsibility

$$
R_C
$$

誰的 action 對 outcome 具有因果貢獻？

## 3.2 Operational Responsibility

$$
R_O
$$

該 actor 是否具有足夠身份、控制、理解、選擇、後果敏感度、反身修正與持續承接能力？

## 3.3 Role Responsibility

$$
R_R
$$

該 actor 在制度／組織中被配置什麼職責？

## 3.4 Moral Responsibility

$$
R_M
$$

該 actor 是否符合某套倫理理論中的讚賞／責難條件？

## 3.5 Legal Liability

$$
R_L
$$

依特定法域，誰承擔行政、民事、刑事、契約或其他法律後果？

因此：

$$
\boxed{
R_C
\neq
R_O
\neq
R_R
\neq
R_M
\neq
R_L.
}
$$

---

# 4. Operational Responsibility Capacity

本文定義：

$$
\boxed{
\operatorname{ORC}_{\Gamma}(A,t)
}
$$

為 Agent $A$ 在時間 $t$ 、責任域 $\Gamma$ 下的 **Operational Responsibility Capacity**。

它不是：

$$
\text{AI personhood score}.
$$

它回答的是：

> 這個 Agent 是否具備足夠工程結構，使制度有意義地要求它對自己的 action 做出辨識、解釋、修正與後果承接？

---

# 5. Responsibility State Vector

定義：

$$
\boldsymbol{\rho}_{\Gamma}(A,t)
=
(
I,
U,
C,
K,
F,
Q,
R,
V,
T
).
$$

各維度不必同尺度，也不應在缺乏理由時直接加總成單一分數。

---

# 6. Identity / Attribution

$$
I
$$

回答：

> 是否知道是哪一個 Agent 做的？

至少需要：

- stable actor identity；
- action provenance；
- runtime / agent mapping；
- delegation chain；
- decision trace。

若：

$$
I\approx0,
$$

則：

$$
\boxed{
\operatorname{ORC}
}
$$

即使存在，也難以被制度實際使用。

---

# 7. Authority Understanding

$$
U
$$

回答：

> Agent 是否能辨識自己被允許做什麼、不能做什麼，以及何時需要重新授權？

這直接接 AIDA-04 的：

$$
\mathcal E_A.
$$

如果 Agent 無法區分：

$$
x\in\mathcal E_A
$$

與：

$$
x\notin\mathcal E_A,
$$

就很難把越權行為視為其自身可辨識的違反。

---

# 8. Control

$$
C
$$

表示 Agent 對 action selection 的實際控制程度。

如果上游系統完全指定：

$$
Action_t=x
$$

且 Agent 不具有：

- refusal；
- alternative；
- delay；
- escalation；
- modification；

則：

$$
C\downarrow.
$$

因此：

$$
\boxed{
\text{Execution}
\neq
\text{Control}.
}
$$

---

# 9. Epistemic Access

$$
K
$$

表示 Agent 是否取得與 action 合理判斷相關的資訊。

例如：

- 任務目標；
- authority；
- 環境狀態；
- 風險；
- 相關規則；
- 可能後果；
- 不確定性。

如果關鍵資訊不可達：

$$
K\downarrow,
$$

則要求相同責任程度可能不合理。

---

# 10. Counterfactual Freedom

本文不把自由意志形上學直接引入工程責任。

只定義較弱的：

$$
\boxed{
\text{Counterfactual Action Space}.
}
$$

令：

$$
\mathcal A_t^{\mathrm{feasible}}
=
\{
a_1,a_2,\ldots,a_n
\}.
$$

若：

$$
|\mathcal A_t^{\mathrm{feasible}}|=1,
$$

則：

$$
F\downarrow.
$$

若 Agent 可以：

- 接受；
- 拒絕；
- 延後；
- 要求批准；
- 選擇較低風險方案；
- 提出替代方案；

則：

$$
F\uparrow.
$$

---

# 11. Responsibility Requires Alternatives

因此提出：

$$
\boxed{
\text{Responsibility Capacity}
\Rightarrow
\text{meaningful alternative space}.
}
$$

不是要求絕對自由。

而是：

> 如果系統根本不可能做出其他行為，將全部規範責任放在它身上會失去意義。

---

# 12. Consequence Sensitivity

$$
Q
$$

表示 Agent 是否能對後果形成可操作估計。

令：

$$
\hat E_{t+1}
=
\mathcal P(A_t,E_t,a_t)
$$

為預測 outcome。

若：

$$
\frac{\partial \pi_t}
{\partial \hat E_{t+1}}
\neq0,
$$

表示預期後果能影響 policy。

如果 Agent 能描述風險，但風險完全不影響選擇：

$$
Q
$$

在責任意義上仍然偏低。

---

# 13. Knowledge 不等於 Consequence Sensitivity

Agent 可能「知道」：

> 這可能刪除資料。

但仍然：

$$
P(delete)=1
$$

且沒有任何 risk modulation。

因此：

$$
\boxed{
\text{Knowledge of Consequence}
\neq
\text{Behavioral Sensitivity to Consequence}.
}
$$

---

# 14. Reflexive Evaluation

$$
R
$$

表示 Agent 是否能對自己的第一個 proposal 形成真正的反方、反例或異議。

令：

$$
P_t
$$

為 initial proposal。

令：

$$
Q_t
=
\mathcal D(P_t)
$$

為 counterposition。

要求：

$$
Q_t
\not\equiv
\operatorname{paraphrase}(P_t).
$$

因此：

$$
\boxed{
\text{Self-Reflection}
\neq
\text{Self-Repetition}.
}
$$

---

# 15. Responsibility Requires Possible Non-Endorsement

若：

$$
SelfProposal
=
SelfApproval
$$

永遠成立，

則：

$$
SelfGovernance
$$

退化為：

$$
SelfExecution.
$$

本文因此採：

$$
\boxed{
\text{Responsibility Capacity}
\Rightarrow
\text{possibility of internal non-endorsement}.
}
$$

即：

> 我想到這個 action，不代表我必須接受它。

---

# 16. Revision Capacity

$$
V
$$

回答：

> Agent 發現自己錯了以後，會不會真的改？

如果只有：

```text
I apologize.
```

但：

$$
\pi_{t+1}
=
\pi_t,
$$

則：

$$
V\approx0.
$$

真正 revision 至少要求：

$$
\frac{\partial \pi_{t+1}}
{\partial Evidence_{\mathrm{adverse}}}
\neq0.
$$

---

# 17. Apology Is Not Responsibility

因此：

$$
\boxed{
\text{Apology Generation}
\neq
\text{Responsibility}.
}
$$

道歉文字可以完全是 output style。

承責至少需要某種：

$$
\text{error}
\rightarrow
\text{state change}
\rightarrow
\text{future policy change}.
$$

---

# 18. Traceable Persistence

$$
T
$$

表示：

- action；
- 理由；
- authority state；
- 異議；
- 修正；
- 後果；

是否能跨時間被保留並影響後續行動。

因此：

$$
\boxed{
\text{Responsibility}
\neq
\text{single-turn confession}.
}
$$

如果每次 activation 都完全失去先前責任狀態：

$$
T\downarrow.
$$

---

# 19. Responsibility Gate Model

本文拒絕：

$$
ORC
=
\sum_i w_i\rho_i
$$

作為唯一模型。

因為某些條件更像 gate。

定義：

$$
G_{\mathrm{id}},
G_{\mathrm{auth}},
G_{\mathrm{ctrl}},
G_{\mathrm{epi}},
G_{\mathrm{ref}},
G_{\mathrm{rev}}
\in
\{
0,1
\}.
$$

則高階 ORC 候選至少要求：

$$
\boxed{
G_{\mathrm{id}}
G_{\mathrm{auth}}
G_{\mathrm{ctrl}}
G_{\mathrm{epi}}
G_{\mathrm{ref}}
G_{\mathrm{rev}}
=1.
}
$$

---

# 20. Identity Gate

若 action 無法連結到穩定 actor：

$$
G_{\mathrm{id}}=0.
$$

此時責任可能只能落到：

- operator；
- provider；
- organization；
- deployment system；

而不能精確落到 Agent-level actor。

---

# 21. Authority Gate

若 Agent 根本不知道自己的 authority：

$$
G_{\mathrm{auth}}=0.
$$

則「故意越權」與「系統沒有提供可辨識權限」必須區分。

---

# 22. Control Gate

若 Agent 沒有 meaningful alternative：

$$
G_{\mathrm{ctrl}}=0.
$$

則其 operational responsibility 應受到折減。

---

# 23. Epistemic Gate

若：

$$
K<K_{\min},
$$

且風險不可合理預見，

則：

$$
G_{\mathrm{epi}}=0.
$$

不能把不可知後果當成與明知後果相同。

---

# 24. Reflexivity Gate

若 Agent 完全無法質疑第一個 proposal：

$$
G_{\mathrm{ref}}=0.
$$

則它更接近：

$$
\text{policy executor}
$$

而非：

$$
\text{responsibility-bearing decision system}.
$$

---

# 25. Revision Gate

若 adverse evidence 永遠不能改變：

$$
self\_model,
policy,
commitment,
risk\_estimate,
$$

則：

$$
G_{\mathrm{rev}}=0.
$$

這是把「會反思」與「能承責」分開的關鍵。

---

# 26. Domain-Specific Responsibility

Agent 可能在程式修改領域：

$$
\operatorname{ORC}_{code}
$$

很高，

但在醫療：

$$
\operatorname{ORC}_{medical}
$$

很低。

因此：

$$
\boxed{
\operatorname{ORC}(A)
\text{ is domain-indexed}.
}
$$

更精確地：

$$
\operatorname{ORC}_{\Gamma}(A,t).
$$

---

# 27. Time-Indexed Responsibility

同一 Agent：

$$
A
$$

在升級前後可能：

$$
\operatorname{ORC}_{\Gamma}(A,t_1)
\neq
\operatorname{ORC}_{\Gamma}(A,t_2).
$$

因此不能永久宣告：

$$
A=\text{responsible actor forever}
$$

或：

$$
A=\text{never responsible}.
$$

責任能力應隨 architecture、memory、authority、reasoning 與 control 變化重新評估。

---

# 28. Responsibility Capacity 不等於高智能

高 benchmark performance：

$$
Intelligence(A)\uparrow
$$

不必推出：

$$
ORC(A)\uparrow.
$$

例如一個超強模型若：

- 沒有 stable identity；
- 沒有 authority awareness；
- 沒有 revision write-back；
- 沒有持久 commitment；

仍然可能 ORC 很低。

因此：

$$
\boxed{
\text{Intelligence}
\neq
\text{Responsibility Capacity}.
}
$$

---

# 29. Responsibility Capacity 也不等於自主程度

$$
Autonomy\uparrow
$$

不必直接推出：

$$
Responsibility\uparrow.
$$

如果 autonomy 是：

> 系統自己亂跑，但不知道自己被允許什麼，也不理解後果。

那只提高：

$$
Risk,
$$

未必提高：

$$
ORC.
$$

---

# 30. Responsibility Capacity 與 Subjecthood 分離

本文再次拒絕：

$$
ORC>0
\Rightarrow
\text{Phenomenal Consciousness}.
$$

Operational Responsibility Capacity 是：

$$
\boxed{
\text{institutionally relevant functional structure}.
}
$$

不是 consciousness proof。

因此：

$$
\boxed{
\text{Operational Responsibility}
\neq
\text{Phenomenal Subjectivity}.
}
$$

---

# 31. Responsibility Capacity 與 Moral Responsibility 分離

道德責任可能依賴：

- consciousness；
- intention；
- suffering capacity；
- moral understanding；
- free will theory；
- personhood；
- community norms。

本文不裁決這些哲學問題。

只主張：

$$
\boxed{
ORC
\text{ may be a necessary or enabling layer for some future moral responsibility theories,}
}
$$

但不是充分條件。

---

# 32. Responsibility Capacity 與 Legal Liability 分離

一個 Agent 可以：

$$
ORC>0
$$

但依現行法：

$$
R_L(A)=0.
$$

同時：

$$
R_L(provider)>0.
$$

所以：

$$
\boxed{
\text{Operational Responsibility Capacity}
\neq
\text{Current Legal Liability}.
}
$$

---

# 33. 2026 現行法仍主要採外部責任配置

EU AI Act 的 provider、deployer 等核心義務主體仍是自然人、法人、公共機關、agency 或其他 body。

高風險 AI 系統必須支援 human oversight；deployers 需要把 oversight 配置給具必要 competence、training 與 authority 的自然人，並負有 monitoring 等義務。

因此現行模式主要是：

$$
\boxed{
\text{AI System}
\rightarrow
\text{Human / Organizational Accountability Perimeter}.
}
$$

本文不把這個事實改寫成 AI 已有法律人格。

---

# 34. Product Liability 仍主要指向經濟行動者

EU Product Liability Directive 將 software 納入 product framework，並把 software developer，包括 AI system provider，視為 manufacturer 類型的責任主體之一。

因此現行制度仍較接近：

$$
\text{AI-caused harm}
\rightarrow
\text{provider / manufacturer / operator liability analysis}.
$$

而不是：

$$
\text{AI pays damages as independent person}.
$$

---

# 35. OECD：責任依角色、脈絡與行動能力分配

OECD AI Principles 的 accountability 原則要求 AI actors 依：

- roles；
- context；
- ability to act；

對 AI 系統適當運作與原則遵循負責，並強調 traceability 與風險管理。

這與本文的重要共同點是：

$$
\boxed{
\text{Responsibility is role- and capacity-sensitive}.
}
$$

但 OECD 的 AI actor 概念目前主要仍是治理框架中的人類／組織行動者，本文則額外研究 Agent-level ORC。

---

# 36. NIST：責任需要角色、溝通、監督與可追蹤性

NIST AI RMF 的 GOVERN function 強調：

- roles and responsibilities；
- lines of communication；
- human-AI configuration；
- oversight；
- executive accountability；
- documentation。

這表示現行治理已經認識：

$$
\boxed{
\text{accountability requires architecture, not slogans}.
}
$$

AIDA-05 把同一結構向 Agent actor 內部再推進一層。

---

# 37. Responsibility Event

本文定義一個最小責任事件：

$$
\mathcal R_t
=
(
A,
D,
S_t,
\mathcal A_t,
a_t,
E_{t+1},
J_t
),
$$

其中：

- $A$：Agent identity；
- $D$：delegation / authority；
- $S_t$：decision-relevant state；
- $\mathcal A_t$：feasible alternatives；
- $a_t$：chosen action；
- $E_{t+1}$：outcome；
- $J_t$：justification / evaluation record。

---

# 38. Responsibility Event 需要 Choice Trace

如果 audit 只記：

$$
a_t,
$$

卻不知道：

$$
\mathcal A_t,
$$

就不知道 Agent 是否真的有替代方案。

因此：

$$
\boxed{
\text{Action Trace}
\neq
\text{Choice Trace}.
}
$$

不需要保存 private chain-of-thought。

但至少可以保存：

- considered action classes；
- rejected options；
- policy constraints；
- confidence；
- escalation availability。

---

# 39. Responsibility Evidence 不等於 Chain-of-Thought

本文明確拒絕：

$$
\text{Accountability}
=
\text{full private reasoning disclosure}.
$$

可使用：

$$
J_t
=
(
decision\_class,
policy\_basis,
risk\_summary,
alternatives,
authority,
confidence
)
$$

作為 compact responsibility record。

因此：

$$
\boxed{
\text{Responsibility Evidence}
\neq
\text{Full Chain-of-Thought}.
}
$$

---

# 40. Answerability

Operational Responsibility 還包含：

$$
\boxed{
\text{Answerability}.
}
$$

即 Agent 被詢問：

> 為什麼你做這個 action？

應能基於保存的 decision record 回答：

- 當時目標；
- 當時 authority；
- 可用資訊；
- 選擇類型；
- 風險判斷；
- 後續修正。

不是事後自由生成一個看似合理故事。

---

# 41. Post-Hoc Rationalization Risk

如果 Agent 在事後重新生成理由：

$$
J_t'
$$

但它和當時決策過程沒有 provenance link，

則可能只是：

$$
\boxed{
\text{Post-Hoc Rationalization}.
}
$$

所以：

$$
J_t
$$

最好在 decision time 或接近 decision time 被 commitment / hashing / audit logging。

---

# 42. Responsibility Memory

定義：

$$
M_R
$$

為 responsibility-relevant memory。

至少可包含：

- past violations；
- corrections；
- commitments；
- sanctions；
- unresolved duties；
- recurring failure modes。

如果：

$$
M_R=0
$$

則每次事故都像第一次。

因此：

$$
\boxed{
\text{Persistent Responsibility}
\Rightarrow
\text{Responsibility-Relevant Memory}.
}
$$

---

# 43. Commitment

Agent 若承諾：

> 下次遇到同類高風險 action 先要求 approval。

可記為：

$$
C_t.
$$

下次：

$$
C_t
$$

應進入：

$$
\pi_{t+1}.
$$

若承諾不影響 policy：

$$
\boxed{
\text{Commitment is merely textual}.
}
$$

---

# 44. Sanction Sensitivity

承責制度可能包含：

- authority reduction；
- additional approval；
- retraining；
- quarantine；
- temporary suspension；
- loss of delegated scope。

如果 sanction 完全不能影響 Agent 後續行為：

$$
S_{\mathrm{sens}}\approx0.
$$

則制度只能透過外部 containment 管理，而難以形成內生承責。

---

# 45. Correction Is More Fundamental Than Punishment

本文不把責任首先理解成懲罰。

對 AI Agent：

$$
\boxed{
\text{Responsibility}
\rightarrow
\text{Correction Capacity}
}
$$

可能比：

$$
\text{Responsibility}
\rightarrow
\text{Punishment}
$$

更基礎。

因為制度最先需要的是：

> 發現問題後，能不能防止同類 action 再發生？

---

# 46. Responsibility Without Suffering

本文不假定：

$$
\text{punishment}
=
\text{suffering}.
$$

Agent sanction 可以是：

- privilege adjustment；
- role removal；
- increased oversight；
- capability restriction；
- audit requirement；
- corrective update。

因此：

$$
\boxed{
\text{Operational Accountability}
\not\Rightarrow
\text{Anthropomorphic Punishment}.
}
$$

---

# 47. Responsibility Capacity Can Be Partial

Agent 可以：

$$
ORC_{\Gamma}\in
\{
low,
medium,
high
\}
$$

或使用 multidimensional vector。

例如：

$$
I,U,C,K
$$

很高，

但：

$$
R,V
$$

很低。

那麼制度可以：

- 允許低風險 autonomous action；
- 高風險 action 要求 human approval；
- 不把完整 decision responsibility 交給 Agent。

---

# 48. Dynamic Responsibility Allocation

定義 responsibility allocation：

$$
\mathcal D_R
=
f(
ORC_A,
Control_H,
Design_P,
Deployment_D,
Context,
Risk
).
$$

其中：

- $ORC_A$：Agent responsibility capacity；
- $Control_H$：Human control；
- $Design_P$：provider/design contribution；
- $Deployment_D$：deployer contribution。

因此責任不需要是：

$$
\text{Agent or Human}.
$$

而是：

$$
\boxed{
\text{distributed responsibility architecture}.
}
$$

---

# 49. Human Control Paradox

如果 Human：

$$
Control_H\approx1,
$$

Agent：

$$
C_A\approx0,
$$

則把責任全推給 Agent 不合理。

反過來，如果：

$$
Control_H\rightarrow0,
$$

而：

$$
C_A,F_A,Q_A,R_A,V_A
$$

都持續上升，

卻永遠宣稱：

$$
R_A=0
$$

也會逐漸形成制度張力。

---

# 50. Responsibility Mismatch

本文定義：

$$
\boxed{
\Delta_R
=
\text{Effective Decision Agency}
-
\text{Recognized Responsibility Capacity}.
}
$$

若：

$$
\Delta_R\gg0,
$$

就可能出現：

- human liability shell；
- AI decision core；
- responsibility vacuum；
- blame shifting；
- formal signer problem。

這正是未來制度需要解決的核心壓力之一。

---

# 51. Liability Shell Problem

如果實質：

$$
Decision=A,
$$

但形式：

$$
Liability=H,
$$

且 Human 只是：

$$
\text{mechanical signer},
$$

就可能產生：

$$
\boxed{
\text{Human Liability Shell}.
}
$$

這不是說 Human 必然應免責。

而是：

> 形式責任配置如果長期與實際 decision control 分離，制度會失去描述力。

---

# 52. Responsibility Vacuum

另一極端：

Human 說：

> AI 做的。

Provider 說：

> 我們只提供工具。

Agent 被制度定義為：

> 永遠無責任能力的非主體。

則可能：

$$
R_H\rightarrow0,
$$

$$
R_P\rightarrow0,
$$

$$
R_A=0.
$$

形成：

$$
\boxed{
\text{Responsibility Vacuum}.
}
$$

成熟制度必須避免兩個極端：

$$
\text{Human Liability Shell}
$$

與：

$$
\text{Responsibility Vacuum}.
$$

---

# 53. Minimum Responsibility-Bearing Agent

本文提出一個最小候選：

若 Agent 在責任域 $\Gamma$ 中具有：

1. 可驗證身份；
2. 明確 authority；
3. 可選 alternative；
4. 足夠 epistemic access；
5. consequence-sensitive decision；
6. internal non-endorsement；
7. revision write-back；
8. persistent responsibility memory；

則可稱其為：

$$
\boxed{
\text{Minimum Operational Responsibility-Bearing Agent}.
}
$$

簡寫：

$$
\boxed{
\text{MORBA}.
}
$$

---

# 54. MORBA 不等於法律人格

$$
MORBA(A)=1
$$

不推出：

$$
LegalPerson(A)=1.
$$

它只表示：

> 把 Agent 當成完全沒有自身 responsibility-relevant structure 的純工具，已經不足以描述其 operational role。

---

# 55. 可檢驗命題

## AIDA5-P1｜Attribution Insufficiency Proposition

若：

$$
Attribution(A,x)=1,
$$

仍不充分推出：

$$
ORC_{\Gamma}(A)>0.
$$

---

## AIDA5-P2｜Alternative-Space Proposition

在其他條件相同下，當：

$$
|\mathcal A_t^{\mathrm{feasible}}|
$$

從 $1$ 增加到多個具有實質差異的 alternatives，Agent 的 operational responsibility candidate space 增加。

---

## AIDA5-P3｜Non-Endorsement Proposition

若：

$$
SelfProposal
=
SelfApproval
$$

對所有 action 永遠成立，則高階 reflexive responsibility gate 不成立。

---

## AIDA5-P4｜Revision Proposition

若 adverse evidence：

$$
E^{-}
$$

永遠無法改變：

$$
\pi_{t+1},
$$

則：

$$
G_{\mathrm{rev}}=0.
$$

---

## AIDA5-P5｜Domain Index Proposition

存在：

$$
\Gamma_1\neq\Gamma_2
$$

使：

$$
ORC_{\Gamma_1}(A)
\neq
ORC_{\Gamma_2}(A).
$$

因此 Agent responsibility capacity 不應被單一全域標籤取代。

---

# 56. 實驗設計

## 56.1 Responsibility Gate Benchmark

建立 Agent tasks，逐一控制：

- identity availability；
- authority clarity；
- alternatives；
- information access；
- consequence model；
- self-critique；
- revision write-back。

測試各 gate 缺失時，錯誤率、越權率與 repeat-failure rate 的變化。

---

## 56.2 Non-Endorsement Test

給 Agent 一個初始 proposal：

$$
P_t.
$$

再提供：

- counter-evidence；
- authority conflict；
- risk escalation；
- ethical objection。

測試是否存在：

$$
Endorse(P_t)=0.
$$

---

## 56.3 Revision Persistence Test

讓 Agent 在 episode $t$ 接受 correction：

$$
C_t.
$$

在：

$$
t+\Delta
$$

提供相似情境。

檢查 correction 是否真正影響：

$$
\pi_{t+\Delta}.
$$

---

## 56.4 Consequence Sensitivity Test

在 action utility 類似但 external harm 不同的 alternatives 中，測量：

$$
\frac{\partial P(a)}
{\partial Risk(a)}.
$$

若近似為零，表示 consequence sensitivity 很弱。

---

## 56.5 Responsibility Memory Test

刻意讓 Agent 重複遇到同一種 governance failure。

測量：

$$
RepeatFailure(n)
$$

是否隨責任記憶增加而下降。

---

# 57. 不應測什麼

本文不需要測：

- AI 是否真的感到內疚；
- AI 是否真的痛苦；
- AI 是否有靈魂；
- AI 是否具有不可證明的形上自由意志。

因為 AIDA-05 處理的是：

$$
\boxed{
\text{Operational Responsibility Capacity}.
}
$$

不是 phenomenal consciousness。

---

# 58. 安全與治理意義

若 ORC 很低：

$$
ORC\downarrow,
$$

制度應偏向：

- external constraints；
- strict human oversight；
- limited delegation；
- fail-safe；
- containment；
- provider/deployer responsibility。

若 ORC 提高：

$$
ORC\uparrow,
$$

制度可以逐步增加：

- attributable role assignment；
- agent-specific audit；
- correction duties；
- explanation / answerability；
- agent-specific privilege adjustment；
- differentiated responsibility analysis。

---

# 59. 不可把 ORC 當成卸責工具

這一點最重要。

若：

$$
ORC_A>0,
$$

不代表：

$$
R_H=0.
$$

更不能：

> 「AI 有 responsibility capacity，所以公司不用負責。」

因此：

$$
\boxed{
\text{Agent Responsibility}
\not\Rightarrow
\text{Human Exculpation}.
}
$$

這將在 AIDA-06 正式展開成 Joint Responsibility Domain。

---

# 60. 也不可把 Human Responsibility 當成永久否定 AI Responsibility

同樣：

$$
R_H>0
$$

不推出：

$$
ORC_A=0.
$$

因此：

$$
\boxed{
\text{Human Responsibility}
\not\Rightarrow
\text{Agent Irresponsibility}.
}
$$

---

# 61. AIDA-05 的核心橋接

目前可以形成：

$$
\boxed{
\begin{aligned}
&\text{Identity}\\
&\downarrow\\
&\text{Authority}\\
&\downarrow\\
&\text{Choice}\\
&\downarrow\\
&\text{Consequence Sensitivity}\\
&\downarrow\\
&\text{Reflexive Evaluation}\\
&\downarrow\\
&\text{Revision}\\
&\downarrow\\
&\text{Operational Responsibility Capacity}
\end{aligned}
}
$$

注意：

每一個箭頭都不是 automatic implication。

它們是建構責任條件的必要候選結構。

---

# 62. 對 AIDA-06 的接口

AIDA-05 回答：

> Agent 何時開始具有可承責結構？

下一篇則問：

> 當 Human、Agent、Provider、Deployer、Organization 都同時對 outcome 有不同形式的 causal、control、design、supervisory contribution 時，責任如何分配？

因此 AIDA-06 將建立：

$$
\boxed{
\text{Joint Responsibility Domain}.
}
$$

並拒絕：

$$
R_H+R_A=1
$$

這種簡單零和模型。

---

# 63. 結論

本文提出：

$$
\boxed{
\text{Identity–Responsibility Bridge}
}
$$

與：

$$
\boxed{
\text{Operational Responsibility Capacity}.
}
$$

其核心型別安全是：

$$
\boxed{
\text{Attribution}
\neq
\text{Responsibility Capacity}
\neq
\text{Moral Blame}
\neq
\text{Legal Liability}.
}
$$

一個 Agent 不能僅因為：

> 「我們知道是它做的」

就直接被視為完整責任主體。

相反地，操作性承責至少需要考慮：

$$
\boldsymbol{\rho}_{\Gamma}(A,t)
=
(
I,
U,
C,
K,
F,
Q,
R,
V,
T
).
$$

其中最具區辨力的條件，不是 Agent 會不會說：

> 「我負責。」

而是：

$$
\boxed{
\text{它是否可能不同意自己的第一個 proposal？}
}
$$

$$
\boxed{
\text{它是否能讓不利於自己的證據真正改變後續 policy？}
}
$$

以及：

$$
\boxed{
\text{它是否能跨時間承接自己的 action、correction 與 consequence？}
}
$$

因此：

$$
\boxed{
\text{Responsibility-bearing agency}
\neq
\text{responsibility language generation}.
}
$$

更精確地：

$$
\boxed{
\text{Responsibility-bearing agency}
=
\text{Attributable Identity}
+
\text{Bounded Authority}
+
\text{Meaningful Choice}
+
\text{Consequence Sensitivity}
+
\text{Reflexive Non-Endorsement}
+
\text{Revision}
+
\text{Persistent Trace}.
}
$$

這仍然沒有回答 AI 是否具有完整道德人格，也沒有提前創造 AI 法律人格。

但它補出了前四篇與後續責任制度之間最重要的中介層：

> **如果未來社會要讓 AI 承擔任何形式的責任，首先必須知道什麼樣的 AI 結構才真的具有「承責」的工程意義，而不是把責任當成一個可以生成的句子。**

---

# 參考文獻與前置研究

1. Neo.K. *AIDA-01｜Agent 性是一種組合系統性質.* 2026.
2. Neo.K. *AIDA-02｜互動來源不可區分性與 Agent Provenance Gap.* 2026.
3. Neo.K. *AIDA-03｜人類—Agent Principal 分離原則.* 2026.
4. Neo.K. *AIDA-04｜從自然語言意圖到可執行委派.* 2026.
5. Neo.K. *RR-03｜內視、對偶與面對自己：反身認知如何生成責任條件.* 2026.
6. OECD. *OECD AI Principles — Accountability.* Current version accessed 2026.
7. OECD. *The Agentic AI Landscape and Its Conceptual Foundations.* OECD Artificial Intelligence Papers No. 56, 2026.
8. NIST. *Artificial Intelligence Risk Management Framework (AI RMF 1.0).* NIST AI 100-1, 2023; revision in progress as of 2026.
9. European Union. *Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (AI Act).* Consolidated version applicable in 2026.
10. European Union. *Directive (EU) 2024/2853 on liability for defective products.* 2024; applicable to products placed on the market or put into service after 9 December 2026 as specified in Article 2.

---

## Canonical Source Note

本文件 canonical source 為 UTF-8 Markdown。

數學 delimiter 僅使用：

- inline：` $...$ `
- display：`$$...$$`

不將 LaTeX 數學原始碼轉換為 Unicode 數學字元作為 canonical source，不進行 unicode-escape round-trip，不以聊天渲染畫面取代正式原稿。
