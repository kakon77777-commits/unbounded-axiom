# 疑點驅動的推理資源配置：Freeze Controller、Value of Information 與自適應 Specialist Routing

**Doubt-Driven Reasoning Allocation: Freeze Control, Value of Information, and Adaptive Specialist Routing**

**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-11

## 摘要

隨著大型語言模型與形式定理證明系統的 inference-time compute 持續擴張，數學 AI 面臨的問題已不再只是「能否投入更多推理資源」，而是「何時值得投入更多資源，以及資源應投入哪一種推理活動」。現有 adaptive test-time compute 研究主要依據問題難度、不確定性或預期正確率收益，決定對單一輸入增加多少 sampling、search 或 verification；多 Agent 形式數學系統則開始將自然語言推理、形式驗證、修復與 orchestration 分離。然而，對研究級數學問題而言，尚存在一個更上游的資源配置問題：當 theorem target 尚未完全穩定時，額外計算究竟應該用於量詞與定義域分析、來源版本核對、自然語言解釋、跨框架 bridge audit，還是應停止擴張並凍結問題？

本文提出 **Doubt-Driven Reasoning Allocation（DDRA）**，將 proof-search 前的 residual uncertainty 表示為多維 **residual doubt vector**：

$$
D_t=(D_F,D_S,D_B,D_P,\ldots),
$$

其中各維分別代表 formal-structural、source-fidelity、framework-bridge、perspective/pragmatic 等未決風險。系統維持一組認知 specialist：

$$
\mathcal M
=
\{
M_{\mathrm{MPF}},
M_{\mathrm{Source}},
M_{\mathrm{Bridge}},
M_{\mathrm{NLU}},
\ldots
\},
$$

並估計每個 specialist 的成本 $C(M_i)$ 與對 residual doubt 的預期消除量。由此定義：

$$
\operatorname{VOI}(M_i\mid D_t)
=
\frac{
\mathbb E[
V(D_t)-V(D_{t+1})
\mid M_i
]
}{
C(M_i)
},
$$

其中 $V(D)$ 是 unresolved doubt 的加權風險函數。

本文將推理控制分為兩個問題：

$$
\boxed{\text{Should I think more?}}
$$

以及：

$$
\boxed{\text{What should I think about next?}}
$$

前者由 **Freeze Controller** 決定；後者由 **VOI Specialist Scheduler** 決定。當 residual doubt 已低於 freeze threshold，或所有剩餘 specialist 的邊際 VOI 低於停止門檻時，系統停止語義擴張並形成 frozen theorem target；反之，選擇最高 VOI specialist 進行下一步審計。

本文整理一組由先前 error-injection 與 holdout-style experiments 所衍生的結構代理實驗。結果顯示，在既定人工標註與 proxy cost model 下，adaptive routing 可以在保持 corruption coverage 的同時顯著減少不必要 specialist calls；但本文明確不將這些結果解讀為實際 token、latency 或 theorem-prover speedup。本文的主要貢獻是提出一個可與真實 telemetry 接軌的推理資源治理模型，使數學 AI 從「固定流程的 solver」轉向「依問題狀態動態分配認知資源的 orchestrator」。

**關鍵詞：** Reasoning Allocation、Value of Information、Test-Time Compute、Specialist Routing、Freeze Controller、Residual Doubt、Mathematical AI、Agent Orchestration、Inference-Time Compute、Formal Theorem Proving

---

## 1. 引言

大型語言模型的 reasoning 能力可以透過增加 inference-time compute 改善。常見方法包括：

- repeated sampling；
- best-of- $N$ ；
- self-consistency；
- search；
- verifier reranking；
- extended reasoning；
- multi-agent decomposition。

然而，若所有輸入都使用相同計算量，系統會出現明顯浪費：

$$
\boxed{
\text{easy cases are over-computed,}
\qquad
\text{hard cases may remain under-computed.}
}
$$

2026 年的 adaptive test-time compute 研究已明確把問題寫成有限平均 budget 下的資源分配：哪些問題值得更多 sampling / reasoning，哪些問題可以低成本完成。Uncertainty-Aware Budget Allocation 以 per-question uncertainty 配置額外 sampling；Adaptive Test-Time Compute Allocation via Constrained Policy Optimization 則將 accuracy–cost trade-off 寫成 constrained optimization，再學習輸入到 compute action 的 allocation policy。ThinkBooster 更進一步將 test-time scaling strategy、scorer、quality–cost benchmark 與 deployable proxy service 整合成 runtime framework。

