# Stationary action basic verification
#
# Harmonic oscillator:
#   L = 1/2 m qdot^2 - 1/2 k q^2
#
# Discrete action:
#   S = sum_n [m/2 ((q[n+1]-q[n])/dt)^2
#              - k/4 (q[n]^2+q[n+1]^2)] dt
#
# The interior gradient condition grad S=0 is equivalent to:
#   m(q[n+1]-2q[n]+q[n-1])/dt^2 + k q[n] = 0
#
# The code verifies:
# 1. discrete stationary path = analytic Euler–Lagrange path
# 2. kinetic and potential variational contributions cancel
# 3. the stationary path is a minimum for T<pi/omega
# 4. it becomes a saddle for T>pi/omega
#
# See the generated CSV and PNG files for numerical results.
