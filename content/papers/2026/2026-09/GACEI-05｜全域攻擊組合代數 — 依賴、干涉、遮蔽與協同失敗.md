---
title: "GACEI-05｜全域攻擊組合代數：依賴、干涉、遮蔽與協同失敗"
title_en: "GACEI-05 | Algebra of Global Attack Composition: Dependency, Interference, Masking, and Synergistic Failure"
series: "全域對抗計算與 AI 工程智能系列"
series_en: "Global Adversarial Computation and AI Engineering Intelligence Series"
series_id: "GACEI-2026"
paper_id: "GACEI-05"
version: "v0.1"
date: "2026-09-08"
language: "zh-Hant"
author: "Neo.K"
organization: "EveMissLab / 一言諾科技有限公司"
document_type: "研究論文 / 對抗組合演算 / 全域驗證 / AI 工程智能"
status: "Canonical Draft"
canonical_source: "UTF-8 Markdown"
math_source_rule: "inline math only $...$ ; display math only $$...$$"
security_scope: "Authorized, isolated, recoverable software testing and simulation only"
depends_on:
  - "GACEI-01 全域對抗計算總論 v0.1"
  - "GACEI-02 MSSP 的對偶 v0.1"
  - "GACEI-03 局部攻擊抽象論 v0.1"
  - "GACEI-04 對抗記憶基底 v0.1"
---

# GACEI-05｜全域攻擊組合代數
## 依賴、干涉、遮蔽與協同失敗

**英文題名：** Algebra of Global Attack Composition: Dependency, Interference, Masking, and Synergistic Failure

---

## 摘要

GACEI-01 至 GACEI-04 依序建立了全域對抗計算、MSSP 對抗對偶、局部攻擊抽象與 SEDB-style 對抗記憶。到此為止，系統已能保存一組具有前提、目標不變量、擾動、觀測、驗證、恢復、成本與 provenance 的 attack operators。然而，真正的全域對抗計算仍缺少一個核心層：**局部 attack 到底何時可以組合？組合之後，原本的 attack semantics、觀測語義與診斷能力是否仍然成立？**

本文提出「全域攻擊組合代數」（Algebra of Global Attack Composition, AGAC）作為第一版 operational composition calculus。本文使用「代數」一詞，表示我們研究 attack operators 的組合、關係、等價、衝突、部分封閉與可重寫規則；本文**不預設**所有 attack operators 構成群、環、域、半群、格或任何單一既有代數結構，也不預設所有組合都具有結合律或交換律。

令授權測試系統的狀態空間為：

$$
\mathcal X,
$$

局部 attack operator 為部分狀態轉換：

$$
T_a:
\mathcal X
\rightharpoonup
\mathcal X,
$$

其適用前提為：

$$
P_a:
\mathcal X
\rightarrow
\{0,1\},
$$

觀測器為：

$$
O_a:
\mathcal X\times\mathcal X
\rightarrow
\mathcal Z_a,
$$

驗證器為：

$$
V_a:
\mathcal Z_a
\rightarrow
\{
\mathrm{Accept},
\mathrm{Reject},
\mathrm{Unknown},
\mathrm{NotMeasured}
\}.
$$

因此一個 attack 的完整執行語義不是只有：

$$
x\mapsto x',
$$

而是：

$$
\boxed{
\llbracket a\rrbracket_\theta(x)
=
\left(
x',
z,
v,
h
\right),
}
$$

其中 $\theta$ 為版本、平台、權限、資源、baseline 與 sandbox 條件， $z$ 為觀測， $v$ 為判定， $h$ 為執行 provenance。

本文首先提出六類基本關係：

$$
a\parallel b
$$

表示可獨立並行；

$$
a\prec b
$$

表示有序依賴；

$$
a\# b
$$

表示組合衝突；

$$
a\triangleright b
$$

表示 $a$ 遮蔽 $b$ 的可觀測效果；

$$
a\odot b
$$

表示存在協同 failure；

$$
a\leadsto b
$$

表示 $a$ 會改變 $b$ 的適用域、狀態或觀測條件。

但本文進一步指出，這六種關係本身還不足以構成全域 attack。真正的組合必須滿足一組「組合可接受條件」：

$$
\boxed{
\mathsf{Composable}(a,b\mid\theta)
}
$$

至少同時考慮：

1. authorization compatibility；
2. precondition satisfiability；
3. baseline consistency；
4. sandbox / recovery compatibility；
5. semantic target compatibility；
6. observation separability；
7. diagnosability preservation；
8. cost feasibility；
9. non-destructive campaign boundedness。

只有：

$$
\mathsf{Composable}(a,b\mid\theta)=1
$$

時，系統才應把 $a,b$ 放入同一 global campaign 的直接組合關係。

本文定義第一版組合算子：

$$
a\circ b
$$

為序列組合；

$$
a\otimes b
$$

為隔離並行組合；

$$
a\oplus b
$$

為條件分支／替代組合；

$$
a\odot b
$$

為協同組合；

$$
a\blacktriangleright b
$$

為具有已知遮蔽語義的受控組合；

$$
[a]_R
$$

為在 restore / snapshot 邊界 $R$ 下執行的 attack。

本文強調：

$$
\boxed{
a\circ b
\neq
b\circ a
}
$$

一般成立；

而：

$$
\boxed{
(a\circ b)\circ c
=
a\circ(b\circ c)
}
$$

也不能無條件假設，因為 observation window、timeout、snapshot、recovery、version binding 與 intermediate evidence 都可能使不同分組具有不同語義。因此 AGAC 是一套**條件化、部分定義、帶觀測的組合演算**。

本文進一步定義「協同失敗」：

$$
\boxed{
V(a)=\mathrm{Accept},
\qquad
V(b)=\mathrm{Accept},
\qquad
V(a\odot b)=\mathrm{Reject}.
}
$$

這描述一類非常重要的全域缺陷：每個局部 component 在單獨擾動下都能維持 contract，但多個局部狀態、時間或依賴擾動組合後，系統才跨越 failure threshold。此類 interaction defect 正是逐局部攻擊最容易漏掉、而全域 campaign 最有價值的地方之一。

