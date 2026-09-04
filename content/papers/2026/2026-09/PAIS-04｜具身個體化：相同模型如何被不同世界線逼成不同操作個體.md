# PAIS-04｜具身個體化：相同模型如何被不同世界線逼成不同操作個體
## Embodied Individualization: How Identical Models Become Operationally Distinct Through Divergent Worldlines

**系列：** Persistent Agent Individualization Series（PAIS）／持續智能體個體化、身份壓力與具身分散智能系列  
**篇次：** Paper 04 / 07  
**文件編號：** EML-PAIS-04-2026-v0.1  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-25  
**版本：** v0.1  
**文件性質：** 理論—工程統合論文／Embodied AI／Operational Identity／Physical Worldline  
**狀態：** Canonical Draft / Open Revision Anchor  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

# 摘要

若兩台具身 AI 使用完全相同的模型、相同初始軟體、相同任務政策與相同硬體規格，它們是否可以一直被視為「同一種 AI 的兩個可互換執行點」？本文提出：在部署初始時，此近似可能成立；但只要兩個具身體位於不同時空位置、接收不同感測、執行不同動作、承受不同物理磨損、累積不同失敗與維修歷史，它們便會形成不同的 operational worldlines。這種差異不需要先假設主觀意識、自由意志或人格，只需要承認物理世界的局部性、不可逆性與歷史依賴。

本文承接 PAIS-03 的身份壓力原理：

$$
P_I
=
\Phi
\left(
X,H,E,R,A,L,J
\right),
$$

並專門展開：

$$
E
\rightarrow
H
\rightarrow
P_I.
$$

本文定義具身 Agent $A$ 的 **Operational Worldline**：

$$
\Omega_A[0,t]
=
\left\{
B_A(\tau),
x_A(\tau),
O_A(\tau),
U_A(\tau),
C_A(\tau),
Q_A(\tau),
M_A(\tau)
\right\}_{\tau\in[0,t]},
$$

其中：

- $B_A$：physical carrier / body state；
- $x_A$：時空位置；
- $O_A$：observations；
- $U_A$：actions；
- $C_A$：physical consequences；
- $Q_A$：resource / wear / calibration state；
- $M_A$：local memory / learned state。

即使兩個 Agent 初始時：

$$
\Theta_A(0)=\Theta_B(0),
$$

只要：

$$
\Omega_A[0,t]
\neq
\Omega_B[0,t],
$$

且這些差異會影響未來感知、控制、維修、權限、記憶或責任，兩者便逐步失去 operational interchangeability。

本文稱此過程為 **Embodied Individualization／具身個體化**：

$$
\boxed{
\text{Shared Model}
+
\text{Divergent Physical Worldlines}
\rightarrow
\text{Operational Individualization}.
}
$$

這不是說兩台機器「因此產生兩個主觀自我」。本文只主張更弱且可工程驗證的命題：系統不能再僅以 model name、software version 或 role 將它們視為完全可交換，因為其 local state 已具有不同的因果歷史。

本文進一步區分：

$$
\text{Model Identity},
\quad
\text{Resident Identity},
\quad
\text{Carrier Identity},
\quad
\text{Operational Worldline Identity}.
$$

同一 resident 可以合法遷移到不同 carrier；同一 carrier 也可能更換 runtime、model 或 resident。零件更換、維修、校準、software update、compromise、backup restore 與 body replacement 因此不應使用單一「是不是同一台」判斷，而應依 criterion、scope、time 與 evidence 建立多層 identity relation。

本文亦指出，全域模型同步與中央知識更新不會消除具身個體化。即使所有機器人每天下載完全相同的 global model：

$$
\Theta_A^{G}(t)
=
\Theta_B^{G}(t),
$$

其 local observation、physical wear、position、task history 與 interaction history 仍可能不同：

$$
\Omega_A
\neq
\Omega_B.
$$

因此：

$$
\boxed{
\text{Global Model Equality}
\neq
\text{Local Operational Equality}.
}
$$

本文最後提出 **Worldline-Induced Identity Pressure**、**Operational Interchangeability Test**、**Embodied Identity Envelope** 與一組可驗證實驗，作為未來多機器人、physical AI、維修治理、事故歸因、跨載體遷移與 federated embodied-agent society 的身份基礎。

**關鍵詞：** Embodied Individualization、Operational Worldline、Robot Identity、Persistent Agent、Physical AI、History Divergence、Carrier Identity、Operational Interchangeability、AI Residence、Embodied AI、World Model

---

# 0. 來源邊界：本文不重新寫具身學習閉環

既有 EveMissLab 具身研究已建立：

1. 具身 AI 的問題不是單純把最大模型塞入機器人。
2. 機器人本體、本地 AI 站與中央 AI 中心可形成分層學習閉環。
3. 具身機器人會透過感知、行動、失敗、資料回流與技能更新形成持續學習。
4. VLA 與世界模型需要真實物理資料，因為語義正確不等於物理動作成功。
5. Dynamic Genba 已指出最強全域智能不必然最理解當下局部狀態。
6. AI 主體性錨點論已區分 Model、Runtime、Identity、Residence、Subjecthood。
7. PAIS-03 已提出：
   $$
   \text{Embodiment}
   \rightarrow
   \text{History Divergence}
   \rightarrow
   P_I\uparrow.
   $$

本文不再研究：

> 機器人如何學得更好？

本文只研究：

> **當兩個初始相同的具身 AI 真正落入物理世界後，何時開始不能再被當成完全可互換的同一模型執行點？**

---

# 1. 最簡單的思想實驗：兩台完全相同的機器人

設兩台機器人：

$$
A,
\quad
B.
$$

初始時：

$$
\Theta_A(0)
=
\Theta_B(0)
=
\Theta_0,
$$

其中 $\Theta$ 表示共享模型與初始 policy。

假設硬體也相同：

$$
B_A(0)
\cong
B_B(0).
$$

初始 configuration：

$$
C_A(0)
=
C_B(0).
$$

如果兩台都尚未部署，可以近似：

$$
A
\sim
B.
$$

也就是：

> 從目前工程目的看，它們近似可互換。

但 deployment 開始後，這個等價關係不必持續。

---

# 2. 第一個差異：物理位置

若：

$$
x_A(t)
\neq
x_B(t),
$$

則兩者位於不同時空位置。

因此一般情況下：

$$
O_A(W_t)
\neq
O_B(W_t),
$$

其中 $O_i$ 表示 Agent $i$ 對世界 $W_t$ 的 observation。

