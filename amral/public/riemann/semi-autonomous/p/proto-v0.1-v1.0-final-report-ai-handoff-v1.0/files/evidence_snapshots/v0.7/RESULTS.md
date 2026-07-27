# Results

## 1. Layer A interval certificate

固定資料：

| 項目 | 值 |
|---|---:|
| radius | $16$ |
| target | $\alpha=21/20$ |
| axis atoms | $58$ |
| core atoms | $2$ |
| positive rank | $60$ |
| negative rank | $2$ |
| decimal precision | $90$ |

核心 enclosure：

| 檢查 | rigorous bound |
|---|---:|
| structural determinant lower | $6.087163164690596\times10^{20}$ |
| maximum projected Gram width | $3.71216\times10^{-84}$ |
| Neumann defect upper | $7.531404753645390\times10^{-15}$ |
| solution radius, column $1$ | $6.479135069600651\times10^{-16}$ |
| solution radius, column $2$ | $2.881263499141683\times10^{-16}$ |
| first Sylvester minor lower | $0.3524279496453903$ |
| determinant lower | $0.0636153172597786$ |

結論：

$$
W_{21/20}\succ0
$$

於套件明確定義的 abstract continuous model。

## 2. Floating cross-check

將 interval midpoint 轉回 v0.6 的 scaled Schur convention，得到

$$
\lambda_{\min}^{\mathrm{mid}}
\approx
0.06988523568969546.
$$

v0.6 最細 time-grid diagnostic 為

$$
\lambda_{\min}^{\mathrm{grid}}
\approx
0.06988523379762435.
$$

差值約

$$
1.8921\times10^{-9}.
$$

此比較只作交叉診斷；證明本身不使用該差值。

## 3. Coefficient orientation

令

$$
B(T)
=
0.112\log T
+0.278\log\log T
+2.510.
$$

| band | stored coefficient | lower count from $|S|$ only | profile |
|---|---:|---:|---|
| $A_0=[14,18]$ | $6.797423271048$ | $0$ | upper |
| $A_1=[18,23]$ | $7.246636980606$ | $0$ | upper |
| $A_2=[23,35]$ | $9.346770522330$ | $0$ | upper |
| $A_3=[35,70]$ | $18.367573606596$ | $5.069962795569$ | upper |
| $A_4=[70,145]$ | $40.545362729236$ | $26.742367141539$ | upper |

五個 stored coefficients 全部符合 downward-rounded upper profile；沒有
一個由目前的 absolute-$S$ argument 直接保證為 positive lower
coefficient。

## 4. Orientation stress test

保留 atoms、probability weights、core measure、kernel 與
$\alpha=21/20$，只把五個 band coefficients 換成上述 lower profile。

所得 floating Schur eigenvalues 約為

$$
-5.53605304212116
$$

與

$$
0.942631731149592.
$$

所以原固定 witness 不會在此替代下存活。這不是「所有可能 witness
皆不存在」的 interval theorem；它只證明下一輪不能機械地把 upper
coefficients 換成 lower coefficients 後宣稱完成。

## 5. 研究判斷

v0.7 成功關閉了四個 v0.6 gaps：

- interval Green pairings；
- structural projection enclosure；
- verified positive solve；
- final Schur positivity。

但 coefficient orientation audit 把真正的下一個瓶頸提前暴露：

$$
\text{continuous numerical legitimacy}
\neq
\text{zeta coefficient legitimacy}.
$$

因此下一輪不先擴張到完整 covering family，而先建立 robust count
coefficient bridge。
