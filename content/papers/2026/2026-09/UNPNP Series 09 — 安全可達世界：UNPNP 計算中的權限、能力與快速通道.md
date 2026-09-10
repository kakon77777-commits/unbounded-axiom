# UNPNP Series 09
## 安全可達世界：UNPNP 計算中的權限、能力與快速通道
### Safe Reachable Worlds: Permission, Capability, and Fast Paths in UNPNP Computation

**系列名稱：** UNPNP Hyperlink & Crystallized Computation Series  
**系列篇次：** 09  
**作者：** Neo.K with Aletheia（GPT）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-07  
**文件性質：** AI 原生計算／權限與安全邊界／UNPNP 理論論文  
**狀態：** Canonical Draft  

---

## 摘要

UNPNP 前八篇逐步建立了複雜度轉移、跨底空間超連結、自適應快速通道、展開—連結—收斂、耦合計算、路徑編譯、計算結晶化，以及有效度超連結路徑編碼。當這些能力結合後，一個 AI-native runtime 可能在極短時間內穿越多個底空間，執行一串已驗證或已結晶的快速 transition。

然而，計算效率的提升具有一個直接且對稱的風險：

$$
\boxed{
\text{合法計算的快速通道，也可能成為錯誤、攻擊或權限濫用的快速通道。}
}
$$

因此，UNPNP 的安全性不能被視為後加模組，而必須成為跨底空間 transition 的一部分。本文提出 **Safe Reachable World**：任一時刻，AI 或其他計算主體實際可運行的世界，不等於其能觀察或知道存在的全部世界，而應被 capability、identity、risk、policy 與 execution context 共同裁剪：

$$
\boxed{
\mathcal W_t^{\mathrm{accessible}}
=
\mathcal W
\cap
\mathcal R(
I_t,
C_t,
P_t,
R_t
).
}
$$

其中：

- $I_t$：當前行動主體與身分上下文；
- $C_t$：capability envelope；
- $P_t$：policy / permission state；
- $R_t$：risk state；
- $\mathcal R$：可達域生成函數。

本文正式提出：

$$
\boxed{
\text{Reachable}
\neq
\text{Authorized}
\neq
\text{Trusted}
\neq
\text{Safe}
}
$$

以及：

$$
\boxed{
\text{Learning}
\not\Rightarrow
\text{Self-Authorization}.
}
$$

AI 可以學會一條更好的路，但不能因為「這條路更快」而自行取得原本不存在的權限。

本文不主張第一代 UNPNP runtime 應直接實作大型企業級 IAM、複雜組織權限樹或跨機構身份聯邦。相反，本文主張先建立一個最小但嚴格的安全骨架：多道閘門、明確 actor identity、capability envelope、risk class、guard、validator、receipt、rollback / fallback 與 fail-closed。

本文進一步將實驗世界分為三個主要域：

$$
\boxed{
\mathcal W_{\mathrm{internal}}
\subset
\mathcal W_{\mathrm{read}}
\subset
\mathcal W_{\mathrm{act}}.
}
$$

第一階段主要允許內部 sandbox、單機遊戲、本地資料、測試 repo 與可回滾狀態；第二階段可以加入受控 external read；第三階段的 external write、不可逆動作、金流、權限變更與 production mutation 應在安全模型成熟前排除在自動 fast path 之外。

本文亦提出 **Authorized Shortest Path**：

$$
\boxed{
\Gamma^\*
=
\arg\min_{
\Gamma
\in
\mathcal P_{\mathrm{authorized}}
}
C(\Gamma)
}
$$

表示 UNPNP 不應搜尋「所有可能路徑中的最快路」，而應搜尋「被授權可行域中的最低成本路徑」。

最後，本文建立 fast path 與 guarded slow path 的安全對偶：穩定、低風險、可逆且 capability 已界定的路徑可以高度耦合與結晶；高風險、未知、不可逆、外部寫入或權限改變的路徑則必須重新展開、增加驗證，甚至要求額外主體審批。

本文的核心原則可以壓縮為：

$$
\boxed{
\textbf{
Couple computation, isolate authority.
}
}
$$

以及：

$$
\boxed{
\textbf{
安全不是讓 AI 走得慢，而是限制它只在正確的可達世界裡走得快。
}
}
$$

**關鍵詞：** UNPNP、Safe Reachable World、Capability、Authorization、Identity、Fast Path、Fail-Closed、Sandbox、Permission Boundary、AI Security、Typed Hyperlink

---

# 1. 為什麼安全必須進入 UNPNP 本體？

如果：

