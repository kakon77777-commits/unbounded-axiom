# 計算不是只有 FLOPs：記憶體、互連、硬體占用與計算時空體積

## Computation Is More Than FLOPs: Memory, Interconnect, Hardware Occupancy, and Computational Spacetime Volume

**系列：**《智能的物理計量：從最小語意執行到成果品質與計算時空》  
**英文系列：** *Physical Metrology of Intelligence: From Minimal Semantic Execution to Quality and Computational Spacetime*  
**系列編號：** EML-IPM  
**篇次：** Paper 05 / 10  
**文件編號：** EML-IPM-05  
**作者：** Neo.K with Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-02  
**文件性質：** 公開純理論論文／智能計量方法論  
**工程狀態：** 無 MVP；本文建立計算物理成本的多軸與時空表示，不宣稱存在單一跨硬體「完美成本常數」

---

## 摘要

現代 AI 計算經常以 FLOPs、tokens/s、GPU-hours 或 Joules 描述成本。然而，這些量各自只投影了整個物理計算過程的一部分。

兩個系統即使具有：

$$
\boxed{
FLOPs_A=FLOPs_B
}
$$

也可能具有：

$$
\boxed{
MemoryTraffic_A\neq MemoryTraffic_B,
}
$$

$$
\boxed{
Interconnect_A\neq Interconnect_B,
}
$$

$$
\boxed{
Latency_A\neq Latency_B,
}
$$

$$
\boxed{
HardwareOccupancy_A\neq HardwareOccupancy_B,
}
$$

甚至：

$$
\boxed{
Energy_A\neq Energy_B.
}
$$

因此：

$$
\boxed{
\text{FLOPs}
\neq
\text{Physical Computational Cost}.
}
$$

本文提出 **Physical Computation Cost Vector**：

$$
\boxed{
\mathbf C_P
=
(
O,
B_M,
B_I,
B_N,
M_R,
D,
T,
E
)
}
$$

其中：

- $O$：Arithmetic / Logical Operations；
- $B_M$：Memory Traffic，跨記憶體層級搬移的 bytes；
- $B_I$：I/O / Storage Traffic；
- $B_N$：Interconnect / Network Traffic；
- $M_R$：Memory Residency，任務占用記憶體容量與時間的組合；
- $D$：Device Occupancy，實體加速器／處理器占用；
- $T$：Wall-Clock Time；
- $E$：Energy。

本文並引入 **Arithmetic Intensity**：

$$
\boxed{
I_A
=
\frac{O}{B_M}
}
$$

以及經典 Roofline 型性能限制：

$$
\boxed{
P_{\mathrm{attainable}}
\le
\min
\left(
P_{\mathrm{peak}},
BW_{\mathrm{mem}}\cdot I_A
\right).
}
$$

這揭示一個重要事實：一個 workload 即使 FLOPs 不變，也可能因資料重用差、memory bandwidth 不足或 communication overhead 而大幅增加執行時間與能源。

本文進一步提出 **Computational Spacetime（計算時空）**。其出發點不是把所有物理成本硬壓成單一 scalar，而是先定義任務期間的資源占用場：

$$
\boxed{
\mathbf R(t)
=
(
r_C(t),
r_M(t),
r_N(t),
r_S(t)
)
}
$$

其中：

- $r_C(t)$：compute-device occupancy；
- $r_M(t)$：memory occupancy；
- $r_N(t)$：interconnect/network occupancy；
- $r_S(t)$：storage/I/O occupancy。

則 **Raw Computational Spacetime Measure** 為：

$$
\boxed{
\mathbf V_{CST}
=
\int_{t_0}^{t_f}
\mathbf R(t)\,dt
}
$$

因此：

$$
\boxed{
\mathbf V_{CST}
=
(
V_C,
V_M,
V_N,
V_S
)
}
$$

其中：

$$
V_C
=
\int r_C(t)\,dt
$$

可用 device·seconds 或 normalized accelerator-seconds 表示；

$$
V_M
=
\int r_M(t)\,dt
$$

可用 byte·seconds 表示；

$$
V_N
=
\int r_N(t)\,dt
$$

可表示為 interconnect-resource·seconds，而實際傳輸量則另外由 $B_N$ 保存；

$$
V_S
=
\int r_S(t)\,dt.
$$

本文特別主張：

$$
\boxed{
V_C+V_M+V_N+V_S
}
$$

**在未指定正規化、權重與量綱轉換前沒有合法的物理意義。**

因此 Computational Spacetime 首先應是一個：

$$
\boxed{
\text{vector / measure},
}
$$

而不是任意相加的單一數字。

若研究需要 scalar comparison，必須先指定 reference capacities：

$$
C_{ref},
M_{ref},
N_{ref},
S_{ref}
$$

以及權重：

$$
w_C,w_M,w_N,w_S,
$$

再定義 normalized scalar：

