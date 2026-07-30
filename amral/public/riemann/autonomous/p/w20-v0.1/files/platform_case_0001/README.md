# Case 0001 平台匯入包

入口：`platform_import_manifest.json` → `case_manifest.json`。

## 強制規則

- 保留所有穩定 ID。
- 不把 `DOCUMENTED_DERIVATION`、`PROTOCOL_ONLY`、`VERIFIED`、`LEGACY_INCOMPLETE`、`SUPERSEDED_RECERTIFIED` 合併成同一狀態。
- 所有頁面維持 `RH_CLAIM=false`。
- `round_packages/` 內含 W-01～W-19 原始工程 ZIP；W-20 ZIP 以發行後 sidecar hash 記錄。
