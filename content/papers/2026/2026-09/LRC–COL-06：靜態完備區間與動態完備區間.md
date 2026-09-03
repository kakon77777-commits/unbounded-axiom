# LRC–COL-06：靜態完備區間與動態完備區間
## Static and Dynamic Completeness Intervals of Composite Operator Languages

**系列：LRC–COL — Language–Reality Coupling & Composite Operator Language**  
**中文：語言—現實耦合與複合算子語言系列**  
**版本：v0.1**  
**日期：2026-08-21**
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  

---

## 摘要

LRC–COL-03 至 LRC–COL-05 已建立複合算子語言的三個核心靜態問題：最小有效基底 $N_{\min}^{effective}$ 、最大有效算子集 $N_{\max}^{effective}$，以及 operator 數量 $N$ 、組合深度 $d$ 、粒度 $g$ 與 verification density $v$ 之間的交換面。然而，這些量只有在 Agent、domain、workload、retriever、context、版本與風險要求固定時才是靜態的。

真實 AI 語言系統不是固定環境。Agent 會學會新的組合規則；某些反覆使用的複合結構會結晶成 macro；新工具、新 domain 與新風險會加入；舊 operator 會被合併、淘汰、版本化；retriever、compiler 與 context architecture 也會改良；多 Agent population 的成員甚至會持續更新與替換。因此真正需要研究的不是單一區間：

$$
I_{\mathcal O}^{S}
=
[
N_{\min}^{effective},
N_{\max}^{effective}
],
$$

而是一個時間依賴區間：

$$
\boxed{
I_{\mathcal O}^{D}(t)
=
[
N_{\min}(t),
N_{\max}(t)
].
}
$$

本文進一步加入動態最佳點：

$$
\boxed{
N_{\min}(t)
\le
N^*(t)
\le
N_{\max}(t),
}
$$

並將動態語言狀態表示為：

$$
\Theta_t
=
(
A_t,
\Omega_t,
\mu_t,
G_t,
R_t,
C_t,
P_t,
V_t
),
$$

其中 $A_t$ 是 Agent 能力、 $\Omega_t$ 是目標域、 $\mu_t$ 是 workload、 $G_t$ 是 grammar/runtime、 $R_t$ 是 retrieval architecture、 $C_t$ 是 context / compute resource、 $P_t$ 是 population / propagation state，而 $V_t$ 是版本與治理狀態。

本文提出：動態最小邊界受到「domain expansion、new distinction、risk constraints」向外推動，也受到「Agent 內化、composition ability、compiler / retrieval improvement、shared context」向內壓縮；動態最大邊界則受到「retrieval、context、semantic discrimination、hierarchy」向外推升，也會受到「semantic collision、drift、version burden、population instability」向內壓縮。

在此基礎上，本文提出一個候選語言生命週期：

$$
\boxed{
\text{Expansion}
\rightarrow
\text{Saturation}
\rightarrow
\text{Compression}
\rightarrow
\text{Re-expansion}.
}
$$

這不是普遍必然律，而是可檢驗的動態模式。近期 emergent-communication 與大型 tool-retrieval 研究提供了幾個重要外部錨點：代際傳播可以提高人工語言的 learnability，但同時可能造成 vocabulary degeneration；不同 plasticity schedule 會顯著影響 dynamic-agent population 的 language drift；而 massive and evolving tool repositories 已迫使 Agent 系統使用 proactive retrieval、multi-step query planning 與 context-aware filtering，而不能依賴靜態全量工具表。

本文最終主張：

$$
\boxed{
\text{A usable composite language should not target a fixed vocabulary size; it should regulate a moving viability interval.}
}
$$

換言之，未來複合語言的核心治理問題不是「最後固定成幾個符號」，而是「如何讓 operator ecology 在世界與 Agent 都持續變化時，仍維持在可學、可傳、可組、可執行的有效區間內」。

---

## 關鍵詞

dynamic completeness；operator ecology；language evolution；semantic drift；macro crystallization；tool retrieval；AI agent；plasticity；language lifecycle；dynamic vocabulary

---

# 1. 靜態模型的限制

前文：

$$
I_{\mathcal O}^{S}
=
[
N_{\min}^{effective},
N_{\max}^{effective}
]
$$

隱含假設：

- Agent 能力固定；
- domain 固定；
- workload 固定；
- context 固定；
- retriever 固定；
- language version 固定。

但真實系統不滿足這些條件。

因此：

$$
\boxed{
I_{\mathcal O}^{S}
}
$$

只能理解為：

> 某一時刻、某一系統狀態下的切片。

---

# 2. 動態狀態 Θ_t

本文定義：

$$
\boxed{
\Theta_t
=
(
A_t,
\Omega_t,
\mu_t,
G_t,
R_t,
C_t,
P_t,
V_t
).
}
$$

其中：

- $A_t$：Agent capability；
- $\Omega_t$：target domain；
- $\mu_t$：workload distribution；
- $G_t$：grammar / compiler / runtime；
- $R_t$：retriever / routing；
- $C_t$：context / compute / memory budget；
- $P_t$：population / propagation state；
- $V_t$：version / governance state。

