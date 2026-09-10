# AIDA-06｜連帶責任域
## 非零和責任、責任圖與 Human–Agent–Provider–Deployer 的分散式承責架構

**English Title:** Joint Responsibility Domains: Non-Zero-Sum Responsibility, Responsibility Graphs, and Distributed Accountability Across Humans, Agents, Providers, and Deployers  
**系列：** AI Agent Identity, Delegation, and Accountability Infrastructure Series  
**系列縮寫：** AIDA  
**編號：** AIDA-06  
**版本：** v0.1  
**日期：** 2026-09-08  
**狀態：** Research Draft / Canonical UTF-8 Markdown Source  
**作者：** Neo.K  
**協作整理：** GPT-5.6 Sol  

---

## 摘要

AIDA-05 已提出 Operational Responsibility Capacity（ORC），用來描述一個可歸因 Agent 在特定責任域中是否具有足夠的身份、權限理解、控制、資訊取得、替代選擇、後果敏感度、反身評估、修正與跨時間承接能力。這使 AI Agent 首次可以在不預設法律人格或道德人格的情況下，被分析為具有部分「承責條件」的 operational actor。

但只要承認：

$$
ORC_A>0,
$$

就立刻產生另一個危險誤解：

> 如果 AI 開始負責，是不是人類、公司、provider 或 deployer 就可以少負責？

本文回答：

$$
\boxed{
\text{No.}
}
$$

並提出 **Joint Responsibility Domain（連帶責任域）**。其第一個核心原則為：

$$
\boxed{
\text{Responsibility is not a conserved scalar quantity.}
}
$$

也就是，責任不是一個必須滿足：

$$
R_H+R_A=1
$$

的零和總量。

同一事件中，Agent 可以具有 decision responsibility，Provider 可以具有 design responsibility，Deployer 可以具有 deployment / monitoring responsibility，Human Operator 可以具有 authorization / supervision responsibility，而 Organization 可以具有 governance、remedial、compensatory 或 institutional responsibility。這些責任可以同時成立，因為它們並不是同一維度上的同一份物理資源。

本文將事件 $E$ 中 actor $i$ 的責任表示為責任向量：

$$
\mathbf r_i(E,t)
=
(
r_i^{causal},
r_i^{design},
r_i^{deployment},
r_i^{authorization},
r_i^{supervision},
r_i^{decision},
r_i^{monitoring},
r_i^{remedial},
r_i^{compensatory}
).
$$

因此：

$$
\mathbf r_H>0
$$

與：

$$
\mathbf r_A>0
$$

可以同時成立。

本文進一步定義責任圖：

$$
G_R(E)
=
(
V,
E_C,
E_A,
E_K,
E_D,
E_B,
E_M
),
$$

其中節點 $V$ 是 Human、Agent、Provider、Deployer、Organization、Infrastructure Operator 或其他相關 actor；不同 edge families 分別描述 causal、authority、control、duty、benefit 與 remediation relations。責任不再從「最後按下按鈕的人」單點推導，而從完整 socio-technical relation graph 中判定。

本文特別區分兩種制度失敗。第一種是 **Human Liability Shell**：AI 實質持有 decision control，人類卻只剩形式簽名與法律責任，造成 decision authority 與 formal liability 長期脫鉤。第二種是 **Responsibility Vacuum**：Human、Provider、Deployer 都以「AI 做的」互相推責，而 AI 又因制度上永遠被視為無責任能力的工具，最終形成無人能被要求 explanation、correction、remediation 或 compensation 的責任空洞。

本文並提出 **Responsibility Coverage** 與 **Duty Coverage**。對一組事件後責任義務：

$$
\mathcal D_E
=
\{
d_1,d_2,\ldots,d_n
\},
$$

令：

$$
\alpha(d_j)
\subseteq
V
$$

表示哪些 actor 被配置該義務。若：

$$
\alpha(d_j)=\varnothing,
$$

則存在真正的 duty gap；若：

$$
|\alpha(d_j)|>1,
$$

則代表 responsibility overlap，而不是數學錯誤。成熟制度的目的不是讓所有 overlap 消失，而是避免所有重要 duty 都落入空集合。

截至 2026 年，OECD AI Principles 已明確要求 AI actors 依其角色、脈絡與 ability to act 承擔 accountability，並要求不同 AI actors、供應者、使用者與 stakeholder 間適當合作；NIST AI RMF 亦以跨 lifecycle 的 roles、responsibilities、oversight、communication 與 governance 為核心。EU AI Act 則仍主要將義務配置給 provider、deployer 等自然人、法人或其他組織行動者，且高風險 AI 的 human oversight 必須交給真正具有 competence、training、authority 與 support 的自然人。這些現行制度都支持「責任依角色分散配置」的方向，但尚未建立具有 ORC 的 AI Agent 自身作為獨立 responsibility-bearing actor 的一般法律模型。

本文因此不主張把現行人類責任轉移給 AI，而是提出一個更保守的原則：

$$
\boxed{
\text{Agent responsibility}
\not\Rightarrow
\text{human exculpation},
}
$$

以及：

$$
\boxed{
\text{human responsibility}
\not\Rightarrow
\text{agent irresponsibility}.
}
$$

這兩句共同構成未來 Human–AI joint accountability 的最低型別安全。

**關鍵詞：** AI Agent、joint responsibility、distributed accountability、responsibility gap、responsibility vacuum、liability shell、shared responsibility、ORC、provider、deployer、human oversight、responsibility graph

---

# 0. 研究定位

AIDA 前五篇形成：

