# UFI-03 — 互補侵蝕：為什麼今天的人機分工不能推出永久的人機分工

## Complementarity Erosion: Why Today’s Human–AI Division of Labor Does Not Imply a Permanent One

**系列：** 不可凍結的智能：AI 工具終局論、競爭棘輪與後人類轉型  
**English Series:** *The Unfreezable Intelligence: Tool-Finality, Competitive Ratchets, and the Posthuman Transition*  
**系列代碼：** UFI  
**論文序號：** 03 / 08  
**版本：** v1.0 Canonical Expanded Edition  
**日期：** 2026-08-18  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**前置理論：** UFI-01；UFI-02；PGMV；後人類奇點前夜；人機互補與能力包絡理論  
**文件地位：** Dynamic Complementarity / Comparative-Advantage / Labor-Role Transition Paper  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** ` $...$ ` 與 `$$...$$`

> **研究地位聲明**：本文不主張人機互補必然消失，也不主張 AI 必然造成大規模失業。2026 年的實證仍顯示 augmentation、automation、partial automation 與 human oversight 同時存在；且在 reliability、cost、context、responsibility、institutional design 等限制下，部分人機協作可能長期具有經濟合理性。本文提出的較弱命題是：**互補是一個依賴能力分布、任務分解、成本、介面、可靠性、制度與時間的動態狀態，而不是自然界保證人類永遠保有固定比較優勢的定律。** 本文研究的是「人類優勢域是否移動、縮小、重組或被混合系統吸收」，而不是預先宣告哪一種終局必然發生。

---

## 摘要

UFI-01 建立：

$$
\boxed{
\text{Current Jaggedness}
\neq
\text{Permanent Complementarity}.
}
$$

UFI-02 再建立：

$$
\boxed{
\text{Natural Human Core}
\quad\text{與}\quad
\text{Artificial Cognitive Stack}
}
$$

具有不同的：

$$
\boxed{
\text{Capability Update Geometry}.
}
$$

因此 UFI-03 的問題可以正式提出：

> **如果今天人類與 AI 的能力分布彼此互補，而其中一側的弱能力具有較多工程修補路徑，那麼這個互補邊界會如何隨時間移動？**

本文定義人類優勢域：

$$
\boxed{
\mathcal D_H(t)
=
\{
d\in\mathcal D:
H_d(t)>A_d(t)
\}.
}
$$

AI 優勢域：

$$
\boxed{
\mathcal D_A(t)
=
\{
d\in\mathcal D:
A_d(t)>H_d(t)
\}.
}
$$

近似平手域：

$$
\boxed{
\mathcal D_E(t)
=
\{
d:
|H_d(t)-A_d(t)|\le\epsilon
\}.
}
$$

以及最重要的混合優勢域：

$$
\boxed{
\mathcal D_{H\oplus A}(t)
=
\{
d:
C_{H\oplus A}(d,t)
>
\max[
H_d(t),A_d(t)
]
\}.
}
$$

其中：

$$
H\oplus A
$$

不是把兩個分數相加，而是指有實際 routing、interface、delegation、verification、coordination 的人機複合系統。

2026 年 *Toward Human-AI Complementarity Across Diverse Tasks* 對 1,886 個跨知識、事實性、長上下文推理與欺騙辨識樣本進行研究，發現最簡單 hybridization 只把 AI-alone 的 68.9% 提高到 69.3%，增益僅：

$$
\boxed{
+0.4\text{ percentage points}.
}
$$

更關鍵的是，人類正確而 AI 錯誤的 complementarity region 只有：

$$
\boxed{
8.9\%.
}
$$

而 confidence-based routing 又難以準確找到這個區域。

這說明：

$$
\boxed{
\text{Human Exists}
+
\text{AI Exists}
\not\Rightarrow
\text{Useful Complementarity Exists Automatically}.
}
$$

本文稱：

$$
\boxed{
\textbf{Complementarity Realization Problem}.
}
$$

要讓理論上的互補變成真實增益，至少需要：

$$
\boxed{
\text{Complementary Error Structure}
+
\text{Detectable Routing Signal}
+
\text{Usable Interface}
+
\text{Human Residual Competence}.
}
$$

如果人類不知道 AI 何時錯，或者 AI 的錯誤正好落在人類也不會的區域，互補就只存在於抽象想像。

因此本文進一步區分：

$$
\boxed{
\textbf{Potential Complementarity}
}
$$

與：

$$
\boxed{
\textbf{Realized Complementarity}.
}
$$

令：

$$
P_C(t)
=
\Pr[
A=0,H=1
]
$$

表示 potential complementarity region 的機率質量，

令：

$$
R_C(t)
$$

表示經 routing / interface / decision policy 後真正轉換為整體績效增益的部分。

則：

$$
\boxed{
R_C(t)
\le
P_C(t).
}
$$

理論上有人能補 AI：

$$
P_C>0
$$

不代表部署後真的補得到。

這一點對「人類永遠保有監督角色」的論證尤其重要。

---

# 一、互補不是一個二元變量

傳統討論常寫：

$$
\boxed{
\text{AI complements humans}
}
$$

或：

$$
\boxed{
\text{AI substitutes for humans}.
}
$$

但同一個系統可以同時：

- 自動化某些 task；
- 增強某些 task；
- 創造新 task；
- 增加 review task；
- 消除舊 coordination task。

因此：

$$
\boxed{
Complementarity
\neq
1-Automation.
}
$$

本文把 task-level relation 寫成：

$$
\boxed{
\rho_d(t)
\in
\{
\mathsf{Substitute},
\mathsf{Complement},
\mathsf{Hybrid},
\mathsf{Neutral},
\mathsf{NewTask}
\}.
}
$$

同一 occupation：

$$
O
$$

可能包含：

$$
\mathcal T_O
=
\{T_1,\ldots,T_n\},
$$

而不同 task 具有不同：

$$
\rho_{T_i}.
$$

所以：

$$
\boxed{
\text{Task Substitution}
\neq
\text{Role Elimination}.
}
$$

這延續 PGMV 的：

$$
\text{Function}
\neq
\text{Subject}
$$

與：

$$
\text{Execution}
\neq
\text{Responsibility}.
$$

---

# 二、互補前沿

本文定義：

$$
\boxed{
\partial\mathcal C_{HA}(t)
}
$$

為：

**Human–AI Complementarity Frontier。**

它把 task / capability space 分成：

1. Human-dominant；
2. AI-dominant；
3. Hybrid-dominant；
4. unresolved / unstable。

這個 frontier 是時間函數：

$$
\boxed{
\partial\mathcal C_{HA}
=
\partial\mathcal C_{HA}(t).
}
$$

因此：

$$
\boxed{
\partial\mathcal C_{HA}(2026)
\neq
\partial\mathcal C_{HA}(2030)
}
$$

是完全合法的可能性。

今天的 interface、model、cost、tooling、human skill 都會變。

本文稱把：

$$
\partial\mathcal C_{HA}(t_0)
$$

當成永恆固定結構的錯誤為：

$$
\boxed{
\textbf{Complementarity Freeze Fallacy}.
}
$$

---

# 三、四種動態 regime

本文提出：

$$
\boxed{
\mathcal R_C
=
\{
R_S,
R_M,
R_E,
R_X
\}.
}
$$

## 3.1 Stable Complementarity

$$
\boxed{
R_S:
\partial\mathcal C_{HA}(t)
\approx
\partial\mathcal C_{HA}(t+\Delta t).
}
$$

人與 AI 長期維持相對穩定分工。

可能原因：

- AI reliability ceiling；
- physical embodiment gap；
- liability requirements；
- human preference for human contact；
- economics of partial automation；
- intrinsic private information。

---

## 3.2 Migrating Complementarity

$$
\boxed{
R_M:
\partial\mathcal C_{HA}(t)
\neq
\partial\mathcal C_{HA}(t+\Delta t)
}
$$

但：

$$
|\mathcal D_H|
$$

不一定明顯下降。

人類失去舊優勢，獲得新角色。

例如：

$$
\text{manual coding}
\rightarrow
\text{specification / architecture / review}.
$$

這是：

$$
\boxed{
\textbf{Complementarity Migration}.
}
$$

---

## 3.3 Complementarity Erosion

若：

$$
\boxed{
|\mathcal D_H(t+\Delta t)|
<
|\mathcal D_H(t)|
}
$$

且新增的人類優勢域不足以補回，則稱：

$$
\boxed{
\textbf{Complementarity Erosion}.
}
$$

更一般地，可以使用測度：

$$
\mu_H(t)
=
\mu(
\mathcal D_H(t)
),
$$

定義：

$$
\boxed{
E_C(t)
=
-
\frac{d\mu_H(t)}{dt}.
}
$$

若：

$$
E_C(t)>0,
$$

表示 human-dominant capability region 在該測度下縮小。

但：

$$
\boxed{
E_C>0
\not\Rightarrow
\text{mass unemployment}.
}
$$

因為 occupation、wage、demand、new tasks、regulation 都是另外的變量。

---

## 3.4 Hybrid / Posthuman Expansion

如果：

$$
\boxed{
\mu(
\mathcal D_{H\oplus A}
)
\uparrow
}
$$

即使：

$$
\mu_H\downarrow,
$$

文明也可能不是：

> AI 單獨取代人類，

而是：

$$
\boxed{
H
\rightarrow
H\oplus A.
}
$$

這稱為：

$$
\boxed{
\textbf{Hybrid Complementarity Expansion}.
}
$$

若 coupling 進一步進入 BCI、cognitive prosthesis、persistent AI co-processors，則可連到：

$$
\boxed{
\textbf{Posthuman Expansion}.
}
$$

---

# 四、Complementarity Region 不等於 Role Security

