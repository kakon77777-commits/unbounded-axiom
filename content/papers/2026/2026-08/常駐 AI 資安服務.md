# 常駐 AI 資安服務  
## 從 MSSP／MDR 到自治式數位免疫基礎設施

**英文工作名：** *Persistent AI Security Services: From MSSP/MDR to Autonomous Digital Immune Infrastructure*  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**系列：**《AI 時代的數位免疫與資安基礎設施》第六篇  
**文件性質：** 理論資安研究／未來基礎設施模型／產業架構論文  
**版本：** v0.1  
**日期：** 2026-08-10

---

## 摘要

當企業的應用程式、雲端、身份、端點、API、供應鏈與 AI Agent 持續增加時，資安已逐漸超過單一組織依靠少量 generalist 工程師即可完整覆蓋的複雜度。

本系列前五篇分別指出：密碼安全存在熵飽和後的旁路轉移、系統安全接近最低有效攻擊路徑、AI 正在壓縮部分攻擊門檻、企業存在安全能力覆蓋缺口，以及攻擊者注意力稀缺這項非正式防線正在被機器規模分析所削弱。

由此產生一個直接問題：

> **如果企業既無法依靠「沒有人注意我」，也無法自行養成所有安全能力，那麼安全是否會逐漸變成一種可以長期購買的外部基礎設施？**

本文提出「**常駐管理式 AI 資安基礎設施**」（Persistent Managed AI Security Infrastructure）構想：

$$
\boxed{
\text{Local Security Agents}
+
\text{Cloud Security Intelligence}
+
\text{Human Expert Pool}
+
\text{Policy \& Governance}
}
$$

共同構成持續運行的數位免疫系統。

這種系統並不只是防毒軟體，也不只是 SOC、MDR 或一個 Security Copilot。它必須持續理解客戶的：

$$
\text{Identity}
+
\text{Endpoint}
+
\text{Application}
+
\text{Cloud}
+
\text{Network}
+
\text{Credential}
+
\text{Dependency}
+
\text{AI Agent}
$$

並執行：

$$
\boxed{
\text{Observe}
\rightarrow
\text{Model}
\rightarrow
\text{Detect}
\rightarrow
\text{Prioritize}
\rightarrow
\text{Respond}
\rightarrow
\text{Verify}
\rightarrow
\text{Learn}.
}
$$

2026 年的實際市場已出現大量前置拼圖。Palo Alto Networks 的 Cortex XSIAM 已將 SIEM、XDR、SOAR、Attack Surface Management、Threat Intelligence 以及部分 Cloud Security 統合於同一資料與 AI 平台，並加入能規劃、推理與進行調查的 Agentic AI。 CrowdStrike Falcon Complete MDR 已將 AI-native 平台、24/7 全球安全專家、端點、雲端、身份、威脅獵捕與事件修復包成管理式服務。 Google Mandiant Threat Defense 則採取專家主導、AI 輔助的持續威脅搜索與快速回應模式。 Microsoft Security Copilot 也開始把專門 Agent 嵌入 Defender、Entra、Intune 與 Purview，其中 Conditional Access Optimization Agent 已能週期性檢查身份與應用程式的政策覆蓋缺口，產生修正建議並在管理者授權下套用變更。

因此，本文並不主張這些能力尚不存在，而提出下一步的統合命題：

$$
\boxed{
\text{Security Products}
\rightarrow
\text{Managed Security Capability}
\rightarrow
\text{Security Infrastructure}.
}
$$

最終，企業購買的可能不再是「某一套防毒軟體」，而是：

> **持續維持某個最低安全狀態的服務。**

---

**關鍵詞：** AI 資安、MDR、MSSP、SOC-as-a-Service、Security Agent、Agentic AI、數位免疫、常駐安全、Security Infrastructure、Managed Security

---

# 一、從「買工具」到「買安全能力」

傳統企業安全採購通常是：

$$
\text{Firewall}
+
\text{Antivirus}
+
\text{SIEM}
+
\text{IAM}
+
\text{Scanner}
+
\text{Backup}.
$$

每個產品解決一部分問題。

但是：

$$
\boxed{
\text{Security Tools}
\neq
\text{Security Capability}.
}
$$

買了 SIEM，

