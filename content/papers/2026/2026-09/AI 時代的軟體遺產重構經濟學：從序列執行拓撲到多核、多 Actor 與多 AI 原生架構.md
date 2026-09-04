# AI 時代的軟體遺產重構經濟學：從序列執行拓撲到多核、多 Actor 與多 AI 原生架構

**The Economics of Legacy Software Reconstruction in the AI Era: From Serial Execution Topologies to Multicore, Multi-Actor, and Multi-Agent-Native Architectures**

作者：Neo.K（許筌崴）  
機構：一言諾科技有限公司（EveMissLab）  
版本：v0.1  
日期：2026-08-20  
性質：理論論文／軟體工程與 AI 系統架構研究

---

## 摘要

大量經典遊戲、企業系統與桌面軟體形成於與今日截然不同的計算條件之下。受限於當時的 CPU 核心數、記憶體容量、圖形與 I/O 架構、工具鏈成熟度、人力成本與單一人類操作者假設，許多系統自然採取高度序列化、共享狀態密集、單一主迴圈、單一焦點、單一權威寫入者或單機邊界明確的軟體拓撲。本文將此類約束統稱為「舊軟體序列時空拓撲」，並強調其不等同於字面上的「所有程式只能使用一顆 CPU 核心」。

本文提出一個核心命題：隨著 AI 程式理解、程式生成、代理式工具使用、多 Agent 協作、自動測試與計算資源持續進步，舊軟體從既有序列拓撲重構為多核、多 Actor、多 AI 原生架構的邊際成本將長期下降。其機制並非 AI 消滅軟體工程，而是 AI 同時壓縮理解、規格抽取、依賴分析、程式重寫、測試生成、差異驗證與修復迭代等多個成本項目。

本文進一步提出 Legacy Reconstruction Cost Model、Parallelizable Topology Model、Irreducible Semantic Lower Bound 與 Reconstruction Crossover Condition。核心判據為：當「繼續維護既有拓撲」的預期總成本高於「解構、重建、驗證與遷移」的成本時，重構會由高風險特例逐步轉化為經濟上合理的常規選項。此轉折對遊戲尤其重要，因為遊戲同時包含長期狀態、即時互動、模擬、AI、圖形、資產、事件、任務、腳本與大量邊界條件，是高複雜度軟體重構的壓力測試場。

本文不主張任意 legacy software 均可完全平行化，也不主張 AI 能消滅因果依賴、規格缺失與驗證成本。相反地，本文提出不可約下界：真正的序列依賴、語義不確定性、行為保真度、安全需求與驗證責任仍會限制重構收益。本文最後討論 HDUS 類計算世界架構作為此種多 Actor、多 AI 與資源圖式軟體的可能承載層，但不將其視為本命題成立的必要條件。

**關鍵詞：** Legacy Software、Software Modernization、AI-assisted Refactoring、Multicore、Multi-Agent、Multi-Actor、Game Reconstruction、Software Archaeology、Task Graph、HDUS

---

## 1. 問題不是「舊軟體能不能跑」，而是它仍活在舊計算時代

一套二十年前的遊戲今天通常可以藉由相容層、模擬器、舊 API、虛擬機或平台移植繼續執行。

但「可以執行」與「其計算拓撲仍然合理」是兩個不同問題。

舊軟體的架構通常同時受到以下條件塑形：

- 可用 CPU 核心數有限；
- thread 與同步工具的工程成本較高；
- 記憶體與儲存較昂貴；
- GPU 與 CPU 工作分配模式不同；
- 網路延遲高且遠端計算不普及；
- CI、fuzzing、property-based testing 與大規模 telemetry 尚未普及；
- 軟體由有限人類團隊手工維護；
- 使用者通常被假設為單一人類；
- AI 不被視為持續存在的 Actor；
- App、Window、Process、Machine 之間高度綁定。

因此，歷史架構可以粗略表示為：

$$
\mathcal{L}_{old}
=
(
S_g,
M,
P,
F_h,
A_h,
B_m
),
$$

其中：

