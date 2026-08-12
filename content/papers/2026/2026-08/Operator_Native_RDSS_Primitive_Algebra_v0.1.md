# Operator-Native RDSS 原語代數與型別系統
## Primitive Algebra and Type System for Operator-Native RDSS

**文件性質：** 預論文形式規格 / Formal Working Draft  
**版本：** v0.1  
**日期：** 2026-08-10  
**作者：Neo.K**  
**機構：EveMissLab／一言諾科技有限公司**  
**前置：** RDSS 01–09、RDSS Operatorization Translation Matrix v0.1、分域算子本體論、形式化壓縮與算子演化

---

# 0. 研究目標

上一階段已將 RDSS 01–09 的主要公式由「狀態、關係、類型、容器、歷史、Meta-State」翻譯為算子或算子束。

本文件進一步回答：

1. 這些算子如何合法組合？
2. 部分作用如何表示？
3. 跨域如何橋接？
4. 何時具有條件性結合律？
5. 投影、歷史與元算子何時相容？
6. ECV 是否能成為 normal form？
7. 12 個原語算子族是否足以生成 RDSS 的主要結構？

本文件不宣稱已建立完整範疇、operad 或代數結構；只有在對應公理成立後，才允許採用那些成熟數學結構作為後端。

---

# 1. 唯一非算子外殼

保留最大合法域：

$$
\boxed{
\mathfrak D_{\mathrm{RDSS}}.
}
$$

域內所有可判定實體皆具算子資格：

$$
\forall x\in\mathfrak D_{\mathrm{RDSS}},
\qquad
\operatorname{Op}(x).
$$

但：

$$
\boxed{
\operatorname{Op}(x)
\land
\operatorname{Op}(y)
\not\Rightarrow
x(y)\downarrow.
}
$$

因此：

$$
\boxed{
Operatorhood
\neq
Applicability
\neq
Executability
\neq
Realization.
}
$$

---

# 2. 算子記錄

一個 RDSS 算子：

$$
\boxed{
\mathcal O
=
\left\langle
\begin{array}{l}
Id,
Version,
Stratum,
Type,
DomSig,
CodSig,
Context,
Adm,
Act,
Effect,
\\
Expand,
Connect,
Converge,
Invariant,
History,
Sem,
Evidence,
WeightRef,
Cert,
\\
Authority,
LocalTime,
RuntimeRef,
MetaDepth
\end{array}
\right\rangle.
}
$$

其中 `DomSig` / `CodSig` 不必被理解為外部靜態集合，而可由型別簽名算子產生。

定義輸入簽名算子：

$$
\mathcal O_{\sigma^-}(\mathcal O)
=
\sigma^-_{\mathcal O},
$$

輸出簽名算子：

$$
\mathcal O_{\sigma^+}(\mathcal O)
=
\sigma^+_{\mathcal O}.
$$

因此所有內部型別資料仍由算子取得。

---

# 3. 部分作用與限制算子

Operator-Native RDSS 不採全函數語義，而採部分作用：

$$
\mathcal O:
A\rightharpoonup B.
$$

為每個 $\mathcal O$ 定義一個**限制／可作用域算子**：

$$
\boxed{
\overline{\mathcal O}
:
A\rightharpoonup A.
}
$$

其語義是：只保留 $\mathcal O$ 當前可合法作用的輸入。

候選公理：

$$
\boxed{
\overline{\mathcal O}
\diamond
\overline{\mathcal O}
\simeq
\overline{\mathcal O}.
}
$$

即 restriction-like idempotence。

並要求：

$$
\boxed{
\mathcal O
\diamond
\overline{\mathcal O}
\simeq
\mathcal O.
}
$$

這表示 $\overline{\mathcal O}$ 是 $\mathcal O$ 的合法定義域投影，而不是另一個任意前處理。

此處與 restriction-category 理論相鄰，但在完整公理被驗證前，只稱 **restriction-like operator algebra**。

---

# 4. Undefined / Failure 不是零值

若：

$$
x
\notin
\operatorname{Dom}(\mathcal O),
$$

則：

$$
\mathcal O(x)
=
\mathsf{Undefined}.
$$

Operator-Native 版本定義失敗算子：

$$
\boxed{
\mathcal O_{\bot}^{\alpha}
}
$$

其中 $\alpha$ 記錄失敗類型，例如：

$$
\alpha
\in
\{
TypeMismatch,
DomainMismatch,
BridgeMissing,
InvariantFailure,
AuthorityFailure,
MigrationUndefined,
Stale,
Missing
\}.
$$

