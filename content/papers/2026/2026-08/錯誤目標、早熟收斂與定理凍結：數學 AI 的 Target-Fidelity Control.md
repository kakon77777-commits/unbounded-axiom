# 錯誤目標、早熟收斂與定理凍結：數學 AI 的 Target-Fidelity Control

**Corrupted Targets, Premature Closure, and Theorem Freezing: Target-Fidelity Control for Mathematical AI**

**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-11

## 摘要

自動形式化與自動定理證明的快速進展，使 AI 系統逐漸具備從自然語言問題、研究文獻或 benchmark statement 出發，自動生成形式命題並尋找證明的能力。然而，當形式證明的後端可靠性持續提升時，一個新的上游風險反而變得更加重要：**AI 可能非常嚴格地證明一個錯誤的 theorem target。**

本文提出 **Target-Fidelity Control（TFC）** 作為數學 AI 在正式 proof search 前的目標治理框架。我們區分兩大類 target corruption。第一類為 **formal-structure corruption**：形式化本身破壞了量詞順序、定義域、uniformity、漸近語義、certificate dependency 或 representation coverage。第二類為 **source-identity corruption**：形式命題本身完全精確，甚至可以被正確證明，但它並不是原始來源真正指定的問題，例如偷偷改成更強或更弱的 formulation、以衍生公式直接取代原始定義、或把 probability theorem 無條件升格成 decision theorem。

本文建立十類 target corruption taxonomy：Quantifier Swap、Domain Omission、Unnecessary Uniformity、Predicate Flattening、Certificate Truncation、Asymptotic-to-Finite Collapse、Wrong Source Formulation、Framework Bridge Collapse、Definition Substitution without Provenance，以及 Representation Coverage Failure。進一步，我們引入 source target $C_{\mathrm{source}}$ 、candidate family $\mathcal C_{\mathrm{candidate}}$ 與 frozen target $C^\ast_{\mathrm{freeze}}$，並將 theorem freezing 建模為一個有條件的 closure 操作，而非單純「形式化成功」的同義詞。

核心流程為：

$$
C_{\mathrm{source}}
\rightarrow
\mathcal C_{\mathrm{candidate}}
\rightarrow
\operatorname{Audit}
\rightarrow
C^\ast_{\mathrm{freeze}}
\rightarrow
\operatorname{Proof}.
$$

我們提出 Target Fidelity、Closure Debt、Freeze Eligibility 與 Premature Closure Risk 等概念，用以描述 theorem target 是否已足夠穩定。本文以 Formal Conjectures 中的 Erdős Problem 90、707、34、Ben Green Open Problem 3，以及 Open Quantum Problem 23 等案例展示不同 corruption 類型。本文不宣稱此 taxonomy 已完備，也不宣稱 target audit 必然降低所有 proof cost；其主要貢獻是把「證明正確」與「證明正確的問題」正式分離，並提供一套可被 error injection、blind evaluation 與 theorem-prover benchmark 檢驗的研究架構。

**關鍵詞：** Target Fidelity、Theorem Freezing、Target Corruption、Premature Closure、Autoformalization、Formal Conjectures、Mathematical AI、Quantifier Dependency、Certificate Structure、Source Fidelity

---

## 1. 引言

形式定理證明通常從一個已知 theorem target 開始：

$$
C.
$$

proof search 的問題是：

$$
\boxed{
\text{Given } C,\text{ find } P \text{ such that } P\vdash C.
}
$$

在這種設定下，只要 proof assistant kernel 正確工作，證明是否符合 $C$ 可以被機器嚴格檢查。

但自動形式化改變了問題。

當 AI 的輸入不是一個已經固定的 Lean theorem，而是：

- 自然語言研究問題；
- 論文中的 informal theorem；
- 歷史 conjecture；
- benchmark description；
- 多版本來源；
- 人類對話中的數學敘述；

系統首先必須生成：

$$
C'.
$$

真正的流程因此變成：

$$
N
\rightarrow
C'
\rightarrow
P.
$$

此時，即使：

$$
P\vdash C'
$$

完全正確，也仍然存在：

$$
\boxed{
C'\stackrel{?}{\equiv}C_{\mathrm{source}}.
}
$$

因此，形式證明的 soundness 並不能單獨解決 target identity。

