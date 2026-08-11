# 多模態生理狀態機：事件驅動式體內監測與 AI 協同架構
## Multimodal Physiological State Machines

**作者：Neo.K**  
**機構：EveMissLab（一言諾科技有限公司）**  
**系列：資訊優先體內智能與自適應微納系統系列 — Paper 04**  
**版本：Version 1.0 — First Public Edition**  
**日期：2026 年 8 月**

## 摘要

連續感測不等於連續高成本推理。本文提出 Multimodal Physiological State Machine（MPSM）：

$$
\boxed{
Sensing\rightarrow State\rightarrow Event\rightarrow Inference
}
$$

而不是：

$$
Sensing\rightarrow AlwaysOnLargeAI.
$$

## 1. 狀態流

對節點：

$$
q_i(t)\in\{Normal,Watch,Anomaly,Urgent,Fault,Unknown\}
$$

更新：

$$
q_i(t+1)=F_i[q_i(t),X_i(t),\Delta X_i(t),C_i(t)]
$$

狀態機的任務不是診斷，而是 Attention Allocation。

## 2. 六層架構

- L0 Physical Sensing
- L1 Signal Conditioning
- L2 Local State Machine
- L3 Event Fusion
- L4 Edge AI
- L5 Medical Reasoning

即：

$$
Sensor\rightarrow State\rightarrow Event\rightarrow EdgeAI\rightarrow MedicalAI.
$$

## 3. 個人基線

$$
z_i(t)=\frac{x_i(t)-\mu_i}{\sigma_i}
$$

人口正常不等於個人正常：

$$
\boxed{PopulationNormal\neq PersonalNormal}
$$

## 4. Event-Driven AI

若事件：

$$
e_t\in\{0,1\}
$$

則高階模型只在 $e_t=1$ 時執行：

$$
C=C_{low}+P(e=1)C_{high}.
$$

## 5. Adaptive Sampling

$$
r(t)=f\left(\left|\frac{dx}{dt}\right|\right)
$$

穩定時低頻，異常時升高 sampling、storage 與 inference。

## 6. 多模態融合

$$
E(t)=G(q_1,\dots,q_n,C(t))
$$

單一弱訊號可能無意義，但跨模態共同偏移可形成強事件。

## 7. 雙軌事件

$$
E=E_{bio}\cup E_{device}
$$

sensor anomaly 不等於 physiological anomaly。

## 8. AI 自身也要有狀態

$$
q_{AI}\in\{Validated,LowConfidence,OOD,Unavailable,Outdated\}
$$

低信心或 OOD 應允許 Unknown/Escalate。

## 9. 多解析度記憶

- Raw Short Buffer
- Event Windows
- Daily Statistics
- Long-Term Trajectories
- Clinical Events

因此：

$$
\boxed{ContinuousAwareness\neq ContinuousHeavyAI}
$$

## 結論

人體大部分時間不需要最高成本推理。合理架構是讓正常狀態保持便宜，只有真正值得注意的變化才得到更多 sampling、memory、communication 與 intelligence。