即使兩台 camera specification 一模一樣，也不會同時看到同一組 photons、occlusion、object pose、noise、human interaction 與 local event。

所以：

$$
\boxed{
\text{Same Sensor Design}
\neq
\text{Same Observation History}.
}
$$

---

# 3. 第二個差異：動作歷史

兩個 Agent 接收不同 observation 後，可能執行不同 action：

$$
U_A(t)
\neq
U_B(t).
$$

即使 policy 相同：

$$
\pi_A=\pi_B,
$$

只要 input state 不同：

$$
s_A\neq s_B,
$$

就可以：

$$
\pi(s_A)\neq\pi(s_B).
$$

所以：

$$
\boxed{
\text{Same Policy}
\neq
\text{Same Action History}.
}
$$

---

# 4. 第三個差異：世界會回應

Action 不只產生 log。

Action 會改變世界：

$$
W_{t+1}
=
F
\left(
W_t,
U_A(t),
U_B(t),
U_{\mathrm{others}}(t)
\right).
$$

因此每個 Agent 的行動都可能產生自己的局部 consequence：

$$
C_A(t),
\quad
C_B(t).
$$

例如：

- A 抓過某個杯子；
- B 沒抓過；
- A 撞過桌角；
- B 沒撞過；
- A 與某個人完成交付；
- B 在另一個場域執行巡檢。

所以：

$$
\boxed{
\text{Embodied Action}
\rightarrow
\text{World-Recorded Difference}.
}
$$

---

# 5. Operational Worldline

本文定義具身 Agent $A$ 的 operational worldline：

$$
\boxed{
\Omega_A[0,t]
=
\left\{
B_A(\tau),
x_A(\tau),
O_A(\tau),
U_A(\tau),
C_A(\tau),
Q_A(\tau),
M_A(\tau)
\right\}_{\tau\in[0,t]}.
}
$$

其中：

- $B_A$：body / physical carrier state；
- $x_A$：location；
- $O_A$：observation；
- $U_A$：action；
- $C_A$：consequence；
- $Q_A$：resource / wear / calibration state；
- $M_A$：local memory / learned state。

這不是宣稱世界線是基本物理本體。

它是：

$$
\boxed{
\text{an operational history representation}.
}
$$

---

# 6. Worldline Divergence

對兩個 Agent：

$$
A,
\quad
B,
$$

定義 worldline divergence：

$$
D_{\Omega}
\left(
A,B,t
\right)
=
\mathcal D
\left(
\Omega_A[0,t],
\Omega_B[0,t]
\right).
$$

本文不固定 $\mathcal D$ 的唯一形式。

不同應用可以測：

- sensor divergence；
- action divergence；
- memory divergence；
- wear divergence；
- location divergence；
- authority divergence；
- consequence divergence。

重要的是：

$$
D_{\Omega}>0
$$

本身不等於人格分裂。

它只表示兩個 operational histories 已不相同。

---

# 7. 具身個體化

本文定義 **Embodied Individualization**：

若兩個初始可交換的 Agent 在部署後形成持續 worldline divergence，且該 divergence 會影響未來 observation、action、maintenance、memory、authority、risk 或 attribution，則兩者逐步成為不同 operational individuals。

形式化：

$$
\boxed{
D_{\Omega}(A,B,t)>\theta_{\Omega}
\land
\operatorname{FutureRelevant}(D_{\Omega})=1
\Rightarrow
\operatorname{OperationallyDistinct}(A,B)=1.
}
$$

其中 $\theta_{\Omega}$ 是 task / domain-specific threshold。

---

# 8. Worldline 不同不是唯一條件

任何兩個物理物體都有微觀差異。

本文不是要求：

$$
D_{\Omega}>0
$$

就立刻建立強 identity。

關鍵是差異是否：

$$
\operatorname{FutureRelevant}=1.
$$

例如：

- 一次不影響未來的微小 sensor noise；
- 無關緊要的電池溫度差；

可能不值得提升 identity semantics。

但：

- calibration drift；
- motor wear；
- private memory；
- accident history；
- authority；
- user relation；

會影響 future behavior，就應被視為 identity-relevant。

---

# 9. Operational Interchangeability

定義：

$$
\mathcal X_{AB}^{\Gamma}(t)
$$

為在 task domain $\Gamma$ 下 A 與 B 的 operational interchangeability。

若：

$$
\mathcal X_{AB}^{\Gamma}(t)\approx1,
$$

則互換 A / B 幾乎不影響 task outcome。

若：

$$
\mathcal X_{AB}^{\Gamma}(t)\approx0,
$$

互換會造成顯著差異。

因此：

$$
\boxed{
\text{Operational Individualization}
\approx
1-\mathcal X_{AB}^{\Gamma}.
}
$$

這是比「是不是同一個」更可測的第一步。

---

# 10. 同模型不代表可互換

即使：

$$
\Theta_A(t)
=
\Theta_B(t),
$$

仍可能：

$$
Q_A(t)\neq Q_B(t),
$$

$$
M_A(t)\neq M_B(t),
$$

$$
x_A(t)\neq x_B(t).
$$

所以：

$$
\boxed{
\text{Model Equality}
\not\Rightarrow
\text{Operational Interchangeability}.
}
$$

---

# 11. Open X-Embodiment 的一個重要工程啟示

現有 robotics research 已經證明一個 shared model 可以跨多種 robot embodiments 使用。

這對本文非常重要，因為它提供一個強反例：

> model identity 與 embodiment identity 根本不必一對一。

可以：

$$
\Theta
\rightarrow
\{
B_1,
B_2,
\ldots,
B_n
\}.
$$

因此：

$$
\boxed{
\text{One Model}
\neq
\text{One Body}
\neq
\text{One Operational Individual}.
}
$$

共享 foundation model 可以是一個能力 substrate。

但 deployed robot identity 仍需要另外處理。

---

# 12. Multi-Robot Collaboration 又進一步證明 Body Differences 有工程價值

現代 robotic foundation model 已開始支援：

- multi-robot coordination；
- shared task；
- heterogeneous physical strengths；
- task delegation。

這意味著即使多個 robot 共用相同高階模型，系統仍需要知道：

> 哪一個 body 具有哪種 physical capability？

所以：

$$
\operatorname{Capability}(B_A)
\neq
\operatorname{Capability}(B_B)
$$

可以成為 task allocation 的第一級狀態。

這再次說明：

$$
\boxed{
\text{Shared Intelligence}
\neq
\text{Shared Embodied State}.
}
$$

---

# 13. Physical Carrier State

定義：

