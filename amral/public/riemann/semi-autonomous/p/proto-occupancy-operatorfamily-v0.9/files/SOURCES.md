# Sources

## 1. 直接父節點

- `RH_ZeroCount_Semantics_Bridge_v0.8`
  - 提供 count upper／lower 的型別修正；
  - 固定本輪 next node；
  - 禁止 scalar count lower 轉成任意 measure operator mass。

- `RH_IntervalGreenKernel_AtomicCertificate_v0.7`
  - 提供固定位置的 abstract continuous interval certificate；
  - 提供 rational atomic witness；
  - 提供 clamped $D^4$ Green、structural projection 與 low-rank Schur
    parent theorem。

本套件內含下列 bytes-locked copies：

- `data/parent_v0.7_rational_atomic_witness.json`
- `data/parent_v0.7_interval_atomic_certificate.json`

## 2. 本輪自含數學

以下推論由套件內程式與本文直接重建：

- Dirichlet Green kernel

  $$
  K(s,t)=\min(s,t)-st;
  $$

- Woodbury identity；
- finite-rank Schur complement；
- $2\times2$ Sylvester criterion；
- occupancy selection PSD surplus argument；
- 兩次 Dirichlet Poincaré inequality；
- rank-one operator difference bound。

## 3. 未使用的來源

本輪沒有使用實際 $\zeta$ zero ordinate tables，也沒有把已驗證低高度
資料當成 unresolved target。沒有新增 argument-principle、Turing method
或 explicit-formula admissibility 的外部定理依賴。

## 4. Source status

| source | status | role |
| --- | --- | --- |
| v0.8 handoff | inherited and locally available | semantic routing |
| v0.7 witness | bytes locked | parent coordinates and weights |
| v0.7 interval certificate | bytes locked | conditional abstract positivity |
| synthetic occupancy axioms | explicit synthetic input | exact prototype only |
| actual zeta occupancy source | absent | open gap |

