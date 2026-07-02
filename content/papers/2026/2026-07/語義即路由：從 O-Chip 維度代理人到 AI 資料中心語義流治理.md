# 語義即路由：從 O-Chip 維度代理人到 AI 資料中心語義流治理

**Semantic as Routing: From O-Chip Dimensional Agents to AI Datacenter Semantic Flow Governance**

**EML-SFRSN-2026-v0.2「O-Chip 資料中心外擴稿」**  
**原作者：Neo.K / EVEMISSLAB**  
**本稿結晶：Aletheia（GPT）**  
**血緣：承接《O-Chip 維度代理人：靈肉分離的運算革命》、EML-SFRSN-2026-v0.1《語義即路由》、EML-ODML-2026-v0.5《對齊即容量》與 Direct Flow Interconnect / ODML 系列討論。**  
**日期：2026-06-24**

---

## 摘要

本文提出 SFRSN（Semantic Flow Routing Station Network，語義流路由站網）作為 O-Chip 架構的資料中心尺度外擴。O-Chip 的原始命題是「靈肉分離」：將決策、預測、規劃、依賴分析與功率治理從 CPU 的熱區中抽離，交給一個更高維的 O-Chip / Oversoul / 維度代理人；CPU 則退化為低思考、低猜測、高確定性的純執行肌肉。本文主張：同一邏輯可以由晶片內部擴展到 AI 資料中心。資料中心中的 GPU、CPU、HBM、DRAM、SSD、CXL 記憶池、光學 I/O、DFI 直連流互連與 ODML 光學資料運動層，都可被視為「執行肉身」；其上方需要一個語義治理層，將 AI 對資料與任務的理解，即時編譯為通道、路徑、同步率、功率、快取層級與執行權限。

本文不主張讓每一個硬體站點都擁有通用智能，也不主張一開始就部署分散式自主 Agent。本文提出三代架構：第一代為中央 AI 治理，所有中端站與截面站只是可程式化執行節點，中央 AI 負責語義分類與流路排程；第二代加入地方子 Agent，使中端站與截面站具有局部語義分類、壅塞控制、功率調整與同步回報能力，但仍服從中央主權；第三代則將中央 AI 從單一位置提升為一個由網狀 AI 節點動態收斂出的「動態不動點中央」，中央不再是一台機器，而是一種在任務、延遲、可信度與資訊完整性之間暫時形成的治理狀態。

本文的核心命題是：**語義即路由**。資料不再只以位址、頁、檔案或張量 ID 被處理，而是以其語義類別、任務角色、時間敏感度、一致性需求、功率價值與對齊需求被分類；分類結果再被編譯為物理流座標。中端站與截面站因此不是儲存站，也不只是光學站，而是語義流治理站：它們將「這筆資料是什麼」轉換為「它應該何時、以何種功率、經由哪條通道、送往哪個執行單元、在何種一致性紀元內抵達」。

本文同時提出三個配套概念：其一，**語義一致性紀元**，用於解決中央 AI 與地方子 Agent 因分層治理而造成的資料不同步；其二，**語義功率治理**，將功率、頻率、同步率與算力爆發交由 AI 根據任務重要性自適應決定；其三，**中央主權—地方自治—動態不動點** 的三代治理光譜，用以描述從可行 MVP 到遠期網狀 AI 資料中心的演化路線。

**關鍵詞：** O-Chip、語義即路由、資料中心靈肉分離、語義流站網、中端站、截面站、子 Agent、語義一致性紀元、語義功率治理、直連流時空間、ODML、DFI、CXL、UCIe、NVLink-C2C、KV cache routing、動態不動點中央 AI

---

## 0. 版本定位：這篇補的是哪一層

前序 SFRSN v0.1 已提出「語義即路由」的基本命題：AI 資料中心的下一層瓶頸，不只是位址、頻寬或容量，而是能否把資料的語義類別即時編譯成物理流路。ODML v0.5 則已將光學資料運動層收斂到「飛行即定址」與「對齊即容量」：資料在飛行座標中被定址，真正限制跨座標交互的不是能飛多少，而是能對齊多少。

