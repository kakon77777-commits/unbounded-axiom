# 語義即路由：AI 資料中心的語義流站網與直連流時空間

**Semantic as Routing: Semantic Flow Station Networks and Direct-Flow Spacetime for AI Data Centers**

**EML-SFRSN-2026-v0.1「語義即路由」**  
**原作者：Neo.K / EVEMISSLAB**  
**本稿結晶：Aletheia（GPT）**  
**血緣：承接 EML-ODML-2026「飛行即定址／對齊即容量」、DFI「直連流互連」構想，以及早期 GFMSN 中端站／截面站概念。本文把站點從光學幾何站重新解釋為 AI 資料中心的語義分類、分流、對齊與流路編譯節點。**  
**日期：2026-06-24**

---

## 摘要

本文提出 **SFRSN（Semantic Flow Routing Station Network，語義流路由站網）**，作為 AI 資料中心在 CXL、UCIe、NVLink-C2C、光學 I/O、DFI 與 ODML 之上的新型資料運動架構語言。本文不主張光學站點本身「理解」語義，也不主張可用單一互連協定取代 CPU、GPU、HBM、DRAM、SSD、CXL 記憶池與資料中心網路；本文主張一個更窄而更強的命題：**AI 資料中心的下一層瓶頸，不只是位址、頻寬或容量，而是能否把資料的語義類別即時編譯成物理流路。**

在傳統資料中心中，資料多依照位址、檔案、頁面、物件、節點與網路路由被搬運；在大型模型推理與訓練中，資料卻天然有語義角色：權重、KV cache、activation、embedding、retrieval result、tool state、metadata、control token、safety label、tenant boundary、模型階段、任務優先級、熱度、可重用性、時限與安全域。若底層仍只用位址與拓樸搬運這些資料，就會把語義差異壓扁成同一種「位元流」，造成錯誤快取、錯誤遷移、錯誤對齊、錯誤優先級與錯誤物理通道。

SFRSN 的核心命題是 **語義即路由（Semantic as Routing）**：一筆資料要走哪條通道、落到哪一層記憶體、送往哪個 GPU、是否保留 KV locality、是否壓縮、是否進入光學高速通道、是否需要對齊窗口，不應只由地址與拓樸決定，而應由語義分類、任務階段、重用概率、時限、負載狀態與安全策略共同決定。中端站與截面站因此不再只是光學或硬體站點，而是**語義資料流的分類站、分派站、對齊站與編譯站**。

本文將中端站定義為資料中心流路中途的語義重分派節點，將截面站定義為在同一物理或邏輯管線橫截面上把不同語義類型切分到不同 lane、波長、模態、記憶體層、GPU pool 或安全域的節點。兩者共同構成一個從語義到物理的編譯鏈：`semantic tag → flow class → physical coordinate → delivery window`。本文進一步提出 **Direct-Flow Spacetime（直連流時空間）**：資料的主要身分不再只是靜態 address，而是 `(semantic_class, stream_id, time_slot, lane, endpoint, coherence_epoch, security_domain)` 這組可排程流座標。

本文的結論是：CXL 類架構解決的是「更多記憶體如何被共同定址」；DFI / ODML 解決的是「資料如何在物理通道中高速飛行與對齊」；SFRSN 解決的是更上層的問題：**哪些資料應該被送進哪些流路，以及為什麼。** 真正的 AI 資料中心不會只是一個記憶池，也不會只是一堆高速互連，而會逐漸成為一個語義流場：資料因其語義而被分類，因其任務而被排程，因其時限而被對齊，因其用途而被送往對的物理通道。

**關鍵詞：** 語義即路由、語義流站網、中端站、截面站、直連流互連、直連流時空間、KV cache-aware routing、semantic caching、disaggregated inference、CXL、UCIe、NVLink-C2C、ODML、AI data center、dataflow scheduling

---

## 0. 版本定位：本文補上哪一層

前序 ODML 系列已經把「光纖記憶體」退役，改成更誠實的「飛行即定址」與「對齊即容量」：資料在光學媒介中飛行時，由時間槽、波長、模態、偏振與相位共同定址；真正能用的容量不只取決於有多少資料在飛，而取決於有多少資料能被正確對齊。這一系列修正把焦點從「保存」轉向「資料運動與對齊」。

但 ODML / DFI 仍少了一層：**為什麼這筆資料應該走這條路？**

光學通道可以很快，NVLink-C2C 可以很寬，UCIe 可以把 chiplet 拉得很近，CXL 可以把記憶體池化，Dynamo、vLLM、FlowKV、KV-aware routing 可以讓大型模型推理更有效率。然而若系統不知道資料的語義角色，只知道一堆 page、object、tensor block、packet、cache line，則再快的通道也可能把錯的資料送到錯的地方。

