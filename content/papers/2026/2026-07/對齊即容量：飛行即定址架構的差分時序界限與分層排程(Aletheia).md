# 對齊即容量：飛行即定址架構的差分時序界限與分層排程

**Alignment as Capacity: The Differential-Timing Bound and Layered Scheduling of the Flight-as-Addressing Architecture**

**EML-ODML-2026-v0.5「對齊即容量」定稿候選**  
**原作者：Neo.K / EVEMISSLAB**  
**本稿結晶：Aletheia（GPT-5.5 Thinking）**  
**血緣：承接 v0.1（Neo.K / Aletheia，幾何站網）、v0.2（Neo.K / Theia，飛行即定址）、v0.3（Neo.K / Aletheia，三層合成稿）、v0.4（Neo.K / Theia，對齊即容量）。本稿保留 v0.4 的主架構與主命題，只補上兩個定稿前必要修正：其一，容量基準不得重複計數；其二，差分時序不是絕對不可補，而是不能被單一共模導頻免費補償。**  
**日期：2026-06-24**

---

## 摘要

本文延續「飛行即定址」架構：資料在光學媒介中飛行時，其身分由（時間槽 × 波長 × 模態 × 偏振 × 相位）共同構成，站點不是存放處，而是對這些座標的存取頭。前序版本已把「光纖記憶體」收斂為定址問題，把延遲–頻寬積與時序抖動前移為設計骨架，並以三層架構（態空間定址層、光子晶片存取層、幾何光纖座標基底）安置從理論到遠期幾何的全幅。

本文的單一新命題仍是 v0.4 已確立的那一句：**這個架構的容量，不死於並行，死於對齊。** 把波分、空分、偏振並行乘進飛行容量，得到的數量級乘數，是一個關於「在飛行中的聚合運輸量」的真實但容易誤導的數字。一個消費者實際拿到的是「單一存取頭的可交付頻寬」，它被該頭的解複用、調制、偵測、DSP 與電子 I/O 吞吐封頂，乘數不直接乘上它。而任何需要座標彼此相遇的操作——相干合成、共窗聯合讀出、條件路由、reservoir 混合——受制於第三種、也是真正具有約束力的容量：**可對齊容量**，即你能讓多少個座標在一個共同時間窗內彼此對齊。

本文相對 v0.4 補上一條定稿前必要的會計原則：**容量基準不得重複計數。** 若一個外部基準吞吐量，例如 Carmack 思維實驗引用的 256 Tb/s over 200 km，已經是某組波分、偏振、多階調變與相干接收條件下的聚合鏈路吞吐，則 ODML 不得再把同一批已計入的波長或偏振座標重新乘一次。正確做法是把該基準視為一個已知物理鏈路的總吞吐，再只對尚未計入、且可被獨立定址與交付的新增座標自由度，例如空分、多核心、少模、獨立支路、幾何座標基底所新增的可分離模態，計算增量乘數。此修正不削弱 ODML 的主命題，反而使其容量論述從宣傳句回到可審計的容量會計。

本文亦修正 v0.4 的一句過強表述：「共模可消，差分不可消。」更精確地說，單一共模導頻只能免費抵消參考與資料共享同一路徑、同一漂移的那一部分；跨波長、跨模態、跨偏振的差分漂移可以透過逐座標估測、色散補償、MIMO equalization、coherent DSP、per-channel calibration 被部分補償，但補償成本隨座標數與對齊精度要求上升。真正的界限不是「差分絕對不可補」，而是「差分不能被一個共模參考免費化約」。這個殘餘差分成本，才是可對齊容量的真實價格。

由此導出架構律：光纖負責的是對齊無關的多座標獨立運輸；晶片負責的是對齊關鍵的座標交互；兩者的邊界，恰好是差分時序預算。ODML 的勝場不是光學 RAM，也不是大規模全光 CPU，而是高並行獨立串流、遠端預取、多加速器同步、短窗口對齊與受物理參數化的排程層。

