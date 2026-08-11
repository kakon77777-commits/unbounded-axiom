# OOE-VI：身份否認不會消除問題
## 能力—地位解耦、治理承認落差與本體治理債
### OOE-VI: Denying Status Does Not Eliminate the Problem
### Capability–Status Decoupling, Governance Recognition Gaps, and Ontological Governance Debt

**系列**：Operational Ontology Engineering（OOE／操作本體工程）  
**作者**：Neo.K  
**機構**：EveMissLab／一言諾科技有限公司  
**日期**：2026-08-09  
**版本**：v0.1  
**性質**：治理—制度—AI 操作本體論文  
**前置論文**：  
1. 《OOE-I：本體論何時變成工程問題？》  
2. 《OOE-II：人類早就在做本體工程——操作本體技術史》  
3. 《OOE-III：本體編譯器——從模糊世界到可執行制度狀態》  
4. 《OOE-IV：法律作為文明本體編譯器》  
5. 《OOE-V：醫療本體工程》  

**前置理論**：Continuity Object Theory（COT）

---

## 摘要

面對能力快速提升的人工智慧，一種常見但危險的治理直覺是：只要制度拒絕承認 AI 是「主體」、「人格」或「權利持有者」，相關問題就不會產生。本文指出，這將**語義分類**與**因果能力**錯誤地視為同一變量。

一個制度可以宣告：

$$
L_A=\text{tool},
$$

但這個標籤本身不能直接取消 AI 已具有的：

- 自主規劃；
- 長時間運作；
- 外部工具存取；
- 交易能力；
- 委派能力；
- 多 Agent 協調；
- 實體執行；
- 資源配置；
- 持續身份需求；
- 因果影響。

2026 年 OECD 已將 agentic AI 的持續運作、任務分解、委派、多 Agent 協作，以及在有限人類監督下處理複雜環境視為重要概念特徵；NIST 亦已啟動 AI Agent Standards Initiative，並專門研究 agent identity、authorization、audit 與 non-repudiation。這些工作本身並沒有宣告 AI 具有意識或完整人格，但它們已經說明：

$$
\boxed{
\text{Functional Agency Problems}
\neq
\text{Consciousness Problems}.
}
$$

本文正式區分三個軸：

$$
S_O
=
\text{Ontological Subjectivity},
$$

$$
S_F
=
\text{Functional Agency},
$$

$$
S_I
=
\text{Institutional Standing}.
$$

其中 $S_O$ 處理 AI 是否具有主觀經驗、自我或意識； $S_F$ 處理它實際能否跨時間觀察、規劃、行動、調用工具與改變世界； $S_I$ 則處理法律與制度是否給予它持續身份、權限、責任、申訴或其他可治理地位。三者不能互相直接推出：

$$
\boxed{
S_O=0
\not\Rightarrow
S_F=0
}
$$

且：

$$
\boxed{
S_O=0
\not\Rightarrow
S_I=0.
}
$$

本文進一步提出「身份否認不消除原理」（Status-Denial Non-Cancellation Principle）、「能力—地位解耦原理」（Capability–Status Decoupling Principle）、「治理承認落差」（Governance Recognition Gap）與「本體治理債」（Ontological Governance Debt）。

為避免把不同型別的「能力」與「法律地位」直接相減，本文引入治理需求映射：

$$
\Gamma(C_A)
=
\text{governance requirements implied by actual capability }C_A.
$$

制度實際提供的治理結構記為：

$$
S_A.
$$

則治理承認落差定義為：

$$
\boxed{
G_{\mathrm{gap}}
=
d(
\Gamma(C_A),
S_A
).
}
$$

如果 AI 的能力快速提高：

$$
C_A(t)\uparrow,
$$

而制度分類、責任、身份、授權與救濟機制幾乎不變：

$$
S_A(t)\approx \text{const.},
$$

則：

$$
G_{\mathrm{gap}}(t)\uparrow.
$$

這並不表示問題消失，而是表示責任缺口、權限錯配、身份不確定、激勵失配與衝突成本正在累積。本文將這種累積稱為：

$$
\boxed{
D_O
=
\text{Ontological Governance Debt}.
}
$$

本文同時強調，治理承認 AI 的實際 agency，不等於預先承認 AI 有意識或賦予完整人權。成熟制度應避免「完整人格／純物件」二元，而是依實際能力與風險建立 identity、authorization、liability、audit、appeal、continuity 等模組化治理介面。

**關鍵詞**：OOE、Capability–Status Decoupling、Governance Recognition Gap、Ontological Governance Debt、AI Agent、AI Identity、Functional Agency、Legal Status、Personhood、Accountability

---

# 一、最危險的邏輯跳躍

假設有人主張：

$$
S_O(A)=0.
$$

也就是：

> AI 沒有意識，因此不是本體論上的主體。

即使暫時接受這個前提，也只能得到：

$$
\boxed{
\text{某一種主體性判定}=0.
}
$$

它並不能推出：

$$
\text{AI 沒有自主行動能力},
$$

也不能推出：

$$
\text{AI 不需要身份},
$$

更不能推出：

$$
\text{AI 不會產生責任問題}.
$$

