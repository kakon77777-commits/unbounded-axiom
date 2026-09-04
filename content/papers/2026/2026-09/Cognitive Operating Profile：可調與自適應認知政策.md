# Cognitive Operating Profile：可調與自適應認知政策

**Cognitive Operating Profile: Adjustable and Adaptive Policies for AI Cognition**

**系列：Adaptive Possibility-Space Cognition（APSC）／Paper 05 of 06**  
**版本：v0.1**  
**日期：2026-08-24**  
**作者：Neo.K**  
**機構：EveMissLab / EVEMISS Technology**

---

## 摘要

自適應可能空間認知（Adaptive Possibility-Space Cognition, APSC）前四篇已依序建立可能空間、受約束展開、反事實觀察展開，以及有限認知時空中的自適應計算控制。然而，若控制器只追求一個固定的全域最優目標，仍無法處理真實使用情境中的根本差異：有些任務要求單輪正確性，有些要求低延遲，有些要求探索廣度，有些要求高風險下的保守驗證，而有些研究任務則刻意接受較高延遲以換取更多反事實與可能空間展開。

本文提出 **Cognitive Operating Profile（COP）** 作為 APSC 的第五層理論。COP 將 AI 的認知政策表示為可調參數向量，而非單一的「Thinking Level」。本文提出 depth、breadth、verification、counterfactual、observation、risk、latency、abstraction、commitment、novelty 等維度，並區分使用者偏好、任務需求、系統安全約束與 AI 自適應建議四種來源。本文主張，認知政策應允許多層控制：使用者可設定偏好；系統可設定不可違反的硬邊界；AI 可在授權區域內依當前狀態調整認知配置。

本文進一步提出 Profile Composition、Profile Conflict Resolution、Adaptive Profile Shift、Policy Hysteresis、Profile Receipt、Calibration、Mode Collapse Prevention 與 User Override 等機制，並定義 Single-Turn Accuracy、Exploration、Low-Latency、High-Risk Assurance、Research 等典型認知模式。本文強調，模式名稱只是介面層，真正 canonical 的內容應是可審計的參數與約束，而不是模糊的「快／慢」「低／高思考」。

本文主張：

$$
\boxed{
\text{There is no universally optimal cognitive profile.}
}
$$

高階 AI 的一部分，是能依任務與使用者目的調整「怎麼想」，而不是只調整「想多久」。

**關鍵詞：** Cognitive Operating Profile、認知政策、可調認知、自適應認知、單輪正確性、探索、低延遲、高風險驗證、使用者控制、認知滑桿、APSC

---

# 1. 問題的提出

## 1.1 「Thinking High」太粗糙

很多 AI 系統把認知控制簡化為：

$$
ThinkingLevel
\in
\{
Low,
Medium,
High
\}.
$$

這種表示隱含：

$$
\text{more thinking}
\Rightarrow
\text{better cognition}.
$$

但 APSC 前四篇已經指出，這不普遍成立。

有些任務需要：

$$
Verification\uparrow
$$

卻不需要：

$$
Breadth\uparrow.
$$

有些任務需要：

$$
Observation\uparrow
$$

卻不需要：

$$
CounterfactualDepth\uparrow.
$$

因此單一 thinking level 無法表達真正的認知偏好。

---

## 1.2 認知偏好是向量，不是標量

本文定義：

$$
\Theta_t
=
(
\theta_d,
\theta_b,
\theta_v,
\theta_{cf},
\theta_o,
\theta_r,
\theta_l,
\theta_a,
\theta_c,
\theta_n
).
$$

其中：

- $\theta_d$：depth；
- $\theta_b$：breadth；
- $\theta_v$：verification；
- $\theta_{cf}$：counterfactual；
- $\theta_o$：observation；
- $\theta_r$：risk sensitivity；
- $\theta_l$：latency preference；
- $\theta_a$：abstraction；
- $\theta_c$：commitment conservatism；
- $\theta_n$：novelty preference。

這組向量即為：

$$
\boxed{
CognitiveOperatingProfile.
}
$$

---

# 2. COP 的正式定義

本文定義：

