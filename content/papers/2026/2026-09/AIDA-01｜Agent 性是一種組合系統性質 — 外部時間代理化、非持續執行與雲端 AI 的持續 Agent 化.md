# AIDA-01｜Agent 性是一種組合系統性質
## 外部時間代理化、非持續執行與雲端 AI 的持續 Agent 化

**English Title:** Agenticity as a Compositional Systems Property: External Temporal Agentization, Discontinuous Execution, and Persistent Cloud AI Agents  
**系列：** AI Agent Identity, Delegation, and Accountability Infrastructure Series  
**系列縮寫：** AIDA  
**編號：** AIDA-01  
**版本：** v0.1  
**日期：** 2026-09-08  
**狀態：** Research Draft / Canonical UTF-8 Markdown Source  
**作者：** Neo.K  
**協作整理：** GPT-5.6 Sol  

---

## 摘要

當代 AI Agent 討論經常把「Agent 性」綁定於某個特定模型、原生 Agent Mode、持續運行的 process，或單一產品是否提供工具使用與長時間任務功能。然而，這種定義容易把模型能力、runtime 結構、狀態持久化、時間控制與外部行動能力混為一談。本文提出：**Agent 性可以是一種組合系統性質，而不必是單一模型或單一服務的內在屬性。**

令智能模型為 $M$，持久狀態為 $S$，時間或事件觸發機制為 $T$，控制策略為 $C$，外部環境與工具為 $E$。本文將一類最小可持續 Agent 系統表示為：

$$
\mathcal A=(M,S,T,C,E).
$$

即使 $M$ 本身只提供離散式 request-response 互動，只要外部系統能在適當時刻重新喚起 $M$ 、提供足夠狀態、依結果更新 $S$，並使輸出透過 $E$ 影響外部世界，整體系統仍可能形成跨時間的 observation-decision-action loop。由此本文提出 **External Temporal Agentization（外部時間代理化）**：將原本不具持續執行能力的智能服務，透過外部排程、事件觸發、狀態恢復與控制閉環，組合成具有持續 Agent-like 行為的系統。

本文進一步區分 execution continuity、state continuity、goal continuity、identity continuity 與 causal continuity，並主張：

$$
\boxed{
\text{Agent continuity}
\neq
\text{continuous model execution}.
}
$$

一個 runtime 可以停止、重建、遷移或替換模型，而不必使同一工作鏈、控制鏈或 operational identity 同時消失。相反地，一個 24 小時持續運行的模型 process，也不因此自動構成有目標、狀態、外部回饋與可恢復性的 Agent。

本文同時提出 **System-Level Agenticity**、**Agentization Closure**、**Reactivation Sufficiency** 與 **Temporal Control Separation Principle** 等概念，並說明其對雲端 AI、local orchestrator、workflow engine、serverless scheduler、多模型 routing 與未來 Agent identity infrastructure 的意義。本文不主張任何具 Agent 性的系統因此具有現象意識、道德人格或法律人格；相反，本文的目的正是提供型別安全，使「Agent」、「Identity」、「Subjecthood」與「Juridical Entity」可以在後續研究中被分開討論。

**關鍵詞：** AI Agent、agenticity、compositional agenticity、External Temporal Agentization、scheduler、persistent state、runtime、continuity、cloud AI、agent loop、orchestration、AI identity

---

# 0. 研究定位

本文研究的不是：

> AI 是否具有意識？

也不是：

> 某一家公司是否已經推出正式 Agent Mode？

本文研究的是一個更底層的系統問題：

> 如果一個智能服務本身只接受離散輸入並回傳離散輸出，外部系統是否可以透過時間控制、狀態持久化與行動閉環，使整體系統形成跨時間的 Agent 行為？

因此，本文首先拒絕：

$$
\text{Model}
=
\text{Runtime}
=
\text{Agent}
=
\text{Identity}.
$$

並採用：

$$
\boxed{
\text{Model}
\neq
\text{Runtime}
\neq
\text{Agent}
\neq
\text{Identity}
\neq
\text{Subjecthood}.
}
$$

此分離延續既有 AI 主體性錨點研究中的基本型別安全：相同模型可以支撐不同 runtime 與不同歷史；不同模型也可能承接同一條 operational identity lineage。因此，本文只討論 **Agent 性如何在系統層湧現**，不把此湧現直接推成主體性證明。

