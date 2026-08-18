# Excel Log-Coordinate Function Stress Test

Open `excel_log_coordinate_function_stress_test.xlsx` in Microsoft Excel and recalculate.

Sheets:
- Function_Map — mapping between ordinary operations and log/additive forms.
- Real_Log — multiplication, division, powers.
- Finite_Affine — finite n/2 vs 3n+1 partial-map test.
- Physics — π powers, roots, Stefan–Boltzmann form, log-sum-exp/log-diff-exp.
- Complex_Phase — Excel complex-number functions and near-cancellation.
- DFT — finite DFT via SUMPRODUCT/COS/SIN.
- Summary — interpretation.

Important: ordinary Excel arithmetic is finite-precision floating point. Exact symbolic
relations involving π or roots of unity are therefore deliberately expected to leave tiny
numeric residuals unless a separate symbolic/exact layer is added.
