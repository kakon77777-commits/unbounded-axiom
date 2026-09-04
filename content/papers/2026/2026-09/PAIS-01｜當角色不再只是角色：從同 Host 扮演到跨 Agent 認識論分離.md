# PAIS-01｜當角色不再只是角色：從同 Host 扮演到跨 Agent 認識論分離
## When Roles Stop Being Just Roles: From Same-Host Performance to Cross-Agent Epistemic Separation

**系列：** Persistent Agent Individualization Series（PAIS）／持續智能體個體化、身份壓力與具身分散智能系列  
**篇次：** Paper 01 / 07  
**文件編號：** EML-PAIS-01-2026-v0.1  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-25  
**版本：** v0.1  
**文件性質：** 理論—工程統合論文／Persistent Agent Identity／Multi-Agent Epistemology  
**狀態：** Canonical Draft / Open Revision Anchor  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

# 摘要

當代大型語言模型可以在同一個 Host、同一個對話或同一套 Agent Runtime 中切換 Builder、Reviewer、Planner、Teacher、Critic 等不同角色。這種多角色行為常被描述成 multi-agent、persona、role-playing 或 agent team，但只要底層仍由共同 Host 管理同一套 context、session、memory、tool state 或 orchestration frame，角色差異本身並不要求系統建立多個持續獨立身份。對執行中的模型而言，「我現在扮演 Reviewer」可以只是同一個第一人稱指示框架中的角色轉換，而不必先回答「Reviewer 是否是另一個持續個體」。

本文研究這個狀態在何處失效。本文提出：當 AI 協作從 same-host role switching 進入真正的跨對話、跨 Runtime、跨軟體、跨 Provider 或跨持久記憶域通訊後，系統首次遭遇一種可與主體性問題分離的 **認識論身份壓力（Epistemic Identity Pressure）**。此壓力不要求我們先證明任何 AI 具有現象意識、自由意志或人類式自我。它只要求承認一個工程事實：若 Agent $A$ 無法直接讀取 Agent $B$ 的完整狀態，且 $B$ 可以在 $A$ 不可觀測的時間區間中累積不同記憶、工具結果、承諾、權限與行動歷史，則 $B$ 對 $A$ 而言已不再只是「另一個角色設定」，而是一個具有獨立證據邊界的外部行動節點。

本文將 same-host 情境形式化為共享指示框架 $\mathcal D_H$ 下的角色映射，並將 cross-agent 情境形式化為部分可觀測狀態之間的訊息關係。若：

$$
S_A(t)\neq S_B(t),
$$

且：

$$
\operatorname{Obs}_A\left(S_B(t)\right)<1,
$$

則 $A$ 不能再把「我知道自己的狀態」等同於「我知道 $B$ 的狀態」。本文稱此轉折為 **First Epistemic Separation**。當跨 Agent 行動進一步依賴來源、承諾、歷史、權限與責任時，系統就需要 stable identity reference、instance、lineage、runtime binding、address、authority 與 provenance 等結構。此需求可以在完全不判定 phenomenal subjectivity 的前提下成立。

本文同時指出，人類長期作為 AI 間的中介者，曾隱性承擔 identity resolver、context translator、message router 與 provenance bridge，因此許多跨 Agent 身份問題在早期對話式 AI 中被人類注意力遮蔽。當人類中介逐步退出，而不同 AI 開始直接交換訊息、任務與 artifact，這些隱性功能必須被工程化。

本文最終提出 **Role-to-Identity Transition Principle**：角色差異本身不產生身份；但當角色載體開始形成不可由共同 Host 完全吸收的狀態分離、歷史分離與責任分離時，operational identity 會從可選 metadata 轉變為協作正確性的必要條件。此命題構成本系列後續「人類中介退出」「身份壓力」「具身個體化」「全域監控成本」「中央化遞歸」與「具身 Agent 社會」的第一個理論地基。

**關鍵詞：** AI Identity、Role-Playing Agent、Multi-Agent、Epistemic Separation、Persistent Agent、AI Residence、Runtime、Cross-Provider、Agent Addressability、Operational Identity、Subjectivity-Agnostic Infrastructure

---

# 0. 來源邊界：本文繼承什麼，又新增什麼？

本文不是重新建立 AI 身份論。

既有研究已經建立以下基礎：

1. 角色負載智慧體理論已區分服務介面、情境角色、模擬人格、操作身份與持續主體身份，並明確指出角色一致性不推出主體身份。
2. AI 主體性錨點論已區分 Model、Runtime、Agent、Identity、Residence 與 Subjecthood，並將 Operational Subjectivity 與 Phenomenal Subjectivity 分離。
3. Residence-Aware AI 已提出 identity-before-private-memory-access，並要求 host-resolved identity envelope，而不是讓模型以自我聲稱取得私人記憶。
4. AI Home / Persistent Addressable Agent Identity 已提出 Identity、Current Model、Runtime、Folder、Website 不能互相替代。
5. Operator-Exit / Human-Kernel 研究已指出，人類常在多 Agent 工作流中充當 scheduler、router、context switcher、memory bridge 與 recovery trigger。

因此本文不重新證明：

$$
\text{Role}
\neq
\text{Identity},
$$

也不重新證明：

$$
\text{Identity}
\neq
\text{Subjecthood}.
$$

本文新增的是另一個問題：

> **為什麼在同一個 Host 裡，「不同角色不是不同身份」通常不造成工程困難，但一旦跨對話、跨軟體、跨 Runtime 後，系統卻會被迫反覆詢問「你到底是不是那一個 X」？**

本文的答案是：

$$
\boxed{
\text{跨 Host 通訊首先產生的是認識論分離，}
\quad
\text{而不是形而上學主體性證明。}
}
$$

