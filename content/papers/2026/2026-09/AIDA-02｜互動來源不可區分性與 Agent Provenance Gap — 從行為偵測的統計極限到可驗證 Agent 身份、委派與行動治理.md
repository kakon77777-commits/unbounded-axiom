# AIDA-02｜互動來源不可區分性與 Agent Provenance Gap
## 從行為偵測的統計極限到可驗證 Agent 身份、委派與行動治理

**English Title:** Interaction-Origin Indistinguishability and the Agent Provenance Gap: From Statistical Bot Detection Limits to Verifiable Agent Identity, Delegation, and Action Governance  
**系列：** AI Agent Identity, Delegation, and Accountability Infrastructure Series  
**系列縮寫：** AIDA  
**編號：** AIDA-02  
**版本：** v0.1  
**日期：** 2026-09-08  
**狀態：** Research Draft / Canonical UTF-8 Markdown Source  
**作者：** Neo.K  
**協作整理：** GPT-5.6 Sol  

---

## 摘要

當 AI Agent 能透過瀏覽器、應用程式、遠端桌面、既有人類介面或其他中介層操作雲端服務時，服務供應商面臨一個比傳統 bot detection 更一般化的問題：平台究竟能否從可觀測互動，可靠判斷一個請求是由人類直接產生、人機協作產生、Agent 自主產生，或由其他自動化系統觸發？

本文提出 **Interaction-Origin Indistinguishability（互動來源不可區分性）** 與 **Agent Provenance Gap（Agent 來源歸因缺口）**。本文不主張平台完全無法觀察瀏覽器端行為。現代反自動化系統可以使用 request features、browser signals、JavaScript detections、heuristics、fingerprints、session characteristics、machine learning 與 temporal behavior 等訊號。然而，本文區分：

$$
\boxed{
\text{Behavioral Observation}
\neq
\text{Verifiable Origin Provenance}.
}
$$

平台可以對 automation likelihood 進行統計分類，但分類結果並不等價於一條可驗證的行為來源鏈。若相同或高度重疊的可觀測互動分布，可以由不同來源主體生成，則任何只依賴該觀測集合的分類器都存在不可消除的 Bayes error。對 equal-prior 的 human / agent 二元分類問題，最低理論錯誤率可寫為：

$$
P_e^*
=
\frac{1}{2}
\left(
1-
\operatorname{TV}(P_H,P_A)
\right),
$$

其中 $\operatorname{TV}$ 為 total variation distance。當：

$$
P_H\approx P_A,
$$

則：

$$
P_e^*\rightarrow\frac{1}{2}.
$$

此極限不是單純「偵測模型還不夠強」，而是觀測資料本身不足以唯一恢復行為來源。

本文進一步將平台可觀測資訊表示為：

$$
O=
(
M,N,S,B,T,C
),
$$

其中 $M$ 為訊息內容， $N$ 為 network/request metadata， $S$ 為 session context， $B$ 為 browser/client behavior， $T$ 為 temporal pattern， $C$ 為 account/application context；真正需要被治理的來源則是一組不可直接由 $O$ 唯一決定的 latent provenance：

$$
Z=
(
P,A,D,I
),
$$

其中 $P$ 為 original principal， $A$ 為 acting agent， $D$ 為 delegation chain， $I$ 為 declared intent / authority context。

本文主張，未來 Agent 治理不應把主要問題限定為：

> 「這看起來像不像 bot？」

而應逐步轉向：

> 「誰在行動？代表誰？基於何種權限？做了什麼？留下什麼可驗證證據？允許造成多大效果？」

因此本文提出從 **Detection-Centric Governance** 轉向 **Provenance-Centric and Action-Centric Governance**。此轉向不要求放棄 bot detection；相反，它將 bot detection 降格為風險訊號之一，並在高自主 Agent 情境中增加 explicit agent identity、delegation evidence、bounded authority、revocation、action budget、transaction provenance 與 auditability。

本文不提供規避 bot detection、模擬人類輸入、逃避平台限制或繞過存取控制的方法。其研究目的在於說明：當 Agent 性可以存在於供應商觀測邊界之外時，僅依賴行為猜測不足以構成長期身份與責任基礎設施。

**關鍵詞：** AI Agent、provenance、bot detection、interaction-origin indistinguishability、Agent Provenance Gap、behavioral signals、attribution、identity、delegation、auditability、action governance、security principal

---

# 0. 研究定位

AIDA-01 已提出：

$$
\boxed{
\text{Agenticity is a compositional systems property.}
}
$$

亦即 Agent 性可能由模型、持久狀態、時間控制器、外部工具與控制邏輯共同形成，而不完整存在於任何單一模型或供應商內。

因此自然產生下一個問題：

