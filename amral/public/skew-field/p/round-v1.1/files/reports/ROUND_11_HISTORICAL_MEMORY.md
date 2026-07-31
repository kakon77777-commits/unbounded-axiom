# 第 11 輪歷史施壓記憶審計

第 11 輪最佳化保留所有既有測試曲線，只改變剛體配置，不因終態活動度低而刪除歷史攻擊。

因此，歷史記憶的作用不是固定舊配置，而是持續要求每一條曾施壓曲線至少存在一個合法放置。

目前分類為：

- 持續骨架：第 5、7、8、10、11 輪曲線；
- 暫態施壓：第 6、9 輪曲線。

第 6、9 輪曲線在終態 leave-one-out 中可為零，但仍被保留於十四族容器測試集。

這避免了「因當前冗餘而刪除，之後重新打開舊缺口」的遺忘問題。

形式上：

\[
\mathcal H_n
=
\{\gamma_j:e_j\ge\varepsilon_{\mathrm{attack}},\ j\le n\}
\]

為歷史施壓記憶，而：

\[
\mathcal A_n
=
\{\gamma_j:\ell_j\ge\varepsilon_{\mathrm{active}}\}
\]

為終態活動集。

一般而言：

\[
\mathcal A_n
\subsetneq
\mathcal H_n.
\]

容器更新的約束集應使用 \(\mathcal H_n\)，壓縮與解釋層則可使用 \(\mathcal A_n\)。