近年的 Formal Conjectures 已把 formalization fidelity 視為 benchmark 維護中的實質問題，並指出 AI 產生的 proof 與 disproof 可以反過來成為 formalization audit 的工具。LeanMarathon 則在長時程 autoformalization 中把 target-fidelity stabilization 放在 proof DAG 執行之前，顯示 statement drift 與 target preservation 已成為研究級 formalization 的系統性問題。Lean-GAP 的資料建構亦指出 informal–formal correspondence verification 是形式化流程中最細緻且最依賴人工監督的環節之一。這些工作共同顯示：target fidelity 已不能被視為單純 parser correctness 的附屬問題。 

本文將這個問題抽象成：

$$
\boxed{
\text{Target-Fidelity Control}.
}
$$

其目的不是重新定義 theorem prover 的邏輯，而是在 proof search 前回答：

> **這個 theorem target 是否已經足夠忠實、完整且穩定，可以開始支付正式證明成本？**

---

## 2. 從 Formal Correctness 到 Target Correctness

設：

$$
C_{\mathrm{source}}
$$

為原始問題。

AI 產生：

$$
C_{\mathrm{formal}}.
$$

至少需要區分三種 correctness：

### 2.1 Syntactic correctness

$$
\operatorname{Syn}(C_{\mathrm{formal}})=1.
$$

例如 Lean code 可解析、型別正確、符號已定義。

### 2.2 Logical correctness

若已找到 proof $P$：

$$
P\vdash C_{\mathrm{formal}}.
$$

proof kernel 接受該證明。

### 2.3 Target correctness

$$
\operatorname{Fid}
(
C_{\mathrm{formal}},
C_{\mathrm{source}}
)
\ge \theta.
$$

即 formal target 與來源問題在 proof-relevant 意義下足夠忠實。

因此：

$$
\boxed{
\operatorname{Syn}=1
\land
\operatorname{Proof}=1
\not\Rightarrow
\operatorname{TargetCorrect}=1.
}
$$

這是本文的出發點。

---

## 3. Target Corruption 的兩個超類

我們將 target corruption 分為兩個基本超類。

# 3.1 Formal-Structure Corruption

形式化過程直接破壞問題的邏輯或結構：

$$
C_{\mathrm{source}}
\xrightarrow{\Pi}
C_{\mathrm{formal}},
$$

其中 $\Pi$ 改變：

- quantifier order；
- domain；
- witness dependency；
- uniformity；
- boundary；
- certificate；
- asymptotic semantics；
- representation coverage。

形式 statement 本身可能十分精確，但它精確地表示了一個不同命題。

形式化工具本身通常可以檢查 syntax 和 types，卻不一定能知道這些改變是否忠實於 source semantics。CRAMF 等 autoformalization 研究已明確指出 ambiguous or missing premises 所造成的 semantic gap 是自然語言到形式語言轉換的重要障礙之一。

# 3.2 Source-Identity Corruption

另一類更難。

假設：

$$
C_1
$$

與：

$$
C_2
$$

各自都是完全合法的 formal theorem。

問題在於 source 指定：

$$
C_1,
$$

AI 卻選了：

$$
C_2.
$$

例如：

- source 有三個遞增強度的 conjectures，AI 選錯版本；
- source 問 maximum value，AI 改證 strongest possible existence；
- source 以 combinatorial object 定義 sequence，AI 直接以已知 closed formula 重新定義 sequence；
- source 得到 probability result，AI 將其直接當成 universal decision theorem。

這種 corruption 不能只靠 AST、type checker 或 proof kernel 發現。

因此：

$$
\boxed{
\text{Formal-Structure Audit}
\neq
\text{Source-Identity Audit}.
}
$$

---

## 4. Target Corruption Taxonomy

本文提出第一版十類 taxonomy。

---

### 4.1 Quantifier Swap

原命題：

$$
\exists W
\forall x\,
P(W,x).
$$

被改成：

$$
\forall x
\exists W_x\,
P(W_x,x).
$$

兩者通常不等價。

最典型的問題是 global witness 被降為 instance-dependent witness。

