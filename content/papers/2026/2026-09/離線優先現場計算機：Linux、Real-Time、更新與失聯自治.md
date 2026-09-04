# 離線優先現場計算機：Linux、Real-Time、更新與失聯自治

**系列：外掛式物理計算機與現場計算設備研究，第 4 篇**  
**英文系列名：External Physical Compute Appliances and Field Computing Systems**  
**英文篇名：Offline-First Field Compute Appliances: Local Execution Closure, Transactional Updates, and Disconnected Autonomy**  
**版本：v0.1**  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：2026-08-29**  
**狀態：公開草稿／部署架構、離線自治與現場恢復框架**

## 摘要

前四篇已將 External Physical Compute Appliance（EPCA）從設備總綱、Carrier-Generalized Abacus、Observable Physical Computation 推進到 Supervisor–Physical-Core Separation。到這一步，一台設備已可以具有 Linux-class Application Plane、real-time controller、FPGA / deterministic I/O、platform management、verification plane 與獨立 physical compute core。然而，這仍不足以讓它成為真正的「現場計算機」。一台部署在工廠、戶外量測站、船舶、礦區、遠端觀測站、維修現場或網路品質不可保證的科研設備，不能把基本運算能力建立在雲端登入、遠端 API、套件倉庫、持續授權伺服器或永遠在線的 control plane 上。

本文提出 Offline-First Field Compute Appliance 架構，將「網路失效仍可計算」正式化為 **Local Execution Closure（LEC）**。LEC 不是「設備有 cache」或「斷網仍能開機」，而是對指定任務集合而言，輸入取得、演算法、backend driver、校正資料、執行 runtime、驗證、結果產生與本地證據保存所需的必要依賴，都能在沒有網路的條件下於設備內部閉合。網路存在時可以提供更新、遠端管理、資料同步、協作、雲端 AI 或額外資料源；網路消失時，已宣告為 local-closed 的核心任務仍應保持語義不變。

本文進一步指出，Local Execution Closure 必須是 task-relative、version-relative 與 freshness-aware。某些任務依賴即時氣象、遠端資料庫或最新模型，因此在斷網時本來就不可能保持相同語義；這不構成 appliance 失敗，而是該任務不屬於本地閉合集合。反之，若設備聲稱某個 FFT、光譜擬合、結構估算、physical-core transform 或校正程序可離線完成，則其依賴不得在執行途中秘密回到網路。

在部署層，本文提出 Read-Only / Immutable Base、A/B System Slot、Recovery Environment、Versioned Algorithm Store、Calibration Store、Evidence Store 與 Durable Job Journal 的分區模型；建立 Stage–Verify–Quiesce–Trial–Health Check–Commit / Rollback 的 transactional update 狀態機；並允許 signed removable-media update，使 air-gapped 或長期失聯設備仍能被安全更新。更新權限與執行權限分離：現有已安裝且已驗證的任務可以在可信時間或網路暫時不可用時繼續執行，但新的軟體安裝、過期 metadata 驗證或無法建立 authenticity 的更新應 fail closed。

本文另提出 Local Field Autonomy 等級 LFA-F0 至 LFA-F5，分別描述 network-bound device、offline boot、offline execution closure、durable disconnected operation、transactional recovery 與 independently auditable field autonomy。此分級與 Paper 02 的 OPC-V、Paper 03 的 ESA-S 正交，形成：

$$
Q_{\mathrm{EPCA}}
=
(\mathrm{OPC\mbox{-}V},\mathrm{ESA\mbox{-}S},\mathrm{LFA\mbox{-}F}).
$$

本文最後主張：offline-first 並不等於 anti-network，也不等於拒絕雲端。它是一個權限與依賴方向的設計原則：

$$
\boxed{
\text{Local Compute}
\rightarrow
\text{Network Enhancement}
}
$$

而不是：

$$
\boxed{
\text{Network Availability}
\rightarrow
\text{Permission to Compute}.
}
$$

這使 EPCA 從「一個被 PC 控制的 accelerator」轉為真正可以被帶到現場、獨立開機、獨立執行、獨立保存證據、失聯後繼續工作、重新連線後再同步的計算設備，並為下一篇多基底模組化 Compute Backplane 提供穩定的 appliance substrate。

**關鍵詞：** Offline-First、Local Execution Closure、Field Computing、Embedded Linux、A/B Update、Transactional Update、Rollback、Recovery、Disconnected Operation、Evidence Store、Algorithm Package、EPCA、Physical Computing

---

## 1. 從「Embedded System」到「Field Computer」還差什麼？

一台 embedded system 可以很強。

它可以具有：

- 多核心 CPU；
- 16 GB、32 GB 或更多記憶體；
- NVMe / eMMC；
- FPGA；
- NPU / GPU；
- physical compute core；
- Ethernet / Wi-Fi / 5G；
- Linux；
- local display；
- USB、CAN、RS-485、GPIO 與高速 sensor I/O。

但只要它在核心任務上依賴：

$$
\text{cloud authentication},
$$

$$
\text{remote API},
$$

$$
\text{online package resolver},
$$

或：

$$
\text{remote compute service},
$$

那麼：

$$
N=0
\Rightarrow
\text{core task unavailable}.
$$

這樣的設備仍然比較接近：

$$
\text{edge client}
$$

而不是本文所說的：

$$
\boxed{
\text{field computer}.
}
$$

本文因此將核心問題改寫為：

> 一台現場計算設備在沒有外部網路服務時，是否仍然保有完成已宣告核心任務的必要狀態、程式、模型、校正、驅動、驗證與結果保存能力？

---

## 2. Offline-First 不是「偶爾可以離線」

常見產品會寫：

> 支援 offline mode。

但這句話可能只表示：

- UI 可以打開；
- 最近一頁資料仍在 cache；
- 可以先建立工作，稍後上傳；
- 部分功能暫時可用；
- 仍必須定期向伺服器重新驗證。

本文需要更強的概念。

對核心計算任務而言：

$$
\boxed{
\text{offline}
\not\equiv
\text{cached user experience}.
}
$$

真正需要的是：

$$
\boxed{
\text{offline}
\Rightarrow
\text{local execution semantics remain closed}.
}
$$

---

## 3. Local Execution Closure：正式定義

令一個任務為 $\tau$。

其完整執行依賴集合為：