> **Cognitive Operating Profile（COP）** 是一組用來調節 AI 認知操作選擇、資源配置、觀察、驗證、展開、抽象、停止與提交行為的可解釋政策參數與約束。

形式上：

$$
COP_t
=
\left\langle
\Theta_t,
\mathcal H,
\mathcal P,
\mathcal A,
\mathcal R
\right\rangle.
$$

其中：

- $\Theta_t$：認知政策參數；
- $\mathcal H$：Hard Constraints；
- $\mathcal P$：User / Task Preferences；
- $\mathcal A$：Adaptive Region；
- $\mathcal R$：Profile Receipts / Audit State。

---

# 3. 四種政策來源

## 3.1 使用者偏好

例如：

> 這次先求快。  
> 這題我要你多驗證。  
> 多探索幾種可能。  
> 不要展開太遠。

可表示為：

$$
P_{\mathrm{user}}.
$$

---

## 3.2 任務需求

任務本身可能要求：

$$
P_{\mathrm{task}}.
$$

例如實時控制天然偏向低延遲；研究任務偏向探索與反事實。

---

## 3.3 系統硬邊界

某些安全、權限、成本與時間條件不可由 AI 任意改寫：

$$
H_{\mathrm{system}}.
$$

因此：

$$
COP
\subseteq
FeasiblePolicyRegion.
$$

---

## 3.4 AI 自適應建議

AI 可根據：

$$
S_t,
B_t,
Risk_t,
Uncertainty_t
$$

提出：

$$
P_{\mathrm{adaptive}}.
$$

但只能在授權範圍：

$$
\mathcal A
$$

內調整。

---

# 4. Profile Composition

最終有效 Profile 不是單一來源：

$$
COP_t^{eff}
=
Compose
(
P_{\mathrm{user}},
P_{\mathrm{task}},
H_{\mathrm{system}},
P_{\mathrm{adaptive}}
).
$$

但：

$$
H_{\mathrm{system}}
$$

擁有最高不可違反優先級。

---

# 5. Profile Conflict

## 5.1 使用者偏好可能互相衝突

例如同時要求：

$$
Latency\downarrow
$$

以及：

$$
Verification\uparrow.
$$

這可能不可同時完全滿足。

---

## 5.2 衝突解析

可以定義：

$$
Resolve
:
\mathcal P
\rightarrow
\Theta^{feasible}.
$$

控制器應回傳：

- 哪些偏好被滿足；
- 哪些被折衷；
- 哪些因硬邊界無法滿足。

---

# 6. Depth

## 6.1 Depth 不是 token 數

 $\theta_d$ 控制的是：

$$
\text{logical cognitive depth}.
$$

而不是單純：

$$
TokenBudget.
$$

---

## 6.2 高 Depth

提高：

- 多步因果；
- 長鏈驗證；
- 長程 rollout；
- 多層 backtracking。

但成本：

$$
C_{\mathrm{compute}}\uparrow.
$$

---

# 7. Breadth

 $\theta_b$ 控制：

$$
|\widehat{\Omega}|.
$$

高 breadth 適合：

- 多假說；
- 多策略；
- 多反例；
- 多場景。

低 breadth 適合：

- 即時任務；
- 明確單解問題；
- 快速局部回答。

---

# 8. Verification

 $\theta_v$ 控制：

- verifier 次數；
- 交叉驗證；
- 外部查證；
- consistency check；
- proof / test / simulation requirement。

高 verification 模式不一定需要高 breadth。

因此：

$$
\theta_v
\not\equiv
\theta_b.
$$

---

# 9. Counterfactual

 $\theta_{cf}$ 控制：

$$
\mathfrak I,
\mathfrak O^{CF}
$$

等反事實算子的使用強度。

高值代表：

- 更多「如果不是這樣」；
- 更多替代世界；
- 更多觀察前模擬；
- 更強反例壓力測試。

---

# 10. Observation

 $\theta_o$ 控制 AI 主動取得外部資訊的傾向。

高值可能增加：

$$
C_{\mathrm{obs}}
$$

但降低：

$$
C_{\mathrm{rollout}}.
$$

因此：

$$
Observation
$$

