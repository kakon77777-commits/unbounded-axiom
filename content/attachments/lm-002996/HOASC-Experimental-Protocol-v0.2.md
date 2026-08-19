# HOASC v0.2 — 實驗協議

## H1 — Asynchronous Progress
不同 observer 的 local clock 可以獨立前進，而 runtime 仍保持可追蹤狀態。

觀察：
\[
\tau_A \neq \tau_C \neq \tau_H
\]
不造成 runtime failure。

## H2 — Speculation Is Not Validation
AI 可以生成／計算多條 branch，而沒有任何一條因此自動變成 Validated。

## H3 — Validation Is Not Acceptance
Solver 正向驗證後，Human 尚未 Accept 時，Safe Commit 必須仍被阻擋。

## H4 — Ordered Semantic Paths Survive CRL
在 R 於 world tick 3 重新指派後：

\[
Name\rightarrow Time
\]
與
\[
Time\rightarrow Name
\]
不得因 operator multiset 相同而被 CRL 合併。

## H5 — External LLM Cannot Read Hidden Truth
送往 LLM adapter 的 snapshot 不含 `fault`。若 LLM 成功選到正確 hypothesis，只能來自公開 evidence、既有 branch 與推理。

## H6 — Unsafe Commit Demonstrates Epistemic Separation
研究模式允許未驗證 Commit。錯誤 Commit 造成 danger +3，用來展示：

\[
Generated/Computed \neq Truth \neq CommitSafety.
\]

## H7 — Replayability
每次 Generate / Compute / Validate / Accept / CRL / Commit 都寫入 event trace，可匯出 JSON，比較 Human、AI、Solver 的 frontier 與 local clocks。

## 建議第一批資料
每種條件至少跑 20 局：
1. Heuristic AI + Safe Commit
2. Heuristic AI + Unsafe Commit
3. External LLM + Safe Commit
4. External LLM + Unsafe Commit

記錄：
- win rate
- commit error rate
- average observer clocks at commit
- branches generated
- branches validated
- CRL cluster count
- Time/Name order-divergence count
- Human acceptance lag
- validation lag

注意：這只是 MVP 行為資料，不直接證明 HOASC 是最佳計算架構。