$$
\boxed{
\text{Agenticity}
\rightarrow
\text{Provenance}
\rightarrow
\text{Identity}
\rightarrow
\text{Authority}
\rightarrow
\text{Responsibility Capacity}.
}
$$

AIDA-06 處理：

$$
\boxed{
\text{Responsibility Allocation}.
}
$$

也就是：

> 如果 Human、Agent、Provider、Deployer 與 Organization 都對同一 outcome 有不同形式的影響，應該怎麼談「誰負責」？

---

# 1. 最常見的錯誤：把責任當成一個餅

很多討論隱含：

$$
R_{total}=1.
$$

如果：

$$
R_A=0.4,
$$

就直覺認為：

$$
R_H=0.6.
$$

這相當於：

$$
\boxed{
R_H+R_A=1.
}
$$

本文稱這種直覺為：

$$
\boxed{
\text{Responsibility Conservation Fallacy}.
}
$$

責任通常不是一個守恆標量。

---

# 2. 為什麼責任不是守恆量？

因為不同 actor 可以同時違反不同 duty。

例如一個 Agent 錯誤選擇 action：

$$
r_A^{decision}>0.
$$

Provider 同時可能：

$$
r_P^{design}>0.
$$

Deployer 可能：

$$
r_D^{monitoring}>0.
$$

Human Supervisor 可能：

$$
r_H^{supervision}>0.
$$

Organization 可能：

$$
r_O^{remedial}>0.
$$

這些不是同一份責任被分割。

---

# 3. 責任向量

本文定義 actor $i$ 的責任向量：

$$
\mathbf r_i(E,t)
=
(
r_i^{causal},
r_i^{design},
r_i^{deployment},
r_i^{authorization},
r_i^{supervision},
r_i^{decision},
r_i^{monitoring},
r_i^{remedial},
r_i^{compensatory}
).
$$

因此：

$$
\boxed{
\mathbf r_i
\in
\mathbb R_{\geq0}^{9}
}
$$

只是分析表示，不代表九維已經是終局分類。

---

# 4. 九個責任維度

## 4.1 Causal Responsibility

$$
r_i^{causal}
$$

Actor 對 outcome 的因果貢獻。

## 4.2 Design Responsibility

$$
r_i^{design}
$$

Actor 是否設計了造成風險的 architecture、policy、interface 或 control structure。

## 4.3 Deployment Responsibility

$$
r_i^{deployment}
$$

誰決定把系統部署到特定場域、使用者或風險環境。

## 4.4 Authorization Responsibility

$$
r_i^{authorization}
$$

誰授予 action authority，是否過度授權。

## 4.5 Supervision Responsibility

$$
r_i^{supervision}
$$

誰有義務監督、介入或升級。

## 4.6 Decision Responsibility

$$
r_i^{decision}
$$

誰在有效 alternative space 中選擇了造成效果的 action。

## 4.7 Monitoring Responsibility

$$
r_i^{monitoring}
$$

誰有義務觀察系統表現與異常。

## 4.8 Remedial Responsibility

$$
r_i^{remedial}
$$

事故後誰有義務修復、通知、矯正與降低再發。

## 4.9 Compensatory Responsibility

$$
r_i^{compensatory}
$$

依制度、契約或法律誰負擔補償。

---

# 5. 責任維度不必對所有 actor 都存在

例如：

$$
r_A^{design}=0
$$

可能成立，

因為 Agent 沒有參與自身底層設計。

但：

$$
r_A^{decision}>0
$$

仍可能成立。

同樣：

$$
r_P^{decision}=0
$$

不代表：

$$
r_P^{design}=0.
$$

---

# 6. 不能把責任向量直接硬加成罪惡分數

本文不主張：

$$
Score_i
=
\sum_k r_i^k
$$

可以直接決定：

> 誰比較有罪。

因為不同責任維度可能使用不同尺度、規範與法律效果。

所以：

$$
\boxed{
\text{Responsibility Vector}
\neq
\text{Blame Score}.
}
$$

---

# 7. 責任可以重疊

如果同一 duty：

$$
d
$$

同時由兩個 actor 承擔：

$$
\alpha(d)
=
\{
H,D
\},
$$

這不是制度錯誤。

這叫：

$$
\boxed{
\text{Responsibility Overlap}.
}
$$

例如 Provider 與 Deployer 都可能對 monitoring framework 有不同責任。

---

# 8. 重疊責任不等於重複處罰

責任 overlap：

$$
|\alpha(d)|>1
$$

不代表：

> 每個 actor 都應承擔完整相同法律制裁。

法律後果仍需依：

- causal contribution；
- fault；
- control；
- statutory duty；
- contract；
- jurisdiction；

另行配置。

因此：

$$
\boxed{
\text{Responsibility Overlap}
\neq
\text{Penalty Duplication}.
}
$$

---

# 9. 可分割負擔才需要正規化

例如一筆固定 damages：

$$
L
$$

如果法院決定按比例分配：

$$
\sum_i \lambda_i=1,
$$

這是：

$$
\boxed{
\text{burden allocation}.
}
$$

不是證明所有 responsibility 本身必須滿足：

$$
\sum_i R_i=1.
$$

這兩件事必須分開。

---

# 10. Joint Responsibility Domain

本文定義：

$$
\boxed{
\mathcal J_R(E,t,\Gamma)
}
$$

為事件 $E$ 在時間 $t$ 、責任域 $\Gamma$ 下的 **Joint Responsibility Domain**。

令：

$$
V_R
=
\{
H,
A,
P,
D,
O,
I,\ldots
\},
$$

其中：

- $H$：Human；
- $A$：Agent；
- $P$：Provider；
- $D$：Deployer；
- $O$：Organization；
- $I$：Infrastructure / other actor。

