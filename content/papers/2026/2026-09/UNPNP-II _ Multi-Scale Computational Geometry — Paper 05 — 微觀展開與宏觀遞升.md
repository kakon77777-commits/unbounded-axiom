# UNPNP-II / Multi-Scale Computational Geometry — Paper 05
## 微觀展開與宏觀遞升
### Recursive Refinement, Coarsening, Multi-Resolution Atlases, and World-to-Primitive Transitions

**系列名稱：** UNPNP-II｜Multi-Scale Computational Geometry  
**系列中文名：** UNPNP 第二層：多尺度計算幾何與相對最短路徑  
**篇次：** Paper 05 / 08  
**作者：** Neo.K with Aletheia（GPT）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-08  
**文件性質：** 多尺度計算／遞歸世界／計算結晶化／UNPNP 擴充論文  
**前置：** Paper 01–04、MWT、GCM、UNPNP-I Path Compilation / Computational Crystallization  
**狀態：** Canonical Draft

---

## 摘要

UNPNP-II 前四篇已建立四個基礎分離：

1. 計算中的「一」不是天然原子；
2. 最短路徑必須相對 computational chart、observer、World boundary 與 objective；
3. computational route 不必是一條普通 graph line，而可以是 point、jump-line、surface、cluster、field 或 recursive geometry；
4. work、causal depth、wall-clock、state distance、geometric distance 與 history 彼此不同。

由此產生下一個核心問題：

> **如果一個高層計算單位下面可以是一整個世界，那這個世界如何被打開？又在什麼條件下可以重新被壓成一個新的「一」？**

本文提出 **Recursive Refinement / Coarsening Framework**，將 UNPNP-II 的多尺度運算正式寫成：

$$
\boxed{
R_{\downarrow}
:
u^{(k)}
\rightarrow
\mathcal W^{(k-1)}
}
$$

與：

$$
\boxed{
R_{\uparrow}
:
\mathcal W^{(k-1)}
\rightarrow
u^{(k)}.
}
$$

其中 $k$ 不是固定五層編號，而是一個可遞歸延伸的 scale index。高層 unit $u^{(k)}$ 在需要時可展開成較低層 local computational world：

$$
\mathcal W^{(k-1)}.
$$

反過來，若一個低層世界在指定 domain 中具有穩定邊界、可驗證語義、可界定副作用、可壓縮 route structure 與正 lifecycle utility，則可以透過 Path Compilation 與 Computational Crystallization 被提升為新的高層 primitive：

$$
\boxed{
\mathcal W^{(k-1)}
\rightarrow
\widehat{\mathcal R}^{(k-1)}
\rightarrow
\kappa^{(k)}.
}
$$

本文將此稱為 **World-to-Primitive Transition**。

同時，當 distribution shift、anomaly、audit、permission change、dependency change 或 failure 發生時，高層 primitive 必須可以重新被打開：

$$
\boxed{
\kappa^{(k)}
\xrightarrow{\operatorname{Reopen}}
\mathcal W^{(k-1)}.
}
$$

因此：

$$
\boxed{
\text{Abstraction}
+
\text{Reopenability}
}
$$

是多尺度計算世界成立的共同條件。

本文亦正式接入 MWT 的：

$$
\boxed{
\text{Finite Active Support}
+
\text{Unbounded Refinement}
}
$$

以及 GCM 的：

$$
\boxed{
\text{Recursive Globality}
\neq
\text{Recursive Full Expansion}.
}
$$

因此，多尺度 Runtime 不應永久展開全部尺度，而只維持一個有限的 active refinement frontier：

$$
\boxed{
|\mathcal F_t^{\mathrm{active}}|
<\infty.
}
$$

世界可以概念上無界精細化：

$$
\cdots
\rightarrow
\mathcal W^{(-2)}
\rightarrow
\mathcal W^{(-1)}
\rightarrow
\mathcal W^{(0)}
\rightarrow
\mathcal W^{(+1)}
\rightarrow
\cdots
$$

但任一時刻真正 materialize 的只是一個有限尺度子集。

本文進一步提出 **Computational Atlas**。一個大型 World 不必使用單一尺度或單一 representation，而可以由多張 chart 組成：

$$
\boxed{
\mathcal A_W
=
\{
(U_i,\chi_i,\sigma_i)
\}_{i\in I}.
}
$$

不同 chart 可以使用不同：

- granularity；
- dependency geometry；
- 24／72 computational configuration；
- temporal-causal frame；
- observer resolution。

chart 之間透過可驗證 transition map / bridge 連接。

因此：

$$
\boxed{
\text{One World}
\neq
\text{One Resolution}
\neq
\text{One Geometry}
\neq
\text{One Computational Form}.
}
$$

本文最後將 UNPNP 的 Path Compilation 與 Computational Crystallization 重新定位為跨尺度轉換機制的一部分。Path Compilation 不再只代表「把一條長路變成一條新超連結」，而可以成為：

$$
\boxed{
\text{lower-scale route}
\rightarrow
\text{higher-scale primitive}.
}
$$

而 Decrystallization 則是：

$$
\boxed{
\text{higher-scale primitive}
\rightarrow
\text{lower-scale route/world}.
}
$$

由此，UNPNP-II 開始具有完整的微觀展開—宏觀遞升閉環。

---

# 1. 一個點下面可以是一整個世界

Paper 03 已建立：

$$
\boxed{
\mathsf{Pt}^{(k)}
=
\mathcal W^{(k-1)}
}
$$

在 scale-relative projection 意義下可以成立。

這句話的真正含義不是「點本體上等於世界」，而是：對第 $k$ 層 Runtime 而言，一個不再展開的 computational unit，在更細的第 $k-1$ 層可以有自己的 state、operator、route、history、observer 與 validation。

因此：

$$
\boxed{
\text{Point}^{(k)}
\rightarrow
\text{World}^{(k-1)}
}
$$

是 refinement relation。

---

# 2. Scale Index

令：

$$
\Sigma
$$

表示可用尺度集合。

不要求：

$$
\Sigma
=
\{-2,-1,0,1,2\}
$$

固定有限。

只需存在局部相鄰關係：

$$
k-1
\prec
k
\prec
k+1.
$$

---

# 3. 微、微遞歸、中、宏、宏遞升

人類語言可粗略寫：

```text
recursive micro
micro
meso
macro
recursive macro
```

但正式上更適合：

$$
\cdots
<
\sigma_{-2}
<
\sigma_{-1}
<
\sigma_0
<
\sigma_{+1}
<
\sigma_{+2}
<
\cdots
$$

表示可繼續向下與向上延伸。

---

# 4. Scale 不等於 Physical Size

微觀不一定表示物理尺寸小。

例如 function internals、database query plan、Agent subroutine、logical proof step，都可以是 computational micro-scale。

所以：

$$
\boxed{
\text{computational scale}
\neq
\text{physical spatial scale}.
}
$$

---

# 5. Scale 也不等於 Time Scale

一個 micro computation 可以耗很久，而 macro event 可以瞬間完成。

所以：

$$
\boxed{
\sigma
\neq
T.
}
$$

Paper 04 的 temporal frame 必須另外保留。

---

# 6. Refinement Operator

第一版：

$$
\boxed{
R_{\downarrow}^{k\to k-1}
:
u^{(k)}
\rightarrow
\mathcal W_u^{(k-1)}.
}
$$

它回答：

> 這個目前被當成一的 unit，內部需要如何展開？

---

# 7. Refinement 不只是看更多字