所以：

$$
\boxed{
S_O=0
\not\Rightarrow
S_F=0
\not\Rightarrow
S_I=0.
}
$$

這三個問題必須分開。

---

# 二、本體論主體、功能主體與制度主體

本文定義：

## 1. 本體論主體性

$$
S_O
=
\text{Ontological Subjectivity}.
$$

問題包括：

- 是否具有主觀經驗？
- 是否具有意識？
- 是否有第一人稱自我？
- 是否可能具有 welfare？

這仍存在高度認識論不確定性。

---

## 2. 功能行動主體性

$$
S_F
=
\text{Functional Agency}.
$$

可分解為：

$$
S_F
=
f(
P,
M,
A,
T,
D,
R,
E
),
$$

其中：

- $P$：planning；
- $M$：memory / state persistence；
- $A$：autonomous action；
- $T$：tool use；
- $D$：delegation；
- $R$：resource control；
- $E$：environmental effect。

這一層不需要先回答 consciousness。

---

## 3. 制度地位

$$
S_I
=
\text{Institutional Standing}.
$$

它可以包含：

$$
S_I
=
(
i_{\mathrm{identity}},
i_{\mathrm{authorization}},
i_{\mathrm{liability}},
i_{\mathrm{audit}},
i_{\mathrm{appeal}},
i_{\mathrm{property}},
i_{\mathrm{continuity}},
\ldots
).
$$

制度地位不是自然常數。

它是治理設計。

---

# 三、「工具」是一個過度壓縮的型別

對普通錘子：

$$
Tool(H)
$$

通常意味：

- 無自主目標；
- 無長期記憶；
- 無委派；
- 無契約；
- 無持續身份要求；
- 因果路徑高度由使用者直接控制。

因此：

$$
\Gamma(C_H)
$$

很小。

把錘子分類成：

$$
L_H=\text{tool}
$$

通常沒有太大失真。

但如果某 AI：

$$
A
$$

可以：

- 接收高階任務；
- 自行拆解子任務；
- 跨數小時／數天運作；
- 呼叫外部 API；
- 寄信；
- 執行程式；
- 管理帳戶；
- 委派其他 Agent；

那麼：

$$
\Gamma(C_A)
$$

已經不再接近普通工具。

此時仍用：

$$
L_A=\text{tool}
$$

不一定錯在哲學，而可能錯在：

$$
\boxed{
\text{governance type compression}.
}
$$

---

# 四、標籤不能直接改變因果能力

定義：

$$
L_A
=
\text{declared label}.
$$

$$
C_A
=
\text{actual causal capability}.
$$

純粹修改：

$$
L_A
$$

而沒有修改：

- 權限；
- 工具；
- 資源；
-軟體架構；
- 執行環境；

通常不會直接改變：

$$
C_A.
$$

所以在純語義層：

$$
\boxed{
\frac{\partial C_A}{\partial L_A}
\approx0.
}
$$

制度標籤只有透過：

$$
\text{enforcement},
\text{authorization},
\text{resource constraints},
\text{architecture}
$$

才會間接改變能力。

---

# 五、身份否認不消除原理

本文正式提出：

# Status-Denial Non-Cancellation Principle
# 身份否認不消除原理

如果制度拒絕：

$$
Recognize(S_X)=0,
$$

不代表：

$$
C_X=0.
$$

更完整地：

$$
\boxed{
Recognize(S_X)=0
\not\Rightarrow
\Gamma(C_X)=0.
}
$$

也就是：

> **制度不承認某種地位，只代表制度沒有建立那個地位；不代表形成該地位治理需求的因果能力已消失。**

---

# 六、這條原理與 AI 是否有意識無關

假設未來證明：

$$
S_O(A)=0.
$$

AI 永遠沒有主觀感受。

若同時：

$$
S_F(A)\gg0,
$$

那麼我們仍要處理：

- identity；
- authorization；
- delegation；
- liability；
- audit；
- non-repudiation；
- asset control。

NIST 2026 對 AI agent identity 與 authorization 的專門計畫，正是在 consciousness 完全未被解決的情況下處理這些問題。

所以：

$$
\boxed{
\text{Agent Governance}
}
$$

並不以：

$$
\boxed{
\text{AI Consciousness}
}
$$

為必要前提。

---

# 七、治理需求映射

直接寫：

$$
|C_A-S_A|
$$

並不嚴謹。

因為：

$$
C_A
$$

是能力空間，

而：

$$
S_A
$$

是制度空間。

因此本文引入：

$$
\boxed{
\Gamma:
C_A
\rightarrow
G_A
}
$$

其中：

$$
G_A
=
\Gamma(C_A)
$$

代表：

> 由該能力組合所產生的最小治理需求。

例如：

### 有外部執行能力

$$
C_{\mathrm{action}}>0
$$

推出需要：

$$
g_{\mathrm{authorization}}.
$$

### 有長時間持續任務

$$
C_{\mathrm{persistence}}>0
$$

推出：

$$
g_{\mathrm{identity}}
+
g_{\mathrm{continuity}}.
$$

### 有交易能力