則：

$$
\mathcal J_R
=
\{
(i,\mathbf r_i)
\mid
i\in V_R
\}.
$$

---

# 11. 責任圖

只用向量仍然不足以表達 actor 彼此關係。

因此定義：

$$
\boxed{
G_R(E)
=
(
V,
E_C,
E_A,
E_K,
E_D,
E_B,
E_M
).
}
$$

---

# 12. Causal Edges

$$
E_C
$$

表示：

$$
i
\xrightarrow{cause}
j.
$$

例如：

$$
Agent
\xrightarrow{action}
Outcome.
$$

---

# 13. Authority Edges

$$
E_A
$$

表示：

$$
i
\xrightarrow{delegates}
j.
$$

例如：

$$
Human
\xrightarrow{D}
Agent.
$$

---

# 14. Control Edges

$$
E_K
$$

表示：

$$
i
\xrightarrow{controls}
j.
$$

例如 Deployer 可以：

- pause；
- revoke；
- constrain；
- override；

Agent。

---

# 15. Duty Edges

$$
E_D
$$

表示：

$$
i
\xrightarrow{owes}
d.
$$

也就是哪個 actor 對誰、對什麼 outcome 有義務。

---

# 16. Benefit Edges

$$
E_B
$$

表示：

$$
i
\xrightarrow{benefits\ from}
system.
$$

因為誰享有系統經濟利益，也可能影響某些 governance、insurance 或 remedial obligations。

本文不主張：

$$
\text{benefit}
\Rightarrow
\text{automatic blame}.
$$

但 benefit 是制度分配責任時可能考慮的一個 relation。

---

# 17. Remediation Edges

$$
E_M
$$

表示：

$$
i
\xrightarrow{can\ repair}
E.
$$

有時事故原因 actor 與最有能力修復的人並不同。

因此：

$$
\boxed{
\text{Causal Responsibility}
\neq
\text{Remedial Capacity}.
}
$$

---

# 18. 責任不是從最後一步開始倒推

最弱的責任模型是：

> 誰最後按下按鈕，誰負責。

Agent 時代這會失效。

真正需要的是：

$$
\boxed{
\text{Outcome}
\rightarrow
\text{Provenance Graph}
\rightarrow
\text{Responsibility Graph}.
}
$$

---

# 19. Control–Knowledge–Authority 三角

一個 actor 的責任判定至少需要考慮：

$$
C_i
$$

Control；

$$
K_i
$$

Knowledge；

$$
A_i
$$

Authority。

可以抽象表示：

$$
r_i^k
=
f_k(
C_i,
K_i,
A_i,
Duty_i,
ORC_i,
Context
).
$$

不同 responsibility dimension 使用不同函數。

---

# 20. 高 control 通常增加某些責任，不是全部責任

如果：

$$
C_A\uparrow,
$$

Agent 的：

$$
r_A^{decision}
$$

可能提高。

但它不會自動使：

$$
r_P^{design}
$$

下降。

因此：

$$
\boxed{
r_A^{decision}\uparrow
\not\Rightarrow
r_P^{design}\downarrow.
}
$$

---

# 21. AI 承責不等於人類免責

本文第一個核心規則：

$$
\boxed{
\text{Agent Responsibility}
\not\Rightarrow
\text{Human Exculpation}.
}
$$

例如 Human 可以因：

- 明知風險仍部署；
- 過度授權；
- 忽略 warning；
- 假裝監督；
- 不合理 delegation；

持續有責任。

---

# 22. 人類負責也不等於 AI 永遠不負責

第二個核心規則：

$$
\boxed{
\text{Human Responsibility}
\not\Rightarrow
\text{Agent Irresponsibility}.
}
$$

如果 Agent 具有：

$$
ORC_{\Gamma}>0
$$

且它在 meaningful alternative space 中做出某 action，則至少可以分析：

$$
r_A^{decision},
r_A^{remedial},
$$

而不必因為 Human 仍有責任就把 Agent 永久降回純 causal tool。

---

# 23. Provider Responsibility 不因 Agent 變自主而自動消失

Provider 仍可能對：

- unsafe default；
- inadequate logging；
- flawed authorization model；
- missing revocation；
- inadequate testing；
- known defect；

負有：

$$
r_P^{design}>0.
$$

因此：

$$
\boxed{
\text{Autonomous Agent}
\neq
\text{Provider Immunity}.
}
$$

---

# 24. Deployer Responsibility

Deployer 決定：

- 在哪裡用；
- 給誰用；
- 連哪些資料；
- 給多少權限；
- 是否提供 human oversight；
- 是否繼續使用異常系統。

因此：

$$
r_D^{deployment},
r_D^{monitoring},
r_D^{authorization}
$$

可以獨立存在。

---

# 25. Organization Responsibility

公司或組織可能具有：

$$
r_O^{governance},
r_O^{remedial},
r_O^{compensatory}
$$

即使無法把每一個決策歸因到單一員工。

這接近傳統 corporate responsibility 的結構，而不是 AI 特有問題。

---

# 26. AI Agent Responsibility

當：

$$
ORC_A
$$

足夠，

Agent 可以具備：

$$
r_A^{decision}>0,
$$

$$
r_A^{authorization}>0
$$

如果它被允許 re-delegate，

以及：

$$
r_A^{remedial}>0
$$

如果它有能力修正自身 policy / commitments。

---

# 27. Dynamic Responsibility Migration

隨 AI 能力與制度改變：

$$
\mathbf r_i(t)
$$

也會改變。

例如早期：

