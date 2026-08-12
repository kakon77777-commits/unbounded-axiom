# 多證法與交叉驗證架構：從單一證明到 AI 原生證明晶格

**English Title:** Multi-Proof and Cross-Verification Architecture: From Single Proofs to AI-Native Proof Lattices  
**Series:** AI-Native Knowledge Expansion, Paper IV  
**Author:** Neo.K  
**Collaborator:** Aletheia (GPT-5.6 Sol)  
**Institution:** EveMissLab / 一言諾科技有限公司  
**Version:** v0.1  
**Date:** 2026-08-10

## 摘要

傳統數學知識庫通常以「命題—證明」為核心單位：一個 theorem 若已有一條被接受的 proof，主要問題似乎已經完成。然而，在 AI 原生研究系統中，單一 proof 不應被視為知識節點的終點。不同證法可以暴露不同依賴、不同中間結構、不同最小假設、不同可泛化方向；不同形式系統與不同 checker 則可以降低對單一實作、單一工具鏈與單一 proof-generation pipeline 的依賴。

本文提出「證明晶格」（Proof Lattice）作為工作模型。對命題 \(T\)，系統不只儲存一個 proof object，而是建立：

\[
\mathcal P(T)
=
\{
\Pi_1,\Pi_2,\ldots,\Pi_n,
V_1,V_2,\ldots,V_m
\},
\]

其中 \(\Pi_i\) 可以是不同推導路徑、不同表示或不同形式系統中的 proof；\(V_j\) 則可以是 kernel check、external checker、symbolic verification、finite exhaustive computation、counterexample search、axiom audit 與 statement-semantic audit。

本文區分「證明多樣性」與「驗證多樣性」，並指出：把同一 proof 在同一 kernel 中重跑十次，不構成十份獨立信任證據。真正的 cross-verification 應分析 proof-path diversity、implementation diversity、formalism diversity、assumption diversity 與 semantic independence。本文進一步提出 Proof Certificate、Verification Matrix、Shared-Dependency Graph 與 Proof Lattice Coverage 等資料結構，並提出一個可實驗的多證法生成—交叉驗證 runtime。

本文不主張多證法可以消除所有信任假設。形式系統仍依賴其邏輯、公理、checker 實作與 formal statement 是否忠實表達 intended meaning。本文的核心命題較為有限：**AI 原生數學可以把「證明是否存在」與「我們如何知道這個證明鏈值得信任」拆成兩個可計算、可審計、可擴張的研究問題。**

**關鍵詞：** 多證法；證明晶格；交叉驗證；形式化證明；proof assistant；trusted computing base；AI 原生數學；external checker；proof diversity；verification architecture

---

## 1. 一條證明夠不夠？

在古典數學實務中，只要：

\[
T
\]

已有一條正確 proof：

\[
\Pi:T,
\]

則 theorem 的真值問題通常已經完成。

在形式系統中，也可以寫成：

\[
K(\Pi,T)=\mathrm{PASS},
\]

其中 \(K\) 是 kernel。

這在邏輯上完全合理。

但 AI 原生研究系統面對的問題比「有沒有 proof」更多：

1. proof 是否依賴未注意到的 axiom？
2. formal statement 是否忠實於原始命題？
3. proof generator 是否偷加條件？
4. checker 是否存在 implementation bug？
5. 不同 proof 是否其實共享同一條脆弱 lemma？
6. 是否存在更短、更一般或更具解釋力的 proof？
7. theorem 的不同表示是否能相互轉換？
8. 一條 proof 的局部結構是否暗示新的 theorem family？

因此：

\[
\boxed{
\text{Proof Existence}
\neq
\text{Proof Trust Architecture}.
}
\]

---

## 2. 從 Proof Pair 到 Proof Lattice

傳統資料結構：

\[
(T,\Pi).
\]

本文建議改成：

\[
\boxed{
\mathfrak L(T)
=
(
T,
\mathcal P_T,
\mathcal V_T,
\mathcal A_T,
\mathcal D_T
)
}
\]

其中：

- \(\mathcal P_T\)：proof set；
- \(\mathcal V_T\)：verification set；
- \(\mathcal A_T\)：axiom / assumption dependencies；
- \(\mathcal D_T\)：shared dependency graph。

這個物件稱為：

\[
\boxed{
\text{Proof Lattice}
}
\]

