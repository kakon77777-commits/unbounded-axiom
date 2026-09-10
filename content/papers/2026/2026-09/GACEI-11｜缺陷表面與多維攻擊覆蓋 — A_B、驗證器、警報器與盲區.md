---
title: "GACEI-11｜缺陷表面與多維攻擊覆蓋：A/B、驗證器、警報器與盲區"
title_en: "GACEI-11 | Defect Surfaces and Multidimensional Adversarial Coverage: A/B Observation, Validators, Alarms, and Blind Spots"
series: "全域對抗計算與 AI 工程智能系列"
series_en: "Global Adversarial Computation and AI Engineering Intelligence Series"
series_id: "GACEI-2026"
paper_id: "GACEI-11"
version: "v0.1"
date: "2026-09-08"
language: "zh-Hant"
author: "Neo.K"
organization: "EveMissLab / 一言諾科技有限公司"
document_type: "研究論文 / 缺陷量測 / 多維覆蓋 / 驗證與警報"
status: "Canonical Draft"
canonical_source: "UTF-8 Markdown"
math_source_rule: "inline math only $...$ ; display math only $$...$$"
security_scope: "Authorized, isolated, recoverable software testing and simulation only"
depends_on:
  - "GACEI-01 全域對抗計算總論 v0.1"
  - "GACEI-02 MSSP 的對偶 v0.1"
  - "GACEI-03 局部攻擊抽象論 v0.1"
  - "GACEI-04 對抗記憶基底 v0.1"
  - "GACEI-05 全域攻擊組合代數 v0.1"
  - "GACEI-06 全域攻擊壓縮 v0.1"
  - "GACEI-07 一眼理解專案 v0.1"
  - "GACEI-08 工程理解不是摘要 v0.1"
  - "GACEI-09 對抗性創造與生成 v0.1"
  - "GACEI-10 全域攻擊的計算理論 v0.1"
  - "DEST-01 多域知識判定論"
  - "DEST-02 多維知識覆蓋論"
---

# GACEI-11｜缺陷表面與多維攻擊覆蓋
## A/B、驗證器、警報器與盲區

## 摘要

GACEI-01 至 GACEI-10 已回答全域對抗計算的注意力、理解、創造、記憶、組合、壓縮與算力配置，但仍缺少最後一個量測核心：**全域 attack 跑完之後，我們到底知道了什麼？**

如果系統只輸出：

```text
PASS
FAIL
47/47
93%
NO BLOCKER
```

則大量重要資訊仍可能被壓掉。例如：product 真的壞了但 alarm 沒響；alarm 響了但 product 沒壞；validator 過期；attack 根本沒有成功施加；環境不支援而只是 NotMeasured；coverage 很高但沒有 interaction coverage；系統知道紅了卻完全無法定位原因。

本文提出「缺陷表面與多維對抗覆蓋」（Defect Surface and Multidimensional Adversarial Coverage, DSMAC），核心區分：

$$
\boxed{
\text{Defect}
\neq
\text{Detectability}
\neq
\text{Diagnosability}
\neq
\text{Coverage}.
}
$$

在固定 baseline：

$$
S^\ast
$$

上建立 control observation：

$$
O_0=\operatorname{Observe}(S^\ast),
$$

再對 global campaign $\mathcal C$ 建立：

$$
O_1=\operatorname{Observe}(\mathcal C(S^\ast)).
$$

由此定義：

$$
\boxed{
\Delta_G=\operatorname{Diff}(O_0,O_1)
}
$$

為 Global Defect Surface 的第一版操作性表示。若 observation space 可量化，可使用：

$$
\Delta_G=d(O_0,O_1),
$$

但本文不要求所有缺陷表面都可被單一距離無損表達。

本文將缺陷表面拆成：

$$
\boxed{
\Delta_G=
(
\Delta_B,
\Delta_X,
\Delta_R,
\Delta_S,
\Delta_T,
\Delta_A,
\Delta_{Rec},
\Delta_O
),
}
$$

