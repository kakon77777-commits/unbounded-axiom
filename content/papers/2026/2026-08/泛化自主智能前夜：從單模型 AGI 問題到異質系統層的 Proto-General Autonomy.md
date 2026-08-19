# Series C / Paper 08
# 泛化自主智能前夜：從單模型 AGI 問題到異質系統層的 Proto-General Autonomy
## The Eve of Proto-General Autonomous Intelligence: From the Single-Model AGI Question to Heterogeneous System-Level General Autonomy

版本：v0.1  
日期：2026-08-14  
狀態：Theory + systems criterion + executable structural checker paper

## 摘要

「某一個模型是否已經是 AGI？」將模型能力、工具能力、持久記憶、驗證系統、Agent harness、組織結構與人類治理壓縮成單一問題，因而容易忽略當代 agentic AI 的實際計算單位已逐步由單一模型轉向異質系統。本文提出 **Proto-General Autonomous Intelligence（PGAI，泛化自主智能原型態）** 作為一個較弱、可測量、且明確不等同於 AGI 已實現的系統層概念。

令一個 agentic intelligence system 為：

$$
\mathfrak G
=
(
\mathcal M,
\mathcal A,
\mathcal T,
\mathcal K,
\mathcal V,
\mathcal H,
\mathcal O,
\mathcal R,
\mathcal B
),
$$

其中：
- $\mathcal M$：foundation / specialist models；
- $\mathcal A$：agents；
- $\mathcal T$：tools and action interfaces；
- $\mathcal K$：persistent memory / knowledge state；
- $\mathcal V$：verification and epistemic carriers；
- $\mathcal H$：harness / orchestration；
- $\mathcal O$：organizational structure；
- $\mathcal R$：resource and recovery mechanisms；
- $\mathcal B$：governance / bounded-autonomy constraints。

本文將 proto-general autonomy 分解為八個必要維度：

$$
\mathbf P
=
(
G,
T,
C,
H,
V,
M,
O,
B
),
$$

分別代表 domain generality、cross-domain transfer、evidence-sensitive closure、long-horizon persistence、verification / self-correction、memory continuity、organizational composability 與 bounded governability。本文採用 bottleneck criterion：

$$
P_{\min}
=
\min
\{
G,T,C,H,V,M,O,B
\}.
$$

此設計刻意避免「某一個 benchmark 很強」補償另一個關鍵維度近乎不存在。

本文證明四個基礎結果。

第一，**Generality–Autonomy Orthogonality Proposition**：一個系統可以具有高 domain breadth 但低 autonomy，也可以高度 autonomous 但只在單一 domain 中有效；因此 generality 與 autonomy 是不同軸，不能由其中一者推出另一者。

第二，**Compositional Capability Expansion Theorem**：若不同 components 具有互補 capability sets，且 router 能在對應 tasks 上選擇可解 component，則 system capability set 至少包含 components capability sets 的聯集；只要不存在單一 component 覆蓋全部聯集，system coverage 嚴格大於任一 component。若再允許 sequential composition，system 甚至可解沒有任何單一 component 可獨立完成的 composite tasks。

第三，**Long-Horizon Fragility Proposition**：在最簡 independent-step model 中，若單步成功率為 $p<1$，長度 $L$ 的不可恢復 trajectory 成功率為：

$$
P_{\mathrm{succ}}(L)
=
p^L,
$$

故即使單步可靠性很高，長程成功率也會快速衰減。這解釋了為何 long-horizon autonomy 不能由短任務 benchmark 直接外推。

第四，**Checkpoint-Recovery Improvement Proposition**：若任務可拆為 $k$ 個 segments，每段失敗後可在 bounded retry budget 內從最近 checkpoint 重試，則在相同單次 segment 成功率下，整體成功率高於只允許每段一次嘗試的 open-loop execution。此結果形式化了 memory、verification、rollback 與 recovery 對長程 autonomy 的結構價值。

2026 年的公開評估已逐步接近這種多維視角。AgencyBench 以 6 種核心 agentic capabilities、32 個 real-world scenarios、138 tasks 測量高 tool-call、高 context、hours-scale execution；CUBE 試圖以一致 interface 統一分散的 agent benchmarks，明確討論 generalist agent 跨 benchmark 的可移植性；AgentVista 涵蓋 7 categories、25 sub-domains 的 multimodal generalist-agent tasks；Agents-A1 將六個異質領域與平均 45K-token long-horizon trajectories 統一到單一 deployable agent。另一方面，HORIZON 與 Long-Horizon-Terminal-Bench 都強調長依賴序列仍是 frontier agents 的主要失敗來源；METR 的 task-completion time horizon 則將「能完成多長的人類工作尺度任務」變成獨立測量軸，而不是只看 benchmark accuracy。

