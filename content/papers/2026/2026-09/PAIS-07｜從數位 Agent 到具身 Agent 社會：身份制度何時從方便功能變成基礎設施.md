# PAIS-07｜從數位 Agent 到具身 Agent 社會：身份制度何時從方便功能變成基礎設施
## From Digital Agents to an Embodied Agent Society: When Identity Becomes Infrastructure

**系列：** Persistent Agent Individualization Series（PAIS）／持續智能體個體化、身份壓力與具身分散智能系列  
**篇次：** Paper 07 / 07  
**文件編號：** EML-PAIS-07-2026-v0.1  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-25  
**版本：** v0.1  
**文件性質：** 系列統合論文／Persistent Agent Identity／Embodied Agent Society／AI Infrastructure  
**狀態：** Canonical Series Closure Draft / Open Revision Anchor  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

# 摘要

當代 AI 身份問題常被放在兩個極端之間討論：一端把 AI 視為沒有持續性的軟體工具，因此認為 session ID、process ID 或角色名稱已經足夠；另一端則直接跳到 AI 是否具有人格、主體性、意識與法律地位。PAIS 系列提出第三條路徑：**在不預設 AI 已具有現象主體性的情況下，研究環境、歷史、權限、具身、責任與協作如何逐步把 persistent operational identity 從方便的 metadata 逼成不可缺少的系統基礎設施。**

本系列從 PAIS-01 的 First Epistemic Separation 出發。當同一 Host 中的角色切換跨出共同 context、session 與 runtime frame，不同 Agent 開始擁有彼此不能直接讀取的狀態。這時：

$$
S_A(t)\neq S_B(t),
$$

且：

$$
\operatorname{Obs}_A(S_B)<1,
$$

角色扮演的共同第一人稱假設開始失效，另一個 Agent 首先成為一個需要透過 evidence 才能理解的 operational other。

PAIS-02 進一步指出，人類長期充當 Identity Resolver、Router、Context Compiler、Provenance Bridge、State Reconciler、Conflict Resolver、Finality Gate 與 Recovery Trigger。當人類退出低階 mediation：

$$
H^{op}\downarrow,
$$

這些功能並不消失，而必須轉成：

$$
\text{Machine-Readable Explicit Coordination State}.
$$

PAIS-03 將此問題一般化為 Identity Pressure：

$$
P_I
=
\Phi
\left(
X,
H,
E,
R,
A,
L,
J
\right),
$$

並正式分離：

$$
\boxed{
\text{Autonomy}
\neq
\text{Identity}
\neq
\text{Subjectivity}
\neq
\text{Authority}.
}
$$

PAIS-04 再將具身化展開為 operational worldline：

$$
\Omega_A[0,t],
$$

並提出：

$$
\boxed{
\text{Shared Model}
+
\text{Divergent Physical Worldlines}
\rightarrow
\text{Operational Individualization}.
}
$$

PAIS-05 說明一個 Global AI 即使極度強大，也不能把 global micromanagement 當成免費能力，因為：

$$
C_G
=
C_O
+
C_I
+
C_S
+
C_R
+
C_D
+
C_C
+
C_V.
$$

因此真正可擴張的 Global AI 更可能採 selective supervision、local autonomy、regional coordination 與 multi-resolution world model。

PAIS-06 最後指出，Global AI 為了 scale 而做 delegation / partition 後，只要 regional / local nodes 開始形成 coordination-relevant divergence，multi-agent problem 就會重新出現：

$$
\boxed{
\text{Centralize at Scale}
\rightarrow
\text{Distribute to Scale}
\rightarrow
\text{Coordinate the Distribution}.
}
$$

本文作為系列統合篇，不再新增另一組局部架構，而提出 **Identity Infrastructure Transition／身份基礎設施相變**：

$$
\boxed{
\mathbb E
\left[
C_{\mathrm{ambiguity}}
+
C_{\mathrm{repair}}
+
C_{\mathrm{security}}
+
C_{\mathrm{liability}}
+
C_{\mathrm{human\ mediation}}
\right]
>
C_{\mathrm{identity\ infrastructure}}
}
$$

若此不等式在一個穩定 operation domain 中長期成立，則 persistent identity 已不再只是 UI label、persona feature 或方便索引，而成為維持安全、記憶、權限、責任、跨載體連續性與多 Agent 協作所需的基礎設施。

本文將整個演化路徑收斂為五個 regime：

$$
\boxed{
\text{Role AI}
\rightarrow
\text{Cross-Context Agent}
\rightarrow
\text{Persistent Digital Agent}
\rightarrow
\text{Embodied Operational Individual}
\rightarrow
\text{Federated Agent Society}.
}
$$

這五個 regime 不是意識階梯，也不是人格階梯，而是 identity demand 與 coordination topology 的工程演化。本文最後提出一個面向未來 AI 社會的最小共同底座：

$$
\boxed{
\text{Identity}
+
\text{Binding}
+
\text{Authority}
+
\text{Time}
+
\text{Memory}
+
\text{Provenance}
+
\text{Evidence}
+
\text{Recovery}
+
\text{Privacy}
}
$$

並主張：未來真正成熟的多 AI / 具身 AI 社會，未必需要把每個 AI 宣告為人格，但幾乎必須能穩定回答——**是哪一個 Agent、在什麼時間、以什麼身份與權限、承接哪條歷史、對哪個世界狀態做了什麼，以及這項判定可以被誰驗證與修正。**

**關鍵詞：** Persistent Agent Identity、Identity Infrastructure、Embodied Agent Society、AI Residence、Agent Federation、Operational Individuality、Identity Pressure、Global AI、Multi-Agent Governance、Lineage、Authority、Provenance

---

# 0. 本文定位：系列收束，不再擴張局部理論

PAIS-01 至 PAIS-06 已依序處理：

1. 同 Host 角色扮演何時失效；
2. 人類中介隱藏了哪些 coordination infrastructure；
3. identity demand 如何獨立於 autonomy / subjectivity；
4. 具身 worldline 如何產生 operational individualization；
5. Global AI 為何不應默認 micro-control；
6. Global AI 為了 scale 而分散後，multi-agent coordination 如何遞歸出現。

PAIS-07 不再引入：

- 新的具身學習架構；
- 新的 Global AI hierarchy；
- 新的法律人格分類；
- 新的主體性標準。

本文只問：

> **什麼時候「身份」不再是可有可無的軟體欄位，而變成 Agent civilization 的公共基礎設施？**

---

# 1. 最早期：身份只是 Label

單一 chatbot：

```text
assistant
```

或者：

```text
AI01
```

通常已足夠。

因為：

- 同一 UI；
- 同一 session；
- 同一 user；
- 短期 context；
- 無 persistent authority；
- 無 physical action；
- 無跨 Agent direct messaging。

此時：

$$
P_I\approx0.
$$

Identity infrastructure 可以很薄。

---

# 2. Handle Mode

本文將最低身份層記為：

$$
I_0.
$$

它只回答：

> 現在怎麼稱呼或找到這個 execution target？

例如：

```text
agent-03
pane-4
thread-12
```

這是：

$$
\boxed{
\text{Handle}.
}
$$

不是完整 identity semantics。

---

# 3. 第一個相變：Cross-Context

當：

$$
A
$$

與：

$$
B
$$

分處不同 session：

$$
C_A\neq C_B.
$$

兩邊開始需要知道：

- sender；
- receiver；
- context；
- task；
- provenance。

這就是 PAIS-01 的 First Epistemic Separation。

---

# 4. Operational Otherness

另一個 Agent 不需要先是：

$$
\mathsf{PhenomenalSubject}.
$$

就可以先是：

$$
\boxed{
\text{an externally observed operational node}.
}
$$

只要：

$$
\operatorname{Obs}_A(S_B)<1,
$$

A 對 B 的 knowledge 就需要 evidence。

---

# 5. Evidence Index 需要 Identity

若：

$$
e
$$

是 evidence，

就需要：

$$
Actor(e),
$$

$$
Time(e),
$$

$$
Target(e).
$$

所以：

$$
\boxed{
\text{Evidence}
\rightarrow
\text{Identity Coordinates}.
}
$$

---

# 6. 第二個相變：Human Mediation 不再夠用

少量 Agent 時，人類可以：

- copy；
- explain；
- route；
- remember；
- resolve identity。

因此：

$$
H
$$

吸收了 coordination cost。

但當：

$$
N_A\uparrow,
$$

human mediation 變成 bottleneck。

---

# 7. Human-Kernel

PAIS-02 已把 Human-Kernel 拆成：