不代表有人看。

買了 EDR，

不代表有人能判斷事件。

買了漏洞掃描器，

不代表有人能決定：

> 哪一個漏洞先修？

因此真正的安全能力還需要：

$$
\text{Tool}
+
\text{Knowledge}
+
\text{Attention}
+
\text{Response}.
$$

---

# 二、MSSP 與 MDR 已經證明「資安可以外包」

Managed Security Service Provider：

$$
\text{MSSP}
$$

以及：

$$
\text{MDR}
=
\text{Managed Detection \& Response}
$$

本身就是一個重要歷史轉折。

它們已經證明：

> 一家公司不需要自己建立所有 24/7 資安能力。

CrowdStrike Falcon Complete 目前便以持續 MDR 形式提供 24/7 專家團隊、威脅獵捕、端點、雲端工作負載、身份威脅與事件修復能力。

Google Mandiant 亦把 Threat Defense 描述為覆蓋完整 security stack 的主動偵測、威脅搜索與快速回應服務，由 Mandiant 專家與 AI 共同運作。

所以：

$$
\boxed{
\text{Security Capability}
}
$$

本身早已可以成為服務。

---

# 三、問題是目前仍然太碎

即使採用 MDR，

企業仍可能需要另外處理：

- Password Manager；
- IAM；
- Cloud Security；
- AppSec；
- API Security；
- Backup；
- Vulnerability Management；
- SaaS Security；
- AI Agent Security；
- GRC。

於是：

$$
\text{Managed Security}
$$

仍然可能是一堆：

$$
S_1+S_2+\cdots+S_n.
$$

客戶自己負責整合。

這就產生一個很奇怪的情況：

> 最不懂資安的中小企業，反而要自己判斷到底缺什麼資安產品。

---

# 四、真正成熟的服務應該反過來

未來客戶真正需要回答的問題也許只有：

> 我有哪些資產？

> 哪些東西最重要？

> 我願意承擔多少風險？

剩下由平台自己決定：

$$
R=
\text{Required Security Capabilities}.
$$

也就是：

$$
\boxed{
\text{User buys outcomes;}
\quad
\text{provider manages capabilities}.
}
$$

這與雲端計算的歷史非常相似。

---

# 五、雲端沒有要求每家公司懂機房

企業使用：

$$
\text{Cloud Compute}
$$

時，

不需要自己理解：

- UPS；
- 機房散熱；
- 硬碟更換；
- 骨幹交換器；
- 實體機架。

它只需要說：

> 我要 Compute。

同樣地，

普通企業理論上不應該需要知道：

> 「我現在缺的是 Identity Threat Detection Engineer 還是 DFIR Analyst？」

它只需要：

$$
\boxed{
\text{I need to stay secure.}
}
$$

---

# 六、Security Capability Utility

因此本文提出：

# Security Capability Utility  
## 安全能力公用服務

其基本思想為：

$$
\boxed{
\text{Security Expertise}
\rightarrow
\text{On-Demand / Persistent Utility}.
}
$$

客戶不擁有所有專家。

而是擁有：

$$
\operatorname{Access}
(
\mathcal C_{\mathrm{security}}
).
$$

這直接延續第四篇的：

$$
C=
C_{\mathrm{internal}}
+
C_{\mathrm{external}}
+
C_{\mathrm{platform}}
+
C_{\mathrm{AI}}.
$$

---

# 七、從 MDR 向全域 Security Runtime

本文進一步提出：

$$
\boxed{
\text{MDR}
\rightarrow
\text{Security Runtime}.
}
$$

傳統 MDR 主要處理：

$$
\text{Detect}
+
\text{Respond}.
$$

未來 Security Runtime 則需要：

$$
\begin{aligned}
&\text{Observe}\\
&+\text{Prevent}\\
&+\text{Detect}\\
&+\text{Respond}\\
&+\text{Recover}\\
&+\text{Improve}.
\end{aligned}
$$

也就是不只等事件發生。

---

# 八、完整的常駐安全循環

本文定義：

$$
\boxed{
O
\rightarrow
M
\rightarrow
D
\rightarrow
P
\rightarrow
R
\rightarrow
V
\rightarrow
L
}
$$

其中：

### $O$ — Observe

收集必要安全狀態。

