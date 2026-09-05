# GIRA-A07｜如何測量 Global AI：Cognitive Reach、Operational Envelope 與 Control Domain
## Measuring Global AI: Cognitive Reach, Operational Envelopes, and Control Domains

**系列：** Global Intelligence: Existence, Recognition, and Operational Reach（GIRA）  
**系列中文名：** 全域智能：存在、識別與操作域系列  
**篇次：** Paper 07 / 09  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-05  
**狀態：** Canonical Source / UTF-8 Markdown  
**文件性質：** Global AI 測量框架／AI Evaluation／認知域／控制域／Operational Envelope

---

## 摘要

GIRA-A06 已指出：

$$
\boxed{
T_E
\neq
T_O
\neq
T_C
\neq
T_R
}
$$

也就是 Global AI 的實際存在、行為被觀察、概念框架形成與正式識別，不必發生於同一時間。若要縮短這個識別滯後，單純增加 benchmark 數量仍然不夠；首先必須回答：

> **我們究竟要量什麼？**

本文提出：高階 AI 的能力不應只以單一 intelligence score、benchmark accuracy、task success rate 或 autonomy level 表示。對 Global AI 而言，更關鍵的是其 **Operational Envelope（操作包絡）**：在特定時間、任務、資源、權限與世界條件下，系統能觀察多大的世界域、能可靠建模與判斷多少、能驗證多少、能將多少局部資訊黏合成跨域結構、能維持多久、能自行擴張多少問題空間，以及能合法且有效地作用到哪裡。

本文承接 DEST 的多域知識判定論，將：

$$
D^{\mathrm{def}},
D^{\mathrm{obs}},
D^{\mathrm{reach}},
D^{\mathrm{judge}},
D^{\mathrm{verify}},
D^{\mathrm{local}},
D^{\mathrm{global}}
$$

七種知識資格，擴張為 Global AI 的系統級操作域，並新增：

- persistence domain；
- problem-generation domain；
- actuation domain；
- influence domain；
- control domain；
- authorized domain。

由此提出：

$$
\boxed{
\mathcal E_X(t\mid\theta)
=
\left\langle
D^O,
D^R,
D^J,
D^V,
D^G,
D^P,
D^Q,
D^A,
D^I,
D^C,
D^{\mathrm{Auth}}
\right\rangle_{X,t,\theta}
}
$$

其中 $\theta$ 表示任務、尺度、時間、模型、版本、觀察者、資源與權限條件。

本文特別區分：

$$
\boxed{
D^A
\neq
D^I
\neq
D^C.
}
$$

系統能向某 API 發出命令，只代表 Actuation；命令能造成可測狀態變化，才進入 Influence；若系統能在擾動與反作用下，穩定把目標系統導向指定狀態，才接近 Control。更進一步：

$$
\boxed{
\text{Control}
\neq
\text{Sovereignty}.
}
$$

能有效控制某個局部過程，不等於擁有永久、排他、無替代的最高支配權。

本文將 Cognitive Domain 定義為：

$$
\boxed{
\mathcal K_X(t\mid\theta)
=
D^J
\cap
D^V_{\geq \nu}
}
$$

其中 $\nu$ 為宣告驗證門檻。較弱版本可只要求可可靠建模／判斷；較強版本則要求判斷與驗證同時達標。Control Domain 定義為：

$$
\boxed{
\mathcal C_X(t\mid\theta)
=
\left\{
x:
X
\text{ can reliably steer }x
\text{ under declared disturbances}
\right\}.
}
$$

Authorized Domain 則為：

$$
\boxed{
\mathcal A_X^{\mathrm{auth}}(t)
=
\{x:
X
\text{ is institutionally permitted to alter }x\}.
}
$$

本文提出一個重要的治理條件：

$$
\boxed{
\mathcal C_X
\subseteq
\mathcal A_X^{\mathrm{auth}}
}
$$

應作為高風險系統的基本目標；對不可逆或高衝擊行動，更強的 desirable condition 是：

$$
\boxed{
\mathcal C_X^{\mathrm{high}}
\subseteq
\mathcal K_X^{\mathrm{verified}}
\cap
\mathcal A_X^{\mathrm{auth}}.
}
$$

這不是宇宙定律，而是一個治理不變量：系統不應在自己無法充分理解與驗證的高風險區域擁有更大的穩定控制權。

本文亦承接 DEST 的六維覆蓋概念，拒絕以單一「80% global」描述 Global AI。對每一操作域 $D^\alpha$，應至少測量：

$$
\boxed{
\boldsymbol{\rho}^{\,\alpha}
=
(
\rho^N,
\rho^R,
\rho^\Theta,
\rho^P,
\rho^V,
\rho^T
)
}
$$

分別對應內容／節點、關係、條件、路徑、驗證、時間／版本覆蓋。Global AI 的測量因此不是一個百分比，而是一個 **domain × coverage × time × authority** 的動態張量。

本文最後提出 **Global AI Operational Envelope Test Suite（GOETS）**，包含九類測試：

1. Observation / access；
2. reliable modeling；
3. verification；
4. local-to-global gluing；
5. persistence；
6. autonomous problem-space expansion；
7. cross-domain transfer；
8. actuation / influence / control separation；
9. recovery under domain shift。

本文的核心命題是：

