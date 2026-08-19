# 全球畫風組合器 / Style Combiner v0.2

**用途：** 把 v0.1 的全球畫師地圖變成可運算的風格組合器  
**產物：**
- `style_combiner_recipes.csv`
- `style_path_recipes.csv`
- `style_combiner_recipes.json`
- 本說明文件

---

## 1. 核心觀念

v0.1 解的是：

> 畫師／風格節點有哪些？

v0.2 解的是：

> 節點之間怎麼混？怎麼產生中間域？怎麼讓 AADS / GAR 直接讀？

每位畫師節點都被視為一個八維向量：

$$
K_a=(L,V,S,D,I,B,R,M)
$$

任兩個節點可以形成：

$$
K_{mix} = \lambda K_a + (1-\lambda)K_b
$$

其中：

$$
0\le \lambda \le 1.
$$

這不是「名字拼接」，而是 **Feature-Space Navigation**。

---

## 2. 組合類型

- **近鄰融合**：距離較近，穩定，適合商用與量產。
- **跨域融合**：距離中等，最有探索價值，容易出現新的合法中間域。
- **對立融合**：距離較遠，適合 frontier search，但需要更強的約束防崩壞。

---

## 3. 前 12 組實用 Recipe

| Recipe ID | A | B | 類型 | 距離 | 建議比例 | 核心關鍵詞 |
|---|---|---|---|---:|---|---|
| mix://style-combiner/001 | 天野喜孝 Yoshitaka Amano | Frank Frazetta | 對立融合 | 123.85 | A:0.60 / B:0.40 | 纖細拉長人物、羽毛般線條、淡彩水彩、金色點綴、新藝術裝飾、空靈幻想、油畫厚塗、強肌肉、野性姿態、黑暗奇幻、暖黑背景、戲劇光 |
| mix://style-combiner/002 | J.C. Leyendecker | Mike Mignola | 對立融合 | 123.82 | A:0.60 / B:0.40 | 雕塑人體、平面刷痕、理想化人物、廣告海報、俐落邊緣、經典服裝、大片黑、角塊形體、極簡陰影、哥德怪談、紅黑配色、雕塑剪影 |
| mix://style-combiner/003 | 新川洋司 Yoji Shinkawa | Pascal Campion | 對立融合 | 123.22 | A:0.60 / B:0.40 | 墨刷、乾筆、黑白高反差、軍事機械、鬆散輪廓、潑墨、動態剪影、暖光日常、家庭、城市、簡化形體、電影構圖 |
| mix://style-combiner/004 | 天野喜孝 Yoshitaka Amano | 阮佳 Ruan Jia | 對立融合 | 116.93 | A:0.60 / B:0.40 | 纖細拉長人物、羽毛般線條、淡彩水彩、金色點綴、新藝術裝飾、空靈幻想、厚塗、史詩奇幻、強明暗、大氣透視、動態人物、巨型場景 |
| mix://style-combiner/005 | 吉田明彥 Akihiko Yoshida | Frank Frazetta | 對立融合 | 110.44 | A:0.60 / B:0.40 | 羊皮紙暖色、短身比例、服裝層次、柔和陰影、奇幻職業設計、油畫厚塗、強肌肉、野性姿態、黑暗奇幻、暖黑背景、戲劇光 |
| mix://style-combiner/006 | Kim Jung Gi | Artgerm / Stanley Lau | 對立融合 | 109.12 | A:0.60 / B:0.40 | 無底稿速寫感、超強透視、多人群像、機械與人體、鋼筆線、複雜場景、超精緻角色封面、乾淨人體、亮麗色彩、柔亮皮膚、英雄海報、商業完成度 |
| mix://style-combiner/007 | Artgerm / Stanley Lau | Sergio Toppi | 對立融合 | 107.11 | A:0.60 / B:0.40 | 超精緻角色封面、乾淨人體、亮麗色彩、柔亮皮膚、英雄海報、商業完成度、雕刻般排線、黑白、碎裂版面、裝飾紋理、強烈面孔、史詩敘事 |
| mix://style-combiner/008 | 新川洋司 Yoji Shinkawa | Krenz Cushart | 對立融合 | 104.56 | A:0.60 / B:0.40 | 墨刷、乾筆、黑白高反差、軍事機械、鬆散輪廓、潑墨、動態剪影、色彩結構、清楚光影、動漫人物、人體設計、邊緣控制 |
| mix://style-combiner/009 | 鄭問 Chen Uen | Pascal Campion | 對立融合 | 104.02 | A:0.60 / B:0.40 | 水墨漫畫、飛白、武俠、歷史人物、強筆勢、粗獷解剖、史詩、暖光日常、家庭、城市、簡化形體、電影構圖 |
| mix://style-combiner/010 | VOFAN | Sergio Toppi | 對立融合 | 102.04 | A:0.60 / B:0.40 | 明亮彩度、光斑、青春少女、都市與天空、廣角、清透動畫色、雕刻般排線、黑白、碎裂版面、裝飾紋理、強烈面孔、史詩敘事 |
| mix://style-combiner/011 | VOFAN | Kim Jung Gi | 對立融合 | 101.43 | A:0.60 / B:0.40 | 明亮彩度、光斑、青春少女、都市與天空、廣角、清透動畫色、無底稿速寫感、超強透視、多人群像、機械與人體、鋼筆線、複雜場景 |
| mix://style-combiner/012 | 吉田明彥 Akihiko Yoshida | 阮佳 Ruan Jia | 對立融合 | 99.91 | A:0.60 / B:0.40 | 羊皮紙暖色、短身比例、服裝層次、柔和陰影、奇幻職業設計、厚塗、史詩奇幻、強明暗、大氣透視、動態人物、巨型場景、筆觸能量 |

