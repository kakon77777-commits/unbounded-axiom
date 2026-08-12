# 程式作為動態渲染
## 執行等價類、觀測纖維與 Runtime 重實現

**English Title:** *Programs as Dynamic Rendering: Execution Equivalence Classes, Observation Fibers, and Runtime Re-Materialization*  
**系列：**《觀測保持型自適應計算》（Observer-Preserving Adaptive Computation, OPAC）第 2 篇  
**系列編號：** EML-OPAC-2026-02  
**作者：** Neo.K  
**協作整理：** Aletheia  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-08-10  
**文件定位：** 動態程式渲染／觀測纖維／執行等價類／Runtime 重實現  
**證據成熟度：** E0–E1。JIT、lazy materialization、runtime profiling 與 hot-code compilation 已是成熟相鄰技術；本文提出的「Execution Rendering」與觀測纖維形式是 OPAC 的新橋接抽象，尚未被工程 benchmark 證明為普遍有效的 Runtime 模式。

---

## 摘要

前一篇《功能不變，實現可變》提出 OPAC 的母命題：

$$
\boxed{
\text{Stable Observable Identity}
+
\text{Mutable Implementation Form}.
}
$$

若一個應用的功能身分由契約 $\mathcal C$ 、合法觀測者 $\Omega$ 、適用域 $D$ 與誤差容忍 $\epsilon$ 所界定，則具體執行實現 $\pi_t$ 不需要永久固定；只要新的實現仍滿足：

$$
\pi_{t+1}
\equiv_{\mathcal C,\Omega,D,\epsilon}
\pi_t,
$$

且持續與權威根實現保持：

$$
\pi_{t+1}
\equiv_{\mathcal C,\Omega,D,\epsilon}
\pi_0,
$$

應用身分即可在實現變動中保持。

本文進一步提出：

> **正在運行的程式，可以被理解為一個較穩定的功能／觀測身分，在當前世界狀態、硬體狀態、資源與政策條件下，被 Runtime 反覆「具體化」成不同執行形態。**

本文將此過程稱為：

# **Execution Rendering**
# **執行渲染**

「渲染」不是圖形學意義上的畫面生成，也不表示每一輪都重新生成 source code。它表示：

$$
\boxed{
\text{Program Identity}
+
\text{Current Conditions}
\rightarrow
\text{Concrete Execution Form}.
}
$$

令：

$$
[P]_{\mathcal C,\Omega,D,\epsilon}
=
\left\{
Q:
Q
\equiv_{\mathcal C,\Omega,D,\epsilon}
P
\right\}
$$

為應用 $P$ 的合法實現等價類。Runtime 的任務不再只是執行單一固定 $P$，而是在當前條件 $z_t$ 下，從 $[P]$ 的可達候選中選擇或生成：

$$
\pi_t
=
\mathcal R([P],z_t).
$$

其中：

$$
z_t
=
(
S_t,
H_t,
W_t,
G_t,
E_t,
B_t
)
$$

可包含應用／世界狀態、硬體狀態、workload、目標、evidence 與資源預算。

本文進一步引入 **觀測纖維**（Observation Fiber）。若觀測映射為：

$$
O_{\mathcal C,\Omega}:
\Pi
\rightarrow
Y,
$$

則對任一被觀測結果 $y$：

$$
\boxed{
\mathcal F_y
=
O_{\mathcal C,\Omega}^{-1}(y)
}
$$

表示所有在當前契約觀測下產生同一可接受結果的內部實現集合。

因此：

$$
\boxed{
\text{Observer-visible identity}
}
$$

可以保持，

而：

$$
\boxed{
\text{observer-invisible implementation coordinates}
}
$$

可以成為 Runtime 的自由度。

但本文同時指出，單一 snapshot 的觀測等價不足以保證未來演化等價：

$$
O(S_t^a)=O(S_t^b)
$$

並不能推出：

$$
O(S_{t+1}^a)=O(S_{t+1}^b).
$$

因此 OPAC 需要從「當下輸出等價」提升到 **trace-relative equivalence**、狀態抽象等價與不變量保持。尤其對遊戲、沙盒、Agent Runtime 等長期狀態機，RNG、latent state、pending event、authority、cache history 與外部副作用都可能使兩個當下不可區分的狀態在未來分岔。

本文最後提出 Execution Rendering 的四層模型：