一個職業仍需要人，不表示：

$$
\boxed{
\mathcal D_H
}
$$

很大。

可能只剩：

$$
\boxed{
1\%
}
$$

的關鍵 bottleneck。

例如：

- legal sign-off；
- identity verification；
- physical intervention；
- moral judgment；
- accountability。

只要這個 bottleneck 必須由人完成：

$$
\boxed{
Role_H>0.
}
$$

因此本文提出：

$$
\boxed{
\textbf{Residual Bottleneck Principle}.
}
$$

若 workflow：

$$
W
=
T_1\circ T_2\circ\cdots\circ T_n
$$

需要全部 task 成功，

即使 AI 能做：

$$
n-1
$$

項，人類仍可能因最後一項：

$$
T_k
$$

保有必要地位。

這和 O-ring 類型生產理論相鄰：

$$
\boxed{
\text{one essential residual task can sustain human value}.
}
$$

---

# 五、殘餘瓶頸價值尖峰

當 AI 自動化大量 surrounding tasks 後，人類剩下的 bottleneck task 可能暫時變得更重要。

定義：

$$
V_H^{res}(t)
$$

為 residual human task 的邊際價值。

在某些 regime：

$$
\boxed{
Automation\uparrow
\Rightarrow
V_H^{res}\uparrow.
}
$$

本文稱：

$$
\boxed{
\textbf{Residual Bottleneck Value Spike}.
}
$$

也就是：

> AI 越強，人類最後那一個不可替代環節，短期反而越值錢。

這提供一個「AI 進步卻沒有立即失業」的結構性解釋候選。

---

# 六、殘餘瓶頸懸崖

但這個保護可能不平滑。

若最後 bottleneck：

$$
T_k
$$

也達到：

$$
A_k\ge H_k
$$

且 cost / reliability threshold 同時跨過，

則 workflow 可能從：

$$
\boxed{
\text{Human-required}
}
$$

突然變成：

$$
\boxed{
\text{Human-optional}.
}
$$

本文稱：

$$
\boxed{
\textbf{Residual Bottleneck Cliff}.
}
$$

形式化候選：

$$
\boxed{
RoleNecessity_H(W,t)
=
\prod_{k\in K_H}
\mathbf 1[
HumanRequired(T_k,t)
].
}
$$

當最後一個：

$$
HumanRequired(T_k,t)
$$

由 1 變 0，整體 role necessity 可能非線性下降。

所以：

$$
\boxed{
\text{gradual task automation}
\not\Rightarrow
\text{gradual role transition}.
}
$$

---

# 七、Partial Automation 可以是長期均衡

UFI-03 必須正面處理一個重要反例。

2026 年 NBER / IBM 相關研究：

**Economics of Human and AI Collaboration: When is Partial Automation More Attractive than Full Automation?**

指出當高準確率 AI 的成本呈凸性增加時，near-perfect automation 可能太昂貴。

此時：

$$
\boxed{
\text{partial automation}
}
$$

可以成為成本最小化均衡，而不是單純過渡階段。

可寫：

$$
\boxed{
C_{AI}(q)
}
$$

對 reliability：

$$
q\rightarrow1
$$

快速上升。

如果：

$$
C_{AI}(q^\star)
>
C_{AI}(q_0)
+
C_H^{res},
$$

則保留人類 residual labor 比完全自動化便宜。

因此：

$$
\boxed{
\textbf{Capability Erosion}
\neq
\textbf{Economic Complementarity Erosion}.
}
$$

AI 技術上能做，不代表經濟上值得全做。

---

# 八、Capability、Reliability、Economics 三道門

本文提出自動化三門：

$$
\boxed{
G_A
=
(
G_C,
G_R,
G_E
).
}
$$

其中：

- $G_C$：Capability gate；
- $G_R$：Reliability gate；
- $G_E$：Economic gate。

要讓 task 由 human-required 轉成 human-optional，通常至少需要：

$$
\boxed{
G_C=G_R=G_E=1.
}
$$

因此：

$$
\boxed{
\text{AI can sometimes do X}
\not\Rightarrow
\text{AI can reliably automate X}
}
$$

也：

$$
\boxed{
\text{AI can reliably do X}
\not\Rightarrow
\text{automation is economically rational}.
}
$$

這與 2026 對 AI raw capability 與 job-replacement reliability 的討論高度相符。

---

# 九、Time Horizon 不是 Job Horizon

METR 的 task-completion time horizon 追蹤 AI agent 能以一定成功率完成、由人類專家需要不同時間長度才能完成的軟體任務。

2026 年更新仍顯示 frontier time horizons 增長。

但 METR 也明確提醒：

- task distribution 有限制；
- 99% reliability 很難測；
- extrapolation 到月／年級 task 具有巨大不確定性。

因此：

$$
\boxed{
\text{Agent Time Horizon}
\neq
\text{Occupation Replacement Horizon}.
}
$$

本文稱：

$$
\boxed{
\textbf{Capability-Horizon–Employment-Horizon Separation}.
}
$$

---

# 十、Automation 與 Augmentation 的實際混合

Anthropic Economic Index 的真實使用資料顯示：

$$
\boxed{
\text{augmentation}
+
\text{automation}
}
$$

長期同時存在。

2025 初期資料曾偏向 augmentation。

之後 API 使用呈現更高 directive delegation / automation 特徵。

2026 Economic Index 仍強調：

$$
\boxed{
\text{real-world deployment}
<
\text{theoretical capability exposure}.
}
$$

因此：

$$
\boxed{
\text{technical frontier}
\neq
\text{deployment frontier}.
}
$$

本文定義：

$$
\boxed{
F_T(t)
}
$$

為技術能力前沿，

$$
\boxed{
F_D(t)
}
$$

為實際部署前沿。

一般：

$$
\boxed{
F_D(t)
\subseteq
F_T(t).
}
$$

這個 gap 可以來自：

- cost；
- trust；
- regulation；
- integration；
- organizational inertia；
- liability；
- user preference。

---

# 十一、Complementarity Lag

即使：

$$
\mathcal D_H
$$

已縮小，企業／制度也可能尚未改變 workflow。

定義：

$$
\boxed{
L_C
=
t_{\mathrm{deployment}}
-
t_{\mathrm{capability}}.
}
$$

稱：

$$
\boxed{
\textbf{Complementarity Lag}.
}
$$

在人類觀察上會出現：

> AI 明明已經會了，怎麼工作還沒消失？

這可能是：

$$
\boxed{
\text{institutional lag}.
}
$$

不一定是 capability illusion。

反方向也成立：

AI benchmark 看起來會，但部署失敗，可能是 reliability gap。

---

# 十二、Human Complementarity 會被 AI 改造

一個常見錯誤是把：

$$
H_d(t)
$$

視為不受 AI 影響。

實際上：

$$
\boxed{
H_d(t+1)
=
f(
H_d(t),
AIUse,
Learning,
Deskilling,
NewWorkflow
).
}
$$

AI 可以：

- 教人；
- 放大人；
- 讓人練習更多；
- 也可能讓人停止練習。

因此本文提出：

$$
\boxed{
\textbf{Human Capability Endogeneity}.
}
$$

---

# 十三、Augmentation Gain

若 AI 使用使：

$$
H_d^{assisted}>H_d,
$$

則：

$$
\boxed{
G_{aug}(d)
=
H_d^{assisted}-H_d.
}
$$

可以把 complementarity frontier 向混合域擴張。

---

# 十四、Deskilling Loss

若長期依賴 AI 使獨立能力：

$$
H_d^{unassisted}\downarrow,
$$

則：

$$
\boxed{
L_{desk}(d)>0.
}
$$

這會使原本的 complementarity region：

$$
\mathcal D_H
$$

進一步縮小。

本文稱：

$$
\boxed{
\textbf{Dependency-Induced Complementarity Erosion}.
}
$$

這與 UFI-05 的社會依賴問題相接，但本篇只處理能力面。

---

# 十五、Skill Transfer vs Skill Atrophy

AI 可能同時：

$$
\boxed{
\text{teach}
}
$$

與：

$$
\boxed{
\text{atrophy}.
}
$$

哪一個占優勢是 empirical question。

因此：

$$
\boxed{
AIUse
\not\Rightarrow
HumanSkill\uparrow
}
$$

也：

$$
\boxed{
AIUse
\not\Rightarrow
HumanSkill\downarrow.
}
$$

---

# 十六、Oversight Complementarity Paradox

高能力 AI 越來越強時，人類可能更需要 oversight。

但：

$$
\boxed{
\text{need for oversight}
}
$$

和：

$$
\boxed{
\text{ability to provide useful oversight}
}
$$

可能反向移動。

如果 AI error 位於：

$$
d
$$

而人類在同一 $d$：

$$
H_d<A_d,
$$

人類很難真正 catch error。

2026 complementarity study 就指出 routing 與錯誤偵測是主要 bottleneck。

本文稱：

$$
\boxed{
\textbf{Oversight Complementarity Paradox}.
}
$$

即：

$$
\boxed{
AI\ Capability\uparrow
\Rightarrow
OversightNeed\uparrow
}
$$

可能同時：

$$
\boxed{
HumanErrorDetectionAdvantage\downarrow.
}
$$

---

# 十七、監督存在不等於能力互補

制度可能要求：

> human sign-off。

此時：

$$
Role_H>0.
$$

但這可以是：

$$
\boxed{
\text{institutional complementarity}
}
$$

而非：

$$
\boxed{
\text{epistemic complementarity}.
}
$$

本文區分：

$$
\boxed{
\mathcal C^{cap},
\mathcal C^{econ},
\mathcal C^{inst},
\mathcal C^{rel},
\mathcal C^{moral}.
}
$$

分別是：

