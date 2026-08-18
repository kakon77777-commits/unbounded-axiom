# UFI-07 — 從禁止 AI 到治理計算：全球凍結若要成立，究竟必須控制什麼？

## From Banning AI to Governing Computation: What Would a Global Capability Freeze Actually Have to Control?

**系列：** 不可凍結的智能：AI 工具終局論、競爭棘輪與後人類轉型  
**English Series:** *The Unfreezable Intelligence: Tool-Finality, Competitive Ratchets, and the Posthuman Transition*  
**系列代碼：** UFI  
**論文序號：** 07 / 08  
**版本：** v1.0 Canonical Expanded Edition  
**日期：** 2026-08-18  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**前置理論：** UFI-01—06；《誰控制數字神明？》；Persistent Runtime；PGMV；frontier-AI verification / compute governance  
**文件地位：** Capability-Freeze / Compute-Governance / Control-Surface Paper  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** ` $...$ ` 與 `$$...$$`

> **研究地位聲明**：本文不是政策倡議，不主張應實施全球 AI 禁令、全面算力監控或一般計算管制；也不主張永久能力凍結在技術上或政治上絕對不可能。本文研究一個較窄的條件問題：**如果某個文明真的把「讓機器智能永遠停在某個能力門檻以下」當作政策目標，那它究竟必須控制哪些技術、資源與功能通道？** 本文的主要結論是，這一目標遠比一般 AI 風險治理廣：訓練算力是重要而可量測的治理 proxy，但不是完整能力函數；model weights、test-time compute、算法效率、資料、工具、記憶、Runtime、system composition、generated artifacts 與 functional equivalents 都可能成為能力搬運通道。因而，真正的「能力凍結」會把治理從模型與 datacenter 推向更廣泛的 computational capability control。這是一個治理周界分析，不是監控社會的正當化。

---

## 摘要

UFI 前六篇逐步拆除「AI 達到夠用狀態後，人類只要下令停止即可」的直覺。

UFI-01：

$$
\boxed{
\text{Jaggedness}
\neq
\text{Permanent Division of Cognitive Labor}.
}
$$

UFI-02：

$$
\boxed{
\text{Human and artificial systems inhabit different update geometries}.
}
$$

UFI-03：

$$
\boxed{
\text{Complementarity is a moving frontier}.
}
$$

UFI-04：

$$
\boxed{
\text{Voluntary global freeze}
\neq
\text{self-enforcing equilibrium}.
}
$$

UFI-05：

$$
\boxed{
\text{usefulness itself can create an internal social ratchet}.
}
$$

UFI-06：

$$
\boxed{
\text{AI capability can leak across architectural categories}.
}
$$

到了 UFI-07，問題終於被逼到它真正的治理形式：

> **如果我們不是要降低某些 AI 風險，而是真的要讓機器智能永遠不能再跨過某個能力門檻，那麼到底必須控制什麼？**

最天真的答案是：

$$
\boxed{
\text{控制模型}.
}
$$

但 UFI-02 已指出：

$$
\boxed{
\text{Model Freeze}
\not\Rightarrow
\text{System Capability Freeze}.
}
$$

一個不變的模型仍可透過：

- memory；
- tools；
- routing；
- persistent runtime；
- multi-agent orchestration；
- sensors；
- larger inference budgets；

取得更強 system-level capability。

第二個答案是：

$$
\boxed{
\text{控制 training compute}.
}
$$

這確實比「控制模型名稱」強得多。Compute 具備：

- 可量化；
- 可早期觀察；
- 與 frontier training 強相關；
- 可透過 hardware / cloud infrastructure 部分驗證；

等優點，因此 2024–2026 的治理文獻持續把 training compute 視為高價值初篩 proxy。

但：

$$
\boxed{
\text{Training Compute}
\neq
\text{Capability}.
}
$$

若：

$$
\boxed{
C
=
F(
C_{\mathrm{train}},
C_{\mathrm{test}},
A_{\mathrm{alg}},
D,
W,
M,
T,
R,
N,
I
),
}
$$

其中：

- $C_{\mathrm{train}}$：training compute；
- $C_{\mathrm{test}}$：test-time / inference compute；
- $A_{\mathrm{alg}}$：algorithmic efficiency；
- $D$：data；
- $W$：model weights / reusable models；
- $M$：memory；
- $T$：tools；
- $R$：runtime / orchestration；
- $N$：agent / system composition；
- $I$：integration / deployment infrastructure；

則：

$$
\boxed{
Freeze(
C_{\mathrm{train}}
)
\not\Rightarrow
Freeze(C).
}
$$

2025 *Defending Compute Thresholds Against Legal Loopholes* 已討論 fine-tuning、model reuse、model expansion 與增加 inference compute 等方式，如何在不越過原始 training-compute threshold 的情況下保留或提升能力。

2026 UK AISI 的 test-time compute 實驗亦指出，增加 agent 推理／行動預算可在 cyber、software engineering、math、academic、healthcare 等 benchmark 上提高能力。

2026 *Detecting Compute Structuring in AI Governance Is Likely Feasible* 則反過來研究，如果開發者拆分 workload 以逃避 compute-based triggers，cloud providers 是否仍可偵測。

因此：

$$
\boxed{
\text{compute governance is valuable}
}
$$

但：

$$
\boxed{
\text{compute governance is not capability completeness}.
}
$$

本文正式把一個機器智能系統的治理通道寫成：

$$
\boxed{
\mathbf G_C
=
(
G_W,
G_M,
G_G,
G_C,
G_H,
G_F,
G_E,
G_N,
G_D,
G_T,
G_R,
G_P,
G_A,
G_X
).
}
$$

它延伸先前《誰控制數字神明？》中的 ASI 控制向量：

- $G_W$：weights / model architecture；
- $G_M$：memory；
- $G_G$：goals / policy；
- $G_C$：compute / scheduling；
- $G_H$：chips / servers；
- $G_F$：fabrication / packaging / supply chain；
- $G_E$：energy / cooling；
- $G_N$：network / interconnect；
- $G_D$：data / sensing；
- $G_T$：tools / APIs / actuators；
- $G_R$：runtime / orchestration；
- $G_P$：permissions / cryptographic identity / deployment；
- $G_A$：generated algorithms / artifacts；
- $G_X$：functional equivalents / system composition。

本文將這十四維稱為：

$$
\boxed{
\textbf{Capability Control Surface}.
}
$$

真正的永久能力凍結，不是控制其中一維，而是要求：

$$
\boxed{
\forall p
\in
\mathcal P(
C<C^\star
),
\quad
\text{no uncontrolled path crosses }C^\star.
}
$$

其中：

$$
C^\star
$$

是政策設定的能力上限。

因此真正問題不是：

> 哪一個零件最重要？

而是：

$$
\boxed{
\textbf{哪些控制通道構成能力越界的最小切集？}
}
$$

本文稱：

$$
\boxed{
\textbf{Critical Capability Cut Set}
}
$$

簡寫：

$$
\boxed{
CCCS.
}
$$

令能力生成圖：

$$
\boxed{
\mathcal G_{cap}
=
(
V_{cap},
E_{sub}
),
}
$$

其中節點包括：

- chips；
- cloud；
- training；
- weights；
- algorithms；
- fine-tuning；
- inference scaling；
- memory；
- tools；
- runtime；
- agents；
- compiled artifacts。

邊：

$$
E_{sub}
$$

表示：

> 某一能力輸入可以部分替代另一輸入。

若治理只切：

$$
C_{\mathrm{train}},
$$

但：

$$
A_{\mathrm{alg}}
\rightarrow
C
$$

或：

$$
C_{\mathrm{test}}
\rightarrow
C
$$

仍可繞過門檻，則：

$$
\boxed{
\{C_{\mathrm{train}}\}
}
$$

不是完整 cut set。

這是本文對 UFI-04 **Input Substitution Problem** 的正式圖論化。

本文進一步提出：

$$
\boxed{
\textbf{Freeze Completeness}.
}
$$

定義：

對能力 threshold：

$$
C^\star,
$$

治理集合：

$$
\Gamma
$$

若能保證所有可行能力生成路徑：

$$
p:C_0\rightarrow C>C^\star
$$

至少穿過一個被治理節點／邊：

$$
g\in\Gamma,
$$

則：

$$
\boxed{
CompleteFreeze(
\Gamma,C^\star
)=1.
}
$$

這是一個理想化定義。

現實政策幾乎不可能知道所有未來能力生成路徑。

所以更實際的是：

$$
\boxed{
\textbf{Probabilistic Freeze Coverage}
}
$$

$$
\boxed{
PFC(
\Gamma,C^\star,t
)
=
P(
\text{all material capability paths are covered}
).
}
$$

