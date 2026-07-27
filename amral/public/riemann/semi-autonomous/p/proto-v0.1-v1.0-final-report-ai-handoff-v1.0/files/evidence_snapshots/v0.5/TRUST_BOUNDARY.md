# Trust Boundary

## E0：有限模型內的 exact statement

若 notch 只以齊次線性約束把父空間 $V$ 縮成 $V'\subseteq V$，則

$$
\mathcal F(V')\subseteq\mathcal F(V),
$$

所以對同一最小化目標

$$
\inf_{\mathcal F(V)}J
\le
\inf_{\mathcal F(V')}J.
$$

因此子空間 notch 不能改善已在完整父空間上求得的 primal optimum。

同樣地，在指定有限 conic model 中，若重建的

$$
W=B_\mu+\alpha C_\nu\succeq0,
$$

則對每個指定 finite primal feasible $A$ 有 $J(A)\ge\alpha$。

## E1：自動結構檢查

- 12 份父 witness 都被 peak-atlas 程式讀取。
- notch screen 包含兩個半徑與每半徑 10 組 code。
- geometry screen 恰有 27 組。
- 四個保存的 joint dual objects 都通過正規化 measure reconstruction。
- Python syntax、tests、JSON、math delimiters、metadata flags 與 release manifest
  由 `validate_package.py` 檢查。
- 所有 `global_rh_certificate` flags 保持 false。

## E2：floating 研究證據

- KDE peak atlas。
- Fourier quadrature 與 constrained whitening。
- external spectral-slope lift 與解析二階導數。
- uniform/core measure optimization。
- joint dual measure optimization。
- dense-axis / 4,941-point core complementary rank-one audit。
- floating eigenvalue reconstruction。

## 尚未建立

1. 沒有 Fourier quadrature 的 directed-rounding enclosure。
2. 沒有連續軸 supremum 證書。
3. 沒有證明目前的 lift 或 polynomial-bump family 在所有維度都必然失敗。
4. 沒有完整 288 refined patches 的新字典 joint exhaustion。
5. 沒有 theorem-backed、interval-evaluated zero-count 與 tail objects。
6. 沒有 arithmetic histogram interpolation error enclosure。
7. 沒有未知偏軸零點區域的完整 leakage budget。
8. 沒有 argument-principle zero-presence 或 validated winding object。
9. 沒有從有限 obstruction 到連續 Paley–Wiener inequality 的轉移。
10. 沒有 local-to-global RH closure、RH 證明或 RH 反證。

## 關鍵解讀

E0 單調性排除的是「在同一父空間內只加齊次 notch constraints」這個策略，
不是排除所有頻譜缺口設計。外部 lift 確實避開了 E0 排除，但本節點只測試
一個具體 family，結果顯示改善不足且開始飽和。

安全 dual 下界大於 $1$ 足以否決相應 finite primal branch；反之，若未來
找到低於 $1$ 的 dual value，也只代表已搜尋 witness 未阻擋，不能單獨證明
primal feasible，更不能推出 RH。