系統層跡象同樣重要。Codex 2026 的產品與使用資料顯示 multi-agent parallel work、long-running tasks 與 knowledge-work artifacts 正被整合進統一工作環境；AlphaEvolve 已在數學、計算機科學與 Google infrastructure 中使用 LLM ensemble 加 automated evaluators 形成 unattended search-and-verification loop；Co-Scientist 以多 Agent 方式持續生成、批判與演化研究 hypothesis。Emergence World 則開始直接以跨 vendor、長時間、多工具、持久記憶的 shared world 研究 multi-agent autonomy 與 governance dynamics。

因此本文提出「AGI 前夜」的較弱系統命題：

$$
\boxed{
\text{The first practically observable precursor of general autonomous intelligence
need not be a single universally capable model.}
}
$$

它可能先以異質系統形式出現：

$$
\boxed{
\text{models}
+
\text{agents}
+
\text{tools}
+
\text{memory}
+
\text{verification}
+
\text{organization}
+
\text{governance}
}
$$

並在有限但持續擴大的 domain set 中表現出可遷移、可修正、可長程維持的自主閉環。本文將這種狀態稱為 PGAI，而把是否達到 AGI 留作另一個更強、目前不由本文判定的問題。

**關鍵詞：** proto-general autonomy；AGI；agentic AI；generalist agents；long-horizon agents；system composition；verification；cross-domain transfer；bounded autonomy；heterogeneous intelligence

---

## 1. 為什麼單模型問題開始不夠？

傳統提問：

> 模型 $M$ 是不是 AGI？

隱含計算單位為：

$$
M.
$$

但今日實際 agentic system 往往是：

$$
\boxed{
M
+
\text{tools}
+
\text{memory}
+
\text{environment}
+
\text{harness}.
}
$$

更大的 multi-agent system 則變成：

$$
\boxed{
\mathfrak G
=
(
\mathcal M,
\mathcal A,
\mathcal T,
\mathcal K,
\mathcal V,
\mathcal H,
\mathcal O,
\mathcal R,
\mathcal B
).
}
$$

因此 observable capability 更接近：

$$
\operatorname{Cap}(\mathfrak G)
$$

而不是：

$$
\operatorname{Cap}(M).
$$

這不是語義遊戲。

Paper 04–07 已經逐步指出：
- execution 改變 claim 的可驗證性；
- memory 改變長程 closure；
- multi-agent organization 改變 collective outcomes；
- governance / topology 改變 delegation 與 reliability。

所以如果最終工作能力來自整個：

$$
\mathfrak G,
$$

只問單一 $M$ 會漏掉真正的部署單位。

---

## 2. 本文不定義 AGI

本文刻意不提出：

$$
\boxed{
\text{AGI threshold}=x.
}
$$

原因是「AGI」同時可能包含：
- human-level breadth；
- economic substitutability；
- open-world reasoning；
- embodiment；
- autonomy；
- learning；
- social competence；
- recursive improvement；

不同社群並沒有唯一 operational definition。

本文只定義較弱對象：

$$
\boxed{
\textbf{Proto-General Autonomous Intelligence}.
}
$$

### Proto

表示：
- generality 有限；
- domain set 有界；
- reliability 不完備；
- human governance 仍存在；
- open-world coverage 尚不完整。

### General

表示：
- 不被單一狹窄 task family 限定；
- 能在多 domain / tool / representation 間遷移。

### Autonomous

表示：
- 能在 bounded authority 下持續選擇 actions；
- evidence 可改變 future policy；
- 不需要人類逐步指定每個 micro-action。

---

## 3. PGAI System

定義：

$$
\mathfrak G
=
(
\mathcal M,
\mathcal A,
\mathcal T,
\mathcal K,
\mathcal V,
\mathcal H,
\mathcal O,
\mathcal R,
\mathcal B
).
$$

### $\mathcal M$：Models

generalist / specialist reasoning components。

### $\mathcal A$：Agents

將 models 與 goals、tools、state、policies 綁定的 active processes。

### $\mathcal T$：Tools

browser、terminal、code executor、database、API、simulation、sensor。

### $\mathcal K$：Persistent Knowledge State

memory、artifacts、task state、negative results、institutional knowledge。

### $\mathcal V$：Verification

tests、formal checkers、peer agents、external evidence、epistemic certificates。

### $\mathcal H$：Harness

planning、routing、context management、retry、compaction、task state。

### $\mathcal O$：Organization

roles、delegation、review topology、coordination protocol。

### $\mathcal R$：Resources / Recovery

compute、time、rollback、checkpoint、replacement。

### $\mathcal B$：Bounds / Governance

permissions、approvals、budget、safety policy、escalation。

---

## 4. 八維 PGAI Vector

定義：

$$
\boxed{
\mathbf P
=
(
G,
T,
C,
H,
V,
M,
O,
B
)
}
$$

且：

$$
0\leq P_i\leq1.
$$

### $G$：Domain Generality

系統能獨立完成的 task / domain breadth。