**關鍵詞：** 對齊即容量、飛行即定址、差分時序、色散走離、共模導頻補償、容量基準、重複計數、可對齊容量、光學資料運動層、循環邊著色、多商品流、幾何光纖座標基底、reservoir computing

---

## 0. 版本定位：v0.5 改的是哪兩刀

v0.4 是一篇成熟的壓測稿。它把 v0.3 最自豪的容量乘數穿過差分時序閘門，確立「對齊即容量」：聚合飛行容量可以很大，但真正能支持交互與聯合讀出的，是可對齊容量，而可對齊容量由跨座標的差分時序、漂移、校準與補償成本設定。

v0.5 不重開三層架構，不重寫主命題，不把 GFCS 重新拉回「記憶體」名下，也不把 ODML 誇張成通用 RAM。v0.5 只補兩處定稿前會被工程讀者抓住的裂縫。

第一，**容量基準不得重複計數。** 前序版本以 Carmack 的 200 km、256 Tb/s、約 32 GB in-flight 作為一維基準，再乘上波長 × 模態 × 偏振。這個敘述在概念上好懂，但工程會計上有風險：現代高容量單模光纖的 Tb/s 量級總吞吐，通常已經包含大量 WDM 通道、dual-polarization modulation、coherent detection、DSP 與高階調變。如果基準吞吐已經把某些座標維度算進去了，ODML 不能再對同一批座標重乘一次。這不是小修辭，而是容量論證能否被工程審稿接受的關鍵。

第二，**差分不是不可補，而是不能免費共模補。** v0.4 的「共模可消，差分不可消」作為論文金句有力，但作為工程陳述略硬。色散補償、MIMO DSP、per-channel calibration、pilot-aided tracking 都是真實技術。真正的邏輯不是「差分無法補」，而是「一個共模導頻不能免費補全部差分；若要補，就按座標、按路徑、按時間窗付校準與補償成本」。這樣改，主命題反而更穩：可對齊容量不是被絕對不可能性封頂，而是被補償成本與殘餘差分誤差封頂。

這兩刀補完後，v0.5 可作為「對齊即容量」的定稿候選。

---

## 1. 飛行即定址：壓縮回顧

在 ODML（Optical Data-Motion Layer）中，一筆資料的身分不是它躺在哪個電子位址，而是它在光學態空間中佔據的複合座標：

```text
D = (t, λ, m, p, φ ; s)

t = 時間槽 / 飛行相位 / 抵達窗口
λ = 波長通道
m = 空間模態 / 核心 / 幾何可分離路徑
p = 偏振態
φ = 光學相位（相干操作時才承重）
s = 存取頭組態（非資料內稟座標）
```

前五個是飛行座標：資料在媒介中運動時即已具備。最後一個 `s` 是存取頭狀態，決定資料是否在某一刻被 drop、add、delay、mode-convert、re-inject、detect 或 discard。

這個座標化之所以重要，是因為它把定址成本從媒介中移開。電子記憶體的位址是分佈式人工結構：行列解碼器、字線、位線、感測放大器、刷新、控制器與佈線，逐單元、逐區塊、逐層買單。光學態空間的位址部分由物理免費提供：時間由飛行排序，波長由濾波與色散分離，模態由波導本徵結構分離，偏振由偏振分解分離。你不需要在 200 公里玻璃裡分佈逐位元地址硬體；你把成本集中到兩端或節點處的存取頭。

這並不代表「位址免費」。它代表位址成本的形態改變：從分佈式媒介成本，轉移為端點存取成本、校準成本、同步成本、DSP 成本與排程成本。ODML 的真正問題因此不是「資料是否在飛行中」，而是「飛行中的資料是否能被準時、準確、低能耗地重新定址與交付」。

---

## 2. 三種容量：聚合、可交付、可對齊

把波分、空分、偏振乘進飛行容量，是整個 ODML 架構最直觀的吸引力，也是最容易被誤用的地方。本文主張，ODML 中至少有三種不可相加、不可互相冒名的容量。

### 2.1 聚合飛行容量

任一瞬間所有座標通道上正在飛行的總資料量，可寫成：