- $S_g$：大量共享或全域狀態；
- $M$：主要控制迴圈；
- $P$：以 process/thread 為核心的執行單位；
- $F_h$：單一 host focus；
- $A_h$：主要人類操作者；
- $B_m$：單機邊界。

此模型在當時未必落後，甚至可能是最佳工程解。

真正的問題是：

> 當計算條件改變後，歷史最優解是否仍然是今日最優解？

本文答案是：未必。

---

## 2. 「單核」應被重新定義為序列拓撲問題

本文使用「單核時空困境」時，不將其嚴格定義為：

$$
CPU\ cores=1.
$$

很多經典軟體實際上早已使用多執行緒、音訊執行緒、I/O thread、render thread 或背景工作。

更準確的問題是：

$$
\boxed{
\text{Architectural Serial Fraction}
}
$$

即整個系統有多少工作因為歷史架構，而不是因為真正不可約的因果關係，被綁在同一個序列控制流、共享狀態域、單一主迴圈或單一權威節點中。

令軟體工作圖為：

$$
G=(V,E),
$$

其中 $V$ 為工作單位， $E$ 為依賴關係。

若舊架構實際執行序近似：

$$
v_1
\rightarrow
v_2
\rightarrow
v_3
\rightarrow
\cdots
\rightarrow
v_n,
$$

不代表所有邊：

$$
(v_i,v_{i+1})\in E
$$

都是必要依賴。

其中部分可能只是：

- 原始程式方便；
- global state 難拆；
- 當年多核收益不足；
- 工具鏈不適合；
- 測試成本過高；
- 團隊沒有足夠時間重構。

因此第一個重要工作不是「平行化」，而是重新估計：

$$
E_{true}
\subseteq
E_{legacy}.
$$

其中 $E_{true}$ 是真正不可消滅的因果依賴，而 $E_{legacy}$ 包含歷史實作造成的額外耦合。

AI 解構的價值之一，就是協助尋找兩者之差：

$$
E_{accidental}
=
E_{legacy}
-
E_{true}.
$$

---

## 3. 從軟體考古到可執行規格

傳統 legacy modernization 最困難的階段之一，不是寫新 code，而是理解舊系統到底在做什麼。

一套成熟軟體的真實規格往往分散於：

- 原始碼；
- scripts；
- config；
- asset metadata；
- database schema；
- build system；
- UI behavior；
- bug workaround；
- save format；
- hidden constants；
- undocumented assumptions；
- 玩家／使用者長期依賴的 emergent behavior。

因此舊系統可表示為：

$$
\mathcal{S}_{legacy}
=
C
+
D
+
A
+
R
+
H,
$$

其中：

- $C$：code；
- $D$：data；
- $A$：assets；
- $R$：runtime behavior；
- $H$：historical assumptions。

真正的解構不是單純反編譯，而是產生一個中間表示：

$$
\mathcal{M}
=
(
State,
Rule,
Event,
Dependency,
Interface,
Invariant,
Trace,
Artifact
).
$$

只要 $\mathcal{M}$ 足夠完整，後續問題就從：

> 重新理解整個舊系統。

轉化成：

> 根據已知 dependency 與 invariant，重新映射到新執行拓撲。

這是問題難度的結構性下降。

---

## 4. AI 正在改變 legacy modernization 的成本結構

到 2026 年，AI-assisted modernization 已不只是研究想法。

Microsoft 的 GitHub Copilot modernization 已提供 legacy application assessment、migration planning、framework upgrade、re-architecture 與 agentic transformation；其文件明確描述可由 modernization agents 分析既有專案、產生目標架構並處理重寫。Google Cloud 的 mainframe modernization 工具亦使用生成式 AI 進行 codebase assessment、依賴映射、business rule 抽取與程式轉換。AWS Transform 則把 specialized AI agents、agentic workflows 與 application decomposition 納入 legacy modernization。

同時，多 Agent 軟體工程工具開始產品化。OpenAI Codex、GitHub Copilot Fleet 與 Anthropic 多 Agent 系統都已將任務分解、隔離執行與平行工作視為主要能力。

