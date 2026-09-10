# UNPNP-II / Multi-Scale Computational Geometry — Paper 04
## 時間不等於路長
### State Distance, Causal Depth, Temporal Order, Parallel Depth, and the Separation of Computational Histories

**系列名稱：** UNPNP-II｜Multi-Scale Computational Geometry  
**系列中文名：** UNPNP 第二層：多尺度計算幾何與相對最短路徑  
**篇次：** Paper 04 / 08  
**作者：** Neo.K with Aletheia（GPT）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-08  
**文件性質：** 計算時間論／因果結構／多尺度路徑論／UNPNP 擴充論文  
**前置：** Paper 01《計算的一到底是什麼？》；Paper 02《最短路徑不存在於真空中》；Paper 03《點、線、歪線、面、叢集與場》  
**狀態：** Canonical Draft

---

## 摘要

UNPNP-II Paper 01 已指出，計算中的「一步」不是天然原子；Paper 02 進一步指出，最短路徑必須相對 computational chart、observer、World boundary 與 objective；Paper 03 則將普通 graph path 擴張成可包含 point、line、jump-line、surface、cluster、field 與 recursive geometry 的 Computational Route Object。

本文處理下一個無法再被省略的問題：

> **時間、因果、工作量、狀態變化與幾何距離，到底是不是同一件事？**

答案是否定的。

假設存在十個彼此獨立的 operation：

$$
a_1,\ldots,a_{10}.
$$

若它們能在同一 parallel layer 中執行，則可能同時有：

$$
W=10,
$$

$$
D_C=1,
$$

$$
H_O=1,
$$

以及：

$$
T_{\mathrm{wall}}=\Delta t,
$$

其中：

- $W$：總工作量；
- $D_C$：因果深度；
- $H_O$：某 observer 所看到的高層 hop；
- $T_{\mathrm{wall}}$：實際 wall-clock 時間。

所以：

$$
\boxed{
10
\neq
1
\neq
\Delta t
}
$$

並不存在矛盾，因為三者回答不同問題。

本文提出第一版 **Computational Temporal-Causal Frame**：

$$
\boxed{
\Theta
=
\langle
\mathcal E,
\preceq_C,
\tau,
\delta_S,
\delta_G,
W,
D,
\mathcal H,
O
\rangle
}
$$

其中：

- $\mathcal E$：events / operations；
- $\preceq_C$：causal partial order；
- $\tau$：time assignment；
- $\delta_S$：state distance；
- $\delta_G$：geometric / route distance；
- $W$：work measure；
- $D$：causal / parallel depth；
- $\mathcal H$：history；
- $O$：observer projection。

本文正式提出：

$$
\boxed{
d_S
\neq
d_C
\neq
d_T
\neq
d_G
}
$$

其中：

- $d_S$：state distance；
- $d_C$：causal distance；
- $d_T$：temporal distance；
- $d_G$：computational geometry distance。

此外，本文將時間至少區分為：

$$
\boxed{
T_{\mathrm{physical}},
T_{\mathrm{wall}},
T_{\mathrm{event}},
T_{\mathrm{logical}},
T_{\mathrm{causal}},
T_{\mathrm{observer}}
}
$$

並指出它們不應被偷偷當成同一軸。

本文同時將 GCM 的 noncommutative global evolution、MWT 的 history-first world semantics，以及 UNPNP 的 route compilation / crystallization 接入同一框架：兩條路即使得到相同 endpoint，也可能因歷史、順序、不可逆副作用、權限與能量消耗不同而不等價。

因此：

$$
\boxed{
\text{State Equality}
\not\Rightarrow
\text{History Equality}.
}
$$

而：

$$
\boxed{
\text{Same Endpoint}
\not\Rightarrow
\text{Same Computation}.
}
$$

本文最後提出，任何 AI-native shortest-route system 都必須同時記錄：

- total work；
- critical / causal depth；
- elapsed time；
- state displacement；
- geometry traversal；
- history / provenance。

否則「路徑變短」可能只是把某一種距離壓縮，卻把成本轉移到另一種時間、因果或歷史維度。

---

# 1. 十個 Operation 到底算一還是十？

考慮：

$$
a_1,a_2,\ldots,a_{10}.
$$

如果它們彼此沒有依賴：

$$
a_i\parallel a_j,
\qquad
i\neq j,
$$

則可以同時執行。

此時：

$$
\boxed{
W=10.
}
$$

但 critical / causal depth：

$$
\boxed{
D_C=1.
}
$$

對上層 observer：

$$
\boxed{
H_O=1
}
$$

也可能成立。

因此同一 execution 可以同時被描述成：

$$
\boxed{
(W,D_C,H_O)
=
(10,1,1).
}
$$

---

# 2. 這不是語言遊戲

三個值分別回答：

### Work

> 總共做了多少計算？

### Causal Depth

> 最長不可並行依賴鏈有多深？

### Observer Hop

> 在目前抽象層，觀察者看見幾個高層 action？

它們本來就不是同一個量。

---

# 3. Wall-Clock 又是第四個量

假設十個 operation 在十個 worker 上同時執行，每個耗時：

$$
10\text{ ms}.
$$

則：

$$
W=10
$$

但：

$$
T_{\mathrm{wall}}
\approx10\text{ ms}
$$

而不是：

$$
100\text{ ms}.
$$

所以：

$$
\boxed{
\text{work}
\neq
\text{elapsed time}.
}
$$

---

# 4. State Distance 又是第五個量

兩個 state：

$$
s_0,
s_1
$$

之間的變化大小可能：

$$
d_S(s_0,s_1)\gg1
$$

即使它只由一次 high-level transition 造成。

例如：

```text
reset_world()
```

表面是一個 call，

但可以一次改變大量 state components。

所以：

$$
\boxed{
\text{small hop count}
\not\Rightarrow
\text{small state displacement}.
}
$$

---

# 5. Geometric Distance 又不同

在 Paper 03 中，route geometry 可以是：

$$
\mathsf{Ln},
\mathsf{Jl},
\mathsf{Sf},
\mathsf{Cl},
\mathsf{Fd},
\mathsf{Rc}.
$$

因此：

$$
d_G
$$

描述的是：

> 在指定 dependency geometry 下，從一個 computational configuration 到另一個 configuration 的 route distance。

它不是 state-space difference，也不是 wall-clock。

---

# 6. 四距離分離

本文正式定義：

$$
\boxed{
d_S
\neq
d_C
\neq
d_T
\neq
d_G.
}
$$

一般情況下不應將它們等同。

---

# 7. State Distance $d_S$

令：

$$
s_i,s_j\in\mathcal S.
$$

定義：

$$
\boxed{
d_S(s_i,s_j)
}
$$

表示狀態差異。

具體 metric 可依 domain 選擇：