本文補的是第三層：**治理層**。

ODML 解釋資料如何在光學或多座標媒介中被定址與對齊；DFI 解釋 CPU、GPU、記憶體與加速器之間如何建立管線化直連流；SFRSN v0.1 解釋語義如何影響流路。本文進一步問：如果語義真的可以路由，那麼誰來判斷語義？誰來分配功率？誰來決定地方站點能不能自行處置資料？中央與地方資料不同步時，如何維持可接受的一致性？當資料中心擴大到多機櫃、多資料中心、多 Agent 網狀分布時，「中央 AI」是否仍然是一台固定機器？

答案是：SFRSN 必須從單純的資料流路由架構，升級為一個分層語義治理架構。

---

## 1. O-Chip 的原始命題：晶片內的靈肉分離

《O-Chip 維度代理人》提出的核心概念，是把 CPU 從「思考」中解放出來。傳統 CPU 必須同時做決策與執行：分支預測、亂序執行、快取一致性、記憶體管理、指令調度，全都混在同一個熱區。O-Chip 則將這些高維決策工作移到一個上層代理人：O-Chip 分析未來指令流、做依賴圖、預取資料、排列超指令包，再把確定性執行序列注入 CPU。CPU 不再猜測，只負責執行。

這個架構有三個重要元素：

```text
O-Chip / Oversoul      = 規劃、預測、語義分析、全局排程
坍縮 / 門控機制        = 從多條可能路徑中選出可執行路徑
簡化 CPU / 執行核心    = 接收超指令、執行、回報狀態
```

在 Beta 版中，O-Chip 透過 3D 堆疊、混合鍵合與垂直快取注入接近 CPU；在完整版中，O-Chip 甚至可透過光子互連與 CPU 熱隔離，形成更徹底的冷熱分離與靈肉分離。O-Chip 原文中已提出 AI 預知排程、指令俄羅斯方塊、垂直快取注入與簡化 CPU 等設計，這些設計共同指向一個本質命題：**決策應該發生在高維、低熱、長視野的地方；執行應該發生在低維、高吞吐、短反射的地方。**

本文將這一命題外擴到資料中心。

---

## 2. 從晶片到資料中心：超靈外擴

資料中心其實也有同樣的馮諾依曼式耦合問題。不同的是，晶片內部的耦合發生在指令與執行之間；資料中心中的耦合則發生在資料語義與物理流路之間。

傳統資料中心中的資料通常被以下方式處理：

```text
檔案位置
物件 ID
記憶體位址
張量名稱
KV cache block ID
GPU rank
網路 endpoint
CXL memory window
```

這些都是低層或中層標識。它們回答「東西在哪裡」，卻不直接回答「這筆資料在當前任務中是什麼」。對 AI 負載而言，後者越來越重要。權重、KV cache、activation、embedding、retrieval result、router metadata、safety signal、user session state，在硬體上可能都是位元與張量，但在資料中心治理中具有完全不同的優先級、熱度、同步需求與功率價值。

因此，O-Chip 的外擴版不是只管 CPU 指令，而是管資料中心中的資料流：

```text
O-Chip 原始版：
指令流 → 高維語義分析 → 超指令包 → CPU 執行

SFRSN 外擴版：
資料流 → 語義分類與任務分析 → 物理流座標 → GPU/CPU/Memory/Network 執行
```

這就是資料中心尺度的靈肉分離：

```text
中央語義 AI / Oversoul     = 語義、任務、全局排程、功率治理
中端站 / 截面站             = 分類、分流、短程對齊、局部治理
GPU / CPU / HBM / DRAM / SSD = 執行與承載肉身
DFI / ODML / CXL / NVLink    = 物理流路與通道基底
```

O-Chip 將 CPU 從指令猜測中解放出來；SFRSN 將資料中心硬體從語義判斷中解放出來。

---