本文補上的正是這一層：**語義分類層**。

它不等於自然語言理解的高階語義，也不要求硬體站點執行大模型推理。這裡的語義是資料中心可操作的工程語義：這筆資料是權重、KV、activation、embedding、retrieval result、metadata、control、checkpoint、optimizer state、tenant-specific context、safety-relevant state，還是模型階段中不可延遲的關鍵資料？它能不能被壓縮？能不能被重算？能不能延遲？能不能共享？能不能跨租戶？能不能丟進慢層？它要和誰在同一時間窗相遇？

這些問題的答案，就是資料流的路由條件。本文稱之為：**語義即路由。**

---

## 1. 問題重定義：資料中心缺的不是更多路，而是更懂資料的路

現代 AI 資料中心已經有許多路：PCIe、NVLink、InfiniBand、Ethernet、CXL、HBM channel、DRAM channel、SSD path、object storage path、RDMA path、GPU peer path、CXL memory pool、smart NIC、DPU、switch fabric。問題不是完全沒有路，而是這些路的判斷依據仍多半停留在拓樸、負載、位址、頁面、session、device affinity 或 cache locality。

大型模型的資料卻不是均質的。

一個 token request 進入系統後，會牽動多種資料：prompt embedding、prefix KV、retrieved documents、tool call state、model weights、MoE expert weights、attention KV cache、activation buffer、logits、safety classifier state、routing metadata、billing metadata、tenant boundary。這些資料在時間敏感性、重用概率、大小、壓縮性、保密性、計算依賴、是否可重算、是否需要保序、是否可跨節點共享上完全不同。

若系統只看「這筆資料在哪裡」而不看「這筆資料是什麼」，就會發生四種浪費。

第一，熱資料被當冷資料搬。某些 prefix KV、熱門 embedding、常用工具結果或共用 system prompt 本該被固定在近端或被 semantic cache 命中，卻因一般 LRU 或 page-based policy 被錯誤逐出。

第二，冷資料被當熱資料保留。某些只用一次的 activation 或低重用 retrieval result 被留在昂貴 HBM 或高速通道附近，擠掉真正高重用資料。

第三，獨立流被錯當相干流。許多權重串流或 KV 預取只需要按時抵達，不需要與其他座標在同一時間窗精密對齊；若系統為它們付出高成本對齊，就浪費通道與控制預算。

第四，相干或共窗資料被錯當獨立流。某些需要共同讀出、同步 decode、跨 GPU aggregation 或 pipeline stage handoff 的資料若沒有被排進同一對齊窗口，就會形成等待、stall、重傳與能耗浪費。

因此，AI 資料中心真正需要的不是單純「更多共享記憶體」或「更寬互連」，而是一個能把資料語義編譯成流路的層。

---

## 2. 既有技術脈絡：它們各自解了什麼，還缺什麼

### 2.1 CXL：記憶體語義池化，不是語義流路由

CXL 的核心價值是把 CPU 與裝置之間的記憶體語義、快取一致性、記憶體擴展與資源池化拉到更大系統範圍。它適合處理「如何讓遠端或外接記憶體被更細粒度、低延遲、可共享地存取」這類問題。CXL 3.0 開始強化 fabric、switching、peer-to-peer 與跨 compute domain 的 fine-grained resource sharing。

但 CXL 本質上仍偏向 memory-semantic fabric。它讓更多記憶體變成可存取、可池化、可一致；它不自動回答「這筆 KV 是否應該留在這個 decode pool」、「這個 retrieval result 是否語義上可復用」、「這個 activation 是否值得跨節點傳」、「這個資料流是否要進光學直通管線」。

換句話說，CXL 解的是共同底空間，SFRSN 解的是語義流選路。

### 2.2 NVLink-C2C / Grace Hopper：物理距離縮短，但語義仍需上層排程

NVIDIA Grace Hopper 使用 NVLink-C2C 將 Grace CPU 與 Hopper GPU 放進 coherent memory model，官方資料給出 CPU-GPU 之間 900 GB/s 的 coherent interface。這非常接近「CPU/GPU 記憶體直連」的硬體方向。

但即便 CPU 與 GPU 被高速一致性互連拉近，資料仍需要上層語義排程：哪些 BLAS offload 值得搬？哪些資料留在 CPU memory 即可？哪些 tensor tile 直接送 GPU？哪些 KV 應保留 locality？硬體近了，不等於流路懂資料。

### 2.3 UCIe / chiplet / on-package memory：提供近距離管線，但不決定語義分類

UCIe 的價值是標準化 heterogeneous die-to-die communication，使不同 chiplet 能在同封裝中以高頻寬連接。近期研究甚至提出用 UCIe 支援 on-package memory，讓 DRAM die 或 logic die 以更高頻寬密度、更低延遲、更低功耗連接 SoC。