作為本文的工作術語。

之所以使用 lattice 而不是 list，是因為不同 proof 之間不只是平行排列。

它們可能存在：

\[
\Pi_1\to\Pi_2,
\]

\[
\Pi_1\simeq\Pi_3,
\]

\[
\Pi_4\subset\Pi_5,
\]

或者共享某個 lemma：

\[
L^\ast.
\]

因此 proof collection 更接近帶偏序、共享依賴與轉換關係的圖結構。

---

## 3. 多證法的五種不同價值

### 3.1 錯誤隔離

若：

\[
\Pi_1,\Pi_2,\Pi_3
\]

由不同路徑推出同一 theorem，而只有 \(\Pi_1\) 依賴某個可疑 lemma：

\[
L_x,
\]

則：

\[
L_x
\]

即使失效，也未必破壞其他 proof。

### 3.2 假設比較

若：

\[
\Pi_1
\]

依賴：

\[
A,B,C,
\]

而：

\[
\Pi_2
\]

只依賴：

\[
A,B,
\]

則 \(C\) 可能不是 theorem 的必要假設，而只是第一條 proof 的技術性依賴。

### 3.3 表示橋接

幾何 proof、代數 proof、向量 proof 可能證明同一 theorem，但揭露不同結構。

因此：

\[
\text{logical equivalence}
\]

不等於：

\[
\text{explanatory equivalence}.
\]

### 3.4 泛化搜尋

某條 proof 使用的工具比原命題更一般，可能揭露：

\[
T
\hookrightarrow
T'.
\]

### 3.5 Proof Compression

如果一個 theorem 已有：

\[
|\Pi_1|=10^4
\]

步 proof，而另一條：

\[
|\Pi_2|=10^2,
\]

那麼第二條 proof 可能形成新的推理壓縮路徑。

---

## 4. 證明多樣性不等於驗證多樣性

需要區分：

\[
\boxed{
\text{Proof Diversity}
}
\]

和：

\[
\boxed{
\text{Verification Diversity}.
}
\]

例如，AI 生成三條不同 Lean proofs：

\[
\Pi^L_1,\Pi^L_2,\Pi^L_3.
\]

若全部由同一個 Lean kernel：

\[
K_L
\]

檢查，則我們擁有三條 proof path，但 checker implementation 仍只有一個。

反之，同一 proof term：

\[
\Pi
\]

可被：

\[
K_L,
K_{N_1},
K_{N_2}
\]

三個不同 checker 驗證。

這增加 checker diversity，但 proof path 仍只有一條。

因此至少要區分兩軸：

\[
D_P=\text{proof-path diversity},
\]

\[
D_V=\text{verifier diversity}.
\]

---

## 5. 更完整的五維多樣性

本文進一步定義：

\[
\boxed{
\mathbf D(T)
=
(
D_P,
D_I,
D_F,
D_A,
D_S
)
}
\]

其中：

- \(D_P\)：Proof-path diversity；
- \(D_I\)：Implementation diversity；
- \(D_F\)：Formalism diversity；
- \(D_A\)：Assumption diversity；
- \(D_S\)：Statement/representation diversity。

### Proof-path diversity

不同證明方法：

\[
\Pi_1\not\cong\Pi_2.
\]

### Implementation diversity

不同 kernel/checker implementation。

### Formalism diversity

例如：

\[
\text{Lean},
\text{Rocq},
\text{Isabelle/HOL},
\text{HOL Light}
\]

等不同 formal systems。

### Assumption diversity

不同 proof 使用不同 axiom / theorem dependency closure。

### Statement diversity

同一 informal claim 的不同 formalization 或 representation。

---

## 6. 重跑不是獨立驗證

若：

\[
K(\Pi)=PASS
\]

執行十次：

\[
K(\Pi)=PASS
\quad \times 10,
\]

它只能很好地排除某些 transient execution problems。

但若 kernel 本身存在 deterministic bug：

\[
b_K,
\]

十次都可能：

\[
PASS.
\]

因此：

\[
\boxed{
10\times\text{same checker}
\neq
10\times\text{independent verification}.
}
\]

同樣地，兩個 checker 若共用大量 source、algorithm 或 parsing pipeline，也不能被視為完全獨立。

所以系統必須維護：

\[
\text{Shared Dependency Graph}.
\]

---

## 7. Shared Dependency Graph

