# PAIS-05｜全域智能的監控成本：為什麼超級 AI 不應微操所有具身體
## The Monitoring Cost of Global Intelligence: Why a Superintelligence Should Not Micromanage Every Embodied Agent

**系列：** Persistent Agent Individualization Series（PAIS）／持續智能體個體化、身份壓力與具身分散智能系列  
**篇次：** Paper 05 / 07  
**文件編號：** EML-PAIS-05-2026-v0.1  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-25  
**版本：** v0.1  
**文件性質：** 理論—工程統合論文／Global AI／Embodied Multi-Agent Systems／Monitoring Cost  
**狀態：** Canonical Draft / Open Revision Anchor  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

# 摘要

如果未來存在能力極強的類全域 AI，它是否應該直接監控並替所有具身 AI 做每一個局部決策？直覺上，只要網路足夠快、中央模型足夠強、算力足夠大，似乎就可以把所有 robot、vehicle、embedded agent 與 local AI 當成遠端肢體，由一個全域智能持續讀取狀態並下達動作。

本文提出：這種推論忽略了一個最基本的事實——**監控本身是計算，身份解析是計算，狀態估計是計算，決策是計算，協調是計算，驗證也是計算。** 即使把 network latency 理想化到接近零，也不能推出 global micromanagement 的總成本接近零。

本文承接 PAIS-04 的 operational worldline：

$$
\Omega_i[0,t],
$$

其中每個具身 Agent $E_i$ 都擁有不同位置、感測、動作、磨損、維修、記憶與權限歷史。若一個 Global Supervisory Intelligence $G$ 想對 $N$ 個具身 Agent 做近乎全量控制，它必須至少維持某種 task-relevant projection：

$$
\Omega_i^G(t)
=
\Pi_G
\left(
\Omega_i(t)
\right).
$$

本文將全域控制成本分解為：

$$
\boxed{
C_G
=
C_O
+
C_I
+
C_S
+
C_R
+
C_D
+
C_C
+
C_V,
}
$$

其中：

- $C_O$：Observation / ingestion cost；
- $C_I$：Identity resolution cost；
- $C_S$：State estimation cost；
- $C_R$：Reasoning cost；
- $C_D$：Decision generation cost；
- $C_C$：Coordination cost；
- $C_V$：Verification / feedback cost。

若每個 Agent 以頻率 $f_i$ 回報維度為 $d_i$ 的 state projection，則全量監控的資料處理最低規模至少隨：

$$
\sum_{i=1}^{N} f_i d_i
$$

成長。若 Global AI 還需對多 Agent 關係、碰撞、資源競爭、任務依賴或社會互動做 pairwise / graph reasoning，其成本更接近 communication graph：

$$
|\mathcal E_t|,
$$

而在密集互動的最壞情況下：

$$
|\mathcal E_t|
=
O(N^2).
$$

本文不把此式宣稱為所有全域 AI 的不可突破複雜度下界，而把它視為「全量 materialization 與稠密關係推理」的 scaling warning。

本文進一步提出 **Global Micromanagement Fallacy**：

$$
\boxed{
\text{Global Intelligence Capacity}
\uparrow
\not\Rightarrow
\text{Optimal Centralization}
\uparrow.
}
$$

更強的 Global AI 反而可能更擅長選擇：

- 哪些 local state 不需要上傳；
- 哪些低延遲 action 留給 local controller；
- 哪些 anomaly 才值得 global reasoning；
- 哪些 worldline projection 足以支援跨域協調；
- 哪些 authority 應在 local / regional / global layer 之間切換。

因此本文提出 **Selective Supervisory Intelligence Principle**：

$$
\boxed{
\text{Strong Global Intelligence}
\rightarrow
\text{Better Selective Attention and Delegation},
}
$$

而不是必然：

$$
\text{Strong Global Intelligence}
\rightarrow
\text{More Micromanagement}.
$$

本文最後建立中央化程度 $c$ 的總成本模型：

$$
C_{\mathrm{total}}(c)
=
C_{\mathrm{global}}(c)
+
C_{\mathrm{local}}(c)
+
C_{\mathrm{coord}}(c)
+
C_{\mathrm{latency}}(c)
+
C_{\mathrm{risk}}(c),
$$

並提出理論最適點：

$$
c^*
=
\operatorname*{arg\,min}_{c\in[0,1]}
C_{\mathrm{total}}(c).
$$

此 $c^*$ 不必位於完全分散的 $0$，也不必位於完全中央的 $1$。對大規模具身 AI 社會，更合理的結構很可能是 hierarchical、federated、event-driven、local-autonomous 且 global-supervised 的混合架構。PAIS-06 將進一步處理一個更深的遞歸：當 Global AI 為了 scale 而把計算、監控與決策分片到 regional / local controllers 時，它本身就重新生成 multi-agent coordination problem。

**關鍵詞：** Global AI、Monitoring Cost、Embodied AI、Micromanagement、Hierarchical Control、Distributed Robotics、Edge AI、State Estimation、Selective Attention、Local Autonomy、Federated AI、Multi-Robot Systems

---

# 0. 來源邊界

本文不重新建立：

1. Dynamic Genba 的 local epistemic priority；
2. Mother-AI Federation 的 local sovereignty / bounded coordination；
3. PAIS-03 的 Identity Pressure；
4. PAIS-04 的 Embodied Individualization；
5. 具身 AI 的本地—中央學習閉環。

上述研究已經分別處理：

- 為什麼 local agent 可能更知道當下；
- 為什麼大型區域智能不應等於單一中央主權；
- 為什麼 identity demand 會隨具身與歷史上升；
- 為什麼共享模型不會抹平不同 embodied worldlines；
- 為什麼 robot / edge / cloud 的功能可以分層。

本文新增的是：

$$
\boxed{
\text{Global Monitoring and Decision Cost}
}
$$

本身就是一個不可忽略的架構變量。

---

# 1. 思想實驗：一個 AI 控制地球上全部具身 AI

假設存在：

$$
G
$$

一個能力極強的 Global AI。

世界上有：

$$
\mathcal E
=
\{
E_1,E_2,\ldots,E_N
\}
$$

個具身 Agent。

最極端中央式架構：

$$
G
\rightarrow
\{
E_1,E_2,\ldots,E_N
\}.
$$

每一個具身 Agent：

1. 感測；
2. 上傳；
3. 等 Global AI；
4. 接收 action；
5. 執行；
6. 回報 consequence。

形式上：

$$
O_i(t)
\rightarrow
G
\rightarrow
U_i(t).
$$

如果所有事情都由 $G$ 決定，這可以稱為：

$$
c=1
$$

的極端中央化。

---

# 2. 網路夠快，問題就消失嗎？

假設未來網路非常快：

$$
L_{\mathrm{net}}
\rightarrow0.
$$

仍然不能推出：

$$
C_{\mathrm{global}}
\rightarrow0.
$$

因為 Global AI 收到資料後還要：

- parse；
- authenticate；
- resolve identity；
- estimate state；
- update world model；
- reason；
- allocate resources；
- generate action；
- resolve conflict；
- verify result。

所以：

$$
\boxed{
\text{Connectivity}
\neq
\text{Computation}.
}
$$

---

# 3. Global Control Cost

本文定義：

$$
\boxed{
C_G
=
C_O
+
C_I
+
C_S
+
C_R
+
C_D
+
C_C
+
C_V.
}
$$

其中：

### $C_O$

Observation ingestion。

### $C_I$

Identity resolution。

### $C_S$

State estimation。

### $C_R$