這些工作處理的是：

$$
\boxed{
\text{How much compute should this input receive?}
}
$$

本文研究另一個相鄰但不同的問題：

$$
\boxed{
\text{What kind of reasoning should receive the next unit of compute?}
}
$$

在研究級數學問題中，一個輸入可能同時存在：

- theorem statement 本身的 formal uncertainty；
- source formulation 是否選對的問題；
- hidden quantifier / witness dependency；
- framework bridge；
- representation provenance；
- natural-language perspective ambiguity。

因此，「多算一次」不是唯一 action。

下一個計算單位可能應該交給：

$$
M_{\mathrm{MPF}},
$$

也可能交給：

$$
M_{\mathrm{SourceFidelity}},
$$

或：

$$
M_{\mathrm{Bridge}},
$$

甚至：

$$
\boxed{
\text{誰都不要叫，直接 Freeze。}
}
$$

因此本文提出：

$$
\boxed{
\text{Doubt-Driven Reasoning Allocation}.
}
$$

---

## 2. 從 Compute Scaling 到 Cognitive Allocation

傳統 test-time compute allocation 可以抽象成：

$$
x
\rightarrow
b(x),
$$

其中 $b(x)$ 是輸入 $x$ 的 computation budget。

若 action 僅為增加 sample 數：

$$
b(x)\in\{1,2,\ldots,B\}.
$$

本文將 action space 擴張為：

$$
a_t
\in
\{
\operatorname{Freeze},
M_1,
M_2,
\ldots,
M_k
\}.
$$

其中 $M_i$ 不是單純不同 LLM，也可以是不同認知功能：

- formal-structure auditor；
- source-fidelity auditor；
- NLU interpreter；
- bridge auditor；
- counterexample searcher；
- premise retriever；
- Lean prover；
- CAS；
- numerical experiment agent。

因此：

$$
\boxed{
\text{Compute Quantity Allocation}
\subset
\text{Cognitive Resource Allocation}.
}
$$

本文的核心不是假定每個 specialist 必須由不同模型執行。

同一個 foundation model 也可以透過：

- 不同 system prompt；
- 不同 tool access；
- 不同 context；
- 不同 objective；
- 不同 verifier；

扮演不同 specialist。

因此 specialist 是 functional role，而不是必然等於 model identity。

---

## 3. 與多 Agent 形式數學的關係

形式數學系統已開始自然出現角色分離。

MA-LoT 使用多 Agent 結構，把自然語言長鏈推理與 Lean formal-language verification 結合。LeanMarathon 則建立一個 multi-agent harness，讓不同 contract-scoped agents 構建、審計、證明與修復共享 blueprint，並由 orchestrator 先穩定 target fidelity，再處理 proof DAG。

這些系統顯示：

$$
\boxed{
\text{Mathematical reasoning}
\neq
\text{one monolithic model call}.
}
$$

本文的延伸在於：

> 如果已經存在多種 Agent / cognitive roles，則上層系統還需要決定「何時叫誰」。

也就是：

$$
\boxed{
\text{Multi-Agent Architecture}
\neq
\text{Adaptive Agent Allocation}.
}
$$

僅僅擁有五個 agents，不等於每題都應該呼叫五個 agents。

---

## 4. Residual Doubt Vector

令問題在時間 $t$ 的狀態為：

$$
S_t.
$$

我們定義 residual doubt：

$$
D_t
=
(
D_F,
D_S,
D_B,
D_P,
D_R,
D_C,
\ldots
).
$$

可包含：

- $D_F$：Formal-Structural Doubt；
- $D_S$：Source-Fidelity Doubt；
- $D_B$：Framework-Bridge Doubt；
- $D_P$：Perspective / Pragmatic Doubt；
- $D_R$：Representation Doubt；
- $D_C$：Certificate / Closure Doubt。

其中：

$$
D_j\ge0.
$$

 $D_j=0$ 不必解讀為「哲學上完全無疑問」，而是：

> 在目前 theorem identity 與 proof obligation 下，此維度沒有剩餘的 load-bearing unresolved issue。

因此 residual doubt 是 operational state，而不是主觀信念的完整哲學模型。

---

## 5. Doubt Value Function

不同 doubt dimensions 的危險性不一定相同。

例如：

- 一個 minor notation ambiguity；
- 一個量詞 swap；
- 一個錯 source formulation；

其後果不同。

