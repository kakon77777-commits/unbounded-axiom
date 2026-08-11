# 唯讀植入式架構：醫療智能系統中的知、判、授權與行分離原則
## Read-Only Implant Architecture: Separation of Sensing, Inference, Authorization and Action

**作者：Neo.K**  
**機構：EveMissLab（一言諾科技有限公司）**  
**系列：資訊優先體內智能與自適應微納系統系列 — Paper 03**  
**版本：Version 1.0 — First Public Edition**  
**日期：2026 年 8 月**

## 摘要

本文提出 Read-Only Implant Architecture（ROIA）與知—判—授權—行分離。核心為：

$$
\boxed{\text{Know}\neq\text{Infer}\neq\text{Authorize}\neq\text{Act}}
$$

「唯讀」不是不能校準或更新，而是沒有直接改變宿主生理狀態的 therapeutic actuator。

## 1. 四種權限

知：

$$
\mathcal K:\mathcal B(t)\rightarrow Y(t)
$$

判：

$$
\mathcal J:Y(t-\tau:t)\rightarrow P(H_k)
$$

授權：

$$
\mathcal U:(\hat H,a^*,C,R)\rightarrow\{Allow,Deny,Escalate\}
$$

行：

$$
\mathcal A:\mathcal B(t)\rightarrow\mathcal B(t+1)
$$

關鍵：

$$
\boxed{\mathcal K\nRightarrow\mathcal J\nRightarrow\mathcal U\nRightarrow\mathcal A}
$$

## 2. ROIA

若：

$$
A_i=\varnothing
$$

則體內節點可以 sensing、通信、校準與維護，但沒有 therapeutic authority。

ROIA 是：

$$
\boxed{\text{Read-Only with respect to host physiology}}
$$

而非 Read-Only Memory。

## 3. 資訊平面與治療平面

$$
\mathcal P_{info}\neq\mathcal P_{ther}
$$

兩者間必須有 Authorization Boundary。

目的不是假設每層不犯錯，而是：

$$
\boxed{\text{Prevent one error from automatically inheriting all downstream authority}}
$$

## 4. 三種授權模式

- U0：No Therapeutic Authority
- U1：Human-Authorized Action
- U2：Preauthorized Bounded Closed Loop

對 U2 定義 Authority Envelope：

$$
\mathcal E_A=(\Omega,A,D,T,C)
$$

只有：

$$
a_t\in\mathcal E_A
$$

才能執行。

## 5. 模型能力與權限分離

$$
\boxed{ModelUpgrade\nRightarrow AuthorityUpgrade}
$$

AI 可以改善，但不能因為更準就自行增加治療範圍。

## 6. Safety Controller

主模型：

$$
M:X\rightarrow H
$$

安全控制：

$$
G:(H,C,D,A)\rightarrow\{Allow,Block,Escalate\}
$$

提出行動的智能，不應必然是唯一驗證該行動的權威。

## 7. 最小醫療權限

$$
Privilege(N_i)=Minimum(Function_i)
$$

命令分為 Read、Configuration、Maintenance、Therapeutic Control；ROIA 允許前三者，但 therapeutic control 為空。

## 結論

AI 能力不等於醫療權限：

$$
\boxed{AI\ Capability\neq Medical\ Authority}
$$

最安全的智能有時正是「知道很多，但被刻意設計成不能直接動手」。
