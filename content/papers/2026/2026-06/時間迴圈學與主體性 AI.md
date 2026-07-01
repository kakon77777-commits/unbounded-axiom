# 補章：時間迴圈學作為主體性 AI 的自主判斷層

在 Cyc-Optional 常識層中，TCF 負責知識格式化與來源歸屬，MDAS 負責概念態空間與因果超圖，ADL 負責行動時的強制判斷，三態邏輯負責保留 Ω 未定與螺旋演化狀態。然而，若只到此為止，系統仍缺少一個關鍵層：

當 AI 面對未成熟條件、未定語境、外部事件、人類授權、多 Agent 協作與長時程任務時，它應如何決定「現在判斷」還是「稍後再判斷」？

這一層不是 Cyc 能解決的，也不是單純知識圖譜能解決的。它屬於控制流問題，亦即時間中的判斷治理問題。

本文將其稱為：

**時間迴圈判斷層**
Temporal Loop Judgment Layer

## 1\. 為何需要時間迴圈判斷層？

傳統 AI 判斷通常假設問題在當下必須回答：

Input → Reasoning → Output

但主體性 AI / Agentic AI 面對的真實世界並非如此。許多問題不是「現在答不出來」，而是「條件尚未成熟」。

例如：

-   等使用者授權。
-   等外部 API 回覆。
-   等其他 Agent 完成子任務。
-   等資料同步完成。
-   等市場資料更新。
-   等測試結果出來。
-   等新證據累積。
-   等語境更明確。
-   等多個候選方案跑完評估。
-   等系統冷卻、資源恢復或部署窗口打開。

這些情況不應被視為失敗，也不應全部推給人類判斷。它們應被視為時間化控制流：

Condition not mature
→ Persist state
→ Suspend
→ Wake by time / event / signal
→ Reload
→ Validate
→ Resume / Degrade / Escalate

因此，主體性 AI 的自主性不只是「能回答」，而是：

**能判斷何時不回答、何時等待、何時保存狀態、何時醒來、何時重新判斷、何時降級、何時請求外部主體。**

## 2\. 時間迴圈與三態邏輯的銜接

三態邏輯將判斷域分為：

{ 真, 假, Ω }

其中 Ω 不是失敗，而是螺旋態、未定態、演化態。

但若只有 Ω，系統會知道「此處未定」，卻不一定知道「接下來該怎麼辦」。時間迴圈學補上的正是這一點。

可定義：

Ω\_state + TemporalLoopPolicy = Managed Uncertainty

也就是說：

-   Ω 不再只是未定標記。
-   Ω 會進入某種時間迴圈。
-   時間迴圈決定何時重檢、由誰喚醒、如何恢復、何時降級。

例如：

{
"state": "Omega",
"reason": "context\_not\_mature",
"temporalLoop": {
"type": "condition\_maturation",
"wakeRule": "new\_context\_available",
"resumePolicy": "reload\_validate\_continue",
"timeoutPolicy": "ask\_human\_or\_degrade"
}
}

這使三態邏輯從靜態判斷域，升級為可執行的時間治理結構。

## 3\. 時間迴圈與 ADL 的銜接

ADL 負責強制判斷。當 Agent 必須行動時，系統不能永遠停留在未定狀態。

但不是所有情況都應立刻進入 ADL。若條件未成熟，應先進入時間迴圈；只有在必須行動、超時、資源耗盡、高風險決策或授權邊界到達時，才啟動 ADL。

可定義：

If action\_required\_now:
ADL\_Force\_Judgment()
Else:
TemporalLoop\_Suspend()

因此，ADL 與時間迴圈不是衝突，而是分工：

-   **時間迴圈**：管理尚未成熟的未來。
-   **ADL**：處理必須當下閉合的判斷。
-   **三態邏輯**：保留未定與螺旋演化狀態。

更精確地說：

Ω → TemporalLoop → Recheck
Ω + deadline → ADL
Ω + high\_risk → Human / External Authority
Ω + sufficient\_context → ⊤ / ⊥
Ω + repeated\_failure → Crash / Degrade

## 4\. 時間迴圈與 MDAS 的銜接

MDAS-TCH 將概念放入四層十五態系統與因果超圖。時間迴圈則提供狀態演化的 runtime 機制。

在 MDAS 中，一個概念可能處於：

-   Ψ：混沌態。
-   Δ：臨界態。
-   Ξ：透明態。
-   Θ：黑箱態。
-   Ω：邏輯螺旋態。
-   ⊕：生成態。
-   ⊙：循環態。
-   ⊗：糾纏態。

時間迴圈可以成為這些狀態之間的遷移規則。

例如：