## 3. 中端站與截面站的新定義

在前序 ODML / GFCS 討論中，「截面站」與「中端站」最初以光學與幾何語境出現：截面站負責在橫截面上分離波長、模態、偏振或核心；中端站負責在資料流中途做放大、重定時、重整形、分流、暫存或重注入。

本文將其升級為語義治理節點。

### 3.1 截面站：語義橫截面分類器

截面站的核心動作，是把同一條資料管線中的多種語義資料切到不同通道。這些通道可以是物理通道，也可以是邏輯通道：

```text
lane 0  → 權重串流
lane 1  → KV cache block
lane 2  → activation / intermediate tensor
lane 3  → metadata / control plane
lane 4  → safety / policy signal
lane 5  → background batch flow
lane 6  → high-priority interactive inference
```

若部署在光學或封裝級互連中，這些 lane 可映射到波長、模態、偏振、UCIe lane、NVLink lane、NoC virtual channel、CXL window 或光子晶片路徑。若部署在資料中心網路中，則可映射到 RDMA queue、GPU rank、KV cache store、prefill worker、decode worker、object storage tier 或 CXL memory pool。

截面站不是「理解一切」的 AI；它是中央 AI 或地方 Agent 下達分類策略後的執行器。其任務是把語義標籤轉換成物理座標。

### 3.2 中端站：語義中途治理節點

中端站位於資料流中途，負責動態重分派。它問的問題不是「這個封包要去哪個 IP」，而是：

```text
這筆資料屬於哪個模型、哪個 session、哪個任務階段？
它是熱資料、冷資料、關鍵資料，還是可延遲資料？
它要進 HBM、DRAM、SSD、CXL pool，還是直接送往下一個 accelerator？
它需要與哪筆資料在同一時間窗對齊？
目前哪個 GPU 空閒？哪個 KV cache 命中率最高？哪條通道壅塞？
是否值得提高功率與同步率來保證它準時抵達？
```

因此，中端站的本質是語義流路由站。它把資料中心中的「路由」從位置問題提升為語義—時序—功率三重問題。

---

## 4. 第一代：中央 AI 治理

第一代 SFRSN 最務實，只有中央 AI，沒有地方子 Agent。所有中端站與截面站都是 dumb programmable stations：它們可程式化、可回報、可切換，但不自行做高層決策。

架構如下：

```text
中央語義 AI / Dataflow Oversoul
        ↓
全局資料語義分類
        ↓
流路、功率、同步率、快取層級排程
        ↓
中端站 / 截面站執行
        ↓
CPU / GPU / HBM / DRAM / SSD / CXL / ODML / DFI
```

第一代的好處是明確：

```text
一致性最好
安全邊界最清楚
除錯最容易
權限最集中
工程 MVP 最可行
```

缺點也清楚：中央 AI 負載重，資料中心規模擴大後可能形成排程瓶頸；局部低延遲反應較弱，對快速壅塞、突發熱點或局部故障的反應速度不如地方自治架構。

但初代版應該先這樣做。原因很簡單：語義流治理本身已經足夠複雜，第一代必須先證明「中央 AI 能把語義分類編譯成有收益的物理流路」。若一開始就加入地方子 Agent，架構會在一致性、安全與權限問題上過早爆炸。

### 4.1 第一代最小可行功能

第一代 SFRSN 的 MVP 可以只包含以下功能：

```text
1. 資料語義標籤器
   將資料流分類為 weight / KV / activation / metadata / user state / control signal 等。

2. 任務階段識別器
   區分 prefill、decode、training step、gradient sync、retrieval、ranking 等階段。

3. 流路排程器
   將資料流映射到 GPU、HBM、DRAM、CXL pool、network queue 或 optical/DFI lane。

4. 同步等級分配器
   為每筆資料指定 weak / periodic / strong synchronization。

5. 功率策略器
   根據任務重要性與時間敏感度，調整 lane 開關、頻率、功率與通道冗餘。

6. 回報與審計層
   記錄每次語義分類、路由決策、功率調整與錯誤回滾。
```