於是：

$$
\boxed{
N_{\min}(t)
=
f_{\min}(\Theta_t),
}
$$

$$
\boxed{
N_{\max}(t)
=
f_{\max}(\Theta_t).
}
$$

---

# 3. 動態完備區間

正式定義：

$$
\boxed{
I_{\mathcal O}^{D}(t)
=
[
N_{\min}(t),
N_{\max}(t)
].
}
$$

這個區間回答：

> 在時間 $t$ 的 Agent、domain、runtime 與治理條件下，什麼規模的 operator language 是有效的？

---

# 4. 動態最佳點

只知道區間仍不夠。

定義：

$$
\boxed{
N^*(t)
=
\arg\max_N
J(N;\Theta_t).
}
$$

因此：

$$
\boxed{
N_{\min}(t)
\le
N^*(t)
\le
N_{\max}(t).
}
$$

而且：

$$
N^*(t)
$$

也會漂移。

---

# 5. 四個不同的動態量

需要同時追蹤：

### Global Library

$$
N_G(t)
$$

### Active Set

$$
N_A(q,t)
$$

### Effective Lower Bound

$$
N_{\min}(t)
$$

### Effective Upper Bound

$$
N_{\max}(t)
$$

因此：

$$
\boxed{
\text{language growth}
\neq
\text{effective interval growth}.
}
$$

---

# 6. Operator 變多，不代表有效區間變大

如果：

$$
N_G(t)\uparrow
$$

但：

- collision 上升；
- retrieval 變差；
- drift 上升；

則：

$$
N_{\max}(t)
$$

反而可能下降。

所以：

$$
\boxed{
\frac{dN_G}{dt}>0
\not\Rightarrow
\frac{dN_{\max}}{dt}>0.
}
$$

---

# 7. Agent 學習會改變下界

假設同一 operator language 在：

$$
t_0
$$

需要很多 explicit macros 才能保持低 depth。

經過訓練／內化後：

$$
A_{t_1}
$$

的 composition ability 上升。

則可能：

$$
\boxed{
N_{\min}(t_1)
<
N_{\min}(t_0).
}
$$

即：

> Agent 變強後，語言可以變小。

---

# 8. Internalization Compression

本文稱：

$$
\boxed{
\text{Internalization Compression}.
}
$$

即原本需要顯式 operator：

$$
O_M
$$

幫助 Agent 的流程，

在 Agent 已穩定內化後，可以退回：

- derived form；
- local macro；
- implicit learned routine。

因此 stable global basis 可以收縮。

---

# 9. 但 Agent 變強也可能讓語言變大

更強的 Agent 可以處理：

- 更多 distinctions；
- 更多 domains；
- 更複雜 tool space。

所以：

$$
A_t\uparrow
$$

可能同時讓：

$$
N_{\min}\downarrow
$$

與：

$$
N_{\max}\uparrow.
$$

結果：

$$
\boxed{
|I_{\mathcal O}^{D}(t)|
}
$$

變寬。

---

# 10. Domain Expansion 會推高下界

如果：

$$
\Omega_{t+1}
\supset
\Omega_t,
$$

加入：

- robotics；
- finance；
- biology；
- new APIs；

原本 basis 可能不再 ε-complete。

因此：

$$
\boxed{
N_{\min}(t+1)
>
N_{\min}(t)
}
$$

可能成立。

---

# 11. Distinction Pressure

新 domain 不一定只是多幾個工具。

它可能要求新的 semantic distinctions。

例如原本只有：

```text
execute
```

新 domain 需要區分：

```text
simulate
preview
commit
rollback
authorize
```

則：

$$
\boxed{
\text{Distinction Pressure}
}
$$

推動 basis expansion。

---

# 12. Risk Pressure 也會讓最小基底增加

在低風險 domain：

```text
do
```

可能足夠。

高風險 domain 可能需要：

- verify；
- authorize；
- checkpoint；
- rollback；
- audit。

因此：

$$
\boxed{
Risk\uparrow
\Rightarrow
N_{\min}^{robust}\uparrow
}
$$

可能成立。

---

# 13. 最小邊界的力學表示

可以先寫成：

$$
\boxed{
\dot N_{\min}
=
F_{\Omega}
+
F_{dist}
+
F_{risk}
-
F_{learn}
-
F_{comp}
-
F_{shared}.
}
$$

其中：

- $F_{\Omega}$：domain expansion；
- $F_{dist}$：new distinction；
- $F_{risk}$：risk constraints；
- $F_{learn}$：Agent learning；
- $F_{comp}$：compiler / composition improvement；
- $F_{shared}$：shared context / stable conventions。

這只是第一版 phenomenological equation。

---

# 14. Dynamic Upper Bound

同樣：

$$
N_{\max}(t)
$$

也不是固定。

如果：

- context 增大；
- retrieval 更好；
- semantic discrimination 更強；
- hierarchy 更合理；

則：

$$
N_{\max}\uparrow.
$$

---

# 15. ToolScope 類系統如何推高上界

大型 toolset 中，

如果直接：

$$
N_A=N_G,
$$

