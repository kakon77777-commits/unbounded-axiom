# Replay

## Environment

建議：

- Python $3.11$ 或更新版本；
- NumPy；
- SciPy。

安裝：

```bash
python -m pip install -r requirements.txt
```

## Full replay

依序執行：

```bash
python generate_certificate.py
python verify_certificate.py
python run_coefficient_orientation_audit.py
python run_orientation_stress_test.py
python run_floating_crosscheck.py
python audit_certificate.py
python -m unittest discover -s tests -v
python validate_package.py
```

## Expected proof markers

`generate_certificate.py` 應輸出：

- `abstract_continuous_interval_certificate: true`
- `global_rh_certificate: false`
- Neumann defect upper 約 $7.5314\times10^{-15}$；
- first minor lower 約 $0.352428$；
- determinant lower 約 $0.0636153$。

`verify_certificate.py` 的所有 checks 都應為 true。

`run_coefficient_orientation_audit.py` 應輸出：

- `orientation_blocker_confirmed: true`
- `all_stored_coefficients_are_lower_certificates: false`
- `global_rh_certificate: false`

unit tests 應通過 $10$ 項檢查，包含一個故意把 inverse candidate 改成零
矩陣的 failure injection。

## What is regenerated

完整重播會重建：

1. Machin $\pi$ enclosure；
2. 所有 rational-angle 三角函數；
3. 所有 real exponential factors；
4. 全部 exponential moments；
5. clamped Green pairings；
6. structural projection；
7. projected Gram hash；
8. Neumann defect 與 solution radii；
9. final Sylvester intervals。

## Release integrity

發布包內執行：

```bash
sha256sum -c MANIFEST.sha256
```

外部下載後執行：

```bash
sha256sum -c RH_IntervalGreenKernel_AtomicCertificate_v0.7_SHA256SUMS.txt
```

## Runtime expectation

在一般桌面 CPU 上，完整 projected Gram 重建通常需要十餘秒。這是
$62\times62$ pairings 的 closed-form interval evaluation，不是卡住或
網路存取。