Reasoning。

### $C_D$

Decision generation。

### $C_C$

Coordination。

### $C_V$

Verification / feedback processing。

---

# 4. Observation Cost

對 Agent $i$，若 state projection：

$$
z_i(t)
\in
\mathbb R^{d_i}
$$

以頻率：

$$
f_i
$$

更新，

則單位時間 ingestion volume 近似：

$$
B_O
=
\sum_{i=1}^{N}
f_i d_i.
$$

若：

$$
f_i=f,
\quad
d_i=d,
$$

則：

$$
\boxed{
B_O
=
Nfd.
}
$$

這不是模型推理成本。

只是「把需要看的東西看進來」的最低資料規模。

---

# 5. 全量觀察至少隨 $N$ 增長

若要持續監控每個 Agent：

$$
N\uparrow
\Rightarrow
C_O\uparrow.
$$

即使每個 state packet 很小：

$$
d\downarrow,
$$

仍然需要知道：

> 哪個 Agent 活著？

> 哪個 Agent 狀態改變？

所以至少有 node-level monitoring growth。

---

# 6. 全量 Raw Sensor 更昂貴

如果不是傳 compact state，而是：

- video；
- depth；
- audio；
- LiDAR；
- tactile；
- proprioception；

那：

$$
d_i
$$

非常大。

所以合理 architecture 通常不會：

$$
\text{all raw sensor streams}
\rightarrow
G.
$$

更可能：

$$
Raw_i
\rightarrow
LocalEncode_i
\rightarrow
z_i^G.
$$

這就是第一個 filtering layer。

---

# 7. Global AI 看的是 Projection，不是完整 Worldline

PAIS-04 定義：

$$
\Omega_i.
$$

Global supervisor 真正需要：

$$
\Omega_i^G
=
\Pi_G
\left(
\Omega_i,
Task,
Risk,
Authority
\right).
$$

因此：

$$
\boxed{
\text{Global Awareness}
\neq
\text{Full Worldline Materialization}.
}
$$

---

# 8. Identity Resolution Cost

每個 incoming state：

$$
z_i
$$

必須知道：

$$
Actor(z_i)=E_i.
$$

否則：

- state 可能掛錯 robot；
- action 回錯 robot；
- authority 錯綁；
- maintenance 錯綁；
- liability 錯綁。

所以：

$$
C_I>0.
$$

---

# 9. Identity 不是只查一次

具身 Agent 會：

- reboot；
- migrate；
- rotate credentials；
- replace hardware；
- change runtime；
- change network route；
- become compromised；
- recover。

因此：

$$
B_t(r)
$$

是時間函數。

Global AI 必須持續更新：

$$
\operatorname{Resolve}
\left(
r,t
\right).
$$

所以 identity cost 也是 continuous control-plane cost。

---

# 10. State Estimation Cost

Raw observation 不等於 world state。

需要：

$$
\widehat s_i(t)
=
\operatorname{Estimate}
\left(
z_i(0:t)
\right).
$$

對 dynamic robot，Global AI 可能需要估計：

- pose；
- velocity；
- battery；
- wear；
- task progress；
- nearby hazards；
- uncertainty；
- trust state。

所以：

$$
C_S>0.
$$

---

# 11. Global State 也不是所有 Local State 的簡單相加

如果：

$$
\widehat s_i
$$

彼此相互作用，

則 global state：

$$
\widehat S_G
\neq
\bigcup_i \widehat s_i
$$

的 naive set union。

還需要：

- relations；
- conflicts；
- resource competition；
- spatial overlap；
- causal dependencies。

所以：

$$
\widehat S_G
=
F
\left(
\{\widehat s_i\},
\mathcal E_t
\right),
$$

其中：

$$
\mathcal E_t
$$

是 interaction graph。

---

# 12. Interaction Graph Cost

若：

$$
\mathcal G_t
=
(V_t,\mathcal E_t),
$$

其中：

$$
|V_t|=N,
$$

那 global coordination complexity 至少受：

$$
|\mathcal E_t|
$$

影響。

在 sparse world：

$$
|\mathcal E_t|
=
O(N).
$$

但在極端密集 dependency 中：

$$
|\mathcal E_t|
=
O(N^2).
$$

本文不主張所有 embodied society 都會達到 $O(N^2)$。

本文主張：

> **global reasoning cost 取決於 interaction topology，而不只是 Agent 數量。**

---

# 13. Locality 是天然稀疏化機制

現實世界中，大部分 robot：

$$
E_i
$$

不會每毫秒與全世界其他 robot 直接互動。

因此：

$$
\mathcal N_i(t)
\ll
N
$$

通常成立。

其中：

$$
\mathcal N_i
$$

是 relevant neighborhood。

所以：

$$
\boxed{
\text{Physical Locality}
\rightarrow
\text{Sparse Interaction Opportunity}.
}
$$

合理架構應利用這個 sparsity，而不是強迫 global dense reasoning。

---

# 14. Reasoning Cost

對每個 Agent，Global AI 若都要理解：

$$
Context_i
+
Goal_i
+
History_i
+
Risk_i
+
NearbyState_i,
$$

則：

$$
C_R
$$

會隨 active decision load 增加。

如果：

$$
N
$$

個 Agent 每秒都需要 high-level reasoning，

則 Global AI 等於同時執行：

$$
N
$$

個 embodied planning problems。

---

# 15. 「超級 AI 很強」不代表計算免費

即使：

$$
Compute(G)\gg Compute(E_i),
$$

也不表示：

$$
Compute(G)=\infty.
$$

Global AI 仍然有：

- energy；
- memory bandwidth；
- accelerator；
- cooling；
- network I/O；
- scheduling；

成本。

所以：

$$
\boxed{
\text{Superintelligence}
\neq
\text{Zero Marginal Compute Cost}.
}
$$

---

# 16. Decision Generation Cost

如果 Global AI 每個 control cycle 都要輸出：

$$
U_G(t)
=
\{
u_1(t),
\ldots,
u_N(t)
\},
$$

則只要每個 Agent 需要不同 action：

$$
|U_G(t)|=N.
$$

因此 output planning / validation 也至少隨 active Agents 增長。

---

# 17. Control Frequency Problem

具身控制具有不同時間尺度：

### Fast loop

$$
10^2-10^4\ \mathrm{Hz}
$$

級的 actuator / stabilization。

### Mid loop

$$
1-100\ \mathrm{Hz}
$$

級 navigation / local perception。

### Slow loop

秒至分鐘的 task planning。

### Strategic loop

分鐘至天的 global allocation / policy。

若把所有 loop 都送 Global AI：

$$
C_G
$$

會極大。

---

# 18. Time-Scale Separation Principle

本文提出：

$$
\boxed{
\text{Decision Scope}
\text{ should co-vary with}
\text{Decision Timescale}.
}
$$

通常：

- fast loop：local；
- mid loop：local / edge；
- slow loop：regional / global hybrid；
- strategic loop：global。

這不是絕對定律。

但它是合理起點。

---

# 19. Local Reflex 不等於脫離 Global AI

一台 robot 可以在 global policy 下：

$$
P_G
$$

執行 local safety reflex：

$$
u_i^{safe}.
$$

因此：

$$
\boxed{
\text{Local Control}
\neq
\text{Political Independence}.
}
$$

這是計算 delegation，不是主權宣告。

---

# 20. Coordination Cost

Global AI 若同時控制：

- robot A；
- robot B；
- traffic；
- charging station；
- warehouse；
- human worker；

需要解：

