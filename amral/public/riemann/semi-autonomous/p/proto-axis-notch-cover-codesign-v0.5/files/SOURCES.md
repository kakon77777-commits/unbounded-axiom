# Sources and Lineage

## 直接父節點

本節點的數值輸入來自
`RH_Support_Prime_Dual_Frontier_v0.4`：

- `outputs/joint_dual_summary.json`
- `outputs/axis_refinement.json`
- `outputs/uniform_frontier.json`
- `outputs/prime_cost.json`
- `metadata/handoff.json`
- `outputs/witnesses/*.witness.json`

本套件將上述必要 artifacts 保存於 `data/`，使 peak atlas 與 v0.5
reconstruction 不依賴工作區外部狀態。

## 外部基礎文獻

1. R. E. A. C. Paley and N. Wiener, *Fourier Transforms in the Complex
   Domain*, AMS Colloquium Publications 19, original 1934; AMS reprint,
   DOI `10.1090/coll/019`.
   本節點只用它作為下一節點 compact-support / entire-function framework
   的歷史來源，沒有引用其中定理完成解析轉移。
2. Louis de Branges, *Hilbert Spaces of Entire Functions*, Prentice-Hall,
   1968.
   本節點只把 de Branges/reproducing-kernel formulation 列為 v0.6
   候選語言，沒有聲稱目前 finite model 已滿足其完整假設。
3. Timothy S. Trudgian, “An improved upper bound for the argument of the
   Riemann zeta-function on the critical line II,” *Journal of Number
   Theory* 134 (2014), 280–292, DOI
   `10.1016/j.jnt.2013.07.017`.
   tail prototype 沿用父節點的 published floating $S(T)$ constants。

## 未使用

- 沒有使用已知 zeta zero ordinates table。
- 沒有從網頁或資料庫匯入新的數值零點。
- 沒有把外部文獻當作本套件 floating computations 的獨立驗證。
