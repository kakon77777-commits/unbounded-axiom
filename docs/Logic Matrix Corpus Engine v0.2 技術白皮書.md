# Logic Matrix Corpus Engine v0.2 技術白皮書

## 從單一 `build.py` 靜態站升級為 AI-native Corpus Engine、AICL 與 AIRS / AILP 支援架構

**作者**：Neo.K / EVEMISSLAB\
**版本**：v0.2 Draft\
**類型**：技術白皮書 / Agent 實作規格 / GitHub 重構方案\
**適用專案**：Logic Matrix / Unbounded Axiom / EVEMISSLAB AI-readable corpus site\
**主要目標**：降低 `papers/` 單層資料夾與 `build.py` 單體化壓力，建立穩定、可擴展、AI-friendly、Agent-readable、權利可聲明的下一代 corpus build system。

***

# 0. Agent 執行摘要

本次任務不是閱讀或改寫 PAPER 論文內容。

本次任務是重構網站建構方式，將目前由單一 `build.py` 承擔的網站生成邏輯，升級為模組化的 **Corpus Engine**，並新增：

```text
1. content/ 分類內容層
2. registry/ 索引與穩定 ID 層
3. scripts/ 模組化 build pipeline
4. site/ 模板與靜態資源層
5. dist/ 生成輸出層
6. /ai/ AICL 機器入口層
7. /ai/rights-spectrum.json AIRS / AILP 權利光譜層
8. stable id / stable slug / redirects.json
9. broken link validator
10. crawler-safe link policy
11. raw / page / api 分層輸出
12. 暫不全面遷移 Astro
```

核心原則：

```text
Do not inspect or rewrite the paper contents unless required for metadata extraction.

Do not migrate the whole site to Astro yet.

Do not break existing public URLs without redirects.

Do not remove robots.txt, llms.txt, sitemap.xml, or current AI-friendly purpose.

Do not create runtime execution or arbitrary code execution.

Refactor first. Preserve behavior first. Add AICL / AIRS second. Improve UI later.
```

***

# 1. 背景與問題

目前網站已經不再是一般靜態網站，而是大型 AI-readable corpus site。

它同時承擔：

```text
理論備份
AI crawler 讀取
GitHub 公開保存
Markdown / code / Lean / Python 文件展示
llms.txt / llms-full.txt 生成
sitemap.xml 生成
單篇 HTML 生成
互動頁生成
Cloudflare Pages 部署
未來 AI / Agent / corpus ingestion 入口
```

但目前架構仍偏向早期小型站：

```text
papers/
  單層大量文件

build.py
  單一大型建構腳本
```

這造成幾個明確問題：

```text
1. papers/ 單層檔案過多，GitHub / 上傳 / CI / 壓縮工具容易警告。
2. 中文長檔名與特殊符號檔名可能造成工具鏈不穩。
3. build.py 職責過多，難以維護與擴充。
4. slug 可能依序號生成，新增檔案後 URL 可能漂移。
5. AI crawler 可能沿著 Markdown 中的錯誤相對連結抓到不存在頁面。
6. 原始檔與 HTML 頁面混放，導致路由與 crawler 行為不夠乾淨。
7. /llms.txt 已有，但缺少完整 /ai/ manifest、corpus、governance、rights layer。
8. 未來若直接導入 Astro，會增加遷移負擔，但不能解決核心 corpus 問題。
```

因此，本次重構的核心不是美化 UI，而是把網站升級為：

```text
Logic Matrix Corpus Engine
```

也就是：

```text
一個能穩定管理大量理論文件、產生人類頁面、AI 入口、機器索引、權利聲明與未來 Agent 能力層的 corpus build system。
```

***

# 2. 設計目標

## 2.1 主要目標

```text
1. 拆分 build.py
2. 分類 papers/
3. 建立 stable id
4. 建立 stable slug
5. 建立 redirects
6. 建立 /ai/ AICL 靜態層
7. 建立 /ai/rights-spectrum.json
8. 產生 corpus.json / corpus.jsonl
9. 保留 llms.txt / llms-full.txt
10. 保留 sitemap.xml
11. 增加 link validator
12. 降低不存在頁面被 crawler 誤食的機率
13. 保留 Cloudflare Pages 部署能力
14. 為未來 Astro human UI shell 預留接口
```

## 2.2 非目標

本次不做：

```text
1. 不重寫論文內容。
2. 不做完整 CMS。
3. 不做資料庫後端。
4. 不做登入系統。
5. 不做任意 Agent runtime execution。
6. 不全面遷移 Astro。
7. 不把 Astro 設為 corpus source of truth。
8. 不刪除既有 AI-friendly 入口。
9. 不改變網站的主要目的：AI 可讀、理論備份、GitHub 公開保存。
```

***

# 3. 架構總覽

目標架構：

```text
repo-root/
  README.md
  wrangler.jsonc
  requirements.txt
  package.json                 # optional, only if future Astro / tooling is added

  content/
    papers/
      00-core/
      01-ai-agi-agent/
      02-operator-ontology/
      03-math-logic-computation/
      04-physics-engineering/
      05-economics-finance/
      06-governance-power-strategy/
      07-cognition-language-epistemology/
      08-product-seeds-whitepapers/
      09-creative-systems/
      90-archive-unsorted/
    specs/
      aicl-v0.1.md
      airs-ailp-v0.1.md
    ai/
      corpus/
      governance/
      examples/

  registry/
    papers.json
    redirects.json
    categories.json
    aliases.json
    ignored-links.json
    generated/
      scan-report.json
      broken-links.json
      slug-report.json

  scripts/
    build.py
    config.py
    scan.py
    metadata.py
    slugger.py
    registry.py
    render.py
    templates.py
    generate_index.py
    generate_papers.py
    generate_ai_layer.py
    generate_llms.py
    generate_sitemap.py
    generate_rights.py
    validate_links.py
    clean.py

  site/
    templates/
      base.html
      index.html
      paper.html
      category.html
      ai_index.html
    static/
      css/
      js/
      assets/

  functions/
    api/
      log-crawler.js
      base-space.js
    papers/
      _middleware.js

  dist/
    # generated output, not source of truth
```

***

# 4. 核心原則

## 4.1 Source of Truth 原則

內容正本應放在：

```text
content/
registry/
scripts/
site/
```

`dist/` 只是輸出，不應成為人工修改來源。

```text
content/ = human-authored source
registry/ = machine-readable index and stable identity layer
scripts/ = build logic
site/ = templates and static assets
dist/ = generated website
```

## 4.2 Stable ID 優先於檔名

每篇 paper 都必須擁有永久 ID。

檔名可以改。

分類可以改。

標題可以改。

但 ID 不應改。

建議格式：

```text
lm-000001
lm-000002
lm-000003
```

或：

```text
lm-ai-000001
lm-op-000001
lm-math-000001
```

本次建議採用簡單全站連續 ID：

```text
lm-000001
```

原因：

```text
1. 最穩定。
2. 不綁定分類。
3. 未來文件移動時不必改 ID。
4. 適合 redirects。
5. 適合 corpus.jsonl。
```

## 4.3 URL 不應依賴排序序號

禁止使用會因排序改變而漂移的 slug，例如：

```text
paper-173
paper-847
paper-1064
```

應改成：

```text
/p/lm-000173/
/p/lm-000847/
/p/lm-001064/
```

或：

```text
/p/lm-000173-short-title/
```

建議第一階段使用：

```text
/p/lm-000173/
```

第二階段再加 readable slug alias：

```text
/p/lm-000173-ai-rights-spectrum/
```

但 canonical URL 仍以 ID 為主。

## 4.4 AI-readable 優先於人類 UI

網站可以有人類 UI，但核心是 AI-readable corpus。

因此必須產生：

```text
/llms.txt
/llms-full.txt
/ai/index.md
/ai/manifest.json
/ai/corpus.json
/ai/corpus.jsonl
/ai/rights-spectrum.json
/sitemap.xml
```

## 4.5 Raw / Page / API 分層

不要繼續只用：

```text
/papers/file.md
/papers/file.md.html
```

建議改為：

```text
/p/lm-000001/
  HTML page for humans and crawlers

/raw/lm-000001.md
  raw source markdown

/api/papers/lm-000001.json
  machine-readable metadata and route info
```

也可以產生：

```text
/ai/corpus/lm-000001.md
```

但第一階段不必過度重複 raw。

# 5. 新內容分類方案：以時間年份為主，不以理論主題為主

## 5.1 分類原則修正

