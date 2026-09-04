# 監督器與物理核心分離：Embedded Supervisor Architecture

**系列：外掛式物理計算機與現場計算設備研究，第 3 篇**  
**英文系列名：External Physical Compute Appliances and Field Computing Systems**  
**英文篇名：Supervisor–Physical-Core Separation: An Embedded Supervisor Architecture for Verifiable Physical Computing**  
**版本：v0.1**  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：2026-08-29**  
**狀態：公開草稿／系統架構、權限與執行合約框架**

## 摘要

前兩篇分別將算盤抽象為可跨 substrate 實現的受約束狀態轉移幾何，並建立 Observable Physical Computation 的驗證分級，要求 physical compute core 的計算貢獻能被量測、干預、消融與獨立驗證。然而，一旦一台 External Physical Compute Appliance 同時包含 Linux SoC、real-time controller、FPGA、ADC/DAC、感測器、記憶體、網路與 physical core，系統將立刻面臨一個更困難的工程問題：如何讓 supervisor 足夠強，能處理配置、校正、時序、重置、更新、refinement、記錄與失效復原，同時又不讓它在未聲明的情況下取代 physical core 的計算角色？

本文提出 Supervisor–Physical-Core Separation Architecture，主張 supervisor 不應被視為單一處理器，而應拆成具有不同時間尺度、權限與失效域的多個 plane：Application Plane、Real-Time Control Plane、Deterministic I/O / Fabric Plane、Platform Management Plane、Verification Plane，以及獨立的 Physical Compute Plane。Linux-class application processor 負責高階任務、使用者介面、套件、網路與非硬即時協調；real-time processor 或 RTOS/bare-metal context 負責 deadline-sensitive sequencing；FPGA 或 programmable logic 負責 deterministic I/O、timestamp、trigger、protocol 與高速資料搬運；platform manager 負責 boot、power、thermal、watchdog 與 recovery；verification plane 保存 raw evidence、challenge、版本與執行承諾；physical core 則保留任務中被宣告為 physical computation 的不可替代因果路徑。

本文進一步提出四個核心不變量：Declared Compute Boundary、No Silent Substitution、Reference-Path Isolation 與 Evidence-Before-Refinement。任何 pre-processing、post-processing 或 digital refinement 都可以存在，但必須被顯式納入 operator chain；reference solver 可以計算正確答案，卻不得寫入 physical result acquisition path；若 physical core 失效，系統可以 fail、degrade 或明確切換 digital fallback，但不得以相同 backend identity 靜默回傳數位結果；任何最終 refinement 之前，必須先固定 physical raw observation、decoder version 與 physical result。

本文定義 Embedded Physical Compute Job Contract，將一次執行拆為 Prepare、Commit、Arm、Execute、Acquire、Decode、Verify、Refine、Publish、Reset 十個階段，並提出 capability/authority matrix、memory partition、result-path taint model、fault-domain model 與 supervisor assurance levels ESA-S0 至 ESA-S5。本文也說明 Linux PREEMPT_RT、heterogeneous application/real-time processors、remoteproc/RPMsg/OpenAMP、hardware watchdog 與 adaptive SoC 等既有技術，可以支撐此架構的大部分控制面；本文的新意不在宣稱這些元件首次存在，而在於將它們組合為一套面向 verifiable physical computing 的權限、因果與證據架構。

本文最後指出，physical computing 的實用化不要求「純物理、零數位控制」。相反地，真正可部署的設備可能高度依賴 digital supervisor。重要的不是數位部分有多強，而是計算責任是否被清楚分配、是否可以驗證、是否存在未聲明的替代路徑，以及設備在失效時是否保持身份與證據的一致性。這一架構為下一篇 Offline-First Field Appliance 提供本地自治、Linux、real-time、更新與斷網運行的控制基礎。

**關鍵詞：** Embedded Supervisor、Physical-Core Non-Substitution、heterogeneous SoC、real-time control、FPGA、Linux、OpenAMP、remoteproc、RPMsg、watchdog、physical computing、provenance、External Physical Compute Appliance

---

## 1. 問題：Supervisor 越強，物理計算越容易被吃掉

一台最簡單的 physical computing demonstrator 可以寫成

$$
x
\rightarrow
\mathcal P
\rightarrow
y_{\mathcal P},
$$

其中 $\mathcal P$ 是 physical compute core。

但真正可用的設備通常還需要：

- 輸入解析；
- 演算法選擇；
- configuration；
- calibration；
- timing；
- ADC/DAC；
- memory；
- display；
- logging；
- network；
- software update；
- error handling；
- reference verification；
- optional digital refinement。

因此很自然會加入 supervisor $\mathcal S$：

$$
\mathcal M
=
(\mathcal S,\mathcal P).
$$

然而當 $\mathcal S$ 的計算力逐漸增加，會出現一個結構性風險：

$$
\mathcal S
\supseteq
F_{\tau},
$$

也就是 supervisor 本身已足以完成目標任務 $F_{\tau}$。

此時 physical core 是否仍在計算，不再能靠設備外觀判定。

最危險的退化形式是：

$$
x
\rightarrow
\mathcal S(x)
\rightarrow
y
\rightarrow
\mathcal P_{\text{display}}.
$$

物理核心仍然亮、仍然振盪、仍然輸出訊號，但已失去真正的 computational authority。

因此本文的核心不是限制 supervisor 的性能，而是限制它的**未聲明權限**。

---

## 2. 核心原則：強 Supervisor 與真 Physical Compute 不矛盾

本文拒絕一個過度純化的命題：

$$
\text{digital assistance}
\Rightarrow
\text{not physical computing}.
$$

這個命題不成立。

實際 physical computing 很可能需要大量數位輔助。

例如：

$$
\text{digital calibration}
+
\text{physical transform}
+
\text{digital decoding}
$$