本文同時提出「遮蔽失敗」與「診斷崩潰」。如果：

$$
a\triangleright b,
$$

且執行 $a$ 後導致 $b$ 的有效 observation 消失，則 $a,b$ 不應被簡單同批執行，除非 campaign 明確設計：

- separate sandbox；
- staged observation；
- replay；
- snapshot restore；
- counterfactual slice；

以恢復可辨識性。本文把此要求稱為：

$$
\boxed{
\text{Diagnosability Preservation}.
}
$$

真正的 global attack 不是「最大化同時破壞」，而是：

$$
\boxed{
\text{Maximize meaningful interaction coverage while preserving causal interpretability.}
}
$$

本文最後把 attack composition 建模成帶型別的 interaction hypergraph：

$$
\mathcal H_A
=
\left(
A,
\mathcal E,
\lambda,
\Theta,
W
\right),
$$

其中 $\mathcal E$ 可連接兩個或多個 attack， $\lambda$ 表示 relation type， $\Theta$ 表示條件纖維， $W$ 表示成本、風險、覆蓋與資訊增益。全域 campaign synthesis 於是被轉換成一個受限 hypergraph selection / scheduling problem：

$$
\boxed{
\mathcal C^\ast
=
\operatorname{Compile}
(
\mathcal H_A,
B,
\tau,
Auth,
Diag
).
}
$$

本文為 GACEI-06 的「全域攻擊壓縮」建立必要前置：只有先知道局部 attack 如何合法組合，才能進一步問如何用最少組合覆蓋最大對抗空間。

**關鍵詞：** Attack Composition、Attack Algebra、Interaction Hypergraph、Synergistic Failure、Masking、Diagnosability、Sequential Composition、Parallel Composition、MSSP、Global Campaign、全域對抗計算、AI 工程智能

---

# 0. 研究定位、安全範圍與「代數」聲明

本文中的所有 attack composition 只適用於：

- 授權軟體；
- synthetic system；
- isolated copy；
- sandbox；
- 可恢復 testbed；
- 內部工程驗證。

本文不描述如何把局部攻擊鏈組合成對第三方真實系統的未授權滲透流程。

---

## 0.1 這不是傳統滲透鏈條教學

本文研究：

$$
\boxed{
\text{Software Adversarial Test Composition}.
}
$$

而不是：

$$
\boxed{
\text{Operational Intrusion Chaining}.
}
$$

其核心目標是：

- 降低測試計算成本；
- 找 interaction defect；
- 保留可診斷性；
- 建立 AI 全域工程理解 benchmark。

---

## 0.2 「代數」是 operational calculus

本文稱：

$$
\mathcal A
$$

為 attack operator space。

但不宣稱：

$$
(\mathcal A,\circ)
$$

一定構成 semigroup。

更不宣稱：

$$
(\mathcal A,+,\cdot)
$$

構成 ring。

本文只研究：

> 哪些 operators 可組合、在哪些條件下可組合、組合後有哪些語義、哪些等式成立、哪些等式不能假設。

---

# 1. Attack 不是只有 Mutation

GACEI-03 已定義：

$$
a
=
(P,T,I,O,V,R,C,K,H).
$$

本文為組合方便，將其分成四層：

$$
\boxed{
a
=
\left(
\mathsf{Sem}_a,
\mathsf{Exec}_a,
\mathsf{Obs}_a,
\mathsf{Gov}_a
\right).
}
$$

---

## 1.1 Semantic Layer

$$
\mathsf{Sem}_a
=
(P_a,I_a,\Theta_a).
$$

回答：

- 何時適用？
- 在測什麼？
- 對哪些條件成立？

---

## 1.2 Execution Layer

$$
\mathsf{Exec}_a
=
(T_a,R_a).
$$

回答：

- 如何擾動？
- 如何恢復？

---

## 1.3 Observation Layer

$$
\mathsf{Obs}_a
=
(O_a,V_a).
$$

回答：

- 看什麼？
- 如何判斷？

---

## 1.4 Governance Layer

$$
\mathsf{Gov}_a
=
(C_a,K_a,H_a,Auth_a).
$$

回答：

- 覆蓋什麼？
- 成本多少？
- 來源是什麼？
- 是否被授權？

---

# 2. Attack 的帶觀測執行語義

給定：

$$
x\in\mathcal X
$$

與：

$$
\theta\in\Theta,
$$

若：

$$
P_a(x,\theta)=1,
$$

則 attack 執行：

$$
T_a(x)=x'.
$$

再觀測：

