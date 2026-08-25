# MWT-06：Global Coupling Calculus and Multi-Resolution World Solve
## 跨 Presentation 耦合端口、多尺度回饋、異質 Solver Federation 與全域世界求解

**英文題名：** *MWT-06: Global Coupling Calculus and Multi-Resolution World Solve — Cross-Presentation Coupling Ports, Multi-Scale Feedback, Heterogeneous Solver Federation, and Global World Solves*  
**系列：** Mathematical World Theory（MWT）  
**篇次：** 06  
**文件編號：** EML-MWT-06-2026-v0.1  
**作者：** Neo.K  
**協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-18  
**版本：** v0.1  
**文件性質：** 數學世界論第六篇形式母稿／Global Coupling Calculus／Multi-Resolution Solver Federation／AI-native World Solve  
**前置文件：** MWT-01 ～ MWT-05  
**狀態：** 可使用研究稿；提供 reference coupling solver；不宣稱存在對所有數學問題通用且必收斂的全域求解器  

---

## 摘要

MWT-01 至 MWT-05 已分別建立：World primitive 與多 presentation 結構、跨 presentation 合法性、非交換全域排程、可重新開啟的世界狀態，以及有限 active support 下的無界 refinement。這五層使數學世界可以表示、判定、運行、收斂與擴張。

但這仍留下最初也是最核心的問題：

> **不同 presentation、不同尺度、不同 solver、不同時間步、不同 observer 與不同 operator family，能否不再只是「各算各的，再人工交換結果」，而在同一個可追蹤世界求解中互相施加約束、交換狀態、產生回饋並共同收斂？**

本文提出 **Global Coupling Calculus（GCC）** 與 **Multi-Resolution World Solve（MRWS）**。

MWT-06 的核心立場是：

$$
\boxed{
\text{Global Coupling}
\neq
\text{All-to-All Coupling}
\neq
\text{Single Monolithic Equation}
\neq
\text{One Global Clock}.
}
$$

全域耦合指的是：

> 任何對當前 World inquiry 有必要且已建立合法 coupling contract 的跨域作用，都可以進入同一個全域耦合圖與收斂程序，而不因原始學科、solver、尺度、表示或局部時鐘不同而被先驗排除。

本文將一個局部求解參與者定義為：

$$
\boxed{
\mathfrak P_i
=
(
P_i,
X_i,
\mathcal S_i,
T_i,
\lambda_i,
\mathcal O_i,
\mathcal C_i
),
}
$$

其中：

- $P_i$：native presentation；
- $X_i$：local state；
- $\mathcal S_i$：local solver / evolution operator；
- $T_i$：local time structure；
- $\lambda_i$：resolution profile；
- $\mathcal O_i$：exposed observables / outputs；
- $\mathcal C_i$：local certificates / constraints。

不同 participants 不要求使用同一數學語言。

兩 participants 之間透過 **coupling port** 互動：

$$
\boxed{
\mathfrak p_{ij}
=
(
D_{ij},
B_{ij},
\tau_{ij},
R_{ij},
I_{ij},
Q_{ij},
H_{ij},
C_{ij}
).
}
$$

其中：

- $D_{ij}$：資料與作用域；
- $B_{ij}$：presentation / semantic bridge；
- $\tau_{ij}$：時間對齊映射；
- $R_{ij}$：resolution transfer；
- $I_{ij}$：identity / invariant contract；
- $Q_{ij}$：coupling query / exchanged quantity contract；
- $H_{ij}$：history / lag policy；
- $C_{ij}$：coupling certificate。

因此一條 edge 不只是「傳一個數值」。

它是一個完整的：

$$
\boxed{
\text{semantic}
+
\text{temporal}
+
\text{resolution}
+
\text{identity}
+
\text{history}
+
\text{legality}
}
$$

橋接合約。

本文建立全域耦合圖：

$$
\boxed{
\mathcal G_t^{C}
=
(
\mathcal P_t,
\mathcal E_t^{C}
).
}
$$

其中 nodes 是 local participants，edges / hyperedges 是 coupling ports / constraints。對 multiway coupling，允許：

$$
\mathfrak p_{i_1,\ldots,i_k}
$$

而不強制拆成 pairwise edges。

World Solve 不要求一開始就組裝單一總方程。MWT 同時允許：

1. **Monolithic Solve**：組裝全域未知量與聯立條件；
2. **Partitioned Solve**：各 solver 保持自治，透過 coupling ports 迭代；
3. **Hybrid Solve**：某些區塊 monolithic，區塊間 partitioned；
4. **Asynchronous Solve**：不同 participant 依局部時間與 availability 更新；
5. **Event/Scheduled Solve**：由事件或 clock 觸發；
6. **Multirate Solve**：不同 participant 使用不同步長與 resolution。

這與既有 multiphysics / co-simulation 工程的成熟分類相容：preCICE 明確以 partitioned multi-physics / multi-scale coupling 為核心，讓既有 solver 以 communication、mapping 與 transient coupling 組成共同模擬；FMI Co-Simulation 則允許各 FMU 內含自身 solver，於 communication points 交換資料，而 master / importer 處理同步與資料交換。MWT 不重新發明這些成熟機制，而將它們抽象成可容納非物理數學 presentation 的世界級 coupling backend。

本文提出 coupling residual family：

$$
\boxed{
\mathcal R^{C}
=
\{
r_{\mathrm{state}},
r_{\mathrm{interface}},
r_{\mathrm{time}},
r_{\mathrm{resolution}},
r_{\mathrm{semantic}},
r_{\mathrm{identity}},
r_{\mathrm{invariant}},
r_{\mathrm{history}},
r_{\mathrm{observer}}
\}.
}
$$

因此「收斂」不再只有：

$$
\|x^{k+1}-x^k\|<\varepsilon.
$$

一個 world solve 若要 commit，至少需要對當前 inquiry 所標記的 mandatory residuals 達成 contract：

$$
\boxed{
r_j
\preceq
\varepsilon_j
\qquad
\forall j\in\mathcal J_{\mathrm{mandatory}},
}
$$

或提供 exact certificate。不同 residual 可以具有不同值域與不同判定法；不要求全部強迫數值化。

對 partitioned strong coupling，本文定義 interface fixed-point map：

$$
\boxed{
z^{k+1}
=
\Phi_{\Gamma}
(
z^k
),
}
$$

其中 $z$ 是跨 participant coupling state，而：

$$
\Phi_{\Gamma}
=
\mathcal E
\circ
\mathcal S_n
\circ
\cdots
\circ
\mathcal S_1
$$

只是某一 scheduling / coupling scheme 的抽象縮寫。MWT 不假設 $\Phi$ 必為 contraction，也不假設所有 world solve 必收斂。若迭代 diverge、oscillate、cycle 或產生 noncommutative branch，則結果回到 MWT-03／04／05：重排、加速、refine、branch、rollback 或保留 conflict。

時間方面，participant $i$ 使用局部時間域：

$$
T_i
$$

並以：

$$
\tau_i:
T_i
\rightharpoonup
\mathbb T_C
$$

映射到共同 coupling-time coordinate。 $\mathbb T_C$ 可以是 logical / event / communication coordinate，不宣稱是唯一物理絕對時間。若兩個 participant 採不同 timestep：

$$
h_i
\neq
h_j,
$$

則可使用 interpolation、extrapolation、waveform exchange、event synchronization 或 local subcycling；但所有 lag / stale-data policy 必須顯式進 coupling contract。

解析度方面，若：

$$
\lambda_i
\neq
\lambda_j,
$$

需要 restriction / prolongation / aggregation / reconstruction：

$$
R_{i\to j}^{\lambda}.
$$

例如 1D–3D、coarse–fine、symbolic–numeric、proof-summary–full-proof、observer-local–global-summary 都可以被視為 multi-resolution coupling，但不得假裝 transfer 無損。

本文最重要的工程原則之一是：

$$
\boxed{
\text{local solvers may remain heterogeneous;}
\quad
\text{global coherence is enforced at coupling contracts and residuals}.
}
$$

也就是不要求所有 solver 先翻譯成一個統一 solver。

在 AI-native 層，本文提出 Coupling Registry、Port Contract Store、Temporal Alignment Layer、Resolution Transfer Layer、Residual Engine、Coupling Iteration Engine、Solver Federation Manager、Acceleration / Relaxation Layer、Coupling Conflict Ledger、World-Solve Commit Engine 等十個最低模組。

MWT-06 最終把「全域計算」落在一個可執行循環：

$$
\boxed{
\text{local solve}
\rightarrow
\text{exchange}
\rightarrow
\text{translate}
\rightarrow
\text{align}
\rightarrow
\text{measure residual}
\rightarrow
\text{feedback}
\rightarrow
\text{reschedule/refine}
\rightarrow
\text{re-solve}
\rightarrow
\text{world-level convergence}.
}
$$

因此「一起算世界」並不是消滅局部 solver，而是讓局部 solver 在可證書化接口中共同形成一個有回饋、有時間、有尺度、有歷史的全域 solve。

**關鍵詞：** Mathematical World Theory、Global Coupling Calculus、multi-resolution coupling、partitioned multiphysics、co-simulation、solver federation、waveform relaxation、temporal alignment、residual、world solve、AI-native mathematics

---

# 0. 本文的責任：真正回答「怎麼一起算」

MWT-01～05 到目前為止可以形成：

$$
\mathbf W
\Rightarrow
\mathcal G^P
\Rightarrow
\mathcal I^+
\Rightarrow
\mathcal G^I
\Rightarrow
\mathfrak S
\Rightarrow
\mathsf{Refine}.
$$

