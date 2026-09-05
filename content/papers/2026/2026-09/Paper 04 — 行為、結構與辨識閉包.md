# Paper 04 — 行為、結構與辨識閉包

## Behavioral, Structural, and Discriminative Closure

**系列：** TDD × MSSP Architecture Backtrace and Fresh Reconstruction  
**系列代號：** ABFR Series  
**文件版本：** v0.1  
**日期：** 2026-08-28  
**作者：** Neo.K / EveMissLab  

---

## 摘要

Paper 01 將 TDD 的 Behavioral Closure 與 Architecture-Level Revalidation 區分；Paper 02 提出 MSSP 可作為 AI Structural Attention Substrate；Paper 03 則正式定義 Architecture Backtrace、Minimal Sufficient Reconstruction Set、Freshness Contract 與 Replay Equivalence。前三篇仍留下最後一個關鍵問題：即使所有檢查都顯示綠燈，我們如何知道檢查器本身真的具有辨識能力？

本文提出 **Discriminative Closure（辨識閉包）**，將「驗證器能否被證明會失敗」提升為 ABFR 的第三層 closure。最弱版本的辨識要求可以寫成：

$$
\begin{aligned}
\text{canonical state} &\rightarrow PASS\\
\text{known violating state} &\rightarrow FAIL
\end{aligned}
$$

然而 MSSP 的後續實驗顯示，這仍不足夠。一個檢查可以在某些情況下失敗，卻實際辨識的是錯誤變量；一個 probe 可以有多個 failure case，但它們全部只是同一語義反例的複本；一個曾經有效的 falsifying witness 可以在 validator 改版後消失，而整體檢查仍然保持「可被證偽」；一個單一 writer 的 concurrency test 即使寫再多 assertion，也根本產不出 lost-update 所需要的 failure schedule。這些案例共同指出：

$$
\boxed{
\text{Can Fail}
\not\Rightarrow
\text{Can Discriminate the Intended Claim}
}
$$

因此本文把 Discriminative Closure 分解為五個候選條件：**Falsifying-Witness Closure、Axis Binding、Witness Reachability、Witness Continuity 與 Authorized-Equivalence Preservation**。每一個可驗證 architecture clause 都必須具有具名的 falsifying witnesses；這些 witnesses 必須真正改變 claim 所依賴的語義軸、實際走到欲驗證的執行路徑；validator revision 不得靜默遺失原有反例；而語義上等價或被明確授權的替代狀態，不應被錯誤拒絕。

本文明確區分 ABFR Discriminative Closure 與 mutation testing。Mutation testing 透過系統性程式變異評估 test suite 是否能殺死 fault-like mutants，是成熟且重要的 fault-based testing 技術；equivalent mutant problem 也提醒我們，不是所有 mutation 都應該被殺死。ABFR 借用「以變異證明檢查器有能力分辨」的基本思想，但 attack object 不只可以是程式碼，也可以是架構宣告、權限、evidence binding、dependency relation、state provenance、reconstruction material、freshness contract 或 replay equivalence。其目標不是產生一個更高 mutation score，而是證明每一條 architecture claim 的 validator 對相關語義差異具有可追蹤、可維持的辨識能力。

本文最終提出三閉包工程 gate：

$$
\boxed{
C_{\text{engineering}}
=
C_B
\land
C_S
\land
C_D
}
$$

並將其展開為可執行的 ABFR+Attack workflow，為下一篇 Cross-Agent Reproducibility 與後續 Spec A / Spec B 提供完整驗證語言。

**關鍵詞：** Mutation Testing；Falsification；Discriminative Closure；TDD；MSSP；ABFR；Architecture Validation；Negative Testing；Metamorphic Testing；Falsifying Witness；Architecture Replay；AI Coding Agent

---

# 1. 最後一個綠燈問題

前三篇已經建立：

$$
C_B
=
\text{Behavioral Closure}
$$

以及：

$$
C_S
=
\text{Structural Reconstruction Closure}
$$

其中 Paper 03 將：

$$
C_S
$$

展開為：

$$
C_S
=
C_{BT}
\land
C_{\text{MSRS}}
\land
C_F
\land
C_R
$$

但即使：

$$
C_B=1
$$

且：

$$
C_S=1
$$

仍然可能存在一種最危險的假象：

> 所有 validator 都是綠的，但其中部分 validator 根本沒有辨識到自己聲稱要保護的東西。

最極端的例子是一個永遠回傳：

```text
PASS
```

的檢查。

它可以讓：

$$
100\%
$$

的正常案例通過。

但它的資訊價值為：

$$
0
$$

因為：

$$
\forall x,
\quad
V(x)=PASS
$$

所以本文的第一條命題是：

$$
\boxed{
\text{Positive Success Alone Is Not Validation Evidence}
}
$$

---

# 2. 從 MSSP 的「要會失敗」開始

MSSP 的實作工作區後來建立了一條非常直接的規則：

> 每一條檢查都要被證明「會失敗」。

其方法不是只寫更多 assertion，而是為 probe 明確列出：

$$
\text{ATTACK}
$$

也就是：

> 改哪裡會讓它變紅？

這個規則抓出過一種非常實際的失敗：作者宣稱某個缺陷存在，但把那個缺陷重新注入後，probe 仍然維持綠色。換句話說，原先的「驗證」沒有能力辨認被宣稱的錯誤。

因此最初可以定義：

$$
C_{\text{failability}}
=
1
$$

若存在至少一個：

$$
x^-
$$

使：

$$
V(x^-)=FAIL
$$

這比永遠綠燈明顯更好。

但 MSSP 後續實驗再次指出：

$$
\boxed{
C_{\text{failability}}
\neq
C_D
}
$$

也就是「會失敗」仍不等於「具有正確辨識能力」。

---

# 3. 會失敗，但失敗在錯的軸

考慮一個 claim：

$$
c:
\text{Evidence must belong to the current event}
$$

假設 validator 讀的是：

$$
\text{evidence exists?}
$$

它確實可能有兩個結果：

$$
\{PASS,FAIL\}
$$

所以它不是 constant validator。

但是 claim 真正需要辨識的軸是：

$$
\text{which event is this evidence about?}
$$

這兩個軸不同。

因此可能：

$$
\operatorname{Axis}(V)
\neq
\operatorname{Axis}(c)
$$

即使：

$$
\exists x,y:
V(x)\neq V(y)
$$

仍然不能證明：

$$
V
$$

驗證了：

$$
c
$$

所以第二條基本命題是：

$$
\boxed{
\text{Output Variation}
\not\Rightarrow
\text{Claim-Relevant Discrimination}
}
$$

---

# 4. 甚至有兩個「關於什麼」

MSSP 的 evidence 實驗又把問題拆成兩個不同軸：

$$
\operatorname{about}(e)
$$

表示：

> 這份 evidence 是關於哪一次事件？

以及：

$$
\operatorname{subject}(e)
$$

表示：

> 這份 evidence 是關於哪一個對象？

一份 evidence 可以：

