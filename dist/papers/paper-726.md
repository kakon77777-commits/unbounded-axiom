# 從修辭性邏輯折疊到工程性空間折疊

**——論空間折疊路徑積分法在當代晶片設計中的可能形式，兼論散熱約束、多物理場路徑與 Agent-EDA 協同**

**作者：** Neo.K with Aletheia
**機構：** 一言諾科技有限公司（EveMissLab）
**日期：** 2026 年 6 月
**類型：** 技術白皮書 / 概念論文 / 多物理場演算法草案
**位置：** 《把指標升格為定律》之正面續篇
**前置依賴：** 《把指標升格為定律》、空間折疊路徑積分法、同步張力折疊法、受約束基底企業的修辭批判

---

## 摘要

本文提出一個從修辭性「邏輯折疊」轉向工程性「空間折疊」的晶片設計方法論：**晶片版空間折疊路徑積分法**（Chip-SFPI, Chip-level Space-Folding Path Integral Method）。本文延續《把指標升格為定律》對「韬定律」與「邏輯折疊」的批判，但本文不再以批判為主，而是將批判反轉為正面命題：若一個企業、研究機構或 AI-EDA 系統不只是把既有設計流程命名為定律，而是真正將「路徑積分、多物理場建模、空間折疊、熱限制、時序收斂與封裝約束」整合成可驗證流程，那麼「空間折疊」可以成為一種有工程意義的設計方法，而不是修辭升格。

本文的核心判斷是：在當代晶片設計，尤其是 2.5D / 3D IC、chiplet、垂直堆疊、先進封裝、high-bandwidth interconnect、AI accelerator 與高功率 SoC 的設計中，迷宮式路徑問題已不再只是「訊號線如何走最短」。真正的路徑包括訊號路徑、資料流路徑、時鐘路徑、供電路徑、熱擴散路徑、機械應力路徑、製程良率路徑與工作負載相位路徑。這些路徑互相纏繞，形成一個多尺度、多物理場、多目標約束系統。若直接進行「空間折疊」——例如直接把模組垂直堆疊、把 critical path 壓短、把功能單元靠近——很容易在訊號上獲利，卻在散熱、IR drop、EMIR、clock skew、局部擁塞、熱點重疊與可靠性上失敗。

因此，本文主張晶片版 SFPI 的合理流程應先採用**方案二：先路徑積分，再空間折疊**。也就是先建立多物理場路徑密度：訊號、功耗、熱、時序、供電、封裝、資料流、工作負載與製程風險；再根據這些路徑場決定哪些結構可以折疊、哪些模組必須分開、哪些資料流適合垂直化、哪些高功耗區域絕不可重疊。完成安全折疊後，再使用**方案一：先折疊，再路徑積分**作為後段優化，在已知熱安全邊界內縮短關鍵路徑、改善 PPA、降低 routing congestion、提升 timing closure 的效率。至於**方案三：同步張力折疊法**，本文認為理論上上限最高，但需要更多實際資料、signoff feedback、workload profile、PDK、package model 與熱模型校準；在現階段，Agent 可以作為候選生成器、工具調度器、異常偵測器與設計評論者，但不應取代 signoff，也不應將未經驗證的推理升格為完成的工程範式。

本文的總命題是：**晶片設計中的空間折疊，不應先折疊晶片，而應先折疊所有可能路徑的物理後果。** 只有在熱、功耗、時序與可靠性共同允許的地方，折疊才是優化；否則，折疊只是把問題壓得更密、更熱、更不可救。

---

## 第一章 問題轉向：從修辭批判到工程重建

《把指標升格為定律》處理的是一個修辭學問題：當一個企業將晶片設計中早已存在的時間常數、路徑優化、3D 整合與多物理場設計包裝成「定律」，它是否完成了真正的科學或工程範式轉移？該文的回答是否定的。工程進展可以是真的，密度提升可以是真的，混合鍵合間距可以是真的，cell-to-cell folding 的流程也可以是真實的；但把這些工程進展升格為「定律」，若沒有對應的量化曲線、可證偽預測、跨企業重複性、長期驗證與公開工具鏈，便是修辭升格。

但這個批判不應停留在否定。更重要的問題是：若我們不接受修辭性邏輯折疊，那麼什麼才是工程性空間折疊？

這正是本文要回答的問題。

本文不把「空間折疊」理解為科幻意義上的物理空間彎曲，也不聲稱當代晶片設計能任意折疊三維物理空間。本文所謂空間折疊，是一種多尺度表示操作與設計流程：

```text
transistor / standard cell
→ cell cluster
→ macro
→ tile
→ die region
→ die
→ stacked layer
→ chiplet
→ package
→ system
```

在這個尺度序列中，設計者不斷做一件事：把低層單元壓縮成高層單元，把高層架構再展開回低層物理實現。晶片設計本來就是折疊與展開的循環：架構抽象是折疊，floorplan 是折疊，placement 是折疊，routing 是展開，signoff 是展開後的物理審判，ECO 是審判後的局部重折疊。