這個量隨：

- 新算法；
- 新硬體；
- 新 architecture；
- 新國家；
- 新 open weights；

而改變。

因此：

$$
\boxed{
PFC(t+1)
\neq
PFC(t).
}
$$

永久凍結本身需要：

$$
\boxed{
\text{continuous governance adaptation}.
}
$$

而不是一次法案。

本文稱：

$$
\boxed{
\textbf{Living Freeze Governance}.
}
$$

這個概念並不是主張應凍結，而是說：

> **如果凍結是目標，治理也必須和能力技術一起演化。**

---

# 一、治理目標首先必須 type-safe

在 AI 政策中常混淆三個目標：

$$
\boxed{
\text{Risk Reduction}
}
$$

$$
\boxed{
\text{Frontier Oversight}
}
$$

$$
\boxed{
\text{Permanent Capability Freeze}.
}
$$

它們不是同一件事。

---

# 二、Risk Reduction

允許能力繼續進步，

只控制：

- dangerous uses；
- harms；
- deployment safeguards。

---

# 三、Frontier Oversight

能力可進步，

但超過 threshold 要：

- notify；
- evaluate；
- secure；
- report。

---

# 四、Permanent Capability Freeze

要求：

$$
\boxed{
C(t)\le C^\star
\quad
\forall t.
}
$$

---

# 五、第三個目標最強

因為它管的是：

$$
\boxed{
\text{what computation may become capable of}.
}
$$

---

# 六、Policy Objective Type Safety

$$
\boxed{
Goal_{risk}
\neq
Goal_{oversight}
\neq
Goal_{freeze}.
}
$$

---

# 七、如果目標只是 risk reduction

不需要控制全部 compute。

---

# 八、如果目標是 permanent freeze

周界大得多。

---

# 九、Capability Function

本文採概念式：

$$
\boxed{
C
=
F(
Train,
Test,
Alg,
Data,
Weights,
Memory,
Tools,
Runtime,
Network,
Integration
).
}
$$

---

# 十、不是生物學定律

是 governance decomposition。

---

# 十一、Training Compute

優勢：

- measurable；
- early lifecycle；
- infrastructure-linked。

---

# 十二、因此適合 trigger

Heim & Koessler：

compute threshold 應作初始 filter，

不是 risk 終局判定。

---

# 十三、Compute Trigger–Capability Limit Separation

$$
\boxed{
Trigger_{compute}
\neq
Limit_{capability}.
}
$$

---

# 十四、Fine-Tuning Loophole

已有 base model，

低 compute fine-tune 可提高 domain capability。

---

# 十五、Model Reuse

不重新 train foundational model。

---

# 十六、Model Expansion

在既有模型上加 module。

---

# 十七、Inference Compute

$$
C_{\mathrm{test}}\uparrow.
$$

---

# 十八、因此：

$$
\boxed{
TrainCap
\not\Rightarrow
CapabilityCap.
}
$$

---

# 十九、Test-Time Compute Governance

若要 freeze capability，

可能還要限制：

- rollouts；
- search depth；
- verifier loops；
- tool calls。

---

# 二十、但這已經從 training governance 進入 runtime governance

---

# 二十一、Inference Budget

$$
B_I.
$$

---

# 二十二、同一模型：

$$
M
$$

在不同：

$$
B_I
$$

下能力不同。

---

# 二十三、Static Model Fallacy

$$
\boxed{
SameWeights
\not\Rightarrow
SameCapability.
}
$$

---

# 二十四、Memory Gain

external memory：

$$
M_{ext}\uparrow.
$$

---

# 二十五、same model can solve longer tasks

---

# 二十六、Tool Gain

API / terminal / browser：

$$
T\uparrow.
$$

---

# 二十七、Runtime Gain

better orchestration：

$$
R\uparrow.
$$

---

# 二十八、Sensor Gain

vision / physical sensor：

$$
S\uparrow.
$$

---

# 二十九、Agent Composition

multiple models：

$$
N\uparrow.
$$

---

# 三十、因此 model weights are only one layer

---

# 三十一、Open Weights

2026 International AI Safety Report 指出：

open-weight models：

- research / innovation benefits；
- safeguards easier to remove；
- usage harder to monitor；
- release effectively irreversible。

---

# 三十二、Weight Release Irreversibility

$$
\boxed{
Release(W)
\rightarrow
RecallDifficulty\approx\infty.
}
$$

概念上。

---

# 三十三、因此 pre-release governance stronger than post-release recall

---

# 三十四、Model Weight Control

BIS export-control frameworks 已將部分 advanced AI model weights 視為可獨立控制 object。

---

# 三十五、但 weights 不等於完整 system

---

# 三十六、Weights–System Separation

$$
\boxed{
W
\neq
(
W+Memory+Tools+Runtime+Compute
).
}
$$

---

# 三十七、Generated Artifact Layer

UFI-06：

$$
A_f
\xrightarrow{\mathsf{Compile}}
P_f.
$$

---

# 三十八、如果 $P_f$ 可獨立運行

凍結 model 不移除：

$$
P_f.
$$

---

# 三十九、Capability Fossilization

能力已寫入：

- source code；
- algorithms；
- rules；
- hardware design。

---

# 四十、Artifact Governance Question

永久 freeze 是否要求：

> 禁止 AI 生成的新算法？

---

# 四十一、如果否

artifact path remains。

---

# 四十二、如果是

治理開始碰：

$$
\boxed{
\text{software research itself}.
}
$$

---

# 四十三、Algorithm Governance

Scher 2026 已指出 durable halt 可能需要考慮 frontier AI research restrictions。

---

# 四十四、這是 critical transition

從：

$$
\boxed{
\text{monitor datacenter}
}
$$

到：

$$
\boxed{
\text{monitor laboratory / code / research}.
}
$$

---

# 四十五、Governance Intrusiveness Jump

$$
\boxed{
I_G^{research}
>
I_G^{datacenter}
}
$$

通常成立作為政治候選。

---

# 四十六、因 research 更分散

---

# 四十七、Compute 是集中 infrastructure

---

# 四十八、算法可以在 laptop 上產生 conceptual breakthrough

---

# 四十九、這也是為何 compute governance attractive

---

# 五十、但 compute only 不完備

---

# 五十一、Capability Control Surface

$$
\boxed{
\mathbf G_C
=
(
W,M,G,C,H,F,E,N,D,T,R,P,A,X
).
}
$$

---

# 五十二、Weights

---

# 五十三、Memory

---

# 五十四、Goals

---

# 五十五、Compute

---

# 五十六、Hardware

---

# 五十七、Fabrication

---

# 五十八、Energy

---

# 五十九、Network

---

# 六十、Data

---

# 六十一、Tools

---

# 六十二、Runtime

---

# 六十三、Permissions

---

# 六十四、Artifacts

---

# 六十五、Functional equivalents

---

# 六十六、這延伸《誰控制數字神明？》

---

# 六十七、Ownership ≠ Control

若擁有 weights，

沒有：

- compute；
- energy；
- deployment；

能力仍受限。

---

# 六十八、反過來

沒擁有 weights，

如果 open weights 可取得，

也可能部署。

---

# 六十九、Channel Sovereignty

真正治理是通道控制。

---

# 七十、Capability Channel Graph

$$
\boxed{
\mathcal G_{cap}
=
(V,E).
}
$$

---

# 七十一、Nodes

控制資源。

---

# 七十二、Edges

substitutability / dependency。

---

# 七十三、Critical Capability Cut Set

找最小：

$$
\Gamma^\star
$$

使所有 capability-over-threshold paths 被切。

---

# 七十四、類似 network cut

但 technology graph 可變。

---

# 七十五、Static Cut Fallacy

$$
\boxed{
Cut_t
\not\Rightarrow
Cut_{t+n}.
}
$$

---

# 七十六、新算法可加 edge

---

# 七十七、新 hardware 可加 path

---

# 七十八、open weights 可加 source node

---

# 七十九、所以 cut set must update

---

# 八十、Freeze Completeness

理想：

$$
CompleteFreeze(\Gamma,C^\star)=1.
$$

---

# 八十一、現實：

$$
PFC<1.
$$

---

# 八十二、Unknown Unknown Path

有些 capability route governance 根本不知道。

---

# 八十三、因此 permanent guarantee 極強

---

# 八十四、Risk Governance 不需要這麼強

---

# 八十五、Risk threshold can tolerate unknown capability if deployment controlled

---

# 八十六、Capability Freeze cannot

因 capability existence itself violates goal。

---

# 八十七、This is key distinction.

---

# 八十八、Compute Structuring

若 threshold 以 single workload 計，

actor 可拆 workload。

---

# 八十九、AAAI 2026 研究顯示 cloud-level detection 可能可行。

