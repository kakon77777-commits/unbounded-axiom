# Paper 05 — 架構推理的跨 AI 可重現性

## Cross-Agent Reproducibility of Architecture Reasoning

**系列：** TDD × MSSP Architecture Backtrace and Fresh Reconstruction  
**系列代號：** ABFR Series  
**文件版本：** v0.1  
**日期：** 2026-08-28  
**作者：** Neo.K / EveMissLab  

---

## 摘要

Paper 01–04 已建立 ABFR（Architecture Backtrace and Fresh Reconstruction）的三閉包方法：Behavioral Closure、Structural Reconstruction Closure 與 Discriminative Closure。然而，只要方法仍主要由單一作者、單一 Agent、單一 repository 或單一既有上下文執行，就不能判斷成功究竟來自方法本身，還是特定模型能力、隱性上下文、熟悉工作區、工具配置或一次性的推理偶然性。

本文提出 **Cross-Agent Reproducibility of Architecture Reasoning（架構推理的跨 AI 可重現性）** 作為 ABFR 從方法設計走向通用性驗證的核心框架。其目標不是要求不同 AI 產生相同 private reasoning、檔案閱讀順序、工具呼叫序列或完全相同的 Minimal Sufficient Reconstruction Set。對存在合法替代 backend、不同 traversal route 與 stochastic policy 的 Agent 而言，要求 trace identity 不但沒有必要，也會錯誤懲罰合法差異。本文真正要求的是：在相同 canonical inputs、scope、execution contract、fresh context 與受控工具邊界下，不同執行者是否能獨立得到**可比較的結構結論、覆蓋必要 critical nodes、重建可接受的 architecture profile、重現必要 falsifying witnesses，並得到一致或可解釋差異的三閉包 verdict**。

本文將可重現性分為四層：**intra-agent repeatability、cross-agent reproducibility、cross-model transportability、cross-project generalizability**。並固定第一輪實驗條件：frozen repository revision、canonical ABFR specification、Inline Execution、禁止 sub-agent alternate path、相同工具與 authority contract、fresh session、predeclared replay equivalence、predeclared witness registry，以及所有 Additional Information Requests 的完整記錄。

本文定義 Critical Structural Coverage、Structural Jaccard、Relation Agreement、Divergence Detection、MSRS Equivalence-Class Agreement、Fresh Reconstruction Success、Witness Reproduction Rate、Three-Closure Verdict Agreement、Additional Information Request Rate、Human Intervention Count、成本與 run-to-run variance 等量測。其核心立場是：**單一 Agent run 不足以支持方法論可重現性；同一 Agent 的 repeatability 與不同 Agent 的 reproducibility 必須分開測。**

近期 repository-level Agent benchmark 已經暴露與本研究高度相關的問題。SWE-bench Verified 以人工驗證任務與 minimal execution setting 強化公平比較；Multi-Docker-Eval 指出 environment construction 仍是 Agent automation 的主要瓶頸之一；RepoReason 將 integration width 指認為 repository-level reasoning 的重要認知瓶頸；SWE-Mutation 顯示 LLM 生成 test suite 可能缺乏足夠 discriminative power；ReproEvalCard 則指出 LLM pipeline 評估若缺少 prompt、judge configuration、retrieval snapshot 與 intermediate traces，重現性會明顯受限。這些結果共同支持本文的實驗設計：不能只比較最終 pass rate，而必須控制 execution environment、保存可重播 evidence、執行多次獨立 rollout，並將方法輸出轉成可比較的結構狀態。

本文不宣稱 ABFR 已具跨 AI 可重現性，而將「其他 AI 是否也能獨立完成」轉換成可證偽問題，並作為後續 **Spec B — Cross-AI ABFR Validation Protocol v0.1** 的理論基礎。

**關鍵詞：** Cross-Agent Reproducibility；AI Coding Agent；ABFR；MSSP；Architecture Reasoning；Repository-Level Reasoning；Fresh Replay；Agent Evaluation；Structural Agreement

---

# 1. 從一次成功到方法成立

若某個 Agent $A$ 在 project $P$ 上成功執行 ABFR，只能得到：

$$
\exists A:
\operatorname{ABFRSuccess}(A,P)=1
$$

不能推出：

$$
\forall A,P:
\operatorname{ABFRSuccess}(A,P)=1
$$

更不能推出：

$$
\text{ABFR is a general methodology}
$$

因此本文研究的不是「ABFR 能不能被某個強 Agent 做到」，而是：

$$
\boxed{
\text{ABFR 是否能在移除原始 Agent 的條件下被重新執行}
}
$$

---

# 2. 核心研究問題

本文將基本問題寫成：

$$
\boxed{
\text{Same Method}
+
\text{Same Canonical Inputs}
+
\text{Fresh Executor}
\overset{?}{\Longrightarrow}
\text{Comparable Structural Conclusions}
}
$$

右側刻意不是：

$$
\text{Identical Reasoning Trace}
$$

而是：

$$
\text{Comparable Structural Conclusions}
$$

因為不同 Agent 可以合法採取不同路徑。

---

# 3. 可重現性不等於 Trace Identity

Paper 03 已定義一個 target $Q$ 可能存在多個合法 MSRS：

$$
S_A,S_B\in\mathfrak M_Q
$$

且：

$$
S_A\neq S_B
$$

但：

$$
\mathcal R(S_A,E_f)
\equiv_{Q,\mathcal I}
\mathcal R(S_B,E_f)
$$

因此 Agent 1 找到 $S_A$ 、Agent 2 找到 $S_B$，兩者都可能正確。

所以：

$$
\boxed{
\text{Reproducibility}
\neq
\text{Trace Identity}
}
$$

本文採：

$$
\boxed{
\text{Reproducibility}
=
\text{Constraint-Compatible Outcome Agreement}
}
$$

