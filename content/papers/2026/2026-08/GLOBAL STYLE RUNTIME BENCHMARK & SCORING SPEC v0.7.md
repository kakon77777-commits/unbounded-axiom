# GLOBAL STYLE RUNTIME BENCHMARK & SCORING SPEC v0.7

## 1. 目標

v0.7 的目標，是讓 v0.6 的 Execution Runtime 從「能執行」進一步變成：

```text
能比較
能評分
能診斷
能重新編譯
能重新綁定
```

完整閉環為：

$$
Search \to Compile \to Bind \to Run \to Score \to Diagnose \to Recompile/Rebind
$$

本版不採用「一個總分決定一切」的設計，而使用：

$$
\boxed{\text{Hard Gates} + \text{Metric Vector} + \text{Optional Composite Score}}
$$

原因是生成圖的不同品質軸彼此並不等價：prompt adherence、單張美感、style consistency、技術畫質、diversity/coverage、anti-homogenization 可能互相衝突。

---

## 2. Metric Vector

定義每一張圖或每一批圖的核心評分向量：

$$
M = (P,Q,A,S,D,H,C,R)
$$

其中：

- $P$ — Prompt / Constraint Adherence
- $Q$ — Technical Image Quality
- $A$ — Human Preference / Aesthetic Proxy
- $S$ — Style Consistency
- $D$ — Diversity / Coverage
- $H$ — Anti-Homogenization
- $C$ — Character / Subject Consistency
- $R$ — Reference / Control Consistency

這八個值都標準化到：

$$
[0,100]
$$

但每個值的 Provider 可以不同。

---

## 3. Hard Gates

在計算總分前，先過最低門檻。

### Gate G0 — Execution Validity
- 圖像成功產出
- 無 corrupt artifact
- metadata 完整

### Gate G1 — Prompt / Constraint Minimum
- 主要主體存在
- 必要數量正確
- 必要關係基本成立

### Gate G2 — Technical Quality Minimum
- 無嚴重 blur / corruption / broken image

### Gate G3 — Project Constraint Minimum
若 project recipe 指定：
- 角色身份
- palette
- reference style
- control pose

則至少達到最低門檻。

任一硬門檻失敗：

```text
score_status = rejected
```

不應靠其他高分補回來。

---

## 4. Prompt / Constraint Adherence — P

推薦採混合 Provider：

### P1 — VQA-based alignment
對複雜自然語言 prompt，用 VQA 類 evaluator 檢查物件、屬性、關係。

### P2 — Object / Count / Position checks
對可明確結構化的條件，使用 object-focused evaluator。

### P3 — Rule-specific validators
例如：
- 是否有劍
- 是否為雨夜
- 是否是兩個人物
- 是否滿足指定色彩區間

定義：

$$
P = w_{vqa}P_{vqa}+w_{obj}P_{obj}+w_{rule}P_{rule}
$$

預設：

$$
(w_{vqa},w_{obj},w_{rule})=(0.45,0.30,0.25)
$$

---

## 5. Technical Image Quality — Q

Q 只評估技術品質，不評估風格好不好。

可包含：

- blur
- noise
- distortion
- exposure
- compression artifact
- broken anatomy detector（可選）

定義：

$$
Q = \sum_i w_i q_i
$$

工程上可接 MUSIQ / IQA provider 或其他 image-quality evaluator。

---

## 6. Human Preference / Aesthetic Proxy — A

A 不應當成「藝術真理」，只作為：

> 一般人類偏好／視覺完成度的 proxy。

可接：
- HPS v2
- ImageReward
- project-specific preference model

若專案已累積自己的人工選擇資料，應逐步增加：

$$
A_{project}
$$

權重，而不是永遠依賴通用 preference model。

---

## 7. Style Consistency — S

對一組同專案圖片：

$$
\mathcal I = \{I_1,\ldots,I_n\}
$$

可使用 pairwise style similarity。