因此定義：

$$
V(D)
=
\sum_j
\lambda_jD_j.
$$

其中：

$$
\lambda_j\ge0
$$

是 risk weight。

更一般可以：

$$
V:
\mathbb R_{\ge0}^m
\rightarrow
\mathbb R_{\ge0}.
$$

而不要求線性。

例如若 source-fidelity doubt 與 formal doubt 同時高時風險超線性增加，可使用：

$$
V(D)
=
\sum_j\lambda_jD_j
+
\sum_{i<j}\gamma_{ij}D_iD_j.
$$

這反映：

$$
\boxed{
\text{doubt dimensions may interact}.
}
$$

---

## 6. Specialist Model

令 specialist set：

$$
\mathcal M
=
\{M_1,\ldots,M_k\}.
$$

每個 specialist 至少具有兩種估計。

### 6.1 Cost

$$
C(M_i\mid S_t)>0.
$$

成本可以是：

- tokens；
- wall-clock latency；
- API cost；
- tool calls；
- proof nodes；
- human supervision；
- energy；
- mixed operational cost。

初期可以使用 proxy cost，未來應改用 runtime telemetry。

### 6.2 Expected doubt transition

呼叫：

$$
M_i
$$

使：

$$
D_t
\rightarrow
D_{t+1}.
$$

定義：

$$
R_i(D_t)
=
\mathbb E[
D_t-D_{t+1}
\mid
M_i,S_t
].
$$

這是一個向量。

例如 MPF：

$$
R_{\mathrm{MPF}}
\approx
(
r_F,
r_S,
r_B,\ldots
)
$$

一般期望：

$$
r_F
$$

較高，

但不必假定：

$$
r_S=r_B=0.
$$

一個 specialist 可能順帶消除多種 doubt。

---

## 7. Value of Information

本文定義 specialist 的基本 VOI：

$$
\boxed{
\operatorname{VOI}(M_i\mid D_t)
=
\frac{
\mathbb E[
V(D_t)-V(D_{t+1})
\mid M_i
]
}{
C(M_i\mid S_t)
}.
}
$$

若使用線性 $V$：

$$
\operatorname{VOI}(M_i\mid D_t)
=
\frac{
\sum_j
\lambda_j
\mathbb E[\Delta D_j\mid M_i]
}{
C(M_i)
}.
$$

這表示：

> 每一單位認知成本，預期消掉多少 proof-relevant unresolved risk。

因此 routing：

$$
\boxed{
M_t^\ast
=
\arg\max_{M_i}
\operatorname{VOI}(M_i\mid D_t).
}
$$

---

## 8. VOI 不等於 Accuracy Predictor

這裡必須區分。

一般 inference allocation 可能估：

$$
P(\text{correct}\mid x,b).
$$

而本文主要估：

$$
\mathbb E[\Delta D\mid M_i,D].
$$

兩者可能相關，但不相同。

例如：

### Case A

MPF specialist 不直接提高 theorem proof probability，

但可以發現：

$$
\forall x\exists y
$$

被誤寫成：

$$
\exists y\forall x.
$$

它的價值是阻止 proof search 進入錯 target。

### Case B

Source Fidelity specialist 完全不會做代數證明，

但可以發現：

> AI 正在證 source 中較強的另一個 variant。

因此：

$$
\boxed{
\text{Value of a reasoning module}
\neq
\text{its standalone solving accuracy}.
}
$$

這是 specialist orchestration 的重要原則。

---

## 9. Freeze Controller：Should I Think More?

只會選 specialist 還不夠。

如果每輪都必須選一個 $M_i$：

$$
M_t^\ast
=
\arg\max_i\operatorname{VOI},
$$

系統仍可能永遠推理。

因此 action set 必須包含：

$$
\boxed{
\operatorname{Freeze}.
}
$$

我們提出兩種基本停止條件。

### 9.1 State-Based Freeze

若：

$$
V(D_t)
\le
\theta_D,
$$

則：

$$
\operatorname{Freeze}(S_t)=1.
$$

即 residual doubt 已低於可接受 threshold。

### 9.2 Marginal-Value Freeze

即使：

$$
V(D_t)>\theta_D,
$$

剩餘疑點也可能成本極高、影響極低。

如果：

$$
\max_i
\operatorname{VOI}(M_i\mid D_t)
\le
\theta_{\mathrm{VOI}},
$$

則可以 conditional freeze。

因此：

