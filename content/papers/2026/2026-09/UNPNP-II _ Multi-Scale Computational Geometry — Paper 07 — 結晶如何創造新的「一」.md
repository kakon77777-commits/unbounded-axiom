# UNPNP-II / Multi-Scale Computational Geometry — Paper 07
## 結晶如何創造新的「一」
### From Macro Packaging to Earned Primitives: Syntactic, Topological, Causal, Semantic, and Physical Compression

**系列名稱：** UNPNP-II｜Multi-Scale Computational Geometry  
**系列中文名：** UNPNP 第二層：多尺度計算幾何與相對最短路徑  
**篇次：** Paper 07 / 08  
**作者：** Neo.K with Aletheia（GPT）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-09  
**文件性質：** 計算結晶化／新原語生成／路徑編譯／多尺度計算論  
**前置：** UNPNP-I Series 06–08；UNPNP-II Paper 01–06；MWT；GCM  
**狀態：** Canonical Draft

---

## 摘要

UNPNP-II 的起點是：

> **計算的一到底是什麼？**

Paper 01 指出，「一」不是天然原子，而是 computational chart-relative unit；Paper 02 指出最短 route 必須相對 world、observer、metric 與 objective；Paper 03–05 分別建立 dependency geometry、time-causal thickness 與 recursive refinement / coarsening；Paper 06 則將 24／72 重新定位為 local route semantics。

現在可以回到最尖銳的問題：

> **當十個、百個甚至百萬個 lower-scale operations 被稱為一個 function、macro、API、algorithm 或 crystal 時，究竟什麼時候只是「看起來是一」，什麼時候才真的產生新的 computational primitive？**

本文提出六層「一」：

$$
\boxed{
1_{\mathrm{syn}},
1_{\mathrm{if}},
1_{\mathrm{top}},
1_{\mathrm{causal}},
1_{\mathrm{sem}},
1_{\mathrm{phy}}
}
$$

分別表示：

1. syntactic one；
2. interface one；
3. topological one；
4. causal one；
5. semantic one；
6. physical one。

本文的核心主張是：

$$
\boxed{
1_{\mathrm{syn}}
\not\Rightarrow
1_{\mathrm{top}}
\not\Rightarrow
1_{\mathrm{causal}}
\not\Rightarrow
1_{\mathrm{phy}}.
}
$$

把十個步驟包進：

```text
macro FastAction()
```

只能保證：

$$
1_{\mathrm{syn}}
$$

或：

$$
1_{\mathrm{if}}.
$$

若底層仍完整執行：

$$
a_1
\rightarrow
a_2
\rightarrow
\cdots
\rightarrow
a_{10},
$$

則：

$$
W=10,
\qquad
D_C=10
$$

仍可能不變。

因此：

$$
\boxed{
\text{one call}
\neq
\text{one computational transition}.
}
$$

本文將真正的 earned primitive 定義為：

$$
\boxed{
\kappa
=
\operatorname{Promote}
(
\widehat{\mathcal R},
D,
G,
V,
U,
P,
F
)
}
$$

其中：

- $\widehat{\mathcal R}$：compiled route；
- $D$：valid domain；
- $G$：guards；
- $V$：verification maturity；
- $U$：lifecycle utility；
- $P$：provenance；
- $F$：fallback / reopen path。

只有當一個 lower-scale route 不只是被重新命名，而是其：

- traversal topology；
- causal structure；
- intermediate materialization；
- reasoning / search requirement；
- verification path；
- runtime cost；

至少有部分被真正改寫，並且：

$$
\boxed{
J_{\mathrm{life}}(\kappa)
<
J_{\mathrm{life}}(\mathcal R)
}
$$

在指定有效域中成立時，才可稱為 **Computational Reunitization**。

本文因此提出：

$$
\boxed{
\text{Crystallization}
=
\text{Verified Reunitization Across Scale}.
}
$$

更進一步：

$$
\boxed{
\text{Path}^{(k-1)}
\rightarrow
\text{Primitive}^{(k)}
}
$$

不是「把下層工作消失」，而是：

> **把下層已成熟、可驗證、可重用的計算世界，轉換成上層不再需要反覆展開的 earned primitive。**

所以結晶真正創造的新「一」具有兩個同時成立的條件：

$$
\boxed{
\text{Compression}
+
\text{Reopenability}.
}
$$

它必須能被當成一，也必須在 failure、audit、shift 或 invalidation 時重新被打開。

---

# 1. 問題：十個變成一個，到底發生了什麼？

假設：

$$
\Gamma
=
a_1
\rightarrow
a_2
\rightarrow
\cdots
\rightarrow
a_{10}.
$$

現在定義：

```text
FastAction()
```

使 caller 只需：

```text
FastAction()
```

這時：

$$
H_{\mathrm{interface}}
=
1.
$$

但這不告訴我們：

$$
W,
D_C,
T,
M,
V
$$

是否改變。

---

# 2. 第一種一：Syntactic One

如果 source code 中：

```text
FastAction()
```

只佔一個 symbol / AST call，

稱：

$$
\boxed{
1_{\mathrm{syn}}.
}
$$

---

# 3. Syntactic Compression

$$
\Gamma
\rightarrow
\operatorname{Name}(\Gamma).
$$

這是：

$$
\boxed{
\text{naming compression}.
}
$$

---

# 4. Naming Compression 不改 Execution

若 runtime 仍：

$$
a_1
\rightarrow
\cdots
\rightarrow
a_{10},
$$

則：

$$
W'=W.
$$

---

# 5. 第二種一：Interface One

API 對 caller 暴露：

```text
POST /do_all
```

稱：

$$
\boxed{
1_{\mathrm{if}}.
}
$$

---

# 6. Interface One 可以隱藏巨大 World

一個 API call 可以內含：

- database；
- network；
- LLM；
- GPU；
- multi-agent workflow。

所以：

$$
\boxed{
1_{\mathrm{if}}
\neq
1_{\mathrm{phy}}.
}
$$

---

# 7. 第三種一：Topological One

如果原本 route：

$$
B_1
\rightarrow
B_2
\rightarrow
\cdots
\rightarrow
B_n
$$

被真正改成：

$$
B_1
\xrightarrow{\widehat{\ell}}
B_n,
$$

且中間 traversal 不再是 ordinary routing 的必要一級結構，

則可形成：

$$
\boxed{
1_{\mathrm{top}}.
}
$$

---

# 8. Topological Compression

$$
\boxed{
\mathsf{Ln}
\rightarrow
\mathsf{Jl}
}
$$

或：