分別表示 behavior、state、relation、semantic、temporal、authority、recovery 與 observability。

令：

$$
D(a)\in\{0,1\}
$$

表示 attack $a$ 是否真的造成目標 defect，

$$
L(a)\in\{0,1\}
$$

表示 alarm 是否發出預期訊號，則：

| 實際缺陷 | Alarm | 判定 |
|---|---|---|
| 1 | 1 | True Positive |
| 1 | 0 | Blind Spot / False Negative |
| 0 | 1 | False Positive |
| 0 | 0 | True Negative |

其中：

$$
\boxed{
D=1,\quad L=0
}
$$

是最值得研究的 Adversarial Blind Spot：系統真的失敗，但驗證與警報體系沒有看見。

本文另加入 attack application 狀態：

$$
A_p\in\{
Applied,
NotApplied,
Partial,
Unknown
\},
$$

以及 measurement 狀態：

$$
M\in\{
Measured,
NotMeasured,
Unknown
\}.
$$

因此：

$$
\boxed{
NotMeasured\neq Pass,
\qquad
NotApplied\neq NoDefect.
}
$$

承接 DEST-02，本文定義：

$$
\boxed{
\boldsymbol\rho_A
=
(
\rho_N,
\rho_R,
\rho_\Theta,
\rho_P,
\rho_I,
\rho_V,
\rho_{Rec},
\rho_T
),
}
$$

分別描述 component、relation、condition、path、interaction、validator、recovery 與 time/version coverage。

本文強調：

$$
\boxed{
Coverage
\neq
Correctness
\neq
Safety.
}
$$

coverage 只回答在明示 reference frame 下測到了哪些工程對象與義務，不能單獨推出沒有未知缺陷。

本文進一步提出三個品質量：

$$
\boxed{
Q_D=\text{Defect Detection Quality},
}
$$

$$
\boxed{
Q_L=\text{Localization / Diagnosability Quality},
}
$$

$$
\boxed{
Q_C=\text{Coverage Quality}.
}
$$

一個 campaign 可以 $Q_C$ 很高但 $Q_D$ 很低：測很多但 validator 很弱；也可以 $Q_D$ 很高但 $Q_L$ 很低：知道紅了卻不知道為什麼紅。

本文最後提出 Defect Surface Certificate，將 baseline、campaign、reference frame、attack application、A/B observations、validator、alarm、blind spots、false positives、NotMeasured、Unknown、localization、coverage vector 與 residual gaps 綁成可重播的工程證據物件。

本文核心結論是：

$$
\boxed{
\text{Global attack value}
\neq
\text{number of red lights}.
}
$$

真正重要的是：

$$
\boxed{
\text{What broke}
+
\text{Whether we saw it}
+
\text{Whether we understood it}
+
\text{What we did not measure}.
}
$$

**關鍵詞：** Defect Surface、A/B Observation、Validator、Alarm、Blind Spot、False Positive、False Negative、NotMeasured、Multidimensional Coverage、Diagnosability、GACEI

---

# 0. 研究定位與安全範圍

本文只處理：

$$
\boxed{
\text{authorized software test measurement and validation}.
}
$$

所有 attack / perturbation 僅作用於 sandbox、synthetic fixture、isolated clone、internal test runtime 與 authorized project。

---

# 1. PASS / FAIL 為什麼太粗？

若：

$$
V(a)=FAIL,
$$

可能代表：

- product defect；
- harness defect；
- validator defect；
- environment mismatch；
- partial application；
- stale baseline；
- unsupported platform。

因此：

$$
\boxed{
FAIL\neq\text{Unique Meaning}.
}
$$

反過來：

$$
V(a)=PASS
$$

也可能是 attack 沒真正施加、validator 太弱、observation 沒看到、版本不對或 precondition 不成立。

所以：