$$
\boxed{
\operatorname{Freeze}
\iff
\left[
V(D_t)\le\theta_D
\right]
\lor
\left[
\max_i\operatorname{VOI}_i
\le\theta_{\mathrm{VOI}}
\right],
}
$$

但第二種 freeze 必須記錄 remaining debt。

---

## 10. Hard Constraints：不是所有風險都可用低 VOI 忽略

純 VOI 最大化可能出現危險。

例如一個 quantifier corruption 的發現成本很高，但若漏掉，其 consequence 非常大。

因此定義 load-bearing set：

$$
\mathcal L(D_t).
$$

若：

$$
D_j\in\mathcal L
$$

且：

$$
D_j>\theta_j^{\mathrm{hard}},
$$

則禁止 freeze。

即：

$$
\boxed{
\operatorname{FreezeEligible}
=
\operatorname{SoftStop}
\land
\operatorname{HardClosure}.
}
$$

其中：

$$
\operatorname{HardClosure}
=
\bigwedge_{j\in\mathcal L}
[
D_j\le\theta_j^{\mathrm{hard}}
].
$$

這使系統不會因成本太高就跳過 theorem identity 的核心風險。

---

## 11. Risk-Aware VOI

更一般地，可以把 catastrophic target error 直接放入價值函數。

若 specialist $M_i$ 有機率發現 fatal corruption：

$$
p_i^{\mathrm{fatal}},
$$

漏掉此 corruption 的 expected loss：

$$
L_{\mathrm{fatal}},
$$

則：

$$
\operatorname{VOI}_{\mathrm{risk}}(M_i)
=
\frac{
\mathbb E[\Delta V]
+
p_i^{\mathrm{fatal}}L_{\mathrm{fatal}}
}{
C(M_i)
}.
$$

如此，「平常不太有用，但偶爾能抓到致命 target error」的 specialist 不會被簡單平均效益淘汰。

---

## 12. Adaptive Routing Algorithm

基本 runtime：

```text
INPUT: source problem / candidate target

1. SURFACE AUDIT
2. estimate residual doubt D_t
3. check hard closure
4. if freeze eligible:
       FREEZE
   else:
       estimate VOI(M_i | D_t)
       choose argmax VOI
       run specialist
       update state and D_t
       repeat
5. output frozen target
6. hand off to MCDM / Proof Router
```

形式化：

$$
S_0
\rightarrow
D_0
\rightarrow
M_0^\ast
\rightarrow
S_1
\rightarrow
D_1
\rightarrow
\cdots
\rightarrow
C^\ast_{\mathrm{freeze}}.
$$

---

## 13. Specialist Roles

本文至少區分四個 proof-search 前 specialist。

### 13.1 Surface Auditor

成本最低。

檢查：

- 明顯 domain omission；
- source 與 target 的 literal mismatch；
- 顯式 boundary；
- 已充分指定的 clean target。

若 Surface 已足夠：

$$
\boxed{
\text{do not call deeper specialists}.
}
$$

### 13.2 MPF Specialist

檢查：

- domain；
- quantifier；
- hidden/transitive quantifier；
- witness dependency；
- uniformity；
- asymptotic semantics；
- certificate tree。

### 13.3 Source-Fidelity Specialist

檢查：

- source formulation family；
- target-strength relation；
- definition provenance；
- representation equivalence；
- benchmark target identity。

### 13.4 Bridge Specialist

檢查：

- probability $\rightarrow$ decision；
- simulation $\rightarrow$ theorem；
- empirical observation $\rightarrow$ universal mathematical claim；
- one model/framework $\rightarrow$ another。

---

## 14. 為何不是 Always-Dual？

一個直覺安全策略是：

> 每題全部跑 Surface + MPF + NLU + Source + Bridge。

稱為：

$$
\operatorname{AlwaysDual}.
$$

其優勢是高 coverage。

但成本：

$$
C_{\mathrm{Always}}
=
\sum_{i=1}^{k}C(M_i)
$$

每題都支付。

若大量問題其實 Surface 就可 freeze：

$$
\boxed{
\text{Always-Dual creates systematic over-expansion}.
}
$$

所以真正目標不是：

$$
\max\text{analysis depth},
$$

而是：

$$
\boxed{
\min C_{\mathrm{audit}}
}
$$

subject to：

$$
\boxed{
P(\text{accept corrupted target})
\le\epsilon.
}
$$

---

## 15. 與 Adaptive Test-Time Compute 的關係

