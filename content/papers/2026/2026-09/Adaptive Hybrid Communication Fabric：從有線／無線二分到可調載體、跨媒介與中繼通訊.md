---
title: "Adaptive Hybrid Communication Fabric：從有線／無線二分到可調載體、跨媒介與中繼通訊"
subtitle: "Series A-05｜Adaptive Hybrid Communication Fabric: Carrier-Agile, Cross-Medium, Multipath, and Relay-Aware Communication"
author: "Neo.K（EVEMISS / EveMissLab）"
ai_collaboration: "Aletheia（GPT-5.6 Sol）"
version: "0.1"
status: "Research Draft / Canonical Source"
date: "2026-08-24"
language: "zh-TW"
series: "Series A｜AI-Native Communication Continuum"
series_number: "A-05"
document_type: "Research Paper"
canonical_source: true
encoding: "UTF-8"
---

# Adaptive Hybrid Communication Fabric：從有線／無線二分到可調載體、跨媒介與中繼通訊

## Series A-05｜Adaptive Hybrid Communication Fabric: Carrier-Agile, Cross-Medium, Multipath, and Relay-Aware Communication

**作者：** Neo.K（EVEMISS / EveMissLab）  
**AI 協作：** Aletheia（GPT-5.6 Sol）  
**版本：** v0.1  
**日期：** 2026-08-24  
**文件狀態：** Research Draft / Canonical Source  

---

# 摘要

Series A-01 至 A-04 已依序建立 AI-Native Communication Continuum、Persistent Communication State、Multimodal-Native Projection 與 AI Communication Runtime。前三篇處理「通訊世界如何持續存在」、第四篇處理「AI 如何在授權邊界內規劃、選擇 Channel、Agent、Tool 與 Action」。本文處理下一個更底層、但直接決定 Continuum 是否真正能跨移動環境持續存在的問題：**當終端同時具有 Wi-Fi、行動網路、衛星、固定網路、局部中繼、光纖、不同無線頻帶與未來可重構物理介面時，系統是否仍應把每一種通訊方式視為彼此割裂的獨立世界？**

本文提出 **Adaptive Hybrid Communication Fabric（AHCF）**。AHCF 不主張「有線」與「無線」工程名詞失效，也不主張所有導線將被無線取代；它主張的是：**wired / wireless 不應再作為 AI-Native Continuum 最高層的第一分類。** 在更一般的架構中，一條可用通訊路徑應被描述為一組可觀察、可選擇、可組合的 propagation / transport / relay capabilities。銅線、光纖、自由空間 RF、毫米波、THz、衛星、表面波、局部 Wi-Fi、行動網路與其他未來媒介，可以在不同層級形成跨媒介路徑，而上層 Communication State 不應被綁定於其中任一單一路徑。

本文以 Communication Fabric Graph 形式化底層連通性：

$$
\boxed{
G_F(t)
=
(V_F,E_F)
}
$$

其中 node 可代表 endpoint、gateway、access point、base station、satellite、relay、transducer、edge compute、fibre endpoint 或可重構物理介面；edge 則不以「wired / wireless」單一標籤定義，而使用 Path Capability Descriptor：

$$
\boxed{
e_i(t)
=
(
m_i,
f_i,
B_i,
L_i,
J_i,
E_i,
R_i,
S_i,
C_i,
Q_i
)
}
$$

其中分別表示 propagation / medium class、frequency or carrier profile、available bandwidth、latency、jitter、energy cost、reliability、security / trust properties、monetary or resource cost 與 policy / quality constraints。對同一 Communication Flow $q$，Fabric Controller 不應只選一條「最快網路」，而是在應用需求與治理條件下求得路徑或多路徑集合：

$$
\boxed{
P_q^*
=
\arg\min_{P\in\mathcal P_q}
J(P\mid\Theta_q)
}
$$

subject to：

$$
Security(P)\ge\tau_S,
$$

$$
Reliability(P)\ge\tau_R,
$$

$$
Latency(P)\le L_{\max},
$$

以及當前使用者、裝置、企業與地區 policy 所要求的其他限制。

AHCF 的核心不是自行發明新的 PHY，而是把已經存在的多路徑、多接入、中繼與跨媒介技術置於同一 architecture contract 下。現有工程已提供明確錨點：Multipath TCP 可在同一連線中同時使用多條 path；3GPP ATSSS 已在 5G 系統中處理 Access Traffic Steering, Switching and Splitting；Release 18 包含 Mobile IAB 與 NTN enhancement；光子整合研究已展示 fibre–wireless shared-bandwidth architecture 與 fibre–wireless–fibre transparent relaying；2026 年 programmable topological metasurface 研究更展示同一可程式電磁平台在 surface-wave guidance 與 radiative beamforming 狀態之間切換。IEEE Information Theory Society 的 Electromagnetic Information Theory（EIT）研究線則進一步把 electromagnetic physics、channel、near-field、RIS、holographic MIMO 與 information theory 放進同一分析框架。這些工作不等同 AHCF，但共同支持一個重要背景：

$$
\boxed{
\text{Communication path and physical-wave behavior are increasingly software-addressable, composable, and reconfigurable.}
}
$$

本文同時嚴格區分三個證據層級。**S0** 為已標準化／已部署能力，例如 MPTCP、5G multi-access、IAB、NTN；**S1** 為已存在實驗或前沿研究，例如 THz fibre–wireless transparent relay、programmable metasurface、EIT-based physical channel modeling；**S2** 則為 EVEMISS 目前仍屬猜想／研究綱領的 FAL-MCI 與 SPFC，即由高階 intent 或 semantic object 經 carrier / backend selection、relay / controller network，再映射至物理控制向量的可能架構。本文允許三層形成研究接口，但不得把 S1 或 S2 描述成已完成的通用商用系統。

對 FARHP / SPAL 的定位亦採保守邊界：FARHP 已處理聲學中的基頻錨定相對諧波相位與可編碼表示；SPAL 研究頻率、相位、振幅、時間與空間聲場是否可以成為 AI-native physical-wave language substrate。這些研究可以啟發 AHCF 對 carrier / phase / waveform state 的高階描述，但：

$$
\boxed{
\text{Modulation / Waveform Coordinate}
\neq
\text{Semantic Meaning}
}
$$

且：

$$
\boxed{
\text{FARHP / SPAL}
\neq
\text{General Network Transport Protocol}.
}
$$

A-05 的工程核心因此不是「用新語言取代 TCP/IP」，而是建立一個 **transport-independent, carrier-aware, relay-aware, policy-aware communication fabric contract**，讓 A-02 的 Persistent Communication State 與 A-04 的 Runtime Decision 在底層網路切換時維持連續。當 Wi-Fi 失效、行動網路變弱、衛星可用、車輛跨基地台、飛機切換連線，或未來環境提供新的 relay / physical backend 時，上層應盡可能滿足：

$$
\boxed{
\Delta Path
\not\Rightarrow
\operatorname{Reset}(CommunicationState).
}
$$

本文最終提出：下一代 AI-native communication architecture 不應以「App 選網路」為中心，而應形成：

$$
\boxed{
\text{Communication Intent}
\rightarrow
\text{Flow Requirements}
\rightarrow
\text{Fabric Policy}
\rightarrow
\text{Path / Multipath Selection}
\rightarrow
\text{Relay / Carrier Execution}
\rightarrow
\text{Continuity Evidence}
}
$$