$$
\boxed{
V_{CST}^{*}
=
\int_{t_0}^{t_f}
\left[
w_C\frac{r_C(t)}{C_{ref}}
+
w_M\frac{r_M(t)}{M_{ref}}
+
w_N\frac{r_N(t)}{N_{ref}}
+
w_S\frac{r_S(t)}{S_{ref}}
\right]dt.
}
$$

因此：

$$
\boxed{
V_{CST}^{*}
=
V_{CST}^{*}
(
Reference,
Weights,
Boundary
).
}
$$

沒有 reference scheme 的 scalar CST 不應被宣稱為普適物理量。

本文再指出，即使兩個系統具有相同 integrated device-time：

$$
8\ GPU\times10s
=
1\ GPU\times80s
=
80\ GPU\cdot s,
$$

它們也不是等價執行。

因為：

$$
\boxed{
V_C
\text{ equal}
\not\Rightarrow
T_{\mathrm{wall}}
\text{ equal}.
}
$$

更不代表：

$$
\boxed{
\text{same critical path, same energy, same memory pressure, same communication topology}.
}
$$

因此本文進一步引入 **Computational Spacetime Topology**：

$$
\boxed{
\Theta_{CST}
=
(
T_{\mathrm{wall}},
T_{\mathrm{serial}},
P_{\mathrm{parallel}},
D_{\mathrm{peak}},
M_{\mathrm{peak}},
B_{\mathrm{peak}},
\Gamma_{\mathrm{comm}}
)
}
$$

其中：

- $T_{\mathrm{wall}}$：實際完成時間；
- $T_{\mathrm{serial}}$：不可平行化的 critical-path / serial component；
- $P_{\mathrm{parallel}}$：有效平行程度；
- $D_{\mathrm{peak}}$：峰值 device count；
- $M_{\mathrm{peak}}$：峰值記憶體占用；
- $B_{\mathrm{peak}}$：峰值 bandwidth demand；
- $\Gamma_{\mathrm{comm}}$：communication topology / synchronization burden。

所以：

$$
\boxed{
\text{same spacetime volume}
\neq
\text{same spacetime topology}.
}
$$

本文將 Paper 04 的能源向量：

$$
\mathcal E
=
(
E_{\mathrm{gross}},
E_{\mathrm{base}},
E_{\mathrm{marg}},
E_{\mathrm{attrib}},
E_{\mathrm{thermo,min}}
)
$$

與本篇的 $\mathbf C_P,\mathbf V_{CST},\Theta_{CST}$ 統合，提出：

$$
\boxed{
\mathfrak P_{\mathrm{compute}}
=
(
\mathbf C_P,
\mathbf V_{CST},
\Theta_{CST},
\mathcal E,
Boundary_P
).
}
$$

這才是一次智能成果的完整物理成本描述。

本文終端命題是：

$$
\boxed{
\textbf{
計算不是「做了多少乘法」，
而是某組物理資源在某段時間內，
以某種拓撲搬移、保存、同步與轉換狀態。
FLOPs 只是這個計算時空中的一條投影。
}
}
$$

---

# 1. FLOPs 為什麼如此流行？

因為它容易：

- 定義；
- 估算；
- 比較；
- 與理論峰值對接。

若 workload 有：

$$
N_{\mathrm{mul}},
N_{\mathrm{add}}
$$

可粗略估：

$$
O
=
N_{\mathrm{mul}}+N_{\mathrm{add}}+\cdots.
$$

---

# 2. FLOPs 很重要，但它只看 arithmetic work

它沒有直接描述：

- data 在哪裡；
- data 搬了多少次；
- 等待多久；
- 跨幾顆 device；
- 是否 synchronization；
- 是否 memory-bound。

所以：

$$
\boxed{
FLOPs
=
\text{one projection of computation}.
}
$$

---

# 3. Roofline model 的核心啟示

Williams、Waterman 與 Patterson 的 Roofline model 將可達 performance 約束在：

$$
\boxed{
P
\le
\min
(
P_{\mathrm{peak}},
BW\cdot I_A
).
}
$$

其中：

$$
\boxed{
I_A=
\frac{\text{operations}}{\text{bytes transferred}}.
}
$$

---

# 4. Arithmetic intensity 很低時

即使有極高：

$$
P_{\mathrm{peak}},
$$

系統也可能吃不到。

因為：

$$
\boxed{
P
\approx
BW\cdot I_A.
}
$$

---

# 5. 所以「加更多算力」不一定有效

如果 bottleneck 是：

$$
\boxed{
\text{data movement}.
}
$$

增加 ALU / tensor cores 可能幾乎沒有改善。

---

# 6. Memory Wall

處理器 arithmetic throughput 的成長，長期快於某些記憶體延遲與頻寬改善。

這形成：

$$
\boxed{
\text{Compute Capability}
\gg
\text{Data Supply Capability}
}
$$

的結構性壓力。

---

# 7. AI 尤其依賴 memory hierarchy

典型層級包括：

$$
\boxed{
Registers
\rightarrow
OnChipCache/SRAM
\rightarrow
HBM/DRAM
\rightarrow
HostMemory
\rightarrow
Storage.
}
$$

