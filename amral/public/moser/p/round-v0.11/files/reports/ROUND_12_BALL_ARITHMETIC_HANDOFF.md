# 第 12 輪 Arb／Ball Arithmetic 交接接口

## 必須重算的物件

1. `data/exact_contact_boundaries.json`
2. `data/special_branch_interval_certificate.json`
3. `data/phase_derivative_box_certificate.json`
4. `data/stationary_root_boxes.json`
5. `data/boundary_neighborhood_audit.json`

## 通過標準

### 特殊分支

$$
\inf(s_{120}-s_{270})>0.
$$

### 事件控制

$$
\inf s_{270}-\sup s_0>0.
$$

### 導數子盒

對每個不含根盒的 $X$：

$$
0\notin s'(X).
$$

### 根盒

對每個 $X_r$：

$$
N(X_r)\subset\operatorname{int}X_r.
$$

### 邊界盒

除 $270^\circ$ 外，每個可能形成局部極小的邊界鄰域 $B_k$：

$$
\inf s(B_k)>\sup s_{270}.
$$

## 成功後的聲明

只能聲明固定十進位平滑候選在完整相位圓上的合同尺度被嚴格包住，並高於固定十進位五連桿事件控制。

仍不能直接推出新的 Moser 面積下界。