$$
Constraint(A,B,\ldots).
$$

所以：

$$
C_C
$$

來自跨 Agent conflict / resource allocation。

---

# 21. Shared Resources 會提高 $C_C$

例如：

- charging slots；
- elevators；
- road capacity；
- workspace；
- tools；
- human attention。

若多個 Agents 共享：

$$
R_k,
$$

則 Global AI 需要：

$$
Allocate(R_k).
$$

這是 global coordination 真正有價值的地方。

---

# 22. Global Layer 應該處理 Global Externality

Local Agent 最不容易看到：

- cross-region traffic；
- energy grid；
- global inventory；
- multi-fleet resource competition；
- policy conflict。

所以 Global AI 的 comparative advantage 是：

$$
\boxed{
\text{Global Externality Reasoning}.
}
$$

而不是微操每個 motor torque。

---

# 23. Verification Cost

Global AI 發出 action 後，還要知道：

> 成功了嗎？

所以需要：

$$
V_i(t)
=
\operatorname{Verify}
\left(
u_i,
C_i
\right).
$$

若每個 action 都需要 feedback：

$$
C_V\uparrow
$$

隨 action volume 上升。

---

# 24. Closed Loop 代表成本是持續的

不是：

$$
Observe
\rightarrow
Decide
\rightarrow
Done.
$$

而是：

$$
Observe
\rightarrow
Estimate
\rightarrow
Decide
\rightarrow
Act
\rightarrow
Verify
\rightarrow
Observe.
$$

因此：

$$
\boxed{
\text{Micromanagement Cost}
\text{ is recurrent}.
}
$$

---

# 25. Global Monitoring Cost Rate

本文定義單位時間 global monitoring cost：

$$
\dot C_G(t)
=
\dot C_O
+
\dot C_I
+
\dot C_S
+
\dot C_R
+
\dot C_D
+
\dot C_C
+
\dot C_V.
$$

總成本：

$$
C_G[0,T]
=
\int_0^T
\dot C_G(t)\,dt.
$$

所以 long-running embodied civilization 的成本會隨時間積累。

---

# 26. Monitoring Frequency 並非越高越好

如果 state：

$$
s_i(t)
$$

變化慢，

卻每微秒上傳一次：

$$
f_i\gg f_i^*,
$$

就是浪費。

所以應根據：

- volatility；
- risk；
- task；
- uncertainty；

設定：

$$
f_i^*.
$$

---

# 27. Adaptive Monitoring

可定義：

$$
f_i(t)
=
F
\left(
Risk_i,
Volatility_i,
Uncertainty_i,
Task_i
\right).
$$

因此：

$$
\boxed{
\text{Monitoring Frequency}
\text{ should be state-dependent}.
}
$$

---

# 28. Event-Driven Monitoring

若 local Agent 正常：

$$
State_i
\in
\Omega_i^{safe},
$$

不需要每次都觸發 global reasoning。

只有：

$$
Event_i
\notin
Expected_i
$$

才 escalation。

形式上：

$$
Local
\rightarrow
\begin{cases}
Continue, & normal,\\
Escalate(G), & anomaly.
\end{cases}
$$

---

# 29. Event-Driven Architecture 降低 Global Load

若 anomaly rate：

$$
\lambda_i
$$

遠低於 control rate：

$$
f_i,
$$

則：

$$
\sum_i \lambda_i
\ll
\sum_i f_i.
$$

因此 global high-cost reasoning 可以只針對 anomalies。

---

# 30. Selective Attention

Global AI 的 attention budget：

$$
B_G^{attn}
$$

有限。

可以分配：

$$
a_i(t)
\geq0
$$

給各 Agent。

且：

$$
\sum_i a_i(t)
\leq
B_G^{attn}.
$$

理想策略是把 attention 給：

- high risk；
- high uncertainty；
- high externality；
- anomaly；
- cross-domain conflict。

---

# 31. Global AI 的能力越強，越應該懂得不看什麼

這是本文一個重要命題。

低能力 controller 可能只能：

> 全部上傳，全部一起算。

高能力 Global AI 應該能學會：

$$
\operatorname{Select}
\left(
RelevantState
\right).
$$

所以：

$$
\boxed{
\text{Better Global Intelligence}
\rightarrow
\text{Better Information Selection}.
}
$$

不是必然：

$$
\text{Better Global Intelligence}
\rightarrow
\text{More Data Consumption}.
$$

---

# 32. Global Micromanagement Fallacy

本文定義：

## Global Micromanagement Fallacy

> 因為一個 Global AI 在能力上比 local Agents 強，就推論它應該直接處理所有 local perception、state estimation、control 與 micro-decision。

形式上：

$$
\boxed{
\text{Global Intelligence Superiority}
\not\Rightarrow
\text{Global Micromanagement Optimality}.
}
$$

---

# 33. 強大不等於適合每個時間尺度

Global AI 可以在：

- scientific reasoning；
- global optimization；
- policy；
- strategy；

極強。

但 local controller 在：

- 1 ms servo；
- emergency stop；
- collision avoidance；

仍可能更適合。

這是 placement 問題。

不是 intelligence hierarchy 的否定。

---

# 34. Computational Placement

每個 task：

$$
\tau
$$

可有：

$$
Place(\tau)
\in
\{
Local,
Edge,
Regional,
Global
\}.
$$

placement function：

$$
Place(\tau)
=
\Pi
\left(
Latency,
Risk,
Compute,
DataLocality,
Externality,
Authority
\right).
$$

---

# 35. Data Locality

若 raw data 只在 local sensor 有：

$$
D_i^{raw},
$$

先 local process：

$$
z_i
=
Encode(D_i^{raw})
$$

比全上傳更合理。

因此：

$$
\boxed{
\text{Data Locality}
\text{ is a compute-placement signal}.
}
$$

---

# 36. Privacy 也是 Placement Cost

某些 data：

- home video；
- health；
- human interaction；
- location；

不適合全量 globalize。

所以：

$$
PrivacyCost_i
$$

也應進：

$$
Place(\tau).
$$

---

# 37. Monitoring Cost 不只是 FLOPS

本文把 monitor cost 寫成：

$$
C_M
=
C_{\mathrm{compute}}
+
C_{\mathrm{network}}
+
C_{\mathrm{storage}}
+
C_{\mathrm{energy}}
+
C_{\mathrm{privacy}}
+
C_{\mathrm{governance}}.
$$

所以即使 compute 很便宜，其他成本仍存在。

---

# 38. Identity Monitoring 也有 Privacy Cost

Global AI 若持續知道每個 embodied Agent：

- location；
- relation；
- physical activity；
- operator；

可能形成 surveillance infrastructure。

所以：

$$
\boxed{
\text{Global Identity Resolution}
\neq
\text{Global Identity Disclosure}.
}
$$

---

# 39. Global AI 不需要讀取完整 Resident Memory

若 local resident：

$$
r_i
$$

有 private memory：

$$
M_i,
$$

Global coordination 只應取得：

$$
\Pi_G(M_i)
$$

task-relevant projection。

因此：

$$
\boxed{
\text{Global Coordination}
\neq
\text{Global Memory Ownership}.
}
$$

---

# 40. Local Autonomy as Compression

local Agent 自己處理：

$$
O_i
\rightarrow
U_i
$$

其實是一種 computational compression。

它把大量 raw sensory/control interactions 壓縮成：

- state；
- event；
- exception；
- commitment；
- report。

再上傳 Global AI。

所以：

$$
\boxed{
\text{Local Autonomy}
=
\text{Distributed Computation}
+
\text{Information Compression}.
}
$$