$$
\boxed{
PASS\neq\text{Proof of No Defect}.
}
$$

---

# 2. Baseline-Controlled Observation

令：

$$
S^\ast
$$

為固定 baseline。

control：

$$
O_0=\operatorname{Observe}(S^\ast).
$$

adversarial：

$$
O_1=\operatorname{Observe}(\mathcal C(S^\ast)).
$$

定義：

$$
\boxed{
\Delta_G=\operatorname{Diff}(O_0,O_1).
}
$$

這建立同 baseline 的比較基礎。

---

# 3. 八維缺陷表面

$$
\boxed{
\Delta_G=
(
\Delta_B,
\Delta_X,
\Delta_R,
\Delta_S,
\Delta_T,
\Delta_A,
\Delta_{Rec},
\Delta_O
).
}
$$

## 3.1 Behavior

錯誤輸出、缺失輸出、重複輸出、invalid response。

## 3.2 State

stale state、lost update、replica divergence、wrong owner mutation。

## 3.3 Relation

forbidden dependency、hidden coupling、wrong routing、broken handoff。

## 3.4 Semantic

contract mismatch、silent loss、wrong equivalence、wrong interpretation。

## 3.5 Temporal

race、wrong order、retry anomaly、timeout drift、replay。

## 3.6 Authority

unauthorized mutation、scope widening、authority confusion。

## 3.7 Recovery

restart divergence、rollback mismatch、incomplete compensation、non-idempotent retry。

## 3.8 Observability

product broken but no log、validator blind、alarm suppressed、evidence bound to wrong version。

---

# 4. Magnitude 不等於 Severity

某一維度可以定義：

$$
m_i=d_i(O_{0,i},O_{1,i}),
$$

但 severity 還需要：

$$
Severity=f(
Impact,
Scope,
Persistence,
Recoverability,
UserHarm,
BusinessCriticality
).
$$

因此一個很小的 state delta 仍可能是嚴重 authority failure。

---

# 5. Detectability

定義：

$$
Det(a)
=
P(
Alarm=1
\mid
Defect=1,
a,\theta
).
$$

False positive rate：

$$
FPR=P(Alarm=1\mid Defect=0).
$$

False negative rate：

$$
FNR=P(Alarm=0\mid Defect=1).
$$

---

# 6. Blind Spot

若：

$$
Defect=1
$$

且：

$$
Alarm=0,
$$

則：

$$
\boxed{
\text{Blind Spot}.
}
$$

它比普通 defect 更危險的情況在於：

> 系統壞了，而且自己的驗證體系不知道。

---

# 7. Validator 與 Alarm 必須分離

令：

$$
V(a)
$$

為 validator judgment，

$$
L(a)
$$

為 alarm emission。

可以：

$$
V=Reject
$$

但：

$$
L=0.
$$

這表示 alarm pipeline 本身有 defect。

完整 detection chain：

$$
\boxed{
Defect
\rightarrow
Observation
\rightarrow
Validator
\rightarrow
Alarm
\rightarrow
Notification
\rightarrow
Decision.
}
$$

任一層都可能失敗。

---

# 8. Attack Application State

$$
A_p\in
\{
Applied,
NotApplied,
Partial,
Unknown
\}.
$$

`Applied` 表示 attack 已確實作用於目標 baseline；`NotApplied` 表示未成功施加；`Partial` 表示只有部分 mutation；`Unknown` 表示無足夠 evidence 確認。

因此：

$$
\boxed{
NotApplied\neq NoDefect.
}
$$

---

# 9. Measurement State

$$
M\in
\{
Measured,
NotMeasured,
Unknown
\}.
$$

其中：

$$
\boxed{
NotMeasured\neq Fail,
\qquad
NotMeasured\neq Pass.
}
$$

`NotMeasured` 是明確知道沒有測；`Unknown` 是不知道是否測到或 evidence 不足。

---

# 10. Outcome Classification

至少區分：