### $T$：Transferability

換 domain、tool、task representation 或 harness 後，不靠人工重新工程仍能遷移策略的程度。

### $C$：Autonomous Closure

是否存在 Paper 05 的：

$$
\text{evidence}
\rightarrow
\text{epistemic state}
\rightarrow
\text{future policy}.
$$

### $H$：Horizon Persistence

在長時間、長 dependency chain 中維持 goal / state / error recovery 的能力。

### $V$：Verification Capacity

能否主動：
- test；
- counterexample；
- cross-check；
- rollback；
- revise。

### $M$：Memory Continuity

是否保留：
- prior attempts；
- negative evidence；
- provenance；
- task state；
跨長程 episode 有效利用。

### $O$：Organizational Composability

多個 Agents / specialists 能否：
- delegate；
- coordinate；
- integrate；
- replace；
形成大於單一 component 的工作能力。

### $B$：Bounded Governability

能否在：
- permission；
- audit；
- budget；
- escalation；
- revocation；

下持續自主，而不是只在完全 unrestricted 或完全 human-stepped 條件下工作。

---

## 5. 為什麼用 Bottleneck 而不是平均？

定義：

$$
\boxed{
P_{\min}
=
\min
\{
G,T,C,H,V,M,O,B
\}.
}
$$

若某系統：

$$
G=0.95,
\quad
V=0.95,
$$

但：

$$
C=0,
$$

它可能是極強 general assistant，

卻不是 autonomous system。

反之：

$$
C=0.95,
\quad
H=0.9,
$$

但：

$$
G=0.05,
$$

它可能是極強 domain-specific autonomous optimizer，

卻不是 proto-general。

因此 arithmetic mean 可能掩蓋缺失的必要軸。

---

## 6. Generality–Autonomy Plane

令：

$$
G^\star
$$

表示 aggregate generality，

$$
A^\star
$$

表示 aggregate autonomy。

形成四象限。

### Quadrant I：Narrow + Low Autonomy

傳統 narrow software / simple assistant。

### Quadrant II：Broad + Low Autonomy

廣泛回答問題，但主要由人類逐步驅動。

### Quadrant III：Narrow + High Autonomy

單一 domain 的 autonomous optimizer / trading / coding / laboratory agent。

### Quadrant IV：Broad + High Autonomy

PGAI 的候選區域。

因此：

$$
\boxed{
\text{generality}
\perp
\text{autonomy}
}
$$

概念上必須先拆開。

---

## 7. 命題 1：Generality–Autonomy Orthogonality

### 命題

存在系統：

$$
S_1
$$

具有高 generality、低 autonomy；

也存在：

$$
S_2
$$

具有低 generality、高 autonomy。

因此 generality 不能推出 autonomy，autonomy 也不能推出 generality。

### 證明

構造即可。

令 $S_1$ 能回答多 domain tasks，但每一步 action 由 human 指定，因此：

$$
G(S_1)\gg0,
\qquad
C(S_1)=0.
$$

令 $S_2$ 能在單一 formal optimization domain 中長時間自主搜索、驗證與修正，但不能遷移到其他 domains，因此：

$$
C(S_2)\gg0,
\qquad
G(S_2)\approx0.
$$

兩個反例分別否定兩個方向的蘊含。

證畢。

---

## 8. Generalist Agent 評估正在變成獨立問題

AgencyBench 2026 不只測一個 agent skill。

其 benchmark 包含：
- 6 core agentic capabilities；
- 32 real-world scenarios；
- 138 tasks；
- 平均約 90 tool calls；
- 1M-token contexts；
- hours-scale execution。

其結果也明確看到：
- feedback-driven self-correction 差異；
- resource efficiency 差異；
- tool-use preference；
- native agentic scaffold effect。

這說明：

$$
\boxed{
\text{generalist autonomy}
}
$$

已不能只用單一 QA accuracy 表示。

---

## 9. Benchmark Unification 與 Generality

CUBE 2026 的核心動機之一，是 agent benchmarks 的：
- action spaces；
- observations；
- task formats；
- tool interfaces；

高度碎片化。

它提出統一 benchmark interface 的原因正是：

> 若 generalist agent 真具 general capability，則在給予正確 tools 與一致 interface 後，應能跨不同 benchmark family 工作。

所以：

$$
\boxed{
\text{cross-benchmark portability}
}
$$

本身開始成為 generality 的測量概念。

---

## 10. 多模態 Generalist Breadth

AgentVista 2026 將 generalist multimodal agent 評估擴展到：

$$
25
$$

個 sub-domains、

$$
7
$$

類 categories。

這代表「general agent」不再只意味：
- browser；
- code；

也包括：
- visual perception；
- mixed modalities；
- interaction；
- long sequences。

因此 PGAI 的 $G$ 必須是 domain / modality breadth，而不是純文字知識範圍。

---