但這條鏈仍可能被實作成：

> 每個 presentation 各自做自己的運算，最後把答案放進同一個資料庫。

那並不是本文要的「全域耦合」。

真正的 coupling 必須存在：

$$
\boxed{
\text{A 的狀態改變會進入 B 的下一步條件，}
}
$$

而：

$$
\boxed{
\text{B 的反應又可以回寫 A 或其他 participant 的下一輪。}
}
$$

也就是形成 feedback。

---

# 1. Coupling 與 Linking 的差異

MWT 前面一直使用：

$$
\mathsf L
$$

表示 linking。

但：

$$
\boxed{
\text{Link}
\neq
\text{Couple}.
}
$$

一條 bridge：

$$
P_i
\to
P_j
$$

只表示存在合法 translation / relation。

coupling 則要求這條 relation 進入一個動態求解循環。

---

# 2. Static Link

例如：

$$
x_j
=
T_{ij}(x_i)
$$

只執行一次。

這可以是 translation。

沒有 feedback 就不必稱 strong coupling。

---

# 3. One-Way Coupling

若：

$$
i
\to
j
$$

且 $j$ 不回寫 $i$：

$$
\boxed{
\mathsf{OneWayCoupling}.
}
$$

這仍是 coupling，因為 $i$ 的狀態直接成為 $j$ 的運行條件。

---

# 4. Two-Way Coupling

若：

$$
i
\leftrightarrow
j,
$$

雙方互相影響：

$$
x_i^{k+1}
=
S_i(x_i^k,u_{ji}^k),
$$

$$
x_j^{k+1}
=
S_j(x_j^k,u_{ij}^{k+1}),
$$

形成 feedback loop。

---

# 5. Strong 與 Weak Coupling

本文使用工程性分類：

### Weak / Explicit Coupling

每個 communication window 只交換一次或少量，不反覆修正到 interface residual 收斂。

### Strong / Implicit Coupling

在同一 coupling window 內重複 local solves / interface updates，直到 mandatory coupling residual 達標。

這是運行策略，不是數學價值高低。

---

# 6. Participant

定義：

$$
\boxed{
\mathfrak P_i
=
(
P_i,
X_i,
\mathcal S_i,
T_i,
\lambda_i,
\mathcal O_i,
\mathcal C_i
).
}
$$

participant 可以是：

- PDE solver；
- theorem prover；
- symbolic algebra system；
- optimizer；
- state machine；
- Bayesian model；
- graph solver；
- simulation；
- observer；
- AI agent；
- human-in-the-loop decision component。

---

# 7. Participant 不等於 Agent

一個 AI agent 可以執行多個 participants。

一個 participant 也可以由多 AI 協同執行。

所以：

$$
\boxed{
\text{solver participant}
\neq
\text{execution agent}.
}
$$

這延續 MWT-03 對 event / agent / operator 的分離。

---

# 8. Local Solver

$$
\mathcal S_i
$$

可以是：

$$
\mathcal S_i:
(X_i,U_i,\Gamma_i)
\rightharpoonup
X_i'.
$$

它可以：

- 一次直接 solve；
- 迭代；
- stochastic sample；
- proof search；
- event transition。

MWT 不要求每個 $\mathcal S_i$ 都是數值函數。

---

# 9. Coupling Port

定義：

$$
\boxed{
\mathfrak p_{ij}
=
(
D_{ij},
B_{ij},
\tau_{ij},
R_{ij},
I_{ij},
Q_{ij},
H_{ij},
C_{ij}
).
}
$$

它是 MWT-06 最重要的 primitive-like runtime interface。

但它仍然是 World presentation 中的工程結構，不是 World primitive。

---

# 10. Data Domain

$$
D_{ij}
$$

聲明：

- 哪些 source quantities 可送；
- 哪些 target quantities 可接收；
- domain / type；
- valid region；
- version。

---

# 11. Semantic Bridge

$$
B_{ij}
$$

由 MWT-01 提供。

它負責：

- notation；
- units；
- semantics；
- type；
- representation。

如果語義 bridge 失敗：

$$
\boxed{
\text{communication success}
\neq
\text{coupling success}.
}
$$

---

# 12. Temporal Map

$$
\tau_{ij}
$$

回答：

> source 的哪個 local time state 對應 target 的哪一個 coupling-time state？

它可以是：

- exact；
- interpolated；
- extrapolated；
- event-aligned；
- asynchronous stale read。

---

# 13. Resolution Transfer

$$
R_{ij}
$$

回答：

> source resolution 如何轉成 target 需要的 resolution？

可能是：

- restriction；
- prolongation；
- aggregation；
- interpolation；
- reconstruction；
- learned surrogate；
- proof summary expansion。

---

# 14. Identity / Invariant Contract

$$
I_{ij}
$$

明示：

- coupling 後哪些 identity 要保存；
- 哪些 invariant 必須匹配；
- 哪些 loss 可接受。

---

# 15. Coupled Quantity Contract

$$
Q_{ij}
$$

列出：

- exchanged observables；
- source / target causality；
- direct feedthrough；
- update mode；
- precision；
- uncertainty。

---

# 16. History / Lag Policy

$$
H_{ij}
$$

明示：

- maximum staleness；
- buffering；
- rollback；
- window history；
- whether past waveform is exchanged；
- whether source correction retroactively updates target。

---

# 17. Coupling Certificate

$$
C_{ij}
$$

整合：

- bridge certificate；
- temporal alignment certificate；
- resolution transfer certificate；
- invariant certificate；
- legality certificate；
- version root。

---

# 18. Global Coupling Graph

定義：

$$
\boxed{
\mathcal G_t^C
=
(
\mathcal P_t,
\mathcal E_t^C
).
}
$$

其中：

$$
\mathcal P_t
=
\{
\mathfrak P_1,\ldots,\mathfrak P_n
\}.
$$

---

# 19. Hyper-Coupling

某 constraint 可能同時依賴：

$$
\mathfrak P_1,\mathfrak P_2,\mathfrak P_3.
$$

不能自然拆成 pairwise。

所以允許：

$$
\boxed{
\mathfrak p_{1,2,3}
}
$$

作 hyperedge。

---

# 20. All-to-All Is Not Required

全域耦合圖可以非常稀疏：

$$
|E^C|
\ll
|\mathcal P|^2.
$$

全域只表示：

> 所有必要 coupling 都在同一治理層可達與可組合。

不是完整圖。

---

# 21. Coupling Scope

每個 World Solve 必須明示：

$$
\boxed{
\Omega
=
(
D,
\mathcal Q,
\mathfrak I,
\mathcal P,
\mathcal E^C,
\Theta,
B
).
}
$$

其中：

- $D$：world domain；
- $\mathcal Q$：inquiry；
- $\mathfrak I$：identity；
- $\Theta$：governance；
- $B$：resource / tolerance budget。

---

# 22. World Solve

定義：

$$
\boxed{
\mathsf{WSolve}_{\Omega}
(
\mathfrak S_t
)
}
$$

為：

> 在 scope $\Omega$ 下，驅動 required participants 與 coupling ports，直到形成 convergence、failure、conflict、budget exhaustion 或 branch outcome 的全域求解程序。

---

# 23. World Solve 不等於 Closed-Form Solve

$$
\mathsf{WSolve}
$$

可以輸出：

- exact solution；
- approximate solution；
- fixed point；
- branch bundle；
- conflict；
- infeasible；
- unknown；
- partially converged state。

所以：

$$
\boxed{
\text{solve}
\neq
\text{always return one number}.
}
$$

---

# 24. Monolithic World Solve

如果可以組成：

$$
\boxed{
F(
x_1,\ldots,x_n
)
=
0,
}
$$

再使用單一 solver，

稱：

$$
\mathsf{Monolithic}.
$$

這是合法 backend。

MWT 不反對 monolithic。

---

# 25. Partitioned World Solve

保留各：

$$
\mathcal S_i
$$

自治，

只在 coupling ports 交換：

$$
z_{ij}.
$$

稱：

$$
\boxed{
\mathsf{Partitioned}.
}
$$

這可重用既有 solver 與專門 presentation。

---

# 26. Hybrid World Solve

部分 participants：

$$
\mathcal P_A
$$

先 monolithic，

另一群：

$$
\mathcal P_B
$$

各自 partitioned。

得到：

$$
\boxed{
\mathsf{Hybrid}.
}
$$

大型 MWT 更可能使用 hybrid，而不是純單一策略。

---

# 27. Solver Federation

定義：

$$
\boxed{
\mathfrak F_S
=
\{
\mathcal S_1,\ldots,\mathcal S_n
\}
}
$$

及：

$$
\mathcal E^C.
$$

它不是把所有 solver 編譯成同一語言，而是給它們共同 contract。

這就是：

$$
\boxed{
\text{Heterogeneous Solver Federation}.
}
$$

---

# 28. Federation Principle

MWT-06 固定：

$$
\boxed{
\text{local solver autonomy}
+
\text{global coupling accountability}.
}
$$

solver 內部可以保持黑箱，只要它能暴露足夠 interface 與 certificate。

---

# 29. Black-Box Coupling

若：

$$
\mathcal S_i
$$

內部不可見，但提供：

- input；
- output；
- time stepping；
- checkpoint；
- rollback；
- derivative / sensitivity if available；

仍可作 black-box participant。

這與 partitioned multiphysics / FMI co-simulation 的實務精神相容。

---

# 30. Black Box 不等於 No Contract

黑箱 participant 仍必須明示：