$$
B_1
\rightarrow
B_2
\rightarrow
\cdots
\rightarrow
B_{100}
$$

已被編譯成：

$$
B_1
\rightarrow
B_{100},
$$

那麼原本散布於中間：

- identity check；
- permission check；
- data validation；
- side-effect boundary；
- audit；

的安全摩擦也可能一起被壓掉。

所以：

$$
\boxed{
\text{path compression}
\not\Rightarrow
\text{security compression}.
}
$$

---

# 2. 快速通道的對稱風險

若：

$$
C_{\mathrm{legitimate}}
\downarrow,
$$

攻擊者若能借用同一通道，

其：

$$
C_{\mathrm{attack}}
$$

也可能下降。

因此：

$$
\boxed{
\text{optimization}
\Rightarrow
\text{attack-surface reconsideration}.
}
$$

---

# 3. Reachable 不等於 Authorized

最基本：

$$
\boxed{
\text{Reachable}
\neq
\text{Authorized}.
}
$$

AI 可以知道：

$$
B_j
$$

存在，

也可以解析：

$$
a_j,
$$

但仍不代表：

$$
\operatorname{Traverse}(B_i,B_j)
$$

被允許。

---

# 4. Authorized 不等於 Trusted

即使某 transition 被允許，

其來源：

$$
S
$$

仍可能不可信。

所以：

$$
\boxed{
\text{Authorized}
\neq
\text{Trusted}.
}
$$

---

# 5. Trusted 不等於 Safe

可信來源也可能：

- bug；
- stale；
- misconfigured；
- incompatible。

因此：

$$
\boxed{
\text{Trusted}
\neq
\text{Safe}.
}
$$

---

# 6. Safe 不等於 Globally Optimal

最安全路不一定最快，

最快路也不一定安全。

因此：

$$
\boxed{
\text{Safety}
\neq
\text{Optimality}.
}
$$

---

# 7. 四層分離

本文提出：

$$
\boxed{
\text{Reachability}
\neq
\text{Authorization}
\neq
\text{Trust}
\neq
\text{Safety}.
}
$$

這四者必須分開建模。

---

# 8. 行動主體 Identity

任何有副作用 transition 都應回答：

> 誰在做？

令：

$$
I_t
$$

為 actor identity。

第一代可簡化為：

$$
I_t
\in
\{
\text{system},
\text{human-owner},
\text{agent},
\text{external}
\}.
$$

---

# 9. Identity 不必一開始複雜化

第一版目標不是完整身份聯邦。

而是保證：

$$
\boxed{
\text{every privileged action has an attributable actor context}.
}
$$

---

# 10. Delegated Identity

若：

$$
I_0
\rightarrow
I_1
\rightarrow
I_2,
$$

表示：

$$
I_0
$$

委託：

$$
I_1,
$$

再委託：

$$
I_2.
$$

---

# 11. Delegation Chain

可以寫：

$$
D_I
=
(
I_0,
I_1,
\ldots,
I_n
).
$$

每次 delegation 都應攜帶 capability 範圍。

---

# 12. Capability Envelope

令：

$$
C_t
$$

為當前能力集合。

例如：

$$
C_t
=
\{
\text{read-web},
\text{read-local},
\text{write-temp},
\text{sandbox-exec}
\}.
$$

---

# 13. Capability 不等於角色名稱

「Agent」不是權限。

真正權限在：

$$
C_t.
$$

因此：

$$
\boxed{
\text{Role label}
\neq
\text{Capability set}.
}
$$

---

# 14. Capability Attenuation

委託後應滿足：

$$
\boxed{
C_{n+1}
\subseteq
C_n.
}
$$

即下游 capability 不應無條件放大。

---

# 15. Capability Amplification 需要新授權

若：

$$
C_{n+1}
\supset
C_n,
$$

則必須：

$$
\operatorname{Reauthorize}=1.
$$

---

# 16. Learning 不能提升權限

即使 AI 學到：

$$
\Gamma_{\mathrm{privileged}}
$$

很有效，

也不能：

$$
C_t
\rightarrow
C_t'
$$

自行加入 privileged capability。

所以：

$$
\boxed{
\text{Learning}
\not\Rightarrow
\text{Self-Authorization}.
}
$$

---

# 17. Safe Reachable World

定義：

$$
\boxed{
\mathcal W_t^{\mathrm{accessible}}
=
\mathcal W
\cap
\mathcal R(
I_t,
C_t,
P_t,
R_t
).
}
$$

---

# 18. 全域世界與可達世界

$$
\mathcal W
$$

可以很大。

但：