因此本文不需要提出：

$$
\text{AI can assist modernization}
$$

作為新命題。

更進一步的新問題是：

$$
\boxed{
\text{AI-assisted modernization}
\rightarrow
\text{topological reconstruction}
}
$$

也就是：

> 當 AI 已能理解、規格化與重寫舊系統後，我們是否仍應只把它遷移成「同一種舊軟體的新語言版本」？

答案未必。

---

## 5. Legacy Reconstruction Cost Model

定義舊軟體完整重構成本：

$$
C_R
=
C_U
+
C_S
+
C_D
+
C_W
+
C_I
+
C_V
+
C_M,
$$

其中：

- $C_U$：理解與軟體考古成本；
- $C_S$：規格抽取成本；
- $C_D$：依賴與拓撲分解成本；
- $C_W$：重寫成本；
- $C_I$：整合成本；
- $C_V$：驗證成本；
- $C_M$：遷移與相容成本。

在傳統人力模式中：

$$
C_R^{human}
$$

可能極高。

AI 介入後，不應粗暴假定：

$$
C_R^{AI}\rightarrow0.
$$

較合理的模型是：

$$
C_R(t)
=
\sum_i
\alpha_i(t)C_i^{human}
+
C_{compute}(t)
+
C_{coord}(t),
$$

其中：

$$
0\le\alpha_i(t)\le1
$$

表示某一成本項目仍需多少人類等價工作量。

若 AI 能力、agent tooling、test generation 與 compute 持續進步，則多個 $\alpha_i(t)$ 具有下降可能：

$$
\frac{d\alpha_U}{dt}<0,
$$

$$
\frac{d\alpha_S}{dt}<0,
$$

$$
\frac{d\alpha_D}{dt}<0,
$$

$$
\frac{d\alpha_W}{dt}<0,
$$

$$
\frac{d\alpha_V}{dt}<0.
$$

因此核心猜想為：

$$
\boxed{
\frac{dC_R}{dt}<0
}
$$

這不是數學必然定理，而是需要長期工程資料驗證的技術經濟假說。

---

## 6. 重構的真正目標：重新求一次計算拓撲

舊軟體現代化常見目標包括：

- 語言升級；
- framework 升級；
- containerization；
- cloud migration；
- API 化；
- database migration。

本文提出另一個維度：

$$
\boxed{
\text{Execution Topology Modernization}
}
$$

也就是不只問：

> 用什麼語言重新寫？

而要問：

> 哪些計算單位今天根本不必再被綁在一起？

令舊執行時間為：

$$
T_{old}
=
\sum_{i=1}^{n}T_i.
$$

若解構後得到平行集合：

$$
\mathcal{P}
=
\{P_1,P_2,\ldots,P_k\},
$$

理想新時間近似：

$$
T_{new}
\approx
\max_j T(P_j)
+
T_{sync}
+
T_{coord}.
$$

因此收益：

$$
S
=
\frac{T_{old}}{T_{new}}.
$$

但此式只在工作真正獨立時成立。

若錯誤拆分依賴，系統會付出：

$$
C_{race}
+
C_{rollback}
+
C_{consistency}.
$$

所以重構的真正價值不在「使用更多核心」，而在：

$$
\boxed{
\text{識別正確的並行邊界}
}
$$

---

## 7. Amdahl 上界仍然存在

任意系統都存在不可平行部分。

令 $p$ 為可平行化比例， $N$ 為有效工作單位數，並加入協調成本 $\omega(N)$：

$$
S(N)
\le
\frac{1}{
(1-p)
+
\frac{p}{N}
+
\omega(N)
}.
$$

即使：

$$
N\rightarrow\infty,
$$

也不代表：

$$
S(N)\rightarrow\infty.
$$

因為：

$$
1-p>0
$$

以及：

$$
\omega(N)>0.
$$

例如：

$$
\text{Damage}
\rightarrow
\text{Death Check}
\rightarrow
\text{Drop Resolution}
$$

具有真實因果順序。

AI 不能因為會寫程式，就把因果律消滅。