設所有 proof/check components 為：

\[
C=\{c_1,\ldots,c_n\}.
\]

建立：

\[
G_D=(C,E_D),
\]

若兩個 component 共用：

- kernel algorithm；
- library；
- parser；
- compiler；
- proof exporter；
- axiom base；
- generated source；
- theorem translation；

則建立 dependency edge。

因此兩個驗證器的「獨立性」不應只是：

\[
c_i\neq c_j.
\]

而要分析：

\[
\operatorname{Shared}(c_i,c_j).
\]

可以定義概念性 independence：

\[
I(c_i,c_j)
=
1-\operatorname{SharedRatio}(c_i,c_j).
\]

這不是概率，而是架構分析量。

---

## 8. Lean 的多層 proof validation

現代 Lean 已經提供一個很好的多層驗證實例。

一般使用時：

\[
\text{elaboration}
\rightarrow
\text{Lean kernel check}.
\]

更高要求可以：

\[
\text{print axioms}
\]

檢查 theorem 的 axiom dependency。

再進一步：

\[
\text{lean4checker}
\]

重新 replay `.olean` 中的 proof declarations。

而在高風險情境：

\[
\text{sandbox}
+
\text{comparator}
+
\text{external checker}.
\]

這種分層本身說明：

\[
\boxed{
\text{proof validation is threat-model dependent}.
}
\]

AI-generated proof 特別適合這個模型，因為生成器可以被視為不可信來源，而 checker 才是驗證邊界。

---

## 9. Small Kernel 與 de Bruijn Criterion

Lean 與 Rocq 都採取類似哲學：

複雜 tactic 可以產生 proof term，但最終由較小、較明確的 kernel 檢查。

抽象成：

\[
\text{Untrusted Search}
\rightarrow
\text{Proof Object}
\rightarrow
\text{Trusted Checker}.
\]

這使：

\[
\text{Generator complexity}
\]

可以很大，而：

\[
\text{verification TCB}
\]

維持較小。

因此 AI-native research runtime 可以允許：

\[
\text{very complex AI prover},
\]

只要最後仍產生：

\[
\text{independently checkable certificate}.
\]

---

## 10. Proof Lattice 的節點與邊

對 theorem \(T\)，定義：

\[
G_T=(V_T,E_T).
\]

節點可以包括：

```text
THEOREM
PROOF
LEMMA
AXIOM
FORMALIZATION
COMPUTATION
COUNTEREXAMPLE_SEARCH
CHECKER_RESULT
SEMANTIC_AUDIT
```

邊可以包括：

```text
PROVES
DEPENDS_ON
REWRITES_TO
GENERALIZES
SPECIALIZES
CHECKED_BY
TRANSLATED_TO
SHARES_DEPENDENCY
REFUTES
SEMANTICALLY_ALIGNS
```

因此：

\[
T
\]

不再只對應一份 proof file。

而是一個可追溯的 proof ecology。

---

## 11. Proof Certificate

每條 proof 建議附：

```text
proof_id
theorem_id
formal_system
proof_method
proof_term_hash
axiom_dependencies
lemma_dependencies
generator
generation_seed_or_trace
checker_results
external_checker_results
statement_hash
formalization_id
proof_length
resource_cost
status
```

其中：

\[
\text{status}
\in
\{
\text{PROVED},
\text{CHECKED},
\text{CROSS\_CHECKED},
\text{REJECTED},
\text{UNKNOWN}
\}.
\]

這些 status 不應混為一個 boolean。

---

## 12. Verification Matrix

對 theorem \(T\)，建立矩陣：

\[
M_T=(m_{ij}),
\]

其中第 \(i\) 列為 proof：

\[
\Pi_i,
\]

第 \(j\) 欄為 verifier：

\[
V_j.
\]

若：

\[
V_j(\Pi_i)=PASS,
\]

則：

\[
m_{ij}=1.
\]

否則可記：

\[
0,\ FAIL,\ UNKNOWN,\ UNSUPPORTED.
\]

例如：

\[
M_T
=
\begin{pmatrix}
1&1&1\\
1&1&0\\
1&?&1
\end{pmatrix}.
\]

這比：

```text
verified=true
```

保留更多信息。

---

## 13. Verification Coverage

定義概念性的：

\[
\boxed{
C_V(T)
=
f(
D_P,
D_I,
D_F,
D_A,
D_S
)
}
\]