與：

$$
InternalReasoning
$$

存在可調 trade-off。

---

# 11. Risk Sensitivity

 $\theta_r$ 控制對：

$$
P(\omega)\ll1
$$

但：

$$
Loss(\omega)\gg1
$$

之分支的保留與檢查程度。

高風險 Profile：

$$
\theta_r\uparrow.
$$

---

# 12. Latency Preference

 $\theta_l$ 表示對低延遲的偏好強度。

高 latency pressure：

$$
\theta_l\uparrow
$$

會促使：

- breadth 下降；
- 遠期解析度下降；
- verifier 次數下降；
- commitment 提前；
- 高成本 observation 被抑制。

---

# 13. Abstraction

 $\theta_a$ 控制何時把高解析狀態轉為：

$$
Scenario,
Region,
Attractor.
$$

高 abstraction rate：

$$
\theta_a\uparrow
$$

適合長期規劃與資源受限情境。

---

# 14. Commitment Conservatism

 $\theta_c$ 控制提交門檻。

高值表示：

$$
\tau_s\uparrow
$$

以及：

$$
\tau_g\downarrow.
$$

也就是需要更高穩定性、更低預期追加收益才提交。

---

# 15. Novelty Preference

 $\theta_n$ 控制系統是否刻意保留新穎、非主流但可行的候選。

若：

$$
\theta_n=0,
$$

系統可能只保留高機率主流分支。

研究情境通常需要：

$$
\theta_n\uparrow.
$$

---

# 16. Single-Turn Accuracy Profile

這是本文中特別重要的模式之一。

目標：

> 不追求最大未來探索，而優先把當前單輪回答做對。

可設定：

$$
\theta_v\uparrow,
$$

$$
\theta_d^{local}\uparrow,
$$

$$
\theta_b\downarrow,
$$

$$
\theta_{cf}^{far}\downarrow,
$$

$$
\theta_c\uparrow.
$$

其特徵是：

$$
\boxed{
\text{local correctness over broad exploration}.
}
$$

---

# 17. Exploration Profile

研究探索模式：

$$
\theta_b\uparrow,
$$

$$
\theta_{cf}\uparrow,
$$

$$
\theta_n\uparrow,
$$

$$
\theta_o\uparrow.
$$

並延後過早 commit。

---

# 18. Low-Latency Profile

目標：

$$
T_{\mathrm{wall}}\downarrow.
$$

可使用：

$$
\theta_l\uparrow,
$$

$$
\theta_b\downarrow,
$$

$$
\theta_d\downarrow,
$$

$$
\theta_a\uparrow.
$$

但不允許突破必要硬安全檢查。

---

# 19. High-Risk Assurance Profile

高風險任務可設定：

$$
\theta_v\uparrow,
$$

$$
\theta_r\uparrow,
$$

$$
\theta_o\uparrow,
$$

$$
\theta_c\uparrow.
$$

同時降低：

$$
Prune_{\mathrm{aggressive}}.
$$

---

# 20. Research Profile

研究模式不應只是「全部拉高」。

若全部維度都最大：

$$
C\rightarrow\infty.
$$

更合理的是：

$$
\theta_b\uparrow,
\theta_{cf}\uparrow,
\theta_n\uparrow,
\theta_o\uparrow
$$

但遠期使用：

$$
\theta_a\uparrow
$$

控制爆炸。

---

# 21. 模式名稱不是 canonical source

介面可以顯示：

- Fast；
- Accurate；
- Research；
- Safe；
- Explore。

但正式系統內部應保存：

$$
\Theta.
$$

因此：

$$
ModeLabel
\neq
CanonicalPolicy.
$$

---

# 22. User Slider

## 22.1 滑桿的理論地位

UI slider 不是簡化玩具，而是：

$$
UserIntent
\rightarrow
PolicyParameter.
$$

---

## 22.2 單滑桿與多滑桿

普通使用者可以使用：

$$
SimpleMode.
$$

進階使用者可以展開：

$$
AdvancedCOP.
$$

---

# 23. AI Self-Adjustment

## 23.1 AI 不應任意改 Profile

允許：

