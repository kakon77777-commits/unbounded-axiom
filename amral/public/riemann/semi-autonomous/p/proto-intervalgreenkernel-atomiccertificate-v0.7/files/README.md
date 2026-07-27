# RH Interval Green-Kernel Atomic Certificate v0.7

本套件把 v0.6 的浮點連續核見證提升為可重播的 Layer A 區間證書。

固定

$$
R=16,\qquad
\alpha_\star=\frac{21}{20},
\qquad
\kappa=
\frac{31794183142988}{10^{18}},
$$

以及 v0.6 的 $58$ 個 axis atoms、$2$ 個 core atoms 和全部有理權重。

## 本輪成立的結果

在明確定義的 real-even clamped $H_0^2(-16,16)$ 模型中，程式以
$90$ 位 directed-decimal interval arithmetic 重建全部連續 Green
pairings、兩個結構約束的投影、$60$ 維正因子系統與最後的 $2$ 維負
Schur complement。

最終得到

$$
\inf T_{11}>0.3524279496453903,
$$

以及

$$
\inf\det T>0.0636153172597786.
$$

因此固定抽象模型中的 operator 滿足

$$
W_{21/20}\succ0.
$$

配合 v0.6 已證明的 weak duality，可在此抽象模型內推出

$$
\Lambda_{16}\geq\frac{21}{20}>1.
$$

## 本輪同時發現的阻塞

五個既有 band coefficients 是由

$$
\frac{\theta(b)-\theta(a)}{\pi}
+B(a)+B(b)
$$

形成的上界輪廓，而非由

$$
\frac{\theta(b)-\theta(a)}{\pi}
-B(a)-B(b)
$$

形成的下界證書。把上界向下取整，不會使它成為下界。

所以：

- Layer A 區間定理成立；
- 既有 coefficient data 尚不能直接轉成 zeta-facing positive-axis
  lower contribution；
- 本套件不是 RH 證明或反證。

## 快速重播

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

## 重要檔案

- `outputs/interval_atomic_certificate.json`：完整區間證書與有理
  Neumann candidate。
- `outputs/certificate_verification.json`：從磁碟讀回後的完整重算。
- `outputs/coefficient_orientation_audit.json`：band coefficient
  上下界方向審計。
- `outputs/orientation_stress_test.json`：換成僅由 $|S(T)|$ 能保證的
  lower profile 後之反壓測試。
- `TRUST_BOUNDARY.md`：合法解讀與未完成項目。
- `NEXT_NODE_ROBUST_COUNTS.md`：v0.8 研究節點。

## 依賴

- Python $3.11$ 或更新版本；
- NumPy；
- SciPy 僅用於 coefficient orientation 的浮點診斷。

核心區間證書不以 SciPy 的特殊函數輸出作為證明端點。
