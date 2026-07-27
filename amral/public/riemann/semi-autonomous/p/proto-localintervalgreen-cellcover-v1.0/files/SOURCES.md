# 來源與譜系

## 直接父輸入

- `RH_IntervalGreenKernel_AtomicCertificate_v0.7`
  - `data/parent_v0.7_rational_atomic_witness.json`
  - `data/parent_v0.7_interval_atomic_certificate.json`
- `RH_Occupancy_OperatorFamily_v0.9`
  - `data/parent_v0.9_clamped_radius_certificate.json`
  - `data/parent_v0.9_floating_location_study.json`

`metadata/source_lineage.json` 記錄每個檔案在 v1.0 中的角色。`verify_cell_cover.py` 會檢查父 witness 的 canonical SHA-256 與父證書一致。

## 研究背景稿

本節點延續下列內部研究線索：

- 《從歸心到等變拓樸：RH 合法判定研究的思考方法與方法群》
- 《等變零點組態拓樸學：RH 軌道型分層有效除子半環與正障礙》
- 《等變算術分離：從軌道空間局部化到 Zeta 顯式公式可容許測試函數》
- 《層化零點障礙與局部全域提升：從有理矩形證書到全臨界帶判定》
- 《歸心後的等變拓樸判定域：RH 除子固定點與繞數障礙重構》
- 《顯式公式中的偏軸正障礙：零點側區域負方向、質數側可計算錐與 ZFC 矛盾架構》

這些稿件提供研究語義與方法群背景；v1.0 的可執行證書只依賴包內列出的 JSON 父輸入與程式碼。

## 外部數學依賴

本包使用標準結果：

- 夾持四階微分算子的 Green 表示；
- 指數函數與三角函數的 Taylor 餘項；
- Neumann 級數可逆性判準；
- Schur 補與 $2\times2$ Sylvester 正定判準。

沒有網路資料、數值零點表或外部不可重播黑箱進入嚴格證書。

