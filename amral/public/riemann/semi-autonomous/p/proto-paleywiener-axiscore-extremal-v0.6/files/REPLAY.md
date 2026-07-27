# Replay

安裝：

```bash
python -m pip install -r requirements.txt
```

## 快速驗證

```bash
python -m unittest discover -s tests -v
python verify_outputs.py
python validate_package.py
```

## 完整研究重播

```bash
python run_green_rank_two.py
python run_quadrature_audit.py
python run_galerkin_convergence.py
python run_atomic_transfer.py
python run_certificate_budget.py
python run_rational_witness.py
python run_summary.py
python verify_outputs.py
python validate_package.py
```

`run_galerkin_convergence.py` 的 raw dimensions 176 與 192 是主要計算成本；
執行時間依 BLAS、CPU 與執行緒設定不同。

## Release

```bash
python build_release.py
```

它會建立：

- package-level `MANIFEST.sha256`；
- 完整 ZIP；
- standalone 主研究稿；
- 外部 `SHA256SUMS.txt`。

解壓後可先執行：

```bash
sha256sum -c MANIFEST.sha256
```

再做快速驗證。