- Hamming；
- Euclidean；
- edit distance；
- graph edit；
- semantic distance；
- Wasserstein；
- domain-specific invariant distance。

---

# 8. Causal Distance $d_C$

給定 causal partial order：

$$
\preceq_C,
$$

定義：

$$
\boxed{
d_C(e_i,e_j)
}
$$

為從事件 $e_i$ 到 $e_j$ 的最小必要 causal depth 或 dependency depth。

---

# 9. Temporal Distance $d_T$

定義：

$$
\boxed{
d_T(e_i,e_j)
=
|\tau(e_j)-\tau(e_i)|.
}
$$

但：

$$
\tau
$$

本身可以是不同時間語義。

這會在後面細分。

---

# 10. Geometric Distance $d_G$

$$
\boxed{
d_G(x,y\mid g,\chi)
}
$$

表示指定 geometry $g$ 與 chart $\chi$ 下的 route distance。

不同 geometry 可有不同 metric。

---

# 11. 同 State Distance，不代表同 Causal Distance

兩條 execution：

$$
\mathcal R_A,
\mathcal R_B
$$

都從：

$$
s_0
$$

到：

$$
s_f.
$$

所以：

$$
d_S^A=d_S^B.
$$

但可能：

$$
d_C^A\neq d_C^B.
$$

---

# 12. 同 Causal Depth，不代表同 Work

兩個 parallel system：

$$
D_C^A=D_C^B=3,
$$

但：

$$
W_A=100,
$$

$$
W_B=10^6.
$$

因此：

$$
\boxed{
\text{depth equality}
\not\Rightarrow
\text{work equality}.
}
$$

---

# 13. 同 Wall-Clock，不代表同 Work

CPU A：

$$
W_A=100
$$

耗：

$$
10\text{ ms}.
$$

GPU B：

$$
W_B=10^6
$$

也可能耗：

$$
10\text{ ms}.
$$

所以：

$$
\boxed{
T_A=T_B
\not\Rightarrow
W_A=W_B.
}
$$

---

# 14. 同 Hop，不代表同 Time

兩個 API 都是一 call：

$$
H_A=H_B=1.
$$

但：

$$
T_A=1\text{ ms},
$$

$$
T_B=60\text{ s}.
$$

所以：

$$
\boxed{
\text{interface topology}
\neq
\text{temporal cost}.
}
$$

---

# 15. Temporal-Causal Frame

本文提出：

$$
\boxed{
\Theta
=
\langle
\mathcal E,
\preceq_C,
\tau,
\delta_S,
\delta_G,
W,
D,
\mathcal H,
O
\rangle.
}
$$

它不是 World 本身，而是對 computation 的 temporal-causal presentation。

---

# 16. Event Set $\mathcal E$

$$
\mathcal E
=
\{e_1,\ldots,e_n\}.
$$

每個 event 可以是：

- instruction；
- function；
- transaction；
- message；
- state transition；
- field update；
- agent action；
- crystal invocation。

---

# 17. Causal Partial Order $\preceq_C$

若：

$$
e_i\preceq_C e_j,
$$

表示：

> $e_j$ 的合法發生依賴 $e_i$。

不要求每一對 event 都可比較。

---

# 18. Concurrency

若：

$$
e_i\npreceq_C e_j
$$

且：

$$
e_j\npreceq_C e_i,
$$

可記為：

$$
e_i\parallel_C e_j.
$$

這表示 causal independence 或至少目前沒有已知 causal ordering。

---

# 19. Parallel 不等於同時

兩個 event 即使 causal-independent：

$$
e_i\parallel_C e_j,
$$

實際硬體也可能因 resource constraint 先後執行。

所以：

$$
\boxed{
\text{causal concurrency}
\neq
\text{physical simultaneity}.
}
$$

---

# 20. 同時也不等於無因果

某些同步系統中，兩個 observable event 可能在同一 clock tick 出現，但其中一個依賴前一 micro-phase 的結果。

所以：

$$
\boxed{
\text{same timestamp}
\not\Rightarrow
\text{causal independence}.
}
$$

---

# 21. 第一種時間：Physical Time

$$
\boxed{
T_{\mathrm{physical}}
}
$$

指實際物理載體中的時間演化。

可能包含：

- signal propagation；
- clock cycle；
- network latency；
- mechanical delay；
- sensor delay。

---

# 22. 第二種時間：Wall-Clock Time

$$
\boxed{
T_{\mathrm{wall}}
}
$$

從外部計時器看：

$$
t_{\mathrm{end}}-t_{\mathrm{start}}.
$$

這是 benchmark 常見量。

---

# 23. 第三種時間：Event Time

$$
\boxed{
T_{\mathrm{event}}
}
$$

指資料或世界事件本身的 timestamp。

在 stream system 中，event time 與 processing time 可以不同。

---

# 24. 第四種時間：Logical Time

$$
\boxed{
T_{\mathrm{logical}}
}
$$

例如 Lamport-style logical ordering。

它不必與 physical seconds 同構。

---

# 25. 第五種時間：Causal Time

$$
\boxed{
T_{\mathrm{causal}}
}
$$

只保留：

> 哪些事件必須先於哪些事件？

它更接近 partial order 而不是單一 scalar clock。

---

# 26. 第六種時間：Observer Time

$$
\boxed{
T_{\mathrm{observer}}
}
$$

不同 observer 可能以不同 sampling rate、frame rate、context window 或 event aggregation 看同一世界。

---

# 27. 六種時間不應混用

因此：

$$
\boxed{
T_{\mathrm{physical}},
T_{\mathrm{wall}},
T_{\mathrm{event}},
T_{\mathrm{logical}},
T_{\mathrm{causal}},
T_{\mathrm{observer}}
}
$$

應分開。

---

# 28. Observer 可以把很多時間步壓成一個

例如 UI 每秒只刷新一次：

$$
\Pi_O
:
\{e_1,\ldots,e_{10^6}\}
\rightarrow
\text{one frame}.
$$

所以：

$$
\boxed{
T_{\mathrm{observer}}
\ll
\text{internal event count}.
}
$$

---

# 29. 這會產生 Temporal Coarse-Graining

定義：

$$
\boxed{
R_{\uparrow}^{T}
:
\{e_i\}_{i=t_0}^{t_1}
\rightarrow
E^{(k+1)}.
}
$$

多個 micro events 被聚成一個 macro temporal unit。

---

# 30. Temporal Refinement

反之：

$$
\boxed{
R_{\downarrow}^{T}
:
E^{(k+1)}
\rightarrow
\{e_1,\ldots,e_n\}^{(k)}.
}
$$

Debug 或 audit 時重新展開時間。

---

# 31. Temporal Unit 也是 Chart-Relative

因此：

