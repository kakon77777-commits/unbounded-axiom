# HOASC Semantic-Causal Game MVP v0.1

一個不用伺服器、直接打開 `index.html` 就能玩的瀏覽器測試遊戲。

## 目的

測試「異質觀察者非同步語義因果計算」最小機制，而不是測 AI 模型能力。

### 三種 observer
- Human：取得敘事／情境線索。
- AI：快速展開候選 query / causal branches。
- Solver：逐條驗證已 Computed 的 branch。

三者擁有獨立 local clocks：
- `τH`
- `τA`
- `τC`

### 核心機制
1. **非同步**：三個 clock 可獨立前進。
2. **Speculative Expansion**：AI 一次生成多條 candidate。
3. **Non-commutative semantic paths**：
   - `Time → Name`
   - `Name → Time`
   在代號 R 於 world tick 3 重新指派後，不再保證等價。
4. **Validation**：Solver 一次只驗一條 Computed branch。
5. **CRL / 收連**：只把 `hypothesis + ordered operator path` 都一致的 branch 合併。
6. **Commit Guard**：安全模式要求正向 Validated 才能 Commit。
7. **Unsafe Commit**：可開研究模式，直接展示「Computed / Generated ≠ Truth」。

## 建議玩法

### 實驗 A：AI 超前
1. 不動 Human / Solver。
2. 連按 AI +1 三到五次。
3. 觀察 `τA >> τH, τC`，大量 candidate 已產生。
4. 此時仍無法安全 Commit。

### 實驗 B：非交換性
1. 推進世界到 tick 3。
2. R 從 A 改指 B。
3. 觀察 `Name → Time` 與 `Time → Name` branch 不會被 CRL 自動合併。

### 實驗 C：異質驗證
1. AI 先展開。
2. Solver 慢慢 +1。
3. 只有一部分 Computed branch 被 Validation。
4. Human 不必同步到相同 clock。

### 實驗 D：Commit
1. 保持安全模式，只有被 Solver 正向驗證的 branch 能 Commit。
2. 開啟「研究模式」後，可未驗證 Commit。
3. 錯誤 Commit 會令危險度 +3。

## 檔案
- `index.html`
- `style.css`
- `engine.js` — 可重用的純遊戲引擎
- `game.js` — UI
- `engine.test.js` — Node 測試
- `TEST_RESULTS.txt`

## 理論映射

\[
T
\rightarrow
SpecExpand
\rightarrow
AsyncFrontiers
\rightarrow
Compute
\rightarrow
Validate
\rightarrow
CRL
\rightarrow
Commit
\]

本 MVP 故意非常小：如果這個模型已足以呈現非同步、多觀察者、語義路徑、驗證與延後 Commit，之後再把真正 LLM / formal solver 接進 observer adapters 即可。
