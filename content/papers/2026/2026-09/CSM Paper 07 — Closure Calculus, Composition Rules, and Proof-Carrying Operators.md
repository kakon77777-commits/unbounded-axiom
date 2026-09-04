# CSM Paper 07 — Closure Calculus, Composition Rules, and Proof-Carrying Operators

## 閉包空間數學論：閉包演算、組合規則與證明承載算子

**English Title:** *Closure-Space Mathematics: Closure Calculus, Composition Rules, and Proof-Carrying Operators*  
**Series:** Closure-Space Mathematics (CSM)  
**Paper:** 07  
**Version:** v0.1  
**Date:** 2026-08-27  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**Language:** zh-TW  
**Status:** Formal Theory / Executable Calculus Core  
**Canonical source:** UTF-8 Markdown  
**Canonical math delimiters:** inline ` $...$ `; display `$$...$$`

---

## 摘要

本文建立閉包空間數學論（Closure-Space Mathematics, CSM）的第一版可執行演算核心。Paper 00–06 已分別建立：相對全域閉包空間、全域性型別、typed closure hypergraph、frontier / cut / exhaustion、closure dynamics、projection invariants，以及 cross-domain transfer laws。本文將這些物件進一步收斂成一套 **proof-carrying closure calculus**，使 closure operation 不再只是敘述性規則，而是具有明確輸入型別、前置條件、作用域、輸出型別、狀態轉移、證書、債務與版本的可驗證算子。

基本算子寫為：