因此「AI 多核化」真正能消除的是：

$$
E_{accidental},
$$

而不是：

$$
E_{true}.
$$

---

## 8. 遊戲是此命題的高難度測試場

遊戲之所以重要，不只是因為市場價值。

它是一種高度混合軟體：

$$
Game
=
Simulation
+
Rendering
+
Input
+
AI
+
Physics
+
Audio
+
UI
+
Scripting
+
Persistence
+
Narrative.
$$

其中同時存在：

- frame-sensitive work；
- 長期世界狀態；
- 大量資料與資產；
- 玩家可見的行為保真度；
- 不可完全形式化的「手感」；
- emergent interactions；
- 大量 rare-state combinations。

因此若 AI 可以可靠地將一套經典遊戲從舊拓撲重構成現代多核、多 Actor、多 AI 版本，代表其能力不只是「會生成 CRUD application」。

遊戲可以被視為：

$$
\boxed{
\text{Legacy Reconstruction Stress Test}
}
$$

---

## 9. 從「NPC AI」到多層智能計算

傳統遊戲 AI 常表示為：

$$
FSM,
\quad
BT,
\quad
Utility,
\quad
Planner.
$$

未來重構不應簡化成：

> 每個 NPC 都掛一個大型語言模型。

這在成本、延遲與一致性上通常不合理。

更可行的是分層：

$$
\text{World AI}
\rightarrow
\text{Faction AI}
\rightarrow
\text{Group AI}
\rightarrow
\text{Character AI}.
$$

而每層可以使用不同計算模型：

$$
M_i
\in
\{
FSM,
BT,
Utility,
SmallModel,
LargeModel,
RuleEngine
\}.
$$

因此 AI-native game architecture 的重點不是：

$$
LLM\ everywhere,
$$

而是：

$$
\boxed{
\text{Dynamic Intelligence Allocation}
}
$$

即依據：

- 角色重要性；
- 事件風險；
- 玩家距離；
- 世界狀態；
- budget；
- latency；
- narrative demand；

動態決定智慧層級。

---

## 10. Multi-Actor 比 Multi-Agent 更一般

未來軟體不只要支援多 AI。

它還可能同時存在：

$$
A
=
\{
Human,
AI_1,
AI_2,
Service,
RemoteHuman,
Automation
\}.
$$

因此真正的軟體現代化方向之一是：

$$
\boxed{
\text{Single-Operator Software}
\rightarrow
\text{Multi-Actor Software}
}
$$

它要求重新思考：

- input ownership；
- focus；
- authority；
- transaction；
- conflict；
- resource identity；
- observation；
- provenance。

傳統：

$$
1\ Human
+
1\ Cursor
+
1\ Focus
$$

不再是唯一合理的操作模型。

這使 legacy reconstruction 不只是一個 performance problem，也是一個 interaction ontology problem。

---

## 11. Multi-Agent Reconstruction 本身也需要拓撲

若重構系統由多 AI 執行，可以表示為：

$$
\mathcal{A}
=
\{A_0,A_1,\ldots,A_n\}.
$$

但：

$$
|\mathcal{A}|\uparrow
$$

不保證：

$$
Productivity\uparrow.
$$

多 Agent 本身存在：

$$
C_{coord}
=
C_{communication}
+
C_{merge}
+
C_{conflict}
+
C_{duplicate}
+
C_{verification}.
$$

因此最佳 Agent 數量應與當前可獨立工作的前沿相關：

$$
N^*
\approx
|\mathcal{F}_{independent}|.
$$

其中：

$$
\mathcal{F}_{independent}
$$

是 task graph 上目前可在不等待彼此的情況下執行的工作集合。

這與 GitHub Fleet、OpenAI multi-agent coding 與 Anthropic orchestrator-worker 系統觀察到的工程事實一致：平行 Agent 對獨立子任務最有效，而依賴密集工作會受到協調成本限制。

---

## 12. 經典遊戲「重製」可能被重新定義

傳統 remake 常聚焦：

$$
Graphics
+
Resolution
+
Assets
+
EnginePort.
$$

