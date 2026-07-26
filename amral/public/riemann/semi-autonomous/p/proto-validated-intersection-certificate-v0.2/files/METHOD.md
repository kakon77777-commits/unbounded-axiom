# Method

## 1. Piecewise-linear reconstruction

The v0.1 floating candidate is reconstructed on the exact uniform grid

\[
t_i=-3+\frac{i}{100},\qquad 0\le i\le600.
\]

The base ordinates are symmetrized decimal constants. The compact hat is

\[
\phi_h(t)=\max(1-|t|/h,0),\qquad h=0.01,
\]

and

\[
\psi(t)=\sum_i y_i\phi_h(t-t_i).
\]

Only the central ordinate is adjusted. If

\[
q_i=\int \phi_h(t-t_i)e^{-t/2}\,dt,
\]

then

\[
y_{300}=b_{300}-\frac{\sum_i b_iq_i}{q_{300}}.
\]

This defines the correction mathematically and forces \(G(i/2)=0\).

## 2. Closed Fourier transform

The Fourier transform of the hat is

\[
\Phi_h(w)=h\left(\frac{\sin(wh/2)}{wh/2}\right)^2.
\]

Therefore

\[
G(w)=\Phi_h(w)\sum_i y_i e^{iwt_i}.
\]

The verifier evaluates this finite exponential polynomial and its derivative with complex interval arithmetic.

## 3. Continuous rectangle certificate

For a cell centered at \(w_0\) with complex radius \(r\), Taylor's theorem gives

\[
G(w)=G(w_0)+G'(w_0)(w-w_0)+R_2,
\]

\[
|R_2|\le\frac12M_2r^2,
\]

where

\[
M_2\ge\sup_{w\in K}|G''(w)|
\]

is bounded directly from

\[
G''(w)=-\int t^2\psi(t)e^{iwt}\,dt.
\]

If \(G(w)\) lies in a disk of center \(c\) and radius \(\varepsilon\), then

\[
\operatorname{Re}(G(w)^2)
\le
\operatorname{Re}(c^2)+2|c|\varepsilon+\varepsilon^2.
\]

Cells that do not close are quartered recursively. The supplied run closes every cell.

## 4. Exact spline autocorrelation

Let

\[
r_k=\sum_i y_i y_{i+k}.
\]

The autocorrelation is

\[
C(x)=\sum_k r_k K_h(x-kh),
\]

where

\[
K_h(x)=h
\begin{cases}
\frac23-u^2+\frac12u^3,&0\le u\le1,\\
\frac16(2-u)^3,&1\le u\le2,\\
0,&u\ge2,
\end{cases}
\qquad u=|x|/h.
\]

Thus \(C\) is a compactly supported cubic spline and no FFT interpolation is used by v0.2.

## 5. Finite-place interval

Only prime powers satisfying

\[
m\log p<6
\]

are active. The exact interval argument

\[
m\,\operatorname{iv.log}(p)
\]

is passed to the cubic correlation enclosure. The finite term is

\[
Q_{\mathrm{fin}}
=
\sum_{m\log p<6}
-2(\log p)p^{-m/2}C(m\log p).
\]

## 6. Archimedean interval

The compact-support time-domain expression is

\[
Q_\infty
=-(\log(4\pi)+\gamma)C(0)
-\int_0^6
\frac{e^{x/2}C(x)-C(0)}{\sinh x}\,dx
-\log(\tanh3)C(0).
\]

The removable singularity on \([0,0.01]\) is rewritten using

\[
C(x)=C(0)+a_2x^2+a_3x^3.
\]

It is enclosed by direct interval subdivision.

The remaining integral is evaluated by composite midpoint intervals. If

\[
I(x)=\frac{e^{x/2}C(x)-C(0)}{\sinh x},
\]

then

\[
|C(x)|\le C(0),
\qquad
|C'(x)|\le\|\psi\|_2\|\psi'\|_2.
\]

On each chunk \([a,b]\), these give an analytic upper bound for \(|I'|\). The composite midpoint error is at most

\[
M_{a,b}(b-a)\Delta/4.
\]

The midpoint values themselves are interval evaluations.

## 7. Final conjunction

The certificate passes only if

\[
\sup_{w\in K}2\operatorname{Re}(G(w)^2)<0
\]

and

\[
\inf Q_{\mathrm{arith}}(\psi)>0.
\]
