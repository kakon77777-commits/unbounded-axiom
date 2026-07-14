import numpy as np
from scipy.integrate import solve_ivp

A = 100.0
alpha = 1.2
k = 2.0

def rhs(t, y):
    x, p, m = y
    return [
        p - m,
        alpha * (A - k*x - p),
        alpha * (A + k*x - m),
    ]

y0 = [3.0, 20.0, 150.0]
t_eval = np.linspace(0.0, 20.0, 2001)
sol = solve_ivp(rhs, (0.0, 20.0), y0, t_eval=t_eval,
                rtol=1e-10, atol=1e-12)

x, p, m = sol.y
J = p - m
Theta = p + m

jacobian = np.array([
    [0.0, 1.0, -1.0],
    [-alpha*k, -alpha, 0.0],
    [alpha*k, 0.0, -alpha],
])
print("eigenvalues:", np.linalg.eigvals(jacobian))
print("final x:", x[-1])
print("final net drive:", J[-1])
print("final total intensity:", Theta[-1])