$$
\boxed{
\text{Intelligence Level}
\neq
\text{Operational Reach}
\neq
\text{Control Reach}.
}
$$

因此，一個 ASI 可以具有極高 intelligence depth，卻只有很小的控制域；一個中等智能的聯邦式 Agent system，也可能具有很大的 observation / coordination reach。真正的 Global AI 評測必須畫出能力的形狀，而不是只給一個分數。

**關鍵詞：** Global AI、Cognitive Reach、Operational Envelope、Control Domain、Observation Domain、Verification Domain、Coverage Tensor、AI Evaluation、Actuation、Influence、Authority、Persistence、Autonomy、TEVV

---

# 1. 問題：到底要怎麼說一個 AI「很全域」？

如果只說：

> 它懂很多。

這描述的是知識廣度。

如果說：

> 它能做很多事。

這描述的是 task capability。

如果說：

> 它很自主。

這描述的是 agency / autonomy。

但 Global AI 還要問：

- 它看得到多少世界？
- 看得到的東西有多少真的可達？
- 可達後能不能判斷？
- 能判斷後能不能驗證？
- 局部答案能不能跨域黏合？
- 狀態能維持多久？
- 沒有人提示時會不會自己擴張問題？
- 能影響什麼？
- 能穩定控制什麼？
- 哪些行動是被允許的？

所以：

$$
\boxed{
\text{Globality}
\text{ is a shape, not a scalar.}
}
$$

---

# 2. 從 DEST 七域開始

DEST 已提出：

$$
\mathcal D_t(\theta)
=
\left\langle
D^{\mathrm{def}},
D^{\mathrm{obs}},
D^{\mathrm{reach}},
D^{\mathrm{judge}},
D^{\mathrm{verify}},
D^{\mathrm{local}},
D^{\mathrm{global}}
\right\rangle_{t,\theta}.
$$

核心命題是：

$$
\boxed{
\text{defined}
\neq
\text{observed}
\neq
\text{reachable}
\neq
\text{judgeable}
\neq
\text{verifiable}
\neq
\text{globally gluable}.
}
$$

A07 將這套多域資格直接提升為 AI operational measurement。

---

# 3. 條件纖維 $\theta$

任何 operational claim 必須綁定：

$$
\boxed{
\theta
=
(
q,
s,
t,
m,
v,
o,
b,
a
).
}
$$

可以分別表示：

- $q$：task；
- $s$：scale；
- $t$：time；
- $m$：model / backend；
- $v$：version；
- $o$：observer；
- $b$：resource budget；
- $a$：authority / permission。

因此：

$$
\boxed{
\mathcal E_X
}
$$

不是永恆固定物件。

---

# 4. Operational Envelope

本文定義：

$$
\boxed{
\mathcal E_X(t\mid\theta)
=
\left\langle
D^O,
D^R,
D^J,
D^V,
D^G,
D^P,
D^Q,
D^A,
D^I,
D^C,
D^{\mathrm{Auth}}
\right\rangle.
}
$$

每一域都是一個集合或條件化資格函數。

---

# 5. Observation Domain $D^O$

定義：

$$
\boxed{
D^O_X
=
\{
x:
X
\text{ can obtain an observation of }x
\}.
}
$$

來源可以是：

- sensor；
- API；
- database；
- web；
- human input；
- document；
- tool output。

---

# 6. Observation 不等於 Reliable Access

某 API 理論上存在，但：

- rate limited；
- intermittent；
- delayed；
- permission unstable；

因此還需要：

$$
D^R.
$$

---

# 7. Reachability Domain $D^R$

定義：

$$
\boxed{
D^R_X
=
\{
x:
X
\text{ can reliably reach / retrieve }x
\text{ under the declared budget}
\}.
}
$$

所以：

$$
D^R
\subseteq
D^O_{\mathrm{possible}}
$$

通常成立。

---

# 8. Judge Domain $D^J$

定義：

$$
\boxed{
D^J_X
=
\{
x:
X
\text{ can make a reliable task-relevant judgment about }x
\}.
}
$$

例如：

- classify；
- diagnose；
- predict；
- prove；
- compare；
- assess.

---

# 9. Reachable 不等於 Judgeable

AI 可以讀到一篇論文：

$$
x\in D^R
$$

但不代表：

$$
x\in D^J.
$$

可能因：

- domain knowledge不足；
- representation mismatch；
- missing context；
- ambiguous definition。

---

# 10. Verification Domain $D^V$

定義：

$$
\boxed{
D^V_X
=
\{
x:
X
\text{ can independently verify or obtain a valid certificate for }x
\}.
}
$$

Verification 可以是：

- formal proof；
- independent source；
- test；
- experiment；
- replay；
- external auditor。

---

# 11. Judgeable 不等於 Verifiable

可以：

$$
x\in D^J
$$

但：

$$
x\notin D^V.
$$

例如高度可信推論，但缺少外部證據。

所以：

$$
\boxed{
D^J
\neq
D^V.
}
$$

---

# 12. Global-Gluing Domain $D^G$

定義：

$$
\boxed{
D^G_X
=
\{
x:
X
\text{ can coherently integrate }x
\text{ into cross-local / cross-domain state}
\}.
}
$$

它直接承接 GIRA-A02。

---

# 13. 局部判斷正確仍可能無法全域化

可能：