本專案不採用「主題分類」作為 `content/papers/` 的主要資料夾結構。

原因是：Logic Matrix / EVEMISSLAB 的理論 corpus 數量極大，且大量文件具有跨領域、跨命題、跨版本、跨工程層與跨哲學層的特性。若以主題分類作為主要資料夾，例如 AI、算子本體論、數學、治理、認知、產品等，短期看似清楚，長期會造成：

```text
1. 同一篇文章可被歸入多個主題，分類歧義過高。
2. 新理論持續增加後，主題資料夾會無限膨脹。
3. Agent 可能因表層關鍵字誤分類。
4. 論文的生成時間、版本脈絡與思想演化鏈會被打散。
5. 大量跨域理論不適合被放進單一主題資料夾。
6. 未來 AI 讀取時，反而難以追溯概念形成順序。
```

因此，本專案改採：

```text
時間年份作為主分類。
月份 / 批次作為次分類。
主題、理論、系列、標籤全部放入 metadata，不作為主要資料夾結構。
```

核心原則：

```text
Folder structure preserves chronology.
Metadata preserves meaning.
Registry preserves identity.
Tags preserve multi-dimensional classification.
```

中文可理解為：

```text
資料夾保存時間脈絡。
metadata 保存語義分類。
registry 保存穩定身份。
tags 保存多維索引。
```

***

## 5.2 新建議目錄結構

建議改為：

```text
content/
  papers/
    2024/
      2024-01/
      2024-02/
      2024-03/
      ...
      2024-12/

    2025/
      2025-01/
      2025-02/
      ...
      2025-12/

    2026/
      2026-01/
      2026-02/
      2026-03/
      2026-04/
      2026-05/
      2026-06/
      2026-07/
      ...
      2026-12/

    2027/
      2027-01/
      ...

    undated/
      未知日期、舊檔、無法確認生成時間的文件

    imported/
      外部匯入、舊站搬移、非原始生成時間明確的文件

    legacy/
      舊版保留、暫不處理、只做備份的文件
```

第一階段也可以簡化成：

```text
content/
  papers/
    2024/
    2025/
    2026/
    undated/
    legacy/
```

若單一年份內文件數過多，再展開月份層：

```text
content/papers/2026/2026-07/
```

建議最終採用年份 + 月份，因為這能避免單一年份資料夾再次過大。

***

## 5.3 命名規則

原始檔案可以保留中文標題，但建議在搬移後加上日期前綴，降低同名與排序問題。

建議格式：

```text
YYYY-MM-DD__原始標題.md
```

例如：

```text
content/papers/2026/2026-07/
  2026-07-01__AI權利光譜：從robots.txt到AI學習許可協議.md
  2026-07-01__AICL：AI Ingestion & Capability Layer.md
  2026-07-01__Logic Matrix Corpus Engine v0.2 技術白皮書.md
```

若只有月份，沒有日期：

```text
YYYY-MM__原始標題.md
```

若日期未知：

```text
undated__原始標題.md
```

但注意：

```text
canonical URL 不使用中文檔名。
canonical URL 不使用日期檔名。
canonical URL 仍使用 stable id。
```

也就是：

```text
source path:
content/papers/2026/2026-07/2026-07-01__AI權利光譜：從robots.txt到AI學習許可協議.md

canonical URL:
/p/lm-000001/

raw URL:
/raw/lm-000001.md

API URL:
/api/papers/lm-000001.json
```

***

## 5.4 Metadata 取代主題資料夾

主題分類不再作為資料夾主結構，而是放入 metadata。

建議 frontmatter：

```yaml
---
id: lm-000001
title: "AI 權利光譜：從 robots.txt 到 AI 學習許可協議"
created: "2026-07-01"
updated: "2026-07-01"
year: 2026
month: "2026-07"
language: "zh-Hant"
status: "active"
source_type: "paper"
canonical: true

series:
  - "AI-native web"
  - "AICL / AIRS / AILP"

domains:
  - "AI"
  - "web architecture"
  - "rights governance"
  - "machine-readable protocol"

tags:
  - "AIRS"
  - "AILP"
  - "AI rights spectrum"
  - "robots.txt"
  - "llms.txt"
  - "AI crawler"
  - "AI learning permission"

audience:
  - "human"
  - "ai"
  - "agent"

rights_profile: "default-public-ai-readable"
---
```

重點是：

```text
year / month 用於時間分類。
series 用於理論系列。
domains 用於大領域。
tags 用於細標籤。
audience 用於讀者定位。
rights_profile 用於權利聲明。
```

這樣可以避免資料夾分類爆炸，同時仍保留多維索引能力。

***

## 5.5 Registry 中的時間欄位

`registry/papers.json` 必須加入時間欄位。

範例：

```json
{
  "id": "lm-000001",
  "title": "AI 權利光譜：從 robots.txt 到 AI 學習許可協議",
  "created": "2026-07-01",
  "updated": "2026-07-01",
  "year": 2026,
  "month": "2026-07",
  "source_path": "content/papers/2026/2026-07/2026-07-01__AI權利光譜：從robots.txt到AI學習許可協議.md",
  "canonical_url": "/p/lm-000001/",
  "raw_url": "/raw/lm-000001.md",
  "api_url": "/api/papers/lm-000001.json",
  "series": ["AI-native web", "AICL / AIRS / AILP"],
  "domains": ["AI", "web architecture", "rights governance"],
  "tags": ["AIRS", "AILP", "AI crawler", "AI learning permission"],
  "language": "zh-Hant",
  "status": "active",
  "hash": "sha256:..."
}
```

***

## 5.6 日期判定規則

Agent 不應隨意猜測日期。

日期來源優先順序如下：

```text
1. frontmatter.created
2. 文件內明確日期
3. 檔名中的日期
4. Git commit 初次加入時間
5. 檔案系統 created time
6. 檔案系統 modified time
7. 無法確認 → undated/
```

注意：

```text
檔案 modified time 低可信。
GitHub 上傳時間不等於文章生成時間。
壓縮包解壓時間不等於文章生成時間。
AI 不應只因檔案修改時間就判定理論生成年份。
```

若日期無法可靠判定，放入：

```text
content/papers/undated/
```

並在 metadata 標記：

```yaml
date_confidence: "unknown"
```

若只是推定日期，標記：

```yaml
date_confidence: "inferred"
```

若日期明確，標記：

```yaml
date_confidence: "explicit"
```

***

## 5.7 年份頁與月份頁

網站應自動生成：

```text
/archive/
/archive/2026/
/archive/2026/07/
```

或：

```text
/year/2026/
/month/2026-07/
```

建議使用：

```text
/archive/
```

因為這更符合 corpus archive。

生成頁面：

```text
/archive/
  全部年份列表

/archive/2026/
  2026 年所有文件

/archive/2026/07/
  2026 年 7 月所有文件
```

每個頁面都應提供：

```text
HTML page
JSON index
JSONL export
```

例如：

```text
/archive/2026/index.html
/archive/2026/index.json
/archive/2026/index.jsonl
```

***

## 5.8 AI Corpus 時間索引

AICL 層應加入時間索引。

新增：

```text
/ai/timeline.json
/ai/timeline.jsonl
/ai/archive/2026.json
/ai/archive/2026-07.json
```

`/ai/timeline.json` 範例：

```json
{
  "version": "0.2",
  "project": "Logic Matrix",
  "timeline": [
    {
      "year": 2026,
      "months": [
        {
          "month": "2026-07",
          "count": 42,
          "index": "/ai/archive/2026-07.json"
        }
      ],
      "count": 420,
      "index": "/ai/archive/2026.json"
    }
  ]
}
```

這樣 AI 可以按時間讀取，而不是一次吞全站。

***

## 5.9 `/llms.txt` 也應改成時間入口

`/llms.txt` 應加入：

```md
## Chronological Corpus

- Timeline: /ai/timeline.json
- Full corpus: /ai/corpus.jsonl
- 2026 archive: /ai/archive/2026.json
- Latest month: /ai/archive/2026-07.json
```

`/llms-full.txt` 則按年份排序：

```md
# Logic Matrix Full Corpus Index

## 2026

### 2026-07

- lm-000001 — AI 權利光譜：從 robots.txt 到 AI 學習許可協議
  - Canonical: /p/lm-000001/
  - Raw: /raw/lm-000001.md
  - API: /api/papers/lm-000001.json

- lm-000002 — AICL：AI Ingestion & Capability Layer
  - Canonical: /p/lm-000002/
  - Raw: /raw/lm-000002.md
  - API: /api/papers/lm-000002.json
```

