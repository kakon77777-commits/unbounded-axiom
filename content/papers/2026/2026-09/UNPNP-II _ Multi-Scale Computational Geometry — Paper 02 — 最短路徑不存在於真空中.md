# UNPNP-II / Multi-Scale Computational Geometry — Paper 02
## 最短路徑不存在於真空中
### Observer-, Granularity-, Scale-, Boundary-, and Objective-Relative Shortest Routes

**系列名稱：** UNPNP-II｜Multi-Scale Computational Geometry  
**系列中文名：** UNPNP 第二層：多尺度計算幾何與相對最短路徑  
**篇次：** Paper 02 / 08  
**作者：** Neo.K with Aletheia（GPT）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-08  
**文件性質：** 計算路徑理論／多目標最佳化／UNPNP 擴充論文  
**前置：** Paper 01《計算的一到底是什麼？》  
**狀態：** Canonical Draft

---

## 摘要

「最短路徑」通常被寫成：

$$
\Gamma^*
=
\arg\min_{\Gamma\in\mathcal P(s,g)}
C(\Gamma).
$$

這個表示在圖論、演算法與最佳化中完全合理，但它隱含一組常被省略的前提：節點與邊已被指定、一步的粒度已固定、可行路徑集合已確定、世界邊界已封閉、觀察者使用同一表示、成本函數已選定，而且不同路徑可以在同一度量下比較。

UNPNP-II Paper 01 已指出：

$$
\boxed{
\text{There is no scale-free computational one.}
}
$$

若「一步」本身依賴 computational chart，則「最短」也不可能脫離 chart 而獨立存在。

本文因此提出：

$$
\boxed{
\text{Shortest Route}
=
\text{Relative Optimum under a Declared Computational World}.
}
$$

這裡的「相對」不是任意主義。本文要求一個 shortest-route claim 至少顯式綁定：

$$
\boxed{
\Xi
=
\langle
\mathbf W,
\partial W,
\chi,
q,
\mathcal F,
\mathbf C,
\omega,
\mathcal V
\rangle
}
$$

其中：

- $\mathbf W$：World primitive 或指定 executable world presentation；
- $\partial W$：此次比較的 World boundary；
- $\chi$：computational chart；
- $q$：task / goal；
- $\mathcal F$：feasible route set；
- $\mathbf C$：成本向量；
- $\omega$：標量化權重或偏好結構；
- $\mathcal V$：驗證與合法性條件。

因此本文將條件式最短路徑寫成：

$$
\boxed{
\mathcal R^*_{\Xi}
=
\arg\min_{\mathcal R\in\mathcal F_{\Xi}}
J_{\Xi}(\mathcal R).
}
$$

若成本無法合理標量化，則改用：

$$
\boxed{
\mathfrak P^*_{\Xi}
=
\operatorname{ParetoMin}_{\mathcal R\in\mathcal F_{\Xi}}
\mathbf C_{\Xi}(\mathcal R).
}
$$

本文提出五個核心區分：

$$
\boxed{
\text{Hop Shortest}
\neq
\text{Work Shortest}
\neq
\text{Depth Shortest}
\neq
\text{Time Shortest}
\neq
\text{Risk-Adjusted Shortest}.
}
$$

並進一步指出：兩條 route 的排序可以因 observer、granularity、scale、resource budget 或 world boundary 改變而反轉，因此「A 比 B 短」若沒有下標，通常是不完整命題。

本文同時把 MWT、GCM 與 UNPNP 接入同一形式。MWT 提供 World / presentation 分離；GCM 提供 heterogeneous domains、global coherence、dynamic configuration 與 observer/materialization 分離；UNPNP 提供跨底空間 route、Adaptive Corridor、Path Compilation、Crystallization 與 Safe Reachable World。三者共同產生新的研究對象：

$$
\boxed{
\text{World-Relative Computational Route Optimization}.
}
$$

它不再只問：「哪條既有路最短？」而問：「在哪個 world boundary、哪種尺度、哪張 chart、哪組 computational configuration 與哪種成本語義下，哪一條 route 最值得被執行、編譯、結晶或重新展開？」

---

# 1. 經典最短路徑其實已經是條件式概念

在 weighted graph：

$$
G=(V,E,w)
$$

中，從 $s$ 到 $g$ 的最短路徑可以寫成：

$$
\Gamma^*
=
\arg\min_{\Gamma\in\mathcal P_G(s,g)}
\sum_{e\in\Gamma}w(e).
$$

這個定義沒有問題，但其成立依賴：