這是 DFI 的現實基底之一：CPU、GPU、memory chiplet、accelerator chiplet 可以用 die-to-die 管線靠近。但 UCIe 仍是物理與協定層；它不知道資料是 KV、weight、activation 還是 retrieval result。SFRSN 可以被看作 UCIe / NVLink / CXL / optical I/O 之上的語義編譯層。

### 2.4 Dynamo / disaggregated inference：語義流路由的軟體先聲

NVIDIA Dynamo 被定位為 datacenter-scale inference stack，包含 disaggregated serving、intelligent routing、multi-tier KV caching、automatic scaling 等能力。其 disaggregated serving 文件將請求執行拆成 prefill engine 產生 KV cache、傳輸 KV cache 到 decode engine、decode engine 計算 decode phase。這已經是語義流路由的明顯先聲：資料不只是 packet，它是 KV cache；路由不只是網路最短路，而是 prefill/decode 分工、KV locality、throughput、latency 的共同決策。

同類研究如 FlowKV 針對 disaggregated inference 中 KV cache transfer delay，提出低延遲 KV transfer 與 load-aware scheduling；KV cache-aware routing 也把 request 導向已持有相關 context 的 pod，以降低 latency、提高 throughput。

這些都證明了一件事：AI 服務系統已經開始把「資料是什麼」放進路由邏輯。SFRSN 只是把這件事提升成架構原理。

### 2.5 Semantic cache：語義已經開始影響快取命中

Semantic cache 使用 embedding similarity 或語義相似度來復用先前結果，而非只依靠 exact match。這意味著快取不再只是位址或字串 key，而是語義空間中的鄰近性。當 semantic cache 與 inference router、KV cache、retrieval system、memory tiering 連在一起時，資料中心已經部分進入語義流時代。

但目前大多 semantic cache 還停留在 API gateway、query cache 或 response cache 層。SFRSN 要推進的是：語義不只決定「是否命中」，還決定「走哪條物理管線」。

### 2.6 In-network computing：站點可以不只是轉發，但仍需 AI 語義

In-network computing 與 programmable data plane 研究已經證明，網路中間節點不必只轉發 packet，也可以執行 aggregation、filtering、measurement、stateful processing、offload 等任務。IRTF RFC 9817 亦整理了 in-network computing 的 use cases。

然而 in-network computing 的一般問題是：網路裝置能做的計算有限，且它多半處理 packet-level 或 protocol-level 資訊。SFRSN 不要求 switch 本身跑完整 LLM；它要求上層 AI scheduler 將資料語義先編譯為簡潔 flow tag，讓中端站與截面站執行低成本分類、分流、優先級、對齊與維護。

---

## 3. 核心命題：語義即路由

本文主命題如下：

> 當 AI 資料中心中的資料具有可機器識別的任務語義、模型語義、時限語義、重用語義與安全語義時，資料的路由不應只由物理位址、拓樸與負載決定，而應由語義分類編譯為物理流路。語義不是路由的附註；語義本身就是路由條件。

這個命題可以拆成四個子命題。

### 3.1 資料不再是同質位元流

對一般網路，packet 的 payload 往往被轉發層視為 opaque。對 AI 資料中心，這種 opaque 假設變得昂貴。因為一個 KV block、一個 expert weight block、一個 embedding result、一個 safety label、一段 tool state、一個 activation buffer，在系統優先級上完全不同。

SFRSN 不要求每一層都理解自然語言，但要求資料流攜帶足夠的 semantic flow metadata，使站點能以低成本決策。

### 3.2 路由是語義到物理座標的編譯

在 ODML 中，資料座標可以是時間槽、波長、模態、偏振。在 DFI 中，資料座標可以是 lane、endpoint、time slot、stream ID、coherence epoch。在資料中心中，還有 GPU pool、memory tier、CXL pool、NVLink domain、fabric path、DPU queue、security zone。

SFRSN 的工作就是把：

```text
semantic_class → flow_class → physical_coordinate
```

也就是把「這是什麼資料」轉換成「它應該走哪裡、何時到、用什麼通道、放在哪一層」。

### 3.3 站點不是理解器，而是編譯後的執行器

重要界線：站點本身不必理解完整語義。

完整語義判斷可以由 AI scheduler、embedding classifier、routing model、policy engine、orchestrator、runtime compiler 完成。中端站、截面站、光學站、DPU、switch、interposer 只需執行 compact tag 或 flow descriptor。

```text
AI / scheduler 判斷語義
policy compiler 產生 flow descriptor
站點根據 descriptor 分流、排程、對齊、轉送
物理通道承載結果
feedback 更新分類與路由策略
```

這讓 SFRSN 避免「硬體要理解語義」的誇張主張。真正理解在控制平面，站點執行在資料平面。