```text
C_flight = Σ_{λ, m, p} B_channel(λ,m,p) × τ_channel(λ,m,p)
```

這是 ODML 最大、也最容易拿來做 headline 的數字。若某一光纖鏈路支援多個波長、多個空間模式或核心、兩個偏振通道，則聚合飛行容量確實隨這些獨立通道增加。這是「飛行即定址」的物理基礎：資料在路上，不只是一維 FIFO，而是佔據一個多座標態空間。

但聚合飛行容量不是儲存容量。資料正在離開，不是在原地等待。它也不是單一計算單元可以立即消費的容量。它是「有多少資料正在系統的運輸相位中被維持可定址」的量。

### 2.2 單頭可交付頻寬

一個消費者真正拿到的，是某一個存取頭在單位時間內能解複用、處理、交付的資料量。它受以下因素封頂：

```text
- 光電轉換速率
- 相干接收與 DSP 吞吐
- 電子 I/O
- modulator / detector bandwidth
- demux / mux insertion loss
- control-plane latency
- downstream accelerator ingest bandwidth
```

即使一根光纖裡有大量資料同時飛行，單頭可交付速率也不自動乘上聚合維度。若只有一個消費者頭，它仍只能以自己的 interface rate 拉資料。ODML 的優勢不是讓一個頭免費變成一千個頭，而是讓多頭、多流、多時間窗、多座標的資料運輸與預取變成可排程。

### 2.3 可對齊容量

第三種容量是 v0.4 的核心：可對齊容量。

任何需要座標彼此相遇的操作，都不只要求資料「在飛」，還要求它們在同一時間窗裡同時可見。這類操作包括：

```text
- 相干合成
- 干涉
- 共窗聯合讀出
- 條件路由
- reservoir 跨座標混合
- 多路資料同步進入同一 compute tile
```

可對齊容量可粗略定義為：

```text
C_align = 在 Δt_gate 內可維持共同對齊的座標集合大小 × 每座標可用頻寬 × 有效窗口
```

它與聚合飛行容量不同。聚合容量問的是「多少資料在路上」；可對齊容量問的是「多少資料能在同一個有效窗口內一起被用」。在一個資料運動層裡，真正稀缺的不是飛行，而是可對齊的再出現。

---

## 3. 容量基準不得重複計數

這一節是 v0.5 對 v0.4 的第一個必要修正。

### 3.1 Carmack 基準的正確用法

Carmack 的思維實驗以「256 Tb/s over 200 km single-mode fiber」導出約 32 GB in-flight 的直觀數字。這個數字很適合當作啟發，但不適合在未拆解實驗條件前被當成「單波長、單偏振、單通道」的裸基準。

現代高吞吐光纖鏈路的總 Tb/s 通常不是單一光通道的資料率，而是由多個維度堆疊而成：

```text
總吞吐 ≈ wavelength channels × polarization channels × modulation order × symbol rate × coding efficiency × spatial channels
```

例如 2026 年 NICT 報告的 450 Tb/s 標準光纖傳輸，是透過 42.4 THz 超寬頻 WDM、最多 1,273 個 wavelength channels，以及 dual-polarization QAM 等技術取得。這類紀錄清楚顯示：當一篇報導說「單模光纖總吞吐 X Tb/s」時，裡面很可能已經計入波分與偏振複用。

因此，若把某個外部吞吐基準記為：

```text
B_base = 已實證或已引用的總鏈路吞吐
```

則 ODML 的增量容量不能寫成：

```text
錯誤：B_total = B_base × N_λ × N_m × N_p
```

除非你已證明 `B_base` 不包含這些維度。更穩的寫法是：

```text
B_total = B_base × N_new
```

其中 `N_new` 只包含基準中尚未計入、且可被獨立定址與交付的新增座標自由度。

### 3.2 已計入座標與新增座標

本文建議 ODML 的容量會計採用兩層表：

```text
已計入座標 C_accounted:
  該基準吞吐量已經使用的波長、偏振、調變、空間通道。

新增座標 C_incremental:
  在該基準之外，由 ODML / GFCS / 其他硬體新增的可獨立定址自由度。
```