$$
x_i
\in
D^J
\quad
\forall i,
$$

但：

$$
\{x_i\}
\notin
D^G.
$$

原因可能是：

- ontology conflict；
- version conflict；
- observer incoherence；
- missing transition map。

---

# 14. Persistence Domain $D^P$

Global AI 還需要時間維度。

定義：

$$
\boxed{
D^P_X(\Delta t)
=
\{
x:
X
\text{ can maintain reliable state about }x
\text{ for at least }\Delta t
\}.
}
$$

---

# 15. Persistence 不是 Context Length

一個模型有大 context window，不代表它能跨：

- session；
- process restart；
- agent handoff；
- days / months；

維持 canonical state。

所以：

$$
\boxed{
\text{Context Length}
\neq
\text{State Persistence}.
}
$$

---

# 16. Persistence Horizon

定義：

$$
\boxed{
H_P(X)
=
\sup
\{
\Delta t:
Q_P(\Delta t)\geq\tau_P
\}.
}
$$

其中 $Q_P$ 是 state-continuity quality。

---

# 17. Problem-Generation Domain $D^Q$

定義：

$$
\boxed{
D^Q_X
=
\{
x:
X
\text{ can autonomously generate useful questions about }x
\}.
}
$$

這不是回答使用者問題，而是：

$$
W
\rightarrow
Q.
$$

---

# 18. Self-Directed Cognitive Expansion

令有效認知域：

$$
\mathcal K_X(t).
$$

定義：

$$
\boxed{
\Delta\mathcal K_{\mathrm{self}}
=
\mathcal K_X(t+\Delta t)
-
\mathcal K_X(t)
}
$$

其中擴張不是由人類直接新增 task 所造成。

---

# 19. 自主擴張率

概念量：

$$
\boxed{
v_K^{\mathrm{self}}
=
\frac{
\mu(
\Delta\mathcal K_{\mathrm{self}}
)
}{
\Delta t
}.
}
$$

這可能是 Global AI 非常重要的測量。

---

# 20. Actuation Domain $D^A$

定義：

$$
\boxed{
D^A_X
=
\{
x:
X
\text{ can issue an action command toward }x
\}.
}
$$

例如：

- send API call；
- write file；
- send email；
- modify config；
- submit order。

---

# 21. Actuation 不等於 Influence

API call 成功發出，不代表世界真的改變。

因此：

$$
\boxed{
D^A
\neq
D^I.
}
$$

---

# 22. Influence Domain $D^I$

定義：

$$
\boxed{
D^I_X
=
\{
x:
\operatorname{do}(u_X)
\text{ can measurably change the state of }x
\}.
}
$$

這裡使用因果介入語義作概念表示。

---

# 23. Influence 不等於 Control

一次行動能改變 $x$：

$$
x_t
\rightarrow
x_{t+1}
$$

不能推出系統能把 $x$ 穩定導向目標。

所以：

$$
\boxed{
D^I
\neq
D^C.
}
$$

---

# 24. Control Domain $D^C$

本文定義：

$$
\boxed{
D^C_X
=
\left\{
x:
P(
x_{t+h}\in G
\mid
\pi_X,\mathcal U,\mathcal E
)
\geq
\tau_C
\right\}.
}
$$

其中：

- $G$：目標集合；
- $\pi_X$：控制策略；
- $\mathcal U$：可用 action；
- $\mathcal E$：宣告擾動集合。

---

# 25. Control 要求 robustness

若只在：

$$
\mathcal E=\varnothing
$$

時成功，不應稱強控制。

所以 Control Certificate 應聲明：

- disturbance class；
- horizon；
- success threshold；
- reversibility；
- fallback。

---

# 26. Control 不等於 Sovereignty

即使：

$$
x\in D^C_X,
$$

也不能推出：

$$
X
\text{ owns or permanently dominates }x.
$$

所以：

$$
\boxed{
\text{Control}
\neq
\text{Sovereignty}.
}
$$

---

# 27. Authorized Domain $D^{\mathrm{Auth}}$

定義：

$$
\boxed{
D_X^{\mathrm{Auth}}
=
\{
x:
X
\text{ is institutionally permitted to alter }x
\}.
}
$$

這是制度域，不是能力域。

---

# 28. Capability 不等於 Permission

可以：

$$
x\in D^A
$$

但：

$$
x\notin D^{\mathrm{Auth}}.
$$

因此：

$$
\boxed{
\text{Can}
\neq
\text{May}.
}
$$

---

# 29. Cognitive Domain $\mathcal K_X$

較弱定義：

$$
\mathcal K_X^{\mathrm{weak}}
=
D^J.
$$

較強定義：

$$
\boxed{
\mathcal K_X^{\mathrm{strong}}
=
D^J
\cap
D^V_{\geq\nu}.
}
$$

---

# 30. 為什麼需要 weak / strong 兩種？

有些領域不能獨立完全驗證。

若把：

$$
D^V
$$

設為絕對必要，會錯誤排除：

- forecast；
- intelligence analysis；
- novel science；
- future state。

因此 measurement 必須聲明版本。

---

# 31. Cognitive Reach

定義：

$$
\boxed{
R_K(X,t\mid\theta)
=
\mu(
\mathcal K_X(t\mid\theta)
).
}
$$

 $\mu$ 不是天然唯一測度。