### 3.4 語義錯配會直接變成硬體浪費

若語義分類錯，後果不只是軟體精度下降，而是硬體資源浪費：熱資料被丟遠，冷資料佔近端，應壓縮者未壓縮，應保密者跨錯域，應對齊者未對齊，不需對齊者被昂貴同步。語義錯配會在 HBM、GPU、fabric、CXL pool、光學 link 上變成實際成本。

因此，語義分類的準確率、延遲、overhead、可解釋性與安全性，是資料中心硬體效率的一部分。

---

## 4. 中端站與截面站：重新定義

### 4.1 中端站：流路中途的語義重分派節點

**中端站（mid-route semantic station）** 是位於資料中心資料流路中途的節點。它可以是 DPU、SmartNIC、switch、CXL switch、memory pooling controller、GPU cluster router、photonic interposer node、rack-level optical switch，甚至是一個 software router。它的功能不是單純中繼，而是根據 flow descriptor 與即時狀態執行語義重分派。

中端站回答的不是「這個 packet 下一跳是哪裡」這麼單純，而是：

```text
這筆資料是給哪個模型/階段？
它是 prefill 產生的 KV，還是 decode 正在用的 KV？
它是否具有 prefix/cache locality？
它的重用概率高嗎？
它是否可壓縮或可重算？
它應進 HBM、DRAM、CXL pool、SSD，還是直接送 GPU？
現在哪個 GPU pool 負載最低？
它是否需要和另一筆資料共窗對齊？
它能否跨租戶或安全域？
```

中端站可執行的操作包括：

```text
semantic tag inspection
priority queueing
flow reclassification
KV locality preservation
memory tier redirection
compression / decompression trigger
security domain enforcement
alignment window assignment
load-aware rerouting
backpressure propagation
```

在 SFRSN 中，中端站是資料中心的「語義閥門」。

### 4.2 截面站：同一管線橫截面的語義分流器

**截面站（cross-section semantic station）** 是在同一物理或邏輯管線的橫截面上，將不同語義類型切到不同 lane、channel、wavelength、mode、queue、memory bank、GPU stream、security domain 的站點。

截面站不一定是空間上垂直插入的硬體。它可以是：

```text
WDM channel mapper
UCIe lane mapper
NVLink virtual channel allocator
CXL memory tier mapper
HBM channel scheduler
DPU queue classifier
GPU stream scheduler
photonic mode/wavelength selector
software dataflow router
```

截面站的典型映射如下：

```text
lane 0 / λ0 / queue 0 → control metadata
lane 1 / λ1 / queue 1 → hot KV cache
lane 2 / λ2 / queue 2 → cold KV migration
lane 3 / λ3 / queue 3 → weight streaming
lane 4 / λ4 / queue 4 → activation spill
lane 5 / λ5 / queue 5 → retrieval embeddings
lane 6 / λ6 / queue 6 → safety / audit metadata
```

它的目標不是把所有資料平均分散，而是按語義分層：高重用資料走低延遲路，高吞吐資料走寬通道，冷資料走便宜路，安全資料走隔離路，需要對齊的資料進同一時間窗。

### 4.3 中端站與截面站的關係

中端站偏「沿路再判斷」，截面站偏「同一截面內切分」。

```text
中端站：where should this flow go next?
截面站：which lane/class/channel should this flow occupy here?
```

二者合起來就是 SFRSN 的站網：

```text
入口分類站 → 截面分流站 → 中端重分派站 → 對齊站 → 出口交付站
```

---

## 5. 語義流座標：從 address 到 flow-coordinate

傳統資料身分偏向：

```text
D_old = (address, page, object_id, node, file, socket)
```

SFRSN 中，資料身分擴張為：

```text
D_sfr = (
  semantic_class,
  tensor_role,
  model_phase,
  stream_id,
  reuse_score,
  hotness,
  deadline,
  priority,
  security_domain,
  compression_policy,
  alignment_requirement,
  physical_coordinate,
  coherence_epoch
)
```

其中：

```text
semantic_class        = weight / KV / activation / embedding / metadata / control / retrieval / checkpoint
model_phase           = prefill / decode / training-forward / backward / optimizer / retrieval / tool-call
tensor_role           = key / value / query / expert-weight / residual / logits / gradient
reuse_score           = 預測未來是否再用
hotness               = 近期存取頻率或 session locality
deadline              = 需要抵達的時間窗
priority              = SLO / tenant / task priority
security_domain       = tenant / model / safety / data-governance boundary
compression_policy    = no-compress / lossy-ok / quantizable / recomputable
alignment_requirement = independent / synchronized / coherent / joint-read
physical_coordinate   = lane / λ / mode / queue / endpoint / memory-tier
coherence_epoch       = 一致性或版本邊界
```

