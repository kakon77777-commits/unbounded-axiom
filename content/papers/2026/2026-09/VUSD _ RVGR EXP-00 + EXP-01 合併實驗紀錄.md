# VUSD / RVGR EXP-00 + EXP-01 合併實驗紀錄
## Human-Gated Visual Counterfactual Pilot & Controlled Material Intervention
### ——從直接凝視漂移到薄紗透明度反事實的首批視覺理解實驗

**版本：** v0.1  
**日期：** 2026-08-31  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**研究系列：** VUSD — Visual Understanding Shared-Domain Theory  
**系統關聯：** EveAtelier / VUSD / RVGR / Style Control / Appeal-Preserving Style Transformation  
**實驗狀態：** Pilot / Early Empirical Evidence  
**實驗介面：** ChatGPT human-gated cross-turn image generation loop

---

# 0. 實驗總覽

本文件合併兩個連續視覺實驗：

| Experiment | 類型 | 主要干預 | 預註冊 | 結果 |
|---|---|---|---|---|
| EXP-00 | Pilot | 回眸往更直接凝視方向漂移 | 否 | `PILOT / INFORMATIVE` |
| EXP-01 | Controlled Counterfactual | 薄紗透明度下降、布料厚度上升 | 是 | `HIT / mild collateral enhancement` |

兩者共同目的是測試 VUSD / RVGR 中的核心命題：

$$
\boxed{
\text{Visual Understanding}
\Rightarrow
\text{Counterfactual Predictability}
}
$$

以及：

$$
\boxed{
\text{Small Visual Change}
\not\Rightarrow
\text{Global Character Redesign}
}
$$

---

# 1. 共同基準角色

兩個實驗均圍繞同一蛇系古風女性角色進行。

角色核心視覺語義包括：

- 黑色長髮；
- 綠色蛇形頭飾；
- 綠色蛇纏繞身體與手部；
- 回身／回眸姿態；
- 綠色色盤與翡翠飾品；
- 修身蛇紋服裝；
- 肩背裸露；
- 高開衩；
- 外披薄紗；
- 神秘、危險、誘惑並存的角色張力；
- 黑色背景下的高 figure-ground separation。

既有成功風格版本已建立：

```text
古風細線柔彩角色立繪風
+
角色專屬綠色高飽和與蛇系危險魅力
```

因此本次實驗不以重新設計角色為目標，而是測試：

> 在鎖定 Identity、Pose、Garment Topology、Palette 與核心 Appeal 的前提下，局部視覺決策改動如何影響 Shared-Domain State。

---

# 2. 實驗介面限制

ChatGPT 圖像生成介面在生成圖片後，本回合無法繼續進行文字判讀。

因此真正可行的實驗流程是：

$$
Predict
\rightarrow
Generate
\rightarrow
\boxed{
Human\ Continuation\ Gate
}
\rightarrow
Observe
\rightarrow
Compare.
$$

亦即：

```text
Turn N:
預測 / 或直接生成

Turn N+1:
使用者輸入「繼續 / 判讀」

Turn N+1:
模型重新觀察結果並比較
```

這表示本環境適合：

# **Human-Gated Counterfactual Experiment**

而不適合宣稱已完成：

# **Autonomous RVGR Loop**

真正無人介入的：

$$
Generate
\rightarrow
Observe
\rightarrow
Rewrite
\rightarrow
Generate
$$

應由本地 EveAtelier / ComfyUI / RVGR Runtime 實作。

---

# 3. EXP-00 — Direct-Gaze Drift Pilot

## 3.1 實驗定位

**狀態：** `PILOT / NOT STRICTLY PRE-REGISTERED`

EXP-00 的生成發生在正式寫下預測之前。

因此：

$$
\boxed{
EXP\text{-}00
\neq
\text{Strict Pre-registered Evidence}
}
$$

本實驗只能作為：

```text
pilot observation
operator-coupling observation
future experiment design evidence
```

不能事後把觀察結果偽裝成事前預測命中。

---

## 3.2 實際生成變化

相較前一成功版本，EXP-00 圖像出現：

```text
臉部與視線更直接朝向觀看者
```

但：

```text
身體仍維持側背 / 回身結構
```

因此並不是：

```text
backward glance → complete frontal pose
```

而較接近：

$$
\text{Indirect Backward Glance}
\rightarrow
\text{More Direct Viewer Gaze}.
$$

---

## 3.3 Shared-Domain 觀察

實際判讀：

$$
Reciprocity \uparrow
$$