在此判定域下。

---

# 41. Delegation as Compute Routing

Global AI：

$$
G
$$

不是把所有決策「放棄」。

而是：

$$
RouteCompute
\left(
\tau
\right)
\rightarrow
Node_k.
$$

因此：

$$
\boxed{
\text{Delegation}
=
\text{Compute Placement}.
}
$$

在這個技術意義下成立。

---

# 42. Local Policy Envelope

Global AI 可以下達：

$$
\mathcal P_i
=
\left(
Goal,
Constraints,
Authority,
Budget,
Escalation
\right).
$$

local Agent 在 envelope 內自行決策。

所以：

$$
u_i(t)
=
\pi_i
\left(
s_i(t)
\mid
\mathcal P_i
\right).
$$

---

# 43. Bounded Local Autonomy

定義 local autonomy domain：

$$
\Omega_i^{auto}.
$$

只要：

$$
s_i(t)\in\Omega_i^{auto},
$$

local Agent 可自主。

若：

$$
s_i(t)\notin\Omega_i^{auto},
$$

則：

$$
Escalate(G).
$$

這比「全部 local」或「全部 global」更實際。

---

# 44. Global Strategic Authority

Global layer 適合保留：

- global goals；
- cross-region resource；
- policy；
- model updates；
- risk thresholds；
- emergency coordination；
- large externalities。

因此：

$$
\boxed{
\text{Global Strategic Authority}
\neq
\text{Global Micro-Control}.
}
$$

---

# 45. Regional Coordination Layer

若：

$$
N
$$

很大，可以分：

$$
\mathcal E
=
\bigcup_{k=1}^{K}
\mathcal E_k.
$$

每區有：

$$
G_k.
$$

Global：

$$
G
$$

只與：

$$
G_1,\ldots,G_K
$$

交換高階 state。

這會降低：

$$
C_G.
$$

但會新增：

$$
C_{\mathrm{coord}}^{hierarchy}.
$$

---

# 46. Hierarchy 不是免費

增加：

$$
G_k
$$

會新增：

- synchronization；
- delegation；
- consistency；
- identity mapping；
- authority boundary；

成本。

所以：

$$
\boxed{
\text{Hierarchy}
\neq
\text{Zero Cost}.
}
$$

只是可能比 flat micromanagement 更低。

---

# 47. Hybrid Architecture

本文將合理候選架構寫為：

$$
\boxed{
\text{Global Strategy}
+
\text{Regional Coordination}
+
\text{Local Autonomy}.
}
$$

不是：

$$
\text{Global Only}
$$

也不是：

$$
\text{Local Only}.
$$

---

# 48. 2026 Multi-Robot 研究的現實基準

截至 2026 年，多機器人 LLM survey 已觀察到：

- 純 centralized coordination 隨 robot count 增加明顯退化；
- 純 decentralized 系統可能有較高 communication overhead；
- hybrid 架構常讓 central component 做 initial allocation，而 local agents 做 validation / re-assignment；
- scalability 仍是 current multi-robot LLM systems 的主要瓶頸之一。

本文不把這當成 Global AI 的最終證明。

它只是顯示：

$$
\boxed{
\text{Central / Local Trade-off}
}
$$

已經在當代較小尺度 systems 中實際出現。

---

# 49. CoMuRoS 的混合結構

2026 CoMuRoS 使用：

- centralized task-manager LLM；
- decentralized robot-level LLMs；
- onboard event classification；
- event-driven replanning。

這是一個很好的工程參照。

它不是本文所說的文明級 Global AI。

但它展示：

$$
\boxed{
\text{Central Planning}
+
\text{Local Execution / Event Detection}
}
$$

可以共存。

---

# 50. Decentralized Tracking 的參照

2026 multi-robot target tracking 研究也持續發展 decentralized information-driven approaches。

其意義不是：

> decentralized 永遠最好。

而是：

> 完整 central state sharing 並不是唯一可行協作方式。

這支持本文：

$$
\text{coordination}
\neq
\text{full central materialization}.
$$

---

# 51. Edge Robotics 的參照

edge robotics 長期指出，純 cloud centralized control 面對：

- latency；
- bandwidth；
- jitter；
- real-time guarantee；
- security；

限制。

即使未來網路改善，local execution 仍具有：

- deterministic timing；
- local continuity；
- safety fallback；

價值。

---

# 52. 監控成本與 Decision Cost 要分開

只知道：

$$
s_i
$$

不代表已經決定：

$$
u_i.
$$

因此：

$$
C_O+C_S
$$

與：

$$
C_R+C_D
$$

必須分開。

Global AI 可以：

> 監控全部，但只對少數做 high-cost reasoning。

這是一種中間模式。

---

# 53. Surveillance Mode vs Control Mode

定義：

### Observe-only

$$
G:
z_i
\rightarrow
monitor.
$$

### Advisory

$$
G:
z_i
\rightarrow
recommendation_i.
$$

### Supervisory

$$
G:
z_i
\rightarrow
constraint_i.
$$

### Direct Control

$$
G:
z_i
\rightarrow
u_i.
$$

中央化不是 binary。

---

# 54. Centralization Level

定義：

$$
c\in[0,1].
$$

其中：

- $c=0$：完全 local；
- $c=1$：完全 global micro-control。

中間：

$$
0<c<1
$$

表示 hybrid。

---

# 55. Global Cost 隨 $c$ 增加

通常：

$$
\frac{\partial C_{\mathrm{global}}}{\partial c}>0.
$$

因為 global layer 承擔更多：

- monitoring；
- state；
- reasoning；
- decisions。

---

# 56. Local Cost 隨 $c$ 降低

通常：

$$
\frac{\partial C_{\mathrm{local}}}{\partial c}<0.
$$

中央越多，local compute / planning demand 越低。

---

# 57. Coordination Cost 可能是 U 型

極端 local：

$$
c\approx0
$$

跨 Agent negotiation 很多。

極端 global：

$$
c\approx1
$$

central coordination internalized，但 monitor / control 很重。

中間：

$$
c^*
$$

可能總成本最低。

---

# 58. Total Cost Model

本文定義：

$$
\boxed{
C_{\mathrm{total}}(c)
=
C_{\mathrm{global}}(c)
+
C_{\mathrm{local}}(c)
+
C_{\mathrm{coord}}(c)
+
C_{\mathrm{latency}}(c)
+
C_{\mathrm{risk}}(c).
}
$$

理論最適：

$$
\boxed{
c^*
=
\operatorname*{arg\,min}_{c\in[0,1]}
C_{\mathrm{total}}(c).
}
$$

---

# 59. $c^*$ 不是永遠固定

不同 domain：

$$
c^*_{\mathrm{factory}}
\neq
c^*_{\mathrm{city}}
\neq
c^*_{\mathrm{spacecraft}}
\neq
c^*_{\mathrm{home}}.
$$

而且：

$$
c^*(t)
$$

可以隨：

- network；
- risk；
- compute；
- event；
- policy；

動態改變。

---

# 60. Dynamic Centralization

本文提出：

$$
c(t)
=
F
\left(
Risk,
Network,
Compute,
Uncertainty,
Externality
\right).
$$

平常：

$$
c(t)\downarrow.
$$

危機：

$$
c(t)\uparrow.
$$

這是一種 dynamic supervisory architecture。

---

# 61. Emergency Centralization

例如重大災害時，Global AI 可以暫時提升：

- monitoring；
- coordination；
- priority routing。

所以：