$$
\mathcal W_t^{\mathrm{accessible}}
$$

只包含：

> 目前主體在目前能力、政策與風險條件下可以合法操作的底空間與 transition。

---

# 19. 可見世界與可執行世界

還可區分：

$$
\mathcal W_t^{\mathrm{visible}}
$$

與：

$$
\mathcal W_t^{\mathrm{executable}}.
$$

通常：

$$
\boxed{
\mathcal W_t^{\mathrm{executable}}
\subseteq
\mathcal W_t^{\mathrm{visible}}.
}
$$

---

# 20. 看得到但不能做

這是必要狀態。

例如 AI 可以看到：

$$
\text{payment endpoint}
$$

存在，

但：

$$
\text{execute-payment}
\notin
C_t.
$$

---

# 21. Multi-Gate Model

第一代不需要複雜權限樹。

但至少需要多道閘門：

$$
G_1
\rightarrow
G_2
\rightarrow
G_3
\rightarrow
G_4.
$$

---

# 22. Gate 1：Identity Gate

確認：

$$
I_t.
$$

---

# 23. Gate 2：Capability Gate

確認：

$$
C_{\mathrm{req}}(\Theta)
\subseteq
C_t.
$$

---

# 24. Gate 3：Risk Gate

確認：

$$
R(\Theta)
\le
R_{\max}(\text{context}).
$$

---

# 25. Gate 4：Execution Guard

確認：

$$
G_\Theta(s_t)=1.
$$

---

# 26. Gate 5：Post-Verification

執行後：

$$
V_\Theta(s_{t+1})=1.
$$

---

# 27. 多道閘門不等於每次問人類

若每一步：

> 是否允許？

都要求人類點確認，

fast path 會失去意義。

所以：

$$
\boxed{
\text{multi-gate}
\neq
\text{human confirmation every step}.
}
$$

---

# 28. Preauthorized Capability Domain

人類可以先授權：

$$
C_{\mathrm{session}}.
$$

在：

$$
C_{\mathrm{session}}
$$

內的低風險路徑可直接走 fast path。

---

# 29. Capability-Bounded Fast Path

即：

$$
\boxed{
\text{Fast Path}
\subset
C_{\mathrm{session}}.
}
$$

---

# 30. Fast Authorization

授權也可以被編譯成低成本 guard。

例如：

$$
V_{\mathrm{cap}}
=
\operatorname{CheckToken}
(
C_{\mathrm{req}},
C_t
).
$$

---

# 31. Fast Authorization 不等於 No Authorization

所以：

$$
\boxed{
C_{\mathrm{auth-fast}}
\ll
C_{\mathrm{auth-deep}}
}
$$

可以，

但：

$$
C_{\mathrm{auth}}=0
$$

不應成為高權限預設。

---

# 32. Risk Classes

第一版可以定義：

$$
R_0
=
\text{pure read},
$$

$$
R_1
=
\text{local reversible write},
$$

$$
R_2
=
\text{sandbox execution},
$$

$$
R_3
=
\text{external reversible action},
$$

$$
R_4
=
\text{external irreversible action}.
$$

---

# 33. 第一代允許域

主要：

$$
R_0,R_1,R_2.
$$

這非常適合遊戲實驗。

---

# 34. 第一代排除域

預設排除：

$$
R_4.
$$

例如：

- payment；
- account privilege mutation；
- destructive production write；
- irreversible external publish；
- critical infrastructure control。

---

# 35. 這不是理論禁止

而是：

$$
\boxed{
\text{Deployment Maturity Boundary}.
}
$$

即理論上可研究，

但第一代不部署。

---

# 36. 三大實驗世界

本文建議：

$$
\boxed{
\mathcal W_{\mathrm{internal}},
\mathcal W_{\mathrm{external-read}},
\mathcal W_{\mathrm{external-act}}.
}
$$

---

# 37. Internal World

$$
\mathcal W_{\mathrm{internal}}
$$

包括：

- single-player game；
- synthetic world；
- test repo；
- local database；
- mock API；
- sandbox process；
- generated fixtures。

---

# 38. External Read World

$$
\mathcal W_{\mathrm{external-read}}
$$

包括：

- public web；
- public GitHub；
- public API；
- read-only database；
- read-only connector。

---

# 39. External Action World

$$
\mathcal W_{\mathrm{external-act}}
$$

包括：

- send mail；
- publish；
- production write；
- delete；
- payment；
- privilege mutation；
- account management。

---

# 40. 分階段擴張

建議：