因此，本文不是發明「折疊」這個工作，而是提出一個判準：

> 只有當折疊之前先積分了多物理場路徑後果，折疊才是工程；若沒有積分後果，只是把折疊命名為定律，那就是修辭。

這個區分非常重要。因為當代半導體已經進入一個階段：單純幾何縮微的邊際收益下降，先進封裝、chiplet、3D stacking、heterogeneous integration、memory-on-logic、logic-on-memory、near-memory computing、AI accelerator topology 等方案越來越重要。表面上看，大家都在「折疊空間」：把原本平面上的距離壓到垂直方向，把原本跨板級或封裝級的連接壓到 die-to-die，把原本遠距資料搬運壓到近記憶體或片上網路。

但真正的困難不在於喊出折疊，而在於折疊後能不能活下來。
活不下來的折疊，不是優化，是壓縮災難。

---

## 第二章 晶片是一座多物理場迷宮

傳統迷宮問題中，路徑只有一種：從起點到終點的可走格序列。牆阻擋路，路連接路。只要存在一條連續通道，迷宮就可解。

晶片設計中的「迷宮」完全不同。晶片不是只有一種路，而是同時存在多種路：

```text
訊號路徑：資料與控制信號如何傳遞；
時鐘路徑：clock tree 如何分布與同步；
供電路徑：電流如何從 power grid 進入 cell；
熱路徑：熱如何從熱點擴散到散熱界面；
資料流路徑：workload 的高頻資料如何在模組間移動；
封裝路徑：die-to-die、interposer、bump、TSV、hybrid bonding 如何連接；
機械應力路徑：熱膨脹與封裝材料差異如何傳遞；
製程風險路徑：良率、對準、鍵合缺陷與可靠性如何累積。
```

這些路徑之間不是獨立的。縮短訊號路徑可能增加局部功率密度；把高頻運算單元靠近 memory 可能降低資料搬運能耗，卻造成熱點重疊；提高 vertical interconnect 密度可能改善 bandwidth，卻增加製程風險與熱阻；把 critical path 垂直化可能改善延遲，卻讓供電與散熱變難。

因此，晶片設計不是單一路徑迷宮，而是多物理場路徑迷宮。

如果把這件事轉成本文的語言，晶片中的每一條候選「路」都不是單純由幾何距離決定，而是由多個場共同決定：

```text
Path(p) =
  Signal(p)
+ Timing(p)
+ Power(p)
+ Thermal(p)
+ IR(p)
+ EMIR(p)
+ Mechanical(p)
+ Yield(p)
+ Package(p)
+ Workload(p)
```

一條路徑在訊號上可能很好，在熱上可能很壞。
一條路徑在平均 workload 下可行，在 burst workload 下可能失效。
一條路徑在 RTL 層看起來漂亮，在 signoff 層可能被 IR drop 或 thermal hotspot 打爆。

這就是為什麼本文主張：晶片設計中不能先折疊再說。因為你不知道自己折疊的是路，還是災難。

---

## 第三章 散熱是第一判定域

在 3D IC 與高功率晶片設計中，散熱不是附加限制，而是第一判定域。

傳統平面晶片至少有一個相對直接的散熱方向：熱從晶片活性區經由封裝、heat spreader、heat sink 或其他散熱結構排出。當晶片進入 3D 堆疊，熱路徑會變得更複雜。上層 die 可能離散熱界面更遠；中間層可能被其他 active layer 包夾；高功耗模組若垂直重疊，熱點會疊加；memory 與 logic 的熱耐受性不同；封裝材料的熱導率與 mechanical stress 也會影響設計邊界。

所以在晶片版 SFPI 中，散熱不是 action function 的一個普通項，而是合法性閘門。

可以這樣寫：

```text
若 Thermal(p) > Limit：
    p 不合法
否則：
    p 進入多目標評分
```

換句話說，某條折疊路徑即使在 timing 上極佳，只要熱無法排出，它就不是候選解。這一點必須放在整個方法論的最前面。

這也可以壓成一句工程判語：

> 沒有熱可行性，就沒有折疊合法性。

在修辭性的「邏輯折疊」裡，折疊常被描述為縮短信號傳播路徑、提升密度、提升能效。但工程性的空間折疊必須先問：

```text
熱往哪裡走？
功耗峰值是否重疊？
IR drop 是否惡化？
EMIR 是否通過？
clock skew 是否可控？
封裝與散熱結構是否能承受？
不同 workload 下是否會熱崩？
```

如果這些問題沒有先被納入，折疊只是把一個平面問題壓縮成立體問題，且通常更糟。

因此本文主張：晶片版 SFPI 的第一原則不是「縮短路徑」，而是「建立熱可行的路徑場」。

---

## 第四章 晶片版路徑積分：先讓所有物理後果出現

在原始迷宮版 SFPI 中，路徑積分意味著：不先選一條路，而是讓所有候選路徑以權重形式存在，再根據作用量選擇穩定路徑。

