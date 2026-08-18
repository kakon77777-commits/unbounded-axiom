# SDPE / BEB A–B–C 研究整理 v0.1

**Date:** 2026-08-15  
**Status:** research synthesis; source-grounded where indicated, higher-level unification explicitly marked as synthesis/inference.

---

# 1. 原始核心：SDPE Phase I

SDPE Phase I 的基本研究對象是未知反例集合的可靠上包絡：

$$
\mathcal C\subseteq\Omega_t,
$$

以及 theorem-guided contraction：

$$
\Omega_{t+1}=\Omega_t\cap H_t.
$$

八層 closure stack 可概括為：

$$
\boxed{
\begin{aligned}
&\text{P01 Survivor Soundness}\\
&\to\text{P02 Representation Faithfulness}\\
&\to\text{P03 Global Coverage / Closure}\\
&\to\text{P04 Trace Compilation / Incremental Replay}\\
&\to\text{P05 Discovery--Verification Dynamics}\\
&\to\text{P06 Exceptional-Core Geometry}\\
&\to\text{P07 Enclosure Routing}\\
&\to\text{P08 Runtime / Benchmark / Observatory}.
\end{aligned}
}
$$

Phase I 最低原則：

$$
\boxed{
\text{走對 proof domain}
+
\text{保存可重播痕跡}
+
\text{只讓 certificate 改變 authoritative survivor state}.
}
$$

---

# 2. BEB 基礎實驗：從理論框架到可攻擊 benchmark

BEB 的第一個作用不是證明未知數學，而是把 SDPE 的 authority rules 變成可攻擊系統。

第一輪實驗暴露出重要 distinction：

$$
\boxed{
\text{label correct}
\neq
\text{route closed}
\neq
\text{submission valid}
\neq
\text{certified closure}.
}
$$

這一階段的價值不只是 benchmark 結果，而是發現：

$$
\boxed{
\text{局部 verifier PASS}
\not\Rightarrow
\text{dataset / audit / global authority 完整}.
}
$$

多 AI recursive audit 亦顯示不同 reviewer 的漏洞覆蓋並非單調包含，較像互補集合。

---

# 3. A 線：Proof Learning Dynamics

A 線版本譜系：

$$
\boxed{
\begin{aligned}
&v0.3\ \text{Lemma Discovery}\\
&\to v0.4\ \text{Proof DAG}\\
&\to v0.5\ \text{Proof Quality}\\
&\to v0.6\ \text{Proof Search}\\
&\to v0.7\ \text{Adaptive Proof Space}\\
&\to v0.8\ \text{Reusable Lemma Library}\\
&\to v0.9\ \text{Selective Transfer}\\
&\to v0.10\ \text{Confidence Memory}.
\end{aligned}
}
$$

## 3.1 第一個相變：route selection -> lemma generation

v0.3 不再把有用 derived action 預先給 participant，而要求 participant 自行提出可驗證 lemma。

這使研究對象由：

$$
\text{choose}(a\in\mathcal A)
$$

轉成：

$$
\text{generate}(\ell)
\to
\text{verify}(\ell)
\to
\text{use}(\ell).
$$

## 3.2 第二個相變：固定 proof space -> adaptive proof space

v0.7 把 fact pool 寫成：

$$
F_0\to F_1\to\cdots\to F_k,
$$

每一個 accepted novel lemma 都會改變下一輪可合法提出的 proof region：

$$
\mathcal R(F_k).
$$

因此 proof space 本身成為動態對象：

$$
\boxed{
\mathcal P_0
\subseteq
\mathcal P_1
\subseteq
\mathcal P_2
\subseteq\cdots.
}
$$

## 3.3 第三個相變：單題 proof -> 跨題 memory / transfer

v0.8--v0.10 使 certified proof history 從同題 replay infrastructure 變成跨 task prior：

$$
\boxed{
\text{proof history of }P_i
\to
\text{candidate prior for }P_{i+1}.
}
$$

但 v0.9 / v0.10 同時拒絕「永遠 reuse」：

$$
\text{retrieve}
\to
\text{applicability / confidence gate}
\to
\text{reuse, probe, reject, or reset}.
$$

而 bounded active memory 使：

$$
M_{t+1}
\not\supseteq
M_t
$$

成為可能。

## 3.4 A 線的核心狀態

可抽象為：

$$
\boxed{
A_t=(\mathcal K_t,M_t,\Pi_t^{\rm learn}),
}
$$

