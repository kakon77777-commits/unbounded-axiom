# RH Support–Prime Dual Frontier v0.4

本套件承接 v0.3，實作分帶、多測試函數與覆蓋式 dual certificate
family。主要結果是：在目前 compact bump dictionary 中，抽樣半徑
$R=10.25,12,14,16$ 都至少有一個困難子矩形被可重建的
$\alpha_{\rm safe}>1$ witness 阻擋；$R=16$ 的粗軸網格
$\alpha<1$ 是假逃逸。

核心數字：

- uniform frontier：126 組幾何；
- cover：18 個原始 patch，細分為 288 個子矩形；
- joint dual：12 個困難子矩形；
- $R=16$ 軸步長 $0.25\to0.025$：
  $\alpha:0.9853\to1.1923$；
- 12 份 witness 全部 floating 重建並保持 PSD；
- $R=10.25$ 實枚舉 $41{,}141{,}456$ 個質數；
- $R=16$ 截斷為 $78{,}962{,}960{,}182{,}680$。

自主研究決策：停止 support-only 暴力擴張；下一節點轉向
`RH_Axis_Notch_Cover_Codesign_v0.5`。

入口：

- 主研究稿：
  `RH支撐質數對偶前沿_軸網格假逃逸與頻譜缺口轉向_v0.4_半AI自主研究稿.md`
- 方法：`METHOD.md`
- 結果：`RESULTS.md`
- 信任邊界：`TRUST_BOUNDARY.md`
- 重播：`REPLAY.md`
- 下一節點：`NEXT_NODE_AXIS_NOTCH_CODESIGN.md`
- 機器可讀 claim/GAP：`metadata/`

本套件不是 RH 證明、不是 RH 反證，也不是連續解析問題的 interval
certificate。