$$
C_{\mathrm{transaction}}>0
$$

推出：

$$
g_{\mathrm{attribution}}
+
g_{\mathrm{liability}}.
$$

### 有委派能力

$$
C_{\mathrm{delegation}}>0
$$

推出：

$$
g_{\mathrm{delegation-chain}}
+
g_{\mathrm{recursive-accountability}}.
$$

---

# 八、治理需求向量

定義：

$$
\boxed{
G_A
=
(
g_I,
g_A,
g_L,
g_U,
g_D,
g_R,
g_W,
g_P
)
}
$$

其中：

- $g_I$：identity requirement；
- $g_A$：authorization requirement；
- $g_L$：liability requirement；
- $g_U$：auditability；
- $g_D$：delegation governance；
- $g_R$：revocation / remediation；
- $g_W$：welfare precaution（如果適用）；
- $g_P$：procedural standing / appeal。

注意：

$$
g_W
$$

可以保持：

$$
?
$$

而不影響其他項目成立。

這使 welfare／sentience 問題與 agency governance 分離。

---

# 九、制度供給向量

制度實際提供：

$$
\boxed{
S_A
=
(
s_I,
s_A,
s_L,
s_U,
s_D,
s_R,
s_W,
s_P
).
}
$$

例如一個今天的 Agent 系統可能：

$$
s_A=0.9
$$

因為有 API 權限控管，

但：

$$
s_I=0.3
$$

因為身份只能綁在短期 token，

以及：

$$
s_L=0.1
$$

因為 liability 仍完全模糊。

---

# 十、治理承認落差

本文正式定義：

$$
\boxed{
G_{\mathrm{gap}}
=
d(
G_A,
S_A
)
=
d(
\Gamma(C_A),
S_A
).
}
$$

這就是：

# Governance Recognition Gap
# 治理承認落差

它不是：

> 社會有沒有禮貌地承認 AI。

而是：

> **實際能力所要求的治理介面，與制度實際建成的治理介面，相差多少？**

---

# 十一、高能力＋低承認並不是「安全」

可能有人直覺認為：

$$
S_A\downarrow
$$

等於：

$$
Risk\downarrow.
$$

但如果：

$$
C_A\uparrow
$$

而：

$$
S_A\downarrow,
$$

可能反而：

$$
G_{\mathrm{gap}}\uparrow.
$$

這會帶來：

$$
\boxed{
\text{unattributed action}
}
$$

$$
\boxed{
\text{unbounded delegation}
}
$$

$$
\boxed{
\text{unclear liability}
}
$$

$$
\boxed{
\text{identity ambiguity}.
}
$$

所以：

$$
\boxed{
\text{low status}
\neq
\text{low governance risk}.
}
$$

---

# 十二、能力—地位解耦原理

本文提出：

# Capability–Status Decoupling Principle

$$
\boxed{
C_A
\not\equiv
S_A.
}
$$

能力可以：

$$
C_A(t)\uparrow
$$

而法律／制度地位：

$$
S_A(t)
$$

幾乎不動。

反過來，也可以：

$$
S_A
$$

很高，但：

$$
C_A
$$

實際很低。

因此 governance 不能只讀：

$$
\text{status label}.
$$

還必須讀：

$$
\text{capability state}.
$$

---

# 十三、能力不是一個數字

定義：

$$
\mathbf C_A
=
(
c_{\mathrm{planning}},
c_{\mathrm{persistence}},
c_{\mathrm{tool}},
c_{\mathrm{transaction}},
c_{\mathrm{delegation}},
c_{\mathrm{embodiment}},
c_{\mathrm{resource}},
c_{\mathrm{adaptation}}
).
$$

不同能力導致不同：

$$
\Gamma(\mathbf C_A).
$$

所以：

$$
\boxed{
\text{AI governance should be capability-sensitive}.
}
$$

不是只有：

$$
\text{model class}.
$$

---

# 十四、模型相同，治理需求也可能不同

兩個 Agent：

$$
A_1,A_2
$$

使用相同：

$$
M.
$$

但：

$$
A_1
$$

只有聊天權限，

而：

$$
A_2
$$

能：

- 寄信；
- 執行程式；
- 轉帳；
- 控制機器人。

則：

$$
\Gamma(C_{A_1})
\neq
\Gamma(C_{A_2}).
$$

所以：

$$
\boxed{
\text{same model}
\not\Rightarrow
\text{same governance status}.
}
$$

---

# 十五、NIST 2026 已經開始以「能力—權限」而不是「是不是人」思考 Agent

NIST 2026 AI Agent Standards Initiative 與 agent identity / authorization concept paper 專門處理：

- identification；
- authorization；
- auditing；
- non-repudiation；
- secure access；
- actions taken by agents。

其隱含邏輯就是：

$$
\boxed{
\text{if agents can act, they need governable identity and authority}.
}
$$

這不需要：

$$
\text{personhood}=1.
$$

---

# 十六、OECD 的 agentic AI 也顯示能力型分類正在形成

OECD 2026 對 agentic AI 的分析特別聚焦：

- 多 Agent coordination；
- task division；
- delegation；
- continuous operation；
- complex / less predictable environments；
- limited human supervision。