active overload 很快出現。

加入：

- tool merging；
- context-aware filtering；

後：

$$
N_A\ll N_G.
$$

因此：

$$
\boxed{
\text{better routing}
\rightarrow
N_{\max}^{effective}\uparrow.
}
$$

---

# 16. ToolDreamer 類 retriever 的意義

2026 年 ToolDreamer 研究指出，大工具集通常不能全部放入 LLM context，因此需要外部 retriever；而單純依 query-description similarity 仍可能有語義 gap。

這意味著：

$$
\boxed{
RetrieverQuality
}
$$

直接是：

$$
N_{\max}
$$

的決定因素。

---

# 17. ToolQP 類 multi-step retrieval 的意義

當 request 本身需要：

$$
O_1\circ O_2\circ O_3,
$$

單次 retrieval 未必能找到完整 tool composition。

2026 年 ToolQP 將 retrieval 改為 iterative query planning。

因此：

$$
\boxed{
\text{better compositional retrieval}
}
$$

也可能推高：

$$
N_{\max}^{effective}.
$$

---

# 18. Open-World Tool Repository

ToolOmni 類工作直接把問題放在：

> massive and evolving tool repositories。

這與 COL 的動態 operator language 幾乎同型。

因為：

$$
\boxed{
\mathcal O_G(t+1)
\neq
\mathcal O_G(t).
}
$$

因此 tool semantics 不能只被靜態 memorization。

---

# 19. 上界的負向壓力

即使 runtime 變強，

以下因素仍會讓：

$$
N_{\max}\downarrow:
$$

- semantic collision；
- version multiplicity；
- language drift；
- population disagreement；
- stale operators；
- ontology fragmentation。

---

# 20. 最大邊界的力學表示

第一版：

$$
\boxed{
\dot N_{\max}
=
G_{retrieval}
+
G_{context}
+
G_{discrim}
+
G_{hier}
-
L_{collision}
-
L_{drift}
-
L_{version}
-
L_{instability}.
}
$$

---

# 21. Dynamic Interval Width

定義：

$$
\boxed{
W_I(t)
=
N_{\max}(t)
-
N_{\min}(t).
}
$$

 $W_I$ 大：

> 語言設計自由度高。

 $W_I$ 小：

> 任何加減 operator 都容易越界。

---

# 22. Interval Collapse

如果：

$$
N_{\min}(t)
>
N_{\max}(t),
$$

則：

$$
\boxed{
I_{\mathcal O}^{D}(t)=\varnothing.
}
$$

代表當前 Agent/runtime 根本不存在同時滿足：

- coverage；
- learnability；
- selection；
- fidelity；
- risk；

的平坦語言。

---

# 23. Interval Collapse 意味著什麼？

不是語言不可能。

而是需要改架構，例如：

- hierarchy；
- external retrieval；
- multi-layer basis；
- stronger Agent；
- domain partition；
- dynamic macro。

也就是：

$$
\boxed{
\text{architecture change}
}
$$

而不是再硬調 N。

---

# 24. Interval Stress

在 collapse 前，

當：

$$
W_I(t)\rightarrow0,
$$

稱：

$$
\boxed{
\text{Interval Stress}.
}
$$

這可以是 language runtime 需要 restructuring 的預警。

---

# 25. Expansion Phase

當新 domain / tool / distinction 快速加入：

$$
\dot N_G>0,
$$

且新增能力的 coverage gain 高，

語言進入：

$$
\boxed{
\text{Expansion}.
}
$$

特徵：

- operator birth 高；
- version 變動高；
- long-tail 快速增加。

---

# 26. Saturation Phase

隨 vocabulary 增長：

- overlap 增加；
- marginal coverage 下降；
- selection / governance cost 上升。

當：

$$
\Delta J_{add}\approx0,
$$

進入：

$$
\boxed{
\text{Saturation}.
}
$$

---

# 27. Compression Phase

此時可能開始：

- merge aliases；
- crystallize motifs；
- retire stale operators；
- build hierarchy；
- improve retriever。

形成：

$$
\boxed{
\text{Compression}.
}
$$

注意 compression 不一定讓：

$$
N_G
$$

下降。

它也可能只讓：

$$
N_A
$$

或：

$$
C_{lang}
$$

下降。

---

# 28. Re-expansion Phase

當新 Agent / 新 domain / 新世界接口出現，

舊壓縮結構可能再次不足。

於是：

$$
\boxed{
\text{Re-expansion}.
}
$$

因此候選生命週期：

$$
\boxed{
Expansion
\rightarrow
Saturation
\rightarrow
Compression
\rightarrow
Re-expansion.
}
$$

---

# 29. 這不是固定四階段定律

某些語言可能：

- 長期擴張；
- 直接 collapse；
- 反覆小幅震盪；
- 多 branch 並行。

所以本文只提出：

$$
\boxed{
\text{candidate lifecycle archetype}.
}
$$

---

# 30. Operator Birth–Death Process

令：

$$
B_t
$$

是新 operator birth rate，

$$
D_t
$$

是 retire / merge rate。

則：

$$
\boxed{
\dot N_G
=
B_t-D_t.
}
$$

