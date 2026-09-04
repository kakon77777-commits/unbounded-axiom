# Paper 05｜Externalized Mixture of Cognitive Experts：為什麼 Expert 一定要住在同一個模型裡？

**English Title:** *Externalized Mixture of Cognitive Experts: Why Must an Expert Live Inside One Model?*  
**系列：**《可展開認知核心：從 MoE、認知密度到 Mother AI 的模型架構命題》  
**作者：** Neo.K × Aletheia  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-08-28  
**文件性質：** 公開命題論文／External Cognitive Experts、模型路由與跨邊界智能架構研究

---

## 摘要

本文提出 **Externalized Mixture of Cognitive Experts（EMCE，外部化認知專家混合）** 命題。前一篇已將 Mixture-of-Experts 視為 Conditional Intelligence：模型可以擁有遠大於單次推理所激活的總容量，但每個 token 只使用其中一部分計算。然而，現有 MoE expert 仍通常存在於同一模型的共同 hidden space、相容參數結構、低延遲 token-level routing 與同一 inference runtime 中。即使 expert weights 被 offload 到 CPU 或較慢記憶體，它們仍然是同一模型的一部分。因此：

$$
\boxed{
\text{Expert Offloading}
\neq
\text{Cognitive Expert Externalization}.
}
$$

本文提出更進一步的問題：

> **如果某些能力已能被條件激活，為什麼它們必須在物理上、參數上與推理 runtime 上永久存在於同一個模型內？**

本文不主張可以直接把 Transformer MoE 的 token-level FFN expert 搬成遠端 API。內部 expert 的接口通常是：

$$
h_l\in\mathbb R^d
$$

而外部模型、Agent、工具或檢索系統的接口通常是文字、結構化狀態、多模態資料或明確任務契約。二者之間存在表示、粒度、延遲、狀態、驗證與權限差異。因此本文提出 **Granularity Lift（粒度提升）**：

$$
\boxed{
\text{Fine-Grained Neural Expert}
\rightarrow
\text{Cognitive Operation}
\rightarrow
\text{External Executor}.
}
$$

也就是：外部化的最小單位不應直接是某個 neuron、FFN expert 或 layer path，而應是可被較高層系統描述、封裝、路由、驗證、替換與回收的 **Cognitive Operation Contract（認知操作契約）**。

本文將 External Cognitive Expert 形式化為：

$$
\boxed{
X_i
=
(
R_i,
I_i,
O_i,
C_i,
S_i,
A_i,
V_i,
H_i
)
}
$$

其中：

- $R_i$：Role / Capability；
- $I_i$：Input Contract；
- $O_i$：Output Contract；
- $C_i$：Context Requirement；
- $S_i$：State Semantics；
- $A_i$：Authority Boundary；
- $V_i$：Verification Contract；
- $H_i$：Health / Cost / History。

因此 External Cognitive Expert 可以由：

$$
\boxed{
\{
\text{External LLM},
\text{Sub-AI},
\text{Specialist Model},
\text{Retrieval System},
\text{Symbolic Solver},
\text{Compiler},
\text{Simulator},
\text{Deterministic Program}
\}
}
$$

實現。

本文提出三種 MoE 尺度：

$$
\boxed{
\text{Micro-MoE}
}
$$

表示 token / layer 級神經 experts；

$$
\boxed{
\text{Meso-MoE}
}
$$

表示 adapters、modules、independently trained sub-networks 與可插拔專家；

$$
\boxed{
\text{Macro-MoE}
}
$$

表示 task / cognitive-operation 級外部模型、Agent、工具與資料系統。

本文強調，Macro-MoE 不是 Internal MoE 的簡單放大，而是一個新的系統架構。真正需要解決的是：

$$
\boxed{
\text{Representation Translation}
+
\text{Context Compilation}
+
\text{Routing}
+
\text{State Transfer}
+
\text{Verification}
+
\text{Authority}
+
\text{Reconvergence}.
}
$$

本文參照 Branch-Train-MiX、Branch-Train-Stitch、BAR、LoRA-Mixer、MoIRA、RouteLLM、Mixture-of-Agents 以及 MoE expert offloading 等研究，指出現有技術已逐步拆開「專家一定要共同訓練、共同權重融合、共同執行」這些假設；但尚未證明一個通用 Mother AI 可以把任意神經能力乾淨 externalize。

本文的核心主張是：

$$
\boxed{
\text{Externalization 的對象不是參數本身，而是可治理的能力接口。}
}
$$

如果未來可以穩定建立：

$$
\text{Resident Core}
+
\text{Internal Conditional Experts}
+
\text{External Cognitive Experts},
$$

那麼模型總參數不再是系統可用能力的唯一上限；系統可以把低頻、專門、昂貴、快速變化或可獨立驗證的能力移出常駐模型，同時保留高頻、低延遲、高中心性與高治理價值的核心能力。

**關鍵詞：** Externalized Mixture of Cognitive Experts、External Expert、Macro-MoE、Granularity Lift、Model Routing、Mixture-of-Agents、Mother AI、Cognitive Command Tower、Modular Intelligence、Capability Interface

---

# 0. 研究定位

Paper 03 提出：

$$
\mathcal C_R
$$

Resident Capability。

Paper 04 提出：

$$
\mathcal C_Q
$$

Conditionally Activated Capability。

Paper 05 現在研究：

$$
\boxed{
\mathcal C_X
}
$$

Externally Expanded Capability。

整個系列因此形成：

$$
\boxed{
\mathcal C
=
\mathcal C_R
\cup
\mathcal C_Q
\cup
\mathcal C_X.
}
$$

