# 歷史施壓記憶與終態活動的雙帳本

## 1. 三個不同量

對第 \(n\) 輪攻擊曲線，記錄：

\[
e_n
=
\mathcal A_{C_{n-1}}(\gamma_n),
\]

\[
\Delta A_n
=
A_n-A_{n-1},
\]

\[
\ell_n
=
\text{curve }\gamma_n
\text{ in final leave-one-out ledger}.
\]

它們分別描述：

- 固定舊容器的攻擊強度；
- 容器回應後的因果面積成本；
- 更新後的終態結構必要性。

## 2. 分類

定義持續比例：

\[
\pi_n=\frac{\ell_n}{e_n}.
\]

若：

\[
e_n\ge\varepsilon_{\mathrm{attack}},
\qquad
\ell_n<\varepsilon_{\mathrm{active}},
\]

則為**暫態施壓曲線**。

若：

\[
e_n\ge\varepsilon_{\mathrm{attack}},
\qquad
\ell_n\ge\varepsilon_{\mathrm{active}},
\]

則為**持續骨架曲線**。

## 3. 第 10 輪結果

\[
e_{10}
=
0.004423629900,
\]

\[
\Delta A_{10}
=
0.002395303600,
\]

\[
\ell_{10}
=
0.002307467379.
\]

因此：

\[
\pi_{10}
=
52.1623%.
\]

Fourier-20 是持續骨架。

第 9 輪攻擊在 \(C_{10}\) 中的 leave-one-out 外露只剩：

\[
0.000044750202,
\]

仍屬暫態施壓類型。

## 4. 記憶原則

容器最佳化不能只保留當前終態活動族。

所有曾滿足：

\[
e_n\ge\varepsilon_{\mathrm{attack}}
\]

的曲線都應保留在歷史測試集，避免容器在壓縮當前活動骨架時重新打開已修補缺口。

因此：

\[
\boxed{
\text{容器狀態}
=
\text{終態活動骨架}
+
\text{歷史施壓記憶}.
}
\]