真正 refinement 可能需要：

- source expansion；
- trace materialization；
- dependency reconstruction；
- causal reconstruction；
- geometry inference；
- lower-scale state loading；
- permission resolution；
- validator binding。

---

# 8. Refinement Cost

$$
\boxed{
C_{\downarrow}
=
C_{\mathrm{load}}
+
C_{\mathrm{materialize}}
+
C_{\mathrm{infer}}
+
C_{\mathrm{verify}}
+
C_{\mathrm{sync}}
+
C_{\mathrm{context}}.
}
$$

---

# 9. Refinement 不應免費

如果 AI 每一步都：

```text
expand everything
```

則：

$$
C_{\downarrow}
$$

本身會成為主要成本。

因此：

$$
\boxed{
\text{maximum refinement everywhere}
}
$$

不是合理策略。

---

# 10. Coarsening Operator

定義：

$$
\boxed{
R_{\uparrow}^{k-1\to k}
:
\mathcal W^{(k-1)}
\rightarrow
u^{(k)}.
}
$$

---

# 11. Coarsening 不等於 Crystallization

任何 summary 都可以 coarse-grain。

所以：

$$
\boxed{
\text{Coarsening}
\supset
\text{Crystallization}.
}
$$

---

# 12. Representational Coarsening

例如：

```text
1000 logs
→ one summary
```

只改 observer representation。

---

# 13. Structural Coarsening

例如：

```text
100 graph nodes
→ one cluster hypernode
```

改變 route representation。

---

# 14. Computational Coarsening

若：

$$
\Gamma^{(k-1)}
$$

可以被新的 procedure：

$$
\widehat{\ell}^{(k)}
$$

取代，且實際成本下降，才接近 computational coarsening。

---

# 15. Crystallizing Coarsening

最強形式：

$$
\boxed{
K:
\widehat{\ell}^{(k)}
\rightarrow
\kappa^{(k)}.
}
$$

經穩定、驗證與 lifecycle promotion 後成為 earned primitive。

---

# 16. World-to-Primitive Transition

本文正式定義：

$$
\boxed{
\operatorname{W2P}
:
\mathcal W^{(k-1)}
\rightarrow
\kappa^{(k)}.
}
$$

其 pipeline：

$$
\mathcal W^{(k-1)}
\rightarrow
\mathcal R^{(k-1)}
\rightarrow
\widehat{\mathcal R}^{(k-1)}
\rightarrow
\kappa^{(k)}.
$$

---

# 17. W2P 不代表世界消失

原 world：

$$
\mathcal W^{(k-1)}
$$

仍可保留於 archive、canonical source、source trace、replay store 或 lower-scale runtime。

所以：

$$
\boxed{
\text{promotion}
\neq
\text{erasure}.
}
$$

---

# 18. Primitive-to-World Transition

反向：

$$
\boxed{
\operatorname{P2W}
:
\kappa^{(k)}
\rightarrow
\mathcal W^{(k-1)}.
}
$$

即 reopen、decrystallize、refine 或 inspect internals。

---

# 19. P2W Trigger

可能由：

```text
failure
distribution shift
audit
debug
permission change
version drift
novel input
low confidence
verification request
```

觸發。

---

# 20. Reopenability

任何 promoted primitive 都應滿足：

$$
\boxed{
\operatorname{Reopen}(\kappa)
\neq
\varnothing.
}
$$

至少存在 provenance path 回到 lower-scale source。

---

# 21. Compression without Reopenability

如果：

$$
\kappa
$$

不可追溯，則 debug、validation、stale detection 與 responsibility 都會惡化。

因此：

$$
\boxed{
\text{compression without reopenability}
=
\text{governance debt}.
}
$$

---

# 22. Multi-Resolution World

一個 World 可同時有：

$$
\rho_{\sigma_1}(\mathbf W),
\ldots,
\rho_{\sigma_n}(\mathbf W).
$$

它們不必全部 materialize。

---

# 23. Resolution Field

對 domain：

$$
D_i,
$$

定義：

$$
\boxed{
\Lambda_t:
D_i
\mapsto
\sigma_i(t).
}
$$

---

# 24. 不同 Domain 可以不同尺度

$$
\sigma_i
\neq
\sigma_j
$$

完全合法。

例如：

```text
stable region → coarse
failing service → fine
high-risk transaction → fine
archive → dormant
```

---

# 25. Maximum Resolution Everywhere 不是 Globality

$$
\boxed{
\text{Global Observation}
\neq
\text{Maximum Resolution Everywhere}.
}
$$

真正需要的是：

$$
\boxed{
\text{Maximum Relevant Distinction Under Bounded Computation}.
}
$$

---

# 26. Active Refinement Frontier

令：

$$
\boxed{
\mathcal F_t^{\mathrm{active}}
}
$$

表示當前真正展開的尺度邊界。

要求：

$$
\boxed{
|\mathcal F_t^{\mathrm{active}}|
<\infty.
}
$$

---

# 27. Conceptually Unbounded, Operationally Finite

世界可以無界 refinement，但 Runtime 只 materialize 有限尺度子集。

所以：

$$
\boxed{
\text{Unbounded Refinement}
\neq
\text{Infinite Active Materialization}.
}
$$

---

# 28. Finite Active Support

這直接承接 MWT：

$$
\boxed{
\text{Finite Active Support}
+
\text{Unbounded Refinement}.
}
$$

---

# 29. GCM 的同一原則

亦對應：

$$
\boxed{
\text{Recursive Globality}
\neq
\text{Recursive Full Expansion}.
}
$$

---

# 30. Active Horizon

$$
\boxed{
H_t^{\Sigma}
=
[
\sigma_{\min}(t),
\sigma_{\max}(t)
].
}
$$

---

# 31. Horizon 可移動

若 anomaly 出現在更低層：

$$
\sigma_{\min}\downarrow.
$$

問題解決後：

$$
\sigma_{\min}\uparrow.
$$

---

# 32. Refinement Debt

若某 domain 長期維持過粗且 unresolved evidence 累積：

$$
\boxed{
D_{\mathrm{refine}}(D_i).
}
$$

---

# 33. Debt Trigger

當：

$$
D_{\mathrm{refine}}
>
\theta_R,
$$

必須：

$$
R_{\downarrow}.
$$

---

# 34. Coarsening Debt

若 domain 已穩定卻永遠保持 micro materialization，則形成：

$$
D_{\mathrm{coarse}}.
$$

---

# 35. Coarsening Trigger

若：

$$
C_{\mathrm{maintain-fine}}
>
E[
C_{\mathrm{reopen}}
],
$$

則應考慮：

$$
R_{\uparrow}.
$$

---

# 36. Scale Utility

$$
\boxed{
U_\sigma
=
B_{\mathrm{information}}
+
B_{\mathrm{control}}
+
B_{\mathrm{verification}}
-
C_{\mathrm{materialize}}
-
C_{\mathrm{reason}}
-
C_{\mathrm{sync}}
-
C_{\mathrm{maintain}}.
}
$$

---

# 37. Optimal Resolution

$$
\boxed{
\sigma^\*
=
\arg\max_{\sigma}
U_\sigma.
}
$$

它是 task-relative。

---

# 38. Resolution Switch

$$
\boxed{
T_\Sigma:
\sigma_i
\rightarrow
\sigma_j.
}
$$

本身有：

$$
C_{\Sigma\text{-switch}}.
$$

---

# 39. Scale Thrashing

若：