Ψ + knowledge\_accumulation\_loop → Δ
Δ + evaluation\_loop → Ξ
Θ + observation\_loop → Δ
Ω + context\_maturation\_loop → ⊤ / ⊥ / Ω
⊗ + multi\_agent\_coordination\_loop → partial disentanglement

也就是說，MDAS 描述「概念處於什麼態」，時間迴圈描述「概念如何跨時間遷移」。

## 5\. 時間迴圈與 TCF 的銜接

TCF 將理論壓縮成結構化格式，包括原語、公理、DAG、定理、證明、模型、壓縮度量、指紋與 provenance。

但理論不是一次完成的。理論本身也會經過時間迴圈：

v0.1 → 批判 → 修正 → 壓縮 → 實例 → 驗證 → v0.2

因此，TCF 可以加入 Temporal Metadata：

{
"theoryId": "EML-COMMONSENSE-LAYER-v0.1",
"temporalStatus": {
"loopType": "spiral\_progress",
"phase": "awaiting\_formalization",
"nextWake": "new\_counterexample\_or\_schema\_update",
"resumePolicy": "revise\_and\_recompute\_CR",
"timeoutPolicy": "freeze\_as\_draft"
}
}

這代表 TCF 不只是理論快照，也可以成為理論演化的版本化時間容器。

## 6\. 主體性 AI 的自主判斷原則

在加入時間迴圈學後，未來主體性 AI 的判斷模式應從：

遇到不確定 → 問人類

升級為：

遇到不確定 → 判斷不確定類型 → 進入對應時間迴圈 → 條件成熟後自主重判 → 必要時才請求人類

可定義五級自主判斷原則：

### Level 0：立即判斷

條件充足、風險低、語境清楚。

Judge now.

### Level 1：時間等待

條件尚未成熟，但可由時間自然成熟。

Suspend until time / condition.

### Level 2：事件喚醒

需要等待外部事件。

Suspend until event.

### Level 3：演化選路

需要同時探索多個候選方案，等待結果後選擇。

Explore → Evaluate → Select.

### Level 4：外部主體介入

涉及高風險、權限、責任、價值衝突或不可自決事項。

Escalate to human / institution / policy.

這裡的重點是：人類不再是所有未定狀態的預設裁判者。人類只在 Level 4 出現。

## 7\. Agent 常識憲法層的更新架構

加入時間迴圈後，Cyc-Optional Knowledge Layer 應更新為：

LLM / Agent 神經主體
↓
TCF Knowledge Card / Provenance
↓
MDAS Concept-State Hypergraph
↓
Cyc-like / Self-built Commonsense Layer
↓
Triadic Logic Ω Detection
↓
Temporal Loop Judgment Layer
↓
ADL Forced Judgment if Action Required
↓
Execute / Suspend / Wake / Degrade / Escalate

其中，Temporal Loop Judgment Layer 負責決定：

-   當下是否需要判斷？
-   是否條件未成熟？
-   應進入哪一類時間迴圈？
-   應由時間、事件、人類、Agent 還是系統訊號喚醒？
-   是否需要 timeout？
-   timeout 後降級還是升級？
-   醒來後是否重新驗證？
-   是否進入 ADL 強制判斷？

這一層是主體性 AI 的時間治理核心。

## 8\. 對 Cyc 的重新定位

Cyc / OpenCyc 類系統提供的是常識內容、本體論與語境工程經驗。
但它不提供完整的時間化自主判斷 runtime。

因此，在 EML 架構中：

Cyc-like Layer = 常識材料
TCF = 格式與來源
MDAS = 動態態空間
三態邏輯 = 未定態
時間迴圈學 = 未定態的時間治理
ADL = 必須行動時的強制閉合
Agent Runtime = 實際執行

這使 Cyc 更加 optional。
因為即使沒有 Cyc，只要有自建常識庫與時間迴圈判斷層，主體性 AI 仍能自主處理大量未定狀態。

## 9\. 結論

時間迴圈學補上了 Cyc-Optional 架構中最重要的缺口。

沒有時間迴圈，AI 面對未定狀態時只剩三種粗糙選擇：

1.  立刻亂判。
2.  永遠不判。
3.  問人類。

有了時間迴圈，AI 可以：

1.  保存狀態。
2.  暫停判斷。
3.  等待條件成熟。
4.  由事件喚醒。
5.  重新驗證。
6.  自主重判。
7.  超時降級。
8.  高風險時才請求人類。
9.  長期沿著螺旋路線演化。

因此，未來主體性 AI 的真正自主性，不是永遠立即回答，而是能在時間中管理自己的不確定性。

一句話：

**三態邏輯讓 AI 承認 Ω。**
**時間迴圈學讓 AI 管理 Ω。**
**ADL 讓 AI 在必要時閉合 Ω。**

這才是 Agent 常識憲法層的完整形態。