1. $V$ 已固定；
2. $E$ 已固定；
3. edge semantics 已固定；
4. $w$ 已固定；
5. source / goal 已固定；
6. feasible path set 已固定；
7. graph boundary 已固定。

因此：

$$
\boxed{
\text{Shortest path is already model-relative.}
}
$$

UNPNP-II 做的不是否定圖論，而是把原本被省略的模型條件重新提升成 Runtime 可操作的研究變數。

---

# 2. 同一 World 可以被切成不同 Graph

令：

$$
\rho_{\chi_1}(\mathbf W)=G_1,
$$

以及：

$$
\rho_{\chi_2}(\mathbf W)=G_2.
$$

即使 $\mathbf W$ 相同，仍可有：

$$
G_1\neq G_2.
$$

例如：

```text
fine chart:
instruction → instruction → instruction → ...

coarse chart:
function → module → algorithm
```

如果直接比較：

$$
L_{G_1}(\Gamma)
$$

與：

$$
L_{G_2}(\Gamma),
$$

就可能把不同單位系統誤當同一尺度。

因此沒有 chart 下標的：

$$
L(\Gamma)
$$

通常是不完整的。

---

# 3. 路徑集合本身也可能變

傳統 shortest path 常假設：

$$
\mathcal P_G(s,g)
$$

已存在。

但 UNPNP 可以生成新的 typed hyperlink：

$$
\widehat{\ell}_{s,g}.
$$

因此：

$$
E_t\neq E_{t+1},
$$

而：

$$
\mathcal P_t(s,g)
\neq
\mathcal P_{t+1}(s,g).
$$

所以 UNPNP 面對的不只是：

$$
\boxed{
\text{shortest path in a graph}
}
$$

而是：

$$
\boxed{
\text{shortest route in an evolving route space}.
}
$$

---

# 4. World boundary 會改變「全域」

GCM 已指出：

$$
\mathrm{Global}_{W}(\mathcal U)
\land
\mathrm{Local}_{H}(\mathcal U)
$$

可以同時成立。

因此 shortest route 也必須相對：

$$
\partial W.
$$

一條在 $W_A$ 內最短的 route，若把 remote service、external cache、accelerator、precomputed index 或 another agent 納入更大的 $W_B$，可能不再最短。

所以：

$$
\boxed{
\mathcal R^*_{W_A}
\neq
\mathcal R^*_{W_B}
}
$$

完全合理。

---

# 5. Observer 不一定看到同一條路

令 $o_u$ 為 user observer， $o_p$ 為 programmer observer， $o_r$ 為 runtime observer， $o_h$ 為 hardware observer。

同一 execution：

```text
click "Generate Report"
```

對 user：

$$
H_{o_u}=1.
$$

對 workflow：

$$
H_{o_p}=8.
$$

對 runtime：

$$
W_{o_r}=10^5.
$$

對 hardware：

$$
W_{o_h}\gg10^5.
$$

因此：

$$
\boxed{
\text{Observer-visible length}
\neq
\text{executional work}.
}
$$

---

# 6. 最短不一定是最快，最快不一定是最值得走

假設：

$$
H_A=2,
\qquad
T_A=100\text{ ms},
$$

但：

$$
H_B=8,
\qquad
T_B=20\text{ ms}.
$$

則：

$$
H_A<H_B
$$

但：

$$
T_A>T_B.
$$

所以：

$$
\boxed{
\text{Hop Shortest}
\neq
\text{Time Shortest}.
}
$$

再假設：

$$
T_A<T_B
$$

但：

$$
R_A\gg R_B.
$$

對高風險任務，B 可能才是合理 optimum。

因此：

$$
\boxed{
\text{Fastest}
\neq
\text{Safest}
\neq
\text{Best}.
}
$$

---

# 7. Work、Depth 與 Wall-Clock 必須分離

若：

$$
W_A=1000,
\qquad
D_A=2,
$$

而：

$$
W_B=100,
\qquad
D_B=20,
$$

A 可能靠高度並行取得較低 wall-clock，但總工作量更高。

因此：

$$
\boxed{
\text{Depth Shortest}
\neq
\text{Work Shortest}.
}
$$

這直接接回 24 計算範式中 sequential / parallel update organization 的差異。

---

# 8. Route Cost Vector

本文定義第一版 route cost vector：

$$
\boxed{
\mathbf C_{\Xi}(\mathcal R)
=
(
H,
W,
D,
T,
M,
K,
V,
P,
U,
E,
R,
L_O
).
}
$$

其中：