AHCF 為 A-06 的 Personal Communication Sovereignty 建立必要前提：只有當使用者的 identity、state 與 authority 不等同於單一網路 Provider，個人通訊主權才真正具有跨網路、跨終端與跨載體的可攜性。

**關鍵詞：** Adaptive Hybrid Communication Fabric；Multipath；ATSSS；MPTCP；IAB；NTN；Satellite；Fibre–Wireless；Transparent Relay；THz；Electromagnetic Information Theory；RIS；Programmable Metasurface；Carrier Agility；FAL-MCI；SPFC；FARHP；SPAL；AI-Native Communication Continuum；EVEMISS

---

# Abstract

This paper proposes the Adaptive Hybrid Communication Fabric (AHCF), the connectivity layer beneath the AI-Native Communication Continuum developed in Series A-01 through A-04. AHCF does not claim that the engineering distinction between wired and wireless communication is obsolete, nor does it predict that wireless links will replace all guided media. Instead, it argues that wired versus wireless should no longer serve as the highest-level architectural partition for a persistent AI-native communication system.

A communication path is modeled as a composable capability rather than as a fixed provider-specific pipe. Endpoints, gateways, fibre links, radio access networks, Wi-Fi, satellite links, mobile relays, edge nodes, transducers and future programmable physical interfaces are represented in a time-varying Communication Fabric Graph. Each edge carries a Path Capability Descriptor that includes medium or propagation class, carrier profile, bandwidth, latency, jitter, energy cost, reliability, security and trust properties, cost, and policy constraints. A Fabric Controller selects one or more admissible paths according to flow requirements rather than according to a single global ranking of networks.

The architecture is grounded in three evidence levels. S0 contains standardized or deployed mechanisms such as Multipath TCP, 3GPP ATSSS, Integrated Access and Backhaul, and Non-Terrestrial Network support. S1 contains experimental or frontier research, including integrated fibre–wireless transparent relaying, terahertz communication, programmable metasurfaces and Electromagnetic Information Theory. S2 contains EVEMISS research conjectures such as Frequency-Agile Language / Machine-Capability Inheritance and Semantic-to-Physical Field Compilation. The three levels may be connected as a research program, but S1 and S2 are not presented as mature universal infrastructure.

The paper also defines a strict boundary for FARHP and SPAL. Frequency, phase, amplitude and waveform state can be physically meaningful communication coordinates and may serve as future AI-native representation substrates, but modulation is not equivalent to semantics and FARHP/SPAL are not general replacements for network transport protocols.

AHCF therefore focuses on transport-independent continuity: changes in access path, carrier, relay topology or provider should not automatically reset persistent communication state. The proposed architecture connects application flow requirements, fabric policy, path or multipath selection, relay execution, observability, degradation handling and continuity evidence. It provides the network substrate for the subsequent Personal Communication Sovereignty paper in Series A-06.

---

# 0. 研究問題：為什麼「有線／無線」不應再是最高層分類？

傳統通訊介紹常先分成：

$$
\text{Communication}
=
\text{Wired}
\cup
\text{Wireless}.
$$

這個分類在教學、部署與硬體選型上仍有價值。例如：

- optical fibre 與 free-space RF 的 path loss 完全不同；
- copper trace 與 satellite link 的 latency、energy、antenna requirement 不可混同；
- wired link 可能具有更穩定的 shielding、physical access control 與容量；
- wireless link 則具有 mobility、broadcast medium、interference 與 spectrum regulation 等特殊問題。

因此本文不提出：

$$
\text{Wired}=\text{Wireless}.
$$

本文真正提出的是：對上層 AI-Native Communication Continuum 而言，**這個二分不應成為 canonical state 與 application logic 的第一依賴。**

如果使用者在桌機透過 Ethernet 進行會議，接著拿起手機切 Wi-Fi，之後進入汽車使用 5G，再進入訊號死角切到 satellite fallback，理想的上層語義不是四個完全不同的工作世界：

```text
Ethernet App State
Wi-Fi App State
5G App State
Satellite App State
```

而應是：

```text
Persistent Communication State
        ↓
Flow Requirements
        ↓
Adaptive Communication Fabric
        ↓
Current Path Set
```

因此：

$$
\boxed{
\text{Connectivity Substrate}
\neq
\text{Communication Identity}.
}
$$

以及：

$$
\boxed{
\text{Path Change}
\neq
\text{Conversation Reset}.
}
$$

---

# 1. 從媒介分類改為 Capability Classification

若不以 wired / wireless 為第一層，可以改以更一般的 capability 維度描述通訊 edge。

本文建議至少分成下列 propagation / medium families：

1. guided electrical；
2. guided optical；
3. radiative RF / microwave / mmWave / THz；
4. satellite / non-terrestrial access；
5. surface-wave / near-field / structured electromagnetic paths；
6. acoustic / ultrasonic paths；
7. free-space optical or other optical wireless paths；
8. virtual / tunneled transport overlays；
9. future transduced cross-domain paths。

這些分類不是互斥到只能選一個 label。

例如 satellite access 仍然可以使用 RF 或 optical carrier；它同時具有：

- non-terrestrial topology；
- radiative propagation；
- specific carrier bands；
- handover / beam / gateway constraints。

因此一條 edge 最好不是：

```text
edge.type = wireless
```

而是能力向量。

定義：

$$
\boxed{
\Gamma(e,t)
=
(
M,
P,
F,
B,
L,
J,
E,
R,
K,
C,
G
)
}
$$

其中：

- $M$：medium / substrate；
- $P$：propagation mode；
- $F$：carrier / frequency profile；
- $B$：bandwidth / throughput envelope；
- $L$：latency；
- $J$：jitter；
- $E$：energy / thermal cost；
- $R$：reliability / loss / availability；
- $K$：security / trust / cryptographic properties；
- $C$：financial / spectrum / resource cost；
- $G$：governance / jurisdiction / policy conditions。

這樣 wired / wireless 仍可保留為 derived label：

$$
Wired(e)=g(\Gamma(e)),
$$

$$
Wireless(e)=h(\Gamma(e)),
$$

但上層 route optimizer 不必只能在兩個大盒子中選擇。

---

# 2. Communication Fabric Graph

定義時間變動的 Fabric Graph：

$$
\boxed{
G_F(t)
=
(V_F(t),E_F(t)).
}
$$

## 2.1 Node

node 可包括：

- user device；
- vehicle gateway；
- cabin compute node；
- Wi-Fi access point；
- cellular base station；
- mobile IAB node；
- satellite；
- satellite gateway；
- fibre endpoint；
- edge data center；
- cloud ingress；
- relay；
- transducer；
- programmable metasurface controller；
- enterprise secure gateway；
- home router；
- peer device。

因此：

$$
V_F
\neq
\text{only routers}.
$$

它是一個 logical communication capability graph。

## 2.2 Edge

每條 edge：

$$
e=(v_i,v_j,\Gamma_e).
$$

edge 可瞬時加入或消失：

$$
E_F(t)
\neq
E_F(t+1).
$$

例如移動車輛：

$$
E_{5G,A}
\rightarrow
E_{5G,B}
\rightarrow
E_{SAT}
\rightarrow
E_{WiFi}.
$$

理想 Continuum 中，上層 PCS 不應跟著重新建立。

---

# 3. 三層證據地位

A-05 必須避免將不同成熟度的技術混成一句「未來通訊已經完成」。

因此定義：