---

# 1. Expert 為什麼一定要和模型住在一起？

Internal MoE 的典型結構：

$$
x
\rightarrow
r(x)
\rightarrow
E_i
\rightarrow
y.
$$

其中 expert：

$$
E_i
$$

通常共享同一 hidden space、模型 architecture、inference graph 與 token-level router。

這是一個極有效率的神經計算架構。

但它不是邏輯必然。

---

# 2. Physical Co-Residence 不是 Cognitive Necessity

現有 MoE 將 experts 放在同一 checkpoint 或相容權重系統中，主要原因包括 latency、tensor compatibility、joint optimization、routing simplicity 與 serving engineering。

這些都是強工程理由。

但不能推出：

$$
\boxed{
\text{expert 必須永遠和 core model 物理共居}.
}
$$

---

# 3. Expert Offloading 已先拆掉第一層假設

MoE expert offloading 系統可以把 expert weights 放到 CPU / host memory，並在 router 決定：

$$
E_i
$$

後再載入 GPU。

因此：

$$
\boxed{
\text{Expert Residency}
\neq
\text{Expert Activation Device}.
}
$$

但這仍未跨出模型本身。

---

# 4. Offloading 還沒有真正 Externalize

即使：

$$
E_i
$$

平常存在 CPU，它仍屬於同一 model checkpoint、使用同一 hidden representation、由同一 token router 選擇，並返回同一 layer。

因此：

$$
\boxed{
\text{Memory Offloading}
\neq
\text{Cognitive Externalization}.
}
$$

---

# 5. 真正 Externalization 必須跨越模型邊界

真正 externalized expert：

$$
X_i
$$

可以是另一模型、另一進程、另一台機器、另一 provider、deterministic tool、retrieval service，或具有局部 state 的 Sub-AI。

因此存在：

$$
\boxed{
\text{Model Boundary Crossing}.
}
$$

---

# 6. 模型邊界不是智能邊界

傳統直覺：

$$
\boxed{
\text{One Intelligence}
=
\text{One Model}.
}
$$

本文提出：

$$
\boxed{
\text{One Cognitive System}
\neq
\text{One Weight File}.
}
$$

如果多個計算單元透過 shared objective、state、capability routing、verification 與 reconvergence 形成一致工作閉環，system-level intelligence 可以跨模型邊界存在。

---

# 7. Internal Expert Interface 與 External Expert Interface 不同

Internal expert 接收：

$$
h_l\in\mathbb R^d.
$$

External expert 通常接收：

$$
q,
C,
S,
T.
$$

因此：

$$
\boxed{
\text{Internal Expert Interface}
\neq
\text{External Expert Interface}.
}
$$

---

# 8. Granularity Lift

本文提出：

$$
\boxed{
\mathsf{Lift}
:
c_{\mathrm{micro}}
\rightarrow
c_{\mathrm{operation}}.
}
$$

其中 $c_{\mathrm{micro}}$ 是細粒度神經操作，而 $c_{\mathrm{operation}}$ 是可描述的認知操作，例如 prove、translate、search、compile、simulate、classify、verify 或 generate candidate patch。

---

# 9. 為什麼需要 Granularity Lift？

如果每一個 token：

$$
t
$$

都要 network round trip，則：

$$
C_{\mathrm{latency}}\rightarrow\infty
$$

在實際系統中。

因此外部 routing granularity 必須從：

$$
\boxed{
\text{token-level}
}
$$

提高到：

$$
\boxed{
\text{operation / subtask-level}.
}
$$

---

# 10. Micro-MoE

定義：

$$
\boxed{
\text{Micro-MoE}
}
$$

為 token-level、layer-level、hidden-state interface、低延遲、共同整合的 neural experts。

---

# 11. Meso-MoE

定義：

$$
\boxed{
\text{Meso-MoE}
}
$$

包括 LoRA experts、adapters、separately trained expert modules、stitchable sub-networks 與 modular checkpoints。

它仍可能存在一個模型 runtime 內，但 expert training 與 storage 已開始解耦。

---

# 12. Macro-MoE

定義：

$$
\boxed{
\text{Macro-MoE}
}
$$

為 task-level / cognitive-operation-level routing，由 independent models、Agents、tools、retrieval、solvers 與 simulators 組成。

它的 expert interface 是：

$$
\boxed{
\text{contract}
}
$$

而不是：

$$
h_l.
$$

---

# 13. 三層 MoE

本文提出跨尺度分類：

$$
\boxed{
\text{MoE}
=
\{
\text{Micro},
\text{Meso},
\text{Macro}
\}.
}
$$

這是本文分析語言，不宣稱是現有產業標準。

---

# 14. Branch-Train-MiX 的意義

Branch-Train-MiX 從 seed model：

$$
M_0
$$

分支訓練：

$$
M_1,M_2,\ldots,M_n
$$

domain experts，再把 feed-forward parameters 組合進 MoE。

這支持：

$$
\boxed{
\text{experts can be trained separately before composition}.
}
$$

---

# 15. Branch-Train-Stitch 的意義

BTS 保留 frozen experts，再用 lightweight stitch layers 進行 representation integration。

這支持：

$$
\boxed{
\text{Expert Preservation}
+
\text{Learned Interface}.
}
$$

---

# 16. BAR 的意義

2026 的 Branch-Adapt-Route 將 domain experts 分開 mid-training、supervised finetuning 與 reinforcement learning，再由 lightweight router 組合。

這支持：

$$
\boxed{
\text{capability update can become expert-local}.
}
$$

---

# 17. Modular Training 的經濟動機