$$
\boxed{
\mathsf{Ln}
\rightarrow
\mathsf{Pt}
}
$$

是典型 geometry rewrite。

---

# 9. Topological One 仍不等於 Causal One

新的 direct edge：

$$
\widehat{\ell}
$$

內部可能仍保留：

$$
a_1
\prec
a_2
\prec
\cdots
\prec
a_{10}.
$$

所以：

$$
D_C
$$

未必下降。

---

# 10. 第四種一：Causal One

若原本必要 causal chain：

$$
a_1
\prec
a_2
\prec
\cdots
\prec
a_{10}
$$

透過重新演算法化、預計算、fusion、parallelization 或新 primitive，

變成：

$$
D_C'=1
$$

或顯著下降，

才形成：

$$
\boxed{
1_{\mathrm{causal}}
}
$$

在指定尺度上的強版本。

---

# 11. Causal Compression

$$
\boxed{
D_C'
<
D_C.
}
$$

---

# 12. Parallelization Can Create Causal Compression

若十個 task 原本被錯誤序列化：

$$
D_C=10
$$

而實際可：

$$
a_1\parallel\cdots\parallel a_{10},
$$

則：

$$
D_C'=1.
$$

---

# 13. 但 Work 仍可能是十

所以：

$$
W'=10.
$$

因此：

$$
\boxed{
1_{\mathrm{causal}}
\neq
1_{\mathrm{phy}}.
}
$$

---

# 14. 第五種一：Semantic One

如果對 task contract：

$$
q,
$$

整段 route：

$$
\Gamma
$$

已可合法視為一個不可再區分的 task primitive，

則形成：

$$
\boxed{
1_{\mathrm{sem}}.
}
$$

---

# 15. Example

對 user：

```text
submit_tax_return()
```

可以是一個 semantic action。

但內部可能有數十個驗證、簽章與傳輸。

---

# 16. Semantic One 需要 Contract

$$
\boxed{
C_{\mathrm{sem}}
=
\langle
I,
G,
O,
S,
V
\rangle.
}
$$

其中：

- $I$：input contract；
- $G$：guard；
- $O$：output；
- $S$：side effects；
- $V$：validator。

---

# 17. Semantic One ≠ Arbitrary Label

如果 caller 所需 relevant invariants 無法由單一 contract 保留，

則：

$$
1_{\mathrm{sem}}
$$

不成立。

---

# 18. 第六種一：Physical One

最強版本：

$$
\boxed{
1_{\mathrm{phy}}.
}
$$

表示在指定 physical machine model 下，原本多階 physical work 真正被更少 physical operations / lower energy / lower data movement 取代。

---

# 19. Physical One 是 Model-Relative

不宣稱宇宙終極原子。

只是：

> 在指定 machine / physical accounting model 中，這段運算已被實際 reduction。

---

# 20. 六個 One 的關係

一般：

$$
1_{\mathrm{phy}}
\Rightarrow
1_{\mathrm{top}}
$$

常常成立，

但不必：

$$
1_{\mathrm{sem}}
\Rightarrow
1_{\mathrm{phy}}.
$$

---

# 21. Weak One

只滿足：

$$
1_{\mathrm{syn}}
+
1_{\mathrm{if}}
$$

稱：

## Weak One

---

# 22. Structural One

滿足：

$$
1_{\mathrm{top}}
$$

稱：

## Structural One

---

# 23. Causal One

滿足：

$$
D_C'\ll D_C.
$$

---

# 24. Semantic One

task contract closure 成立。

---

# 25. Strong Computational One

本文提出：

$$
\boxed{
1_{\mathrm{comp}}
=
1_{\mathrm{top}}
+
1_{\mathrm{sem}}
+
\Delta J>0
}
$$

作為第一版強計算單位。

---

# 26. Strong Physical One

如果再有：

$$
W'\ll W
$$

或：

$$
E'\ll E,
$$

可接近：

$$
1_{\mathrm{phy}}.
$$

---

# 27. Crystallization 不要求 Physical One

這點非常重要。

一個 crystal 可以是非常有價值的 earned primitive，

即使其內部仍需要大量 physical work。

---

# 28. 為什麼？

因為它可能降低：

- route search；
- reasoning；
- coordination；
- verification；
- materialization；
- latency。

---

# 29. Example：Compiled Database Query

底層仍做大量 I/O，

但 query planning 不再每次重做。

---

# 30. Example：Model Inference

底層矩陣計算巨大，

但對 caller：

$$
1_{\mathrm{sem}}
+
1_{\mathrm{top}}
$$

都可能成立。

---

# 31. Example：GPU Kernel

一個 launch 是：

$$
1_{\mathrm{if}}
$$

但內部：

$$
W\gg1.
$$

---

# 32. Example：Perfect Hash

可能同時：

- topological；
- semantic；
- low online work；

非常接近強 earned primitive。

---

# 33. Macro Packaging

若：

```text
macro M():
  a1()
  ...
  a10()
```

則：

$$
\boxed{
1_{\mathrm{syn}}
+
1_{\mathrm{if}}
}
$$

成立。

---

# 34. 但如果：

$$
W'=W,
D_C'=D_C,
T'\approx T,
$$

則：

$$
\boxed{
\text{Macro Packaging}
\neq
\text{Computational Reunitization}.
}
$$

---

# 35. Memoization

保存：

$$
M[x]=y.
$$

下一次：

$$
x\rightarrow y.
$$

這可以形成：

$$
1_{\mathrm{top}}
$$

與低 online work。

---

# 36. 但 Memoization 依賴 Input Recurrence

所以：

$$
\boxed{
\text{memoization}
\neq
\text{general path compilation}.
}
$$

---

# 37. Trace Cache

保存 execution trace。

可降低 planning / routing，

但不一定改 data processing。

---

# 38. Stage Fusion

兩 stage：

$$
A\rightarrow B
$$

融合：

$$
F_{AB}.
$$

可能降低：

- materialization；
- memory traffic；
- synchronization。

---

# 39. Stage Fusion 更接近 Topological / Physical Compression

尤其如果中間 state 不再 materialize。

---

# 40. Algorithmic Rewriting

例如：

$$
O(n^2)
\rightarrow
O(n\log n).
$$

這是真正 work structure 改寫。

---

# 41. Semantic Recompilation

如果原 route 的意義被重新表示成更短 executable form：

$$
\operatorname{Semantics}(\Gamma)
\simeq
\operatorname{Semantics}(\widehat{\Gamma}).
$$

---

# 42. Path Compilation

UNPNP-I 已定義：

$$
\operatorname{PC}(\Gamma)
=
\widehat{\ell}.
$$