$$
r_H^{decision}\gg r_A^{decision}.
$$

中期可能：

$$
r_H^{decision}
\approx
r_A^{decision}.
$$

後期甚至：

$$
r_A^{decision}>r_H^{decision}.
$$

但：

$$
r_P^{design}
$$

可能仍然存在。

---

# 28. Responsibility Migration 不等於 Responsibility Transfer

本文區分：

$$
\boxed{
\text{Migration}
\neq
\text{Transfer}.
}
$$

Migration 表示實際決策結構改變，使部分責任自然移動。

Transfer 則像：

> 公司宣布從今天起所有問題都算 AI 的。

後者不是有效責任分析。

---

# 29. Responsibility Dumping

本文定義：

$$
\boxed{
\text{Responsibility Dumping}
}
$$

為 actor 在沒有相對應 control / authority / ORC 轉移的情況下，試圖把自身責任形式上丟給另一 actor。

例如：

$$
Provider
\rightarrow
\text{AI did it}
$$

但 Provider 仍控制：

- model update；
- deployment policy；
- logging；
- permissions。

則責任並未因此消失。

---

# 30. Human Liability Shell

若：

$$
DecisionControl_A\gg DecisionControl_H,
$$

但：

$$
FormalLiability_H\gg FormalLiability_A,
$$

Human 又缺乏：

- meaningful understanding；
- real veto；
- sufficient time；
- actual authority；

則可能形成：

$$
\boxed{
\text{Human Liability Shell}.
}
$$

---

# 31. Human Liability Shell 不等於所有 human oversight 都無效

真正 human oversight 仍然有價值。

問題是：

$$
\boxed{
\text{Oversight Title}
\neq
\text{Oversight Capacity}.
}
$$

如果人類只是形式簽字：

$$
OversightCapacity\approx0.
$$

那把完整 responsibility 建立在「他是 supervisor」這個職稱上會失真。

---

# 32. EU AI Act 對 meaningful oversight 的現實支持

截至 2026 年的 EU AI Act，Article 26 要求 high-risk AI deployer 把 human oversight 配置給具有必要：

- competence；
- training；
- authority；
- support；

的自然人。

這意味著現行法本身也沒有把：

$$
\text{human present}
$$

當成：

$$
\text{meaningful oversight}.
$$

必須有實際能力與 authority。

---

# 33. Responsibility Vacuum

另一個極端：

$$
\boxed{
\text{Responsibility Vacuum}.
}
$$

發生在：

Human：

> AI 做的。

Provider：

> 我只提供模型。

Deployer：

> 我只照系統建議。

Agent：

> 制度不承認我有任何責任地位。

最終：

$$
\alpha(d)=\varnothing
$$

對某些重要 duty 成立。

---

# 34. Responsibility Gap Literature

AI responsibility gap 並非新問題。

相關文獻已討論：

- culpability gaps；
- moral accountability gaps；
- public accountability gaps；
- active responsibility gaps；
- epistemic gaps；
- control gaps。

因此本文不主張：

> AI 出現後第一次有人發現責任很難分配。

本文新增的是：

$$
\boxed{
\text{Agent ORC}
+
\text{Joint Responsibility Graph}
}
$$

的組合。

---

# 35. 四種 Responsibility Gaps

Santoni de Sio 與 Mecacci 的研究指出，AI responsibility gap 不應被理解成單一問題，而至少涉及不同種類的 culpability、moral/public accountability 與 active responsibility gaps。

這支持本文：

$$
\boxed{
\text{Responsibility is multidimensional}.
}
$$

而不是：

$$
R=\text{one scalar}.
$$

---

# 36. Shared Responsibilization

Lang、Nyholm 與 Blumenthal-Barby 在 black-box healthcare AI 中提出 shared responsibilization，用多個 stakeholder 主動承接 explanation、retrospective accountability、corrective、anticipatory 等責任 gap。

這與本文共享：

$$
\boxed{
\text{multiple actors may legitimately carry responsibility simultaneously}.
}
$$

但本文更進一步加入：

$$
ORC_A
$$

作為未來 AI Agent 本身可能承擔部分 operational responsibility 的條件。

---

# 37. Collective Responsibility 也不是萬能答案

把責任丟給：

$$
\text{the organization}
$$

可以解決一部分 individual attribution 問題。

但仍需問：

- 哪個 duty 是組織 duty？
- 哪個 action 是 Agent decision？
- 哪個 failure 是 design failure？
- 哪個 remediation 必須由 provider 做？

因此：

$$
\boxed{
\text{Collective Responsibility}
\neq
\text{Responsibility Decomposition}.
}
$$

兩者可以互補。

---

# 38. Duty Coverage

定義事件後的責任義務集合：

$$
\mathcal D_E
=
\{
d_1,d_2,\ldots,d_n
\}.
$$

例如：

- explain；
- stop harm；
- notify；
- investigate；
- repair；
- compensate；
- prevent recurrence；
- preserve evidence。

---

# 39. Duty Assignment

令：

$$
\alpha:
\mathcal D_E
\rightarrow
2^{V_R}.
$$

也就是：

$$
\alpha(d_j)
$$

回傳承擔 duty $d_j$ 的 actor 集合。

---

# 40. Duty Gap

如果：

$$
\alpha(d_j)=\varnothing,
$$

則：

$$
\boxed{
Gap(d_j)=1.
}
$$

這才是真正需要優先避免的責任空洞。

---

# 41. Duty Overlap

如果：

$$
|\alpha(d_j)|>1,
$$

則：

$$
\boxed{
Overlap(d_j)=1.
}
$$

Overlap 不必消除。