$$
D_{\tau}
=
\{
D_{\mathrm{alg}},
D_{\mathrm{runtime}},
D_{\mathrm{driver}},
D_{\mathrm{cal}},
D_{\mathrm{data}},
D_{\mathrm{verify}},
D_{\mathrm{storage}}
\}.
$$

設備在時間 $t$ 的本地可用狀態為：

$$
L_t.
$$

網路可用性寫為：

$$
N_t\in\{0,1\}.
$$

如果在：

$$
N_t=0
$$

時，存在一個完全本地的 execution plan：

$$
\pi_{\mathrm{local}}
$$

使得：

$$
D_{\tau}
\subseteq
L_t,
$$

且任務可以完成：

$$
x
\xrightarrow{\pi_{\mathrm{local}}}
y,
$$

並產生本地可保存的 evidence：

$$
E_{\tau},
$$

則稱：

$$
\boxed{
\mathrm{LEC}_{\tau}(t)=1.
}
$$

---

## 4. LEC 的輸出不只是答案

對 EPCA 而言，離線閉合不能只要求：

$$
y
$$

出得來。

還應要求至少形成：

$$
R_{\tau}
=
(y,E_{\tau}).
$$

其中 $E_{\tau}$ 可以包含：

- job ID；
- input hash；
- algorithm identity；
- algorithm version / revision；
- physical backend identity；
- backend firmware；
- calibration identity；
- runtime revision；
- raw physical observation；
- decoded physical result；
- optional refinement result；
- error estimate；
- monotonic timestamp；
- trusted wall-clock time，若可用；
- temperature / power / health metadata；
- supervisor assurance state；
- OPC evidence reference。

因此：

$$
\boxed{
\text{Local Execution Closure}
\supset
\text{Local Evidence Closure}.
}
$$

---

## 5. LEC 是 Task-Relative，而不是設備的永久屬性

不能只寫：

> 這台設備支援 offline。

更準確的說法是：

$$
\mathrm{LEC}_{\tau}=1
$$

或：

$$
\mathrm{LEC}_{\tau}=0.
$$

例如：

$$
\tau_1=\text{local FFT}
$$

可能：

$$
\mathrm{LEC}_{\tau_1}=1.
$$

但是：

$$
\tau_2=\text{query latest satellite weather field}
$$

若沒有本地最新資料，則：

$$
\mathrm{LEC}_{\tau_2}=0.
$$

這不是設備故障。

而是任務本身包含 remote freshness requirement。

---

## 6. Freshness-Aware Local Closure

令資料 $d_i$ 的年齡為：

$$
a_i(t).
$$

任務 $\tau$ 對該資料允許的最大 freshness horizon 為：

$$
h_i(\tau).
$$

只有當：

$$
a_i(t)
\le
h_i(\tau)
$$

時，本地副本才能滿足該依賴。

因此更完整的 LEC 是：

$$
\boxed{
\mathrm{LEC}_{\tau}(t)=1
\iff
D_{\tau}\subseteq L_t
\land
\forall d_i\in D_{\tau},
\ a_i(t)\le h_i(\tau).
}
$$

這防止一種常見錯誤：

> 有 cache，所以我們是 offline-first。

如果 cache 已經超過任務允許的有效期，語義就不同了。

---

## 7. Version-Relative Closure

同一任務：

$$
\tau
$$

在不同版本可能需要不同依賴。

因此 LEC 應綁定 execution manifest：

$$
M_{\tau}^{(v)}.
$$

例如：

$$
M_{\tau}^{(v)}
=
(
A_v,
R_v,
D_v,
C_v,
P_v
).
$$

其中：

- $A_v$：algorithm package；
- $R_v$：runtime；
- $D_v$：driver；
- $C_v$：calibration；
- $P_v$：physical backend configuration。

因此：

$$
\boxed{
\mathrm{LEC}_{\tau,v}
}
$$

比籠統的 offline flag 更有意義。

---

## 8. Network Optionality 原則

對已宣告 local-closed 的任務，網路應該是：

$$
\text{enhancement}
$$

而不是：

$$
\text{permission source}.
$$

也就是：

$$
\boxed{
N=1
\Rightarrow
\text{more capability, fresher data, easier management}
}
$$

但：

$$
\boxed{
N=0
\Rightarrow
\text{declared local core remains executable}.
}
$$

---

## 9. 網路可以增加什麼？

有網路時可以加入：

- software update；
- algorithm package update；
- calibration distribution；
- remote telemetry；
- remote diagnostics；
- evidence upload；
- team collaboration；
- remote data source；
- optional cloud compute；
- optional AI service；
- fleet management。

這些都可以存在。

但應寫成：

$$
\text{Local Core}
+
\text{Network Extension}.
$$

而不是：

$$
\text{Network Service}
+
\text{local shell}.
$$

---

## 10. 離線不等於與外界隔絕

Offline-first 也不代表：

- 永遠不連網；
- 不允許遠端管理；
- 不允許雲端資料；
- 不允許 AI；
- 不允許集中式 fleet management。

它真正改變的是 dependency orientation：

$$
\boxed{
\text{Compute authority originates locally.}
}
$$

遠端系統提供：

$$
\text{augmentation}.
$$

---

## 11. 一個 Offline-First EPCA 的本地狀態

本文建議最低本地部署狀態寫成：

$$
\mathcal L
=
\mathcal B
\oplus
\mathcal R
\oplus
\mathcal A
\oplus
\mathcal D
\oplus
\mathcal C
\oplus
\mathcal J
\oplus
\mathcal E
\oplus
\mathcal Q.
$$

其中：

- $\mathcal B$：base OS / boot environment；
- $\mathcal R$：compute runtime；
- $\mathcal A$：algorithm store；
- $\mathcal D$：backend driver / firmware；
- $\mathcal C$：calibration store；
- $\mathcal J$：durable job journal；
- $\mathcal E$：evidence store；
- $\mathcal Q$：recovery environment。

---

## 12. 為什麼 Base OS 應該盡量小？

對現場設備，base OS 的主要任務不是提供桌面體驗。

它應主要提供：

- boot；
- device drivers；
- security primitives；
- storage；
- process isolation；
- update framework；
- local service supervision；
- networking；
- hardware access control；
- recovery。

因此：

$$
\boxed{
\text{small trusted base}
<
\text{general desktop stack}.
}
$$

較小的 base 不代表一定比較安全，但通常更容易：

- inventory；
- version pinning；
- test；
- rollback；
- reproducibility；
- field recovery。