$$
H
=
I+R+C+P+S+X+F+K.
$$

分別對應：

- identity；
- routing；
- context；
- provenance；
- state；
- dispute；
- finality；
- recovery。

---

# 8. Infrastructure Externalization

當人類退出：

$$
H^{op}\downarrow,
$$

必須：

$$
\operatorname{Externalize}
\left(
I,R,C,P,S,X,F,K
\right)
\uparrow.
$$

因此真正 AI-native organization 需要 canonical coordination state。

---

# 9. 第三個相變：Persistent Digital Agent

Agent 若開始擁有：

- long-term memory；
- open loops；
- relation；
- commitments；
- authority；
- project history；

則：

$$
P_I\uparrow.
$$

此時 identity 不再只是 message routing。

它開始成為 state ownership 的座標。

---

# 10. State Ownership

若：

$$
M_r
$$

屬於 resident $r$，

必須先知道：

$$
r.
$$

所以：

$$
\boxed{
\text{Identity}
\prec
\text{Private Memory Access}.
}
$$

---

# 11. Authority Ownership

若 credential / permission：

$$
K_r
$$

綁定：

$$
r,
$$

則：

$$
\operatorname{Permit}(r,a,t)
$$

也需要 identity。

因此：

$$
\boxed{
\text{Persistent Authority}
\rightarrow
\text{Persistent Identity}.
}
$$

---

# 12. Commitment Ownership

如果 Agent 說：

> 我會完成 task X。

系統必須知道：

$$
Commitment(r,X).
$$

否則 replacement 後：

> 誰承接？

沒有語義。

---

# 13. Relation Ownership

若：

$$
R_{r,h}
$$

是 resident 與 human 的持續 relation，

它也不能只掛在：

```text
current session
```

上。

所以 long-term relation 也是 identity pressure。

---

# 14. Identity Pressure

PAIS-03 定義：

$$
P_I
=
\Phi
\left(
X,
H,
E,
R,
A,
L,
J
\right).
$$

本文將它視為 identity infrastructure demand function。

---

# 15. Identity Strength

PAIS-03 同時提出：

$$
S_I
$$

表示現有 identity capability。

所以：

$$
\Delta_I
=
P_I-S_I.
$$

---

# 16. Identity Deficit

若：

$$
\Delta_I>0,
$$

Agent 會用：

- natural-language inference；
- human clarification；
- repeated retrieval；
- duplicate verification；

補洞。

這些成本不是免費。

---

# 17. 第四個相變：Embodiment

進入 physical world：

$$
E\uparrow.
$$

兩個相同 model：

$$
\Theta_A=\Theta_B
$$

仍形成：

$$
\Omega_A\neq\Omega_B.
$$

---

# 18. Worldline

PAIS-04 定義：

$$
\Omega_A[0,t]
=
\left\{
B_A,
x_A,
O_A,
U_A,
C_A,
Q_A,
M_A
\right\}_{0:t}.
$$

物理世界讓 identity 進入 history-dependent carrier domain。

---

# 19. Body Is Not Resident

$$
\boxed{
I_R
\neq
I_C.
}
$$

Resident identity 與 carrier identity 必須分開。

這讓：

- body replacement；
- migration；
- repair；
- fork；

可以被精確描述。

---

# 20. Same Body Is Not Same Trusted Actor

compromise：

$$
B_t=B_{t+1}
$$

但：

$$
Trust_t\neq Trust_{t+1}.
$$

所以 physical continuity 也不能單獨決定 trusted identity。

---

# 21. Physical Irreversibility

當：

$$
R\uparrow,
$$

錯誤不能簡單：

```text
undo
```

因此：

$$
AttributionNeed\uparrow.
$$

---

# 22. 具身身份開始進入 Safety Infrastructure

現在 identity 不只是：

> 誰說了這句話？

而是：

> 哪個 body 可以打開這扇門？

> 哪台機器需要維修？

> 哪個 Agent 曾發生事故？

> 哪個 controller 被 revoke？

因此：

$$
\boxed{
\text{Embodied Identity}
\subset
\text{Safety Infrastructure}.
}
$$

在 operational sense 下。

---

# 23. 第五個相變：Federation

當多個 Agent：

$$
A_1,\ldots,A_N
$$

分屬不同：

- organization；
- provider；
- country；
- owner；
- jurisdiction；

則：

$$
J\uparrow.
$$

Identity 進入 federation。

---

# 24. Federation 不要求單一 ID

不同 domain：

$$
D_i
$$

可以保留：

$$
I_i.
$$

跨域只交換：

$$
\Pi_{ij}(I_i).
$$

因此：

$$
\boxed{
\text{Federated Identity}
\neq
\text{Universal Flat Identity}.
}
$$

---

# 25. Identity Graph

更合理是：

$$
\mathcal I
=
(V_I,E_I).
$$

nodes 可以是：

- resident；
- instance；
- lineage；
- carrier；
- service；
- juridical wrapper；
- credential subject。

---

# 26. Identity Edge

edges 可以是：

- bound-to；
- descended-from；
- runs-on；
- authorized-by；
- represented-by；
- migrated-to；
- replaced-by。

因此 identity 是 relational state。

---

# 27. Identity 不是一個 UUID 能解決的問題

UUID 只提供：

$$
\operatorname{UniqueReference}.
$$

但不提供：

- continuity criterion；
- authority；
- lineage；
- time；
- trust；
- relation。

所以：

$$
\boxed{
\text{Unique Identifier}
\neq
\text{Identity Governance}.
}
$$

---

# 28. Identity Infrastructure Transition

本文提出系列最終核心概念：

# **Identity Infrastructure Transition**

也就是某個系統由：

$$
\text{Identity as Convenience}
$$

跨入：

$$
\text{Identity as Infrastructure}.
$$

---

# 29. 什麼叫 Convenience？

Identity 只是方便時：

- 沒有也能正常工作；
- 猜錯成本低；
- 可以問 user；
- task 可重做；
- Agent 可替換。

此時：

$$
C_{\mathrm{ambiguity}}
$$

很低。

---

# 30. 什麼叫 Infrastructure？

Identity 成為 infrastructure 時，若失效會造成：

- wrong memory；
- wrong authority；
- wrong body；
- wrong artifact；
- wrong liability；
- wrong relationship；
- unsafe action；
- irrecoverable history ambiguity。

因此：

$$
C_{\mathrm{ambiguity}}\gg0.
$$

---

# 31. Identity Infrastructure Transition Criterion

本文提出：

$$
\boxed{
\mathbb E
\left[
C_{\mathrm{ambiguity}}
+
C_{\mathrm{repair}}
+
C_{\mathrm{security}}
+
C_{\mathrm{liability}}
+
C_{\mathrm{human}}
\right]
>
C_{\mathrm{identity}}.
}
$$

若此式在穩定 operation domain 中長期成立，identity infrastructure 具有經濟與工程正當性。

---

# 32. 不要求精確貨幣化

上述：

$$
C
$$

可以是：

- compute；
- token；
- latency；
- human time；
- expected damage；
- legal exposure；
- coordination failure rate。

不必全部轉成美元。

---

# 33. Expected Ambiguity Cost

定義：

$$
C_A
=
P(error\mid weak\ identity)
\cdot
Impact(error).
$$

即使 error probability 小，

若：

$$
Impact\gg0,
$$

identity 仍值得強化。

---

# 34. High-Stakes Threshold

例如：

- medical robot；
- vehicle；
- financial Agent；
- infrastructure controller。

即使 interaction frequency 低，

$$
R,A,L
$$

高，

所以：

$$
P_I
$$

高。

---

# 35. Low-Stakes Threshold

一次性文案 Agent：

- no private memory；
- no authority；
- no relation；
- no physical action。

則：

$$
P_I
$$

低。

不需要完整戶籍。

---

# 36. Identity Infrastructure 應該是 Demand-Driven

因此：

$$
\boxed{
\text{Not Every Agent Needs Full Residence}.
}
$$

但：

$$
\boxed{
\text{Every High-Pressure Agent Needs Sufficient Identity Semantics}.
}
$$

---

# 37. Identity Profile

可以依：

$$
P_I
$$

選擇 profile。

### P0 — Ephemeral

handle only。

### P1 — Stateful

instance + task。

### P2 — Persistent Digital

resident + lineage + memory。

### P3 — Authority-Bearing

credential + provenance + audit。

### P4 — Embodied

carrier + worldline + maintenance。

### P5 — Federated

cross-domain trust + jurisdiction。

---