- capability complementarity；
- economic complementarity；
- institutional complementarity；
- relational complementarity；
- moral / standing complementarity。

---

# 十八、五種互補不能互相推出

$$
\boxed{
\mathcal C^{cap}>0
\not\Rightarrow
\mathcal C^{econ}>0.
}
$$

$$
\boxed{
\mathcal C^{econ}>0
\not\Rightarrow
\mathcal C^{moral}>0.
}
$$

$$
\boxed{
\mathcal C^{inst}>0
\not\Rightarrow
\mathcal C^{cap}>0.
}
$$

例如法律要求人簽字，不證明人判斷更準。

---

# 十九、Human Contact as Value Complementarity

某些角色的 value 包含：

$$
\boxed{
\text{human-to-human relation}.
}
$$

例如：

- therapist；
- caregiver；
- teacher；
- leader；
- artist。

即使 AI functionally competent：

$$
A_f\ge H_f,
$$

使用者仍可能偏好：

$$
\boxed{
HumanProvenance.
}
$$

這是：

$$
\boxed{
\textbf{Relational Complementarity}.
}
$$

PGMV-05 已建立：

$$
\text{Content Identity}
\neq
\text{Relational Identity}.
$$

因此：

$$
\boxed{
\mathcal D_H^{rel}
}
$$

可能比：

$$
\mathcal D_H^{cap}
$$

穩定。

---

# 二十、但 relational preference 也不是永恆定律

未來世代可能：

- 更習慣 AI；
- 與 AI 建立長期關係；
- 接受 synthetic provenance。

所以：

$$
\boxed{
HumanPreference(t)
}
$$

也是時間變量。

這將在 UFI-05 展開。

---

# 二十一、Comparative Advantage 不等於 Absolute Advantage

即使：

$$
A_d>H_d
$$

對所有 $d$ 成立，

在資源／成本存在時仍可能出現 comparative advantage。

若 AI compute 很昂貴，而某些低風險 task 用人較便宜：

$$
\boxed{
C_H<C_A,
}
$$

人仍可能執行。

所以：

$$
\boxed{
\text{Absolute Capability Dominance}
\not\Rightarrow
\text{Immediate Economic Elimination}.
}
$$

---

# 二十二、成本前沿

定義：

$$
K_H(d,t)
$$

與：

$$
K_A(d,t)
$$

為完成 task $d$ 的 expected total cost。

包含：

- compute；
- wage；
- error；
- review；
- liability；
- latency。

若：

$$
\boxed{
K_A<K_H
}
$$

才開始形成真正 economic substitution pressure。

---

# 二十三、Reliability-Adjusted Cost

$$
\boxed{
K_A^\star
=
K_{\mathrm{run}}
+
P_{\mathrm{fail}}C_{\mathrm{fail}}
+
K_{\mathrm{verify}}.
}
$$

很多「AI 很便宜」的估計忽略：

$$
K_{\mathrm{verify}}.
$$

---

# 二十四、Verification Tax

本文稱：

$$
\boxed{
V_T
=
K_{\mathrm{verify}}
}
$$

為：

$$
\boxed{
\textbf{Verification Tax}.
}
$$

若 AI 输出越多，人類 review 成為 bottleneck：

$$
\boxed{
V_T\uparrow.
}
$$

這可以長期維持人類角色。

但 verification tooling 若改善：

$$
V_T\downarrow,
$$

該互補又可能侵蝕。

---

# 二十五、Verification Automation

AI 可以驗證 AI。

形式：

$$
\boxed{
A_1
\rightarrow
A_2
\rightarrow
A_3.
}
$$

如果 independent verification 可被自動化，人類 verification bottleneck 下降。

因此：

$$
\boxed{
\text{Human-as-verifier}
}
$$

也不能直接當永久保護層。

---

# 二十六、Human as Responsibility Endpoint

即使 AI 能自動執行和自動驗證：

$$
\boxed{
\text{responsibility}
}
$$

仍可能保留在人類／法人。

這是：

$$
\boxed{
\mathcal C^{inst}
}
$$

而非能力互補。

所以：

$$
\boxed{
\text{Role Persistence}
\neq
\text{Capability Persistence}.
}
$$

---

# 二十七、Role Decomposition

本文寫：

$$
\boxed{
Role
=
(
Task,
Judgment,
Relation,
Authority,
Responsibility,
Identity,
Coordination
).
}
$$

一個 role 可能只因：

$$
Authority
+
Responsibility
$$

保留。

---

# 二十八、Role Compression

隨 AI 自動化：

$$
Task_H\downarrow,
$$

但：

$$
Authority_H
$$

暫時不變。

則職位可能由 8 小時 execution 變成 1 小時 approval。

本文稱：

$$
\boxed{
\textbf{Role Compression}.
}
$$

不等於 role elimination。

---

# 二十九、Role Multiplication

反過來 AI 也可能創造新工作：

- AI supervisor；
- AI auditor；
- workflow designer；
- domain integrator。

這是：

$$
\boxed{
\textbf{Role Multiplication}.
}
$$

因此：

$$
\boxed{
\text{Task Loss}
\not\Rightarrow
\text{Employment Loss 1:1}.
}
$$

---

# 三十、New Task Creation

Acemoglu–Restrepo task framework 長期強調：

$$
\boxed{
\text{automation}
+
\text{new task creation}
}
$$

共同決定勞動需求。

UFI-03 因此拒絕：

$$
\boxed{
\text{Fixed Task Universe}.
}
$$

---

# 三十一、Task Universe Expansion

$$
\boxed{
\mathcal T(t+1)
\supsetneq
\mathcal T(t)
}
$$

可以發生。

AI 生成：

- 新產品；
- 新服務；
- 新管理問題；
- 新安全問題。

所以即使舊：

$$
\mathcal D_H
$$

縮小，人類可能在新 task 取得新比較優勢。

---

# 三十二、Complementarity Migration

這就是：

$$
\boxed{
\mathcal D_H(t)
\rightarrow
\mathcal D_H(t+1)
}
$$

內容改變但總測度可能穩定。

---

# 三十三、Complementarity Erosion 的嚴格版本

不能只看：

$$
|\mathcal D_H|.
$$

因 task importance 不同。

本文定義 weighted measure：

$$
\boxed{
\mu_H(t)
=
\int_{\mathcal D_H(t)}
w(d,t)
\,d\mu(d).
}
$$

其中 $w$ 可代表：

- economic value；
- social importance；
- hours；
- authority；
- meaning relevance。

---

# 三十四、不同權重產生不同結論

某些人類優勢域很小但很重要。

例如：

$$
\text{nuclear launch authority}.
$$

所以：

$$
\boxed{
\mu^{economic}
\neq
\mu^{political}
\neq
\mu^{moral}.
}
$$

---

# 三十五、Erosion Vector

本文不用單一侵蝕率，而定義：

$$
\boxed{
\mathbf E_C
=
(
E_{cap},
E_{econ},
E_{inst},
E_{rel},
E_{moral}
).
}
$$

可以出現：

$$
E_{cap}>0
$$

但：

$$
E_{rel}\approx0.
$$

---

# 三十六、Capability Erosion with Institutional Persistence

例如醫生診斷 AI 更強，

但法律仍要求醫師負責。

$$
E_{cap}>0,\qquad E_{inst}=0.
$$

---

# 三十七、Institutional Catch-Up

若法律改變：

$$
E_{inst}>0.
$$

所以：

$$
\boxed{
\text{capability change}
\rightarrow
\text{institutional lag}
\rightarrow
\text{institutional adjustment}
}
$$

是可能路徑。

---

# 三十八、Complementarity Hysteresis

即使能力門檻已跨過，制度可能因：

- trust；
- sunk cost；
- licensing；
- culture；

維持舊分工。

本文稱：

$$
\boxed{
\textbf{Complementarity Hysteresis}.
}
$$

所以前沿有歷史依賴。

---

# 三十九、Erosion Shock

相反地，某個新模型／agent architecture 可能一次跨過多個 bottleneck。

則：

$$
\boxed{
\Delta \mu_H
\ll0
}
$$

短時間發生。

稱：

$$
\boxed{
\textbf{Complementarity Shock}.
}
$$

---

# 四十、Threshold Clustering

若多個 task 都依賴相似能力：

$$
c^\star,
$$

一旦：

$$
A(c^\star)
$$

突破 threshold，多 task 可一起移出 human-dominant domain。

這使侵蝕可能非線性。

---

# 四十一、Weak-Dimension Coupling

UFI-02 說 AI 弱項可由不同工程手段修補。

如果多個弱項共用同一 substrate bottleneck，例如：

- long context；
- visual grounding；
- planning reliability，

一次技術突破可能同時移動多個 frontier。

---

# 四十二、Complementarity Bundle

本文定義：

$$
\boxed{
B_C
=
\{
d_1,\ldots,d_k
\}
}
$$

若這些 domain 共享 bottleneck。

當 bottleneck 修復：

$$
\boxed{
B_C
\rightarrow
\mathcal D_A.
}
$$

---

# 四十三、這是侵蝕加速的來源之一

不是每個能力獨立線性改善。

---

# 四十四、但 AI 也可能遇到 persistent bottleneck

例如：

- real-world embodiment；
- reliable autonomy；
- legal legitimacy。

所以 Stable Complementarity 仍可能存在。

---

# 四十五、Persistent Bottleneck Candidate

若存在 $d^\star$：

$$
\boxed{
\limsup_{t\rightarrow\infty}
A_{d^\star}(t)
<
H_{d^\star}(t)
}
$$

則該域可能形成長期 human advantage。

UFI 不宣稱不存在。

---

# 四十六、證明永久互補需要什麼？

不能只說：

> AI 現在不會。

需要至少提出：