$$
1_{\mathrm{frame}}
\neq
1_{\mathrm{tick}}
\neq
1_{\mathrm{transaction}}
\neq
1_{\mathrm{epoch}}.
$$

跟 Paper 01 的 unitization 完全一致。

---

# 32. Work

定義：

$$
\boxed{
W(\mathcal R)
=
\sum_{e\in\mathcal R}
w(e).
}
$$

最簡單情況每 event 權重為 1。

---

# 33. Causal Depth

若 causal DAG 為：

$$
G_C,
$$

則：

$$
\boxed{
D_C(\mathcal R)
=
\max_{\gamma_C}
|\gamma_C|.
}
$$

即最長必要依賴鏈。

---

# 34. Parallel Width

定義：

$$
\boxed{
P_W
=
\max_t
|\mathcal E_t^{\parallel}|.
}
$$

表示最大同時可執行寬度。

---

# 35. Work–Depth Pair

對 parallel computation：

$$
\boxed{
(W,D_C)
}
$$

通常比：

$$
H
$$

更有意義。

---

# 36. Critical Path

若每 event 有 duration：

$$
c_t(e),
$$

則 critical path：

$$
\boxed{
C_{\mathrm{crit}}
=
\max_{\gamma_C}
\sum_{e\in\gamma_C}
c_t(e).
}
$$

理想無額外 overhead 時：

$$
T_{\mathrm{wall}}
\ge
C_{\mathrm{crit}}.
$$

---

# 37. Wall-Clock 還包含 Scheduling Overhead

所以：

$$
T_{\mathrm{wall}}
=
C_{\mathrm{crit}}
+
C_{\mathrm{schedule}}
+
C_{\mathrm{sync}}
+
C_{\mathrm{queue}}
+
C_{\mathrm{IO}}
+\cdots
$$

不應只看 DAG depth。

---

# 38. Geometry Depth 與 Causal Depth 也不同

一條 graph：

$$
v_1\rightarrow v_2\rightarrow v_3
$$

幾何 hop 為 2。

但如果：

$$
v_2
$$

本身是一個 parallel surface，

其 causal depth 可能：

$$
D_C\gg2
$$

或：

$$
D_C\approx2
$$

視內部結構而定。

---

# 39. Recursive Geometry 讓 Depth 變成多層量

可以定義：

$$
D_C^{(k)}
$$

表示第 $k$ 層 causal depth。

因此：

$$
\boxed{
D_C
=
\{D_C^{(k)}\}_{k\in\Sigma}.
}
$$

不是永遠只一個 scalar。

---

# 40. Macro Depth

對高層 observer：

$$
D_C^{(M)}=3
$$

可能成立。

---

# 41. Micro Depth

但展開每個 macro unit 後：

$$
D_C^{(\mu)}=10^4.
$$

兩者都合法。

---

# 42. Cross-Scale Critical Path

完整 critical path 可能跨尺度：

$$
M_1
\rightarrow
\mu_{1,1}
\rightarrow
\mu_{1,2}
\rightarrow
M_2
\rightarrow
\cdots
$$

因此需要：

$$
\boxed{
C_{\mathrm{crit}}^{\mathrm{cross-scale}}.
}
$$

---

# 43. 時間不是一定單調對應「進度」

某些計算長時間等待 I/O：

$$
T_{\mathrm{wall}}\uparrow
$$

但：

$$
W
$$

幾乎不變。

所以：

$$
\boxed{
\text{elapsed time}
\neq
\text{computational progress}.
}
$$

---

# 44. 計算很多也可能狀態不變

例如驗證：

$$
f(s)=s
$$

或大量 search 最後沒有 commit。

則：

$$
W\gg0
$$

但：

$$
d_S(s_0,s_f)=0.
$$

所以：

$$
\boxed{
\text{work}
\not\Rightarrow
\text{state displacement}.
}
$$

---

# 45. 狀態變很多也可能 Work 很小

例如：

```text
load_snapshot()
```

可能一次將整個 world state 替換。

在 high-level unit 下：

$$
W_{\mathrm{surface}}\approx1
$$

但：

$$
d_S\gg1.
$$

---

# 46. 因果鏈很長，狀態變化可以很小

例如 iterative convergence：

$$
x_0\rightarrow x_1\rightarrow\cdots\rightarrow x_n
$$

每一步：

$$
d_S(x_i,x_{i+1})\ll1,
$$

但：

$$
D_C=n.
$$

---

# 47. 狀態距離大，因果深度也可以小

一個 parallel transform：

$$
X\rightarrow X'
$$

可一次更新大量 coordinates。

所以：