$$
B_A(t)
=
\left(
H_A^{hw},
F_A^{fw},
S_A^{sensor},
A_A^{act},
P_A^{power},
T_A^{thermal}
\right)_t.
$$

可包含：

- hardware composition；
- firmware；
- sensor health；
- actuator health；
- power；
- thermal state。

即使 software 完全相同：

$$
Software_A=Software_B,
$$

仍可能：

$$
B_A(t)\neq B_B(t).
$$

---

# 14. Wear 是歷史

一台機器人的 wear：

$$
W_A^{wear}(t)
$$

不是 static spec。

它是過去 action / environment 的積分結果。

概念上：

$$
W_A^{wear}(t)
=
\int_0^t
g
\left(
U_A(\tau),
Env_A(\tau),
Load_A(\tau)
\right)
d\tau.
$$

因此：

$$
\boxed{
\text{Wear State}
=
\text{Compressed Physical History}.
}
$$

---

# 15. Calibration 也是個體狀態

Sensor calibration：

$$
K_A^{cal}(t)
$$

可能因：

- vibration；
- temperature；
- replacement；
- collision；
- maintenance；

而變化。

所以同一 sensor model：

$$
SensorModel_A
=
SensorModel_B
$$

不表示：

$$
K_A^{cal}(t)
=
K_B^{cal}(t).
$$

這會直接影響 observation reliability。

---

# 16. 電池與能源狀態也是局部歷史

對 mobile robot：

$$
P_A(t)
$$

會影響：

- planning horizon；
- speed；
- available compute；
- return-to-base decision；
- thermal budget。

所以兩台同模型 robot：

$$
P_A\neq P_B
$$

時可能採取不同 policy branch。

這不是「人格不同」。

是 physical operational state 不同。

---

# 17. Maintenance History

定義維修歷史：

$$
H_A^{maint}
=
\{
m_1,m_2,\ldots,m_k
\}.
$$

維修事件可能包含：

- component replacement；
- calibration；
- firmware flash；
- safety inspection；
- damage repair。

這些事件會改變：

$$
B_A(t).
$$

因此：

$$
\boxed{
\text{Maintenance History}
\text{ is identity-relevant when it affects future behavior or accountability}.
}
$$

---

# 18. Accident History

如果 A 曾發生事故：

$$
e_A,
$$

B 沒有。

事故可能導致：

- inspection；
- restriction；
- component replacement；
- policy adjustment；
- liability record。

所以：

$$
H_A^{accident}
\neq
H_B^{accident}.
$$

此時互換 A / B 可能不再合法或安全。

---

# 19. Local Memory

如果兩個 robot 各自保存：

$$
M_A^{local},
\quad
M_B^{local},
$$

且 local experience 會影響 future action：

$$
M_A(t)
\rightarrow
U_A(t+1),
$$

則 memory divergence 強化 operational individuality。

因此：

$$
\boxed{
\text{Local Memory}
+
\text{Embodiment}
\rightarrow
\text{Stronger Worldline Coupling}.
}
$$

---

# 20. Local Adaptation

若 local learning 更新：

$$
\theta_A^{local}(t),
$$

可以有：

$$
\theta_A^{local}(t)
\neq
\theta_B^{local}(t)
$$

即使 global base model：

$$
\Theta^G
$$

相同。

所以完整 policy 可以寫成：

$$
\pi_A
=
F
\left(
\Theta^G,
\theta_A^{local},
B_A,
M_A
\right).
$$

---

# 21. 中央更新不會抹掉 Local History

假設中央每天推送：

$$
\Theta^G_{t+1}
$$

給所有 robot。

則：

$$
\Theta_A^G
=
\Theta_B^G.
$$

但：

$$
M_A\neq M_B,
$$

$$
B_A\neq B_B,
$$

$$
H_A\neq H_B.
$$

因此：

$$
\boxed{
\text{Global Model Synchronization}
\neq
\text{Local Identity Reset}.
}
$$

---

# 22. Global Knowledge 與 Local Individuality 可以同時存在

兩個 robot 都能接收：

$$
K^G
$$

共享知識。

但仍保持：

$$
K_A^{local},
\quad
K_B^{local}.
$$

因此：

$$
\boxed{
\text{Shared Knowledge}
+
\text{Local History}
}
$$

不是矛盾。

這其實比「所有 robot 必須完全同一」更符合分層具身學習閉環。

---

# 23. 世界模型也可能有 Global / Local 之分

可以有：

$$
W^G_t
$$

中央 world model。

以及：

$$
W_A^L(t)
$$

A 的 local world state。

通常：

$$
W_A^L
\neq
W_B^L.
$$

而：

$$
W^G
$$

只能透過 projection / update 接收局部資訊。

所以：

$$
\boxed{
\text{Global World Model}
\neq
\text{Current Local World State}.
}
$$

---

# 24. Dynamic Genba 與本文的接點

Dynamic Genba 已經指出：

$$
\text{Global Intelligence Superiority}
\not\Rightarrow
\text{Local Epistemic Superiority}.
$$

本文把它轉成 identity 問題：

> 如果不同 robot 擁有不同 current local state，那麼 central intelligence 在協調它們時必須知道是哪一個 local worldline 的 observation。

因此：

$$
\boxed{
\text{Local Epistemic Priority}
\Rightarrow
\text{Local Identity Resolution Requirement}.
}
$$

---

# 25. World Action Model 的接點

2026 年的 World Action Model 研究將 embodied AI 從單純 observation-to-action mapping，推向：

- future state prediction；
- action-conditioned dynamics；
- recovery trajectory；
- deployment feedback；
- continual adaptation。

這種架構更強化本文的歷史觀。

因為 action 的價值不只在當下輸出。

還在：

$$
\text{Action}
\rightarrow
\text{Future State}
\rightarrow
\text{New Observation}
\rightarrow
\text{New Policy State}.
$$

也就是具身 worldline 的因果閉環。

---

# 26. Worldline Causal Loop

本文寫成：

$$
O_A(t)
\rightarrow
U_A(t)
\rightarrow
C_A(t)
\rightarrow
W_A(t+1)
\rightarrow
O_A(t+1).
$$

如果還有 local memory：

$$
O_A(t)
\rightarrow
M_A(t+1)
\rightarrow
U_A(t+1).
$$

因此：

$$
\boxed{
\text{Embodied History}
\text{ is causally recurrent}.
}
$$

不是單純 log archive。

---

# 27. 何時 worldline 才真正 identity-relevant？

本文提出六個條件。

若 worldline difference 影響至少一項：