---

## 4. 中段 12 組 Recipe

| Recipe ID | A | B | 類型 | 距離 | 建議比例 | 核心關鍵詞 |
|---|---|---|---|---:|---|---|
| mix://style-combiner/013 | Syd Mead | Mike Mignola | 對立融合 | 143.29 | A:0.60 / B:0.40 | 未來工業設計、車輛、建築、乾淨透視、反射材質、企業未來感、大片黑、角塊形體、極簡陰影、哥德怪談、紅黑配色、雕塑剪影 |
| mix://style-combiner/014 | VOFAN | H.R. Giger | 對立融合 | 139.81 | A:0.60 / B:0.40 | 明亮彩度、光斑、青春少女、都市與天空、廣角、清透動畫色、生物機械、灰黑單色、管線骨骼、噴繪、陰冷、異形空間 |
| mix://style-combiner/015 | H.R. Giger | Loish / Lois van Baarle | 對立融合 | 137.93 | A:0.60 / B:0.40 | 生物機械、灰黑單色、管線骨骼、噴繪、陰冷、異形空間、柔和曲線、女性角色、彩色陰影、流動頭髮、動畫感、乾淨數位筆觸 |
| mix://style-combiner/016 | 天野喜孝 Yoshitaka Amano | Syd Mead | 對立融合 | 129.77 | A:0.60 / B:0.40 | 纖細拉長人物、羽毛般線條、淡彩水彩、金色點綴、新藝術裝飾、空靈幻想、未來工業設計、車輛、建築、乾淨透視、反射材質、企業未來感 |
| mix://style-combiner/017 | Alphonse Mucha | James Gurney | 對立融合 | 126.46 | A:0.60 / B:0.40 | 新藝術、花卉框飾、長髮女性、平面海報、柔和色、圓形光環、裝飾線、想像寫實、自然光、傳統媒材、恐龍與文明、可信材質 |
| mix://style-combiner/018 | Artgerm / Stanley Lau | H.R. Giger | 對立融合 | 116.45 | A:0.60 / B:0.40 | 超精緻角色封面、乾淨人體、亮麗色彩、柔亮皮膚、英雄海報、商業完成度、生物機械、灰黑單色、管線骨骼、噴繪、陰冷、異形空間 |
| mix://style-combiner/019 | 吉田明彥 Akihiko Yoshida | Syd Mead | 對立融合 | 104.53 | A:0.60 / B:0.40 | 羊皮紙暖色、短身比例、服裝層次、柔和陰影、奇幻職業設計、未來工業設計、車輛、建築、乾淨透視、反射材質、企業未來感 |
| mix://style-combiner/020 | loundraw | Simon Stålenhag | 對立融合 | 104.44 | A:0.60 / B:0.40 | 透明空氣感、逆光、淺景深、青春人物、天空、柔亮色彩、電影構圖、北歐郊野、巨大機械、陰天、懷舊日常、寫實環境 |
| mix://style-combiner/021 | 早稻 Zao Dao | Artgerm / Stanley Lau | 對立融合 | 104.17 | A:0.60 / B:0.40 | 中國水墨、妖怪、山林、黑白灰、乾濕筆交錯、古意、荒誕、超精緻角色封面、乾淨人體、亮麗色彩、柔亮皮膚、英雄海報 |
| mix://style-combiner/022 | redjuice | 鄭問 Chen Uen | 對立融合 | 95.71 | A:0.60 / B:0.40 | 冷色數位光、纖細角色、SF介面、透明材質、霓虹、精密科技、水墨漫畫、飛白、武俠、歷史人物、強筆勢、粗獷解剖 |
| mix://style-combiner/023 | Frank Frazetta | Mike Mignola | 對立融合 | 134.58 | A:0.60 / B:0.40 | 油畫厚塗、強肌肉、野性姿態、黑暗奇幻、暖黑背景、戲劇光、大片黑、角塊形體、極簡陰影、哥德怪談、紅黑配色、雕塑剪影 |
| mix://style-combiner/024 | 阮佳 Ruan Jia | Mike Mignola | 對立融合 | 130.64 | A:0.60 / B:0.40 | 厚塗、史詩奇幻、強明暗、大氣透視、動態人物、巨型場景、筆觸能量、大片黑、角塊形體、極簡陰影、哥德怪談、紅黑配色 |