基準方案：

$$
S_{DINO} = \frac{2}{n(n-1)}\sum_{i<j}\cos(E_D(I_i),E_D(I_j))
$$

其中 $E_D$ 是 DINO 類 embedding。

更進階可使用：
- DiffSim
- CSD-style descriptor
- project-trained style encoder

注意：

$$
\text{Style Consistency} \neq \text{Image Similarity}
$$

必須避免把「所有構圖都一樣」誤認為風格一致。

---

## 8. Diversity / Coverage — D

D 分兩層。

### 8.1 Batch Diversity
評估同一 query / recipe 的候選是否真的有變化。

可用：
- pairwise DINO distance
- LPIPS / DiffSim distance
- composition embedding spread

### 8.2 Dataset / Mode Coverage
對大量生成結果，應使用 coverage-oriented metric。

本版預留 IRS（Image Retrieval Score）Provider，用於估計生成集合覆蓋真實／參考分佈的程度。

因此：

$$
D = w_bD_{batch}+w_cD_{coverage}
$$

小批生成時：

$$
w_c=0
$$

大規模 benchmark 時才啟用 coverage。

---

## 9. Anti-Homogenization — H

這是本系統自訂的實驗性指標，不宣稱為現有學術標準。

H 的目的不是追求「越不像越好」，而是避免：

```text
同一張臉
同一個半身正面構圖
同一種霓虹光
同一種皮膚質感
同一種高概率商業審美模板
```

本版定義：

$$
H = 100 - Penalty_{hom}
$$

其中：

$$
Penalty_{hom}
=
\alpha F+
\beta C+
\gamma P+
\delta T
$$

- $F$：Face-template repetition
- $C$：Composition repetition
- $P$：Palette / lighting repetition
- $T$：Texture / finish repetition

預設：

$$
(\alpha,\beta,\gamma,\delta)=(0.35,0.30,0.20,0.15)
$$

---

## 10. Character / Subject Consistency — C

如果是同一角色跨圖生成：

$$
C = Similarity(E_{identity}(I_i),E_{identity}(I_{ref}))
$$

可依角色類型選：
- face embedding
- DINO subject embedding
- project character encoder

但需要同時檢查：

$$
\text{Identity Consistency} \neq \text{Pose/Composition Repetition}
$$

因此 C 高不代表 H 高。

---

## 11. Reference / Control Consistency — R

R 分為：

- $R_{style}$：style reference consistency
- $R_{subject}$：subject reference consistency
- $R_{control}$：pose / depth / edge / color control consistency

可定義：

$$
R = w_sR_{style}+w_uR_{subject}+w_cR_{control}
$$

沒有某類 reference 時，對應項目不計分並重新正規化權重。

---

## 12. Optional Composite Score

只有通過 Hard Gates 後，才計算：

$$
Score =
0.20P+
0.10Q+
0.10A+
0.20S+
0.15D+
0.15H+
0.05C+
0.05R
$$

這只是預設 profile。

不同任務應有不同權重，例如：

### Character Production
提高：
- $S$
- $C$
- $H$

### Concept Exploration
提高：
- $D$
- $H$

### Marketing Key Art
提高：
- $P$
- $Q$
- $A$

---

## 13. Scoring Status

建議狀態：

```text
rejected
weak
acceptable
good
excellent
```

預設：

- `< 55` → weak
- `55–69` → acceptable
- `70–84` → good
- `85+` → excellent

但 hard-gate failure 一律：

```text
rejected
```

---

## 14. Diagnose Layer

評分後不是只說「差」。

系統應輸出診斷向量：

```text
prompt_failure
quality_failure
style_drift
low_diversity
generic_face_repetition
composition_repetition
identity_drift
reference_drift
```

每一種診斷映射到不同修正行為。

---

## 15. Recompile / Rebind Policy

### Rule R1 — Prompt failure
若：

$$
P < 60
$$

則：