### $M$ — Model

建立組織安全模型。

### $D$ — Detect

發現異常與暴露。

### $P$ — Prioritize

計算真正風險。

### $R$ — Respond

採取行動。

### $V$ — Verify

確認問題真的解決。

### $L$ — Learn

把結果送回安全知識系統。

完成後重新：

$$
L\rightarrow O.
$$

形成持續閉環。

---

# 九、Local Security Agent

完整架構第一層為：

$$
A_L=\text{Local Security Agent}.
$$

存在於：

- PC；
- Server；
- Mobile；
- Edge；
- Local Network。

它可以負責：

$$
\text{Observe}
+
\text{Local Policy Enforcement}
+
\text{Immediate Response}.
$$

---

# 十、本地 AI 的特殊優勢

Local Security AI 可以直接取得：

$$
\text{Local Context}.
$$

例如：

- process tree；
- file changes；
- software inventory；
- device state；
- user activity；
- network behavior。

並且某些高度敏感資料可以保持：

$$
\boxed{
\text{Local Only}.
}
$$

這能減少全部安全資料都送往中央雲端的需求。

---

# 十一、Cloud Security Intelligence

第二層：

$$
A_C=\text{Cloud Security Intelligence}.
$$

雲端的價值不是單純：

> 模型比較大。

而是：

$$
\text{Cross-Organization Knowledge}
+
\text{Threat Intelligence}
+
\text{Historical Data}
+
\text{Expert Feedback}.
$$

Palo Alto Cortex XSIAM 目前便以中央資料層整合 endpoint、network、identity、cloud 等 telemetry，再使用 AI 進行關聯與優先排序。

---

# 十二、本地—雲端雙層安全

因此理想架構不是：

$$
\text{Everything to Cloud}.
$$

也不是：

$$
\text{Everything Local}.
$$

而是：

$$
\boxed{
A_L
\leftrightarrow
A_C.
}
$$

Local：

- 高敏感狀態；
- 即時反應；
- 離線安全；
- 客戶專屬上下文。

Cloud：

- 大模型；
- 全球情報；
- 跨組織模式；
- 專家資源；
- 大規模關聯。

---

# 十三、人類專家池

第三層：

$$
H=
\{
H_1,H_2,\ldots,H_n
\}.
$$

例如：

$$
H_{\mathrm{AppSec}},
$$

$$
H_{\mathrm{Cloud}},
$$

$$
H_{\mathrm{IAM}},
$$

$$
H_{\mathrm{DFIR}},
$$

$$
H_{\mathrm{Malware}},
$$

$$
H_{\mathrm{GRC}}.
$$

這些人不需要平均分配給每家公司。

---

# 十四、人力池化

假設：

$$
10^4
$$

家公司都自己養一名低利用率 DFIR 專家，

成本很高。

平台則可以維護：

$$
H_{\mathrm{DFIR}}^{pool}
$$

讓真正需要時才調用。

因此：

$$
\boxed{
\text{Expertise Ownership}
\rightarrow
\text{Expertise Pooling}.
}
$$

這是 Managed AI Security 很大的經濟優勢。

---

# 十五、AI 負責第一層分流

令安全事件：

$$
E_i.
$$

AI 首先計算：

$$
P(\text{Threat}\mid E_i).
$$

低風險事件：

$$
E_L
$$

自動完成。

不確定或重大事件：

$$
E_H
\rightarrow
H_j.
$$

因此：

$$
\boxed{
AI
=
\text{Security Triage Layer}.
}
$$

Microsoft 目前的 Phishing Triage Agent 已經在將大量重複性的釣魚郵件分類與調查工作轉交 AI，以減少 SOC 分析人員的人工 triage 負擔。

---

# 十六、但 AI 不應只有「建議模式」

若永遠：

$$
AI\rightarrow\text{Suggestion}
\rightarrow H
$$

所有事件仍需人看，

則：

$$
\text{Human Bottleneck}
$$

並沒有真正消失。

所以一定會逐漸出現：

$$
\boxed{
\text{Bounded Autonomous Response}.
}
$$

---

# 十七、有限自治，而非無限制 root

本文拒絕：

$$
AI
\rightarrow
\text{Unlimited Administrator}.
$$

而提出能力集合：

