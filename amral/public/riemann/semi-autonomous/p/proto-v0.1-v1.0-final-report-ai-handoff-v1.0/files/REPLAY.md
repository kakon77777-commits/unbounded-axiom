# 重播與驗證

## 最低驗證

在本目錄執行：

```bash
python3 validate_release.py
```

預期：

- required files 全部存在；
- JSON 全部可解析；
- 十個 canonical source ZIP 的 SHA-256 一致；
- 十個 ZIP 的 CRC 與 internal manifest 全部通過；
- canonical evidence snapshots 與 ZIP members 的 SHA-256 一致；
- hard false/true flags 一致；
- package manifest 全部通過。

此模式適用於只拿到 final synthesis ZIP 的情況：它驗證包內 manifest、recorded canonical audit 與 snapshots。

若十個主鏈 ZIP、六篇前史稿、六個前史工程包及前史整合 ZIP 都位於本包的預期相對位置，執行完整來源重審：

```bash
python3 validate_release.py --require-sources
```

此模式會重新讀取所有 canonical sources，而不只檢查包內的 recorded audit。

## 重建 machine metadata 與 snapshots

本包位於十個來源 ZIP 的同層目錄時，可執行：

```bash
python3 build_release.py
```

該命令會：

1. 直接讀十個 canonical ZIP；
2. 重做 CRC 與 internal manifest audit；
3. 重建 `metadata/*.json`；
4. 重新抽取 `evidence_snapshots/`；
5. 更新 source archive audit。

## 不在 final synthesis 中重跑的部分

本包沒有重新執行十節點的全部高成本 optimization。每節點自己的 replay 與 tests 保留在原始 ZIP；final synthesis 驗證的是：

- canonical source integrity；
- claims/gaps/handoffs 的逐位元快照；
- 跨節點語義與狀態一致性；
- final package 自身完整性。