---

# 43. Paper 07 將 Path Compilation 放入 Reunitization

$$
\boxed{
\operatorname{PC}
\subset
\operatorname{Reunitize}.
}
$$

---

# 44. Reunitization

定義：

$$
\boxed{
\operatorname{RU}
:
\mathcal R^{(k-1)}
\rightarrow
u^{(k)}.
}
$$

---

# 45. 不是所有 RU 都成功

candidate：

$$
u_c^{(k)}
$$

先進 validation。

---

# 46. Earned Primitive

只有：

$$
\operatorname{Promote}(u_c)=1
$$

才成：

$$
\kappa.
$$

---

# 47. Promotion Conditions

第一版：

$$
\boxed{
S(\kappa)\ge\theta_S
}
$$

$$
\boxed{
V(\kappa)\ge\theta_V
}
$$

$$
\boxed{
U(\kappa)>0
}
$$

$$
\boxed{
R(\kappa)\le\theta_R.
}
$$

---

# 48. Stability

$$
S(\kappa)
=
f(
\text{repeatability},
\text{dependency stability},
\text{domain stability},
\text{version stability}
).
$$

---

# 49. Verification

可由：

- differential test；
- property test；
- replay；
- formal proof；
- statistical validation；
- shadow run；

累積。

---

# 50. Utility

$$
\boxed{
U(\kappa)
=
B_{\mathrm{runtime}}
+
B_{\mathrm{future}}
+
B_{\mathrm{context}}
-
C_{\mathrm{compile}}
-
C_{\mathrm{verify}}
-
C_{\mathrm{maintain}}
-
C_{\mathrm{select}}
-
C_{\mathrm{risk}}.
}
$$

---

# 51. Valid Domain

$$
\boxed{
D_\kappa.
}
$$

primitive 只在 $D_\kappa$ 內有效。

---

# 52. Guard

$$
\boxed{
G_\kappa(x)=1
}
$$

才允許 fast path。

---

# 53. Outside Domain

若：

$$
G_\kappa(x)=0,
$$

必須：

$$
\text{slow path}
$$

或：

$$
\text{deny}.
$$

---

# 54. Provenance

$$
\boxed{
P_\kappa.
}
$$

記來源 route、version、evidence、compiler history。

---

# 55. Fallback

$$
\boxed{
F_\kappa.
}
$$

記 decrystallization / original route。

---

# 56. Reopen Pointer

$$
\boxed{
\operatorname{Reopen}(\kappa)
\rightarrow
\mathcal R_{\mathrm{source}}.
}
$$

---

# 57. Crystallization Definition

本文定義：

$$
\boxed{
\operatorname{Crystallize}
=
\operatorname{Promote}
\circ
\operatorname{Verify}
\circ
\operatorname{Compile}.
}
$$

---

# 58. 但不是所有 Compiler Output 都是 Crystal

$$
\boxed{
\text{compiled}
\neq
\text{crystallized}.
}
$$

---

# 59. Candidate

剛編譯：

$$
\widehat{\ell}
$$

先是 candidate。

---

# 60. Cold

初步驗證。

---

# 61. Warm

反覆成功。

---

# 62. Hot

高頻、穩定、guard cheap、validator mature。

---

# 63. Stale

dependency / version / policy 漂移。

---

# 64. Retired

不再值得使用。

---

# 65. New One Is Lifecycle-Bound

所以：

$$
\boxed{
1_{\mathrm{earned}}
=
1_{\mathrm{epoch,domain}}.
}
$$

不是永恆的一。

---

# 66. Dynamic One

今天是 hot primitive，

明天可能 stale。

---

# 67. 「一」可以退化回多

$$
\boxed{
\kappa^{(k)}
\rightarrow
\mathcal R^{(k-1)}.
}
$$

---

# 68. Decrystallization

這是：

$$
\boxed{
\text{one}
\rightarrow
\text{many}
}
$$

的合法反向操作。

---

# 69. 所以 Primitive 不是不可分

只是：

> 在當前 task / scale / epoch 不需要分。

---

# 70. Paper 01 的「一」現在完整了

$$
\boxed{
1
=
\text{declared unit}
+
\text{earned stability}
+
\text{reopen path}.
}
$$

對 strong primitive 而言。

---

# 71. Hidden Thickness

Paper 04：

$$
\Delta(\kappa)
=
(
\Delta_W,
\Delta_C,
\Delta_T,
\Delta_S
).
$$

---

# 72. Crystal 不應丟掉 Hidden Thickness

即使上層：

$$
H=1,
$$

仍保存：

$$
W_{\mathrm{range}},
D_{\mathrm{range}},
T_{\mathrm{range}}.
$$

---

# 73. Resource Envelope

$$
\boxed{
E_\kappa
=
(
W_{\min},
W_{\max},
D_{\max},
T_{p95},
M_{\max},
R_{\max}
).
}
$$

---

# 74. Point with Thickness

所以：

$$
\boxed{
\mathsf{Pt}^{(k)}
+
\Delta^{(k-1)}
}
$$

是較完整的 primitive 表示。

---

# 75. False O(1)

如果只看：

$$
H=1
$$

就宣稱：

$$
O(1),
$$

是典型錯誤。

---

# 76. Online Constant-Time vs Lifecycle Cost

即使：

$$
T_{\mathrm{online}}=O(1),
$$

仍要：

$$
C_{\mathrm{pre}},
C_{\mathrm{update}},
C_{\mathrm{storage}}.
$$

---

# 77. Crystallization Shifts Cost in Time

$$
\boxed{
C_{\mathrm{past}}
\uparrow
\Rightarrow
C_{\mathrm{now}}
\downarrow
}
$$

可能成立。

---

# 78. 這是 Complexity Transfer

不是 Complexity Disappearance。

---

# 79. Topological Compression

若：

$$
H'\ll H,
$$

記：

$$
\boxed{
\Delta_{\mathrm{top}}>0.
}
$$

---

# 80. Causal Compression

若：

$$
D_C'\ll D_C,
$$

記：

$$
\boxed{
\Delta_{\mathrm{causal}}>0.
}
$$

---

# 81. Work Compression

若：

$$
W'\ll W,
$$

記：

$$
\boxed{
\Delta_{\mathrm{work}}>0.
}
$$

---

# 82. Time Compression

若：

$$
T'\ll T,
$$

記：

$$
\boxed{
\Delta_{\mathrm{time}}>0.
}
$$

---

# 83. Materialization Compression

若中間 state 減少：

$$
M'\ll M.
$$

---

# 84. Semantic Compression