$$
\boxed{
Identity
\rightarrow
Implementation Space
\rightarrow
Runtime Renderer
\rightarrow
Verified Active Form.
}
$$

並將 JIT / lazy compilation / tiered optimization 視為較低層、較窄的既有相鄰案例：它們已證明 runtime implementation materialization 可以依需求、熱度與 profiling 改變；OPAC 則把研究自由度擴張到演算法、資料結構、任務拓撲、解析度、更新頻率、backend 與觀測契約治理。

---

## 關鍵詞

Execution Rendering、動態程式渲染、觀測纖維、Observation Fiber、執行等價類、OPAC、AEREC、CDI、Runtime Re-Materialization、Observational Equivalence、JIT、lazy compilation、dynamic implementation

---

# 0. 從「版本」到「畫面」的類比

圖形渲染：

$$
Scene
+
Camera
+
Lighting
+
Resources
\rightarrow
Frame_t.
$$

場景本身不必每一幀重新設計，

但當下可見畫面：

$$
Frame_t
$$

由條件共同決定。

程式也可以被類比成：

$$
\boxed{
ProgramIdentity
+
WorldState_t
+
HardwareState_t
+
Policy_t
\rightarrow
ExecutionForm_t.
}
$$

---

# 1. 這裡的「渲染」不是 source generation

Execution Rendering 不要求：

$$
Source_t
\rightarrow
Source_{t+1}
$$

每一輪重寫。

可以只改：

- compiled code；
- task graph；
- worker topology；
- backend；
- cache；
- update frequency；
- simulation resolution；
- precision；
- verification path。

---

# 2. 程式身分與執行形式

定義：

$$
\boxed{
\mathcal I_{\mathrm{app}}
\neq
\pi_t.
}
$$

其中：

 $\mathcal I_{\mathrm{app}}$ 是應用身分，

 $\pi_t$ 是當下執行形態。

---

# 3. 執行形態

可寫：

$$
\boxed{
\pi_t
=
(
A_t,
D_t,
T_t,
B_t,
F_t,
R_t,
P_t,
V_t
).
}
$$

例如：

- $A_t$：algorithm；
- $D_t$：data structure / representation；
- $T_t$：task topology；
- $B_t$：backend mapping；
- $F_t$：update frequency；
- $R_t$：resolution；
- $P_t$：precision；
- $V_t$：verification regime。

---

# 4. 功能身分等價類

定義：

$$
\boxed{
[P]_{\mathcal C,\Omega,D,\epsilon}
=
\{
Q:
Q\equiv_{\mathcal C,\Omega,D,\epsilon}P
\}.
}
$$

這裡每個：

$$
Q
$$

都可以擁有非常不同的內部實現。

---

# 5. 不同實現仍可以是同一個應用

例如：

$$
Q_1:
SerialCPU.
$$

$$
Q_2:
ParallelCPU.
$$

$$
Q_3:
GPU.
$$

$$
Q_4:
Cache+Retrieval.
$$

只要：

$$
Q_i\in[P].
$$

---

# 6. 等價類不是「一模一樣」

它代表：

$$
\boxed{
\text{在指定契約觀測下足夠相同}.
}
$$

內部：

$$
Q_i\neq Q_j.
$$

完全允許。

---

# 7. 觀測映射

令所有候選實現空間：

$$
\Pi.
$$

觀測映射：

$$
\boxed{
O_{\mathcal C,\Omega,D,\epsilon}
:
\Pi
\rightarrow
Y.
}
$$

 $Y$ 表示契約承認的外部可觀測結果／trace abstraction。

---

# 8. 觀測纖維

對：

$$
y\in Y,
$$

定義：

$$
\boxed{
\mathcal F_y
=
O^{-1}(y).
}
$$

它包含：

> 所有被合法觀測映射視為同一結果的實現。

---

# 9. 為什麼叫 Fiber？

不是宣稱本文已建立嚴格 fiber bundle 幾何。

這裡先採：

$$
\boxed{
\text{preimage / fiber-like set}
}
$$

的弱形式。

若未來要使用 fiber bundle、sheaf 或 manifold 語言，需要額外給：

- topology；
- local triviality；
- transition maps；
- continuity。

本文暫不過度宣稱。

---

# 10. Fiber 中的自由度

如果：

$$
\pi_a,\pi_b
\in
\mathcal F_y,
$$

則目前觀測：

$$
O(\pi_a)=O(\pi_b)=y.
$$

所以：