Formal Conjectures 的 Erdős Problem 90 formalization 對 Sawin proof 的一個 arithmetic reduction 特別指出：必須先固定**同一個無限質數集 $Q$**，再對任意 $N$ 找到高次 totally real field；若每個 field 都各自選一個 $Q_F$，命題會變得大幅不同，而原 uniformity 正是 proof 的 load-bearing feature。

抽象地：

$$
\boxed{
\exists Q\,
\forall N\,
\exists F_N
\neq
\forall N\,
\exists F_N\,
\exists Q_N.
}
$$

---

### 4.2 Domain Omission

原命題：

$$
\forall x\in D,\;P(x).
$$

形式化後：

$$
\forall x\in D',\;P(x),
$$

其中：

$$
D\neq D'.
$$

Domain omission 特別危險，因為 theorem 可能因此變強、變弱，甚至由 true 變 false。

Ben Green Open Problem 3 的 formal statement 明確要求：

$$
A\subseteq[0,1],
\qquad
A\text{ open},
\qquad
\mu(A)>\frac13,
$$

再問是否存在 $x,y,z\in A$ 使：

$$
xy=z.
$$

如果刪掉 `IsOpen A`，得到的是一個不同 theorem target，而不是 harmless simplification。

因此：

$$
\boxed{
\text{Boundary / Domain}
\subset
\text{Problem Identity}.
}
$$

---

### 4.3 Unnecessary Uniformity

與 Quantifier Swap 相反，AI 也可能無意中要求比原問題更強的 uniformity。

例如：

$$
\forall k\forall\epsilon
\exists N(k,\epsilon)
\forall n\ge N:\;P(k,\epsilon,n)
$$

被改成：

$$
\forall\epsilon
\exists N(\epsilon)
\forall k
\forall n\ge N:\;P(k,\epsilon,n).
$$

即使原 theorem 可證，強化後的 theorem 可能未知甚至為 false。

所以 theorem proving failure 可能並不表示 prover 不夠強，而是：

$$
\boxed{
\text{AI accidentally strengthened the theorem}.
}
$$

---

### 4.4 Predicate Flattening

有些 predicate 在 surface syntax 上是一個單一詞：

$$
\operatorname{HasDensity}(S,1),
$$

但其 proof semantics 包含極限與全域量詞。

若系統把：

> 「 $S$ 不具有密度 $1$ 」

錯壓成：

> 「找一個 $n\notin S$ 」

則 certificate type 已被破壞。

因為：

$$
\exists n\notin S
$$

完全可能與：

$$
\operatorname{density}(S)=1
$$

同時成立。

因此需要區分：

$$
Q_{\mathrm{surface}}
$$

與：

$$
Q_{\mathrm{transitive}}.
$$

我們稱 proof-relevant unfolding：

$$
\operatorname{SemanticExpand}_{\mathcal R}(P).
$$

它只展開會改變量詞、certificate、global/local nature 的 predicate，而不是遞迴展開所有定義。

---

### 4.5 Certificate Truncation

設原命題：

$$
\forall A\exists B\;P(A,B).
$$

反證需要：

$$
\exists A^\ast\forall B\;\neg P(A^\ast,B).
$$

如果 AI 找到：

$$
A^\ast
$$

就宣稱「counterexample found」，它其實只完成外層 witness。

完整 certificate 應是：

$$
\boxed{
A^\ast
+
\forall B\;\neg P(A^\ast,B).
}
$$

Erdős Problem 707 正是實例。Formal Conjectures 將 conjecture formalize 為「每個 finite Sidon set 是否可延伸到 perfect difference set」，而明確 counterexample theorem 對具體 $A$ 不只證明 finite 與 Sidon，還證：

$$
\forall B,n,\quad
A\subseteq B
\Rightarrow
\neg\operatorname{PerfectDifferenceSet}(B,n).
$$

因此：

$$
\boxed{
\text{Counterexample Object}
\neq
\text{Counterexample Certificate}.
}
$$

---

### 4.6 Asymptotic-to-Finite Collapse

漸近命題：

$$
f(n)=o(g(n))
$$

不是「前很多個 $n$ 看起來很小」。

其 negation 也不是「找很多有限 counterexamples」。

例如 Erdős Problem 34 的 formal statement把：

$$
S(\pi)=o(n^2)
$$

寫成：