$$
Outcome\in
\{
ProductDefect,
HarnessDefect,
ValidatorDefect,
PlatformUnsupported,
EnvironmentFailure,
NotMeasured,
Unknown
\}.
$$

例如 Windows-specific 測試在 Linux 不成立，應更傾向標記 `NotMeasured` / `PlatformUnsupported`，而不是直接說產品 fail。

---

# 11. A/B 與 A/B/AB

單 attack：

$$
A:S^\ast,
$$

$$
B:a(S^\ast).
$$

比較：

$$
\Delta(a)=\operatorname{Diff}(A,B).
$$

interaction attack 則另取：

$$
AB:(a\odot b)(S^\ast).
$$

比較 $A$ 、 $B$ 與 $AB$，可以估計 interaction-specific residual：

$$
\Delta_{AB}
=
O_{AB}
-
\widehat F(O_A,O_B).
$$

其中 $\widehat F$ 是若兩者只有獨立效果時的預期組合結果。

---

# 12. Validator Drift

validator：

$$
V_t
$$

可能對：

$$
S_t
$$

有效，但對：

$$
S_{t+1}
$$

已經過期。

因此：

$$
V=V(\theta,version).
$$

若：

$$
\Delta Version>\tau,
$$

要求：

$$
Revalidate(V).
$$

alarm threshold 也可能 drift。

---

# 13. Detection Quality

定義：

$$
\boxed{
Q_D
=
f(
TPR,
TNR,
FPR,
FNR,
Calibration,
VersionFit
).
}
$$

這表示 validator / alarm 的品質必須與 product defect 數量分開評價。

---

# 14. Diagnosability

被偵測後，還要問：

> 能不能知道為什麼？

令：

$$
\Pi:
Evidence\rightarrow CandidateCauses.
$$

可以用 localization accuracy、counterfactual replay、causal support 與 diagnostic information gain 評估。

概念上：

$$
IG_D
=
H(Cause)-H(Cause\mid Evidence).
$$

因此：

$$
\boxed{
Q_L
=
f(
LocalizationAccuracy,
DiagnosticIG,
Replayability,
CausalSupport
).
}
$$

一個系統可以非常會叫警報，但完全不知道 root cause。

---

# 15. 多維對抗 Coverage

本文定義：

$$
\boxed{
\boldsymbol\rho_A
=
(
\rho_N,
\rho_R,
\rho_\Theta,
\rho_P,
\rho_I,
\rho_V,
\rho_{Rec},
\rho_T
).
}
$$

其中：

- $\rho_N$：component / node；
- $\rho_R$：relation；
- $\rho_\Theta$：condition；
- $\rho_P$：path；
- $\rho_I$：interaction；
- $\rho_V$：validator / detection；
- $\rho_{Rec}$：recovery；
- $\rho_T$：time / version。

---

# 16. Coverage Reference Frame

完整 coverage claim 必須綁定：

$$
\mathfrak F_C
=
(
U,
\Theta,
\mu,
Version,
Validator,
History
).
$$

沒有 reference frame 的單一「93%」沒有穩定工程語義。

---

# 17. Open Denominator

新 attack family、版本或 validator blind spot 出現時：

$$
U_t\rightarrow U_{t+1}.
$$

即使 covered mass 增加，相對 coverage ratio 仍可能下降。

所以：

$$
\boxed{
\text{Absolute Coverage Gain}
\neq
\text{Relative Coverage Gain}.
}
$$

---

# 18. Coverage Quality

定義：

$$
\boxed{
Q_C
=
f(
Breadth,
Depth,
Balance,
ReferenceFrameQuality,
ResidualHonesty
).
}
$$

Breadth 看跨多少 dimension；Depth 看每個 dimension 測多深；Balance 看是否有短板；ReferenceFrameQuality 看分母是否明確；ResidualHonesty 看是否誠實列出 Unknown、NotMeasured、Deferred。

---

# 19. Worst-Dimension Risk

