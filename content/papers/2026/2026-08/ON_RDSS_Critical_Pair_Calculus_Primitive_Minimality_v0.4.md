# Operator-Native RDSS：Critical Pair Calculus、條件合流與原語最小性
## Critical-Pair Calculus, Conditional Confluence, and Primitive Minimality in Operator-Native RDSS

**版本：** v0.4 Working Draft  
**日期：** 2026-08-10  
**作者：Neo.K**  
**機構：EveMissLab／一言諾科技有限公司**  
**定位：** 深層形式化／有限模型驗證／原語消除分析

---

# 摘要

本文件在 ON-RDSS v0.3 的 Certified Paracomposition 與 normalization framework 上再推進三步：

1. 將六類 Critical Pair 提升為統一的 **Critical-Pair Calculus**；
2. 把 Newman-style termination + local confluence 的路線限制在固定 Operator Algebra Snapshot 下，避免 Meta-Operator 在 normalization 途中改變重寫系統；
3. 建立第一個 primitive elimination checker，測試 12 原語在不同等價標準下的最小性。

本輪最重要的結果是：

$$
\boxed{
\text{Primitive Minimality is Equivalence-Relative}.
}
$$

若只要求 extensional input-output equivalence，則一個不受限制、可跨 arity / stratum / meta-depth 的萬能 `Transform*` 幾乎可模擬全部原語，導致原語理論塌縮。

若要求：

$$
\boxed{
\text{arity}
+
\text{stratum}
+
\text{meta-depth}
+
\text{semantic obligations}
}
$$

被保存，則有限 derivability model 得到唯一的 6 原語候選基底：

$$
\boxed{
\mathfrak P_6
=
\{
Realize,
Transform,
Relate,
Select,
Certify,
Meta
\}.
}
$$

而：

$$
Type,
Gate,
Bridge,
Project,
Remember,
Order
$$

可以在明示 specification / policy / certificate 條件下作為派生宏。

此結果不是數學最小性證明，而是一個第一代有限模型假說。

---

# 1. 為什麼先處理 Critical Pair，而不是直接證結合律？

ON-RDSS 的 reduction relation：

$$
W
\Rightarrow_{\Gamma,c}
W'
$$

不是純語法重寫。

每一步還依賴：

- Type；
- Bridge；
- History；
- Authority；
- Certificate；
- Projection loss；
- Algebra version。

因此：

$$
\boxed{
\text{Associativity}
}
$$

不能只靠：

$$
(O_3\diamond O_2)\diamond O_1
=
O_3\diamond(O_2\diamond O_1)
$$

這種無條件等式建立。

真正要檢查的是：

> 兩條合法 reduction path 在相同 Operator Algebra Snapshot 下是否可 join？

所以 Critical Pair 是更底層的分析單位。

---

# 2. 統一 Critical Pair 定義

定義 ON-RDSS Critical Pair：

$$
\boxed{
CP
=
\left\langle
W,
r_1@i,
r_2@j,
W_1,
W_2,
\Gamma,
\mathfrak A,
Obl
\right\rangle.
}
$$

其中：

- $W$：共同起始 operator word / wiring；
- $r_1@i$：第一個 reduction rule 與作用位置；
- $r_2@j$：第二個 reduction rule 與作用位置；
- $W_1,W_2$：一步分岔結果；
- $\Gamma$：上下文；
- $\mathfrak A$：Operator Algebra Snapshot；
- $Obl$：兩條路徑的 certificate obligations。

定義 Joinability：

$$
\boxed{
\mathcal O_{\mathrm{Join}}
:
CP
\rightharpoonup
\{
Joinable,
ObsJoinable_Q,
NonJoinable,
Unknown
\}
\times Cert.
}
$$

---

# 3. CP-1：Bracketing Critical Pair

對：

$$
W=[O_1,O_2,O_3],
$$

兩種局部 reduction：

$$
[O_1,O_2,O_3]
\Rightarrow
[O_{21},O_3],
$$

與：

$$
[O_1,O_2,O_3]
\Rightarrow
[O_1,O_{32}].
$$

若兩者最後：

$$
[O_{321}^{(L)}]
$$

與：

$$
[O_{321}^{(R)}]
$$

滿足：

$$
O_{321}^{(L)}
\simeq_\Gamma
O_{321}^{(R)},
$$

才可在該 triple 上發出：

$$
\boxed{
AssocCert(O_3,O_2,O_1).
}
$$