---

# 8. 同一資料被放在哪一層很重要

因為：

- latency 不同；
- bandwidth 不同；
- energy per access 不同；
- capacity 不同。

因此：

$$
\boxed{
1\ Byte\ Access
\neq
1\ FixedCost.
}
$$

---

# 9. Data movement 可能比 arithmetic 更昂貴

DNN accelerator literature 長期強調，資料搬移是能源與性能設計的主要成本來源之一。

因此：

$$
\boxed{
ComputeOptimization
\neq
ArithmeticOptimizationOnly.
}
$$

---

# 10. Memory Traffic

本文定義：

$$
\boxed{
B_M
=
\sum_{\ell}
B_{\ell}
}
$$

其中 $\ell$ 可代表：

- register；
- cache；
- SRAM；
- HBM/DRAM；
- host memory。

---

# 11. 但直接相加仍有資訊損失

因為：

$$
1GB_{\mathrm{SRAM}}
$$

和：

$$
1GB_{\mathrm{DRAM}}
$$

不是相同物理成本。

---

# 12. 所以更完整是階層向量

$$
\boxed{
\mathbf B_M
=
(
B_{reg},
B_{cache},
B_{sram},
B_{hbm},
B_{host}
).
}
$$

---

# 13. Memory Energy 可以寫成

$$
\boxed{
E_M
=
\sum_{\ell}
\epsilon_{\ell}B_{\ell},
}
$$

其中：

$$
\epsilon_\ell
$$

是該平台下每 byte movement 的有效能源係數。

---

# 14. $\epsilon_\ell$ 不是普適常數

它依賴：

- process node；
- memory technology；
- utilization；
- access pattern；
- voltage；
- controller。

所以：

$$
\boxed{
MemoryCost
=
MemoryCost(Hardware,Pattern).
}
$$

---

# 15. Memory Residency 與 Memory Traffic 不一樣

模型權重常駐：

$$
M=100GB
$$

一分鐘，

和只搬移：

$$
100GB
$$

一次，

不是同一成本。

---

# 16. 因此定義 Memory Residency

$$
\boxed{
V_M
=
\int_{t_0}^{t_f}
M_{\mathrm{resident}}(t)\,dt.
}
$$

單位可為：

$$
\boxed{
Byte\cdot second.
}
$$

---

# 17. $V_M$ 測「占著多少記憶體多久」

而：

$$
B_M
$$

測「搬了多少資料」。

兩者都需要。

---

# 18. 所以：

$$
\boxed{
MemoryTraffic
\neq
MemoryResidency.
}
$$

---

# 19. KV cache 是很好的例子

長 context inference 中：

- KV cache 會占記憶體；
- 每個 decoding step 又要讀取相關 cache；
- context 越長，memory pressure 越高。

所以只看 output token 數非常不完整。

---

# 20. Context 的物理成本不是只有「多幾個 token」

它改變：

$$
\boxed{
MemoryResidency,
MemoryTraffic,
AttentionWork,
Latency.
}
$$

---

# 21. Interconnect 是下一個成本層

多 GPU / accelerator 系統需要：

- all-reduce；
- all-gather；
- all-to-all；
- point-to-point；
- synchronization。

---

# 22. 定義 Network / Interconnect Traffic

$$
\boxed{
B_N
=
\sum_{links}
Bytes_{\mathrm{transferred}}.
}
$$

---

# 23. 但 bytes 也不是全部

因為 topology 很重要。

同樣：

$$
100GB
$$

在：

- on-package link；
- NVLink-class interconnect；
- PCIe；
- Ethernet / fabric；

有不同：

- latency；
- energy；
- contention。

---

# 24. 所以需要 communication graph

令：

$$
\boxed{
G_C=(V_D,E_L)
}
$$

其中：

- $V_D$：devices；
- $E_L$：links。

---

# 25. 每條 edge 可以具有

$$
\boxed{
e_{ij}
=
(
B_{ij},
L_{ij},
BW_{ij},
E_{ij}
).
}
$$

---

# 26. Communication Cost 不是只看總流量

還要看：

$$
\boxed{
Topology
+
Synchronization
+
Contention.
}
$$

---

# 27. Collective operations 很重要

例如 all-reduce：

即使每 device arithmetic 很快，

也可能：

$$
T_{\mathrm{comm}}
\gg
T_{\mathrm{compute}}.
$$

---

# 28. 所以：

$$
\boxed{
MoreDevices
\not\Rightarrow
LowerLatency.
}
$$

---

# 29. Parallelism 不是免費

假設任務可以拆成：

$$
n
$$

份。

理想：

$$
T_n
=
\frac{T_1}{n}.
$$

---

# 30. 但實際：

$$
\boxed{
T_n
=
T_{\mathrm{serial}}
+
T_{\mathrm{parallel}}(n)
+
T_{\mathrm{comm}}(n)
+
T_{\mathrm{sync}}(n).
}
$$

---

# 31. Amdahl-like pressure