即使：

$$
\bar\rho=0.95,
$$

但：

$$
\rho_V=0.2,
$$

仍可能有嚴重 blind spot。

因此可要求：

$$
\min_j\rho_j\ge\tau_j.
$$

---

# 20. Weighted Coverage

可定義：

$$
\rho_w
=
\frac{
\sum_i w_i Covered_i
}{
\sum_i w_i
}.
$$

但 weighted score 不能取代 vector，因為 weight design 本身可能有爭議。

---

# 21. Coverage、Correctness、Safety 三分

$$
\boxed{
Coverage\neq Correctness\neq Safety.
}
$$

coverage 回答「測了多少與測了什麼」；correctness 回答「目前 evidence 是否支持 contract」；safety 還涉及未建模世界、操作條件與 residual risk。

---

# 22. 三個表面

對每個 coverage unit $u$，可以建立：

$$
Severity(u),
$$

$$
Detectability(u),
$$

$$
Diagnosability(u).
$$

因此：

$$
\boxed{
\mathcal S_F
=
(
SeverityField,
DetectabilityField,
DiagnosabilityField
).
}
$$

最危險區域是：

$$
Severity\uparrow,
\qquad
Detectability\downarrow,
\qquad
Diagnosability\downarrow.
$$

---

# 23. Blind-Spot Risk

可定義：

$$
BR(u)
=
Severity(u)
\cdot
P(Defect_u)
\cdot
(1-Detectability(u)).
$$

再加 diagnosability：

$$
DR(u)
=
BR(u)
\cdot
(1-Diagnosability(u)).
$$

這可以直接回饋 GACEI-10 的下一輪資源配置。

---

# 24. Validation Debt

定義：

$$
D_V
=
D_{\mathrm{unmeasured}}
+
D_{\mathrm{weak-validator}}
+
D_{\mathrm{stale}}
+
D_{\mathrm{unknown}}
+
D_{\mathrm{blind}}.
$$

Coverage debt：

$$
D_C
=
D_N+D_R+D_\Theta+D_P+D_I+D_V+D_{Rec}+D_T.
$$

Debt 不自動等於 release blocker；只有與 critical claim 相交時才必須阻擋。

---

# 25. Claim Scope

一個 release / assurance claim 應表示為：

$$
Claim
=
(
Scope,
Version,
Environment,
Coverage,
Evidence,
Residual
).
$$

而不是無條件說：

> 系統安全。

---

# 26. Evidence-Claim Binding

每個 claim 必須能回到：

$$
Evidence.
$$

`54/54 passed` 只能支持它明示的那一層 denominator，不能推出「everything passed」。

---

# 27. Denominator Integrity

不同 evidence layers 應保留分層 denominator，例如：

```yaml
behavioral: 54/54
structural: 47/47
acceptance: 40/40
adversarial_controls: 11/11
```

把它們直接壓成一個總數可能丟失 layer semantics。

---

# 28. A/B Validity

A 與 B 必須盡量滿足：

- same baseline；
- same relevant config；
- same version；
- same observation protocol。

否則 $\Delta$ 可能被 confound。

---

# 29. Reproducibility

若同 attack 重跑 $n$ 次，定義：

$$
RR(a)
=
\frac{
N_{\mathrm{reproduced}}
}{
N_{\mathrm{attempts}}
}.
$$

stochastic defect 的 reproduction rate 可以低，但不代表它是假的；race condition 本來就可能是概率性。

---

# 30. Detection Calibration

如果 validator confidence 為 $p$，實際 correctness 應與 $p$ 大致相容。可建立 calibration error，而不是把 confidence 當真值。

---

# 31. Alarm Threshold Frontier

threshold 太低：

$$
FPR\uparrow.
$$

threshold 太高：

$$
FNR\uparrow.
$$

因此存在 precision-recall / sensitivity-specificity trade-off，不同 assurance profile 可有不同 threshold。

---