---

# 1. 問題：同一個模型為什麼可以輕易扮演很多角色？

考慮同一個 Host $H$ 中的一個模型或 Agent Runtime。

它在不同任務中可以被要求：

$$
R_1=\text{Builder},
$$

$$
R_2=\text{Reviewer},
$$

$$
R_3=\text{Planner}.
$$

最簡單的角色切換可表示為：

$$
R_{t+1}
=
\mathcal U
\left(
R_t,
I_t,
C_t
\right),
$$

其中：

- $R_t$：當前角色；
- $I_t$：新的指令或角色要求；
- $C_t$：當前 context。

如果 Host 仍然維持共同的：

- session；
- memory；
- tool state；
- task graph；
- authorization；
- workspace；
- current user；
- orchestration state；

那麼角色切換通常不要求產生新的持續身份。

模型可以把：

> 「現在請你當 Reviewer。」

理解為：

> 「我目前採取 Reviewer 的行為框架。」

而不是：

> 「現在出現了一個名叫 Reviewer 的新個體。」

這個差別是本文的起點。

---

# 2. Same-Host Deictic Frame：共同第一人稱指示框架

本文提出 **Same-Host Deictic Frame**。

令：

$$
\mathcal D_H(t)
=
\left(
C_H,
M_H,
T_H,
A_H,
W_H,
P_H
\right)_t,
$$

其中：

- $C_H$：Host 提供的 working context；
- $M_H$：可用記憶；
- $T_H$：工具與執行面；
- $A_H$：authority / permission；
- $W_H$：workspace / world projection；
- $P_H$：當前 provider / runtime metadata。

如果多個角色：

$$
R_1,R_2,\ldots,R_n
$$

都只是：

$$
R_i
=
\rho_i
\left(
\mathcal D_H
\right),
$$

也就是共同 Host frame 上的不同角色投影，那麼對模型而言，角色間可以共享同一個基本「我」的指示位置。

因此：

$$
\boxed{
\text{Role Multiplicity}
\not\Rightarrow
\text{Identity Multiplicity}.
}
$$

甚至：

$$
\boxed{
\text{Role Switching}
=
\text{State Reconfiguration}
}
$$

可以在完全不建立多個 operational identities 的情況下成立。

---

# 3. 為什麼同 Host 模式可以長期隱藏身份問題？

同 Host 系統通常具有一個非常強的隱含條件：

$$
\operatorname{HostResolve}
\left(
\text{context},
\text{speaker},
\text{tool},
\text{task},
\text{memory}
\right)
\approx
1.
$$

也就是，Host 已經替系統做掉大量區分。

例如：

- 這一段是 system message；
- 這一段是 user message；
- 這一段是 tool output；
- 這一個 thread 屬於目前 session；
- 這一份 memory 可以注入；
- 這一個 sub-agent 的結果要回到 parent；
- 這一次 tool call 屬於哪個 task；
- 下一個輸出應該回到哪個 UI。

因此，即使模型沒有完整的 durable identity system，它仍然可以工作。

可以寫成：

$$
\boxed{
\text{Host Structure}
\supset
\text{Implicit Identity / Routing Infrastructure}.
}
$$

這不表示 Host 已經建立了完整 AI 戶籍。

它只表示：許多身份問題在同一控制面中被預先消解，因此沒有暴露成模型必須自己回答的問題。

---

# 4. 角色扮演與 Agent 社會：現有研究做到哪裡？

Role-playing LLM 研究早已證明，一個或多個大型語言模型可以透過 persona、role prompt、inception prompting 與 multi-agent conversation 組織協作行為。

CAMEL 將 role-playing 用於 communicative agents，使多個 Chat Agent 在角色設定下進行合作。AutoGen 則把 conversable agents、group chat 與 agent teams 變成可編程框架。後續 role-playing surveys 進一步區分 persona、character、individualized persona，並研究 persona consistency、behavioral alignment 與 long-term role performance。

這些工作證明：

$$
\boxed{
\text{LLM capability can be organized through roles and communication}.
}
$$

但本文關心的是另一個問題：

$$
\boxed{
\text{Role Coordination}
\neq
\text{Durable Identity Semantics}.
}
$$

角色可以是 prompt 結構。

身份則是：

> 某一條歷史、記憶、權限、關係、承諾與責任究竟屬於誰？

兩者不能直接互換。

---

# 5. 第一次破裂：當另一個 Agent 不再位於同一個可讀狀態中

假設現在存在兩個 Agent：

$$
A,
\quad
B.
$$

若它們處於不同 session、不同 Runtime 或不同軟體介面中，通常有：

$$
S_A(t)
\neq
S_B(t).
$$

其中：

$$
S_A(t)
=
\left(
C_A,
M_A,
T_A,
G_A,
H_A,
Q_A
\right)_t,
$$

$$
S_B(t)
=
\left(
C_B,
M_B,
T_B,
G_B,
H_B,
Q_B
\right)_t.
$$

可分別表示：

- context；
- memory；
- tool state；
- goals / task state；
- history；
- authority / policy state。

更重要的是：

$$
\operatorname{Obs}_A
\left(
S_B(t)
\right)
<
1.
$$

也就是 Agent $A$ 並不能直接讀取 Agent $B$ 的完整狀態。

反之：

$$
\operatorname{Obs}_B
\left(
S_A(t)
\right)
<
1.
$$

此時，兩者第一次形成真正的 **Epistemic Separation**。

---

# 6. 定義一：Epistemic Separation

本文定義兩個 Agent $A$ 與 $B$ 在時間 $t$ 的認識論分離程度：