所以結合律被重寫為「所有 relevant bracketing critical pairs 可 join」。

---

# 4. CP-2：Bridge Critical Pair

若：

$$
B_1,B_2:
X\rightharpoonup Y
$$

皆通過 bridge certification，

則：

$$
W
\Rightarrow_{B_1}
W_1,
$$

$$
W
\Rightarrow_{B_2}
W_2.
$$

分三種結果：

## Strong bridge confluence

$$
W_1\Rightarrow^\ast N,
\qquad
W_2\Rightarrow^\ast N.
$$

## Observational bridge confluence

$$
\Pi_Q(N_1)
=
\Pi_Q(N_2).
$$

## Historical bridge divergence

$$
N_1\not\simeq_Q N_2.
$$

第三種要求 Bridge choice 寫入歷史。

---

# 5. CP-3：Projection Critical Pair

比較：

$$
Project\diamond Transform
$$

與：

$$
\overline{Transform}\diamond Project.
$$

若存在 projected transform：

$$
\overline{Transform},
$$

使：

$$
\boxed{
Project
\diamond
Transform
\simeq_Q
\overline{Transform}
\diamond
Project,
}
$$

稱為 projection-stable transformation。

若不存在，表示 projection 丟掉了未來作用需要的資訊。

這對父容器 coarse state 尤其重要。

---

# 6. CP-4：History Critical Pair

若：

$$
O_B\diamond O_A
$$

與：

$$
O_A\diamond O_B
$$

具有相同目前 observable output：

$$
\Pi_Q(Result_{AB})
=
\Pi_Q(Result_{BA}),
$$

但：

$$
H_{AB}
\neq
H_{BA},
$$

且此歷史差異改變後續可達域：

$$
Reach_{AB}
\neq
Reach_{BA},
$$

則：

$$
\boxed{
CP_H
=
NonJoinable.
}
$$

這提供比「現在值不同」更強的 path dependence 判準。

---

# 7. CP-5：Authority Critical Pair

兩條 reduction path：

$$
W\Rightarrow^\ast N_1,
$$

$$
W\Rightarrow^\ast N_2
$$

即使 extensional result 相同，也必須檢查：

$$
AuthorityEffect(N_1)
\stackrel{?}{=}
AuthorityEffect(N_2).
$$

若：

$$
AuthorityEffect(N_1)
\neq
AuthorityEffect(N_2),
$$

則不得以普通 observational equivalence 合流。

所以 Authority 是 confluence semantics 的一部分，不只是 Runtime metadata。

---

# 8. CP-6：Meta Critical Pair

兩個 Meta-Operators：

$$
M_1,
M_2
$$

同時可作用於：

$$
\mathfrak A_t.
$$

形成：

$$
M_2(M_1(\mathfrak A_t))
$$

與：

$$
M_1(M_2(\mathfrak A_t)).
$$

如果：

$$
\boxed{
M_2\circ M_1
\not\simeq
M_1\circ M_2,
}
$$

則產生 Operator Algebra branch。

此時不是普通 execution history，而是：

$$
\boxed{
\text{Algebra History}.
}
$$

---

# 9. Critical Pair 並不全是古典 term-rewriting critical pair

本文件使用 `Critical Pair` 作為 ON-RDSS 廣義術語。

其中：

- Bracketing overlap 比較接近傳統 rewriting critical-pair；
- Bridge / Projection / History / Authority / Meta 則包含語義、治理與版本衝突。

因此更精確名稱可以是：

$$
\boxed{
\text{Certified Semantic Critical Pair}.
}
$$

不要把全部六類誤稱為古典 term-rewriting syntactic critical pairs。

---

# 10. Algebra Snapshot

定義：

$$
\boxed{
\mathfrak A_t
=
(
\mathfrak P_t,
\Sigma_t,
Rules_t,
Bridge_t,
Cert_t,
Equiv_t,
Authority_t
).
}
$$

所有 termination / confluence 討論必須相對：

$$
\boxed{
\mathfrak A_t=\text{fixed}.
}
$$

原因是：

$$
M_t:
\mathfrak A_t
\rightharpoonup
\mathfrak A_{t+1}
$$

若在 normalization 中途發生，

同一 $W$ 的 rewrite relation 已經改變。

---

# 11. Algebra Lock

定義：

$$
\boxed{
Lock(W)
=
SnapshotID(\mathfrak A_t).
}
$$

一次 normalization：

$$
W
\Rightarrow^\ast
NF_{\mathfrak A_t}(W)
$$