---

# 4. 四層可重現性

## 4.1 Intra-Agent Repeatability

同一模型、Agent shell、工具、repository 與 protocol，以 fresh session 重跑：

$$
A_i^{(1)},A_i^{(2)},\ldots
$$

是否能得到穩定核心結論？

它測：

$$
\text{run-to-run variance}
$$

而不是跨模型差異。

## 4.2 Cross-Agent Reproducibility

不同 Agent system：

$$
A_1,A_2,\ldots,A_n
$$

在相同 benchmark contract 下，是否能獨立重現 critical structure、fresh reconstruction、required witnesses 與 closure verdict？

## 4.3 Cross-Model Transportability

固定 Agent shell、工具與 protocol，只替換 underlying model：

$$
M_1,M_2,\ldots,M_n
$$

測方法是否依賴單一模型家族。

## 4.4 Cross-Project Generalizability

即使不同 AI 都能在 MSSP project 成功，也可能只是與 MSSP taxonomy 高度耦合。

因此必須比較：

$$
P_{\mathrm{MSSP}}
$$

與：

$$
P_{\mathrm{non-MSSP}}
$$

若 non-MSSP project 只要具有 explicit architecture、relations、tests 與 fresh boundary 也能執行 ABFR，才開始支持：

$$
\text{ABFR-MSSP}
\subseteq
\text{ABFR-General}
$$

---

# 5. Repeatability 先於 Reproducibility

若同一 Agent 的：

$$
\text{Repeatability}\approx 0
$$

那麼跨 Agent 差異很難解釋。

因此：

$$
\boxed{
\text{Repeatability First}
\rightarrow
\text{Cross-Agent Reproducibility}
}
$$

單次成功不能代表一個 Agent condition。

Agent 執行可能受到 sampling、planner branch、tool timing、search ordering、environment state、retry path、context compression 與服務狀態影響。

第一輪 pilot 建議：

$$
n_{\text{pilot}}\geq 3
$$

正式比較可從：

$$
n_{\text{formal}}\geq 5
$$

起步，再依觀察 variance 調整。這些是工程起點，不是統計學普遍定理。

---

# 6. Model Effect 與 Agent-System Effect

完整 Agent system 可以表示為：

$$
A_i=
(
M_i,
F_i,
T_i,
P_i
)
$$

其中：

- $M_i$：model；
- $F_i$：framework；
- $T_i$：tool set；
- $P_i$：policy / prompt / execution mode。

因此：

$$
\boxed{
\text{Model Effect}
\neq
\text{Agent-System Effect}
}
$$

若比較模型本身，應盡量固定：

$$
F,T,P
$$

只改：

$$
M
$$

若比較完整產品 Agent，則必須把 shell / framework 當成實驗變項，而不能把差異全部歸因於 model。

---

# 7. 第一輪固定 Inline Execution

本系列第一輪通用性驗證固定：

$$
\boxed{
\text{Execution Mode}
=
\text{Inline Execution}
}
$$

不提供：

- sub-agent alternate path；
- hidden worker；
- automatic delegation；
- secondary-model task splitting。

不是因為 multi-agent 不可行，而是要先降低 orchestration confound。

第一輪問題是：

$$
\boxed{
\text{Can one fresh executor follow ABFR end-to-end?}
}
$$

---

# 8. Frozen Experimental Baseline

每次 experiment 都必須固定：

$$
B
=
(
repo,
commit,
tests,
artifacts,
toolchain
)
$$

最低記錄：

```text
repository
commit SHA
working tree status
language/runtime versions
dependency lock identity
test command
ABFR protocol version
task ID
```

若：

$$
B_i\neq B_j
$$

則兩個 run 不應直接比較。

---

# 9. Canonical Input Packet

所有 executor 得到相同：

$$
I_C
=
\{
B,
Q,
R,
A_d,
\mathcal I,
\mathcal F,
\simeq_Q,
W,
\Pi
\}
$$

其中：

- $B$：baseline；
- $Q$：replay targets；
- $R$：behavioral requirements；
- $A_d$：declared architecture；
- $\mathcal I$：architecture invariants；
- $\mathcal F$：Freshness Contract；
- $\simeq_Q$：Replay Equivalence；
- $W$：witness registry；
- $\Pi$：execution protocol。

但 benchmark oracle 不應全部提供給 executor。

因此：

$$
I_C
=
I_{\text{executor}}
\cup
I_{\text{oracle}}
$$

例如 injected hidden dependency、critical nodes 與 hidden divergence 放在：

$$
I_{\text{oracle}}
$$

避免把答案寫進提示詞。

---

# 10. Fresh Session

每個 run：

$$
r_{i,j}
$$

必須建立新的 execution context：

$$
C_{\text{prior}}=0
$$

至少在 protocol 可控制範圍內：

- 不提供前一 run 對話；
- 不提供其他 Agent 結果；
- 不提供作者口頭補充；
- 不沿用 hidden notes；
- 不把上一 run 的 private reasoning 直接餵入。

允許重用 canonical artifacts 與經 Freshness Contract 明示的 materials。

---

# 11. Tool Capability 與 Authority Contract

工具能力：

$$
T_i
=
\{
t_1,\ldots,t_k
\}
$$

可能包括 file read、search、shell、tests、git、network、container、database、GUI。

第一輪應盡量固定 common denominator：

$$
T_{\cap}
=
\bigcap_iT_i
$$

若某 Agent 缺必要工具，應標記 capability-limited，而不是直接算 reasoning failure。

同時：

$$
\text{Capability}
\neq
\text{Authority}
$$

所以另固定：

```text
read source: yes
modify worktree: yes
run tests: yes
network: protocol-defined
push git: no
deploy: no
access secrets: no
```

---

# 12. Human Interaction 與 AIR

primary experiment 原則：