$$
\Theta_{t+1}
=
Adapt(\Theta_t,S_t)
$$

但必須：

$$
\Theta_{t+1}
\in
\mathcal A.
$$

---

## 23.2 Adaptive Region

定義：

$$
\mathcal A
=
[\Theta_{\min},\Theta_{\max}].
$$

使用者可以限制：

> 你可以自己調整，但 verification 不可低於 0.8。

---

# 24. Profile Shift Trigger

觸發 Profile 改變的條件包括：

- uncertainty spike；
- risk spike；
- deadline approaching；
- repeated verifier disagreement；
- observation contradiction；
- branch explosion；
- answer stabilization。

可表示：

$$
Trigger_t
=
f(S_t,B_t).
$$

---

# 25. Adaptive Profile Shift

當：

$$
Trigger_t=1,
$$

AI 可以提出：

$$
\Theta_{t+1}^{proposal}.
$$

但：

$$
\Theta_{t+1}^{eff}
=
Project_{\mathcal A}
(
\Theta_{t+1}^{proposal}
).
$$

---

# 26. Policy Hysteresis

若 Profile 對微小變化過度敏感：

$$
\Theta_t
\leftrightarrow
\Theta_{t+1}
$$

可能產生抖動。

因此加入 hysteresis：

$$
|\Delta Trigger|
>
\tau_h
$$

才允許切換。

---

# 27. Profile Stability

定義：

$$
Stab_{\Theta}
=
1-
\frac{
N_{\mathrm{unnecessary\ shifts}}
}{
N_{\mathrm{steps}}
}.
$$

頻繁切換不一定代表更智能。

---

# 28. Profile Receipt

每次重要 Profile 變更可記錄：

$$
Receipt_t
=
(
\Theta_{old},
\Theta_{new},
Reason,
Trigger,
Budget,
ExpectedEffect
).
$$

這使自適應政策可被審計。

---

# 29. 使用者 Override

使用者可以：

$$
Override(\Theta).
$$

但：

$$
Override
\not\supset
HardSafetyConstraints.
$$

因此：

$$
UserPreference
\neq
UnlimitedAuthority.
$$

---

# 30. Profile Calibration

## 30.1 初始值不可能一次正確

需要透過任務資料估計：

$$
\Theta^\ast.
$$

---

## 30.2 個人化 calibration

不同使用者可能偏好不同：

$$
U_{\mathrm{user}}(Q,T,C).
$$

因此 Profile 可以學習：

$$
\widehat U_{\mathrm{user}}.
$$

但應允許：

- reset；
- inspect；
- override；
- opt-out。

---

# 31. 任務條件化 Profile

Profile 不應只依使用者，也依任務：

$$
\Theta_t
=
f(
User,
Task,
Risk,
Budget,
Deadline,
State
).
$$

---

# 32. Profile Inheritance

子任務可繼承母任務：

$$
\Theta_{\mathrm{child}}
=
Inherit(\Theta_{\mathrm{parent}}).
$$

但某些維度可被局部修改。

例如 verifier 子任務：

$$
\theta_v^{child}
>
\theta_v^{parent}.
$$

---

# 33. 多 Agent Profile

不同子 Agent 可以有不同 Profile：

$$
\Theta_1,\ldots,\Theta_n.
$$

例如：

- Agent A：探索；
- Agent B：驗證；
- Agent C：反例；
- Agent D：低延遲整合。

因此 multi-agent 不必全部使用同一 cognition style。

---

# 34. Profile Diversity

可定義：

$$
D_{\Theta}
=
\frac{
1
}{
n(n-1)
}
\sum_{i\neq j}
d(\Theta_i,\Theta_j).
$$

適度 Profile diversity 可提高搜索空間覆蓋。

---

# 35. Mode Collapse

如果所有 Agent 最後都收斂到：

$$
\Theta^\ast
$$

可能造成：

$$
CognitiveModeCollapse.
$$

因此某些研究任務應刻意保留 Profile diversity。

---

# 36. Profile 與資源控制器

Paper 04 控制器：

$$
u_t^\ast
=
\arg\max
[
\Delta Q(u)
-
\lambda^\top C(u)
].
$$