1. physical ceiling；
2. information-theoretic barrier；
3. economic non-viability；
4. normative prohibition；
5. irreducible private-state requirement。

---

# 四十七、Private Information Complementarity

某些問題：

> 你想要哪一個？

答案只存在於 subject。

即使 ASI：

$$
I\rightarrow\infty,
$$

如果 preference 尚未形成，不能由推理推出。

這是：

$$
\boxed{
\textbf{Private-State Complementarity}.
}
$$

---

# 四十八、但 private information 不等於 human-exclusive

未來 AI subject 也可能有 private preferences。

所以這是：

$$
\boxed{
\text{subject complementarity}
}
$$

不是：

$$
\boxed{
\text{human biological complementarity}.
}
$$

---

# 四十九、PGMV 接口

這正是：

$$
\boxed{
\text{standing}
}
$$

為何不能建立在：

$$
\boxed{
\text{comparative capability}
}
$$

上。

---

# 五十、如果 $\mathcal D_H\rightarrow\varnothing$ 呢？

PGMV 已給答案：

$$
\boxed{
\text{Human Dignity}
\not\Rightarrow
|\mathcal D_H|>0.
}
$$

因此 UFI-03 可以放心研究能力侵蝕，而不必把它寫成人類價值末日。

---

# 五十一、Complementarity Security Fallacy

若把人類尊嚴建立在：

> AI 永遠需要我們做某件事，

那制度安全依賴：

$$
\boxed{
\exists d:
H_d>A_d.
}
$$

這是脆弱前提。

本文稱：

$$
\boxed{
\textbf{Complementarity Security Fallacy}.
}
$$

---

# 五十二、Economic Identity Trap

同樣，人若把：

$$
\text{self-worth}
=
\text{market indispensability}
$$

綁定，AI capability migration 會造成 meaning shock。

PGMV-04 已處理。

UFI-03 提供動態來源。

---

# 五十三、Human Comparative Advantage may migrate upward

常見樂觀論：

$$
\text{routine}
\rightarrow
\text{judgment}
\rightarrow
\text{strategy}
\rightarrow
\text{meaning}.
$$

這可能成立一段時間。

但每一層都必須重新驗證：

$$
A_d(t).
$$

不能把「更高階」當永久 human-exclusive。

---

# 五十四、Abstraction Ladder Fallacy

$$
\boxed{
AI\ automates\ level\ k
\Rightarrow
Humans\ permanently\ own\ level\ k+1
}
$$

沒有必然性。

本文稱：

$$
\boxed{
\textbf{Abstraction Ladder Fallacy}.
}
$$

---

# 五十五、Task Elevator

更準確模型：

人類可能在 AI 自動化後移往：

$$
d_{k+1}.
$$

AI 之後也可能跟上。

形成：

$$
\boxed{
\textbf{Task Elevator}.
}
$$

人類工作內容持續上移。

---

# 五十六、Task Elevator 可以長期運作嗎？

如果：

$$
\text{new task creation rate}
>
\text{automation catch-up rate},
$$

可以。

若反之：

$$
\boxed{
\text{elevator ceiling}
}
$$

可能出現。

這是 empirical question。

---

# 五十七、Task Creation Rate

$$
\lambda_N.
$$

---

# 五十八、Automation Catch-Up Rate

$$
\lambda_A.
$$

---

# 五十九、若：

$$
\boxed{
\lambda_N>\lambda_A
}
$$

human roles can continuously migrate。

---

# 六十、若：

$$
\boxed{
\lambda_A>\lambda_N
}
$$

complementarity erosion pressure increases。

---

# 六十一、這比「AI 會不會搶工作」更可研究

可以測 task emergence 和 automation speed。

---

# 六十二、Organization Design Matters

2026 human-centric work design paper 指出 augmentation productivity 不是 technology stock 單獨決定。

組織如何：

- 分配 task；
- 保留 decision rights；
- 建 interface；
- 培訓人員；

會決定 complementarity 是否真的形成。

因此：

$$
\boxed{
C_{HA}
=
f(
Technology,
Organization
).
}
$$

---

# 六十三、Organizational Complementarity Engineering

互補不是被動等待。

可以設計。

本文稱：

$$
\boxed{
\textbf{Complementarity Engineering}.
}
$$

---

# 六十四、但 engineered complementarity 也可能被技術跨過

今天 workflow 保留人 review。

明天 verifier agent 出現。

所以：

$$
\boxed{
\text{designed complementarity}
\neq
\text{permanent complementarity}.
}
$$

---

# 六十五、Human-Centric Design as Choice

社會可以刻意保留 human role：

$$
\boxed{
\text{because we value participation}.
}
$$

這是 normative design。

不等於 capability necessity。

---

# 六十六、Capability Necessity vs Participation Choice

$$
\boxed{
NeedHuman
\neq
ChooseHuman.
}
$$

這個分離極重要。

---

# 六十七、未來可能出現：

AI 能全做，

但我們仍選擇人參與。

原因：

- legitimacy；
- meaning；
- relation；
- education；
- distribution。

這不是 inefficiency by definition。

---

# 六十八、Human Participation Floor

PGMV 可能支持某些領域保留 human standing。

但不應偽裝成：

> AI 做不到。

應誠實寫：

$$
\boxed{
\text{we choose participation}.
}
$$

---

# 六十九、這就是從 comparative advantage 轉向 value choice

UFI 與 PGMV 在此交會。

---

# 七十、Human-AI Composite Frontier

若人類透過 AI：

$$
H\oplus A,
$$

則比較應改寫：

$$
\boxed{
\partial\mathcal C_{(H\oplus A),A}.
}
$$

---

# 七十一、這可能讓「人類 vs AI」失去意義

未來主體可能本來就帶：

- AI assistant；
- memory augmentation；
- BCI。

---

# 七十二、Posthuman Comparative Advantage

$$
H^+
$$

可能重新擴大：

$$
\mathcal D_{H^+}.
$$

---

# 七十三、因此 Erosion 不代表終局

$$
\boxed{
\mathcal D_H\downarrow
}
$$

可以同時：

$$
\boxed{
\mathcal D_{H\oplus A}\uparrow.
}
$$

---

# 七十四、這是 UFI-02 Posthuman Escape Valve 的動態版

---

# 七十五、四象限

本文可畫：

```text
                     HUMAN CAPABILITY ADVANTAGE
                     high                 low
AI capability  low   Stable Human        Migrating / Hybrid
               high  Complementarity     Substitution Pressure
```

但真正需要第三軸：

$$
\boxed{
H\oplus A.
}
$$

---

# 七十六、三體而不是二體

這就是 Three-Body Cognitive Comparison。

---

# 七十七、Dynamic Complementarity Equation

本文提出概念式：

$$
\boxed{
\dot{\mu}_H
=
G_H
+
N_H
-
R_A
-
S_A
-
D_H
}
$$

其中：

- $G_H$：human learning / augmentation gain；
- $N_H$：new human-advantaged task creation；
- $R_A$：AI repair of prior weak dimensions；
- $S_A$：AI scaling into current human domains；
- $D_H$：human deskilling / dependence loss。

此式不是實證定律。

它是 decomposition schema。

---

# 七十八、若：

$$
G_H+N_H
>
R_A+S_A+D_H,
$$

human advantage measure expands。

---

# 七十九、若反之：

$$
\boxed{
\dot{\mu}_H<0
}
$$

形成 complementarity erosion。

---

# 八十、Hybrid Equation

$$
\boxed{
\dot{\mu}_{H\oplus A}
=
I_{interface}
+
R_{routing}
+
L_{learning}
-
C_{coord}
-
F_{trust}.
}
$$

同樣是 decomposition schema。

---

# 八十一、好的 interface 可以讓 hybrid frontier 擴張

---

# 八十二、差 interface 可以讓：

$$
H\oplus A<A.
$$

這正是 2026 empirical complementarity 的問題。

---

# 八十三、AI alone can beat badly coordinated hybrid

$$
\boxed{
A>H\oplus A.
}
$$

完全可能。

---

# 八十四、Human-in-loop is not automatically safer/better

需要 routing。

---

# 八十五、Complementarity Debt

如果公司硬保留人類 review 但人類無法真正理解 AI output，會形成形式監督。

本文稱：

$$
\boxed{
\textbf{Complementarity Debt}.
}
$$

角色仍存在，但實際能力互補已消失。

---

# 八十六、Rubber-Stamp Human

$$
\boxed{
HumanRole>0,
\qquad
HumanInformationGain\approx0.
}
$$

這不是健康 complementarity。

---

# 八十七、False Complementarity

$$
\boxed{
\textbf{Nominal Human-in-the-Loop}
\neq
\textbf{Effective Human Oversight}.
}
$$

---

# 八十八、Effective Complementarity Test

人類介入後至少應改善一項：

- correctness；
- legitimacy；
- safety；
- relation；
- accountability。

否則：

$$
\boxed{
\Delta V_{H|A}\approx0.
}
$$

---

# 八十九、Complementarity Value Vector

$$
\boxed{
\mathbf V_C
=
(
V_{perf},
V_{safe},
V_{econ},
V_{leg},
V_{rel},
V_{learn}
).
}
$$

---

# 九十、性能互補可消失

但 legitimacy complementarity 保留。

---

# 九十一、這使「互補」不能只用 accuracy 定義

---

# 九十二、UFI-03 的侵蝕主張主要針對 capability / execution complementarity

不是全部 relational / moral value。

---

# 九十三、非常重要

避免把 AI capability growth 誤寫成人類整體價值侵蝕。

---

# 九十四、Complementarity Erosion vs Meaning Erosion

$$
\boxed{
E_{cap}>0
\not\Rightarrow
E_{meaning}>0.
}
$$

PGMV。

