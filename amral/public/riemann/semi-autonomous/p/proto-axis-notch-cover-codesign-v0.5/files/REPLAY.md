# Replay

Python 需求：

```bash
python -m pip install -r requirements.txt
```

## 快速完整性重播

這一層不重跑長時間 optimization：

```bash
python -m unittest discover -s tests -v
python verify_joint_results.py
python validate_package.py
```

## 由保存輸入重建探索輸出

依序執行：

```bash
python run_peak_atlas.py
python run_notch_screen.py
python run_lift_screen.py
python run_lift_scaling.py
python run_lift_joint.py
python run_geometry_screen.py
python run_geometry_joint.py
python verify_joint_results.py
python run_summary.py
python validate_package.py
```

完整 optimization 的時間依 BLAS、CPU 與執行緒配置而變；joint 與
27-geometry sweep 是主要成本。輸出是 deterministic floating research
objects，但不同線性代數函式庫可能造成末位差異。

## Release

在套件根目錄執行：

```bash
python build_release.py
```

它會：

1. 排除 cache 產生 `MANIFEST.sha256`；
2. 建立頂層同名資料夾的 ZIP；
3. 複製 standalone 研究稿；
4. 建立外部 `SHA256SUMS.txt`。

解壓後可用：

```bash
sha256sum -c MANIFEST.sha256
```

檢查套件內檔案。
