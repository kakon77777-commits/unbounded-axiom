# RH v0.1–v1.0 完整研究報告與 AI 交接

本包整合十個主研究節點、前史來源索引、統一 claim register、GAP ledger、失敗—修正地圖、依賴圖、後續 AI 執行協定，以及由 canonical ZIP 逐位元抽出的核心證據快照。

本包不證明或反證黎曼猜想。

目前最高正面結論是在抽象 clamped Green/operator 模型內，對 $58$ 個獨立位置變量證得半寬

$$
h=1.78\times10^{-6}
$$

的 downward-closed interval cover family。`actual_zeta_occupancy_family`、`explicit_formula_transfer_certified` 與 `global_rh_certificate` 均為 `false`。

## 閱讀順序

1. `RH半AI自主研究完整報告_v0.1-v1.0_與後續AI交接_v1.0.md`
2. `AI_HANDOFF.md`
3. `metadata/ai-handoff.json`
4. `metadata/claim-register.json`
5. `metadata/gap-ledger.json`
6. `metadata/failure-correction-map.json`
7. `metadata/dependency-graph.json`
8. `validation/source-archive-audit.json`

## 目錄

- `metadata/`：統一 machine-readable 帳本與交接；
- `evidence_snapshots/`：十個 canonical source ZIP 的核心 claim、GAP、handoff、summary 與 trust-boundary 快照；
- `validation/`：來源 archive、snapshot 與 release 驗證；
- `build_release.py`：從 canonical ZIP 重建 metadata 與 snapshots；
- `validate_release.py`：獨立檢查 final package；
- `REPLAY.md`：重播程序；
- `TRUST_BOUNDARY.md`：允許與禁止的推論。

完整十個來源 ZIP 不重複塞入本包；其名稱、大小與 SHA-256 位於 `metadata/artifact-index.json`。