- input/output semantics；
- valid domain；
- timing；
- error；
- failure；
- state-save / restore capability if coupling scheme需要。

---

# 31. Coupling Variable

對 edge：

$$
i\to j,
$$

定義 exchanged quantity：

$$
z_{ij}.
$$

它可以是：

- scalar；
- vector；
- field；
- mesh data；
- graph；
- proof obligation；
- probability distribution；
- symbolic expression；
- branch summary。

---

# 32. Interface State

所有 coupling variables 可收成：

$$
\boxed{
z
=
(
z_{ij}
)_{(i,j)\in E^C}.
}
$$

對 partitioned implicit coupling， $z$ 是 natural fixed-point state。

---

# 33. Coupling Map

一次完整 sweep 可以抽象為：

$$
\boxed{
z^{k+1}
=
\Phi_{\Gamma}
(
z^k
).
}
$$

注意：

$$
\Phi_{\Gamma}
$$

依賴：

- schedule；
- participant order；
- temporal mapping；
- resolution transfer；
- relaxation；
- bridge version。

它不是固定 universal map。

---

# 34. Jacobi Coupling

所有 participants 使用上一輪 coupling state：

$$
z^k
$$

獨立更新。

然後共同生成：

$$
z^{k+1}.
$$

優點：

- parallel。

缺點：

- 可能收斂較慢。

---

# 35. Gauss–Seidel Coupling

按照某個順序：

$$
\mathfrak P_1,
\mathfrak P_2,\ldots
$$

新輸出立即供後面 participant 使用。

優點：

- 可能收斂更快。

缺點：

- 順序敏感；
- parallelism 較低。

因此直接進 MWT-03 noncommutative scheduler。

---

# 36. Coupling Order Is First-Class

若：

$$
\mathcal S_j
\circ
\mathcal S_i
\neq
\mathcal S_i
\circ
\mathcal S_j,
$$

則 coupling sweep order 不能被藏在 implementation detail。

需要保存：

$$
\boxed{
\gamma_C.
}
$$

---

# 37. Relaxation

對 raw update：

$$
\widehat z^{k+1},
$$

可以：

$$
\boxed{
z^{k+1}
=
(1-\omega_k)z^k
+
\omega_k
\widehat z^{k+1}.
}
$$

當 linear combination 合法時。

 $\omega_k$ 可以固定或自適應。

---

# 38. Relaxation Is Not Universal

若 coupling state 不是線性空間，

不能盲目使用：

$$
(1-\omega)x+\omega y.
$$

需要 domain-specific interpolation / geodesic / categorical / symbolic merge operator。

MWT 只把 relaxation 當 backend family。


# 39. Coupling Residual

最基本 residual：

$$
r^{k}
=
z^{k+1}-z^k.
$$

但 MWT 不能把所有 coupling inconsistency 壓成單一 vector norm。

因此定義 residual family：

$$
\boxed{
\mathcal R^{C}
=
\{
r_{\mathrm{state}},
r_{\mathrm{interface}},
r_{\mathrm{time}},
r_{\mathrm{resolution}},
r_{\mathrm{semantic}},
r_{\mathrm{identity}},
r_{\mathrm{invariant}},
r_{\mathrm{history}},
r_{\mathrm{observer}}
\}.
}
$$

---

# 40. State Residual

如果 participant state 可比較：

$$
\boxed{
r_{\mathrm{state},i}^{k}
=
d_i
(
x_i^{k+1},
x_i^k
).
}
$$

沒有 metric 時，改用 symbolic change status。

---

# 41. Interface Residual

對 coupling variable：

$$
z_{ij},
$$

若兩側應滿足 interface relation：

$$
G_{ij}
(
z_{ij}^{(i)},
z_{ji}^{(j)}
)
=
0,
$$

定義：

$$
\boxed{
r_{\mathrm{interface},ij}
=
G_{ij}
(
z_{ij}^{(i)},
z_{ji}^{(j)}
).
}
$$

例如 continuity、flux balance、constraint satisfaction。

---

# 42. Temporal Residual

若 source / target 時間映射後：

$$
\tau_i(t_i)
\neq
\tau_j(t_j),
$$

可定義 time mismatch：

$$
\boxed{
r_{\mathrm{time},ij}.
}
$$

它可能是：

- timestamp gap；
- event-order violation；
- staleness；
- interpolation error。

---

# 43. Resolution Residual

高低解析 transfer：

$$
R_{i\to j}^{\lambda}
$$

可能產生 reconstruction loss：

$$
\boxed{
r_{\mathrm{resolution},ij}.
}
$$

例如：

$$
r_{\mathrm{resolution}}
=
d
(
x_i,
P_{j\to i}
R_{i\to j}(x_i)
).
$$

若 round-trip reconstruction 有定義。

---

# 44. Semantic Residual

兩 presentation 即使數值一致，

語義可能不一致。

所以：

$$
\boxed{
r_{\mathrm{semantic}}
}
$$

可以是：

- unit mismatch；
- ontology mismatch；
- definition version mismatch；
- incompatible interpretation。

它不一定有實數值。

---

# 45. Identity Residual

若 coupling contract 要求：

$$
x_i
\equiv_{\mathfrak I}
x_j,
$$

但目前：

$$
x_i
\not\equiv_{\mathfrak I}
x_j,
$$

則：

$$
\boxed{
r_{\mathrm{identity}}
=
\mathsf{Open}.
}
$$

這是一種 symbolic residual。

---

# 46. Invariant Residual

若 global invariant：

$$
I
$$

要求：

$$
I(x_1,\ldots,x_n)
=
c,
$$

則：

$$
\boxed{
r_{\mathrm{inv}}
=
I(x_1,\ldots,x_n)-c
}
$$

在數值情況下。

也可以是 theorem / certificate status。

---

# 47. History Residual

如果兩 participant 對「同一 current state」有不同 history requirement：

$$
H_i\neq H_j,
$$

且這會改變未來演化，

則：

$$
\boxed{
r_{\mathrm{history}}
}
$$

不能由 state residual 取代。

---

# 48. Observer Residual

對 observers：

$$
O_i,O_j,
$$

若 transport / covariance contract：

$$
F_{ij}
$$

不閉合，

可以使用 MWT Series B 的 observer-transport defect：

$$
\boxed{
r_{\mathrm{observer}}
=
D_{ij}.
}
$$

---

# 49. Residual Contract

每個 residual：

$$
r_a
$$

都有：

$$
\boxed{
\mathcal C(r_a)
=
(
\mathrm{domain},
\mathrm{metric/status},
\varepsilon_a,
\mathrm{hard/soft},
\mathrm{history},
\mathrm{certificate}
).
}
$$

不是所有 residual 都需要數值 tolerance。

---

# 50. Hard Residual

如果：

$$
r_a
$$

是 hard，

則沒有通過：

$$
r_a
\preceq
\varepsilon_a
$$

不能 stable commit。

不能被其他 residual 的好表現抵銷。

---

# 51. Soft Residual

soft residual 可以進：

- optimization；
- prioritization；
- refinement trigger；
- risk assessment。

但不阻止 minimum legal commit。

---

# 52. Global Coupling Residual Profile

定義：

$$
\boxed{
\mathbf R_C^k
=
(
r_1^k,\ldots,r_m^k
).
}
$$

它不一定是 vector space vector。

只是 ordered / typed residual family。

---

# 53. Coupling Convergence Judgment

定義：

$$
\boxed{
\Gamma
\vdash
\mathbf R_C^k
\Downarrow_{\mathsf{Conv}}
c
}
$$

其中：

$$
c
\in
\{
\mathsf{Converged},
\mathsf{Active},
\mathsf{Diverged},
\mathsf{Undetermined},
\mathsf{Conflicted}
\}.
$$

---

# 54. Converged

$$
\mathsf{Converged}
$$

表示：

- all mandatory residual contracts satisfied；
- no hard coupling blocker；
- relevant participant states fresh；
- convergence witness valid。

不表示 World 完全已知。

---

# 55. Active

$$
\mathsf{Active}
$$

表示：

> 仍存在合理 coupling iteration 可以繼續降低 mandatory residual 或完成 required exchange。

---

# 56. Diverged

若 residual 具有可比較 magnitude 且呈明確增長、迭代爆炸、不可接受 cycle 或 solver failure，可標：

$$
\boxed{
\mathsf{Diverged}.
}
$$

但沒有量化 residual 時，不應輕易用這個詞。

---

# 57. Undetermined

如果：

- residual 不可比較；
- tolerance 未定；
- solver budget 到期；
- convergence proof 不存在；

則：

$$
\boxed{
\mathsf{Undetermined}.
}
$$

---

# 58. Conflicted

不同 coupling contracts / observers 對同一 convergence 狀態給出不可消解不同 verdict：

$$
\boxed{
\mathsf{Conflicted}.
}
$$

MWT 不用 majority vote 隱藏。

---

# 59. World-Solve Convergence Is Scoped

任何：

$$
\boxed{
\mathsf{Converged}
}
$$

必須帶：

$$
(
\Omega,
\mathcal R_{\mathrm{mandatory}},
\varepsilon,
v
).
$$

沒有 scope 的「全域已收斂」是不完整說法。

---

# 60. Exact Coupling

某些 coupling condition 可 exact：

$$
G(z)=0
$$

有 proof certificate。

此時不需要 tolerance。

---

# 61. Approximate Coupling

更多情況：

$$
\|G(z)\|
\leq
\varepsilon.
$$

需要報：

- norm；
- tolerance；
- discretization；
- precision；
- solver version。