作為 verification coverage。

這不是「 theorem 為真的概率」。

而是：

> 我們對 theorem 的 proof/check 結構覆蓋到了多少不同失敗模式？

例如：

- proof-path diversity 高，可以防止某條 proof-specific hidden dependency；
- implementation diversity 高，可以降低單一 checker bug 的影響；
- formalism diversity 高，可以暴露 translation / foundation assumptions；
- statement diversity 高，可以暴露 formalization mismatch。

---

## 14. 不應建立虛假的 Proof Confidence Probability

一個誘惑是定義：

\[
P(T=\text{true})=0.999999.
\]

但若沒有可靠的 probabilistic model，這種數字很容易製造虛假精確度。

因此本文建議優先輸出向量：

\[
\boxed{
\mathbf C_T
=
(
c_{\mathrm{proof}},
c_{\mathrm{checker}},
c_{\mathrm{axiom}},
c_{\mathrm{semantic}},
c_{\mathrm{replication}}
)
}
\]

而不是單一 confidence score。

系統可以說：

```text
proof_path_coverage = high
checker_diversity = medium
axiom_audit = clean
semantic_alignment = human-reviewed
cross_formalism_replication = absent
```

這比任意的：

```text
confidence = 99.97%
```

更誠實。

---

## 15. Semantic Gap：形式證明仍然可能證明錯的「意思」

形式 proof checker 回答的是：

\[
\boxed{
\text{Does this proof term inhabit this formal theorem type?}
}
\]

它不自動回答：

\[
\boxed{
\text{Does this formal theorem faithfully express the intended informal claim?}
}
\]

因此 Proof Lattice 必須增加：

\[
\text{Semantic Audit}.
\]

可以把完整鏈條寫成：

\[
I
\rightarrow
F
\rightarrow
\Pi
\rightarrow
K,
\]

其中：

- \(I\)：informal/intended claim；
- \(F\)：formal statement；
- \(\Pi\)：proof；
- \(K\)：checker。

Kernel 主要驗證：

\[
\Pi:F.
\]

但：

\[
I\leftrightarrow F
\]

仍需另外處理。

這是形式驗證最重要的邊界之一。

---

## 16. 多形式系統驗證

更強的路徑是：

\[
F_L(T)
\]

在 Lean 形式化，

\[
F_R(T)
\]

在 Rocq 形式化，

\[
F_H(T)
\]

在 HOL-family system 形式化。

分別得到：

\[
\Pi_L,\Pi_R,\Pi_H.
\]

若：

\[
K_L(\Pi_L)=PASS,
\]

\[
K_R(\Pi_R)=PASS,
\]

\[
K_H(\Pi_H)=PASS,
\]

則我們得到 cross-formalism replication。

但仍需要注意：

\[
F_L(T),
F_R(T),
F_H(T)
\]

是否真的表示相同 informal theorem。

因此多系統驗證本身也需要：

\[
\text{Statement Alignment}.
\]

---

## 17. Flyspeck 的歷史意義

Kepler conjecture 的 Flyspeck formal proof 使用 HOL Light 與 Isabelle 完成，是大型形式化數學中非常重要的多 proof-assistant 工程案例。

這不代表「同一整套 proof 被兩個系統完全獨立重做」。

它更適合說明：

\[
\boxed{
\text{large formal mathematics can be decomposed across multiple proof environments}.
}
\]

這對未來 AI-native proof lattice 有重要啟發：大型 theorem graph 不必要求全世界只使用一個 prover。

可以存在：

\[
\text{multi-system proof ecology}.
\]

---

## 18. 計算驗證也可以進入晶格

假設 theorem 可化約成有限問題：

\[
T
\iff
\bigwedge_{i=1}^{N}Q_i.
\]

那麼：

\[
\operatorname{ExhaustiveCheck}(Q_1,\ldots,Q_N)
\]

可以成為一條 proof/verification edge。

但需要保存：

1. reduction proof；
2. enumeration completeness proof；
3. program/certificate；
4. checker；
5. environment/version。

因此：

\[
\boxed{
\text{Computation}
}
\]

不必是 formal mathematics 的外部東西。

它可以是 Proof Lattice 中的一種 certified branch。

---

## 19. Numerical Testing 的位置

數值測試仍然重要，但不能標成：