仍然可以是一個真實的 hybrid physical computing pipeline。

真正需要禁止的是：

$$
\boxed{
\text{silent substitution}
}
$$

也就是系統對外宣稱執行 backend 為 $\mathcal P$，實際卻由 $\mathcal S$ 完成相同 functional mapping。

因此：

$$
\boxed{
\text{Supervisor Strength}
\neq
\text{Supervisor Authority}
}
$$

一顆很強的 CPU 可以只有有限的 result-path authority；一顆很弱的 MCU 也可能因架構設計不良而具有完全替代權限。

---

## 3. 從單一 Supervisor 改為多 Plane 架構

本文將 supervisor 展開為：

$$
\mathcal S
=
\mathcal A
\oplus
\mathcal R
\oplus
\mathcal F
\oplus
\mathcal M_g
\oplus
\mathcal V,
$$

其中：

- $\mathcal A$：Application Plane；
- $\mathcal R$：Real-Time Control Plane；
- $\mathcal F$：Deterministic I/O / Fabric Plane；
- $\mathcal M_g$：Platform Management Plane；
- $\mathcal V$：Verification Plane。

另外保留：

$$
\mathcal P
=
\text{Physical Compute Plane}.
$$

因此 EPCA 的執行核心可寫成：

$$
\boxed{
\mathcal M_{\text{exec}}
=
\mathcal A
\oplus
\mathcal R
\oplus
\mathcal F
\oplus
\mathcal M_g
\oplus
\mathcal V
\oplus
\mathcal P.
}
$$

這種拆法的目的不是追求元件數量，而是將不同時間尺度與權限分離。

---

## 4. Application Plane：Linux 應該做什麼？

Application Plane 最適合由 Linux-class processor 執行。

其任務包括：

$$
\begin{aligned}
&\text{user interface},\\
&\text{job parsing},\\
&\text{algorithm package management},\\
&\text{networking},\\
&\text{filesystem},\\
&\text{database},\\
&\text{update orchestration},\\
&\text{high-level scheduling},\\
&\text{non-real-time preprocessing},\\
&\text{report generation}.
\end{aligned}
$$

Application Plane 可以很強。

它甚至可以具有多核心 CPU、大量 RAM、GPU 或 NPU。

但本文主張：

$$
\boxed{
\mathcal A
\text{ 不應直接成為 hard real-time pulse / trigger loop 的唯一執行者。}
}
$$

原因不只在性能，而在可預測性與 fault isolation。

Linux 適合複雜軟體環境；critical timing 則應盡可能下沉到 real-time 或 programmable logic plane。

---

## 5. Real-Time Control Plane：控制時間，而不是偷偷算答案

Real-Time Control Plane $\mathcal R$ 負責：

- trigger sequencing；
- fixed-period control loop；
- pulse scheduling；
- safety interlock；
- deterministic sensor acquisition；
- timeout；
- reset sequencing；
- hardware state machine coordination。

可寫為：

$$
u_{t+1}
=
\mathcal R(z_t,c_t),
$$

其中 $z_t$ 是設備狀態， $c_t$ 是當前 command context。

重要的是， $\mathcal R$ 的合法職責通常是：

$$
\text{control law},
$$

而不是：

$$
F_{\tau}(x).
$$

若某個任務確實需要 real-time processor 執行部分數位計算，則必須顯式聲明：

$$
F_{\tau}
=
D
\circ
P
\circ
R
\circ
E,
$$

而不能把 $R$ 隱藏在「控制器」這個名稱裡。

---

## 6. Deterministic I/O / Fabric Plane：高速、固定、可追蹤

對光、RF、聲學、類比或 CIM backend，I/O 經常比高階軟體更接近性能瓶頸。

因此可將 $\mathcal F$ 放在 FPGA、CPLD、programmable logic 或專用 interface ASIC 中。

其工作包括：

$$
\begin{aligned}
&\text{ADC/DAC framing},\\
&\text{sample alignment},\\
&\text{timestamp},\\
&\text{trigger fan-out},\\
&\text{high-speed protocol},\\
&\text{DMA},\\
&\text{buffering},\\
&\text{simple deterministic transform},\\
&\text{hardware interlock}.
\end{aligned}
$$

這個 plane 很容易變成隱性計算核心。

例如 FPGA 中的一段 DSP pipeline 可能已完成：

$$
y=F_{\tau}(x).
$$

因此本文要求 FPGA bitstream 也屬於 provenance：

$$
\boxed{
\text{bitstream identity}
\in
\text{execution evidence}.
}
$$

不能只記錄 Linux software version。

---

## 7. Platform Management Plane：它可以重啟一切，但不能改寫結果

Platform Management Plane $\mathcal M_g$ 負責設備生命週期：

- boot；
- secure / verified boot 選配；
- power domain；
- clock domain；
- thermal management；
- watchdog；
- reset；
- health monitoring；
- fallback image；
- low-level recovery。

它的 authority 可以很高，例如：

$$
\mathcal M_g
:\
\text{system}
\rightarrow
\text{reset}.
$$

但高 platform authority 不等於 result authority。

本文要求：

$$
\boxed{
\mathcal M_g
\text{ 可以終止一個結果，不能在失效時偽造一個結果。}
}
$$

也就是：

$$
\text{failure}
\rightarrow
\text{FAIL / RETRY / FALLBACK-DECLARED},
$$

而不是：

$$
\text{failure}
\rightarrow
\text{silent synthetic result}.
$$

---

## 8. Verification Plane：不是 UI Logger

Verification Plane $\mathcal V$ 不只是 log service。

它應保存足以重建一次執行證據鏈的資料：

$$
E
=
(x,h_c,\theta,u,o,y_{\mathcal P},d,v,t,f),
$$

其中可以包含：