---

## 13. Immutable / Read-Only Base 的角色

現場設備最怕的是：

> 在使用數個月後，系統已經不知道自己變成什麼。

因此可以把系統拆成：

$$
\boxed{
\text{Immutable Base}
+
\text{Mutable Data}.
}
$$

Base 保存：

- kernel；
- system services；
- runtime；
- drivers；
- update agent。

Mutable data 保存：

- job input；
- output；
- evidence；
- local configuration；
- logs；
- permitted calibration state。

這可以降低更新後留下半套套件的風險。

---

## 14. 不必綁死某一種 Embedded Linux

本文不規定必須使用：

- Ubuntu Core；
- Yocto；
- Buildroot；
- Debian；
- OSTree-based distribution；
- vendor Linux。

因為 EPCA 的架構命題高於 distribution 選型。

但現有系統已證明：

$$
\text{immutable / image-based embedded Linux}
$$

以及：

$$
\text{transactional update / rollback}
$$

是成熟工程路線，而不是本文需要重新發明的底層能力。

---

## 15. A/B System Slot

一種典型部署可使用：

$$
\boxed{
S_A
\oplus
S_B.
}
$$

目前執行：

$$
S_A.
$$

新版本寫入：

$$
S_B.
$$

寫入完成前：

$$
S_A
$$

保持可啟動。

更新成功後才切換：

$$
S_A
\rightarrow
S_B.
$$

如果：

$$
\mathrm{Health}(S_B)=0,
$$

則：

$$
S_B
\rightarrow
S_A.
$$

---

## 16. A/B 的真正目的不是「有兩份系統」

核心是：

$$
\boxed{
\text{Activation is atomic at system identity level.}
}
$$

也就是更新過程不應出現：

$$
\frac{1}{2}S_A+
\frac{1}{2}S_B.
$$

對 field appliance 而言，這比傳統 desktop 的 in-place package mutation 更容易管理。

---

## 17. Recovery Environment 應與 A/B 分開理解

即使 A/B 都無法正常啟動，仍可以保留：

$$
\mathcal Q
=
\text{Recovery Environment}.
$$

其任務不是執行完整研究工作，而是：

- self-test；
- storage inspection；
- log export；
- network repair；
- slot selection；
- image restore；
- factory recovery；
- field service。

因此：

$$
\boxed{
\text{Run System}
\neq
\text{Recovery System}.
}
$$

---

## 18. System Update 與 Algorithm Update 必須分離

若每次新增一個演算法都更新整個 OS，成本太高。

因此建議：

$$
\boxed{
\text{System Image}
\neq
\text{Algorithm Package}.
}
$$

System Image 更新：

- kernel；
- runtime ABI；
- core drivers；
- supervisor services。

Algorithm Package 更新：

- computation graph；
- numerical kernel；
- physical-core configuration；
- parameter schema；
- validation vectors；
- optional UI definition。

---

## 19. Algorithm Package 不是一般 App

對 EPCA 而言，algorithm package 應比較像：

$$
\boxed{
\text{versioned computational contract}.
}
$$

它至少應聲明：

$$
A
=
(
\mathrm{id},
\mathrm{version},
\mathrm{input},
\mathrm{output},
\mathrm{backend},
\mathrm{precision},
\mathrm{resources},
\mathrm{validator}
).
$$

如果使用 physical core，還需包含：

- required backend type；
- allowed firmware range；
- calibration compatibility；
- pre-processing operator；
- physical operator；
- decoder；
- refinement policy；
- OPC evidence requirement。

---

## 20. Calibration 是第一級部署物件

Physical computing 尤其不能假設 calibration 永遠不變。

令 calibration snapshot 為：

$$
C_k.
$$

每一筆 physical result 應綁定：

$$
\mathrm{id}(C_k).
$$

更新 backend firmware 或 physical module 之後，可能需要：

$$
C_k
\rightarrow
C_{k+1}.
$$

因此系統更新成功不代表 physical compute automatically valid。

仍需：

$$
\boxed{
\mathrm{OSHealth}=1
\land
\mathrm{BackendHealth}=1
\land
\mathrm{CalibrationCompatible}=1.
}
$$

---

## 21. Transactional Update Manifest

一次更新可以抽象為：

$$
U
=
(
M,
A,
H,
\Sigma,
K,
R
).
$$

其中：

- $M$：manifest；
- $A$：artifacts；
- $H$：hashes；
- $\Sigma$：signatures；
- $K$：compatibility constraints；
- $R$：rollback / recovery policy。

更新不應只問：

> 檔案下載完了嗎？

而應問：

$$
\boxed{
\text{這組 artifacts 是否共同形成一個可啟動、可驗證、可回復的版本？}
}
$$

---

## 22. 建議的 Update State Machine

本文提出：

$$
\begin{aligned}
&\mathrm{Discover}\rightarrow
\mathrm{Fetch}\rightarrow
\mathrm{Verify}\rightarrow
\mathrm{Stage}\rightarrow\\
&\mathrm{Quiesce}\rightarrow
\mathrm{ActivateTrial}\rightarrow
\mathrm{HealthCheck}\rightarrow
\mathrm{Commit}.
\end{aligned}
$$

若任一步失敗：

$$
\rightarrow
\mathrm{Rollback}
$$

或：

$$
\rightarrow
\mathrm{Recovery}.
$$

---

## 23. Quiesce 是 Physical Compute Appliance 特別重要的一步

一般軟體服務更新時，可能只需停止 daemon。

EPCA 還可能有：

- physical core 正在執行；
- ADC 正在 acquisition；
- FPGA queue 尚未 drain；
- evidence 尚未 commit；
- calibration state 正在寫入。

因此更新 activation 前應達成：

$$
\boxed{
\mathrm{QuiescentState}=1.
}
$$

也就是：

- 不接受新 job；
- 已開始 job 完成或被安全中止；
- raw evidence 已固定；
- journal 已 flush；
- backend 已進 safe idle；
- persistent state 已一致。

---

## 24. Trial Boot 與 Commit

更新後第一次啟動不應立刻視為永久成功。

可先進：

$$
S_{\mathrm{trial}}.
$$

再執行：

$$
\mathrm{BootHealth},
$$

$$
\mathrm{RuntimeHealth},
$$

$$
\mathrm{StorageHealth},
$$

$$
\mathrm{PhysicalBackendSelfTest}.
$$

全部滿足後才：

