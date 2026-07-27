# Next Node: Local Interval Green Cell Cover v0.10

## 節點

`RH-LocalIntervalGreen-CellCover-20260725-v0.10`

## 首要決策

v0.9 已證明：

- occupancy 量詞架構合法；
- exact cover family 可消除 interval dependency；
- 全域 Poincaré budget 只能給約 $10^{-15}$ 尺度；
- floating local study 的轉折在約 $10^{-2}$ 尺度。

所以下一步不再增加 scalar count precision，也不直接接未解 $\zeta$ 高度。
先改善 local Green enclosure。

## Work package `WP10-GREEN-LOCAL`

1. 對 axis density

   $$
   f_x(t)=\cos(xt)
   $$

   建立 cell-valued exponential/trigonometric enclosure。

2. 對 projected Green pairings

   $$
   \langle p_x,p_y\rangle
   $$

   建立一階與二階位置導數的 directed interval bounds。

3. 保留 low negative rank，以 interval Schur family 判定，不先形成
   full operator interval。

4. 使用 adaptive cell cover，測試半徑梯級

   $$
   10^{-8},\ 10^{-6},\ 10^{-4},\ 10^{-3}.
   $$

5. 每個失敗必須區分：

   - actual point counterexample；
   - interval dependency inconclusive；
   - Neumann inverse enclosure failure；
   - Sylvester lower-bound failure；
   - resource stop。

## Work package `WP10-OCC-SOURCE`

與 kernel 工程分離，只建立 presence certificate schema：

- endpoint nonzero certificate；
- argument-principle winding count；
- Turing-style zero-count interval；
- multiplicity convention；
- source hash；
- resolved-height versus unresolved-height label。

在 `WP10-GREEN-LOCAL` 未能處理 macroscopic cells 前，不把真實 ordinate
tables 當成 global RH target。

## Separate Track A

upper-envelope method no-go 仍是獨立節點：

- upper count theorem direction；
- tail upper coefficient；
- epigraph semantics；
- v0.7 abstract witness 的 method-level interpretation。

Track A 不得與 actual occupancy flags 混寫。

## 停止條件

- 若 local interval family 在 $10^{-8}$ 即無法通過，輸出 formal
  enclosure-failure ledger；
- 若只有精確 coordinates 能通過，標記 `coordinate-dependent`；
- 若 floating failure 有 exact interval point witness，另開
  counterexample node；
- 所有 global RH flags 保持 false。