Uncertainty-aware allocation 已顯示，固定 sampling budget 平均分配到所有問題並非理想策略；依 uncertainty 配置 budget 可以改善有限計算資源下的 reasoning performance。

Constrained Policy Optimization 類方法則可寫成：

$$
\max_\pi
\mathbb E[\operatorname{Accuracy}]
$$

subject to：

$$
\mathbb E[C]\le B.
$$

本文可類比寫為：

$$
\min_\pi
\mathbb E[
\mathcal R_{\mathrm{target}}
+
\alpha C
]
$$

或：

$$
\max_\pi
\mathbb E[
\operatorname{TargetFidelity}
]
$$

subject to：

$$
\mathbb E[C_{\mathrm{audit}}]
\le B.
$$

差異是 action 不只是 budget level：

$$
a\neq\text{more samples}.
$$

而是：

$$
a\in\{
\operatorname{Freeze},
M_{\mathrm{MPF}},
M_{\mathrm{Source}},
M_{\mathrm{Bridge}},
\ldots
\}.
$$

因此 DDRA 可以理解為：

$$
\boxed{
\text{structured test-time compute allocation over cognitive roles}.
}
$$

---

## 16. 與 Selective Verification 的關係

近期 selective verification 工作指出，在 search 中平均驗證所有 intermediate hypotheses 會浪費 verifier calls；應優先驗證較具資訊價值的狀態。

本文的精神相似：

$$
\boxed{
\text{not every unresolved branch deserves verification}.
}
$$

但我們把 allocation point 放得更上游：

- selective verification：選擇哪個 reasoning state 要驗證；
- DDRA：選擇哪個 **problem-understanding / formalization specialist** 值得先投入。

兩者未來可以組合：

$$
\text{Problem-Space VOI}
\rightarrow
\text{Proof-State VOI}.
$$

---

## 17. EXP-0005：Freeze Controller 的結構代理結果

在先前開發集的結構模擬中，我們比較：

1. Surface-only；
2. Always-MPF；
3. Always-Dual；
4. Adaptive Controller。

以每個 audit module invocation 為一個 proxy cost unit。

結果顯示，在該人工建立 development set 上：

- Surface-only 成本最低，但漏掉大量深層 target corruption；
- Always-MPF 能抓 formal-structure corruption，但漏掉 source-fidelity 與 bridge 類；
- Always-Dual coverage 完整，但存在大量 unnecessary module calls；
- Adaptive Controller 在相同人工 coverage 下，用顯著更少 module invocations 完成 audit。

其中 Adaptive 相較 Always-Dual 的 module-call proxy 約降低：

$$
57.7\%.
$$

但：

$$
\boxed{
57.7\%
\text{ is not measured compute saving}.
}
$$

它只表示在人工 annotation 與 unit-cost assumption 下，啟動的分析模組較少。

---

## 18. EXP-0006：Holdout-Style Generalization

為避免控制器只記住 development cases，後續換用新的 Formal Conjectures 問題類型：

- Erdős 12；
- Erdős 26；
- Erdős 56；
- Open Quantum Problem 13；
- Open Quantum Problem 35；
- OEIS A6697。

這些案例新增：

- optimization-target replacement；
- representation-coverage failure；
- definition substitution / provenance gap。

固定 controller policy 後的 holdout-style 結構測試顯示，routing taxonomy 可以自然把：

- quantifier / uniformity $\rightarrow$ MPF；
- source identity / provenance $\rightarrow$ Source Fidelity；
- explicit boundary $\rightarrow$ Surface；
- representation coverage $\rightarrow$ MPF / Source Fidelity。

但也暴露 rule-based controller 的保守性：

> 一些 case 會同時啟動兩個 specialist，即使一個 specialist 已可能足夠。

這直接導向 VOI scheduler。

---

## 19. EXP-0007：VOI Specialist Scheduler

在下一步 simulation 中，為 specialist 指定 proxy costs：

$$
C_{\mathrm{Surface}}=1,
$$

$$
C_{\mathrm{MPF}}=2,
$$

$$
C_{\mathrm{Source}}=1.3,
$$

$$
C_{\mathrm{Bridge}}=1.2.
$$

並以人工 residual-doubt profiles 估計各 specialist 的 expected doubt reduction。

得到：

$$
\operatorname{VOI}(M_i)
=
\frac{\mathbb E[\Delta D]}{C_i}.
$$