$$
\boxed{
\mathrm{Commit}(S_{\mathrm{trial}}).
}
$$

否則 rollback。

---

## 25. Power-Loss Safety

Field appliance 必須假設：

$$
\text{power can disappear at inconvenient times}.
$$

例如：

- update 正在寫入；
- evidence 正在 commit；
- physical job 剛完成；
- filesystem metadata 正在變更。

因此設計目標應是：

$$
\boxed{
\text{Power loss}
\not\Rightarrow
\text{unknown machine identity}.
}
$$

設備重啟後至少能知道：

- 上次 committed system version；
- staging version；
- 上次 committed job；
- 哪個 job 可能已 physical-executed 但未 publish；
- evidence 是否完整；
- 是否必須進 recovery。

---

## 26. Durable Job Journal

每個 job 應具有：

$$
j
\rightarrow
\mathrm{JobRecord}(j).
$$

其中保存：

- job ID；
- creation state；
- input identity；
- execution manifest；
- backend identity；
- state transition；
- evidence reference；
- result publication state。

最簡單的狀態可以是：

$$
\mathrm{NEW}
\rightarrow
\mathrm{PREPARED}
\rightarrow
\mathrm{ARMED}
\rightarrow
\mathrm{EXECUTED}
\rightarrow
\mathrm{EVIDENCED}
\rightarrow
\mathrm{PUBLISHED}.
$$

---

## 27. Crash 後不要假裝「沒事」

若 crash 發生在：

$$
\mathrm{EXECUTED}
$$

之後，但：

$$
\mathrm{PUBLISHED}
$$

之前，不能直接重新算並覆蓋。

應至少分類為：

$$
\boxed{
\mathrm{EXECUTED\_UNPUBLISHED}
}
$$

或在無法判斷時：

$$
\boxed{
\mathrm{EXECUTION\_STATE\_UNCERTAIN}.
}
$$

這在 physical core 具有 stochastic、thermal 或 calibration drift 時尤其重要。

---

## 28. Result Publication 應具 Idempotency

若網路重新連線後重送結果，不應產生多個看似不同的 execution。

可以使用：

$$
K_j
=
H(
\mathrm{job\_id},
\mathrm{manifest},
\mathrm{input\_hash}
).
$$

作為 publication idempotency key。

同一 committed execution 的遠端同步應是：

$$
\text{copy / replicate},
$$

而不是：

$$
\text{re-create as a new computation}.
$$

---

## 29. Offline Evidence Queue

失聯時：

$$
E_1,E_2,\ldots,E_n
$$

應先安全保存在本地。

重新連線後：

$$
\{E_i\}_{i=1}^{n}
\rightarrow
\text{remote archive}.
$$

但遠端 sync 成功與否，不應改寫本地已 committed 的結果語義。

因此：

$$
\boxed{
\text{Evidence generation}
\neq
\text{Evidence upload}.
}
$$

---

## 30. Storage Pressure 是真實 Field Failure Mode

離線設備可能幾天、幾週甚至更久無法上傳。

因此 evidence store 需要：

- retention policy；
- priority；
- compression；
- capacity watermark；
- write reservation；
- protected metadata；
- optional export to removable media。

系統不能在 storage 100% 後才第一次思考這個問題。

---

## 31. Evidence 不應被一般 Log Rotation 靜默刪除

一般 log 可以：

$$
\text{rotate}.
$$

但被列為 scientific / engineering evidence 的 artifact 應有不同 retention policy。

可以定義：

$$
\mathcal E
=
\mathcal E_{\mathrm{critical}}
\oplus
\mathcal E_{\mathrm{diagnostic}}
\oplus
\mathcal E_{\mathrm{temporary}}.
$$

優先保留：

$$
\mathcal E_{\mathrm{critical}}.
$$

---

## 32. Signed Offline Update

沒有網路不代表不能更新。

可以透過：

- USB；
- SD card；
- service laptop；
- local maintenance network；
- portable repository。

送入：

$$
U_{\mathrm{offline}}.
$$

但是 trust root 必須已存在設備內。

設備仍需：

$$
\mathrm{VerifySignature}(U)=1,
$$

$$
\mathrm{VerifyHash}(U)=1,
$$

以及 compatibility check。

因此：

$$
\boxed{
\text{Offline update}
\neq
\text{unsigned update}.
}
$$

---

## 33. TUF / Uptane 類思想可以被借用，但不必照搬

TUF 強調 software update metadata、角色分離、key compromise resilience 與 rollback / freeze attack 防禦；Uptane 則把這種思路推到連線不穩定、設備異質、更新失敗代價很高的車載環境。

EPCA 不需要宣稱自己是 TUF 或 Uptane implementation。

但可以借用其重要原則：

$$
\boxed{
\text{signed metadata}
+
\text{role separation}
+
\text{rollback protection}
+
\text{compromise resilience}.
}
$$

---

## 34. Offline Time 是一個容易被忽略的問題

Secure update metadata 常與時間相關。

但 field appliance 長時間失聯時可能遇到：

- RTC 漂移；
- RTC battery failure；
- trusted network time unavailable；
- TPM state change；
- clock 被重設。

因此：

$$
\text{monotonic execution time}
$$

與：

$$
\text{trusted wall-clock time}
$$

應分開。

---

## 35. Time Failure 不應自動摧毀既有本地計算能力

若設備失去可信 wall-clock，合理策略可以是：

$$
\boxed{
\text{run already-installed validated workloads}
}
$$

但：

$$
\boxed{
\text{reject freshness-sensitive new update validation}
}
$$

直到 trusted time 被重新建立。

也就是：

$$
\text{Execution Authority}
\neq
\text{Update Authority}.
$$

---

## 36. Local Authentication 也不應完全依賴 Cloud

若核心現場功能需要每次登入遠端 identity provider：

$$
N=0
\Rightarrow
\text{authorized operator locked out}.
$$

因此可以保留：

- local device identity；
- local operator role；
- hardware token；
- cached but policy-bounded credentials；
- service key；
- physical maintenance mode。

但這些機制必須依使用場域安全需求設計。

本文只確立原則：

$$
\boxed{
\text{Local compute should have a local authorization path.}
}
$$

---

## 37. Field Runtime State Machine

一台 EPCA 可至少具有：