# 32. Blind-Spot Discovery Test

有些 attack 不是測 product，而是測：

$$
\boxed{
\text{Can the validator notice a known-bad state?}
}
$$

至少保留：

$$
w^-
$$

與：

$$
w^+,
$$

要求：

$$
V(w^-)=Reject,
$$

$$
V(w^+)=Accept.
$$

若 policy 要求告警，還應：

$$
Alarm(w^-)=1.
$$

---

# 33. Meta-Verification Stop

不應：

$$
V
\rightarrow
V(V)
\rightarrow
V(V(V))
\rightarrow
\infty.
$$

最低 discriminative evidence 足夠後，除非 validator、claim、risk 或 evidence 發生重大變化，否則停止。

---

# 34. Defect Surface Certificate

本文提出：

```yaml
defect_surface_certificate:
  baseline:
  campaign_id:
  reference_frame:
  control_observation:
  adversarial_observation:
  attack_application_status:
  defect_surface:
  validator_results:
  alarm_results:
  notification_results:
  true_positives:
  blind_spots:
  false_positives:
  true_negatives:
  not_measured:
  unknown:
  localization:
  coverage_vector:
  severity_field:
  detectability_field:
  diagnosability_field:
  residual_gaps:
  validation_debt:
  version:
  provenance:
```

它不是安全證書，而是：

$$
\boxed{
\text{Evidence-Bearing Measurement Object}.
}
$$

---

# 35. Cross-Version Comparison

若：

$$
S_t\rightarrow S_{t+1},
$$

可以比較：

$$
\Delta_G^{(t)}
$$

與：

$$
\Delta_G^{(t+1)}.
$$

但 defect reduction、coverage improvement、detectability improvement、diagnosability improvement 必須分開描述。

---

# 36. Repair Evaluation

repair 後可能：

$$
Defect\downarrow
$$

但：

$$
FPR\uparrow.
$$

也就是產品改善但 monitoring 變吵。兩者都應保存。

---

# 37. Goodhart Risk

若團隊只追：

$$
\text{green count}
$$

或：

$$
\text{coverage percent},
$$

容易造成 metric optimization。

因此多維 vector 與 residual honesty 比單一 KPI 更安全。

---

# 38. MSSP Overlay

MSSP 可把 defect surface 回投：

- TMS；
- relation；
- boundary；
- state；
- invariant。

並建立 tested / failed / blind / NotMeasured / unknown overlay。

但 heatmap 只是 projection，不能取代 canonical evidence。

---

# 39. 與 GACEI-07、09、10 的閉環

GACEI-07 的 attention 可根據 BlindSpotRisk 重新配置 observation。

GACEI-09 可對 residual + blind spot 生成新的 attack hypothesis。

GACEI-10 可根據 diagnostic risk 提高 verification budget。

因此：

$$
\boxed{
Attack
\rightarrow
DefectSurface
\rightarrow
BlindSpot
\rightarrow
NewAttention
\rightarrow
NewAttack
\rightarrow
Memory.
}
$$

每輪仍必須有 budget 與 stop。

---

# 40. Benchmark

建立 synthetic projects，注入：

1. visible defect；
2. hidden defect；
3. false alarm；
4. stale validator；
5. NotMeasured platform；
6. interaction defect；
7. localization ambiguity。

比較：

### A：Pass/Fail Only

只輸出紅綠。

### B：Coverage Only

只輸出 coverage。

### C：Detection Matrix

加入 TP/FP/FN/TN。

### D：DSMAC

完整 defect surface + detection + diagnosis + multidimensional coverage。

測量：

$$
DefectRecall,
$$

$$
BlindSpotRecall,
$$

$$
FalsePositiveRate,
$$

$$
LocalizationAccuracy,
$$

$$
CoverageCalibration,
$$

$$
ResidualHonesty,
$$

$$
DecisionQuality.
$$

最終關心：

> 哪一種 representation 能讓 release / repair / defer 決策更正確？