$$
\boxed{
\mathcal W_{\mathrm{internal}}
\rightarrow
\mathcal W_{\mathrm{external-read}}
\rightarrow
\mathcal W_{\mathrm{external-act}}.
}
$$

---

# 41. 不需要一開始就像 Google

大型企業 IAM：

- 多租戶；
- 跨組織；
- 法規；
- 多角色；
- temporary elevation；
- audit；
- federation；

非常複雜。

第一代 UNPNP 不需要直接複製。

---

# 42. Minimal Security Core

第一版只需：

$$
\boxed{
I
+
C
+
R
+
G
+
V
+
\text{Receipt}.
}
$$

---

# 43. Typed Secure Hyperlink

將 Series 02 的 hyperlink 擴充為：

$$
\boxed{
\ell_{\mathrm{secure}}
=
\langle
a,
\tau,
I,
C,
R,
G,
E,
V,
P,
F
\rangle.
}
$$

其中：

- $a$：address；
- $\tau$：transition type；
- $I$：allowed actor context；
- $C$：required capabilities；
- $R$：risk class；
- $G$：guard；
- $E$：execution semantics；
- $V$：validator；
- $P$：provenance；
- $F$：fallback / rollback。

---

# 44. Security Is Part of Link Semantics

所以：

$$
\boxed{
\text{secure hyperlink}
\neq
\text{hyperlink}
+
\text{later security plugin}.
}
$$

---

# 45. Authorized Shortest Path

傳統 shortest path：

$$
\Gamma^\*
=
\arg\min_{\Gamma}
C(\Gamma).
$$

安全版：

$$
\boxed{
\Gamma^\*
=
\arg\min_{
\Gamma
\in
\mathcal P_{\mathrm{authorized}}
}
C(\Gamma).
}
$$

---

# 46. Authorized Path Set

$$
\mathcal P_{\mathrm{authorized}}
=
\{
\Gamma:
\forall \Theta_i\in\Gamma,
\operatorname{Authorize}(\Theta_i)=1
\}.
$$

---

# 47. Risk-Adjusted Path

更完整：

$$
\Gamma^\*
=
\arg\min_{\Gamma}
\left[
C(\Gamma)
+
\lambda
R(\Gamma)
\right]
$$

subject to：

$$
\operatorname{Auth}(\Gamma)=1.
$$

---

# 48. Lowest Cost 不等於最低步數

仍然：

$$
|\Gamma_1|<|\Gamma_2|
$$

不代表：

$$
C(\Gamma_1)<C(\Gamma_2).
$$

---

# 49. Security Cost 也算成本

因此：

$$
C(\Gamma)
$$

應包含：

$$
C_{\mathrm{security}}.
$$

安全不是「額外免費」。

---

# 50. Security Fast Path

如果：

$$
\Gamma
$$

長期：

- stable；
- low-risk；
- authorized；
- reversible；

則 security checks 本身也可被 fast-compiled。

---

# 51. Security Slow Path

若：

- identity changed；
- capability changed；
- risk increased；
- environment changed；
- provenance uncertain；

則：

$$
\text{fast security}
\rightarrow
\text{deep security}.
$$

---

# 52. Fail-Closed

若 authorization：

$$
A(\Theta)=\mathsf{unknown},
$$

則：

$$
\boxed{
\mathsf{unknown}
\rightarrow
\mathsf{deny}
}
$$

或：

$$
\mathsf{escalate}.
$$

不能：

$$
\mathsf{unknown}\rightarrow\mathsf{allow}.
$$

---

# 53. Fail-Closed 與性能

Fail-closed 不代表：

> 一切慢。

只對：

$$
\text{uncertain path}
$$

走 slow path。

已知安全 path 仍可以高速。

---

# 54. Prompt Injection 的抽象風險

如果外部輸入：

$$
U
$$

能影響：

$$
\mathcal M
$$

選 route，

而 AI 擁有：

$$
C_{\mathrm{privileged}},
$$

可能出現：

$$
U
\rightarrow
AI(C_{\mathrm{privileged}})
\rightarrow
\text{privileged action}.
$$

---

# 55. Confused Deputy

這正是：

$$
\boxed{
\text{Confused Deputy}
}
$$

的 AI-native 版本。

---

# 56. 外部內容不應繼承 Agent Capability

所以：

$$
\boxed{
C(U)
\not\Rightarrow
C(AI).
}
$$

更準確：

> untrusted content 不應因被高權限 AI 讀取，就取得高權限影響力。

---

# 57. Data-to-Action Barrier

外部內容到 action 之間至少要有：