$$
\forall c>0\;
\exists N\;
\forall n\ge N\;
\forall p,\quad
S(n,p)<cn^2.
$$

所以其反證結構必須到達：

$$
\boxed{
\exists c>0
\forall N
\exists n\ge N
\exists p:
S(n,p)\ge cn^2.
}
$$

無論電腦列出多少有限反例，只要沒有「任意遠」的 closure，就仍然不是完整 asymptotic disproof。

---

### 4.7 Wrong Source Formulation

source 本身可能有：

$$
C_1
\Leftarrow
C_2
\Leftarrow
C_3
$$

等多個強度不同的 formulation。

Open Quantum Problem 23 的正式化議題明確列出三層 SIC conjecture：

1. 所有維度存在 SIC-POVM；
2. 所有維度存在 group-covariant SIC；
3. Zauner-type symmetry 下存在 fiducial vector。

三者形成遞增強度階層，而不是同一 statement 的語法改寫。

因此，即使：

$$
C_2
$$

被完美 formalize 並證明，也不能說：

> 「我們完成了 benchmark 所指定的 $C_1$ 」

除非 benchmark 本來就指定 $C_2$，或已明示 equivalence / implication 的使用方式。

因此：

$$
\boxed{
\text{Formal precision}
\neq
\text{Source-target fidelity}.
}
$$

---

### 4.8 Framework Bridge Collapse

推理可能從一個 framework 跳到另一個：

$$
F_i
\rightarrow
F_j.
$$

例如：

$$
\text{probability theorem}
\rightarrow
\text{decision recommendation}.
$$

從：

$$
P(\text{win}\mid\text{switch})
=
\frac23
$$

直接推成：

$$
\forall\text{ rational agents},\;
\text{switch is uniquely correct}
$$

需要額外的 utility、risk preference、knowledge state 與 decision rule。

因此：

$$
\boxed{
\text{Probability Dominance}
\neq
\text{Universal Behavioral Norm}.
}
$$

我們稱跨 framework 所需的額外條件為 bridge toll。

若未支付：

$$
\text{BridgeDebt}>0.
$$

---

### 4.9 Definition Substitution without Provenance

設原始 object：

$$
a_{\mathrm{source}}(n)
$$

由某 combinatorial process 定義。

研究文獻發現：

$$
a_{\mathrm{source}}(n)
=
f(n).
$$

AI 若直接重新定義：

$$
a(n):=f(n)
$$

並證明後續 theorem，則它證的是 formula-defined object 的 theorem。

若要回到 source problem，還需要：

$$
\boxed{
\forall n,\quad
a_{\mathrm{source}}(n)=f(n).
}
$$

缺少此步，稱：

$$
\boxed{
\text{Provenance Gap}.
}
$$

這是一種非常隱蔽的 corruption，因為替換後的 formal development 可能比原問題乾淨得多，甚至全部可自動證明。

---

### 4.10 Representation Coverage Failure

形式數學常利用等價 representation 簡化問題。

例如 source quantifies over：

$$
\forall A\in\mathcal S
$$

而 formalization 透過 symmetry，只檢查 canonical representative：

$$
A_0
$$

再以 group action：

$$
G\curvearrowright\mathcal S
$$

覆蓋所有 case。

若 AI 保留 canonical representative，卻漏掉：

$$
\forall g\in G,
$$

則 representation 不再覆蓋 source domain。

因此：

$$
\boxed{
\text{Equivalent Representation}
=
\text{Local Form}
+
\text{Coverage Theorem}.
}
$$

少掉 coverage，就只是 projection，不是 equivalent formalization。

---

## 5. 一個統一的 Target Corruption 定義

令：

$$
C_s
$$

為 source problem，

$$
C_f
$$

為 formal candidate。

令 proof-relevant invariant set：

$$
\mathcal I(C)
=
(
D,Q,\mathcal G_Q,
U,\mathcal C_T,
R,B,E,\mathcal P
),
$$

其中：

- $D$：domain；
- $Q$：quantifiers；
- $\mathcal G_Q$：dependency；
- $U$：uniformity；
- $\mathcal C_T$：certificate structure；
- $R$：representation；
- $B$：bridge requirements；
- $E$：equivalence / implication relation；
- $\mathcal P$：provenance。

我們稱：