## S0｜Standardized / Deployed Capability

包括但不限於：

- TCP/IP、QUIC 等既有 transport substrate；
- Multipath TCP；
- 3GPP multi-access / ATSSS；
- Integrated Access and Backhaul；
- Release 18 Mobile IAB；
- 5G Non-Terrestrial Network enhancement；
- Wi-Fi / cellular handoff 與既有 mobility mechanisms；
- satellite broadband / direct-to-device 的現代部署形態。

這一層可以直接進近期工程 roadmap。

## S1｜Experimental / Frontier Research

例如：

- ultra-wideband fibre–wireless integration；
- THz transparent relay；
- programmable metasurface；
- topological surface-wave / radiative state switching；
- EIT、near-field、holographic MIMO；
- cell-free / distributed radio architectures；
- advanced optical wireless / photonic-radio integration。

這一層可以作 research adapter / simulation target，不應假設當前普遍可用。

## S2｜Architecture Conjecture / Research Program

EVEMISS 目前包括：

- FAL-MCI；
- SPFC；
- carrier-agile semantic-to-physical mapping；
- AI 依 semantic / effect intent 選擇 physical backend；
- future physical-field compiler。

其地位是：

$$
\boxed{
S2
=
\text{Conjecture / Architecture Hypothesis}
}
$$

不是：

$$
S2=\text{Established Network Standard}.
$$

---

# 4. Multi-Access 已經證明「單一介面」不是自然限制

MPTCP 的基本精神是：同一 transport session 可以同時利用多個 network path。

抽象表示：

$$
\boxed{
Connection
\rightarrow
\{p_1,p_2,\ldots,p_n\}.
}
$$

而不是：

$$
Connection\rightarrow p_1\text{ forever}.
$$

對 AI-Native Continuum 更重要的是，這使「path identity」與「communication identity」有機會分離。

但 A-05 不把 MPTCP 當作唯一 implementation。

其功能角色是證明：

$$
\boxed{
\text{Multipath Session}
}
$$

在成熟 Internet stack 中已有標準化前例。

此外，Multipath QUIC 仍屬演進中的標準工作；截至 2026 年初可見 IETF multipath QUIC draft 明確討論同一 QUIC connection 同時管理多條 path。A-05 因此將 QUIC multipath 視為可追蹤的 evolution point，而不把 Internet-Draft 說成 final RFC。

---

# 5. 3GPP ATSSS：Access 不再只能單一路徑選擇

ATSSS 的名稱本身已經指出三個行為：

- Steering；
- Switching；
- Splitting。

概念上：

$$
\boxed{
Traffic
\rightarrow
\text{Steer / Switch / Split across accesses}.
}
$$

這與 A-05 的 Fabric 層非常接近，但作用範圍不同。

AHCF 不是 ATSSS 的重新命名。

ATSSS 是 3GPP multi-access 架構中的標準能力；AHCF 是更上層、跨 transport / provider / physical backend 的 architecture contract。

可以寫：

$$
\boxed{
ATSSS
\subset
\mathcal C_{AHCF}^{available}.
}
$$

但不能寫：

$$
ATSSS=AHCF.
$$

Release 18 的規格工作仍持續處理 ATSSS capability、EPC / 5GC access 組合與多接入行為，顯示 multi-access 本身不是邊緣概念，而是現代 5G 系統架構的重要方向。

---

# 6. IAB 與 Mobile IAB：中繼不再只是固定基礎設施

Integrated Access and Backhaul（IAB）的核心意義之一，是允許 radio access 與 backhaul 在同一 NR 生態中被整合。

Release 18 的 Mobile IAB 進一步使 mobile relay / backhaul node 成為標準化研究與規格能力。

因此 relay topology 可以具有：

$$
R(t)=\{r_1(t),r_2(t),\ldots,r_n(t)\}.
$$

路徑可能為：

$$
UE
\rightarrow
MobileRelay
\rightarrow
Donor
\rightarrow
Core.
$$

對未來車隊、巴士、列車、船舶、臨時基地與災害環境而言，這很重要：

$$
\boxed{
\text{Infrastructure}
\not\Rightarrow
\text{all nodes fixed in space}.
}
$$

A-05 因此將 relay mobility 作為 Fabric Graph 的第一級能力，而不是例外情況。

---

# 7. NTN：地面網路不是唯一空間域

5G Non-Terrestrial Networks 將 satellite / aerial topology 納入標準系統演進。

對 AHCF 而言，最重要的不是宣稱：

> Satellite 會取代 terrestrial network。

而是：

$$
\boxed{
\text{Terrestrial Path}
\cup
\text{Non-Terrestrial Path}
}
$$

可以進入同一 Flow Policy。

例如：

$$
P_q(t)
=
\{
5G,
WiFi,
Satellite
\}.
$$

當使用者進入偏遠道路：

$$
Availability(5G)\downarrow,
$$

Fabric 可以依服務需求切換到：

$$
SatelliteFallback.
$$

但若 satellite link 只有較低頻寬或較高成本，Runtime 應同時觸發 A-03 的 modality degradation：

$$
4KVideo
\rightarrow
LowRateVideo
\rightarrow
Audio
\rightarrow
Text.
$$

所以 AHCF 與 Multimodal Projection 是雙向耦合，不只是「找到任何能上網的路」。

---

# 8. Fibre–Wireless Transparent Relay：跨媒介不是純概念

2026 年 Nature 發表的 integrated photonics fibre–wireless system 展示 shared-bandwidth infrastructure，並實驗達成高資料率 fibre 與 THz wireless link；該研究也明確討論：

$$
\text{Fibre}
\rightarrow
\text{Wireless}
\rightarrow
\text{Fibre}
$$

的 transparent relaying。

這件事對 A-05 的理論意義大於具體速率紀錄。

它說明：

$$
\boxed{
\text{A logical signal path can cross physical-medium boundaries.}
}
$$

因此上層不應必然把 medium transition 視為 communication identity transition。

注意：這不表示當前 Internet 可任意透明跨所有 medium，也不表示所有轉導零成本。

每個 conversion 都具有：

$$
Cost_{conv},
$$

$$
Noise_{conv},
$$

$$
Latency_{conv},
$$

$$
Power_{conv}.
$$

所以 path optimizer 必須把 transduction 加入 edge cost。

---

# 9. Programmable Metasurface：傳播環境本身開始可程式化

傳統網路常把 propagation environment 視為外部條件：

$$
Environment
\rightarrow
Channel.
$$

RIS / programmable metasurface 的重要性在於，一部分環境響應開始進入可控制域：

$$
Controller
\rightarrow
SurfaceState
\rightarrow
ChannelResponse.
$$

2026 年的 programmable topological metasurface 實驗展示同一平台可以在兩種不同物理機制之間重構：

1. topologically protected surface-wave guidance；
2. radiative directional beamforming。

抽象上：

$$
\boxed{
Mode_{surface}
\leftrightarrow
Mode_{radiative}.
}
$$

這不表示「有線與無線已完全合一」。

它更精確地支持：

> physical propagation mode 可能逐步成為 software-addressable state。

因此 AHCF 的 future interface 應允許：

```text
PhysicalPathController
```

而不是把所有 PHY 假設成永遠不可重構的黑盒。

---

# 10. Electromagnetic Information Theory：資訊理論重新接回物理場

Shannon-style abstraction 的力量之一，是可以把大量底層物理細節抽象成 channel。