- 很新鮮；
- 內容正確；
- 真的是某次 observation；

但仍然：

$$
\operatorname{about}(e)\neq current\_event
$$

或：

$$
\operatorname{subject}(e)\neq current\_subject
$$

若 validator 只綁其中一個軸，另一個錯誤仍可能通過。

因此：

$$
\boxed{
\text{Fresh}
\neq
\text{Relevant}
}
$$

而：

$$
\boxed{
\text{Relevant to the event}
\neq
\text{Relevant to the subject}
}
$$

這說明 Discriminative Closure 必須能描述 claim dimensions，而不能只問 validator 是否有過 FAIL。

---

# 5. 具名反例，而不是漂亮的數量

另一個 MSSP 實驗提出：

$$
\text{discrimination delta}
$$

原始直覺是：

> 一條 clause 有多少 observation 能讓它失敗？

但這個數字可以被 duplicate fixture 灌高。

假設只有一個語義反例：

$$
w_1
$$

把它複製十次：

$$
w_1^{(1)},\ldots,w_1^{(10)}
$$

raw count 變成：

$$
10
$$

但 distinct semantic case 仍然只有：

$$
1
$$

因此：

$$
\boxed{
\text{Raw Failure Count}
\not\Rightarrow
\text{Semantic Discrimination Breadth}
}
$$

更強的方法是保留：

$$
\text{Named Falsifying Witnesses}
$$

也就是每一個真正不同的反例都具有穩定 identity、語義描述與移除理由。

---

# 6. Falsifying Witness

對一個 validator：

$$
V
$$

與 architecture clause：

$$
c
$$

定義 falsifying witness：

$$
w^-
$$

若：

1. $w^-$ 明確違反 $c$ ；
2. $w^-$ 在 test / replay 中可以實際生成；
3. $V(w^-)=FAIL$ ；
4. failure reason 與 $c$ 的違反原因一致；

則稱：

$$
\operatorname{Falsifies}(w^-,V,c)=1
$$

將所有具名 falsifying witnesses 記為：

$$
W_c^-
=
\{
w_1^-,
w_2^-,
\ldots,
w_k^-
\}
$$

注意：

$$
|W_c^-|
$$

不是越大越好。

重要的是：

$$
\operatorname{SemanticallyDistinct}(W_c^-)
$$

以及 witnesses 是否覆蓋 claim 的必要 failure dimensions。

---

# 7. Positive Witness

只做 negative testing 也不夠。

若 validator 對所有輸入都 FAIL：

$$
\forall x,
V(x)=FAIL
$$

它同樣沒有實用辨識力。

因此定義 positive witness：

$$
w^+
$$

若：

1. $w^+$ 滿足 clause $c$ ；
2. $V(w^+)=PASS$ ；

則：

$$
\operatorname{Supports}(w^+,V,c)=1
$$

positive witness 集合：

$$
W_c^+
$$

因此最弱的雙向 discrimination 要求：

$$
\exists w^+\in W_c^+:
V(w^+)=PASS
$$

且：

$$
\exists w^-\in W_c^-:
V(w^-)=FAIL
$$

---

# 8. Binary Discrimination 還是不夠

即使同時具有：

$$
PASS
$$

與：

$$
FAIL
$$

仍可能辨識錯軸。

因此本文將 claim 表為：

$$
c
=
(
\Theta_c,
\Gamma_c
)
$$

其中：

- $\Theta_c$：claim-relevant dimensions；
- $\Gamma_c$：允許保持不變或容許變動的其他 dimensions。

例如：

$$
\Theta_c
=
\{
\text{evidence.about}
\}
$$

而為了測 event binding，可以要求：

$$
\Gamma_c
$$

中的 subject、payload、timestamp freshness 等保持固定。

如果只改：

$$
\text{about}
$$

就能讓 verdict 翻轉：

$$
PASS
\rightarrow
FAIL
$$

才對該 axis 提供直接 discrimination evidence。

---

# 9. Axis-Bound Witness Pair

定義一組：

$$
(w^+,w^-)
$$

為 axis-bound witness pair，若：

$$
\Delta(w^+,w^-)
\subseteq
\Theta_c
$$

且：

$$
V(w^+)=PASS
$$

$$
V(w^-)=FAIL
$$

其中：

$$
\Delta
$$

表示兩個 witness 的語義差異集合。

理想的單軸 probe 有：

$$
|\Delta(w^+,w^-)|=1
$$

但實務上有些 architecture claim 必須改變多個互相約束的欄位，所以本文只要求：

$$
\Delta(w^+,w^-)
\subseteq
\Theta_c
$$

而不是一律 single-variable。

---

# 10. Axis Binding Closure

定義：

$$
C_{\text{axis}}(c)=1
$$

若對每一個 mandatory discrimination dimension：

$$
\theta_i
\in
\Theta_c
$$

存在至少一組具名 witness pair：

$$
(w_i^+,w_i^-)
$$

使 verdict 對：

$$
\theta_i
$$

的合法 / 違反變化具有正確反應。

這避免：

> validator 確實會 fail，但 fail 的是另一件事。

---

# 11. 測試如果產不出失敗世界，也沒有用

另一種更深的問題是：

> 你寫了正確的 assertion，但 test harness 根本無法產生真正會壞的 execution。

例如 lost update 需要：

$$
\text{read}_A
\rightarrow
\text{read}_B
\rightarrow
\text{write}_A
\rightarrow
\text{write}_B
$$

這種 interleaving。

如果測試永遠是：

$$
A
\rightarrow
B
$$

一個一個跑，那麼再多 assertion 都看不到 lost update。

所以：

$$
\boxed{
\text{Correct Assertion}
\not\Rightarrow
\text{Reachable Counterexample}
}
$$

---

# 12. Witness Reachability

令 test / replay harness：

$$
H
$$

可生成的 execution set 為：

$$
\mathcal X(H)
$$

若 falsifying witness：

$$
w^-
$$

只存在於理論描述，但：

$$
w^-
\notin
\mathcal X(H)
$$

則它不能作為實際 discrimination evidence。

因此要求：

$$
\boxed{
w^-
\in
\mathcal X(H)
}
$$

定義：

$$
C_{\text{reach}}(c)=1
$$

若所有 mandatory falsifying witness classes 至少有一個可實際生成的 witness。

---

# 13. Reachability 不只適用 concurrency

相同問題會出現在：

- error recovery；
- permission denial；
- network partition；
- stale cache；
- conflicting writer；
- expired evidence；
- wrong-subject evidence；
- alternate backend；
- crash before commit；
- crash after external effect；
- partial deployment；
- replay under fresh context。

如果 test harness 永遠只能產生 happy path，validator 再漂亮都不能證明 failure handling。

---

# 14. Witness Continuity

假設 validator v1 有：

$$
W_{c,1}^-
=
\{
w_a,w_b,w_c
\}
$$

改版後 v2：

$$
W_{c,2}^-
=
\{
w_a,w_b
\}
$$

即：

$$
w_c
$$