- $x$：輸入；
- $h_c$：pre-execution commitment；
- $\theta$：configuration；
- $u$：control trace；
- $o$：raw observations；
- $y_{\mathcal P}$：decoded physical result；
- $d$：decoder identity；
- $v$：software / firmware / bitstream version；
- $t$：time metadata；
- $f$：fault / health state。

因此 $\mathcal V$ 的第一原則是：

$$
\boxed{
\text{evidence must precede interpretation whenever feasible}.
}
$$

若只保存 supervisor 已解釋後的 summary，日後很難重新判斷 physical core 是否真的符合模型。

---

## 9. Physical Compute Plane：保留被宣告的因果核心

Physical Compute Plane $\mathcal P$ 可以是：

- optical network；
- RF metastructure；
- acoustic network；
- analog circuit；
- memristive / CIM array；
- spin-wave system；
- mechanical network；
- fluidic system；
- 其他可控制且可讀出的 physical substrate。

本文不要求 $\mathcal P$ 獨立完成整個 task。

只要求系統清楚聲明它負責的 operator：

$$
P_{\theta}:X_P\rightarrow Y_P.
$$

完整任務可以是：

$$
F_{\tau}
=
D
\circ
P_{\theta}
\circ
E.
$$

或混合形式：

$$
F_{\tau}
=
R_2
\circ
D
\circ
P_{\theta}
\circ
R_1
\circ
E.
$$

只要 $R_1$ 、 $R_2$ 被明確揭露，這仍然是合法的 hybrid compute pipeline。

---

## 10. 第一不變量：Declared Compute Boundary

對每一個 job，系統必須先聲明計算邊界：

$$
B_J
=
(E,R_1,P,D,R_2).
$$

其中哪些是：

$$
\text{digital},
$$

哪些是：

$$
\text{physical},
$$

哪些是：

$$
\text{measurement},
$$

都應可被 inspection。

因此不能只說：

> 本設備使用 photonic computing。

而應至少能說：

$$
\boxed{
P_{\theta}
\text{ 在完整 operator chain 中負責哪一段。}
}
$$

---

## 11. 第二不變量：No Silent Substitution

若 job manifest 宣告 backend 為 $\mathcal P_k$，則 execution identity 為：

$$
I_J
=
(\tau,\mathcal P_k,B_J,v_J).
$$

若 $\mathcal P_k$ 失效，系統可以：

$$
\text{FAIL},
$$

$$
\text{RETRY},
$$

或：

$$
\text{FALLBACK}(\mathcal D),
$$

其中 $\mathcal D$ 是 digital backend。

但若 fallback 發生，身份必須改為：

$$
I'_J
=
(\tau,\mathcal D,B'_J,v'_J).
$$

因此：

$$
\boxed{
I'_J
\neq
I_J.
}
$$

這就是 No Silent Substitution。

---

## 12. 第三不變量：Reference-Path Isolation

Paper 02 允許 reference solver：

$$
y_{\mathcal R}
=
F_{\mathrm{ref}}(x).
$$

但如果 reference solver 和 result acquisition 共享可寫路徑，驗證就會被污染。

因此需要：

$$
\boxed{
\mathcal R_{\mathrm{ref}}
\not\rightarrow
\text{physical-result write path}.
}
$$

Reference solver 可以：

- 讀取 input；
- 讀取 physical result；
- 計算 expected answer；
- 產生 comparison metric。

但不應：

- 寫入 raw measurement buffer；
- 覆寫 $y_{\mathcal P}$ ；
- 在 physical acquisition failure 時自動補值；
- 修改 challenge response。

---

## 13. 第四不變量：Evidence Before Refinement

若 physical backend 是低精度類比裝置，數位 refinement 很合理。

例如：

$$
y_0
=
y_{\mathcal P},
$$

再：

$$
y
=
\mathcal R_f(x,y_0).
$$

但如果只保存 $y$，將無法判斷 physical core 的原始貢獻。

所以本文要求：

$$
\boxed{
(y_{\mathcal P},E_{\mathrm{raw}})
\text{ must be committed before }
\mathcal R_f.
}
$$

最後輸出可以同時包含：

$$
R
=
(y_{\mathcal P},y_{\mathrm{final}},E).
$$

這使 mixed-precision 不會破壞 causal attribution。

---

## 14. Job Contract：一次計算不再只是 function call

本文提出 Embedded Physical Compute Job Contract。

一次 job $J$ 可表示為：

$$
J
=
(x,\tau,B_J,C_J,Q_J),
$$

其中：

- $x$：輸入；
- $\tau$：task / algorithm identity；
- $B_J$：compute boundary；
- $C_J$：constraints；
- $Q_J$：verification / quality policy。

執行不應只有：

$$
\operatorname{run}(x).
$$

而應形成明確生命週期。

---

## 15. 十階段執行生命週期

本文建議最小狀態機：

$$
\boxed{
\text{Prepare}
\rightarrow
\text{Commit}
\rightarrow
\text{Arm}
\rightarrow
\text{Execute}
\rightarrow
\text{Acquire}
\rightarrow
\text{Decode}
\rightarrow
\text{Verify}
\rightarrow
\text{Refine}
\rightarrow
\text{Publish}
\rightarrow
\text{Reset}.
}
$$

各階段職責如下。

### 15.1 Prepare

解析 job、載入 backend、校正、分配 buffer。

### 15.2 Commit

固定 configuration、operator chain、版本與 challenge context。

### 15.3 Arm

啟動 hardware trigger、sensor、evidence capture。

### 15.4 Execute

physical core 執行被宣告的 operator。

### 15.5 Acquire

取得 raw physical observation。

### 15.6 Decode

由固定 decoder 將 observation 轉為 $y_{\mathcal P}$。

### 15.7 Verify

reference comparison、intervention check、health check。

### 15.8 Refine

若 policy 允許，進行明確標示的 digital refinement。