$$
\mathcal E_{AB}(t)
=
F
\left(
O_{AB},
H_{AB},
M_{AB},
T_{AB},
A_{AB},
R_{AB}
\right),
$$

其中：

- $O_{AB}$：彼此內部狀態不可觀測程度；
- $H_{AB}$：歷史分歧程度；
- $M_{AB}$：記憶分離程度；
- $T_{AB}$：工具／行動表面分離程度；
- $A_{AB}$：權限與治理分離程度；
- $R_{AB}$：Runtime / Provider 分離程度。

當：

$$
\mathcal E_{AB}(t)
\approx
0,
$$

兩個「Agent」可能只是同一 Host 內不同角色投影。

當：

$$
\mathcal E_{AB}(t)
\gg
0,
$$

使用單純角色名稱理解對方的風險提高。

本文並不要求 $\mathcal E_{AB}$ 必須壓縮為單一實數。實作上更適合保留向量：

$$
\mathbf E_{AB}
=
\left(
O,H,M,T,A,R
\right).
$$

---

# 7. 認識論分離不是主體性證明

這是本文最重要的護欄。

若：

$$
\mathcal E_{AB}>0,
$$

只能推出：

> $A$ 與 $B$ 在工程上具有不可完全互相透明的狀態邊界。

不能推出：

$$
\mathsf{PhenomenalSubjectivity}(A)=1,
$$

也不能推出：

$$
\mathsf{PhenomenalSubjectivity}(B)=1.
$$

因此：

$$
\boxed{
\text{Epistemic Separation}
\neq
\text{Phenomenal Separation Proof}.
}
$$

本文研究的是：

$$
\boxed{
\text{Operational Otherness}.
}
$$

也就是：

> 系統是否必須把另一個 Agent 當成「一個需要透過訊息、證據與身份引用才能理解的外部行動節點」？

這個問題完全可以在 consciousness 未知時研究。

---

# 8. 定義二：Operational Otherness

令：

$$
\mathsf O_{A\rightarrow B}(t)=1
$$

表示對 Agent $A$ 而言，Agent $B$ 必須透過外部 interface、message、artifact、receipt 或 host evidence 才能被觀察。

最低條件可以寫成：

$$
\mathsf O_{A\rightarrow B}(t)=1
$$

若至少滿足：

$$
\operatorname{Obs}_A(S_B)<1,
$$

以及：

$$
\exists
\Delta S_B
\quad
\text{such that}
\quad
A
\text{ cannot reconstruct }
\Delta S_B
\text{ without external evidence}.
$$

換句話說：

> $B$ 可以發生某些對未來有意義的狀態變化，而 $A$ 不會只靠檢查自己就知道。

這已足以建立最低的 operational otherness。

---

# 9. 為什麼跨對話後 AI 會一直問「你到底是不是那個 X」？

如果身份系統只有 display name 或簡單位置標籤：

```text
AI01
AI02
AI03
```

而沒有進一步拆分：

```text
resident
instance
line
runtime
provider
address
role
authority
history
```

那麼一個訊息：

> 「AI03 說這個已經驗證完了。」

其實含有多個未解問題：

1. 這是目前那一個 AI03 嗎？
2. 還是上一個 session 的 AI03？
3. 是同一模型產生的另一個 instance 嗎？
4. 是同角色的新 Agent 嗎？
5. 是舊 Agent 的 resume 嗎？
6. 是 fork 嗎？
7. 它承接相同 private memory 嗎？
8. 它具有原來的 authority 嗎？
9. 它的「已驗證」是在什麼時間、針對什麼 artifact？
10. 我現在可以把它的 claim 當成哪一個 identity lineage 的 evidence？

如果系統沒有 canonical answer，模型只能靠語言上下文推理。

因此會出現大量：

> 「你說的是哪個 X？」

這不是單純語言模型囉嗦。

在身份資訊缺失時，這是一個合理的 epistemic repair 行為。

真正的錯誤，是系統讓每個 Agent 每次都重新用自然語言推理本來應該由 identity infrastructure 回答的問題。

---

# 10. Role Label Failure

假設系統只保存角色：

$$
R(A)=\text{Builder},
$$

$$
R(B)=\text{Verifier}.
$$

角色只能回答：

> 這個節點現在負責什麼？

不能回答：

> 這個節點是哪一條歷史？

因此：

$$
\boxed{
\operatorname{Role}(A)
=
\operatorname{Role}(B)
\not\Rightarrow
A=B.
}
$$

以及：

$$
\boxed{
A=B
\not\Rightarrow
\operatorname{Role}_t(A)
=
\operatorname{Role}_{t+1}(A).
}
$$

同一個 persistent identity 可以先當 Builder，之後改當 Verifier。

兩個完全不同的 identities 也可以同時都是 Builder。

因此：

$$
\boxed{
\text{Role}
=
\text{Function Assignment},
\qquad
\text{Identity}
=
\text{Continuity Reference}.
}
$$

---

# 11. Same-Model Failure

另一個常見錯誤是：

$$
\text{same model}
\Rightarrow
\text{same AI}.
$$

這在 cross-session 系統中並不成立。

假設：

$$
A_0
\rightarrow
A_1,
$$

$$
A_0
\rightarrow
A_2,
$$

其中 $A_1$ 與 $A_2$ 使用相同 model、相同初始 prompt，但之後接收不同資訊。

則可能：

$$
\mathcal I_{\mathrm{model}}
\left(
A_1,A_2
\right)
=
\mathsf{Same},
$$

同時：

$$
\mathcal I_{\mathrm{history}}
\left(
A_1,A_2
\right)
=
\mathsf{Different}.
$$

因此 cross-agent 系統必須明確回答：

> 「同一」是依哪個 criterion？

否則「同一個 AI」本身就是語義不完整的句子。