如果：

$$
E_i
$$

可以單獨更新，則某個 domain 更新不必重新處理整個 monolithic model。

因此：

$$
\boxed{
\text{Update Locality}
}
$$

本身就是 modular expert architecture 的重要價值。

---

# 18. LoRA-Mixer 的意義

LoRA-Mixer 研究 frozen / modular LoRA experts 加 learned routing，展示 experts 可以逐步具有 plug-and-play、reusable 與 task-specific 特性。

這使：

$$
\boxed{
\text{Meso-MoE}
}
$$

開始變得實際。

---

# 19. RouteLLM 提供 Macro Routing 的另一條線

RouteLLM 做：

$$
q
\rightarrow
r(q)
\rightarrow
\begin{cases}
M_{\mathrm{weak}}\\
M_{\mathrm{strong}}
\end{cases}.
$$

這是：

$$
\boxed{
\text{model-level conditional execution}.
}
$$

它把 model 變成 selectable compute resource。

---

# 20. Strong / Weak Router 還太粗

若只有：

$$
\{
M_{\mathrm{weak}},
M_{\mathrm{strong}}
\},
$$

主要回答的是：

> 問題是否值得升級？

Mother AI 則需要回答：

- 需要什麼能力；
- 誰適合；
- 要什麼 context；
- 怎麼驗證；
- 有什麼 authority；
- 失敗後怎麼 fallback。

因此：

$$
\boxed{
\text{Capability Routing}
>
\text{Difficulty Routing}.
}
$$

---

# 21. Marginal Gain Routing

對 external expert：

$$
X_i
$$

定義：

$$
\boxed{
\Delta Q_i
=
Q(S\oplus X_i)-Q(S).
}
$$

再計算：

$$
\boxed{
U_i
=
\frac{
\Delta Q_i
}{
C_i^{\mathrm{total}}
}.
}
$$

其中總成本包括 inference、network、context、coordination、verification 與 human attention。

---

# 22. Mixture-of-Agents 提供組合智能證據

Mixture-of-Agents 以 layered agents 組合不同 LLM outputs，顯示在某些 benchmark 上：

$$
\boxed{
Q_{\mathrm{system}}
>
\max_i
Q(A_i)
}
$$

可以成立。

但：

$$
\boxed{
\text{MoA}
\neq
\text{MoE}.
}
$$

因為它是 message-level、coarse-grained 且 coordination-heavy。

---

# 23. MoIRA 的意義

MoIRA 研究 decoupled experts + external text router。

其架構信號是：

$$
\boxed{
\text{expert 不必永久被 monolithic router 與共同 training graph 鎖死}.
}
$$

這與 Macro-MoE 更接近。

---

# 24. External Cognitive Expert 的正式定義

本文定義：

$$
\boxed{
X_i
=
(
R_i,
I_i,
O_i,
C_i,
S_i,
A_i,
V_i,
H_i
).
}
$$

---

# 25. Role / Capability

$$
R_i
$$

回答：

> 這個 expert 提供什麼能力？

例如 code generation、theorem proving、web research、translation、image analysis、simulation。

---

# 26. Input Contract

$$
I_i
$$

定義 required fields、format、assumptions、maximum context 與 data classification。

避免：

$$
\boxed{
\text{prompt soup}.
}
$$

---

# 27. Output Contract

$$
O_i
$$

定義 output schema、candidate type、confidence、citations、artifacts 與 failure state。

因此：

$$
\boxed{
\text{response text}
\neq
\text{contracted result}.
}
$$

---

# 28. Context Requirement

$$
C_i
$$

定義 expert 需要 full source、summary、causal graph、API docs、prior state 或 examples。

---

# 29. State Semantics

$$
S_i
$$

區分 stateless、session-local、task-local 與 persistent。

不是每個 external expert 都需要記憶。

---

# 30. Authority Boundary

$$
A_i
$$

定義 read、generate candidate、execute、write、commit 或 publish。

因此：

$$
\boxed{
\text{Expert Capability}
\neq
\text{Expert Authority}.
}
$$

---

# 31. Verification Contract

$$
V_i
$$

定義 compiler、tests、schema、source grounding、proof checking 或 human review。

沒有：

$$
V_i
$$

就會增加：

$$
\boxed{
\text{epistemic risk}.
}
$$

---

# 32. Health / Cost / History

$$
H_i
$$

保存 latency、price、success、failure modes、last validated、version、provider 與 availability。

因此 expert 是：

$$
\boxed{
\text{measured capability object}.
}
$$

---

# 33. External Cognitive Expert 不一定是 AI

如果任務是：

$$
\text{sort 1 million rows},
$$

最好 expert 可能是：

$$
\boxed{
\text{program}.
}
$$

如果任務是 compile TypeScript，最好 verifier 可能是 compiler。

因此：

$$
\boxed{
\text{Cognitive Expert}
\neq
\text{LLM only}.
}
$$

---

# 34. Deterministic Experts

本文允許：

$$
X_i
=
\text{deterministic executor}.
$$

例如 parser、compiler、database、symbolic solver、optimizer。

---

# 35. Retrieval / Search 也是 Expert

Retrieval expert：

$$
X_R
$$

負責：

$$
\boxed{
q
\rightarrow
\text{relevant evidence set}.
}
$$

Web search expert 則提供：

$$
\boxed{
\text{external world observation}.
}
$$

它們不是 reasoning sovereignty。

---

# 36. Specialist Model 是 External Expert

例如：

$$
X_{\mathrm{vision}}
$$

或：

$$
X_{\mathrm{math}}
$$

可以由不同模型提供。