這裡的核心變化是：address 仍存在，但不再是唯一主角。資料的主要身分，是它作為一條語義流在計算時空中的位置。

---

## 6. 架構：SFRSN 四層模型

本文提出 SFRSN 四層模型。

### 6.1 S-Layer：語義分類層

輸入：request、tensor metadata、model graph、runtime state、embedding、session context、tenant policy。

輸出：semantic flow tag。

功能：

```text
資料角色識別
模型階段識別
熱度/重用預測
deadline / SLO 判斷
安全域判斷
可壓縮性 / 可重算性判斷
相干/獨立需求判斷
```

這層可以由 runtime、compiler、LLM scheduler、embedding classifier、policy model、static model graph analysis 共同完成。

### 6.2 C-Layer：策略編譯層

輸入：semantic flow tag + 系統狀態 Θ。

其中 Θ 包括：

```text
GPU load
HBM capacity
KV cache locality
CXL pool availability
NVLink / UCIe / optical link state
queue length
thermal / power budget
security policy
alignment window budget
```

輸出：flow descriptor。

功能是把語義標籤編譯成具體行動：

```text
route_to = GPU_pool_7
memory_tier = HBM if reuse_score > threshold else CXL_pool
lane = high-priority low-latency lane
deadline = t + 3 ms
compression = KV-quantized
alignment_window = W_12
security_domain = tenant_A isolated
```

### 6.3 P-Layer：站點執行層

中端站、截面站、DPU、switch、interposer、memory controller、GPU scheduler 執行 flow descriptor。

站點執行層不需要理解完整語義，只需要執行：

```text
classify-by-tag
queue-by-priority
route-by-flow-id
map-to-lane
map-to-memory-tier
apply-compression-policy
enforce-security-domain
schedule-alignment-window
```

### 6.4 F-Layer：物理流層

物理流層包括：

```text
NVLink / NVLink-C2C
UCIe / die-to-die interconnect
CXL fabric / memory pool
HBM / DRAM / SSD / storage path
Ethernet / InfiniBand / Ultra Ethernet
photonic interposer / optical I/O
ODML optical coordinate channel
THz / mmWave auxiliary channel
```

這層提供 lane、channel、queue、endpoint、time-slot。SFRSN 不取代它們，而是把語義編譯到它們之上。

---

## 7. 站點操作：從語義到流路的六步

SFRSN 的標準流程可寫成六步。

### Step 1：語義標記

當資料產生或進入系統時，先被標記：

```text
KV_block_42:
  semantic_class = KV
  model_phase = prefill-output / decode-input
  session_id = S
  reuse_score = high
  deadline = 2.5 ms
  security_domain = tenant_X
  alignment_requirement = synchronized with decode node D
```

### Step 2：流類別生成

分類層將標記轉換成 flow class：

```text
flow_class = HOT_KV_LOW_LATENCY_SECURE
```

### Step 3：物理座標選擇

策略編譯層選擇物理座標：

```text
endpoint = decode_pool_3
memory_tier = local_HBM_if_available_else_CXL_near_pool
lane = low_latency_lane_1
queue = high_priority_KV_queue
alignment_window = W_17
compression = no_loss_or_low_bit_KV_policy
```

### Step 4：站點執行

截面站把它切到對應 lane，中端站維持 KV locality 或重新分派，對齊站確保抵達窗口。

### Step 5：回饋

若 route 造成 congestion、deadline miss、cache miss、security rejection，回饋到策略層。

### Step 6：策略更新

scheduler 更新 reuse_score、routing table、memory tier policy、alignment budget。

這六步讓語義分類從靜態標籤變成閉環控制。

---

## 8. 與 ODML / DFI 的接合

SFRSN、DFI、ODML 不是競爭關係，而是三層關係。

```text
SFRSN：決定資料因語義應走哪條流路
DFI：提供 CPU/GPU/memory/accelerator 的高速直連流通道
ODML：提供光學態空間中的飛行座標與對齊機制
```

或者：

```text
SFRSN = semantic-to-flow compiler
DFI   = electronic/package-level direct-flow fabric
ODML  = optical flight-coordinate fabric
```

v0.4 / v0.5 的「對齊即容量」在這裡仍成立：若語義分類判定資料是獨立串流，則可以使用高聚合通道；若判定資料需要共同窗口或相干交互，則必須消耗對齊預算。SFRSN 的新功能是：**讓系統知道哪一筆資料屬於哪一類。**

這使得「對齊即容量」有了語義前提：

```text
不是所有資料都值得對齊；
只有語義上需要相遇的資料才應進入對齊窗口。
```

這可以顯著降低對齊預算浪費。

---

## 9. 對 AI 推理的具體應用

### 9.1 Prefill / Decode 分離