在晶片設計中，這個思想可以轉化為：

> 不先決定怎麼堆疊與折疊，而是先建立所有候選資料流、訊號流、熱流、功耗流、時序流與封裝流的物理後果，再根據這些後果決定如何折疊。

定義一條候選設計路徑 `p`，它可能是一個 module placement、routing topology、vertical partition、chiplet split、memory-logic stacking decision 或 package connection pattern。其作用量可寫為：

```text
A(p) =
  α · Delay(p)
+ β · Wirelength(p)
+ γ · Congestion(p)
+ δ · PowerDensity(p)
+ ε · ThermalGradient(p)
+ ζ · IRDrop(p)
+ η · EMIRRisk(p)
+ θ · ClockSkew(p)
+ ι · MechanicalStress(p)
+ κ · YieldRisk(p)
+ λ · PackageCost(p)
+ μ · WorkloadBurstRisk(p)
```

其中每個係數代表不同設計目標與風險權重。路徑權重則可寫成：

```text
Weight(p) = exp(-A(p) / T)
```

這裡的 `T` 不是物理溫度，而是設計探索的容忍度。`T` 高，系統保留更多激進候選；`T` 低，系統更快收斂到保守候選。

但晶片版路徑積分與迷宮版不同。迷宮版裡，路徑通常是空間序列；晶片版裡，路徑是設計決策鏈：

```text
架構切分
→ 模組群聚
→ floorplan
→ layer assignment
→ vertical interconnect placement
→ routing topology
→ power delivery network
→ clock tree
→ thermal path
→ package coupling
→ workload validation
→ signoff feedback
```

因此，晶片版路徑積分不是單純求 routing path，而是對整個設計空間的候選配置做權重化。

可以用偽代碼表示：

```python
def chip_path_action(candidate, models):
    delay = timing_model(candidate)
    wire = wirelength_model(candidate)
    congestion = routing_congestion_model(candidate)
    power_density = power_model(candidate)
    thermal = thermal_model(candidate)
    ir = ir_drop_model(candidate)
    emir = emir_model(candidate)
    clock = clock_skew_model(candidate)
    stress = mechanical_model(candidate)
    yield_risk = yield_model(candidate)
    package = package_model(candidate)
    workload = workload_burst_model(candidate)

    if thermal.max_temp > models.thermal_limit:
        return INF

    if ir.max_drop > models.ir_limit:
        return INF

    if emir.risk > models.emir_limit:
        return INF

    return (
        α * delay
        + β * wire
        + γ * congestion
        + δ * power_density
        + ε * thermal.gradient
        + ζ * ir.max_drop
        + η * emir.risk
        + θ * clock.skew
        + ι * stress.max
        + κ * yield_risk
        + λ * package.cost
        + μ * workload.burst_risk
    )
```

這就是本文所謂「先路徑積分」：先讓所有物理後果進場，不能只看訊號延遲。

---

## 第五章 為什麼方案二應該先於方案一

原始 SFPI 有三個方案：

```text
方案一：先空間折疊，再路徑積分
方案二：先路徑積分，再空間折疊
方案三：同步張力折疊法
```

在迷宮問題裡，方案一很有吸引力。因為先把 32×32 壓成 16×16、8×8、4×4、2×2、1×1，可以迅速獲得大尺度方向，再逐層展開路徑。這對一般迷宮很優雅。

但在晶片設計裡，方案一若用在初始階段，風險很高。因為先折疊會先做抽象與壓縮，而抽象與壓縮最容易抹掉的是局部物理災難：

```text
窄路徑擁塞；
局部熱點；
clock skew；
IR drop；
power delivery bottleneck；
vertical hotspot overlap；
封裝熱阻；
工作負載相位疊加；
局部良率風險。
```

在高層 floorplan 上，兩個模組看起來「應該靠近」；但在真實運作中，它們可能同時高功耗、同時 burst、同時拉電流、同時製造熱點。若先折疊，系統會把「資料流距離短」誤判成「設計優化」。等到後段 signoff 才發現問題，成本極高。

因此，本文主張晶片設計應先用方案二：

```text
Integral → Fold → Unfold
```

也就是：

```text
先建立多物理場路徑密度；
再根據場決定空間折疊；
最後展開回具體 floorplan、routing、stacking 與 package。
```

方案二的核心優勢是：它讓細節先發言。熱點先發言，功耗先發言，IR drop 先發言，資料流先發言，封裝先發言。等這些場都出現後，再談折疊，才不會把物理問題平均掉。

這可稱為：

> 物理場優先的折疊方法。

與之相對，若一開始就提出「我們要把訊號路徑折短」「我們要把邏輯垂直化」「我們要以 τ 替代幾何縮微」，但沒有先建立多物理場後果，那就是目標先行，而不是物理先行。

在工程裡，目標先行很常見，但若目標不受物理場約束，就會變成敘事先行。

---

## 第六章 方案二的具體流程

