# Results

## 1. Semantic bridge

| transfer | status |
|---|---|
| count upper $\to$ supremum leakage upper bound | valid |
| count lower $\to$ infimum scalar lower bound | valid |
| count lower $\to$ arbitrary probability average | false |
| upper-envelope lower bound $\to$ actual zero-sum lower bound | false |
| upper-envelope lower bound $\to$ method no-go | valid |

二點 exact countermodel 滿足

$$
Z=0,\qquad
L\int H\,d\delta_{x_1}=1.
$$

因此第三條不是缺少精度，而是一般命題本身為假。

## 2. Five-band floating profiles

| band | lower candidate | upper candidate |
|---|---:|---:|
| $A_0=[14,18]$ | $0$ | $6.797423271049$ |
| $A_1=[18,23]$ | $0$ | $7.246636980607$ |
| $A_2=[23,35]$ | $0$ | $9.346770522331$ |
| $A_3=[35,70]$ | $5.069962795568$ | $18.367573606597$ |
| $A_4=[70,145]$ | $26.742367141539$ | $40.545362729237$ |

表中數值是 floating profile。endpoint convention 與 transcendental
directed enclosure 尚未證書化。

## 3. Robust lower-profile search

| raw dimension | effective dimension | optimized $\alpha$ |
|---:|---:|---:|
| $24$ | $22$ | $2.6662663794$ |
| $40$ | $38$ | $1.0616159317$ |
| $64$ | $62$ | $0.4565992248$ |
| $80$ | $78$ | $0.3168124263$ |
| $96$ | $94$ | $0.2363398270$ |
| $120$ | $118$ | $0.1705859126$ |
| $144$ | $142$ | $0.1394428108$ |
| $160$ | $158$ | $0.1301510855$ |
| $176$ | $174$ | $0.1297049092$ |
| $192$ | $190$ | $0.1297047862$ |

第一個低於 $1$ 的 raw dimension 是 $64$。所以低維

$$
\alpha>1
$$

在正確 lower candidate profile 下是明確的 Galerkin truncation
artifact。

## 4. Direct Green transfer

| $\Delta t$ | grid count | threshold |
|---:|---:|---:|
| $0.02$ | $1601$ | $0.1296980713$ |
| $0.01$ | $3201$ | $0.1297028387$ |
| $0.005$ | $6401$ | $0.1297031276$ |

最後值與 effective dimension $190$ Galerkin 值相差小於

$$
1.7\times10^{-6}.
$$

## 5. Sampled primal escape

在 $101\times101$ core grid 與 axis step $0.01$ 下，正規化後得到

$$
\max_{\mathrm{core\ grid}}B=-1
$$

及

$$
\mathcal E_L^{\mathrm{sampled}}
=
0.1297069814.
$$

非零 band 的 sampled maxima 約為

$$
\sup_{A_3}H
\approx
1.00123\times10^{-5},
$$

$$
\sup_{A_4}H
\approx
2.95980\times10^{-8}.
$$

因此下輪不應嘗試把原 upper-profile witness 重新微調成 lower-profile
obstruction。

## 6. v0.7 的新分類

v0.7 的 interval certificate 保留：

$$
W_{21/20}\succ0
$$

仍是已完成的 abstract continuous theorem。

但其兩個外部解讀分開：

- upper-envelope method no-go：有希望，尚缺 count/tail source theorem；
- actual zero-side positive obstruction：未證，且 scalar counts 不足。

## 7. Prototype relevance

目前 patch 高度約 $20.4$。Platt–Trudgian 已嚴格驗證所有高度不超過
$3\cdot10^{12}$ 的非平凡 $\zeta$ 零點都在臨界線上。因此這個 patch
在本研究中只能作 functional-analytic prototype，不是未決的實際
$\zeta$ 偏軸區域。

## 8. Decision

下一個資料結構不能再是

$$
[L_j,U_j]
$$

而必須是帶位置量詞的 occupancy/operator-family certificate，例如：

$$
\gamma_{jk}\in I_{jk},
\qquad
m_{jk}\ge1,
$$

以及對所有允許位置共同成立的

$$
W_\alpha(\gamma_{11},\ldots,\gamma_{JK})
\succeq0.
$$

若沒有位置或局部組態資訊，count lower 只能落到 infimum，通常退化到
零。