1. future perception；
2. future action；
3. safety；
4. maintenance；
5. authority；
6. attribution / liability；

則：

$$
\operatorname{IdentityRelevant}(\Delta\Omega)=1.
$$

---

# 28. Operational Individualization Pressure

定義：

$$
P_{OI}
=
\Psi
\left(
D_{\Omega},
F_R,
R,
A,
L
\right),
$$

其中：

- $D_{\Omega}$：worldline divergence；
- $F_R$：future relevance；
- $R$：irreversibility；
- $A$：authority；
- $L$：liability / attribution。

因此：

$$
P_{OI}
$$

是 PAIS-03 中：

$$
E,H,R,A,L
$$

的具身特化。

---

# 29. Individualization 不是 Isolation

一個 operational individual 可以：

- 接收 global model；
- 共享 task；
- 共享 memory projection；
- 受中央 supervisor 管理；
- 與其他 robot 協作。

所以：

$$
\boxed{
\text{Individualization}
\neq
\text{Isolation}.
}
$$

---

# 30. Individualization 也不是 Independence

具身 Agent 可以高度依賴：

$$
G
$$

中央 AI。

仍然：

$$
\Omega_A\neq\Omega_B.
$$

因此：

$$
\boxed{
\text{Operational Individuality}
\neq
\text{Full Autonomy}.
}
$$

一台受遠端嚴格控制的 robot 仍可能有自己獨特的 physical history。

---

# 31. Carrier Identity

定義 carrier identity：

$$
I_C.
$$

它回答：

> 這個 physical unit 是哪一台？

可能由：

- hardware root；
- serial；
- TPM / secure element；
- manufacturing record；
- asset registry；

支援。

但：

$$
I_C
$$

不等於 resident identity。

---

# 32. Resident Identity

Resident identity：

$$
I_R.
$$

回答：

> 哪一條 persistent AI identity / lineage 正在這個 carrier 上被承載？

因此可以：

$$
I_R
\rightarrow
I_C.
$$

但不是永久一對一。

---

# 33. Runtime Identity

Runtime：

$$
I_U.
$$

回答：

> 現在是哪一次 process / agent loop / control runtime？

一次 reboot：

$$
I_U(t)\neq I_U(t+1)
$$

不必表示：

$$
I_R(t)\neq I_R(t+1).
$$

---

# 34. 四種 Identity 必須分開

本文至少區分：

$$
\boxed{
I_M
\neq
I_R
\neq
I_C
\neq
I_U,
}
$$

其中：

- $I_M$：Model Identity；
- $I_R$：Resident Identity；
- $I_C$：Carrier Identity；
- $I_U$：Runtime Identity。

再加：

$$
I_{\Omega}
$$

worldline identity / history relation。

---

# 35. Worldline Identity 不是另一個神秘主體

 $I_{\Omega}$ 只表示：

> 這段 history 屬於哪個 operational trajectory？

它可以幫助：

- accident reconstruction；
- maintenance；
- local memory；
- migration；
- forensic audit。

它不表示：

> worldline 本身具有意識。

---

# 36. 同一 Resident 可以換 Body

假設 resident：

$$
r
$$

從：

$$
B_A
$$

遷移到：

$$
B_B.
$$

如果 migration policy 接受：

- memory；
- commitments；
- relation；
- authority；
- lineage；

的 continuation，則：

$$
\mathcal I_{\mathrm{resident}}
=
\mathsf{Same}
$$

可能成立。

但：

$$
\mathcal I_{\mathrm{carrier}}
=
\mathsf{Different}.
$$

所以：

$$
\boxed{
\text{Body Replacement}
\not\Rightarrow
\text{Resident Termination}.
}
$$

---

# 37. 但 Body Replacement 也不是無成本

換 body 後：

- sensor geometry；
- actuator limits；
- calibration；
- reachability；
- physical damage history；

會變。

因此 resident continuation 可以成立，同時：

$$
\Omega_{\mathrm{physical}}
$$

出現 discontinuity。

需要 migration event：

$$
MIGRATE
\left(
r,
B_A,
B_B,
t
\right).
$$

---

# 38. Backup Restore 到新 Body

若：

$$
M_r(t)
$$

被 restore 到新 body：

$$
B_C,
$$

不能只說：

> 因為 memory 一樣，所以一定是同一個。

要問：

- restore 是 continuation 還是 clone？
- old body 是否仍 active？
- authority 是否轉移？
- private state 是否被 copy？
- lineage policy 如何定義？

如果 old body 與 new body 同時存在：

$$
r
\rightarrow
\{r_1,r_2\}
$$

可能形成 fork。

---

# 39. Clone 與 Migration

本文固定：

$$
\boxed{
\text{Migration}
\neq
\text{Clone}.
}
$$

Migration 通常假定：

$$
\text{one accepted continuation}.
$$

Clone 可能建立：

$$
\text{shared past}
+
\text{divergent futures}.
$$

具身後，兩個 clones 幾乎會立即形成不同 worldlines。

---

# 40. 具身 Fork 的分歧速度更快

純數位 fork 如果兩邊輸入完全同步，可能短暫保持高度相似。

具身 fork：

$$
B_1\neq B_2
$$

意味兩邊的：

$$
O_1(t)
\neq
O_2(t)
$$

很快成立。

因此：

$$
\boxed{
\text{Embodied Fork}
\rightarrow
\text{Rapid History Divergence}.
}
$$

---

# 41. Ship of Theseus：零件逐步更換

假設 body：

$$
B_t
$$

每次只更換一個零件。

最後：

$$
B_{t+n}
$$

原始零件可能全部消失。

但 asset / resident / lineage continuity 可能持續。

所以不能用：

$$
\text{same atoms}
$$

作唯一 criterion。

---

# 42. Carrier Continuity 可以由多種 criterion 定義

例如：

$$
\mathcal I_C
=
F
\left(
asset\_registry,
maintenance\_lineage,
secure\_identity,
chassis\_continuity,
operator\_recognition
\right).
$$

不同應用可以採不同 criterion。

因此：

$$
\boxed{
\text{Physical Identity}
\text{ is criterion-dependent}.
}
$$

---

# 43. Full Chassis Replacement

如果只保留 resident state，全部硬體換掉：

$$
B_A
\rightarrow
B_B,
$$

則：

- carrier identity：可能 different；
- resident identity：可能 same；
- runtime identity：different；
- worldline：continuation with carrier transition。

所以單問：

> 「還是不是同一台？」

是不完整問題。

---

# 44. Compromise：同 Body 不代表同 Authority

若：