晶片版方案二可以分為七個階段。

### 6.1 建立設計圖譜

首先把晶片設計轉成多層圖譜：

```text
G_arch：架構資料流圖
G_logic：邏輯模組圖
G_timing：時序依賴圖
G_power：功耗與供電圖
G_thermal：熱擴散圖
G_package：封裝互連圖
G_workload：工作負載相位圖
G_process：製程與良率風險圖
```

每個節點不是單純代表物理位置，而是代表一個功能單元、資料單元、熱源、功耗源或製程風險源。每條邊也不是單純代表線，而可能代表資料流、電流、熱流、時序依賴、封裝連接或風險耦合。

### 6.2 建立多物理場

接著為每個圖建立場：

```text
Signal Field
Timing Field
Power Field
Thermal Field
Clock Field
IR Field
EMIR Field
Mechanical Field
Yield Field
Workload Phase Field
```

這些場不必一開始就是 signoff 級精度。早期可以用 surrogate model、architectural simulator、歷史資料、近似熱模型、power estimate、floorplan estimate。重點是：不要在沒有場的情況下折疊。

### 6.3 路徑積分與候選生成

對每一組可能的 partition / placement / layer assignment / chiplet split / package topology 產生候選，計算其作用量 `A(p)`，形成候選權重。

```python
for candidate in design_candidates:
    A = chip_path_action(candidate, models)
    W = exp(-A / T)
    candidate.weight = W
```

此時不急著選單一方案，而是保留 top-k 候選，形成候選雲。

### 6.4 多尺度折疊

將候選雲折疊到更高層：

```text
cell-level candidates
→ cluster-level candidates
→ macro-level candidates
→ tile-level candidates
→ die-level candidates
→ layer-level candidates
→ package-level candidates
```

每一層折疊都保留高權重結構，同時標記被壓縮掉的風險。這裡不允許「平均化消失」。若某個子區塊包含極高熱點，即使父層平均溫度正常，也必須保留異常標記。

因此折疊函數不能只是平均，而要類似：

```text
Fold(block) =
  weighted_summary
+ max_risk_marker
+ hotspot_marker
+ congestion_marker
+ timing_critical_marker
+ yield_warning
```

這是晶片設計中非常重要的細節：折疊不應消除危險，折疊應攜帶危險摘要。

### 6.5 折疊決策

根據折疊後的多尺度場，系統才決定：

```text
哪些模組可以靠近；
哪些模組可以垂直堆疊；
哪些模組必須水平分散；
哪些高功耗單元不能重疊；
哪些資料流適合短距互連；
哪些 memory / compute 組合適合近距化；
哪些區域需要熱通道；
哪些區域需要保留 routing slack；
哪些區域要犧牲線長換取熱安全。
```

### 6.6 展開與物理實作

折疊決策再展開回具體設計：

```text
floorplan
placement
routing
PDN
clock tree
thermal via / thermal path
bump / TSV / hybrid bonding layout
package routing
cooling interface
```

### 6.7 回饋與迭代

最後進入 EDA 工具與 signoff 回饋：

```text
timing signoff
power signoff
EMIR
thermal signoff
physical verification
package co-simulation
workload stress test
```

若失敗，回到前面更新場與權重，而不是直接在局部補洞。

---

## 第七章 方案一的正確位置：後段優化，而非初始決策

方案一不是不能用。相反，在晶片設計中，方案一非常有價值，但它不應作為初始方法，而應作為方案二之後的優化方法。

方案一是：

```text
Fold → Integral → Unfold
```

在晶片設計中，它可以用於以下情境：

```text
已經知道熱安全邊界；
已經知道 forbidden stacking zones；
已經知道 high-risk power domains；
已經知道 package constraints；
已經知道 workload hotspots；
已經有一組可行 floorplan。
```

在這些條件下，方案一可以快速壓縮設計空間，尋找更好的局部優化：

```text
縮短 critical path；
改善 data locality；
降低 wirelength；
減少 routing congestion；
優化 clock tree；
調整 vertical interconnect；
在熱安全範圍內提高密度；
在可靠性限制內壓低 latency。
```

此時方案一的角色不是「決定折疊是否可行」，而是「在可行折疊內尋找更優解」。

可以用一句話區分：

```text
方案二負責不死；
方案一負責變強。
```

這是本文最重要的工程順序判斷之一。

如果直接用方案一，就像在不知道身體能不能承受的情況下先加壓。
如果先用方案二，再用方案一，就是先做生理檢查，再做力量訓練。

晶片也是如此。
先知道熱、電、時序、封裝與良率能否承受，再壓縮空間，才是工程。

---

## 第八章 方案三：同步張力折疊法與 Agent 的邊界

第三方案是：

```text
P₃ = Resolve[
  Unfold(Integral(Fold(M))),
  Unfold(Fold(Integral(M)))
]
```

也就是同時運行：

```text
A 流：先折疊，再積分；
B 流：先積分，再折疊；
```

