# Extremal Antagonism Round 4
#
# Full local Markovian model:
#   dx/dt = p - m - Cmax*tanh(z) + u(t)
#   dp/dt = alpha(P_target(x)-p)
#   dm/dt = alpha(M_target(x)-m)
#   dz/dt = beta*x
#
# Exact elimination of z:
#   c(t)=Cmax*tanh(z0+beta*integral_0^t x(s)ds)
#
# Therefore the third channel can be eliminated only by adding
# explicit history dependence or increasing differential order.
# The supplied CSV files contain the complete numerical sweeps.