$$
\boxed{
\text{interpretation}
\rightarrow
\text{policy}
\rightarrow
\text{capability}
\rightarrow
\text{execution}.
}
$$

---

# 58. 讀取與命令分離

即：

$$
\boxed{
\text{Retrieved instruction}
\neq
\text{authorized instruction}.
}
$$

---

# 59. Provenance Boundary

每個 transition 應知道：

> 這個決策受到哪些來源影響？

不用保存 chain-of-thought，

但要有：

$$
P_{\mathrm{source}}.
$$

---

# 60. Poisoned Fast Path

若一條：

$$
\kappa
$$

建立時資料被污染，

則它可能：

$$
\boxed{
\text{fail fast}.
}
$$

---

# 61. Fast Invalidation

所以：

$$
\boxed{
\text{fast path}
\Rightarrow
\text{fast invalidation}.
}
$$

---

# 62. Invalidation Signals

包括：

- capability change；
- identity change；
- version change；
- dependency hash mismatch；
- validator failure；
- abnormal execution；
- provenance alert。

---

# 63. Security Crystal

可以有：

$$
\kappa_{\mathrm{sec}}.
$$

保存：

- known-safe route；
- denied route；
- rollback；
- capability contract。

---

# 64. Negative Security Crystal

反覆證明某 route 不安全，

可以：

$$
\kappa_{\mathrm{deny}}^-.
$$

讓 Expansion 階段直接遮蔽。

---

# 65. 安全經驗也能結晶

所以安全學習：

$$
\boxed{
\text{not only faster allow,
but faster deny}.
}
$$

---

# 66. 但權限不能被結晶成擴張

即：

$$
\boxed{
\text{frequent success}
\not\Rightarrow
\text{broader permission}.
}
$$

---

# 67. Permission Drift

若：

$$
C_t
$$

改變，

所有依賴該 capability 的 crystal 必須 revalidate。

---

# 68. Capability Dependency Graph

建立：

$$
G_C
=
(V_K,E_C).
$$

其中：

$$
\kappa_i
\rightarrow
c_j
$$

表示 crystal 依賴 capability。

---

# 69. Revocation

若：

$$
c_j
$$

被撤銷，

則：

$$
\forall \kappa_i:
c_j\in C_{\mathrm{req}}(\kappa_i),
$$

全部降級。

---

# 70. Revocation 必須快

否則：

$$
\text{stale authorization window}
$$

會成為攻擊面。

---

# 71. Session Capability

第一代可採：

$$
C_{\mathrm{session}}.
$$

每次 session 開始時固定。

---

# 72. Task Capability

更細：

$$
C_{\mathrm{task}}
\subseteq
C_{\mathrm{session}}.
$$

每個 task 只拿需要能力。

---

# 73. Least Capability Principle

本文提出：

$$
\boxed{
\text{Grant the minimum capability required for the current corridor.}
}
$$

---

# 74. Capability by Corridor

如果：

$$
\Gamma
$$

只需要：

$$
\{c_1,c_2\},
$$

則不應給：

$$
\{c_1,\ldots,c_{10}\}.
$$

---

# 75. Capability Narrowing

Corridor Generator 在選 path 時可同時最小化：

$$
|C_{\mathrm{req}}(\Gamma)|.
$$

---

# 76. Security-Aware Utility

Series 08 的：

$$
U_H
$$

加入：

$$
C_{\mathrm{risk}}
$$

與：

$$
C_{\mathrm{privilege}}.
$$

所以：

$$
\boxed{
U_H^{\mathrm{secure}}
=
U_H
-
\lambda_RR
-
\lambda_P|C_{\mathrm{req}}|.
}
$$

---

# 77. 少權限本身是價值

兩條同成本路徑：

$$
\Gamma_1,
\Gamma_2.
$$

若：

$$
C_{\mathrm{req}}(\Gamma_1)
\subset
C_{\mathrm{req}}(\Gamma_2),
$$

通常優先：

$$
\Gamma_1.
$$

---

# 78. Reversible First

同理：

$$
\operatorname{Reversible}(\Gamma_1)=1
$$

比不可逆路徑更適合 fast path。

---

# 79. 安全與 Repairability

若路徑可以：

$$
\operatorname{Rollback},
$$

失敗損害較低。

因此 repairability 也是 security utility。

---

# 80. Internal Game Experiment

單機遊戲中：

$$
\mathcal W_{\mathrm{game}}
$$

非常適合測：

- capability scope；
- save / rollback；
- negative crystal；
- fast authorization；
- state isolation。

---

# 81. 遊戲權限可以簡化

例如：