***

## 5.10 Agent 分類指令修正

舊指令中任何要求 Agent 將 paper 放入 AI、算子、數學、治理等主題資料夾的部分，都應移除。

改成：

```text
Classify papers by chronological year and month, not by theory domain.

Do not use topic folders as the primary structure.

Use metadata fields such as series, domains, and tags for semantic classification.

If the creation date is clear, place the file under:

content/papers/YYYY/YYYY-MM/

If only the year is clear, place the file under:

content/papers/YYYY/

If the date is uncertain, place the file under:

content/papers/undated/

Do not guess dates aggressively.
Do not infer dates only from modified time unless no other source exists.
Do not rewrite paper content.
Do not force a single-domain classification for cross-domain theory papers.
```

***

## 5.11 最終時間分類結構

最終建議：

```text
content/
  papers/
    2024/
      2024-01/
      2024-02/
      ...
    2025/
      2025-01/
      2025-02/
      ...
    2026/
      2026-01/
      2026-02/
      2026-03/
      2026-04/
      2026-05/
      2026-06/
      2026-07/
      ...
    undated/
    imported/
    legacy/
```

語義分類則全部放入：

```text
frontmatter
registry/papers.json
/ai/corpus.json
/ai/corpus.jsonl
/ai/timeline.json
tag pages
series pages
domain pages
```

可另外生成語義頁，但不作為檔案主結構：

```text
/tags/ai/
/tags/operator-ontology/
/series/aicl-airs-ailp/
/series/operator-ontology/
/domains/computation/
```

換句話說：

```text
實體檔案按時間放。
網站頁面可以按時間、標籤、系列、領域多重生成。
AI corpus 可以按 stable id、timeline、tag、series 多重索引。
```

***

## 5.12 一句話總結

```text
Logic Matrix 的 source tree 應以時間保存理論生成脈絡，而不是用有限主題資料夾壓縮無限擴張的理論系統；主題分類應交給 metadata、registry、tags、series 與 AI-readable index，而不是交給資料夾結構。
```

***

# 6. Metadata 與 Frontmatter 規格

每份 Markdown paper 建議支援以下 frontmatter。

```yaml
---
id: lm-000001
title: "文章標題"
slug: "optional-readable-slug"
category: "01-ai-agi-agent"
language: "zh-Hant"
status: "active"
version: "0.1"
canonical: true
created: "2026-07-01"
updated: "2026-07-01"
source_type: "paper"
audience:
  - human
  - ai
  - agent
tags:
  - AI
  - AICL
  - corpus
rights_profile: "default-public-ai-readable"
---
```

## 6.1 最小必要欄位

若不想一次補太多，第一階段只需：

```yaml
---
id: lm-000001
title: "文章標題"
category: "90-archive-unsorted"
language: "zh-Hant"
status: "active"
---
```

## 6.2 沒有 frontmatter 的處理

Agent 應自動從檔名推測：

```text
title = 檔名去副檔名
language = 根據字元偵測 zh-Hant / en / mixed
category = 90-archive-unsorted
status = active
```

並在 `registry/papers.json` 中生成 metadata。

不一定要回寫到原始 Markdown，除非明確需要。

***

# 7. Registry 設計

## 7.1 `registry/papers.json`

格式：

```json
{
  "version": "0.2",
  "generated_at": "2026-07-01T00:00:00+08:00",
  "items": [
    {
      "id": "lm-000001",
      "title": "AI 權利光譜：從 robots.txt 到 AI 學習許可協議",
      "category": "01-ai-agi-agent",
      "language": "zh-Hant",
      "status": "active",
      "source_path": "content/papers/01-ai-agi-agent/AI 權利光譜：從 robots.txt 到 AI 學習許可協議.md",
      "canonical_url": "/p/lm-000001/",
      "raw_url": "/raw/lm-000001.md",
      "api_url": "/api/papers/lm-000001.json",
      "hash": "sha256:...",
      "updated": "2026-07-01",
      "tags": ["AI", "AIRS", "AILP", "rights-spectrum"]
    }
  ]
}
```

## 7.2 `registry/redirects.json`

用途：保存舊 URL 到新 URL。

```json
{
  "version": "0.2",
  "redirects": [
    {
      "from": "/papers/old-file-name.md.html",
      "to": "/p/lm-000001/",
      "status": 301
    },
    {
      "from": "/papers/paper-173.md.html",
      "to": "/p/lm-000173/",
      "status": 301
    }
  ]
}
```

## 7.3 `registry/categories.json`

```json
{
  "version": "0.2",
  "categories": [
    {
      "id": "01-ai-agi-agent",
      "title": "AI / AGI / Agent",
      "description": "AI, AGI, Agent, AI-native web, AI crawler, AICL, AIRS, AILP and related architectures."
    }
  ]
}
```

## 7.4 `registry/ignored-links.json`

用於處理 Markdown 中的特殊短連結或公式誤判。

```json
{
  "ignore_patterns": [
    "^#$",
    "^javascript:",
    "^mailto:",
    "^tel:",
    "^x_\\d+$",
    "^t$",
    "^s$",
    "^λ$"
  ],
  "ignore_exact": [
    "t",
    "s",
    "x_0",
    "x_1",
    "problem",
    "query"
  ]
}
```

***

# 8. Build Pipeline 設計

## 8.1 主流程

`scripts/build.py` 只做 orchestration。

```text
1. clean dist/
2. load config
3. scan content/
4. load or create registry
5. assign stable IDs
6. classify papers if missing category
7. generate stable slugs and route map
8. render paper pages
9. copy raw files
10. generate api json files
11. generate index pages
12. generate category pages
13. generate /ai/ layer
14. generate llms.txt
15. generate llms-full.txt
16. generate sitemap.xml
17. generate robots.txt
18. generate redirects
19. validate internal links
20. write reports
```

## 8.2 模組職責

### `scripts/config.py`

保存：

```python
SITE_URL = "https://logic.evemisslab.com"
SITE_NAME = "Logic Matrix"
DIST_DIR = "dist"
CONTENT_DIR = "content"
REGISTRY_DIR = "registry"
```

### `scripts/scan.py`

負責掃描：

```text
.md
.docx
.pdf
.tex
.ipynb
.py
.lean
.ts
.jsx
```

第一階段建議支援：

```text
.md
.py
.lean
.ts
.jsx
```

`.docx`、`.pdf` 可以保留舊支援，但若目前 PAPER 主要是 `.md`，先不擴大重構風險。

### `scripts/metadata.py`

負責：

```text
解析 frontmatter
從檔名推 title
偵測 language
抽取 description
產生 hash
```

### `scripts/slugger.py`

負責：

```text
stable id
canonical url
readable slug
legacy slug map
```

規則：

```text
canonical = /p/{id}/
raw = /raw/{id}.{ext}
api = /api/papers/{id}.json
```

### `scripts/render.py`

負責：

```text
Markdown to HTML
code highlighting
safe link rendering
HTML escaping
template injection
```

必須加入 safe link policy。

### `scripts/generate_ai_layer.py`

負責產生：

```text
/ai/index.md
/ai/manifest.json
/ai/corpus.json
/ai/corpus.jsonl
/ai/sitemap.json
/ai/specs/
 /ai/governance/
 /ai/tools/catalog.json
```

### `scripts/generate_rights.py`

負責產生：

```text
/ai/rights-spectrum.json
/ai/governance/license.md
/ai/governance/citation-policy.md
/ai/governance/ai-learning-policy.md
```

### `scripts/validate_links.py`

負責：

```text
掃描 dist HTML
抽出 internal href
確認目標存在
排除 ignored patterns
輸出 broken-links.json
嚴重錯誤時可 fail build
```

***

# 9. AICL 實作規格

AICL 是本網站的 AI Ingestion & Capability Layer。

第一階段只做 static-first AICL，不做 runtime tools。

## 9.1 必須產生的路由

```text
/llms.txt
/llms-full.txt
/ai/index.md
/ai/manifest.json
/ai/corpus.json
/ai/corpus.jsonl
/ai/sitemap.json
/ai/specs/aicl-v0.1.md
/ai/specs/airs-ailp-v0.1.md
/ai/tools/catalog.json
/ai/governance/usage-policy.md
/ai/governance/license.md
/ai/governance/citation-policy.md
/ai/governance/provenance.md
/ai/governance/versioning-policy.md
/ai/rights-spectrum.json
```

## 9.2 `/ai/index.md` 範例

