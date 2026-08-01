# RH AI 研究起點 v2.1：統一證書後端

本版本整合 RH-W-18。主要新增：

- W-04 至 W-17 的共同 manifest；
- 單一 `rhcert.py` 驗證入口；
- 原生 verifier adapter；
- artifact SHA-256 identity；
- claim firewall；
- legacy incomplete 與 superseded 狀態；
- 三層 adversarial red-team。

執行：

```bash
cd RH_W_18_工程包_v0.1
python rhcert.py verify
python redteam_backend.py
```

本版本不證明或反證黎曼猜想。
