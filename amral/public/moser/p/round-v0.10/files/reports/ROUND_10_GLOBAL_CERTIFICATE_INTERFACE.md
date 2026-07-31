# 第 10 輪全域相位證書接口

## 已生成的機讀帳本

- `data/phase_contact_intervals.csv`
- `data/round10_summary.json`
- `data/round10_global_exclusion_audit.json`

## 每個區間包含

$$
(
I_k,
\Sigma_k,
\min s'(I_k),
\max s'(I_k),
\{\phi:s'(\phi)=0\},
\min_{I_k}s
).
$$

## 下一層嚴格化

1. 用區間算術包住每個接觸切換；
2. 將 PCHIP 座標替換成任意精度積分或可證積分包絡；
3. 對固定簽章公式建立 $s'(\phi)$ 區間；
4. 對光滑駐點做 interval Newton；
5. 對 $120^\circ$ 與 $270^\circ$ 建立專用差值包絡。

## 最終目標

產生可機讀證書：

$$
\forall \phi\in[0,2\pi),
\qquad
s(\phi)\ge s(3\pi/2).
$$

本輪尚未聲稱完成此嚴格證書。
