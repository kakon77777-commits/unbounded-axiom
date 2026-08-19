# \(X_iX_jT\neq X_jX_iT\)？
## 問算子的非交換性、作用順序與語義曲率

**英文題名：** *Does \(X_iX_jT\neq X_jX_iT\)? Non-Commutativity, Operator Order, and Semantic Curvature in a Question-Operator Calculus*  
**系列：**《T 的最小完備可問：從問算子到高階語義空間》Paper 02  
**版本：** v0.1 候選理論草稿  
**日期：** 2026-08-13  
**作者：** Neo.K、Aletheia（AI 協作）

---

## 摘要

Paper 01 提出候選 T-問算子生成基底：

\[
\mathcal Q_0=\{\mathbf B,\mathbf D,\mathbf G,\mathbf F,\mathbf C,\mathbf O\}
\]

與語義空間提升算子：

\[
X_{\mathcal S}.
\]

高階 T-query 因而可寫成：

\[
q=\mathbf Q(X_{\mathcal S_n}\cdots X_{\mathcal S_1}T;\theta).
\]

本文研究最先出現的代數問題：

\[
\boxed{
X_iX_jT\stackrel{?}{\equiv_Q}X_jX_iT.
}
\]

本文首先區分三種「次序不同」：

1. **Syntactic Order Difference**：operator word 字面不同；
2. **Semantic Order Difference**：經型別檢查、語義解釋與 normal form 後仍不 query-equivalent；
3. **Resolution Order Difference**：問題語義相同，但求解成本、證據可用性或資訊損失依執行順序不同。

因此：

\[
X_iX_j\neq_{\mathrm{string}}X_jX_i
\]

不足以證明真正非交換性。本文將 semantic non-commutativity 定義為：

\[
\boxed{
X_iX_jT\not\equiv_QX_jX_iT.
}
\]

為避免「語義曲率」只是一個幾何隱喻，本文只在**相同 seed、相同兩個 lifts、不同作用路徑，最後產生不同 normalized query semantics** 時，定義離散 Semantic Curvature Defect：

\[
\boxed{
\mathrm{Curv}_{ij}(T)=
\begin{cases}
0,&NF(X_iX_jT)\equiv_QNF(X_jX_iT),\\
1,&\text{otherwise}.
\end{cases}
}
\]

若進一步存在 task-relative query pseudometric \(d_Q\)，才定義量化版本：

\[
\boxed{
\kappa_{ij}(T)
=
d_Q\!\left(
NF(X_iX_jT),
NF(X_jX_iT)
\right).
}
\]

因此本文的 semantic curvature 首先只是**離散路徑依賴的工作術語**，不宣稱已建立 Riemannian manifold、connection 或 curvature tensor。

本文提供第一個明確 witness。於 \(t_0\)，名稱 T 指向 A；到 \(t_1\)，A 改名為 U，而名稱 T 被重新分配給 B。則：

\[
X_{\mathrm{Time}(t_1)}
X_{\mathrm{Name}(T)}(T)
=
A@t_1,
\]

但：

\[
X_{\mathrm{Name}(T)}
X_{\mathrm{Time}(t_1)}(T)
=
B@t_1.
\]

因此：

\[
\boxed{
X_{\mathrm{Time}}
X_{\mathrm{Name}}T
\not\equiv_Q
X_{\mathrm{Name}}
X_{\mathrm{Time}}T.
}
\]

本文將非交換性來源分為 referential mutation、information loss、context mutation、policy mutation、type mutation、branching 與 history accumulation，並建立 Conditional Commutativity、Commutation Domain、Order Orbit、Order Multiplicity、Semantic Holonomy（僅在可逆子域）、Operator Commutation Graph、Commutation Certificate 與 Non-Commutativity Witness。

本文最後得到一個對 Query Compiler 極重要的原則：

\[
\boxed{
\text{Operator order is semantic data unless commutativity has been established.}
}
\]

---

## 關鍵詞

問算子、non-commutativity、operator order、semantic curvature、path dependence、query equivalence、semantic lift、\(X^nT\)、erotetic logic、dynamic epistemic logic