$$
\sigma_a
\leftrightarrow
\sigma_b
$$

頻繁來回，可形成 Scale Thrashing。

---

# 40. Hysteresis

為避免反覆切換，可要求：

$$
\theta_{\downarrow}
\neq
\theta_{\uparrow}.
$$

---

# 41. Computational Atlas

對 World：

$$
\mathbf W,
$$

定義：

$$
\boxed{
\mathcal A_W
=
\{
(U_i,\chi_i,\sigma_i)
\}_{i\in I}.
}
$$

---

# 42. Atlas 不只是一組 View

每張 chart 可有自己的：

- unitization；
- geometry；
- computational form；
- transition law；
- temporal frame；
- observer projection；
- cost model。

---

# 43. Chart Overlap

若：

$$
U_i\cap U_j\neq\varnothing,
$$

需要 consistency map。

---

# 44. Transition Map

$$
\boxed{
\psi_{ij}:
\rho_i(U_i\cap U_j)
\rightarrow
\rho_j(U_i\cap U_j).
}
$$

這裡借用 atlas 的結構思想，不宣稱必為微分幾何 smooth map。

---

# 45. Computational Transition Map

可由 serialization、embedding、compilation、summarization、discretization、aggregation、type translation、causal projection 或 semantic bridge 實作。

---

# 46. Transition Fidelity

$$
\boxed{
F_{ij}
\in
[0,1].
}
$$

---

# 47. Loss

$$
\boxed{
L_{ij}
=
1-F_{ij}.
}
$$

若：

$$
L_{ij}
>
\theta_L,
$$

不能安全替代。

---

# 48. Atlas Consistency

對 task invariant：

$$
I_q,
$$

要求：

$$
\boxed{
I_q(
\psi_{ij}(x)
)
\simeq
I_q(x).
}
$$

---

# 49. Triple Overlap

希望：

$$
\psi_{ik}
\simeq
\psi_{jk}\circ\psi_{ij}
$$

在 relevant invariants 上一致。

---

# 50. Glue Debt

若 transition map 存在 unresolved inconsistency：

$$
\boxed{
D_{\mathrm{glue}}.
}
$$

---

# 51. Atlas 不要求全局單一 Chart

如果一個 World 不能被一種 representation 低成本完整處理，就保留 multiple local charts。

---

# 52. One World, Many Charts

$$
\boxed{
\text{One World}
\neq
\text{One Chart}.
}
$$

---

# 53. Atlas 與 MWT

MWT 的 presentation：

$$
\rho_{\alpha,O,t}(\mathbf W)
$$

提供多 chart 的本體邊界。

---

# 54. Atlas 與 GCM

GCM 不要求所有 domain 使用同一 computational form；本文再補上不要求相同 chart / scale。

---

# 55. Atlas 與 UNPNP

UNPNP hyperlink 可以成為：

$$
\boxed{
\text{cross-chart transition}.
}
$$

---

# 56. Scale Hyperlink

$$
\boxed{
\ell_{\sigma_i\to\sigma_j}
:
(U_i,\sigma_i)
\rightarrow
(U_j,\sigma_j).
}
$$

---

# 57. Upward Hyperlink

$$
\ell_{\uparrow}
$$

把 micro result 映射到 macro conclusion。

---

# 58. Downward Hyperlink

$$
\ell_{\downarrow}
$$

從 macro alert resolve 到 micro evidence。

---

# 59. Cross-Scale Hyperlink Cost

$$
\boxed{
C_{\ell_\Sigma}
=
C_{\mathrm{resolve}}
+
C_{\mathrm{materialize}}
+
C_{\mathrm{translate}}
+
C_{\mathrm{verify}}.
}
$$

---

# 60. Scale Routing

Runtime 不只選「下一個 state 去哪裡」，也選「下一步在哪個尺度算」。

---

# 61. Scale-Aware Corridor

