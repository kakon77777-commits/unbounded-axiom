# Operator-Native RDSS：從六原語到單一型別—效果算子綱要
## From Six Semantic Generators to a Typed-Effect Universal Operator Schema

**版本：** v0.5 Working Draft  
**日期：** 2026-08-10  
**作者：Neo.K**  
**機構：EveMissLab／一言諾科技有限公司**  
**定位：** 形式核心收斂／算子型別—效果系統／原語獨立性修正

---

# 摘要

前一版 ON-RDSS 在 E1「分層、義務保持」等價下得到六個候選生成元：

$$
\{
Realize,
Transform,
Relate,
Select,
Certify,
Meta
\}.
$$

本版進一步指出：這六者可能並非六個「數學本體 primitive」，而更適合被理解為同一個通用部分算子 schema 的六種受約束 **operator profiles**。

真正需要防止的，不是「一個通用 Operator 概念」，而是**無型別、無效果、無元層級紀律的萬能 Transform**。

因此本版提出：

$$
\boxed{
\mathsf{Op}
[
\vec\sigma
\Rightarrow
\tau
\;!\;
\epsilon
\;@\;
d
]
}
$$

作為 ON-RDSS 的第一代統一算子型別。

其中：

- $\vec\sigma$：輸入 sorts 與 arity；
- $\tau$：輸出 sort；
- $\epsilon$：effect / semantic obligation set；
- $d$：meta-depth；
- 作用仍為 partial；
- legality 仍由 context / certificate 決定。

六個原語由此降格為六個 profile，而不是六種不同本體物。

本文件提出三種不同意義的基底：

1. **S6 Semantic Basis**：六種語義角色；
2. **K3 Governed Formal Kernel**：Act / Judge / Meta；
3. **U1 Typed-Effect Universal Operator Schema**：一種 Operator schema，以 type/effect/meta-depth 保留差異。

最終結論是：

$$
\boxed{
\text{One Operator Schema}
\neq
\text{One Undifferentiated Operator}.
}
$$

---

# 1. 前一版六原語

E1 候選：

$$
\boxed{
\mathfrak P_6
=
\{
R,T,L,S,C,M
\},
}
$$

其中：

- $R=Realize$ ；
- $T=Transform$ ；
- $L=Relate$ ；
- $S=Select$ ；
- $C=Certify$ ；
- $M=Meta$。

這六者之所以獨立，依賴五個 separation firewalls：

$$
\boxed{
F
=
\{
Arity,
RelationFormation,
SupportEffect,
ProofRelevance,
MetaDepth
\}.
}
$$

---

# 2. 六原語獨立性的真正來源

## Realize

靠：

$$
Arity=0
$$

與其他正 arity action 分離。

## Transform

靠 input-sensitive ordinary-state mutation 分離。

## Relate

靠：

$$
Arity\ge2
$$

且 codomain 是 relation stratum 分離。

## Select

靠 support-reducing effect 分離。

## Certify

靠 proof-relevant witness birth 分離。

## Meta

靠 meta-depth / rule-space modification 分離。

因此：

$$
\boxed{
\text{六個角色的獨立性}
}
$$

主要來自：

$$
\boxed{
\text{typed/effect distinctions},
}
$$

不一定需要六套完全不同的 primitive constructor。

---

# 3. 壞的一元塌縮：Untyped Act*

若定義一個完全無限制：

$$
Act^\ast
$$

允許：

- 任意 arity；
- 任意 input/output sort；
- 任意 effect；
- 產生 relation；
- 產生 certificate；
- 修改 operator algebra；
- 跨 meta-depth；

則：

$$
\boxed{
Realize,
Transform,
Relate,
Select,
Certify,
Meta
\subseteq
Act^\ast.
}
$$

形式上：

$$
|\mathfrak P|=1.
$$

但此時所有區分只剩自然語言 tag。

所以：

$$
\boxed{
Act^\ast
}
$$

是 presentation collapse，而不是有解釋力的形式統一。

---