Mother AI 不需要所有 modalities 與高解析度專門能力都常駐。

---

# 37. Sub-AI 是 Stateful External Expert

Sub-AI：

$$
A_i(t)
$$

可以有 local memory、plan、tool loop 與 task state。

因此：

$$
\boxed{
\text{Sub-AI}
=
\text{stateful macro expert candidate}.
}
$$

---

# 38. Externalization 不等於 Delegation

Delegation：

$$
M\rightarrow A_i
$$

只是一次行為。

Externalization 更強：

$$
\boxed{
\text{某能力在架構上被視為非核心、可替換、按需載入}.
}
$$

---

# 39. Capability Slot

Mother AI 不應保存：

$$
\boxed{
\text{Model X = worker}.
}
$$

而應保存：

$$
\boxed{
\text{Role Slot}.
}
$$

例如：

$$
R_{\mathrm{bounded-code}}.
$$

然後：

$$
\operatorname{Bind}(R,X_i).
$$

---

# 40. Role Persistence > Worker Persistence

$$
\boxed{
R
\neq
X_i.
}
$$

一個 role 可以：

$$
X_1
\rightarrow
X_2
$$

替換。

因此可以形成：

$$
\boxed{
\text{functional continuity without model identity continuity}.
}
$$

---

# 41. External Expert Registry

定義：

$$
\boxed{
\mathcal X_t
=
\{
X_1,\ldots,X_n
\}.
}
$$

每個 expert 的：

$$
H_i(t)
$$

持續更新。

---

# 42. Capability-Aware Routing

定義 eligible set：

$$
\boxed{
\mathcal E(T)
=
\{
X_i:
\operatorname{Cap}(X_i)\supseteq R_T
\}.
}
$$

再要求：

$$
\operatorname{PolicyCompatible}(X_i)=1.
$$

最後：

$$
X^\ast
=
\arg\max_{X_i\in\mathcal E(T)}
U(X_i,T).
$$

---

# 43. Router 不一定是 LLM

Router 可以是 rule、classifier、small model、Mother AI 或 hybrid planner。

因此：

$$
\boxed{
\text{Router}
\neq
\text{necessarily LLM}.
}
$$

---

# 44. Externalization Tax

定義：

$$
\boxed{
C_X
=
C_{\mathrm{route}}
+
C_{\mathrm{context}}
+
C_{\mathrm{network}}
+
C_{\mathrm{execution}}
+
C_{\mathrm{verify}}
+
C_{\mathrm{merge}}
+
C_{\mathrm{retry}}.
}
$$

外部 expert 只有在能力增益大於完整外置成本時才有價值。

---

# 45. Network Tax

Internal MoE 是 local low-latency communication。

Macro-MoE 通常跨 process / network。

因此低粒度 externalization 可能完全不划算。

---

# 46. Context Compilation

Mother AI 必須建立：

$$
\boxed{
C_T
=
\operatorname{CompileContext}(S,T,R).
}
$$

Context compilation 需要 select、order、compress、mark evidence、preserve constraints 與 provenance。

因此：

$$
\boxed{
\text{Retrieval}
\neq
\text{Context Compilation}.
}
$$

---

# 47. Context Translation

不同 expert 可能需要不同表示：

$$
C_i
\neq
C_j.
$$

因此：

$$
\boxed{
\operatorname{Project}_i(S)
}
$$

生成：

$$
C_i.
$$

這是一種 representation translation。

---

# 48. State Transfer

若 expert 是 stateful，Mother AI 必須決定：

$$
\boxed{
\text{what state to transfer}
}
$$

以及：

$$
\boxed{
\text{what state not to transfer}.
}
$$

避免 privacy leak、irrelevant context 與 identity confusion。

---

# 49. Return Contract

External expert 不應只回 arbitrary prose。

更理想：

$$
\boxed{
O_i
=
(
candidate,
evidence,
confidence,
unknowns,
artifacts
).
}
$$

---

# 50. Candidate-Only Principle

對高風險工作：

$$
\boxed{
\text{External Expert}
\rightarrow
\text{Candidate}
}
$$

而不是：

$$
\boxed{
\text{External Expert}
\rightarrow
\text{Accepted State}.
}
$$

---

# 51. Verification 使 Externalization 可行

真正的架構目標是：

$$
\boxed{
P(
\text{wrong candidate accepted}
)
\rightarrow0,
}
$$

而不是要求：

$$
\boxed{
P(
\text{expert never wrong}
)
\rightarrow1.
}
$$

---

# 52. Cheap Generation + Strong Verification

如果：

$$
X_{\mathrm{cheap}}
$$

品質稍低，但：

$$
V
$$

便宜可靠，

則：

$$
\boxed{
\text{cheap generation + strong verification}
}
$$

可能優於：

$$
\boxed{
\text{expensive generation + weak verification}.
}
$$

---

# 53. External Expert 可以 Disposable

External expert 不一定需要 persistent identity。

它可以：

$$
\text{spawn}
\rightarrow
\text{work}
\rightarrow
\text{retire}.
$$

真正持久的是：

$$
\boxed{
\text{Role}
+
\text{Contract}
+
\text{Evidence}.
}
$$

---

# 54. Persistent Child AI 仍有位置

如果某工作需要 long-term local memory、relationship continuity、specialized history 或 autonomous long loop，External Expert 可以升級成 Persistent Child Resident。

但這不是所有 expert 的必要條件。

---

# 55. Macro-MoE Routing Granularity

Internal：

$$
g_{\mathrm{micro}}
=
\text{token}.
$$

Macro：