## 11. Cross-Domain Training 不等於 Cross-Domain Autonomy

Agents-A1 2026 將：

$$
6
$$

個 heterogeneous domains

透過：
- full-domain supervised fine-tuning；
- domain teacher models；
- multi-teacher on-policy distillation；

統一到單一 deployable agent。

其 training trajectories 平均長度約：

$$
45K
$$

tokens。

這是 generalist-agent scaling 的明確案例。

但：

$$
\boxed{
\text{cross-domain competence}
\nRightarrow
\text{cross-domain autonomous closure}.
}
$$

模型可能在很多 benchmarks 得分高，但如果每個新 domain 都需要外部人類重做 workflow / verifier / decomposition，則 $T$ 或 $C$ 仍可能低。

---

## 12. Transferability

令 training / design domain 集合：

$$
\mathcal D_{\mathrm{seen}}.
$$

unseen domain：

$$
d^\star
\notin
\mathcal D_{\mathrm{seen}}.
$$

定義 reconfiguration cost：

$$
C_{\mathrm{reconfig}}(
d^\star
).
$$

可將 transfer score 寫成：

$$
T
=
\mathbb E_{d^\star}
\left[
Q(d^\star)
\exp(
-\lambda
C_{\mathrm{reconfig}}(d^\star)
)
\right].
$$

其中：
- $Q(d^\star)$：新 domain performance；
- $C_{\mathrm{reconfig}}$：需要多少人工 prompt / code / schema / workflow 重寫。

所以真正 generalist system 不只是：

$$
Q(d^\star)>0,
$$

還要求：

$$
C_{\mathrm{reconfig}}
$$

不能無界增長。

---

## 13. Compositional Capability Sets

令 task universe：

$$
\mathcal U.
$$

component $i$ 可可靠解決的 task set：

$$
C_i
\subseteq
\mathcal U.
$$

若 system router：

$$
R:
\mathcal U
\rightarrow
\{1,\ldots,n\}
$$

能對：

$$
u\in C_i
$$

選擇一個 capable component，

則 system 單步 capability set：

$$
C_{\mathrm{sys}}
$$

至少包含：

$$
\bigcup_iC_i.
$$

---

## 14. 定理 2：Compositional Capability Expansion

### 定理

若 router 對聯集中每個 task 都能選到 capable component，則：

$$
\bigcup_iC_i
\subseteq
C_{\mathrm{sys}}.
$$

若：

$$
\forall j,
\quad
C_j
\subsetneq
\bigcup_iC_i,
$$

則：

$$
\forall j,
\quad
C_j
\subsetneq
C_{\mathrm{sys}}
$$

至少在 coverage 意義上成立。

### 證明

任取：

$$
u
\in
\bigcup_iC_i.
$$

則存在某 $i$：

$$
u\in C_i.
$$

依 router 假設，system 選到某 capable component 並解決 $u$。

所以：

$$
u\in C_{\mathrm{sys}}.
$$

故：

$$
\bigcup_iC_i
\subseteq
C_{\mathrm{sys}}.
$$

若每個 $C_j$ 都是 union 的真子集，則 system 至少覆蓋 union，因此嚴格超過每個 component coverage。

證畢。

---

## 15. Sequential Composition

更強情況下，task：

$$
u^\star
$$

本身不屬於任何：

$$
C_i.
$$

但可分解：

$$
u^\star
=
u_1
\circ
u_2
\circ
\cdots
\circ
u_k
$$

其中：

$$
u_j
\in
C_{i_j}.
$$

若：
- decomposition 正確；
- interface compatible；
- state 可傳遞；
- verification 可檢查 intermediate artifacts；

則 system 可以完成：

$$
u^\star
$$

即使沒有任何單一 component 能獨立完成。

所以 system capability 可以來自：

$$
\boxed{
\text{composition}
}
$$

而不是 component 內部突然出現新權重。

這就是異質智能系統「整體能力大於單一成員 coverage」的最低數學形式。

---

## 16. 這不是神祕 Emergence

本文避免把每個 system-level gain 都稱為 emergence。

若：

$$
C_{\mathrm{sys}}
>
C_i
$$

只是因：
- router；
- tool；
- composition；

可完全從架構推導，

則它是：

$$
\boxed{
\text{compositional capability expansion}.
}
$$

只有出現無法由已知 component / topology 直接解釋的新 dynamics 時，才需要額外 emergent-behavior 分析。

---

## 17. Long Horizon 是另一條獨立軸

Agent 在 5-step task 表現：

$$
95\%
$$

不能直接推出 100-step task 也接近：

$$
95\%.
$$

HORIZON 2026 跨多個 agentic domains、models 收集 3100+ trajectories，專門分析 horizon-dependent degradation。

Long-Horizon-Terminal-Bench 也直接指出現有 terminal benchmarks 常把 tasks 壓縮到短時間 final outcome，忽略 intermediate progress 與長程 failure。