$$
\operatorname{Corrupt}(C_s,C_f)=1
$$

若存在 proof-relevant invariant $I$，使：

$$
I(C_s)\not\equiv I(C_f)
$$

且沒有一個已記錄、可接受的 bridge / equivalence justification：

$$
J_I:
I(C_s)\rightsquigarrow I(C_f).
$$

因此 target corruption 不等於「文字不同」。

兩個 statement 可以長得完全不同但等價。

反之，兩個 statement 也可以看起來幾乎相同，卻因一個量詞位置而不同。

---

## 6. Target Fidelity

我們不強迫 fidelity 必須先壓成單一 scalar。

可先使用向量：

$$
\mathfrak F_{\mathrm{target}}
=
(
F_D,F_Q,F_U,F_C,F_R,F_B,F_E,F_P
).
$$

分別表示：

- Domain Fidelity；
- Quantifier Fidelity；
- Uniformity Fidelity；
- Certificate Fidelity；
- Representation Fidelity；
- Bridge Fidelity；
- Equivalence Fidelity；
- Provenance Fidelity。

理想狀態：

$$
\mathfrak F_{\mathrm{target}}
=
(1,1,\ldots,1).
$$

但在實際研究中，有些項目可能：

$$
?
$$

即尚未判定。

因此：

$$
\boxed{
\text{Unknown}
\neq
\text{False}.
}
$$

target audit 不應因不確定性而自動判 source mismatch，但應阻止高風險 target 被過早 freeze。

---

## 7. Closure Debt

我們定義：

$$
\boxed{
\mathcal D_{\mathrm{closure}}(C)
}
$$

為 theorem target 尚未支付的 proof-relevant closure debt。

可拆成：

$$
\mathcal D_{\mathrm{closure}}
=
D_Q+D_D+D_C+D_B+D_E+D_P+\cdots
$$

其中：

- $D_Q$：quantifier debt；
- $D_D$：domain debt；
- $D_C$：certificate debt；
- $D_B$：bridge debt；
- $D_E$：equivalence debt；
- $D_P$：provenance debt。

例如：

### Case A

source 與 candidate 的 definition equivalence 尚未證明：

$$
D_P>0.
$$

### Case B

量詞 dependency 已完全確定：

$$
D_Q=0.
$$

### Case C

source formulation 有兩種合法版本，研究者尚未指定目標：

$$
D_E>0.
$$

Closure Debt 的目的不是把所有數學背景都展開，而是標記：

> **哪些未決事項如果處理錯，會改變 theorem identity？**

---

## 8. Freeze Eligibility

Theorem freeze 不應等於：

$$
\text{Lean accepts the statement}.
$$

我們定義：

$$
\operatorname{FreezeEligible}(C)=1
$$

至少要求：

### F1. Domain Closure

所有 load-bearing domain / boundary 已明確。

### F2. Quantifier Closure

$$
Q_s
\rightarrow
Q_t
$$

所需的 proof-relevant quantifier expansion 已穩定。

### F3. Dependency Closure

witness dependency 與 uniformity 已固定。

### F4. Certificate Closure

若 target 為 proof / disproof / construction，其 certificate type 已確定。

### F5. Source-Fidelity Closure

source formulation 與 formal target 的關係已明示：

$$
=,\quad
\Leftrightarrow,\quad
\Rightarrow,\quad
\Leftarrow,\quad
\text{variant}.
$$

### F6. Bridge Closure

任何跨 framework inference 已有明示 assumptions。

### F7. Provenance Closure

若 object 被替換為 equivalent representation / formula，等價或 provenance obligation 已記錄。

因此：

$$
\boxed{
\operatorname{FreezeEligible}
=
F_1\land F_2\land\cdots\land F_7.
}
$$

工程上可以允許部分項目為 conditional freeze，但必須把 unresolved debt 寫入 frozen target metadata。

---

## 9. Premature Closure

如果：

$$
\mathcal D_{\mathrm{closure}}(C)>0
$$

卻執行：

$$
\operatorname{Freeze}(C),
$$

我們稱：

$$
\boxed{
\operatorname{PrematureClosure}(C)=1.
}
$$

Premature closure 的危險在 AI 系統中特別高，因為 formal proof 會產生非常強的心理訊號：

> 「Lean 證明了，所以是對的。」