但 AI 時代可能出現第二類：

$$
\boxed{
\text{Computational Remake}
}
$$

其核心不是換貼圖，而是：

$$
\text{Old Behavior}
\rightarrow
\text{New Computational Topology}.
$$

例如：

- main-loop-bound NPC simulation 被拆成 task graph；
- faction simulation 可獨立運行；
- pathfinding 分散到 worker pool；
- narrative AI 成為可選智慧層；
- save state 被提升為可版本化 world state；
- single-focus interaction 改為 multi-actor transaction；
- legacy modules 被逐步包裝為 Resources；
- AI agents 可在隔離 scope 中讀、改、驗證世界。

所以：

$$
\text{Remake}
\neq
\text{Visual Upgrade}.
$$

它可能變成：

$$
\boxed{
\text{Temporal-Spatial Computational Reconstruction}
}
$$

---

## 13. 維護與重構的交叉點

令未來一段時間內持續維護 legacy system 的成本為：

$$
C_L(H),
$$

其中 $H$ 是時間 horizon。

令完整現代化重構成本為：

$$
C_R(t).
$$

則存在可能的 crossover：

$$
\boxed{
C_R(t^*)
<
C_L(H)
}
$$

一旦成立：

> 重構比繼續維護古董更便宜。

此時軟體遺產的經濟性會改變。

過去某套軟體可能因為：

- code 太亂；
- 文件缺失；
- 原作者離開；
- regression test 不足；
- rewrite 風險太高；

而永遠留在 legacy state。

AI 若持續降低：

$$
C_U+C_S+C_D+C_W+C_V,
$$

就可能將部分「不可重寫」系統推入可重構區域。

這是本文最重要的經濟命題。

---

## 14. 不可約語義下界

本文反對一個過度樂觀結論：

$$
C_R\rightarrow0.
$$

即使 AI 極強，仍存在：

$$
\boxed{
C_{min}
=
C_{semantic}
+
C_{serial}
+
C_{verification}
+
C_{migration}
+
C_{risk}.
}
$$

### 14.1 語義下界

若原軟體某些規則從未被文件化，也無可觀察行為足以反推，AI 無法憑空知道唯一正確答案。

### 14.2 序列下界

真正具有因果順序的 state transition 不能任意平行化。

### 14.3 驗證下界

「能生成」不等於「已證明等價」。

### 14.4 遷移下界

玩家存檔、企業資料、插件、生態系與外部 API 都可能形成現實約束。

### 14.5 風險下界

安全關鍵、金融、醫療或大型線上服務的錯誤成本可能遠高於程式生成成本。

因此本文真正主張的是：

$$
C_R(t)\downarrow,
$$

而不是：

$$
C_R(t)\rightarrow0.
$$

---

## 15. Behavioral Oracle 與差異驗證

若原系統仍可執行，它本身可以部分充當 behavioral oracle。

對狀態：

$$
s_i
$$

輸入動作：

$$
a_i,
$$

舊系統得到：

$$
o_i^{old}.
$$

新系統得到：

$$
o_i^{new}.
$$

可以建立：

$$
d(
o_i^{old},
o_i^{new}
)
<
\epsilon.
$$

更完整地：

$$
\mathcal{T}
=
\{
(s_i,a_i,o_i)
\}_{i=1}^{N}.
$$

透過：

- replay；
- fuzzing；
- generated states；
- save-state mutation；
- differential testing；
- property checking；

大量產生行為對照。

AI 與算力上升的另一個重要作用，就是讓：

$$
N\uparrow
$$

的成本下降。

因此，重構能力的提高不只來自更會寫 code，也來自：

$$
\boxed{
\text{More Affordable Verification}
}
$$

---

## 16. 但 Behavioral Oracle 不是完整真理

舊系統輸出：

$$
o_i^{old}
$$

不代表：

$$
o_i^{old}
=
\text{Intended Behavior}.
$$

因為原版可能包含：

- bug；
- undefined behavior；
- accidental exploit；
- platform-specific artifact；
- frame-rate dependency；
- race condition。