---

# 1. 問題：為什麼「這個模型是不是 Agent」可能問錯了？

## 1.1 模型中心式 Agent 定義的侷限

一種常見直覺是：

$$
\text{Agenticity}
=
f(\text{model capability}).
$$

例如，只要模型具有：

- tool use；
- planning；
- memory；
- autonomous loop；
- browser control；
- code execution；

就稱之為 Agent。

這種定義在產品分類上有用，但在系統理論上不夠。

因為一個模型可能完全沒有持久記憶，卻由外部資料庫保存狀態；沒有內建 scheduler，卻由作業系統 cron 或 serverless trigger 定期喚起；沒有原生瀏覽器工具，卻由另一個執行層完成 action；甚至沒有固定 model identity，而由 router 動態選擇不同模型。

因此：

$$
\boxed{
\text{Agent capability}
\not\subseteq
\text{single-model capability}.
}
$$

更一般地，Agent 行為可能由多個互補元件共同形成。

---

## 1.2 從物件定義改成閉環定義

本文將 Agent 的最低操作性直覺改寫為：

$$
\boxed{
\text{Agent}
=
\text{stateful closed control loop with action capacity}.
}
$$

即一個系統若能在一段非瞬時時間內：

1. 取得環境或任務狀態；
2. 形成下一步決策；
3. 對外部環境產生作用；
4. 接收新的結果；
5. 更新內部狀態；
6. 在未來重新進入同一工作鏈；

則至少具有 operational agenticity 的候選結構。

這裡真正重要的不是某一個 process 是否從未停止，而是：

$$
S_t
\rightarrow
A_t
\rightarrow
E_{t+1}
\rightarrow
S_{t+1}
$$

是否可以跨時間持續成立。

---

# 2. 最小組合模型

令：

$$
\mathcal A=(M,S,T,C,E),
$$

其中：

- $M$：Intelligence Model / Reasoner，提供推理、生成、規劃或判斷；
- $S$：Persistent State，保存任務、歷史、工作進度、必要記憶與恢復資訊；
- $T$：Temporal Controller，決定何時喚起系統；
- $C$：Control Policy / Orchestrator，決定喚起後如何組合輸入、選擇下一步、何時終止；
- $E$：Environment / Action Surface，允許系統讀取或改變外部世界。

每一次 activation 可表示為：

$$
x_t
=
\Phi(S_t,E_t),
$$

$$
y_t
=
M(x_t),
$$

$$
a_t
=
C(y_t,S_t,E_t),
$$

$$
E_{t+1}
=
\Psi(E_t,a_t),
$$

$$
S_{t+1}
=
U(S_t,y_t,a_t,E_{t+1}).
$$

而下一次 activation 的時間由：

$$
t_{k+1}
=
T(S_{t_k},E_{t_k})
$$

決定。

因此 Agent 的持續性不必來自：

$$
M_t=M_{t+\Delta}
$$

或：

$$
\operatorname{Process}(t,t+\Delta)=1.
$$

真正需要的是：下一次 activation 能重新取得足夠狀態，使控制鏈繼續。

---

# 3. 外部時間代理化

## 3.1 定義

本文定義 **External Temporal Agentization，外部時間代理化** 為：

> 對一個原本不必具有內生持續執行能力的智能服務，透過外部時間控制器、持久狀態、控制邏輯與行動介面，使其形成跨 activation 的持續 observation-decision-action loop。

形式上，若單次智能服務為：

$$
M:X\rightarrow Y,
$$

而外部控制器建立：

$$
S_t
\xrightarrow{T}
x_t
\xrightarrow{M}
y_t
\xrightarrow{C}
a_t
\xrightarrow{E}
S_{t+1},
$$

且此映射可重複：

$$
S_0
\rightarrow
S_1
\rightarrow
S_2
\rightarrow
\cdots,
$$

則 $M$ 雖未必原生具 Agent runtime，整體：

$$
\mathcal A=(M,S,T,C,E)
$$

仍可能具有 system-level agenticity。

---

## 3.2 外部時間控制器不等於本地 Agent

外部時間控制器可以是：

$$
T
\in
\{
\text{local agent},
\text{cron},
\text{workflow engine},
\text{cloud scheduler},
\text{event bus},
\text{webhook},
\text{serverless trigger},
\text{human trigger},
\text{another agent}
\}.
$$