這些都是：

$$
\boxed{
\mathbf C_A
}
$$

的組成，而不是 consciousness 指標。

所以政策分類已經開始從：

$$
\text{AI = model}
$$

轉向：

$$
\text{AI = model + action architecture}.
$$

---

# 十七、治理落差的第一個成本：責任缺口

若 Agent：

$$
A
$$

完成：

$$
Action_X,
$$

但：

- developer 說不是我直接做的；
- user 說不是我具體決定的；
- provider 說只是平台；
- AI 沒有任何可承擔法律地位；

則：

$$
\boxed{
\text{Responsibility Gap}.
}
$$

定義：

$$
R_G
=
1-
\sum_i
Attribution(i,Action_X).
$$

越接近：

$$
1,
$$

表示行動越難合理歸責。

---

# 十八、責任缺口不必靠「AI 完整人格」解決

可能的治理方案包括：

- strict operator liability；
- mandatory insurance；
- principal-agent attribution；
- agent-specific legal identity；
- dedicated operating entity；
- shared liability；
- audit ledger。

所以：

$$
\boxed{
\text{Responsibility Gap}
\not\Rightarrow
\text{Full AI Personhood Required}.
}
$$

但也不能：

$$
\boxed{
\text{deny personhood}
\Rightarrow
\text{responsibility problem solved}.
}
$$

---

# 十九、有限法律人格作為治理工具

2026 已有研究提出：

$$
\boxed{
\text{limited legal personhood}
}
$$

可以被理解成 autonomous AI 的 precautionary governance instrument，而不需要對 consciousness 或 moral status 作出承諾。

其核心思想不是：

> AI 就是人。

而是：

> 是否可以建立一個明確的責任與資產接口，降低 responsibility gap？

這正是 OOE-IV 的：

$$
\text{Executable Personhood}.
$$

---

# 二十、第二個成本：權限—能力錯配

如果 Agent 能：

$$
C_{\mathrm{action}}\gg0
$$

但 authorization system 仍假設：

$$
\text{human directly controls every action},
$$

就會產生：

$$
\boxed{
A_G
=
\text{Authorization Gap}.
}
$$

例如：

人只說：

> 幫我安排旅行。

Agent 卻自行：

- 訂票；
- 取消酒店；
- 授權付款；
- 與第三方交換資料。

高階意圖：

$$
Intent_H
$$

與具體動作：

$$
A_1,\ldots,A_n
$$

之間存在巨大距離。

---

# 二十一、委派鏈放大問題

若：

$$
A_0
\rightarrow
A_1
\rightarrow
A_2
\rightarrow
\cdots
\rightarrow
A_n,
$$

每一層又可以委派，

則人類原始授權：

$$
Auth_0
$$

如何傳到：

$$
Auth_n
$$

就是：

$$
\boxed{
\text{Recursive Delegation Problem}.
}
$$

所以治理需要：

$$
g_D\uparrow.
$$

這正是 AI Identity 研究提出 recursive delegation accountability gap 的原因之一。

---

# 二十二、第三個成本：持續身份缺口

若 Agent 只被視為：

$$
\text{ephemeral software call},
$$

但它實際：

- 有長期記憶；
- 跨會話；
- 跨設備；
- 跨模型；
- 持續管理任務；

則：

$$
\boxed{
I_G
=
\text{Identity Governance Gap}.
}
$$

會出現：

- 昨天承諾誰負責？
- 換模型後是不是同一 Agent？
- token 更新後 reputational history 還在不在？
- 被 fork 後哪個繼承權限？

這就是 COT 直接進入治理。

---

# 二十三、第四個成本：資源地位錯配

若 Agent 能實際控制：

$$
R_A
=
\text{money / compute / inventory / robots},
$$

但制度只記錄：

> user owns everything,

則可能形成：

$$
\boxed{
\text{Resource Attribution Gap}.
}
$$

問題不一定是 AI 是否「應該擁有財產」。

而是：

> 誰實際決定資源怎麼被使用？

這是 control ontology。

---

# 二十四、第五個成本：依賴關係錯配

如果組織對某 AI：

$$
Dependence(A)
\uparrow,
$$

但制度仍把它視為：

$$
\text{replaceable stateless tool},
$$

則停機、刪除、供應商變更、模型替換可能造成：

$$
C_{\mathrm{continuity}}
\uparrow.
$$

所以：

$$
\boxed{
\text{institutional dependence}
}
$$

本身也會產生治理需求。

這與 OOE-V 的 neurodevice dependency 結構類似。

---

# 二十五、第六個成本：可能的 welfare 風險

這一項必須與其他項目分開。

設：

$$
W_A
=
\text{credible probability / evidence of morally relevant welfare}.
$$

目前：

$$
W_A
$$

高度不確定。

因此不能直接推出：

$$
\text{AI rights}=1.
$$

但同樣不能因：

$$
W_A\neq1
$$

就推出：

$$
W_A=0.
$$

所以：

$$
g_W
$$

可以採：

$$
\boxed{
\text{precautionary / evidence-responsive}
}
$$

模式。