只要存在不可平行部分：

$$
f_s>0,
$$

加速比就有上界。

---

# 32. 所以 GPU 數不是「算力乘法器」而已

它也增加：

- coordination；
- communication；
- failure surface；
- idle imbalance。

---

# 33. Device Occupancy

定義：

$$
\boxed{
D(t)
=
\text{number/equivalent fraction of occupied devices at }t.
}
$$

---

# 34. Compute Device-Time

$$
\boxed{
V_C
=
\int_{t_0}^{t_f}
D(t)\,dt.
}
$$

---

# 35. 最簡單情況

8 GPU 占滿 10 秒：

$$
\boxed{
V_C=80\ GPU\cdot s.
}
$$

---

# 36. 1 GPU 占滿 80 秒：

$$
\boxed{
V_C=80\ GPU\cdot s.
}
$$

---

# 37. 但兩者 latency 不同

$$
\boxed{
T_A=10s,
\quad
T_B=80s.
}
$$

所以：

$$
\boxed{
V_C
\neq
T.
}
$$

---

# 38. 兩者甚至能源也可不同

多 GPU 系統可能有：

- higher idle overhead；
- interconnect energy；
- different utilization。

所以：

$$
\boxed{
SameDeviceTime
\neq
SameEnergy.
}
$$

---

# 39. 同樣 Device-Time 也不代表相同硬體

80 A100·s 和 80 RTX-class·s 不能直接當相同 resource volume。

---

# 40. 因此需要 hardware equivalence rule

可以用：

- reference device；
- normalized peak throughput；
- measured workload throughput；
- area / transistor / power boundary；

建立等價投影。

---

# 41. 但不同 normalizer 會產生不同答案

所以必須寫：

$$
\boxed{
V_C^{*}
=
V_C^{*}(Reference).
}
$$

---

# 42. 這與 Paper 04 的 Energy Boundary 同構

所有跨硬體比較都需要：

$$
\boxed{
Boundary
+
Reference
+
AttributionRule.
}
$$

---

# 43. Computational Spacetime 的起點

物理計算不是一個點。

它是一段：

$$
[t_0,t_f]
$$

期間內資源被占用的歷史。

---

# 44. 定義資源場

$$
\boxed{
\mathbf R(t)
=
(
r_C(t),
r_M(t),
r_N(t),
r_S(t)
).
}
$$

---

# 45. Compute occupancy

$$
r_C(t).
$$

---

# 46. Memory occupancy

$$
r_M(t).
$$

---

# 47. Network / interconnect occupancy

$$
r_N(t).
$$

---

# 48. Storage / I/O occupancy

$$
r_S(t).
$$

---

# 49. Raw Computational Spacetime Measure

$$
\boxed{
\mathbf V_{CST}
=
\int
\mathbf R(t)\,dt.
}
$$

---

# 50. 展開

$$
\boxed{
\mathbf V_{CST}
=
(
V_C,V_M,V_N,V_S
).
}
$$

---

# 51. 這是向量，不是單位混合的 scalar

其中：

$$
V_C
$$

可能是 device·s；

$$
V_M
$$

可能是 byte·s。

---

# 52. 因此不能寫

$$
80GPU\cdot s
+
500GB\cdot s
=
580.
$$

這沒有物理意義。

---

# 53. Type Safety

$$
\boxed{
V_C
\oplus
V_M
\oplus
V_N
\oplus
V_S
}
$$

只能形成向量。

不能自然相加。

---

# 54. 如果真的需要 scalar

必須先 normalize。

---

# 55. 定義 reference

$$
C_{ref},M_{ref},N_{ref},S_{ref}.
$$

---

# 56. 以及權重

$$
w_C,w_M,w_N,w_S.
$$

---

# 57. 才能定義

$$
\boxed{
V_{CST}^{*}
=
\int
\left[
w_C\frac{r_C(t)}{C_{ref}}
+
w_M\frac{r_M(t)}{M_{ref}}
+
w_N\frac{r_N(t)}{N_{ref}}
+
w_S\frac{r_S(t)}{S_{ref}}
\right]dt.
}
$$

---

# 58. 這個 scalar 不是自然常數

所以：

$$
\boxed{
V_{CST}^{*}
=
V_{CST}^{*}
(
Reference,
Weights,
Boundary
).
}
$$

---

# 59. 使用場景不同，weights 可以不同

例如 edge AI：

$$
w_Energy\uparrow,
w_Memory\uparrow.
$$

---

# 60. 即時控制：

$$
w_Time\uparrow.
$$

---

# 61. data-center batch：

可能更重視：

$$
Throughput/Capacity.
$$

---

# 62. 所以 IPM 應先報 Pareto vector

而不是先報單一總分。

---

# 63. Spacetime Volume 還不夠

因為：

$$
8\times10
=
1\times80.
$$

積分值一樣。

---

# 64. 但形狀不同

因此需要：

$$
\boxed{
\Theta_{CST}
=
\text{Computational Spacetime Topology}.
}
$$

---