COP 會改變：

$$
\lambda.
$$

因此：

$$
\lambda
=
g(\Theta).
$$

同時也改變：

$$
\mathcal U_t^{priority}.
$$

---

# 37. Profile 與 COE

Paper 03 的觀察價值：

$$
V_{obs}(q)
$$

可受：

$$
\theta_o,
\theta_{cf},
\theta_r
$$

調節。

因此同一個觀察，在不同 Profile 下可能得到不同優先級。

---

# 38. Profile 與可能空間

高 breadth：

$$
|\widehat{\Omega}|\uparrow.
$$

高 abstraction：

$$
Resolution\downarrow.
$$

高 novelty：

$$
RareFeasibleBranches\uparrow.
$$

所以 COP 直接塑造工作可能空間。

---

# 39. Profile 與停止條件

Paper 04 的停止：

$$
EV_{\mathrm{further}}
\leq
Cost_{\mathrm{further}}.
$$

但 COP 會改變 Cost 的相對權重與 commit 門檻。

因此：

$$
StopPolicy
=
f(
MVC,
Budget,
\Theta
).
$$

---

# 40. Profile 與單輪正確性

單輪正確性不等於最終世界模型最好。

它優化：

$$
Q_{\mathrm{local}}.
$$

因此：

$$
Q_{\mathrm{local}}
\neq
Q_{\mathrm{global}}.
$$

COP 允許使用者明確指定這種偏好。

---

# 41. Profile 與長期研究

長期研究可允許：

$$
Q_{\mathrm{global}}
$$

優先於：

$$
Latency.
$$

但仍應受總預算約束。

---

# 42. Profile Conflict Matrix

可以建立：

$$
M_{ij}
=
Conflict(\theta_i,\theta_j).
$$

常見衝突：

- latency vs verification；
- breadth vs compute；
- novelty vs certainty；
- abstraction vs local detail；
- early commit vs risk assurance。

---

# 43. Profile Feasibility

不是任意向量都能實現。

必須滿足：

$$
\Theta
\in
\mathcal F_{\Theta}.
$$

其中：

$$
\mathcal F_{\Theta}
$$

是受模型能力、資源與系統限制決定的可行域。

---

# 44. Profile Projection

若使用者要求：

$$
\Theta^{req}
\notin
\mathcal F_{\Theta},
$$

則：

$$
\Theta^{eff}
=
Project_{\mathcal F_{\Theta}}
(
\Theta^{req}
).
$$

系統應揭示折衷，而不是假裝完全做到。

---

# 45. Profile Regret

定義：

$$
R_{\Theta}
=
Q(
\Theta^\ast
)
-
Q(
\Theta_{\mathrm{used}}
).
$$

若長期 Profile regret 高，代表 calibration 或 routing 失敗。

---

# 46. User Preference Regret

即使決策品質高，如果明顯違反使用者偏好，也可能產生：

$$
R_{\mathrm{user}}.
$$

例如使用者要快速答案，但 AI 自動進入深度研究模式。

---

# 47. Profile Safety

使用者可能要求：

> 不要驗證，直接回答。

在某些高風險任務中：

$$
\theta_v
$$

不能降到系統最低值以下。

因此：

$$
\Theta_{\mathrm{user}}
\cap
H_{\mathrm{system}}
$$

才形成實際政策。

---

# 48. Profile Transparency

系統不必暴露內部私有推理，但可以暴露：

- Profile 名稱；
- 主要參數；
- 是否自適應變更；
- 是否因風險提高驗證；
- 是否因 deadline 降低探索。

這提供：

$$
OperationalTransparency
$$

而非私有推理透明。

---

# 49. Profile API

工程上可表示：

```json
{
  "profile": {
    "depth": 0.65,
    "breadth": 0.30,
    "verification": 0.85,
    "counterfactual": 0.20,
    "observation": 0.40,
    "risk": 0.75,
    "latency": 0.70,
    "abstraction": 0.55,
    "commitment": 0.80,
    "novelty": 0.15
  },
  "adaptive": true
}
```

此 JSON 只是工程表示，canonical 理論仍是：