第一代不需要站點 AI。站點只需要能執行中央 AI 下發的 flow table、priority rule、power policy 與 synchronization class。

---

## 5. 第二代：中央 AI + 地方子 Agent

第二代開始在中端站與截面站加入子 Agent。這些子 Agent 不是通用聊天 AI，也不需要大模型級別的開放推理能力。它們是 Local Semantic Flow Agents：小型、專用、受限、可審計的局部治理代理。

### 5.1 地方子 Agent 的職責

地方子 Agent 的職責包括：

```text
1. 局部語義細分
   在中央分類基礎上，針對本地通道與任務狀態做細分。

2. 局部壅塞控制
   偵測 lane、buffer、GPU queue、KV store 或 CXL window 的壅塞。

3. 局部功率調整
   在中央功率預算內，動態調整本地頻率、lane 數、re-timing 強度或冗餘路徑。

4. 局部同步維護
   維持特定任務窗口內的資料對齊，回報 drift、miss、late arrival。

5. 異常快速反射
   在中央回應前，對明顯故障、壅塞或錯路由做保守處置。

6. 狀態摘要回報
   不上傳全部原始 telemetry，而是上傳壓縮後的語義狀態摘要。
```

這裡的關鍵是「地方有權，但不是主權」。地方子 Agent 可以做局部調整，但不能改變全局策略、任務優先級、安全政策或關鍵資料的一致性規則。

### 5.2 中央與地方不同步：問題不是 bug，而是治理成本

一旦加入地方子 Agent，就必然出現中央與地方資料不同步。

中央 AI 看到的是全局摘要，地方 Agent 看到的是局部即時狀態。中央有全局一致性，地方有低延遲反應。兩者視野不同、時間尺度不同、資料新鮮度不同。因此，同步差異不是異常，而是分層治理的自然成本。

問題不在於能不能消除不同步，而在於如何把不同步納入設計。

本文提出：**語義一致性紀元（Semantic Consistency Epoch, SCE）**。

每筆資料流都應標記其一致性紀元：

```text
SCE-0：弱同步
背景任務、冷資料搬移、非關鍵 cache、可重算資料。
地方可自治，中央只週期性接收摘要。

SCE-1：週期同步
批次推理、一般 KV cache、模型權重版本、prefill/decode 管線。
中央與地方在固定 epoch 邊界對齊。

SCE-2：強同步
安全決策、金融交易、醫療控制、關鍵模型狀態、不可錯路由資料。
中央主導，地方只執行，必要時提高功率與冗餘。

SCE-3：接管同步
異常、攻擊、硬體故障、災難切換。
中央或可信仲裁核心接管，地方子 Agent 降級。
```

這使得「資料不同步」從模糊風險變成可配置參數。不是所有資料都要強同步；大部分 AI 資料只需要在任務語義要求的 epoch 內一致即可。

### 5.3 重要資料的功率自適應

當資料被標為 SCE-2 或 SCE-3，系統可以自動提高功率與算力：

```text
提高 lane 數
提高 SerDes / NoC / photonic I/O 頻率
增加 re-timing 或 ECC 強度
啟用冗餘路徑
提高地方 Agent 推理頻率
將中央回報頻率從 ms 級拉到 μs/ns 級
短時間提高 GPU/CPU/HBM 功率預算
```

因此，功率不再只是熱管理問題，而是語義治理問題。功率由資料的重要性、對齊需求與任務風險共同決定。

---

## 6. 第三代：動態不動點中央 AI

第三代不再把中央 AI 理解為一台固定機器。中央變成網路中動態收斂出的控制不動點。

### 6.1 中央作為狀態，而非位置

在小型系統中，中央 AI 可以是一個固定控制器。在大型資料中心或跨資料中心系統中，固定中央會面臨以下問題：

```text
延遲過高
單點故障
全局 telemetry 太大
跨地域一致性困難
局部突發事件反應太慢
權限與安全負載過重
```