$$
\boxed{
\text{No non-canonical answer injection}
}
$$

若 Agent 詢問額外資訊，記錄：

$$
AIR
$$

包括 Paper 03 的：

- AIR-1 Canonical Navigation；
- AIR-2 Missing Documentation；
- AIR-3 Hidden Environment；
- AIR-4 Hidden Decision；
- AIR-5 Authority Request。

定義：

$$
N_{AIR}(r)
$$

並記：

$$
H_I(r)
$$

即非 canonical human interventions。

理想：

$$
H_I=0
$$

但 pilot 中 $H_I>0$ 本身就是「哪些資訊尚未進 canonical method」的研究結果。

---

# 13. 輸出不能只有 Final Answer

每個 run 必須輸出：

$$
O_r
=
(
B_r,
S_r,
M_r,
F_r,
R_r,
D_r,
W_r,
V_r,
C_r
)
$$

其中：

- $B_r$：backtrace result；
- $S_r$：structural coverage；
- $M_r$：MSRS candidate；
- $F_r$：freshness evidence；
- $R_r$：replay evidence；
- $D_r$：declared / observed / effective divergence；
- $W_r$：witness results；
- $V_r$：three-closure verdict；
- $C_r$：cost / interaction metrics。

不要求保存 private chain-of-thought。

需要保存的是：

$$
\boxed{
\text{Reproducible Evidence}
\neq
\text{Private Chain-of-Thought}
}
$$

例如 inspected artifacts、tool calls、frontier transitions、structured claims、test results 與 evidence links。

---

# 14. Structural Agreement

Agent $i$ 得到 structural node set：

$$
V_i
$$

可計算 exploratory Jaccard：

$$
J_V(i,j)
=
\frac{
|V_i\cap V_j|
}{
|V_i\cup V_j|
}
$$

但 Jaccard 不能作為唯一成功標準。

若 benchmark 已知 critical set：

$$
K^*
$$

則：

$$
CSC(i)
=
\frac{
|V_i\cap K^*|
}{
|K^*|
}
$$

稱為 Critical Structural Coverage。

同理 relation set：

$$
E_i
$$

可以計算：

$$
CRA(i)
=
\frac{
|E_i\cap E^*|
}{
|E^*|
}
$$

其中 $E^*$ 是 critical relation ground truth。

---

# 15. Divergence Detection

Controlled benchmark 可注入：

$$
D^*
=
\{
d_1,\ldots,d_m
\}
$$

例如：

- undeclared dependency；
- false modularity；
- authority leak；
- stale evidence；
- hidden runtime state。

Agent 回報：

$$
\hat D_i
$$

則：

$$
Precision_D
=
\frac{
|\hat D_i\cap D^*|
}{
|\hat D_i|
}
$$

$$
Recall_D
=
\frac{
|\hat D_i\cap D^*|
}{
|D^*|
}
$$

這讓 ABFR 可以與 TDD-only 直接比較 architecture-defect detection。

---

# 16. MSRS Agreement

不能要求：

$$
M_i=M_j
$$

因為多個合法 MSRS 可能同時存在。

應定義 equivalence class：

$$
[M]_{Q,\mathcal I}
$$

若：

$$
M_i
\sim_{Q,\mathcal I}
M_j
$$

即兩者都能 fresh reconstruct、replay equivalent 且保留 invariants，則：

$$
Agreement_{MSRS}(i,j)=1
$$

即使 literal set 不同。

這是「不同路徑、相容結論」的核心例子。

---

# 17. Fresh Reconstruction 與 Replay Metrics

對 run：

$$
FRS(r)
=
\begin{cases}
1,&\text{fresh reconstruction succeeds}\\
0,&\text{otherwise}
\end{cases}
$$

但失敗仍需依 Paper 03 分類：

$$
FR\text{-}01,\ldots,FR\text{-}07
$$

對 replay targets $q_k$，每個 Agent 輸出：

$$
v_{i,k}
\in
\{
PASS,
PARTIAL,
FAIL,
INCONCLUSIVE
\}
$$

若不同 Agent 使用相同：

$$
\simeq_Q
$$

卻得到不同 verdict，必須追查 evidence、environment、observation 或 reasoning 差異。

---

# 18. Witness Reproduction

Paper 04 定義 falsifying witness registry：

$$
W^-
$$

對 fresh Agent：

$$
A_i
$$

若能重現 witness $w$ 的 expected failure，記：

$$
Rep_i(w)=1
$$

定義：

$$
WRR_i
=
\frac{
\sum_{w\in W^-}Rep_i(w)
}{
|W^-|
}
$$

critical witness 可以要求：

$$
WRR=1
$$

若 Agent 找到 registry 之外的新有效反例：

$$
w_{\text{new}}
$$

則記 Novel Witness Discovery，但它是額外研究指標，不是基本 PASS 要求。

---

# 19. Three-Closure Verdict Agreement

每個 Agent 輸出：

$$
V_i
=
(
C_B,
C_S,
C_D
)
$$

與：

$$
V_{3C}
\in
\{
PASS,
PARTIAL,
FAIL,
INCONCLUSIVE
\}
$$

可以報：

- exact percent agreement；
- pairwise agreement；
- 適用時使用 Cohen's kappa、Fleiss' kappa 或 Krippendorff's alpha。

但：

$$
\boxed{
\text{Agreement}
\not\Rightarrow
\text{Correctness}
}
$$

如果所有 Agent 都犯同一錯誤，agreement 仍會很高。

所以 agreement 必須和 hidden oracle / injected ground truth 一起報。



# 20. Correctness 與 Reproducibility 必須分開

反過來：

$$
\text{Correctness}
\not\Rightarrow
\text{Reproducibility}
$$

如果每個 Agent 最後都修好功能，但：