所以：

$$
\boxed{
Undefined
\neq
0
\neq
False.
}
$$

---

# 5. 十二個原語算子族

暫定：

$$
\boxed{
\mathfrak P_{\mathrm{RDSS}}
=
\{
\mathsf{Realize},
\mathsf{Transform},
\mathsf{Relate},
\mathsf{Type},
\mathsf{Select},
\mathsf{Gate},
\mathsf{Bridge},
\mathsf{Project},
\mathsf{Remember},
\mathsf{Order},
\mathsf{Certify},
\mathsf{Meta}
\}.
}
$$

---

# 6. Realize

狀態不是第一級靜態物，而由零元算子實現：

$$
\boxed{
\mathcal O_{\mathrm{Realize}}^\sigma
:
\mathbf 1
\rightharpoonup
\sigma.
}
$$

當前 state：

$$
x_t
=
\mathcal O_{\mathrm{Realize},t}().
$$

因此：

$$
\boxed{
State_t
=
\operatorname{Realization}
(
\mathcal O_{\mathrm{Realize},t}
).
}
$$

---

# 7. Transform

$$
\boxed{
\mathcal O_{\mathrm{Transform}}
:
\sigma_A
\rightharpoonup
\sigma_B.
}
$$

它承擔：

- state transition；
- rule application；
- migration；
- skip-time；
- local update。

普通 object-transition 即 Transform 的特例。

---

# 8. Relate

$$
\boxed{
\mathcal O_{\mathrm{Relate}}^\rho
:
(
\mathcal O_A,
\mathcal O_B
)
\rightharpoonup
\mathcal O_{A\rho B}.
}
$$

 $\rho$ 可以是：

- dependency；
- causality；
- trust；
- containment；
- reference；
- event routing；
- temporal relation。

Relate 的輸出本身仍為算子。

---

# 9. Type

$$
\boxed{
\mathcal O_{\mathrm{Type}}
:
(
\mathcal O_x,
\Gamma
)
\rightharpoonup
\mathcal O_{\mathrm{TypeProfile}}.
}
$$

其工作是：

- typing；
- classification；
- role attribution；
- type refinement；
- type compatibility。

`Type` 不等於永久 label。

---

# 10. Select

$$
\boxed{
\mathcal O_{\mathrm{Select}}
:
(
\mathfrak O,
Q,
B,
\Gamma
)
\rightharpoonup
\mathfrak O_{\mathrm{eff}}.
}
$$

承擔：

- finite effective support；
- attention；
- active operator selection；
- backend choice；
- scheduler selection。

要求：

$$
|\mathfrak O_{\mathrm{eff}}|<\infty.
$$

---

# 11. Gate

$$
\boxed{
\mathcal O_{\mathrm{Gate}}
:
(
\mathcal O,
\Gamma
)
\rightharpoonup
\{
Pass,
Reject,
BridgeRequired,
Undefined
\}.
}
$$

Gate 表示：

- boundary；
- permission；
- precondition；
- authority；
- safety gate。

它不產生主要業務結果，而決定是否允許後續作用。

---

# 12. Bridge

$$
\boxed{
\mathcal O_{\mathrm{Bridge}}^{B\rightsquigarrow C}
:
B
\rightharpoonup
C.
}
$$

若：

$$
\mathsf{Cod}(\mathcal O_1)=B,
$$

$$
\mathsf{Dom}(\mathcal O_2)=C,
$$

且：

$$
B\not\sim C,
$$

則只有存在合法 Bridge 時：

$$
\boxed{
\mathcal O_2
\diamond
\mathcal O_{\mathrm{Bridge}}
\diamond
\mathcal O_1
}
$$

才可能定義。

Bridge 必須記錄：

- loss；
- reversibility；
- semantic realization；
- evidence；
- certificate。

---

# 13. Project

$$
\boxed{
\mathcal O_{\mathrm{Project}}^{Q,\varepsilon}
:
\mathcal O_A
\rightharpoonup
\mathcal O_{A_Q}.
}
$$

Project 承擔：

- observation；
- coarse-graining；
- parent projection；
- semantic view；
- task-relative state reduction。

必須附：

$$
Loss(\mathcal O_{\mathrm{Project}})
\le
\varepsilon
$$

或明確聲明超界。

---

# 14. Remember

