# Anima Dataset Ingestion Spec v0.1
## 將 Anima / Danbooru Artist Tag Gallery 轉換為 Model-Conditioned Style Observation Database

**版本：** v0.1  
**日期：** 2026-08-14  
**用途：** Global Artist Map / Style Kernel Searcher / GAR / AADS / Closed-Loop Runtime

---

# 0. 核心定位

本規格的最重要原則是：

$$
\boxed{
\text{Artist Style}
\neq
\text{Anima Response to Artist Tag}
}
$$

因此外部 Anima artist gallery 的資料不直接寫成：

```text
artist = style
```

而是寫成：

$$
O_{a,m,p}
=
Observation(
artist\_tag=a,
model=m,
prompt=p
)
$$

其中：

- $a$：artist tag
- $m$：model / model version
- $p$：fixed control prompt / benchmark condition
- $O$：在該條件下得到的 model-conditioned visual observation

這能避免把「模型如何理解某 artist tag」誤寫成「藝術家的真實風格本體」。

---

# 1. 為什麼這個資料源有價值

Anima Style Explorer 類資料有三個非常適合研究的特性：

1. 大規模 artist tag 節點；
2. 固定 control prompt 下的 preview；
3. Works / dataset-strength 與 Uniqueness 類欄位。

這意味著我們可以把它當成：

> **External Model-Conditioned Style Observation Dataset**

而不是單純畫師名錄。

---

# 2. 三層資料模型

```text
Artist Identity Layer
        ↓
Model-Conditioned Observation Layer
        ↓
Derived Style Kernel Layer
```

---

## 2.1 Artist Identity Layer

只記錄「身份／tag／來源」：

```yaml
artist_tag_id: artisttag://anima/example
source_system: anima
artist_tag_raw: "@example"
artist_tag_normalized: "example"
canonical_name: null
aliases: []
taxonomy: danbooru_based
```

這一層不做風格判定。

---

## 2.2 Model-Conditioned Observation Layer

記錄特定模型與 benchmark 條件下的觀測：

```yaml
observation_id: observation://anima2b/example/base-preview-01
artist_tag_id: artisttag://anima/example
model_family: Anima
model_version: 2B
benchmark_prompt_id: benchmark://anima/fixed-control/default
works_count: null
uniqueness_score: null
preview_url: null
preview_hash: null
```

---

## 2.3 Derived Style Kernel Layer

這一層才是我們自己的分析：

```yaml
style_kernel_id: kernel://anima2b/example/base-preview-01
observation_id: observation://anima2b/example/base-preview-01
line_to_painterly: null
flat_to_volumetric: null
muted_to_saturated: null
minimal_to_dense: null
organic_to_industrial: null
bright_to_dark: null
stylized_to_realist: null
static_to_dynamic: null
```

八維沿用目前 Global Artist Style Map：

$$
K=(L,V,S,D,I,B,R,M)
$$

---

# 3. Tier 系統

目前資料庫應分三個 Tier：

## Tier A — Curated Anchor Nodes

我們已人工拆解與核對的高品質畫師節點。

用途：

- 語意錨點
- 校正 Style Kernel
- 人工 benchmark
- Router 的可信參考

---

## Tier B — External Observed Artist Nodes

由 Anima / Illustrious / NoobAI 等 Style Explorer 匯入的大規模 artist tags。

它們代表：

> 模型對 tag 的標準化視覺響應。

---

## Tier C — Auto-Derived Style Nodes

由 AI / vision analyzer 從 preview 自動估計：

```text
line
palette
lighting
composition
anatomy
texture
material
style embedding
8D style kernel
```

這一層必須帶：

```text
analyzer_version
confidence
source_observation_id
```

---

# 4. Canonical Output Files

v0.1 正式定義四個核心資料檔：

```text
artist_tag.csv
style_observation.jsonl
style_kernel.jsonl
source_provenance.json
```

另加：

```text
source_adapter_contract.json
field_mapping.csv
ingestion_pipeline.json
```

---

# 5. artist_tag.csv

建議欄位：

```text
artist_tag_id
source_system
artist_tag_raw
artist_tag_normalized
canonical_name
aliases_json
taxonomy
works_count
uniqueness_score
uniqueness_rank
source_record_url
first_seen_at
last_seen_at
```

### 注意

`works_count` 只能解釋為：

> 該 source / model / dataset context 中的近似資料量或 tag 強度訊號。

不可解釋成藝術家影響力、品質或真實作品總數。

---

# 6. style_observation.jsonl

每一行代表一次**模型條件觀測**。

必要欄位：

```text
observation_id
artist_tag_id
source_system
model_family
model_version
benchmark_prompt_id
preview_index
preview_url
preview_mime
preview_hash
works_count_snapshot
uniqueness_snapshot
fetched_at
```

可選：