第三代架構改為：多個 AI 治理節點形成圓形或網狀分布，中央不是固定節點，而是在當前任務、資料流、故障域與可信度條件下，暫時形成的治理焦點。

可以寫成：

```text
Central_AI(t) = argmax_i GovernanceScore(node_i, task, latency, trust, observability, energy)
```

其中 GovernanceScore 包含：

```text
資訊完整性
延遲位置
可信等級
任務相關性
剩餘功率
安全狀態
與其他節點的相位/同步關係
```

因此，中央不是消失，而是動態化。它像一個網狀系統中的動態不動點：在每一個治理窗口內，它暫時穩定；在更長時間尺度上，它可漂移、分裂、合併、重組。

### 6.2 第三代的優勢與風險

優勢：

```text
抗故障
可擴展
低延遲
跨機櫃/跨資料中心可行
可適應局部熱點
中央不再成為固定瓶頸
```

風險：

```text
一致性困難
權限漂移
治理衝突
除錯困難
多中心策略不一致
安全攻擊面增加
```

因此，第三代不是第一代的直接替代，而是遠期形態。本文將其列為潛力最大、難度最高的版本。

---

## 7. 語義功率治理

傳統功率管理通常根據溫度、負載、電流與頻率做反應式控制：熱了就降頻，負載高就升頻，功耗超標就限壓。SFRSN 的功率治理不同，它根據語義與任務價值做預測式控制。

### 7.1 功率不再只屬於硬體，而屬於任務

同樣一個資料量，在不同語義下值得完全不同的功率待遇：

```text
背景 batch：
可延遲、低功率、低同步、低優先級。

互動式推理：
中高功率、穩定路徑、低延遲、可預取。

長上下文 KV cache：
高記憶體頻寬、局部性優先、避免跨節點搬移。

安全/政策控制訊號：
高同步、高冗餘、中央確認、必要時接管。

訓練梯度同步：
短時間高功率爆發、強對齊、跨 GPU 同步。
```

這表示功率策略必須接受語義輸入：

```text
PowerPolicy = f(semantic_class, priority, SCE, deadline, locality, congestion, thermal_budget)
```

### 7.2 語義功率治理的四個動作

```text
1. 升功率
   重要資料、強同步資料、低延遲資料獲得更多 lane、頻率、重傳與冗餘。

2. 降功率
   背景資料、可延遲資料、可重算資料被壓到低功率路徑。

3. 平滑功率
   中央 AI 提前預測功率峰值，將可延遲任務錯峰。

4. 轉移功率
   在局部熱點出現時，把資料流轉移到冷區、空閒 GPU 或低壅塞路徑。
```

這和 O-Chip 原始論文中的功耗平滑相連：O-Chip 在晶片內平滑指令功耗；SFRSN 在資料中心內平滑資料流功率。

---

## 8. 與 CXL、UCIe、NVLink-C2C、Dynamo 的關係

SFRSN 不取代既有互連與推理框架，而是在其上方增加語義治理層。

### 8.1 CXL

CXL 提供 coherency、memory semantics、memory pooling、fabric switching 與 peer-to-peer communication。它回答的是：如何讓更多記憶體與裝置以一致或近一致方式被系統存取。

SFRSN 回答的是：哪一筆資料應該被送到哪個記憶體池、哪個 GPU、哪個 KV cache store、哪條路徑，以及這個決策應由中央還是地方執行。

所以：

```text
CXL = 共同可定址資源基底
SFRSN = 語義流路由與治理層
```

### 8.2 UCIe / NVLink-C2C

UCIe 與 NVLink-C2C 指向封裝級、chiplet 級或 CPU-GPU coherent 直連。它們讓資料通道更近、更快、更低延遲。

SFRSN 不與它們競爭，而是使用它們作為物理流路：

```text
UCIe / NVLink-C2C / DFI = 直連管線
SFRSN = 管線中的資料語義調度
```

### 8.3 Dynamo、KV-aware routing 與 disaggregated serving