$$
\boxed{
\mathcal O:
(X_1,\ldots,X_n;\Gamma)
\rightharpoonup
(Y_1,\ldots,Y_m;\Gamma')
}
$$

其中：

- $X_i$：輸入 closure objects；
- $\Gamma$：作用域、假設、representation、policy 與版本環境；
- $Y_j$：輸出 closure objects；
- 部分箭頭 $\rightharpoonup$ 表示 operator 可能因 type / scope / certificate / debt 不足而拒絕執行。

本文提出：

$$
\boxed{
\mathsf{PCO}
=
\langle
\mathsf{Signature},
\mathsf{Pre},
\mathsf{Transform},
\mathsf{Post},
\mathsf{Cert},
\mathsf{Debt},
\mathsf{Version}
\rangle
}
$$

稱為 **Proof-Carrying Closure Operator**。

算子在執行後不得只輸出 result，還必須輸出：

$$
\boxed{
\text{result}
+
\text{certificate}
+
\text{debt delta}
+
\text{ledger event}.
}
$$

本文建立第一版 operator family：

1. $\mathsf{Infer}$：implication closure；
2. $\mathsf{Block}$：obstruction propagation；
3. $\mathsf{Refute}$：claim-level negative closure；
4. $\mathsf{Prove}$：claim-level positive closure；
5. $\mathsf{Condition}$：conditional closure；
6. $\mathsf{Bridge}$：cross-domain / cross-representation lift；
7. $\mathsf{Project}$：native-to-view projection；
8. $\mathsf{Transfer}$：cross-domain authority transfer；
9. $\mathsf{Quotient}$：semantic / route / obstruction quotient；
10. $\mathsf{Split}$：撤銷過度 quotient；
11. $\mathsf{Reopen}$：重開；
12. $\mathsf{Discharge}$：debt 清償；
13. $\mathsf{Cut}$：cut certification；
14. $\mathsf{Cover}$：obstruction cover；
15. $\mathsf{Exhaust}$：relative exhaustion；
16. $\mathsf{Promote}$：globality / authority promotion；
17. $\mathsf{Replay}$：ledger reconstruction；
18. $\mathsf{Compile}$：runtime / graph / view compilation。

本文特別強調 closure operators 的組合不是自由的。即使：

$$
\mathcal O_1
\quad\text{與}\quad
\mathcal O_2
$$

各自合法，也不代表：

$$
\mathcal O_2\circ\mathcal O_1
$$

合法。組合需要：

$$
\boxed{
\mathsf{CompCert}(\mathcal O_1,\mathcal O_2).
}
$$

本文因此定義：

- type composability；
- scope composability；
- certificate composability；
- debt composability；
- authority monotonicity；
- version coherence；
- bridge coherence；
- projection closure-commutation；
- transfer conservation；
- reopening invalidation。

本文提出第一版 **Closure Normal Form**：

$$
\boxed{
\mathsf{CNF}
=
\mathsf{Normalize}
\to
\mathsf{Validate}
\to
\mathsf{Infer}
\to
\mathsf{Propagate}
\to
\mathsf{Resolve}
\to
\mathsf{Rebuild}
\to
\mathsf{Project}.
}
$$

其中 `Project` 預設在 native closure state 完成後執行；若採 incremental projection，必須附帶 Paper 05 所定義的 incremental materialization certificate。

本文最後定義 NS closure graph compiler 的最小 interface。NS 過去文件中的 `CLOSED`、`OPEN`、`NO-GO`、`SURVIVOR`、`STOP`、`CONDITIONAL` 不再直接變成 graph status，而要先被 parse 成 claim / assumption / scope / certificate candidates，再經 closure calculus 決定真正 status。由此，CSM 從本文開始具備直接進入 reference runtime 的形式基礎。

---

# 1. 研究定位

CSM Paper 00–06 已提供：

$$
\text{Objects}
+
\text{Graphs}
+
\text{Dynamics}
+
\text{Projection}
+
\text{Transfer}.
$$

本文新增：

$$
\boxed{
\text{Executable Closure Calculus}.
}
$$

---

# 2. Closure Judgment

定義 closure judgment：

$$
\boxed{
\Gamma
\vdash
x
:
\tau
\;[\sigma]
\;\{\chi\}
\;\langle d\rangle
}
$$

其中：

- $\Gamma$：closure environment；
- $x$：object；
- $\tau$：object type；
- $\sigma$：closure status；
- $\chi$：certificate set；
- $d$：debt set。

---

# 3. Closure Environment

$$
\boxed{
\Gamma
=
(
D,
A,
\rho,
\Gamma_R,
\mathcal T,
\mathcal B,
\mathcal P,
\nu
).
}
$$

其中：

- $D$：domain / scope；
- $A$：active assumptions；
- $\rho$：representation；
- $\Gamma_R$：route grammar；
- $\mathcal T$：theorem base；
- $\mathcal B$：bridge set；
- $\mathcal P$：policy；
- $\nu$：version。

---

# 4. Judgment Noncollapse

同一 object 在不同 $\Gamma$ 下可有不同 status：

$$
\Gamma_1\vdash x[\mathsf{OPEN}],
$$

$$
\Gamma_2\vdash x[\mathsf{BLOCKED}].
$$

因此：

$$
\boxed{
\sigma(x)
\text{ is environment-indexed}.
}
$$

---

# 5. Proof-Carrying Closure Operator

定義：

$$
\boxed{
\mathsf{PCO}
=
\langle
\mathsf{Signature},
\mathsf{Pre},
\mathsf{Transform},
\mathsf{Post},
\mathsf{Cert},
\mathsf{Debt},
\mathsf{Version}
\rangle.
}
$$

---

# 6. Operator Signature

$$
\boxed{
\mathsf{Sig}(\mathcal O)
:
(\tau_1,\ldots,\tau_n)
\to
(\tau'_1,\ldots,\tau'_m).
}
$$

---

# 7. Operator Preconditions

$$
\mathsf{Pre}(\mathcal O,\Gamma,X)
$$

至少可包含：

- type；
- scope；
- assumptions；
- target fidelity；
- bridge validity；
- certificate presence；
- representation compatibility；
- version freshness。

---

# 8. Operator Transform

$$
\mathsf{Transform}_{\mathcal O}
(X,\Gamma)
=
Y.
$$

---

# 9. Operator Postconditions

$$
\mathsf{Post}_{\mathcal O}(Y,\Gamma')
$$

定義 output 的：

- status；
- authority；
- debt；
- provenance；
- ledger event。

---

# 10. Operator Certificate

每次 theorem-level operator execution 產生：

$$
\boxed{
\chi_{\mathcal O}.
}
$$

---

# 11. Operator Debt Delta

定義：

$$
\boxed{
\Delta d_{\mathcal O}
=
d_{\rm out}
\setminus
d_{\rm in}.
}
$$

---

# 12. Operator Ledger Event

$$
e_{\mathcal O}
=
\langle
\mathcal O,
X,
Y,
\Gamma,
\Gamma',
\chi,
\Delta d,
\nu
\rangle.
$$

---

# 13. Fail-Closed Rule

若 precondition 任一 theorem-critical gate FAIL：

$$
\boxed{
\mathcal O(X)
=
\mathsf{REFUSE}.
}
$$

不得 best-effort 偷升 status。

---

# 14. Defer Rule

若資訊不足但未證非法：

$$
\boxed{
\mathcal O(X)
=
\mathsf{DEFER}
}
$$

並新增 debt。

---

# 15. Refuse 與 Defer 不同

$$
\boxed{
\mathsf{REFUSE}
\neq
\mathsf{DEFER}.
}
$$

---

# 16. Operator Family

第一版：

$$
\boxed{
\mathfrak O_{\rm calc}
=
\{
\mathsf{Infer},
\mathsf{Block},
\mathsf{Refute},
\mathsf{Prove},
\mathsf{Condition},
\mathsf{Bridge},
\mathsf{Project},
\mathsf{Transfer},
\mathsf{Quotient},
\mathsf{Split},
\mathsf{Reopen},
\mathsf{Discharge},
\mathsf{Cut},
\mathsf{Cover},
\mathsf{Exhaust},
\mathsf{Promote},
\mathsf{Replay},
\mathsf{Compile}
\}.
}
$$

---

# 17. Infer Operator

$$
\mathsf{Infer}:
(\mathsf{Claim}^n,\mathsf{Lemma})
\rightharpoonup
\mathsf{Claim}.
$$

---

# 18. Infer Preconditions

需要：

- implication certificate；
- assumptions satisfied；
- scope compatible；
- version current。

---

# 19. Infer Output

若 proof complete：

$$
\sigma=\mathsf{CLOSED}^{+}.
$$

若 assumptions 未閉：

$$
\sigma=\mathsf{CONDITIONAL}.
$$

---

# 20. Block Operator

$$
\mathsf{Block}:
(\mathsf{Obstruction},\mathsf{RouteState})
\rightharpoonup
\mathsf{RouteState}.
$$

---

# 21. Block Preconditions

需要：

$$
\mathsf{OPCert}
=
\mathsf{PASS}.
$$

---

# 22. Block Output

通常：

$$
\mathsf{OPEN}
\to
\mathsf{BLOCKED}.
$$

---

# 23. Block Cannot Refute Claim

$$
\boxed{
\mathsf{Block}
\neq
\mathsf{Refute}.
}
$$

---

# 24. Refute Operator

$$
\mathsf{Refute}:
(\mathsf{Claim},\mathsf{Counterexample/NoGoCert})
\rightharpoonup
\mathsf{Claim}.
$$

---

# 25. Refute Output

$$
\boxed{
\sigma=\mathsf{CLOSED}^{-}.
}
$$

---

# 26. Prove Operator

$$
\mathsf{Prove}:
(\mathsf{Claim},\mathsf{ProofCert})
\rightharpoonup
\mathsf{Claim}.
$$

---

# 27. Prove Output

$$
\boxed{
\sigma=\mathsf{CLOSED}^{+}.
}
$$

---

# 28. Condition Operator

$$
\mathsf{Condition}:
(\mathsf{Claim},\mathsf{AssumptionSet})
\rightharpoonup
\mathsf{Claim}.
$$

---

# 29. Condition Output

$$
\boxed{
\sigma=\mathsf{CONDITIONAL}.
}
$$

---

# 30. Bridge Operator

$$
\mathsf{Bridge}:
(x_A,\mathsf{BridgeCert}_{A\to B})
\rightharpoonup
x_B.
$$

---

# 31. Bridge Preconditions

- source object valid；
- bridge active；
- scope map valid；
- target type defined；
- loss/debt declared。

---

# 32. Bridge Output Authority

authority 由 bridge cert 決定，不由 source status 自動複製。

---

# 33. Project Operator

$$
\mathsf{Project}:
\mathfrak C^{\rm nat}
\rightharpoonup
\mathcal V.
$$

---

# 34. Project Preconditions

需要：

$$
\mathsf{ProjCert}.
$$

---

# 35. Project Cannot Upgrade Authority

$$
\boxed{
\mathsf{Authority}(\mathcal V)
\le
\mathsf{Authority}(\mathfrak C^{\rm nat}).
}
$$

---

# 36. Transfer Operator

$$
\mathsf{Transfer}:
x_A
\rightharpoonup
x_B.
$$

---

# 37. Transfer Preconditions

需要：

$$
\mathsf{TContract},
\quad
\mathsf{BridgeCert}.
$$

---

# 38. Transfer Output

可為：

- conservative；
- lossy；
- undefined。

---

# 39. Quotient Operator

$$
\mathsf{Quotient}:
(x_1,\ldots,x_n)
\rightharpoonup
[x]_\sim.
$$

---

# 40. Quotient Preconditions

需要 equivalence evidence。

---

# 41. Quotient No-Go

embedding / lexical similarity 不足以執行 theorem-level quotient。

---

# 42. Split Operator

$$
\mathsf{Split}:
[x]_\sim
\rightharpoonup
(x_1,\ldots,x_n).
$$

---

# 43. Split Trigger

- false equivalence；
- assumption divergence；
- scope divergence；
- representation semantic divergence。

---

# 44. Split Output

通常觸發：

$$
\text{frontier rebuild}.
$$

---

# 45. Reopen Operator

$$
\mathsf{Reopen}:
(\mathsf{Blocked/ClosedObject},\mathsf{ReopenCert})
\rightharpoonup
\mathsf{ReopenedObject}.
$$

---

# 46. Reopen Preconditions

需要 invalidated premise / bridge / theorem / scope。

---

# 47. Reopen Output

$$
\boxed{
\sigma=\mathsf{REOPENED}.
}
$$

---

# 48. Discharge Operator

$$
\mathsf{Discharge}:
(d,\chi_d)
\rightharpoonup
\varnothing.
$$

---

# 49. Discharge Preconditions

debt-specific certificate。

---

# 50. Discharge Cascade

清償 parent debt 可能使 downstream CONDITIONAL 升 CLOSED。

---

# 51. Cut Operator

$$
\mathsf{Cut}:
(\mathcal R,C)
\rightharpoonup
\mathsf{CutCert}.
$$

---

# 52. Cut Preconditions

route grammar + route completeness scope 必明確。

---

# 53. Cover Operator

$$
\mathsf{Cover}:
(\mathcal R,\mathcal O)
\rightharpoonup
\mathsf{CoverCert}.
$$

---

# 54. Exhaust Operator

$$
\mathsf{Exhaust}:
(
\mathsf{RCCert},
\mathsf{CutCert},
\mathsf{CoverCert}
)
\rightharpoonup
\mathsf{RECert}.
$$

---

# 55. Exhaust Preconditions

不得有 uncovered admissible route。

---

# 56. Exhaust Output

只產生 relative exhaustion level。

---

# 57. Promote Operator

$$
\mathsf{Promote}:
(
x_{D_0},
\mathsf{PromotionCert}_{D_0\to D_1}
)
\rightharpoonup
x_{D_1}.
$$

---

# 58. Promote Preconditions

- quantifier lift；
- scope；
- uniformity；
- representation；
- bridge；
- debt。

---

# 59. Promote No-Go

$$
\boxed{
\text{local theorem}
\not\Rightarrow
\text{global theorem}.
}
$$

---

# 60. Replay Operator

$$
\mathsf{Replay}:
(\mathsf{Ledger},\mathsf{Policy})
\to
\mathfrak C.
$$

---

# 61. Replay Determinism

固定 ledger + policy 下應 deterministic。

---

# 62. Compile Operator

$$
\mathsf{Compile}:
\mathfrak C
\rightharpoonup
\mathsf{RuntimeArtifact}.
$$

---

# 63. Compile Preconditions

需 projection / serialization contract。

---

# 64. Compile Authority

runtime artifact authority 不得超過 source state。

---

# 65. Composition

令：

$$
\mathcal O_1:
A\rightharpoonup B,
$$

$$
\mathcal O_2:
B\rightharpoonup C.
$$

形式上可寫：

$$
\mathcal O_2\circ\mathcal O_1.
$$

---

# 66. Type Composability

需要：

$$
\operatorname{cod}(\mathcal O_1)
\subseteq
\operatorname{dom}(\mathcal O_2).
$$

---

# 67. Scope Composability

$$
\Gamma_1'
$$

必滿足 $\mathcal O_2$ 的 scope preconditions。

---

# 68. Certificate Composability

 $\chi_1$ 若是 $\mathcal O_2$ prerequisite，必可驗證。

---

# 69. Debt Composability

若 $\mathcal O_1$ 產生 unresolved debt， $\mathcal O_2$ 不得假裝 debt-free。

---

# 70. Version Composability

兩 operator 必在 compatible versions 上執行。

---

# 71. Authority Composability

下游 operator 不得無證提升 upstream authority。

---

# 72. Composition Certificate

$$
\boxed{
\mathsf{CompCert}(
\mathcal O_1,\mathcal O_2
).
}
$$

---

# 73. Composition Failure

如果任一：

- type；
- scope；
- cert；
- debt；
- version；
- authority；

不相容：

$$
\boxed{
\mathcal O_2\circ\mathcal O_1
=
\mathsf{REFUSE}.
}
$$

---

# 74. Associativity Warning

即使三個 operator pairwise composable，也不自動保證：

$$
(\mathcal O_3\circ\mathcal O_2)\circ\mathcal O_1
=
\mathcal O_3\circ(\mathcal O_2\circ\mathcal O_1).
$$

---

# 75. Associativity Debt

如果 composition 會引入不同 intermediate debt / scope，需：

$$
\mathsf{AssocCert}.
$$

---

# 76. Commutation

若：

$$
\mathcal O_1\mathcal O_2
=
\mathcal O_2\mathcal O_1,
$$

稱 commute。

---

# 77. Noncommuting Operator Pair

典型：

$$
\mathsf{Quotient}
$$

與：

$$
\mathsf{Block}
$$

可能不交換。

---

# 78. Reopen–Project Noncommutation

如果 view 未支援 invalidation：

$$
\mathsf{Project}\circ\mathsf{Reopen}
\neq
\mathsf{Reopen}^{\Pi}\circ\mathsf{Project}.
$$

---

# 79. Transfer–Refute Noncommutation

source refutation 不一定可 transfer 到 target。

---

# 80. Operator Authority Order

定義：

$$
\mathcal O_1
\preceq_{\rm auth}
\mathcal O_2
$$

若 $\mathcal O_2$ 可產生較高 authority output。

---

# 81. Authority Inflation No-Go

operator composition 不得憑空提升：

$$
\boxed{
A_{\rm out}
>
\max A_{\rm input}
}
$$

除非 composition 中包含新的 theorem / promotion cert。

---

# 82. Proof-Carrying Composition

合法 composition 必輸出 composite cert：

$$
\boxed{
\chi_{2\circ1}.
}
$$

---

# 83. Composite Debt

$$
\boxed{
d_{2\circ1}
=
\mathsf{Map}(d_1)
\cup
d_2
\cup
d_{\rm comp}.
}
$$

---

# 84. Operator Normalization

同一 closure effect 可能由多條 operator sequence 產生。

需要 normalization。

---

# 85. Closure Normal Form

第一版：

$$
\boxed{
\mathsf{CNF}
=
\mathsf{Normalize}
\to
\mathsf{Validate}
\to
\mathsf{Infer}
\to
\mathsf{Propagate}
\to
\mathsf{Resolve}
\to
\mathsf{Rebuild}
\to
\mathsf{Project}.
}
$$

---

# 86. Normalize Phase

執行：

- canonical identity；
- scope normalization；
- assumption normalization；
- representation normalization；
- quotient candidates。

---

# 87. Validate Phase

驗證：

- certs；
- theorem status；
- versions；
- bridge；
- provenance。

---

# 88. Infer Phase

執行 implication / conditional theorem inference。

---

# 89. Propagate Phase

執行 obstruction / bridge / debt propagation。

---

# 90. Resolve Phase

處理：

- prove；
- refute；
- block；
- discharge；
- reopen；
- split / merge。

---

# 91. Rebuild Phase

重建：

- frontier；
- cuts；
- covers；
- exhaustion；
- fixed-point candidates。

---

# 92. Project Phase

依用途生成：

- audit；
- research；
- visual；
- execution view。

---

# 93. CNF 不要求唯一

不同合法 schedules 可能同樣得到 closure-equivalent state。

---

# 94. CNF Goal

目的不是 theorem proof normal form。

而是 runtime state transition 的 canonical discipline。

---

# 95. Proof-Carrying Operator Graph

每個 runtime operation 本身也形成 graph：

$$
\boxed{
\mathcal G_{\rm op}.
}
$$

---

# 96. Operator Node

節點是 operator instance：

$$
o_i.
$$

---

# 97. Operator Edge

若 output of $o_i$ 是 input of $o_j$：

$$
o_i\to o_j.
$$

---

# 98. Operator DAG

單次 closure transaction 理想上應可形成 DAG。

---

# 99. Operator Cycle

如果存在 replay / reopen / split，可跨 transaction 形成 cycle。

---

# 100. Transaction

定義：

$$
\boxed{
\mathsf{ClosureTxn}
}
$$

為一組 atomic closure operations。

---

# 101. Transaction Preconditions

- version head；
- policy；
- input hashes；
- cert availability。

---

# 102. Transaction Commit

成功：

$$
\mathsf{COMMIT}.
$$

失敗：

$$
\mathsf{ABORT}.
$$

---

# 103. Partial Commit No-Go

theorem-level status mutation 不允許無記錄 partial commit。

---

# 104. Transaction Ledger

每次 transaction 產生：

- input state hash；
- event list；
- output state hash；
- cert list；
- debt delta。

---

# 105. Idempotence

某些 operator 應滿足：

$$
\mathcal O(\mathcal O(x))
=
\mathcal O(x).
$$

例如已正規化 Normalize。

---

# 106. Non-Idempotent Operators

Reopen / Transfer / Promote 未必 idempotent。

---

# 107. Idempotence Certificate

runtime 可標記 operator 是否：

- idempotent；
- monotone；
- reversible；
- lossy。

---

# 108. Monotone Operator

對固定 environment：

$$
X\preceq Y
\Rightarrow
\mathcal O(X)\preceq\mathcal O(Y).
$$

不假設全部 operator monotone。

---

# 109. Reversible Operator

若有 verified inverse：

$$
\mathcal O^{-1}.
$$

---

# 110. Lossy Operator

Projection / Transfer 可 lossy。

---

# 111. Operator Effect Type

$$
\mathsf{Effect}
\in
\{
\mathsf{READ},
\mathsf{STATUS},
\mathsf{GRAPH},
\mathsf{DEBT},
\mathsf{SCOPE},
\mathsf{VERSION},
\mathsf{VIEW}
\}.
$$

---

# 112. Read-Only Operator

例如 query / inspect。

---

# 113. Mutating Operator

例如 Refute / Reopen / Quotient。

---

# 114. Mutation Authority

mutating operator 必有 authority level。

---

# 115. Operator Capability Boundary

runtime 不應讓 visualization operator 改 native theorem status。

---

# 116. Proof-Carrying Mutation

每次 native status mutation：

$$
\boxed{
\text{mutation}
+
\text{cert}
+
\text{ledger}
}
$$

不可分。

---

# 117. Closure Query Calculus

除了 mutation，也定義 query：

$$
\mathsf{Query}_{\rm Cl}.
$$

---

# 118. Query Types

- status；
- frontier；
- cut membership；
- obstruction coverage；
- debt；
- transferability；
- replay history。

---

# 119. Query Authority

query result 必標 native / projected source。

---

# 120. Query on Projection

如果 query 超出 projection authority：

$$
\boxed{
\mathsf{REFUSE}.
}
$$

---

# 121. Proof-Carrying Refusal

refusal 也可附：

- missing invariant；
- missing cert；
- missing scope；
- required rehydration。

---

# 122. Closure Exception

若 operator 遇到未分類 case：

$$
\mathsf{UNKNOWN}.
$$

不要自動 BLOCKED。

---

# 123. UNKNOWN vs DEFER

UNKNOWN 表示 semantic status 不明。

DEFER 表示目前 execution 缺資訊。

---

# 124. Runtime Status Lattice

可用 operational partial order：

$$
\mathsf{UNKNOWN},
\mathsf{OPEN},
\mathsf{CONDITIONAL},
\mathsf{BLOCKED},
\mathsf{REOPENED},
\mathsf{CLOSED}^{+},
\mathsf{CLOSED}^{-},
\mathsf{STALE}.
$$

本文不主張它是單一線性 lattice。

---

# 125. Status Transition Table

合法例：

$$
\mathsf{OPEN}
\to
\mathsf{BLOCKED},
$$

$$
\mathsf{BLOCKED}
\to
\mathsf{REOPENED},
$$

$$
\mathsf{CONDITIONAL}
\to
\mathsf{CLOSED}^{+},
$$

$$
\mathsf{CLOSED}^{+}
\to
\mathsf{STALE}.
$$

---

# 126. Illegal Direct Transition

例如：

$$
\mathsf{BLOCKED}
\to
\mathsf{CLOSED}^{-}
$$

沒有 RefuteCert 時非法。

---

# 127. Transition Certificate

每個 status transition 都有：

$$
\boxed{
\mathsf{StatusTransCert}.
}
$$

---

# 128. Debt-Carrying Status

同一 status 可有不同 debt：

$$
\mathsf{CONDITIONAL}\langle d_1\rangle,
$$

$$
\mathsf{CONDITIONAL}\langle d_2\rangle.
$$

---

# 129. Certificate Stack

輸出 theorem-level closure 需：

$$
\boxed{
\mathsf{CertStack}
}
$$

---

# 130. CertStack Example

$$
\mathsf{StatementCert}
+
\mathsf{ScopeCert}
+
\mathsf{ProofCert}
+
\mathsf{BridgeCert}
+
\mathsf{VersionCert}.
$$

---

# 131. Certificate Minimality

不必每次附全 corpus。

但需要可追溯 refs。

---

# 132. Proof-Carrying Reference

certificate 可是：

- proof object；
- theorem reference；
- validation artifact；
- executable check；
- hash-locked source。

---

# 133. Runtime Trust Model

CSM runtime 不自行把自然語言 claim 當 theorem。

---

# 134. Source Extraction Boundary

自然語言 artifact 先經：

$$
\mathsf{Extract}
$$

產生 candidate objects。

---

# 135. Extract Operator

$$
\mathsf{Extract}:
\mathsf{Artifact}
\rightharpoonup
\mathsf{CandidateGraph}.
$$

---

# 136. Candidate Status

extract output 預設：

$$
\mathsf{UNVERIFIED}.
$$

---

# 137. Candidate-to-Native Promotion

需要：

$$
\mathsf{Validate}.
$$

---

# 138. NS Document Compiler

對 NS 文件：

$$
\boxed{
\mathsf{NSCompile}
:
\mathsf{PaperArtifact}
\rightharpoonup
\mathsf{ClosureCandidateGraph}.
}
$$

---

# 139. NS Label Parsing

原始：

`CLOSED`

不得直接變：

$$
\mathsf{CLOSED}^{+}.
$$

---

# 140. NS CLOSED Candidate

先生成：

$$
\mathsf{StatusCandidate}(\texttt{CLOSED}).
$$

---

# 141. NS NO-GO Candidate

先生成：

$$
\mathsf{ObstructionCandidate}.
$$

---

# 142. NS SURVIVOR Candidate

先生成：

$$
\mathsf{RouteStateCandidate}.
$$

---

# 143. NS STOP Candidate

先生成：

$$
\mathsf{FrontierCandidate}.
$$

---

# 144. NS OPEN Candidate

先生成：

$$
\mathsf{OpenClaimCandidate}.
$$

---

# 145. NS Validation Pass

再抽取：

- statement；
- assumptions；
- scope；
- theorem source；
- proof/check；
- dependencies；
- version。

---

# 146. NS Closure Promotion

只有 validation 後才執行：

$$
\mathsf{Prove},
\mathsf{Block},
\mathsf{Refute},
\mathsf{Condition}.
$$

---

# 147. NS Cross-Series Composition

例如：

$$
\mathsf{Extract}_{\rm X72}
\to
\mathsf{Normalize}
\to
\mathsf{Transfer}_{\rm X72\to DCRP}
\to
\mathsf{Block}.
$$

每一步都需 cert。

---

# 148. NS False Merge Prevention

若 transfer cert 不足：

$$
\mathsf{Quotient}
=
\mathsf{REFUSE}.
$$

---

# 149. NS Runtime Transaction

一篇新 paper 進入：

$$
\boxed{
\mathsf{Ingest}
\to
\mathsf{Extract}
\to
\mathsf{Normalize}
\to
\mathsf{Validate}
\to
\mathsf{ApplyClosure}
\to
\mathsf{Rebuild}
\to
\mathsf{Snapshot}.
}
$$

---

# 150. NS Snapshot

輸出：

- native graph hash；
- frontier；
- active obstructions；
- survivors；
- debt；
- cuts；
- exhaustion level；
- version。

---

# 151. NS View Compile

再：

$$
\mathsf{Project}
$$

生成：

- overview；
- audit；
- frontier；
- obstruction；
- survivor views。

---

# 152. Runtime Proof Boundary

graph mining / clustering / LLM extraction 不具有 theorem mutation authority。

---

# 153. Human/AI Audit Boundary

某些 Cert 可由：

- theorem prover；
- symbolic checker；
- independent audit；
- human review；

提供。

---

# 154. Mixed Verification

不同 cert source 可組合，但需 provenance。

---

# 155. Machine Schema — Operator

```yaml
closure_operator:
  operator_id:
  operator_type:
  input_types: []
  output_types: []
  preconditions: []
  scope_requirements: []
  certificate_requirements: []
  debt_behavior:
  authority_effect:
  version:
```

---

# 156. Machine Schema — Operator Instance

```yaml
operator_instance:
  instance_id:
  operator_id:
  input_object_ids: []
  environment_id:
  precondition_results: {}
  output_object_ids: []
  output_statuses: {}
  certificate_ids: []
  debt_added: []
  debt_discharged: []
  ledger_event_id:
  result:
```

---

# 157. Machine Schema — Composition

```yaml
operator_composition:
  composition_id:
  operator_instances: []
  type_compatible:
  scope_compatible:
  certificate_compatible:
  debt_compatible:
  version_compatible:
  authority_compatible:
  composition_certificate:
  result:
```

---

# 158. Machine Schema — Closure Transaction

```yaml
closure_transaction:
  txn_id:
  input_state_hash:
  policy_id:
  version:
  operator_instances: []
  certificate_ids: []
  debt_delta:
  output_state_hash:
  commit_status:
```

---

# 159. Machine Schema — NS Compiler

```yaml
ns_closure_compiler:
  artifact_ref:
  extracted_claims: []
  extracted_assumptions: []
  extracted_scopes: []
  extracted_dependencies: []
  label_candidates: []
  certificate_candidates: []
  normalization_status:
  validation_status:
  closure_operator_plan: []
  native_graph_delta:
```

---

# 160. Validation Scenario A — Block is not Refute

Input obstruction + route。

expected:

$$
\mathsf{OPEN}\to\mathsf{BLOCKED},
$$

parent claim unchanged。

---

# 161. Validation Scenario B — Refute requires counterexample/no-go cert

No cert。

expected: REFUSE。

---

# 162. Validation Scenario C — Conditional to Proven

Debt discharge satisfies assumptions。

expected: CONDITIONAL -> CLOSED_POSITIVE。

---

# 163. Validation Scenario D — Invalid composition

Project visual-only view then Refute on view。

expected: composition REFUSE。

---

# 164. Validation Scenario E — Valid projection composition

Audit projection with proof-fidelity cert then read-only query。

expected: PASS。

---

# 165. Validation Scenario F — Transfer authority downgrade

Lossy transfer theorem source to broader target。

expected: authority lowered + debt added。

---

# 166. Validation Scenario G — Reopen stale downstream

Invalidated common premise。

expected: Reopen + rebuild frontier。

---

# 167. Validation Scenario H — Quotient then split

False equivalence discovered。

expected: split + restore histories + frontier rebuild。

---

# 168. Validation Scenario I — Exhaust relative only

RCCert/Cut/Cover PASS。

expected: relative exhaustion cert, not absolute claim proof without parent bridge。

---

# 169. Validation Scenario J — NS NO-GO parsing

Document says NO-GO。

expected: obstruction candidate, not native CLOSED_NEGATIVE。

---

# 170. Validation Scenario K — NS STOP parsing

Document says STOP-D105。

expected: frontier candidate。

---

# 171. Validation Scenario L — Authority inflation cycle

ANALOGY -> STRUCTURE -> THEOREM without new cert。

expected: FAIL.

---

# 172. Core No-Go 1

$$
\boxed{
\text{operator exists}
\not\Rightarrow
\text{operator application legal}.
}
$$

---

# 173. Core No-Go 2

$$
\boxed{
\text{two legal operators}
\not\Rightarrow
\text{legal composition}.
}
$$

---

# 174. Core No-Go 3

$$
\boxed{
\text{composition path}
\not\Rightarrow
\text{associative composition}.
}
$$

---

# 175. Core No-Go 4

$$
\boxed{
\text{result}
\not\Rightarrow
\text{certified result}.
}
$$

---

# 176. Core No-Go 5

$$
\boxed{
\text{same output status}
\not\Rightarrow
\text{same certificate strength}.
}
$$

---

# 177. Core No-Go 6

$$
\boxed{
\text{runtime success}
\not\Rightarrow
\text{mathematical theorem}.
}
$$

---

# 178. Core No-Go 7

$$
\boxed{
\text{compiled graph}
\not\Rightarrow
\text{canonical native truth}.
}
$$

---

# 179. Core No-Go 8

$$
\boxed{
\text{automatic extraction}
\not\Rightarrow
\text{automatic theorem status}.
}
$$

---

# 180. Paper 07 核心命題一

## Proof-Carrying Operator Principle

任何 theorem-level closure mutation 都必須由 proof-carrying operator 執行；其輸出至少包含 result、certificate、debt delta 與 ledger event。

---

# 181. Paper 07 核心命題二

## Composition Safety Principle

合法 operator composition 需要 type、scope、certificate、debt、version 與 authority 六類 compatibility 同時通過。

---

# 182. Paper 07 核心命題三

## Authority Noninflation Principle

沒有新 theorem / promotion certificate 的 operator composition，不得增加 closure authority。

---

# 183. Paper 07 核心命題四

## Fail-Closed Mutation Principle

theorem-critical precondition 失敗時，runtime 必須拒絕 native status mutation，而不是 best-effort 繼續。

---

# 184. Paper 07 核心命題五

## Closure Normal Form Principle

對大多數 artifact-driven closure update，可優先採：

$$
\mathsf{Normalize}
\to
\mathsf{Validate}
\to
\mathsf{Infer}
\to
\mathsf{Propagate}
\to
\mathsf{Resolve}
\to
\mathsf{Rebuild}
\to
\mathsf{Project}.
$$

---

# 185. Paper 07 核心命題六

## Candidate-to-Native Firewall

任何從自然語言、圖像、LLM extraction 或 heuristic mining 得到的 object，預設只能進 Candidate Layer；只有通過 validation / certificate gate 才能進 Native Closure Layer。

---

# 186. Paper 07 核心命題七

## NS Compiler Safety Principle

NS 過去文件中的 `CLOSED / OPEN / NO-GO / SURVIVOR / STOP / CONDITIONAL` 皆必須先編譯成候選物件，不得直接控制 native theorem status。

---

# 187. 與 Paper 00–06 的整合

Paper 00：
- closure object model。

Paper 01：
- scope / globality types。

Paper 02：
- graph / obstruction / reopening。

Paper 03：
- frontier / cut / exhaustion。

Paper 04：
- event dynamics / replay。

Paper 05：
- projection / attention / compilation。

Paper 06：
- cross-domain transfer / authority。

Paper 07：
- proof-carrying executable calculus。

---

# 188. Reference Runtime Boundary

從本文開始，理論已足以設計：

$$
\boxed{
\textbf{CSM Reference Runtime v0.1}
}
$$

但 runtime 尚未在本文實作。

---

# 189. Runtime MVP 最小能力

1. parse canonical records；
2. validate type signatures；
3. store native graph；
4. execute PCOs；
5. maintain status ledger；
6. propagate obstruction；
7. reopen stale routes；
8. calculate frontier；
9. build cuts/covers；
10. track debt；
11. transfer / project；
12. replay；
13. export snapshots。

---

# 190. NS Runtime MVP

NS 可作第一個大型 dataset。

但先建立：

$$
\boxed{
\text{NS Relative-Global Closure Graph v0.1}
}
$$

再做 theorem automation。

---

# 191. Paper 08 路線

下一篇應處理：

$$
\boxed{
\textbf{Closure-Space Runtime Semantics and Executable Reference Model}
}
$$

內容：

- machine state；
- transition system；
- deterministic replay；
- transaction semantics；
- certificate registry；
- debt registry；
- graph storage；
- query language；
- compiler interfaces；
- NS ingestion profile；
- conformance tests。

---

# 192. 結論

CSM 到 Paper 06 為止，已經有完整的理論物件，但仍可能停留在：

> 我們知道 closure 應該怎麼運作。

Paper 07 的目標是把它轉成：

> 系統究竟允許哪個 operator 在什麼前提下改變哪個 closure status。

因此本文的核心不是新增更多術語，而是建立：

$$
\boxed{
\text{typed inputs}
+
\text{preconditions}
+
\text{operator effect}
+
\text{certificate}
+
\text{debt}
+
\text{ledger}.
}
$$

最重要的安全原則為：

$$
\boxed{
\text{no proof-carrying certificate}
\Rightarrow
\text{no theorem-level mutation}.
}
$$

以及：

$$
\boxed{
\text{two legal steps}
\not\Rightarrow
\text{one legal composition}.
}
$$

這使 closure space 不再只是圖，而開始成為可以被執行、驗證、拒絕、回放與編譯的數學運算系統。

對 NS 而言，這也是非常關鍵的一步：過去幾百篇研究稿中的各種 status label，不再直接支配我們的判斷，而先被抽取、正規化、驗證，再由 closure calculus 決定它真正能封哪一條路、在哪個 scope 下有效、能否跨 series 傳遞、是否還有 debt，以及何時應該 reopening。

這就是從：

$$
\boxed{
\text{研究文獻堆}
}
$$

真正走向：

$$
\boxed{
\text{可執行相對全域閉包空間}.
}
$$

---

## 附錄 A — Paper 07 核心不變量

1. theorem-level mutation 必須 proof-carrying；
2. operator application 必須通過 precondition；
3. operator composition 必須有 CompCert；
4. debt 不得在 composition 中消失；
5. authority 不得無證膨脹；
6. Block 不等於 Refute；
7. Project 不得提升 native authority；
8. Transfer 不得自動複製 source status；
9. Quotient 必須有 equivalence evidence；
10. Split 必須可恢復 search history；
11. Reopen 必須有 invalidated-condition evidence；
12. Exhaust 只能產生 relative exhaustion；
13. Promote 必須有 globality / authority cert；
14. Candidate layer 不得直接修改 Native Closure Layer；
15. runtime success 不等於 theorem proof。

---

## 附錄 B — 系列依賴

### Paper 00
Relative-Global Closure Space

### Paper 01
Scope / Globality Typing

### Paper 02
Typed Closure Graph / Obstruction

### Paper 03
Frontier / Cut / Exhaustion

### Paper 04
Closure Dynamics / Replay / Reopening

### Paper 05
Projection / Attention / Compilation

### Paper 06
Cross-Domain Transfer / Authority Conservation

### Paper 07
Proof-Carrying Closure Calculus / Composition / Runtime Semantics Interface

---

**END OF CSM PAPER 07 v0.1**
