# 空間域證明包圍論 II
## 路徑域完備性與表示非坍縮
### Spatial-Domain Proof Enclosure II: Route-Domain Completeness and Representation Non-Collapse

**Version:** v0.1  
**Date:** 2026-08-14  
**Status:** theorem-style foundational formalization; not a claim of a complete proof calculus  
**Canonical source:** UTF-8 Markdown; canonical mathematics uses ` $...$ ` and `$$...$$` only.

---

## 摘要

《空間域證明包圍論 I》將全域命題

$$
C:\forall d\in D,\;P(d)
$$

改寫為對真實反例集合

$$
\mathcal C
=
\{d\in D:\neg P(d)\}
$$

的可靠上包絡收縮：在研究表示域 $X$ 中維持 survivor envelope $\Omega_t$，並要求永久保持

$$
\mathcal C_X\subseteq\Omega_t.
$$

然而，這個框架最先可能失敗的地方不是 theorem cut，而是**研究表示本身**。實際研究往往使用

$$
\phi:D\to X
$$

將原始問題轉為 parity code、symbolic itinerary、lattice coordinate、graph quotient、abstract state、proof state、幾何投影或其他中介表示。若 $\phi$ 遺失 proof-relevant distinctions，後續即使在 $X$ 中得到極漂亮的空集合結論，也可能只證明「某個錯誤投影已空」，而非原命題無反例。

本文形式化 SDPE 的第二個地基：**Route-Domain Completeness / Representation Non-Collapse**。

首先，任意表示 $\phi:D\to X$ 自然誘導 powerset 層的 abstraction / concretization：

$$
\alpha_\phi(A)=\phi(A),
\qquad
\gamma_\phi(B)=\phi^{-1}(B).
$$

本文證明

$$
\boxed{
\alpha_\phi(A)\subseteq B
\iff
A\subseteq\gamma_\phi(B),
}
$$

因此 $(\alpha_\phi,\gamma_\phi)$ 構成一個 Galois connection。其 concrete-side closure

$$
\operatorname{Sat}_\phi(A)
:=
\gamma_\phi\alpha_\phi(A)
=
\phi^{-1}(\phi(A))
$$

正是「沿表示 fiber 做飽和」的操作。這揭示 representation compression 的核心代價：一旦只在 $X$ 中推理，任何 concrete set 的精確可表示性取決於它是否為 fiber-saturated。

本文進一步證明**表示可定義性等價定理**：對任意 $A\subseteq D$，下列條件等價：

1. $A=\operatorname{Sat}_\phi(A)$ ；
2. 存在 $B\subseteq\phi(D)$ 使 $A=\phi^{-1}(B)$ ；
3. $A$ 的 membership 在每個 $\phi$ -fiber 上保持常數。

因此，若要將 $P$ 精確下降為 quotient predicate $P_X$，必要且充分條件不是 $\phi$ injective，而是

$$
\boxed{
\phi(d_1)=\phi(d_2)
\Longrightarrow
P(d_1)=P(d_2).
}
$$

為處理長時間數學研究不只依賴一個 predicate 的情形，本文引入 proof-relevant predicate family $\Sigma$ 、fiber signature $\sigma_\Sigma$ 與 **proof-relevant fiber multiplicity**

$$
\boxed{
m_\Sigma(x)
:=
\left|
\{\sigma_\Sigma(d):d\in\phi^{-1}(x)\}
\right|.
}
$$

當 $m_\Sigma(x)>1$ 時， $x$ 為 representation-singular fiber：表示把對後續證明有不同意義的 concrete states 壓成同一抽象點。

本文強調一項關鍵 no-go：

$$
\boxed{
\text{representation non-collapse}
\neq
\text{global injectivity}.
}
$$

粗表示仍可完全 sound，只要 mixed fibers 不被錯誤排除。本文因此區分兩條合法策略：

- **Exact-Quotient Strategy**：要求 proof-relevant predicates 在 fiber 上同質；
- **Conservative-Envelope Strategy**：允許 mixed fibers，但將其保留為 unknown / survivor，除非存在整個 fiber 的 concrete exclusion certificate。

本文證明 Fiber-Safe Exclusion Theorem、Mixed-Fiber Obstruction、Refinement Monotonicity、Predicate Factorization、Operator-Soundness / Completeness 區分，以及 Multi-Chart Route-Atlas Closure Theorem。對動態問題，本文進一步指出 pointwise predicate preservation 不足；若 theorem cut 依賴可達性、迭代、固定點或時序語義，則需要對相關 operator 的 sound abstraction，甚至 strong preservation / completeness。

最終，本文把「走對路徑域」拆成可稽核的六項義務：**coverage、fiber adequacy、cut liftability、operator preservation、boundary ownership、certificate replayability**。任何表示轉換、降維、投影、商化、壓縮、幾何快速通道，都必須攜帶 Route Representation Contract，而不能只宣稱「新表示比較簡單」。

本文的結論是：SDPE 的 global closure 並不要求研究表示完美無損，而要求**所有損失都被顯式型別化，所有 mixed fibers 都不能被靜默刪除，所有 abstract exclusions 都能安全 lift 回 concrete domain**。

---

## 關鍵詞

空間域證明包圍；route-domain completeness；representation non-collapse；fiber；Galois connection；abstract interpretation；strong preservation；CEGAR；projection；quotient；proof-relevant signature；representation singularity；refinement；global proof

---

# 1. 問題：如果一開始走錯表示域，後面所有收縮都可能是假的

Paper 01 的基本 closure theorem 依賴一項最先但也最容易被忽略的前提：研究域必須完整涵蓋所有真實反例的表示。

設

$$
\phi:D\to X.
$$

Paper 01 定義

$$
\mathcal C_X=\phi(\mathcal C)
$$

並要求

$$
\mathcal C_X\subseteq\Omega_0.
$$

如果這一步失敗，後續即使存在

$$
\Omega_T=\varnothing,
$$

也不能推出