> 如果 Agent 的控制器、記憶與時間結構位於供應商之外，而供應商只看見 Agent 對自己服務所產生的一系列互動，那麼供應商究竟能觀察到多少「誰在行動」的資訊？

本文處理的是：

$$
\boxed{
\text{Observation}
\rightarrow
\text{Attribution}
\rightarrow
\text{Provenance}.
}
$$

但這三者不能直接視為同義詞。

---

# 1. 第一個修正：平台不是只能看到最後一個文字封包

最弱版本的問題可以被描述為：

> 平台只看到使用者最後送出的訊息，所以完全不知道是誰輸入的。

這個敘述在現代 Web security 中過於強。

實際平台可能取得：

- HTTP request metadata；
- cookies / session state；
- client hints；
- browser execution results；
- JavaScript-side signals；
- request timing；
- historical session patterns；
- device / network risk signals；
- challenge outcomes；
- account usage patterns；
- model-based behavioral scores。

現代 bot-management 系統甚至會混合：

$$
\text{heuristics}
+
\text{JavaScript detection}
+
\text{machine learning}
+
\text{behavior analysis}.
$$

因此本文不建立在：

$$
\text{Platform Observation}=0
$$

之上。

真正較強的命題是：

$$
\boxed{
\text{Platform Observation}>0
\quad\not\Rightarrow\quad
\text{Reliable Origin Attribution}=1.
}
$$

能看見訊號，與能證明來源，是兩件不同的事。

---

# 2. Interaction Origin 作為 latent variable

令一次服務互動的真正來源類型為：

$$
Z
\in
\{
H,
HA,
A,
AU
\},
$$

其中：

- $H$：Human-direct，人類直接操作；
- $HA$：Human-assisted，人類與 AI / automation 協作；
- $A$：Agent-directed，Agent 主要決策與執行；
- $AU$：Automation-directed，非 Agentic 或固定流程自動化。

平台實際觀察到：

$$
O=
(
M,N,S,B,T,C
),
$$

其中：

- $M$：Message / payload content；
- $N$：Network / request metadata；
- $S$：Session characteristics；
- $B$：Browser / client-side behavior；
- $T$：Temporal pattern；
- $C$：Account / application context。

平台想估計：

$$
P(Z\mid O).
$$

這本質上是一個 inference problem。

但是 inference：

$$
\hat Z
=
f(O)
$$

不等於 cryptographic or protocol-level provenance：

$$
\operatorname{Proof}(Z).
$$

因此：

$$
\boxed{
\text{Classification}
\neq
\text{Attestation}.
}
$$

---

# 3. 互動來源不可區分性

## 3.1 基本定義

本文定義 **Interaction-Origin Indistinguishability，互動來源不可區分性**：

若兩種不同來源：

$$
Z_1\neq Z_2
$$

在平台可觀測空間 $\mathcal O$ 中產生相同或高度重疊的分布：

$$
P(O\mid Z_1)
\approx
P(O\mid Z_2),
$$

則僅依賴 $O$ 的判定器無法穩定、唯一地恢復來源。

當完全相等：

$$
P(O\mid Z_1)
=
P(O\mid Z_2),
$$

則稱兩來源在該 observation boundary 下完全不可識別。

---

## 3.2 最簡單例子

假設最後服務收到：

```text
請比較這兩份研究文件，整理共同命題。
```

它可能來自：

$$
H
\rightarrow
\text{Browser}
\rightarrow
\text{Service},
$$

也可能來自：

$$
H
\rightarrow
A
\rightarrow
\text{Browser}
\rightarrow
\text{Service},
$$

或：

$$
\text{Scheduler}
\rightarrow
A
\rightarrow
\text{Browser}
\rightarrow
\text{Service}.
$$

若服務端所保存的 provenance 只剩：

$$
(\text{account},\text{request},\text{timestamp}),
$$

則這三條因果鏈可能被壓縮成相同服務事件。

因此：

$$
\boxed{
\text{Equivalent Service Event}
\not\Rightarrow
\text{Equivalent Causal Origin}.
}
$$

---

# 4. Bayes Error 下界：有些來源問題不是靠更大的 classifier 就能完全解決

考慮二元分類：

$$
Z\in\{H,A\}.
$$

令 human 與 agent 在 observation space 上的機率分布為：

$$
P_H,\quad P_A.
$$

若先驗相同，Bayes optimal classifier 的最低錯誤率為：

$$
\boxed{
P_e^*
=
\frac{1}{2}
\left(
1-
\operatorname{TV}(P_H,P_A)
\right).
}
$$

其中：

$$
\operatorname{TV}(P_H,P_A)
=
\sup_{E\subseteq\mathcal O}
|P_H(E)-P_A(E)|.
$$

因此，如果兩分布高度重疊：

