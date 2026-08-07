# 迷你具身智能的本地計算核心：Jetson、x86、ARM 與外部主腦

**系列：狀態驅動的本地具身 AI｜第 6 篇**  
**版本：v0.1**  
**日期：2026-08-01**

---

## 摘要

當一台迷你陪伴機器人需要同時完成即時控制、語音、視覺、世界狀態維護、小模型推理與按需大型模型調用時，「把所有功能塞進一塊最強晶片」並不是唯一、也通常不是最好的硬體策略。真正的問題是：哪些工作必須在機器人體內、哪些工作可以放在本地外部主機、哪些工作可以延後到雲端，以及不同層級之間如何在網路中斷、模型失效與電量下降時保持降級運作。

本文將迷你具身 AI 的本地計算拆成五種物理角色：MCU 即時控制器、低功耗感知 SoC、邊緣 AI 主控、局域網／個人外部主腦，以及雲端前沿模型。以 2026 年公開硬體為參考，NVIDIA Jetson Orin 仍是機器人原型與邊緣生成式 AI 的成熟選擇；Jetson Thor 已大幅提高至 128 GB 記憶體與高階 Blackwell 計算，但 40–130 W 功耗使它更接近大型機器人、移動平台或邊緣伺服器，而不是桌面大小以下的迷你陪伴機器人。Qualcomm RB5 類平台代表另一條低功耗 ARM 異質運算路線；Raspberry Pi 5 加 AI HAT+ 2 則顯示 2026 年的低成本 SBC 已可在附加 8 GB AI 記憶體與 40 TOPS INT4 加速器的情況下運行約 6B 級 LLM/VLM。

在 x86／高記憶體外部主腦方面，AMD Ryzen AI Max+ 395 的 128 GB LPDDR5x、256 GB/s 記憶體頻寬與大型整合 GPU 展示了一種與手機、機器人高度相關的設計思想：本地模型的關鍵不只是 NPU TOPS，而是「可被模型真正使用的記憶體容量、頻寬與軟體堆疊」。Apple M4 Pro Mac mini 可提供最高 64 GB 統一記憶體與 273 GB/s 頻寬，也適合作為局域網低噪音外部主腦，但不是典型嵌入式機器人模組。

本文最終提出：迷你具身 AI 的最佳硬體不是一顆「超級腦」，而是一個可分離、可降級的計算拓撲：

$$
\text{MCU}
\rightarrow
\text{Always-on Edge}
\rightarrow
\text{Local AI SoC}
\leftrightarrow
\text{External Personal Brain}
\leftrightarrow
\text{Cloud}.
$$

這個拓撲直接為下一篇「本地大語言模型手機」建立硬體前提：手機不必直接取代所有機器人控制器，而可以成為可隨身移動、共享記憶與世界狀態的個人 AI 主腦。

**關鍵詞：** Jetson Orin、Jetson Thor、ARM、x86、Ryzen AI Max+ 395、Qualcomm RB5、Raspberry Pi、外部主腦、邊緣 AI、本地大語言模型

---

# 1. 問題不是「哪一顆晶片最強？」

討論具身 AI 硬體時，最容易被單一性能數字吸引：

- TOPS；
- TFLOPS；
- NPU；
- GPU 核心數；
- 模型 tokens/s。

但一台真正長時間工作的迷你機器人，約束更接近：

$$
\mathcal H
=
f(
P,
T,
M,
B,
I,
L,
C,
S
),
$$

其中：

- $P$ ：功耗；
- $T$ ：散熱；
- $M$ ：可用記憶體；
- $B$ ：記憶體頻寬；
- $I$ ：感測器與馬達 I/O；
- $L$ ：延遲；
- $C$ ：成本；
- $S$ ：軟體生態。

因此：

$$
\boxed{
\text{Best AI Chip}
\neq
\text{Best Robot Architecture}.
}
$$

如果某個平台能跑更大的模型，但：

- 需要 100 W；
- 要巨大風扇；
- 啟動慢；
- 沒有即時 I/O；
- 沒有可靠 MCU；
- 機器人一斷 Wi-Fi 就完全失能；

那它未必適合迷你具身系統。

---

# 2. 先把「腦」拆成五種不同工作

一台二白式迷你機器人其實不需要只有一個腦。

它至少可以分成：