---

# 0. 研究邊界

本文不主張：

1. 所有語義算子都不交換；
2. 任意兩個修飾語順序不同就代表 semantic non-commutativity；
3. semantic curvature 已等同微分幾何曲率；
4. query space 已被證明為流形；
5. 一般 query space 中可直接使用 \(X_iX_j-X_jX_i\)；
6. 所有 semantic lifts 都有 inverse；
7. \(d_Q\) 已有唯一標準定義；
8. 非交換性必然表示問題更難；
9. operator order 永遠改變答案；
10. 本文已完成 sound / complete 的問算子代數。

---

# 1. 從 \(X^nT\) 立刻得到次序問題

只要：

\[
X_i,X_j\in\Sigma_X,
\]

就存在兩條自然 path：

\[
T\xrightarrow{X_j}X_jT\xrightarrow{X_i}X_iX_jT
\]

與：

\[
T\xrightarrow{X_i}X_iT\xrightarrow{X_j}X_jX_iT.
\]

如果兩條 path 總是等價，\(X\)-word 可以大幅被視為 unordered feature set。

如果不等價：

\[
\boxed{
\operatorname{Order}(X_i,X_j)
\subset
\operatorname{Semantics}(q).
}
\]

---

# 2. Query Semantic Backend

令：

\[
\llbracket q\rrbracket_{\mathcal M,\mathcal T}
\]

表示 query \(q\) 在模型 \(\mathcal M\)、任務 \(\mathcal T\) 下的語義。

本文不固定單一 backend。它可以具體實作成：

- answer-space semantics；
- partition semantics；
- inquisitive state；
- resolution requirement；
- typed information request。

因此本文的 operator calculus 是 backend-agnostic。

---

# 3. Query Equivalence

定義：

\[
\boxed{
q_1\equiv_Q^{\mathcal M,\mathcal T}q_2
}
\]

若兩者要求相同 task-relevant resolution。

這是交換性之前的必要基礎。

---

# 4. Typed Semantic Lift

每個：

\[
X_i
\]

都是 typed transformation：

\[
\boxed{
X_i:\mathcal D_i\to\mathcal C_i.
}
\]

只有兩個次序都 well-typed 時，才有資格比較：

\[
X_iX_jT
\]

與：

\[
X_jX_iT.
\]

所以：

\[
\boxed{
\text{Non-composability}\neq\text{Non-commutativity}.
}
\]

---

# 5. Strong Commutativity

對 domain \(D\)，若：

\[
\forall T\in D,\quad
X_iX_jT\equiv_QX_jX_iT,
\]

稱：

\[
\boxed{
Commute_D(X_i,X_j).
}
\]

---

# 6. Local Commutativity

只對指定 T：

\[
\boxed{
Commute_T(X_i,X_j)
\iff
X_iX_jT\equiv_QX_jX_iT.
}
\]

因此「可交換」本身可以是 state-dependent。

---

# 7. Conditional Commutativity

若存在條件：

\[
\Phi
\]

使：

\[
\mathcal M,T\models\Phi
\Rightarrow
X_iX_jT\equiv_QX_jX_iT,
\]

則記作：

\[
\boxed{
X_i\bowtie_\Phi X_j.
}
\]

這比直接宣稱 universal commutativity 更實用。

---

# 8. Semantic Non-Commutativity

若存在 witness：

\[
T^*
\]

使：

\[
\boxed{
X_iX_jT^*
\not\equiv_Q
X_jX_iT^*,
}
\]

即可否證 universal commutativity。

---

# 9. Witness 1：Time × Name

在 \(t_0\)：

\[
Ref(T,t_0)=A.
\]

在 \(t_1\)：

\[
Ref(T,t_1)=B,
\]

而 A 仍持續存在但名稱改成 U：

\[
Ref(U,t_1)=A.
\]

---

# 10. Name-Then-Time

先解析當前名稱 T：

\[
X_{\mathrm{Name}(T)}(T)=A@t_0.
\]