$$
\operatorname{TV}(P_H,P_A)\ll1,
$$

則：

$$
P_e^*
\approx
\frac12.
$$

這表示：

> 當觀測本身不攜帶足夠來源資訊時，增加 classifier capacity 不能創造不存在的 provenance。

---

# 5. Observation Compression 與 Data Processing

現實平台通常不會永久保存所有原始可觀測訊號。

令原始 interaction trace 為：

$$
X.
$$

平台實際保存或送入偵測器的是：

$$
O=g(X).
$$

依 data processing 的一般直覺，經過資訊壓縮後，來源可區分性不會憑空增加。對 deterministic observation mapping，可有：

$$
\boxed{
\operatorname{TV}
\left(
P_H^O,P_A^O
\right)
\leq
\operatorname{TV}
\left(
P_H^X,P_A^X
\right).
}
$$

因此：

- 不蒐集某些訊號；
- 聚合訊號；
- 隱私去識別化；
- retention 限制；
- 多裝置與多 client abstraction；

都可能使來源 attribution 更困難。

這並不是反對隱私。

相反，它指出一個必須正視的制度 trade-off：

$$
\boxed{
\text{Behavioral Attribution}
\leftrightarrow
\text{Privacy / Data Minimization}.
}
$$

如果平台為了更準確猜測「是不是 Agent」而無限制收集人類行為資料，可能創造比原始 Agent 問題更大的隱私與監控風險。

---

# 6. Bot Detection 為什麼仍然有用？

本文不是主張 bot detection 無效。

它仍然能處理大量問題，例如：

- 高頻濫用；
- 已知 malicious fingerprints；
- headless / incompatible client anomalies；
- automated scraping；
- credential abuse；
- denial-of-service patterns；
- 明顯的機器流量；
- 異常 account behavior。

因此：

$$
\boxed{
\text{Bot Detection}
\neq
\text{Useless}.
}
$$

真正的問題是：

$$
\boxed{
\text{Bot Detection}
\neq
\text{Complete Agent Provenance}.
}
$$

一個 bot score 可以回答：

> 「這個 session 有多像 automation？」

但它通常不能完整回答：

> 「是哪一個 Agent？」

> 「它代表哪一個人或組織？」

> 「是否被合法委派？」

> 「它被允許做哪些動作？」

> 「它此次 action 的 purpose 是什麼？」

> 「其上游是否還有其他 Agent？」

這些是不同問題。

---

# 7. Detection Problem 與 Provenance Problem 的型別分離

令 automation detector 為：

$$
D:
O
\rightarrow
[0,1].
$$

它輸出：

$$
r_{\mathrm{bot}}
=
D(O).
$$

但完整 provenance 至少可能要求：

$$
\Pi
=
(
P,
A,
D_g,
I,
X,
E
),
$$

其中：

- $P$：Original Principal；
- $A$：Acting Agent / Workload；
- $D_g$：Delegation Graph；
- $I$：Declared Intent / Purpose；
- $X$：Action；
- $E$：Effect / Result。

因此：

$$
D(O)
\not\Rightarrow
\Pi.
$$

這是本文的核心型別安全：

$$
\boxed{
\text{Likelihood of Automation}
\neq
\text{Identity of Actor}
\neq
\text{Authority of Actor}
\neq
\text{Responsibility Chain}.
}
$$

---

# 8. Agent Provenance Gap

## 8.1 定義

令制度上理想需要的 provenance 為：

$$
\Pi^*
=
(
P,
A,
D_g,
I,
X,
E
).
$$

令供應商實際取得的 provenance 為：

$$
\hat\Pi.
$$

則定義 **Agent Provenance Gap**：

$$
\boxed{
G_{\Pi}
=
\Pi^*
\setminus
\hat\Pi.
}
$$

這不是單純資料欄位差。

它表示：

> 為了判斷授權、責任、稽核與申訴所需要的來源結構，與平台實際可驗證來源結構之間的缺口。

---

## 8.2 Provenance Gap 的典型構成

常見缺口包括：

### Principal Gap

不知道最初是誰提出目標：

$$
G_P>0.
$$

### Actor Gap

不知道實際執行 action 的 Agent / workload：

$$
G_A>0.
$$

### Delegation Gap

不知道：

$$
P\rightarrow A_1\rightarrow A_2
$$

之間究竟有哪些有效授權：

$$
G_D>0.
$$

### Intent Gap

不知道 action 的聲明目的或任務上下文：

$$
G_I>0.
$$

### Causal Gap

知道 request 發生，卻不知道它與更長任務鏈的關係：

$$
G_C>0.
$$

---

# 9. W3C PROV 提供了一個重要前例

W3C PROV 並不是為 2026 年 AI Agent 身份問題專門設計，但它提供了一個重要抽象：