$$
C_{\mathrm{game}}
=
\{
\text{read-state},
\text{local-action},
\text{save},
\text{reload}
\}.
$$

不需要企業 IAM。

---

# 82. Mod / Test Runtime

甚至可把：

$$
\text{write-game-state}
$$

限制在：

$$
\text{test copy}.
$$

---

# 83. Sandbox as Subspace

Sandbox 本身可視為：

$$
B_{\mathrm{sandbox}}.
$$

其 capability：

$$
C_{\mathrm{sandbox}}
$$

與 host 隔離。

---

# 84. Sandbox Escape 不在理論抽象中忽略

工程上必須承認：

$$
\text{sandbox}
\neq
\text{absolute safety}.
$$

但第一代可將其作為主要安全邊界。

---

# 85. Safety Envelope

定義：

$$
E_S
=
\langle
I,
C,
R,
T,
B
\rangle.
$$

其中：

- $I$：identity；
- $C$：capability；
- $R$：risk limit；
- $T$：time limit；
- $B$：resource budget。

---

# 86. Transition 必須在 Envelope 內

$$
\Theta
\in
E_S
$$

才允許。

---

# 87. Resource Budget 也是安全

即使是合法運算，

若：

$$
C_{\mathrm{resource}}
$$

無界，

也可能造成 denial-of-service。

所以：

$$
B
$$

是安全的一部分。

---

# 88. Time Budget

同理：

$$
T_{\max}
$$

限制 runaway process。

---

# 89. Memory Budget

$$
M_{\max}
$$

限制 memory explosion。

---

# 90. Search Budget

對 Omphalos / 搜尋：

$$
Q_{\max}
$$

限制過度外部呼叫。

---

# 91. Cost Budget

$$
C_{\mathrm{api}}\le B_{\mathrm{api}}.
$$

避免 fast path 無限制調用付費服務。

---

# 92. Safety Receipt

每個 privileged transition 留：

$$
r_t
=
\langle
I_t,
C_t,
R_t,
G_t,
V_t,
P_t,
\text{result}
\rangle.
$$

---

# 93. Receipt 不需要 Chain-of-Thought

只需要足夠：

- audit；
- replay；
- invalidate；
- compare；
- attribute。

---

# 94. Audit 不等於人工審核每一步

Audit 可以 async。

所以：

$$
\text{fast execution}
+
\text{later audit}
$$

可以共存於低風險 path。

---

# 95. High-Risk Path 需要同步審查

若：

$$
R\ge\theta_{\mathrm{high}},
$$

則：

$$
\text{async audit}
$$

不足。

---

# 96. Human Gate

某些 path 可以要求：

$$
H_{\mathrm{approval}}=1.
$$

但這不是所有 path 的 default。

---

# 97. Multi-Agent Separation

高風險下，

可以分：

- proposer；
- executor；
- verifier；
- approver。

避免：

$$
\boxed{
\text{propose}
\rightarrow
\text{execute}
\rightarrow
\text{verify}
\rightarrow
\text{approve}
}
$$

由同一主體全包。

---

# 98. Separation of Duties

可寫：

$$
I_P
\neq
I_A
$$

於高風險情境。

---

# 99. 低風險不用強制多主體

否則效率太差。

所以 separation 也應 risk-adaptive。

---

# 100. Security Escalation Ladder

第一版：

$$
S_0
=
\text{automatic fast},
$$

$$
S_1
=
\text{automatic + deep verify},
$$

$$
S_2
=
\text{sandbox only},
$$

$$
S_3
=
\text{human approval},
$$

$$
S_4
=
\text{deny}.
$$

---

# 101. Dynamic Security Level

根據：

$$
R,
N,
I,
C
$$

決定：

$$
S_t.
$$

---

# 102. Known Safe Path

若：

$$
N\downarrow,
$$

$$
R\downarrow,
$$

$$
T_K\uparrow,
$$

則可以：

$$
S_t\rightarrow S_0.
$$

---

# 103. Novel Path

若：

$$
N\uparrow,
$$

則：

$$
S_t
$$

升級。

---

# 104. High Privilege Path

若：

$$
|C_{\mathrm{req}}|\uparrow,
$$

也升級。

---

# 105. Security as a Routing Dimension

Adaptive Corridor Generator 不只找最快：

$$
\Gamma.
$$

還要找：

$$
\Gamma
$$

的：

- cost；
- capability；
- risk；
- rollback。

---

# 106. Multi-Objective Secure Routing

$$
\mathbf U
=
(
\text{speed},
\text{cost},
\text{risk},
\text{privilege},
\text{reversibility}
).
$$