但這只描述 cardinality，

不描述效用。

---

# 31. Utility-Weighted Ecology

對 operator $O_i$：

$$
u_i(t).
$$

整體：

$$
\boxed{
U_{\mathcal O}(t)
=
\sum_i u_i(t).
}
$$

可能：

$$
N_G\uparrow
$$

但：

$$
U_{\mathcal O}\downarrow.
$$

所以語言演化不能只追 operator count。

---

# 32. Crystallization

反覆 motif：

$$
m
$$

如果通過 macro admission gate，

形成：

$$
O_m.
$$

這是：

$$
\boxed{
\text{Crystallization}.
}
$$

它可能暫時：

$$
N_G\uparrow.
$$

---

# 33. Consolidation

若：

$$
O_m
$$

成熟後：

- 替代多個舊 aliases；
- 舊 macro 被 deprecated；
- low-value operators 被 retire；

則：

$$
\boxed{
\text{Consolidation}.
}
$$

這才可能讓：

$$
N_G\downarrow.
$$

---

# 34. 所以 Crystallization ≠ Compression

很重要：

$$
\boxed{
\text{Crystallization}
\neq
\text{Cardinality Compression}.
}
$$

結晶最初可能增加 vocabulary。

只有後續 consolidation 才可能壓縮總語言複雜度。

---

# 35. Internalization 又是第三件事

如果 Agent 已學會：

$$
O_m
$$

的 semantics，

可以把 definition 移出 active context。

因此：

$$
C_{context}\downarrow
$$

但：

$$
N_G
$$

可能不變。

所以：

$$
\boxed{
\text{Internalization Compression}
}
$$

主要壓縮 context / learning cost，而非 operator count。

---

# 36. 三種 Compression

因此至少區分：

### Cardinality Compression
operator 真的變少。

### Context Compression
每次不需載入那麼多定義。

### Cognitive Compression
Agent 已把複合程序內化成低成本 routine。

這三者不能混為一談。

---

# 37. Generational Transmission

若：

$$
Language_g
\rightarrow
Agent_{g+1}
\rightarrow
Language_{g+1},
$$

進入：

$$
\boxed{
\text{intergenerational language dynamics}.
}
$$

---

# 38. 2025 LLM Iterated Transmission 的提醒

COLING 2025 的 LLM emergent-language 研究顯示：

- initially unstructured artificial languages 可以逐代形成一些 structure；
- generational transmission 可以提高 learnability；
- 但同時可能產生 non-humanlike degenerate vocabularies。

因此：

$$
\boxed{
\text{Learnability Gain}
\neq
\text{Semantic Quality Gain}.
}
$$

---

# 39. Degeneration Pressure

如果每一代都偏好：

- 更容易學；
- 更短；
- 更高成功率；

但沒有足夠 grounding constraints，

語言可能：

$$
\boxed{
\text{compress toward degenerate conventions}.
}
$$

因此 language evolution 需要：

- world grounding；
- semantic coverage；
- novelty retention。

---

# 40. Population Turnover

動態 Agent population：

$$
P_t
$$

也會影響語言。

新 Agent 進入：

- 需要 learnability；
- 可能推動 regularization。

舊 Agent 留存：

- 提供 continuity；
- 抑制 drift。

---

# 41. 2026 Plasticity Result

CoNLL 2026 的研究顯示：

- static populations 可形成 shared languages；
- population turnover 後，age-based plasticity 顯著降低 drift；
- uniformly low plasticity 無法快速整合 newcomers；
- uniformly high plasticity 則語言變化太快，stable conventions 難形成。

這提供一個直接的 dynamic-language boundary：

$$
\boxed{
\text{Plasticity}
\leftrightarrow
\text{Stability}.
}
$$

---

# 42. 語言層的 Stability–Plasticity Tradeoff

定義：

$$
\pi_t
$$

為平均 language plasticity。

太低：

$$
\pi_t\downarrow
\Rightarrow
Adaptation\downarrow.
$$

太高：

$$
\pi_t\uparrow
\Rightarrow
Drift\uparrow.
$$

因此存在：

$$
\boxed{
\pi^*.
}
$$

---

# 43. Operator Version Plasticity

不是所有 operator 都應同樣可塑。

可以：

### Core
低 plasticity。

### Experimental
高 plasticity。

### Ephemeral
極高 plasticity。

這和 RLMM 方法論版本治理相接。

---

# 44. Frequency 不是單一演化驅動

2025 EMNLP 的 frequency-compositionality 研究顯示，人工 communication system 中 compositionality 並不是 frequency 本身的固有結果；limited exposure 是重要驅動因素。

因此 dynamic COL 不能簡化成：

> 高頻 → macro；低頻 → composition。

真正是：

$$
\boxed{
\text{Frequency}
+
\text{Exposure}
+
\text{Task Pressure}
+
\text{Transmission}.
}
$$

---

# 45. Frequency Threshold 必須動態

前篇的 macro threshold：

$$
f^*
$$

應改成：

$$
\boxed{
f^*(t)
=
f(
Agent,
Domain,
Exposure,
Risk,
Drift
).
}
$$