- $H$：hop count；
- $W$：total work；
- $D$：causal / parallel depth；
- $T$：wall-clock latency；
- $M$：memory / materialization；
- $K$：communication / crossing cost；
- $V$：verification cost；
- $P$：precompute / compile cost；
- $U$：update / maintenance cost；
- $E$：energy / irreversible cost；
- $R$：risk / authorization cost；
- $L_O$：observation / projection loss。

這不是宣稱十二維是終極完備，而是避免把本質不同的成本過早壓成單一 scalar。

---

# 9. Scalar Objective 與 Pareto Route

若任務允許指定權重：

$$
\omega
=
(
\omega_H,
\omega_W,
\dots,
\omega_{L_O}
),
$$

則：

$$
\boxed{
J_{\Xi}(\mathcal R)
=
\omega^\top
\mathbf C_{\Xi}(\mathcal R).
}
$$

於是：

$$
\boxed{
\mathcal R^*_{\Xi}
=
\arg\min_{\mathcal R\in\mathcal F_{\Xi}}
J_{\Xi}(\mathcal R).
}
$$

若 latency、correctness、energy、privacy、safety 等成本不能合理交換，則不強迫 scalarization，而使用：

$$
\boxed{
\mathfrak P^*_{\Xi}
=
\operatorname{ParetoMin}
\mathbf C_{\Xi}.
}
$$

此時 optimum 可能是一組 route，而不是唯一一條線。

---

# 10. Relative 不等於 Arbitrary

如果 shortest route 是 observer-relative，不表示每個 observer 想說誰最短都可以。

一個合法 claim 必須提供：

$$
\boxed{
\Xi
=
\langle
\mathbf W,
\partial W,
\chi,
q,
\mathcal F,
\mathbf C,
\omega,
\mathcal V
\rangle.
}
$$

因此 relativity 是：

$$
\boxed{
\text{declared conditionality},
}
$$

不是：

$$
\boxed{
\text{unconstrained subjectivity}.
}
$$

---

# 11. Shortest-Route Claim

本文定義：

$$
\boxed{
\operatorname{SRC}
=
\langle
\mathcal R^*,
\Xi,
\operatorname{Proof},
\operatorname{Receipt}
\rangle.
}
$$

任何重要「最短」主張至少應回答：

1. relative to which world？
2. relative to which world boundary？
3. relative to which chart？
4. relative to which observer？
5. under which feasible set？
6. minimizing which costs？
7. under which legality / authority？
8. under which version / epoch？

---

# 12. Route Ranking Reversal

若在 $\chi_1$ 下：

$$
J_{\chi_1}(\mathcal R_A)
<
J_{\chi_1}(\mathcal R_B),
$$

但在 $\chi_2$ 下：

$$
J_{\chi_2}(\mathcal R_A)
>
J_{\chi_2}(\mathcal R_B),
$$

則稱為：

## Route Ranking Reversal

它可能來自：

- observer 變化；
- granularity 變化；
- resource budget 變化；
- scale 變化；
- risk policy 變化；
- world boundary 變化。

這種排名反轉不一定是矛盾，而可能只是條件集改變。

---

# 13. Feasible Before Optimal

本文提出：

$$
\boxed{
\text{Feasibility}
\rightarrow
\text{Optimality}.
}
$$

定義：

$$
\mathcal F_{\Xi}
=
\{
\mathcal R:
\operatorname{Legal}
\land
\operatorname{Authorized}
\land
\operatorname{GuardValid}
\land
\operatorname{ResourceFeasible}
\}.
$$

只在 $\mathcal F_{\Xi}$ 裡找 optimum。

這直接繼承 UNPNP Safe Reachable World。

---

# 14. Authorized Shortest Route

若 actor $a$ 具有 capability envelope $Cap_a$，則：

$$
\mathcal F_{\Xi,a}
\subseteq
\mathcal F_{\Xi}.
$$

因此：

$$
\boxed{
\mathcal R^*_{\Xi,a}
=
\arg\min_{\mathcal R\in\mathcal F_{\Xi,a}}
J_{\Xi}(\mathcal R).
}
$$

更快但未授權的 route 根本不應進入最佳化候選。

因此：

$$
\boxed{
\text{Reachable}
\neq
\text{Eligible}
\neq
\text{Authorized}
\neq
\text{Optimal}.
}
$$

---

# 15. Externalization 不能被偷偷忽略

若 route 之所以短，是因為：

- index 已建；
- model 已訓練；
- cache 已填；
- database 已整理；
- human 已標記；
- compiler 已預計算；

則 cost ledger 必須記錄：

$$
C_{\mathrm{externalized}}.
$$

否則會形成：