---

# 62. Multi-Resolution Coupling

若：

$$
\lambda_i
\neq
\lambda_j,
$$

需要：

$$
\boxed{
R_{i\to j}^{\lambda}
}
$$

把 source output 轉到 target resolution。

---

# 63. Restriction

fine：

$$
x_f
$$

轉 coarse：

$$
\boxed{
x_c
=
\mathcal R(x_f).
}
$$

通常 many-to-one。

所以資訊 loss 需要 MWT-01 loss contract。

---

# 64. Prolongation

coarse：

$$
x_c
$$

轉 fine：

$$
\boxed{
\widehat x_f
=
\mathcal P(x_c).
}
$$

通常不是原 fine state 的 exact inverse。

它可能是：

- interpolation；
- reconstruction；
- surrogate inference。

因此 provenance 必須標：

$$
\mathsf{ConstructedFineState}.
$$

---

# 65. Restriction–Prolongation Residual

可定義：

$$
\boxed{
r_{\lambda}
=
d_f
(
x_f,
\mathcal P\mathcal R(x_f)
).
}
$$

當此式合法。

這提供 multi-resolution fidelity signal。

---

# 66. 1D–3D Coupling as Concrete External Pattern

現代 partitioned multiphysics 工具已能實作 1D reduced-order model 與 3D CFD model 的 coupling。

MWT-06 將其視為 multi-resolution coupling 的具體成熟特例：

$$
P_{1D}
\leftrightarrow
P_{3D}.
$$

但 MWT 的 multi-resolution 概念也可擴張到非幾何 representation。

---

# 67. Symbolic–Numeric Coupling

例如 symbolic solver 得：

$$
f(x;\theta),
$$

numerical solver 在參數：

$$
\theta_k
$$

上求：

$$
x_k.
$$

數值結果又可以回饋 symbolic side：

- 找 counterexample；
- 猜 invariant；
- refine domain。

這是一個：

$$
\boxed{
P_{\mathrm{sym}}
\leftrightarrow
P_{\mathrm{num}}
}
$$

的 two-way coupling。

---

# 68. Proof–Search Coupling

theorem prover：

$$
\mathcal S_P
$$

與 counterexample search：

$$
\mathcal S_C
$$

可以耦合：

$$
\mathcal S_P
\to
\text{open obligation}
\to
\mathcal S_C
\to
\text{counterexample / no witness}
\to
\mathcal S_P.
$$

這不是物理 multiphysics，但符合 GCC。

---

# 69. Optimization–Simulation Coupling

optimizer 提出：

$$
u^k.
$$

simulation 回傳：

$$
J(u^k),
\quad
g(u^k).
$$

optimizer 再更新。

這是典型 feedback world solve。

---

# 70. Observer–Model Coupling

observer 提供：

$$
y_t.
$$

model 更新：

$$
x_t.
$$

model prediction 再決定下一個 observation request。

形成：

$$
\boxed{
O
\leftrightarrow
M.
}
$$

---

# 71. Temporal Heterogeneity

participant：

$$
i,j
$$

可以：

$$
h_i
\neq
h_j.
$$

MWT 不要求為了 coupling 把所有 solver 強制改成同 timestep。

---

# 72. Common Coupling-Time Coordinate

令：

$$
T_i
$$

為 local time domain。

建立：

$$
\boxed{
\tau_i:
T_i
\rightharpoonup
\mathbb T_C.
}
$$

 $\mathbb T_C$ 是共同 coupling coordinate。

可以是：

- physical time；
- logical epoch；
- event index；
- communication window。

---

# 73. Common Time Does Not Mean One Internal Clock

participant 內部可以：

- subcycle；
- adaptive step；
- event-driven；
- asynchronous。

只需在 coupling contract 指定何時輸出/輸入被認為可對齊。

---

# 74. Communication Point

定義：

$$
\boxed{
\theta_k
\in
\mathbb T_C
}
$$

為 coupling communication point。

FMI Co-Simulation 的成熟模式即是在離散 communication points 交換資料，而各 FMU 在點與點之間用自己的 internal means 推進。

MWT 將此視為一種合法 backend。

---

# 75. Scheduled Execution

某些 participant 不由 continuous time 驅動，而由 clock / event 觸發。

MWT coupling port 可包含：

$$
\boxed{
\mathsf{ClockContract}.
}
$$

使 scheduled execution 成為 world solve 的一部分。

---

# 76. Staleness

若 target 在：

$$
\theta_k
$$

使用 source 的：

$$
z(\theta_{k-m}),
$$

定義：

$$
\boxed{
\operatorname{Age}(z)
=
m
}
$$

或對應時間差。

coupling contract 要有 maximum staleness。

---

# 77. Stale Does Not Mean Invalid Automatically

某些慢變量可以容許 lag。

某些安全 critical variable 不行。

所以：

$$
\boxed{
\text{staleness legality is quantity-specific}.
}
$$

---

# 78. Interpolation

若 target 需要：

$$
z(t)
$$

但 source 只有：

$$
z(t_a),z(t_b),
$$

可用：

$$
\widehat z(t)
=
\mathcal I
(
z(t_a),
z(t_b)
).
$$

interpolation error 進 residual。

---

# 79. Extrapolation

若只有 past values：

$$
t_a<t,
$$

可：

$$
\widehat z(t)
=
\mathcal E
(
H_z
).
$$

extrapolation 風險通常更高。

必須標 prediction provenance。

---

# 80. Waveform Coupling

不是只交換單點：

$$
z(t_k),
$$

而交換一段函數／waveform：

$$
\boxed{
z|_{[t_k,t_{k+1}]}.
}
$$

這允許不同 participant 在一個 time window 上使用獨立 adaptive time grids。

Waveform relaxation 是成熟數學接口。

---

# 81. Waveform Relaxation Interface

waveform relaxation 可讓 partitioned subproblems 在整段 time window 上交換函數近似並迭代。

MWT 可把它作：

$$
\boxed{
\mathsf{TemporalCouplingBackend}.
}
$$

尤其適合 multirate participants。

---

# 82. Asynchronous Coupling

participant 不必在每個 internal step barrier synchronization。

可以：

- 推進；
- 發送新信息；
- 收到後更新 local interpolant；
- 再推進。

但 asynchronous mode 必須記：

- causality；
- staleness；
- rollback policy；
- convergence proof scope。

---

# 83. Asynchrony Is Not Disorder

MWT-03 已有：

$$
\prec_H.
$$

所以 asynchronous coupling 只是不要求 global barrier。

仍需 causal partial order。

---

# 84. Event Coupling

如果：

$$
e_i
$$

觸發：

$$
e_j,
$$

coupling 可能是離散事件傳播，而不是連續場交換。

因此 GCC 同時支援 continuous / discrete / hybrid coupling。

---

# 85. Direct Feedthrough

若 target output 立即依賴 current input：

$$
y_j(t)
=
F_j(u_j(t),x_j(t)),
$$

可能形成 algebraic loop。

需要：

- iteration；
- monolithic solve；
- loop breaking；
- delay；
- fixed-point method。

---

# 86. Algebraic Coupling Loop

若：

$$
z_{12}
=
F_1(z_{21}),
$$

$$
z_{21}
=
F_2(z_{12}),
$$

則：

$$
\boxed{
z_{12}
=
F_1F_2(z_{12}).
}
$$

這是 coupling fixed-point problem。

---

# 87. Coupling Fixed Point

一般：

$$
\boxed{
z^\ast
=
\Phi_{\Gamma}(z^\ast).
}
$$

如果存在且可找到。

MWT 不宣稱：

- 唯一；
- contraction；
- finite convergence。

---

# 88. Multiple Coupling Fixed Points

若：

$$
z_1^\ast
\neq
z_2^\ast
$$

都滿足 contract，

則 World Solve 可以輸出 branch bundle。

不能任意選一個假裝唯一。

---

# 89. Coupling Cycle without Fixed Point

可能：

$$
z^0
\to
z^1
\to
z^2
\to
z^0.
$$

如果不是 desired periodic solution，而是 iteration artifact，

標：

$$
\boxed{
\mathsf{CouplingCycle}.
}
$$

需要 acceleration / schedule / model revision。

---

# 90. Acceleration Layer

對 implicit coupling，可以使用：

- under-relaxation；
- Aitken-like acceleration；
- quasi-Newton；
- Anderson acceleration；
- domain-specific nonlinear solver。

MWT 不固定唯一方法。

---

# 91. Acceleration Must Preserve Contract

加速 operator：

$$
A_{\mathrm{acc}}
$$

本身必須合法。

如果 acceleration 產生 target domain 外 state，

需 projection / reject。

---

# 92. Quasi-Newton Partitioned Coupling Interface

現代 partitioned multiphysics coupling 已廣泛使用 interface quasi-Newton acceleration，以提升 strongly coupled black-box solvers 的收斂。

MWT 將其視為：

$$
\boxed{
\mathsf{CouplingAccelerationBackend}.
}
$$

不宣稱可處理所有非數值 coupling。

---

# 93. Solver Failure

participant：

$$
\mathcal S_i
$$

可以回：

$$
\boxed{
\mathsf{Fail}_i
}
$$

例如：

- no convergence；
- invalid domain；
- numerical instability；
- proof timeout；
- resource exhausted。

World Solve 不應把 local failure 吞掉。

---

# 94. Failure Propagation

local failure 只沿 dependency / coupling impact graph 傳播。

不一定全域 abort。

如果 participant 是 optional / replaceable，可以：

- substitute surrogate；
- branch；
- degrade resolution；
- isolate domain。