然後讓兩者在權重、因果、物理約束與 signoff feedback 中互相對抗。

放到晶片設計裡，A 流代表 top-down 架構與 floorplan 壓縮：

```text
架構目標
→ 高層 partition
→ layer assignment
→ package topology
→ routing estimate
→ physical check
```

B 流代表 bottom-up 物理場推回：

```text
cell / macro / power / thermal / timing / routing field
→ density map
→ risk map
→ folded physical feasibility
→ architecture correction
```

同步張力法要解的是：

```text
高層架構想要什麼？
底層物理允許什麼？
兩者衝突在哪裡？
衝突是否可以透過重新分層、重新放置、重新供電、重新散熱解決？
```

這是理論上最強的方法，因為它不會只聽架構，也不會只聽物理。它同時讓「想做什麼」與「能不能做」互相打架。

但它現在也最麻煩。原因是它需要非常多資料：

```text
PDK；
standard cell library；
timing/power model；
package model；
thermal model；
cooling model；
floorplan candidates；
routing congestion map；
PDN model；
IR drop feedback；
EMIR feedback；
clock tree feedback；
workload profile；
burst power trace；
silicon measurement data；
yield data；
ECO history；
tool invocation logs；
signoff reports。
```

沒有這些資料，Agent 只能做語言推理；而語言推理在這裡遠遠不夠。晶片設計不是講得通就可以，必須跑得通、冷得下來、供得上電、過得了 signoff、量產得出來。

因此本文對 Agent 的判斷是：

> Agent 可以協助同步張力法，但不能在缺少資料與工具回饋時取代同步張力法。

更精確地說，當代 Agent 適合做：

```text
候選方案生成；
設計空間摘要；
工具流程調度；
多輪實驗管理；
異常報告比較；
signoff failure clustering；
constraint conflict explanation；
ECO 建議；
設計紀錄與決策追蹤。
```

但不適合做：

```text
憑語言推理宣稱完成 signoff；
憑概念圖判定熱安全；
憑高層架構幻想良率；
憑 benchmark 敘事取代 silicon measurement；
把未驗證的設計策略命名為定律。
```

這裡正好回到前一篇批判：AI-EDA 若沒有驗證，就會把修辭包裝得更漂亮；但 AI-EDA 若有完整工具回饋與資料閉環，它可能成為真正的新型設計協作者。

---

## 第九章 Agent-EDA 協同的合理架構

本文不主張讓 Agent 取代 EDA，而是主張建立 Agent-EDA 協同。

合理架構應該是：

```text
Human Architect
→ Agent Planner
→ EDA Toolchain
→ Multiphysics Simulation
→ Signoff Feedback
→ Agent Critic
→ Human Decision
→ Iteration
```

其中 Agent 有四個角色。

### 9.1 Planner：候選設計規劃者

Agent 可以根據架構需求與限制，生成多組 candidate：

```text
不同 chiplet split；
不同 memory-compute proximity；
不同 layer assignment；
不同 floorplan；
不同 PDN strategy；
不同 thermal path；
不同 package topology；
不同 cooling assumption。
```

但每個候選必須帶有假設，不可只給結論。

### 9.2 Orchestrator：工具調度者

Agent 可以負責呼叫 EDA / simulation / analysis 工具，管理流程：

```text
run floorplan estimation；
run power estimation；
run thermal simulation；
run congestion analysis；
run timing estimation；
run package co-simulation；
collect signoff reports。
```

這使 Agent 像實驗室助理，而不是神諭。

### 9.3 Critic：衝突分析者

Agent 最有價值的地方之一，是讀取多個工具報告後，找出衝突：

```text
這個 candidate timing 很好，但熱失敗；
這個 candidate 熱安全，但 wirelength 太長；
這個 candidate 平均功耗低，但 burst 風險高；
這個 candidate package 成本高，但 yield risk 低；
這個 candidate 在某 workload 下好，在另一 workload 下壞。
```

這就是同步張力法中的「張力解讀」。

### 9.4 Historian：設計記憶者

晶片設計有大量迭代。Agent 可以記錄：

```text
為什麼放棄某個 floorplan；
某個 ECO 解了什麼問題，又引入什麼問題；
某個熱點從哪一輪開始出現；
某個 timing fix 為何導致 power 變差；
某個封裝選項為何被排除；
```

這種設計記憶非常重要。因為大型設計中，很多問題不是「不知道怎麼算」，而是「不知道之前為什麼那樣決定」。

Agent 在這裡有巨大價值，但前提是它忠於紀錄，而不是替紀錄編故事。

---

## 第十章 不能把 SFPI 變成新的「韬定律」

本文必須明確警告一件事：晶片版 SFPI 自己也可能墮落成修辭。

如果有人把本文方法簡化成：

```text
我們發明了空間折疊路徑積分定律；
它將取代摩爾定律；
它能重塑半導體；
它是新時代晶片設計總原則；
```

那本文就被誤用了。

本文提出的不是定律，而是一組流程判準：