$$
\mathcal C=\varnothing.
$$

更微妙的是，即使 $\phi(D)$ 完全覆蓋原域， $\phi$ 仍可能因 many-to-one compression 把 proof-relevant differences 壓進同一 fiber。

因此至少要區分兩個問題：

$$
\boxed{
\text{Coverage Problem:}
\quad
\text{所有可能反例是否真的進入 route domain？}
}
$$

以及

$$
\boxed{
\text{Collapse Problem:}
\quad
\text{進入後是否丟失了後續證明需要區分的資訊？}
}
$$

兩者不同。

一個 surjective representation 仍然可能嚴重坍縮；一個 non-injective representation 也可能完全足夠。

這篇研究的核心就是找出兩者之間的正式邊界。

---

# 2. 與既有形式方法的關係

## 2.1 Abstract Interpretation：sound abstraction 並不要求 injectivity

Cousot 與 Cousot 的 abstract interpretation 建立 concrete semantics 與 abstract semantics 之間的 order-theoretic approximation。其核心不是保留 concrete state 的一一對應，而是保證 abstraction 對所研究語義是 sound。

這對 SDPE 有直接啟示：

> 壓縮本身不是問題；沒有型別化壓縮損失才是問題。

Paper 02 將這一精神移到一般數學研究中的 counterexample domain。

## 2.2 Model Checking and Abstraction：抽象空間可以更小，但 preservation 必須明示

Clarke、Grumberg 與 Long 的 abstraction work 已經明確展示：模型檢查可以在較小的 abstract model 上執行，但抽象關係必須足以保留目標 temporal properties。

因此「新表示上比較容易證」本身不構成 global proof；真正需要的是 property-preservation theorem。

## 2.3 Completeness in Abstract Interpretation

Giacobazzi、Ranzato 與 Scozzari 將 completeness 形式化為 abstract computation 沒有額外遺失其 abstract domain 本可表達資訊的情況，並研究 complete shell / kernel。

這與本文的 proof-relevant non-collapse 有重要結構對照：

$$
\boxed{
\text{soundness}
\neq
\text{completeness}.
}
$$

SDPE 可以在 representation 不完整時保持 sound，只是 survivor 中會累積更多 false positives；只有在想把 abstract result 當成 exact quotient result 時，才需要更強 preservation。

## 2.4 Strong Preservation

Ranzato 與 Tapparo 將 model-checking strong preservation 與 abstract-interpretation completeness 聯繫起來：若 abstraction 對指定 specification language strongly preserving，concrete 與 abstract model checking 對該語言得到相同結果。

本文採用相同的相對化精神：

> 「非坍縮」永遠應相對於 proof-relevant language / predicate family / operator family，而不是要求保留 concrete world 的每一個微小差異。

## 2.5 CEGAR 與 2026 Reachability-Guided Abstraction Refinement

CEGAR 說明 mixed / spurious abstract states 不需要一開始全部消失；可以在發現不足時 refine abstraction。

2026 年 Ganty、Manini 與 Ranzato 更進一步研究 reachability-guided refinement 與 semi-completeness：不必為整個 universe 追求昂貴 full completeness，而可在真正 relevant / reachable region 上建立足夠 completeness。

這與 SDPE 的 route-domain 思路高度相容：

$$
\boxed{
\text{不要求全宇宙表示完美，}
\text{只要求所有可能反例與 proof-relevant region 被 soundly 處理。}
}
$$

## 2.6 本篇定位

本文不宣稱創造 Galois connection、abstract refinement、strong preservation 或 quotient abstraction。

本文的工作是把這些成熟形式概念重新組織成一個適用於**長時間、多表示、多 theorem cut、全域數學證明研究**的 route-domain contract，並與 Paper 01 的 survivor enclosure 接合。

---

# 3. 表示映射自然產生一個 Galois connection

令

$$
\phi:D\to X
$$

為任意表示映射。

只考慮實際 image：

$$
X_\phi:=\phi(D).
$$

在 powerset 上定義：

$$
\alpha_\phi:\mathcal P(D)\to\mathcal P(X_\phi),
$$

$$
\boxed{
\alpha_\phi(A):=\phi(A),
}
$$

以及

$$
\gamma_\phi:\mathcal P(X_\phi)\to\mathcal P(D),
$$

$$
\boxed{
\gamma_\phi(B):=\phi^{-1}(B).
}
$$

## Theorem 3.1 — Representation-Induced Galois Connection

對所有

$$
A\subseteq D,
\qquad
B\subseteq X_\phi,
$$

有

$$
\boxed{
\alpha_\phi(A)\subseteq B
\iff
A\subseteq\gamma_\phi(B).
}
$$

### Proof

若

$$
\phi(A)\subseteq B,
$$

則對每個 $d\in A$， $\phi(d)\in B$，故

$$
d\in\phi^{-1}(B).
$$

反向亦同。

 $\square$

因 $X_\phi$ 已限制為 image，還有

$$
\boxed{
\alpha_\phi\gamma_\phi(B)=B.
}
$$

因此這裡實際得到 powerset 層的 Galois insertion。

---

# 4. Fiber Saturation：所有表示坍縮的基本幾何

## Definition 4.1 — Representation Fiber

對 $x\in X_\phi$，定義 fiber：

$$
\boxed{
F_x
:=
\phi^{-1}(\{x\}).
}
$$

若 $|F_x|>1$，表示將多個 concrete states 壓到同一 abstract state。

這本身沒有問題。

真正重要的是這些 concrete states 是否對後續 proof obligations 可互換。

## Definition 4.2 — Fiber Saturation Operator

定義：

$$
\boxed{
\operatorname{Sat}_\phi(A)
:=
\gamma_\phi\alpha_\phi(A)
=
\phi^{-1}(\phi(A)).
}
$$

它等於所有與 $A$ 中某點共享表示值之 fiber 的聯集。

## Proposition 4.3 — Saturation Is a Closure Operator

 $\operatorname{Sat}_\phi$ 滿足：