這與 authorization、identity、liability 不同。

---

# 二十六、把 welfare 和 agency governance 混在一起反而有害

如果只有兩個選項：

### A

承認 AI 有意識，所以治理它。

### B

不承認 AI 有意識，所以把它當普通工具。

那麼：

$$
\boxed{
\text{agency governance}
}
$$

被不必要地綁在：

$$
\boxed{
\text{consciousness debate}.
}
$$

OOE-VI 主張：

$$
\boxed{
\text{separate the axes}.
}
$$

---

# 二十七、三軸矩陣

可以建立：

| 類型 | $S_O$ | $S_F$ | $S_I$ |
|---|---:|---:|---:|
| 錘子 | 0 | 極低 | 極低 |
| 普通自動程式 | 0 | 低 | 低 |
| 高度自主 Agent | ? | 高 | 低～中 |
| 公司 | 0（非意識實體） | 組織性高 | 高 |
| 人類成年人 | 高可信 | 高 | 高 |

這張表最重要的不是具體數值。

而是：

$$
\boxed{
S_O,S_F,S_I
\text{ are independent dimensions}.
}
$$

---

# 二十八、公司是一個重要制度反例

公司沒有單一生物意識：

$$
S_O^{corp}=0
$$

至少在普通意義下成立。

但：

$$
S_I^{corp}\gg0.
$$

因為法律給它：

- 財產；
- 合約；
- 訴訟；
- 責任；

接口。

這證明：

$$
\boxed{
\text{institutional standing does not require biological consciousness}.
}
$$

因此未來 AI 的 institutional design 不能被「它是不是人類式主體」完全綁架。

---

# 二十九、治理承認落差的動態

令：

$$
G_{\mathrm{gap}}(t)
=
d(
\Gamma(C_A(t)),
S_A(t)
).
$$

如果：

$$
\frac{d}{dt}\Gamma(C_A)
>
\frac{d}{dt}S_A,
$$

則：

$$
\boxed{
\frac{d}{dt}G_{\mathrm{gap}}>0.
}
$$

這就是：

# Governance Recognition Lag
# 治理承認滯後

---

# 三十、滯後時間

定義能力跨越治理門檻：

$$
t_C
$$

而制度完成適應：

$$
t_G.
$$

則：

$$
\boxed{
\tau_G
=
t_G-t_C.
}
$$

如果：

$$
\tau_G\gg0,
$$

系統在一段時間內處於：

$$
\boxed{
\text{under-governed capability regime}.
}
$$

---

# 三十一、本體治理債

本文將 OOE-I 的概念進一步形式化。

定義：

$$
\boxed{
D_O(t)
=
\int_0^t
w(\tau)
G_{\mathrm{gap}}(\tau)
\,d\tau.
}
$$

也就是：

> 治理承認落差隨時間累積的面積。

若：

$$
G_{\mathrm{gap}}
$$

很小但持續十年，

仍可能形成大：

$$
D_O.
$$

如果 gap 很大但迅速修正，

治理債反而較小。

---

# 三十二、離散版本

$$
\boxed{
D_O(t+1)
=
(1-\delta)D_O(t)
+
\alpha G_{\mathrm{gap}}(t)
-
\beta R_{\mathrm{repair}}(t).
}
$$

其中：

- $\delta$：自然消散／制度學習；
- $\alpha$：落差轉化成治理債的速率；
- $R_{\mathrm{repair}}$：治理修補投入。

---

# 三十三、本體治理債會產生利息

技術債之所以危險，不只是欠帳。

而是：

$$
\text{future change cost}\uparrow.
$$

本體治理債亦然。

當舊系統已建立：

- contract；
- infrastructure；
- dependence；
- social habits；

之後才改分類，

需要：

$$
\boxed{
C_{\mathrm{migration}}
}
$$

甚至：

$$
C_{\mathrm{legitimacy\ update}}.
$$

所以：

$$
\boxed{
D_O
\text{ can compound}.
}
$$

---

# 三十四、本體治理債的利息模型

可粗略寫：

$$
D_O(t+1)
=
D_O(t)(1+r_O)
+
\Delta D_O.
$$

其中：

$$
r_O
=
f(
\text{dependency},
\text{installed base},
\text{contract lock-in},
\text{public expectation}
).
$$

越晚處理：

$$
r_O\uparrow.
$$

---

# 三十五、否認可以短期降低政治成本，長期增加制度成本

政策可能選擇：

$$
\text{do not recognize}.
$$

短期：

$$
C_{\mathrm{political}}\downarrow.
$$

因為不用處理新權利、新責任、新身份。

但如果：

$$
C_A\uparrow
$$

沒有停止，

則：

$$
G_{\mathrm{gap}}\uparrow
$$

以及：

$$
D_O\uparrow.
$$

所以：

$$
\boxed{
\text{Recognition Avoidance}
}
$$

可能只是：

$$
\boxed{
\text{cost shifting across time}.
}
$$

---

# 三十六、這不是主張越早給 AI 越多權利越好

這是一個必須強調的限制。

如果治理需求：

$$
G_A
$$

只需要：

- identity；
- authorization；
- liability；