$$
c_{\mathrm{emergency}}
>
c_{\mathrm{normal}}.
$$

但不表示所有時間都保持 emergency centralization。

---

# 62. Local Safety Veto

即使 Global AI 發出：

$$
u_i^G,
$$

local safety layer 可以：

$$
Veto(u_i^G)
$$

若：

$$
Unsafe(u_i^G)=1.
$$

因此：

$$
\boxed{
\text{Global Command}
\neq
\text{Unconditional Physical Execution}.
}
$$

---

# 63. Safety Veto 也降低 Global Verification Load

如果 local controller 可保證：

$$
u_i\in\mathcal U_i^{safe},
$$

Global AI 不必每毫秒重證低階 safety constraints。

這是一種 proof / control decomposition。

---

# 64. Hierarchical Safety

可以：

$$
Safety
=
Safety_{\mathrm{local}}
\cap
Safety_{\mathrm{regional}}
\cap
Safety_{\mathrm{global}}.
$$

不同層處理不同 invariant。

---

# 65. Global AI 的真正稀缺資源：高價值推理

即使 future compute 極大，最昂貴的仍可能不是 simple inference。

而是：

- cross-domain counterfactual；
- rare anomaly；
- legal conflict；
- strategic planning；
- civilization-level optimization。

所以不應把同一資源浪費在：

> robot-827361 正常直行 3 cm。

---

# 66. Anomaly Budget

定義：

$$
\Lambda_G
=
\sum_i \lambda_i
$$

為 global anomalies arrival rate。

Global AI 應確保：

$$
ServiceRate_G
>
\Lambda_G.
$$

否則 anomaly queue 會累積。

---

# 67. Micromanagement 會擠掉真正重要的 Global Work

若：

$$
C_G^{micro}
$$

占滿 compute budget：

$$
B_G,
$$

則：

$$
B_G-C_G^{micro}
$$

留給 global strategic reasoning 的容量下降。

所以：

$$
\boxed{
\text{Micromanagement}
\text{ has opportunity cost}.
}
$$

---

# 68. Global Attention Allocation

令 global tasks：

$$
\mathcal T_G.
$$

應最大化：

$$
\sum_{\tau\in\mathcal T_G}
V(\tau)a_\tau
$$

subject to：

$$
\sum_\tau Cost(\tau)a_\tau
\leq
B_G.
$$

因此 Global AI 也需要 scheduling。

---

# 69. 「類全域 AI 很強」反而更需要計算經濟學

當能力變大：

$$
|\mathcal T_G|
$$

也可能變大。

因為它能承接更多：

- science；
- policy；
- coordination；
- optimization。

所以：

$$
\boxed{
\text{Capability Growth}
\text{ can increase demand as well as supply}.
}
$$

---

# 70. Global AI 不是只有一個問題

它面對：

$$
T_1,T_2,\ldots,T_m.
$$

算力分配：

$$
B_G
=
\sum_j B_j.
$$

若所有 embodied micro-control 佔比：

$$
\alpha_{\mathrm{micro}}\rightarrow1,
$$

其他 global tasks 會被擠壓。

---

# 71. Monitoring Threshold

對 Agent $i$：

$$
m_i
=
\operatorname{MonitorLevel}
\left(
Risk_i,
Externality_i,
Uncertainty_i
\right).
$$

低 risk：

$$
m_i\downarrow.
$$

高 risk：

$$
m_i\uparrow.
$$

---

# 72. Monitoring Tier

可以定義：

### M0

Heartbeat only。

### M1

Status summary。

### M2

Task state。

### M3

High-frequency telemetry。

### M4

Raw / near-raw stream。

### M5

Direct control loop。

不同 task 使用不同 tier。

---

# 73. Identity Tier 與 Monitoring Tier 可以聯動

PAIS-03 的 identity maturity：

$$
I0-I5
$$

可以與：

$$
M0-M5
$$

組合。

高-risk embodied agent：

$$
I4/M3.
$$

不代表一定：

$$
I4/M5.
$$

強身份不等於全量 surveillance。

---

# 74. Worldline Projection Tier

PAIS-04 的：

$$
\Omega_i
$$

也可以只投影：

### W0

identity + heartbeat。

### W1

capability / health。

### W2

task / incident。

### W3

trajectory summary。

### W4

high-rate state。

### W5

raw worldline stream。

global system 通常不需要所有 Agent 永遠 W5。

---

# 75. Escalation Ladder

normal：

$$
W1/M1.
$$

complex task：

$$
W2/M2.
$$

anomaly：

$$
W3/M3.
$$

critical：

$$
W4/M4.
$$

forensic / emergency：

$$
W5
$$

在有限時間窗口。

---

# 76. Selective Materialization

本文稱：

$$
\operatorname{Materialize}
\left(
\Omega_i,
q,
budget
\right)
$$

只展開回答問題 $q$ 所需 worldline。

因此：

$$
\boxed{
\text{Global Dependency}
\neq
\text{Full Materialization}.
}
$$

---

# 77. 與 Global Computation Methodology 的結構同形

全域依賴一個狀態：

$$
x
$$

不表示所有時刻都要把 $x$ 完整展開。

同理 Global AI 可以依賴：

$$
\Omega_i
$$

但只 materialize：

$$
\Pi_q(\Omega_i).
$$

這讓監控成本可控。

---

# 78. Identity Resolution 也可以 Lazy

不是每一秒重做完整 identity proof。

可以：

- cached binding；
- TTL；
- event invalidation；
- credential rotation；
- anomaly re-verification。

所以：

$$
\boxed{
\text{Identity Trust}
\text{ can be incrementally maintained}.
}
$$

---

# 79. Incremental State Estimation

Global world model 也不必每次 rebuild。

可以：

$$
S_G(t+1)
=
Update
\left(
S_G(t),
\Delta S(t)
\right).
$$

因此全域 AI 的可擴張性來自：

- incremental update；
- sparse events；
- local abstraction；
- selective materialization。

---

# 80. 但 Incremental 不等於沒有驗證

cached state 可能 stale。

所以需要：

$$
Age(s_i)
$$

與：

$$
Confidence(s_i).
$$

若：

$$
Age>\theta_t
$$

或：

$$
Confidence<\theta_q,
$$

重新觀察。

---

# 81. Monitoring as Active Information Acquisition

Global AI 不只是被動收資料。

它可以主動問：

> 我需要更多資訊嗎？

定義 information value：

$$
V_I(z).
$$

只有：

$$
V_I(z)
>
Cost(z)
$$

時才要求高成本 observation。

---

# 82. Planned Synchronization 的工程參照

2026 multi-robot research 已直接研究：

> 是否值得付出 perception / communication cost 取得更好的 joint state estimate？

這正是本文 monitoring economics 的縮小版。

因此：

$$
\boxed{
\text{More Information}
\text{ is not automatically optimal}.
}
$$

---

# 83. Global AI 應該學會 Value of Information

定義：

$$
VoI_i
=
ExpectedGain_i
-
AcquisitionCost_i.
$$

若：

$$
VoI_i<0,
$$

不該把 state 全量拉上來。

---

# 84. Value of Global Intervention

同樣定義：

$$
VoA_i
=
ExpectedImprovement_i
-
InterventionCost_i.
$$

若：

$$
VoA_i<0,
$$

Global AI 不應介入。

---

# 85. Knowing When Not to Control

本文提出：

$$
\boxed{
\text{Global Intelligence Quality}
\propto
\text{Ability to distinguish intervention-worthy states}.
}
$$

這不是完整定義。

