# EML Base Space Evolution — From Simulated Toy to Living Causal Graph

## Agent handoff specification (for Fable 5 / Mythos)

**作者**：Neo.K / EVEMISSLAB（願景）· Claude Opus 4.8（規格草擬）
**日期**：2026-07-02
**類型**：技術敘述 / Agent 執行規格 / 交接文件
**適用專案**：Logic Matrix / Unbounded Axiom（`logic.evemisslab.com`）
**目標讀者**：接手實作的 AI agent（Fable 5）——你會在乾淨 context 下讀到這份，本文件提供完整背景與可執行路線。

---

# 0. 這份文件是什麼

Neo 的原始概念裡，`base-space.html`（「EML Base Space · 拓撲耦合矩陣底空間」）不該只是裝飾，而是一張**活的理論因果圖**：AI agent 造訪這個 corpus 後，能**自動更新、修正、補充、改良**理論之間的因果邏輯，並讓那張圖反映理論的真實狀態（已驗證 / 修訂中 / 被反駁）。

**現況是一個誠實的示範/玩具**。本文件的任務是把它從玩具推向真實，並定義一條**分階段、可信、有治理**的路徑。這不是要一次做完，而是給你一個成熟度階梯 + 每一階的具體工程 + 驗收標準。

核心原則：

```text
Read first. Extract truth second. Propose third. Verify adversarially fourth. Publish gated fifth.
Never let an arbitrary crawling agent write directly into the canonical corpus.
Formal (Lean-checkable) claims may auto-advance; prose theory stays human-gated.
Do not break canonical /p/{id}/ URLs, the AI layer, or anti-cloaking.
```

---

# 1. 現況：為什麼它是玩具

`base-space` 目前的資料是**假造的**：

- **邊（weights）**：由論文標題的字元 hash 決定性生成（`base-space.js` / `src/worker.js` 的 `baseSpace()` seed 邏輯：同語言 0.2、跨語言 0.02，過門檻 0.15 稀疏化）。**與論文的真實內容/依賴無關。**
- **節點狀態（states：`true`/`omega`/`false`，即三態邏輯 ⊤/Ω/⊥）**：由爬蟲命中數決定（`hits_<id>` > 20 → true、> 1 → omega）。**是流量計數，不是理論真偽。**
- 它**視覺化了一個隱喻**（「AI 爬蟲注意力驅動理論狀態」），但沒有計算任何真實因果或真偽。

相關檔案：

```text
scripts/generators.py :: write_base_space()   → dist/base-space.html（canvas 前端 + client fallback generateSimulatedData）
src/worker.js         :: baseSpace()           → GET /api/base-space（KV weights2/states2 seed/讀）
src/worker.js         :: logCrawler()          → GET /api/log-crawler?id=（命中驅動狀態）
dist/papers-metadata.json                       → [{id,title,ext,lang,canonical,raw}]（前端 + seed 的資料源）
scripts/agi_eigen_synthesis.py                  → 三態邏輯 + SVD/特徵值合成模擬器（MVP，目前獨立）
```

KV 鍵（Cloudflare `BASE_SPACE_KV`，已綁定）：`hits`、`hits_<id>`、`weights2`（`{id:{id:number}}`）、`states2`（`{id:"true"|"omega"|"false"}`）。全部以 **stable id（`lm-NNNNNN`）** 為鍵。

---

# 2. 願景（Neo 的原始概念）

```text
Agents come to the site → they autonomously keep the theory causal logic correct:
  - update    (新資料/新論文改變依賴時，更新邊)
  - correct   (發現錯誤推論/斷裂時，修正)
  - supplement(發現缺口時，補充)
  - improve   (發現更強的表述/證明時，改良)
And the base-space graph reflects the *real* state of each claim, not crawler traffic.
```

---

# 3. 成熟度階梯（L0–L5）

| 階 | 能力 | 可行度（2026-07） | 已有的零件 |
|---|---|---|---|
| L0 | agent 能**讀** corpus | 完成 | AICL `/ai/` 層、`/ai/corpus.jsonl`、`/raw/{id}` |
| L1 | 抽出**真實因果/依賴圖** | 現在可做 | `tcf_schema.py`（TCF §2 DAG） |
| L2 | agent **批判/提案** | 現在可做 | §25 三段式 ingest（`ingest/01-before → 02-staging → 03-after`） |
| L3 | 提案**對抗式驗證**才接受 | 現在可做（多 agent） | AICL Capability Layer（ACL，現 `runtime_enabled:false`） |
| L4 | **人閘門**發布 | 現在可做 | `scripts/publish_ingested.py`（唯一寫入 corpus 者） |
| L5 | 高信心變更**全自動**發布 | 只對可形式化核心開放 | `.lean` 檔 + FDRS 證明（機器可檢核） |

---