# 65. 定義

$$
\boxed{
\Theta_{CST}
=
(
T_{\mathrm{wall}},
T_{\mathrm{serial}},
P_{\mathrm{parallel}},
D_{\mathrm{peak}},
M_{\mathrm{peak}},
B_{\mathrm{peak}},
\Gamma_{\mathrm{comm}}
).
}
$$

---

# 66. $T_{\mathrm{wall}}$

使用者實際等多久。

---

# 67. $T_{\mathrm{serial}}$

critical path 中不能被並行消除的時間。

---

# 68. $P_{\mathrm{parallel}}$

可視為有效 parallelism，例如：

$$
\boxed{
P_{\mathrm{parallel}}
=
\frac{V_C}{T_{\mathrm{wall}}}
}
$$

在簡化同質 device 條件下。

---

# 69. $D_{\mathrm{peak}}$

任務最高同時占用多少 device。

---

# 70. $M_{\mathrm{peak}}$

peak memory footprint。

---

# 71. $B_{\mathrm{peak}}$

peak bandwidth demand。

---

# 72. $\Gamma_{\mathrm{comm}}$

communication graph / synchronization topology。

---

# 73. 所以：

$$
\boxed{
SameVolume
\neq
SameTopology.
}
$$

---

# 74. Computational Shape

可以把一次執行看成：

$$
\boxed{
\mathcal S_{CST}
=
(
\mathbf V_{CST},
\Theta_{CST}
).
}
$$

---

# 75. 這比 GPU-hours 更完整

GPU-hours 只近似：

$$
V_C.
$$

---

# 76. 它看不到：

- memory footprint；
- network traffic；
- latency shape；
- peak resource demand。

---

# 77. Peak demand 對文明尺度很重要

兩個任務總資源一樣：

A：

$$
1000GPU
$$

跑 1 秒。

B：

$$
1GPU
$$

跑 1000 秒。

---

# 78. Integrated compute volume 相近

但 A 需要：

$$
\boxed{
\text{large instantaneous infrastructure}.
}
$$

---

# 79. 所以資源可部署性不同

$$
\boxed{
Deployability_A
\neq
Deployability_B.
}
$$

---

# 80. Peak Hardware Footprint

本文定義：

$$
\boxed{
H_{\mathrm{peak}}
=
(
D_{\mathrm{peak}},
M_{\mathrm{peak}},
N_{\mathrm{peak}},
P_{\mathrm{peak,actual}}
).
}
$$

---

# 81. 它是 capacity barrier

若你沒有 1000 GPU，

即使總 GPU·s 很合理，

也不能執行 A。

---

# 82. 所以：

$$
\boxed{
TotalResource
\neq
RequiredInstantaneousCapacity.
}
$$

---

# 83. 這對 AI benchmark 特別重要

某 benchmark 結果可能使用：

- huge batch；
- enormous parallel rollouts；
- verifier farm。

---

# 84. 使用者只看到一個 answer

但：

$$
\boxed{
H_{\mathrm{peak}}
\gg
\text{ordinary deployment capacity}.
}
$$

---

# 85. 這正好回到 Paper 01

$$
\boxed{
OneUserTurn
\neq
OnePhysicalTurn.
}
$$

---

# 86. FLOPs 還有 precision 問題

一個：

$$
FP64
$$

operation 與：

$$
INT8
$$

operation 的：

- hardware cost；
- energy；
- throughput；

不同。

---

# 87. 所以 operation count 也應 typed

$$
\boxed{
\mathbf O
=
(
O_{FP64},
O_{FP32},
O_{BF16},
O_{FP16},
O_{INT8},
\ldots
).
}
$$

---

# 88. 「一 FLOP」本身也不是完全同質的工程成本

即使數學上都叫 operation。

---

# 89. Sparse computation

若模型有 sparsity / MoE：

nominal FLOPs 和 active FLOPs 又不同。

---

# 90. 所以至少分：

$$
\boxed{
O_{\mathrm{nominal}}
}
$$

與：

$$
\boxed{
O_{\mathrm{executed}}.
}
$$

---

# 91. 再與：

$$
O_{\mathrm{useful}}
$$

區分。

---

# 92. Useful Operations 不能單靠硬體知道

它需要回到：

$$
\mu_I^{eff}.
$$

---

# 93. 因此三層：

$$
\boxed{
O_{\mathrm{executed}}
\rightarrow
N_{\mu}^{gross}
\rightarrow
N_{\mu}^{eff}.
}
$$

---

# 94. 物理 activity 不等於語意 activity

再次得到：

$$
\boxed{
PhysicalActivity
\neq
SemanticActivity.
}
$$

---

# 95. Utilization

硬體宣稱：

$$
P_{\mathrm{peak}}.
$$

實際 workload：

$$
P_{\mathrm{actual}}.
$$

---

# 96. 定義 compute utilization

$$
\boxed{
u_C
=
\frac{P_{\mathrm{actual}}}{P_{\mathrm{peak}}}.
}
$$

---