但當：

- extremely large arrays；
- holographic MIMO；
- RIS；
- near-field；
- continuous aperture；
- complex wave manipulation；

成為研究重點時，單純把 channel 當固定矩陣可能不足以描述全部可用 degrees of freedom。

EIT 的研究方向正是把：

$$
\text{Electromagnetic Physics}
+
\text{Information Theory}
$$

重新放進同一分析框架。

對 A-05 而言，EIT 是重要的學術相鄰域，但 AHCF 不主張自己建立新的 electromagnetic information theory。

其關係是：

$$
\boxed{
EIT
\rightarrow
\text{physical capability model input}
\rightarrow
AHCF.
}
$$

未來如果 physical path capability 可以由更嚴謹的 field model 估計，AHCF 的路由器便不必只依 RSSI / throughput 等簡化指標。

---

# 11. Path Capability Descriptor

本文提出最小 descriptor：

$$
\boxed{
D_e
=
(
Identity,
Medium,
Propagation,
Carrier,
Capacity,
Latency,
Loss,
Mobility,
Energy,
Security,
Cost,
Policy,
Evidence
).
}
$$

## 11.1 Identity

包括：

- path ID；
- provider ID；
- interface ID；
- relay chain ID；
- epoch / version。

## 11.2 Medium / Propagation

例如：

```text
guided-electrical
guided-optical
radiative-rf
radiative-thz
satellite-rf
surface-wave
free-space-optical
acoustic
virtual-tunnel
```

## 11.3 Carrier

可以包含：

$$
F=
(
f_c,
\Delta f,
modulation,
phaseProfile,
beamProfile
).
$$

但對一般 Internet path，可以只暴露必要抽象，不要求每個 App 理解 PHY。

## 11.4 Capacity

$$
Capacity_e(t)
$$

應視為時間變量。

## 11.5 Mobility

例如：

```text
fixed
handover-capable
mobile-relay
non-terrestrial-moving
opportunistic
```

## 11.6 Security

不能只有：

```text
secure = true
```

而應至少區分：

- link encryption；
- end-to-end encryption capability；
- provider visibility；
- trust domain；
- jurisdiction；
- credential binding；
- known downgrade risk。

---

# 12. Flow Requirement Contract

上層 ACR 不應直接說：

> 用 Wi-Fi。

而應先表達需求：

$$
\boxed{
\Theta_q
=
(
B_q,
L_q,
J_q,
R_q,
S_q,
E_q,
C_q,
M_q
).
}
$$

例如語音通話：

$$
L_q\le L_{voice},
$$

$$
J_q\le J_{voice},
$$

可靠度需高於某門檻。

而背景文件同步：

$$
Latency\text{ sensitivity}\downarrow,
$$

但：

$$
Integrity\text{ requirement}\uparrow.
$$

因此同一裝置可以同時：

$$
q_{voice}\rightarrow P_1,
$$

$$
q_{sync}\rightarrow P_2,
$$

$$
q_{video}\rightarrow P_1\cup P_3.
$$

這比「整台手機現在走哪一個網路」更細。

---

# 13. Routing Objective 不應只有 Throughput

定義多目標 cost：

$$
\boxed{
J(P)
=
\lambda_L L(P)
+
\lambda_J J(P)
+
\lambda_E E(P)
+
\lambda_C C(P)
+
\lambda_R \bigl(1-R(P)\bigr)
+
\lambda_S Risk(P)
+
\lambda_G GovPenalty(P).
}
$$

權重：

$$
\lambda_i
$$

由 flow class、user policy、enterprise policy、battery state、surface state 與 emergency state 決定。

對安全關鍵 flow，不宜只靠 soft cost。

應改用 hard constraints：

$$
Security(P)\ge\tau_S,
$$

$$
Trust(P)\ge\tau_T.
$$

這延續 A-04：

$$
Capability\neq Permission.
$$

一條 path 即使 technically reachable，也不代表 allowed。

---

# 14. Single-Path、Failover 與 Multipath

AHCF 至少支援三種 policy。

## 14.1 Single Best Path

$$
P_q=\{p^*\}.
$$

適合：

- 成本敏感；
- 能耗敏感；
- 簡單背景流量。

## 14.2 Failover

$$
p_1
\xrightarrow{failure}
p_2.
$$

要求：

- state 不丟失；
- session resume；
- no duplicate side effect；
- application replay 安全。

## 14.3 Concurrent Multipath

$$
P_q
=
\{p_1,p_2,\ldots,p_k\}.
$$

可做：

- aggregation；
- redundancy；
- latency racing；
- traffic class splitting；
- control/data plane separation。

但 multipath 會引入：

- reordering；
- path asymmetry；
- different MTU；
- trust differences；
- duplicated traffic cost；
- congestion coupling。

因此：

$$
\boxed{
\text{More paths}
\not\Rightarrow
\text{better communication}.
}
$$

---

# 15. Path Change 與 A-02 Persistent State

A-02 已定義 persistent state 不應依單一 Surface 或 Provider 存在。

A-05 加上：

$$
\boxed{
\Delta NetworkPath
\not\Rightarrow
\Delta CanonicalState.
}
$$

但這不表示 zero-loss handoff 必然可達。

定義 Network Continuity Loss：

$$
\boxed{
L_{NC}
=
\eta_1 L_{session}
+
\eta_2 L_{media}
+
\eta_3 L_{ordering}
+
\eta_4 L_{security}
+
\eta_5 L_{context}.
}
$$

其中：

- $L_{session}$：transport / session resume loss；
- $L_{media}$：media interruption；
- $L_{ordering}$：message ordering damage；
- $L_{security}$：security downgrade；
- $L_{context}$：上層 state reconstruction loss。

目標：

$$
L_{NC}\rightarrow0,
$$

而不是宣稱：

$$
L_{NC}=0
$$

對所有物理環境成立。

---

# 16. Transport Session 不是 Communication Session

這是 A-05 必須明確寫下的層級差異。

$$
\boxed{
TransportSession
\neq
CommunicationSession.
}
$$

一個 CommunicationSession 可以跨越：

$$
TCP_1
\rightarrow
QUIC_2
\rightarrow
WebRTC_3
\rightarrow
StoreAndForward_4.
$$

同樣：

$$
\boxed{
IPAddress
\neq
ActorIdentity.
}
$$

因此 Continuum Identity 應存在更高層。

A-05 不要求底層永遠 seamless；它要求上層具有 resume / reconstruct / degrade / retry 的明確契約。

---

# 17. Relay Chain

定義 relay chain：

$$
\boxed{
\mathcal R(P)
=
(r_1,r_2,\ldots,r_n).
}
$$

每個 relay 具有：

$$
D_{r_i}
=
(
Capability,
Trust,
Latency,
Cost,
Jurisdiction,
Transform
).
$$

Transform 可能是：

- packet forwarding；
- protocol gateway；
- NAT；
- media relay；
- transcoding；
- fibre-to-radio conversion；
- radio-to-optical conversion；
- frequency conversion；
- signal amplification；
- store-and-forward；
- future physical transduction。

因此 relay 不是只有：

> 中間幫忙傳封包的機器。

而是一個：

$$
\boxed{
\text{Path Transformation Node}.
}
$$

但 transform 越多，越需要 evidence 與 trust metadata。

---

# 18. Conversion Ledger

當 path 跨媒介或轉碼時，系統應留下 Conversion Ledger：

