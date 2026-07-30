# RH-W-10 工程包 v0.1

本包研究 lag-$1$ 的 prime-$3$ 支撐邊界

$$
\log3=d+4h.
$$

主要成果：

1. prime-$3$ 新矩陣元素以
   $$
   (d+4h-\log3)_+^7
   $$
   軟啟動；
2. 邊界正則性為 $C^6$、非 $C^7$；
3. 新區塊對任意方向的符號由相鄰相關決定；
4. 邊界前後兩個有理十五維腔室都取得
   $$
   Q(c)>10^{-9}c^TGc
   $$
   的純有理驗證；
5. 局部掃描未觀察到 avoided crossing；
6. prime-$3$ 剛進場的直接量級約 $10^{-28}$，不足以解釋 $10^{-9}$ 的近零譜底。

## 主要文件

- `01_RH-W-10_素數邊界局部模態_v0.1.md`
- `02_RH-W-10_證書與局部掃描審計_v0.1.md`
- `prime3_soft_activation_certificate.json`
- `theta_minus_15x15_interval.json`
- `theta_plus_15x15_interval.json`
- `local_boundary_exploration.csv`

## 驗證

```bash
python verify_prime3_activation.py
python verify_theta_minus.py
python verify_theta_plus.py
```

## 範圍

這是固定有限維字典中的局部結構與數值證書，不是 RH 證明。