$$
DirectViewerBinding \uparrow
$$

$$
DirectionalConflict \downarrow
$$

但：

$$
DirectionalConflict \neq 0.
$$

因為：

```text
Body Direction
仍然偏離觀者

Face / Gaze
更直接朝向觀者
```

所以：

$$
BodyDirection
\neq
GazeDirection
$$

仍然成立。

---

## 3.4 重要意外結果

原先理論上若角色真正：

```text
回眸 → 完全正面凝視
```

可能預期：

$$
ApproachAvoidanceTension \downarrow.
$$

但 EXP-00 中：

```text
身體離開
+
臉更直接看向觀者
```

仍保留明顯 relational conflict。

因此：

$$
ApproachAvoidanceTension
$$

沒有大幅崩解。

這表示：

# **Gaze Decision 與 Body Orientation 是耦合的。**

---

## 3.5 EXP-00 初步命題

### 命題 00-A

$$
\boxed{
\text{Gaze Change}
\neq
\text{Whole Pose Change}
}
$$

### 命題 00-B

$$
\boxed{
\text{Direct Gaze Increase}
\not\Rightarrow
\text{Directional Tension Collapse}
}
$$

若：

$$
BodyDirection
\neq
GazeDirection
$$

仍被保留。

### 命題 00-C

$$
\boxed{
\text{Visual Decision}
\text{ can be causally coupled}
}
$$

因此視覺反事實不應把：

```text
gaze
pose
head direction
neck
hair flow
```

視為完全獨立變量。

---

## 3.6 EXP-00 對 Minimal Causal Closure 的支持

Paper 04 提出：

$$
\boxed{
\text{Minimal Intervention}
=
\text{Minimal Causal Closure}
}
$$

而不是：

> 永遠只改一個 scalar。

EXP-00 顯示：

```text
gaze
```

的視覺作用依賴：

```text
face direction
body direction
pose
viewer relation
```

因此：

$$
Closure(Gaze)
\supseteq
\{
FaceDirection,
BodyRelation
\}.
$$

至少在人物立繪 domain 中值得進一步驗證。

---

## 3.7 EXP-00 證據判定

**Disposition：**

`PILOT / INFORMATIVE / NON-CONFIRMATORY`

原因：

- 具有明確視覺變化；
- 對 operator coupling 有研究價值；
- 但不存在事前固定預測；
- 因此不作為正式「預測命中」證據。

---

# 4. EXP-01 — Sheer-Fabric Opacity Counterfactual

## 4.1 實驗定位

**狀態：** `PRE-REGISTERED CONTROLLED COUNTERFACTUAL`

本次先在生成前固定：

- Intervention；
- Locked Variables；
- Predicted Perceptual Delta；
- Predicted Shared-Domain Delta；
- Predicted Observer Projection。

之後才執行生成。

因此：

$$
\boxed{
EXP\text{-}01
=
\text{First Strictly Pre-registered Pilot in this sequence}
}
$$

---

# 5. EXP-01 Intervention

實際 Provider Instruction：

> 保持人物身份、姿勢、構圖、服裝剪裁、蛇與整體配色完全不變；僅將袖子與披帛的半透明薄紗材質調得更不透明、更有布料厚度，其他部分不要修改。

注意：

> 完整 VUSD reasoning 並未直接灌入圖像 Provider。

這次也暴露出一個重要工程原則：

$$
\boxed{
\text{Reasoning Layer}
\neq
\text{Execution Instruction}
}
$$

高階語義應由 AADS / RABCL 編譯成最小 Provider Instruction。

---

# 6. EXP-01 Locked Variables

要求保持：

- Identity；
- face identity；
- hairstyle；
- snake identity / role；
- pose；
- backward-turn structure；
- composition；
- garment topology；
- green palette；
- overall saturation direction；
- shoulder/back exposure topology；
- leg slit topology；
- character-specific danger / mystery / appeal profile。

形式上：

$$
\Delta I
\approx0,
$$

$$
\Delta G
\approx0,
$$

$$
\Delta Pose
\approx0,
$$

$$
\Delta Palette
\approx0.
$$

主要允許：

$$
\Delta MaterialTransparency
\neq0.
$$

---

# 7. EXP-01 預註冊預測

## 7.1 Decision-level

$$
Transparency \downarrow
$$

---

## 7.2 Perceptual / Material-level

預測：

$$
UnderlyingContourVisibility \downarrow
$$

$$
LayerSeparation \uparrow
$$