如果 task-relevant contract 更小但等價：

$$
C_{\mathrm{sem}}'\ll C_{\mathrm{sem}}.
$$

---

# 85. Verification Compression

若舊 route 每次深度驗證，

新 crystal 只需 cheap guard + periodic deep validation，

可：

$$
C_V'\ll C_V.
$$

---

# 86. Reasoning Compression

AI 不再每次重新 plan：

$$
C_{\mathrm{reason}}'\ll C_{\mathrm{reason}}.
$$

---

# 87. Route Search Compression

$$
C_{\mathrm{route-search}}'\ll C_{\mathrm{route-search}}.
$$

---

# 88. Compression Vector

因此：

$$
\boxed{
\Delta_{\mathrm{crystal}}
=
(
\Delta_{\mathrm{top}},
\Delta_{\mathrm{causal}},
\Delta_{\mathrm{work}},
\Delta_{\mathrm{time}},
\Delta_{\mathrm{material}},
\Delta_{\mathrm{semantic}},
\Delta_{\mathrm{verify}},
\Delta_{\mathrm{reason}}
).
}
$$

---

# 89. Crystal 不必每項都正

例如 parallelization：

$$
\Delta_{\mathrm{causal}}>0,
$$

但：

$$
\Delta_{\mathrm{work}}\le0
$$

可能成立。

---

# 90. Lifecycle Utility 決定是否值得

所以不要求所有成本同時下降。

---

# 91. Pareto Crystal

如果：

$$
\kappa
$$

在多維成本上 Pareto 優於 baseline，

可 promotion。

---

# 92. Scalarized Crystal

若 policy 有權重：

$$
J_\omega.
$$

---

# 93. Crystal Regret

如果 promote 錯了：

$$
\operatorname{Regret}_\kappa
=
J(\kappa)-J(\Gamma).
$$

---

# 94. Negative Crystal

若：

$$
\operatorname{Regret}_\kappa>0
$$

長期成立，

應 retire。

---

# 95. Macro Packaging Failure

最常見假 crystal：

$$
H_{\mathrm{if}}\downarrow
$$

但：

$$
W,D,T,V
$$

都不變。

---

# 96. Cache-Only Crystal

只對 exact repeated input 有效。

可視為 narrow-domain earned primitive。

---

# 97. Generalized Crystal

對：

$$
x\in D_\kappa
$$

一整類輸入成立。

---

# 98. Domain Width

可定義：

$$
\boxed{
\mu(D_\kappa)
}
$$

衡量適用範圍。

---

# 99. Wider Domain ≠ Better

domain 越寬，guard / validation 可能越難。

---

# 100. Narrow Hot Crystal Can Be Valuable

高頻窄域仍很值得。

---

# 101. Semantic Equivalence

要求：

$$
\boxed{
\operatorname{Semantics}(\kappa,x)
\simeq_q
\operatorname{Semantics}(\Gamma,x)
}
$$

對：

$$
x\in D_\kappa.
$$

---

# 102. Task-Relative Equivalence

不必保存無關 internal details。

---

# 103. But History-Sensitive Tasks Need More

如果 audit / causality relevant，

需保留：

$$
V_H,
V_C,
V_T.
$$

---

# 104. Full Promotion Gate

$$
\boxed{
V_{\mathrm{full}}
=
V_S
\land
V_C
\land
V_T
\land
V_G
\land
V_\Sigma
\land
V_A.
}
$$

需要哪些由 task 決定。

---

# 105. Physical Compression Is Strong but Optional

如果：

$$
W',
E',
M'
$$

都顯著下降，

則 crystal 更接近 physical reunitization。

---

# 106. Physical Shortcut

例如新 hardware primitive：

$$
\operatorname{AES\_NI}
$$

相較 software implementation。

---

# 107. Instruction Fusion

CPU micro-op fusion 也是 physical/topological compression 例子。

---

# 108. GPU Tensor Core

macro matrix op 可能對指定 hardware 成為更強 physical primitive。

---

# 109. Precomputed Hardware

ASIC 把大量 general computation 轉成 fixed physical structure。

---

# 110. Complexity Externalization to Matter

這是：

$$
\boxed{
\text{runtime complexity}
\rightarrow
\text{hardware structure}.
}
$$

---

# 111. 但 Build Cost 必須算

ASIC design / fabrication 不是免費。

---

# 112. One in Hardware Can Cost a Factory

所以：

$$
\boxed{
1_{\mathrm{phy,online}}
\neq
1_{\mathrm{life}}.
}
$$

---

# 113. Crystal as Frozen Structure

crystal 本質上把過去 computation 固定成 future structure。

---

# 114. Structure Can Be Software, Memory, or Hardware

例如：

- index；
- code；
- model；
- table；
- hardware；
- protocol；
- route graph。

---

# 115. Crystallization Is Substrate-Agnostic

只要未來 route 不再需要原始完整求解。

---

# 116. Semantic Crystal

保存 reusable semantic transformation。

---

# 117. Navigation Crystal

保存 reusable route。

---

# 118. Configuration Crystal

保存 reusable computational-form switching pattern。

---

# 119. Temporal-Causal Crystal

保存 reusable causal / timing contract。

---

# 120. Physical Crystal

把 computation 固化進 physical structure。

---

# 121. Crystal Family

因此：

$$
\boxed{
\mathfrak K
=
\{
\kappa_S,
\kappa_N,
\kappa_C,
\kappa_T,
\kappa_P,\ldots
\}.
}
$$

---

# 122. 多種 Crystal 可以疊加

一個 configuration crystal 裡可以引用 navigation crystal。

---

# 123. Nested Crystal

$$
\kappa^{(k)}
=
F(
\kappa_1^{(k-1)},
\ldots,
\kappa_n^{(k-1)}
).
$$

---

# 124. Crystal Tower

Paper 05：

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

# 125. New One Can Be Built from Old Ones

所以 primitive generation 是 recursive。

---

# 126. But Tower Inherits Risk

底層 crystal stale 可污染上層。

---

# 127. Dependency-Aware Invalidation

$$
\boxed{
\operatorname{Invalidate}(\kappa_i)
\Rightarrow
\operatorname{Revalidate}(\operatorname{Parents}(\kappa_i)).
}
$$

---

# 128. Crystal DAG

$$
\boxed{
G_K
=
(V_K,E_K).
}
$$

---

# 129. Crystal DAG Is Maintenance Structure

不是 World 本身。

---

# 130. Crystal Provenance

每個 node 必須知道：

- source；
- compiler；
- validator；
- version；
- parent / child；
- active domain。

---