# 4. 好的一元統一：Typed-Effect Operator Schema

定義：

$$
\boxed{
\mathsf{Op}
[
(\sigma_1,\ldots,\sigma_n)
\Rightarrow
\tau
\;!\;
\epsilon
\;@\;
d
].
}
$$

其實例：

$$
\mathcal O:
\sigma_1\times\cdots\times\sigma_n
\rightharpoonup
\tau.
$$

其中：

$$
\epsilon
\subseteq
\mathcal E_{\mathrm{effect}}.
$$

例如：

$$
\mathcal E_{\mathrm{effect}}
=
\{
realize,
mutate,
relate,
select,
support\_reduce,
judge,
witness,
project,
loss,
authority,
meta,
rewrite
\}.
$$

---

# 5. Typing Judgment

正式寫：

$$
\boxed{
\Gamma
\vdash
\mathcal O
:
\vec\sigma
\Rightarrow
\tau
\;!\;
\epsilon
\;@\;
d.
}
$$

解讀：

> 在上下文 $\Gamma$ 下，算子 $\mathcal O$ 接受 $\vec\sigma$ 型輸入，產生 $\tau$ 型輸出，具有 effect set $\epsilon$，作用於 meta-depth $d$。

合法可執行性再寫：

$$
\boxed{
\Gamma;\mathcal C
\vdash
\mathcal O
\downarrow.
}
$$

因此：

$$
\boxed{
Typing
\neq
Executability.
}
$$

---

# 6. Realize Profile

$$
\boxed{
\Gamma
\vdash
\mathcal O_R
:
()
\Rightarrow
State
\;!\;
\{realize\}
\;@\;
0.
}
$$

其特徵不是「另一種本體」，而是：

$$
Arity(\mathcal O_R)=0.
$$

---

# 7. Transform Profile

$$
\boxed{
\Gamma
\vdash
\mathcal O_T
:
State
\Rightarrow
State
\;!\;
\{mutate\}
\;@\;
0.
}
$$

更一般：

$$
\mathcal O_T:
\sigma
\rightharpoonup
\tau
$$

但不得跨 operator-algebra meta boundary，除非顯式標記 Meta effect。

---

# 8. Relate Profile

$$
\boxed{
\Gamma
\vdash
\mathcal O_L
:
(State,State)
\Rightarrow
Relation
\;!\;
\{relate\}
\;@\;
0.
}
$$

因此 Relate 的差異由：

$$
Arity\ge2
$$

和：

$$
Codomain=Relation
$$

表達。

---

# 9. Select Profile

$$
\boxed{
\Gamma
\vdash
\mathcal O_S
:
Family[\sigma]
\Rightarrow
Family[\sigma]
\;!\;
\{select,support\_nonincreasing\}
\;@\;
0.
}
$$

其核心 effect obligation：

$$
\boxed{
Supp(
\mathcal O_S(X)
)
\subseteq
Supp(X).
}
$$

若 selector 具有生成能力，則必須另加：

$$
generate
$$

effect，不得仍標為純 Select。

---

# 10. Certify Profile

$$
\boxed{
\Gamma
\vdash
\mathcal O_C
:
Candidate
\Rightarrow
Cert
\;!\;
\{judge,witness,provenance\}
\;@\;
0.
}
$$

其中：

$$
Cert
$$

不是單一 Boolean。

至少可攜帶：

$$
(
Decision,
Reason,
EvidenceRefs,
RuleVersion,
Scope,
Failures,
Timestamp
).
$$

因此：

$$
\boxed{
ProofRelevantCert
\neq
BooleanValidity.
}
$$

---

# 11. Meta Profile

$$
\boxed{
\Gamma
\vdash
\mathcal O_M
:
(
Algebra[d],
Evidence
)
\Rightarrow
Algebra[d+1]
\;!\;
\{meta,rewrite\}
\;@\;
d+1.
}
$$

更精確地，輸出不一定永遠是 $d+1$，但必須顯式改變或作用於 operator-description / rule-space stratum。

Meta 的本質不是名稱，而是：

