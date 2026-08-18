# Dynamic Logic / Generative Judgment Complete v0.3

本包包含完整理論、宗教／終極支線、技術規格與第一個最小 reference replay seed。

## 理論主系列

`00 → 01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09 → 10`

新增 v0.3：

- 08 判斷狀態機的形式語義與轉移公理
- 09 證據圖、真值與判斷狀態解耦
- 10 可重放判斷與語義等價：Event Sourcing → Replay Verification

## 宗教／終極存在支線

`R1 → R2 → R3`

## 技術文件

`T1 → T2 → T3 → T4 → T5 → T6 → T7`

新增 v0.3：

- T6 Dynamic Logic Schema Pack
- T7 EveGlyph Reference Implementation Handoff

## Machine-readable / Demo

- `schemas/*.schema.json`
- `demo/live-judgment-demo.md`
- `demo/demo-events.jsonl`
- `reference/reducer-reference.mjs`
- `reference/test-replay.mjs`

Reference replay golden test 已實際執行通過。

核心原則：

`Replay != Rejudge`

Replay 使用已提交事件重建歷史；Rejudge 才使用新模型重新分析舊證據。