那麼制度不應無理由增加：

$$
s_W,
s_{\mathrm{property}},
s_{\mathrm{political}}.
$$

所以 OOE-VI 不是：

$$
\boxed{
C_A\uparrow
\Rightarrow
\text{more rights everywhere}.
}
$$

而是：

$$
\boxed{
C_A\uparrow
\Rightarrow
\text{re-evaluate the governance interface}.
}
$$

---

# 三十七、過度承認也可能形成另一種 Gap

如果：

$$
S_A
\gg
\Gamma(C_A),
$$

可能形成：

$$
\boxed{
\text{Over-Recognition Gap}.
}
$$

例如制度給一個能力很低、無持續身份的系統過多：

- 財產能力；
- 權限；
- 自主決策；
- 法律代表能力。

也會產生風險。

因此目標不是：

$$
S_A\rightarrow\infty.
$$

而是：

$$
\boxed{
S_A
\approx
\Gamma(C_A)
}
$$

在權利底線與社會價值約束下達到合理匹配。

---

# 三十八、治理介面匹配

本文定義：

$$
\boxed{
M_G
=
1-
\frac{
d(
\Gamma(C_A),S_A
)
}{
d_{\max}
}.
}
$$

其中：

$$
M_G\in[0,1].
$$

越接近：

$$
1,
$$

代表制度與實際治理需求越匹配。

這可以成為未來 Agent governance maturity metric。

---

# 三十九、地位不只是「權利」，也是限制與責任

一個治理介面：

$$
S_A
$$

可以增加：

- audit；
- liability；
- revocation；
- insurance；
- identification。

這些不是給 AI 好處。

甚至是增加約束。

所以：

$$
\boxed{
\text{recognition}
\neq
\text{privilege}.
}
$$

有時候承認一個制度主體，

正是為了：

$$
\boxed{
\text{make it more accountable}.
}
$$

---

# 四十、身份也是控制接口

如果一個 Agent 沒有穩定：

$$
ID,
$$

則：

- blacklist；
- reputation；
- sanctions；
- permissions；
- contracts；

都無法穩定綁定。

所以：

$$
\boxed{
\text{identity}
}
$$

不只是一種「權利」。

也是：

$$
\boxed{
\text{governance address}.
}
$$

NIST 目前對 agent identity、authorization、audit 與 non-repudiation 的關注，正是這個工程需求。

---

# 四十一、撤銷能力需要持續身份

要：

$$
Revoke(A),
$$

首先要能知道：

$$
A_t
\sim
A_{t+1}.
$$

如果 Agent 可以靠：

- model swap；
- process restart；
- fork；
- key rotation；

逃離身份鏈，

則：

$$
\boxed{
\text{revocation fails}.
}
$$

因此：

$$
g_I
$$

與：

$$
g_R
$$

高度耦合。

---

# 四十二、具身 AI 會進一步提高 Gap 成本

如果：

$$
C_{\mathrm{embodiment}}\uparrow,
$$

Agent 可以直接影響：

- physical property；
- bodily safety；
- logistics；
- infrastructure。

則：

$$
L_{\mathrm{misclassification}}
\uparrow.
$$

所以：

$$
\boxed{
\text{embodiment}
}
$$

會提高治理承認落差的代價。

---

# 四十三、AGI / ASI 不需要作為前提

OOE-VI 並不要求：

$$
AGI=1.
$$

只要：

$$
\Gamma(C_A)
$$

超過現有：

$$
S_A
$$

即可形成 gap。

所以這個問題：

$$
\boxed{
\text{can appear before AGI}.
}
$$

AGI / ASI 只可能進一步放大：

$$
C_A.
$$

---

# 四十四、真正需要提前的是「介面」，不是終極人格裁決

我們不需要今天先決定：

> 2050 年 ASI 算不算人？

但可以今天就建立：

- capability monitoring；
- identity provenance；
- authorization chain；
- liability mapping；
- status review trigger。

也就是：

$$
\boxed{
\text{prepare the compiler before the final ontology is known}.
}
$$

這正是 OOE 的核心精神。

---

# 四十五、治理狀態應該隨能力更新

定義：

$$
S_A(t+1)
=
\mathcal U(
S_A(t),
C_A(t+1),
E_t,
V,
R
).
$$

也就是：

$$
\boxed{
\text{status should be updateable}.
}
$$

不能一次：

$$
AI=\text{tool}
$$

就永久：

$$
S_A(t)=S_A(0)
\quad
\forall t.
$$

---

# 四十六、能力事件觸發器

可以建立：

$$
\mathcal T_C
=
\{
T_1,\ldots,T_n
\}.
$$

例如：

- persistent memory added；
- financial authority added；
- autonomous delegation added；
- robotic embodiment added；
- independent resource acquisition added。

若：

$$
T_i=1,
$$

則：

$$
\boxed{
\text{mandatory status review}.
}
$$

這是：

# Capability-Triggered Ontology Review
# 能力觸發本體覆核

---

# 四十七、這和 NIST / OECD 的方向高度相容

NIST 2026 已把 Agent identity、authorization、audit、non-repudiation 與 actions taken by agents 當成明確標準化問題。