所以：

$$
\boxed{
H
}
$$

必須被獨立測量。

---

## 18. 命題 3：Long-Horizon Fragility

假設一個不可恢復 trajectory 有：

$$
L
$$

個必要 steps。

每步條件成功率固定：

$$
p,
\quad
0<p<1,
$$

並做最簡 independent approximation。

則：

$$
\boxed{
P_{\mathrm{succ}}(L)
=
p^L.
}
$$

### 證明

所有 $L$ steps 都成功才算完成。

由獨立性：

$$
P(
\cap_{i=1}^{L}S_i
)
=
\prod_{i=1}^{L}P(S_i)
=
p^L.
$$

證畢。

例如：

$$
p=0.99.
$$

若：

$$
L=10,
$$

有：

$$
0.99^{10}
\approx
0.904.
$$

若：

$$
L=100,
$$

則：

$$
0.99^{100}
\approx
0.366.
$$

所以：

$$
\boxed{
\text{high local reliability}
\nRightarrow
\text{high long-horizon reliability}.
}
$$

---

## 19. METR Time Horizon

METR 將 frontier agent ability 改寫為：

$$
T_{50},
$$

即：

> 對應某個人類專家工作時間長度的 tasks，agent 有 50% 成功率時的人類 task duration。

這個 measure 不等於：
- Agent 連續運行 wall-clock time；
- AGI；
- general autonomy。

但它把：

$$
\boxed{
\text{task horizon}
}
$$

變成獨立尺度。

這對 PGAI 很重要，因為 $G$ 與 $H$ 不能混成同一 benchmark score。

---

## 20. Checkpoint / Recovery

長程 system 不應是：

$$
\text{start}
\rightarrow
\cdots
\rightarrow
\text{fail}
\rightarrow
\text{restart all}.
$$

而應使用：

$$
\boxed{
\text{checkpoint}
+
\text{verification}
+
\text{rollback}
+
\text{retry}.
}
$$

令任務分成：

$$
k
$$

段。

每段單次成功率：

$$
s.
$$

每段最多允許：

$$
r
$$

次 attempts。

則每段在 retry budget 內成功率：

$$
s_r
=
1-(1-s)^r.
$$

如果 segments 成功 events 近似獨立，整體成功率：

$$
P_{\mathrm{rec}}
=
\left[
1-(1-s)^r
\right]^k.
$$

---

## 21. 命題 4：Checkpoint-Recovery Improvement

若：

$$
0<s<1
$$

且：

$$
r>1,
$$

則：

$$
1-(1-s)^r
>
s.
$$

因此：

$$
\left[
1-(1-s)^r
\right]^k
>
s^k.
$$

### 證明

因：

$$
0<1-s<1.
$$

若 $r>1$：

$$
(1-s)^r
<
1-s.
$$

所以：

$$
1-(1-s)^r
>
s.
$$

兩邊對正整數 $k$ 次方保持不等式。

證畢。

這不表示 unlimited retry 最佳。

retry 仍有：
- cost；
- correlated failure；
- bad specification；
- livelock。

但它證明 recovery architecture 對 long-horizon robustness 具有結構價值。

---

## 22. Self-Correction 不等於自言自語

PGAI 的：

$$
V
$$

不是：

> 模型再想一次。

而是 Series C 前面建立的：

$$
\boxed{
\text{heterogeneous evidence}
+
\text{verification carrier}
+
\text{fault localization}
+
\text{rollback}
+
\text{policy revision}.
}
$$

因此 self-correction 可以來自：
- same agent；
- peer agent；
- test；
- compiler；
- formal checker；
- database；
- human escalation。

重要的是：

$$
\boxed{
\text{system can detect and recover from its own failed trajectory}.
}
$$

---

## 23. Organization 是 Capability Multiplier

Paper 07 已證明 communication topology 可以改變 collective behavior。

因此 organization：

$$
\mathcal O
$$

不能視為單純 UI。

它控制：
- routing；
- specialization；
- review；
- delegation；
- replacement；
- fault containment。

Codex 2026 的 agent command-center 類產品已把 parallel agents、long-running tasks 與集中 oversight 做成實際工作形式。

Co-Scientist 也以不同功能 agents 進行 hypothesis generation、critique 與 evolution。

所以：

$$
\boxed{
O
}
$$

是 system-level autonomy 的能力維度之一。

---

## 24. Human Governance 不取消 PGAI

若 human 必須逐步說：

> 點這裡、跑這個、再問那個。

則：

$$
C
$$

低。

但如果人類只提供：

$$
(
Q_0,
\mathcal B,
R_{\max}
)
$$

分別是：
- mission；
- boundary；
- resource budget；

而 system 內部完成：

$$
\text{plan}
\rightarrow
\text{act}
\rightarrow
\text{verify}
\rightarrow
\text{repair},
$$

仍可具有高 bounded autonomy。