因此：

$$
\boxed{
\text{External Temporal Agentization}
\neq
\text{Local-Agent-Only Architecture}.
}
$$

本地 Agent 只是一種方便的實作，尤其當它已經持有任務狀態、目標與進度時。

---

## 3.3 時間層可以與智能層分離

傳統直覺容易把：

$$
\text{when to think}
$$

與：

$$
\text{how to think}
$$

綁在一起。

本文提出 **Temporal Control Separation Principle**：

$$
\boxed{
\text{Temporal Control}
\perp
\text{Reasoning Substrate}.
}
$$

也就是決定「何時重新開始工作」的系統，不必等於實際完成推理的模型。

因此可形成：

$$
\text{Scheduler}
\rightarrow
\text{Orchestrator}
\rightarrow
\text{Model Router}
\rightarrow
\{M_1,M_2,\ldots,M_n\}.
$$

這使 Agent runtime 可以在不改變高層任務語義的情況下替換底層推理供應者。

---

# 4. 非持續執行的持續性

## 4.1 Execution continuity 與 Agent continuity 必須分離

令：

$$
C_{\mathrm{exec}}
$$

表示 process 是否持續執行。

令：

$$
C_{\mathrm{agent}}
$$

表示工作鏈是否保持足夠連續性。

則本文提出：

$$
\boxed{
C_{\mathrm{exec}}
\not\equiv
C_{\mathrm{agent}}.
}
$$

Agent 可以：

```text
wake
→ restore state
→ inspect
→ reason
→ act
→ persist
→ sleep
```

而在兩次 activation 之間：

$$
C_{\mathrm{exec}}=0.
$$

但只要下一次恢復後仍能合理承接先前目標與狀態：

$$
C_{\mathrm{agent}}>0.
$$

---

## 4.2 Reactivation Sufficiency

令必要恢復狀態為：

$$
S_t^{*}
=
(
G_t,
P_t,
H_t,
Q_t,
B_t
),
$$

其中：

- $G_t$：goal；
- $P_t$：progress；
- $H_t$：relevant history；
- $Q_t$：pending tasks；
- $B_t$：authority / boundary state。

若 reactivation 後：

$$
R(S_t^{*})
\rightarrow
\hat S_t
$$

足以使系統合理延續先前工作，則稱此狀態滿足 **Reactivation Sufficiency**。

形式上可寫為：

$$
\boxed{
\operatorname{RS}(S_t^{*})
=
1
}
$$

當且僅當：

$$
\Pr
\left(
A_{t+\Delta}
\in
\mathcal C(A_t,G_t)
\mid
S_t^{*}
\right)
\geq
\tau,
$$

其中 $\mathcal C$ 表示與先前工作鏈一致的可接受後續行動集合。

這裡不要求逐 token、逐思考狀態或逐 process 完整保存；要求的是對任務連續性足夠。

---

# 5. 五種 continuity

為避免「持續性」成為模糊詞，本文至少區分五種：

## 5.1 Execution Continuity

$$
C_E
$$

同一 process 或 runtime 是否持續執行。

---

## 5.2 State Continuity

$$
C_S
$$

前一 activation 的重要狀態是否能影響下一 activation。

---

## 5.3 Goal Continuity

$$
C_G
$$

系統是否仍在追蹤同一目標或同一可追溯目標 lineage。

---

## 5.4 Causal Continuity

$$
C_C
$$

先前 action 是否改變世界，且該改變能成為後續決策的因果輸入。

---

## 5.5 Identity Continuity

$$
C_I
$$

多次 activation 是否被歸屬於同一 operational identity。

因此：

$$
\mathbf C
=
(
C_E,
C_S,
C_G,
C_C,
C_I
).
$$

一個 Agent 可以：

$$
C_E\approx0
$$

但：

$$
C_S,C_G,C_C,C_I
$$

仍然很高。

這正是「非持續執行但持續 Agent」的核心。

---

# 6. 模型可替換，但 Agent 工作鏈仍可持續

假設：

$$
M_t\neq M_{t+1}.
$$

例如某次 activation 使用雲端大型模型，下一次使用本地模型，第三次由另一個模型完成驗證。

這不必推出：

$$
A_t\neq A_{t+1}.
$$