---

# 46. Hysteresis：加入與刪除不應用同一門檻

若 operator：

$$
O
$$

剛因：

$$
\Delta J>\tau_{add}
$$

加入。

使用量稍微下降就立即刪除，

會造成：

$$
\boxed{
\text{Operator Churn}.
}
$$

因此應有：

$$
\tau_{remove}
<
\tau_{add}.
$$

---

# 47. Operator Hysteresis

定義：

$$
\boxed{
\begin{cases}
Add(O), & U_O>\tau_{add}\\
Keep(O), & \tau_{remove}\le U_O\le\tau_{add}\\
Retire(O), & U_O<\tau_{remove}.
\end{cases}
}
$$

這就是：

$$
\boxed{
\text{Operator Hysteresis}.
}
$$

---

# 48. 為什麼 Hysteresis 重要？

沒有 hysteresis：

$$
O
\rightarrow
add
\rightarrow
remove
\rightarrow
add
\rightarrow\cdots
$$

會增加：

- version burden；
- training instability；
- semantic drift；
- user confusion。

---

# 49. Interval Hysteresis

不只是 operator 個體。

整個：

$$
I_{\mathcal O}^{D}(t)
$$

也可能有 path dependence。

即同樣：

$$
\Theta
$$

從 expansion 方向進入，

與從 compression 方向進入，

得到的 language state 不同。

---

# 50. Path Dependence

形式：

$$
\boxed{
\mathcal O_t
\neq
f(\Theta_t)
}
$$

單獨決定。

而是：

$$
\boxed{
\mathcal O_t
=
f(
\Theta_t,
H_{0:t}
).
}
$$

其中：

$$
H_{0:t}
$$

是演化歷史。

---

# 51. Dynamic Optimum 也可能有切換成本

即使：

$$
N^*(t)
$$

改變，

立刻把語言改到新 optimum 可能不划算。

因為：

$$
C_{migration}.
$$

所以真正 policy：

$$
\boxed{
N_{policy}(t)
\neq
N^*(t)
}
$$

可能成立。

---

# 52. Inertia

語言可能維持在略次優區：

$$
J(N)<J(N^*)
$$

但避免巨大 migration cost。

這是：

$$
\boxed{
\text{Language Inertia}.
}
$$

---

# 53. Migration-Adjusted Objective

可寫：

$$
\boxed{
J_D
=
J_{current}
-
C_{migration}
-
C_{retraining}
-
C_{compatibility}.
}
$$

只有新版本 gain 足夠大才切換。

---

# 54. Dynamic Basis State

完整 operator 狀態可以：

$$
\boxed{
\mathcal B_t
=
(
\mathcal O_t,
G_t,
H_t,
R_t,
V_t
).
}
$$

其中：

- $\mathcal O_t$：operator set；
- $G_t$：grammar；
- $H_t$：hierarchy；
- $R_t$：retriever；
- $V_t$：version map。

---

# 55. State Transition

語言演化：

$$
\boxed{
\mathcal B_{t+1}
=
\mathcal F(
\mathcal B_t,
Workload_t,
Failure_t,
Novelty_t,
Agent_t
).
}
$$

---

# 56. 五種基本演化操作

### Birth

新增 operator。

### Crystallize

高頻 motif 升格。

### Merge

重疊 operators 合併。

### Split

God Operator / ambiguous operator 拆分。

### Retire

低效、過時 operator 退出 stable set。

---

# 57. 再加入第六種：Reground

若語義漂移：

$$
Meaning(O_t)
\neq
TargetMeaning,
$$

不一定刪除。

可以：

$$
\boxed{
Reground(O).
}
$$

重新把 operator 接回：

- examples；
- world behavior；
- formal expansion。

---

# 58. 語義漂移率

定義：

$$
\boxed{
D_{drift}(O;t_1,t_2)
=
D(
Sem_{t_1}(O),
Sem_{t_2}(O)
).
}
$$

整體：

$$
\boxed{
\bar D_{drift}(t)
=
\mathbb E_O[D_{drift}(O)].
}
$$

---

# 59. Drift Budget

要求：

$$
\boxed{
\bar D_{drift}(t)
\le
B_D.
}
$$

超過則：

- freeze；
- reground；
- rollback；
- branch version。

---

# 60. Dynamic Nmax 受 Drift 影響

operator 越多、版本越多、population 越不穩，

drift-control cost 越大。

因此：

$$
D_{drift}\uparrow
\Rightarrow
N_{\max}\downarrow
$$

可能成立。

---

# 61. Dynamic Nmin 也受 Drift 影響

如果 primitives 本身語義不穩，

可能需要更多：

- disambiguation；
- version markers；
- explicit constraints。

因此：

$$
D_{drift}\uparrow
\Rightarrow
N_{\min}^{robust}\uparrow.
$$

所以 drift 會從兩邊擠壓 interval。

---

# 62. Drift-Induced Interval Compression

因此：

$$
\boxed{
D_{drift}\uparrow
\Rightarrow
W_I(t)\downarrow
}
$$

是非常重要的候選命題。

---