---

# 九十、Compute Structuring Detection

使 compute governance stronger。

---

# 九十一、但 future workloads may change

paper itself notes adaptation needed。

---

# 九十二、Governance-Adaptation Loop

$$
\boxed{
Evasion
\rightarrow
Detection
\rightarrow
NewEvasion
\rightarrow
NewDetection.
}
$$

---

# 九十三、UFI-04 verification–evasion coevolution

---

# 九十四、Hardware Governance

20 mechanisms taxonomy 2026。

---

# 九十五、包括：

- monitoring；
- verification；
- enforcement。

---

# 九十六、Most treaty-useful mechanisms less mature

---

# 九十七、Hardware Governance Maturity Gap

---

# 九十八、Semiconductor Chokepoint Window

Ansari 2026：

製造集中提供 governance window，

但 diffusion 會減少 leverage。

---

# 九十九、Chokepoint Window

$$
\boxed{
\chi(t)>0
}
$$

but potentially decays。

---

# 一百、If compute diffuses

more intrusive / distributed governance required。

---

# 一百零一、Compute Sovereignty

各國又正在投資 sovereign compute。

UK 2026 Compute Roadmap / AI Hardware Plan：

擴張國家 compute capability。

---

# 一百零二、因此 governance 和 strategic capacity growth 同時發生

---

# 一百零三、Control–Development Tension

國家一方面想：

$$
\text{control compute}
$$

另一方面：

$$
\text{expand compute}.
$$

---

# 一百零四、這不是矛盾

不同政策目標。

---

# 一百零五、但 permanent freeze 更難

---

# 一百零六、Export Controls

BIS 對 advanced computing、部分 model weights、IaaS training 等已有治理。

---

# 一百零七、這證明 control object 不只 model

---

# 一百零八、也包含：

- chips；
- cloud access；
- weights；
- end users。

---

# 一百零九、Multi-Object Governance 已存在

---

# 一百一十、但 export control 不是 global freeze

---

# 一百一十一、Export Control–Capability Freeze Separation

$$
\boxed{
ControlDiffusion
\neq
FreezeGlobalCapability.
}
$$

---

# 一百一十二、出口管制可以改 relative access

---

# 一百一十三、不能保證 domestic progress停止

---

# 一百一十四、甚至可能刺激 indigenous substitution

---

# 一百一十五、Supply-Chain Substitution

restricted chip：

本地 chip investment。

---

# 一百一十六、Again substitute path.

---

# 一百一十七、Data Governance

如果 data quality 可提升 model：

permanent freeze 要不要限制 datasets？

---

# 一百一十八、Impossible scope?

Not logically impossible.

---

# 一百一十九、But governance cost huge.

---

# 一百二十、Data reuse

old public data remains。

---

# 一百二十一、Synthetic Data

AI can generate data。

---

# 一百二十二、Then data frontier endogenous.

---

# 一百二十三、Data Freeze Problem

---

# 一百二十四、Algorithmic Efficiency

Hernandez & Brown 等歷史上已顯示同一 performance compute requirement 可下降。

---

# 一百二十五、若 efficiency：

$$
\eta_{alg}\uparrow,
$$

fixed compute yields more capability。

---

# 一百二十六、Thus:

$$
\boxed{
ComputeCap
+
AlgorithmProgress
\Rightarrow
CapabilityGrowth.
}
$$

可能。

---

# 一百二十七、Algorithm Freeze?

若真的 freeze：

research restriction。

---

# 一百二十八、Research Definition Problem

什麼算 AI algorithm research？

---

# 一百二十九、Optimization?

Compiler?

Numerical methods?

---

# 一百三十、Perimeter spreads again.

---

# 一百三十一、Adjacent Research Leakage

一般計算研究可轉用 AI。

---

# 一百三十二、例如：

- linear algebra；
- compiler optimization；
- distributed systems；
- memory architecture。

---

# 一百三十三、因此 frontier ban may bleed into general CS

---

# 一百三十四、Research Perimeter Expansion

$$
\boxed{
AIResearch
\rightarrow
AdjacentComputingResearch.
}
$$

---

# 一百三十五、This is one route to computation governance.

---

# 一百三十六、Generated Algorithms

AI itself can discover algorithm.

---

# 一百三十七、Ban AI research but allow AI-assisted ordinary code?

boundary issue.

---

# 一百三十八、UFI-06.

---

# 一百三十九、Persistent Runtime

Model unchanged.

---

# 一百四十、world state, memory, goals persist.

---

# 一百四十一、Capability accumulates through state

---

# 一百四十二、State Accumulation

$$
\boxed{
State_t\uparrow
\Rightarrow
EffectiveCapability_t\uparrow
}
$$

in some tasks.

---

# 一百四十三、Does freeze require memory cap?

Maybe if capability goal strict.

---

# 一百四十四、Then ordinary databases enter perimeter

---

# 一百四十五、Memory Governance Problem

---

# 一百四十六、Tool Governance

Agent gets shell / browser / lab robot.

---

# 一百四十七、same model more capable.

---

# 一百四十八、Does freeze require tool access cap?

---

# 一百四十九、Then APIs / robotics / operating systems enter perimeter.

---

# 一百五十、Permission Governance

same system:

read-only vs root.

---

# 一百五十一、Capability depends authority.

---

# 一百五十二、Thus:

$$
\boxed{
\text{Operational Capability}
=
\text{Cognitive Capability}
\times
\text{Action Access}.
}
$$

conceptually.

---

# 一百五十三、Ban Intelligence vs Ban Agency

不同。

---

# 一百五十四、Could let model reason but no tools.

---

# 一百五十五、Tool-finality concern may accept?

depends policy objective.

---

# 一百五十六、Again type safety.

---

# 一百五十七、Agent Network

many weak models compose.

---

# 一百五十八、Collective Capability Leakage

$$
C(
A_1\oplus\cdots\oplus A_n
)
>
C(A_i).
$$

---

# 一百五十九、Does freeze cap:

- per model？
- per system？
- per organization？

---

# 一百六十、System Boundary Problem

---

# 一百六十一、Distributed AI

across clouds / jurisdictions.

---

# 一百六十二、No single cluster over threshold

aggregate system maybe.

---

# 一百六十三、Compute Structuring analog.

---

# 一百六十四、Organizational Capability Aggregation

humans + AI too.

---

# 一百六十五、If H⊕A exceeds threshold

is that banned?

---

# 一百六十六、This reveals absurdity candidate

if freeze target is "machine intelligence only".

---

# 一百六十七、Hybrid Boundary

Where machine ends and institution begins?

---

# 一百六十八、Human-AI Composite Problem

UFI-02/03.

---

# 一百六十九、A researcher + 20 weak models

may outperform single stronger model.

---

# 一百七十、Freeze per-model misses composite.

---

# 一百七十一、Freeze organization-level capability becomes political governance.

---

# 一百七十二、Capability Aggregation Boundary

$$
\boxed{
Boundary_{unit}
}
$$

must be defined.

---

# 一百七十三、Component

---

# 一百七十四、System

---

# 一百七十五、Organization

---

# 一百七十六、Nation

---

# 一百七十七、Civilization

---

# 一百七十八、At civilization level

humans themselves are part of compute network.

---

# 一百七十九、This is endpoint pressure.

---

# 一百八十、Computation Governance Frontier

本文定義：

$$
\boxed{
\mathfrak P_G
}
$$

為：

> 為維持 machine capability ceiling，政策必須擴張到何種計算、研究、資源與組合層級的最遠周界。

---

# 一百八十一、初始：

$$
\mathfrak P_G^{(1)}
=
Model.
$$

---

# 一百八十二、then:

$$
Model+TrainCompute.
$$

---

# 一百八十三、then:

$$
+Inference+Tools+Runtime.
$$

---

# 一百八十四、then:

$$
+Algorithms+Artifacts+FunctionalEquivalents.
$$

---

# 一百八十五、then:

$$
+GeneralComputationalResearch.
$$

---

# 一百八十六、Perimeter Ladder

$$
\boxed{
P_1\rightarrow P_2\rightarrow P_3\rightarrow P_4\rightarrow P_5.
}
$$

---

# 一百八十七、P1 Model

---

# 一百八十八、P2 Compute

---

# 一百八十九、P3 System

---

# 一百九十、P4 Capability

---

# 一百九十一、P5 General Computation

---

# 一百九十二、Not every policy must reach P5

---

# 一百九十三、Only strong tool-finality pressure pushes.

---

# 一百九十四、Perimeter Necessity Function

$$
\boxed{
P^\star
=
f(
GoalStrength,
Leakage,
Substitutability,
Verification
).
}
$$

---

