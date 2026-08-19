# GLOBAL STYLE RUNTIME — ADAPTIVE EVALUATION & AUTO-REFINEMENT v0.8

## 1. 目的

v0.7 已經完成：

$$
Run \to Score \to Diagnose
$$

v0.8 要把這個結果真正接回 Runtime：

$$
\boxed{
Run
\to Verify
\to Diagnose
\to SelectAction
\to Refine
\to Run
}
$$

也就是讓系統不只「知道分數不好」，而是知道下一步應該：

```text
ACCEPT
RESAMPLE
RECOMPILE
REBIND
REPAIR
SWITCH_BACKEND
HUMAN_REVIEW
STOP
```

本版將 v0.7 的評分向量：

$$
M=(P,Q,A,S,D,H,C,R)
$$

真正轉換成 Runtime action。

---

# 2. 為何需要閉環，而不是固定 Prompt + 固定 CFG

固定生成流程屬於 open-loop：

```text
設定 prompt / model / guidance
→ 一路生成到底
→ 最後才看結果
```

v0.8 改成 closed-loop：

```text
產生候選
→ 檢查目前狀態
→ 判斷錯在哪一層
→ 只修改必要控制變量
→ 再生成／修復
```

這與近年的 feedback guidance、test-time scaling、self-verification、agentic refinement 路線一致。

---

# 3. Adaptive Controller

定義控制器：

$$
\pi_a:
(M,G,B,H_t)
\rightarrow
A_t
$$

其中：

- $M$：metric vector
- $G$：hard gates
- $B$：剩餘預算
- $H_t$：歷史狀態
- $A_t$：下一個 action

---

# 4. Action Set

## A0 — ACCEPT
條件已滿足，停止自動 refinement。

## A1 — RESAMPLE
模型／風格方向正確，只是候選 seed 不佳。

適用：
- 分數接近門檻
- Style 沒漂
- Prompt 也沒大錯
- Diversity 仍可接受

## A2 — RECOMPILE
人類意圖沒有被 prompt / constraint program 正確表達。

適用：

$$
P<\tau_P
$$

或 evaluator 指出：
- 遺漏物件
- 關係錯誤
- 空間條件錯誤
- prompt 過於模糊

## A3 — REBIND
Prompt 大致正確，但 model / adapter / reference / control 可達域不合。

適用：

$$
P,S,C,R
$$

多輪持續低於門檻，或 style / identity provider 明顯失配。

## A4 — REPAIR
整體構圖已正確，只存在局部失敗。

例如：
- 手
- 臉
- 文字
- 局部材質
- 小區域 artefact

這時不應整張重抽。

## A5 — SWITCH_BACKEND
目前 backend 的品質／相容性／穩定性持續不足。

## A6 — HUMAN_REVIEW
當 verifier 彼此衝突、風格判斷屬高主觀性、或剩餘 budget 很低時，交給人類裁決。

## A7 — STOP
失敗不可恢復或 budget 已耗盡。

---

# 5. Action Priority

第一版採以下優先順序：

```text
Execution invalid
  ↓
Backend / asset failure
  ↓
Localized technical defect
  ↓
Prompt / semantic defect
  ↓
Style / identity / reference defect
  ↓
Homogenization / diversity defect
  ↓
Near-threshold candidate variance
  ↓
Accept
```

目的在避免最常見的錯誤：

> 一看到結果不好就整個重寫 Prompt。

---

# 6. Diagnostic Vector

除了原始 metric vector，本版新增：

$$
D_g=(d_P,d_Q,d_S,d_D,d_H,d_C,d_R)
$$

其中：

$$
d_i=\max(0,\tau_i-M_i)
$$

代表每個維度距離門檻還差多少。

最大 deficit 會成為主要故障候選，但不直接等於 action；還要結合歷史與 budget。

---

# 7. Persistent Failure

如果某維度連續：

$$
M_i^{(t)}<\tau_i
$$

且經過兩次相同類型 refinement 仍沒有改善：

$$
\Delta M_i\leq\epsilon
$$

則停止在同一層反覆微調，升級 action：

```text
RECOMPILE → REBIND
RESAMPLE → RECOMPILE / REBIND
REPAIR → SWITCH_BACKEND
```

---

# 8. Verifier Router

v0.8 不假設所有 evaluator 每次都全開。

採三級 verifier：

## Tier 0 — Cheap / Early
用途：快速篩掉明顯失敗候選。

例如：
- early latent probe
- low-cost alignment scorer
- execution validity
- obvious artifact detector

## Tier 1 — Standard
用途：正式 v0.7 metric vector。

例如：
- prompt adherence
- image quality
- style consistency
- diversity
- reference consistency

## Tier 2 — Expensive / Semantic
只在：
- borderline
- verifier disagreement
- complex composition
- high-value final candidate

時啟動。

例如：
- MLLM verifier
- multi-agent checker
- human review

因此：

$$
Cost_{verify}
$$

本身也成為 runtime budget。

---

# 9. Early Quality Assessment

如果 early verifier 在中間 latent 已經能高信心預測：

$$
Q_{final}<\tau_{abort}
$$

則可：

```text
abort trajectory
→ reuse compute for another seed
```

這比把所有候選都跑完整 diffusion steps 再淘汰更有效率。

---

# 10. Test-Time Scaling Policy

v0.8 把 test-time compute 分成兩條軸：

## 10.1 Trajectory Exploration

增加不同：
- seed
- initial noise
- candidate branch

即：

$$
N_{traj}\uparrow
$$

## 10.2 Iterative Refinement

對最佳候選做：
- recompile
- local repair
- rebind
- re-render

即：

$$
N_{refine}\uparrow
$$

Runtime 不應固定：

```text
所有 prompt 都 N=8、refine=2
```