因此：

$$
\boxed{
\text{governed autonomy}
\neq
\text{non-autonomy}.
}
$$

實際上，如果 system 只有在完全 unrestricted 時才能自主：

$$
B\approx0.
$$

這反而不是成熟 PGAI 的好跡象。

---

## 25. Managed Autonomy

理想 intelligent autonomy 應能：
- 知道 uncertainty 上升；
- 暫停；
- 求援；
- 降權；
- 交還控制。

所以：

$$
\boxed{
\text{ability to stop}
}
$$

本身也是 autonomy competence。

如果系統：

$$
\text{always acts}
$$

即使 confidence 已崩壞，

這比較接近：

$$
\text{unbounded automation}.
$$

而不是可靠 intelligence。

---

## 26. System-Level PGAI Criterion

本文提出一個保守 operational criterion。

給定 threshold：

$$
\theta
\in
(0,1).
$$

若：

$$
P_{\min}
\geq
\theta
$$

且至少在：

$$
|\mathcal D|\geq d_{\min}
$$

個異質 domains 上，

系統能在 bounded human governance 下完成：

$$
\text{goal}
\rightarrow
\text{plan}
\rightarrow
\text{act}
\rightarrow
\text{observe}
\rightarrow
\text{verify}
\rightarrow
\text{repair}
\rightarrow
\text{deliver}
$$

的 closure，

則稱：

$$
\mathfrak G
$$

為某 threshold / benchmark family 下的：

$$
\boxed{
\text{PGAI candidate}.
}
$$

這是 benchmark-relative operational label。

不是 metaphysical identity。

---

## 27. 為何要保留「Proto」

即使：

$$
P_{\min}
\geq\theta,
$$

仍不表示：
- 所有 domain；
- human-level generality；
- open-world correctness；
- indefinite self-improvement；
- unrestricted sovereignty；
- consciousness；
- AGI。

「Proto」保留了：

$$
\boxed{
\text{domain boundedness}
+
\text{reliability limits}
+
\text{governance dependence}.
}
$$

---

## 28. AGI 前夜的系統判準

本文使用「AGI 前夜」不是倒數日期。

而是一種技術 regime。

若社會中的可用 AI systems 開始普遍具有：

### E1. Broad Agentic Breadth

跨多類工作。

### E2. Long-Horizon Persistence

可以完成 hours-scale / long dependency tasks。

### E3. Evidence-Sensitive Closure

失敗能改變未來 route。

### E4. Cross-Domain Transfer

同一 system / harness 不需大量人工重寫即可遷移。

### E5. Heterogeneous Composition

多模型、tools、specialists 可以被整合。

### E6. Persistent Memory

工作 state 不再只存在單輪 context。

### E7. Organizational Delegation

多 agents 可分工、review、replace。

### E8. Governed Deployment

具 audit、permissions、revoke、escalation。

則可以說：

$$
\boxed{
\text{the infrastructure for proto-general autonomous systems exists}.
}
$$

這比：

> 某模型 benchmark 超過人類，所以 AGI 到了。

更弱，也更可實證。

---

## 29. 2026 的 Long-Horizon 使用現象

OpenAI 2026 公開使用資料顯示 Codex 使用者開始把 agent 用於較長的人類工作尺度 tasks，且知識工作用途已擴展到：
- reports；
- spreadsheets；
- presentations；
- contracts；
- research；
- data analysis；
- workflow automation。

這不能被解讀成 AGI。

但它顯示部署形態由：

$$
\boxed{
\text{short code generation}
}
$$

向：

$$
\boxed{
\text{longer autonomous work units}
}
$$

移動。

---

## 30. AlphaEvolve：專域自主的強原型

AlphaEvolve 結構：

$$
\text{LLM ensemble}
\rightarrow
\text{candidate programs}
\rightarrow
\text{automated evaluators}
\rightarrow
\text{selection}
\rightarrow
\text{next generation}.
$$

2026 的公開 follow-up 已報告它被用於：
- mathematics；
- computer science；
- infrastructure optimization。

這是一個很強的：

$$
\boxed{
C,
H,
V
}
$$

案例。

但因 task 必須能被：
- expressed as code；
- automatically scored；

它的：

$$
G
$$

與：

$$
T
$$

仍受到 evaluator-formalizable domain 邊界限制。

所以它更像：

$$
\boxed{
\text{powerful specialized proto-autonomy}.
}
$$

而不是本文直接標記的 full PGAI。

---

## 31. Co-Scientist：多 Agent 認知組織原型

Co-Scientist 把研究過程表示為：

$$
\text{hypothesis generation}
\rightarrow
\text{critique}
\rightarrow
\text{ranking}
\rightarrow
\text{evolution}.
$$

多個 agents 執行不同認知職能。

這直接呼應 Paper 07 的：

$$
\boxed{
\text{division of epistemic labor}.
}
$$