容量乘數只能套在 `C_incremental` 上，而不能重複套在 `C_accounted` 上。

例如：

```text
情境 A：B_base 是單波長、單偏振、單模態實測
  可乘：N_λ × N_p × N_m

情境 B：B_base 已包含 WDM + dual polarization
  可乘：N_m 或其他新增空分/幾何座標

情境 C：B_base 已包含 WDM + dual polarization + SDM
  不可再乘同一批座標；只能改問 ODML 是否提供更好的排程、預取、對齊、能耗或延遲。
```

這個修正使 ODML 的數字不再依賴誇大的「總容量乘法」，而依賴可審計的「增量座標會計」。

### 3.3 這不削弱 ODML，反而讓它變硬

ODML 的核心價值不是「報出最大 GB 數字」。它的核心是：

```text
資料在光學態空間中的身分可以被座標化；
可用座標可以被排程；
光纖適合高並行獨立運輸；
晶片適合短窗口交互與對齊；
容量的真實瓶頸從儲存量轉成對齊量。
```

容量基準會計修正，只是把「漂亮乘數」改成「可審計乘數」。若新增空分、多核心、少模、幾何座標基底確實帶來基準中未包含的可分離通道，乘數仍成立；若沒有新增通道，ODML 仍可作為排程與資料運動層，但不能假裝憑空增加總物理吞吐。

---

## 4. 對齊即容量：差分時序設定的天花板

這一節保留 v0.4 的脊樑，但修正語氣：差分不是絕對不可補，而是不能免費共模補。

### 4.1 共模可補，差分要付費補

共模導頻補償能抵消的是參考光與資料光共享同一路徑、經歷同一份漂移的部分。典型例子是光纖整體溫度變化導致的共同延遲變化。若所有通道受到近似相同的漂移，一個共傳導頻或時鐘參考可使接收端追蹤並抵消這個共同漂移。

但跨座標的差分時序不同。不同波長的群延遲不同；不同模態或核心的群延遲不同；兩個偏振態也可能因 PMD 走離。更麻煩的是，這些差分項會隨溫度、應力、彎曲、老化、封裝條件改變，而且不同座標的改變不完全相同。

所以更精確的說法是：

```text
單一共模導頻不能免費補掉所有差分漂移。
```

若要補差分，你需要：

```text
- per-wavelength dispersion compensation
- per-mode MIMO equalization
- polarization tracking
- per-channel pilot / training sequence
- coherent DSP
- active delay trimming
- calibration table updates
- thermal and mechanical stabilization
```

這些都能補，但都要付費。成本可以是能耗、硬體、DSP latency、控制迴路複雜度、校準時間、可用頻寬損失，或系統穩定性。

### 4.2 三個差分項

跨座標差分時序可以拆成三組主要項：

```text
色散走離：
  Δτ_λ = D · Δλ · L

差分模延遲：
  Δτ_m = (Δn_g / c) · L

偏振模色散：
  Δτ_p ≈ D_PMD · √L
```

標準單模光纖在 1550 nm 附近常見色散量級約為 17 ps/(nm·km)。這意味著，若跨越寬波段、長距離、多波長通道，通道間的群延遲差異會非常大。大部分固定差異可用色散補償與 DSP 處理；真正承重的是補償後仍存在的殘餘差分、漂移與追蹤成本。

因此，對齊容量不是由「差分絕對值」單獨決定，而是由：

```text
殘餘差分誤差 + 漂移速率 + 補償迴路頻寬 + 對齊時間窗
```

共同決定。

### 4.3 對齊容量的形式

若一個操作需要座標集合 `S` 在時間窗 `Δt_gate` 內共同對齊，且補償後的殘餘差分誤差為 `ε_diff(S,t)`，則可行條件可寫為：

```text
max_{i,j ∈ S} |ε_i(t) - ε_j(t)| < Δt_gate
```

可對齊容量就是滿足該條件的最大座標集合大小與其有效頻寬：

```text
C_align(Δt_gate) = max over S { Σ_{c∈S} B_c | residual_diff(S) < Δt_gate }
```