$$
z_a
=
O_a(x,x',\theta).
$$

判定：

$$
v_a
=
V_a(z_a,\theta).
$$

所以：

$$
\boxed{
\llbracket a\rrbracket_\theta(x)
=
(x',z_a,v_a,h_a).
}
$$

如果：

$$
P_a(x,\theta)=0,
$$

則：

$$
\llbracket a\rrbracket_\theta(x)
=
\mathrm{NotApplicable}.
$$

---

# 3. 為什麼 Attack Composition 不是函數合成那麼簡單？

如果只看：

$$
T_a,
T_b,
$$

當然可以問：

$$
T_b\circ T_a.
$$

但完整 attack 還有：

- precondition；
- observation；
- validator；
- recovery；
- cost；
- authorization；
- provenance。

因此：

$$
\boxed{
T_b\circ T_a
\text{ exists}
}
$$

不代表：

$$
\boxed{
a\circ b
\text{ is a valid adversarial composition}.
}
$$

---

# 4. Sequential Composition

本文定義：

$$
\boxed{
a\circ b
}
$$

表示：

> 先執行 $a$，保留或轉換其結果，再讓 $b$ 在 $a$ 的 post-state 上執行。

注意本文採語義：

$$
a\circ b
=
\text{$a$ then $b$}.
$$

這與部分數學領域的函數記號方向不同，因此本文全文以此定義為準。

---

## 4.1 Sequential precondition

要求：

$$
P_a(x)=1
$$

且：

$$
P_b(T_a(x))=1.
$$

因此：

$$
\boxed{
P_{a\circ b}(x)
=
P_a(x)
\land
P_b(T_a(x)).
}
$$

---

## 4.2 Sequential evidence

組合 evidence：

$$
E_{a\circ b}
=
(E_a,E_b,E_{ab}^{\mathrm{interaction}}).
$$

不能只保存最終：

$$
E_b.
$$

因為：

$$
E_a
$$

可能是定位根因的必要中間證據。

---

# 5. Parallel Composition

本文定義：

$$
\boxed{
a\otimes b
}
$$

為「隔離並行」或「可證明安全的並行」。

它不是：

> 兩個 attack 同時 start 就算。

---

## 5.1 最安全形式

使用兩個共享 baseline 的隔離 sandbox：

$$
S_a
\cong
S_b
\cong
S^\ast.
$$

然後：

$$
a(S_a),
\qquad
b(S_b).
$$

這叫：

$$
\boxed{
\text{Baseline-Equivalent Parallelism}.
}
$$

---

## 5.2 同一 runtime 並行

若真的同一 runtime：

$$
a,b
$$

並行，

至少要求：

$$
\operatorname{WriteSet}(a)
\cap
\operatorname{WriteSet}(b)
=
\varnothing
$$

或存在明確 synchronization semantics。

否則不是 independent parallel，而是 interaction attack。

---

# 6. Alternative / Branch Composition

定義：

$$
\boxed{
a\oplus b
}
$$

表示：

> 根據條件、觀測或 budget 選擇 $a$ 或 $b$。

例如：

$$
a\oplus_\phi b
=
\begin{cases}
a,&\phi=1,\\
b,&\phi=0.
\end{cases}
$$

這對 adaptive global campaign 很重要。

---

# 7. Synergistic Composition

定義：

$$
\boxed{
a\odot b
}
$$

表示：

> 組合的研究目的就是測 $a,b$ 的交互效應，而非把它們當成獨立 attack。

---

## 7.1 最典型形式

$$
V(a)=\mathrm{Accept},
$$

$$
V(b)=\mathrm{Accept},
$$

但：

$$
V(a\odot b)=\mathrm{Reject}.
$$

---

## 7.2 Interaction defect

定義：

$$
\boxed{
F_{\mathrm{syn}}(a,b)
=
1
}
$$

若：

$$
\neg F(a)
\land
\neg F(b)
\land
F(a,b).
$$

這表示 failure 不能由任何單一 attack 的局部效果充分解釋。

---

# 8. Dependency

定義：

$$
\boxed{
a\prec b
}
$$

若 $b$ 的成立需要：

$$
Post(a).
$$

這不是 attack severity 關係。

而是：

$$
\boxed{
\text{Execution Dependency}.
}
$$

---

## 8.1 Dependency DAG

若：

$$
\prec
$$

在一個 campaign subset 上無 cycle，

可形成 DAG：

$$
G_D.
$$

---

## 8.2 Cycle

若：

$$
a\prec b,
$$

$$
b\prec a,
$$

則：

$$
\boxed{
\text{Unsatisfied Circular Dependency}
}
$$

除非存在：

- fixed point；
- staged state；
- external initializer。

否則 campaign compiler 應拒絕。

---

# 9. Conflict

定義：

$$
\boxed{
a\# b
}
$$

若：

$$
a,b
$$

在同一 execution context 中不能同時保持 intended semantics。

---

## 9.1 Precondition conflict

例如：

$$
Post(a)
\models
\neg P_b.
$$

---

## 9.2 Recovery conflict

$$
R_a
$$

會清除：

$$
b
$$

需要的 state。

---

## 9.3 Validator conflict

$$
a
$$

改變：

$$
O_b
$$

的 observation substrate。

---

# 10. Masking

定義：

$$
\boxed{
a\triangleright b
}
$$

若：

$$
Signal_b
$$

在：

$$
a
$$

存在後變得不可辨識或不可歸因。

---

## 10.1 完全遮蔽

$$
I(Signal_b;Observation\mid a)
\approx0.
$$

這裡 $I$ 只表示資訊性直覺，不宣稱所有實作都必須以 Shannon mutual information 計算。

---

## 10.2 部分遮蔽

 $b$ 的 signal 仍存在，但：

$$
SNR_b
\downarrow.
$$

---

# 11. Masking 不等於 Conflict

若：

$$
a\triangleright b,
$$

兩者仍可能物理上可一起執行。

但：

$$
\boxed{
\text{Executable Together}
\neq
\text{Diagnosable Together}.
}
$$

這是 GAC 很重要的區分。

---

# 12. Influence

定義：

$$
\boxed{
a\leadsto b
}
$$

表示：

> $a$ 會改變 $b$ 的 applicability、cost、observation、validator 或 effect distribution。

它比：

$$
a\prec b
$$

更一般。

---

# 13. Composition Acceptability

本文定義：

$$
\boxed{
\mathsf{Composable}(a,b\mid\theta).
}
$$

第一版：

$$
\mathsf{Composable}
=
A
\land
P
\land
B
\land
R
\land
S
\land
O
\land
D
\land
C.
$$

其中：

- $A$：authorization compatible；
- $P$：preconditions satisfiable；
- $B$：baseline compatible；
- $R$：recovery compatible；
- $S$：semantic target meaningful；
- $O$：observation plan valid；
- $D$：diagnosability acceptable；
- $C$：cost feasible。

---

# 14. Authorization Compatibility

若：

$$
Auth(a)=1,
$$

$$
Auth(b)=1,
$$

也不能直接推出：

$$
Auth(a\odot b)=1.
$$

因為組合可能擴大：

- resource use；
- scope；
- data exposure；
- state mutation。

所以：

$$
\boxed{
Auth(a)
\land
Auth(b)
\not\Rightarrow
Auth(a\star b).
}
$$

---

# 15. Baseline Compatibility

兩個 attack 若不是作用於同一：

$$
baseline
$$

或可證明等價 snapshot，

不能直接合成同一 global observation。

---

## 15.1 Baseline identity

$$
BID
=
Hash
(
source,
build,
config,
fixture,
architecture,
validator
).
$$

---

# 16. Recovery Compatibility

若：

$$
a
$$

後：

$$
R_a
$$

會：

- destroy sandbox；
- reset state；
- invalidate $b$ ；

則：

$$
a\circ b
$$

可能無定義。

---

# 17. Semantic Target Compatibility

如果：

$$
a
$$

與：

$$
b
$$

測完全無關的 system slices，

組合仍可能合法，

但：

$$
\operatorname{InfoGain}(a\odot b)
$$

可能沒有額外價值。

因此：

$$
\boxed{
\text{Composable}
\neq
\text{Worth Composing}.
}
$$

---

# 18. Diagnosability Preservation

本文定義：

$$
\boxed{
D(a,b)
}
$$

表示：

> 組合後仍能把主要失敗證據合理投影到 attack / structure candidates。

---

## 18.1 最低條件

若：

$$
F(a,b)=1,
$$

但無法判斷：

- $a$ ；
- $b$ ；
- interaction；
- harness；

哪個是原因，

則：

$$
D(a,b)
$$

低。

---

## 18.2 診斷崩潰

定義：

$$
\boxed{
\text{Diagnostic Collapse}
}
$$

當：

$$
\operatorname{FailureDetected}=1
$$

但：

$$
\operatorname{LocalizationInformation}
\approx0.
$$

---

# 19. Global Attack 不是最大破壞

所以全域 campaign 的目標不是：

$$
\max
\operatorname{Damage}.
$$

而是：

$$
\boxed{
\max
\left(
\operatorname{Coverage}
+
\operatorname{InfoGain}
+
\operatorname{InteractionDiscovery}
\right)
}
$$

subject to：

$$
\operatorname{Safety}=1,
$$

$$
\operatorname{Diagnosability}\ge\tau_D,
$$

$$
\operatorname{Cost}\le B.
$$

---

# 20. Snapshot-Bounded Composition

定義：

$$
\boxed{
[a]_R
}
$$

表示：

> 在 snapshot / restore boundary $R$ 內執行 $a$。

因此：

$$
[a]_R\otimes[b]_R
$$

可以保證兩個 attack 都從等價 baseline 開始。

---

# 21. Replay-Bounded Composition

若：

$$
a\triangleright b,
$$

可改為：

$$
[a]_R
\rightarrow
\text{restore}
\rightarrow
[b]_R
$$

再：

$$
[a\odot b]_R
$$

第三次執行 interaction。

這形成三段證據：

$$
E_a,
E_b,
E_{ab}.
$$

---

# 22. A/B/AB 三元比較

對 synergy 特別重要：

$$
O_A,
O_B,
O_{AB}.
$$

定義 interaction residual：

$$
\Delta_{AB}
=
O_{AB}
-
\widehat F(O_A,O_B).
$$

其中：

$$
\widehat F
$$

是「若兩者只是獨立效果，預期組合結果」。

若：

$$
\Delta_{AB}
$$

顯著，

表示存在 interaction effect。

---

# 23. 不要求線性可加

通常：

$$
O_{AB}
\neq
O_A+O_B.
$$

因此：

$$
\boxed{
\text{Attack Effect}
\text{ need not be additive}.
}
$$

---

# 24. Non-Commutativity

一般：

$$
\boxed{
a\circ b
\neq
b\circ a.
}
$$

原因可能包括：

- state mutation；
- cache；
- retry；
- lifecycle；
- version；
- timeout；
- recovery；
- observation window。

---

# 25. Conditional Commutativity

若：

$$
a\parallel b
$$

且：

$$
ReadWriteIndependent(a,b)=1,
$$

$$
ObservationIndependent(a,b)=1,
$$

則可以有：

$$
a\circ b
\equiv_\theta
b\circ a.
$$

注意是：

$$
\equiv_\theta
$$

條件化等價，不是 bytes identical。

---

# 26. Associativity 不能預設

若只看 pure state transform：

$$
T_c(T_b(T_a(x))),
$$

分組看似相同。

但 attack evidence 可能不同。

例如：

$$
(a\circ b)\circ c
$$

可能先生成：

$$
E_{ab},
$$

再進入 $c$ ；

而：

$$
a\circ(b\circ c)
$$

可能使用不同 observation boundary。

因此：

$$
\boxed{
(a\circ b)\circ c
\not\equiv
a\circ(b\circ c)
}
$$

一般不能預設。

---

# 27. Evidence-Sensitive Associativity

若：

1. state transition equivalent；
2. intermediate evidence preserved；
3. observation windows equivalent；
4. recovery semantics equivalent；
5. timeout semantics equivalent；

才可以宣告：

$$
(a\circ b)\circ c
\equiv_E
a\circ(b\circ c).
$$

---

# 28. Identity Attack

可以定義：

$$
\mathbf 1
$$

為 no-op control。

要求：

$$
T_{\mathbf 1}(x)=x.
$$

若 observation contract 相容，可有：

$$
\mathbf 1\circ a
\equiv
a,
$$

$$
a\circ\mathbf 1
\equiv
a.
$$

但：

$$
\mathbf 1
$$

仍可能有測量成本。

---

# 29. Null / Invalid Attack

定義：

$$
\bot_A
$$

為：

- unauthorized；
- unsatisfied precondition；
- invalid validator；
- impossible recovery；

等無法進入 campaign 的 attack。

---

# 30. Attack Hypergraph

Pairwise graph 不足以表示：

$$
a\odot b\odot c.
$$

因此：

$$
\boxed{
\mathcal H_A
=
(A,\mathcal E,\lambda,\Theta,W).
}
$$

---

## 30.1 Hyperedge

$$
e
=
\{a_1,\ldots,a_k\}.
$$

relation type：

$$
\lambda(e)
\in
\{
INDEPENDENT,
ORDERED,
CONFLICT,
MASKING,
SYNERGY,
DEPENDENCY,
INFLUENCE
\}.
$$

---

# 31. Conditional Hyperedge

同一組 attack 在不同：

$$
\theta
$$

可以具有不同 relation。

例如：

$$
a\parallel b
$$

在 Linux，

但：

$$
a\# b
$$

在 Windows-specific runtime。

因此：

$$
\boxed{
Relation(a,b)
=
Relation(a,b\mid\theta).
}
$$

---

# 32. Hypergraph 也是可學習知識

如果歷史上反覆觀察：

$$
a\odot b
$$

具有 synergy，

這不是一次 campaign detail。

它可以被 promotion 成：

$$
\boxed{
\text{Attack Interaction Knowledge}.
}
$$

未來存入 AMS。

---

# 33. Attack Interaction Memory

GACEI-04 的 relation graph 因此需要保存：

```text
REQUIRES
CONFLICTS
MASKS
SYNERGIZES_WITH
INFLUENCES
COMMUTES_UNDER
NONCOMMUTES_UNDER
```

並綁定：

$$
\theta.
$$

---

# 34. Composition Closure

給定 attack family：

$$
F.
$$

若：

$$
a,b\in F
$$

不能保證：

$$
a\circ b\in F.
$$

所以：

$$
\boxed{
\text{Attack Family}
\text{ need not be composition-closed}.
}
$$

---

# 35. Composition Can Create New Family

例如：

$$
a\in F_{\mathrm{state}},
$$

$$
b\in F_{\mathrm{temporal}},
$$

但：

$$
a\odot b
\in
F_{\mathrm{state-temporal-interaction}}.
$$

這可以形成新 family proposal。

---

# 36. Composite Attack Identity

定義：

$$
ID(a\star b)
$$

不能只 hash：

$$
ID(a)+ID(b).
$$

還要包含：

- operator；
- ordering；
- condition；
- snapshot boundary；
- observation contract。

因此：

$$
ID_{\mathrm{comp}}
=
Hash
(
ID_a,
ID_b,
\star,
\theta,
R,
O
).
$$

---

# 37. Equivalent Composite Campaign

兩個 composite：

$$
c_1,c_2
$$

即使 script 不同，

若：

- target invariants equivalent；
- state transition equivalent；
- observation equivalent；
- validator equivalent；
- recovery equivalent；

可以：

$$
c_1
\equiv_{\theta,I,O}
c_2.
$$

---

# 38. Campaign DAG

若所有 non-parallel dependencies 可形成 partial order：

$$
\prec,
$$

可建立：

$$
G_C
=
(A_C,E_C).
$$

---

# 39. Topological Schedule

若：

$$
G_C
$$

acyclic，

可以：

$$
\operatorname{TopoSort}(G_C)
$$

形成可執行 schedule。

---

# 40. Parallel Antichain

在 partial order 中，antichain：

$$
\mathcal A_{\parallel}
$$

可作 parallel candidate。

但仍需檢查：

$$
\#
$$

與：

$$
\triangleright.
$$

---

# 41. Interference Matrix

對：

$$
n
$$

個 attacks，

可以建立稀疏：

$$
M_I
\in
\mathbb R^{n\times n}.
$$

元素：

$$
M_{ij}
$$

描述：

- 0：unknown / none；
- positive：synergy；
- negative：conflict / masking；

但單一數值會丟 relation semantics。

因此實作上更適合：

$$
\boxed{
\text{Sparse Typed Relation Matrix}.
}
$$

---

# 42. Higher-Order Interaction

三個 attack：

$$
a,b,c
$$

可能：

$$
F(a,b)=0,
$$

$$
F(a,c)=0,
$$

$$
F(b,c)=0,
$$

但：

$$
F(a,b,c)=1.
$$

這表示：

$$
\boxed{
\text{Pairwise Coverage}
\neq
\text{Higher-Order Coverage}.
}
$$

---

# 43. 組合爆炸

若：

$$
n
$$

個 attack，

所有 subset：

$$
2^n.
$$

若考慮 ordering：

$$
\sum_{k=1}^{n}
{n\choose k}k!.
$$

所以不能 brute force。

---

# 44. Architecture-Induced Pruning

若 project architecture graph：

$$
G_S
$$

顯示：

$$
a
$$

與：

$$
b
$$

作用域沒有 causal path，

則：

$$
P_{\mathrm{synergy}}(a,b)
$$

可以降低。

這就是：

$$
\boxed{
\text{Architecture Understanding}
\rightarrow
\text{Composition-Space Compression}.
}
$$

---

# 45. Invariant-Induced Pruning

若：

$$
I_a
\cap
I_b
=
\varnothing
$$

且無 shared dependency，

可降低 interaction priority。

---

# 46. State-Induced Pruning

若：

$$
\operatorname{WriteSet}(a)
\cap
(\operatorname{ReadSet}(b)\cup \operatorname{WriteSet}(b))
=
\varnothing,
$$

且反向同樣成立，

可以提高：

$$
a\parallel b
$$

信心。

---

# 47. Observation-Induced Pruning

若：

$$
a
$$

與：

$$
b
$$

共享同一不可分離 signal channel，

則同時執行可能：

$$
D(a,b)\downarrow.
$$

因此應分 lane。

---

# 48. Campaign Lane

本文提出：

$$
\boxed{
\text{Lane}
}
$$

作為 global campaign 的執行分區。

不同 lane 可以：

- isolated parallel；
- ordered；
- interaction-specific；
- validator-specific。

---

# 49. 四種基礎 Lane

## L1：Independent Replay Lane

跑已知單 attack。

## L2：Pair Interaction Lane

跑：

$$
a\odot b.
$$

## L3：Higher-Order Lane

只跑高風險 hyperedge。

## L4：Diagnostic Lane

對 failure 做 counterfactual replay。

---

# 50. 全域 Campaign 不是單一大爆炸

因此：

$$
\boxed{
\text{Global}
\neq
\text{Everything Simultaneously}.
}
$$

真正 global：

$$
\boxed{
\text{One Global Plan}
+
\text{Coordinated Lanes}
+
\text{Shared Baseline Reference}
+
\text{Integrated Evidence}.
}
$$

---

# 51. Composition Safety

定義：

$$
SafeComp(c)
=
Auth(c)
\land
Sandbox(c)
\land
Bounded(c)
\land
Recoverable(c).
$$

---

# 52. Boundedness

一個 adaptive campaign 不應：

$$
\text{generate attack}
\rightarrow
\text{generate children}
\rightarrow
\infty.
$$

因此每個 composition plan 必須有：

- depth budget；
- compute budget；
- execution budget；
- wall-clock budget；
- novelty threshold。

---

# 53. Composition Cost

對 composite：

$$
c=a\star b,
$$

一般：

$$
K(c)
\neq
K(a)+K(b).
$$

因為可能有：

- shared setup savings；
- synchronization overhead；
- restore cost；
- extra diagnosis cost。

---

# 54. Synergy Value

定義：

$$
SV(a,b)
=
\operatorname{InfoGain}(a\odot b)
-
\operatorname{InfoGain}(a)
-
\operatorname{InfoGain}(b).
$$

若：

$$
SV>0,
$$

表示 interaction test 具有額外資訊價值。

---

# 55. Redundancy

若：

$$
a,b
$$

覆蓋幾乎相同 invariant / path，

且歷史結果高度重合，

可定義：

$$
Red(a,b)\uparrow.
$$

campaign compiler 可降低同時選取。

---

# 56. Composition Utility

本文提出：

$$
U(c)
=
\alpha Cov(c)
+
\beta IG(c)
+
\gamma Risk(c)
+
\delta Novel(c)
-
\eta Cost(c)
-
\mu Red(c)
-
\nu DiagLoss(c).
$$

---

# 57. Global Composition Optimization

因此：

$$
\boxed{
C^\ast
=
\arg\max_{C\in\mathfrak C}
U(C)
}
$$

subject to：

$$
Cost(C)\le B,
$$

$$
Auth(C)=1,
$$

$$
Diag(C)\ge\tau_D,
$$

$$
Coverage(C)\ge\tau_C.
$$

這是 GACEI-06 的直接前置。

---

# 58. MSSP 中的組合優勢

MSSP 顯式：

- ownership；
- boundary；
- dependency；
- state；

因此：

$$
\operatorname{ReadSet},
\operatorname{WriteSet},
I,
E
$$

相對容易推導。

這使：

$$
\mathsf{Composable}(a,b)
$$

比 spaghetti architecture 更容易估計。

---

# 59. MSSP 中的組合風險

同樣因為結構清楚，

AI 很容易枚舉：

$$
\neg I_i
$$

與它們的組合。

因此：

$$
N_{\mathrm{candidate\ comp}}
$$

可能迅速膨脹。

所以需要：

$$
\boxed{
\text{Composition Intelligence}
}
$$

而不是：

$$
\boxed{
\text{Composition Enthusiasm}.
}
$$

---

# 60. Attack Memory 對組合的作用

AMS 可以提供：

- known conflicts；
- known synergy；
- known masking；
- historical cost；
- transfer evidence。

因此 planner 不必每次重新學：

$$
Relation(a,b).
$$

---

# 61. Unknown Relation

若 AMS 沒資料：

$$
Relation(a,b)=UNKNOWN.
$$

不能：

$$
UNKNOWN
\rightarrow
INDEPENDENT.
$$

這是重要安全原則。

---

# 62. Unknown 的處理

可：

1. separate lane；
2. cheap probe；
3. static dependency analysis；
4. sandbox trial；
5. defer。

---

# 63. Composition Probe

對未知 pair：

$$
(a,b),
$$

先跑最小：

$$
Probe(a,b)
$$

只測：

- precondition compatibility；
- masking；
- shared state；
- validator collision。

若通過，再進 full interaction test。

---

# 64. AI 全域注意力在這裡測什麼？

AI 必須一次看見：

$$
G_S
+
H_A
+
I
+
X
+
O
+
B.
$$

不是只看單 attack。

---

# 65. 理解能力

AI 要判斷：

> 這兩個局部 attack 為什麼可能有交互？

這是 architecture understanding。

---

# 66. 解析能力

要拆出：

- shared state；
- shared boundary；
- ordering；
- validator；
- recovery。

---

# 67. 創造能力

AI 可能從：

$$
a,b
$$

生成以前沒見過的：

$$
a\odot b
$$

interaction hypothesis。

---

# 68. 生成能力

再把：

$$
a\odot b
$$

變成可執行 sandbox experiment。

---

# 69. 計算能力

在：

$$
2^n
$$

組合空間中剪枝、排序、分 lane。

---

# 70. 驗證能力

區分：

$$
\text{Local Fail}
$$

與：

$$
\text{Interaction Fail}.
$$

---

# 71. 定位能力

把：

$$
F(a,b)
$$

投影回：

- $a$ ；
- $b$ ；
- relation；
- boundary；
- shared state；
- validator。

---

# 72. 組合學習

若：

$$
a\odot b
$$

反覆產生同類 failure，

可抽象成：

$$
m_{ab}.
$$

再寫回 AMS。

---

# 73. Global Attack Grammar

本文提出第一版 grammar：

```text
Campaign :=
    Attack
  | Sequence(Campaign, Campaign)
  | Parallel(Campaign, Campaign)
  | Branch(Condition, Campaign, Campaign)
  | Interaction(AttackSet)
  | RestoreBoundary(Campaign)
  | DiagnosticReplay(Campaign)
```

---

# 74. Grammar 需要 Type Check

不是任意 AST 都可執行。

需要：

$$
TypeCheck(Campaign)=Pass.
$$

---

# 75. Campaign Type

可記錄：

$$
\tau_C
=
(
Baseline,
Auth,
StateDomain,
ObservationDomain,
RecoveryDomain,
Budget
).
$$

---

# 76. Type Error 例子

若：

$$
Sequence(a,b)
$$

但：

$$
PostType(a)
\not\models
PreType(b),
$$

則：

$$
TypeError.
$$

---

# 77. Interaction Type Error

如果：

$$
a\odot b
$$

沒有共同 observation window，

interaction claim 不可判定。

---

# 78. Diagnostic Type Error

若 composite 沒有：

- provenance；
- lane id；
- baseline id；

則：

$$
\Pi_{\mathrm{fail}}
$$

可能無法可靠執行。

---

# 79. Composition Normal Form

未來可以研究把 campaign rewrite 成 normal form。

第一版可嘗試：

$$
\boxed{
\text{Freeze}
\rightarrow
\text{Independent}
\rightarrow
\text{Interactions}
\rightarrow
\text{Diagnostics}
\rightarrow
\text{Restore}
}
$$

但本文不主張唯一 normal form。

---

# 80. Rewrite Rules

在條件成立時：

$$
a\otimes b
\Rightarrow
b\otimes a.
$$

若：

$$
a\parallel b.
$$

---

## 80.1 Sequence fusion

若：

$$
a\circ b
$$

反覆出現且 recovery / observation 可合併，

可：

$$
a\circ b
\Rightarrow
m_{ab}.
$$

---

## 80.2 Conflict split

若：

$$
a\# b,
$$

則：

$$
a\otimes b
\Rightarrow
[a]_R
\oplus_{\mathrm{lane}}
[b]_R.
$$

意思是拆 lane，而不是強行一起跑。

---

# 81. Mask split

若：

$$
a\triangleright b,
$$

則：

$$
a\odot b
$$

前應至少有：

$$
a,
b,
ab
$$

三組對照。

---

# 82. Synergy promotion

若：

$$
SV(a,b)\gg0,
$$

可提高該 hyperedge 的 future priority。

---

# 83. Evidence Provenance

每一個 composite execution：

$$
e_c
$$

至少綁：

- baseline；
- component attacks；
- operator；
- order；
- lane；
- snapshot；
- observation；
- validator；
- time；
- version。

---

# 84. Failure Attribution

對 composite：

$$
c,
$$

failure attribution 不應只輸出：

```text
failed = true
```

而應：

$$
Attribution(c)
=
\left(
A_{\mathrm{local}},
A_{\mathrm{interaction}},
A_{\mathrm{harness}},
U
\right).
$$

---

# 85. Interaction Attribution

例如：

$$
P(F\mid a)=0.05,
$$

$$
P(F\mid b)=0.03,
$$

$$
P(F\mid a,b)=0.8.
$$

這可以支持 interaction hypothesis，但不自動證明唯一因果機制。

---

# 86. Counterfactual Diagnostics

可以比較：

$$
F(a,b),
$$

$$
F(a,\neg b),
$$

$$
F(\neg a,b),
$$

$$
F(\neg a,\neg b).
$$

這是一種受控 factorial-style diagnostic。

---

# 87. Higher-Order Diagnostics

三 attack 可比較：

$$
2^3
$$

個 presence/absence cells。

但只對高風險 small subset 使用，避免組合爆炸。

---

# 88. 組合深度

定義：

$$
Depth(C).
$$

不是越深越好。

若：

$$
Depth(C)\uparrow,
$$

通常：

$$
DiagLoss(C)\uparrow
$$

與：

$$
Cost(C)\uparrow.
$$

---

# 89. 最小互動深度

若某 failure 需要：

$$
k
$$

個 attack 才出現，

定義：

$$
d_F=k.
$$

這可以作為：

$$
\boxed{
\text{Interaction Complexity}
}
$$

之一。

---

# 90. Attack Composition Complexity

可定義：

$$
\kappa(C)
=
f
(
|A_C|,
Depth(C),
Width(C),
HyperedgeOrder(C),
StateCoupling(C)
).
$$

---

# 91. Complexity 不等於價值

高：

$$
\kappa
$$

可能只是亂。

因此：

$$
\boxed{
\text{Complex Campaign}
\neq
\text{High-Value Campaign}.
}
$$

---

# 92. Local Attack Coverage 與 Interaction Coverage

分開：

$$
\rho_{\mathrm{local}},
$$

$$
\rho_{\mathrm{interaction}}.
$$

---

# 93. Pairwise Interaction Coverage

若候選 pair set：

$$
E_2,
$$

已測：

$$
T_2,
$$

則：

$$
\rho_2
=
\frac{|T_2|}{|E_2|}.
$$

但前提是：

$$
E_2
$$

分母有明確 reference frame。

---

# 94. Higher-Order Coverage

對：

$$
k\ge3,
$$

不能假裝要全部：

$$
{n\choose k}
$$

窮舉。

應採：

- architecture-guided；
- risk-guided；
- history-guided；
- novelty-guided。

---

# 95. Global Coverage Shape

因此 global coverage 至少包含：

$$
\boldsymbol\rho_G
=
(
\rho_{\mathrm{local}},
\rho_{\mathrm{pair}},
\rho_{\mathrm{higher}},
\rho_{\mathrm{path}},
\rho_{\mathrm{validator}},
\rho_{\mathrm{recovery}}
).
$$

---

# 96. 組合的停止規則

若新增 composite：

$$
c
$$

只增加：

$$
Redundancy
$$

而：

$$
\Delta Coverage
\approx0,
$$

$$
\Delta InfoGain
\approx0,
$$

則停止。

---

# 97. Marginal Composition Value

定義：

$$
MCV(c)
=
\frac{
\Delta Coverage(c)
+
\Delta InfoGain(c)
+
\Delta RiskResolution(c)
}{
Cost(c)+\epsilon
}.
$$

---

# 98. Shadow Price

若：

$$
MCV(c)
<
\lambda_B,
$$

則：

$$
c
\rightarrow
Defer.
$$

這直接接 AICTE。

---

# 99. 研究假說

## H1：Interaction-aware campaign 能發現 sequential-local 漏失缺陷

存在專案族，使：

$$
D_{\mathrm{interaction}}
>
D_{\mathrm{local-only}}.
$$

---

## H2：Diagnosability constraint 可降低無效紅燈

若 campaign optimization 加入：

$$
Diag(C)\ge\tau_D,
$$

則：

$$
N_{\mathrm{unattributable\ red}}
\downarrow.
$$

---

## H3：Architecture-guided pruning 可降低組合空間

相較 uniform pairwise enumeration：

$$
C_{\mathrm{arch-pruned}}
<
C_{\mathrm{uniform}}
$$

且 defect recall 不顯著下降。

---

## H4：Attack interaction memory 可降低未來 composition discovery 成本

若 AMS 已保存：

$$
SYNERGIZES_WITH,
MASKS,
CONFLICTS,
$$

則：

$$
C_{\mathrm{relation-discovery}}
\downarrow.
$$

---

## H5：過深 composite 會降低可診斷性

在部分系統：

$$
Depth(C)\uparrow
\Rightarrow
Diag(C)\downarrow.
$$

因此全域不等於無限深。

---

# 100. Benchmark 設計

建立 synthetic systems，故意注入：

1. pure local defect；
2. pair synergy defect；
3. three-way defect；
4. masking case；
5. conflict case；
6. recovery interference；
7. validator collision。

比較三種 AI：

### A：Local-only

逐 attack。

### B：Naive Batch

很多 attack 一起跑。

### C：AGAC-aware

先建立 interaction graph，再編譯 campaign。

測：

$$
\text{Defect Recall},
$$

$$
\text{Interaction Recall},
$$

$$
\text{Unattributable Red},
$$

$$
\text{Compute Cost},
$$

$$
\text{Time-to-Diagnosis},
$$

$$
\text{False Positive},
$$

$$
\text{Campaign Size}.
$$

---

# 101. 本文非主張

本文不主張：

1. attack operators 構成群、環、域或 complete algebra；
2. sequence composition 一定具結合律；
3. parallel composition 一定具交換律；
4. 所有 pairwise independent 都代表 higher-order independent；
5. 所有組合 effect 都線性可加；
6. 所有 attack interaction 都能用單一數值表示；
7. 所有 unknown relation 都可視為 independent；
8. 所有可執行組合都值得執行；
9. global attack 等於所有 attack 同時執行；
10. synergy 越多越好；
11. campaign 越深越好；
12. 全域 attack 應最大化破壞程度；
13. diagnostics 可以完全自動找到唯一 root cause；
14. attack composition 應脫離 authorization boundary；
15. interaction hypergraph 必然存在唯一最優 campaign；
16. 本文可以取代正式軟體測試、model checking、fuzzing、故障注入或安全工程。

本文主張的是：

$$
\boxed{
\text{局部 attack 的組合必須有條件、有型別、有觀測、有恢復、有診斷語義。}
}
$$

以及：

$$
\boxed{
\text{Globality comes from coordinated structural composition, not from attack count.}
}
$$

---

# 102. 與 GACEI-01 至 04 的關係

GACEI-01：

$$
\text{為什麼要全域 attack？}
$$

GACEI-02：

$$
\text{MSSP 如何把 global failure 投影回 local responsibility？}
$$

GACEI-03：

$$
\text{局部 attack 如何抽象成 reusable operator？}
$$

GACEI-04：

$$
\text{這些 operator 如何被長期記憶？}
$$

本文：

$$
\boxed{
\text{這些 remembered operators 如何合法組合？}
}
$$

---

# 103. 下一篇：全域攻擊壓縮

GACEI-06 將回答：

> 已知 attack 與其 interaction graph 都存在後，怎麼選最少的一組，取得最大的有效全域覆蓋？

核心將研究：

$$
\boxed{
\text{Attack Set Cover}
+
\text{Interaction Cover}
+
\text{Risk Weight}
+
\text{Information Gain}
+
\text{Compute Budget}.
}
$$

以及：

$$
\boxed{
\text{Global Adversarial Compression}.
}
$$

---

# 104. 結論

局部 attack 可以被抽象、被記憶，仍不代表它們可以任意拼接。

真正的問題是：

$$
\boxed{
\text{When does composition preserve meaning?}
}
$$

如果：

$$
a
$$

與：

$$
b
$$

一起執行後：

- precondition 失效；
- validator 失真；
- evidence 被遮蔽；
- recovery 崩潰；
- baseline 不一致；
- root cause 無法定位；

那麼：

$$
a+b
$$

不是高品質 global attack。

它只是：

$$
\boxed{
\text{Adversarial Noise}.
}
$$

本文因此提出：

$$
\boxed{
\mathsf{Composable}(a,b\mid\theta)
}
$$

作為所有 attack combination 的基本 gate。

只有通過：

$$
\text{Authorization}
+
\text{Precondition}
+
\text{Baseline}
+
\text{Recovery}
+
\text{Semantic Target}
+
\text{Observation}
+
\text{Diagnosability}
+
\text{Cost}
$$

的 attack 組合，才應進入 global campaign。

因此真正的全域攻擊不是：

> 一口氣把所有東西都弄壞。

而是：

> **在共同 baseline 與有限資源下，選擇一組具有結構意義的局部擾動，安排其並行、順序、隔離與交互，使系統暴露最多有價值的 failure behavior，同時仍能知道為什麼紅、紅在哪裡、哪些 attack 彼此造成了什麼。**

其核心式可壓縮為：

$$
\boxed{
\text{Local Operators}
+
\text{Typed Interactions}
+
\text{Bounded Scheduling}
+
\text{Preserved Diagnosability}
=
\text{Global Adversarial Composition}.
}
$$

這才是大量局部攻擊真正轉化成全域攻擊的第一個演算法基礎。

---

## Canonical Source Note

本文件之正式原稿為 UTF-8 Markdown。

所有數學原始碼僅使用：

- inline：` $...$ `
- display：`$$...$$`

不以 Unicode 數學字元替代 LaTeX source，不進行 unicode-escape round-trip，不將聊天渲染畫面視為 canonical source。