$$
\boxed{
\mathcal O_{\mathrm{Remember}}
:
\mathcal O_{\mathrm{Trajectory}}
\rightharpoonup
\mathcal O_{\mathrm{Memory}}.
}
$$

增量形式：

$$
\boxed{
\mathcal O_{M,t+1}
=
\mathcal O_{\mathrm{MemUpdate}}
\diamond
\mathcal O_{E,t+1}
\diamond
\mathcal O_{S,t+1}
\diamond
\mathcal O_{M,t}.
}
$$

Remember 不等於完整 archival history。

---

# 15. Order

$$
\boxed{
\mathcal O_{\mathrm{Order}}
:
(
e_a,e_b
)
\rightharpoonup
\{
e_a\prec e_b,
e_b\prec e_a,
e_a\parallel e_b
\}.
}
$$

Order 承擔：

- logical clock；
- causal ordering；
- local-time ordering；
- cross-container temporal alignment。

---

# 16. Certify

$$
\boxed{
\mathcal O_{\mathrm{Certify}}
:
(
\mathcal O,
\Gamma,
Evidence
)
\rightharpoonup
\mathcal O_{\mathrm{Cert}}
\cup
\{
Reject,
Inconclusive
\}.
}
$$

Certificate 自身視為零元 witness operator：

$$
\boxed{
\mathcal O_{\mathrm{Cert}}:
\mathbf 1
\rightharpoonup
\mathsf{Proof/WitnessRecord}.
}
$$

因此證書仍位於算子域內。

---

# 17. Meta

$$
\boxed{
\mathcal M
:
\mathcal O_t
\rightharpoonup
\mathcal O_{t+1}.
}
$$

作用於算子束時：

$$
\boxed{
\mathcal M_t:
\mathbb O_t
\rightharpoonup
\mathbb O_{t+1}.
}
$$

Meta 承擔：

- rule rewrite；
- operator birth；
- type-regime transition；
- schema evolution；
- ECV policy rewrite；
- validator evolution。

---

# 18. 算子束

多算子可形成：

$$
\boxed{
\mathbb O
=
\operatorname{Bundle}
\langle
\mathcal O_1,\ldots,\mathcal O_n
\rangle.
}
$$

Bundle 自身仍是算子：

$$
\operatorname{Op}(\mathbb O)=\mathsf{yes}.
$$

但其可執行性要求：

$$
\boxed{
\mathcal O_{\mathrm{BundleCert}}
(
\mathcal O_1,\ldots,\mathcal O_n
)
=
\mathcal O_{\mathrm{Cert}}^{bundle}.
}
$$

---

# 19. 合成算子 $\diamond$

定義部分合成：

$$
\boxed{
\diamond:
(
\mathcal O_2,\mathcal O_1,\Gamma
)
\rightharpoonup
\mathcal O_{21}.
}
$$

若：

$$
\mathsf{CodSig}(\mathcal O_1)
\sim_\Gamma
\mathsf{DomSig}(\mathcal O_2),
$$

且：

$$
\mathcal O_{\mathrm{Certify}}^{comp}
(
\mathcal O_2,\mathcal O_1,\Gamma
)
=
\mathcal O_{\mathrm{Cert}},
$$

則：

$$
\mathcal O_2\diamond\mathcal O_1
\downarrow.
$$

否則：

$$
\mathcal O_2\diamond\mathcal O_1
=
\mathcal O_{\bot}^{comp}.
$$

---

# 20. Identity Operator

每一簽名 $\sigma$ 引入：

$$
\boxed{
\mathcal I_\sigma
:
\sigma
\rightharpoonup
\sigma.
}
$$

候選公理：

$$
\mathcal O\diamond\mathcal I_{\sigma^-}
\simeq
\mathcal O,
$$

$$
\mathcal I_{\sigma^+}\diamond\mathcal O
\simeq
\mathcal O,
$$

前提是對應作用均定義。

這是 algebraic identity，不等於 RDSS 的 entity identity。

---

# 21. 條件性結合律

不預設全域：

$$
(\mathcal O_3\diamond\mathcal O_2)\diamond\mathcal O_1
=
\mathcal O_3\diamond(\mathcal O_2\diamond\mathcal O_1).
$$

定義結合律證書算子：

$$
\boxed{
\mathcal O_{\mathrm{AssocCert}}
:
(
\mathcal O_3,
\mathcal O_2,
\mathcal O_1,
\Gamma
)
\rightharpoonup
\mathcal O_{\mathrm{Cert}}^{assoc}.
}
$$