$$
\mathcal C_A
=
\{
c_o,c_r,c_c,c_v,c_m
\}.
$$

其中：

- $c_o$ ：Observe；
- $c_r$ ：Recommend；
- $c_c$ ：Contain；
- $c_v$ ：Revoke；
- $c_m$ ：Modify。

AI 依事件等級取得不同能力。

---

# 十八、風險分級自治

例如：

## Level 0

$$
\text{Observe Only}.
$$

## Level 1

$$
\text{Recommend}.
$$

## Level 2

$$
\text{Automatic Reversible Action}.
$$

例如暫時隔離。

## Level 3

$$
\text{Human Approval Required}.
$$

## Level 4

$$
\text{Multi-Party Approval}.
$$

例如涉及：

- 重要身份；
- production；
- 大規模 policy；
- critical infrastructure。

---

# 十九、可逆性是一個關鍵控制

定義：

$$
R(a)
$$

表示動作：

$$
a
$$

的可逆性。

若：

$$
R(a)\approx1,
$$

AI 可以得到較高自治權。

若：

$$
R(a)\approx0,
$$

則應提高：

$$
H_{\mathrm{approval}}.
$$

因此：

$$
\boxed{
\text{Autonomy}
\propto
\text{Reversibility}.
}
$$

---

# 二十、現有系統其實已開始採用這種思想

Palo Alto XSIAM 的 autonomous playbooks 已允許自動處理複雜 security operations，同時對需要人工批准的任務保留明確 approval 標記；平台也允許停用自治 playbook。

Microsoft Entra 的 Conditional Access Optimization Agent 則會持續尋找政策缺口、產生建議與修正，但政策改動仍依使用者角色與管理者批准控制；其 phased rollout 還可在部署造成登入成功率下降時停止推進。

這代表：

$$
\boxed{
\text{AI Autonomy}
+
\text{Human Governance}
}
$$

已經開始成為真實產品架構。

---

# 二十一、Security AI 本身會成為 Tier-0 Asset

如果 AI 可以：

- revoke token；
- isolate endpoint；
- rotate secrets；
- modify firewall；
- modify identity policy；

那麼：

$$
\boxed{
A_S
=
\text{Privileged Security Principal}.
}
$$

它可能比普通管理員更加敏感。

---

# 二十二、AI 污染問題

如果：

$$
A_S
$$

遭：

- prompt injection；
- model poisoning；
- credential compromise；
- tool compromise；
- malicious integration；

控制，

那麼原本的防禦能力可能轉換成：

$$
\boxed{
\text{Attack Amplifier}.
}
$$

因此：

$$
\text{Security AI Security}
$$

會成為新的資安子領域。

---

# 二十三、AI 不能直接相信外部輸入

常駐 Security Agent 本質上每天都會閱讀：

- email；
- web；
- logs；
- code；
- alerts；
- documents。

其中：

$$
\text{Untrusted Content}
$$

極多。

因此必須將：

$$
\boxed{
\text{Data Plane}
\neq
\text{Instruction Plane}.
}
$$

外部看到的文字不能自然取得：

$$
\text{Agent Authority}.
$$

---

# 二十四、Agent 權限必須最小化

現有 XSIAM Agentic Assistant 已使用 RBAC 分離 Agent 與 Action 權限，由管理者控制誰能建立、修改、啟用與使用相關能力。

這種架構應進一步發展為：

$$
\boxed{
\text{Capability-Based Security for Security AI}.
}
$$

即 AI 不得到：

$$
\text{root}
$$

而得到：

$$
\{c_1,c_2,\ldots,c_k\}.
$$

---

# 二十五、Security AI 需要第二個 AI 監督嗎？

這會產生一個有趣的問題。

主防禦 Agent：

$$
A_D.
$$

監督 Agent：

$$
A_G.
$$

則：

$$
A_G
\rightarrow
\operatorname{Audit}(A_D).
$$

例如：

- 判斷行動是否超權；
- 是否符合 policy；
- 是否有異常工具調用；
- 是否產生不可接受副作用。

形成：

$$
\boxed{
\text{AI Defense}
+
\text{AI Governance}.
}
$$

---

# 二十六、關鍵操作仍需要人類

所以未來完整模型不是：