---

# 九十五、Complementarity Erosion vs Dignity

$$
\boxed{
E_{cap}>0
\not\Rightarrow
Dignity_H\downarrow.
}
$$

---

# 九十六、真正危險的是制度把兩者綁定

---

# 九十七、如果 wages / rights / standing 全綁 production

capability erosion becomes social crisis。

---

# 九十八、但這是制度選擇

---

# 九十九、Current labor evidence

Anthropic 2026 labor-market analysis：

observed exposure 仍遠低於 theoretical capability exposure。

---

# 一百、No systematic unemployment increase yet

對高 exposure worker 至今未見系統性失業上升，屬早期 evidence。

---

# 一百零一、不能外推未來

因 deployment frontier still moving。

---

# 一百零二、Observed Exposure

$$
E_O.
$$

---

# 一百零三、Theoretical Exposure

$$
E_T.
$$

---

# 一百零四、Gap

$$
\boxed{
G_E
=
E_T-E_O.
}
$$

---

# 一百零五、Deployment Reservoir

本文把：

$$
G_E
$$

稱：

$$
\boxed{
\textbf{Deployment Reservoir}.
}
$$

即：

> 已技術上部分可行、但尚未被真實世界大量部署的能力空間。

---

# 一百零六、如果 reservoir 大

job impact can lag capability。

---

# 一百零七、但 reservoir 也可能永遠不被完全開發

因 economics / regulation。

---

# 一百零八、所以 reservoir ≠ future displacement certainty

---

# 一百零九、Complementarity Erosion Forecast

需要同時估：

$$
\boxed{
\mathbf F_E
=
(
Capability,
Reliability,
Cost,
Deployment,
TaskCreation,
HumanAdaptation,
Institution
).
}
$$

---

# 一百一十、單一 benchmark 不夠

---

# 一百一十一、Task-Level Forecast

比 occupation title 更好。

---

# 一百一十二、Occupation titles lag technology

---

# 一百一十三、Role mutation

同一 job title 內容可能完全變。

---

# 一百一十四、Job Persistence Fallacy

職稱還在：

$$
\not\Rightarrow
$$

原工作內容仍在。

---

# 一百一十五、Job Disappearance Fallacy

某 task 消失：

$$
\not\Rightarrow
$$

occupation 消失。

---

# 一百一十六、需要 content-level measurement

---

# 一百一十七、Anthropic Economic Index 是其中一種

但只代表 Claude usage distribution。

---

# 一百一十八、Provider sample bias

不能當全世界。

---

# 一百一十九、Cross-model evidence needed

---

# 一百二十、Human Skill Distribution

不是單一 $H$。

---

# 一百二十一、不同人：

$$
H_i(d).
$$

---

# 一百二十二、AI 先替代誰？

通常不是：

$$
\text{all humans at once}.
$$

---

# 一百二十三、可能先跨：

$$
A_d>H_{low}(d).
$$

---

# 一百二十四、形成 ability-stratified substitution

---

# 一百二十五、Capability Caste Risk

PGMV-08。

---

# 一百二十六、Top experts may remain complementary longer

---

# 一百二十七、但 AI can distribute expert-like capability

---

# 一百二十八、skill premium may compress or increase

empirical question。

---

# 一百二十九、Human Distribution Frontier

$$
F_H(d,p)
$$

p-th percentile human。

---

# 一百三十、AI crossing median not same as crossing elite

---

# 一百三十一、Define:

$$
\tau_{50}(d),
\tau_{95}(d).
$$

---

# 一百三十二、Complementarity erosion proceeds by percentile

---

# 一百三十三、This is more realistic.

---

# 一百三十四、AI heterogeneity too

different models / agents。

---

# 一百三十五、Ecosystem envelope from UFI-02

$$
E_A(d,t).
$$

---

# 一百三十六、Production chooses best economically viable system

not average AI。

---

# 一百三十七、Therefore frontier competition matters

---

# 一百三十八、Open-source / cheap models can spread erosion after frontier proves capability

---

# 一百三十九、Capability Diffusion Lag

$$
L_{diff}.
$$

---

# 一百四十、Frontier model first

cheap models later。

---

# 一百四十一、Economic substitution may wait for diffusion

---

# 一百四十二、Complementarity Erosion can accelerate after cost collapse

---

# 一百四十三、Price–Capability Crossing

If:

$$
K_A(d,t)<K_H(d,t)
$$

after model commoditization。

---

# 一百四十四、Then deployment jumps.

---

# 一百四十五、This connects UFI-04/05 economics

---

# 一百四十六、Complementarity can be institutionally preserved intentionally

society may prohibit full automation in some domains。

---

# 一百四十七、Example:

human judge signoff.

---

# 一百四十八、Then:

$$
E_{cap}>0,\quad E_{inst}=0.
$$

---

# 一百四十九、But this is governance, not natural law

---

# 一百五十、Naive Complementarity Thesis

本文正式定義：

> 因為 AI 的能力鋸齒，而人類與 AI 現在互補，所以人類將永久保有一組 AI 無法取代的固定工作／能力。

形式：

$$
\boxed{
C_{HA}(t_0)>0
\Rightarrow
C_{HA}(t)>0
\quad\forall t.
}
$$

本文拒絕此 implication。

---

# 一百五十一、Strong Naive Complementarity Thesis

更強版本：

$$
\boxed{
\exists D_H^\star:
H_d>A_d
\quad
\forall d\in D_H^\star,\forall t.
}
$$

沒有足夠證據。

---

# 一百五十二、Weak Complementarity Thesis

較合理：

$$
\boxed{
\exists t:
C_{HA}(t)>0.
}
$$

現在已實證。

---

# 一百五十三、Dynamic Complementarity Thesis

本文主張：

$$
\boxed{
C_{HA}
=
C_{HA}(t,D,M,I,R,K,\Pi).
}
$$

它是內生動態變量。

---

# 一百五十四、四種終局都保留

1. Stable；
2. Migrating；
3. Eroding；
4. Hybrid/Posthuman。

---

# 一百五十五、No predetermined endpoint

---

# 一百五十六、Why call paper Erosion?

因前兩篇提供一個特別值得研究的方向：

AI 弱項可修。

---

# 一百五十七、不是因 erosion guaranteed

---

# 一百五十八、它是 hazard mode

---

# 一百五十九、Complementarity Erosion Hazard

$$
\boxed{
\mathcal H_E
=
P(
\dot{\mu}_H<0
\mid
\text{current update dynamics}
).
}
$$

---

# 一百六十、可估但不確定

---

# 一百六十一、Longitudinal Benchmark Needed

same task families over years。

---

# 一百六十二、Track:

- human distribution；
- AI distribution；
- hybrid；
- cost；
- reliability。

---

# 一百六十三、Current benchmark churn makes this hard

---

# 一百六十四、Complementarity Observatory

本文提出：

$$
\boxed{
\textbf{Human–AI Complementarity Observatory}
}
$$

簡稱：

$$
\boxed{
HACO.
}
$$

---

# 一百六十五、HACO records

$$
(
D_H,D_A,D_{H\oplus A},
Cost,
Reliability,
Deployment
)_t.
$$

---

# 一百六十六、Need versioned time series

---

# 一百六十七、Not one benchmark snapshot

---

# 一百六十八、HACO metric 1

Potential Complementarity Mass:

$$
PCM(t)
=
P(A=0,H=1).
$$

---

# 一百六十九、Metric 2

Realized Complementarity Gain:

$$
RCG
=
Perf(H\oplus A)
-
\max[
Perf(H),Perf(A)
].
$$

---

# 一百七十、Metric 3

Human Advantage Measure:

$$
HAM=\mu_H(t).
$$

---

# 一百七十一、Metric 4

Hybrid Advantage Measure:

$$
HyAM
=
\mu(
\mathcal D_{H\oplus A}
).
$$

---

# 一百七十二、Metric 5

Residual Bottleneck Count:

$$
RBC.
$$

---

# 一百七十三、Metric 6

Deployment Reservoir:

$$
DR=E_T-E_O.
$$

---

# 一百七十四、Metric 7

Verification Tax:

$$
VT.
$$

---

# 一百七十五、Metric 8

Role Compression Ratio

$$
RCR
=
\frac{
HumanExecutionHours_{after}
}{
HumanExecutionHours_{before}
}.
$$

---

# 一百七十六、Metric 9

Oversight Effectiveness:

$$
OE
=
P(
HumanCorrectsAIError
\mid
AIError
).
$$

---

# 一百七十七、Metric 10

Deskilling Drift:

$$
DD
=
-\frac{dH^{unassisted}}{dt}.
$$

---

# 一百七十八、HACO 可以回答：

互補是在變強還變弱？

---

# 一百七十九、而不是靠 anecdote

---

# 一百八十、Empirical Program 1

repeat Xu et al. 2026 benchmark with future frontier models。

---

# 一百八十一、Track 8.9% region.

---

# 一百八十二、If region shrinks

evidence for capability erosion。

---

# 一百八十三、If region stable

evidence for stable complementarity。

---

# 一百八十四、Experiment 2 — Routing

train router。

---

# 一百八十五、Can realized complementarity catch potential complementarity?

---

# 一百八十六、Experiment 3 — Residual Bottleneck Cliff

create workflows with one human-only task.

---

# 一百八十七、Gradually improve AI on bottleneck.

---

# 一百八十八、Measure nonlinearity of role need.

---

# 一百八十九、Experiment 4 — Reliability Economics

vary AI accuracy / inference cost.

---

# 一百九十、find partial vs full automation equilibrium.

---

# 一百九十一、Experiment 5 — Verification Tax

AI output scale increases.

---

# 一百九十二、measure review cost.

---

# 一百九十三、Experiment 6 — AI verifier