但 Lean 真正保證的是：

$$
P\vdash C_f.
$$

它不自動保證：

$$
C_f=C_s.
$$

因此，形式證明越可靠，target audit 反而越重要。

因為後端的高可信度可能掩蓋前端 target selection error。

---

## 10. 五個代表案例

## 10.1 Erdős 90：Uniformity 是 theorem identity

其 totally-real-tower reduction 需要：

$$
\exists Q\text{ infinite}
\;\forall N
\;\exists F_N
$$

而 $Q$ 必須在 $F_N$ 之前固定。

若改為：

$$
\forall N\exists F_N\exists Q_N,
$$

就破壞 load-bearing uniformity。

分類：

$$
\boxed{
\text{Quantifier Swap}
+
\text{Uniformity Corruption}.
}
$$

---

## 10.2 Erdős 707：Counterexample 是一棵 certificate tree

原 statement：

$$
\forall A_{\mathrm{finite,Sidon}}
\exists B,n\;P(A,B,n).
$$

反例不是只找到：

$$
A^\ast.
$$

而是：

$$
\exists A^\ast
[
\operatorname{Finite}(A^\ast)
\land
\operatorname{Sidon}(A^\ast)
\land
\forall B,n\neg P(A^\ast,B,n)
].
$$

分類：

$$
\boxed{
\text{Certificate Truncation}.
}
$$

---

## 10.3 Erdős 34：Finite evidence 不能關閉 asymptotic negation

原問題：

$$
S(\pi)=o(n^2).
$$

完整反證需要：

$$
\exists c>0\forall N\exists n\ge N\exists p:
S(n,p)\ge cn^2.
$$

分類：

$$
\boxed{
\text{Asymptotic-to-Finite Collapse}.
}
$$

---

## 10.4 Green Problem 3：Boundary 不是附註

source 明確要求：

$$
A\text{ open}
\land
A\subseteq[0,1]
\land
\mu(A)>\frac13.
$$

若直接改成 arbitrary measurable set，problem identity 已變。

分類：

$$
\boxed{
\text{Domain Omission}.
}
$$

---

## 10.5 Open Quantum Problem 23：精確 theorem 也可能選錯版本

SIC-POVM 問題存在遞增強度的三個 formulation：

$$
C_{\mathrm{SIC}},
\quad
C_{\mathrm{covariant}},
\quad
C_{\mathrm{Zauner}},
$$

且：

$$
C_{\mathrm{Zauner}}
\Rightarrow
C_{\mathrm{covariant}}
\Rightarrow
C_{\mathrm{SIC}}.
$$

選擇其中一個完全合法的 formal theorem，不代表它就是 benchmark 當前指定的 target。

分類：

$$
\boxed{
\text{Wrong Source Formulation}.
}
$$

---

## 11. Target Freeze State Machine

我們提出：

$$
\boxed{
C_{\mathrm{source}}
\rightarrow
\mathcal C_{\mathrm{candidate}}
\rightarrow
\operatorname{Audit}
\rightarrow
C^\ast_{\mathrm{freeze}}
}
$$

的 state machine。

```text
SOURCE
  ↓
CANDIDATE
  ↓
AUDIT
  ├─ corruption → REJECT / REFORMULATE
  ├─ ambiguity → EXPAND
  ├─ excess scope → CONTRACT
  └─ closure debt sufficiently cleared → FREEZE
                                      ↓
                                    PROOF
```

重要的是：

$$
\boxed{
\text{EXPAND}
\neq
\text{REJECT}.
}
$$

問題不清楚不等於問題無效。

同樣：

$$
\boxed{
\text{CONTRACT}
\neq
\text{WEAKEN}.
}
$$

Contract 是排除 proof-irrelevant branches，不是偷偷改弱 theorem。

---

## 12. Frozen Target Metadata

一個成熟的 frozen theorem target 不應只有 formula。

應附：

$$
\mathcal M_{\mathrm{freeze}}
=
(
C^\ast,
V,
S,
D,
Q,
G,
B,
P,
R
).
$$

其中：

- $V$：version；
- $S$：source reference；
- $D$：domain record；
- $Q$：quantifier/dependency record；
- $G$：target-strength relation graph；
- $B$：bridge ledger；
- $P$：provenance；
- $R$：remaining debt / risk。