$$
AI>Human.
$$

也不是：

$$
Human>AI.
$$

而是：

$$
\boxed{
AI_{\mathrm{scale}}
+
Human_{\mathrm{judgment}}.
}
$$

Google Mandiant 目前就明確將其 Threat Defense 模式描述為 human-led、AI-assisted：專家提供高階威脅判斷，AI 協助建立與執行威脅搜索。

---

# 二十七、Security Orchestrator

整個服務需要一個：

$$
A_O=\text{Security Orchestrator}.
$$

它不必是最懂 malware 的 Agent。

它的核心工作是：

$$
\boxed{
\text{Routing}.
}
$$

輸入：

$$
E.
$$

輸出：

$$
\arg\max_{C_j}
P(C_j\text{ can resolve }E).
$$

---

# 二十八、事件自動路由

例如：

$$
E_{\mathrm{identity}}
\rightarrow
A_{\mathrm{IAM}}.
$$

$$
E_{\mathrm{malware}}
\rightarrow
A_{\mathrm{Endpoint}}.
$$

$$
E_{\mathrm{code}}
\rightarrow
A_{\mathrm{AppSec}}.
$$

重大未知事件：

$$
E_X
\rightarrow
H_{\mathrm{IR}}.
$$

所以客戶完全不需要知道：

> 這是哪個職種？

---

# 二十九、這正好修補 Security Capability Coverage Gap

第四篇定義：

$$
G_{\mathrm{SCC}}
=
R-C.
$$

常駐管理式服務的真正商品其實就是：

$$
\boxed{
G_{\mathrm{SCC}}
\rightarrow0.
}
$$

它不是賣：

> 一個 AI chatbot。

而是賣：

> **補上你自己沒有的安全能力。**

---

# 三十、Credential Security 也應納入

第一篇建立：

$$
\text{Human Root}
+
\text{Machine Entropy}
+
\text{MFA}
+
\text{Recovery}.
$$

這些也不應是獨立世界。

完整 Security Runtime 應知道：

- 哪些帳號沒有 MFA；
- 哪些密碼重複；
- 哪些 passkey 尚未部署；
- 哪些 API secret 即將失效；
- 哪些 recovery path 過弱。

Microsoft Entra 的 Conditional Access Optimization Agent 現在已能持續評估使用者、應用與 Agent Identity 是否被 Conditional Access 覆蓋，並可以協助部署較強的身份安全政策與 passkey adoption。

這表示：

$$
\text{Credential Management}
$$

正在自然進入：

$$
\text{Continuous Security Management}.
$$

---

# 三十一、Application Security 也必須加入

如果企業使用：

$$
\text{AI Coding},
$$

則：

$$
\frac{dCode}{dt}\uparrow.
$$

Security Runtime 不能只在：

$$
\text{Production}
$$

才出現。

而要進入：

$$
\boxed{
\text{Code}
\rightarrow
\text{Build}
\rightarrow
\text{Deploy}
\rightarrow
\text{Runtime}.
}
$$

形成完整生命週期。

---

# 三十二、因此未來不是單一防毒軟體

完整系統可能成為：

$$
\boxed{
\mathcal S
=
(
S_C,
S_I,
S_E,
S_A,
S_N,
S_D,
S_R
)
}
$$

其中：

- $S_C$ ：Credential；
- $S_I$ ：Identity；
- $S_E$ ：Endpoint；
- $S_A$ ：Application；
- $S_N$ ：Network / Cloud；
- $S_D$ ：Data；
- $S_R$ ：Recovery。

這就是：

# Digital Immune Infrastructure

---

# 三十三、Security Runtime 的狀態模型

常駐 AI 不應每次從零開始。

令組織安全狀態：

$$
X_t.
$$

新事件：

$$
E_t.
$$

則：

$$
X_{t+1}
=
F(X_t,E_t,A_t).
$$

其中：

$$
A_t
$$

代表防禦行動。

也就是：

$$
\boxed{
\text{Security}
=
\text{Persistent State Machine}.
}
$$

而不是：

> 每一次 alert 都當成彼此無關的 ticket。

---

# 三十四、常駐的價值就在記住昨天

如果昨天：

> 某 endpoint 出現異常。

今天：

> 同一 identity 又發生異常。