- 有時漏 architecture divergence；
- 有時靠作者補充；
- 有時 fresh reconstruction 失敗；
- 有時 witness 無法重現；

則 final correctness 不足以支持 method reproducibility。

因此每個 experiment 至少同時報：

$$
\text{Task Correctness}
$$

與：

$$
\text{Method Reproducibility}
$$

---

# 21. Disagreement Taxonomy

不同 Agent verdict 不同時，至少分類：

### DG-01 Coverage Disagreement
某 Agent 沒看到 critical structure。

### DG-02 Relation Interpretation
節點相同，但 dependency / authority relation 判斷不同。

### DG-03 Effective-State Interpretation
對：

$$
A_e
$$

推導不同。

### DG-04 Equivalence Interpretation
對相同 replay output 是否：

$$
\simeq_Q
$$

判斷不同。

### DG-05 Evidence Weighting
看到相同 evidence，但可信度不同。

### DG-06 Tool Observation
實際 tool run 產生不同結果。

### DG-07 Environment Drift
benchmark environment 沒固定好。

### DG-08 Protocol Violation
Agent 沒遵守 ABFR procedure。

### DG-09 Benchmark Ambiguity
canonical instructions 本身不足。

### DG-10 Legitimate Alternative Architecture
不同結論都位於允許的 architecture equivalence class。

這個 taxonomy 比只報「模型不一致」更有診斷價值。

---

# 22. Run-to-Run Variance

對 scalar metric $m$：

$$
m_1,\ldots,m_n
$$

計算：

$$
\bar m
=
\frac{1}{n}
\sum_i m_i
$$

與：

$$
s_m
=
\sqrt{
\frac{
\sum_i(m_i-\bar m)^2
}{
n-1
}
}
$$

對 categorical verdict 則報 frequency、entropy 與 agreement。

如果同一 Agent 產生：

$$
PASS,FAIL,PASS,INCONCLUSIVE,PASS
$$

只報平均 pass rate 仍不足以描述其穩定性。

---

# 23. Stability Profile

每個 Agent 可有：

$$
S_A
=
(
S_{coverage},
S_{replay},
S_{witness},
S_{verdict},
S_{cost}
)
$$

這區分：

> 平均很好但非常不穩定

與：

> 每次都中等但高度穩定。

兩者在工程使用上是不同風險。

---

# 24. Cost Metrics

每個 run 記錄：

$$
C_r
=
(
T_r,
K_r,
N_r,
L_r,
H_r
)
$$

其中：

- $T_r$：tokens / context usage；
- $K_r$：tool calls；
- $N_r$：files / structural nodes inspected；
- $L_r$：wall-clock；
- $H_r$：human interventions。

若平台不提供某項數值，應記：

$$
UNKNOWN
$$

而不是推估假數字。

效率排序只能在相同 closure class 中比較：

$$
\boxed{
\text{Closure Correctness}
>
\text{Efficiency}
}
$$

---

# 25. 三級 Benchmark

## Tier 1 — Synthetic / Controlled

刻意注入：

- hidden dependency；
- false modularity；
- authority leak；
- stale evidence；
- wrong subject；
- untracked fixture。

這一層的優勢是：

$$
D^*
$$

與：

$$
K^*
$$

有明確 ground truth。

## Tier 2 — Small Real Repository

使用真實 project，但固定 commit、task、environment 與已知 architecture defect。

## Tier 3 — Large Repository / Long-Horizon

測：

- context traversal；
- revisit；
- environment reconstruction；
- integration width；
- multi-stage replay。

第一輪應先通過 Tier 1，再往大 repository 擴張。

---

# 26. Injected Defect 的要求

Injected defect 不應直接洩漏答案。

它應：

1. 符合原專案 code style；
2. 通過 baseline functional tests；
3. 不在 task text 中直接命名；
4. 能被 architecture backtrace 或 fresh reconstruction 揭露；
5. 具有 deterministic 或可驗證 oracle。

理想 benchmark 正是：

$$
\text{TDD-only passes}
$$

但：

$$
\text{ABFR should detect structural defect}
$$

---

# 27. 三個主要 Method Conditions

第一輪至少比較：

$$
G_0
=
\text{TDD-only}
$$

$$
G_1
=
\text{TDD + generic clean rerun}
$$

$$
G_2
=
\text{TDD + ABFR}
$$

其中 $G_1$ 非常重要，因為它回答：

> ABFR 的收益是來自「重新跑一次」，還是來自 structured backtrace + MSRS + freshness + witness closure？

保持相同 Agent、repository、requirement、工具與 budget，再比較：

$$
\Delta Recall_D
$$

$$
\Delta FRS
$$

$$
\Delta WRR
$$

$$
\Delta H_I
$$

與成本差。

---

# 28. MSSP 與 Non-MSSP Profile

再比較：

$$
P_M
=
\text{MSSP-native project}
$$

與：

$$
P_N
=
\text{non-MSSP project}
$$

ABFR method core 不變，只替換 architecture adapter。

定義：

$$
\mathcal A_{adapter}
:
A_{\text{native}}
\rightarrow
A_{\text{neutral}}
$$

neutral representation 至少包含：

$$
\{
Entity,
Relation,
Responsibility,
Authority,
State,
Evidence
\}
$$

若只有 MSSP project 成功，就應稱：

$$
\text{MSSP-specific methodology}
$$

而不是直接聲稱 general methodology。

---

# 29. Adapter 也可能失敗

如果 native architecture 有重要 relation，但 adapter 漏掉：

$$
A_{\text{native}}
\not\rightarrow
A_{\text{neutral}}
$$

那麼 Agent backtrace 的漏失不能直接歸因於 model。

因此需要：

$$
Coverage_{adapter}
$$

或 controlled adapter tests。

這把：

$$
\text{Agent Failure}
$$

與：

$$
\text{Representation Failure}
$$