# 63. Dynamic Interval Stability

定義：

$$
\boxed{
S_I(t)
=
-\left|
\frac{dN_{\min}}{dt}
\right|
-
\left|
\frac{dN_{\max}}{dt}
\right|.
}
$$

更高代表 interval 邊界變動慢。

但穩定不代表好。

---

# 64. Stable but Bad Interval

如果：

$$
I(t)
=
[500,510]
$$

長期穩定，

但 Agent 學習成本極高，

仍不是好語言。

所以要同時報：

- interval stability；
- interval location；
- interval width；
- peak utility。

---

# 65. Optimal-Point Velocity

定義：

$$
\boxed{
v_{N^*}
=
\frac{dN^*}{dt}.
}
$$

如果：

$$
|v_{N^*}|
$$

很大，

表示語言需求變化快，

不適合頻繁 hard-code stable operators。

---

# 66. Ephemeral Layer 應吸收高速變動

當：

$$
|v_{N^*}|\uparrow,
$$

更多新 operators 應留在：

$$
\boxed{
\text{Ephemeral / Experimental Layer}
}
$$

而不是立即進 Stable Core。

---

# 67. Stable Core 應吸收低速變動

只有在 utility 長期穩定：

$$
U_O(t)>\tau
$$

持續窗口：

$$
W,
$$

才進：

$$
\boxed{
\text{Stable Core}.
}
$$

---

# 68. Promotion Delay

定義：

$$
\boxed{
T_{promote}(O)
}
$$

從 operator birth 到進 stable layer 所需時間。

如果太短：

- noise 被永久化。

太長：

- 好 operator 無法傳播。

存在：

$$
T_{promote}^*.
$$

---

# 69. Retirement Delay

同樣：

$$
\boxed{
T_{retire}(O)
}
$$

避免 temporary usage dip 就刪除 operator。

這和 hysteresis 一致。

---

# 70. Dynamic Completeness 不是每次都重新從零算

實際 runtime 不會每秒全局 optimization。

需要：

$$
\boxed{
\text{incremental adaptation}.
}
$$

每次只處理：

- new failure；
- new motif；
- new domain；
- stale operator；
- retriever change。

---

# 71. Incremental Update Rule

第一版：

$$
\boxed{
\mathcal B_{t+1}
=
\mathcal B_t
+
\Delta_{birth}
+
\Delta_{crystal}
+
\Delta_{split}
-
\Delta_{merge}
-
\Delta_{retire}.
}
$$

注意 merge 可能不單純是「減一」，實際是 graph transformation。

---

# 72. Stability Gate

每次 update 後需要測：

- coverage；
- held-out composition；
- selection；
- fidelity；
- drift；
- migration compatibility。

若破壞 stable invariants：

$$
\boxed{
Rollback.
}
$$

---

# 73. Dynamic Completeness 的核心不是追最佳點

如果每次都追：

$$
N^*(t),
$$

可能造成：

$$
\boxed{
\text{Over-Adaptive Language}.
}
$$

因此真正目標是：

> **維持在高效可行區，而不是每一刻精準站在數學 optimum。**

---

# 74. Viability Band

定義：

$$
\boxed{
V_{\tau}(t)
=
\{
N:
J(N,t)\ge
J(N^*,t)-\tau
\}.
}
$$

只要語言維持：

$$
N(t)\in V_{\tau}(t),
$$

就不必頻繁重構。

---

# 75. 這比追 N* 更穩健

因為：

- 減少 migration；
- 減少版本 churn；
- 提高跨 Agent compatibility。

因此：

$$
\boxed{
\text{Good dynamic governance}
=
\text{stay inside a viability band}.
}
$$

---

# 76. Dynamic Completeness Interval vs Viability Band

不要混淆：

### Completeness Interval

$$
I_{\mathcal O}^{D}(t)
$$

表示可接受的最大範圍。

### Viability Band

$$
V_{\tau}(t)
$$

表示接近最佳的甜蜜區。

所以：

$$
\boxed{
V_{\tau}(t)
\subseteq
I_{\mathcal O}^{D}(t).
}
$$

---

# 77. 語言治理的真正目標

不是：

> 把 operator 數永遠固定在 64。

而是：

$$
\boxed{
\mathcal O_t
\text{ remains inside }
V_{\tau}(t)
}
$$

同時：

- drift bounded；
- migration bounded；
- compatibility preserved。

---

# 78. Dynamic Completeness 的十二個正式命題

## DC-P1 — Agent-Learning Contraction

Agent composition ability 提高時， $N_{\min}$ 可下降。

## DC-P2 — Domain-Expansion Pressure

target domain 擴張通常推高 $N_{\min}$。

## DC-P3 — Retrieval-Expanded Upper Bound

retrieval / routing 改善可推高 $N_{\max}$。

## DC-P4 — Drift Compression

semantic drift 同時推高 robust lower bound 並壓低 upper bound，縮小 interval。

## DC-P5 — Crystallization–Consolidation Distinction

macro crystallization 不必然減少 vocabulary；consolidation 才可能造成 cardinality compression。

## DC-P6 — Multi-Form Compression