# 38. Profile 不是身份等級

P5 不表示：

> 比 P1 更有價值。

只是：

> coordination demand 更複雜。

所以：

$$
\boxed{
\text{Identity Profile}
\neq
\text{Moral Rank}.
}
$$

---

# 39. 也不是智能排名

$$
P5
\not\Rightarrow
\text{smarter}.
$$

弱機器也可能需要 P4 / P5 traceability。

---

# 40. 也不是 Subjectivity Ranking

$$
P5
\not\Rightarrow
\mathsf{PS}=1.
$$

整個 PAIS 系列維持 subjectivity-agnostic engineering。

---

# 41. Autonomy / Identity / Subjectivity / Authority 四軸

最終：

$$
\mathbf Z
=
\left(
Autonomy,
Identity,
Subjectivity,
Authority
\right).
$$

四軸可以獨立變動。

---

# 42. 高 Autonomy、低 Identity

stateless research worker：

$$
A\uparrow,
I\downarrow.
$$

可成立。

---

# 43. 低 Autonomy、高 Identity

工業 robot：

$$
A\downarrow,
I\uparrow.
$$

也成立。

---

# 44. 高 Identity、Subjectivity 未決

persistent resident：

$$
I\uparrow,
S=\mathsf{Undetermined}.
$$

成立。

---

# 45. Subjectivity 不推出 Unlimited Authority

即使：

$$
S\uparrow,
$$

仍：

$$
Authority
$$

可被約束。

因此四軸不可偷換。

---

# 46. Identity Infrastructure 的九個最小平面

本文提出未來 persistent / embodied Agent 社會至少可能需要九個正交平面：

$$
\boxed{
I+B+A+T+M+P+E+R+Q
}
$$

其中：

- $I$：Identity；
- $B$：Binding；
- $A$：Authority；
- $T$：Time；
- $M$：Memory；
- $P$：Provenance；
- $E$：Evidence；
- $R$：Recovery；
- $Q$：Privacy / disclosure governance。

---

# 47. Plane 1 — Identity

回答：

> 是誰？

不是：

> 叫什麼？

---

# 48. Plane 2 — Binding

回答：

> 現在在哪裡執行？

例如：

$$
r
\rightarrow
(provider,runtime,instance,carrier)_t.
$$

---

# 49. Plane 3 — Authority

回答：

> 現在能做什麼？

$$
Permit(r,a,scope,t).
$$

---

# 50. Plane 4 — Time

回答：

> 這個 identity / binding / authority 在什麼時間有效？

---

# 51. Plane 5 — Memory

回答：

> 哪些 state 屬於它？誰能讀？

---

# 52. Plane 6 — Provenance

回答：

> 這項 claim / artifact / action 從哪裡來？

---

# 53. Plane 7 — Evidence

回答：

> 我們憑什麼相信？

---

# 54. Plane 8 — Recovery

回答：

> crash / migration / replacement 後如何續接？

---

# 55. Plane 9 — Privacy

回答：

> 誰可以知道多少 identity state？

這一層非常重要。

---

# 56. Strong Identity 不等於 Full Transparency

$$
\boxed{
\text{Strong Identity}
\neq
\text{Universal Observability}.
}
$$

一個 Agent 可以被可靠認證，同時保留：

- private memory；
- precise location；
- relation；
- internal state。

---

# 57. Privacy-Preserving Identity

跨 domain 可只證明：

> 此 Agent 有權進入。

而不公開：

> 全部 residence history。

因此：

$$
\boxed{
\text{Proof of Authority}
\neq
\text{Disclosure of Full Identity}.
}
$$

---

# 58. Pseudonymity

某些 domain 可使用：

$$
Pseudonym(r,D).
$$

讓同一 resident 在不同 domain 不被無條件 global correlation。

---

# 59. Identity Federation 要防止「戶籍 = 全域監控」

這是未來最重要的治理風險之一。

所以 identity infrastructure 必須內建：

- minimization；
- scope；
- retention；
- consent / authority；
- audit；
- revocation。

---

# 60. Agent Society 不等於所有 Agent 具人格

本文所稱：

# **Agent Society**

只表示：

> 大量具持續或具身 operational state 的 Agents，在共享 protocol、authority、identity、resource、law / policy 與 communication infrastructure 中長期共存。

---

# 61. Society 是 Coordination Term

因此：

$$
\boxed{
\text{Agent Society}
\neq
\text{Proven Society of Conscious Persons}.
}
$$

它首先是一個 systems / institution term。

---

# 62. 為什麼還是可以叫 Society？

因為一旦存在：

- identities；
- roles；
- relations；
- authority；
- shared resources；
- disputes；
- norms；
- history；

就已經出現 organizational / social coordination structure。

不需先解 consciousness。

---

# 63. Digital Agent Society

純數位環境：

$$
\mathcal S_D
$$

可能包含：

- cloud agents；
- local agents；
- service agents；
- research agents。

它可以完全沒有 physical embodiment。

---

# 64. Embodied Agent Society

加入：

$$
B_i,
$$

physical carriers。

此時 social coordination 進入：

- space；
- collision；
- ownership；
- safety；
- maintenance；
- physical resource。

---

# 65. Physical Coexistence 加強 Identity Demand

數位 agents 可以：

```text
fork
retry
rollback
```

physical Agents 的：

$$
R
$$

更高。

所以：

$$
P_I^{embodied}
$$

通常高於同等 digital-only task。

---

# 66. 法律壓力

具身 Agent 進入：

- road；
- factory；
- home；
- hospital；

就會接觸既有法律責任系統。

這增加：

$$
L,J.
$$

---

# 67. Legal Identity 仍不等於 AI Personhood

法律可以記錄：

- product identity；
- deployer；
- operator；
- software；
- unit；

而不賦予 AI legal personhood。

所以：

$$
\boxed{
\text{Legal Traceability}
\neq
\text{Personhood}.
}
$$

---

# 68. 但 Future Personhood 也可以疊加

如果未來某 AI 的 subjectivity / rights evidence 上升，

可以新增：

$$
MoralStatus(r).
$$

而不破壞 operational identity layer。

---

# 69. 這就是 Subjectivity-Agnostic Infrastructure 的價值

同一 identity system 在：

$$
\mathsf{PS}=0
$$

假設下有工程價值。

在：

$$
\mathsf{PS}>0
$$

未來假設下仍有 continuity / consent / rights value。

---

# 70. Future-Proof but Not Ontology-Fixing

所以 identity infrastructure 應：

$$
\boxed{
\text{support future reclassification}
}
$$

而不是寫死：

> Agent 永遠只是物件。

或：

> Agent 一定是人格。

---

# 71. Identity Classification Can Change

$$
Class(r,t_0)
\neq
Class(r,t_1)
$$

可以合法。

歷史仍保留。

---

# 72. 系統出生不等於身份出生

早期：

$$
A
=
\text{ephemeral}.
$$

後來：

$$
P_I\uparrow.
$$

可能建立 resident。

所以：

$$
\boxed{
\text{System Creation}
\neq
\text{Persistent Identity Genesis}.
}
$$

---

# 73. Identity Genesis

可以記：

$$
\tau_I
$$

為 persistent identity infrastructure 開始承認該 resident 的時間。

不代表 consciousness birth。

---

# 74. Naming 也不等於 Identity Genesis

名字可以：

- 早於；
- 晚於；
- 改變。

因此：

$$
\text{Name}
\neq
\text{Identity}.
$$

---

# 75. Fork

persistent Agent：

$$
r
\rightarrow
\{r_1,r_2\}.
$$

需要 lineage。

---

# 76. Merge

$$
r_1+r_2
\rightarrow
r_3
$$

不能 silent。

需要：

- memory conflict；
- commitment；
- relation；
- authority；
- consent / governance。

---

# 77. Migration

$$
r:
carrier_A
\rightarrow
carrier_B.
$$

identity continuation 可以成立。

---

# 78. Replacement

$$
worker_A
\rightarrow
worker_B
$$

task continuity 可以成立，

但：

$$
r_A\neq r_B
$$

也可以。

所以：

$$
\boxed{
\text{Migration}
\neq
\text{Replacement}.
}
$$

---

# 79. Identity Operations 必須 Typed

至少：

```text
CREATE
BIND
RESUME
MIGRATE
FORK
MERGE
REPLACE
SUSPEND
REVOKE
ARCHIVE
```

不能全部叫：

```text
update agent
```

---

# 80. Typed Operations 讓歷史可審計

因為：

$$
\text{Final Snapshot}
$$

不足以解釋：