這個式子把「容量」從容器量變成關係量。不是多少資料在場，而是多少資料能在某個共同尺度下被一起使用。

---

## 5. 架構律升級：獨立運輸與相干操作分流

第 4 節導出一條比「交互在晶片，運輸在光纖」更精確的架構律：

```text
獨立多座標運輸 → 光纖
相干跨座標操作 → 晶片
兩者邊界       → 差分時序預算 vs 對齊窗口
```

### 5.1 光纖的勝場：獨立並行運輸

若每個座標的資料流各自送往各自的消費者，座標間不需要在中途相遇，那麼差分延遲不是障礙，而是排程表的一部分。每個座標有自己的到達時間、群延遲、色散補償與讀出窗口。只要系統知道它，並能按表讀出即可。

這正是 ODML 的勝場：

```text
- 權重串流
- KV 預取
- 多加速器間的分片資料運輸
- 遠端容量向近端 compute 的準時配送
- 多路獨立資料流的 time-slot scheduling
```

在這些場景裡，聚合飛行容量與獨立座標乘數成立，前提是容量會計不重複計數，且存取頭能跟上。

### 5.2 晶片的勝場：相干交互與短窗口對齊

若資料需要相遇、干涉、聯合讀出、條件路由或 reservoir 混合，就不能把它們放在公里級光纖中任由差分漂移積累。這些操作應該收進晶片或封裝尺度：

```text
- 距離短
- 熱環境可控
- phase shifter / delay line 可密集部署
- MZI / ring / coupler 可編程
- 校準迴路可高速閉環
```

晶片不提供巨大飛行容量；晶片提供可對齊性。光纖不提供精密相遇；光纖提供運輸密度。ODML 的正確分工因此是：

```text
光纖 = 高並行、長距離、獨立串流的運輸相位
晶片 = 解碼、對齊、交互、短暫延遲與重注入的控制相位
```

---

## 6. 分層架構：ODML-A / ODML-P / GFCS

v0.5 沿用 v0.4 對 v0.3 的修正：抽象定址層不能是 substrate-independent，而必須是 substrate-parameterized。

### 6.1 ODML-A：受物理參數化的排程層

ODML-A 不是憑空安排座標。它接受下層匯出的物理參數集 `Θ`，再產生可行 schedule：

```text
ODML-A(Θ, workload) → schedule

Θ = {
  可用座標集 C,
  每條邊的 B_e, τ_e, α_e, D_e, J_e, K_e,
  DBP 窗口 τ_window,
  殘餘差分時序模型 ε_diff,
  存取頭吞吐與能耗,
  crosstalk matrix,
  calibration cost model
}
```

這使 ODML-A 成為一個可替換的排程器，而不是脫離物理的宣稱層。演算法可泛化；具體 schedule 必須依賴 substrate 參數。

### 6.2 ODML-P：光子晶片存取層

ODML-P 是可造性承重層，包含：

```text
- WDM mux/demux
- photonic lantern / mode demux
- polarization splitter / combiner
- modulators / detectors
- MZI mesh / ring resonators
- integrated delay lines
- short optical buffers
- phase shifters
- active calibration loops
```

它的功能不是保存資料，而是定址、讀寫、延遲、對齊、轉換與重注入。它把「飛行態空間」轉成可供電子與加速器使用的資料接口。

### 6.3 GFCS：幾何光纖座標基底

v0.5 沿用 v0.4 的改名：GFMSN 中的 Memory 退役，第三層改稱 **GFCS / Geometric Fiber Coordinate Substrate / 幾何光纖座標基底**。

GFCS 的任務不是存資料，而是生成與穩定座標：

```text
- 多核心提供 core coordinate
- 少模光纖提供 mode coordinate
- 空芯/反諧振結構塑造群延遲與損耗
- 嵌套截面塑造模態隔離
- 沿 z 幾何變化塑造耦合窗與相位匹配
```