$$
A\subseteq\operatorname{Sat}_\phi(A),
$$

$$
A\subseteq B
\Longrightarrow
\operatorname{Sat}_\phi(A)
\subseteq
\operatorname{Sat}_\phi(B),
$$

以及

$$
\operatorname{Sat}_\phi(
\operatorname{Sat}_\phi(A)
)
=
\operatorname{Sat}_\phi(A).
$$

因此 representation compression 在 concrete domain 上對應一個 closure：

$$
\boxed{
A
\longmapsto
\text{整個 fiber saturation of }A.
}
$$

這個 observation 是本文後續所有 non-collapse 定義的基礎。

---

# 5. 什麼 concrete property 能被表示域精確看見？

## Definition 5.1 — $\phi$ -Definable Set

若存在

$$
B\subseteq X_\phi
$$

使

$$
A=\gamma_\phi(B),
$$

則稱 $A\subseteq D$ 為 $\phi$ -definable。

也就是 $A$ 能完全由 abstract representation 判定。

## Theorem 5.2 — Fiber Definability Equivalence

對任意 $A\subseteq D$，下列三項等價：

1.
$$
A=\operatorname{Sat}_\phi(A);
$$

2. 存在 $B\subseteq X_\phi$ 使
$$
A=\phi^{-1}(B);
$$

3. membership in $A$ 在每一個 fiber 上為常數，即
$$
\phi(d_1)=\phi(d_2)
\Longrightarrow
\bigl(d_1\in A\iff d_2\in A\bigr).
$$

### Proof

 $1\Rightarrow2$：取

$$
B=\phi(A).
$$

則

$$
\phi^{-1}(B)
=
\operatorname{Sat}_\phi(A)
=A.
$$

 $2\Rightarrow3$：若 $d_1,d_2$ 在同一 fiber，則是否屬於 $\phi^{-1}(B)$ 只取決於共同 image 是否在 $B$。

 $3\Rightarrow1$：任何與 $A$ 中點同 fiber 的點都因 membership constant 而仍在 $A$，故 saturation 不新增點。

 $\square$

---

# 6. Property Factorization：何時原命題可以精確下降到 quotient？

令

$$
P:D\to\{0,1\}
$$

為原始命題 predicate。

## Definition 6.1 — Property-Faithful Representation

若

$$
\boxed{
\phi(d_1)=\phi(d_2)
\Longrightarrow
P(d_1)=P(d_2),
}
$$

則稱 $\phi$ 對 $P$ property-faithful。

## Theorem 6.2 — Property Factorization Theorem

下列條件等價：

1. $\phi$ 對 $P$ property-faithful；
2. safe set
$$
S_P:=\{d:P(d)=1\}
$$
為 $\phi$ -saturated；
3. counterexample set
$$
\mathcal C:=\{d:P(d)=0\}
$$
為 $\phi$ -saturated；
4. 存在唯一函數
$$
P_X:X_\phi\to\{0,1\}
$$
使
$$
\boxed{
P=P_X\circ\phi.
}
$$

### Consequence

若上述條件成立，則

$$
\boxed{
\forall d\in D\;P(d)
\iff
\forall x\in X_\phi\;P_X(x).
}
$$

這就是最強形式的 route-domain exact quotient。

但 SDPE **不要求每一篇研究都達到這個強度**。

---

# 7. Mixed-Fiber Obstruction：表示坍縮真正危險的位置

## Definition 7.1 — $P$ -Mixed Fiber

若某個 $x\in X_\phi$ 的 fiber 中存在

$$
d_+,d_-\in F_x
$$

使

$$
P(d_+)=1,
\qquad
P(d_-)=0,
$$

則稱 $F_x$ 為 $P$ -mixed fiber。

## Theorem 7.2 — Mixed-Fiber Obstruction

若存在 $P$ -mixed fiber，則不存在 total quotient predicate

$$
P_X:X_\phi\to\{0,1\}
$$

使

$$
P=P_X\circ\phi.
$$

### Proof

若

$$
\phi(d_+)=\phi(d_-)=x,
$$

則 factorization 要求

$$
P(d_+)=P_X(x)=P(d_-),
$$

矛盾。

 $\square$

## No-Go 7.3 — Abstract Boolean Classification of a Mixed Fiber

若某 abstract point 為 mixed fiber，則不能僅依 abstract state $x$ 給出「safe」或「counterexample」二元分類並宣稱對整個 fiber 成立。

合法選項只有：

1. 保留為 survivor / unknown；
2. refine representation；
3. 使用額外 concrete certificate 證明所需結論其實對整個 fiber 成立；
4. 改變 proof language，使被壓掉的 distinction 不再 proof-relevant，並重新證明 adequacy。

---

# 8. Proof-Relevant Signature：非坍縮應相對於什麼？

真正的數學研究不只使用最終 predicate $P$。

它還可能使用必要條件、invariant、residue、boundary class、reachability、local obstruction 等大量 predicate。

令

$$
\Sigma
=
\{Q_\lambda:D\to V_\lambda\}_{\lambda\in\Lambda}
$$

為 proof-relevant observable family。

## Definition 8.1 — Proof-Relevant Signature

定義

$$
\boxed{
\sigma_\Sigma(d)
:=
\bigl(Q_\lambda(d)\bigr)_{\lambda\in\Lambda}.
}
$$

## Definition 8.2 — Proof-Relevant Fiber Multiplicity

對 $x\in X_\phi$ 定義

$$
\boxed{
m_\Sigma(x)
:=
\left|
\{\sigma_\Sigma(d):d\in F_x\}
\right|.
}
$$

若 cardinality 不適合直接量化，也可只記錄 signature set：

$$
\mathfrak S_\Sigma(x)
:=
\{\sigma_\Sigma(d):d\in F_x\}.
$$

## Definition 8.3 — $\Sigma$ -Non-Collapse

若對所有 $x\in X_\phi$，