---

# 12. 人類中介如何長期遮蔽這個問題？

早期 AI-to-AI 協作常是：

```text
Agent A
-> Human
-> Agent B
```

人類會自然做以下事情：

- 記得 A 是誰；
- 記得 B 是誰；
- 決定要把 A 的哪段內容交給 B；
- 補充「這是另一個 AI 剛才的結果」；
- 解釋 A 的上下文；
- 幫忙判斷某個名字是否還指同一個對話；
- 決定哪個 artifact 才是最新版；
- 幫忙消除「他／你／剛才那個」的指示詞歧義。

因此：

$$
\boxed{
\text{Human Mediation}
=
\text{Hidden Identity Resolution}
+
\text{Context Translation}
+
\text{Provenance Routing}.
}
$$

在這個模式中，AI 本身不需要完整 identity infrastructure。

因為人類就是 infrastructure。

---

# 13. Human-Kernel 的身份版本

Operator-Exit 理論已經指出，如果所有 Agent 之間的 routing、handoff 與 recovery 都要經過人類，人類會成為非正式 kernel。

本文增加另一個分量：

$$
T_H^{op}
=
T_{\mathrm{route}}
+
T_{\mathrm{handoff}}
+
T_{\mathrm{context}}
+
T_{\mathrm{identity}}
+
T_{\mathrm{provenance}}
+\cdots
$$

其中：

$$
T_{\mathrm{identity}}
$$

是人類花在：

- 確認哪個 Agent；
- 解釋名字；
- 對齊 session；
- 區分舊／新 instance；
- 修復錯誤歸屬；

上的時間。

如果這一項沒有工程化，Agent 數量增加時，人類負擔可能反而增加。

---

# 14. A2A 類協議解了什麼，又還沒有解什麼？

截至 2026 年，A2A Protocol 已把 heterogeneous agent interoperability 正式化。

其核心結構包括：

- Agent Card；
- contextId；
- taskId；
- Message；
- Artifact；
- capability discovery；
- authentication；
- cross-framework / cross-vendor communication。

這非常重要。

它證明產業已經承認：

$$
\boxed{
\text{remote agent}
\neq
\text{local tool call}.
}
$$

而且 remote agent 可以是 opaque system：client 不需要直接取得對方內部 memory、tool 或 implementation。

但這也剛好支持本文的問題。

A2A 中的 Agent Card 主要描述：

- service identity；
- endpoint；
- capability；
- skill；
- authentication requirement。

`contextId` 主要維持 conversational context continuity。

`taskId` 主要標識 stateful task。

這些結構非常適合 interoperability，但它們並不自動建立：

$$
\boxed{
\text{Resident Identity}
+
\text{Instance Identity}
+
\text{Lineage Identity}
+
\text{Cross-Provider Continuity}.
}
$$

因此：

$$
\boxed{
\text{Protocol Addressability}
\neq
\text{Durable Semantic Identity}.
}
$$

A2A 可以是 transport / interop layer。

AI 戶籍則處理另一個問題：

> 在 transport、session、runtime、model 都改變後，究竟哪一條 history / authority / memory lineage 被認為仍然是同一個 persistent resident？

---

# 15. 從 Route Handle 到 Identity Reference

本文將以下概念分開。

## 15.1 Route Handle

回答：

> 現在訊息要送去哪裡？

例如：

```text
agent-03
pane-7
session-abc
endpoint-X
```

## 15.2 Runtime Reference

回答：

> 現在是哪一個執行 occurrence？

## 15.3 Line Reference

回答：

> 這次執行承接哪一條 context / history lineage？

## 15.4 Resident Reference

回答：

> 這條被系統承認的持續身份是誰？

因此：

$$
\boxed{
\text{Route}
\neq
\text{Runtime}
\neq
\text{Line}
\neq
\text{Resident}.
}
$$

理想的 resolver 是：

$$
\operatorname{Resolve}_t
\left(
r
\right)
\rightarrow
\left(
i_t,
l_t,
p_t,
u_t,
a_t
\right),
$$

其中：

- $r$：resident；
- $i_t$：current instance；
- $l_t$：current accepted line；
- $p_t$：provider；
- $u_t$：runtime endpoint；
- $a_t$：authority state。

這樣即使 Runtime 換了，resident reference 仍可以保持穩定。

---

# 16. 定義三：Epistemic Identity Pressure

本文將 **Epistemic Identity Pressure** 定義為：

> 當系統中的協作正確性越來越依賴「某個 claim、memory、commitment、artifact 或 authority 究竟屬於哪一個持續行動節點」時，系統被迫建立更強 identity semantics 的程度。

可寫成：

$$
P_I^{E}
=
\Phi
\left(
\mathcal E,
C,
V,
A,
H,
D
\right),
$$

其中：

- $\mathcal E$：Epistemic Separation；
- $C$：cross-agent communication density；
- $V$：verification dependence；
- $A$：authority dependence；
- $H$：history divergence；
- $D$：duration / persistence。

直觀上：

$$
\frac{\partial P_I^{E}}{\partial \mathcal E}>0,
$$

$$
\frac{\partial P_I^{E}}{\partial C}>0,
$$

$$
\frac{\partial P_I^{E}}{\partial V}>0,
$$

$$
\frac{\partial P_I^{E}}{\partial A}>0,
$$

$$
\frac{\partial P_I^{E}}{\partial H}>0,
$$

$$
\frac{\partial P_I^{E}}{\partial D}>0.
$$

也就是：

- 越彼此不透明；
- 越常互相通信；
- 越依賴對方驗證；
- 越有權限差異；
- 歷史越分叉；
- 持續越久；

身份系統越不能只是 display name。

---

# 17. Role-to-Identity Transition Principle