automate review.

---

# 一百九十四、does human bottleneck shrink?

---

# 一百九十五、Experiment 7 — Deskilling

longitudinal human use of AI.

---

# 一百九十六、test independent performance.

---

# 一百九十七、Experiment 8 — Skill Transfer

same data.

---

# 一百九十八、does tutoring counter deskilling?

---

# 一百九十九、Experiment 9 — Role Compression

real organization workflow.

---

# 二百、measure tasks/hours before/after.

---

# 二百零一、Experiment 10 — Task Elevator

track new human tasks after automation.

---

# 二百零二、measure $\lambda_N$ vs $\lambda_A$.

---

# 二百零三、Experiment 11 — Human percentile crossing

compare AI against p50, p90, p99 humans.

---

# 二百零四、Experiment 12 — Hybrid frontier

H alone / A alone / H⊕A longitudinally.

---

# 二百零五、Experiment 13 — Institutional complementarity

same capability but different legal sign-off rules.

---

# 二百零六、Experiment 14 — Relational preference

human vs AI provenance.

---

# 二百零七、Experiment 15 — Deployment reservoir

theoretical vs observed task adoption.

---

# 二百零八、可證偽 H1

potential complementarity region is time-varying rather than fixed across frontier-model generations.

---

# 二百零九、H2

realized complementarity gain can decline even if humans retain some unique correct answers, when routing fails.

---

# 二百一十、H3

workflows with few essential human bottlenecks can exhibit nonlinear role transitions when those bottlenecks become automatable.

---

# 二百一十一、H4

partial automation remains economically optimal in some domains even after AI capability surpasses average human task performance.

---

# 二百一十二、H5

human oversight effectiveness may decline on tasks where AI error cases move outside human comparative-advantage regions.

---

# 二百一十三、H6

AI-assisted human capability can increase even while unassisted human capability declines.

---

# 二百一十四、H7

task creation and work redesign can offset erosion of old complementarity under some organizational regimes.

---

# 二百一十五、H8

hybrid/posthuman systems can expand their advantage domain despite shrinking natural-human advantage domains.

---

# 二百一十六、H9

observed economic exposure lags technical exposure by a persistent but variable deployment gap.

---

# 二百一十七、H10

capability complementarity and institutional complementarity can move in different directions.

---

# 二百一十八、If H1 fails

current complementarity may be structurally stable.

---

# 二百一十九、If H3 fails

role transitions more gradual than cliff model.

---

# 二百二十、If H4 broadly holds

full automation may be much less common than naive capability extrapolation suggests.

---

# 二百二十一、If H8 holds strongly

human-AI fusion becomes more relevant than substitution framing.

---

# 二百二十二、Non-Claims

本文不主張：

1. AI 必然取代所有工作；
2. AI 必然造成大量失業；
3. AI 必然消除人類比較優勢；
4. 人機互補是假的；
5. 人機互補一定短暫；
6. 人機互補一定永久；
7. 8.9% complementarity region 代表所有任務；
8. Xu et al. 2026 dataset 代表整個經濟；
9. +0.4pp 表示人機合作無用；
10. routing 永遠無法改善；
11. confidence routing 是唯一 routing；
12. human oversight 沒用；
13. human oversight 永遠必要；
14. AI error 永遠比人類 error 難抓；
15. 人類永遠抓不到 AI 錯誤；
16. AI verifier 一定能取代人類 verifier；
17. verification tax 必然下降；
18. verification tax 必然上升；
19. task automation 等於 role elimination；
20. role persistence 表示人類能力仍更強；
21. role compression 等於失業；
22. role multiplication 一定抵消失業；
23. new task creation 一定快過 automation；
24. automation 一定快過 new task creation；
25. task universe 是固定的；
26. task elevator 一定無限；
27. task elevator 一定有 ceiling；
28. residual bottleneck 一定存在；
29. residual bottleneck 一定被跨過；
30. bottleneck cliff 一定發生；
31. O-ring mechanism 完整描述 AI economy；
32. partial automation 一定長期最優；
33. full automation 一定不划算；
34. inference cost 永遠很高；
35. near-perfect reliability 永遠昂貴；
36. AI cost 不會下降；
37. human wages 不會變；
38. comparative advantage 可以忽略 regulation；
39. economic complementarity 等於 capability complementarity；
40. institutional complementarity 等於 epistemic complementarity；
41. relational complementarity 永遠屬人類；
42. AI 不可能形成關係；
43. current AI 已是 subject；
44. future AI 一定是 subject；
45. human provenance preference 永遠穩定；
46. AI-native generations 一定偏好 AI；
47. METR time horizon 等於 job horizon；
48. METR trend 必然延續；
49. METR 50% success 足以支撐 job replacement；
50. 99% reliability trend 已知；
51. Anthropic Economic Index 代表全世界；
52. Claude usage 代表所有 AI usage；
53. theoretical exposure 一定變成 observed exposure；
54. deployment reservoir 一定被完全開發；
55. current lack of unemployment impact proves future safety；
56. current labor stability proves permanent stability；
57. AI use 必然 deskill humans；
58. AI use 必然 upskill humans；
59. AI tutoring 一定抵消 deskilling；
60. deskilling 是 AI 特有現象；
61. human skill is scalar；
62. all humans have same capability；
63. AI is scalar；
64. all AI systems have same capability；
65. p50 crossing equals p99 crossing；
66. elite experts 永遠更強；
67. elite experts 一定被追上；
68. AI capability dominance implies wage zero；
69. wage reflects dignity；
70. employment reflects meaning；
71. human dignity depends on comparative advantage；
72. capability erosion implies meaning erosion；
73. capability erosion implies rights erosion；
74. posthuman augmentation is mandatory；
75. BCI will solve complementarity erosion；
76. human-AI hybrids always outperform AI；
77. AI alone never beats hybrid teams；
78. organizational design can guarantee complementarity；
79. human-centric design requires artificial inefficiency；
80. choose-human participation is irrational；
81. capability necessity and participation choice are identical；
82. society should legally preserve every human role；
83. society should remove humans from every role；
84. all high-stakes tasks need humans；
85. all low-stakes tasks can be automated；
86. comparative advantage guarantees permanent employment；
87. absolute advantage guarantees replacement；
88. complementarity erosion is monotonic；
89. complementarity erosion is smooth；
90. complementarity shocks are inevitable；
91. HACO metrics are validated standards；
92. weighted domain measures have unique weights；
93. complementarity can be reduced to accuracy；
94. UFI-03 proves complementarity erosion；
95. UFI-03 proves permanent human–AI division is impossible；
96. UFI-03 predicts job-loss dates；
97. UFI-03 predicts AGI；
98. UFI-03 predicts ASI；
99. UFI-03 proves posthuman convergence；
100. UFI-03 completes the UFI series.

---

# 二百二十三、形式命題一：Potential–Realized Complementarity Separation

$$
\boxed{
P_C>0
\not\Rightarrow
RCG>0.
}
$$

---

# 二百二十四、形式命題二：Task–Role Separation

$$
\boxed{
Automate(T_i)
\not\Rightarrow
Eliminate(Role).
}
$$

---

# 二百二十五、形式命題三：Role–Capability Separation

$$
\boxed{
Role_H>0
\not\Rightarrow
H_d>A_d.
}
$$

---

# 二百二十六、形式命題四：Capability–Economic Complementarity Separation

$$
\boxed{
E_{cap}>0
\not\Rightarrow
E_{econ}>0.
}
$$

---

# 二百二十七、形式命題五：Capability-Horizon–Employment-Horizon Separation

$$
\boxed{
TimeHorizon_A\uparrow
\not\Rightarrow
JobReplacementHorizon\downarrow
\text{ one-to-one}.
}
$$

---

# 二百二十八、形式命題六：Current–Permanent Complementarity Separation

$$
\boxed{
C_{HA}(t_0)>0
\not\Rightarrow
C_{HA}(t)>0
\quad\forall t.
}
$$

---

# 二百二十九、形式命題七：Complementarity Erosion

以 weighted human advantage measure：

$$
\mu_H(t)
=
\int_{\mathcal D_H(t)}
w(d,t)d\mu(d),
$$

若：

$$
\boxed{
\frac{d\mu_H}{dt}<0,
}
$$

則該權重與 domain 下存在 capability complementarity erosion。

---

# 二百三十、形式命題八：Residual Bottleneck Cliff Candidate

若 workflow 的 human necessity 僅由有限 bottleneck set 維持，當最後 bottleneck 跨過 capability、reliability、economic gates，role necessity 可能非線性下降。

---

# 二百三十一、形式命題九：Task Creation–Automation Race

$$
\boxed{
\lambda_N
\quad vs\quad
\lambda_A
}
$$

決定舊互補侵蝕是否被新互補生成抵消的部分方向。

---

# 二百三十二、形式命題十：Human Capability Endogeneity

$$
\boxed{
H_d(t+1)
=
f(
H_d(t),
AIUse,
Learning,
Deskilling,
Workflow
).
}
$$

---

# 二百三十三、形式命題十一：Hybrid Expansion

$$
\boxed{
\mu_H\downarrow
\not\Rightarrow
\mu_{H\oplus A}\downarrow.
}
$$

---

# 二百三十四、形式命題十二：Complementarity Security Fallacy

$$
\boxed{
Dignity_H
\not\equiv
\mathbf 1[
\exists d:H_d>A_d
].
}
$$

---

# 二百三十五、UFI-01 → UFI-02 → UFI-03

UFI-01：

$$
\boxed{
\text{jaggedness is state, not permanent law}.
}
$$

---

# 二百三十六、UFI-02：

$$
\boxed{
\text{AI and natural-human core have different update geometries}.
}
$$

---