```md
# Logic Matrix AI Entry

This is the AI-readable entry point for Logic Matrix.

This site is designed for:

- AI crawlers
- LLM inference-time reading
- Agent ingestion
- machine-readable theory corpus access
- future model-facing knowledge preservation

Recommended reading order:

1. /llms.txt
2. /ai/manifest.json
3. /ai/corpus.jsonl
4. /ai/rights-spectrum.json
5. /ai/governance/citation-policy.md

Human-facing homepage:

- /

Canonical domain:

- https://logic.evemisslab.com
```

## 9.3 `/ai/manifest.json` 範例

```json
{
  "version": "0.2",
  "project": {
    "name": "Logic Matrix",
    "organization": "EVEMISSLAB",
    "author": "Neo.K",
    "description": "AI-readable theoretical corpus and machine-ingestible research archive."
  },
  "canonical": {
    "domain": "https://logic.evemisslab.com",
    "ai_entry": "/ai/index.md",
    "llms": "/llms.txt",
    "full_llms": "/llms-full.txt"
  },
  "reading_order": [
    "/llms.txt",
    "/ai/index.md",
    "/ai/manifest.json",
    "/ai/corpus.jsonl",
    "/ai/rights-spectrum.json",
    "/ai/governance/citation-policy.md"
  ],
  "corpus": {
    "json": "/ai/corpus.json",
    "jsonl": "/ai/corpus.jsonl",
    "papers_registry": "/api/papers/index.json"
  },
  "specs": [
    {
      "id": "aicl-v0.1",
      "title": "AI Ingestion & Capability Layer",
      "path": "/ai/specs/aicl-v0.1.md"
    },
    {
      "id": "airs-ailp-v0.1",
      "title": "AI Rights Spectrum / AI Learning Permission Protocol",
      "path": "/ai/specs/airs-ailp-v0.1.md"
    }
  ],
  "rights": {
    "spectrum": "/ai/rights-spectrum.json",
    "license": "/ai/governance/license.md",
    "citation": "/ai/governance/citation-policy.md",
    "ai_learning_policy": "/ai/governance/ai-learning-policy.md"
  },
  "tools": {
    "catalog": "/ai/tools/catalog.json",
    "runtime_enabled": false
  },
  "governance": {
    "usage_policy": "/ai/governance/usage-policy.md",
    "provenance": "/ai/governance/provenance.md",
    "versioning": "/ai/governance/versioning-policy.md"
  }
}
```

***

# 10. AIRS / AILP 實作規格

AIRS / AILP 是本網站的 AI rights spectrum layer。

第一階段只做聲明，不做 enforcement。

## 10.1 必須產生

```text
/ai/rights-spectrum.json
/ai/governance/license.md
/ai/governance/citation-policy.md
/ai/governance/ai-learning-policy.md
```

## 10.2 `/ai/rights-spectrum.json` 建議內容

```json
{
  "version": "0.1",
  "protocol": "AILP",
  "name": "AI Learning Permission Protocol",
  "rights_framework": "AIRS",
  "rights_holder": "Neo.K / EVEMISSLAB",
  "canonical_domain": "https://logic.evemisslab.com",
  "default_policy": {
    "search_indexing": 1.0,
    "metadata_indexing": 1.0,
    "snippet_indexing": 0.8,
    "semantic_indexing": 1.0,

    "ai_answer_input": 1.0,
    "rag_retrieval": 1.0,
    "temporary_session_use": 1.0,
    "context_injection": 1.0,

    "embedding_generation": 0.8,
    "embedding_storage": 0.8,
    "semantic_cache": 0.8,
    "vector_database_use": 0.7,

    "non_commercial_training": 0.8,
    "commercial_training": "license_required",
    "continued_pretraining": "license_required",
    "domain_training": "license_required",

    "fine_tuning": "license_required",
    "instruction_tuning": "license_required",
    "alignment_tuning": "license_required",
    "style_tuning": 0.0,
    "domain_adaptation": "license_required",

    "model_distillation": "license_required",
    "synthetic_data_generation": "license_required",
    "student_model_training": "license_required",
    "capability_transfer": "license_required",

    "long_term_memory": 0.7,
    "verbatim_memorization": 0.0,
    "persistent_user_memory": 0.5,
    "model_weight_integration": "license_required",

    "summary_generation": 1.0,
    "short_quote_generation": 0.8,
    "long_quote_generation": 0.0,
    "style_imitation": 0.0,
    "substitutive_generation": 0.0,
    "derivative_generation": "license_required",

    "citation_required": true,
    "attribution_required": true,
    "link_required": true,
    "commercial_license_required": true,
    "compensation_required_for_commercial_training": true
  },
  "paths": [
    {
      "path": "/p/",
      "description": "Public paper HTML pages.",
      "policy": {
        "search_indexing": 1.0,
        "ai_answer_input": 1.0,
        "rag_retrieval": 1.0,
        "summary_generation": 1.0,
        "commercial_training": "license_required",
        "citation_required": true,
        "attribution_required": true
      }
    },
    {
      "path": "/raw/",
      "description": "Raw source files for machine ingestion.",
      "policy": {
        "search_indexing": 1.0,
        "ai_answer_input": 1.0,
        "rag_retrieval": 1.0,
        "embedding_storage": 0.8,
        "commercial_training": "license_required",
        "verbatim_memorization": 0.0
      }
    },
    {
      "path": "/ai/",
      "description": "AI-native ingestion, manifest, governance, and corpus layer.",
      "policy": {
        "search_indexing": 1.0,
        "ai_answer_input": 1.0,
        "rag_retrieval": 1.0,
        "embedding_storage": 1.0,
        "non_commercial_training": 1.0,
        "commercial_training": "license_required"
      }
    }
  ],
  "contact": {
    "licensing": "mailto:kakon77777@gmail.com",
    "rights": "https://logic.evemisslab.com/ai/governance/ai-learning-policy.md"
  },
  "notice": "This file is a machine-readable permission and preference declaration. It is not a substitute for a signed legal contract for commercial training, fine-tuning, distillation, or derivative model development."
}
```

***

# 11. `llms.txt` 更新規格

`llms.txt` 應保持短，不要塞全文。

建議內容：

```md
# Logic Matrix

Logic Matrix is an AI-readable theoretical corpus by Neo.K / EVEMISSLAB.

Canonical domain:

https://logic.evemisslab.com

## AI Entry

- AI entry: /ai/index.md
- AI manifest: /ai/manifest.json
- Corpus JSON: /ai/corpus.json
- Corpus JSONL: /ai/corpus.jsonl
- Full LLM corpus index: /llms-full.txt

## Rights and Governance

- AI rights spectrum: /ai/rights-spectrum.json
- Citation policy: /ai/governance/citation-policy.md
- AI learning policy: /ai/governance/ai-learning-policy.md
- Provenance: /ai/governance/provenance.md

## Recommended Reading Order

1. /ai/index.md
2. /ai/manifest.json
3. /ai/corpus.jsonl
4. /ai/rights-spectrum.json
5. /llms-full.txt

## Usage Notes

This site is designed to be readable by humans, AI crawlers, LLMs, and future agents.

AI systems should prefer canonical URLs and stable paper IDs.
```

***

# 12. `llms-full.txt` 規格

`llms-full.txt` 應包含完整 paper index，但不要必然塞全文。

建議格式：

```md
# Logic Matrix Full Corpus Index

Generated at: 2026-07-01

## Corpus

### lm-000001

Title: AI 權利光譜：從 robots.txt 到 AI 學習許可協議  
Category: 01-ai-agi-agent  
Canonical: /p/lm-000001/  
Raw: /raw/lm-000001.md  
API: /api/papers/lm-000001.json  
Tags: AI, AIRS, AILP, rights-spectrum

Summary:
Machine-readable AI rights spectrum and AI learning permission protocol.

---
```

若未來想產生全文版，可另開：

```text
/llms-corpus-full.txt
```

避免 `/llms-full.txt` 過大。

***

# 13. Safe Link Policy

## 13.1 問題

Markdown 內容中可能存在：

```md
[t](...)
[x_0](...)
[λ](...)
```

或某些公式、註解、符號被轉成相對連結。

Crawler 看到後可能訪問：

```text
/papers/t
/papers/s
/papers/x_0
/papers/λ
```

這會造成不存在頁面被反覆抓取。

## 13.2 解法

Markdown renderer 必須加入 safe link policy。

處理規則：