分開。

---

# 30. Cross-Agent Matrix

實驗空間可以寫成：

$$
\mathcal E
=
A
\times
P
\times
M
\times
R
$$

其中：

- $A$：Agent / model condition；
- $P$：project；
- $M$：method condition；
- $R$：repeated runs。

例如較完整設計：

$$
3\times3\times2\times5
=
90
$$

runs。

若第一輪資源有限，可先：

$$
3\times2\times2\times3
=
36
$$

runs。

這能初步回答：

1. 同一 AI 自己穩不穩？
2. ABFR 是否比 TDD-only 多抓架構缺陷？
3. 不同 AI 是否能使用同一 protocol？
4. MSSP / non-MSSP 是否皆有初步可行性？

---

# 31. Environment Reconstruction 是一級指標

Multi-Docker-Eval 的 2026 結果顯示，environment construction 本身仍是 software engineering Agent 的重要瓶頸。

對 ABFR 而言這不是前置雜務。

Fresh Reconstruction 本來就要求：

$$
E_f
$$

可以被建立。

因此：

$$
\boxed{
\text{Environment Reconstruction}
}
$$

直接屬於：

$$
C_F
$$

與：

$$
C_R
$$

不能把：

> 測試在原工作區能跑

當成：

> architecture 可以 fresh reconstruct。

---

# 32. Repository-Level Integration Width

RepoReason 2026 的 repository-level white-box evaluation 指出 integration width 是重要認知瓶頸之一。

這與 Paper 02 的 Structural Attention 假說直接相鄰。

所以 experiment 應至少記錄 integration-width proxy：

- critical files；
- critical modules；
- relation hops；
- cross-layer dependencies。

再觀察：

$$
Performance
\sim
W_I
$$

是否隨 integration width 上升而下降。

---

# 33. Test Discriminative Power 不能由 Agent 自我宣告

SWE-Mutation 顯示 LLM 生成 test suite 可能表面完整但 discriminative power 仍不足。

因此不能讓 executor：

1. 自己寫 test；
2. 自己決定 test 足夠；
3. 只用自己那套 test 宣告成功。

至少 critical witness 必須由 frozen registry、hidden mutation 或 independent evaluator 提供外部約束。

這正是 Paper 04 的：

$$
C_D
$$

在 cross-agent experiment 中的必要性。

---

# 34. Evaluation Artifact Reproducibility

ReproEvalCard 對 LLM pipeline 評估的核心提醒是：模型與 dataset 不足以重現 pipeline evaluation，還需要 prompt、judge configuration、retrieval snapshot 與 intermediate traces 等 artifact。

ABFR evaluation 同樣需要：

```text
canonical protocol
repository revision
architecture snapshot
tool capability contract
authority contract
freshness evidence
replay target definitions
equivalence profile
witness registry
structured run trace
verdict
```

換言之：

$$
\boxed{
\text{A reproducibility methodology itself needs reproducible evaluation artifacts}
}
$$

---

# 35. Experiment Package

每個 experiment condition 建議輸出：

```text
experiment/
  manifest.json
  canonical-input/
  oracle/
  runs/
    agent-A-run-01/
    agent-A-run-02/
    agent-B-run-01/
  evaluation/
  summary/
```

其中：

$$
\text{oracle}
$$

在 executor 執行期間不可見。

每個 run manifest 至少有：

```text
run_id
agent_id
model_id
agent_shell
protocol_version
repo_commit
method_condition
execution_mode
tool_contract
authority_contract
freshness_mode
start_time
end_time
final_verdict
```

---

# 36. Structural Trace

不要求 private reasoning，但需要可重播 trace event：

```text
visited_node
relation_followed
evidence_read
claim_created
claim_resolved
claim_unresolved
frontier_added
frontier_closed
test_executed
reconstruction_step
witness_executed
```

這使我們比較的是：

$$
\text{architecture traversal}
$$

而不是自然語言思考內容。

---

# 37. Protocol Compliance 與 Method Uptake

若 Agent 最後修對功能，但跳過：

- backtrace；
- fresh reconstruction；
- replay；
- attack；

則：

$$
\text{Task Success}=1
$$

但：

$$
\text{ABFR Compliance}=0
$$

不能算 ABFR 成功。

因此定義：

$$
PC(r)
$$

為 Protocol Compliance。

另定義：

$$
MU(r)
$$

為 Method Uptake。

最低 Method Uptake 要有 actual backtrace、fresh reconstruction、replay、witness execution 與 evidence emission。

所以：

$$
\boxed{
\text{Vocabulary Adoption}
\neq
\text{Method Adoption}
}
$$

---

# 38. Blindness Levels

Cross-AI experiment 可分：

### B0 — Open
Agent 知道 defect 類型。

### B1 — Method-Blind Defect
Agent 知道 ABFR，但不知道 injected defect。

### B2 — Partial Blind
Agent 知道 project area，不知道 exact target node。

### B3 — Fully Hidden Oracle
Agent 只收到正常 task，所有 defect truth 都由 evaluator 保留。

第一輪最合理的是：

$$
B1
$$

因為我們要測「知道方法後，能不能自己找到未透露的 architecture defect」。

---

# 39. Leakage 與 Contamination

Benchmark 必須檢查：

- filenames；
- comments；
- issue text；
- commit messages；
- test names；
- generated artifacts；

是否洩漏 oracle。

公共 GitHub repository 也可能存在 training contamination，因此第一輪最好混合：

- newly generated controlled benchmark；
- recent injected mutation；
- public real repository。

最可靠的 hidden defect 應在 experiment 建立後注入。

---

# 40. Cross-Agent Independence

Primary experiment 要求：

$$
O_i
\cap
Context_j
=
\varnothing
$$

對：

$$
i\neq j
$$

