# 駐定作用一體多面 v1.0：論文與驗證資料包

## 內容

- `00_paper`：完整 Markdown 論文
- `01_code`：Python 驗證程式
- `02_data`：數值總表、Hessian 掃描與作用量曲率資料
- `03_figures`：全部驗證圖
- `MANIFEST.csv`：檔案大小與 SHA-256

## 核心驗證

1. 離散作用量駐定解與解析 Euler–Lagrange 解一致。
2. 動能與位能變分在駐定路徑上相互抵消。
3. $T<\pi/\omega$ 時作用量為局部最小。
4. $T>\pi/\omega$ 時駐定路徑轉為鞍點。
5. 驗證「駐定—局部動力—變分抵消」可作同一系統的不同表徵。

## 執行

```bash
python stationary_action_basic_verification.py
```

需要：

- Python 3
- NumPy
- pandas
- Matplotlib