$$
\boxed{
\Delta RuleSpace\neq0.
}
$$

---

# 12. 六角色成為 Profile Predicates

定義：

$$
\boxed{
Realize(O)
}
$$

當且僅當其 signature / effect 滿足 Realize profile。

類似：

$$
Transform(O),
Relate(O),
Select(O),
Certify(O),
Meta(O).
$$

所以：

$$
\boxed{
Role
=
Predicate(\mathsf{OpSignature}).
}
$$

而不是：

$$
Role
=
SeparateOntology.
$$

---

# 13. 多重角色

一個算子可以同時滿足多個 profile。

例如一個關係生成後同時產生 certificate 的算子：

$$
\Gamma
\vdash
O
:
(A,B)
\Rightarrow
(Relation,Cert)
!
\{relate,judge,witness\}.
$$

則：

$$
Relate(O)=1,
$$

且：

$$
CertifyAspect(O)=1.
$$

因此 Role 不再需要互斥。

這比「每個算子只能屬於一種 primitive」更符合分域算子本體論的多作用面思想。

---

# 14. K3：Governed Formal Kernel

雖然可以使用單一 schema，但工程／形式語義上仍可把 operation constructor 分成三種 kernel modes：

$$
\boxed{
K_3
=
\{
Act,
Judge,
Meta
\}.
}
$$

## Act

改變／產生 ordinary computational structure。

包括：

- Realize；
- Transform；
- Relate；
- Select。

## Judge

產生 proof-relevant admissibility / evidence / certificate。

即原 Certify。

## Meta

改變 operator / rule / algebra description。

---

# 15. 為什麼 K3 有工程價值？

因為三者可以直接對應三個 Runtime plane：

$$
\boxed{
ExecutionPlane
\leftrightarrow
Act
}
$$

$$
\boxed{
VerificationPlane
\leftrightarrow
Judge
}
$$

$$
\boxed{
MetaGovernancePlane
\leftrightarrow
Meta.
}
$$

這比六個 Runtime engine 更簡潔。

六角色仍保留在 signature / effect system 中。

---

# 16. K3 也不是絕對最小

如果把：

$$
Judge
$$

視為：

$$
Act:
Candidate\to Cert,
$$

則：

$$
K_3
\rightarrow
K_2
=
\{Act,Meta\}.
$$

如果把 operator algebra reify 成 ordinary data，使：

$$
Meta
$$

也只是：

$$
Act:
Algebra\to Algebra,
$$

則：

$$
K_2
\rightarrow
K_1.
$$

因此：

$$
\boxed{
\text{Primitive count itself has no meaning without a type/effect discipline}.
}
$$

---

# 17. Reflection 對 Meta 獨立性的挑戰

Reflective rewriting systems 已展示：object theory / rewrite theory 可以在一個 universal reflective theory 中被 reify 並作為可計算資料處理。

因此：

$$
\boxed{
Meta
}
$$

不是數學上先驗不可還原的 primitive。

ON-RDSS 若要保留 Meta role，理由應是：

$$
\boxed{
\text{governance/type-effect separation},
}
$$

而不是宣稱所有數學框架都必須有不可還原 meta operator。

---

# 18. Meta-depth 仍然重要

即使同一 universal theory 可以承載多層 reflection，ON-RDSS Runtime 仍需要：

$$
\boxed{
Depth(O)=d.
}
$$

原因不是本體論純潔性，而是：

- authority；
- rollback；
- replay；
- validation；
- resource budget；
- reflective regress；

需要知道「這次作用正在修改哪一層規則」。

因此 Meta-depth 是 effect-system 欄位。

---

# 19. Composition Typing Rule

假設：

$$
\Gamma
\vdash
O_1:
\vec\sigma
\Rightarrow
\tau
!
\epsilon_1
@
d_1,
$$

以及：

$$
\Gamma
\vdash
O_2:
(\tau,\vec\rho)
\Rightarrow
\upsilon
!
\epsilon_2
@
d_2.
$$

若：

