# Replay

## 1. 環境

建議：

- Python $3.11$ 或更新；
- NumPy；
- SciPy。

exact semantic、cover 與 clamped budget 層只依賴 Python standard
library。浮點對抗診斷需要 NumPy 與 SciPy。

## 2. 完整重建

```bash
python run_all.py
```

執行順序固定為：

```text
run_semantic_bridge.py
generate_cover_certificate.py
verify_cover_certificate.py
run_clamped_radius_certificate.py
verify_clamped_radius_certificate.py
run_floating_clamped_study.py
run_summary.py
verify_outputs.py
validate_package.py
```

## 3. 單元測試

```bash
python run_tests.py
```

預期共有 $8$ 個 tests，全部通過。

## 4. 個別驗證

```bash
python verify_cover_certificate.py
python verify_clamped_radius_certificate.py
python verify_outputs.py
python validate_package.py
```

## 5. Release

```bash
python build_release.py
```

它會在 parent directory 建立：

- `RH_Occupancy_OperatorFamily_v0.9.zip`
- standalone 中文研究稿
- `RH_Occupancy_OperatorFamily_v0.9_SHA256SUMS.txt`

## 6. 乾淨 ZIP 重播

```bash
tmpdir="$(mktemp -d)"
unzip RH_Occupancy_OperatorFamily_v0.9.zip -d "$tmpdir"
cd "$tmpdir/RH_Occupancy_OperatorFamily_v0.9"
python run_all.py
python run_tests.py
python validate_package.py
```

最後可用 `MANIFEST.sha256` 檢查 package tree。parent v0.7 inputs 已鎖定
並內含於 `data/`，乾淨重播不需要 sibling packages。

