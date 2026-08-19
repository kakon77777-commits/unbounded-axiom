# Anti-Homogenization Rules v0.4

## Core Principle

不要讓輸出落入：

```text
好看，但毫無辨識度，而且一看就像常見 AI 網紅圖
```

## Rule Families

### 1. Face Template Penalty
- 避免單一審美模板反覆出現。
- 避免過度光滑皮膚與一致化五官比例。

### 2. Composition Template Penalty
- 避免反覆使用相同半身正面構圖。
- 若題材允許，優先引入敘事型構圖與視覺節奏。

### 3. Material Logic Penalty
- 工業題材避免無意義亂細節。
- 厚塗題材避免泥化與假筆觸。

### 4. Style Overbinding Penalty
- 避免過度依賴單一作者名 LoRA。
- 先使用中性特徵配方，再局部接 adapter。

## Operational Guideline

若同時使用：
- 作者名參考
- LoRA
- 參考圖
- prompt recipe

則建議限制直接命名風格權重：

$$
0 \leq w_{named\_style} \leq 0.35
$$

其餘風格資訊分配給：
- 線條
- 色彩
- 材質
- 構圖
- 光影
- 世界觀物件語彙