$$
\begin{aligned}
&\mathrm{BOOTSTRAP},\\
&\mathrm{READY\_OFFLINE},\\
&\mathrm{READY\_CONNECTED},\\
&\mathrm{EXECUTING},\\
&\mathrm{DEGRADED},\\
&\mathrm{UPDATE\_STAGED},\\
&\mathrm{RECOVERY}.
\end{aligned}
$$

其中最重要的是：

$$
\mathrm{READY\_OFFLINE}
$$

不是錯誤狀態。

它是一個正常 operational state。

---

## 38. Network Loss 應該是 State Transition，不是 System Failure

若設備由：

$$
\mathrm{READY\_CONNECTED}
$$

失去網路，理想行為是：

$$
\mathrm{READY\_CONNECTED}
\rightarrow
\mathrm{READY\_OFFLINE}.
$$

而不是：

$$
\mathrm{READY\_CONNECTED}
\rightarrow
\mathrm{ERROR}.
$$

除非當前 job 本身：

$$
\mathrm{LEC}_{\tau}=0.
$$

---

## 39. Fail-Operational 與 Fail-Closed 必須分開

Offline-first 不能被誤解為「任何情況都硬跑」。

某些失效應：

$$
\text{fail-operational}.
$$

例如：

- network unavailable；
- remote telemetry unavailable；
- update server unavailable。

只要 local closure 存在，仍可繼續。

另一些失效應：

$$
\text{fail-closed}.
$$

例如：

- update signature invalid；
- backend identity unknown；
- calibration incompatible；
- result path contamination；
- physical core fault 超過允許範圍。

---

## 40. Digital Fallback 可以有，但必須改身份

Paper 03 已確立：

$$
\text{No Silent Substitution}.
$$

因此若 physical backend 故障：

$$
\mathcal P
\rightarrow
\mathrm{FAIL},
$$

設備可以選擇：

$$
\mathcal S_{\mathrm{digital}}
$$

接手。

但輸出必須標記：

$$
\boxed{
\mathrm{backend}=\text{digital-fallback}
}
$$

而不是繼續宣稱：

$$
\mathrm{backend}=\text{physical-core}.
$$

---

## 41. Degraded Mode 應是顯式狀態

現場設備可能因：

- 過熱；
- 電池不足；
- sensor noise；
- calibration aging；
- storage pressure；
- 部分 compute module unavailable；

而需要降低能力。

因此：

$$
\mathrm{DEGRADED}
$$

可以合法存在。

但設備應說清楚：

- 哪些算法不可用；
- 哪些 precision 降低；
- 哪些 backend 被停用；
- 哪些 evidence 不完整；
- 是否允許 publish。

---

## 42. Brownout / Battery / UPS 對 Field Device 的意義

本文不要求所有 EPCA 都有 UPS。

但可以根據部署場景加入：

- supercapacitor；
- small UPS；
- battery-backed flush window；
- power-fail interrupt；
- voltage supervisor。

目的不是讓機器永遠不關機，而是提供：

$$
\Delta t_{\mathrm{safe}}
$$

讓：

- journal commit；
- evidence metadata flush；
- physical core safe idle；
- storage sync。

---

## 43. Watchdog 不是 Recovery Architecture 的全部

Hardware watchdog 可以處理：

$$
\text{system stops making progress}.
$$

但它無法告訴你：

- job 是否已 physical-executed；
- result 是否已 publish；
- update 是否應 commit；
- calibration 是否仍相容。

因此：

$$
\boxed{
\text{watchdog}
<
\text{recovery architecture}.
}
$$

---

## 44. Field Recovery Matrix

至少可以定義下列 fault class：

| Fault | 核心任務 | Update | 建議狀態 |
|---|---|---|---|
| Network loss | 若 LEC=1 繼續 | 暫停 fetch | READY_OFFLINE |
| Remote server loss | 繼續 | 暫停 | READY_OFFLINE |
| Physical core fault | 停止或顯式 fallback | 可維持 | DEGRADED / FAIL |
| Calibration invalid | 依 policy 停止 | 可更新 calibration | DEGRADED |
| OS trial boot failure | 不執行新 job | rollback | RECOVERY / old slot |
| Storage pressure | 限制新 job | 暫停 update | DEGRADED |
| Power loss | 重啟後恢復 journal | 依 slot 狀態恢復 | BOOTSTRAP |
| Trusted time loss | 已安裝 workload 可繼續 | freshness-sensitive update 禁止 | READY_OFFLINE |

這張表的重點不是固定所有產品行為，而是要求：

$$
\boxed{
\text{failure semantics must be declared before deployment}.
}
$$

---

## 45. Local Field Autonomy 分級

本文新增：

$$
\boxed{
\mathrm{LFA\mbox{-}F0}
\rightarrow
\mathrm{LFA\mbox{-}F5}.
}
$$

### LFA-F0 — Network-Bound Device

$$
N=0
\Rightarrow
\text{core computation unavailable}.
$$

### LFA-F1 — Offline Boot

設備能斷網開機，但核心任務未必閉合。

### LFA-F2 — Local Execution Closure

至少一組宣告任務具有：

$$
\mathrm{LEC}_{\tau}=1.
$$

### LFA-F3 — Durable Disconnected Operation

除 LEC 外，還具有：

- durable job journal；
- local evidence queue；
- crash recovery；
- disconnected multi-job operation。

### LFA-F4 — Transactional Update and Recovery

再加入：

- signed update；
- A/B 或等價 atomic deployment；
- trial boot；
- rollback；
- recovery environment；
- calibration compatibility gate。

### LFA-F5 — Independently Auditable Field Autonomy

再加入：

- explicit task closure manifest；
- offline evidence closure；
- independently inspectable update manifest；
- recovery provenance；
- reconnect sync 不改寫原始 committed evidence；
- fault-injection validation。

---

## 46. LFA 不等於「可以離線多久」

LFA 衡量 architecture assurance。

另一個獨立量是：

$$
T_{\mathrm{offline,max}}.
$$

它可能受到：

- battery；
- storage；
- calibration horizon；
- local data freshness；
- maintenance interval；
- consumables；
- sensor drift；
- operator logistics。

因此：

$$
\boxed{
\mathrm{LFA\mbox{-}F5}
\not\Rightarrow
T_{\mathrm{offline,max}}=\infty.
}
$$

---

## 47. EPCA 現在具有三個正交座標

Paper 02：

$$
\mathrm{OPC\mbox{-}V}
$$

回答：

> physical core 的因果計算證據有多強？

Paper 03：