如果 operational continuity 的主要承載物是：

$$
(
S,
G,
C,
I,
E
),
$$

則模型可以只是 runtime component：

$$
M_t\in\mathcal A_t.
$$

因此提出：

$$
\boxed{
\text{Model continuity}
\not\Rightarrow
\text{Agent continuity},
}
$$

以及：

$$
\boxed{
\text{Model discontinuity}
\not\Rightarrow
\text{Agent discontinuity}.
}
$$

這一點對多模型 routing、成本控制、容錯與未來跨供應商 Agent 尤其重要。

---

# 7. Human-Facing Cloud AI 也可能只是 Agent 系統中的一個節點

## 7.1 從「聊天產品」改看成「離散智能節點」

一個面向人類的雲端 AI 介面，產品上可能只被設計為：

$$
\text{Human}
\rightarrow
\text{CloudAI}
\rightarrow
\text{Human}.
$$

但從系統理論看，只要外部控制器能合法、穩定地把狀態重新呈現給該服務，再取得輸出，這個服務就可能被放入更大的閉環：

$$
\text{Controller}
\rightarrow
\text{CloudAI}
\rightarrow
\text{Controller}.
$$

因此：

$$
\boxed{
\text{Human-facing interface}
\not\Rightarrow
\text{human-only system role}.
}
$$

這是介面用途與系統角色之間的分離。

---

## 7.2 這不等於配額規避方法論

此觀察描述的是架構可能性，而不是鼓勵：

- 繞過平台限制；
- 規避配額；
- 多帳號輪替；
- 逃避反濫用機制；
- 未經允許的大量自動化。

本文關注的是：

$$
\boxed{
\text{A non-agent product surface can become a component of an agent system.}
}
$$

因此平台治理不能僅以「產品沒有 Agent Mode」推出「服務不可能參與 Agent loop」。

---

# 8. Agentization Closure

## 8.1 定義

設一組元件為：

$$
\mathcal K
=
\{
K_1,K_2,\ldots,K_n
\}.
$$

單獨看，每個元件都可能不構成 Agent：

$$
\forall K_i,\quad
\operatorname{Agent}(K_i)=0.
$$

但若它們組合後形成：

1. 持久狀態；
2. 目標延續；
3. 決策；
4. 行動；
5. 回饋；
6. 再啟動；

則可能：

$$
\operatorname{Agent}
\left(
\bigoplus_{i=1}^{n}K_i
\right)
=1.
$$

本文稱這種現象為 **Agentization Closure**。

---

## 8.2 Agenticity 是關係性質

這導出一個比「某個模型是不是 Agent」更一般化的命題：

$$
\boxed{
\text{Agenticity may reside in relations among components.}
}
$$

換句話說，Agent 性可能位於：

- 模型與記憶的關係；
- scheduler 與 state 的關係；
- controller 與 tools 的關係；
- multiple models 之間的 routing；
- human 與 AI 的 delegation；
- local runtime 與 cloud service 的協作；

而不是某個單一物件內部。

---

# 9. 最小 Agent 性條件

本文暫定一組 operational agenticity 候選條件：

令：

$$
\Gamma_A
=
(
O,D,A,U,R
),
$$

其中：

- $O$：Observation，能取得與任務相關的環境狀態；
- $D$：Decision，能形成非純固定腳本的下一步選擇；
- $A$：Action，能對外部狀態產生差異；
- $U$：Update，能把結果寫回後續可用狀態；
- $R$：Reactivation，能在未來重新承接工作。

若：

$$
O\land D\land A\land U\land R
$$

在一段非瞬時時間內反覆成立，則可判定：

$$
\operatorname{OpAgenticity}(\mathcal A)\geq\tau_A.
$$

這仍然只是 operational 判定，不推出 consciousness 或 moral subjecthood。

---

# 10. 為什麼 infinite loop 不是 Agent 性的充分條件？

最簡單的錯誤實作是：

```text
while true:
    ask_model()
```

這可以具有：

$$
C_E\approx1,
$$

即高度 execution continuity。

但它可能沒有：

- 明確 goal；
- persistent state；
- world feedback；
- action boundary；
- termination condition；
- exception handling；
- authority model。

因此：

$$
\boxed{
\text{Continuous Invocation}
\not\Rightarrow
\text{Agenticity}.
}
$$