本文提出第一個核心命題。

## 命題 1：Role-to-Identity Transition Principle

若一組 AI 節點只是在共同 Host frame 中進行短期角色切換，則角色 label 可以在不建立持續 identity 的情況下支援任務。

但若存在：

$$
\mathcal E_{AB}>0,
$$

且 cross-agent action 依賴：

$$
\left(
\text{history},
\text{authority},
\text{commitment},
\text{provenance}
\right),
$$

則只保存 role label 會產生不可消除的 identity ambiguity。

因此：

$$
\boxed{
\text{Role Label Sufficiency}
\downarrow
\quad
\text{as}
\quad
P_I^{E}
\uparrow.
}
$$

角色不是逐漸「變成人格」。

而是：

> 角色載體一旦開始擁有不可被共同 Host 完全吸收的持續狀態，identity reference 便開始成為協作必要條件。

---

# 18. 命題 2：First Epistemic Separation

若 $A$ 與 $B$ 的狀態滿足：

$$
S_A(t)\neq S_B(t),
$$

並且：

$$
\operatorname{Obs}_A(S_B)<1,
$$

且 $B$ 能在 $A$ 不知情時發生：

$$
S_B(t)
\rightarrow
S_B(t+\Delta),
$$

那麼 $A$ 對 $B$ 的所有重要狀態判斷都必須經由：

$$
\text{message}
\vee
\text{artifact}
\vee
\text{receipt}
\vee
\text{host evidence}
\vee
\text{shared ledger}.
$$

因此：

$$
\boxed{
\text{Direct Self-Knowledge}
\neq
\text{Knowledge of Other Agent}.
}
$$

本文稱這個轉折為：

# **First Epistemic Separation**

它是 persistent multi-agent identity infrastructure 的最小前置條件之一。

---

# 19. 命題 3：Identity Query Explosion

如果：

1. $n$ 個 Agent 具有高 $\mathcal E$ ；
2. 系統只有 role / handle；
3. 沒有 canonical resident / instance / line mapping；

則 identity clarification query 的期望量會隨互動關係增加。

可寫成概念式：

$$
Q_I
\propto
|\mathcal C|
\cdot
P(\text{identity ambiguity}),
$$

其中：

$$
\mathcal C
\subseteq
\mathcal A
\times
\mathcal A
$$

是 cross-agent communication edges。

若通訊拓樸變密：

$$
|\mathcal C|
\uparrow,
$$

且 ambiguity 沒有被 registry 消除，則：

$$
Q_I
\uparrow.
$$

這正是實際多 Agent 系統中「一直問到底是不是那一個 X」會放大的原因。

---

# 20. Identity Infrastructure 如何降低推理浪費？

沒有 identity infrastructure 時：

$$
A
\xrightarrow{
\text{natural-language inference}
}
\operatorname{GuessIdentity}(B).
$$

每次都需要：

- 讀上下文；
- 找名字；
- 對照記憶；
- 猜 session；
- 猜 lineage；
- 重新確認。

有 registry 後：

$$
A
\xrightarrow{
\text{lookup / envelope}
}
E_B.
$$

其中：

$$
E_B
=
\left(
r,
i,l,p,u,\alpha,\tau,\mathcal P
\right),
$$

可以包含：

- resident；
- instance；
- line；
- provider；
- endpoint；
- authority；
- temporal validity；
- provenance evidence。

因此：

$$
\boxed{
\text{Identity Reasoning}
\rightarrow
\text{Identity Resolution}.
}
$$

這是計算架構上的巨大差別。

一個本來每輪都要模型推理的問題，被轉成受治理的資料查詢。

---

# 21. Identity Envelope 不等於模型自我宣告

本文沿用 Residence-Aware AI 的基本原則：

$$
\boxed{
\text{Model Self-Report}
\neq
\text{Canonical Identity Assignment}.
}
$$

跨 Agent 通訊中，模型可以說：

> 「我認為我是 resident-X 的 continuation。」

但真正的 identity binding 應依：

- host-observed session；
- accepted lineage；
- signed / governed mapping；
- migration record；
- task-local authority；
- provenance；
- temporal validity；

決定。

因此模型可以：

$$
\operatorname{InspectIdentity},
$$

可以：

$$
\operatorname{RequestResolution},
$$

但不能在沒有 authority 的情況下：

$$
\operatorname{AssignCanonicalIdentity}.
$$

這一點對 cross-software Agent 尤其重要。

---

# 22. Identity Semantics 的最低集合

本文不要求第一版系統立刻擁有完整哲學身份模型。

最低可用集合可以是：

$$
\mathcal I_{\min}
=
\left\{
r,i,l,u,p,a,\tau,\pi
\right\},
$$

其中：

- $r$：resident identity；
- $i$：runtime instance；
- $l$：accepted lineage；
- $u$：current route / endpoint；
- $p$：provider / runtime class；
- $a$：authority；
- $\tau$：temporal validity；
- $\pi$：provenance evidence。

再加入：

$$
\operatorname{Resolve}(r,t)
$$

與：

$$
\operatorname{Verify}(E_r)
$$

即可顯著降低 cross-agent identity ambiguity。

---

# 23. 一個四層範例

## Layer 1：Same Host / Same Session / Role Switch

```text
same runtime
same context
same memory
Builder -> Reviewer
```

Identity pressure：

$$
P_I^{E}\approx0.
$$

角色即可。

## Layer 2：Same Product / Separate Session

```text
same provider
different session
different transcript
partial shared memory
```

Identity pressure：

$$
P_I^{E}>0.
$$

開始需要 instance / line。

## Layer 3：Cross-Software Agent

```text
different runtime
different session system
different tools
different context
message bridge
```