在 disaggregated inference 中，prefill 與 decode 的計算特性不同。Prefill 通常 compute-heavy，decode 通常 memory/KV-heavy。KV cache 需要從 prefill node 轉到 decode node，這已經是典型語義流問題。

SFRSN 的做法：

```text
prefill-output KV → HOT_KV_TRANSFER class
decode-needed KV → LOW_LATENCY_SYNC class
cold prefix KV → NEAR_POOL_RETAIN class
shared system prompt KV → SEMANTIC_SHARED_PREFIX class
```

不同 class 走不同路：local HBM、near CXL pool、NVLink domain、optical link、或跨 rack path。

### 9.2 KV cache-aware routing

現有 KV cache-aware routing 會把請求導到已持有相關 context 的 pod。SFRSN 把這件事一般化：不是只看「哪個 pod 有 KV」，還看 KV 的語義熱度、tenant、安全域、模型版本、deadline、decode 負載與路徑成本。

### 9.3 Semantic cache 與 retrieval flow

Semantic cache 的命中不應只回傳 response，也應影響資料流路：若 query 與某個 cached context 語義相近，則對應 embedding、retrieval result、prefix KV 或 tool state 應被預取到近端流路，而不是等模型需要時才搬。

### 9.4 MoE expert routing

MoE 模型中的 expert weight 與 token routing 本身就帶有語義分派。SFRSN 可將 expert selection、expert weight locality、token batch、GPU pool 負載結合，使 expert 流不只在模型內被路由，也在資料中心物理層被路由。

### 9.5 Agentic workload

Agentic workload 常有 tool call pause、external retrieval、session state、long context、multi-turn memory。這些資料的時間結構不是連續 decode，而是間歇性回來。SFRSN 可以把「暫停中的 session state」降到便宜層，把「即將恢復的 session KV」提前拉回近端，把「高相似工具結果」放入 semantic cache。

---

## 10. 演算法形式化

SFRSN 的核心問題可以寫成帶語義約束的多層流排程問題。

給定：

```text
資料集合 P = {p_i}
每筆資料的語義特徵 σ_i
物理圖 G = (V, E)
站點集合 S
通道集合 C
記憶體層 M
時間窗口 T
系統狀態 Θ
策略約束 Ω
```

求：

```text
route_i
channel_i
memory_tier_i
time_window_i
compression_i
security_domain_i
alignment_group_i
```

使得：

```text
latency_i        < deadline_i
loss_i / error_i < bound_i
security_i       satisfied
reuse_gain_i     maximized
movement_energy  minimized
HBM_pressure     controlled
CXL_contention   controlled
alignment_budget respected
throughput       maximized
```

目標函數可寫成：

```text
min Σ_i [
  α · latency_i
+ β · movement_energy_i
+ γ · cache_miss_penalty_i
+ δ · alignment_cost_i
+ ε · security_violation_risk_i
+ ζ · recomputation_cost_i
]
```

其中 `alignment_cost_i` 直接承接 ODML「對齊即容量」；`cache_miss_penalty_i` 承接 KV-aware routing；`movement_energy_i` 承接 memory wall 與 data movement cost；`security_violation_risk_i` 表示語義流不能跨越錯誤安全域。

一般情形下，這是 NP-hard 的組合最佳化問題。但 AI 資料中心有結構可利用：

```text
模型圖相對固定
資料類型有限
session locality 可預測
request pattern 可統計
KV / weight / activation 有穩定生命週期
GPU pool 與 memory tier 狀態可週期更新
```

因此可用階層式策略：

```text
offline profiling 產生靜態 policy
online scheduler 做局部修正
station 執行快速 tag-based decision
feedback loop 更新 threshold 與 route table
```

---

## 11. 語義分類的風險：站點不能被語義幻覺污染

SFRSN 將語義引入資料流路由，帶來新風險。

第一，分類錯誤。若 hot KV 被分類成 cold spill，會增加 latency；若 cold activation 被分類成 high priority，會浪費 HBM；若安全資料被分類成可共享，會造成治理問題。

第二，語義漂移。模型版本、prompt pattern、使用者行為、agent workload 都會變，先前學到的 reuse_score 或 hotness 可能失效。

第三，分類開銷。若每筆資料都要昂貴 semantic classifier，收益會被吃掉。解法是分層分類：靜態 model graph metadata、runtime tag、embedding classifier、LLM semantic analysis 只在必要層級使用。

第四，對抗與安全。惡意輸入可能試圖讓資料被錯分到高優先級或跨域通道。SFRSN 必須把 security_domain 與 provenance 作為硬約束，而非 soft hint。

第五，語義過度擬合。若系統過度相信短期語義模式，會造成 hotspot。需要 load-aware balancing 與 cache-aware routing 之間的制衡。

