# Sources and Lineage

## Parent node

直接父節點：

`RH_PaleyWiener_AxisCore_Extremal_v0.6`

保存輸入：

- `data/rational_atomic_witness_v0.6.json`
- `data/parent_handoff_v0.6.json`

## Mathematical sources

1. R. E. A. C. Paley and N. Wiener,
   *Fourier Transforms in the Complex Domain*,
   AMS Colloquium Publications $19$, $1934$,
   DOI `10.1090/coll/019`,
   <https://bookstore.ams.org/coll-19>.
   用於 compact support 與 entire Fourier-transform framework。
2. N. Aronszajn,
   “Theory of Reproducing Kernels,”
   *Transactions of the American Mathematical Society* $68$,
   $1950$, pp. $337$–$404$,
   DOI `10.1090/S0002-9947-1950-0051437-7`,
   <https://doi.org/10.1090/S0002-9947-1950-0051437-7>.
   用於 reproducing-kernel 與 representer 背景。
3. Timothy S. Trudgian,
   “An improved upper bound for the argument of the Riemann zeta-function
   on the critical line II,”
   *Journal of Number Theory* $134$, $2014$, pp. $280$–$292$,
   DOI `10.1016/j.jnt.2013.07.017`,
   <https://openresearch-repository.anu.edu.au/items/2484efc1-7e1b-4a99-821a-ffb0bcbe5697>.
   published abstract 所列的 inherited bound 為

   $$
   |S(T)|
   \leq
   0.112\log T
   +0.278\log\log T
   +2.510
   $$

   對 $T\geq e$。

## Software specifications

1. Python `decimal` contexts 與 directed rounding modes：
   <https://docs.python.org/3.11/library/decimal.html>.
2. SciPy `loggamma`：
   <https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.loggamma.html>.
   只用於 coefficient orientation 的 floating diagnostic。
3. NumPy linear solve：
   <https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html>.
   只產生 rational inverse／solution candidates；證明由 directed
   residual enclosure 完成。

## Internal derivations

本節點直接推導與實作：

- exponential clamped Green representer；
- rational moment recurrence；
- Machin/Taylor transcendental enclosure；
- two-sided Green orientation intersection；
- Neumann family regularity certificate；
- square-root-free $B^{-1}-Q$ Schur reduction；
- coefficient upper/lower orientation audit。

## Not used

- 沒有使用 known zeta zero ordinates。
- 沒有匯入外部 zero table。
- 沒有使用外部 interval arithmetic package。
- ordinary floating special functions 沒有提供 Layer A 證明端點。