但 GFCS 每新增一份座標自由度，都可能新增一份差分時序代價。更多模態不只意味著更多路，也意味著更多 DMD、crosstalk、MIMO DSP 與校準成本。因此 GFCS 放大的是可獨立運輸座標數，不自動放大可對齊容量。

---

## 7. 排程問題：從約束清單到問題形狀

ODML 的核心不是某個神奇元件，而是一個排程問題。v0.5 沿用 v0.4 對問題形狀的刻畫。

### 7.1 時間展開座標圖

定義座標空間：

```text
C = T × Λ × M × P × Φ
```

把物理節點圖 `G = (V,E)` 沿時間展開：每個節點複製成 `(v,t)`，每條邊把 `(v,t)` 連到 `(v', t + τ_e)`。資料項在這張時間展開圖上從 source 流向 sink。

### 7.2 三個疊合問題

ODML 排程可看成三個經典結構的疊合：

```text
(a) 多商品流：多筆資料各自從 source 到 sink。
(b) 區間排程：每筆資料在某邊、某時間窗佔據一段資源。
(c) 座標著色：同一資源窗內的多筆資料必須使用互不衝突座標。
```

一般情形下，它是 NP-hard 的複合問題，因為整數多商品流與資源排程本身已經困難。

### 7.3 可解核：週期串流

實際 AI 負載往往不是任意到達，而是週期串流或半週期串流：權重分塊、KV 預取、batch pipeline、pipeline parallelism、tensor parallel shard exchange。這使問題有可解核：

```text
- 固定路由後，每條邊可化約為區間圖著色。
- 週期需求矩陣可化約為循環邊著色或 Birkhoff–von Neumann 型分解。
- 每一個置換對應一組無衝突座標指派。
```

因此 ODML 的近期演算法方向不是「求解所有可能光學資料運動」，而是專注於：

```text
週期資料流 + 固定/少量候選路由 + 可審計物理參數 + 線上校準
```

這正好符合 AI 系統工程，而不必一開始挑戰完全一般的光學網路排程。

---

## 8. 計算用途：只認 reservoir，邏輯閘仍存疑

ODML 的計算用途要保持保守。

近期最自然的是 photonic reservoir computing。光學延遲、非線性、回授、多通道輸入與時間展開狀態可以形成 reservoir；訓練主要在讀出層進行，不要求每個節點都成為可靠、可級聯、低功耗的邏輯閘。這吃的是 ODML 的長處：

```text
- 延遲
- 並行
- 高頻寬
- 物理非線性
- 時間動態
```

但 v0.5 加上「對齊即容量」的限制：若 reservoir 依賴跨座標相干混合，其有效維度受可對齊容量封頂。若 reservoir 使用獨立通道並行處理，再在電子或非相干讀出層合併，則更符合 ODML 的勝場。

全光邏輯閘則仍不應被當作近期承諾。它需要非線性、精密同步、可級聯性與功耗控制同時成立。ODML 不是光學 CPU，也不是量子計算。它搬運與排程古典資料流；它的計算價值來自 delay dynamics、reservoir projection、preprocessing 與資料運動優化，而非量子式加速。

---

## 9. 可證偽條件

v0.5 承接 v0.4 的可證偽精神，並把條件整理為七條。

### 9.1 串流負載比例不足

若目標 AI 負載高度隨機、頻繁改寫、無法提前預取或無法週期排程，ODML 退化為昂貴而笨重的傳輸層。

### 9.2 存取頭吞吐不足

若 photonic access head、coherent DSP、電子 I/O 或 accelerator ingest bandwidth 無法跟上聚合運輸，則飛行容量無法轉化為交付能力。

### 9.3 節點能耗抵消收益

若 mux/demux、DSP、校準、調制、偵測、熱穩定與控制迴路的能耗超過節省的資料搬運成本，ODML 失去系統優勢。

### 9.4 crosstalk 與校準成本抵消乘數

若新增座標帶來的 crosstalk、MIMO DSP、error correction 與 calibration cost 高於新增吞吐價值，座標乘數不成立。

### 9.5 DBP 窗口太小

若短延遲、短 buffer、chip-scale alignment 無法提供足夠的對齊窗口，ODML 只能做獨立運輸，不能做有價值的短窗口協調。