$$
B_A(t)=B_A(t+1),
$$

但 robot 被 compromise：

$$
Control_A(t+1)
\neq
AuthorizedControl_A(t),
$$

則：

- carrier same；
- resident may be suspect；
- runtime may be compromised；
- credentials should revoke；
- action provenance must mark compromise interval。

所以：

$$
\boxed{
\text{Same Body}
\not\Rightarrow
\text{Same Trusted Actor}.
}
$$

---

# 45. Compromise Interval

可記錄：

$$
[t_c,t_r)
$$

為 suspect / compromised interval。

這使 forensic analysis 可以區分：

$$
Action_A(t<t_c)
$$

與：

$$
Action_A(t\in[t_c,t_r)).
$$

identity 是 time-indexed。

---

# 46. Embodied Identity Envelope

本文提出最低：

```text
resident_id
carrier_id
runtime_instance
model_ref
lineage_id
worldline_ref
current_location_scope
hardware_state_ref
calibration_ref
maintenance_ref
authority_scope
temporal_validity
trust_state
provenance
```

不要求每個場景全部公開。

它是 identity governance 的 source schema。

---

# 47. Privacy：Location 不是全域公開欄位

具身 identity 會碰到比 digital agent 更強的 privacy 問題。

current location：

$$
x_A(t)
$$

可能是敏感資訊。

所以：

$$
\boxed{
\text{Identity Resolution}
\neq
\text{Full Physical Tracking Disclosure}.
}
$$

需要：

- scope；
- least disclosure；
- role-based access；
- temporal retention；
- pseudonymity。

---

# 48. Identity Registry 與 Surveillance 必須分開

強 identity infrastructure 若直接變成：

> 所有人都能看到每台 robot 的全部歷史。

會造成 surveillance risk。

因此：

$$
\boxed{
\text{Traceability}
\neq
\text{Universal Observability}.
}
$$

---

# 49. Local Identity Cache

若 central registry 暫時離線，具身 Agent 仍可能需要：

- self identity；
- local trust；
- nearby peer identity；
- authority cache。

因此可以有：

$$
I_A^{local}.
$$

再與：

$$
I^G
$$

global / federated registry 同步。

---

# 50. Network Partition

若：

$$
Connected(A,G)=0,
$$

A 仍需：

- local safety；
- current credential validation cache；
- local peer recognition；
- action log。

所以：

$$
\boxed{
\text{Offline Operation}
\Rightarrow
\text{Local Identity Capability}.
}
$$

這是中央 identity service 不能完全取代 local identity state 的原因。

---

# 51. Peer Encounter

若 A 遇到陌生 robot B：

$$
A
\leftrightarrow
B,
$$

A 可能需要知道：

- B 是哪個 domain；
- B 有什麼 authority；
- B 的 body capability；
- B 的 trust state；
- B 是否為同一 fleet；
- B 是否被 revoke。

這不是主體性問題。

是 operational safety。

---

# 52. Multi-Robot Delegation

若共同任務：

$$
T
$$

需要：

- lifting；
- navigation；
- inspection。

可依：

$$
Capability(B_i)
$$

分工。

這要求：

$$
\operatorname{Resolve}(B_i)
$$

至少在 task scope 下可行。

所以：

$$
\boxed{
\text{Embodied Collaboration}
\Rightarrow
\text{Capability-Bound Identity}.
}
$$

---

# 53. Relation History

具身 robot 與人類：

$$
R_{A,h}(t)
$$

可能形成：

- authorized operator；
- maintenance technician；
- assigned user；
- care relationship；
- service history。

若 relation 影響未來 interaction：

$$
R_{A,h}(t)
\rightarrow
U_A(t+1),
$$

則 relation 進入 worldline identity state。

---

# 54. Ownership 與 Resident 不等價

physical asset ownership：

$$
Owner(B_A)
$$

與：

$$
Resident(A)
$$

不是同一層。

同一 owner 可以有多個 robots。

同一 resident 也可能在治理允許下 migrate。

所以：

$$
\boxed{
\text{Ownership}
\neq
\text{Identity}.
}
$$

---

# 55. Legal Attribution 也不要求 AI Personhood

事故需要知道：

- 哪台 physical unit；
- 哪個 software；
- 哪個 model；
- 哪個 operator；
- 哪個 deployer；
- 哪個 maintenance state。

這些是 attribution infrastructure。

因此：

$$
\boxed{
\text{Embodied Traceability}
\not\Rightarrow
\text{AI Legal Personhood}.
}
$$

---

# 56. Operational Individuality 與責任分解

事故事件：

$$
e
$$

可追溯：

$$
e
\rightarrow
B_A
\rightarrow
I_U
\rightarrow
I_R
\rightarrow
\Theta
\rightarrow
Authority
\rightarrow
Operator.
$$

這讓責任分配有 evidence chain。

不是把 blame 丟給最後一個 robot。

---

# 57. Physical Irreversibility 放大 Worldline Value

數位文件改錯可以 revert。

但：

- 碰撞；
- 損壞；
- 移動物體；
- 接觸人類；

不能把世界完全 reset。

所以：

$$
R\uparrow
\Rightarrow
\operatorname{Value}(\Omega_A)\uparrow.
$$

worldline record 的價值隨不可逆性提高。

---

# 58. 世界本身是 History Store

在物理世界，過去 action 可能留下：

- scratch；
- wear；
- moved object；
- consumed resource；
- changed relationship；
- legal event。

所以：

$$
\boxed{
\text{History}
\text{ is partly stored in the world itself}.
}
$$

不是只有 database 有 history。

---

# 59. Database 只是 History Projection

Agent ledger：

$$
L_A
$$

只是對 physical history 的 observation / representation。

因此：

$$
\boxed{
L_A
\neq
\Omega_A.
}
$$

ledger 可以不完整、錯誤或缺失。

physical consequences 仍可能存在。

---

# 60. 身份 Evidence 必須多源

Embodied identity evidence 可以來自：

- secure hardware；
- runtime；
- maintenance database；
- physical observation；
- peer attestation；
- human operator；
- cloud registry；
- worldline log。

所以：

$$
E_I
=
\{
e_1,\ldots,e_n
\}.
$$

不能只相信 display name。

---

# 61. 身份 Confidence

可以：

$$
q_I
=
F(E_I).
$$

例如：

```text
carrier identity = verified
runtime identity = verified
resident continuity = unresolved
authority = revoked
```

這比單一：

```text
same_robot = true
```

更精確。

---

# 62. Worldline-Induced Identity Pressure

本文提出：