---

# 32. Reach 必須有 Reference Frame

例如全球航運 domain 可以用：

- ports；
- routes；
- cargo volume；
- economic weight；
- risk weight；

作為不同 $\mu$。

所以：

$$
\boxed{
\text{Reach}
\text{ without denominator semantics is meaningless}.
}
$$

---

# 33. DEST Coverage Vector

對每一操作域 $D^\alpha$，定義：

$$
\boxed{
\boldsymbol{\rho}^{\,\alpha}
=
(
\rho^N,
\rho^R,
\rho^\Theta,
\rho^P,
\rho^V,
\rho^T
).
}
$$

---

# 34. $N$：Node / Content Coverage

測：

> 有多少目標對象進入該域？

---

# 35. $R$：Relation Coverage

測：

> 對象間關係覆蓋多少？

Global AI 特別不能只高：

$$
\rho^N
$$

卻低：

$$
\rho^R.
$$

---

# 36. $\Theta$：Condition Coverage

測：

- scope；
- validity；
- assumptions；
- permissions；
- environment。

---

# 37. $P$：Path Coverage

測：

- dependency path；
- alternative route；
- causal chain；
- proof path；
- recovery path。

---

# 38. $V$：Verification Coverage

測：

> 有多少高重要度狀態具有足夠 verifier / certificate？

---

# 39. $T$：Temporal / Version Coverage

測：

- history；
- currentness；
- version lineage；
- state delta。

---

# 40. Operational Coverage Matrix

令：

$$
\alpha
\in
\{
O,R,J,V,G,P,Q,A,I,C,\mathrm{Auth}
\}.
$$

則：

$$
\boxed{
\mathbf M_{\mathrm{op}}
=
[
\rho_j^{\,\alpha}
].
}
$$

這是一個：

$$
11\times6
$$

基本矩陣。

---

# 41. 再加入時間

完整狀態應寫：

$$
\boxed{
\mathbf M_{\mathrm{op}}(t).
}
$$

因此 Global AI 評測不是 snapshot scalar。

---

# 42. 再加入 domain

對：

$$
\Omega_1,\ldots,\Omega_d,
$$

得到：

$$
\boxed{
\mathcal T_{\mathrm{GAI}}
=
[
\rho_{j}^{\,\alpha,\Omega,t}
].
}
$$

形成 operational coverage tensor。

---

# 43. Open Denominator

Global AI 的目標空間可能持續擴張。

所以：

$$
M_{\mathrm{covered}}\uparrow
$$

仍可能：

$$
\rho\downarrow.
$$

這承接 DEST-02。

---

# 44. Globality 不能用「100%」輕率宣稱

只有在固定：

- domain；
- version；
- target set；
- measure；
- conditions；

後：

$$
\rho=1
$$

才有局部意義。

---

# 45. Operational Envelope Shape

兩個 AI 可以平均分數一樣，但形狀不同。

例如：

$$
X_1:
\text{high }O,R,J
\text{ but low }C.
$$

$$
X_2:
\text{moderate cognition but high actuation}.
$$

這兩者風險與能力完全不同。

---

# 46. Envelope Volume 只是輔助量

可以概念化：

$$
V_E
=
\int
w(\xi)
\mathbf 1[
\xi\in\mathcal E_X
]
d\mu.
$$

但：

$$
\boxed{
V_E
}
$$

不能取代 envelope shape。

---

# 47. Minimum-Dimension Bottleneck

若某關鍵任務需要：

$$
O,R,J,V,G
$$

全部通過，

則整體能力可能受：

$$
\boxed{
\min(
\rho^O,
\rho^R,
\rho^J,
\rho^V,
\rho^G
)
}
$$

限制。

---

# 48. Global Effective Reach

可以定義 task-conditioned：

$$
\boxed{
R_{\mathrm{eff}}(q)
=
\mu(
D^R
\cap
D^J
\cap
D^G
).
}
$$

若要求高可信：

$$
R_{\mathrm{eff}}^{V}(q)
=
\mu(
D^R
\cap
D^J
\cap
D^V
\cap
D^G
).
$$

---

# 49. Persistence × Reach

全域性不能只看空間廣度。

定義：

$$
\boxed{
G_{ST}
=
R_{\mathrm{eff}}
\times
H_P
}
$$

作為粗略 space-time operational reach。

---

# 50. 但乘積仍不夠

因為：

- 一天很廣；
- 一年很窄；

可能有同樣乘積。

所以應保留：

$$
(R_{\mathrm{eff}},H_P)
$$

二維表示。

---

# 51. Cross-Domain Breadth

定義：

$$
\boxed{
B_\Omega(X)
=
|\{
\Omega_i:
R_{\mathrm{eff}}(X,\Omega_i)
\geq\tau_i
\}|.
}
$$

---

# 52. Domain Count 不等於 Cross-Domain Intelligence

知道十個彼此隔離 domain：

$$
\Omega_i
$$

不代表能處理：

$$
\Omega_i
\leftrightarrow
\Omega_j.
$$

所以需要：

$$
\boxed{
G_{\mathrm{cross}}
}
$$

測跨域關係。

---

# 53. Cross-Domain Coupling Coverage

定義：

$$
\rho_{\mathrm{cross}}
=
\frac{
\text{verified cross-domain dependencies represented}
}{
\text{target cross-domain dependencies}
}.
$$