$$
\boxed{m_\Sigma(x)=1,}
$$

則稱 $\phi$ 對 $\Sigma$ non-collapsing。

這不是幾何 injectivity。

同一 fiber 可以含有無限多 concrete states，只要它們對所有 proof-relevant observables 給出相同 signature。

## Definition 8.4 — Representation Singular Set

定義

$$
\boxed{
\operatorname{Sing}_\Sigma(\phi)
:=
\{x\in X_\phi:m_\Sigma(x)>1\}.
}
$$

這些點是 proof-relevant singular fibers。

在 SDPE runtime 中，它們應被視為 representation debt，而不是默默當作普通 abstract states。

---

# 9. Predicate-Family Factorization

## Theorem 9.1 — $\Sigma$ Factorization

若 $\phi$ 對 $\Sigma$ non-collapsing，則對每個 $Q_\lambda\in\Sigma$，存在唯一

$$
\overline Q_\lambda:X_\phi\to V_\lambda
$$

使

$$
\boxed{
Q_\lambda
=
\overline Q_\lambda\circ\phi.
}
$$

### Proof

對 $x\in X_\phi$ 任取 $d\in F_x$，定義

$$
\overline Q_\lambda(x):=Q_\lambda(d).
$$

 $\Sigma$ -non-collapse 保證不同 $d\in F_x$ 給出同一值，因此 well-defined。

 $\square$

## Corollary 9.2 — Boolean Closure

若所有 atomic predicates in $\Sigma$ factor through $\phi$，則由它們有限 Boolean composition 得到的 predicates 亦 factor through $\phi$。

因此 representation adequacy 可以相對於一個 proof language 而不是單一 theorem 定義。

---

# 10. Soundness 不要求 non-collapse：Fiber-Safe Exclusion

這一節是本文最重要的限制條款。

即使

$$
\operatorname{Sing}_\Sigma(\phi)\neq\varnothing,
$$

SDPE 仍然可以 soundly 運作。

只要 coarse representation 不把 mixed fibers 錯誤排除即可。

設 abstract survivor

$$
\Omega\subseteq X_\phi
$$

滿足

$$
\mathcal C\subseteq\gamma_\phi(\Omega).
$$

## Theorem 10.1 — Fiber-Safe Exclusion Theorem

令

$$
E\subseteq\Omega.
$$

若存在 theorem / certificate 證明

$$
\boxed{
\gamma_\phi(E)\cap\mathcal C=\varnothing,
}
$$

則更新

$$
\boxed{
\Omega'
:=
\Omega\setminus E
}
$$

仍保持