因此 reconstruction 必須區分：

$$
\text{Observed}
$$

$$
\text{Intended}
$$

$$
\text{Preserved}
$$

三種語義。

對經典遊戲尤其如此：

某個 bug 可能已成為 speedrun 技巧。

此時：

$$
Bug_{historical}
$$

是否應被修掉，不是單純技術問題，而是產品與保存策略問題。

---

## 17. 三種重構目標

因此本文提出三種 reconstruction mode。

### Mode A：Behavior-Preserving Reconstruction

目標：

$$
\mathcal{B}_{new}
\approx
\mathcal{B}_{old}.
$$

主要重構底層拓撲，不改變使用者可觀察行為。

### Mode B：Semantics-Preserving Modernization

保留核心規則，但允許修復：

- performance bottleneck；
- known bug；
- unsafe behavior；
- obsolete interface。

### Mode C：Generative Expansion

以原系統為基底：

$$
\mathcal{S}_{old}
\subset
\mathcal{S}_{new}.
$$

直接加入：

- multi-AI；
- richer simulation；
- persistent world；
- dynamic content；
- multi-actor interaction；
- new resource graph。

第三種才是真正可能把「經典軟體」變成 AI 時代新系統的模式。

---

## 18. 從 legacy executable 到 computational world

傳統遊戲或軟體經常被理解為：

$$
Application
=
Executable.
$$

但重構後可以改為：

$$
\boxed{
Application
=
Persistent\ Computational\ World.
}
$$

例如：

$$
\mathcal{W}
=
(
Actors,
Resources,
Fields,
State,
Capabilities,
Transactions
).
$$

此時：

- rendering 只是 projection；
- process 只是 execution backend；
- AI 是 Actor；
- NPC simulation 是 Field；
- save 是 world-state serialization；
- remote compute 是 Resource；
- human input 是 Actor action；
- legacy executable 可以退化成 compatibility Resource。

這正是 HDUS 類架構可能介入的地方。

---

## 19. HDUS 的角色：承載層，而非必要前提

本文命題不依賴 HDUS 才成立。

任何可以提供：

- multi-actor identity；
- task/field abstraction；
- resource graph；
- capability；
- transaction；
- provenance；
- heterogeneous execution；

的 runtime 都可以支援此方向。

但 HDUS 的 World / Field / Actor / Resource 模型天然適合描述：

$$
\text{Legacy Software}
\rightarrow
\text{Multi-Actor Computational World}.
$$

因此可以想像漸進遷移：

$$
LegacyExecutable
\rightarrow
LegacyResource
\rightarrow
ExtractedResources
\rightarrow
NativeFields
\rightarrow
MultiActorWorld.
$$

這比一次性 rewrite 更安全。

舊系統可以在重構期間繼續執行，新模組逐步取代舊模組。

---

## 20. 漸進式拓撲替換

理想重構不必是：

$$
Old
\rightarrow
Delete
\rightarrow
New.
$$

而可以是：

$$
\mathcal{S}_0
\rightarrow
\mathcal{S}_1
\rightarrow
\mathcal{S}_2
\rightarrow
\cdots
\rightarrow
\mathcal{S}_n.
$$

每一步只替換一個 topology boundary。

例如：

$$
MainLoop
\rightarrow
MainLoop+WorkerPool,
$$

再：

$$
NPCSystem
\rightarrow
NPCField,
$$

再：

$$
QuestState
\rightarrow
VersionedResource,
$$

再：

$$
SingleHumanInput
\rightarrow
MultiActorBroker.
$$

若每一步都具有 differential test 與 rollback，重構風險可顯著下降。

---

## 21. 一個可測量的 Modernization Index

為避免把「AI 原生化」寫成宣傳詞，本文提出初步指標：

$$
MI
=
w_1P
+
w_2D
+
w_3A
+
w_4V
+
w_5R,
$$

其中：

- $P$：可安全平行化比例；
- $D$：依賴顯式化程度；
- $A$：multi-actor readiness；
- $V$：verification coverage；
- $R$：resource decoupling。

並滿足：