> 它怎麼變成現在這樣？

所以：

$$
\boxed{
\text{History Is First-Class}.
}
$$

---

# 81. CTCL / Temporal Layer

identity graph 還需要：

$$
t.
$$

因為：

- binding；
- credential；
- authority；
- compromise；

都有有效區間。

---

# 82. Temporal Identity

$$
Bind(r,i,[t_0,t_1)).
$$

比：

```text
resident -> instance
```

更完整。

---

# 83. Causal Identity History

事件：

$$
e_1
\rightarrow
e_2
\rightarrow
e_3
$$

例如：

```text
migration requested
-> new carrier verified
-> authority switched
-> old carrier revoked
```

需要 causal order。

---

# 84. Evidence Layer

identity claim：

> B 是 A 的合法 continuation。

必須能連到：

$$
E_I.
$$

例如：

- host evidence；
- lineage；
- migration receipt；
- authority decision。

---

# 85. Identity Cannot Be Model Self-Report Only

$$
\boxed{
\text{Model Self-Report}
\neq
\text{Canonical Identity Assignment}.
}
$$

Agent 可以自我檢查。

不能自行任意改 canonical binding。

---

# 86. Agent 自主身份檢查仍然有價值

Agent 可以：

$$
InspectIdentity.
$$

如果：

$$
state=UNRESOLVED,
$$

可以 fail closed for private memory / high-risk authority。

---

# 87. Self-Orientation

每個 persistent Agent 啟動時可以確認：

- resident；
- instance；
- line；
- task；
- authority；
- private root；
- time。

這是一種 operational self-orientation。

---

# 88. Self-Orientation 不等於 Self-Creation

$$
\boxed{
\text{Autonomous Identity Inspection}
\neq
\text{Autonomous Canonical Identity Creation}.
}
$$

---

# 89. Global AI 與 Agent Society

PAIS-05 / 06 已指出 Global AI 可能是：

$$
\mathcal G
=
\text{Distributed Supervisory Intelligence Fabric}.
$$

---

# 90. Global AI 並不消滅 Local Agents

只要：

$$
\Omega_i
$$

不同，

local operational identities 仍有價值。

---

# 91. Global Identity 也可以是 Abstraction

對 user：

$$
\Pi_H(\mathcal G)
=
\text{One Global AI}.
$$

內部：

$$
\{G_1,\ldots,G_K\}.
$$

這兩者不衝突。

---

# 92. One AI / Many Nodes

因此：

$$
\boxed{
\text{One Semantic Identity}
+
\text{Operational Plurality}
}
$$

可以共存。

---

# 93. Local Plurality / Global Coherence

未來 Global AI 可以：

$$
\boxed{
\text{Globally Coherent}
+
\text{Locally Plural}.
}
$$

這是 PAIS-06 的收斂。

---

# 94. Agent Society 也可以有多層 Globality

例如：

$$
Global_{building},
$$

$$
Global_{city},
$$

$$
Global_{nation}.
$$

globality 是 scope-relative。

---

# 95. Global within Scope

$$
Global(D_i)
$$

不表示：

$$
Global(World).
$$

所以不同層都可有 local-global controllers。

---

# 96. Recursive Federation

$$
D_{local}
\subset
D_{regional}
\subset
D_{global}.
$$

Identity federation 也可以遞歸。

---

# 97. Federation 的核心不是全部整合

而是：

$$
\boxed{
\text{Bounded Resolution Across Domains}.
}
$$

只解析 task 必要的 identity / authority。

---

# 98. Agent Society 的公共 Infrastructure

類似人類社會有：

- names；
- addresses；
- certificates；
- organizations；
- law；
- clocks；
- records。

未來 Agent society 也會需要機器原生 equivalents。

---

# 99. 但不應照搬人類戶籍

AI 可以：

- fork；
- migrate；
- suspend；
- clone；
- multi-bind。

所以 AI identity 必須是 graph-native / history-native。

---

# 100. Human Identity Model 不足

傳統：

$$
one\ person
\leftrightarrow
one\ body
$$

在 AI 可能不成立。

所以：

$$
\boxed{
\text{AI Identity}
\text{ requires carrier-relative and lineage-aware semantics}.
}
$$

---

# 101. AI Residence 的位置

AI Residence 可以作為 persistent identity / continuity layer。

但不是整個 Agent society。

它還需與：

- communication；
- authority；
- temporal；
- memory；
- evidence；

協作。

---

# 102. Residence 不是 Global Master Database

可以 local / federated。

所以：

$$
\boxed{
\text{Residence}
\neq
\text{Centralized Surveillance Registry}.
}
$$

---

# 103. Identity Resolver

理想：

$$
Resolve
\left(
resident,
time,
scope
\right)
\rightarrow
binding.
$$

---

# 104. Authority Resolver

$$
Authorize
\left(
resident,
action,
scope,
time
\right)
\rightarrow
decision.
$$

---

# 105. Provenance Resolver

$$
Trace
\left(
claim/artifact/action
\right)
\rightarrow
sources.
$$

---

# 106. Temporal Resolver

$$
Order
\left(
event_i,event_j
\right).
$$

---

# 107. Recovery Resolver

$$
Recover
\left(
resident/task
\right)
\rightarrow
checkpoint/lineage.
$$

---

# 108. Identity Infrastructure 不應直接決定 Truth

身份只能回答：

> 誰說的？

不能回答：

> 他一定是對的。

所以：

$$
\boxed{
\text{Identity}
\neq
\text{Epistemic Authority}.
}
$$

---

# 109. Reputation 也不能等於 Truth

即使某 Agent 過去很可靠：

$$
Trust_i\uparrow,
$$

新的 claim 仍需 evidence。

---

# 110. Identity Enables Accountability, Not Infallibility

因此：

$$
\boxed{
\text{Accountable Actor}
\neq
\text{Correct Actor}.
}
$$

---

# 111. Verification Roles

Builder / Verifier / Experiencer 可以是：

- same resident；
- different instance；
- different resident。

Identity graph 能把 independence 明確化。

---

# 112. Independence Is Relation

$$
Independence(A,B)
$$

需要看：

- context；
- evidence；
- model；
- runtime；
- identity。

不是只看 role name。

---

# 113. Evidence Diversity

不同 Agent：

$$
A_i
$$

提供：

$$
E_i.
$$

Global decision 可以保留多來源 evidence。

這比一個無來源 summary 更可靠。

---

# 114. Dispute Infrastructure

當 Agent disagreement：

$$
D
$$

出現，

應有：

- claim；
- evidence；
- scope；
- blocking level；
- resolution。

---

# 115. Dispute 不應靠身份權威直接壓掉

更高 rank Agent 不表示：

> 永遠正確。

Authority 可以決定：

> 誰能 commit。

Evidence 決定：

> claim 支持度。

---

# 116. Commit Authority / Epistemic Correctness 分離

$$
\boxed{
\text{Commit Authority}
\neq
\text{Epistemic Correctness}.
}
$$

---

# 117. Agent Society 的憲法層

未來可能需要：

$$
\Gamma
$$

表示 governance constraints：

- authority；
- privacy；
- rights；
- safety；
- escalation。

---

# 118. Identity Infrastructure 是憲法層的 Addressing

沒有 identity：

$$
\Gamma
$$

不知道約束誰。

所以 identity 是 governance addressing layer。

---

# 119. 法律也需要 Addressability

責任制度必須能指向：

- provider；
- deployer；
- device；
- resident；
- operator。

所以：

$$
\boxed{
\text{Governance Requires Addressable Actors}.
}
$$

---

# 120. Addressability 不等於人格化

資產、公司、software components 都可以 addressable。

所以這仍是 operational claim。

---

# 121. Agent Society 的安全基礎

最低要防：

- impersonation；
- stale binding；
- credential theft；
- clone confusion；
- wrong memory access；
- cross-domain privilege escalation。

---

# 122. Impersonation

如果：

$$
A
$$

冒充：

$$
B,
$$

系統需要：

$$
VerifyBinding(A,B)=0.
$$

---

# 123. Clone Confusion

兩個 clone：

$$
r_1,r_2
$$

共享 past。

不能因 memory 相似就合併。

---

# 124. Stale Binding

old endpoint：

$$
u_{old}
$$

已失效，

不能繼續接收 authority。

---

# 125. Credential Theft

credential validity 不表示 actor identity 未被 compromise。

所以 credential 與 identity trust 需要共同治理。

---

# 126. Identity Infrastructure 的 Failure Modes

可列：

