# Method

## 1. Target and adaptive cover

The mother window is

$$
K=[20,20.5]\times[-0.2,-0.1].
$$

The cover is stratified by distance to the symmetry axis. The two farther
strata use height windows of width $0.20$; the two nearer strata use height
windows of width $0.10$. Adjacent windows overlap.

The exact-cover audit uses rational breakpoints. It checks every atomic
two-dimensional cell and every boundary probe induced by those breakpoints,
then independently checks a $501\times301$ grid.

## 2. Rank-one candidates

Let $\psi_r$ be real, even, and supported in $[-3,3]$, with transform

$$
G_r(w)=\int_{-3}^{3}\psi_r(t)e^{iwt}\,dt.
$$

Each candidate satisfies the structural constraints

$$
G_r(0)=G_r(i/2)=0,
$$

and is normalized by

$$
\langle \psi_r,\psi_r\rangle_{C_0}=1.
$$

The off-axis orbit block is

$$
B_r(w)=2\operatorname{Re}\!\left(G_r(w)^2\right).
$$

On the real axis, $G_r(t)$ is real and therefore

$$
B_r(t)=2G_r(t)^2\ge 0.
$$

The arithmetic scalar is evaluated by the inherited quadratic matrix:

$$
q_r=Q_{\mathrm{arith}}(\psi_r).
$$

Every retained candidate is constrained by

$$
q_r\ge 5\times10^{-5}.
$$

## 3. No zero-ordinate fitting

The optimizer does not impose $G_r(\gamma_n)=0$ and does not evaluate any
individual $\gamma_n$ while generating candidates.

Instead it uses the continuous real-axis energy proxy

$$
E_r
=
\sum_{I\in\mathcal I}
\int_I |G_r(t)|^2
\left(1+\frac{\log(1+t)}{2\pi}\right)\,dt,
$$

with

$$
\mathcal I=\{[14,35],[35,70],[70,145]\}.
$$

The first 50 ordinates are loaded only after candidate generation and are
reported as a holdout diagnostic.

## 4. Penalized local minimax search

For each seed patch and penalty $\mu$, the floating QCQP is

$$
\min_{y,\tau}
\left[
\tau
+\mu\frac{y^\mathsf{T}Ey}{\operatorname{tr}(E)/d}
\right],
$$

subject to

$$
\|y\|_2=1,
\qquad
y^\mathsf{T}Qy\ge 5\times10^{-5},
$$

and

$$
y^\mathsf{T}M(w)y\le\tau
\quad
\text{on the seed grid}.
$$

The penalty schedule is

$$
\mu\in\{0,1.5\times10^{-4},2\times10^{-4},2.5\times10^{-4}\}.
$$

Eighteen patches times four penalties produce 72 rank-one candidates.

## 5. Nonnegative conic aggregation

For a patch $\alpha$, use

$$
f_{\alpha,\lambda}
=
\sum_r\lambda_r f_r,
\qquad
\lambda_r\ge0.
$$

Then

$$
B_{\alpha,\lambda}(w)
=
\sum_r\lambda_r B_r(w),
$$

and

$$
Q_{\mathrm{arith}}(f_{\alpha,\lambda})
=
\sum_r\lambda_r q_r.
$$

Thus real-axis nonnegativity and arithmetic positivity are preserved without
introducing quadratic cross terms.

Stage one minimizes real-axis band energy under unit target negativity:

$$
\min_{\lambda\ge0}\sum_r\lambda_r E_r
$$

subject to

$$
\sum_r\lambda_r B_r(w)\le-1
\quad(w\in K_\alpha^{\mathrm{active}})
$$

and

$$
\sum_r\lambda_r q_r\ge10^{-3}.
$$

Stage two allows an energy slack $\sigma=0.05$ and minimizes the positive
guard peak $u$:

$$
\sum_r\lambda_r E_r\le(1+\sigma)E_\alpha^\star,
$$

$$
\sum_r\lambda_r B_r(w)\le u
\quad(w\in W_\alpha\setminus K_\alpha).
$$

An exchange loop inserts a worst dense-core point if the active constraints
miss it.

## 6. Diagnostics

After optimization, the following quantities are evaluated:

$$
Z_{50}
=
\sum_r\lambda_r\sum_{n=1}^{50}|G_r(\gamma_n)|^2,
$$

the guard positive maximum, and a prototype tail bound based on

$$
|G_r(t)|
\le
\frac{\operatorname{TV}(\psi_r')}{t^2}.
$$

The crude continuous sign audit uses

$$
|\nabla B_r(w)|
\le
4e^{2R|y|}
\|\psi_r\|_1
\|t\psi_r\|_1.
$$

These are floating quadrature and floating linear-algebra computations. They
are not interval enclosures.
