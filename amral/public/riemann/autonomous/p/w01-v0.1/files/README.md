# RH-W-01 工程包 v0.1

本包是 RH GAP Atlas 的第一個正式工作單位。

它不嘗試證明黎曼猜想，而是固定 Weil 顯式公式路線的測試函數空間、Mellin 正規化、零點求和方式、卷積／相關型與符號慣例，並將原先單一 `RH-W-01` 拆成八個可獨立接力的子 GAP。

## 內容

- `RH-W-01_測試函數空間固定_v0.1.md`：主規格文件
- `RH-W-01_subgaps.json`：機器可讀子 GAP
- `RH-W-01_subgaps.csv`：試算表版本
- `candidate_schema.json`：候選生成器提交格式
- `validate_w01.py`：登錄檢查器
- `VALIDATION.txt`：檢查結果

## 核心狀態

- 已固定：B0 基準公式與符號
- 未完成：候選生成族、閉包拓撲、負證人壓縮、形式化
- 下一節點：`RH-W-01-D/E`