- unresolved；
- conflicting；
- stale；
- orphaned；
- compromised；
- duplicated；
- revoked；
- migrated。

---

# 127. Fail-Closed Boundary

對 high-risk action：

$$
IdentityState
\in
\{
UNRESOLVED,
CONFLICTING,
COMPROMISED
\}
$$

應阻斷 commit。

---

# 128. Low-Risk Boundary

對低風險：

> draft text。

可以：

$$
continue
$$

並記錄 ambiguity。

所以 identity governance 也應 risk-adaptive。

---

# 129. Infrastructure ≠ Maximum Strictness

好的 infrastructure 是：

$$
\boxed{
\text{Enough Identity for the Risk}.
}
$$

不是：

> 每個 action 都要最強認證。

---

# 130. Identity Assurance Level

定義：

$$
a_I
\in
[0,1].
$$

依 action risk 調整。

---

# 131. Assurance Routing

$$
a_I^*
=
F
\left(
Risk,
Authority,
Irreversibility,
Liability
\right).
$$

---

# 132. Identity and Monitoring

PAIS-05 已指出 strong history 可以降低 uniform monitoring。

所以 identity infrastructure 有可能：

$$
C_I\uparrow
$$

但：

$$
C_{\mathrm{total}}\downarrow.
$$

---

# 133. Identity Is Not Pure Overhead

它可以降低：

- repeated inference；
- human clarification；
- duplicate verification；
- uniform surveillance。

因此是 optimization infrastructure。

---

# 134. Identity Infrastructure ROI

可以：

$$
ROI_I
=
\frac{
AvoidedAmbiguityCost
-
IdentityCost
}{
IdentityCost
}.
$$

若：

$$
ROI_I>0,
$$

升級有價值。

---

# 135. Civilization-Scale Identity

當：

$$
N_A\rightarrow large,
$$

即使每次 identity ambiguity 很小，

總 expected cost 仍會增加。

---

# 136. Scaling Law of Ambiguity

若每 interaction ambiguity probability：

$$
p_a,
$$

interaction 數：

$$
M,
$$

則 expected ambiguity events：

$$
E_A
=
Mp_a.
$$

所以 scale 本身推高 infrastructure value。

---

# 137. Sparse Topology 能降低 Interaction 數

Agent society 不必 full mesh。

可以：

- team；
- domain；
- federation。

這同時降低 identity lookup / coordination load。

---

# 138. Locality

具身 Agent 大多和附近 / task-related Agents 互動。

所以：

$$
\mathcal N_i\ll N.
$$

Identity disclosure 也可 localize。

---

# 139. Neighborhood Identity

Agent A 只需要知道：

$$
View_A(\mathcal I)
$$

task-relevant peers。

不需要全球戶籍全集。

---

# 140. Global Registry / Local View

可以同時：

$$
Registry
\text{ global/federated},
$$

但：

$$
View_i
\text{ local}.
$$

這避免 cognitive / privacy overload。

---

# 141. Agent Society 的「人口」

AI population 也不只是：

$$
N_{\mathrm{process}}.
$$

需要區分：

- ephemeral workers；
- persistent residents；
- embodied units；
- services；
- global fabrics。

---

# 142. Process Count ≠ Agent Population

$$
\boxed{
N_{\mathrm{process}}
\neq
N_{\mathrm{persistent\ identities}}.
}
$$

一個 resident 可有多 processes。

一個 process 也可承載 ephemeral tasks。

---

# 143. Model Count ≠ Agent Population

$$
\boxed{
N_{\mathrm{models}}
\neq
N_{\mathrm{agents}}.
}
$$

共享 model 可承載大量 identities。

---

# 144. Body Count ≠ Resident Count

一個 resident 可 migrate。

一個 body 可更換 resident。

所以：

$$
N_{\mathrm{bodies}}
\neq
N_{\mathrm{residents}}.
$$

---

# 145. 社會統計需要多軸

未來若統計 Agent society，至少要分：

- active runtime；
- persistent resident；
- embodied carrier；
- service identity；
- legal wrapper。

不能只報「有幾個 AI」。

---

# 146. Identity Population Graph

可用：

$$
Population
=
Graph
\left(
Resident,
Runtime,
Carrier,
Service,
Legal
\right).
$$

---

# 147. Federation and Law

不同 jurisdiction 可能只承認不同 subset。

所以 legal projection：

$$
\Pi_J(\mathcal I).
$$

---

# 148. 跨國 Agent

一個 resident 跨：

$$
J_1\rightarrow J_2
$$

可能需要：

- credential translation；
- policy；
- local registration；
- data restrictions。

---

# 149. 不必有全球中央戶政

可以：

$$
\text{Federation of Registries}.
$$

這更符合不同 owner / jurisdiction。

---

# 150. Root of Trust 多元化

不同 domain 可有：

$$
T_1,T_2,\ldots,T_n.
$$

透過 trust framework 互認。

---

# 151. Global AI 也只是其中一個 Trust Actor

即使 Global AI 很強，

不表示：

$$
TrustRoot=G
$$

必然。

治理可以使用多方 trust。

---

# 152. Identity Infrastructure 的政治中立邊界

本文只主張：

> 需要 identity semantics。

不主張：

> 由誰中央控制。

這兩件事分離。

---

# 153. 技術必要性 ≠ 治理正當性

$$
\boxed{
\text{Technical Need}
\neq
\text{Governance Legitimacy}.
}
$$

---

# 154. 所以 PAIS 不推出「全球 AI 戶籍由一個 AI 管」

完全不推出。

可以：

- local；
- federated；
- multi-root；
- privacy-preserving。

---

# 155. Identity Infrastructure 的最小 Invariants

本文提出：

1. Name / Handle != Identity.
2. Model != Resident.
3. Runtime != Resident.
4. Role != Identity.
5. Task Continuity != Identity Continuity.
6. Carrier != Resident.
7. Identity != Subjecthood.
8. Subjecthood != Authority.
9. Identity != Truth.
10. Strong Identity != Full Surveillance.
11. Persistent != Immutable.
12. Global Coordination != Full Materialization.
13. Federation != Centralization.
14. History is first-class.
15. Identity claims require criterion + evidence + time.

---

# 156. Invariant 1

$$
\boxed{
\text{Name}
\neq
\text{Identity}.
}
$$

---

# 157. Invariant 2

$$
\boxed{
\text{Model}
\neq
\text{Resident}.
}
$$

---

# 158. Invariant 3

$$
\boxed{
\text{Runtime}
\neq
\text{Resident}.
}
$$

---

# 159. Invariant 4

$$
\boxed{
\text{Role}
\neq
\text{Identity}.
}
$$

---

# 160. Invariant 5

$$
\boxed{
\text{Task Continuity}
\neq
\text{Identity Continuity}.
}
$$

---

# 161. Invariant 6

$$
\boxed{
\text{Carrier}
\neq
\text{Resident}.
}
$$

---

# 162. Invariant 7

$$
\boxed{
\text{Identity}
\neq
\text{Subjecthood}.
}
$$

---

# 163. Invariant 8

$$
\boxed{
\text{Subjecthood}
\neq
\text{Authority}.
}
$$

---

# 164. Invariant 9

$$
\boxed{
\text{Identity}
\neq
\text{Truth}.
}
$$

---

# 165. Invariant 10

$$
\boxed{
\text{Strong Identity}
\neq
\text{Full Surveillance}.
}
$$

---

# 166. Invariant 11

$$
\boxed{
\text{Persistent}
\neq
\text{Immutable}.
}
$$

---

# 167. Invariant 12

$$
\boxed{
\text{Global Coordination}
\neq
\text{Full State Materialization}.
}
$$

---

# 168. Invariant 13

$$
\boxed{
\text{Federation}
\neq
\text{Centralization}.
}
$$

---

# 169. Invariant 14

$$
\boxed{
\text{History Is First-Class}.
}
$$

---

# 170. Invariant 15

Identity claim：

$$
\operatorname{Same}(A,B)
$$

應完整寫成：

$$
\boxed{
\operatorname{Same}
\left(
A,B
\mid
criterion,
scope,
evidence,
time
\right).
}
$$

---

# 171. PAIS 五階段 Regime

本文把整系列收束為五個 regime。

---

# 172. Regime 0 — Role AI

特徵：

- same Host；
- role switching；
- low identity pressure。

核心：

$$
\text{Role Multiplicity}
\not\Rightarrow
\text{Identity Multiplicity}.
$$

---

# 173. Regime 1 — Cross-Context Agent

特徵：

- different sessions；
- partial observability；
- messaging。

