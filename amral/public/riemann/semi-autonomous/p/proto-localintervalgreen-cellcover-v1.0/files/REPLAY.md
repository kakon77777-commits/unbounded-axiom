# 重播

## 環境

- Python $3.11$ 或更新版本
- NumPy $1.26$ 或更新版本

安裝依賴：

```bash
python -m pip install -r requirements.txt
```

## 快速驗證

在包根目錄執行：

```bash
PYTHONPATH=. python verify_cell_cover.py
PYTHONPATH=. python run_summary.py
PYTHONPATH=. python run_tests.py
```

`verify_cell_cover.py` 會重建半徑 $1.78\times10^{-6}$ 的最大盒 Gram 族與距中心 $10^{-3}$ 的精確角點 Gram，通常約需一分鐘。

## 完整重建

```bash
PYTHONPATH=. python run_all.py
```

它依序：

1. 重算七級半徑階梯、最大盒、覆蓋族及角點；
2. 獨立重驗最大盒與角點；
3. 生成摘要；
4. 跑七個快速測試；
5. 執行全包語義與檔案檢查。

完整重建時間主要由九次 $62\times62$ 區間 Green–Gram 計算構成。

## 輸出判讀

成功時應看到：

- `maximum_certificate_verifies: true`
- `cover_family_verifies: true`
- `radius_ladder_verifies: true`
- `corner_diagnostic_verifies: true`
- `global_rh_certificate: false`

最後一項保持 `false` 是正確結果，不是驗證失敗。

## 封裝

```bash
PYTHONPATH=. python build_release.py
```

封裝器先執行驗證，更新 `MANIFEST.sha256`，再生成 ZIP、獨立中文研究稿與 SHA-256 清單。

