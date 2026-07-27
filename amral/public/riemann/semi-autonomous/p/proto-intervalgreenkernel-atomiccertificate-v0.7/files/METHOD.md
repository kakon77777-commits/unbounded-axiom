# Method

## 1. 為什麼不用時間網格

v0.6 已用三個 time steps 觀察到 Green reconstruction 收斂，但普通
trapezoid quadrature 不能自動提供 directed enclosure。v0.7 改寫每個
density 為有限 exponential sum，直接使用 clamped boundary-value
problem 的閉式 representer。

這消除了：

- time-step truncation；
- numerical ODE solve；
- Galerkin dictionary；
- 對高頻 oscillation 的 sampling ambiguity。

## 2. 超越函數包絡

### 2.1 $\pi$

使用 Machin identity

$$
\pi
=
16\arctan\left(\frac15\right)
-4\arctan\left(\frac1{239}\right).
$$

每個 arctangent 用 alternating series，分別取 $96$ 與 $40$ 項，並
以第一個 omitted term 給出 rational remainder enclosure。

最終

$$
\pi\in
[
3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482,
$$

$$
3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803483
].
$$

### 2.2 三角函數

對 rational angle $\theta$ 選整數 $k$，令

$$
r=\theta-k\frac{\pi}{2},
$$

並驗證整個 interval $r$ 落在絕對值小於 $0.8$ 的區域。再以 $44$ 項
Taylor polynomial 與 Lagrange remainder 包住 $\sin r$ 和 $\cos r$，
最後依 $k\bmod4$ 回復象限。

### 2.3 指數函數

先取 $m$ 使

$$
\left|\frac{x}{2^m}\right|\leq\frac1{16},
$$

對 reduced argument 使用 $48$ 項 Taylor polynomial，並用

$$
e^{|\xi|}<2
$$

包住 remainder；之後進行 $m$ 次 interval squaring。

## 3. Directed decimal arithmetic

所有證明運算使用 $90$ 位十進位 precision：

- lower endpoints 使用 `ROUND_FLOOR`；
- upper endpoints 使用 `ROUND_CEILING`；
- ordinary floating point 只用來產生 inverse candidate 與 diagnostic
  comparison，不提供證明端點。

所有 finite decimal endpoints 本身都是有理數。

## 4. 雙向 Green pairing 交集

自伴 Green operator 滿足

$$
\Gamma(a,b)=\Gamma(b,a).
$$

程式以兩種 boundary orientation 獨立計算 exponential pairing，然後
取兩個 rigorous intervals 的交集。若交集為空，程式立即失敗。

這同時：

- 縮小 cancellation enclosure；
- 檢查 $b=0$ 特例和 $b\neq0$ Hermite correction 的一致性；
- 防止只沿單一公式路徑悄悄漂移。

## 5. 結構投影

先完整 enclosure structural $2\times2$ Gram determinant，只有在其
lower endpoint 嚴格為正後才建立 interval inverse。所有 evaluation
pairings 再逐一扣除 finite-rank correction。

完整 projected Gram 的 endpoint serialization 取 SHA-256，證書讀回
重算時必須完全一致。

## 6. Neumann certificate

不直接做 interval Gaussian elimination。普通 NumPy inverse 只生成
finite-decimal rational candidate $\mathcal R$。真正的 regularity proof
是 directed recomputation：

$$
q=
\left\|I-\mathcal R\mathbf A\right\|_\infty<1.
$$

此方法把「猜一個 inverse」與「證明它對整個 interval family 有效」
分離。把 candidate 替換成零矩陣時，測試必須因 $q=1$ 而拒絕。

## 7. 三種重播

1. `verify_certificate.py`：重建全部 transcendental、Green、projection、
   Neumann 與 Sylvester intervals。
2. `audit_certificate.py`：用 `Fraction` 對已序列化的 strict
   inequalities、probability sums 與 trust flags 做精確審計。
3. unit tests：檢查 $\pi$、三角恆等式、指數互逆、constant Green closed
   form、完整證書與 failure injection。

## 8. Coefficient orientation audit

對 band $[a,b]$，標準 difference identity 給出

$$
N(b)-N(a)
=
\frac{\theta(b)-\theta(a)}{\pi}
+S(b)-S(a).
$$

若只有

$$
|S(T)|\leq B(T),
$$

則可直接推出

$$
L_{a,b}
=
\frac{\theta(b)-\theta(a)}{\pi}
-B(a)-B(b)
$$

與

$$
U_{a,b}
=
\frac{\theta(b)-\theta(a)}{\pi}
+B(a)+B(b).
$$

v0.6 的係數符合 $U_{a,b}$ 的 downward-rounded profile，而不是
$L_{a,b}$。因此 v0.7 不把 abstract certificate 超譯為 zeta theorem。