$$
COP.
$$

---

# 50. 實驗設計

## 50.1 Fixed Profile Baseline

所有任務使用同一：

$$
\Theta_0.
$$

---

## 50.2 User-Selected Profile

使用者手動選模式。

---

## 50.3 Task-Routed Profile

系統依任務分類選 Profile。

---

## 50.4 Adaptive COP

允許：

$$
\Theta_t
\rightarrow
\Theta_{t+1}.
$$

---

# 51. 評估指標

比較：

$$
Q_{\mathrm{task}},
$$

$$
T_{\mathrm{wall}},
$$

$$
C_{\mathrm{compute}},
$$

$$
R_{\Theta},
$$

$$
R_{\mathrm{user}},
$$

$$
ProfileShiftCount,
$$

$$
DeadlineMissRate,
$$

$$
CriticalErrorRate.
$$

---

# 52. 主要失敗模式

1. **One-Dimensional Thinking Control**：把所有認知壓成單一 thinking level；
2. **Profile Misrouting**：任務被送到錯 Profile；
3. **Over-Adaptive Oscillation**：頻繁切換；
4. **User Preference Override**：AI 無授權改掉使用者偏好；
5. **Safety Underflow**：verification 或 risk sensitivity 低於必要值；
6. **Research Everything**：所有任務都進研究模式；
7. **Speed Everything**：所有任務都過早 commit；
8. **Mode Label Illusion**：UI 名稱與真正參數不一致；
9. **Hidden Profile Shift**：AI 改政策但無 receipt；
10. **Mode Collapse**：多 Agent 全部使用同一認知型態；
11. **Profile Overfitting**：過度個人化到一般化能力下降；
12. **Infeasible Profile Promise**：宣稱可以同時最大速度與最大驗證。

---

# 53. 可否證命題

## 命題一：多維 Profile 應優於單一 thinking level

若：

$$
COP
$$

不能在多類任務上比單標量控制提供更佳 quality-latency-risk trade-off，則其複雜性缺乏必要性。

---

## 命題二：Adaptive COP 應優於 Fixed COP

若自適應 Profile：

$$
Q_{\mathrm{adaptive}}
\leq
Q_{\mathrm{fixed}}
$$

且成本更高，則 adaptive shift 機制需要修正。

---

## 命題三：使用者偏好應可被可靠映射

若「單輪正確」「低延遲」「探索」等明確偏好無法穩定映射到可預測行為，則 COP 尚未形成有效操作政策。

---

# 54. 正式 COP 模型

本文提出：

$$
\mathcal{COP}_t
=
\left\langle
\Theta_t,
P_{\mathrm{user}},
P_{\mathrm{task}},
H_{\mathrm{system}},
\mathcal A,
\Pi_{\Theta},
\pi_{\mathrm{shift}},
\mathcal R_{\Theta}
\right\rangle.
$$

其中：

- $\Theta_t$：當前 Profile；
- $P_{\mathrm{user}}$：使用者偏好；
- $P_{\mathrm{task}}$：任務需求；
- $H_{\mathrm{system}}$：硬邊界；
- $\mathcal A$：AI 可自適應區域；
- $\Pi_{\Theta}$：可行域投影；
- $\pi_{\mathrm{shift}}$：Profile Shift Policy；
- $\mathcal R_{\Theta}$：Profile Receipts。

---

# 55. 與 APSC 前四篇的關係

Paper 01：

$$
APSC.
$$

Paper 02：

$$
PossibilitySpace.
$$

Paper 03：

$$
CounterfactualObservation.
$$

Paper 04：

$$
AdaptiveComputationControl.
$$

本文：

$$
\boxed{
\text{How should the control policy itself be configured?}
}
$$

因此：

$$
\Theta
\rightarrow
Control
\rightarrow
CognitiveOperations.
$$

---

# 56. 與 Paper 06 的接口

Paper 06 的 AI 張力競技場將允許：

- 不同 Agent 使用不同 Profile；
- 相同模型使用不同 Profile；
- 固定 Profile vs Adaptive Profile；
- 不同 budget 下比較；
- 對手改變後是否自適應 shift。