$$
H=
\{
H_0,H_1,H_2,H_3,H_4
\}.
$$

其中：

### $H_0$ ：Real-Time Controller

負責：

- 馬達；
- 編碼器；
- PWM；
- 舵機；
- 急停；
- 電池；
- 碰撞；
- watchdog。

典型平台：

- STM32；
- ESP32；
- RP2040；
- 其他 MCU／RTOS。

這一層通常不跑 LLM。

---

### $H_1$ ：Always-on Perception

負責：

- wake word；
- VAD；
- IMU；
- 簡單聲源定位；
- 低功耗感知；
- 簡單事件分類。

它可能是 MCU、DSP、NPU 或手機式低功耗 SoC 的一部分。

---

### $H_2$ ：Local AI Compute

負責：

- ASR；
- TTS；
- 人臉；
- 物體辨識；
- VLM；
- 世界狀態 Runtime；
- 行為樹；
- 本地 LLM；
- ROS 2。

這才是通常被稱為「機器人大腦」的部分。

---

### $H_3$ ：External Personal Brain

例如：

- Mac mini；
- Ryzen AI 小型工作站；
- 家中 AI NAS；
- AI PC；
- 未來本地 AI 手機。

與機器人透過：

$$
\text{Wi-Fi / Ethernet / 5G}
$$

連接。

負責：

- 大模型；
- 長期記憶；
- 多機器人共享狀態；
- 深度規劃；
- 本地資料庫；
- 大型 VLM。

---

### $H_4$ ：Cloud Frontier

最後才是：

- 雲端前沿模型；
- 網路搜尋；
- 大型推理；
- 超大 context；
- 遠端服務。

所以：

$$
\boxed{
\text{Robot Intelligence}
\neq
\text{One Processor}.
}
$$

它其實是一個計算拓撲。

---

# 3. 為什麼 MCU 永遠不應被大型模型淘汰？

假設機器人以：

$$
1\text{ kHz}
$$

更新馬達控制。

則控制週期只有：

$$
1\text{ ms}.
$$

任何需要：

- token generation；
- Python runtime；
- 網路 round trip；
- CUDA kernel 啟動；
- 記憶檢索；

的系統，都不應成為這條控制迴圈的必要依賴。

因此：

$$
\boxed{
\tau_{\mathrm{motor}}
\ll
\tau_{\mathrm{LLM}}.
}
$$

合理架構是：

```text
LLM：
「向主人靠近」

    ↓

Navigation / Motion Planner：
target_velocity = ...

    ↓

MCU：
PID / motor loop
```

模型發的是：

$$
\text{intent / goal},
$$

不是：

$$
\text{PWM every millisecond}.
$$

這不只是安全問題，也是時間尺度問題。

---

# 4. Jetson Orin：2026 年仍然很合理的機器人主控

NVIDIA Jetson Orin 系列的優勢不是單純 TOPS。

它真正的價值是：

$$
\text{CUDA}
+
\text{TensorRT}
+
\text{JetPack}
+
\text{ROS / Isaac ecosystem}
+
\text{camera / I/O}.
$$

官方目前的 Orin 系列涵蓋：

- Orin Nano；
- Orin NX；
- AGX Orin。

公開規格從 Orin Nano 4GB 約 34 TOPS，一直到 AGX Orin 最高約 275 TOPS。

而且 CPU 本身就是 ARM Cortex-A78AE 系列。

所以 Jetson Orin 本質上是一個：

$$
\boxed{
\text{ARM CPU}
+
\text{NVIDIA GPU}
+
\text{robotics I/O}
}
$$

的嵌入式平台。

這正適合：

- 多攝影機；
- CUDA 視覺；
- TensorRT；
- ROS 2；
- 本地 VLM；
- 小型生成式模型。

---

# 5. Orin Nano、Orin NX、AGX Orin 怎麼選？

如果以迷你具身 AI 為目的，可以粗略分成：

## Orin Nano

適合：

- 基礎視覺；
- ASR；
- 小型模型；
- ROS；
- 原型陪伴機器人。

優勢：

- 小；
- 相對低功耗；
- 生態成熟。

限制：

$$
M_{\mathrm{RAM}}
$$

通常比真正本地大模型主機小很多。

因此它更適合：

$$
\text{Perception Brain}
$$

而不是：

$$
\text{All-in-one 30B LLM Brain}.
$$

