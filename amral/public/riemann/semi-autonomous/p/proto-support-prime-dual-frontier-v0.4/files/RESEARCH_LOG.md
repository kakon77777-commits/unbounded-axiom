# Research Log

日期：2026-07-24

## 起點

承接 v0.3：$R=3$ finite surrogate 被 dual lower bound $2$ 否決。原
handoff 建議建立 support–prime frontier，採用分帶、多測試函數與
覆蓋式證書族。

## 本輪決策軌跡

1. 建立 126 組 uniform frontier。
2. 發現中心逃逸早於 patch 多點逃逸，故中心不足以作通過判定。
3. 將 18 patch 細分為 288 子矩形。
4. 對困難子矩形共同最佳化五帶軸測度與核心測度。
5. 在粗軸步長 $0.25$ 下，$R=16$ 曾出現 $\alpha<1$。
6. 對相應 Gram direction 做 dense axis audit，發現 objective 回升到約
   $3.05$，判定存在漏峰。
7. 重構 cutting-plane，保存 axis transforms 而非全部 outer matrices，
   使 $0.05$ 與 $0.025$ 網格可運行。
8. 細化證實

   $$
   0.9853\to1.1923,
   $$

   粗網格逃逸為假。
9. 重跑四個半徑 joint dual；全部至少有一個安全阻擋。
10. 根據 dual gate，不啟動高成本 primal branch。
11. 以 segmented sieve 在 $R=10.25$ 實枚舉 4,114 萬個質數。
12. 對比 $R=16$ 的約 2.47 兆質數成本代理，決定停止 support-only
    擴張。
13. 下一節點轉向 axis-notch/dictionary/cover co-design。

## 被否決的錯誤推論

- 「中心 threshold 小於 $1$，所以整個 patch 可行。」
- 「uniform measure 小於 $1$，所以 full dual optimum 小於 $1$。」
- 「粗軸 grid 找不到峰，所以 axis budget 已通過。」
- 「log histogram 降低矩陣更新，所以不再需要枚舉質數。」
- 「finite dual obstruction 是 RH 的反證。」

## 保留的開放方向

最有價值的資訊不是半徑本身，而是 joint witness 的 sparse active axis
supports。它們指出目前 dictionary 的能量峰在哪裡，應作為 v0.5 notch
constraints 的資料來源。