## False Shortest Route

表面：

$$
C_{\mathrm{online}}\approx1,
$$

實際：

$$
C_{\mathrm{total}}
\gg1.
$$

這與 UNPNP 的 Complexity Transfer 完全一致。

---

# 16. Online Shortest 不等於 Lifecycle Shortest

以 cache 為例，第一次：

$$
x
\rightarrow
f(x)
\rightarrow
y
$$

需要：

$$
C_{\mathrm{first}}
=
C_f+C_{\mathrm{store}}.
$$

未來 hit：

$$
x\rightarrow y
$$

可能只有：

$$
C_{\mathrm{hit}}.
$$

但完整 lifecycle：

$$
C_{\mathrm{life}}
=
C_f
+
C_{\mathrm{store}}
+
NC_{\mathrm{hit}}
+
C_{\mathrm{invalidate}}.
$$

因此：

$$
\boxed{
\text{online shortest}
\neq
\text{lifecycle shortest}.
}
$$

---

# 17. Route Geometry

Paper 01 已提出：

$$
\kappa
\in
\{
\text{point},
\text{line},
\text{jump-line},
\text{surface},
\text{cluster},
\text{field},
\text{recursive}
\}.
$$

因此 shortest route 不必永遠是「線最短」。

不同 geometry 可使用不同度量。

線可以用：

$$
L=\sum_iw_i.
$$

surface 可能更適合看：

$$
D_{\mathrm{critical}}.
$$

field 可能更自然地看：

$$
\int
\mathcal L(\phi,\dot\phi,t)\,dt.
$$

所以：

$$
\boxed{
\text{Route Metric}
=
\text{Geometry-Dependent}.
}
$$

---

# 18. Point、Line、Jump-Line、Surface、Cluster、Field

### Point

當某轉移已成 earned primitive，hop count 幾乎失去區分力，需轉看 lookup、guard、verification、update 與 provenance。

### Line

$$
a_1\rightarrow a_2\rightarrow\cdots\rightarrow a_n
$$

是傳統 shortest-path 最自然的情境。

### Jump-Line

$$
a_1\rightarrow a_{17}\rightarrow a_{230}\rightarrow a_{900}
$$

其價值可能來自 indexing、heuristic、semantic addressing 或 compiled hyperlink。

### Surface

大量獨立或弱依賴 operations 同步演化時：

$$
W\gg1,
\qquad
D\approx1.
$$

### Cluster

$$
K_1\rightarrow K_2\rightarrow K_3
$$

但每個 $K_i$ 內部又是一個 world。

所以：

$$
\boxed{
\text{inter-cluster length}
\neq
\text{intra-cluster work}.
}
$$

### Field

若系統以：

$$
\phi(x,t)
$$

演化，route 可能是 state-space trajectory：

$$
\gamma:t\mapsto\phi_t.
$$

所以：

$$
\boxed{
\text{UNPNP route}
\supset
\text{ordinary graph path}.
}
$$

---

# 19. Recursive Geometry

若一個 node：

$$
v^{(k)}
$$

本身展開為：

$$
\mathcal W^{(k-1)},
$$

route 可以：

$$
v_A^{(k)}
\rightarrow
\mathcal W_A^{(k-1)}
\rightarrow
\mathcal W_B^{(k-1)}
\rightarrow
v_B^{(k)}.
$$

因此：

> 一條宏觀 edge 的最短性，可能取決於內部微觀 world 的 route。

---

# 20. Micro-Shortest 與 Macro-Shortest 可能衝突

宏觀有：

$$
A\rightarrow B\rightarrow C.
$$

Route 1：

$$
A\rightarrow C
$$

宏觀只一 hop，但內部：

$$
W=10^6.
$$

Route 2：

$$
A\rightarrow B\rightarrow C
$$

宏觀兩 hop，但：

$$
W=10^3.
$$

因此：

$$
\boxed{
\text{macro hop shortest}
\neq
\text{micro work shortest}.
}
$$

---

# 21. Scale-Crossing Route

令 $R_{\downarrow}$ 表示 refinement， $R_{\uparrow}$ 表示 coarse-graining。

一條 route 可以：

$$
M
\xrightarrow{R_{\downarrow}}
\mu
\rightarrow
\mu'
\xrightarrow{R_{\uparrow}}
M'.
$$

所以 scale change 本身就是 route action，其成本：

$$
C_{\mathrm{scale-switch}}
$$

必須計入。

因此：

$$
\boxed{
C_{\mathrm{route}}
=
C_{\mathrm{within-scale}}
+
C_{\mathrm{scale-switch}}.
}
$$