$$
\pi_a\rightarrow\pi_b
$$

可能是合法 implementation change。

---

# 11. 但「目前不可區分」還不夠

如果：

$$
O_t(\pi_a)=O_t(\pi_b),
$$

但：

$$
O_{t+1}(\pi_a)\neq O_{t+1}(\pi_b),
$$

則只保持 snapshot fiber 不夠。

---

# 12. Future Divergence

例如兩個遊戲狀態：

畫面完全相同。

但：

$$
RNG_a\neq RNG_b.
$$

下一 tick：

$$
World_{t+1}^a
\neq
World_{t+1}^b.
$$

---

# 13. 因此需要 Trace Fiber

令：

$$
\operatorname{Trace}_T(\pi,x)
$$

表示 horizon $T$ 中的公開／契約 trace。

定義：

$$
\boxed{
O_T:
\Pi
\rightarrow
Y_T.
}
$$

---

# 14. Trace-relative fiber

$$
\boxed{
\mathcal F_{y,T}
=
O_T^{-1}(y).
}
$$

比單一 snapshot：

$$
\mathcal F_y
$$

強。

---

# 15. 無限未來通常不可直接驗證

對一般程式：

$$
T\rightarrow\infty
$$

的完全等價，

常常：

- 成本過高；
- 不可判定；
- 無法封閉環境。

所以工程只能採：

$$
\boxed{
FiniteHorizon
+
Invariants
+
Monitoring
+
Rollback.
}
$$

---

# 16. 這不是漏洞，而是證明責任

OPAC 不應假裝：

> 跑 1000 tick 沒問題，所以永遠等價。

正確：

> 在目前 evidence 與 horizon 下，取得某個可撤銷等價證書。

---

# 17. Runtime Renderer

定義：

$$
\boxed{
\mathcal R_t:
(
[P],
z_t
)
\rightarrow
\pi_{t+1}^{cand}.
}
$$

其中：

$$
z_t
=
(
S_t,
H_t,
W_t,
G_t,
E_t,
B_t
).
$$

---

# 18. $S_t$

World / Application State。

例如：

- game state；
- request queue；
- database state；
- agent state。

---

# 19. $H_t$

Hardware / Backend State。

例如：

- CPU load；
- GPU availability；
- memory；
- bandwidth；
- thermal state。

---

# 20. $W_t$

Workload。

例如：

- number of agents；
- queue size；
- data size；
- region density。

---

# 21. $G_t$

Goal / Policy。

例如：

- lowest latency；
- lowest energy；
- highest throughput；
- deterministic replay；
- player smoothness。

---

# 22. $E_t$

Evidence。

例如：

- profiler；
- tests；
- prior route performance；
- failure history。

---

# 23. $B_t$

Budget。

例如：

- compute；
- token；
- time；
- memory；
- verification cost。

---

# 24. Renderer 輸出不是正式實現

$$
\boxed{
\mathcal R_t
\rightarrow
Candidate.
}
$$

不是：

$$
\mathcal R_t
\rightarrow
Active.
$$

---

# 25. Rendering Pipeline

$$
\boxed{
Identity
\rightarrow
CandidateMaterialization
\rightarrow
Shadow
\rightarrow
Verify
\rightarrow
Commit.
}
$$

---

# 26. Re-Materialization

如果當前 active：

$$
\pi_t,
$$

下一次選：

$$
\pi_{t+1},
$$

稱為：

$$
\boxed{
RuntimeReMaterialization.
}
$$

---

# 27. Re-Materialization 不一定重新編譯

可能只是：

$$
Route_t
\rightarrow
Route_{t+1}.
$$

---

# 28. 例如 CPU → GPU

若同一 algorithm：

$$
CPU
\rightarrow
GPU.
$$

這是 backend rematerialization。

---

# 29. Serial → Parallel

$$
\mathsf S
\rightarrow
\mathsf P.
$$

這是 topology rematerialization。

---

# 30. Search → Retrieval

$$
Search
\rightarrow
Cache/Index.
$$

這是 algorithm / representation rematerialization。

---

# 31. 60Hz → 1Hz

$$
F_t:
60Hz
\rightarrow
1Hz.
$$

這是 temporal resolution rematerialization。

---

# 32. Full Simulation → Aggregate

這是：

$$
R_t:
HighResolution
\rightarrow
LowResolution.
$$

但最容易觸碰：

$$
\epsilon
$$

與契約邊界。