---

## 5. 後段 12 組 Recipe

| Recipe ID | A | B | 類型 | 距離 | 建議比例 | 核心關鍵詞 |
|---|---|---|---|---:|---|---|
| mix://style-combiner/025 | WLOP | Mike Mignola | 對立融合 | 126.59 | A:0.60 / B:0.40 | 光滑厚塗、逆光、唯美人物、超長髮、霧氣、華麗服裝、夢幻電影光、大片黑、角塊形體、極簡陰影、哥德怪談、紅黑配色 |
| mix://style-combiner/026 | Jean Giraud / Mœbius | Simon Stålenhag | 對立融合 | 123.19 | A:0.60 / B:0.40 | 清晰細線、平塗色、超現實科幻、巨大空間、奇異生物、乾淨世界建構、北歐郊野、巨大機械、陰天、懷舊日常、寫實環境、冷暖克制 |
| mix://style-combiner/027 | 新川洋司 Yoji Shinkawa | Greg Rutkowski | 對立融合 | 117.32 | A:0.60 / B:0.40 | 墨刷、乾筆、黑白高反差、軍事機械、鬆散輪廓、潑墨、動態剪影、數位厚塗、奇幻景觀、金色逆光、大片雲霧、角色遠景 |
| mix://style-combiner/028 | Kim Jung Gi | Loish / Lois van Baarle | 對立融合 | 112.41 | A:0.60 / B:0.40 | 無底稿速寫感、超強透視、多人群像、機械與人體、鋼筆線、複雜場景、柔和曲線、女性角色、彩色陰影、流動頭髮、動畫感、乾淨數位筆觸 |
| mix://style-combiner/029 | Sergio Toppi | Loish / Lois van Baarle | 對立融合 | 108.26 | A:0.60 / B:0.40 | 雕刻般排線、黑白、碎裂版面、裝飾紋理、強烈面孔、史詩敘事、柔和曲線、女性角色、彩色陰影、流動頭髮、動畫感、乾淨數位筆觸 |
| mix://style-combiner/030 | 鄭問 Chen Uen | Greg Rutkowski | 對立融合 | 106.36 | A:0.60 / B:0.40 | 水墨漫畫、飛白、武俠、歷史人物、強筆勢、粗獷解剖、史詩、數位厚塗、奇幻景觀、金色逆光、大片雲霧、角色遠景 |
| mix://style-combiner/031 | GUWEIZ | Jean Giraud / Mœbius | 對立融合 | 96.73 | A:0.60 / B:0.40 | 城市夜景、低飽和、動漫人物、雨霧、電影逆光、鬆散厚塗、孤獨感、清晰細線、平塗色、超現實科幻、巨大空間、奇異生物 |
| mix://style-combiner/032 | 天野喜孝 Yoshitaka Amano | J.C. Leyendecker | 對立融合 | 95.29 | A:0.60 / B:0.40 | 纖細拉長人物、羽毛般線條、淡彩水彩、金色點綴、新藝術裝飾、空靈幻想、雕塑人體、平面刷痕、理想化人物、廣告海報、俐落邊緣、經典服裝 |
| mix://style-combiner/033 | Mike Mignola | Greg Rutkowski | 對立融合 | 135.54 | A:0.60 / B:0.40 | 大片黑、角塊形體、極簡陰影、哥德怪談、紅黑配色、雕塑剪影、數位厚塗、奇幻景觀、金色逆光、大片雲霧、角色遠景、電影感 |
| mix://style-combiner/034 | 新川洋司 Yoji Shinkawa | WLOP | 對立融合 | 118.25 | A:0.60 / B:0.40 | 墨刷、乾筆、黑白高反差、軍事機械、鬆散輪廓、潑墨、動態剪影、光滑厚塗、逆光、唯美人物、超長髮、霧氣 |
| mix://style-combiner/035 | 新川洋司 Yoji Shinkawa | Loish / Lois van Baarle | 對立融合 | 117.3 | A:0.60 / B:0.40 | 墨刷、乾筆、黑白高反差、軍事機械、鬆散輪廓、潑墨、動態剪影、柔和曲線、女性角色、彩色陰影、流動頭髮、動畫感 |
| mix://style-combiner/036 | loundraw | Mike Mignola | 對立融合 | 94.62 | A:0.60 / B:0.40 | 透明空氣感、逆光、淺景深、青春人物、天空、柔亮色彩、電影構圖、大片黑、角塊形體、極簡陰影、哥德怪談、紅黑配色 |

