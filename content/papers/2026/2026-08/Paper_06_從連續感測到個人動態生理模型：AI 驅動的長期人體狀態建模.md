# 從連續感測到個人動態生理模型：AI 驅動的長期人體狀態建模
## From Continuous Sensing to Personal Dynamic Physiology Models

**作者：Neo.K**  
**機構：EveMissLab（一言諾科技有限公司）**  
**系列：資訊優先體內智能與自適應微納系統系列 — Paper 06**  
**版本：Version 1.0 — First Public Edition**  
**日期：2026 年 8 月**

## 摘要

本文提出 Personal Dynamic Physiology Model（PDPM），作為連續生理資料與完整 Human Digital Twin 之間的保守中間層：

$$
\boxed{
Measurement\neq State\neq Trajectory\neq Counterfactual\neq DigitalTwin
}
$$

PDPM 不宣稱複製完整人體，而是持續估計有限醫療問題下的個體狀態及其演化。

## 1. 部分可觀測

人體真實狀態：

$$
S(t)
$$

感測值：

$$
Y(t)=H(S(t),D(t))+\epsilon(t)
$$

而通常：

$$
n_{observed}\ll m_{true}.
$$

所以需要：

$$
\hat S(t)=P(S(t)\mid Y_{0:t}).
$$

## 2. PDPM 定義

$$
\mathcal P=(Y,D,B,C,E,\hat S,T,U)
$$

分別表示 observation、device reliability、baseline、context、event memory、latent state、transition model 與 uncertainty。

## 3. 為什麼不直接叫 Digital Twin

完整 digital twin 至少要求 patient specificity、dynamic updating、prediction、validation、uncertainty quantification，若聲稱 intervention 還需要更高 causal evidence。

因此：

$$
\boxed{PDPM\subseteq PossibleFutureDigitalTwinArchitecture}
$$

但不等同完整 twin。

## 4. 七層架構

Observation → Data Reliability → Personal Baseline → Event Memory → Latent State → Trajectory → Clinical Interpretation。

## 5. 個人基線

$$
B=P(X\mid Context)
$$

而且：

$$
B=B(t).
$$

需同時保留 short-term 與 long-term baseline，避免慢性惡化被「新正常」吞掉。

## 6. Model-of-Models

$$
PDPM=\mathcal M_1\oplus\cdots\oplus \mathcal M_k
$$

例如 cardiac、metabolic、sleep、activity，再由 global model 處理跨域耦合。

## 7. Population Prior + Personal Evidence

$$
P(S_i|Y_i)\propto P(Y_i|S_i)P_{pop}(S_i)
$$

個人資料逐漸增加時，模型越來越 individualized，但人口證據仍不能被單一人的歷史取代。

## 8. Prediction 與 Counterfactual 分離

$$
P(S(t+\tau)\mid History)
$$

不同於：

$$
P(S(t+\tau)\mid do(a)).
$$

能預測不等於能可靠回答「若改治療會怎樣」。

## 9. 成熟度階梯

P0 Longitudinal Record  
P1 Dynamic Baseline  
P2 State Estimator  
P3 Trajectory Predictor  
P4 Conditional Scenario Model  
P5 Validated Counterfactual Model  
P6 Clinical Digital Twin  
P7 Closed-Loop Twin

且：

$$
P_n\nRightarrow P_{n+1}.
$$

## 10. Observed / Estimated / Predicted

資料必須標明 provenance：

$$
I\in\{Observed,Derived,Estimated,Predicted,Counterfactual\}.
$$

避免把模型推測畫成已測得事實。

## 結論

醫療真正需要的可能不是「電腦裡另一個完整的我」，而是一個知道自己知道什麼、不知道什麼，並能隨可信證據逐步更新的個人生理模型。