$$
d_S(X,X')\gg1,
$$

但：

$$
D_C=1.
$$

---

# 48. History

令：

$$
\boxed{
\mathcal H
=
(e_1,e_2,\ldots,e_n;\preceq_C,\tau,\rho)
}
$$

表示 execution history。

其中：

$$
\rho
$$

可包含 provenance / receipt。

---

# 49. History 不是單純 Log

History 需要保存：

- order；
- causal relation；
- actor；
- version；
- side effects；
- observations；
- validations；
- irreversible events。

---

# 50. State Equality 不等於 History Equality

若：

$$
s_f^{A}=s_f^{B},
$$

仍可能：

$$
\boxed{
\mathcal H_A\neq\mathcal H_B.
}
$$

---

# 51. 例：先扣款再退款 vs 從未扣款

兩者最終餘額可能相同：

$$
s_f^A=s_f^B.
$$

但：

$$
\mathcal H_A\neq\mathcal H_B.
$$

所以不能因 endpoint 相同就說 route 等價。

---

# 52. 例：Delete + Restore

最終檔案內容可以相同，

但 delete 事件本身可能觸發：

- audit；
- notification；
- retention；
- external side effect。

因此：

$$
\boxed{
\text{state restoration}
\neq
\text{history erasure}.
}
$$

---

# 53. Noncommutativity

若：

$$
A\circ B
\neq
B\circ A,
$$

則 order 本身改變結果。

因此：

$$
\boxed{
\text{history order is computational state}.
}
$$

---

# 54. 即使交換，成本也可能不交換

有時：

$$
A\circ B(s)
=
B\circ A(s)
$$

在 endpoint 上相同，

但：

$$
C(A\circ B)
\neq
C(B\circ A).
$$

所以 cost history 也重要。

---

# 55. History-Sensitive Route Equivalence

定義：

$$
\boxed{
\mathcal R_A
\simeq_{\Xi,\mathcal H}
\mathcal R_B
}
$$

只有當 relevant endpoint invariants、history obligations 與 side-effect semantics 都相容。

---

# 56. Endpoint Equivalence 是較弱關係

$$
\mathcal R_A
\simeq_{\mathrm{end}}
\mathcal R_B
$$

只表示終態相同。

通常：

$$
\boxed{
\simeq_{\Xi,\mathcal H}
\Rightarrow
\simeq_{\mathrm{end}}
}
$$

但反向不成立。

---

# 57. Path Compilation 必須尊重 History Semantics

若原始：

$$
\Gamma
=
A\rightarrow B\rightarrow C
$$

要編譯成：

$$
\widehat{\ell},
$$

不能只驗：

$$
s_f(\Gamma)
=
s_f(\widehat{\ell}).
$$

還需驗：

- required events；
- audit；
- authorization；
- irreversible effects；
- temporal constraints。

---

# 58. Temporal Equivalence

定義：

$$
\boxed{
\mathcal R_A
\simeq_T
\mathcal R_B
}
$$

表示在指定 task contract 中，兩者 temporal obligations 等價。

例如：

- deadline；
- timeout；
- order；
- freshness；
- synchronization。

---

# 59. Causal Equivalence

$$
\boxed{
\mathcal R_A
\simeq_C
\mathcal R_B
}
$$

表示 relevant causal dependencies 被保留。

---

# 60. State Equivalence

$$
\boxed{
\mathcal R_A
\simeq_S
\mathcal R_B.
}
$$

---

# 61. Full Route Equivalence

第一版：

$$
\boxed{
\mathcal R_A
\simeq_{\mathrm{route}}
\mathcal R_B
}
$$

至少需要指定哪些：

$$
\{
S,C,T,G,H
\}
$$

invariants 必須保留。

---

# 62. 不同任務要求不同 Equivalence

對 pure lookup：

$$
S
$$

可能最重要。

對 financial transaction：

$$
H,C,T
$$

都很重要。

對 simulation：

$$
T,G
$$

可能很重要。

所以：

$$
\boxed{
\text{route equivalence is task-relative}.
}
$$

---

# 63. 時間與 24／72 的關係

24／72 中：

- sequential；
- jump；
- parallel；
- recognition；

描述 update organization。

它們會影響：

$$
D_C,
W,
T.
$$

但不等同某個固定時間複雜度。

---

# 64. Sequential 不等於慢

一條 sequence：

$$
\mathsf S
$$

如果只有三步，

可以比一個巨大 parallel surface 更快。

所以：

$$
\boxed{
\mathsf S
\neq
\text{slow}.
}
$$

---

# 65. Parallel 不等於少工作

$$
\mathsf P
$$

通常改變：

$$
D_C,
T_{\mathrm{wall}}
$$

但不必降低：

$$
W.
$$

---

# 66. Recognition 不等於零時間

$$
\mathsf R
$$

可以是零搜尋展開，

但：

$$
T_{\mathrm{online}}
\ge
\Omega(1)
$$

在標準物理模型下仍成立。

---

# 67. Jump 不等於少因果

跳躍 addressing 可以減少 traversal hop，

但 resolve / verify / boundary crossing 可能形成新的 causal chain。

---

# 68. Transition Law 與時間

72 格中的：

$$
F,K,Q
$$

也可能帶不同 temporal semantics。

---

# 69. Deterministic Transition

$$
x_{t+1}=F(x_t).
$$

時間順序通常可明確建模。

---

# 70. Stochastic Kernel

$$
x_{t+1}\sim K(\cdot\mid x_t).
$$

除了時間，還要記：

- random seed；
- sample path；
- distribution history。

---

# 71. Quantum-Like Transition

若使用 quantum channel-like semantics，

需要保留：

- operation ordering；
- measurement events；
- noncommutativity；
- branch / outcome record。

---

# 72. 因此 Time Frame 也是 Local Configuration

不同 domain：

$$
D_i
$$

可以使用不同：

$$
\Theta_i.
$$

GCM 不要求全世界共享同一 clock semantics。

---

# 73. Global Time 不等於 One Clock Everywhere

因此：

$$
\boxed{
\text{Global Temporal Coherence}
\neq
\text{One Global Scalar Clock}.
}
$$

---

# 74. Global Temporal Coherence

更準確：

$$
\boxed{
\text{Global Temporal Coherence}
=
\text{consistent composition of local temporal / causal frames}.
}
$$

---

# 75. Cross-Domain Clock Bridge

若：

$$
D_i
$$

與：

$$
D_j
$$

有不同 clocks，

需：

$$
\boxed{
B_{ij}^{T}
}
$$

完成 mapping / synchronization / uncertainty bound。

---

# 76. Clock Mapping 也有誤差

$$
\epsilon_{ij}^{T}>0.
$$

所以跨域 exact simultaneity 可能不能被假設。

---

# 77. Causal Bridge 比 Clock Sync 更強

即使 timestamp 不完全同步，

只要能證明：

$$
e_i\prec e_j,
$$

仍可建立 causal legality。

所以：

$$
\boxed{
\text{causal consistency}
\not\Rightarrow
\text{perfect clock synchronization}.
}
$$

---

# 78. Distributed Systems 的直接接口

這裡自然接：

- logical clocks；
- vector clocks；
- happens-before；
- causal consistency；
- partial order scheduling。

但本文不宣稱取代這些成熟理論。

---

# 79. UNPNP-II 的新增點

本文把這些時間／因果結構放進：

$$
\boxed{
\text{multi-scale route optimization}.
}
$$

即它們不只是 distributed system correctness 工具，也是 route metric 的一部分。

---

# 80. Route Cost Vector 擴充

Paper 02：

$$
\mathbf C
=
(H,W,D,T,M,K,V,P,U,E,R,L_O).
$$

本文把：

$$
D
$$

進一步拆成：

$$
D_C,
D_G,
D_S
$$

等不同深度／距離。

---

# 81. 建議新向量

$$
\boxed{
\mathbf C_{\mathrm{TC}}
=
(
H,
W,
D_C,
T_{\mathrm{wall}},
d_S,
d_G,
C_{\mathrm{sync}},
C_{\mathrm{history}},
C_{\mathrm{verify}}
).
}
$$

---

# 82. Shortest-by-Time

$$
\boxed{
\mathcal R_T^\*
=
\arg\min
T_{\mathrm{wall}}(\mathcal R).
}
$$

---

# 83. Shortest-by-Causal-Depth

$$
\boxed{
\mathcal R_C^\*
=
\arg\min
D_C(\mathcal R).
}
$$

---

# 84. Shortest-by-Work

$$
\boxed{
\mathcal R_W^\*
=
\arg\min
W(\mathcal R).
}
$$

---

# 85. Shortest-by-State-Distance

有些 control problem 可能最小化：

$$
\int
d_S(s_t,s^\*)\,dt.
$$

與最少 computational work 完全不同。

---

# 86. Shortest-by-History-Risk

某些 route 可能最小化：

$$
C_{\mathrm{history-risk}}.
$$

例如避免不可逆操作。

---

# 87. 因此沒有唯一「時間最短」概念

即使只談 time，也至少要說：

- physical；
- wall；
- event；
- causal；
- logical；
- observer。

---

# 88. Time Compression

Path compilation 有時壓縮：

$$
T_{\mathrm{wall}}
$$

但未必壓縮：

$$
W.
$$

例如 parallelization。

---

# 89. Work Compression

Algorithmic improvement 可以：

$$
W\downarrow
$$

即使：

$$
T_{\mathrm{wall}}
$$

因硬體不同沒有明顯變化。

---

# 90. Causal Compression

Stage fusion 可以：

$$
D_C\downarrow.
$$

---

# 91. Observer Compression

Aggregation 可以：

$$
H_O\downarrow
$$

但 execution 完全沒變。

---

# 92. State Compression

某些 symbolic transform 可能縮小 state representation：

$$
M\downarrow
$$

但 route depth 不變。

---

# 93. 不同 Compression 要分開命名

所以：

$$
\boxed{
\text{compression}
}
$$

至少應帶下標：

$$
C_W,
C_D,
C_T,
C_O,
C_S.
$$

---

# 94. False Speedup

如果：

$$
H_O\downarrow
$$

但：

$$
W,T
$$

完全不變，

這只是 interface compression。

不應宣稱 computational speedup。

---

# 95. False Parallelism

如果 tasks 看似可並行，

但 hidden dependency 存在：

$$
e_i\prec_C e_j,
$$

則 surface geometry 判斷錯誤。

---

# 96. False Causal Compression

如果 path compiler 移除某 intermediate event，

但那個 event 是：

- audit；
- consent；
- validation；
- commit barrier；

則：

$$
\widehat{\ell}
$$

可能 state-equivalent 但 causally invalid。

---

# 97. Path Compilation 的新 Promotion Gate

除原本：

- semantic equivalence；
- lower cost；
- guard；
- validation；

還需：

$$
\boxed{
V_C=1,
\qquad
V_T=1,
\qquad
V_H=1
}
$$

在 task 要求時。

---

# 98. Crystallization 會建立 Macro Time

當：

$$
\Gamma^{(\mu)}
\rightarrow
\kappa^{(M)},
$$

上層可以把整段 micro history 視為一個 macro event：

$$
E^{(M)}.
$$

---

# 99. Macro Event 不能抹除 Micro History

所以：

$$
\boxed{
E^{(M)}
\rightarrow
\mathcal H^{(\mu)}
}
$$

必須可追溯。

---

# 100. Temporal Crystal

本文提出一個候選概念：

## Temporal Crystal

一段穩定、已驗證的 event / causal sequence 被提升成 macro temporal primitive。

形式：

$$
\boxed{
K_T(
\mathcal H^{(\mu)}
)
=
\theta^{(M)}.
}
$$

---

# 101. Temporal Crystal 與 Computational Crystal 不同

Computational Crystal 強調 reusable computation。

Temporal Crystal 強調：

- ordered history；
- causal contract；
- timing envelope。

兩者可以重疊，但不完全相同。

---

# 102. 例：Transaction

一個 transaction：

$$
\theta_{\mathrm{tx}}
$$

在上層是一個 event。

但內部：

```text
authorize
→ reserve
→ write
→ verify
→ commit
```

具有不可刪除因果順序。

---

# 103. 例：Agent Tool Action

上層：

```text
send_report()
```

是一個 action。

但若內部有：

```text
resolve identity
→ authorize
→ generate
→ validate
→ send
```

不能因為追求 shortest path 把 authorization 跳掉。

---

# 104. 這直接接 Safe Reachable World

所以：

$$
\boxed{
\text{causal shortest}
}
$$

必須在 authorized event graph 中求解。

---

# 105. Authorized Causal Graph

令：

$$
G_C^{\mathrm{auth}}
$$

只保留合法 causal transitions。

則：

$$
\boxed{
D_C^\*
=
\min_{\gamma\in G_C^{\mathrm{auth}}}
D_C(\gamma).
}
$$

---

# 106. 更短的非法歷史不參與比較

如果：

$$
\gamma_{\mathrm{skip-auth}}
$$

更短，

但違反 policy，

它不屬於 feasible set。

---

# 107. Time Budget

任務可有：

$$
B_T.
$$

例如 deadline。

route 必須：

$$
T_{\mathrm{wall}}(\mathcal R)
\le
B_T.
$$

---

# 108. Causal Budget

某些 real-time pipeline 可限制：

$$
D_C\le\theta_D.
$$

即便 work 很大，只要能並行也可接受。

---

# 109. Work Budget

edge device 可能限制：

$$
W\le B_W.
$$

此時不能只靠大規模 parallel brute force。

---

# 110. Energy Budget

物理 runtime 可能限制：

$$
E\le B_E.
$$

因此 fastest route 未必可行。

---

# 111. Multi-Budget Feasible Set

$$
\boxed{
\mathcal F_B
=
\{
\mathcal R:
W\le B_W,
T\le B_T,
E\le B_E,
R\le B_R
\}.
}
$$

---

# 112. Time-Causal Pareto Front

如果：

$$
W,
D_C,
T,
E
$$

彼此 trade-off，

則：

$$
\boxed{
\mathfrak P^\*_{\mathrm{TC}}
=
\operatorname{ParetoMin}
(
W,D_C,T,E
).
}
$$

---

# 113. 同一演算法在不同硬體的 Temporal Geometry 不同

algorithm structure 相同，

但 CPU / GPU / distributed runtime 會改變：

$$
T_{\mathrm{wall}},
D_{\mathrm{physical}},
C_{\mathrm{sync}}.
$$

所以：

$$
\boxed{
\text{algorithm}
\neq
\text{fixed temporal realization}.
}
$$

---

# 114. 同一 Hardware 上不同 Scheduler 也不同

$$
\mathcal S_1\neq\mathcal S_2
$$

可以導致：

$$
T_1\neq T_2.
$$

所以 runtime scheduling 是 temporal route 的一部分。

---

# 115. GCM Scheduler 接口

GCM 原本有：

$$
\mathcal S
$$

作為 scheduling / routing。

本文補：

$$
\boxed{
\mathcal S_T
=
\text{temporal-causal scheduling policy}.
}
$$

---

# 116. 非交換 Scheduler

若：

$$
A\circ B\neq B\circ A,
$$

scheduler 不只是效能元件，而是 world-state semantics 的一部分。

---

# 117. MWT 的直接接口

MWT 已將：

- noncommutative history；
- branching；
- convergence；
- observer-relative world；

列為一級結構。

因此本文不是把 history 新加給 MWT，而是把 MWT 的 history semantics 接入 UNPNP shortest-route accounting。

---

# 118. World Presentation 與 Time Presentation

MWT：

$$
\rho_{\alpha,O,t}(\mathbf W)
$$

是 World presentation。

本文進一步允許：

$$
\boxed{
\rho^T_{\beta,O}
(
\mathcal H
)
=
\Theta_O
}
$$

表示 observer-specific temporal presentation。

---

# 119. 同一 History 可有不同 Time Presentation

例如：

- exact timestamps；
- causal DAG；
- transaction sequence；
- narrative summary。

所以：

$$
\Theta_1\neq\Theta_2
$$

不等於 history 不同。

---

# 120. Temporal Projection Loss

若 summary：

$$
\Pi_T(\mathcal H)
$$

遺失關鍵 ordering，

可能產生：

$$
L_T>0.
$$

這也應進 cost ledger。

---

# 121. 最短路徑與時間解析度

粗時間解析度可能讓：

$$
D_C
$$

看起來更小。

因此：

$$
\boxed{
\text{temporal resolution}
}
$$

也是 chart 的一部分。

---

# 122. Micro-Recursion

在 micro scale：

$$
e^{(k)}
$$

可再展開：

$$
e_1^{(k-1)}
\rightarrow
\cdots
\rightarrow
e_n^{(k-1)}.
$$

這是 temporal recursion。

---

# 123. Macro-Ascent

反向：

$$
\mathcal H^{(k)}
\rightarrow
E^{(k+1)}.
$$

一整段 history 上升成 macro event。

---

# 124. 所以「一秒」也不是固定 computational unit

一秒內可以：

- 什麼都沒做；
- 一次慢 I/O；
- 十億次 operation；
- 一次 global state swap。

所以：

$$
\boxed{
\text{physical time unit}
\neq
\text{computational unit}.
}
$$

---

# 125. Computation Rate

可以定義：

$$
\boxed{
r_W
=
\frac{W}{T_{\mathrm{wall}}}.
}
$$

但這仍不是「智能」或「進度」本身，只是 work rate。

---

# 126. Causal Progress Rate

$$
\boxed{
r_C
=
\frac{D_C}{T_{\mathrm{wall}}}.
}
$$

---

# 127. State Change Rate

$$
\boxed{
r_S
=
\frac{d_S(s_0,s_t)}{T}.
}
$$

三種 rate 可能完全不同。

---

# 128. Route Learning 會改變 Temporal Profile

當：

$$
\Gamma
\rightarrow
\widehat{\ell}
\rightarrow
\kappa,
$$

未來：

$$
W_t,
D_t,
T_t
$$

都可能下降，

但下降幅度不同。

---

# 129. Structural Learning 的證據應是向量

因此不能只報：

> latency 下降 30%。

更好：

$$
\boxed{
\Delta
\mathbf C
=
(
\Delta W,
\Delta D_C,
\Delta T,
\Delta M,
\Delta V,
\Delta R
).
}
$$

---

# 130. Frozen-Model Experiment 的新 Metric

原 UNPNP frozen-model：

$$
\theta_{t+1}=\theta_t.
$$

現在可測：

$$
W_t\downarrow,
$$

$$
D_{C,t}\downarrow,
$$

$$
T_t\downarrow,
$$

$$
H_{O,t}\downarrow.
$$

---

# 131. 這能區分不同 Optimization

若只有：

$$
H_O\downarrow
$$

可能只是 UI compression。

若：

$$
W,D_C,T
$$

都下降，

才更接近真正 computational restructuring。

---

# 132. 因果保留是更強驗證

如果：

$$
D_C\downarrow
$$

但 required causal obligations 全部保留，

這比單純 hidden macro packaging 更強。

---

# 133. Temporal Drift

即使 route semantics 不變，

hardware load、network、queue 可能使：

$$
T_t
$$

漂移。

所以：

$$
\boxed{
\text{temporal validity}
}
$$

具有 epoch。

---

# 134. Causal Drift

dependency 或 policy 改變後：

$$
\preceq_C^{(t)}
\neq
\preceq_C^{(t+1)}.
$$

舊 crystal 可能失效。

---

# 135. History Invalidation

如果新規則要求新增 audit event，

原 path：

$$
\Gamma
$$

即使 endpoint 還對，

也可能：

$$
V_H=0.
$$

必須 stale。

---

# 136. Temporal Guard

Crystal 可以帶：

```text
deadline
max_age
freshness
minimum_ordering
required barriers
timeout
clock-domain
```

---

# 137. Causal Guard

可以帶：

```text
must_follow
must_precede
must_not_overlap
must_commit_after
must_validate_before
```

---

# 138. Temporal-Causal Crystal

綜合可定義：

$$
\boxed{
\kappa_{TC}
=
\langle
D,
G_T,
G_C,
H,
V,
F,
R
\rangle.
}
$$

其中：

- $D$：valid domain；
- $G_T$：temporal guards；
- $G_C$：causal guards；
- $H$：history template；
- $V$：validator；
- $F$：fallback；
- $R$：receipts。

---

# 139. 一個 Route 的「短」可能來自不同來源

### Type A

少做 work：

$$
W\downarrow.
$$

### Type B

增加 parallelism：

$$
D_C\downarrow.
$$

### Type C

減少 I/O：

$$
T\downarrow.
$$

### Type D

減少 observer steps：

$$
H_O\downarrow.
$$

### Type E

減少 state materialization：

$$
M\downarrow.
$$

---

# 140. 因此 Speedup 必須標型

本文建議：

```text
work-speedup
depth-speedup
latency-speedup
observer-hop-speedup
materialization-speedup
lifecycle-speedup
```

---

# 141. 一個非常典型的錯誤

若：

```text
10 UI steps
→ 1 API call
```

但：

$$
W,D,T
$$

沒變，

只能說：

$$
\boxed{
H_O\downarrow.
}
$$

不能說：

$$
\boxed{
C_{\mathrm{compute}}\downarrow.
}
$$

---

# 142. 真正 Path Compilation 的時間版本

若：

$$
\Gamma
$$

編譯成：

$$
\widehat{\ell}
$$

並：

$$
W(\widehat{\ell})<W(\Gamma)
$$

或：

$$
D_C(\widehat{\ell})<D_C(\Gamma)
$$

或：

$$
T(\widehat{\ell})<T(\Gamma),
$$

且 semantics / history obligations 保留，則形成真實 time-causal improvement。

---

# 143. 一個 Route 可以 Work 變多但更值得

例如 parallel brute force：

$$
W\uparrow,
$$

$$
D_C\downarrow,
$$

$$
T\downarrow.
$$

如果 deadline 很重要，它仍可能是 optimum。

---

# 144. 一個 Route 可以 Time 變長但更值得

例如 verification：

$$
T\uparrow
$$

但：

$$
R\downarrow.
$$

高風險任務下更值得。

---

# 145. 最短不是道德詞

所以：

$$
\boxed{
\text{shortest}
\neq
\text{best in all senses}.
}
$$

它永遠是 objective-relative。

---

# 146. Time-Causal Route Certificate

建議：

```text
TimeCausalRouteCertificate
- route_id
- world_revision
- chart
- temporal_frame
- causal_graph_digest
- work
- causal_depth
- wall_time
- event_time_range
- state_distance
- geometry_distance
- history_digest
- temporal_guards
- causal_guards
- validation
- epoch
```

---

# 147. Minimum History Requirement

有些 task 可以只保留：

$$
H_{\mathrm{digest}}.
$$

有些必須保留 full event history。

所以：

$$
\boxed{
\text{history granularity}
}
$$

也應 task-relative。

---

# 148. History Compression

$$
\mathcal H
\rightarrow
\widehat{\mathcal H}
$$

可以節省 storage，

但需保留 relevant invariants。

---

# 149. History Crystal

經常重複的合法 history pattern：

$$
\mathcal H_1,\ldots,\mathcal H_n
$$

可抽象成：

$$
\kappa_H.
$$

但 source history 仍應可追溯。

---

# 150. History Crystal 不等於刪除歷史

所以：

$$
\boxed{
\text{history crystallization}
\neq
\text{history erasure}.
}
$$

---

# 151. MWT × GCM × UNPNP 的時間閉環

MWT：

$$
\mathbf W_t
$$

保留 history / branch / noncommutativity。

GCM：

$$
\Phi_G(t)
$$

組合多域局部演化。

UNPNP：

$$
\mathcal R_t
$$

選擇與重寫 route。

三者現在共同形成：

$$
\boxed{
\mathbf W_t
\xrightarrow{\Phi_G,\mathcal R_t}
\mathbf W_{t+1},
\qquad
\mathcal H_{t+1}
=
\mathcal H_t
\oplus
\Delta\mathcal H_t.
}
$$

---

# 152. 世界演化與觀察不必同步

observer 可以：

$$
\Pi_O(\mathbf W_t)
$$

低頻更新，

而 world：

$$
\mathbf W_t
$$

高頻演化。

因此：

$$
\boxed{
\text{observer frame}
\neq
\text{world epoch}.
}
$$

---

# 153. 這是宏、中、微時間尺度的正式入口

不同尺度：

$$
\sigma_\mu,
\sigma_m,
\sigma_M
$$

可以有不同 clock / epoch。

---

# 154. Micro Clock

處理：

- instruction；
- event；
- packet；
- microstate。

---

# 155. Meso Clock

處理：

- function；
- transaction；
- agent action；
- batch。

---

# 156. Macro Clock

處理：

- workflow；
- episode；
- project；
- world epoch。

---

# 157. Macro Clock 不必是 Micro Clock 的整數倍

因為 macro event 可能由：

- completion；
- convergence；
- trigger；
- threshold；

決定，而不是固定 tick count。

---

# 158. Event-Defined Time

因此可以有：

$$
\boxed{
t_{k+1}
=
\inf
\{
t:
\mathcal C(\mathbf W_t)=1
\}.
}
$$

即條件達成才進下一 macro epoch。

---

# 159. Recursive Time

一個 macro epoch：

$$
T^{(k)}
$$

裡面可以嵌套：

$$
T_1^{(k-1)},\ldots,T_n^{(k-1)}.
$$

---

# 160. Recursive Time 與 Recursive Geometry 對偶

Paper 03：

$$
\mathsf{Pt}^{(k)}
=
\mathcal W^{(k-1)}.
$$

本文：

$$
\boxed{
\text{Macro Event}^{(k)}
=
\text{Micro History}^{(k-1)}.
}
$$

---

# 161. 這使「一個點」也具有時間厚度

高層 point：

$$
v^{(k)}
$$

可以不是瞬間，而是一段 micro-duration 被壓縮後的 temporal object。

---

# 162. Temporal Thickness

定義：

$$
\boxed{
\Delta_T(v^{(k)})
}
$$

表示該 macro unit 所包含的 lower-scale duration envelope。

---

# 163. Computational Thickness

同理：

$$
\boxed{
\Delta_W(v^{(k)})
}
$$

表示 hidden work。

---

# 164. Causal Thickness

$$
\boxed{
\Delta_C(v^{(k)})
}
$$

表示 hidden causal depth。

---

# 165. 一個高層 Point 因此可以攜帶 Thickness Vector

$$
\boxed{
\Delta(v)
=
(
\Delta_W,
\Delta_C,
\Delta_T,
\Delta_S
).
}
$$

這能防止高層抽象把成本全部藏掉。

---

# 166. Earned Point 的完整條件因此更清楚

一個 route 升成 point，不表示其 thickness 消失。

而是：

$$
\boxed{
\text{internal structure removed from ordinary routing}
+
\text{resource thickness retained as metadata}.
}
$$

---

# 167. 這是 UNPNP-II 對「一」的第二次修正

Paper 01：

> 一是 scale-relative。

本文：

> 一還可以具有 hidden temporal-causal thickness。

所以：

$$
\boxed{
1_{\chi}
\neq
\text{zero-dimensional zero-cost atom}.
}
$$

---

# 168. 對最短路徑的更完整表示

Route：

$$
\mathcal R
$$

不只帶 geometry，

還帶：

$$
\Theta.
$$

因此可寫：

$$
\boxed{
\mathcal R
=
\langle
\mathcal G,
\Theta,
\chi,
\mathcal H
\rangle.
}
$$

作為高層 shorthand。

---

# 169. World-Relative Optimization 再擴充

$$
\boxed{
\mathcal R^\*
=
\arg\min_{\mathcal R}
J(
\mathcal R
\mid
\mathbf W,
\chi,
\Theta,
q,
B,
\text{Risk},
\mathcal H
).
}
$$

---

# 170. Joint Geometry-Time Optimization

甚至：

$$
\boxed{
(g^\*,\Theta^\*,\mathcal R^\*)
=
\arg\min_{g,\Theta,\mathcal R}
J(
g,\Theta,\mathcal R
\mid
\mathbf W,q,B,R
).
}
$$

---

# 171. 但不能把真實時間當成自由變數

Runtime 可以改 representation、scheduler、parallelism，

但不能任意宣稱物理 latency 不存在。

所以：

$$
\boxed{
\text{temporal modeling freedom}
\neq
\text{physical-time erasure}.
}
$$

---

# 172. 這再次回到 Complexity Transfer

如果：

$$
T_{\mathrm{online}}\downarrow
$$

是因：

$$
C_{\mathrm{precompute}}\uparrow,
$$

需計入 total lifecycle。

---

# 173. Time Shifted Complexity

可定義：

$$
\boxed{
C_{\mathrm{total}}
=
C_{\mathrm{past}}
+
C_{\mathrm{now}}
+
E[
C_{\mathrm{future}}
].
}
$$

---

# 174. 過去計算可以讓現在看起來 O(1)

index、model、crystal 都是例子。

所以：

$$
\boxed{
\text{present-time shortness}
\neq
\text{lifecycle shortness}.
}
$$

---

# 175. 未來維護也會反噬現在的短路

如果 crystal 常 stale：

$$
C_{\mathrm{maintain}}\uparrow.
$$

則：

$$
J_{\mathrm{life}}
$$

可能變差。

---

# 176. Temporal Amortization

重複 $N$ 次：

$$
C_{\mathrm{life}}
=
C_{\mathrm{build}}
+
N C_{\mathrm{run}}
+
C_{\mathrm{maintain}}.
$$

這仍是 Path Compilation 是否值得的關鍵。

---

# 177. 第一條核心定律

$$
\boxed{
\textbf{
Work, causal depth, elapsed time, state distance, and geometric distance are distinct computational quantities.
}
}
$$

---

# 178. 第二條核心定律

$$
\boxed{
\textbf{
Parallelism can reduce causal depth and wall-clock time without reducing total work.
}
}
$$

---

# 179. 第三條核心定律

$$
\boxed{
\textbf{
Same endpoint does not imply same history, and same history summary does not imply same causal structure.
}
}
$$

---

# 180. 第四條核心定律

$$
\boxed{
\textbf{
A macro computational unit may contain non-zero temporal, causal, and physical thickness.
}
}
$$

---

# 181. 第五條核心定律

$$
\boxed{
\textbf{
Path compilation is valid only when the task-relevant state, causal, temporal, and history invariants are preserved.
}
}
$$

---

# 182. 對 Paper 03 的補充

Paper 03 說：

$$
\text{Computational Route}
\supset
\text{Graph Path}.
$$

本文補：

$$
\boxed{
\text{Computational Route}
=
\text{Geometry}
+
\text{Causality}
+
\text{Time}
+
\text{History}.
}
$$

至少在 route accounting 層如此。

---

# 183. 對 Paper 02 的補充

Paper 02 說：

$$
\text{Shortest}
=
\text{chart-relative and objective-relative}.
$$

本文進一步說：

$$
\boxed{
\text{the objective itself must distinguish time-like quantities}.
}
$$

---

# 184. 對 Paper 01 的補充

Paper 01 問：

> 什麼算一？

本文回答：

> 即使算一，也要記住這個一裡面可能包含多少工作、多少因果深度、多少物理時間與多少歷史。

---

# 185. 第一批實驗：Independent 10

World：

$$
a_1,\ldots,a_{10}
$$

完全獨立。

驗證：

$$
W=10,
\qquad
D_C=1.
$$

比較 single-thread / parallel runtime。

---

# 186. 第二批實驗：Hidden Dependency

表面十個 independent tasks，

偷偷加入：

$$
a_3\prec a_7.
$$

測 geometry / causal inference 是否能發現。

---

# 187. 第三批實驗：Same Endpoint Different History

建立兩條 route：

$$
\mathcal R_A,
\mathcal R_B
$$

終態相同，但一條有 irreversible side effect。

測 endpoint-only validator 是否錯誤 promote。

---

# 188. 第四批實驗：Macro Hidden Thickness

將高成本 workflow 包成一個 call。

測 naive hop metric 是否誤判為 speedup。

---

# 189. 第五批實驗：Crystallized Temporal-Causal Route

讓 repeated workflow：

$$
\Gamma
$$

被編譯成：

$$
\kappa_{TC}.
$$

要求：

- work 降低或 depth 降低；
- causal obligations 保留；
- history receipt 完整。

---

# 190. 成功條件

如果 geometry-aware + temporal-causal-aware runtime 能顯著降低：

- false speedup claim；
- invalid compilation；
- hidden dependency error；
- endpoint-only equivalence error；

則本文 layer 具有獨立工程價值。

---

# 191. 失敗條件

若所有區分都能由現有：

- work-depth model；
- causal DAG；
- distributed logical time；
- profiler；

低成本完整處理，且 UNPNP-II 統一層沒有額外 routing / crystallization 增益，

則應縮減新術語。

---

# 192. 與既有理論的關係

本文不取代：

- parallel algorithms；
- critical path method；
- DAG scheduling；
- distributed causality；
- logical clocks；
- event-time processing；
- hybrid systems；
- temporal logic。

本文的新增目的，是把這些時間／因果 distinctions 接入：

$$
\boxed{
\text{multi-scale route selection}
+
\text{path compilation}
+
\text{crystallization}.
}
$$

---

# 193. Paper 05 的接口

前四篇已建立：

1. 一是相對的；
2. 最短是相對的；
3. 路不一定是線；
4. 時間不等於路長。

下一步就可以正式處理：

> **一個計算世界如何向下無限展開，又如何向上把整個世界壓成一個新的點？**

因此 Paper 05：

## 微觀展開與宏觀遞升
### Recursive Refinement, Coarsening, Multi-Resolution Atlases, and World-to-Primitive Transitions

將正式建立：

$$
R_\downarrow,
\qquad
R_\uparrow,
$$

以及：

$$
\boxed{
\text{World}^{(k)}
\leftrightarrow
\text{Primitive}^{(k+1)}.
}
$$

---

# 結論

當十個 operation 同時執行時，問：

> 到底算一還是十？

其實問題缺少下標。

在同一 execution 中，完全可以：

$$
W=10,
$$

$$
D_C=1,
$$

$$
H_O=1,
$$

$$
T_{\mathrm{wall}}=10\text{ ms},
$$

同時：

$$
d_S
$$

又是另一個值。

所以：

$$
\boxed{
\text{Work}
\neq
\text{Causal Depth}
\neq
\text{Wall Time}
\neq
\text{State Distance}
\neq
\text{Geometry Distance}.
}
$$

而一條真正的 computational route，也不能只保存：

$$
s_0\rightarrow s_f.
$$

它至少還有：

$$
\boxed{
\mathcal R
=
\langle
\mathcal G,
\Theta,
\chi,
\mathcal H
\rangle.
}
$$

其中：

- $\mathcal G$：dependency geometry；
- $\Theta$：temporal-causal frame；
- $\chi$：computational chart；
- $\mathcal H$：history。

因此本文最終命題是：

$$
\boxed{
\textbf{
時間不是路長，
因果不是時間，
工作量不是因果深度，
而終點更不是整條歷史。
}
}
$$

只有當這些量被分開，UNPNP 才能真正回答：

> **一條被稱為「更短」的新路，究竟縮短了什麼，又把什麼成本轉移到了哪裡？**

這就是 UNPNP-II 從多尺度計算幾何進一步進入多尺度時間—因果計算論的核心。