$$
g_{\mathrm{macro}}
\in
\{
\text{operation},
\text{subtask},
\text{task},
\text{episode}
\}.
$$

---

# 56. Optimal Granularity

太細：

$$
C_X\uparrow.
$$

太粗：

$$
\text{specialization benefit}\downarrow.
$$

因此存在：

$$
\boxed{
g^\ast
=
\arg\max_g
\eta_E(g).
}
$$

---

# 57. Interaction Frequency

如果 expert 每秒需要大量交互，Macro-MoE 不可行。

如果每個 task 只需少數次調用，就可能可行。

因此：

$$
\boxed{
F_{\mathrm{interaction}}
}
$$

是 externalization 核心變數。

---

# 58. Representation Boundary

Internal expert：

$$
h_l
\rightarrow E_i(h_l).
$$

External expert：

$$
C_T
\rightarrow X_i(C_T).
$$

因此需要：

$$
\boxed{
\mathsf{Lift}
}
$$

與：

$$
\boxed{
\mathsf{Project}.
}
$$

---

# 59. Functional Compression

Granularity Lift 不要求保留 hidden state 的全部資訊，而要保留 task-relevant functional state。

因此可寫：

$$
C_T
=
\operatorname{CompressFunctionally}(h_{1:L},T).
$$

本文只提出形式，不公開實作。

---

# 60. Interface Fidelity

定義：

$$
\boxed{
F_I
=
\frac{
Q(
X\mid C_T
)
}{
Q(
X\mid C_T^\ast
)
}.
}
$$

如果：

$$
F_I\ll1,
$$

表示 context bridge 不足。

---

# 61. External Expert 也是 Epistemic Instrument

每次 delegation 都可以產生：

$$
\boxed{
\text{Capability Evidence}.
}
$$

因此：

$$
\boxed{
\text{External Expert}
=
\text{Worker}
+
\text{Probe}.
}
$$

這會在後續 Capability Boundary Tomography 正式展開。

---

# 62. External Expert Market

若：

$$
|\mathcal X|\uparrow,
$$

Mother AI 面對：

$$
\boxed{
\text{AI Labor Market}.
}
$$

它必須知道新模型、價格、能力、latency、reliability 與 version。

---

# 63. Discovery 與 Execution 分離

一個模型可以由 discovery source 發現，但由另一 execution provider 執行。

因此：

$$
\boxed{
\text{Discovery Provider}
\neq
\text{Execution Provider}.
}
$$

---

# 64. Observation 不等於 Qualification

市場熱門度、benchmark、vendor model card 只能作為：

$$
\boxed{
\text{discovery signal}.
}
$$

真正 production routing 需要：

$$
\boxed{
\text{Discover}
\rightarrow
\text{Probe}
\rightarrow
\text{Verify}
\rightarrow
\text{Qualify}.
}
$$

---

# 65. External Expert Passport

保存：

$$
\boxed{
P_i
=
(
identity,
capability,
cost,
evidence,
failures,
version,
roles
).
}
$$

這使 expert 成為可治理資源。

---

# 66. Multi-Provider Redundancy

同一 role：

$$
R
$$

可綁：

$$
X_1,X_2,X_3.
$$

當：

$$
X_1\rightarrow\bot,
$$

切到：

$$
X_2.
$$

因此：

$$
\boxed{
\text{Role Continuity}
>
\text{Provider Continuity}.
}
$$

---

# 67. Heterogeneous Experts

External expert pool 可以同時包含：

$$
\boxed{
\text{AI}
+
\text{Program}
+
\text{Retrieval}
+
\text{Human}.
}
$$

因此真正架構是：

$$
\boxed{
\text{Heterogeneous Cognitive-Computational Mixture}.
}
$$

---

# 68. Expert Authority 不由能力決定

即使：

$$
Q(X_i)\uparrow,
$$

也不能推出：

$$
A_i\uparrow.
$$

因此：

$$
\boxed{
\text{Competence}
\neq
\text{Authority}.
}
$$

---

# 69. Coordinator / Reviewer 也可以是 Expert

Coordinator 提供 decomposition / synchronization。

Reviewer 提供 critique / comparison。

但二者都不自動取得 Mother-level acceptance authority。

---

# 70. Verification Topology

Macro-MoE 不只有 execution graph：

$$
G_E.
$$

還需要：

$$
\boxed{
G_V
}
$$

verification graph。

因此：

$$
\boxed{
G_E
\neq
G_V.
}
$$

---

# 71. Reconvergence

多個 external experts：

$$
X_1,\ldots,X_n
$$

產生：

$$
o_1,\ldots,o_n.
$$

系統需要：

$$
\boxed{
\mathsf{Reconverge}
(
o_1,\ldots,o_n
).
}
$$

---

# 72. Reconvergence 不是 Majority Vote

如果：

$$
o_1,o_2,o_3
$$

互相矛盾，不應只投票。

應考慮 evidence、expertise、verifier、source、version 與 confidence。

---

# 73. Evidence-Weighted Reconvergence

可概念化：

$$
\boxed{
o^\ast
=
\operatorname{ArgMax}_o
\sum_i
w_i
E_i(o),
}
$$

其中 $w_i$ 來自 task-specific qualification，而非模型名氣。

---

# 74. External Expert 失敗語義

至少區分：

$$
\boxed{
\text{SUCCESS},
\text{UNKNOWN},
\text{UNSUPPORTED},
\text{FAILED},
\text{TIMEOUT}.
}
$$

不能所有失敗都變成 prose。

---

# 75. Graceful Failure

如果：

$$
X_i\rightarrow\bot,
$$