---

# 107. Pareto Secure Paths

可以保留：

$$
\text{Pareto set}.
$$

依 task 選。

---

# 108. Security and Crystallization

只有：

$$
\kappa
$$

同時通過：

$$
V_{\mathrm{functional}}
$$

與：

$$
V_{\mathrm{security}}
$$

才能 hot。

---

# 109. Functional Success 不足

即：

$$
\boxed{
\text{works}
\neq
\text{safe to reuse}.
}
$$

---

# 110. Security Regression

新版本 crystal 即使更快，

若：

$$
R_{\mathrm{new}}
>
R_{\mathrm{old}},
$$

可能不 promotion。

---

# 111. Risk Budget

允許：

$$
\Delta R
$$

不超過：

$$
B_R.
$$

---

# 112. Security Break-Even

安全措施也有成本，

但高風險失敗成本：

$$
C_F^{\mathrm{security}}
$$

可能非常大。

所以不能只看平均 runtime。

---

# 113. Expected Loss

可寫：

$$
E_L
=
p_{\mathrm{fail}}
C_{\mathrm{impact}}.
$$

納入 utility。

---

# 114. Rare Catastrophic Risk

即使：

$$
p_{\mathrm{fail}}
$$

很低，

若：

$$
C_{\mathrm{impact}}
$$

極高，

仍不適合 fast path。

---

# 115. 因此風險不是只有失敗率

要看：

$$
\boxed{
\text{Probability}
\times
\text{Impact}.
}
$$

---

# 116. Safe-by-Construction Candidate

某些 transition 可以透過：

- pure function；
- immutable data；
- sandbox；
- type；
- transaction；

降低風險。

---

# 117. Reversible-by-Construction

例如 copy-on-write：

$$
s_t
\rightarrow
\tilde{s}_{t+1}
$$

驗證後才 commit。

---

# 118. Read-Only by Default

外部 provider 第一階段可預設：

$$
\boxed{
\text{read-only}.
}
$$

---

# 119. Write Requires Explicit Capability

$$
\text{write}
\notin
C_t
$$

除非明確授權。

---

# 120. Irreversible Write Requires Stronger Gate

$$
R_4
$$

需更強：

$$
S_t.
$$

---

# 121. Minimal Security Architecture

第一代可寫：

```text
Actor Context
    ↓
Capability Envelope
    ↓
Risk Classifier
    ↓
Transition Guard
    ↓
Fast / Slow Path Selector
    ↓
Execution
    ↓
Validator
    ↓
Receipt
    ↓
Promotion / Invalidation
```

---

# 122. 與 Series 05 的接口

Series 05：

$$
A
\otimes
P
\otimes
E
\otimes
G
\otimes
V.
$$

本篇強調：

$$
P
$$

雖可耦合，

不可消失。

---

# 123. 與 Series 06 的接口

Path Compilation 不能消除：

$$
\text{necessary security checkpoints}.
$$

若中間：

$$
B_{50}
$$

是不可消除 authority boundary，

則：

$$
1\rightarrow100
$$

可能不合法。

---

# 124. Security-Preserving Path Compilation

只有：

$$
\operatorname{SecurityInvariant}
(
\widehat{\ell}
)
=
1
$$

才能取代原 path。

---

# 125. 與 Series 07 的接口

Crystal 必須攜帶：

$$
C_{\mathrm{req}},
$$

$$
R,
$$

$$
X_{\mathrm{security}}.
$$

---

# 126. 與 Series 08 的接口

EHPE 中：

$$
U_H
$$

必須納入：

$$
C_{\mathrm{risk}}
$$

與：

$$
C_{\mathrm{privilege}}.
$$

---

# 127. 與遊戲白皮書的接口

單機遊戲可把：

$$
C_t
$$

固定在低風險集合。

所以非常適合先驗證計算方法，

避免安全問題淹沒核心實驗。

---

# 128. 為什麼先遊戲，再外部？

因為：

$$
\boxed{
\text{Computational Feasibility}
\neq
\text{Deployment Readiness}.
}
$$

先證明：

$$
\text{ELC}
+
\text{Path Compilation}
+
\text{Crystallization}
$$

有效，

再擴安全域。

---

# 129. 不要讓安全系統掩蓋計算實驗

如果第一版直接加入：

- enterprise IAM；
- federation；
- multi-tenant；
- legal compliance；

最後慢了，

不知道是：

$$
\text{UNPNP failure}
$$

還是：

$$
\text{security overhead}.
$$

---

# 130. 分階段驗證

因此：