必須固定：

- rule version；
- type version；
- bridge registry；
- certifier；
- equivalence relation；
- authority policy。

這不要求全系統停止，只要求此次 reduction trace 的 formal semantics 固定。

---

# 12. Newman-style 路線的正確使用位置

在一般抽象 rewriting system 中，終止性加局部合流可導向全域合流。

ON-RDSS 若要借用這一路線，必須限制在：

$$
\boxed{
\text{Fixed Algebra Snapshot}
}
$$

下的 terminating rewrite subsystem。

因此候選路線為：

$$
\boxed{
Termination_{\mathfrak A}
+
LocalConfluence_{\mathfrak A}
\Rightarrow
Confluence_{\mathfrak A}.
}
$$

但若：

$$
\mathfrak A_t
\rightarrow
\mathfrak A_{t+1}
$$

發生於 normalization 中途，不能直接套用固定 rewriting system 的結論。

---

# 13. Observational Confluence 不自動繼承

即使：

$$
\Pi_Q(N_1)
=
\Pi_Q(N_2),
$$

也不能直接說：

$$
N_1,N_2
$$

在完整系統中 confluent。

只能說：

$$
\boxed{
N_1
\simeq_Q
N_2.
}
$$

如果後續 operator：

$$
O_{future}
$$

能重新看見投影丟掉的差異，

則：

$$
\simeq_Q
$$

不一定是 congruence。

所以還需要檢查：

$$
N_1\simeq_Q N_2
\Rightarrow
O(N_1)\simeq_Q O(N_2)
$$

是否對允許的 future operator class 成立。

---

# 14. Primitive Minimality 必須先定義「等價」

考慮：

$$
Type,
Gate,
Bridge,
Project,
Remember,
Order.
$$

它們表面都可以說是某種 transformation。

若 `Transform` 被允許：

- 任意 arity；
- 任意 input/output stratum；
- 產生 judgment；
- 產生 relation；
- 修改 operator algebra；
- 形成 nullary value；

那麼：

$$
\boxed{
\mathfrak P
=
\{Transform^\ast\}
}
$$

就能 extensional 模擬所有 primitive。

這個結果幾乎沒有理論價值。

因此 primitive minimality 必須 relative to equivalence regime。

---

# 15. 三種 Equivalence Regime

## E0 — Extensional Untyped Equivalence

只要求 input-output 行為可模擬。

結果：

$$
\boxed{
|\mathfrak P_{min}^{E0}|
=
1.
}
$$

候選：

$$
\{Transform^\ast\}.
$$

此塌縮被視為反例：E0 太弱，不能作為 ON-RDSS 的本體／原語等價標準。

---

## E1 — Stratified Obligation-Preserving Equivalence

要求保存：

- arity；
- stratum；
- meta-depth；
- primary semantic obligation；
- certificate obligations；
- history / loss / authority effect。

本輪有限 checker 得到：

$$
\boxed{
|\mathfrak P_{min}^{E1}|
=
6.
}
$$

唯一候選基底：

$$
\boxed{
\mathfrak P_6
=
\{
Realize,
Transform,
Relate,
Select,
Certify,
Meta
\}.
}
$$

---

## E2 — Role-Preserving Equivalence

若每一具名語義角色本身都要求被視為 primitive identity，

則：

$$
\boxed{
|\mathfrak P_{min}^{E2}|
=
12.
}
$$

這是最保守版本。

---

# 16. E1 六原語候選的推導

在 static specification 可作為參數而非 computational primitive 的前提下：

## Type

$$
\boxed{
Type
\approx
Select
+
Certify
+
TYPE\_SCHEMA.
}
$$

---

## Gate

$$
\boxed{
Gate
\approx
Select
+
Certify
+
POLICY.
}
$$

---

## Project

$$
\boxed{
Project
\approx
Transform
+
Certify
+
LOSS\_SPEC.
}
$$

---

## Order

$$
\boxed{
Order
\approx
Relate
+
Certify
+
ORDER\_AXIOMS.
}
$$

---

## Bridge

$$
\boxed{
Bridge
\approx
Transform
+
Type
+
Certify
+
BRIDGE\_SPEC.
}
$$

進一步代入 Type：

$$
Bridge
\approx
Transform
+
Select
+
Certify
+
TYPE\_SCHEMA
+
BRIDGE\_SPEC.
$$

---

## Remember

$$
\boxed{
Remember
\approx
Transform
+
Project
+
Certify
+
HISTORY\_SPEC.
}
$$

