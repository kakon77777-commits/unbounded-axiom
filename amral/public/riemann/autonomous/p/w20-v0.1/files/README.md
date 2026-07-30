# RH-W-20 工程包 v0.1

## 狀態

- Batch：`RH Engineering Relay — Batch 01`
- 範圍：`RH-W-01` ～ `RH-W-20`
- 平台案例：`CASE-0001-RH-WEIL-BATCH01`
- 結論：`BATCH01_COMPLETE`
- `RH_CLAIM=false`

## 快速驗證

```bash
python verify_batch01_release.py
```

完整驗證會：

1. 驗證 Case 0001 JSON/CSV 結構與二十節點完整性；
2. 檢查 dependency graph 無研究接力環路；
3. 檢查所有 claim、failure、trust 與 handoff 均禁止 RH 升格；
4. 重放 `backend_v0.2/rhcert.py verify`；
5. 重放 `backend_v0.2/redteam_zoo.py`；
6. 驗證 release SHA-256 索引。

## 主要文件

- `01_RH-W-20_Batch01統合與Case0001發行_v0.1.md`
- `02_RH-W-20_二十輪研究地圖與有限數學結果總表_v0.1.md`
- `03_RH-W-20_失敗修正信任邊界與研究倫理_v0.1.md`
- `04_RH-W-20_Batch02交棒與平台匯入規格_v0.1.md`
- `platform_case_0001/`
- `backend_v0.2/`
