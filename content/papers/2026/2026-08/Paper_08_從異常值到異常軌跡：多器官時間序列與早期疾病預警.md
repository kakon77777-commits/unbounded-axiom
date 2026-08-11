# 從異常值到異常軌跡：多器官時間序列與早期疾病預警
## From Abnormal Values to Abnormal Trajectories

**作者：Neo.K**  
**機構：EveMissLab（一言諾科技有限公司）**  
**系列：資訊優先體內智能與自適應微納系統系列 — Paper 08**  
**版本：Version 1.0 — First Public Edition**  
**日期：2026 年 8 月**

## 摘要

傳統異常判定：

$$
x(t)>\theta
$$

主要回答「現在是否越界」。本文提出 Multiscale Disease Trajectory Warning Framework（MDTW），把疾病預警擴展為長期漂移、速度、加速度、變點、跨模態耦合、恢復失敗與多時間尺度風險。

核心區分：

$$
\boxed{
PreclinicalSignal\neq RiskPrediction\neq EarlyDetection\neq ActionableWarning\neq ImprovedOutcome
}
$$

## 1. 值與軌跡

即使：

$$
x_A(t)=x_B(t)
$$

若過去路徑不同，臨床意義也可能不同。

因此：

$$
Value(t)\neq Trajectory(t).
$$

## 2. 三至四類異常

Type I Level Anomaly  
Type II Dynamic Anomaly  
Type III Structural Anomaly  
Type IV Relational Anomaly

例如：

$$
C_{12}(t)=Corr(x_1,x_2)
$$

改變，即使單一訊號仍「正常」，系統關係也可能已偏移。

## 3. 疾病不是二態

$$
Baseline\rightarrow Drift\rightarrow CompensatedChange\rightarrow Prodromal\rightarrow ClinicalDisease.
$$

但 Prediagnostic Association 不等於 confirmed preclinical pathology。

## 4. Prediction Horizon

所有風險應寫成：

$$
P(E\ within\ \tau\mid History)
$$

而不是沒有時間窗的單一 risk score。

越早：

$$
LeadTime\uparrow
$$

通常也伴隨：

$$
Uncertainty\uparrow.
$$

## 5. 最佳預警時間

$$
\tau^*
=
\arg\max_\tau[
ClinicalUtility(\tau)-Uncertainty(\tau)-FalseAlarmCost(\tau)
$$

因此不是越早越好。

## 6. Change-Point Detection

$$
P(x|t<t_c)\neq P(x|t>t_c)
$$

表示系統在 $t_c$ 後不再像以前。但 change point 本身不是疾病，只是值得升級觀測的 event。

## 7. 多模態與 Incremental Value

多模態不是自動優於單模態。新增模態必須證明：

$$
\Delta Performance,\quad \Delta Calibration,\quad \Delta Utility.
$$

## 8. Warning Ladder

W0 Stable  
W1 Trajectory Drift  
W2 Persistent Multimodal Change  
W3 Elevated Clinical Risk  
W4 Actionable Clinical Warning

低階事件可以只由系統記錄，不必全部通知患者。

## 9. Actionability

$$
A(E)=\text{availability of a useful response to the warning}
$$

所以：

$$
PredictionAccuracy\neq ClinicalActionability.
$$

## 10. Multi-Horizon Risk

$$
\mathbf R(t)=
[R_{1h},R_{24h},R_{7d},R_{1y},R_{5y}]
$$

風險本身也是一條 trajectory：

$$
R=R(t,\tau).
$$

## 結論

真正需要預警的不一定是「數值已經壞掉」，而可能是「人體正在用以前沒出現過的方式改變」。安全的預警必須同時帶風險、時間窗、不確定性、證據來源與可行動性。