---

## 6. 三段式風格路徑

本版除了 A × B，也提供 8 組三段式路徑：

```text
空靈裝飾鏈：Mucha -> Amano -> WLOP
墨線機械鏈：Toppi -> Shinkawa -> Nihei
都市空氣感鏈：VOFAN -> loundraw -> GUWEIZ
史詩幻想鏈：Frazetta -> Gurney -> Ruan Jia
復古未來鏈：Mœbius -> Syd Mead -> Range Murata
高密度漫畫鏈：Toppi -> Kim Jung Gi -> Boichi
流行高飽和鏈：Loish -> Mika Pikazo -> Artgerm
黑暗異形鏈：Giger -> Nihei -> Simon Stålenhag
```

---

## 7. 最建議的使用法

不要只說：

```text
A + B
```

而是讓 Agent 讀取：

- `keywords_zh / keywords_en`
- 八維坐標
- `combo_type`
- `suggested_mix_ratio`
- `prompt_recipe_zh / en`

然後再編譯成真正的生成指令。

---

## 8. 和 GAR / AADS 的結合

一組混合配方可以記成：

```yaml
style_mix:
  id: mix://style-combiner/001
  source_nodes:
    - artistref://...
    - artistref://...
  coordinates:
    ...
  features:
    ...
  suggested_mix_ratio: "A:0.50 / B:0.50"
```

這樣就不需要直接依賴人名當最終 Prompt，而是讓名字退回成「導航索引」。

---

## 9. 最值得玩的方向

### A. 空靈裝飾
Mucha × Amano × WLOP

### B. 墨線機械
Toppi × Shinkawa × Nihei

### C. 都市空氣感
VOFAN × loundraw × GUWEIZ

### D. 亞洲史詩幻想
Gurney × 阮佳 × WLOP

### E. 復古未來
Mœbius × Syd Mead × Range Murata

### F. 高彩流行角色
Loish × Mika Pikazo × Artgerm

---

## 10. 下一版可推進

v0.3 可以直接做：

1. **Style Kernel Searcher**：一句描述回傳最近節點與 5 組混合配方  
2. **Anti-Homogenization Filter**：專門避開 generic AI beauty-face  
3. **Prompt Compiler**：輸出 SDXL / Flux / 通用英文版  
4. **Model / LoRA Compatibility Layer**：把每組 recipe 接到 GAR