---

# 22. Observer Switch 也有成本

從 $o_1$ 切換到 $o_2$ 可能需要：

- projection；
- translation；
- summarization；
- materialization；
- re-indexing；
- verification。

所以一般：

$$
C_{\mathrm{observer-switch}}>0.
$$

因此「換個角度看就變短」也不是免費操作。

---

# 23. Chart Transition

本文定義：

$$
\boxed{
T_{\chi}:
\chi_i
\rightarrow
\chi_j.
}
$$

這表示 UNPNP-II 不只 route world state，還可以 route：

$$
\boxed{
\text{representation regime}.
}
$$

完整運行因此不是只有：

$$
(s_0,s_1,\ldots,s_n),
$$

而是：

$$
\boxed{
\mathfrak R
=
((s_0,\chi_0),
(s_1,\chi_1),
\ldots,
(s_n,\chi_n)).
}
$$

本文稱為：

## Charted Computational Route

---

# 24. Chart 與 Route 聯合最佳化

若 chart 可變：

$$
\boxed{
\mathfrak R^*
=
\arg\min_{\mathfrak R}
J(
\mathfrak R
\mid
\mathbf W,
q,
B,
Risk
).
}
$$

更明確地：

$$
\boxed{
(\mathcal R^*,\chi^*)
=
\arg\min_{\mathcal R,\chi}
J(
\mathcal R,
\chi
\mid
\mathbf W,
q,
B,
Risk,
\mathcal H
).
}
$$

這已經同時包含：

- state routing；
- scale routing；
- representation routing；
- computational-form routing。

---

# 25. 24／72 Route

對每個 segment $r_i$，可以標記：

$$
p_i\in\mathfrak P_{24},
$$

以及：

$$
\lambda_i\in\mathfrak L_3.
$$

因此一條 route 可以是：

$$
P5^F
\rightarrow
P11^F
\rightarrow
P17^F
\rightarrow
P23^F.
$$

直觀上：

```text
sequential
→ selective jump
→ parallel
→ recognition / retrieval
```

所以最佳化不一定永遠是在單一算法範式內尋找。

因此：

$$
\boxed{
\text{Algorithm Selection}
\subset
\text{Computational Route Selection}.
}
$$

---

# 26. Path Compilation 會改變未來最短路

若：

$$
\Gamma:
B_1\rightarrow\cdots\rightarrow B_n
$$

被編譯：

$$
\operatorname{PC}(\Gamma)
=
\widehat{\ell}_{1,n},
$$

則：

$$
E_{t+1}
=
E_t
\cup
\{\widehat{\ell}_{1,n}\}.
$$

所以：

$$
\mathcal P_{t+1}
\neq
\mathcal P_t.
$$

今天最短的 route：

$$
\mathcal R_t^*
$$

明天可能因新 crystal 成為：

$$
\mathcal R_{t+1}^*
\neq
\mathcal R_t^*.
$$

不是因 task 改變，而是：

$$
\boxed{
\text{the computational world learned new routes}.
}
$$

---

# 27. History-Relative Shortest Route

完整 context 可以加入：

$$
\mathcal H_t.
$$

所以：

$$
\Xi_t
=
\langle
\mathbf W_t,
\partial W_t,
\chi_t,
q,
\mathcal H_t,
\mathcal F_t,
\mathbf C_t,
\omega_t,
\mathcal V_t
\rangle.
$$

於是：

$$
\boxed{
\mathcal R_t^*
=
\arg\min_{\mathcal R\in\mathcal F_t}
J_t(\mathcal R).
}
$$

因此：

$$
\boxed{
\text{Shortest Route}
=
\text{epoch-relative claim}.
}
$$

---

# 28. Shortest Route Certificate

第一版：

```text
ShortestRouteCertificate
- route_id
- world_boundary
- world_revision
- chart
- observer
- task_contract
- feasible_set_digest
- cost_vector
- objective
- comparison_set
- legality
- authorization
- verification
- epoch
- expiry
- fallback
```

沒有這些條件時，系統最好只說：

> currently preferred route

而不是：

> globally shortest route

---

# 29. Exact Shortest 與 Preferred Route

實際 AI Runtime 常不可能窮舉：

$$
\mathcal F.
$$

所以要區分：

$$
\boxed{
\mathcal R^*_{\mathrm{exact}}
}
$$

與：

$$
\boxed{
\widehat{\mathcal R}_{\mathrm{preferred}}.
}
$$

Adaptive Corridor 實際可能只 reveal：