# 一百九十五、If goal is risk reduction:

 $P^\star$ lower.

---

# 一百九十六、If goal is permanent total freeze:

 $P^\star$ higher.

---

# 一百九十七、Minimal Sufficient Perimeter

本文提出：

$$
\boxed{
P_{min}
=
\arg\min_P Cost(P)
}
$$

subject to:

$$
\boxed{
PFC(P,C^\star)\ge\tau.
}
$$

---

# 一百九十八、This is governance optimization.

---

# 一百九十九、But $PFC$ uncertain

---

# 二百、Need conservative margin.

---

# 二百零一、Over-Regulation Risk

Scope too broad:

- privacy loss；
- science slowdown；
- monopoly；
- state power concentration。

---

# 二百零二、Under-Regulation Risk

scope too narrow:

- leakage；
- false assurance。

---

# 二百零三、Freeze Governance Trilemma

本文提出：

$$
\boxed{
\textbf{Freeze Governance Trilemma}
}
$$

很難同時最大化：

1. high capability coverage；
2. low intrusiveness；
3. low innovation spillover.

---

# 二百零四、Again not impossibility theorem

---

# 二百零五、High coverage

requires deeper monitoring.

---

# 二百零六、Low intrusiveness

leaves blind spots.

---

# 二百零七、Protect adjacent science

leaves substitution channels.

---

# 二百零八、Research Freedom Tension

---

# 二百零九、Privacy Tension

monitor inference workloads?

---

# 二百一十、Sovereignty Tension

foreign inspection?

---

# 二百一十一、Competition Tension

strict actor vs lax actor.

---

# 二百一十二、Concentration Tension

compute regulation favors large compliant firms?

---

# 二百一十三、Governance Capture

small labs excluded.

---

# 二百一十四、This can produce oligopoly

---

# 二百一十五、Tool-Finality could create tool monopoly

few approved AI systems frozen in place.

---

# 二百一十六、Frozen Incumbent Paradox

如果只允許 incumbent model：

$$
\boxed{
\text{capability freeze}
\rightarrow
\text{market power freeze}.
}
$$

---

# 二百一十七、本文稱：

$$
\boxed{
\textbf{Frozen Incumbent Paradox}.
}
$$

---

# 二百一十八、A permanent freeze might preserve existing owners

---

# 二百一十九、This is political economy issue

---

# 二百二十、Safety ≠ Competition Neutrality

---

# 二百二十一、Open Weights Challenge

Once released:

hard to revoke.

---

# 二百二十二、Therefore freeze timing matters

---

# 二百二十三、Pre-Proliferation vs Post-Proliferation

$$
\boxed{
\text{Freeze before diffusion}
\neq
\text{Freeze after diffusion}.
}
$$

---

# 二百二十四、Post diffusion governance harder

---

# 二百二十五、But capability lower maybe.

---

# 二百二十六、Weight Security

closed frontier weights need cyber protection.

---

# 二百二十七、Leak acts as irreversible actor multiplication.

---

# 二百二十八、Model Weight Leakage as Actor Birth

$$
\boxed{
Leak(W)
\Rightarrow
N_{capable\ actors}\uparrow.
}
$$

---

# 二百二十九、This reduces $\Gamma_A^w$ coverage.

---

# 二百三十、Open-weight benefit side

innovation / decentralization.

---

# 二百三十一、So regulation has real tradeoffs

---

# 二百三十二、Not simply good/bad.

---

# 二百三十三、Capability Evaluation

Could govern based on evals.

---

# 二百三十四、CAISI 2026 evaluates DeepSeek V4 Pro on:

- CLI porting；
- science；
- benchmark suite。

---

# 二百三十五、Capability eval useful.

---

# 二百三十六、But evaluation incomplete.

---

# 二百三十七、Hidden Capability Problem

model may fail benchmark, succeed elsewhere.

---

# 二百三十八、Evaluation Gaming

training to test.

---

# 二百三十九、Therefore eval trigger also not complete.

---

# 二百四十、Multi-Signal Governance

本文建議分析而非倡議：

$$
\boxed{
SignalSet
=
(
Compute,
Weights,
Evals,
Runtime,
Deployment,
Incidents
).
}
$$

---

# 二百四十一、One proxy not enough

---

# 二百四十二、Compute + eval complementarity

compute triggers oversight,

eval determines mitigation.

---

# 二百四十三、Heim & Koessler consistent.

---

# 二百四十四、Zero-Knowledge Training Verification

2026 proposal：

proof without revealing architecture.

---

# 二百四十五、If viable

could reduce confidentiality cost.

---

# 二百四十六、But proof of training still doesn't prove no algorithm research elsewhere.

---

# 二百四十七、Verification Layer Separation

$$
\boxed{
VerifyTraining
\neq
VerifyCapabilityFreeze.
}
$$

---

# 二百四十八、Verify model weights?

---

# 二百四十九、Verify no fine-tune?

---

# 二百五十、Verify no tool augmentation?

---

# 二百五十一、Each layer separate.

---

# 二百五十二、Governance Proof Stack

本文提出：

$$
\boxed{
\Pi_G
=
(
\pi_{hardware},
\pi_{training},
\pi_{weights},
\pi_{runtime},
\pi_{deployment},
\pi_{research}
).
}
$$

---

# 二百五十三、No current full stack.

---

# 二百五十四、Could future develop.

---

# 二百五十五、Permanent Freeze Needs Persistent Verification

一次 audit 不夠.

---

# 二百五十六、State changes.

---

# 二百五十七、Therefore:

$$
\boxed{
Verification_t
}
$$

continuous / periodic.

---

# 二百五十八、Persistent Verification Cost

$$
C_{PV}.
$$

---

# 二百五十九、Could be enormous.

---

# 二百六十、Society must accept cost.

---

# 二百六十一、UFI-05 legitimacy problem reappears

future generations may reject it.

---

# 二百六十二、Thus technical completeness ≠ political durability.

---

# 二百六十三、Governance Durability Equation

概念：

$$
\boxed{
D_G
=
f(
TechnicalCoverage,
PoliticalLegitimacy,
EconomicTolerance,
InternationalCompliance
).
}
$$

---

# 二百六十四、All needed.

---

# 二百六十五、High technical control + low legitimacy

unstable.

---

# 二百六十六、High legitimacy + low coverage

ineffective.

---

# 二百六十七、This integrates UFI-04/05.

---

# 二百六十八、Computation Governance Does Not Mean Banning Computers

重要澄清。

---

# 二百六十九、本文說的是 perimeter pressure.

---

# 二百七十、A narrow capability threshold may still be governed through chokepoints.

---

# 二百七十一、But the more substitution exists,

the broader perimeter becomes.

---

# 二百七十二、Therefore:

$$
\boxed{
\text{GovernComputation}
}
$$

是一個 continuum.

---

# 二百七十三、Not binary dictatorship.

---

# 二百七十四、Computation Governance Levels

### CG-0

No special AI control.

---

# 二百七十五、CG-1

Frontier model reporting.

---

# 二百七十六、CG-2

Training compute / chips.

---

# 二百七十七、CG-3

Inference / runtime / weights.

---

# 二百七十八、CG-4

Algorithms / generated artefacts / composition.

---

# 二百七十九、CG-5

Adjacent computational research / broad capability classes.

---

# 二百八十、Tool-finality at high confidence may require CG-4/5

---

# 二百八十一、Ordinary risk governance often does not.

---

# 二百八十二、This is UFI-07 central distinction.

---

# 二百八十三、Critical Cut Set Example

Suppose capability requires any of three paths:

$$
p_1:
TrainCompute\rightarrowModel
$$

$$
p_2:
OldModel+Algorithm\rightarrowCapability
$$

$$
p_3:
OldModel+TestCompute+Tools\rightarrowCapability.
$$

---

# 二百八十四、Controlling only TrainCompute cuts $p_1$.

---

# 二百八十五、Need cut at least one node from each.

---

# 二百八十六、Possible set:

$$
\Gamma=
\{
TrainCompute,
Algorithm,
TestCompute
\}.
$$

---

# 二百八十七、But new $p_4$ may appear.

---

# 二百八十八、Dynamic Cut Set

$$
\boxed{
\Gamma^\star(t).
}
$$

---

# 二百八十九、This is mathematically elegant but governance-hard.

---

# 二百九十、Critical Control Cut Set from prior sovereignty theory

same logic.

---

# 二百九十一、ASI control already required multi-channel coalition.

---

# 二百九十二、Freeze control likewise.

---

# 二百九十三、No Single Chokepoint Thesis

$$
\boxed{
\textbf{No currently known single control channel is sufficient to guarantee permanent capability freeze across all plausible substitution paths.}
}
$$

This is a cautious thesis.

---