---

## Orin NX

可以視為很有吸引力的中間點。

它有較強 AI 推理能力，同時仍是相對緊湊的模組。

如果迷你機器人需要：

- 多模型並行；
- VLM；
- 較大的本地 LLM；
- 多攝影機；

Orin NX 往往比 Nano 更有餘裕。

---

## AGX Orin

適合：

- 大型移動機器人；
- 多感測器；
- 研究平台；
- 人形機器人；
- 高階自主設備。

但對一個桌面／家用迷你角色機器人而言：

$$
\text{size}
+
\text{power}
+
\text{cooling}
$$

可能已經過度。

---

# 6. Jetson Thor：強大，但不是二白尺寸的答案

Jetson Thor 已經進入完全不同的等級。

2026 年 NVIDIA 公開規格顯示，Jetson AGX Thor Developer Kit 提供：

- 128 GB LPDDR5X；
- 約 273 GB/s 記憶體頻寬；
- Blackwell GPU；
- 最高 2070 FP4 TFLOPS；
- 40–130 W 功耗。

這個方向非常有趣，因為：

$$
128\text{ GB}
$$

意味著它開始接近「真正大型本地具身模型」的容量需求。

但：

$$
40\sim130\text{ W}
$$

已經告訴我們：

> 它是 physical AI 工作站級核心，不是小型玩具機器人的普通主控。

Thor 更適合：

- 人形機器人；
- 自動駕駛研究；
- 大型 AMR；
- 多模態物理 AI；
- 局域網邊緣伺服器。

因此在迷你系統中，它更可能扮演：

$$
H_3
$$

而不是：

$$
H_1.
$$

---

# 7. Qualcomm RB5：另一條 ARM 異質運算路線

Jetson 不是唯一的 ARM 機器人方案。

Qualcomm Robotics RB5 類平台代表了更接近手機 SoC 的哲學：

$$
\text{CPU}
+
\text{GPU}
+
\text{DSP}
+
\text{ISP}
+
\text{AI Engine}.
$$

官方 RB5 平台使用 QRB5165／Kryo 585，AI Engine 公開標示最高約 15 TOPS，並針對：

- 多攝影機；
- ISP；
- 電腦視覺；
- Wi-Fi；
- 5G；
- ROS 2；

提供整合。

這種架構的優勢不是比 Jetson 更強，而是：

$$
\boxed{
\text{Mobile-class heterogeneous efficiency}.
}
$$

對小型移動機器人來說：

- 功耗；
- 影像 ISP；
- 無線通訊；
- 尺寸；

可能比超大 GPU 更重要。

也就是說：

> 未來本地 AI 手機與迷你機器人的硬體演化，其實很可能逐漸靠近同一類 SoC 設計。

---

# 8. Raspberry Pi 也開始跨入小型生成式 AI

2026 年一個很有代表性的變化，是 Raspberry Pi 的 AI HAT+ 2。

官方資料顯示，它使用 Hailo-10H：

- 40 TOPS INT4；
- 自帶 8 GB 記憶體；
- 可在 Raspberry Pi 5 上運行本地 LLM／VLM；
- 官方描述約支援至 6B 級模型。

這不代表 Raspberry Pi 5 突然變成大型 AI 工作站。

真正重要的是：

$$
\boxed{
\text{Low-cost SBC}
+
\text{dedicated AI memory}
}
$$

已經可以開始處理生成式 AI。

這非常值得注意。

因為早期迷你機器人通常是：

$$
\text{SBC}
+
\text{Cloud AI}.
$$

現在正在變成：

$$
\text{SBC}
+
\text{Local Small Generative AI}
+
\text{Cloud Escalation}.
$$

這正好吻合第 5 篇提出的按需智能。

---

# 9. ARM 的真正優勢：不是「AI 比 x86 強」

討論 ARM 與 x86 時，最容易落入錯誤比較：

> ARM 比較省電，所以一定適合 AI。

實際上沒有這麼簡單。

指令集本身不是主要決定因素。

真正差異更接近：

$$
\text{platform integration}.
$$

手機／嵌入式 ARM SoC 常把：

- ISP；
- DSP；
- NPU；
- media engine；
- security enclave；
- low-power cores；

高度整合。

因此對：

- always-on camera；
- wake word；
- tracking；
- multi-sensor；

