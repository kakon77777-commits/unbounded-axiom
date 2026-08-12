# State–Law–Calibration Triangulation

## Goal
Infer simultaneously:
- hidden world state z0,
- shared physical-law parameters (wx, wy),
- observer calibration gains g_i.

The hidden true values are used only for final scoring.

## Key structural result: an exact calibration gauge

All observer channels in this experiment are homogeneous quadratic functions q_i(z).

Measurements are:
y_i(t)=g_i q_i(z(t)).

For any nonzero scale lambda:

z -> lambda z
g_i -> g_i / lambda^2

leaves every measurement exactly unchanged.

Measured numerical mismatch under lambda=1.7:
**6.661e-16**

But physical energy changes by:
E(lambda z)/E(z) = **2.89**

Therefore, with all sensor gains unknown, absolute state amplitude and absolute energy are not identifiable from these data.
This is not an optimizer failure; it is an exact gauge freedom of the observation model.

## Gauge family

|   lambda |   state_norm |   physical_energy |   mean_sensor_gain |   max_measurement_difference |
|---------:|-------------:|------------------:|-------------------:|-----------------------------:|
|     0.55 |     0.778789 |          0.410545 |           3.33333  |                  4.44089e-16 |
|     0.75 |     1.06199  |          0.76341  |           1.79259  |                  8.88178e-16 |
|     1    |     1.41598  |          1.35717  |           1.00833  |                  0           |
|     1.4  |     1.98237  |          2.66006  |           0.514456 |                  6.66134e-16 |
|     1.9  |     2.69036  |          4.8994   |           0.279317 |                  4.44089e-16 |

## Gauge fixing
Observer O1 is treated as a calibrated anchor with known gain g1=1.

Once that anchor is supplied, the remaining state, law parameters, and other gains become reconstructible in this benchmark.

## Trial sweep
36 trials:
noise sigma = 0, 0.005, 0.02.

O5 has a persistent +30% calibration drift on top of random sensor-gain variation.

|   sigma |   mean_state_err_nominal |   mean_state_err_joint |   mean_law_err_nominal |   mean_law_err_joint |   mean_gain_rel_rmse |   median_energy_rel_error |   mean_drift_gain_rel_error |   drift_identification_rate |
|--------:|-------------------------:|-----------------------:|-----------------------:|---------------------:|---------------------:|--------------------------:|----------------------------:|----------------------------:|
|   0     |                 1.27983  |               0.85424  |              0.0171512 |          7.92294e-12 |          1.60206e-11 |               2.69128e-14 |                 7.14093e-12 |                    0.916667 |
|   0.005 |                 1.38271  |               1.70226  |              0.0196664 |          0.00406654  |          0.0108117   |               0.00444705  |                 0.00714632  |                    0.75     |
|   0.02  |                 0.863363 |               0.587655 |              0.03946   |          0.0194376   |          0.0621106   |               0.0164105   |                 0.0485829   |                    0.75     |

Overall:
- nominal-calibration mean state error: 1.1753
- joint calibrated mean state error: 1.04805
- nominal-calibration mean law error: 0.0254259
- joint calibrated mean law error: 0.00783471
- mean gain relative RMSE: 0.0243074
- median energy relative error: 0.00209411

## Series-B interpretation

There are now four logically distinct unknowns:

1. State:
   which hidden world configuration is present?

2. Law:
   what shared dynamics generate the histories?

3. Observer:
   what local measurement channel is each observer using?

4. Gauge/anchor:
   which transformations of world state and observer calibration leave all observations invariant?

The fourth item is crucial.

A provisional global model is only defined up to the gauge freedoms left unbroken by the observer network.
A unique "global state" requires either:
- a calibrated reference observer,
- a known invariant/scale,
- an external standard,
- or some other gauge-fixing condition.

This is the first MVP showing that derived globality can itself have equivalence classes rather than a unique representative.

## Quantum-pretransition significance

The same structural issue will reappear whenever global state parameters and measurement-channel calibration are inferred jointly.

In a future quantum setting:
- state scale/gauge is replaced by the relevant quantum-state representation redundancies and tomography identifiability constraints;
- observer gains become measurement-channel calibration parameters;
- a "global quantum state" may only be identifiable relative to a calibrated measurement frame.

Series B therefore needs an explicit gauge/identifiability layer before entering quantum measurement theory.


## Residual discrete observer gauge after scale anchoring

Fixing one calibrated observer removes the continuous scale freedom

z -> lambda z,  g_i -> g_i/lambda^2,

but it does not remove every observer symmetry.

All channels in this benchmark are quadratic and therefore satisfy

q_i(z)=q_i(-z).

Hence z and -z remain exactly observationally indistinguishable even after the gain scale is anchored.

A follow-up benchmark gave:
- mean raw state error: 1.11298
- mean state error modulo the Z2 equivalence z~ -z: 0.0113683
- improvement factor after quotienting the unobservable sign gauge: 97.9x

Therefore the physically/observationally meaningful reconstructed object in this benchmark is not a unique vector z, but the equivalence class

[z] = {z,-z}.

This is a decisive Series-B result:
a derived global state may only exist uniquely in the quotient by observer-invisible gauge transformations.