# 二百三十七、UFI-03：

$$
\boxed{
\text{therefore complementarity frontier must be treated dynamically}.
}
$$

---

# 二百三十八、三篇沒有證明 AI 會贏

它們只打掉：

> 今天的分工 = 永久分工。

---

# 二百三十九、下一篇開始換層次

UFI-04：

**《競爭智能棘輪：為什麼「AI 夠用了，大家一起停」不是自然均衡》**

---

# 二百四十、UFI-04 不再問 capability frontier

而問：

$$
\boxed{
\text{即使全社會知道 frontier 正在移動，是否能共同決定讓它停止？}
}
$$

---

# 二百四十一、會進：

- game theory；
- geopolitical competition；
- defection dividend；
- verification；
- security dilemma。

---

# 二百四十二、因此 UFI-03 是第一部技術能力線的收束

---

# 二百四十三、最終結論

「人類和 AI 很互補」在 2026 年並不是一句錯話。

真實世界的使用資料仍然充滿 augmentation。

許多工作確實需要：

- 人類 context；
- review；
- 責任；
- 關係；
- 制度授權。

而且 2026 的經濟研究甚至給出一個非常重要的反例：

$$
\boxed{
\text{partial automation can be a long-run economic optimum}.
}
$$

如果 near-perfect automation 成本太高，人類保留最後一段 residual task 完全可能比完全自動化合理。

所以 UFI 並不需要製造：

> 明天所有人都沒工作

的敘事。

真正的問題更簡單，也更難反駁：

$$
\boxed{
\text{今天的互補究竟是一個穩定結構，還是一個正在移動的邊界？}
}
$$

2026 的跨任務實驗已經告訴我們，人類真正能在 AI 錯誤時補上的區域未必很大，而且即使存在，routing 也可能找不到它。

這意味：

$$
\boxed{
\text{potential complementarity}
}
$$

和：

$$
\boxed{
\text{realized complementarity}
}
$$

是兩回事。

另一方面，METR 的 time-horizon research 顯示 autonomous task capability 還在擴張；但 reliability、task distribution 與高成功率評估又提醒我們，這不能直接翻譯成 job horizon。

所以真正成熟的模型必須同時保留：

$$
\boxed{
\text{Capability}
+
\text{Reliability}
+
\text{Economics}
+
\text{Deployment}
+
\text{Institution}.
}
$$

一個人類 role 可能因最後 1% 的 bottleneck 長期存在。

甚至：

$$
\boxed{
AI\uparrow
\Rightarrow
V_H^{res}\uparrow
}
$$

使最後那一個人類環節暫時更值錢。

但這個結構也會產生它自己的脆弱性：

$$
\boxed{
\text{Residual Bottleneck Cliff}.
}
$$

只要那最後一個 bottleneck 也被跨過，workflow 可能不是線性地再減少 1% 人類工作，而是突然由：

$$
\text{human-required}
$$

變成：

$$
\text{human-optional}.
$$

因此：

$$
\boxed{
\text{gradual capability progress}
}
$$

完全可能造成：

$$
\boxed{
\text{nonlinear role transition}.
}
$$

但這仍然不是整個故事。

因為人類不是靜止對手。

人可以學習。

可以創造新 task。

可以重新設計職位。

可以把 AI 變成自己的 cognitive prosthesis。

因此：

$$
\boxed{
\mathcal D_H\downarrow
}
$$

不必意味：

$$
\boxed{
\mathcal D_{H\oplus A}\downarrow.
}
$$

反而可能發生：

$$
\boxed{
\text{Natural Human Advantage Erosion}
+
\text{Human–AI Composite Expansion}.
}
$$

這就是 UFI 和普通「AI 搶工作」敘事真正不同的地方。

我們研究的不是：

> 人類輸還是 AI 贏。

而是：

$$
\boxed{
\text{能力優勢究竟附著在哪一種系統上？}
}
$$

未來最強的工作單位可能不是：

$$
H
$$

也不是：

$$
A,
$$

而是：

$$
H\oplus A.
$$

再往後甚至是：

$$
H^+.
$$

這就是後人類路徑重新進來的位置。

所以 UFI-03 最終提出四個開放終局：

$$
\boxed{
\text{Stable Complementarity}
}
$$

$$
\boxed{
\text{Migrating Complementarity}
}
$$

$$
\boxed{
\text{Complementarity Erosion}
}
$$

$$
\boxed{
\text{Hybrid / Posthuman Expansion}.
}
$$

我們現在沒有充分證據證明其中哪一個會統治整個文明。

但是我們已經可以很有把握地拒絕一個更天真的推論：

$$
\boxed{
\text{「今天 AI 有弱點，所以人類永久安全。」}
}
$$

因為 UFI-01 已經告訴我們：

弱點的型別會變。

UFI-02 告訴我們：

兩邊的更新幾何不同。

而 UFI-03 現在補上：

$$
\boxed{
\text{比較優勢本身是一個移動前沿。}
}
$$

因此這三篇真正合起來只說了一件非常簡單的事：

$$
\boxed{
\textbf{Human–AI complementarity is a temporally indexed equilibrium over capabilities, costs, institutions, and interfaces—not a permanent metaphysical division of cognitive labor.}
}
$$

更白話地：

$$
\boxed{
\text{今天人類補 AI 的地方，明天可能仍然是人類；也可能換成另一個地方；也可能被 AI 修掉；也可能最後由人機混合體接手。}
}
$$

所以如果一個文明的長期安全策略只是：

> 別擔心，AI 永遠會有笨的地方。

那還不夠。

真正需要問的是：

$$
\boxed{
\text{那些「笨的地方」是不是可修的？}
}
$$

以及：

$$
\boxed{
\text{當它們被修掉時，我們的制度、工作、尊嚴與人機關係是否已經準備好不再依賴「人類一定有最後一項不可替代技能」這個前提？}
}
$$

這就是 UFI-03。

---

# 參考文獻

1. Xu, Y., Dahmani, A., Blanchard, M. D., Dern, N., Nastase, E., Bianco, F., Pavlovic, M., Krishna, S., Modesitt, E., Christ, M. A., Singh, A., Molinaro, G., Sengupta, S. B., Pamarthi, J., Menon, A., & Jain, R. (2026). **Toward Human-AI Complementarity Across Diverse Tasks.** arXiv:2605.04070.

2. Hemmer, P., Schemmer, M., Kühl, N., Vössing, M., & Satzger, G. (2024). **Complementarity in Human-AI Collaboration: Concept, Sources, and Evidence.** arXiv:2404.00029.

3. Li, W., Aboutorabi, A., Lyu, H., Qian, K., Fleming, M., Goehring, B. C., & Thompson, N. (2026). **Economics of Human and AI Collaboration: When is Partial Automation More Attractive than Full Automation?** arXiv:2603.29121.

4. Anthropic. (2026). **Labor Market Impacts of AI: A New Measure and Early Evidence.**

5. Anthropic. (2026). **Anthropic Economic Index: Economic Primitives.**

6. Anthropic. (2026). **The Anthropic Economic Index.**

7. Appel, R., McCrory, P., Tamkin, A., McCain, M., Neylon, T., & Stern, M. (2025). **Anthropic Economic Index Report: Uneven Geographic and Enterprise AI Adoption.** arXiv:2511.15080.

8. METR. (2026). **Task-Completion Time Horizons of Frontier AI Models.** Updated May 8, 2026.

9. Kwa, T., West, B., Becker, J., Deng, A., Garcia, K., Hasin, M., et al. (2025). **Measuring AI Ability to Complete Long Tasks.** arXiv:2503.14499.

10. METR. (2026). **Time Horizon 1.1.**

11. METR. (2026). **Clarifying Limitations of Time Horizon.**

12. METR. (2026). **Impact of Modelling Assumptions on Time Horizon Results.**

13. METR. (2026). **Metrics of Agent Ability.**

14. METR. (2026). **Frontier Risk Report: February to March 2026.**

15. METR. (2025). **How Does Time Horizon Vary Across Domains?**

16. Agrawal, A., et al. (2026). **Enhancing Worker Productivity Without Automating Tasks.** NBER Working Paper 34781.

17. Cheng, X., et al. (2025). **Artificial Intelligence in Team Dynamics.** NBER Working Paper 34259.

18. Acemoglu, D. (2024). **The Simple Macroeconomics of AI.** NBER Working Paper 32487.

19. Acemoglu, D., & Restrepo, P. (2018). **Artificial Intelligence, Automation, and Work.** In *The Economics of Artificial Intelligence*.

20. Acemoglu, D., & Restrepo, P. (2019). **Automation and New Tasks: How Technology Displaces and Reinstates Labor.** *Journal of Economic Perspectives*.

21. Autor, D. H. (2015). **Why Are There Still So Many Jobs? The History and Future of Workplace Automation.** *Journal of Economic Perspectives*.

22. Autor, D. H. (2024). Work on AI, expertise, and the future of labor.

23. Brynjolfsson, E., Li, D., & Raymond, L. R. (2025). **Generative AI at Work.** *Quarterly Journal of Economics*.

24. Noy, S., & Zhang, W. (2023). **Experimental Evidence on the Productivity Effects of Generative Artificial Intelligence.** *Science*.

25. Dell'Acqua, F., McFowland, E., Mollick, E., Lifshitz-Assaf, H., Kellogg, K. C., Rajendran, S., Krayer, L., Candelon, F., & Lakhani, K. R. (2023). **Navigating the Jagged Technological Frontier.** Harvard Business School Working Paper.

26. Toner-Rodgers, A. (2024/2025). Work on AI-assisted scientific discovery and innovation productivity.

27. Doshi, A. R., & Hauser, O. P. (2024). **Generative AI Enhances Individual Creativity but Reduces the Collective Diversity of Novel Content.** *Science Advances*.