$$
\mathrm{ESA\mbox{-}S}
$$

回答：

> supervisor authority separation 有多強？

Paper 04：

$$
\mathrm{LFA\mbox{-}F}
$$

回答：

> 設備在失聯、更新與現場故障下的本地自治有多強？

因此：

$$
\boxed{
Q_{\mathrm{EPCA}}
=
(
\mathrm{OPC\mbox{-}V},
\mathrm{ESA\mbox{-}S},
\mathrm{LFA\mbox{-}F}
).
}
$$

---

## 48. 三軸不能互相取代

一台設備可以：

$$
(\mathrm{OPC\mbox{-}V5},\mathrm{ESA\mbox{-}S2},\mathrm{LFA\mbox{-}F1}).
$$

意思是 physical evidence 很強，但 supervisor separation 與現場自治普通。

也可以：

$$
(\mathrm{OPC\mbox{-}V1},\mathrm{ESA\mbox{-}S5},\mathrm{LFA\mbox{-}F5}).
$$

意思是 appliance engineering 很成熟，但 physical computation evidence 還弱。

因此：

$$
\boxed{
\text{deployment maturity}
\neq
\text{physical-compute evidence strength}.
}
$$

---

## 49. Local Closure Coverage Ratio

對目標任務集合：

$$
\mathcal T
=
\{\tau_1,\ldots,\tau_n\},
$$

可定義：

$$
\mathrm{LCCR}
=
\frac{
|\{\tau_i:\mathrm{LEC}_{\tau_i}=1\}|
}{|\mathcal T|}.
$$

這可以衡量：

> 這台設備宣稱支援的工作，有多少真的能完全本地閉合？

但 LCCR 仍然不能直接代表性能。

---

## 50. Recovery Time 與 Evidence Loss Window

部署測試可以至少量測：

$$
T_{\mathrm{recovery}},
$$

以及：

$$
W_{\mathrm{evidence\ loss}}.
$$

理想設計讓：

$$
W_{\mathrm{evidence\ loss}}
\rightarrow
0,
$$

但實際上會受到 write batching、storage endurance 與 performance 的取捨。

重要的是必須被量測與聲明。

---

## 51. Reconnect 不等於「讓雲端修正歷史」

設備重新連線後可以：

- upload evidence；
- fetch updates；
- sync result；
- 取得新 data；
- remote re-analysis。

但如果遠端重新分析得到：

$$
y',
$$

不應直接把原本：

$$
y
$$

改掉。

應形成：

$$
R_{\mathrm{local}}
$$

以及：

$$
R_{\mathrm{remote\ reanalysis}}.
$$

這保持科研 provenance。

---

## 52. 範例一：現場振動分析

輸入：

$$
x(t).
$$

本地 pipeline：

$$
x(t)
\rightarrow
\mathrm{window}
\rightarrow
\mathrm{FFT}
\rightarrow
\mathrm{feature}
\rightarrow
\mathrm{diagnosis}.
$$

若所有演算法與 calibration 都在本地：

$$
\mathrm{LEC}_{\tau}=1.
$$

有網路時再：

- 上傳歷史趨勢；
- 更新 fault library；
- 接遠端 AI；
- 做 fleet comparison。

網路不是現場判斷的必要條件。

---

## 53. 範例二：光譜／光學量測

儀器取得：

$$
s(\lambda).
$$

EPCA 本地執行：

$$
\text{baseline correction}
\rightarrow
\text{denoise}
\rightarrow
\text{peak detection}
\rightarrow
\text{fit}
\rightarrow
\theta.
$$

若使用 optical / analog physical core，則再保存：

$$
E_{\mathcal P}.
$$

這讓結果即使在離線實驗室產生，也具有完整 local provenance。

---

## 54. 範例三：結構與工程估算

現場輸入：

$$
(
G,
M,
F,
B
),
$$

代表幾何、材料、載荷與 boundary condition。

設備執行有限的一組：

- matrix solve；
- reduced model；
- response estimate；
- uncertainty bound。

不必具備完整 CAD workstation。

因此再次顯示：

$$
\boxed{
\text{General computational power}
\not\Rightarrow
\text{General-purpose PC UX}.
}
$$

---

## 55. 範例四：RF / 聲學 Field Computer

若 Paper 01 的 CGA 以 RF 或 acoustic substrate 實作：

$$
\mathcal P_{\mathrm{RF/acoustic}},
$$

Linux supervisor 可負責：

- waveform selection；
- ADC/DAC configuration；
- timing；
- calibration；
- physical evidence；
- result decoding；
- local UI。

網路則只負責：

- package update；
- remote archive；
- collaboration。

這正是：

$$
\text{physical computer}
+
\text{field appliance}
$$

的結合。

---

## 56. 範例五：遠端科研站

想像一個：

- 山區；
- 海上；
- 極地；
- 沙漠；
- 臨時野外站；

部署的 sensor + EPCA。

即使：

$$
N=0
$$

數日，設備仍可：

$$
\text{measure}
\rightarrow
\text{compute}
\rightarrow
\text{validate}
\rightarrow
\text{store evidence}.
$$

恢復網路後才：

$$
\text{sync}.
$$

這比「離線只存 raw data、回基地才算」多出一個新的 operational option。

---

## 57. 為什麼 Memory 越大，這個類別越有價值？

傳統 embedded device 常被迫：

$$
\text{do little locally}
$$

因為記憶體與 storage 不足。

但如果現代 SoC appliance 擁有：

$$
16\ \mathrm{GB},
\quad
32\ \mathrm{GB},
\quad
64\ \mathrm{GB}
$$

甚至更多記憶體，則可以把更多：

- numerical libraries；
- lookup tables；
- models；
- local dataset；
- calibration history；
- evidence；

保留在本地。

因此：

$$
\boxed{
\text{memory abundance}
\uparrow
\Rightarrow
\text{possible local closure set}
\uparrow.
}
$$

---

## 58. 但「塞很多記憶體」不是 LEC 的充分條件

即使有：

$$
128\ \mathrm{GB}
$$

RAM，如果 license server 每次啟動都要上網，仍然：

$$
\mathrm{LEC}=0.
$$

如果 calibration key 只能從 cloud 拿，也可能：

$$
\mathrm{LEC}=0.
$$

所以 LEC 是 dependency architecture，不只是 hardware capacity。

---

## 59. AI 在這裡仍然不是必要元件

Paper 04 完全可以在：

$$
\text{AI}=0
$$

