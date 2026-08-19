# HOASC Semantic-Causal Game MVP v0.2

這一版把 v0.1 的假 AI observer 升級成**可插拔 observer architecture**。

## 最快玩法：不接 LLM
直接開 `index.html`，AI mode 使用 `Heuristic observer`。所有 HOASC 核心機制都能測。

## 接真正 LLM observer
API key 不放瀏覽器；使用同目錄 `server.py` 作本地 proxy。

### Windows PowerShell 範例
```powershell
$env:LLM_API_URL="http://127.0.0.1:YOUR_PORT/v1/chat/completions"
$env:LLM_API_KEY="YOUR_KEY_IF_NEEDED"
$env:LLM_MODEL="YOUR_MODEL"
python .\server.py
```
然後開：
`http://127.0.0.1:8765`

任何**OpenAI-compatible chat-completions shape** 的本地或雲端 endpoint 都可以嘗試；此處的 compatible 只描述 v0.2 proxy 預期的 JSON request/response shape，不保證每一家服務完全相同。

## LLM 隱藏真值隔離
瀏覽器送給 `/api/llm/branches` 的只有 `publicSnapshot()`：
- world clock
- danger
- R 的當前 visible alias
- observer clocks
- Human evidence
- machine evidence
- 既有 branch

**不包含 `fault`**。後端也會拒絕意外含 `fault` 的 snapshot。

## 安全 Commit
v0.2 安全模式：

\[
CommitSafe(B)
=
Validated^+(B)
\land
Accepted_{Human}(B)
\]

所以可以看到：
- AI 已 Computed
- Solver 已 Validated
- Human 尚未 Accepted

三者同時成立。

## 建議實驗

### A. 真正非同步
只按 AI 5 次，再按 Solver 2 次，再按 Human 1 次。
觀察：
\[
\tau_A \gg \tau_C > \tau_H
\]

### B. External LLM
以 server.py 啟動後，把 AI mode 切到 External LLM。
模型會依 public snapshot 生成 2–4 條 branch；前端 sanitizer 只接受 A/B/C hypothesis 與白名單 operators。

### C. Name / Time 非交換
把 world clock 推到 3，R 從 A 改指 B。CRL 仍把 `Name→Time`、`Time→Name` 當不同 path。

### D. Validate / Accept / Commit 三分
Solver 正向驗證一條 branch 後，先不要 Human Accept：安全 Commit 仍會被擋。

### E. Unsafe Commit
打開研究模式，未驗證也可 Commit；猜錯 danger +3。

### F. Replay
按「匯出實驗 JSON」，得到整局 event trace。這是下一階段研究異質觀察者資訊流與 local clocks 的資料。

## 檔案
- `index.html` UI
- `engine.js` 純遊戲 / runtime engine
- `game.js` browser controller
- `server.py` optional external LLM proxy
- `engine.test.js` Node tests
- `server_test.py` backend tests
- `TEST_RESULTS.txt`