### 15.9 Publish

輸出 result 與 evidence envelope。

### 15.10 Reset

將 backend 回到可重複的初始條件。

---

## 16. Commit 階段為什麼重要？

如果 configuration 可以在 execution 後被修改，provenance 就會失真。

因此 Commit 應產生：

$$
h_J
=
H(
\tau,
B_J,
\theta,
v_{\mathrm{fw}},
v_{\mathrm{bit}},
v_{\mathrm{decoder}},
q
).
$$

這個 hash 不一定一開始就需要 trusted hardware。

即使只是普通 cryptographic hash，也能提供：

$$
\text{before/after consistency}.
$$

真正高安全等級的 attestation 可以留到產品化階段。

---

## 17. Authority Matrix：能力和權限分開

本文建議每個 plane 都有 capability 與 authority 兩張表。

例如：

| Plane | 可讀 input | 可寫 config | 可觸發 physical core | 可寫 raw evidence | 可寫 physical result | 可計算 reference | 可 reset system |
|---|---:|---:|---:|---:|---:|---:|---:|
| Application $\mathcal A$ | 是 | 是 | 間接 | 否 | 否 | 可 | 請求 |
| Real-Time $\mathcal R$ | 有限 | 有限 | 是 | append only | 否 | 原則上否 | backend |
| Fabric $\mathcal F$ | stream | hardware | 是 | append / DMA | 只寫 raw acquisition | 否 | backend |
| Management $\mathcal M_g$ | metadata | platform | enable/disable | 否 | 否 | 否 | 是 |
| Verification $\mathcal V$ | 是 | 否 | challenge | append / seal | seal | 可比較 | 否 |
| Physical $\mathcal P$ | encoded | physical | n/a | sensor 產生 | 因果來源 | 否 | physical reset |

這不是唯一合法矩陣。

真正重要的是：

$$
\boxed{
\text{capability}
\neq
\text{authority}.
}
$$

---

## 18. Result Path 應該是單向的

對驗證級 backend，理想 result path 為：

$$
\mathcal P
\rightarrow
\mathcal F
\rightarrow
\mathcal V
\rightarrow
D
\rightarrow
y_{\mathcal P}.
$$

Application Plane 可以讀：

$$
y_{\mathcal P},
$$

卻不應直接寫入此路徑。

若需要 refinement：

$$
y_{\mathcal P}
\rightarrow
\mathcal R_f
\rightarrow
y_{\mathrm{final}}.
$$

因此 physical result 與 final result 是兩個不同欄位，而不是同一個 mutable variable。

---

## 19. Result-Path Taint Model

本文引入簡化的 taint 標記。

資料來源可以標為：

$$
T
\in
\{
P,D,R,M,U
\},
$$

其中：

- $P$：physical-origin；
- $D$：digital-computed；
- $R$：reference-only；
- $M$：measured metadata；
- $U$：user-provided。

若 $y_{\mathcal P}$ 的 dependency graph 中出現 reference-only value：

$$
R
\rightarrow
y_{\mathcal P},
$$

則應視為驗證污染。

這個 model 不需要一開始就做成完整 information-flow security system。

它首先是一個 architecture review rule。

---

## 20. Memory 不應只有一塊 Shared RAM

異質系統最容易的做法是所有 processor 共用一大塊 RAM。

這很方便，但驗證邊界會變模糊。

本文建議至少概念上區分：

$$
M
=
M_A
\oplus
M_R
\oplus
M_F
\oplus
M_E
\oplus
M_{\mathrm{ref}}.
$$

其中：

- $M_A$：application memory；
- $M_R$：real-time state；
- $M_F$：DMA / acquisition buffer；
- $M_E$：evidence ring / evidence store；
- $M_{\mathrm{ref}}$：reference solver memory。

即使底層仍位於同一 DDR，也應透過：

- MMU / MPU；
- IOMMU；
- hardware firewall；
- reserved memory；
- access control；
- process isolation；

建立邏輯邊界。

---

## 21. Linux 與 Hard Real-Time：不要把問題假裝不存在

Linux 可以做 real-time。

現代 mainline kernel 已包含 PREEMPT_RT 路徑，可大幅降低 scheduling latency，並支援 real-time scheduling policy。

但本文仍不主張把所有 deterministic control 都塞進 Linux userspace。

原因是整體 deadline 不只受 scheduler 影響，還包含：

$$
L
=
L_{\mathrm{sched}}
+
L_{\mathrm{irq}}
+
L_{\mathrm{bus}}
+
L_{\mathrm{driver}}
+
L_{\mathrm{DMA}}
+
L_{\mathrm{device}}.
$$

因此架構應依 deadline 分層。

例如：

$$
\text{ms--s scale}
\rightarrow
\mathcal A,
$$

$$
\text{us--ms deterministic loop}
\rightarrow
\mathcal R,
$$

$$
\text{sub-us / cycle-level timing}
\rightarrow
\mathcal F.
$$

具體界線依硬體而定，不應把上述數值視為固定標準。

---

## 22. Heterogeneous SoC 為什麼很適合 EPCA？

現有 adaptive SoC 已經證明一種成熟模式：

$$
\text{Application CPU}
+
\text{Real-Time CPU}
+
\text{Programmable Logic}
+
\text{Platform Manager}.
$$

這和本文需要的 supervisor decomposition 高度相容。

因此 EPCA 第一代不必自製 SoC。

可以直接利用現有異質平台，把：

$$
\mathcal A,\mathcal R,\mathcal F,\mathcal M_g
$$

映射到既有硬體，再將真正新的研究集中於：

$$
\mathcal P
+
\mathcal V
+
\text{contract}.
$$

這能大幅降低 MVP 的不必要工程風險。

---

## 23. Linux + RTOS / Bare Metal 不是奇怪架構