非常有優勢。

這是一種：

$$
\text{heterogeneous efficiency}
$$

而不是「ARM 指令天然比較會跑 LLM」。

---

# 10. x86 的優勢：軟體、記憶體與大型本地模型

如果機器人不要求所有東西都塞在身體裡，x86 的角色會完全不同。

例如：

- mini PC；
- AI workstation；
- NAS；
- home server。

此時：

$$
\text{power budget}
$$

從：

$$
5\sim20\text{ W}
$$

變成：

$$
50\sim150\text{ W}.
$$

限制放鬆後，就可以換取：

- 大記憶體；
- 強 GPU；
- 通用軟體；
- 大模型。

所以：

$$
\boxed{
\text{x86 external brain}
}
$$

是非常合理的具身 AI 組件。

---

# 11. Ryzen AI Max+ 395：重要的不是它是 x86，而是它的記憶體形態

AMD Ryzen AI Max+ 395 是這條線很有意思的參考。

AMD 的 AI Halo 開發平台公開配置包括：

- 16 核 Zen 5 CPU；
- Radeon 8060S；
- 40 CU RDNA 3.5；
- XDNA 2 NPU；
- 128 GB LPDDR5x；
- 8000 MT/s；
- 256 GB/s 記憶體頻寬。

整機開發平台 TDP 為 120 W。

這顯然不是要塞進迷你二白。

但它展示了：

$$
\boxed{
\text{large shared memory}
+
\text{large integrated GPU}
}
$$

這種對本地模型非常有利的方向。

大型語言模型最常見的限制之一不是：

$$
\text{TOPS 不夠},
$$

而是：

$$
\text{模型放不進記憶體}.
$$

假設權重採 4-bit：

$$
M_{\mathrm{weights}}
\approx0.5P\text{ GB},
$$

其中 $P$ 是十億參數數。

一個 70B 模型光權重就約：

$$
35\text{ GB},
$$

更不用說：

- KV cache；
- runtime；
- vision encoder；
- 系統記憶體。

因此：

$$
128\text{ GB}
$$

比「NPU 多幾十 TOPS」更可能決定你到底能不能本地跑某些大型模型。

---

# 12. TOPS 不能直接跨平台比較

這裡必須特別警告。

例如：

- 40 TOPS INT4；
- 67 TOPS INT8；
- 2070 TFLOPS FP4 sparse；
- NPU 50 TOPS；

不能直接拿數字大小排序真實 LLM 性能。

因為它們可能使用不同：

- precision；
- sparsity assumption；
- operation definition；
- memory system；
- software kernel；
- model architecture。

因此：

$$
\boxed{
\text{Peak TOPS}
\neq
\text{LLM tokens/s}.
}
$$

更重要的是：

$$
\text{usable throughput}
=
f(
\text{compute},
\text{bandwidth},
\text{memory},
\text{kernel},
\text{quantization},
\text{context}
).
$$

所以硬體選型必須看實際模型 workload，而不是只看宣傳數字。

---

# 13. Mac mini：非常合理的「安靜外部主腦」

Mac mini 不是機器人嵌入式平台。

它沒有 Jetson 那種典型：

- GPIO；
- CAN；
- carrier board；
- robotics SDK。

但如果角色改成：

$$
H_3=\text{External Personal Brain},
$$

情況就不同。

2024 M4 Pro Mac mini 官方規格最高可以配置：

- 64 GB 統一記憶體；
- 273 GB/s 記憶體頻寬。

它很適合作為：

- 本地 LLM；
- 長期記憶；
- 語音服務；
- 家中 AI server；
- 多機器人共享推理主機。

機器人則透過局域網呼叫：

```text
robot.local
    ↔
mac-mini.home
```

這在研究原型階段尤其方便。

---

# 14. 外部主腦不是「雲端」

這一點非常重要。

可以區分：

$$
\text{On-body}
$$

$$
\text{Local External}
$$

$$
\text{Remote Cloud}.
$$

它們不是同一件事。

外部本地主腦可以放在：

- 家中；
- 車內；
- 背包；
- 手機；
- 辦公室。

因此仍可維持：

- 低延遲；
- 私人網路；
- 本地資料；
- 高頻寬；
- 無 Internet 運作。

所以：

$$
\boxed{
\text{Local AI}
\neq
\text{All AI must physically fit inside the robot}.
}
$$