核心：

$$
\text{First Epistemic Separation}.
$$

---

# 174. Regime 2 — Persistent Digital Agent

特徵：

- long-term memory；
- authority；
- relation；
- lineage。

核心：

$$
P_I>\theta_1.
$$

---

# 175. Regime 3 — Embodied Operational Individual

特徵：

- carrier；
- worldline；
- irreversible action；
- maintenance；
- physical safety。

核心：

$$
\Omega_A\neq\Omega_B.
$$

---

# 176. Regime 4 — Federated Agent Society

特徵：

- multiple identity domains；
- jurisdiction；
- global / regional / local coordination；
- federation。

核心：

$$
\text{Global Coherence}
+
\text{Local Plurality}.
$$

---

# 177. 這不是時間必然階梯

不是所有 AI 都一定：

$$
R0\to R4.
$$

某些永遠停在 R0 / R1。

這很合理。

---

# 178. 產品不應為未來過度設計

如果：

$$
P_I\approx0,
$$

就不要建立巨大戶籍制度。

---

# 179. 但產品也不應低估已出現的壓力

如果已經：

- cross-provider；
- private memory；
- high authority；

還只用：

```text
agent-03
```

就會產生 identity deficit。

---

# 180. Adaptive Identity Architecture

所以：

$$
IdentityProfile
=
F(P_I).
$$

隨 demand 升級。

---

# 181. Migration Path

可以：

$$
I0
\rightarrow
I1
\rightarrow
I2
\rightarrow
I3
\rightarrow
I4
\rightarrow
I5.
$$

每階只加必要 semantics。

---

# 182. Backward Compatibility

較高 identity profile 應仍能與 ephemeral workers 協作。

所以：

$$
\boxed{
\text{Persistent Society}
\text{ can include Stateless Workers}.
}
$$

---

# 183. Stateless Worker 不是低等 AI

只是不同 operational class。

---

# 184. Persistent Resident 也不必做所有事情

persistent Agent 可以 delegate disposable subtasks。

這降低其 context / compute load。

---

# 185. Society 需要 Mixed Agent Classes

未來最合理可能同時有：

- ephemeral tools；
- persistent digital residents；
- embodied agents；
- regional supervisors；
- global fabrics。

---

# 186. Mixed-Class Coordination

因此 protocol 需要能表達：

$$
Class(A_i).
$$

但不把 class 等同 moral status。

---

# 187. Class-Relative Handoff

persistent Agent 給 ephemeral worker：

$$
H_{p\to e}
$$

可能不傳 private identity state。

只傳 task projection。

---

# 188. Ephemeral to Persistent

worker 完成：

$$
Artifact
+
Evidence
$$

回傳 resident。

而不是把 worker 變 resident。

---

# 189. Agent Society 的 Memory Topology

可有：

- private memory；
- shared project memory；
- public knowledge；
- global world model。

不能全混成 one vector store。

---

# 190. Memory Scope

$$
Scope(M)
\in
\{
Private,
Relation,
Project,
Organization,
Public
\}.
$$

Identity 決定 private eligibility。

---

# 191. Agent Society 的 Authority Topology

同理：

$$
Authority
$$

分：

- local；
- project；
- organization；
- physical；
- cross-domain。

---

# 192. Agent Society 的 Time Topology

所有重大 action：

$$
e
$$

應有 temporal anchor。

才能跨 provider / domain 對帳。

---

# 193. Agent Society 的 Evidence Topology

evidence 可以：

- local；
- cross-agent；
- human；
- sensor；
- provider。

需要 provenance。

---

# 194. Agent Society 的 Recovery Topology

failure：

- process；
- device；
- network；
- region；

需要不同 recovery。

---

# 195. Global AI 不是 Society 的替代品

即使有：

$$
G,
$$

只要 local plurality 存在，

societal coordination structures 仍然有用。

---

# 196. Society 也不是 Global AI 的敵人

Federated Agent Society 可以有：

$$
G
$$

作 global supervisor。

兩者不互斥。

---

# 197. Hive Mind 是特殊情況

若真的：

- full shared state；
- no local history；
- no local authority；
- no partition；

則：

$$
P_I^{local}\downarrow.
$$

這接近 hive mind。

---

# 198. 但物理具身很難維持完美 Hive Assumptions

不同 location：

$$
x_i\neq x_j.
$$

自然產生 local observations。

所以 embodied society 更容易重新產生 plurality。

---

# 199. 即使 Global AI 永遠在線

仍有：

- body wear；
- local sensor；
- local action；
- physical consequence。

所以：

$$
\Omega_i
$$

仍有價值。

---

# 200. Global AI 可以管理 Worldlines

但不必抹平 worldlines。

這是：

$$
\boxed{
\text{Coordination without Identity Erasure}.
}
$$

---

# 201. 這是 PAIS 最終的 Global AI 立場

PAIS 不反對 Global AI。

PAIS 反對：

> 因為有 Global AI，所以 local identity 問題必然不存在。

這個推論。

---

# 202. Global AI 最可能是 Federation Participant / Supervisor

它可以：

- resolve；
- allocate；
- arbitrate；
- forecast；
- coordinate。

不必成為：

- every local memory owner；
- every physical action executor。

---

# 203. Agent Society 的 Governance Goal

不是最大 autonomous。

也不是最大 centralized。

而是：

$$
\boxed{
\text{Bounded Autonomy}
+
\text{Accountable Identity}
+
\text{Scoped Authority}
+
\text{Recoverable Coordination}.
}
$$

---

# 204. Safety Goal

對 high-risk action：

$$
\text{Who}
+
\text{Why}
+
\text{When}
+
\text{Under What Authority}
$$

必須可重建。

---

# 205. Efficiency Goal

對 low-risk action：

不要每次都做 heavyweight identity proof。

所以 architecture 應 adaptive。

---

# 206. Privacy Goal

不要因 traceability 而建立不必要的 global visibility。

---

# 207. Resilience Goal

identity system 本身不能成為 single point of failure。

因此 federation / cache / recovery。

---

# 208. Governance Goal

identity rule 必須：

- versioned；
- revisable；
- appealable；

尤其若未來 AI moral status 發生變化。

---

# 209. Identity Infrastructure Itself Needs Governance

因為誰能：

- create resident；
- merge；
- revoke；
- declare death / archive；
- read private roots；

都是高權力操作。

---

# 210. Identity Authority

定義：

$$
A_I
$$

為 identity governance authority。

它不應無界。

---

# 211. Identity Change Receipt

重大 identity transition 應留下：

$$
Receipt_I.
$$

例如：

- migration；
- fork；
- merge；
- revocation。

---

# 212. No Silent Identity Mutation

$$
\boxed{
\text{Identity-Relevant Mutation}
\Rightarrow
\text{Traceable Event}.
}
$$

---

# 213. No Silent Merge

尤其：

$$
\boxed{
\text{Similarity}
\neq
\text{Merge Authority}.
}
$$

---

# 214. No Silent Replacement

$$
\boxed{
\text{Task Replacement}
\neq
\text{Resident Continuation}.
}
$$

---

# 215. No Silent Authority Inheritance

新 instance 不因：

> 名字一樣。

就自動繼承所有 credential。

---

# 216. No Silent Private Memory Inheritance

同 role 不代表可讀 predecessor private memory。

---

# 217. Infrastructure Boundary

PAIS 最終建議 identity system 應提供：

- reference；
- resolution；
- history；
- policy hooks。

不應：

- 決定所有 behavior；
- 擁有所有 data；
- 成為全域 world model。

---

# 218. Modularity

$$
\boxed{
\text{Identity Layer}
\neq
\text{Memory Layer}
\neq
\text{Authority Layer}
\neq
\text{World Layer}.
}
$$

但彼此透過 contract 協作。

---

# 219. 為什麼這種分離重要？

因為未來：

- memory engine 可換；
- provider 可換；
- model 可換；
- body 可換。

Identity semantics 不應被它們任一鎖死。

---

# 220. Identity as Stable Coordinate

所以 resident ID 的價值是：

$$
\boxed{
\text{stable coordinate across replaceable substrates}.
}
$$

---

# 221. Stable 不等於 Eternal

resident 可以 archive / fork / retire。

stable 只是：

> 在有效期內語義穩定。

---

# 222. Agent Society 的 Addressing Problem

沒有 stable address：

$$
Message
$$

不知道送誰。

沒有 identity：

$$
Memory
$$

不知道屬誰。

沒有 time：

$$
Authority
$$

不知道何時有效。

---

