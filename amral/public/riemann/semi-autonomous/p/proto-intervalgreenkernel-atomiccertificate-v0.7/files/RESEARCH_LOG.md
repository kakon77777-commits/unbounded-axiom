# Research Log

## 2026-07-25：接手 v0.6

固定研究決策：

- 不再增加 Galerkin dimension；
- 不再搜尋新的 axis dictionary；
- 固定 $\alpha=21/20$；
- 固定 $58$ axis atoms 與 $2$ core atoms；
- 先完成 abstract continuous interval certificate。

## Closed-form Green route

最初考慮 composite interval quadrature，但高頻 densities 會使
derivative remainder 與二重 Green integral 過度膨脹。改採
exponential decomposition：

$$
\cos(xt)
=
\frac{e^{ixt}+e^{-ixt}}{2},
$$

以及相應的 trigonometric-hyperbolic 四項分解。

clamped boundary-value problem 可化為 exponential particular solution
加 cubic correction，使所有 pairings 只需有限 moments。

## Arithmetic route

環境沒有預裝 Arb／FLINT。為避免把任意精度浮點冒充 interval：

- 以 Machin alternating series 自建 $\pi$ enclosure；
- 以 directed `Decimal` contexts 實作基本 interval operations；
- 以顯式 Taylor remainder 包住 $\exp$、$\sin$、$\cos$；
- 保存的 endpoints 全部為 finite-decimal rationals。

## Solver route

直接 interval elimination 雖可嘗試，但證書較大且依賴傳播難審計。
改用：

$$
\|I-\mathcal R A\|_\infty<1.
$$

ordinary floating inverse 只負責提出 $\mathcal R$；directed interval
recomputation 才負責證明。

## Certificate result

得到：

$$
\|I-\mathcal R A\|_\infty
\leq
7.531404753645390\times10^{-15},
$$

$$
\inf T_{11}
>
0.3524279496453903,
$$

$$
\inf\det T
>
0.0636153172597786.
$$

Layer A 成功。

## Failure injection

把保存的 inverse candidate 全部改成零。此時

$$
\|I-\mathcal R A\|_\infty=1,
$$

驗證器必須拋出錯誤。測試通過，證明 verifier 不會無條件接受
certificate flags。

## Unexpected but decisive finding

審計父節點的 band coefficient code 時發現：

$$
\text{stored coefficient}
\approx
\frac{\Delta\theta}{\pi}+B(a)+B(b),
$$

即 upper count profile。

若正向 axis operator 需要 guaranteed lower coefficient，正確的直接
bound 應是

$$
\max\left(
0,\
\frac{\Delta\theta}{\pi}-B(a)-B(b)
\right).
$$

前 $3$ 帶的此下界全為 $0$。固定 witness 的 lower-profile stress test
出現約

$$
\lambda_{\min}=-5.53605.
$$

因此 v0.8 必須先解決 coefficient semantics；不能把 Layer A 的成功
直接推向 covering expansion。

## Research decision

下一輪優先順序：

1. 回到零點側不等式，逐行確認 coefficient direction。
2. 將每帶係數改成 uncertainty interval。
3. 若 worst-case lower endpoints 不足，加入 validated zero-count 或
   zero-presence objects。
4. 重新最佳化 robust witness。
5. 只有 robust zeta-facing single-patch certificate 成立後，才擴張
   分帶、多測試函數、覆蓋式證書族。
