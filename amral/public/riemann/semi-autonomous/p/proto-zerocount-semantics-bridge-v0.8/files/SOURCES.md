# Sources

## External mathematical sources

1. T. S. Trudgian, “An improved upper bound for the argument of the
   Riemann zeta-function on the critical line II,” *Journal of Number
   Theory* 134 (2014), 280–292.

   - [arXiv:1208.5846](https://arxiv.org/abs/1208.5846)
   - [DOI: 10.1016/j.jnt.2013.07.017](https://doi.org/10.1016/j.jnt.2013.07.017)

   arXiv abstract states

   $$
   |S(T)|
   \le
   0.111\log T
   +
   0.275\log\log T
   +
   2.450
   $$

   for $T\ge e$. v0.4–v0.7 inherited the slightly larger floating profile

   $$
   0.112\log T
   +
   0.278\log\log T
   +
   2.510.
   $$

   v0.8 preserves that inherited conservative profile for lineage
   comparability, but does not mark its exact version provenance or endpoint
   use as certified.

2. NIST Digital Library of Mathematical Functions, §25.10, “Zeros”:

   - [DLMF §25.10](https://dlmf.nist.gov/25.10)
   - [Riemann–Siegel theta definition](https://dlmf.nist.gov/25.10.E2)

   Used for notation and the Riemann–Siegel theta context. DLMF states that
   $N(T)$ counts zeros in the critical strip and records the standard theta
   function used for zero computation.

3. D. J. Platt and T. S. Trudgian, “The Riemann hypothesis is true up to
   $3\cdot10^{12}$,” *Bulletin of the London Mathematical Society* 53
   (2021), 792–797.

   - [arXiv:2004.09765](https://arxiv.org/abs/2004.09765)
   - [DOI: 10.1112/blms.12460](https://doi.org/10.1112/blms.12460)

   Used only to classify the height-$20.4$ patch as a prototype rather than an
   unresolved actual $\zeta$ target.

## Parent research artifacts

The following local packages are the direct lineage:

1. `RH_Banded_MultiTest_Cover_Certificates_v0.1`
2. `RH_PSD_Gram_Banded_Global_Dominance_v0.2`
3. `RH_Axis_Target_Dual_Obstruction_v0.3`
4. `RH_Support_Prime_Dual_Frontier_v0.4`
5. `RH_Axis_Notch_Cover_Codesign_v0.5`
6. `RH_PaleyWiener_AxisCore_Extremal_v0.6`
7. `RH_IntervalGreenKernel_AtomicCertificate_v0.7`

The semantic reconstruction specifically uses:

- v0.1 `METHOD.md` and internal paper, where axis energy is called a proxy;
- v0.2 `METHOD.md`, where count upper multiplies band supremum;
- v0.3 `METHOD.md`, where the dual lower-bounds the epigraph objective;
- v0.6 `THEORY.md` and paper, where the continuous measure dual is defined;
- v0.7 `coefficient_orientation_audit.json` and
  `orientation_stress_test.json`.

## Uploaded conceptual sources

The attached internal draft

`顯式公式中的偏軸正障礙_零點側區域負方向質數側可計算錐與ZFC矛盾架構_v0.1_內部稿(1).md`

already identifies the non-target zero contribution as an upper leakage
problem and writes a majorant-measure prototype. v0.8 sharpens that interface
by separating scalar upper envelopes from operator lower bounds.

## Software

- Python standard library
- NumPy
- SciPy

No external zero ordinate table is used in the v0.8 optimization.