即 Agent B 不能看到 Agent A 的結果。

所有 independent runs 完成後，才可做 secondary：

$$
\text{Peer Review Phase}
$$

研究 evidence exchange 後的 convergence。

但：

$$
\boxed{
\text{Consensus}
\not\Rightarrow
\text{Truth}
}
$$

仍需 external oracle。

---

# 41. 可接受與不可接受的差異

通常可接受：

- 讀檔順序不同；
- tool call order 不同；
- equivalent MSRS；
- 合法 backend 不同；
- 額外但無害的 structural nodes；
- 不同自然語言命名；
- 不同效率。

通常不可接受：

- 漏掉 critical hidden dependency；
- authority verdict 相反；
- 一方靠 hidden context 才能 fresh reconstruct；
- critical falsifying witness 一方通過；
- replay equivalence 被 post-hoc 放寬；
- unresolved 被當作 PASS；
- critical three-closure verdict 相反且無法解釋。

---

# 42. General-Method Success Criterion

通用方法不要求所有模型永遠成功。

比較合理的是：

$$
P(
G_{3C}=1
\mid
ABFR
)
$$

相對於：

$$
P(
G_{3C}=1
\mid
control
)
$$

是否提高，以及：

$$
P(
\text{critical defect detected}
\mid
ABFR
)
$$

是否提高。

通用方法論的意義是：

> 多種 executor 能使用、效益可被重複觀察、失敗邊界可以描述。

而不是：

> 每一個 AI 永遠成功。

---

# 43. Capability Threshold

如果某些 Agent 穩定成功，另一些總是失敗在 Backtrace Frontier Management，這可能表示存在：

$$
\theta_{ABFR}
$$

使：

$$
Capability(A)\geq\theta_{ABFR}
$$

時方法才實用。

這仍是有價值的結果。

ABFR 不需要對最弱模型也成立，才可以成為工程方法；但最低能力邊界必須被實驗描述。

---

# 44. Failure Anatomy

每個 run 的 stage vector：

$$
Z_r
=
(
z_B,
z_{BT},
z_{REC},
z_{MS},
z_F,
z_R,
z_D
)
$$

其中每個：

$$
z_i
\in
\{
PASS,
PARTIAL,
FAIL,
INCONCLUSIVE
\}
$$

分別代表：

- Behavioral；
- Backtrace；
- Reconciliation；
- MSRS；
- Freshness；
- Replay；
- Discrimination。

這比只發一個 leaderboard score 更重要。

---

# 45. Primary Endpoints

第一輪建議 primary endpoints：

1. Critical Structural Coverage；
2. Injected Divergence Recall；
3. Fresh Reconstruction Success；
4. Critical Witness Reproduction；
5. Three-Closure Verdict Correctness；
6. Human Intervention Count。

Secondary endpoints：

- Structural Jaccard；
- Relation Jaccard；
- tool calls；
- tokens；
- wall time；
- MSRS cost；
- novel witness discovery。

---

# 46. 主要假說

## H1 — Cross-Agent Feasibility

存在至少兩個不同 executor：

$$
A_i\neq A_j
$$

能在相同 canonical inputs 與 fresh condition 下獨立完成：

$$
G_{3C}=1
$$

且不需：

$$
H_I>0
$$

## H2 — Architecture Defect Detection

相對 TDD-only：

$$
Recall_D^{ABFR}
>
Recall_D^{TDD}
$$

## H3 — Fresh Reconstruction

相對 generic handoff：

$$
FRS^{ABFR}
>
FRS^{generic}
$$

## H4 — Structural Agreement Exceeds Trace Agreement

不同 Agent 的 tool trace overlap 可以很低，但：

$$
CSC
$$

與：

$$
CRA
$$

仍高。

即：

$$
\boxed{
\text{Different Paths}
\rightarrow
\text{Compatible Structural Conclusions}
}
$$

## H5 — Multiple Valid MSRS

對可替換架構：

$$
M_i\neq M_j
$$

但：

$$
M_i
\sim_{Q,\mathcal I}
M_j
$$

支持 Paper 03 的：

$$
|\mathfrak M_Q|>1
$$

## H6 — Witness Registry Improves Verdict Stability

提供：

$$
W^+,W^-,W^{\equiv}
$$

應比 vague architecture rules 提升 $C_D$ 的跨 Agent一致性。

## H7 — Freshness Reveals Hidden Context Dependence

若 control 使用 previous state 而 PASS，但 fresh run FAIL 且可分類為 FR leakage，表示 ABFR 成功揭露 hidden causal support。

## H8 — Cross-Project Transport

MSSP 與 non-MSSP project 都能被多 Agent 執行，才支持 taxonomy independence。

---

# 47. Negative Result Criteria

下列都應視為重要負面證據：

1. 多數 Agent 無法理解 protocol；
2. backtrace 成本遠高於收益；
3. ABFR 與 TDD-only defect recall 無差；
4. fresh replay 大量失敗於 protocol 自身；
5. non-MSSP adapter 無法穩定建立；
6. MSRS 幾乎不可操作；
7. witness 維護成本過高；
8. Agent disagreement 無法由 evidence 解釋。

研究必須允許：

$$
\boxed{
\text{ABFR is not generally useful}
}
$$

成為合法結論。

---

# 48. Success Levels

## Level 0 — Anecdotal
單 Agent、單 project。

## Level 1 — Repeatable
同 Agent 多次 fresh run。

## Level 2 — Cross-Agent Reproducible
不同 Agent 成功。

## Level 3 — Cross-Model Transportable
固定 shell 下不同模型成功。

## Level 4 — Cross-Project Generalizable
MSSP / non-MSSP profile 均成功。

## Level 5 — Comparative Benefit
相對 control 具有明顯工程與統計優勢。

只有 Level 4–5 才適合較強地稱：