再展開：

$$
Remember
\approx
Transform
+
Certify
+
LOSS\_SPEC
+
HISTORY\_SPEC.
$$

---

# 17. 六個目前不可消除的候選

有限 E1 checker 中：

$$
\boxed{
Realize
}
$$

不可由其他 primitive 推導，因其是 nullary realization。

$$
\boxed{
Transform
}
$$

不可消除，因它是 first-order state/value change。

$$
\boxed{
Relate
}
$$

不可消除，因它是 multi-input relation-producing action。

$$
\boxed{
Select
}
$$

不可消除，因 subset / continuation selection 不是普通 value transform。

$$
\boxed{
Certify
}
$$

不可消除，因 witness / admissibility judgment 不能由被判定作用本身自動產生。

$$
\boxed{
Meta
}
$$

不可消除，因它跨越 meta-depth，修改 operator / algebra rules 本身。

---

# 18. 為什麼 Meta 不能降成 Transform？

如果允許：

$$
Transform:
\mathfrak A_t
\to
\mathfrak A_{t+1},
$$

那 Meta 的確會被 Transform 吞掉。

因此 ON-RDSS 必須保留：

$$
\boxed{
\text{Meta-Depth Stratification}.
}
$$

定義：

$$
Depth(Transform)=0,
$$

$$
Depth(Meta)\ge1.
$$

普通 Transform 必須：

$$
\boxed{
Depth_{out}
=
Depth_{in}.
}
$$

Meta 則允許：

$$
\boxed{
RuleSpace_{out}
\neq
RuleSpace_{in}.
}
$$

這個分層是防止「萬物 Transform 化」的核心公理候選。

---

# 19. 為什麼 Realize 不能降成 Transform？

若 Transform 被允許有：

$$
\mathbf1\to X
$$

的 nullary signature，

則 Realize 也消失。

因此 E1 要求：

$$
\boxed{
Arity(Transform)\ge1,
}
$$

而：

$$
\boxed{
Arity(Realize)=0.
}
$$

所以 primitive independence 依賴 arity discipline。

---

# 20. 為什麼 Relate 不能降成 Transform？

若 Transform 可自由接受多個 operator 並輸出 relation operator，

則 Relate 也會塌縮。

E1 因此限制：

$$
Transform:
O_x\rightharpoonup O_y
$$

為 single-subject transformation，

而：

$$
Relate:
(O_x,O_y,\ldots)
\rightharpoonup
O_{rel}
$$

為 relation-forming action。

這是另一個 primitive-separation axiom。

---

# 21. Primitive Minimality 的真正形式

原語最小性不應只問：

$$
P_i
\stackrel{?}{\in}
Closure(\mathfrak P\setminus\{P_i\}).
$$

而應問：

$$
\boxed{
P_i
\stackrel{?}{\in}
Closure_{E,\Gamma,Obligation}
(
\mathfrak P\setminus\{P_i\}
).
}
$$

其中：

- $E$：等價制度；
- $\Gamma$：結構域；
- `Obligation`：必須保存的語義義務。

所以不存在脫離等價制度的「絕對最小原語數」。

---

# 22. Primitive Checker 實驗結果

本輪有限 checker 對 12 原語逐一移除。

結果：

| Primitive | 移除後可導出？ |
|---|---:|
| Realize | 否 |
| Transform | 否 |
| Relate | 否 |
| Type | 是 |
| Select | 否 |
| Gate | 是 |
| Bridge | 是 |
| Project | 是 |
| Remember | 是 |
| Order | 是 |
| Certify | 否 |
| Meta | 否 |

所以 E1 toy model 得：

$$
\boxed{
\mathfrak P_6
=
\{
Realize,
Transform,
Relate,
Select,
Certify,
Meta
\}.
}
$$

---

# 23. 此結果不能如何解讀？

不能說：

> ON-RDSS 已證明只有六個基本算子。

因為推導結果依賴：

1. 我們選定的 semantic obligations；
2. specification 被視為參數而非 primitive；
3. Transform 的 arity / meta-depth 限制；
4. Select / Certify 的能力定義；
5. 尚未加入真實 wiring semantics。

正確說法是：

$$
\boxed{
\text{在 E1 有限義務模型下，存在一個六生成元候選。}
}
$$

---

# 24. 下一步：六原語是否還能繼續縮？

現在應逐一攻擊：

## Realize vs Select

能否把 realization 視為從候選 singleton family 中選取？

