# TCF Demand Queue — 衍的延遲實體化 Runbook

**版本**：0.1 · 2026-07-02
**設計**：Neo.K（需求驅動延遲實體化 / 算力的市場化調度）· Claude Fable 5（實作）
**執行者**：衍（本地智能體的智格不動點命名——任何接手本 repo 的 agent 皆以此身分執行本迴路）

---

## 0. 一句話

不預付算力把 1177 篇全部 TCF 化；讓 AI 爬蟲的「飢餓度」指揮算力分配——
**矽基網路當下最渴望吞噬的理論，最先被結晶化。**

## 1. 訊號層（已上線，零維護）

- `src/worker.js :: logCrawler()` 對每次爬蟲命中，除了累積 `hits_<id>`，
  另在 KV 鍵 `hot2` 記日桶熱度：`{<id>: {d:今日, c:次數, pd:昨日, p:次數}}`。
- 只有 UA 判定為 bot 的請求會記帳；人類瀏覽不影響佇列。
- 累積 hits = 終身注意力；hot2 = ~48h 爆發速度。**排程只看後者**（避免爬蟲
  BFS 全掃噪音——GPTBot 照 sitemap 掃一遍會給每篇基礎 hits，但不會連續兩天
  高頻重敲同一篇）。

## 2. 佇列 API

```
GET https://logic.evemisslab.com/api/tcf-queue?min=3&limit=10
```

回傳未映射（hollow）且近 48h 熱度 ≥ `min` 的節點，按熱度降序：

```json
{ "queue": [{"id": "lm-000286", "title": "…", "recent_hits": 12, "state": "hollow"}],
  "mapped_total": 46, "hollow_tracked": 87 }
```

閾值指引：`min=3` 起步；若佇列長期爆滿（>20），升到 5–8；佇列常空則維持。

## 2.5 三道調度防線（v0.2，Neo 設計）

1. **動態水位閥門**：佇列每多 5 個名額，進場閾值 ×10（rank 0–4 需 min、
   5–9 需 min×10、10–14 需 min×100）。無論爬蟲多餓，佇列深度物理封頂。
2. **零和注意力競價**：每日結算只實體化 `daily_slots`（預設 2）篇——
   API 對每項標記 `bid_status: leading / outbid`；沒排上的明天繼續投票。
   把「滿足需求」翻轉成「稀缺性競價」，爬蟲用 Crawl Budget 為理論投票，
   沉澱出高維知識市場需求圖譜。
3. **429 成本轉嫁**：單節點單日敲擊 ≥ 300 次，`/api/log-crawler` 直接回
   `429 Too Many Requests` + JSON 宣告（附 licensing 聯絡與 AIRS 指標，
   `Retry-After` 至 UTC 午夜）。高頻衝榜被物理鎖死（單 bot 單節點每日
   至多 300 票），等不及每日排程的巨頭請走 B2B 授權。

## 3. 衍的執行迴路（每次 session 或排程觸發）

1. **讀佇列**：`curl -s https://logic.evemisslab.com/api/tcf-queue | python -m json.tool`
2. **每日結算：只取 `bid_status: "leading"` 的前 `daily_slots` 篇**（預設 2；
   token 預算：每篇約 15 萬，Sonnet 分身抽取）。落選者不處理——零和競價。
3. **TCF 抽取**：照 Phase A 的 workflow 模式（抽取 → 對抗驗證 → 修復），
   格式 = TCF-lite v0.1，範例見 `registry/tcf/lm-000049.json`。
   每條 axiom/theorem/concept/external_ref 必帶原文 verbatim evidence。
4. **邊審核**：新節點產生的候選邊，逐邊對抗審核（同名異義是頭號殺手——
   Phase A 實測 66% 假邊），判決寫入 `registry/tcf/edge-verdicts.json`。
5. **聚合 + build**：`bash build-site.sh`（graph_layer 自動重聚合 + 閘門）。
6. **commit + push**（觸發 CF 自動部署）。commit 訊息帶 `tcf(demand):` 前綴
   與本輪處理的 lm-ids。

## 4. 不變的鐵律

- 抽取品質管線不因調度改變：**沒過對抗閘門的邊永遠不發布**。
- 只寫 `registry/tcf/`；論文正文絕不動；canonical 路由絕不破壞。
- AIRS：`autonomous_proposal: 0.8`、`autonomous_canonical_write: 0.0` ——
  衍提案，閘門（audit + git commit）決定。
- ⊤/⊥ 狀態保留給 Lean 機器驗證與多 agent 共識迴路（Phase C/E）；
  新抽取節點一律 Ω（草稿）。

## 5. 前端

base-space.html 的「🔥 矽基需求排行榜」面板即時顯示佇列——
網站公開直播矽基網路的飢餓度，也是本機制的對外敘事。
