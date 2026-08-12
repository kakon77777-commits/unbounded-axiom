# Collective Embedded AI Physics MVP

## Goal
Test whether individually incomplete embedded observers can collectively reconstruct a global physical state, and whether the collective can identify a corrupted observer instead of misclassifying its inconsistency as a physical anomaly.

## Global system
2D isotropic oscillator, state:
z=(x,y,vx,vy)

Global reference state at t*=1.17:
z_true = [0.3286279353933152, 0.7842920204262449, -1.540644741442272, 0.6365393822190147]

Global invariants at t*:
- E = 3.40070125
- Lz = 2.40975

## 1. Static collective accessibility

| coalition   |   num_observers |   num_measurements |   joint_rank |   joint_nullity |
|:------------|----------------:|-------------------:|-------------:|----------------:|
| O1          |               1 |                  2 |            2 |               2 |
| O2          |               1 |                  2 |            2 |               2 |
| O3          |               1 |                  2 |            2 |               2 |
| O4          |               1 |                  2 |            2 |               2 |
| O1+O2       |               2 |                  4 |            3 |               1 |
| O1+O3       |               2 |                  4 |            3 |               1 |
| O2+O3       |               2 |                  4 |            4 |               0 |
| O1+O2+O3    |               3 |                  6 |            4 |               0 |
| All4        |               4 |                  8 |            4 |               0 |

Key result:
- every individual observer has rank 2/4;
- O1+O2 and O1+O3 remain rank 3/4;
- O2+O3 already reaches rank 4/4;
- therefore collective access can be complete even when every individual access map is incomplete.

## 2. Noisy one-shot reconstruction

| coalition   |   joint_rank |   state_error |   measurement_residual |   energy_rel_error |   Lz_rel_error |
|:------------|-------------:|--------------:|-----------------------:|-------------------:|---------------:|
| O1          |            2 |    1.66712    |            0           |         0.706809   |    1           |
| O2          |            2 |    1.01023    |            0           |         0.348967   |    1           |
| O3          |            2 |    1.57533    |            0           |         0.64517    |    1           |
| O4          |            2 |    0.716049   |            4.96507e-16 |         0.148986   |    0.155254    |
| O1+O2       |            3 |    0.638615   |            0.00993146  |         0.0491857  |    0.0845296   |
| O1+O3       |            3 |    1.54082    |            0.0264414   |         0.590677   |    0.858325    |
| O2+O3       |            4 |    0.0258517  |            0           |         0.00497295 |    0.017061    |
| O1+O2+O3    |            4 |    0.0236704  |            0.0114094   |         0.0248193  |    0.0267345   |
| All4        |            4 |    0.00816103 |            0.0165126   |         0.00306903 |    0.000430978 |

Interpretation:
full-rank coalitions reconstruct hidden state and global invariants substantially better than rank-deficient individuals.

## 3. Dynamic observability

| case              |   num_times |   num_rows |   observability_rank |   nullity |   condition_number |
|:------------------|------------:|-----------:|---------------------:|----------:|-------------------:|
| O1 @ one instant  |           1 |          2 |                    2 |         2 |          nan       |
| O1 @ two instants |           2 |          4 |                    4 |         0 |            4.39343 |
| O2 @ one instant  |           1 |          2 |                    2 |         2 |          nan       |
| O2 @ two instants |           2 |          4 |                    2 |         2 |          inf       |
| O4 @ one instant  |           1 |          2 |                    2 |         2 |          nan       |
| O4 @ two instants |           2 |          4 |                    4 |         0 |            4.58304 |

Most important case:
O1 sees only position (x,y), rank 2 at one instant.
At two separated times, the stacked observation matrix reaches rank 4.

Therefore:
instantaneous non-identifiability != historical non-identifiability.

History acts as an information source.

## 4. Position-only reconstruction from history

|   num_time_samples |   observability_rank |   z0_reconstruction_error |   measurement_residual |
|-------------------:|---------------------:|--------------------------:|-----------------------:|
|                  1 |                    2 |                 1.107     |            0           |
|                  2 |                    4 |                 0.0337681 |            2.48253e-16 |
|                  3 |                    4 |                 0.016588  |            0.00375441  |
|                  5 |                    4 |                 0.0643147 |            0.0420169   |
|                  9 |                    4 |                 0.0112232 |            0.0705396   |

The same Embedded AI can move from incomplete to effectively global reconstruction by accumulating time-indexed observations, without changing its instantaneous sensor.

## 5. Corrupted observer experiment

O4 was intentionally biased by:
bias = [0.22, -0.18]

Using all observers blindly:
- global measurement residual = 0.170362645501
- state error = 0.105579596771
- energy relative error = 0.111949020891
- Lz relative error = 0.125802823783

Leave-one-observer-out diagnostics:

| excluded_observer   |   prediction_residual_on_excluded |   fit_residual_on_kept |   state_error |
|:--------------------|----------------------------------:|-----------------------:|--------------:|
| O1_pos              |                         0.0903358 |             0.151355   |      0.122748 |
| O2_xvx              |                         0.189407  |             0.123866   |      0.199337 |
| O3_yvy              |                         0.191601  |             0.121738   |      0.184382 |
| O4_diag             |                         0.260784  |             0.00376227 |      0.016018 |

Detected suspect:
**O4_diag**

After excluding the suspect:
- repaired state error = 0.0160179980539
- repaired energy relative error = 0.000383791338078
- repaired Lz relative error = 0.00169438987011

This demonstrates a key Series-B use:
an observer inconsistency can be localized at the network level before being interpreted as a failure of the underlying physical law.

## 6. Interpretation in Global/Embedded language

Global Reference AI:
- knows z_true directly.

Embedded observer O_i:
- knows A_i z.

Collective observer network:
A_collective = stack(A_i)

If rank(A_collective)=4, the network can reconstruct the 4D state even though every individual A_i is non-injective.

Dynamic observer:
A_history = stack(A_i Phi(t_k))

Even one rank-deficient observer can become globally observable when A_history reaches full rank.

Corrupted observer:
network consistency residuals reveal that one local channel is incompatible with the rest.

## Proposed observer-gap decomposition

Delta_G->i:
- instantaneous access gap
- dynamic observability gap
- reconstruction error
- invariant-estimation gap

Delta_network:
- joint-rank deficit
- coalition reconstruction error
- observer consistency residual
- corruption/localization score
- global invariant residual after fusion

## Conclusion
The classical MVP supports the following claim:

"Individual embedded observers can be informationally incomplete while an observer collective is globally reconstructive; time history and inter-observer communication are two distinct mechanisms that can close the Global–Embedded gap."

It also supports:
"Apparent physical-law violations should be tested against observer-network inconsistency before being classified as global physical anomalies."