# 131. Crystal Without Provenance Is Dangerous

因為不知道何時 invalid。

---

# 132. Staleness

依賴：

$$
d
$$

改變時：

$$
\kappa
$$

可能 stale。

---

# 133. Staleness Probability

可估：

$$
P_{\mathrm{stale}}(\kappa,t).
$$

---

# 134. Maintenance Cost

$$
C_M(\kappa)
=
C_{\mathrm{monitor}}
+
C_{\mathrm{revalidate}}
+
C_{\mathrm{update}}.
$$

---

# 135. Hot Crystal with Huge Maintenance May Be Bad

因此 frequency alone 不夠。

---

# 136. Utility Again

$$
U(\kappa)
=
B_{\mathrm{reuse}}
-
C_{\mathrm{life}}.
$$

---

# 137. Crystallization Threshold

只有：

$$
U(\kappa)>\theta_U
$$

才值得 promotion。

---

# 138. Crystal Selectivity

不是所有 route 都該結晶。

---

# 139. This Is EHPE's Core Principle

$$
\boxed{
\text{Can compile}
\neq
\text{Should compile}.
}
$$

---

# 140. Paper 07 Adds

$$
\boxed{
\text{Can call as one}
\neq
\text{Has earned one}.
}
$$

---

# 141. Earned One

定義：

$$
\boxed{
1_{\mathrm{earned}}
=
\langle
D,
G,
S,
V,
U,
P,
F,
E_\Delta
\rangle.
}
$$

---

# 142. $D$

valid domain。

---

# 143. $G$

guard。

---

# 144. $S$

stability。

---

# 145. $V$

verification maturity。

---

# 146. $U$

utility。

---

# 147. $P$

provenance。

---

# 148. $F$

fallback / reopen。

---

# 149. $E_\Delta$

hidden thickness / resource envelope。

---

# 150. Earned One Is Not Just a Number

它是一個帶 contract 的 runtime object。

---

# 151. New Primitive Record

```text
EarnedPrimitive
- primitive_id
- scale
- domain
- semantic_contract
- guard
- configuration
- geometry
- temporal_causal_contract
- resource_envelope
- verification
- provenance
- reopen_pointer
- lifecycle_state
```

---

# 152. Primitive Invocation

$$
\boxed{
\operatorname{Invoke}(\kappa,x)
}
$$

先：

$$
G_\kappa(x).
$$

---

# 153. Guard Pass

fast path。

---

# 154. Guard Fail

slow path / reopen。

---

# 155. Validator

每次可 cheap validate。

---

# 156. Periodic Deep Validation

避免 hidden drift。

---

# 157. Shadow Validation

新 version：

$$
\kappa'
$$

先 shadow。

---

# 158. Promotion

只有 equivalence + utility 成立。

---

# 159. Demotion

若 fail rate 上升。

---

# 160. Reopening

$$
\kappa
\rightarrow
\mathcal R_{\mathrm{source}}.
$$

---

# 161. Reopening Can Be Partial

只展開 relevant subpath。

---

# 162. Selective Decrystallization

$$
\boxed{
\operatorname{Reopen}_q(\kappa)
}
$$

只為 task $q$ 展開需要的部分。

---

# 163. Full Decrystallization

audit / formal analysis 才全開。

---

# 164. Decrystallization Cost

$$
C_{\mathrm{reopen}}.
$$

應計入 lifecycle。

---

# 165. Too-Cheap Crystal Can Be Expensive to Reopen

這是 hidden maintenance debt。

---

# 166. Reopenability Score

$$
\boxed{
R_O(\kappa)
}
$$

評估：

- source availability；
- reconstruction fidelity；
- provenance completeness；
- replayability。

---

# 167. Promotion Should Require Minimum Reopenability

除非 domain 明確接受 irreversible abstraction。

---

# 168. Irreversible Crystal

某些 hardware compilation 不可完整反向。

可以存在，但必須宣告 loss。

---

# 169. Loss Declaration

$$
\boxed{
L_{\mathrm{reopen}}.
}
$$

---

# 170. Crystallization Receipt

```text
CrystallizationReceipt
- source_route
- source_scale
- target_primitive
- target_scale
- compression_vector
- semantic_equivalence
- causal_equivalence
- temporal_equivalence
- work_before_after
- depth_before_after
- latency_before_after
- verification
- provenance
- valid_domain
- guard
- reopenability
- lifecycle
```

---

# 171. One as Contracted Compression

因此最準確的定義是：

$$
\boxed{
\text{New One}
=
\text{Contracted, Verified, Reopenable Compression}.
}
$$

---

# 172. Why Contracted?

因為它只在 declared domain / semantics 下成立。

---

# 173. Why Verified?

因為不能靠命名創造 primitive。

---

# 174. Why Reopenable?

因為抽象不能永久遮蔽 failure source。

---

# 175. Why Compression?

因為沒有任何成本／結構壓縮，就只是 rename。

---

# 176. Compression Need Not Be Physical

可以是 reasoning、routing、verification 等成本壓縮。

---

# 177. Computational Reunitization Criterion

本文提出：

$$
\boxed{
\operatorname{RU}(\Gamma)=1
}
$$

若至少：

$$
\Delta_{\mathrm{struct}}>0
$$

且：

$$
V_{\mathrm{relevant}}=1
$$

且：

$$
U_{\mathrm{life}}>0.
$$

---

# 178. Structural Gain

可由：

$$
\Delta_{\mathrm{top}},
\Delta_{\mathrm{causal}},
\Delta_{\mathrm{reason}},
\Delta_{\mathrm{material}}
$$

任一或多個構成。

---

# 179. Pure Interface Gain Is Not Enough

若只有：

$$
\Delta_{\mathrm{if}}>0
$$

則不算 strong RU。

---

# 180. Pure Semantic Gain May Be Useful but Not Computational

例如好的 API design。

可以稱 semantic abstraction，但不必稱 computation speedup。

---

# 181. Terminology Discipline

本文建議：

- macro；
- abstraction；
- compiled path；
- crystal；
- earned primitive；

分開用。

---

# 182. Macro

只是 packaging。

---

# 183. Abstraction

隱藏 detail。

---

# 184. Compiled Path

執行拓撲被改寫。

---

# 185. Crystal

compiled / stabilized reusable route with lifecycle。

---

# 186. Earned Primitive

在 higher scale 被合法當作 unit 的 mature crystal。

---

# 187. Earned Primitive Can Exist Without Speedup

如果主要收益是：

- reliability；
- verification；
- coordination；

仍可能值得。

---

# 188. But Then Don't Claim Speedup