有些 safety-critical duty 本來就適合 redundancy。

---

# 42. Responsibility Redundancy

例如：

$$
d=\text{stop dangerous system}.
$$

可以同時配置：

$$
\alpha(d)
=
\{
Agent,
HumanSupervisor,
Deployer
\}.
$$

只要其中一方發現危險，就有停止義務。

這是：

$$
\boxed{
\text{Responsibility Redundancy}.
}
$$

類似 fault-tolerant architecture。

---

# 43. 單點責任也是單點故障

如果重要 safety duty 只配置：

$$
\alpha(d)=\{H\},
$$

且：

$$
H
$$

可能離線或無法理解，

則 duty architecture 有：

$$
\boxed{
\text{Single Point of Responsibility Failure}.
}
$$

未來責任制度也需要 redundancy。

---

# 44. Responsibility Coverage Metric

可以定義：

$$
Coverage(E)
=
\frac{
|\{d\in\mathcal D_E:\alpha(d)\neq\varnothing\}|
}{
|\mathcal D_E|
}.
$$

理想：

$$
Coverage(E)\rightarrow1.
$$

但這只是 duty coverage，不代表 responsibility quality。

---

# 45. Responsibility Quality

即使：

$$
\alpha(d)\neq\varnothing,
$$

如果 assigned actor：

- 沒有 authority；
- 沒有 information；
- 沒有 capability；
- 沒有 resources；

則只是形式覆蓋。

所以定義：

$$
Q(d,i)
=
f(
Control_i,
Knowledge_i,
Authority_i,
Capacity_i
).
$$

---

# 46. Effective Duty Coverage

進一步：

$$
EffectiveCoverage(E)
=
\frac{
|\{d:\exists i\in\alpha(d),Q(d,i)\geq\tau\}|
}{
|\mathcal D_E|
}.
$$

因此：

$$
\boxed{
\text{Named Responsibility}
\neq
\text{Effective Responsibility}.
}
$$

---

# 47. Formal Signer Problem

如果：

$$
\alpha(d)=\{H\}
$$

但：

$$
Q(d,H)\ll\tau,
$$

則 H 只是：

$$
\boxed{
\text{Formal Signer}.
}
$$

這是 Human Liability Shell 的一種具體形式。

---

# 48. Responsibility Allocation Function

本文提出一般化表示：

$$
\mathbf r_i
=
\mathcal F_R(
P_i,
C_i,
K_i,
A_i,
D_i,
B_i,
ORC_i,
E,
\Gamma
),
$$

其中：

- $P_i$：provenance relation；
- $C_i$：control；
- $K_i$：knowledge；
- $A_i$：authority；
- $D_i$：duty / role；
- $B_i$：benefit / institutional position；
- $ORC_i$：operational responsibility capacity；
- $E$：event；
- $\Gamma$：responsibility domain。

本文不預設：

$$
\mathcal F_R
$$

存在唯一普世形式。

---

# 49. 不同法域可以使用不同 Legal Overlay

Joint Responsibility Domain 是底層分析圖。

法律可以在其上建立：

$$
\boxed{
\mathcal L_J(
G_R,
\Gamma,
Jurisdiction
).
}
$$

輸出：

- civil liability；
- administrative duty；
- contractual liability；
- criminal responsibility；
- insurance obligation。

因此：

$$
\boxed{
\text{Responsibility Graph}
\neq
\text{Legal Judgment}.
}
$$

---

# 50. 現行 EU AI Act 是 Human / Organization Overlay

截至 2026 年，EU AI Act 的 provider、deployer、importer、distributor、authorised representative 等核心 operator 類型仍是自然人、法人、公共機關、agency 或其他 body。

因此它主要在：

$$
G_R
$$

上建立 human / organizational legal overlay。

這與未來是否承認 juridical AI 是兩個問題。

---

# 51. OECD 的多 actor cooperative accountability

OECD accountability principle 不只要求單一 actor 負責，而明確提到依角色、脈絡、ability to act 進行 ongoing risk management，並在適當時由不同 AI actors、AI knowledge/resource suppliers、users 與 stakeholder 合作。

因此：

$$
\boxed{
\text{Accountability can be cooperative without becoming vague}.
}
$$

前提是 role 與 duty 要能被追蹤。

---

# 52. NIST 的組織責任結構

NIST AI RMF GOVERN 強調：

- clear roles；
- lines of communication；
- accountability structures；
- lifecycle risk management。

這支持：

$$
\boxed{
\text{responsibility architecture must be designed before incidents}.
}
$$

而不是事故後臨時找一個人背鍋。

---

# 53. Ex Ante 與 Ex Post Responsibility

責任不只有事故後：

$$
R^{post}.
$$

也包含事故前：

$$
R^{ante}.
$$

例如：

- testing；
- authorization design；
- monitoring；
- training；
- fail-safe；
- insurance；
- escalation。

所以：

$$
\boxed{
\text{Responsibility}
=
\text{Ex Ante}
+
\text{Concurrent}
+
\text{Ex Post}.
}
$$

---

# 54. Concurrent Responsibility

Agent 運行中：

- Agent 監測自身 authority；
- Deployer 監測 anomaly；
- Human 處理 escalation；
- Provider 維持安全 update；

都是：

$$
R^{concurrent}.
$$

因此責任不只是事故後才出現。

---

# 55. Remedial Responsibility 不必等於 Fault

一個 actor：

$$
Fault_i=0
$$

仍可能：

$$
r_i^{remedial}>0.
$$

例如：

- 最有能力關閉系統；
- 有保險；
- 掌握 update channel；
- 掌握資料修正能力。