```text
seed
sampler
scheduler
steps
cfg
resolution
quality_tags
other_generation_metadata
```

如果來源沒有提供，就必須是 `null`，不可推測。

---

# 7. style_kernel.jsonl

由我們自己的 vision analyzer 產生。

核心欄位：

```text
style_kernel_id
observation_id
analyzer_id
analyzer_version
confidence
```

八維：

```text
line_to_painterly
flat_to_volumetric
muted_to_saturated
minimal_to_dense
organic_to_industrial
bright_to_dark
stylized_to_realist
static_to_dynamic
```

擴展欄位：

```text
line_density
edge_sharpness
palette_entropy
color_temperature
value_contrast
texture_density
face_geometry_signature
composition_signature
material_signature
style_embedding_uri
```

---

# 8. source_provenance.json

每一個 ingestion run 必須保存：

```text
source_name
source_url
source_type
source_license
source_terms_status
source_repository
source_revision
crawler_version
fetched_at
record_count
image_binary_policy
notes
```

這使未來可以知道：

> 這一批資料到底是從哪一版 source 進來的。

---

# 9. Preview Image Policy

v0.1 預設：

$$
\boxed{
\text{Metadata First, Image Mirroring Off by Default}
}
$$

也就是第一階段只存：

```text
preview URL
preview index
content hash（若實際研究快取有取得）
source attribution
```

不預設把外部 preview 圖大量重新發布到我們的公共資料庫。

研究環境若需要 vision analysis，可以建立：

```text
local_research_cache
```

但 cache 與公開資料庫分離。

---

# 10. Image Cache 狀態

```text
not_requested
queued
cached_private
hash_verified
analysis_complete
evicted
blocked
```

---

# 11. Source Adapter

不同外部 gallery 欄位不同，因此 ingestion core 不直接依賴特定網站 DOM。

每個來源實作一個 Adapter：

```text
Source Adapter
    ↓
Raw Record
    ↓
Normalizer
    ↓
Canonical Artist Tag
    ↓
Canonical Observation
```

最小 contract：

```text
probe_source()
list_records()
parse_artist_tag()
parse_works_count()
parse_uniqueness()
parse_preview_urls()
parse_source_metadata()
normalize_record()
```

---

# 12. v0.1 Source Adapters

預留三個：

```text
adapter://mooshie/anima-style-gallery
adapter://thetacursed/anima-style-explorer
adapter://nregret/anima-tools-datajs
```

其中第三個特別適合作為機器化 ingestion source，因為公開專案明確描述 `data.js` 為 40,000+ 詳盡畫師資料，並包含 CDN 映射與 uniqueness 資料。

---

# 13. Source Priority

建議：

```text
Tier 1: structured source file / repo data
Tier 2: official gallery metadata endpoint
Tier 3: rendered DOM scrape
Tier 4: manual fallback
```

也就是：

> 有 data.js / JSON / index file 就不要靠瀏覽器畫面 OCR 或 DOM 猜。

---

# 14. Artist Tag Normalization

Anima artist syntax 通常使用：

```text
@artist_tag
```

我們拆成：

```text
artist_tag_raw       = "@foo"
artist_tag_normalized = "foo"
```

永遠保留 raw，不只保存 normalized。

---

# 15. Alias 與 Identity

Danbooru artist tag 不一定等於真實姓名。

因此：

```text
artist_tag_normalized
```

與：

```text
canonical_name
```

必須分離。

只有外部可信 identity resolution 成功後，才填 canonical name。

---

# 16. Works Count

保存兩層：

```text
works_count_current
works_count_observation_snapshot
```

原因：外部 source 可能更新。

---

# 17. Uniqueness

保存：

```text
uniqueness_score
uniqueness_rank
uniqueness_source
```

若 source 只提供 rank，不能自行反推出 score。

---

# 18. 固定 Benchmark Prompt

如果來源宣稱所有 preview 使用固定 control prompt，資料庫應保存：

```text
benchmark_prompt_id
```

即使 prompt 文字本身暫時未知，也先記：

```text
benchmark://anima/fixed-control/unknown-v1
```

直到 source 能被驗證。

不可自創 control prompt 後假裝是 source 原始 prompt。

---

# 19. Multiple Preview Support

目前 gallery 類工具可能出現多 preview。

所以 observation 必須使用：

```text
preview_index
```

而不能假設：

```text
one artist = one image
```

---

# 20. Model-Conditioned Matrix

未來對同一 artist tag，可以有：

```text
Anima
Illustrious
NoobAI
Flux / other models
```

因此：

$$
K_{a,m_1}
\neq
K_{a,m_2}
$$

本資料模型天然支援：

```text
artist_tag_id
    ├── observation: Anima
    ├── observation: Illustrious
    └── observation: NoobAI
```

---

# 21. Cross-Model Style Drift