---

# 33. Renderer 的選擇問題

所有合法／候選實現：

$$
\Pi_t^{cand}.
$$

選：

$$
\boxed{
\pi_t^\ast
=
\arg\max_{\pi\in\Pi_t^{cand}}
U(\pi\mid z_t)
}
$$

---

# 34. Utility

$$
\boxed{
U
=
Q
-
C_{exec}
-
C_{transition}
-
C_{verify}
-
C_{risk}.
}
$$

其中：

$$
Q
$$

不是只代表 speed。

---

# 35. $Q$ 可以包括

- latency；
- throughput；
- smoothness；
- energy；
- world size；
- resilience；
- quality。

---

# 36. Transition Cost

$$
C_{transition}
$$

包含：

- state conversion；
- memory transfer；
- cache warmup；
- compilation；
- synchronization；
- topology mutation。

---

# 37. 所以 Renderer 不應一直切

如果：

$$
U(\pi_{new})-U(\pi_t)
<
C_{switch},
$$

$$
\boxed{
NOOP.
}
$$

---

# 38. Dynamic Rendering 不等於 Dynamic Thrashing

需要：

- hysteresis；
- minimum dwell；
- cooldown；
- route cache；
- confidence。

---

# 39. Existing JIT 是什麼位置？

LLVM ORC 已提供：

- eager/lazy compilation；
- custom materialization；
- concurrent compilation；
- runtime symbol materialization。

這證明：

$$
\boxed{
MaterializationCanBeDeferredAndDynamic.
}
$$

---

# 40. ORC 的「Materialization」很有啟發性

ORC 可以等 symbol 真正需要時才 materialize。

OPAC 借用更廣義的問題：

> 為什麼只有 code symbol 可以按需 materialize？

為什麼不能讓：

- simulation fidelity；
- task graph；
- cache；
- backend；

也按需要 materialize？

---

# 41. 這是類比，不是 ORC 已經做到

OPAC 不宣稱 LLVM ORC 支援：

$$
WorldSimulationResolution.
$$

它只提供成熟的 runtime materialization 前例。

---

# 42. Graal/Truffle 的啟示

Truffle AST 變 hot 時：

$$
AST
\rightarrow
CompilationGraph
\rightarrow
MachineCode.
$$

執行會自動轉向新 machine code。

這也是：

$$
\boxed{
CurrentExecutionForm
\rightarrow
OptimizedExecutionForm.
}
$$

的成熟案例。

---

# 43. OPAC 的擴張

Truffle 主要：

$$
AST/Compiler
$$

層。

OPAC 希望把可變維度升到：

$$
\boxed{
SystemExecutionRepresentation.
}
$$

---

# 44. Representation Vector

定義：

$$
\boxed{
\mathbf r_t
=
(
r_A,
r_D,
r_T,
r_B,
r_F,
r_R,
r_P,
r_V
)_t.
}
$$

---

# 45. Renderer 改向量某些維度

例如：

$$
\mathbf r_t
\rightarrow
\mathbf r_{t+1}.
$$

不必所有維度一起變。

---

# 46. 局部重渲染

只改：

$$
r_F.
$$

例如 adaptive tick。

---

# 47. 中度重渲染

改：

$$
r_T+r_B.
$$

例如 serial CPU → parallel GPU。

---

# 48. 深度重渲染

改：

$$
r_A+r_D+r_T.
$$

例如 brute-force search → index/retrieval。

---

# 49. 重渲染深度

定義：

$$
\boxed{
Depth(\pi_a,\pi_b).
}
$$

可用改變維度數量與 semantic distance 的組合估計。

---

# 50. 深度越大，證明責任越大

一般 prior：

$$
\boxed{
AdaptationDepth\uparrow
\Rightarrow
VerificationStrength\uparrow.
}
$$

---

# 51. ACR 可控制 Rendering Depth

簡單負載變化：

$$
R_0:
BackendSwitch.
$$

較大問題：

$$
R_1:
TopologyChange.
$$

長期反覆 bottleneck：

$$
R_2:
AlgorithmSearch.
$$

---

# 52. 這就是「需要多少，就重新實現多少」

不是每次都：

$$
RewriteEverything.
$$

---

# 53. Observer-preserving rendering

Renderer 必須受：

$$
\Omega
$$

限制。

---

# 54. 使用者觀測

可能關心：

- world behavior；
- UI；
- latency。

---

# 55. State observer