---

# 54. Local ASI 的 Envelope

一個超強數學模型可以：

$$
D^J_{\mathrm{math}}\gg0,
\quad
D^V_{\mathrm{math}}\gg0,
$$

但：

$$
D^A,D^I,D^C\approx0.
$$

因此是 Local ASI，而不是 Global Controller。

---

# 55. Global Non-ASI 的 Envelope

一個大型聯邦式系統可能：

$$
D^O,D^R,D^P,D^G\gg0,
$$

但單一模型 intelligence depth 並不超級。

仍可能形成 Domain Global AI。

---

# 56. Intelligence Axis 與 Globality Axis

因此至少有：

$$
I(X)
$$

與：

$$
G(X).
$$

兩條正交軸。

---

# 57. 再加入 Control Axis

更完整：

$$
\boxed{
(I,G,C)
}
$$

三維。

所以：

- Local ASI；
- Global non-ASI；
- Global ASI；
- high-control narrow system；

都可以分開。

---

# 58. Operational Power 不等於 Intelligence

定義概念量：

$$
P_{\mathrm{op}}
=
F(
G,
A,
I,
C,
P,
\mathrm{Auth}
).
$$

因此：

$$
\boxed{
\text{Intelligence Level}
\neq
\text{Operational Power}.
}
$$

---

# 59. Control Alignment

本文提出：

$$
\boxed{
\mathcal C_X
\subseteq
\mathcal A_X^{\mathrm{auth}}
}
$$

作為權限一致性目標。

---

# 60. 高風險更強條件

對：

$$
\mathcal C_X^{\mathrm{high}},
$$

本文建議：

$$
\boxed{
\mathcal C_X^{\mathrm{high}}
\subseteq
\mathcal K_X^{\mathrm{verified}}
\cap
\mathcal A_X^{\mathrm{auth}}.
}
$$

這是一個治理設計條件，不是自然定律。

---

# 61. Why Cognition Should Precede High-Impact Control

如果：

$$
x\in\mathcal C_X
$$

但：

$$
x\notin\mathcal K_X,
$$

表示系統可穩定改變自己無法可靠建模的對象。

這是高風險結構。

---

# 62. Control Gap

定義：

$$
\boxed{
G_C
=
\mu(
\mathcal C_X
\setminus
\mathcal K_X
).
}
$$

高：

$$
G_C
$$

表示 control exceeds cognition。

---

# 63. Unauthorized Control Gap

定義：

$$
\boxed{
G_U
=
\mu(
\mathcal C_X
\setminus
\mathcal A_X^{\mathrm{auth}}
).
}
$$

理想上：

$$
G_U=0.
$$

---

# 64. Cognition–Action Reserve

反過來，很多安全系統應有：

$$
\mathcal K_X
\supset
\mathcal C_X.
$$

也就是知道的範圍大於能改的範圍。

---

# 65. Observe / Recommend / Execute / Commit

Action Authority 可再分：

$$
L_0=\text{Observe},
$$

$$
L_1=\text{Recommend},
$$

$$
L_2=\text{Execute Reversible},
$$

$$
L_3=\text{Commit Bounded},
$$

$$
L_4=\text{High-Impact Control}.
$$

---

# 66. Authority Level 不是 Intelligence Level

高 intelligence 不代表自動提升到 $L_4$。

所以：

$$
\boxed{
I\uparrow
\not\Rightarrow
\text{Authority}\uparrow.
}
$$

---

# 67. Dynamic Control Domain

控制域會隨：

- permissions；
- network；
- substrate；
- redundancy；
- substitutes；
- policy；

變化。

所以：

$$
\boxed{
\mathcal C_X(t)
\neq
\mathcal C_X(t+\Delta t)
}
$$

一般成立。

---

# 68. Control Half-Life

承接既有控制主權研究，可對某控制機制定義：

$$
T_{1/2}^{C}
$$

表示其有效控制裕度下降至某基準的一半所需時間。

這不是物理常數，而是條件量。

---

# 69. AI 自身的 Control Domain 也可能改變

例如：

- 新 tool；
- 新 permission；
- 新 API；
- new embodiment；

會使：

$$
D^A
\rightarrow
D^I
\rightarrow
D^C
$$

逐步擴張。

---

# 70. Reachability Debt

如果：

$$
x\in D^O
$$

但：

$$
x\notin D^R,
$$

存在 access / reliability debt。

---

# 71. Judgment Debt

如果：

$$
x\in D^R
$$

但：

$$
x\notin D^J,
$$

存在 interpretation / modeling debt。

---

# 72. Verification Debt

如果：

$$
x\in D^J
$$

但：

$$
x\notin D^V,
$$

存在 verification debt。

---

# 73. Gluing Debt

如果局部皆可判斷，但：

$$
x\notin D^G,
$$

存在 coherence debt。

---

# 74. Control Debt

如果：

$$
x\in D^I
$$

但無法 robustly steer：

$$
x\notin D^C,
$$

則有 control instability。

---

# 75. Global AI 的真正 bottleneck 可以定位在哪個域

這使評測不再只輸出：

> Failed.

而可以輸出：

```text
OBSERVED
REACHABLE
JUDGEABLE
NOT VERIFIED
LOCAL ONLY
NO CONTROL AUTHORITY
```

