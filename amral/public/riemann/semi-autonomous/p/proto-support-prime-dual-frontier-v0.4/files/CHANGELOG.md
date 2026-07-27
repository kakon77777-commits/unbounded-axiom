# Changelog

## v0.4 — 2026-07-24

- 建立 126 組 support/density/width uniform frontier。
- 將 18 patch 細分為 288 子矩形。
- 實作五帶 axis measure 與多點 core measure joint dual。
- 匯出並重建 12 份 floating sparse-measure witnesses。
- 識別並重播 $R=16$ 的 coarse-axis false escape。
- 將 axis active search 改為 transform-based，避免 dense outer-matrix
  記憶體爆炸。
- 改用 Trudgian published constants
  $0.112,0.278,2.510$。
- 實作 segmented prime-power log histogram。
- 實際 benchmark 到 $R=10.25$。
- 設定 dual-gated primal stop rule。
- 決定下一節點轉向 axis-notch cover co-design。
- 保持所有 global RH certificate flags 為 false。

