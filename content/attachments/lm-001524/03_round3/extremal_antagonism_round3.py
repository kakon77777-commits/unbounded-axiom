# Extremal Antagonism Round 3
# See generated CSV files for full Monte Carlo and covariance results.
# Core equations:
#
# dx = (p - m - gamma*x + b)dt + sigma_x dW_x
# dp = alpha(Amax*sigmoid(mu-k*x)-p)dt + sigma_d dW_p
# dm = alpha(Amax*sigmoid(mu+k*x)-m)dt + sigma_d dW_m
#
# Failure when |x| exceeds a specified survival boundary.
#
# Linearized stationary covariance:
# J Sigma + Sigma J^T + Q = 0
#
# The experiment compares reserve capacity and connection feedback
# near the saturation boundary.