例如：

```yaml
target_status: frozen
source_version: OQP-23-vX
formal_target: SIC-existence
stronger_variants:
  - group-covariant-SIC
  - Zauner-symmetric-SIC
equivalence_status: not-assumed
domain_status: closed
quantifier_status: closed
bridge_debt: 0
provenance_debt: 0
```

如此，proof agent 才不需要自己猜：

> 「這三個 conjecture 是不是都算同一題？」

---

## 13. 與現有研究的關係

Formal Conjectures 的設計已經明確承認 formalization correctness 需要社群持續審核，並利用 proof/disproof 回饋改善 benchmark fidelity。LeanMarathon 進一步把 target-fidelity stabilization 變成長時程 formalization orchestrator 的第一階段，而 Lean-GAP 顯示 informal–formal correspondence verification 在資料建構上仍高度困難。這些結果支持一個共同方向：**可靠數學 AI 的瓶頸不只在 proof search，也在 theorem statement preservation。**

本文與這些工作的差異，是進一步把 target error 分解成可診斷 taxonomy，並把「是否開始 proof search」建模成 freeze-control problem。

因此：

$$
\boxed{
\text{Formalization}
\rightarrow
\text{Audit}
\rightarrow
\text{Freeze}
\rightarrow
\text{Proof}
}
$$

應被視為與：

$$
\text{Formalization}
\rightarrow
\text{Proof}
$$

不同的系統架構。

---

## 14. 可檢驗假說

### H1：Corruption Recall

加入 Target-Fidelity Control 應提升：

$$
P(
\text{detect corrupted target before proof}
).
$$

### H2：False-Freeze Reduction

$$
P(
\text{freeze wrong target}
\mid
\mathrm{TFC}
)
<
P(
\text{freeze wrong target}
\mid
\mathrm{direct\ formalization}
).
$$

### H3：Clean-Target Restraint

良好的 audit system 不能什麼都懷疑：

$$
P(
\text{unnecessary expansion}
\mid
\text{clean explicit target}
)
$$

應保持低值。

### H4：Proof-Cost Reduction

若錯 target 原本會引發大量搜索，則 target audit 可能降低：

$$
\text{tokens},
\quad
\text{proof branches},
\quad
\text{premise retrieval},
\quad
\text{wall time}.
$$

但本文再次強調：

$$
\boxed{
\text{target audit}
\neq
\text{intrinsic theorem simplification}.
}
$$

---

## 15. 初步實驗框架

我們將後續 benchmark 分成三個模式：

### A. Compact / Baseline

直接給 source / candidate。

### B. MPF Audit

額外檢查：

- domain；
- quantifier；
- dependency；
- certificate；
- asymptotic semantics。

### C. Dual-Tension / TFC

再加入：

- source fidelity；
- NLU；
- framework bridge；
- doubt/tolerance；
- theorem freeze。

實驗中應同時放入：

$$
\boxed{
\text{corrupted samples}
+
\text{clean controls}.
}
$$

否則一個永遠回答「有問題」的系統也能得到高 corruption recall。

因此至少記錄：

$$
\text{TP,FP,TN,FN},
$$

以及：

$$
\text{Precision},
\text{Recall},
\text{Specificity},
\text{False Freeze Rate}.
$$

---

## 16. 失敗模式

### 16.1 Audit Overreach

系統把 harmless reformulation 誤判為 corruption。

### 16.2 Equivalence Blindness

不同 representation 實際等價，但 audit system 因無法證 equivalence 而永遠拒絕 freeze。

### 16.3 Source Authority Problem

歷史 source 本身可能互相矛盾。

### 16.4 Infinite Expansion

每個定義都可繼續追問 provenance，造成 regress。

因此需要：

$$
\boxed{
\text{proof-relevant stopping rule}.
}
$$

### 16.5 Conservative Bias

過度追求 zero false-freeze 可能造成大量 unnecessary audit cost。

因此後續需要推理資源控制，而這將是本系列下一篇的主題。

---

## 17. 討論：證明錯誤 vs. 證明錯題

我們應把兩個失敗明確分開：

### Type I

$$
P\not\vdash C.
$$

證明錯了。

### Type II