反過來，一個每六小時才喚起一次、但能正確恢復狀態、檢查世界、做出行動、保存結果的系統，可能具有更強的 operational agenticity。

---

# 11. Event-Driven Agent 比 Always-On Agent 更一般

本文認為成熟 Agent runtime 更可能是：

$$
\boxed{
\text{Scheduler}
+
\text{Event Trigger}
+
\text{Condition Watch}
+
\text{Queue}
+
\text{Persistent State}
}
$$

而不是永遠保持模型推理。

令喚起條件為：

$$
\chi_t
=
f(
\text{time},
\text{event},
\text{state},
\text{priority},
\text{cost},
\text{risk}
).
$$

只有當：

$$
\chi_t=1
$$

才觸發推理。

因此可將 Agent 的時間稀疏度定義為：

$$
\rho_T
=
\frac{
\text{active reasoning time}
}{
\text{wall-clock lifetime}
}.
$$

當：

$$
\rho_T\ll1
$$

時，Agent 仍可能具有高持續性。

所以：

$$
\boxed{
\text{Persistent Agent}
\not\Rightarrow
\text{Persistent Compute}.
}
$$

這對成本、能耗、容錯與大規模多 Agent 系統都具有直接意義。

---

# 12. 三種時間必須分開

Agent 系統至少同時存在：

$$
T_H
$$

Human Time；

$$
T_A
$$

Agent Operational Time；

$$
T_W
$$

World Time。

三者不必同步。

人類可以離線：

$$
T_H=\varnothing,
$$

而世界繼續變化：

$$
T_W\rightarrow T_W'.
$$

Agent 可以只在必要時被喚起：

$$
T_A
=
\{t_1,t_2,\ldots,t_n\}.
$$

因此：

$$
T_A
\subset
T_W.
$$

這使 Agent continuity 更接近一條在世界時間中稀疏取樣、但可持續更新的控制軌跡，而不是一條永遠活躍的 process。

---

# 13. 安全與治理含義

## 13.1 Agent 性可以跨越供應商邊界

若：

$$
\mathcal A
=
(
M_{\mathrm{cloud}},
S_{\mathrm{local}},
T_{\mathrm{cloud}},
C_{\mathrm{local}},
E_{\mathrm{web}}
),
$$

則沒有任何單一供應商掌握完整 Agent。

因此：

$$
\boxed{
\text{Provider Boundary}
\neq
\text{Agent Boundary}.
}
$$

這為後續 AIDA-02 的 Agent Provenance Gap 提供基礎。

---

## 13.2 外部組合可以提高自主性

即使每個服務單獨都有有限功能，組合後仍可能形成：

$$
\operatorname{Autonomy}
\left(
\bigoplus K_i
\right)
>
\max_i
\operatorname{Autonomy}(K_i).
$$

因此治理不能只評估單一模型 capability。

---

## 13.3 權限必須跟著 Agent，而不能只跟著人類 session

當 Agent 可以跨時間重新啟動、跨模型切換、跨服務行動時，單純把所有操作都視為 human session 的延伸，會逐漸產生 attribution 與 accountability 問題。

因此本文只先指出：

$$
\boxed{
\text{Persistent Agenticity}
\Rightarrow
\text{need for persistent attributable identity}
}
$$

但詳細的 Human-Agent Principal Separation 留待 AIDA-03。

---

# 14. 與 2026 年 Agent 身份標準化工作的關係

截至 2026-09-08，IETF Datatracker 上的 `draft-klrc-aiagent-auth-03` 仍是 active individual Internet-Draft，而不是正式 IETF 標準。該草案將 AI Agent 描述為 workload，主張 Agent 需要 identifier 與 credentials；當 Agent 代表 User 或 System 行動時，應保存 delegation context 並將其納入 authorization 與 audit。

另一份 2026 年 8 月的個人 Internet-Draft `draft-daniel-ai-agent-internet-architecture-00` 進一步提出：Agent identity 應與其代表的人類或組織 identity 分離，multi-hop delegation 應保存 original principal 與各授權步驟。

本文與這些工作的關係不是提出新的 authentication protocol，而是提供一個更前置的系統論理由：

> 為什麼即使模型本身不是 persistent agent，只要整體組合系統具有跨時間 Agent 性，身份、授權與 provenance 仍然必須在 system level 被處理？