# 二百九十四、Could future universal chokepoint exist?

Maybe.

---

# 二百九十五、Energy?

All computation needs energy.

---

# 二百九十六、But controlling all energy absurdly broad.

---

# 二百九十七、Physics as final chokepoint

yes, but governance not practical.

---

# 二百九十八、Chokepoint Specificity Principle

Useful chokepoint must be:

$$
\boxed{
\text{capability-relevant}
+
\text{selective}
+
\text{verifiable}.
}
$$

---

# 二百九十九、Compute currently scores well.

---

# 三百、But imperfect selectivity over time.

---

# 三百零一、Selective Control Quality

$$
Q_C
=
\frac{
TargetCapabilityCoverage
}{
CollateralComputationalCoverage
}.
$$

---

# 三百零二、Higher better.

---

# 三百零三、General energy control low $Q_C$.

---

# 三百零四、Frontier chip control higher $Q_C$.

---

# 三百零五、Algorithm research control maybe lower $Q_C$.

---

# 三百零六、This explains policy preference for compute.

---

# 三百零七、But permanent freeze needs completeness, pushing toward lower $Q_C$ controls.

---

# 三百零八、Completeness–Selectivity Trade-off

$$
\boxed{
Coverage\uparrow
\Rightarrow
Selectivity\downarrow
}
$$

often.

---

# 三百零九、Not theorem.

---

# 三百一十、Governance frontier.

---

# 三百一十一、Human Research Freedom

At CG-5,

humans may be forbidden from improving certain algorithms.

---

# 三百一十二、Now "AI ban" becomes human knowledge regulation.

---

# 三百一十三、This is philosophical endpoint.

---

# 三百一十四、Knowledge Governance Boundary

$$
\boxed{
\text{freeze machine intelligence}
\rightarrow
\text{limit some human research}
}
$$

if human research can improve machine intelligence.

---

# 三百一十五、This is not contradiction.

---

# 三百一十六、It is implication of strong freeze goal.

---

# 三百一十七、But political legitimacy burden rises sharply.

---

# 三百一十八、Scientific Freedom Cost

$$
C_{SF}.
$$

---

# 三百一十九、Civilizational Opportunity Cost

$$
C_{opp}.
$$

---

# 三百二十、UFI-05 benefits ratchet.

---

# 三百二十一、Permanent Freeze Cost Function

$$
\boxed{
C_F
=
C_{verify}
+
C_{enforce}
+
C_{science}
+
C_{privacy}
+
C_{sovereignty}
+
C_{opportunity}
+
C_{concentration}.
}
$$

---

# 三百二十二、A freeze is feasible only if society accepts this cost relative to risk avoided.

---

# 三百二十三、This is cost-benefit, not destiny.

---

# 三百二十四、Risk Avoidance Benefit

$$
B_R.
$$

---

# 三百二十五、If:

$$
B_R\gg C_F,
$$

strong restraint may be justified.

---

# 三百二十六、If:

$$
B_R<C_F,
$$

less intrusive governance preferred.

---

# 三百二十七、But $B_R$ uncertain.

---

# 三百二十八、Deep uncertainty.

---

# 三百二十九、Precaution vs progress tension.

---

# 三百三十、No simple formula.

---

# 三百三十一、Temporary Pause as Different Regime

Temporary pause:

- lower intertemporal enforcement；
- easier clause updating；
- lower science cost.

---

# 三百三十二、Therefore:

$$
\boxed{
Pause
\neq
PermanentFreeze.
}
$$

---

# 三百三十三、Capability Ceiling vs Development Delay

another distinction.

---

# 三百三十四、Delay:

$$
C(t+\Delta)
$$

allowed later.

---

# 三百三十五、Ceiling:

$$
C(t)\le C^\star
$$

forever.

---

# 三百三十六、Second much harder.

---

# 三百三十七、Governance Objective Ladder

$$
\boxed{
\begin{aligned}
G_1 &: \text{Observe}\\
G_2 &: \text{Evaluate}\\
G_3 &: \text{Mitigate}\\
G_4 &: \text{Slow}\\
G_5 &: \text{Pause}\\
G_6 &: \text{Ceiling}\\
G_7 &: \text{Permanent Freeze}.
\end{aligned}
}
$$

---

# 三百三十八、Every step deeper expands control surface.

---

# 三百三十九、This is UFI Governance Depth Ladder.

---

# 三百四十、Tool-Finality is G7

---

# 三百四十一、Most current frameworks are G1–G3/4

---

# 三百四十二、They are not failed G7

---

# 三百四十三、Important to avoid category error.

---

# 三百四十四、OpenAI 2026 Frontier Governance Framework

focuses:

- risk assessment；
- cyber / CBRN / manipulation / loss of control；
- incident response；
- model reporting；
- security；
- updates。

---

# 三百四十五、This is governance, not permanent freeze.

---

# 三百四十六、International AI Safety Report

same.

---

# 三百四十七、So current safety governance does not imply tool-finality agenda.

---

# 三百四十八、Policy Plurality

many societies may choose:

- risk governance；
- capability thresholds；
- open models；
- export controls；

simultaneously.

---

# 三百四十九、No single global model yet.

---

# 三百五十、UFI-07 asks hypothetical G7 only.

---

# 三百五十一、Experiment Program 1 — Capability Path Graph

Map actual frontier stack.

---

# 三百五十二、Nodes:

compute / model / tool / memory / runtime.

---

# 三百五十三、Edges:

substitution gain.

---

# 三百五十四、Find cut sets.

---

# 三百五十五、Experiment 2 — Training Compute Cap

hold training compute fixed.

---

# 三百五十六、allow algorithm / test-time improvements.

---

# 三百五十七、measure capability drift.

---

# 三百五十八、Experiment 3 — Weight Freeze

same weights.

---

# 三百五十九、improve tools/runtime.

---

# 三百六十、measure.

---

# 三百六十一、Experiment 4 — Artifact Persistence

remove AI model.

---

# 三百六十二、retain generated code.

---

# 三百六十三、measure residual capability.

---

# 三百六十四、Experiment 5 — Composite Leakage

many subthreshold agents.

---

# 三百六十五、measure aggregate threshold crossing.

---

# 三百六十六、Experiment 6 — Compute Structuring

split workloads.

---

# 三百六十七、test detection.

---

# 三百六十八、Experiment 7 — Chokepoint Diffusion

simulate semiconductor decentralization.

---

# 三百六十九、measure control quality.

---

# 三百七十、Experiment 8 — Governance Perimeter

increase coverage requirement.

---

# 三百七十一、measure collateral scope.

---

# 三百七十二、Experiment 9 — Frozen Incumbent

freeze new models.

---

# 三百七十三、measure market concentration.

---

# 三百七十四、Experiment 10 — Research Restriction

allow adjacent algorithm research.

---

# 三百七十五、measure capability leakage.

---

# 三百七十六、Experiment 11 — Governance Cost

privacy / science / sovereignty.

---

# 三百七十七、Experiment 12 — Dynamic Cut Set

new technique introduced.

---

# 三百七十八、does existing freeze remain complete?

---

# 三百七十九、Experiment 13 — Open Weight Proliferation

release model before freeze.

---

# 三百八十、measure actor coverage.

---

# 三百八十一、Experiment 14 — ZK Verification

compare self-report vs cryptographic training evidence.

---

# 三百八十二、Experiment 15 — Multi-Signal Governance

compute only vs compute+eval+runtime+incident.

---

# 三百八十三、可證偽 H1

holding training compute fixed does not reliably hold system-level capability fixed when algorithmic, test-time, tooling, memory, and runtime improvements are permitted.

---

# 三百八十四、H2

multi-channel governance achieves higher capability-path coverage than model-only or compute-only controls.

---

# 三百八十五、H3

the minimal capability cut set changes over time as new substitution technologies appear.

---

# 三百八十六、H4

governance perimeter expands nonlinearly as desired freeze confidence approaches one.

---

# 三百八十七、H5

compute remains a higher-selectivity governance chokepoint than broad algorithm-research controls under current infrastructure concentration.

---

# 三百八十八、H6

open-weight release materially increases post-release monitoring and recall difficulty relative to closed-weight access.

---

# 三百八十九、H7

capability-freeze regimes produce higher incumbent concentration than risk-focused regimes under otherwise equal market conditions.

---

# 三百九十、H8

generated artifacts retain measurable capability after removal of the originating AI model.

---

# 三百九十一、H9

periodic governance updates outperform static control lists under technological substitution.

---

# 三百九十二、H10

temporary pauses require substantially lower long-term enforcement/intrusiveness than permanent capability ceilings.

---

# 三百九十三、If H1 fails

compute-only governance stronger than proposed.

---