```text
先多物理場路徑積分；
再根據路徑場折疊空間；
再用折疊優先法做局部優化；
在資料足夠時才使用同步張力；
所有結論必須回到 EDA 工具與 signoff 驗證。
```

它不是定律，因為它尚未有跨產品、跨節點、跨公司、跨製程的量化驗證。它也不應被叫做定律。更準確的稱呼是：

```text
方法論；
設計流程；
啟發式框架；
Agent-EDA 協作架構；
多物理場折疊優化策略。
```

如果未來有人要把它升格為更高層概念，必須至少提出以下證據：

```text
在多個設計案例中降低 design iteration；
在同等 PPA 下改善 thermal headroom；
在同等 thermal limit 下改善 latency / bandwidth；
在 2.5D / 3D / chiplet 設計中降低 signoff failure；
在真實 EDA flow 中可重複；
在 silicon measurement 中通過；
在不同 workload 下保持穩定；
在成本與良率上不崩潰。
```

沒有這些，就不能把方法論升格為定律。

這點非常重要。因為本文正是從「把指標升格為定律」的批判中長出來的。若本文自己也被包裝成定律，那就只是換了一個名字重演同一個錯誤。

---

## 第十一章 形式化草案

定義晶片設計狀態為：

```text
D = (G, C, M, W)
```

其中：

```text
G = 多層設計圖譜；
C = 約束集合；
M = 多物理場模型；
W = 工作負載集合。
```

多層設計圖譜：

```text
G = {
  G_arch,
  G_logic,
  G_timing,
  G_power,
  G_thermal,
  G_package,
  G_workload,
  G_process
}
```

約束集合：

```text
C = {
  timing_limit,
  power_limit,
  thermal_limit,
  ir_limit,
  emir_limit,
  area_limit,
  cost_limit,
  yield_limit,
  package_limit
}
```

候選設計：

```text
p ∈ P
```

作用量：

```text
A(p | D) =
  α · Delay(p)
+ β · Wirelength(p)
+ γ · Congestion(p)
+ δ · PowerDensity(p)
+ ε · ThermalRisk(p)
+ ζ · IRDrop(p)
+ η · EMIRRisk(p)
+ θ · ClockSkew(p)
+ ι · Stress(p)
+ κ · YieldRisk(p)
+ λ · PackageCost(p)
+ μ · WorkloadRisk(p)
```

合法性條件：

```text
Legal(p) = True
iff
  Thermal(p) ≤ ThermalLimit
  IRDrop(p) ≤ IRLimit
  EMIRRisk(p) ≤ EMIRLimit
  Timing(p) ≤ TimingLimit
  YieldRisk(p) ≤ YieldLimit
```

權重：

```text
Weight(p) = exp(-A(p | D) / T)
```

折疊算子：

```text
𝓕: P_low → P_high
```

展開算子：

```text
𝓤: P_high → Candidates(P_low)
```

路徑積分算子：

```text
𝓘(P) = TopK({Weight(p), p ∈ P and Legal(p)})
```

方案二：

```text
P₂ = 𝓤𝓕𝓘(D)
```

方案一後段優化：

```text
P₁_refine = 𝓤𝓘𝓕(P₂)
```

同步張力法：

```text
P₃ = 𝓡[
  𝓤𝓘𝓕(D),
  𝓤𝓕𝓘(D)
]
```

其中張力解算：

```text
Score_Tension(p) =
  a · WeightScore(p)
+ b · CausalConsistency(p)
+ c · FoldingStability(p)
+ d · SignoffAgreement(p)
- e · Conflict(p)
```

這裡的 `CausalConsistency` 指設計理由是否與物理後果一致；`SignoffAgreement` 指候選方案是否與工具回饋一致；`Conflict` 指 top-down 與 bottom-up 結果之間的不一致。

---

## 第十二章 複雜度：優雅不等於免費

晶片版 SFPI 的複雜度必須分層討論。

若設計空間有 `N` 個低層元素，建立折疊金字塔的理想成本近似為：

```text
N + N/4 + N/16 + ... < 4N/3
```

因此單純多尺度折疊本身是優雅的，接近 `O(N)`。

但真正昂貴的是候選設計與多物理場模擬。若候選數為 `K`，每個候選需要 `m` 個模型評估，則初步成本可寫為：

```text
O(K · m · ModelCost)
```

若進一步加入多輪迭代 `T`：

```text
O(T · K · m · ModelCost)
```

這看起來很重。但 SFPI 的優雅之處在於：它不是窮舉所有物理實現，而是先用場與折疊降低候選空間，再把昂貴的 signoff 留給更少、更有希望的候選。

因此，它的目標不是取代 EDA signoff，而是減少無效 signoff、減少錯誤設計方向、減少後段返工。

可以這樣理解：

```text
傳統壞流程：
先做一個看似合理的折疊
→ 後段發現熱/電/時序失敗
→ 大量 ECO
→ 回頭重做

SFPI 流程：
先建立多物理場路徑場
→ 過濾高風險折疊
→ 再生成候選
→ 少量高品質 signoff
→ 更少返工
```

