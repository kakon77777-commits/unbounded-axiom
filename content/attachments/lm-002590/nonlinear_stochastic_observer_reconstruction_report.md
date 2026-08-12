# Nonlinear + Stochastic Observer-Only Reconstruction

## Setup
Hidden classical state:
z=(x,y,vx,vy)

Dynamics:
anisotropic 2D harmonic oscillator with wx=1.1, wy=1.7.

The hidden state is never used by the reconstruction routine.
It is retained only for final scoring.

Each Embedded AI sees a nonlinear stochastic channel y_i=h_i(z)+epsilon_i.
One channel (O5) is biased in corrupted trials.

## Exact individual ambiguity
O6 observes:
h6(z)=(x^2+y^2, vx^2+vy^2).

Therefore h6(z)=h6(-z) exactly.

Demo measurement mismatch:
0.000e+00

Yet state distance:
1.99249

Thus individual non-globality is now nonlinear many-to-one ambiguity, not linear rank deficiency.

## Trials
Total: 96
Noise sigma: 0, 0.005, 0.02, 0.05
Clean and corrupted conditions.

## Aggregate results

|   sigma | corrupt   |   mean_state_one |   mean_state_hist_ls |   mean_state_hist_rob |   mean_state_repaired |   median_E_repaired |   median_action_repaired |   suspect_accuracy |
|--------:|:----------|-----------------:|---------------------:|----------------------:|----------------------:|--------------------:|-------------------------:|-------------------:|
|   0     | False     |       4.3008e-14 |          6.04007e-13 |            3.6419e-12 |           9.37012e-12 |         6.00779e-16 |              7.32904e-16 |                  1 |
|   0     | True      |       0.130458   |          0.052179    |            0.009904   |           8.13527e-13 |         1.56594e-16 |              4.64994e-16 |                  1 |
|   0.005 | False     |       0.140728   |          0.00283969  |            0.00283637 |           0.00283637  |         0.000791373 |              0.00138343  |                  1 |
|   0.005 | True      |       0.22825    |          0.0647033   |            0.0130428  |           0.00250576  |         0.000796338 |              0.000889958 |                  1 |
|   0.02  | False     |       0.0269082  |          0.0122336   |            0.0120927  |           0.0120927   |         0.00325204  |              0.00523102  |                  1 |
|   0.02  | True      |       0.160277   |          0.0725927   |            0.0177147  |           0.011646    |         0.00381808  |              0.00652732  |                  1 |
|   0.05  | False     |       0.278712   |          0.0180361   |            0.0184647  |           0.0184647   |         0.00417882  |              0.00565067  |                  1 |
|   0.05  | True      |       0.174644   |          0.0701599   |            0.0377116  |           0.0260702   |         0.00847115  |              0.0133953   |                  1 |

## Overall clean reconstruction
- one-time mean state error: 0.111587
- history LS mean error: 0.00827736
- history robust mean error: 0.00834845

## Corrupted reconstruction
- history plain LS mean error: 0.0649087
- history robust mean error: 0.0195933
- diagnose+remove mean error: 0.0100555
- corrupted O5 identification accuracy: 100.000%
- repaired median energy relative error: 0.000831172
- repaired median action-vector relative error: 0.00246136

## Series-B interpretation
The observer map is now nonlinear:

y_i = h_i(z) + epsilon_i.

Global reconstruction is a robust nonlinear inverse problem:

G_provisional = argmin_z Sum_i,t rho(h_i(Phi_t z)-y_i,t).

Observer consistency is evaluated after constructing G_provisional.
The largest channel residual is treated as an observer-level anomaly candidate.
After excluding the suspect, a new global model is reconstructed.

This is a concrete implementation of:
local observation -> provisional globality -> observer consistency -> revised globality.

## Quantum-pretransition meaning
The architecture no longer depends on linear projections A_i z.
It already supports:
- many-to-one measurement maps,
- nonlinear local symmetries,
- stochastic observations,
- corrupted channels,
- robust global reconstruction.

A quantum version can replace h_i(z) by a measurement/channel map M_i(rho) without changing the conceptual Global/Embedded observer pipeline.