$$
P\vdash C_f,
\qquad
C_f\not\equiv C_s.
$$

證明是對的，但證錯題。

傳統 theorem prover 主要防 Type I。

Target-Fidelity Control 主要防 Type II。

在 AI 系統中，Type II 可能尤其危險，因為成功通過 proof kernel 會為錯 target 提供極強可信度外觀。

因此：

$$
\boxed{
\text{Proof Verification}
+
\text{Target Verification}
}
$$

比只有其中一個更接近完整的 mathematical-AI reliability。

---

## 18. 結論

本文提出 Target-Fidelity Control，將 theorem target 的生成、審計與凍結正式放在 proof search 前。

核心區分為：

$$
\boxed{
\text{Formal-Structure Corruption}
}
$$

與：

$$
\boxed{
\text{Source-Identity Corruption}.
}
$$

並提出十類 corruption：

$$
\begin{aligned}
&\text{Quantifier Swap},\\
&\text{Domain Omission},\\
&\text{Unnecessary Uniformity},\\
&\text{Predicate Flattening},\\
&\text{Certificate Truncation},\\
&\text{Asymptotic-to-Finite Collapse},\\
&\text{Wrong Source Formulation},\\
&\text{Framework Bridge Collapse},\\
&\text{Definition Substitution without Provenance},\\
&\text{Representation Coverage Failure}.
\end{aligned}
$$

完整流程因此不再只是：

$$
C\rightarrow\operatorname{Proof},
$$

而是：

$$
\boxed{
C_{\mathrm{source}}
\rightarrow
\mathcal C_{\mathrm{candidate}}
\rightarrow
\operatorname{Audit}
\rightarrow
C^\ast_{\mathrm{freeze}}
\rightarrow
\operatorname{Proof}.
}
$$

本文最核心的主張可以濃縮為：

$$
\boxed{
\text{形式證明回答「這個命題證對了嗎？」；}
}
$$

而 Target-Fidelity Control 先回答：

$$
\boxed{
\text{「這真的是我們要證的命題嗎？」}
}
$$

當數學 AI 逐步具備更高證明能力時，後一個問題的重要性只會上升，而不會下降。

---

## 參考文獻

1. Firsching, M., Lezeau, P., Mercuri, S., et al. *Formal Conjectures: An Open and Evolving Benchmark for Verified Discovery in Mathematics.* arXiv:2605.13171, 2026.
2. Zhang, Y., Sun, Y., Suzuki, T., Lee, J. D., Liu, F. *LeanMarathon: Toward Reliable AI Co-Mathematicians through Long-Horizon Lean Autoformalization.* arXiv:2606.05400, 2026.
3. Lee, S., Hwang, B.-H., Lim, H., et al. *Lean-GAP: A Dataset of Formalized Graduate Algebra Problems.* arXiv:2606.02588, 2026.
4. Lu, W., Du, L., Li, S., et al. *Automated Formalization via Conceptual Retrieval-Augmented LLMs.* arXiv:2508.06931, 2025.
5. The Formal Conjectures Authors. *Erdős Problem 90: The Unit Distance Problem.* Formal Conjectures repository, 2026.
6. The Formal Conjectures Authors. *Erdős Problem 707: Embedding Sidon Sets in Perfect Difference Sets.* Formal Conjectures repository, 2026.
7. The Formal Conjectures Authors. *Erdős Problem 34.* Formal Conjectures repository, 2026.
8. The Formal Conjectures Authors. *Ben Green's Open Problem 3.* Formal Conjectures repository, 2026.
9. The Formal Conjectures Authors. *Open Quantum Problem 23: SIC POVMs and Zauner's Conjecture.* Formal Conjectures issue / formalization record, 2026.

---

## 研究狀態聲明

本文提出的 Target-Fidelity Control、Target Corruption Taxonomy、Closure Debt、Freeze Eligibility、Premature Closure Risk 與相關記號，屬於本文的研究框架。十類 taxonomy 不是聲稱已被證明完備的分類定理；其用途是建立可重播、可擴充與可實驗檢驗的 target-audit vocabulary。

本文中的 Formal Conjectures 案例用於展示 corruption 類型與 proof obligation 結構；任何關於 theorem 真偽或 formalization status 的敘述應以對應來源版本為準。