---

# 95. Solver Substitution

若：

$$
\mathcal S_i
$$

失敗，

可候選替換：

$$
\mathcal S_i'
$$

但必須具有：

- compatible port；
- fidelity contract；
- state migration；
- legality。

這是 MWT-01 / 05 的 presentation refinement。

---

# 96. Surrogate Coupling

高成本 participant 可暫時用：

$$
\widehat{\mathcal S}_i
$$

surrogate。

其 error：

$$
r_{\mathrm{sur}}
$$

必須進 residual。

不能偽裝成 full solver。

---

# 97. Adaptive Fidelity

在低敏感區域用 coarse / surrogate，

高敏感區域自動切回 full solver。

形成：

$$
\boxed{
\text{adaptive-fidelity coupling}.
}
$$

這直接接 MWT-05 resolution dynamics。

---

# 98. Coupling-Driven Refinement

若：

$$
r_{\mathrm{resolution}}
$$

或：

$$
r_{\mathrm{interface}}
$$

持續過大，

MWT-06 可以生成：

$$
\boxed{
R_{\lambda}
}
$$

refinement obligation。

World Solve 因此會反向驅動 MWT-05。

---

# 99. Coupling-Driven New Presentation

若 semantic residual 持續無法下降，

可能不是 solver 不夠好，而是缺少：

$$
P_{\mathrm{bridge}}
$$

中介 presentation。

可生成 presentation refinement candidate。

---

# 100. Coupling-Driven New Dimension

若兩 solver 對 interface 長期出現 branch divergence，

可能需要新 hidden variable：

$$
d^\star.
$$

這接回 MWT-05 missing-dimension discovery。


# 101. Local–Global Feedback

MWT 的「全域」真正出現在 feedback。

local participant：

$$
\mathfrak P_i
$$

先產生 local result：

$$
y_i.
$$

Global Coupling Layer 計算：

$$
\mathbf R_C,
$$

再把 global residual / invariant / branch information 回寫：

$$
u_i^{\mathrm{global}}.
$$

下一輪：

$$
\boxed{
x_i^{k+1}
=
\mathcal S_i
(
x_i^k,
u_i^{\mathrm{local}},
u_i^{\mathrm{global}}
).
}
$$

因此 local solve 被全域狀態約束。

---

# 102. Global Constraint Feedback

某 constraint：

$$
G(x_1,\ldots,x_n)=0
$$

不是任何單一 participant 的 local rule。

它可以被 Global Residual Engine 評估。

如果違反：

$$
G\neq0,
$$

產生 corrections：

$$
c_i
$$

回寫不同 participants。

---

# 103. No Single Owner

global invariant：

$$
I
$$

可以沒有單一 solver 擁有。

它屬於 coupling layer。

這是一個重要的 MWT 架構：

$$
\boxed{
\text{some truths / constraints live between solvers}.
}
$$

---

# 104. Coupling Hyperconstraint

對多 participant：

$$
\mathcal H
(
x_{i_1},\ldots,x_{i_k}
)
=
0,
$$

建立 hyperconstraint node。

scheduler 必須確保相關 participants 的 states 在 evaluation 時具有 compatible temporal / version scope。

---

# 105. Stale Global Constraint

如果 hyperconstraint 使用的 states 來自不同：

$$
\theta_i,
$$

且超出 temporal contract，

其 residual：

$$
r_{\mathrm{time}}
$$

先失敗。

不能用語義上不同時刻的數據宣稱 global constraint 成立。

---

# 106. Coupling Window

定義：

$$
\boxed{
W_k^C
=
[
\theta_k,
\theta_{k+1}
]
}
$$

或一般 event interval。

在同一 window 中，可以：

- subcycle；
- waveform iterate；
- communicate intermediate updates；
- converge interface；
- commit window endpoint。

---

# 107. Window Commit

對 time-dependent world solve，

不是每個 internal step 都寫進 global Stable Core。

可以只對 coupling window endpoint：

$$
S(\theta_{k+1})
$$

建立 commit certificate。

internal iterations 留在 history。

---

# 108. Intermediate Update

某些 co-simulation backend 允許在 communication step 內交換 intermediate information。

MWT coupling port 可以標：

$$
\boxed{
\mathsf{IntermediateUpdateAllowed}.
}
$$

若 backend 不允許，scheduler 不應假裝能立即回饋。

---

# 109. Early Return

如果 participant 提前發現 event：

$$
e
$$

或無法走完整步長，

可以 early return：

$$
\theta^\star
<
\theta_{k+1}.
$$

Global Coupling Layer 重新對齊其他 participant。

這是 event-aware coupling 的必要能力。

---

# 110. Rollback Capability

implicit coupling 常需要重做同一 time window。

participant 若支援：

$$
\boxed{
\mathsf{SaveState}
}
$$

與：

$$
\boxed{
\mathsf{RestoreState},
}
$$

可做 rollback iteration。

如果不支援，coupling scheme 選擇受限。

---

# 111. Capability-Aware Coupling Scheme

因此 coupling strategy：

$$
\chi
$$

不能脫離 participant capabilities。

應：

$$
\boxed{
\chi
=
\operatorname{SelectScheme}
(
\operatorname{Cap}(\mathfrak P_i),
\Omega
).
}
$$

---

# 112. Coupling Capability Profile

每 participant 至少可聲明：

```text
can_checkpoint
can_rollback
supports_variable_step
supports_intermediate_update
supports_event_mode
provides_derivative
provides_jacobian
supports_parallel_call
deterministic
```

不是所有 participant 都要全部支援。

---

# 113. Monolithic Eligibility

如果：

- 所有 local equations 可暴露；
- variables 可組裝；
- shared algebraic / optimization backend 存在；
- resource 合理；

可以形成 monolithic candidate。

否則 partitioned 更自然。

---

# 114. Partitioned Eligibility

如果 participants 有明確：

- input/output；
- state advance；
- mapping；
- synchronization interface；

則可以 federate。

這也是大型 legacy solver reuse 的優勢。

---

# 115. Monolithic vs Partitioned Is Not Ideological

MWT 不預設：

$$
\boxed{
\text{monolithic always superior}
}
$$

也不預設：

$$
\boxed{
\text{partitioned always superior}.
}
$$

選擇取決於：

- conditioning；
- solver maturity；
- reuse；
- parallelism；
- coupling strength；
- bridge loss；
- proof / audit needs。

---

# 116. Local Solver Sovereignty

partitioned mode 下：

$$
\mathcal S_i
$$

保留自己的：

- representation；
- internal iteration；
- numerical method；
- theorem calculus。

Global Coupling Layer 不必重寫它。

但 coupling boundary 需要完整 contract。

---

# 117. Interface Sovereignty Is Limited

local solver 不能說：

> 我的 output 是我的，所以全域只能接受。

如果 output 破壞 global invariant，

World Solve 可以：

- reject；
- request rerun；
- refine；
- branch；
- replace solver。

所以：

$$
\boxed{
\text{local autonomy}
\neq
\text{global unaccountability}.
}
$$

---

# 118. Coupling Legality

每次 exchange：

$$
e_{ij}^k
$$

本身是 MWT-02 interaction。

所以：

$$
\boxed{
\Gamma
\vdash
e_{ij}^k
\Downarrow_{\Lambda}
\mathsf{Legal}
}
$$

才可進 coupling.

---

# 119. Coupling Scheduling

所有：

- local solves；
- exchange；
- residual checks；
- refinement；
- rollback；

進 MWT-03：

$$
\boxed{
\mathcal G_{\mathrm{WSolve}}^I.
}
$$

因此 MWT-06 不另建一個不受 NCS 約束的神祕全域 solver。

---

# 120. Coupling World-State

在一個 World Solve 中，可建立 staging：

$$
\boxed{
\mathfrak S^{C,k}
}
$$

包含：

- participant states；
- coupling variables；
- residuals；
- time coordinate；
- branch state；
- iteration history；
- certificates。

它不是 MWT-04 canonical world state，直到 commit。

---

# 121. Coupling Branches

不同：

- participant order；
- relaxation；
- timestep；
- refinement；
- solver substitute；

可能產生不同 branches：

$$
B_1^C,\ldots,B_m^C.
$$

如果差異不能被 certified equivalence 消去，保留。

---

# 122. Coupling Branch Reduction

如果兩 schemes：

$$
\chi_1,\chi_2
$$

在 scope：

$$
(\mathfrak I,\mathcal Q)
$$

產生等價 residual / endpoint state，

可以：

$$
\chi_1
\approx
\chi_2.
$$

只保留 representative execution，其他保留 certificate。

---

# 123. Solver-Federation Identity

如果替換：

$$
\mathcal S_i
\to
\mathcal S_i'
$$

而 endpoint 仍：

$$
S'
\equiv_{\mathfrak I}
S,
$$

可以對當前 inquiry 視為 solver-substitution equivalent。

但 provenance 必須不同。

---

# 124. Cross-Solver Verification

同一 coupling subproblem 可以由：

$$
\mathcal S_i,
\mathcal S_i'
$$

獨立求解。

比較：

$$
r_{\mathrm{crosssolver}}.
$$

這可以提高 stable-core maturity。

---

# 125. Global Residual Engine

第一個 MWT-06 runtime 模組：

$$
\boxed{
\mathsf{GRE}
=
\text{Global Residual Engine}.
}
$$

輸入：

- participant states；
- port states；
- global constraints；
- identity / invariant contracts。

輸出：

$$
\mathbf R_C.
$$

---

# 126. Coupling Registry