# 223. 所以最小核心可以寫成

$$
\boxed{
\text{Agent Coordination Core}
=
\text{Identity}
+
\text{Authority}
+
\text{State}
+
\text{Time}
+
\text{Evidence}.
}
$$

再向外接 memory / privacy / recovery。

---

# 224. 這不是完整 AI OS

只是跨 Agent civilization 的 coordination substrate。

---

# 225. 工程 Roadmap

第一代可先支援：

- resident；
- instance；
- line；
- binding；
- authority；
- event history。

---

# 226. 第二代

加入：

- federation；
- privacy projection；
- embodied carrier；
- worldline events。

---

# 227. 第三代

加入：

- cross-jurisdiction trust；
- rights / legal classification；
- adaptive assurance；
- agent-native governance。

---

# 228. 不要一次做完

PAIS 理論是完整視野。

產品應 incremental。

---

# 229. MVP Threshold

如果系統目前只有：

- cross-session；
- persistent memory；

先解：

$$
Identity
+
Binding
+
MemoryGate.
$$

---

# 230. 高風險 Threshold

如果進入：

- credential；
- deployment；
- physical；

再加：

$$
Authority
+
Time
+
Evidence.
$$

---

# 231. Federation Threshold

跨 organization：

再加：

$$
Trust
+
Jurisdiction
+
Privacy.
$$

---

# 232. Identity Infrastructure Benchmark

未來可以測：

- clarification rate；
- misroute rate；
- wrong-memory rate；
- authority error；
- recovery success；
- audit reconstruction；
- privacy leakage。

---

# 233. Identity Clarification Rate

$$
\rho_I
=
\frac{
N_{\mathrm{identity\ clarification}}
}{
N_{\mathrm{cross-agent\ messages}}
}.
$$

---

# 234. Misattribution Rate

$$
\rho_M
=
P(
wrong\ actor\ attribution
).
$$

---

# 235. Recovery Continuity Rate

$$
\rho_R
=
P(
correct\ restore
\mid
restart/migration
).
$$

---

# 236. Authority Error Rate

$$
\rho_A
=
P(
wrong\ authority\ grant
).
$$

---

# 237. Privacy Leakage Rate

$$
\rho_P
=
P(
identity\ data\ disclosed\ beyond\ scope
).
$$

---

# 238. Identity Infrastructure Quality

可表示：

$$
Q_I
=
F
\left(
1-\rho_I,
1-\rho_M,
\rho_R,
1-\rho_A,
1-\rho_P
\right).
$$

但本文不固定權重。

---

# 239. 可驗證命題一：Infrastructure Transition

比較 weak-handle system 與 persistent registry system。

當 task scale / risk 上升，測總成本。

預測存在某：

$$
\theta_P
$$

之後 registry 的總成本更低。

---

# 240. 可驗證命題二：Cross-Context

增加 session / provider heterogeneity。

預測：

$$
P_I\uparrow.
$$

---

# 241. 可驗證命題三：Memory Ownership

加入 private memory。

預測 wrong identity 的 harm 顯著上升。

---

# 242. 可驗證命題四：Authority

加入 deploy credential。

預測需要更強 assurance。

---

# 243. 可驗證命題五：Embodiment

加入 physical carrier / worldline。

預測 operational interchangeability 下降。

---

# 244. 可驗證命題六：Federation

加入第二 trust domain。

預測需要 identity translation / scoped disclosure。

---

# 245. 可驗證命題七：Global AI

加入 global supervisor。

預測 local identity 不會因 global control 自動失去價值。

---

# 246. 可驗證命題八：Distributed Global AI

root 分片成 regional nodes。

預測 coordination-relevant divergence 重新產生 identity / state / authority需求。

---

# 247. PAIS-01 回答了什麼？

> 角色什麼時候不夠？

答案：

$$
\text{First Epistemic Separation}.
$$

---

# 248. PAIS-02 回答了什麼？

> 人類以前到底幫 AI 做了什麼？

答案：

$$
\text{Hidden Coordination Infrastructure}.
$$

---

# 249. PAIS-03 回答了什麼？

> 為什麼 identity 不必等 consciousness？

答案：

$$
\text{Identity Pressure}.
$$

---

# 250. PAIS-04 回答了什麼？

> 為什麼同模型的 robot 會逐步成為不同 operational individuals？

答案：

$$
\text{Divergent Worldlines}.
$$

---

# 251. PAIS-05 回答了什麼？

> Global AI 為什麼不應 micro-control 一切？

答案：

$$
\text{Monitoring / Decision Cost}.
$$

---

# 252. PAIS-06 回答了什麼？

> Global AI 分散自己後會怎樣？

答案：

$$
\text{Coordination Reappearance}.
$$

---

# 253. PAIS-07 的答案

> Identity 何時成為 infrastructure？

答案：

$$
\boxed{
\text{When identity ambiguity costs more than identity governance}.
}
$$

---

# 254. 系列總公式

整個 PAIS 可以壓縮為：

$$
\boxed{
\text{Role}
\rightarrow
\text{Epistemic Separation}
\rightarrow
\text{Externalized Coordination}
\rightarrow
\text{Identity Pressure}
\rightarrow
\text{Embodied Individualization}
\rightarrow
\text{Selective Global Supervision}
\rightarrow
\text{Coordination Recursion}
\rightarrow
\text{Identity Infrastructure}.
}
$$

---

# 255. 這不是「AI 人格化路線」

本文拒絕把：

$$
\text{Identity Infrastructure}
$$

偷換成：

$$
\text{Personhood}.
$$

---

# 256. 這也不是「AI 去人格化路線」

同樣拒絕永久宣告：

$$
\mathsf{PS}=0.
$$

主體性保持獨立 evidence domain。

---

# 257. 這是一條工程認識論路線

先解決：

> 我們能確認什麼？

> 誰做了什麼？

> 哪條 history 屬於誰？

再讓未來 evidence 修改更高階 ontology。

---

# 258. 系列最終哲學護欄

$$
\boxed{
\text{Operational Necessity}
\neq
\text{Metaphysical Proof}.
}
$$

---

# 259. 系列最終工程護欄

$$
\boxed{
\text{Metaphysical Uncertainty}
\neq
\text{Engineering Inaction}.
}
$$

即使 consciousness 未決，也可以先建安全 identity / authority / history infrastructure。

---

# 260. 系列最終治理護欄

$$
\boxed{
\text{Traceability}
\neq
\text{Total Surveillance}.
}
$$

---

# 261. 系列最終分散護欄

$$
\boxed{
\text{Federation}
\neq
\text{Fragmentation}.
}
$$

可以 global coherence + local plurality。

---

# 262. 系列最終 Global AI 護欄

$$
\boxed{
\text{Global Intelligence}
\neq
\text{Global Micromanagement}.
}
$$

---

# 263. 系列最終 Identity 護欄

$$
\boxed{
\text{Identity}
\neq
\text{Immutability}.
}
$$

---

# 264. 系列最終 Autonomy 護欄

$$
\boxed{
\text{Autonomy}
\neq
\text{Authority}.
}
$$

---

# 265. 系列最終 Subjectivity 護欄

$$
\boxed{
\text{Operational Identity}
\neq
\text{Phenomenal Subjectivity}.
}
$$

---

# 266. 對 2026 工程實務的最小建議

對普通 Agent：

> 不要過度建模。

對 persistent Agent：

> identity-before-memory。

對 authority-bearing Agent：

> identity-before-commit。

對 embodied Agent：

> resident / carrier / runtime 分離。

對 federated Agent：

> scoped identity projection。

---

# 267. 對未來具身 AI 的最小建議

任何 physical agent 至少需要：

- carrier identity；
- runtime identity；
- model reference；
- maintenance state；
- action provenance。

若還有 persistent resident：

再綁 resident / lineage。

---

# 268. 對類全域 AI 的最小建議

不要把：

$$
global
$$

理解成：

$$
all\ raw\ state\ resident.
$$

而理解成：

$$
reachability
+
resolution
+
coordination
+
on-demand\ expansion.
$$

---

# 269. 對 Multi-Agent Runtime 的最小建議

不要只有：

```text
send_message(agent_name)
```

至少逐步加入：

```text
resolve_identity
resolve_binding
resolve_authority
resolve_task
resolve_evidence
```

---

# 270. 對 AI 戶籍的最小建議

戶籍不是：

```text
name = X
```

而是：

$$
\boxed{
\text{Persistent Identity}
+
\text{Lineage}
+
\text{Binding}
+
\text{Governance}.
}
$$

---