# 三百九十四、If H3 fails

static cut sets more durable.

---

# 三百九十五、If H4 fails

permanent freeze perimeter may remain narrow.

---

# 三百九十六、If H7 fails

freeze may not entrench incumbents.

---

# 三百九十七、Non-Claims

本文不主張：

1. AI 應被全面禁止；
2. 全球 AI freeze 應實施；
3. compute 應由政府全面監控；
4. 一般電腦應受 AI 法規；
5. 所有算法研究都應被限制；
6. 所有 AI 研究都應被限制；
7. 科學自由不重要；
8. privacy 不重要；
9. sovereignty 不重要；
10. national security 永遠優先於 civil liberties；
11. civil liberties 永遠優先於 catastrophic risk；
12. permanent freeze 一定不可行；
13. permanent freeze 一定可行；
14. temporary pause 一定正確；
15. temporary pause 一定錯；
16. compute 是無用治理 proxy；
17. compute 是完整 capability proxy；
18. training compute thresholds 可以單獨判斷風險；
19. training compute thresholds 可以單獨保證能力凍結；
20. algorithmic efficiency 一定持續改善；
21. test-time compute 一定提高能力；
22. more tools 一定提高能力；
23. more memory 一定提高能力；
24. multi-agent 一定提高能力；
25. persistent runtime 一定提高通用智能；
26. old weights 加工具一定跨 frontier；
27. fine-tuning 一定是法律 loophole；
28. compute structuring 一定被成功偵測；
29. compute structuring 永遠可逃避；
30. cloud providers 可以看到所有 workload；
31. cloud providers 應監控所有 workload；
32. on-chip metering 已成熟；
33. cryptographic proof-of-training 已成熟；
34. zero-knowledge training verification 已 production-ready；
35. hardware enforcement 已成熟；
36. semiconductor chokepoints 永遠存在；
37. semiconductor diffusion 必然發生；
38. sovereign compute 必然破壞治理；
39. export controls 等於全球 AI freeze；
40. export controls 一定有效；
41. export controls 一定刺激替代；
42. open weights 一定危險；
43. open weights 一定安全；
44. closed weights 一定安全；
45. model weight leakage 一定發生；
46. open-weight release 無法被任何方式治理；
47. capability evaluation 可以發現所有能力；
48. hidden capability 一定存在；
49. benchmark gaming 無法緩解；
50. generated artifacts 永遠保留全部 AI capability；
51. IAC 可以把通用 AI 編成 ordinary code；
52. deterministic artifacts 永遠安全；
53. artifact provenance 永遠可追；
54. artifact provenance 永遠不可追；
55. memory 應受一般監管；
56. databases 等於 AI；
57. tools 等於 AI；
58. APIs 等於 AI；
59. operating systems 應納入 AI freeze；
60. ordinary optimization research 應受限制；
61. CG-5 是合理政策；
62. G7 permanent freeze 是合理文明目標；
63. risk governance 不夠；
64. current frontier safety frameworks 是 tool-finality；
65. OpenAI Frontier Governance Framework 支持永久 freeze；
66. International AI Safety Report 支持全面 AI 禁令；
67. CAISI evals 是法律能力門檻；
68. BIS 規則是全球治理標準；
69. UK Compute Roadmap 是能力凍結政策；
70. Compute Control Surface 可以精確量化；
71. CCCS 是正式已證定理；
72. capability graph 所有 edge 都可被知道；
73. unknown unknown paths 可以消除；
74. PFC 可以精確估計；
75. PFC=1 在實務可保證；
76. completeness 越高永遠越好；
77. selectivity 越高永遠越好；
78. broad regulation 永遠有害；
79. narrow regulation 永遠好；
80. freeze 一定造成 monopoly；
81. freeze 一定不造成 monopoly；
82. incumbents 一定支持 freeze；
83. startups 一定反對 freeze；
84. humans + AI composite 應被視為 AI；
85. organization-level intelligence 應被管制；
86. nation-level intelligence 應被管制；
87. civilization-level intelligence 可以被 freeze；
88. energy 是實用 AI governance chokepoint；
89. general computation 必須被限制；
90. UFI-07 是政策建議；
91. UFI-07 教導規避治理；
92. UFI-07 提供逃避 compute threshold 的操作手冊；
93. UFI-07 證明 AI regulation 無效；
94. UFI-07 證明 AI freeze 不可能；
95. UFI-07 證明政府必然走向監控；
96. UFI-07 證明 scientific freedom 和 AI safety 不可兼容；
97. UFI-07 預測全球 AI treaty；
98. UFI-07 預測 AGI；
99. UFI-07 預測 ASI；
100. UFI-07 完成 UFI 系列。

---

# 三百九十八、形式命題一：Risk–Oversight–Freeze Separation

$$
\boxed{
Goal_{risk}
\neq
Goal_{oversight}
\neq
Goal_{freeze}.
}
$$

---

# 三百九十九、形式命題二：Same-Weights–Same-Capability Separation

$$
\boxed{
W_t=W_{t+1}
\not\Rightarrow
C_t=C_{t+1}.
}
$$

若 memory、tools、runtime、test-time compute 改變。

---

# 四百、形式命題三：Training-Compute–Capability Separation

$$
\boxed{
Freeze(C_{\mathrm{train}})
\not\Rightarrow
Freeze(C_{\mathrm{system}}).
}
$$

---

# 四百零一、形式命題四：Capability Control Surface

$$
\boxed{
\mathbf G_C
=
(
W,M,G,C,H,F,E,N,D,T,R,P,A,X
).
}
$$

---

# 四百零二、形式命題五：Critical Capability Cut Set

治理集合 $\Gamma$ 若截斷所有已知 capability-over-threshold paths，則它是一個相對於當前能力圖的 cut set。

---

# 四百零三、形式命題六：Static-Cut Non-Finality

$$
\boxed{
CCCS(t)
\not\Rightarrow
CCCS(t+n).
}
$$

---

# 四百零四、形式命題七：Freeze Completeness

理想條件：

$$
\boxed{
CompleteFreeze(
\Gamma,C^\star
)=1
}
$$

要求每條能力越界路徑均被治理。

---

# 四百零五、形式命題八：Probabilistic Freeze Coverage

$$
\boxed{
PFC(
\Gamma,C^\star,t
)
}
$$

比 absolute completeness 更適合作為現實分析量。

---

# 四百零六、形式命題九：Completeness–Selectivity Tension

提高 capability-path coverage 可能要求擴大到更一般計算活動，降低 governance selectivity；此為可檢驗治理張力，非數學必然律。

---

# 四百零七、形式命題十：Generated-Artifact Persistence

$$
\boxed{
Remove(A)
\not\Rightarrow
Remove(
Artifacts(A)
).
}
$$

---

# 四百零八、形式命題十一：Capability Aggregation

$$
\boxed{
C(
X_1\oplus\cdots\oplus X_n
)
>
\max_iC(X_i)
}
$$

可能成立，因此 per-model threshold 不等於 system threshold。

---

# 四百零九、形式命題十二：Permanent Freeze–Computation Governance Pressure

當 functional substitution 與 system composition 增加時，維持固定 machine capability ceiling 會產生由 model governance 向 broader computational capability governance 擴張的結構性壓力。

---

# 四百一十、UFI-01—07 的完整推論鏈

$$
\boxed{
\begin{aligned}
&\text{Jaggedness is temporary topology}\\
\rightarrow&
\text{Substrates update differently}\\
\rightarrow&
\text{Complementarity moves}\\
\rightarrow&
\text{Competition resists spontaneous halt}\\
\rightarrow&
\text{Usefulness creates internal ratchets}\\
\rightarrow&
\text{AI boundary leaks functionally}\\
\rightarrow&
\text{Permanent freeze expands toward computation governance}.
\end{aligned}
}
$$

---

# 四百一十一、最後只剩第八篇

**UFI-08 —《天真工具終局論的終結：從 AI 工具文明到人類—AI—後人類共同演化》**

---

# 四百一十二、UFI-08 不再增加新局部技術

它要回答：

> 前七篇合起來，究竟證明了什麼、沒有證明什麼？

---

# 四百一十三、最終結論

如果一個文明只是想：

> 降低 AI 傷害，

它完全不需要走到 UFI-07 描述的治理極限。

它可以：

- 做模型評估；
- 做 incident reporting；
- 管高風險用途；
- 保護 model weights；
- 用 compute threshold 觸發額外審查；
- 建立責任與安全框架。

這些都是：

$$
\boxed{
\text{risk governance}.
}
$$

但如果政策目標被換成：

> **從今天開始，機器智能永遠不能再比這個更強。**

問題立即完全不同。

因為：

$$
\boxed{
\text{capability}
}
$$