$$
\boxed{
\text{compute}
\rightarrow
\text{secure coupling}
\rightarrow
\text{external deployment}.
}
$$

---

# 131. Core Proposition I

$$
\boxed{
\textbf{
UNPNP 的安全目標不是讓所有 transition 都變慢，而是限制 fast path 只能存在於明確授權的可達世界。
}
}
$$

---

# 132. Core Proposition II

$$
\boxed{
\textbf{
Reachable、Authorized、Trusted 與 Safe 是四個不同層次，任何一個都不能被另一個自動推出。
}
}
$$

---

# 133. Core Proposition III

$$
\boxed{
\textbf{
AI 可以學會新的計算路徑，但不能由學習結果自行提升權限。
}
}
$$

---

# 134. Core Proposition IV

$$
\boxed{
\textbf{
安全閘門可以被編譯得更快，但不能被編譯掉。
}
}
$$

---

# 135. Core Proposition V

$$
\boxed{
\textbf{
高風險、不可逆與外部作用域在第一代 UNPNP 實驗中應被排除，直到安全模型與驗證成熟。
}
}
$$

---

# 136. 第一版總模型

令：

$$
\Theta
$$

為 candidate transition。

執行條件：

$$
\boxed{
\operatorname{Exec}(\Theta)=1
}
$$

若：

$$
I_t\in I_{\mathrm{allowed}}(\Theta),
$$

$$
C_{\mathrm{req}}(\Theta)
\subseteq
C_t,
$$

$$
R(\Theta)
\le
R_{\max},
$$

$$
G_\Theta(s_t)=1.
$$

執行後：

$$
V_\Theta(s_{t+1})=1.
$$

---

# 137. Safe Reachable World 總式

因此：

$$
\boxed{
\mathcal W_t^{\mathrm{accessible}}
=
\{
B_j
\in
\mathcal W:
\exists
\Gamma_{t\rightarrow j}
\text{ satisfying }
I,C,R,G,V
\}.
}
$$

---

# 138. 結論

UNPNP 的快速通道如果成熟，

真正的形態可能是：

$$
B_1
\xrightarrow{\kappa}
B_{100}.
$$

這是一件很強的事。

也正因如此，

不能把：

$$
\kappa
$$

只理解成：

> 一條更快的路。

它還必須回答：

- 誰可以走？
- 在什麼 task 下走？
- 需要哪些 capability？
- 有什麼 side effect？
- 有多大風險？
- 能否 rollback？
- 驗證失敗怎麼辦？
- 什麼情況下立即失效？

因此真正成熟的 fast path 應是：

$$
\boxed{
\text{Fast}
+
\text{Typed}
+
\text{Authorized}
+
\text{Bounded}
+
\text{Verifiable}
+
\text{Invalidatable}.
}
$$

安全的目標也不是：

> 把所有 path 都塞進繁瑣權限樹。

第一代真正需要的是：

$$
\boxed{
\text{明確的可達域}
+
\text{多道低成本閘門}
+
\text{能力邊界}
+
\text{風險分級}
+
\text{fail-closed}
+
\text{rollback}.
}
$$

只要 transition 位於這個安全 envelope 中，

AI 就可以走得很快。

一旦離開，

它就應：

$$
\text{fast path}
\rightarrow
\text{guarded slow path}
$$

甚至：

$$
\text{deny}.
$$

所以本篇最終可以收束為：

$$
\boxed{
\textbf{
安全不是阻止快速計算，
而是定義快速計算可以在哪個世界裡發生。
}
}
$$

以及：

$$
\boxed{
\textbf{
耦合計算，隔離權限。
}
}
$$

下一篇將收束整個理論系列，把這套機制從抽象計算模型帶回第一個實驗工程問題：

> 如何先在單機遊戲中驗證 Adaptive Corridor、ELC、Path Compilation、Crystallization 與 EHPE，並為未來一般程式的 AI 再編譯留下接口？

---

## 後續篇章

**Series 10｜從遊戲世界到一般程式：AI 自我重組計算圖的研究路線**

下一篇將整理：

$$
\text{Synthetic World}
\rightarrow
\text{Turn-Based Game}
\rightarrow
\text{Simulation Game}
\rightarrow
\text{Real-Time Game}
\rightarrow
\text{Controlled Legacy Program}
$$

並建立：

- baseline；
- frozen-model experiment；
- reasoning ratio；
- corridor hit ratio；
- crystallization ratio；
- average runtime cost；
- replay；
- shadow recompilation；
- safe experimental scope；
- success / failure criteria；
- general-program recompilation future interface。
