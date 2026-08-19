# GLOBAL STYLE KERNEL SEARCHER v0.3

**性質：** 可查詢的風格搜尋器原型  
**用途：** 讓 AADS / GAR / Prompt Compiler 由一句自然語言需求，返回最接近的畫師節點、混合配方與路徑配方。  
**依賴資料：**
- `artist_keyword_style_map.csv`
- `style_combiner_recipes.csv`
- `style_path_recipes.csv`

---

## 1. 核心目的

v0.1 解決：畫師節點與畫風座標的建立。  
v0.2 解決：節點之間的混合配方。  
v0.3 解決：**一句需求如何查詢到最近的 Style Kernel，並回傳可直接用於生成的候選方案。**

---

## 2. 整體流程

```text
自然語言需求
    ↓
Lexicon Parser
    ↓
Target Axes / Region / Flags
    ↓
Artist Ranker
    ↓
Hybrid Recipe Ranker
    ↓
Path Recipe Ranker
    ↓
Prompt Compiler / AADS / GAR
```

對應形式：

$$
Q \to P(Q) \to K_t \to \mathcal{N}(K_t)
$$

其中：
- $Q$：使用者查詢
- $P(Q)$：解析器輸出
- $K_t$：查詢的目標風格向量
- $\mathcal{N}(K_t)$：附近的畫師／配方鄰域

---

## 3. 八維風格座標

$$
K=(L,V,S,D,I,B,R,M)
$$

- $L$：Line → Painterly
- $V$：Flat → Volumetric
- $S$：Muted → Saturated
- $D$：Minimal → Dense
- $I$：Organic → Industrial
- $B$：Bright → Dark
- $R$：Stylized → Realist
- $M$：Static → Dynamic

---

## 4. 查詢解析

搜尋器先把自然語言轉成：
- 目標軸值 `target_axes`
- 區域偏好 `preferred_regions`
- 旗標，例如 `anti_homogenization = true`

例如：

```text
低飽和、空氣感、偏日式、不要太網紅臉
```

會被近似解析成：
- 低飽和
- 中低亮度／有空氣透視
- 偏日本地區
- 抑制 generic commercial beauty-face

---

## 5. 排名結果

每個查詢會返回三層：
1. **Top Artists**
2. **Top Hybrid Recipes**
3. **Top Style Paths**

這讓系統可以同時回答：
- 最近的單一節點是誰？
- 最近的二元混合配方是什麼？
- 最近的三段式風格路徑是什麼？

---

## 6. 這版輸出檔案

- `style_kernel_searcher_schema.json`
- `style_kernel_lexicon.csv`
- `style_kernel_query_examples.csv`
- `style_kernel_demo_results.json`
- `style_kernel_demo_summary.csv`

---

## 7. 示範查詢

本版內建 10 組示範查詢：
1. 低飽和、空氣感、偏日式、不要太網紅臉
2. 墨線、機械、黑白、動態、工業
3. 空靈、裝飾、夢幻、長髮、華麗
4. 厚塗、史詩、奇幻、角色與大場景
5. 工業科幻、巨大結構、陰冷、低飽和
6. 高飽和、潮流、海報感、角色設計
7. 水墨、武俠、黑白灰、妖怪山林
8. 童話、古典、書籍插畫、裝飾感
9. 復古未來、設計感、乾淨透視、機械
10. 電影感、都市夜景、青春人物、空氣感

---

## 8. 對 AADS 的價值

AADS 不再需要直接把「畫師名字」作為最終生成指令，而可以做：

```text
query
→ style kernel search
→ choose artists / hybrid recipes / paths
→ compile into neutral feature recipe
→ bind model / LoRA / reference / control assets
```

也就是：

$$
Intent \to StyleSearch \to StyleRecipe \to Generation
$$

---

## 9. Anti-Homogenization

本版加入非常初步的 `anti_homogenization`。  
它會對過於 generic、過度商業化、容易落入「AI 網紅臉」傾向的節點做懲罰。

之後可進一步變成：
- face-template penalty
- generic composition penalty
- over-polished character penalty
- over-saturated social-art penalty

---

## 10. 下一步 v0.4

最自然的下一步是 **v0.4 Prompt Compiler + GAR Binding**，也就是直接把查詢結果綁到：
- base model
- LoRA / adapter
- reference set
- control profile
- negative recipe
- anti-homogenization rules

讓輸出不只是「查到誰」，而是「直接可執行」。

---

## 11. 總結

v0.3 代表這整套系統第一次從：

```text
地圖
```

走向：

```text
查詢器
```

也就是把全球畫風資料正式變成：

> **一句描述 → 最近節點 → 混合配方 → 路徑配方 → 可編譯風格方案。**