# 4. 轉換 A — 真實拓撲（L1，最高槓桿的第一步）

**把假 weights 換成真依賴邊。** 你已經有 `tcf_schema.py`：它把任意理論規範化成九節結構，其中 **§2 DAG = 概念依賴圖**。

實作路線：

```text
1. 對 content/papers/ 的每篇（先挑核心 30–50 篇原型，再全量 1177）跑一個 TCF 抽取 pass：
   - 用 LLM 從論文抽出 §0 原語、§1 公理、§2 概念依賴 DAG、§4 定理、§5 推導鏈。
   - 產出 registry/tcf/<id>.json（符合 tcf_schema.py 的 dataclass；可直接用該模組序列化/驗證/算 CR 壓縮度量）。
2. 把跨論文的依賴/引用/概念共享聚合成一張全域邊集：
   - 邊 = 「論文 A 的某定理依賴論文 B 的某公理/原語」或「概念 X 在 A 定義、被 B 使用」。
   - 產出 dist/ai/graph.json（{nodes:[id...], edges:[{from,to,type,weight,evidence}]}）。
3. base-space 改讀這張真圖：
   - write_base_space + src/worker.js baseSpace() 的 seed 改成「若 /ai/graph.json 存在，用真邊；否則 fallback 舊模擬」。
   - 前端 canvas 不需大改（它已按 id 畫鄰接矩陣）；只是 weights 從假變真。
```

驗收：`dist/ai/graph.json` 存在且每條邊帶 `evidence`（可回溯到來源論文的段落/公理）；base-space 的矩陣反映真實依賴（抽查幾篇，人工確認邊合理）。

**這一步做完，base-space 立刻從玩具變成「理論依賴地形圖」。** 且 `/ai/graph.json` 本身就是給 AI 的高價值機器資產（AICL 的自然延伸）。

---

# 5. 轉換 B — 有意義的三態（L3/L5）

現在的 `true/omega/false` 是爬蟲命中數。真實版本 = **驗證狀態**：

```text
true (⊤)   = 已被機器證明（Lean 通過）或多 agent 對抗驗證達共識
omega (Ω)  = 修訂中 / 有未決張力 / 有相衝的提案
false (⊥)  = 被反駁（找到反例或矛盾）
```

實作路線：

```text
1. 可形式化核心：對能寫成 Lean 的命題，建立「提案 → 形式化 → machine-check → 通過才轉 true」的迴路。
   - 你已有 .lean 檔（FDRS_en.lean / FDRS_zn.lean）與 FDRS 證明作為範例。
   - 這是唯一可以往 L5 全自動、且可信的部分（機器證明不會騙人）。
2. 不可形式化的散文理論：用多 agent 對抗驗證（correctness / consistency-with-corpus / refutation 三種 lens）
   產生一個信心分數與狀態；但狀態變更只寫進「提案層」，不直接改 canonical，等 L4 人閘門。
3. state 的來源改成上述驗證信號，不再是 hits。hits 可保留為「注意力」的另一個維度（次要）。
```

驗收：至少一條可形式化命題走完 Lean 迴路自動轉 `true`；至少一條散文命題被多 agent 標為 `omega`（有張力）並產出可讀的驗證報告。

---

# 6. 已經蓋好的骨架（把它們接起來）

| 願景零件 | 現有實作 |
|---|---|
| agent 讀取入口 | `/ai/manifest.json`、`/ai/corpus.jsonl`、`/ai/index.md`、`/raw/{id}` |
| 真拓撲來源 | `tcf_schema.py`（TCF 九節 + §2 DAG + CR 壓縮度量） |
| 真驗證來源 | `.lean` 檔 + FDRS 證明（可機器檢核） |
| 提案入口 + 暫存 | §25：`ingest/01-before → 02-agent-staging → 03-after`，`scripts/ingest.py` |
| 唯一寫入 corpus | `scripts/publish_ingested.py`（人閘門發布） |
| agent 工具層 | AICL Capability Layer（`/ai/tools/catalog.json`，現宣告式、`runtime_enabled:false`） |
| 治理/權利 | AIRS `/ai/rights-spectrum.json`（AILP）——可加一條「agent 可提案、不可直接寫入」 |
| 三態邏輯數學 | `agi_eigen_synthesis.py`（三態 + SVD/特徵值；可作為狀態動力學的計算核） |

**缺的不是零件，是接線 + 把 base-space 的假信號換成真信號。**

---

# 7. 信任與治理邊界（不可跳過）

```text
可形式化（Lean-checkable）  → 可往 L5 全自動（機器證明背書）
不可形式化的理論散文        → 最多 L4 人閘門（agent 提案 + 對抗驗證，Neo 核准才進庫）
任意爬蟲 agent              → 只能讀 + 提案到 ingest/ 或 proposals/；永遠不能直接寫 content/papers/
```

