# Results

## 1. Exact semantic bridge

`OccupancySelectionOperatorTransfer` 已以符號層閉合：

$$
\text{cell occupancy}
+
\text{universal selected family}
\Longrightarrow
\text{all-point operator positivity}.
$$

它不允許以下替換：

$$
\text{count lower}
\rightsquigarrow
\text{arbitrary measure operator mass}.
$$

## 2. Count-only exact failure

在 Dirichlet Green model 中，同樣 total count $2$ 但兩點都位於 $1/5$
時：

| quantity | exact value |
| --- | ---: |
| Schur determinant | $-254/558009$ |
| certified negative quadratic | $-663194/13755479859$ |
| operator PSD | false |

因此「有兩點」與「左右 cell 各有一點」具有不同 operator 語義。

## 3. Exact adaptive cover

| quantity | result |
| --- | ---: |
| root box directly certified | false |
| total tree nodes | $15$ |
| certified leaves | $8$ |
| unresolved leaves | $0$ |
| maximum leaf depth | $7$ |
| minimum first-minor lower | $936790565/9707986602$ |
| minimum determinant lower | $996149099768633906407318481/92259342242007809509970517515625$ |

根盒失敗是 interval dependency failure；cover family 成功後，合成
uncertain-location operator family 對全部位置嚴格 positive。

## 4. Conditional clamped $58$-cell family

| quantity | exact value |
| --- | ---: |
| parent alpha | $21/20$ |
| child alpha | $1$ |
| convex margin | $1/21$ |
| independent location cells | $58$ |
| uniform half-width | $1/500000000000000$ |
| perturbation upper | $12328822128706060288/299401138693037109375$ |
| coercivity lower | $13498624663403281109/2095807970851259765625$ |
| budget critical half-width | $10219558867389/4418649850928252007219200000$ |

在 parent v0.7 abstract theorem 下，這是一張精確 universal location
family certificate。它仍是 coordinate-dependent dual-atom calibration，
不是實際零點 occupancy。

## 5. Floating adversarial corner study

| cell half-width | adversarial threshold at $\Delta t=0.02$ |
| ---: | ---: |
| $0.012$ | $1.0458517424$ |
| $0.014$ | $1.0240427949$ |
| $0.015$ | $1.0124640056$ |
| $0.016$ | $1.0004604738$ |
| $0.017$ | $0.9880516263$ |
| $0.018$ | $0.9748129050$ |
| $0.020$ | $0.9471623347$ |

固定角點的 finest-step values 為：

| half-width | $\Delta t=0.005$ threshold |
| ---: | ---: |
| $0.015$ | $1.0124737413$ |
| $0.016$ | $1.0004702150$ |
| $0.017$ | $0.9880613743$ |

這些數字只描述 deterministic corner search，沒有 universal quantifier。

## 6. 決策

保留 occupancy/operator-family 主線，下一節點不回去追求更精細的 scalar
count profile。優先開發 local interval clamped-Green derivative bounds
與 adaptive location-cell Schur cover，以縮小約 $8\times10^{12}$ 的
proof-budget gap。

$\zeta$ occupancy presence theorem 與 upper-envelope no-go source
certification 保持為兩條獨立工作線。