\[
PROOF
\]

除非問題已被合法化約為有限 exhaustive case。

因此：

\[
\operatorname{Test}(T)=PASS
\]

應標記：

\[
\text{EVIDENCE},
\]

而不是：

\[
\text{THEOREM PROVED}.
\]

Proof Lattice 的好處正是：

\[
\text{proof},
\text{evidence},
\text{refutation search}
\]

可以共存，而不必全部壓成一個「可信度」。

---

## 20. AI Multi-Prover Architecture

可以建立：

```text
Prover-A: synthetic/algebraic
Prover-B: geometric
Prover-C: induction/search
Prover-D: SMT/CAS assisted
Formalizer-Lean
Formalizer-Rocq
CounterexampleHunter
AxiomAuditor
KernelChecker-A
ExternalChecker-B
StatementAuditor
Deduplicator
```

工作流：

\[
T
\rightarrow
\text{multi-prover generation}
\rightarrow
\text{proof canonicalization}
\rightarrow
\text{dependency extraction}
\rightarrow
\text{checker matrix}
\rightarrow
\text{semantic audit}
\rightarrow
\mathfrak L(T).
\]

---

## 21. Proof 路徑去重

AI 可能生成：

\[
1000
\]

條 proof，但其中：

\[
950
\]

條其實只是同一 proof template 的小改寫。

所以定義：

\[
\operatorname{CanProof}(\Pi).
\]

將 proof 依：

- lemma dependency；
- tactic skeleton；
- proof term structure；
- key intermediate propositions；

做 canonical clustering。

真正有價值的是：

\[
|\mathcal P_T/\sim_{\mathrm{proof}}|,
\]

而不是：

\[
|\mathcal P_T|.
\]

這與 Paper II 的 structural deduplication 完全對應。

---

## 22. Proof Novelty

可以定義 proof novelty：

\[
N_P(\Pi)
=
\alpha d_{\mathrm{lemma}}
+
\beta d_{\mathrm{structure}}
+
\gamma d_{\mathrm{representation}}
+
\delta d_{\mathrm{assumption}}.
\]

若：

\[
N_P(\Pi)\approx0,
\]

則新 proof 主要是重複。

若：

\[
N_P(\Pi)\gg0
\]

且仍成功證明同一 theorem，則可能具有較高研究價值。

---

## 23. AI 原生數學中的「證明工業化」

傳統研究：

\[
T
\rightarrow
\Pi
\rightarrow
\text{publish}.
\]

AI-native workflow 可以變成：

\[
T
\rightarrow
10^4\text{ proof candidates}
\rightarrow
10^2\text{ verified proofs}
\rightarrow
10\text{ structural proof classes}
\rightarrow
3\text{ genuinely distinct proof families}.
\]

人類最終只需要看：

\[
\operatorname{RenderHuman}(
\Pi^\ast_1,\Pi^\ast_2,\Pi^\ast_3
).
\]

因此「大量 proof」不是要求人類閱讀大量 proof。

而是讓機器利用大量 proof 建立更高信任與結構覆蓋，再將最有價值部分投影給人類。

---

## 24. 最小實驗

選擇：

\[
100
\]

個中等難度、已有 Lean formalization 的 theorem。

對每個 theorem：

### Stage 1
生成最多 100 條 proof candidates。

### Stage 2
kernel check。

### Stage 3
抽取：

- proof-term structure；
- lemma dependency；
- axiom dependency；
- proof length。

### Stage 4
proof clustering。

### Stage 5
對代表 proof 使用 external checker。

### Stage 6
挑 10 個 theorem 嘗試第二形式系統重建。

比較：

### Baseline
只保存第一條成功 proof。

### Proof-Lattice
保存多 proof family + cross-check metadata。

測：

- proof repair success；
- theorem generalization discovery；
- hidden assumption detection；
- checker bug sensitivity；
- proof compression；
- OOD theorem proving；
- human explanation quality。

---

## 25. Proof Lattice 的失敗模式

本框架自身也可能失敗。

### 25.1 偽多樣性

看似多 proof，實際共享同一路徑。

### 25.2 共通 checker bug

多個 checker 可能共享相同理論或 implementation mistake。

### 25.3 Translation mismatch

Lean theorem 與 Rocq theorem 看似同一命題，實際 formal statements 不同。

### 25.4 Axiom mismatch