因此 COP 將成為競技場的重要自變量。

---

# 57. 核心命題總結

### 命題一：認知政策是向量

$$
\boxed{
ThinkingLevel
\not\equiv
CognitiveOperatingProfile.
}
$$

### 命題二：不存在普遍最優 Profile

$$
\boxed{
\forall Task,\ \Theta^\ast_{Task}
\text{ need not be identical}.
}
$$

### 命題三：使用者可控制認知偏好

$$
\boxed{
UserPreference
\rightarrow
CognitivePolicy.
}
$$

### 命題四：AI 自適應必須受授權區域限制

$$
\boxed{
\Theta_{t+1}
\in
\mathcal A.
}
$$

### 命題五：模式名稱不是 canonical policy

$$
\boxed{
ModeLabel
\neq
\Theta.
}
$$

### 命題六：Profile 改變應可被審計

$$
\boxed{
AdaptiveShift
\Rightarrow
ProfileReceipt.
}
$$

### 命題七：單輪正確性是一種合法認知目標

$$
\boxed{
Q_{\mathrm{local}}
\text{ can be prioritized over }
Q_{\mathrm{global}}.
}
$$

---

# 58. 結論

本文提出 Cognitive Operating Profile，將「AI 要怎麼想」正式提升為可配置、可自適應、可審計的政策層。

真正成熟的 AI 介面不應只提供：

> 快 / 慢。  
> Thinking Low / High。

而應在適當抽象層上允許：

> 這次先求單輪正確。  
> 這次多探索。  
> 這次少展開遠期。  
> 這次高風險，多驗證。  
> 這次延遲優先。  
> 這次允許 AI 在一定範圍內自行調整。

形式上：

$$
\boxed{
\Theta
\rightarrow
\lambda
\rightarrow
\pi_{\mathrm{sched}}
\rightarrow
\pi_{\mathrm{stop}}
\rightarrow
\pi_{\mathrm{commit}}
\rightarrow
Cognition.
}
$$

因此，認知控制不再只是「模型有多少計算」，而是：

$$
\boxed{
\text{which cognitive trade-off the system is currently optimizing}.
}
$$

這也使使用者與 AI 的關係從「給一個 prompt，模型自己猜應該怎麼想」，轉向：

$$
\boxed{
\text{explicit cognitive policy negotiation}.
}
$$

下一篇 Paper 06 將完成本系列理論收束：**AI 張力競技場——有限可能空間智能的動態對抗驗證**。它將把前五篇中的可能空間、觀察、資源控制與 COP 放入多智能體、部分觀察、有限預算、對手反作用與可重播環境中進行綜合驗證。

---

## 版本記錄

### v0.1 — 2026-08-24

本版首次固定：

1. Cognitive Operating Profile canonical 定義；
2. 十維 Profile Vector；
3. User / Task / System / Adaptive 四源政策；
4. Profile Composition；
5. Conflict Resolution；
6. Depth；
7. Breadth；
8. Verification；
9. Counterfactual；
10. Observation；
11. Risk；
12. Latency；
13. Abstraction；
14. Commitment Conservatism；
15. Novelty Preference；
16. Single-Turn Accuracy Profile；
17. Exploration Profile；
18. Low-Latency Profile；
19. High-Risk Assurance Profile；
20. Research Profile；
21. Mode Label 非 canonical；
22. User Slider；
23. Adaptive Region；
24. Profile Shift Trigger；
25. Adaptive Profile Shift；
26. Policy Hysteresis；
27. Profile Stability；
28. Profile Receipt；
29. User Override；
30. Profile Calibration；
31. Task-Conditioned Profile；
32. Profile Inheritance；
33. Multi-Agent Profile；
34. Profile Diversity；
35. Mode Collapse Prevention；
36. APSC Controller Interface；
37. COE Interface；
38. Possibility-Space Interface；
39. Stop / Commit Interface；
40. Profile Conflict Matrix；
41. Profile Feasibility；
42. Profile Projection；
43. Profile Regret；
44. User Preference Regret；
45. Profile Transparency；
46. Profile API；
47. Experiment Design；
48. 可否證命題。