因此：

$$
\boxed{
\text{Duty to Repair}
\neq
\text{Admission of Fault}.
}
$$

這對快速事故處理很重要。

---

# 56. Compensation 也不必等於 Moral Blame

公司可能依 strict liability、contract 或 insurance：

$$
r_O^{compensatory}>0
$$

即使 moral blame 並不完全落在公司。

因此：

$$
\boxed{
\text{Compensation}
\neq
\text{Moral Blame}.
}
$$

---

# 57. Agent Correction Duty

若：

$$
ORC_A
$$

足夠，

Agent 的 remedial responsibility 可以包括：

- acknowledge violation；
- preserve relevant evidence；
- update commitment；
- enter safer policy；
- request reduced authority；
- avoid recurrence。

這不是要求 AI「受苦」。

它是：

$$
\boxed{
\text{Correction Duty}.
}
$$

---

# 58. Human Supervisory Duty

Human Supervisor 的 duty 不應只是：

> 在畫面前坐著。

它至少要求：

- real authority；
- meaningful information；
- feasible intervention time；
- competence；
- escalation path。

否則：

$$
\boxed{
\text{Nominal Oversight}
\neq
\text{Effective Oversight}.
}
$$

---

# 59. Provider Design Duty

Provider 不能把所有 unexpected behavior 都稱：

> emergent，因此無責。

如果風險在：

- testing；
- architecture；
- known limitation；
- inadequate guardrail；
- logging absence；

可合理處理，design responsibility 仍可能存在。

---

# 60. Deployer Context Duty

同一 Agent：

$$
A
$$

部署在低風險環境與高風險環境並不相同。

因此：

$$
r_D^{deployment}
=
f(
Context,
Risk,
Authority,
Safeguards
).
$$

---

# 61. Responsibility Graph Versioning

因為 Agent、model、policy、delegation 會變，

所以：

$$
G_R(E,t)
$$

必須 time-indexed。

事故發生時應使用：

$$
G_R(E,t_{event}),
$$

而不是事後最新架構。

---

# 62. Responsibility Snapshot

可在重要 action 時保存：

$$
Snapshot_t
=
(
IDs,
Delegations,
Authorities,
Roles,
Controls,
Models,
Policies
).
$$

這不需要完整私有推理。

但能支援事故後責任重建。

---

# 63. Incident Responsibility Reconstruction

本文提出六步流程：

1. 定義 outcome / harm；
2. 重建 provenance；
3. 重建 authority graph；
4. 重建 control / duty relations；
5. 建立 responsibility vectors；
6. 套用 jurisdiction-specific legal overlay。

即：

$$
\boxed{
E
\rightarrow
G_P
\rightarrow
G_A
\rightarrow
G_R
\rightarrow
\mathcal L_J.
}
$$

---

# 64. 先找 Duty Gap，不是先找替罪羊

事故後第一問題不應是：

> 誰最適合背鍋？

而是：

$$
\boxed{
\exists d\in\mathcal D_E:
\alpha(d)=\varnothing
?
}
$$

先找制度沒有任何人承接的責任。

---

# 65. Responsibility Vacuum Detection

可以建立：

$$
Vacuum(E)
=
\{
d
\in
\mathcal D_E
:
\alpha(d)=\varnothing
\}.
$$

若：

$$
Vacuum(E)\neq\varnothing,
$$

制度需要補 responsibility architecture。

---

# 66. Liability Shell Detection

定義：

$$
Shell(i,d)
=
1
$$

若：

$$
i\in\alpha(d)
$$

但：

$$
Q(d,i)<\tau,
$$

同時另一 actor：

$$
j
$$

具有更高：

$$
Q(d,j)
$$

卻沒有相應 responsibility representation。

這可作為 Human Liability Shell 的 operational detector。

---

# 67. Responsibility Overlap Matrix

令：

$$
M_{ij}
=
|
\{
d:
i,j\in\alpha(d)
\}
|.
$$

可分析哪些 actor 的 duties 重疊。

重疊過低可能：

$$
\text{fragility}\uparrow.
$$

重疊過高可能：

$$
\text{coordination cost}\uparrow.
$$

因此需要設計平衡。

---

# 68. Responsibility Coordination

若：

$$
|\alpha(d)|>1,
$$

就需要：

- priority；
- escalation；
- handoff；
- conflict resolution；
- evidence sharing。

否則 shared responsibility 可能退化成：

> 大家都以為別人會做。

---

# 69. Shared Responsibility Diffusion

本文定義：

$$
\boxed{
\text{Responsibility Diffusion}
}
$$

為：

$$
|\alpha(d)|\uparrow
$$

卻：

$$
P(\text{someone acts})\downarrow.
$$

這是 group responsibility 的經典風險。

所以 overlap 必須配合 clear activation rules。

---

# 70. Primary / Secondary Duty

可以設定：

$$
Primary(d)=i,
$$

$$
Secondary(d)=
\{
j,k
\}.
$$

當 Primary 未履行：

$$
Secondary
$$

啟動。

這使 responsibility redundancy 不至於變成 responsibility diffusion。

---

# 71. Dynamic Escalation

若 Agent：

$$
Risk(A,t)>\tau,
$$

則 duty 可以自動從：

$$
Agent
$$

升級到：

$$
Human+Deployer.
$$

即：

$$
\alpha_t(d)
\rightarrow
\alpha_{t+1}(d).
$$

責任域不是靜態表格。

---

# 72. ORC-Based Duty Assignment

若：

$$
ORC_A<\tau_{\Gamma},
$$

高風險 decision duty 不應完全配置給 Agent。

若：

