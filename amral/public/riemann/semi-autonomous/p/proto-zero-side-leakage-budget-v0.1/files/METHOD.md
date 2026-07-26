# METHOD

The zero side is split schematically as

\[
Q_{\rm zero}
=Q_{\rm target}+Q_{\rm axis}+Q_{\rm finite,off}+Q_{\rm tail}.
\]

The existing validated certificate controls only \(Q_{\rm target}\).

For the same explicit piecewise-linear test function, this package evaluates
\(|G(\gamma_n)|^2\) at the first critical-line zeros and constructs a tail
majorant from

\[
|G(t)|\le \frac{\operatorname{TV}(\psi')}{t^2}.
\]

A unit-height zero-count majorant is generated from the
Riemann--von Mangoldt decomposition and the explicit bound

\[
|S(T)|\le 0.111\log T+0.275\log\log T+2.450
\quad(T\ge e).
\]

The finite-window unknown off-axis budget uses the unconditional strip bound

\[
|G(x+iy)|
\le \int |\psi(t)|e^{|y||t|}\,dt.
\]

This bound is intentionally conservative. It exposes the scale mismatch rather
than pretending that leakage has been solved.