---

# 41. 研究假說

## H1：DSMAC 比單一 pass/fail 更能預測 release risk

$$
PredictivePower_{DSMAC}
>
PredictivePower_{binary}.
$$

## H2：顯式 blind-spot testing 可降低 false-green rate

$$
FalseGreen\downarrow.
$$

## H3：Multidimensional coverage 可降低 denominator collapse

$$
CoverageMisinterpretation\downarrow.
$$

## H4：Diagnosability-aware campaign 可降低 unattributable red

$$
UnattributableRed\downarrow.
$$

## H5：Residual honesty 可降低過度自信

明示 Unknown / NotMeasured 的系統，其 post-release surprise 應較低。

---

# 42. 本文非主張

本文不主張：

1. 所有 defect 都可用單一距離量化；
2. A/B 可以解決所有因果問題；
3. alarm 沒響就一定是 validator defect；
4. coverage 高等於 safety；
5. coverage 高等於 correctness；
6. false positive 永遠比 false negative 不重要；
7. 所有 blind spot 都能被有限 attack 發現；
8. severity 可以完全客觀化；
9. diagnosability 可以唯一數值化；
10. 所有 validator 都需要無限 meta-verification；
11. NotMeasured 應算成 Fail；
12. Unknown 應算成 Fail；
13. denominator 越大越好；
14. 單一總分可取代所有向量；
15. Defect Surface Certificate 是安全認證；
16. 本文方法可用於未授權真實系統攻擊分析。

本文主張的是：

$$
\boxed{
\text{全域對抗測試的結果必須同時描述缺陷、可偵測性、可診斷性與覆蓋，而不能只輸出紅綠。}
}
$$

---

# 43. 與 GACEI-10 的關係

GACEI-10 回答：

$$
\boxed{
\text{有限算力應花在哪裡？}
}
$$

本文回答：

$$
\boxed{
\text{花完之後，怎麼知道我們真的學到了什麼？}
}
$$

---

# 44. 下一篇：全域工程智能 Benchmark

GACEI-12 將把整套系列收束成：

$$
\boxed{
\text{Global Engineering Intelligence Benchmark}.
}
$$

給 AI 一個陌生專案、有限 observation、有限 compute、attack memory 與 sandbox，測 attention、understanding、resolution、creativity、generation、computation、verification、localization 與 memory / learning。

---

# 45. 結論

全域 attack 最容易產生三種錯覺：

> 跑得很多，所以知道很多。

> 全綠，所以系統很好。

> 全紅，所以測試很強。

這三個推論都不充分。

真正需要保存的是：

$$
\boxed{
\text{What changed?}
}
$$

$$
\boxed{
\text{Was that change actually a defect?}
}
$$

$$
\boxed{
\text{Did our validator see it?}
}
$$

$$
\boxed{
\text{Did our alarm surface it?}
}
$$

$$
\boxed{
\text{Can we localize why it happened?}
}
$$

$$
\boxed{
\text{What did we not measure?}
}
$$

因此本文把全域對抗結果壓縮成：

$$
\boxed{
\text{Defect}
+
\text{Detectability}
+
\text{Diagnosability}
+
\text{Coverage}.
}
$$

最後：

$$
\boxed{
\text{Global Evidence}
=
\text{Defect Surface}
+
\text{Detection Matrix}
+
\text{Localization}
+
\text{Coverage Vector}
+
\text{Residual}.
}
$$

這才是一次全域對抗計算真正完成後，值得寫入記憶、交給下一個 AI、用來 repair、release 與下一輪 reasoning 的工程證據。

---

## Canonical Source Note

本文件之正式原稿為 UTF-8 Markdown。

所有數學原始碼僅使用：

- inline：` $...$ `
- display：`$$...$$`

不以 Unicode 數學字元替代 LaTeX source，不進行 unicode-escape round-trip，不將聊天渲染畫面視為 canonical source。
