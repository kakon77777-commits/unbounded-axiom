# RH-W-08 工程包 v0.1

本包完成第一條「搜尋 → 嚴格細化 → exact 證書」的 RH Weil 腔室流水線。

## 主要結果

在固定網格掃描 122 個 translated cubic B-spline 腔室後，選出：

$$
h=\frac3{20},\qquad d=\frac9{40},\qquad N=13.
$$

完整 prime-power 區間重建與純有理驗證器證明：

$$
Q(c)>10^{-5}c^TGc
$$

對這個固定十三維空間中的所有非零係數向量成立。

這只是有限維正性，不構成 RH 證明。

## 檔案

- `01_RH-W-08_腔室搜尋與嚴格細化_v0.1.md`：主研究文件。
- `02_RH-W-08_阿基米德尾界精化_v0.1.md`：尾界改良推導。
- `search_chambers.py`：浮點探索器，只能產生候選。
- `chamber_search_results.csv/json`：122 個腔室排序。
- `refine_selected_chamber.py`：選定候選的嚴格區間重建器。
- `arch_tail_refinement.py`：signed derivative tail compiler。
- `refined_13x13_interval.json`：完整十三維區間證書。
- `verify_refined_certificate.py`：只使用 `int` 與 `Fraction` 的 exact verifier。
- `refinement_attempt_old_tail_inconclusive.json`：舊尾界失敗記錄。
- `RH-W-08_subgaps_v0.1.csv`：GAP 狀態。

## 重播

```bash
python search_chambers.py
python refine_selected_chamber.py
python verify_refined_certificate.py
```

探索器需要 NumPy、SciPy；exact verifier 不需要浮點數或第三方數值套件。

## 來源定位

本工程使用經典 Riemann–Weil 顯式公式與 Weil 正性框架。當代相關背景包括：

- Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096.
- Akiva Groskin, *A finite Guinand–Weil dictionary and archimedean tail order for the truncated Weil quadratic form*, arXiv:2607.02828.
- Enrico Bombieri, *Problems of the Millennium: The Riemann Hypothesis*, Clay Mathematics Institute.

本包的搜尋網格、B-spline 支撐腔室編譯、signed tail refinement 與證書工作流屬於本研究計畫的工程組裝；不宣稱上述來源支持本包的具體十三維數值。