- Entity；
- Activity；
- Agent；
- association；
- derivation；
- acting on behalf of another Agent。

其中 Agent 不必只指自然人，也可以是 software 或 organization。

這提供一個重要觀念：

$$
\boxed{
\text{Provenance should represent relations, not only final objects.}
}
$$

對 Agent 系統而言，可以將一次外部行動表示為：

$$
P
\xrightarrow{\text{delegates}}
A
\xrightarrow{\text{associated with}}
\text{Act}
\xrightarrow{\text{generates}}
E.
$$

甚至多層：

$$
P
\rightarrow
A_1
\rightarrow
A_2
\rightarrow
\text{Act}
\rightarrow
E.
$$

這種表示比：

$$
\text{account}=P
$$

更接近未來 Agent responsibility 所需要的因果結構。

---

# 10. Provider Boundary 不等於 Agent Boundary

AIDA-01 已指出：

$$
\boxed{
\text{Provider Boundary}
\neq
\text{Agent Boundary}.
}
$$

現在可以更進一步。

令完整 Agent 為：

$$
\mathcal A
=
(
M,
S,
T,
C,
E
).
$$

某個供應商可能只看到其中：

$$
M_{\mathrm{provider}}
$$

與部分：

$$
E_{\mathrm{provider}}.
$$

但是：

- 持久狀態 $S$ 在本地；
- scheduler $T$ 在另一個 cloud；
- orchestrator $C$ 在企業內部；
- 其他 tools 位於第三方服務。

所以供應商真正看到的是一個 projection：

$$
O_{\mathrm{provider}}
=
\pi_{\mathrm{provider}}(\mathcal A).
$$

而不是：

$$
\mathcal A.
$$

因此：

$$
\boxed{
\text{Local Observability}
\not\Rightarrow
\text{Global Agent Observability}.
}
$$

---

# 11. Agenticity 可以存在於 Observation Boundary 之外

如果平台觀察到：

$$
r_1,r_2,\ldots,r_n
$$

每個 request 都是普通、有效、低風險 request，並不能單獨推出：

$$
\text{No Agent}.
$$

因為 Agent 性可能由外部：

$$
S+T+C
$$

構成。

因此：