其中：

- $\mathcal K_t$：累積 certified proof knowledge；
- $M_t$：當前 active reusable memory；
- $\Pi_t^{\rm learn}$：生成、檢索、probe、transfer、eviction policy。

A 線主要問題：

$$
\boxed{
\text{證明者如何形成、保存、重組與遷移可驗證知識？}
}
$$

---

# 4. B 線：Certified Proof-Control Dynamics

B 線版本譜系：

$$
\boxed{
\begin{aligned}
&v0.2.0\ \text{Managed Query Evaluator}\\
&\to v0.3.0\ \text{Restricted Observation Certification}\\
&\to v0.4.0\ \text{Exact Optimal Adaptive Certification}\\
&\to v0.5.0\ \text{Shared Global Budget}\\
&\to v0.6.0\ \text{Posterior-State Bellman}\\
&\to v0.7.0\ \text{Horizon Bisimulation Quotient}\\
&\to v0.8.0\ \text{Dual-Sandwich Action Pruning}\\
&\to v0.9.0\ \text{Context-Sensitive Occupancy Duality}\\
&\to v1.0.0\ \text{Proof-Carrying Bellman Certification}.
\end{aligned}
}
$$

## 4.1 核心轉折：query count 不是充分狀態

v0.6 發現同樣的 query age 可以對應不同 continuation value，因此粗狀態表示會丟失 proof-control relevant information。

狀態必須升級為 posterior state：

$$
b_t.
$$

共享 budget 下形成 Bellman control：