在相同 holdout-style sample 上，VOI routing 能避免部分 rule-based 的保守 double-routing。

代理結果：

- Always-Dual：48 module calls；
- Rule-Based Adaptive：26；
- VOI Scheduler：24。

VOI scheduler 的 weighted proxy cost 相對 Always-Dual 約降低：

$$
51.8\%.
$$

相對 Rule-Based Adaptive 約降低：

$$
11.2\%.
$$

與利用 gold information 才能定義的 oracle lower bound 相比，proxy overhead 約：

$$
4.3\%.
$$

再次強調：

$$
\boxed{
\text{這些全部是 controller simulation，}
\text{不是實際 LLM / Lean 性能結果。}
}
$$

---

## 20. 一個重要結果：Routing 可以是序列，而不是一次分類

有些問題：

$$
D_F\gg0,
\qquad
D_S\gg0.
$$

此時可能：

$$
M_{\mathrm{Source}}
\rightarrow
M_{\mathrm{MPF}}
\rightarrow
\operatorname{Freeze}.
$$

例如 representation fidelity 問題：

1. Source specialist 先判定某 representation 是否可能忠實；
2. MPF 再檢查 symmetry / quantifier coverage 是否完整。

因此：

$$
\boxed{
\text{Routing}
\neq
\text{one-shot classification}.
}
$$

更像：

$$
D_t
\rightarrow
M_t
\rightarrow
D_{t+1}
\rightarrow
M_{t+1}.
$$

也就是 closed-loop reasoning control。

---

## 21. Problem-Level Scheduler 與 Proof-Level Scheduler

本文主要處理 proof search 前。

但完整數學 AI 可以有兩級 scheduler。

### Level A：Problem-Space Scheduler

決定：

- target 是否穩定；
- 該叫哪個 semantic/formal specialist；
- 是否 Freeze。

### Level B：Proof-Space Scheduler

Target freeze 後決定：

- Lean search；
- premise retrieval；
- counterexample；
- CAS；
- numerical experiment；
- natural-language lemma planning；
- ATP。

因此：

$$
\boxed{
\text{Problem-Space Governance}
\rightarrow
\text{Proof-Space Governance}.
}
$$

這避免 proof-level agent 被要求替上游 target corruption 買單。

---

## 22. 與 MCDM 的接口

MCDM 類 difficulty router 用來評估 frozen problem 的研究障礙向量。

因此順序應是：

$$
C^\ast_{\mathrm{freeze}}
\rightarrow
\mathrm{MCDM}
\rightarrow
\mathrm{ResearchRouter}.
$$

而不是：

$$
C_{\mathrm{raw}}
\rightarrow
\mathrm{MCDM}.
$$

因為如果 candidate target 本身不穩定：

$$
\mathrm{MCDM}(C_1)
\neq
\mathrm{MCDM}(C_2).
$$

甚至：

$$
\operatorname{Var}
[
\mathrm{MCDM}(C_i)
]
\gg0
$$

可以成為 target-instability diagnostic。

因此 DDRA 位於 MCDM 的上游。

---

## 23. 可學習的 Routing Policy

目前的 $C(M_i)$ 與 $R_i(D)$ 可以人工指定。

但真正 Runtime 應由 telemetry 學習：

$$
\widehat C_t(M_i)
$$

以及：

$$
\widehat R_t(M_i\mid X,D).
$$

其中 $X$ 包含：

- problem domain；
- theorem form；
- source type；
- model version；
- prompt version；
- tool availability。

於是：

$$
\widehat{\operatorname{VOI}}_t(M_i)
=
\frac{
\widehat{\mathbb E}[\Delta V]
}{
\widehat C_t(M_i)
}.
$$

這將是本系列下一篇 self-calibrating orchestration 的核心。

---

## 24. 評測指標

未來真實 benchmark 至少應保存：

### 24.1 Target Safety

$$
\text{Corruption Recall},
$$

$$
\text{False Freeze Rate},
$$

$$
\text{Clean Freeze Rate}.
$$

### 24.2 Routing Efficiency

$$
N_{\mathrm{module\ calls}},
$$

$$
\text{tokens},
$$

$$
\text{latency},
$$

$$
\text{tool calls}.
$$

### 24.3 Proof-Downstream Effect

$$
\text{proof branches},
$$

$$
\text{premise retrieval count},
$$

$$
\text{Lean elaboration failures},
$$

$$
\text{proof search nodes},
$$

$$
\text{proof success}.
$$