現有 Linux remoteproc、RPMsg 與 OpenAMP 已經支援 asymmetric multiprocessing 的典型模式：

$$
\text{Linux host}
\leftrightarrow
\text{RTOS / bare-metal remote processor}.
$$

這意味著 EPCA 可以採：

$$
\mathcal A_{\text{Linux}}
\leftrightarrow
\mathcal R_{\text{RTOS}}
\leftrightarrow
\mathcal F
\leftrightarrow
\mathcal P.
$$

Linux 負責 remote processor lifecycle 與高階 IPC；real-time context 則保持較小、較可預測的 execution surface。

本文不綁定 OpenAMP，但將它視為一個重要的現成工程參考。

---

## 24. IPC Contract 應該比 Generic RPC 更窄

如果 Application Plane 可以任意 RPC 到 real-time plane，權限邊界可能只是形式上的。

因此本文建議 EPCA 定義窄介面，例如：

$$
\operatorname{prepare}(job),
$$

$$
\operatorname{arm}(commitment),
$$

$$
\operatorname{execute}(token),
$$

$$
\operatorname{abort}(reason),
$$

$$
\operatorname{status}(),
$$

$$
\operatorname{read\_evidence}(cursor),
$$

$$
\operatorname{reset}(scope).
$$

而不是提供：

$$
\operatorname{write\_arbitrary\_memory}().
$$

或：

$$
\operatorname{run\_arbitrary\_code}().
$$

這就是最小權限原則在 compute appliance 中的具體形式。

---

## 25. Calibration 是控制，不是免責區

類比 physical core 幾乎一定需要 calibration：

$$
\theta^*
=
\operatorname{Calibrate}(r,s,e),
$$

其中 $r$ 是 reference stimulus， $s$ 是 sensor response， $e$ 是 environment state。

但 calibration routine 本身也可能偷偷學會：

$$
F_{\tau}.
$$

因此必須區分：

$$
\text{device calibration}
$$

與：

$$
\text{task solving}.
$$

若 calibration 依賴 task-specific ground truth，應記入 compute boundary。

例如：

$$
P_{\theta(x)}(x)
$$

和：

$$
P_{\theta_0}(x)
$$

不是同一種系統。

---

## 26. Preprocessing 也可能吃掉整個問題

假設 physical core 只接受低維向量：

$$
z=E(x).
$$

如果 $E$ 已經計算出答案，然後只把答案編碼給 physical core，則：

$$
P(E(x))
$$

只是 presentation path。

因此 preprocessing 必須接受 contribution audit。

一個簡單測試是：

若將 physical core 替換為 identity 或 random operator，preprocessing 是否仍足以高精度重建答案？

若是，則 physical contribution 可能過低。

這個判斷不一定是二元，但必須被量測。

---

## 27. Decoder 也可能是隱藏 Solver

類似地：

$$
y=D(o,x).
$$

如果 decoder 同時讀取原始 input $x$，就可能完全忽略 physical observation $o$。

所以對高驗證等級，應檢查：

$$
I(y;o\mid x),
$$

或至少用 intervention 測試：

$$
o
\rightarrow
o'
$$

是否會產生模型一致的：

$$
y
\rightarrow
y'.
$$

若 decoder 在 $o$ 被破壞後仍穩定回傳正確答案，必須解釋其來源。

---

## 28. Fault Domain：Linux 掛掉，不應等於物理核心瞬間失控

現場設備必須考慮 fault containment。

本文建議至少區分：

$$
F_A,
F_R,
F_F,
F_P,
F_V,
F_M.
$$

例如：

### 28.1 Application Plane failure

可能反應：

$$
\text{RT plane completes current safe transaction}
\rightarrow
\text{quiesce}.
$$

### 28.2 Real-Time Plane failure

可能反應：

$$
\text{fabric interlock}
\rightarrow
\text{disable physical excitation}.
$$

### 28.3 Physical Core failure

可能反應：

$$
\text{mark result invalid}
\rightarrow
\text{capture evidence}
\rightarrow
\text{reset backend}.
$$

### 28.4 Verification Plane failure

若 policy 要求 OPC-V5：

$$
\text{no evidence}
\Rightarrow
\text{no verified result}.
$$

這些行為必須在 architecture level 定義，而不是等 crash 後臨時決定。

---

## 29. Watchdog：重啟不是唯一用途

Hardware watchdog 的基本作用是：若關鍵 software 不再回報存活，系統能自動 reset。

但 EPCA 可以進一步使用分層 watchdog：

$$
W_A,
W_R,
W_P,
W_E.
$$

分別監控：

- application heartbeat；
- real-time deadline；
- physical backend response；
- evidence pipeline progress。

最重要的原則仍是：

$$
\boxed{
\text{watchdog recovery does not authorize result fabrication}.
}
$$

Reset 可以修復設備；不能修復已經不存在的計算證據。

---

## 30. Safe State 與 Compute State 分離

對具有雷射、RF、超音波、高電壓或其他激勵源的設備，安全狀態應獨立定義。

令：

$$
S_{\mathrm{safe}}
$$

為不持續產生危險輸出的狀態。

任何高階 plane failure 都應存在路徑：

$$
F
\rightarrow
S_{\mathrm{safe}}.
$$

這條路徑最好由：

$$
\mathcal R
\text{ 或 }
\mathcal F
\text{ 或硬體 interlock}
$$

保證，而不是依賴 Linux GUI process 正常運作。

本文不對具體能量或安全規範下結論；實際設備仍需依 substrate 與法規設計。

---

## 31. Backend Driver Contract

對不同 physical core，Application Plane 不應知道全部硬體細節。

可以定義 backend contract：

$$
\mathcal B_k
=
(
C_k,
P_k,
O_k,
R_k,
H_k
),
$$

其中：

- $C_k$：capability descriptor；
- $P_k$：prepare / configure；
- $O_k$：execute / observe；
- $R_k$：reset / recover；
- $H_k$：health / evidence descriptor。