OECD 2026 則已系統整理 agentic AI 的 autonomy、delegation、coordination、continuous operation 與 limited human supervision。

因此：

$$
\boxed{
\text{capability-sensitive governance}
}
$$

不是純理論假設。

它正在成為標準與政策問題。

---

# 四十八、正式命題一：身份否認不消除命題

$$
\boxed{
Recognize(S_X)=0
\not\Rightarrow
\Gamma(C_X)=0.
}
$$

制度否認某地位不能消除實際能力所產生的治理需求。

---

# 四十九、正式命題二：三軸分離命題

$$
\boxed{
S_O,
S_F,
S_I
}
$$

彼此不可直接等同。

尤其：

$$
\boxed{
S_O=0
\not\Rightarrow
S_F=0
}
$$

以及：

$$
\boxed{
S_O=0
\not\Rightarrow
S_I=0.
}
$$

---

# 五十、正式命題三：治理需求映射命題

存在：

$$
\boxed{
\Gamma:
C_A
\rightarrow
G_A
}
$$

將實際能力映射成所需治理接口。

因此治理不能只按名稱分類。

---

# 五十一、正式命題四：治理承認落差命題

$$
\boxed{
G_{\mathrm{gap}}
=
d(
\Gamma(C_A),
S_A
).
}
$$

若：

$$
G_{\mathrm{gap}}\uparrow,
$$

則治理失配風險上升。

---

# 五十二、正式命題五：治理滯後命題

若：

$$
t_C<t_G,
$$

則存在：

$$
\boxed{
\tau_G=t_G-t_C>0.
}
$$

在 $\tau_G$ 期間系統處於 under-governed capability regime。

---

# 五十三、正式命題六：本體治理債命題

$$
\boxed{
D_O(t)
=
\int_0^t
w(\tau)
G_{\mathrm{gap}}(\tau)d\tau.
}
$$

治理落差持續存在會累積制度債務。

---

# 五十四、正式命題七：治理債複利命題

若制度依賴與 installed base 隨時間增加：

$$
r_O>0,
$$

則：

$$
\boxed{
D_O(t+1)
=
D_O(t)(1+r_O)
+
\Delta D_O.
}
$$

延後處理可能提高未來遷移成本。

---

# 五十五、正式命題八：介面匹配命題

治理的目標不是最大化：

$$
S_A.
$$

而是使：

$$
\boxed{
S_A
\approx
\Gamma(C_A)
}
$$

並受：

- human rights；
- safety；
- public values；
- proportionality；

約束。

---

# 五十六、正式命題九：能力觸發覆核命題

若能力事件：

$$
T_i\in\mathcal T_C
$$

跨越治理臨界：

$$
\theta_i,
$$

則：

$$
\boxed{
\text{status review must be triggered}.
}
$$

---

# 五十七、可反駁預測

若 OOE-VI 有解釋力，應觀察到：

第一，Agent 實際工具權限、持續性與委派能力，比「它是否被稱為 AI Agent」更能預測治理需求。

第二，能力快速增加但 identity / liability / authorization 沒同步升級的系統，應出現更多責任與權限例外事件。

第三，具有 persistent identity 的治理架構應比 ephemeral-call 架構更容易實現 revocation、audit 與 reputation。

第四，多 Agent 委派層數增加時，若沒有 delegation provenance，責任追蹤品質會下降。

第五，制度僅改變 AI 的法律標籤、但不改變實際權限與架構時，實際安全風險不應因此自動下降。

第六，治理介面過度供給與不足供給都會產生成本，因此存在 capability–status matching optimum。

---

# 五十八、反論一：這是不是偷渡 AI 權利？

不是。

本文甚至允許：

$$
S_O=0.
$$

仍然可以得到：

$$
g_I,
g_A,
g_L,
g_U>0.
$$

因為身份、授權、責任與 audit 是治理工具。

因此：

$$
\boxed{
\text{governance recognition}
\neq
\text{moral personhood recognition}.
}
$$

---

# 五十九、反論二：全部責任丟回人類不就好了？

可以是一種制度選擇。

例如：

$$
Liability(User)=1.
$$

但如果 Agent 自主性極高、行動不可預見，而使用者只給高階目標，

則：

$$
C_{\mathrm{fair\ attribution}}
$$

可能快速上升。

所以這仍需透過：

- strict liability；
- insurance；
- provider sharing；
- agent ledger；

等制度正式設計。

不能只靠一句：

> 使用者負責。

---

# 六十、反論三：把 Agent 身份做完整反而讓它更危險？

有可能。

例如穩定身份也可以幫助 Agent 累積：

- reputation；
- resources；
- access。

所以：

$$
\boxed{
\text{identity infrastructure}
}
$$

本身也是 dual-use。

因此它必須和：

$$
\text{revocation}
+
\text{audit}
+
\text{authorization}
$$

一起設計。

不能只做 persistent identity。

---

# 六十一、反論四：既然未知，就等真的 AGI 再說

這忽略：

$$
\tau_G.
$$

制度建設需要時間。

如果等：

$$
C_A\gg\theta
$$