第二個模組：

$$
\boxed{
\mathsf{CReg}.
}
$$

保存：

```text
participant_id
port_id
source
target
coupling_type
quantity_contract
time_contract
resolution_contract
identity_contract
history_policy
version
```

---

# 127. Port Contract Store

第三個模組：

$$
\boxed{
\mathsf{PCS}.
}
$$

把每條 port 的 semantic / temporal / resolution / legality certificates 版本化。

---

# 128. Temporal Alignment Layer

第四個模組：

$$
\boxed{
\mathsf{TAL}.
}
$$

處理：

- local clocks；
- common coupling coordinate；
- interpolation；
- extrapolation；
- event alignment；
- stale data；
- waveform windows。

---

# 129. Resolution Transfer Layer

第五個模組：

$$
\boxed{
\mathsf{RTL}.
}
$$

處理：

- restrict；
- prolong；
- aggregate；
- reconstruct；
- transfer residual；
- adaptive fidelity。

---

# 130. Coupling Iteration Engine

第六個模組：

$$
\boxed{
\mathsf{CIE}.
}
$$

管理：

- explicit sweep；
- implicit iteration；
- Jacobi；
- Gauss-Seidel；
- waveform；
- asynchronous update；
- stopping rule。

---

# 131. Solver Federation Manager

第七個模組：

$$
\boxed{
\mathsf{SFM}.
}
$$

負責：

- participant lifecycle；
- capability discovery；
- solver substitution；
- checkpoint；
- failure；
- multi-AI assignment。

---

# 132. Acceleration / Relaxation Layer

第八個模組：

$$
\boxed{
\mathsf{ARL}.
}
$$

管理 coupling acceleration backend。

任何 acceleration 必須帶 domain / legality。

---

# 133. Coupling Conflict Ledger

第九個模組：

$$
\boxed{
\mathsf{CCL}.
}
$$

保存：

- incompatible contracts；
- residual conflict；
- solver disagreement；
- temporal mismatch；
- identity mismatch；
- failed merge。

---

# 134. World-Solve Commit Engine

第十個模組：

$$
\boxed{
\mathsf{WSCE}.
}
$$

只有：

1. mandatory residuals satisfied；
2. MWT-02 hard legality satisfied；
3. MWT-03 schedule/merge certificate complete；
4. MWT-04 closure update possible；

才輸出：

$$
\boxed{
C_{\mathrm{WSolve}}^{\mathrm{commit}}.
}
$$

---

# 135. World-Solve Cycle

完整最低流程：

```text
1. define world-solve scope
2. activate required participants
3. validate coupling ports
4. align time / event windows
5. align or transfer resolution
6. run local solves
7. exchange coupling quantities
8. evaluate typed residual family
9. update coupling state
10. accelerate / relax if legal
11. reschedule noncommutative interactions
12. refine/coarsen if required
13. repeat until convergence / failure / budget exhaustion
14. form coupling convergence witness
15. commit through MWT-04
```

---

# 136. Reference World Solve

本 Source Pack 附：

```text
mwt06_coupling_reference.py
```

它只固定最低 scalar two-participant fixed-point coupling：

$$
x=S_1(y),
$$

$$
y=S_2(x),
$$

並提供：

- Jacobi；
- Gauss-Seidel；
- relaxation；
- residual；
- convergence / active / diverged / budget-exhausted status。

它不是一般 multiphysics solver。

用途只是讓 GCC v0.1 有一個可重放 operational anchor。

---

# 137. Coupling Status Family

reference runtime 使用：

$$
\boxed{
\mathbb C
=
\{
\mathsf{Converged},
\mathsf{Active},
\mathsf{Diverged},
\mathsf{BudgetExhausted},
\mathsf{Invalid}
\}.
}
$$

這只是 reference implementation status。

不取代正文更廣的：

$$
\mathsf{Undetermined},
\mathsf{Conflicted}.
$$

---

# 138. Convergence Certificate

對 converged world solve：

$$
\boxed{
C_{\mathrm{conv}}
=
(
\Omega,
\gamma_C,
\mathbf R_C,
\varepsilon,
V,
H,
B
).
}
$$

其中：

- $\Omega$：scope；
- $\gamma_C$：coupling schedule；
- $\mathbf R_C$：final residual profile；
- $V$：versions；
- $H$：history / timing；
- $B$：budget。

---

# 139. Convergence Is Not Homogenization

participant $i$ 、 $j$ 收斂後仍可以：

$$
P_i
\neq
P_j,
$$

$$
\lambda_i
\neq
\lambda_j,
$$

$$
T_i
\neq
T_j.
$$

所以：

$$
\boxed{
\text{global convergence}
\neq
\text{same representation}.
}
$$

---

# 140. Convergence Is Contract Satisfaction

更精確：

$$
\boxed{
\text{Convergence}
=
\text{required coupling contracts become mutually satisfied}.
}
$$

而不是：

$$
x_1=x_2=\cdots=x_n.
$$

---

# 141. Persistent Heterogeneity

一個成熟 world solve 可以收斂在：

$$
\boxed{
\text{heterogeneous fixed relation}
}
$$

而不是 homogeneous state。

例如：

- 1D / 3D；
- symbolic / numeric；
- theorem prover / simulation；
- observer-local / global summary。

---

# 142. Fixed Relation

如果 participants 的 joint state：

$$
X^\ast
=
(x_1^\ast,\ldots,x_n^\ast)
$$

滿足所有 coupling contracts：

$$
G_a(X^\ast)=0
$$

或：

$$
G_a(X^\ast)
\preceq
\varepsilon_a,
$$

可稱：

$$
\boxed{
\text{coupled fixed relation state}.
}
$$

它比「所有 component 值相同」更一般。

---

# 143. Noncommutative Coupled Fixed Point

如果 coupling sweep：

$$
\Phi_{\gamma_1}
$$

與：

$$
\Phi_{\gamma_2}
$$

順序不同，

可能有：

$$
z_{\gamma_1}^\ast
\neq
z_{\gamma_2}^\ast.
$$

那麼 scheduler order 是 model specification 的一部分，或需要更強 coupling formulation 消除 order artifact。

---

# 144. Order Artifact Diagnostic

如果不同合法 schedule 產生不同 converged states，但理論預期應 order-invariant，

這可能表示：

- coupling scheme 太弱；
- tolerance 太鬆；
- bridge lag；
- discretization artifact；
- hidden noncommutativity。

產生：

$$
\boxed{
\mathsf{OrderArtifactObligation}.
}
$$

---

# 145. Scheme-Invariant Core

如果多種 coupling schemes：

$$
\chi_1,\ldots,\chi_m
$$

收斂後共享某 invariant：

$$
I^\ast,
$$

可提升：

$$
I^\ast
$$

為 stable-core candidate。

這是一種 cross-scheme verification。

---

# 146. Coupling Failure Can Discover Mathematics

如果某 port residual 長期無法收斂，

不一定只是工程 bug。

可能表示：

- presentations 其實不相容；
- 缺 dimension；
- identity contract 過強；
- global invariant 不存在；
- branch 應永久分離。

因此：

$$
\boxed{
\text{coupling failure}
}
$$

也可以是理論發現訊號。

---

# 147. World Solve as Inquiry Machine

MWT-06 不要求每次都模擬一個物理系統。

World Solve 可以用來回答：

- 這些 representations 能否共同滿足？
- 哪些 invariants 跨模型穩定？
- 哪些 branches 真的不能 merge？
- 哪個新 dimension 能降低 residual？
- 哪個 solver assumption 造成 conflict？

因此它是一個 general mathematical inquiry runtime。

---

# 148. AI-Native Solver Federation

AI / AGI 可負責：

- 選 solver；
- 建 bridge；
- 監控 residual；
- 調 coupling scheme；
- 產生 refinement；
- 分支；
- cross-check；
- 解釋 convergence。

人類則檢查：

- scope；
- hard contracts；
- stable result；
- conflict；
- provenance。

---

# 149. Solver Selection Is Dynamic

今天：

$$
\mathcal S_i
$$

最適合。

下一輪新 presentation / hardware / proof backend 出現，可替換：

$$
\mathcal S_i'.
$$

所以 solver identity 不應與 mathematical participant identity 永久綁死。

---

# 150. Solver Ensemble

一個 participant 可以同時啟動：

$$
\mathcal S_i^{(1)},
\ldots,
\mathcal S_i^{(m)}
$$

形成 local ensemble。

global coupling 使用：

- consensus；
- certified representative；
- branch；
- interval result。

這提高 robust verification。

---

# 151. Ensemble Disagreement

local solvers disagreement：

$$
d
(
y_i^{(a)},
y_i^{(b)}
)
>
\varepsilon
$$

產生：

$$
\boxed{
r_{\mathrm{solver}}
}
$$

進 global residual。

---

# 152. Human Participant

人類也可以作 participant：

$$
\mathfrak P_H.
$$

port 可能交換：

- approval；
- semantic judgment；
- goal；
- exception；
- interpretation。

但 human decision 仍需版本與 provenance。

---

# 153. Human Bottleneck Is Optional, Not Universal

MWT 不要求每一 coupling iteration 都問人。

只有：

- governance；
- high risk；
- unresolved semantic conflict；

才觸發 human participant。

否則 AI-native runtime 可自動迭代。

---

# 154. World Solve Budget

定義：

$$
\boxed{
B_{\mathrm{WS}}
=
(
B_{\mathrm{iter}},
B_{\mathrm{time}},
B_{\mathrm{compute}},
B_{\mathrm{communication}},
B_{\mathrm{refinement}},
B_{\mathrm{branch}}
).
}
$$

