import numpy as np
from scipy.integrate import solve_ivp

A_max = 100.0
alpha = 1.0
k = 1.0

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

def rhs(t, y, mu, gamma):
    x, p, m = y
    p_target = A_max * sigmoid(mu - k*x)
    m_target = A_max * sigmoid(mu + k*x)
    return [
        p - m - gamma*x,
        alpha*(p_target - p),
        alpha*(m_target - m),
    ]

def jacobian(mu, gamma):
    s = sigmoid(mu)
    slope = A_max*k*s*(1-s)
    return np.array([
        [-gamma, 1.0, -1.0],
        [-alpha*slope, -alpha, 0.0],
        [ alpha*slope, 0.0, -alpha],
    ])

for mu in [0, 2, 4, 6, 8, 10]:
    chi = sigmoid(mu)
    eig = np.linalg.eigvals(jacobian(mu, gamma=0.0))
    print(mu, chi, eig)
