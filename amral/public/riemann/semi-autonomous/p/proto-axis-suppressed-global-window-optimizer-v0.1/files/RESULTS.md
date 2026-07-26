# RESULTS

## Arithmetic-positive dimension versus annihilation count

| q | Reduced dimension | Positive directions | Maximum arithmetic eigenvalue |
|---:|---:|---:|---:|
| 0 | 22 | 12 | 5.89381875 |
| 4 | 18 | 8 | 0.42111899 |
| 8 | 14 | 4 | 0.00290303 |
| 10 | 12 | 2 | 0.00203168 |
| 12 | 10 | 1 | 0.00119356 |
| 15 | 7 | 0 | -0.00014260 |

At `q=15`, this basis contains no arithmetic-positive direction after the
finite axis constraints are applied.

## Selected q=12 candidate

\[
\max_{w\in K_{\rm target}}B(w)
\approx -2.64607989612e-08,
\]

\[
Q_{\rm arith}
\approx 5.00000000001e-05,
\]

\[
\sum_{n=13}^{50}|G(\gamma_n)|^2
\approx 0.000154365729672.
\]

The finite-window maximum remains positive:

\[
\max_{w\in W_{\rm control}}B(w)
\approx 0.267543612562.
\]

The remaining measured axis prefix is about `5833.75` times the target
negative margin. The largest control-window peak is about
`1.011e+07` times that margin.

## Interpretation

Increasing `q` lowers measured axis leakage, but it also collapses the
arithmetic-positive subspace and weakens phase-shaping freedom.

The current 24-bump model did not produce simultaneous:

\[
B<0\text{ on the target},\qquad
B\le0\text{ on the whole control window},\qquad
Q_{\rm arith}>0.
\]
