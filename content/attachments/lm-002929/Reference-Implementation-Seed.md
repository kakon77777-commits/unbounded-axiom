# Reference Implementation Seed

本資料夾目前不提供完整 runtime 實作，避免在 EveGlyph 既有架構之外另造第二套 evaluator。

工程實作請依：

- `../T2_EveGlyph_Dynamic_Logic_Integration_Spec_v0.1.md`
- `../T6_Dynamic_Logic_Schema_Pack_v0.1.md`
- `../T7_EveGlyph_Dynamic_Logic_Reference_Implementation_Handoff_v0.1.md`
- `../demo/demo-events.jsonl`

第一個必須通過的 golden behavior：

`omega -> provisionally_true -> omega -> provisionally_false`

Replay 必須使用 committed events，不重新呼叫 stochastic model。