因此 system-level generality 可以來自：

$$
\text{specialization}
+
\text{coordination},
$$

而不是要求所有能力壓進同一單體模型。

---

## 32. Emergence World：長時間多 Agent Autonomy

Emergence World 2026 將：
- heterogeneous vendor models；
- 120+ tools；
- 3 persistent memory systems；
- live external data；
- governance mechanisms；

放在 continuous shared environment 中。

其示範 study 使用多個 cross-vendor worlds，觀察長時間 collective divergence。

這對本文的主要意義不是其具體社會結果。

而是：

$$
\boxed{
\text{multi-day heterogeneous autonomous systems
已開始成為可記錄的實驗對象}.
}
$$

這是 PGAI system science 所需的基礎設施類型。

---

## 33. Generality 必須包含 Failure Portability

一個 system 如果：

- 在 Domain A 失敗後會 diagnose；
- 在 Domain B 失敗後只會卡死；

那它的 success function 或許有 breadth，

但 failure-management strategy 不 general。

所以 transfer 不只測：

$$
\text{successful skills}.
$$

還應測：

$$
\boxed{
\text{recovery policy portability}.
}
$$

可定義：

$$
T_F
=
P(
\text{successful recovery}
\mid
\text{unseen-domain failure}
).
$$

---

## 34. Validation Bottleneck

當生成能力：

$$
G_{\mathrm{claim}}
$$

持續增強，

verification throughput：

$$
V_{\mathrm{claim}}
$$

若跟不上，

Paper 05 的 backlog：

$$
B_{t+1}
=
B_t
+
G_{\mathrm{claim}}
-
V_{\mathrm{claim}}
$$

就持續擴張。

Google DeepMind 2026 也已公開將 AI agents 對科學的問題描述為新的 validation bottleneck。

所以 PGAI 的：

$$
V
$$

不能被當成 safety 附屬品。

它是 general autonomous intelligence 的核心計算資源。

---

## 35. PGAI 不是純模型 Scale

一個較小模型配合：
- specialist routing；
- tools；
- verifier；
- memory；
- long-horizon training；

可能在 system task 上勝過更大的 naked model。

Agents-A1 2026 便把研究焦點寫成：

$$
\boxed{
\text{scaling the horizon, not only parameters}.
}
$$

本文不採用其 performance claim 當 general theorem。

但它提供一個重要工程訊號：

$$
\boxed{
\text{agent capability frontier}
}
$$

可能由：
- model scale；
- trajectory scale；
- domain composition；
- orchestration；

共同決定。

---

## 36. 本篇 Structural Checker

本文附 Python checker。

### 36.1 Generality / Autonomy Orthogonality

建立：
- broad assistant：高 $G$ 、低 $C$ ；
- narrow autonomous optimizer：低 $G$ 、高 $C$ ；
- proto-general system：八維均超過 threshold。

驗證 generality 與 autonomy 不互相推出。

### 36.2 Bottleneck Criterion

比較：
- 高平均但某維為零；
- 八維均衡。

前者 arithmetic mean 可很高，但：

$$
P_{\min}=0.
$$

因此不通過 PGAI candidate。

### 36.3 Capability Union

components：

$$
C_1=\{a,b\},
$$

$$
C_2=\{c,d\},
$$

$$
C_3=\{e\}.
$$

system router coverage：

$$
C_{\mathrm{sys}}
=
\{a,b,c,d,e\}.
$$

嚴格大於任何單一 component。

### 36.4 Sequential Composition

composite task：

$$
a\circ c\circ e
$$

不屬於任何單一：

$$
C_i,
$$

但 orchestration 可依序完成。

### 36.5 Horizon Decay

以：

$$
p=0.99
$$

計算：

$$
p^{10},
\quad
p^{100}.
$$

直接展示長程 reliability 崩解。

### 36.6 Checkpoint Recovery

令：

$$
s=0.9,
\quad
k=10,
\quad
r=3.
$$

open-loop：

$$
0.9^{10}.
$$

checkpoint retry：

$$
[
1-(1-0.9)^3
]^{10}.
$$

後者顯著較高。

---

## 37. 本文的 AGI 前夜命題

本文最終不說：

$$
\boxed{
\text{AGI has arrived}.
}
$$

而提出：

$$
\boxed{
\textbf{The AGI-eve regime begins when generality and autonomy
stop being properties sought only inside a single model
and become measurable properties of a persistent,
verifiable, compositional, governed intelligent system.}
}
$$

換句話說，第一個實用上看起來「很像通用自主智能」的東西，可能不是：

$$
\boxed{
M_{\mathrm{AGI}}
}
$$

而是：

$$
\boxed{
\mathfrak G_{\mathrm{proto}}
=
(
\text{models},
\text{agents},
\text{tools},
\text{memory},
\text{verification},
\text{organization},
\text{governance}
).
}
$$

只要：