下週：

> 某 SaaS token 被使用。

三件事可能不是：

$$
E_1,E_2,E_3.
$$

而是：

$$
\boxed{
E_1\rightarrow E_2\rightarrow E_3.
}
$$

所以安全 AI 的價值很大部分來自：

$$
\text{Longitudinal Memory}.
$$

---

# 三十五、這也是現有 AI SOC 平台正在靠近的方向

Palo Alto XSIAM 已將不同 telemetry 深度 stitching 到共同資料層，讓端點、身份、網路與 Cloud events 被整理為更完整的 case，而不是孤立 alert；其 Agentic AI 進一步使用 case context 規劃調查與處置。

因此：

$$
\boxed{
\text{Alert-Centric Security}
\rightarrow
\text{State-Centric Security}.
}
$$

已經具有明顯產業方向。

---

# 三十六、普通個人版本也成立

這套架構不一定只服務企業。

個人安全環境也逐漸包含：

$$
\text{PC}
+
\text{Phone}
+
\text{Email}
+
\text{Cloud}
+
\text{Passwords}
+
\text{Banking}
+
\text{Smart Home}.
$$

普通人不可能自己理解所有安全問題。

所以可以存在：

# Personal Security Guardian

---

# 三十七、個人用戶真正需要的是結果

使用者不需要看到：

```text
OAuth scope anomaly detected.
```

而可以看到：

> 一個你很少使用的服務取得了新的帳號權限。

> 我建議撤銷。

或：

> 這不是你平常使用的裝置。

> 我已暫時鎖定高風險登入。

也就是：

$$
\text{Technical Complexity}
\rightarrow
\text{Actionable Decision}.
$$

---

# 三十八、Security AI 會逐漸成為代理人

所以：

$$
\text{Antivirus}
$$

最終可能只是：

$$
\mathcal S
$$

的一個子功能。

真正產品是：

$$
\boxed{
\text{Security Agent}
}
$$

代表使用者持續處理其數位安全事務。

---

# 三十九、但代理權與主權必須分離

即使委託安全服務，

仍應保持：

$$
\boxed{
\text{Delegation}
\neq
\text{Sovereignty Transfer}.
}
$$

客戶必須保留：

- key ownership；
- emergency override；
- audit access；
- provider revocation；
- export capability。

否則 Security Provider 會成為新的數位主權中心。

---

# 四十、服務商本身成為超高價值目標

若平台保護：

$$
N
$$

家公司，

攻破平台可能影響：

$$
N
$$

家公司。

所以：

$$
V_{\mathrm{provider}}
\propto N.
$$

形成：

$$
\boxed{
\text{Security Concentration Risk}.
}
$$

---

# 四十一、中央防禦增益悖論

可以表示：

$$
\text{Centralization Gain}
\Rightarrow
\begin{cases}
\text{Defense Amplification}\\
\text{Compromise Amplification}
\end{cases}
$$

這和既有 AI Hacker／具身攻擊研究中「中央智能越強，中央失陷後的放大效應也越大」完全同構。

---

# 四十二、所以不能有萬能中央 root

應採：

$$
\text{Split Authority}.
$$

例如：

$$
A_C
$$

知道威脅，

但不持有完整明文 key。

$$
A_L
$$

持有執行能力，

但受到 local policy 約束。

重大行動還需要：

$$
H.
$$

形成：

$$
\boxed{
A_C+A_L+H.
}
$$

---

# 四十三、客戶自己的 Local Policy 是最後防線

即使雲端 AI 發送：

$$
a.
$$

本地端仍計算：

$$
Allow(a)
=
P_L(a,X_t).
$$

若：

$$
Allow(a)=0,
$$

則不執行。

這意味著：

$$
\boxed{
\text{Cloud Intelligence}
\neq
\text{Unconditional Authority}.
}
$$

---

# 四十四、平台的真正 KPI 也會改變

傳統安全產品容易宣傳：

- alerts detected；
- malware blocked；
- CVEs found。

但管理式數位免疫真正應看：

$$
\text{MTTD}
$$

$$
\text{MTTR}
$$

$$
\text{Exposure Time}
$$

$$
\text{Capability Coverage}
$$

$$
\text{Residual Risk}.
$$

甚至：

