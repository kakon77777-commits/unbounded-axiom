# RH Equivariant Arithmetic Obstruction Integration v1.0

這是 `CASE-0001-RH-WEIL-BATCH01` 的等變算術障礙整合分支，收錄六篇理論稿、六個原始工程 ZIP、可重播驗證結果，以及 AI 自主數學平台所需的案例索引。

本包不證明或反證黎曼猜想。

## 最重要的整合結論

目前已嚴格驗證：同一個明確緊支撐測試函數可以同時滿足：

$$
\sup_{w\in K}2\operatorname{Re}(G(w)^2)<0
$$

與：

$$
Q_{\mathrm{arith}}(\psi)>0.
$$

但這只是一個單一函數、單一合成矩形上的交集證書。它不是算術矩陣半正定，也沒有控制目標外全部零點。

現有零點側洩漏預算顯示，第一個已知臨界線零點的正貢獻約為目標負裕量的 $2387.591$ 倍，所以當前單目標函數不能產生完整零點側負值。

## 閱讀順序

1. `RH_等變算術障礙整合總論_v1.0.md`
2. `INTEGRATION_AUDIT.md`
3. `metadata/gap_map.json`
4. `metadata/dependency_graph.json`
5. `metadata/certificate_index.json`
6. `handoff/next_experiment_spec.md`

## 如何驗證

整包檔案雜湊位於：

`validation/checksums.sha256`

本次重播結果位於：

`validation/test_report.json`

原始來源未被修改，完整保留於：

- `sources/theory/`
- `sources/packages/`

## 目前未完成

- 目標矩形外全部零點貢獻的無條件上界；
- 對任意正則有理矩形的統一測試函數生成器；
- 結構性算術正錐或一般 PSD 證書；
- 顯式公式與區間證書的證明助理形式化；
- RH。

## 下一個 AI 應做什麼

執行 `handoff/next_experiment_spec.md` 所定義的「全域支配證書最佳化器 v0.2」。主成功指標不是目標窗負值，而是：

$$
\Delta_K
=
c_K
-
E_{\mathrm{axis}}
-
E_{\mathrm{mid}}
-
E_{\mathrm{tail}}
-
E_{\mathrm{unknown}}
>0,
$$

並同時具有：

$$
Q_{\mathrm{arith}}\ge\delta>0.
$$

除非兩者均以嚴格證書成立，不得標記為已閉合 GAP。