```text
flow_id
path_epoch
source_medium
target_medium
relay_id
transformation_type
input_integrity
output_integrity
latency_added
security_boundary
policy_decision
```

定義 cumulative conversion risk：

$$
\boxed{
Risk_{conv}(P)
=
1-
\prod_{i=1}^{n}
(1-r_i).
}
$$

此式只是簡化工程指標，不代表不同風險必然獨立。

它的目的，是強迫 architecture 記住：

$$
\text{Transparent to user}
\not\Rightarrow
\text{physically or security-wise free}.
$$

---

# 19. Security：多路徑不能變成最低安全路徑攻擊

如果：

$$
P=\{p_{secure},p_{weak}\},
$$

錯誤設計可能使整體安全性退化到：

$$
Security(P)
\approx
\min Security(p_i).
$$

因此多路徑策略必須指定：

- 哪些資料可 split；
- 哪些資料只可走 E2EE；
- 哪些 path 可承載 key material；
- metadata 是否可見；
- relay 是否可解密；
- 是否允許 lawful / enterprise gateway termination；
- downgrade 時是否必須停止而不是切換。

核心不變量：

$$
\boxed{
ConnectivityFallback
\not\Rightarrow
SecurityFallback.
}
$$

若安全條件無法滿足，可以：

$$
Execute
\rightarrow
Defer
$$

或：

$$
Execute
\rightarrow
Refuse.
$$

這與 A-04 的 policy state machine 一致。

---

# 20. End-to-End Encryption 應高於 Access Path

理想狀態：

$$
\boxed{
E2EEContext
\not\equiv
AccessNetwork.
}
$$

這樣：

$$
WiFi
\rightarrow
5G
\rightarrow
Satellite
$$

不必重新定義 conversation security identity。

但仍需要注意：

- traffic analysis；
- provider metadata；
- DNS / name resolution；
- certificate / key continuity；
- enterprise interception policy；
- lawful requirements；
- geographic jurisdiction changes。

所以 A-06 將進一步處理 sovereignty，而 A-05 只建立 Path Security Descriptor。

---

# 21. Connectivity Orchestrator

AHCF 的核心 runtime 可寫為：

$$
\boxed{
\mathfrak F:
(
G_F,
\Theta_q,
\Pi_{net},
\Omega_t
)
\rightarrow
P_q^*.
}
$$

其中：

- $G_F$：Fabric Graph；
- $\Theta_q$：Flow Requirement；
- $\Pi_{net}$：Network / security policy；
- $\Omega_t$：observed environment；
- $P_q^*$：selected path set。

它不是大語言模型本身。

可由：

- deterministic policy；
- congestion controller；
- routing algorithm；
- reinforcement learning；
- predictive model；
- AI planner；
- hybrid controller；

共同實現。

A-04 的 AI Runtime 可以提出：

```text
need low-latency secure voice + background document sync
```

但不應由 LLM 每個 packet 做 route selection。

---

# 22. Control Plane、Data Plane 與 Evidence Plane

AHCF 建議三平面：

## 22.1 Fabric Control Plane

負責：

- path discovery；
- capability registry；
- policy；
- route selection；
- handover decision；
- multipath strategy；
- relay negotiation。

## 22.2 Data Plane

負責：

- actual packet / frame / media transport；
- encryption；
- congestion control；
- retransmission；
- forward / relay；
- conversion execution。

## 22.3 Evidence / Observation Plane

負責：

- path telemetry；
- handover record；
- quality metrics；
- provider error；
- conversion record；
- policy decision；
- security downgrade detection；
- continuity loss report。

這延續 EVEMISS 既有 Control / Runtime / Evidence 分層，而不是另做一套孤立網路治理。

---

# 23. Network Observation State

定義：

$$
\boxed{
\Omega_t
=
(
Interfaces,
Paths,
Signal,
Capacity,
Latency,
Loss,
Energy,
Cost,
Security,
LocationClass,
Mobility
).
}
$$

注意 LocationClass 不等於保存精確定位。

可只表示：

```text
home
enterprise
vehicle
public
remote-road
airborne
unknown
```

並由 privacy policy 決定是否保留更精細資訊。

---

# 24. Predictive Handover

AI / ML 可以在上層協助預測：

$$
Pr(
PathFailure_{t+\Delta t}
\mid
\Omega_{0:t}
).
$$

例如車輛接近：

- tunnel；
- known dead zone；
- coverage boundary；
- congested event area。

系統可以預先：

1. 建立 secondary path；
2. warm up satellite link；
3. 降低 video bitrate；
4. sync critical state；
5. checkpoint current task；
6. 延後非必要 large transfer。

因此 handover 可以由 reactive：

$$
Failure\rightarrow Recovery
$$

提升成 predictive：

$$
RiskPrediction\rightarrow Preparation\rightarrow Handover.
$$

這是 AI 對 Communication Fabric 最現實的價值之一。

---

# 25. Degradation Ladder

不是所有 path 都能維持同一 media quality。

因此為每個 intent 定義：

$$
\boxed{
\mathcal D_q
=
(d_0,d_1,\ldots,d_n).
}
$$

例如會議：

```text
4K video
→ HD video
→ low-frame video
→ audio
→ live transcript
→ asynchronous message
```

要求：

$$
Semantics(d_{i+1})
\approx
Semantics(d_i)
$$

但 media fidelity 可以下降。

A-03 的 Projection Engine 與 A-05 的 Fabric Controller 必須協作：

$$
NetworkState
\rightarrow
ProjectionPolicy.
$$

反過來：

$$
UserIntent
\rightarrow
FlowRequirement.
$$

---

# 26. Vehicle Scenario

對我們本系列後續 Series B 特別重要的是車輛環境。

假設車內具有：

$$
\mathcal I
=
\{
5G_A,
5G_B,
WiFi,
Satellite
\}.
$$

Connectivity Orchestrator 可以建立：

$$
P_{control}=5G_A,
$$

$$
P_{video}=5G_A+5G_B,
$$

$$
P_{sync}=WiFi\text{ when available},
$$

$$
P_{emergency}=5G\lor Satellite.
$$

進入死角：

$$
Availability(5G_A,5G_B)\rightarrow0.
$$

不代表：

$$
CommunicationState\rightarrow0.
$$

而是：

$$
SurfaceProjection
\rightarrow
ReducedBandwidthMode.
$$

這就是「交通時空持續存在」在網路層的真正工程需求。

---

# 27. Aircraft Scenario

飛行環境可能具有：

- cabin Wi-Fi；
- satellite backhaul；
- local aircraft network；
- cached edge service；
- restricted services；
- variable latency / coverage。

對上層使用者：

```text
Office → Airport → Aircraft → Ground → Hotel
```

理想是：

$$
PCS_{office}
\rightarrow
PCS_{aircraft}
\rightarrow
PCS_{hotel}
$$

保持 logical continuity。

但 Fabric 必須承認：

$$
PhysicalConnectivity
$$

可能斷續。

因此：

$$
\boxed{
\text{Continuity}
\neq
\text{Always-online assumption}.
}
$$

真正 robust 的 Continuum 必須有 offline / delayed / store-and-forward mode。

---

# 28. Store-and-Forward 也是 Fabric Capability

現代「always online」思維常忽略：斷網時最好的 path 可能是：

$$
\text{Local Queue}
\rightarrow
\text{Future Network}.
$$

因此：