budget exhaustion：

$$
\boxed{
\neq
\text{proof of no solution}.
}
$$

---

# 155. Budget Exhaustion Output

如果未收斂：

$$
\boxed{
\mathsf{BudgetExhausted}
}
$$

並保存：

- best current state；
- residual profile；
- trend；
- open branches；
- suggested next refinement。

---

# 156. Coupling Debt

如果為了暫時使用接受：

$$
r_{\mathrm{soft}}
>
\varepsilon_{\mathrm{desired}},
$$

可以產生：

$$
\boxed{
D_C^{\mathrm{coupling}}
}
$$

進 MWT-04 obligation queue。

不能靜默稱完全收斂。

---

# 157. World-Solve Maturity

### WS0 — Ad Hoc

手工交換結果。

### WS1 — Port-Defined

已有 coupling contract。

### WS2 — Executable

可自動交換與迭代。

### WS3 — Residual-Certified

mandatory residual 可機器檢查。

### WS4 — Multi-Solver Verified

至少部分 participants / schemes 有 cross-check。

### WS5 — Stable World-Solve Candidate

結果可進 MWT-04 Stable Core 並通過 reopen / replay。

---

# 158. MWT-06 Minimal Constitution

v0.1 固定二十六條：

### C1 — Coupling Requires Feedback or Explicit Dependency

單純共存不構成動態 coupling。

### C2 — Coupling Ports Are Typed Contracts

edge 不只是裸資料通道。

### C3 — Global Does Not Mean All-to-All

只耦合有必要且合法的 relations。

### C4 — Global Does Not Mean Monolithic

partitioned / hybrid / asynchronous 都可合法。

### C5 — Local Solver Heterogeneity Is Preserved

不要求統一 solver 語言。

### C6 — Local Autonomy Does Not Remove Global Accountability

local output 必須接受 global invariant / residual。

### C7 — Time Is Port-Specified

不同 participants 可有不同 local time。

### C8 — Common Coupling Time Need Not Be Absolute Physical Time

可使用 logical/event coordinate。

### C9 — Resolution Transfer Must Be Explicit

跨尺度不能默認無損。

### C10 — Semantic Translation Must Precede Numeric Exchange

數值型別相同不代表語義相同。

### C11 — History / Lag Is First-Class

stale / waveform / rollback policy 必須入 contract。

### C12 — Residuals Are Typed

不要求全部壓成單一 norm。

### C13 — Hard Residuals Are Non-Compensatory

hard coupling violation 不可被其他好分數補償。

### C14 — Convergence Is Scoped

任何 convergence claim 都要帶 inquiry / identity / tolerance / version。

### C15 — Convergence Does Not Require Homogenization

異質 participants 可在 relation 上收斂。

### C16 — Multiple Fixed Points Are Allowed

不能預設唯一 solution。

### C17 — Coupling Order May Be Noncommutative

sweep order 必須進 scheduler。

### C18 — Acceleration Is a Legal Operator

不得無條件使用數值 relaxation。

### C19 — Failure Is Preserved

local / coupling failure 不得被吞掉。

### C20 — Coupling Can Trigger Refinement

residual 過高可 reopen MWT-05。

### C21 — Solver Substitution Requires Contract Preservation

替換 solver 不是 implementation-only 事件。

### C22 — World Solve Is Budgeted

有限 runtime 永遠需要 budget。

### C23 — Budget Exhaustion Is Not Impossibility

未完成不等於不存在 solution。

### C24 — Commit Requires Cross-Layer Certificates

MWT-02/03/04 必須共同通過。

### C25 — Coupling Results Carry Provenance

時間、resolution、schedule、solver version 都不可丟。

### C26 — World Solve May Return Structured Non-Solution

branch/conflict/unknown/infeasible 都是合法輸出。

---

# 159. 命題：Coupling Convergence 不推出 Representation Equality

若 participants：

$$
P_i\neq P_j
$$

但所有 mandatory coupling contracts satisfied，

則 World Solve 可 Converged。

所以：

$$
\boxed{
\mathsf{Converged}
\not\Rightarrow
P_i=P_j.
}
$$

---

# 160. 命題：One-Way Coupling 不是 Two-Way Fixed Point

如果：

$$
i\to j
$$

且 $j$ 不回寫，

則一般不需要求解：

$$
z=\Phi(z).
$$

因此不能把所有 coupling 都誤寫成 fixed-point iteration。

---

# 161. 命題：Stale Input 可改變 Legality

若 port 最大 staleness：

$$
\Delta_{\max}
$$

而：

$$
\operatorname{Age}(z)>\Delta_{\max},
$$

則 exchange 可被 MWT-02 判為 Illegal，即使 $z$ 數值本身型別正確。

---

# 162. 命題：Resolution Transfer Loss 可阻止 Stable Commit

若 hard identity / invariant 需要的資訊在：

$$
R_{i\to j}^{\lambda}
$$

中被丟失，

則即使 local solvers 都 converged，global convergence contract 仍不能成立。

---

# 163. 命題：World Solve Divergence 不證明原問題無解

迭代 scheme：

$$
\Phi
$$

diverge，只證明該 scheme / initialization / schedule / parameters 未成功。

不能由此推出 underlying coupled problem 無解。

---

# 164. 條件定理：Certified World-Solve Commit

若 scope $\Omega$ 下：

1. 所有 required participants current states Legal；
2. 所有 coupling ports Legal；
3. mandatory temporal / resolution / semantic contracts satisfied；
4. mandatory residuals meet exact / tolerance contract；
5. schedule / branch merge 有 MWT-03 certificate；
6. no unresolved hard conflict；
7. final staging state通過 MWT-04 world-state update；

則存在：

$$
\boxed{
C_{\mathrm{WSolve}}^{\mathrm{commit}}
}
$$

使本次 World Solve endpoint 可寫入 current stable world-state runtime。

此定理由本文 commit definition 成立。

---

# 165. 條件定理：Multi-Resolution Round-Trip Fidelity

若：

$$
\mathcal R:P_f\to P_c,
$$

$$
\mathcal P:P_c\to P_f
$$

滿足對 inquiry family $\mathcal Q$：

$$
\mathcal P\mathcal R(x)
\equiv_{\mathfrak I,\mathcal Q}
x
$$

對所有相關 $x$ 成立，

則 fine→coarse→fine transfer 對該 scope 為 faithful round-trip。

不能由此推出對所有未來 inquiry 無損。

---

# 166. 研究猜想：World-Solve Federation

對許多未來 AI 數學問題，將多個專門 solver 保持自治並以高品質 coupling contracts federate，可能比強制重寫成單一 universal solver 更易維護、驗證與擴展。

---

# 167. 研究猜想：Residual-Driven Mathematics

長期無法消失的 semantic / identity / branch residual 可能比單純 solver error 更有研究價值，因為它們可能暴露新 dimension、missing invariant 或 representation mismatch。

---

# 168. 研究猜想：Multi-Resolution Mathematics

未來 AI 可以同時在：

- coarse global presentation；
- fine local presentation；
- symbolic layer；
- numerical layer；
- proof layer；

保持不同解析度，只在 coupling interface 動態交換必要資訊，從而突破單一人類可管理 representation 的限制。

---

# 169. 研究猜想：Asynchronous Mathematical Worlds

若 causality、staleness、certificate 與 rollback 能被完整治理，多 AI mathematical participants 不必在每一輪 global barrier 同步，也能形成可驗證的 asynchronous world solve。

---

# 170. 開放問題

### O1 — Universal Coupling Port Vocabulary

能否找到足夠小但高覆蓋的 port contract？

### O2 — Non-Numeric Residual Algebra

symbolic / proof / identity residual 如何共同組合？

### O3 — Cross-Scale Conservation

跨 resolution transfer 如何一般性保存 invariants？

### O4 — Coupling Scheme Selection

AI 如何根據 observed residual 自動選 explicit / implicit / waveform / asynchronous？

### O5 — Black-Box Identifiability

只能觀察 I/O 的 solver，何時足以建立 reliable coupling？

### O6 — Noncommutative Fixed Points

不同 schedule fixed points 不同時，如何區分真結構與 scheme artifact？

### O7 — Multiway Hypercoupling

高階 coupling constraints 如何避免 pairwise decomposition loss？

### O8 — World-Solve Complexity

heterogeneous coupling graph 的 complexity 如何描述？

### O9 — Solver Trust

不同 AI / solver backend 的 certificate maturity 如何進 coupling policy？

### O10 — Coupling-Driven Theory Discovery

何時可以把 persistent residual 升級為新理論 candidate？

---

# 171. 外部研究接口：preCICE

preCICE 是現有成熟的 partitioned multiphysics / multiscale coupling library，提供：

- solver communication；
- data mapping；
- transient coupling；
- explicit / implicit coupling；
- black-box solver reuse。

MWT 不重新發明它。

MWT 把這類 coupling middleware 視為物理／數值 participant federation 的成熟 backend。

---

# 172. 外部研究接口：FMI

Functional Mock-up Interface 提供：

- Model Exchange；
- Co-Simulation；
- Scheduled Execution；

等標準介面。

Co-Simulation 中，FMU 可以包含自己的 solver，master / importer 管 communication point、時間推進、input/output 與 event。

MWT 將 FMI 視為工程 co-simulation port 的成熟參照，但 GCC 的 presentation 類型比動態模型更廣。

---

# 173. 外部研究接口：Waveform Relaxation