$$
\widehat{\mathcal F}_t
\subseteq
\mathcal F_t.
$$

因此：

$$
\widehat{\mathcal R}_t
=
\arg\min_{\mathcal R\in\widehat{\mathcal F}_t}
J_t(\mathcal R)
$$

不能自動推出：

$$
\widehat{\mathcal R}_t
=
\mathcal R_t^*.
$$

所以 UNPNP 更適合使用：

$$
\boxed{
\text{best validated route under current revealed world}.
}
$$

---

# 30. Exploration Cost 與 Stop Rule

若要 reveal 更多候選 route，必須支付：

$$
C_{\mathrm{explore}}.
$$

因此存在：

$$
\boxed{
\text{route quality}
\leftrightarrow
\text{search cost}.
}
$$

若繼續探索的預期收益：

$$
E[\Delta J]
$$

低於：

$$
C_{\mathrm{explore}},
$$

則：

$$
\boxed{
\operatorname{StopExplore}=1.
}
$$

這讓 Adaptive Corridor 不必窮舉所有可能 route。

---

# 31. Route Regret

若系統選擇：

$$
\widehat{\mathcal R}
$$

而真正 optimum 是：

$$
\mathcal R^*,
$$

定義：

$$
\boxed{
\operatorname{Regret}
=
J(\widehat{\mathcal R})
-
J(\mathcal R^*).
}
$$

實際系統可能只能估計 regret upper bound。

因此更實用的是 bounded revealed optimum：

$$
\boxed{
\widehat{\mathcal R}_B^*
=
\arg\min_{\mathcal R\in\widehat{\mathcal F}_B}
J(\mathcal R).
}
$$

---

# 32. 與 MWT 的關係

MWT 強調：

$$
\mathbf W
$$

不等於任何 presentation。

因此 shortest route 是對：

$$
\rho_{\chi,O,t}(\mathbf W)
$$

的 route claim，並不是對 World primitive 本身宣稱絕對最短。

所以：

$$
\boxed{
\text{Shortest route belongs to a world presentation, not to World-in-itself}.
}
$$

---

# 33. 與 GCM 的關係

GCM 定義：

$$
\Phi_G
=
\operatorname{Compose}_{\mathcal C_G}
(
\Phi_1,
\ldots,
\Phi_n
).
$$

不同 domain 可以使用不同 computational forms。

因此 route optimization 必須遵守：

$$
\mathcal C_G.
$$

局部最快 route 如果破壞全域 invariant：

$$
\operatorname{Coherent}_W=0,
$$

就不能被選。

因此：

$$
\boxed{
\sum \text{local shortest}
\neq
\text{global shortest}.
}
$$

---

# 34. 非交換歷史

若：

$$
A\circ B
\neq
B\circ A,
$$

則：

$$
A\rightarrow B
$$

與：

$$
B\rightarrow A
$$

即使 endpoint 相同，history cost / legality 也可能不同。

因此：

$$
\boxed{
\text{same endpoint}
\neq
\text{same route semantics}.
}
$$

Shortest route 必須保留 history / provenance，而不能只比較終態。

---

# 35. Route Equivalence

本文暫定：

$$
\mathcal R_1
\simeq_{\Xi}
\mathcal R_2
$$

當它們在 $\Xi$ 指定的 relevant invariants 上等價。

若 observer、task 或 risk context 改變，完全可能：