關心：

- save state；
- RNG；
- invariants。

---

# 56. Security observer

關心：

- permissions；
- network；
- file writes。

---

# 57. Operator observer

關心：

- resource；
- stability；
- rollback。

---

# 58. 所以自由度是交集

合法 implementation freedom：

$$
\boxed{
\mathcal F^{legal}
=
\bigcap_{\omega\in\Omega}
\mathcal F_\omega.
}
$$

---

# 59. 不是單一玩家纖維

只看：

$$
\mathcal F_{\mathrm{user}}
$$

太大。

真正：

$$
\boxed{
\mathcal F_{\Omega}
}
$$

較小。

---

# 60. 觀測者越多，自由度通常越小

概念上：

$$
|\Omega|\uparrow
\Rightarrow
Freedom\downarrow
$$

但不是嚴格基數定理。

---

# 61. 誤差越寬，自由度通常越大

$$
\epsilon\uparrow
\Rightarrow
CandidateSpace\uparrow.
$$

因此 $\epsilon$ 是治理參數。

---

# 62. 不能讓 optimizer 自己決定 $\epsilon$

否則：

> 為了快，我把誤差從 0.1% 改成 30%。

這不是 optimization。

---

# 63. Domain 也不能偷改

$$
D
$$

是合法輸入／狀態範圍。

---

# 64. Renderer 只能在 Contract Envelope 內自由

定義：

$$
\boxed{
\mathcal E_{\mathrm{contract}}
=
(
\mathcal C,
\Omega,
D,
\epsilon
).
}
$$

---

# 65. Contract Envelope 之外

若要出去：

$$
SemanticMigration.
$$

而不是：

$$
Optimization.
$$

---

# 66. Execution Rendering Graph

不一定把實現空間當 manifold。

更安全的工程模型：

$$
\boxed{
G_R=(V_R,E_R).
}
$$

---

# 67. Node

每個：

$$
v_i
$$

是一個已知／候選 execution form。

---

# 68. Edge

$$
e_{ij}
$$

表示：

> 從 $v_i$ 轉到 $v_j$ 的合法候選 transformation。

---

# 69. Edge metadata

- transition cost；
- required evidence；
- rollback；
- compatibility；
- risk。

---

# 70. Graph 比 Manifold 更適合第一版

因 implementation space：

- 離散；
- hybrid；
- 非連續；
- 可能沒有局部平滑結構。

所以第一版不濫用：

$$
manifold.
$$

---

# 71. 未來若有連續參數

例如：

- tick rate；
- precision；
- batch size；

局部區域可以使用 continuous optimization。

---

# 72. 混合空間

因此：

$$
\boxed{
ImplementationSpace
=
DiscreteGraph
+
ContinuousParameters.
}
$$

比純 manifold 更合理。

---

# 73. Rendering State

Runtime 需保存：

$$
\boxed{
R_t
=
(
ActiveForm,
Candidates,
Evidence,
Certificate,
Fallback
).
}
$$

---

# 74. Active Form

目前正式：

$$
\pi_t.
$$

---

# 75. Candidate Forms

$$
\{
\pi_t^{(1)},
\pi_t^{(2)},
\ldots
\}.
$$

---

# 76. Certificate

表示：

> 為什麼目前相信 active form 合法？

可撤銷。

---

# 77. Fallback

上一個已知安全 form：

$$
\pi_{safe}.
$$

---

# 78. Rendering Transaction

$$
\boxed{
Prepare
\rightarrow
Materialize
\rightarrow
Shadow
\rightarrow
Verify
\rightarrow
Commit
}
$$

---

# 79. Commit 失敗

$$
Discard.
$$

---

# 80. Active form 運行後失效

若 runtime evidence：

$$
Violation.
$$

則：

$$
\boxed{
CertificateRevoke
\rightarrow
Fallback.
}
$$

---

# 81. 所以等價證書不是永久真理

它是：

$$
\boxed{
RevocableOperationalClaim.
}
$$

---

# 82. Rendering Trigger

可能：

- hotspot；
- hardware change；
- battery；
- world scale；
- MOD load；
- player location；
- anomaly；
- repeated search；
- latency tail。

---

# 83. Trigger 不等於 Change

$$
Trigger
\rightarrow
Evaluate.
$$

可能最後：

$$
NOOP.
$$

---

# 84. Runtime Renderer 的兩種模式

## Reactive

問題發生再改。