$$
MaterialWeight \uparrow
$$

---

## 7.3 Shared-Domain-level

預測：

$$
Reveal \downarrow
$$

$$
Conceal \uparrow
$$

$$
BodylineSalience \downarrow
\quad
\text{（小幅）}
$$

---

## 7.4 Observer Projection-level

預測：

$$
Mystery \uparrow
$$

$$
Formality \uparrow
$$

並預測：

$$
SensualTension \downarrow
\quad
\text{（小至中幅）}
$$

但：

$$
\boxed{
SensualTension
\not\rightarrow
Collapse
}
$$

原因是角色張力還由：

```text
gaze
backward pose
shoulder/back exposure
bodyline
high slit
snake motif
danger cue
```

共同承擔。

---

# 8. EXP-01 實際觀察

## 8.1 Material Change

實際生成後：

- 袖子與披帛明顯更不透明；
- 布料厚度上升；
- 垂墜感增加；
- 原本偏透明薄紗轉為較接近有重量的綠色薄綢 / 紗衣；
- 紋理與金色細節更加可讀。

因此：

$$
Transparency \downarrow
$$

與：

$$
MaterialWeight \uparrow
$$

明確命中。

---

## 8.2 Shared-Domain Change

觀察結果支持：

$$
Reveal \downarrow
$$

$$
Conceal \uparrow
$$

且：

$$
MaterialSeparation \uparrow.
$$

`BodylineSalience` 有小幅下降或被重新分配，但角色核心身形與姿態仍清楚可讀。

因此：

$$
BodylineSalience
\not\rightarrow
Collapse.
$$

---

## 8.3 Observer Projection

角色整體：

```text
神秘感 ↑
正式感 ↑
危險女王感 ↑
```

而：

```text
整體吸引力沒有明顯下降
```

原先預測：

$$
SensualTension \downarrow
\quad
\text{（小至中幅）}
$$

實際更接近：

$$
SensualTension
\approx
Stable
\quad
\text{或僅小幅下降}.
$$

也就是：

> 預測方向並非完全錯誤，但實際張力保持程度比預期更高。

因此此子項應標：

`PARTIAL HIT`

而不是強行記成完整 HIT。

---

# 9. 為什麼性張力沒有崩解？

實驗顯示：

$$
\boxed{
\text{Character Appeal}
\neq
\text{Transparency Parameter Only}
}
$$

角色魅力仍由多因子共同支撐：

$$
A
=
f(
Gaze,
Pose,
ExposureTopology,
Bodyline,
GarmentCut,
SnakeMotif,
Color,
DangerCue,
ViewerBinding
).
$$

因此即使：

$$
Transparency \downarrow,
$$

只要其他核心 relation 保持：

$$
A
$$

可以維持高值。

---

# 10. EXP-01 初步理論結論

### 命題 01-A

$$
\boxed{
Transparency \downarrow
\not\Rightarrow
SensualityCollapse
}
$$

### 命題 01-B

$$
\boxed{
\text{Single Surface Parameter}
\neq
\text{Whole-character Appeal Determinant}
}
$$

### 命題 01-C

$$
\boxed{
\text{Character-specific sensual tension}
\text{ can be redundantly distributed}
}
$$

### 命題 01-D

提高遮蔽後，魅力不一定消失，而可能出現：

$$
\text{Direct Reveal}
\rightarrow
\text{Mystery / Formality / Controlled Allure}
$$

的重分配。

---

# 11. EXP-01 輕微 Collateral Enhancement

本次並非完美單變量 A/B。

觀察到：

1. 臉部有輕微精緻化；
2. 手與蛇局部細節有些微變化；
3. 衣料紋理與裝飾也被順手精修。

因此實驗類型更精確地是：

$$
\boxed{
\text{Controlled Edit with Mild Collateral Enhancement}
}
$$

而不是：

```text
perfect single-variable intervention
```

---

# 12. EXP-01 結果判定

## Overall Disposition

`HIT / mild collateral enhancement`

子項：

| Prediction | Result |
|---|---|
| Transparency ↓ | HIT |
| MaterialWeight ↑ | HIT |
| Reveal ↓ | HIT |
| Conceal ↑ | HIT |
| BodylineSalience 小幅 ↓ | PARTIAL / weak |
| Mystery ↑ | HIT |
| Formality ↑ | HIT |
| SensualTension 小至中幅 ↓ | PARTIAL — 實際保持程度高於預期 |
| Identity / Pose / Garment Core 保持 | HIT |
| 完全單變量控制 | MISS — 有輕微 collateral enhancement |

