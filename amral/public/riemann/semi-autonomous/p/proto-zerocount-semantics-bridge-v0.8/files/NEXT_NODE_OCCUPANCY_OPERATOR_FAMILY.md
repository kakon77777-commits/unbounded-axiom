# Next Node: Occupancy Operator Family v0.9

## 決策

不要再把 scalar count lower profile 乘上任意 atomic dual measure。
下一節點改建 location-aware occupancy certificate。

## 目標 schema

每個 band 至少保存：

```json
{
  "band_id": "A_j",
  "endpoint_convention": "...",
  "cells": [
    {
      "interval": ["a_jk", "b_jk"],
      "multiplicity_lower": 1,
      "presence_theorem": "...",
      "source_hash": "...",
      "interval_status": "certified"
    }
  ]
}
```

## Operator 量詞

不要先尋找可能只能為零的固定

$$
Q_{jk}\preceq P_x
\qquad
\forall x\in I_{jk}.
$$

保留 uncertain locations

$$
x_{jk}\in I_{jk},
$$

並直接 interval-certify

$$
W_\alpha(\{x_{jk}\})
\succeq0
\qquad
\forall x_{jk}\in I_{jk}.
$$

因 negative core rank 很低，仍可嘗試把無限維判定降成 small Schur
matrix family。

## 研究順序

1. 先以 synthetic rational cells 測試 uncertain-location Green pairing；
2. 對每個 cell 建立 interval trigonometric/exponential pairings；
3. 以 branch-and-bound 細分最壞 location cells；
4. 建立 exact occupancy-to-operator-family theorem；
5. 再接一個有來源的 argument-principle 或 Turing-style presence
   certificate；
6. 與 upper-envelope Track A 分開發布。

## 停止條件

- 若 uncertain-location family 在 cell 收縮下仍無法通過，輸出 formal
  robust-failure record；
- 若只在使用精確 ordinates 時通過，明確標記為 coordinate-dependent；
- 不得用低高度 prototype 宣稱新的 $\zeta$ 排除；
- 不得把 scalar count accuracy 當成 operator accuracy。

## Track A

可另行完成 v0.7 upper-envelope method no-go：

1. interval-certify upper count profiles；
2. interval-certify tail envelope coefficient；
3. 固定 epigraph semantics；
4. 將 v0.7 abstract positivity轉成 proof-method impossibility theorem。

Track A 與 occupancy Track B 的輸出、flags 與定理名稱必須分離。