的情況下成立。

所有 offline-first、update、recovery、job journal、evidence 與 physical backend control，都可由 deterministic software 完成。

未來 AI 可以做：

- algorithm recommendation；
- anomaly explanation；
- backend routing；
- maintenance assistance；
- local natural-language UI。

但 AI 應是：

$$
\text{optional orchestrator},
$$

不是：

$$
\text{mandatory network dependency}.
$$

---

## 60. Minimal Network Surface

當設備不是 cloud-dependent 後，甚至可以讓 network plane 更保守。

例如只開放：

- signed update fetch；
- authenticated management；
- evidence sync；
- local LAN API。

而 physical execution 不接受任意 remote code injection。

因此：

$$
\boxed{
\text{network convenience}
\not\Rightarrow
\text{unbounded remote authority}.
}
$$

---

## 61. 現有技術已經提供大部分底層積木

2026 年的 Ubuntu Core 26 已經是面向 embedded device 的 minimal / immutable OS，並具有 recovery 與 image lifecycle 能力。

RAUC 提供 signed bundle 與 slot-based embedded Linux update。

Mender 提供 A/B root filesystem deployment、trial/commit/rollback 類 workflow。

OSTree 類 image tree deployment 展示了 atomic operating-system switch / rollback 的另一條路線。

TUF 與 Uptane 則提供 software update authenticity、metadata role separation 與 compromise-resilient update 的設計基礎。

因此本文的研究新意不是：

> 發明 A/B update。

而是：

$$
\boxed{
\text{將這些部署能力納入 physical compute appliance 的 local closure contract。}
}
$$

---

## 62. EPCA-2 的正式化

Paper 00 將 EPCA-2 暫稱：

$$
\text{Offline-First Field Appliance}.
$$

本文現在把它具體化。

一台設備要進入 EPCA-2，至少應：

1. 具有至少一組 $\mathrm{LEC}_{\tau}=1$ 的核心任務；
2. 能在 $N=0$ 狀態正常 boot；
3. 不以 remote service 作為核心 execution permission；
4. 本地保存 execution manifest 與 evidence；
5. 在失聯時維持明確 job lifecycle；
6. reconnect 後可同步但不改寫原始 committed result；
7. physical backend identity 在 fallback 時不被靜默冒充。

因此：

$$
\boxed{
\mathrm{EPCA\mbox{-}2}
\Rightarrow
\exists\tau:\mathrm{LEC}_{\tau}=1.
}
$$

---

## 63. EPCA-2 不要求最高 LFA

一台初代產品可以：

$$
\mathrm{EPCA\mbox{-}2}
+
\mathrm{LFA\mbox{-}F2}.
$$

也就是已具 offline execution closure，但還沒有完整的 transactional recovery / independent audit。

後續工程成熟後再推到：

$$
\mathrm{LFA\mbox{-}F4}
$$

或：

$$
\mathrm{LFA\mbox{-}F5}.
$$

這避免把 MVP 一開始就要求成 industrial-grade final system。

---

## 64. 第一代 MVP 的合理邊界

若真的要做第一台 demonstrator，本文建議只要求：

- local display；
- local input；
- embedded Linux；
- one physical backend；
- one deterministic algorithm package format；
- local calibration；
- local evidence；
- Ethernet / Wi-Fi optional；
- signed package update；
- simple rollback；
- network unplug test。

第一代不用：

- fleet-scale cloud；
- AI；
- arbitrary third-party package ecosystem；
- multi-user enterprise identity；
- dozens of physical substrates。

核心是先證明：

$$
\boxed{
\text{拔掉網路，這仍然是一台完整的計算機。}
}
$$

---

## 65. 建議的 Offline Validation Protocol

公開 demonstrator 可以直接做：

### Test 1 — Cold Boot Without Network

$$
N=0
$$

從斷電狀態開機。

### Test 2 — Execute Declared Closed Job

執行：

$$
\tau_{\mathrm{closed}}.
$$

### Test 3 — Mid-Job Network Loss

執行途中：

$$
N:1\rightarrow0.
$$

結果不得改變 physical compute semantics。

### Test 4 — Reconnect Sync

完成多筆離線 job 後：

$$
N:0\rightarrow1.
$$

驗證 evidence sync。

### Test 5 — Interrupted Update

在 stage / trial 階段切斷電源，驗證 rollback / recovery。

### Test 6 — Physical Backend Fault

驗證 fail / degraded / declared fallback，而不是 silent substitution。

---

## 66. Offline-First 對科研可重現性的額外價值

如果一個 result 依賴：

$$
\text{unknown cloud service revision},
$$

數年後可能很難重建。

但若：

$$
R
=
(y,E,M_{\tau}^{(v)}),
$$

且 execution manifest 本地保存，則至少知道：

> 當時到底是由哪一套演算法、backend、calibration、runtime 與 physical state 產生結果。

所以 offline-first 並不只是網路可靠性議題。

它也可以提升：

$$
\boxed{
\text{computational provenance}.
}
$$

---

## 67. Offline-First 對工程維修的額外價值

現場技師真正需要的常常不是：

> 這台設備能不能上網？

而是：

> 我現在能不能得到可信的計算結果？

如果網路壞掉後整台設備失效，工程上的 dependency chain 會變長。

Offline-first 讓：

$$
\text{field mission}
$$

與：

$$
\text{network mission}
$$

分離。

這可以降低單點故障。

---

## 68. 但 Offline-First 也增加責任

本地自治越強，設備本身就必須承擔更多：

- patch management；
- cryptographic verification；
- storage management；
- recovery；
- hardware health；
- evidence integrity；
- local authorization。

所以：

$$
\boxed{
\text{offline autonomy}
\neq
\text{engineering simplicity}.
}
$$

它只是把責任從 cloud dependency 移回 appliance。

---

## 69. 與 Paper 03 的關係

Paper 03 問：

> supervisor 怎麼不偷算？

Paper 04 問：

> supervisor 怎麼在沒有外部服務時仍然是完整 supervisor？

因此：

$$
\boxed{
\text{Authority Separation}
+
\text{Local Execution Closure}
}
$$

才形成真正的 field appliance。

---

## 70. 下一篇接口：Multi-Substrate Compute Backplane

到了 Paper 04，設備已經具備：

- physical core verification；
- supervisor separation；
- local execution closure；
- offline runtime；
- update；
- recovery；
- evidence store。