### 24.4 Regret

若存在 oracle 或 hindsight estimate：

$$
R_T
=
\sum_{t=1}^{T}
[
V(a_t^\ast)-V(a_t)
].
$$

### 24.5 Over-Expansion

$$
\operatorname{OER}
=
\frac{
\text{unnecessary specialist calls}
}{
\text{all specialist calls}
}.
$$

---

## 25. 三個核心 Hypotheses

### H1：Adaptive Freeze

相較 Always-Dual：

$$
\mathbb E[C_{\mathrm{audit}}]
$$

應下降，而 target-corruption miss rate 不顯著上升。

### H2：VOI Routing

相較固定 rule-based routing：

$$
\operatorname{VOI\ Scheduler}
$$

應降低 over-expansion。

### H3：Downstream Search

若上游 target audit 避免了 wrong target / wrong certificate route：

$$
\mathbb E[
C_{\mathrm{proof}}
\mid
\mathrm{DDRA}
]
<
\mathbb E[
C_{\mathrm{proof}}
\mid
\mathrm{DirectProof}
].
$$

但這是 empirical hypothesis，不是本文已證結果。

---

## 26. 失敗模式

### 26.1 Wrong Doubt Estimation

若：

$$
D_t
$$

估錯，

則 VOI 全部跟著錯。

### 26.2 Wrong Specialist Capability Model

若：

$$
R_i(D)
$$

估得太樂觀，會過度調用某 specialist。

### 26.3 Cheap-but-Useless Bias

若成本權重過重：

$$
\arg\max\operatorname{VOI}
$$

可能偏向便宜但只能消除小疑點的 specialist。

因此需 hard closure / fatal-risk term。

### 26.4 Endless Audit

若：

$$
\theta_D
$$

過低，

系統可能永遠不 Freeze。

### 26.5 Premature Freeze

若：

$$
\theta_D
$$

過高，

則重新產生 Paper 02 的 premature closure。

### 26.6 Correlated Specialists

兩個 specialists 可能高度冗餘：

$$
R_i\approx R_j.
$$

若 scheduler 不考慮 conditional marginal value，可能重複付費。

更完整應估：

$$
\operatorname{VOI}
(
M_j
\mid
D,
M_i\text{ already run}
).
$$

---

## 27. 從 Solver 到 Orchestrator

傳統 AI solver：

$$
\boxed{
\text{Problem}
\rightarrow
\text{Answer}.
}
$$

Agent system：

$$
\boxed{
\text{Problem}
\rightarrow
\text{Agents}
\rightarrow
\text{Answer}.
}
$$

本文提出的 adaptive orchestrator：

$$
\boxed{
\text{Problem}
\rightarrow
D_t
\rightarrow
\text{Choose Specialist}
\rightarrow
D_{t+1}
\rightarrow
\cdots
\rightarrow
\operatorname{Freeze}.
}
$$

因此上層 AI 真正需要回答：

$$
\boxed{
\text{Who should think?}
}
$$

$$
\boxed{
\text{What should they think about?}
}
$$

以及：

$$
\boxed{
\text{When should everyone stop thinking?}
}
$$

---

## 28. 認知資源治理

這使推理系統可以分層：

$$
\begin{array}{ll}
L_0 &: \text{Solver / Worker}\\
L_1 &: \text{Specialist Reasoner}\\
L_2 &: \text{Adaptive Orchestrator}\\
L_3 &: \text{Epistemic Governor}
\end{array}
$$

 $L_0$ 解局部問題。

 $L_1$ 專門處理某種認知功能。

 $L_2$ 決定 specialist allocation。

 $L_3$ 管理：

- target 是否值得 Freeze；
- 哪些 unresolved risks 不可忽略；
- 推理預算怎麼分；
- 哪些認知活動目前沒有邊際價值。

因此：

$$
\boxed{
\text{Tool Routing}
\subset
\text{Reasoning Routing}
\subset
\text{Problem-Space Governance}.
}
$$

本文主要建立中間層：

$$
\boxed{
\text{Reasoning Routing}.
}
$$

---

## 29. 討論

Adaptive test-time compute 已經提出一個重要觀念：

> inference compute 應是可分配資源，而不是固定常數。

本文再推一步：

> **reasoning type 本身也應是可分配資源。**

對數學 AI 而言，額外的一千 tokens 可以拿來：

- 繼續同一路推 proof；
- 回頭檢查量詞；
- 找 source；
- 檢查 provenance；
- 反例搜尋；
- 形式驗證。