應說：

$$
U>0
$$

而不是：

$$
T\downarrow.
$$

---

# 189. Speedup Claim Must Specify Dimension

如 Paper 04：

- work-speedup；
- depth-speedup；
- latency-speedup；
- observer-hop-speedup；
- lifecycle-speedup。

---

# 190. Crystal Claim Also Must Specify Compression Dimension

例如：

```text
topological crystal
causal crystal
semantic crystal
routing crystal
physical crystal
```

---

# 191. Composite Crystal

多種 compression 同時存在。

---

# 192. Crystal Strength Vector

$$
\boxed{
\mathbf S_\kappa
=
(
s_{\mathrm{top}},
s_{\mathrm{causal}},
s_{\mathrm{semantic}},
s_{\mathrm{physical}},
s_{\mathrm{verify}},
s_{\mathrm{reopen}}
).
}
$$

---

# 193. Strength Is Not One Scalar Necessarily

可用 Pareto profile。

---

# 194. Weak Crystal

主要 semantic / interface benefit。

---

# 195. Strong Crystal

多維 structural + lifecycle benefit。

---

# 196. Physical Crystal

physical work reduction 顯著。

---

# 197. Governing Crystal

主要 governance / authorization / verification reuse。

---

# 198. Crystal Type Is Not Ontology

只是一種工程 profile。

---

# 199. Crystallization and 24／72

lower route：

$$
P5^F
\rightarrow
P11^F
\rightarrow
P17^F
$$

可被 higher-scale：

$$
P23^F
$$

primitive 表示。

---

# 200. This Is Form Ascent

$$
\boxed{
(S/J/P)^{(\mu)}
\rightarrow
R^{(M)}
}
$$

可能成立。

---

# 201. But Macro R Keeps Hidden Internals

所以：

$$
R^{(M)}
$$

不代表 micro R。

---

# 202. Law Ascent

micro stochastic：

$$
K
$$

可在 macro 呈現 approximate deterministic：

$$
\widehat F_\epsilon.
$$

---

# 203. Geometry Ascent

$$
\mathsf{Sf}^{(\mu)}
\rightarrow
\mathsf{Pt}^{(M)}.
$$

---

# 204. Time Ascent

micro history：

$$
\mathcal H^{(\mu)}
$$

變 macro event：

$$
E^{(M)}.
$$

---

# 205. Scale Ascent

這些全部共同形成 earned primitive。

---

# 206. Full Ascent Record

$$
\boxed{
A_\kappa
=
(
p_\mu,
\lambda_\mu,
g_\mu,
\Theta_\mu
)
\rightarrow
(
p_M,
\lambda_M,
g_M,
\Theta_M
).
}
$$

---

# 207. This Is Not Lossless by Default

必須有 bridge / fidelity。

---

# 208. Multi-Scale Crystal

因此 primitive 可以攜帶 source configuration atlas。

---

# 209. Crystal Atlas

$$
\boxed{
\mathcal A_\kappa
}
$$

保存內部不同 scale / config 的來源。

---

# 210. Reopen Uses Atlas

audit 時選需要的 chart 展開。

---

# 211. MWT Interface

MWT 的 World primitive 不被 crystal 取代。

Crystal 只是 runtime presentation / reusable primitive。

---

# 212. GCM Interface

GCM 可把 hot crystal 當 domain-local solver / primitive。

---

# 213. UNPNP Interface

UNPNP 用 hyperlink 尋址 crystal。

---

# 214. Crystal Hyperlink

$$
\boxed{
\ell_\kappa:
x
\rightarrow
\kappa(x).
}
$$

---

# 215. Configuration Hyperlink

Paper 06：

