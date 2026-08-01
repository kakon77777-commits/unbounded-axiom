# RH-W-18 統一證書後端

執行：

```bash
python rhcert.py list
python rhcert.py verify
python redteam_backend.py
```

預期總狀態：`PASS_WITH_DECLARED_LIMITATIONS`。限制不是執行失敗，而是 manifest 中明示的 `PROTOCOL_ONLY`、`SUPERSEDED_RECERTIFIED` 與 `LEGACY_INCOMPLETE`。

本包不證明或反證黎曼猜想。

狀態計數：11 `VERIFIED`、1 `PROTOCOL_ONLY`、1 `SUPERSEDED_RECERTIFIED`、1 `LEGACY_INCOMPLETE`。