$$
\boxed{
\mathcal C\subseteq\gamma_\phi(\Omega').
}
$$

### Proof

任何 counterexample 若 image 位於 $E$，則它本身位於 $\gamma_\phi(E)\cap\mathcal C$，與假設矛盾。因此所有 counterexamples 的 image 都留在 $\Omega\setminus E$。

 $\square$

### 核心意義

因此 coarse / lossy representation 不是禁用的。

真正禁用的是：

$$
\boxed{
\text{只因投影點看起來安全，就把整個 fiber 刪掉。}
}
$$

合法 exclusion 必須是 fiber-safe。

---

# 11. Exact Quotient 與 Conservative Envelope：兩條合法研究策略

本文因此正式區分兩種 route strategy。

## 11.1 Exact-Quotient Strategy

要求對 proof language $\Sigma$：

$$
\operatorname{Sing}_\Sigma(\phi)=\varnothing.
$$

此時 proof-relevant predicates 可直接下降至 $X_\phi$。

優點：

- abstract reasoning 可直接對應 concrete reasoning；
- false positive fibers 少；
- closure certificate 簡單。

缺點：

- representation 可能很大；
- 建造或驗證 non-collapse 很昂貴；
- 可能失去 abstraction 帶來的計算優勢。

## 11.2 Conservative-Envelope Strategy

允許

$$
\operatorname{Sing}_\Sigma(\phi)\neq\varnothing.
$$

但要求：

- mixed fibers 預設保留；
- exclusions 必須 fiber-safe；
- spurious survivors 可以透過 refinement 再拆；
- final empty survivor 只有在整條 soundness invariant 被保留時才有 global 意義。

這是更接近 Abstract Interpretation / CEGAR 的 SDPE 實作方式。

## Principle 11.3 — No-False-Exclusion Principle

$$
\boxed{
\text{SDPE 可以容忍 false-positive survivors，}
\text{但不能容忍 false-negative counterexamples。}
}
$$

---

# 12. Representation Refinement：如何修復 mixed fibers？

令

$$
\phi:D\to X
$$

為舊表示，加入新的 discriminator

$$
\psi:D\to Y.
$$

定義 refined representation：

$$
\boxed{
\phi'(d)
:=
(\phi(d),\psi(d))
\in X\times Y.
}
$$

## Theorem 12.1 — Refinement Saturation Monotonicity

對任意

$$
A\subseteq D,
$$

有

$$
\boxed{
\operatorname{Sat}_{\phi'}(A)
\subseteq
\operatorname{Sat}_{\phi}(A).
}
$$

### Proof

若兩點在 $\phi'$ 下同 fiber，則它們必然在 $\phi$ 下同 fiber。故 refined fibers 只會比舊 fibers 細，不會更粗。

 $\square$

## Corollary 12.2 — Refinement Cannot Increase Fiber-Induced False Positives

若以 saturation excess

$$
\operatorname{Sat}_\phi(A)\setminus A
$$

衡量表示導致的不可區分區，則 refinement 不會增加此 excess。

## Theorem 12.3 — Signature-Separating Recovery

若對所有

$$
d_1,d_2\in D
$$

只要

$$
\phi(d_1)=\phi(d_2)
$$

且

$$
\sigma_\Sigma(d_1)\neq\sigma_\Sigma(d_2),
$$

就有

$$
\psi(d_1)\neq\psi(d_2),
$$

則 refined representation $\phi'$ 對 $\Sigma$ non-collapsing。

這就是 SDPE 版 refinement target：

$$
\boxed{
\text{不要追求分開所有 concrete states；}
\text{只分開 proof-relevant mixed signatures。}
}
$$

---

# 13. Operator Preservation：靜態 predicate 完整還不夠

很多數學問題不是只判斷單點 predicate。

例如：

- dynamical orbit；
- reachability；
- induction；
- recurrence；
- fixed point；
- closure operator；
- graph transition；
- temporal logic。

令

$$
T:\mathcal P(D)\to\mathcal P(D)
$$

為 concrete transformer。

## Definition 13.1 — Best Representation-Induced Abstract Transformer

定義

$$
\boxed{
T^\#
:=
\alpha_\phi
\circ T
\circ\gamma_\phi.
}
$$

它先把 abstract set lift 回 concrete fibers，執行 concrete transformer，再重新 abstraction。

## Proposition 13.2 — Forward Soundness

對任意 concrete $A\subseteq D$：

$$
\boxed{
\alpha_\phi(T(A))
\subseteq
T^\#(\alpha_\phi(A)).
}
$$

### Proof

由

$$
A\subseteq\gamma_\phi\alpha_\phi(A)
$$

以及 $T$ monotone，即得。

 $\square$

## Definition 13.3 — Operator Completeness on $A$

若

$$
\boxed{
\alpha_\phi(T(A))
=
T^\#(\alpha_\phi(A)),
}
$$

則稱表示對 $T$ 在 $A$ 上 complete。

soundness 允許 spurious abstract successors；completeness 排除這種由 abstraction 造成的額外行為。

### 13.4 Why this matters for SDPE

若 theorem cut 依賴

$$
T^n,
\quad
\operatorname{Reach}(T),
\quad
\operatorname{Fix}(T),
$$

只證 $P$ 在 fibers 上同質仍然不足。

必須另外證：所使用的 transition / reachability semantics 在 representation 中是 soundly transported。

更強的 strong preservation / bisimulation 類條件可在需要 exact temporal reasoning 時使用；但 SDPE 不要求每一個 route 都達到這個強度。

---

# 14. Route-Domain Completeness 不是一個 Boolean，而是一組義務

「走對路徑域」若只寫成

$$
\mathcal C_X\subseteq\Omega_0
$$

仍過於粗糙。

本文提出六項 Route Adequacy Obligations。

## 14.1 Coverage Obligation

必須證：

$$
\boxed{
\mathcal C
\subseteq
\bigcup_i U_i,
}
$$

其中 $U_i$ 是真正進入研究表示的 concrete chart domains。

最強但不必要的充分條件是

$$
D=\bigcup_iU_i.
$$

## 14.2 Fiber Adequacy Obligation

對 proof-relevant $\Sigma$，必須知道：

- fibers 是否 $\Sigma$ -homogeneous；或
- 哪些 points 位於 $\operatorname{Sing}_\Sigma(\phi)$。

## 14.3 Cut Liftability Obligation

任何 abstract exclusion $E\subseteq X$ 必須具有 concrete lift certificate：

$$
\boxed{
\gamma_\phi(E)\cap\mathcal C=\varnothing.
}
$$

## 14.4 Operator Preservation Obligation

若 cut 使用 dynamics / reachability / induction，必須證相關 transformer 的 forward soundness，必要時證 completeness / strong preservation。

## 14.5 Boundary Ownership Obligation

representation chart boundary、mixed fiber、undefined transform、partial map domain 都不能掉入無主區。

它們必須：

- 被某 chart 接手；
- 被保留為 survivor；或
- 有獨立 exclusion certificate。

## 14.6 Replayability Obligation

route certificate 必須保存：

- representation version；
- domain / codomain；
- abstraction / concretization；
- proof-relevant language；
- known losses；
- singular fibers / boundary debt；
- theorem dependencies；
- checker / replay path。

---

# 15. Route Adequacy Vector

對 representation $\phi$，定義一個不必壓成單一 scalar 的資格向量：

$$
\boxed{
\mathbf A(\phi)
=
(
A_{\rm cov},
A_{\rm fiber},
A_{\rm lift},
A_{\rm op},
A_{\rm boundary},
A_{\rm replay}
).
}
$$

每一分量可以標記：

$$
\{\mathsf{Pass},\mathsf{Fail},\mathsf{Open},\mathsf{Scoped},\mathsf{Branch}\}.
$$

因此一個 representation 不應只被描述為「好／不好」。

例如可以出現：

$$
\mathbf A(\phi)
=
(
\mathsf{Pass},
\mathsf{Open},
\mathsf{Pass},
\mathsf{Scoped},
\mathsf{Open},
\mathsf{Pass}
).
$$

這意味著：

> route coverage 已證，exclusion 可 lift，certificate 可重播，但 fiber non-collapse 尚未完全處理，dynamic semantics 只在某 scope 保證，boundary 仍有 debt。

這比「此表示已驗證」更精確。

---

# 16. Route Representation Contract

結合 DEST 的 Navigation Contract、GCS projection sufficiency 與 SDPE proof obligations，本文提出最小 representation contract：

$$
\boxed{
\operatorname{RouteCert}(\phi)
=
\langle
Dom,
Cod,
\phi,
\alpha,
\gamma,
Cover,
\Sigma,
Sing,
Ops,
Lift,
Boundary,
Loss,
Dep,
Version,
Replay
\rangle.
}
$$

其中：

- $Dom$：concrete 適用域；
- $Cod$：abstract / route domain；
- $\phi$：表示映射；
- $\alpha,\gamma$：abstraction / concretization；
- $Cover$：counterexample coverage theorem；
- $\Sigma$：proof-relevant signature family；
- $Sing$：已知 representation-singular fibers；
- $Ops$：需要 preservation 的 operators；
- $Lift$：abstract exclusion 如何回到 concrete certificate；
- $Boundary$：partial / chart boundaries 的 ownership；
- $Loss$：已知 representation loss；
- $Dep$：依賴 theorem / data / version；
- $Version$：representation version；
- $Replay$：重建與獨立驗證方法。

沒有此 contract 的表示快速通道，可以作探索工具，但不能直接成為 final proof closure 的可信節點。

---

# 17. 多表示不是問題：Route Atlas

單一表示通常不可能同時最適合所有反例型態。

因此定義 chart family：

$$
\boxed{
\mathfrak A
=
\{(U_i,\phi_i,X_i,\Omega_i)\}_{i\in I}.
}
$$

其中

$$
U_i\subseteq D,
$$

$$
\phi_i:U_i\to X_i.
$$

## Definition 17.1 — Counterexample-Covering Route Atlas

若

$$
\boxed{
\mathcal C
\subseteq
\bigcup_{i\in I}U_i,
}
$$

則稱 $\mathfrak A$ counterexample-covering。

每一 chart 要求

$$
\phi_i(\mathcal C\cap U_i)
\subseteq
\Omega_i.
$$

## Theorem 17.2 — Multi-Chart Empty-Survivor Closure

若：

1. $\mathfrak A$ counterexample-covering；
2. 每一 chart survivor sound；
3. 對所有 $i$，
$$
\Omega_i=\varnothing,
$$

則

$$
\boxed{\mathcal C=\varnothing.}
$$

### Proof

若存在 $c\in\mathcal C$，由 coverage 必有 $c\in U_i$。則

$$
\phi_i(c)\in\Omega_i,
$$

與 $\Omega_i=\varnothing$ 矛盾。

 $\square$

### 17.3 What this theorem does not solve

這個 theorem 只證明「每個 chart 都被完全關閉時」的 global closure。

若不同 charts 的 theorem cuts 相互依賴、overlap 上有 translation、cycle consistency 或 boundary ownership 問題，仍需要 Paper 03 的 global gluing / coverage certificate。

因此：

$$
\boxed{
\text{atlas coverage}
\neq
\text{automatic gluing completeness}.
}
$$

---

# 18. 表示組合：每多過一層轉換都可能新增 collapse

實際 AI research 常有：

$$
D
\xrightarrow{\phi}
X
\xrightarrow{\psi}
Y.
$$

例如：

$$
\text{raw problem}
\to
\text{symbolic code}
\to
\text{feature vector}
\to
\text{cluster / branch class}.
$$

## Proposition 18.1 — Composition Can Only Coarsen Fibers

對 composite

$$
\chi:=\psi\circ\phi,
$$

有

$$
\boxed{
\operatorname{Sat}_\phi(A)
\subseteq
\operatorname{Sat}_\chi(A).
}
$$

因為 composite equality

$$
\chi(d_1)=\chi(d_2)
$$

可能在 $\phi(d_1)\neq\phi(d_2)$ 時仍成立。

所以每增加一層 compression，都可能增加 proof-relevant mixed fibers。

## Theorem 18.2 — Faithful Composition

若：

1. $P=P_X\circ\phi$ ；
2. $P_X=P_Y\circ\psi$ ；

則

$$
\boxed{
P=P_Y\circ(\psi\circ\phi).
}
$$

因此 representation composition 可以合法，但每一層都要有自己的 preservation certificate。

## No-Go 18.3 — Uncertified Shortcut Composition

不能因為

$$
\phi
$$

與

$$
\psi
$$

各自在不同 context 看似合理，就自動推出 composite route 對 final proof faithful。

所需 invariant 必須穿過整條 chain。

---

# 19. Representation Debt

本文把表示尚未解決的 proof obligations 統一稱為 representation debt。

定義 debt profile：

$$
\boxed{
\mathbf D_{\rm repr}
=
(
D_{\rm cover},
D_{\rm fiber},
D_{\rm lift},
D_{\rm op},
D_{\rm boundary},
D_{\rm version}
).
}
$$

特別地，對當前 survivor $\Omega_t$，定義 unresolved singular-fiber region：

$$
\boxed{
\mathcal U_t^{\rm sing}
:=
\Omega_t
\cap
\operatorname{Sing}_\Sigma(\phi).
}
$$

這個集合可以用作 route-selection signal：

- 若很大，優先 refine representation；
- 若很小但每個 fiber 很難，可能改用 concrete certificate；
- 若 singularity 只來自不再 relevant 的 observable，縮小 $\Sigma$ ；
- 若來自新的 theorem dependency，重新 version representation contract。

這將表示選擇從風格問題變成 proof-debt routing 問題。

---

# 20. 與五個既有系列的接口

## 20.1 全域量詞—證明張力—研究路由

GQCM 提供：

$$
\text{如何把逐點全域量詞轉成結構控制問題。}
$$

本篇補：

$$
\boxed{
\text{被選中的結構域必須如何證明沒有遺失反例。}
}
$$

## 20.2 DEST 多域知識判定論

DEST 已區分 definition / observation / reachability / judgment / verification / local / global domains。

Paper 02 將 route completeness 看成一個多域資格，而不是「表示存在」即算完成。

## 20.3 DEST 表示逃逸與解空間導航

DEST-09 已提出 Navigation Contract 與 Projection Sufficiency。

本文把這個工程／知識規格收斂成 proof-side 必要條件：任何 projection / Fold / Compress / Reparam 若進入 final proof，都必須提供 fiber-level preservation / lift certificate。

## 20.4 解空間幾何計算論

GCS 允許：

$$
\text{rewrite solution space, then navigate it}.
$$

本文補上：

$$
\boxed{
\text{幾何快速通道不能改變 proof truth by hiding fibers.}
}
$$

## 20.5 X 積分與 non-collapse

X 積分系列反覆區分 projection、multiplicity、non-collapse 與 structural residue。

本文給出一個 proof-side fiber 版本：

$$
m_\Sigma(x)>1
$$

表示 abstract point 仍包含多個 proof-relevant concrete signatures。

因此 raw fiber cardinality、measure、dimension 都不是唯一關鍵；真正重要的是 proof-relevant multiplicity。

---

# 21. 主要 No-Go 結果

## No-Go 21.1 — Surjectivity Is Not Completeness

即使

$$
\phi(D)=X,
$$

也不能推出 representation 對 $P$ 或 $\Sigma$ faithful。

## No-Go 21.2 — Injectivity Is Not Necessary

要求

$$
\phi(d_1)=\phi(d_2)
\Rightarrow
d_1=d_2
$$

是足夠但通常過強的條件。

SDPE 只需要保留 proof-relevant distinctions 或使用 fiber-safe exclusion。

## No-Go 21.3 — Small Fibers Are Not Safe Fibers

即使

$$
|F_x|=2,
$$

只要兩點對 $P$ 或某個 critical invariant 不同，該 fiber 仍然是 singular。

反之，即使 $F_x$ 無限，只要 signature homogeneous，也可以完全安全。

## No-Go 21.4 — Low-Dimensional Projection Is Not Automatically Sound

降維降低搜索成本，不代表保留 proof truth。

需要 saturation / factorization / lift certificate。

## No-Go 21.5 — Empty Projection Without Route Soundness Is Not a Proof

若 survivor 在 $X$ 中被清空，但 route coverage、fiber-safe cuts 或 operator preservation 失敗，則

$$
\Omega_T=\varnothing
$$

只是一個 abstract computation result，不是 original theorem certificate。

## No-Go 21.6 — Pointwise Property Preservation Does Not Guarantee Dynamic Preservation

若 proof 依賴 reachability / transition / fixed point，只知道 $P$ 在 fiber 上同質不足。

需要 operator-level preservation。

## No-Go 21.7 — More Representations Do Not Automatically Give Coverage

列舉很多 charts 不等於

$$
\mathcal C\subseteq\bigcup_iU_i.
$$

coverage theorem 必須獨立存在。

## No-Go 21.8 — No Observed Escape Does Not Mean No Representation Escape

目前所有表示都失敗，只能證明目前 atlas 未完成，不能推出不存在新合法 representation。

---

# 22. Route-Domain Completeness 的兩個層級

本篇最後將「走對路徑域」正式拆成 weak 與 strong 兩個層級。

## Definition 22.1 — Weak Route Completeness

若：

1. 所有 counterexamples 都進入 route atlas；
2. survivor envelope sound；
3. 每個 exclusion fiber-safe；
4. boundary 不被遺失；

則稱 route weakly counterexample-complete。

這足以支援 SDPE 的 sound contraction。

## Definition 22.2 — Strong Route Completeness Relative to $(\Sigma,\mathcal T)$

除 weak completeness 外，若：

1. $\phi$ 對 proof language $\Sigma$ non-collapsing；
2. 對需要的 transformer family $\mathcal T$ 達到指定 completeness / strong-preservation level；

則稱 route strongly complete relative to $(\Sigma,\mathcal T)$。

### Principle

$$
\boxed{
\text{SDPE closure 需要 weak completeness；}
\text{exact quotient reasoning 才需要 strong completeness。}
}
$$

這個區分避免把實務可用的 sound abstraction 錯誤要求成 perfect representation。

---

# 23. Paper 02 的主定理鏈

本篇核心可以壓縮為：

$$
\boxed{
\phi:D\to X
}
$$

自然產生

$$
\boxed{
\alpha_\phi\dashv\gamma_\phi
}
$$

以及 concrete fiber closure

$$
\boxed{
\operatorname{Sat}_\phi=\gamma_\phi\alpha_\phi.
}
$$

proof-relevant set / predicate 能在 $X$ 中精確表示，當且僅當它對 fiber saturation closed：

$$
\boxed{
A=\operatorname{Sat}_\phi(A).
}
$$

因此 representation 的真正 proof loss 不是「many-to-one」本身，而是

$$
\boxed{
\text{同一 fiber 中仍存在不同 proof-relevant signatures}.}
$$

若存在 mixed fibers，有兩條合法路：

$$
\boxed{
\text{Refine}
\quad\vee\quad
\text{Retain + Fiber-Safe Certificate}.
}
$$

而不是：

$$
\boxed{
\text{Project and silently discard.}
}
$$

---

# 24. 對 SDPE 整體框架的影響

Paper 01 的 closure rule：

$$
\Omega_{t+1}
=
\Omega_t\cap H_t
$$

現在必須改讀成：

$$
\boxed{
\begin{aligned}
&\text{representation route certified},\\
&\text{counterexamples covered},\\
&\text{abstract cut fiber-safe},\\
&\text{dynamic semantics preserved when used},\\
&\text{boundary owned},\\
&\text{then commit }\Omega_{t+1}.
\end{aligned}
}
$$

所以 theorem cut 的 verification 不只檢查 theorem statement。

還要檢查 theorem 所使用的 representation 是否仍在有效 certificate scope 內。

這也解釋為什麼長期研究到後期可能進入 verification-dominated phase：

> theorem 越多、表示越多、跨表示橋越多，真正昂貴的部分可能變成 preservation / coverage / version / boundary audit，而不是新 lemma 的生成。

---

# 25. 下一篇：Coverage、Gap 與 Global Closure Certificate

Paper 02 解決的是：

$$
\boxed{
\text{一個 route / chart 怎麼證明不漏反例、不靜默坍縮？}
}
$$

但多 chart 情形還留下一個更大的問題：

$$
\boxed{
\text{所有局部 route 合起來真的完整嗎？}
}
$$

因此 Paper 03 將正式研究：

$$
\boxed{
\textbf{多維覆蓋、Gap 與 Global Closure Certificate}.}
$$

核心目標包括：

- branch union completeness；
- boundary ownership；
- overlap compatibility；
- cycle / cocycle debt；
- local-to-global gluing；
- multidimensional coverage vector；
- final empty-domain certificate。

Paper 03 的基本問題將不再是「每一篇 lemma 對不對」，而是：

$$
\boxed{
\text{這些正確 lemmas 是否真的覆蓋了整個 counterexample atlas？}
}
$$

---

# 26. Theorem / Definition / Hypothesis Ledger

## 26.1 本篇內部定理

1. Representation-Induced Galois Connection；
2. Saturation Closure Proposition；
3. Fiber Definability Equivalence；
4. Property Factorization Theorem；
5. Mixed-Fiber Obstruction；
6. Predicate-Family Factorization；
7. Fiber-Safe Exclusion Theorem；
8. Refinement Saturation Monotonicity；
9. Signature-Separating Recovery；
10. Abstract Transformer Forward Soundness；
11. Multi-Chart Empty-Survivor Closure；
12. Faithful Representation Composition。

## 26.2 本篇定義

- representation fiber；
- fiber saturation；
- $\phi$ -definable set；
- property-faithful representation；
- proof-relevant signature；
- proof-relevant fiber multiplicity；
- representation singular set；
- weak / strong route completeness；
- route adequacy vector；
- route representation contract；
- representation debt；
- route atlas。

## 26.3 外部技術 grounding

- Abstract Interpretation / Galois connection tradition；
- abstract model checking / property preservation；
- completeness in abstract interpretation；
- strong preservation；
- CEGAR；
- reachability-guided semi-complete refinement。

這些只作結構 grounding，不被描述為 SDPE 的原創 theorem。

## 26.4 Open problems

- 如何有效發現 $\operatorname{Sing}_\Sigma(\phi)$ 而不展開所有 fibers；
- 如何選擇最小 discriminator $\psi$ 消除 critical singularity；
- 如何衡量 representation debt 與 verification cost；
- 多 chart overlap 的完整 gluing criterion；
- infinite atlas 的 closure certificate；
- proof-language $\Sigma$ 動態變化時如何 propagation stale certificates；
- representation composition 長鏈的 loss accounting；
- 在 Lean / Coq / SMT 中編碼 RouteCert 的最小形式。

---

# 27. 結論

空間域證明包圍若要成為真正的全域證明方法，第一個問題從來不是「能不能找到更聰明的表示」。

真正的問題是：

$$
\boxed{
\text{這個表示是否有權代表所有可能反例？}
}
$$

以及：

$$
\boxed{
\text{它壓掉的 distinctions 是否對證明真的不重要？}
}
$$

本文給出的答案不是要求 representation injective，而是建立 fiber-level discipline。

任意表示自然帶來：

$$
\operatorname{Sat}_\phi(A)
=
\phi^{-1}(\phi(A)).
$$

因此表示的 proof power 取決於哪些 concrete sets / predicates / dynamics 對這個 fiber closure 穩定。

若 proof-relevant signatures 在 fiber 上同質，可以安全 quotient。

若不同質，不能靜默排除，只能：

$$
\boxed{
\text{refine}
\quad\vee\quad
\text{retain}
\quad\vee\quad
\text{prove the whole fiber safe}.
}
$$

由此，「走對路徑域」被正式拆成可驗證的 route obligations，而不再只是研究直覺。

這也確立 SDPE 的第二個最低原則：

$$
\boxed{
\textbf{所有表示壓縮都必須對 proof-relevant fibers 負責。}
}
$$

Paper 01 的第一原則是：

$$
\boxed{
\textbf{所有 theorem cuts 都必須保持 counterexample envelope sound。}
}
$$

Paper 02 現在補上：

$$
\boxed{
\textbf{所有 route transformations 都必須保存或顯式管理 counterexample-relevant distinctions。}
}
$$

下一步才有資格討論多條正確 route 如何真正黏成 global closure。

---

# References

## External primary literature

1. P. Cousot and R. Cousot, **Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs by Construction or Approximation of Fixpoints**, POPL 1977, pp. 238–252. DOI: `10.1145/512950.512973`.
2. E. M. Clarke, O. Grumberg, and D. E. Long, **Model Checking and Abstraction**, *ACM Transactions on Programming Languages and Systems* 16(5), 1512–1542, 1994. DOI: `10.1145/186025.186051`.
3. E. M. Clarke, O. Grumberg, S. Jha, Y. Lu, and H. Veith, **Counterexample-Guided Abstraction Refinement**, CAV 2000, LNCS 1855, pp. 154–169. DOI: `10.1007/10722167_15`.
4. R. Giacobazzi, F. Ranzato, and F. Scozzari, **Making Abstract Interpretations Complete**, *Journal of the ACM* 47(2), 361–416, 2000. DOI: `10.1145/333979.333989`.
5. F. Ranzato and F. Tapparo, **Generalized Strong Preservation by Abstract Interpretation**, *Journal of Logic and Computation* 17(1), 157–197, 2007; arXiv:`cs/0401016`.
6. R. Giacobazzi and F. Ranzato, **The Best of Abstract Interpretations**, *Proceedings of the ACM on Programming Languages* 9 (POPL), Article 46, 2025. DOI: `10.1145/3704882`.
7. P. Ganty, N. Manini, and F. Ranzato, **Reachability-Guided Abstraction Refinement**, FM 2026, LNCS 16556, pp. 599–618. DOI: `10.1007/978-3-032-26204-2_31`.

## Internal framework antecedents

8. **空間域證明包圍論 I：全域量詞、反例域與可驗證收縮**, v0.1, 2026.
9. **多域知識判定論：定義域、觀察域、可達域、判定域、驗證域、局部域與全域黏合域**, DEST-01, v0.1, 2026.
10. **表示逃逸與解空間導航 2.0：幾何改寫、通道證書、成本與跨表示不變量**, DEST-09, v0.1, 2026.
11. **幾何快速通道：解空間折疊、橋接、投影與隧穿算子**, GCS-05, v0.1, 2026.
12. **X 積分系列**, 2026, especially the non-collapse / projection / premeasure line.