cardinality、context、cognitive compression 必須分開。

## DC-P7 — Lifecycle Archetype

operator languages 可能出現 expansion → saturation → compression → re-expansion 的循環。

## DC-P8 — Plasticity–Stability Optimum

dynamic population 中存在 nontrivial language-plasticity optimum。

## DC-P9 — Hysteretic Governance

operator admission 與 retirement 應使用不同 threshold 以避免 churn。

## DC-P10 — History Dependence

同一當前環境可能因不同演化歷史得到不同有效 language state。

## DC-P11 — Viability-over-Optimality

動態語言治理應優先維持 viability band，而非持續追逐瞬時 optimum。

## DC-P12 — Interval Collapse Trigger

若 $N_{\min}>N_{\max}$，需要 architecture change，而不是單純調整 vocabulary size。

---

# 79. 第一版實驗設計：Dynamic Domain Sweep

起始 domain：

$$
\Omega_0.
$$

逐步加入：

$$
\Omega_1,
\Omega_2,\ldots
$$

每一階量：

- $N_{\min}$ ；
- $N^*$ ；
- $N_{\max}$ ；
- depth；
- fidelity；
- active set；
- drift。

觀察：

$$
I_{\mathcal O}^{D}(t).
$$

---

# 80. Agent Learning Sweep

固定 domain，

但讓 Agent 經：

$$
E_0,E_1,\ldots,E_k
$$

不同 exposure / training。

觀察是否：

$$
N_{\min}(t)\downarrow.
$$

這可直接測 Internalization Compression。

---

# 81. Retriever Upgrade Sweep

固定：

$$
N_G.
$$

逐步提升：

- embedding retriever；
- reasoning retriever；
- multi-step planner；
- hierarchy。

觀察：

$$
N_{\max}(t).
$$

---

# 82. Population Turnover Sweep

建立 Agent population。

每隔：

$$
k
$$

步換入 newcomer。

比較：

- uniform high plasticity；
- uniform low plasticity；
- age-based / staged plasticity。

量：

$$
D_{drift}
$$

與：

$$
K_{\epsilon}^{stable}.
$$

---

# 83. Iterated Transmission Sweep

每代只讓下一 Agent 接觸前一代語言的一部分。

量：

- learnability；
- vocabulary size；
- compositionality；
- semantic coverage；
- degeneration。

這直接接 LRC–COL-09。

---

# 84. Hysteresis Experiment

設定 operator utility 隨 workload 緩慢上升、再下降。

比較：

### No Hysteresis
同一 threshold add/remove。

### Hysteresis
 $\tau_{add}>\tau_{remove}$。

量：

- churn；
- version count；
- performance；
- migration cost。

---

# 85. Expansion–Compression Cycle Test

設 workload：

### Phase A
快速加入新 motifs。

### Phase B
固定 workload。

### Phase C
長期重複。

### Phase D
再加入新 domain。

觀察：

$$
N_G(t),
N_A(t),
C_{lang}(t),
Y_L(t).
$$

若出現：

$$
Expansion
\rightarrow
Saturation
\rightarrow
Compression
\rightarrow
Re-expansion,
$$

則支持 lifecycle archetype。

---

# 86. 我們現在終於有「靜態值」和「動態區間」

靜態：

$$
\boxed{
I_{\mathcal O}^{S}
=
[
N_{\min}^{effective},
N_{\max}^{effective}
].
}
$$

動態：

$$
\boxed{
I_{\mathcal O}^{D}(t)
=
[
N_{\min}(t),
N_{\max}(t)
].
}
$$

最佳點：

$$
\boxed{
N^*(t).
}
$$

高效甜蜜區：

$$
\boxed{
V_{\tau}(t).
}
$$

---

# 87. 最初問題的正式回答

最初問：

> 「應該會有一個靜態跟動態的範圍值區間嗎？」

本文的答案是：

$$
\boxed{
\text{Yes, as a useful research model.}
}
$$

但它不是物理常數。

它是條件化於：

$$
\boxed{
Agent
+
Domain
+
Workload
+
Runtime
+
Retrieval
+
Population
+
Risk
+
History.
}
$$

---

# 88. 更重要的結果

未來真正好的 language runtime 不應只知道：

> 我現在有 80 個 operator。

而應知道：

```text
Current Global Library:
Current Active-Set Distribution:
Estimated Nmin:
Estimated Nmax:
Estimated N*:
Viability Band:
Drift Rate:
Birth Rate:
Retirement Rate:
Migration Cost:
```

也就是：

$$
\boxed{
\text{Language Self-Monitoring}.
}
$$

---

# 89. 這已經接近 Operator Ecology Runtime

一套動態 COL 最後看起來不只是 parser。

它更像：

$$
\boxed{
\text{Operator Ecology Manager}.
}
$$

管理：

- birth；
- learning；
- crystallization；
- competition；
- merge；
- split；
- drift；
- retirement。

---

# 90. 與 LRC 的最終接合

語言 operator ecology 的改變最後會影響：

$$
Y_L(t)
$$

與：

$$
\kappa_{LR}(t).
$$

因此動態語言設計不是內部 elegance。