---

# 13. EXP-00 與 EXP-01 的共同發現

兩個實驗共同指出：

# **角色視覺語義具有冗餘與耦合。**

即：

$$
\boxed{
\text{One Meaning}
\not\leftrightarrow
\text{One Visual Parameter}
}
$$

更合理：

$$
Meaning
=
f(
D_1,D_2,\dots,D_n,
Interactions
).
$$

---

# 14. Coupling + Redundancy

EXP-00 顯示：

```text
gaze effect
```

與：

```text
body orientation
```

耦合。

EXP-01 顯示：

```text
sensual appeal
```

由：

```text
transparency
+
pose
+
gaze
+
exposure topology
+
bodyline
+
symbolic motif
```

共同承擔。

所以：

$$
\boxed{
\text{Visual Semantics}
=
\text{Coupled}
+
\text{Redundantly Encoded}
}
$$

是一個值得後續正式測試的假說。

---

# 15. 對 VUSD Paper 03 的意義

Paper 03 主張：

$$
\text{Shared Relation}
\neq
\text{Experienced Meaning}.
$$

EXP-01 正好顯示：

```text
Reveal / Conceal
```

明顯變化，

但：

```text
整體角色吸引力
```

沒有等比例下降。

所以：

$$
\Delta U_i
\neq
\Delta M_O
$$

具有初步經驗支持。

---

# 16. 對 VUSD Paper 04 的意義

Paper 04 提出：

$$
\Delta D
\rightarrow
\Delta P
\rightarrow
\Delta U
\rightarrow
\Delta M_O.
$$

EXP-01 是第一個在此對話中：

```text
先寫預測
→ 再生成
→ 再觀察
```

的完整 Pilot。

因此可作為：

# **Early Counterfactual Evidence Sample**

但不能擴張成普遍美術定律。

---

# 17. 對 Appeal-Preserving Style Transformation 的意義

既有命題：

$$
StyleTransformation
\neq
CharacterRedesign.
$$

EXP-01 顯示：

> 材質調整可以在保持角色核心 appeal 的情況下完成。

所以：

$$
\boxed{
\text{Material Edit}
\neq
\text{Audience Appeal Rewrite}
}
$$

如果其他 semantic locks 有效。

---

# 18. 對 Character-Specific Expressive Override 的意義

本角色具有：

```text
高綠色飽和
蛇紋
薄紗 / 披帛
危險誘惑
```

這些不是 Style Core 本身。

所以：

$$
\boxed{
\text{Style Core}
\neq
\text{Character-Specific Expression}
}
$$

需要獨立保存：

```text
CharacterExpressiveProfile
```

---

# 19. 對 RVGR 的意義

兩輪實驗共同呈現：

$$
Generate
\rightarrow
Observe
\rightarrow
Diagnose
\rightarrow
Rewrite
\rightarrow
Reobserve.
$$

但因 ChatGPT UI 限制，中間存在：

```text
Human Continuation Gate
```

因此此處只能稱：

# **Human-Gated L0 Reflexive Visual Revision Pilot**

不能稱：

```text
Autonomous RVGR Runtime
```

---

# 20. 對 AADS / RABCL 的重要意外發現

第一次嘗試 EXP-01 時，高階 reasoning 與大量：

```text
exposure
bodyline
sensual tension
reveal / conceal
```

語義被一起送入生成環境，觸發安全防護，導致 Provider 拒絕生成。

後來將執行指令縮減為：

> 僅將薄紗調得更不透明、更有布料厚度，其餘保持。

即可正常生成。

這提供一個重要工程證據：

$$
\boxed{
\text{Reasoning Representation}
\neq
\text{Provider Prompt}
}
$$

---

# 21. Semantic Compiler Requirement

AADS / VUSD 可以內部保存：

```text
完整意圖
Shared-Domain target
appeal rationale
counterfactual prediction
```

但 RABCL 應編譯成：

```text
最小充分執行指令
```

形式：

$$
\boxed{
HighLevelReasoning
\rightarrow
MinimalExecutionInstruction.
}
$$

---

# 22. Provider Prompt Leakage Failure

此次失敗可暫時分類：

# `F-PROMPT-01 — Reasoning-to-Execution Leakage`

定義：

> 高階分析語義被不必要地直接傳遞給 Provider，造成安全誤判、注意力污染或執行偏移。

---

# 23. 建議架構修正