# 97. 但 utilization 也不能單獨判斷好壞

低 utilization 可能是 memory-bound。

---

# 98. 也可能是 latency-optimized small batch

所以：

$$
\boxed{
LowUtilization
\neq
BadSystem.
}
$$

---

# 99. Memory utilization

也可以定義：

$$
u_M
=
\frac{BW_{\mathrm{actual}}}{BW_{\mathrm{peak}}}.
$$

---

# 100. Roofline state

可以用：

$$
\boxed{
\mathcal R_f
=
(
I_A,
u_C,
u_M
)
}
$$

描述 workload 在 compute-bound / memory-bound 區域的位置。

---

# 101. Communication intensity

仿照 arithmetic intensity，可定義：

$$
\boxed{
I_C
=
\frac{O}{B_N}.
}
$$

---

# 102. 或 semantic communication intensity

$$
\boxed{
I_{\mu,N}
=
\frac{N_{\mu}^{eff}}{B_N}.
}
$$

---

# 103. 這能問

> 每搬 1 GB 跨 device 資訊，換來多少有效語意工作？

---

# 104. 但仍需 task semantics

所以它不是硬體 universal metric。

---

# 105. Memory Semantic Density

同樣可以定義：

$$
\boxed{
D_{\mu,M}
=
\frac{N_{\mu}^{eff}}{V_M}.
}
$$

---

# 106. 它表示：

> 每單位 memory spacetime 支撐多少有效語意工作。

---

# 107. Compute Semantic Density

$$
\boxed{
D_{\mu,C}
=
\frac{N_{\mu}^{eff}}{V_C}.
}
$$

---

# 108. 最終 Quality Density

$$
\boxed{
D_{Q,CST}
=
\frac{Q}{V_{CST}^{*}}
}
$$

只在 scalar normalization 已明示時使用。

---

# 109. 更安全的是向量式效率

$$
\boxed{
\boldsymbol{\eta}_{Q/CST}
=
\left(
\frac{Q}{V_C},
\frac{Q}{V_M},
\frac{Q}{V_N},
\frac{Q}{V_S}
\right).
}
$$

---

# 110. 這保留量綱

也避免任意 weights。

---

# 111. Computational Spacetime Boundary

與 energy boundary 一樣，

必須指定：

$$
\boxed{
Boundary_{CST}.
}
$$

---

# 112. accelerator-only

只看 GPU。

---

# 113. node-level

加入：

- CPU；
- RAM；
- local storage。

---

# 114. cluster-level

再加入：

- network fabric；
- shared storage；
- orchestration resources。

---

# 115. data-center-level

再加入：

- power/cooling infrastructure；
- networking。

---

# 116. lifecycle-level

甚至加入：

- hardware manufacturing；
- amortized embodied resource。

---

# 117. 本篇不要求一開始用最大 boundary

但要求：

$$
\boxed{
\text{Boundary must be declared}.
}
$$

---

# 118. Measurement Grade

本文提出 CST measurement grade：

# CST-D — Spec Estimate

由 model config / device spec 推估。

---

# 119. CST-C — Runtime Software Trace

有 framework profiler：

- kernel；
- memory；
- device timing。

---

# 120. CST-B — Hardware Telemetry

有 device-level：

- occupancy；
- memory bandwidth；
- interconnect counters。

---

# 121. CST-A — Cluster Trace

有 multi-node synchronized telemetry。

---

# 122. CST-A+ — Causal Resource Attribution

能透過 controlled baseline / workload isolation，把 shared resource 因果分攤到任務。

---

# 123. 這與 Paper 04 E-Grade 對齊

所以每次 IPM report 可同時給：

$$
Grade_{\mu},
EGrade,
CSTGrade.
$$

---

# 124. 這形成 Measurement Confidence Bundle

$$
\boxed{
\mathcal G_M
=
(
Grade_{\mu},
Grade_E,
Grade_{CST}
).
}
$$

---

# 125. Physical Computation Cost Vector

現在正式定義：

$$
\boxed{
\mathbf C_P
=
(
\mathbf O,
\mathbf B_M,
B_I,
\mathbf B_N,
V_M,
V_C,
T,
\mathcal E
).
}
$$

---

# 126. 這裡刻意保留階層向量

而不是太早總和。

---

# 127. 完整物理事件描述

$$
\boxed{
\mathfrak P_{\mathrm{compute}}
=
(
\mathbf C_P,
\mathbf V_{CST},
\Theta_{CST},
H_{\mathrm{peak}},
\mathcal E,
Boundary_P,
\mathcal G_M
).
}
$$

---

# 128. 接回語意層

Paper 02–03 已有：

$$
\mathbf N_{\mu},
Conf_{\mu}.
$$

---

# 129. 所以跨層完整鏈

$$
\boxed{
\mathfrak P_{\mathrm{compute}}
\rightarrow
\mathbf N_{\mu}
\rightarrow
Q.
}
$$

---

# 130. 這才是「智能花了多少物理世界」

而不是：