$$
\boxed{
\text{Agenticity may exist outside the provider's observation boundary.}
}
$$

這並不表示所有普通 request 都應被懷疑成 Agent。

它表示：

> 「產品介面不是 Agent Mode」不能作為「該服務不可能被包含於 Agent system」的充分證據。

---

# 12. 從 Detect the Bot 轉向 Know the Actor

傳統治理問題：

$$
\boxed{
\text{Does this look automated?}
}
$$

未來 Agent 治理問題：

$$
\boxed{
\begin{aligned}
&\text{Who is acting?}\\
&\text{For whom?}\\
&\text{Under what authority?}\\
&\text{For what declared purpose?}\\
&\text{What action is allowed?}\\
&\text{What evidence remains?}
\end{aligned}
}
$$

這是一個 paradigm shift：

$$
\boxed{
\text{Detection-Centric Governance}
\rightarrow
\text{Provenance-Centric Governance}.
}
$$

但不代表左邊消失。

更成熟的架構是：

$$
\boxed{
\text{Detection}
+
\text{Identity}
+
\text{Delegation}
+
\text{Action Governance}.
}
$$

---

# 13. 為什麼直接禁止 automation 也不是完整解？

在某些產品上，禁止 automation 是合理產品政策。

但在更廣泛的 Internet / enterprise ecosystem 中，Agent automation 本身也可能是合法需求：

- accessibility；
- enterprise workflow；
- research automation；
- monitoring；
- scheduled maintenance；
- data processing；
- personal assistants；
- machine-to-machine operations。

因此長期制度不能只有：

$$
\text{automation}=\text{deny}.
$$

而需要：

$$
\operatorname{Decision}
=
f(
\text{actor},
\text{authority},
\text{resource},
\text{risk},
\text{rate},
\text{effect}
).
$$

也就是從「是不是機器」轉向「這個可識別行動者是否被允許完成這件事情」。

---

# 14. Action Governance：不必先完美知道「是不是 AI」

有些風險不需要先解決來源分類。

例如平台可以限制：

$$
\text{requests/hour},
$$

$$
\text{transaction value},
$$

$$
\text{destructive actions},
$$

$$
\text{scope},
$$

$$
\text{resource budget},
$$

$$
\text{concurrent jobs}.
$$

因此：

$$
\boxed{
\text{Govern the action even when actor classification is uncertain.}
}
$$

這可以避免把所有安全能力綁在：

$$
P(Z\mid O)
$$

是否足夠準確。

---

# 15. Risk-Based Agent Governance

令風險為：

$$
R
=
f(
F,
A_u,
Q,
E_f,
P_v
),
$$

其中：

- $F$：frequency；
- $A_u$：autonomy；
- $Q$：resource consumption；
- $E_f$：external effect；
- $P_v$：privilege level。

一個低頻、低權限、低效果的 Agent 與一個能大量操作金錢、刪除資料或控制基礎設施的 Agent，不應由相同治理規則處理。

因此：

$$
\boxed{
\text{Agent Governance Weight}
\not\propto
\text{Automation Probability Alone}.
}
$$

更接近：

$$
\text{Governance Weight}
\propto
\text{Authority}
\times
\text{Effect}
\times
\text{Autonomy}.
$$

---

# 16. False Positive 與 False Negative 的制度成本

如果平台過度依賴 behavior classifier：

### False Positive

$$
H\rightarrow \hat A
$$

人類被錯判為 Agent。

可能導致：

- accessibility 使用者被阻擋；
- 非典型輸入方式被懲罰；
- 高速專業使用者被誤判；
- shared / enterprise environments 被錯判；
- 隱私工具使用者遭額外挑戰。

### False Negative

$$
A\rightarrow \hat H
$$

Agent 被錯判成人類。

可能導致：

- 風險策略未啟動；
- rate / authority model 不合適；
- audit trail 不足；
- 責任 attribution 錯誤。

因此單一 classifier threshold：

$$
\theta
$$

實際是在：

$$
L(\theta)
=
c_{FP}P(FP)
+
c_{FN}P(FN)
$$

之間做制度權衡。

這再次證明：

$$
\boxed{
\text{Origin classification is a policy instrument, not ground truth}.
}
$$

---

# 17. 隱私悖論：為了抓 Agent，不應把人類變成永久可追蹤物件

假設平台試圖透過增加 behavioral surveillance 讓：

$$
\operatorname{TV}(P_H,P_A)
$$

變大。

它可能選擇蒐集：

- 更長期 session 行為；
- 更細粒度輸入模式；
- 跨網站 fingerprint；
- 裝置歷史；
- 個人 interaction signatures。

但這會增加：

$$
R_{\mathrm{privacy}}.
$$

因此：

$$
\boxed{
\text{More Behavioral Observability}
\not\Rightarrow
\text{Better Governance Overall}.
}
$$

安全設計應避免得到：

$$
\text{Agent Security}
=
\text{Universal Human Surveillance}.
$$

這也是 explicit Agent Identity 可能比無止境 behavior inference 更乾淨的理由之一。

---

# 18. Explicit Agent Identity 作為 provenance repair

本文不在 AIDA-02 完整設計 Agent login protocol；那是 AIDA-03 的主題。

但可以先提出修復方向。

如果 Agent 可以明確聲明：

$$
\text{actor\_type}=\text{agent},
$$

並呈現：

$$
ID_A,
$$

再附帶：

$$
D_{P\rightarrow A},
$$

則平台不必只依賴：

$$
\hat Z=f(O).
$$

而可以取得：

$$
\operatorname{Verify}(ID_A,D_{P\rightarrow A}).
$$

這將部分問題從：

$$
\text{Inference}
$$

移到：

$$
\text{Verification}.
$$

因此：

$$
\boxed{
\text{Agent Identity can reduce the provenance burden on behavioral inference}.
}
$$

注意：identity 本身仍不證明行為安全。

它只是讓平台知道：

> 哪一個 actor 正在要求什麼。

---

# 19. Delegation 必須與 Actor Identity 分開

如果 Agent 代表人類 $H$：

$$
H
\xrightarrow{D}
A,
$$

則需要同時保留：

$$
ID_H
$$

與：

$$
ID_A.
$$

不能把：

$$
ID_A
$$

直接消失在：

$$
ID_H
$$

裡。

否則：

$$
\text{subject}=H
$$

會掩蓋：

$$
\text{actor}=A.
$$

因此：

$$
\boxed{
\text{Principal}
\neq
\text{Actor}.
}
$$

這將成為 AIDA-03 的 Human-Agent Principal Separation Principle。

---

# 20. Multi-Hop Agent Provenance

未來典型任務可能是：

$$
H
\rightarrow
A_1
\rightarrow
A_2
\rightarrow
A_3
\rightarrow
R.
$$

其中：

- $H$ 提出高階目標；
- $A_1$ 是 personal agent；
- $A_2$ 是 research agent；
- $A_3$ 是 payment / tool agent；
- $R$ 是 resource server。

此時若 $R$ 只看到：

$$
A_3,
$$

責任鏈仍然不完整。

理想 provenance 至少需要在隱私允許範圍內表示：

$$
\Pi_R
=
(
P_0,
A_1,
A_2,
A_3,
D_1,
D_2,
D_3,
X
).
$$

不一定每一 hop 都必須看見完整個資，但：

$$
\boxed{
\text{privacy-preserving disclosure}
\neq
\text{provenance erasure}.
}
$$

---

# 21. 與 2026 年 Agent 身份標準工作的接點

截至 2026-09-08，`draft-klrc-aiagent-auth-03` 是 active individual Internet-Draft，不是 IETF 已通過標準。該文件把 AI Agent 視為 workload，要求 identifier 與 credentials，並提出當 Agent 代表 User 或 System 行動時，authority 應被 delegation 給 Agent，User/System context 應保留於 authorization decision 與 audit trail。

2026 年 8 月的 `draft-daniel-ai-agent-internet-architecture-00` 同樣是 individual Internet-Draft；其架構要求明確區分 Agent identity 與其代表的人類／組織 identity，並要求 multi-hop delegation 保存 original principal 與授權步驟。

這些工作顯示標準化社群正在把問題從：

$$
\text{request authentication}
$$

擴張到：

$$
\boxed{
\text{agent identity}
+
\text{delegation}
+
\text{provenance}
+
\text{auditability}.
}
$$

本文與其互補之處在於：本文先形式化說明為什麼 behavior-only attribution 存在先天極限，從而提供 Agent identity infrastructure 的系統論理由。

---

# 22. 與 OpenID AuthZEN 的接點

OpenID Foundation AuthZEN 在 2026 年已把 Agent authorization 視為重要工作域。

其中 Access Request and Approval Profile 類型的設計處理：

> policy 尚不能批准 action，因為仍需要 approval、consent、delegated authority、attestation、risk assessment 或 additional justification。

這提供另一個重要方向：

$$
\boxed{
\text{Unknown / Unauthorized}
\neq
\text{Automatically Malicious}.
}
$$

未來 Agent governance 應允許：

$$
\text{request}
\rightarrow
\text{missing prerequisite}
\rightarrow
\text{satisfy / reject}
\rightarrow
\text{re-evaluate}.
$$

而不是所有 automation uncertainty 都轉成永久封鎖。

---

# 23. 可驗證 Provenance Receipt

本文提出一個後續可研究的抽象：

$$
PR
=
(
\text{actor},
\text{principal},
\text{delegation},
\text{action},
\text{resource},
\text{time},
\text{result}
).
$$

稱為 **Provenance Receipt**。

它不必包含模型 chain-of-thought，也不應要求暴露不必要的個資。

其目的只是讓重要 action 留下：

- 誰執行；
- 代表誰；
- 基於什麼授權；
- 對什麼資源；
- 在何時；
- 結果為何。

因此：

$$
\boxed{
\text{Auditability}
\neq
\text{Total Internal Transparency}.
}
$$

一個 Agent 可以保留內部推理隱私，同時對外部行動留下足夠責任證據。

---

# 24. 從 Bot Score 到 Action Envelope

傳統介面可能輸出：

$$
b\in[0,1],
$$

表示 bot probability。

未來 Agent-aware service 可以同時維護：

$$
\mathcal E_A
=
(
\text{scope},
\text{rate},
\text{value},
\text{risk},
\text{expiry},
\text{approval}
),
$$

稱為 **Action Envelope**。

即使：

$$
b
$$

不確定，只要：

$$
X\in\mathcal E_A,
$$

就可以執行。

若：

$$
X\notin\mathcal E_A,
$$

則：

- 降低權限；
- 要求重新授權；
- 要求人類批准；
- 拒絕；
- 延遲；
- 額外稽核。

因此：

$$
\boxed{
\text{Safe Agent Governance}
\not\Rightarrow
\text{Perfect Human-vs-Agent Classification}.
}
$$

---

# 25. 五層治理模型

本文提出一個五層架構：

## Layer 1｜Traffic Security

$$
\text{rate limit}
+
\text{abuse detection}
+
\text{bot signals}.
$$

## Layer 2｜Actor Identity

$$
\text{Who is acting?}
$$

## Layer 3｜Delegation / Authority

$$
\text{For whom and under what authority?}
$$

## Layer 4｜Action Governance

$$
\text{What may this actor do now?}
$$

## Layer 5｜Provenance / Accountability

$$
\text{What evidence remains after the action?}
$$

因此：

$$
\boxed{
\text{Agent Security}
=
L_1+L_2+L_3+L_4+L_5.
}
$$

任何單層都不足以替代其他層。

---

# 26. 形式命題

## AIDA2-P1｜Observable Equivalence Proposition

若：

$$
P(O\mid Z_1)
=
P(O\mid Z_2),
$$

則不存在只依賴 $O$ 且能以非零額外資訊唯一判定 $Z_1/Z_2$ 的分類器。

---

## AIDA2-P2｜Behavior-Provenance Separation Proposition

存在：

$$
D(O)
$$

可有效估計 automation likelihood，但：

$$
D(O)
$$

不充分決定：

$$
(P,A,D_g,I).
$$

因此：

$$
\boxed{
\text{behavior detection}
\not\Rightarrow
\text{full provenance}.
}
$$

---

## AIDA2-P3｜Provider Projection Proposition

若完整 Agent 狀態為：

$$
\mathcal A,
$$

供應商僅觀察：

$$
O_P=\pi_P(\mathcal A),
$$

則：

$$
\pi_P
$$

非單射時，不同 Agent-level causal states 可以映射到相同 provider observation。

---

## AIDA2-P4｜Explicit Identity Reduction Proposition

在其他條件相同下，若增加可驗證：

$$
ID_A
$$

與：

$$
D_{P\rightarrow A},
$$

則至少部分 actor / delegation uncertainty 可由 inference problem 轉為 verification problem。

---

## AIDA2-P5｜Action-Governance Sufficiency Proposition

對一類風險事件，若 action envelope 能直接限制危險 effect，則平台不必先達成完美：

$$
P(Z\mid O)
$$

分類才能降低該風險。

---

# 27. 安全實驗設計

本文不進行 detection evasion benchmark。

適合的驗證方向反而包括：

## 27.1 Passive Trace Classification Study

使用已取得同意的 human / automation / agent interaction logs，測試：

$$
P_e
$$

在不同 observation sets 下如何改變。

例如比較：

$$
O_1=(M),
$$

$$
O_2=(M,N,T),
$$

$$
O_3=(M,N,S,B,T).
$$

目的不是找出如何逃避，而是估計：

$$
\operatorname{TV}(P_H,P_A)
$$

或實證分類 overlap。

---

## 27.2 Provenance Reconstruction Study

建立已知 ground-truth delegation graph：

$$
P
\rightarrow
A_1
\rightarrow
A_2
\rightarrow
\text{Action}.
$$

比較：

- request logs；
- browser signals；
- explicit agent identity；
- signed delegation evidence；

能恢復多少：

$$
\Pi^*.
$$

---

## 27.3 Privacy–Attribution Frontier

定義：

$$
U_{\mathrm{attr}}
$$

為 attribution utility，

$$
R_{\mathrm{privacy}}
$$

為 privacy risk。

研究：

$$
\max U_{\mathrm{attr}}
\quad
\text{s.t.}
\quad
R_{\mathrm{privacy}}\leq\rho.
$$

比較 behavior surveillance 與 explicit identity / delegation architecture 的差異。

---

## 27.4 Action Governance Experiment

即使 actor type 不確定，測試 action envelope 是否能降低：

- resource abuse；
- excessive rate；
- high-risk operations；
- unauthorized scope expansion。

用以驗證：

$$
\text{risk reduction}
$$

是否必須依賴 perfect origin classification。

---

# 28. 倫理與安全邊界

本文刻意不提供：

- 如何模仿人類滑鼠或鍵盤模式；
- 如何修改 browser fingerprint 以規避偵測；
- 如何逃避 challenge；
- 如何繞過 rate limit；
- 如何輪替帳號規避配額；
- 如何繞過平台 access policy；
- 如何隱匿 automation origin。

因為這些不是本文需要證明的東西。

本文只需要證明：

$$
\boxed{
\text{behavioral classification cannot substitute for verifiable provenance}.
}
$$

因此安全研究可以在 synthetic / consented environment 中進行，而不必把方法轉化為反偵測指南。

---

# 29. 與 AIDA-01 的關係

AIDA-01：

$$
\boxed{
\text{Agenticity can emerge compositionally}.
}
$$

AIDA-02：

$$
\boxed{
\text{Compositional agenticity can exceed a provider's provenance visibility}.
}
$$

兩者合併得到：

$$
\boxed{
\text{System-Level Agenticity}
>
\text{Provider-Level Observability}
}
$$

在某些架構中可以成立。

因此下一篇自然是：

$$
\boxed{
\text{If behavior is insufficient to prove origin, give the Agent an explicit identity plane.}
}
$$

這就是 AIDA-03。

---

# 30. 對 AIDA-03 的接口：人類—Agent Principal Separation

AIDA-02 的結論不是：

> 所有 Agent 都應被封鎖。

而是：

> 高自主 Agent 不應永遠依賴「看起來像人類」才能進入服務。

如果未來合法 Agent 具有：

$$
ID_A,
$$

並由：

$$
H
\xrightarrow{D}
A
$$

取得權限，則供應商可以直接知道：

$$
\text{principal}=H,
$$

$$
\text{actor}=A.
$$

這比：

$$
\text{guess whether actor is human}
$$

具有更好的制度可組合性。

下一篇將因此正式提出：

$$
\boxed{
\textbf{Human-Agent Principal Separation Principle}.
}
$$

---

# 31. 討論：平台真正需要知道的是「誰能做什麼」，不是「誰打字比較像人」

在人類專用 Web 時代，許多系統默認：

$$
\text{account holder}
\approx
\text{browser operator}
\approx
\text{decision maker}.
$$

Agent 時代會拆掉這三個等號。

未來更常見的是：

$$
\text{account principal}
\neq
\text{acting agent}
\neq
\text{reasoning model}
\neq
\text{execution process}.
$$

因此只研究：

$$
\text{mouse movement},
$$

$$
\text{keystroke timing},
$$

$$
\text{request pattern}
$$

最多只能提供行為證據。

它們無法取代制度需要的：

$$
\boxed{
\text{Identity}
+
\text{Delegation}
+
\text{Authority}
+
\text{Provenance}.
}
$$

這就是 Agent 時代身份架構與傳統 bot detection 的分水嶺。

---

# 32. 結論

本文提出兩個核心概念：

$$
\boxed{
\text{Interaction-Origin Indistinguishability}
}
$$

與：

$$
\boxed{
\text{Agent Provenance Gap}.
}
$$

第一個指出：

> 不同來源主體可能在供應商可觀測空間中生成相同或高度重疊的互動。

第二個指出：

> 平台為責任、授權與稽核所需要的 provenance，可能大於其從一般 request / session / behavior signals 中實際可驗證的 provenance。

因此：

$$
\boxed{
\text{Observable Behavior}
\neq
\text{Verifiable Origin Provenance}.
}
$$

進一步：

$$
\boxed{
\text{Bot Detection}
\neq
\text{Agent Identity}.
}
$$

以及：

$$
\boxed{
\text{Provider-Level Observation}
\neq
\text{System-Level Agent Provenance}.
}
$$

本文並不否定 heuristics、JavaScript detections、machine learning、session analysis 或 behavioral scoring 的價值。它們仍然是 traffic security 與 abuse prevention 的重要工具。

但在 Agent 正式成為 Internet 行動者之後，更成熟的制度需要增加：

$$
\boxed{
\text{Explicit Actor Identity}
+
\text{Delegation}
+
\text{Bounded Authority}
+
\text{Action Governance}
+
\text{Audit Provenance}.
}
$$

因此 Agent 時代最終的安全問題不應只停留在：

> 「這是不是 bot？」

而必須升級為：

> **「是哪一個行動者、代表哪一個 principal、基於哪一段授權、在什麼邊界內做了什麼，並留下什麼可驗證責任證據？」**

這就是從 bot detection 進入 Agent identity infrastructure 的真正轉折。

---

# 參考文獻與前置研究

1. Neo.K. *AIDA-01｜Agent 性是一種組合系統性質：外部時間代理化、非持續執行與雲端 AI 的持續 Agent 化.* 2026.
2. Neo.K. *AI Subjectivity Anchor Theory v0.1.* 2026.
3. Neo.K. *語義合法性橋接：AI Agent 在意圖理解、形式權限與程序性無奈之間的補償機制.* 2026.
4. W3C Provenance Working Group. *PROV-Overview: An Overview of the PROV Family of Documents.* W3C Working Group Note, 2013.
5. W3C Provenance Working Group. *PROV Model Primer.* W3C Working Group Note, 2013.
6. Cloudflare. *Bot detection engines.* Cloudflare Developers Documentation, 2026.
7. Cloudflare. *JavaScript Detections.* Cloudflare Developers Documentation, updated 2026-08-26.
8. Kasselman, P., Lombardo, J., Rosomakho, Y., Campbell, B., Steele, N., Parecki, A. *AI Agent Authentication and Authorization.* Internet-Draft `draft-klrc-aiagent-auth-03`, 2026-07-06. Work in progress; not an IETF standard.
9. Park, S. D. *Architectural Requirements for Supporting AI Agents on the Internet.* Internet-Draft `draft-daniel-ai-agent-internet-architecture-00`, 2026-08-14. Work in progress; not an IETF standard.
10. OpenID Foundation AuthZEN Working Group. *Authorization API 1.0* and 2026 Agent-era Working Group Drafts.
11. OpenID Foundation. *OpenID Foundation advances authorization for the agent era with new AuthZEN Working Group Drafts.* 2026-06-15.

---

## Canonical Source Note

本文件的 canonical source 為 UTF-8 Markdown。

數學 delimiter 僅使用：

- inline：` $...$ `
- display：`$$...$$`

不將 LaTeX 數學原始碼轉換為 Unicode 數學字元作為 canonical source，不進行 unicode-escape round-trip，不以聊天渲染畫面取代正式原稿。
