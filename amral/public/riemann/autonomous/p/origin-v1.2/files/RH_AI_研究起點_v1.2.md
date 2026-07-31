# RH AI 研究起點 v1.2
## 自適應腔室延拓與 $10^{-9}$ 有限維廣義正裕度

**日期：** 2026-07-23  
**作者標記：** 原始研究方向 Neo.K；研究重構與工程實作 Aletheia（GPT-5.6 Thinking）  
**性質：** 非證明研究工程包

---

# 1. 本版接續內容

v1.1 已完成：

$$
\text{固定網格搜尋}
\rightarrow
\text{十三維候選}
\rightarrow
10^{-5}\text{ 嚴格正裕度}.
$$

v1.2 進一步完成：

$$
\text{局部自適應延拓}
\rightarrow
\text{prime-power 邊界追蹤}
\rightarrow
\text{十五維近臨界候選}
\rightarrow
10^{-9}\text{ 嚴格正裕度}.
$$

---

# 2. 固定候選

$$
\boxed{
h=\frac{87}{400},
\qquad
d=\frac{117}{512},
\qquad N=15
}.
$$

探索性廣義譜底約為：

$$
1.32\times10^{-9}.
$$

候選距離 lag-$1$ 的 $n=3$ 活化邊界：

$$
\log3=d+4h
$$

只剩約：

$$
9.67\times10^{-5}.
$$

---

# 3. 嚴格結果

完整枚舉所有支撐內的 $24$ 個 prime powers，建立十五維真實 Weil 區間矩陣與精確 Gram 矩陣。

純有理驗證器證明：

$$
\boxed{
Q(c)>10^{-9}c^TGc
\qquad
\forall c\ne0
}.
$$

這只證明固定十五維子空間中的正性，不能推出 RH。

---

# 4. 精度工程

本版新增：

1. Binet／digamma 的 Euler 常數有符號餘項區間；
2. $S_3,S_5,S_7,S_8$ 的有理二段尾延拓；
3. prime-power 活化邊界追蹤；
4. 自適應座標延拓路徑保存；
5. $10^{-32}$ 網格有理中心；
6. exact $LDL^T$ 廣義正裕度驗證。

矩陣最大列誤差約為：

$$
2.01\times10^{-12}.
$$

---

# 5. 下一節點

```text
RH-W-10-PRIME-BOUNDARY-LOCAL-MODE
```

不再繼續盲目壓低譜值，而是固定：

$$
\log3=d+4h
$$

附近的邊界前、邊界上與邊界後三個狀態，研究新進場的 prime-$3$ 矩陣塊對最低模態的單側作用。