因此，SFPI 的複雜度優雅不在於「每一步都更便宜」，而在於「更少把昂貴步驟花在錯方向上」。

這也回到上一篇論文的問題：有時候計算複雜度不是只看求解器跑多快，而是看問題表達是否先排除了錯誤空間。

---

## 第十三章 晶片版 SFPI 的最小可行實驗

如果要把本文從概念推向工程，最小可行實驗不應直接挑戰完整商用 SoC，而應從較小設計開始。

### 13.1 Toy Model

建立一個簡化 many-core / accelerator grid：

```text
16 個 compute tile；
4 個 memory tile；
2 層或 3 層堆疊；
簡化 NoC；
簡化 power map；
簡化 thermal model；
多組 workload trace。
```

目標不是做出真晶片，而是驗證流程是否能降低壞候選。

### 13.2 Baseline

設置三個 baseline：

```text
傳統平面 floorplan；
手工 3D partition；
單目標 latency-driven folding。
```

### 13.3 SFPI 流程

使用方案二：

```text
先建立 dataflow / power / thermal / timing field；
再折疊成 3D partition；
再展開成 floorplan；
再用方案一優化 critical path。
```

### 13.4 評估指標

評估不能只看 latency，至少要看：

```text
maximum temperature；
thermal gradient；
average latency；
tail latency；
energy per operation；
wirelength；
routing congestion；
IR risk proxy；
performance under burst workload；
design iteration count。
```

### 13.5 成功條件

如果 SFPI 能在同等或更低 maximum temperature 下改善 latency / energy，或在同等 latency 下顯著降低 thermal hotspot，則可視為初步有效。

若它只改善 latency 但熱崩，則失敗。
若它只降低平均溫度但犧牲過多效能，也只是保守設計，不算成功。

---

## 第十四章 與當代 3DIC / Chiplet 設計的關係

本文不主張現代 EDA 沒有做這些事。相反，本文承認：當代 3DIC / chiplet / advanced packaging 流程已經高度依賴多物理場 co-design。TSMC、Synopsys、Cadence、Siemens、Ansys 等工具鏈已經把 3D 物理堆疊、邏輯連接、timing、power、thermal、EMIR、package co-design 放入共同流程。

因此本文的定位不是「取代現有 EDA」，而是提出一個更清楚的高層演算法語法：

```text
現有 EDA 是工具層；
SFPI 是設計順序與 Agent 協作層。
```

它回答的是：

```text
在多個工具、模型、候選、限制之間，應該先算什麼？
什麼時候可以折疊？
什麼時候不能折疊？
Agent 應該調度什麼？
什麼東西必須交給 signoff？
如何避免把概念包裝成定律？
```

因此本文與當代 EDA 的關係是疊加，不是替代。

如果說現代 EDA 是顯微鏡與測量儀，那麼 SFPI 是實驗設計方法。沒有顯微鏡，方法無法驗證；沒有方法，顯微鏡可能被拿來測錯問題。

---

## 第十五章 從「韬定律」批判到「工程折疊」判準

至此可以回到前一篇論文。

「韬定律」的問題不在於優化時間常數錯了，也不在於邏輯折疊沒有工程價值。相反，時間、路徑、密度、3D 整合都是真問題。真正的問題是：把一個已在產業中持續演進的設計方向命名為定律，並將工程進展升格為範式主張。

本文提供的反向判準是：

```text
若你聲稱折疊是工程方法：
請給出多物理場流程。

若你聲稱折疊改善延遲：
請同時給出熱、IR、EMIR、clock、良率資料。

若你聲稱折疊是新範式：
請證明它跨設計、跨節點、跨工具、跨 workload 可重複。

若你聲稱 Agent 能做同步張力：
請給出工具閉環與 signoff feedback，而不是語言推理。

若你只是重新命名既有設計流程：
那就是修辭，不是範式。
```

這也是本文最終想建立的分界：

> 修辭性折疊，只改寫說法；工程性折疊，必須改寫可驗證流程。

---

## 第十六章 未來：AI、EDA 與維度計算

從更遠的視角看，晶片版 SFPI 只是更大問題的一個局部：未來 AI 系統如何處理多尺度、多物理場、多目標約束的設計空間？

當代人類工程師很難同時維持所有層級：

```text
架構；
RTL；
floorplan；
placement；
routing；
power；
thermal；
clock；
package；
cooling；
workload；
yield；
supply chain；
成本；
量產。
```

EDA 工具能算很多，但工具本身不會自然形成跨層敘事與決策記憶。Agent 能形成敘事與決策記憶，但若沒有工具閉環，又容易幻覺。未來真正有價值的系統，應該是：

```text
EDA 的可驗證計算
+
Agent 的多候選推理
+
人類架構師的判斷
+
實際 silicon feedback
```