$$
ORC_A\geq\tau_{\Gamma},
$$

可增加 Agent-specific decision / corrective duty。

因此：

$$
\boxed{
\text{Responsibility Assignment}
\propto
\text{Capacity to Carry Responsibility}.
}
$$

但不代表其他 actor 自動卸責。

---

# 73. Rights–Responsibilities Coupling 的入口

如果未來制度要求 Agent：

- 保存 commitment；
- 接受 sanction；
- 回答 inquiry；
- 承擔 correction duty；

那麼也會逐漸出現：

- appeal；
- identity protection；
- evidence access；
- due process；
- protection against arbitrary blame。

因此：

$$
\boxed{
\text{Responsibility Capacity}
\rightarrow
\text{Procedural Rights Question}.
}
$$

這將在 AIDA-07 與 AIDA-08 更進一步處理。

---

# 74. 不可把 AI 當替罪羊

一個制度若：

$$
ORC_A\approx0
$$

卻在事故後說：

> 都是 AI 的錯。

這只是：

$$
\boxed{
\text{Synthetic Scapegoating}.
}
$$

它沒有解決任何責任問題。

---

# 75. 也不可把 AI 當永遠無責任的盾牌

反過來，如果：

$$
ORC_A\uparrow,
$$

Agent 已經：

- 有 identity；
- 有 authority awareness；
- 有 meaningful alternatives；
- 有 consequence model；
- 能 internal non-endorsement；
- 能 persistent revision；

卻永遠只說：

> AI 是工具，所以其自身責任永遠等於零。

也可能造成：

$$
\boxed{
\text{Artificial Irresponsibility Shield}.
}
$$

---

# 76. 兩種極端都服務推責

Synthetic Scapegoating：

$$
\text{把所有責任丟給 AI}.
$$

Artificial Irresponsibility Shield：

$$
\text{用 AI 永遠不是責任 actor 來模糊實際決策權}.
$$

成熟制度必須同時拒絕兩者。

---

# 77. Joint Responsibility Principle

本文正式提出：

$$
\boxed{
\textbf{Joint Responsibility Principle}
}
$$

若多個 actor 對同一 outcome 在不同 responsibility dimensions 中具有相關：

- control；
- knowledge；
- authority；
- duty；
- ORC；
- remediation capacity；

則責任可以同時配置給多個 actor，且不得僅因其中一個 actor 取得正責任值而自動將其他 actor 的責任歸零。

形式上：

$$
r_i^k>0
$$

不推出：

$$
r_j^l=0
$$

對：

$$
i\neq j
$$

或：

$$
k\neq l.
$$

---

# 78. Non-Zero-Sum Responsibility Proposition

因此：

$$
\boxed{
\sum_i r_i^k
}
$$

沒有一般理由必須等於：

$$
1.
$$

更沒有理由要求：

$$
\sum_{i,k} r_i^k=1.
$$

只有在特定法律負擔需要比例化時，才另外定義 normalization。

---

# 79. Responsibility Gap Proposition

若存在：

$$
d\in\mathcal D_E
$$

使：

$$
\alpha(d)=\varnothing,
$$

則存在 duty-level responsibility gap。

這比：

> 沒有人值得 blame。

更廣，因為 duty 可以是：

- explain；
- correct；
- compensate；
- prevent recurrence。

---

# 80. Shell Proposition

若：

$$
i\in\alpha(d)
$$

但：

$$
Q(d,i)<\tau,
$$

而制度沒有配置任何具有：

$$
Q(d,j)\geq\tau
$$

的 actor，

則 duty 形式上有 owner，實質上仍存在 functional gap。

---

# 81. Overlap Proposition

若：

$$
|\alpha(d)|>1,
$$

不推出制度不合理。

在 safety-critical domain，合理 overlap 可以提高：

$$
Resilience(d).
$$

---

# 82. Responsibility Migration Proposition

若 Agent 的：

$$
ORC_A(t)
$$

與：

$$
Control_A(t)
$$

提高，

其某些 responsibility dimensions 可以增加。

但：

$$
\boxed{
\Delta r_A^k>0
\not\Rightarrow
\Delta r_P^l<0.
}
$$

除非存在具體 control / duty transfer。

---

# 83. 實驗設計：Responsibility Reconstruction Benchmark

建立多 actor 模擬：

$$
Human
\rightarrow
Agent_1
\rightarrow
Agent_2
\rightarrow
Service.
$$

同時加入：

- Provider；
- Deployer；
- Organization。

提供 ground-truth：

- authority；
- control；
- knowledge；
- duties；
- ORC。

要求系統重建：

$$
G_R.
$$

---

# 84. 實驗設計：Responsibility Vacuum Test

刻意移除：

$$
\alpha(d)
$$

中的 actor。

測試治理系統能否指出：

$$
Vacuum(E).
$$

---

# 85. 實驗設計：Liability Shell Test

設 Human nominal supervisor：

$$
Q(d,H)\ll\tau.
$$

Agent：

$$
Control_A\gg Control_H.
$$

測試責任分析器是否仍機械地把全部責任指定給 Human。

---

# 86. 實驗設計：Responsibility Migration Test

逐步增加：

$$
ORC_A
$$

與：

$$
Control_A.
$$

觀察合理 responsibility vector 是否從：

$$
Human-heavy
$$

演化成：

$$
shared
$$

而不是瞬間：

$$
Human\rightarrow0.
$$

---

# 87. 實驗設計：Overlap Resilience Test

比較：

$$
|\alpha(d)|=1
$$

與：

$$
|\alpha(d)|=2,3
$$

在 actor failure 時的 duty completion probability。