$$
PathType
\supset
StoreAndForward.
$$

對非即時任務：

$$
q_{email},
q_{document},
q_{artifactUpload}
$$

可以先 commit local state，再於網路恢復後傳送。

這比讓 UI 顯示永久 loading 更符合 Persistent Communication State。

---

# 29. Provider Abstraction

現有 Consumer Core 已有 Provider Broker。

A-05 將其擴張為兩層：

```text
Service Provider Adapter
Network / Connectivity Provider Adapter
```

前者例如：

- speech provider；
- email provider；
- phone provider；
- AI provider。

後者例如：

- cellular；
- Wi-Fi managed network；
- satellite；
- enterprise network；
- tunnel / VPN；
- local peer link。

重要：

$$
\boxed{
AIProvider
\neq
NetworkProvider
\neq
CommunicationIdentity.
}
$$

A-06 將進一步把此差異轉成 sovereignty contract。

---

# 30. Carrier Agility

FAL-MCI 提出：同一 semantic object 不必永遠綁定固定 carrier、固定頻帶或固定 physical backend。

A-05 採納其中較保守、已有工程類比的 Level I：

## Carrier / Backend Retuning

若 logical payload：

$$
O
$$

可經：

$$
R_{p_1}(O),
$$

$$
R_{p_2}(O),
$$

且接收後 logical integrity 維持：

$$
Decode(R_{p_i}(O))\approx O,
$$

那麼 carrier / medium 可以成為 path optimizer 的 degree of freedom。

這在現代網路中其實已有弱形式：

- Ethernet / Wi-Fi 同一 IP service；
- fibre / wireless backhaul；
- cellular band selection；
- satellite fallback；
- frequency-agile radio。

A-05 不需要假設高階 semantic language 已直接控制波形，就能成立。

---

# 31. Frequency / Phase 不是天然語義

SPAL 與 FARHP 提醒我們：頻率與相位可以成為可測、可控制、可離散化的資訊自由度。

例如：

$$
X(\tau,\omega)
=
A(\tau,\omega)e^{i\Phi(\tau,\omega)}.
$$

FARHP 對準週期聲音使用：

$$
\psi_k(t)
=
\operatorname{wrap}
\left(
\phi_k(t)-k\phi_1(t)
\right).
$$

這些都可作 future physical-wave representation 的研究接口。

但 A-05 必須保留：

$$
\boxed{
PhysicalCoordinate
\neq
SemanticPrimitive.
}
$$

只有在額外定義 codebook、operator contract、composition 與 receiver semantics 後，physical state 才可能成為高階語言的一部分。

因此：

$$
PSK\neq SPAL,
$$

$$
QAM\neq SemanticLanguage.
$$

---

# 32. FAL-MCI 與 A-05 的接口

FAL-MCI 的候選鏈：

$$
\text{Semantic Kernel}
\rightarrow
\text{Frequency / Phase / Carrier Selection}
\rightarrow
\text{Relay / Controller Network}
\rightarrow
\text{Physical Backend}.
$$

A-05 不採納整條鏈為既成實作。

目前可採納的是：

$$
\boxed{
\text{Flow Requirement}
\rightarrow
\text{Carrier / Path Selection}
\rightarrow
\text{Relay Network}.
}
$$

未來如果 FAL-MCI 的更強版本得到實驗支持，可以增加：

```text
Semantic/Operator Compiler Adapter
```

而不需要推翻 AHCF。

這是重要的 forward compatibility。

---

# 33. SPFC 與 A-05 的接口

SPFC 提出：

$$
L
\rightarrow
I_F
\rightarrow
IR_F
\rightarrow
u
\rightarrow
\mathcal R
\rightarrow
F(\mathbf x,t).
$$

其中 $\nu$ 為 physical control vector。

對 A-05 而言，SPFC 不應進入今日 transport core。

它應位於：

```text
Future Physical Path Compiler
```

其輸出若經安全驗證，可成為 Fabric Graph 中新的 programmable edge / relay capability。

所以：

$$
\boxed{
SPFC
\rightarrow
\text{Future AHCF Capability Provider}
}
$$

而不是：

$$
SPFC=AHCF.
$$

---

# 34. AI 在 Fabric 裡的合理角色

AI 可以做：

- traffic classification；
- path quality prediction；
- anomaly detection；
- handover prediction；
- congestion forecasting；
- policy explanation；
- cost optimization；
- capability discovery；
- failure diagnosis；
- adaptive media recommendation。

但不應把 packet forwarding 本身交給高延遲生成模型逐包推理。

因此：

$$
\boxed{
AI
\rightarrow
\text{Policy / Prediction / Planning}
}
$$

而：

$$
\boxed{
Deterministic Runtime
\rightarrow
\text{Fast Data-Plane Execution}.
}
$$

兩者混合才比較合理。

---

# 35. Fabric Policy

定義：

$$
\boxed{
\Pi_F
=
(
Allow,
Deny,
Prefer,
Avoid,
Require,
Budget,
Fallback
).
}
$$

例如：

```text
REQUIRE end_to_end_encryption FOR private_voice
AVOID metered_satellite FOR bulk_sync
PREFER enterprise_wifi FOR internal_artifacts
ALLOW cellular_multi_path FOR conference
REQUIRE human_notice BEFORE security_downgrade
DENY unknown_relay FOR credential_material
```

這種 policy 必須比自然語言 prompt 更靠近 executable contract。

---

# 36. QoS 不等於 User Utility

網路常優化：

- throughput；
- latency；
- packet loss。

但 AI-Native Continuum 真正需要的可能是：

$$
\boxed{
Utility_q
=
f(
QoS,
Task,
Attention,
Cost,
Privacy,
Surface
).
}
$$

例如在車上休息：

$$
Utility_{notification}
$$

可能因 interruption cost 而很低，即使網路完美。

所以 Fabric 不直接決定「要不要通知使用者」。

A-04 Attention Broker 決定 interaction；A-05 只回報 network capability。

這保持分層。

---

# 37. Fabric Telemetry

最小 metrics：

```text
path.available
path.rtt_ms
path.jitter_ms
path.loss_rate
path.throughput_up
path.throughput_down
path.energy_estimate
path.metered
path.cost_estimate
path.security_level
path.handover_count
path.relay_chain
flow.degradation_level
flow.continuity_loss
```

Telemetry 的目的不是蒐集越多越好。

而是支援：

$$
Plan
\rightarrow
Observe
\rightarrow
Evaluate
\rightarrow
Adapt.
$$

A-06 將要求 retention 與 privacy boundary。

---

# 38. Evidence Receipt

每次重要 path migration 可以產生：

```json
{
  "flow_id": "...",
  "from_path": "...",
  "to_path": "...",
  "reason": "quality_degradation",
  "policy_epoch": "...",
  "security_before": "...",
  "security_after": "...",
  "continuity_loss_ms": 0,
  "degradation_level": 1,
  "timestamp": "..."
}
```

這不是要記錄每一個 packet。

而是：

$$
\boxed{
\text{Meaningful Network-State Transition}
\rightarrow
\text{Auditable Receipt}.
}
$$

如此 A-04 的 Action Receipt 與 A-05 的 Fabric Receipt 可以關聯。

---

# 39. Failure Taxonomy

AHCF 至少區分：

## F1｜Interface Failure

NIC / modem / radio unavailable。

## F2｜Coverage Failure

physical link 不可達。

## F3｜Congestion Failure