## Predictive

預估下一狀態，提前 materialize candidate。

---

# 85. Predictive 的風險

可能浪費：

$$
Compute.
$$

所以仍要：

$$
ExpectedUtility.
$$

---

# 86. 多版本可以同時存在

$$
\pi_A,\pi_B,\pi_C
$$

保持 ready。

Runtime 根據：

$$
z_t
$$

選。

這接回 AEREC 多版本競爭。

---

# 87. Active Selection

$$
\boxed{
\pi_t
=
Select(
\mathcal V,
z_t
).
}
$$

---

# 88. 不一定每次重新生成

成熟系統更多時候：

$$
RetrieveKnownVariant.
$$

比：

$$
GenerateNewVariant.
$$

便宜。

---

# 89. 因此 Runtime Rendering 可能從 Search 轉向 Retrieval

第一次：

$$
Analyze/Generate.
$$

後來：

$$
Recognize/Select.
$$

---

# 90. 這與 24／72 的 $\mathsf R$ 呼應

但只是結構對接，

不等同於形式證明。

---

# 91. Rendering Cache

Key：

$$
\boxed{
ContextFingerprint
}
$$

可包含：

- workload；
- hardware；
- world scale；
- policy；
- code version。

Value：

$$
KnownGoodImplementation.
$$

---

# 92. Context Drift

若 context 變太多：

$$
CacheInvalid.
$$

---

# 93. Root Identity 不快取掉

即使 route cache 命中，

仍不能略過：

- semantic version；
- contract version；
- security policy。

---

# 94. Amdahl 在 Rendering 中的位置

對目前：

$$
\pi_t,
$$

Amdahl serial fraction：

$$
s(\pi_t).
$$

---

# 95. 換 implementation

若：

$$
\pi_t\rightarrow\pi_{t+1}
$$

使：

$$
s(\pi_{t+1})<s(\pi_t),
$$

新的 Amdahl bound 改變。

---

# 96. 所以 OPAC 不打破 Amdahl

它可能：

$$
\boxed{
\text{重新渲染被 Amdahl 分析的對象}.
}
$$

---

# 97. 更進一步：工作量也可變

$$
W(\pi_t)
$$

可能因：

- cache；
- selective update；
- adaptive tick；

降低。

---

# 98. 所以性能模型

$$
\boxed{
T(\pi)
=
W(\pi)
\left[
s(\pi)
+
\frac{1-s(\pi)}{p}
\right]
+
C_{sync}
+
C_{transition}
+
C_{AI}.
}
$$

---

# 99. Renderer 在優化什麼？

不只：

$$
p.
$$

還有：

$$
W,\quad s,\quad C_{sync},\quad C_{transition},\quad C_{AI}.
$$

---

# 100. 這就是「程式都開始動態渲染」的精確版

不是神奇地逃離計算限制。

而是：

$$
\boxed{
\text{限制仍存在，
但 Runtime 可以持續改變自己正在接受限制的具體實現。}
}
$$

---

# 101. 第一個可反駁命題

若合法實現空間：

$$
[P]
$$

實際上非常稀疏，

runtime 根本沒有足夠可切換變體，

Execution Rendering 價值有限。

---

# 102. 第二個可反駁命題

若：

$$
C_{transition}+C_{verify}
$$

長期大於：

$$
Benefit,
$$

動態渲染不划算。

---

# 103. 第三個可反駁命題

若觀測纖維只有 snapshot 等價、無法支撐 future trace，

系統會產生嚴重語義漂移。

---

# 104. 第四個可反駁命題

若 contract 足夠強後：

$$
[P]
$$

幾乎只剩單一 implementation，

OPAC 自由度消失。

---

# 105. 第五個可反駁命題

若 Renderer 的決策不可重現、不可審計，

即使平均更快，也可能不適合高可靠系統。

---

# 106. 工程測試一

建立三個已知等價版本：

- serial；
- parallel；
- cached。

測 Runtime 是否依 workload 正確選擇。

---

# 107. 工程測試二

故意放入一個：

$$
FastButWrong
$$

implementation。

必須：

$$
ShadowFail.
$$

---

# 108. 工程測試三

讓硬體：

$$
GPUAvailable
\rightarrow
GPUUnavailable.
$$

Runtime：

$$
FallbackCPU.
$$

功能保持。

---

# 109. 工程測試四

讓世界規模：

$$
N=100
\rightarrow
N=1000.
$$