只有：

$$
\mathcal O_{\mathrm{AssocCert}}
\downarrow
$$

時，才有：

$$
\boxed{
(\mathcal O_3\diamond\mathcal O_2)\diamond\mathcal O_1
\simeq_\Gamma
\mathcal O_3\diamond(\mathcal O_2\diamond\mathcal O_1).
}
$$

證書至少檢查：

1. 兩種括號次序皆定義；
2. Bridge 選擇相容；
3. History effect 相容；
4. Side effect 相容；
5. Invariant 相容；
6. Projection loss 相容；
7. Authority 不因括號改變。

因此 Operator-Native RDSS 目前不是普通 category，而是**條件性部分合成系統**。

---

# 22. 非交換性

一般：

$$
\boxed{
\mathcal O_2\diamond\mathcal O_1
\not\simeq
\mathcal O_1\diamond\mathcal O_2.
}
$$

順序差異可以來自：

- state mutation；
- history；
- side effect；
- causal direction；
- authority；
- resource consumption；
- non-idempotent bridge。

因此非交換是預設，而交換需要證書。

---

# 23. Exchange / Commutation Certificate

若希望：

$$
\mathcal O_A\diamond\mathcal O_B
\simeq
\mathcal O_B\diamond\mathcal O_A,
$$

必須取得：

$$
\boxed{
\mathcal O_{\mathrm{CommCert}}
(
\mathcal O_A,\mathcal O_B,\Gamma
)
=
\mathcal O_{\mathrm{Cert}}^{comm}.
}
$$

---

# 24. Projection–Meta Compatibility

重要問題：

$$
\mathcal O_\Pi
\diamond
\mathcal M
\stackrel{?}{\simeq}
\overline{\mathcal M}
\diamond
\mathcal O_\Pi.
$$

定義：

$$
\boxed{
\mathcal O_{\Pi M\mathrm{Cert}}
:
(
\mathcal O_\Pi,
\mathcal M,
\Gamma
)
\rightharpoonup
\mathcal O_{\mathrm{Cert}}^{\Pi M}.
}
$$

若存在某 projected meta-operator：

$$
\overline{\mathcal M},
$$

使：

$$
\boxed{
\mathcal O_\Pi
\diamond
\mathcal M
\simeq
\overline{\mathcal M}
\diamond
\mathcal O_\Pi,
}
$$

則稱 **projection-stable meta-transition**。

若不存在，表示 Meta 改寫包含被投影掉但對未來重要的結構，父層投影不能安全忽略。

---

# 25. History–Composition Compatibility

希望研究：

$$
\mathcal O_{\mathrm{Remember}}
(
\mathcal O_2\diamond\mathcal O_1
)
$$

是否可由局部歷史組合得到。

定義 Trace composition：

$$
\boxed{
\mathcal O_{\mathrm{TraceComp}}
:
(
Trace(\mathcal O_1),
Trace(\mathcal O_2)
)
\rightharpoonup
Trace(\mathcal O_2\diamond\mathcal O_1).
}
$$

若：

$$
\boxed{
Remember(
Trace_2\oplus Trace_1
)
\simeq
Remember(Trace_2)
\diamond_H
Remember(Trace_1),
}
$$

則稱 history compiler 在該子類上具有**合成相容性**。

不預設全域 functoriality。

---

# 26. Bridge Composition

兩個橋接：

$$
\mathcal O_{B_1}:A\rightharpoonup B,
$$

$$
\mathcal O_{B_2}:B\rightharpoonup C
$$

若合法，可得：

$$
\boxed{
\mathcal O_{B_2}
\diamond
\mathcal O_{B_1}
:
A\rightharpoonup C.
}
$$

但證書需合成：

$$
\boxed{
\mathcal O_{\mathrm{CertComp}}
:
(
Cert_1,
Cert_2
)
\rightharpoonup
Cert_{21}.
}
$$

若中間投影有損：

$$
Loss(B_2\diamond B_1)
$$

需重新計算，不能只相加而不檢查語義。

---

# 27. Container Macro

Container 不設為原語。

定義宏：

$$
\boxed{
\mathcal O_{\mathrm{Container}}
=
\operatorname{Bundle}
\langle
Realize,
Gate,
Relate,
Project,
Certify,
Expand,
Pack
\rangle.
}
$$

其中 Expand / Pack 可由 Transform + Select + Project 的特化組合實現。

因此 Container 是高階 operator pattern。

---