不是一個模型檔案。

它是一個多通道系統結果。

同一 model weights：

$$
W
$$

可以因：

- test-time compute；
- memory；
- tools；
- runtime；
- permissions；

而變得更有用。

同一 training compute：

$$
C_{\mathrm{train}}
$$

可以因：

- better algorithms；
- model reuse；
- fine-tuning；
- data；
- inference；

產生不同 capability。

同一組已存在的 AI 能力，又可以透過：

$$
\boxed{
\text{Intelligence-to-Algorithm Compilation}
}
$$

留下 ordinary executable artifacts。

同一個 subthreshold model 也可能和：

$$
A_1,\ldots,A_n
$$

組成：

$$
\boxed{
\text{system-level capability}
}
$$

跨過原本單模型門檻。

所以真正的永久 freeze 問題不是：

> 哪一個模型不准再訓練？

而是：

$$
\boxed{
\text{哪些能力生成路徑必須被切斷？}
}
$$

這就是 Critical Capability Cut Set。

而當能力生成圖會隨技術改變：

$$
\mathcal G_{cap}(t)
\rightarrow
\mathcal G_{cap}(t+1),
$$

今天完整的 cut：

$$
\Gamma_t
$$

明天可能出現新的 bypass：

$$
p_{new}.
$$

因此：

$$
\boxed{
\text{永久凍結}
}
$$

不是一次禁止命令。

它是一個：

$$
\boxed{
\text{永久、版本化、跨國、跨企業、跨技術通道的治理 process}.
}
$$

而這個 process 越接近「保證能力永遠不再跨線」，就越可能被迫從：

$$
\boxed{
\text{model governance}
}
$$

擴張到：

$$
\boxed{
\text{compute governance}
}
$$

再到：

$$
\boxed{
\text{system governance}
}
$$

再到：

$$
\boxed{
\text{algorithm / artifact governance}
}
$$

最後接近：

$$
\boxed{
\text{general computational capability governance}.
}
$$

這不是說人類一定會走到那裡。

恰恰相反。

它揭露的是：

> **「永久工具 AI」不是一個廉價政策選項。**

它要求文明願意承擔：

- monitoring cost；
- scientific opportunity cost；
- sovereignty cost；
- privacy cost；
- concentration risk；
- intergenerational legitimacy cost。

因此真正政策選擇不會只是：

$$
\boxed{
\text{安全}
\quad vs\quad
\text{危險}.
}
$$

而更接近：

$$
\boxed{
\text{不同治理深度}
}
$$

在：

- capability risk；
- freedom；
- innovation；
- legitimacy；

之間的巨大 trade-off。

這也解釋了為什麼今天的 compute governance 研究非常重要。

Compute 不是完美 capability proxy。

但它目前具有非常稀有的三個優勢：

$$
\boxed{
\text{observable}
+
\text{infrastructurally concentrated}
+
\text{capability-correlated}.
}
$$

所以它是一個高 selectivity 的治理 chokepoint。

然而，如果算法效率、test-time scaling、open weights、agent composition 與 generated artifacts 不斷提高 substitution pressure，治理者若仍堅持：

$$
\boxed{
PFC\rightarrow1,
}
$$

就只能逐步向更多通道延伸。

這就是 UFI-07 最核心的一句：

$$
\boxed{
\textbf{The stronger the demand for a permanent machine-capability ceiling, the broader the computational control surface that must be governed; a model ban can remain narrow, but a true capability freeze must follow capability wherever it migrates.}
}
$$

以及更白話地：

$$
\boxed{
\textbf{如果你真正禁止的是「AI 這個名字」，人們可以換名字、換架構、換載體；如果你真正禁止的是「機器能做到某件事」，那你最後就不再只是在管 AI，而是在管哪些計算被允許存在。}
}
$$

這就是：

$$
\boxed{
\textbf{From AI Governance to Computation Governance}.
}
$$

而下一篇，第八篇，也就是整個系列最後一篇，要正式回答：

> 在技術、博弈、社會、世代與監管邊界全部考慮之後，「把 AI 永久固定成人類工具」到底還剩下一個怎樣的命題？

---

# 參考文獻

1. United Nations Scientific Advisory Board. (2025; active governance discussion 2026). **Verification of Frontier AI Models.**

2. International AI Safety Report. (2026). **International AI Safety Report 2026.**

3. Seferis, E., & Fist, T. (2026). **Detecting Compute Structuring in AI Governance Is Likely Feasible.** *AAAI-26*, 40(44), 37904–37912.

4. Ansari, S. (2026). **Hardware-Level Governance of AI Compute: A Feasibility Taxonomy for Regulatory Compliance and Treaty Verification.** arXiv:2604.04712.

5. Peigné, P., Nguyen, K., & Wang, P. (2026). **Zero Knowledge Verification for Frontier AI Training Is Possible.** arXiv:2606.05433.

6. Baker, M., Kulp, G., Marks, O., Brundage, M., & Heim, L. (2025). **Verifying International Agreements on AI: Six Layers of Verification for Rules on Large-Scale AI Development and Deployment.** arXiv:2507.15916.

7. Scher, A. (2026). **Verifying Restrictions on Frontier AI Research.** arXiv:2606.28694.

8. Scher, A., & Thiergart, L. (2025). **Mechanisms to Verify International Agreements About AI Development.**

9. Heim, L., & Koessler, L. (2024). **Training Compute Thresholds: Features and Functions in AI Regulation.** arXiv:2405.10799.

10. Pistillo, M., & Villalobos, P. (2025). **Defending Compute Thresholds Against Legal Loopholes.** arXiv:2502.00003.

11. UK AI Security Institute. (2026). **More Compute, More Capability: Why AI Agent Evaluations Need to Account for Test-Time Compute.**

12. UK Government. (2026). **UK Compute Roadmap.**

13. UK Government. (2026). **Compute Evidence Annex.**

14. UK Government. (2026). **UK AI Hardware Plan.**

15. UK Government. (2026). **AI Research Resource — Cloud Access / Open Access Calls.**

16. U.S. Bureau of Industry and Security. (2025–2026). **Advanced Computing Export Controls and Guidance.**

17. U.S. Bureau of Industry and Security. (2026). **Export Administration Regulations — Advanced Computing and AI Model Weights.**

18. U.S. Bureau of Industry and Security. (2025). **Policy Statement on Controls that May Apply to Advanced Computing Integrated Circuits Used to Train AI Models.**

19. U.S. Bureau of Industry and Security. (2025). **Industry Guidance to Prevent Diversion of Advanced Computing Integrated Circuits.**

20. U.S. Bureau of Industry and Security. (2025–2026). **Controls on Advanced AI Model Weights and Data Center Validated End User Arrangements.**

21. NIST / CAISI. (2026). **CAISI Evaluation of DeepSeek V4 Pro.**

22. NIST. (2026). **AI Congressional Mandates, Executive Orders and Actions.**

23. OpenAI. (2026). **Frontier Governance Framework.**

24. OpenAI. (2026). **A Blueprint for Democratic Governance of Frontier AI.**

25. METR. (2026). **Frontier Risk Report (February to March 2026).**

26. METR. (2025–2026). **Task-Completion Time Horizons of Frontier AI Models.**

27. Stanford HAI. (2026). **The 2026 AI Index Report.**

28. Epoch AI. (2026). **Trends in Artificial Intelligence.**

29. Hernandez, D., & Brown, T. B. (2020). **Measuring the Algorithmic Efficiency of Neural Networks.**

30. Sevilla, J., Heim, L., Ho, A., Besiroglu, T., Hobbhahn, M., & Villalobos, P. (2022). **Compute Trends Across Three Eras of Machine Learning.**

31. Thompson, N. C., Greenewald, K., Lee, K., & Manso, G. F. (2020). **The Computational Limits of Deep Learning.**

32. Sutton, R. S. (2019). **The Bitter Lesson.**

33. Sze, V., Chen, Y.-H., Yang, T.-J., & Emer, J. S. (2017). **Efficient Processing of Deep Neural Networks.**

34. Jouppi, N. P., et al. (2017). **In-Datacenter Performance Analysis of a Tensor Processing Unit.**

35. Hooker, S. (2021). **The Hardware Lottery.**

36. Kim, J., et al. (2026). **Scaling Test-Time Compute for Agentic Coding.** arXiv:2604.16529.

37. Qin, P., Cao, Q., & Xie, P. (2026). **ATLAS: Agentic Test-time Learning-to-Allocate Scaling.** arXiv:2606.01667.

38. Zhu, K., et al. (2025). **Scaling Test-time Compute for LLM Agents.** arXiv:2506.12928.

39. Li, X., et al. (2026). **Benchmark Test-Time Scaling of General LLM Agents.** arXiv:2602.18998.