系統應 fallback，而不是 global cognition collapse。

---

# 76. Security Boundary

外部模型可能看到：

$$
C_T.
$$

因此 context projection 必須考慮 privacy、secrets、licensing、jurisdiction 與 provider policy。

---

# 77. Context Minimization

應只提供：

$$
\boxed{
C_T^{\min}
}
$$

足夠完成任務的最小 context，避免 full memory exfiltration。

---

# 78. External Expert 不應直接改寫 Core

除非：

$$
\boxed{
\text{proposal}
\rightarrow
\text{verification}
\rightarrow
\text{commit}.
}
$$

因此：

$$
X_i
\not\rightarrow
K_R
$$

直接寫入。

---

# 79. Externalize / Internalize 可以雙向

能力：

$$
c
$$

可以：

$$
\boxed{
R
\rightarrow
Q
\rightarrow
X
}
$$

也可以：

$$
\boxed{
X
\rightarrow
Q
\rightarrow
R.
}
$$

這是一個 dynamic placement lifecycle。

---

# 80. Internalization Criteria

若某 external capability usage frequency、latency sensitivity、cost 或 reliability criticality 持續上升，則：

$$
N_R(c)\uparrow.
$$

可能值得 internalize。

---

# 81. Externalization Criteria

若某 resident capability usage frequency 下降、update rate 上升、specialist quality 上升、verification 更容易且 interface granularity 較粗，則：

$$
P_X(c)\uparrow.
$$

---

# 82. Mother AI 是 Router of Routers

如果 internal MoE 有 router、model pool 有 router、tool pool 有 router、verification 有 router，Mother AI 變成：

$$
\boxed{
\text{meta-router}.
}
$$

但 meta-routing 不只是 dispatch。

---

# 83. Meta-Routing 還要選 Topology

Mother AI 可能選：

$$
\boxed{
\tau
\in
\{
\text{direct},
\text{fanout},
\text{pipeline},
\text{supervisor},
\text{debate},
\text{map-reduce}
\}.
}
$$

因此：

$$
\boxed{
(\tau^\ast,\mathbf X^\ast,\mathbf V^\ast)
=
\arg\max
U(
\tau,\mathbf X,\mathbf V
\mid T
).
}
$$

---

# 84. Temporary Cognitive Organization

當：

$$
\mathbf X
$$

按任務變化，系統不是固定員工名冊，而是在生成：

$$
\boxed{
\text{temporary cognitive organization}.
}
$$

---

# 85. Externalized MoE 與 Mother AI

$$
\boxed{
\text{Mother AI}
+
\text{External Cognitive Experts}
}
$$

更接近：

$$
\boxed{
\text{persistent cognitive core}
+
\text{dynamically assembled capability field}.
}
$$

---

# 86. External Expert 能力可以超過 Mother

可以：

$$
C_i(T)
>
C_M(T).
$$

只要 Mother 能 detect、delegate、verify 與 integrate。

因此局部 expert superiority 不破壞 global Mother coordination。

---

# 87. 但 Mother 必須知道自己較弱

如果：

$$
C_i>C_M
$$

但 Mother 不知道，就會自己硬做、錯誤覆蓋 expert 或驗證不足。

因此 capability self-model 仍是 resident core。

---

# 88. Externalization 可以降低 Resident Parameter Pressure

如果能力：

$$
c
$$

可由：

$$
X_c
$$

可靠提供，resident model 未必需要為低頻能力保留同等高解析度容量。

理論上：

$$
P_R\downarrow
$$

可能成立。

但 weight-level 如何做到，不在本文公開範圍。

---

# 89. Externalization 不等於 Delete Parameters

$$
\boxed{
\text{Capability Externalization}
\neq
\text{Parameter Deletion}.
}
$$

現有 neural representations 高度糾纏。

因此第一代可以先做 system-level externalization，而不是 weight surgery。

---

# 90. 三階段研究路線

## 第一代

$$
M_{\mathrm{frontier}}
+
\mathcal X.
$$

研究 routing、cost、capability map、verification 與 externalization gain。

## 第二代

$$
M_{\mathrm{smaller}}
+
\mathcal X.
$$

研究較小 Mother Core 是否能維持系統能力。

## 第三代

$$
K_{\mathrm{native}}
+
\mathcal C_Q
+
\mathcal C_X.
$$

研究 native Cognitive Kernel。

---

# 91. 十三類失敗模式

## 91.1 Granularity Too Fine

外部呼叫頻率過高，latency 爆炸。

## 91.2 Granularity Too Coarse

expert 專門化優勢消失。

## 91.3 Context Loss

context projection 丟失關鍵前提。

## 91.4 Context Overload

為避免 loss，把全部 context 都送出去。

## 91.5 Router Misclassification

選錯 expert。

## 91.6 Expert Drift

外部模型更新後能力改變。

## 91.7 Verification Collapse

產生速度遠超 verifier。

## 91.8 Authority Leakage

expert 取得超出角色需要的權限。

## 91.9 Vendor Lock-In

核心能力依賴單一 provider。

## 91.10 Reconvergence Failure

多 expert 結果無法一致整合。

## 91.11 Hidden Coordination Tax

多模型架構實際成本高於單體。

## 91.12 False MoE Analogy

把 external model routing 直接宣稱為 token-level MoE 等價物。

## 91.13 Core Hollowing

外置過多，使 Mother AI 無法驗證外部結果。

---

# 92. 十五項主要命題

## 命題 1：Expert Physical Co-Residence 非必要命題

expert 的功能存在不必邏輯上要求與 core model 永久物理共居。