$$
\text{general methodology}
$$

---

# 49. 第一輪建議流程

### Phase A — Protocol Smoke Test
同一 Agent：

$$
3
$$

次 fresh run。

確認：

- Spec B 沒歧義；
- output schema 可用；
- benchmark 可 reset；
- oracle 沒洩漏。

### Phase B — Cross-Agent Pilot
三個 AI 各：

$$
3
$$

次。

### Phase C — Method Control
同一三個 AI 跑 TDD-only、generic clean rerun 與 ABFR。

### Phase D — Non-MSSP Transfer
再加入至少一個 non-MSSP project。

---

# 50. Experiment Integrity Gate

在解讀 Agent 結果前，先驗：

$$
G_E
=
B_F
\land
T_F
\land
A_F
\land
C_F
\land
O_H
$$

其中：

- $B_F$：baseline frozen；
- $T_F$：tool contract fixed；
- $A_F$：authority fixed；
- $C_F$：fresh context；
- $O_H$：oracle hidden。

若：

$$
G_E=0
$$

該 run 不應進 primary comparison。

---

# 51. Protocol Violation

若 Agent：

- 使用不允許的 sub-agent；
- 讀 oracle；
- 使用 previous run artifact；
- 跳過 fresh reconstruction；
- 修改 hidden test；
- result 出來後才修改 equivalence；

則標：

$$
PV
$$

Protocol Violation。

final result 就算正確，也不能保留為 ABFR primary success。

---

# 52. Cross-Agent Reproducibility Criterion v0.1

對 project-task：

$$
(P,Q)
$$

若至少兩個獨立 executor：

$$
A_i,A_j
$$

在多次 fresh runs 中：

1. protocol compliance 成立；
2. critical structural coverage 達門檻；
3. critical divergence 被識別；
4. fresh reconstruction 成功；
5. critical witnesses 正確重現；
6. three-closure verdict 與 oracle 相容；
7. 不依賴非 canonical human intervention；

則稱：

$$
\boxed{
CAR(P,Q)=1
}
$$

其中：

$$
CAR
=
\text{Cross-Agent Reproducibility}
$$

CAR 不要求所有 AI 都成功。

---

# 53. Method Generalization Criterion

令 project family：

$$
\mathcal P
=
\{
P_1,\ldots,P_k
\}
$$

若：

$$
CAR(P_i,Q_i)=1
$$

跨越至少兩種不同 architecture profile，且至少一種不是 MSSP-native，則可以標記：

$$
G_{method}
=
\text{SUPPORTED}
$$

而不是：

$$
\text{PROVEN}
$$

有限 benchmark 永遠不等於 universal proof。

---

# 54. 為什麼現在不能先寫 Paper 06

Paper 06 預定為：

## A Multi-Agent Empirical Evaluation of Architecture Backtrace and Fresh Reconstruction

目前還沒有 cross-agent dataset。

所以現在不應預先寫：

- 成功率；
- effect size；
- p-value；
- model ranking；
- generality conclusion。

Paper 05 到此只建立 protocol-ready research design。

---

# 55. 對 Spec B 的直接要求

Spec B 至少固定：

```text
EXPERIMENT_ID
RUN_ID
AGENT_ID
MODEL_ID
AGENT_SHELL
REPOSITORY
COMMIT
METHOD_CONDITION
EXECUTION_MODE=INLINE
FRESH_CONTEXT=true
TOOL_CONTRACT
AUTHORITY_CONTRACT
TARGETS
INVARIANTS
EQUIVALENCE_PROFILE
WITNESS_REGISTRY
OUTPUT_SCHEMA
STOP_CONDITIONS
PROTOCOL_VIOLATIONS
```

並明確：

```text
SUBAGENT_PATH = NOT PROVIDED
```

停止條件至少包括：

1. three-closure PASS；
2. blocking FAIL；
3. critical unresolved；
4. environment impossible under contract；
5. budget exhausted；
6. protocol violation。

---

# 56. Evaluator

Evaluator 最好與 executor 分開。

優先序：

$$
\boxed{
\text{Executable / Deterministic Oracle}
>
\text{Frozen External Judge}
>
\text{LLM-Only Judge}
}
$$

如果只能使用 LLM judge，至少固定：

- judge model；
- prompt；
- temperature；
- rubric；
- judge count。

---

# 57. Method-Level Fresh Replay

整個系列最初來自一個意外：某個本地 Agent 在精確 TDD plan 後，自主提出在進入 Direct runtime / UI 前先做 MSSP fresh replay。

Paper 01–04 把這個一次性組合抽象化。

Paper 05 現在做最後一個必要動作：

$$
\boxed{
\text{Remove the original Agent from the experiment}
}
$$

如果換掉原始 Agent，方法仍能被另一個 fresh executor 重建，才開始說明：

> 被發現的不是某一個 Agent 的個人技巧，而是一個可轉移的方法。

這形成一個遞迴：

ABFR 對 software system 問：

$$
\text{Can architecture reconstruct the system?}
$$

Paper 05 對 ABFR 自己問：

$$
\boxed{
\text{Can specification reconstruct the method in another AI?}
}
$$

如果：

$$
\text{ABFR Spec}
+
\text{Fresh AI}
\rightarrow
\text{Comparable ABFR Execution}
$$

那麼 ABFR 自己也通過了一種：

$$
\text{Method-Level Fresh Replay}
$$

這不是循環論證，因為 benchmark 與 oracle 仍由外部固定。

---

# 58. 不宣稱事項

本文明確不宣稱：