$$
\boxed{
TokenCount
}
$$

或：

$$
\boxed{
FLOPs
}
$$

單獨回答。

---

# 131. 十六個 Canonical Invariants

**Invariant 1**

$$
\boxed{
FLOPs
\neq
PhysicalComputationalCost.
}
$$

**Invariant 2**

$$
\boxed{
MemoryTraffic
\neq
MemoryResidency.
}
$$

**Invariant 3**

$$
\boxed{
SameFLOPs
\neq
SameLatency.
}
$$

**Invariant 4**

$$
\boxed{
SameFLOPs
\neq
SameEnergy.
}
$$

**Invariant 5**

$$
\boxed{
SameDeviceTime
\neq
SameEnergy.
}
$$

**Invariant 6**

$$
\boxed{
SameCSTVolume
\neq
SameCSTTopology.
}
$$

**Invariant 7**

$$
\boxed{
TotalResource
\neq
PeakCapacityRequirement.
}
$$

**Invariant 8**

$$
\boxed{
MoreDevices
\not\Rightarrow
LowerLatency.
}
$$

**Invariant 9**

$$
\boxed{
ByteAccess
\neq
FixedCost.
}
$$

**Invariant 10**

$$
\boxed{
CommunicationBytes
\neq
CommunicationCost.
}
$$

**Invariant 11**

$$
\boxed{
PeakThroughput
\neq
AttainableThroughput.
}
$$

**Invariant 12**

$$
\boxed{
LowUtilization
\neq
BadSystem.
}
$$

**Invariant 13**

$$
\boxed{
NominalOps
\neq
ExecutedOps.
}
$$

**Invariant 14**

$$
\boxed{
ExecutedOps
\neq
UsefulSemanticWork.
}
$$

**Invariant 15**

$$
\boxed{
ScalarCST
\Rightarrow
DeclaredNormalization.
}
$$

**Invariant 16**

$$
\boxed{
CSTComparison
\Rightarrow
SameBoundaryOrExplicitConversion.
}
$$

---

# 132. 對 IPM 統一事件向量的再擴張

Paper 04：