不同系統使用不同 classical/choice/extensionality assumptions。

### 25.5 Library contamination

多條 proof 其實全部依賴同一個錯誤 upstream lemma。

### 25.6 Semantic mismatch

形式 statement 本身錯誤表達原問題。

因此：

\[
\boxed{
\text{More Proofs}
\neq
\text{Automatically More Trust}.
}
\]

---

## 26. 與現有工具的關係

Lean 官方的 validation guidance 已經呈現多層 validation 架構：從一般 kernel acceptance、axiom inspection、`lean4checker` replay，一直到高風險情況下的 sandboxed comparator 與 external checker。

Lean 的 kernel 被刻意保持為小型 proof-term checker，且官方明確指出存在 Rust 與 Lean 等其他重實作，可以用來 cross-check。

Lean Kernel Arena 進一步把多個 checker 放入同一測試與 benchmark 架構，使 checker diversity 本身成為可直接觀察的工程對象。

Rocq 同樣遵循 de Bruijn criterion：複雜 tactic 建立 proof term，最終由較小 kernel type-check，縮小 trusted code base。

因此本文提出的 Proof Lattice 並非要求 proof assistants 改變其基本邏輯，而是把現有「proof object + kernel + independent checker」原則提升成 AI-native knowledge graph 的資料架構。

---

## 27. 研究邊界

本文不主張：

1. 多 proof 會增加 theorem 的邏輯真值；
2. 多 checker 等同統計獨立樣本；
3. 不同 proof assistant 一定彼此獨立；
4. cross-formalism replication 可以消除 semantic mismatch；
5. formal proof 可以自動證明其公理描述現實；
6. Proof Lattice Coverage 是 theorem truth probability；
7. 所有 theorem 都值得生成大量 proof；
8. 計算驗證可以無條件取代 deductive proof；
9. human-readable proof 不再有價值。

本文只主張：

\[
\boxed{
\text{proof trust can be represented structurally rather than rhetorically}.
}
\]

---

## 28. 結論

Paper I 問：

> 如何擴張基礎知識？

Paper II 問：

> 如何區分真正不同的變種？

Paper III 問：

> 如何系統生成錯誤與反例？

Paper IV 則問：

> 一旦 theorem 被證明，為什麼研究應該停止？

本文的答案是：

\[
\boxed{
\text{one theorem}
\rightarrow
\text{many proof paths}
\rightarrow
\text{many verification paths}
\rightarrow
\text{one auditable proof lattice}.
}
\]

因此 AI-native mathematics 的基本研究物件可以從：

\[
(T,\Pi)
\]

升級成：

\[
\boxed{
\mathfrak L(T)
=
T
+
\text{Proof Families}
+
\text{Checker Matrix}
+
\text{Dependency Graph}
+
\text{Axiom Audit}
+
\text{Semantic Audit}.
}
\]

這不代表一個 theorem 需要無限重證。

真正目標是：

\[
\boxed{
\text{maximize informative verification diversity}
}
\]

而不是：

\[
\text{maximize proof count}.
\]

當 AI 能廉價產生大量 proofs 時，新的瓶頸不再只是「找得到 proof 嗎？」

而會變成：

> 哪些 proof 真正不同？  
> 哪些 checker 真正提供額外信任？  
> 哪些 proof 暴露新的結構？  
> 哪些驗證只是重複同一假設？

這就是從「證明」走向「證明工程」。

下一篇將處理：

\[
\boxed{
\text{AI-Native Research Graph and Machine-First Knowledge Objects}.
}
\]

即把前四篇的 proposition、variation、counterexample、proof lattice 統一成機器原生研究圖，正式回答：如果論文不再是主要知識本體，而只是面向人類的 rendering，AI 原生研究系統應該儲存什麼？

---

## 參考文獻

Lean Project. *Validating a Lean Proof*. Lean Language Reference.

Lean Project. *Elaboration and Compilation: The Kernel*. Lean Language Reference.

Lean Project. *Lean Kernel Arena*.

Rocq Project. *Core Language — The Rocq Prover Reference Manual*.

Hales, T. et al. (2017). *A Formal Proof of the Kepler Conjecture*. Forum of Mathematics, Pi, 5, e2.

Hales, T. (2024). *The Formal Proof of the Kepler Conjecture: a critical retrospective*. arXiv:2402.08032.