「本地」可以指：

$$
\text{user-controlled local compute domain}.
$$

---

# 15. 這會產生一個很實際的迷你機器人分層

例如二白式機器人可以配置：

### 本體

```text
STM32
+ microphones
+ camera
+ wheel controller
+ battery
+ low-power ARM SBC
```

本體負責：

$$
\text{survival}
+
\text{reflex}
+
\text{state continuity}.
$$

### 本地 AI SoC

可能是：

- Jetson Orin Nano/NX；
- Qualcomm 類平台；
- Raspberry Pi + accelerator；
- 其他 ARM NPU SoC。

負責：

$$
\text{vision}
+
\text{ASR}
+
\text{small LLM}
+
\text{router}.
$$

### 外部主腦

可能是：

- Ryzen AI；
- Mac mini；
- GPU PC；
- NAS。

負責：

$$
\text{large LLM}
+
\text{VLM}
+
\text{memory}
+
\text{deep planning}.
$$

### 雲端

只有最後才：

$$
\text{frontier escalation}.
$$

---

# 16. 斷線時應該發生什麼？

這是一個判斷架構好壞的簡單測試。

如果外部主腦斷線：

$$
H_3=0,
$$

機器人不應變成磚頭。

而應降級為：

$$
H_0+H_1+H_2.
$$

仍然可以：

- 停止；
- 避障；
- 回充；
- 辨識主人；
- 執行既有技能；
- 簡單說話；
- 保留世界狀態。

如果本地 AI SoC 也失效：

$$
H_2=0,
$$

至少：

$$
H_0
$$

仍能：

- 停馬達；
- 保護電池；
- 進入 fault；
- 等待維修。

因此：

$$
\boxed{
\text{Graceful Degradation}
}
$$

應該從硬體層就設計，而不是事後補救。

---

# 17. 世界狀態到底存在哪裡？

當系統變成多計算節點時，一個自然問題出現：

> $S_t$ 到底在哪裡？

最差的答案是：

> 只存在大模型 context 裡。

更合理的是分層：

$$
S_t=
S_t^{\mathrm{critical}}
\cup
S_t^{\mathrm{local}}
\cup
S_t^{\mathrm{extended}}.
$$

例如：

### Critical State

放在機器人本體：

- 電量；
- fault；
- 當前安全模式；
- 裝置 ID；
- 最後任務 checkpoint。

### Local Operational State

放在主控 SBC：

- 人物；
- 房間；
- 當前對話；
- BT；
- local map。

### Extended State

放在個人外部主腦：

- 長期記憶；
- 完整事件歷史；
- 大型向量庫；
- 跨設備世界模型。

如此：

$$
\text{network loss}
$$

不等於：

$$
\text{identity/state loss}.
$$

---

# 18. 硬體選型真正該問的七個問題

與其問：

> 哪顆晶片最強？

更合理的是問：

1. 最長可以接受多少瓦？
2. 機器人內可容納多大散熱？
3. 斷網後必須保留哪些能力？
4. 要同時跑哪些模型？
5. 最大本地模型需要多少記憶體？
6. 是否需要 ROS、CUDA、特定驅動？
7. 哪些資料可以送到外部主腦／雲端？

這七個答案確定後，硬體選型才有意義。

---

# 19. 迷你機器人硬體不是越集中越高級

很多人會直覺認為：

$$
\text{Everything On-device}
>
\text{Distributed System}.
$$

但對具身 AI，未必如此。

把所有東西塞入本體會增加：

- 熱；
- 電池；
- 重量；
- 成本；
- 噪音；
- 維修難度。

反過來：

$$
\text{Small Body}
+
\text{Local External Brain}
$$

可能是一個更好的產品。

尤其對：

- 家庭陪伴；
- 桌面角色；
- 移動寵物機器人；

它們並不會離家數百公里。

只要家中存在：

$$
\text{Personal AI Hub},
$$

機器人本體完全可以非常小。

---

# 20. 這其實正在指向「手機就是主腦」

如果外部主腦需要：

- 隨身；
- 低功耗；
- 有電池；
- 有 5G/Wi-Fi；
- 有麥克風；
- 有攝影機；
- 有 NPU；
- 有安全晶片；
- 有大量個人資料；

那最自然的既有硬體就是：

