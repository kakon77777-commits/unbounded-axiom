# RH-W-20：Batch 02 交棒與平台匯入規格

## 1. 交棒物件

Batch 02 不應只讀最後一篇摘要，而應載入：

1. `research_nodes.json`：二十輪 typed nodes。
2. `dependency_graph.json`：研究接力與 recertification edges。
3. `claim_ledger.json`：有限主張與 scope。
4. `failure_and_revision_log.json`：失敗、修正與 disposition。
5. `certificate_index.json`：可執行性與信任狀態。
6. `trust_boundary.json`：後端不能保證的事項。
7. `handoff_batch_02.json`：下一批候選軌道。

## 2. 建議的 Batch 02 主軸

優先順序不必等於輪次順序，但建議至少保留兩條並行主線：

- **可信度線：** 簽章、第二 verifier、可重現建置、形式化 kernel。
- **數學線：** 多事件腔室圖、prime-power entry surfaces、各向異性低譜流形、字典擴張與完備性壓力測試。

## 3. 平台匯入最低契約

前端或資料庫必須：

- 不改寫 `node_id`、`claim_id`、`event_id`；
- 保留 typed status，不把所有成功執行顯示成同一個「已證明」；
- 顯示 `rh_claim=false`；
- 允許一個節點同時擁有有限成果與未完成事項；
- 將 `RECERTIFIES` 與普通 dependency 分開渲染；
- 不因後續節點成功而隱藏歷史缺口。

## 4. Case 0001 的平台意義

這個案例不是為了證明 AI 已經解決 RH，而是展示：

> 一個 AI 研究程序如何在長期開放問題上形成可接力的節點、可重放的有限證書、可見的失敗與修正，以及不會被成功敘事抹除的信任邊界。