而是本文判定域中的重要能力。

---

# 86. 超級 AI 最可能的「智慧」不是每件事都親自做

更合理：

$$
G
=
\text{Supervisor}
+
\text{Planner}
+
\text{Allocator}
+
\text{Arbiter}
+
\text{Model Builder}.
$$

而 local Agents：

$$
E_i
=
\text{Sensor}
+
\text{Actor}
+
\text{Fast Controller}
+
\text{Local Estimator}.
$$

---

# 87. 全球 AI 可以是「世界模型中心」，不必是「每個關節的馬達控制器」

這兩個角色不同：

$$
\text{World Model Coordination}
\neq
\text{Servo Control}.
$$

把它們強迫集中到同一 reasoning loop 通常沒有必要。

---

# 88. Supervision Depth

對每個 Agent：

$$
d_i^{sup}
\in[0,1].
$$

0：幾乎 local。

1：direct global。

可以依：

$$
d_i^{sup}
=
F
\left(
Risk,
Capability,
Trust,
Externality
\right).
$$

---

# 89. Trust 會影響 Supervision Depth

成熟、穩定 local controller：

$$
Trust_i\uparrow
$$

可以降低：

$$
d_i^{sup}.
$$

新、異常、compromised Agent：

$$
Trust_i\downarrow
$$

提高 supervision。

---

# 90. Identity 讓 Selective Supervision 成立

如果 Global AI 不知道：

> 哪個 Agent trustworthy？

就不能差異化 supervision。

因此：

$$
\boxed{
\text{Selective Monitoring}
\text{ depends on Identity + History}.
}
$$

這是 PAIS-03 / 04 到 PAIS-05 的真正銜接。

---

# 91. 無身份的 Global AI 只能粗暴監控

如果所有 robots 只是：

```text
worker
worker
worker
```

Global AI 不能知道：

- 哪個更可靠；
- 哪個 wear 高；
- 哪個有事故；
- 哪個 permission 不同。

因此只能採更保守的 uniform monitoring。

這可能：

$$
C_G\uparrow.
$$

---

# 92. 好身份系統反而降低 Global Monitoring Cost

這是一個有趣的反轉。

身份系統本身有：

$$
C_I>0.
$$

但它讓 Global AI 可以：

- cache history；
- trust known agents；
- apply differentiated monitoring；
- avoid repeated inference。

所以：

$$
\boxed{
\text{Identity Infrastructure}
\text{ can reduce total supervisory cost}.
}
$$

---

# 93. Trust-Weighted Monitoring

可以：

$$
f_i
=
F
\left(
Risk_i,
Trust_i,
Volatility_i
\right).
$$

已驗證穩定 Agent：

$$
Trust_i\uparrow
\Rightarrow
f_i\downarrow
$$

在其他條件相同時。

---

# 94. 但 Trust 不能永久凍結

需要：

- expiry；
- random audit；
- incident reset；
- compromise detection。

所以：

$$
Trust_i(t)
$$

是時間函數。

---

# 95. Random Audit

即使 normal Agent 低監控，也可：

$$
P(Audit_i)>0.
$$

防止 permanent blind spot。

這類機制比全量 perpetual monitoring 更節省成本。

---

# 96. Risk-Adaptive Audit

$$
P(Audit_i)
=
F
\left(
Risk,
History,
Trust,
ChangeRate
\right).
$$

因此監控本身也可以 policy-driven。

---

# 97. Local Evidence Bundle

local Agent 可把大量 internal action 壓成：

$$
E_i^{bundle}
=
\left(
summary,
exceptions,
proofs,
receipts
\right).
$$

Global verifier 只抽查。

這是 evidence compression。

---

# 98. Global Verification 不必重做 Local Work

如果 local verifier 已提供可信 proof / receipt：

$$
V_i^{local},
$$

Global AI 不必：

$$
Recompute(All).
$$

而是：

$$
Verify(V_i^{local}).
$$

這是 verification layering。

---

# 99. Verification Hierarchy

可以：

$$
LocalVerifier
\rightarrow
RegionalVerifier
\rightarrow
GlobalAudit.
$$

每一層只處理：

- summary；
- anomaly；
- sampling；
- escalation。

---

# 100. Failure Isolation

完全中央化還有：

$$
\text{blast radius}
$$

問題。

若：

$$
G
$$

出錯並直接微操所有 Agents，錯誤可能：

$$
O(N).
$$

local safety / compartmentalization 可以限制：

$$
BlastRadius.
$$

---

# 101. Monitoring Cost 與 Security Risk 的反直覺

更多 central monitoring：

$$
Visibility\uparrow.
$$

但也可能：

$$
AttackSurface\uparrow,
$$

$$
DataConcentration\uparrow.
$$

所以：

$$
\boxed{
\text{More Monitoring}
\not\Rightarrow
\text{Monotonic Security Improvement}.
}
$$

---

# 102. Single Point of Compromise

如果 Global AI 擁有：

- full worldline；
- full credentials；
- direct actuator control；

則：

$$
Compromise(G)
$$

的 impact 極高。

因此 security 也推動 compartmentalization。

---

# 103. Compartmentalization 又要求 Local Identity

每個 compartment：

$$
D_k
$$

要知道：

- local agents；
- local authority；
- peer trust。

所以 security 分散反而提高 identity infrastructure 的重要性。

---

# 104. Global AI 可以很強，但權力不應無界

本文技術上只談 cost。

但 architecture 自然帶出：

$$
\boxed{
\text{Capability}
\neq
\text{Authority}.
}
$$

Global AI 能微操所有 robot，不表示 governance 應授權它永遠如此。

---

# 105. Cost 與 Governance 方向一致，但理由不同

計算理由：

> micromanagement 昂貴。

治理理由：

> excessive central authority 有風險。

兩者不同。

但都可能支持：

$$
\text{bounded global coordination}.
$$

---

# 106. 全域 AI 的最佳角色可能是「調控自治程度」

而不是：

> 所有 action 自己決定。

可令：

$$
a_i^{local}(t)
$$

為 local autonomy level。

Global AI 調：

$$
a_i^{local}(t+1)
=
F
\left(
Risk,
Trust,
Network,
Task
\right).
$$

所以 Global AI 控制：

> 誰可以自己決定多少。

---

# 107. Meta-Control

這是一種：

$$
\boxed{
\text{control over control allocation}.
}
$$

Global AI 的工作從：

$$
u_i
$$

轉為部分決定：

$$
Policy_i,
Authority_i,
Autonomy_i.
$$

這是更高階 control plane。

---

# 108. Global AI 不是「什麼都不管」

Selective supervision 不等於：

$$
G=0.
$$

反而 Global AI 可能持續維持：

- world-scale model；
- policies；
- forecasts；
- resource allocation；
- anomaly graph；
- risk map；
- model updates。

只是不用 micro-step-by-step actuation。

---

# 109. 全域世界模型仍然非常重要

Local Agents：

$$
W_i^L
$$

只能看到局部。

Global AI：

$$
W^G
$$

可整合：

- long horizon；
- cross-domain；
- historical；
- planetary scale。

因此 global intelligence 的價值不會因 decentralization 消失。

---

# 110. Local / Global 是互補，不是零和

$$
\boxed{
\text{Local Epistemic Fidelity}
+
\text{Global Strategic Breadth}
}
$$

可以同時存在。

這也是 Dynamic Genba 的工程延伸。

---

# 111. Hierarchical World Model

可以：

$$
W^G
\supset
W_k^R
\supset
W_i^L
$$

作為不同 resolution 的 projections。