$$
Adm_\Gamma(O_2,O_1)
$$

與：

$$
CertComp(O_2,O_1)\downarrow,
$$

則：

$$
\boxed{
\Gamma
\vdash
O_2\diamond O_1
:
(\vec\sigma,\vec\rho)
\Rightarrow
\upsilon
!
(\epsilon_1\sqcup\epsilon_2)
@
\max(d_1,d_2).
}
$$

但若 effect interaction 有特殊規則，例如：

$$
project
+
mutate,
$$

需額外 critical-pair / effect compatibility judgment。

---

# 20. Effect Compatibility

定義：

$$
\boxed{
\mathcal O_{\mathrm{EffCompat}}
:
(
\epsilon_1,
\epsilon_2,
\Gamma
)
\rightharpoonup
\{
Compatible,
OrderedOnly,
BridgeRequired,
Conflict
\}
\times Cert.
}
$$

例如：

## Pure relation + pure relation

可能 Compatible。

## Project + Mutate

可能 OrderedOnly。

## AuthorityWrite + RuntimeObserve

可能 Conflict，除非經 Proposal / Judge / Commit path。

## Meta + Meta

需 Meta critical-pair analysis。

---

# 21. Proof-Relevance Firewall

如果：

$$
Cert
=
Bool,
$$

則 Certify 很可能進一步被普通 Act / Select 吸收。

因此 ON-RDSS 要求 governance-critical certificate 採 proof-relevant semantics：

$$
\boxed{
Cert
=
(
Decision,
Witness,
Provenance,
RuleVersion,
Scope
).
}
$$

這使：

$$
\boxed{
Judge
}
$$

在工程層保持獨立價值。

這是一個設計／治理約束，而非普遍數學定理。

---

# 22. Good U1 vs Bad K1

## Bad K1

$$
Act^\ast
$$

只有一個名字，所有差異是 informal tags。

結果：

$$
\boxed{
\text{概念失去區分力}.
}
$$

## Good U1

$$
\boxed{
\mathsf{Op}
[
\vec\sigma
\Rightarrow
\tau
!
\epsilon
@
d
].
}
$$

雖然只有一種 Operator schema，但：

- arity 可檢查；
- sorts 可檢查；
- effects 可檢查；
- meta-depth 可檢查；
- certificate obligations 可檢查；
- partiality 可檢查。

因此：

$$
\boxed{
OneSchema
\neq
OneSemantics.
}
$$

---

# 23. 與多分型代數理論的接口

多分型 algebraic theory 的一般思想允許不同 sorts 上存在不同 arity 的 operations，並研究這些 operations 的 models。

ON-RDSS 可以保守地借用這種：

$$
\boxed{
\text{many-sorted signature discipline}
}
$$

來承載：

- State；
- Relation；
- Family；
- Cert；
- Algebra；
- Evidence；

而不需要把這些重新提升成互相競爭的本體。

它們只是 Operator signature 的不同 sorts。

---

# 24. 新的最小表示

因此 ON-RDSS 的深層形式核心可以重新寫成：

$$
\boxed{
\mathfrak D_{\mathrm{RDSS}}
+
\Sigma_{\mathrm{sort}}
+
\Sigma_{\mathrm{effect}}
+
\mathsf{Op}
+
\mathcal W
+
\Rightarrow_{\Gamma,Cert}
+
\mathcal M_{\mathrm{version}}.
}
$$

其中：

- $\mathfrak D_{\mathrm{RDSS}}$：最大域；
- $\Sigma_{\mathrm{sort}}$：多分型簽名；
- $\Sigma_{\mathrm{effect}}$：效果／義務簽名；
- $\mathsf{Op}$：單一 typed partial operator schema；
- $\mathcal W$：operator words / wiring；
- $\Rightarrow$：certified reduction；
- $\mathcal M_{\mathrm{version}}$：operator algebra version evolution。

---

# 25. 六角色不消失，而是升格為 Profile Library

定義：

