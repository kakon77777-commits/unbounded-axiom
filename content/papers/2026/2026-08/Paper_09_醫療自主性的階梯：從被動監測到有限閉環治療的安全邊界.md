# 醫療自主性的階梯：從被動監測到有限閉環治療的安全邊界
## The Ladder of Medical Autonomy

**作者：Neo.K**  
**機構：EveMissLab（一言諾科技有限公司）**  
**系列：資訊優先體內智能與自適應微納系統系列 — Paper 09**  
**版本：Version 1.0 — First Public Edition**  
**日期：2026 年 8 月**

## 摘要

本文提出 Medical Autonomy Ladder（MAL），區分：

$$
\boxed{Automation\neq Adaptation\neq Autonomy}
$$

並以「權限範圍」而不是模型大小或演算法複雜度衡量醫療自主性。

## 1. 四個自主維度

$$
\mathbf A=[A_G,A_I,A_X,A_M]
$$

分別為 Goal Authority、Inference Authority、Action Authority、Modification Authority。

## 2. L0–L7

L0 External Passive Monitoring  
L1 Minimally Invasive Monitoring  
L2 Fixed Distributed In-Body Sensing  
L3 Multimodal Body-State Monitoring  
L4 AI-Assisted Prediction and Decision Support  

$$
\boxed{\text{ACTUATION BOUNDARY}}
$$

L5 Human-Authorized Intervention  
L6 Bounded Closed-Loop Therapy  
L7 Broad Autonomous Therapeutic Agency

## 3. Information Autonomy Domain

L0–L4 可以高度自主地看、整理、預測，但：

$$
\mathcal A=0.
$$

這是一條重要安全斷點。

## 4. L6 與 Authority Envelope

$$
a_t=\pi(S_t)
$$

但只能：

$$
S_t\in\Omega_{approved},\qquad a_t\in A_{approved}.
$$

即：

$$
\mathcal E_A=(\Omega,A,D,T,C).
$$

## 5. Closed Loop 不等於 AI

Controller 可以是 PID、rule-based、MPC 或 ML。因此：

$$
ClosedLoop\neq AI.
$$

模型再大，如果沒有 actuation authority，仍可能只在 L4。

## 6. L7 的質變

L6 目標與 action space 是預先定義的；L7 開始具有更廣泛 goal/strategy/action-selection freedom。真正的問題是 Authority Expansion。

## 7. Dynamic Autonomy

自主性應可降級：

$$
L=L(t)
$$

例如 sensor fault 或 OOD 時：

$$
L_6\rightarrow L_4.
$$

高不確定性應收縮 action space：

$$
U\uparrow\Rightarrow Authority\downarrow.
$$

## 8. Minimum Necessary Autonomy

$$
L^*
=
\min\{L:ClinicalUtility(L)\geq U_{required}\}
$$

不是最大化 autonomy，而是使用能完成任務的最低必要自主性。

## 9. Physical Scale 與 Autonomy 分離

$$
\boxed{PhysicalScale\perp AutonomyLevel}
$$

納米機器可以完全被動；大型設備也可以高度自主。

## 結論

合理的自主醫療不是「能自動化多少」，而是「需要自動化多少」。能用資訊解決就停在資訊；需要人工授權就停在 L5；只有在明確 bounded domain 中才跨入 L6。L7 是警戒線，不是必然終點。