它最後會改變：

> **同一單位語言在不同時代到底能可靠地做多少事。**

---

# 91. 本篇核心公式組

動態 interval：

$$
\boxed{
I_{\mathcal O}^{D}(t)
=
[
N_{\min}(t),
N_{\max}(t)
].
}
$$

dynamic optimum：

$$
\boxed{
N^*(t)
=
\arg\max_NJ(N;\Theta_t).
}
$$

interval width：

$$
\boxed{
W_I(t)
=
N_{\max}(t)-N_{\min}(t).
}
$$

operator birth-death：

$$
\boxed{
\dot N_G
=
B_t-D_t.
}
$$

hysteresis：

$$
\boxed{
\begin{cases}
Add,& U>\tau_{add}\\
Keep,& \tau_{remove}\le U\le\tau_{add}\\
Retire,& U<\tau_{remove}.
\end{cases}
}
$$

viability band：

$$
\boxed{
V_{\tau}(t)
=
\{
N:
J(N,t)\ge
J(N^*,t)-\tau
\}.
}
$$

---

# 92. 非主張

本文不主張：

1. 所有語言都必然出現四階段 lifecycle；
2. $N_{\min}$ 隨 Agent 學習一定單調下降；
3. $N_{\max}$ 隨模型進步一定單調上升；
4. operator count 足以描述 language evolution；
5. iterated transmission 必然改善 compositionality；
6. high plasticity 一定不好；
7. hysteresis threshold 有通用固定值；
8. dynamic optimum 值得每次追蹤到精確最大值；
9. global operator library 可以無限成長；
10. 本篇 phenomenological differential equations 已被實證。

本文只提出：

$$
\boxed{
\text{The effective size of a composite operator language should be modeled as a moving viability interval shaped by agent learning, domain expansion, retrieval capacity, semantic drift, population dynamics, and historical path dependence.}
}
$$

---

# 93. 文獻錨點

1. **Searching for Structure: Investigating Emergent Communication with Large Language Models（COLING 2025）**  
   模擬 LLM 代際學習 artificial languages；結果顯示 generational transmission 可以提高 learnability，但同時可能形成 non-humanlike degenerate vocabularies。這支持「傳播與壓縮不等於單調改善」。

2. **Frequency & Compositionality in Emergent Communication（EMNLP 2025）**  
   指出 compositionality 並非 frequency 本身的固有結果，limited exposure 是重要驅動；支持 dynamic macro policy 必須同時考慮 exposure 與 task pressure。

3. **Cognitively Inspired Developmental Trajectories Improve Explore-Exploit Dynamics in Neural Agent Emergent Communication（CoNLL 2026）**  
   在 dynamic population turnover 中，age-based plasticity 顯著降低 language drift；uniform low plasticity 適應 newcomer 太慢，而 uniform high plasticity 使語言變動過快、穩定 convention 難形成。這直接支持本文的 stability–plasticity dynamic。

4. **ToolScope: Enhancing LLM Agent Tool Use through Tool Merging and Context-Aware Filtering（ACL 2026）**  
   大型 toolsets 中的 redundancy / overlap / context limits 可藉 merging 與 filtering 改善，支持 runtime architecture 可以移動 $N_{\max}^{effective}$。

5. **ToolDreamer: Instilling LLM Reasoning Into Tool Retrievers（EACL 2026）**  
   指出 large tool collections 不能全部放入 context，需要 external retrieval，而 query 與 tool-description language space 的 alignment 會直接影響 retrieval quality。支持 retriever 作為 dynamic upper-bound factor。

6. **Beyond Single-Shot: Multi-step Tool Retrieval via Query Planning（ACL Findings 2026）**  
   對 massive dynamic tool libraries，以 iterative query planning 處理 compositional retrieval，比 static single-shot matching 更適合複雜任務。支持「operator library 規模與 retrieval architecture 必須聯合建模」。

7. **ToolOmni: Enabling Open-World Tool Use via Agentic Learning with Proactive Retrieval and Grounded Execution（ACL 2026）**  
   直接研究 massive and evolving tool repositories 下的 open-world tool retrieval / execution，支持 $N_G(t)$ 本身就是動態量，而不能視為靜態 vocabulary。

---

# 94. 下一篇

## LRC–COL-07：AI 學習時間
### 從記憶符號到操作理解
### AI Learning Time: From Symbol Recall to Operational Understanding

下一篇正式處理最初命題空間中的：

$$
\boxed{
T_{\epsilon}^{learn}.
}
$$

將區分：

- symbol recognition；
- definition recall；
- familiar composition；
- novel composition；
- cross-domain transfer；
- execution fidelity；
- retention；
- re-learning。

並回答：

> **到底看到幾次、用幾次、經過多少不同 composition，才有資格說 AI「理解」了一個複合算子？**

同時建立：

$$
\boxed{
\text{Exposure}
\rightarrow
\text{Acquisition}
\rightarrow
\text{Generalization}
\rightarrow
\text{Operational Understanding}
}
$$

的學習曲線，而不是把「能複述定義」當成學會。

**END — LRC–COL-06 v0.1**