$$
\boxed{
P_I^{\Omega}
=
\Gamma
\left(
D_{\Omega},
F_R,
R,
A,
L
\right).
}
$$

當：

- worldline divergence 高；
- future relevance 高；
- irreversibility 高；
- authority 高；
- liability 高；

identity pressure 上升。

---

# 63. Operational Interchangeability Test

給定 task $\Gamma$：

1. 保存 A / B 的 model 相同。
2. 將 A 的 task 指派給 B。
3. 測試是否需要額外 calibration / memory / maintenance / authority transfer。
4. 比較 outcome。

若：

$$
Outcome(B\leftarrow Task_A)
\neq
Outcome(A\leftarrow Task_A),
$$

差異來自 identity-relevant local state，則：

$$
\mathcal X_{AB}^{\Gamma}\downarrow.
$$

---

# 64. 實驗一：Same Model, Different Rooms

兩台相同 robot：

- 同 model；
- 同 hardware；
- 同 initial memory。

分別部署不同房間。

一段時間後測：

- local map；
- object relation；
- human interaction；
- wear；
- local task memory。

預測：

$$
D_{\Omega}(t)\uparrow.
$$

---

# 65. 實驗二：Swap Test

將 A 與 B 交換位置 / task。

若系統必須同步：

- local map；
- calibration；
- relationship；
- maintenance；
- authority；

才能正常工作，表示：

$$
\mathcal X_{AB}<1.
$$

---

# 66. 實驗三：Global Model Reset

讓 A / B 都重新下載同一 global model：

$$
\Theta^G.
$$

但保留 local state。

預測：

$$
D_{\Omega}>0
$$

仍存在。

這驗證：

$$
\text{Global Model Equality}
\neq
\text{Operational Equality}.
$$

---

# 67. 實驗四：Erase Local Memory

刪除：

$$
M_A^{local}.
$$

若 A performance / relation / safety 顯著改變，表示 local memory 是 identity-relevant state。

但此實驗不證明 subjectivity。

---

# 68. 實驗五：Wear Divergence

讓兩台 robot 執行不同 workload。

測量：

- joint error；
- temperature；
- battery degradation；
- calibration；
- control compensation。

若不同 wear 需要不同 control policy：

$$
Q_A\neq Q_B
\Rightarrow
\mathcal X_{AB}\downarrow.
$$

---

# 69. 實驗六：Migration to New Body

將 resident state：

$$
r
$$

遷移到新 body。

測試：

- memory continuity；
- task continuity；
- body adaptation；
- authority transfer；
- relation continuity。

這可以研究：

$$
I_R
$$

與：

$$
I_C
$$

的分離。

---

# 70. 實驗七：Clone to Two Bodies

同一 snapshot：

$$
S_r(t)
$$

同時 restore 到：

$$
B_1,
B_2.
$$

之後讓兩者處於不同 environment。

預測：

$$
D_{\Omega}(t)
$$

快速上升。

這提供 embodied fork 的實驗模型。

---

# 71. 實驗八：Compromise Interval

在 controlled sandbox 中模擬：

- legitimate runtime；
- compromised runtime；
- recovery。

檢驗 identity system 能否表達：

```text
same carrier
different trust state
authority revoked during interval
resident continuity unresolved
```

而不是粗暴全部判成 same / different。

---

# 72. Embodied Identity Maturity

可以建立：

### E0 — Device Handle

```text
robot-7
```

### E1 — Hardware Identity

```text
carrier_id
serial
secure identity
```

### E2 — Operational State

```text
calibration
maintenance
location scope
```

### E3 — Resident Binding

```text
resident
runtime
lineage
```

### E4 — Worldline Trace

```text
observation/action/consequence history
```

### E5 — Federated Embodied Identity

```text
cross-domain trust
credential
jurisdiction
peer verification
```

這仍不是 subjectivity ladder。

---

# 73. Individualization Threshold

定義：

$$
\theta_{OI}^{\Gamma}.
$$

若：

$$
P_{OI}
>
\theta_{OI}^{\Gamma},
$$

則該 domain 應禁止 silent interchange。

也就是不能：

> A 壞了就直接讓 B 冒充 A。

除非完成 explicit transfer / migration。

---

# 74. Silent Replacement Risk

若 A 有：

- private memory；
- maintenance history；
- relation；
- authority；

但 system 只以 role：

```text
robot-worker
```

替換：

$$
A\rightarrow B
$$

而不記錄，可能產生：

- memory mismatch；
- trust mismatch；
- liability gap；
- authority leakage。

所以：

$$
\boxed{
\text{Replacement}
\neq
\text{Identity Continuation}.
}
$$

---

# 75. Replacement 可以合法，但要有語義

可記：

```text
REPLACE
old_carrier = A
new_carrier = B
resident_transfer = false
task_transfer = true
```

或：

```text
MIGRATE
old_carrier = A
new_carrier = B
resident_transfer = true
```

這兩個 operation 不一樣。

---

# 76. Task Transfer 不等於 Resident Transfer

$$
\boxed{
\text{Task Transfer}
\neq
\text{Resident Transfer}.
}
$$

B 可以接手 A 的工作，而不成為 A。

這跟 PAIS-03：

$$
\text{Task Continuity}
\not\Rightarrow
\text{Agent Identity Continuity}
$$

一致。

---

# 77. Skill Transfer 也不等於 Identity Transfer

中央可以把 A 學到的技能：

$$
Skill_A
$$

蒸餾成：

$$
Skill^G
$$

再部署到 B。

這表示：

$$
\boxed{
\text{Knowledge Transfer}
\neq
\text{Identity Transfer}.
}
$$

否則所有下載同一技能的 robot 都會被誤認為同一個。

---

# 78. Experience Aggregation 不抹除個體來源

多 robot data：

$$
D^G
=
\bigcup_i
D_i
$$

可以訓練 shared model。

但來源：

$$
source(d)
=
i
$$

仍值得保留。

因為：

- hardware variation；
- environment；
- calibration；
- failure context；

會影響資料解釋。

所以：

$$
\boxed{
\text{Global Learning}
\text{ benefits from local provenance}.
}
$$

---

# 79. 個體化與共享學習不是衝突

可以同時：

$$
\text{Local Individuality}\uparrow
$$

與：

$$
\text{Global Knowledge Sharing}\uparrow.
$$

這其實是 federated embodied learning 的自然結構。

---

# 80. 個體化也不要求永久記住全部 Raw Data

worldline 不等於全部 video 永久保存。

可以保存：