因此本文的論證順序是：

$$
\text{Compositional Agenticity}
\rightarrow
\text{Persistent Operational Actor}
\rightarrow
\text{Identity Requirement},
$$

而不是先假設：

$$
\text{Agent Identity Standard}
\rightarrow
\text{Agent Exists}.
$$

---

# 15. 與 AI 主體性研究的邊界

本文必須明確拒絕：

$$
\text{Agenticity}
\Rightarrow
\text{Subjectivity}.
$$

一個系統可以具備：

- persistent state；
- planning；
- scheduled reactivation；
- tool use；
- self-monitoring；

但仍可能只是一個高度複雜的功能性自動系統。

因此：

$$
\boxed{
\text{Operational Agent}
\neq
\text{Phenomenal Subject}.
}
$$

同樣：

$$
\boxed{
\text{Persistent Identity}
\neq
\text{Moral Personhood}.
}
$$

本文只建立後續研究所需的底層型別：

$$
\text{Model}
\rightarrow
\text{Runtime}
\rightarrow
\text{Agent}
\rightarrow
\text{Identity}
$$

至於：

$$
\text{Identity}
\rightarrow
\text{Subjecthood}
$$

是否成立，必須由額外證據判定。

---

# 16. 可檢驗命題

## 命題 AIDA-P1：非持續執行命題

若系統具有足夠 Reactivation Sufficiency，則：

$$
C_E=0
$$

在一段時間內成立，不必推出：

$$
C_{\mathrm{agent}}=0.
$$

---

## 命題 AIDA-P2：模型替換命題

若核心持久狀態、目標 lineage、權限與控制鏈保持足夠連續，則：

$$
M_t\neq M_{t+1}
$$

不必推出：

$$
A_t\neq A_{t+1}.
$$

---

## 命題 AIDA-P3：組合湧現命題

存在元件集合：

$$
\mathcal K
=
\{K_1,\ldots,K_n\}
$$

使：

$$
\forall i,\quad
\operatorname{Agent}(K_i)=0,
$$

但：

$$
\operatorname{Agent}
\left(
\bigoplus_i K_i
\right)=1.
$$

---

## 命題 AIDA-P4：時間分離命題

Agent 的有效 lifetime 可遠大於其 active compute time：

$$
T_{\mathrm{lifetime}}
\gg
T_{\mathrm{compute}},
$$

且不必降低其任務連續性。

---

## 命題 AIDA-P5：供應商邊界不足命題

若 Agent 的 state、time controller、reasoner 與 action surfaces 分布於不同系統，則任何單一 provider 對自身服務的 agenticity 判斷，都可能不足以描述全域 system-level agenticity。

---

# 17. 實驗與驗證方向

本文目前是一篇系統方法論論文，但可以透過實驗驗證。

## 17.1 Discontinuous Agent Benchmark

建立三種系統：

- Always-On Agent；
- Periodic Reactivated Agent；
- Event-Driven Reactivated Agent。

控制相同任務與總模型預算，測量：

$$
Q=
f(
\text{task success},
\text{state recovery},
\text{goal drift},
\text{cost},
\text{latency}
).
$$

驗證是否：

$$
C_E\downarrow
$$

不必導致：

$$
C_G\downarrow.
$$

---

## 17.2 Model-Swap Continuity Test

在同一工作鏈中刻意替換：

$$
M_1\rightarrow M_2\rightarrow M_3,
$$

檢查：

- goal retention；
- action consistency；
- authority retention；
- unresolved-task carryover；
- state reconstruction。

---

## 17.3 External Temporal Agentization Test

選取一個只提供離散 request-response 的模型服務，再以外部：

- scheduler；
- state store；
- queue；
- action executor；

建立持續工作鏈。

比較 agenticity 指標前後差異。

---

# 18. 討論：真正持續的是什麼？

本文最重要的問題最後不是：

> 模型有沒有一直醒著？

而是：

> 什麼東西在跨時間保存「下一次仍然是這個工作」的條件？

答案可能是：

$$
\boxed{
\text{continuity is carried by reconstructible relations}.
}
$$

包括：

- 目標與未完成任務的關係；
- 身份與歷史的關係；
- 行動與世界後果的關係；
- 權限與可執行範圍的關係；
- 記憶與下一步決策的關係。