$$
\boxed{
\mathcal M:
(
s,
q,
\sigma,
\mathcal A_W,
B,
R,
\mathcal H
)
\mapsto
(\Phi,\sigma').
}
$$

---

# 62. Route May Refine Before Moving

有時 optimum action 是先：

$$
s^{(k)}
\xrightarrow{R_\downarrow}
\mathcal W^{(k-1)}
$$

再決策。

---

# 63. Route May Coarsen Before Moving

也可以：

$$
\mathcal W^{(k-1)}
\xrightarrow{R_\uparrow}
u^{(k)}
\rightarrow
u'^{(k)}.
$$

---

# 64. Route May Alternate Scale

$$
M
\rightarrow
m
\rightarrow
\mu
\rightarrow
m
\rightarrow
M.
$$

這是一條 scale route。

---

# 65. Scale Route Cost

$$
\boxed{
C_\Sigma(\mathcal R)
=
C_{\downarrow}
+
C_{\mathrm{micro}}
+
C_{\uparrow}
+
C_{\mathrm{macro}}.
}
$$

---

# 66. Fine Is Not Always Better

若：

$$
C_{\downarrow}
+
C_{\mathrm{micro}}
>
C_{\mathrm{macro-approx}},
$$

且 approximation 足夠，則不應 refinement。

---

# 67. Coarse Is Not Always Better

若 macro chart 遺失重要 invariant：

$$
L_O>\theta,
$$

必須 refinement。

---

# 68. Resolution as Risk Control

高風險 action 可要求不得使用過粗抽象。

---

# 69. Financial Example

Inquiry 可 coarse。

真正 transfer 前要 refine identity、authorization、balance、recipient、limits 與 transaction state。

---

# 70. Compiler Example

macro：

```text
optimize function
```

可展開 CFG、SSA、dataflow、alias、vectorization、register allocation。

---

# 71. AI Agent Example

macro：

```text
complete research task
```

meso：

```text
search
retrieve
compare
reason
verify
write
cite
```

micro：

```text
tool calls
model invocations
memory reads
```

---

# 72. Adventure Land Example

macro：

```text
farm_cycle
```

meso：

```text
farm
restock
bank
return
```

micro：

```text
navigation
inventory
combat
state checks
```

---

# 73. Generative Agents Example

macro：

```text
persona_step
```

meso：

```text
perceive
retrieve
plan
reflect
execute
```

micro：

```text
memory nodes
embedding
LLM calls
retrieval scoring
```

---

# 74. Scale-Aware Crystallization

如果：

$$
\Gamma_\mu
$$

穩定：

$$
\Gamma_\mu
\rightarrow
\kappa_m.
$$

之後：

$$
\Gamma_m
\rightarrow
\kappa_M.
$$

---

# 75. Recursive Crystallization

$$
\boxed{
K^{(k+1)}
(
K^{(k)}
(
\Gamma^{(k-1)}
)
)
}
$$

形成 nested earned primitives。

---

# 76. Crystallization Tower

$$
\Gamma^{(-2)}
\rightarrow
\kappa^{(-1)}
\rightarrow
\kappa^{(0)}
\rightarrow
\kappa^{(+1)}.
$$

---

# 77. Tower 不等於永久封閉

任何：

$$
\kappa^{(k)}
$$

都可 reopening。

---

# 78. Cascading Reopen

底層 dependency 改變可能讓上層 crystal 連鎖 stale。

---

# 79. Invalidation Propagation

$$
\boxed{
\operatorname{Invalidate}
(
\kappa^{(k-1)}
)
\Rightarrow
\operatorname{Revalidate}
(
\kappa^{(k)}
).
}
$$

---

# 80. Scale Dependency Graph

$$
\boxed{
G_\Sigma
=
(V_\Sigma,E_\Sigma)
}
$$

可記錄 derived-from、refines、coarsens、validates、depends-on、invalidates。

---

# 81. Scale Graph 不等於 World

仍只是 runtime metadata。

---

# 82. Hidden Thickness Across Scale

Paper 04 的：

$$
\Delta(v)
=
(
\Delta_W,
\Delta_C,
\Delta_T,
\Delta_S
)
$$

應保留於 higher-scale primitive。

---

# 83. Thickness Accumulation

$$
\boxed{
\Delta_W^{(+1)}
=
\operatorname{Agg}
(
\Delta_W^{(0)}
)
}
$$

依 task 可用 sum / max / distribution。

---

# 84. Thickness Summary

可保存 resource envelope：

$$
\boxed{
\mathcal E_\Delta
=
(
W_{\min},
W_{\max},
D_{\max},
T_{\mathrm{p95}},
R_{\max}
).
}
$$

---

# 85. Resource Envelope

高層 point 即使 hop = 1，仍能估算 work、depth、latency 與 risk。

---

# 86. False Primitive

如果 hidden dependency / thickness 完全不可界定，應標：

$$
\boxed{
\text{opaque unit}
}
$$

而不是 earned primitive。

---

# 87. Opaque Unit ≠ Earned Primitive

$$
\boxed{
\text{Opaque Unit}
\neq
\text{Earned Primitive}.
}
$$

前者只是看不到；後者是驗證後不需平常展開。

---

# 88. Scale Authority

不是所有 observer 都有權：

$$
R_\downarrow.
$$

---

# 89. Authorized Refinement

$$
\boxed{
R_{\downarrow}^{a}
:
u^{(k)}
\rightarrow
\mathcal W^{(k-1)}.
}
$$

只有 actor $a$ 有 capability 才合法。

---

# 90. Authorized Coarsening

高風險 summary 也不能隨意生成，因為 aggregate 也可能洩漏資訊。

---

# 91. Safe Reachable World × Scale

$$
\boxed{
\mathcal W_{t,a}^{\mathrm{safe}}
=
\{
(D,\sigma):
\operatorname{Authorized}(a,D,\sigma)
\}.
}
$$

---

# 92. Visible ≠ Refinable

$$
\boxed{
\text{Visible}
\neq
\text{Refinable}.
}
$$

---

# 93. Refinable ≠ Executable

$$
\boxed{
\text{Refinable}
\neq
\text{Executable}.
}
$$

---

# 94. Responsibility Does Not Vanish Under Coarsening

$$
\boxed{
\text{Coarsening}
\not\Rightarrow
\text{Responsibility Erasure}.
}
$$

---

# 95. Multi-Resolution Validation

每一層可以有：

$$
V^{(k)}.
$$

---

# 96. Local Validation

驗 lower-scale implementation。

---

# 97. Cross-Scale Validation

驗：

$$
R_{\uparrow}
$$

是否保留 higher-level contract。

---

# 98. Reopen Validation

驗：

$$
R_{\downarrow}
$$

能否重建足夠 source structure。

---

# 99. Scale Round-Trip

$$
u^{(k)}
\xrightarrow{R_\downarrow}
\mathcal W^{(k-1)}
\xrightarrow{R_\uparrow}
\widehat{u}^{(k)}.
$$

要求：

$$
\boxed{
\widehat{u}^{(k)}
\simeq_q
u^{(k)}.
}
$$

---

# 100. 不要求 Bitwise Identity

Round-trip 可採 task-relative semantic equivalence。

---

# 101. Lossy Coarsening

若：

$$
R_\uparrow
$$

有 loss：

$$
L_\uparrow>0,
$$

必須明示。

---

# 102. Loss Budget

$$
\boxed{
L_\uparrow
\le
B_L(q).
}
$$

---

# 103. Task-Lossless

即使 global information 有 loss，只要 task invariants 保留，也可稱 task-lossless。

---

# 104. Scale-Relative Validity

宏觀 conclusion 應帶：

$$
\sigma
$$

而不是宣稱 absolute truth。

---

# 105. Resolution Certificate

```text
ResolutionCertificate
- domain
- world_revision
- active_scale
- task
- observer
- refinement_reason
- coarsening_reason
- fidelity
- loss_budget
- validation
- epoch
```

---

# 106. Refinement Receipt

```text
RefinementReceipt
- source_unit
- source_scale
- target_scale
- materialized_world
- authorization
- cost
- evidence
- validator
- expiry
```

---

# 107. Coarsening Receipt

```text
CoarseningReceipt
- source_world
- source_scale
- target_unit
- target_scale
- preserved_invariants
- information_loss
- hidden_thickness
- provenance
- invalidation
```

---

# 108. World-to-Primitive Certificate

應至少保存：

```text
source_world
valid_domain
compiled_route
semantic_contract
resource_envelope
temporal_causal_envelope
verification
provenance
reopen_pointer
lifecycle_state
```

---

# 109. Primitive-to-World Certificate

```text
primitive
reason_for_reopen
resolved_source
scale
version
authorization
reconstruction_fidelity
missing_sources
```

---

# 110. Missing Source

如果 source 消失，不可假裝 P2W 完整可逆。

應標：

$$
\boxed{
\text{reopenability degraded}.
}
$$

---

# 111. Partial Reopen

$$
\kappa
\rightarrow
\widehat{\mathcal W}
$$

可作 approximate reconstruction，但需標 fidelity。

---

# 112. Digest ≠ Crystal

$$
\boxed{
\text{digest}
\neq
\text{crystallized primitive}.
}
$$

Hash 不提供可執行 contract。

---

# 113. Summary ≠ Primitive

$$
\boxed{
\text{summary}
\neq
\text{executable crystal}.
}
$$

---

# 114. Model Weight ≠ Automatic Primitive

trained model 是否成為 earned primitive，仍取決於 contract、verification、version、provenance 與 fallback。

---

# 115. Macro / Micro Boundary 可以移動

今天：

$$
f()
$$

是 point。

debug 時：

$$
f()
\rightarrow
CFG
\rightarrow
instructions.
$$

---

# 116. Dynamic Scale Boundary

$$
\boxed{
B_\Sigma(t,q,O).
}
$$

---

# 117. Observer-Relative Scale

User、Compiler、Hardware Profiler 可以有不同 active frontier。

---

# 118. Same World, Different Active Frontier

$$
\mathcal F_{t,O_1}^{\mathrm{active}}
\neq
\mathcal F_{t,O_2}^{\mathrm{active}}.
$$

正常。

---

# 119. Shared World ≠ Shared Resolution

$$
\boxed{
\text{Shared World}
\neq
\text{Shared Active Resolution}.
}
$$

---

# 120. Scale-Constrained Route

$$
\sigma_{\min}
\le
\sigma(t)
\le
\sigma_{\max}.
$$

---

# 121. Forbidden Refinement

某些 domain 可禁止到過細 privacy scale。

---

# 122. Required Refinement

高風險操作前可以要求最低 audit resolution。

---

# 123. Scale-Aware Shortest Route

Paper 02 的 route optimization 現在加入 scale path：

$$
\boxed{
(\mathcal R^\*,\Sigma^\*)
=
\arg\min_{\mathcal R,\Sigma}
J(
\mathcal R,\Sigma
\mid
W,q,B,R
).
}
$$

---

# 124. Short Route May Require Deep Refinement

有時：

$$
R_\downarrow
$$

先花成本，反而找到更短 future path。

---

# 125. Value of Information

$$
\boxed{
VOI_{\downarrow}
=
E[
J_{\mathrm{before}}
-
J_{\mathrm{after}}
]
-
C_{\downarrow}.
}
$$

若：

$$
VOI_{\downarrow}>0,
$$

refinement 值得。

---

# 126. Value of Coarsening

$$
\boxed{
VOC_{\uparrow}
=
C_{\mathrm{maintain-fine}}
-
E[
C_{\mathrm{reopen}}
+
C_{\mathrm{loss}}
].
}
$$

---

# 127. Adaptive Resolution Policy

$$
\boxed{
\pi_\Sigma:
(
W,q,O,B,R,\mathcal H
)
\mapsto
\{
R_\downarrow,
R_\uparrow,
\operatorname{Stay}
\}.
}
$$

---

# 128. Scale-Route Co-Optimization

$$
\boxed{
(\Sigma^\*,\mathcal R^\*)
=
\arg\min
J(
\Sigma,\mathcal R
).
}
$$

---

# 129. Atlas Router

$$
\boxed{
\mathcal M_{\mathrm{atlas}}
:
(
W,q,O,B,R
)
\mapsto
(U_i,\chi_i,\sigma_i).
}
$$

---

# 130. Atlas Router → Corridor

$$
\mathcal M_{\mathrm{atlas}}
\rightarrow
\mathcal M_{\mathrm{corridor}}.
$$

---

# 131. Joint Router

更強：

$$
\boxed{
(\chi,\sigma,\mathcal R)
=
\mathcal M_{\mathrm{joint}}
(
W,q,B,R,\mathcal H
).
}
$$

---

# 132. Geometry × Scale

Paper 03 的 $g$ 與本文 $\sigma$ 不同。

同一 geometry 可存在多個 scale。

---

# 133. Geometry May Change under Coarsening

$$
\mathsf{Sf}^{(\mu)}
\rightarrow
\mathsf{Pt}^{(M)}.
$$

---

# 134. Geometry May Change under Refinement

$$
\mathsf{Pt}^{(M)}
\rightarrow
\mathsf{Cl}^{(m)}
\rightarrow
\mathsf{Ln}^{(\mu)}.
$$

---

# 135. Time × Scale

Paper 04 的 macro event：

$$
E^{(k)}
$$

可展開成 micro history：

$$
\mathcal H^{(k-1)}.
$$

---

# 136. Temporal Refinement

$$
R_{\downarrow}^{T}
\subset
R_{\downarrow}.
$$

---

# 137. Causal Refinement

`transaction` 展開成：

```text
authorize
reserve
write
verify
commit
```

是：

$$
R_{\downarrow}^{C}.
$$

---

# 138. State Refinement

$$
s^{(M)}
\rightarrow
(s_1,\ldots,s_n)^{(\mu)}.
$$

---

# 139. Geometry Refinement

$$
\mathsf{Pt}^{(M)}
\rightarrow
\mathsf{Cl}^{(\mu)}.
$$

---

# 140. Multi-Axis Refinement

實際 refinement 往往同時改：

$$
(
\sigma,
g,
\tau,
p,
\lambda,
O
).
$$

因此：

$$
\boxed{
R_{\downarrow}
=
\text{multi-axis chart refinement}.
}
$$

---

# 141. Refinement Path

$$
\chi_0
\rightarrow
\chi_1
\rightarrow
\cdots
\rightarrow
\chi_n.
$$

---

# 142. Refinement Path 本身也可最佳化

不同方法可由 source、trace、profiler、symbolic expansion、simulation 到達 target detail。

---

# 143. Coarsening Path 也可以不同

可選 summary、cluster、index、compile、model、crystal。

---

# 144. Scale Compilation

$$
\boxed{
\operatorname{SC}
:
\mathcal W^{(k-1)}
\rightarrow
\kappa^{(k)}.
}
$$

---

# 145. Scale Decompilation

$$
\boxed{
\operatorname{SD}
:
\kappa^{(k)}
\rightarrow
\mathcal W^{(k-1)}.
}
$$

不要求完全逆，只要求合法 reopen。

---

# 146. Lossless Audit Mode

高風險 domain 可要求 exact replay，而不是 task-relative reconstruction。

---

# 147. Archive as Scale Backstop

online runtime 不保留 micro materialization 時，archive 保存 canonical evidence。

---

# 148. Active Scale ≠ Available Historical Scale

$$
\boxed{
\text{Active Scale}
\neq
\text{Available Historical Scale}.
}
$$

---

# 149. Dormant World

lower-scale world 可以 dormant，不 active 但可重載。

---

# 150. Dormant ≠ Deleted

$$
\boxed{
\text{Dormant}
\neq
\text{Nonexistent}.
}
$$

---

# 151. Lazy Refinement

只有 task 需要時：

$$
R_\downarrow.
$$

---

# 152. Predictive Refinement

如果：

$$
P(\text{need micro soon})>\theta,
$$

可以提前展開。

---

# 153. Predictive Coarsening

長期不需要的 detail 可提早 de-materialize。

---

# 154. Scale Cache

最近展開的 lower-scale world 可暫存。

---

# 155. Scale Cache ≠ Crystal

cache 保存 materialization；crystal 保存成熟 computational primitive。

---

# 156. Resolution Policy Memory

Runtime 可以學習：

> 哪些 task 通常要展開到哪一層？

---

# 157. Repeated Refinement Path 可結晶

例如：

```text
macro alert
→ module
→ function
→ exact trace
```

反覆成功，可形成：

$$
\widehat{\ell}_{\downarrow}.
$$

---

# 158. Refinement Hyperlink

$$
\boxed{
\widehat{\ell}_{\downarrow}
:
u^{(k)}
\rightarrow
W_{\mathrm{target}}^{(k-n)}.
}
$$

跳過不必要中間 materialization。

---

# 159. Upward Crystallized Link

$$
\widehat{\ell}_{\uparrow}
:
W^{(k-n)}
\rightarrow
\kappa^{(k)}.
$$

---

# 160. Cross-Scale Path Compilation

$$
\boxed{
\operatorname{PC}_{\Sigma}
:
\mathcal R_{\mathrm{cross-scale}}
\rightarrow
\widehat{\ell}_{\Sigma}.
}
$$

---

# 161. Cross-Scale Crystal

$$
\boxed{
K_{\Sigma}
(
\widehat{\ell}_{\Sigma}
)
=
\kappa_{\Sigma}.
}
$$

---

# 162. Debug Crystal

若某 error pattern 的 macro symptom 反覆指向同一 micro evidence，可結晶成 diagnostic hyperlink。

---

# 163. Memory Crystal

high-level project crystal 可以按需展開到 source decision nodes，也是 cross-scale reveal。

---

# 164. Compiler Crystal

high-level source pattern 可以映射到 optimized lower-level execution form。

---

# 165. Multi-Scale Computational Diameter

$$
\boxed{
\operatorname{ECD}_{\Sigma,\Xi}(W)
=
\sup_{x,y}
d_{\Sigma,\Xi}(x,y).
}
$$

---

# 166. Crystallization Can Reduce Cross-Scale Diameter

cross-scale hyperlink 成熟後：

$$
\operatorname{ECD}_{t+1}
<
\operatorname{ECD}_{t}
$$

可能成立。

---

# 167. World Ontology 沒有因此縮小

下降的是 effective computational distance。

---

# 168. Scale Complexity Transfer

$$
C_{\mathrm{online-refine}}
\downarrow
$$

可能來自：

$$
C_{\mathrm{index}}
+
C_{\mathrm{crystal}}
+
C_{\mathrm{maintenance}}
\uparrow.
$$

---

# 169. Cross-Scale Cost Ledger

$$
\boxed{
C_{\mathrm{scale-total}}
=
C_{\mathrm{refine}}
+
C_{\mathrm{coarsen}}
+
C_{\mathrm{bridge}}
+
C_{\mathrm{validate}}
+
C_{\mathrm{maintain}}
+
C_{\mathrm{reopen}}.
}
$$

---

# 170. Amortized Scale Optimization

$$
C_{\mathrm{life}}
=
C_{\mathrm{build-scale-links}}
+
N C_{\mathrm{route}}
+
C_{\mathrm{maintenance}}.
$$

---

# 171. Scale-Optimal ≠ Route-Optimal

coarse scale 的 route 很短，information loss 仍可能過高。

---

# 172. Verification May Trigger Refinement

如果：

$$
V^{(k)}
<\theta_V,
$$

可只為驗證而：

$$
R_\downarrow.
$$

---

# 173. Verification-Only Refinement

$$
\boxed{
R_{\downarrow}^{V}.
}
$$

---

# 174. Observation-Only Refinement

$$
R_{\downarrow}^{O}.
$$

---

# 175. Execution Refinement

$$
R_{\downarrow}^{E}.
$$

三者不必相同。

---

# 176. Compute Fine, Observe Coarse

$$
\sigma_{\mathrm{compute}}
<
\sigma_{\mathrm{observe}}
$$

可以成立。

---

# 177. Compute Coarse, Observe Fine

可以插值成高解析 presentation，但必須標 observation loss。

---

# 178. Materialize Selectively

$$
\boxed{
\text{Compute Globally}
+
\text{Materialize Selectively}.
}
$$

---

# 179. Multi-Resolution Solve

多尺度 solver：

$$
S_\mu,
S_m,
S_M
$$

可共同工作。

---

# 180. Scale Coupling Port

$$
\boxed{
P_{\mu\leftrightarrow M}.
}
$$

---

# 181. AI-Native Distinction

AI 可以動態選：

- 是否 refinement；
- 到哪層；
- 哪個 chart；
- 哪種 geometry；
- 哪個 solver；
- 何時 coarsen。

---

# 182. Scale Selection 不能只靠 LLM Feel

需要 metrics、receipts、validation、replay 與 cost ledger。

---

# 183. Scale Benchmark

可比較：

### A

Always fine。

### B

Always coarse。

### C

Rule-based adaptive。

### D

AI adaptive + crystallized scale routes。

---

# 184. Metrics

至少：

```text
refinement_count
coarsening_count
scale_switches
active_nodes
materialized_state
route_cost
verification_cost
reopen_count
false_coarsening
false_refinement
information_loss
crystal_hit
```

---

# 185. False Coarsening

粗 abstraction 抹掉重要 dependency 導致錯誤決策。

---

# 186. False Refinement

不必要展開巨大 micro world 造成成本爆炸。

---

# 187. Premature Crystallization

尚未穩定就：

$$
W^{(k-1)}
\rightarrow
\kappa^{(k)}
$$

會隱藏 unresolved structure。

---

# 188. Over-Refinement

永遠追求：

$$
\sigma\rightarrow-\infty
$$

不可能 operationally complete。

---

# 189. Infinite Regress

每個 primitive 都可再問「裡面還有什麼」，但 Runtime 不需回答到宇宙終極原子。

---

# 190. Operational Stopping Condition

若：

$$
VOI_{\downarrow}\le0
$$

或 budget 不足，停止 refinement。

---

# 191. Sufficient Resolution

$$
\boxed{
\operatorname{SufficientResolution}
(
\sigma
\mid
q,B,R
)=1.
}
$$

---

# 192. Task-Sufficient ≠ Ontologically Final

$$
\boxed{
\text{task-sufficient}
\neq
\text{ontologically final}.
}
$$

---

# 193. No Final Macro Required

向上同樣可以無界，但本文不宣稱存在一個 ultimate primitive 包含宇宙。

---

# 194. Scale-Relative Globality

$$
\boxed{
\mathrm{Global}_{W^{(k)}}(U)
\land
\mathrm{Local}_{W^{(k+1)}}(U).
}
$$

---

# 195. Macro Ascent and Global Computation

macro ascent 可以理解為：

> 把 lower-level global coherent world 提升成 higher-level local primitive。

---

# 196. Global-to-Local Primitive

$$
\boxed{
\text{Global}^{(k)}
\rightarrow
\text{Local Primitive}^{(k+1)}.
}
$$

---

# 197. Local-to-World Refinement

$$
\boxed{
\text{Local Primitive}^{(k+1)}
\rightarrow
\text{Global World}^{(k)}.
}
$$

---

# 198. Scale Duality

$$
\boxed{
\text{Global}^{(k)}
\leftrightarrow
\text{Local}^{(k+1)}.
}
$$

---

# 199. Macro Primitive as Contract

higher-scale primitive 主要保存：

- input；
- output；
- guard；
- side effects；
- resource envelope；
- verification；
- provenance；
- reopen pointer。

---

# 200. Contract Is Scale Boundary

API contract 可以是 scale boundary 的工程表示。

---

# 201. API 不自動代表 Good Boundary

若 abstraction leakage 很大，scale boundary 不穩定。

---

# 202. Boundary Stability

$$
\boxed{
S_B(u)
=
f(
\text{contract stability},
\text{dependency stability},
\text{error containment},
\text{reopen frequency}
).
}
$$

---

# 203. Frequent Reopen 是警訊

若：

$$
f_{\mathrm{reopen}}\gg1,
$$

可能表示 abstraction 太粗、environment 漂移或 guard 太弱。

---

# 204. Crystal Demotion

$$
\text{hot}
\rightarrow
\text{warm}
\rightarrow
\text{cold}
\rightarrow
\text{stale}.
$$

並可能向下重新展開。

---

# 205. Scale Lifecycle

```text
raw
observed
structured
compiled
crystallized
coarse-stable
reopened
revalidated
retired
```

---

# 206. Scale History

必須保存：

$$
\mathcal H_\Sigma.
$$

---

# 207. Same Primitive State ≠ Same Scale History

兩個 hot crystal 可能來源與驗證成熟度完全不同。

---

# 208. Scale Provenance

$$
\boxed{
\text{scale provenance}
}
$$

是一級資料。

---

# 209. Cross-Scale Responsibility

高層 primitive 出錯可向下 trace：

$$
\kappa^{(k)}
\rightarrow
\kappa^{(k-1)}
\rightarrow
\mathcal H^{(k-2)}.
$$

---

# 210. Cross-Scale Explanation

AI 可以回答：

> 為什麼這一整組 operation 被當成一？

並展開 provenance。

---

# 211. Human-Readable Projection

人類不必讀全部 micro details，只需：

- abstraction；
- confidence；
- reason；
- drill-down path。

---

# 212. AI-Native Internal Scale

AI 可使用比人類 UI 更細或更異質的 internal atlas，但仍要保留可審計 projection。

---

# 213. Scale Portability

primitive 跨 runtime 搬移時，reopen pointer、contract 與 resource envelope 需要可移植。

---

# 214. Portable Macro Contract ≠ Portable Micro Implementation

$$
\boxed{
\text{portable macro contract}
\neq
\text{portable micro implementation}.
}
$$

---

# 215. Portable Crystal

較容易移植的是：

- semantic contract；
- provenance；
- tests；
- interface；
- guards。

實作可重編譯。

---

# 216. Cross-Provider Recrystallization

$$
\kappa_A^{(k)}
\rightarrow
W_B^{(k-1)}
\rightarrow
\kappa_B^{(k)}.
$$

---

# 217. Mathematical World Atlas

對數學研究，一個 theorem-level point 可展開成 lemmas、definitions、experiments、formal proof 與 counterexample search。

---

# 218. Proof-to-Primitive

形式驗證 derivation：

$$
\Pi
$$

可成 higher-scale reusable lemma primitive。

---

# 219. Lemma Reopening

$$
\text{Lemma}
\rightarrow
\text{Proof Object}.
$$

---

# 220. MWT 的自然接口

MWT 同時容納 object、proof、computation、observer、presentation；UNPNP-II 負責它們的尺度路由。

---

# 221. 24／72 Across Scale

每層：

$$
p^{(k)}
\in
\mathfrak P_{24},
$$

$$
\lambda^{(k)}
\in
\mathfrak L_3.
$$

---

# 222. Scale Transition Can Change Form

$$
p^{(k)}
\neq
p^{(k+1)}
$$

正常。

---

# 223. Example

micro：

$$
D\text{-}P\text{-}D-F
$$

macro：

$$
D\text{-}R\text{-}D-F.
$$

底層 parallel computation 在高層成 recognition primitive。

---

# 224. This Is Not O(0) Magic

高層 recognition 仍攜帶 hidden build / execution thickness。

---

# 225. Local Metadata

一個 unit 的 local configuration 可寫：

$$
\boxed{
c_i^{(k)}
=
\langle
\sigma_i,
g_i,
p_i,
\lambda_i,
\Theta_i,
O_i
\rangle.
}
$$

---

# 226. Multi-Scale Route Object

Paper 03 的 route object 可加入 scale：

$$
\boxed{
\mathcal R_\Sigma
=
\langle
U,E,H,\preceq,\mathcal K,\mathcal F,\Sigma,\Pi,\Theta
\rangle.
}
$$

---

# 227. Route Segment Carries Scale

$$
r_i
=
\langle
u_i,
u_j,
\sigma_i,
\sigma_j,
g_i,
p_i,
\lambda_i
\rangle.
$$

---

# 228. Cross-Scale Edge

若：

$$
\sigma_i\neq\sigma_j,
$$

則是 cross-scale transition。

---

# 229. Scale-Conserving Edge

若：

$$
\sigma_i=\sigma_j,
$$

為 within-scale transition。

---

# 230. Scale Jump

若跨多層 direct hyperlink，需要更強 validation。

---

# 231. Jump Is Not Skip of Obligations

可跳 representation，不可跳 authorization、invariants、causality、proof obligations。

---

# 232. Cross-Scale Validator

$$
\boxed{
V_\Sigma(r_i)
}
$$

驗 target correctness、fidelity、hidden dependency、permissions 與 resource envelope。

---

# 233. Scale Safety

過粗可能漏風險，過細可能暴露敏感資訊。

---

# 234. Safe Resolution Interval

$$
\boxed{
\sigma
\in
[
\sigma_{\mathrm{privacy}},
\sigma_{\mathrm{safety}}
].
}
$$

---

# 235. Actor-Specific Safe Interval

$$
\Sigma_a^{\mathrm{safe}}
\neq
\Sigma_b^{\mathrm{safe}}.
$$

---

# 236. Scale as Capability

能力包可包含：

```text
can_refine_to_level
can_reopen_crystal
can_view_micro_provenance
can_execute_micro_tools
```

---

# 237. Scale-Aware Authorization

$$
\boxed{
\operatorname{Auth}
(
a,D,\sigma,op
).
}
$$

---

# 238. Refinement Attack Surface

更細資料可能包含 secrets、credentials、private memory 或 internal prompts。

因此：

$$
R_\downarrow
$$

是 security-sensitive action。

---

# 239. Coarsening Can Leak Aggregates

summary 也可能洩漏 aggregate information，所以 $R_\uparrow$ 同樣需 privacy analysis。

---

# 240. Scale-Safe Hyperlink

cross-scale hyperlink 必須綁 actor、purpose、scope、expiry、projection policy。

---

# 241. Semantic Validity ≠ Accessibility

$$
\boxed{
\text{Valid}
\neq
\text{Accessible}.
}
$$

---

# 242. Active Frontier Scheduling

Runtime 要決定哪些 domain 值得保持 fine。

---

# 243. Frontier Budget

$$
\boxed{
\sum_{D_i\in\mathcal F_t}
C_{\mathrm{active}}(D_i)
\le
B_t.
}
$$

---

# 244. Frontier Optimization

$$
\boxed{
\mathcal F_t^\*
=
\arg\max_{\mathcal F}
\sum_i
U_\sigma(D_i)
}
$$

subject to budget。

---

# 245. Priority

高優先：

- uncertainty；
- risk；
- novelty；
- active failure；
- verification debt。

低優先：

- stable；
- repetitive；
- well-crystallized。

---

# 246. Crystallization Frees Frontier Budget

lower-scale world 升成 hot primitive 後可釋放 active budget。

---

# 247. Reopen Consumes Frontier Budget

大量 stale crystal 會造成 resource pressure。

---

# 248. Scale Breathing

健康 Runtime 應：

$$
\boxed{
\text{Refine}
\rightarrow
\text{Solve}
\rightarrow
\text{Crystallize}
\rightarrow
\text{Coarsen}
\rightarrow
\text{Reopen when needed}.
}
$$

---

# 249. Scale Breathing 與 ELC

Expansion 可對應 refinement；Linking 建 cross-scale / cross-domain bridge；Convergence 可對應 coarsening / crystallization。

但兩者不完全同義。

---

# 250. Combined Loop

$$
\boxed{
R_\downarrow
\rightarrow
E
\rightarrow
L
\rightarrow
C
\rightarrow
K
\rightarrow
R_\uparrow.
}
$$

---

# 251. Reality Demands Reopen

若新 evidence 到來，再：

$$
R_\downarrow.
$$

---

# 252. Dynamic Fixed Point at Scale

stable primitive 更像：

$$
K_t
\simeq
K_{t+1}
$$

在一定 epoch 下穩定。

---

# 253. World Change May Shift Optimal Scale

$$
W_t\rightarrow W_{t+1}
$$

可以使：

$$
\sigma_t^\*
\neq
\sigma_{t+1}^\*.
$$

---

# 254. Learning Is Scale Reorganization

系統學到的不只是 knowledge，也包括：

> 哪些東西未來不必再展開那麼細？

---

# 255. Healthy Forgetting as Coarsening

只要保留 provenance，將 low-value micro detail 從 active world 移出不等於 destructive forgetting。

---

# 256. Active De-materialization ≠ Canonical Deletion

$$
\boxed{
\text{active de-materialization}
\neq
\text{canonical deletion}.
}
$$

---

# 257. AI Memory Interface

working context 可 coarse，canonical memory 保留 source。

---

# 258. Retrieval Is Refinement

$$
\boxed{
\text{Crystal First}
\rightarrow
\text{Source on Demand}
}
$$

是一種 memory-scale refinement。

---

# 259. Semantic Crystal as Macro Point

$$
\kappa_M
$$

可視為 memory world 的 macro point。

---

# 260. Source Nodes as Micro World

$$
\{m_1,\ldots,m_n\}
$$

是其 lower-scale support。

---

# 261. Memory Reopen

$$
\kappa_M
\rightarrow
\{m_i\}.
$$

符合 P2W。

---

# 262. Scale-Aware Search

Search router 可先選：

```text
summary
crystal
document
paragraph
event
raw source
```

哪一層足夠。

---

# 263. Memory Scale Pareto

$$
\boxed{
\operatorname{ParetoMin}
(
C_{\mathrm{search}},
L_{\mathrm{semantic}},
C_{\mathrm{context}}
).
}
$$

---

# 264. Generalization

同一原理適用 code、simulation、proof、workflow、distributed system、game world。

---

# 265. 底空間套底空間

每個：

$$
\mathcal B_i^{(k)}
$$

可包含：

$$
\{
\mathcal B_{i,1}^{(k-1)},
\ldots
\}.
$$

---

# 266. Nested Subspaces

$$
\boxed{
\mathcal B^{(k)}
\supset
\mathcal B^{(k-1)}
\supset
\mathcal B^{(k-2)}
}
$$

只是其中一種 nesting。

---

# 267. Overlapping Subspaces

不要求樹狀，也可 DAG / hypergraph / cover。

---

# 268. Scale Structure 不一定是 Tree

因此：

$$
\Sigma
$$

更適合是 partially ordered scale relation。

---

# 269. Scale Poset

$$
\boxed{
(\Sigma,\preceq_\Sigma).
}
$$

---

# 270. Multiple Refinement Axes

object 可沿 spatial、temporal、semantic、causal、code、observer 等不同方向 refinement。

---

# 271. Scale Vector

更一般：

$$
\boxed{
\boldsymbol{\sigma}
=
(
\sigma_S,
\sigma_T,
\sigma_C,
\sigma_M,
\sigma_O
).
}
$$

---

# 272. Scalar Scale 只是簡化

v0.1 可先用單 $k$ 推理，但保留 vector-scale extension。

---

# 273. Anisotropic Refinement

只展開 causal dimension：

$$
\sigma_C\downarrow
$$

而其他維度不變。

---

# 274. Multi-Dimensional Active Frontier

$$
\boxed{
\mathcal F_t
\subset
\Sigma_1\times\cdots\times\Sigma_m.
}
$$

---

# 275. 工程 MVP 不必一次做完

第一版可以只用：

```text
coarse
medium
fine
```

三級。

---

# 276. 理論保持可擴張

避免把 MVP 限制誤認成 ontology。

---

# 277. 第一條核心定律

$$
\boxed{
\textbf{
A computational primitive may be a compressed world at a finer scale.
}
}
$$

---

# 278. 第二條核心定律

$$
\boxed{
\textbf{
Unbounded refinement does not require unbounded active materialization.
}
}
$$

---

# 279. 第三條核心定律

$$
\boxed{
\textbf{
Coarsening is not crystallization unless the higher-scale unit earns executable and verifiable primitive status.
}
}
$$

---

# 280. 第四條核心定律

$$
\boxed{
\textbf{
Every promoted primitive must retain lawful reopenability or explicitly declare its loss.
}
}
$$

---

# 281. 第五條核心定律

$$
\boxed{
\textbf{
Global at one scale may be local at another scale.
}
}
$$

---

# 282. 第六條核心定律

$$
\boxed{
\textbf{
One World does not imply one resolution, one geometry, one observer, or one computational form.
}
}
$$

---

# 283. 對 Paper 01 的收束

Paper 01 問「什麼算一？」；本文回答：一可以來自一整個 lower-scale world 的合法收斂與結晶。

---

# 284. 對 Paper 02 的收束

Paper 02 說 shortest 是 relative；本文加入 scale route 本身進 optimization。

---

# 285. 對 Paper 03 的收束

Paper 03 說 geometry 可 heterogeneous；本文說 geometry 可以隨 refinement / coarsening 跨尺度改變。

---

# 286. 對 Paper 04 的收束

Paper 04 說 macro event 具有 temporal-causal thickness；本文將 thickness 保留為高層 primitive metadata。

---

# 287. 對 UNPNP-I 的收束

Path Compilation：

$$
\Gamma
\rightarrow
\widehat{\ell}.
$$

Crystallization：

$$
\widehat{\ell}
\rightarrow
\kappa.
$$

本文擴張：

$$
\boxed{
\mathcal W^{(k-1)}
\rightarrow
\Gamma^{(k-1)}
\rightarrow
\widehat{\ell}^{(k)}
\rightarrow
\kappa^{(k)}.
}
$$

---

# 288. 對 MWT 的接口

World primitive 不被拆成唯一 canonical tuple；refinement 作用的是 presentation / runtime world。

---

# 289. 對 GCM 的接口

domain / resolution / materialization / observer 可被 Scale Policy 動態選擇。

---

# 290. 對 24／72 的接口

每一 scale 可以有自己的：

$$
p^{(k)},
\lambda^{(k)}.
$$

---

# 291. 下一篇：24／72 作為局部路徑語法

前五篇完成多尺度底座。

Paper 06 將回答：

> **一條跨尺度 route 的每一段，到底如何標記它使用的是哪種 computational form 與 transition law？**

---

# 292. Paper 06 預告

## 24／72 作為局部路徑語法
### Computational Forms and Transition Laws as Local Route Semantics

將定義：

$$
\boxed{
r_i
=
\langle
B_i,
U_i,
O_i,
L_i,
g_i,
\sigma_i,
\Theta_i
\rangle.
}
$$

並研究：

$$
P5^F
\rightarrow
P11^F
\rightarrow
P17^K
\rightarrow
P23^F
$$

這種跨範式、跨轉移律、跨幾何、跨尺度 route。

---

# 結論

如果一個 high-level function、algorithm、agent action 或 computational crystal 被視為一個「點」，不代表它下面什麼都沒有。

相反：

$$
\boxed{
\text{Point}^{(k)}
\rightarrow
\text{World}^{(k-1)}
}
$$

可以是一個正常 refinement relation。

而 lower-scale world 經過路徑辨識、編譯、驗證、domain 界定與 lifecycle 評估後，也可以：

$$
\boxed{
\text{World}^{(k-1)}
\rightarrow
\text{Primitive}^{(k)}.
}
$$

因此多尺度 computational world 的基本呼吸是：

$$
\boxed{
\text{Refine}
\rightarrow
\text{Compute}
\rightarrow
\text{Verify}
\rightarrow
\text{Crystallize}
\rightarrow
\text{Coarsen}
\rightarrow
\text{Reopen when needed}.
}
$$

但這個世界不能靠「全部展開」運行。

它必須遵守：

$$
\boxed{
\text{Finite Active Support}
+
\text{Unbounded Refinement}.
}
$$

所以真正的多尺度 AI-native Runtime 不是永遠看得最細，而是：

> **在有限資源下，持續決定哪裡需要往下展開、哪裡可以向上結晶、哪些世界可以暫時休眠，以及哪些已經被壓成一個點的世界必須重新被打開。**

最終，本篇可以壓成：

$$
\boxed{
\textbf{
微觀不是永遠的底，
宏觀也不是永遠的頂；
一個世界可以成為一個點，
一個點也可以重新打開成一個世界。
}
}
$$

這就是 UNPNP-II 從「多尺度路徑」正式進入「遞歸計算世界」的關鍵接口。