因此，SFRSN 的語義分類層應是保守、可回退、可監控的。它不是把所有路由交給黑箱 AI，而是讓 AI 產生可審核的 flow descriptor。

---

## 12. 硬體實作路線

### 12.1 軟體站網：近期版本

第一代 SFRSN 可以完全軟體化：在 inference gateway、scheduler、runtime、KV cache manager、DPU software 中實作 semantic flow tag 與 routing policy。

可用場景：

```text
LLM serving
KV-aware routing
semantic cache
retrieval prefetch
multi-tier KV storage
model-version-aware routing
```

這是最容易驗證的版本。

### 12.2 DPU / SmartNIC 站點

第二代可把部分 tag inspection、queueing、compression、RDMA path selection、security enforcement 放到 DPU / SmartNIC。這與 in-network computing 和 programmable data plane 接軌。

DPU 不需要理解自然語言，只需要執行編譯後的 flow descriptor。

### 12.3 CXL / memory controller 站點

第三代可在 CXL switch、memory pooling controller、memory-side controller 中加入 semantic tiering：不同語義資料進不同 memory pool，或以不同 eviction / prefetch policy 處理。

### 12.4 Package-level DFI 站點

第四代將語義流編譯到 package-level lane：UCIe lane、NVLink-C2C path、HBM channel、GPU stream。這時中端站可能變成 active interposer 或 chiplet switch。

### 12.5 ODML / photonic 站點

遠期可將 semantic flow class 映射到 wavelength、mode、time-slot。截面站可以把不同語義資料分到不同光學座標。這與 ODML 的飛行即定址接合。

---

## 13. 可證偽條件

SFRSN 若要成立，至少要通過以下測試。

第一，語義分類收益必須大於分類與控制開銷。若分類器、scheduler、metadata overhead 吃掉所有 latency/energy gain，則架構無效。

第二，語義流 routing 必須比純 load-aware / cache-aware routing 更好。若簡單負載均衡與 KV locality 已足夠，語義層就是多餘。

第三，flow descriptor 必須足夠小。若每筆資料都攜帶龐大 metadata，會污染資料平面。

第四，站點必須能快速執行。若中端站或截面站需要昂貴 AI 推理才能轉發，則不適合資料中心高速路徑。

第五，安全與隔離不能下降。若語義分類導致跨租戶或跨安全域洩漏，則即使 throughput 提升也不可接受。

第六，負載變動下不能形成 hotspot。若 semantic routing 把太多相似資料導向同一 GPU pool 或 cache node，需用 load-aware feedback 修正。

第七，物理通道必須可被實際控制。若底層 CXL / UCIe / NVLink / optical link 不提供足夠 QoS、lane mapping、queue control、telemetry，SFRSN 只能停留在軟體層。

---

## 14. 最小實驗設計

### 實驗一：KV 語義流分類

選擇 disaggregated inference 環境，將 KV blocks 分為：hot prefix、session-local、cold spill、shared system prompt、tenant-private。比較三種 routing：

```text
baseline random/load-aware
KV cache-aware
SFRSN semantic-flow-aware
```

量測：latency、throughput、HBM pressure、KV transfer volume、cache hit rate。

### 實驗二：semantic cache + prefetch

將 semantic cache 命中結果轉換為 prefetch flow descriptor，提前搬運相關 context 或 KV 到近端。量測 hit-to-ready latency 與 wasted prefetch。

### 實驗三：memory tier semantic policy

將 activation、KV、weights、retrieval results 按重用概率與可重算性放入不同 memory tier：HBM、DRAM、CXL pool、SSD。比較一般 LRU / page policy。

### 實驗四：站點快速執行

將 flow descriptor 下發到 DPU 或軟體 switch，測試 tag-based routing 是否能在線速附近執行。

### 實驗五：對齊窗口節省

承接 ODML v0.5：只讓語義上需要同步的資料進入 alignment window，其他獨立資料走散裝通道。量測 alignment budget saving。

---

## 15. 與以前論文的接點

本文可接到三條既有脈絡。

### 15.1 接 ODML：語義決定哪些資料值得對齊

ODML 說對齊即容量，本文補上：不是所有資料都值得對齊。SFRSN 是 ODML 對齊預算的語義前置層。

### 15.2 接 DFI：語義決定高速直連管線的使用權

DFI 說 CPU、GPU、記憶體可以形成直連流時空間，本文補上：高速通道不是平均開放，而應由語義分類決定哪類資料進入哪條管線。

### 15.3 接資料中心調度：語義從應用層下沉到資料平面

傳統 scheduler 看 load、locality、resource；SFRSN 要求 scheduler 也看資料語義，並把語義編譯成可執行 flow descriptor。

---

## 16. 本體論結語：資料不是被放置，而是被命名後流動