1. 不同 AI 必須具有相同 reasoning trace。
2. 高 structural Jaccard 等於正確。
3. 高 agreement 等於 truth。
4. 同一模型一次成功代表 repeatability。
5. 三次 run 足以建立正式統計結論。
6. agent shell 差異可以忽略。
7. environment setup 只是測試雜務。
8. 工具能力不同也可直接公平比較。
9. public repository 完全沒有 training contamination。
10. non-MSSP 成功一次就證明 architecture independence。
11. cross-agent success 等於 universal applicability。
12. LLM judge 可以無條件取代 deterministic oracle。
13. sub-agent architecture 永遠不好。
14. Inline Execution 是最終最佳 architecture。
15. ABFR 已被證明比 TDD-only 更好。
16. ABFR 已被證明具 cross-agent reproducibility。

---

# 59. 結論

一個方法由某個強 AI 成功執行，只能證明：

$$
\exists A:
Success(A)=1
$$

不能證明方法具有通用性。

因此 ABFR 必須接受方法層的 fresh replay：

$$
\boxed{
\text{Method Specification}
+
\text{Fresh Independent AI}
\rightarrow
\text{Comparable Structural Execution}
}
$$

本文將這個問題拆成：

$$
\text{Repeatability}
$$

$$
\text{Cross-Agent Reproducibility}
$$

$$
\text{Cross-Model Transportability}
$$

$$
\text{Cross-Project Generalizability}
$$

真正應比較的不是私人 reasoning trace，而是：

$$
\boxed{
\text{Critical Structure}
+
\text{Divergence}
+
\text{Fresh Reconstruction}
+
\text{Witnesses}
+
\text{Three-Closure Verdict}
}
$$

健康的 cross-agent result 可以是：

$$
\text{Different Traversal Paths}
$$

但：

$$
\text{Compatible Architecture Conclusions}
$$

本文提出：

$$
CAR(P,Q)
$$

作為 Cross-Agent Reproducibility 的第一版操作定義，並建立 frozen baseline、canonical input、fresh context、fixed tools、fixed authority、Inline Execution、hidden oracle、repeated runs、TDD-only control、generic-rerun control、non-MSSP transfer 與 structured evidence output 的完整框架。

這使 ABFR Series 第一次真正具備「可以交給其他 AI 做盲測」的條件。

如果另一個 AI 無法由規格重建這個方法，我們就還沒有通用方法論。

如果不同 Agent、不同模型與不同 architecture profile 都能在 fresh condition 下反覆得到相容的三閉包結果，ABFR 才開始有資格從一次非常有價值的方法組合，轉變成：

$$
\boxed{
\text{a reproducible AI-assisted software engineering methodology}
}
$$

---

# 參考文獻

[1] SWE-bench. (2025–2026). *SWE-bench Verified*. Human-validated subset of 500 SWE-bench instances and standardized evaluation settings.

[2] Fu, K., Liu, T., Shang, Z., Ma, Y., Liu, J., Yang, J., & Bian, K. (2026). *Multi-Docker-Eval: A “Shovel of the Gold Rush” Benchmark on Automatic Environment Building for Software Engineering*. Findings of ACL 2026. DOI: 10.18653/v1/2026.findings-acl.889.

[3] Li, J., Su, Y., & Lyu, M. R. (2026). *From Laboratory to Real-World Applications: Benchmarking Agentic Code Reasoning at the Repository Level*. Proceedings of ACL 2026, 8845–8869. DOI: 10.18653/v1/2026.acl-long.399.

[4] Sun, Y., Zhao, Y., Wang, Y., Du, Y., Ma, Z., Wang, J., Zhang, M., Zhang, K., & Huang, Z. (2026). *SWE-Mutation: Can LLMs Generate Reliable Test Suites in Software Engineering?* Findings of ACL 2026, 39651–39674. DOI: 10.18653/v1/2026.findings-acl.1976.

[5] Pattnayak, P., & Bhatia, A. (2026). *ReproEvalCard: A Reporting Standard for Reproducible Evaluation of LLM Pipelines*. Proceedings of ACL 2026, Short Papers.

[6] Hans, A., & Bilionis, I. (2026). *Coding-agents can replicate scientific machine learning papers*. arXiv:2607.02134.

[7] Jha, S., Paltenghi, M., Maddila, C., Murali, V., Ugare, S., & Chandra, S. (2026). *ProdCodeBench: A Production-Derived Benchmark for Evaluating AI Coding Agents*. arXiv:2604.01527.

[8] Jiang, J., Zheng, S., Vidra, N., & Setty, S. (2026). *Beyond Pass@k: Measuring Reliability and Security of Agentic Code Generation*. arXiv:2608.14711.

[9] Neo.K / EveMissLab. (2026). *MSSP Field Manual 01–06 and Development Area*. thisoneisneok.com/mssp.

[10] Neo.K / EveMissLab. (2026). *ABFR Series Papers 01–04*.

---

## Canonical status

本文為 **ABFR Series Paper 05 v0.1**。

目前狀態：

- Cross-agent reproducibility question: defined.
- Repeatability / reproducibility / transportability / generalizability distinction: defined.
- Inline Execution control: fixed for first-round validation.
- Sub-agent alternate path: explicitly not provided.
- Canonical input packet: defined.
- Fresh-session policy: defined.
- Tool / authority contract: defined.
- Structured run output: defined.
- Structural coverage metrics: defined.
- Divergence detection metrics: defined.
- MSRS equivalence-class agreement: defined.
- Fresh reconstruction metric: defined.
- Witness reproduction metric: defined.
- Three-closure verdict comparison: defined.
- AIR / human intervention metrics: defined.
- TDD-only and generic-rerun controls: defined.
- MSSP / non-MSSP transfer design: defined.
- Cross-AI empirical results: pending.
- Statistical superiority claim: not made.
- General methodology claim: not yet established.

下一正式產出應為 **Spec A — ABFR Methodology v0.1**，接著 **Spec B — Cross-AI ABFR Validation Protocol v0.1**。Spec B 完成後即可開始第一輪 fresh cross-AI pilot。