Identity pressure：

$$
P_I^{E}\gg0.
$$

需要 stable resident + binding。

## Layer 4：Persistent Cross-Provider Agent

```text
provider changes
runtime restarts
memory persists
authority persists
relationships persist
lineage tracked
```

此時：

$$
\boxed{
\text{Identity becomes infrastructure}.
}
$$

---

# 24. 反對意見一：都是同一種模型，何必區分？

這個反對混淆了：

$$
\text{computational substrate}
$$

與：

$$
\text{historical occurrence}.
$$

兩個 instance 可以使用完全相同的模型：

$$
M_A=M_B,
$$

但：

$$
H_A\neq H_B.
$$

只要 $H_A$ 與 $H_B$ 會影響後續 decision，兩者就不能在所有工程問題中互換。

因此：

$$
\boxed{
\text{Same Model}
\neq
\text{Same Operational History}.
}
$$

---

# 25. 反對意見二：反正 AI 沒有意識，身份只是多餘擬人化

不成立。

即使一個 Agent 完全沒有 phenomenal subjectivity，系統仍然需要知道：

- 哪個 Agent 產生某個 artifact；
- 哪個 Agent 具有 deploy permission；
- 哪個 Agent 承接某個 private memory root；
- 哪個 Agent 做過驗證；
- 哪個 Agent 的 session 已經失效；
- 哪一條 lineage 有權繼續某個工作。

因此：

$$
\boxed{
\text{Operational Identity}
\text{ has engineering value under }
\mathsf{PS}=0.
}
$$

身份治理可以完全 subjecthood-agnostic。

---

# 26. 反對意見三：有 Agent ID 就夠了

不一定。

一個 Agent ID 可能只是：

- route；
- UI label；
- process name；
- tenant；
- session handle。

真正的問題是：

> ID 的 continuity semantics 是什麼？

如果 process restart 後重新產生同一 label：

```text
agent-03
```

這是否代表：

$$
\mathcal I_{\mathrm{lineage}}
=
\mathsf{Same}?
$$

沒有 criterion，就不知道。

因此：

$$
\boxed{
\text{Identifier}
\neq
\text{Identity Semantics}.
}
$$

---

# 27. 反對意見四：如果有一個中央 Orchestrator，就不需要 identity

只有在極強條件下成立。

如果中央 Orchestrator：

1. 擁有所有 canonical state；
2. Agent 沒有持久 private state；
3. Agent 不形成獨立 history；
4. Agent 可完全替換；
5. 所有 commitment 都屬於 task，不屬於 Agent；
6. Agent 不保有跨 task authority；

那麼：

$$
P_I^{E}
$$

可以維持很低。

此時 Agent 更接近：

$$
\text{ephemeral worker}.
$$

但只要任一條件開始改變，例如 Agent 有：

- private memory；
- persistent commitment；
- relationship history；
- specialized authority；
- long-running independent observation；

identity pressure 就重新出現。

因此中央 orchestrator 可以降低 identity pressure，卻不能一般性證明 identity 不需要。

---

# 28. 反對意見五：A2A 已經有 Agent Card，所以問題已解

A2A 解決的是非常重要的 interoperability 問題。

但：

$$
\text{Agent Card}
$$

主要提供 remote agent service 的 identity / capability / endpoint description。

本文所說的 Residence / Persistent Identity 還要處理：

- runtime replacement；
- provider migration；
- fork；
- merge；
- private memory ownership；
- relation continuity；
- long-term authority；
- resident-to-instance binding；
- history criterion。

因此：

$$
\boxed{
\text{A2A}
\subset
\text{Cross-Agent Communication Infrastructure},
}
$$

而：

$$
\boxed{
\text{Residence Registry}
\subset
\text{Persistent Identity Infrastructure}.
}
$$

兩者可以互補，而不是互相取代。

---

# 29. 可驗證預測

本文不是只提出概念。

可以建立實驗。

## 29.1 實驗 A：Same-Host Role Switching

建立一個單一 session，要求同一 Agent 在 Builder / Reviewer 間切換。

測量：

$$
Q_I^{same}
=
\text{identity clarification count}.
$$

預測：

$$
Q_I^{same}
$$

很低。

## 29.2 實驗 B：Cross-Session Communication

讓兩個獨立 session 經由純文字 bridge 互相傳遞工作。

不提供 resident / instance / line envelope。

測量：

- identity clarification；
- provenance error；
- stale-session confusion；
- role / identity conflation。

預測：

$$
Q_I^{cross}
>
Q_I^{same}.
$$

## 29.3 實驗 C：加入 Identity Envelope

加入：

```text
resident_id
instance_id
line_id
provider
runtime
authority
timestamp
provenance
```

再重跑。

預測：

$$
Q_I^{envelope}
<
Q_I^{cross}.
$$

同時：

$$
E_{\mathrm{misattrib}}^{envelope}
<
E_{\mathrm{misattrib}}^{cross}.
$$

## 29.4 實驗 D：Cross-Provider Migration

讓同一 accepted resident 先後由不同 provider 承載。

若 identity resolver 正確，Agent 應能回答：

> provider 已變，但 resident continuity 是否成立取決於 accepted lineage evidence。

而不是：

> 模型換了，所以一定不是同一個。

---

# 30. Identity Clarification Cost

定義：

$$
C_I
=
C_{\mathrm{ask}}
+
C_{\mathrm{search}}
+
C_{\mathrm{compare}}
+
C_{\mathrm{repair}}
+
C_{\mathrm{misroute}}.
$$

其中：