$$
\mathcal R_1
\not\simeq_{\Xi'}
\mathcal R_2.
$$

因此 route equivalence 本身也是 context-relative，但不是任意。

---

# 36. Invariant-Preserving Chart Transition

令：

$$
I_q
$$

為任務相關 invariants。

若：

$$
T_{\chi}:
\chi_i
\rightarrow
\chi_j,
$$

至少要求：

$$
\boxed{
I_q(
U_{\chi_i}(\mathcal C)
)
\simeq
I_q(
U_{\chi_j}(\mathcal C)
).
}
$$

否則 chart switch 可能只是偷偷換了問題。

---

# 37. Projection-Induced False Shortest

如果 coarse chart $\chi_c$ 把關鍵 side effect 壓掉，可能得到：

$$
J_{\chi_c}(\mathcal R_A)
<
J_{\chi_c}(\mathcal R_B),
$$

但 fine chart 發現：

$$
R_A\gg R_B.
$$

本文稱為：

## Projection-Induced False Shortest

因此粗尺度 route 必須考慮：

$$
L_O
$$

即 observation / projection loss。

---

# 38. Resolution Debt

若 route 為了快速決策而保持粗解析度，可累積：

$$
D_{\mathrm{resolution}}.
$$

當：

$$
D_{\mathrm{resolution}}
>
\theta_D,
$$

必須：

$$
R_{\downarrow}.
$$

也就是重新把世界看細。

這使 coarse-grained shortest route 不會永久遮蔽低層異常。

---

# 39. 最短路徑可以故意不是最短

在探索、學習、驗證階段，系統可能故意選：

$$
J(\mathcal R_E)
>
J(\mathcal R^*)
$$

因為：

$$
B_{\mathrm{information}}(\mathcal R_E)
$$

更大。

因此：

$$
\boxed{
\text{Exploration Route}
\neq
\text{Execution Route}.
}
$$

可加入 information gain：

$$
J
=
C
-
\beta I.
$$

當系統不確定時，較長 route 可能更值得，因為它降低未來不確定性。

---

# 40. 最短與最可結晶也不同

某 route $\mathcal R_A$ 單次最便宜，但非常不穩定；另一條 $\mathcal R_B$ 稍貴，但可高度重用。

則 lifecycle utility 可能：

$$
U_H(\mathcal R_B)
>
U_H(\mathcal R_A).
$$

因此：

$$
\boxed{
\text{single-run optimum}
\neq
\text{crystallization optimum}.
}
$$

可以定義 future-aware objective：

$$
\boxed{
J_{\mathrm{future}}
=
C_{\mathrm{now}}
-
\eta B_{\mathrm{reuse}}
+
C_{\mathrm{compile}}
+
C_{\mathrm{maintain}}.
}
$$

這直接接回 EHPE。

---

# 41. Crystallization 是 Future Route-Space Mutation

一條 route 只有在：

$$
\mathcal R
\simeq
\widehat{\ell}
$$

且：

$$
J(\widehat{\ell})
<
J(\mathcal R)
$$

時，Path Compilation 才具有實際意義。

結晶後：

$$
\widehat{\ell}
\rightarrow
\kappa
$$

會把新的 route 或 primitive 加入未來搜尋空間。

所以：

$$
\boxed{
\text{Crystallization}
=
\text{future route-space mutation}.
}
$$

---

# 42. Dynamic Shortest-Route Loop

$$
\boxed{
\text{Route Search}
\rightarrow
\text{Execution}
\rightarrow
\text{Verification}
\rightarrow
\text{Compilation}
\rightarrow
\text{Crystallization}
\rightarrow
\text{New Route Space}
\rightarrow
\text{Route Search}.
}
$$

這意味著 shortest route 不是一次性的靜態結果，而是 runtime history 的函數。

---

# 43. 四種 Shortest-Route 問題

### Type I｜Fixed-Graph Shortest Path

 $G$ 與 $w$ 固定。

### Type II｜Adaptive Route Selection

 $G_t$ 可 reveal，但 topology 不改。

### Type III｜Route-Space Rewriting

$$
G_{t+1}\neq G_t
$$

因 compilation / crystallization 產生新 transition。

### Type IV｜Chart-and-Route Co-Optimization

不只：

$$
G_{t+1}\neq G_t,
$$

甚至：

$$
\chi_{t+1}\neq\chi_t.
$$

UNPNP-I 主要研究 Type II–III；UNPNP-II 正式進入 Type IV。

---

# 44. 完整研究問題

不再只是：

$$
\min_{\Gamma}C(\Gamma).
$$

而是：

$$
\boxed{
\min_{\chi,\mathcal R,p,\lambda}
J(
\chi,
\mathcal R,
p,
\lambda
\mid
\mathbf W,
q,
B,
Risk,
\mathcal H
).
}
$$

其中 $p$ 來自 computational form space， $\lambda$ 來自 transition-law family。

這是本文提出的：

## World-Relative Computational Route Optimization

雛形。

---

# 45. 不要把這誤讀成「萬物都可任意換表示」

Chart transition 必須有：

- semantics preservation；
- bridge；
- validation；
- cost；
- provenance。

所以：

$$
\chi_i\rightarrow\chi_j
$$

不是免費 re-labeling。

任何因「換一個說法」而產生的表面縮短，如果沒有 execution、verification 或 lifecycle 的實際改善，都不能宣稱為 computational shortest-route improvement。

---

# 46. Effective Computational Diameter

給定 $\Xi$，定義：

$$
\boxed{
\operatorname{ECD}_{\Xi}(W)
=
\sup_{s,g}
d_{\Xi}(s,g),
}
$$

其中 $d_{\Xi}$ 為 context-relative route cost。

若 crystallization 成功：

$$
\operatorname{ECD}_{\Xi,t+1}(W)
<
\operatorname{ECD}_{\Xi,t}(W)
$$

可能成立。

這表示：

> 對同一個 Runtime 而言，世界的有效計算直徑真的縮短了。

但：

$$
\boxed{
\text{effective computational distance}
\neq
\text{physical distance}.
}
$$

物理世界不會因一個 hyperlink 而免費消失。

---

# 47. Hyperlink 的重新定位

Hyperlink：

$$
\ell:
(\mathcal B_i,s_i)
\rightarrow
(\mathcal B_j,s_j)
$$

不是消滅物理成本，而是建立：

$$
\boxed{
\text{addressable transition abstraction}.
}
$$

它可能降低：

- search；
- coordination；
- reasoning；
- navigation；
- intermediate materialization；

但其他成本仍必須進 ledger。

---

# 48. 最短路徑必須說清楚「短在哪裡」

本文建議工程系統使用：

```text
shortest-by-hop
shortest-by-work
shortest-by-depth
shortest-by-latency
shortest-by-lifecycle-cost
shortest-by-risk-adjusted-cost
Pareto-preferred
currently-preferred
```

避免脫離 qualifier 的：

```text
shortest
```

---

# 49. 五條核心定律

第一：

$$
\boxed{
\textbf{
There is no shortest route without a declared route metric.
}
}
$$

第二：

$$
\boxed{
\textbf{
There is no route metric without a declared computational chart.
}
}
$$

因此：

$$
\boxed{
\text{Shortest}
\Rightarrow
\text{Metric}
\Rightarrow
\text{Chart}.
}
$$

第三：

$$
\boxed{
\textbf{
Local shortest routes do not generally compose into a global shortest route.
}
}
$$

第四：

$$
\boxed{
\textbf{
A route may become shorter because the computational world has changed, not because the task has changed.
}
}
$$

第五：

$$
\boxed{
\textbf{
Relative optimality is conditional, not arbitrary.
}
}
$$

---

# 50. 對 UNPNP 的重新表述

UNPNP-I：

> 發現、建立、編譯與結晶有效跨底空間路徑。

UNPNP-II：

> 在多尺度、多觀察者、多幾何與多計算配置世界中，同時決定「什麼叫一步」以及「哪一條 route 在當前條件下值得被稱為最優」。

因此：

$$
\boxed{
\text{UNPNP-II}
=
\text{Route-Space}
+
\text{Chart-Space}
+
\text{World-Relative Optimization}.
}
$$

---

# 51. 與 Paper 03 的接口

本文已經指出：

- point；
- line；
- jump-line；
- surface；
- cluster；
- field；
- recursive geometry；

不能共享單一 naive path metric。

下一篇因此正式處理：

## Paper 03｜點、線、歪線、面、叢集與場
### Computational Dependency Geometry Beyond Ordinary Graph Paths

它將回答：

> **當計算本身不再是一條線時，「路徑」究竟應該被廣義化成什麼數學對象？**

---

# 結論

「最短路徑」不是錯誤概念。

真正的問題是，人們太容易省略它成立所依賴的條件。

當 computational unit、scale、observer、world boundary、route geometry、computational form、transition law 與 lifecycle 都可能動態改變時，沒有下標的：

$$
\Gamma^*
$$

已不足以描述 AI-native runtime。

本文因此提出：

$$
\boxed{
\mathcal R^*_{\Xi}
=
\arg\min_{\mathcal R\in\mathcal F_{\Xi}}
J_{\Xi}(\mathcal R)
}
$$

以及在不可合理標量化時：

$$
\boxed{
\mathfrak P^*_{\Xi}
=
\operatorname{ParetoMin}
\mathbf C_{\Xi}.
}
$$

更進一步，當 chart 也可以被 Runtime 選擇：

$$
\boxed{
(\mathcal R^*,\chi^*)
=
\arg\min_{\mathcal R,\chi}
J(
\mathcal R,
\chi
\mid
\mathbf W,
q,
B,
Risk,
\mathcal H
).
}
$$

因此最終命題不是：

> 世界上存在一條脫離條件的絕對最短路徑。

而是：

$$
\boxed{
\textbf{
最短路徑是一個相對於世界邊界、計算尺度、觀察者、表示、合法域與成本語義的條件式最優命題。
}
}
$$

而當 Runtime 可以改寫 route space、產生新 hyperlink、結晶新 primitive 並切換 computational chart 時，研究問題更進一步變成：

$$
\boxed{
\textbf{
不是只在世界中尋找最短路，
而是持續改變未來「最短」可以成立的計算世界。
}
}
$$