## 命題 2：Offloading 非 Externalization 命題

$$
\boxed{
\text{Expert Offloading}
\neq
\text{Cognitive Externalization}.
}
$$

## 命題 3：Granularity Lift 必要命題

Internal expert 若要 externalize，通常需要：

$$
\boxed{
\text{token-level}
\rightarrow
\text{operation-level}.
}
$$

## 命題 4：Capability Interface 命題

Externalization 的最小單位更適合是 Capability Contract，而不是 parameter block。

## 命題 5：Role–Executor Separation 命題

$$
\boxed{
\text{Role}
\neq
\text{Executor}.
}
$$

## 命題 6：Model Boundary 非 Intelligence Boundary 命題

系統級智能可以跨多模型與工具存在。

## 命題 7：Macro Conditional Compute 命題

External routing 是 coarse-grained conditional compute 的一種形式。

## 命題 8：Verification-Enables-Externalization 命題

越可獨立驗證的能力，越適合 externalization。

## 命題 9：Interaction Granularity 命題

能力是否適合 externalize，高度取決於交互粒度與頻率。

## 命題 10：External Expert Heterogeneity 命題

expert 不必是 LLM，可以是 deterministic tool、retrieval、human 或 simulator。

## 命題 11：Dynamic Placement 命題

能力可以在：

$$
R,Q,X
$$

之間隨時間遷移。

## 命題 12：Externalized System Gain 命題

存在任務分布，使：

$$
Q(M+\mathcal X)
>
Q(M)
$$

且總 cognitive density 提高。

## 命題 13：Externalization Tax Bound 命題

若：

$$
C_X
$$

超過能力增益，externalization 應被拒絕。

## 命題 14：Mother-as-Meta-Router 命題

Mother AI 需要選擇的不只是 model，還包括 topology、verification 與 authority。

## 命題 15：Externalized MoE Bridge 命題

Macro-MoE 可以成為 Internal Conditional Intelligence 與 Expandable Intelligence 之間的架構橋梁。

---

# 93. 十組可否證實驗

## 實驗 1：Same Task, Internal vs External

比較 resident model、internal conditional expert 與 external specialist。

測：

$$
Q,
C,
L,
V.
$$

## 實驗 2：Granularity Sweep

從 cognitive operation 到 whole-task 改變切分粒度，測：

$$
\eta_E(g).
$$

尋找：

$$
g^\ast.
$$

## 實驗 3：Context Projection Ablation

逐步減少：

$$
C_T.
$$

測：

$$
Q_X.
$$

找 Minimum Sufficient Delegation Context。

## 實驗 4：Expert Substitution

同一 role：

$$
R
$$

切換：

$$
X_1,X_2,X_3.
$$

測 role continuity。

## 實驗 5：Provider Failure

讓：

$$
X_1\rightarrow\bot.
$$

測 fallback latency、quality 與 state preservation。

## 實驗 6：Verification Cost Crossover

比較 cheap expert + strong verifier 與 expensive expert + weak verifier。

## 實驗 7：Heterogeneous Executor

同一任務部分交 LLM、Python、compiler、retrieval，測 best mixed topology。

## 實驗 8：MoA vs Router vs Mother Planner

比較 layered Mixture-of-Agents、simple model router 與 Mother topology planner。

## 實驗 9：External Expert Drift

固定 task suite，比較模型版本更新前後：

$$
\Delta Q_i.
$$

## 實驗 10：Smaller Mother + External Pool

比較：

$$
M_L
$$

large monolithic，

與：

$$
M_S+\mathcal X.
$$

固定 total cost 或最低品質門檻，測 cognitive density。

---

# 94. 什麼結果會支持本文？

以下結果會支持：

1. external specialists 在某些能力上可替代 resident high-cost execution；
2. operation-level granularity 存在穩定效益區；
3. context compilation 可以顯著小於 full context 而維持品質；
4. role 可跨 model / provider 保持功能連續；
5. heterogeneous executor mix 優於 all-LLM；
6. cheap-worker + verifier 具有較高 verified utility；
7. provider failure 能 graceful failover；
8. smaller Mother + expert pool 在等成本下達到或超過 large monolith；
9. expert qualification history 能改善 routing；
10. externalization gain 能跨多 task family 重現。

---

# 95. 什麼結果會削弱本文？

以下結果會削弱：

1. external interface cost 長期高於能力節省；
2. context projection 無法保留足夠 cognition；
3. capability 無法形成可重用 contract；
4. external experts 表示差異使 reconvergence 高度不穩；
5. routing error 抵消所有專門化收益；
6. verification cost 使 cheap expert 不再便宜；
7. provider drift 使 qualification 無法維持；
8. smaller Mother 無法治理更強 external experts；
9. macro routing 只適合少數極粗任務；
10. monolithic frontier model 在等總系統成本下持續全面支配。

---

# 96. 公開命題與未公開實作邊界

本文公開：

- Micro / Meso / Macro-MoE；
- Granularity Lift；
- External Cognitive Expert contract；
- routing / verification / reconvergence concepts；
- externalization cost；
- dynamic placement；
- falsification tests。

本文不公開：

- 如何從 neural MoE 自動抽出 cognitive operation；
- private high-dimensional capability projection；
- latent-to-contract compiler；
- parameter disentanglement；
- external expert bridge encoding；
- capability substitution search；
- reconvergence optimizer；
- core retraining / convergence method。

因此：

$$
\boxed{
\text{Externalized Expert Architecture}
\neq
\text{Disclosure of the Extraction Method}.
}
$$

---

# 97. 與 Paper 06 的銜接

Paper 05 回答：

