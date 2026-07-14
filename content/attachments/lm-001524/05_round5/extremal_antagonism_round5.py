# Extremal Antagonism Round 5
#
# General connector form:
#   Z_t = K[X_[0,t]]
#   c_t = Phi(Z_t)
#
# Linear memory-kernel family:
#   Z_t = integral_0^t K(t-s) H(X_s) ds
#
# Special cases:
#   instantaneous: K(t-s)=delta(t-s)
#   integral:      K(t-s)=1
#   leaky:         K(t-s)=exp(-(t-s)/tau)
#   multiscale:    K(t-s)=sum_i a_i exp(-(t-s)/tau_i)
#
# Tests:
# 1. reversed histories with equal endpoint and equal total integral
# 2. closed-loop disturbance rejection and memory-unwinding costs
