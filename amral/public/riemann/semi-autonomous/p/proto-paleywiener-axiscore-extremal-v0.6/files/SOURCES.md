# Sources and Lineage

## Parent node

直接父節點：

`RH_Axis_Notch_Cover_Codesign_v0.5`

保存輸入：

- `data/parent_handoff.json`
- `data/parent_experiment_summary.json`
- `data/parent_peak_atlas.json`
- `data/parent_lift_joint.json`
- `data/parent_geometry_joint.json`
- `data/parent_joint_verification.json`

## External primary sources

1. R. E. A. C. Paley and N. Wiener,
   *Fourier Transforms in the Complex Domain*,
   AMS Colloquium Publications 19, 1934,
   DOI `10.1090/coll/019`,
   <https://bookstore.ams.org/coll-19>.
   用於 compact support、exponential type 與 entire-function framework。
2. N. Aronszajn, “Theory of Reproducing Kernels,”
   *Transactions of the American Mathematical Society* 68 (1950),
   337–404,
   DOI `10.1090/S0002-9947-1950-0051437-7`.
   用於 RKHS/Riesz representer 的標準背景。
3. Louis de Branges, *Hilbert Spaces of Entire Functions*,
   Prentice-Hall, 1968.
   用於 entire-function Hilbert-space 語境；本節點不是在宣稱所定義空間已
   直接等同某個特定 de Branges space。
4. Timothy S. Trudgian,
   “An improved upper bound for the argument of the Riemann zeta-function
   on the critical line II,”
   *Journal of Number Theory* 134 (2014), 280–292,
   DOI `10.1016/j.jnt.2013.07.017`.
   tail/count floating profile 沿用父研究鏈；theorem-object transfer 尚未完成。

## Internal derivations

以下結果在本節點直接推導：

- trace-class weak duality；
- one-axis/one-core rank-two formula；
- clamped Green kernel；
- structural finite-rank projection；
- atomic Woodbury–Schur reduction。

## Not used

- 沒有使用 known zeta zero ordinates。
- 沒有匯入外部 numerical zero table。
- 沒有使用外部宣稱替代本套件的 kernel reconstruction。