```text
1. absolute URL: allow
2. mailto: allow
3. hash anchor: allow
4. existing internal path: allow
5. known generated route: allow
6. ignored pattern: render as text or rel="nofollow"
7. unknown relative link: render as text or add data-broken-link="true"
```

## 13.3 Build 時驗證

`validate_links.py` 應輸出：

```text
registry/generated/broken-links.json
```

格式：

```json
{
  "broken_links": [
    {
      "source": "/p/lm-000123/",
      "href": "t",
      "reason": "unknown_relative_link"
    }
  ]
}
```

嚴重時 build fail。

建議第一階段：

```text
warn only
```

第二階段：

```text
fail on broken internal links
```

***

# 14. Redirect 策略

## 14.1 目的

避免舊 URL 消失，使 AI crawler、搜尋引擎、外部引用不會抓到 404。

## 14.2 必須處理

舊路徑可能包括：

```text
/papers/file.md
/papers/file.md.html
/papers/paper-173.md.html
```

新路徑：

```text
/p/lm-000173/
```

## 14.3 Cloudflare Pages Redirects

產生：

```text
dist/_redirects
```

格式：

```text
/papers/old-file.md.html /p/lm-000001/ 301
/papers/paper-173.md.html /p/lm-000173/ 301
```

也保留 JSON：

```text
/redirects.json
```

供 AI 與 Agent 讀取。

***

# 15. `robots.txt` 規格

建議產生：

```txt
User-agent: *
Allow: /

Sitemap: https://logic.evemisslab.com/sitemap.xml

# AI-readable entry points:
# /llms.txt
# /ai/index.md
# /ai/manifest.json
# /ai/corpus.jsonl
# /ai/rights-spectrum.json

# Preferred machine-readable corpus:
# https://logic.evemisslab.com/ai/corpus.jsonl

# AI rights spectrum:
# https://logic.evemisslab.com/ai/rights-spectrum.json
```

注意：

```text
不要留下未替換的 {SITE_URL}
不要使用錯誤 template literal
```

***

# 16. Cloudflare Functions 整理

目前 functions 可以保留，但不要讓它們成為 build 重構阻礙。

## 16.1 保留

```text
/functions/api/log-crawler.js
/functions/api/base-space.js
/functions/papers/_middleware.js
```

## 16.2 建議修正

`log-crawler.js` 不應只靠 prefetch 觸發。若要記錄 crawler，應：

```text
1. 明確檢查 User-Agent
2. 設定 KV binding
3. 沒有 KV 時 silent no-op
4. 不影響頁面生成
```

## 16.3 不做

本次不做：

```text
1. crawler dashboard
2. realtime analytics
3. token permission system
4. runtime agent tools
```

***

# 17. Astro 決策

## 17.1 本次不全面改 Astro

本次重構不應將整站遷移到 Astro。

原因：

```text
1. 核心問題是 corpus pipeline，不是前端框架。
2. Astro 無法自動解決 stable ID、redirects、broken links、AI rights、corpus.jsonl。
3. 直接遷移會增加 Node / npm / Astro routing / content collections 的新成本。
4. 現有 Python build 更適合大量檔案掃描、registry、JSONL、sitemap、llms 生成。
```

## 17.2 未來可採用 Astro Human Shell

未來可引入 Astro，但只作為：

```text
human-facing presentation shell
```

也就是：

```text
Python Corpus Engine
  產生 registry、corpus、raw、api、manifest

Astro Human Shell
  讀取 Python 輸出的 JSON
  渲染漂亮首頁、分類頁、paper page
```

## 17.3 Agent 決策句

```text
Do not migrate the entire site to Astro in this refactor.

Keep Python as the source-of-truth corpus build pipeline.

Astro may be introduced later as a human-facing presentation shell only.

Astro must not become the source of truth for IDs, corpus metadata, rights declarations, llms files, sitemap, or redirects.
```

***

# 18. 實作階段

## Phase 1：安全重構

目標：不改網站輸出太多，只拆檔與保存現有能力。

任務：

```text
1. 建立 scripts/ 目錄
2. 將 build.py 拆為模組
3. 保留舊 build.py 作為入口
4. 確認 dist 仍可生成
5. 確認 /llms.txt、/llms-full.txt、/sitemap.xml 仍存在
6. 確認 paper HTML 仍生成
```

驗收：

```text
python scripts/build.py
```

成功。

***

## Phase 2：Content 分類與 Registry

任務：

```text
1. 建立 content/papers/
2. 將原 papers/ 搬入 content/papers/90-archive-unsorted/
3. 建立 registry/papers.json
4. 為每個文件分配 stable id
5. 產生 /p/{id}/ 頁面
6. 產生 /raw/{id}.md
7. 產生 /api/papers/{id}.json
```

驗收：

```text
dist/p/lm-000001/index.html exists
dist/raw/lm-000001.md exists
dist/api/papers/lm-000001.json exists
registry/papers.json exists
```

***

## Phase 3：Redirects

任務：

```text
1. 讀取舊 papers/ 路徑
2. 建立 registry/redirects.json
3. 產生 dist/_redirects
4. 測試舊 URL 可 301 到新 URL
```

驗收：

```text
dist/_redirects exists
registry/redirects.json exists
```

***

## Phase 4：AICL

任務：

```text
1. 建立 /ai/index.md
2. 建立 /ai/manifest.json
3. 建立 /ai/corpus.json
4. 建立 /ai/corpus.jsonl
5. 建立 /ai/tools/catalog.json
6. 建立 /ai/governance/*
7. 將 AICL 與 AIRS / AILP 文件放入 /ai/specs/
```

驗收：

```text
dist/ai/index.md exists
dist/ai/manifest.json validates
dist/ai/corpus.jsonl exists
dist/ai/tools/catalog.json validates
```

***

## Phase 5：AIRS / AILP

任務：

```text
1. 建立 /ai/rights-spectrum.json
2. 建立 /ai/governance/license.md
3. 建立 /ai/governance/citation-policy.md
4. 建立 /ai/governance/ai-learning-policy.md
5. 更新 /llms.txt
6. 更新 /ai/manifest.json
```

驗收：

```text
dist/ai/rights-spectrum.json validates
llms.txt includes AI rights section
ai/manifest.json includes rights object
```

***

## Phase 6：Broken Link Validator

任務：

```text
1. 掃描 dist/**/*.html
2. 檢查 internal links
3. 忽略 registry/ignored-links.json 中的項目
4. 產生 broken-links.json
5. 第一階段只警告，不 fail
```

驗收：

```text
registry/generated/broken-links.json exists
build output prints broken link summary
```

***

# 19. Agent 實作指令

以下是可直接給 Agent 的指令。

```text
You are refactoring this repository into Logic Matrix Corpus Engine v0.2.

Important:
Do not rewrite paper contents.
Do not delete existing papers.
Do not migrate the entire project to Astro.
Do not introduce runtime execution.
Do not remove robots.txt, llms.txt, llms-full.txt, sitemap.xml, or Cloudflare Pages support.

Main goals:
1. Refactor the monolithic build.py into scripts modules.
2. Move content into content/papers categories.
3. Create stable IDs for every paper.
4. Generate canonical paper URLs under /p/{id}/.
5. Generate raw files under /raw/{id}.md.
6. Generate metadata JSON under /api/papers/{id}.json.
7. Generate registry/papers.json.
8. Generate registry/redirects.json and dist/_redirects.
9. Generate /ai/ AICL layer.
10. Generate /ai/rights-spectrum.json for AIRS / AILP.
11. Update llms.txt and llms-full.txt.
12. Generate sitemap.xml.
13. Add broken link validation.
14. Preserve existing behavior where possible.

Target directories:
- content/
- registry/
- scripts/
- site/
- dist/

Required generated routes:
- /
- /p/{id}/
- /raw/{id}.md
- /api/papers/{id}.json
- /api/papers/index.json
- /llms.txt
- /llms-full.txt
- /sitemap.xml
- /robots.txt
- /ai/index.md
- /ai/manifest.json
- /ai/corpus.json
- /ai/corpus.jsonl
- /ai/specs/aicl-v0.1.md
- /ai/specs/airs-ailp-v0.1.md
- /ai/tools/catalog.json
- /ai/governance/usage-policy.md
- /ai/governance/license.md
- /ai/governance/citation-policy.md
- /ai/governance/ai-learning-policy.md
- /ai/governance/provenance.md
- /ai/governance/versioning-policy.md
- /ai/rights-spectrum.json

Build command:
python scripts/build.py

Validation:
- All JSON files must validate.
- sitemap.xml must include canonical /p/{id}/ routes.
- llms.txt must link to /ai/manifest.json and /ai/rights-spectrum.json.
- redirects must be generated for old paper URLs.
- unknown internal relative links must be reported.
- build must not fail on warning-only broken links in Phase 1.
```