可連線但 QoS 不可接受。

## F4｜Provider Failure

authentication / billing / backend outage。

## F5｜Relay Failure

中間 relay 不可用。

## F6｜Security Failure

path 可通，但不符合 trust / encryption policy。

## F7｜Jurisdiction Failure

path 會跨越 policy 禁止的區域或 provider domain。

## F8｜Conversion Failure

跨媒介轉換造成 integrity / quality 不可接受。

## F9｜Handover Failure

新 path 可用，但 migration 失敗。

## F10｜Continuity Reconstruction Failure

network 已恢復，上層 session / task 沒有正確 resume。

最後一類再次證明：

$$
\boxed{
NetworkRecovery
\neq
CommunicationRecovery.
}
$$

---

# 40. Local-first 與 Fabric 的關係

若 Continuum 過度假設 cloud always reachable，那任何 network innovation 都只能減少失敗，不能消除架構脆弱性。

所以應允許：

$$
LocalState
\rightarrow
Checkpoint
\rightarrow
DeferredSync.
$$

這使：

$$
Connectivity=0
$$

時，某些本地活動仍可繼續：

- 閱讀 cache；
- 寫草稿；
- 記錄 voice note；
- local AI reasoning；
- task update；
- offline message queue。

網路恢復後：

$$
Reconcile(Local,Remote).
$$

因此 AHCF 的最高 robustness 不是：

> 我永遠有至少一條網路。

而是：

> 即使暫時沒有網路，Communication World 也不必歸零。

---

# 41. Reference Architecture

```text
┌────────────────────────────────────────────────────┐
│ A-04 AI Communication Runtime                     │
│ Intent / Planner / Router / Attention / Policy    │
└───────────────────────┬────────────────────────────┘
                        │ Flow Requirement Contract
┌───────────────────────▼────────────────────────────┐
│ A-05 Adaptive Hybrid Communication Fabric         │
│                                                    │
│  Fabric Policy Engine                             │
│  Capability Registry                              │
│  Path Graph                                       │
│  Multipath Controller                             │
│  Handover / Relay Manager                         │
│  Security / Trust Filter                          │
│  Degradation Coordinator                          │
│  Fabric Evidence                                  │
└───────────────┬─────────────┬─────────────┬────────┘
                │             │             │
        ┌───────▼──────┐ ┌────▼─────┐ ┌────▼──────────┐
        │ IP / QUIC    │ │ 3GPP     │ │ Wi-Fi / LAN   │
        │ MPTCP / VPN  │ │ ATSSS    │ │ Ethernet      │
        └──────────────┘ │ IAB/NTN  │ └───────────────┘
                         └──────────┘
                │             │             │
        ┌───────▼─────────────▼─────────────▼────────┐
        │ Physical / Provider / Relay Adapters       │
        │ fibre | RF | satellite | THz | surface    │
        │ future programmable physical interfaces   │
        └────────────────────────────────────────────┘
```

此圖的核心是：

$$
\boxed{
Application
\not\rightarrow
PhysicalLink\ directly.
}
$$

中間需要 Fabric Contract。

---

# 42. Minimum API Contract

## 42.1 Discover Paths

```text
GET /fabric/paths
```

回傳：

- capability；
- health；
- trust；
- metering；
- current epoch。

## 42.2 Submit Flow Requirement

```text
POST /fabric/flows
```

輸入：

```json
{
  "class": "interactive_voice",
  "max_latency_ms": 150,
  "min_security": "e2ee",
  "reliability": "high",
  "metered_policy": "allow",
  "fallback": ["audio", "text"]
}
```

## 42.3 Observe Flow

```text
GET /fabric/flows/{flow_id}
```

## 42.4 Force Policy Action

例如使用者可要求：

```text
PIN(path)
DISABLE(path)
AVOID(provider)
PAUSE(flow)
FORCE_LOCAL_ONLY
```

AI 不應移除 human override。

---

# 43. Path Selection State Machine

```text
DISCOVER
→ EVALUATE
→ SELECT
→ ESTABLISH
→ VERIFY
→ ACTIVE
→ DEGRADE / MIGRATE / SPLIT
→ VERIFY
→ ACTIVE
→ CLOSE
```

任何 security violation：

```text
ACTIVE
→ BLOCKED
→ REVIEW / FAILOVER / CLOSE
```

任何 connectivity loss：

```text
ACTIVE
→ OFFLINE_QUEUE
→ DISCOVER
```

因此 OFFLINE 不是 exception crash，而是正式 state。

---

# 44. 近期工程版本不需要先做 6G

A-05 的重要工程判斷是：

$$
\boxed{
\text{AHCF MVP}
\not\Rightarrow \text{Require}
\text{new PHY invention}.
}
$$

第一版完全可以使用：

- Ethernet；
- Wi-Fi；
- one or more cellular modems；
- VPN；
- MPTCP where supported；
- QUIC-based application sessions；
- satellite terminal as optional adapter；
- local store-and-forward；
- path health monitor；
- policy engine；
- application-level resume。

也就是先做：

$$
\boxed{
\text{Software-defined Hybrid Connectivity Orchestrator}.
}
$$

而不是等待未來硬體。

---

# 45. Phase 0～Phase 5 Roadmap

## Phase 0｜Simulation

建立 fake paths：

```text
wifi_good
wifi_bad
cellular_good
cellular_dead
satellite_slow
untrusted_public
```

驗證 route policy。

## Phase 1｜PC Multi-Interface

實驗：

- Ethernet；
- Wi-Fi；
- tethering；
- VPN；
- local queue。

## Phase 2｜Vehicle Gateway Prototype

加入：

- dual cellular；
- vehicle Wi-Fi；
- optional satellite；
- predictive handover；
- bandwidth degradation hooks。

## Phase 3｜Application-aware Multipath

讓：

- voice；
- video；
- sync；
- agent traffic；

使用不同 policy。

## Phase 4｜Relay / Edge Fabric

加入：

- local edge；
- peer relay；
- mobile relay test；
- enterprise gateway；
- evidence receipts。

## Phase 5｜Physical Programmability Research

才開始接：

- SDR；
- programmable radio；
- RIS；
- metasurface；
- THz / photonic research；
- FAL-MCI / SPFC experimental adapters。

---

# 46. Measurement Harness

每次測試至少記錄：

$$
T_{handover},
$$

$$
PacketLoss_{handover},
$$

$$
SessionResumeRate,
$$

$$
ContinuityLoss,
$$

$$
SecurityDowngradeCount,
$$

$$
CostPerFlow,
$$

$$
EnergyPerFlow.
$$

對 multimodal task 再加：

$$
ProjectionDegradationLevel.
$$

最終真正重要的 KPI 不是只有：

$$
Throughput.
$$

而是：

$$
\boxed{
TaskCompletionUnderMobility.
}
$$

---

# 47. 可證偽命題

A-05 提出下列可驗證命題。

## H1｜跨 path 可降低 communication interruption

在相同 coverage profile 下：

$$
Interruption_{multi}
<
Interruption_{single}.
$$

若長期測試不成立，則 path orchestration 的成本可能高於收益。

## H2｜Application-aware policy 優於 global best-network policy

對 mixed workload：

$$
Utility_{flow-aware}
>
Utility_{global}.
$$

## H3｜Predictive handover 可降低 transition loss

$$
L_{NC}^{predictive}
<
L_{NC}^{reactive}.
$$