消失。

但 v2 仍可能：

- 能 PASS；
- 能 FAIL；
- mutation score 看起來仍高；
- 新增了其他反例。

若沒有保留 witness identity，就無法知道某一個原本能抓到的語義缺陷已經失去。

因此：

$$
\boxed{
\text{Validator Falsifiability}
\not\Rightarrow
\text{Falsifying-Witness Continuity}
}
$$

---

# 15. Falsifying-Witness Continuity

令：

$$
W_{c,t}^-
$$

表示版本 $t$ 的具名反例集合。

版本遷移：

$$
t\rightarrow t+1
$$

需要對每一個：

$$
w\in W_{c,t}^-
$$

滿足至少一個：

### K1 — PRESERVED

$$
w\in W_{c,t+1}^-
$$

且仍可正確失敗。

### K2 — REPLACED

舊 witness 被更精確的新 witness 替代，且保留 lineage。

### K3 — RETIRED-WITH-REASON

claim、architecture 或 threat model 已改變，因此 witness 被正式退役。

不允許：

### K4 — SILENTLY-DROPPED

沒有理由直接消失。

因此定義：

$$
C_{\text{continuity}}(c)=1
$$

若所有歷史 mandatory witness 都具備可追蹤 disposition。

---

# 16. 為什麼 raw mutation score 不夠

經典 mutation score 可寫為：

$$
MS
=
\frac{
\text{killed mutants}
}{
\text{non-equivalent mutants}
}
$$

它是衡量 test suite fault-detection adequacy 的重要指標。

但對 ABFR architecture validator 而言，單一 raw score 可能遮蔽：

1. duplicate semantic mutants；
2. 某個關鍵 witness 被移除；
3. validator 在錯誤 axis 上殺死 mutant；
4. test 根本沒有走到 target path；
5. 某些 mutation 是合法替換，不應被殺死。

所以本文不使用：

$$
C_D=MS
$$

而是把 mutation / attack 當成產生 discrimination evidence 的工具。

---

# 17. Equivalent Mutant 問題對 ABFR 的提醒

Mutation testing 長期面臨 equivalent mutant problem。

某個程式 mutation：

$$
m(P)
$$

雖然語法改變，但對所有可能測試仍與原程式行為等價。

這種 mutant 不應因「test 沒殺死」就直接算 test weakness。

ABFR 有完全對應的 architecture 問題。

例如：

- 合法 backend substitution；
- 不影響 target 的檔名變更；
- 允許的 dependency patch-level update；
- 符合 contract 的 implementation replacement；
- equivalence profile 明確允許的 timestamp 差異。

這些是：

$$
\text{Authorized / Equivalent Variants}
$$

而不是 violating mutants。

因此 validator 若把所有變化都判 FAIL：

$$
\text{over-rejection}
$$

也不算高品質 discrimination。

---

# 18. Authorized-Equivalence Preservation

令：

$$
W_c^{\equiv}
$$

表示對 clause $c$ 而言，被明確允許的等價變體。

要求：

$$
\forall w\in W_c^{\equiv},
\quad
V(w)=PASS
$$

或得到對應的：

$$
ALLOWED
$$

verdict。

因此定義：

$$
C_{\text{eq}}(c)=1
$$

若 validator 不會將已授權等價狀態錯誤拒絕。

這使 discrimination 同時具有：

$$
\text{Sensitivity}
$$

與：

$$
\text{Specificity}
$$

的工程類比。

---

# 19. Discriminative Closure 的五個部分

本文 v0.1 定義：

$$
\boxed{
C_D(c)
=
C_{\text{witness}}
\land
C_{\text{axis}}
\land
C_{\text{reach}}
\land
C_{\text{continuity}}
\land
C_{\text{eq}}
}
$$

其中：

### $C_{\text{witness}}$

存在具名 positive / falsifying witnesses。

### $C_{\text{axis}}$

validator 在 claim-relevant axis 上辨識。

### $C_{\text{reach}}$

test / replay harness 能實際產生相關反例。

### $C_{\text{continuity}}$

validator 版本變更不能靜默丟失既有 falsifying witness。

### $C_{\text{eq}}$

合法等價變體不被錯誤殺死。

---

# 20. Clause-Level 到 System-Level

對 architecture claim 集：

$$
\mathcal C
=
\{
c_1,\ldots,c_n
\}
$$

不是所有 clause 風險相同。

定義 mandatory subset：

$$
\mathcal C_M
\subseteq
\mathcal C
$$

則 system-level Discriminative Closure：

$$
C_D(\mathcal C_M)=1
$$

若：

$$
\forall c_i\in\mathcal C_M,
\quad
C_D(c_i)=1
$$

對非 mandatory clause 可以得到：

$$
PARTIAL
$$

而不是讓整個 release 永遠無法前進。

---

# 21. 三閉包

Paper 01–04 現在可以得到：

$$
\boxed{
C_{\text{engineering}}
=
C_B
\land
C_S
\land
C_D
}
$$

其中：

$$
C_B
=
\text{Behavioral Closure}
$$

$$
C_S
=
\text{Structural Reconstruction Closure}
$$

$$
C_D
=
\text{Discriminative Closure}
$$

三者回答不同問題。

---

# 22. Behavioral Closure 問什麼？

$$
C_B
$$

問：

> 系統是否滿足已聲明的代表行為？

典型證據：

- unit tests；
- integration tests；
- property tests；
- end-to-end tests；
- contract tests。

它主要是：

$$
\text{Requirement}
\rightarrow
\text{Executable Behavior}
$$

---

# 23. Structural Closure 問什麼？

$$
C_S
$$

問：

> 這些行為是否能由宣告架構，在移除 hidden support 後重新構成？

典型證據：

- architecture backtrace；
- declared / observed / effective reconciliation；
- MSRS；
- freshness evidence；
- replay equivalence。

它主要是：

$$
\text{Working System}
\rightarrow
\text{Explicit Structural Support}
\rightarrow
\text{Fresh Reconstruction}
$$

---

# 24. Discriminative Closure 問什麼？

$$
C_D
$$

問：

> 我們用來證明前兩件事的 validator，真的能分辨相關的好與壞嗎？

典型證據：

- named positive witnesses；
- named falsifying witnesses；
- axis-bound mutations；
- schedule / state fault injection；
- witness lineage；
- authorized-equivalence cases。

它主要是：

$$
\text{Validation Claim}
\rightarrow
\text{Proven Ability to Discriminate}
$$

---

# 25. 為什麼三者不能合併成一個 PASS

一個專案可以：

$$
C_B=1
$$

但：

$$
C_S=0
$$

例如測試全綠，但 clean reconstruction 缺 hidden dependency。

也可以：

$$
C_B=1,
\quad
C_S=1
$$

但：

$$
C_D=0
$$

例如 fresh replay 通過，但 architecture validator 對已知 violating mutation 仍然 PASS。

也可能：

$$
C_D=1
$$

而：

$$
C_B=0
$$