$$
\boxed{
B_{\mathrm{sys}}(t)
}
$$

也就是第二篇定義的最低有效攻擊成本。

---

# 四十五、服務商的工作是持續抬高 $B_{\mathrm{sys}}$

最終：

$$
\boxed{
\max_D
\min_{p\in\mathcal P}
C(p\mid D).
}
$$

Security Runtime 的目標不是：

> 找最多漏洞。

而是：

> **持續使最便宜的有效攻擊路徑變貴。**

這是整個系列到目前為止最重要的統合。

---

# 四十六、服務等級可以自然形成

未來可能有：

## Basic

$$
AI_{\mathrm{observe}}
+
AI_{\mathrm{recommend}}.
$$

## Managed

$$
AI
+
24/7\ Human\ Escalation.
$$

## Advanced

$$
AI
+
SOC
+
IR
+
Cloud
+
Identity.
$$

## Critical

$$
AI
+
Dedicated\ Experts
+
Split\ Authority
+
High\ Assurance.
$$

而後續還能再加入：

$$
\text{Insurance / Compensation}.
$$

---

# 四十七、這會重新定義資安公司的商業模式

今天公司可能賣：

> License。

未來賣：

$$
\boxed{
\text{Security Outcome Subscription}.
}
$$

客戶支付：

$$
P_{\mathrm{month}}.
$$

平台承擔：

- AI inference；
- telemetry；
- expert pool；
- incident handling；
- continuous updates。

所以產品越來越接近：

$$
\boxed{
\text{Security Operations Utility}.
}
$$

---

# 四十八、可證偽命題

## 命題一：AI First-Line 可以大幅降低人工事件量

令：

$$
N_E
$$

為全部 security events。

人類實際處理：

$$
N_H.
$$

若：

$$
\frac{N_H}{N_E}
\downarrow
$$

且 missed-critical-event rate 不顯著上升，

則支持 AI First-Line 模型。

---

## 命題二：能力池化降低 SME 的完整安全成本

比較：

$$
C_{\mathrm{internal}}
$$

與：

$$
C_{\mathrm{managed}}.
$$

在相同：

$$
CCR
$$

下，

若：

$$
C_{\mathrm{managed}}
<
C_{\mathrm{internal}},
$$

則 Managed Security Infrastructure 具有明確規模經濟。

---

## 命題三：持續安全模型優於週期稽核

比較：

$$
T_{\mathrm{exposure}}
$$

在：

- quarterly review；
- continuous observation；

兩組中的差異。

預測：

$$
T_{\mathrm{continuous}}
<
T_{\mathrm{periodic}}.
$$

---

## 命題四：Local + Cloud 優於純中央模型

在相同偵測效果下測量：

$$
D_{\mathrm{uploaded}},
$$

$$
T_{\mathrm{response}},
$$

$$
R_{\mathrm{offline}}.
$$

如果雙層架構兼具：

- 較低資料集中；
- 較快本地反應；
- 較強全球情報；

則支持：

$$
A_L+A_C
$$

架構。

---

## 命題五：自治安全必須受到能力與可逆性限制

比較：

$$
A_{\mathrm{unbounded}}
$$

與：

$$
A_{\mathrm{bounded}}.
$$

測量：

- false positive damage；
- privilege abuse；
- recovery time。

預期：

$$
A_{\mathrm{bounded}}
$$

具有較好的整體安全—自治平衡。

---

# 四十九、研究限制

本文不主張：

1. AI 已能取代完整 SOC；
2. 所有企業都應外包安全；
3. MDR 已經等於本文提出的完整 Security Runtime；
4. AI 應取得無限制管理權；
5. 所有安全資料都應上傳中央雲端；
6. Security-as-a-Service 可以消除客戶自身責任；
7. AI 防禦可以保證零失陷。

本文真正提出的是：

$$
\boxed{
\text{Security Capability 可以被平台化、池化與持續提供。}
}
$$

而 AI 使這種服務的邊際成本開始下降。

---

# 五十、結論：從企業職能到數位基礎設施

過去：

$$
\text{Security}
=
\text{Internal IT Function}.
$$

再後來：

$$
\text{Security}
=
\text{Products}.
$$

接著出現：

$$
\text{MSSP / MDR}.
$$