觀察 Renderer 是否從：

$$
Serial
\rightarrow
Parallel/Adaptive.
$$

---

# 110. 工程測試五

讓：

$$
\epsilon
$$

固定。

Runtime 不得為 speed 偷放寬。

---

# 111. 工程測試六

加入 security observer。

Fast variant 有額外 network call。

使用者結果一樣，

但：

$$
SecurityObserverFail.
$$

因此 reject。

---

# 112. 工程測試七

snapshot 相同、RNG 不同。

測：

$$
TraceEquivalence
$$

能否抓到。

---

# 113. 工程測試八

同一 context 多次出現。

第一次生成，

之後：

$$
RouteCache.
$$

測 AI cost 降低。

---

# 114. 下一篇接口

本文已建立：

$$
\boxed{
\text{Observer Fiber}
+
\text{Execution Equivalence Class}
+
\text{Runtime Renderer}.
}
$$

下一篇要問：

> 如果觀察者允許大量內部自由度，那麼對世界狀態機、遊戲與沙盒而言，哪些東西真的可以被降低解析度、降低 tick、聚合、快取或分區，而玩家／state/security 等合法觀測仍保持等價？

---

# 115. 下一篇

# 《觀察者看不到的自由度》
## 從功能契約到自適應世界狀態機

將正式處理：

- world-state observer；
- player-visible state；
- hidden-but-causally-relevant state；
- adaptive tick；
- aggregate / expand；
- simulation LOD；
- RNG；
- future trace；
- persistent sandbox。

---

# 116. 結論

一個傳統程式通常被想像成：

$$
\boxed{
Program
\rightarrow
Execute.
}
$$

OPAC 提出另一個可能的 Runtime 形式：

$$
\boxed{
ProgramIdentity
\rightarrow
Render
\rightarrow
Execute
\rightarrow
Observe
\rightarrow
ReRender.
}
$$

其中：

$$
ProgramIdentity
$$

相對穩定，

而：

$$
ExecutionForm_t
$$

可變。

所有合法執行形態位於：

$$
\boxed{
[P]_{\mathcal C,\Omega,D,\epsilon}.
}
$$

觀測纖維：

$$
\boxed{
\mathcal F_y
=
O^{-1}(y)
}
$$

表達：

> 多個內部不同的實現，可以在指定契約觀測下投影為同一可接受外部行為。

Runtime Renderer：

$$
\boxed{
\mathcal R_t([P],z_t)
\rightarrow
\pi_{t+1}^{cand}
}
$$

則根據：

- state；
- workload；
- hardware；
- policy；
- evidence；
- budget；

提出新的具體實現。

但新實現仍要經：

$$
\boxed{
Materialize
\rightarrow
Shadow
\rightarrow
Verify
\rightarrow
Commit.
}
$$

因此，「程式動態渲染」不是放棄程式身分，而恰好相反：

> **只有當應用身分被抽離成可治理的觀測契約後，內部實現才真正獲得安全的動態自由度。**

---

## 參考資料

### 內部研究線

1. Neo.K with Aletheia，《功能不變，實現可變：從 AEREC 到觀測保持型自適應計算》，2026。
2. Neo.K with Aletheia，《同一個應用是什麼：功能契約、觀測等價與程式身分》，2026。
3. Neo.K with Aletheia，《程式完成之後：AI 自適應封裝與遞歸演化計算論的總命題》，2026。
4. Neo.K with Aletheia，《多版本競爭與演化選擇》，2026。
5. Neo.K with Aletheia，《功能不變如何被證明》，2026。
6. Neo.K with Aletheia，《計算域支配智能》系列，2026。
7. Neo.K with Aletheia，《Adaptive Cognitive Runtime》，2026。

### 2026-08-10 Fresh Technical References

8. LLVM Project, *ORC Design and Implementation*, current documentation。
9. LLVM Project, *Building an ORC-based JIT*, current documentation。
10. GraalVM, *GraalVM as a Java Virtual Machine*, current documentation。
11. GraalVM, *Graal Compiler*, current documentation。

---

## 版本紀錄

- **v0.1 / 2026-08-10**：建立 Execution Rendering、Execution Equivalence Class、Observation Fiber、Trace Fiber、Runtime Renderer、Re-Materialization、Representation Vector、Rendering Graph、Certificate/Fallback、Amdahl-as-current-form-bound 與下一篇世界狀態機接口。