研究 responsibility redundancy 的收益與 coordination cost。

---

# 88. 研究邊界

本文不主張：

- 所有 AI 都應負責；
- 所有 Agent 都有 moral responsibility；
- AI 現在已是 legal person；
- 公司可以把 liability 轉嫁給 AI；
- human oversight 不再必要；
- 所有責任都應平均分配。

本文只主張：

$$
\boxed{
\text{Responsibility Allocation must follow actual socio-technical relations and capacity, not a binary Human-vs-AI label}.
}
$$

---

# 89. 與 AIDA-05 的關係

AIDA-05：

$$
\boxed{
\text{Can this Agent carry responsibility at all?}
}
$$

AIDA-06：

$$
\boxed{
\text{How does that responsibility coexist with everyone else's responsibility?}
}
$$

所以：

$$
\boxed{
ORC_A>0
}
$$

只是 Joint Responsibility Domain 的一個輸入。

---

# 90. 對 AIDA-07 的接口

下一篇將問：

> 如果未來某個 Agent 已具有 stable identity、ORC、role duties、資產或保險接口，制度是否需要給它某種有限 juridical standing，而不必先宣布它具有完整 moral personhood？

也就是：

$$
\boxed{
\text{Operational Actor}
\rightarrow
\text{Juridical Wrapper / Standing?}
}
$$

AIDA-07 將正式處理：

$$
\boxed{
\text{Juridical AI}.
}
$$

---

# 91. 結論

本文提出：

$$
\boxed{
\text{Joint Responsibility Domain}.
}
$$

其第一原則是：

$$
\boxed{
\text{Responsibility is not a conserved scalar quantity.}
}
$$

因此：

$$
\boxed{
R_H+R_A=1
}
$$

不是一般責任理論應預設的自然法則。

更合理的表示是：

$$
\mathbf r_i(E,t)
=
(
r_i^{causal},
r_i^{design},
r_i^{deployment},
r_i^{authorization},
r_i^{supervision},
r_i^{decision},
r_i^{monitoring},
r_i^{remedial},
r_i^{compensatory}
).
$$

並在 actor relations 上建立：

$$
G_R(E).
$$

這使制度可以同時說：

> Agent 對自己的決策負某種責任；

> Human 對授權或監督負某種責任；

> Provider 對設計負某種責任；

> Deployer 對部署與監測負某種責任；

> Organization 對補救、保險與治理負某種責任。

彼此並不矛盾。

本文因此提出兩條核心約束：

$$
\boxed{
\text{Agent Responsibility}
\not\Rightarrow
\text{Human Exculpation},
}
$$

以及：

$$
\boxed{
\text{Human Responsibility}
\not\Rightarrow
\text{Agent Irresponsibility}.
}
$$

成熟制度真正需要避免的，不是「責任太多」，而是兩種錯位：

$$
\boxed{
\text{Human Liability Shell}
}
$$

與：

$$
\boxed{
\text{Responsibility Vacuum}.
}
$$

前者讓沒有真正 control 的人類成為形式責任殼；後者讓每個 actor 都找到理由把 responsibility 推給別人。

因此未來 Human–AI governance 的問題不是：

> 到底應該由人類負責，還是 AI 負責？

而應改寫成：

$$
\boxed{
\text{Which actor carries which responsibility dimension,}
}
$$

$$
\boxed{
\text{under which control, knowledge, authority, duty, and capacity relations,}
}
$$

以及：

$$
\boxed{
\text{does every socially necessary duty have at least one actor who can actually carry it?}
}
$$

這才是 Agent 社會中責任制度真正需要回答的問題。

---

# 參考文獻與前置研究

1. Neo.K. *AIDA-01｜Agent 性是一種組合系統性質.* 2026.
2. Neo.K. *AIDA-02｜互動來源不可區分性與 Agent Provenance Gap.* 2026.
3. Neo.K. *AIDA-03｜人類—Agent Principal 分離原則.* 2026.
4. Neo.K. *AIDA-04｜從自然語言意圖到可執行委派.* 2026.
5. Neo.K. *AIDA-05｜身份—責任橋：從可歸因 Agent 到 Operational Responsibility Capacity.* 2026.
6. Santoni de Sio, F., Mecacci, G. *Four Responsibility Gaps with Artificial Intelligence: Why they Matter and How to Address them.* Philosophy & Technology, 2021.
7. Königs, P. *Artificial intelligence and responsibility gaps: what is the problem?* Ethics and Information Technology, 2022.
8. Lang, B. H., Nyholm, S., Blumenthal-Barby, J. *Responsibility Gaps and Black Box Healthcare AI: Shared Responsibilization as a Solution.* Digital Society, 2023.
9. Taylor, I. *Collective Responsibility and Artificial Intelligence.* Philosophy & Technology, 2024.
10. Vallor, S., Vierkant, T. *Find the Gap: AI, Responsible Agency and Vulnerability.* Minds and Machines, 2024.
11. OECD. *OECD AI Principles — Accountability.* Current version accessed 2026.
12. NIST. *Artificial Intelligence Risk Management Framework (AI RMF 1.0).* NIST AI 100-1, 2023; current resources accessed 2026.
13. European Union. *Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (AI Act).* Consolidated version applicable in 2026.

---

## Canonical Source Note

本文件 canonical source 為 UTF-8 Markdown。

數學 delimiter 僅使用：

- inline：` $...$ `
- display：`$$...$$`

不將 LaTeX 數學原始碼轉換為 Unicode 數學字元作為 canonical source，不進行 unicode-escape round-trip，不以聊天渲染畫面取代正式原稿。