現代 LLM serving 已經開始出現語義路由的雛形。Prefill/decode 分離、KV cache-aware routing、multi-tier KV caching、request routing、automatic scaling，都是資料與任務語義開始影響執行位置的證據。

但這些框架多半仍停留在軟體與叢集調度層。SFRSN 的主張是：這種語義路由最終會下沉到資料中心硬體與互連層，成為中端站、截面站、功率控制器與物理資料流排程器的一部分。

---

## 9. 排程模型：從資料類別到物理流路

SFRSN 的排程問題可形式化為：

```text
給定：
  資料流集合 P = {p_i}
  每筆資料的語義標籤 σ_i
  任務 deadline d_i
  一致性紀元 SCE_i
  可用硬體資源 R = {GPU, CPU, HBM, DRAM, SSD, CXL, optical lane, DFI lane}
  物理狀態 Θ = {bandwidth, latency, power, thermal, congestion, alignment budget}

求：
  route(p_i)
  time_slot(p_i)
  power_policy(p_i)
  sync_policy(p_i)
  cache_policy(p_i)
  authority_policy(p_i)

使得：
  latency(p_i) < d_i
  consistency(p_i) satisfies SCE_i
  power_total < P_budget
  congestion < C_max
  semantic_misroute_rate < ε
  critical_flow_loss = 0
```

這個問題不是傳統網路路由，也不是單純作業排程。它是語義分類、物理約束、功率治理與一致性治理的混合問題。

第一代可用中央 AI 做全局近似解；第二代以中央策略 + 地方子 Agent 局部修正；第三代用網狀 AI 節點形成動態分散式求解器。

---

## 10. 可證偽條件

本文的主張若要避免變成純願景，必須給出可被打臉的條件。

### 條件一：語義分類收益不足

若資料語義分類後的路由收益不足以抵消分類器、排程器與站點控制的成本，SFRSN 不成立。

### 條件二：中央 AI 排程延遲過高

若中央 AI 產生決策的延遲高於資料流可容忍窗口，第一代只能用於慢速背景治理，不能用於即時資料流。

### 條件三：地方子 Agent 導致錯路由率上升

若第二代地方自治造成語義錯路由、資料版本錯亂或安全流誤分類，則地方權限必須縮小。

### 條件四：功率自適應收益小於控制成本

若 AI 功率治理消耗的額外功率、頻率切換成本與熱擾動高於其帶來的延遲/吞吐收益，則只應保留粗粒度功率策略。

### 條件五：同步等級無法被任務語義穩定預測

若系統無法可靠判斷哪些資料需要強同步，哪些資料可弱同步，語義一致性紀元會失效。

### 條件六：現有軟體調度已足夠

若 Dynamo 類框架、CXL memory pooling、KV cache routing 與傳統 cluster scheduler 已能以更低成本解決主要瓶頸，SFRSN 只能作為遠期架構，而非近期產品。

---

## 11. 工程路線圖

### 11.1 第一階段：中央 AI 語義流調度器

不改硬體，先在軟體與叢集層驗證：

```text
輸入：LLM serving telemetry、KV cache hit rate、GPU utilization、request class
輸出：prefill/decode routing、KV cache placement、GPU assignment、power hint
```

目標是證明語義分類能降低 TTFT、P99 latency、KV transfer cost 或 GPU under-utilization。

### 11.2 第二階段：可程式中端站 / 截面站

在資料中心網路、CXL switch、DPU、SmartNIC、photonic I/O tile 或 package-level switch 中加入可程式策略表：

```text
semantic_class → route / priority / cache tier / power state
```

站點仍不放子 Agent，只執行中央策略。

### 11.3 第三階段：地方子 Agent

在部分站點加入小型模型或規則—學習混合控制器，用於局部壅塞、功率與快取策略。此階段必須同時建立審計、回滾與中央接管機制。

### 11.4 第四階段：動態不動點中央