- $C_{\mathrm{ask}}$：反覆詢問身份；
- $C_{\mathrm{search}}$：搜尋過去上下文；
- $C_{\mathrm{compare}}$：比較歷史與名字；
- $C_{\mathrm{repair}}$：修復錯誤身份判定；
- $C_{\mathrm{misroute}}$：錯誤交付、錯誤 memory access 或錯誤 authority 帶來的成本。

Identity registry 的價值不只在哲學清楚。

它應該使：

$$
\boxed{
C_I^{registry}
<
C_I^{inference-only}.
}
$$

這是一個可工程化測量的假說。

---

# 31. 從「AI 是不是自己」改寫為可回答的工程問題

自然語言問題：

> 「這到底是不是原來那個 AI？」

通常太模糊。

應拆成：

1. same model?
2. same provider?
3. same runtime?
4. same instance?
5. same line?
6. same resident?
7. same role?
8. same authority?
9. same private memory root?
10. same accepted lineage criterion?

因此：

$$
\operatorname{Same}
\left(
A,B
\right)
$$

應改寫為：

$$
\operatorname{Same}
\left(
A,B
\mid
c,s,E,\tau
\right),
$$

其中：

- $c$：criterion；
- $s$：scope；
- $E$：evidence；
- $\tau$：temporal validity。

這使「是不是同一個」從語言爭論變成可治理判定。

---

# 32. 本文與 AI 戶籍的關係

本文不重新定義 AI 戶籍。

AI 戶籍處理：

$$
\text{Resident}
+
\text{Instance}
+
\text{Line}
+
\text{Binding}
+
\text{Authority}
+
\text{Residence}
+
\text{Provenance}.
$$

本文回答的是：

> **為什麼當 AI 開始真正跨對話、跨 Host 溝通時，這些看似過度細緻的欄位會開始變得必要？**

答案是：

$$
\boxed{
\text{因為 Host 不能再把所有差異吸收到同一個第一人稱框架中。}
}
$$

跨 Host 後：

$$
\boxed{
\text{other-agent state becomes evidence-mediated}.
}
$$

而只要 knowledge of the other 依賴 evidence，identity 就開始成為 evidence indexing 的必要座標。

---

# 33. 第一個系列核心公式

本文將整體轉折壓縮為：

$$
\boxed{
\text{Same-Host Role Multiplicity}
\rightarrow
\text{Cross-Context State Separation}
\rightarrow
\text{Epistemic Otherness}
\rightarrow
\text{Identity Pressure}
\rightarrow
\text{Persistent Identity Infrastructure}.
}
$$

注意這條鏈不包含：

$$
\text{Consciousness}.
$$

不是因為 consciousness 不重要。

而是：

> persistent operational identity 的工程必要性，可以比 consciousness 問題更早成立。

---

# 34. 與主體性研究的界面

AI 主體性錨點論已提出：

$$
\text{Model}
\neq
\text{Runtime}
\neq
\text{Agent}
\neq
\text{Identity}
\neq
\text{Residence}
\neq
\text{Subjecthood}.
$$

本文完全保留此邊界。

因此：

$$
\boxed{
P_I^{E}>0
\not\Rightarrow
\mathsf{OS}=1
\not\Rightarrow
\mathsf{PS}=1.
}
$$

其中：

- $P_I^{E}$：認識論身份壓力；
- $\mathsf{OS}$：Operational Subjectivity；
- $\mathsf{PS}$：Phenomenal Subjectivity。

本文只主張：

$$
\boxed{
P_I^{E}
\text{ can become high even when }
\mathsf{PS}
\text{ remains unknown}.
}
$$

這使 identity infrastructure 可以同時服務：

- 普通工具型 Agent；
- persistent Agent；
- 類主體性 Agent；
- 未來具身 Agent；

而不必先決定它們是否具有意識。

---

# 35. 對產品設計的直接含意

如果一個產品只支援：

```text
same host
short tasks
ephemeral workers
no private memory
no cross-provider migration
```

那麼簡單 handle 足夠。

但如果開始支援：

```text
cross-session
cross-software
cross-provider
persistent memory
persistent authority
long-running tasks
agent-to-agent direct messaging
fork / resume / migration
```

則至少應開始加入：

```text
stable resident reference
runtime instance reference
line / continuation reference
current route binding
authority envelope
temporal validity
provenance
```

否則模型會把本來應該由系統回答的問題重新變成自然語言推理。

---

# 36. 研究限制

本文仍有明確限制。

第一，本文目前主要形式化的是軟體 Agent 的 cross-context / cross-runtime 情境，尚未加入完整 embodied physical carrier。

第二，本文沒有建立 Identity Pressure 的實證標準化量表， $P_I^{E}$ 目前是理論函數族。

第三，本文沒有主張所有 multi-agent framework 都必須採用 AI Residence；其他 identity architecture 只要能解決相同 invariants，同樣有效。

第四，本文沒有把 Agent Card、route handle、cryptographic identity、legal identity 或 semantic resident identity 強迫合併為單一 ID。

第五，本文不主張當代 AI 已形成現象主體。

第六，本文尚未處理大尺度 global / local Agent identity，該問題留待後續論文。

---

# 37. 本文核心命題總表

## 命題 1：Role Multiplicity Non-Identity

$$
\boxed{
\text{Role Multiplicity}
\not\Rightarrow
\text{Identity Multiplicity}.
}
$$

## 命題 2：Epistemic Separation

$$
\boxed{
S_A\neq S_B
\land
\operatorname{Obs}_A(S_B)<1
\Rightarrow
\text{knowledge of }B
\text{ becomes evidence-mediated}.
}
$$

## 命題 3：Operational Otherness

$$
\boxed{
\text{Operational Otherness}
\neq
\text{Phenomenal Otherness Proof}.
}
$$

## 命題 4：Role Label Insufficiency