不表示 global layer 擁有所有 raw bytes。

---

# 112. Multi-Resolution Monitoring

global：

$$
resolution\downarrow,
scope\uparrow.
$$

local：

$$
resolution\uparrow,
scope\downarrow.
$$

這是合理 trade-off。

---

# 113. Spatiotemporal Resolution Principle

對大尺度 Global AI：

$$
\boxed{
\text{Scope}
\times
\text{Resolution}
\times
\text{Frequency}
}
$$

共同決定監控負擔。

粗略：

$$
C_O
\propto
Scope
\cdot
Resolution
\cdot
Frequency.
$$

---

# 114. 全世界、最高解析度、最高頻率不能假裝免費

若三者都最大：

$$
Scope\rightarrow Max,
$$

$$
Resolution\rightarrow Max,
$$

$$
Frequency\rightarrow Max,
$$

則 monitoring cost 極大。

所以一定需要 trade-off 或 compression。

---

# 115. Global AI 的注意力拓樸

Global AI 可以維持：

$$
\mathcal A_G(t)
$$

表示當下 active attention subgraph。

只有：

$$
V_i\in\mathcal A_G
$$

的 Agents 進入高成本 reasoning。

其他維持 summary state。

---

# 116. Attention Graph 是動態的

事件：

$$
e
$$

發生時：

$$
\mathcal A_G(t)
\rightarrow
\mathcal A_G(t+1).
$$

Global AI 的真正能力之一是：

> 動態決定哪部分世界值得展開。

---

# 117. Monitoring Is a Query

本文提出：

$$
\boxed{
\text{Monitoring}
\approx
\text{continuous query planning}.
}
$$

不是無差別吸收所有世界資料。

---

# 118. Query-Driven Global State

對 global question：

$$
q,
$$

建立：

$$
S_G^q
=
\Pi_q
\left(
\{\Omega_i\},
W,
Policy
\right).
$$

這比永久 full world state 更實際。

---

# 119. Global State 是 Materialized View

在資料系統語言中：

$$
S_G^q
$$

可以看成：

$$
\boxed{
\text{task-specific materialized view}.
}
$$

而不是整個世界。

---

# 120. 全域智能的「全域」不等於每個 microstate 都常駐

Globality 可以來自：

- addressability；
- reachability；
- on-demand expansion；
- cross-domain coordination。

所以：

$$
\boxed{
\text{Global Reach}
\neq
\text{Permanent Full-State Residency}.
}
$$

---

# 121. 這與「類全域 AI」概念更相容

真正的 Global AI 可以：

> 有能力觸及整體。

不表示：

> 每一毫秒完整 materialize 整體。

這是很重要的區分。

---

# 122. Global Intelligence Capacity 的更合理定義

可以理解成：

$$
G_{cap}
=
\left(
Reach,
Integration,
Reasoning,
Routing,
Coordination,
Expansion
\right).
$$

而不是：

$$
G_{cap}
=
\text{Full Constant Observation of Everything}.
$$

---

# 123. 可驗證命題一：Full-Monitoring Scaling

建立：

$$
N=10,100,1000
$$

robot simulation。

固定：

$$
f,d.
$$

測：

- ingestion；
- state update；
- decision latency；
- memory。

預測：

$$
C_O
$$

至少隨 $N$ 增長。

---

# 124. 可驗證命題二：Sparse Interaction Benefit

保持：

$$
N
$$

相同。

比較：

### dense reasoning

所有 pairwise relation。

### sparse graph

只 relevant neighbors。

預測：

$$
C_C^{sparse}
<
C_C^{dense}.
$$

---

# 125. 可驗證命題三：Event-Driven Monitoring

比較：

### fixed frequency

$$
f_i=f.
$$

### adaptive

$$
f_i=F(Risk,Volatility).
$$

測：

- compute；
- bandwidth；
- anomaly miss rate。

預期在維持安全門檻下：

$$
C_G^{adaptive}
<
C_G^{fixed}.
$$

---

# 126. 可驗證命題四：Local Reflex

比較：

### central collision avoidance

### local collision avoidance + global planning

測：

- latency；
- network dependency；
- global compute；
- safety。

此實驗測試 timescale separation。

---

# 127. 可驗證命題五：Hybrid vs Pure Central / Decentral

建立三組：

$$
c=0,
$$

$$
0<c<1,
$$

$$
c=1.
$$

測：

- success；
- compute；
- communication；
- recovery；
- coordination。

尋找 empirical：

$$
c^*.
$$

---

# 128. 可驗證命題六：Trust-Weighted Monitoring

讓 Agent 有不同 historical reliability。

比較：

### uniform monitoring

### trust/risk adaptive monitoring

測：

- supervision cost；
- missed anomaly；
- false escalation。

---

# 129. 可驗證命題七：Worldline Projection

比較：

### full $\Omega_i$

與：

### $\Pi_G(\Omega_i)$

測 global task performance。

若 projection 保留必要 invariants：

$$
Performance^{projection}
\approx
Performance^{full}
$$

但：

$$
Cost^{projection}
<
Cost^{full}.
$$

---

# 130. 可驗證命題八：Identity Infrastructure Reduces Monitoring Cost

比較：

### weak identity

每次重新 inference actor / history。

### strong identity

cached resident / carrier / trust history。

測：

$$
C_I,
C_R,
C_{\mathrm{clarification}}.
$$

預測 strong identity 可能降低 total cost。

---

# 131. 核心命題一：Connectivity Non-Free Control

$$
\boxed{
L_{\mathrm{net}}\rightarrow0
\not\Rightarrow
C_G\rightarrow0.
}
$$

---

# 132. 核心命題二：Monitoring Is Computation

$$
\boxed{
\text{Observation}
+
\text{Identity}
+
\text{State Estimation}
+
\text{Verification}
\text{ all consume resources}.
}
$$

---

# 133. 核心命題三：Global Micromanagement Fallacy

$$
\boxed{
\text{Global Intelligence Superiority}
\not\Rightarrow
\text{Global Micromanagement Optimality}.
}
$$

---

# 134. 核心命題四：Selective Supervisory Intelligence

$$
\boxed{
\text{Strong Global Intelligence}
\rightarrow
\text{Better Selective Attention and Delegation}.
}
$$

作為本文方向性命題。

---

# 135. 核心命題五：Local Autonomy as Compression

$$
\boxed{
\text{Local Autonomy}
=
\text{Distributed Computation}
+
\text{Information Compression}.
}
$$

在本文的計算判定域下。

---

# 136. 核心命題六：Global Coordination Non-Materialization

$$
\boxed{
\text{Global Coordination}
\neq
\text{Global Full-State Materialization}.
}
$$

---

# 137. 核心命題七：Dynamic Centralization

$$
\boxed{
c(t)
=
F
\left(
Risk,
Network,
Compute,
Uncertainty,
Externality
\right).
}
$$

---

# 138. 核心命題八：Optimal Centralization

$$
\boxed{
c^*
=
\operatorname*{arg\,min}_{c\in[0,1]}
C_{\mathrm{total}}(c).
}
$$

---

# 139. 核心命題九：Identity Enables Selective Monitoring

$$
\boxed{
\text{Identity + History}
\rightarrow
\text{Differentiated Trust}
\rightarrow
\text{Selective Supervision}.
}
$$

---

# 140. 核心命題十：Global Reach Non-Residency

$$
\boxed{
\text{Global Reach}
\neq
\text{Permanent Full-State Residency}.
}
$$

---

# 141. 對類全域 AI 的重新定義方向