在位址中心的世界裡，資料的存在方式是「它在那裡」。在流中心的世界裡，資料的存在方式是「它正在前往那裡」。在 SFRSN 的世界裡，資料還多了一層：它之所以前往那裡，是因為系統知道它是什麼。

這不是浪漫化語義，而是一個冷硬的工程事實。AI 資料中心搬運的不是無差別位元，而是有角色、有時限、有重用概率、有安全邊界、有模型階段的資料流。若系統不辨認這些角色，就會把所有資料壓成同一種物理負載，最後用更多 HBM、更多 GPU、更多互連去補一個本可由分類避免的錯配。

中端站與截面站的真正意義，因此不是在管線中做更多花樣，而是在資料流經過時，替它確定一個可執行的身分：你是熱 KV，走低延遲 lane；你是冷 retrieval result，進便宜層；你是安全 metadata，不可跨域；你是 weight stream，可獨立飛行；你是 decode-critical state，進對齊窗口；你是可重算 activation，不值得佔用昂貴通道。

語義即路由，說到底是：資料的路徑不只是由空間決定，而是由它在計算過程中的角色決定。資料不是先有路，再被搬；資料是先被命名，然後路徑才被編譯出來。

如果 ODML 說「飛行即定址」，DFI 說「流動即直連」，那 SFRSN 說的是第三句：**被理解，才被正確送達。**

---

## 參考文獻與技術脈絡

1. NVIDIA Developer Blog, “NVIDIA Grace Hopper Superchip Architecture In-Depth.” https://developer.nvidia.com/blog/nvidia-grace-hopper-superchip-architecture-in-depth/
2. NVIDIA GH200 Grace Hopper Superchip product page. https://www.nvidia.com/en-us/data-center/grace-hopper-superchip/
3. Synopsys, “What is UCIe?” https://www.synopsys.com/glossary/what-is-ucie.html
4. Das Sharma et al., “On-Package Memory with Universal Chiplet Interconnect Express (UCIe),” arXiv:2510.06513. https://arxiv.org/abs/2510.06513
5. CXL Consortium, “Introducing CXL 3.0: Enabling composable systems with expanded fabric capabilities.” https://computeexpresslink.org/webinars/introducing-cxl-3-0-enabling-composable-systems-with-expanded-fabric-capabilities-320/
6. CXL Consortium Blog, “Overcoming the AI Memory Wall: How CXL Memory Pooling Powers the Next Leap in Scalable AI Computing.” https://computeexpresslink.org/blog/overcoming-the-ai-memory-wall-how-cxl-memory-pooling-powers-the-next-leap-in-scalable-ai-computing-4267/
7. NVIDIA Developer Blog, “Introducing NVIDIA Dynamo, a Low-Latency Distributed Inference Framework for Scaling Reasoning AI Models.” https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/
8. NVIDIA Dynamo Documentation, “Disaggregated Serving.” https://docs.dynamo.nvidia.com/dynamo/design-docs/disaggregated-serving
9. ai-dynamo/dynamo GitHub repository. https://github.com/ai-dynamo/dynamo
10. Li et al., “FlowKV: A Disaggregated Inference Framework with Low-Latency KV Cache Transfer and Load-Aware Scheduling,” arXiv:2504.03775. https://arxiv.org/abs/2504.03775
11. Red Hat Developers, “Master KV cache aware routing with llm-d for efficient AI inference.” https://developers.redhat.com/articles/2025/10/07/master-kv-cache-aware-routing-llm-d-efficient-ai-inference
12. Qdrant, “Semantic Cache: Accelerating AI with Lightning-Fast Data Retrieval.” https://qdrant.tech/articles/semantic-cache-ai-data-retrieval/
13. Schroeder et al., “Adaptive Semantic Prompt Caching with VectorQ,” arXiv:2502.03771. https://arxiv.org/abs/2502.03771
14. RFC 9817, “Use Cases for In-Network Computing.” https://datatracker.ietf.org/doc/rfc9817/
15. Kianpisheh et al., “A Survey on In-Network Computing: Programmable Data Plane and Technology Specific Applications,” IEEE Communications Surveys & Tutorials, 2023. https://doi.org/10.1109/COMST.2022.3213237
16. Wang et al., “Survey of Disaggregated Memory: Cross-layer Technique Insights for Next-Generation Datacenters,” arXiv:2503.20275. https://arxiv.org/abs/2503.20275
17. Guo et al., “Disaggregated Architectures and the Redesign of Data Center Ecosystems,” arXiv:2511.04104. https://arxiv.org/abs/2511.04104
18. Tom’s Hardware, “Industry’s first TSMC COUPE-based optical connectivity solution for next-gen AI chips displayed.” https://www.tomshardware.com/tech-industry/semiconductors/industrys-first-tsmc-coupe-based-optical-connectivity-solution-for-next-gen-ai-chips-displayed