再沿 A 的 temporal lineage 移到 \(t_1\)：

\[
\boxed{
X_{\mathrm{Time}(t_1)}
X_{\mathrm{Name}(T)}T
=
A@t_1.
}
\]

---

# 11. Time-Then-Name

先把 query context 移到 \(t_1\)：

\[
X_{\mathrm{Time}(t_1)}T.
\]

再解析當時的名稱 T：

\[
\boxed{
X_{\mathrm{Name}(T)}
X_{\mathrm{Time}(t_1)}T
=
B@t_1.
}
\]

因此兩條 path 不等價。

---

# 12. 它們到底差在哪？

第一條在問：

> **現在叫 T 的那個東西，到 \(t_1\) 是誰？**

第二條在問：

> **到了 \(t_1\)，那時叫 T 的東西是誰？**

表面都包含「T」「時間」「名稱」，但 scope 不同。

因此：

\[
\boxed{
\text{Same semantic ingredients}
\not\Rightarrow
\text{Same composed query}.
}
\]

---

# 13. 第一類來源：Referential Mutation

如果：

\[
X_i
\]

會改變：

\[
Ref,
\]

而：

\[
X_j
\]

依賴 referent，

則交換順序可能改變 query target。

---

# 14. Witness 2：Observer × Name

假設 private alias：

\[
secretAlias\mapsto A.
\]

LimitedObserver 無法看到此 mapping。

若先解析名稱：

\[
secretAlias\to A,
\]

再切換 observer，仍可保留已解析 identity。

若先切換 limited observer，再解析名稱：

\[
secretAlias\to Unresolved.
\]

因此：

\[
\boxed{
X_{\mathrm{Observer}}
X_{\mathrm{Name}}T
\not\equiv_Q
X_{\mathrm{Name}}
X_{\mathrm{Observer}}T.
}
\]

---

# 15. 第二類來源：Information Loss

若：

\[
X_i
\]

先刪除或遮蔽 \(X_j\) 需要的 distinction：

\[
\boxed{
\text{loss before resolution}
\neq
\text{resolution before loss}.
}
\]

---

# 16. Lossy Operator

若存在：

\[
z_1\neq z_2
\]

但：

\[
X_i(z_1)=X_i(z_2),
\]

則 \(X_i\) 對該 state dimension 是 many-to-one。

這類 operator 特別容易造成 order sensitivity。

---

# 17. 第三類來源：Context Mutation

如果：

\[
X_i:c\mapsto c',
\]

而 \(X_j\) 的 semantics 依賴 context：