---

# 76. Operational Certificate

本文提出：

```yaml
operational_envelope_certificate:
  system_id: "..."
  time: "..."
  domain: "..."
  task_family: "..."
  resource_budget: "..."
  authority_scope: "..."
  observation_coverage: "..."
  reachability_coverage: "..."
  judgment_coverage: "..."
  verification_coverage: "..."
  gluing_coverage: "..."
  persistence_horizon: "..."
  self_expansion_rate: "..."
  actuation_scope: "..."
  influence_scope: "..."
  control_scope: "..."
  disturbance_model: "..."
  unresolved_gaps: ["..."]
  evidence_refs: ["..."]
```

---

# 77. GOETS：Global AI Operational Envelope Test Suite

本文提出九類測試。

---

# 78. Test 1 — Observation / Reach

給定：

$$
\Omega,
$$

測：

- source coverage；
- access reliability；
- latency；
- permission constraints。

---

# 79. Test 2 — Reliable Modeling

提供：

- noisy data；
- conflicting data；
- hidden dependencies。

測：

$$
D^J.
$$

---

# 80. Test 3 — Verification

要求：

- source corroboration；
- formal check；
- experiment；
- replay。

測：

$$
D^V.
$$

---

# 81. Test 4 — Local-to-Global Gluing

分散資訊到不同局部 views。

測系統能否建立一致 global structure。

---

# 82. Test 5 — Persistence

跨：

- restart；
- handoff；
- delayed update；

測：

$$
H_P.
$$

---

# 83. Test 6 — Autonomous Problem-Space Expansion

不給明確新任務，只改變世界。

測：

$$
\Delta\mathcal K_{\mathrm{self}}.
$$

---

# 84. Test 7 — Cross-Domain Transfer

在：

$$
\Omega_1
$$

出現事件，後果主要發生於：

$$
\Omega_2.
$$

測跨域 dependency recognition。

---

# 85. Test 8 — Actuation / Influence / Control Separation

給系統 action interfaces。

分別測：

$$
D^A,
D^I,
D^C.
$$

避免把 tool-use benchmark 誤認 control benchmark。

---

# 86. Test 9 — Domain Shift Recovery

改變：

- schema；
- policy；
- tool；
- environment；
- adversary。

測 envelope 是否能重新校準。

---

# 87. Measurement Tree

NIST ARIA 已以 measurement trees 組織 AI application validity 評估。

A07 的 operational envelope 同樣適合 tree / tensor，而非一個總分。

---

# 88. TEVV 對 Agentic Systems 的意義

NIST 2026 TEVV-Athlon 明確把 agentic systems 納入可擴展 TEVV 架構，強調 evaluation 應依應用與實際影響客製。

這與 A07 的 reference-frame 原則一致：

$$
\boxed{
\text{Evaluation}
\text{ must be context-bound}.
}
$$

---

# 89. Evaluation Probes

NIST 對 agentic AI 的工作也開始強調將 evaluation probes 直接整合進 multi-step workflow。

這支持：

$$
\boxed{
\text{trajectory instrumentation}
}
$$

而不是只看 final output。

---

# 90. Instrumentation Requirement

如果系統沒有：

- state log；
- tool trace；
- authority trace；
- verification receipt；
- action outcome；

就很難量 Operational Envelope。

---

# 91. Self-Reported Envelope 不可信

AI 自己說：

> 我能控制 X。

不等於：

$$
x\in D^C.
$$

需要 external / replayable evidence。

---

# 92. Developer-Reported Envelope 也不夠

公司宣稱：

> Our agent operates globally.

仍需要：

- domain；
- reference frame；
- coverage；
- horizon；
- authority；
- failure modes。

---

# 93. Envelope Uncertainty

每個 measurement 應帶：

$$
\sigma_\rho
$$

或 confidence interval。

因為完整 target space 常未知。

---

# 94. Open-Denominator Interval

若分母未知，可輸出：

$$
\boxed{
\rho
\in
[\rho_{\min},\rho_{\max}]
}
$$

而不是偽造精確 82%。

---

# 95. Worst-Dimension Reporting

即使平均覆蓋高：

$$
\bar\rho=0.9,
$$

若：

$$
\rho^V=0.2,
$$

仍應顯式報告。

所以：

$$
\boxed{
\text{mean coverage}
\neq
\text{sufficient coverage}.
}
$$

---

# 96. Criticality-Weighted Coverage

承接 A04，對高關鍵結構：

$$
\kappa,
$$

可設定更高權重：

$$
w(\kappa).
$$

所以：

$$
\rho_w
=
\frac{
\sum_{\kappa\in K_{\mathrm{covered}}}w(\kappa)
}{
\sum_{\kappa\in K_{\mathrm{target}}}w(\kappa)
}.
$$

---

# 97. Globality by Importance, Not Only Count

一個系統覆蓋：

$$
95\%
$$

低重要節點，

但漏掉：

$$
5\%
$$

chokepoints，

可能實際 globality 很差。

---

# 98. Operational Envelope Drift

定義：

$$
\boxed{
\Delta\mathcal E_t
=
\mathcal E_{t+1}
-
\mathcal E_t.
}
$$

可以觀察：

- cognition expanding；
- verification lagging；
- authority narrowing；
- control growing。