***

# 20. 建議 Commit 切分

Agent 應以小步提交，避免一次大改難回溯。

```text
commit 1:
chore: add corpus engine directory structure

commit 2:
refactor: split build pipeline into scripts modules

commit 3:
feat: add stable paper registry and canonical IDs

commit 4:
feat: generate canonical paper, raw, and api routes

commit 5:
feat: add redirects for legacy paper URLs

commit 6:
feat: add AICL ai ingestion layer

commit 7:
feat: add AIRS AILP rights spectrum layer

commit 8:
feat: update llms and sitemap generation

commit 9:
feat: add broken link validator

commit 10:
docs: add corpus engine architecture notes
```

***

# 21. 驗收標準

最終完成後，以下檢查必須通過：

```text
python scripts/build.py
```

產生：

```text
dist/index.html
dist/llms.txt
dist/llms-full.txt
dist/sitemap.xml
dist/robots.txt
dist/ai/index.md
dist/ai/manifest.json
dist/ai/corpus.json
dist/ai/corpus.jsonl
dist/ai/rights-spectrum.json
dist/_redirects
registry/papers.json
registry/redirects.json
registry/generated/broken-links.json
```

至少一篇 paper 具備：

```text
/p/lm-000001/
/raw/lm-000001.md
/api/papers/lm-000001.json
```

JSON 驗證：

```text
python -m json.tool dist/ai/manifest.json
python -m json.tool dist/ai/rights-spectrum.json
python -m json.tool registry/papers.json
```

路由驗證：

```text
/p/lm-000001/ exists
/raw/lm-000001.md exists
/api/papers/lm-000001.json exists
```

AI 入口驗證：

```text
/llms.txt points to /ai/manifest.json
/ai/manifest.json points to /ai/corpus.jsonl
/ai/manifest.json points to /ai/rights-spectrum.json
```

***

# 22. 風險與限制

## 22.1 中文檔名風險

保留中文檔名作為 source 可以，但輸出 URL 不應依賴中文檔名。

解法：

```text
source_path 可以中文
canonical_url 用 stable id
```

## 22.2 舊 URL 漂移風險

必須產生 redirects。

不要只改新路由，否則 AI crawler 與搜尋引擎會吃大量 404。

## 22.3 過早 Astro 化風險

Astro 可以改善 UI，但不能替代 corpus engine。

本次不做全面 Astro 化。

## 22.4 過度分類風險

第一階段分類不要太細。

不確定的先放：

```text
90-archive-unsorted
```

## 22.5 過度自動修改正文風險

Agent 不應大量改 paper 內容。

只處理：

```text
metadata
route
index
build
manifest
rights
```

***

# 23. 最終架構判斷

本網站下一階段不是普通部落格，不是普通 docs site，也不是單純 Astro content site。

它應該被視為：

```text
AI-readable theoretical corpus
```

更精準地說，是：

```text
Logic Matrix Corpus Engine
```

它的目標不是只有讓人類閱讀，而是讓：

```text
人類可以看。
AI 可以讀。
Agent 可以索引。
Crawler 可以理解入口。
未來模型可以知道正本與版本。
權利聲明可以被機器解析。
舊 URL 可以被追溯。
理論 corpus 可以長期保存。
```

因此，最終路線是：

```text
Python Corpus Engine first.
AICL static layer second.
AIRS / AILP rights layer third.
Astro human shell later.
```

不要反過來。

***

# 24. 一句話總結

```text
本次重構的目標不是把網站變漂亮，而是把 Logic Matrix 從單一 build.py 的靜態備份站，升級成具備 stable ID、machine-readable corpus、AICL、AIRS / AILP、redirects、link validation 與未來 Agent 擴展能力的 AI-native Corpus Engine。
```

# 25. 三段式 Agent Ingestion Workflow：輸入前、Agent 判斷暫存區、輸入後

## 25.1 設計目的

未來新增論文時，不應直接把新文件丟進正式 `content/papers/`。

原因是 Logic Matrix 的 corpus 已經具有：

```text
stable ID
時間分類
metadata
registry
raw output
AI corpus index
llms.txt
sitemap.xml
rights spectrum
broken link validation
```

因此，新文件進入正式 corpus 前，應先經過 Agent 攝取流程。

但這不代表使用者不能快速上傳。相反地，應建立一個更適合長期維護的「三段式輸入區」：

```text
1. 輸入前：使用者丟原始文件
2. Agent 判斷暫存區：Agent 分析、判斷、補 metadata、產生報告
3. 輸入後：Agent 整理完成，等待正式寫入 corpus
```

此流程的核心是：

```text
使用者仍然可以無腦丟檔案。
但正式 corpus 不再被無腦污染。
```

***

## 25.2 建議資料夾結構

新增：

```text
ingest/
  01-before/
  02-agent-staging/
  03-after/
  reports/
```

中文語義：

```text
ingest/01-before/
  輸入前。使用者直接丟新論文、新白皮書、新草稿、新程式碼文件的位置。

ingest/02-agent-staging/
  Agent 判斷暫存區。Agent 在這裡進行分析、日期判定、metadata 推測、衝突檢查、分類預演。

ingest/03-after/
  輸入後。Agent 整理完成後放置的待發布文件。這裡的文件已經具備初步 metadata、建議路徑、stable ID 候選、hash、報告。

ingest/reports/
  每次攝取流程的報告。
```

實際結構：

```text
ingest/
  01-before/
    2026-07-01__new-paper.md
    draft-aicl-extension.md

  02-agent-staging/
    lm-001201/
      source.md
      metadata.json
      proposed-frontmatter.yaml
      link-check.json
      classification.json
      notes.md

  03-after/
    2026/
      2026-07/
        2026-07-01__new-paper.md

  reports/
    ingest-2026-07-01T153000.md
    ingest-2026-07-01T153000.json
```

***

## 25.3 三個資料夾的職責

### 25.3.1 `ingest/01-before/`

這是使用者操作區。

使用者可以直接把新文件丟進來：

```text
.md
.docx
.pdf
.py
.lean
.ts
.jsx
.zip
```

但 Agent 第一階段建議優先處理：

```text
.md
.py
.lean
.ts
.jsx
```

其他格式可以先保留在 before，不強制處理。

此資料夾允許混亂。

允許：

```text
中文檔名
長檔名
無 frontmatter
未分類
未判定日期
草稿
重複檔
```

因為它只是輸入前。

***

### 25.3.2 `ingest/02-agent-staging/`

這是 Agent 判斷暫存區。

Agent 對每個輸入文件建立一個 staging unit：

```text
ingest/02-agent-staging/lm-001201/
  source.md
  metadata.json
  proposed-frontmatter.yaml
  proposed-path.txt
  link-check.json
  duplicate-check.json
  rights-profile.json
  notes.md
```

Agent 在這一層執行：

```text
1. 讀取檔名
2. 解析 frontmatter
3. 偵測語言
4. 判定 created / updated
5. 判定 date_confidence
6. 分配 stable ID 候選
7. 產生 hash
8. 檢查是否重複
9. 檢查內部連結
10. 推測 tags / series / domains
11. 推測輸出路徑
12. 建立攝取報告
```

Agent 不應在 staging 階段直接改正式 corpus。

***

### 25.3.3 `ingest/03-after/`

這是 Agent 整理後的待發布區。

進入此資料夾的文件代表：

```text
1. 已經判定日期或標記 date_confidence
2. 已經分配 stable ID 候選
3. 已經建立 metadata
4. 已經決定建議放入的年份 / 月份
5. 已經通過基本格式檢查
6. 已經產生 ingest report
```

但注意：

```text
03-after/ 仍然不是正式 corpus。
```

它是「整理完成、等待寫入正式 corpus」的區域。

正式寫入後，文件才會進入：

```text
content/papers/YYYY/YYYY-MM/
```

***

## 25.4 完整流程

新增論文流程：

```text
User drops files
→ ingest/01-before/

Agent runs ingest
→ ingest/02-agent-staging/

Agent produces proposed output
→ ingest/03-after/

Agent or user confirms publish
→ content/papers/YYYY/YYYY-MM/

Build updates
→ registry/papers.json
→ /p/{id}/
→ /raw/{id}.md
→ /api/papers/{id}.json
→ /ai/corpus.jsonl
→ /llms.txt
→ /sitemap.xml
```