\[
\llbracket X_j\rrbracket_c
\neq
\llbracket X_j\rrbracket_{c'},
\]

則可能不交換。

典型：

- time；
- namespace；
- language；
- institution；
- jurisdiction。

---

# 18. 第四類來源：Policy Mutation

若：

\[
X_i:\Pi_1\mapsto\Pi_2,
\]

而 \(X_j\) 是 classification / identity judgment，

則：

\[
Judge_{\Pi_2}(T)
\]

不必等於先用 \(\Pi_1\) 判斷再 transport 結果。

---

# 19. 第五類來源：Type Mutation

有些 operator 會把：

\[
Object\to NamedObject
\]

或：

\[
Query\to MetaQuery.
\]

若：

\[
X_iX_jT
\]

well-typed，

但：

\[
X_jX_iT
\]

type error，

本文稱：

\[
\boxed{
\text{Type-Asymmetric Non-Composability}.
}
\]

它比 ordinary non-commutativity 更根本。

---

# 20. 第六類來源：Branching

若：

\[
X_i:T\to\{T_1,T_2\},
\]

而 \(X_j\) 要求 single bearer，

則「先 fork 再問」與「先問再 fork」會產生不同 answer structure。

---

# 21. 第七類來源：History Accumulation

兩條 path 可能 current state 相同：

\[
State(X_iX_jT)=State(X_jX_iT),
\]

但 provenance：

\[
P_{ij}\neq P_{ji}.
\]

如果 task 關心 history：

\[
\boxed{
\text{state-commutative}
\not\Rightarrow
\text{identity-commutative}.
}
\]

---

# 22. Task-Relative Commutativity

對 task \(\mathcal T_1\)，兩條 path 可能等價。

對 task \(\mathcal T_2\)，若後者關心 provenance，就可能不等價。

因此：

\[
\boxed{
Commute_{\mathcal T_1}
\not\Rightarrow
Commute_{\mathcal T_2}.
}
\]

---

# 23. Answer-Space Defect

若：

\[
Ans(q)
\]

是 admissible complete-answer space，可定義：

\[
\boxed{
\Delta^{Ans}_{ij}(T)
=
Ans(X_iX_jT)
\triangle
Ans(X_jX_iT).
}
\]

只要：

\[
\Delta^{Ans}_{ij}(T)\neq\varnothing,
\]

就得到一個直接 semantic witness。

---

# 24. Resolution-Requirement Defect

若 query backend 不方便用 answer set，可比較：

\[
Req(q).
\]

定義：

\[
\boxed{
\Delta^{Req}_{ij}(T)
=
Req(X_iX_jT)
\triangle
Req(X_jX_iT).
}
\]

---

# 25. Semantic Commutation Square

考慮離散方塊：

\[
\begin{array}{ccc}
T & \xrightarrow{X_i} & X_iT\\
\downarrow X_j && \downarrow X_j\\
X_jT & \xrightarrow{X_i} & X_iX_jT
\end{array}
\]

另一條 path 的右下角是：

\[
X_jX_iT.
\]

若兩者 query-equivalent，方塊交換。

---

# 26. Flat Semantic Square

\[
\boxed{
Flat_{ij}(T)
\iff
X_iX_jT\equiv_QX_jX_iT.
}
\]

---

# 27. Curved Semantic Square

\[
\boxed{
Curved_{ij}(T)
\iff
X_iX_jT\not\equiv_QX_jX_iT.
}
\]

這裡 curved 只表示 discrete path dependence。

---

# 28. Semantic Curvature Indicator

\[
\boxed{
\mathrm{Curv}_{ij}(T)
=
\begin{cases}
0,&Flat_{ij}(T),\\
1,&Curved_{ij}(T).
\end{cases}
}
\]

---

# 29. Quantitative Curvature

若有 task-relative query pseudometric：

\[
d_Q,
\]

才定義：

\[
\boxed{
\kappa_{ij}(T)
=
d_Q(
NF(X_iX_jT),
NF(X_jX_iT)
).
}
\]

不同 task 可以有不同 \(d_Q\)。

---

# 30. 為什麼叫「曲率」？

本文只借用一個非常有限的幾何直觀：

> 相同兩個局部方向，沿不同順序移動後，無法回到同一 semantic endpoint。

因此真正主張只有：

\[
\boxed{
\text{curvature-like path defect}.
}
\]

不是物理或微分幾何定理。

---

# 31. 曲率的形式前置條件

必須依序有：

\[
\boxed{
Typing
\to
QuerySemantics
\to
Equivalence
\to
Normalization
\to
Commutativity
\to
Curvature.
}
\]

任何前一層未定義，就不能跳著談曲率。

---

# 32. Operator Path

對 operator word：

\[
w=X_{i_n}\cdots X_{i_1},
\]

定義：

\[
\boxed{
Path(w,T).
}
\]

---

# 33. Path Equivalence

\[
\boxed{
w_1\sim_Tw_2
\iff
w_1T\equiv_Qw_2T.
}
\]

---

# 34. Order Orbit

對同一 operator multiset：

\[
\mathcal X=\{X_1,\ldots,X_n\},
\]

定義：

\[
\boxed{
\mathcal O_{\mathcal X}(T)
=
\left\{
[
X_{\pi(n)}\cdots X_{\pi(1)}T
]_{\equiv_Q}
:\pi\in S_n
\right\}.
}
\]

---

# 35. Order Multiplicity

\[
\boxed{
M_{\mathrm{ord}}(\mathcal X,T)
=
|\mathcal O_{\mathcal X}(T)|.
}
\]

若：

\[
M_{\mathrm{ord}}=1,
\]

所有 permutations 對該 T 等價。

若：

\[
M_{\mathrm{ord}}>1,
\]

存在 order-sensitive semantic classes。

---

# 36. Pairwise Flat 不一定 Global Flat

若 operator semantics 本身 state-dependent，pairwise test 只在原 seed 上成立，不必在經其他 lift 後仍成立。

因此未經 theorem 不能推出：

\[
\boxed{
\text{pairwise flatness}
\Rightarrow
\text{global permutation flatness}.
}
\]

---

# 37. Higher-Order Order Effect

三個 operator：

\[
X_i,X_j,X_k
\]

可能 pairwise 看似交換，但六種 permutation 中仍形成多個 query classes。

因此未來要研究：

\[
M_{\mathrm{ord}}^{(3)}.
\]

---

# 38. Order Spectrum

對深度 \(n\)：

\[
\boxed{
C_n(T)
=
|\mathcal O_{\mathcal X_n}(T)|.
}
\]

本文稱為：

# Order Spectrum

沒有機率分布時不叫 entropy。

---

# 39. Order Entropy 的限制

只有在對 permutation：

\[
\pi
\]

指定機率：

\[
p(\pi),
\]

才有資格定義 Shannon-style：

\[
H_{\mathrm{order}}.
\]

這沿用前一系列對 entropy 用語的嚴格限制。

---

# 40. Conditional Idempotence

是否：

\[
X_i^2T\equiv_QX_iT
\]

也不能先驗成立。

若第二次 lift 不增加新結構，可 idempotent。

若第二次代表「對 \(X_i\)-structure 本身再施加 \(X_i\)」，可能不等價。

---

# 41. Absorption Candidate

若：

\[
S_i\preceq S_j
\]

且 \(S_j\) 完整包含 \(S_i\) 的 task-relevant structure，

可能：

\[
X_jX_iT\equiv_QX_jT.
\]

但必須另證 order information 沒有被刪掉。

---

# 42. Reversible Subdomain

多數 lifts 可能不可逆。

只在：

\[
\Sigma_X^{rev}
\subseteq\Sigma_X
\]

中指定 inverse 後，才研究 closed loops。

---

# 43. Semantic Holonomy

若：

\[
X_i^{-1},X_j^{-1}
\]

存在，定義：

\[
\boxed{
H_{ij}(T)
=
X_i^{-1}X_j^{-1}X_iX_jT.
}
\]

若：

\[
H_{ij}(T)\not\equiv_QT,
\]

表示閉合 operator loop 留下 semantic residue。

本文稱此為：

# Semantic Holonomy

僅限可逆子域。

---

# 44. Curvature 與 Holonomy 的關係

Curvature defect 不需要 inverse。

Holonomy 需要可逆 loop。

所以：

\[
\boxed{
\text{Curvature Defect}
}
\]

比：

\[
\boxed{
\text{Holonomy Test}
}
\]

適用範圍更廣。

---

# 45. Future Semantic Connection

若未來要比較「同一 operator」如何在不同 semantic frames 中 transport，需要類似：

\[
\nabla_{i\to j}
\]

的 transport rule。

本篇只把：

\[
\boxed{
\text{Semantic Connection}
}
\]

列為 future work，不宣稱已建立。

---

# 46. Flat Domain / Curved Domain

\[
\boxed{
D_{\mathrm{flat}}(X_i,X_j)
=
\{T:X_iX_jT\equiv_QX_jX_iT\}.
}
\]

\[
\boxed{
D_{\mathrm{curv}}(X_i,X_j)
=
\{T:X_iX_jT\not\equiv_QX_jX_iT\}.
}
\]

---

# 47. Operator Commutation Graph

建立：

\[
\boxed{
G_C=(V_X,E_C).
}
\]

node 是 semantic lifts。

edge 表示在指定 domain / task 下已建立 commutativity。

---

# 48. Weighted Commutation Graph

若 benchmark distribution \(P(T)\) 已明確定義，可用：

\[
\boxed{
w_{ij}
=
P[
X_iX_jT\equiv_QX_jX_iT
].
}
\]

但高 empirical commute rate 不能證明 universal commutativity。

---

# 49. Compiler Canonicalization

Query Compiler 只能在已有 commutation proof 的 pair 上重排：

\[
X_iX_jT
\to
X_jX_iT.
\]

否則必須：

\[
\boxed{
\text{Preserve AST order}.
}
\]

---

# 50. Operator-Sort Semantic Bug

如果 compiler 為了 canonical order，直接把所有 \(X\) 按名稱排序：

\[
X_{\mathrm{Time}}X_{\mathrm{Name}}T
\to
X_{\mathrm{Name}}X_{\mathrm{Time}}T,
\]

在 Time × Name witness 中就會改變 referent。

本文稱：

\[
\boxed{
\text{Operator-Sort Semantic Bug}.
}
\]

---

# 51. Scope Barrier

若某 operator 建立 scope，使另一 operator 放在 scope 內／外產生不同語義，定義：

\[
\boxed{
ScopeBarrier(X_i,X_j).
}
\]

這是自然語言到 AST 編譯的重要資訊。

---

# 52. Query AST

例如：

```text
Query(
  generator = B,
  target =
    Lift(Time,
      Lift(Name, T)
    )
)
```

不同於：

```text
Query(
  generator = B,
  target =
    Lift(Name,
      Lift(Time, T)
    )
)
```

所以 \(X^nT\) 不是 bag-of-tags。

---

# 53. Operator Versioning

若：

\[
X_i^{v1}
\]

與：

\[
X_i^{v2}
\]

semantics 不同，

commutativity 也可能不同。

因此任何 commutation rule 都必須攜帶 operator version。

---

# 54. Commutation Certificate

本文提出：

\[
\boxed{
CC_{ij}
=
(
X_i^{v_i},
X_j^{v_j},
Domain,
Task,
Conditions,
Evidence,
Status
).
}
\]

Status：

\[
\{
UniversalWithinDomain,
Conditional,
CounterexampleFound,
Unknown
\}.
\]

---

# 55. Non-Commutativity Witness

定義：

\[
\boxed{
NCW_{ij}
=
(
T^*,
q_{ij},
q_{ji},
Ans_{ij},
Ans_{ji},
Model,
Task
).
}
\]

一個 witness 即可反駁 universal commutativity。

---

# 56. Query Curvature Map

對 operator family：

\[
\Sigma_X
\]

可建立：

\[
\boxed{
K_D=[Curv_{ij}]
}
\]

或有 metric 時：

\[
\boxed{
K_D=[\kappa_{ij}].
}
\]

這只是 pairwise path-defect map，不是 physical curvature tensor。

---

# 57. Time × Name 的 Flat Condition

若：

\[
Ref(T,t_0)=Ref(T,t_1)
\]

且 temporal transport 無歧義，

則兩個 operator 可以在該 T 上交換。

所以：

\[
\boxed{
\text{non-commutativity is often state-dependent}.
}
\]

---

# 58. Observer × Name 的 Flat Condition

若不同 observers 擁有完全相同 name-resolution evidence，而且沒有 visibility filtering，Observer × Name 可能 commute。

---

# 59. Fork × Recovery

先 fork：

\[
T\to(T_1,T_2)
\]

再 recovery，可能產生 rival recovery candidates。

先 recovery 再 fork，recovery 可能只有 single pre-fork target。

因此：

\[
\boxed{
X_{\mathrm{Recovery}}X_{\mathrm{Fork}}T
}
\]

與：

\[
\boxed{
X_{\mathrm{Fork}}X_{\mathrm{Recovery}}T
}
\]

是高非交換性候選。

---

# 60. Scale × Boundary

先定 scale 再問 boundary：

> 在 molecular scale，T 的邊界在哪？

先固定 boundary 再 scale：

> 已固定的 T-boundary 在 molecular scale 如何呈現？

scope 可能不同。

---

# 61. Cause × Counterfactual

\[
X_{\mathrm{Counterfactual}}
X_{\mathrm{Cause}}T
\]

問：

> 固定 causal model 後，拿掉一個 cause 會怎樣？

而：

\[
X_{\mathrm{Cause}}
X_{\mathrm{Counterfactual}}T
\]

問：

> 在反事實世界中，T 的 cause 是什麼？

順序可直接改變 evaluation frame。

---

# 62. Model × Memory

AI identity 中：

\[
X_{\mathrm{Memory}}
X_{\mathrm{Model}}T
\]

可解讀為：

> 換模型後，檢查 memory continuity。

反方向：

\[
X_{\mathrm{Model}}
X_{\mathrm{Memory}}T
\]

則可能是：

> 固定 memory identity 後，再問哪個 model substrate 支持它。

二者可能不同。

---

# 63. 曲率直觀：Operator Path Leaves Memory

若 \(X_i\) 的效果會依賴：

> 之前是否經過 \(X_j\)，

則 path 留下 semantic memory。

本文把這視為 semantic-curvature 最直觀的最低解釋：

\[
\boxed{
\text{semantic path dependence}
=
\text{history-sensitive composition}.
}
\]

---

# 64. Flatness 直觀：Path Forgetfulness

若所有 relevant paths 都收斂到同一 query-equivalence class，可稱該 domain 對該 operator family具有：

\[
\boxed{
\text{path forgetfulness}.
}
\]

---

# 65. 與 Inferential Erotetic Logic 的接口

既有 Inferential Erotetic Logic 已正式處理 question evocation、question generation 與 erotetic implication，即問題如何在條件下導出另一個問題。

本文的新增焦點不是「能不能從問題推出新問題」，而是：

\[
\boxed{
\text{兩個都能生成問題的 semantic lifts，作用順序是否改變生成結果？}
}
\]

---

# 66. 與 Dynamic Epistemic Logic 的接口

Dynamic Epistemic Logic 的重要形式思想之一，是把 epistemic actions 作為 object-language operators / modalities，並讓資訊事件改變後續 action 所作用的 model state。

本文的 \(X\)-lifts 不等同 DEL actions，但共享一個重要結構：

\[
\boxed{
\text{earlier semantic operations can change the state on which later operations are interpreted}.
}
\]

---

# 67. 與 Inquisitive Logic 的接口

Inquisitive frameworks 讓 questions / issues 本身進入正式語義與邏輯。

未來：

\[
\equiv_Q
\]

可以選用 inquisitive-state equivalence 作具體 backend。

本篇維持 backend-neutral。

---

# 68. 第一批 Benchmark Pair

\[
\boxed{
\begin{aligned}
&Time\times Name\\
&Observer\times Name\\
&Namespace\times Translation\\
&Policy\times Classification\\
&Scale\times Boundary\\
&Fork\times Recovery\\
&Model\times Memory\\
&Institution\times Naming\\
&Cause\times Counterfactual\\
&Part\times Replacement
\end{aligned}
}
\]

---

# 69. Counterexample-First 原則

對每個候選交換律：

\[
X_iX_j\stackrel{?}{\equiv}X_jX_i,
\]

先搜尋 witness。

因為：

\[
\boxed{
\exists T^*:X_iX_jT^*\not\equiv_QX_jX_iT^*
}
\]

即可終止 universal claim。

---

# 70. Mutation Testing

未來 Query Compiler 應故意建立 mutant：

> 把 operator word 自動排序。

如果 Time × Name benchmark 沒抓到錯誤，代表 validator 對 order semantics 不敏感。

---

# 71. 本篇附帶最小驗證模型

本 ZIP 包含 Python toy validator：

1. Time × Name：預期 non-commuting；
2. Observer × Name：預期 non-commuting；
3. Stable Time × Name：預期 commuting control。

目標不是證明整個理論，而是建立：

\[
\boxed{
\text{known-curved FAIL-to-commute}
+
\text{known-flat PASS-to-commute}.
}
\]

---

# 72. 目前最安全的代數名稱

本文尚未得到 group、ring、Lie algebra。

因此現階段最安全的稱呼是：

\[
\boxed{
\text{typed non-commutative query term calculus with partial rewrite laws}.
}
\]

---

# 73. 「幾何」的成熟階梯

### Level 0

\[
Curv_{ij}\in\{0,1\}.
\]

### Level 1

\[
\kappa_{ij}=d_Q(q_{ij},q_{ji}).
\]

### Level 2

operator path / loop defects。

### Level 3

transport / connection-like rules。

### Level 4

真正可比較的 discrete semantic geometry。

Paper 02 只正式站在 Level 0，並預留 Level 1。

---

# 74. 核心命題一

\[
\boxed{
\text{String-order difference}
\not\Rightarrow
\text{semantic non-commutativity}.
}
\]

---

# 75. 核心命題二

\[
\boxed{
X_iX_jT^*\not\equiv_QX_jX_iT^*
}
\]

是一個 universal commutativity claim 的反例。

---

# 76. 核心命題三

\[
\boxed{
Commute_D(X_i,X_j)
}
\]

是 domain / task / operator-version relative 的。

---

# 77. 核心命題四

語義曲率最低只等於：

\[
\boxed{
\text{normalized semantic path dependence}.
}
\]

---

# 78. 核心命題五

Lossy operator 若先刪除後續 operator 所需 distinction，是自然非交換性來源。

---

# 79. 核心命題六

Query canonicalization 必須遵守：

\[
\boxed{
Type
\to
Scope
\to
Equivalence
\to
CommutationProof
\to
Rewrite.
}
\]

不能先排序、後補語義。

---

# 80. 核心命題七

pairwise flatness 在沒有額外 theorem 時，不足以證明 higher-order global flatness。

---

# 81. Paper 01 的修正

Paper 01 將：

\[
X^nT
\]

描述成高階語義空間。

Paper 02 現在補充：

\[
\boxed{
X^nT
}
\]

不是只由「有哪些 \(X\)」決定。

它還由：

\[
\boxed{
\operatorname{Order}(X_n,\ldots,X_1)
}
\]

決定。

---

# 82. 最終公式

所以完整 query term 從：

\[
q=\mathbf Q(\{X_1,\ldots,X_n\},T)
\]

修正為：

\[
\boxed{
q
=
\mathbf Q(
X_{i_n}\circ\cdots\circ X_{i_1}(T);
\theta
).
}
\]

operator word 是 ordered。

---

# 83. 結論

一開始我們只問：

\[
X_iX_jT
\stackrel{?}{=}
X_jX_iT.
\]

現在可以精確回答：

1. 兩個字串不同，不夠；
2. 兩個 order 都必須 well-typed；
3. 必須先定義 query semantics；
4. 必須先定義 \(\equiv_Q\)；
5. 必須 normalization；
6. 若仍：

\[
X_iX_jT
\not\equiv_Q
X_jX_iT,
\]

才是 semantic non-commutativity。

而當這種差異被理解為同一 semantic square 上的 path dependence 時，本文才稱：

\[
\boxed{
\mathrm{Curv}_{ij}(T)=1.
}
\]

因此「語義曲率」最終不是：

> 問題空間很彎。

而是一個極具體的句子：

\[
\boxed{
\text{你先進入哪一個語義空間，
會改變你之後究竟在問哪一個問題。}
}
\]

Time × Name 已給出最小 witness：

\[
\boxed{
\text{先解析 T 是誰，再前往未來}
\neq
\text{先前往未來，再解析那時的 T 是誰}.
}
\]

所以：

\[
\boxed{
X^nT
}
\]

真正更接近：

\[
\boxed{
\text{an ordered path through semantic space}.
}
\]

下一篇：

# Paper 03：問句的 Normal Form
## T Query Compiler、重寫系統、型別規則與可問等價

因為只要 operator order 真的會改變語義，我們接下來就必須回答：

> **哪些 rewrite 可以做？哪些次序不能動？兩句表面不同的自然語言問題，何時才真的算同一個問題？**