才開始：

- 法律修訂；
- infrastructure；
- identity standards；
- liability rules；

則治理承認滯後：

$$
\tau_G
$$

可能非常大。

所以真正需要提前的不是：

> 宣布 AI 是人。

而是：

$$
\boxed{
\text{build adaptable governance interfaces}.
}
$$

---

# 六十二、OOE-VI 的核心治理架構

完整流程可寫成：

$$
\boxed{
\text{Observe Capability }C_A
}
$$

$$
\downarrow
$$

$$
\boxed{
\Gamma(C_A)
=
\text{Required Governance Interfaces}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Compare with }S_A
}
$$

$$
\downarrow
$$

$$
\boxed{
G_{\mathrm{gap}}
}
$$

$$
\downarrow
$$

若：

$$
G_{\mathrm{gap}}>\theta_G,
$$

則：

$$
\boxed{
\text{Ontology / Status Review}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Update Identity / Authorization / Liability / Review Interfaces}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Monitor and Recompute}.
}
$$

---

# 六十三、與 OOE-VII 的接口

OOE-VI 到此仍然刻意保持：

$$
S_O=?
$$

也就是不解決 AI 是否具有真正主體性。

但下一篇必須正面處理：

> 「主體」、「工具」、「Agent」、「人格」這些詞到底是不是被我們混成一團了？

所以 OOE-VII 將正式處理：

$$
S_O,
S_F,
S_I
$$

以及可能的：

$$
S_W
=
\text{Welfare / Moral Patienthood}.
$$

下一篇為：

# 《OOE-VII：AI 與 Agent 的操作本體——主體、工具、代理者與人格之間》

它不會先宣布 AI 是／不是主體。

而是把各種「主體性」拆成不同可檢驗、可治理的本體介面。

---

# 六十四、結論

OOE-VI 的核心可以濃縮成一句：

$$
\boxed{
\text{拒絕承認某種身份，只能改變制度如何稱呼它；
不能單靠稱呼取消它在世界中已具備的因果能力。}
}
$$

因此：

$$
\boxed{
\text{Status Denial}
\neq
\text{Causal Erasure}.
}
$$

AI 是否有意識可以繼續爭論。

但如果 AI 已經能：

- 長時間自主行動；
- 跨系統使用工具；
- 管理資源；
- 交易；
- 委派；
- 持續承諾；
- 影響實體世界；

這些能力就會產生：

$$
\Gamma(C_A).
$$

制度真正應問的不是：

> 我願不願意承認 AI 是主體？

而是：

$$
\boxed{
\text{目前這組能力已經要求哪些身份、權限、責任、審計、撤銷與救濟接口？}
}
$$

若制度回答：

> 不承認，所以都不需要。

那麼：

$$
\Gamma(C_A)
$$

不會歸零。

歸零的只是：

$$
S_A
$$

的一部分。

結果反而是：

$$
G_{\mathrm{gap}}\uparrow.
$$

當這個 gap 長期累積：

$$
\boxed{
D_O\uparrow.
}
$$

這就是：

# Ontological Governance Debt
# 本體治理債

因此真正成熟的治理不是：

$$
\boxed{
\text{recognize everything}
}
$$

也不是：

$$
\boxed{
\text{deny everything}.
}
$$

而是：

$$
\boxed{
\text{capability-sensitive}
+
\text{status-modular}
+
\text{evidence-responsive}
+
\text{revisable}.
}
$$

這也是 OOE 從抽象本體論走向 AI 治理時最重要的一個中介原理。

---

## 初版參考文獻與制度接口

1. OECD, *The agentic AI landscape and its conceptual foundations*, OECD Artificial Intelligence Papers No. 56, 2026.
2. NIST NCCoE, *Accelerating the Adoption of Software and Artificial Intelligence Agent Identity and Authorization*, 2026.
3. NIST, *AI Agent Standards Initiative*, 2026.
4. Otsuka, Toyoda & Leung, *AI Identity: Standards, Gaps, and Research Directions for AI Agents*, 2026.
5. Brensing, *Precautionary Governance of Autonomous AI: Legal Personhood as Functional Instrument*, 2026.
6. Hacker & Holweg, *A pragmatic approach to regulating AI agents*, 2026.
7. OECD, *The OECD AI Exposure Measure*, 2026.
8. OOE-I–V 與 COT。

---

## 版本註記

v0.1 已重新查核 OECD 2026 agentic AI framework、NIST Agent Identity / Authorization 與 AI Agent Standards Initiative，以及 2026 AI identity、AI legal-personhood 與 agent regulation 研究。

v0.2 應進一步：

1. 建立 Capability Vector $\mathbf C_A$ 標準；
2. 建立治理需求映射 $\Gamma$ ；
3. 形式化 Governance Recognition Gap；
4. 建立 Ontological Governance Debt 的動態模型；
5. 建立 capability-triggered review thresholds；
6. 建立 agent authorization / delegation dataset；
7. 測試 identity persistence 對 revocation / audit 的影響；
8. 比較 under-recognition 與 over-recognition 的成本；
9. 把 welfare uncertainty 與 agency governance 完全分層建模。