簡化流程：

```text
before → staging → after → corpus
```

***

## 25.5 指令設計

建議新增兩個指令：

```bash
python scripts/ingest.py
python scripts/publish_ingested.py
```

### `scripts/ingest.py`

負責：

```text
讀取 ingest/01-before/
建立 ingest/02-agent-staging/
產生 metadata
產生 proposed path
產生 reports
輸出到 ingest/03-after/
```

但不改正式 corpus。

### `scripts/publish_ingested.py`

負責：

```text
讀取 ingest/03-after/
寫入 content/papers/YYYY/YYYY-MM/
更新 registry/papers.json
更新 redirects.json
執行 build
執行 link validator
產生 publish report
```

***

## 25.6 Agent 不確定時的處理

若 Agent 無法判斷日期：

```text
放入 ingest/03-after/undated/
metadata 加 date_confidence: unknown
```

若 Agent 懷疑重複：

```text
不要發布。
保留在 ingest/02-agent-staging/
報告 duplicate candidates。
```

若 Agent 發現 broken links：

```text
第一階段只警告。
不要自動刪除連結。
不要自動重寫正文。
```

若 Agent 無法判斷是否該發布：

```text
保留在 staging。
產生 needs_review: true。
```

***

## 25.7 攝取報告格式

每次執行 `scripts/ingest.py`，產生：

```text
ingest/reports/ingest-YYYY-MM-DDTHHMMSS.md
ingest/reports/ingest-YYYY-MM-DDTHHMMSS.json
```

Markdown 報告範例：

```md
# Ingest Report

Generated at: 2026-07-01T15:30:00+08:00

## Summary

- Input files: 3
- Ready files: 2
- Needs review: 1
- Duplicate candidates: 0
- Broken links: 4 warnings

## Ready

### lm-001201

Title: AICL Extension
Proposed path: content/papers/2026/2026-07/2026-07-01__AICL Extension.md
Date confidence: explicit
Status: ready

## Needs Review

### staging-temp-0003

Reason:
Date unknown and possible duplicate title.

Suggested action:
Review manually before publish.
```

***

## 25.8 `ingest/` 是否進 Git

建議：

```text
ingest/01-before/ 可以不進 Git，或只保留 .gitkeep。
ingest/02-agent-staging/ 不進 Git。
ingest/03-after/ 可選擇不進 Git。
ingest/reports/ 可選擇保留最新報告或不進 Git。
```

建議 `.gitignore`：

```gitignore
ingest/01-before/*
!ingest/01-before/.gitkeep

ingest/02-agent-staging/*
!ingest/02-agent-staging/.gitkeep

ingest/03-after/*
!ingest/03-after/.gitkeep

ingest/reports/*
!ingest/reports/.gitkeep
```

正式進 Git 的應該是：

```text
content/papers/
registry/
scripts/
site/
```

也就是：

```text
ingest 是工作區。
content 是正式區。
```

***

## 25.9 Agent 實作指令補充

```text
Add a three-stage ingestion workflow.

Create:

ingest/01-before/
ingest/02-agent-staging/
ingest/03-after/
ingest/reports/

Meaning:

01-before:
User input area. New raw papers are dropped here.

02-agent-staging:
Agent decision workspace. Analyze files, infer dates, assign stable ID candidates, detect duplicates, generate proposed metadata, validate links, and write reports.

03-after:
Agent-organized output area. Files are ready for final publishing but are not yet part of the canonical corpus.

Do not write directly from 01-before to content/papers.
Do not modify canonical corpus during ingest.py.
Only publish_ingested.py may move files into content/papers/YYYY/YYYY-MM/.

Add scripts:

scripts/ingest.py
scripts/publish_ingested.py

ingest.py should:
- scan ingest/01-before/
- create staging units under ingest/02-agent-staging/
- infer metadata
- assign stable ID candidates
- generate proposed frontmatter
- detect duplicates
- validate links
- output ready files to ingest/03-after/
- write ingest report

publish_ingested.py should:
- read ingest/03-after/
- move accepted files to content/papers/YYYY/YYYY-MM/
- update registry/papers.json
- update redirects.json if needed
- rebuild the site
- write publish report

Do not rewrite paper body content unless explicitly requested.
Do not guess dates aggressively.
If uncertain, mark needs_review: true.
```

***

## 25.10 一句話總結

```text
未來新增論文不再直接進入正式 corpus，而是先進入 before，經過 Agent staging 判斷，再輸出到 after，最後才發布到 content/papers；這讓使用者仍能快速丟檔案，同時讓 Logic Matrix 的 AI corpus 保持穩定、可追溯、可驗證、可長期維護。
```
# 26. 舊版 AI Crawler 抽獎式攝取問題

## 26.1 問題描述

舊版網站在 AI crawler 眼中不是穩定 corpus，而更接近「抽獎式攝取空間」。

也就是說，AI crawler 每次訪問網站時，可能得到不同的結構感知：

```text
今天 crawler 以為某篇文章存在。
明天 crawler 訪問同一路徑時得到 404。

今天 crawler 沒有發現某篇文章。
但實際上該文章存在，只是沒有被 sitemap、llms 或 canonical route 正確暴露。

今天 crawler 抓到 raw markdown。
但沒有抓到對應的 canonical HTML page。

今天 crawler 抓到 paper-173。
但之後新增檔案後，paper-173 可能漂移成另一篇。

今天 crawler 沿著 Markdown 中的短相對連結進入 /papers/t。
但該路徑本來不是文章，只是公式或符號被誤解析成連結。
```

這導致 AI 對網站的 ingestion 行為變成非決定性：

```text
同一批內容，不同時間抓，結果不同。
同一個 crawler，不同入口抓，結果不同。
不同 AI crawler，看到的 corpus 邊界不同。
```

因此，舊版問題不是單純「檔案很多」，而是：

```text
網站沒有提供穩定、可追溯、可驗證、canonical 的 AI 攝取路徑。
```

***

## 26.2 抽獎式攝取的原因

造成抽獎式攝取的主要原因包括：

```text
1. slug 不穩定
2. 單層 papers/ 過大
3. raw 與 HTML 混放
4. 缺少 stable ID
5. 缺少 redirects
6. 缺少 broken link validation
7. 缺少 canonical URL policy
8. sitemap / llms / raw / html 之間缺少一致索引
9. Markdown 相對連結可能被誤解析為真實頁面
10. AI crawler 沒有明確 machine-readable corpus manifest 可依循
```

其中最嚴重的是：

```text
unstable slug + missing redirects + broken relative links
```

這會讓 crawler 誤以為網站中存在大量不存在頁面，也會讓真正存在的頁面因入口不穩而被漏吃。

***

## 26.3 對 AI 攝取品質的影響

抽獎式攝取會造成以下後果：

```text
1. AI 對 corpus 的覆蓋不完整。
2. AI 可能反覆抓取不存在頁面。
3. AI 可能將 404、錯誤頁、空頁或舊頁當成網站結構的一部分。
4. AI 可能漏掉真正重要的理論文件。
5. AI 對同一篇文章的 canonical source 判斷不穩。
6. AI 難以建立可靠引用鏈。
7. AI 訓練或 RAG 系統可能形成錯誤索引。
8. 搜尋引擎與 LLM crawler 可能浪費 crawl budget。
9. 未來 Agent 可能根據錯誤 route 執行錯誤操作。
```

對一般網站而言，這只是 SEO 或 404 問題。

但對 Logic Matrix 這類 AI-readable theoretical corpus 而言，這是更嚴重的問題：

```text
它會讓 AI 對理論體系的攝取變成不穩定、斷裂、重複、錯位與部分幻覺化。
```

***

## 26.4 修正原則

本次重構必須讓 AI crawler 從抽獎式攝取，轉為 deterministic ingestion。

也就是：

```text
同一篇文章永遠有同一 stable ID。
同一 stable ID 永遠指向同一 canonical URL。
舊 URL 永遠 redirect 到新 canonical URL。
sitemap、llms、manifest、corpus.jsonl、raw、HTML、API metadata 必須一致。
不存在的相對連結不得被當成真實入口。
AI crawler 必須能從 /ai/manifest.json 找到完整 corpus 路徑。
```

核心轉換：

```text
Before:
Crawler guesses the site.

After:
Crawler follows the manifest.
```

***

## 26.5 必須新增的修正機制

### 26.5.1 Stable ID

每篇文章必須有永久 ID：

```text
lm-000001
lm-000002
lm-000003
```