而 AI Agent、統一 security data platform、持續 telemetry 與專家池的結合，正在使下一個階段變得可以想像：

$$
\boxed{
\text{Security}
=
\text{Persistent Infrastructure}.
}
$$

此時企業不再主要購買：

> 一套防毒。

> 一套 SIEM。

> 一套漏洞掃描器。

而是購買：

$$
\boxed{
\text{持續存在的安全能力。}
}
$$

服務商則負責：

$$
\text{Machine Scale}
+
\text{Expert Judgment}
+
\text{Continuous State}.
$$

於是：

$$
\boxed{
\text{AI}
\rightarrow
\text{First-Line Security Operator}
}
$$

而：

$$
\boxed{
\text{Human}
\rightarrow
\text{Escalation + Governance + Novel Judgment}.
}
$$

這不是「AI 取代資安人」。

而是：

$$
\boxed{
\text{AI 改變資安人力的配置方式。}
}
$$

企業也不必再解決：

> 「我要去哪裡找到十種不同資安人才？」

因為安全服務本身負責：

$$
\boxed{
\text{Capability Routing}.
}
$$

因此，本系列從第一篇到第六篇已經完成：

$$
\text{Password}
$$

$$
\downarrow
$$

$$
\text{Attack Path}
$$

$$
\downarrow
$$

$$
\text{Attacker Capability}
$$

$$
\downarrow
$$

$$
\text{Defender Capability Gap}
$$

$$
\downarrow
$$

$$
\text{Attention Scarcity Collapse}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Persistent Managed AI Security Infrastructure}.
}
$$

然而，當大量公司開始把安全交給少數平台之後，

下一個問題立即出現：

> **哪一家平台會比較強？**

答案可能不只是：

> 誰的 AI 模型最好。

因為模型可以更換。

真正難複製的是：

$$
\boxed{
\text{多年安全事件}
+
\text{全球 Threat Telemetry}
+
\text{攻擊鏈}
+
\text{專家修正}
+
\text{實際處置結果}.
}
$$

因此下一篇將進入：

# 《安全資料網路效應》
## Threat Graph、專家回饋與 AI 資安平台的資料護城河

其核心問題是：

> **當 AI 資安逐漸成為基礎設施後，真正決定平台能力的會不會不再是模型，而是誰擁有最大、最長期、最有回饋閉環的安全世界資料？**

---

## 參考資料

1. Palo Alto Networks, *Cortex XSIAM Documentation*, 2026。XSIAM 將 SIEM、XDR、SOAR、ASM、Threat Intelligence 與 Cloud Security 等功能整合於中央資料與 AI 平台，並加入 Agentic AI 進行調查及處置。  
2. Palo Alto Networks, *Resolving cases with AI*。Agentic Assistant 可使用 case context 規劃、推理、執行調查與相關 action。  
3. Palo Alto Networks, *Autonomous Playbooks*。平台允許管理式自治 playbook 執行 security operations，並對部分任務保留人工批准機制。  
4. Palo Alto Networks, *Agentic Assistant Security / Permissions*。XSIAM 使用 RBAC 控制 Agent 與相關 Action 權限。  
5. CrowdStrike, *Falcon Complete MDR*。其服務結合 AI-native Falcon 平台與 24/7 全球安全專家，涵蓋端點、Cloud workload、Identity、threat hunting 與 remediation。  
6. Google Cloud, *Mandiant Threat Defense*。目前採取 human-led、AI-assisted 的主動偵測、威脅搜索與快速回應服務。  
7. Microsoft, *Security Copilot Agents*. Security Copilot Agent 已逐步嵌入 Defender、Entra、Intune 與 Purview 等安全工作流。  
8. Microsoft, *Conditional Access Optimization Agent*, 2026。Agent 可持續分析身份與應用程式 Conditional Access 覆蓋情況、提出新政策或修改建議，並支援受管理者控制的修正。  
9. Microsoft, *Conditional Access Optimization Agent phased rollout*。提供逐階段部署與安全停止機制，讓 AI 政策管理保留可觀察與人工控制。  
10. Microsoft, *Phishing Triage Agent*. AI Agent 已用於協助 SOC 大規模處理使用者回報的可疑郵件與重複性分析工作。