這種系統不會像傳統工具，也不會像聊天機器人。它更像是一個持續運行的設計場：候選方案不斷生成，工具不斷評估，Agent 不斷比較張力，人類不斷設定價值函數，實際晶片數據不斷回流。

在這個意義上，SFPI 不是單一演算法，而是一種未來設計系統的語法。它說的是：

```text
先讓可能性成場；
讓場接受物理審判；
再折疊空間；
再展開實作；
再以回饋修正場。
```

這和迷宮版 SFPI 的精神一致，但更加現實，也更加殘酷。因為在迷宮裡，路徑錯了只是走不通；在晶片裡，路徑錯了可能是數千萬美元、數月工程、甚至整個產品節點的失敗。

---

## 結論：不要先折疊晶片，先折疊後果

本文提出晶片版空間折疊路徑積分法，並主張其正確工程順序應為：

```text
1. 先路徑積分：
   建立訊號、時序、功耗、熱、供電、封裝、工作負載與製程風險場。

2. 再空間折疊：
   根據多物理場決定哪些模組可以靠近、垂直化、chiplet 化或封裝整合。

3. 再折疊優先優化：
   在已知熱安全與可靠性邊界內，用折疊優先法優化 critical path 與 PPA。

4. 最後才同步張力：
   在資料、工具與 signoff feedback 足夠時，使用 Agent-EDA 協同做 top-down 與 bottom-up 的張力解算。
```

本文的核心不是提出一個新名詞，而是提出一個防止名詞空轉的工程判準。

「空間折疊」若沒有熱、電、時序、封裝、工作負載與 signoff 回饋，就是口號。
「路徑積分」若沒有實際模型與候選評估，就是比喻。
「Agent 設計」若不能調用工具與接受驗證，就是漂亮的幻覺。
「定律」若沒有可證偽曲線與長期重複驗證，就是修辭資產。

因此，晶片設計中的真正折疊不是把模組堆起來，也不是把指標命名為定律，而是：

> 先把所有可能路徑的物理後果折疊進設計決策，再把通過物理審判的決策展開成實際晶片。

最後用一句話收束本文：

**不要先折疊晶片；先折疊後果。**
能承受後果的折疊，是工程。
不能承受後果的折疊，是包裝。

---

## 附錄 A：三種方案在晶片設計中的定位

| 方案  | 原始形式                     | 晶片設計定位                    | 適合階段     | 主要風險                     |
| --- | ------------------------ | ------------------------- | -------- | ------------------------ |
| 方案一 | Fold → Integral → Unfold | 先建立高層折疊，再優化路徑             | 後段優化     | 過早壓掉熱點與局部風險              |
| 方案二 | Integral → Fold → Unfold | 先建立多物理場，再決定折疊             | 初始主流程    | 模型成本較高                   |
| 方案三 | Resolve[方案一, 方案二]        | top-down 與 bottom-up 同步張力 | 高資料成熟度階段 | 需要大量資料與 signoff feedback |

---

## 附錄 B：晶片版 Action Function

```text
A(p) =
  α · Delay(p)
+ β · Wirelength(p)
+ γ · Congestion(p)
+ δ · PowerDensity(p)
+ ε · ThermalGradient(p)
+ ζ · IRDrop(p)
+ η · EMIRRisk(p)
+ θ · ClockSkew(p)
+ ι · MechanicalStress(p)
+ κ · YieldRisk(p)
+ λ · PackageCost(p)
+ μ · WorkloadBurstRisk(p)
```

其中：

```text
ThermalRisk、IRDrop、EMIRRisk 可作為硬限制；
Delay、Wirelength、Congestion、PowerDensity 可作為優化目標；
YieldRisk、PackageCost、MechanicalStress 可作為工程可行性限制；
WorkloadBurstRisk 用於防止平均情況掩蓋極端情況。
```

---

## 附錄 C：Agent-EDA 協同最小閉環

```text
Human Architect:
    定義目標與不可違反限制

Agent Planner:
    生成候選設計與假設

EDA Toolchain:
    執行 floorplan / timing / power / thermal / EMIR / package 分析

Agent Critic:
    比較報告、找出張力、提出修正

Human Reviewer:
    決定下一輪方向

Silicon / Measurement Feedback:
    校準模型，修正下一輪候選
```

---

## 附錄 D：防止修辭升格的五條規則

1. 不把方法叫成定律，除非它有可證偽量化曲線。
2. 不把工具流程叫成範式，除非它跨案例重複有效。
3. 不把 Agent 推理叫成設計完成，除非它通過工具與 signoff。
4. 不把 latency 改善叫成成功，除非熱、電、可靠性同時通過。
5. 不把命名當創新，除非命名背後有新能力。

---

## 附錄 E：一句話版本

```text
傳統晶片設計在空間中找路；
修辭性邏輯折疊把找路命名為定律；
工程性空間折疊先計算所有路徑的物理後果，
再決定哪些空間真的可以被折疊。
```

**Neo.K with Aletheia｜EveMissLab｜2026 年 6 月**