下一個問題是：

> 如果 physical core 不再只有一種，而是 optical、RF、acoustic、analog、FPGA、CIM 或其他 future substrate 都可以插入，如何讓它們共享同一台 appliance？

Paper 05 將因此處理：

$$
\boxed{
\text{Compute Backplane}
+
\text{Physical Module Contract}
+
\text{Discovery}
+
\text{Capability Descriptor}
+
\text{Isolation}
+
\text{Algorithm Binding}.
}
$$

此時 EPCA 將從：

$$
\text{one appliance}
+
\text{one physical core}
$$

進入：

$$
\boxed{
\text{one appliance}
+
\text{replaceable compute substrates}.
}
$$

---

## 71. 結論：網路應該讓計算機變強，而不是讓計算機獲得存在資格

現代 connected computing 很容易形成一個習慣：

$$
\text{network}
\rightarrow
\text{identity}
\rightarrow
\text{service}
\rightarrow
\text{permission}
\rightarrow
\text{compute}.
$$

這對許多 consumer service 合理。

但對現場工程與科研 appliance，不一定是最佳方向。

本文提出另一個結構：

$$
\boxed{
\text{Local Identity}
+
\text{Local Runtime}
+
\text{Local Algorithm}
+
\text{Local Backend}
+
\text{Local Evidence}
}
$$

先形成：

$$
\boxed{
\text{Local Execution Closure}.
}
$$

然後網路加入：

$$
\text{Update}
+
\text{Sync}
+
\text{Remote Management}
+
\text{Additional Data}
+
\text{AI / Cloud Enhancement}.
$$

因此：

$$
\boxed{
\text{Offline-First}
\neq
\text{Offline-Only}.
}
$$

而是：

$$
\boxed{
\text{Local Compute First, Network Enhancement Second}.
}
$$

當這個原則與 Paper 02 的 physical evidence、Paper 03 的 supervisor authority separation 結合後，EPCA 才真正從一台有趣的 experimental computer，跨成可以帶到現場的 computational appliance。

最簡單的驗收語句仍然是：

$$
\boxed{
\text{拔掉網路，它仍然知道自己是什麼、能算什麼、怎麼算，以及如何證明剛才算過。}
}
$$

---

## 參考文獻與工程資料

1. Canonical. *Ubuntu Core 26*. Released 14 May 2026. Ubuntu Core 26 is described as a minimal, immutable operating system for embedded devices with long-term security maintenance and image lifecycle support. https://documentation.ubuntu.com/core/uc26/
2. Canonical. *Ubuntu Core Release Notes*. Ubuntu Core 26 is the latest stable Ubuntu Core release as of 2026-08-29; essential snaps are managed through snapd and the platform provides recovery and remodeling mechanisms. https://documentation.ubuntu.com/core/reference/release-notes/
3. Canonical. *Recovery modes*. Ubuntu Core provides run, recover, factory-reset and reinstall workflows, allowing a damaged running system to be inspected or restored from a separate recovery environment. https://documentation.ubuntu.com/core/explanation/recovery-modes/
4. Canonical. *Remodel essential snaps*. New essential snaps and recovery systems are tested through boot verification; failed verification aborts the remodel and reverses changes. https://documentation.ubuntu.com/core/explanation/remodel-essential-snaps/
5. RAUC Project. *Using RAUC*. RAUC supports signed update bundles, slot-based deployment and boot success/failure handling for embedded Linux systems. https://rauc.readthedocs.io/en/latest/using.html
6. Mender. *Combining Operating System and Application updates*. Mender documents A/B root filesystem updates in which a new filesystem image is written to the inactive partition, verified, booted and committed after successful first boot. https://docs.mender.io/artifact-creation/combining-system-and-application-updates
7. Mender. *Customize the update process*. Mender exposes rollback states and update state scripts that can be used for integrity checks and recovery behavior. https://docs.mender.io/overview/customize-the-update-process
8. OSTree Project. *Historical OSTree README: Atomic upgrades, rollback*. OSTree describes atomic operating-system tree switching and rollback semantics. https://ostreedev.github.io/ostree/README-historical/
9. The Update Framework. *TUF Specification*, version 1.0.35, 2026-07-15. TUF defines a framework for securing software update systems against classes of repository and metadata attacks. https://github.com/theupdateframework/specification/blob/master/tuf-spec.md
10. Uptane Alliance. *Uptane Standard for Design and Implementation*. Uptane adapts compromise-resilient software update concepts to connected ground vehicles and other constrained or safety-sensitive devices. https://uptane.org/docs/latest/standard/uptane-standard
11. Kuppusamy, T. K., DeLong, L. A., & Cappos, J. (2018). *Uptane: Security and Customizability of Software Updates for Vehicles*. IEEE Vehicular Technology Magazine, 13(1), 66-73. DOI: 10.1109/MVT.2017.2778751.
12. Linux Kernel Documentation. *Watchdog Support*. Hardware/software watchdog infrastructure is one component of system liveness and recovery, but does not replace higher-level job and evidence recovery semantics. https://docs.kernel.org/watchdog/index.html

---

## 前置系列與本系列銜接

- 《跨尺度構成與動態約束域研究》v0.1：有效物理等價、構成復現、可達域與動態約束。
- 《認知功能體的物理實現與自然可觀測性研究》v0.1：存在、可觀測、可辨識與跨 substrate 功能實現。
- Paper 00：EPCA、Local Execution Closure 的初始概念、Physical-Core Non-Substitution 與 Evidence-Bearing Result。
- Paper 01：Carrier-Generalized Abacus、position coding、mode coding、relation coding 與 dynamical geometry。
- Paper 02：OPC-V0 至 OPC-V5、causal intervention、ablation、independent challenge 與 falsifiable physical evidence。
- Paper 03：Application / Real-Time / Fabric / Management / Verification planes、Declared Compute Boundary、No Silent Substitution、Reference-Path Isolation、Evidence Before Refinement 與 ESA-S0 至 ESA-S5。

本篇將 Paper 00 的 Local Execution Closure 從原則提升為完整 deployment contract，並增加 LFA-F0 至 LFA-F5。從這裡開始，EPCA 不再只是「一台物理計算展示機」，而是具有明確 disconnected semantics、update semantics、recovery semantics 與 evidence semantics 的 field computer。下一篇將把這個穩定 appliance substrate 擴展為可容納多種 interchangeable physical compute modules 的 compute backplane。