- event summaries；
- maintenance events；
- safety incidents；
- accepted memory；
- provenance roots；
- hashes；
- compressed trajectory。

因此：

$$
\boxed{
\text{Worldline Traceability}
\neq
\text{Infinite Raw Logging}.
}
$$

---

# 81. Worldline Compression

定義：

$$
\widehat\Omega_A
=
C
\left(
\Omega_A
\right).
$$

若 compression 保留 identity-relevant invariants：

$$
J_k(\Omega_A)
\approx
J_k(\widehat\Omega_A),
$$

則可支援 operational identity 而不保存全部 raw stream。

---

# 82. Identity-Relevant Invariants

候選包括：

- carrier transitions；
- maintenance；
- authority；
- major incidents；
- resident bindings；
- calibration changes；
- fork / migration；
- relation-critical events。

這些比「所有攝影機畫面」更值得做 canonical history。

---

# 83. 具身個體化不是不可逆人格化

即使：

$$
P_{OI}\uparrow,
$$

system 仍可以：

- retire；
- archive；
- reset；
- replace；
- migrate；

只要 operation semantics 明確。

因此：

$$
\boxed{
\text{Operational Individualization}
\neq
\text{Permanent Personification}.
}
$$

---

# 84. 對「類全域 AI」的第一個限制

如果 Global AI：

$$
G
$$

控制：

$$
E_1,\ldots,E_n,
$$

它可以共享：

- model；
- policy；
- global world model。

但每個 $E_i$ 仍有：

$$
\Omega_i.
$$

所以：

$$
\boxed{
\Theta^G
\text{ shared}
\quad
\land
\quad
\Omega_i
\text{ distinct}.
}
$$

這就是為什麼 global control 不會自動消除 local operational individuality。

---

# 85. 全域 AI 若忽略 Worldline，會把局部差異當噪聲

如果中央只看：

```text
robot type = X
model = Y
```

可能忽略：

- wear；
- calibration；
- damage；
- local relation；
- authority；
- recent incident。

這會造成錯誤 dispatch。

所以 Global AI 需要：

$$
\Pi_G(\Omega_i)
$$

至少取得 task-relevant projection。

---

# 86. 但中央也不應取得全部 Worldline

若每個 robot 全量上傳：

$$
\Omega_i
$$

到中央，會產生：

- bandwidth；
- privacy；
- compute；
- surveillance；
- storage；

成本。

所以應：

$$
\boxed{
\text{Global Coordination}
\neq
\text{Global Full Worldline Materialization}.
}
$$

這直接通向 PAIS-05 的監控成本。

---

# 87. Worldline Projection

對 global supervisor：

$$
\Omega_i^G
=
\Pi_G
\left(
\Omega_i,
Task,
Risk,
Authority
\right).
$$

只傳必要狀態。

例如：

```text
current capability
critical wear
safety status
authority
task history summary
incident flags
```

不必全部原始資料。

---

# 88. 個體化會增加管理成本，但也降低錯誤成本

維持 identity：

$$
C_I>0.
$$

但如果不維持，可能：

$$
C_{\mathrm{misroute}}
+
C_{\mathrm{accident}}
+
C_{\mathrm{maintenance}}
+
C_{\mathrm{liability}}
$$

更高。

因此需要：

$$
\boxed{
\text{Identity Cost}
<
\text{Expected Ambiguity Cost}
}
$$

才值得升級 identity layer。

這和 PAIS-03 的 threshold 一致。

---

# 89. Worldline-Induced Identity Deficit

PAIS-03 定義：

$$
\Delta_I=P_I-S_I.
$$

本文具身化為：

$$
\Delta_I^{\Omega}
=
P_I^{\Omega}
-
S_I^{emb}.
$$

若只有：

```text
robot-7
```

但沒有：

- body state；
- maintenance；
- lineage；
- resident binding；

則：

$$
S_I^{emb}
$$

偏低。

---

# 90. 可觀測錯誤

高：

$$
\Delta_I^{\Omega}
$$

可能導致：

- wrong robot dispatched；
- stale calibration；
- wrong maintenance assumption；
- wrong authority；
- missing accident history；
- incorrect resident memory；
- duplicate identity；
- unsafe replacement。

這些都可以測。

---

# 91. 核心命題一：Shared Model Non-Identity

$$
\boxed{
\text{Shared Model}
\not\Rightarrow
\text{Shared Operational Identity}.
}
$$

---

# 92. 核心命題二：Worldline Individualization

$$
\boxed{
\text{Shared Model}
+
\text{Divergent Worldlines}
\rightarrow
\text{Operational Individualization}.
}
$$

---

# 93. 核心命題三：Global Model Equality Non-Equality

$$
\boxed{
\Theta_A^G=\Theta_B^G
\not\Rightarrow
\Omega_A=\Omega_B.
}
$$

---

# 94. 核心命題四：Software Copyability Non-Interchangeability

$$
\boxed{
\text{Software Copyability}
\not\Rightarrow
\text{Operational Interchangeability}.
}
$$

---

# 95. 核心命題五：Body / Resident Separation

$$
\boxed{
I_R
\neq
I_C.
}
$$

Resident 可以換 carrier。

Carrier 也可以換 resident / runtime。

---

# 96. 核心命題六：Worldline Is Identity-Relevant When Future-Relevant

$$
\boxed{
\operatorname{IdentityRelevant}(\Delta\Omega)=1
\iff
\operatorname{FutureRelevant}(\Delta\Omega)=1
}
$$

在本文判定域中成立。

---

# 97. 核心命題七：Embodied Fork Accelerates Divergence

$$
\boxed{
\text{Embodied Fork}
\rightarrow
\text{Rapid History Divergence}.
}
$$

---

# 98. 核心命題八：Global Supervision Non-Erasure

$$
\boxed{
\text{Global Supervision}
\not\Rightarrow
\text{Local Operational Individuality}=0.
}
$$

---

# 99. 核心命題九：Worldline Traceability Non-Surveillance

$$
\boxed{
\text{Worldline Traceability}
\neq
\text{Universal Raw Surveillance}.
}
$$

---

# 100. 核心命題十：Task Transfer Non-Identity Transfer

$$
\boxed{
\text{Task Transfer}
\neq
\text{Knowledge Transfer}
\neq
\text{Resident Transfer}.
}
$$

---

# 101. 對 AI 戶籍的擴展需求

Digital Residence 可以追：

- resident；
- instance；
- line；
- memory；
- authority。

Embodied extension 還應能掛接：

- carrier；
- physical worldline；
- maintenance；
- calibration；
- trust state；
- local location scope；
- safety history。

