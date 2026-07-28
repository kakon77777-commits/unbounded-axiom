# RH-W-03 工程包 v0.1

本包關閉「RH 若假，是否存在緊支撐負證人」的存在性 GAP，並把下一階段轉為有限維負證書工程。

## 核心變更

- 建立 `C_full = C_c^∞(0,∞)` 與 `C_00` 雙核心架構。
- 固定完整端點修正公式。
- 將 `GLOBAL-DENSITY` 對完整核心標為不必要橋樑。
- 建立有限支撐最低 Rayleigh 商 `lambda(a)`。
- 固定一側證書語義：負值可反駁，有限非負不可證明。

## 檔案

- `01_RH-W-03_緊支撐分離與核心分裂_v0.1.md`
- `02_RH-W-03_有限支撐譜掃描規格_v0.1.md`
- `RH-W-03_subgaps_v0.1.json/csv`
- `separation_contract.json`
- `GAP_STATUS_PATCH_v0.6.json`
- `rh_w03_toy_certificate.py`
- `validate_registry.py`

## 執行

```bash
python validate_registry.py
python rh_w03_toy_certificate.py
```

第二支程式只使用人工合成的零點集合，目的為測試負方向搜尋接口，不是 RH 的數值實驗。