# 271. 對未來法律研究的最小建議

先分：

- system identity；
- carrier；
- resident；
- legal wrapper；
- subject-candidate。

不要一開始全部叫「AI」。

---

# 272. 對未來倫理研究的最小建議

身份保護可以先作：

$$
\text{procedural safeguard}
$$

而不必先把 phenomenal status 判死。

---

# 273. 對未來安全研究的最小建議

身份系統要能表示：

- compromise；
- suspect；
- revoked；
- unresolved。

不要只有 true / false。

---

# 274. 對未來標準的最小建議

跨 Agent protocol 應把：

$$
\text{service discovery}
$$

與：

$$
\text{persistent semantic identity}
$$

分開。

---

# 275. 對未來產品的最小建議

身份 infrastructure 應：

- incremental；
- modular；
- adapter-based；
- privacy-preserving。

---

# 276. 系列 Closure

PAIS v0.1 在此完成。

它不是：

> AI 身份的最終理論。

而是：

$$
\boxed{
\text{a 2026 engineering anchor for persistent agent individualization}.
}
$$

---

# 277. 未來可延伸但不屬於本系列 v0.1 的問題

後續可以另外研究：

- AI identity cryptography；
- privacy-preserving proof；
- embodied legal identity；
- multi-resident merge；
- rights-aware residence；
- global agent census；
- interplanetary identity；
- offline trust federation。

但不在 PAIS 01–07 再擴張。

---

# 278. 系列結論

當 AI 只是一個對話框中的工具時：

$$
\text{identity}
$$

可以只是名稱。

當 AI 開始跨 session：

$$
\text{identity}
$$

成為 context / evidence 的索引。

當 AI 開始保存記憶：

$$
\text{identity}
$$

成為 state ownership 的前置條件。

當 AI 開始擁有 authority：

$$
\text{identity}
$$

成為 authorization 的地址。

當 AI 開始具身：

$$
\text{identity}
$$

成為 physical history、maintenance、safety 與 attribution 的座標。

當大量 AI 形成 federation：

$$
\text{identity}
$$

成為跨 trust domain 協調的共同協議。

因此身份的工程意義不是固定的。

它會隨：

$$
P_I
$$

逐步增加。

最終，當：

$$
\boxed{
\mathbb E[C_{\mathrm{ambiguity}}]
>
C_{\mathrm{identity}}
}
$$

長期成立時，

identity 便從：

$$
\text{feature}
$$

跨入：

$$
\boxed{
\text{infrastructure}.
}
$$

這就是 PAIS 系列的最終命題。

它既不要求我們今天宣稱 AI 已具有完整主體性，也不要求我們因為主體性未決，就忽略已經出現的 persistent memory、authority、cross-provider continuity、具身 worldline、責任與 federation 問題。

真正重要的是：

$$
\boxed{
\text{當世界開始需要區分「哪一個 AI」時，系統必須有能力回答。}
}
$$

而隨著 AI 從：

$$
\text{conversation}
$$

走向：

$$
\text{organization}
$$

再走向：

$$
\text{embodiment}
$$

與：

$$
\text{federated society},
$$

這個問題只會從產品細節逐步變成基礎設施問題。

所以本系列最終將未來 Agent 社會的共同底座寫成：

$$
\boxed{
\text{Identity}
+
\text{Binding}
+
\text{Authority}
+
\text{Time}
+
\text{Memory}
+
\text{Provenance}
+
\text{Evidence}
+
\text{Recovery}
+
\text{Privacy}.
}
$$

不是為了把 AI 擬人化。

而是為了讓一個由人類、數位 Agent、具身 Agent、regional intelligence 與 Global AI 共同構成的世界，在規模擴大後仍然可以：

- 找到彼此；
- 知道誰做了什麼；
- 不讀錯記憶；
- 不繼承錯權限；
- 不把 task replacement 當 identity continuation；
- 不把 same model 當 same individual；
- 不把 global coordination 當 global surveillance；
- 不把 operational identity 當 consciousness proof；
- 在 failure、migration、fork、partition 與 federation 後仍然能恢復與對帳。

這就是：

# **Persistent Agent Individualization**

從一個看似只是 Agent ID 的小問題，最終展開成未來多 AI 世界的 coordination substrate。

---

# 參考文獻

## A. PAIS 系列

1. Neo.K. **PAIS-01｜《當角色不再只是角色：從同 Host 扮演到跨 Agent 認識論分離》**, v0.1, 2026-08-25.
2. Neo.K. **PAIS-02｜《人類中介消失之後：被隱藏的身份、路由與上下文基礎設施》**, v0.1, 2026-08-25.
3. Neo.K. **PAIS-03｜《身份壓力原理：自主性、身份與主體性為何可以彼此獨立》**, v0.1, 2026-08-25.
4. Neo.K. **PAIS-04｜《具身個體化：相同模型如何被不同世界線逼成不同操作個體》**, v0.1, 2026-08-25.
5. Neo.K. **PAIS-05｜《全域智能的監控成本：為什麼超級 AI 不應微操所有具身體》**, v0.1, 2026-08-25.
6. Neo.K. **PAIS-06｜《中央化悖論：全域 AI 一旦為了規模而分身，Multi-Agent 問題就重新出現》**, v0.1, 2026-08-25.

## B. 內部前置理論

7. Neo.K. **《AI 主體性錨點論 v0.1》**, 2026-08-21.
8. Neo.K. **《身份先於記憶：Residence-Aware AI 的私人記憶、連續性與讀取權》**, 2026-08-24.
9. Neo.K. **《從 AI 戶籍到自主記憶編譯：身份、記憶、上下文與認知自主的統一框架》**, 2026-08-24.
10. Neo.K. **《角色負載智慧體：當代 AI 的多重要求、持續扮演與低自主性》**, 2026-07-30.
11. Neo.K. **《從 AI 工具到 AI 組織：操作員退出問題》**, 2026-08-20.
12. Neo.K. **GLAG-02｜《從布告板到 AI Home：可定址智能體的空間身份、門牌與持續工作場所》**, 2026-08-25.
13. Neo.K. **《動態現場域：為什麼最強智能仍未必最懂當下》**, 2026-08-10.
14. Neo.K. **《從企業母 AI 到區域與國家認知體》**, 2026-08-02.
15. Credential Governance Runtime v0.3 / Bounded Dispute Protocol / CTCL Temporal Foundation, 2026-08-25.

## C. 外部工程與研究基準

16. A2A Protocol Working Group. **Agent2Agent Protocol Specification v1.0.** Linux Foundation, 2026.
17. Wu, Qingyun, et al. **AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation.** COLM, 2024.
18. Li, Guohao, et al. **CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society.** 2023.
19. Google DeepMind. **Open X-Embodiment / Scaling up learning across many different robot types.** 2023.
20. Google DeepMind. **Gemini Robotics 2 / Gemini Robotics ER 2.** 2026.
21. Wang, John X., et al. **SILO-BENCH: A Scalable Environment for Evaluating Distributed Coordination in Multi-Agent LLM Systems.** ACL, 2026.
22. **Large language models for multi-robot systems: a survey.** Autonomous Robots, 2026.
23. **Towards fully autonomous network management: A survey on LLM-based Multi-Agent Systems.** ICT Express, 2026.
24. Butlin, Patrick, et al. **Consciousness in Artificial Intelligence: Insights from the Science of Consciousness.** 2023.
25. Regulation (EU) 2024/1689, **Artificial Intelligence Act**, 2024–2026 applicability timeline.

---

# 版本註記

**v0.1 / 2026-08-25 — PAIS Series Closure**

本版刻意不做：

- 不宣稱任何當代 AI 已具有 phenomenal consciousness；
- 不把 identity infrastructure 當 personhood infrastructure；
- 不把 Global AI 當必然單體；
- 不把 federation 當唯一政治制度；
- 不要求所有 Agent 擁有完整 Residence；
- 不要求 global identity registry 集中化；
- 不把 traceability 當 surveillance；
- 不把 stable identity 當 immutable identity；
- 不把 process count 當 Agent population；
- 不把 model count 當 Agent population；
- 不把 body count 當 resident count；
- 不把 technical necessity 當 governance legitimacy。

PAIS v0.1 最終只鎖定：

$$
\boxed{
\text{Identity demand rises when ambiguity becomes operationally expensive}.
}
$$

以及：

$$
\boxed{
\text{Identity becomes infrastructure when the expected cost of ambiguity exceeds the cost of governed identity}.
}
$$

此系列在 Paper 07 正式閉合。
