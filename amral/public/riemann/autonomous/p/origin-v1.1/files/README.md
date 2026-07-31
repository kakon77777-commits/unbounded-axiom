# RH AI 研究起點 v1.1
## 自動搜尋與嚴格細化

本整合包收錄 `RH-W-07` 與 `RH-W-08`。

目前工程鏈已從：

$$
\text{固定多素數腔室}
$$

推進到：

$$
\boxed{
\text{有限網格搜尋}
\rightarrow
\text{廣義譜排序}
\rightarrow
\text{候選嚴格重建}
\rightarrow
\text{尾界自動升級}
\rightarrow
\text{純有理證書}
}
$$

## 本版核心成果

固定搜尋網格共掃描：

$$
122
$$

個 translated cubic B-spline 腔室。

排名第一的候選為：

$$
h=\frac3{20},
\qquad
d=\frac9{40},
\qquad
N=13.
$$

完整 prime-power 枚舉至 $27$，並由 exact verifier 證明：

$$
Q(c)>10^{-5}c^TGc
$$

對該固定十三維空間中的所有非零 $c$ 成立。

這只是有限維正性，不構成 RH 證明。

## 文件順序

1. `01_RH-W-07_多素數支撐腔室編譯器_v0.1.md`
2. `02_RH-W-07_證書架構與GAP更新_v0.1.md`
3. `03_RH-W-08_腔室搜尋與嚴格細化_v0.1.md`
4. `04_RH-W-08_阿基米德尾界精化_v0.1.md`

完整程式、區間矩陣與重播腳本位於獨立的 `RH_W_08_工程包_v0.1`。

## 下一節點

$$
\boxed{
\texttt{RH-W-09-ADAPTIVE-CHAMBER-CONTINUATION}
}
$$

下一輪將由目前最小候選出發，進行局部參數 continuation、prime-power 活化邊界細分與最低模態追蹤。