> 如果能力可以被描述成 external expert，架構上如何存在？

但尚未回答：

> **如何從成熟模型中真正辨認、分離、壓縮與重組這些能力？**

因此下一篇：

$$
\boxed{
\text{Cognitive Factorization Problem}.
}
$$

它將正式處理：

$$
\boxed{
D,C,X,L,R,G
}
$$

即 Decompose、Compress、Expand、Link、Reconcile、Converge。

---

# 98. 結論

Internal MoE 已經證明：

$$
\boxed{
\text{not every capability must be active at every moment}.
}
$$

Expert offloading 又證明：

$$
\boxed{
\text{not every expert weight must remain on the active accelerator}.
}
$$

Modular expert training、model routing、Mixture-of-Agents 與 external-router systems 再進一步顯示：

$$
\boxed{
\text{specialized capability can increasingly be trained, stored, selected, and combined across modular boundaries}.
}
$$

因此本文提出下一個問題：

$$
\boxed{
\text{Why must an expert remain inside one model at all?}
}
$$

答案不是：

> 把 MoE expert 直接搬到網路。

真正需要的是：

$$
\boxed{
\text{Granularity Lift}.
}
$$

將 fine neural computation 提升為：

$$
\boxed{
\text{governable cognitive operation}.
}
$$

接著由：

$$
\boxed{
X_i
=
(
R_i,
I_i,
O_i,
C_i,
S_i,
A_i,
V_i,
H_i
)
}
$$

這類 External Cognitive Expert 提供。

如果這個方向成立，未來一個 AI 系統的能力集合可能不再只是：

$$
\mathcal C(M).
$$

而是：

$$
\boxed{
\mathcal C_{\mathrm{system}}
=
\mathcal C_R
\cup
\mathcal C_Q
\cup
\mathcal C_X.
}
$$

其中核心認知常駐，高交互、低延遲專門能力條件激活，低頻、高解析度、可替換能力外部展開。

這意味 One Intelligence 未來可能是一個：

$$
\boxed{
\text{persistent cognitive center}
+
\text{dynamically assembled expert field}
}
$$

而不再必須是一個：

$$
\boxed{
\text{single ever-expanding model checkpoint}.
}
$$

這就是 Externalized Mixture of Cognitive Experts 的核心命題。

---

# References

1. Xue, L., Fu, Y., Lu, Z., Mai, L., & Marina, M. K. (2024). *MoE-Infinity: Offloading-Efficient MoE Model Serving*. arXiv:2401.14361.
2. Sukhbaatar, S., et al. (2024). *Branch-Train-MiX: Mixing Expert LLMs into a Mixture-of-Experts LLM*. COLM 2024 / arXiv:2403.07816.
3. Ong, I., et al. (2025). *RouteLLM: Learning to Route LLMs from Preference Data*. ICLR 2025.
4. Wang, J., et al. (2025). *Mixture-of-Agents Enhances Large Language Model Capabilities*. ICLR 2025.
5. Zhang, Q., et al. (2025). *BTS: Harmonizing Specialized Experts into a Generalist LLM*. EMNLP 2025.
6. Al-Maamari, M., Ben Amor, M., Mitrović, J., & Granitzer, M. (2025). *Mixture of Modular Experts: Distilling Knowledge from a Multilingual Teacher into Specialized Modular Language Models*. SAC 2025.
7. Li, W., et al. (2026). *LoRA-Mixer: Coordinate Modular LoRA Experts Through Serial Attention Routing*. ICLR 2026.
8. Morrison, J., et al. (2026). *Train Separately, Merge Together: Modular Post-Training with Mixture-of-Experts*. arXiv:2604.18473.
9. Luo, Y., et al. (2026). *RouteLMT: Learned Sample Routing for Hybrid LLM Translation Deployment*. arXiv:2604.22520.
10. *MoIRA: Modular Instruction Routing Architecture for Multi-Task Robotics*. Neurocomputing, 2026.
11. Chamma, A., El Herraoui, O., & Shang, G. (2026). *MixtureKit: A General Framework for Composing, Training, and Visualizing Mixture-of-Experts Models*. ACL 2026 System Demonstrations.
12. Neo.K. & Aletheia. (2026). *Cognitive Density Hypothesis：認知密度命題*.
13. Neo.K. & Aletheia. (2026). *Resident Cognitive Core：Mother Model 到底必須常駐什麼？*.
14. Neo.K. & Aletheia. (2026). *MoE as Conditional Intelligence：Shared Core、Routed Experts 與能力局部化*.
15. Neo.K. & Aletheia. (2026). *子 AI 是認知器官，不是獨立 Workflow*.
16. Neo.K. & Aletheia. (2026). *母 AI、世界狀態機與子智能網路：三向耦合的 AI 中心動態認知架構*.

---

# Canonical Source Note

本檔案為正式 UTF-8 Markdown canonical source。

數學 source 僅使用：

```text
 $...$
$$...$$
```

本文為公開命題論文。

本文公開 Externalized Mixture of Cognitive Experts 的架構定義、Micro / Meso / Macro-MoE、Granularity Lift、External Cognitive Expert contract、routing / verification / reconvergence 問題、externalization cost、dynamic capability placement 與 falsification framework。

本文不公開任何未驗證或未公開的 weight-level cognitive factorization、private capability projection、latent-to-contract compiler、parameter disentanglement、expert extraction、external bridge encoding、capability substitution search、reconvergence optimization 或 core retraining / convergence method。

因此：

$$
\boxed{
\text{Public Architecture Proposition}
\neq
\text{Private Technical Realization}.
}
$$