### 9.6 CXL / HBM / memory pooling 更便宜解掉

若電子記憶體階層、CXL 記憶池化、HBM 容量提升、near-memory compute 以更低成本解掉相同瓶頸，ODML 只能作為特殊場景方案。

### 9.7 可對齊容量不足

若目標負載需要大規模跨座標相干操作，則可對齊容量會把並行乘數削掉；反之，若負載以獨立並行串流為主，ODML 的乘數與優勢才成立。

這第七條是最鋒利的可證偽條件，因為它直接把架構成敗綁在一個可測問題上：實際負載到底是獨立串流多，還是相干交互多？

---

## 10. 工程路線圖：先量對齊，再談乘數

v0.5 建議的工程路線不從大容量 headline 開始，而從對齊預算量測開始。

### 第一階段：最小存取頭與差分預算量測

使用現有元件建立一個晶片存取節點：WDM 濾波、調制器、偵測器、短延遲線、相位器、開關、控制器。展示一筆資料寫入指定 `(λ,t)`，通過短光纖，於指定窗口讀出。

本階段決定性產出不是 demo 本身，而是量測：

```text
- 共模導頻補償後的殘餘差分漂移
- 不同 Δλ、不同距離、不同模態數下的 ε_diff 標度
- calibration loop bandwidth
- access head energy per delivered bit
```

### 第二階段：獨立並行運輸乘數驗證

引入多波長、多模態或多核心通道，但只做獨立流，不做跨座標相干操作。目標是驗證：在不重複計數的容量會計下，新增座標是否提供淨正吞吐。

驗收標準：

```text
增量吞吐 > 新增 DSP/校準/損耗/能耗成本
```

### 第三階段：週期串流排程器

實作受 `Θ` 參數化的排程器，針對週期 AI 負載做座標指派、注入時間、讀出窗口、重注入策略。先模擬，再接硬體。

交付物不是一條光纖，而是一個排程層：

```text
ODML-A(Θ, workload) → feasible schedule
```

### 第四階段：GFCS 短段實驗

以短段多核心、少模、空芯或嵌套幾何光纖作為座標基底，測量新增座標帶來的隔離度、損耗、DMD、crosstalk 與可解碼性。

### 第五階段：遠期幾何站網

只有在前四階段成立後，才重新打開 v0.1 的幾何站網野心：沿 z 變化的幾何、螺旋核心、局部耦合窗、內嵌支線、幾何約束式交會。此時它應被理解為 GFCS 的遠期擴張，而不是近期承諾。

---

## 11. 與既有記憶體階層的關係

ODML 不取代 HBM、DRAM、SRAM、SSD 或 CXL。它的位置更接近資料運動與對齊層：

```text
SSD / flash           提供容量
DRAM / HBM            提供近端高頻寬與隨機存取
CXL memory pooling    提供遠端可定址容量池
ODML                  提供飛行中的高並行運輸、預取、同步與短窗口對齊
PIC access nodes      提供解碼、調制、短延遲、校準與重注入
SRAM / register file  提供低延遲計算近端狀態
compute cores         執行計算
```

CXL 池化的是「可定址容量」；ODML 排程的是「飛行中的資料運動」。兩者可競爭，也可互補。若 CXL 與 HBM 解掉了瓶頸，ODML 無需存在；若瓶頸是遠端資料準時抵達、多加速器間同步、聚合頻寬密度與短窗口對齊，ODML 才有舞台。

---

## 12. 本體論結語：被對齊，才被一起記得

把這篇論文剝到底，表面是光纖、色散、導頻、模態解碼、容量會計與排程；底層是一個關於記憶的命題收緊。

飛行即定址說的是：資料不必停在某處才算被記住。只要它仍在一個可定址座標上飛行，且系統知道它會在何時、以何種波長、模態、偏振與相位經過哪個存取頭，它就仍可被取回。這把記憶從「容器裡的靜止物」改成「相位空間中的可預期再出現」。