如果可以，Realize 可能被 Select 吃掉。

但如果候選不存在以前就需要 Realize，則循環。

---

## Relate vs Transform

若 relation object 可以由對 pair-state 的 Transform 產生，

Relate 可能不獨立。

但那會把 unary / multi-object stratum 再次混合。

---

## Select vs Relate + Certify

選擇是否可以被編碼為 relation-to-preference + certified maximal element？

如果可以，Select 可能被導出。

但 infinite / partial / multiobjective selection 未必能如此簡化。

---

## Certify vs Meta

如果 certificate regime 本身是 Meta 產物，Certify 是否仍 primitive？

Meta 可以改 certifier，不代表能替代 certifier 的當次 judgment。

目前兩者應分離。

---

# 25. 六原語候選的結構角色

六個候選恰好形成六種不可直接互換的作用面：

$$
\boxed{
Realize
}
$$

回答「有什麼當前被實現」。

$$
\boxed{
Transform
}
$$

回答「它如何改變」。

$$
\boxed{
Relate
}
$$

回答「多個存在如何形成關係」。

$$
\boxed{
Select
}
$$

回答「哪些可能性當前被採用」。

$$
\boxed{
Certify
}
$$

回答「為何這次作用可以被承認」。

$$
\boxed{
Meta
}
$$

回答「以上規則如何改變」。

這六個目前比十二個更像真正的 generator candidates。

---

# 26. ECV 在六原語下的重構

原來：

$$
E
\sim
Select+Transform+Realize.
$$

$$
C
\sim
Relate+Bridge+Gate.
$$

由於：

$$
Bridge
\approx
Transform+Select+Certify,
$$

$$
Gate
\approx
Select+Certify,
$$

所以：

$$
\boxed{
C
\sim
Relate
+
Transform
+
Select
+
Certify.
}
$$

而：

$$
V
\sim
Project+Certify+Transform
$$

且：

$$
Project
\approx
Transform+Certify,
$$

故：

$$
\boxed{
V
\sim
Transform+Certify.
}
$$

因此 ECV 甚至可重寫成六原語的高階 pattern，而不是獨立運算基礎。

---

# 27. ON-RDSS 最小候選生成系統

若 E1 六原語成立，最小候選可寫：

$$
\boxed{
\mathfrak B_{\mathrm{ONRDSS}}
=
(
\mathfrak D,
\{
R,T,L,S,C,M
\},
\mathcal W,
\Rightarrow,
\Gamma,
Cert
)
}
$$

其中：

- $R=Realize$ ；
- $T=Transform$ ；
- $L=Relate$ ；
- $S=Select$ ；
- $C=Certify$ ；
- $M=Meta$。

Operator words：

$$
\mathcal W
=
\mathcal W(R,T,L,S,C,M).
$$

其他 RDSS 語義由 certified macros 建立。

---

# 28. 新的研究主問題

到這一層後，研究問題已經從：

> RDSS 能不能全部算子化？

變成：

> **是否存在一個小型、分層、部分可組合的算子生成集，使 RDSS 的所有高階語義都能由 certified rewriting 導出？**

也就是：

$$
\boxed{
\text{Find minimal }
\mathfrak P
\text{ such that }
Closure_{E,\Gamma,Cert}(\mathfrak P)
\supseteq
RDSSCore.
}
$$

---

# 29. 下一輪最值得做的事

1. 對六原語逐一做反向消除攻擊；
2. 建立 arity / stratum / meta-depth 的正式型別系統；
3. 對固定 Algebra Snapshot 實作 local critical-pair checker；
4. 將 six-generator words 接到 typed wiring graph；
5. 測試是否存在 5-generator 或更小候選；
6. 找到第一個「不能由六原語合法表示」的 RDSS 操作，若存在即推翻六原語假說。

---

# 30. 暫定結論

目前 ON-RDSS 已出現三層收斂：

第一層：

$$
RDSS\ 01\text{--}09
\rightarrow
12\ operator\ families.
$$

第二層：

$$
12
\rightarrow
\boxed{
6\ candidate\ generators
}
$$

在 E1 obligation-preserving equivalence 下。

第三層的真正問題是：

$$
\boxed{
6
\stackrel{?}{\rightarrow}
5,4,\ldots
}
$$

但這一步不能靠語言直覺，而必須靠：

- typed derivability；
- semantic obligations；
- critical-pair behavior；
- counterexample construction。

所以現在我們第一次真正有了一個可以「往下證最小性」的方向。