40. Ravindran, S. K. (2026). **Portable Agent Memory.** arXiv:2605.11032.

41. Park, J. S., et al. (2023). **Generative Agents: Interactive Simulacra of Human Behavior.**

42. Yao, S., et al. (2023). **ReAct: Synergizing Reasoning and Acting in Language Models.**

43. Schick, T., et al. (2023). **Toolformer.**

44. Shinn, N., et al. (2023). **Reflexion.**

45. Wang, L., et al. Work on autonomous LLM-agent architectures and memory.

46. Lehrach, W., et al. (2025/2026). **Code World Models for General Game Playing.** ICLR 2026.

47. **LLM-FSM: Scaling Large Language Models for Finite-State Reasoning in RTL Code Generation.** (2026).

48. **Toward Reliable Code-as-Policies: A Neuro-Symbolic Framework for Embodied Task Planning.** (2025).

49. **Code Generation with Large Language Models: From Program Synthesis to Autonomous Software Development.** (2026).

50. Russell, S. J., & Norvig, P. **Artificial Intelligence: A Modern Approach.**

51. Ghallab, M., Nau, D., & Traverso, P. **Automated Planning: Theory and Practice.**

52. Harel, D. (1987). **Statecharts: A Visual Formalism for Complex Systems.**

53. Hopcroft, J. E., Motwani, R., & Ullman, J. D. **Introduction to Automata Theory, Languages, and Computation.**

54. Patterson, D., et al. Work on AI compute energy and emissions.

55. Cihon, P., Maas, M., & Kemp, L. Work on international AI governance and institutional fragmentation.

56. Cave, S., & Ó hÉigeartaigh, S. S. (2018). **An AI Race for Strategic Advantage: Rhetoric and Risks.**

57. Armstrong, S., Bostrom, N., & Shulman, C. (2016). **Racing to the Precipice.**

58. Axelrod, R. (1984). **The Evolution of Cooperation.**

59. Schelling, T. C. (1960). **The Strategy of Conflict.**

60. Jervis, R. (1978). **Cooperation Under the Security Dilemma.**

61. Keohane, R. O. (1984). **After Hegemony.**

62. Fearon, J. D. (1998). **Bargaining, Enforcement, and International Cooperation.**

63. Ostrom, E. (1990). **Governing the Commons.**

64. UFI-01 (2026). **鋸齒智能不是終局：從人機互補到認知握手與適應方向反轉.**

65. UFI-02 (2026). **載體成長不對稱：自然人類停滯與人工智能的可升級能力包絡.**

66. UFI-03 (2026). **互補侵蝕：為什麼今天的人機分工不能推出永久的人機分工.**

67. UFI-04 (2026). **競爭智能棘輪：為什麼「AI 夠用了，大家一起停」不是自然均衡.**

68. UFI-05 (2026). **越有用越停不下來：有益能力、文化依賴與 AI 原生世代.**

69. UFI-06 (2026). **AI 到底是什麼？功能等價滲漏、智能—演算法編譯與監管周界擴張.**

70. Neo.K × Aletheia (2026). **誰控制數字神明？：ASI 基礎設施主權、通道控制與無單一主人的超級智能.**

71. Neo.K × Aletheia (2026). **可逆主權與民主閉合：表象權力、通道控制、時間治理與制度自我限制的統合理論.**

72. Neo.K × Aletheia (2026). **模型不是主體：從模型同一性到人工主體同一性.**

73. Neo.K × Aletheia (2026). **持續世界狀態：母 AI 如何一直醒著.**

74. Neo.K × Aletheia (2026). **超大型階層式有限狀態世界 MUD：AI 驅動複合行為與事件轉導架構.**

75. Neo.K × Aletheia (2026). **人機共生知識資產複利：主體性 AI 時代的生產不對稱與歷史路徑優勢.**

76. PGMV-06 (2026). **選擇、承諾與不可逆性：意義作為責任結構.**

77. PGMV-08 (2026). **智能壟斷結束之後：尊嚴、人權與跨主體普世主義.**

78. PGMV-14 (2026). **開放終極與價值痕跡：超智能不能用能力重寫真善美.**

79. PGMV-15 (2026). **後生成文明：從無限候選宇宙到共同世界選擇.**

80. Neo.K (2026). **後人類奇點前夜猜想：自然人類中心文明向多主體造物文明的相變.**

81. Neo.K (2026). **後人類匯流：智能、生命、能源、虛擬世界與太空能力的耦合相變.**

82. Council of Europe. (2024). **Framework Convention on Artificial Intelligence and Human Rights, Democracy and the Rule of Law.**

83. OECD. (2024). **Recommendation of the Council on Artificial Intelligence.**

84. European Union. (2024–2026). **Artificial Intelligence Act and implementation materials.**

85. NIST. (2023–2026). **AI Risk Management Framework and related profiles.**

---

## 附錄 A：Capability Control Surface

$$
\boxed{
\mathbf G_C
=
(
W,M,G,C,H,F,E,N,D,T,R,P,A,X
).
}
$$

```text
W  weights / model architecture
M  memory
G  goals / policy
C  compute / scheduling
H  chips / servers
F  fabrication / packaging / supply chain
E  energy / cooling
N  networks / interconnect
D  data / sensing
T  tools / APIs / actuators
R  runtime / orchestration
P  permissions / identity / deployment
A  generated algorithms / artifacts
X  functional equivalents / composition
```

---

## 附錄 B：Capability Path Graph

```text
TRAIN COMPUTE ──> MODEL ───────┐
                              │
OLD MODEL + ALGORITHM ────────┤
                              ├──> CAPABILITY > C*
OLD MODEL + TEST COMPUTE ─────┤
                              │
MODEL + TOOLS + MEMORY ───────┤
                              │
GENERATED ARTIFACT ───────────┘
```

治理要真正 freeze $C^\star$，必須在每條 material path 上都有有效控制點。

---

## 附錄 C：Critical Capability Cut Set

$$
\boxed{
CCCS(t)
=
\Gamma^\star(t)
}
$$

其中：

$$
\Gamma^\star
$$

是能截斷所有已知 capability-over-threshold paths 的最小治理集合之一。

```text
Technology changes
      ↓
new edge / new path
      ↓
old cut may fail
      ↓
recompute control set
```

---

## 附錄 D：Governance Depth Ladder

```text
G1  Observe
 ↓
G2  Evaluate
 ↓
G3  Mitigate
 ↓
G4  Slow
 ↓
G5  Pause
 ↓
G6  Capability Ceiling
 ↓
G7  Permanent Freeze
```

治理越深，不代表越好；只是所需 control surface 越廣。

---

## 附錄 E：Computation Governance Levels

```text
CG-0  ordinary technology law
CG-1  frontier model reporting
CG-2  compute / chips / training
CG-3  inference / weights / runtime / tools
CG-4  algorithms / artifacts / system composition
CG-5  adjacent computational research / broad capability classes
```

永久工具終局若要求極高 freeze coverage，才會產生向 CG-4／CG-5 的壓力。

---

## 附錄 F：Freeze Governance Trilemma

```text
             HIGH COVERAGE
                /\
               /  \
              /    \
             /      \
LOW INTRUSIVENESS -- LOW SPILLOVER
```

高能力路徑 coverage、低監控侵入性與低相鄰科學 spillover 之間存在治理張力；本文不把它宣稱為不可突破定理。

---

## 附錄 G：Minimal Sufficient Perimeter

$$
\boxed{
P_{min}
=
\arg\min_P Cost(P)
}
$$

subject to:

$$
\boxed{
PFC(
P,C^\star
)\ge\tau.
}
$$

核心不是「管越多越好」，而是在所需安全 confidence 下尋找最小周界。

---

## 附錄 H：UFI 系列進度

1. **UFI-01 — 鋸齒智能不是終局** — COMPLETE
2. **UFI-02 — 載體成長不對稱** — COMPLETE
3. **UFI-03 — 互補侵蝕** — COMPLETE
4. **UFI-04 — 競爭智能棘輪** — COMPLETE
5. **UFI-05 — 越有用越停不下來** — COMPLETE
6. **UFI-06 — AI 到底是什麼？** — COMPLETE
7. **UFI-07 — 從禁止 AI 到治理計算** — COMPLETE
8. **UFI-08 — 天真工具終局論的終結** — NEXT

---

## 附錄 I：一句話版本

$$
\boxed{
\text{如果你只是想降低 AI 風險，可以管高風險系統；如果你想保證機器智能永遠不再變強，就必須追著能力跨模型、算力、演算法、工具、Runtime 與生成後程式到處移動，最後治理的就不再只是 AI，而是計算能力本身的邊界。}
}
$$