$$
\boxed{
\text{Smartphone}.
}
$$

目前手機最大的限制是：

- 可用記憶體；
- 散熱；
- 模型開放程度；
- OS 權限；
- 背景 Runtime；
- 長時間推理。

但它已經具備外部 AI 主腦需要的幾乎所有「非模型」條件。

因此下一階段非常自然：

$$
\text{External Brain}
\rightarrow
\text{Portable External Brain}
\rightarrow
\text{AI-native Phone}.
$$

---

# 21. 一個 2026 年可實作的原型配置

如果今天做一台「二白類」MVP，可以非常務實：

### Robot Body

- MCU；
- 輪式底盤；
- IMU；
- camera；
- microphone array；
- speaker；
- proximity sensor。

### Edge Computer

- Jetson Orin Nano/NX，或
- Raspberry Pi 5 + AI accelerator，或
- 其他 ARM NPU SBC。

### Runtime

- ROS 2；
- world-state service；
- FSM／BT；
- local ASR/TTS；
- small vision model；
- small LLM／router。

### External Brain

- Ryzen AI Max+ 395 類主機；
- Mac mini；
- GPU workstation。

### Cloud

- only when needed。

整體：

$$
\boxed{
\text{MCU}
+
\text{Edge AI}
+
\text{World State}
+
\text{External LLM}
}
$$

今天就能做。

真正困難的已經不再是：

> 這些零件存不存在？

而是：

> Runtime 是否設計得足夠穩定，讓這些零件像同一個持續存在的智能系統？

---

# 22. 結論：機器人的「腦」應該是一個拓撲，而不是一塊板子

從第一篇一路到現在，我們可以重新定義「機器人大腦」。

傳統想像：

$$
\text{Brain}
=
\text{Central Processor}.
$$

但更適合本地具身 AI 的定義可能是：

$$
\boxed{
\text{Brain}
=
\text{Persistent State}
+
\text{Distributed Compute Topology}
+
\text{Routing Policy}.
}
$$

因此：

- MCU 可以是反射腦；
- Jetson 是感知腦；
- 本地 LLM 是互動腦；
- 家中工作站是深度思考腦；
- 雲端是偶爾使用的外部超級腦。

關鍵不是哪一顆晶片「代表 AI」。

而是所有計算節點是否共享：

$$
S_t,
$$

並由同一套：

$$
\text{Event}
+
\text{Priority}
+
\text{Router}
$$

共同協調。

到這一步，迷你具身機器人與下一個主題已經只差一步：

> 如果真正重要的是一個可以隨身攜帶、擁有大量私人狀態、連接所有身體的外部主腦，那它最終會不會就是下一代手機？

這正是第 7 篇：

**《本地大語言模型手機：從 AI 功能手機到個人 AI Runtime》**

---

# 參考資料

1. NVIDIA. *Jetson Orin — Next-level AI performance for next-gen robotics and edge solutions*.  
   https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/

2. NVIDIA. *Jetson Developer Kits / Jetson AGX Thor*.  
   https://developer.nvidia.com/embedded/jetson-developer-kits

3. NVIDIA. *Jetson Thor — Advanced AI for Physical Robotics*.  
   https://www.nvidia.com/en-gb/autonomous-machines/embedded-systems/jetson-thor/

4. Qualcomm. *Qualcomm Robotics RB5 Platform*.  
   https://www.qualcomm.com/news/releases/2020/06/qualcomm-launches-worlds-first-5g-and-ai-enabled-robotics-platform

5. Qualcomm. *Flight RB5 5G Platform Hardware / QRB5165N SOM*.  
   https://www.qualcomm.com/internet-of-things/products/flight-rb5-platform/hardware

6. Raspberry Pi. *AI HATs Documentation*.  
   https://www.raspberrypi.com/documentation/accessories/ai-hat-plus.html

7. Raspberry Pi. *AI HAT+ 2*.  
   https://www.raspberrypi.com/products/ai-hat-plus-2/

8. AMD. *Ryzen AI Halo Developer Platform with Ryzen AI Max+ 395*.  
   https://www.amd.com/zh-cn/products/processors/desktops/ryzen/ryzen-ai-halo/ryzen-ai-max-plus-395.html

9. Apple. *Mac mini (2024) Technical Specifications*.  
   https://support.apple.com/zh-tw/121555