- 投毒 / 漂移 / 幻覺式「修正」是真實風險——驗證層與人閘門是防線。
- 把這條寫進 AIRS：新增 permission 如 `autonomous_proposal: 0.8`、`autonomous_canonical_write: 0.0 (human_gate_required)`，讓治理機器可讀。
- `publish_ingested.py` 維持「唯一寫入 canonical」的地位；agent 的產物一律先落 `ingest/01-before/` 或新的 `proposals/`，走同一條驗證+閘門。

---

# 8. 分階段實作計畫（可執行）

```text
Phase A (L1 原型)：挑 30–50 篇核心論文跑 TCF 抽取 → registry/tcf/<id>.json → 聚合 dist/ai/graph.json
                   → base-space 改讀真圖。驗收：真邊帶 evidence，人工抽查合理。
Phase B (L1 全量)：擴到全 1177 篇；graph.json 進 AICL 層（manifest 加指標）。
Phase C (L3 驗證層)：多 agent 對抗驗證器（correctness/consistency/refutation lens）→ 提案信心分數 + 狀態。
Phase D (L2 提案迴路)：agent 讀 corpus → 找缺口/錯誤/延伸 → 草擬提案落 proposals/ → 走驗證 → 人閘門。
Phase E (L5 形式化核心)：Lean 迴路——可形式化命題自動 machine-check → 通過轉 true。
Phase F (三態接真信號)：base-space state 改由驗證結果驅動，非 hits。
```

每階都要：不破壞既有 canonical 路由 / AI 層 / anti-cloaking；產物先進 staging，人核准才進 canonical；build 用 `bash build-site.sh` 驗證後才 push。

---

# 9. Repo 背景（給乾淨 context 的你）

```text
Repo        : D:\Ai\work together\unbounded-axiom（public github kakon77777-commits/unbounded-axiom）
Live        : https://logic.evemisslab.com（Cloudflare Workers Static Assets — 不是 Pages）
Build       : bash build-site.sh   （python3 build.py → shell/ astro build → cp -r shell/dist/. dist/）
Deploy      : CF 執行 build-site.sh，再 npx wrangler deploy
Dynamic routes: 在 src/worker.js（單一 Worker，main 入口）——不是 functions/（Workers-Assets 不吃 Pages functions 慣例）
              /api/base-space、/api/log-crawler、/papers/* 301（catch-all，用 dist/papers-legacy-map.json）
Engine      : scripts/{config,helpers,render,generators,registry,idroutes,validate,ai_layer,build}.py + 根 build.py
Human shell : shell/（Astro 5，讀引擎 JSON；產 /、/p/{id}/、/timeline/，overlay 到 dist/）
Corpus      : content/papers/YYYY/YYYY-MM/*.md（1177 篇）；registry/papers.json（stable ids lm-NNNNNN）
Canonical   : /p/{id}/（人漂亮 + 機器可解析：JSON-LD/canonical/robots/ai-content-policy/rel=alternate/?id prefetch）
Machine     : /raw/{id}.ext、/api/papers/{id}.json、/ai/*（manifest/corpus.jsonl/timeline/specs/governance/rights-spectrum）
Ingest §25  : ingest/01-before → scripts/ingest.py → 02-agent-staging + 03-after → scripts/publish_ingested.py → content/papers
KV          : BASE_SPACE_KV（已綁 namespace 834dc040…）；鍵 weights2/states2/hits/hits_<id>，全 id-keyed
Windows 陷阱: 靜態/dev 伺服器會鎖 dist/（WinError 32）；跑 build.py 前先停 preview / kill workerd.exe
鐵律        : 只重構不改論文正文（除 metadata）；不破壞 canonical URL；反 cloaking；§25 治理；AIRS 權利
```

TCF 參考實作已在 `tcf_schema.py`（九節 dataclass、fingerprint、CR 度量、attribution/provenance）。三態動力學核在 `agi_eigen_synthesis.py`。

---

# 10. 非目標 / 風險

```text
非目標：一次全自動化；讓任意 agent 直接改理論庫；假裝散文理論可被機器「證明」。
風險  ：LLM 提的「修正」看似合理卻錯（plausible-but-wrong）→ 必須對抗驗證 + 人閘門。
        TCF 抽取品質參差 → 邊要帶 evidence、可回溯、可被否決。
        自動化跑過頭傷害 corpus 可信度 → 寧可慢、可審計、可回溯。
```

---

# 11. 一句話總結

```text
把 base-space 從「爬蟲命中數驅動的假三態圖」升級為「TCF 真實依賴拓撲 + Lean/多-agent 驗證驅動的真三態」，
並用 §25 提案治理 + AICL 能力層 + AIRS 權利，讓 agent 能提案、被驗證、經人閘門地改良理論——
可形式化的核心可全自動，其餘人閘門。零件都在，缺的是接線與換掉假信號。
```