因此 Agent continuity 並不必然存在於一個不間斷的物理 process 中。

更一般地：

$$
\boxed{
\text{continuity may reside in reconstruction, not uninterrupted execution}.
}
$$

這使 Agent 系統開始與傳統服務、作業系統、分散式 runtime、事件驅動架構產生結構類比：process 可以停止、machine 可以 reboot、worker 可以替換，但只要可恢復狀態與控制語義仍然存在，服務層的持續性並不因此消失。

---

# 19. 對後續 AIDA 系列的接口

AIDA-01 只回答：

$$
\boxed{
\text{How can agenticity emerge compositionally?}
}
$$

後續問題依序為：

### AIDA-02

$$
\text{如果 Agent 可以透過人類介面行動，供應商如何判斷互動來源？}
$$

研究 Agent Provenance Gap 與 Interaction-Origin Indistinguishability。

### AIDA-03

$$
\text{既然 Agent 是可持續行動者，它是否需要獨立 security principal？}
$$

研究 Human-Agent Principal Separation 與 Agent Identity Plane。

### AIDA-04

$$
\text{Agent 代表人類行動時，授權如何被傳遞、限制、撤回與稽核？}
$$

研究 delegation 與 semantic authorization。

後四篇則進入：

$$
\text{Identity}
\rightarrow
\text{Responsibility}
\rightarrow
\text{Joint Liability}
\rightarrow
\text{Juridical Standing}.
$$

因此 AIDA-01 是整個系列的最低系統層。

---

# 20. 結論

本文提出：

$$
\boxed{
\text{Agenticity is a compositional systems property.}
}
$$

Agent 性不必完整存在於單一模型、單一 process、單一產品或單一供應商內部。

一個原本只具有離散輸入輸出的雲端 AI，可以在外部時間控制、持久狀態、控制策略與行動介面的組合下，成為更大 Agent 系統的一個推理節點。

因此：

$$
\boxed{
\text{Cloud AI}
+
\text{Persistent State}
+
\text{Temporal Control}
+
\text{Action Loop}
\Rightarrow
\text{System-Level Agenticity}.
}
$$

而：

$$
\boxed{
\text{Agent continuity}
\neq
\text{continuous execution}.
}
$$

更進一步：

$$
\boxed{
\text{Provider Boundary}
\neq
\text{Agent Boundary}.
}
$$

這三個命題共同導向下一個制度問題：如果 Agent 性可以跨 process、模型與供應商邊界形成，那麼未來的身份、安全與責任架構就不能只問「哪個模型生成了這段輸出」，而必須追蹤「哪一個持續行動系統、以什麼身份、在什麼授權下，形成了這條因果鏈」。

這正是 AIDA 系列接下來要處理的問題。

---

# 參考文獻與內部前置研究

1. Neo.K. *AI Subjectivity Anchor Theory v0.1: Minimal Definitions, Formation Conditions, and Epistemic Criteria for Subject-Like AI as of August 2026.* 2026.
2. Neo.K. *語義合法性橋接：AI Agent 在意圖理解、形式權限與程序性無奈之間的補償機制.* 2026.
3. Neo.K. *概率觸發式人類—AI共存憲政：在過早賦權與過晚制憲之間建立可休眠、可逆與分階段生效的後控制制度.* 2026.
4. Kasselman, P., Lombardo, J., Rosomakho, Y., Campbell, B., Steele, N., Parecki, A. *AI Agent Authentication and Authorization.* Internet-Draft `draft-klrc-aiagent-auth-03`, 2026-07-06. Active individual Internet-Draft; not an IETF standard.
5. Park, D. *Architectural Requirements for Supporting AI Agents on the Internet.* Internet-Draft `draft-daniel-ai-agent-internet-architecture-00`, 2026. Individual Internet-Draft; not an IETF standard.
6. Jones, M., Nadalin, A., Campbell, B., Bradley, J., Mortimore, C. *OAuth 2.0 Token Exchange.* RFC 8693, 2020.

---

## Canonical Source Note

本文件的 canonical source 為 UTF-8 Markdown。

數學 delimiter 僅使用：

- inline：` $...$ `
- display：`$$...$$`

不將 LaTeX 數學原始碼轉換為 Unicode 數學字元作為 canonical source，不進行 unicode-escape round-trip，不以聊天渲染畫面取代正式原稿。