# 28. ECV Macro

ECV 亦不是原語，而是：

$$
\boxed{
\mathcal O_{ECV}
=
\mathcal O_V
\diamond
\mathcal O_C
\diamond
\mathcal O_E.
}
$$

其中：

- $\mathcal O_E$ 通常由 Select + Transform + Realize 組合；
- $\mathcal O_C$ 通常由 Relate + Bridge + Gate 組合；
- $\mathcal O_V$ 通常由 Project + Certify + Transform 組合。

---

# 29. ECV Normal Form：不作全域公理

定義 ECV-reducible 子類：

$$
\boxed{
\mathfrak D_{ECV}
\subseteq
\mathfrak D_{\mathrm{RDSS}}.
}
$$

若某合法算子鏈 $\mathcal O$ 存在：

$$
\mathcal O_E,\mathcal O_C,\mathcal O_V
$$

使：

$$
\boxed{
\mathcal O
\simeq_\Gamma
\mathcal O_V
\diamond
\mathcal O_C
\diamond
\mathcal O_E,
}
$$

且存在 ECV equivalence certificate，才稱 $\mathcal O$ 具有 ECV normal form。

因此：

$$
\boxed{
\text{ECV Normal Form}
}
$$

目前是**子類性質／待證問題**，不是 universal theorem。

---

# 30. Runtime Macro

Runtime lifecycle 可寫為：

$$
\boxed{
\mathcal O_{\mathrm{Runtime}}
=
\mathcal O_{\mathrm{Remember}}
\diamond
\mathcal O_{\mathrm{Certify}}
\diamond
\mathcal O_{\mathrm{Project}}
\diamond
\mathcal O_{\mathrm{Transform}}
\diamond
\mathcal O_{\mathrm{Gate}}
\diamond
\mathcal O_{\mathrm{Select}}
\diamond
\mathcal O_{\mathrm{Realize}}.
}
$$

這不是唯一順序，而是一個典型**admissible execution skeleton**。

若需要跨域：

$$
\mathcal O_{\mathrm{Bridge}}
$$

插入 Gate / Transform 之間。

若需要 schema 改寫：

$$
\mathcal M
$$

只能在 Proposal / Certify / Authority 條件滿足後加入。

---

# 31. Meta Safety

定義：

$$
\boxed{
\mathcal O_{\mathrm{MetaSafe}}
:
(
\mathcal M,
\mathbb O,
\Gamma
)
\rightharpoonup
\mathcal O_{\mathrm{Cert}}^{meta}.
}
$$

至少檢查：

- hard invariant；
- authority；
- migration；
- version lineage；
- rollback；
- affected bridges；
- validator compatibility；
- meta-depth。

只有：

$$
\mathcal O_{\mathrm{MetaSafe}}
\downarrow
$$

才允許：

$$
\mathcal M(\mathbb O)
\downarrow.
$$

---

# 32. Meta-Depth

定義：

$$
\boxed{
\mathcal O_{\mathrm{Depth}}
(
\mathcal M
)
=
d_{\mathrm{meta}}.
}
$$

要求：

$$
d_{\mathrm{meta}}
\le
d_{\max}
$$

或：

$$
Cost_{\mathrm{meta}}
\le
B_{\mathrm{meta}}.
$$

這使反身性保持有限活動支撐。

---

# 33. Operator Identity

定義動態身份判定算子：

$$
\boxed{
\mathcal O_{\mathrm{Identity}}
:
(
\mathcal O_t,
\mathcal O_{t+1},
History,
Contract
)
\rightharpoonup
\{
Same,
Fork,
Clone,
Broken,
Unknown
\}
\times
Cert.
}
$$

因此：

$$
Content_t\neq Content_{t+1}
$$

不必推出身份斷裂。

---

# 34. Version Identity vs Operator Identity

版本相同：

$$
Version(\mathcal O_A)=Version(\mathcal O_B)
$$

不必表示 runtime identity 相同。

內容相同：

$$
Hash(\mathcal O_A)=Hash(\mathcal O_B)
$$

也不必表示 operator identity 相同。

所以：

$$
\boxed{
VersionEquality
\neq
ContentEquality
\neq
OperatorIdentity.
}
$$

---

# 35. Closure

定義 admissible closure：

若：

$$
\mathcal O_1,\mathcal O_2
\in
\mathfrak D_{\mathrm{RDSS}},
$$

且：