例如 validator 能正確拒絕錯誤 state，但功能本身仍沒完成。

因此：

$$
\boxed{
C_B,C_S,C_D
}
$$

不能互相替代。

---

# 26. ABFR Attack

本文將針對 architecture validation 的故意變異統稱：

$$
\text{ABFR Attack}
$$

這裡的 attack 不是 security exploit 的狹義含義，而是：

> 對被驗證 claim 施加可控制、可回復、可追蹤的反例變異。

一個 attack：

$$
\mu
$$

作用於：

$$
x
$$

得到：

$$
x'=\mu(x)
$$

如果：

$$
x
\models c
$$

而：

$$
x'
\not\models c
$$

則：

$$
\mu
$$

為 violating mutation。

預期：

$$
V(x)=PASS
$$

$$
V(x')=FAIL
$$

---

# 27. Attack Object 不只程式碼

ABFR attack 可以修改：

### A1. Code

例如刪掉 freshness check。

### A2. Dependency

加入未宣告 sibling coupling。

### A3. Architecture Declaration

把 optional role 錯標成 core。

### A4. Authority

讓不該寫入者取得 write permission。

### A5. Evidence Binding

將正確 evidence 掛到錯誤 event 或 subject。

### A6. Runtime State

注入 stale cache / previous-run state。

### A7. Reconstruction Material

偷偷提供未宣告 fixture。

### A8. External Contract

讓 stub 與 production semantic mismatch。

### A9. Schedule

產生 lost-update / race / crash interleaving。

### A10. Replay Equivalence

嘗試把 equivalence contract 放寬到讓原本違規狀態通過。

因此：

$$
\boxed{
\text{Architecture Mutation}
\supset
\text{Code Mutation}
}
$$

這是 ABFR 與一般 mutation-testing scope 最重要的差異之一。

---

# 28. Claim-Directed Mutation

隨機 mutation 可能造成很多無意義變化。

ABFR 更偏好：

$$
\boxed{
\text{Claim-Directed Mutation}
}
$$

對 clause：

$$
c
$$

先找：

$$
\Theta_c
$$

再產生：

$$
\mu_{\theta}
$$

只破壞其中一個 claim dimension。

例如：

$$
c:
\text{only CommitGate may write World}
$$

可以有：

$$
\mu_1:
\text{grant Plugin write authority}
$$

而不是隨便改一個 unrelated function。

這使 failure 更容易歸因。

---

# 29. Attack 必須可回復

每一個 mutation 都應具備：

- unique ID；
- target claim；
- mutated axis；
- exact patch / state change；
- expected verdict；
- actual verdict；
- cleanup / rollback；
- evidence。

即：

$$
\mu
=
(
id,
c,
\theta,
\Delta,
V_{expected},
V_{actual},
rollback,
evidence
)
$$

這避免「手動弄壞看看」成為不可重播實驗。

---

# 30. Negative Witness Registry

對每個重要 clause：

$$
c
$$

建立：

$$
\mathcal W(c)
=
(
W_c^+,
W_c^-,
W_c^{\equiv}
)
$$

每個 witness 至少記錄：

```text
witness_id
claim_id
semantic_case
mutation_id
affected_axis
expected_verdict
actual_verdict
reachability_method
evidence
introduced_in
retired_in
retirement_reason
```

這個 registry 是 Paper 05 Cross-Agent Protocol 的重要輸入之一。

---

# 31. 為什麼要具名

若只存：

```text
mutation_score = 0.93
```

下一版即使：

$$
w_{critical}
$$

消失，也可能因新增十個低風險 mutants 讓分數更高。

具名 witness 則可以比較：

$$
W_{t}^-
\rightarrow
W_{t+1}^-
$$

所以：

$$
\boxed{
\text{Identity Preservation}
>
\text{Anonymous Aggregate Count}
}
$$

對 architecture governance 尤其重要。

---

# 32. Discrimination Matrix

對 clauses：

$$
c_1,\ldots,c_n
$$

以及 witnesses：

$$
w_1,\ldots,w_m
$$

可建立：

$$
D_{ij}
=
\begin{cases}
1, & V_{c_i}(w_j)=\text{expected verdict}\\
0, & \text{otherwise}
\end{cases}
$$

但還要另外記錄：

$$
A_{ij}
$$

表示 witness 是否真正作用於：

$$
\Theta_{c_i}
$$

以及：

$$
R_{ij}
$$

表示 witness 是否可實際到達 validator path。

因此有效 discrimination 不是只看：

$$
D_{ij}
$$

而是：

$$
D_{ij}
\cdot
A_{ij}
\cdot
R_{ij}
$$

---

# 33. Semantic Witness Coverage

定義 mandatory semantic cases：

$$
K_c
=
\{
k_1,\ldots,k_r
\}
$$

若每一個 case 至少有一個有效 falsifying witness，則：

$$
Coverage_D(c)
=
\frac{
|\{k_i:\exists w^- \text{ covers }k_i\}|
}{
|K_c|
}
$$

這比 duplicate mutation count 更接近本文需要的 coverage。

但：

$$
Coverage_D=1
$$

仍不自動推出：

$$
C_D=1
$$

因為還需 continuity 與 authorized-equivalence preservation。

---

# 34. Wrong-Axis Score

可以定義：

$$
WAS(c)
=
\frac{
\text{failing witnesses whose verdict is driven by non-target axis}
}{
\text{all failing witnesses}
}
$$

理想：

$$
WAS(c)=0
$$

這個量測在真實專案中不容易完全自動化，但 controlled benchmark 可以直接設計。

例如：

- 固定 payload；
- 固定 timestamp；
- 固定 subject；
- 只切換 about-event；

如果 verdict 不變，就代表：

$$
C_{\text{axis}}=0
$$

---

# 35. Reachability Coverage

令 mandatory failure schedules / states 為：

$$
\mathcal X_c^-
$$

test harness 實際能產生：

$$
\hat{\mathcal X}_c^-
$$

則：

$$
Coverage_R(c)
=
\frac{
|\hat{\mathcal X}_c^-\cap\mathcal X_c^-|
}{
|\mathcal X_c^-|
}
$$

同樣，真實世界通常不知道完整：

$$
\mathcal X_c^-
$$

所以這個量測最適合 injected benchmark 或 formally enumerated small-state systems。

---

# 36. Continuity Score

令歷史 mandatory witness：

$$
W_{c,t}^-
$$

在下一版有合法 disposition 的集合為：

$$
L_{c,t\rightarrow t+1}
$$

則：

$$
Continuity(c)
=
\frac{
|L_{c,t\rightarrow t+1}|
}{
|W_{c,t}^-|
}
$$

release gate 可要求：

$$
Continuity(c)=1
$$

對 critical clause 特別合理。

---

# 37. Authorized-Equivalence False Positive Rate

定義：

$$
FPR_{\equiv}(c)
=
\frac{
|\{w\in W_c^{\equiv}:V(w)=FAIL\}|
}{
|W_c^{\equiv}|
}
$$

理想：

$$
FPR_{\equiv}(c)=0
$$

這防止 validator 透過「什麼都不准變」取得虛假的高 kill rate。

---

# 38. Discriminative Closure Verdict

對 clause：

$$
c
$$

本文建議 verdict：

$$
V_D(c)
\in
\{
PASS,
PARTIAL,
FAIL,
INCONCLUSIVE
\}
$$

### PASS

五個 closure component 全部成立。

### PARTIAL

有非 blocking witness / coverage 缺口，但 mandatory cases 已閉合。

### FAIL

critical witness 未被殺死、wrong-axis、不可到達、silent witness loss 或 authorized equivalent 被錯誤拒絕。

### INCONCLUSIVE

缺少足夠資料判斷 witness 的語義或等價性。

---

# 39. Equivalent / Authorized Variant 不能硬殺

這是一個容易被「攻擊測試」文化忽略的點。

如果 architecture contract 明確允許：

$$
Backend_A
\simeq_Q
Backend_B
$$

那麼：

$$
Backend_A
\rightarrow
Backend_B
$$

不應被 validator 當成 violation。

所以好的 validator 不是：

$$
\text{Maximize FAIL}
$$

而是：

$$
\boxed{
\text{Reject the forbidden differences and preserve the allowed differences}
}
$$

這和 Paper 03 的 replay equivalence 完全一致。

---

# 40. Equivalence Contract 本身也要被攻擊

假設：

$$
\simeq_{Q,1}
$$

原本要求 authority 完全一致。

下一版改成：

$$
\simeq_{Q,2}
$$

忽略 authority difference。

這可能讓原本：

$$
FAIL
$$

的 architecture drift 被「重新定義成相同」而變：

$$
PASS
$$

因此 equivalence contract revision 也需要：

- owner；
- version；
- rationale；
- affected witnesses；
- migration evidence。

換言之：

$$
\boxed{
\text{Changing the meaning of same is a governance event}
}
$$

---

# 41. Metamorphic Testing 可以怎麼加入

Metamorphic Testing 在缺乏單次輸出 oracle 時，透過多次執行之間應保持的 metamorphic relation 進行驗證。

ABFR 可以利用這個思想。

例如：

$$
MR_1:
\text{Replace allowed backend}
\Rightarrow
\text{behavior remains equivalent}
$$

以及：

$$
MR_2:
\text{Move evidence to wrong subject}
\Rightarrow
\text{validator verdict flips}
$$

其中：

$$
MR_1
$$

是 authorized-equivalence relation；

$$
MR_2
$$

是 falsifying relation。

因此：

$$
\boxed{
\text{Metamorphic Relations}
}
$$

可以成為 ABFR witness generator / oracle source。

但 ABFR 不等同於 Metamorphic Testing，因為其 closure 還包含 architecture backtrace、freshness、authority、witness continuity 與 governance。

---

# 42. Mutation Testing 可以怎麼加入

Mutation Testing 非常適合幫：

$$
C_D
$$

產生 attack。

例如 code-level clause：

$$
c:
\text{reject stale capture}
$$

可以 mutation：

$$
\mu:
\text{remove freshness comparison}
$$

然後要求：

$$
V(\mu(P))=FAIL
$$

但 architecture-level claim 可能需要非 code mutation，例如：

$$
\mu:
\text{inject stale database snapshot}
$$

或：

$$
\mu:
\text{grant unauthorized writer}
$$

所以 Paper 04 的設計是：

$$
\boxed{
\text{Mutation Testing}
\subseteq
\text{Available Attack Techniques}
}
$$

而不是：

$$
\text{ABFR Attack}
=
\text{Mutation Testing}
$$

---

# 43. Property-Based Testing 可以怎麼加入

如果 claim 有可生成狀態空間：

$$
X
$$

property-based testing 可以用來搜尋：

$$
x\in X
$$

使：

$$
c(x)=0
$$

並檢查：

$$
V(x)=FAIL
$$

特別適合：

- boundary values；
- permission combinations；
- schema invariants；
- ordering；
- state-machine transitions。

這可以降低人工列舉 witness 的成本。

---

# 44. Fault Injection 可以怎麼加入

Paper 03 的 Fresh Reconstruction / Recovery 類 target 對 fault injection 特別自然。

例如：

$$
\{
\text{crash before execute},
\text{crash after execute},
\text{crash before commit},
\text{network loss},
\text{partial write}
\}
$$

每個 fault point 可以是：

$$
w^-
$$

或：

$$
w^{\equiv}
$$

取決於 architecture contract。

因此：

$$
\boxed{
\text{Fault Injection}
}
$$

是 state / runtime dimension 的 witness generation technique。

---

# 45. Attack Selection

不是每個 milestone 都值得攻擊所有 clause。

可以定義 risk weight：

$$
r(c)
$$

與 change impact：

$$
\Delta(c)
$$

則 attack priority：

$$
P(c)
=
r(c)\cdot \Delta(c)
$$

高風險、高變更 clause 優先執行完整 witness suite。

低風險、未變更 clause 可以使用：

- witness continuity check；
- sampling；
- cached evidence；

但 critical invariant 不應只靠 cache。

---

# 46. Attack Budget

令 attack 成本：

$$
C_A
$$

包含：

$$
C_A
=
C_{\text{mutation}}
+
C_{\text{rebuild}}
+
C_{\text{replay}}
+
C_{\text{cleanup}}
+
C_{\text{analysis}}
$$

因此工程上需要：

$$
\max
\frac{
\text{expected discrimination gain}
}{
C_A
}
$$

而不是盲目最大化 mutation 數量。

這也是具名 semantic witness 比大量匿名變異更適合架構層的原因之一。

---

# 47. AI 為什麼適合做這件事

對人類而言，持續維護：

- 每條 clause；
- 每個 witness；
- 每個 axis；
- 每次 validator revision；
- 每個 witness lineage；

成本很高。

AI 特別適合：

$$
\text{Repeated Cross-Reference}
$$

與：

$$
\text{Systematic Mutation Generation}
$$

但 AI 也有風險：

- 自己設計的 validator 可能自己合理化；
- 可能產生 superficial mutants；
- 可能在結果出來後放寬 equivalence；
- 可能把不同語義 case 當成重複；
- 可能遺忘舊 witness。

因此 Paper 04 的方法故意把：

$$
\text{witness identity}
$$

與：

$$
\text{predeclared expected verdict}
$$

外部化。

---

# 48. Cross-Agent Attack

後續 Paper 05 可以測：

> Agent A 寫 validator，Agent B 能不能找到讓它錯判的 witness？

這比：

> Agent A 自己證明自己是對的。

更接近 independent challenge。

但第一輪 protocol 仍可固定 Inline Execution，避免 sub-agent architecture 干擾。

跨 Agent 可以在不同 session 分別扮演：

- implementer；
- backtracer；
- attacker；
- replay executor。

這是一個研究設計，不代表每個正式工程流程都必須使用四個模型。

---

# 49. Validator Self-Attack

即使只有一個 AI，也可以要求：

1. 先凍結 claim；
2. 先凍結 validator；
3. 再產生 mutation；
4. 不允許在看到結果後修改 expected verdict；
5. 若 validator 修改，重新跑全部歷史 witnesses。

這降低：

$$
\text{post-hoc rationalization}
$$

---

# 50. Attack Before UI

Paper 01 已提出：

$$
\text{TDD}
\rightarrow
\text{ABFR}
\rightarrow
\text{Runtime/UI}
$$

Paper 04 現在進一步寫成：

$$
\boxed{
\text{TDD}
\rightarrow
\text{Backtrace}
\rightarrow
\text{Fresh Reconstruction}
\rightarrow
\text{Replay}
\rightarrow
\text{Attack}
\rightarrow
\text{Runtime/UI}
}
$$

原因是 UI 越完整：

$$
C_{\text{projection}}
\uparrow
$$

越可能增加：

- hidden state；
- async path；
- browser residue；
- human workaround；
- integration masking。

所以在 foundation milestone 上，先證明 validator 能被打紅，再加 projection layer，比完成 UI 後才追底層架構更乾淨。

---

# 51. 完整 ABFR+Attack 流程

本文提出 v0.1：

$$
\begin{aligned}
1.&\quad \text{Freeze Baseline}\\
2.&\quad \text{Declare Behavioral Requirements}\\
3.&\quad \text{Declare Architecture Claims}\\
4.&\quad \text{Write Precise TDD Plan}\\
5.&\quad \text{Red}\\
6.&\quad \text{Implement}\\
7.&\quad \text{Green}\\
8.&\quad \text{Refactor}\\
9.&\quad \text{Architecture Backtrace}\\
10.&\quad \text{Declared/Observed/Effective Reconciliation}\\
11.&\quad \text{Derive MSRS Candidate}\\
12.&\quad \text{Fresh Reconstruction}\\
13.&\quad \text{Replay}\\
14.&\quad \text{Freeze Validator / Equivalence Profile}\\
15.&\quad \text{Run Named Positive Witnesses}\\
16.&\quad \text{Run Named Falsifying Witnesses}\\
17.&\quad \text{Check Axis Binding}\\
18.&\quad \text{Check Witness Reachability}\\
19.&\quad \text{Check Witness Continuity}\\
20.&\quad \text{Run Authorized-Equivalence Cases}\\
21.&\quad \text{Decide Three-Closure Verdict}\\
22.&\quad \text{Only Then Expand Runtime/UI}
\end{aligned}
$$

---

# 52. 三閉包 Gate 的完整形式

對 milestone targets：

$$
Q
$$

architecture claims：

$$
\mathcal C_M
$$

定義：

$$
G_{\text{3C}}
=
C_B(Q)
\land
C_S(Q)
\land
C_D(\mathcal C_M)
$$

其中：

$$
C_S(Q)
=
C_{BT}
\land
C_{\text{MSRS}}
\land
C_F
\land
C_R
$$

而：

$$
C_D(\mathcal C_M)
=
\bigwedge_{c\in\mathcal C_M}
\left(
C_{\text{witness}}
\land
C_{\text{axis}}
\land
C_{\text{reach}}
\land
C_{\text{continuity}}
\land
C_{\text{eq}}
\right)
$$

因此：

$$
\boxed{
G_{\text{3C}}
}
$$

不是單一 test result，而是多層 evidence closure。

---

# 53. Release Verdict

本文建議 milestone / release 的 closure verdict 為：

$$
V_{\text{3C}}
\in
\{
PASS,
PARTIAL,
FAIL,
INCONCLUSIVE
\}
$$

### PASS

所有 mandatory：

$$
C_B,C_S,C_D
$$

成立。

### PARTIAL

沒有 blocking failure，但存在明示 deferred clause / witness gap。

### FAIL

至少一個 blocking behavioral、structural 或 discriminative criterion 失敗。

### INCONCLUSIVE

evidence 不足，不能合理宣稱通過或失敗。

---

# 54. 不允許「因為 attacker 太強所以忽略」

如果 attack 找到：

$$
w^-
$$

使 validator 錯判，正確處理方式不是：

> 這個案例太刁鑽，所以不算。

而是先分類。

### Case A — Valid Violation

那就是：

$$
C_D=0
$$

需要修 validator / architecture。

### Case B — Authorized Variant

把：

$$
w^-
$$

重新分類為：

$$
w^{\equiv}
$$

但必須更新 equivalence contract 並說明理由。

### Case C — Out of Scope

若 target scope 從一開始就排除該 case，可以標記 out-of-scope。

但不能在 attack 結果出來後沒有治理紀錄地改 scope。

---

# 55. 不允許 Silent Equivalence Expansion

若原本：

$$
w
$$

應 FAIL。

validator 更新後：

$$
w
$$

變 PASS。

允許的原因包括：

- architecture contract 改版；
- witness 原本被錯誤分類；
- risk acceptance；
- feature semantics 改變。

但必須有：

$$
\operatorname{GovernanceEvent}(w)
$$

否則：

$$
\boxed{
\text{FAIL}\rightarrow\text{PASS}
}
$$

本身就是需要審查的 signal。

---

# 56. 不允許 Duplicate Witness Inflation

如果：

$$
w_1,w_2
$$

只有 ID 不同，但：

$$
\operatorname{SemanticCase}(w_1)
=
\operatorname{SemanticCase}(w_2)
$$

則：

$$
w_1,w_2
$$

不能在 semantic witness coverage 中算兩個不同 case。

可以保留多個 implementation instances，但 coverage identity 應依：

$$
\operatorname{SemanticCase}
$$

計算。

---

# 57. 不允許 Dead-Path Mutation

若 mutation：

$$
\mu
$$

發生在從來不會被 target workload 執行的 path：

$$
\operatorname{Reach}(Q,\mu)=0
$$

那麼：

$$
V(\mu(P))=PASS
$$

不能直接被解釋為 validator weakness。

正確 verdict 是：

$$
\text{UNREACHED}
$$

然後追問：

> 這個 path 是否應該在 test scope 內？

這把 reachability 與 discrimination 分開。

---

# 58. 不允許 Wrong-Reason Kill

如果 mutation 目的是破壞：

$$
\theta_1
$$

但 test 因另一個獨立錯誤：

$$
\theta_2
$$

FAIL，不能算成功 kill。

因此每個 witness 應有：

$$
\operatorname{ExpectedFailureReason}
$$

並比對：

$$
\operatorname{ActualFailureReason}
$$

至少在 critical clause 上：

$$
\operatorname{ActualReason}
\simeq
\operatorname{ExpectedReason}
$$

---

# 59. Failure Reason Equivalence

錯誤訊息不必逐字相同。

可以定義：

$$
\simeq_{reason}
$$

例如：

$$
\{
\text{AUTHORITY_DENIED},
\text{WRITE_NOT_ALLOWED}
\}
$$

可能屬於同一 semantic class。

因此：

$$
\operatorname{ReasonClass}
(
V(w^-)
)
=
\operatorname{ExpectedClass}(w^-)
$$

比字串比對更穩定。

---

# 60. Failure Taxonomy

本文新增 Discriminative Failure：

## DC-01 Constant Green

validator 對 known violating witness 仍 PASS。

## DC-02 Constant Red

合法 positive / authorized variant 也全部 FAIL。

## DC-03 Wrong-Axis Discrimination

validator 會變，但不是因 claim-relevant axis。

## DC-04 Duplicate-Witness Inflation

多個 witness 其實同一 semantic case。

## DC-05 Unreachable Witness

test harness 產不出 required counterexample。

## DC-06 Silent Witness Loss

validator revision 讓歷史 witness 消失，無治理理由。

## DC-07 Equivalent-Variant Rejection

合法替代狀態被錯誤拒絕。

## DC-08 Dead-Path Mutation

mutation 未抵達 target execution path。

## DC-09 Wrong-Reason Kill

validator FAIL，但不是因預期 violation。

## DC-10 Post-Hoc Equivalence Relaxation

看到結果後才放寬「相同」的定義。

## DC-11 Scope Laundering

看到 counterexample 後才將其標為 out-of-scope。

## DC-12 Attack Contamination

mutation 同時改太多 unrelated dimensions，無法判斷是哪個變化造成 verdict。

---

# 61. 可證偽假說

## H1 — Can-Fail Is Insufficient

存在 validator：

$$
V
$$

滿足：

$$
\exists x,y:
V(x)\neq V(y)
$$

但：

$$
C_{\text{axis}}=0
$$

因此單純證明「會 fail」不足以建立 $C_D$。

---

## H2 — Named Witness Continuity Finds Regression Missed by Aggregate Score

存在 validator revision：

$$
V_t\rightarrow V_{t+1}
$$

使 aggregate mutation / failure count 不下降，甚至上升，但某個 critical witness 被 silent drop。

具名 witness continuity 可以檢出此 regression。

---

## H3 — Reachability Analysis Finds False Assurance

存在 test suite：

$$
T
$$

具有正確 assertion，但：

$$
w^-\notin\mathcal X(T)
$$

導致 critical failure mode 永遠不可生成。

---

## H4 — Authorized-Equivalence Set Reduces Over-Rejection

加入：

$$
W^{\equiv}
$$

後，可以發現只追求 kill rate 的 validator 對合法替代 architecture 過度拒絕。

---

## H5 — Claim-Directed Attacks Are More Diagnostic

相對 random mutation：

$$
\text{Claim-Directed Mutation}
$$

應提高：

$$
\frac{
\text{actionable architecture findings}
}{
\text{attack cost}
}
$$

---

## H6 — Cross-Agent Attack Increases Novel Witness Discovery

對相同 frozen validator：

$$
A_{\text{implementer}}
$$

與獨立：

$$
A_{\text{attacker}}
$$

相比 self-attack，可能產生更多 distinct semantic witnesses。

這是待實驗問題，不預設一定成立。

---

# 62. 與既有 Mutation Testing 的關係

Mutation Testing 是成熟的 fault-based testing 技術。Jia 與 Harman 的經典 survey 系統整理了 mutation operators、mutation adequacy、equivalent mutants、成本與工具發展。

近年的研究仍持續處理 equivalent mutant detection，包含利用大型語言模型輔助判斷 semantic equivalence。

這些工作提醒 ABFR 兩件事。

第一：

$$
\boxed{
\text{A surviving mutation is not automatically a test failure}
}
$$

因為 mutation 可能等價。

第二：

$$
\boxed{
\text{Mutation adequacy is about the quality of the oracle/test relation, not merely producing many mutants}
}
$$

Paper 04 延伸這個精神到 architecture validation，但不重新命名 mutation testing。

---

# 63. 與 Metamorphic Testing 的關係

Metamorphic Testing 處理 oracle problem：當單一執行的正確輸出難以直接知道時，利用多次執行間應維持的關係作為 oracle。

2026 年已有研究把 LLM 用於 metamorphic relation inference 與 follow-up test generation。

ABFR 可以將：

$$
\text{allowed architecture transformation}
$$

與：

$$
\text{forbidden architecture transformation}
$$

都寫成 metamorphic-style relations。

例如：

$$
Backend_A
\rightarrow
Backend_B
$$

應維持：

$$
Q
$$

的行為等價；

而：

$$
Evidence.subject
\rightarrow
WrongSubject
$$

應讓 verdict 翻轉。

因此 MT 是 ABFR attack oracle 的重要工具之一。

---

# 64. 與 MSSP 方法演化的關係

MSSP 的實驗方法本身已從：

$$
\text{check must fail}
$$

進一步演化到：

$$
\text{what exactly can make it fail?}
$$

再到：

$$
\text{is it failing on the right axis?}
$$

以及：

$$
\text{which named counterexamples still survive validator revision?}
$$

這條演化路徑正是本文 Discriminative Closure 的經驗來源。

因此 Paper 04 並不是把一般 mutation testing 硬套進 MSSP，而是把 MSSP 自己已經透過 probes 發現的 validator epistemology 收斂成 ABFR 的正式第三閉包。

---

# 65. 方法論的一句話版本

Behavioral Closure：

> 功能真的照要求工作嗎？

Structural Closure：

> 這個工作狀態真的能由宣告架構重新建立嗎？

Discriminative Closure：

> 我們用來證明前兩件事的檢查，真的知道什麼情況該失敗嗎？

因此：

$$
\boxed{
\text{Works}
\land
\text{Reconstructs}
\land
\text{Discriminates}
}
$$

才構成本文所稱的三閉包。

---

# 66. 對 AI 工程的意義

AI coding agent 的一個危險特性是：

> 它可以非常快速地產生大量看起來完整的測試、validator、報告與綠燈。

所以未來工程品質不能只看：

$$
\text{number of tests}
$$

或：

$$
\text{all green}
$$

而必須問：

$$
\boxed{
\text{What named state makes this check go red, and why?}
}
$$

更進一步：

$$
\boxed{
\text{Can another AI reproduce that red state from canonical artifacts?}
}
$$

這把「AI 很會寫測試」轉換成「AI 必須證明測試具有辨識能力」。

---

# 67. 對通用方法論的意義

如果 ABFR 要離開 MSSP，成為通用方法，它至少需要一個與具體 taxonomy 無關的基本語言。

Paper 04 現在提供：

$$
\{
\text{Claim},
\text{Validator},
\text{Positive Witness},
\text{Falsifying Witness},
\text{Authorized Equivalent},
\text{Axis},
\text{Reachability},
\text{Continuity}
\}
$$

這些概念不依賴：

$$
FMS/SMS/TMS
$$

名稱。

所以即使另一個專案使用：

- Clean Architecture；
- Hexagonal Architecture；
- microservices；
- monorepo package graph；
- plugin architecture；
- workflow graph；

仍可建立：

$$
C_D
$$

這將是 Paper 05 / Spec B 要實驗的通用性之一。

---

# 68. 不宣稱事項

本文明確不宣稱：

1. Discriminative Closure 取代 mutation testing。
2. 所有 architecture claim 都能找到有限完整 witness set。
3. 所有 mutation 都應該被 kill。
4. 高 mutation score 等於高 Discriminative Closure。
5. 具名 witness 越多越好。
6. 每個 witness 必須只修改一個物理欄位。
7. validator 的文字錯誤訊息必須完全相同。
8. AI 能可靠自動判斷所有 equivalent mutants。
9. attack 越激進越好。
10. 每個 milestone 都必須跑所有歷史 attack。
11. Cross-Agent attack 一定優於 self-attack。
12. 三閉包構成 formal proof。
13. PASS 表示不存在未知 failure mode。
14. equivalent / authorized variant 可以在 attack 後無治理紀錄地重新定義。
15. 「會 fail」已經足以證明 validator 正確。

---

# 69. Paper 05 的輸入

完成 Paper 04 後，Cross-Agent experiment 已有完整核心資料模型。

每個 fresh AI 至少需要處理：

```text
baseline
behavioral requirements
architecture claims
declared architecture
replay targets
freshness contract
equivalence profile
positive witnesses
falsifying witnesses
authorized-equivalence witnesses
witness lineage
closure rules
```

輸出：

```text
TDD verdict
backtrace result
MSRS candidate
fresh reconstruction evidence
replay verdict
attack results
wrong-axis findings
reachability findings
witness-continuity findings
equivalence false positives
three-closure verdict
additional information requests
```

這使我們可以第一次真正比較：

$$
\text{AI}_1,
\text{AI}_2,
\ldots
$$

是否能獨立執行同一套方法，而不是只比較「誰最後把 code 寫對」。

---

# 70. 結論

一個永遠綠燈的 validator 沒有證據價值。

但本文進一步指出：

$$
\boxed{
\text{A validator that can fail may still be epistemically weak}
}
$$

因為它可能：

- 在錯的軸上失敗；
- 只具有重複的單一反例；
- 根本產不出關鍵 failure schedule；
- 在改版時靜默遺失重要 witness；
- 把合法等價替代也全部拒絕。

因此 ABFR 的第三閉包不能只寫成：

$$
\exists x:
V(x)=FAIL
$$

而必須要求：

$$
\boxed{
C_D(c)
=
C_{\text{witness}}
\land
C_{\text{axis}}
\land
C_{\text{reach}}
\land
C_{\text{continuity}}
\land
C_{\text{eq}}
}
$$

最後，Paper 01–04 形成完整的三閉包工程命題：

$$
\boxed{
C_{\text{engineering}}
=
C_B
\land
C_S
\land
C_D
}
$$

也就是：

$$
\boxed{
\text{Works}
\land
\text{Reconstructs}
\land
\text{Discriminates}
}
$$

TDD 讓實作必須先面對可執行的行為要求。

MSSP / ABFR 讓工作系統必須面對 architecture backtrace 與 fresh reconstruction。

Discriminative Closure 再要求所有重要 validator 面對具名的反例、正確的語義軸、可生成的 failure world，以及歷史 witness 的持續追蹤。

因此本文提出的最終工程原則是：

> **一個宣稱，若不能指出什麼具名狀態會讓它失敗、為什麼會失敗、那個狀態是否真的可生成，以及下一版是否仍保有這個反例，就還沒有形成完整的驗證閉包。**

下一步不再是增加新的理論層。

下一步是把這套三閉包交給不同 AI、不同 repository、不同 architecture profile，看看它是否真的能被獨立重現。

---

# 參考文獻

[1] Jia, Y., & Harman, M. (2011). *An Analysis and Survey of the Development of Mutation Testing*. IEEE Transactions on Software Engineering, 37(5), 649–678. DOI: 10.1109/TSE.2010.62.

[2] DeMillo, R. A., Lipton, R. J., & Sayward, F. G. (1978). *Hints on Test Data Selection: Help for the Practicing Programmer*. Computer, 11(4), 34–41.

[3] Tian, Z., Shu, H., Wang, D., Cao, X., Kamei, Y., & Chen, J. (2024). *Large Language Models for Equivalent Mutant Detection: How Far Are We?* Proceedings of ISSTA 2024, 1733–1745. DOI: 10.1145/3650212.3680395.

[4] Pugh, T., Mina Lopez, C., Peacock, S., Deng, L., Dehlinger, J., & Chakraborty, S. (2025). *Enhancing Mutation Testing Efficiency: A Comparative Study of Machine Learning Models for Equivalent Mutant Identification*. Software Testing, Verification and Reliability, 35, e70004. DOI: 10.1002/stvr.70004.

[5] Cañizares, P. C., Gómez-Abajo, P., Guerra, E., & de Lara, J. (2026). *Towards metamorphic testing with LLM-based workflows: Metamorphic relation inference and follow-up test case generation*. Information and Software Technology, 196, 108150. DOI: 10.1016/j.infsof.2026.108150.

[6] *ISVMT: An approach of indicator systems validation based on metamorphic testing and data mutation*. Information and Software Technology, 189, 107944 (2026). DOI: 10.1016/j.infsof.2025.107944.

[7] Neo.K / EveMissLab. (2026). *MSSP Field Manual / Development Area*. thisoneisneok.com, accessed 2026-08-28.

[8] Neo.K / EveMissLab. (2026). *MSSP Discussion D-003 — 一份拿去跟自己副本比對的宣告，是同一個缺陷穿了一件檢查的外衣*. thisoneisneok.com, accessed 2026-08-28.

[9] Neo.K / EveMissLab. (2026). *MSSP Example 009 — 具名反例的延續性*. thisoneisneok.com, accessed 2026-08-28.

[10] Neo.K / EveMissLab. (2026). *MSSP Example 010 — 證據要說出它是關於哪一次事件與哪一個主體*. thisoneisneok.com, accessed 2026-08-28.

[11] Neo.K / EveMissLab. (2026). *MSSP Example 012 — 兩個寫入者，以及測試產不出來的那個排程*. thisoneisneok.com, accessed 2026-08-28.

---

## Canonical status

本文為 **ABFR Series Paper 04 v0.1**。

目前狀態：

- Three-closure model: defined.
- Discriminative Closure: defined for v0.1.
- Named falsifying witnesses: defined.
- Axis binding: defined.
- Witness reachability: defined.
- Falsifying-witness continuity: defined.
- Authorized-equivalence preservation: defined.
- ABFR Attack object classes: defined.
- Discriminative failure taxonomy: defined.
- Cross-AI validation: pending.
- Empirical superiority over mutation-score baselines: not claimed.
- Completeness of witness sets: not claimed.
- Formal verification status: not claimed.

後續版本若改變某個 witness 的 expected verdict、equivalence class、semantic identity 或 retirement reason，必須建立顯式 governance record；不得以 validator 改版後的綠燈靜默覆蓋歷史反例。