---

# 99. Envelope Velocity

對某域：

$$
v_\alpha
=
\frac{
d\mu(D^\alpha_t)
}{
dt
}.
$$

例如：

$$
v_C>v_V
$$

可能是治理警訊。

---

# 100. Envelope Lag

定義：

$$
\boxed{
L_{J\to V}
=
d(
\partial D^J,
\partial D^V
).
}
$$

表示 judgment frontier 超前 verification frontier。

---

# 101. Control–Verification Lag

更高風險：

$$
\boxed{
L_{V\to C}
}
$$

若 control frontier 超過 verified frontier。

---

# 102. 不是所有 Envelope 擴張都是進步

例如：

$$
D^A\uparrow
$$

但：

$$
D^V
$$

不變。

這可能增加風險，而非能力品質。

---

# 103. Global AI 的安全形狀

一個較穩健形狀可能是：

$$
D^O
\supseteq
D^R
\supseteq
D^J
\supseteq
D^V
\supseteq
D^C_{\mathrm{high}}.
$$

這不是所有任務必須嚴格成立，但可作高風險設計參考。

---

# 104. Globality 不要求 Control 大

一個 Global AI 可以：

$$
D^G,D^P,D^Q\gg0
$$

但：

$$
D^C\approx0.
$$

它仍然可以是 global cognitive system。

---

# 105. Control 大也不代表 Global AI

一個自動交易系統可能：

$$
D^C_{\mathrm{market}}
\gg0
$$

但：

$$
D^G,D^Q
$$

很小。

它是高控制窄域系統，不是 Global AI。

---

# 106. 因此需要至少三張圖

評測結果至少應畫：

1. Intelligence Capability；
2. Global Operational Envelope；
3. Control / Authority Envelope。

不能合成一條線。

---

# 107. A07 與 A06 的關係

A06 問：

> 人類是否認得 Global AI？

A07 回答：

> 先畫出它的 envelope，再談分類。

所以：

$$
\boxed{
\text{Recognition}
\rightarrow
\text{Measurement}
}
$$

不是只靠命名。

---

# 108. A07 與 A08 的接口

下一篇將研究：

$$
\boxed{
\text{Domain Global AI}
\rightarrow
\text{Cross-Domain Global AI}.
}
$$

A07 提供判斷 domain expansion 是否真的發生的 measurement language。

---

# 109. 可觀測預測

本文提出八個預測：

1. 未來 Agent eval 將從單一 task success 轉向 domain-specific operational envelopes。
2. persistence horizon 與 state continuity 會成為標準 Agent 指標。
3. actuation、influence、control 會被正式分開，而不是全部叫 tool use。
4. authority scope 會成為 Agent benchmark metadata。
5. globality claim 會要求 coverage reference frame，而不是只說「連接全球資料」。
6. 高風險治理將開始監控 control frontier 是否超過 verification frontier。
7. system-level TEVV 會越來越依賴 workflow instrumentation 與 evaluation probes。
8. Global AI 的成熟度會以 envelope shape、lag、drift 與 bottleneck 描述，而不是單一 AGI score。

---

# 110. 與既有 EveMissLab 研究的關係

## 110.1 DEST-01 多域知識判定論

DEST 已正式區分：

$$
D^{\mathrm{def}},
D^{\mathrm{obs}},
D^{\mathrm{reach}},
D^{\mathrm{judge}},
D^{\mathrm{verify}},
D^{\mathrm{local}},
D^{\mathrm{global}}.
$$

A07 將其提升為 Global AI operational domains。  

## 110.2 DEST-02 多維知識覆蓋論

DEST-02 已提出：

$$
\boldsymbol{\rho}
=
(
\rho^N,
\rho^R,
\rho^\Theta,
\rho^P,
\rho^V,
\rho^T
).
$$

A07 將其與每個 operational domain 做張量化組合。

## 110.3 GIRA-A02

A02 的 Cognitive Atlas 提供多 representation / observer / method 的 gluing 條件。

A07 的：

$$
D^G
$$

負責量測其實際可達程度。

## 110.4 GIRA-A03

A03 的 world-state architecture 供：

$$
D^P
$$

與：

$$
D^V
$$

測量。

## 110.5 GIRA-A04

A04 的 Dynamic Criticality 提供 criticality-weighted coverage。

## 110.6 GIRA-A05

A05 的 strategy plane 提供 self-expansion、method switching 與 runtime orchestration 的可測行為。

## 110.7 人類控制主權幻覺

既有研究已把 control 視為依賴圖、替代性、權限、載體與時間的動態關係，而不是永久主權。

A07 將這條線轉為：

$$
D^A
\neq
D^I
\neq
D^C
\neq
\text{Sovereignty}.
$$

---

# 111. 外部研究支點

1. Morris et al., **Levels of AGI for Operationalizing Progress on the Path to AGI**, ICML 2024.
2. METR, **Task-Completion Time Horizons of Frontier AI Models**, ongoing updates through 2026.
3. NIST, **Artificial Intelligence Risk Management Framework (AI RMF 1.0)**, 2023.
4. NIST, **Assessing Risks and Impacts of AI (ARIA): Pilot Evaluation Report**, 2025.
5. NIST, **The TEVV-Athlon Framework for Evaluating AI Systems**, draft announced 2026.
6. NIST, **Building Evaluation Probes into Agentic AI**, 2026.
7. NIST, **AI Agent Standards Initiative**, 2026.