$$
\boxed{
\mathfrak R_{\mathrm{profiles}}
=
\{
Realize,
Transform,
Relate,
Select,
Certify,
Meta,
Bridge,
Project,
Remember,
Order,
Gate,\ldots
\}.
}
$$

這些不再叫 primitive。

更適合叫：

$$
\boxed{
\text{Certified Operator Profiles}.
}
$$

每個 profile 指定：

- required arity；
- required sorts；
- required effects；
- forbidden effects；
- meta-depth；
- certificate obligations；
- algebraic laws。

---

# 26. Bridge Profile

例如：

$$
Bridge(O)
$$

要求：

$$
\Gamma
\vdash
O:
B
\Rightarrow
C
!
\{
transform,
cross\_domain,
loss?
\}
@
d
$$

以及：

$$
BridgeCert(O)\downarrow.
$$

所以 Bridge 不需要 primitive status，仍具有完整正式語義。

---

# 27. Remember Profile

$$
Remember(O)
$$

要求：

- input 是 trajectory/history sort；
- output 是 operational memory sort；
- effects 包含 history-compress；
- provenance preserved；
- loss bound 可證。

因此它仍是獨立可檢查 profile。

---

# 28. Operator Ontology 與這個結果

這一步其實更接近算子本體論最初方向。

不是：

> 世界底層存在六種本體。

而是：

$$
\boxed{
\text{世界／系統只需要一種「算子」基本語法，}
}
$$

但每一次算子出現都必須明示：

$$
\boxed{
\text{它作用於誰、輸出什麼、產生什麼效果、位於哪一層、憑什麼合法。}
}
$$

所以「萬物皆算子」與「不可亂算」第一次在同一型別系統中真正合流。

---

# 29. 本輪有限 checker

本輪 toy checker 建立一個統一：

```text
OpSig(inputs, output, effects, meta_depth)
```

並成功將六個舊原語分別分類為：

- Realize profile；
- Transform profile；
- Relate profile；
- Select profile；
- Certify profile；
- Meta profile。

同時測試：

- State-realization 可接 State-transform；
- State-realization 可作為 Relate 的一個輸入；
- Cert 不可直接接到 Algebra input；
- State 不可直接接 Family<State> selector。

這證明「單一 operator schema」不必等於「失去型別安全」。

但這仍是有限 toy type checker，不是完整 type soundness proof。

---

# 30. 下一步

現在真正值得做的已不是：

$$
6\to5?
$$

而是把：

$$
\boxed{
\mathsf{Op}
[
\vec\sigma
\Rightarrow
\tau
!
\epsilon
@
d
]
}
$$

發展成正式的 ON-RDSS Type-and-Effect Calculus。

需要：

1. sort formation rules；
2. operator formation rules；
3. effect lattice / effect algebra；
4. composition typing；
5. partiality / restriction typing；
6. certificate typing；
7. meta-depth rules；
8. wiring typing；
9. subject reduction；
10. progress / explicit residual theorem。

---

# 31. 暫定結論

本輪最大的修正是：

$$
\boxed{
12\ primitives
\rightarrow
6\ semantic\ generators
\rightarrow
1\ typed\ operator\ schema
}
$$

並不矛盾。

三者處於不同層：

$$
\boxed{
\text{Profile Layer}
}
$$

保留 12+ 個有意義的 operator profiles。

$$
\boxed{
\text{Semantic Generator Layer}
}
$$

暫時保留六種基本作用面。

$$
\boxed{
\text{Formal Syntax Layer}
}
$$

可以只有一種：

$$
\mathsf{Op}[\vec\sigma\Rightarrow\tau!\epsilon@d].
$$

真正避免 tautology 的不是 primitive 名稱數量，而是：

$$
\boxed{
\text{Type}
+
\text{Effect}
+
\text{Partiality}
+
\text{Certificate}
+
\text{MetaDepth}.
}
$$

因此 ON-RDSS 現在可以第一次真正地說：

> **域內一切皆是算子，但每一算子都必須在可檢查的多分型、效果、部分作用與元層級制度中取得自己的作用資格。**