而應依：
- query complexity
- verifier confidence
- initial score
- remaining budget

動態調整。

---

# 11. Difficulty Estimation

定義：

$$
\chi(q)\in[0,1]
$$

表示 query difficulty。

可由以下因素估計：

```text
object count
relation count
spatial constraints
style constraints
identity constraints
text rendering requirement
reference constraints
```

例如：

```text
單人半身肖像
χ ≈ 0.2

四角色 + 明確空間關係 + 特定風格 + 文字
χ ≈ 0.9
```

---

# 12. Compute Budget Allocation

初版：

$$
B_{traj}=B_0(1+\alpha\chi)
$$

$$
B_{verify}=V_0(1+\beta\chi)
$$

但如果 early score 很高：

$$
M_{early}>\tau_{fastaccept}
$$

可以提前停止擴張。

---

# 13. Refinement State Machine

```text
NEW
 ↓
RUNNING
 ↓
VERIFYING
 ↓
DIAGNOSING
 ├─ ACCEPTED
 ├─ RESAMPLING
 ├─ RECOMPILING
 ├─ REBINDING
 ├─ REPAIRING
 ├─ SWITCHING_BACKEND
 ├─ HUMAN_REVIEW
 └─ STOPPED
```

每一輪 refinement 都建立新 lineage child packet，不覆寫父 packet。

---

# 14. Monotonic Improvement Rule

自動 refinement 不應因一個分數提升，而默許其他核心分數大幅下降。

定義 hard-regression tolerance：

$$
M_i^{(t+1)}
\geq
M_i^{(t)}-\delta_i
$$

對核心維度：

- Prompt
- Style
- Character
- Reference

尤其嚴格。

如果 action 讓 Style +15、但 Prompt -30，則判定 refinement 不合格。

---

# 15. Pareto Acceptance

不同目標可能互相衝突：

- Style consistency
- Diversity
- Prompt adherence
- Creative novelty

因此可採 Pareto acceptance：

候選 $x$ 若不存在另一候選 $y$ 在所有核心維度都不差且至少一維更好，則保留在 Pareto set。

這避免 composite score 過早把「不同但都好」的作品淘汰。

---

# 16. Anti-Homogenization Control

若：

$$
H<60
$$

控制器優先：

1. **不要**增加 named-style weight
2. 增加 seed / trajectory diversity
3. 改變 composition constraint
4. 改變 face / silhouette sampling rule
5. 降低 shared portrait template
6. 必要時切換 style neighbor / hybrid kernel

也就是：

$$
H\downarrow
\not\Rightarrow
StyleStrength\uparrow
$$

這非常重要。

---

# 17. Local Repair Policy

若：

$$
P,S,C,R\geq threshold
$$

而：

$$
Q<\tau_Q
$$

且 defect 可定位到 mask：

$$
\mathcal R_{defect}\subset I
$$

則執行局部修復，而不是 full regeneration。

這可保留已經正確的：
- 構圖
- 角色
- 色彩
- 風格核

---

# 18. Agentic Refiner

v0.8 可以把 refinement roles 拆成：

```text
Planner
Checker
Diagnoser
Refiner
Editor
Verifier
Controller
```

但第一版 Runtime 不要求七個獨立模型；它們可以是同一個 Agent 的七種 role state。

---

# 19. Self-Verification vs External Verification

支持兩種模式：

## External
生成模型和 verifier 分開。

優點：
- 獨立性較高

缺點：
- 成本高

## Self-Verified
若 multimodal generator 本身具圖像理解能力，可對自身候選做 alignment / defect feedback。

優點：
- 省 verifier 成本
- 更容易進入多輪 refinement

缺點：
- 可能存在自我偏誤

所以 Runtime 保留：

```text
self
external
hybrid
```

三種 verifier mode。

---

# 20. Stop Conditions

系統必須知道何時停止。

## Success Stop

```text
hard gates pass
AND
core metrics pass
AND
no major verifier disagreement
```

## Budget Stop

```text
max rounds reached
OR
compute budget exhausted
```

## Plateau Stop

如果：

$$
\max_i |M_i^{(t+1)}-M_i^{(t)}|<\epsilon
$$

連續多輪成立，停止盲目迭代。

## Human Stop

若主觀性過高，交人類裁決。

---

# 21. v0.8 Runtime Loop

```text
packet
  ↓
run candidates
  ↓
Tier-0 early verify
  ├─ hopeless → abort/resample
  ↓
finish promising candidates
  ↓
Tier-1 metric vector
  ↓
diagnose deficits
  ↓
policy controller
  ├─ accept
  ├─ resample
  ├─ recompile
  ├─ rebind
  ├─ local repair
  ├─ backend switch
  └─ human review
  ↓
child packet
  ↓
repeat until stop condition
```

---

# 22. 成功條件

v0.8 MVP 成功標準：

1. 能讀 v0.7 scoring vector。
2. 能產生 deterministic diagnostic action。
3. 能追蹤 refinement budget。
4. 能升級 persistent failure。
5. 能處理 hard-gate failure。
6. 能在 accepted / stopped / human_review 間正確終止。
7. 每輪生成 child lineage packet。
8. 不以單一 composite score 覆蓋 hard gates。

---

# 23. 下一步 v0.9

v0.9 最自然進入：

> **Closed-Loop Runtime Prototype**

直接把：

```text
v0.3 Searcher
v0.4 Compiler
v0.5 Packet
v0.6 Runner
v0.7 Scorer
v0.8 Controller
```

串成真正可以從一條 query 跑到 refinement decision 的本地原型。

即：

$$
\boxed{
Query
\to Runtime
\to Candidate
\to Score
\to AutoRefine
}
$$

這一步之後，才真正值得接實際 ComfyUI / Diffusers backend。