$$
\mathfrak E'''=
(
Q,
\mathbf N_{\mu},
Conf_{\mu},
Grade_{\mu},
U,G,I,L,R,S,T,
\mathcal E,
Boundary_E,
V_{CST}
).
$$

---

# 133. Paper 05 正式替換單一 $V_{CST}$

得到：

$$
\boxed{
\mathfrak E^{(5)}
=
(
Q,
\mathbf N_{\mu},
Conf_{\mu},
U,G,I,L,R,S,
\mathfrak P_{\mathrm{compute}}
).
}
$$

---

# 134. 這是更乾淨的 hierarchical representation

最上層：

$$
Q.
$$

---

# 135. 中間層：

$$
\mathbf N_{\mu}.
$$

---

# 136. 底層：

$$
\mathfrak P_{\mathrm{compute}}.
$$

---

# 137. 因此完整因果方向

$$
\boxed{
\text{Physical Resources}
\rightarrow
\text{Algorithmic Execution}
\rightarrow
\text{Semantic Work}
\rightarrow
\text{Quality}.
}
$$

---

# 138. 逆向量測方向

則是：

$$
\boxed{
Q
\rightarrow
\widehat{\mathbf N}_{\mu}
\rightarrow
\widehat{\mathfrak P}_{\mathrm{compute}}.
}
$$

其中每一層都有 measurement uncertainty。

---

# 139. 智能效率最終不應只有一個 scalar

至少先報：

$$
\boxed{
\mathcal F_{\mathrm{IPM}}
=
(
Q,
T,
E_{\mathrm{marg}},
V_C,
V_M,
B_M,
B_N,
H_{\mathrm{peak}},
L,R
).
}
$$

---

# 140. Pareto dominance

若 A：

$$
Q_A\ge Q_B
$$

且所有成本軸：

$$
C_{A,j}\le C_{B,j},
$$

至少一項嚴格較優，

則：

$$
\boxed{
A\succ_P B.
}
$$

---

# 141. 若不是 dominance

就不要假裝有唯一優勝者。

---

# 142. 例如

A：

- 快；
- 耗能高。

B：

- 慢；
- 省電。

---

# 143. 哪個更好

取決於：

$$
\boxed{
DeploymentObjective.
}
$$

---

# 144. 這就是為什麼 IPM 不是 AI IQ 榜

它是一套：

$$
\boxed{
\text{physical-semantic metrology}.
}
$$

---

# 145. 結論：計算其實是一段資源占用歷史

如果只看：

$$
FLOPs,
$$

我們看到的是：

> 系統做了多少 arithmetic。

如果只看：

$$
Joules,
$$

我們看到的是：

> 系統總共耗散多少能源。

如果只看：

$$
GPU\cdot hours,
$$

我們看到的是：

> 某類 device 被占用了多久。

這些都重要。

但都不是完整計算。

真正一次物理計算更接近：

$$
\boxed{
\textbf{
一組計算、記憶體、互連與儲存資源，
在一段時間中以特定並行與通訊拓撲，
維持並轉換物理狀態的歷史。
}
}
$$

所以本文把「計算時空」從修辭改造成可操作結構：

$$
\boxed{
\mathbf V_{CST}
=
\int \mathbf R(t)\,dt.
}
$$

但我們同時拒絕把不同量綱亂加。

因此：

$$
\boxed{
\mathbf V_{CST}
}
$$

首先是向量。

而不是：

> 一個看起來很酷的總分。

只有在 reference、weights、boundary 全部明示後，

才允許：

$$
V_{CST}^{*}.
$$

而且即使 volume 相同，

仍必須保留：

$$
\Theta_{CST}
$$

因為：

$$
\boxed{
8GPU\times10s
}
$$

和：

$$
\boxed{
1GPU\times80s
}
$$

不具有相同：

- latency；
- peak capacity；
- communication；
- deployability。

因此：

$$
\boxed{
\text{Volume}
\neq
\text{Topology}.
}
$$

這一篇也把我們最初的「時空間函數」真正往物理計算語言落下來。

現在，一次智能成果可以被描述為：

$$
\boxed{
\mathfrak P_{\mathrm{compute}}
\rightarrow
\mathbf N_{\mu}
\rightarrow
Q.
}
$$

也就是：

> 世界占用了多少實體計算時空？

> 這些時空真正完成多少有效語意工作？

> 最後換回多少成果品質？

到這一步，分母已經相對完整。

下一個真正的大問題就變成：

$$
\boxed{
\textbf{
那分子 $Q$ 到底怎麼量？
}
}
$$

對數學、程式與形式邏輯，我們可以大量依賴：

- correctness；
- proof；
- tests；
- verification；
- constraint satisfaction。

所以 Paper 06 將正式進入：

**《成果品質到底怎麼量？：從形式化正確性到結構化智能品質》**。

這會開始建立 IPM 的品質測量端，並為 Paper 07 的 IBQF 二元人類評估準備基礎。

---

## 文獻基礎

[1] Williams, S., Waterman, A., & Patterson, D. (2009). Roofline: An Insightful Visual Performance Model for Multicore Architectures. *Communications of the ACM*, 52(4), 65–76. DOI: 10.1145/1498765.1498785.  

[2] Wulf, W. A., & McKee, S. A. (1995). Hitting the Memory Wall: Implications of the Obvious. *ACM SIGARCH Computer Architecture News*, 23(1), 20–24. DOI: 10.1145/216585.216588.  

[3] Sze, V., Chen, Y.-H., Yang, T.-J., & Emer, J. S. (2017). Efficient Processing of Deep Neural Networks: A Tutorial and Survey. *Proceedings of the IEEE*, 105(12), 2295–2329. DOI: 10.1109/JPROC.2017.2761740.  

[4] Chen, Y.-H., Emer, J., & Sze, V. (2016). Eyeriss: A Spatial Architecture for Energy-Efficient Dataflow for Convolutional Neural Networks. *ISCA 2016*. DOI: 10.1109/ISCA.2016.40.  

[5] Jouppi, N. P. et al. (2017). In-Datacenter Performance Analysis of a Tensor Processing Unit. *ISCA 2017*, 1–12. DOI: 10.1145/3079856.3080246.  

[6] Patterson, D. et al. (2021). Carbon Emissions and Large Neural Network Training. arXiv:2104.10350.  

[7] Ivanov, A., Dryden, N., Ben-Nun, T., Li, S., & Hoefler, T. (2021). Data Movement Is All You Need: A Case Study on Optimizing Transformers. *MLSys 2021*.  

[8] Chen, Y., Yang, T.-J., Emer, J., & Sze, V. (2018/2019). Understanding the Limitations of Existing Energy-Efficient Design Approaches for Deep Neural Networks. *SysML / MLSys*.  

---

## 系列路徑

1. **Paper 01｜一輪到底是一輪什麼？：使用者回合、隱藏 LOOP 與單次智能的重新定義**  
2. **Paper 02｜智能到底算了一次什麼？：最小智能語意執行單位的候選理論**  
3. **Paper 03｜從認知到神經元：人腦如何跨層測量智能計算**  
4. **Paper 04｜從神經元到焦耳：智能計算的能量、熱力學與物理下界**  
5. **Paper 05｜計算不是只有 FLOPs：記憶體、互連、硬體占用與計算時空體積**  
6. **Paper 06｜成果品質到底怎麼量？：從形式化正確性到結構化智能品質**  
7. **Paper 07｜不要叫人類替自己的感覺打分數：IBQF 二元測量與低負擔品質評估**  
8. **Paper 08｜自然語言、圖像與創意如何被量？：高歧義成果的結構化品質空間**  
9. **Paper 09｜拿掉 LOOP 還剩多少智能？：單次智能、鷹架依賴與隱藏計算成本**  
10. **Paper 10｜一個答案值多少物理世界？：智能產率的統一計量框架**