$$
\sum_iw_i=1.
$$

此指標不主張為通用標準，只作為比較 legacy 與 reconstructed architecture 的研究工具。

更重要的量則是：

$$
\Delta MI
=
MI_{new}
-
MI_{old}.
$$

如果：

$$
\Delta MI>0
$$

但：

$$
Cost_{runtime}
$$

或：

$$
RegressionRate
$$

大幅惡化，仍不能稱為成功。

---

## 22. 真正的成功函數

因此重構成功不等於：

$$
MoreThreads
+
MoreAgents.
$$

本文提出：

$$
Q_R
=
f(
Fidelity,
Performance,
Maintainability,
Parallelism,
Verifiability,
Cost,
Risk
).
$$

成功重構至少要同時提高部分指標，而不能以嚴重犧牲其他指標換取表面上的「多核」。

尤其：

$$
Parallelism\uparrow
$$

若導致：

$$
Consistency\downarrow\downarrow,
$$

就是失敗。

同理：

$$
AI\ Actors\uparrow
$$

若：

$$
CoordinationCost\uparrow\uparrow,
$$

也不是進步。

---

## 23. 核心命題

本文最終提出五個命題。

### 命題一：AI 重構成本下降命題

在模型能力、工具使用、自動驗證與算力持續進步的條件下，部分 legacy software 的有效重構成本具有長期下降趨勢：

$$
\boxed{
\frac{dC_R}{dt}<0.
}
$$

### 命題二：歷史序列耦合可分離命題

舊軟體的序列依賴可以分解為：

$$
\boxed{
E_{legacy}
=
E_{true}
\cup
E_{accidental}.
}
$$

現代化主要作用於：

$$
E_{accidental}.
$$

### 命題三：重構交叉點命題

對部分長期維護系統，存在：

$$
\boxed{
t^*:
C_R(t^*)
<
C_L(H).
}
$$

此後重構可能比維護 legacy architecture 更具經濟性。

### 命題四：多 AI 非單調收益命題

多 Agent 數量增加不保證效能單調上升：

$$
\boxed{
N_{AI}\uparrow
\not\Rightarrow
Performance\uparrow.
}
$$

存在由 task graph、communication 與 shared-state constraints 決定的有效區間。

### 命題五：軟體遺產拓撲可再生成命題

當舊系統的狀態、規則、依賴、介面與行為被充分解構後，其實作拓撲不必被視為不可變歷史事實：

$$
\boxed{
\text{Preserve Semantics}
\not\Rightarrow
\text{Preserve Execution Topology}.
}
$$

這是本文最核心的一句。

---

## 24. 可證偽條件

本文不是以不可證偽的未來預測收尾。

若未來實驗普遍顯示：

1. AI 對 large legacy systems 的理解成本沒有隨能力提升下降；
2. AI 產生的 reconstruction specification 長期無法達到可驗證完整度；
3. multi-agent coordination cost 抵消大多數重構收益；
4. differential testing 無法有效控制 semantic drift；
5. legacy maintenance cost 長期仍顯著低於 AI reconstruction cost；

則本文的強形式：

$$
\frac{dC_R}{dt}<0
$$

至少需要被限制於更小的軟體類別。

相反地，若 longitudinal benchmarks 顯示：

$$
C_R^{2028}
<
C_R^{2026}
$$

並且：

$$
Q_R^{2028}
\ge
Q_R^{2026},
$$

則可以逐步累積支持。

---

## 25. 建議實驗

### Experiment A：經典小型遊戲

選擇具有：

- 可取得 source 或合法分析版本；
- deterministic replay；
- 中等規模；
- 清楚 game state；

的舊遊戲。

比較：

$$
HumanOnly
$$

與：

$$
Human+AI
$$

重構成本。

### Experiment B：拓撲抽取

要求 AI 從 legacy code 建立：

$$
G_{legacy}.
$$

再由獨立 verifier 檢查：

$$
E_{true}
$$

與：

$$
E_{accidental}.
$$

### Experiment C：Behavioral Oracle

產生：

$$
10^3,
10^4,
10^5
$$