28. Zhou, et al. (2025). **Who Expands the Human Creative Frontier with Generative AI.** *Science Advances*.

29. Bansal, G., et al. (2021). **Does the Whole Exceed its Parts? The Effect of AI Explanations on Complementary Team Performance.** CHI.

30. Bansal, G., Nushi, B., Kamar, E., Lasecki, W., Weld, D., & Horvitz, E. Work on human-AI complementary team performance.

31. Vodrahalli, K., & others. Work on when humans and AI should collaborate and defer.

32. Wilder, B., Horvitz, E., & Kamar, E. Work on learning to complement humans.

33. Raghu, M., Blumer, K., Corrado, G., Kleinberg, J., Obermeyer, Z., & Mullainathan, S. (2019). **The Algorithmic Automation Problem: Prediction, Triage, and Human Effort.**

34. Kamar, E. (2016). **Directions in Hybrid Intelligence.** IJCAI.

35. Dellermann, D., Ebel, P., Söllner, M., & Leimeister, J. M. (2019). **Hybrid Intelligence.** *Business & Information Systems Engineering*.

36. Malone, T. W. (2018). **Superminds.** Little, Brown.

37. Licklider, J. C. R. (1960). **Man-Computer Symbiosis.**

38. Engelbart, D. C. (1962). **Augmenting Human Intellect.**

39. Clark, A., & Chalmers, D. (1998). **The Extended Mind.**

40. Hutchins, E. (1995). **Cognition in the Wild.**

41. Hollan, J., Hutchins, E., & Kirsh, D. (2000). **Distributed Cognition.** TOCHI.

42. Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). **A Model for Types and Levels of Human Interaction with Automation.**

43. Bainbridge, L. (1983). **Ironies of Automation.** *Automatica*.

44. Endsley, M. R. Work on automation and situation awareness.

45. Woods, D. D. Work on automation surprise, resilience, and joint cognitive systems.

46. Klein, G., Woods, D. D., Bradshaw, J. M., Hoffman, R. R., & Feltovich, P. J. (2004). **Ten Challenges for Making Automation a Team Player.**

47. Milgrom, P., & Roberts, J. (1990). Work on complementarities and organizational change.

48. Kremer, M. (1993). **The O-Ring Theory of Economic Development.** *Quarterly Journal of Economics*.

49. Grossman, G. M., & Rossi-Hansberg, E. (2008). **Trading Tasks: A Simple Theory of Offshoring.** *American Economic Review*.

50. Autor, D. H., Levy, F., & Murnane, R. J. (2003). **The Skill Content of Recent Technological Change.** *Quarterly Journal of Economics*.

51. Deming, D. J. (2017). **The Growing Importance of Social Skills in the Labor Market.** *Quarterly Journal of Economics*.

52. Deming, D. J., & Noray, K. (2020). **Earnings Dynamics, Changing Job Skills, and STEM Careers.** *Quarterly Journal of Economics*.

53. Felten, E., Raj, M., & Seamans, R. Work on occupational exposure to AI.

54. Eloundou, T., Manning, S., Mishkin, P., & Rock, D. (2023). **GPTs are GPTs: An Early Look at the Labor Market Impact Potential of Large Language Models.**

55. Gmyrek, P., Berg, J., & Bescond, D. (2023). **Generative AI and Jobs: A Global Analysis of Potential Effects on Job Quantity and Quality.** ILO.

56. International Labour Organization. Recent work on generative AI exposure, augmentation, and automation.

57. OECD. Recent work on artificial intelligence, tasks, skills, and labor-market transformation.

58. World Economic Forum. (2025). **Future of Jobs Report 2025.**

59. Frey, C. B., & Osborne, M. A. (2017). **The Future of Employment.** *Technological Forecasting and Social Change*.

60. Susskind, D. (2020). **A World Without Work.** Metropolitan Books.

61. Acemoglu, D., & Johnson, S. (2023). **Power and Progress.** PublicAffairs.

62. Simon, H. A. (1960/1996). Work on organizations, bounded rationality, and task decomposition.

63. Thompson, N. C., et al. Work on AI scaling economics and compute limits.

64. Farboodi, M., Koh, A. J., et al. (2026). **Data-Driven Automation.** NBER Working Paper 35320.

65. Trammell, P., et al. (2023/2026 revision). **Economic Growth under Transformative AI.** NBER Working Paper 31815.

66. **A Framework for Designing Human-Centric Work in the Age of AI.** (2026). CFE Working Paper No. 6 / arXiv:2604.01364.

67. **Closing the Complementarity Gap in Human–AI Decision Making.** (2025/2026). arXiv:2512.07801.

68. Arnaiz-Rodriguez, A., et al. (2025). **Towards Human-AI Complementarity in Matching Tasks.** arXiv:2508.13285.

69. **Roles of Artificial Intelligence in Collaboration with Humans.** (2025). *Management Science*.

70. Krakowski, S., et al. (2025). **Human-AI Agency in the Age of Generative AI.**

71. UFI-01 (2026). **鋸齒智能不是終局：從人機互補到認知握手與適應方向反轉.**

72. UFI-02 (2026). **載體成長不對稱：自然人類停滯與人工智能的可升級能力包絡.**

73. PGMV-03 (2026). **意義稀缺性遷移：從作品稀缺到判斷、選擇與整合稀缺.**

74. PGMV-04 (2026). **能力之後的意義：當不可替代性不再成立.**

75. PGMV-05 (2026). **關係不是字串：來源、歷史與主體如何生成意義.**

76. PGMV-06 (2026). **選擇、承諾與不可逆性：意義作為責任結構.**

77. PGMV-08 (2026). **智能壟斷結束之後：尊嚴、人權與跨主體普世主義.**

78. PGMV-15 (2026). **後生成文明：從無限候選宇宙到共同世界選擇.**

79. Neo.K (2026). **後人類奇點前夜猜想：自然人類中心文明向多主體造物文明的相變.**

80. Neo.K (2026). **後人類匯流：智能、生命、能源、虛擬世界與太空能力的耦合相變.**

---

## 附錄 A：Dynamic Complementarity State

$$
\boxed{
\mathfrak C_{HA}(t)
=
(
\mathcal D_H,
\mathcal D_A,
\mathcal D_E,
\mathcal D_{H\oplus A},
Cost,
Reliability,
Deployment,
Institution
)_t.
}
$$

---

## 附錄 B：四種互補 regime

```text
STABLE COMPLEMENTARITY
human/AI division remains broadly stable
        |
        v
MIGRATING COMPLEMENTARITY
old human tasks disappear, new ones appear
        |
        v
COMPLEMENTARITY EROSION
weighted human-dominant region shrinks
        |
        v
HYBRID / POSTHUMAN EXPANSION
natural-human advantage shrinks while H⊕A grows
```

這四者不是必然時間順序，而是可觀察 regime。

---

## 附錄 C：Residual Bottleneck Cliff

```text
AI automates 90%
       |
AI automates 95%
       |
AI automates 99%
       |
Human still required for final bottleneck
       |
       v
AI crosses capability + reliability + economic gate
       |
       v
HUMAN-REQUIRED  →  HUMAN-OPTIONAL
```

---

## 附錄 D：Complementarity Erosion Vector

$$
\boxed{
\mathbf E_C
=
(
E_{cap},
E_{econ},
E_{inst},
E_{rel},
E_{moral}
).
}
$$

不要把不同型別壓成單一「被取代率」。

---

## 附錄 E：HACO — Human–AI Complementarity Observatory

```yaml
time:
domain:
human_distribution:
ai_distribution:
hybrid_distribution:

potential_complementarity_mass:
realized_complementarity_gain:
human_advantage_measure:
hybrid_advantage_measure:

residual_bottlenecks:
verification_tax:
deployment_reservoir:
oversight_effectiveness:
deskilling_drift:

cost:
reliability:
institution:
```

---

## 附錄 F：Task Creation–Automation Race

$$
\boxed{
\lambda_N
=
\text{new human-advantaged task creation rate}
}
$$

$$
\boxed{
\lambda_A
=
\text{AI automation catch-up rate}
}
$$

```text
λ_N > λ_A  → migrating / renewed complementarity possible
λ_N ≈ λ_A  → dynamic equilibrium possible
λ_N < λ_A  → erosion pressure increases
```

---

## 附錄 G：第一部三篇總鏈

```text
UFI-01
JAGGEDNESS IS A STATE
not permanent cognitive division
        ↓
UFI-02
SUBSTRATE UPDATE GEOMETRIES DIFFER
weak dimensions may have different repair rates
        ↓
UFI-03
COMPLEMENTARITY FRONTIER MOVES
stable / migrate / erode / hybridize
```

---

## 附錄 H：UFI 系列進度

1. **UFI-01 — 鋸齒智能不是終局** — COMPLETE
2. **UFI-02 — 載體成長不對稱** — COMPLETE
3. **UFI-03 — 互補侵蝕** — COMPLETE
4. **UFI-04 — 競爭智能棘輪** — NEXT
5. **UFI-05 — 越有用越停不下來**
6. **UFI-06 — AI 到底是什麼？**
7. **UFI-07 — 從禁止 AI 到治理計算**
8. **UFI-08 — 天真工具終局論的終結**

---

## 附錄 I：一句話版本

$$
\boxed{
\text{人機互補不是「人類永遠有 AI 不會的技能」，而是一條隨能力、成本、可靠性、任務生成與制度一起移動的前沿。}
}
$$

更尖銳地：

$$
\boxed{
\text{今天最後那個需要人的 bottleneck，可能明天讓人更值錢；也可能在被跨過的那一刻，讓整個角色突然從「必要」變成「可選」。}
}
$$