```text
recompile prompt
increase explicit constraints
add object/relationship checks
```

### Rule R2 — Style drift
若：

$$
S < 65
$$

則：

```text
increase style-kernel constraints
change reference strategy
increase style adapter weight moderately
```

### Rule R3 — Homogenization
若：

$$
H < 60
$$

則：

```text
increase diversity budget
switch composition seed policy
reduce named-style weight
add face/composition variation constraints
```

### Rule R4 — Quality failure
若：

$$
Q < 55
$$

則：

```text
change backend profile
increase render steps / resolution
invoke repair / enhancement pass
```

### Rule R5 — Reachability suspicion
若多輪：

$$
P,S,C,R
$$
持續低於門檻，則可能是：

> current model profile / asset binding cannot reach target domain.

此時：

```text
rebind model
switch LoRA / adapter family
switch backend
```

而不是繼續無限改 prompt。

---

## 16. Retry Budget

每一次 refinement 都消耗 budget。

定義：

$$
B=(N_{retry},T_{gpu},Cost_{cloud})
$$

預設 Runtime 可設：

```text
max_recompile = 2
max_rebind = 1
max_backend_switch = 1
```

避免無限自動重試。

---

## 17. Benchmark Suite

v0.7 建議先建立 6 類 benchmark：

1. **Prompt Adherence Suite**
2. **Style Stability Suite**
3. **Anti-Homogenization Suite**
4. **Character Consistency Suite**
5. **Reference / Control Suite**
6. **Coverage / Exploration Suite**

每類至少 20 prompts，第一版共：

$$
120\ prompts
$$

即可開始。

---

## 18. Benchmark Reproducibility

每一次 benchmark run 必須保存：

```text
benchmark_version
model_profile
adapter versions
recipe version
seed policy
runner version
metric provider versions
raw metric outputs
normalized metric vector
final status
```

否則分數不可比較。

---

## 19. Metric Provider 原則

本系統正式沿用：

$$
\boxed{Metric \neq Provider}
$$

例如 `StyleConsistency` 可以由：

```text
DINO provider
DiffSim provider
CSD provider
Project Style Encoder
```

實作。

因此 metric schema 不綁定單一模型。

---

## 20. 現有研究對應

本版參考的主要公開評估方向包括：

- GenEval：物件、數量、位置、顏色等細粒度 prompt alignment；
- VQAScore / GenAI-Bench：以 VQA 形式處理複雜 compositional prompt alignment；
- HPS v2 / ImageReward：人類偏好 proxy；
- StyleAligned：以 CLIP text alignment + DINO set consistency 衡量風格一致生成；
- DiffSim：用 diffusion features 評估 appearance / style similarity；
- ICE-Bench：將 aesthetic、imaging quality、prompt following、reference consistency 等拆成多維評估；
- IRS：專門衡量生成模型的 distribution diversity / coverage。

本系統不把任何一個 metric 當唯一真值，而把它們放入 Metric Provider Registry。

---

## 21. v0.8 方向

v0.8 最自然的下一步是：

> **Adaptive Evaluation & Auto-Refinement Runtime**

也就是讓 v0.7 的分數真正控制 v0.6 的執行：

$$
Run \to Score \to Diagnose \to Recompile/Rebind \to Run
$$

並加入：

- metric calibration
- human feedback weighting
- project-specific evaluator
- adaptive backend selection
- evidence store

---

## 22. 結論

v0.7 的真正價值，是避免系統陷入這種錯誤：

> 「一張圖看起來很漂亮，所以這次生成成功。」

對真正遊戲／專案美術而言，成功其實是：

$$
\boxed{
\text{Prompt Correct}
\land
\text{Quality Acceptable}
\land
\text{Style Stable}
\land
\text{Diversity Preserved}
\land
\text{Homogenization Controlled}
}
$$

所以 v0.7 把 Runtime 從「生成器」正式推進成：

> **可量測的視覺約束求解系統。**