$$
V_q(\mathbf N)
=
\max_a
\mathbb E[
r(a)+V_{q-1}(\mathbf N')
].
$$

## 4.2 v0.7：exact compression without information loss

state explosion 之後，v0.7 沒有退回粗 feature compression，而建立 finite-horizon behavioral equivalence：

$$
s\sim_h t
$$

僅當剩餘 horizon $h$ 內 reward / successor-equivalence behavior 完全一致。

因此：

$$
\boxed{
\text{behavioral equivalence}
\Rightarrow
\text{exact Bellman quotient}.
}
$$

這是 P02 Representation Non-Collapse 的控制論實例。

同版並把 finite rational recursion integerize：

$$
Z_h=D_hV_h,
$$

使 exact Bellman 可由大整數運算完成。

## 4.3 v0.8--v0.9：不安全的 state compression 改成可證 action compression

對 action $a$ 建立：

$$
Q_h(a;S)\le U_h(a;S)
$$

並以可執行 policy 得到：

$$
L_h(S)\le V_h(S).
$$

若：

$$
U_h(a;S)\le L_h(S),
$$

則 action 可安全 prune。

v0.9 再把 local scalar priority 的失敗提升為 context-sensitive relation：

$$
a\preceq_{S,h}b.
$$

所以 B 線逐步形成：

$$
\boxed{
\text{state quotient only when exact}
+
\text{otherwise certificate-prune actions}.
}
$$

## 4.4 v1.0：Proof-Carrying Bellman

v1.0 的 trust boundary：

$$
\boxed{
\text{untrusted discovery}
\to
\text{exact policy evaluation}
\to
\text{layered exact certification}.
}
$$

numerical search 可以錯；它沒有 theorem authority。

只有 exact evaluation + alternative-action certificates 可決定 optimality。

## 4.5 B 線核心狀態

可抽象為：

$$
\boxed{
B_t=(b_t,q_t,\Pi_t^{\rm ctrl},\mathcal V_t),
}
$$

其中：

- $b_t$：posterior / information state；
- $q_t$：remaining resource budget；
- $\Pi_t^{\rm ctrl}$：adaptive proof-control policy；
- $\mathcal V_t$：exact value / upper-lower certificate envelope。

B 線主要問題：

$$
\boxed{
\text{在有限資訊、有限資源與嚴格 trust boundary 下，下一步如何最優且可證？}
}
$$

---

# 5. C 線：Observer-Network Causal Epistemics

C 線不是繼續改 proof algorithm，而是研究：

$$
\boxed{
\text{我們如何知道 memory / observer architecture 真正改變了 Agent behavior？}
}
$$

目前 REAL RUN 001 明確仍是 instrumented causal pilot 設計，不是已完成 empirical result。

## 5.1 核心問題

C 線研究 proof rollback 後：

$$
\text{authoritative proof state}
$$

可以重新張開，但已驗證失敗的知識是否產生：

$$
\boxed{
\text{epistemic hysteresis}.
}
$$

即：

$$
\text{rollback}
\to
\text{persistent negative knowledge}
\to
\text{repair}
\to
\text{reclosure}.
$$

## 5.2 Memory causal arm

$$
M^+
=
\text{repair public view}
+
\text{verified failure-memory},
$$

$$
M^-
=
\text{same repair public view}
+
\text{matched neutral artifact}.
$$

兩者都使用 fresh repair session，以避免：

$$
\text{memory content effect}
$$

與

$$
\text{session continuity / prompt-volume effect}
$$

混淆。

## 5.3 Architecture causal arm

REAL RUN 001 合法比較的是：

$$
ON_{\rm pkg}
\quad\text{vs}\quad
SA_{\rm pkg},
$$

而不是直接宣稱 pure role separation。

因為 system package 同時改變 agent count、independent sampling、context independence、communication topology 等。

## 5.4 Literal cache vs semantic enclosure

若 memory 只讓 Agent 不再提出同一個 literal route：

$$
IRR_{\rm literal}\downarrow,
$$

最保守解讀是 negative cache。

若連未直接列出的 semantic-equivalent dead routes 也下降：

$$
IRR_{\sim}^{\rm pre}\downarrow,
$$

才有較強 evidence：

$$
\boxed{
\text{verified negative knowledge}
\to
\text{semantic search-space pruning}.
}
$$

## 5.5 C 線核心狀態

可抽象為：

$$
\boxed{
C_t=(\mathcal E_t,\mathcal O_t,I_t,\Gamma_t),
}
$$

其中：

- $\mathcal E_t$：可觀察／declared epistemic route state；
- $\mathcal O_t$：frozen route ontology / semantic equivalence；
- $I_t$：memory / architecture / rollback interventions；
- $\Gamma_t$：observer ledger + causal estimands。

C 線主要問題：

$$
\boxed{
\text{如何把「AI 看起來學到了」變成可反駁的 causal statement？}
}
$$

---

# 6. A / B / C 並不是三個相同實驗

最乾淨的分工是：

$$
\boxed{
\begin{array}{c|c|c}
A & B & C\\
\hline
\text{Learning} & \text{Control} & \text{Causal Validation}\\
\mathcal K_t & (b_t,q_t) & \mathcal E_t\\
\text{如何變強} & \text{下一步怎麼做} & \text{怎麼知道真的有效}
\end{array}
}
$$

A/B 主要是 object-level proof dynamics。

C 是 meta-level experimental epistemology。

---

# 7. 與原始 SDPE 的重新統一

原始 SDPE 只有最突出的收縮方向：

$$
\Omega_{t+1}\subseteq\Omega_t.
$$

A 線補出知識擴張：

$$
\mathcal K_t\subseteq\mathcal K_{t+1}.
$$

但 active memory 不必單調：

$$
M_{t+1}\not\supseteq M_t.
$$

B 線補出 belief/resource dynamics：

$$
(b_t,q_t)
\xrightarrow{\Pi_t}
(b_{t+1},q_{t+1}).
$$

C 線則提出一個仍待 empirical testing 的 epistemic-search contraction：

$$
\mathcal E_{t+1}
\stackrel{?}{\subseteq}
\mathcal E_t
$$

在 verified failure memory 介入後是否成立，以及 rollback 後是否出現 hysteresis。

因此新的統一狀態可暫寫成：

$$
\boxed{
\mathfrak X_t
=
(
\Omega_t,
\mathcal K_t,
M_t,
b_t,
q_t,
\Pi_t,
\mathcal E_t,
\mathcal H_t
).
}
$$

其中：

- $\Omega_t$：counterexample survivor space；
- $\mathcal K_t$：certified proof knowledge；
- $M_t$：active bounded memory；
- $b_t$：posterior information state；
- $q_t$：resource state；
- $\Pi_t$：learning / control / routing policy；
- $\mathcal E_t$：declared admissible epistemic route space；
- $\mathcal H_t$：proof / observer provenance history。

---

# 8. 目前最值得保留的理論分離

## 8.1 Truth != Proof

$$
\boxed{
\text{答案正確}
\neq
\text{證明合法}.
}
$$

## 8.2 Proof State != Epistemic State

$$
\boxed{
\text{proof rollback}
\neq
\text{epistemic rollback}.
}
$$

## 8.3 Search State != Certificate

$$
\boxed{
\text{untrusted search intelligence}
\neq
\text{proof authority}.
}
$$

## 8.4 Memory != Semantic Learning

$$
\boxed{
\text{literal blacklist avoidance}
\neq
\text{semantic epistemic enclosure}.
}
$$

## 8.5 Local Compression != Safe Representation

$$
\boxed{
\text{state compression}
\text{ only legal when proof/control relevant distinctions are preserved}.
}
$$

## 8.6 Better Package != Identified Component Cause

$$
\boxed{
ON_{\rm pkg}>SA_{\rm pkg}
\not\Rightarrow
\text{role separation alone caused the effect}.
}
$$

---

# 9. 現階段證據等級

### Level I — Formal / exact within released calculus

包括：

- survivor / certificate invariants；
- finite symbolic replay；
- A 線受限 calculus 下的 lemma / adaptive proof-space properties；
- B 線 finite-horizon Bellman / quotient / certification results；
- runtime authority separation。

### Level II — Controlled synthetic benchmark evidence

包括：

- routing traps；
- proof-space growth；
- lemma reuse / transfer / memory experiments；
- exact control comparisons。

這些支持「在該 benchmark / calculus 內」的機制，不等同未知數學的一般定律。

### Level III — Causal AI empirical evidence

目前仍未完成。

C 的 v0.4 / v0.5 明確仍要求：

$$
\boxed{
\text{preflight}
\to
\text{isolated REAL RUN}
\to
\text{post-freeze oracle scoring}.
}
$$

因此現在不能宣稱：

- persistent failure memory 已實證降低 AI repair cost；
- Observer Network 已實證降低 false certification；
- semantic epistemic enclosure 已實證存在。

---

# 10. 現在真正長出的 Phase II 問題

## Q1 — Dual-Space Coupling

是否存在可驗證條件，使：

$$
\Omega_t\downarrow
$$

伴隨：

$$
\mathcal K_t\uparrow
$$

並真正降低：

$$
D_t^{\rm frontier}?
$$

## Q2 — Learning–Control Coupling

若 proof memory / lemma library 本身會成長：

$$
\mathcal K_t\to\mathcal K_{t+1},
$$

B 線的 Bellman policy 應如何把「未來會學到新 lemma」納入 state？

## Q3 — Bounded-Memory Optimality

在：

$$
|M_t|\le B
$$

下，應保存哪些 proof objects，才能最佳化未來 discovery / certification cost？

## Q4 — Epistemic Hysteresis

proof rollback 後，如果：

$$
\Omega_t
$$

重新擴張，但：

$$
\mathcal E_t
$$

不完全重新張開，這個差值能否穩定、可重現、跨模型？

## Q5 — Semantic Negative Knowledge

verified failure memory 是否能超越 literal blacklist，對未見過但結構等價的 route 產生 transfer？

## Q6 — Observer-Network Decomposition

如何真正分離：

$$
\text{role separation},
\quad
\text{agent count},
\quad
\text{independent sampling},
\quad
\text{model heterogeneity},
\quad
\text{communication topology}?
$$

## Q7 — Joint Fixed Point

是否存在某種穩定 regime：

$$
\boxed{
(
\Omega_t,
\mathcal K_t,
M_t,
\Pi_t,
\mathcal E_t
)
\to
(
\Omega_*,
\mathcal K_*,
M_*,
\Pi_*,
\mathcal E_*
)
}
$$

使新增研究不再要求新的元層，而主要只需 existing invariant 下的 ordinary refinement？

---

# 11. 一句話總結

最初 SDPE 問：

$$
\boxed{
\text{如何把 counterexample space 包死？}
}
$$

A 線把它推成：

$$
\boxed{
\text{證明者如何長出新的可驗證 proof space？}
}
$$

B 線把它推成：

$$
\boxed{
\text{在有限資訊與成本下，如何最優且可證地控制 proof search？}
}
$$

C 線再問：

$$
\boxed{
\text{我們如何因果地知道這些 memory / architecture / observer 機制真的改變了 AI？}
}
$$

因此目前整個研究已從單一的「空間域證明包圍」自然展開成：

$$
\boxed{
\textbf{Proof-Space Learning}
+
\textbf{Certified Proof Control}
+
\textbf{Causal Epistemic Validation}.
}
$$

這三條線目前最好保持分離實驗，最後再做統一模型；過早合併反而會失去可辨識性。