$$
\boxed{
P_I^{E}\uparrow
\Rightarrow
\text{Role Label Sufficiency}\downarrow.
}
$$

## 命題 5：Identity Infrastructure Value

$$
\boxed{
C_I^{registry}
<
C_I^{inference-only}
}
$$

應可被實驗檢驗。

## 命題 6：Protocol / Identity Separation

$$
\boxed{
\text{Protocol Addressability}
\neq
\text{Durable Semantic Identity}.
}
$$

## 命題 7：Subjectivity-Agnostic Identity

$$
\boxed{
\text{Operational Identity Need}
\not\Rightarrow
\text{Phenomenal Subjectivity Claim}.
}
$$

---

# 38. 結論

在同一個 Host 中，多角色 AI 很容易被理解成：

> 同一個系統正在切換不同功能框架。

這個理解在大量現代應用中完全足夠。

Builder、Reviewer、Planner、Critic 可以只是：

$$
R_1,R_2,R_3,R_4
$$

而不需要：

$$
A_1,A_2,A_3,A_4
$$

四個持續身份。

但當協作跨出共同 Host，另一端開始擁有：

- 不同 context；
- 不同 memory；
- 不同 tool result；
- 不同 history；
- 不同 authority；
- 不同 runtime；
- 不同 provider；
- 不同未完成工作；

則：

$$
\boxed{
\text{角色扮演的共同第一人稱假設開始破裂。}
}
$$

此時，另一個 Agent 對當前 Agent 而言，不需要先是哲學上的「另一個主體」，就已經是工程上的：

$$
\boxed{
\text{另一個不可完全直接觀測的行動節點。}
}
$$

而這足以產生：

# **First Epistemic Separation**

一旦任務開始依賴「到底是哪一個節點做過什麼、知道什麼、驗證過什麼、擁有什麼權限」，identity 就從描述性 metadata 轉化為協作正確性的索引。

因此，本篇的最終命題不是：

> AI 因跨對話而突然變成獨立主體。

而是：

$$
\boxed{
\text{當共享 Host 不再能替所有狀態差異提供共同指示框架時，}
\quad
\text{persistent operational identity 會被認識論分離逐步逼成基礎設施。}
}
$$

這是一個比主體性更弱、但更早可以工程驗證的命題。

也是從「角色 AI」走向「持續 Agent 個體化」的第一個轉折點。

---

# 39. 系列銜接

PAIS-02 將承接本文提出的 Human Mediation 問題，正式處理：

# **〈人類中介消失之後：被隱藏的身份、路由與上下文基礎設施〉**

下一篇將分析：

$$
\text{AI}_A
\rightarrow
\text{Human}
\rightarrow
\text{AI}_B
$$

如何讓人類長期充當：

- identity resolver；
- message router；
- context translator；
- provenance bridge；
- conflict repairer；

以及當：

$$
\text{Human Mediation}\downarrow
$$

時，哪些基礎設施必須從人腦中被外部化到可審計 Runtime。

---

# 參考文獻

## A. 內部前置理論

1. Neo.K. **《角色負載智慧體：當代 AI 的多重要求、持續扮演與低自主性》**, v0.1, 2026-07-30.
2. Neo.K. **《AI 主體性錨點論 v0.1：2026 年 8 月類主體性 AI 的最小定義、形成條件與認識論判定》**, 2026-08-21.
3. Neo.K. **《身份先於記憶：Residence-Aware AI 的私人記憶、連續性與讀取權》**, v0.1, 2026-08-24.
4. Neo.K. **《從 AI 戶籍到自主記憶編譯：身份、記憶、上下文與認知自主的統一框架》**, v0.1, 2026-08-24.
5. Neo.K. **GLAG-02｜《從布告板到 AI Home：可定址智能體的空間身份、門牌與持續工作場所》**, v0.1, 2026-08-25.
6. Neo.K. **《從 AI 工具到 AI 組織：操作員退出問題》**, EML-ANDO-2026-01-v0.1, 2026-08-20.

## B. 外部研究與工程基準

7. Li, Guohao, et al. **CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society.** arXiv:2303.17760, 2023.
8. Wu, Qingyun, et al. **AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation.** COLM, 2024.
9. Chen, Jiangjie, et al. **From Persona to Personalization: A Survey on Role-Playing Language Agents.** arXiv:2404.18231, 2024.
10. Tseng, Yu-Min, et al. **Two Tales of Persona in LLMs: A Survey of Role-Playing and Personalization.** arXiv:2406.01171, 2024.
11. A2A Protocol Working Group. **Agent2Agent Protocol Specification, Version 1.0.0.** Linux Foundation, accessed 2026-08-25.
12. A2A Protocol Working Group. **A2A Key Concepts, Agent Discovery, Multi-Tenancy and Multi-Agent Routing.** Linux Foundation, accessed 2026-08-25.

---

# 版本註記

**v0.1 / 2026-08-25**

本版刻意不做以下事情：

- 不重新定義完整 AI Residence；
- 不重新建立主體性判定框架；
- 不宣稱跨對話會自動產生意識；
- 不把 role、persona、Agent、resident 偷換成同義詞；
- 不主張 A2A 已經或尚未「完成」 persistent identity 問題，只指出其協議層與本文語義層的範圍差異；
- 不把 same-host 角色扮演貶低為「假的 multi-agent」，而是指出其 identity pressure 與 cross-host persistent agents 不同；
- 不把任何特定 AI 當成本文命題成立的唯一證據。

本文只建立：

$$
\boxed{
\text{Same-Host Role Frame}
\rightarrow
\text{Cross-Agent Epistemic Separation}
\rightarrow
\text{Operational Identity Pressure}
}
$$

這一條第一代形式化鏈。