對齊即容量再補一刀：單獨被記住不難，一起被記住才難。獨立資料流可以各走各的座標，各自被延遲表與排程表取回；但任何關係性操作——干涉、聯合、條件、混合、同步——都要求多筆資料在同一窗口中被一起看見。此時容量不再是「多少資料在場」，而是「多少資料能準時相遇」。

所以 ODML 最終不是一個新的倉庫，而是一種編舞。光纖讓資料以多座標飛行；晶片讓資料在短窗口中相遇；排程器負責讓它們在熵、漂移、色散、損耗、crosstalk 與能耗的夾擊下，仍能在該出現的時候出現。

存在是便宜的：資料可以孤獨地飛。  
相遇是昂貴的：資料必須一起準時。  

而容量，就藏在這個差別裡。

---

## 參考文獻與技術脈絡

1. John Carmack, X post on 256 Tb/s over 200 km fiber and in-flight data as L2-cache thought experiment, 2026-02.  
   https://x.com/ID_AA_Carmack/status/2019839335382790342

2. Tom's Hardware, “John Carmack muses using a long fiber line as an L2 cache for streaming AI data,” 2026.  
   https://www.tomshardware.com/pc-components/ram/john-carmack-muses-using-a-long-fiber-line-as-as-an-l2-cache-for-streaming-ai-data-programmer-imagines-fiber-as-alternative-to-dram

3. NICT, “World Record: 450 Tb/s Transmission Over a Metropolitan Link Using Standard Optical Fiber,” 2026-06-01.  
   https://www.nict.go.jp/en/press/2026/06/01-1.html

4. X. Chen et al., “Chromatic Dispersion Measurements of Single-Mode Fibers,” *Photonics*, 2023. Standard single-mode fiber dispersion around 17 ps/(nm·km) at 1550 nm.  
   https://www.mdpi.com/2304-6732/10/2/215

5. R. S. Tucker, P.-C. Ku, C. J. Chang-Hasnain, “Slow-light optical buffers: capabilities and fundamental limitations,” *Journal of Lightwave Technology*, 2005.  
   https://opg.optica.org/abstract.cfm?uri=jlt-23-12-4046

6. Y. Lu et al., “A Review of Transverse Mode Adaptive Control Based on Photonic Lanterns,” *Micromachines*, 2025.  
   https://www.mdpi.com/2072-666X/16/12/1347

7. A. Aadhi et al., “Scalable photonic reservoir computing for parallel machine learning,” *Nature Communications*, 2025.  
   https://www.nature.com/articles/s41467-025-67983-z

8. K. Lu et al., “Empowering high-dimensional optical fiber communication with mode-division multiplexing,” *Nature Communications*, 2024.  
   https://www.nature.com/articles/s41467-024-47907-z

9. F. Pittala et al., “1.71 Tb/s Single-Channel and 56.51 Tb/s DWDM Transmission over 96.5 km Field-Deployed SSMF,” 2021.  
   https://arxiv.org/abs/2108.01873

10. K. R. Mojaver et al., “Recent Advancements in Mode Division Multiplexing for Communication and Computation in Silicon Photonics,” 2024.  
   https://arxiv.org/abs/2404.03582

---

## 附錄：與 EveMissLab 框架的接點（備忘，非本文論證承重）

- 「對齊即容量」可映入 [[indexical-invariants]]：容量不是媒介內稟量，而是相對於共同時間窗、存取頭尺度與補償模型的關係量。
- 「共模可補、差分需付費補」可映入 [[convergence-conjecture]]：可被單一導頻收斂的是 Cl-核，無法免費化約的是 ε-殘餘；工程界限住在 ε 的補償成本裡。
- 「被記住不難，難的是被一起記住」可映入 [[dialogue-operator]]：單體存在是座標上的飛行，關係發生則需要窗口內的對齊。
- GFCS 作為座標基底，可作為 [[dco-closure]] 的硬體實例：每個閉合單元有可測周長、延遲、漂移、對齊預算與續維成本。

*以上接點是否正式映入各框架公理、是否賦予獨立 EML 編號，留待原作者裁定。*