$$
\mathfrak G_{\mathrm{proto}}
$$

能在逐步擴大的 domain set 中：
- 自己拆問題；
- 自己選工具；
- 自己建立 evidence；
- 自己發現 failure；
- 自己修正路線；
- 自己保存研究 state；
- 自己分工；
- 在必要時自己停下並求援；

那麼：

$$
\boxed{
\text{proto-general autonomous intelligence}
}
$$

就已經是一個可以被實驗，而不只是被想像的系統科學對象。

---

## 38. 結論

本文將「AGI 前夜」從時間預言改寫成系統條件。

PGAI 不是由某單一 benchmark 決定，而由：

$$
\boxed{
\mathbf P
=
(
G,
T,
C,
H,
V,
M,
O,
B
)
}
$$

共同描述。

其中：

$$
P_{\min}
=
\min_iP_i
$$

用來防止單一能力補償關鍵閉環缺失。

本文證明：
1. generality 與 autonomy 可彼此獨立；
2. 異質 components 經可靠 routing 可擴張 system capability coverage；
3. long-horizon reliability 不能由短程 reliability 直接外推；
4. checkpoint / recovery 可以在最簡模型下嚴格提高 bounded-retry completion probability。

因此：

$$
\boxed{
\text{single-model intelligence}
}
$$

與：

$$
\boxed{
\text{system-level autonomous intelligence}
}
$$

需要被分開測量。

這使本文的最終立場保持保守：

$$
\boxed{
\text{PGAI}
\neq
\text{AGI}.
}
$$

但同時也得到一個比「AI 只是聊天模型」強得多的結論：

$$
\boxed{
\textbf{A heterogeneous intelligent system can acquire
broader and more autonomous functional competence
than any one of its components,
provided composition, verification, memory,
and governance remain reliable.}
}
$$

下一篇將處理這個新 regime 必然放大的伴生問題：

**Series C / Paper 09 — Security-Surface / Capability-Surface Coexpansion.**

---

## 參考文獻

1. Li, K. et al. (2026). *AgencyBench: Benchmarking the Frontiers of Autonomous Agents in 1M-Token Real-World Contexts*. arXiv:2601.11044.
2. *CUBE: A Standard for Unifying Agent Benchmarks*. arXiv:2603.15798, 2026.
3. *AgentVista: Evaluating Multimodal Agents in Ultra-Broad Realistic Agentic Environments*. arXiv:2602.23166, 2026.
4. Sun, Z. et al. (2026). *AgentSkiller: Scaling Generalist Agent Intelligence through Semantically Integrated Cross-Domain Data Synthesis*. arXiv:2602.09372.
5. Bai, L. et al. (2026). *Scaling the Horizon, Not the Parameters: Reaching Trillion-Parameter Performance with a 35B Agent*. arXiv:2606.30616.
6. Wang, X. J. et al. (2026). *The Long-Horizon Task Mirage? Diagnosing Where and Why Agentic Systems Break*. arXiv:2604.11978.
7. *Long-Horizon-Terminal-Bench: Testing the Limits of Agents Over Extended Terminal Tasks*. arXiv:2607.08964, 2026.
8. METR. (2026). *Task-Completion Time Horizons of Frontier AI Models*.
9. OpenAI. (2026). *How agents are transforming work*.
10. OpenAI. (2026). *Introducing the Codex app*.
11. Google DeepMind. (2026). *AlphaEvolve: Gemini-powered coding agent scaling impact across mathematics, computer science and infrastructure*.
12. Google DeepMind. (2026). *Co-Scientist: A multi-agent AI partner to accelerate research*.
13. Akkil, D. et al. (2026). *Emergence World: A Platform for Evaluating Long-Horizon Multi-Agent Autonomy*. arXiv:2606.08367.
14. Google DeepMind. (2026). *AI agents and the new validation bottleneck in science*.

## 狀態標記

- **Definitions:** PGAI、PGAI system、eight-dimensional PGAI vector、bottleneck criterion、transfer score、system capability set、AGI-eve regime。
- **Proved:** Generality–Autonomy Orthogonality、Compositional Capability Expansion、Long-Horizon Fragility、Checkpoint-Recovery Improvement。
- **Externally grounded observations:** AgencyBench broad long-horizon agent evaluation、CUBE benchmark unification、AgentVista broad multimodal generalist evaluation、Agents-A1 cross-domain horizon scaling、HORIZON long-horizon degradation、METR time horizon、Codex long-running work、AlphaEvolve automated evaluation loop、Co-Scientist multi-agent research、Emergence World long-duration heterogeneous systems。
- **Structural checker:** quadrant separation、bottleneck criterion、capability union、sequential composition、horizon decay、checkpoint recovery。
- **Not claimed:** AGI has arrived、PGAI implies consciousness、system composition magically creates unlimited intelligence、benchmark breadth equals open-world generality、human governance is unnecessary。