## H4｜Local-first checkpoint 可降低 hard reset

$$
ResetRate_{local-first}
<
ResetRate_{cloud-only}.
$$

## H5｜增加 path 數量不保證效益單調增加

不存在一般保證：

$$
U(n+1)>U(n).
$$

這是一個重要反證保護，避免「更多網路一定更好」的錯誤產品假設。

---

# 48. 邊界：本文不主張什麼？

A-05 不主張：

1. wired / wireless 工程分類應被刪除；
2. 無線可以取代所有晶片／資料中心／電力導線；
3. 所有跨媒介 conversion 都能透明且零成本；
4. satellite 可以在所有情況取代 terrestrial network；
5. multipath 永遠比 single path 快；
6. RIS / metasurface 已普遍成為商用網路核心；
7. EIT 已取代 Shannon information theory；
8. FARHP / SPAL 是 Internet transport protocol；
9. FAL-MCI / SPFC 已被實驗證明為通用語義—物理通訊編譯器；
10. AI 應逐 packet 控制所有網路；
11. path switch 可以忽略 security / jurisdiction / cost；
12. always connected 是 Continuum 的必要條件。

本文真正主張只有：

$$
\boxed{
\text{Communication Continuity should be architecturally independent from any single access path, carrier, provider, or physical medium whenever the underlying task permits it.}
}
$$

---

# 49. 對 EVEMISS 現有產品的回流

## 49.1 PAI Relay

增加：

- connectivity-aware CommunicationSession；
- network-quality-aware call / message fallback；
- local queue；
- satellite / cellular fallback adapter；
- no-security-downgrade policy。

## 49.2 Consumer Core

既有 Provider / Session / Event / WebRTC / Transport 層可增加：

```text
fabric/
path-registry/
flow-policy/
connectivity-observer/
handover-manager/
relay-adapter/
```

## 49.3 Enterprise Communication Suite

增加：

- approved network domain；
- enterprise path policy；
- VPN / secure gateway preference；
- continuity evidence；
- network-related incident class。

## 49.4 Virtual Character Platform

對 live performance：

- media degradation ladder；
- multi-network failover；
- local buffer；
- partial agent continuation when external network fails。

因此 AHCF 是共用 primitive，但仍不得共享不同產品的 identity / memory / authority。

---

# 50. 與 Series B 的橋接

Series B 將處理：

$$
\text{Programmable Mobility Space}.
$$

A-05 只提供它需要的 connectivity substrate。

對車艙：

$$
VehicleSurface
+
AHCF
\rightarrow
ConnectedMobileSpace.
$$

再加 A-02～A-04：

$$
ConnectedMobileSpace
+
PCS
+
MultimodalProjection
+
ACR
\rightarrow
PersistentHumanAIContinuum.
$$

所以 Series B 不需要重新發明 network stack。

---

# 51. 下一篇 A-06 的問題

當 AHCF 可以在不同 provider、network、relay 與 physical path 之間切換後，立即出現新的問題：

> **誰擁有那個跨路徑仍然持續存在的 identity、state、keys、permissions、memory 與 communication history？**

如果答案仍然是：

> 某一個單一 Provider。

那 Continuum 只是在技術上跨網路，制度上仍被鎖死。

因此 A-06 將定義：

# **Personal Communication Sovereignty**

並研究：

- canonical personal state；
- provider independence；
- key ownership；
- encrypted state；
- revocable delegation；
- export / migration；
- local / cloud authority；
- recovery；
- personal communication ledger；
- model replaceability。

---

# 52. 結論

通訊技術的歷史可以被粗略描述為：

$$
\text{Dedicated Medium}
\rightarrow
\text{Packet Network}
\rightarrow
\text{Mobile Access}
\rightarrow
\text{Multi-Access}
\rightarrow
\text{Hybrid Physical Network}.
$$

但 AI-Native Communication Continuum 再向前要求一件事：

$$
\boxed{
\text{Logical communication world must persist while physical paths change beneath it.}
}
$$

因此本文提出 Adaptive Hybrid Communication Fabric：不消滅 wired / wireless，而是把它們從最高層 ontology 降為 path capability；不要求一項尚不存在的萬能通訊技術，而是讓 Ethernet、Wi-Fi、cellular、satellite、MPTCP、ATSSS、IAB、NTN、relay、fibre、THz 與未來 physical adapters 可以在一個共同 Fabric Contract 下逐步加入。

對當代工程，第一步已經可以做：

$$
\boxed{
\text{Multi-interface observation}
+
\text{Flow policy}
+
\text{Failover / Multipath}
+
\text{Local-first resume}
+
\text{Evidence}.
}
$$

對前沿研究，fibre–wireless transparent relay、programmable metasurface 與 EIT 顯示 physical communication substrate 正變得更加可整合與可程式化。

對 EVEMISS 的遠期研究，FAL-MCI 與 SPFC 則提供更強的 carrier / backend / field compilation 猜想，但必須保持猜想地位，直到有可重複實驗支持。

最終架構可以收斂為：

$$
\boxed{
\text{Persistent State}
\rightarrow
\text{Communication Intent}
\rightarrow
\text{AI Runtime}
\rightarrow
\text{Flow Requirement}
\rightarrow
\text{Adaptive Fabric}
\rightarrow
\text{Path / Relay / Carrier}
}
$$

底層可以變。

上層不必因此重新成為另一個人、另一段對話、另一個工作世界。

這才是 AI-Native Communication Continuum 在網路與物理連通性層真正需要的「連續」。

---

# 參考資料與外部技術錨點

1. IETF, RFC 8684, *TCP Extensions for Multipath Operation with Multiple Addresses*, 2020. `https://www.rfc-editor.org/rfc/rfc8684.html`
2. 3GPP TS 23.501 / related Release 18 change requests, Access Traffic Steering, Switching and Splitting (ATSSS). `https://portal.3gpp.org/`
3. 3GPP Release 18 Mobile IAB work items and TS 38-series change requests. `https://portal.3gpp.org/`
4. 3GPP Release 18 NR NTN enhancements. `https://portal.3gpp.org/`
5. Zhang, Y. et al., “Integrated photonics enabling ultra-wideband fibre–wireless communication,” *Nature* 651, 348–355, 2026. `https://www.nature.com/articles/s41586-026-10172-9`
6. Tsai, D. P. et al., “Trivial-nontrivial programmable topological metasurfaces for sensing and communication,” *Light: Science & Applications*, 2026. `https://www.nature.com/articles/s41377-026-02419-x`
7. IEEE Information Theory Society, *Electromagnetic Information Theory*, JSAIT Special Issue. `https://www.itsoc.org/jsait/jsait-issue/electromagnetic-information-theory`
8. IETF QUIC Working Group, *Managing multiple paths for a QUIC connection*, Internet-Draft, 2026 evolution point; draft status must be checked before implementation claims.

---

# Canonical Source Statement

本文件為本輪正式 UTF-8 canonical source。

- 數學 delimiter 僅使用 ` $...$ ` 與 `$$...$$`；
- 不以聊天渲染畫面作為正式原稿；
- 不進行 escape 類 round-trip；
- 不將 LaTeX 轉成 Unicode 數學字元後再當 source；
- FARHP / SPAL / FAL-MCI / SPFC 的研究地位依本文 S0 / S1 / S2 分層處理；
- 正式 commit 前應執行 encoding、delimiter、manifest、hash 與 ZIP integrity validation。