級狀態與 replay，觀察 reconstruction divergence。

### Experiment D：多 Agent 重構

比較：

$$
N=1,2,4,8,16
$$

時：

- completion time；
- token/compute；
- merge conflicts；
- regression count；
- repair cycles。

用實驗估計：

$$
N^*.
$$

### Experiment E：Legacy vs Native Topology

比較：

$$
\mathcal{S}_{legacy}
$$

與：

$$
\mathcal{S}_{reconstructed}
$$

在：

- throughput；
- latency；
- CPU utilization；
- scalability；
- maintainability；
- observability；

上的差異。

---

## 26. 對未來軟體產業的含義

如果本文命題成立，AI 可能不只提高「新軟體生成速度」。

更深層的變化是：

$$
\boxed{
\text{Software Heritage Becomes Recomputable}.
}
$$

也就是軟體遺產從：

> 固定的 historical implementation

逐漸變成：

> 可被重新理解、重新規格化、重新驗證與重新生成的 semantic artifact。

這會改變：

- remake；
- remaster；
- emulator；
- enterprise modernization；
- operating-system migration；
- game preservation；
- abandoned software；
- scientific code；
- infrastructure software；

的成本曲線。

歷史 code 不再必然等於歷史 architecture。

---

## 27. 結論

本文提出的不是：

> AI 未來可以把所有舊遊戲自動多核化。

而是一個更一般、也更可驗證的命題。

舊軟體的執行拓撲受到其誕生時代的硬體、工具與人力條件塑形。當 AI、agent tooling、自動驗證與計算資源發生質變時，維持舊拓撲的理由也可能失效。

因此：

$$
\boxed{
\text{Legacy Semantics}
\neq
\text{Legacy Topology}.
}
$$

只要能將：

$$
State,
Rule,
Dependency,
Invariant,
Behavior
$$

從歷史 implementation 中抽離，新的實作就可以重新尋找：

$$
\text{Parallelism},
\text{Multi-Actor},
\text{Multi-Agent},
\text{Distributed Resources}.
$$

真正不能被 AI 消滅的，是：

$$
\text{Irreducible Causality}
+
\text{Semantic Uncertainty}
+
\text{Verification Responsibility}.
$$

但除此之外，大量過去因成本過高而被視為「只能這樣維護」的歷史耦合，可能逐步變成可重新計算的工程選擇。

若此趨勢延續，AI 對軟體史最深的影響之一，或許不只是生成更多新程式，而是讓人類第一次有能力以較低成本重新計算舊軟體的整體架構。

---

## 參考資料

1. OpenAI. *Introducing the Codex App*. 2026.
2. OpenAI. *Codex: AI Coding Agents for Software Engineering*. 2026.
3. GitHub. *Running Tasks in Parallel with the Fleet Command*. GitHub Docs, 2026.
4. GitHub. *Custom Agents and Sub-Agent Orchestration*. GitHub Docs, 2026.
5. Anthropic. *How We Built Our Multi-Agent Research System*. 2025.
6. Microsoft Learn. *GitHub Copilot Modernization Overview*. 2026.
7. Microsoft Learn. *Re-architect Projects by Using GitHub Copilot Modernization*. 2026.
8. Google Cloud. *Mainframe Assessment Tool Overview*. 2026.
9. Google Cloud. *Mainframe Migration and Modernization with AI*. 2026.
10. AWS. *AWS Transform Migration Launch Guide*. 2026.
11. AWS Prescriptive Guidance. *Understanding Application Decomposition*. 2026.
12. Amdahl, G. M. *Validity of the Single Processor Approach to Achieving Large Scale Computing Capabilities*. AFIPS, 1967.

---

## 理論地位聲明

本文提出之成本函數、重構交叉點、Modernization Index 與長期下降關係均屬理論模型與可驗證命題，不代表已被產業資料普遍證實。文中對未來多核、多 Actor、多 AI 軟體架構的推論應透過 longitudinal benchmark、legacy reconstruction experiment、behavioral differential testing 與實際維護成本資料持續檢驗。