這些 action 的 information gain 完全不同。

因此真正的 inference-time intelligence 不只是：

$$
\boxed{
\text{think longer}.
}
$$

更是：

$$
\boxed{
\text{think in the right place}.
}
$$

而更成熟時，還包括：

$$
\boxed{
\text{know when not to think further}.
}
$$

---

## 30. 結論

本文提出 Doubt-Driven Reasoning Allocation，將數學 AI 的 proof-search 前資源治理建模為 residual doubt 上的 sequential decision problem。

核心狀態：

$$
D_t.
$$

核心 action：

$$
a_t
\in
\{
\operatorname{Freeze},
M_1,\ldots,M_k
\}.
$$

核心選擇準則：

$$
\boxed{
\operatorname{VOI}(M_i\mid D_t)
=
\frac{
\mathbb E[
V(D_t)-V(D_{t+1})
]
}{
C(M_i)
}.
}
$$

核心停止原則：

$$
\boxed{
\text{Freeze when residual risk is sufficiently closed,}
}
$$

或：

$$
\boxed{
\text{when no remaining reasoning action has adequate marginal value,}
}
$$

但 load-bearing target risks 必須滿足 hard closure。

因此：

$$
\boxed{
\text{Should I think more?}
}
$$

由 Freeze Controller 回答，

而：

$$
\boxed{
\text{What should I think about next?}
}
$$

由 VOI Scheduler 回答。

這使數學 AI 從固定 pipeline：

$$
\text{Formalize}
\rightarrow
\text{Prove}
$$

轉向：

$$
\boxed{
\text{Observe}
\rightarrow
\text{Estimate Doubt}
\rightarrow
\text{Allocate Reasoning}
\rightarrow
\text{Update}
\rightarrow
\text{Freeze}
\rightarrow
\text{Prove}.
}
$$

本文的結構代理實驗只證明該控制流程可以被工程化與量測，而不證明它已在真實模型上降低 inference 或 formal-proof 成本。下一篇將進一步研究如何從 runtime telemetry 自動學習 specialist cost、能力與 routing policy，使 orchestrator 從固定規則提升為 self-calibrating meta-orchestrator。

---

## 參考文獻

1. Nguyen, M., Gupta, S., Le, H. *Uncertainty-Aware Budget Allocation for Adaptive Test-Time Reasoning.* arXiv:2605.26849, 2026.
2. Zhai, Z., Li, B., Xiao, B., Li, M., Wang, X. *Adaptive Test-Time Compute Allocation for Reasoning LLMs via Constrained Policy Optimization.* arXiv:2604.14853, 2026.
3. Qu, S. *Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure.* arXiv:2602.03975, 2026.
4. Smirnov, V., Nguyen, C., Senichev, S., et al. *ThinkBooster: A Unified Framework for Seamless Test-Time Scaling of LLM Reasoning.* arXiv:2606.06915, 2026.
5. Zhang, Y., Sun, Y., Suzuki, T., Lee, J. D., Liu, F. *LeanMarathon: Toward Reliable AI Co-Mathematicians through Long-Horizon Lean Autoformalization.* arXiv:2606.05400, 2026.
6. Wang, R., Pan, R., Li, Y., et al. *MA-LoT: Multi-Agent Lean-based Long Chain-of-Thought Reasoning Enhances Formal Theorem Proving.* arXiv:2503.03205, 2025.
7. Chen, J., Chen, W., Du, J., et al. *Seed-Prover 1.5: Mastering Undergraduate-Level Theorem Proving via Learning from Experience.* arXiv:2512.17260, 2025.
8. Firsching, M., Lezeau, P., Mercuri, S., et al. *Formal Conjectures: An Open and Evolving Benchmark for Verified Discovery in Mathematics.* arXiv:2605.13171, 2026.

---

## 研究狀態聲明

本文提出的 Doubt-Driven Reasoning Allocation、Residual Doubt Vector、Freeze Controller、Specialist VOI、Hard Closure 與相關 routing 架構，屬於本文提出的研究框架。

本文所述 EXP-0005～EXP-0007 數值來自人工 annotation、結構代理成本與 controller simulation；它們不應被引用為實際 LLM token savings、wall-clock speedup、Lean proof-node reduction 或通用性能提升。這些 empirical claims 必須由獨立 Agent、固定模型版本、真實 runtime telemetry 與 formal prover logs 重新驗證。
