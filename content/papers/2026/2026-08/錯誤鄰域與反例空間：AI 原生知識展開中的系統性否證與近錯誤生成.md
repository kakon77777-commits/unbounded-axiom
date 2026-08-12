# 錯誤鄰域與反例空間：AI 原生知識展開中的系統性否證與近錯誤生成

**English Title:** Error Neighborhoods and Counterexample Spaces: Systematic Falsification and Near-Miss Generation for AI-Native Knowledge Expansion  
**Series:** AI-Native Knowledge Expansion, Paper III  
**Author:** Neo.K  
**Collaborator:** Aletheia (GPT-5.6 Sol)  
**Institution:** EveMissLab / 一言諾科技有限公司  
**Version:** v0.1  
**Date:** 2026-08-10

## 摘要

AI 數學推理通常以「如何產生正確答案與正確證明」為主要目標，但真正可靠的推理能力不只要求系統知道何時可以推出結論，也要求系統知道何時**不能**推出結論、哪一個前提不可刪除、哪一個量詞不能替換、哪一個定義域不能擴張，以及一個看似正確的證明究竟在哪一步開始失效。

本文在 Base Knowledge Space Expansion（BKSE）框架下提出「錯誤鄰域」（Error Neighborhood）與「反例空間」（Counterexample Space）。對一個已驗證命題 \(P\)，我們不只生成其合法正向變種，也有系統地生成與 \(P\) 結構距離很近、但因局部修改而變成錯誤、不可證、條件不足或語義越界的命題 \(P'\)。這些負向節點不被視為垃圾資料，而被保存為帶有錯誤類型、最小反例、失效位置、修復操作與母命題距離的可驗證研究物件。

本文區分至少八類錯誤：假設刪除、量詞變異、定義域越界、方向反轉、類型錯置、局部推導污染、依賴失真，以及有限驗證誤升格為全稱證明。進一步提出「最小失敗差」（Minimal Failure Delta）與「反例證書」（Counterexample Certificate），使 AI 能學習的不只是 \(\text{true}/\text{false}\)，而是「為什麼這個極近鄰命題失敗」以及「最小需要改回什麼才重新成立」。

本文主張：AI 原生數學的可靠性可能高度依賴一種被低估的資料——**與真命題非常接近、但可被形式驗證為錯誤的近鄰資料**。這些資料可提高邊界辨識、假設敏感度、反例搜尋、proof repair、形式化驗證與自主研究中的批判能力。

**關鍵詞：** 錯誤鄰域；反例空間；近錯誤；假設消融；形式化反例；AI 原生數學；BKSE；否證；proof repair；adversarial verification

---

## 1. 正確資料不是完整的推理資料

若一個模型只看過：

\[
P_1\to \text{proof}_1,\qquad
P_2\to \text{proof}_2,\qquad \ldots
\]

它主要學習的是：

\[
\text{如何從可證命題走向證明}.
\]

但真正的數學推理還包含另一半：

\[
\boxed{\text{Why is this tempting statement not provable?}}
\]

例如：

\[
A\land B\Rightarrow C
\]

成立，不代表：

\[
A\Rightarrow C.
\]

同樣地：

\[
P(1),P(2),\ldots,P(N)
\]

全部通過，也不等於已證明：

\[
\forall n,\ P(n).
\]

因此本文將高品質推理資料拆成：

\[
D=D^+\cup D^-,
\]

其中 \(D^+\) 是合法命題、證明與正向變種，\(D^-\) 是近錯誤、反例、錯誤證明、越界條件與不可合法推導節點。

---

## 2. 錯誤鄰域

對一個已驗證命題 \(P\)，令結構距離為：

\[
d_S(P,Q).
\]

定義半徑 \(\epsilon\) 下的候選鄰域：

\[
N_\epsilon(P)=\{Q:d_S(P,Q)\le \epsilon\}.
\]

其中不能維持原合法關係的節點構成：

\[
\boxed{
N^-_\epsilon(P)
=
\{Q\in N_\epsilon(P):\operatorname{Valid}(Q)=0\}.
}
\]

更嚴格地，系統應保存：

\[
\operatorname{Status}(Q)
\in
\{
\text{false},
\text{counterexample-found},
\text{ill-typed},
\text{domain-invalid},
\text{unjustified},
\text{unknown}
\}.
\]

其中最重要的硬限制是：

\[
\boxed{
\text{not proved}\neq\text{disproved}.
}
\]

---

## 3. 為什麼近錯誤比隨機錯誤重要？

考慮：

\[
P:x>0\Rightarrow x^2>0.
\]

若改成：

\[
P':x\ge0\Rightarrow x^2>0,
\]

只改變一個邊界條件，且 \(x=0\) 就構成反例。

這種近錯誤的資訊價值遠高於完全無關的錯誤，例如 \(2+2=19\)。

因此提出：

\[
\boxed{
\text{Negative Data Value}
\propto
\text{Structural Proximity}
\times
\text{Failure Informativeness}.
}
\]

好的負樣本不是越荒謬越好，而是越接近正確、越容易誤判、又越能被精確否證越好。

---

## 4. 八類核心錯誤算子

設命題的結構指紋為：

\[
\Phi(P)
=
(
\mathcal D,\mathcal O,\mathcal Q,\mathcal A,\mathcal R,\mathcal C,\mathcal K
).
\]

本文定義八種基本錯誤算子。

### 4.1 假設刪除

若：

\[
A_1\land A_2\Rightarrow C,
\]

生成：

\[
A_1\Rightarrow C
\]

或：

\[
A_2\Rightarrow C.
\]

記為：

\[
T^-_{\mathrm{assump}}.
\]

其目的不是假設刪除後一定錯，而是測試某假設是否必要。

### 4.2 量詞變異

例如：

\[
\forall x\,P(x)
\]

改成：

\[
\exists x\,P(x),
\]

或交換：

\[
\forall x\exists y
\]

與：

\[
\exists y\forall x.
\]

記為：

\[
T^-_{\mathrm{quant}}.
\]

### 4.3 定義域越界

若：

\[
\forall x\in D,\ P(x)
\]

被無條件擴張為：

\[
\forall x\in D',\ P(x),
\qquad D\subsetneq D',
\]

記為：

\[
T^-_{\mathrm{domain}}.
\]

### 4.4 方向反轉

若：

\[
A\Rightarrow B,
\]

生成：

\[
B\Rightarrow A.
\]

此操作不預設新命題為假，必須交給 verifier。

### 4.5 型別錯置

將 operator、relation 或 theorem 套用到不相容的對象型別。

記為：

\[
T^-_{\mathrm{type}}.
\]

形式系統在此類錯誤上具有明顯優勢，因為許多錯誤會在 elaboration 或 type checking 階段直接暴露。

### 4.6 局部推導污染

原證明：

\[
S_0\to S_1\to\cdots\to S_n.
\]

在第 \(k\) 步插入非法 transition：

\[
S_k
Rightarrow S_{k+1}'.
\]

得到錯誤 proof \(\pi'\)。

### 4.7 依賴失真

包括：

- 引用不存在的 lemma；
- circular dependency；
- 使用更強 theorem 偽裝成較弱前提；
- provenance 遺失；
- duplicate source 被誤當成獨立依據。

### 4.8 有限驗證誤升格

若：

\[
P(1),\ldots,P(N)
\]

皆成立，卻錯誤推出：

\[
\forall n\in\mathbb N,\ P(n),
\]

這不是計算錯，而是證據型態錯置：

\[
\boxed{
\text{finite computational support}

ot\Rightarrow
\text{universal proof}.
}
\]

---

## 5. 反例空間

若命題為 \(P(x)\)，定義：

\[
\boxed{
\mathcal C(P)
=
\{x\in D:\neg P(x)\}.
}
\]

若：

\[
\mathcal C(P)\neq\varnothing,
\]

則其中任意元素都是反例。

AI-native system 不應只找到任意反例，還可研究：

- 最小反例；
- 最簡反例；
- 邊界反例；
- 高對稱反例；
- 反例族；
- 反例生成規則；
- 反例密度。

因此 falsification 本身也能形成一個結構空間。

---

## 6. 最小失敗差

若真命題 \(P\) 經 mutation 變成錯誤命題 \(P'\)，寫成：

\[
P'=P+\Delta.
\]

定義：

\[
\boxed{
\Delta^\ast
=
\arg\min_{\Delta} d(\Delta)
}
\]

subject to：

\[
\operatorname{Valid}(P+\Delta)=0.
\]

稱為 Minimal Failure Delta。

它回答：

> 最少改什麼，就足以讓正確命題失效？

---

## 7. 最小修復差

給定錯誤命題 \(P^-\)，定義：

\[
\boxed{
\Delta_R^\ast
=
\arg\min_{\Delta_R}d(\Delta_R)
}
\]

subject to：

\[
\operatorname{Verified}(P^-+\Delta_R)=1.
\]

例如：

\[
x\ge0\Rightarrow x^2>0
\]

可以修成：

\[
x>0\Rightarrow x^2>0
\]

或：

\[
x\ge0\Rightarrow x^2\ge0.
\]

因此負資料不應只有：

\[
\text{false},
\]

而應附：

\[
\boxed{
\text{false}
+
\text{why}
+
\text{counterexample}
+
\text{minimal repair}.
}
\]

---

## 8. 反例證書

高品質負節點可以表示為：

```text
claim_id
parent_id
mutation_operator
failure_class
structural_distance
counterexample
counterexample_proof
failed_assumption_or_step
minimal_failure_delta
minimal_repair_delta
verification_system
axiom_dependencies
status
```

其中：

\[
\text{status}
\in
\{
\text{DISPROVED},
\text{ILL\_TYPED},
\text{DOMAIN\_INVALID},
\text{PROOF\_INVALID},
\text{UNKNOWN}
\}.
\]

必須禁止：

\[
\text{UNKNOWN}\to\text{FALSE}.
\]

---

## 9. 形式反例的價值

形式反例最好同時包含 witness：

\[
x^\ast
\]

以及可機械檢查的失敗證明：

\[
x^\ast\in D
\]

和：

\[
\neg P(x^\ast).
\]

因此：

\[
\boxed{
\text{Counterexample}
=
\text{Witness}
+
\text{Proof of Failure}.
}
\]

---

## 10. 從證明器到否證器

AI-native mathematics 不應只有：

\[
\operatorname{Prover}(P),
\]

還應有：

\[
\operatorname{Disprover}(P).
\]

完整 routing：

\[
P
\rightarrow
\begin{cases}
\operatorname{Prove}(P),\
\operatorname{Disprove}(P),\
\operatorname{FindMissingAssumption}(P),\
\operatorname{ReturnUnknown}(P).
\end{cases}
\]

若 \(P\) 是錯的，強迫 prover 不斷「證明」只會誘發 hallucinated lemmas、偷補假設與無效推導。

因此應先做：

\[
\boxed{
\text{Claim Triage}.
}
\]

---

## 11. Claim Triage

定義：

\[
\mathcal R(P)
\in
\{
\text{likely-provable},
\text{likely-false},
\text{ill-posed},
\text{underspecified},
\text{unknown}
\}.
\]

這不是最終真值判定，只是資源路由。

例如：

\[
\mathcal R(P)=\text{likely-false}
\]

時，可以優先執行 counterexample search。

---

## 12. Proof Repair 與錯誤局部化

設：

\[
\pi=(s_0,s_1,\ldots,s_n).
\]

定義第一個失敗位置：

\[
k^\ast
=
\min\{k:s_k
Rightarrow s_{k+1}\}.
\]

則 repair agent 不必重做整個 proof，而可以只處理：

\[
(s_{k^\ast},s_{k^\ast+1}).
\]

所以錯誤資料的粒度可以從：

\[
\text{whole proof wrong}
\]

縮小為：

\[
\boxed{
\text{first invalid edge}.
}
\]

這對 verifier、critic 與 repair model 都具有更高訓練價值。

---

## 13. 錯誤距離與課程式訓練

可以依結構距離建立 curriculum：

### Level 1
明顯錯誤。

### Level 2
單一條件錯誤。

### Level 3
單一量詞或 boundary 錯誤。

### Level 4
長證明中的單步錯誤。

### Level 5
形式表面合法，但偷換 definition 或 domain。

### Level 6
多條真 theorem 組合後產生非法 global inference。

越高階的負資料越集中在：

\[
d_S(P,P^-)\to0^+.
\]

即：

> 幾乎正確，只差一點。

---

## 14. 對抗式生成

定義：

\[
G^+=\text{Proposition/Proof Generator},
\]

\[
G^-=\text{Adversarial Mutator}.
\]

流程：

\[
P
\rightarrow
G^-(P)
\rightarrow
\{P_1^-,\ldots,P_n^-\}.
\]

再由 verifier：

\[
V(P_i^-)
\in
\{
\text{proved},
\text{disproved},
\text{invalid},
\text{unknown}
\}.
\]

如果 mutator 本來想生成錯誤命題，但某個 \(P_i^-\) 反而被正式證明成立，這不是垃圾結果，而可能是：

\[
\boxed{
\text{accidental theorem discovery}.
}
\]

---

## 15. 錯誤生成如何反過來產生新數學？

若命題 \(P\) 有假設：

\[
A_1,\ldots,A_n,
\]

系統逐一消融：

\[
P_{-A_1},
P_{-A_2},
\ldots,
P_{-A_n}.
\]

若結果分別為：

\[
P_{-A_1}\text{ disproved},
\]

\[
P_{-A_2}\text{ proved},
\]

\[
P_{-A_3}\text{ unknown},
\]

則立即產生：

1. \(A_1\) 的必要性證據；
2. \(A_2\) 可能冗餘；
3. \(A_3\) 成為新的 open question。

所以：

\[
\boxed{
\text{Attack}\rightarrow\text{Structure Discovery}.
}
\]

---

## 16. 「AI 邏輯潔癖」的工程化

大型模型有時會主動指出漏洞、邊界條件、隱含假設與定義衝突，但這種行為本身並不保證正確。

因此與其依賴模型性格，不如制度化成角色：

```text
AssumptionAuditor
CounterexampleHunter
BoundaryMutator
ProofCorruptor
DependencyChecker
RepairAgent
FormalVerifier
```

此時：

\[
\boxed{
\text{critical tendency}
\rightarrow
\text{research architecture}.
}
\]

---

## 17. 錯誤價值函數

不是所有錯誤都值得保存。

定義：

\[
V^-(P^-)
=
\alpha S+\beta M+\gamma C+\delta R-\lambda D,
\]

其中：

- \(S\)：structural proximity；
- \(M\)：minimality；
- \(C\)：counterexample clarity；
- \(R\)：repair value；
- \(D\)：duplicate/redundancy。

高價值負樣本應靠近真命題、錯得少但關鍵、可給明確反例、可定位失敗原因，並有清楚修復路徑。

---

## 18. 與有限計算證明的邊界

如果先嚴格證明：

\[
P
\iff
\bigwedge_{i=1}^{N}P_i
\]

且程式完整檢查所有有限 \(P_i\)，則計算可以成為證明鏈的一部分。

但若只有：

\[
P(1),\ldots,P(N)
\]

成立，而原命題是：

\[
\forall n\in\mathbb N,\ P(n),
\]

則仍只是有限支持。

因此 error generator 應大量產生：

\[
\boxed{
\text{Proof-Type Confusion Cases}.
}
\]

讓模型學會區分：

- exhaustive finite proof；
- sampling；
- numerical evidence；
- symbolic derivation；
- formal proof；
- heuristic evidence。

---

## 19. 最小實驗

選擇 500 個已形式化基礎 theorem。

對每個 theorem 生成：

- 5 個 assumption-deletion variants；
- 5 個 quantifier/domain variants；
- 5 個 proof-step corruptions；
- 5 個 converse/generalization candidates。

得到約：

\[
10^4
\]

個候選錯誤或分叉節點。

每個節點經：

1. Lean parse/type check；
2. theorem prover；
3. counterexample search；
4. canonical deduplication；
5. failure classification；
6. minimal repair search。

比較：

### Model A
只用正確 theorem/proof data。

### Model B
加入結構化錯誤鄰域。

測：

- theorem validity classification；
- counterexample generation；
- missing-assumption detection；
- proof repair；
- false-premise resistance；
- formal proof success；
- OOD mutation robustness。

核心假說：

\[
\boxed{
\operatorname{Robustness}(B)
>
\operatorname{Robustness}(A).
}
\]

---

## 20. 研究邊界

本文不主張：

1. 所有錯誤都能自動找到反例；
2. theorem prover 無法證明即代表 theorem false；
3. 所有必要假設都能靠單一消融找到；
4. 最小反例在所有領域都存在或容易計算；
5. 結構距離已有唯一正確定義；
6. negative data 越多越好；
7. adversarial agent 的批評一定正確；
8. counterexample training 可以取代 proof training；
9. 數學 falsification 可無條件搬到哲學或經驗科學。

最重要的硬限制仍是：

\[
\boxed{
\text{Failure to prove}
\neq
\text{proof of failure}.
}
\]

---

## 21. 與現有工作的關係

2026 年的 *Learning to Disprove* 直接提出 formal counterexample generation：模型不只提出反例 candidate，還必須產生可由 Lean 4 自動驗證的形式證明；其 synthetic-data 方法之一正是系統性移除 theorem hypotheses，再建立反例任務。這是本文「假設消融 → 反例空間」的一個直接工程近鄰。

2025 年的 CounterMATH 從數學概念理解角度顯示，counterexample-driven reasoning 對現有數學 LLM 仍具明顯挑戰，並提出相應資料工程方法。

APOLLO 類 proof-repair pipeline 則展示了另一個互補方向：利用 Lean compiler 找出失敗子引理與錯誤位置，進行局部修復、重組與重新驗證，而非盲目重採樣整份 proof。

Lean 官方 proof-validation 文件也特別區分「形式 proof 是否被 kernel 接受」與「formal theorem statement 究竟是否正確對應 intended informal meaning」。因此 error neighborhood 最終仍必須同時管理形式錯誤與 statement/semantic mismatch。

---

## 22. 結論

AI 原生知識展開不能只有：

\[
\text{How can this be proved?}
\]

還必須制度化另一個問題：

\[
\boxed{
\text{How can this fail?}
}
\]

對每一個可靠命題 \(P\)，其高品質資料環境應同時包含：

\[
\mathcal E^+(P)
\]

與：

\[
\mathcal E^-(P),
\]

其中：

\[
\mathcal E^+(P)
=
\text{合法變種與證明鄰域},
\]

\[
\mathcal E^-(P)
=
\text{錯誤鄰域與反例空間}.
\]

完整知識節點因此不是只有：

\[
P+\text{Proof},
\]

而是：

\[
\boxed{
P
+
\text{Proof}
+
\text{Assumption Boundary}
+
\text{Counterexamples}
+
\text{Failure Modes}
+
\text{Repair Paths}.
}
\]

Paper I 建立基礎知識展開。

Paper II 建立變種身份與命題分叉。

Paper III 加入：

\[
\boxed{
\text{systematic falsification}.
}
\]

到這裡，BKSE 才第一次同時具有：

\[
\text{生成}
+
\text{區分}
+
\text{攻擊}.
\]

下一篇將進入：

\[
\boxed{
\text{Multi-Proof and Cross-Verification Architecture}.
}
\]

也就是：同一命題為什麼不應只保存一條 proof，以及 AI 如何利用多證法、不同形式系統、不同 verifier 與不同推導路徑建立「證明晶格」，把單一路徑信任轉化成多路徑交叉驗證網路。

---

## 參考文獻

Li, Z., Li, Z., Yang, K., Ma, X., & Su, Z. (2026). *Learning to Disprove: Formal Counterexample Generation with Large Language Models*. arXiv:2603.19514.

Li, Y., Kuang, J., Huang, H., et al. (2025). *One Example Shown, Many Concepts Known! Counterexample-Driven Conceptual Reasoning in Mathematical LLMs*. arXiv:2502.10454.

Ospanov, A., & Yousefzadeh, R. (2025). *APOLLO: Automated LLM and Lean Collaboration for Advanced Formal Reasoning*. arXiv:2505.05758.

Lean Project. *Validating a Lean Proof*. Lean Language Reference.

Lean Project. *Lean.Meta.Tactic.BVDecide.Counterexample*. Lean API Documentation.