$$
(s,c_i)\rightarrow(s',c_j).
$$

可被 crystal 固化。

---

# 216. World-to-Primitive

Paper 05：

$$
W^{(k-1)}
\rightarrow
\kappa^{(k)}.
$$

Paper 07 給出 promotion criteria。

---

# 217. Primitive-to-World

reopen criteria 也完成。

---

# 218. New One Is a Boundary Object

primitive 是 lower / higher scale 之間的 boundary。

---

# 219. Boundary Contract

其 input/output/guard 定義 higher-scale interface。

---

# 220. Boundary Provenance

其 source / atlas 定義 lower-scale trace。

---

# 221. Boundary Thickness

其 resource envelope 定義 hidden cost。

---

# 222. Boundary Reopenability

其 fallback 定義跨尺度逆向路。

---

# 223. So Primitive Is Not Just Function

更像：

$$
\boxed{
\text{cross-scale contract object}.
}
$$

---

# 224. Primitive Stability

若 boundary 漂移，primitive 失效。

---

# 225. Abstraction Leakage

如果 higher-scale caller 常需知道 lower internals：

$$
L_A\uparrow.
$$

---

# 226. High Leakage Means Poor Primitive

可能需降級。

---

# 227. Primitive Quality

$$
\boxed{
Q_\kappa
=
f(
S,
V,
U,
R_O,
-L_A
).
}
$$

---

# 228. Reopen Frequency

$$
f_{\mathrm{reopen}}
$$

是 primitive quality 指標。

---

# 229. Too Frequent Reopen

表示 abstraction boundary 不穩。

---

# 230. Never Reopen Is Not Automatically Good

可能只是沒監測到 drift。

---

# 231. Periodic Audit

hot crystal 仍需 periodic deep validation。

---

# 232. Verification Budget

$$
B_V
$$

可動態分配。

---

# 233. More Critical Crystal Gets More Validation

依 risk / dependency centrality。

---

# 234. Crystal Centrality

$$
\operatorname{Cent}(\kappa)
$$

越高，失效影響越大。

---

# 235. Systemic Crystal

被很多上層 route 依賴。

---

# 236. Systemic Crystal Needs Stronger Gate

---

# 237. Crystal Failure Propagation

$$
\kappa_i
\rightarrow
\{\kappa_j\}
$$

依賴圖中可能連鎖。

---

# 238. Circuit Breaker

當 fail rate 超過：

$$
\theta_F,
$$

自動 slow path。

---

# 239. Safe Reopen

slow path 不能因 fast path failure 而也失效。

---

# 240. Independent Fallback

理想上 fallback 路徑應降低 correlated failure。

---

# 241. Crystal Diversity

不同 implementation 可提供：

$$
\kappa_A,\kappa_B.
$$

---

# 242. Cross-Validation

用不同 crystal 比較結果。

---

# 243. High-Assurance Domain

可以保留：

- fast crystal；
- slow canonical；
- independent validator。

---

# 244. Crystal Is Not Authority

快路不擴權。

---

# 245. Derived Primitive Does Not Inherit Greater Permission

$$
\boxed{
\text{Faster Primitive}
\not\Rightarrow
\text{Greater Authority}.
}
$$

---

# 246. Source Authority Upper Bound

primitive authority：

$$
\operatorname{Auth}(\kappa)
\subseteq
\operatorname{Auth}(\text{source}).
$$

---

# 247. Authorization Must Re-evaluate

尤其 permission / epoch 變化時。

---

# 248. Governance Crystal

可以結晶「如何驗權」的流程，

但不能繞過授權本身。

---

# 249. Guard Must Remain Live

不能因過去驗證過一次就永久跳過 revocation。

---

# 250. Revocation Is Anti-Crystal Event

使 fast path 暫停。

---

# 251. Lifecycle World

每個 primitive 所在世界會演化：

$$
W_t.
$$

所以：

$$
G_\kappa(W_t)
$$

必須持續有效。

---

# 252. Crystal Fitness

$$
\boxed{
F_\kappa(t)
=
U(\kappa\mid W_t).
}
$$

---

# 253. Fitness Can Decline

所以 retirement 正常。

---

# 254. Crystallization Is Evolution, Not Monument

它是可生、可熟、可退役的 runtime structure。

---

# 255. Crystal Population

一個系統可有：

$$
\mathcal K_t
=
\{\kappa_1,\ldots,\kappa_n\}.
$$

---

# 256. Population Maintenance Cost

$$
C_{\mathcal K}
=
\sum_i C_M(\kappa_i)
+
C_{\mathrm{select}}.
$$

---

# 257. Too Many Crystals Can Hurt

所以：

$$
\boxed{
\text{more crystals}
\neq
\text{better system}.
}
$$

---

# 258. Crystal Garbage Collection

低 utility / stale / duplicate primitive 應 retire。

---

# 259. Duplicate Crystal Detection

若：

$$
\kappa_i
\simeq
\kappa_j,
$$

可 merge 或保留 diversity depending on risk。

---

# 260. Crystal Compression of Crystals

多個 related crystals 可再向上結晶。

---

# 261. Meta-Primitive

$$
\boxed{
\kappa^{(+1)}
=
K(
\kappa_1^{(0)},
\ldots,
\kappa_n^{(0)}
).
}
$$

---

# 262. Meta-Primitive Is New One at Higher Scale

這正是宏遞升。

---

# 263. Infinite Meta-Crystallization Is Bounded Operationally

仍遵守 finite active support。

---

# 264. Active Crystal Frontier

只把 relevant primitives active。

---

# 265. Dormant Crystal

低頻 crystal 可 dormant。

---

# 266. Rehydrate Crystal

需要時重載。

---

# 267. Crystal Cache ≠ Crystal Store

cache 是 active realization；store 是 canonical metadata。

---

# 268. Computational One Can Be Dormant

primitive 存在，不代表 active memory 中展開。

---

# 269. New One and Observer

對 user：

$$
\kappa
$$

是一個 action。

對 runtime：

可是一個 point with thickness。

對 auditor：

可 reopen 成 route。

---

# 270. One Is Observer-Relative but Governed by Same Provenance

---

# 271. Multiple Views of Same Primitive

$$
\Pi_{O_1}(\kappa)
\neq
\Pi_{O_2}(\kappa).
$$

---

# 272. Shared Primitive ≠ Shared View

---

# 273. Primitive Semantics Must Be Stable across Views

relevant invariants 保留。

---

# 274. Crystal Explanation

AI 應能回答：

> 這個一是怎麼來的？

---

# 275. Explanation Path

$$
\kappa
\rightarrow
\operatorname{Receipt}
\rightarrow
\operatorname{SourceRoute}.
$$

---

# 276. Explainable One

這比 opaque macro 強很多。

---

# 277. Primitive Audit

可比較：

- claimed compression；
- measured compression；
- source equivalence；
- hidden costs。

---

# 278. False Crystal Detector

如果：

$$
\Delta_{\mathrm{claimed}}>0
$$

但 empirical：

$$
\Delta_{\mathrm{measured}}\le0,
$$

標 false crystal。

---

# 279. Crystal Inflation

系統過度把普通 function 稱為 crystal。

---

# 280. Terminology Inflation Is Dangerous

會讓 metric 失真。

---

# 281. Canonical Rule

只有：

$$
\operatorname{RU}=1
$$

且 lifecycle gate 過，才叫 computational crystal。

---

# 282. Otherwise Use Ordinary Terms

macro、cache、function、summary、wrapper。

---

# 283. Experiment 1：Macro Packaging

Baseline：

$$
a_1\rightarrow\cdots\rightarrow a_{10}.
$$

Variant：

```text
M()
```

測：

$$
W,D,T.
$$

預期不變。

---

# 284. Experiment 2：Parallelization

同十 task，改成 parallel surface。

預期：

$$
D_C\downarrow,
$$

但：

$$
W\approx.
$$

---

# 285. Experiment 3：Indexing

repeated search：

$$
\mathsf{Ln}
\rightarrow
\mathsf{Jl}.
$$

測 build + lifecycle。

---

# 286. Experiment 4：Memoization

exact repeated input。

測 narrow-domain crystal。

---

# 287. Experiment 5：Path Compilation

同一 input class，建立 new executable form。

---

# 288. Experiment 6：Crystallization

反覆成功後 promotion。

---

# 289. Experiment 7：Distribution Shift

使 guard fail，看是否安全 reopen。

---

# 290. Experiment 8：Hidden Cost

API 一 call 但 physical work 巨大，測 naive metric 是否誤判。

---

# 291. Experiment 9：Invalidation Cascade

底層 crystal stale，測上層 dependency revalidation。

---

# 292. Experiment 10：Crystal Population

增加大量低價值 crystal，測 selection / maintenance overhead。

---

# 293. Success Metrics

```text
topological_reduction
causal_depth_reduction
work_reduction
latency_reduction
reasoning_reduction
verification_reduction
materialization_reduction
guard_cost
reopen_cost
stale_rate
maintenance_cost
false_crystal_rate
```

---

# 294. Primitive Promotion Accuracy

$$
\boxed{
A_P
=
\frac{\text{beneficial promoted crystals}}
{\text{all promoted crystals}}
}
$$

---

# 295. Crystal Recall

有價值 candidate 被成功 promotion 的比例。

---

# 296. Over-Crystallization Rate

低 utility crystal 被 promotion。

---

# 297. Under-Crystallization Rate

高 utility route 沒被 promotion。

---

# 298. Reopen Success Rate

$$
R_{\mathrm{reopen}}.
$$

---

# 299. Provenance Completeness

$$
P_C.
$$

---

# 300. Lifecycle Gain

$$
\boxed{
G_{\mathrm{life}}
=
C_{\mathrm{baseline-life}}
-
C_{\mathrm{crystal-life}}.
}
$$

---

# 301. Paper 07's Strongest Claim

不是：

> 所有複雜 computation 最後都能變成 O(1)。

而是：

$$
\boxed{
\textbf{
部分穩定、可驗證、可重用的低層計算世界，
可以在更高尺度被合法提升為新的 earned primitive。
}
}
$$

---

# 302. This Does Not Solve P/NP

因為 compile / build / verification cost 仍在。

---

# 303. Non-Uniform Shortcut Warning

每 instance 專門造一個 crystal：

$$
\forall x\exists\kappa_x
$$

不能推出：

$$
\exists K\forall x.
$$

---

# 304. Universal Crystal Compiler Is Stronger Claim

本文不宣稱存在。

---

# 305. General Primitive Learner

真正強問題是：

> 能否對一個 problem family 自動發現哪些 route 值得升格？

---

# 306. This Is Experimental

需要 frozen-model benchmark。

---

# 307. Structural Learning

如果模型不變：

$$
\theta_{t+1}
=
\theta_t
$$

但：

$$
\mathcal K_{t+1}
\neq
\mathcal K_t,
$$

且 cost 下降，

支持 runtime structural learning。

---

# 308. Crystal Creation Rate

$$
r_K.
$$

---

# 309. But Quality > Quantity

看：

$$
G_{\mathrm{life}}
$$

而不是只看 $r_K$。

---

# 310. MWT Interface

Crystal 是 presentation / runtime primitive，不是 World ontology。

---

# 311. GCM Interface

不同 domain 可用不同 crystal / non-crystal solver。

---

# 312. 24／72 Interface

crystal 可在 macro scale 呈現不同 computational form。

---

# 313. Time-Causal Interface

macro point 必須保留 hidden causal / temporal thickness。

---

# 314. Scale Interface

primitive 是 cross-scale boundary object。

---

# 315. Route Grammar Interface

crystal invocation 本身是一個 typed route segment。

---

# 316. UNPNP-I Interface

Path Compilation 造新路；Paper 07 解釋何時新路真正成為新的「一」。

---

# 317. 核心定律一

$$
\boxed{
\textbf{
One call is not one computation.
}
}
$$

---

# 318. 核心定律二

$$
\boxed{
\textbf{
Packaging does not create a new primitive; verified reunitization does.
}
}
$$

---

# 319. 核心定律三

$$
\boxed{
\textbf{
A new computational one is domain-bound, lifecycle-bound, and scale-relative.
}
}
$$

---

# 320. 核心定律四

$$
\boxed{
\textbf{
Crystallization compresses future computation without erasing past cost or source provenance.
}
}
$$

---

# 321. 核心定律五

$$
\boxed{
\textbf{
A strong primitive must be both usable as one and reopenable as many.
}
}
$$

---

# 322. 核心定律六

$$
\boxed{
\textbf{
Physical compression is the strongest form of reunitization, but it is not required for computational crystallization.
}
}
$$

---

# 323. 核心定律七

$$
\boxed{
\textbf{
More crystals do not imply a better computational world.
}
}
$$

---

# 324. 對 Paper 01 的最終回答

「一」不是 primitive because declared。

它是 primitive because：

$$
\boxed{
\text{declared}
+
\text{verified}
+
\text{useful}
+
\text{reopenable}.
}
$$

---

# 325. 對 Paper 02 的回答

新的「一」會改變 future route space，因此 shortest route 也會改變。

---

# 326. 對 Paper 03 的回答

結晶可以：

$$
\mathsf{Ln}
\rightarrow
\mathsf{Jl}
\rightarrow
\mathsf{Pt}.
$$

---

# 327. 對 Paper 04 的回答

point 雖是一 hop，仍保存 temporal-causal thickness。

---

# 328. 對 Paper 05 的回答

lower-scale world 可以變 higher-scale primitive，但 reopenability 必須保留。

---

# 329. 對 Paper 06 的回答

heterogeneous configuration route 可以被整體結晶成 macro configuration primitive。

---

# 330. Paper 08 的接口

前七篇現在已具備所有局部元件。

最後一篇要把：

- MWT；
- GCM；
- UNPNP；
- 24／72；
- computational geometry；
- time-causal frame；
- scale；
- crystallization；

正式整成同一個 World-Relative Optimization 框架。

---

# 331. Paper 08 預告

## 從 MWT × GCM × UNPNP 到 World-Relative Optimization
### A Unified Multi-Scale Theory of Computational Worlds, Routes, Configurations, and Earned Primitives

核心形式將是：

$$
\boxed{
(\mathcal A^\*,\Gamma_C^\*,\mathcal R^\*,\mathcal K^\*)
=
\arg\min
J(
\mathbf W,
\mathcal A,
\Gamma_C,
\mathcal R,
\mathcal K
\mid
q,B,R,\mathcal H
).
}
$$

---

# 結論

當十個 operation 被寫成：

```text
FastAction()
```

我們最多只知道：

$$
1_{\mathrm{syn}}
$$

或：

$$
1_{\mathrm{if}}.
$$

只有當底層 route 真正經過：

- dependency rewriting；
- path compilation；
- semantic validation；
- lifecycle evaluation；
- provenance fixation；
- guard binding；
- reopenability preservation；

後，才有資格：

$$
\boxed{
\mathcal R^{(k-1)}
\rightarrow
\kappa^{(k)}.
}
$$

因此真正的新「一」不是名字，不是括號，不是 function call，也不是 API surface。

它是：

$$
\boxed{
\text{New One}
=
\text{Contracted}
+
\text{Verified}
+
\text{Useful}
+
\text{Reopenable}
+
\text{Compressed}.
}
$$

而最精確的一句可以寫成：

$$
\boxed{
\textbf{
結晶不是把十個步驟叫成一個；
結晶是讓十個步驟在更高尺度上，真正獲得成為一個新計算原語的資格。
}
}
$$

這個資格不是永久的。

當 world、dependency、permission、distribution 或 cost 結構改變時：

$$
\boxed{
1
\rightarrow
10
}
$$

也必須能再次成立。

所以 UNPNP-II 的「一」最終不是不可分原子，而是：

> **一個被世界暫時承認、可以高效重用、可以被驗證、也可以在必要時重新打開的計算結晶。**