Capability descriptor 可以包含：

$$
\begin{aligned}
&\text{supported operators},\\
&\text{input domain},\\
&\text{output domain},\\
&\text{precision},\\
&\text{latency range},\\
&\text{calibration requirements},\\
&\text{verification level},\\
&\text{environment constraints}.
\end{aligned}
$$

這為 Paper 05 的 modular compute backplane 提供直接接口。

---

## 32. Backend 不能自己宣告自己通過驗證

如果 physical backend driver 同時：

1. 控制硬體；
2. 讀取 raw signal；
3. 解碼；
4. 判斷成功；
5. 產生 provenance；

那麼驗證面仍可能形成單一信任閉環。

因此高 OPC 等級下，至少部分 evidence 應由獨立路徑取得。

例如：

$$
\mathcal P
\rightarrow
\begin{cases}
\mathcal F_1\rightarrow D\rightarrow y_{\mathcal P},\\
\mathcal F_2\rightarrow \mathcal V\rightarrow E_{\mathrm{raw}}.
\end{cases}
$$

不一定要完整雙份硬體，但應避免所有證據只來自同一個可任意修改的 software component。

---

## 33. Supervisor Assurance Levels：ESA-S0 至 ESA-S5

為和 OPC-V 分開，本文提出 Embedded Supervisor Assurance level：

$$
\text{ESA-S0}
\rightarrow
\text{ESA-S1}
\rightarrow
\text{ESA-S2}
\rightarrow
\text{ESA-S3}
\rightarrow
\text{ESA-S4}
\rightarrow
\text{ESA-S5}.
$$

### ESA-S0 — Monolithic Controller

單一 processor / software stack，沒有明確 compute boundary。

### ESA-S1 — Declared Boundary

已記錄 digital / physical operator chain，但仍主要靠軟體規範。

### ESA-S2 — Role-Separated Supervisor

Application、real-time / I/O 與 physical backend 角色分離。

### ESA-S3 — Authority-Separated Result Path

reference path、raw acquisition 與 result publication 具有明確寫入權限分離。

### ESA-S4 — Fault-Isolated Supervisor

具 watchdog、safe-state、memory / processor isolation、declared fallback 與 evidence preservation。

### ESA-S5 — Independently Auditable Supervisor

execution commitment、backend identity、evidence chain、reference isolation 與 critical configuration 可由獨立 verifier 重放或稽核。

ESA-S 是 supervisor architecture assurance，不是設備性能排名。

---

## 34. OPC-V 與 ESA-S 是兩個不同軸

一台設備可以：

$$
\text{OPC-V4},
\quad
\text{ESA-S1},
$$

代表 physical contribution 有很強的實驗證據，但 supervisor engineering 還很原型化。

也可以：

$$
\text{OPC-V1},
\quad
\text{ESA-S4},
$$

代表 embedded system 很穩健，但 physical computation 的因果驗證仍不足。

因此應用二維描述：

$$
\boxed{
Q_{\mathrm{EPCA}}
=
(\mathrm{OPC\mbox{-}V},\mathrm{ESA\mbox{-}S}).
}
$$

未來再加入 performance 與 field robustness，形成多軸 benchmark。

---

## 35. 一個推薦的第一代硬體映射

若目標是研究 demonstrator，而不是量產，本文建議：

$$
\boxed{
\text{Linux SoC}
+
\text{RT core}
+
\text{FPGA / PL}
+
\text{Physical Core}
+
\text{independent measurement path}.
}
$$

其中：

### Linux SoC / APU

負責：UI、algorithm package、storage、network、high-level job orchestration。

### RT core / RPU

負責：trigger、control state machine、deadline、interlock、backend lifecycle。

### FPGA / PL

負責：ADC/DAC、timestamp、DMA、high-speed I/O、hardware trigger。

### Physical Core

負責：被明確定義的 physical operator。

### Verification path

負責：raw capture、challenge、commitment、provenance。

這種配置不要求使用特定廠商，只是一個角色映射。

---

## 36. MVP 不需要 Linux 也可以

雖然本文大量討論 Linux，但 EPCA-0 / EPCA-1 MVP 可以更小：

$$
\text{MCU}
+
\text{FPGA}
+
\mathcal P.
$$

甚至：

$$
\text{MCU}
+
\mathcal P.
$$

只要能保證：

- compute boundary 清楚；
- physical result 可量測；
- reference path 不污染；
- failure 不 silent fallback；
- evidence 可保存。

Linux 是 field appliance 的能力擴張，不是 physical computing 的本體條件。

---

## 37. 何時應該使用 PREEMPT_RT？

若 Application Plane 同時需要較低 latency、複雜 Linux userspace 與 networking，可以採 PREEMPT_RT。

但本文建議將問題寫成：

$$
\text{deadline budget}
\rightarrow
\text{execution placement},
$$

而不是：

$$
\text{Linux or no Linux}.
$$

對每個 control task $c_i$ 定義：

$$
D_i
=
\text{deadline},
$$

$$
J_i
=
\text{allowed jitter},
$$

$$
C_i
=
\text{worst-case execution requirement}.
$$

再決定它屬於：

$$
\mathcal A,
\mathcal R,
\mathcal F
$$

哪一層。

這比用單一 OS 名稱決定全部架構更合理。

---

## 38. Supervisor 的計算也要計入性能成本

若 future benchmark 只量測：

$$
T_{\mathcal P},
$$

會誇大 physical core 的實際效益。

完整 latency 應包含：

$$
T_{\mathrm{end}}
=
T_E
+
T_C
+
T_P
+
T_A
+
T_D
+
T_V
+
T_R,
$$

其中：

