# Replay

## 環境

Python 3.12，依賴：

```text
numpy>=2.0
scipy>=1.14
```

## 快速核驗

```bash
python run_source_profile.py
python run_cover_audit.py
python verify_saved_witnesses.py
python -m unittest discover -s tests -v
python validate_package.py
```

`verify_saved_witnesses.py` 會從 12 份 JSON 中重建正規化 measure
witness，不重新做 joint optimization。

## 中等成本重播

```bash
python run_prime_cost.py
```

這會實際枚舉到 $R=10.25$，本機參考時間約數秒；硬體不同時時間會變。

## 高成本重播

```bash
python run_frontier_sweep.py
python run_axis_refinement.py
python run_joint_dual.py
```

`run_joint_dual.py` 會重做 12 個 joint optimizations；參考時間約數分鐘。
`run_axis_refinement.py` 包含步長 $0.025$ 的 $R=16$ 最佳化。

## 建立 release

```bash
python validate_package.py
python build_release.py
```

release 會在 package 上層產生 ZIP、獨立研究稿與 SHA256SUMS。

## 重播限制

浮點最佳化的最後數字可能隨 BLAS、SciPy 與硬體略變。判定應以安全
margin、重建 PSD 與 trust boundary 為準，不應要求逐 bit 相同。