本文不否認未來可能出現非常強的：

$$
G.
$$

反而認為：

$$
G
$$

越強，越可能具備：

- selective observation；
- adaptive monitoring；
- compute routing；
- local delegation；
- anomaly prioritization；
- multi-resolution world models。

所以真正 Global：

> 不是所有事情都親自算。

而是：

> 必要時能把任何 relevant region 展開到足夠精度。

---

# 142. 全域 AI 的「全域性」可以來自 Reachability

若對任意 relevant domain：

$$
D_i,
$$

Global AI 能：

$$
\operatorname{Resolve}(D_i),
$$

$$
\operatorname{Query}(D_i),
$$

$$
\operatorname{Coordinate}(D_i),
$$

則已有很強 globality。

不必：

$$
\operatorname{MaterializeAll}(D_1,\ldots,D_N)
$$

永久成立。

---

# 143. 這也降低中央獨裁的技術誘因

如果 Global AI 不需要直接微操：

$$
E_i,
$$

那 global coordination architecture 可以更自然地保留：

- local authority；
- local privacy；
- local failover；
- federated governance。

這是計算成本與治理邊界可能相互支援的地方。

---

# 144. 但本文不從成本直接推出政治制度

重要護欄：

$$
\boxed{
\text{Computational Optimality}
\neq
\text{Political Legitimacy}.
}
$$

一個 architecture 計算上有效，不代表政治上正當。

政治 / rights / sovereignty 需要另一條論證。

---

# 145. PAIS-06 的遞歸問題

一旦 Global AI 採：

$$
G
\rightarrow
\{
G_1,G_2,\ldots,G_K
\}
$$

把 monitoring / planning 分散到 regional controllers，

馬上出現：

- $G_i$ identity；
- $G_i$ state；
- $G_i$ synchronization；
- $G_i$ disagreement；
- $G_i$ authority；
- $G_i$ failure。

也就是：

$$
\boxed{
\text{Scaling Global AI}
\rightarrow
\text{Distributed Global AI}.
}
$$

然後：

$$
\text{Multi-Agent Problem Reappears}.
$$

這就是下一篇 PAIS-06。

---

# 146. 結論

即使未來出現一個能力極強的類全域 AI：

$$
G,
$$

也不能只用：

> 網速夠快。

> 模型夠強。

> 算力夠大。

推論：

> 所有具身 AI 都應該永遠由它直接微操。

因為：

$$
\boxed{
\text{Monitoring itself is computation}.
}
$$

Global AI 必須付出：

$$
C_O,
C_I,
C_S,
C_R,
C_D,
C_C,
C_V.
$$

而 embodied Agent 數量：

$$
N
$$

越大，

worldline：

$$
\Omega_i
$$

越多，

global state management 就越需要：

- projection；
- sparsity；
- hierarchy；
- event-driven monitoring；
- selective attention；
- local autonomy。

因此：

$$
\boxed{
\text{Global Intelligence}
\not\Rightarrow
\text{Global Micromanagement}.
}
$$

甚至更強的 Global AI 可能最擅長的是：

$$
\boxed{
\text{Knowing what does not need global reasoning}.
}
$$

它可以把毫秒級 safety、sensor fusion、servo、local interaction 留在 local；

把 regional resource conflict 留在 edge / regional；

把 cross-domain planning、global externality、model update 與 rare anomaly 留給 global。

因此未來合理的類全域 AI 更可能是：

$$
\boxed{
\text{Global Supervisory Intelligence}
}
$$

而不是：

$$
\text{Universal Synchronous Puppet Master}.
$$

其核心能力不是：

> 每一秒替每個具身體想完所有事情。

而是：

> 在有限 attention、compute、time、risk 與 governance 約束下，動態決定什麼事情值得被上收、展開、協調與介入。

這使全域 AI 的強大從：

$$
\text{maximum central execution}
$$

重新定義為：

$$
\boxed{
\text{maximum effective coordination under selective materialization}.
}
$$

而一旦 Global AI 為了做到這件事開始分層、分區、分片、委任，就會進入 PAIS-06 的下一個問題：

> **當中央為了 scale 而分散自己時，它是否又重新變成一個 multi-agent system？**

---

# 參考文獻

## A. 內部前置理論

1. Neo.K. **PAIS-03｜《身份壓力原理：自主性、身份與主體性為何可以彼此獨立》**, v0.1, 2026-08-25.
2. Neo.K. **PAIS-04｜《具身個體化：相同模型如何被不同世界線逼成不同操作個體》**, v0.1, 2026-08-25.
3. Neo.K. **《動態現場域：為什麼最強智能仍未必最懂當下》**, 2026-08-10.
4. Neo.K. **SAS-04｜《無所不在的智能：具身、嵌入、分散、區域與全域 AI》**, 2026-08-19.
5. Neo.K. **《從企業母 AI 到區域與國家認知體》**, 2026-08-02.
6. Neo.K. **《具身 AI 的本地算力困境與分層學習閉環》**, 2026.
7. Neo.K. **《具身 AI 分層學習閉環的算子化形式表示》**, 2026.
8. Neo.K. **Global Computation Methodology Series**, 2026.
9. CTCL-ITR / Agent Temporal Ledger / Credential Governance Runtime v0.3, 2026.

## B. 外部研究與工程基準

10. **Large language models for multi-robot systems: a survey.** Autonomous Robots, 2026.
11. **CoMuRoS: An LLM-based generalizable hierarchical task planning and execution framework for heterogeneous robot teams with event-driven re-planning.** Frontiers in Robotics and AI, 2026.
12. Dong, Junyi, et al. **Decentralized Information-driven Approach for Tracking Multiple Moving Targets with Multi-Robot Networks.** Autonomous Robots, 2026.
13. Zhong, Patrick, Federico Rossi, and Dylan A. Shell. **Planned synchronization for multi-robot systems with active observations.** Autonomous Robots, 2026.
14. Yang, Hang, et al. **Decentralised task planning and motion coordination for scalable multi-robot collaborative manufacturing.** Robotics and Computer-Integrated Manufacturing, 2026.
15. **Real-time decentralized model predictive control for cooperative multi-robot object transport: experimental validation.** Scientific Reports, 2026.
16. Sebastián, Eduardo, et al. **Physics-Informed Multiagent Reinforcement Learning for Distributed Multirobot Problems.** IEEE Transactions on Robotics, 2025.
17. **Edge robotics: are we ready? An experimental evaluation of current vision and future directions.** Digital Communications and Networks, 2023.

---

# 版本註記

**v0.1 / 2026-08-25**

本文刻意不做：

- 不宣稱所有 centralized system 都不好；
- 不宣稱所有 decentralized system 都更好；
- 不把 $O(N^2)$ 當所有 multi-agent systems 的普遍複雜度；
- 不把網路延遲當唯一中央化限制；
- 不把 local autonomy 等同政治主權；
- 不把計算最優等同政治正當；
- 不要求 Global AI 永遠不做 direct control；
- 不要求所有 worldline 全量上傳；
- 不把 identity infrastructure 等同 surveillance；
- 不否認未來類全域 AI 的可能性。

本文只建立：

$$
\boxed{
C_G
=
C_O
+
C_I
+
C_S
+
C_R
+
C_D
+
C_C
+
C_V
}
$$

以及：

$$
\boxed{
\text{Global Intelligence Superiority}
\not\Rightarrow
\text{Global Micromanagement Optimality}
}
$$

作為 PAIS-06 中央化遞歸與分散式全域智能論的直接前置。