可以定義：

$$
\Delta K(a;m_1,m_2)
=
K_{a,m_1}-K_{a,m_2}
$$

研究：

> 不同模型到底如何解讀同一個 artist tag？

這會成為非常重要的資料產品。

---

# 22. Anchor Calibration

Tier A 人工 Anchor 可以用來校正 Tier C 自動 Style Kernel。

例如：

```text
Anima observation
→ AI analyzer
→ predicted kernel
→ compare curated anchor
→ calibrate analyzer
```

---

# 23. Ingestion Pipeline

```text
DISCOVER SOURCE
    ↓
FETCH STRUCTURED RECORDS
    ↓
NORMALIZE TAG IDENTITY
    ↓
STORE ARTIST TAG
    ↓
STORE MODEL-CONDITIONED OBSERVATION
    ↓
OPTIONAL PRIVATE PREVIEW CACHE
    ↓
VISION ANALYSIS
    ↓
DERIVE STYLE KERNEL
    ↓
NEAREST-NEIGHBOR / CLUSTER BUILD
    ↓
GAR / SEARCHER INDEX
```

---

# 24. Idempotency

每次 ingestion 必須可重跑。

主 key：

```text
(source_system, artist_tag_normalized, model_version, preview_index)
```

避免同一批 source 重跑後產生無限重複資料。

---

# 25. Update Detection

如果：

```text
works count changed
uniqueness changed
preview URL changed
preview hash changed
```

不要直接覆蓋歷史 observation。

建立新的：

```text
observation_revision
```

---

# 26. Tombstone

若 source 移除某 artist tag：

```text
deleted_at
source_status = removed
```

不要刪掉歷史研究資料。

---

# 27. Confidence

每個 derived kernel 必須保存：

```text
confidence_global
confidence_line
confidence_palette
confidence_composition
...
```

因為固定 benchmark preview 可能不足以觀察藝術家的所有視覺維度。

---

# 28. Bias Warning

固定 benchmark prompt 有一個巨大優點：控制變量。

但也有明顯限制：

> 它觀察的是「某 artist tag 對同一題目的模型反應」，不是藝術家所有題材、年代、媒材的完整分布。

因此：

$$
O_{a,m,p}
\neq
StyleDistribution(a)
$$

---

# 29. DataStrength

可以從 Works 建立：

$$
DataStrength(a,m)
$$

但其解釋只能是：

> source/model context 下的資料支撐量 proxy。

不可當成：

```text
藝術價值
知名度
技術力
```

---

# 30. ModelUniqueness

同理：

$$
ModelUniqueness(a,m)
$$

只是：

> 模型對該 tag 響應的獨特性訊號。

不是藝術史上的 absolute uniqueness。

---

# 31. Database Integration

匯入完成後：

```text
Anima Dataset
↓
Style Observation DB
↓
Style Kernel DB
↓
Global Artist Graph
↓
Style Kernel Searcher
↓
Style Combiner
↓
Prompt Compiler
↓
GAR
```

---

# 32. v0.1 不做的事

本版不：

1. 批量公開鏡像所有 preview 圖；
2. 宣稱 artist tag 等於真實作者完整風格；
3. 自動把 Works 解釋成藝術家作品總數；
4. 自動把 uniqueness 解釋成藝術價值；
5. 未驗證就填 canonical identity；
6. 假設每個 artist 只有一張 preview；
7. 假設 Anima 與其他模型對 tag 的理解相同。

---

# 33. v0.1 最小成功條件

1. 可以 ingest 至少一種 structured source。
2. 產生 `artist_tag.csv`。
3. 產生 `style_observation.jsonl`。
4. 保留完整 provenance。
5. 允許 preview metadata without image mirroring。
6. 可以讓 analyzer 寫回 `style_kernel.jsonl`。
7. 可以 merge 進現有 8D Style Map。
8. ingestion 可重跑且不重複。

---

# 34. 建議實作順序

## Phase A — Metadata Census

先拿下：

```text
artist tag
works
uniqueness
preview URLs
source revision
```

## Phase B — Private Analysis Cache

只對需要分析的 preview 做 local cache。

## Phase C — Style Analyzer

產八維 kernel + extended descriptors。

## Phase D — Cross-Model Join

加入 Illustrious / NoobAI observations。

## Phase E — Search / GAR Integration

把數萬節點正式接進 Style Kernel Searcher。

---

# 35. 最終定位

這個資料庫不應叫：

> 畫師真實風格資料庫

而應叫：

$$
\boxed{
\textbf{Model-Conditioned Artist Style Observation Database}
}
$$

它研究的其實是：

> **artist tag × dataset × model × benchmark prompt → visual response**

這比單純保存畫師名字更有研究價值，也能直接成為 AADS / GAR / Closed-Loop Runtime 的大規模風格導航層。
