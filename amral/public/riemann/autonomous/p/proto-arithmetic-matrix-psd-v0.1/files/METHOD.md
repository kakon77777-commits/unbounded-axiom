# Method and audit boundary

## 1. Unitized logarithmic coordinate

The package works with a real even compactly supported function \(\psi\) on the additive logarithmic line:

\[
G(t)=\int_{\mathbb R}\psi(x)e^{itx}\,dx.
\]

The basis consists of normalized pairs of smooth translated bumps.

## 2. Correlation matrix field

For basis functions \(\psi_j\), define

\[
C_x(j,k)=\frac12\int_{\mathbb R}
\bigl(\psi_j(u)\psi_k(u-x)+\psi_k(u)\psi_j(u-x)\bigr)\,du.
\]

For \(\operatorname{supp}\psi_j\subset[-R,R]\), one has \(C_x=0\) for \(|x|\ge 2R\). The implementation computes the complete lag grid by FFT correlation and linearly interpolates only when a prime-power location does not coincide with the grid.

## 3. Archimedean matrix: primary time-domain form

After imposing \(G(\pm i/2)=0\), the pole terms in the additive explicit formula vanish. For an even convolution square, the implemented archimedean matrix is

\[
M_\infty
=-(\log(4\pi)+\gamma)C_0
-\int_0^{2R}
2\bigl(C_x-e^{-x/2}C_0\bigr)
\frac{e^{x/2}}{e^x-e^{-x}}\,dx
-\log(\tanh R)\,C_0.
\]

The last displayed term is the analytically integrated contribution from \(x>2R\). Since \(\log(\tanh R)<0\), this contribution is positive.

At \(x=0\), the integrand is assigned its removable-limit value \(C_0/2\).

This compact time-domain formula is the primary computation used for eigenvalues and PSD classification.

## 4. Spectral cross-check

The package separately evaluates the truncated spectral expression

\[
\frac1{2\pi}\int_{-T}^{T}
\left[
\Re\operatorname{digamma}\left(\frac14+\frac{it}{2}\right)-\log\pi
\right]
G_j(t)\overline{G_k(t)}\,dt.
\]

The operator-norm difference from the time-domain matrix is reported as `archimedean_spectral_crosscheck_norm`. It is only a diagnostic of the finite spectral cutoff and does not affect the PSD result.

## 5. Finite-place matrix

For each activated prime power \(p^m\) with \(m\log p<2R\), the contribution in the chosen \(Q_\zeta\) convention is

\[
M_{p,m}
=-2(\log p)p^{-m/2}C_{m\log p}.
\]

The activation set is finite for every fixed \(R\).

## 6. Constraint projection

The matrix is compressed to the nullspace of the evaluation rows at \(i/2\) and, by default, at \(0\):

\[
G(i/2)=0,
\qquad G(0)=0.
\]

The first removes the explicit-formula endpoint terms. The second connects the prototype to the known small-support archimedean positivity setup.

## 7. What is structural and what remains numerical

Structural in the chosen convention:

- the prime-power activation threshold;
- the coefficient \(-2(\log p)p^{-m/2}\);
- the compact-support archimedean formula;
- the endpoint and central linear constraints;
- symmetry of the bilinear matrices.

Numerical only:

- discretized bump functions and correlations;
- quadrature on \([0,2R]\);
- interpolation at \(m\log p\);
- nullspace and eigenvalue calculations;
- the final PSD classification.

## 8. v0.2 target

- interval enclosure of the correlation field \(C_x\);
- interval quadrature for the removable-singularity archimedean kernel;
- rational or interval \(LDL^T\) certificates;
- common basis import from the phase-shaping package;
- direct feasibility tests combining regional negativity and arithmetic positivity.