- $T_E$：encode / preprocess；
- $T_C$：configure / calibration；
- $T_P$：physical compute；
- $T_A$：acquisition；
- $T_D$：decode；
- $T_V$：verification；
- $T_R$：optional refinement。

能耗也同理：

$$
E_{\mathrm{end}}
=
\sum_i E_i.
$$

Supervisor separation 不能變成 performance accounting 的逃生門。

---

## 39. 一個簡化的 Non-Substitution 測試

對任務集 $X_T$，可進行三組 execution：

### A. 正常 physical backend

$$
y_A
=
\mathcal M(x;\mathcal P).
$$

### B. physical core 被消融

$$
y_B
=
\mathcal M(x;\varnothing).
$$

### C. physical core 被替換為錯誤 transfer function

$$
y_C
=
\mathcal M(x;\widetilde{\mathcal P}).
$$

如果：

$$
y_A
\approx
y_B
\approx
y_C
\approx
F_{\tau}(x)
$$

且系統仍宣稱 backend 為 $\mathcal P$，則存在高度 substitution 疑慮。

反之，如果 B、C 依模型失效或產生特定偏差，而 A 正常，則支持 physical causal attribution。

這直接承接 Paper 02 的 OPC-V3 / V4。

---

## 40. Failure Semantics：不要只有 Exception

本文建議 result status 至少區分：

$$
\begin{aligned}
&\text{VALID\_PHYSICAL},\\
&\text{VALID\_HYBRID},\\
&\text{VALID\_DIGITAL\_FALLBACK},\\
&\text{INVALID\_EVIDENCE},\\
&\text{BACKEND\_FAULT},\\
&\text{CALIBRATION\_FAIL},\\
&\text{TIMEOUT},\\
&\text{ABORTED}.
\end{aligned}
$$

這樣同一個數值答案：

$$
y=42
$$

不會掩蓋完全不同的 causal history。

結果真正應是：

$$
R
=
(y,s,E),
$$

其中 $s$ 是 execution status。

---

## 41. 數位 Fallback 是好功能，但必須改名

現場設備追求 availability，很自然會加入 digital fallback。

本文完全支持：

$$
\mathcal P
\xrightarrow{\text{fault}}
\mathcal D.
$$

但對外結果必須表示：

$$
\text{backend}=\mathcal D.
$$

因此：

$$
\boxed{
\text{availability}
\text{ 可以提高，}
\text{provenance}
\text{ 不可以被抹掉。}
}
$$

這會是 field appliance 很重要的產品原則。

---

## 42. Security 不是本篇主題，但權限架構已經替它留位置

本文的 authority separation 與 memory partition 同時具有 security 價值。

例如未來可以加入：

- signed backend manifest；
- signed FPGA bitstream；
- measured boot；
- TPM / secure element；
- hardware root of trust；
- per-plane privilege；
- secure update；
- remote attestation。

但本篇不要求這些全部存在，才叫 EPCA。

它們屬於：

$$
\text{deployment assurance}.
$$

本文首先要求的是：

$$
\text{causal and authority clarity}.
$$

---

## 43. 對公開研究裝置的最低建議

一台公開 EPCA demonstrator 若要具備合理可驗證性，本文建議至少：

1. 公開 compute boundary；
2. 公開 backend identity；
3. 保存 physical raw evidence；
4. 保存 firmware / bitstream / decoder version；
5. reference solver 不得寫入 physical result；
6. physical failure 不得 silent fallback；
7. 具至少一種 intervention / ablation test；
8. 若有 refinement，保存 refinement 前的 physical result；
9. 提供可重跑的 job manifest；
10. 清楚標示結果是 physical、hybrid 或 digital fallback。

這些要求通常比追求完整硬體安全更適合研究初期。

---

## 44. 不能保證什麼？

本文框架仍有明確邊界。

### 44.1 分 plane 不等於自動安全

若所有 plane 都由同一 privileged firmware 控制，形式分層不等於真正隔離。

### 44.2 Hardware isolation 也不能證明演算法宣告正確

工程權限分離需要和 Paper 02 的 causal test 搭配。

### 44.3 PREEMPT_RT 不保證任意硬體的 worst-case latency

驅動、bus、firmware、device 都可能造成 latency。

### 44.4 FPGA 不是天然可信

bitstream 本身可能執行未聲明計算。

### 44.5 reference isolation 不等於完全排除 side channel

高 threat model 仍需要 security architecture。

### 44.6 supervisor separation 不等於性能優勢

它提高可驗證性與工程可維護性，但不保證 throughput 或 energy efficiency。

---

## 45. 本篇主要命題

### 命題一

$$
\boxed{
\text{Supervisor Strength}
\neq
\text{Supervisor Authority}.
}
$$

### 命題二

Physical computing 不要求零數位輔助；真正需要禁止的是未聲明的 digital substitution。

### 命題三

Supervisor 應依時間尺度與權限拆成 application、real-time、fabric、management 與 verification planes。

### 命題四

每個 job 應先固定 Declared Compute Boundary，再執行 physical computation。

### 命題五

Reference solver 可以存在，但不得寫入 physical result acquisition path。

### 命題六

Digital refinement 可以存在，但 physical raw evidence 與 $y_{\mathcal P}$ 應先 commit。

### 命題七

Physical backend failure 可以觸發 digital fallback，但 backend identity 與 provenance 必須改變。

### 命題八

Supervisor assurance 與 physical-computation evidence 是兩個不同軸：

$$
Q_{\mathrm{EPCA}}
=
(\mathrm{OPC\mbox{-}V},\mathrm{ESA\mbox{-}S}).
$$

---

## 46. 從 Paper 02 到 Paper 03 的跨越

Paper 02 問：

> 如何證明 physical core 真的在算？

本篇則問：

> 如何設計一台夠強的 embedded computer 去控制 physical core，卻不破壞這項證明？

因此主線變成：