$$
\mathcal O_{\mathrm{Certify}}^{comp}
(
\mathcal O_2,\mathcal O_1
)
\downarrow,
$$

則：

$$
\boxed{
\mathcal O_2\diamond\mathcal O_1
\in
\mathfrak D_{\mathrm{RDSS}}.
}
$$

這只是**合法合成閉包**，不是「所有任意作用都封閉」。

---

# 36. Operator Birth

生成新算子：

$$
\boxed{
\mathcal G_{\mathcal O}
:
(
\mathfrak O_t,
\Gamma,
Evidence
)
\rightharpoonup
\mathcal O_{\mathrm{candidate}}.
}
$$

候選算子需依序通過：

$$
Type
\rightarrow
Gate
\rightarrow
Certify
\rightarrow
Authority.
$$

才進入：

$$
\mathfrak O_{t+1}^{authoritative}.
$$

---

# 37. Primitive Completeness：暫不宣稱

12 原語是否完備，目前只提出兩種可測命題。

## 表達候選完備

對 RDSS 01–09 的所有核心公式，是否皆可由 12 原語有限組合表示？

目前 translation matrix 給出初步支持。

## 工程候選完備

對 reference runtime 所需操作，是否皆可由 12 原語實現而不新增基礎 primitive？

仍需 prototype 驗證。

因此不得直接宣稱：

$$
\boxed{
\mathfrak P_{\mathrm{RDSS}}
\text{ 已數學完備}.
}
$$

---

# 38. 可能的八原語壓縮

候選：

$$
\mathfrak P_{\min}
=
\{
Realize,
Transform,
Relate,
Select,
Bridge,
Project,
Certify,
Meta
\}.
$$

其中：

$$
Type
\approx
Select+Certify,
$$

$$
Gate
\approx
Select+Certify,
$$

$$
Remember
\approx
Transform+Project,
$$

$$
Order
\approx
Relate+Certify.
$$

但此壓縮可能失去 Stratum 可讀性。

因此：

$$
\boxed{
12\text{-primitive}
}
$$

目前作為 formal working basis。

---

# 39. 第一代代數公理候選

## A1 — Operatorhood

$$
\forall x\in\mathfrak D_{\mathrm{RDSS}},
\quad
Op(x).
$$

## A2 — Partiality

$$
Op(x)\not\Rightarrow x(y)\downarrow.
$$

## A3 — Restriction

$$
\overline O\diamond\overline O
\simeq
\overline O.
$$

## A4 — Restriction stability

$$
O\diamond\overline O
\simeq
O.
$$

## A5 — Typed identity

$$
O\diamond I_{\sigma^-}
\simeq
O,
$$

$$
I_{\sigma^+}\diamond O
\simeq
O.
$$

## A6 — Certified composition

$$
CertComp(O_2,O_1)
\downarrow
\Rightarrow
O_2\diamond O_1
\downarrow.
$$

## A7 — Bridge necessity

若 codomain / domain 不相容且沒有 bridge：

$$
O_2\diamond O_1
=
O_\bot^{BridgeMissing}.
$$

## A8 — Conditional associativity

$$
AssocCert(O_3,O_2,O_1)
\downarrow
\Rightarrow
(O_3\diamond O_2)\diamond O_1
\simeq
O_3\diamond(O_2\diamond O_1).
$$

## A9 — Witness preservation

正式合成：

$$
O_2\diamond O_1
$$

必須可追到：

$$
Cert_1,Cert_2,Cert_{comp}.
$$

## A10 — Meta governance

$$
MetaSafe(M,O)
\downarrow
\Rightarrow
M(O)\downarrow.
$$

---

# 40. 目前結論

Operator-Native RDSS 的數學核心不再是：

$$
State
+
Relation
+
Container
+
History
+
MetaState.
$$

而是：

$$
\boxed{
\mathfrak D_{\mathrm{RDSS}}
+
\mathfrak P_{\mathrm{RDSS}}
+
\diamond
+
\overline{(\cdot)}
+
Bridge
+
Cert
+
Meta.
}
$$

更口語地：

> **一個最大合法域中，由有型別的部分算子、合法橋接、證書化合成與受治理元算子共同形成的遞歸動態運算系統。**

目前最值得下一輪優先證明／反駁的四件事：

1. restriction-like 公理能否對 12 原語一致成立；
2. 條件性結合律的最小充分條件；
3. 12 原語對 RDSS 01–09 的表達候選完備性；
4. ECV normal form 到底對哪些子類成立、哪些子類必然失敗。