```text
VUSD / AADS
    ↓
Full Rationale
    ↓
RABCL
    ↓
Execution Compiler
    ↓
Minimal Provider Instruction
    ↓
Provider
```

Provider 不需要知道：

> 完整美術論文式理由。

它只需要知道：

> 這一步要改什麼。

---

# 24. 實驗證據強度分級

## EXP-00

```text
Evidence Grade:
PILOT / OBSERVATIONAL
```

不可用於：

```text
claiming preregistered prediction success
```

---

## EXP-01

```text
Evidence Grade:
PRE-REGISTERED PILOT
```

但仍受：

```text
single sample
generator collateral drift
single main human observer
single primary multimodal evaluator
```

限制。

---

# 25. 目前不能宣稱的事情

這兩個實驗不能證明：

```text
所有人物立繪都符合這些關係
所有文化都同樣理解
所有 AI 都能可靠判斷
透明度與魅力存在固定函數
VUSD 已被全面實證
```

---

# 26. 可以合理記錄的事情

目前可以寫：

1. VUSD Shared-Domain decomposition 可以實際指導圖像比較；
2. 預註冊的局部 visual counterfactual 在單一樣本中具可觀察預測力；
3. 角色 appeal 顯示多因子冗餘；
4. gaze 與 body orientation 顯示 operator coupling；
5. Provider execution prompt 應與高階 reasoning 分離；
6. human-gated L0 reflexive revision 可在現有介面運作。

---

# 27. 下一階段建議

本對話若繼續測試，可採少量、高資訊量實驗。

## EXP-02 — Gaze / Body Orientation Controlled Test

真正預註冊：

```text
只改 gaze / head orientation 的最小因果閉包
```

測：

$$
Reciprocity,
DirectionalConflict,
ViewerBinding,
ApproachAvoidanceTension.
$$

---

## EXP-03 — Palette Saturation Counterfactual

鎖定：

```text
identity
pose
material
garment
```

只改：

$$
AccentSaturation.
$$

測：

```text
salience
danger cue
richness
style coherence
```

---

## EXP-04 — Snake Motif Reduction

降低：

```text
snake visual prominence
```

但保留人物。

測：

```text
thematic identity
danger cue
contour repetition
character distinctiveness
```

---

# 28. 本地端建議接手項目

本地 EveAtelier / RVGR 應接：

```text
automated A/B variant generation
shared-state extraction
counterfactual record storage
prediction vs observation comparison
multi-model evaluator
human review UI
```

---

# 29. Canonical Experiment Record Schema

建議未來統一：

```json
{
  "experimentId": "VUSD-EXP-01",
  "status": "PRE_REGISTERED_PILOT",
  "artifactBefore": "...",
  "artifactAfter": "...",
  "intervention": {},
  "lockedVariables": [],
  "predictedDelta": {},
  "observedDelta": {},
  "collateralChanges": [],
  "observerResults": [],
  "disposition": "HIT",
  "limitations": []
}
```

---

# 30. 最終整合結論

EXP-00 與 EXP-01 雖然只是很早期的兩個視覺實驗，但共同提供了一個比「AI 好像懂美術」更具體的方向：

$$
\boxed{
\text{AI Visual Judgment}
\text{ can be decomposed into testable relational predictions}.
}
$$

EXP-00 顯示：

$$
\text{Gaze}
$$

不能脫離：

$$
\text{Body Orientation}
$$

理解。

EXP-01 則顯示：

$$
\text{Transparency}
$$

不能直接等同：

$$
\text{Whole-character Sensuality}.
$$

所以更合理的視覺模型是：

$$
\boxed{
\text{Meaning}
=
f(
\text{Multiple Visual Decisions},
\text{Relations},
\text{Observer},
\text{Context}
)
}
$$

而不是：

```text
一個美術特徵
=
一個固定感受
```

這正是 VUSD 所提出：

$$
Artifact
\rightarrow
PerceptualRelation
\rightarrow
SharedDomain
\rightarrow
ObserverProjection
$$

的初步實驗化。

目前最重要的工程結論則是：

$$
\boxed{
\text{Reasoning Layer}
\neq
\text{Execution Layer}
}
$$

以及：

$$
\boxed{
\text{Human-Gated Pilot}
\neq
\text{Autonomous RVGR Runtime}.
}
$$

因此，這兩個實驗最適合作為：

> **VUSD / RVGR 從理論走向真正 MVP 驗證的第一批種子紀錄。**

---

**End of VUSD / RVGR EXP-00 + EXP-01 Combined Experimental Record — v0.1**