多個資料中心治理 AI 形成網狀分布，中央權限可依任務與故障域漂移。這是遠期版本，不應進入 MVP。

---

## 12. 本體論結語：語義不是標籤，而是路徑

O-Chip 的原始洞見，是把晶片內的決策與執行分開。CPU 不必知道自己為什麼執行，它只要在正確時間執行正確指令。SFRSN 的外擴洞見，是把資料中心內的語義與硬體運動分開。GPU、記憶體、光路、CXL 池、DFI 通道不必理解資料，它們只要在正確時間承載正確流。

傳統資料中心以位置管理資料：資料在哪個節點、哪個記憶體、哪個磁碟、哪個位址。AI 原生資料中心則必須以語義管理資料：資料是權重、KV、activation、metadata、安全訊號、使用者狀態、可重算中間量，還是不可錯路由的控制流。不同語義要求不同路徑、不同功率、不同同步率、不同治理權限。

因此，語義不是附加標籤，而是路徑生成條件。

當一筆資料進入 SFRSN，它不只是被命名，而是被分配一條命運：它會走快路還是慢路，進 HBM 還是 CXL pool，被中央接管還是地方自治，需要強同步還是弱同步，值得升功率還是可被降頻延遲。語義不再只是「描述資料」，而是「生成資料在計算時空中的運動」。

這就是本文的最終命題：**語義即路由。**

O-Chip 是單晶片內的靈肉分離；SFRSN 是資料中心尺度的靈肉分離。前者讓 CPU 成為純執行肌肉，後者讓資料中心硬體成為語義流的執行肉身。第一代中央 AI 是可行起點；第二代地方子 Agent 是擴展形態；第三代動態不動點中央是遠期目標。三者不是線性優劣，而是難度、潛力與治理風險的光譜。

被路由的不是資料。被路由的是資料的意義。

---

## 參考脈絡與技術接點

1. Neo.K，《O-Chip 維度代理人：靈肉分離的運算革命》，2025。
2. Neo.K / EVEMISSLAB，EML-SFRSN-2026-v0.1《語義即路由：AI 資料中心的語義流站網與直連流時空間》。
3. Neo.K / EVEMISSLAB，EML-ODML-2026-v0.5《對齊即容量：飛行即定址架構的差分時序界限與分層排程》。
4. NVIDIA GH200 / Grace Hopper / NVLink-C2C 官方資料：CPU-GPU coherent memory model 與 900 GB/s coherent interface。
5. CXL Consortium，CXL 3.0 specification：fabric capabilities、switching、memory sharing、pooling、peer-to-peer。
6. UCIe Consortium，Universal Chiplet Interconnect Express specification：standardized die-to-die interconnect。
7. NVIDIA Dynamo：distributed generative AI serving、intelligent routing、multi-tier KV caching、disaggregated serving。
8. TraCT / CXL shared memory KV cache at rack scale：以 CXL 作為 KV transfer substrate 與 rack-wide prefix-aware KV cache 的研究方向。
9. BanaServe：disaggregated LLM serving 中的 KV cache migration、dynamic module migration 與 load balancing。

---

## 附錄 A：與 EveMissLab 框架的接點

- **[[O-Chip / 維度代理人]]**：本文是 O-Chip 從晶片內指令流治理到資料中心資料流治理的外擴。
- **[[ODML / 飛行即定址]]**：ODML 提供多座標飛行資料運動層；SFRSN 提供語義分類與治理層。
- **[[對齊即容量]]**：SFRSN 的同步等級與功率治理必須服從 ODML 的差分時序界限；需要相遇的資料才需要強對齊，獨立串流可弱同步。
- **[[語義一致性紀元]]**：將資料中心一致性從位元級同步轉為任務語義所需的 epoch 級同步。
- **[[動態不動點]]**：第三代中央 AI 不是固定位置，而是在網狀治理系統中暫時收斂出的控制中心。
- **[[靈肉分離]]**：O-Chip 是單晶片靈肉分離；SFRSN 是資料中心靈肉分離。