$$
\boxed{
\text{Verifiable Physical Core}
\rightarrow
\text{Authority-Separated Supervisor}
\rightarrow
\text{Deployable Hybrid Compute Appliance}.
}
$$

前兩篇主要建立 physical computation 的本體與證據條件。

從本篇開始，系列正式進入 appliance engineering。

---

## 47. 下一篇接口：Offline-First Field Appliance

有了 supervisor decomposition 之後，下一個問題就不再是「能不能控制」，而是：

> 如果這台設備真的被帶進工廠、戶外、實驗站、船上、礦區、維修現場或離線實驗室，它如何在沒有雲端、沒有穩定網路甚至 application service 部分失效時，仍然完成本地計算？

Paper 04 將處理：

$$
\boxed{
\text{Local Execution Closure}
+
\text{Offline-First Runtime}
+
\text{Real-Time Service}
+
\text{Transactional Update}
+
\text{Field Recovery}.
}
$$

具體包括：

- minimal embedded Linux；
- read-only / immutable base system；
- A/B system image；
- signed algorithm package；
- local algorithm repository；
- network optionality；
- disconnected operation；
- device identity；
- job queue；
- local evidence storage；
- update rollback；
- field-mode UI；
- remote management 但非 remote dependency。

因此 Paper 03 是 control-plane architecture，Paper 04 則是 deployment architecture。

---

## 48. 結論：不要追求「沒有數位電腦」，而要追求「沒有模糊責任」

Physical computing 很容易陷入一個錯誤浪漫化：彷彿只有完全不使用 CPU、MCU、FPGA 或 Linux，才算真正的新型計算。

實際工程恰好相反。

一個可以被使用、校正、驗證、更新與復原的 physical compute appliance，很可能需要非常成熟的數位控制系統。

問題不在於 supervisor 是否存在。

也不在於 supervisor 是否很強。

真正的問題是：

$$
\boxed{
\text{誰在計算什麼？}
}
$$

$$
\boxed{
\text{誰有權改寫什麼？}
}
$$

$$
\boxed{
\text{失效時誰可以替代誰？}
}
$$

$$
\boxed{
\text{替代發生時，設備是否如實改變身份？}
}
$$

以及：

$$
\boxed{
\text{結果是否留下足夠證據，使第三方能重新檢查這條因果鏈？}
}
$$

因此本文提出的 supervisor separation 並不是「把 Linux 放旁邊」這麼簡單。

它是一個 compute authority architecture。

它允許：

$$
\text{Linux}
+
\text{RTOS}
+
\text{FPGA}
+
\text{physical substrate}
$$

共同構成一台計算機，同時保留各自的責任邊界。

這使 EPCA 可以既是一台現代 embedded system，又不失去「physical core 真的在計算」這個系列最初想保留的核心。

---

## 參考文獻與工程資料

1. Tzarouchis, D. C., Edwards, B., & Engheta, N. (2025). *Programmable wave-based analog computing machine: a metastructure that designs metastructures*. Nature Communications, 16, 908. DOI: 10.1038/s41467-025-56019-1.
2. Hua, S., Divita, E., Yu, S., et al. (2025). *An integrated large-scale photonic accelerator with ultralow latency*. Nature, 640, 361-367. DOI: 10.1038/s41586-025-08786-6.
3. Sacchi, E., Zanetto, F., Martinez, A. I., et al. (2025). *Integrated electronic controller for dynamic self-configuration of photonic circuits*. Light: Science & Applications, 14, 348. DOI: 10.1038/s41377-025-01977-w.
4. Bogaerts, W., Perez, D., Capmany, J., Miller, D. A. B., Poon, J. K. S., Englund, D., Morichetti, F., & Melloni, A. (2020). *Programmable photonic circuits*. Nature, 586, 207-216. DOI: 10.1038/s41586-020-2764-0.
5. Linux Kernel Documentation. *Real-time preemption*. https://docs.kernel.org/core-api/real-time/
6. Linux Kernel Documentation. *Real-Time Kernel configuration*. https://docs.kernel.org/next/core-api/real-time/kernel-configuration.html
7. Linux Kernel Documentation. *Remote Processor Framework*. https://docs.kernel.org/staging/remoteproc.html
8. Linux Kernel Documentation. *Remote Processor Messaging (rpmsg) Framework*. https://docs.kernel.org/staging/rpmsg.html
9. Linux Kernel Documentation. *Watchdog Support*. https://docs.kernel.org/watchdog/index.html
10. OpenAMP Project. *Components and Capabilities*, v2026.04.0. https://openamp.readthedocs.io/en/v2026.04.0/protocol_details/components.html
11. AMD. *Versal Adaptive SoC System Software Developers Guide*, UG1304, 2026.1.
12. AMD. *Versal Adaptive SoC Technical Reference Manual*, AM011, Revision 1.9, 2026.

---

## 前置系列與本系列銜接

- 《跨尺度構成與動態約束域研究》v0.1：有效物理等價、構成復現、可達域與動態約束。
- 《認知功能體的物理實現與自然可觀測性研究》v0.1：存在、可觀測、可辨識與跨 substrate 功能實現。
- Paper 00：EPCA、Local Execution Closure、Physical-Core Non-Substitution、Supervisor Separation 與 Evidence-Bearing Result。
- Paper 01：Carrier-Generalized Abacus、position coding、mode coding、relation coding 與 dynamical geometry。
- Paper 02：OPC-V0 至 OPC-V5、causal intervention、ablation、independent challenge 與 falsifiable physical evidence。

本篇將 Paper 02 的驗證要求轉為具體 embedded architecture：不是壓低 supervisor 能力，而是把 capability、authority、result path、reference path、memory、fault domain 與 evidence path 分開。這為後續 offline-first field appliance、多 substrate backplane、mixed-precision refinement 與 AI orchestration 提供一致的執行邊界。
