# Joint World–Law Reconstruction

## Goal
Embedded observers do not know:
1. the hidden global state z0;
2. the physical-law parameters wx, wy.

They receive only nonlinear noisy local measurements.

The simulator retains the true state and true law only for final scoring.

## Model
Hidden dynamics:
anisotropic 2D harmonic oscillator.

Unknown parameter vector:
p=(x0,y0,vx0,vy0,wx,wy).

Observers:
six nonlinear channels h_i(z).

Joint provisional global model:
p_hat = argmin_p Sum_i,t rho(h_i(Phi_t(p) z0)-y_i,t).

## Scenarios
A. Law-shift only:
true frequencies differ from a fixed nominal law.

B. Law-shift + local observer corruption:
O5 also receives a persistent measurement bias.

Noise levels:
0, 0.005, 0.02, 0.05.

Total trials:
112.

## Aggregate results

|   sigma | corrupt   |   mean_state_err_nominal |   mean_state_err_joint |   mean_state_err_repaired |   mean_law_err_nominal |   mean_law_err_joint |   mean_law_err_repaired |   median_Eerr_repaired |   mean_residual_contrast |   suspect_accuracy |
|--------:|:----------|-------------------------:|-----------------------:|--------------------------:|-----------------------:|---------------------:|------------------------:|-----------------------:|-------------------------:|-------------------:|
|   0     | False     |                 0.376607 |             0.168439   |                0.168439   |               0.265692 |           0.0295156  |              0.0295156  |            5.16657e-16 |                 0.605251 |           1        |
|   0     | True      |                 0.32349  |             0.0186069  |                0.188151   |               0.279915 |           0.0300146  |              0.0238635  |            9.42527e-15 |                48.5441   |           0.714286 |
|   0.005 | False     |                 0.236892 |             0.00368274 |                0.00368274 |               0.26123  |           0.00370181 |              0.00370181 |            0.000911743 |                 1.31782  |           1        |
|   0.005 | True      |                 0.449862 |             0.234302   |                0.0908784  |               0.28797  |           0.0794489  |              0.0269117  |            0.00198559  |                26.3418   |           0.5      |
|   0.02  | False     |                 0.165204 |             0.101778   |                0.101778   |               0.225407 |           0.0321819  |              0.0321819  |            0.00433929  |                 1.74074  |           1        |
|   0.02  | True      |                 0.249059 |             0.472553   |                0.0139499  |               0.272488 |           0.056334   |              0.0219181  |            0.00296353  |                11.3171   |           0.785714 |
|   0.05  | False     |                 0.322888 |             0.030797   |                0.030797   |               0.243209 |           0.0579571  |              0.0579571  |            0.0110168   |                 1.25422  |           1        |
|   0.05  | True      |                 0.215885 |             0.0463468  |                0.264965   |               0.218228 |           0.0461948  |              0.0537954  |            0.00893146  |                 4.96593  |           0.571429 |

## Clean law-shift cases
Wrong fixed nominal law:
- mean state error = 0.275398
- mean law-parameter error = 0.248885

Joint state+law inference:
- mean state error = 0.0761743
- mean law-parameter error = 0.0308391
- median law-parameter error = 0.00626034

Interpretation:
a globally shared mismatch across observer histories is absorbed by changing the inferred world law rather than blaming one local observer.

## Corrupted observer cases
Before observer repair:
- mean joint state error = 0.192952
- mean joint law error = 0.0529981

Observer diagnosis:
- O5 identification accuracy = 64.286%

After removing the suspect and refitting state+law:
- mean state error = 0.139486
- mean law error = 0.0316222
- median energy relative error = 0.00239191

## Series-B interpretation

There are now three distinct defect hypotheses:

1. State defect:
   the current hidden state estimate is wrong.

2. World-law defect:
   the shared dynamics parameters are wrong.
   Evidence appears coherently across many observers and many times.

3. Observer defect:
   one local channel remains inconsistent after the shared law is re-estimated.

The inference loop is:

local observations
-> provisional state+law model
-> cross-observer residual pattern
-> classify global-law vs local-observer mismatch
-> reweight/remove observer if needed
-> reconstruct revised global model.

This is the first Series-B MVP where "world model" and "observer model" are inferred simultaneously rather than assumed.

## Quantum-pretransition significance
A future quantum version can replace:
- classical state z by density operator rho or another global quantum description;
- parameters (wx,wy) by Hamiltonian/channel parameters theta;
- nonlinear h_i by quantum measurement maps M_i.

The structural inference problem remains:
jointly infer global state, shared law, and observer/channel calibration while separating global anomalies from local measurement defects.


## Diagnostic refinement after the first benchmark

The first leave-one-observer-out diagnostic identified corrupted O5 in only 64.29% of corrupted trials, below the predeclared 75% target.

A second diagnostic was then tested:

1. jointly refit the shared hidden state and shared physical-law parameters using all observers;
2. compute each observer's residual against that shared provisional world-law model;
3. classify the observer with the largest remaining local residual as the fault candidate.

This improved corrupted-O5 identification to:

**91.07%**

A benchmark-tuned hybrid rule combining residual contrast with the original leave-one-out score reached:

**92.86%**

at a residual-contrast threshold of 4.0.

The 92.86% number is benchmark-tuned and should not be treated as a general theorem or deployable threshold. The more important structural result is that residual localization after shared-law refitting substantially outperformed the original leave-one-out method.

Interpretation:
when the physical law is also unknown, a wrong global law can partially absorb a local observer bias. The correct diagnostic order is therefore:

shared state+law inference
-> residual localization
-> observer-fault hypothesis
-> refit without/reweight suspect.

This is a genuine separation problem between:
- state defect,
- shared world-law defect,
- local observer defect.