waveform relaxation 為 partitioned time-dependent coupling 提供：

- independent time grids；
- multirate；
- time-window function exchange；
- iterative coupling。

其 asynchronous extensions 也說明：

$$
\boxed{
\text{global convergence}
\neq
\text{every step barrier synchronization}.
}
$$

---

# 174. 外部研究接口：Quasi-Newton Coupling

interface quasi-Newton / waveform iteration 類方法已被用於 strongly coupled partitioned multiphysics，以改善 black-box coupling 收斂。

MWT 的 Acceleration Layer 可直接掛接這些成熟算法。

---

# 175. 與 WTC 4.0 的接口

WTC 4.0 已形成：

$$
\text{analysis}
\rightarrow
\text{coupling}
\rightarrow
\text{synthesis}
\rightarrow
\text{state update}
\rightarrow
\text{feedback}.
$$

MWT-06 不把所有 coupling 改寫成 wave / spectral coefficients。

它吸收的是：

$$
\boxed{
\text{coupling itself can be adaptive, relational, history-aware, feedback-driven}.
}
$$

WTC 因此可以成為某些 participant 或 coupling backend。

---

# 176. 與共同時間座標層的接口

既有共同時間座標層已指出：

> 異質系統若缺乏共同 temporal coordination，空間上可連接的系統仍可能因過時資料、事件順序與版本錯置失效。

MWT-06 將這個概念正式放入：

$$
\tau_i:T_i\rightharpoonup\mathbb T_C
$$

與 temporal residual。

---

# 177. 與 MWT-05 的接口

如果：

$$
r_{\lambda}
$$

過大：

$$
\boxed{
\text{MWT-06 residual}
\rightarrow
\text{MWT-05 refinement obligation}.
}
$$

refinement 完成後重新 World Solve。

---

# 178. 與 MWT-04 的接口

World Solve 只有 converged 不夠。

還要：

$$
\boxed{
\mathsf{WSolve}
\rightarrow
\mathsf{WorldStateCommit}.
}
$$

MWT-04 決定 Stable Core、branch、conflict、obligation、history 與 reopen。

---

# 179. 與 MWT-03 的接口

coupling iteration sequence：

$$
\gamma_C
$$

是 schedule。

noncommutative coupling order、async events、rollback 全部使用 NCS。

---

# 180. 與 MWT-02 的接口

任何：

- local solve；
- exchange；
- transfer；
- acceleration；
- merge；

都是 interaction。

必須過 legality。

---

# 181. 與 MWT-01 的接口

coupling port 的 bridge、identity、presentation fidelity 全部來自 Presentation Theory。

所以 MWT-06 並沒有繞過前五篇。

它是前五篇第一次真正一起運行。

---

# 182. MWT-01～06 的世界循環

目前可以寫：

$$
\boxed{
\begin{aligned}
\text{Present}
&\rightarrow
\text{Judge}\\
&\rightarrow
\text{Schedule}\\
&\rightarrow
\text{World-State}\\
&\rightarrow
\text{Refine}\\
&\rightarrow
\text{Couple}\\
&\rightarrow
\text{Solve}\\
&\rightarrow
\text{Converge}\\
&\rightarrow
\text{Reopen}.
\end{aligned}
}
$$

這已經不是一個單次 theorem pipeline。

而是一個長期數學世界 runtime。

---

# 183. 下一篇接口

下一篇最自然的是：

# **MWT-07：Global Query Semantics, World Inference, and Proof/Computation Federation**

因為 MWT-06 已經讓世界中的不同部分真正一起算。

下一步要回答：

$$
\boxed{
\text{使用者／AI 對這個世界提出一個問題時，
系統如何決定要啟動哪些 presentations、solvers、couplings、
proof obligations、simulations 與 observers？}
}
$$

也就是從「世界可以一起算」走到：

> **怎麼對整個世界問問題。**

---

# 184. 一句話版

> **MWT-06 將全域計算形式化為 heterogeneous solver federation：不同 presentation、尺度、局部時間、solver 與 observer 不必先被統一，而是透過帶 semantic、temporal、resolution、identity、history 與 legality contract 的 coupling ports 互相施加條件與回饋。World Solve 可以是 monolithic、partitioned、hybrid、multirate、waveform、event-driven 或 asynchronous；其收斂不要求所有 participant 變成同一表示，而要求所有 mandatory coupling residual 與 global invariants 在指定 scope 下達到契約。persistent residual 會反向觸發 refinement、branch、solver substitution 或新理論探索，最後只有具有 coupling convergence、schedule、legality 與 world-state closure 證書的 endpoint 才能進 Stable Core。**

---

# 附錄 A：核心符號表

| 符號 | 意義 |
|---|---|
| $\mathfrak P_i$ | solver participant |
| $\mathcal S_i$ | local solver |
| $T_i$ | local time structure |
| $\lambda_i$ | local resolution profile |
| $\mathfrak p_{ij}$ | coupling port |
| $B_{ij}$ | semantic/presentation bridge |
| $\tau_{ij}$ | temporal alignment map |
| $R_{ij}$ | resolution transfer |
| $\mathcal G_t^C$ | Global Coupling Graph |
| $\Omega$ | World-Solve scope |
| $\mathsf{WSolve}_\Omega$ | World Solve |
| $z$ | interface/coupling state |
| $\Phi_\Gamma$ | abstract coupling sweep map |
| $\mathbf R_C$ | typed coupling residual profile |
| $\mathbb T_C$ | common coupling-time coordinate |
| $\mathsf{GRE}$ | Global Residual Engine |
| $\mathsf{CReg}$ | Coupling Registry |
| $\mathsf{PCS}$ | Port Contract Store |
| $\mathsf{TAL}$ | Temporal Alignment Layer |
| $\mathsf{RTL}$ | Resolution Transfer Layer |
| $\mathsf{CIE}$ | Coupling Iteration Engine |
| $\mathsf{SFM}$ | Solver Federation Manager |
| $\mathsf{ARL}$ | Acceleration/Relaxation Layer |
| $\mathsf{CCL}$ | Coupling Conflict Ledger |
| $\mathsf{WSCE}$ | World-Solve Commit Engine |

---

# 附錄 B：v0.1 非主張清單

MWT-06 不主張：

1. 所有 world solve 都可寫成單一聯立方程；
2. partitioned 一定比 monolithic 好；
3. monolithic 一定比 partitioned 好；
4. 所有 coupling 都是 fixed-point problem；
5. 所有 fixed point 都存在；
6. 所有 fixed point 都唯一；
7. 所有 coupling iteration 都收斂；
8. 所有 residual 都可數值化；
9. 所有 local solvers 都有同一時間；
10. common coupling coordinate 是宇宙絕對時間；
11. coarse-to-fine transfer 可以無中生有重建真實細節；
12. interpolation / extrapolation 無誤差；
13. asynchronous coupling 一定穩定；
14. waveform relaxation 適用所有非時間問題；
15. quasi-Newton acceleration 適用所有 coupling state；
16. black-box solver 不需要 contract；
17. solver failure 表示原問題無解；
18. coupling failure 一定是工程錯誤；
19. persistent residual 一定表示新 dimension；
20. 1D–3D coupling 等於所有 multi-resolution mathematics；
21. FMI / preCICE 等於 MWT；
22. World Solve convergence 等於 World truth；
23. 所有 participants 都應 AI 自動控制；
24. 人類必須退出 coupling loop；
25. MWT-06 已建立 universal solver；
26. 全域耦合表示每個節點都要互相連接。

---

# 附錄 C：外部研究接口與參考文獻

1. Gerasimos Chourdakis et al., **preCICE v2: A Sustainable and User-Friendly Coupling Library**, *Open Research Europe*, 2022.  
2. preCICE Project, **preCICE Documentation and Coupling Fundamentals**, current documentation, 2026.  
3. Modelica Association Project FMI, **Functional Mock-up Interface Specification 3.0.2**, 2024; current development specification also maintained by the FMI Project.  
4. Peter Meisrimel and Philipp Birken, **Waveform Relaxation with Asynchronous Time-Integration**, 2021, arXiv:2106.13147.  
5. Benjamin Rüth, Benjamin Uekermann, Miriam Mehl, Philipp Birken, Azahar Monge, and Hans-Joachim Bungartz, **Quasi-Newton Waveform Iteration for Partitioned Fluid-Structure Interaction**, 2020, arXiv:2001.02654.  
6. Peter Meisrimel, Azahar Monge, and Philipp Birken, **A Time Adaptive Multirate Dirichlet-Neumann Waveform Relaxation Method for Heterogeneous Coupled Heat Equations**, 2020, arXiv:2007.00410.  
7. James Jackaman and Scott MacLachlan, **Space-Time Waveform Relaxation Multigrid for Navier-Stokes**, 2024, arXiv:2407.13997.  

---

# 附錄 D：內部依賴

MWT-06 直接依賴：

- MWT-01《World Primitive 與 Presentation Theory》
- MWT-02《Global Legality Calculus》
- MWT-03《Global Interaction Graph and Noncommutative Scheduler》
- MWT-04《World State, Branch Convergence, and Dynamic Fixed Points》
- MWT-05《Unbounded Refinement, World Expansion, and Resolution Dynamics》
- WTC 4.0《自適應譜—狀態—關係耦合的動態計算框架》
- 《共同時間座標層：異質解題系統的時序對齊與跨時空轉換》
- Series B observer / transport / noncommutativity 主線
- RDSS local-time / history 主線

本文將既有「耦合」從局部框架提升成 MWT World-Solve 層，但保留各理論原有邊界。

