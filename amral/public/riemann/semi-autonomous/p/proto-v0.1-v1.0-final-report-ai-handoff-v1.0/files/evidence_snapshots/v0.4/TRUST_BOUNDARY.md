# Trust Boundary

## E0：有限模型內成立

若序列化非負測度正規化為機率測度，且

$$
W=T+\sum_j\underline N_j\int P\,d\mu_j
+\alpha\int C\,d\nu\succeq0,
$$

則對任何指定離散 primal-feasible $A\succeq0$，

$$
J(A)\ge\alpha.
$$

此外，

$$
\operatorname{supp}\psi\subset[-R,R]
\Longrightarrow
p^m<e^{2R}
$$

是本構造的 exact support cutoff。

## E1：自動重播結構檢查

- 18 個原始 patch 與 288 個 refined patches 都通過 cover audit。
- joint summary 指向的 12 個 witness 路徑與實際檔案集合相同。
- JSON、Python syntax、tests、manifest 與 archive 結構由
  `validate_package.py` 和 `build_release.py` 檢查。
- 所有 `global_rh_certificate` flags 保持 false。

## E2：floating 研究證據

- 126 組 uniform frontier；
- 12 個 joint dual measure optimizations；
- 12 份序列化 witness 的 floating reconstruction；
- $R=16$ 的四級 axis refinement；
- Trudgian published constants 的 floating evaluation；
- $R=10.25$ 以下 named radii 的 segmented prime enumeration；
- tail multiplier 與 Fourier quadrature。

## 尚未建立

1. 沒有 Fourier integral 的 directed-rounding enclosure。
2. 沒有連續軸 supremum 證書；axis grid 仍是離散模型。
3. 沒有完整 288 patch joint dual exhaustion。
4. `count_majorant` 與 tail 尚未封裝成帶完整假設的 theorem objects。
5. histogram 線性插值沒有 interval error。
6. $R=12,14,16$ 沒有實際建出完整 arithmetic matrix。
7. 沒有未知偏軸零點區域的完整 leakage budget。
8. 沒有 argument-principle 或 validated winding zero-presence object。
9. 沒有 local-to-global RH contradiction。
10. 沒有 RH 證明、RH 反證或等價判準證明。

## 關鍵解讀

`at_least_one_searched_patch_blocked=true` 只表示：在指定半徑、
dictionary、離散軸網格、核心點與 floating matrices 中，至少一個已搜尋
子矩形不可能達成 $J(A)<1$。

`full_refined_cover_joint_gate_exhausted=false` 必須保持可見。它表示本節點
沒有對 288 個子矩形逐一做 joint optimization。

粗網格的 $\alpha<1$ 不能解讀成 primal feasible；已重建且 PSD 的
$\alpha>1$ 則足以否決相應有限 primal branch。