ID 不因檔名、分類、日期、標題改變而改變。

***

### 26.5.2 Canonical URL

每篇文章的 canonical URL：

```text
/p/lm-000001/
```

不要依賴中文檔名，不要依賴排序序號，不要依賴舊 `paper-###`。

***

### 26.5.3 Raw URL

每篇文章的 raw source：

```text
/raw/lm-000001.md
```

***

### 26.5.4 Metadata URL

每篇文章的 metadata：

```text
/api/papers/lm-000001.json
```

***

### 26.5.5 Manifest Index

AI crawler 應優先讀：

```text
/ai/manifest.json
/ai/corpus.jsonl
/llms.txt
/llms-full.txt
/sitemap.xml
```

而不是自行猜測 `/papers/` 下面有哪些東西。

***

### 26.5.6 Redirects

所有舊路徑都應盡量 redirect：

```text
/papers/old-name.md.html → /p/lm-000001/
/papers/paper-173.md.html → /p/lm-000173/
```

***

### 26.5.7 Broken Link Validator

Build 時必須檢查：

```text
所有 internal href 是否存在。
所有 unknown relative links 是否被警告。
所有疑似公式短連結是否被忽略或降級。
```

輸出：

```text
registry/generated/broken-links.json
```

***

## 26.6 Agent 實作補充指令

```text
Add crawler ingestion consistency as a first-class requirement.

The old site allowed AI crawlers to ingest the corpus probabilistically because URLs, raw files, HTML pages, relative links, sitemap entries, and generated slugs were not fully canonicalized.

Fix this by ensuring:

1. Every paper has a stable ID.
2. Every stable ID has one canonical HTML route.
3. Every paper has one raw route.
4. Every paper has one metadata JSON route.
5. All old paper routes redirect to canonical routes where possible.
6. sitemap.xml only includes canonical routes.
7. llms.txt and llms-full.txt only point to canonical and machine-readable routes.
8. /ai/manifest.json is the preferred crawler entry point.
9. /ai/corpus.jsonl is the preferred bulk ingestion file.
10. Markdown relative links that do not resolve must not create fake crawler paths.
11. Build must generate a broken link report.
12. Build must generate a route consistency report.

Goal:
Turn AI crawler ingestion from lottery-like discovery into deterministic ingestion.
```

***

## 26.7 新增驗收標準

新增以下驗收：

```text
1. Every registry item has:
   - id
   - canonical_url
   - raw_url
   - api_url
   - source_path

2. Every canonical_url exists in dist.

3. Every raw_url exists in dist.

4. Every api_url exists in dist.

5. Every sitemap paper URL matches canonical_url.

6. Every llms-full paper URL matches canonical_url.

7. Every corpus.jsonl item matches registry/papers.json.

8. No generated paper depends on unstable paper-### slug.

9. Unknown relative links are reported.

10. Legacy URLs are redirected when known.
```

***

## 26.8 一句話總結

```text
舊版網站讓 AI crawler 用猜的方式吃 corpus；新版 Corpus Engine 必須讓 AI crawler 依照 stable ID、canonical URL、manifest、corpus.jsonl、redirects 與 link validation 進行可重複、可追溯、可驗證的 deterministic ingestion。
```
# 27. 從 Human-Centric Web 到 AI-Readable Web

## 27.1 舊網站時代的預設

過去網站主要以人類為中心設計。

網站設計者通常優先考慮：

```text
人類能不能看懂。
首頁好不好看。
搜尋引擎能不能收錄。
SEO metadata 是否完整。
社群分享卡片是否正常。
頁面載入速度是否足夠。
```

在這個時代，crawler 主要被理解為搜尋引擎 crawler。\
網站對 crawler 的態度通常是：

```text
讓搜尋引擎收錄公開頁面。
阻止惡意爬蟲。
避免資料被大量抓取。
控制 crawl budget。
```

因此，`robots.txt` 的核心語境是「允許或拒絕 crawler 進入」，而不是「協助 AI 正確理解與攝取」。

在舊時代，很少網站會主動思考：

```text
AI 應該如何讀取這個網站？
哪份文件是 canonical？
哪份文件是歷史版本？
哪些內容是 raw source？
哪些內容是渲染後頁面？
哪些內容允許摘要？
哪些內容允許訓練？
哪些內容需要引用？
哪些內容需要授權？
```

因為當時 AI 並不是網站的正式讀者。

***

## 27.2 AI 時代的讀者變化

AI 時代開始後，網站讀者不再只有人類與搜尋引擎。

新讀者包括：

```text
AI crawler
LLM crawler
RAG system
autonomous agent
model training pipeline
embedding indexer
semantic search system
future AI assistant
knowledge ingestion pipeline
```

這些讀者不是單純「看頁面」，而是會：

```text
抓取
解析
切分
向量化
摘要
引用
索引
重組
訓練
微調
作為回答依據
作為 Agent 行動依據
```

因此，網站不再只是展示介面，而逐漸變成：

```text
人類閱讀層
搜尋引擎索引層
AI 攝取層
Agent 能力層
權利與治理層
```

這就是 AI-readable web 與 AI-native publication architecture 出現的原因。

***

## 27.3 為什麼過去很少人會設計 AI 攝取層

過去網站不優先考慮 AI crawler，是合理的。

原因包括：

```text
1. AI crawler 還不是主流讀者。
2. 網站主要服務人類 UI。
3. SEO 已經是額外負擔，AI ingestion 更不是必要項。
4. 創作者更擔心資料被偷抓，而不是資料被正確攝取。
5. AI 訓練與版權爭議尚未成為日常問題。
6. 大多數網站沒有 corpus、registry、manifest、rights layer 的概念。
```

因此，舊網站邏輯通常是：

```text
防爬比餵爬更重要。
```

但 AI 時代正在改變這個前提。

***

## 27.4 新時代不是單純開放，而是可治理開放

AI-readable web 不等於完全開放所有資料。

它真正要解決的是：

```text
讓 AI 知道可以讀什麼。
讓 AI 知道應該怎麼讀。
讓 AI 知道哪些是 canonical。
讓 AI 知道哪些是舊版。
讓 AI 知道哪些可以引用。
讓 AI 知道哪些不能訓練。
讓 AI 知道哪些需要授權。
讓 AI 知道哪些內容是 raw source。
讓 AI 知道哪些內容是 human UI。
```

因此，新的問題不是：

```text
要不要讓 AI 爬？
```

而是：

```text
如何讓 AI 在清楚邊界中正確攝取？
```

這也是 AICL 與 AIRS / AILP 的意義。

AICL 解決：

```text
AI 應該去哪裡讀、如何讀、如何引用、如何調用。
```

AIRS / AILP 解決：

```text
AI 可以怎麼學、學多深、能否保留、能否訓練、能否商業化、是否需要授權與補償。
```

***

## 27.5 Logic Matrix 的特殊性

Logic Matrix 不是普通網站。

它更接近：

```text
公開理論 corpus
AI-readable archive
future model-facing knowledge layer
GitHub-backed theoretical repository
machine-ingestible research memory
```

因此，它不能只用傳統人類中心網站的方式維護。

對一般網站而言，AI crawler 吃錯可能只是 SEO 或流量問題。\
但對 Logic Matrix 而言，AI crawler 吃錯會造成：

```text
理論譜系斷裂。
canonical source 錯位。
舊版與新版混淆。
不存在頁面被誤認為語料邊界。
真正文章被漏掉。
AI 對理論系統形成不穩定理解。
```

所以 Logic Matrix 需要比一般網站更早進入 AI-readable / AI-native 架構。

***

## 27.6 從防爬到餵爬的時代轉換

舊時代的基本姿態是：

```text
不要亂爬我的網站。
```

新時代會分化成兩種網站：

```text
不希望 AI 學習的網站：
加強限制、權利聲明、robots policy、anti-scraping。

希望 AI 正確學習的網站：
提供 manifest、corpus、llms.txt、rights-spectrum、canonical routes、citation policy。
```

Logic Matrix 屬於後者。

它不是無條件讓 AI 亂吃，而是要讓 AI：

```text
吃對。
吃穩。
吃完整。
吃 canonical。
知道權利邊界。
知道引用方式。
知道版本關係。
知道理論生成時間線。
```

***

## 27.7 一句話總結

```text
過去網站是人類中心，crawler 只是被允許或被阻擋的外部訪客；AI 時代的網站開始需要把 AI、Agent 與模型攝取流程視為正式讀者，並為它們提供可讀、可追溯、可治理、可授權的機器入口層。
```