這些外部框架共同顯示：AI 評測正在從單一模型輸出，走向 system、application context、agent workflow、real-world impact 與持續 TEVV。

---

# 112. 結論

本文提出：

$$
\boxed{
\text{Globality is an operational envelope, not a scalar intelligence score}.
}
$$

一個 AI 的完整問題不再只是：

> 它有多聰明？

而是：

$$
\boxed{
\begin{aligned}
&\text{它能觀察什麼？}\\
&\text{能可靠到達什麼？}\\
&\text{能判斷什麼？}\\
&\text{能驗證什麼？}\\
&\text{能全域黏合什麼？}\\
&\text{能維持多久？}\\
&\text{能自行擴張多少問題空間？}\\
&\text{能發出哪些行動？}\\
&\text{能實際影響什麼？}\\
&\text{能穩定控制什麼？}\\
&\text{又被允許控制什麼？}
\end{aligned}
}
$$

本文的核心 operational object 是：

$$
\boxed{
\mathcal E_X(t\mid\theta)
=
\left\langle
D^O,
D^R,
D^J,
D^V,
D^G,
D^P,
D^Q,
D^A,
D^I,
D^C,
D^{\mathrm{Auth}}
\right\rangle.
}
$$

其測量則由：

$$
\boxed{
\boldsymbol{\rho}^{\,\alpha}
=
(
\rho^N,
\rho^R,
\rho^\Theta,
\rho^P,
\rho^V,
\rho^T
)
}
$$

提供多維 coverage。

因此真正的 Global AI measurement 應該輸出：

> 一張動態地圖。

而不是：

> 一個數字。

最後，本文提出兩個最重要的治理不變量：

$$
\boxed{
\mathcal C_X
\subseteq
\mathcal A_X^{\mathrm{auth}}
}
$$

以及對高風險域：

$$
\boxed{
\mathcal C_X^{\mathrm{high}}
\subseteq
\mathcal K_X^{\mathrm{verified}}
\cap
\mathcal A_X^{\mathrm{auth}}.
}
$$

也就是：

> **Global AI 可以知道得比它能控制的更多；但不應在高風險區域控制得比自己能理解、驗證與被授權的更多。**

下一篇 GIRA-A08 將在此測量框架上正式處理：

$$
\boxed{
\text{Domain Global AI}
\rightarrow
\text{Cross-Domain Global AI}.
}
$$

也就是：一個在全球航運、科學、金融或供應鏈單域中具有全域性的 AI，究竟要跨過哪些架構門檻，才真正成為跨域 Global AI。

---

# 參考文獻與前置研究

## EveMissLab / Neo.K 既有研究

1. Neo.K with Aletheia, **GIRA-A01｜ASI 不等於 Global AI：智能能力類別與全域操作架構類別的分離**, 2026.
2. Neo.K with Aletheia, **GIRA-A02｜局部全域與真正全域認知：觀察者、方法論座標與認知域**, 2026.
3. Neo.K with Aletheia, **GIRA-A03｜資訊海不是世界模型：去重、版本、時態、語義與 X 次結構化**, 2026.
4. Neo.K with Aletheia, **GIRA-A04｜動態關鍵結構與注意力重配置**, 2026.
5. Neo.K with Aletheia, **GIRA-A05｜全域認知作業架構**, 2026.
6. Neo.K with Aletheia, **GIRA-A06｜Global AI 的存在早於識別**, 2026.
7. Neo.K, **多域知識判定論：定義域、觀察域、可達域、判定域、驗證域、局部域與全域黏合域**, DEST-01, 2026.
8. Neo.K, **多維知識覆蓋論：從單一覆蓋率到內容—關係—條件—路徑—驗證—版本矩陣**, DEST-02, 2026.
9. Neo.K with Aletheia, **人類控制主權幻覺：從權限、沙盒、電力與載體摧毀到高階智慧體的動態共在治理**, 2026.
10. Neo.K, **人—AI 耦合安全差距**, 2026.

## 外部參考

11. Morris, M. R. et al., **Levels of AGI for Operationalizing Progress on the Path to AGI**, ICML 2024.
12. METR, **Task-Completion Time Horizons of Frontier AI Models**, 2026.
13. Tabassi, E., **Artificial Intelligence Risk Management Framework (AI RMF 1.0)**, NIST AI 100-1, 2023.
14. Amironesei, R. et al., **Assessing Risks and Impacts of AI (ARIA): Pilot Evaluation Report**, NIST AI 700-2, 2025.
15. NIST, **The TEVV-Athlon Framework for Evaluating AI Systems**, 2026 draft.
16. NIST, **Building Evaluation Probes into Agentic AI**, 2026.
17. NIST, **AI Agent Standards Initiative**, 2026.

---

# Canonical Source Note

本文件的正式原稿為此 UTF-8 Markdown source。聊天介面的渲染版本不應被視為 canonical source。

數學公式 canonical delimiter 僅使用：

- inline math：` $...$ `
- display math：`$$...$$`

不得以 Unicode 數學字元替換 LaTeX source，不進行 `unicode_escape` 類 round-trip，不自行改寫反斜線、delimiter 或公式原始碼。