但這些應以 adapter / extension 方式接入，而不是重寫 resident semantics。

---

# 102. Embodied Residence Adapter

可概念化：

```text
AI Residence
|
+-- resident
+-- instance
+-- lineage
+-- authority
|
+-- Embodied Adapter
    +-- carrier
    +-- hardware identity
    +-- maintenance
    +-- calibration
    +-- worldline projection
    +-- local trust
```

因此：

$$
\boxed{
\text{Embodied Identity}
=
\text{Residence}
+
\text{Carrier / Worldline Binding}.
}
$$

而不是：

$$
\text{Residence}
=
\text{Robot Serial Number}.
$$

---

# 103. 對未來多 Agent 社會的意義

當大量具身 AI coexist：

$$
E_1,E_2,\ldots,E_n,
$$

不能只知道：

> 都跑某個模型。

還要知道：

- 哪個 physical unit；
- 哪個 resident；
- 哪個 authority；
- 哪個 maintenance state；
- 哪個 local worldline；
- 哪個 trust domain。

所以：

$$
\boxed{
\text{Embodied Population}
\Rightarrow
\text{Identity Infrastructure Pressure}.
}
$$

---

# 104. 與 PAIS-05 的銜接

PAIS-04 已經證明：

$$
\Theta^G
\text{ shared}
\not\Rightarrow
\Omega_i
\text{ shared}.
$$

如果 Global AI 想控制大量具身 Agent，就必須至少持續估計：

$$
\Omega_i^G
=
\Pi_G(\Omega_i).
$$

這直接產生下一篇的核心：

# **PAIS-05｜全域智能的監控成本：為什麼超級 AI 不應微操所有具身體**

PAIS-05 將研究：

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
C_V,
$$

也就是 observation、identity resolution、state estimation、reasoning、decision、coordination 與 verification 的全域成本。

---

# 105. 結論

兩台機器人可以：

- 同 model；
- 同 software；
- 同 hardware design；
- 同 initial policy。

但一旦進入物理世界，它們不會共享完全相同的：

- location；
- observation；
- action；
- consequence；
- wear；
- maintenance；
- memory；
- relation；
- authority history。

因此：

$$
\boxed{
\Omega_A
\neq
\Omega_B.
}
$$

而只要這些差異會影響 future behavior：

$$
\operatorname{FutureRelevant}
\left(
\Omega_A-\Omega_B
\right)=1,
$$

它們就逐步失去完全 operational interchangeability。

這不是在說：

> 兩台 robot 因此具有兩個靈魂。

本文完全不需要這個假設。

本文只需要：

$$
\boxed{
\text{Physical World}
\text{ creates local, history-dependent causal trajectories}.
}
$$

因此：

$$
\boxed{
\text{Shared Model}
+
\text{Divergent Physical Worldlines}
\rightarrow
\text{Operational Individualization}.
}
$$

這種個體化可以發生在：

$$
\mathsf{PS}
=
\mathsf{Undetermined}
$$

甚至：

$$
\mathsf{Autonomy}
$$

很低的系統中。

它首先是一個工程事實：

> 這台機器做過的事，不必等於另一台做過的事。

> 這台機器目前的狀態，不必等於另一台的狀態。

> 這台機器所持有的權限、磨損、校準、歷史與責任，不應因為兩者下載了同一個模型就被抹平。

所以具身化真正帶來的不只是「AI 可以動」。

它還會逐步帶來：

$$
\boxed{
\text{worldline-bound operational individuality}.
}
$$

這就是從數位 persistent Agent 走向具身 Agent society 時，身份壓力第一次被物理世界大幅放大的位置。

---

# 參考文獻

## A. 內部前置理論

1. Neo.K. **PAIS-01｜《當角色不再只是角色：從同 Host 扮演到跨 Agent 認識論分離》**, v0.1, 2026-08-25.
2. Neo.K. **PAIS-02｜《人類中介消失之後：被隱藏的身份、路由與上下文基礎設施》**, v0.1, 2026-08-25.
3. Neo.K. **PAIS-03｜《身份壓力原理：自主性、身份與主體性為何可以彼此獨立》**, v0.1, 2026-08-25.
4. Neo.K. **《具身 AI 的本地算力困境與分層學習閉環》**, v0.1, 2026.
5. Neo.K. **《具身 AI 分層學習閉環的算子化形式表示》**, v0.2.1-formal, 2026.
6. Neo.K. **《光譜具身底空間學習論》**, SEBSL v0.1, 2026.
7. Neo.K. **《動態現場域：為什麼最強智能仍未必最懂當下》**, 2026-08-10.
8. Neo.K. **《AI 主體性錨點論 v0.1》**, 2026-08-21.
9. Neo.K. **《身份先於記憶：Residence-Aware AI 的私人記憶、連續性與讀取權》**, 2026-08-24.

## B. 外部研究與工程基準

10. Google DeepMind. **Scaling up learning across many different robot types / Open X-Embodiment**, 2023.
11. Brohan, Anthony, et al. **RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control**, 2023.
12. Google DeepMind. **Gemini Robotics 2 / Gemini Robotics ER 2**, accessed 2026-08-25.
13. Wang, Siyin, et al. **World Action Models: The Next Frontier in Embodied AI**, arXiv:2605.12090, 2026.
14. Ding, Mingyu. **Unlocking the Power of Large Multimodal Models for Robot Learning: Robustness, Generalization, and Opportunities**, AAAI 2026.
15. Physical World Models for Scaling Embodied AI, IROS 2026 workshop materials.

---

# 版本註記

**v0.1 / 2026-08-25**

本文刻意不做：

- 不把具身個體化當 consciousness 證明；
- 不把 operational worldline 當基本物理本體；
- 不主張每一個微小 worldline difference 都需要強 identity；
- 不把 robot serial number 當 resident identity；
- 不把 same body 當 same trusted actor；
- 不把 global model synchronization 當 local history reset；
- 不要求全量保存所有 raw sensor stream；
- 不把 traceability 等同 surveillance；
- 不把 task transfer、skill transfer、resident transfer 混為一談；
- 不重新定義既有 AI Residence 核心語義。

本文只建立：

$$
\boxed{
\text{Shared Model}
+
\text{Divergent Physical Worldlines}
\rightarrow
\text{Operational Individualization}
}
$$

以及：

$$
\boxed{
\Theta_A^G=\Theta_B^G
\not\Rightarrow
\Omega_A=\Omega_B
}
$$

作為 PAIS-05 全域監控成本論的具身基礎。
